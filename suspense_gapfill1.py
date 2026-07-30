# -*- coding: utf-8 -*-
"""Suspense Ahead — emergency gap-fill. The queue had nothing scheduled from
Jul 29 21:08 (last actual post) through Aug 1 10:00 - a ~37hr hole between two
older batches. This closes it with 8 fresh items (none repeat anything in the
Aug 1-7 batch already queued) at the page's usual 6/day rhythm."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_suspense import suspense_card, sms_chat

IMG = mkdir("images/suspense_gap1")

# (kind, args, caption, first_comment_or_None, when)
POSTS = [
 ("card", dict(text="I have keys but no locks.\nSpace but no room.\nYou can enter, but never leave.\n\n*What am I?*",
               kicker="RIDDLE", emoji="⌨️"),
  "🧠 Simple once you see it. Answer before the pin 👇", "⌨️ ANSWER: A keyboard.", "2026-07-30T21:00:00+00:00"),

 ("card", dict(text="A man is found dead in the desert,\nholding a burnt match.\nNothing else around him for miles.\n\nHow did he die?", kicker="WHODUNIT", emoji="🏜️"),
  "🕵️ Nothing else on the scene. Solve it 👇", "🏜️ ANSWER: He jumped from a hot air balloon after it caught fire — the match was to see how much fuel he had left. 🎈",
  "2026-07-30T23:00:00+00:00"),

 ("text", None,
  "Two-line horror 👇\n\nMy smart speaker just said good morning to me.\n\nI never set up a wake word, and I don't own a smart speaker.\n\n😳 React 😱 if that got you.",
  None, "2026-07-31T10:00:00+00:00"),

 ("card", dict(text="Spot the *odd one* — 10 seconds:\n\n👻 👻 👻 👻 👻\n👻 👻 🎃 👻 👻\n👻 👻 👻 👻 👻",
               kicker="SPOT IT", emoji="👀"),
  "👀 Quick — which row? 👇", "🎃 ANSWER: Row 2.", "2026-07-31T13:00:00+00:00"),

 ("sms", dict(messages=[("in", "did you let the dog out?"), ("out", "no, I'm not even home yet"),
                        ("in", "then who's been walking past my window all night")],
              contact="Roommate", time_label="Today 2:14 AM"),
  "📱 Which line got you? React 😱 👇", None, "2026-07-31T16:00:00+00:00"),

 ("card", dict(text="The more you remove,\nthe bigger I get.\n\n*What am I?*", kicker="RIDDLE", emoji="🕳️"),
  "🧠 Comment your answer before the pin 👇", "🕳️ ANSWER: A hole.", "2026-07-31T19:00:00+00:00"),

 ("card", dict(text="Two brothers race each other home.\nThe loser's horse wins the family fortune.\nA stranger whispers one sentence to the slower brother's rider.\n\nBoth horses take off at full speed. What did the stranger say?",
               kicker="BRAIN TEASER", emoji="🐎"),
  "🕵️ One sentence flips the whole race. Solve it 👇",
  "🐎 ANSWER: \"Switch horses.\" Each brother then races the OTHER horse as fast as possible to make his own horse (which determines the loser) finish last.",
  "2026-07-31T21:00:00+00:00"),

 ("text", None,
  "Two-line horror 👇\n\nI keep hearing my name called from the kitchen when I'm the only one home.\n\nTonight it said please, for the first time.\n\n😳 Tag someone who wouldn't check.",
  None, "2026-07-31T23:00:00+00:00"),
]

assert len(POSTS) == 8


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n = 0
    for idx, (kind, args, caption, fc, when) in enumerate(POSTS, 1):
        iid = f"asu-gap1-{idx}"
        if iid in have:
            continue
        if kind == "text":
            it = {"id": iid, "account": "suspense-ahead", "network": "facebook",
                  "type": "text", "message": caption, "when": when, "status": "pending"}
        else:
            img = f"{IMG}/{idx}.png"
            fn = suspense_card if kind == "card" else sms_chat
            render(fn, out_path=img, **args)
            it = {"id": iid, "account": "suspense-ahead", "network": "facebook",
                  "type": "photo", "message": caption, "image_url": img,
                  "when": when, "status": "pending"}
        if fc:
            it["first_comment"] = fc
        items.append(it)
        n += 1
        print(f"  {iid} -> {when}")
    save(q)
    print(f"queued {n} gap-fill items, total {len(items)}")


if __name__ == "__main__":
    build()
