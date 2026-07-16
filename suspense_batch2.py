# -*- coding: utf-8 -*-
"""Suspense Ahead: 7-day every-3-hours batch (56 posts), Jul 16 09:00 UTC onward.
Builds images + queue.json items for the cloud runner. Calibrated per age-flag
rules: intrigue > menace, no explicit gore, third-person victims.
Formats: LS long story, MS micro story, R solvable riddle (+answer comment),
T theory/unsolved, W what-would-you-do, H2 two-sentence horror, HB heartbeat,
SMS chat story."""

FOLLOW = "\n\nFollow Suspense Ahead — one mystery every 3 hours."
GEO = "US,GB,IE,DE,FR,NL,BE,SE,NO,DK,FI,ES,IT,PT,AT,CH,PL,CZ"

# ---------------------------------------------------------------- pools

RIDDLES = [  # (card_text, caption, answer_comment)
("Two guards. Two doors.\nOne always lies.\nOne always tells the truth.\n\n*One question. One chance.* 👇",
 "🚪 One door leads out. One doesn't. You may ask ONE guard ONE question — but you don't know which guard lies.\n\nWhat do you ask? Answer in the first comment — but try first 👇" + FOLLOW,
 "🕵️ ANSWER: Ask either guard — \"Which door would the OTHER guard say leads out?\" Then pick the opposite door. The lie and the truth cancel each other. Got it right? 🧠👇"),
("The detective looked at the window once.\n\n*\"You broke it yourself,\"* he said.\n\nHow did he know? 👇",
 "🪟 A shop owner reports a break-in: \"They smashed the window and took everything.\" The detective looks at the window for five seconds and says: \"No one broke in. You did this.\"\n\nWhat did he see? Answer in the first comment 👇" + FOLLOW,
 "🕵️ ANSWER: The broken glass was lying OUTSIDE the shop. A window smashed from outside scatters glass INSIDE. It was broken from within. Did you spot it? 👇"),
("Born on the same day.\nSame mother. Same father.\n\nBut they are *not twins.*\n\nHow? 👇",
 "👶 Two children, born on the same day of the same year, to the same mother and father — yet the hospital records say they are NOT twins. The records are correct.\n\nHow is this possible? First comment has the answer 👇" + FOLLOW,
 "🕵️ ANSWER: They're two of TRIPLETS. Same birth, three children. The simplest answers hide best. 😏 Too easy or did it get you? 👇"),
("Every rainy day, he rides\nthe elevator to the *7th floor.*\n\nEvery sunny day — only the 5th.\n\nWhy? 👇",
 "🛗 A man lives on the 7th floor. On rainy days, he takes the elevator straight to 7. On sunny days, he gets off at 5 and walks two floors up. He isn't exercising.\n\nWhy? Answer in the first comment 👇" + FOLLOW,
 "🕵️ ANSWER: He's short. He can only reach the button for 5 — except on rainy days, when he has an umbrella to press 7. 🌂 Be honest — did you know this one? 👇"),
("Three doors. Three fates.\nDoor 1: searing flames.\nDoor 2: expert assassins.\nDoor 3: lions that haven't eaten in *3 months.*\n\nWhich door? 👇",
 "🚪 A classic that still fools people: you must pass through one door. Behind door 1 — a raging fire. Door 2 — trained assassins. Door 3 — lions that haven't eaten in three months.\n\nWhich one do you choose, and why? 👇" + FOLLOW,
 "🕵️ ANSWER: Door 3. Lions that haven't eaten in three months aren't hungry — they're gone. Nothing survives that long without food. 🦁 Did the fear almost trick you? 👇"),
("A field. A man. An *unopened package* beside him.\n\nThe closer they looked,\nthe stranger it got. 👇",
 "📦 A man is found in the middle of an empty field. No footprints lead to him. Beside him lies an unopened package. Investigators took one look at the package and closed the case.\n\nWhat was in it? First comment 👇" + FOLLOW,
 "🕵️ ANSWER: A parachute. It never opened. The 'package' told the whole story — sky, not field. 🪂 How fast did you get it? 👇"),
("She poured two identical drinks.\nHer guest drank fast — and was fine.\nShe drank slowly — and *collapsed.*\n\nSame drink. What happened? 👇",
 "🧊 Two glasses. Same pitcher, same iced drink. The guest, thirsty, finished hers in a minute — perfectly fine. The host sipped hers slowly over an hour — and ended the evening in the hospital.\n\nWhat was different? Answer below in the first comment 👇" + FOLLOW,
 "🕵️ ANSWER: It was in the ICE. Drunk fast, the ice hadn't melted yet. Sipped slowly, it dissolved into the drink. ❄️ Clever or cruel? 👇"),
("Midnight. A knock on your hotel door.\nA stranger: *\"Sorry — wrong room.\"*\n\nThe front desk says:\ncall security. Why? 👇",
 "🏨 You're in a hotel. At midnight, someone knocks. You open — a stranger looks surprised: \"Oh, sorry, I thought this was my room.\" He walks away. The receptionist tells you to report it immediately.\n\nWhy? First comment 👇" + FOLLOW,
 "🕵️ ANSWER: Nobody knocks on their OWN hotel room door. He was checking if the room was empty. 🚨 Would you have caught that in the moment? Honest answers 👇"),
("The ship's ladder hangs\n*6 rungs* above the water.\nThe tide rises 1 foot every hour.\n\nHow many rungs underwater\nafter 6 hours? 👇",
 "⚓ A rope ladder hangs off a ship, its lowest rung exactly at the water. Rungs are a foot apart. The tide rises one foot per hour. After six hours, how many rungs are underwater?\n\nThink carefully — first comment has it 👇" + FOLLOW,
 "🕵️ ANSWER: Zero. The ship FLOATS — it rises with the tide, ladder and all. 🚢 Did the math trap get you? 👇"),
("He said: *\"I was reading when\nthe power went out.\nI lost my page in the dark.\"*\n\nThe detective arrested him. Why? 👇",
 "🕯️ A man's study was searched after a robbery next door. His alibi: \"I was home reading by candlelight all evening. When the power went out around 9, I lost my page in the dark and went to bed.\"\n\nThe detective arrested him on the spot. What was the mistake? 👇" + FOLLOW,
 "🕵️ ANSWER: He said he was reading by CANDLELIGHT — a power cut wouldn't affect a candle. His 'dark' never happened. 🔍 Would you have caught the slip? 👇"),
("8 days.\nNo sleep.\nCompletely healthy.\n\n*How?* 👇",
 "😴 A woman went eight full days without sleeping — no coffee, no medical tricks, no harm done. Doctors found nothing unusual.\n\nHow did she do it? (The answer will annoy you.) First comment 👇" + FOLLOW,
 "🕵️ ANSWER: She slept at NIGHT. Eight DAYS without sleep — the days were never the problem. 😅 Annoyed? Tag someone this would fool 👇"),
("The stranger returned her wallet.\nEverything was there.\n\nShe thanked him —\nthen quietly called the police. *Why?* 👇",
 "👛 Her wallet vanished at the café. An hour later, a helpful stranger appeared at her door holding it: \"Found this on the street — everything should be there.\" It was: cards, cash, ID, untouched.\n\nShe smiled, thanked him… and dialed the police the moment he left. Why? 👇" + FOLLOW,
 "🕵️ ANSWER: She never told him where she lived — and her address isn't on anything… except the home address on her ID means he read through it, fine — but how did he know she'd LOST it rather than left it with a friend? He watched her. And the cash untouched means the wallet was never the point. 🚨 What was YOUR theory? 👇"),
]

THEORY = [  # (card_text or None, caption)
(None, "✈️ In 1971, a man in a business suit bought a $20 plane ticket under the name Dan Cooper.\n\nMid-flight, he calmly handed a note to a flight attendant. Hours later, he collected $200,000, ordered the plane back into the night sky — and jumped into a storm over the Washington forests with a parachute.\n\nThe FBI investigated for 45 YEARS. They interviewed a thousand suspects. In 2016, they officially gave up.\n\nNo body. No parachute. Only a small stack of his cash, found buried on a riverbank in 1980 — miles from any flight path that made sense.\n\nD.B. Cooper either died in those woods… or pulled off the only unsolved skyjacking in American history and lived quietly ever after.\n\n👇 Which is it? Dead in the trees — or grandpa somewhere, smiling at the news every anniversary?" + FOLLOW),
("A man found on a beach in 1948.\nNo ID. No labels in his clothes.\n\nIn his pocket: a scrap of paper —\n*\"Tamám Shud\" — \"it is ended.\"*\n\nNo one ever came for him. 👇",
 "🏖️ Adelaide, Australia, 1948. A well-dressed man found on Somerton Beach. Every label cut from his clothing. No wallet, no ID.\n\nIn a hidden pocket: a torn scrap reading \"Tamám Shud\" — Persian for \"it is ended\" — ripped from a rare book of poetry.\n\nWhen police found THE book, the back page held a phone number… and an uncrackable cipher.\n\nThe number belonged to a nurse living minutes from the beach. She denied knowing him. Witnesses said she nearly fainted when shown his photo.\n\nDNA finally gave him a name in 2022 — but not a reason. The cipher remains unsolved. The nurse took whatever she knew to her grave.\n\n👇 Spy? Rejected lover? Something else? Give us your theory." + FOLLOW),
(None, "🚢 In 1955, the MV Joyita was found drifting in the South Pacific — listing, engines dead, radio tuned to the distress channel.\n\nAll 25 people aboard: gone.\n\nHere's what makes it impossible to explain:\n— The ship was practically unsinkable (cork-lined hull).\n— The lifeboats were missing — but no distress call was ever received.\n— A doctor's bag sat open on deck, bloodied bandages beside it.\n— Every clock aboard had stopped at 10:25.\n— 4 tons of cargo had vanished with the people.\n\nThe official inquiry called the crew's fate \"inexplicable.\" Seventy years later, it still is. Twenty-five people left an unsinkable ship in the middle of the night — for nowhere.\n\n👇 Pirates? Mutiny? Something in the water? What empties an unsinkable ship?" + FOLLOW),
("For 19 years, a small Ohio town\nreceived thousands of letters.\n\nThe writer knew *everything* —\nsecrets no outsider could know.\n\nThey never caught him. 👇",
 "✉️ Circleville, Ohio, 1976. Residents start receiving letters — thousands over 19 years. The writer knew private things: affairs, debts, conversations held behind closed doors.\n\nA man went to prison for writing them. Here's the problem: the letters KEPT COMING while he was locked in a cell — postmarked from the same city, in the same handwriting.\n\nWhen he was released, they stopped.\n\nThe FBI analyzed everything. The writer was never identified. To this day, nobody knows who watched an entire town for two decades — or why.\n\n👇 The imprisoned man's accomplice? A neighbor everyone trusted? Who writes 19 years of letters and never slips once?" + FOLLOW),
(None, "📺 Chicago, November 22, 1987. During the evening news, every TV screen in the broadcast area glitches — and a man in a plastic mask hijacks two television stations in one night.\n\nThe first intrusion: 28 seconds of the masked figure swaying silently. The second, during Doctor Who: 90 seconds of distorted rambling before the signal cut.\n\nHijacking a broadcast tower requires serious engineering skill and equipment — this wasn't a prank from a basement. The FCC investigation went nowhere. Reddit spent decades on it. Nothing.\n\nWhoever did it needed professional knowledge, planning, and nerve — then never did it again, never bragged, never slipped.\n\nThe Max Headroom Incident remains the most famous unsolved broadcast intrusion in history.\n\n👇 Why hijack two TV stations… just to say nothing? Best theory gets pinned." + FOLLOW),
("A quiet farm town, 1994.\nRain fell six times that summer —\n\nbut it wasn't rain.\n\n*Gelatinous blobs.* And then people got sick. 👇",
 "🌧️ Oakville, Washington, August 1994. Six times in three weeks, rain fell carrying translucent, jelly-like blobs. Almost everyone who touched them developed flu-like symptoms. Cats and dogs in town reportedly fell ill.\n\nA lab technician who examined a sample found human white blood cells in it — then the sample mysteriously vanished from the lab.\n\nTheories: military waste dumping, jellyfish pulverized by bombing runs offshore, atmospheric experiments. The Air Force denied everything. No official explanation was ever given.\n\nThe blobs never fell again.\n\n👇 What fell on Oakville? And why did the samples disappear?" + FOLLOW),
(None, "🔊 There is a sound that only 2-4% of people can hear.\n\nThey call it The Hum — a low, diesel-engine drone that never stops. Reported in Taos (New Mexico), Bristol (England), Windsor (Canada) — always at night, always indoors, always when everything else is silent.\n\nIt's been studied since the 1970s. Ruled out: tinnitus (it stops when sufferers leave town), power lines, factories, traffic.\n\nSome researchers blame low-frequency industrial noise bouncing through bedrock. Others point to gas pipelines, military communications, or the ocean floor itself.\n\nNobody has ever found the source. People have moved houses, cities, even countries to escape it. Some say it followed them.\n\n👇 Can you hear a hum right now, in a silent room? You might be one of the 4%." + FOLLOW),
]

WWYD = [  # (card_text, caption)
("You're home alone.\nFrom the kitchen, you hear\nyour own voice say:\n\n*\"I'm in here.\"* 👇",
 "🌘 Rules: no calling anyone, the doors are locked, and you have to decide in 10 seconds.\n\nDo you check the kitchen — or walk straight out the front door?\n\nReact 🚪 for leave, 👀 for check. Explain yourself in the comments 👇" + FOLLOW),
("Your GPS says:\n*\"You have arrived home.\"*\n\nBut the house in front of you\nis not your house.\n\nThe porch light turns on. 👇",
 "🏠 Every turn was familiar. Every street was right. But the house at your address… isn't yours. And someone inside just noticed you.\n\nDo you knock, check the street sign, or reverse and drive away without looking back? 👇" + FOLLOW),
("A stranger stops you:\n*\"Don't take your usual shortcut today.\"*\n\nYou've never seen them before.\nThey walk away without explaining. 👇",
 "🚶 You never told anyone your route. You take the same shortcut every single day.\n\nToday — do you take it anyway, or go the long way and never find out what they meant?\n\nBe honest about what you'd ACTUALLY do 👇" + FOLLOW),
("Scrolling your own camera roll,\nyou find a photo of yourself —\n\n*asleep.*\n\nTaken from inside your room.\nDated three years ago. 👇",
 "📱 You lived alone three years ago.\n\nThe photo is real — it's in your camera roll's cloud backup, original metadata, your old bedroom.\n\nDo you show anyone? Delete it? Or scroll to see if there are more?\n\n(Important: would you even WANT to know if there are more?) 👇" + FOLLOW),
("In a crowd, you spot a face\nyou haven't thought about in 20 years:\n\nyour childhood imaginary friend.\n\nThey wave. *They remember you.* 👇",
 "🎈 Exactly how you pictured them at age six — but grown up, like they aged alongside you.\n\nThey're walking toward you, smiling like an old friend at a reunion.\n\nDo you wave back? Run? Ask them their name to test it?\n\nWhat's your move? 👇" + FOLLOW),
("The elevator stops on floor 4.\nNobody gets in.\n\nBut the button for your floor\n*un-presses itself.* 👇",
 "🛗 You're alone in the elevator. The doors close. And the panel now shows a floor you never pressed: the basement.\n\nDo you press your floor again, hit the emergency button, or ride it down to see what's there?\n\nReact 🔴 = emergency button, ⬇️ = ride it down. Comments: what happens next? 👇" + FOLLOW),
("Your video call froze.\nTheir face stuck mid-sentence.\n\nBut the room behind them\n*kept moving.* 👇",
 "💻 The call \"froze\" — frozen face, frozen voice. Except the curtain behind them is still swaying. The door behind them is now open; it was closed a second ago.\n\nDo you say something? Hang up? Screenshot it?\n\nAnd the real question: do you tell THEM what you saw? 👇" + FOLLOW),
]

H2 = [  # two-sentence horror — (card_text, caption)
("My daughter won't stop crying\nand screaming in the middle of the night.\n\nI visit her grave and ask her\nto stop — *but it doesn't help.*",
 "😨 Two sentences. That's all a story needs.\n\nCan you write a scarier one in two sentences? Best one gets pinned 📌👇" + FOLLOW),
("The last man on Earth\nsat alone in a room.\n\nThere was a *knock* on the door.",
 "🚪 The oldest two-sentence chiller ever written — and still undefeated.\n\nYour turn: continue the story in ONE sentence. What's on the other side of that door? 👇" + FOLLOW),
("My reflection just smiled at me.\n\nI wasn't smiling back.",
 "🪞 Quick — look at your phone's black screen right now.\n\nStill just you? Good. Keep it that way.\n\nTwo-sentence horror night: drop yours below. The best one gets pinned 📌👇" + FOLLOW),
("I always thought my cat stared at me\nwhile I slept.\n\nLast night I realized she's staring at something *behind* me.",
 "🐈 Pet owners know: when they stare at nothing… it's never nothing.\n\nWhat does YOUR pet stare at? Tell us the spot in your house 👇" + FOLLOW),
("The babysitter called us, annoyed:\n*\"You forgot to tell me your son sleepwalks.\"*\n\nOur son is at his grandmother's tonight.",
 "😰 Every parent just felt that one.\n\nRate the chill 1-10, and drop a two-sentence story of your own below 👇" + FOLLOW),
("I saw my wife wave at me\nfrom the kitchen window\nas I pulled into the driveway.\n\nShe's been at her sister's since Monday — *she just texted me from there.*",
 "🏡 The wave is what gets me. Not hiding. WAVING.\n\nWould you go inside? Honest answers only 👇" + FOLLOW),
("Day 1,847 of being trapped in this room.\n\nToday, for the first time,\none of my captors *looked directly into the camera.*",
 "📹 Read it twice. Then read it once more.\n\n(Got it? Don't spoil it — just type \"I saw it\" 👀 and let others suffer.) 👇" + FOLLOW),
("My smart speaker said:\n*\"Goodnight, both of you.\"*\n\nI live alone.",
 "🔊 Technology never lies. That's the problem.\n\nWhat's the creepiest thing a device has ever done to you? True stories only 👇" + FOLLOW),
("The photo of our camping trip\nfinally got developed.\n\nIn every single picture,\nthere's one extra tent.",
 "🏕️ Six friends. Five tents. Count them again.\n\nCamping horror stories — has anything unexplainable happened to you outdoors? 👇" + FOLLOW),
]

MICRO = [  # text-only micro stories
"""The night guard's log, Tuesday, 2:14 AM:

"Motion sensor, east wing. Checked. Nothing."

2:37 AM: "Motion sensor, east wing. Checked. Nothing."

2:58 AM: "Motion sensor, east wing. I'm not checking again. It stands very still and it looks almost like a coat rack, and I have decided it is a coat rack."

Wednesday's log, different handwriting:

"New guard starts tonight. East wing sensor removed per request. There is no coat rack in the east wing inventory."

👇 Would you have checked a third time?""" + FOLLOW,
"""My grandmother had a rule: always say "excuse me" when you walk through a cold spot in the house.

We laughed at her. Old superstitions.

After she passed, we cleared out the house. Boxes, dust, memories. My brother walked through the hallway and shivered — "Cold spot," he smirked. "Excuuuse me."

From the empty bedroom, my grandmother's voice, warm as ever:

"You're excused, sweetheart."

We finished packing outside. Both of us. In the rain.

👇 Superstition from your family that you secretly still follow?""" + FOLLOW,
"""The wrong-number text said: "Stop wearing the blue jacket. It makes you too easy to follow."

I typed back: "Wrong number — and I'm not wearing a blue jacket."

"Of course not. You took it off when you sat down by the window."

I looked down at the blue jacket on the back of my café chair.

Three dots appeared. Then: "Sorry. Wrong number."

The dots never came back. I've never worn the jacket again.

👇 What would your reply have been?""" + FOLLOW,
"""Hotel review, 1 star:

"Room was clean, staff polite. BUT at 3 AM someone kept sliding papers under my door. Blank pages, over and over. When I finally opened the door, the hallway was empty — and my missing luggage tag was taped to the outside of my door. I checked out immediately."

Hotel's reply, posted publicly:

"Dear guest — we apologize. However, our records show your room was our only occupied room that night, and Room 4 has no door gap. We do not have a Room 4."

The review was for Room 4.

👇 Which detail bothers you most?""" + FOLLOW,
"""My son's drawing was taped to the fridge: our family — me, his mom, him, and the dog. And one extra figure, taller than all of us, standing slightly apart.

"Who's that, buddy?"

"That's the quiet man. He doesn't like being drawn."

We framed it as a funny kid story. Kids draw weird things.

Yesterday my son ran up, upset, and tore the drawing off the fridge.

"He says I have to draw him CLOSER now."

👇 Parents: creepiest thing your kid has ever said? (The comments on these are always gold.)""" + FOLLOW,
"""The radio station's final broadcast, 1974, ended like every night: "Goodnight, listeners. See you tomorrow."

The station closed that night. License expired. Tower dismantled two years later.

In 2009, a trucker on Route 9 caught a signal on the old frequency. Static, then a warm voice: "Goodnight, listeners. See you tomorrow."

He reported it as a prank. The FCC found nothing broadcasting within 400 miles.

He drives a different route now. Not because of the voice, he says.

Because it knew his name.

👇 Late-night drivers: what have you heard on empty roads?""" + FOLLOW,
"""Estate sale listing: "Antique mirror, mahogany frame, 1890s. $40. Sold as-is. Please do not ask about the tape."

Every inch of the glass was covered in old masking tape, layer over layer, brittle with age.

The seller — the family's granddaughter — would only say: "Grandmother taped it the night grandfather passed. She said he kept being late."

"Late for what?"

"For his reflection. It kept arriving a few seconds after him."

The mirror sold in an hour. The buyer left a review last month: five stars.

"Removed the tape. He's very punctual now."

👇 Would you buy it? $40 is $40.""" + FOLLOW,
]

STORIES = [  # long prime-time stories, text-only
"""The call center where I worked nights had one rule nobody explained: if a caller stays silent, you may hang up after ten seconds — except on line 9. On line 9, you wait.

Line 9 rang maybe once a month. Always 3-4 AM. Always silence — but not empty silence. Breathing. Distant sounds. Once, faint music from a kitchen radio.

I asked my supervisor who it was. She said: "Someone who needs to know a person is there. You want the job, you wait on line 9."

For two years, I waited. Sometimes twenty minutes. The caller never spoke. But right before hanging up, every time — a whisper: "Thank you."

My last week, line 9 rang. Silence. Breathing. Then, for the first time, a full sentence:

"You can stop waiting now. I found everyone I was looking for."

The next morning, corporate emailed: line 9 had been disconnected for non-payment.

It had been disconnected for six years.

👇 Would you have kept answering? Follow for one story every night.""" + FOLLOW,
"""My carpool app matched me with the same driver three days in a row. Different cities. I was traveling for work — Cleveland, then Columbus, then Cincinnati. Same driver. Same gray sedan. Same air freshener shaped like a lighthouse.

Day three, I joked about it: "You following me, Dan?"

He didn't laugh. He pulled over, calm as anything, and said: "I drive one city. I've never left Columbus. What are the other rides you're talking about?"

We compared apps. His ride history showed only our Columbus trip. Mine showed all three — same name, same face, same license plate. He photographed my screen with shaking hands and asked me to email him the screenshots.

He canceled the ride. Left me on the shoulder of the interstate.

That night, a new notification: "Your driver Dan is arriving."

I hadn't booked a ride.

I don't use the app anymore. But every few weeks, in whatever city work sends me to, a gray sedan with a lighthouse air freshener drives past my hotel. Slowly.

👇 Coincidence has a limit. What's yours?""" + FOLLOW,
"""My grandfather was a lighthouse keeper for 41 years. When he retired, they gave him a plaque and the old logbook — decades of his own tidy handwriting.

Going through his things last spring, I read it. Mostly weather. Ship names. Repairs.

But every year, on March 9th, the same entry. No weather. No ships. Just one line:

1961: "Answered the bell. Told them: not yet."
1974: "Answered the bell. Not yet."
1988: "Bell again. NOT YET."
2003, his last year, in shakier writing: "Answered the bell. Told them: soon."

There is no bell at that lighthouse. I checked the maritime records, the blueprints, everything. No bell, no buoy, nothing that rings.

Grandfather passed away peacefully last March. The 9th.

The new keeper posts updates on the lighthouse's little Facebook page. Two weeks ago: "Weird one tonight — anyone else near the point hear a bell?"

I haven't told him. I'm not sure 'not yet' is mine to say.

👇 Would you tell him? One story every night — follow so you don't miss tomorrow's.""" + FOLLOW,
"""The apartment was perfect and $400 under market. The landlord's only quirk: "Rent includes the hall closet staying locked. It's grandfathered storage. Never opened, never a problem."

Fine by me. For a year, no problem — until the building's pipes burst and every unit had to be drained and inspected. Management sent a locksmith for the closet.

I stayed home to watch. Nosy? Absolutely.

The locksmith opened it in thirty seconds. Inside: nothing. Empty shelf paper, a bare bulb, dust.

And on the inside of the door — dozens of tally marks scratched into the paint, grouped in fives. Under them, in old pencil, a child's handwriting:

"Days since it knocked back: "

The count after it was scratched out. Rewritten. Scratched out again. The last number I could make out was 3.

The locksmith looked at it for a while. Then he re-locked the door, no charge, and told me: "Tell management it's rusted shut, yeah?"

We both got quieter after that. The rent's still cheap. The closet stays locked.

Some discounts explain themselves eventually.

👇 Would you have knocked? Be honest.""" + FOLLOW,
"""Every small town has a house kids dare each other to touch. Ours was the Merrin place — empty since before anyone could remember, taxes somehow always paid.

The dare was simple: knock three times, count to ten, run.

Nobody ever finished counting. You'd knock, and before you hit 'four' or 'five,' you'd hear footsteps inside walking TOWARD the door — unhurried, heavy, certain. Every kid in town knew those footsteps. Forty years of kids.

Here's what I never told anyone. The summer I was twelve, I didn't run. I froze. The count in my head reached ten.

The footsteps stopped on the other side of the door. A letter slot I'd never noticed creaked open, and a voice — patient, pleasant, like a shopkeeper's — said:

"Ten. Finally. Come back when you remember this house, and I'll tell you what you win."

I'm 43 now. I moved away, married, built a life. Last month my mother mentioned, offhand: "They finally sold the Merrin place. New owner's been asking around about a boy who finished counting."

I remember the house. I have not gone back.

👇 Finish the count or run? One story every night at 8 — follow Suspense Ahead.""" + FOLLOW,
"""I proofread audiobooks for a living. Publishers send me the narrator's raw audio; I flag mistakes against the manuscript. Mispronunciations, skipped lines. Routine.

Last October, a thriller novel, chapter 14. The narrator read a paragraph that wasn't in my manuscript:

"She checks the peephole twice now. Good habit. The chain, though — she forgets the chain on Tuesdays, when the laundry makes her rush."

I flagged it: 'Not in text — please cut.' The studio replied: "Our file has no such line. Timestamp?"

I sent the timestamp. They sent back that section of their master recording. The paragraph wasn't in it. Same session, same file size, one paragraph difference — only on my copy.

I'd have called it a glitch and moved on. Except I do my laundry on Tuesdays. And that night, for the first time, I noticed how often I'd been leaving the chain off.

I use the chain every day now. I also quit thrillers — I only proof cookbooks and biographies.

Last week, a biography's narrator paused mid-sentence, off-script, and said quietly: "Better. The chain suits you."

👇 The scariest part isn't being watched. It's being COACHED. Follow for tomorrow night's story.""" + FOLLOW,
"""The overnight stocker at our grocery store, Marcus, swore the intercom sometimes paged names of people who weren't there. We ribbed him about it for years.

"Attention: Daniel, please come to register three." No Daniel on shift. No Daniel on the schedule. Store empty except us.

It happened maybe twice a year. Always a different name. Always register three — a register we stopped using after remodeling in 2015, but never removed.

Marcus kept a list taped inside his locker. Eleven names over nine years. He called it his "roll call."

Here's where I stop being able to explain things. Marcus started noticing the names in the local paper — weeks or months after each page. Small stories. A retirement. An award. An obituary. Every name, eventually, passed through that paper. A town of 40,000 people; maybe it's odds.

The last page came in June, clear as a morning announcement:

"Attention: Marcus, please come to register three."

Marcus didn't go. Marcus put in his notice, moved to his brother's in Arizona, and blocked us all "just for a while."

The store's quiet now. Nobody's been paged since.

Register three's light turns on by itself some nights. We unplugged it in July.

It's on right now.

👇 Would you have answered the page? Follow — a new story every night at 8.""" + FOLLOW,
]

HB = [  # heartbeats — text-only quickies
"Fill in the blank:\n\nThe scariest sound at 3 AM is ____.\n\n(Wrong answers also accepted 😅)👇" + FOLLOW,
"One word. The creepiest place you've ever been.\n\nJust one word — let everyone's imagination do the rest 👇" + FOLLOW,
"Finish the sentence:\n\n\"I stopped going there after ____.\"\n\nTrue stories get pinned 📌👇" + FOLLOW,
"You're a character in a horror movie.\n\nThe last emoji you used is now your role in the film. 💀\n\nPost it below — no cheating, no scrolling back 👇" + FOLLOW,
"Unpopular horror opinion. Drop yours.\n\nWe'll start: jump scares are the laziest form of fear. Fight us 👇" + FOLLOW,
"Rate your fear 1-10:\n\n🌊 Deep, open ocean at night.\n\n(If you said 1, you've never actually thought about it.) 👇" + FOLLOW,
"What's a completely normal sound that instantly unsettles you?\n\nOurs: a phone vibrating in an empty room 👇" + FOLLOW,
]

SMS_STORIES = [  # (messages, contact, time_label, caption)
([("in", "Hey, it's your neighbor from 3B. Sorry for the late text."),
  ("out", "no worries, what's up?"),
  ("in", "Could you stop pacing? It's right above my bedroom and it's been hours."),
  ("out", "I'm not home. I'm at my parents' this week."),
  ("in", "…"),
  ("in", "Then please tell me you left your TV on."),
  ("out", "I don't own a TV")],
 "Neighbor 3B", "Today 1:12 AM",
 "📱 She never answered the last question.\n\nWhat's the move here — call the building manager at 1 AM, or read these messages again from your parents' guest room and not sleep?\n\n👇 What would YOU text back?" + FOLLOW),
([("in", "Your package was delivered."),
  ("out", "I didn't order anything?"),
  ("in", "Delivered to: front porch. Signed by: resident."),
  ("out", "nobody's home, I'm at work"),
  ("in", "Signature on file: [your name]"),
  ("in", "Delivery photo attached: your front door, slightly open."),
  ("out", "I locked that door.")],
 "Delivery Updates", "Today 2:47 PM",
 "📦 The signature is yours. The door is open. You're 40 minutes away.\n\nDo you: call a neighbor, call the police, or drive home and open that package?\n\nAnd the question nobody's asking — what's IN the box you never ordered? Theories below 👇" + FOLLOW),
([("in", "Mom: Dinner's ready, come downstairs ❤️"),
  ("out", "coming!"),
  ("in", "Mom: Hurry before it gets cold"),
  ("out", "on my way down"),
  ("in", "Mom: Sweetheart, I just got home. I haven't started dinner."),
  ("in", "Mom: Who told you to come downstairs?")],
 "Mom ❤️", "Today 7:03 PM",
 "🍽️ Read the timestamps again. Both messages. Same contact.\n\nThe kitchen light is on. Something smells amazing. Your mom's car is just pulling into the driveway.\n\nDo you go downstairs? 👇" + FOLLOW),
]

# ---------------------------------------------------------------- schedule builder

def build_items():
    """56 slots, every 3h from 2026-07-16T09:00Z. Returns queue items + render jobs."""
    from datetime import datetime, timedelta, timezone
    base = datetime(2026, 7, 16, 9, 0, tzinfo=timezone.utc)
    items, renders = [], []
    ri = ti = wi = hi = mi = si = bi = smi = 0
    for k in range(56):
        when = (base + timedelta(hours=3 * k)).isoformat()
        hour = (9 + 3 * k) % 24
        item = {"id": f"sa2-{k:02d}", "account": "suspense-ahead",
                "network": "facebook", "geo_countries": GEO,
                "when": when, "status": "pending"}
        if hour == 0 and si < len(STORIES):      # prime long story
            item |= {"type": "text", "message": STORIES[si]}; si += 1
        elif hour == 3 and wi < len(WWYD):        # late-night WWYD card
            card, cap = WWYD[wi]; wi += 1
            img = f"images/suspense/b2_w{wi:02d}.png"
            renders.append(("card", card, img, "What Would You Do", "🌒"))
            item |= {"type": "photo", "message": cap, "image_url": img}
        elif hour == 6 and ri < len(RIDDLES):     # EU-morning riddle
            card, cap, ans = RIDDLES[ri]; ri += 1
            img = f"images/suspense/b2_r{ri:02d}.png"
            renders.append(("card", card, img, "Detective Riddle", "🕵️"))
            item |= {"type": "photo", "message": cap, "image_url": img,
                     "first_comment": ans}
        elif hour == 9 and mi < len(MICRO):       # micro story
            item |= {"type": "text", "message": MICRO[mi]}; mi += 1
        elif hour == 12 and ri < len(RIDDLES):    # midday riddle
            card, cap, ans = RIDDLES[ri]; ri += 1
            img = f"images/suspense/b2_r{ri:02d}.png"
            renders.append(("card", card, img, "Detective Riddle", "🔍"))
            item |= {"type": "photo", "message": cap, "image_url": img,
                     "first_comment": ans}
        elif hour == 15 and bi < len(HB):         # heartbeat
            item |= {"type": "text", "message": HB[bi]}; bi += 1
        elif hour == 18 and (ti < len(THEORY) or smi < len(SMS_STORIES)):
            # alternate theory <-> SMS across the week's 18:00 slots
            want_sms = (((k - 3) // 8) % 2 == 1)
            if (want_sms and smi < len(SMS_STORIES)) or ti >= len(THEORY):
                msgs, contact, tl, cap = SMS_STORIES[smi]; smi += 1
                img = f"images/suspense/b2_s{smi:02d}.png"
                renders.append(("sms", msgs, img, contact, tl))
                item |= {"type": "photo", "message": cap, "image_url": img}
            else:
                card, cap = THEORY[ti]; ti += 1
                if card:
                    img = f"images/suspense/b2_t{ti:02d}.png"
                    renders.append(("card", card, img, "Unsolved", "🗂️"))
                    item |= {"type": "photo", "message": cap, "image_url": img}
                else:
                    item |= {"type": "text", "message": cap}
        elif hour == 21 and hi < len(H2):         # two-sentence horror card
            card, cap = H2[hi]; hi += 1
            img = f"images/suspense/b2_h{hi:02d}.png"
            renders.append(("card", card, img, "Two-Sentence Horror", ""))
            item |= {"type": "photo", "message": cap, "image_url": img}
        else:  # pool exhausted for this hour — fall back to remaining pools
            if ti < len(THEORY):
                card, cap = THEORY[ti]; ti += 1
                item |= {"type": "text", "message": cap}
            elif hi < len(H2):
                card, cap = H2[hi]; hi += 1
                item |= {"type": "text", "message": card.replace("*", "") + "\n\n" + cap}
            elif bi < len(HB):
                item |= {"type": "text", "message": HB[bi]}; bi += 1
            else:
                continue  # skip slot if truly out of content
        items.append(item)
    return items, renders
