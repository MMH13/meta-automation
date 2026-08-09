# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #2, Aug 5. "The Group Chat" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "Our friend group chat\nhas 8 members.",
  "narration": "Our friend group chat has eight members."},
 {"kind": "beat", "text": "Last night, a 9th name\nappeared in the member list.",
  "narration": "Last night, a ninth name appeared in the member list."},
 {"kind": "beat", "text": "No one added them.\nNo one recognized the name.",
  "narration": "No one added them. No one recognized the name."},
 {"kind": "beat", "text": "I asked in the chat\nwho they were.",
  "narration": "I asked in the chat who they were."},
 {"kind": "beat", "text": "The new member replied\nwith just one word.",
  "narration": "The new member replied with just one word."},
 {"kind": "beat", "text": "\"*Soon.*\"",
  "narration": "Soon."},
 {"kind": "beat", "text": "Everyone assumed it was a prank.\nSomeone's cousin, maybe.",
  "narration": "Everyone assumed it was a prank. Someone's cousin, maybe."},
 {"kind": "beat", "text": "Then the messages started.\nOne for each of us, sent privately.",
  "narration": "Then the messages started. One for each of us, sent privately."},
 {"kind": "beat", "text": "Each message named something\nonly that person could know.",
  "narration": "Each message named something only that person could know."},
 {"kind": "beat", "text": "My message said:\n\"*You still have the porch light on.*\"",
  "narration": "My message said: you still have the porch light on."},
 {"kind": "window", "caption": "I looked outside.\nThe porch light was on. *I never turned it on.*", "silhouette": False,
  "narration": "I looked outside. The porch light was on. I never turned it on."},
 {"kind": "beat", "text": "One by one,\neveryone left the chat.",
  "narration": "One by one, everyone left the chat."},
 {"kind": "beat", "text": "The 9th member\nstayed.",
  "narration": "The ninth member stayed."},
 {"kind": "end", "text": "This morning, a new message:\n*\"Don't leave. I just got here.\"*",
  "question": "Would you leave the chat?",
  "narration": "This morning, a new message: don't leave. I just got here."},
]

OUT = "images/suspense_daily/aug05_reel2.mp4"
WORK = "images/suspense_daily/aug05_reel2_work"
STATE = "suspense_daily_aug05_reel2_state.json"
LOCK = "suspense_daily_aug05_reel2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
