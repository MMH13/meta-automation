# -*- coding: utf-8 -*-
"""Health Daily — reel day 1, #2. "Why You're Always Tired at 3PM"."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_health_reel import build

BEATS = [
 {"kind": "hook", "text": "That 3 PM crash\nisn't *random*.",
  "narration": "That three P M crash isn't random."},
 {"kind": "beat", "text": "It's often a mix of\nlunch, dehydration,\nand low light exposure.",
  "narration": "It's often a mix of lunch, dehydration, and low light exposure."},
 {"kind": "beat", "text": "Reaching for coffee\nonly masks it\nfor an hour.",
  "narration": "Reaching for coffee only masks it for an hour."},
 {"kind": "beat", "text": "Try water, a 5-minute walk,\nand natural light\ninstead.",
  "narration": "Try water, a five minute walk, and natural light instead."},
 {"kind": "end", "text": "Your energy\n*comes back faster* than you'd think.",
  "question": "When does your energy usually dip?",
  "narration": "Your energy comes back faster than you'd think."},
]

OUT = "images/health_reels/day01_2.mp4"
WORK = "images/health_reels/day01_2_work"
STATE = "health_reel_day01_2_state.json"
LOCK = "health_reel_day01_2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
