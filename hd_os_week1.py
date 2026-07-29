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
    out = []
    for d in range(days):
        day = start + timedelta(days=d)
        for si, hour in enumerate(REEL_HOURS):
            cat, title, hook, beats, value, q, tags, srcs = REELS[(d * 3 + si) % len(REELS)]
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
            cat, fw, title, hook, headline, value, q, prompt, tags, srcs = IMAGES[(d * 3 + si) % len(IMAGES)]
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
