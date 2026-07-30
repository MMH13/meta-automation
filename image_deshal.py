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

# === Radio Deshal signature brand (OWN colors — deliberately NOT earki red) ===
BRAND = {
    "teal":   "#0e4d5c",   # primary deep teal
    "teal2":  "#0a3a45",   # darker teal (gradient end)
    "yellow": "#ffcc29",   # sunny accent
    "cream":  "#fdfbf3",
    "ink":    "#0a2a32",
}

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


def deshal_headline(headline, out_path, dateline="রেডিও দেশাল ব্যুরো",
                    kicker="ব্যঙ্গ সংবাদ", emoji=""):
    """Fake-news 'breaking headline' satire card in Radio Deshal's OWN brand
    (teal + yellow). For EVERGREEN/safe satire only — no real people/politics."""
    B = BRAND
    hero = f'<div class="hero">{emoji}</div>' if emoji else ""
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_BN}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:linear-gradient(160deg,{B['teal']} 0%,{B['teal2']} 100%);
       font-family:'Hind Siliguri',sans-serif; }}
  .grain {{ position:absolute; inset:0; opacity:.06;
       background-image:radial-gradient(#fff 1px, transparent 1px);
       background-size:22px 22px; }}
  /* top brand bar */
  .bar {{ position:absolute; top:0; left:0; right:0; height:120px;
       background:{B['yellow']}; display:flex; align-items:center;
       padding:0 56px; gap:20px; }}
  .logo {{ width:70px; height:70px; border-radius:50%; background:{B['teal']};
       display:flex; align-items:center; justify-content:center; font-size:38px; }}
  .brandname {{ font-family:'Baloo Da 2',cursive; font-weight:800; font-size:46px;
       color:{B['teal']}; line-height:1; }}
  .live {{ margin-left:auto; background:{B['teal']}; color:{B['yellow']};
       font-family:'Baloo Da 2',cursive; font-weight:800; font-size:28px;
       padding:12px 24px; border-radius:10px; letter-spacing:1px; }}
  /* kicker tag */
  .kick {{ position:absolute; top:180px; left:56px; background:{B['yellow']};
       color:{B['ink']}; font-family:'Baloo Da 2',cursive; font-weight:800;
       font-size:32px; padding:10px 26px; border-radius:8px; letter-spacing:1px; }}
  .wrap {{ position:absolute; left:56px; right:56px; top:270px; bottom:230px;
       display:flex; flex-direction:column; justify-content:center; gap:30px; }}
  {hero and '.hero { font-size:130px; }'}
  .headline {{ font-family:'Baloo Da 2',cursive; font-weight:800;
       font-size:82px; line-height:1.28; color:#fff; }}
  .headline .hl {{ color:{B['yellow']}; }}
  /* bottom ticker */
  .ticker {{ position:absolute; bottom:0; left:0; right:0; height:150px;
       background:{B['yellow']}; display:flex; align-items:center; padding:0 56px; }}
  .tk-tag {{ background:{B['teal']}; color:{B['yellow']}; font-family:'Baloo Da 2',cursive;
       font-weight:800; font-size:30px; padding:14px 26px; border-radius:8px;
       margin-right:26px; white-space:nowrap; }}
  .dateline {{ font-size:34px; font-weight:600; color:{B['ink']}; line-height:1.25; }}
</style></head><body>
  <div class="grain"></div>
  <div class="bar"><div class="logo">📻</div>
    <div class="brandname">রেডিও দেশাল</div>
    <div class="live">সংবাদ</div></div>
  <div class="kick">🎙️ {escape(kicker)}</div>
  <div class="wrap">{hero}
    <div class="headline">{_bn_hl(headline, B['yellow'])}</div></div>
  <div class="ticker"><div class="tk-tag">দেশাল বিশেষ</div>
    <div class="dateline">— {escape(dateline)}</div></div>
</body></html>"""
    return _render_html(html, out_path)


def deshal_story(title, story_text, out_path, kicker="আজকের গল্প", emoji="💛"):
    """Long-form narrative/story card in Radio Deshal's OWN brand (teal + yellow).
    Unlike deshal_card (big punchy one-liners), this fits an actual paragraph —
    for the occasional emotional/relatable 'গল্প' post, not the meme one-liners."""
    B = BRAND
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_BN}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:linear-gradient(165deg,{B['teal']} 0%,{B['teal2']} 100%);
       font-family:'Hind Siliguri',sans-serif; }}
  .grain {{ position:absolute; inset:0; opacity:.05;
       background-image:radial-gradient(#fff 1px, transparent 1px);
       background-size:22px 22px; }}
  .bar {{ position:absolute; top:0; left:0; right:0; height:110px;
       background:{B['yellow']}; display:flex; align-items:center;
       padding:0 52px; gap:18px; }}
  .logo {{ width:62px; height:62px; border-radius:50%; background:{B['teal']};
       display:flex; align-items:center; justify-content:center; font-size:32px; }}
  .brandname {{ font-family:'Baloo Da 2',cursive; font-weight:800; font-size:40px;
       color:{B['teal']}; line-height:1; }}
  .kick {{ position:absolute; top:150px; left:52px; background:{B['yellow']};
       color:{B['ink']}; font-family:'Baloo Da 2',cursive; font-weight:800;
       font-size:28px; padding:9px 22px; border-radius:8px; letter-spacing:.5px; }}
  .wrap {{ position:absolute; left:66px; right:66px; top:230px; bottom:130px;
       display:flex; flex-direction:column; gap:26px; overflow:hidden; }}
  .emoji {{ font-size:64px; text-align:center; }}
  .title {{ font-family:'Baloo Da 2',cursive; font-weight:800; font-size:52px;
       line-height:1.28; color:{B['yellow']}; text-align:center; }}
  .body {{ font-size:34px; line-height:1.62; color:{B['cream']}; font-weight:500; }}
  .body p {{ margin-bottom:22px; }}
  .body .hl {{ color:{B['yellow']}; font-weight:700; }}
  .foot {{ position:absolute; bottom:0; left:0; right:0; height:90px;
       background:{B['yellow']}; display:flex; align-items:center;
       justify-content:center; font-family:'Baloo Da 2',cursive; font-weight:800;
       font-size:32px; color:{B['ink']}; }}
</style></head><body>
  <div class="grain"></div>
  <div class="bar"><div class="logo">📻</div>
    <div class="brandname">রেডিও দেশাল</div></div>
  <div class="kick">{escape(kicker)}</div>
  <div class="wrap">
    <div class="emoji">{emoji}</div>
    <div class="title">{escape(title)}</div>
    <div class="body">{"".join(f'<p>{_bn_hl_inline(p, B["yellow"])}</p>' for p in story_text.strip().split(chr(10)+chr(10)))}</div>
  </div>
  <div class="foot">👉 রেডিও দেশাল</div>
</body></html>"""
    return _render_html(html, out_path)


def _bn_hl_inline(text, color):
    import re
    return re.sub(r"\*(.+?)\*", lambda m: f'<span class="hl">{m.group(1)}</span>', escape(text.strip()))


def _bn_hl(text, color):
    import re
    out = []
    for ln in text.strip().split("\n"):
        h = re.sub(r"\*(.+?)\*", lambda m: f'<span class="hl">{m.group(1)}</span>',
                   escape(ln.strip()))
        out.append(h)
    return "<br>".join(out)
