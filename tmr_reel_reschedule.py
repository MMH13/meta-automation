# -*- coding: utf-8 -*-
"""Pull the TMR poster-reel schedule forward so posting starts immediately
instead of waiting for the original Aug 25 start.

- every reel shifts back one day (Aug 25..Sep 23 -> Aug 24..Sep 22)
- day 1 is additionally set to a moment already in the past, so the next
  hourly cron run picks it up rather than waiting for today's 17:00 slot

Only touches pending tmr-reel-* items; anything already posted is left alone.
"""
from datetime import datetime, timedelta, timezone

from aug_common import load, save

SHIFT = timedelta(days=1)


def run():
    q = load()
    now = datetime.now(timezone.utc)
    first_when = (now - timedelta(minutes=5)).replace(microsecond=0)

    reels = [i for i in q["items"]
             if i.get("id", "").startswith("tmr-reel-") and i.get("status") == "pending"]
    reels.sort(key=lambda i: i["when"])

    if not reels:
        print("no pending TMR reels found")
        return

    for n, item in enumerate(reels):
        old = datetime.fromisoformat(item["when"])
        new = first_when if n == 0 else (old - SHIFT)
        item["when"] = new.isoformat()
        if n < 3 or n == len(reels) - 1:
            print(f"  {item['id']:<34} {old.isoformat()[:16]} -> {new.isoformat()[:16]}")
        elif n == 3:
            print("  ...")

    save(q)
    print(f"\nrescheduled {len(reels)} reels; first fires on the next cron run")


if __name__ == "__main__":
    run()
