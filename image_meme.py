# -*- coding: utf-8 -*-
"""রেডিও দেশাল — MEME templates. Built to the meme-system image rules:
simple · clean · mobile-first · HIGH CONTRAST · MINIMAL TEXT · never overcrowded.

Deliberately lighter chrome than image_deshal.py's cards (no ticker, no long
footer, no intro paragraph) — the joke should be readable in under 2 seconds
at thumbnail size.

  meme_statement(text, ...)      one big punchline
  meme_nobody(setup, punch, ...) "Nobody: / Me:" two-block format
  meme_split(top, bottom, ...)   two-panel setup→punchline
"""

from html import escape
import re

from image_html import _render_html, W, H

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Anek+Bangla:wght@600;700;800&family=Hind+Siliguri:wght@600;700'
      '&display=swap" rel="stylesheet">')

# high-contrast palettes (bg, text, accent)
THEMES = {
    "yellow": ("#ffd60a", "#0b0b0b", "#e63946"),
    "black":  ("#0b0b0b", "#ffffff", "#ffd60a"),
    "red":    ("#e63946", "#ffffff", "#ffd60a"),
    "blue":   ("#0077b6", "#ffffff", "#ffd60a"),
    "white":  ("#f5f5f5", "#0b0b0b", "#e63946"),
    "sky":    ("#6cc4e8", "#0b1e2d", "#ffffff"),   # Argentina-ish
}

_TAG = "রেডিও দেশাল"


def _lines(text, accent):
    out = []
    for ln in text.strip().split("\n"):
        h = re.sub(r"\*(.+?)\*", lambda m: f'<span style="color:{accent}">{m.group(1)}</span>',
                   escape(ln.strip()))
        out.append(f"<div>{h}</div>")
    return "\n".join(out)


def _base(bg, fg, inner, size=88):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{bg}; color:{fg};
       font-family:'Anek Bangla','Hind Siliguri',sans-serif; }}
  .wrap {{ position:absolute; inset:90px 76px 130px; display:flex;
       flex-direction:column; justify-content:center; align-items:center;
       text-align:center; }}
  .big {{ font-weight:800; font-size:{size}px; line-height:1.34; }}
  .tag {{ position:absolute; bottom:52px; left:0; right:0; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-size:30px; font-weight:700;
       opacity:.45; letter-spacing:1px; }}
</style></head><body>
  {inner}
  <div class="tag">📻 {_TAG}</div>
</body></html>"""


def meme_statement(text, out_path, theme="yellow", emoji="", size=88):
    bg, fg, ac = THEMES[theme]
    hero = f'<div style="font-size:120px;margin-bottom:26px">{emoji}</div>' if emoji else ""
    inner = f'<div class="wrap">{hero}<div class="big">{_lines(text, ac)}</div></div>'
    return _render_html(_base(bg, fg, inner, size), out_path)


def meme_nobody(setup, punch, out_path, theme="black", emoji=""):
    """setup shown small/muted (e.g. 'কেউ কিছু বলেনি:'), punch shown huge."""
    bg, fg, ac = THEMES[theme]
    hero = f'<div style="font-size:96px;margin-top:22px">{emoji}</div>' if emoji else ""
    inner = f"""<div class="wrap">
      <div style="font-size:52px;font-weight:700;opacity:.72;margin-bottom:38px;
                  line-height:1.3">{_lines(setup, ac)}</div>
      <div style="width:120px;height:5px;background:{ac};margin-bottom:38px"></div>
      <div class="big">{_lines(punch, ac)}</div>{hero}</div>"""
    return _render_html(_base(bg, fg, inner), out_path)


def meme_split(top_text, bottom_text, out_path, top_theme="sky",
               bottom_theme="black", top_emoji="", bottom_emoji=""):
    tbg, tfg, tac = THEMES[top_theme]
    bbg, bfg, bac = THEMES[bottom_theme]
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       font-family:'Anek Bangla','Hind Siliguri',sans-serif; }}
  .half {{ position:absolute; left:0; right:0; height:50%; display:flex;
       flex-direction:column; align-items:center; justify-content:center;
       text-align:center; padding:60px 74px; gap:18px; }}
  .t {{ top:0; background:{tbg}; color:{tfg}; }}
  .b {{ bottom:0; background:{bbg}; color:{bfg}; }}
  .tx {{ font-weight:800; font-size:66px; line-height:1.3; }}
  .em {{ font-size:96px; }}
  .tag {{ position:absolute; bottom:26px; left:0; right:0; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-size:28px; font-weight:700;
       color:{bfg}; opacity:.45; }}
</style></head><body>
  <div class="half t">{f'<div class="em">{top_emoji}</div>' if top_emoji else ''}
    <div class="tx">{_lines(top_text, tac)}</div></div>
  <div class="half b">{f'<div class="em">{bottom_emoji}</div>' if bottom_emoji else ''}
    <div class="tx">{_lines(bottom_text, bac)}</div></div>
  <div class="tag">📻 {_TAG}</div>
</body></html>"""
    return _render_html(html, out_path)
