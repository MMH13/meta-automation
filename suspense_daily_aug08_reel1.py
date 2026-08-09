# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #1, Aug 8. "The Package" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "A package arrived\naddressed to me.",
  "narration": "A package arrived addressed to me."},
 {"kind": "beat", "text": "No return address.\nNo shipping label, just my name.",
  "narration": "No return address. No shipping label, just my name."},
 {"kind": "beat", "text": "I hadn't ordered\nanything.",
  "narration": "I hadn't ordered anything."},
 {"kind": "beat", "text": "Inside was a single photo.\nOf my *front door*.",
  "narration": "Inside was a single photo. Of my front door."},
 {"kind": "house", "caption": "Taken from across the street.\nLast night, based on the lighting.", "lit_window": True,
  "narration": "Taken from across the street. Last night, based on the lighting."},
 {"kind": "beat", "text": "I checked my own doorbell footage.\nNo one had been there.",
  "narration": "I checked my own doorbell footage. No one had been there."},
 {"kind": "beat", "text": "Two days later,\nanother package.",
  "narration": "Two days later, another package."},
 {"kind": "beat", "text": "Same no return address.\nA new photo inside.",
  "narration": "Same no return address. A new photo inside."},
 {"kind": "beat", "text": "This one was taken\n*from inside my house*.",
  "narration": "This one was taken from inside my house."},
 {"kind": "window", "caption": "Looking out at the street\nfrom my own living room.", "silhouette": False,
  "narration": "Looking out at the street, from my own living room."},
 {"kind": "beat", "text": "I checked every lock.\nEverything secure.",
  "narration": "I checked every lock. Everything secure."},
 {"kind": "clock", "caption": "The photo's timestamp\nread *2:14 AM* last night.", "hour": 2, "minute": 14,
  "narration": "The photo's timestamp read two fourteen A M last night."},
 {"kind": "beat", "text": "I was asleep\nat 2:14 AM.",
  "narration": "I was asleep at two fourteen A M."},
 {"kind": "end", "text": "Today, a third package arrived.\n*I haven't opened it yet.*",
  "question": "Would you open it?",
  "narration": "Today, a third package arrived. I haven't opened it yet."},
]

OUT = "images/suspense_daily/aug08_reel1.mp4"
WORK = "images/suspense_daily/aug08_reel1_work"
STATE = "suspense_daily_aug08_reel1_state.json"
LOCK = "suspense_daily_aug08_reel1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
