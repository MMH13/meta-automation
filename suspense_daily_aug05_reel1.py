# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #1, Aug 5. "The Rideshare" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I ordered a rideshare\nat 2 AM.",
  "narration": "I ordered a rideshare at two A M."},
 {"kind": "beat", "text": "The driver's name matched.\nThe car matched. Everything checked out.",
  "narration": "The driver's name matched. The car matched. Everything checked out."},
 {"kind": "beat", "text": "Twenty minutes in,\nI noticed something odd.",
  "narration": "Twenty minutes in, I noticed something odd."},
 {"kind": "beat", "text": "My GPS showed we'd already passed\nmy drop-off. *Twice.*",
  "narration": "My GPS showed we'd already passed my drop-off. Twice."},
 {"kind": "window", "caption": "I looked outside.\nNone of the streets looked familiar.", "silhouette": False,
  "narration": "I looked outside. None of the streets looked familiar."},
 {"kind": "beat", "text": "I asked him to pull over.\nHe just kept driving, calm as ever.",
  "narration": "I asked him to pull over. He just kept driving, calm as ever."},
 {"kind": "beat", "text": "The doors locked automatically.\nI hadn't touched anything.",
  "narration": "The doors locked automatically. I hadn't touched anything."},
 {"kind": "beat", "text": "I asked again, louder.\nHe finally spoke.",
  "narration": "I asked again, louder. He finally spoke."},
 {"kind": "beat", "text": "\"*Almost there.*\"\nHis voice didn't match his profile picture.",
  "narration": "Almost there. His voice didn't match his profile picture."},
 {"kind": "beat", "text": "I checked the app again.\nThe photo now showed a different face.",
  "narration": "I checked the app again. The photo now showed a different face."},
 {"kind": "clock", "caption": "The trip timer read\n*47 minutes* for a 12-minute ride.", "hour": 2, "minute": 47,
  "narration": "The trip timer read forty seven minutes, for a twelve minute ride."},
 {"kind": "beat", "text": "I grabbed the door handle.\nIt wouldn't open.",
  "narration": "I grabbed the door handle. It wouldn't open."},
 {"kind": "beat", "text": "Then, without warning,\nthe car stopped.",
  "narration": "Then, without warning, the car stopped."},
 {"kind": "end", "text": "He turned around and smiled.\n*\"You were quiet this whole time. Good.\"*",
  "question": "Would you have stayed quiet too?",
  "narration": "He turned around and smiled. You were quiet this whole time. Good."},
]

OUT = "images/suspense_daily/aug05_reel1.mp4"
WORK = "images/suspense_daily/aug05_reel1_work"
STATE = "suspense_daily_aug05_reel1_state.json"
LOCK = "suspense_daily_aug05_reel1.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
