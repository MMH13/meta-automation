# -*- coding: utf-8 -*-
"""Health Daily — 30-day queue refill, 7 posts/day (2026-08-08 -> 2026-09-06),
continuing right after the existing queue's Aug 7 tail. 6 image cards (each
mirrored to FB photo + IG image) + 1 FB text check-in per day, same proven
format as aug_health.py (value-formula captions, save-CTA, comment-bait
question). 70 unique items across 7 content pools, cycled across 30 days —
each item repeats ~3x over the month. All original, general-audience-safe
health content (hydration, sleep, food, movement, myth-busting) — no
prescription-level claims."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_health_light import health_fact, health_myth_fact

IMG = mkdir("images/health_refill1")
SAVE = "\n\n💚 Bookmark this. You'll need it later."

# ---------------------------------------------------------------- morning
# (text, kicker, emoji, caption)
MORNING = [
 ("Open the curtains\n*right after* you wake up.", "MORNING TIP", "☀️",
  "☀️ Natural light within minutes of waking is the strongest signal your body clock reads all day — it steadies your energy and helps you fall asleep easier tonight.\n\n→ Open curtains before you check your phone\n→ Even a cloudy sky counts\n→ Balcony or window, 2 minutes is enough" + SAVE + "\n💬 First thing you do after opening your eyes? 👇"),
 ("Eat breakfast within\n*90 minutes* of waking.", "MORNING TIP", "🍳",
  "🍳 Skipping breakfast for hours often backfires by lunchtime — you overeat, reach for sugar, or crash by 11. Eating within 90 minutes keeps blood sugar (and mood) steadier all morning.\n\n→ Doesn't need to be big, just balanced\n→ Protein + fiber beats plain toast\n→ Intermittent fasting? Fine — just don't skip the plan entirely" + SAVE + "\n💬 What time was your first bite today? 👇"),
 ("Do 10 squats\nbefore checking your phone.", "MORNING TIP", "🦵",
  "🦵 Ten squats sounds small, but it wakes up circulation and muscle before your brain even reaches for the scroll. A genuinely better start than the news feed.\n\n→ Bodyweight only, no equipment needed\n→ Takes under 60 seconds\n→ Try it right when the alarm goes off" + SAVE + "\n💬 Would you actually try this tomorrow? 👇"),
 ("Make your bed —\nit's a *tiny win* before 8 AM.", "MORNING TIP", "🛏️",
  "🛏️ It sounds trivial, but one completed task before you've even left the bedroom sets a 'today I follow through' tone for everything after.\n\n→ Takes under 2 minutes\n→ You return to a calmer room tonight too\n→ Small wins compound — this is the cheapest one there is" + SAVE + "\n💬 Bed made or not today? Honest 👇"),
 ("Skip the snooze button.\nIt *fragments* your last sleep cycle.", "MORNING TIP", "⏰",
  "⏰ Those extra 9 minutes don't add real rest — they interrupt a fresh sleep cycle you'll never finish, which is why snoozing often leaves you groggier than just getting up.\n\n→ Move the alarm across the room\n→ One alarm, no snooze, no negotiating\n→ You'll actually feel more awake, not less" + SAVE + "\n💬 Snooze addict or one-alarm person? 👇"),
 ("Plan your day\nin *3 lines*, not a list of 20.", "MORNING TIP", "📝",
  "📝 A 20-item to-do list guarantees you'll feel behind by 10 AM. Three real priorities, written down, actually get done — and everything else fits around them.\n\n→ Write the 3 before you open email\n→ Everything else is 'if time allows'\n→ Finishing 3 beats starting 20" + SAVE + "\n💬 How many things are actually on today's list? 👇"),
 ("Stretch your spine\nbefore you reach for coffee.", "MORNING TIP", "🧘",
  "🧘 Hours lying down leave your spine stiff — a slow stretch before caffeine wakes up circulation the way coffee alone can't.\n\n→ Reach up, twist gently side to side\n→ 60 seconds is plenty\n→ Do it standing right by the bed" + SAVE + "\n💬 Stiff mornings or loose? 👇"),
 ("Eat *protein*\nin your first meal.", "MORNING TIP", "🥚",
  "🥚 A carb-only breakfast spikes blood sugar fast, then drops it — hello 11 AM cravings. Protein flattens that curve and keeps you full for hours.\n\n→ Eggs, yogurt, dal, nuts, paneer\n→ Aim for a palm-sized portion\n→ Works at 7 AM or noon, whenever you eat first" + SAVE + "\n💬 What was your first meal today? 👇"),
 ("Say one thing\nyou're *looking forward to* today.", "MORNING TIP", "💭",
  "💭 Naming one good thing before the day starts primes your brain to actually notice it when it happens — a small habit with a real mood payoff.\n\n→ Doesn't have to be big\n→ 'Lunch with a friend' counts\n→ Say it out loud, not just in your head" + SAVE + "\n💬 What's your one thing today? 👇"),
 ("Walk while\nyour coffee brews.", "MORNING TIP", "🚶",
  "🚶 Those 3-4 minutes you'd spend staring at the coffee maker are free movement time — small, but it adds up over a year of mornings.\n\n→ Around the kitchen counts\n→ Stairs if you have them\n→ Pairs naturally with a habit you already do" + SAVE + "\n💬 Would you try this tomorrow? 👇"),
]

# ------------------------------------------------------------------- myth
# (myth, fact, caption)
MYTH = [
 ("Detox teas and juices\nclean out your body.",
  "Your liver and kidneys detox 24/7 — no tea speeds that up. Most 'detox' effects are just from cutting sugar and processed food, not the tea itself.",
  "🍵 'Detox tea' is one of the most successful myths ever marketed. Your organs already do this job continuously — what actually changes is that you're drinking less soda that week.\n\n→ Save the money\n→ Water + real food does the same job\n→ If it works, it's usually the diet change, not the tea" + SAVE + "\n💬 Ever tried a 'detox' product? 👇"),
 ("You need 8 glasses\nof water a day, exactly.",
  "8 glasses is a rough average, not a rule. Needs vary by body size, activity, and climate — thirst and pale urine are better guides than a fixed number.",
  "💧 The '8 glasses' rule is a decades-old estimate, not a medical law. Someone active in a hot climate needs more; someone smaller and sedentary may need less.\n\n→ Pale yellow urine = well hydrated\n→ Thirst is a real signal, not a failure\n→ Food (fruit, soup) counts toward intake too" + SAVE + "\n💬 Do you track your water or just drink when thirsty? 👇"),
 ("Cracking your knuckles\ncauses arthritis.",
  "Studies comparing knuckle-crackers to non-crackers found no link to arthritis. The sound is just gas bubbles releasing in the joint fluid.",
  "🖐️ Grandma's warning doesn't hold up under research — knuckle cracking hasn't been shown to cause arthritis. It might annoy people nearby, but it's harmless.\n\n→ The sound is gas releasing, not bone damage\n→ Multiple studies found no arthritis link\n→ Still, if it hurts, that's a different signal — stop" + SAVE + "\n💬 Are you a knuckle-cracker? 👇"),
 ("You lose most of your\nbody heat through your head.",
  "You lose heat through any exposed skin roughly proportional to surface area. The head-heat myth came from a flawed old military study.",
  "🧢 The '40% heat loss through your head' claim traces back to a poorly designed study decades ago. Cover whatever skin is exposed — hands, neck, head — heat loss follows surface area, not one special body part.\n\n→ A scarf matters as much as a hat\n→ Gloves and warm socks count too\n→ Old myth, still repeated everywhere" + SAVE + "\n💬 Did you believe this one? 👇"),
 ("Reading in dim light\nruins your eyesight.",
  "Dim light causes temporary eye strain — headaches, tiredness — but no lasting damage. It just makes reading less comfortable, not dangerous.",
  "📖 Reading in low light feels uncomfortable, but it doesn't cause permanent vision damage — it's simply less pleasant on tired eyes.\n\n→ Strain, not injury, is the real effect\n→ Better lighting just makes it easier\n→ Regular eye checkups matter far more" + SAVE + "\n💬 Do you read on your phone in bed with lights off? 👇"),
 ("Going outside with\nwet hair gives you a cold.",
  "Colds are caused by viruses, not temperature. You can get more exposed to viruses indoors in winter crowds than from wet hair outside.",
  "🌧️ Being cold doesn't cause a cold — a virus does. Winter colds spike because people crowd indoors more, sharing viruses, not because anyone's hair was wet.\n\n→ Wet hair outside: uncomfortable, not dangerous\n→ Hand-washing matters more than hair-drying\n→ Cold weather can weaken immune response slightly, but it's not the direct cause" + SAVE + "\n💬 Were you told this growing up too? 👇"),
 ("Microwaving food\ndestroys all its nutrients.",
  "Microwaving actually preserves more nutrients than boiling in many cases — shorter cook time and less water contact means less nutrient loss.",
  "🍲 Microwaves get an unfair reputation. Because they cook fast with little added water, they often retain more vitamins than boiling — which leaches nutrients into the water you pour away.\n\n→ Steaming and microwaving are actually gentle methods\n→ Overcooking (any method) is the real nutrient-killer\n→ Convenience doesn't mean 'less healthy' here" + SAVE + "\n💬 Do you avoid the microwave for this reason? 👇"),
 ("You should always\nstretch before exercising.",
  "Static stretching before exercise can actually reduce power output. A dynamic warm-up (light movement) is better prep than holding stretches cold.",
  "🏃 Holding a stretch on cold muscles before a workout can temporarily reduce strength and power. Dynamic movement — leg swings, arm circles, a light jog — warms up the body better.\n\n→ Save static stretching for after\n→ Dynamic warm-up = movement, not holding\n→ 5 minutes of light cardio beats 5 minutes of static stretching pre-workout" + SAVE + "\n💬 How do you usually warm up? 👇"),
 ("Natural sugar (honey, fruit)\nis totally different from table sugar.",
  "Chemically, your body processes fructose and glucose from honey/fruit similarly to table sugar. The real advantage of fruit is the fiber and nutrients that come with it.",
  "🍯 'Natural' sugar isn't magically metabolized differently — your body sees sugar as sugar. What makes fruit better than candy is the fiber, water, and vitamins that come bundled with it, slowing absorption.\n\n→ Whole fruit > fruit juice (fiber matters)\n→ Honey is still sugar, just with trace nutrients\n→ Moderation applies to 'natural' sugar too" + SAVE + "\n💬 Did this one surprise you? 👇"),
 ("You must poop\nevery single day to be healthy.",
  "Normal bowel frequency ranges from 3 times a day to 3 times a week, depending on the person. Consistency for YOUR body matters more than a daily rule.",
  "🚽 There's no universal rule requiring a daily bowel movement. What matters is what's normal and consistent for your own body — a real, sudden change is the actual signal to watch, not the calendar.\n\n→ Range of 'normal' is wider than most think\n→ Fiber + water help keep things regular\n→ A real change in pattern is worth mentioning to a doctor" + SAVE + "\n💬 Did you know the range was that wide? 👇"),
]

# ------------------------------------------------------------- didyouknow
DIDYOUKNOW = [
 ("Your *bones* are constantly\nrebuilding — a new skeleton\nroughly every 10 years.", "DID YOU KNOW?", "🦴",
  "🦴 Bone tissue is constantly being broken down and rebuilt — which is why weight-bearing movement (walking, lifting) matters at every age, not just for athletes.\n\n→ Movement signals bones to stay strong\n→ Calcium + vitamin D support the rebuild\n→ Bone density peaks in your 20s-30s, so build it early" + SAVE + "\n💬 Do you do any weight-bearing exercise? 👇"),
 ("*Laughing* lowers stress\nhormones measurably within\nminutes.", "DID YOU KNOW?", "😂",
  "😂 A real laugh measurably drops cortisol (your stress hormone) within minutes — which is why a funny video sometimes helps more than 'trying to calm down.'\n\n→ It's a genuine physiological reset, not just a mood thing\n→ Even forced laughter has some effect\n→ Cheap, fast, and completely free" + SAVE + "\n💬 What's the last thing that made you really laugh? 👇"),
 ("Your *sense of smell*\nis directly wired to\nmemory and emotion.", "DID YOU KNOW?", "👃",
  "👃 Smell is the only sense with a direct line to your brain's memory and emotion centers — which is why one specific smell can instantly bring back a whole memory.\n\n→ This is why scent-based memories feel so vivid\n→ It's also linked to appetite and mood\n→ Try it: a familiar smell can genuinely calm you down" + SAVE + "\n💬 What smell instantly takes you back somewhere? 👇"),
 ("*Standing* burns meaningfully\nmore calories than sitting,\nover a full day.", "DID YOU KNOW?", "🧍",
  "🧍 Standing burns more calories than sitting — not dramatically per minute, but across a full workday it adds up meaningfully. Small shifts, real difference.\n\n→ Standing desk or just standing calls\n→ Set a timer to stand every hour\n→ Movement breaks matter more than one intense workout" + SAVE + "\n💬 Do you sit most of the day? 👇"),
 ("Your *heart* beats about\n100,000 times a day\nwithout you noticing once.", "DID YOU KNOW?", "❤️",
  "❤️ About 100,000 heartbeats a day, entirely on autopilot — one of the best reminders that your body is doing enormous work you never consciously notice.\n\n→ Cardio fitness makes each beat more efficient\n→ Resting heart rate is a good fitness signal\n→ Small daily movement supports this system quietly" + SAVE + "\n💬 Do you know your resting heart rate? 👇"),
 ("*Chewing gum* can improve\nfocus and alertness in\nshort bursts.", "DID YOU KNOW?", "🦷",
  "🦷 A few minutes of chewing gum has been linked to short bursts of improved alertness and focus — a small, real effect, not just a placebo feeling.\n\n→ Sugar-free is the better choice\n→ Useful for a mid-afternoon focus dip\n→ Not a replacement for actual sleep, just a small boost" + SAVE + "\n💬 Would you try this at your next slump? 👇"),
 ("Your *skin* is your\nlargest organ — and it\nrenews itself monthly.", "DID YOU KNOW?", "🧴",
  "🧴 Skin renews itself roughly every month — old cells shed, new ones form. Part of why consistent habits (sleep, water, less sugar) show results over weeks, not overnight.\n\n→ Give any skin routine at least 4-6 weeks\n→ Sun protection matters daily, not just summer\n→ Hydration from inside shows up outside too" + SAVE + "\n💬 How long do you usually give a new routine? 👇"),
 ("*Cold exposure* (even a cool\nshower) can boost alertness\nfaster than caffeine.", "DID YOU KNOW?", "🚿",
  "🚿 A short burst of cold water can spike alertness faster than a cup of coffee — no caffeine crash afterward either.\n\n→ Even 20-30 seconds at the end of a shower counts\n→ It's a genuine nervous-system reset\n→ Great for an afternoon slump without more caffeine" + SAVE + "\n💬 Could you handle a cold shower finish? 👇"),
 ("*Yawning* helps cool\nyour brain, not just\nsignal tiredness.", "DID YOU KNOW?", "🥱",
  "🥱 Yawning isn't only about tiredness — one theory is it helps cool the brain and increase alertness, which is why you sometimes yawn when you're bored, not sleepy.\n\n→ Contagious yawning is linked to empathy, oddly enough\n→ Frequent yawning can also mean you need more sleep\n→ Either way, it's your body doing quiet maintenance" + SAVE + "\n💬 Did you just yawn reading this? 👇"),
 ("Your *gut* has its own\nnervous system — nearly\n500 million neurons.", "DID YOU KNOW?", "🦠",
  "🦠 Your gut has almost 500 million neurons of its own — enough that scientists call it the 'second brain.' It's a real part of why stress and digestion are so connected.\n\n→ This is the gut-brain connection in action\n→ Fiber and fermented foods support this system\n→ Stress genuinely shows up in your stomach first for many people" + SAVE + "\n💬 Does stress hit your stomach first for you? 👇"),
]

# --------------------------------------------------------------------food
FOOD = [
 ("*Walnuts* — one of the best\nplant sources of\nomega-3 fats.", "FOOD SPOTLIGHT", "🌰",
  "🌰 A small handful of walnuts covers a meaningful chunk of your daily plant-based omega-3s — genuinely good for heart and brain health.\n\n→ A small handful (not a bowlful) is the right portion\n→ Great plain or in oatmeal/salad\n→ One of the best snacks if you're not eating fish" + SAVE + "\n💬 Do you snack on nuts or reach for chips? 👇"),
 ("*Turmeric* — a compound\nlinked to lower\ninflammation.", "FOOD SPOTLIGHT", "🟡",
  "🟡 Curcumin, the active compound in turmeric, is linked to lower inflammation markers — though your body absorbs it far better with a little black pepper and fat.\n\n→ Pair with black pepper for real absorption\n→ Cooked into food works better than a pinch in water\n→ Not a cure-all, but a genuinely useful everyday spice" + SAVE + "\n💬 Turmeric milk — do you drink it? 👇"),
 ("*Garlic* — supports heart\nhealth when eaten\nregularly, raw or cooked.", "FOOD SPOTLIGHT", "🧄",
  "🧄 Regular garlic intake is linked to better heart-health markers — and it works both raw and cooked, though raw has a slightly stronger effect.\n\n→ Crushing it and letting it sit 10 min boosts the active compound\n→ Cooked garlic is gentler but still beneficial\n→ Small, consistent amounts beat an occasional large dose" + SAVE + "\n💬 Heavy-handed with garlic in your cooking? 👇"),
 ("*Sweet potato* — steady energy\nplus more vitamin A\nthan most vegetables.", "FOOD SPOTLIGHT", "🍠",
  "🍠 Sweet potato gives slow-release energy plus more vitamin A than most vegetables on your plate — genuinely one of the best-value carbs out there.\n\n→ Keep the skin on for extra fiber\n→ Roasted or boiled, both work\n→ A smarter side than plain white rice most days" + SAVE + "\n💬 Sweet potato or regular potato — pick one 👇"),
 ("*Chickpeas* — cheap plant\nprotein with fiber that\nkeeps you full.", "FOOD SPOTLIGHT", "🫘",
  "🫘 Chickpeas pack real protein and fiber for very little cost — a genuinely underrated staple for anyone eating more plant-based meals.\n\n→ Roasted = crunchy snack, boiled = base for curries/salads\n→ Fiber keeps you full for hours\n→ One of the cheapest proteins per gram available" + SAVE + "\n💬 Chana/chickpeas — how do you usually cook them? 👇"),
 ("*Ginger* — settles digestion\nand eases nausea,\nbacked by real research.", "FOOD SPOTLIGHT", "🫚",
  "🫚 Ginger has real, research-backed effects on nausea and digestion — which is why it's been used for this specifically across so many different cultures for centuries.\n\n→ Fresh grated in tea works well\n→ Helpful before/after a heavy meal\n→ Genuinely effective, not just a folk remedy" + SAVE + "\n💬 Ginger tea — yes or no for you? 👇"),
 ("*Dark chocolate* (70%+) — genuine\nantioxidants, in\nsmall amounts.", "FOOD SPOTLIGHT", "🍫",
  "🍫 Dark chocolate (70% or higher) does carry real antioxidants — the catch is portion size. A couple of squares, not a full bar, is where the benefit lives.\n\n→ Higher cocoa % = less sugar, more benefit\n→ Small amount, most days, beats none or too much\n→ Milk chocolate doesn't carry the same benefit" + SAVE + "\n💬 Dark chocolate fan or too bitter for you? 👇"),
 ("*Eggs* — one of the most\ncomplete, affordable\nprotein sources there is.", "FOOD SPOTLIGHT", "🥚",
  "🥚 Eggs contain all nine essential amino acids your body can't make itself — genuinely one of the most complete, affordable proteins available anywhere.\n\n→ The yolk carries most of the nutrients, don't skip it\n→ Great at any meal, not just breakfast\n→ Cheap, versatile, and filling" + SAVE + "\n💬 How do you usually eat your eggs? 👇"),
 ("*Lentils/Dal* — fiber, protein,\nand iron in one\ncheap bowl.", "FOOD SPOTLIGHT", "🍲",
  "🍲 One bowl of dal covers real protein, fiber, and iron — part of why it's been a daily staple across generations, not just tradition for its own sake.\n\n→ Add a squeeze of lemon to boost iron absorption\n→ Different dals offer slightly different nutrient mixes\n→ A genuinely complete, cheap meal component" + SAVE + "\n💬 What's your go-to dal? 👇"),
 ("*Pumpkin seeds* — magnesium\nthat many people\nare quietly low on.", "FOOD SPOTLIGHT", "🎃",
  "🎃 Many people run quietly low on magnesium — pumpkin seeds are one of the easiest, tastiest ways to close that gap.\n\n→ A small handful covers a meaningful share of daily needs\n→ Magnesium supports sleep and muscle relaxation too\n→ Roasted and lightly salted is an easy daily habit" + SAVE + "\n💬 Ever tried pumpkin seeds as a snack? 👇"),
]

# ---------------------------------------------------------------- evening
EVENING = [
 ("Turn off overhead lights\n*an hour* before bed.", "EVENING TIP", "💡",
  "💡 Bright ceiling lights tell your brain it's still daytime, delaying your sleep hormone. Dimming an hour before bed is one of the simplest sleep upgrades there is.\n\n→ Switch to lamps in the evening\n→ Warm light beats bright white\n→ It's the whole room, not just your phone screen" + SAVE + "\n💬 What time do the lights go down in your house? 👇"),
 ("No screens\nin the *last 30 minutes*\nbefore sleep.", "EVENING TIP", "📵",
  "📵 That 'just 5 more minutes' scroll reliably turns into 40 — plus blue light and mental stimulation both delay sleep more than people expect.\n\n→ Charge the phone across the room\n→ Read a few pages instead\n→ Your brain needs boredom to actually switch off" + SAVE + "\n💬 Honest — phone in bed tonight? 👇"),
 ("Keep the bedroom\n*cool*, not warm.", "EVENING TIP", "🌡️",
  "🌡️ Sleep starts with a small drop in your core body temperature — a hot room fights that every single night. Cooler air = faster, deeper sleep.\n\n→ Fan or a cracked window helps\n→ Lighter blanket, cooler room, over a heavy one\n→ A warm shower before bed actually helps you cool down after" + SAVE + "\n💬 Fan on all night, or off? 👇"),
 ("Write down\ntomorrow's *top 3* tasks\nbefore you sleep.", "EVENING TIP", "📝",
  "📝 A racing mind at bedtime is often your brain worried it'll forget something. Writing 3 tasks down lets it actually let go.\n\n→ Three, not thirty — the point is emptying your head\n→ Keep a notepad by the bed\n→ You fall asleep faster and wake up clearer" + SAVE + "\n💬 Do you plan the night before? 👇"),
 ("Stretch for *2 minutes* —\nloosen a whole day\nof sitting.", "EVENING TIP", "🧘",
  "🧘 Hours hunched at a desk leave hips and back tight — which follows you straight into a restless night. A short, gentle stretch signals the body to wind down.\n\n→ Neck, shoulders, hips, hamstrings\n→ Slow and easy, never forced\n→ Pair it with dimming the lights" + SAVE + "\n💬 Do you stretch before bed? 👇"),
 ("Avoid heavy meals\n*3 hours* before\nbedtime.", "EVENING TIP", "🍽️",
  "🍽️ A heavy meal right before bed keeps digestion active when your body should be winding down — often behind restless nights people can't explain.\n\n→ Give it at least 2-3 hours before lying down\n→ A light snack is fine if you're genuinely hungry\n→ Spicy/fatty food especially disrupts sleep quality" + SAVE + "\n💬 Late dinners — guilty or not? 👇"),
 ("Keep your phone charging\n*outside* the bedroom.", "EVENING TIP", "🔌",
  "🔌 The phone by the pillow is the #1 silent sleep thief — one glance turns into scrolling, one buzz turns into being awake. Charging it elsewhere removes the temptation entirely.\n\n→ Buy a cheap alarm clock so 'I need it for the alarm' stops being the excuse\n→ Out of arm's reach is often enough\n→ Your morning routine improves too" + SAVE + "\n💬 Where does your phone sleep? 👇"),
 ("A warm shower\n*before bed* actually\ncools your body after.", "EVENING TIP", "🚿",
  "🚿 Sounds backwards, but a warm shower raises your temperature briefly — then the rapid cool-down afterward mimics the natural drop your body needs to fall asleep.\n\n→ Time it about an hour before bed\n→ Warm, not hot\n→ Pair with dim lights after for the full effect" + SAVE + "\n💬 Shower morning or night person? 👇"),
 ("Skip the nightcap —\nalcohol *fragments*\ndeep sleep.", "EVENING TIP", "🍷",
  "🍷 Alcohol can make you fall asleep faster but fragments deep sleep later in the night — which is why you can sleep 8 hours and still wake up tired.\n\n→ Deep sleep is where real recovery happens\n→ Even one drink measurably affects sleep quality\n→ If you drink, earlier in the evening is gentler than right before bed" + SAVE + "\n💬 Did you know alcohol affected sleep quality this much? 👇"),
 ("Same bedtime,\n*even on weekends*,\nbeats sleeping in.", "EVENING TIP", "⏰",
  "⏰ Sleeping till noon Saturday, then 6 AM Monday, is like flying across time zones every week — your body clock never settles. A steady bedtime beats trying to 'catch up.'\n\n→ Same sleep/wake time, even weekends\n→ Consistency beats total hours banked\n→ Mornings get noticeably easier within a week" + SAVE + "\n💬 Fixed bedtime, or all over the place? 👇"),
]

# ------------------------------------------------------------ text checkin
TEXT_CHECKIN = [
 "Quick check-in 👇\n\nOn a scale of 1-10, how rested do you feel right now?\n\nDrop your number — and one thing that would move it up a point 👇",
 "Honest question 👇\n\nWhat's the last thing you ate that actually made you feel good afterward — not just tasted good, felt good?\n\nComment it below 👇",
 "Fill in the blank 👇\n\n\"My body feels best when I ______.\"\n\nSometimes naming it is the reminder you needed 👇",
 "One-word check-in 👇\n\nHow's your energy right now — in exactly one word?\n\nWe'll start: \"Okay.\" Your turn 👇",
 "Real talk 👇\n\nWhat's one health habit you keep meaning to start but haven't yet?\n\nSay it here — it's the first step 👇",
 "Quick poll 👇\n\nWhich slump hits you hardest?\n\n😴 Morning grogginess\n😩 Afternoon crash\n🥱 Evening exhaustion\n\nDrop your answer 👇",
 "Two-word check-in 👇\n\nHow does your body feel right now — in exactly two words?\n\nWe'll start: \"Tired, hopeful.\" Your turn 👇",
 "Honest question 👇\n\nWhat's the ONE health habit that would change the most for you — if you actually stuck to it?\n\nNot all of them. Just one 👇",
 "Quick check-in 👇\n\nHow many hours did you actually sleep last night?\n\n😴 7-8　😐 5-6　😩 under 5\n\nDrop your number below 👇",
 "One healthy thing you did today 👇\n\nDrank water. Took the stairs. Slept early. Said no to seconds.\n\nType it below — someone reading might need the idea 👇",
]

# -------------------------------------------------------------- quickfact
QUICKFACT = [
 ("Two minutes of *slow\nbreathing* calms your body\nfaster than almost anything free.", "QUICK FACT", "😮‍💨",
  "😮‍💨 In for 4 seconds, out for 6. That long exhale flips you from stress mode into rest mode — heart rate drops, shoulders loosen. Costs nothing, works in minutes.\n\n→ Try five rounds right now\n→ Works anywhere, no equipment\n→ One of the fastest free stress tools there is" + SAVE + "\n💬 Feel calmer after 5 rounds? 👇"),
 ("Chew slowly — digestion\nstarts in your *mouth*,\nnot your stomach.", "QUICK FACT", "🍽️",
  "🍽️ Swallowing half-chewed food makes your stomach do extra work — which is where a lot of bloating actually comes from. Slowing down also lets 'full' signals catch up.\n\n→ Put the fork down between bites\n→ Chew until it's nearly liquid\n→ Bonus: you eat less without trying" + SAVE + "\n💬 Fast or slow eater? 👇"),
 ("*Consistency* beats intensity.\nSmall daily habits\nwin every time.", "QUICK FACT", "🌱",
  "🌱 One healthy choice today beats a perfect plan that starts 'Monday.' Health is built in ordinary, boring days — not dramatic resets you can't sustain.\n\n→ Pick one small habit you can't fail at\n→ Repeat it daily, boringly\n→ Let it get easy before adding the next" + SAVE + "\n💬 What small habit are you sticking to? 👇"),
 ("A *10-minute walk* can lift\na low mood faster\nthan sugar.", "QUICK FACT", "🚶",
  "🚶 When you feel flat, reaching for a snack is often really reaching for a mood boost. A short walk gives the same lift, without the crash 30 minutes later.\n\n→ Outside beats indoors (light helps)\n→ 10 minutes is enough to shift mood\n→ Bonus: it aids digestion too" + SAVE + "\n💬 Walk or snack when you're low? 👇"),
 ("*Sunlight* in the morning\nsets your sleep clock\nfor that same night.", "QUICK FACT", "🌤️",
  "🌤️ Morning light is the strongest signal your body clock reads all day — better energy today, and genuinely easier sleep tonight.\n\n→ Ten minutes outdoors within an hour of waking\n→ Outdoor light beats any indoor bulb\n→ Cloudy days still count" + SAVE + "\n💬 Do you get daylight before 9 AM? 👇"),
 ("Your neck holds up a head\nthat gets *heavier* the more\nyou look down at your phone.", "QUICK FACT", "📱",
  "📱 Looking down at a screen loads your neck like a small child sitting on it. Hours of that daily is why so many people carry neck and upper-back pain by evening.\n\n→ Lift the phone to eye level\n→ Every 20 min, roll shoulders back\n→ Tuck the chin, don't crane forward" + SAVE + "\n💬 Neck or back stiff by evening? 👇"),
 ("*Grip strength* is one of\nthe simplest signs of\nhow well you're ageing.", "QUICK FACT", "🤝",
  "🤝 It sounds odd, but how firmly you can grip tracks with overall strength and healthy ageing. Weak hands often mean weak everything else.\n\n→ Carry your own groceries\n→ Hang from a bar occasionally\n→ Small things that keep the whole body capable" + SAVE + "\n💬 Firm handshake, or need to work on it? 👇"),
 ("*Loneliness* affects health\nas much as many\nphysical risk factors.", "QUICK FACT", "💚",
  "💚 Connection is a genuine health input — like food and sleep. Long-term isolation strains the body in measurable ways, while a good conversation eases it.\n\n→ One call, one message, today\n→ It counts more than you'd think\n→ Tag someone you've been meaning to check on" + SAVE + "\n💬 Who came to mind just now? 👇"),
 ("Cooked *tomatoes* release more\nof their best antioxidant\nthan raw ones.", "QUICK FACT", "🍅",
  "🍅 Unusual but true — heat unlocks more lycopene, the antioxidant linked to heart health. So tomato curry and sauce have a genuine upside.\n\n→ A little oil helps absorption\n→ Raw tomatoes are still great for other nutrients\n→ Variety wins: eat them both ways" + SAVE + "\n💬 Raw or cooked tomatoes for you? 👇"),
 ("*Cold water on your face*\ncan calm a racing\nheart in seconds.", "QUICK FACT", "💦",
  "💦 Splashing cold water on your face can trigger a genuine reflex that slows your heart rate — a fast, free way to interrupt a spike of anxiety or stress.\n\n→ Works in under 30 seconds\n→ Cold wrists work too, if you're not near a sink\n→ A real physiological tool, not just a distraction" + SAVE + "\n💬 Would you try this next time you're stressed? 👇"),
]

HOURS = [1, 4, 7, 10, 13, 16, 19]  # matches aug_health.py's 7-slot rhythm
START_DATE = "2026-08-08"
DAYS = 30


def _dates(n):
    import datetime as dt
    d0 = dt.date.fromisoformat(START_DATE)
    return [(d0 + dt.timedelta(days=i)).isoformat() for i in range(n)]


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    counters = {"morning": 0, "myth": 0, "know": 0, "food": 0, "evening": 0, "text": 0, "quick": 0}
    n_img = 0
    dates = _dates(DAYS)

    # 6 image slots/day rotate through these 6 pools in order; slot 6 (index 3,
    # 0-based pos 3) is skipped for image and used for the text check-in instead
    # to match aug_health.py's exact layout: fact,myth,fact,fact,fact,text,fact
    SLOT_POOLS = ["morning", "myth", "know", "food", "evening", "text", "quick"]

    for day_idx, date in enumerate(dates):
        for slot_idx, hour in enumerate(HOURS):
            pool = SLOT_POOLS[slot_idx]
            base_id = f"hd-refill1-{day_idx:02d}-{slot_idx}"
            if base_id in have or (base_id + "-fb") in have:
                continue
            ts = f"{date}T{hour:02d}:00:00+00:00"

            if pool == "text":
                caption = TEXT_CHECKIN[counters["text"] % len(TEXT_CHECKIN)]
                counters["text"] += 1
                items.append({"id": base_id, "account": "health-daily", "network": "facebook",
                             "type": "text", "message": caption, "when": ts, "status": "pending"})
                continue

            img_path = f"{IMG}/{day_idx:02d}_{slot_idx}.png"
            if pool == "morning":
                text, kicker, emoji, caption = MORNING[counters["morning"] % len(MORNING)]
                counters["morning"] += 1
                render(health_fact, text, img_path, kicker=kicker, emoji=emoji)
            elif pool == "myth":
                myth, fact, caption = MYTH[counters["myth"] % len(MYTH)]
                counters["myth"] += 1
                render(health_myth_fact, myth, fact, img_path)
            elif pool == "know":
                text, kicker, emoji, caption = DIDYOUKNOW[counters["know"] % len(DIDYOUKNOW)]
                counters["know"] += 1
                render(health_fact, text, img_path, kicker=kicker, emoji=emoji)
            elif pool == "food":
                text, kicker, emoji, caption = FOOD[counters["food"] % len(FOOD)]
                counters["food"] += 1
                render(health_fact, text, img_path, kicker=kicker, emoji=emoji)
            elif pool == "evening":
                text, kicker, emoji, caption = EVENING[counters["evening"] % len(EVENING)]
                counters["evening"] += 1
                render(health_fact, text, img_path, kicker=kicker, emoji=emoji)
            else:  # quick
                text, kicker, emoji, caption = QUICKFACT[counters["quick"] % len(QUICKFACT)]
                counters["quick"] += 1
                render(health_fact, text, img_path, kicker=kicker, emoji=emoji)

            n_img += 1
            items.append({"id": base_id + "-fb", "account": "health-daily", "network": "facebook",
                         "type": "photo", "message": caption, "image_url": img_path,
                         "when": ts, "status": "pending"})
            items.append({"id": base_id + "-ig", "account": "health-daily", "network": "instagram",
                         "type": "image", "message": caption, "image_url": img_path,
                         "when": ts, "status": "pending"})
        if (day_idx + 1) % 5 == 0:
            print(f"  ...{day_idx+1}/{DAYS} days built ({n_img} images so far)")
    save(q)
    print(f"HEALTH DAILY refill: rendered {n_img} images, queue now {len(items)} items")


if __name__ == "__main__":
    build()
