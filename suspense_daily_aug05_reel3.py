# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #3, Aug 5. "The Attic" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "The attic in my new house\nhas no door.",
  "narration": "The attic in my new house has no door."},
 {"kind": "beat", "text": "Just a hatch in the ceiling,\npainted shut years ago.",
  "narration": "Just a hatch in the ceiling, painted shut years ago."},
 {"kind": "beat", "text": "The realtor said\nno one's been up there in a decade.",
  "narration": "The realtor said no one's been up there in a decade."},
 {"kind": "house", "caption": "I didn't think about it again.\nUntil the first week.", "lit_window": True,
  "narration": "I didn't think about it again. Until the first week."},
 {"kind": "beat", "text": "Every night, around 2 AM,\nI heard footsteps above my bedroom.",
  "narration": "Every night, around two A M, I heard footsteps above my bedroom."},
 {"kind": "beat", "text": "Slow. Deliberate.\n*Directly over my bed.*",
  "narration": "Slow. Deliberate. Directly over my bed."},
 {"kind": "beat", "text": "I told myself it was the house settling.\nOld houses do that.",
  "narration": "I told myself it was the house settling. Old houses do that."},
 {"kind": "clock", "caption": "But it happened at *2 AM*.\nEvery single night.", "hour": 2, "minute": 0,
  "narration": "But it happened at two A M. Every single night."},
 {"kind": "beat", "text": "I got a ladder.\nDecided to check the hatch myself.",
  "narration": "I got a ladder. Decided to check the hatch myself."},
 {"kind": "beat", "text": "The paint was cracked\nalong one edge. *Recently.*",
  "narration": "The paint was cracked along one edge. Recently."},
 {"kind": "door", "caption": "Like something had been\nopening it from the inside.", "ajar": True,
  "narration": "Like something had been opening it from the inside."},
 {"kind": "beat", "text": "I pushed the hatch.\nIt wouldn't budge.",
  "narration": "I pushed the hatch. It wouldn't budge."},
 {"kind": "beat", "text": "Then I heard it.\nFootsteps, right above me, *right now*.",
  "narration": "Then I heard it. Footsteps, right above me, right now."},
 {"kind": "end", "text": "I climbed down.\nI haven't looked up since.",
  "question": "What do you think is up there?",
  "narration": "I climbed down. I haven't looked up since."},
]

OUT = "images/suspense_daily/aug05_reel3.mp4"
WORK = "images/suspense_daily/aug05_reel3_work"
STATE = "suspense_daily_aug05_reel3_state.json"
LOCK = "suspense_daily_aug05_reel3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
