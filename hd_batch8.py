# -*- coding: utf-8 -*-
"""Health Daily 8/day batch — Jul 17-23 (7 days x 7 new posts).
The 8th daily slot is the existing flagship infographic at 09:00 BD.
Types: fact (card), myth (split card), text.
Each entry: (type, payload, caption)
  fact  -> (text, kicker, emoji)
  myth  -> (myth, fact)
  text  -> None
"""

F = "\n\n💚 Follow Health Daily for daily evidence-based health tips."

# ---- 7 days x 7 posts, grouped by day ----
DAYS = [
# ============ DAY 1 ============
[
("fact", ("Drink a glass of water\n*before* your morning tea.", "MORNING TIP", "💧"),
 "☀️ You wake up mildly dehydrated — you just lost water for 7-8 hours through breathing alone.\n\nTea or coffee first thing gives you caffeine on an empty tank. Water first, then tea, and you'll notice steadier energy through the morning.\n\n💬 Tea-first or water-first? Be honest 👇" + F),
("myth", ("You must drink exactly 8 glasses of water a day.",
          "There's no magic number. Your needs depend on body size, activity, and weather — and food, tea, and milk all count. Pale yellow urine is the real signal."),
 "💧 The '8 glasses' rule has no strong scientific origin — it's a rough guideline, not a prescription.\n\nBetter approach: drink when thirsty, drink more when hot or active, and check the colour.\n\n💬 How do YOU track your water? 👇" + F),
("fact", ("Your brain is about *73% water*.\nEven mild dehydration\ncan cloud your focus.", "DID YOU KNOW?", "🧠"),
 "🧠 That 3 PM brain fog? Before you reach for more coffee, try a glass of water.\n\nStudies show even 1-2% dehydration measurably affects concentration and mood.\n\n💬 Ever noticed you focus better after drinking water? 👇" + F),
("fact", ("*Bananas* aren't just potassium.\nOne has ~3g fiber and\nsteady, slow-release energy.", "FOOD SPOTLIGHT", "🍌"),
 "🍌 The most underrated cheap food there is.\n\nGreat before a walk or workout, and the fiber keeps you full longer than most snacks at the same price.\n\n💬 Banana lover or not a fan? 👇" + F),
("fact", ("Dim the lights *1 hour*\nbefore bed —\nnot just your phone.", "EVENING TIP", "🌙"),
 "🌙 Everyone talks about phone screens, but bright ceiling lights do the same thing: they tell your brain it's still daytime.\n\nTry lamps instead of overheads after 9 PM. It's a small change with a real effect on how fast you fall asleep.\n\n💬 What time do you usually get to sleep? 👇" + F),
("text", None,
 "Quick check-in 👇\n\nHow's your energy today?\n\n⚡ High — feeling great\n😐 Okay — up and down\n😴 Low — running on empty\n\nDrop your emoji below. And if you picked 😴 — when did you last drink water or step outside?" + F),
("fact", ("Walking *10 minutes* after a meal\ncan lower your blood sugar spike\nmore than a 30-min walk later.", "QUICK FACT", "🚶"),
 "🚶 Timing beats duration here. The walk works best while your body is actually processing the meal.\n\nAfter lunch or dinner — around the block, around the house, anywhere.\n\n💬 Team walk or team couch after dinner? 👇" + F),
],
# ============ DAY 2 ============
[
("fact", ("Open a window or step outside\nwithin *1 hour* of waking.", "MORNING TIP", "🌅"),
 "🌅 Morning daylight sets your body clock for the whole day — better alertness now, easier sleep tonight.\n\n10-15 minutes is enough. Have your tea outside if you can.\n\n💬 Do you see daylight before 9 AM most days? 👇" + F),
("myth", ("Eating late at night makes you gain weight.",
          "Total calories matter far more than the clock. Late eating is linked to weight gain mostly because late snacks tend to be extra, and often processed."),
 "🌙 Your body doesn't have a 'fat storage' switch that flips at 8 PM.\n\nThat said — if late eating is *extra* eating, or it wrecks your sleep, that's the real problem.\n\n💬 Are you a late-night snacker? 👇" + F),
("fact", ("You blink about *60% less*\nwhen looking at a screen.\nThat's why your eyes burn.", "DID YOU KNOW?", "👀"),
 "👀 Your eyes rely on blinking to stay moist. Screens make you forget.\n\nThe fix is free: every 20 minutes, look 20 feet away for 20 seconds — and blink fully a few times.\n\n💬 How many hours a day are you on screens? 👇" + F),
("fact", ("*Eggs* are one of the few foods\nwith complete protein AND\nvitamin D — which most of us lack.", "FOOD SPOTLIGHT", "🥚"),
 "🥚 Cheap, fast, filling. Two eggs give ~12g of high-quality protein.\n\nAnd the yolk — long unfairly demonised — carries most of the nutrients.\n\n💬 How do you take your eggs? 👇" + F),
("fact", ("Keep your bedroom *cool*.\nYour body needs to drop\ntemperature to fall asleep.", "EVENING TIP", "🌡️"),
 "🌡️ Sleep starts with a small drop in core body temperature. A hot room fights that.\n\nCooler room, lighter blanket — many people fall asleep faster within days.\n\n💬 Fan on all night, or off? 👇" + F),
("text", None,
 "Be honest 👇\n\nWhat time did you actually fall asleep last night?\n\n🌙 Before 11 PM\n😐 11 PM – 1 AM\n🦉 After 1 AM\n\nAnd what kept you up? Comment below — we're all guilty of something." + F),
("fact", ("Standing up every *30 minutes*\nmatters more than\none long workout.", "QUICK FACT", "🪑"),
 "🪑 Long unbroken sitting affects blood sugar and circulation — even in people who exercise daily.\n\nSet a timer. Stand, stretch, walk 2 minutes. That's it.\n\n💬 How long do you sit at a stretch? 👇" + F),
],
# ============ DAY 3 ============
[
("fact", ("Eat *protein* at breakfast\nbefore anything sweet.", "MORNING TIP", "🍳"),
 "🍳 A carb-only breakfast spikes blood sugar and leaves you hungry by 11 AM.\n\nEggs, yogurt, dal, leftover chicken — anything with protein steadies the whole morning.\n\n💬 What did you have for breakfast today? 👇" + F),
("myth", ("Sweating means you're burning more fat.",
          "Sweat is temperature control, not fat loss. You can sweat buckets in a sauna and burn almost nothing — or barely sweat on a cold-weather run and burn plenty."),
 "💦 A hot room makes you sweat. It doesn't make the workout better.\n\nWhat actually matters: intensity, duration, and consistency.\n\n💬 Do you prefer working out in heat or cool? 👇" + F),
("fact", ("Your gut has ~*500 million*\nneurons — it literally\nsends signals to your brain.", "DID YOU KNOW?", "🦠"),
 "🦠 It's why stress upsets your stomach, and why gut health affects mood.\n\nFeed it well: fiber, fermented food, and variety.\n\n💬 Do you eat yogurt/dahi regularly? 👇" + F),
("fact", ("*Spinach* + a squeeze of lemon\n= far more iron absorbed.\nVitamin C unlocks plant iron.", "FOOD SPOTLIGHT", "🥬"),
 "🥬 Plant iron is hard for your body to absorb — but vitamin C dramatically improves it.\n\nSo: lemon on your greens, tomato in your dal. Small trick, real difference.\n\n💬 Did you know this one? 👇" + F),
("fact", ("No caffeine after *2 PM*.\nHalf of it can still be\nin your system at 8 PM.", "EVENING TIP", "☕"),
 "☕ Caffeine's half-life is around 5-6 hours. That 4 PM cup is still working at bedtime — even if you fall asleep, it lightens your sleep.\n\n💬 What's your caffeine cut-off time? 👇" + F),
("text", None,
 "Quick poll 👇\n\nWhich is hardest for YOU to do consistently?\n\n💧 Drink enough water\n😴 Sleep 7-8 hours\n🚶 Move every day\n🥗 Eat properly\n\nDrop your emoji. You'll be surprised how many people picked the same one." + F),
("fact", ("Chewing food *thoroughly*\nis the easiest digestion fix\nnobody talks about.", "QUICK FACT", "🍽️"),
 "🍽️ Digestion starts in your mouth. Swallowing half-chewed food makes your stomach do work it wasn't designed for — hello bloating.\n\nSlow down. Put the fork down between bites.\n\n💬 Fast eater or slow eater? 👇" + F),
],
# ============ DAY 4 ============
[
("fact", ("Make your bed.\nIt's not about tidiness —\nit's a *2-minute win* at 7 AM.", "MORNING TIP", "🛏️"),
 "🛏️ Starting the day with one completed task is a genuine psychological nudge. Small, but it compounds.\n\nBonus: you're far less likely to crawl back in.\n\n💬 Do you make your bed daily? 👇" + F),
("myth", ("You need supplements to be healthy.",
          "For most people, food covers it. Supplements help when you're actually deficient — which a blood test tells you, not an advertisement."),
 "💊 The supplement industry is worth billions because it sells certainty, not health.\n\nTest first. Then supplement what's actually low (vitamin D is a common one).\n\n💬 Do you take any supplements? Which? 👇" + F),
("fact", ("Your body makes about\n*1.5 litres of saliva* daily —\nand it's your first defence.", "DID YOU KNOW?", "😮"),
 "😮 Saliva starts digestion, protects your teeth, and fights bacteria.\n\nDry mouth all the time? That's often dehydration — or a medication side effect worth asking your doctor about.\n\n💬 Did this one surprise you? 👇" + F),
("fact", ("*Garlic* is at its healthiest\nwhen crushed and left\nfor 10 minutes before cooking.", "FOOD SPOTLIGHT", "🧄"),
 "🧄 Crushing triggers the enzyme reaction that creates allicin — the compound behind most of garlic's benefits. Cooking immediately destroys it.\n\nCrush first, chop your onions, then cook.\n\n💬 Trying this tonight? 👇" + F),
("fact", ("A warm shower before bed\ncools your body *afterwards* —\nand that helps you sleep.", "EVENING TIP", "🚿"),
 "🚿 Counterintuitive but real: warming your skin sends blood to the surface, and your core temperature drops after — which is the sleep signal.\n\n90 minutes before bed is the sweet spot.\n\n💬 Morning shower or night shower? 👇" + F),
("text", None,
 "Fill in the blank 👇\n\n\"I know I should ______ , but I never do.\"\n\nHealth edition. Be honest — no judgement here. Sometimes writing it down is the first push." + F),
("fact", ("*Cold hands* often mean\nyour body is prioritising\nyour core — not poor health.", "QUICK FACT", "🥶"),
 "🥶 It's usually normal circulation doing its job.\n\nBut if hands turn white or blue, go numb, or it happens with pain — that's worth a doctor's opinion.\n\n💬 Always-cold hands? Comment 🙋" + F),
],
# ============ DAY 5 ============
[
("fact", ("Stretch for *2 minutes*\nbefore you touch your phone.", "MORNING TIP", "🙆"),
 "🙆 Your body has been still for 8 hours. Two minutes of gentle stretching wakes up your spine and shoulders before you hunch over a screen.\n\nNeck rolls, shoulder rolls, reach up, touch toes. Done.\n\n💬 Do you stretch in the morning? 👇" + F),
("myth", ("Carbs make you fat.",
          "Excess calories do. Whole-food carbs — rice, oats, fruit, lentils — come with fiber and nutrients. The problem is refined carbs and portion size, not the food group."),
 "🍚 Half the world eats rice daily and doesn't share one body type.\n\nThe real issue: refined, processed carbs eaten in excess without protein or fiber alongside.\n\n💬 Could you give up rice? 👇" + F),
("fact", ("Laughing *100 times*\nis roughly comparable to\n10 minutes of rowing.", "DID YOU KNOW?", "😂"),
 "😂 It works your diaphragm, abs, and even lowers stress hormones.\n\nNot a replacement for exercise — but a genuinely good reason to call the friend who makes you laugh.\n\n💬 Tag the person who makes you laugh most 👇" + F),
("fact", ("*Dark chocolate* (70%+)\nhas magnesium, fiber,\nand real antioxidants.", "FOOD SPOTLIGHT", "🍫"),
 "🍫 The catch: milk chocolate is mostly sugar. 70%+ cocoa is where the benefits live.\n\nA square or two in the evening — genuinely fine.\n\n💬 Dark chocolate: love it or too bitter? 👇" + F),
("fact", ("Write tomorrow's *3 tasks*\nbefore bed.\nYour brain stops rehearsing them.", "EVENING TIP", "📝"),
 "📝 Lying awake with a spinning mind is often just your brain refusing to forget tomorrow's list.\n\nWrite it down. You're telling your brain it's safe to stop holding it.\n\n💬 Does your mind race at bedtime? 👇" + F),
("text", None,
 "Two-word check-in 👇\n\nDescribe how your body feels right now — in exactly two words.\n\nWe'll start: \"Tired. Hopeful.\"\n\nYour turn." + F),
("fact", ("Your *sense of thirst*\nweakens as you age.\nOlder adults dehydrate faster.", "QUICK FACT", "👵"),
 "👵 If you have elderly parents or grandparents — they often simply don't feel thirsty, even when they need water.\n\nA glass offered is better than waiting to be asked.\n\n📌 Share this with someone who has older parents at home." + F),
],
# ============ DAY 6 ============
[
("fact", ("Sunlight *before* screens.\nEven 5 minutes\nchanges your whole morning.", "MORNING TIP", "☀️"),
 "☀️ Most of us check a phone before we've seen daylight. Your body clock reads screens as noise and sunlight as the real signal.\n\nBalcony, window, rooftop — 5 minutes counts.\n\n💬 What's the FIRST thing you do after waking? Honest answers 👇" + F),
("myth", ("Going out with wet hair gives you a cold.",
          "Colds come from viruses, not temperature. You catch more colds in winter because people crowd indoors and share air — not because of wet hair."),
 "🤧 Your grandmother meant well. The science just doesn't back this one.\n\nBeing cold may stress the body slightly, but without a virus, there's nothing to catch.\n\n💬 Who else grew up hearing this? 🙋" + F),
("fact", ("Your bones are\n*completely replaced*\nroughly every 10 years.", "DID YOU KNOW?", "🦴"),
 "🦴 Your skeleton is constantly rebuilding itself. Which means what you eat and how you move now literally builds the bones you'll have later.\n\nCalcium, vitamin D, and weight-bearing movement.\n\n💬 Did you know this? 👇" + F),
("fact", ("*Yogurt/dahi* is one of the\ncheapest probiotic foods\navailable anywhere.", "FOOD SPOTLIGHT", "🥛"),
 "🥛 Plain, unsweetened is best — flavoured versions can carry as much sugar as dessert.\n\nOne small bowl daily is a genuinely good habit for your gut.\n\n💬 Do you eat dahi daily? 👇" + F),
("fact", ("Put your phone\n*across the room* at night.\nNot beside the pillow.", "EVENING TIP", "📵"),
 "📵 If it's within reach, you'll check it — at bedtime, at 2 AM, and the moment you wake.\n\nAcross the room = it doubles as an alarm you have to stand up for.\n\n💬 Where does your phone sleep? Honest 👇" + F),
("text", None,
 "One healthy thing you did today 👇\n\nSmall counts. Drank water. Took the stairs. Went to bed early. Said no to the second cup.\n\nType it below — someone reading might need the idea." + F),
("fact", ("*Loneliness* affects health\ncomparably to well-known\nphysical risk factors.", "QUICK FACT", "💚"),
 "💚 Human connection isn't a luxury — it's a health input, like sleep and food.\n\nOne call. One message. Today.\n\n💬 Tag someone you've been meaning to check on 👇" + F),
],
# ============ DAY 7 ============
[
("fact", ("Don't check email\nfor the first *30 minutes*\nof your day.", "MORNING TIP", "📧"),
 "📧 Starting your day inside someone else's priorities puts you in reaction mode before you've even had tea.\n\nGive yourself 30 minutes that belong to you.\n\n💬 Do you check your phone before getting out of bed? 👇" + F),
("myth", ("You should push through pain when exercising.",
          "'No pain, no gain' is dangerous advice. Muscle burn is normal; sharp, sudden, or joint pain is your body warning you. Pushing through it is how injuries happen."),
 "🏋️ There's a difference between effort and damage.\n\nBurn = fine. Sharp pain, joint pain, or pain that lingers days = stop and get it checked.\n\n💬 Ever pushed through and regretted it? 👇" + F),
("fact", ("Your stomach lining\nreplaces itself every\n*few days* — it has to.", "DID YOU KNOW?", "🔬"),
 "🔬 Otherwise your own stomach acid would digest it. Your body is quietly rebuilding you all the time.\n\nWorth feeding it decently.\n\n💬 Surprised by this one? 👇" + F),
("fact", ("*Lentils/dal* — protein AND\nfiber in one cheap bowl.\nMost foods give you one.", "FOOD SPOTLIGHT", "🫘"),
 "🫘 One of the most complete, affordable foods on earth — and it's already in most of our kitchens.\n\nProtein, fiber, iron, and it keeps you full for hours.\n\n💬 How often do you eat dal? 👇" + F),
("fact", ("Same *bedtime* every night\nbeats sleeping longer\non weekends.", "EVENING TIP", "⏰"),
 "⏰ Sleeping till noon on Friday and 6 AM on Monday is jet lag without the holiday. Your body clock can't keep up.\n\nConsistency > catching up.\n\n💬 Same bedtime daily, or all over the place? 👇" + F),
("text", None,
 "This week's honest question 👇\n\nWhich ONE habit would change your health the most if you actually stuck to it?\n\nNot all of them. Just one.\n\nComment it — then do it tomorrow. We'll ask again next week 😉" + F),
("fact", ("The best exercise\nis the one you'll\n*actually keep doing.*", "QUICK FACT", "🏃"),
 "🏃 The perfect gym plan you quit in 3 weeks loses to the boring 20-minute walk you do for years.\n\nPick what fits your life, not what impresses people.\n\n💬 What's YOUR sustainable movement? 👇" + F),
],
]
