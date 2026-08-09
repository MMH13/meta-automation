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


def _svg_page(svg, caption="", extra=""):
    cap = (f'<div class="cap"><div class="content">{_lines_html(caption)}</div></div>'
           if caption else "")
    return _page(
        f'<div class="scene">{svg}</div>{cap}',
        extra + """
  .scene { position:absolute; inset:0; display:flex; align-items:center;
       justify-content:center; }
  .cap { position:absolute; left:86px; right:86px; bottom:460px;
       text-align:center; }
  .cap .content { font-size:44px; line-height:1.4; }
  .cap .content .hl { color:#e33b4e; font-weight:700; }
""")


def sr_scene_house(out_path, caption="", lit_window=True):
    """Original silhouette illustration — a house at night. No stock/photo assets."""
    glow = ('<rect x="430" y="300" width="70" height="90" fill="#ffb84d" opacity="0.85"/>'
            if lit_window else "")
    svg = f"""<svg width="1080" height="1920" viewBox="0 0 1080 1920">
      <polygon points="300,760 540,560 780,760" fill="#15171d"/>
      <rect x="330" y="760" width="420" height="380" fill="#1a1d24"/>
      <polygon points="540,560 540,610 300,790 300,760" fill="#0d0f14" opacity="0.4"/>
      {glow}
      <rect x="500" y="950" width="90" height="190" fill="#0a0b0e"/>
      <circle cx="150" cy="220" r="70" fill="#2a2d36" opacity="0.5"/>
    </svg>"""
    return _render_html(_svg_page(svg, caption), out_path, size=(RW, RH))


def sr_scene_hallway(out_path, caption=""):
    """Original perspective-line hallway illustration, door glowing at the end."""
    svg = """<svg width="1080" height="1920" viewBox="0 0 1080 1920">
      <polygon points="150,1920 930,1920 620,760 460,760" fill="#101217"/>
      <polygon points="150,1920 460,760 460,700 100,1920" fill="#0a0b0e"/>
      <polygon points="930,1920 620,760 620,700 980,1920" fill="#0a0b0e"/>
      <rect x="500" y="640" width="80" height="130" fill="#c94a3a" opacity="0.55"/>
    </svg>"""
    return _render_html(_svg_page(svg, caption), out_path, size=(RW, RH))


def sr_scene_door(out_path, caption="", ajar=True):
    """Original door illustration, slightly open with dark gap if ajar."""
    gap = ('<polygon points="540,560 620,560 600,1400 540,1400" fill="#020304"/>'
           if ajar else "")
    svg = f"""<svg width="1080" height="1920" viewBox="0 0 1080 1920">
      <rect x="340" y="560" width="400" height="840" fill="#1c2027"/>
      <rect x="340" y="560" width="400" height="840" fill="none"
            stroke="#3a3f4a" stroke-width="6"/>
      <circle cx="700" cy="990" r="12" fill="#8a8f99"/>
      {gap}
    </svg>"""
    return _render_html(_svg_page(svg, caption), out_path, size=(RW, RH))


def sr_scene_window(out_path, caption="", silhouette=True):
    """Original window illustration, optional silhouette figure outside."""
    fig = ('<ellipse cx="540" cy="880" rx="70" ry="130" fill="#050608"/>'
           '<circle cx="540" cy="720" r="46" fill="#050608"/>' if silhouette else "")
    svg = f"""<svg width="1080" height="1920" viewBox="0 0 1080 1920">
      <rect x="290" y="620" width="500" height="620" fill="#1a2230"/>
      <rect x="290" y="620" width="500" height="620" fill="none"
            stroke="#3a3f4a" stroke-width="10"/>
      <line x1="540" y1="620" x2="540" y2="1240" stroke="#3a3f4a" stroke-width="8"/>
      <line x1="290" y1="930" x2="790" y2="930" stroke="#3a3f4a" stroke-width="8"/>
      {fig}
    </svg>"""
    return _render_html(_svg_page(svg, caption), out_path, size=(RW, RH))


def sr_scene_clock(out_path, caption="", hour=3, minute=0):
    """Original clock-face illustration for time-stamp beats."""
    import math
    hh = ((hour % 12) + minute / 60) * 30
    mm = minute * 6
    def _hand(deg, length, width, color):
        rad = math.radians(deg - 90)
        x2 = 540 + length * math.cos(rad)
        y2 = 900 + length * math.sin(rad)
        return f'<line x1="540" y1="900" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
    svg = f"""<svg width="1080" height="1920" viewBox="0 0 1080 1920">
      <circle cx="540" cy="900" r="260" fill="#12141a" stroke="#3a3f4a" stroke-width="6"/>
      {_hand(hh, 130, 14, '#eceef2')}
      {_hand(mm, 190, 8, '#e33b4e')}
      <circle cx="540" cy="900" r="14" fill="#e33b4e"/>
    </svg>"""
    return _render_html(_svg_page(svg, caption), out_path, size=(RW, RH))


def sr_end(text, out_path, question=""):
    extra = (".line { font-size:60px; line-height:1.38; } .line .hl { color:#e33b4e; font-weight:700; }"
             " .q { font-size:36px; font-weight:500; color:#eceef2; line-height:1.5;"
             " border-top:2px solid #e33b4e77; padding-top:30px; margin-top:10px; }")
    q = f'<div class="q">{escape(question)}</div>' if question else ""
    inner = f'<div class="safe"><div class="content">{_lines_html(text)}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))
