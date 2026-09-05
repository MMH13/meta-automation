# -*- coding: utf-8 -*-
"""Daily Wisdom — reel batch enqueuer.

Builds each reel via video_wisdom_stock.build(), hosts it on the
ig-video-assets release (video_store.upload — no video ever gets committed to
git), then appends one pending queue.json item per reel.

Slug convention: "dw_d<day>_<name>" — day is 1-based against START_DATE.
Initial slot is a placeholder; wisdom_reels_6perday.py lays every pending
reel onto the real 6/day grid afterward, same two-step pattern as TMR.

Usage:
    python wisdom_reel_enqueue.py wisdom_reel_content1
"""
import importlib
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from aug_common import load, save
from video_wisdom_stock import build as build_reel
import video_store

_HERE = Path(__file__).parent
START_DATE = date(2026, 9, 6)
PLACEHOLDER_HOUR = 8

_SLUG_RE = re.compile(r"^dw_d(\d+)_")


def _slot_for(slug):
    m = _SLUG_RE.match(slug)
    if not m:
        raise ValueError(f"slug {slug!r} doesn't match the dw_d<day>_ convention")
    d = START_DATE + timedelta(days=int(m.group(1)) - 1)
    return f"{d.isoformat()}T{PLACEHOLDER_HOUR:02d}:00:00+00:00"


def main(module_name):
    mod = importlib.import_module(module_name)
    reels = mod.REELS

    out_dir = _HERE / "images" / f"wisdom_reels_{module_name.replace('wisdom_reel_', '')}"
    out_dir.mkdir(parents=True, exist_ok=True)

    have = {i.get("id") for i in load()["items"]}
    n = 0

    for slug, pillar, beats, caption in reels:
        fb_id = f"dw-reel-{slug}"
        if fb_id in have:
            continue

        video_path = out_dir / f"{slug}.mp4"
        work_dir = out_dir / f"{slug}_work"
        state = out_dir / f"{slug}_state.json"
        lock = out_dir / f"{slug}.lock"

        if not video_path.is_file():
            print(f"\n=== building {slug} [{pillar}] ({len(beats)} beats) ===")
            build_reel(beats, str(video_path), str(work_dir), str(state), str(lock))

        when = _slot_for(slug)
        src = video_store.upload(video_path)

        q = load()
        items = q["items"]
        if fb_id not in {i.get("id") for i in items}:
            items.append({
                "id": fb_id, "account": "asmr-life", "network": "facebook",
                "type": "reel", "message": caption,
                "video_path": video_path.relative_to(_HERE).as_posix(),
                "video_src": src,
                "when": when, "status": "pending",
            })
            n += 1
            save(q)
            have = {i.get("id") for i in items}

        print(f"  queued {slug} for {when}")

    print(f"\nqueued {n} new items")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python wisdom_reel_enqueue.py <content_module_name>")
        sys.exit(1)
    main(sys.argv[1])
