# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #3, Aug 8. "The Mirror" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I noticed it\nbrushing my teeth.",
  "narration": "I noticed it brushing my teeth."},
 {"kind": "beat", "text": "My reflection\nwas a half-second behind.",
  "narration": "My reflection was a half second behind."},
 {"kind": "beat", "text": "I moved my hand.\nIt followed, just slightly late.",
  "narration": "I moved my hand. It followed, just slightly late."},
 {"kind": "beat", "text": "I told myself\nI was just tired.",
  "narration": "I told myself I was just tired."},
 {"kind": "beat", "text": "The next morning,\nsame thing. A little more delay.",
  "narration": "The next morning, same thing. A little more delay."},
 {"kind": "window", "caption": "I covered every mirror\nin the house.", "silhouette": False,
  "narration": "I covered every mirror in the house."},
 {"kind": "beat", "text": "It didn't help.\nI could still feel it, watching from somewhere.",
  "narration": "It didn't help. I could still feel it, watching from somewhere."},
 {"kind": "beat", "text": "Three nights later,\nI uncovered the bathroom mirror.",
  "narration": "Three nights later, I uncovered the bathroom mirror."},
 {"kind": "beat", "text": "I stood perfectly still.\nWaiting.",
  "narration": "I stood perfectly still. Waiting."},
 {"kind": "clock", "caption": "For *ten full seconds*,\nnothing moved.", "hour": 11, "minute": 30,
  "narration": "For ten full seconds, nothing moved."},
 {"kind": "beat", "text": "Then my reflection\nblinked. *I hadn't.*",
  "narration": "Then my reflection blinked. I hadn't."},
 {"kind": "beat", "text": "It smiled.\nI wasn't smiling.",
  "narration": "It smiled. I wasn't smiling."},
 {"kind": "beat", "text": "I backed away slowly.\nIt stayed exactly where I'd been standing.",
  "narration": "I backed away slowly. It stayed exactly where I'd been standing."},
 {"kind": "end", "text": "It's still in there.\n*Waiting for me to look again.*",
  "question": "Would you look again?",
  "narration": "It's still in there. Waiting for me to look again."},
]

OUT = "images/suspense_daily/aug08_reel3.mp4"
WORK = "images/suspense_daily/aug08_reel3_work"
STATE = "suspense_daily_aug08_reel3_state.json"
LOCK = "suspense_daily_aug08_reel3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
