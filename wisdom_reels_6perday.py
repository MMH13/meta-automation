# -*- coding: utf-8 -*-
"""Rebalance every PENDING Daily Wisdom reel onto a 6-per-day schedule.

Slots follow the user's own default schedule from the content spec (8:00,
10:30, 13:00, 15:30, 18:30, 21:00), treated as UTC since every other page in
this queue is scheduled in UTC and the spec gave no timezone. Flag this to
the user — if the audience is meant to see these at those times in their
LOCAL zone instead, the SLOTS list below is the only thing that needs to
change.

Re-runnable, same pattern as tmr_reels_6perday.py: run it again after
building more reels and everything (old pending + new) is re-laid onto the
grid from today forward. Slots already committed to Facebook (status
"scheduled" or "posted") are treated as taken so a re-lay can never collide
with a post Meta has already locked in.
"""
from datetime import datetime, timedelta, timezone

from aug_common import load, save

SLOTS = [8, 10, 13, 15, 18, 21]          # UTC hours — see docstring
PER_DAY = len(SLOTS)


def run():
    q = load()
    now = datetime.now(timezone.utc)

    reels = [i for i in q["items"]
             if i.get("id", "").startswith("dw-reel-") and i.get("status") == "pending"]
    if not reels:
        print("no pending Daily Wisdom reels")
        return
    reels.sort(key=lambda i: i["when"])

    taken = {i["when"] for i in q["items"]
             if i.get("account") == "asmr-life" and i.get("status") in ("scheduled", "posted")}

    day = now.date()
    todays_remaining = [h for h in SLOTS if datetime(day.year, day.month, day.day, h,
                                                     tzinfo=timezone.utc) > now]
    grid = []
    if todays_remaining:
        grid += [datetime(day.year, day.month, day.day, h, tzinfo=timezone.utc)
                 for h in todays_remaining]
    d = day + timedelta(days=1)
    while len(grid) < len(reels):
        grid += [datetime(d.year, d.month, d.day, h, tzinfo=timezone.utc) for h in SLOTS]
        d += timedelta(days=1)
    grid = [g for g in grid if g.isoformat() not in taken]

    for item, when in zip(reels, grid):
        item["when"] = when.isoformat()

    save(q)

    first, last = grid[0], grid[len(reels) - 1]
    print(f"rescheduled {len(reels)} reels to {PER_DAY}/day")
    print(f"  first: {first.isoformat()[:16]}")
    print(f"  last:  {last.isoformat()[:16]}")
    print(f"  covers {(last.date() - first.date()).days + 1} days")


if __name__ == "__main__":
    run()
