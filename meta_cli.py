"""CLI for the Meta automation hub — mainly the scheduled-post queue runner.

Usage:
    python meta_cli.py schedule-ahead       # hand upcoming FB items to Meta to publish
    python meta_cli.py run-queue            # post everything due in queue.json
    python meta_cli.py run-queue --dry-run  # show what would post, change nothing
    python meta_cli.py list-queue           # show queue with status

queue.json format (times are ISO-8601; naive = local time):
    {"items": [
      {"id": "unique-slug",
       "account": "zelobiz",
       "network": "facebook" | "instagram",
       "type": "link" | "photo" | "image" | "carousel" | "reel",
       "message": "caption/message text",
       "link": "https://... (facebook link posts)",
       "image_url": "https://... (photo/image) OR",
       "image_urls": ["...", "..."] (carousel),
       "video_url": "https://... (IG reel — must be a public URL IG can fetch),
       "video_path": "images/reels/x.mp4 (FB reel — local file if present)",
       "video_src": "https://... (FB reel — release URL, used when the file is absent)",
       "when": "2026-07-14T09:00:00",
       "status": "pending"}
    ]}

The runner posts every 'pending' item whose 'when' is in the past, then writes
status posted/failed + the API result back into queue.json. Wire run-queue.ps1
into Windows Task Scheduler (e.g. every 15 minutes) for hands-off scheduling.
"""

import collections
import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

_HERE = Path(__file__).parent
QUEUE_FILE = _HERE / "queue.json"
COMMENTS_FILE = _HERE / "comments.json"

sys.path.insert(0, str(_HERE))
import meta_mcp_server as meta  # reuse _api/_cfg/_ig_id and the accounts config
import publish_reel  # FB reels need the 3-phase video_reels upload, not fb_post*
import video_store  # reel mp4s live in a GitHub release, not in this repo


def _due(item) -> bool:
    when = datetime.fromisoformat(item["when"])
    if when.tzinfo is None:
        when = when.astimezone()
    return when <= datetime.now().astimezone()


def _post(item) -> dict:
    acct = item.get("account", "")
    net, typ = item["network"], item.get("type", "link")
    msg = item.get("message", "")
    geo = item.get("geo_countries", "")
    if net == "facebook":
        if typ == "photo":
            img = item.get("image") or item["image_url"]  # URL or local path
            r = json.loads(meta.fb_post_photo(img, msg, geo_countries=geo,
                                              account=acct))
        elif typ == "reel":
            r = publish_reel.publish(acct, video_store.resolve(item), msg)
        else:  # "link" / "text"
            r = json.loads(meta.fb_post(msg, item.get("link", ""),
                                        geo_countries=geo, account=acct))
        fc = item.get("first_comment")
        if fc:
            post_id = r.get("post_id") or r["id"]
            try:
                c = meta._api("POST", f"{post_id}/comments", account=acct,
                              payload={"message": fc})
                r["first_comment_id"] = c.get("id")
            except Exception as e:  # comment failure shouldn't fail the post
                r["first_comment_error"] = str(e)[:200]
        return r
    if net == "instagram":
        if typ == "carousel":
            return json.loads(meta.ig_post_carousel(item["image_urls"], msg, account=acct))
        if typ == "reel":
            return json.loads(meta.ig_post_reel(item["video_url"], msg,
                                                item.get("cover_url", ""), account=acct))
        return json.loads(meta.ig_post_image(item["image_url"], msg, account=acct))
    raise RuntimeError(f"unknown network {net!r}")


# GitHub's scheduled workflows are best-effort, not punctual: the "hourly" cron
# here actually fires with 3-6h gaps. Every item that came due in the gap is
# then posted back-to-back, which is how health-daily ended up publishing SIX
# posts inside one clock hour — a whole day's cadence in one burst, on a page
# whose engagement problem was already diagnosed as burst posting.
#
# Capping per account per run turns a catch-up into a drip: the overflow stays
# pending and goes out on the next run instead of all at once. The cap is per
# ACCOUNT, not global, so one busy page can't starve the others.
MAX_PER_ACCOUNT_PER_RUN = 3


def run_queue(dry_run: bool, max_per_account: int = MAX_PER_ACCOUNT_PER_RUN) -> None:
    q = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    due = [i for i in q["items"] if i.get("status") == "pending" and _due(i)]
    if not due:
        print("Nothing due.")
        return

    due.sort(key=lambda i: i["when"])  # oldest first, so nothing starves
    taken, held = [], collections.Counter()
    for item in due:
        acct = item.get("account") or meta.DEFAULT_ACCOUNT
        if max_per_account and sum(1 for t in taken
                                   if (t.get("account") or meta.DEFAULT_ACCOUNT) == acct
                                   ) >= max_per_account:
            held[acct] += 1
            continue
        taken.append(item)
    if held:
        print("held for next run (per-account cap "
              f"{max_per_account}): " + ", ".join(f"{a}:{n}" for a, n in held.items()))
    due = taken

    for n, item in enumerate(due):
        label = f"{item['id']} [{item['network']}/{item.get('type')}] -> {item.get('account') or meta.DEFAULT_ACCOUNT}"
        if dry_run:
            print("WOULD POST:", label)
            continue
        if n:  # pace writes — bursts previously tripped Meta's abuse block
            time.sleep(8)
        try:
            result = _post(item)
            item["status"] = "posted"
            item["result"] = result
            item["posted_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
            print("POSTED:", label, "->", result)
        except Exception as e:  # keep going; record the failure
            item["status"] = "failed"
            item["error"] = str(e)
            print("FAILED:", label, "->", e)
    if not dry_run:
        QUEUE_FILE.write_text(json.dumps(q, indent=2, ensure_ascii=False),
                              encoding="utf-8")


def run_comments(dry_run: bool) -> None:
    """Deliver queued first-comments once their (FB-native-scheduled) post is live.
    comments.json items: {photo_id, when (ISO, = post publish time), message,
    account, status}. Retries until 24h past 'when', then marks failed."""
    if not COMMENTS_FILE.is_file():
        return
    q = json.loads(COMMENTS_FILE.read_text(encoding="utf-8"))
    due = [i for i in q["items"] if i.get("status") == "pending" and _due(i)]
    if not due:
        return
    changed = False
    for item in due:
        label = f"comment on {item['photo_id']}"
        if dry_run:
            print("WOULD COMMENT:", label)
            continue
        try:
            r = meta._api("POST", f"{item['photo_id']}/comments",
                          account=item.get("account", ""),
                          payload={"message": item["message"]})
            item["status"] = "posted"
            item["result"] = r
            changed = True
            print("COMMENTED:", label, "->", r.get("id"))
        except Exception as e:
            when = datetime.fromisoformat(item["when"])
            if when.tzinfo is None:
                when = when.astimezone()
            age_h = (datetime.now().astimezone() - when).total_seconds() / 3600
            if age_h > 24:
                item["status"] = "failed"
                item["error"] = str(e)
                changed = True
                print("FAILED (gave up):", label, "->", e)
            else:
                print("NOT READY (will retry):", label, "->", str(e)[:120])
    if changed and not dry_run:
        COMMENTS_FILE.write_text(json.dumps(q, indent=2, ensure_ascii=False),
                                 encoding="utf-8")


def list_queue() -> None:
    q = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    for i in q["items"]:
        print(f"{i.get('status','?'):8} {i['when']}  {i['id']}  "
              f"[{i['network']}/{i.get('type')}] {i.get('account','(default)')}")
    if not q["items"]:
        print("Queue is empty.")


# ---------------------------------------------------------------- scheduling
# GitHub's cron is not punctual: measured gaps of 3-6h, and one stretch where
# nothing ran for 3.5h and 24 items went overdue. While the runner is the thing
# that must be awake at the exact minute, the posting schedule can only ever be
# as reliable as GitHub's scheduler.
#
# So hand the timing to Meta instead. Facebook accepts scheduled_publish_time on
# feed posts, photos and reels, and publishes them itself at the exact minute.
# The cron then only has to run SOMETIME in a multi-day window to hand work over
# in advance — a 4-hour gap stops mattering.
#
# Instagram has no equivalent (its containers expire in 24h and still need an
# explicit publish call), so IG items keep going through run_queue.
SCHEDULE_MIN_LEAD = timedelta(minutes=20)   # Meta's floor is 10 min; leave margin
# Meta's ceiling is 75 days, but handing over a month at once FREEZES the queue:
# a scheduled post is committed at that minute, so any later reschedule (e.g.
# re-laying reels onto the 6/day grid) would be silently ignored by Facebook
# while the local queue looked correct. A short horizon keeps the queue editable
# and still removes the dependency on GitHub being punctual — the cron only has
# to run once every few days to stay ahead.
SCHEDULE_HORIZON = timedelta(days=7)
SCHEDULE_MAX_PER_RUN = 40   # each reel is a full video upload; don't marathon


def _schedule_one(item) -> dict:
    """Hand one Facebook item to Meta with a scheduled publish time."""
    acct = item.get("account", "")
    typ = item.get("type", "link")
    msg = item.get("message", "")
    geo = item.get("geo_countries", "")
    when = item["when"]

    if typ == "reel":
        ts = datetime.fromisoformat(when)
        if ts.tzinfo is None:
            ts = ts.astimezone()
        return publish_reel.publish(acct, video_store.resolve(item), msg,
                                    schedule_ts=int(ts.timestamp()))
    if typ == "photo":
        img = item.get("image") or item["image_url"]
        return json.loads(meta.fb_post_photo(img, msg, schedule=when,
                                             geo_countries=geo, account=acct))
    return json.loads(meta.fb_post(msg, item.get("link", ""), schedule=when,
                                   geo_countries=geo, account=acct))


def _queue_first_comment(item, result) -> None:
    """A scheduled post isn't live yet, so its first comment can't be posted now.
    Hand it to comments.json, which already exists to deliver comments once a
    natively-scheduled post goes live."""
    fc = item.get("first_comment")
    if not fc:
        return
    target = (result.get("post_id") or result.get("id")
              or result.get("video_id"))
    if not target:
        print(f"  (no id to comment on for {item['id']})")
        return
    existing = ({"items": []} if not COMMENTS_FILE.is_file()
                else json.loads(COMMENTS_FILE.read_text(encoding="utf-8")))
    if any(c.get("photo_id") == str(target) for c in existing["items"]):
        return
    existing["items"].append({"photo_id": str(target), "when": item["when"],
                              "message": fc, "account": item.get("account", ""),
                              "status": "pending"})
    COMMENTS_FILE.write_text(json.dumps(existing, indent=2, ensure_ascii=False),
                             encoding="utf-8")


def schedule_ahead(dry_run: bool, horizon: timedelta = SCHEDULE_HORIZON,
                   limit: int = SCHEDULE_MAX_PER_RUN) -> None:
    q = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    now = datetime.now().astimezone()
    lo, hi = now + SCHEDULE_MIN_LEAD, now + horizon

    def when_of(i):
        w = datetime.fromisoformat(i["when"])
        return w.astimezone() if w.tzinfo is None else w

    cand = [i for i in q["items"]
            if i.get("status") == "pending"
            and i.get("network") == "facebook"
            and lo <= when_of(i) <= hi]
    cand.sort(key=lambda i: i["when"])          # soonest first, so nothing is missed

    if not cand:
        print("Nothing to hand to Meta.")
        return
    total = len(cand)
    if limit and total > limit:
        cand = cand[:limit]
        print(f"{total} eligible; handing over the soonest {limit} this run "
              f"(the rest go on later runs)")
    print(f"handing {len(cand)} Facebook item(s) to Meta "
          f"(due between {lo:%Y-%m-%d %H:%M} and {hi:%Y-%m-%d %H:%M})")

    done = 0
    for item in cand:
        label = f"{item['id']} [{item.get('type')}] -> {item.get('account')} @ {item['when'][:16]}"
        if dry_run:
            print("WOULD SCHEDULE:", label)
            continue
        try:
            result = _schedule_one(item)
            # Only now is it Meta's job. run_queue skips anything not "pending",
            # so this status change is what prevents a double post.
            item["status"] = "scheduled"
            item["result"] = result
            item["scheduled_at"] = now.isoformat(timespec="seconds")
            _queue_first_comment(item, result)
            done += 1
            print("SCHEDULED:", label)
        except Exception as e:
            item["error"] = str(e)[:300]
            print("SCHEDULE FAILED:", label, "->", e)
        # Persist after EVERY item: a crash midway must not leave posts live on
        # Facebook that the queue still thinks are pending, which would repost.
        if not dry_run:
            QUEUE_FILE.write_text(json.dumps(q, indent=2, ensure_ascii=False),
                                  encoding="utf-8")
    if not dry_run:
        print(f"handed {done}/{len(cand)} to Meta")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] not in ("run-queue", "list-queue", "schedule-ahead"):
        print(__doc__)
        sys.exit(1)
    dry = "--dry-run" in args
    if args[0] == "run-queue":
        run_queue(dry_run=dry)
        run_comments(dry_run=dry)
    elif args[0] == "schedule-ahead":
        def _opt(flag, default):
            return int(args[args.index(flag) + 1]) if flag in args else default
        schedule_ahead(dry_run=dry,
                       horizon=timedelta(days=_opt("--horizon-days",
                                                   SCHEDULE_HORIZON.days)),
                       limit=_opt("--max", SCHEDULE_MAX_PER_RUN))
        run_comments(dry_run=dry)
    else:
        list_queue()
