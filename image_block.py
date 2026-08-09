# -*- coding: utf-8 -*-
"""Mamun Hossain — solid color-block posts (modeled on top-performing BD AI-creator
format: bold solid background, big centered Bengali+English code-switched text).

The reference page's highest-engagement posts are all this format. Deliberately
minimal chrome — the hook IS the whole image. Code-switching (mixing English words
inline) is the native voice; write text that way.

  block_post(text, theme, footer)   *stars* = accent-colored words
"""

from html import escape
import re

from image_html import _render_html, W, H

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Anek+Bangla:wght@600;700;800&family=Hind+Siliguri:wght@600;700;800'
      '&display=swap" rel="stylesheet">')

THEMES = {   # (background, text, accent-for-*stars*)
    "crimson": ("#e8112d", "#ffffff", "#ffd60a"),
    "black":   ("#0a0a0a", "#ffffff", "#ffd60a"),
    "charcoal":("linear-gradient(160deg,#2c2c2e 0%,#111113 100%)", "#ffffff", "#56d6ff"),
    "navy":    ("linear-gradient(160deg,#12183a 0%,#0a0f26 100%)", "#ffffff", "#56d6ff"),
    "green":   ("#0b7a3b", "#ffffff", "#ffe14d"),
}


def block_post(text, out_path, theme="crimson", footer="🚀 Mamun Hossain",
               size=78):
    bg, fg, ac = THEMES[theme]
    lines = []
    for ln in text.strip().split("\n"):
        h = re.sub(r"\*(.+?)\*",
                   lambda m: f'<span style="color:{ac}">{m.group(1)}</span>',
                   escape(ln.strip()))
        lines.append(f"<div>{h}</div>")
    body = "\n".join(lines)
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{bg}; font-family:'Anek Bangla','Hind Siliguri',sans-serif; }}
  .wrap {{ position:absolute; inset:96px 80px 128px; display:flex;
       flex-direction:column; justify-content:center; align-items:center;
       text-align:center; }}
  .txt {{ color:{fg}; font-weight:800; font-size:{size}px; line-height:1.42;
       letter-spacing:.3px; }}
  .foot {{ position:absolute; bottom:52px; left:0; right:0; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:700; font-size:30px;
       color:{fg}; opacity:.55; }}
</style></head><body>
  <div class="wrap"><div class="txt">{body}</div></div>
  <div class="foot">{escape(footer)}</div>
</body></html>"""
    return _render_html(html, out_path)
