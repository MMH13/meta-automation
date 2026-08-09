# -*- coding: utf-8 -*-
"""Suspense Ahead — 30-day card queue refill, 6/day (2026-08-10 -> 2026-09-08),
continuing right after the card queue's Aug 7 tail (separate from the video/
reel content, which is built and published directly, not through this
queue). Same rotation as suspense_gapfill1.py: riddle, whodunit, 2-line
horror, spot-it, sms-horror, brain-teaser. 60 unique items across 6 pools,
cycled across 180 slots — each repeats 3x over the month. All original."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from datetime import date, timedelta

from aug_common import load, save, mkdir, render
from image_suspense import suspense_card, sms_chat

IMG = mkdir("images/suspense_refill1")

# ---------------------------------------------------------------- riddles
# (text, emoji, caption, answer)
RIDDLES = [
 ("I have cities, but no houses.\nI have mountains, but no trees.\nI have water, but no fish.\n\n*What am I?*", "🗺️",
  "🧠 Simple once you see it. Answer before the pin 👇", "🗺️ ANSWER: A map."),
 ("The more you take,\nthe more you leave behind.\n\n*What am I?*", "👣",
  "🧠 Comment your answer before the pin 👇", "👣 ANSWER: Footsteps."),
 ("I'm light as a feather,\nyet the strongest person\ncan't hold me more than a few minutes.\n\n*What am I?*", "💨",
  "🧠 Everyone's holding one right now. Answer 👇", "💨 ANSWER: Your breath."),
 ("I have a neck but no head.\nI have a body but no legs.\n\n*What am I?*", "🍾",
  "🧠 Look around your kitchen. Answer 👇", "🍾 ANSWER: A bottle."),
 ("The more of me there is,\nthe less you see.\n\n*What am I?*", "🌑",
  "🧠 Comment before the pin 👇", "🌑 ANSWER: Darkness."),
 ("I'm always in front of you,\nbut you can never see me.\n\n*What am I?*", "⏳",
  "🧠 Simple once you see it. Answer 👇", "⏳ ANSWER: The future."),
 ("I go up,\nbut I never come down.\n\n*What am I?*", "🎂",
  "🧠 Happens to all of us. Answer 👇", "🎂 ANSWER: Your age."),
 ("I have no voice,\nyet I speak to you.\nI tell of the world's events.\n\n*What am I?*", "📰",
  "🧠 Comment your answer before the pin 👇", "📰 ANSWER: A newspaper."),
 ("Feed me and I live.\nGive me water and I die.\n\n*What am I?*", "🔥",
  "🧠 Classic one. Answer before the pin 👇", "🔥 ANSWER: Fire."),
 ("I have branches,\nbut no fruit, trunk, or leaves.\n\n*What am I?*", "🏦",
  "🧠 Think finance, not forest. Answer 👇", "🏦 ANSWER: A bank."),
]

# --------------------------------------------------------------- whodunit
# (text, emoji, caption, answer)
WHODUNIT = [
 ("A woman is found dead in a locked room\nwith a puddle of water and broken glass.\nNo windows were open.\n\nHow did she die?", "🚪",
  "🕵️ Nothing else in the room. Solve it 👇",
  "🚪 ANSWER: She hanged herself standing on a block of ice, which melted into the 'puddle.' The broken glass was from a light fixture she kicked."),
 ("A man walks into a bar and asks for a glass of water.\nThe bartender pulls out a gun and points it at him.\nThe man says thank you and leaves.\n\nWhy?", "🔫",
  "🕵️ No one got hurt. Figure out why 👇",
  "🔫 ANSWER: The man had hiccups and wanted water to cure them. Scaring him worked faster."),
 ("Two bodies are found in a cabin,\nsurrounded by broken glass and water,\nwith no signs of forced entry.\n\nWhat happened?", "🐠",
  "🕵️ The 'cabin' is the key detail. Solve it 👇",
  "🐠 ANSWER: They were fish — the 'cabin' was an aquarium tank that shattered."),
 ("A man is found dead in a field\nwith an unopened package next to him.\n\nHow did he die?", "🪂",
  "🕵️ Nothing else on the scene. Solve it 👇",
  "🪂 ANSWER: He was skydiving and his parachute — the unopened package — failed."),
 ("A woman shoots her husband.\nThen holds him underwater for 5 minutes.\nFinally, she hangs him.\n\nMinutes later they have dinner together. How?", "📷",
  "🕵️ Nobody got hurt. Figure it out 👇",
  "📷 ANSWER: She's a photographer — she shot a photo, developed it in water, then hung it to dry."),
 ("A man is found dead in his office\non the 25th floor. A note reads\n'I can't do this anymore.' The window is open.\n\nWas it suicide?", "🏢",
  "🕵️ One detail rules it out. Solve it 👇",
  "🏢 ANSWER: No — the window only opens 4 inches, too small to fit through. He was murdered and the scene staged."),
 ("A truck driver is going the wrong way\ndown a one-way street.\nA police officer watches and says nothing.\n\nWhy?", "🚶",
  "🕵️ The job title is a clue. Solve it 👇",
  "🚶 ANSWER: He was walking, not driving."),
 ("A man dies of thirst in his own home,\nwith a fully stocked kitchen\nand running water.\n\nHow?", "🐟",
  "🕵️ Think small. Solve it 👇",
  "🐟 ANSWER: He was a goldfish — his bowl had run dry."),
 ("A body is found in the desert\nwith a burnt matchstick in his hand.\nNothing else for miles.\n\nHow did he die?", "🎈",
  "🕵️ Look up, not around. Solve it 👇",
  "🎈 ANSWER: He jumped from a hot air balloon on fire after checking how much fuel was left with the match."),
 ("A woman calls police: 'My husband is dead,\nI found him in the bath.'\nThey arrest her immediately.\n\nHow did they know?", "🛁",
  "🕵️ One detail gave her away. Solve it 👇",
  "🛁 ANSWER: The bathroom light was broken — pitch black. She couldn't have 'found' him unless she was already in there when it happened."),
]

# ---------------------------------------------------------------- 2-line
TWO_LINE = [
 "Two-line horror 👇\n\nMy smart speaker just said good morning to me.\n\nI never set up a wake word, and I don't own a smart speaker.\n\n😳 React 😱 if that got you.",
 "Two-line horror 👇\n\nI keep hearing my name called from the kitchen when I'm the only one home.\n\nTonight it said please, for the first time.\n\n😳 Tag someone who wouldn't check.",
 "Two-line horror 👇\n\nMy reflection waved at me before I raised my hand.\n\nI haven't looked in a mirror since.\n\n😳 React 😱 if that got you.",
 "Two-line horror 👇\n\nI found a photo of myself sleeping on my phone.\n\nI don't remember taking it, and I sleep alone.\n\n😳 Tag someone who checks their camera roll now.",
 "Two-line horror 👇\n\nMy dog won't stop staring at the empty chair across the room.\n\nWe don't have an empty chair.\n\n😳 React 😱 if that got you.",
 "Two-line horror 👇\n\nI got a text from my mother today.\n\nShe passed away three years ago.\n\n😳 Tag someone who'd call the number back.",
 "Two-line horror 👇\n\nThe nightlight in my daughter's room turns off every night at exactly 3 AM.\n\nWe don't have a timer on it.\n\n😳 React 😱 if that got you.",
 "Two-line horror 👇\n\nI heard someone whisper my name as I fell asleep.\n\nIt sounded exactly like my own voice.\n\n😳 Tag someone who won't sleep tonight.",
 "Two-line horror 👇\n\nMy houseplants have started leaning toward the hallway closet instead of the window.\n\nI haven't opened that closet in years.\n\n😳 React 😱 if that got you.",
 "Two-line horror 👇\n\nI woke up with my bedroom door locked from the inside.\n\nI don't own a key that fits it.\n\n😳 Tag someone who checks their locks now.",
]

# --------------------------------------------------------------- spot-it
# (grid_text, emoji, caption, answer)
SPOT_IT = [
 ("Spot the *odd one* — 10 seconds:\n\n👻 👻 👻 👻 👻\n👻 👻 🎃 👻 👻\n👻 👻 👻 👻 👻", "👀",
  "👀 Quick — which row? 👇", "🎃 ANSWER: Row 2."),
 ("Spot the *odd one* — 10 seconds:\n\n💀 💀 💀 💀 💀\n💀 💀 💀 💀 💀\n💀 ☠️ 💀 💀 💀", "👀",
  "👀 Quick — which row? 👇", "☠️ ANSWER: Row 3."),
 ("Spot the *odd one* — 10 seconds:\n\n🕷️ 🕷️ 🕷️ 🕷️ 🕷️\n🕷️ 🕷️ 🕸️ 🕷️ 🕷️\n🕷️ 🕷️ 🕷️ 🕷️ 🕷️", "👀",
  "👀 Quick — which row? 👇", "🕸️ ANSWER: Row 2."),
 ("Spot the *odd one* — 10 seconds:\n\n👁️ 👁️ 👁️ 👁️ 👁️\n👁️ 👁️ 👁️ 👁️ 👁️\n👁️ 👁️ 👁️ 🫣 👁️", "👀",
  "👀 Quick — which row? 👇", "🫣 ANSWER: Row 3."),
 ("Spot the *odd one* — 10 seconds:\n\n🔪 🔪 🔪 🔪 🔪\n🔪 🩸 🔪 🔪 🔪\n🔪 🔪 🔪 🔪 🔪", "👀",
  "👀 Quick — which row? 👇", "🩸 ANSWER: Row 2."),
 ("Spot the *odd one* — 10 seconds:\n\n🦇 🦇 🦇 🦇 🦇\n🦇 🦇 🦇 🦇 🦇\n🦇 🦇 🐦‍⬛ 🦇 🦇", "👀",
  "👀 Quick — which row? 👇", "🐦‍⬛ ANSWER: Row 3."),
 ("Spot the *odd one* — 10 seconds:\n\n🕯️ 🕯️ 🕯️ 🕯️ 🕯️\n🕯️ 🕯️ 🕯️ 🖤 🕯️\n🕯️ 🕯️ 🕯️ 🕯️ 🕯️", "👀",
  "👀 Quick — which row? 👇", "🖤 ANSWER: Row 2."),
 ("Spot the *odd one* — 10 seconds:\n\n🎭 🎭 🎭 🎭 🎭\n🎭 🎭 🎭 🎭 🎭\n🎭 😶 🎭 🎭 🎭", "👀",
  "👀 Quick — which row? 👇", "😶 ANSWER: Row 3."),
 ("Spot the *odd one* — 10 seconds:\n\n🐦‍⬛ 🐦‍⬛ 🐦‍⬛ 🐦‍⬛ 🐦‍⬛\n🐦‍⬛ 🐦‍⬛ 🦉 🐦‍⬛ 🐦‍⬛\n🐦‍⬛ 🐦‍⬛ 🐦‍⬛ 🐦‍⬛ 🐦‍⬛", "👀",
  "👀 Quick — which row? 👇", "🦉 ANSWER: Row 2."),
 ("Spot the *odd one* — 10 seconds:\n\n🌙 🌙 🌙 🌙 🌙\n🌙 🌙 🌙 🌙 🌙\n🌙 🌚 🌙 🌙 🌙", "👀",
  "👀 Quick — which row? 👇", "🌚 ANSWER: Row 3."),
]

# ------------------------------------------------------------ sms-horror
# (messages, contact, time_label, caption)
SMS_HORROR = [
 ([("in", "did you let the dog out?"), ("out", "no, I'm not even home yet"),
   ("in", "then who's been walking past my window all night")], "Roommate", "Today 2:14 AM",
  "📱 Which line got you? React 😱 👇"),
 ([("in", "are you still awake?"), ("out", "yeah what's up"),
   ("in", "good. don't come downstairs tonight, ok?")], "Mom", "Today 11:47 PM",
  "📱 That reply though. React 😱 👇"),
 ([("in", "wrong number, sorry"), ("out", "who is this"),
   ("in", "i said sorry. go back to sleep. i can see you")], "Unknown", "Today 3:03 AM",
  "📱 Would you have replied? React 😱 👇"),
 ([("in", "is the babysitter still there?"), ("out", "yeah why"),
   ("in", "we don't have a babysitter tonight")], "Sister", "Today 1:12 AM",
  "📱 Which line got you? React 😱 👇"),
 ([("in", "just a heads up, unit 4B has been vacant for 3 years"), ("out", "i live in 4B"),
   ("in", "i know. that's why i'm texting.")], "Landlord", "Today 9:58 PM",
  "📱 Would you move out tonight? React 😱 👇"),
 ([("in", "i left the package at your door"), ("out", "i didn't order anything"),
   ("in", "someone did. it has your name on it. and today's date.")], "Delivery Driver", "Today 11:30 PM",
  "📱 Would you open the door? React 😱 👇"),
 ([("in", "why did you just call me from your landline"), ("out", "i don't have a landline"),
   ("in", "then who just answered when i called back")], "Best Friend", "Today 2:47 AM",
  "📱 Which line got you? React 😱 👇"),
 ([("in", "hey does your house creak a lot at night too?"), ("out", "not really why"),
   ("in", "ok never mind. it's probably just my house then")], "New Neighbor", "Today 10:15 PM",
  "📱 That last line though. React 😱 👇"),
 ([("in", "i'm running late, order without me"), ("out", "you already got here an hour ago"),
   ("in", "no i didn't. who's sitting across from you")], "Husband", "Today 12:03 AM",
  "📱 Would you look up right now? React 😱 👇"),
 ([("in", "i'm so sorry, i have the wrong house"), ("out", "whose house did you mean to be at"),
   ("in", "yours. i just got the address wrong by one digit")], "Unknown Number", "Today 4:44 AM",
  "📱 Which line got you? React 😱 👇"),
]

# ------------------------------------------------------------- brain-teaser
# (text, emoji, caption, answer)
BRAIN_TEASER = [
 ("A farmer has a fox, a chicken, and a bag of grain.\nHe can only take one across the river at a time,\nand can't leave the fox with the chicken,\nor the chicken with the grain.\n\nHow does he get all three across?", "🦊",
  "🕵️ One sentence flips the whole puzzle. Solve it 👇",
  "🦊 ANSWER: Take the chicken first, return empty, take the fox, bring the chicken back, take the grain, return empty, take the chicken."),
 ("You have two ropes. Each takes exactly\n60 minutes to burn, but unevenly.\n\nHow do you measure 45 minutes?", "🔥",
  "🕵️ Think about lighting both ends. Solve it 👇",
  "🔥 ANSWER: Light one rope at both ends and the other at one end. When rope 1 burns out (30 min), light the other end of rope 2 — it finishes in 15 more minutes. Total: 45."),
 ("A man pushes his car to a hotel\nand instantly loses everything.\n\nWhat game is he playing?", "🎲",
  "🕵️ You've played this one. Solve it 👇",
  "🎲 ANSWER: Monopoly."),
 ("Two brothers race to inherit their father's fortune —\nthe loser's horse wins.\nA stranger whispers one sentence to the slower brother's rider,\nand both horses take off at full speed.\n\nWhat did the stranger say?", "🐎",
  "🕵️ One sentence flips the whole race. Solve it 👇",
  "🐎 ANSWER: \"Switch horses.\" Each brother now races the OTHER horse hard, which determines who loses."),
 ("You're in a room with 3 switches.\nEach controls one of 3 bulbs in another room.\nYou can only enter that room once.\n\nHow do you find out which switch controls which bulb?", "💡",
  "🕵️ Think temperature, not just light. Solve it 👇",
  "💡 ANSWER: Turn on switch 1, wait a few minutes, turn it off, turn on switch 2, then enter. Lit bulb = switch 2. Warm-but-off bulb = switch 1. Cold bulb = switch 3."),
 ("A woman has 8 identical-looking balls,\none is slightly heavier.\nShe has a balance scale,\nusable only twice.\n\nHow does she find the heavier ball?", "⚖️",
  "🕵️ Split into groups first. Solve it 👇",
  "⚖️ ANSWER: Split 3/3/2. Weigh the two 3s — if balanced, weigh the remaining 2. If unbalanced, take the heavier 3, weigh 2 of them — heavier wins, or the third is heavier if those balance."),
 ("I am an odd number.\nTake away one letter\nand I become even.\n\nWhat number am I?", "🔢",
  "🕵️ Think spelling, not math. Solve it 👇",
  "🔢 ANSWER: Seven — remove the 's' and it becomes 'even'."),
 ("A man looks at a photo and says:\n'Brothers and sisters I have none,\nbut this man's father is my father's son.'\n\nWho is in the photo?", "🖼️",
  "🕵️ Read it twice. Solve it 👇",
  "🖼️ ANSWER: His own son."),
 ("A clock strikes 13 times,\none second apart.\n\nHow many seconds pass\nbetween the first and last strike?", "🕐",
  "🕵️ Count the gaps, not the strikes. Solve it 👇",
  "🕐 ANSWER: 12 seconds — there are only 12 gaps between 13 strikes."),
 ("If you have me, you want to share me.\nIf you share me, you don't have me.\n\n*What am I?*", "🤫",
  "🧠 Comment your answer before the pin 👇",
  "🤫 ANSWER: A secret."),
]

DAYS = 30
HOURS = [10, 13, 16, 19, 21, 23]
START_DATE = date(2026, 8, 10)
ROTATION = ["riddle", "whodunit", "two_line", "spot_it", "sms", "brain_teaser"]


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    counters = {k: 0 for k in ROTATION}
    n = 0

    for day_idx in range(DAYS):
        d = START_DATE + timedelta(days=day_idx)
        for slot_idx, hour in enumerate(HOURS):
            iid = f"asu-refill1-{d.isoformat()}-{hour}"
            if iid in have:
                continue
            when = f"{d.isoformat()}T{hour:02d}:00:00+00:00"
            kind = ROTATION[slot_idx]

            if kind == "two_line":
                caption = TWO_LINE[counters["two_line"] % len(TWO_LINE)]
                counters["two_line"] += 1
                items.append({"id": iid, "account": "suspense-ahead", "network": "facebook",
                             "type": "text", "message": caption, "when": when, "status": "pending"})
                n += 1
                continue

            img = f"{IMG}/{d.isoformat()}_{hour}.png"
            if kind == "riddle":
                text, emoji, caption, answer = RIDDLES[counters["riddle"] % len(RIDDLES)]
                counters["riddle"] += 1
                render(suspense_card, text, img, kicker="RIDDLE", emoji=emoji)
            elif kind == "whodunit":
                text, emoji, caption, answer = WHODUNIT[counters["whodunit"] % len(WHODUNIT)]
                counters["whodunit"] += 1
                render(suspense_card, text, img, kicker="WHODUNIT", emoji=emoji)
            elif kind == "spot_it":
                text, emoji, caption, answer = SPOT_IT[counters["spot_it"] % len(SPOT_IT)]
                counters["spot_it"] += 1
                render(suspense_card, text, img, kicker="SPOT IT", emoji=emoji)
            elif kind == "brain_teaser":
                text, emoji, caption, answer = BRAIN_TEASER[counters["brain_teaser"] % len(BRAIN_TEASER)]
                counters["brain_teaser"] += 1
                render(suspense_card, text, img, kicker="BRAIN TEASER", emoji=emoji)
            else:  # sms
                messages, contact, time_label, caption = SMS_HORROR[counters["sms"] % len(SMS_HORROR)]
                counters["sms"] += 1
                render(sms_chat, messages, img, contact=contact, time_label=time_label)
                answer = None

            it = {"id": iid, "account": "suspense-ahead", "network": "facebook",
                 "type": "photo", "message": caption, "image_url": img,
                 "when": when, "status": "pending"}
            if answer:
                it["first_comment"] = answer
            items.append(it)
            n += 1
        if (day_idx + 1) % 5 == 0:
            print(f"  ...{day_idx+1}/{DAYS} days built ({n} items so far)")
    save(q)
    print(f"Suspense Ahead refill: queued {n} items, total {len(items)}")


if __name__ == "__main__":
    build()
