"""CLI for the Meta automation hub — mainly the scheduled-post queue runner.

Usage:
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
       "video_path": "images/reels/x.mp4 (FB reel — local file, 3-phase upload)",
       "when": "2026-07-14T09:00:00",
       "status": "pending"}
    ]}

The runner posts every 'pending' item whose 'when' is in the past, then writes
status posted/failed + the API result back into queue.json. Wire run-queue.ps1
into Windows Task Scheduler (e.g. every 15 minutes) for hands-off scheduling.
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path

_HERE = Path(__file__).parent
QUEUE_FILE = _HERE / "queue.json"
COMMENTS_FILE = _HERE / "comments.json"

sys.path.insert(0, str(_HERE))
import meta_mcp_server as meta  # reuse _api/_cfg/_ig_id and the accounts config
import publish_reel  # FB reels need the 3-phase video_reels upload, not fb_post*


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
            r = publish_reel.publish(acct, item["video_path"], msg)
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


def run_queue(dry_run: bool) -> None:
    q = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    due = [i for i in q["items"] if i.get("status") == "pending" and _due(i)]
    if not due:
        print("Nothing due.")
        return
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


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] not in ("run-queue", "list-queue"):
        print(__doc__)
        sys.exit(1)
    if args[0] == "run-queue":
        run_queue(dry_run="--dry-run" in args)
        run_comments(dry_run="--dry-run" in args)
    else:
        list_queue()
