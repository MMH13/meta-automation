# -*- coding: utf-8 -*-
"""Health Daily — 9:16 reel frames (1080x1920).

Brand per the growth-OS mandate: bright, trustworthy, clean — white, blue and
green, not the dark cinematic look used for the movie page. Text is safe-zoned
clear of Facebook's reel UI (top ~250px, bottom ~430px).

  hd_hook(text, out)                opening frame — biggest type
  hd_beat(text, out, kicker)        mid-reel statement
  hd_end(text, out, question)       closing frame + engagement question
"""
from html import escape
import re

from image_html import _render_html

RW, RH = 1080, 1920

_F = ('<link href="https://fonts.googleapis.com/css2?'
      'family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600;700'
      '&display=swap" rel="stylesheet">')

# bright, clinical-but-warm palette
C = {
    "bg1": "#f7fbff",     # near-white blue
    "bg2": "#e8f2fb",
    "ink": "#12303f",     # deep readable slate
    "blue": "#12658f",    # trust blue
    "green": "#1f9d63",   # health green
    "mute": "#5b7a8c",
}


def _hl(txt, color):
    """*starred* phrases take the accent colour."""
    out = []
    for ln in txt.strip().split("\n"):
        h = re.sub(r"\*(.+?)\*",
                   lambda m: f'<span style="color:{color}">{m.group(1)}</span>',
                   escape(ln.strip()))
        out.append(f"<div>{h}</div>")
    return "\n".join(out)


def _page(inner, extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">{_F}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{RW}px; height:{RH}px; overflow:hidden; position:relative;
       background:linear-gradient(170deg,{C['bg1']} 0%,{C['bg2']} 100%);
       font-family:'Inter',sans-serif; color:{C['ink']}; }}
  .blob {{ position:absolute; border-radius:50%; filter:blur(2px); opacity:.5; }}
  .b1 {{ width:520px; height:520px; right:-160px; top:120px;
       background:radial-gradient(circle at 30% 30%, #d6ecff, transparent 70%); }}
  .b2 {{ width:460px; height:460px; left:-150px; bottom:380px;
       background:radial-gradient(circle at 60% 40%, #d8f5e6, transparent 70%); }}
  .rule {{ position:absolute; left:0; right:0; top:0; height:12px;
       background:linear-gradient(90deg,{C['blue']},{C['green']}); }}
  .safe {{ position:absolute; left:86px; right:86px; top:250px; bottom:430px;
       display:flex; flex-direction:column; justify-content:center;
       align-items:center; text-align:center; }}
  .brand {{ position:absolute; bottom:300px; left:0; right:0; text-align:center;
       font-family:'Poppins',sans-serif; font-size:30px; font-weight:700;
       letter-spacing:5px; color:{C['blue']}; opacity:.8; }}
  {extra}
</style></head><body>
  <div class="rule"></div><div class="blob b1"></div><div class="blob b2"></div>
  {inner}
  <div class="brand">HEALTH DAILY</div>
</body></html>"""


def hd_hook(text, out_path, size=90):
    extra = f""".big {{ font-family:'Poppins',sans-serif; font-weight:800;
       font-size:{size}px; line-height:1.14; letter-spacing:-1px; }}"""
    inner = f'<div class="safe"><div class="big">{_hl(text, C["blue"])}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def hd_beat(text, out_path, kicker="", size=74):
    extra = f""".kick {{ font-family:'Poppins',sans-serif; font-size:26px;
       font-weight:700; letter-spacing:5px; color:{C['green']};
       margin-bottom:34px; text-transform:uppercase; }}
  .beat {{ font-family:'Poppins',sans-serif; font-weight:700; font-size:{size}px;
       line-height:1.2; letter-spacing:-.5px; }}"""
    k = f'<div class="kick">{escape(kicker)}</div>' if kicker else ""
    inner = f'<div class="safe">{k}<div class="beat">{_hl(text, C["blue"])}</div></div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))


def hd_end(text, out_path, question=""):
    extra = f""".e {{ font-family:'Poppins',sans-serif; font-weight:800;
       font-size:80px; line-height:1.16; letter-spacing:-1px; margin-bottom:40px; }}
  .q {{ font-size:40px; font-weight:600; line-height:1.45; color:{C['ink']};
       border-top:3px solid {C['green']}; padding-top:34px; }}"""
    q = f'<div class="q">{_hl(question, C["green"])}</div>' if question else ""
    inner = f'<div class="safe"><div class="e">{_hl(text, C["blue"])}</div>{q}</div>'
    return _render_html(_page(inner, extra), out_path, size=(RW, RH))
