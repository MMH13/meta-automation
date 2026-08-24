# -*- coding: utf-8 -*-
"""Top Movie Reviews — poster-reel batch enqueuer.

Builds each reel via video_movie_reel_poster.py, then APPENDS one pending
queue.json item per reel (network:facebook, type:reel, video_path). Top Movie
Reviews has no linked IG account, so it's one item per reel — no public-asset
upload step, unlike the Health Daily pipeline.

Slug convention: "tmr_d<day>_<name>" — day is 1-based against START_DATE.
Reels land at 17:00 UTC, between the existing static card slots (13/15/19/23).

Usage:
    python tmr_reel_enqueue.py tmr_reel_content1
"""
import importlib
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from aug_common import load, save
from video_movie_reel_poster import build as build_reel

_HERE = Path(__file__).parent
START_DATE = date(2026, 8, 25)
REEL_HOUR = 17

_SLUG_RE = re.compile(r"^tmr_d(\d+)_")


def _slot_for(slug):
    m = _SLUG_RE.match(slug)
    if not m:
        raise ValueError(f"slug {slug!r} doesn't match the tmr_d<day>_ convention")
    d = START_DATE + timedelta(days=int(m.group(1)) - 1)
    return f"{d.isoformat()}T{REEL_HOUR:02d}:00:00+00:00"


def main(module_name):
    mod = importlib.import_module(module_name)
    reels = mod.REELS

    out_dir = _HERE / "images" / f"tmr_reels_{module_name.replace('tmr_reel_', '')}"
    out_dir.mkdir(parents=True, exist_ok=True)

    have = {i.get("id") for i in load()["items"]}
    n = 0

    for slug, beats, caption in reels:
        fb_id = f"tmr-reel-{slug}"
        if fb_id in have:
            continue

        video_path = out_dir / f"{slug}.mp4"
        work_dir = out_dir / f"{slug}_work"
        state = out_dir / f"{slug}_state.json"
        lock = out_dir / f"{slug}.lock"

        if not video_path.is_file():
            print(f"\n=== building {slug} ({len(beats)} beats) ===")
            build_reel(beats, str(video_path), str(work_dir), str(state), str(lock))

        when = _slot_for(slug)

        q = load()
        items = q["items"]
        if fb_id not in {i.get("id") for i in items}:
            items.append({
                "id": fb_id, "account": "top-movie-reviews", "network": "facebook",
                "type": "reel", "message": caption,
                "video_path": video_path.relative_to(_HERE).as_posix(),
                "when": when, "status": "pending",
            })
            n += 1
            save(q)
            have = {i.get("id") for i in items}

        print(f"  queued {slug} for {when}")

    print(f"\nqueued {n} new items")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python tmr_reel_enqueue.py <content_module_name>")
        sys.exit(1)
    main(sys.argv[1])
