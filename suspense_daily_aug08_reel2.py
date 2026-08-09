# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #2, Aug 8. "The Night Bus" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I take the last bus\nhome every night.",
  "narration": "I take the last bus home every night."},
 {"kind": "beat", "text": "Same route.\nSame ten stops.",
  "narration": "Same route. Same ten stops."},
 {"kind": "beat", "text": "Last night,\nthe driver announced an eleventh.",
  "narration": "Last night, the driver announced an eleventh."},
 {"kind": "beat", "text": "\"*Mill Street.*\"\nI'd never heard of it.",
  "narration": "Mill Street. I'd never heard of it."},
 {"kind": "beat", "text": "No one else on the bus\nreacted at all.",
  "narration": "No one else on the bus reacted at all."},
 {"kind": "window", "caption": "I looked at the route map\non my phone.", "silhouette": False,
  "narration": "I looked at the route map on my phone."},
 {"kind": "beat", "text": "Ten stops.\nMill Street wasn't one of them.",
  "narration": "Ten stops. Mill Street wasn't one of them."},
 {"kind": "beat", "text": "The bus slowed down\nanyway.",
  "narration": "The bus slowed down anyway."},
 {"kind": "clock", "caption": "The doors opened\nat *exactly* midnight.", "hour": 0, "minute": 0,
  "narration": "The doors opened at exactly midnight."},
 {"kind": "beat", "text": "No stop.\nJust dark trees on both sides.",
  "narration": "No stop. Just dark trees on both sides."},
 {"kind": "beat", "text": "One passenger\nstood up and got off.",
  "narration": "One passenger stood up and got off."},
 {"kind": "beat", "text": "I'd never noticed them\nsitting there before that moment.",
  "narration": "I'd never noticed them sitting there before that moment."},
 {"kind": "beat", "text": "The driver didn't say anything.\nThe doors just closed.",
  "narration": "The driver didn't say anything. The doors just closed."},
 {"kind": "end", "text": "Tonight, the driver announced\n*Mill Street* again.",
  "question": "Would you get off?",
  "narration": "Tonight, the driver announced Mill Street again."},
]

OUT = "images/suspense_daily/aug08_reel2.mp4"
WORK = "images/suspense_daily/aug08_reel2_work"
STATE = "suspense_daily_aug08_reel2_state.json"
LOCK = "suspense_daily_aug08_reel2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
