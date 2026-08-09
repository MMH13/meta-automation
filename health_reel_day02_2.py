# -*- coding: utf-8 -*-
"""Health Daily — reel day 2, #2. "Your Desk Is Quietly Hurting You"."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_health_reel import build

BEATS = [
 {"kind": "hook", "text": "Hours hunched at a screen\nadd up *faster* than you think.",
  "narration": "Hours hunched at a screen add up faster than you think."},
 {"kind": "beat", "text": "Your neck carries extra weight\nevery time you look down.",
  "narration": "Your neck carries extra weight every time you look down."},
 {"kind": "beat", "text": "Set a timer:\nevery 20 minutes,\nlook up and roll your shoulders.",
  "narration": "Set a timer: every twenty minutes, look up and roll your shoulders."},
 {"kind": "beat", "text": "Small adjustment.\n*Real relief* by evening.",
  "narration": "Small adjustment. Real relief by evening."},
 {"kind": "end", "text": "Try it\n*right now.*",
  "question": "Neck or back stiff by evening?",
  "narration": "Try it right now."},
]

OUT = "images/health_reels/day02_2.mp4"
WORK = "images/health_reels/day02_2_work"
STATE = "health_reel_day02_2_state.json"
LOCK = "health_reel_day02_2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
