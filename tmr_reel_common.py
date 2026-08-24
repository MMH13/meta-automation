# -*- coding: utf-8 -*-
"""Shared builder for Top Movie Reviews poster reels.

Each reel is the same 7-beat countdown shape (hook + 5 poster cards + CTA), so
content files declare it compactly and this expands it into the beats list the
pipeline wants, plus the FB caption.

  countdown(slug, eyebrow, headline, headline_vo, films) -> (slug, beats, caption)

films: list of 5 tuples, in COUNTDOWN order (No. 5 first, No. 1 last):
  (title, year, take_text, take_vo)

take_text uses \n for line breaks and *stars* for amber highlight; take_vo is
the spoken version (no markup, no line breaks).
"""
import re

ORDINALS = ["No. 5", "No. 4", "No. 3", "No. 2", "No. 1"]
SPOKEN = ["Number five", "Number four", "Number three", "Number two", "Number one"]

END_TEXT = "Which one\n*broke you?*"
END_Q = "Drop your pick below 👇"
END_VO = "Which one broke you?"
SIGNOFF = "🎬 Top Movie Reviews — one honest verdict a day."


def _plain(s):
    """Strip markup/line breaks for use in the caption."""
    return re.sub(r"\s+", " ", s.replace("*", "")).strip()


def countdown(slug, eyebrow, headline, headline_vo, films,
              end_text=END_TEXT, end_q=END_Q, end_vo=END_VO, hashtags=""):
    if len(films) != 5:
        raise ValueError(f"{slug}: expected 5 films, got {len(films)}")

    beats = [{"kind": "hook", "eyebrow": eyebrow, "text": headline,
              "narration": headline_vo}]

    for i, (title, year, take_text, take_vo) in enumerate(films):
        beats.append({
            "kind": "poster", "kicker": ORDINALS[i],
            "title": title, "year": year,
            "text": take_text,
            "narration": f"{SPOKEN[i]}. {title}. {take_vo}",
        })

    beats.append({"kind": "end", "text": end_text, "question": end_q,
                  "narration": end_vo})

    listing = " · ".join(f"{ORDINALS[i]} {f[0]}" for i, f in enumerate(films))
    caption = (f"🎬 {_plain(headline)}\n\n{listing}\n\n"
               f"{_plain(end_q)}\n\n{SIGNOFF}")
    if hashtags:
        caption += f"\n\n{hashtags}"

    return (slug, beats, caption)
