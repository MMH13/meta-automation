# -*- coding: utf-8 -*-
"""One-time queue restructure: Health Daily moves from 6 images/day (mirrored
FB+IG) + 1 text checkin to the new standing cadence of 6 reels + 2 images/day.
This script prunes the currently-pending health-daily image/text queue items
down to just the 2 kept slots (index 02 = 07:00 UTC, 04 = 13:00 UTC), freeing
the other 5 daily slots (01, 04-old, 10, 16, 19) for reel items to be added
separately by hd_reel_enqueue.py. Run once."""
from aug_common import load, save

KEEP_SLOTS = {"02", "04"}


def _slot(item_id):
    parts = item_id.split("-")
    tail = parts[-1]
    return parts[-2] if tail in ("fb", "ig") else tail


def should_prune(i):
    if i.get("account") != "health-daily" or i.get("status") != "pending":
        return False
    if not i["id"].startswith("hd-refill1-"):
        return False
    if i.get("type") == "text":
        return True
    return _slot(i["id"]) not in KEEP_SLOTS


def run():
    q = load()
    before = len(q["items"])
    q["items"] = [i for i in q["items"] if not should_prune(i)]
    removed = before - len(q["items"])
    save(q)
    print(f"removed {removed} items; queue now {len(q['items'])} total")


if __name__ == "__main__":
    run()
