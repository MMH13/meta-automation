# -*- coding: utf-8 -*-
"""Top Movie Reviews — 9:16 (1080x1920) FULL-frame reel cards built around the
official TMDB poster (blurred poster backdrop + sharp poster + brand text).

Unlike image_reel_movie_overlay.py (transparent overlays composited onto stock
B-roll), these are complete frames: the poster IS the visual. ffmpeg then only
has to Ken-Burns them, so all layout/design happens here in CSS.

EDITORIAL USE: posters come from TMDB via tmdb.py, are shown inside our own
review layout with a visible credit line, and are never reposted standalone —
the same convention already used by the static cards in tmr_static_aug.py.

  mvp_hook(text, out)                                 brand-gradient opener
  mvp_poster(title, year, text, out, poster, kicker)  poster card
  mvp_end(text, out, question)                        brand-gradient closer
"""
from html import escape
from pathlib import Path

from image_html import _render_html, _lines_html

SW, SH = 1080, 1920

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Bebas+Neue&family=Inter:wght@400;500;600;700'
      '&display=swap" rel="stylesheet">')

AMBER = "#ffb703"
CREAM = "#f4f0ff"
BG1 = "#1e1633"
BG2 = "#120c21"

CREDIT = "Poster © respective studio · used for review"


def _uri(p):
    """Local path -> file:/// URI the headless browser can load."""
    return Path(p).resolve().as_uri()


_BASE_CSS = f"""
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{SW}px; height:{SH}px; overflow:hidden; position:relative;
       font-family:'Inter',sans-serif; color:{CREAM};
       background:linear-gradient(165deg,{BG1} 0%,{BG2} 100%); }}
  .kicker {{ font-family:'Bebas Neue',sans-serif; font-size:40px;
       letter-spacing:8px; color:{AMBER}; text-transform:uppercase;
       text-shadow:0 2px 10px rgba(0,0,0,.75); }}
  .title {{ font-family:'Bebas Neue',sans-serif; font-size:92px; line-height:1;
       letter-spacing:2px; color:{CREAM}; text-shadow:0 3px 16px rgba(0,0,0,.85); }}
  .year {{ font-family:'Inter',sans-serif; font-size:30px; font-weight:500;
       color:{AMBER}; letter-spacing:3px; }}
  .rule {{ width:150px; height:3px; background:{AMBER}; opacity:.85; border-radius:2px; }}
  .take {{ font-family:'Inter',sans-serif; font-weight:600; font-size:44px;
       line-height:1.32; color:{CREAM}; text-shadow:0 2px 12px rgba(0,0,0,.85); }}
  .take .hl {{ color:{AMBER}; }}
  .footer {{ position:absolute; bottom:64px; width:100%; text-align:center;
       font-family:'Bebas Neue',sans-serif; font-size:30px; letter-spacing:7px;
       color:rgba(244,240,255,.72); text-shadow:0 2px 8px rgba(0,0,0,.7); }}
  .credit {{ position:absolute; bottom:34px; width:100%; text-align:center;
       font-size:17px; font-weight:400; color:rgba(244,240,255,.42);
       letter-spacing:.3px; }}
"""


def _shell(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>{_BASE_CSS}{extra}</style></head><body>{inner}</body></html>"""


def mvp_poster(title, year, text, out_path, poster_path, kicker=""):
    """Blurred poster fills the frame; the sharp poster sits above the text."""
    uri = _uri(poster_path)
    extra = f"""
  .bg {{ position:absolute; inset:-60px; background:url('{uri}') center/cover no-repeat;
       filter:blur(46px) brightness(.34) saturate(1.1); }}
  .vig {{ position:absolute; inset:0;
       background:radial-gradient(120% 80% at 50% 22%, transparent 30%, rgba(18,12,33,.72) 100%); }}
  .poster {{ position:absolute; top:132px; left:50%; transform:translateX(-50%);
       width:720px; height:1080px; object-fit:cover; border-radius:16px;
       box-shadow:0 34px 90px rgba(0,0,0,.8), 0 0 0 2px rgba(255,183,3,.28); }}
  .panel {{ position:absolute; left:70px; right:70px; top:1290px;
       display:flex; flex-direction:column; align-items:center;
       text-align:center; gap:18px; }}
"""
    y = f'<div class="year">{escape(str(year))}</div>' if year else ""
    k = f'<div class="kicker">{escape(kicker)}</div>' if kicker else ""
    inner = (f'<div class="bg"></div><div class="vig"></div>'
             f'<img class="poster" src="{uri}">'
             f'<div class="panel">{k}'
             f'<div class="title">{escape(title)}</div>{y}'
             f'<div class="rule"></div>'
             f'<div class="take">{_lines_html(text)}</div></div>'
             f'<div class="footer">TOP MOVIE REVIEWS</div>'
             f'<div class="credit">{escape(CREDIT)}</div>')
    return _render_html(_shell(inner, extra), out_path, size=(SW, SH))


def _collage(posters):
    """Full-bleed blurred wash built from the reel's own posters — gives the
    hook/end cards the same colour richness as the poster cards, instead of a
    flat brand gradient."""
    if not posters:
        return "", ""
    cells = list(posters)
    while len(cells) < 6:                       # fill the 3x2 grid
        cells.append(cells[len(cells) % len(posters)])
    imgs = "".join(f'<img src="{_uri(p)}">' for p in cells[:6])
    css = """
  .collage { position:absolute; inset:-90px; display:grid;
       grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(2,1fr);
       filter:blur(42px) brightness(.34) saturate(1.18); }
  .collage img { width:100%; height:100%; object-fit:cover; }
  .vig { position:absolute; inset:0;
       background:radial-gradient(115% 75% at 50% 45%, transparent 28%, rgba(18,12,33,.78) 100%); }
"""
    return f'<div class="collage">{imgs}</div><div class="vig"></div>', css


def mvp_hook(text, out_path, posters=None, eyebrow="", size=104):
    """Opening card: blurred poster collage + a fanned strip of the actual
    posters (teases what's coming) + the headline."""
    bg, bg_css = _collage(posters)
    strip = ""
    if posters:
        strip = ('<div class="strip">'
                 + "".join(f'<img src="{_uri(p)}">' for p in posters[:5])
                 + '</div>')
    extra = bg_css + f"""
  .strip {{ position:absolute; top:560px; left:0; right:0;
       display:flex; justify-content:center; align-items:center; }}
  .strip img {{ width:200px; height:300px; object-fit:cover; border-radius:11px;
       margin:0 -4px; box-shadow:0 20px 48px rgba(0,0,0,.75),
       0 0 0 2px rgba(255,183,3,.24); }}
  .strip img:nth-child(1) {{ transform:rotate(-9deg) translateY(18px); }}
  .strip img:nth-child(2) {{ transform:rotate(-4.5deg) translateY(5px); }}
  .strip img:nth-child(3) {{ transform:scale(1.05); z-index:3; }}
  .strip img:nth-child(4) {{ transform:rotate(4.5deg) translateY(5px); }}
  .strip img:nth-child(5) {{ transform:rotate(9deg) translateY(18px); }}
  .hookwrap {{ position:absolute; left:70px; right:70px; top:1120px;
       display:flex; flex-direction:column; align-items:center;
       text-align:center; gap:22px; }}
  .title .hl {{ color:{AMBER}; }}
"""
    eb = f'<div class="kicker">{escape(eyebrow)}</div>' if eyebrow else ""
    inner = (f'{bg}{strip}<div class="hookwrap">{eb}'
             f'<div class="title" style="font-size:{size}px;line-height:1.06">'
             f'{_lines_html(text)}</div><div class="rule"></div></div>'
             f'<div class="footer">TOP MOVIE REVIEWS</div>')
    return _render_html(_shell(inner, extra), out_path, size=(SW, SH))


def mvp_end(text, out_path, question="", posters=None):
    """Closing card: same blurred poster collage, text centred on the CTA."""
    bg, bg_css = _collage(posters)
    extra = bg_css + f"""
  .endwrap {{ position:absolute; left:80px; right:80px; top:0; bottom:0;
       display:flex; flex-direction:column; justify-content:center;
       align-items:center; text-align:center; gap:30px; }}
  .title .hl {{ color:{AMBER}; }}
"""
    q = (f'<div class="take" style="border-top:3px solid {AMBER}88;padding-top:28px">'
         f'{escape(question)}</div>') if question else ""
    inner = (f'{bg}<div class="endwrap">'
             f'<div class="title" style="font-size:98px;line-height:1.08">'
             f'{_lines_html(text)}</div>{q}</div>'
             f'<div class="footer">TOP MOVIE REVIEWS</div>')
    return _render_html(_shell(inner, extra), out_path, size=(SW, SH))
