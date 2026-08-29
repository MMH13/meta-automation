# -*- coding: utf-8 -*-
"""Merge a local queue.json against origin's, which the cloud poster advances
independently while we build content locally.

The rule that matters: origin is the only authority on what has actually been
POSTED, and we are the only authority on what is still SCHEDULED. So

  - terminal on origin (posted/failed) -> take origin's item wholesale, always.
    Rescheduling something already live would repost it.
  - still pending on origin            -> take the local item (it carries any
    reschedule we just did), but graft origin's status fields back on.
  - local-only ids                     -> append (content built this session)
  - origin-only ids                    -> keep (built elsewhere)

Never line-merge queue.json: git will happily interleave two valid JSON files
into one invalid one, and the poster reads it on every cron tick.

    python merge_queue_origin.py <origin_queue.json>
"""
import json
import sys

STATUS_FIELDS = ("status", "posted_at", "error", "result",
                 "first_comment_id", "first_comment_error")
TERMINAL = {"posted", "failed", "skipped"}


def run(origin_path):
    origin = json.load(open(origin_path, encoding="utf-8"))
    local = json.load(open("queue.json", encoding="utf-8"))

    o_by_id = {i["id"]: i for i in origin["items"]}
    l_by_id = {i["id"]: i for i in local["items"]}

    merged, took_origin, rescheduled = [], 0, 0
    for iid, o in o_by_id.items():
        l = l_by_id.get(iid)
        if l is None or o.get("status") in TERMINAL:
            merged.append(o)
            took_origin += 1
            continue
        item = dict(l)
        for f in STATUS_FIELDS:                 # origin still owns status
            if f in o:
                item[f] = o[f]
            else:
                item.pop(f, None)
        if item.get("when") != o.get("when"):
            rescheduled += 1
        merged.append(item)

    only_local = [iid for iid in l_by_id if iid not in o_by_id]
    merged.extend(l_by_id[iid] for iid in only_local)

    json.dump({"items": merged}, open("queue.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)

    print(f"origin items taken as-is (terminal or unknown locally): {took_origin}")
    print(f"pending items keeping our local schedule:               {len(o_by_id) - took_origin}")
    print(f"  of which the 'when' actually changed:                 {rescheduled}")
    print(f"new local-only items appended:                          {len(only_local)}")
    print(f"total: {len(merged)}")


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "origin_queue.json")
