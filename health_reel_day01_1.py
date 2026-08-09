# -*- coding: utf-8 -*-
"""Health Daily — reel day 1, #1. "The 2-Minute Morning Reset"."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_health_reel import build

BEATS = [
 {"kind": "hook", "text": "Your first 2 minutes awake\nset the tone for your *whole day*.",
  "narration": "Your first two minutes awake set the tone for your whole day."},
 {"kind": "beat", "text": "Most people reach\nfor their phone first.",
  "narration": "Most people reach for their phone first."},
 {"kind": "beat", "text": "Try this instead:\nopen a window, drink water,\ntake 3 deep breaths.",
  "narration": "Try this instead: open a window, drink water, take three deep breaths."},
 {"kind": "beat", "text": "No app.\nNo notification.\nJust you and your body waking up.",
  "narration": "No app. No notification. Just you and your body waking up."},
 {"kind": "end", "text": "Small reset.\n*Big difference by 9 AM.*",
  "question": "What's the first thing you do when you wake up?",
  "narration": "Small reset. Big difference by nine A M."},
]

OUT = "images/health_reels/day01_1.mp4"
WORK = "images/health_reels/day01_1_work"
STATE = "health_reel_day01_1_state.json"
LOCK = "health_reel_day01_1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
