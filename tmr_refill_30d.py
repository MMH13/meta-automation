# -*- coding: utf-8 -*-
"""Top Movie Reviews — 30-day refill, 4/day (2026-08-16 -> 2026-09-14),
continuing right after tmr_static_aug.py's Aug 15 tail. Same format/voice:
take (puzzle/hot-take/fact/debate), review (poster + rating), list (top-5).
60 unique items across 3 pools, cycled across 120 slots — each repeats ~2x."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from datetime import date, timedelta

from aug_common import load, save, mkdir, render
from image_movie import movie_take, movie_list, movie_review_poster

IMG = mkdir("images/tmr_refill1")
F = "\n\n🎬 Top Movie Reviews — one honest verdict a day."
T_R = "\n\n#MovieReview #FilmTwitter #Cinephile #MustWatch #MovieNight #FilmLovers #WhatToWatch #Cinema"
T_G = "\n\n#GuessTheMovie #MovieQuiz #FilmBuff #MovieTrivia #Cinephile #MovieGame #NameThatMovie"
T_D = "\n\n#MovieDebate #FilmTwitter #Cinephile #HotTake #MovieTalk #FilmDiscussion #Cinema"

# ---------------------------------------------------------------- reviews
# (title, year, rating, verdict, line, genre, caption)
REVIEWS = [
 ("Parasite", 2019, 5.0, "MASTERPIECE",
  "Bong Joon-ho's genre-hopping class thriller that earns every twist and became the first non-English Best Picture winner.",
  "THRILLER · DRAMA",
  "🎬 PARASITE (2019) — 5/5\n\nA poor family cons their way into working for a wealthy one, one lie at a time. Then the film changes shape completely — twice.\n\nBong Joon-ho refuses to let you settle into one genre. It's a comedy, then a thriller, then something closer to horror, and every shift is earned by what came before. The staircase, the flood, the birthday party — each sequence recalibrates what the film is about.\n\nIt's rare for a film this entertaining to also be this angry. The class commentary never feels like a lecture because the story does all the arguing.\n\nWeakness: nothing, honestly. If anything, the ending is almost too quiet after everything before it — and that's deliberate.\n\nVerdict: the best film of its decade, and it's not particularly close.\n\n👇 First watch or rewatch — did you see the twist coming?\n\n🔁 Share this with someone who still hasn't seen it." + T_R + F),
 ("The Dark Knight", 2008, 5.0, "MASTERPIECE",
  "Heath Ledger's Joker turns a superhero sequel into a genuine crime epic about chaos versus order.",
  "ACTION · CRIME",
  "🎬 THE DARK KNIGHT (2008) — 5/5\n\nThe film that proved a comic-book movie could be a genuine crime epic, not a lesser genre wearing a cape.\n\nHeath Ledger's Joker isn't just a great villain performance — it's a philosophical argument the whole film has to answer. He doesn't want money or power. He wants to prove chaos always wins, and Nolan builds every set piece around testing that theory.\n\nThe ferry scene alone justifies the whole runtime. Two boats, one choice, and the film trusts the audience to sit with the tension instead of rushing past it.\n\nWeakness: Two-Face's turn happens fast, almost too fast for how much the film asks you to feel about it.\n\nVerdict: still the ceiling for what a blockbuster can be.\n\n👇 Best Joker performance — Ledger, or does someone else even come close?\n\n🔁 Share this with someone who still hasn't seen it." + T_R + F),
 ("Interstellar", 2014, 4.5, "AMBITIOUS",
  "Nolan's love-letter to physics and fatherhood — a three-hour space epic that goes for the tear-jerker and mostly earns it.",
  "SCI-FI · DRAMA",
  "🎬 INTERSTELLAR (2014) — 4.5/5\n\nA father leaves his daughter behind to save humanity, and the film spends three hours making you feel exactly what that costs.\n\nThe science is real enough that a physicist consulted on the black hole visuals — but the film's actual engine is the relationship, not the wormhole. That docking sequence set to Hans Zimmer's score is as tense as anything Nolan has made.\n\nThe farmhouse scene, where years pass in messages, is one of the most devastating stretches in his filmography.\n\nWeakness: the fifth-dimension bookshelf sequence divides people hard — some find it moving, others find it a bridge too far.\n\nVerdict: flawed, enormous, and unforgettable.\n\n👇 Did the ending work for you, or lose you?\n\n🔁 Share this with someone who cried at the docking scene." + T_R + F),
 ("Goodfellas", 1990, 5.0, "MASTERPIECE",
  "Scorsese's kinetic mob epic that makes crime look thrilling right up until it shows you exactly what it costs.",
  "CRIME · DRAMA",
  "🎬 GOODFELLAS (1990) — 5/5\n\n\"As far back as I can remember, I always wanted to be a gangster.\" Then the film spends 145 minutes showing you why, and why that was a mistake.\n\nThe Copacabana tracking shot is the most famous single shot in gangster cinema for a reason — it makes the lifestyle look genuinely irresistible before the back half turns the same energy into paranoia and cocaine-fuelled dread.\n\nJoe Pesci's Tommy is terrifying precisely because the film never signals when he's about to explode. Neither do the characters around him.\n\nWeakness: the final act's frantic pacing is intentional, but it's genuinely exhausting on a first watch.\n\nVerdict: the template every mob film since has been measured against.\n\n👇 Best Scorsese film — go 👇\n\n🔁 Share this with someone who's never sat through the whole thing." + T_R + F),
 ("Pulp Fiction", 1994, 5.0, "MASTERPIECE",
  "Tarantino scrambled the timeline and reinvented what a crime film could sound like — still endlessly quotable three decades on.",
  "CRIME · DRAMA",
  "🎬 PULP FICTION (1994) — 5/5\n\nThree stories, told out of order, connected by a briefcase nobody ever fully explains. It shouldn't work. It's one of the most influential films ever made.\n\nWhat holds it together isn't plot — it's voice. Every character, down to the diner robbers, talks like they've thought about foot massages and Royales with cheese their whole life. That's the real innovation: dialogue as characterization, not exposition.\n\nSamuel L. Jackson's Ezekiel 25:17 monologue is one of the great screen performances of the '90s, and it's delivered twice with two completely different meanings.\n\nWeakness: the nonlinear structure is a gimmick for some viewers — it rewards rewatching more than it rewards a first pass.\n\nVerdict: still the most purely fun 2.5 hours in serious cinema.\n\n👇 Which story thread is your favourite — Vincent, Butch, or Jules?\n\n🔁 Share this with someone who's only seen the poster." + T_R + F),
 ("No Country for Old Men", 2007, 5.0, "MASTERPIECE",
  "The Coens' bleak, near-silent thriller where the villain is unstoppable and the hero doesn't get to win.",
  "THRILLER · CRIME",
  "🎬 NO COUNTRY FOR OLD MEN (2007) — 5/5\n\nA man finds two million dollars at a drug deal gone wrong. What follows is one of the tensest, quietest thrillers ever made.\n\nJavier Bardem's Anton Chigurh barely raises his voice and is somehow the most frightening screen presence of the decade — a captive bolt pistol and a coin flip as his entire moral code. The Coens strip out the score almost entirely, so every creak of a floorboard lands like a gunshot.\n\nThe ending refuses the genre's usual catharsis completely, and that's the whole point the film is making about violence and old age.\n\nWeakness: if you need a clean resolution, this will genuinely frustrate you. That's by design, but it's worth the warning.\n\nVerdict: as close to a perfect thriller as the genre gets.\n\n👇 That ending — brilliant or a letdown? Be honest.\n\n🔁 Share this with someone who needs the warning." + T_R + F),
 ("Her", 2013, 4.5, "TENDER",
  "Spike Jonze's quiet sci-fi romance about a man falling for his AI — eerily more relevant with every passing year.",
  "SCI-FI · ROMANCE",
  "🎬 HER (2013) — 4.5/5\n\nA lonely man falls in love with an operating system. It sounds like a gimmick premise. It's one of the most sincere romances of the 2010s.\n\nJoaquin Phoenix carries entire scenes on his face alone, reacting to a voice, and Scarlett Johansson's vocal performance does more emotional work than most fully embodied ones. The near-future Los Angeles is warm and pastel, never dystopian — which makes the loneliness land harder, not softer.\n\nIt was written and shot years before anyone had a voice assistant on their phone. Watching it now feels less like science fiction and more like a documentary that arrived early.\n\nWeakness: the pacing is deliberately slow — if you want plot momentum, this isn't built for you.\n\nVerdict: tender, prophetic, and quietly devastating.\n\n👇 Did this feel like fiction to you, or a little too real?\n\n🔁 Share this with someone glued to their AI chatbot." + T_R + F),
 ("Moonlight", 2016, 4.5, "PROFOUND",
  "A three-act coming-of-age story about identity, told in near-silence, that won Best Picture in the most chaotic envelope moment ever.",
  "DRAMA",
  "🎬 MOONLIGHT (2016) — 4.5/5\n\nThree chapters, three actors, one boy growing into a man who's never been allowed to just be himself.\n\nBarry Jenkins shoots silence better than almost anyone working — entire scenes carry more weight in a held look than most films manage in a page of dialogue. The beach scene in chapter one is one of the tenderest moments put on screen this century.\n\nIt's a small, intimate film that never reaches for a big moment, and that restraint is exactly why it lingers.\n\nWeakness: the deliberate pace and structure ask a lot of patience from viewers used to more conventional plotting.\n\nVerdict: quiet, patient, and genuinely moving.\n\n👇 Which of the three chapters hit hardest for you?\n\n🔁 Share this with someone who's never seen a Barry Jenkins film." + T_R + F),
 ("The Grand Budapest Hotel", 2014, 4.5, "DELIGHTFUL",
  "Wes Anderson's most purely fun film — a caper wrapped in pastel symmetry with a surprisingly sad center.",
  "COMEDY · ADVENTURE",
  "🎬 THE GRAND BUDAPEST HOTEL (2014) — 4.5/5\n\nA concierge and his lobby boy get tangled in a stolen painting, a murder, and a prison break — all inside Anderson's most meticulously designed world yet.\n\nRalph Fiennes is a revelation as Gustave H, somehow perfectly deadpan and genuinely heartfelt at once. The film moves at a sprint, gag after gag, and yet finds time for a real melancholy underneath — a world about to be destroyed by war, glimpsed through a story about manners and loyalty.\n\nEvery frame is symmetrical to the point of obsession. It should feel cold. It doesn't.\n\nWeakness: the whimsy is a lot — if Anderson's style isn't for you, this is the most Anderson film there is.\n\nVerdict: his funniest film with his saddest ending.\n\n👇 Favourite Wes Anderson film — go 👇\n\n🔁 Share this with someone who's never watched a Wes Anderson film." + T_R + F),
 ("Children of Men", 2006, 5.0, "MASTERPIECE",
  "Cuarón's dystopian thriller with the greatest unbroken action take in modern cinema — bleak, urgent, and still unmatched.",
  "SCI-FI · THRILLER",
  "🎬 CHILDREN OF MEN (2006) — 5/5\n\nNo child has been born in 18 years. Then one is. The film that follows is grim, breathless, and one of the most technically astonishing thrillers ever made.\n\nThe car ambush sequence, shot in a single unbroken take with a camera rig built specifically for it, is still the reference point directors point to when discussing long takes. But the craft never overshadows the story — a refugee crisis that felt speculative in 2006 and feels close to documentary now.\n\nClive Owen carries the exhaustion of the whole film in his face, barely speaking when it counts most.\n\nWeakness: it's relentlessly bleak — there's very little relief across the runtime.\n\nVerdict: one of the great, underseen masterpieces of the 2000s.\n\n👇 Have you seen it? If not, why not — genuinely?\n\n🔁 Share this with someone who thinks they've seen every great sci-fi film." + T_R + F),
 ("Eternal Sunshine of the Spotless Mind", 2004, 5.0, "MASTERPIECE",
  "Kaufman and Gondry turn a breakup into a memory-erasing sci-fi maze that somehow argues FOR heartbreak.",
  "SCI-FI · ROMANCE",
  "🎬 ETERNAL SUNSHINE OF THE SPOTLESS MIND (2004) — 5/5\n\nA couple erases each other from their memories after a bad breakup. Then, mid-procedure, one of them decides he wants to keep her after all.\n\nMichel Gondry's practical, in-camera effects — rooms collapsing, faces blurring, memories dissolving in real time — still look more inventive than most modern CGI. But the real trick is Kaufman's script, which uses the gimmick to argue something genuinely moving: that the pain is worth it, that you'd choose the heartbreak again just to have had the good part.\n\nJim Carrey's most restrained, best performance sits at the center of it.\n\nWeakness: the nonlinear memory structure takes real attention to track on a first watch.\n\nVerdict: the smartest, saddest romance of its decade.\n\n👇 Would you actually erase a painful relationship if you could?\n\n🔁 Share this with someone going through a breakup (gently)." + T_R + F),
 ("City of God", 2002, 5.0, "MASTERPIECE",
  "A kinetic, unflinching portrait of Rio's favelas told through a decade of gang violence — one of the great debuts in film history.",
  "CRIME · DRAMA",
  "🎬 CITY OF GOD (2002) — 5/5\n\nTwo boys grow up in Rio's favelas. One becomes a photographer. The other becomes one of the most feared gang leaders in the city. The film follows both, and everyone around them, across a decade.\n\nFernando Meirelles shoots poverty and violence with a kinetic, almost joyful camera style that makes the horror land harder by contrast — the film never asks for pity, it just shows you exactly what happened.\n\nMost of the cast were non-actors recruited from actual favelas, which gives every scene a rawness professional actors rarely achieve.\n\nWeakness: the violence is unflinching and constant — it's not an easy watch, and it isn't trying to be.\n\nVerdict: one of the greatest crime films ever made, from any country.\n\n👇 Have you seen it? It deserves to be talked about more.\n\n🔁 Share this with someone who's never watched a Brazilian film." + T_R + F),
 ("The Departed", 2006, 4.5, "RELENTLESS",
  "Scorsese's Boston crime saga where two moles — one cop, one criminal — race to expose each other before it's too late.",
  "CRIME · THRILLER",
  "🎬 THE DEPARTED (2006) — 4.5/5\n\nA cop infiltrates the mob. A mobster infiltrates the police. Neither knows the other exists until they're both racing to unmask a rat before they're found first.\n\nScorsese finally won his Best Director Oscar for this, and while it's not his most personal work, it might be his most purely entertaining — Nicholson unhinged, DiCaprio at his most anxious, Damon coolly dangerous, Wahlberg stealing every scene he's in.\n\nThe final ten minutes deliver one of the bleakest, most efficient endings in the genre.\n\nWeakness: the rat symbolism at the very end is the one moment the film oversells its point.\n\nVerdict: a genre exercise executed at the highest possible level.\n\n👇 Best performance in this cast — genuinely stacked. Go 👇\n\n🔁 Share this with someone who loves a good double-cross." + T_R + F),
 ("There Will Be Blood", 2007, 5.0, "MASTERPIECE",
  "Daniel Day-Lewis becomes an oil baron consumed by greed in one of the most towering performances ever filmed.",
  "DRAMA",
  "🎬 THERE WILL BE BLOOD (2007) — 5/5\n\n\"I drink your milkshake.\" A line so famous it's easy to forget the two-and-a-half hours of slow-burning menace that earn it.\n\nDaniel Day-Lewis doesn't play Daniel Plainview so much as inhabit him completely — an oil prospector whose ambition curdles into something monstrous scene by scene. Paul Thomas Anderson shoots the American West as a place greed built and greed will eventually hollow out.\n\nJonny Greenwood's dissonant score does as much storytelling as any dialogue in the film.\n\nWeakness: the deliberate, punishing pace will lose viewers who want momentum over atmosphere.\n\nVerdict: one of the defining American films of the 21st century.\n\n👇 That final scene — still one of the boldest closes in cinema. Thoughts?\n\n🔁 Share this with someone who's never seen a PTA film." + T_R + F),
 ("Mad Max: Fury Road", 2015, 5.0, "MASTERPIECE",
  "A two-hour car chase that redefined what modern action cinema could look like — practical, relentless, and shockingly coherent.",
  "ACTION · SCI-FI",
  "🎬 MAD MAX: FURY ROAD (2015) — 5/5\n\nThe plot is a truck driving in one direction, then the other. That's genuinely most of it. It's still one of the best action films ever made.\n\nGeorge Miller, at 70 years old, shot almost everything practically — real cars, real stunts, real desert — and edited it so every single shot tells you exactly where everyone is and what's happening. That clarity is what most modern action films have completely lost.\n\nFuriosa arguably steals the film from its own title character, and the film is better for letting her.\n\nWeakness: if you want dialogue-driven story, this genuinely isn't it — the film says almost everything through motion.\n\nVerdict: the action benchmark every blockbuster since has failed to match.\n\n👇 Best modern action film — does anything actually beat this?\n\n🔁 Share this with someone who thinks action films peaked in the '90s." + T_R + F),
]

# ------------------------------------------------------------------- lists
# (title_html, items, kicker, caption)
LISTS = [
 ("Endings That *Recontextualize*<br>the Whole Film",
  ["The Sixth Sense (1999)", "Fight Club (1999)", "The Usual Suspects (1995)",
   "Shutter Island (2010)", "Parasite (2019)"], "THE TWIST",
  "🌀 Some endings don't just surprise you — they make you want to start the film over immediately.\n\n1️⃣ THE SIXTH SENSE — the one that made everyone rewind\n2️⃣ FIGHT CLUB — every scene means something different now\n3️⃣ THE USUAL SUSPECTS — that coffee cup\n4️⃣ SHUTTER ISLAND — the final line changes everything\n5️⃣ PARASITE — the letter that will never arrive\n\n👇 Which one made you immediately rewatch it?\n\n🔁 Save this list." + T_R + F),
 ("Movie Monologues That Still\n*Give You Chills*",
  ["\"I coulda had class\" — On the Waterfront", "\"You can't handle the truth\" — A Few Good Men",
   "\"Ezekiel 25:17\" — Pulp Fiction", "\"I drink your milkshake\" — There Will Be Blood",
   "\"Greed is good\" — Wall Street"], "PURE ACTING",
  "🎤 A great monologue needs no music, no cuts, no help. Just an actor and a room.\n\n1️⃣ ON THE WATERFRONT — Brando's coulda-been-a-contender\n2️⃣ A FEW GOOD MEN — Nicholson at full volume\n3️⃣ PULP FICTION — Jules before he pulls the trigger\n4️⃣ THERE WILL BE BLOOD — Day-Lewis unravels completely\n5️⃣ WALL STREET — Gekko's whole philosophy in ninety seconds\n\n👇 Which one do you know word for word?\n\n🔁 Save this list." + T_R + F),
 ("Sequels That Beat\nthe *Original*",
  ["The Godfather Part II (1974)", "Aliens (1986)", "Terminator 2 (1991)",
   "The Dark Knight (2008)", "Toy Story 2 (1999)"], "RARE AIR",
  "⚡ Lightning striking twice is genuinely rare. These five did it.\n\n1️⃣ GODFATHER PART II — deepens everything the first film built\n2️⃣ ALIENS — swaps horror for war and somehow it works better\n3️⃣ TERMINATOR 2 — the villain becomes the hero and it's flawless\n4️⃣ THE DARK KNIGHT — Batman Begins was good. This was generational.\n5️⃣ TOY STORY 2 — rare Pixar sequel that out-emotions the original\n\n👇 Which sequel beat its original for you?\n\n🔁 Save this list." + T_R + F),
 ("Movies With *One Location*\nThat Never Get Boring",
  ["12 Angry Men (1957)", "Rope (1948)", "Buried (2010)",
   "Locke (2013)", "The Shining (1980, mostly)"], "CONTAINED CINEMA",
  "🚪 No car chases. No new sets. Just tension, built entirely from a single room.\n\n1️⃣ 12 ANGRY MEN — one jury room, unbearable tension\n2️⃣ ROPE — Hitchcock, one apartment, fake-single-take\n3️⃣ BURIED — Ryan Reynolds, a coffin, ninety minutes\n4️⃣ LOCKE — a man, a car, a phone, one of the tensest dramas ever\n5️⃣ THE SHINING — one hotel becomes a character itself\n\n👇 Which one proves you don't need a big budget?\n\n🔁 Save this list." + T_R + F),
 ("Directors Whose Style You Can\n*Spot in 5 Seconds*",
  ["Wes Anderson — symmetry and pastel", "Quentin Tarantino — trunk shots and dialogue",
   "Christopher Nolan — nonlinear time", "Denis Villeneuve — scale and silence",
   "David Fincher — desaturated dread"], "SIGNATURE STYLE",
  "🎥 Mute the trailer and you'd still know exactly whose film this is.\n\n1️⃣ WES ANDERSON — perfect symmetry, pastel palettes\n2️⃣ TARANTINO — trunk shots, feet, endless dialogue\n3️⃣ NOLAN — time bent into a structure, never linear\n4️⃣ VILLENEUVE — massive scale, minimal dialogue\n5️⃣ FINCHER — every scene looks slightly sick, on purpose\n\n👇 Whose style is the most instantly recognizable to you?\n\n🔁 Save this list." + T_R + F),
 ("Villains Who Only Appear in\n*One Scene* and Steal the Film",
  ["Alfred Molina — Boogie Nights", "Christoph Waltz — Inglourious Basterds (opener)",
   "Gary Oldman — The Professional", "Judi Dench — Shakespeare in Love",
   "Anthony Hopkins — Silence of the Lambs (screen time)"], "MINIMAL SCREEN TIME",
  "⏱️ Some actors don't need the runtime — they need one scene to own the whole film.\n\n1️⃣ ALFRED MOLINA — Boogie Nights, one unbearable drug-deal scene\n2️⃣ CHRISTOPH WALTZ — that farmhouse opener alone won him the Oscar conversation\n3️⃣ GARY OLDMAN — Léon, pure menace in every frame he's in\n4️⃣ JUDI DENCH — 8 minutes of screen time, Best Supporting Oscar\n5️⃣ HOPKINS — barely 16 minutes of screen time in the whole film\n\n👇 Which performance surprised you when you found out the runtime?\n\n🔁 Save this list." + T_R + F),
 ("Films That Made You Root for\nthe *Wrong Person*",
  ["No Country for Old Men", "Nightcrawler", "American Psycho",
   "Joker (2019)", "Gone Girl"], "MORALLY GREY",
  "😬 The film knows exactly what it's doing when you catch yourself rooting for the villain.\n\n1️⃣ NO COUNTRY — Chigurh's coin flips still make you tense, not relieved\n2️⃣ NIGHTCRAWLER — Gyllenhaal's ambition is repulsive and magnetic\n3️⃣ AMERICAN PSYCHO — satire so sharp people miss the point entirely\n4️⃣ JOKER — the film dares you to sympathize, then pulls back\n5️⃣ GONE GIRL — by the end you're not sure who you're rooting for\n\n👇 Which one made you feel the most uncomfortable about your own reaction?\n\n🔁 Save this list." + T_R + F),
 ("Scores That Are Better Than\nthe Films *Deserve*",
  ["Tron: Legacy — Daft Punk", "Drive — Cliff Martinez",
   "The Social Network — Reznor/Ross", "Blade Runner 2049 — Zimmer/Wallfisch",
   "It Follows — Disasterpeace"], "UNDERRATED SCORES",
  "🎧 Sometimes the soundtrack does more work than the script.\n\n1️⃣ TRON: LEGACY — Daft Punk's only film score, still incredible\n2️⃣ DRIVE — synthwave before synthwave was a genre name\n3️⃣ THE SOCIAL NETWORK — the score that made 'Facebook drama' feel like a heist\n4️⃣ BLADE RUNNER 2049 — dread you can feel in your chest\n5️⃣ IT FOLLOWS — one of the scariest scores ever written\n\n👇 Which score do you listen to outside the film?\n\n🔁 Save this list." + T_R + F),
 ("Movies Where the *Setting*\nIs Basically a Character",
  ["Jaws — Amity Island", "The Shining — the Overlook Hotel",
   "Blade Runner — future LA", "Parasite — the two houses",
   "Mad Max: Fury Road — the desert"], "PLACE AS CHARACTER",
  "🗺️ Change the setting and these films fall apart completely.\n\n1️⃣ JAWS — a beach town that can't afford to close its beach\n2️⃣ THE SHINING — a hotel with its own memory and malice\n3️⃣ BLADE RUNNER — a city as drenched in mood as any character\n4️⃣ PARASITE — two houses that ARE the entire class argument\n5️⃣ FURY ROAD — a desert that's basically the antagonist\n\n👇 Which setting could you never imagine the story without?\n\n🔁 Save this list." + T_R + F),
 ("Directorial *Comebacks*\nAfter Years Away",
  ["Mad Max: Fury Road — Miller, 30 years later", "The Irishman — Scorsese, epic scale return",
   "A Quiet Place — Krasinski's genre pivot", "Top Gun: Maverick — Cruise/Kosinski, decades later",
   "The Batman — Reeves after years in blockbuster limbo"], "SECOND ACTS",
  "🎬 Sometimes the wait makes the return hit even harder.\n\n1️⃣ FURY ROAD — 30 years after the original trilogy, somehow better\n2️⃣ THE IRISHMAN — Scorsese at 77, still swinging for the fences\n3️⃣ A QUIET PLACE — Krasinski's total genre reinvention\n4️⃣ TOP GUN: MAVERICK — proof legacy sequels can actually work\n5️⃣ THE BATMAN — a genuinely different take after years of noise\n\n👇 Best comeback film — go 👇\n\n🔁 Save this list." + T_R + F),
 ("Films Under $10 Million\nThat Made Hundreds of Millions",
  ["Paranormal Activity — $15k budget", "The Blair Witch Project — $60k budget",
   "Get Out — $4.5M budget", "Rocky — $1M budget", "Napoleon Dynamite — $400k budget"],
  "MICRO-BUDGET MIRACLES",
  "💰 Proof a great idea beats a big budget almost every time.\n\n1️⃣ PARANORMAL ACTIVITY — $15,000 budget, nearly $200M worldwide\n2️⃣ BLAIR WITCH — $60,000 shot on consumer camcorders\n3️⃣ GET OUT — $4.5M, one of the smartest horror films ever made\n4️⃣ ROCKY — $1M, won Best Picture\n5️⃣ NAPOLEON DYNAMITE — $400k, cult phenomenon for two decades\n\n👇 Which one still surprises you the most?\n\n🔁 Save this list." + T_R + F),
 ("Actors Who Turned Down\n*Iconic* Roles",
  ["Will Smith — Neo in The Matrix", "Tom Selleck — Indiana Jones",
   "Sean Connery — Gandalf", "Emily Blunt — Black Widow",
   "Leonardo DiCaprio — Neo in The Matrix"], "THE ROAD NOT TAKEN",
  "🤯 Some of cinema's most iconic castings almost went to someone completely different.\n\n1️⃣ WILL SMITH — passed on Neo to make Wild Wild West instead\n2️⃣ TOM SELLECK — a scheduling conflict cost him Indiana Jones\n3️⃣ SEAN CONNERY — turned down Gandalf, called the script 'confusing'\n4️⃣ EMILY BLUNT — passed on Black Widow before Scarlett Johansson\n5️⃣ DICAPRIO — was ALSO offered Neo before Reeves\n\n👇 Which almost-casting would've changed everything?\n\n🔁 Save this list." + T_R + F),
 ("Films That Get Better\non the *Third* Watch",
  ["Mulholland Drive", "Arrival", "The Prestige",
   "Primer", "Blade Runner 2049"], "REWATCH VALUE",
  "🔁 Some films aren't fully finished until you've seen them at least three times.\n\n1️⃣ MULHOLLAND DRIVE — the third watch is when the pieces finally click\n2️⃣ ARRIVAL — the structure means every rewatch reveals more\n3️⃣ THE PRESTIGE — you catch the trick hiding in plain sight\n4️⃣ PRIMER — genuinely needs a diagram and multiple viewings\n5️⃣ BLADE RUNNER 2049 — dense with details you miss the first time\n\n👇 Which film did you truly 'get' on rewatch #3?\n\n🔁 Save this list." + T_R + F),
 ("Best *Cold Opens*\nin Movie History",
  ["Up (2009)", "Inglourious Basterds (2009)", "No Country for Old Men (2007)",
   "There Will Be Blood (2007)", "The Dark Knight (2008)"], "FIRST FIVE MINUTES",
  "🎬 You've got five minutes to hook an audience before they decide. These nailed it.\n\n1️⃣ UP — the wordless marriage montage, four minutes, everyone cries\n2️⃣ INGLOURIOUS BASTERDS — a farmhouse, unbearable tension\n3️⃣ NO COUNTRY — Chigurh's strangling scene, near silence, pure dread\n4️⃣ THERE WILL BE BLOOD — 15 minutes, barely a word of dialogue\n5️⃣ THE DARK KNIGHT — the bank heist that introduces the Joker perfectly\n\n👇 Best cold open — pick one 👇\n\n🔁 Save this list." + T_R + F),
 ("Movies That Predicted the Future\n(Whether They Meant To or Not)",
  ["Her — AI companionship", "Minority Report — targeted ads",
   "The Truman Show — reality TV/social media", "Wall-E — consumer culture",
   "Network — 24-hour outrage media"], "ACCIDENTAL PROPHECY",
  "🔮 Some films weren't trying to predict anything. They just got uncomfortably close.\n\n1️⃣ HER — AI companionship, years before it was a real product category\n2️⃣ MINORITY REPORT — personalized ads that scan your eyes, now basically real\n3️⃣ THE TRUMAN SHOW — a life lived for an audience, before social media existed\n4️⃣ WALL-E — consumer culture taken to its logical, uncomfortable end\n5️⃣ NETWORK — 'I'm mad as hell' predicted cable news by decades\n\n👇 Which one feels the most uncomfortably accurate now?\n\n🔁 Save this list." + T_R + F),
]

# ------------------------------------------------------------------- takes
# (text, kicker, emoji, caption) — mix of puzzle/fact/debate/hot-take
TAKES = [
 ("🎬 🏝️ 🏐 🔥 🦀\n\n*Guess the movie.*", "EMOJI PUZZLE", "🧩",
  "🧩 Five emojis, one very famous film about being stranded.\n\n👇 Comment your answer.\n\n🔁 Share this with someone who talks to volleyballs." + T_G + F),
 ("🎬 🕷️ 🕸️ 🏙️ 👨\n\n*Guess the movie.*\n\n(Multiple valid answers.)", "EMOJI PUZZLE", "🧩",
  "🧩 This one's got more than one right answer. Name any of them.\n\n👇 Comment your pick.\n\n🔁 Share this with a comic-book fan." + T_G + F),
 ("Finish the line:\n\n\"With great power comes\ngreat ______\"", "FINISH IT", "🎬",
  "🎬 One of the most quoted lines in modern film history. Everyone knows it.\n\n👇 Comment the full line.\n\n🔁 Share this with a Spider-Man fan." + T_G + F),
 ("A movie can win Best Picture\nand still not be your\n*favourite* film of that year.", "HOT TAKE", "🏆",
  "🏆 Awards measure a committee's taste in one specific season. They don't measure what actually stuck with you.\n\nPlenty of Best Picture winners are forgotten faster than the films they beat.\n\n👇 Name a Best Picture winner that isn't even your favourite from that YEAR.\n\n🔁 Share this and start an argument." + T_D + F),
 ("The *trailer* for a horror film\nis often scarier than\nthe actual film. 👻", "HOT TAKE", "👻",
  "👻 Trailers cut together the three best jump scares with a pulse-pounding edit. The full film has to build atmosphere for 90 minutes to earn even one of those moments.\n\nThat's why so many horror trailers peak before the movie even starts.\n\n👇 A horror trailer that was scarier than the film itself?\n\n🔁 Share this with a horror fan." + T_D + F),
 ("Some actors are\n*always* playing\nthe same character —\nand it still works. 🎭", "THE DEBATE", "🎭",
  "🎭 Certain actors have a persona so strong that every role becomes a variation on it. Sometimes that's a criticism. Sometimes it's exactly why you buy a ticket.\n\n👇 Name an actor who's 'always the same guy' — and you still love it.\n\n🔁 Share this and see who agrees." + T_D + F),
 ("A film's *first ten minutes*\ntell you everything about\nhow much it respects you.", "HOT TAKE", "⏱️",
  "⏱️ Exposition dumped through clunky dialogue in the opening scene is a film that doesn't trust its audience. A film that shows instead of tells, right from frame one, usually earns your trust for the next two hours.\n\n👇 A film whose opening ten minutes told you exactly what you were in for?\n\n🔁 Share this with someone who judges a film fast." + T_D + F),
 ("🎬 🐉 🏰 ⚔️ 💍\n\n*Guess the trilogy.*", "EMOJI PUZZLE", "🧩",
  "🧩 Five emojis, one legendary trilogy.\n\n👇 Comment your answer.\n\n🔁 Share this with a fantasy fan." + T_G + F),
 ("The *hardest* job in a movie\nisn't the lead role.\nIt's playing the character\neveryone has to believe\nis funny. 😂", "MOVIE FACT", "😂",
  "😂 Drama has a formula. Comedy has timing, and timing either works or it completely doesn't — there's no partial credit.\n\nThat's why great comedic performances get overlooked at awards season constantly.\n\n👇 A comedic performance that deserved more recognition?\n\n🔁 Share this with someone who underrates comedy." + T_D + F),
 ("You can tell a director\ntrusts their actors when\nthey let a scene run\n*long*. 🎥", "MOVIE FACT", "🎥",
  "🎥 Cutting fast is often a safety net — it hides a performance that isn't quite landing. Letting a scene breathe is a director betting everything on the actor in front of the camera.\n\n👇 A scene that ran long and was better for it?\n\n🔁 Share this with someone who loves a slow burn." + T_R + F),
 ("Finish the line:\n\n\"I feel the need...\nthe need for ______\"", "FINISH IT", "🎬",
  "🎬 One of the most quoted duos in movie history said this together.\n\n👇 Comment the full line — and the film.\n\n🔁 Share this with someone who quotes '80s action films." + T_G + F),
 ("🎬 🧙 💍 🌋 👁️\n\n*Guess the movie.*", "EMOJI PUZZLE", "🧩",
  "🧩 Five emojis, one eye you definitely recognize.\n\n👇 Comment your answer.\n\n🔁 Share this with a fantasy fan." + T_G + F),
 ("A film doesn't need a\n*likeable* protagonist.\nIt needs an\n*interesting* one. 🎭", "HOT TAKE", "🎭",
  "🎭 'I couldn't root for anyone' is one of the most common complaints about serious dramas — and it usually misses the point entirely.\n\nSome of the greatest films ever made star people you'd never want to actually know.\n\n👇 A film with an unlikeable lead that's still one of your favourites?\n\n🔁 Share this and see who agrees." + T_D + F),
 ("The *best* remakes don't\ncopy the original.\nThey ask a completely\ndifferent question. 🎬", "THE DEBATE", "🔄",
  "🔄 Most remakes fail because they just repeat the same beats with better effects. The rare good ones use the same premise to say something the original never attempted.\n\n👇 Name a remake that's genuinely better than the original.\n\n🔁 Share this and let them argue." + T_D + F),
 ("A twist only works if the\nfilm could've told you\nthe truth *the whole time* —\nand you still wouldn't\nhave seen it. 🌀", "MOVIE FACT", "🌀",
  "🌀 The best twists survive a second viewing. You go back and every clue was right there, hiding in plain sight, and you still fell for it completely.\n\nThat's the difference between a twist and a cheap trick.\n\n👇 A twist that held up perfectly on rewatch?\n\n🔁 Share this with someone who loves a good twist." + T_R + F),
 ("🎬 🚗 🏎️ 💨 🌉\n\n*Guess the movie franchise.*", "EMOJI PUZZLE", "🧩",
  "🧩 Five emojis, one very loud franchise.\n\n👇 Comment your answer.\n\n🔁 Share this with someone who's seen every entry." + T_G + F),
 ("Practical stunts don't\njust look better —\nthey change how the actor\n*performs* the scene. 🎬", "MOVIE FACT", "🎬",
  "🎬 An actor genuinely hanging off a building reacts differently than one standing in front of a green screen imagining it. The fear is real, and the camera catches it.\n\n👇 A stunt sequence you still can't believe was real?\n\n🔁 Share this with an action-movie fan." + T_R + F),
 ("Nobody talks about how\n*exhausting* a two-and-a-half\nhour film can be when it's\ngreat every single minute. 🎬", "HOT TAKE", "⏳",
  "⏳ 'Too long' usually means 'poorly paced,' not 'over two hours.' A great film can run three hours and feel shorter than a mediocre 90-minute one.\n\n👇 A long film that never once felt long?\n\n🔁 Share this with someone who avoids long films." + T_D + F),
 ("Finish the line:\n\n\"Why so ______?\"", "FINISH IT", "🎬",
  "🎬 One of the most quoted villain lines in modern cinema.\n\n👇 Comment the answer.\n\n🔁 Share this with a comic-book fan." + T_G + F),
 ("A great score doesn't\ntell you how to feel.\nIt tells you a half-second\n*before* the scene does. 🎵", "MOVIE FACT", "🎵",
  "🎵 The best film composers work almost subliminally — you feel the shift in tension before your conscious brain registers why.\n\n👇 A score that manipulated your emotions and you didn't even notice?\n\n🔁 Share this with someone who never notices the score." + T_R + F),
 ("🎬 🍫 🏭 🎩 👦\n\n*Guess the movie.*", "EMOJI PUZZLE", "🧩",
  "🧩 Five emojis, one golden ticket.\n\n👇 Comment your answer.\n\n🔁 Share this with someone who loves this one." + T_G + F),
 ("You're allowed to think\na 'classic' is\ngenuinely overrated.\nThat's not a crime. 🎬", "HOT TAKE", "🤷",
  "🤷 Canon status doesn't make a film immune to criticism. You can understand exactly why it's considered great and still not personally rate it that highly.\n\n👇 A 'classic' you think is genuinely overrated — be brave.\n\n🔁 Share this and see who's honest." + T_D + F),
 ("The best plot twists in\nhistory were foreshadowed\nin the *title* the whole time.", "MOVIE FACT", "🎯",
  "🎯 Some of the smartest scripts hide the entire twist in plain sight — right there in the title — and you only notice on the way out of the theatre.\n\n👇 A title that gave away the twist and you didn't even notice?\n\n🔁 Share this with someone who loves a hidden clue." + T_R + F),
 ("A film's *runtime* isn't\nthe problem.\nA film's *pacing* is.", "THE DEBATE", "⏱️",
  "⏱️ People blame length for boredom, but the real culprit is almost always pacing. A tightly-paced three hours beats a saggy ninety minutes every time.\n\n👇 Short but boring, or long but gripping — which frustrates you more?\n\n🔁 Share this and let them debate." + T_D + F),
 ("🎬 🦈 🌊 🏖️ 🚤\n\n*Guess the movie.*", "EMOJI PUZZLE", "🧩",
  "🧩 Five emojis, one iconic theme you can probably hum right now.\n\n👇 Comment your answer.\n\n🔁 Share this with someone afraid of the ocean." + T_G + F),
 ("Some of the best character\nactors have never had\na single leading role —\nand you'd recognize them\ninstantly. 🎭", "MOVIE FACT", "🎭",
  "🎭 The industry has a whole tier of actors who elevate every film they're in without ever headlining one. You know the face. You might not know the name.\n\n👇 Name a character actor who makes every film better?\n\n🔁 Share this and give them credit." + T_R + F),
 ("Finish the line:\n\n\"You talkin' to ______?\"", "FINISH IT", "🎬",
  "🎬 One of the most imitated lines in cinema history.\n\n👇 Comment the answer and the film.\n\n🔁 Share this with someone who does the impression badly." + T_G + F),
 ("A sequel that ignores\nwhat made the first film\nwork isn't really a\nsequel — it's a different\nfilm wearing the name. 🎬", "HOT TAKE", "🎬",
  "🎬 The worst sequels don't fail from lack of budget. They fail because they misunderstand why anyone loved the original in the first place.\n\n👇 A sequel that completely missed the point of its own franchise?\n\n🔁 Share this and let them vent." + T_D + F),
 ("Some films are *better*\nthe less you know\ngoing in. Marketing has\nbecome the enemy of\nthe experience. 🤫", "HOT TAKE", "🤫",
  "🤫 Trailers now regularly show the best three moments, the twist, and sometimes the ending. The best modern viewing habit is genuinely: hear it's good, watch it, ask questions after.\n\n👇 A film you're glad you went into completely blind?\n\n🔁 Share this with a trailer-watcher." + T_D + F),
 ("The credits scene\nculture didn't start\nwhere you think it did. 🎬", "MOVIE FACT", "🎬",
  "🎬 Post-credit scenes feel like a modern superhero-film invention, but the tradition of rewarding patient viewers goes back decades further than most people realize.\n\n👇 Best post-credits scene you've ever sat through for?\n\n🔁 Share this with someone who always leaves early." + T_R + F),
]

DAYS = 30
HOURS = [13, 15, 19, 23]
START_DATE = date(2026, 8, 16)


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    counters = {"review": 0, "list": 0, "take": 0}
    n = 0
    rotation = ["take", "review_or_list", "take", "take"]

    for day_idx in range(DAYS):
        d = START_DATE + timedelta(days=day_idx)
        alt_review = (day_idx % 2 == 0)
        for slot_idx, hour in enumerate(HOURS):
            iid = f"tmrr1-{d.isoformat()}-{hour}"
            if iid in have:
                continue
            when = f"{d.isoformat()}T{hour:02d}:00:00+00:00"
            kind = rotation[slot_idx]
            if kind == "take":
                text, kicker, emoji, caption = TAKES[counters["take"] % len(TAKES)]
                counters["take"] += 1
                img = f"{IMG}/{d.isoformat()}_{hour}.png"
                render(movie_take, text, img, kicker=kicker, emoji=emoji)
            else:
                if alt_review:
                    title, year, rating, verdict, line, genre, caption = REVIEWS[counters["review"] % len(REVIEWS)]
                    counters["review"] += 1
                    img = f"{IMG}/{d.isoformat()}_{hour}.png"
                    render(movie_review_poster, title, year, rating, verdict, line, img, genre=genre)
                else:
                    title, li, kicker, caption = LISTS[counters["list"] % len(LISTS)]
                    counters["list"] += 1
                    img = f"{IMG}/{d.isoformat()}_{hour}.png"
                    render(movie_list, title, li, img, kicker=kicker)
            items.append({"id": iid, "account": "top-movie-reviews", "network": "facebook",
                         "type": "photo", "message": caption, "image_url": img,
                         "when": when, "status": "pending"})
            n += 1
        if (day_idx + 1) % 5 == 0:
            print(f"  ...{day_idx+1}/{DAYS} days built ({n} items so far)")
    save(q)
    print(f"TMR refill: queued {n} items, total {len(items)}")


if __name__ == "__main__":
    build()
