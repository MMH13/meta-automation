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


def movie_review_poster(title, year, rating, verdict, line, out_path, genre="",
                        poster_url="", credit="Poster © respective studio · used for review"):
    """Review card with the official poster set inside our branded frame.

    poster_url may be a remote URL (e.g. a TMDB image URL) or a local file path.
    Editorial use for genuine criticism — the poster sits as one panel inside
    original layout and original written commentary, never reposted alone.
    Always keep the `credit` line visible.
    """
    src = poster_url
    if src and not src.startswith(("http://", "https://", "file:")):
        from pathlib import Path
        src = Path(src).resolve().as_uri()
    art = (f'<img class="poster" src="{src}">' if src
           else '<div class="poster ph">POSTER</div>')
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_MV}
<style>
  {_CSS}
  .wrap {{ position:absolute; left:100px; right:100px; top:170px; bottom:150px;
       display:flex; gap:46px; align-items:center; }}
  .poster {{ width:430px; height:645px; object-fit:cover; border-radius:14px;
       box-shadow:0 26px 60px rgba(0,0,0,.62); flex:none;
       border:1px solid rgba(255,255,255,.14); }}
  .ph {{ display:flex; align-items:center; justify-content:center;
       background:linear-gradient(160deg,#2a2145,#15102a); color:{B['mute']};
       font-family:'Bebas Neue',sans-serif; font-size:38px; letter-spacing:6px; }}
  .side {{ flex:1; padding-top:6px; }}
  .kick {{ font-size:22px; letter-spacing:5px; color:{B['rose']}; font-weight:600;
       margin-bottom:14px; }}
  .ttl {{ font-family:'Bebas Neue',sans-serif; font-size:82px; line-height:.94;
       letter-spacing:1px; margin-bottom:14px; }}
  .meta {{ font-size:25px; letter-spacing:2px; color:{B['mute']};
       margin-bottom:26px; }}
  .stars {{ font-size:52px; color:{B['amber']}; letter-spacing:3px; }}
  .num {{ font-size:30px; font-weight:700; margin-left:12px; }}
  .line {{ font-size:30px; line-height:1.5; color:{B['cream']}; opacity:.94;
       margin:26px 0 30px; }}
  .badge {{ display:inline-block; background:{B['amber']}; color:#151020;
       font-family:'Bebas Neue',sans-serif; font-size:33px; letter-spacing:3px;
       padding:13px 30px; border-radius:7px; }}
  .credit {{ position:absolute; bottom:104px; left:0; right:0; text-align:center;
       font-size:17px; color:{B['mute']}; opacity:.6; letter-spacing:1px; }}
</style></head><body>
  {_hdr()}
  <div class="wrap">
    {art}
    <div class="side">
      <div class="kick">THE REVIEW</div>
      <div class="ttl">{escape(str(title)).upper()}</div>
      <div class="meta">{year}{' · ' + escape(genre) if genre else ''}</div>
      <div class="stars">{_stars(rating)}<span class="num">{rating}/5</span></div>
      <div class="line">{escape(line)}</div>
      <div class="badge">{escape(verdict)}</div>
    </div>
  </div>
  <div class="credit">{escape(credit)}</div>
  <div class="foot">FOLLOW FOR DAILY REVIEWS</div>
</body></html>"""
    return _render_html(html, out_path)


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
