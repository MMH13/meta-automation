# -*- coding: utf-8 -*-
"""Health Daily - 10 reels/day cadence, batch 1 (days 1-5).
Niches: nutrition, hydration, gut health. 4-beat reels (hook, beat, beat,
end) via image_reel_health_overlay.py's hdo_* renderers + real Pexels B-roll.
"""

REELS = [
("hd10_d1_1_protein_leftover_myth", [
 {"kind": "hook", "text": "Reheated protein\nis not\nless nutritious.", "narration": "Reheating leftover chicken or fish does not strip away its protein.", "query": "reheating food kitchen"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Protein structure\nsurvives heat\nfine.", "narration": "Protein is remarkably heat-stable, so a second round in the microwave barely changes it.", "query": "microwave food closeup"},
 {"kind": "beat", "kicker": "WHAT ACTUALLY DROPS", "text": "Some B-vitamins fade,\nnot the protein\nitself.", "narration": "What does fade a little with repeated reheating is heat-sensitive B-vitamins, not the protein.", "query": "cooked chicken meal"},
 {"kind": "end", "query": "cooked chicken meal", "text": "Leftovers are\nstill a real meal.", "question": "Meal-prepping this week?", "narration": "So leftovers are still a real, protein-complete meal, not a downgrade."},
], "Reheated chicken isn't 'worse' protein 🍗\n\nProtein is heat-stable, it survives the microwave just fine. Some B-vitamins fade slightly, but the protein content barely changes.\n\n💚 Bookmark this if you meal-prep.\n\n💬 Meal-prepping this week?"),

("hd10_d1_2_fruit_juice_whole_fruit", [
 {"kind": "hook", "text": "A glass of juice\nand a piece of fruit\naren't the same.", "narration": "A glass of orange juice and an actual orange are not nutritionally the same thing.", "query": "orange juice fruit table"},
 {"kind": "beat", "kicker": "THE FIBER GAP", "text": "Juicing removes\nmost of the fiber\nthat slows sugar.", "narration": "Juicing strips out most of the fiber that would normally slow down how fast sugar hits your blood.", "query": "juicing oranges fresh"},
 {"kind": "beat", "kicker": "QUICK FACT", "text": "Whole fruit\nfills you up\nfaster too.", "narration": "Whole fruit also fills you up faster, since you're chewing and getting the fiber alongside the sugar.", "query": "eating orange slice"},
 {"kind": "end", "query": "eating orange slice", "text": "Whole fruit wins\nmost days.", "question": "Juice or whole fruit — which do you reach for?", "narration": "Whole fruit wins on most days when you have the choice."},
], "Orange juice ≠ an orange 🍊\n\nJuicing removes most of the fiber that slows sugar absorption. Whole fruit fills you up faster and hits your blood sugar more gently.\n\n💚 Bookmark this for your next grocery run.\n\n💬 Juice or whole fruit — which do you reach for?"),

("hd10_d1_3_late_night_eating_metabolism", [
 {"kind": "hook", "text": "Eating late\ndoesn't magically\nturn into fat.", "narration": "Eating a meal late at night doesn't magically convert straight into body fat.", "query": "late night kitchen snack"},
 {"kind": "beat", "kicker": "WHAT MATTERS MORE", "text": "Total daily intake\nmatters more than\nthe clock.", "narration": "What actually matters more than the clock on the wall is your total intake across the whole day.", "query": "clock kitchen evening"},
 {"kind": "beat", "kicker": "THE REAL ISSUE", "text": "Late eating is often\njust mindless\nextra eating.", "narration": "The real issue with late-night eating is usually that it's mindless, on top of an already full day.", "query": "person eating couch night"},
 {"kind": "end", "query": "person eating couch night", "text": "Watch the plate,\nnot the clock.", "question": "Are you a late-night snacker?", "narration": "Watch what's on the plate, not just what time it is."},
], "Late-night eating doesn't 'turn into fat' 🌙\n\nYour body doesn't have a fat-storage switch that flips at 8pm. What matters more is your total intake for the day — late eating is usually just extra, mindless eating.\n\n💚 Bookmark this if you snack late.\n\n💬 Are you a late-night snacker?"),

("hd10_d1_4_hydration_thirst_lag", [
 {"kind": "hook", "text": "By the time\nyou feel thirsty,\nyou're already behind.", "narration": "By the time your brain registers thirst, you're already a little behind on fluids.", "query": "person drinking water outdoor"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Thirst lags behind\nyour actual\nfluid loss.", "narration": "The thirst signal genuinely lags behind your actual fluid loss, sometimes by an hour or more.", "query": "sweating exercise outdoor"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "Sip on a\nschedule, not\njust on thirst.", "narration": "A simple fix is sipping on a rough schedule through the day instead of waiting for thirst to remind you.", "query": "water bottle desk"},
 {"kind": "end", "query": "water bottle desk", "text": "Small sips,\nall day long.", "question": "How much water have you had today?", "narration": "Small, steady sips all day beat one big glass when you finally notice you're parched."},
], "You're thirsty AFTER you're already dehydrated 💧\n\nThirst lags behind your actual fluid loss, sometimes by an hour. Sipping on a schedule beats waiting for the signal.\n\n💚 Bookmark this as your hydration reminder.\n\n💬 How much water have you had today?"),

("hd10_d1_5_gut_lining_barrier", [
 {"kind": "hook", "text": "Your gut lining\nis one cell\nthick.", "narration": "The lining of your gut is remarkably thin, just a single layer of cells thick.", "query": "digestive system health"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "That thin layer\ndecides what enters\nyour bloodstream.", "narration": "That paper-thin layer is the checkpoint deciding what actually gets let into your bloodstream.", "query": "gut health illustration body"},
 {"kind": "beat", "kicker": "HOW TO SUPPORT IT", "text": "Fiber and fermented\nfoods help keep\nit strong.", "narration": "Fiber-rich and fermented foods are two of the simplest ways to help keep that barrier strong.", "query": "fermented food vegetables"},
 {"kind": "end", "query": "fermented food vegetables", "text": "A stronger gut\nlining, a stronger you.", "question": "Do you eat fermented foods regularly?", "narration": "A stronger gut lining tends to mean a stronger, steadier you overall."},
], "Your gut lining is just ONE cell thick 🦠\n\nThat thin layer is the checkpoint for what enters your bloodstream. Fiber and fermented foods help keep it strong.\n\n💚 Bookmark this gut-health basic.\n\n💬 Do you eat fermented foods regularly?"),

("hd10_d1_6_cooking_veggies_nutrients", [
 {"kind": "hook", "text": "Cooking veggies\ncan boost some\nnutrients.", "narration": "Cooking your vegetables can actually boost the availability of some nutrients, not just destroy them.", "query": "cooking vegetables stovetop"},
 {"kind": "beat", "kicker": "THE SCIENCE", "text": "Heat breaks down\ncell walls, freeing\nup nutrients.", "narration": "Heat breaks down tough plant cell walls, which can free up nutrients like lycopene and beta-carotene.", "query": "chopped tomatoes carrots"},
 {"kind": "beat", "kicker": "STILL TRUE", "text": "Some vitamins\ndo drop with\nlong cooking.", "narration": "It's still true that some heat-sensitive vitamins, like vitamin C, do drop with long cooking times.", "query": "steaming vegetables pot"},
 {"kind": "end", "query": "steaming vegetables pot", "text": "Mix raw\nand cooked.", "question": "Raw or cooked veggies — which do you prefer?", "narration": "Mixing raw and cooked vegetables through the week covers you either way."},
], "Cooking your veggies can boost nutrients 🥕\n\nHeat breaks down plant cell walls, freeing up nutrients like lycopene and beta-carotene. Some vitamins like C do drop with long cooking though.\n\n💚 Bookmark this before your next meal prep.\n\n💬 Raw or cooked veggies — which do you prefer?"),

("hd10_d1_7_bloating_food_combos", [
 {"kind": "hook", "text": "Bloating isn't always\nabout what\nyou ate.", "narration": "Bloating isn't always just about what you ate, sometimes it's about how fast you ate it.", "query": "stomach discomfort person"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Eating fast means\nswallowing more\nair.", "narration": "Eating quickly means you're also swallowing more air along with your food.", "query": "person eating quickly meal"},
 {"kind": "beat", "kicker": "OTHER TRIGGERS", "text": "Carbonated drinks\nand certain sugars\nadd gas too.", "narration": "Carbonated drinks and certain sugar alcohols can add extra gas on top of that.", "query": "sparkling drink glass"},
 {"kind": "end", "query": "sparkling drink glass", "text": "Slow down,\nbreathe between bites.", "question": "What usually bloats you?", "narration": "Slowing down and breathing between bites is a small habit that actually helps."},
], "Bloating isn't always about WHAT you ate 💨\n\nEating fast means swallowing more air. Carbonated drinks and certain sugar alcohols add extra gas on top.\n\n💚 Bookmark this for your next meal.\n\n💬 What usually bloats you?"),

("hd10_d1_8_water_first_thing_morning", [
 {"kind": "hook", "text": "A glass of water\nfirst thing isn't\nmagic, but it helps.", "narration": "A glass of water first thing in the morning isn't magic, but it genuinely helps.", "query": "morning water glass sunlight"},
 {"kind": "beat", "kicker": "WHY IT HELPS", "text": "You lose fluid\novernight just\nby breathing.", "narration": "You lose a surprising amount of fluid overnight just through breathing and skin.", "query": "person waking up bed"},
 {"kind": "beat", "kicker": "QUICK FACT", "text": "It kickstarts digestion\nand wakes up\nyour system.", "narration": "That first glass also helps kickstart digestion and wakes your whole system up gently.", "query": "drinking water morning kitchen"},
 {"kind": "end", "query": "drinking water morning kitchen", "text": "One habit,\nbig payoff.", "question": "Do you drink water before coffee?", "narration": "One small habit, and a genuinely solid payoff for how the rest of your morning feels."},
], "Water before coffee, every morning ☀️\n\nYou lose fluid overnight just through breathing. A glass of water first thing kickstarts digestion and wakes your system up gently.\n\n💚 Bookmark this morning reminder.\n\n💬 Do you drink water before coffee?"),

("hd10_d1_9_probiotic_food_sources", [
 {"kind": "hook", "text": "Probiotics aren't\nonly found\nin supplements.", "narration": "Probiotics aren't something you only get from a supplement bottle.", "query": "yogurt kimchi jars"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Yogurt, kimchi,\nand kefir all\ncarry live cultures.", "narration": "Everyday foods like yogurt, kimchi, and kefir all carry live, beneficial cultures naturally.", "query": "fermented food jars table"},
 {"kind": "beat", "kicker": "WHAT TO LOOK FOR", "text": "Check for\n'live active cultures'\non the label.", "narration": "When you're shopping, check the label for the phrase 'live active cultures' to know it's genuine.", "query": "reading food label grocery"},
 {"kind": "end", "query": "reading food label grocery", "text": "Food first,\nsupplement second.", "question": "What's your favorite fermented food?", "narration": "Food-first is usually the better place to start before reaching for a supplement."},
], "You don't need a pill for probiotics 🥣\n\nYogurt, kimchi, and kefir all carry live, beneficial cultures naturally. Check the label for 'live active cultures' to know it's genuine.\n\n💚 Bookmark this before your next grocery trip.\n\n💬 What's your favorite fermented food?"),

("hd10_d1_10_sugar_crash_cycle", [
 {"kind": "hook", "text": "That 3pm crash\nis often a sugar\nyou ate at lunch.", "narration": "That familiar 3pm energy crash is often traced right back to something sugary you ate at lunch.", "query": "tired person afternoon desk"},
 {"kind": "beat", "kicker": "THE CYCLE", "text": "A sugar spike\nis always followed\nby a dip.", "narration": "A sharp sugar spike is almost always followed by an equally sharp dip afterward.", "query": "sugary dessert plate"},
 {"kind": "beat", "kicker": "THE FIX", "text": "Pairing carbs\nwith protein\nsmooths the curve.", "narration": "Pairing carbs with some protein or fat at the same meal smooths that whole curve out.", "query": "balanced meal plate protein"},
 {"kind": "end", "query": "balanced meal plate protein", "text": "Balance the plate,\nskip the crash.", "question": "Do you get an afternoon energy crash?", "narration": "Balance the plate at lunch, and you can often skip the crash entirely."},
], "That 3pm crash? Look at what you had for lunch 📉\n\nA sugar spike is almost always followed by a dip. Pairing carbs with protein or fat at the same meal smooths the whole curve out.\n\n💚 Bookmark this before lunch tomorrow.\n\n💬 Do you get an afternoon energy crash?"),

("hd10_d2_1_eating_slowly_satiety", [
 {"kind": "hook", "text": "It takes about\n20 minutes to feel\nactually full.", "narration": "It takes roughly twenty minutes for your brain to register that you're actually full.", "query": "person eating slowly table"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Fullness signals\ntravel slower\nthan you eat.", "narration": "The hormones that signal fullness travel through your body slower than most people finish a fast meal.", "query": "meal table food closeup"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "Put your fork down\nbetween\nbites.", "narration": "A simple fix is putting your fork down between bites, which naturally slows the whole meal.", "query": "putting down fork plate"},
 {"kind": "end", "query": "putting down fork plate", "text": "Slower meals,\nnatural portions.", "question": "Do you eat fast or slow?", "narration": "Slower meals tend to land you at a more natural portion size, no counting needed."},
], "It takes 20 minutes to actually feel full ⏱️\n\nFullness hormones travel slower than most people finish a meal. Putting your fork down between bites naturally slows things down.\n\n💚 Bookmark this before your next meal.\n\n💬 Do you eat fast or slow?"),

("hd10_d2_2_dehydration_brain_fog", [
 {"kind": "hook", "text": "Mild dehydration\ncan feel like\nbrain fog.", "narration": "Even mild dehydration can show up as something that feels a lot like brain fog.", "query": "person concentrating work desk"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Losing just 1-2%\nof body water\naffects focus.", "narration": "Losing just one to two percent of your body's water can measurably affect focus and mood.", "query": "person tired working laptop"},
 {"kind": "beat", "kicker": "EASY CHECK", "text": "Check your\nurine color\nas a rough gauge.", "narration": "A rough, easy gauge is simply checking urine color, pale straw usually means you're doing fine.", "query": "water bottle glass desk"},
 {"kind": "end", "query": "water bottle glass desk", "text": "Water before\ncoffee, again.", "question": "Ever mistake thirst for tiredness?", "narration": "Reaching for water before coffee is often the faster fix for that foggy feeling."},
], "That brain fog might just be dehydration 🧠\n\nLosing just 1-2% of your body's water can measurably affect focus and mood. Urine color is a rough, easy gauge.\n\n💚 Bookmark this for your next slow afternoon.\n\n💬 Ever mistake thirst for tiredness?"),

("hd10_d2_3_gut_bacteria_diversity", [
 {"kind": "hook", "text": "Your gut has\ntrillions of\ndifferent bacteria.", "narration": "Your gut is home to trillions of bacteria, spanning hundreds of different species.", "query": "healthy meal variety table"},
 {"kind": "beat", "kicker": "WHY VARIETY MATTERS", "text": "More plant variety\nfeeds more\nbacteria species.", "narration": "Eating a wider variety of plants feeds a wider variety of those bacterial species.", "query": "colorful vegetables market"},
 {"kind": "beat", "kicker": "SIMPLE GOAL", "text": "Aim for 20-30\ndifferent plants\na week.", "narration": "A simple goal researchers point to is around twenty to thirty different plant foods a week.", "query": "grocery basket vegetables fruit"},
 {"kind": "end", "query": "grocery basket vegetables fruit", "text": "Variety over\nperfection.", "question": "How many different plants did you eat this week?", "narration": "Variety over perfection is the real takeaway here."},
], "Aim for 20-30 different plants a week 🌱\n\nMore plant variety feeds more species of gut bacteria. It's not about perfection, it's about variety.\n\n💚 Bookmark this weekly goal.\n\n💬 How many different plants did you eat this week?"),

("hd10_d2_4_frozen_vs_fresh_produce", [
 {"kind": "hook", "text": "Frozen vegetables\ncan be just as\nnutritious as fresh.", "narration": "Frozen vegetables can genuinely be just as nutritious as fresh ones, sometimes more so.", "query": "frozen vegetables bag"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Frozen produce\nis picked and frozen\nat peak ripeness.", "narration": "Frozen produce is typically picked and frozen at peak ripeness, locking in nutrients right away.", "query": "vegetables harvest fresh"},
 {"kind": "beat", "kicker": "COMPARE THIS", "text": "'Fresh' produce\ncan sit in transit\nfor days.", "narration": "Fresh produce labeled in stores can sit in transit and storage for days before it reaches you.", "query": "produce aisle grocery store"},
 {"kind": "end", "query": "produce aisle grocery store", "text": "Frozen is a\nsmart, cheap option.", "question": "Do you keep frozen veggies on hand?", "narration": "Frozen is a genuinely smart, budget-friendly option, not a downgrade."},
], "Frozen veggies aren't the 'lesser' option ❄️\n\nThey're picked and frozen at peak ripeness. 'Fresh' produce can actually sit in transit for days before reaching you.\n\n💚 Bookmark this before your next grocery run.\n\n💬 Do you keep frozen veggies on hand?"),

("hd10_d2_5_electrolyte_myth_sports_drinks", [
 {"kind": "hook", "text": "Most people\ndon't need a\nsports drink.", "narration": "Most people going about a normal day don't actually need a sports drink.", "query": "sports drink bottle gym"},
 {"kind": "beat", "kicker": "WHEN YOU DO", "text": "They help after\nlong, sweaty\nworkouts.", "narration": "They genuinely help after long, sweaty workouts over sixty to ninety minutes.", "query": "athlete sweating workout"},
 {"kind": "beat", "kicker": "OTHERWISE", "text": "Plain water covers\nmost daily\nhydration needs.", "narration": "Otherwise, plain water covers most people's daily hydration needs just fine.", "query": "drinking water bottle"},
 {"kind": "end", "query": "drinking water bottle", "text": "Save the sugar\nfor real sweat sessions.", "question": "Do you reach for sports drinks often?", "narration": "Save the added sugar for the days you're genuinely sweating hard."},
], "You probably don't need that sports drink 🏃\n\nThey help after long, sweaty workouts over 60-90 minutes. Otherwise, plain water covers most daily needs just fine.\n\n💚 Bookmark this before your next gym run.\n\n💬 Do you reach for sports drinks often?"),

("hd10_d2_6_skipping_meals_metabolism", [
 {"kind": "hook", "text": "Skipping one meal\nwon't 'slow down'\nyour metabolism.", "narration": "Skipping a single meal will not meaningfully slow down your metabolism.", "query": "empty plate table"},
 {"kind": "beat", "kicker": "WHAT REALLY HAPPENS", "text": "Your body just\nadjusts and moves\non fairly quickly.", "narration": "Your body simply adjusts and carries on, it's built to handle occasional gaps.", "query": "person busy day skipping meal"},
 {"kind": "beat", "kicker": "THE REAL RISK", "text": "The risk is\novereating later\nfrom being too hungry.", "narration": "The bigger risk is usually overeating later because you got too hungry to think clearly.", "query": "person eating large meal"},
 {"kind": "end", "query": "person eating large meal", "text": "Plan ahead,\nnot punish yourself.", "question": "Do you ever accidentally skip meals?", "narration": "Planning ahead beats skipping and then overcorrecting later."},
], "One skipped meal won't wreck your metabolism 🍽️\n\nYour body just adjusts and moves on. The real risk is overeating later because you got too hungry to think clearly.\n\n💚 Bookmark this for busy days.\n\n💬 Do you ever accidentally skip meals?"),

("hd10_d2_7_fiber_gut_bacteria_food", [
 {"kind": "hook", "text": "Fiber is basically\nfood for your\ngut bacteria.", "narration": "Fiber is essentially food, specifically for the bacteria living in your gut.", "query": "whole grains fiber food"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your body can't\ndigest fiber -\nyour bacteria can.", "narration": "Your own body can't actually digest fiber, but the bacteria in your gut can, and thrive on it.", "query": "beans lentils bowl"},
 {"kind": "beat", "kicker": "WHAT THEY MAKE", "text": "In return, they\nmake compounds\nthat protect your gut.", "narration": "In return, those bacteria make short-chain fatty acids that help protect your gut lining.", "query": "healthy gut illustration"},
 {"kind": "end", "query": "healthy gut illustration", "text": "Feed them well,\nthey pay it back.", "question": "Are you getting enough fiber?", "narration": "Feed them well, and they genuinely pay it back."},
], "Fiber is food for your gut bacteria, not you 🌾\n\nYour body can't digest fiber, but your gut bacteria can. In return, they make compounds that protect your gut lining.\n\n💚 Bookmark this fiber fact.\n\n💬 Are you getting enough fiber?"),

("hd10_d2_8_coffee_hydration_myth", [
 {"kind": "hook", "text": "Coffee doesn't\ndehydrate you\nthe way people think.", "narration": "Coffee doesn't actually dehydrate you the way most people have been told.", "query": "coffee cup morning table"},
 {"kind": "beat", "kicker": "THE OLD MYTH", "text": "Yes, caffeine\nis a mild\ndiuretic.", "narration": "Yes, caffeine is a mild diuretic, meaning it can make you urinate a bit more.", "query": "pouring coffee cup"},
 {"kind": "beat", "kicker": "BUT HERE'S THE THING", "text": "The fluid in\nyour coffee still\ncounts overall.", "narration": "But the fluid you're drinking in that coffee still counts toward your daily total overall.", "query": "coffee cup steam close"},
 {"kind": "end", "query": "coffee cup steam close", "text": "Your coffee\ncounts too.", "question": "How many cups of coffee do you drink daily?", "narration": "So your morning coffee genuinely counts toward hydration too."},
], "Coffee doesn't dehydrate you like you think ☕\n\nCaffeine is a mild diuretic, sure. But the fluid in your coffee still counts toward your daily total overall.\n\n💚 Bookmark this coffee myth-buster.\n\n💬 How many cups of coffee do you drink daily?"),

("hd10_d2_9_food_order_blood_sugar", [
 {"kind": "hook", "text": "The ORDER you\neat your food in\ncan change your blood sugar.", "narration": "The order you eat different foods in can genuinely change how your blood sugar responds.", "query": "plate meal vegetables protein"},
 {"kind": "beat", "kicker": "THE TRICK", "text": "Vegetables and protein\nfirst, carbs\nlast.", "narration": "Eating vegetables and protein first, then saving carbs for last, blunts the sugar spike.", "query": "salad vegetables plate"},
 {"kind": "beat", "kicker": "WHY IT WORKS", "text": "Fiber and protein\nslow how fast\nsugar hits your blood.", "narration": "The fiber and protein slow down how quickly sugar from the carbs actually hits your bloodstream.", "query": "food plate healthy meal"},
 {"kind": "end", "query": "food plate healthy meal", "text": "Same meal,\nsmarter order.", "question": "Ever tried eating your veggies first?", "narration": "Same exact meal, just a smarter order on the plate."},
], "Eat your veggies FIRST, carbs last 🥗\n\nThis order blunts your blood sugar spike. Fiber and protein slow down how fast sugar from carbs hits your bloodstream.\n\n💚 Bookmark this for your next meal.\n\n💬 Ever tried eating your veggies first?"),

("hd10_d2_10_leaky_gut_explained", [
 {"kind": "hook", "text": "'Leaky gut'\nis a real, but often\nmisunderstood, term.", "narration": "Leaky gut is a real physiological concept, but it's often misunderstood online.", "query": "digestive health illustration"},
 {"kind": "beat", "kicker": "WHAT IT MEANS", "text": "It means the gut\nlining has become\nmore permeable.", "narration": "It simply means the gut lining has become more permeable than it should normally be.", "query": "gut lining medical illustration"},
 {"kind": "beat", "kicker": "WHAT HELPS", "text": "Fiber, sleep, and\nlower stress all\nsupport that lining.", "narration": "Fiber-rich food, good sleep, and lower stress all genuinely support that lining over time.", "query": "healthy lifestyle food sleep"},
 {"kind": "end", "query": "healthy lifestyle food sleep", "text": "Support it daily,\nnot with a quick fix.", "question": "Have you heard the term 'leaky gut' before?", "narration": "It responds to daily habits, not a single quick fix."},
], "'Leaky gut' is real, but often oversimplified 🔬\n\nIt means the gut lining has become more permeable than normal. Fiber, sleep, and lower stress all genuinely support that lining.\n\n💚 Bookmark this gut-health explainer.\n\n💬 Have you heard the term 'leaky gut' before?"),

("hd10_d3_1_reading_nutrition_labels", [
 {"kind": "hook", "text": "Serving size is\nthe first thing\nto check on a label.", "narration": "The serving size is the very first thing worth checking on any nutrition label.", "query": "reading nutrition label package"},
 {"kind": "beat", "kicker": "WHY IT TRICKS PEOPLE", "text": "A 'small' bag can\nlist 2-3 servings\nper package.", "narration": "A bag that looks like one snack can actually list two or three servings hidden inside it.", "query": "snack bag chips package"},
 {"kind": "beat", "kicker": "QUICK CHECK", "text": "Multiply the numbers\nby servings if you'll\neat the whole thing.", "narration": "If you know you'll finish the whole package, just multiply the listed numbers by the servings shown.", "query": "grocery shopping label check"},
 {"kind": "end", "query": "grocery shopping label check", "text": "One extra glance\nsaves confusion.", "question": "Do you check serving sizes on labels?", "narration": "One extra glance at the label saves a lot of confusion later."},
], "That 'one bag' might actually be 3 servings 📦\n\nServing size is the first thing to check on a label. Multiply the numbers if you know you'll eat the whole thing.\n\n💚 Bookmark this before your next snack.\n\n💬 Do you check serving sizes on labels?"),

("hd10_d3_2_water_temperature_digestion", [
 {"kind": "hook", "text": "Cold water doesn't\nactually slow down\ndigestion much.", "narration": "Cold water doesn't actually slow your digestion down in any meaningful way.", "query": "cold water glass ice"},
 {"kind": "beat", "kicker": "THE OLD BELIEF", "text": "The idea was cold\nwater 'solidifies'\nfat in your stomach.", "narration": "The old belief was that cold water would somehow solidify fat sitting in your stomach.", "query": "glass water table"},
 {"kind": "beat", "kicker": "WHAT'S TRUE", "text": "Your body warms\nliquids fast, cold\nor not.", "narration": "Your body actually warms any liquid to body temperature quite quickly, regardless of how cold it started.", "query": "drinking water person"},
 {"kind": "end", "query": "drinking water person", "text": "Drink whatever\ntemperature you like.", "question": "Cold water or room temp — what's your go-to?", "narration": "Drink whatever temperature you actually enjoy, it won't hurt your digestion either way."},
], "Cold water doesn't slow digestion, that's a myth 🧊\n\nYour body warms any liquid to body temperature fast, cold or not. Drink whatever temperature you actually enjoy.\n\n💚 Bookmark this myth-buster.\n\n💬 Cold water or room temp — what's your go-to?"),

("hd10_d3_3_gut_health_mood_link", [
 {"kind": "hook", "text": "Most of your\nserotonin is made\nin your gut.", "narration": "A striking amount of your body's serotonin is actually produced in your gut, not your brain.", "query": "gut brain connection illustration"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Around 90% of it\nis made by\ngut cells.", "narration": "Roughly ninety percent of your body's serotonin is made by cells lining your digestive tract.", "query": "digestive system health illustration"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "A healthier gut\nmay support a\nsteadier mood.", "narration": "That's part of why a healthier, more balanced gut may support a steadier mood overall.", "query": "person relaxed happy outdoor"},
 {"kind": "end", "query": "person relaxed happy outdoor", "text": "Your gut and\nmood are linked.", "question": "Ever noticed food affecting your mood?", "narration": "Your gut and your mood are far more linked than most people realize."},
], "90% of your serotonin is made in your GUT 🧠\n\nNot your brain. That's part of why a healthier, more balanced gut may support a steadier mood overall.\n\n💚 Bookmark this gut-mood connection.\n\n💬 Ever noticed food affecting your mood?"),

("hd10_d3_4_healthy_fat_sources", [
 {"kind": "hook", "text": "Not all fat\ndeserves the\nbad reputation.", "narration": "Not all dietary fat deserves the bad reputation it's carried for decades.", "query": "avocado nuts olive oil"},
 {"kind": "beat", "kicker": "GOOD SOURCES", "text": "Avocado, nuts,\nolive oil, and fatty\nfish are great picks.", "narration": "Avocado, nuts, olive oil, and fatty fish are all genuinely great sources to build meals around.", "query": "salmon avocado healthy food"},
 {"kind": "beat", "kicker": "WHAT THEY DO", "text": "They help you\nabsorb vitamins\nA, D, E, and K.", "narration": "These fats also help your body actually absorb vitamins A, D, E, and K from your food.", "query": "healthy fats food variety"},
 {"kind": "end", "query": "healthy fats food variety", "text": "Fat isn't\nthe enemy.", "question": "What's your favorite healthy fat source?", "narration": "Fat, the right kind, isn't the enemy it was made out to be."},
], "Fat isn't the enemy it was made out to be 🥑\n\nAvocado, nuts, olive oil, and fatty fish help you absorb vitamins A, D, E, and K from your food.\n\n💚 Bookmark this before your next grocery run.\n\n💬 What's your favorite healthy fat source?"),

("hd10_d3_5_sparkling_water_hydration", [
 {"kind": "hook", "text": "Sparkling water\nhydrates you just\nas well as still.", "narration": "Sparkling water hydrates you just as effectively as still water does.", "query": "sparkling water glass bubbles"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "The bubbles are\njust carbon dioxide,\nnothing else.", "narration": "Those bubbles are simply dissolved carbon dioxide, they don't change how the water hydrates you.", "query": "carbonated water bottle"},
 {"kind": "beat", "kicker": "ONE CAVEAT", "text": "Watch flavored\nversions for\nadded sugar.", "narration": "The one caveat is watching flavored versions, some sneak in a surprising amount of added sugar.", "query": "flavored sparkling water can"},
 {"kind": "end", "query": "flavored sparkling water can", "text": "Plain sparkling\nis a solid choice.", "question": "Do you drink sparkling water?", "narration": "Plain sparkling water is a genuinely solid, hydrating choice."},
], "Sparkling water hydrates just as well as still 🫧\n\nThe bubbles are just carbon dioxide. Just watch flavored versions for sneaky added sugar.\n\n💚 Bookmark this hydration myth-buster.\n\n💬 Do you drink sparkling water?"),

("hd10_d3_6_meal_timing_workout", [
 {"kind": "hook", "text": "Eating too close\nto a workout can\nleave you sluggish.", "narration": "Eating a big meal too close to a workout can leave you feeling sluggish and heavy.", "query": "person pre workout meal"},
 {"kind": "beat", "kicker": "THE SWEET SPOT", "text": "A light meal\n1-2 hours before\nusually works well.", "narration": "A lighter meal about one to two hours before exercise tends to work well for most people.", "query": "athlete eating snack gym"},
 {"kind": "beat", "kicker": "WHY", "text": "Digestion competes\nwith muscles for\nblood flow.", "narration": "Digestion and working muscles are actually competing for the same blood flow at the same time.", "query": "person exercising gym"},
 {"kind": "end", "query": "person exercising gym", "text": "Time it right,\nfeel the difference.", "question": "Do you eat before or after workouts?", "narration": "Time it right, and you'll genuinely feel the difference in your workout."},
], "Big meal right before a workout? Bad idea 🏋️\n\nDigestion and working muscles compete for the same blood flow. A light meal 1-2 hours before works best.\n\n💚 Bookmark this before your next gym session.\n\n💬 Do you eat before or after workouts?"),

("hd10_d3_7_fermented_foods_variety", [
 {"kind": "hook", "text": "Not all fermented\nfoods bring the\nsame bacteria.", "narration": "Different fermented foods actually bring different strains of beneficial bacteria to the table.", "query": "kimchi sauerkraut jars"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Yogurt, kombucha,\nkimchi, and miso\nall differ.", "narration": "Yogurt, kombucha, kimchi, and miso each carry their own distinct mix of live cultures.", "query": "fermented foods variety table"},
 {"kind": "beat", "kicker": "THE TAKEAWAY", "text": "Rotating between\nthem may support\nmore diversity.", "narration": "Rotating between a few different ones through the week may support more diversity in your gut.", "query": "person eating fermented food"},
 {"kind": "end", "query": "person eating fermented food", "text": "Mix it up,\ndon't stick to one.", "question": "Which fermented food do you eat most?", "narration": "Mixing it up beats sticking to just one, no matter how good that one is."},
], "Different fermented foods = different bacteria 🥬\n\nYogurt, kombucha, kimchi, and miso each carry their own mix of live cultures. Rotating between them may support more diversity.\n\n💚 Bookmark this fermented food fact.\n\n💬 Which fermented food do you eat most?"),

("hd10_d3_8_sodium_hidden_sources", [
 {"kind": "hook", "text": "Most of your sodium\nisn't coming from\nthe salt shaker.", "narration": "Most of the sodium in a typical diet isn't coming from the salt shaker at all.", "query": "salt shaker table food"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Bread, sauces, and\ndeli meat quietly\nadd up fast.", "narration": "Everyday foods like bread, sauces, and deli meat quietly add up to most of your daily sodium.", "query": "bread deli sandwich food"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "Check labels on\nthe foods you eat\nmost often.", "narration": "A simple fix is checking labels specifically on the foods you eat most often, not occasional treats.", "query": "reading food label grocery"},
 {"kind": "end", "query": "reading food label grocery", "text": "It's the everyday\nfoods, not the shaker.", "question": "Do you check sodium on labels?", "narration": "It's the everyday staples, not the shaker on your table, doing most of the work."},
], "The salt shaker isn't your main sodium source 🧂\n\nBread, sauces, and deli meat quietly add up to most of your daily sodium. Check labels on foods you eat most often.\n\n💚 Bookmark this before your next grocery trip.\n\n💬 Do you check sodium on labels?"),

("hd10_d3_9_plant_protein_complete", [
 {"kind": "hook", "text": "You don't need\nmeat at every\nmeal for protein.", "narration": "You don't need meat at every single meal to get enough complete protein.", "query": "beans lentils quinoa bowl"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Quinoa, soy, and\nbuckwheat are\ncomplete on their own.", "narration": "Foods like quinoa, soy, and buckwheat actually contain all the essential amino acids on their own.", "query": "quinoa soy healthy food"},
 {"kind": "beat", "kicker": "EASY COMBO", "text": "Rice and beans\ntogether also\ncover the full set.", "narration": "Pairing something like rice and beans together also covers the full set of essential amino acids.", "query": "rice beans meal bowl"},
 {"kind": "end", "query": "rice beans meal bowl", "text": "Plant protein\ncan absolutely work.", "question": "Have you tried a plant-based meal this week?", "narration": "Plant protein can absolutely carry a meal on its own, no meat required."},
], "You don't need meat at every meal for protein 🌾\n\nQuinoa, soy, and buckwheat are complete proteins on their own. Rice and beans together also cover the full set.\n\n💚 Bookmark this for meatless Monday.\n\n💬 Have you tried a plant-based meal this week?"),

("hd10_d3_10_gut_healing_foods", [
 {"kind": "hook", "text": "Bone broth alone\nwon't 'heal'\nyour gut.", "narration": "Bone broth on its own is not a magic fix that will heal your gut by itself.", "query": "bone broth soup bowl"},
 {"kind": "beat", "kicker": "WHAT HELPS MORE", "text": "Consistent fiber\nand fermented food\nmatter far more.", "narration": "Consistent fiber intake and fermented foods over time matter far more than any single 'healing' food.", "query": "healthy meal fiber vegetables"},
 {"kind": "beat", "kicker": "THE REAL PATTERN", "text": "It's the pattern\nover weeks that\ncounts, not one food.", "narration": "It's the eating pattern sustained over weeks that counts, not chasing one trendy food.", "query": "healthy eating routine kitchen"},
 {"kind": "end", "query": "healthy eating routine kitchen", "text": "No single food\nis a fix-all.", "question": "Have you tried a 'gut healing' trend before?", "narration": "No single food is ever really a complete fix-all, consistency wins."},
], "Bone broth alone won't 'heal' your gut 🍲\n\nConsistent fiber and fermented foods over time matter far more. It's the pattern over weeks that counts, not one food.\n\n💚 Bookmark this gut-health reality check.\n\n💬 Have you tried a 'gut healing' trend before?"),

("hd10_d4_1_snack_ingredient_list", [
 {"kind": "hook", "text": "A short ingredient\nlist is usually a\ngood sign.", "narration": "A short, recognizable ingredient list is usually a genuinely good sign on packaged snacks.", "query": "snack package ingredients label"},
 {"kind": "beat", "kicker": "QUICK RULE", "text": "If you can't\npronounce it, ask\nwhy it's there.", "narration": "If you can't pronounce an ingredient, it's worth a quick pause to wonder why it's even there.", "query": "reading ingredients label closeup"},
 {"kind": "beat", "kicker": "NOT ALWAYS BAD", "text": "Some long names\nare just vitamins,\nnot scary at all.", "narration": "To be fair, some long scientific names are just vitamins or minerals, not anything to worry about.", "query": "vitamin supplement bottle"},
 {"kind": "end", "query": "vitamin supplement bottle", "text": "Read past\nthe front label.", "question": "Do you flip packages over to read ingredients?", "narration": "Read past the flashy front label to the actual ingredient list."},
], "Short ingredient list = usually a good sign 🏷️\n\nSome long scientific names are just vitamins, not scary. But if you can't pronounce most of it, it's worth a look.\n\n💚 Bookmark this before your next snack aisle trip.\n\n💬 Do you flip packages over to read ingredients?"),

("hd10_d4_2_hydration_skin_myth", [
 {"kind": "hook", "text": "Drinking more water\nwon't instantly fix\ndry skin.", "narration": "Drinking more water alone won't instantly fix dry, flaky skin.", "query": "person applying moisturizer skin"},
 {"kind": "beat", "kicker": "THE NUANCE", "text": "Hydration helps\noverall, but skin\nneeds a barrier too.", "narration": "Being well hydrated helps your whole body, but skin also needs an actual moisture barrier on the surface.", "query": "skincare moisturizer bottle"},
 {"kind": "beat", "kicker": "WHAT ACTUALLY HELPS SKIN", "text": "A good moisturizer\nlocks in moisture\ntopically.", "narration": "A good moisturizer works by locking moisture into the skin's surface directly, which water alone can't do.", "query": "moisturizer cream jar"},
 {"kind": "end", "query": "moisturizer cream jar", "text": "Hydrate inside\nand out.", "question": "What's your go-to for dry skin?", "narration": "Hydrating from the inside and caring for skin from the outside both genuinely matter."},
], "Water alone won't fix dry skin 💧\n\nBeing hydrated helps your whole body, but skin also needs an actual moisture barrier on the surface. Hydrate inside and out.\n\n💚 Bookmark this skin-health myth-buster.\n\n💬 What's your go-to for dry skin?"),

("hd10_d4_3_digestive_enzymes_basics", [
 {"kind": "hook", "text": "Your body already\nmakes its own\ndigestive enzymes.", "narration": "Your body already makes its own set of digestive enzymes, every single day.", "query": "digestive system illustration"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Saliva alone starts\nbreaking down food\nbefore you swallow.", "narration": "Saliva alone contains an enzyme that starts breaking down carbs before you've even swallowed.", "query": "person chewing food"},
 {"kind": "beat", "kicker": "WHAT HELPS NATURALLY", "text": "Chewing thoroughly\ngives those enzymes\nmore surface to work.", "narration": "Chewing your food thoroughly gives those natural enzymes far more surface area to actually work with.", "query": "person chewing meal slowly"},
 {"kind": "end", "query": "person chewing meal slowly", "text": "Chew more,\nhelp your system.", "question": "Do you rush your meals?", "narration": "Chewing more is a free, built-in way to help your own digestive system."},
], "Your saliva starts digesting food before you swallow 🦷\n\nYour body already makes its own digestive enzymes. Chewing thoroughly gives them more surface area to work with.\n\n💚 Bookmark this before your next meal.\n\n💬 Do you rush your meals?"),

("hd10_d4_4_added_sugar_names", [
 {"kind": "hook", "text": "Sugar hides under\nmore than 50\ndifferent names.", "narration": "Added sugar can hide on a label under more than fifty different names.", "query": "sugar packets ingredients"},
 {"kind": "beat", "kicker": "COMMON DISGUISES", "text": "Dextrose, maltose,\nand cane syrup\nare all still sugar.", "narration": "Names like dextrose, maltose, and cane syrup are all still, simply, sugar.", "query": "food label ingredients closeup"},
 {"kind": "beat", "kicker": "QUICK TIP", "text": "Anything ending in\n'-ose' is usually\na sugar.", "narration": "A handy quick tip is that most words ending in '-ose' are some form of sugar.", "query": "person reading label store"},
 {"kind": "end", "query": "person reading label store", "text": "Now you know\nwhat to look for.", "question": "Were you surprised by any of these names?", "narration": "Now you know exactly what to scan for on a busy label."},
], "Sugar hides under 50+ different names 🍬\n\nDextrose, maltose, cane syrup — all still sugar. Quick tip: anything ending in '-ose' usually is too.\n\n💚 Bookmark this label-reading cheat sheet.\n\n💬 Were you surprised by any of these names?"),

("hd10_d4_5_water_intake_formula_myth", [
 {"kind": "hook", "text": "The '8 glasses\na day' rule isn't\nactually science.", "narration": "The famous 'eight glasses a day' rule isn't actually based on solid science.", "query": "water glasses row table"},
 {"kind": "beat", "kicker": "WHERE IT CAME FROM", "text": "It traces back to\na vague, misquoted\nrecommendation.", "narration": "It traces back to a vague, widely misquoted recommendation from decades ago.", "query": "water bottle desk work"},
 {"kind": "beat", "kicker": "WHAT ACTUALLY MATTERS", "text": "Needs vary by\nbody size, climate,\nand activity level.", "narration": "Your actual needs vary quite a bit based on body size, climate, and how active you are.", "query": "person drinking water outdoor exercise"},
 {"kind": "end", "query": "person drinking water outdoor exercise", "text": "Listen to your body\nover a fixed number.", "question": "Do you track your water intake?", "narration": "Listening to your own body beats chasing one fixed number."},
], "'8 glasses a day' isn't actually science 🚱\n\nIt traces back to a vague, misquoted recommendation. Your real needs vary by body size, climate, and activity level.\n\n💚 Bookmark this hydration myth-buster.\n\n💬 Do you track your water intake?"),

("hd10_d4_6_gut_immune_connection", [
 {"kind": "hook", "text": "A huge chunk of\nyour immune system\nlives in your gut.", "narration": "A surprisingly large portion of your entire immune system is actually housed in your gut.", "query": "gut immune system illustration"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Around 70% of\nimmune cells\nline your intestines.", "narration": "Roughly seventy percent of your body's immune cells are estimated to line your intestines.", "query": "digestive system health"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "A balanced gut may\nsupport a more\nresponsive immune system.", "narration": "That's part of why a balanced, diverse gut may support a more responsive immune system overall.", "query": "healthy person immune wellness"},
 {"kind": "end", "query": "healthy person immune wellness", "text": "Gut health is\nimmune health.", "question": "Did you know your gut was that connected to immunity?", "narration": "Gut health and immune health are far more connected than most people think."},
], "70% of your immune cells live in your GUT 🛡️\n\nA balanced, diverse gut may support a more responsive immune system overall.\n\n💚 Bookmark this immune-gut connection.\n\n💬 Did you know your gut was that connected to immunity?"),

("hd10_d4_7_healthy_carbs_myth", [
 {"kind": "hook", "text": "Carbs aren't\nthe enemy people\nmake them out to be.", "narration": "Carbohydrates aren't the enemy they've been made out to be in a lot of diet trends.", "query": "whole grains bread bowl"},
 {"kind": "beat", "kicker": "THE NUANCE", "text": "Whole grains and\nrefined carbs affect\nyour body very differently.", "narration": "Whole grains and refined carbs affect your blood sugar and energy very differently from each other.", "query": "brown rice quinoa oats"},
 {"kind": "beat", "kicker": "WHAT TO LOOK FOR", "text": "Fiber content is\nthe real thing\nto check.", "narration": "Fiber content is really the thing worth checking, not just whether it's a carb at all.", "query": "whole grain bread slice"},
 {"kind": "end", "query": "whole grain bread slice", "text": "It's the type,\nnot the category.", "question": "Whole grain or refined — which do you usually pick?", "narration": "It's the type of carb that matters, not the whole category being 'bad'."},
], "Carbs aren't the enemy 🍞\n\nWhole grains and refined carbs affect your body very differently. Fiber content is the real thing to check.\n\n💚 Bookmark this carb myth-buster.\n\n💬 Whole grain or refined — which do you usually pick?"),

("hd10_d4_8_dehydration_headache_link", [
 {"kind": "hook", "text": "That random\nafternoon headache\nmight just be water.", "narration": "That random headache that shows up in the afternoon might genuinely just be a hydration issue.", "query": "person headache afternoon"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Even mild fluid loss\ncan trigger\ntension headaches.", "narration": "Even mild fluid loss can trigger the kind of tension headache that creeps up slowly.", "query": "person tired desk work"},
 {"kind": "beat", "kicker": "QUICK TEST", "text": "Drink a full glass\nand wait\n20 minutes.", "narration": "A quick, low-cost test is drinking a full glass of water and giving it about twenty minutes.", "query": "drinking water glass"},
 {"kind": "end", "query": "drinking water glass", "text": "Water before\nreaching for meds.", "question": "Do you drink water before taking painkillers?", "narration": "Worth trying water before reaching straight for the painkillers."},
], "That afternoon headache might just be water 🤕\n\nEven mild fluid loss can trigger tension headaches. Try a full glass and wait 20 minutes before reaching for meds.\n\n💚 Bookmark this for your next headache.\n\n💬 Do you drink water before taking painkillers?"),

("hd10_d4_9_probiotics_vs_prebiotics", [
 {"kind": "hook", "text": "Probiotics and\nprebiotics are\nnot the same thing.", "narration": "Probiotics and prebiotics sound alike, but they're not the same thing at all.", "query": "yogurt fiber food table"},
 {"kind": "beat", "kicker": "PROBIOTICS", "text": "Probiotics are the\nlive bacteria\nthemselves.", "narration": "Probiotics are the actual live, beneficial bacteria, found in things like yogurt and kefir.", "query": "yogurt kefir jars"},
 {"kind": "beat", "kicker": "PREBIOTICS", "text": "Prebiotics are the\nfiber that feeds\nthose bacteria.", "narration": "Prebiotics are the fiber, found in foods like garlic and onions, that feeds those bacteria.", "query": "garlic onion vegetables"},
 {"kind": "end", "query": "garlic onion vegetables", "text": "You genuinely\nneed both.", "question": "Did you know the difference before this?", "narration": "You genuinely need both working together for a healthy gut."},
], "Probiotics ≠ Prebiotics — know the difference 🧬\n\nProbiotics are the live bacteria (yogurt, kefir). Prebiotics are the fiber that feeds them (garlic, onions). You need both.\n\n💚 Bookmark this before your next grocery trip.\n\n💬 Did you know the difference before this?"),

("hd10_d4_10_mindless_snacking_triggers", [
 {"kind": "hook", "text": "Most mindless\nsnacking is triggered\nby boredom, not hunger.", "narration": "Most mindless snacking is actually triggered by boredom or stress, not real hunger.", "query": "person snacking couch tv"},
 {"kind": "beat", "kicker": "QUICK CHECK", "text": "Ask yourself if\nan apple sounds\ngood right now.", "narration": "A quick, honest check is asking yourself if a plain apple would actually sound appealing right now.", "query": "apple fruit snack"},
 {"kind": "beat", "kicker": "IF THE ANSWER IS NO", "text": "You're probably\nbored, not\nactually hungry.", "narration": "If the answer is no, you're probably bored or stressed, not genuinely hungry.", "query": "person distracted phone"},
 {"kind": "end", "query": "person distracted phone", "text": "Name the feeling\nbefore the fridge.", "question": "Do you snack out of boredom?", "narration": "Naming the feeling before opening the fridge changes a lot."},
], "The 'would an apple sound good?' test 🍎\n\nIf the answer is no, you're probably bored or stressed, not actually hungry. Name the feeling before the fridge.\n\n💚 Bookmark this snacking check-in.\n\n💬 Do you snack out of boredom?"),

("hd10_d5_1_calorie_quality_myth", [
 {"kind": "hook", "text": "Not all calories\nhit your body\nthe exact same way.", "narration": "Not all calories affect your body in exactly the same way, despite the same number on the label.", "query": "food variety table meal"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "200 calories of\nsoda and 200 of\nalmonds behave differently.", "narration": "Two hundred calories from soda and two hundred from almonds trigger very different responses in your body.", "query": "almonds soda comparison"},
 {"kind": "beat", "kicker": "THE DIFFERENCE", "text": "Fiber, protein, and\nfat slow absorption\nand fill you up.", "narration": "Fiber, protein, and fat all slow absorption and help you actually feel full, unlike sugar alone.", "query": "healthy food fiber protein"},
 {"kind": "end", "query": "healthy food fiber protein", "text": "Quality shapes\nhow calories feel.", "question": "Do you think about calorie quality or just the number?", "narration": "Quality genuinely shapes how those calories feel and behave in your body."},
], "200 calories of soda ≠ 200 calories of almonds 🥜\n\nFiber, protein, and fat slow absorption and fill you up. Calorie quality shapes how they actually behave in your body.\n\n💚 Bookmark this nutrition myth-buster.\n\n💬 Do you think about calorie quality or just the number?"),

("hd10_d5_2_hydration_exercise_timing", [
 {"kind": "hook", "text": "Hydrating starts\nbefore your workout,\nnot during it.", "narration": "Good hydration actually starts before your workout even begins, not once you're already sweating.", "query": "person drinking water gym"},
 {"kind": "beat", "kicker": "THE SIMPLE RULE", "text": "A glass or two\n1-2 hours\nbeforehand helps.", "narration": "A glass or two of water about one to two hours beforehand sets you up much better.", "query": "water bottle gym bag"},
 {"kind": "beat", "kicker": "DURING THE WORKOUT", "text": "Small sips are\nbetter than\nbig gulps.", "narration": "Small, steady sips during the workout are gentler on your stomach than big gulps.", "query": "athlete drinking water break"},
 {"kind": "end", "query": "athlete drinking water break", "text": "Start hydrated,\nstay hydrated.", "question": "When do you usually drink water around workouts?", "narration": "Start already hydrated, and staying that way through the workout is much easier."},
], "Hydration starts BEFORE your workout, not during 💦\n\nA glass or two 1-2 hours beforehand sets you up better. Small sips during beat big gulps.\n\n💚 Bookmark this before your next workout.\n\n💬 When do you usually drink water around workouts?"),

("hd10_d5_3_gut_reset_myth", [
 {"kind": "hook", "text": "There's no such\nthing as a\n3-day 'gut reset'.", "narration": "There's no real, science-backed version of a three-day gut reset that magically fixes everything.", "query": "healthy food cleanse juice"},
 {"kind": "beat", "kicker": "WHY IT SOUNDS APPEALING", "text": "Trendy 'cleanses'\npromise a fast,\ndramatic fix.", "narration": "Trendy cleanses promise a fast, dramatic fix, which is exactly why they're appealing.", "query": "juice cleanse bottles"},
 {"kind": "beat", "kicker": "WHAT ACTUALLY WORKS", "text": "Gut bacteria shift\nmeaningfully over\nweeks, not days.", "narration": "Your gut bacteria composition genuinely shifts meaningfully over weeks of consistent eating, not a few days.", "query": "healthy meal week variety"},
 {"kind": "end", "query": "healthy meal week variety", "text": "Consistency beats\nany quick cleanse.", "question": "Have you ever tried a 'gut reset' program?", "narration": "Consistency over weeks beats any quick cleanse every single time."},
], "There's no such thing as a 3-day 'gut reset' 🚫\n\nGut bacteria shift meaningfully over weeks of consistent eating, not days. Consistency beats any quick cleanse.\n\n💚 Bookmark this before buying a 'cleanse'.\n\n💬 Have you ever tried a 'gut reset' program?"),

("hd10_d5_4_omega6_omega3_balance", [
 {"kind": "hook", "text": "Most modern diets\nhave way more\nomega-6 than omega-3.", "narration": "Most modern diets lean heavily toward omega-6 fats, with far less omega-3 than is ideal.", "query": "salmon fish omega healthy food"},
 {"kind": "beat", "kicker": "WHERE OMEGA-6 HIDES", "text": "Vegetable oils and\nprocessed foods\nare loaded with it.", "narration": "Vegetable oils and a lot of processed, packaged foods are quietly loaded with omega-6.", "query": "cooking oil bottle kitchen"},
 {"kind": "beat", "kicker": "SIMPLE BALANCE", "text": "Fatty fish, walnuts,\nand flaxseed help\ntip the scale back.", "narration": "Adding fatty fish, walnuts, and flaxseed a few times a week helps tip that balance back.", "query": "walnuts flaxseed healthy food"},
 {"kind": "end", "query": "walnuts flaxseed healthy food", "text": "Small swaps,\nbetter balance.", "question": "Do you eat fatty fish regularly?", "narration": "A few small swaps a week make a real, measurable difference."},
], "Your omega-3 to omega-6 ratio is probably off 🐟\n\nVegetable oils and processed foods are loaded with omega-6. Fatty fish, walnuts, and flaxseed help balance it back.\n\n💚 Bookmark this before your next meal plan.\n\n💬 Do you eat fatty fish regularly?"),

("hd10_d5_5_water_vs_other_drinks", [
 {"kind": "hook", "text": "Not every drink\nhydrates you\nequally well.", "narration": "Not every drink hydrates you equally, even though they're all technically liquid.", "query": "drinks variety table"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Alcohol and high-sugar\ndrinks can actually\npull water out of you.", "narration": "Alcohol and very sugary drinks can actually pull water out of your body faster than they put it in.", "query": "sugary drinks soda cans"},
 {"kind": "beat", "kicker": "BEST BETS", "text": "Plain water, milk,\nand herbal tea\nhydrate reliably.", "narration": "Plain water, milk, and herbal tea are reliable, straightforward choices for real hydration.", "query": "herbal tea water milk"},
 {"kind": "end", "query": "herbal tea water milk", "text": "Check what's\nactually in your glass.", "question": "What's your most-consumed drink besides water?", "narration": "Worth checking what's actually in your glass most days."},
], "Not every drink hydrates you equally 🥤\n\nAlcohol and very sugary drinks can pull water out faster than they put it in. Water, milk, and herbal tea are reliable choices.\n\n💚 Bookmark this hydration guide.\n\n💬 What's your most-consumed drink besides water?"),

("hd10_d5_6_digestion_time_foods", [
 {"kind": "hook", "text": "Different foods\ntake very different\ntimes to digest.", "narration": "Different foods can take dramatically different amounts of time to fully digest.", "query": "meal food variety plate"},
 {"kind": "beat", "kicker": "FAST", "text": "Fruit can pass\nthrough in as\nlittle as 30 minutes.", "narration": "Fruit alone can pass through your stomach in as little as thirty minutes.", "query": "fresh fruit bowl"},
 {"kind": "beat", "kicker": "SLOW", "text": "Fatty, protein-heavy\nmeals can take\nseveral hours.", "narration": "Fatty, protein-heavy meals can take several hours to fully move through your system.", "query": "steak protein meal plate"},
 {"kind": "end", "query": "steak protein meal plate", "text": "Timing your meals\nmakes more sense now.", "question": "Ever notice some meals sit heavier than others?", "narration": "That's exactly why some meals sit a lot heavier than others."},
], "Fruit digests in 30 min, a heavy meal takes hours ⏳\n\nFatty, protein-heavy meals take several hours to move through your system. That's why some meals sit heavier.\n\n💚 Bookmark this digestion timing fact.\n\n💬 Ever notice some meals sit heavier than others?"),

("hd10_d5_7_nutrient_timing_myth", [
 {"kind": "hook", "text": "The '30-minute\nanabolic window'\nis mostly overhyped.", "narration": "The famous thirty-minute post-workout anabolic window is largely overhyped for most people.", "query": "post workout protein shake"},
 {"kind": "beat", "kicker": "WHAT RESEARCH SHOWS", "text": "Your muscles stay\nreceptive to protein\nfor hours, not minutes.", "narration": "Research actually shows your muscles stay receptive to protein for hours after exercise, not just minutes.", "query": "gym workout recovery"},
 {"kind": "beat", "kicker": "WHAT MATTERS MORE", "text": "Total daily protein\nmatters far more\nthan exact timing.", "narration": "Your total protein intake across the whole day matters far more than hitting an exact window.", "query": "protein food variety meal"},
 {"kind": "end", "query": "protein food variety meal", "text": "Relax the timing,\nfocus on the total.", "question": "Do you rush a protein shake after workouts?", "narration": "Relax on the exact timing and focus on your total for the day instead."},
], "The post-workout 'anabolic window' is overhyped ⏱️\n\nYour muscles stay receptive to protein for hours, not minutes. Total daily protein matters far more than exact timing.\n\n💚 Bookmark this fitness myth-buster.\n\n💬 Do you rush a protein shake after workouts?"),

("hd10_d5_8_bloating_carbonation", [
 {"kind": "hook", "text": "Carbonated drinks\ncan trap gas in\nyour stomach fast.", "narration": "Carbonated drinks can trap a surprising amount of gas in your stomach quite quickly.", "query": "carbonated drink glass bubbles"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Each sip adds\ntiny bubbles that\nneed to escape.", "narration": "Every sip adds tiny bubbles of carbon dioxide that eventually need somewhere to go.", "query": "sparkling drink pouring glass"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "Sipping slowly\ngives gas time\nto escape gradually.", "narration": "Sipping slowly instead of gulping gives that gas time to escape gradually instead of building up.", "query": "person sipping drink slowly"},
 {"kind": "end", "query": "person sipping drink slowly", "text": "Slow sips,\nless bloat.", "question": "Do carbonated drinks bloat you?", "narration": "Slower sips genuinely mean less bloat afterward."},
], "Carbonated drinks trap gas fast if you gulp them 🫧\n\nEach sip adds tiny bubbles that need to escape. Sipping slowly gives that gas time to escape gradually.\n\n💚 Bookmark this before your next fizzy drink.\n\n💬 Do carbonated drinks bloat you?"),

("hd10_d5_9_gut_brain_axis_stress", [
 {"kind": "hook", "text": "Stress can\nliterally change\nyour gut bacteria.", "narration": "Chronic stress can literally shift the balance of bacteria living in your gut.", "query": "stressed person gut connection"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your gut and brain\ntalk constantly\nthrough the vagus nerve.", "narration": "Your gut and brain are in constant two-way communication through a nerve called the vagus nerve.", "query": "nervous system brain illustration"},
 {"kind": "beat", "kicker": "WHAT HELPS", "text": "Calming activities\ncan genuinely support\ngut balance too.", "narration": "Calming activities like slow breathing or a short walk can genuinely support your gut balance too.", "query": "person relaxing breathing calm"},
 {"kind": "end", "query": "person relaxing breathing calm", "text": "Calm mind,\ncalmer gut.", "question": "Have you noticed stress affecting your digestion?", "narration": "A calmer mind really does tend to mean a calmer gut."},
], "Stress can literally shift your gut bacteria 🧘\n\nYour gut and brain talk constantly through the vagus nerve. Calming activities genuinely support gut balance too.\n\n💚 Bookmark this stress-gut connection.\n\n💬 Have you noticed stress affecting your digestion?"),

("hd10_d5_10_eating_mindfully_habit", [
 {"kind": "hook", "text": "Eating without\nyour phone changes\nhow much you eat.", "narration": "Eating without a phone or screen in front of you genuinely changes how much you end up eating.", "query": "person eating without phone"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Distracted eating\nmakes it harder to\nnotice fullness cues.", "narration": "Distracted eating makes it noticeably harder for your brain to pick up on natural fullness cues.", "query": "person eating phone distracted"},
 {"kind": "beat", "kicker": "SIMPLE PRACTICE", "text": "Just one meal a day,\nscreen-free, is\na strong start.", "narration": "Starting with just one screen-free meal a day is a genuinely strong, doable place to start.", "query": "family meal table together"},
 {"kind": "end", "query": "family meal table together", "text": "One mindful meal\na day counts.", "question": "Could you try one screen-free meal today?", "narration": "One mindful, screen-free meal a day counts for more than people expect."},
], "Eating with your phone changes how much you eat 📵\n\nDistracted eating makes it harder to notice fullness cues. One screen-free meal a day is a strong start.\n\n💚 Bookmark this mindful-eating tip.\n\n💬 Could you try one screen-free meal today?"),
]
