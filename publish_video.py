# -*- coding: utf-8 -*-
"""Publish a regular Facebook feed/Watch video to a page (NOT a Reel).

Reels use the video_reels three-phase flow (see publish_reel.py). Feed/Watch
videos use the simpler single-request /{page_id}/videos upload — fine for
files under ~1GB, which covers everything this project produces.

Usage:
    python publish_video.py --account suspense-ahead \
        --video images/suspense_longform1_square.mp4 --caption-file caption.txt
    python publish_video.py ... --dry-run     # validate without publishing
    python publish_video.py ... --schedule 2026-08-01T18:00:00+00:00
"""
import argparse
import json
import sys
import time
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8")

_HERE = Path(__file__).parent
VER = "v23.0"
GRAPH_VIDEO = f"https://graph-video.facebook.com/{VER}"
GRAPH = f"https://graph.facebook.com/{VER}"


def _creds(account):
    with open(_HERE / "accounts.json", encoding="utf-8") as f:
        acc = json.load(f)
    a = acc["accounts"][account]
    return a["page_id"], a["page_token"]


def _to_unix(iso_str):
    import datetime as _dt
    dt = _dt.datetime.fromisoformat(iso_str)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=_dt.timezone.utc)
    return int(dt.timestamp())


def publish(account, video_path, caption, dry_run=False, schedule=None):
    pid, tok = _creds(account)
    vid_file = (_HERE / video_path) if not Path(video_path).is_absolute() else Path(video_path)
    if not vid_file.is_file():
        raise FileNotFoundError(vid_file)
    size = vid_file.stat().st_size
    print(f"page={pid}  file={vid_file.name}  {size/1e6:.1f} MB  caption={len(caption)} chars")

    if dry_run:
        print("DRY RUN — nothing published.")
        return None

    data = {"description": caption, "access_token": tok}
    if schedule:
        data["published"] = "false"
        data["scheduled_publish_time"] = str(_to_unix(schedule))

    with vid_file.open("rb") as fh:
        resp = requests.post(f"{GRAPH_VIDEO}/{pid}/videos", data=data,
                             files={"source": (vid_file.name, fh)}, timeout=600)
    body = resp.json() if resp.text else {}
    if resp.status_code >= 400:
        err = body.get("error") or {}
        raise RuntimeError(f"Graph API {resp.status_code}: "
                           f"{err.get('message', resp.text[:500])}")
    video_id = body["id"]
    print(f"upload OK — video_id={video_id}")

    if schedule:
        return {"video_id": video_id, "status": "scheduled",
                "publish_at": schedule}

    # Encoding is async; poll until it's actually live.
    for attempt in range(20):
        time.sleep(6)
        try:
            r = requests.get(f"{GRAPH}/{video_id}",
                             params={"fields": "id,status,permalink_url", "access_token": tok},
                             timeout=30)
            st = r.json()
        except Exception:
            continue
        phase = (st.get("status") or {}).get("video_status")
        print(f"  poll {attempt+1}: {phase}")
        if phase in ("ready", "published"):
            return {"video_id": video_id, "permalink": st.get("permalink_url"), "status": phase}
    return {"video_id": video_id, "status": "still processing"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--account", required=True)
    ap.add_argument("--video", required=True)
    ap.add_argument("--caption-file")
    ap.add_argument("--caption", default="")
    ap.add_argument("--schedule", help="ISO datetime, e.g. 2026-08-01T18:00:00+00:00")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    cap = args.caption
    if args.caption_file:
        cap = Path(args.caption_file).read_text(encoding="utf-8")
    print(json.dumps(publish(args.account, args.video, cap, args.dry_run, args.schedule),
                     indent=1, ensure_ascii=False))
