# -*- coding: utf-8 -*-
"""Health check across every managed page: what the LIVE Graph API says was
actually posted recently, cross-checked against what the queue thinks.

Catches the failure modes that have actually bitten this project: a page
silently running dry, a queue that says "posted" while the page shows
nothing, overdue items piling up, and repeated failures.

    python check_all_pages.py
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

_HERE = Path(__file__).parent
ACC = json.load(open(_HERE / "accounts.json", encoding="utf-8"))
QUEUE = json.load(open(_HERE / "queue.json", encoding="utf-8"))
NOW = datetime.now(timezone.utc)


def graph(path, params, token):
    params = dict(params)
    params["access_token"] = token
    url = f"https://graph.facebook.com/v20.0/{path}?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=25) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"_err": f"HTTP {e.code}: {e.read().decode()[:120]}"}
    except Exception as e:
        return {"_err": str(e)[:120]}


def per_day(times):
    """posts/day over the last 7 days, from ISO timestamps"""
    cutoff = NOW - timedelta(days=7)
    recent = [t for t in times if datetime.fromisoformat(t.replace("+0000", "+00:00")) >= cutoff]
    return len(recent) / 7.0, recent


def main():
    rows = []
    for key, cfg in ACC["accounts"].items():
        items = [i for i in QUEUE["items"] if i.get("account") == key]
        if not items:
            continue  # page not driven by this queue

        token, page_id = cfg.get("page_token"), cfg.get("page_id")
        feed = graph(f"{page_id}/posts",
                     {"fields": "created_time,attachments{media_type}", "limit": 50}, token)

        if "_err" in feed:
            live_rate, last_live, kinds = None, feed["_err"], {}
        else:
            times = [p["created_time"] for p in feed.get("data", [])]
            live_rate, recent = per_day(times)
            last_live = times[0][:16].replace("T", " ") if times else "never"
            kinds = Counter(
                a.get("media_type")
                for p in feed.get("data", [])[:20]
                for a in p.get("attachments", {}).get("data", [])
            )

        pending = [i for i in items if i.get("status") == "pending"]
        # "scheduled" = handed to Meta, which will publish it itself. It is NOT
        # a stalled item, and counting it as overdue would cry wolf every run.
        sched = [i for i in items if i.get("status") == "scheduled"]
        overdue = [i for i in pending
                   if datetime.fromisoformat(i["when"]) <= NOW]
        failed = [i for i in items if i.get("status") == "failed"]
        future = sorted(i["when"] for i in pending + sched)
        runway = "—"
        if future:
            last_day = datetime.fromisoformat(future[-1]).date()
            runway = f"{(last_day - NOW.date()).days}d (to {last_day})"

        rows.append({
            "page": cfg.get("page_name", key),
            "live_rate": live_rate,
            "last_live": last_live,
            "kinds": kinds,
            "pending": len(pending),
            "scheduled": len(sched),
            "overdue": len(overdue),
            "failed": len(failed),
            "runway": runway,
        })

    print(f"{'PAGE':<22}{'LIVE/day':>9}{'LAST LIVE':>18}{'PEND':>6}{'SCHED':>7}{'DUE':>5}{'FAIL':>6}  RUNWAY")
    print("-" * 95)
    for r in rows:
        rate = f"{r['live_rate']:.1f}" if r["live_rate"] is not None else "ERR"
        print(f"{r['page']:<22}{rate:>9}{r['last_live']:>18}"
              f"{r['pending']:>6}{r['scheduled']:>7}{r['overdue']:>5}"
              f"{r['failed']:>6}  {r['runway']}")

    print("\nrecent media mix (last 20 live posts):")
    for r in rows:
        if r["kinds"]:
            mix = ", ".join(f"{k}×{v}" for k, v in r["kinds"].most_common())
            print(f"  {r['page']:<22} {mix}")

    print("\nflags:")
    any_flag = False
    for r in rows:
        if r["overdue"]:
            print(f"  ! {r['page']}: {r['overdue']} item(s) overdue and unposted")
            any_flag = True
        if r["failed"]:
            print(f"  ! {r['page']}: {r['failed']} failed item(s)")
            any_flag = True
        if r["live_rate"] == 0:
            print(f"  ! {r['page']}: nothing posted live in the last 7 days")
            any_flag = True
        if r["pending"] == 0 and r["scheduled"] == 0:
            print(f"  ! {r['page']}: queue EMPTY — will go dark")
            any_flag = True
    if not any_flag:
        print("  none — all pages posting and stocked")


if __name__ == "__main__":
    main()
