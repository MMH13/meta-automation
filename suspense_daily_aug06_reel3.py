# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #3, Aug 6. "The Voicemail" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I found an old answering machine\nin my grandmother's attic.",
  "narration": "I found an old answering machine in my grandmother's attic."},
 {"kind": "beat", "text": "One saved message.\nNever played.",
  "narration": "One saved message. Never played."},
 {"kind": "beat", "text": "I pressed play,\njust out of curiosity.",
  "narration": "I pressed play, just out of curiosity."},
 {"kind": "beat", "text": "It was my own voice.\n*Saying my name.*",
  "narration": "It was my own voice. Saying my name."},
 {"kind": "beat", "text": "\"*Don't come home tonight.*\"\nThat's all it said.",
  "narration": "Don't come home tonight. That's all it said."},
 {"kind": "beat", "text": "The message was dated\nfrom *before I was born*.",
  "narration": "The message was dated from before I was born."},
 {"kind": "house", "caption": "I called my mother\nto ask about it.", "lit_window": False,
  "narration": "I called my mother to ask about it."},
 {"kind": "beat", "text": "She went quiet\nfor a long time.",
  "narration": "She went quiet for a long time."},
 {"kind": "beat", "text": "She said the machine\nbelonged to my grandmother's *sister*.",
  "narration": "She said the machine belonged to my grandmother's sister."},
 {"kind": "beat", "text": "A sister\nI'd never heard of.",
  "narration": "A sister I'd never heard of."},
 {"kind": "clock", "caption": "She disappeared\nthe night of *that recording*.", "hour": 11, "minute": 59,
  "narration": "She disappeared the night of that recording."},
 {"kind": "beat", "text": "No one ever found her.\nThe family stopped talking about it.",
  "narration": "No one ever found her. The family stopped talking about it."},
 {"kind": "beat", "text": "Tonight,\nI'm staying somewhere else.",
  "narration": "Tonight, I'm staying somewhere else."},
 {"kind": "end", "text": "But my phone just buzzed.\n*A voicemail. No caller ID.*",
  "question": "Would you listen to it?",
  "narration": "But my phone just buzzed. A voicemail. No caller I D."},
]

OUT = "images/suspense_daily/aug06_reel3.mp4"
WORK = "images/suspense_daily/aug06_reel3_work"
STATE = "suspense_daily_aug06_reel3_state.json"
LOCK = "suspense_daily_aug06_reel3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
