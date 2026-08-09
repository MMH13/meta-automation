# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #2, Aug 6. "Room 214" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "The motel clerk\ngave me room 214.",
  "narration": "The motel clerk gave me room two fourteen."},
 {"kind": "beat", "text": "\"*Don't use the door\nto 212,*\" she said.",
  "narration": "Don't use the door to two twelve, she said."},
 {"kind": "beat", "text": "I hadn't noticed\nthere was a connecting door.",
  "narration": "I hadn't noticed there was a connecting door."},
 {"kind": "beat", "text": "I laughed it off.\nProbably just noisy neighbors.",
  "narration": "I laughed it off. Probably just noisy neighbors."},
 {"kind": "door", "caption": "The connecting door\nhad no lock. Just a bolt.", "ajar": False,
  "narration": "The connecting door had no lock. Just a bolt."},
 {"kind": "beat", "text": "Around midnight,\nI heard the bolt slide.",
  "narration": "Around midnight, I heard the bolt slide."},
 {"kind": "beat", "text": "Slow.\n*On its own.*",
  "narration": "Slow. On its own."},
 {"kind": "beat", "text": "I turned on every light\nin the room.",
  "narration": "I turned on every light in the room."},
 {"kind": "beat", "text": "The bolt slid back\nthe *other* way.",
  "narration": "The bolt slid back the other way."},
 {"kind": "clock", "caption": "The clock read\n*12:14 AM.*", "hour": 0, "minute": 14,
  "narration": "The clock read twelve fourteen A M."},
 {"kind": "beat", "text": "Room *214*.\nThe numbers weren't a coincidence.",
  "narration": "Room two fourteen. The numbers weren't a coincidence."},
 {"kind": "beat", "text": "I checked the door again.\nStill bolted. From my side.",
  "narration": "I checked the door again. Still bolted. From my side."},
 {"kind": "beat", "text": "But now,\nI could hear breathing on the other side.",
  "narration": "But now, I could hear breathing on the other side."},
 {"kind": "end", "text": "I checked out at dawn.\n*The front desk said room 212 doesn't exist.*",
  "question": "What was on the other side?",
  "narration": "I checked out at dawn. The front desk said room two twelve doesn't exist."},
]

OUT = "images/suspense_daily/aug06_reel2.mp4"
WORK = "images/suspense_daily/aug06_reel2_work"
STATE = "suspense_daily_aug06_reel2_state.json"
LOCK = "suspense_daily_aug06_reel2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
