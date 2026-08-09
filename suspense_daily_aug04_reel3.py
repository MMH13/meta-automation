# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #3, Aug 4. "The Nightly Photo" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I take a photo\nof my apartment every night.",
  "narration": "I take a photo of my apartment every night."},
 {"kind": "beat", "text": "Just a habit.\nFor insurance, I told myself.",
  "narration": "Just a habit. For insurance, I told myself."},
 {"kind": "beat", "text": "Last week, I noticed something\nin the corner of one photo.",
  "narration": "Last week, I noticed something in the corner of one photo."},
 {"kind": "window", "caption": "A shape,\nnear the window.", "silhouette": True,
  "narration": "A shape, near the window."},
 {"kind": "beat", "text": "I checked the room.\nNothing there.",
  "narration": "I checked the room. Nothing there."},
 {"kind": "beat", "text": "I told myself\nit was a shadow.",
  "narration": "I told myself it was a shadow."},
 {"kind": "beat", "text": "The next night,\nthe shape was closer.",
  "narration": "The next night, the shape was closer."},
 {"kind": "beat", "text": "Still by the window.\nBut *further into the room*.",
  "narration": "Still by the window. But further into the room."},
 {"kind": "beat", "text": "I started checking every night.\nEach photo, a little closer.",
  "narration": "I started checking every night. Each photo, a little closer."},
 {"kind": "clock", "caption": "By the *seventh night*,\nit was standing by my bed.", "hour": 3, "minute": 0,
  "narration": "By the seventh night, it was standing by my bed."},
 {"kind": "beat", "text": "I stopped taking photos\nafter that.",
  "narration": "I stopped taking photos after that."},
 {"kind": "beat", "text": "But last night,\nmy phone camera turned on by itself.",
  "narration": "But last night, my phone camera turned on by itself."},
 {"kind": "end", "text": "I didn't take that photo.\n*Something else did.*",
  "question": "Would you look at what it captured?",
  "narration": "I didn't take that photo. Something else did."},
]

OUT = "images/suspense_daily/aug04_reel3.mp4"
WORK = "images/suspense_daily/aug04_reel3_work"
STATE = "suspense_daily_aug04_reel3_state.json"
LOCK = "suspense_daily_aug04_reel3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
