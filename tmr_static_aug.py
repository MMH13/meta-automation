# -*- coding: utf-8 -*-
"""Top Movie Reviews — the 43 static posts that fill Jul 31 → Aug 15 to 6/day.

Slot map per day: 11:00 reel · 13:00 static · 15:00 static · 19:00 static
                  21:00 reel · 23:00 static
Aug 1-7 already hold 15:00/19:00/23:00 from OS Week 1, so those days need
only the 13:00 slot. Jul 31 and Aug 8-15 need all four.

Reviews pull the official poster from TMDB (editorial use, credit line on card).
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from datetime import date, timedelta

from aug_common import load, save, mkdir, render
from image_movie import movie_take, movie_list, movie_review_poster

IMG = mkdir("images/tmr_aug")
F = "\n\n🎬 Top Movie Reviews — one honest verdict a day."
T_R = "\n\n#MovieReview #FilmTwitter #Cinephile #MustWatch #MovieNight #FilmLovers #WhatToWatch #Cinema"
T_G = "\n\n#GuessTheMovie #MovieQuiz #FilmBuff #MovieTrivia #Cinephile #MovieGame #NameThatMovie"
T_D = "\n\n#MovieDebate #FilmTwitter #Cinephile #HotTake #MovieTalk #FilmDiscussion #Cinema"

# kinds: take(text,kicker,emoji,caption) | list(title,items,kicker,caption)
#        review(title,year,rating,verdict,line,genre,caption)
POSTS = [
# ═══════════ JUL 31 — 4 posts ═══════════
("take", "🎬 🌊 🚢 🧊 💔\n\n*Guess the movie.*", "EMOJI PUZZLE", "🧩",
 "🧩 Five emojis, one film almost everyone has seen.\n\nIf you get it in under two seconds, you're not alone — but say it anyway.\n\n👇 Comment your answer.\n\n🔁 Share this with someone who cries at it." + T_G + F),
("review", "The Prestige", 2006, 4.5, "OBSESSIVE",
 "Two magicians destroy each other over a trick the film shows you in the opening minute.",
 "MYSTERY · DRAMA",
 "🎬 THE PRESTIGE (2006) — 4.5/5\n\n\"Are you watching closely?\" It asks in the first line, and it means it.\n\nNolan's most underrated film is about obsession disguised as a magic-trick mystery. Two rivals ruin themselves trying to out-perform each other, and the film is structured exactly like the trick it describes — pledge, turn, prestige.\n\nBale and Jackman are both excellent, but the real achievement is the construction. The answer is on screen in the first sixty seconds. You just won't see it.\n\nWeakness: it's cold. You admire it more than you love it, and some viewers never warm to anyone in it.\n\nVerdict: the best film about the cost of being the best.\n\n👇 Did you spot it on first watch? Honestly?\n\n🔁 Share this with someone who needs a rewatch." + T_R + F),
("take", "The *Wilhelm scream* has been\nhidden in hundreds of films\nsince 1951.\n\nOnce you hear it,\nyou can't unhear it. 🔊", "MOVIE FACT", "🎥",
 "🔊 It's a stock sound effect recorded in 1951, and sound designers have been sneaking it into films as an in-joke for decades.\n\nStar Wars. Indiana Jones. Lord of the Rings. Once someone points it out, you start catching it everywhere — and it slightly ruins dramatic death scenes forever.\n\nSorry in advance.\n\n👇 Have you ever noticed it?\n\n🔁 Share this and ruin it for a friend." + T_R + F),
("take", "The *best* film of the last\ndecade probably wasn't\nnominated for anything. 🏆", "HOT TAKE", "🎯",
 "🔥 Awards reward a certain kind of film: released late in the year, serious in tone, with a campaign budget behind it.\n\nPlenty of genuinely great films don't fit that shape — genre films, comedies, animation, anything released in February.\n\nThe trophy measures a season. It doesn't measure a film.\n\n👇 Name a film you love that got zero recognition.\n\n🔁 Share this if you've got one." + T_D + F),
# ═══════════ AUG 1-7 — 13:00 slot only, 1/day ═══════════
("take", "Yesterday: *TITANIC* 🚢\n\nToday — name the film:\n\n\"Say hello to my\nlittle friend.\"", "GUESS THE LINE", "🎯",
 "🎯 Yesterday's emoji puzzle was TITANIC.\n\nToday's is a line rather than a picture — and it's one of the most quoted in film history.\n\n👇 Comment the film (and the character if you know it).\n\n🔁 Share this with someone who quotes movies constantly." + T_G + F),
("take", "A film can be *technically perfect*\nand still leave you\nfeeling nothing. 🎞️", "HOT TAKE", "🤔",
 "🔥 Flawless cinematography, immaculate sound design, precise editing — and somehow you don't care about anyone in it.\n\nCraft is necessary. It just isn't sufficient. A messy film that makes you feel something beats a perfect one that doesn't, every time.\n\n👇 Name a beautiful film that left you cold.\n\n🔁 Share this and see who agrees." + T_D + F),
("take", "Films are getting *longer*.\n\nThe average blockbuster\nnow runs well past\ntwo hours. ⏱️", "THE DEBATE", "⏳",
 "⏳ Three-hour runtimes used to be reserved for epics. Now they're routine.\n\nThe argument for: streaming trained us to binge, and directors have more freedom than ever.\n\nThe argument against: length is often a substitute for editing. Plenty of long films are 100-minute stories wearing a bigger coat.\n\n👇 Would you rather a tight 95 minutes or a sprawling 3 hours?\n\n🔁 Share this with someone who always falls asleep." + T_D + F),
("take", "🎬 🤖 🌧️ 🏙️ 🕵️\n\n*Guess the movie.*\n\n(Two answers are valid.)", "EMOJI PUZZLE", "🧩",
 "🧩 Five emojis — and unusually, two different films fit this one perfectly.\n\nName either. Name both if you spot it.\n\n👇 Comment your answer.\n\n🔁 Share this with a sci-fi fan." + T_G + F),
("list", "5 Films Where the Villain Has a Point",
 ["Se7en", "No Country for Old Men", "Nightcrawler", "There Will Be Blood", "Whiplash"],
 "UNCOMFORTABLE VIEWING",
 "😈 The best antagonists aren't evil for fun. They have an argument — and the film makes you sit with it.\n\nThat discomfort is the whole point. If you never waver, the film isn't doing its job.\n\n👇 Which movie villain were you uncomfortably close to agreeing with?\n\n🔁 Save this list." + T_D + F),
("take", "Watching a film on your *phone*\nisn't watching the film.\n\nToo far? 📱", "HOT TAKE", "🍿",
 "🔥 Directors spend months on framing, sound design and colour — and then it gets watched on a 6-inch screen with one earbud in, at 1.5x speed, while someone scrolls.\n\nThe counter-argument is fair: a film watched badly still beats a film not watched at all.\n\nBut something is genuinely lost.\n\n👇 Phone, laptop, TV or cinema — where do you actually watch?\n\n🔁 Share this with a serial phone-watcher." + T_D + F),
("take", "The scariest horror films\nshow you *almost nothing*. 🚪", "MOVIE FACT", "😱",
 "🚪 Jump scares are cheap and they work for about a second. Dread lasts for days.\n\nThe films people still can't shake — Alien, The Blair Witch Project, Hereditary — mostly withhold. Your imagination builds something far worse than any effects budget could.\n\nHorror learned the wrong lesson from jump scares.\n\n👇 What's the scariest film you've genuinely never recovered from?\n\n🔁 Share this with someone brave." + T_R + F),
# ═══════════ AUG 8 — 4 posts ═══════════
("take", "Yesterday: *BLADE RUNNER*\n(or Minority Report) 🤖\n\nToday: finish the line —\n\n\"I'm going to make him\nan offer ______\"", "FINISH IT", "🎬",
 "🎬 Both answers counted yesterday — that's why it was a good puzzle.\n\nToday, finish three:\n\n1. \"I'm going to make him an offer ______\"\n2. \"Here's looking at ______\"\n3. \"You can't handle ______\"\n\n👇 Comment all three. No Googling.\n\n🔁 Share this with someone who'll get two out of three." + T_G + F),
("review", "Arrival", 2016, 4.5, "PROFOUND",
 "The rare sci-fi film where nobody fires a weapon and the tension never drops for a second.",
 "SCI-FI · DRAMA",
 "🎬 ARRIVAL (2016) — 4.5/5\n\nTwelve objects appear around the world. A linguist is asked to talk to what's inside.\n\nWhat lands: it's a first-contact film where the weapon is grammar. Villeneuve builds enormous tension out of people slowly understanding each other, which should be impossible and isn't.\n\nAmy Adams carries the entire film on restraint. The score does half the emotional work. And the structure — which I won't spoil — reframes everything the second time you watch it.\n\nWeakness: the middle sags slightly under the military subplot, which is the least interesting thread.\n\nVerdict: science fiction that's actually about being a person.\n\n👇 Did you see the ending coming?\n\n🔁 Share this with someone who thinks sci-fi is all spaceships." + T_R + F),
("take", "*Every* Pixar film follows\nthe same emotional structure —\n\nand it works *every time*. 🎈", "MOVIE FACT", "🎥",
 "🎈 A character who is certain about their place → something breaks the certainty → they resist → they let go → the ending reframes the beginning.\n\nToy Story. Up. Inside Out. Ratatouille. Coco.\n\nKnowing the formula doesn't stop it working. That's the interesting part — structure isn't a trick, it's a delivery system.\n\n👇 Which Pixar film hit you hardest?\n\n🔁 Share this with someone who cried at Up." + T_R + F),
("take", "You don't have a\n*favourite film*.\n\nYou have a favourite film\n*for a mood*. 🎭", "HOT TAKE", "🎬",
 "🔥 Nobody actually has one favourite. You have a sad-night film, a background film, a show-off film, and a film you'd defend in an argument but rarely rewatch.\n\nThe \"what's your favourite film\" question is unanswerable because it's the wrong question.\n\n👇 Give us all four of yours instead.\n\n🔁 Share this and compare lists." + T_D + F),
# ═══════════ AUG 9 ═══════════
("take", "Answers:\n1. \"...he can't refuse\"\n2. \"...you, kid\"\n3. \"...the truth!\"\n\nToday — *odd one out* 👇", "ANSWER + PUZZLE", "✅",
 "✅ The Godfather, Casablanca, A Few Good Men.\n\nToday's puzzle — which is the odd one out, and why?\n\n🎬 Whiplash\n🎬 Black Swan\n🎬 The Wrestler\n🎬 Inception\n\n(There's a real answer. Several defensible ones too.)\n\n👇 Comment your pick and your reasoning.\n\n🔁 Share this with someone who overthinks." + T_G + F),
("list", "5 Directors Who Never Won Best Director",
 ["Alfred Hitchcock", "Stanley Kubrick", "Ridley Scott", "David Fincher", "Denis Villeneuve"],
 "THE ACADEMY'S BLIND SPOT",
 "🏆 Between them: Psycho, 2001, Alien, Se7en, Blade Runner 2049.\n\nNot one Best Director win. Hitchcock was nominated five times and never won.\n\nIt's the clearest evidence that awards track a moment, not a career.\n\n👇 Whose loss is the most indefensible?\n\n🔁 Share this with a film-history nerd." + T_R + F),
("take", "A *bad* first act can be saved.\n\nA bad *third* act\nkills the whole film. 🎯", "THE DEBATE", "⚔️",
 "⚔️ You'll forgive a slow start. You'll never forgive a bad ending.\n\nThe ending is what you leave with — it rewrites your memory of everything before it, and it decides whether you ever rewatch.\n\nCounter-argument: if the first act loses you, there is no third act, because you've stopped watching.\n\n👇 Which matters more — the setup or the landing?\n\n🔁 Share this and let them fight." + T_D + F),
("take", "Some films are *better*\nwhen you know\nnothing about them. 🤫", "HOT TAKE", "🎬",
 "🤫 Trailers now show the best three moments, the twist, and often the ending. Marketing has become the enemy of the experience.\n\nThe best modern viewing habit is genuinely just: hear it's good, watch it, ask questions after.\n\n👇 What's a film you're glad you went into blind?\n\n🔁 Share this with someone who watches every trailer twice." + T_D + F),
# ═══════════ AUG 10 ═══════════
("take", "Odd one out: *INCEPTION* 🎬\n\nThe others are all about\nself-destruction through\nobsession with craft.\n\nNew puzzle 👇", "ANSWER + PUZZLE", "🎯",
 "🎯 Whiplash, Black Swan and The Wrestler are all about destroying your body for your art. Inception is the outlier — though plenty of you argued Cobb qualifies, and that's fair.\n\nNew one: 🎬 🕰️ 🚂 ❄️ 🔪 — guess the film.\n\n👇 Comment your answer.\n\n🔁 Share this with a mystery fan." + T_G + F),
("review", "Whiplash", 2014, 5.0, "RELENTLESS",
 "A two-hour panic attack about the cost of greatness, with one of the best endings ever filmed.",
 "DRAMA · MUSIC",
 "🎬 WHIPLASH (2014) — 5/5\n\nA drummer at an elite conservatory meets a teacher who believes cruelty produces genius.\n\nWhat lands: it's shot and cut like a thriller. Blood on the drums, a metronome as a weapon, and a rhythm that never lets you settle. It runs under two hours and feels like a sprint.\n\nJ.K. Simmons is terrifying precisely because he's sometimes right — and the film refuses to tell you how much. That ambiguity is the whole argument.\n\nWeakness: it isn't interested in a balanced view of teaching. It's a portrait of obsession, not a thesis.\n\nVerdict: that final ten minutes is one of the great endings in modern film.\n\n👇 Was Fletcher a monster, or a maker of greatness?\n\n🔁 Share this with someone who needs to see it." + T_R + F),
("take", "The average shot length\nin action films has\n*collapsed*.\n\nThat's why modern\naction feels *worse*. 🎥", "MOVIE FACT", "⚡",
 "⚡ Older action held a shot long enough for you to read the geography — who's where, moving which way.\n\nModern action often cuts so fast that your brain never builds the map, so the sequence registers as noise rather than tension.\n\nIt's why Fury Road and John Wick feel so different: they let you see.\n\n👇 Which modern action film actually lets you follow it?\n\n🔁 Share this with someone who says action films 'all look the same now'." + T_R + F),
("take", "You're allowed to *dislike*\na film everyone loves.\n\nYou're not obliged\nto \"get\" it. 🎬", "HOT TAKE", "🤷",
 "🤷 Film taste has become weirdly moralised. Not liking an acclaimed film gets treated as a failure of comprehension rather than a difference of taste.\n\nYou can understand exactly what a film is doing and still find it cold, slow or dull. That's a legitimate response.\n\n👇 What's a beloved classic you just don't rate? Be brave.\n\n🔁 Share this and see who's honest." + T_D + F),
# ═══════════ AUG 11 ═══════════
("take", "Yesterday: *MURDER ON THE\nORIENT EXPRESS* 🚂\n\nToday: which decade? 👇", "ANSWER + QUIZ", "🕰️",
 "🕰️ Yesterday was Murder on the Orient Express.\n\nToday — name the decade each of these came out. No Googling:\n\n1. The Godfather\n2. Pulp Fiction\n3. Blade Runner\n4. Jaws\n5. The Matrix\n\n👇 Comment your five decades.\n\n🔁 Share this with someone who'll get all five." + T_G + F),
("list", "5 Films That Are Basically Perfect at Their Job",
 ["Die Hard — the action film", "Alien — the horror film", "Groundhog Day — the comedy",
  "Toy Story — the animation", "Heat — the crime film"],
 "GENRE BENCHMARKS",
 "🎯 Not necessarily the 'greatest films ever' — but the ones that do their specific job so well that everything after is measured against them.\n\nDie Hard invented a whole template. Alien is still the benchmark for dread. Groundhog Day is structurally flawless.\n\n👇 Which genre benchmark did we miss?\n\n🔁 Save this list." + T_R + F),
("take", "Nobody says\n\"why would you read\nthat book *again*?\" 📚\n\nSo why is rewatching\ntreated as a waste? 🔁", "THE DEBATE", "🎞️",
 "🔁 Re-reading a novel is considered thoughtful. Re-listening to an album is normal. Rewatching a film somehow gets treated as failure of imagination.\n\nBut films are dense — you physically cannot catch everything in one pass. The second viewing is where you see the construction.\n\n👇 How many times have you seen your most-rewatched film?\n\n🔁 Share this with a serial rewatcher." + T_D + F),
("take", "The best *comedies* are\nalmost never nominated\nfor anything. 🎭", "HOT TAKE", "😂",
 "😂 Making people laugh is measurably harder than making them sad — sadness has a reliable formula, comedy has timing that either works or doesn't.\n\nYet drama gets the trophies and comedy gets treated as light entertainment.\n\n👇 Name a comedy that deserved serious awards attention.\n\n🔁 Share this with someone who quotes comedies constantly." + T_D + F),
# ═══════════ AUG 12 ═══════════
("take", "Answers: 70s, 90s, 80s,\n70s, 90s 🕰️\n\nToday — *one word* 👇", "ANSWER + PROMPT", "✅",
 "✅ The Godfather (1972), Pulp Fiction (1994), Blade Runner (1982), Jaws (1975), The Matrix (1999).\n\nToday's is simple but harder than it sounds:\n\nDescribe your favourite film in exactly ONE word. No title. Let people guess it.\n\n👇 Go.\n\n🔁 Share this and guess someone else's." + T_G + F),
("review", "No Country for Old Men", 2007, 5.0, "MERCILESS",
 "A chase film with no music, no comfort, and one of the most frightening screen villains ever put on film.",
 "THRILLER · CRIME",
 "🎬 NO COUNTRY FOR OLD MEN (2007) — 5/5\n\nA man finds money in the desert. Someone comes to get it back.\n\nWhat lands: the Coens strip out almost all the score. Long stretches play in near silence, and the absence of music makes every room feel dangerous. It's one of the boldest sound decisions in modern American film.\n\nJavier Bardem's Anton Chigurh is genuinely frightening because he's consistent — he has rules, and he follows them regardless of what you deserve.\n\nWeakness: the ending refuses you catharsis, deliberately. Many viewers hate it. It's also the entire point of the film.\n\nVerdict: a masterpiece that doesn't care whether you're satisfied.\n\n👇 That final scene — brilliant, or a cheat?\n\n🔁 Share this and start the argument." + T_R + F),
("take", "*Silence* is the most\nunderused tool in\nmodern filmmaking. 🔇", "MOVIE FACT", "🎧",
 "🔇 Most films score almost every scene, which tells you constantly how to feel. Remove the music and the audience has to decide for themselves — and that's uncomfortable in exactly the right way.\n\nNo Country for Old Men. There Will Be Blood's opening twenty minutes. A Quiet Place's entire premise.\n\nSilence makes you lean in.\n\n👇 Which scene is scarier because there's no music?\n\n🔁 Share this with someone who notices sound design." + T_R + F),
("take", "A film that *divides* people\nis usually more interesting\nthan one everyone\nmildly likes. ⚔️", "HOT TAKE", "🎯",
 "⚔️ Universal approval usually means a film played it safe. The films that split rooms took a swing.\n\nA 6/10 everyone agrees on is far less interesting than a film half the audience calls a masterpiece and half calls a mess.\n\n👇 Name the most divisive film you actually love.\n\n🔁 Share this with someone who disagreed with you about it." + T_D + F),
# ═══════════ AUG 13 ═══════════
("take", "Some of your one-word answers\nwere *incredible* 👏\n\nToday — hardest question\non this page 👇", "COMMUNITY", "💬",
 "💬 Yesterday's one-word game produced some genuinely brilliant answers. \"Grief.\" \"Rain.\" \"Loud.\" All immediately guessable once you knew.\n\nToday, the hardest question we've asked:\n\nWhat's the film that changed how you see something in real life?\n\nNot your favourite. The one that actually changed something.\n\n👇 Take your time with this one.\n\n🔁 Share it with someone who'll have a real answer." + T_R + F),
("list", "5 Films to Watch When You Can't Decide",
 ["Spirited Away", "The Grand Budapest Hotel", "Back to the Future", "Paddington 2", "Ratatouille"],
 "GUARANTEED GOOD NIGHT",
 "🍿 Forty minutes of scrolling and you've picked nothing. It happens to everyone.\n\nScreenshot this. Every one of these is a guaranteed good evening, works for almost any audience, and doesn't demand anything of you.\n\n👇 What's your go-to when you can't decide?\n\n🔁 Save this for next Friday." + T_R + F),
("take", "Sequels aren't the problem.\n\n*Unnecessary* sequels are. 🎬", "THE DEBATE", "🔁",
 "🔁 The Godfather Part II. Aliens. The Dark Knight. Toy Story 2. All sequels, all arguably better than the original.\n\nThe problem isn't continuation — it's continuation without a story. A sequel made because a film earned money isn't a sequel, it's a product.\n\n👇 Best sequel ever made? And the worst?\n\n🔁 Share this and compare." + T_D + F),
("take", "Watching a film in a *cinema*\nwith strangers is a\ncompletely different\nexperience. 🎟️", "HOT TAKE", "🍿",
 "🎟️ A room full of people gasping at once, or laughing together, changes what the film is. Comedy is measurably funnier in a full room. Horror is worse — in the best way.\n\nYou can't replicate that on a sofa, however good your TV is.\n\n👇 What's the best cinema experience you've ever had?\n\n🔁 Share this with someone you'd go with." + T_D + F),
# ═══════════ AUG 14 ═══════════
("take", "Your answers yesterday were\ngenuinely *moving* 💙\n\nToday — lighter 👇", "COMMUNITY", "💬",
 "💙 Some of yesterday's answers about films that changed how you see something were genuinely moving. Thank you for those.\n\nToday's is deliberately lighter:\n\nWhat's the film you've quoted most in real life — and what's the line?\n\n👇 Go on.\n\n🔁 Share this with the person you quote it at." + T_G + F),
("review", "Heat", 1995, 4.5, "MONUMENTAL",
 "A crime epic where the cops and the thieves are the same kind of person, and both know it.",
 "CRIME · DRAMA",
 "🎬 HEAT (1995) — 4.5/5\n\nA detective and a career criminal circle each other across Los Angeles.\n\nWhat lands: Michael Mann treats both men with total seriousness. Neither is the villain. They're professionals who happen to be on opposite sides, and the film's famous coffee-shop scene is just two men admitting they understand each other completely.\n\nThe downtown shootout is still the benchmark — real gunfire recordings, real spatial geography, no shaky-cam confusion. You always know where everyone is.\n\nWeakness: it's nearly three hours and some of the domestic subplots sag.\n\nVerdict: the best American crime film since the Godfathers.\n\n👇 Best crime film ever made — this, or something else?\n\n🔁 Share this with someone who's never seen it." + T_R + F),
("take", "The most rewatched scenes\non earth are usually\n*two people talking*. 💬", "MOVIE FACT", "🎥",
 "💬 Not explosions. Not chases. Conversations.\n\nThe Heat diner scene. The Pulp Fiction breakfast. The Good Will Hunting bench. Before Sunrise, which is nothing but talking.\n\nSpectacle gets you into the cinema. Dialogue is what people replay for twenty years.\n\n👇 What's the best two-hander conversation scene in film?\n\n🔁 Share this with someone who values a good script." + T_R + F),
("take", "You will never watch\nmost of the great films\never made.\n\nAnd that's *fine*. 🎞️", "HOT TAKE", "🌍",
 "🌍 Roughly 50,000 films get made every year. You might watch 100. Even a devoted cinephile will miss almost everything.\n\nThe watchlist guilt is pointless. You're not falling behind — there is no behind. Watch what you're drawn to, and let the rest go.\n\n👇 How many films are on your watchlist right now? Honestly.\n\n🔁 Share this with someone whose list is out of control." + T_D + F),
# ═══════════ AUG 15 ═══════════
("take", "Two weeks. Hundreds of\ncomments. *Zero* agreement. 🎬\n\nExactly right 👇", "COMMUNITY", "🏁",
 "🏁 Two weeks of arguing about endings, villains, subtitles and whether a bad third act ruins a film.\n\nYou disagreed with us constantly, which is the whole point. A film page where everyone agrees is a film page nobody reads.\n\n👇 What was the best argument we had?\n\n🔁 Share this if you enjoyed it." + T_D + F),
("list", "5 Films We'll Argue About Forever",
 ["Inception — did the top fall?", "No Country for Old Men — that ending",
  "Blade Runner — is Deckard one?", "The Shining — what does it mean?",
  "2001 — what happens at the end?"],
 "UNRESOLVED",
 "❓ Every one of these has been argued about for decades without resolution — and every one is better for it.\n\nA film that answers everything is finished the moment it ends. These aren't finished.\n\n👇 Pick one and give us your answer.\n\n🔁 Save this and revisit the arguments." + T_D + F),
("take", "Ambiguity isn't the director\nbeing lazy.\n\nIt's the director\ntrusting *you*. 🎯", "HOT TAKE", "🎬",
 "🎯 \"They just didn't know how to end it\" is usually wrong. Leaving a question open is a deliberate, difficult choice — and much harder to land than a tidy resolution.\n\nAn answered film is over. An open one keeps running in your head for years.\n\n👇 Which ambiguous ending do you think about most?\n\n🔁 Share this with someone who hates open endings." + T_D + F),
("take", "You pick what's next 🎬\n\nThis page is built\naround what *you*\nactually want.", "YOUR CALL", "🗳️",
 "🗳️ End of two weeks. Everything on this page from here is shaped by what you ask for.\n\nSo pick:\n\n→ A specific film reviewed properly (name it)\n→ A deep dive on one director or actor\n→ More quizzes, riddles and puzzles\n→ Underrated films nobody talks about\n→ Something else entirely\n\n👇 Comment what you want next. Top answers get built.\n\n🔁 Share this if you want the page to keep going." + T_R + F),
]

assert len(POSTS) == 43, len(POSTS)


def slots():
    """Yield (date, hour) for each of the 43 static posts."""
    out = []
    d0 = date(2026, 7, 31)
    out += [(d0, h) for h in (13, 15, 19, 23)]              # Jul 31: 4
    for i in range(1, 8):                                    # Aug 1-7: 13:00 only
        out.append((date(2026, 8, i), 13))
    for i in range(8, 16):                                   # Aug 8-15: 4 each
        out += [(date(2026, 8, i), h) for h in (13, 15, 19, 23)]
    return out


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    sl = slots()
    assert len(sl) == len(POSTS), f"{len(sl)} slots vs {len(POSTS)} posts"
    n = 0
    for idx, (entry, (d, hour)) in enumerate(zip(POSTS, sl)):
        iid = f"tmrs-{d:%m%d}-{hour:02d}"
        if iid in have:
            continue
        img = f"{IMG}/{d:%m%d}_{hour:02d}.png"
        kind = entry[0]
        if kind == "take":
            _, text, kicker, emoji, cap = entry
            render(movie_take, text, img, kicker=kicker, emoji=emoji)
        elif kind == "list":
            _, title, li, kicker, cap = entry
            render(movie_list, title, li, img, kicker=kicker)
        else:  # review — pull the official poster
            _, title, year, rating, verdict, line, genre, cap = entry
            poster = ""
            try:
                from tmdb import cache_poster
                poster = cache_poster(title, year)
            except Exception as e:
                print(f"   poster lookup failed for {title}: {str(e)[:80]}")
            render(movie_review_poster, title, year, rating, verdict, line, img,
                   genre=genre, poster_url=poster)
        n += 1
        print(f"  {iid} {kind:6s} -> {img}")
        items.append({"id": iid, "account": "top-movie-reviews", "network": "facebook",
                      "type": "photo", "message": cap, "image_url": img,
                      "when": f"{d.isoformat()}T{hour:02d}:00:00+00:00", "status": "pending"})
    save(q)
    print(f"TMR STATIC: {n} new posts, queue now {len(items)} items")


if __name__ == "__main__":
    build()
