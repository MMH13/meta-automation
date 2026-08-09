# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #2, Aug 7. "The Text From Myself" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I got a text\nfrom my own number.",
  "narration": "I got a text from my own number."},
 {"kind": "beat", "text": "Just one word:\n\"*Behind.*\"",
  "narration": "Just one word: behind."},
 {"kind": "beat", "text": "I laughed it off.\nProbably a spoofed number, a scam.",
  "narration": "I laughed it off. Probably a spoofed number, a scam."},
 {"kind": "beat", "text": "Then it texted again.\n\"*Look behind you.*\"",
  "narration": "Then it texted again: look behind you."},
 {"kind": "window", "caption": "I was home alone.\nEvery door locked.", "silhouette": False,
  "narration": "I was home alone. Every door locked."},
 {"kind": "beat", "text": "I turned around anyway.\nNothing there.",
  "narration": "I turned around anyway. Nothing there."},
 {"kind": "beat", "text": "I texted back:\n\"who is this.\"",
  "narration": "I texted back: who is this."},
 {"kind": "beat", "text": "The reply came instantly.\n\"*You know who this is.*\"",
  "narration": "The reply came instantly: you know who this is."},
 {"kind": "clock", "caption": "The timestamp\nmatched *my own clock*, to the second.", "hour": 11, "minute": 34,
  "narration": "The timestamp matched my own clock, to the second."},
 {"kind": "beat", "text": "I called my own number\nto see who'd answer.",
  "narration": "I called my own number to see who'd answer."},
 {"kind": "beat", "text": "It rang once.\nThen my phone in my hand rang too.",
  "narration": "It rang once. Then my phone in my hand rang too."},
 {"kind": "beat", "text": "*Both at the same time.*",
  "narration": "Both at the same time."},
 {"kind": "beat", "text": "I hung up.\nOne more text came through.",
  "narration": "I hung up. One more text came through."},
 {"kind": "end", "text": "\"*Almost found you.*\"",
  "question": "Would you check behind you right now?",
  "narration": "Almost found you."},
]

OUT = "images/suspense_daily/aug07_reel2.mp4"
WORK = "images/suspense_daily/aug07_reel2_work"
STATE = "suspense_daily_aug07_reel2_state.json"
LOCK = "suspense_daily_aug07_reel2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
