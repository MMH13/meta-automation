# -*- coding: utf-8 -*-
"""Re-lay every PENDING Health Daily hd10 reel onto the daily grid (3 reels per
24h since 2026-11-02, was 10/day), starting from the next free slot (30+ min out).

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

SLOTS = [int(h) for h in os.environ.get("HD_SLOTS", "3,11,19").split(",")]
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
    # Once CI hands a reel's FB item to Meta (status "scheduled"), its IG twin is
    # still "pending" until due. Leave those reels exactly where they are: moving
    # the IG item would split it from its FB slot.
    held = set()
    for i in q["items"]:
        m = _RE.match(i.get("id", ""))
        if (m and i.get("account") == "health-daily" and i.get("network") == "facebook"
                and i.get("status") != "pending"):
            held.add(m.group(1))
    pairs = {k: v for k, v in pairs.items() if k not in held}
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
