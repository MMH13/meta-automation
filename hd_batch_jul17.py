# -*- coding: utf-8 -*-
"""Health Daily 14-day batch: 1 post/day, FB 09:00 +06 (native schedule)
+ IG 09:10 +06 (local queue). Day 1 = 2026-07-17.
Fields: n, title, bullets (card), theme, cap (FB+IG caption)."""

POSTS = [
{"n":1,"theme":"mint_light","title":"Eat Protein First Thing in the Morning",
 "bullets":["Keeps you full until lunch","Steadies blood sugar & energy","Reduces late-night cravings","Protects muscle as you age"],
 "cap":"""🍳 The easiest health upgrade nobody talks about: eat 25-30g of protein at breakfast.

Most of us start the day with mostly carbs — bread, paratha, cereal, biscuits with tea. Result? Energy crash and hunger by 11 AM.

Here's what a protein-first breakfast does:

✅ Keeps you full for hours (protein is the most satiating nutrient)
✅ Steadies blood sugar — no mid-morning crash
✅ Reduces cravings later in the day
✅ Helps maintain muscle, especially after 30

🥚 Easy options:
• 2-3 eggs, any style
• Greek yogurt or thick dahi with nuts
• Leftover chicken or fish from dinner
• Lentils/dal with your breakfast

💬 What did YOU have for breakfast today? Be honest 👇

📌 Save this as your morning reminder.

#HealthDaily #Protein #BreakfastIdeas #HealthyEating #Nutrition #HealthTips #StayHealthy"""},

{"n":2,"theme":"teal_dark","title":"The 10,000 Steps Myth — What Science Really Says",
 "bullets":["10K was a 1960s marketing number","Big benefits start at 4,000 steps","7,000-8,000 is the sweet spot","Pace matters less than showing up"],
 "cap":"""🚶 Confession: the "10,000 steps a day" rule wasn't science. It came from a 1960s Japanese pedometer ad.

Here's what research actually shows:

✅ Health benefits start around 4,000 steps/day
✅ Most of the longevity benefit arrives by 7,000-8,000 steps
✅ Beyond that, gains flatten out — more is fine, but not required
✅ Consistency beats intensity — daily 6,000 beats weekend 15,000

So if 10K has been discouraging you — stop chasing it. Aim for 7,000. That's roughly an hour of total walking spread across your whole day.

💡 Painless ways to add steps: take calls while walking, park farther, use stairs, walk after meals.

💬 How many steps do you average? Check your phone and tell us below 👇

📌 Share this with the friend who gave up on 10K.

#HealthDaily #Walking #10000Steps #FitnessMyths #HealthTips #StayActive #HealthyLifestyle"""},

{"n":3,"theme":"mint_light","title":"Your Gut Controls More Than You Think",
 "bullets":["70% of immune cells live in your gut","Gut bacteria affect mood & sleep","Fermented foods feed good bacteria","Variety of plants = healthier gut"],
 "cap":"""🦠 Your gut isn't just digesting food — it's running a big part of your health:

• ~70% of your immune system lives in your gut
• Gut bacteria produce chemicals that affect mood, sleep and even cravings
• A struggling gut shows up as bloating, low energy, skin issues, and getting sick often

💚 How to feed the good bacteria:

✅ Fermented foods — yogurt/dahi, kefir, pickled vegetables
✅ Fiber — vegetables, fruits, whole grains, lentils
✅ Variety — aim for many different plant foods each week; each feeds different bacteria
✅ Go easy on ultra-processed food and unnecessary antibiotics

💡 Simple start: one serving of plain yogurt daily + one new vegetable each week.

💬 Do you eat yogurt/dahi regularly? Every day, sometimes, or never? 👇

📌 Save this — your gut will thank you.

#HealthDaily #GutHealth #Probiotics #Digestion #HealthTips #Nutrition #Wellness"""},

{"n":4,"theme":"teal_dark","title":"5 Sneaky Signs You're Dehydrated",
 "bullets":["Afternoon fatigue & brain fog","Headaches that come from nowhere","Craving sugar late in the day","Dark yellow urine = warning light"],
 "cap":"""💧 You might be dehydrated right now and not know it.

Thirst shows up LATE. Before that, dehydration disguises itself as:

1️⃣ Afternoon fatigue — feeling drained by 3 PM for no reason
2️⃣ Brain fog — trouble focusing, slow thinking
3️⃣ Random headaches — often the first sign
4️⃣ Sugar cravings — your body confuses thirst with hunger
5️⃣ Dark yellow urine — the clearest warning light your body gives

💚 Easy fixes:
✅ Glass of water right after waking (you lose water all night)
✅ Keep a bottle where you can SEE it — visibility drives the habit
✅ Drink a glass before each meal
✅ In hot weather or after sweating, add a pinch of salt + lemon to water

💬 How many glasses have you had today so far? Count and comment 👇

📌 Share this with someone who lives on tea and forgets water 😄

#HealthDaily #Hydration #DrinkWater #HealthTips #Energy #Wellness #StayHealthy"""},

{"n":5,"theme":"mint_light","title":"The Deficiency Half the World Has: Vitamin D",
 "bullets":["Low D = fatigue, low mood, weak bones","Indoor life is the main cause","15-20 min of sun helps a lot","A simple blood test tells you"],
 "cap":"""☀️ If you're always tired, moody, or getting sick often — check your vitamin D.

It's one of the most common deficiencies in the world, especially for people who work indoors. South Asia included — sunshine outside, deficiency inside.

Why it matters:
• Vitamin D powers your immune system
• Low levels are linked to fatigue, low mood, and body aches
• Your bones need it to absorb calcium — deficiency now = weak bones later

💚 What helps:
✅ 15-20 minutes of direct sun on skin (arms/face), ideally before 10 AM
✅ Foods: fatty fish, egg yolks, fortified milk
✅ If levels are low, doctors often suggest a supplement — but test first, don't guess

⚠️ Get the simple blood test (Vitamin D 25-OH) before starting high-dose supplements — more is not better.

💬 When did you last spend 15+ minutes in the sun? Today, this week, or can't remember? 👇

📌 Save & share — someone you love is probably deficient.

#HealthDaily #VitaminD #Sunshine #Immunity #HealthTips #Fatigue #Wellness"""},

{"n":6,"theme":"teal_dark","title":"Your Eyes Need the 20-20-20 Rule",
 "bullets":["Every 20 min, look 20 ft away","Hold it for 20 seconds","Blink fully — screens cut blinking 60%","Screen slightly below eye level"],
 "cap":"""👀 Eyes burning by evening? Blurry vision after work? That's digital eye strain — and most screen users have it.

The fix doctors recommend is free — the 20-20-20 rule:

⏰ Every 20 minutes
👁️ Look at something 20 feet (6 meters) away
⏱️ For at least 20 seconds

Why it works: staring at screens locks your focus muscles and cuts your blinking by more than half. Regular "distance breaks" let both reset.

💚 Bonus protection:
✅ Blink fully and often (we forget!)
✅ Screen at arm's length, top slightly below eye level
✅ Match screen brightness to the room — a bright screen in a dark room is a strain machine
✅ Dry eyes? Artificial tears help; persistent problems → eye doctor

💬 How many hours a day are you on screens? Be honest 👇

📌 Save this and share it with your work team.

#HealthDaily #EyeHealth #ScreenTime #2020Rule #HealthTips #DigitalWellness #EyeStrain"""},

{"n":7,"theme":"mint_light","title":"Cut Sugar Without Feeling Miserable",
 "bullets":["Swap drinks first — biggest win","Fruit when cravings hit","Protein breakfast kills cravings","Read labels: sugar hides in sauces"],
 "cap":"""🍬 You don't need to quit sugar overnight. You need smart swaps that don't feel like punishment:

1️⃣ Fix drinks FIRST — sugary tea, soft drinks, packaged juice are the biggest source. Swap to water, lemon water, or tea with half the sugar (then quarter). This one change beats all others.

2️⃣ Craving something sweet? Eat fruit — the fiber slows the sugar down. A banana ≠ a candy bar, no matter what anyone says.

3️⃣ Eat protein at breakfast — stable blood sugar in the morning = way fewer cravings at night.

4️⃣ Read labels — sugar hides in ketchup, sauces, bread, "healthy" cereals, flavored yogurt.

5️⃣ Don't keep it at home — you can't eat what isn't there. Willpower is for the shop, not the kitchen.

💡 Give it 2 weeks. Cravings genuinely shrink as your taste buds adjust.

💬 What's YOUR biggest sugar weakness — tea, desserts, or cold drinks? 👇

📌 Save this for the next craving.

#HealthDaily #SugarFree #HealthyEating #Nutrition #HealthTips #WeightLoss #Wellness"""},

{"n":8,"theme":"teal_dark","title":"Measuring Blood Pressure at Home? Do It Right",
 "bullets":["Sit quietly 5 min before measuring","Feet flat, back supported, arm at heart level","No tea/coffee/smoking 30 min prior","Measure same time daily, keep a log"],
 "cap":"""🩺 Home blood pressure monitors are great — but most people use them wrong, and wrong readings cause wrong decisions.

How to measure properly:

✅ Sit quietly for 5 minutes first — no phone, no talking
✅ Feet flat on floor, back supported, legs uncrossed
✅ Arm resting on a table at heart level
✅ Cuff on bare skin, not over clothes
✅ No tea, coffee, or smoking 30 minutes before
✅ Take 2 readings 1 minute apart, note both
✅ Same time every day — morning is ideal

📊 What the numbers mean (general guide):
• Below 120/80 — normal
• 120-139 / 80-89 — elevated, lifestyle attention
• 140/90+ repeatedly — see your doctor

⚠️ One high reading ≠ hypertension. Patterns over days matter — that's why the log is gold for your doctor.

💬 Do you have a BP monitor at home? When did you last check? 👇

📌 Save this checklist next to your monitor.

#HealthDaily #BloodPressure #Hypertension #HeartHealth #HealthTips #PreventiveHealth"""},

{"n":9,"theme":"mint_light","title":"The 5-Minute Stress Reset That Actually Works",
 "bullets":["Slow exhale switches off alarm mode","4-6 breathing: in 4s, out 6s","Works because it's physiology, not magic","Use before sleep or hard conversations"],
 "cap":"""😮‍💨 When stress hits, your body flips into alarm mode — racing heart, tight chest, spinning thoughts.

Here's the fastest legal way to switch it off: breathe out SLOWER than you breathe in.

The 4-6 reset:
1️⃣ Breathe in through your nose — 4 seconds
2️⃣ Breathe out slowly through your mouth — 6 seconds
3️⃣ Repeat for 5 minutes

That's it. No app, no subscription.

Why it works: a long exhale activates the vagus nerve — your body's built-in "calm down" switch. Heart rate drops within minutes. It's physiology, not a life hack.

💚 Use it:
• Before sleep (better than scrolling)
• Before difficult conversations
• Stuck in traffic
• Anytime your chest feels tight

⚠️ Ongoing overwhelming stress or anxiety? Please talk to a professional — that's strength, not weakness.

💬 Try 5 rounds right now, then tell us — feel the difference? 👇

📌 Save this for your next stressful day.

#HealthDaily #StressRelief #Breathing #MentalHealth #Calm #HealthTips #Wellness"""},

{"n":10,"theme":"teal_dark","title":"What Actually Boosts Immunity (Hint: Not Pills)",
 "bullets":["Sleep 7-8h — your #1 immune booster","Move daily, even just walking","Eat colors: fruits & vegetables","Chronic stress silently weakens defense"],
 "cap":"""🛡️ Immunity "boosters" are a billion-dollar industry. Here's the uncomfortable truth: no pill beats these four basics.

1️⃣ SLEEP — 7-8 hours. People sleeping under 6 hours are several times more likely to catch a cold after virus exposure. Sleep is when your immune system trains.

2️⃣ MOVEMENT — 30 minutes of daily walking measurably improves immune surveillance. Extreme exhaustion does the opposite — balance, not punishment.

3️⃣ FOOD — your immune cells are built from what you eat. Colorful fruits & vegetables, protein at every meal, and vitamin C from real food (guava, citrus, capsicum) beat most supplements.

4️⃣ STRESS CONTROL — chronic stress floods you with cortisol, which suppresses immune function. That's why you get sick right after your most stressful weeks.

💊 Supplements have their place (vitamin D if deficient, zinc when sick) — but they're the icing, not the cake.

💬 Which of the 4 is weakest for you right now? 👇

📌 Save & share — flu season always comes back.

#HealthDaily #Immunity #ImmuneSystem #HealthTips #Sleep #Nutrition #Wellness"""},

{"n":11,"theme":"mint_light","title":"Desk Job Destroying Your Back? Fix These 4 Things",
 "bullets":["Screen top at eye level","Elbows 90°, shoulders relaxed","Stand & move every 45 minutes","Strengthen your core, not just stretch"],
 "cap":"""🪑 Back or neck pain by evening? Your desk setup is probably attacking you 8 hours a day.

The 4 fixes that matter most:

1️⃣ Screen height — top of screen at eye level. Looking down at a laptop all day = "tech neck." A stack of books under the laptop + separate keyboard works fine.

2️⃣ Arms — elbows at ~90°, shoulders relaxed, wrists straight. If your shoulders are shrugged all day, your chair or desk height is wrong.

3️⃣ Movement — the best posture is the NEXT posture. Stand, stretch, or walk for 2 minutes every 45 minutes. Set a timer; your discipline won't do it alone.

4️⃣ Core strength — a strong core holds your spine so your back muscles don't have to. Even 5 minutes of planks + bridges daily changes things in a month.

⚠️ Pain that shoots down your leg, numbness, or weakness — that's a doctor visit, not a stretching video.

💬 Where do you feel it most — neck, lower back, or shoulders? 👇

📌 Save this and audit your desk right now.

#HealthDaily #BackPain #Posture #DeskJob #Ergonomics #HealthTips #OfficeLife"""},

{"n":12,"theme":"teal_dark","title":"Morning Sunlight: The Free Health Upgrade",
 "bullets":["Sets your body clock for the day","Makes falling asleep easier at night","Boosts morning alertness naturally","10-15 minutes outdoors is enough"],
 "cap":"""🌅 The cheapest health upgrade on earth: get sunlight in your eyes within an hour of waking.

(No, not staring at the sun — just being outside facing daylight.)

What 10-15 minutes of morning light does:

✅ Anchors your body clock — your brain marks "daytime started now"
✅ Better sleep tonight — melatonin release gets scheduled ~14-16 hours later
✅ Natural alertness — morning light triggers a healthy cortisol pulse (this is the GOOD cortisol timing)
✅ Better mood — light exposure is a core tool for low mood

☕ Best combo: morning tea/coffee on the balcony or rooftop instead of indoors. Same drink, free health upgrade.

📱 The reverse also matters: bright screens at midnight tell your brain "it's daytime" — that's why sleep gets wrecked.

💬 Do you see the sky before 9 AM most days, or does your morning start under a roof? 👇

📌 Share with the friend who can't sleep at night but never sees the morning.

#HealthDaily #MorningRoutine #Sunlight #CircadianRhythm #SleepBetter #HealthTips #Wellness"""},

{"n":13,"theme":"mint_light","title":"Fiber: The Most Underrated Nutrient",
 "bullets":["Feeds your good gut bacteria","Keeps you full — helps weight control","Steadies blood sugar & cholesterol","Most people get less than half enough"],
 "cap":"""🌾 Everyone talks protein. Almost nobody talks fiber — yet most people eat less than HALF of what they need (~25-30g/day).

What enough fiber does:

✅ Feeds good gut bacteria (they literally eat it)
✅ Keeps you full longer — natural appetite control
✅ Slows sugar absorption — steadier energy, better blood sugar
✅ Helps lower cholesterol
✅ Keeps digestion... reliable 😄

🥗 Easy ways to hit 25-30g:
• Swap white rice/bread for whole grain versions (even half the time)
• Dal/lentils — fiber powerhouses you already know
• Eat fruit whole, don't juice it — juicing throws the fiber away
• Add vegetables to every meal, not just dinner
• Snack on nuts, seeds, chickpeas

⚠️ Increase gradually + drink more water, or your stomach will file a complaint.

💬 Rate your fiber game: strong 💪, average 😐, or "mostly white rice" 😅 👇

📌 Save this and add ONE fiber source tomorrow.

#HealthDaily #Fiber #GutHealth #Nutrition #HealthyEating #HealthTips #Wellness"""},

{"n":14,"theme":"teal_dark","title":"How to Spot Ultra-Processed Food in 5 Seconds",
 "bullets":["Ingredient list longer than 5 items?","Names you can't pronounce?","Would your grandmother recognize it?","UPFs are linked to 30+ health risks"],
 "cap":"""🏭 Not all "processed" food is bad — cheese, yogurt, frozen vegetables are processed and fine.

The problem is ULTRA-processed: industrial products engineered to be irresistible. They're now linked to obesity, type 2 diabetes, heart disease, and even depression.

🔍 The 5-second test — check the ingredient list:

1️⃣ More than 5 ingredients? Suspicious.
2️⃣ Ingredients you can't pronounce or wouldn't find in a kitchen (emulsifiers, flavor enhancers, colorings)? Ultra-processed.
3️⃣ Would your grandmother recognize this as food? No? There's your answer.

Common offenders: instant noodles, chips, packaged cakes/biscuits, soft drinks, "fruit" drinks, processed meat, most breakfast cereals.

💚 The realistic goal — not perfection:
✅ Cook simple meals when you can
✅ Swap the WORST offenders first (usually drinks & snacks)
✅ 80/20 rule — mostly real food, occasional treats without guilt

💬 Which ultra-processed food would be hardest for YOU to give up? Honesty time 👇

📌 Save this for your next grocery trip.

#HealthDaily #UltraProcessedFood #HealthyEating #Nutrition #RealFood #HealthTips #Wellness"""},
]

assert len(POSTS) == 14
