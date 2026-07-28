# -*- coding: utf-8 -*-
"""Publish a Facebook Reel to a page.

Reels do NOT use the photo/video endpoints — they need the three-phase
video_reels flow:

  1. start   POST /{page_id}/video_reels?upload_phase=start   -> video_id + upload_url
  2. upload  POST rupload.facebook.com/video-upload/{ver}/{video_id}  (binary body)
  3. finish  POST /{page_id}/video_reels?upload_phase=finish&video_state=PUBLISHED

Usage:
    python publish_reel.py --account top-movie-reviews \
        --video images/reels/reel1_jaws.mp4 --caption-file caption.txt
    python publish_reel.py ... --dry-run     # validate without publishing
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

_HERE = Path(__file__).parent
VER = "v23.0"
GRAPH = f"https://graph.facebook.com/{VER}"
RUPLOAD = f"https://rupload.facebook.com/video-upload/{VER}"


def _creds(account):
    with open(_HERE / "accounts.json", encoding="utf-8") as f:
        acc = json.load(f)
    a = acc["accounts"][account]
    return a["page_id"], a["page_token"]


def _post(url, data=None, headers=None, raw=None, timeout=300):
    body = raw if raw is not None else (
        urllib.parse.urlencode(data or {}).encode())
    req = urllib.request.Request(url, data=body, headers=headers or {}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            txt = r.read().decode()
            return json.loads(txt) if txt.strip().startswith("{") else {"raw": txt}
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode()[:600]
        except Exception:
            pass
        raise RuntimeError(f"HTTP {e.code}: {detail}") from None


def publish(account, video_path, caption, dry_run=False, schedule_ts=None):
    """schedule_ts: unix seconds. When set, the reel is uploaded now and
    published by Facebook later (video_state=SCHEDULED) — so scheduled reels
    do not need this machine to be on at post time."""
    pid, tok = _creds(account)
    vid_file = (_HERE / video_path) if not Path(video_path).is_absolute() else Path(video_path)
    if not vid_file.is_file():
        raise FileNotFoundError(vid_file)
    size = vid_file.stat().st_size
    print(f"page={pid}  file={vid_file.name}  {size/1e6:.1f} MB  caption={len(caption)} chars")

    if dry_run:
        print("DRY RUN — nothing published.")
        return None

    # --- phase 1: start ------------------------------------------------
    start = _post(f"{GRAPH}/{pid}/video_reels",
                  {"upload_phase": "start", "access_token": tok})
    video_id = start["video_id"]
    print(f"1/3 start OK — video_id={video_id}")

    # --- phase 2: binary upload ---------------------------------------
    blob = vid_file.read_bytes()
    _post(f"{RUPLOAD}/{video_id}", raw=blob, timeout=900, headers={
        "Authorization": f"OAuth {tok}",
        "offset": "0",
        "file_size": str(size),
        "Content-Type": "application/octet-stream",
    })
    print("2/3 upload OK")

    # --- phase 3: finish + publish (or schedule) -----------------------
    fields = {
        "upload_phase": "finish",
        "video_id": video_id,
        "description": caption,
        "access_token": tok,
    }
    if schedule_ts:
        fields["video_state"] = "SCHEDULED"
        fields["scheduled_publish_time"] = str(int(schedule_ts))
    else:
        fields["video_state"] = "PUBLISHED"
    fin = _post(f"{GRAPH}/{pid}/video_reels", fields)
    print(f"3/3 finish OK — {fin}")

    if schedule_ts:
        import datetime as _dt
        when = _dt.datetime.utcfromtimestamp(int(schedule_ts))
        return {"video_id": video_id, "status": "scheduled",
                "publish_at_utc": when.isoformat() + "Z"}

    # Encoding is async; poll until it's actually live.
    for attempt in range(20):
        time.sleep(6)
        q = urllib.parse.urlencode({"fields": "id,status,permalink_url", "access_token": tok})
        try:
            with urllib.request.urlopen(f"{GRAPH}/{video_id}?{q}", timeout=30) as r:
                st = json.load(r)
        except Exception:
            continue
        phase = (st.get("status") or {}).get("video_status")
        print(f"  poll {attempt+1}: {phase}")
        if phase in ("ready", "published"):
            return {"video_id": video_id, "permalink": st.get("permalink_url"), "status": phase}
    return {"video_id": video_id, "status": "still processing"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--account", default="top-movie-reviews")
    ap.add_argument("--video", required=True)
    ap.add_argument("--caption-file")
    ap.add_argument("--caption", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    cap = args.caption
    if args.caption_file:
        cap = Path(args.caption_file).read_text(encoding="utf-8")
    print(json.dumps(publish(args.account, args.video, cap, args.dry_run),
                     indent=1, ensure_ascii=False))
