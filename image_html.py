"""Organic post images via HTML/CSS rendered by headless Edge — free, offline-capable.

Recreates the natural "photo of a handwritten note" look of top BD creator
pages: warm bokeh backgrounds, torn/rotated paper, handwritten-style Bengali
fonts (proper script shaping via the browser's text engine — something PIL
cannot do).

Usage:
    from image_html import generate_html_image
    generate_html_image(text="৫টা ফ্রি AI টুল...", out_path="images/x.png",
                        style="torn_paper", footer="Mamun Hossain")

Text lines are separated by \n. Wrap a line in *stars* to highlight it.
"""

import re
import subprocess
import time
from html import escape
from pathlib import Path

_HERE = Path(__file__).parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

W, H = 1080, 1350  # 4:5, same as competitor posts

# Google Fonts: Galada = handwritten-feel Bengali+Latin; Hind Siliguri = clean.
_FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Galada&'
          'family=Hind+Siliguri:wght@400;600;700&display=swap" rel="stylesheet">')

# Clean sans for English health-card layouts.
_FONTS_HEALTH = ('<link href="https://fonts.googleapis.com/css2?'
                 'family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">')


def _lines_html(text: str) -> str:
    out = []
    for ln in text.strip().split("\n"):
        ln = ln.strip()
        if not ln:
            out.append('<div class="gap"></div>')
            continue
        # *starred* segments (whole line or inline) become highlighted spans
        html = re.sub(r"\*(.+?)\*", lambda m: f'<span class="hl">{m.group(1)}</span>',
                      escape(ln))
        out.append(f'<div class="line">{html}</div>')
    return "\n".join(out)


def _tpl_torn_paper(text: str, footer: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
         background: radial-gradient(120% 90% at 70% 10%, #4a3423 0%, #2b1d14 55%, #1a110b 100%); }}
  .bokeh {{ position:absolute; border-radius:50%; filter:blur(22px);
            background:rgba(255,196,110,.5); }}
  .b1 {{ width:130px;height:130px;top:70px;left:120px;opacity:.75 }}
  .b2 {{ width:90px;height:90px;top:180px;right:150px;opacity:.6 }}
  .b3 {{ width:170px;height:170px;top:40px;right:-40px;opacity:.5 }}
  .b4 {{ width:70px;height:70px;bottom:200px;left:60px;opacity:.5 }}
  .b5 {{ width:110px;height:110px;bottom:80px;right:90px;opacity:.65 }}
  .b6 {{ width:56px;height:56px;top:400px;left:40px;opacity:.4 }}
  .b7 {{ width:80px;height:80px;bottom:340px;right:30px;opacity:.35 }}
  .vignette {{ position:absolute; inset:0;
       background: radial-gradient(85% 75% at 50% 48%, transparent 55%, rgba(0,0,0,.55) 100%); }}
  .paper {{ position:absolute; left:50%; top:50%;
       width:820px; min-height:900px;
       transform:translate(-50%,-50%) rotate(-2.4deg);
       background:
         linear-gradient(174deg, #fbf7ee 0%, #f3ecdd 60%, #e9e0cd 100%);
       clip-path: polygon(2.2% 1.8%, 12% 0.4%, 25% 1.9%, 38% 0.6%, 52% 2%, 66% 0.3%,
         79% 1.7%, 91% 0.5%, 98.2% 2.6%, 99.4% 14%, 98.1% 27%, 99.6% 40%,
         98.3% 53%, 99.5% 66%, 98% 79%, 99.3% 90%, 97.6% 98.2%, 86% 99.5%,
         73% 98.2%, 60% 99.6%, 47% 98.3%, 34% 99.5%, 21% 98.1%, 9% 99.4%,
         1.6% 97.8%, 0.5% 86%, 1.9% 73%, 0.4% 60%, 1.8% 47%, 0.6% 34%, 2% 21%, 0.7% 9%);
       box-shadow: 0 30px 70px rgba(0,0,0,.55);
       padding: 90px 70px 110px;
       display:flex; flex-direction:column; justify-content:center; }}
  .paper::after {{ content:""; position:absolute; inset:0; opacity:.5; pointer-events:none;
       background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.45 0 0 0 0 0.4 0 0 0 0 0.33 0 0 0 0.06 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"); }}
  .note {{ font-family:'Galada','Hind Siliguri',sans-serif; color:#1d3f8f;
           text-align:center; position:relative; z-index:2; }}
  .line {{ font-size:72px; line-height:1.5; }}
  .line .hl {{ color:#c0392b; font-size:1.1em; }}
  .gap {{ height:26px; }}
  .footer {{ position:absolute; bottom:34px; width:100%; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:600; font-size:30px;
       color:rgba(255,235,205,.85); letter-spacing:.5px; z-index:3;
       text-shadow:0 2px 8px rgba(0,0,0,.6); }}
</style></head><body>
  <div class="bokeh b1"></div><div class="bokeh b2"></div><div class="bokeh b3"></div>
  <div class="bokeh b4"></div><div class="bokeh b5"></div><div class="bokeh b6"></div>
  <div class="bokeh b7"></div>
  <div class="vignette"></div>
  <div class="paper"><div class="note">{_lines_html(text)}</div></div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""


def _tpl_sticky_note(text: str, footer: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: linear-gradient(160deg,#1c2333 0%,#10141f 70%);; }}
  .glow {{ position:absolute; width:700px; height:500px; left:190px; top:-160px;
       background:radial-gradient(closest-side, rgba(110,160,255,.28), transparent);
       filter:blur(10px); }}
  .lamp {{ position:absolute; width:420px; height:420px; right:-80px; bottom:-60px;
       background:radial-gradient(closest-side, rgba(255,190,90,.35), transparent);
       filter:blur(8px); }}
  .note-wrap {{ position:absolute; left:50%; top:50%;
       transform:translate(-50%,-50%) rotate(1.8deg); }}
  .sticky {{ width:800px; min-height:840px;
       background: linear-gradient(178deg,#ffe98a 0%,#ffd95c 78%,#f4c93e 100%);
       box-shadow: 0 26px 60px rgba(0,0,0,.6);
       border-radius: 4px 4px 26px 4px;
       padding: 84px 64px 100px;
       display:flex; flex-direction:column; justify-content:center; position:relative; }}
  .sticky::before {{ content:""; position:absolute; top:-26px; left:50%;
       transform:translateX(-50%) rotate(-1deg);
       width:280px; height:56px; background:rgba(240,240,235,.65);
       box-shadow:0 4px 10px rgba(0,0,0,.18); }}
  .sticky::after {{ content:""; position:absolute; right:0; bottom:0;
       border-width:0 0 44px 44px; border-style:solid;
       border-color:transparent transparent rgba(0,0,0,.14) transparent; }}
  .note {{ font-family:'Galada','Hind Siliguri',sans-serif; color:#232323;
           text-align:center; }}
  .line {{ font-size:62px; line-height:1.55; }}
  .line .hl {{ color:#b03024; font-size:1.1em; }}
  .gap {{ height:24px; }}
  .footer {{ position:absolute; bottom:34px; width:100%; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:600; font-size:30px;
       color:rgba(215,225,255,.8); z-index:3; }}
</style></head><body>
  <div class="glow"></div><div class="lamp"></div>
  <div class="note-wrap"><div class="sticky"><div class="note">{_lines_html(text)}</div></div></div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""


def _tpl_whiteboard(text: str, footer: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: linear-gradient(180deg,#8a9bb0 0%,#6e8095 40%,#4f6076 100%); }}
  .desk {{ position:absolute; bottom:0; width:100%; height:230px;
       background: linear-gradient(180deg,#7a5232 0%,#5d3d24 100%); }}
  .desk::before {{ content:""; position:absolute; top:0; width:100%; height:14px;
       background:rgba(255,255,255,.14); }}
  .mug {{ position:absolute; bottom:150px; right:130px; width:110px; height:130px;
       background:linear-gradient(180deg,#d84c3f,#b03a2e); border-radius:10px 10px 18px 18px;
       box-shadow:0 14px 24px rgba(0,0,0,.35); }}
  .mug::after {{ content:""; position:absolute; right:-38px; top:24px; width:44px; height:56px;
       border:12px solid #b03a2e; border-radius:50%; }}
  .board {{ position:absolute; left:50%; top:80px; transform:translateX(-50%) rotate(-.6deg);
       width:880px; height:940px; background:linear-gradient(168deg,#ffffff 0%,#f4f6f4 55%,#e9edea 100%);
       border:26px solid #cfd6dd; border-bottom-color:#b8c0c8; border-radius:14px;
       box-shadow: 0 34px 70px rgba(0,0,0,.45), inset 0 0 60px rgba(160,175,190,.25);
       display:flex; align-items:center; justify-content:center; padding:70px 60px; }}
  .board::after {{ content:""; position:absolute; right:40px; bottom:-58px; width:150px; height:26px;
       background:#3a70c8; border-radius:6px; box-shadow:0 6px 12px rgba(0,0,0,.3);
       transform:rotate(4deg); }}
  .note {{ font-family:'Galada','Hind Siliguri',sans-serif; color:#20458c;
       text-align:center; }}
  .line {{ font-size:66px; line-height:1.55; }}
  .line .hl {{ color:#c0392b; font-size:1.1em; }}
  .gap {{ height:24px; }}
  .footer {{ position:absolute; bottom:60px; width:100%; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:600; font-size:30px;
       color:rgba(255,240,225,.9); z-index:3; text-shadow:0 2px 6px rgba(0,0,0,.5); }}
</style></head><body>
  <div class="desk"></div><div class="mug"></div>
  <div class="board"><div class="note">{_lines_html(text)}</div></div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""


def _tpl_notebook(text: str, footer: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: linear-gradient(150deg,#3d2c20 0%,#241a12 100%); }}
  .light {{ position:absolute; width:900px; height:700px; left:90px; top:-200px;
       background:radial-gradient(closest-side, rgba(255,205,130,.30), transparent); filter:blur(6px); }}
  .page-wrap {{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%) rotate(1.6deg); }}
  .page {{ width:840px; height:1020px; position:relative;
       background:
         repeating-linear-gradient(180deg, transparent 0 78px, rgba(90,130,200,.35) 78px 80px),
         linear-gradient(172deg,#fdfaf2 0%,#f4efe2 100%);
       box-shadow: 0 30px 66px rgba(0,0,0,.55);
       border-radius: 6px 14px 14px 6px;
       padding: 100px 70px 80px 130px;
       display:flex; align-items:center; }}
  .page::before {{ content:""; position:absolute; left:86px; top:0; bottom:0; width:3px;
       background:rgba(220,90,90,.5); }}
  .holes {{ position:absolute; left:-26px; top:60px; bottom:60px; width:52px;
       display:flex; flex-direction:column; justify-content:space-between; }}
  .hole {{ width:34px; height:34px; border-radius:50%;
       background:#241a12; border:6px solid #cfc8b8;
       box-shadow: inset 0 3px 6px rgba(0,0,0,.6); }}
  .note {{ font-family:'Galada','Hind Siliguri',sans-serif; color:#2b3550;
       text-align:left; width:100%; }}
  .line {{ font-size:60px; line-height:1.62; }}
  .line .hl {{ color:#b03024; font-size:1.08em; }}
  .gap {{ height:22px; }}
  .footer {{ position:absolute; bottom:36px; width:100%; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:600; font-size:30px;
       color:rgba(255,235,205,.85); z-index:3; }}
</style></head><body>
  <div class="light"></div>
  <div class="page-wrap"><div class="page">
    <div class="holes">""" + "".join('<div class="hole"></div>' for _ in range(8)) + f"""</div>
    <div class="note">{_lines_html(text)}</div>
  </div></div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""


def _tpl_gradient_poster(text: str, footer: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: linear-gradient(135deg,#131a3a 0%,#3a1d6e 45%,#0f4a6e 100%); }}
  .orb {{ position:absolute; border-radius:50%; filter:blur(4px); opacity:.5;
       border:3px solid rgba(140,200,255,.5); }}
  .o1 {{ width:400px;height:400px; top:-120px; right:-100px; }}
  .o2 {{ width:260px;height:260px; bottom:140px; left:-80px; }}
  .o3 {{ width:120px;height:120px; top:220px; left:90px;
       background:radial-gradient(circle,rgba(120,220,255,.25),transparent); border:none; }}
  .grain {{ position:absolute; inset:0; opacity:.35; pointer-events:none;
       background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.05 0'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); }}
  .brand {{ position:absolute; top:80px; width:100%; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:700; font-size:34px;
       letter-spacing:6px; color:rgba(140,215,255,.95); }}
  .bar {{ position:absolute; top:140px; left:50%; transform:translateX(-50%);
       width:120px; height:8px; background:#56d6ff; border-radius:4px; }}
  .content {{ position:absolute; inset:200px 90px 170px; display:flex;
       flex-direction:column; justify-content:center; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:700; color:#f4f8ff; }}
  .line {{ font-size:78px; line-height:1.45; }}
  .line .hl {{ color:#56d6ff; }}
  .gap {{ height:30px; }}
  .footer {{ position:absolute; bottom:56px; width:100%; text-align:center;
       font-family:'Hind Siliguri',sans-serif; font-weight:600; font-size:30px;
       color:rgba(200,220,255,.75); }}
</style></head><body>
  <div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
  <div class="grain"></div>
  <div class="brand">MAMUN HOSSAIN</div><div class="bar"></div>
  <div class="content">{_lines_html(text)}</div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""


def _tpl_chat_ui(text: str, footer: str) -> str:
    """text format: user message, then '---' on its own line, then AI reply."""
    parts = text.split("\n---\n")
    user_msg = parts[0].strip()
    ai_msg = parts[1].strip() if len(parts) > 1 else ""
    def bub(t):
        return "<br>".join(escape(x) for x in t.split("\n"))
    return f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: linear-gradient(160deg,#232735 0%,#15181f 100%);
       font-family:'Hind Siliguri',sans-serif; }}
  .phone {{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
       width:860px; height:1150px; background:#212121; border-radius:48px;
       box-shadow: 0 40px 90px rgba(0,0,0,.65), 0 0 0 14px #060606,
                   0 0 0 17px rgba(255,255,255,.08);
       overflow:hidden; display:flex; flex-direction:column; }}
  .head {{ padding:34px 44px; display:flex; align-items:center; gap:20px;
       border-bottom:1px solid rgba(255,255,255,.09); }}
  .logo {{ width:54px; height:54px; border-radius:50%;
       background:#fff; display:flex; align-items:center; justify-content:center;
       font-weight:700; color:#111; font-size:30px; }}
  .head .t {{ color:#ececec; font-size:34px; font-weight:600; }}
  .head .s {{ color:#19c37d; font-size:24px; }}
  .chat {{ flex:1; padding:44px 40px; display:flex; flex-direction:column; gap:34px; }}
  .bubble {{ max-width:82%; padding:30px 36px; border-radius:26px;
       font-size:35px; line-height:1.6; }}
  .user {{ align-self:flex-end; background:#2f5cd6; color:#f4f7ff;
       border-bottom-right-radius:8px; }}
  .ai {{ align-self:flex-start; background:#2f2f2f; color:#e9e9e9;
       border-bottom-left-radius:8px; }}
  .label {{ font-size:24px; opacity:.65; margin-bottom:10px; }}
  .typing {{ align-self:flex-start; color:#9a9a9a; font-size:28px; padding-left:12px; }}
  .footer {{ position:absolute; bottom:30px; width:100%; text-align:center;
       font-weight:600; font-size:30px; color:rgba(200,215,255,.7); }}
</style></head><body>
  <div class="phone">
    <div class="head"><div class="logo">AI</div>
      <div><div class="t">ChatGPT</div><div class="s">● online</div></div></div>
    <div class="chat">
      <div class="bubble user"><div class="label">আপনি:</div>{bub(user_msg)}</div>
      <div class="bubble ai"><div class="label">AI:</div>{bub(ai_msg)}</div>
      <div class="typing">পুরো প্রম্পট প্রথম কমেন্টে 👇</div>
    </div>
  </div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""


TEMPLATES = {
    "torn_paper": _tpl_torn_paper,
    "sticky_note": _tpl_sticky_note,
    "whiteboard": _tpl_whiteboard,
    "notebook": _tpl_notebook,
    "gradient_poster": _tpl_gradient_poster,
    "chat_ui": _tpl_chat_ui,
}


def _render_html(html: str, out_path: str) -> str:
    out = Path(out_path)
    if not out.is_absolute():
        out = _HERE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()  # so we can detect the fresh write, not a stale file
    tmp = out.with_suffix(".html")
    tmp.write_text(html, encoding="utf-8")
    subprocess.run([
        EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        f"--window-size={W},{H}", "--virtual-time-budget=15000",
        f"--screenshot={out}", tmp.as_uri(),
    ], check=True, capture_output=True, timeout=120)
    # --headless=new flushes the screenshot asynchronously AFTER the process
    # exits, so poll until the file appears and its size stops growing.
    last = -1
    for _ in range(40):  # up to ~12s
        time.sleep(0.3)
        if out.is_file():
            size = out.stat().st_size
            if size > 0 and size == last:
                break
            last = size
    else:
        raise RuntimeError("Edge produced no screenshot in time")
    tmp.unlink(missing_ok=True)
    return str(out)


def generate_html_image(text: str, out_path: str, style: str = "torn_paper",
                        footer: str = "Mamun Hossain") -> str:
    return _render_html(TEMPLATES[style](text, footer), out_path)


# ---- Health Daily branded card (clean English infographic style) -----------

_HEALTH_THEMES = {
    "teal_dark": {"bg": "linear-gradient(158deg,#0b4232 0%,#0d6c57 100%)",
                  "title": "#f5faf7", "eyebrow": "#6ee7b7", "chip": "rgba(110,231,183,.16)",
                  "chiptxt": "#d6f5e8", "accent": "#6ee7b7", "foot": "rgba(214,245,232,.8)"},
    "mint_light": {"bg": "linear-gradient(158deg,#ecfdf5 0%,#d1fae5 100%)",
                   "title": "#0b3d2e", "eyebrow": "#0d9668", "chip": "#ffffff",
                   "chiptxt": "#0b4232", "accent": "#0d9668", "foot": "rgba(11,66,50,.7)"},
}


def generate_health_image(title: str, bullets, out_path: str,
                          eyebrow: str = "HEALTH DAILY",
                          footer: str = "Follow for daily health tips",
                          theme: str = "teal_dark") -> str:
    """Clean health infographic: eyebrow label, big title, check-bulleted benefits.
    bullets: list of short strings (3-5 recommended)."""
    t = _HEALTH_THEMES[theme]
    items = "\n".join(
        f'<div class="item"><span class="tick">✓</span><span>{escape(b)}</span></div>'
        for b in bullets)
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_HEALTH}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{t['bg']}; font-family:'Poppins',sans-serif; }}
  .ring {{ position:absolute; border-radius:50%; border:3px solid {t['accent']};
       opacity:.16; }}
  .r1 {{ width:520px;height:520px; top:-160px; right:-150px; }}
  .r2 {{ width:300px;height:300px; bottom:120px; left:-120px; }}
  .wrap {{ position:absolute; inset:96px 90px 150px; display:flex;
       flex-direction:column; }}
  .eyebrow {{ font-size:34px; font-weight:700; letter-spacing:5px;
       color:{t['eyebrow']}; }}
  .bar {{ width:96px; height:8px; border-radius:4px; background:{t['accent']};
       margin:26px 0 40px; }}
  .title {{ font-size:82px; font-weight:800; line-height:1.12; color:{t['title']}; }}
  .items {{ margin-top:60px; display:flex; flex-direction:column; gap:34px; }}
  .item {{ display:flex; align-items:flex-start; gap:26px; font-size:46px;
       font-weight:500; color:{t['title']}; line-height:1.3; }}
  .tick {{ flex:none; width:60px; height:60px; border-radius:50%;
       background:{t['chip']}; color:{t['accent']}; font-weight:800;
       display:flex; align-items:center; justify-content:center; font-size:36px; }}
  .footer {{ position:absolute; bottom:56px; left:90px; right:90px;
       font-size:32px; font-weight:600; color:{t['foot']}; }}
</style></head><body>
  <div class="ring r1"></div><div class="ring r2"></div>
  <div class="wrap">
    <div class="eyebrow">{escape(eyebrow)}</div><div class="bar"></div>
    <div class="title">{escape(title)}</div>
    <div class="items">{items}</div>
  </div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""
    return _render_html(html, out_path)


# ---- Health Daily medical infographic (matches the page's established style)

def generate_health_infographic(data: dict, out_path: str) -> str:
    """Dense branded medical infographic, modeled on Health Daily's existing posts.

    data = {
      "title": "FATTY LIVER", "subtitle": "A SILENT PROBLEM",
      "subtitle2": "THAT CAN BECOME SERIOUS" (optional),
      "intro": "short 2-3 line explanation",
      "hero": {"emoji": "😴", "badge": "Mg" (optional), "caption": "..."},
      "alert": "top-right reminder chip text",
      "sections": [ {"heading": "COMMON SYMPTOMS",
                     "items": [{"e": "😴", "t": "Fatigue"}, ...]} x2-3 ],
      "protect": {"heading": "HOW TO PROTECT ...",
                  "items": [{"e":"🥗","t":"Eat a balanced diet"}, ... up to 6]},
      "goodnews": {"lead": "Good news:", "bold": "...", "rest": "..."},
      "note": "right cell of bottom banner (e.g. check-ups reminder)",
      "bottomline": "final one-liner",
    }
    """
    d = data
    GREEN = "#14532d"; DGREEN = "#0e3d20"; RED = "#c0392b"; CREAM = "#fbfdf9"
    YELL = "#f8e16c"

    def items_html(items, cls="itm"):
        return "\n".join(
            f'<div class="{cls}"><span class="ic">{i["e"]}</span>'
            f'<span class="tx">{escape(i["t"])}</span></div>' for i in items)

    sections_html = ""
    for s in d.get("sections", []):
        sections_html += (f'<div class="col"><div class="colhead">{escape(s["heading"])}</div>'
                          f'<div class="colbody">{items_html(s["items"])}</div></div>')

    protect = d.get("protect")
    protect_html = ""
    if protect:
        cells = "\n".join(
            f'<div class="pcell"><div class="pic">{i["e"]}</div>'
            f'<div class="ptx">{escape(i["t"])}</div></div>' for i in protect["items"])
        protect_html = (f'<div class="protect"><div class="phead">{escape(protect["heading"])}</div>'
                        f'<div class="prow">{cells}</div></div>')

    hero = d.get("hero", {})
    badge = (f'<div class="badge">{escape(hero["badge"])}</div>'
             if hero.get("badge") else "")

    gn = d.get("goodnews", {})
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_HEALTH}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{CREAM}; font-family:'Poppins',sans-serif; color:#1b1b1b; }}
  .page {{ position:absolute; inset:0; padding:28px 36px 24px; display:flex;
       flex-direction:column; gap:16px; }}
  /* header */
  .hdr {{ display:flex; justify-content:space-between; align-items:flex-start; }}
  .brand {{ display:flex; gap:16px; align-items:center; }}
  .logo {{ width:64px; height:64px; border-radius:50%; background:#e8f5ec;
       display:flex; align-items:center; justify-content:center; font-size:36px;
       border:3px solid {GREEN}; }}
  .bname {{ font-size:36px; font-weight:800; color:{GREEN}; line-height:1; }}
  .bname span {{ color:{RED}; }}
  .btag {{ font-size:18px; font-weight:600; color:#444; margin-top:6px; }}
  .alert {{ background:{DGREEN}; color:#fff; font-size:19px; font-weight:600;
       padding:12px 18px; border-radius:12px; max-width:350px; line-height:1.35; }}
  .alert b {{ color:{YELL}; }}
  /* title row */
  .trow {{ display:flex; gap:30px; align-items:center; }}
  .tl {{ flex:1.4; }}
  .title {{ font-size:64px; font-weight:800; color:{GREEN}; line-height:.98;
       letter-spacing:-1px; }}
  .sub {{ font-size:34px; font-weight:800; color:{RED}; margin-top:8px; line-height:1.05; }}
  .sub2 {{ font-size:24px; font-weight:700; color:#222; margin-top:4px; }}
  .intro {{ border-left:7px solid {GREEN}; padding:8px 0 8px 18px; margin-top:14px;
       font-size:21px; font-weight:500; line-height:1.4; color:#333; }}
  .hero {{ flex:1; display:flex; flex-direction:column; align-items:center; gap:10px; }}
  .hcirc {{ width:220px; height:220px; border-radius:50%; background:#e8f5ec;
       display:flex; align-items:center; justify-content:center; font-size:120px;
       position:relative; box-shadow:0 14px 30px rgba(20,83,45,.18); }}
  .badge {{ position:absolute; right:0; top:0; background:{RED}; color:#fff;
       font-size:28px; font-weight:800; width:72px; height:72px; border-radius:50%;
       display:flex; align-items:center; justify-content:center;
       border:5px solid #fff; }}
  .hcap {{ font-size:20px; font-weight:700; color:{GREEN}; text-align:center; }}
  /* section columns */
  .cols {{ display:flex; gap:18px; }}
  .col {{ flex:1; background:#f2f8f3; border:2px solid #dcebe0; border-radius:14px;
       overflow:hidden; display:flex; flex-direction:column; }}
  .colhead {{ background:{DGREEN}; color:#fff; font-size:21px; font-weight:700;
       text-align:center; padding:11px 8px; letter-spacing:.5px; }}
  .colbody {{ padding:14px 16px; display:flex; flex-direction:column; gap:12px; }}
  .itm {{ display:flex; align-items:center; gap:16px; }}
  .ic {{ flex:none; width:52px; height:52px; border-radius:50%; background:#fff;
       border:2px solid #dcebe0; display:flex; align-items:center;
       justify-content:center; font-size:27px; }}
  .tx {{ font-size:20px; font-weight:600; line-height:1.25; }}
  /* protect row */
  .protect {{ border:2px solid #dcebe0; border-radius:14px; overflow:hidden; }}
  .phead {{ background:{DGREEN}; color:{YELL}; font-size:22px; font-weight:800;
       text-align:center; padding:10px; letter-spacing:.5px; }}
  .prow {{ display:flex; background:#f2f8f3; padding:14px 10px; }}
  .pcell {{ flex:1; display:flex; flex-direction:column; align-items:center;
       gap:12px; padding:0 6px; }}
  .pic {{ width:74px; height:74px; border-radius:50%; background:#fff;
       border:2px solid #dcebe0; display:flex; align-items:center;
       justify-content:center; font-size:37px; }}
  .ptx {{ font-size:17px; font-weight:600; text-align:center; line-height:1.25; }}
  /* good news banner */
  .banner {{ display:flex; gap:0; border-radius:14px; overflow:hidden; }}
  .gn {{ flex:1.5; background:{DGREEN}; padding:14px 22px; color:#fff; }}
  .gn .lead {{ color:{YELL}; font-size:21px; font-weight:800; }}
  .gn .bold {{ font-size:23px; font-weight:800; line-height:1.2; }}
  .gn .rest {{ font-size:18px; font-weight:500; color:#dcebe0; margin-top:4px; }}
  .nt {{ flex:1; background:{GREEN}; padding:14px 20px; color:#fff; font-size:18px;
       font-weight:600; line-height:1.35; display:flex; align-items:center; }}
  .nt b {{ color:{YELL}; }}
  .bottom {{ text-align:center; font-size:22px; font-weight:700; color:{GREEN}; }}
  .bottom span {{ color:{RED}; }}
</style></head><body>
<div class="page">
  <div class="hdr">
    <div class="brand"><div class="logo">💚</div>
      <div><div class="bname">Health <span>Daily</span></div>
      <div class="btag">Be Conscious. Be Healthy. Be You.</div></div></div>
    <div class="alert">🔔 {d.get("alert","")}</div>
  </div>
  <div class="trow">
    <div class="tl">
      <div class="title">{escape(d["title"])}</div>
      <div class="sub">{escape(d.get("subtitle",""))}</div>
      {f'<div class="sub2">{escape(d["subtitle2"])}</div>' if d.get("subtitle2") else ''}
      <div class="intro">{escape(d.get("intro",""))}</div>
    </div>
    <div class="hero"><div class="hcirc">{hero.get("emoji","💚")}{badge}</div>
      <div class="hcap">{escape(hero.get("caption",""))}</div></div>
  </div>
  <div class="cols">{sections_html}</div>
  {protect_html}
  <div class="banner">
    <div class="gn"><span class="lead">{escape(gn.get("lead","Good news:"))}</span>
      <div class="bold">{escape(gn.get("bold",""))}</div>
      <div class="rest">{escape(gn.get("rest",""))}</div></div>
    <div class="nt"><span>📋&nbsp; {d.get("note","")}</span></div>
  </div>
  <div class="bottom">{d.get("bottomline","Your body deserves care. Your health deserves attention. 💚")}</div>
</div>
</body></html>"""
    return _render_html(html, out_path)


if __name__ == "__main__":
    p = generate_html_image("৫টা ফ্রি AI টুল\n*যা প্রতি সপ্তাহে আপনার*\n২০+ ঘণ্টা বাঁচাবে! 🤯\n\nলিস্ট ক্যাপশনে 👇",
                            "images/html_test.png")
    print("wrote", p)
