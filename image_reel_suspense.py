# -*- coding: utf-8 -*-
"""Suspense Ahead — 9:16 reel frames (1080x1920).

Same visual DNA as image_suspense.py's suspense_card (dark radial gradient,
red glow, film grain, vignette, Oswald kicker, red *highlights*) but sized
for true Reels and safe-zoned clear of Facebook's reel UI (top ~250px header,
bottom ~430px caption/buttons/CTA).

  sr_hook(text, out)                 opening frame — biggest type
  sr_beat(text, out, kicker)         mid-reel line
  sr_end(text, out, question)        closing frame + engagement question
"""
from html import escape

from image_html import _render_html, _lines_html
from image_suspense import _GRAIN

RW, RH = 1080, 1920


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{RW}px; height:{RH}px; overflow:hidden; position:relative;
       background: radial-gradient(130% 90% at 50% 0%, #1c1f26 0%, #0d0f14 55%, #060708 100%);
       font-family:'Poppins',sans-serif; }}
  .grain {{ position:absolute; inset:0; opacity:.5; background-image:{_GRAIN}; }}
  .glow {{ position:absolute; width:900px; height:460px; left:90px; top:-200px;
       background:radial-gradient(closest-side, rgba(190,30,45,.24), transparent);
       filter:blur(10px); }}
  .vig {{ position:absolute; inset:0;
       background: radial-gradient(85% 75% at 50% 45%, transparent 55%, rgba(0,0,0,.78) 100%); }}
  .safe {{ position:absolute; left:86px; right:86px; top:250px; bottom:430px;
       display:flex; flex-direction:column; justify-content:center;
       align-items:center; text-align:center; gap:34px; }}
  .kicker {{ font-family:'Oswald',sans-serif; font-size:32px; font-weight:600;
       letter-spacing:7px; color:#e33b4e; text-transform:uppercase; }}
  .kicker::before, .kicker::after {{ content:"—"; color:#5a5f6b; margin:0 16px; }}
  .content {{ font-family:'Oswald',sans-serif; font-weight:500; color:#eceef2; }}
  .bar {{ width:120px; height:6px; background:#e33b4e; border-radius:3px; }}
  .footer {{ position:absolute; bottom:300px; width:100%; text-align:center;
       font-family:'Oswald',sans-serif; font-size:28px; font-weight:600;
       letter-spacing:5px; color:rgba(210,215,225,.55); }}
  {extra}
</style></head><body>
  <div class="glow"></div><div class="grain"></div><div class="vig"></div>
  {inner}
  <div class="footer">SUSPENSE AHEAD</div>
</body></html>"""


def sr_hook(text, out_path, size=64):
    extra = f".line {{ font-size:{size}px; line-height:1.36; }} .line .hl {{ color:#e33b4e; font-weight:700; }}"
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div><div class="bar"></div></div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def sr_beat(text, out_path, kicker="", size=58):
    extra = f".line {{ font-size:{size}px; line-height:1.4; }} .line .hl {{ color:#e33b4e; font-weight:700; }}"
    k = f'<div class="kicker">{escape(kicker)}</div>' if kicker else ""
    inner = f'<div class="safe">{k}<div class="content">{_lines_html(text)}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def sr_end(text, out_path, question=""):
    extra = (".line { font-size:60px; line-height:1.38; } .line .hl { color:#e33b4e; font-weight:700; }"
             " .q { font-size:36px; font-weight:500; color:#eceef2; line-height:1.5;"
             " border-top:2px solid #e33b4e77; padding-top:30px; margin-top:10px; }")
    q = f'<div class="q">{escape(question)}</div>' if question else ""
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))
