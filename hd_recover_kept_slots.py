# -*- coding: utf-8 -*-
"""Recovery for a bug in hd_prune_range.py: KEEP_SLOTS was written as the
zero-padded strings {"02","04"} but the id format's slot token is an
un-padded single digit ("...-02-4-fb" -> slot "4", not "04"), so the compare
never matched and ALL 390 old health-daily image/text items were removed
instead of the intended 60 (slots 2 and 4 kept, 2 images/day x 30 days).
This restores just the correct slots 2 ("07:00") and 4 ("13:00") from the
pre-prune committed snapshot back into the current queue.json."""
import json
from aug_common import load, save

SNAPSHOT = r"C:\Users\Mamun\AppData\Local\Temp\claude\C--Users-Mamun\342921e7-8b70-4b1e-a567-64dceeb06cda\scratchpad\queue_before.json"
KEEP_SLOTS = {"2", "4"}


def _slot(item_id):
    parts = item_id.split("-")
    tail = parts[-1]
    return parts[-2] if tail in ("fb", "ig") else tail


def run():
    before = json.load(open(SNAPSHOT, encoding="utf-8"))
    to_restore = [
        i for i in before["items"]
        if i.get("account") == "health-daily"
        and i.get("status") == "pending"
        and i["id"].startswith("hd-refill1-")
        and i.get("type") != "text"
        and _slot(i["id"]) in KEEP_SLOTS
    ]
    print(f"recovering {len(to_restore)} items (expect 60: 2 slots x 2 networks x 30 days)")

    q = load()
    have = {i["id"] for i in q["items"]}
    added = 0
    for i in to_restore:
        if i["id"] not in have:
            q["items"].append(i)
            added += 1
    save(q)
    print(f"added {added} items back; queue now {len(q['items'])} total")


if __name__ == "__main__":
    run()
