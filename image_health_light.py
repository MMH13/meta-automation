# -*- coding: utf-8 -*-
"""Health Daily LIGHT templates — for high-frequency posting (8/day).

Shares the page's brand DNA with the flagship infographic (cream bg, deep green,
red accents, 💚 Health Daily header, "Be Conscious. Be Healthy. Be You.") but
lighter to produce/consume. The dense infographic stays the daily flagship.

  health_fact(kicker, text, ...)  -> "DID YOU KNOW?" / tip / food-spotlight card
  health_myth_fact(myth, fact)    -> red MYTH / green FACT split card
"""

from html import escape

from image_html import _render_html, W, H, _FONTS_HEALTH

GREEN = "#14532d"; DGREEN = "#0e3d20"; RED = "#c0392b"
CREAM = "#fbfdf9"; YELL = "#f8e16c"; MINT = "#e8f5ec"


def _hdr():
    return f"""
  <div class="hdr">
    <div class="logo">💚</div>
    <div><div class="bname">Health <span>Daily</span></div>
    <div class="btag">Be Conscious. Be Healthy. Be You.</div></div>
  </div>"""


_HDR_CSS = f"""
  .hdr {{ position:absolute; top:34px; left:44px; right:44px; display:flex;
       align-items:center; gap:14px; }}
  .logo {{ width:60px; height:60px; border-radius:50%; background:{MINT};
       border:3px solid {GREEN}; display:flex; align-items:center;
       justify-content:center; font-size:32px; }}
  .bname {{ font-size:34px; font-weight:800; color:{GREEN}; line-height:1; }}
  .bname span {{ color:{RED}; }}
  .btag {{ font-size:17px; font-weight:600; color:#555; margin-top:4px; }}
"""


def health_fact(text: str, out_path: str, kicker: str = "DID YOU KNOW?",
                emoji: str = "💡", footer: str = "Follow for daily health tips",
                accent: str = GREEN) -> str:
    """Single-idea card. Wrap *phrases* in stars to highlight them."""
    import re
    body = "<br>".join(
        re.sub(r"\*(.+?)\*", lambda m: f'<span class="hl">{m.group(1)}</span>',
               escape(ln.strip()))
        for ln in text.strip().split("\n"))
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_HEALTH}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{CREAM}; font-family:'Poppins',sans-serif; }}
  .ring {{ position:absolute; border-radius:50%; border:3px solid {accent};
       opacity:.10; }}
  .r1 {{ width:520px;height:520px; top:-170px; right:-160px; }}
  .r2 {{ width:340px;height:340px; bottom:-130px; left:-120px; }}
  {_HDR_CSS}
  .wrap {{ position:absolute; inset:170px 80px 140px; display:flex;
       flex-direction:column; justify-content:center; align-items:center;
       text-align:center; gap:34px; }}
  .kick {{ background:{accent}; color:#fff; font-size:30px; font-weight:700;
       letter-spacing:3px; padding:12px 30px; border-radius:30px; }}
  .emoji {{ font-size:130px; }}
  .txt {{ font-size:60px; font-weight:700; line-height:1.32; color:{DGREEN}; }}
  .hl {{ color:{RED}; }}
  .bar {{ width:110px; height:7px; background:{accent}; border-radius:4px; }}
  .foot {{ position:absolute; bottom:56px; left:0; right:0; text-align:center;
       font-size:28px; font-weight:600; color:#5a6b60; }}
</style></head><body>
  <div class="ring r1"></div><div class="ring r2"></div>
  {_hdr()}
  <div class="wrap">
    <div class="kick">{escape(kicker)}</div>
    <div class="emoji">{emoji}</div>
    <div class="txt">{body}</div>
    <div class="bar"></div>
  </div>
  <div class="foot">{escape(footer)}</div>
</body></html>"""
    return _render_html(html, out_path)


def health_myth_fact(myth: str, fact: str, out_path: str,
                     footer: str = "Follow for daily health tips") -> str:
    """Red MYTH (top) vs green FACT (bottom) split card."""
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_HEALTH}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{CREAM}; font-family:'Poppins',sans-serif; }}
  {_HDR_CSS}
  .panel {{ position:absolute; left:60px; right:60px; border-radius:22px;
       padding:44px 46px; display:flex; flex-direction:column; gap:16px; }}
  .myth {{ top:180px; height:460px; background:#fdecea; border:3px solid {RED}; }}
  .fact {{ bottom:150px; height:460px; background:{MINT}; border:3px solid {GREEN}; }}
  .tag {{ display:inline-flex; align-items:center; gap:12px; align-self:flex-start;
       font-size:30px; font-weight:800; letter-spacing:2px; padding:10px 26px;
       border-radius:24px; color:#fff; }}
  .myth .tag {{ background:{RED}; }}
  .fact .tag {{ background:{GREEN}; }}
  .body {{ font-size:44px; font-weight:600; line-height:1.34; }}
  .myth .body {{ color:#7d241a; }}
  .fact .body {{ color:{DGREEN}; }}
  .vs {{ position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
       width:96px; height:96px; border-radius:50%; background:#fff; z-index:4;
       border:4px solid {GREEN}; display:flex; align-items:center;
       justify-content:center; font-size:40px; }}
  .foot {{ position:absolute; bottom:56px; left:0; right:0; text-align:center;
       font-size:28px; font-weight:600; color:#5a6b60; }}
</style></head><body>
  {_hdr()}
  <div class="panel myth"><div class="tag">❌ MYTH</div>
    <div class="body">{escape(myth)}</div></div>
  <div class="vs">👇</div>
  <div class="panel fact"><div class="tag">✅ FACT</div>
    <div class="body">{escape(fact)}</div></div>
  <div class="foot">{escape(footer)}</div>
</body></html>"""
    return _render_html(html, out_path)
