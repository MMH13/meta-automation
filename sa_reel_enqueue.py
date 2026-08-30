# -*- coding: utf-8 -*-
"""Suspense Ahead — reel batch enqueuer, routing through queue.json instead
of one-shot publish scripts (the same architecture fix applied to Health
Daily: only what's due posts, paced, instead of a manual batch blast).
Suspense Ahead is FB-only (no ig_user_id in accounts.json), so each reel
gets exactly ONE queue item (network:facebook, type:reel, video_path) - no
public-repo upload step needed.

Slug convention: "..._d<day>_<slot>_...", day is 1-based, slot is one of
s1/s2/s3 (short reels) or lf (long-form). Mapped to SHORT_HOURS[0..2] and
LONGFORM_HOUR respectively. Chosen to interleave with the card queue's own
slots (10/13/16/19/21/23 UTC) without colliding.

Usage:
    python sa_reel_enqueue.py suspense_reel_content1
"""
import importlib
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from aug_common import load, save
import video_store
from video_suspense_stock import build as build_reel

_HERE = Path(__file__).parent
START_DATE = date(2026, 8, 11)
SHORT_HOURS = [0, 6, 15]  # UTC
LONGFORM_HOUR = 18

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

_SLUG_RE = re.compile(r"_d(\d+)_(s1|s2|s3|lf)_")


def _slot_for(slug):
    m = _SLUG_RE.search(slug)
    if not m:
        raise ValueError(f"slug {slug!r} doesn't match the _d<day>_<s1|s2|s3|lf>_ convention")
    day_idx, tag = int(m.group(1)) - 1, m.group(2)
    d = START_DATE + timedelta(days=day_idx)
    hour = LONGFORM_HOUR if tag == "lf" else SHORT_HOURS[int(tag[1]) - 1]
    return f"{d.isoformat()}T{hour:02d}:00:00+00:00"


def main(module_name):
    mod = importlib.import_module(module_name)
    reels = mod.REELS

    out_dir = _HERE / "images" / f"suspense_reels_{module_name.replace('suspense_reel_', '')}"
    out_dir.mkdir(parents=True, exist_ok=True)

    have = {i.get("id") for i in load()["items"]}
    n = 0

    for slug, beats, caption in reels:
        fb_id = f"sa-cadence-{slug}-fb"
        if fb_id in have:
            continue

        video_path = out_dir / f"{slug}.mp4"
        work_dir = out_dir / f"{slug}_work"
        video_state = out_dir / f"{slug}_state.json"
        lock = out_dir / f"{slug}.lock"

        if not video_path.is_file():
            print(f"\n=== building {slug} ({len(beats)} beats) ===")
            build_reel(beats, str(video_path), str(work_dir), str(video_state), str(lock),
                      VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)

        when = _slot_for(slug)

        q = load()
        items = q["items"]
        ids_now = {i.get("id") for i in items}
        if fb_id not in ids_now:
            items.append({
                "id": fb_id, "account": "suspense-ahead", "network": "facebook",
                "type": "reel", "message": caption,
                # video_path stays for local runs; video_src is what the CI
                # runner uses, since mp4s are no longer tracked in this repo.
                "video_path": video_path.relative_to(_HERE).as_posix(),
                "video_src": video_store.upload(video_path),
                "when": when, "status": "pending",
            })
            n += 1
            save(q)
            have = {i.get("id") for i in items}

        print(f"  queued {slug} for {when}")

    print(f"\nqueued {n} new items")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python sa_reel_enqueue.py <content_module_name>")
        sys.exit(1)
    main(sys.argv[1])
