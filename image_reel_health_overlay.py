# -*- coding: utf-8 -*-
"""Health Daily — 9:16 (1080x1920) transparent overlay frames, meant to be
composited (ffmpeg overlay) on top of real Pexels stock-footage clips instead
of the solid-card look in image_reel_health.py. Same brand DNA (Poppins/Inter,
blue+green two-tone) but as white/light type over a bottom scrim so it reads
over any footage.

  hdo_hook(text, out)                opening overlay — biggest type
  hdo_beat(text, out, kicker="")     mid-reel overlay
  hdo_end(text, out, question="")    closing overlay + engagement question
"""
from html import escape

from image_html import _render_html, _lines_html

SW, SH = 1080, 1920

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600;700'
      '&display=swap" rel="stylesheet">')

BLUE = "#6dd0ff"
GREEN = "#4be3a0"


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background: transparent !important; }}
  body {{ width:{SW}px; height:{SH}px; overflow:hidden; position:relative;
       font-family:'Inter',sans-serif; }}
  /* Scrim now darkens the middle band (roughly the 250-1490px safe zone,
     where the text lives after the fix below) instead of only the bottom -
     text moved, so the contrast band has to move with it. Softer at the
     very top/bottom since text no longer sits there. */
  .scrim {{ position:absolute; left:0; right:0; top:0; bottom:0;
       background: linear-gradient(180deg,
         rgba(7,15,20,.25) 0%, rgba(7,15,20,.55) 18%, rgba(7,15,20,.55) 75%,
         rgba(7,15,20,.3) 100%); }}
  /* Was bottom:180px + justify-content:flex-end - text grew upward from
     near the bottom edge, so the LAST line sat right where FB/IG's own
     reel UI (caption, action buttons, progress bar) overlaps the frame.
     Centered in the same 250px-top/430px-bottom safe zone the non-stock
     renderer already uses correctly, so every line clears the real UI. */
  .safe {{ position:absolute; left:80px; right:80px; top:250px; bottom:430px;
       display:flex; flex-direction:column; justify-content:center;
       align-items:center; text-align:center; gap:28px; }}
  .kicker {{ font-family:'Poppins',sans-serif; font-size:26px; font-weight:700;
       letter-spacing:5px; color:{GREEN}; text-transform:uppercase; }}
  .content {{ font-family:'Poppins',sans-serif; font-weight:700; color:#f4fbff;
       text-shadow: 0 2px 12px rgba(0,0,0,.65); }}
  .content .hl {{ color:{BLUE}; }}
  .bar {{ width:96px; height:5px; border-radius:3px;
       background:linear-gradient(90deg,{BLUE},{GREEN}); }}
  .footer {{ position:absolute; bottom:70px; width:100%; text-align:center;
       font-family:'Poppins',sans-serif; font-size:24px; font-weight:700;
       letter-spacing:5px; color:rgba(244,251,255,.75); }}
  {extra}
</style></head><body>
  <div class="scrim"></div>
  {inner}
  <div class="footer">HEALTH DAILY</div>
</body></html>"""


def hdo_hook(text, out_path, size=76):
    extra = f".line {{ font-size:{size}px; line-height:1.22; letter-spacing:-.5px; }}"
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div><div class="bar"></div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def hdo_beat(text, out_path, kicker="", size=62):
    extra = f".line {{ font-size:{size}px; line-height:1.28; letter-spacing:-.3px; }}"
    k = f'<div class="kicker">{escape(kicker)}</div>' if kicker else ""
    inner = f'<div class="safe">{k}<div class="content">{_lines_html(text)}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def hdo_end(text, out_path, question=""):
    extra = (".line { font-size:66px; line-height:1.24; letter-spacing:-.5px; }"
             " .q { font-size:36px; font-weight:600; color:#f4fbff; line-height:1.45;"
             f" border-top:3px solid {GREEN}77; padding-top:28px; margin-top:8px;"
             " text-shadow:0 2px 10px rgba(0,0,0,.6); }")
    q = f'<div class="q">{escape(question)}</div>' if question else ""
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)
