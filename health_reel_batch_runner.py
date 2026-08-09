# -*- coding: utf-8 -*-
"""Health Daily — generic reel batch runner. Builds, FB-publishes, and
IG-publishes every (slug, beats, caption) tuple from a given content module,
with a resumable per-batch JSON state file.

Usage:
    python health_reel_batch_runner.py health_reel_content3
"""
import importlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_health_reel import build as build_reel
from publish_reel import publish as publish_fb
from publish_ig_reel import publish as publish_ig

_HERE = Path(__file__).parent


def main(module_name):
    mod = importlib.import_module(module_name)
    reels = mod.REELS

    out_dir = _HERE / "images" / f"health_reels_{module_name.replace('health_reel_', '')}"
    cap_dir = out_dir / "captions"
    state_path = _HERE / f"{module_name}_state.json"
    out_dir.mkdir(parents=True, exist_ok=True)
    cap_dir.mkdir(parents=True, exist_ok=True)

    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.is_file() else {}

    def _save():
        state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

    for slug, beats, caption in reels:
        rec = state.setdefault(slug, {})
        video_path = out_dir / f"{slug}.mp4"
        work_dir = out_dir / f"{slug}_work"
        video_state = out_dir / f"{slug}_state.json"
        lock = out_dir / f"{slug}.lock"
        cap_path = cap_dir / f"{slug}.txt"

        if not rec.get("built"):
            print(f"\n=== building {slug} ===")
            build_reel(beats, str(video_path), str(work_dir), str(video_state), str(lock))
            rec["built"] = True
            _save()

        cap_path.write_text(caption, encoding="utf-8")

        if not rec.get("fb_video_id"):
            print(f"  publishing {slug} to FB...")
            r = publish_fb("health-daily", str(video_path), caption)
            rec["fb_video_id"] = r["video_id"]
            rec["fb_permalink"] = r.get("permalink")
            _save()
            print(f"  FB: {r}")

        if not rec.get("ig_media_id"):
            print(f"  publishing {slug} to IG...")
            try:
                r = publish_ig("health-daily", str(video_path), caption, asset_name=f"{slug}.mp4")
                rec["ig_media_id"] = r["ig_media_id"]
                rec["ig_permalink"] = r.get("permalink")
                _save()
                print(f"  IG: {r}")
            except Exception as e:
                print(f"  IG FAILED for {slug}: {e}")
                print("  (will retry on next run — not blocking the rest of the batch)")

    print("\n=== batch summary ===")
    for slug, *_ in reels:
        rec = state.get(slug, {})
        print(f"  {slug}: built={rec.get('built', False)} fb={bool(rec.get('fb_video_id'))} ig={bool(rec.get('ig_media_id'))}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python health_reel_batch_runner.py <content_module_name>")
        sys.exit(1)
    main(sys.argv[1])
