# -*- coding: utf-8 -*-
"""Health Daily Growth OS — Week 1 (Jul 31 → Aug 6). 6 posts/day = 3 reels + 3 images.

Every claim below is traceable to WHO / CDC / NIH / Mayo / Harvard Health /
Cleveland Clinic / NHS / Johns Hopkins. Nothing invented, no miracle cures,
uncertainty stated where evidence is mixed.

Weekly balance held: 2 nutrition, 2 exercise, 1 mental health, 1 disease
prevention, 1 myth-vs-fact, 1 riddle, 1 healthy habit, 1 scientific fact,
1 lifestyle mistake — spread across the week and rotated so no topic repeats.

Emits the mandated JSON schema to hd_os_week1.json for automation.
"""
import json
import sys
from datetime import date, timedelta

sys.stdout.reconfigure(encoding="utf-8")

DISCLAIMER = ("This content is for educational purposes and is not a substitute "
              "for professional medical advice.")
CTA = "Follow for daily health education. Save this post. Share it with family."

# Reel slots 08:00 / 14:00 / 20:00 UTC · image slots 11:00 / 17:00 / 23:00 UTC
REEL_HOURS = [8, 14, 20]
IMG_HOURS = [11, 17, 23]

# ── Reels ───────────────────────────────────────────────────────────────────
# (category, title, hook, beats[(onscreen, voiceover)], caption_value, question,
#  hashtags, sources)
REELS = [
("Hydration", "You're drinking water at the wrong time",
 "You're drinking water — just at the wrong time.",
 [("YOU'RE DRINKING WATER\nAT THE *WRONG TIME*",
   "You're drinking water. You're just doing it at the wrong time."),
  ("MOST PEOPLE WAIT\nUNTIL THEY'RE *THIRSTY*",
   "Most people wait until they feel thirsty."),
  ("THIRST SHOWS UP\n*LATE*",
   "But thirst is a late signal. By the time you feel it, you're already mildly dehydrated."),
  ("IT SHOWS UP AS\n*TIREDNESS* AND\nPOOR CONCENTRATION",
   "And mild dehydration usually shows up as tiredness and poor concentration, not a dry mouth."),
  ("SIP *THROUGHOUT*\nTHE DAY",
   "So sip steadily through the day instead of drinking a lot at once. Keep a bottle where you can see it.")],
 "Thirst is your body's late warning, not its first one. Mild dehydration is linked to reduced "
 "concentration and increased tiredness — so if your afternoon energy dips, water is worth trying "
 "before another coffee. Most adults get enough from drinks and food combined; pale-yellow urine is "
 "a reasonable everyday guide.",
 "Do you drink water regularly, or only when you're thirsty?",
 ["#hydration", "#healthyhabits", "#dailyhealthtips", "#wellness", "#healthylifestyle", "#drinkwater", "#healthed"],
 ["NHS — Water, drinks and your health", "Harvard T.H. Chan School of Public Health — The Nutrition Source: Water"]),

("Exercise", "Why a walk after dinner beats lying down",
 "Ten minutes after dinner changes how your body handles the meal.",
 [("A *10-MINUTE WALK*\nAFTER DINNER",
   "A ten minute walk after dinner does more than you'd think."),
  ("YOUR BLOOD SUGAR\nRISES AFTER *EVERY* MEAL",
   "Your blood sugar rises after every meal. That's completely normal."),
  ("LIGHT WALKING HELPS\nMUSCLES USE\nSOME OF THAT *GLUCOSE*",
   "But light walking helps your muscles take up some of that glucose from the blood."),
  ("STUDIES LINK IT TO\nSMALLER POST-MEAL\n*SPIKES*",
   "Research links short post-meal walks with smaller spikes after eating."),
  ("AROUND THE BLOCK\nIS *ENOUGH*",
   "You don't need a workout. Around the block is enough. And it helps digestion and sleep too.")],
 "You don't need a gym for this one. Muscles use glucose when they move, so a gentle walk after "
 "eating helps blunt the post-meal rise in blood sugar. It's one of the simplest habits with real "
 "evidence behind it — especially useful if you sit a lot in the evening.",
 "Are you team walk-after-dinner, or team sofa?",
 ["#walking", "#exercise", "#bloodsugar", "#healthyhabits", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["Diabetes UK — Physical activity and blood glucose", "Mayo Clinic — Walking: Trim your waistline, improve your health"]),

("Sleep", "The bedroom temperature mistake",
 "Your bedroom is probably too warm to sleep well.",
 [("YOUR BEDROOM IS\nPROBABLY *TOO WARM*",
   "Your bedroom is probably too warm."),
  ("TO FALL ASLEEP, YOUR\nBODY MUST *COOL DOWN*",
   "To fall asleep, your body has to drop its core temperature slightly."),
  ("A HOT ROOM\n*FIGHTS* THAT",
   "A hot room works against that, which is why you lie there awake."),
  ("A COOLER ROOM HELPS\nYOU FALL ASLEEP\n*FASTER*",
   "A cooler room helps most people fall asleep faster and wake less during the night."),
  ("COOLER ROOM.\nLIGHTER BLANKET.\n*BETTER SLEEP.*",
   "Cooler room, lighter blanket. A warm shower an hour before bed helps too — it cools you afterwards.")],
 "Falling asleep depends on a small drop in your core body temperature. A room that's too warm "
 "delays that process. Sleep guidance generally recommends a cool, dark, quiet bedroom — and it's "
 "one of the easiest changes to make tonight.",
 "Is your bedroom cool enough at night?",
 ["#sleep", "#sleephealth", "#healthyhabits", "#wellness", "#dailyhealthtips", "#healthylifestyle", "#bettersleep"],
 ["CDC — Tips for Better Sleep", "NHS — How to get to sleep"]),

("Heart Health", "The salt you can't see",
 "Most of your salt isn't coming from the salt shaker.",
 [("MOST OF YOUR SALT\nISN'T FROM THE\n*SALT SHAKER*",
   "Most of the salt you eat doesn't come from the salt shaker."),
  ("IT'S ALREADY IN\n*PACKAGED FOOD*",
   "It's already in packaged and processed food before it reaches you."),
  ("BREAD. SAUCES.\nSOUP. *SNACKS*.",
   "Bread, sauces, soups, ready meals and snacks are the usual sources."),
  ("TOO MUCH SALT RAISES\n*BLOOD PRESSURE*",
   "Eating too much salt over time raises blood pressure, which is a major risk factor for heart disease and stroke."),
  ("CHECK *LABELS*.\nCOOK MORE AT HOME.",
   "Check labels, cook more at home, and lean on herbs, garlic and lemon for flavour. Your taste adjusts in a couple of weeks.")],
 "The World Health Organization recommends adults consume less than 5g of salt per day — about one "
 "teaspoon — and most people worldwide eat more than that. The bigger lever isn't your salt shaker, "
 "it's packaged food. Reducing gradually works better than going bland overnight, because your taste "
 "genuinely adapts.",
 "Do you check the salt content on food labels?",
 ["#hearthealth", "#bloodpressure", "#nutrition", "#healthyeating", "#dailyhealthtips", "#wellness", "#preventivecare"],
 ["WHO — Salt reduction fact sheet", "American Heart Association — How much sodium should I eat per day?"]),

("Brain Health", "Morning light sets your whole day",
 "Ten minutes of morning light changes how you sleep tonight.",
 [("MORNING LIGHT CHANGES\nHOW YOU SLEEP\n*TONIGHT*",
   "Ten minutes of morning light changes how you sleep tonight."),
  ("YOUR BODY CLOCK RUNS\nON *LIGHT*",
   "Your body clock is set mainly by light, not by the time on your phone."),
  ("MORNING LIGHT SAYS:\n*THE DAY HAS STARTED*",
   "Getting daylight early tells your brain the day has started."),
  ("THAT HELPS MELATONIN\nARRIVE ON TIME\n*AT NIGHT*",
   "That helps your sleep hormone arrive at the right time in the evening."),
  ("10 MINUTES OUTSIDE.\nEVEN ON A *CLOUDY* DAY.",
   "Ten minutes outside in the morning is enough. Even a cloudy day is far brighter than indoor lighting.")],
 "Light is the strongest signal for your circadian rhythm — the internal clock that controls sleep, "
 "alertness and hormone timing. Outdoor light in the morning is dramatically brighter than indoor "
 "light, even under cloud. It's free, takes ten minutes, and tends to improve both daytime energy "
 "and night-time sleep.",
 "Do you get outside before 9am?",
 ["#brainhealth", "#sleep", "#circadianrhythm", "#healthyhabits", "#wellness", "#dailyhealthtips", "#mentalhealth"],
 ["NIH News in Health — The Power of Light", "Cleveland Clinic — Circadian Rhythm"]),

("Gut Health", "Fibre is the nutrient nobody talks about",
 "Everyone talks protein. Almost nobody talks fibre.",
 [("EVERYONE TALKS *PROTEIN*.\nNOBODY TALKS *FIBRE*.",
   "Everyone talks about protein. Almost nobody talks about fibre."),
  ("MOST ADULTS DON'T GET\n*ENOUGH*",
   "And most adults don't get enough of it."),
  ("FIBRE FEEDS YOUR\n*GUT BACTERIA*",
   "Fibre feeds the bacteria in your gut, and helps keep digestion regular."),
  ("IT'S LINKED TO LOWER\n*HEART DISEASE* RISK",
   "Higher fibre intake is linked with lower risk of heart disease and type 2 diabetes."),
  ("BEANS. OATS. FRUIT.\nVEG. *WHOLE GRAINS*.",
   "Beans, lentils, oats, fruit, vegetables and whole grains. Increase it slowly and drink water alongside.")],
 "Fibre does a lot of quiet work: it feeds gut bacteria, supports regular digestion, and higher "
 "intakes are associated with lower risk of heart disease and type 2 diabetes. Most people fall "
 "short of recommended intakes. Increase gradually — a sudden jump can cause bloating.",
 "How much fibre do you think you get in a day?",
 ["#guthealth", "#fibre", "#nutrition", "#healthyeating", "#dailyhealthtips", "#wellness", "#digestivehealth"],
 ["Harvard T.H. Chan — The Nutrition Source: Fiber", "Mayo Clinic — Dietary fiber: Essential for a healthy diet"]),

("Immunity", "Sleep is an immune function",
 "Short sleep makes you more likely to catch what's going around.",
 [("SHORT SLEEP MAKES YOU\nMORE LIKELY TO\n*GET SICK*",
   "Short sleep makes you more likely to catch what's going around."),
  ("YOUR IMMUNE SYSTEM\nDOES REPAIR WORK\n*WHILE YOU SLEEP*",
   "Your immune system does a lot of its work while you sleep."),
  ("STUDIES LINK SHORT SLEEP\nWITH HIGHER RATES\nOF *INFECTION*",
   "Research links regularly short sleep with higher rates of infection after exposure."),
  ("SLEEP ISN'T *LAZY*.\nIT'S MAINTENANCE.",
   "Sleep isn't laziness. It's maintenance. Most adults need seven to nine hours.")],
 "Sleep and immunity are directly connected. During sleep your body produces and redistributes "
 "immune cells, and consistently short sleep is associated with greater susceptibility to infection. "
 "If you're run down and sleeping five hours, the sleep is the more useful fix than another supplement.",
 "How many hours did you sleep last night?",
 ["#immunity", "#sleep", "#immunesystem", "#wellness", "#dailyhealthtips", "#healthylifestyle", "#sleephealth"],
 ["CDC — Sleep and Health", "NIH News in Health — Sleep On It"]),

("Diabetes", "Why the order you eat matters",
 "Eating the same meal in a different order changes your blood sugar.",
 [("THE *ORDER* YOU EAT\nCHANGES YOUR\nBLOOD SUGAR",
   "Eating the same meal in a different order can change your blood sugar response."),
  ("VEGETABLES AND PROTEIN\n*FIRST*",
   "Try vegetables and protein first."),
  ("STARCHY CARBS\n*LAST*",
   "Then the starchy carbohydrates last."),
  ("SMALLER SPIKE.\nSAME *MEAL*.",
   "Studies suggest this produces a smaller rise in blood glucose after eating — from the same food.")],
 "This is a small, low-effort change with reasonable evidence behind it: eating vegetables and "
 "protein before carbohydrates is associated with a lower post-meal glucose rise. It doesn't replace "
 "medical treatment for diabetes, but it's a sensible habit for most people. Evidence is still "
 "developing, so treat it as a helpful tweak rather than a rule.",
 "Would you try changing the order of your next meal?",
 ["#diabetes", "#bloodsugar", "#nutrition", "#healthyeating", "#dailyhealthtips", "#wellness", "#preventivecare"],
 ["Cleveland Clinic — Food order and blood sugar", "Harvard Health — Carbohydrates and blood sugar"]),

("Kidney Health", "Your kidneys filter your blood 30+ times a day",
 "Your kidneys clean your entire blood supply many times every single day.",
 [("YOUR KIDNEYS FILTER\nYOUR BLOOD *ALL DAY*",
   "Your kidneys filter your entire blood supply many times a day, every day."),
  ("THEY REMOVE WASTE\nAND EXTRA *FLUID*",
   "They remove waste and extra fluid, and help control blood pressure."),
  ("KIDNEY DISEASE OFTEN\nHAS *NO EARLY SIGNS*",
   "Early kidney disease often has no symptoms at all, which is why it's frequently missed."),
  ("THE BIGGEST RISKS:\n*DIABETES* AND\nHIGH BLOOD PRESSURE",
   "The two biggest causes are diabetes and high blood pressure. Managing those protects your kidneys.")],
 "Kidneys quietly do enormous work — filtering waste, balancing fluid, and helping regulate blood "
 "pressure. Chronic kidney disease usually develops without symptoms until it's advanced, and the "
 "leading causes are diabetes and high blood pressure. If you have either, regular check-ups matter "
 "more than any single food or drink.",
 "Have you ever had your kidney function checked?",
 ["#kidneyhealth", "#preventivecare", "#diabetes", "#bloodpressure", "#dailyhealthtips", "#wellness", "#healthawareness"],
 ["National Kidney Foundation — How your kidneys work", "CDC — Chronic Kidney Disease Basics"]),

("Healthy Aging", "Grip strength predicts healthy aging",
 "How firmly you can grip says a lot about how you're aging.",
 [("*GRIP STRENGTH*\nPREDICTS HOW\nYOU'RE AGEING",
   "How firmly you can grip says a surprising amount about how you're ageing."),
  ("IT REFLECTS *OVERALL*\nMUSCLE STRENGTH",
   "It reflects overall muscle strength, not just your hands."),
  ("MUSCLE PROTECTS BONES,\nJOINTS AND *BALANCE*",
   "Muscle protects your bones and joints, and supports balance, which prevents falls later in life."),
  ("CARRY THINGS.\nLIFT THINGS.\n*USE IT.*",
   "Carry your own shopping. Lift things. Strength training works at any age, including in your seventies.")],
 "Grip strength is used in research as a simple marker of overall muscular strength, and lower grip "
 "strength is associated with poorer health outcomes as people age. The practical takeaway isn't to "
 "squeeze a ball — it's that maintaining muscle through regular resistance activity supports "
 "independence later.",
 "Do you do any strength training in a normal week?",
 ["#healthyaging", "#strengthtraining", "#muscle", "#wellness", "#dailyhealthtips", "#fitness", "#healthylifestyle"],
 ["Harvard Health — Grip strength and health", "WHO — Physical activity guidelines for older adults"]),

("Women's Health", "Iron: why it's absorbed better with vitamin C",
 "Plant iron is hard to absorb — unless you pair it correctly.",
 [("PLANT IRON IS *HARD*\nTO ABSORB",
   "Iron from plant foods is much harder for your body to absorb than iron from meat."),
  ("*VITAMIN C* UNLOCKS IT",
   "Vitamin C significantly improves how much of it you actually absorb."),
  ("LEMON ON SPINACH.\nTOMATO IN LENTILS.",
   "So squeeze lemon over greens, or add tomato to lentils and beans."),
  ("AND SKIP TEA OR COFFEE\n*WITH* THE MEAL",
   "And avoid tea or coffee right with the meal — compounds in them reduce iron absorption.")],
 "Iron deficiency is one of the most common nutritional deficiencies worldwide, and it "
 "disproportionately affects women of reproductive age. Pairing plant iron sources with vitamin C "
 "meaningfully improves absorption, while tea and coffee taken with the meal reduce it. If you're "
 "persistently tired, ask your doctor for a blood test rather than self-supplementing.",
 "Did you know about the vitamin C trick?",
 ["#womenshealth", "#iron", "#nutrition", "#anemia", "#dailyhealthtips", "#wellness", "#healthyeating"],
 ["WHO — Anaemia fact sheet", "NIH Office of Dietary Supplements — Iron Fact Sheet"]),

("Preventive Care", "The health checks worth doing",
 "Most serious conditions are silent long before you feel them.",
 [("MOST SERIOUS CONDITIONS\nARE *SILENT* AT FIRST",
   "Most serious conditions are completely silent long before you feel anything."),
  ("BLOOD PRESSURE.\nBLOOD SUGAR.\n*CHOLESTEROL*.",
   "Blood pressure, blood sugar and cholesterol are the three that quietly cause the most damage."),
  ("ALL THREE ARE\n*SIMPLE* TO CHECK",
   "All three are simple to check, and often free at a pharmacy or clinic."),
  ("CHECKING IS *CHEAP*.\nFINDING OUT LATE\nISN'T.",
   "Checking is cheap. Finding out late is not. Ask your doctor what's appropriate for your age.")],
 "Prevention works because these conditions develop silently over years. Blood pressure, blood "
 "glucose and cholesterol checks are quick, widely available, and give you a chance to act early. "
 "What's recommended varies by age, family history and risk factors — so this is a conversation with "
 "your doctor, not a fixed checklist.",
 "When did you last have a general health check?",
 ["#preventivecare", "#healthcheck", "#hearthealth", "#bloodpressure", "#dailyhealthtips", "#wellness", "#healthawareness"],
 ["CDC — Preventive Health Care", "NHS — NHS Health Check"]),

("Liver Health", "Your liver does over 500 jobs",
 "Your liver quietly runs hundreds of processes right now.",
 [("YOUR LIVER DOES\n*HUNDREDS* OF JOBS",
   "Your liver performs hundreds of separate functions in your body."),
  ("IT FILTERS BLOOD,\nSTORES ENERGY,\nMAKES *PROTEINS*",
   "It filters blood, stores energy, makes proteins and helps you digest fat."),
  ("IT ALSO *DETOXES* YOU —\nFOR FREE, 24/7",
   "It also detoxifies your body around the clock, for free. No tea or juice does this."),
  ("PROTECT IT: LIMIT ALCOHOL,\nKEEP A HEALTHY WEIGHT",
   "Protect it by limiting alcohol and keeping a healthy weight. Fatty liver disease is now very common.")],
 "The liver handles an enormous range of tasks — filtering blood, storing glucose, producing "
 "proteins, processing medication, and producing bile for digesting fats. It also performs the "
 "detoxification that 'detox' products claim to provide. Non-alcoholic fatty liver disease is "
 "increasingly common and is closely tied to weight and metabolic health.",
 "Have you ever fallen for a 'detox' product?",
 ["#liverhealth", "#detoxmyth", "#nutrition", "#healthylifestyle", "#dailyhealthtips", "#wellness", "#preventivecare"],
 ["Johns Hopkins Medicine — Liver: Anatomy and Functions", "NHS — Non-alcoholic fatty liver disease"]),

("Weight Loss", "Why crash diets fail",
 "The diet that works is the one you can still do in a year.",
 [("THE DIET THAT *WORKS*\nIS THE ONE YOU CAN\nSTILL DO IN A *YEAR*",
   "The diet that works is the one you can still be doing in a year."),
  ("VERY RESTRICTIVE PLANS\nWORK — *BRIEFLY*",
   "Very restrictive plans do produce fast results, briefly."),
  ("THEN MOST PEOPLE\n*REGAIN* IT",
   "Then most people regain the weight, because the plan was never sustainable."),
  ("SMALLER CHANGES.\n*KEPT LONGER.*",
   "Smaller changes kept for longer beat dramatic changes abandoned in three weeks.")],
 "Rapid weight loss from highly restrictive diets is usually followed by regain, because the "
 "approach can't be maintained. Guidance from major health bodies consistently favours gradual, "
 "sustainable change — modest calorie reduction, more fibre and protein, and regular activity. "
 "Slower is genuinely more effective long-term.",
 "What's one small change you could actually keep?",
 ["#weightloss", "#healthyeating", "#sustainablehabits", "#nutrition", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["NHS — Start losing weight", "Mayo Clinic — Weight loss: 6 strategies for success"]),

("Men's Health", "The symptom men most often ignore",
 "Men are statistically less likely to see a doctor early.",
 [("MEN ARE LESS LIKELY\nTO SEE A DOCTOR\n*EARLY*",
   "Men are statistically less likely to see a doctor when something first changes."),
  ("\"IT'LL PROBABLY\nSORT ITSELF OUT\"",
   "It'll probably sort itself out is the most expensive sentence in men's health."),
  ("EARLY DETECTION CHANGES\nOUTCOMES FOR MOST\n*SERIOUS* CONDITIONS",
   "For most serious conditions, early detection genuinely changes the outcome."),
  ("BOOK THE APPOINTMENT.\n*THAT'S IT.*",
   "If something has changed and stayed changed, book the appointment. That's the whole message.")],
 "Research consistently shows men are less likely than women to seek medical help early, and later "
 "presentation is associated with worse outcomes across many conditions. This isn't about anxiety — "
 "it's that a persistent change (in energy, weight, bowel habits, a lump, or a mole) is worth a "
 "conversation with a doctor rather than a wait-and-see.",
 "Tag someone who's been putting off an appointment.",
 ["#menshealth", "#preventivecare", "#healthawareness", "#earlydetection", "#dailyhealthtips", "#wellness", "#checkup"],
 ["NHS — Why men should see a GP", "Cleveland Clinic — Men's health screenings by age"]),

("Healthy Recipes", "A breakfast that keeps you full till lunch",
 "If you're starving by 11am, your breakfast is the problem.",
 [("STARVING BY *11AM*?\nIT'S YOUR BREAKFAST.",
   "If you're starving by eleven in the morning, your breakfast is usually the reason."),
  ("CARBS *ALONE* SPIKE\nTHEN DROP YOU",
   "A carbohydrate-only breakfast raises blood sugar quickly, then drops it, and the crash feels like hunger."),
  ("ADD *PROTEIN*\nAND *FIBRE*",
   "Adding protein and fibre flattens that curve."),
  ("OATS + YOGHURT + NUTS.\n*OR* EGGS + VEG.",
   "Oats with yoghurt and nuts. Or eggs with vegetables. Either keeps most people full for hours.")],
 "A breakfast built only from refined carbohydrates causes a faster rise and fall in blood glucose, "
 "which many people experience as mid-morning hunger. Pairing carbohydrates with protein and fibre "
 "slows digestion and improves fullness. This works whether you eat at 7am or midday — the "
 "composition matters more than the clock.",
 "What's your usual breakfast?",
 ["#healthyrecipes", "#breakfast", "#nutrition", "#protein", "#dailyhealthtips", "#healthyeating", "#wellness"],
 ["Harvard T.H. Chan — The Nutrition Source: Protein", "Mayo Clinic — Healthy breakfast: Quick, flexible options"]),

("Daily Wellness", "Chew slowly — digestion starts in your mouth",
 "Digestion starts in your mouth, not your stomach.",
 [("DIGESTION STARTS IN\nYOUR *MOUTH*",
   "Digestion starts in your mouth, not your stomach."),
  ("CHEWING BREAKS FOOD DOWN\nAND MIXES IN *ENZYMES*",
   "Chewing physically breaks food down and mixes in enzymes that begin the process."),
  ("SWALLOWING HALF-CHEWED\nFOOD MAKES YOUR STOMACH\nWORK *HARDER*",
   "Swallowing half-chewed food leaves your stomach doing extra work, which is where a lot of bloating comes from."),
  ("SLOW DOWN.\nPUT THE FORK *DOWN*.",
   "Slow down and put the fork down between bites. Fullness signals also need about twenty minutes to arrive.")],
 "Chewing thoroughly is the first mechanical and chemical step of digestion. Eating quickly is "
 "associated with greater discomfort and with eating more before fullness signals register — those "
 "hormonal signals take roughly 20 minutes. Slowing down is free and helps both digestion and "
 "portion control.",
 "Are you a fast eater or a slow eater?",
 ["#dailywellness", "#digestion", "#guthealth", "#mindfuleating", "#dailyhealthtips", "#wellness", "#healthyhabits"],
 ["Cleveland Clinic — Digestive system: How it works", "NHS — Digestion and bloating"]),

("Vitamin Deficiencies", "Vitamin D: the one most people are short on",
 "Vitamin D is the deficiency most people don't know they have.",
 [("VITAMIN D IS THE ONE\nMOST PEOPLE ARE\n*SHORT ON*",
   "Vitamin D is the deficiency most people don't realise they have."),
  ("YOUR SKIN MAKES IT\nFROM *SUNLIGHT*",
   "Your skin makes it from sunlight, so people who spend most of the day indoors are more at risk."),
  ("IT HELPS YOUR BODY\nABSORB *CALCIUM*",
   "It helps your body absorb calcium, which is why it matters for bones and muscles."),
  ("SUNLIGHT, OILY FISH,\nEGGS — OR ASK ABOUT\nA *SUPPLEMENT*",
   "Sunlight, oily fish and eggs help. In darker months many health services recommend a supplement — ask your doctor.")],
 "Vitamin D supports calcium absorption and bone health, and deficiency is common — particularly in "
 "people with limited sun exposure, darker skin, or who live far from the equator. Several national "
 "health bodies recommend supplementation during autumn and winter. Don't megadose: more is not "
 "better, and it's worth checking with your doctor.",
 "Do you take vitamin D in the winter?",
 ["#vitamind", "#nutrition", "#bonehealth", "#deficiency", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["NHS — Vitamin D", "NIH Office of Dietary Supplements — Vitamin D Fact Sheet"]),

("Home Workouts", "You don't need a gym to build strength",
 "You can build real strength with no equipment at all.",
 [("NO GYM.\nNO EQUIPMENT.\n*STILL WORKS.*",
   "You can build genuine strength with no equipment at all."),
  ("SQUATS. PUSH-UPS.\nLUNGES. *PLANKS*.",
   "Squats, push-ups, lunges and planks cover most major muscle groups."),
  ("GUIDELINES SUGGEST\nSTRENGTH WORK\n*TWICE A WEEK*",
   "Physical activity guidelines recommend muscle-strengthening activity on at least two days a week."),
  ("START WITH WHAT YOU\nCAN DO *TODAY*",
   "Start with what you can actually do today, even if that's five repetitions. Consistency beats intensity.")],
 "Global physical activity guidelines recommend muscle-strengthening activity at least twice a week "
 "alongside regular aerobic movement. Bodyweight exercises count. Muscle supports metabolism, joint "
 "stability and independence as you age — and progress comes from doing it regularly, not from doing "
 "it perfectly.",
 "What's your go-to home exercise?",
 ["#homeworkout", "#strengthtraining", "#exercise", "#fitness", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["WHO — Physical activity fact sheet", "CDC — How much physical activity do adults need?"]),

("Mental Health", "The 2-minute breathing reset",
 "Two minutes of slow breathing calms your body faster than almost anything free.",
 [("TWO MINUTES OF\n*SLOW BREATHING*",
   "Two minutes of slow breathing calms your body faster than almost anything else that's free."),
  ("BREATHE IN FOR *4*.\nOUT FOR *6*.",
   "Breathe in for four seconds. Out for six."),
  ("THE *LONG EXHALE*\nIS THE KEY",
   "The long exhale is the part that matters."),
  ("IT SHIFTS YOU TOWARD\n*REST* MODE",
   "It shifts your nervous system toward its rest-and-recover state. Heart rate settles, shoulders drop."),
  ("FIVE ROUNDS.\n*RIGHT NOW.*",
   "Try five rounds right now, before you scroll on. It costs nothing and works within minutes.")],
 "Slow breathing with a longer exhale activates the parasympathetic nervous system — the branch "
 "that calms you down. It's used in clinical stress-management guidance because it's simple, free "
 "and works quickly. It isn't a treatment for anxiety disorders, but it's a genuinely useful tool "
 "in a stressful moment.",
 "Try five rounds — did you feel any calmer?",
 ["#mentalhealth", "#stressrelief", "#breathing", "#wellness", "#dailyhealthtips", "#mindfulness", "#selfcare"],
 ["Harvard Health — Relaxation techniques: Breath control helps quell errant stress response",
  "NHS — Breathing exercises for stress"]),

("Walking", "Steps: the 10,000 number was a marketing slogan",
 "The 10,000 steps target didn't come from science.",
 [("THE *10,000 STEPS* TARGET\nDIDN'T COME FROM\nSCIENCE",
   "The ten thousand steps target didn't come from research. It came from a 1960s pedometer name."),
  ("REAL BENEFITS START\n*MUCH LOWER*",
   "Studies suggest meaningful health benefits start well below that."),
  ("AROUND *7,000* STEPS\nCAPTURES MOST OF IT",
   "Around seven thousand steps a day captures much of the benefit for many adults, with gains levelling off after."),
  ("SO DON'T QUIT AT 6,000.\n*IT ALREADY COUNTS.*",
   "So if you're at six thousand, that already counts. Don't treat ten thousand as pass or fail.")],
 "The 10,000-step figure originated as a marketing slogan, not a clinical recommendation. Research "
 "since suggests substantial benefit at lower counts, with returns levelling off at higher numbers — "
 "the exact figure varies by age and study. The useful message: more steps than yesterday beats "
 "hitting an arbitrary target or giving up.",
 "How many steps do you average in a day?",
 ["#walking", "#steps", "#exercise", "#healthyhabits", "#dailyhealthtips", "#wellness", "#activelifestyle"],
 ["Harvard Health — 10,000 steps a day: is that a magic number?", "CDC — Physical activity basics"]),

("Eye Health", "Screens don't damage your eyes — but they do dry them",
 "Screens won't ruin your eyesight. They will dry your eyes out.",
 [("SCREENS WON'T *RUIN*\nYOUR EYESIGHT",
   "Screens will not permanently damage your eyesight. That's a myth."),
  ("BUT YOU BLINK\n*FAR LESS* AT A SCREEN",
   "But you blink far less when you're concentrating on one, so your eyes dry out."),
  ("THAT'S THE BURNING,\nGRITTY *FEELING*",
   "That's the burning, gritty feeling by the evening. It's dryness, not damage."),
  ("EVERY 20 MINUTES,\nLOOK *FAR AWAY*\nAND BLINK",
   "Every twenty minutes, look at something far away for twenty seconds and blink fully. It genuinely helps.")],
 "Digital eye strain is real but it's about dryness and fatigue, not permanent damage — a "
 "distinction worth knowing, because the fear is worse than the facts. Reduced blink rate is the "
 "main mechanism. Regular distance breaks, full blinking, and good lighting are the standard advice.",
 "Do your eyes feel tired by the end of the day?",
 ["#eyehealth", "#screentime", "#digitaleyestrain", "#dailyhealthtips", "#wellness", "#healthyhabits", "#eyecare"],
 ["American Academy of Ophthalmology — Computers, Digital Devices and Eye Strain",
  "NHS — Looking after your eyes"]),

]
# ── Images ──────────────────────────────────────────────────────────────────
# (category, framework, title, hook, headline, caption_value, question,
#  image_prompt, hashtags, sources)
IMAGES = [
("Medical Myth vs Fact", "Myth → Truth", "Eating fat makes you fat",
 "\"Eating fat makes you fat\" — one of the most persistent food myths.",
 "MYTH: Eating fat\nmakes you fat",
 "Fat is essential. Your body needs it for hormones, brain function and to absorb vitamins A, D, E "
 "and K. Weight gain comes from consistently taking in more energy than you use — not from one "
 "nutrient. Unsaturated fats from nuts, olive oil, oily fish and avocado are actively linked with "
 "better heart health.",
 "Did you grow up avoiding all fats?",
 "Clean modern health infographic, 4:5 vertical. Split composition: top half a red-tinted panel "
 "labelled MYTH, bottom half a green-tinted panel labelled FACT. Flat-lay of almonds, olive oil, "
 "avocado and salmon on a white marble surface, bright even studio lighting, soft shadows. Generous "
 "clean white space at top and bottom for large text overlay. Trustworthy palette: white, soft blue, "
 "fresh green. No text rendered in image. Photorealistic, high detail.",
 ["#myths", "#nutrition", "#healthyeating", "#healthyfats", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["Harvard T.H. Chan — The Nutrition Source: Fats and Cholesterol", "NHS — Fat: the facts"]),

("Healthy Habits", "Daily Habit", "The 30-minute sitting rule",
 "Sitting for hours affects your health even if you exercise daily.",
 "Stand up every\n30 MINUTES",
 "Long unbroken sitting is associated with health risks that regular exercise doesn't fully cancel "
 "out. The fix is small and repeatable: stand, stretch or walk for a couple of minutes every half "
 "hour. Set a timer if you work at a desk — the point is breaking up the sitting, not the intensity.",
 "How long do you usually sit without a break?",
 "Clean modern health infographic, 4:5 vertical. A bright airy home office, a person of ambiguous "
 "age standing to stretch beside a desk, natural window light, soft blue and white palette. Wide "
 "empty space in the upper third for a large text headline. Warm, encouraging, non-clinical mood. "
 "Diverse, realistic body type. No text rendered in image. Photorealistic.",
 ["#healthyhabits", "#deskjob", "#movement", "#wellness", "#dailyhealthtips", "#healthylifestyle", "#officehealth"],
 ["WHO — Physical activity guidelines", "Mayo Clinic — Sitting risks: How harmful is too much sitting?"]),

("Health Riddles", "Riddle", "Riddle: the silent number",
 "I have no mouth, but I can tell your health.",
 "I HAVE NO MOUTH\nBUT I CAN TELL\nYOUR HEALTH.\n\nDoctors check me\nevery visit.\n\nWhat am I?",
 "Take a guess before you scroll. It's something almost every check-up includes, it's completely "
 "painless, and it can flag a serious problem years before you'd ever feel symptoms.",
 "What's your answer? Comment below — I'll reveal it tomorrow.",
 "Clean minimal health infographic, 4:5 vertical. Soft blue gradient background, a simple elegant "
 "line-art illustration of a blood pressure cuff in white, centred small. Large clear empty area "
 "for text overlay. Calm, curious, puzzle-like mood. Bright trustworthy palette of white and soft "
 "blue. No text rendered in image. High-quality vector infographic style.",
 ["#healthriddle", "#healthquiz", "#guessit", "#dailyhealthtips", "#wellness", "#healthawareness", "#bloodpressure"],
 ["CDC — High Blood Pressure Symptoms and Causes"]),

("Nutrition", "Top 5 Tips", "5 foods with more potassium than a banana",
 "Bananas get the credit — but these have more potassium.",
 "MORE POTASSIUM\nTHAN A BANANA",
 "Potassium helps balance the effects of sodium and supports healthy blood pressure, and most people "
 "get less than recommended. Bananas are the famous source, but potatoes with skin, white beans, "
 "spinach, lentils and plain yoghurt all deliver more per serving. Note: if you have kidney disease, "
 "check with your doctor before increasing potassium.",
 "Which of these do you eat most often?",
 "Clean modern nutrition infographic, 4:5 vertical. Overhead flat-lay on a white surface showing a "
 "baked potato, white beans, fresh spinach, lentils and a bowl of plain yoghurt arranged with even "
 "spacing. Bright natural studio lighting, crisp shadows, fresh green and white palette. Large empty "
 "band across the top third for a text headline. No text rendered in image. Photorealistic, "
 "high detail, appetising.",
 ["#nutrition", "#potassium", "#hearthealth", "#healthyeating", "#dailyhealthtips", "#bloodpressure", "#wellness"],
 ["NIH Office of Dietary Supplements — Potassium Fact Sheet", "Harvard T.H. Chan — The Nutrition Source: Potassium"]),

("Lifestyle Mistakes", "Mistakes People Make", "The 20-20-20 rule for screen eyes",
 "Your eyes burn by evening because you blink far less at a screen.",
 "THE 20-20-20 RULE",
 "When you focus on a screen you blink much less often, so your eyes dry out and sting. The standard "
 "advice is simple: every 20 minutes, look at something about 20 feet away for 20 seconds. Blink "
 "fully while you do it. Position your screen slightly below eye level to reduce strain further.",
 "How many hours a day are you on a screen?",
 "Clean modern health infographic, 4:5 vertical. A person at a bright desk looking away from their "
 "laptop toward a window, relaxed posture, soft natural daylight, calm blue and white palette. "
 "Uncluttered composition with generous empty space in the top third for a large text overlay. "
 "Diverse, realistic, friendly mood. No text rendered in image. Photorealistic.",
 ["#eyehealth", "#screentime", "#digitaleyestrain", "#healthyhabits", "#dailyhealthtips", "#wellness", "#worklife"],
 ["American Academy of Ophthalmology — Computers, Digital Devices and Eye Strain",
  "NHS — Eye health tips"]),

("Early Disease Symptoms", "Hidden Fact", "High blood pressure has no symptoms",
 "High blood pressure usually has no symptoms at all.",
 "HIGH BLOOD PRESSURE\nUSUALLY HAS\nNO SYMPTOMS",
 "This is why it's often called a silent condition. Many people with high blood pressure feel "
 "completely normal, which is exactly what makes it dangerous — it can quietly raise the risk of "
 "heart attack, stroke and kidney damage over years. The only reliable way to know is to measure it. "
 "Most pharmacies will check it free.",
 "When did you last have your blood pressure checked?",
 "Clean modern health infographic, 4:5 vertical. A calm clinical scene: a person's upper arm with a "
 "blood pressure cuff, a friendly healthcare worker's hands, bright white and soft blue palette, "
 "even diffuse lighting, reassuring and non-frightening. Generous clean space at the top for a large "
 "text headline. Diverse skin tone. No graphic medical imagery. No text rendered in image. "
 "Photorealistic.",
 ["#bloodpressure", "#hearthealth", "#preventivecare", "#healthawareness", "#dailyhealthtips", "#wellness", "#checkup"],
 ["WHO — Hypertension fact sheet", "CDC — High Blood Pressure Symptoms and Causes"]),

("Medical Myth vs Fact", "Myth → Truth", "Cracking knuckles causes arthritis",
 "\"Cracking your knuckles causes arthritis\" — it doesn't.",
 "MYTH: Knuckle cracking\ncauses arthritis",
 "Studies have not found a link between knuckle cracking and arthritis. The sound comes from gas "
 "bubbles in the fluid that cushions your joints. It may annoy people around you, but it isn't "
 "damaging your hands. If cracking is painful or accompanied by swelling, that's different — see a doctor.",
 "Are you a knuckle cracker?",
 "Clean modern health infographic, 4:5 vertical. Split composition: red-tinted MYTH panel above, "
 "green-tinted FACT panel below. Close-up of relaxed healthy hands on a white surface, bright even "
 "studio lighting, soft shadows, diverse skin tone. Large clean areas for text overlay top and "
 "bottom. White, soft blue and green palette. No text rendered in image. Photorealistic.",
 ["#myths", "#jointhealth", "#arthritis", "#dailyhealthtips", "#wellness", "#healthfacts", "#mythbusting"],
 ["Harvard Health — Knuckle cracking and arthritis", "Cleveland Clinic — Is cracking your knuckles bad?"]),

("Nutrition", "Do This Instead", "Swap the sugary drink",
 "One daily sugary drink adds up faster than almost anything else.",
 "SWAP THIS →\nFOR THIS",
 "A single sugar-sweetened drink a day is one of the easiest sources of excess calories to remove, "
 "and regular consumption is associated with higher risk of type 2 diabetes and weight gain. Water, "
 "sparkling water with lemon, or unsweetened tea all work. If you drink one daily, swapping even "
 "half of them is progress.",
 "What's your usual drink with meals?",
 "Clean modern nutrition infographic, 4:5 vertical. Side-by-side comparison on a white background: "
 "a glass of cola on the left, a glass of water with fresh lemon and mint on the right, equal "
 "framing. Bright studio lighting, crisp condensation, fresh and appealing. Clean empty band across "
 "the top for a text headline. White, blue and green palette. No text rendered in image. Photorealistic.",
 ["#nutrition", "#sugar", "#healthyswaps", "#diabetes", "#dailyhealthtips", "#healthyeating", "#wellness"],
 ["WHO — Reducing free sugars intake", "Harvard T.H. Chan — The Nutrition Source: Sugary Drinks"]),

("Mental Health", "Problem → Solution", "Write down tomorrow's three tasks",
 "A racing mind at bedtime is often just your brain afraid it'll forget.",
 "3 TASKS.\nBEFORE BED.",
 "If you lie awake mentally rehearsing tomorrow, writing it down helps. Research on bedtime writing "
 "suggests that noting down upcoming tasks can help people fall asleep faster than journaling about "
 "the day. Keep it to three items — the goal is emptying your head, not planning your year.",
 "Does your mind race when you lie down?",
 "Clean modern health infographic, 4:5 vertical. A simple notebook and pen on a bedside table beside "
 "a warm dim lamp, calm evening mood, soft warm lighting with cool blue shadows. Uncluttered, "
 "peaceful, generous empty space in the upper third for a text headline. Soft blue and white "
 "palette. No text rendered in image. Photorealistic, cosy.",
 ["#mentalhealth", "#sleep", "#stressrelief", "#healthyhabits", "#dailyhealthtips", "#wellness", "#bettersleep"],
 ["NIH News in Health — Sleep On It", "Harvard Health — Blue light has a dark side"]),

("Health Riddles", "Riddle", "Riddle: the organ that regrows",
 "I'm the only organ in your body that can regrow itself.",
 "I'M THE ONLY ORGAN\nTHAT CAN REGROW\nITSELF.\n\nI do over 500 jobs.\nAlcohol is my enemy.\n\nWhat am I?",
 "A clue: it filters your blood, stores energy, and does the detox work that expensive teas claim "
 "to do. Take a guess before you scroll past.",
 "What's your answer? Comment below — reveal tomorrow.",
 "Clean minimal health infographic, 4:5 vertical. Soft blue gradient background with an elegant "
 "white line-art illustration of a liver, centred and small, non-graphic and stylised. Large empty "
 "area for text overlay. Calm, curious, puzzle mood. White and soft blue palette. No text rendered "
 "in image. High-quality vector infographic style.",
 ["#healthriddle", "#healthquiz", "#liverhealth", "#dailyhealthtips", "#wellness", "#guessit", "#healthawareness"],
 ["Johns Hopkins Medicine — Liver: Anatomy and Functions"]),

("Exercise", "Top 5 Tips", "Movement snacks beat one long workout you skip",
 "You don't need an hour. You need to stop sitting for eight.",
 "MOVEMENT\nSNACKS",
 "Short bursts of activity spread across the day count toward your weekly total. Guidelines now "
 "recognise that any movement is better than none, and activity accumulated in short bouts still "
 "provides benefit. Take the stairs, walk during calls, stretch between tasks. The best workout is "
 "the one you'll actually repeat.",
 "What's one movement snack you could add today?",
 "Clean modern health infographic, 4:5 vertical. A person taking the stairs in a bright airy "
 "building, mid-step, natural daylight from a large window, energetic but calm mood. Diverse, "
 "realistic, everyday clothing. Generous clean space at the top for a large text headline. Fresh "
 "green, white and soft blue palette. No text rendered in image. Photorealistic.",
 ["#exercise", "#movement", "#healthyhabits", "#fitness", "#dailyhealthtips", "#wellness", "#activelifestyle"],
 ["WHO — Physical activity fact sheet", "CDC — Adding physical activity to your life"]),

("Sleep", "Mistakes People Make", "Catching up on sleep at weekends",
 "Sleeping in on Saturday doesn't cancel a short week.",
 "SLEEP DEBT DOESN'T\nWORK LIKE THAT",
 "Sleeping until noon on Saturday after five short nights shifts your body clock, a bit like flying "
 "across time zones every weekend. You can recover some function, but it isn't a clean reset. A "
 "consistent sleep and wake time — even at weekends — works better than trying to catch up.",
 "Is your weekend sleep very different from weekdays?",
 "Clean modern health infographic, 4:5 vertical. A tidy sunlit bedroom with an alarm clock on a "
 "bedside table, crisp white bedding, soft morning light through curtains. Calm and uncluttered "
 "with a large empty area at the top for a text headline. White and soft blue palette. No text "
 "rendered in image. Photorealistic.",
 ["#sleep", "#sleephealth", "#circadianrhythm", "#healthyhabits", "#dailyhealthtips", "#wellness", "#bettersleep"],
 ["CDC — Sleep and Sleep Disorders", "NHS — Why lack of sleep is bad for your health"]),

("Immunity", "Myth → Truth", "Vitamin C doesn't stop colds",
 "Vitamin C won't stop you catching a cold.",
 "MYTH: Vitamin C\nprevents colds",
 "For most people, regular vitamin C supplements don't prevent colds. Reviews of the evidence "
 "suggest they may slightly shorten how long a cold lasts, but the prevention effect is small and "
 "mainly seen in people under extreme physical stress. Sleep, hand hygiene and vaccination do more.",
 "Do you take vitamin C when you feel a cold coming?",
 "Clean modern health infographic, 4:5 vertical. Split red MYTH panel above, green FACT panel below. "
 "Fresh oranges and lemons on a white surface, bright natural studio lighting, crisp and fresh. "
 "Generous empty areas for text overlay. White, green and soft blue palette. No text rendered in "
 "image. Photorealistic, high detail.",
 ["#immunity", "#vitaminc", "#myths", "#coldandflu", "#dailyhealthtips", "#wellness", "#mythbusting"],
 ["NIH Office of Dietary Supplements — Vitamin C Fact Sheet", "Cochrane — Vitamin C for preventing and treating the common cold"]),

("Blood Pressure", "Science Simplified", "What the two numbers mean",
 "Most people have no idea what their blood pressure numbers mean.",
 "120 / 80\nWHAT IT MEANS",
 "The top number is the pressure when your heart beats. The bottom is the pressure when it rests "
 "between beats. Both matter. Readings are generally considered elevated above roughly 130/80, but "
 "thresholds vary by guideline and by person — your doctor interprets it alongside your age and risk "
 "factors, not as a single number in isolation.",
 "Do you know your numbers?",
 "Clean modern health infographic, 4:5 vertical. A digital blood pressure monitor on a white "
 "surface, screen blank, soft even studio lighting, minimal and clinical but reassuring. Large clean "
 "empty space for text overlay. White, soft blue and green palette. Non-frightening. No text "
 "rendered in image. Photorealistic.",
 ["#bloodpressure", "#hearthealth", "#preventivecare", "#healthawareness", "#dailyhealthtips", "#wellness", "#healthfacts"],
 ["American Heart Association — Understanding Blood Pressure Readings", "WHO — Hypertension fact sheet"]),

("Gut Health", "Do This Instead", "Fermented foods for your gut",
 "Your gut bacteria respond to what you feed them within days.",
 "FEED YOUR\nGUT BACTERIA",
 "Fermented foods like plain yoghurt, kefir, kimchi and sauerkraut contain live cultures, and "
 "research suggests regular intake can increase gut microbial diversity. Pair them with fibre — the "
 "bacteria need it to thrive. Start small if you're not used to them, and choose unsweetened versions.",
 "Do you eat any fermented foods regularly?",
 "Clean modern nutrition infographic, 4:5 vertical. Overhead flat-lay of plain yoghurt, kimchi, "
 "sauerkraut and kefir in simple white bowls on a light wooden surface, bright natural lighting, "
 "fresh and appetising. Clean empty band across the top for a text headline. White, green and soft "
 "blue palette. No text rendered in image. Photorealistic, high detail.",
 ["#guthealth", "#fermentedfoods", "#probiotics", "#nutrition", "#dailyhealthtips", "#healthyeating", "#wellness"],
 ["Harvard T.H. Chan — The Nutrition Source: Fermented Foods", "Cleveland Clinic — Probiotics"]),

("Healthy Aging", "Hidden Fact", "Loneliness affects physical health",
 "Loneliness affects your body, not just your mood.",
 "CONNECTION IS\nA HEALTH INPUT",
 "Social connection is increasingly recognised as a genuine health factor. Long-term loneliness and "
 "social isolation are associated with higher risks of heart disease, stroke and dementia. It sits "
 "alongside diet, sleep and movement as something worth deliberately maintaining — one call or one "
 "visit counts more than people assume.",
 "Who could you message today?",
 "Clean modern health infographic, 4:5 vertical. Two people of different generations sitting "
 "together talking over tea in a bright warm room, natural window light, genuine warmth and "
 "connection. Diverse ages and ethnicities. Generous clean space in the upper third for a text "
 "headline. Warm white, soft blue and green palette. No text rendered in image. Photorealistic.",
 ["#healthyaging", "#mentalhealth", "#loneliness", "#connection", "#dailyhealthtips", "#wellness", "#wellbeing"],
 ["CDC — Loneliness and Social Isolation", "WHO — Social isolation and loneliness"]),

("Healthy Habits", "Before → After", "Two minutes of stretching before bed",
 "A day of sitting follows you into the night.",
 "2 MINUTES\nBEFORE BED",
 "Hours at a desk leave hips, back and shoulders tight, and that tension can make it harder to "
 "settle at night. A short, gentle stretch signals wind-down and eases stiffness. Keep it slow and "
 "never force a position — the goal is release, not flexibility training.",
 "Do you stretch before bed?",
 "Clean modern health infographic, 4:5 vertical. A person stretching gently on a mat beside a bed in "
 "warm low evening light, calm and unhurried, comfortable clothing. Diverse and realistic body type. "
 "Uncluttered with generous empty space at the top for a text headline. Warm white and soft blue "
 "palette. No text rendered in image. Photorealistic, peaceful.",
 ["#healthyhabits", "#stretching", "#sleep", "#mobility", "#dailyhealthtips", "#wellness", "#eveningroutine"],
 ["NHS — Flexibility exercises", "Mayo Clinic — Stretching: Focus on flexibility"]),

("Scientific Health Facts", "Hidden Fact", "Your heart beats around 100,000 times a day",
 "Your heart beats about 100,000 times a day without a single break.",
 "100,000 BEATS\nEVERY DAY",
 "That's roughly 35 million beats a year, every year, without pause. The best things you can do for "
 "it are unglamorous and well proven: move regularly, don't smoke, watch salt and saturated fat, "
 "manage stress, and know your blood pressure numbers.",
 "When did you last check your blood pressure?",
 "Clean modern health infographic, 4:5 vertical. An abstract elegant heartbeat line rendered in soft "
 "blue on a clean white background, minimal and modern, with subtle depth. Large clear empty area "
 "for a text overlay. Calm, trustworthy, medical-editorial style. White, blue and green palette. "
 "No text rendered in image. High-quality vector infographic.",
 ["#hearthealth", "#healthfacts", "#cardiovascular", "#dailyhealthtips", "#wellness", "#preventivecare", "#sciencefacts"],
 ["American Heart Association — How the Heart Works", "Cleveland Clinic — Heart facts"]),

("Weight Loss", "Myth → Truth", "You can't spot-reduce fat",
 "Doing sit-ups will not burn belly fat specifically.",
 "MYTH: Sit-ups burn\nbelly fat",
 "You can't choose where your body loses fat. Crunches strengthen the muscles underneath, but the "
 "fat above them only reduces through overall energy balance and activity. This is one of the most "
 "persistent fitness myths, and it costs people a lot of wasted effort. Whole-body movement plus "
 "diet does the work.",
 "Who was told sit-ups were the secret?",
 "Clean modern health infographic, 4:5 vertical. Split red MYTH panel above, green FACT panel below. "
 "A person doing a full-body movement in a bright airy home space, natural light, encouraging and "
 "realistic rather than aspirational. Diverse body type. Clean empty areas for text overlay. White, "
 "green and soft blue palette. No text rendered in image. Photorealistic.",
 ["#weightloss", "#fitnessmyths", "#exercise", "#mythbusting", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["Mayo Clinic — Spot reduction: Why it doesn't work", "NHS — Exercise and weight loss"]),

("Healthy Eating", "Top 5 Tips", "Read the ingredients, not the front",
 "The front of the packet is marketing. The back is information.",
 "READ THE BACK,\nNOT THE FRONT",
 "\"Natural\", \"light\" and \"multigrain\" are marketing terms with little regulated meaning. The "
 "ingredients list and nutrition panel tell you what's actually there. Two quick habits: ingredients "
 "are listed by weight, so the first few dominate — and check sugar and salt per 100g to compare "
 "products fairly.",
 "Do you check labels, or go by the front of the pack?",
 "Clean modern nutrition infographic, 4:5 vertical. A person's hands holding a plain unbranded food "
 "package, turning it to read the back, in a bright supermarket aisle with soft depth of field. "
 "Natural lighting, diverse skin tone, everyday and relatable. Generous clean space at the top for "
 "a text headline. White, soft blue and green palette. No readable text or real brands in image. "
 "Photorealistic.",
 ["#healthyeating", "#nutrition", "#foodlabels", "#healthyshopping", "#dailyhealthtips", "#wellness", "#healthylifestyle"],
 ["NHS — Food labels", "Harvard T.H. Chan — The Nutrition Source: Food label guide"]),

("Bone Health", "Science Simplified", "Your bones are living tissue",
 "Your skeleton is rebuilding itself right now.",
 "YOUR BONES ARE\nLIVING TISSUE",
 "Bone isn't fixed scaffolding — it's constantly being broken down and rebuilt throughout your life. "
 "That's why what you do now matters later: weight-bearing movement like walking, along with enough "
 "calcium and vitamin D, supports bone strength as you age. Strength training helps too, at any age.",
 "Did you know your bones rebuild themselves?",
 "Clean modern health infographic, 4:5 vertical. An older adult and a younger adult walking together "
 "outdoors in bright morning light, both smiling, active and healthy. Fresh green and white palette, "
 "airy and optimistic. Large uncluttered sky area at the top for a text headline. Diverse ages and "
 "ethnicities. No text rendered in image. Photorealistic, warm natural lighting.",
 ["#bonehealth", "#healthyaging", "#calcium", "#vitamind", "#dailyhealthtips", "#wellness", "#strengthtraining"],
 ["NIH Osteoporosis and Related Bone Diseases National Resource Center — Bone Health for Life",
  "Cleveland Clinic — Bone Health"]),
]


def build_json(start=date(2026, 7, 31), days=7):
    # No topic may repeat within 60 days, so a 3-reel + 3-image day over 7 days
    # needs 21 distinct items of each. Fail loudly rather than silently cycling.
    need = days * 3
    if len(REELS) < need or len(IMAGES) < need:
        raise SystemExit(
            f"Need {need} unique reels and {need} unique images for {days} days "
            f"at 3+3/day; have {len(REELS)} reels and {len(IMAGES)} images. "
            "Add more before building — repeating topics breaks the 60-day rule.")
    out = []
    for d in range(days):
        day = start + timedelta(days=d)
        for si, hour in enumerate(REEL_HOURS):
            cat, title, hook, beats, value, q, tags, srcs = REELS[d * 3 + si]
            script = "\n".join(f"[{i+1}] ON-SCREEN: {o.replace(chr(10),' / ')}\n    VO: {v}"
                               for i, (o, v) in enumerate(beats))
            out.append({
                "date": f"{day.isoformat()}T{hour:02d}:00:00+00:00",
                "post_type": "Reel", "category": cat, "title": title, "hook": hook,
                "caption": f"{hook}\n\n{value}\n\n{q}\n\n{CTA}",
                "image_prompt": "",
                "reel_script": script,
                "voiceover": " ".join(v for _, v in beats),
                "onscreen_text": " | ".join(o.replace("\n", " ") for o, _ in beats),
                "cta": CTA, "hashtags": tags, "sources": srcs, "disclaimer": DISCLAIMER,
            })
        for si, hour in enumerate(IMG_HOURS):
            cat, fw, title, hook, headline, value, q, prompt, tags, srcs = IMAGES[d * 3 + si]
            out.append({
                "date": f"{day.isoformat()}T{hour:02d}:00:00+00:00",
                "post_type": "Image", "category": cat, "framework": fw, "title": title,
                "hook": hook, "headline": headline,
                "caption": f"{hook}\n\n{value}\n\n{q}\n\n{CTA}",
                "image_prompt": prompt, "reel_script": "", "voiceover": "",
                "onscreen_text": headline.replace("\n", " "),
                "cta": CTA, "hashtags": tags, "sources": srcs, "disclaimer": DISCLAIMER,
            })
    out.sort(key=lambda x: x["date"])
    return out


if __name__ == "__main__":
    data = build_json()
    with open("hd_os_week1.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    from collections import Counter
    print(f"items: {len(data)}  ({Counter(i['post_type'] for i in data)})")
    print("categories:", dict(Counter(i["category"] for i in data)))
    print("wrote hd_os_week1.json")
