# -*- coding: utf-8 -*-
"""Append only the NEW hd10 reel items from a local queue snapshot onto the
queue.json in the current directory, leaving every existing item untouched.

Used inside a clean `git worktree` of origin/main so a checkpoint can ship
new reels while a render is still writing the live local queue.json, and
without merge_queue_origin.py (which can let a stale local `pending` overwrite
an item CI has since handed to Meta).

    python hd_append_new.py <path-to-local-queue.json>
"""
import json
import sys

from aug_common import load, save

src = json.load(open(sys.argv[1], encoding="utf-8"))
q = load()
have = {i["id"] for i in q["items"]}
new = [i for i in src["items"]
       if i.get("account") == "health-daily" and i["id"].startswith("hd-cadence-hd10_")
       and i["id"] not in have and i.get("status") == "pending"]
q["items"].extend(new)
save(q)
print(f"appended {len(new)} new hd10 items ({len({i['id'].rsplit('-', 1)[0] for i in new})} reels)")
