# -*- coding: utf-8 -*-
"""Suspense Ahead — daily reel #3, Aug 7. "The Wedding Video" — original story."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_suspense_reel import build

BEATS = [
 {"kind": "hook", "text": "I rewatched my parents'\nwedding video last week.",
  "narration": "I rewatched my parents' wedding video last week."},
 {"kind": "beat", "text": "Old VHS, transferred to digital\nyears ago.",
  "narration": "Old V H S, transferred to digital years ago."},
 {"kind": "beat", "text": "I'd seen it a dozen times growing up.\nEvery face familiar.",
  "narration": "I'd seen it a dozen times growing up. Every face familiar."},
 {"kind": "beat", "text": "This time,\nI noticed someone new.",
  "narration": "This time, I noticed someone new."},
 {"kind": "beat", "text": "In the back row,\na man in a dark suit.",
  "narration": "In the back row, a man in a dark suit."},
 {"kind": "house", "caption": "No one in my family\nrecognized him.", "lit_window": False,
  "narration": "No one in my family recognized him."},
 {"kind": "beat", "text": "I paused the frame.\nHe was looking directly at the camera.",
  "narration": "I paused the frame. He was looking directly at the camera."},
 {"kind": "beat", "text": "Not at my parents.\n*At whoever was filming.*",
  "narration": "Not at my parents. At whoever was filming."},
 {"kind": "beat", "text": "I asked my mother\nif she remembered him.",
  "narration": "I asked my mother if she remembered him."},
 {"kind": "beat", "text": "She went pale.\nSaid she'd never noticed him before.",
  "narration": "She went pale. Said she'd never noticed him before."},
 {"kind": "clock", "caption": "She'd watched that tape\n*hundreds of times.* Never once saw him.", "hour": 9, "minute": 0,
  "narration": "She'd watched that tape hundreds of times. Never once saw him."},
 {"kind": "beat", "text": "I checked the next scene.\nHe was closer to the camera now.",
  "narration": "I checked the next scene. He was closer to the camera now."},
 {"kind": "beat", "text": "Scene after scene,\nhe kept getting closer.",
  "narration": "Scene after scene, he kept getting closer."},
 {"kind": "end", "text": "I haven't reached the end of the tape yet.\n*I'm afraid to see how close he gets.*",
  "question": "Would you finish watching it?",
  "narration": "I haven't reached the end of the tape yet. I'm afraid to see how close he gets."},
]

OUT = "images/suspense_daily/aug07_reel3.mp4"
WORK = "images/suspense_daily/aug07_reel3_work"
STATE = "suspense_daily_aug07_reel3_state.json"
LOCK = "suspense_daily_aug07_reel3.lock"

if __name__ == "__main__":
    build(BEATS, OUT, WORK, STATE, LOCK)
