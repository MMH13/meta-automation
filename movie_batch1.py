# -*- coding: utf-8 -*-
"""Top Movie Reviews — launch batch, 3/day x 7 days = 21 posts.
English, geo-gated US+EU. ORIGINAL text only — no posters, stills, or clips.
Entry: (kind, payload, caption)
  review -> (title, year, rating, verdict, line, genre)
  list   -> (title_html, items, kicker)
  take   -> (text, kicker, emoji)
"""

F = "\n\n🎬 Follow Top Movie Reviews — an honest verdict every day."

POSTS = [
# ---------------- DAY 1 ----------------
("review", ("Sicario", 2015, 4.5, "WORTH IT",
  "Villeneuve turns a border raid into 90 minutes of held breath. Deakins shoots the desert like a warning.", "Thriller"),
 """🎬 SICARIO (2015) — 4.5/5

Most thrillers tell you who to root for. This one refuses.

Emily Blunt plays an FBI agent dropped into an operation nobody will explain to her — and Villeneuve makes you share her confusion instead of explaining it away. You're never ahead of the story. You're never comfortable.

The tunnel sequence is one of the most tense stretches of the last decade, and it works because Roger Deakins shoots it in near-darkness and lets you strain to see.

Then Benicio del Toro walks off with the entire film in the last twenty minutes.

Not a fun watch. A great one.

💬 Have you seen it? Rate it out of 5 in the comments 👇""" + F),
("list", ("Underrated <em>Thrillers</em><br>You Probably Missed",
  ["Prisoners (2013)", "Nightcrawler (2014)", "Wind River (2017)",
   "The Guilty (2018, Danish)", "Coherence (2013)"], "THE WATCHLIST"),
 """🔖 Five thrillers that deserved a much bigger audience:

1️⃣ PRISONERS — Jackman and Gyllenhaal, and a moral question with no clean answer. Two and a half hours that feel like ninety minutes.

2️⃣ NIGHTCRAWLER — Gyllenhaal again, playing something not quite human. LA has never looked more sinister.

3️⃣ WIND RIVER — quiet, cold, devastating. The most underrated of the Sheridan scripts.

4️⃣ THE GUILTY (the Danish original) — one man, one room, one phone. Somehow unbearable.

5️⃣ COHERENCE — made for almost nothing, and it'll wreck your brain for a week.

📌 Save this for your next "nothing to watch" night.

💬 Which one have you already seen? And what would YOU add to this list? 👇""" + F),
("take", ("A movie can be\n*perfectly made*\nand still\n*forgettable.*", "HOT TAKE", "🎬"),
 """🎬 Controversial, but I'll die on this hill.

Technical perfection isn't the same as impact. Some films are flawlessly shot, scored, and acted — and you've forgotten them by the car park.

Meanwhile a rough, uneven, slightly messy film can live in your head for years, because it actually made you FEEL something.

Craft gets you a good film. Something riskier gets you a memorable one.

💬 Name a "technically brilliant" movie you found totally forgettable. Be brave 👇""" + F),
# ---------------- DAY 2 ----------------
("review", ("Parasite", 2019, 5.0, "MASTERPIECE",
  "Bong Joon-ho builds a comedy, then quietly removes the floor. Nothing prepares you for the second half.", "Thriller"),
 """🎬 PARASITE (2019) — 5/5

The rare film that deserved every award it got.

It starts as a comedy. A poor family cons their way into a rich household, one job at a time, and it's genuinely funny — you're enjoying the scheme.

Then a doorbell rings, and Bong Joon-ho pulls the floor out. Literally.

What makes it a masterpiece isn't the twist — it's that the film never tells you who to blame. Nobody here is a villain. Everybody's just trying to climb, and the architecture won't let them all fit.

That final shot of the stairs. That's the whole movie.

💬 Where does it rank in YOUR all-time top 10? 👇""" + F),
("list", ("Movies With <em>Perfect</em><br>Endings",
  ["The Prestige (2006)", "Whiplash (2014)", "No Country for Old Men (2007)",
   "Arrival (2016)", "The Truman Show (1998)"], "THE WATCHLIST"),
 """🎯 An ending can save a film — or ruin one. These five stick the landing perfectly.

1️⃣ THE PRESTIGE — the answer was on screen the whole time. Rewatch it and feel stupid, happily.

2️⃣ WHIPLASH — no dialogue in the last nine minutes. None needed.

3️⃣ NO COUNTRY FOR OLD MEN — people hated it in 2007. They were wrong.

4️⃣ ARRIVAL — turns the entire film into a different film, retroactively.

5️⃣ THE TRUMAN SHOW — "Good morning, and in case I don't see ya…" Still perfect.

💬 What's the best final scene in movie history? One answer only 👇""" + F),
("take", ("The best twist isn't\nthe one you *never saw coming.*\n\nIt's the one you\n*should have.*", "HOT TAKE", "🌀"),
 """🌀 A cheap twist hides information from you.

A great twist shows you everything — and trusts you to miss it. Then when it lands, you don't feel tricked. You feel like you were part of it.

That's the difference between "wait, WHAT?" and "…oh. OH."

The Sixth Sense. The Prestige. Fight Club. All of them play fair. The clues were sitting there the entire time.

💬 Which movie twist did YOU actually see coming? And which one destroyed you? 👇""" + F),
# ---------------- DAY 3 ----------------
("review", ("Whiplash", 2014, 5.0, "MASTERPIECE",
  "A 106-minute panic attack about the price of greatness — and it refuses to tell you whether it was worth it.", "Drama"),
 """🎬 WHIPLASH (2014) — 5/5

It's a movie about a drummer. It plays like a thriller.

Miles Teller wants to be great. J.K. Simmons wants to make him great, and doesn't care what it costs. The film's genius is that it never picks a side — it just shows you the bill.

That last nine minutes might be the best-edited sequence of the 2010s. No speeches. No hug. Just two people finally understanding each other through a drum solo.

And then it ends. Immediately. Before you can decide whether that was a triumph or a tragedy.

Still arguing about it a decade later.

💬 Was Fletcher right? Genuinely — argue it out below 👇""" + F),
("list", ("Great Films Under<br><em>100 Minutes</em>",
  ["Whiplash (2014) — 106", "Run Lola Run (1998) — 81",
   "Before Sunrise (1995) — 101", "Toy Story (1995) — 81",
   "12 Angry Men (1957) — 96"], "THE WATCHLIST"),
 """⏱️ Not every great film needs three hours.

Some of the best movies ever made are done before your dinner gets cold:

1️⃣ WHIPLASH — 106 minutes and not one wasted
2️⃣ RUN LOLA RUN — 81 minutes at a full sprint
3️⃣ BEFORE SUNRISE — two people, one night, no plot, perfect
4️⃣ TOY STORY — 81 minutes that changed animation forever
5️⃣ 12 ANGRY MEN — one room, 96 minutes, still unbeaten

The modern 3-hour runtime is a choice, not a requirement.

💬 What's the best short film (under 100 min) you've ever seen? 👇""" + F),
("take", ("*Rewatching* a film\nyou love isn't\nwasting time.\n\nIt's *reading a book twice.*", "TAKE", "🔁"),
 """🔁 Nobody says "why would you read that book again?"

But rewatch a film and suddenly you're wasting your evening.

Here's the thing — a good film changes when you already know the ending. You stop watching the plot and start watching the CRAFT. The setups you missed. The performance choices. The shot that meant nothing the first time and everything now.

Some films only truly begin on the second watch.

💬 What movie have you rewatched the most? Honest count 👇""" + F),
# ---------------- DAY 4 ----------------
("review", ("Arrival", 2016, 4.5, "WORTH IT",
  "A first-contact film where the weapon is grammar. Quiet, patient, and it rewires the whole story in one line.", "Sci-Fi"),
 """🎬 ARRIVAL (2016) — 4.5/5

The rare sci-fi film where nobody shoots anything.

Aliens arrive. The world panics. And the hero is… a linguist. The entire plot is about learning to communicate — and Villeneuve makes that more tense than any invasion.

Amy Adams gives one of the great restrained performances. Half of it is just her face processing something impossible.

And then the film says one sentence near the end that reframes literally everything you just watched. Not a gotcha. A gut punch.

Watch it twice. It's a different film the second time.

💬 Did you figure it out before the reveal? Honest answers 👇""" + F),
("list", ("Sci-Fi That Isn't<br>About <em>Space</em>",
  ["Arrival (2016)", "Ex Machina (2014)", "Her (2013)",
   "Children of Men (2006)", "Gattaca (1997)"], "THE WATCHLIST"),
 """🚀 Sci-fi doesn't need spaceships. The best of it is about us.

1️⃣ ARRIVAL — language, grief, and time
2️⃣ EX MACHINA — three characters, one house, deeply unsettling
3️⃣ HER — the most believable near-future ever filmed, and it's a love story
4️⃣ CHILDREN OF MEN — that single-take car scene still hasn't been topped
5️⃣ GATTACA — 1997, and more relevant every single year

No lasers. Just very good questions.

💬 Which is the best sci-fi film of the last 25 years? Fight it out 👇""" + F),
("take", ("*Subtitles* aren't work.\n\nThey're the price of\nthe *other 90%*\nof cinema.", "TAKE", "🌍"),
 """🌍 "I don't do subtitles" is the most expensive sentence in film.

You're not avoiding effort — you're avoiding Parasite. Oldboy. Amélie. Spirited Away. City of God. Pan's Labyrinth. Drive My Car. Society of the Snow.

Ten minutes in, your brain stops noticing them. That's it. That's the entire barrier.

Bong Joon-ho said it best: "Once you overcome the one-inch-tall barrier of subtitles, you'll be introduced to so many more amazing films."

💬 What's the best non-English film you've ever seen? Recommend one below 👇""" + F),
# ---------------- DAY 5 ----------------
("review", ("The Prestige", 2006, 4.5, "WORTH IT",
  "Nolan's most rewatchable film. It tells you the trick in the first line, then spends two hours proving you weren't watching.", "Mystery"),
 """🎬 THE PRESTIGE (2006) — 4.5/5

"Are you watching closely?"

The film opens by telling you it's going to fool you. Then it does it anyway. That's the flex.

Two magicians destroy each other's lives over an obsession — and Nolan structures the whole thing like the magic trick it describes: pledge, turn, prestige. The film IS the trick.

The reason it's endlessly rewatchable: every single clue is on screen. The answer is in the first five minutes. You just weren't watching closely.

Bale and Jackman are both excellent, but the film's real trick is that it's about the cost of obsession — and it makes you complicit in it.

💬 Did you catch it on the first watch? Nobody will believe you 👇""" + F),
("list", ("Movies That Get<br><em>Better</em> On Rewatch",
  ["The Prestige (2006)", "Arrival (2016)", "Fight Club (1999)",
   "Shutter Island (2010)", "Memento (2000)"], "THE WATCHLIST"),
 """🔁 Some films are built to be watched twice. These five reward it most:

1️⃣ THE PRESTIGE — the answer is in the opening line
2️⃣ ARRIVAL — becomes a completely different story
3️⃣ FIGHT CLUB — Tyler is in the background before you meet him
4️⃣ SHUTTER ISLAND — every single character is performing
5️⃣ MEMENTO — good luck ever seeing it "properly" once

The first watch is the plot. The second watch is the film.

💬 Which movie hit you HARDER the second time? 👇""" + F),
("take", ("Nolan\n*or*\nVilleneuve?\n\nPick one. *Defend it.*", "THIS OR THAT", "🎥"),
 """🎥 Two of the biggest directors working. Both do big ideas on a huge canvas. Only one can win.

🔵 NOLAN — Inception, The Prestige, Interstellar, Oppenheimer, The Dark Knight. Puzzle-box structure, practical effects, time as a weapon.

🟠 VILLENEUVE — Sicario, Arrival, Blade Runner 2049, Dune. Patience, dread, and the best visual eye of his generation.

No fence-sitting. One name.

💬 Comment 🔵 or 🟠 — and tell us WHY 👇""" + F),
# ---------------- DAY 6 ----------------
("review", ("Blade Runner 2049", 2017, 4.5, "WORTH IT",
  "A sequel nobody needed that turned out better than it had any right to be. Slow, gorgeous, and quietly heartbreaking.", "Sci-Fi"),
 """🎬 BLADE RUNNER 2049 (2017) — 4.5/5

A 35-years-later sequel to an untouchable classic. It should have been a disaster.

Instead Villeneuve made something patient and enormous — a film confident enough to sit in silence, and beautiful enough to earn it. Deakins finally got his Oscar for this, and it wasn't a consolation prize.

Gosling plays K as a man slowly discovering he might matter. The film's cruellest, best decision is what it does with that hope.

Fair warning: it's slow. Deliberately. If you want action, this isn't it. If you want to feel something enormous and sad — clear an evening.

That snow scene. That's all I'll say.

💬 Better or worse than the 1982 original? Dangerous question 👇""" + F),
("list", ("Best <em>One-Location</em><br>Movies Ever Made",
  ["12 Angry Men (1957)", "Rear Window (1954)", "The Guilty (2018)",
   "Buried (2010)", "Rope (1948)"], "THE WATCHLIST"),
 """🚪 No budget? No problem. These films trap you in one place and never let go.

1️⃣ 12 ANGRY MEN — one jury room, twelve men, zero weak scenes
2️⃣ REAR WINDOW — Hitchcock builds a thriller out of a man who can't move
3️⃣ THE GUILTY — a call centre. That's it. That's the movie.
4️⃣ BURIED — Ryan Reynolds in a coffin for 95 minutes. Genuinely.
5️⃣ ROPE — Hitchcock again, faking a single unbroken take in 1948

Constraint makes better films than money does.

💬 Which of these have you seen? And what did we miss? 👇""" + F),
("take", ("The scariest movies\ndon't show you\n*the monster.*\n\nThey show you\n*the door.*", "TAKE", "🚪"),
 """🚪 Horror learned the wrong lesson from jump scares.

Your imagination is a better special effects department than any studio. Jaws is terrifying because the shark barely works. Alien is terrifying because you barely see it. The Blair Witch Project has NO monster at all.

The moment you show the thing, it stops being fear and starts being design.

Suggestion > revelation. Every time.

💬 What's the scariest movie you've ever seen — and did it show you the monster? 👇""" + F),
# ---------------- DAY 7 ----------------
("review", ("Prisoners", 2013, 4.0, "WORTH IT",
  "A two-and-a-half hour moral trap. Villeneuve asks what you'd do, then makes sure you don't like the answer.", "Thriller"),
 """🎬 PRISONERS (2013) — 4/5

A child goes missing. The police have no evidence. The father takes matters into his own hands.

That's the setup, and the film spends 153 minutes refusing to let you feel good about any of it. Hugh Jackman is terrifying — not as a villain, as a father. Gyllenhaal's detective is the only one behaving reasonably, and he's losing.

Deakins shooting rain and grey Pennsylvania. Villeneuve's patience. A film that trusts you to sit with discomfort instead of resolving it.

Docked half a point for a final act that leans a bit convenient. The rest is close to perfect.

💬 Would you have done what Jackman's character did? Honest answer 👇""" + F),
("list", ("Films For People Who<br>\"Don't Do <em>Subtitles</em>\"",
  ["Parasite (2019, Korean)", "Oldboy (2003, Korean)",
   "City of God (2002, Portuguese)", "Pan's Labyrinth (2006, Spanish)",
   "Society of the Snow (2023, Spanish)"], "THE WATCHLIST"),
 """🌍 Start here. Ten minutes in, you'll forget you're reading.

1️⃣ PARASITE — the easiest entry point ever made. Funny, then not.
2️⃣ OLDBOY — one corridor. One hammer. You'll never forget it.
3️⃣ CITY OF GOD — kinetic, brutal, alive. Opens at a sprint.
4️⃣ PAN'S LABYRINTH — a fairy tale that isn't for children
5️⃣ SOCIETY OF THE SNOW — recent, devastating, unbelievably well made

Pick one. That's all it takes.

📌 Save this list.

💬 Which one are you watching first? 👇""" + F),
("take", ("What's your\n*comfort movie?*\n\nThe one you put on\nwhen nothing\nelse works.", "YOUR TURN", "🍿"),
 """🍿 Everyone has one. The film you've seen so many times you don't even watch it anymore — you just need it in the room.

It doesn't have to be good. That's not the job. The job is that it feels like a blanket.

Ours changes weekly. Some nights it's The Truman Show. Some nights it's a Studio Ghibli. Some nights it's a film we'd never publicly rate above 3/5 — and that's the point.

No judgement in this comment section. None.

💬 What's YOUR comfort movie? 👇""" + F),
]
