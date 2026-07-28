# -*- coding: utf-8 -*-
"""Top Movie Reviews — 9:16 reel frames (1080x1920) in the page brand.

These are the frames you drop straight into CapCut. Text is burned in at the
right size for mobile, safe-zoned away from the UI overlays (top ~220px is
covered by the FB header, bottom ~420px by caption/buttons/CTA).

  reel_hook(text, out)                 opening frame — biggest type, stops scroll
  reel_beat(text, out, kicker)         mid-reel statement frame
  reel_title(top, big, bottom, out)    title card w/ small-big-small stack
  reel_end(text, out, question)        end frame w/ comment prompt

All original type on original backgrounds — no studio assets.
"""
from html import escape
import re

from image_html import _render_html

RW, RH = 1080, 1920

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Bebas+Neue&family=Inter:wght@400;600;700;800&display=swap" '
      'rel="stylesheet">')

B = {"bg1": "#1e1633", "bg2": "#0d0918", "amber": "#ffb703",
     "cream": "#f4f0ff", "mute": "#9d93b8", "rose": "#ef476f"}

# top/bottom padding keeps text clear of Facebook's reel UI overlays
_BASE = f"""
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{RW}px; height:{RH}px; overflow:hidden; position:relative;
       background:linear-gradient(168deg,{B['bg1']} 0%,{B['bg2']} 100%);
       font-family:'Inter',sans-serif; color:{B['cream']}; }}
  .glow {{ position:absolute; width:900px; height:520px; left:90px; top:-180px;
       background:radial-gradient(closest-side, rgba(255,183,3,.17), transparent);
       filter:blur(14px); }}
  .grain {{ position:absolute; inset:0;
       background:repeating-linear-gradient(180deg,
         rgba(255,255,255,.028) 0 2px, transparent 2px 5px); }}
  .safe {{ position:absolute; left:82px; right:82px; top:250px; bottom:430px;
       display:flex; flex-direction:column; justify-content:center;
       align-items:center; text-align:center; }}
  .brand {{ position:absolute; bottom:300px; left:0; right:0; text-align:center;
       font-family:'Bebas Neue',sans-serif; font-size:30px; letter-spacing:7px;
       color:{B['amber']}; opacity:.75; }}
"""


def _hl(txt, color):
    """*starred* words get the accent colour."""
    out = []
    for ln in txt.strip().split("\n"):
        h = re.sub(r"\*(.+?)\*",
                   lambda m: f'<span style="color:{color}">{m.group(1)}</span>',
                   escape(ln.strip()))
        out.append(f"<div>{h}</div>")
    return "\n".join(out)


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>{_BASE}{extra}</style></head><body>
  <div class="glow"></div>{inner}<div class="grain"></div>
  <div class="brand">TOP MOVIE REVIEWS</div>
</body></html>"""


def reel_hook(text, out_path, size=96):
    """Frame 1. Must work with sound off — this is the scroll-stopper."""
    extra = f""".big {{ font-family:'Bebas Neue',sans-serif; font-size:{size}px;
       line-height:1.04; letter-spacing:1px; }}"""
    inner = f'<div class="safe"><div class="big">{_hl(text, B["amber"])}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def reel_beat(text, out_path, kicker="", size=72):
    extra = f""".kick {{ font-size:26px; letter-spacing:6px; color:{B['rose']};
       font-weight:700; margin-bottom:34px; }}
  .beat {{ font-family:'Bebas Neue',sans-serif; font-size:{size}px;
       line-height:1.1; letter-spacing:1px; }}"""
    k = f'<div class="kick">{escape(kicker)}</div>' if kicker else ""
    inner = f'<div class="safe">{k}<div class="beat">{_hl(text, B["amber"])}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def reel_title(top, big, bottom, out_path):
    """top = small kicker (e.g. the year), big = the hero line (the film title),
    bottom = the payoff. Hero type auto-shrinks for long titles so it always fits."""
    n = len(big)
    hero = 132 if n <= 11 else 108 if n <= 16 else 86 if n <= 22 else 68
    extra = f""".t {{ font-size:38px; font-weight:600; color:{B['mute']};
       letter-spacing:6px; margin-bottom:26px; }}
  .b {{ font-family:'Bebas Neue',sans-serif; font-size:{hero}px; line-height:.96;
       color:{B['amber']}; letter-spacing:2px; }}
  .u {{ font-size:40px; font-weight:600; margin-top:30px; line-height:1.35; }}"""
    inner = (f'<div class="safe"><div class="t">{escape(top)}</div>'
             f'<div class="b">{escape(big)}</div>'
             f'<div class="u">{_hl(bottom, B["amber"])}</div></div>')
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def reel_end(text, out_path, question=""):
    extra = f""".e {{ font-family:'Bebas Neue',sans-serif; font-size:86px;
       line-height:1.06; letter-spacing:1px; margin-bottom:40px; }}
  .q {{ font-size:40px; font-weight:600; line-height:1.45; color:{B['cream']};
       border-top:2px solid rgba(255,183,3,.45); padding-top:34px; }}"""
    q = f'<div class="q">{_hl(question, B["amber"])}</div>' if question else ""
    inner = f'<div class="safe"><div class="e">{_hl(text, B["amber"])}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))
