# -*- coding: utf-8 -*-
"""Health Daily — reel day 1, #3. "The Sleep Habit Everyone Skips"."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_health_reel import build

BEATS = [
 {"kind": "hook", "text": "You can do everything else right\nand still sleep *badly*.",
  "narration": "You can do everything else right and still sleep badly."},
 {"kind": "beat", "text": "If your phone\nis still in your hand.",
  "narration": "If your phone is still in your hand."},
 {"kind": "beat", "text": "Blue light and scrolling\nkeep your brain\nin 'alert' mode.",
  "narration": "Blue light and scrolling keep your brain in alert mode."},
 {"kind": "beat", "text": "Put it down\n*30 minutes* before\nyou actually want to sleep.",
  "narration": "Put it down thirty minutes before you actually want to sleep."},
 {"kind": "end", "text": "Your body needs\n*boredom* to switch off.",
  "question": "Phone in bed tonight — yes or no?",
  "narration": "Your body needs boredom to switch off."},
]

OUT = "images/health_reels/day01_3.mp4"
WORK = "images/health_reels/day01_3_work"
STATE = "health_reel_day01_3_state.json"
LOCK = "health_reel_day01_3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
