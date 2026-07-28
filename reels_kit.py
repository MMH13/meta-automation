# -*- coding: utf-8 -*-
"""Top Movie Reviews — reel production kit. Renders every burned-in text frame
for the 3 launch reels at 1080x1920, ready to drop into CapCut.

Output: images/reels/r{n}_{seq}_{name}.png  (numbered = assembly order)

You supply only the B-roll behind them (AI stills, prompts in REELS_KIT.md).
No studio assets anywhere in this pipeline.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

from aug_common import mkdir, render
from image_reel import reel_hook, reel_beat, reel_title, reel_end

OUT = mkdir("images/reels")

# (seq, name, fn, args)  — seq doubles as CapCut assembly order
REEL1 = [  # "The Jaws Accident" — 32s
    (1, "hook", reel_hook,
     ("THE SCARIEST SHARK\nIN MOVIE HISTORY\n*BARELY APPEARS*",), {"size": 92}),
    (2, "beat", reel_beat,
     ("SPIELBERG BUILT A\n*MECHANICAL SHARK*",), {"kicker": "1975", "size": 76}),
    (3, "beat", reel_beat,
     ("IN SALT WATER\nIT *KEPT BREAKING*",), {"size": 78}),
    (4, "beat", reel_beat,
     ("SO HE STOPPED\nSHOWING IT",), {"size": 82}),
    (5, "beat", reel_beat,
     ("A FIN.\nA BARREL.\n*NOTHING AT ALL.*",), {"size": 84}),
    (6, "end", reel_end,
     ("FIFTY YEARS LATER\nHORROR IS STILL COPYING\nA *BROKEN PROP*",),
     {"question": "What's the scariest thing you\n*never actually saw* on screen?"}),
]

REEL2 = [  # "1999 Broke Cinema" — 40s
    (1, "hook", reel_hook,
     ("SIX FILMS CAME OUT\nIN *ONE YEAR*\nAND ALL SIX\nCHANGED MOVIES",), {"size": 88}),
    (2, "title", reel_title, ("1999", "THE MATRIX", "rewrote *action* forever"), {}),
    (3, "title", reel_title, ("1999", "FIGHT CLUB", "rewired a *generation*"), {}),
    (4, "title", reel_title, ("1999", "THE SIXTH SENSE", "made the *twist* a genre"), {}),
    (5, "title", reel_title, ("1999", "BEING JOHN MALKOVICH", "made *weird* mainstream"), {}),
    (6, "title", reel_title, ("1999", "MAGNOLIA", "went completely *for broke*"), {}),
    (7, "title", reel_title, ("1999", "THE BLAIR WITCH PROJECT", "invented *found footage*"), {}),
    (8, "end", reel_end,
     ("ONE YEAR.\nWE NEVER GOT\n*ANOTHER LIKE IT.*",),
     {"question": "Which *1999* film holds up best?"}),
]

REEL3 = [  # "Say the Line Wrong" — 25s
    (1, "hook", reel_hook,
     ("YOU'VE BEEN QUOTING\nTHESE MOVIES\n*WRONG*\nYOUR WHOLE LIFE",), {"size": 88}),
    (2, "beat", reel_beat,
     ("\"LUKE, I AM\nYOUR FATHER\"\n\nHE NEVER SAYS\n*LUKE*",),
     {"kicker": "MISQUOTE 01", "size": 66}),
    (3, "beat", reel_beat,
     ("\"PLAY IT AGAIN,\nSAM\"\n\n*NOBODY* SAYS THIS\nIN CASABLANCA",),
     {"kicker": "MISQUOTE 02", "size": 66}),
    (4, "beat", reel_beat,
     ("\"ELEMENTARY,\nMY DEAR WATSON\"\n\n*NOT IN A SINGLE*\nORIGINAL STORY",),
     {"kicker": "MISQUOTE 03", "size": 62}),
    (5, "end", reel_end,
     ("THREE OF THE MOST\nFAMOUS LINES EVER.\n*NONE OF THEM REAL.*",),
     {"question": "Which one did *you* believe?"}),
]

REELS = {1: REEL1, 2: REEL2, 3: REEL3}


def build():
    total = 0
    for rn, frames in REELS.items():
        print(f"=== REEL {rn} ({len(frames)} frames) ===")
        for seq, name, fn, args, kw in [(s, n, f, a, k) for s, n, f, a, k in frames]:
            out = f"{OUT}/r{rn}_{seq:02d}_{name}.png"
            render(fn, *args, out, **kw)
            total += 1
            print(f"  {out}")
    print(f"DONE — {total} reel frames at 1080x1920")


if __name__ == "__main__":
    build()
