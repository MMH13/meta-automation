# -*- coding: utf-8 -*-
"""Health Daily — reel day 2, #1. "The Hydration Check You're Skipping"."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_health_reel import build

BEATS = [
 {"kind": "hook", "text": "You don't need to count\nglasses of water.",
  "narration": "You don't need to count glasses of water."},
 {"kind": "beat", "text": "Check the color instead.\n*Pale yellow* = well hydrated.",
  "narration": "Check the color instead. Pale yellow means well hydrated."},
 {"kind": "beat", "text": "Dark yellow?\nYour body's asking for more.",
  "narration": "Dark yellow? Your body's asking for more."},
 {"kind": "beat", "text": "Thirst is a real signal too —\nit's not a failure.",
  "narration": "Thirst is a real signal too. It's not a failure."},
 {"kind": "end", "text": "Simple check.\n*No app needed.*",
  "question": "What color was it today?",
  "narration": "Simple check. No app needed."},
]

OUT = "images/health_reels/day02_1.mp4"
WORK = "images/health_reels/day02_1_work"
STATE = "health_reel_day02_1_state.json"
LOCK = "health_reel_day02_1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
