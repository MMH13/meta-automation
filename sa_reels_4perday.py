# -*- coding: utf-8 -*-
"""Rebalance every PENDING Suspense Ahead reel onto a 4-per-day schedule.

Batch 10 switched the page from 3-short+1-longform/day to a uniform 4x
60-90s reels/day. sa_reel_enqueue.py's _slot_for() still stamps a rough
day-index placeholder on new items; this script re-lays every pending reel
onto the real grid from now forward, same two-step pattern as
wisdom_reels_6perday.py / tmr_reels_6perday.py.

Slots (0/6/12/18 UTC) were chosen to avoid the page's existing card queue
hours (10/13/16/19/21/23 UTC, per sa_reel_enqueue.py's docstring).

Re-runnable: run it again after building more reels and everything (old
pending + new) is re-laid from today forward. Slots already committed to
Facebook (status "scheduled" or "posted") are treated as taken so a re-lay
can never collide with a post Meta has already locked in.
"""
from datetime import datetime, timedelta, timezone

from aug_common import load, save

SLOTS = [0, 6, 12, 18]          # UTC hours — see docstring
PER_DAY = len(SLOTS)


def run():
    q = load()
    now = datetime.now(timezone.utc)

    reels = [i for i in q["items"]
             if i.get("id", "").startswith("sa-cadence-") and i.get("account") == "suspense-ahead"
             and i.get("status") == "pending"]
    if not reels:
        print("no pending Suspense Ahead reels")
        return
    reels.sort(key=lambda i: i["when"])

    taken = {i["when"] for i in q["items"]
             if i.get("account") == "suspense-ahead" and i.get("status") in ("scheduled", "posted")}

    # Build the grid skipping taken slots AS we go, not as a post-hoc filter -
    # a naive post-hoc filter can under-fill the grid and crash indexing the
    # tail (the exact bug hit and fixed in wisdom_reels_6perday.py).
    grid = []
    d = now.date()
    while len(grid) < len(reels):
        for h in SLOTS:
            dt = datetime(d.year, d.month, d.day, h, tzinfo=timezone.utc)
            if dt > now and dt.isoformat() not in taken:
                grid.append(dt)
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
