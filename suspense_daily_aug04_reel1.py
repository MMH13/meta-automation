# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #1, Aug 4. "The Landline" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I took a babysitting job\nfor a family I'd never met.",
  "narration": "I took a babysitting job for a family I'd never met."},
 {"kind": "beat", "text": "The mother left a note:\n*\"Don't answer the landline. Ever.\"*",
  "narration": "The mother left a note: don't answer the landline. Ever."},
 {"kind": "beat", "text": "I laughed.\nWho even uses a landline anymore?",
  "narration": "I laughed. Who even uses a landline anymore?"},
 {"kind": "house", "caption": "The house was quiet.\n*Too quiet.*", "lit_window": True,
  "narration": "The house was quiet. Too quiet."},
 {"kind": "beat", "text": "At 9 PM,\nthe landline rang.",
  "narration": "At nine P M, the landline rang."},
 {"kind": "beat", "text": "I let it go to voicemail.\nThe message was just static.",
  "narration": "I let it go to voicemail. The message was just static."},
 {"kind": "beat", "text": "Then, *three words*:\n\"Check the closet.\"",
  "narration": "Then, three words: check the closet."},
 {"kind": "door", "caption": "I checked the hallway closet.\nEmpty. Just coats.", "ajar": True,
  "narration": "I checked the hallway closet. Empty. Just coats."},
 {"kind": "beat", "text": "I told myself it was a prank.\nSome kid messing with the family.",
  "narration": "I told myself it was a prank. Some kid messing with the family."},
 {"kind": "clock", "caption": "At *10 PM*,\nthe landline rang again.", "hour": 10, "minute": 0,
  "narration": "At ten P M, the landline rang again."},
 {"kind": "beat", "text": "Same static.\nSame three words.",
  "narration": "Same static. Same three words."},
 {"kind": "beat", "text": "This time,\nI noticed something.",
  "narration": "This time, I noticed something."},
 {"kind": "beat", "text": "A coat in the closet\nthat *wasn't there before*.",
  "narration": "A coat in the closet that wasn't there before."},
 {"kind": "end", "text": "I called the mother.\nShe said- *\"We don't own a landline.\"*",
  "question": "What was ringing?",
  "narration": "I called the mother. She said: we don't own a landline."},
]

OUT = "images/suspense_daily/aug04_reel1.mp4"
WORK = "images/suspense_daily/aug04_reel1_work"
STATE = "suspense_daily_aug04_reel1_state.json"
LOCK = "suspense_daily_aug04_reel1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
