# -*- coding: utf-8 -*-
"""Health Daily — reel batch enqueuer for the new 6-reels+2-images/day
cadence (2026-08-09). Unlike health_reel_batch_runner.py, this does NOT
publish immediately — it builds each reel locally, uploads it to the public
IG asset repo for a stable video_url, then APPENDS two pending queue.json
items (one facebook/reel with a local video_path, one instagram/reel with
the public video_url) at the slug's assigned daily slot. This routes reels
through the cron-paced queue runner instead of a manual batch blast, which
is the actual fix for the burst-posting problem measured 2026-08-09.

Slug naming convention read by this script: "..._d<day>_<pos>_...", where
day is 1-based and pos is 1-6 (mapped to REEL_HOURS[pos-1]).

Usage:
    python hd_reel_enqueue.py health_reel_cadence1
    python hd_reel_enqueue.py health_reel_cadence2 --stock   # real Pexels B-roll pipeline
"""
import importlib
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from aug_common import load, save
import video_store
from publish_ig_reel import _upload_public

_HERE = Path(__file__).parent
START_DATE = date(2026, 8, 11)
REEL_HOURS = [1, 4, 10, 16, 19, 22]  # UTC; 07/13 stay reserved for images

_SLUG_RE = re.compile(r"_d(\d+)_(\d+)_")


def _slot_for(slug):
    m = _SLUG_RE.search(slug)
    if not m:
        raise ValueError(f"slug {slug!r} doesn't match the _d<day>_<pos>_ convention")
    day_idx, pos = int(m.group(1)) - 1, int(m.group(2)) - 1
    d = START_DATE + timedelta(days=day_idx)
    hour = REEL_HOURS[pos]
    return f"{d.isoformat()}T{hour:02d}:00:00+00:00"


def main(module_name, stock=False):
    if stock:
        from video_health_reel_stock import build as build_reel
    else:
        from video_health_reel import build as build_reel

    mod = importlib.import_module(module_name)
    reels = mod.REELS

    out_dir = _HERE / "images" / f"health_reels_{module_name.replace('health_reel_', '')}"
    out_dir.mkdir(parents=True, exist_ok=True)

    have = {i.get("id") for i in load()["items"]}
    n = 0

    for slug, beats, caption in reels:
        fb_id, ig_id = f"hd-cadence-{slug}-fb", f"hd-cadence-{slug}-ig"
        if fb_id in have and ig_id in have:
            continue

        video_path = out_dir / f"{slug}.mp4"
        work_dir = out_dir / f"{slug}_work"
        video_state = out_dir / f"{slug}_state.json"
        lock = out_dir / f"{slug}.lock"

        if not video_path.is_file():
            print(f"\n=== building {slug} ===")
            build_reel(beats, str(video_path), str(work_dir), str(video_state), str(lock))

        when = _slot_for(slug)
        video_url = None
        if ig_id not in have:
            print(f"  uploading {slug} to public asset repo for IG...")
            video_url = _upload_public(str(video_path), asset_name=f"{slug}.mp4")

        # Reload right before writing so a concurrent editor's changes
        # (e.g. a queue prune running in another process) aren't clobbered
        # by this script's own stale in-memory snapshot.
        q = load()
        items = q["items"]
        ids_now = {i.get("id") for i in items}

        if fb_id not in ids_now:
            items.append({
                "id": fb_id, "account": "health-daily", "network": "facebook",
                "type": "reel", "message": caption,
                # video_path stays for local runs; video_src is what the CI
                # runner uses, since mp4s are no longer tracked in this repo.
                "video_path": video_path.relative_to(_HERE).as_posix(),
                "video_src": video_store.upload(video_path),
                "when": when, "status": "pending",
            })
            n += 1

        if ig_id not in ids_now:
            items.append({
                "id": ig_id, "account": "health-daily", "network": "instagram",
                "type": "reel", "message": caption, "video_url": video_url,
                "when": when, "status": "pending",
            })
            n += 1

        save(q)
        have = {i.get("id") for i in items}
        print(f"  queued {slug} for {when}")

    print(f"\nqueued {n} new items")


if __name__ == "__main__":
    args = sys.argv[1:]
    stock = "--stock" in args
    args = [a for a in args if a != "--stock"]
    if len(args) != 1:
        print("usage: python hd_reel_enqueue.py <content_module_name> [--stock]")
        sys.exit(1)
    main(args[0], stock=stock)
