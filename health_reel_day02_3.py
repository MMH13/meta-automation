# -*- coding: utf-8 -*-
"""Health Daily — reel day 2, #3. "The 60-Second Stress Reset"."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_health_reel import build

BEATS = [
 {"kind": "hook", "text": "Stressed?\nYou don't need *20 minutes*.",
  "narration": "Stressed? You don't need twenty minutes."},
 {"kind": "beat", "text": "Breathe in\nfor 4 seconds.",
  "narration": "Breathe in for four seconds."},
 {"kind": "beat", "text": "Out\nfor 6 seconds.",
  "narration": "Out for six seconds."},
 {"kind": "beat", "text": "The longer exhale\ntells your body to calm down.",
  "narration": "The longer exhale tells your body to calm down."},
 {"kind": "end", "text": "Five rounds.\n*That's it.*",
  "question": "Feel calmer after 5 rounds?",
  "narration": "Five rounds. That's it."},
]

OUT = "images/health_reels/day02_3.mp4"
WORK = "images/health_reels/day02_3_work"
STATE = "health_reel_day02_3_state.json"
LOCK = "health_reel_day02_3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
