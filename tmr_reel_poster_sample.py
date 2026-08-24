# -*- coding: utf-8 -*-
"""Top Movie Reviews — SAMPLE poster-montage reel (same 5 films as the
stock-footage sample, so the two formats can be compared directly).

Posters come from TMDB via tmdb.py, shown inside our own review layout with a
credit line — same editorial-use convention as the static cards.

    python tmr_reel_poster_sample.py
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_movie_reel_poster import build

_HERE = Path(__file__).parent

BEATS = [
 {"kind": "hook", "eyebrow": "Thriller countdown",
  "text": "5 films\nyou'll never\n*unsee.*",
  "narration": "Five thrillers you will never unsee. Number one still gets people."},

 {"kind": "poster", "kicker": "No. 5", "title": "Shutter Island", "year": 2010,
  "text": "The second watch\nis a *different film.*",
  "narration": "Number five. Shutter Island. The second watch is a different film."},

 {"kind": "poster", "kicker": "No. 4", "title": "Gone Girl", "year": 2014,
  "text": "Nobody in it\nis *telling the truth.*",
  "narration": "Number four. Gone Girl. Nobody in it is telling the truth."},

 {"kind": "poster", "kicker": "No. 3", "title": "Prisoners", "year": 2013,
  "text": "Two hours of dread,\nand *no easy answer.*",
  "narration": "Number three. Prisoners. Two hours of dread, and no easy answer."},

 {"kind": "poster", "kicker": "No. 2", "title": "Oldboy", "year": 2003,
  "text": "One corridor.\nOne take.\n*Unforgettable.*",
  "narration": "Number two. Oldboy. One corridor, one take, unforgettable."},

 {"kind": "poster", "kicker": "No. 1", "title": "Se7en", "year": 1995,
  "text": "The last five minutes\n*never leave you.*",
  "narration": "Number one. Seven. The last five minutes never leave you."},

 {"kind": "end",
  "text": "Which one\n*broke you?*",
  "question": "Drop your pick below 👇",
  "narration": "Which one broke you?"},
]

OUT = _HERE / "images" / "tmr_poster_sample" / "tmr_poster_5_thrillers.mp4"
WORK = _HERE / "images" / "tmr_poster_sample" / "work"
STATE = _HERE / "images" / "tmr_poster_sample" / "state.json"
LOCK = _HERE / "images" / "tmr_poster_sample" / "sample.lock"

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    build(BEATS, str(OUT), str(WORK), str(STATE), str(LOCK))
