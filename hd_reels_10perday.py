# -*- coding: utf-8 -*-
"""Re-lay every PENDING Health Daily hd10 reel onto the 10-reels/day grid,
starting from the next free slot (at least 30 min out).

hd_reel_enqueue.py stamps each reel with a slot derived from its day number
against START_DATE (2026-09-11), so reels built after that date come out
already in the past - CI would treat them as overdue and post them in bursts.
Same two-step pattern as wisdom_reels_6perday.py / sa_reels_4perday.py:
enqueue, then re-lay. A reel's Facebook and Instagram items always share one
slot. Slots already held by a scheduled/posted health-daily item are skipped.
"""
import os
import re
from datetime import datetime, timedelta, timezone

from aug_common import load, save

SLOTS = [int(h) for h in os.environ.get("HD_SLOTS", "0,2,5,7,9,11,14,16,19,22").split(",")]
LEAD = timedelta(minutes=30)
_RE = re.compile(r"^hd-cadence-(hd10_d(\d+)_(\d+)_.+)-(fb|ig)$")


def run():
    q = load()
    now = datetime.now(timezone.utc)

    pairs = {}
    for i in q["items"]:
        if i.get("account") != "health-daily" or i.get("status") != "pending":
            continue
        m = _RE.match(i.get("id", ""))
        if m:
            pairs.setdefault(m.group(1), (int(m.group(2)), int(m.group(3)), []))[2].append(i)
    if not pairs:
        print("no pending hd10 reels")
        return
    order = sorted(pairs.items(), key=lambda kv: (kv[1][0], kv[1][1]))

    taken = {i["when"] for i in q["items"]
             if i.get("account") == "health-daily" and i.get("status") in ("scheduled", "posted")}

    grid = []
    d = now.date()
    while len(grid) < len(order):
        for h in SLOTS:
            dt = datetime(d.year, d.month, d.day, h, tzinfo=timezone.utc)
            if dt > now + LEAD and dt.isoformat() not in taken:
                grid.append(dt)
        d += timedelta(days=1)

    for (slug, (_, _, items)), when in zip(order, grid):
        for it in items:
            it["when"] = when.isoformat()

    save(q)
    first, last = grid[0], grid[len(order) - 1]
    print(f"re-laid {len(order)} reels ({sum(len(v[2]) for _, v in order)} items) at {len(SLOTS)}/day")
    print(f"  first: {first.isoformat()[:16]}")
    print(f"  last:  {last.isoformat()[:16]}")
    print(f"  covers {(last.date() - first.date()).days + 1} days")


if __name__ == "__main__":
    run()
