# -*- coding: utf-8 -*-
"""Push every pending reel's video to the release and stamp `video_src` on it.

Run this after building a batch (and before untracking videos from git) so the
CI runner can post from a checkout that contains no mp4s at all. Re-runnable:
already-hosted assets are skipped, already-stamped items are left alone.

    python host_pending_videos.py            # upload + stamp
    python host_pending_videos.py --check    # report only, change nothing

The queue is reloaded immediately before writing. The uploads take minutes and
a render or the cron may append items in the meantime; holding one in-memory
copy across the whole run is how a previous script silently undid concurrent
edits.
"""
import json
import sys
from pathlib import Path

import video_store

_HERE = Path(__file__).parent
QUEUE = _HERE / "queue.json"


def pending_with_video(items):
    return [i for i in items
            if i.get("status") == "pending" and i.get("video_path")]


def run(check_only=False):
    items = json.loads(QUEUE.read_text(encoding="utf-8"))["items"]
    pend = pending_with_video(items)
    hosted = video_store.hosted_names()

    missing_local, to_upload = [], []
    for i in pend:
        p = _HERE / i["video_path"]
        if p.name in hosted:
            continue
        (to_upload if p.is_file() else missing_local).append(i)

    print(f"pending reels:        {len(pend)}")
    print(f"already hosted:       {len(pend) - len(to_upload) - len(missing_local)}")
    print(f"to upload:            {len(to_upload)}")
    if missing_local:
        print(f"!! NOT hosted and NOT on disk: {len(missing_local)}")
        for i in missing_local[:10]:
            print(f"     {i['id']} -> {i['video_path']}")
        print("   these cannot post — build them or remove them from the queue")

    if check_only:
        return

    for n, i in enumerate(to_upload, 1):
        p = _HERE / i["video_path"]
        mb = p.stat().st_size / 1e6
        print(f"[{n}/{len(to_upload)}] {p.name} ({mb:.1f} MB)", flush=True)
        video_store.upload(p, known=hosted)

    # reload — a render or the cron may have appended while we uploaded
    q = json.loads(QUEUE.read_text(encoding="utf-8"))
    stamped = 0
    for i in pending_with_video(q["items"]):
        name = Path(i["video_path"]).name
        if name in hosted and not i.get("video_src"):
            i["video_src"] = video_store.url_for(name)
            stamped += 1
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nuploaded {len(to_upload)}, stamped video_src on {stamped} item(s)")
    if missing_local:
        print(f"WARNING: {len(missing_local)} pending item(s) still have no hosted video")


if __name__ == "__main__":
    run(check_only="--check" in sys.argv)
