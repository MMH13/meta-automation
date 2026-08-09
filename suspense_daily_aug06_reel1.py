# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #1, Aug 6. "The Doorbell" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "My smart doorbell\nsent an alert at 3 AM.",
  "narration": "My smart doorbell sent an alert at three A M."},
 {"kind": "beat", "text": "Someone was standing\non my porch.",
  "narration": "Someone was standing on my porch."},
 {"kind": "beat", "text": "I checked the live feed.\nNo one was there.",
  "narration": "I checked the live feed. No one was there."},
 {"kind": "beat", "text": "I dismissed it.\nProbably a bug.",
  "narration": "I dismissed it. Probably a bug."},
 {"kind": "house", "caption": "The next night,\nthe same alert came.", "lit_window": True,
  "narration": "The next night, the same alert came."},
 {"kind": "beat", "text": "This time, I watched\nthe recording, frame by frame.",
  "narration": "This time, I watched the recording, frame by frame."},
 {"kind": "beat", "text": "For *one frame*,\nsomething was there.",
  "narration": "For one frame, something was there."},
 {"kind": "beat", "text": "Not a person.\nJust a shape, too tall for the porch light.",
  "narration": "Not a person. Just a shape, too tall for the porch light."},
 {"kind": "door", "caption": "I checked the lock.\nStill deadbolted from inside.", "ajar": False,
  "narration": "I checked the lock. Still deadbolted from inside."},
 {"kind": "clock", "caption": "The timestamp read\n*3:03 AM.* Exactly.", "hour": 3, "minute": 3,
  "narration": "The timestamp read three oh three A M. Exactly."},
 {"kind": "beat", "text": "Same time.\nEvery single night.",
  "narration": "Same time. Every single night."},
 {"kind": "beat", "text": "Last night,\nI decided to stay awake and watch.",
  "narration": "Last night, I decided to stay awake and watch."},
 {"kind": "beat", "text": "At 3:03, the doorbell rang.\nI looked at the live feed.",
  "narration": "At three oh three, the doorbell rang. I looked at the live feed."},
 {"kind": "end", "text": "The porch was empty.\n*But the doorbell was still ringing.*",
  "question": "Would you open the door?",
  "narration": "The porch was empty. But the doorbell was still ringing."},
]

OUT = "images/suspense_daily/aug06_reel1.mp4"
WORK = "images/suspense_daily/aug06_reel1_work"
STATE = "suspense_daily_aug06_reel1_state.json"
LOCK = "suspense_daily_aug06_reel1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
