# -*- coding: utf-8 -*-
"""Daily Wisdom — 9:16 (1080x1920) transparent overlay frames, composited
(ffmpeg overlay) on top of real Pexels B-roll — rain, candlelight, ruins,
night streets — via video_wisdom_stock.py, mirroring the health/suspense
stock-footage pipelines.

Brand: near-black scrim, warm ivory type, muted bronze accent — cinematic and
quiet rather than bright/energetic, distinct from every other page's palette
(TMR = amber/violet, Health = blue/green, Style Spotlight = cream/gold).
Serif display face for the idea itself (it should read like something worth
remembering, not a listicle), sans for the small supporting text.

  dw_hook(text, out)                 opening line — biggest type
  dw_beat(text, out, kicker="")      mid-reel insight
  dw_end(text, out, cta="")          closing line + optional CTA/question
"""
from html import escape

from image_html import _render_html, _lines_html

SW, SH = 1080, 1920

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600'
      '&display=swap" rel="stylesheet">')

IVORY = "#f3ede2"
BRONZE = "#c9a26a"


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background: transparent !important; }}
  body {{ width:{SW}px; height:{SH}px; overflow:hidden; position:relative;
       font-family:'Inter',sans-serif; }}
  .scrim {{ position:absolute; left:0; right:0; bottom:0; height:56%;
       background: linear-gradient(180deg, transparent 0%, rgba(8,8,7,.58) 32%, rgba(5,5,4,.92) 100%); }}
  .safe {{ position:absolute; left:84px; right:84px; bottom:180px;
       display:flex; flex-direction:column; justify-content:flex-end;
       align-items:center; text-align:center; gap:26px; }}
  .kicker {{ font-family:'Inter',sans-serif; font-size:24px; font-weight:600;
       letter-spacing:5px; color:{BRONZE}; text-transform:uppercase; }}
  .content {{ font-family:'Playfair Display',serif; font-weight:600; color:{IVORY};
       text-shadow: 0 2px 14px rgba(0,0,0,.7); }}
  .content .hl {{ color:{BRONZE}; font-style:italic; }}
  .bar {{ width:88px; height:3px; border-radius:2px; background:{BRONZE}; opacity:.85; }}
  .cta {{ font-family:'Inter',sans-serif; font-size:32px; font-weight:500;
       color:rgba(243,237,226,.88); line-height:1.4;
       border-top:1px solid rgba(201,162,106,.5); padding-top:26px; margin-top:6px; }}
  .footer {{ position:absolute; bottom:68px; width:100%; text-align:center;
       font-family:'Inter',sans-serif; font-size:22px; font-weight:600;
       letter-spacing:5px; color:rgba(243,237,226,.6); }}
  {extra}
</style></head><body>
  <div class="scrim"></div>
  {inner}
  <div class="footer">DAILY WISDOM</div>
</body></html>"""


def dw_hook(text, out_path, size=74):
    extra = f".line {{ font-size:{size}px; line-height:1.28; letter-spacing:-.3px; }}"
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div><div class="bar"></div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def dw_beat(text, out_path, kicker="", size=60):
    extra = f".line {{ font-size:{size}px; line-height:1.32; letter-spacing:-.2px; }}"
    k = f'<div class="kicker">{escape(kicker)}</div>' if kicker else ""
    inner = f'<div class="safe">{k}<div class="content">{_lines_html(text)}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def dw_end(text, out_path, cta=""):
    extra = ".line { font-size:64px; line-height:1.3; letter-spacing:-.3px; }"
    c = f'<div class="cta">{escape(cta)}</div>' if cta else ""
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div>{c}</div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)
