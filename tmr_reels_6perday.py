# -*- coding: utf-8 -*-
"""Rebalance every PENDING Top Movie Reviews reel onto a 6-per-day schedule.

Reel slots are chosen to interleave with the existing static card slots
(13/15/19/23 UTC), giving an evenly spread day rather than clumps:

    01  05  09  11  [13]  [15]  17  [19]  21  [23]
    ^^  ^^  ^^  ^^                ^^        ^^        = reels
                    ^^^^  ^^^^        ^^^^      ^^^^  = static cards

Re-runnable: run it again after building more reels and everything (old
pending + new) is re-laid onto the same 6/day grid from today forward.
"""
from datetime import datetime, timedelta, timezone

from aug_common import load, save

SLOTS = [1, 5, 9, 11, 17, 21]          # UTC hours, 6 per day
PER_DAY = len(SLOTS)


def run():
    q = load()
    now = datetime.now(timezone.utc)

    reels = [i for i in q["items"]
             if i.get("id", "").startswith("tmr-reel-") and i.get("status") == "pending"]
    if not reels:
        print("no pending TMR reels")
        return
    reels.sort(key=lambda i: i["when"])          # keep existing order

    # Slots already committed to Facebook. Once an item is handed to Meta it
    # publishes at that exact minute no matter what the queue says later, so
    # reusing its slot here would double-book it: two reels at one time, and
    # the queue would look correct while Facebook disagreed.
    taken = {i["when"] for i in q["items"]
             if i.get("id", "").startswith("tmr-reel-")
             and i.get("status") in ("scheduled", "posted")}

    # start today if any of today's slots are still ahead of us, else tomorrow
    day = now.date()
    todays_remaining = [h for h in SLOTS if datetime(day.year, day.month, day.day, h,
                                                     tzinfo=timezone.utc) > now]
    def free(slots):
        return [t for t in slots if t.isoformat() not in taken]

    grid = []
    if todays_remaining:
        grid += free([datetime(day.year, day.month, day.day, h, tzinfo=timezone.utc)
                      for h in todays_remaining])
    d = day + timedelta(days=1)
    while len(grid) < len(reels):
        grid += free([datetime(d.year, d.month, d.day, h, tzinfo=timezone.utc)
                      for h in SLOTS])
        d += timedelta(days=1)

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
