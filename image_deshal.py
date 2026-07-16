# -*- coding: utf-8 -*-
"""রেডিও দেশাল (Radio Deshal) image templates — bright, playful Bengali entertainment cards.

deshal_card(): vibrant gradient, big Bengali text (*red/yellow highlights*), brand badge.
deshal_versus(): two-panel "X vs Y" relatable comparison.
Bengali renders correctly via the browser text engine (Hind Siliguri font).
"""

from html import escape

from image_html import _render_html, W, H

_FONTS_BN = ('<link href="https://fonts.googleapis.com/css2?'
             'family=Hind+Siliguri:wght@400;500;600;700&family=Baloo+Da+2:wght@600;700;800'
             '&display=swap" rel="stylesheet">')

# rotating fun gradients (bright, entertainment vibe)
THEMES = {
    "sunset":  ("linear-gradient(150deg,#ff6b6b 0%,#ee5a6f 45%,#f0932b 100%)", "#fff3d6"),
    "grape":   ("linear-gradient(150deg,#6c5ce7 0%,#a55eea 50%,#fd79a8 100%)", "#ffe8a3"),
    "ocean":   ("linear-gradient(150deg,#0984e3 0%,#00cec9 100%)", "#fff3b0"),
    "mango":   ("linear-gradient(150deg,#f7971e 0%,#ffd200 100%)", "#7a3e00"),
    "berry":   ("linear-gradient(150deg,#c31432 0%,#240b36 100%)", "#ffd93d"),
    "mint":    ("linear-gradient(150deg,#11998e 0%,#38ef7d 100%)", "#0b3d2e"),
}


def _bn_lines(text, hl):
    out = []
    for ln in text.strip().split("\n"):
        ln = ln.strip()
        if not ln:
            out.append('<div class="gap"></div>'); continue
        import re
        h = re.sub(r"\*(.+?)\*", lambda m: f'<span class="hl" style="color:{hl}">{m.group(1)}</span>',
                   escape(ln))
        out.append(f'<div class="ln">{h}</div>')
    return "\n".join(out)


def deshal_card(text, out_path, theme="sunset", emoji="", badge_bn="রেডিও দেশাল"):
    bg, hl = THEMES[theme]
    hero = f'<div class="hero">{emoji}</div>' if emoji else ""
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_BN}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{bg}; font-family:'Hind Siliguri',sans-serif; }}
  .blob {{ position:absolute; border-radius:50%; background:rgba(255,255,255,.12); }}
  .b1 {{ width:420px;height:420px; top:-140px; right:-120px; }}
  .b2 {{ width:300px;height:300px; bottom:-100px; left:-90px; }}
  .badge {{ position:absolute; top:56px; left:0; right:0; text-align:center;
       font-family:'Baloo Da 2',cursive; font-size:40px; font-weight:800;
       color:#fff; letter-spacing:1px; text-shadow:0 3px 12px rgba(0,0,0,.25); }}
  .badge::before {{ content:"📻 "; }}
  .wrap {{ position:absolute; inset:170px 80px 150px; display:flex;
       flex-direction:column; justify-content:center; align-items:center;
       text-align:center; gap:20px; }}
  .hero {{ font-size:150px; filter:drop-shadow(0 12px 26px rgba(0,0,0,.28)); }}
  .ln {{ font-family:'Baloo Da 2',cursive; font-weight:700; font-size:74px;
       line-height:1.34; color:#fff; text-shadow:0 3px 14px rgba(0,0,0,.22); }}
  .hl {{ font-weight:800; }}
  .gap {{ height:24px; }}
  .foot {{ position:absolute; bottom:60px; left:0; right:0; text-align:center;
       font-size:32px; font-weight:600; color:rgba(255,255,255,.85); }}
</style></head><body>
  <div class="blob b1"></div><div class="blob b2"></div>
  <div class="badge">{escape(badge_bn)}</div>
  <div class="wrap">{hero}<div class="txt">{_bn_lines(text, hl)}</div></div>
  <div class="foot">👉 ফলো করুন রেডিও দেশাল</div>
</body></html>"""
    return _render_html(html, out_path)


def deshal_versus(top_label, top_text, bottom_label, bottom_text, out_path,
                  emoji_top="😎", emoji_bottom="😭"):
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_BN}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       font-family:'Hind Siliguri',sans-serif; }}
  .half {{ position:absolute; left:0; right:0; height:50%; display:flex;
       flex-direction:column; align-items:center; justify-content:center;
       text-align:center; padding:70px 80px; gap:14px; }}
  .top {{ top:0; background:linear-gradient(150deg,#0984e3,#00cec9); }}
  .bottom {{ bottom:0; background:linear-gradient(150deg,#e84393,#f0932b); }}
  .emoji {{ font-size:120px; filter:drop-shadow(0 10px 22px rgba(0,0,0,.25)); }}
  .label {{ font-family:'Baloo Da 2',cursive; font-weight:800; font-size:38px;
       color:rgba(255,255,255,.9); letter-spacing:2px; }}
  .txt {{ font-family:'Baloo Da 2',cursive; font-weight:700; font-size:52px;
       line-height:1.3; color:#fff; text-shadow:0 3px 12px rgba(0,0,0,.22); }}
  .vs {{ position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
       width:130px; height:130px; border-radius:50%; background:#fff;
       display:flex; align-items:center; justify-content:center; z-index:5;
       font-family:'Baloo Da 2',cursive; font-weight:800; font-size:52px;
       color:#e84393; box-shadow:0 10px 30px rgba(0,0,0,.35); }}
  .badge {{ position:absolute; top:34px; left:0; right:0; text-align:center;
       font-family:'Baloo Da 2',cursive; font-size:34px; font-weight:800;
       color:#fff; text-shadow:0 2px 10px rgba(0,0,0,.3); z-index:6; }}
</style></head><body>
  <div class="badge">📻 রেডিও দেশাল</div>
  <div class="half top"><div class="emoji">{emoji_top}</div>
    <div class="label">{escape(top_label)}</div>
    <div class="txt">{_bn_lines_plain(top_text)}</div></div>
  <div class="half bottom"><div class="emoji">{emoji_bottom}</div>
    <div class="label">{escape(bottom_label)}</div>
    <div class="txt">{_bn_lines_plain(bottom_text)}</div></div>
  <div class="vs">VS</div>
</body></html>"""
    return _render_html(html, out_path)


def _bn_lines_plain(text):
    return "<br>".join(escape(x) for x in text.strip().split("\n"))
