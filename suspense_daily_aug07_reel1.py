# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #1, Aug 7. "The Parking Garage" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "My office building's parking garage\nhas 3 levels.",
  "narration": "My office building's parking garage has three levels."},
 {"kind": "beat", "text": "P1, P2, P3.\nThat's what the signs say.",
  "narration": "P one, P two, P three. That's what the signs say."},
 {"kind": "beat", "text": "Last night, I parked on P2\nlike always.",
  "narration": "Last night, I parked on P two like always."},
 {"kind": "beat", "text": "When I came back,\nmy car was gone.",
  "narration": "When I came back, my car was gone."},
 {"kind": "hallway", "caption": "I searched every level.\n*Nothing.*",
  "narration": "I searched every level. Nothing."},
 {"kind": "beat", "text": "Then I noticed\nan elevator button I'd never seen.",
  "narration": "Then I noticed an elevator button I'd never seen."},
 {"kind": "beat", "text": "*P4.*\nBelow the lowest level.",
  "narration": "P four. Below the lowest level."},
 {"kind": "door", "caption": "The elevator doors\nwere already open, waiting.", "ajar": True,
  "narration": "The elevator doors were already open, waiting."},
 {"kind": "beat", "text": "I didn't press anything.\nThe doors closed on their own.",
  "narration": "I didn't press anything. The doors closed on their own."},
 {"kind": "clock", "caption": "The display showed\n*going down*, past P3.", "hour": 11, "minute": 40,
  "narration": "The display showed going down, past P three."},
 {"kind": "beat", "text": "The doors opened\non a level with no lights.",
  "narration": "The doors opened on a level with no lights."},
 {"kind": "beat", "text": "My car was there.\nParked perfectly, facing the wrong way.",
  "narration": "My car was there. Parked perfectly, facing the wrong way."},
 {"kind": "beat", "text": "I got in and drove\nas fast as I could toward the exit.",
  "narration": "I got in and drove as fast as I could toward the exit."},
 {"kind": "end", "text": "This morning, I asked security about P4.\n*\"There's no P4. There's only ever been three levels.\"*",
  "question": "Where was my car really parked?",
  "narration": "This morning, I asked security about P four. There's no P four. There's only ever been three levels."},
]

OUT = "images/suspense_daily/aug07_reel1.mp4"
WORK = "images/suspense_daily/aug07_reel1_work"
STATE = "suspense_daily_aug07_reel1_state.json"
LOCK = "suspense_daily_aug07_reel1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
