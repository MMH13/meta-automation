# -*- coding: utf-8 -*-
"""Suspense Ahead — 1:1 (1080x1080) long-form pipeline overlay frames.

These are transparent PNGs meant to be composited (ffmpeg overlay) on top of
real stock-footage clips, not standalone posts. Same brand DNA as
image_reel_suspense.py (dark/red, Oswald kicker, red *highlights*) but with
no opaque background of their own - a bottom scrim guarantees caption
legibility over any footage.

  sq_hook(text, out)                 opening overlay - biggest type
  sq_beat(text, out, kicker="")       mid-video line
  sq_end(text, out, question="")      closing overlay + engagement question
"""
from html import escape

from image_html import _render_html, _lines_html
from image_suspense import _GRAIN

SW, SH = 1080, 1080


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background: transparent !important; }}
  body {{ width:{SW}px; height:{SH}px; overflow:hidden; position:relative;
       font-family:'Poppins',sans-serif; }}
  .grain {{ position:absolute; inset:0; opacity:.32; background-image:{_GRAIN}; }}
  .scrim {{ position:absolute; left:0; right:0; bottom:0; height:62%;
       background: linear-gradient(180deg, transparent 0%, rgba(6,7,8,.55) 30%, rgba(6,7,8,.92) 100%); }}
  .safe {{ position:absolute; left:70px; right:70px; bottom:110px;
       display:flex; flex-direction:column; justify-content:flex-end;
       align-items:center; text-align:center; gap:26px; }}
  .kicker {{ font-family:'Oswald',sans-serif; font-size:28px; font-weight:600;
       letter-spacing:6px; color:#e33b4e; text-transform:uppercase; }}
  .kicker::before, .kicker::after {{ content:"—"; color:#8a8f99; margin:0 14px; }}
  .content {{ font-family:'Oswald',sans-serif; font-weight:500; color:#eceef2;
       text-shadow: 0 2px 10px rgba(0,0,0,.6); }}
  .bar {{ width:100px; height:5px; background:#e33b4e; border-radius:3px; }}
  .footer {{ position:absolute; bottom:44px; width:100%; text-align:center;
       font-family:'Oswald',sans-serif; font-size:24px; font-weight:600;
       letter-spacing:4px; color:rgba(220,225,232,.6); }}
  {extra}
</style></head><body>
  <div class="grain"></div><div class="scrim"></div>
  {inner}
  <div class="footer">SUSPENSE AHEAD</div>
</body></html>"""


def sq_hook(text, out_path, size=54):
    extra = f".line {{ font-size:{size}px; line-height:1.32; }} .line .hl {{ color:#e33b4e; font-weight:700; }}"
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div><div class="bar"></div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def sq_beat(text, out_path, kicker="", size=48):
    extra = f".line {{ font-size:{size}px; line-height:1.36; }} .line .hl {{ color:#e33b4e; font-weight:700; }}"
    k = f'<div class="kicker">{escape(kicker)}</div>' if kicker else ""
    inner = f'<div class="safe">{k}<div class="content">{_lines_html(text)}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def sq_end(text, out_path, question=""):
    extra = (".line { font-size:50px; line-height:1.34; } .line .hl { color:#e33b4e; font-weight:700; }"
             " .q { font-size:30px; font-weight:500; color:#eceef2; line-height:1.5;"
             " border-top:2px solid #e33b4e77; padding-top:22px; margin-top:6px;"
             " text-shadow:0 2px 8px rgba(0,0,0,.6); }")
    q = f'<div class="q">{escape(question)}</div>' if question else ""
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)
