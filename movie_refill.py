# -*- coding: utf-8 -*-
"""Top Movie Reviews 7-day refill — 3/day = 21 (review / list / take rotation).
Original text only, no posters. English, geo US+EU.
Entry: (kind, payload, caption)
  review -> (title, year, rating, verdict, line, genre)
  list   -> (title_html, items, kicker)
  take   -> (text, kicker, emoji)
"""
F = "\n\n🎬 Follow Top Movie Reviews — an honest verdict every day."

POSTS = [
# D1
("review", ("Se7en", 1995, 4.5, "WORTH IT",
  "Fincher's rain-soaked nightmare builds to one of cinema's most quietly devastating endings. 'What's in the box' still hurts.", "Thriller"),
 """🎬 SE7EN (1995) — 4.5/5

Two detectives. Seven murders. One of the darkest films a major studio ever released — and it never flinches.

Fincher shoots the whole thing in perpetual rain and shadow, so by the time the sun finally appears in the last scene, you know something terrible is coming.

Pitt and Freeman are perfectly matched — young rage against tired wisdom. But it's Kevin Spacey's calm that turns your stomach.

That ending was nearly changed by the studio. They were wrong. It's the reason people still talk about it 30 years later.

💬 Where does it rank in your all-time thrillers? 👇""" + F),
("list", ("Movies That *Ruined* You<br>(In the Best Way)",
  ["Requiem for a Dream (2000)", "Grave of the Fireflies (1988)",
   "Manchester by the Sea (2016)", "Hereditary (2018)", "Come and See (1985)"], "THE WATCHLIST"),
 """💔 Some films you love. Some films you survive. These five leave a mark.

1️⃣ REQUIEM FOR A DREAM — you'll never be the same after that final montage
2️⃣ GRAVE OF THE FIREFLIES — animated, and the saddest film ever made
3️⃣ MANCHESTER BY THE SEA — grief, played with unbearable honesty
4️⃣ HEREDITARY — horror that's really about family trauma
5️⃣ COME AND SEE — the greatest, most harrowing war film ever

Watch responsibly. Maybe not all in one week.

💬 Which film wrecked you the most? 👇""" + F),
("take", ("A great villain\nbelieves he's\nthe *hero.*", "HOT TAKE", "🎭"),
 """🎭 The lazy villain wants to 'watch the world burn.' The great one thinks he's saving it.

Thanos. The Joker in some tellings. Amon Goeth. Anton Chigurh with his coin. The best antagonists have a logic you can almost follow — and that's what makes them terrifying.

If you understand exactly why they're doing it, and part of you can't fully argue back, the writers did their job.

💬 Best-written movie villain of all time? One name 👇""" + F),
# D2
("review", ("Inside Out", 2015, 4.5, "WORTH IT",
  "Pixar turns a child's brain into an adventure and quietly explains grief better than most adult dramas.", "Animation"),
 """🎬 INSIDE OUT (2015) — 4.5/5

A kids' movie that made every adult in the theatre cry.

The premise sounds gimmicky — emotions as characters running a control room in a child's head. In lesser hands it's a cartoon. In Pixar's, it becomes the clearest explanation of sadness anyone has put on screen.

The lesson lands without a single lecture: you can't be happy all the time, and trying to erase sadness only makes things worse. Joy needs Sadness.

That's a heavy idea for a family film. It earns it completely.

💬 Which Pixar film hit you hardest as an adult? 👇""" + F),
("list", ("Directorial *Debuts*<br>That Announced a Genius",
  ["Reservoir Dogs — Tarantino (1992)", "Whiplash — Chazelle (2014)",
   "Get Out — Peele (2017)", "Pi — Aronofsky (1998)",
   "Following — Nolan (1998)"], "THE WATCHLIST"),
 """🎬 Some directors arrive fully formed. These debuts made the industry sit up.

1️⃣ RESERVOIR DOGS — Tarantino's voice, complete on day one
2️⃣ WHIPLASH — technically Chazelle's second, but the one that announced him
3️⃣ GET OUT — Peele turned horror into social commentary overnight
4️⃣ PI — Aronofsky, shot for $60k, already obsessive and brilliant
5️⃣ FOLLOWING — Nolan's £3,000 debut, already playing with time

Everyone starts somewhere. These started at the top.

💬 Best directorial debut ever? 👇""" + F),
("take", ("The *rewatch* is where\na film becomes\nyour friend.", "TAKE", "🔁"),
 """🔁 The first watch is a stranger telling you a story. The tenth is an old friend you visit.

You stop watching for what happens and start noticing how it's made — the glance you missed, the line that means something new now, the shot that was foreshadowing all along.

Some films you don't finish understanding until the third viewing. That's not a flaw. That's depth.

💬 What film have you rewatched the most? Honest number 👇""" + F),
# D3
("review", ("Oldboy", 2003, 4.5, "WORTH IT",
  "Park Chan-wook's revenge masterpiece with a corridor fight and a twist that still leaves people speechless. Not for the faint-hearted.", "Thriller"),
 """🎬 OLDBOY (2003) — 4.5/5

A man is imprisoned in a room for 15 years. No explanation. Then, just as suddenly, he's released — and given five days to find out why.

Park Chan-wook made one of the most influential thrillers of the century. The single-take hallway fight, shot side-on like a video game, has been copied endlessly and bettered never.

But it's the ending that makes it legendary — a gut-punch so bleak it recontextualises the entire film. You won't 'enjoy' it. You won't forget it.

⚠️ Heavy content. Go in prepared.

💬 Have you seen it? React 😶 if that ending got you 👇""" + F),
("list", ("Films Under *90 Minutes*<br>That Punch Above Their Weight",
  ["Before Sunrise (1995) — 101", "Run Lola Run (1998) — 81",
   "The Iron Giant (1999) — 86", "Rope (1948) — 80",
   "Primer (2004) — 77"], "THE WATCHLIST"),
 """⏱️ Great cinema doesn't need three hours. These end before your popcorn does:

1️⃣ RUN LOLA RUN — 81 minutes at a dead sprint
2️⃣ THE IRON GIANT — 86 minutes, and it'll make you cry
3️⃣ ROPE — Hitchcock faking one unbroken take, 80 tense minutes
4️⃣ PRIMER — 77 minutes, and you'll need a diagram
5️⃣ BEFORE SUNRISE — two people, one night, quietly perfect

Tight, sharp, unforgettable.

💬 Best short film (under 90 min) you've seen? 👇""" + F),
("take", ("The best *soundtrack*\ndisappears —\nyou feel it before\nyou hear it.", "TAKE", "🎵"),
 """🎵 You remember the themes from Star Wars or Interstellar. But the greatest scores are often the ones you never consciously notice.

They tell you how to feel a half-second before the scene does. Dread creeping in. Hope rising. Your pulse following music you're not even aware of.

A great score doesn't sit on top of a film. It becomes its nervous system.

💬 Best film score of all time? One answer 👇""" + F),
# D4
("review", ("La La Land", 2016, 4.0, "WORTH IT",
  "A gorgeous modern musical with a bittersweet ending that divides everyone — and that's exactly why it works.", "Musical"),
 """🎬 LA LA LAND (2016) — 4/5

A love letter to dreamers, jazz, and the city where ambitions go to be tested.

Chazelle shoots it like a classic Hollywood musical but writes it like a modern heartbreak. Gosling and Stone have real chemistry, and the opening highway number sets a bar the film mostly clears.

The ending is the whole conversation. That final 'what if' montage — of the life they didn't have — is one of the boldest closes a crowd-pleaser has attempted.

Docked a point for a saggy middle. But that ending earns its place.

💬 The ending: perfect or frustrating? Genuinely split the comments 👇""" + F),
("list", ("Movies Everyone *Pretends*<br>to Understand",
  ["2001: A Space Odyssey (1968)", "Mulholland Drive (2001)",
   "Enemy (2013)", "The Tree of Life (2011)", "Tenet (2020)"], "THE WATCHLIST"),
 """🌀 It's okay to admit you Googled the ending. Everyone did.

1️⃣ 2001 — the greatest film nobody fully explains
2️⃣ MULHOLLAND DRIVE — Lynch isn't going to help you
3️⃣ ENEMY — that final shot. Yes, THAT one.
4️⃣ THE TREE OF LIFE — is it a film or a prayer?
5️⃣ TENET — even the cast admitted they weren't sure

Confusion can be a feature, not a bug.

💬 Which one still confuses you? No shame here 👇""" + F),
("take", ("A slow film isn't\na *boring* film.\n\nPatience is a\nstyle, not a flaw.", "TAKE", "🐢"),
 """🐢 'Nothing happened.' Something happened — you just wanted it faster.

Some of the greatest films breathe. They let a moment sit. They trust you to lean in instead of grabbing your collar every ten seconds.

Blade Runner 2049. There Will Be Blood. Drive. Their power comes from restraint — the quiet that makes the loud moments land like a hammer.

Not every film should be slow. But 'slow' isn't an insult.

💬 A 'slow' film you secretly love? 👇""" + F),
# D5
("review", ("The Social Network", 2010, 4.5, "WORTH IT",
  "Fincher and Sorkin turn a website's origin into a Shakespearean tragedy about ambition and loneliness. Endlessly quotable.", "Drama"),
 """🎬 THE SOCIAL NETWORK (2010) — 4.5/5

'A film about Facebook' sounds like the most boring pitch imaginable. It's one of the sharpest dramas of its decade.

Sorkin's dialogue moves so fast you'll want subtitles, and Fincher directs it like a thriller. Together they build a tragedy: a man who connected the world and ended it alone at a laptop, refreshing a friend request.

That final shot says everything the two hours built to. Quiet, and devastating.

Fifteen years on, it plays less like history and more like prophecy.

💬 Best 'based on a true story' film? 👇""" + F),
("list", ("Perfect *Opening Scenes*<br>in Movie History",
  ["Saving Private Ryan (1998)", "Up (2009)",
   "The Dark Knight (2008)", "Inglourious Basterds (2009)",
   "Touch of Evil (1958)"], "THE WATCHLIST"),
 """🎬 You have five minutes to hook an audience. These nailed it.

1️⃣ UP — the wordless marriage montage. Four minutes. Everyone cries.
2️⃣ SAVING PRIVATE RYAN — the beach. Cinema has never been more brutal.
3️⃣ THE DARK KNIGHT — the bank heist that introduces the Joker perfectly
4️⃣ INGLOURIOUS BASTERDS — a farmhouse, and unbearable tension
5️⃣ TOUCH OF EVIL — one unbroken take, 1958, still stunning

A great opening is a promise. These kept it.

💬 Best opening scene ever? 👇""" + F),
("take", ("You don't *outgrow*\na great film.\n\nIt grows *with* you.", "TAKE", "🎬"),
 """🎬 The film you loved at 15 hits differently at 30 — and again at 50.

You notice the parent's exhaustion you missed as a kid. The line that was a joke becomes a truth. The character you rooted for becomes the one you understand.

A great film doesn't stay the same. You change, and it reveals a part it was hiding until you were ready.

💬 A film that means something completely different to you now? 👇""" + F),
# D6
("review", ("Spirited Away", 2001, 5.0, "MASTERPIECE",
  "Miyazaki's dazzling, strange masterpiece — a girl lost in a spirit world, and the most imaginative film ever animated.", "Animation"),
 """🎬 SPIRITED AWAY (2001) — 5/5

A ten-year-old wanders into a bathhouse for spirits and has to work to save her parents. That's the plot. It doesn't begin to describe the experience.

Miyazaki fills every frame with detail no one asked for and everyone remembers — the soot sprites, the train across the water, No-Face. It follows dream logic, not story logic, and it's better for it.

It won the Oscar. It outgrossed Titanic in Japan. But numbers miss the point: it feels like remembering a dream you never actually had.

The greatest animated film ever made. It's not close.

💬 Favourite Studio Ghibli film? 👇""" + F),
("list", ("Foreign Films to *Start*<br>Your Subtitle Journey",
  ["Parasite (2019, Korea)", "Amélie (2001, France)",
   "Life Is Beautiful (1997, Italy)", "Your Name (2016, Japan)",
   "The Lives of Others (2006, Germany)"], "THE WATCHLIST"),
 """🌍 'I don't do subtitles' costs you the best films ever made. Start here — you'll forget you're reading in ten minutes.

1️⃣ PARASITE — the perfect gateway. Funny, then not.
2️⃣ AMÉLIE — pure joy, painted in gold and green
3️⃣ LIFE IS BEAUTIFUL — will break your heart and mend it
4️⃣ YOUR NAME — gorgeous, and a global phenomenon
5️⃣ THE LIVES OF OTHERS — quiet, tense, unforgettable

One inch of subtitles. A whole world behind it.

💬 Which are you watching first? 👇""" + F),
("take", ("Practical effects age\nlike wine.\n\nBad CGI ages\nlike milk. 🥛", "HOT TAKE", "🎥"),
 """🎥 Watch a 1993 dinosaur next to a 2015 one. The older one often looks better. Why?

Practical effects are really there — light hits them correctly, actors react to something real. Great CGI is invisible; bad CGI is a countdown to looking dated.

Jaws, The Thing, Jurassic Park's best shots — decades old and still convincing. Some films from last year already look plastic.

Real beats fake, when the budget lets it.

💬 Best practical effect that still holds up? 👇""" + F),
# D7
("review", ("Casino Royale", 2006, 4.5, "WORTH IT",
  "The reboot that saved Bond — brutal, emotional, and the best the franchise has ever been. Craig arrives fully formed.", "Action"),
 """🎬 CASINO ROYALE (2006) — 4.5/5

Bond was a cartoon by 2005 — invisible cars, gadgets, self-parody. This tore it all down and started over.

Craig's 007 bleeds, makes mistakes, and — remarkably — falls in love for real. The famous poker game is more tense than most action climaxes, and the stairwell fight is bruising in a way Bond had never been.

Then it does the unthinkable: it gives him a heart, and breaks it. 'The name's Bond' has never been more earned than in that final line.

The best film in a 60-year franchise. Fight me.

💬 Best Bond, no wrong answers (there are wrong answers) 👇""" + F),
("list", ("Comfort Movies for a *Bad Day*",
  ["The Truman Show (1998)", "Chef (2014)",
   "Paddington 2 (2017)", "About Time (2013)",
   "Kung Fu Panda (2008)"], "THE WATCHLIST"),
 """🍿 Not every film needs to challenge you. Some just need to hug you.

1️⃣ THE TRUMAN SHOW — hopeful in a way that sneaks up on you
2️⃣ CHEF — the most feel-good film about food ever
3️⃣ PADDINGTON 2 — genuinely one of the kindest films made
4️⃣ ABOUT TIME — really about appreciating ordinary days
5️⃣ KUNG FU PANDA — funnier and wiser than it has any right to be

Save this list for a rough evening.

💬 What's YOUR comfort movie? No judgement 👇""" + F),
("take", ("What film do you\n*quote* the most\nwithout even\nrealising it?", "YOUR TURN", "💬"),
 """💬 Some lines escape the movie and just become... how you talk.

'I'll be back.' 'You can't handle the truth.' 'Why so serious?' 'I'm walking here!' 'Say hello to my little friend.'

You've quoted a film this week without thinking about it. Everyone has one that's burrowed into daily life.

💬 The movie line you quote most often — go 👇""" + F),
]
assert len(POSTS) == 21
