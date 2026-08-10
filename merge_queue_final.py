# -*- coding: utf-8 -*-
"""One-time careful merge of local queue.json (30-day/180-reel Health Daily
cadence rebuild) against origin/main's queue.json (which the cloud poster's
cron has been advancing independently for many hours). Origin's status/
posted_at/error/result always win for any id present there; ids only in
local (this session's new content) get appended. Reports the diff before
writing so it can be sanity-checked."""
import json

ORIGIN_PATH = r"C:\Users\Mamun\AppData\Local\Temp\claude\C--Users-Mamun\342921e7-8b70-4b1e-a567-64dceeb06cda\scratchpad\origin_queue.json"
STATUS_FIELDS = ("status", "posted_at", "error", "result", "first_comment_id", "first_comment_error")


def strip_status(item):
    return {k: v for k, v in item.items() if k not in STATUS_FIELDS}


def run():
    origin = json.load(open(ORIGIN_PATH, encoding="utf-8"))
    local = json.load(open("queue.json", encoding="utf-8"))

    origin_by_id = {i["id"]: i for i in origin["items"]}
    local_by_id = {i["id"]: i for i in local["items"]}

    only_local = set(local_by_id) - set(origin_by_id)
    only_origin = set(origin_by_id) - set(local_by_id)
    shared = set(local_by_id) & set(origin_by_id)

    content_conflicts = []
    for iid in shared:
        if strip_status(origin_by_id[iid]) != strip_status(local_by_id[iid]):
            content_conflicts.append(iid)

    print(f"only in local (new this session): {len(only_local)}")
    print(f"only in origin (posted while we built): {len(only_origin)}")
    print(f"shared: {len(shared)}")
    print(f"genuine content conflicts (non-status fields differ): {len(content_conflicts)}")
    for iid in content_conflicts[:10]:
        print("  CONFLICT:", iid)

    merged = []
    for iid, item in origin_by_id.items():
        merged.append(item)  # origin wins for anything it already has
    for iid in only_local:
        merged.append(local_by_id[iid])

    out = {"items": merged}
    json.dump(out, open("queue.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"\nmerged queue.json written: {len(merged)} total items")


if __name__ == "__main__":
    run()
