# -*- coding: utf-8 -*-
"""Style Spotlight — editorial fashion templates (cream / charcoal / gold).

Deliberately distinct from the other pages' brands (Health=green, Deshal=teal+yellow,
Suspense=dark+red, Mamun=navy+cyan). Editorial magazine feel: serif display,
generous whitespace, thin rules, small-caps kicker.

All content is ORIGINAL text on branded graphics — no photos of real people
(no rights/copyright exposure, and it stays monetization-eligible).

  style_card(kicker, title, points, ...)   -> editorial list card
  style_this_that(label_a, a, label_b, b)  -> "which would you pick" card
  style_myth(myth, fact)                   -> style myth vs truth
"""

from html import escape

from image_html import _render_html, W, H

_FONTS_ED = ('<link href="https://fonts.googleapis.com/css2?'
             'family=Playfair+Display:ital,wght@0,500;0,700;0,800;1,500&'
             'family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">')

BRAND = {
    "cream": "#f8f3ef",
    "ink":   "#26221f",
    "gold":  "#b8935f",
    "rose":  "#c9797d",
    "mute":  "#8a807a",
}
B = BRAND


def _hdr(page="STYLE SPOTLIGHT"):
    return f"""
  <div class="hdr">
    <div class="rule"></div>
    <div class="pname">{escape(page)}</div>
    <div class="rule"></div>
  </div>"""


_CSS_BASE = f"""
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background:{B['cream']}; font-family:'Jost',sans-serif; color:{B['ink']}; }}
  .frame {{ position:absolute; inset:38px; border:2px solid {B['gold']}; opacity:.35; }}
  .hdr {{ position:absolute; top:78px; left:90px; right:90px; display:flex;
       align-items:center; gap:20px; }}
  .hdr .rule {{ flex:1; height:1px; background:{B['gold']}; opacity:.7; }}
  .pname {{ font-size:26px; font-weight:500; letter-spacing:7px; color:{B['gold']}; }}
  .foot {{ position:absolute; bottom:76px; left:0; right:0; text-align:center;
       font-size:24px; font-weight:400; letter-spacing:3px; color:{B['mute']}; }}
"""


def style_card(title, points, out_path, kicker="STYLE RULES", emoji=""):
    """Editorial list card. points = list of short strings."""
    items = "\n".join(
        f'<div class="pt"><span class="n">{i+1:02d}</span>'
        f'<span class="t">{escape(p)}</span></div>'
        for i, p in enumerate(points))
    hero = f'<div class="emoji">{emoji}</div>' if emoji else ""
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_ED}
<style>
  {_CSS_BASE}
  .wrap {{ position:absolute; inset:170px 90px 150px; display:flex;
       flex-direction:column; justify-content:center; gap:34px; }}
  .kick {{ font-size:24px; letter-spacing:5px; color:{B['rose']}; font-weight:500; }}
  .emoji {{ font-size:74px; }}
  .title {{ font-family:'Playfair Display',serif; font-weight:800; font-size:76px;
       line-height:1.14; }}
  .title em {{ font-style:italic; color:{B['gold']}; }}
  .hr {{ width:90px; height:3px; background:{B['gold']}; }}
  .pts {{ display:flex; flex-direction:column; gap:26px; margin-top:6px; }}
  .pt {{ display:flex; gap:22px; align-items:baseline; }}
  .n {{ font-family:'Playfair Display',serif; font-size:34px; color:{B['gold']};
       font-weight:700; min-width:56px; }}
  .t {{ font-size:38px; font-weight:400; line-height:1.34; }}
</style></head><body>
  <div class="frame"></div>{_hdr()}
  <div class="wrap">
    <div class="kick">{escape(kicker)}</div>
    {hero}
    <div class="title">{title}</div>
    <div class="hr"></div>
    <div class="pts">{items}</div>
  </div>
  <div class="foot">FOLLOW FOR DAILY STYLE</div>
</body></html>"""
    return _render_html(html, out_path)


def style_this_that(label_a, text_a, label_b, text_b, out_path,
                    question="WHICH WOULD YOU PICK?"):
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_ED}
<style>
  {_CSS_BASE}
  .q {{ position:absolute; top:180px; left:90px; right:90px; text-align:center;
       font-family:'Playfair Display',serif; font-size:56px; font-weight:700; }}
  .opt {{ position:absolute; left:90px; right:90px; height:400px;
       display:flex; flex-direction:column; justify-content:center; gap:16px;
       padding:44px 50px; }}
  .a {{ top:300px; background:#fff; border:2px solid {B['gold']}; }}
  .b {{ bottom:180px; background:{B['ink']}; color:{B['cream']}; }}
  .lab {{ font-family:'Playfair Display',serif; font-size:44px; font-weight:800; }}
  .a .lab {{ color:{B['gold']}; }}
  .b .lab {{ color:{B['gold']}; }}
  .tx {{ font-size:34px; font-weight:400; line-height:1.35; }}
  .or {{ position:absolute; top:735px; left:50%; transform:translate(-50%,-50%);
       width:92px; height:92px; border-radius:50%; background:{B['rose']};
       color:#fff; display:flex; align-items:center; justify-content:center;
       font-family:'Playfair Display',serif; font-size:32px; font-weight:700;
       z-index:5; letter-spacing:1px; }}
</style></head><body>
  <div class="frame"></div>{_hdr()}
  <div class="q">{escape(question)}</div>
  <div class="opt a"><div class="lab">{escape(label_a)}</div>
    <div class="tx">{escape(text_a)}</div></div>
  <div class="or">OR</div>
  <div class="opt b"><div class="lab">{escape(label_b)}</div>
    <div class="tx">{escape(text_b)}</div></div>
  <div class="foot">COMMENT YOUR PICK</div>
</body></html>"""
    return _render_html(html, out_path)


def style_myth(myth, truth, out_path):
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_ED}
<style>
  {_CSS_BASE}
  .panel {{ position:absolute; left:90px; right:90px; padding:44px 48px;
       display:flex; flex-direction:column; gap:18px; }}
  .m {{ top:200px; min-height:380px; background:#fff;
       border-left:6px solid {B['rose']}; }}
  .t {{ bottom:180px; min-height:420px; background:{B['ink']};
       border-left:6px solid {B['gold']}; color:{B['cream']}; }}
  .tag {{ font-size:24px; letter-spacing:5px; font-weight:500; }}
  .m .tag {{ color:{B['rose']}; }}
  .t .tag {{ color:{B['gold']}; }}
  .body {{ font-family:'Playfair Display',serif; font-size:42px; font-weight:500;
       line-height:1.32; }}
  .m .body {{ font-style:italic; }}
</style></head><body>
  <div class="frame"></div>{_hdr()}
  <div class="panel m"><div class="tag">THE MYTH</div>
    <div class="body">"{escape(myth)}"</div></div>
  <div class="panel t"><div class="tag">THE TRUTH</div>
    <div class="body">{escape(truth)}</div></div>
  <div class="foot">FOLLOW FOR DAILY STYLE</div>
</body></html>"""
    return _render_html(html, out_path)
