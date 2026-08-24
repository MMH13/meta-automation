# -*- coding: utf-8 -*-
"""Top Movie Reviews — SAMPLE stock-footage reel, built to show the format
before committing to a backlog. Countdown/recommendation structure matching
the pacing of the reference reel, but with original one-line takes over
generic atmospheric B-roll (no posters, stills, or film clips).

Text is deliberately short per line: Bebas Neue is a condensed display face,
so 3-5 words per line reads best at reel size.

    python tmr_reel_sample.py
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_movie_reel_stock import build

_HERE = Path(__file__).parent

BEATS = [
 {"kind": "hook",
  "text": "5 thrillers\nthat *wreck*\nyour head.",
  "narration": "Five thrillers that wreck your head.",
  "query": "dark empty cinema theater seats"},

 {"kind": "beat", "kicker": "No. 5", "title": "Shutter Island",
  "text": "The second watch\nis a *different film.*",
  "narration": "Number five. Shutter Island. The second watch is a different film.",
  "query": "lighthouse coast waves dramatic sky"},

 {"kind": "beat", "kicker": "No. 4", "title": "Gone Girl",
  "text": "Nobody in it\nis *telling the truth.*",
  "narration": "Number four. Gone Girl. Nobody in it is telling the truth.",
  "query": "suburban street houses evening dusk"},

 {"kind": "beat", "kicker": "No. 3", "title": "Prisoners",
  "text": "Two hours of dread,\nand *no easy answer.*",
  "narration": "Number three. Prisoners. Two hours of dread, and no easy answer.",
  "query": "rain forest road misty moody daylight"},

 {"kind": "beat", "kicker": "No. 2", "title": "Oldboy",
  "text": "One corridor.\nOne take.\n*Unforgettable.*",
  "narration": "Number two. Oldboy. One corridor, one take, unforgettable.",
  "query": "long corridor hallway lights perspective"},

 {"kind": "beat", "kicker": "No. 1", "title": "Se7en",
  "text": "The last five minutes\n*never leave you.*",
  "narration": "Number one. Seven. The last five minutes never leave you.",
  "query": "rain city street neon reflections night"},

 {"kind": "end",
  "text": "Which one\n*broke you?*",
  "question": "Drop your pick below 👇",
  "narration": "Which one broke you?",
  "query": "cinema projector beam light dust dark"},
]

OUT = _HERE / "images" / "tmr_sample" / "tmr_sample_5_thrillers.mp4"
WORK = _HERE / "images" / "tmr_sample" / "tmr_sample_5_thrillers_work"
STATE = _HERE / "images" / "tmr_sample" / "tmr_sample_state.json"
LOCK = _HERE / "images" / "tmr_sample" / "tmr_sample.lock"

CAPTION = (
    "🎬 5 thrillers that wreck your head — in the best way.\n\n"
    "No. 5 Shutter Island · No. 4 Gone Girl · No. 3 Prisoners · "
    "No. 2 Oldboy · No. 1 Se7en\n\n"
    "👇 Which one broke you? Drop your pick below.\n\n"
    "🎬 Top Movie Reviews — one honest verdict a day."
)

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    build(BEATS, str(OUT), str(WORK), str(STATE), str(LOCK))
