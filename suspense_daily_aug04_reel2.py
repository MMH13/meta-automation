# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #2, Aug 4. "Floor 13" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "My office building\nhas 13 floors.",
  "narration": "My office building has thirteen floors."},
 {"kind": "beat", "text": "But the elevator panel\nonly goes up to *12*.",
  "narration": "But the elevator panel only goes up to twelve."},
 {"kind": "beat", "text": "I asked security about it once.\nHe just changed the subject.",
  "narration": "I asked security about it once. He just changed the subject."},
 {"kind": "hallway", "caption": "Late one night,\nI worked past everyone else.",
  "narration": "Late one night, I worked past everyone else."},
 {"kind": "beat", "text": "I got in the elevator.\nPressed 1 for the lobby.",
  "narration": "I got in the elevator. Pressed one for the lobby."},
 {"kind": "beat", "text": "The doors closed.\n*Then the button for 13 lit up.*",
  "narration": "The doors closed. Then the button for thirteen lit up."},
 {"kind": "beat", "text": "I hadn't touched it.",
  "narration": "I hadn't touched it."},
 {"kind": "clock", "caption": "The display read\n*11:47 PM.*", "hour": 11, "minute": 47,
  "narration": "The display read eleven forty seven P M."},
 {"kind": "beat", "text": "The elevator went up.\n*Not down.*",
  "narration": "The elevator went up. Not down."},
 {"kind": "door", "caption": "The doors opened\non a floor that shouldn't exist.", "ajar": True,
  "narration": "The doors opened on a floor that shouldn't exist."},
 {"kind": "beat", "text": "A long hallway.\nOne light flickering at the end.",
  "narration": "A long hallway. One light flickering at the end."},
 {"kind": "beat", "text": "I pressed the lobby button\nover and over.",
  "narration": "I pressed the lobby button over and over."},
 {"kind": "beat", "text": "The doors finally closed.\nI didn't look back.",
  "narration": "The doors finally closed. I didn't look back."},
 {"kind": "end", "text": "Next morning, security said-\n*\"There's only 12.\nThere's always been 12.\"*",
  "question": "Then what floor did I visit?",
  "narration": "Next morning, security said: there's only twelve. There's always been twelve."},
]

OUT = "images/suspense_daily/aug04_reel2.mp4"
WORK = "images/suspense_daily/aug04_reel2_work"
STATE = "suspense_daily_aug04_reel2_state.json"
LOCK = "suspense_daily_aug04_reel2.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
