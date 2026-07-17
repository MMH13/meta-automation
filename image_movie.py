# -*- coding: utf-8 -*-
"""Top Movie Reviews — cinematic templates (midnight violet + amber gold).

Distinct from every other page brand (Health=cream/green, Deshal=teal/yellow,
Suspense=black/red, Mamun=navy/cyan, Style=cream/charcoal/gold).

CONTENT RULE: original text on branded graphics ONLY. Never posters, stills, or
clips — studios are the most aggressive rights claimants on Facebook, and
reposted footage is how pages get deleted rather than throttled.

  movie_review(title, year, rating, verdict, line)  -> star-rated review card
  movie_list(title, items, kicker)                  -> numbered recommendation list
  movie_take(text, kicker, emoji)                   -> hot take / trivia / this-or-that
"""

from html import escape

from image_html import _render_html, W, H

_FONTS_MV = ('<link href="https://fonts.googleapis.com/css2?'
             'family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&'
             'display=swap" rel="stylesheet">')

BRAND = {
    "bg1":   "#1e1633",   # midnight violet
    "bg2":   "#120c21",   # deeper
    "amber": "#ffb703",   # premiere gold
    "cream": "#f4f0ff",
    "mute":  "#9d93b8",
    "rose":  "#ef476f",
}
B = BRAND

_CSS = f"""
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:linear-gradient(165deg,{B['bg1']} 0%,{B['bg2']} 100%);
       font-family:'Inter',sans-serif; color:{B['cream']}; }}
  .glow {{ position:absolute; width:820px; height:420px; left:130px; top:-200px;
       background:radial-gradient(closest-side, rgba(255,183,3,.16), transparent);
       filter:blur(12px); }}
  .sprocket {{ position:absolute; top:0; bottom:0; width:44px;
       background:repeating-linear-gradient(180deg,
         rgba(255,255,255,.09) 0 26px, transparent 26px 60px); }}
  .sl {{ left:0; }} .sr {{ right:0; }}
  .hdr {{ position:absolute; top:60px; left:100px; right:100px; display:flex;
       align-items:center; gap:18px; }}
  .hdr .bar {{ flex:1; height:1px; background:{B['amber']}; opacity:.5; }}
  .pname {{ font-family:'Bebas Neue',sans-serif; font-size:34px; letter-spacing:5px;
       color:{B['amber']}; }}
  .foot {{ position:absolute; bottom:58px; left:0; right:0; text-align:center;
       font-size:23px; letter-spacing:3px; color:{B['mute']}; }}
"""


def _hdr():
    return ('<div class="glow"></div><div class="sprocket sl"></div>'
            '<div class="sprocket sr"></div>'
            '<div class="hdr"><div class="bar"></div>'
            '<div class="pname">TOP MOVIE REVIEWS</div>'
            '<div class="bar"></div></div>')


def _stars(rating):
    full = int(rating)
    half = (rating - full) >= 0.5
    s = "★" * full + ("½" if half else "") + "☆" * (5 - full - (1 if half else 0))
    return s


def movie_review(title, year, rating, verdict, line, out_path, genre=""):
    """rating: float out of 5. verdict: short tag e.g. 'WORTH IT'. line: 1-2 sentences."""
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_MV}
<style>
  {_CSS}
  .wrap {{ position:absolute; inset:170px 100px 140px; display:flex;
       flex-direction:column; justify-content:center; gap:26px; }}
  .kick {{ font-size:22px; letter-spacing:5px; color:{B['rose']}; font-weight:600; }}
  .title {{ font-family:'Bebas Neue',sans-serif; font-size:104px; line-height:.98;
       letter-spacing:1px; }}
  .meta {{ font-size:28px; color:{B['mute']}; letter-spacing:2px; }}
  .stars {{ font-size:76px; color:{B['amber']}; letter-spacing:6px; }}
  .rnum {{ font-family:'Bebas Neue',sans-serif; font-size:44px; color:{B['cream']};
       margin-left:14px; }}
  .line {{ font-size:36px; font-weight:400; line-height:1.42; color:#e6e0f5; }}
  .verdict {{ align-self:flex-start; background:{B['amber']}; color:{B['bg2']};
       font-family:'Bebas Neue',sans-serif; font-size:36px; letter-spacing:3px;
       padding:12px 32px; border-radius:6px; }}
</style></head><body>
  {_hdr()}
  <div class="wrap">
    <div class="kick">THE REVIEW</div>
    <div class="title">{escape(title)}</div>
    <div class="meta">{escape(str(year))}{('  ·  ' + escape(genre)) if genre else ''}</div>
    <div class="stars">{_stars(rating)}<span class="rnum">{rating}/5</span></div>
    <div class="line">{escape(line)}</div>
    <div class="verdict">{escape(verdict)}</div>
  </div>
  <div class="foot">FOLLOW FOR DAILY REVIEWS</div>
</body></html>"""
    return _render_html(html, out_path)


def movie_list(title, items, out_path, kicker="THE WATCHLIST"):
    li = "\n".join(
        f'<div class="it"><span class="n">{i+1:02d}</span>'
        f'<span class="t">{escape(x)}</span></div>' for i, x in enumerate(items))
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_MV}
<style>
  {_CSS}
  .wrap {{ position:absolute; inset:170px 100px 140px; display:flex;
       flex-direction:column; justify-content:center; gap:30px; }}
  .kick {{ font-size:22px; letter-spacing:5px; color:{B['rose']}; font-weight:600; }}
  .title {{ font-family:'Bebas Neue',sans-serif; font-size:82px; line-height:1.02; }}
  .title em {{ color:{B['amber']}; font-style:normal; }}
  .hr {{ width:90px; height:3px; background:{B['amber']}; }}
  .items {{ display:flex; flex-direction:column; gap:24px; }}
  .it {{ display:flex; gap:22px; align-items:baseline; }}
  .n {{ font-family:'Bebas Neue',sans-serif; font-size:34px; color:{B['amber']};
       min-width:50px; }}
  .t {{ font-size:36px; font-weight:400; line-height:1.3; }}
</style></head><body>
  {_hdr()}
  <div class="wrap">
    <div class="kick">{escape(kicker)}</div>
    <div class="title">{title}</div>
    <div class="hr"></div>
    <div class="items">{li}</div>
  </div>
  <div class="foot">SAVE THIS · FOLLOW FOR MORE</div>
</body></html>"""
    return _render_html(html, out_path)


def movie_take(text, out_path, kicker="HOT TAKE", emoji="🎬"):
    import re
    body = "<br>".join(
        re.sub(r"\*(.+?)\*", lambda m: f'<span class="hl">{m.group(1)}</span>',
               escape(ln.strip()))
        for ln in text.strip().split("\n"))
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_MV}
<style>
  {_CSS}
  .wrap {{ position:absolute; inset:180px 100px 150px; display:flex;
       flex-direction:column; justify-content:center; align-items:center;
       text-align:center; gap:34px; }}
  .kick {{ font-family:'Bebas Neue',sans-serif; font-size:34px; letter-spacing:6px;
       color:{B['bg2']}; background:{B['amber']}; padding:10px 30px; border-radius:6px; }}
  .emoji {{ font-size:110px; }}
  .txt {{ font-family:'Bebas Neue',sans-serif; font-size:72px; line-height:1.24;
       letter-spacing:.5px; }}
  .hl {{ color:{B['amber']}; }}
  .hr {{ width:110px; height:3px; background:{B['rose']}; }}
</style></head><body>
  {_hdr()}
  <div class="wrap">
    <div class="kick">{escape(kicker)}</div>
    {f'<div class="emoji">{emoji}</div>' if emoji else ''}
    <div class="txt">{body}</div>
    <div class="hr"></div>
  </div>
  <div class="foot">COMMENT YOUR VERDICT</div>
</body></html>"""
    return _render_html(html, out_path)
