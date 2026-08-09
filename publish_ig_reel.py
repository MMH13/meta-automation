# -*- coding: utf-8 -*-
"""Publish a local video file to Instagram as a Reel.

IG's Reels API needs a genuinely public video_url. Two things were tried and
ruled out (2026-08-06): (1) Facebook's own CDN `source` URL for an
already-published FB reel — fails every time with error 2207076; (2) a
GitHub release asset in a PRIVATE repo — same error, because the URL isn't
actually fetchable by anyone unauthenticated (confirmed via plain curl: 404).
**The fix**: host the file as a release asset in a dedicated PUBLIC repo
(github.com/MMH13/ig-video-assets) — confirmed working end-to-end.

Usage:
    python publish_ig_reel.py --account health-daily --video path/to/reel.mp4 --caption-file cap.txt
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8")

_HERE = Path(__file__).parent
GRAPH = "https://graph.facebook.com/v23.0"
ASSET_REPO = "MMH13/ig-video-assets"
ASSET_RELEASE_TAG = "videos"


def _creds(account):
    acc = json.load(open(_HERE / "accounts.json", encoding="utf-8"))["accounts"][account]
    if not acc.get("ig_user_id"):
        raise RuntimeError(f"{account} has no linked ig_user_id")
    return acc["page_token"], acc["ig_user_id"]


def _upload_public(video_path, asset_name=None):
    """Upload to the public asset repo's release; return the public download URL."""
    video_path = Path(video_path)
    name = asset_name or video_path.name
    subprocess.run(["gh", "release", "upload", ASSET_RELEASE_TAG, str(video_path),
                    "--repo", ASSET_REPO, "--clobber"], check=True, capture_output=True, text=True)
    return f"https://github.com/{ASSET_REPO}/releases/download/{ASSET_RELEASE_TAG}/{name}"


def publish(account, video_path, caption, dry_run=False, asset_name=None):
    token, ig_id = _creds(account)
    src = _upload_public(video_path, asset_name=asset_name)
    print(f"  hosted at: {src}")

    if dry_run:
        print("DRY RUN — not creating IG media container.")
        return None

    r = requests.post(f"{GRAPH}/{ig_id}/media",
                      data={"media_type": "REELS", "video_url": src, "caption": caption,
                            "access_token": token}, timeout=60)
    body = r.json()
    if r.status_code >= 400:
        raise RuntimeError(f"IG media create {r.status_code}: {body}")
    container_id = body["id"]
    print(f"  IG container created: {container_id}")

    deadline = time.time() + 300
    while time.time() < deadline:
        st = requests.get(f"{GRAPH}/{container_id}", params={"fields": "status_code,status", "access_token": token}, timeout=30).json()
        code = st.get("status_code")
        if code == "FINISHED":
            break
        if code == "ERROR":
            raise RuntimeError(f"IG container {container_id} failed: {st}")
        time.sleep(5)
    else:
        raise RuntimeError(f"IG container {container_id} not ready after 300s")

    pub = requests.post(f"{GRAPH}/{ig_id}/media_publish",
                        data={"creation_id": container_id, "access_token": token}, timeout=60).json()
    media_id = pub.get("id")
    perm = requests.get(f"{GRAPH}/{media_id}", params={"fields": "permalink", "access_token": token}, timeout=30).json()
    return {"ig_media_id": media_id, "permalink": perm.get("permalink"), "status": "published"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--account", required=True)
    ap.add_argument("--video", required=True)
    ap.add_argument("--asset-name", help="override the hosted filename (default: source filename)")
    ap.add_argument("--caption-file")
    ap.add_argument("--caption", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    cap = args.caption
    if args.caption_file:
        cap = Path(args.caption_file).read_text(encoding="utf-8")
    print(json.dumps(publish(args.account, args.video, cap, args.dry_run, args.asset_name), indent=1, ensure_ascii=False))
