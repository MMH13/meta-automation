# -*- coding: utf-8 -*-
"""Suspense Ahead image templates — dark cinematic cards + SMS chat stories.

suspense_card(): kicker label ("DETECTIVE RIDDLE"), big text with *red highlights*,
film-grain dark background, red accent bar, SUSPENSE AHEAD footer.
sms_chat(): iPhone-Messages-style fictional chat story, dark mode.
"""

from html import escape

from image_html import _render_html, W, H, _lines_html

_FONTS_SUS = ('<link href="https://fonts.googleapis.com/css2?'
              'family=Oswald:wght@500;600;700&family=Poppins:wght@400;500;600'
              '&display=swap" rel="stylesheet">')

_GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
          "width='260' height='260'%3E%3Cfilter id='n'%3E%3CfeTurbulence "
          "baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/%3E%3C"
          "feColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.05 0'/%3E"
          "%3C/filter%3E%3Crect width='260' height='260' filter='url(%23n)'/%3E%3C/svg%3E\")")


def suspense_card(text: str, out_path: str, kicker: str = "SUSPENSE AHEAD",
                  emoji: str = "", footer: str = "SUSPENSE AHEAD") -> str:
    hero = (f'<div class="hero">{emoji}</div>' if emoji else "")
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_SUS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: radial-gradient(130% 100% at 50% 0%, #1c1f26 0%, #0d0f14 55%, #060708 100%);
       font-family:'Poppins',sans-serif; }}
  .grain {{ position:absolute; inset:0; opacity:.5; background-image:{_GRAIN}; }}
  .glow {{ position:absolute; width:900px; height:420px; left:90px; top:-190px;
       background:radial-gradient(closest-side, rgba(190,30,45,.22), transparent);
       filter:blur(10px); }}
  .vig {{ position:absolute; inset:0;
       background: radial-gradient(85% 80% at 50% 45%, transparent 55%, rgba(0,0,0,.75) 100%); }}
  .wrap {{ position:absolute; inset:100px 90px 130px; display:flex;
       flex-direction:column; justify-content:center; align-items:center;
       text-align:center; gap:36px; }}
  .kicker {{ font-family:'Oswald',sans-serif; font-size:34px; font-weight:600;
       letter-spacing:8px; color:#e33b4e; text-transform:uppercase; }}
  .kicker::before, .kicker::after {{ content:"—"; color:#5a5f6b; margin:0 18px; }}
  .hero {{ font-size:120px; filter:drop-shadow(0 10px 30px rgba(227,59,78,.35)); }}
  .content {{ font-family:'Oswald',sans-serif; font-weight:500; color:#eceef2; }}
  .line {{ font-size:64px; line-height:1.42; }}
  .line .hl {{ color:#e33b4e; font-weight:700; }}
  .gap {{ height:26px; }}
  .bar {{ width:130px; height:6px; background:#e33b4e; border-radius:3px; }}
  .footer {{ position:absolute; bottom:56px; width:100%; text-align:center;
       font-family:'Oswald',sans-serif; font-size:30px; font-weight:600;
       letter-spacing:6px; color:rgba(210,215,225,.55); }}
</style></head><body>
  <div class="glow"></div><div class="grain"></div><div class="vig"></div>
  <div class="wrap">
    <div class="kicker">{escape(kicker)}</div>
    {hero}
    <div class="content">{_lines_html(text)}</div>
    <div class="bar"></div>
  </div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""
    return _render_html(html, out_path)


def sms_chat(messages, out_path: str, contact: str = "Unknown",
             time_label: str = "Today 11:58 PM",
             footer: str = "SUSPENSE AHEAD") -> str:
    """messages: list of (side, text) where side is 'in' (grey, left) or
    'out' (blue, right). Renders an iPhone-Messages-style dark chat."""
    bubbles = f'<div class="tstamp">{escape(time_label)}</div>'
    for side, text in messages:
        t = escape(text).replace("\n", "<br>")
        bubbles += f'<div class="msg {side}"><span>{t}</span></div>'
    html = f"""<!doctype html><html><head><meta charset="utf-8">{_FONTS_SUS}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{W}px; height:{H}px; overflow:hidden; position:relative;
       background: radial-gradient(130% 100% at 50% 0%, #17191f 0%, #0a0b0e 60%);
       font-family:'Poppins',sans-serif; }}
  .grain {{ position:absolute; inset:0; opacity:.45; background-image:{_GRAIN}; }}
  .phone {{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
       width:780px; height:1140px; background:#000; border-radius:54px;
       box-shadow: 0 46px 100px rgba(0,0,0,.8), 0 0 0 14px #101013,
                   0 0 0 16px rgba(255,255,255,.07), 0 0 90px rgba(227,59,78,.12);
       overflow:hidden; display:flex; flex-direction:column; }}
  .head {{ padding:30px 30px 20px; text-align:center; background:#101013;
       border-bottom:1px solid rgba(255,255,255,.08); }}
  .avatar {{ width:82px; height:82px; border-radius:50%; margin:0 auto 10px;
       background:linear-gradient(160deg,#3a3f4a,#23262e); display:flex;
       align-items:center; justify-content:center; font-size:40px; color:#9aa0ad;
       font-weight:600; }}
  .cname {{ color:#f2f3f5; font-size:30px; font-weight:600; }}
  .csub {{ color:#8a8f9a; font-size:20px; margin-top:2px; }}
  .chat {{ flex:1; padding:34px 30px; display:flex; flex-direction:column;
       gap:18px; overflow:hidden; }}
  .tstamp {{ text-align:center; color:#70757f; font-size:20px; margin-bottom:6px; }}
  .msg {{ max-width:78%; padding:20px 26px; border-radius:30px; font-size:29px;
       line-height:1.45; }}
  .msg.in {{ align-self:flex-start; background:#26282e; color:#eceef2;
       border-bottom-left-radius:8px; }}
  .msg.out {{ align-self:flex-end; background:#0a84ff; color:#fff;
       border-bottom-right-radius:8px; }}
  .footer {{ position:absolute; bottom:34px; width:100%; text-align:center;
       font-family:'Oswald',sans-serif; font-size:28px; font-weight:600;
       letter-spacing:6px; color:rgba(210,215,225,.5); }}
</style></head><body>
  <div class="grain"></div>
  <div class="phone">
    <div class="head"><div class="avatar">?</div>
      <div class="cname">{escape(contact)}</div>
      <div class="csub">Messages</div></div>
    <div class="chat">{bubbles}</div>
  </div>
  <div class="footer">{escape(footer)}</div>
</body></html>"""
    return _render_html(html, out_path)
