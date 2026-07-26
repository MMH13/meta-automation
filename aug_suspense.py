# -*- coding: utf-8 -*-
"""Suspense Ahead — Aug 1-7. 6 posts/day (FB). US/EU audience, English.
Mix: riddle (answer in comment) / 2-line horror text / twist card / spot-it puzzle / sms.
No geo targeting (removed per user)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, when, mkdir, render
from image_suspense import suspense_card, sms_chat

IMG = mkdir("images/aug_suspense")

# kinds:
#  ("card", text, kicker, emoji, caption, first_comment)
#  ("sms", messages, contact, time_label, caption, first_comment)
#  ("text", caption, first_comment_or_None)
DAYS = [
# ---- DAY 1 ----
[
 ("card", "I have cities, but no houses.\nMountains, but no trees.\nWater, but no fish.\n\n*What am I?*", "RIDDLE", "🗺️",
  "🧠 90% get this wrong. Comment your answer before you check the pinned one 👇",
  "🗺️ ANSWER: A map. Did you get it? 😏"),
 ("text", "Two-line horror 👇\n\nI always tuck my daughter in at night.\n\nTonight she whispered, \"Daddy, check the closet — there's another daddy in there.\"\n\n😳 React with 😱 if that got you.",
  None),
 ("card", "A woman is found dead in a locked room.\nThe only clue: a small puddle of water\nand a piece of *rope* hanging from the ceiling.\n\nHow did she die?", "WHODUNIT", "🔍",
  "🕵️ You have all the clues. Solve it in the comments before you look 👇",
  "🔍 ANSWER: She stood on a block of ice to hang herself — it melted, leaving only the puddle. 🧊"),
 ("card", "Find the *odd one* in 10 seconds:\n\n👨‍💼 👨‍💼 👨‍💼 👨‍💼\n👨‍💼 🕵️ 👨‍💼 👨‍💼\n👨‍💼 👨‍💼 👨‍💼 👨‍💼\n\nComment the ROW you spotted it in.", "SPOT IT", "👀",
  "👀 Only sharp eyes catch it fast. Which row? 👇",
  "👀 ANSWER: Row 2. The one looking back at you. 🕵️"),
 ("card", "A man is found hanging in an empty, sealed room,\n10 feet off the ground. No furniture, no ladder —\njust a *puddle* beneath his feet.\n\nHow?", "BRAIN TEASER", "🧊",
  "🕵️ Same trick, new room. Figure out the puddle 👇",
  "🧊 ANSWER: He stood on a block of ice that has since melted. ❄️"),
 ("text", "911 transcript, never explained:\n\nOperator: \"911, what's your emergency?\"\nCaller (whispering): \"He's in the house.\"\nOperator: \"Where are you?\"\nCaller: \"Under the bed.\"\nOperator: \"...ma'am, we traced the call. It's coming from under the bed too.\"\n\n😳 React 😱",
  None),
],
# ---- DAY 2 ----
[
 ("card", "The more you take,\nthe more you leave behind.\n\n*What am I?*", "RIDDLE", "👣",
  "🧠 Simpler than it looks. Answer in the comments before the pin 👇",
  "👣 ANSWER: Footsteps. 🚶"),
 ("text", "Hotel review, 1 star:\n\n\"Clean room, polite staff. But every night at 3:07 AM, the phone rang. Front desk swore no calls were made. On night three, I picked up.\n\nIt was my own voice.\"\n\n😳 Would you check out?",
  None),
 ("card", "A man pushes his car to a hotel\nand loses all his money.\n\n*What happened?*", "BRAIN TEASER", "🎲",
  "🎩 Think carefully. It's not a crime. Comment your guess 👇",
  "🎲 ANSWER: He's playing Monopoly. 🏨"),
 ("sms", [("in", "You up?"), ("out", "yeah, who's this?"), ("in", "It's Mom."),
          ("out", "Mom died last year."), ("in", "I know. Open the door.")],
  "Mom ❤️", "Today 3:04 AM",
  "📱 The last text is why I don't sleep with my phone on. React 😱 👇",
  None),
 ("card", "What has a neck but no head,\ntwo arms but no hands?", "RIDDLE", "👕",
  "🧠 You're probably wearing the answer. Comment it 👇",
  "👕 ANSWER: A shirt. 🧵"),
 ("card", "Find the *different* one — 10 seconds:\n\n🔴 🔴 🔴 🔴 🔴\n🔴 🔴 🔴 🔴 🔴\n🔴 🔴 🟠 🔴 🔴\n\nComment the row.", "SPOT IT", "🟠",
  "👀 Quick — which row breaks the pattern? 👇",
  "🟠 ANSWER: Row 3 — the orange one. 🟠"),
],
# ---- DAY 3 ----
[
 ("card", "What has to be *broken*\nbefore you can use it?", "RIDDLE", "🥚",
  "🧠 Easy one — but say it before you scroll to the pin 👇",
  "🥚 ANSWER: An egg. 🍳"),
 ("card", "A detective walks into a room.\nThe victim is on the floor with a cassette recorder\nin one hand and a gun in the other.\n\nHe presses play: \"I can't go on...\" then a gunshot.\n\nThe detective knows it's *murder*. How?", "WHODUNIT", "🎙️",
  "🕵️ One detail gives it away. Solve it in the comments 👇",
  "🎙️ ANSWER: Someone rewound the tape to the start. A man who just shot himself couldn't have. 🔎"),
 ("text", "Two-line horror 👇\n\nMy smartwatch counts how many people are in the room.\n\nIt's just me at home tonight — but it keeps saying 2.\n\n😳 Drop a 😱 and tag someone brave.",
  None),
 ("card", "Find the *different* one — 10 seconds:\n\n🌚 🌚 🌚 🌚 🌚\n🌚 🌚 🌑 🌚 🌚\n🌚 🌚 🌚 🌚 🌚\n\nComment the row.", "SPOT IT", "🌙",
  "👀 Harder than it looks on a small screen. Which row? 👇",
  "🌙 ANSWER: Row 2 — the one with no face. 🌑"),
 ("sms", [("in", "did you get home ok?"), ("out", "yeah just walked in"),
          ("in", "good. don't turn around."), ("out", "what? why"),
          ("in", "I said don't turn around.")],
  "Unknown", "Today 12:41 AM",
  "📱 Which line made you cold? React 😱 👇",
  None),
 ("card", "I'm always in front of you\nbut can't be seen.\n\n*What am I?*", "RIDDLE", "🔮",
  "🧠 It's right there. Comment your answer 👇",
  "🔮 ANSWER: The future. ⏳"),
],
# ---- DAY 4 ----
[
 ("card", "I speak without a mouth\nand hear without ears.\nI have no body, but I come alive\nwith the *wind*.\n\nWhat am I?", "RIDDLE", "🍃",
  "🧠 A classic. Answer before the pin 👇",
  "🍃 ANSWER: An echo. 🗣️"),
 ("text", "911 transcript, unexplained:\n\nCaller: \"Someone's in my house.\"\nOperator: \"Are you safe?\"\nCaller: \"I'm hiding under the bed.\"\nOperator: \"Officers are 2 minutes away.\"\nCaller: \"...they just whispered, 'they're not coming for you.'\"\n\n😳 React 😱",
  None),
 ("card", "Two men enter a restaurant.\nBoth order the same iced drink.\nOne drinks slowly and lives.\nThe other drinks fast — and *dies*.\n\nWhy?", "BRAIN TEASER", "🧊",
  "🕵️ Same drink, different fate. Figure out why 👇",
  "🧊 ANSWER: The ice was poisoned. The slow drinker's ice didn't melt in time; the fast drinker's did. 🥶"),
 ("card", "Spot the *impostor* — 10 seconds:\n\n😀 😀 😀 😀 😀\n😀 😀 😀 🙂 😀\n😀 😀 😀 😀 😀\n\nWhich row hides the fake smile?", "SPOT IT", "🙂",
  "👀 The fake smile is close. Comment the row 👇",
  "🙂 ANSWER: Row 2 — the one that isn't really happy. 🙂"),
 ("card", "The one who makes it doesn't want it.\nThe one who buys it doesn't need it.\nThe one who uses it can't *feel* it.\n\nWhat is it?", "RIDDLE", "⚰️",
  "🧠 Dark, but famous. Answer in the comments 👇",
  "⚰️ ANSWER: A coffin. 🪦"),
 ("text", "Two-line horror 👇\n\nI got a notification: \"Your photo memories from today.\"\n\nI hadn't taken any photos. It was 14 pictures of me, asleep, from above.\n\n😳 React 😱 and tag someone.",
  None),
],
# ---- DAY 5 ----
[
 ("card", "What can travel around the world\nwhile staying in a *corner*?", "RIDDLE", "📮",
  "🧠 Old-school clever. Say it before the pin 👇",
  "📮 ANSWER: A stamp. ✉️"),
 ("card", "A girl is found alone in a field.\nShe's dry — but *everything around her*\nis soaked with rain.\n\nHow?", "WHODUNIT", "☔",
  "🕵️ The answer is simpler than you think. Comment your solve 👇",
  "☔ ANSWER: She was carried there after the rain — or arrived under cover. The 'dry victim' is the whole clue. 🌧️"),
 ("text", "Two-line horror 👇\n\nMy toddler keeps giggling at the baby monitor and waving.\n\nHer crib is in the same room as us tonight — the monitor's been unplugged for a week.\n\n😳 Sleep well.",
  None),
 ("sms", [("in", "are you home?"), ("out", "yeah why"), ("in", "lock your door"),
          ("out", "why?? you're scaring me"), ("in", "because I'm already inside")],
  "Unknown", "Today 11:58 PM",
  "📱 Which text made your stomach drop? React 😱 👇",
  None),
 ("card", "A murderer is sentenced to death.\nHe must choose one of three rooms:\none full of fire, one with assassins,\none with lions that haven't eaten in 3 years.\n\nWhich room is *safe*?", "BRAIN TEASER", "🦁",
  "🕵️ Only one keeps him alive. Which room, and why? 👇",
  "🦁 ANSWER: The lions' room — after 3 years without food, they'd be long dead. 💀"),
 ("card", "Spot the *odd symbol* — 10 seconds:\n\n⭐ ⭐ ⭐ ⭐ ⭐\n⭐ ⭐ ⭐ ⭐ ⭐\n⭐ ⭐ ⭐ ✨ ⭐\n\nComment the row.", "SPOT IT", "✨",
  "👀 Quick eyes only. Which row? 👇",
  "✨ ANSWER: Row 3 — the sparkle, not the star. ✨"),
],
# ---- DAY 6 ----
[
 ("card", "The person who makes it, sells it.\nThe person who buys it, never uses it.\nThe person who uses it, never *knows* they are.\n\nWhat is it?", "RIDDLE", "⚰️",
  "🧠 Dark but famous. Answer in the comments 👇",
  "⚰️ ANSWER: A coffin. 🪦"),
 ("card", "A man lives on the 20th floor.\nEvery morning he takes the elevator down.\nComing home, he rides to the 10th floor,\nthen takes the *stairs* — except when it rains.\n\nWhy?", "BRAIN TEASER", "🛗",
  "🕵️ The classic. If you know it, don't spoil it — let others guess 👇",
  "🛗 ANSWER: He's short and can only reach the 10th-floor button — unless he has an umbrella to press the 20th. ☔"),
 ("text", "Two-line horror 👇\n\nI live alone, so I set two plates out sometimes just to feel less lonely.\n\nLast night, both plates were empty in the morning.\n\n😳 React 😱 if you'd move out.",
  None),
 ("card", "Find the *odd symbol* — 10 seconds:\n\n♠️ ♠️ ♠️ ♠️ ♠️\n♠️ ♠️ ♠️ ♠️ ♣️\n♠️ ♠️ ♠️ ♠️ ♠️\n\nComment the row.", "SPOT IT", "♠️",
  "👀 Quick — which row breaks the pattern? 👇",
  "♠️ ANSWER: Row 2 — the club at the end. ♣️"),
 ("sms", [("in", "babe I'm outside, come down"), ("out", "you're sweet but I'm at my mom's tonight"),
          ("in", "no you're not. I can see you in the window."), ("out", "...I'm 200 miles away")],
  "❤️", "Today 10:12 PM",
  "📱 So who's at the window? React 😱 👇",
  None),
 ("card", "What gets *wetter*\nthe more it dries?", "RIDDLE", "🧺",
  "🧠 Simple but sneaky. Comment your answer 👇",
  "🧺 ANSWER: A towel. 🚿"),
],
# ---- DAY 7 ----
[
 ("card", "I'm tall when I'm young\nand short when I'm old.\n\n*What am I?*", "RIDDLE", "🕯️",
  "🧠 Nice and simple. Answer before the pin 👇",
  "🕯️ ANSWER: A candle. 🔥"),
 ("card", "A body is found at the bottom of a tall building.\nThe detective checks each floor, opening every window,\ndropping a coin from each. Back down, she declares\nit a *suicide, not murder*. How did she know?", "WHODUNIT", "🏢",
  "🕵️ Think about the windows. Solve it 👇",
  "🏢 ANSWER: Every window was locked from the inside — no one could have pushed him and re-locked it. 🔒"),
 ("text", "Chill of the week 👇\n\nMy phone's photo app made a 'memories' video titled *'You & Him ❤️'*.\n\nEvery photo was of me sleeping. I live alone.\n\n😳 React 😱 and tag someone who needs to lose sleep tonight.",
  None),
 ("card", "Spot the *fake* — 10 seconds:\n\n🔒 🔒 🔒 🔒 🔒\n🔒 🔓 🔒 🔒 🔒\n🔒 🔒 🔒 🔒 🔒\n\nWhich row is unlocked?", "SPOT IT", "🔓",
  "👀 One door is open. Which row? 👇",
  "🔓 ANSWER: Row 2 — the unlocked one. Hope it wasn't yours. 🔓"),
 ("card", "Forward I'm heavy, but backward I'm not.\n\n*What am I?*", "RIDDLE", "🎣",
  "🧠 Read it literally. Comment your answer 👇",
  "🎣 ANSWER: The word 'ton' — backward it's 'not.' 🔤"),
 ("text", "Last two-line horror of the week 👇\n\nEvery night my dog barks at the empty hallway.\n\nTonight he came and hid behind me — and something in the hallway kept barking back.\n\n😳 React 😱. Sleep tight.",
  None),
],
]

HOURS = [10, 13, 16, 19, 21, 23]  # UTC — 6 slots across US/EU day & evening


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n_img = 0
    for di, day in enumerate(DAYS):
        for pi, entry in enumerate(day):
            kind = entry[0]
            ts = when(di, HOURS[pi])
            iid = f"asu-d{di+1}-{pi+1}"
            if iid in have:
                continue  # resume: already enqueued
            if kind == "text":
                _, caption, fc = entry
                it = {"id": iid, "account": "suspense-ahead", "network": "facebook",
                      "type": "text", "message": caption, "when": ts, "status": "pending"}
                if fc:
                    it["first_comment"] = fc
                items.append(it)
                continue
            img_path = f"{IMG}/d{di+1}_{pi+1}.png"
            if kind == "card":
                _, text, kicker, emoji, caption, fc = entry
                render(suspense_card, text, img_path, kicker=kicker, emoji=emoji)
            elif kind == "sms":
                _, msgs, contact, tlabel, caption, fc = entry
                render(sms_chat, msgs, img_path, contact=contact, time_label=tlabel)
            n_img += 1
            print(f"  rendered {img_path}")
            it = {"id": iid, "account": "suspense-ahead", "network": "facebook",
                  "type": "photo", "message": caption, "image_url": img_path,
                  "when": ts, "status": "pending"}
            if fc:
                it["first_comment"] = fc
            items.append(it)
    save(q)
    print(f"SUSPENSE AHEAD: rendered {n_img} images, queue now {len(items)} items")


if __name__ == "__main__":
    build()
