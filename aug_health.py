# -*- coding: utf-8 -*-
"""Health Daily — Aug 1-7 refill. 7 posts/day: 6 image cards (FB+IG mirror) + 1 text (FB).
Fresh topics (no overlap with July). Value-formula captions, save-CTA (no bare 'Follow me')."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, when, mkdir, render
from image_health_light import health_fact, health_myth_fact

IMG = mkdir("images/aug_hd")
SAVE = "\n\n💚 Bookmark this. You'll need it later."

# kinds: fact=(text,kicker,emoji,caption)  myth=(myth,fact,caption)  text=(caption,)
DAYS = [
# ---- DAY 1 ----
[
 ("fact", ("Drink a glass of water\n*before* your morning coffee.", "MORNING TIP", "💧",
   "☕ Reaching for coffee first on an empty, dehydrated body is why the caffeine hits hard then crashes. A glass of water first steadies your energy and eases that mid-morning slump.\n\n→ Water first, coffee second\n→ Wait 60–90 min after waking for coffee if you can\n→ It blunts the crash more than a second cup ever will" + SAVE + "\n💬 Coffee before or after water — honestly? 👇")),
 ("myth", ("Eating after 8 PM makes you gain weight.",
   "The clock doesn't add fat — total daily calories do. A late, balanced meal is fine; it's mindless late-night snacking that adds up.",
   "🌙 You've heard 'never eat after 8.' But your body doesn't read a clock. What matters is how much you eat across the whole day, not the hour.\n\n→ A proper late dinner: fine\n→ Chips on the couch at 11 PM: that's the real issue\n→ If late eating disturbs your sleep, shift it earlier for comfort, not fear" + SAVE + "\n💬 Are you a late-night snacker? 👇")),
 ("fact", ("How fast your heart\n*slows down* after exercise\ntells you how fit you are.", "DID YOU KNOW?", "❤️",
   "❤️ It's called heart-rate recovery. A heart that drops quickly back to rest after effort is a strong sign of fitness — and it improves with regular movement.\n\nWalk briskly, then time how fast you settle. In a few weeks of consistent activity, you'll settle faster." + SAVE + "\n💬 How's your recovery after climbing stairs? 👇")),
 ("fact", ("*Bananas* — potassium that\nhelps balance salt and\nsteady your blood pressure.", "FOOD SPOTLIGHT", "🍌",
   "🍌 Most of us get too much salt and too little potassium — the mineral that counters it. Bananas are one of the easiest, cheapest fixes.\n\n→ Also in potatoes, beans, spinach, yogurt\n→ Great pre-walk snack for steady energy\n→ Pair with nuts for staying power" + SAVE + "\n💬 Banana: daily or never? 👇")),
 ("fact", ("Charge your phone\n*outside* the bedroom.", "EVENING TIP", "🔌",
   "🔌 The phone by the pillow is the #1 silent sleep thief — one glance and you're scrolling, one buzz and you're awake. Charging it in another room removes the temptation entirely.\n\nBuy a cheap alarm clock so 'I need it for the alarm' stops being the excuse." + SAVE + "\n💬 Where does your phone sleep? 👇")),
 ("text", ("Quick check-in 👇\n\nHow many hours did you actually sleep last night?\n\n😴 7–8\n😐 5–6\n😩 under 5\n\nDrop your number — and if it was under 5, what kept you up?",)),
 ("fact", ("Your neck holds up a head\nthat gets *heavier* the more\nyou look down at your phone.", "QUICK FACT", "📱",
   "📱 Looking down at a screen loads your neck like a small child sitting on it. Hours of that daily is why so many people have neck and upper-back pain.\n\n→ Lift the phone to eye level\n→ Every 20 min, roll the shoulders back\n→ Tuck the chin, don't crane forward" + SAVE + "\n💬 Neck or back stiff by evening? 👇")),
],
# ---- DAY 2 ----
[
 ("fact", ("Splash *cold water* on your face\nwhen the afternoon slump hits.", "MORNING TIP", "🚿",
   "🚿 That 3 PM fog? Before you reach for a third coffee, try cold water on the face or wrists. It triggers a quick alertness response — no caffeine, no crash later.\n\n→ Cold water on face/wrists\n→ Or a 2-minute walk in fresh air\n→ Save the coffee for when you truly need it" + SAVE + "\n💬 When does your energy dip most? 👇")),
 ("myth", ("Supplements can replace a bad diet.",
   "Pills fill gaps — they can't undo poor eating. Whole food gives fiber and dozens of compounds no capsule copies.",
   "💊 Multivitamins have their place, but no supplement 'cancels' junk food. Real food comes as a package your body absorbs far better.\n\n→ Fix the plate first\n→ Supplement genuine gaps (e.g. vitamin D, B12 if advised)\n→ Save your money on the fancy 'detox' pills" + SAVE + "\n💬 What do you actually take daily? 👇")),
 ("fact", ("Even *mild dehydration*\nshows up as brain fog\nbefore you feel thirsty.", "DID YOU KNOW?", "🧠",
   "🧠 Your brain is about 75% water. Being just slightly low hits focus, mood and headaches — long before your mouth feels dry.\n\nKeep a bottle in sight; we drink more when we can see it. Pale-yellow urine is your real hydration signal." + SAVE + "\n💬 How many glasses so far today? 👇")),
 ("fact", ("*Oats* — slow-release energy\nand fiber that keeps you\nfull till lunch.", "FOOD SPOTLIGHT", "🥣",
   "🥣 One of the cheapest complete breakfasts there is. The fiber steadies blood sugar and feeds good gut bacteria — so you're not starving by 11.\n\n→ Add nuts + fruit for staying power\n→ Skip the sugary instant sachets\n→ Overnight oats = zero-effort mornings" + SAVE + "\n💬 Oats: love them or can't do the texture? 👇")),
 ("fact", ("Write tomorrow's *top 3 tasks*\nbefore you sleep.", "EVENING TIP", "📝",
   "📝 A racing mind at bedtime is often just your brain afraid it'll forget things. Offload them onto paper and it lets go — you fall asleep faster and wake up clearer.\n\nThree tasks, not thirty. The point is to empty the head, not plan the year." + SAVE + "\n💬 Do you plan the night before? 👇")),
 ("text", ("Fill in the blank 👇\n\n\"I feel my healthiest when I ______.\"\n\nSometimes naming it is the reminder you needed. Comment yours 👇",)),
 ("fact", ("A 10-minute walk\ncan lift a low mood\n*faster* than sugar.", "QUICK FACT", "🚶",
   "🚶 When you feel flat, the reach for a snack is often a reach for a mood boost. A short walk gives you the same lift — without the crash 30 minutes later.\n\n→ Outside beats indoors (light helps)\n→ 10 minutes is enough to shift the mood\n→ Bonus: it aids digestion too" + SAVE + "\n💬 Walk or snack when you're low? 👇")),
],
# ---- DAY 3 ----
[
 ("fact", ("Put *protein* in your\nfirst meal, whatever time\nyou eat it.", "MORNING TIP", "🍳",
   "🍳 A carb-only breakfast spikes then drops your blood sugar — hello 11 AM cravings. Adding protein flattens that curve and keeps you full for hours.\n\n→ Eggs, yogurt, dal, nuts, cheese\n→ Aim for a palm-sized portion\n→ Works whether you eat at 7 AM or noon" + SAVE + "\n💬 What's your usual first meal? 👇")),
 ("myth", ("No pain, no gain.",
   "Sharp pain is a warning, not a badge. Progress comes from consistent effort — soreness is optional, injury sets you back weeks.",
   "💪 The 'push through the pain' idea injures more people than it helps. Mild muscle fatigue is fine; sharp or joint pain means stop.\n\n→ Challenge ≠ pain\n→ Rest days are when you actually get stronger\n→ Consistency beats one brutal session you can't repeat" + SAVE + "\n💬 Ever pushed too hard and paid for it? 👇")),
 ("fact", ("Your *skin* often shows\nyour sleep, water and stress\nbefore anything else does.", "DID YOU KNOW?", "✨",
   "✨ Chasing glow with creams while sleeping 4 hours is fighting yourself. Skin reflects habits: water, sleep, and less sugar do more than most products.\n\nBefore the next serum, fix the basics for two weeks and watch what changes." + SAVE + "\n💬 What changed your skin most — product or habit? 👇")),
 ("fact", ("*Berries* — big antioxidants,\nlow sugar, and they curb\nsweet cravings.", "FOOD SPOTLIGHT", "🫐",
   "🫐 One of the few genuinely sweet foods that loves you back — high in fiber and antioxidants, low on the blood-sugar spike.\n\n→ Frozen is just as good (and cheaper)\n→ Toss into yogurt or oats\n→ A handful when the sugar craving hits" + SAVE + "\n💬 Berries or you'd rather have chocolate? 👇")),
 ("fact", ("Keep the phone *out of reach*\nfor the first hour after\nyou lie down.", "EVENING TIP", "📵",
   "📵 'Just five minutes' turns into an hour, and the blue light plus the mental stimulation delay sleep by far more than you think.\n\n→ Charge it across the room\n→ Read a few pages instead\n→ Your brain needs boredom to switch off" + SAVE + "\n💬 Honest — phone in bed or not? 👇")),
 ("text", ("Honest question 👇\n\nWhat's the ONE health habit that would change the most for you — if you actually stuck to it?\n\nNot all of them. Just one. Comment it, then start tomorrow 👇",)),
 ("fact", ("Two minutes of *slow breathing*\ncalms your body faster\nthan almost anything free.", "QUICK FACT", "😮‍💨",
   "😮‍💨 In for 4 seconds, out for 6. The long exhale flips you from stress mode into rest mode — heart rate drops, shoulders loosen. Costs nothing, works in minutes.\n\nTry five rounds right now before you scroll on." + SAVE + "\n💬 Feel calmer after 5 rounds? 👇")),
],
# ---- DAY 4 ----
[
 ("fact", ("Get *daylight* in your eyes\nwithin an hour of waking.", "MORNING TIP", "🌅",
   "🌅 Morning light is the single strongest signal that sets your body clock — better energy today and easier sleep tonight. Ten minutes on the balcony with your tea counts.\n\n→ Outdoor light beats any indoor bulb\n→ No sunglasses for those first minutes\n→ Cloudy days still work" + SAVE + "\n💬 Do you see daylight before 9 AM? 👇")),
 ("myth", ("Sit-ups burn belly fat.",
   "You can't spot-reduce fat. Crunches build the muscle underneath, but the fat on top only drops with overall diet and activity.",
   "🔥 A thousand sit-ups won't melt belly fat — the body burns fat all over, not where you work. Abs are made in the kitchen first.\n\n→ Build the muscle with core work\n→ Reveal it with overall fat loss\n→ Walking + protein does more for the waist than crunches" + SAVE + "\n💬 Who was told sit-ups were the secret? 🙋 👇")),
 ("fact", ("Your *gut* makes much of the\nchemistry that affects your mood.", "DID YOU KNOW?", "🦠",
   "🦠 The gut and brain talk constantly. A big share of your feel-good chemistry starts in the gut — which is why what you eat quietly shapes how you feel.\n\nFeed it fiber and fermented foods, and your mood often follows within weeks." + SAVE + "\n💬 Does stress hit your stomach first? 👇")),
 ("fact", ("*Yogurt/dahi* — one of the\ncheapest probiotic foods\non earth.", "FOOD SPOTLIGHT", "🥛",
   "🥛 Plain, unsweetened yogurt feeds the good bacteria in your gut — better digestion and, over time, better mood.\n\n→ Plain beats flavoured (those hide dessert-level sugar)\n→ Add fruit or nuts yourself\n→ One small bowl a day is a genuinely good habit" + SAVE + "\n💬 Do you eat dahi daily? 👇")),
 ("fact", ("Two minutes of *stretching*\nbefore bed loosens\na day of sitting.", "EVENING TIP", "🧘",
   "🧘 Hours hunched at a desk leave the hips and back tight — which follows you into a restless night. A short, gentle stretch signals the body to wind down.\n\n→ Neck, shoulders, hips, hamstrings\n→ Slow and easy, never forced\n→ Pair it with dimming the lights" + SAVE + "\n💬 Do you stretch before bed? 👇")),
 ("text", ("Two-word check-in 👇\n\nHow does your body feel right now — in exactly two words?\n\nWe'll start: \"Tired. Hopeful.\" Your turn 👇",)),
 ("fact", ("Cooked *tomatoes* release\nmore of their best antioxidant\nthan raw ones.", "QUICK FACT", "🍅",
   "🍅 Unusual but true — heat unlocks lycopene, the antioxidant linked to heart health. So tomato curry and sauce have their upside.\n\n→ A little oil helps absorption\n→ Raw tomatoes are still great for other nutrients\n→ Variety wins: eat them both ways" + SAVE + "\n💬 Raw or cooked tomatoes for you? 👇")),
],
# ---- DAY 5 ----
[
 ("fact", ("*Move* for five minutes\nbefore you sit down\nto work.", "MORNING TIP", "⚡",
   "⚡ Going straight from bed to chair keeps your body in low gear all morning. Five minutes of movement first — a walk, stretches, stairs — wakes up circulation and focus.\n\n→ It doesn't need to be a 'workout'\n→ Enough to feel slightly warm\n→ Your first hour of work will feel sharper" + SAVE + "\n💬 Do you move before you sit? 👇")),
 ("myth", ("Brown bread is always healthier than white.",
   "Many 'brown' loaves are white bread dyed with caramel colour. Look for 'whole grain' as the first ingredient — that's what matters.",
   "🍞 The colour tells you nothing. Some brown bread is just white bread with colouring. The real signal is the ingredient list.\n\n→ Look for 'whole wheat/grain' listed first\n→ 'Multigrain' and 'brown' are marketing, not proof\n→ More fiber per slice = the actual win" + SAVE + "\n💬 Ever checked your bread's label? 👇")),
 ("fact", ("*Grip strength* is one of the\nsimplest signs of how well\nyou're ageing.", "DID YOU KNOW?", "🤝",
   "🤝 It sounds odd, but how firmly you can grip tracks with overall strength and healthy ageing. Weak hands often mean weak everything else.\n\nCarry your own groceries, hang from a bar, use a stress ball — small things that keep the whole body capable." + SAVE + "\n💬 Firm handshake or need to work on it? 👇")),
 ("fact", ("*Spinach + lemon* =\nfar more iron absorbed.", "FOOD SPOTLIGHT", "🥬",
   "🥬 Iron from plants is hard to absorb — but vitamin C unlocks it. A squeeze of lemon on your greens can multiply how much iron you actually get.\n\n→ Lemon on spinach, tomato in dal\n→ Skip tea/coffee right after iron-rich meals (they block it)\n→ Cheap trick, real difference" + SAVE + "\n💬 Did you know this one? 👇")),
 ("fact", ("Keep the bedroom *cool*.\nYour body must drop\ntemperature to fall asleep.", "EVENING TIP", "🌡️",
   "🌡️ Sleep begins with a small dip in your core temperature — a hot room fights that every night. Cooler air, a lighter blanket, and you drift off faster.\n\n→ Fan or cracked window helps\n→ A warm shower before bed actually cools you after\n→ Cooler room > heavier blanket" + SAVE + "\n💬 Fan on all night or off? 👇")),
 ("text", ("One healthy thing you did today 👇\n\nDrank water. Took the stairs. Slept early. Said no to seconds.\n\nType it below — someone reading might need the idea 👇",)),
 ("fact", ("Cutting *salt* slowly\nlets your taste buds\nadjust in about two weeks.", "QUICK FACT", "🧂",
   "🧂 Too much salt quietly raises blood pressure — but going bland overnight never lasts. Reduce it gradually and food that once tasted flat starts tasting right.\n\n→ Cut back a little at a time\n→ Lean on herbs, lemon, garlic for flavour\n→ Watch the hidden salt in packaged food" + SAVE + "\n💬 Heavy hand with the salt? Honest 👇")),
],
# ---- DAY 6 ----
[
 ("fact", ("Don't check your phone\nfor the first *20 minutes*\nof your day.", "MORNING TIP", "🌄",
   "🌄 Opening notifications first thing throws you into reaction mode before you've even woken up. Give yourself 20 phone-free minutes and the whole day feels less rushed.\n\n→ Water, light, a stretch first\n→ Emails will still be there at 9\n→ Start the day on your terms, not the inbox's" + SAVE + "\n💬 First thing you do after waking? Honest 👇")),
 ("myth", ("Eating carbs at night is bad for you.",
   "Carbs don't behave differently after dark. Total intake and quality matter, not timing. Some people even sleep better with an evening carb.",
   "🍚 'No carbs after 6' is a diet myth. Your body doesn't switch rules at sunset. A sensible portion of whole-food carbs at dinner is completely fine.\n\n→ It's the amount, not the hour\n→ Rice, oats, fruit = fine at night\n→ Chips and sweets are the real evening trap" + SAVE + "\n💬 Do you avoid carbs at night? 👇")),
 ("fact", ("You blink *far less*\nstaring at a screen —\nthat's why eyes burn.", "DID YOU KNOW?", "👀",
   "👀 Focused on a screen, you blink about half as often, so eyes dry out and sting by evening. The fix is almost free.\n\n→ Every 20 min, look 20 feet away for 20 seconds\n→ Blink fully and often\n→ Position the screen slightly below eye level" + SAVE + "\n💬 Hours a day on screens? 👇")),
 ("fact", ("*Green tea* — steady focus\nwithout the coffee jitters.", "FOOD SPOTLIGHT", "🍵",
   "🍵 Less caffeine than coffee, plus a calming compound that smooths it out — so you get gentle, sustained focus instead of a spike and crash.\n\n→ Great mid-morning or early afternoon\n→ Skip the sugar\n→ Not a magic fat-burner — just a solid swap" + SAVE + "\n💬 Tea or coffee person? 👇")),
 ("fact", ("Dim the lights *an hour*\nbefore bed — not just\nyour phone.", "EVENING TIP", "💡",
   "💡 Bright overhead lights tell your brain it's still daytime and delay your sleep hormone. Switching to lamps in the evening helps you fall asleep faster.\n\n→ Warm, low light after 9 PM\n→ Lamps over ceiling lights\n→ It's the whole room, not only the screen" + SAVE + "\n💬 What time do you usually sleep? 👇")),
 ("text", ("This week's honest question 👇\n\nWhat's one health habit you dropped that you'd like to restart?\n\nWriting it down is the first step back. Comment it 👇",)),
 ("fact", ("Chew slowly — digestion\nstarts in your *mouth*,\nnot your stomach.", "QUICK FACT", "🍽️",
   "🍽️ Swallowing half-chewed food makes your stomach do extra work — which is where a lot of bloating comes from. Slowing down also lets 'full' signals catch up.\n\n→ Put the fork down between bites\n→ Chew until it's nearly liquid\n→ Bonus: you eat less without trying" + SAVE + "\n💬 Fast or slow eater? 👇")),
],
# ---- DAY 7 ----
[
 ("fact", ("Do the *hardest task first* —\nbefore your willpower drains.", "MORNING TIP", "🐸",
   "🐸 Your focus and self-control are highest early. Spend them on the task you dread most, and the rest of the day feels downhill instead of a looming cloud.\n\n→ Pick the one thing you keep avoiding\n→ Do it before email and messages\n→ 'Eat the frog' first, coast after" + SAVE + "\n💬 What task do you keep pushing back? 👇")),
 ("myth", ("Sweating in a sauna 'flushes out toxins.'",
   "Sweat is temperature control, not detox. Your liver and kidneys handle toxins 24/7. Saunas can relax you — they don't cleanse you.",
   "🧖 The 'sweating out toxins' idea sells a lot of saunas and wraps, but it isn't how the body works. Your organs do the detoxing, for free.\n\n→ Sweat = cooling, not cleansing\n→ Saunas are fine for relaxation\n→ Drink water — you're losing fluid, not 'toxins'" + SAVE + "\n💬 Ever bought a 'detox' product? 👇")),
 ("fact", ("*Loneliness* affects health\nas much as many\nphysical risk factors.", "DID YOU KNOW?", "💚",
   "💚 Connection is a genuine health input — like food and sleep. Long-term isolation strains the body in measurable ways, while a good conversation eases it.\n\nOne call, one message, today. It counts more than you think." + SAVE + "\n💬 Tag someone you've been meaning to check on 👇")),
 ("fact", ("*Olive oil* — a fat that's\nactually good for\nyour heart.", "FOOD SPOTLIGHT", "🫒",
   "🫒 Not all fat is the enemy. Extra-virgin olive oil is rich in the kind linked to better heart health — a smarter everyday choice than heavily refined oils.\n\n→ Great drizzled raw over salad or dal\n→ A little goes a long way (still calorie-dense)\n→ Real EVOO tastes peppery, not flat" + SAVE + "\n💬 What oil do you cook with? 👇")),
 ("fact", ("A *consistent bedtime*\nbeats sleeping in\non weekends.", "EVENING TIP", "⏰",
   "⏰ Sleeping till noon Saturday then 6 AM Monday is like flying across time zones every week — your body never settles. A steady bedtime beats trying to 'catch up.'\n\n→ Same sleep/wake time, even weekends\n→ Consistency > total hours banked\n→ Your mornings get easier within a week" + SAVE + "\n💬 Fixed bedtime or all over the place? 👇")),
 ("text", ("Last check-in of the week 👇\n\nOne word: how do you WANT to feel next week?\n\nWe'll start: \"Lighter.\" Your turn — then let's make it happen 👇",)),
 ("fact", ("Consistency beats intensity.\n*Small daily habits*\nwin every time.", "QUICK FACT", "🌱",
   "🌱 One healthy choice today beats a perfect plan that starts 'Monday.' Health is built in ordinary days, not dramatic resets you can't sustain.\n\n→ Pick one small habit you can't fail at\n→ Repeat it daily, boringly\n→ Let it get easier before you add the next" + SAVE + "\n💬 What small habit are you sticking to? 👇")),
],
]

HOURS = [1, 4, 7, 10, 13, 16, 19]  # UTC posting slots across the day (7 posts)


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n_img = 0
    for di, day in enumerate(DAYS):
        for pi, entry in enumerate(day):
            kind = entry[0]
            hour = HOURS[pi]
            base_id = f"ahd-d{di+1}-{pi+1}"
            ts = when(di, hour)
            if base_id in have or (base_id + "-fb") in have:
                continue  # resume: already enqueued
            if kind == "text":
                caption = entry[1]
                items.append({"id": base_id, "account": "health-daily", "network": "facebook",
                              "type": "text", "message": caption, "when": ts, "status": "pending"})
                continue
            # render image
            img_path = f"{IMG}/d{di+1}_{pi+1}.png"
            if kind == "fact":
                text, kicker, emoji, caption = entry[1]
                render(health_fact, text, img_path, kicker=kicker, emoji=emoji)
            else:  # myth
                myth, fact, caption = entry[1]
                render(health_myth_fact, myth, fact, img_path)
            n_img += 1
            print(f"  rendered {img_path}")
            # FB photo + IG image mirror
            items.append({"id": base_id + "-fb", "account": "health-daily", "network": "facebook",
                          "type": "photo", "message": caption, "image_url": img_path,
                          "when": ts, "status": "pending"})
            items.append({"id": base_id + "-ig", "account": "health-daily", "network": "instagram",
                          "type": "image", "message": caption, "image_url": img_path,
                          "when": ts, "status": "pending"})
    save(q)
    print(f"HEALTH DAILY: rendered {n_img} images, queue now {len(items)} items")


if __name__ == "__main__":
    build()
