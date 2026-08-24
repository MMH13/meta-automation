# -*- coding: utf-8 -*-
"""Top Movie Reviews — 9:16 (1080x1920) transparent overlay frames for the
stock-footage reel pipeline (video_movie_reel_stock.py).

Same brand DNA as image_movie.py (midnight violet + amber gold, Bebas Neue
display type) but rendered with no background of its own, so these composite
over real Pexels B-roll. A bottom scrim guarantees the caption stays legible
over any footage.

CONTENT RULE (inherited from image_movie.py, unchanged): original text over
GENERIC/atmospheric footage only. Never posters, stills, or clips from actual
films — the whole point of this pipeline is to get a cinematic montage feel
without touching studio-copyrighted frames.

  mvo_hook(text, out)                opening overlay — biggest type
  mvo_beat(text, out, kicker="")     mid-reel line (kicker doubles as "#1", etc.)
  mvo_end(text, out, question="")    closing overlay + engagement question
"""
from html import escape

from image_html import _render_html, _lines_html

SW, SH = 1080, 1920

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Bebas+Neue&family=Inter:wght@400;500;600;700'
      '&display=swap" rel="stylesheet">')

AMBER = "#ffb703"
CREAM = "#f4f0ff"


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background: transparent !important; }}
  body {{ width:{SW}px; height:{SH}px; overflow:hidden; position:relative;
       font-family:'Inter',sans-serif; }}
  .scrim {{ position:absolute; left:0; right:0; bottom:0; height:60%;
       background: linear-gradient(180deg, transparent 0%, rgba(18,12,33,.58) 28%, rgba(18,12,33,.94) 100%); }}
  .safe {{ position:absolute; left:80px; right:80px; bottom:180px;
       display:flex; flex-direction:column; justify-content:flex-end;
       align-items:center; text-align:center; gap:26px; }}
  .kicker {{ font-family:'Bebas Neue',sans-serif; font-size:40px;
       letter-spacing:8px; color:{AMBER}; text-transform:uppercase;
       text-shadow:0 2px 10px rgba(0,0,0,.7); }}
  .title {{ font-family:'Bebas Neue',sans-serif; font-size:96px;
       line-height:1; letter-spacing:2px; color:{CREAM};
       text-shadow:0 3px 14px rgba(0,0,0,.8); }}
  .rule {{ width:150px; height:3px; background:{AMBER}; opacity:.85;
       border-radius:2px; }}
  .content {{ font-family:'Bebas Neue',sans-serif; color:{CREAM};
       letter-spacing:1px; text-shadow: 0 3px 14px rgba(0,0,0,.75); }}
  .content .hl {{ color:{AMBER}; }}
  /* the verdict line under a film title: Inter, sentence case, so it reads
     as commentary and is clearly separate from the Bebas title above it */
  .take {{ font-family:'Inter',sans-serif; font-weight:600; font-size:46px;
       line-height:1.32; letter-spacing:0; color:{CREAM};
       text-shadow:0 2px 12px rgba(0,0,0,.8); }}
  .take .hl {{ color:{AMBER}; }}
  .bar {{ width:110px; height:5px; border-radius:3px; background:{AMBER};
       box-shadow:0 0 18px rgba(255,183,3,.55); }}
  .footer {{ position:absolute; bottom:70px; width:100%; text-align:center;
       font-family:'Bebas Neue',sans-serif; font-size:30px;
       letter-spacing:7px; color:rgba(244,240,255,.72);
       text-shadow:0 2px 8px rgba(0,0,0,.7); }}
  {extra}
</style></head><body>
  <div class="scrim"></div>
  {inner}
  <div class="footer">TOP MOVIE REVIEWS</div>
</body></html>"""


def mvo_hook(text, out_path, size=104):
    extra = f".line {{ font-size:{size}px; line-height:1.06; }}"
    inner = (f'<div class="safe"><div class="content">{_lines_html(text)}</div>'
             f'<div class="bar"></div></div>')
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def mvo_beat(text, out_path, kicker="", title="", size=86):
    """title: optional film name, rendered as its own Bebas block with an
    amber rule under it. When set, `text` becomes the verdict line and is
    rendered in Inter so the two don't visually run together."""
    if title:
        extra = ""
        inner = (f'<div class="safe">'
                 f'{f"<div class=\'kicker\'>{escape(kicker)}</div>" if kicker else ""}'
                 f'<div class="title">{escape(title)}</div>'
                 f'<div class="rule"></div>'
                 f'<div class="take">{_lines_html(text)}</div>'
                 f'</div>')
    else:
        extra = f".line {{ font-size:{size}px; line-height:1.1; }}"
        k = f'<div class="kicker">{escape(kicker)}</div>' if kicker else ""
        inner = f'<div class="safe">{k}<div class="content">{_lines_html(text)}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)


def mvo_end(text, out_path, question=""):
    extra = (".line { font-size:92px; line-height:1.08; }"
             " .q { font-family:'Inter',sans-serif; font-size:38px; font-weight:600;"
             f" color:{CREAM}; line-height:1.45; border-top:3px solid {AMBER}88;"
             " padding-top:28px; margin-top:8px; letter-spacing:0;"
             " text-shadow:0 2px 10px rgba(0,0,0,.7); }")
    q = f'<div class="q">{escape(question)}</div>' if question else ""
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(SW, SH), transparent=True)
