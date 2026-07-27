# -*- coding: utf-8 -*-
"""Top Movie Reviews — Page Growth OS, Week 1 (Aug 1-7). 3 posts/day = 21.

Follows the Step 7 weekly spine: 2 reviews, 2 celeb stories, 2 facts, 2 riddles,
1 quiz, 1 poll, 1 trending, 1 throwback, 1 fan debate + daily engagement post
(Step 4) with the ANSWER withheld and posted the NEXT day.

Rules enforced: original text only, no posters/stills/footage, no invented facts.
Celebrity content is limited to well-documented career facts (no net worth,
no relationship claims). New releases get debate/preview framing, never a
fabricated critique of a film not seen.

Replaces the previous generic amv-* Aug items.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, when, mkdir, render
from image_movie import movie_review, movie_list, movie_take

IMG = mkdir("images/tmr_w1")
F = "\n\n🎬 Top Movie Reviews — one honest verdict a day."

# ---- 15 viral hashtags (rotated; FB caps usefulness, so we use 8-12 per post)
TAGS_REVIEW = "\n\n#MovieReview #FilmTwitter #Cinephile #MustWatch #MovieNight #FilmLovers #WhatToWatch #Cinema #MovieRecommendation #FilmCritic"
TAGS_GAME = "\n\n#GuessTheMovie #MovieQuiz #FilmBuff #MovieTrivia #Cinephile #MovieGame #FilmQuiz #NameThatMovie #MovieLovers #TriviaTime"
TAGS_DEBATE = "\n\n#MovieDebate #FilmTwitter #Cinephile #HotTake #MovieTalk #FilmDiscussion #Cinema #MovieOpinions #FilmLovers #Unpopular Opinion".replace(" Opinion", "Opinion")

# kinds: ("review", title, year, rating, verdict, line, genre, caption)
#        ("list", title, items, kicker, caption)
#        ("take", text, kicker, emoji, caption)
POSTS = [
# ============================ DAY 1 (Aug 1) ============================
("take", "🎬 🌀 🏨 👴 🔫\n\n*Guess the movie.*\n\nNo Googling.", "EMOJI PUZZLE", "🧩",
 "🧩 Five emojis. One modern classic.\n\nIf you get it instantly you've seen it more than once — and you know exactly which scene we mean.\n\nToo easy? Prove it. Too hard? Guess anyway.\n\n👇 Comment your answer.\n\n🔁 Share this with the friend who claims they know every movie." + TAGS_GAME + F),

("review", "Parasite", 2019, 5.0, "MASTERPIECE",
 "Starts as a con-artist comedy, turns into something that leaves a mark. Every frame is doing work — and the class metaphor never once feels like homework.",
 "THRILLER · DRAMA",
 "🎬 PARASITE (2019) — 5/5\n\nA family cons its way into a rich household. That's all you should know going in.\n\nWhat lands: the tonal control. It's genuinely funny for forty minutes, then it turns, and you realise the film has been building the trap the entire time. Song Kang-ho does more with a look than most actors do with a monologue.\n\nThe direction is the star. Bong Jooho stages the two houses like opposing arguments — one all light and staircases, one below the street. You feel the class divide before anyone explains it.\n\nWeakness? The final act asks a lot of you emotionally. Some viewers find the turn too abrupt. We'd argue that's the point.\n\nVerdict: the rare film that swept awards AND deserved it.\n\n👇 Comment: did the ending land for you, or lose you?\n\n🔁 Share this with someone who still avoids subtitles." + TAGS_REVIEW + F),

("take", "The *Jaws* shark barely appears\nbecause the robot kept breaking.\n\nThe malfunction created\nthe suspense. 🦈", "MOVIE FACT", "🎥",
 "🦈 One of cinema's greatest scares was an accident.\n\nThe mechanical shark on Jaws failed constantly in the salt water. Spielberg couldn't show it — so he suggested it instead. A fin. A barrel. That score.\n\nThe result is a masterclass: what you don't see is scarier than what you do. Half of modern horror is still copying a broken prop.\n\nLimitation forced imagination. It usually does.\n\n👇 Comment: what's the scariest thing you never actually saw on screen?\n\n🔁 Share this with a film nerd who'll appreciate it." + TAGS_REVIEW + F),

# ============================ DAY 2 (Aug 2) ============================
("take", "Yesterday's answer:\n\n*THE GRAND BUDAPEST HOTEL* 🏨\n\nToday:\n\n🦇 🃏 🏙️ ⚖️ 🔥", "ANSWER + NEW PUZZLE", "🧩",
 "🧩 Yesterday's emoji puzzle was THE GRAND BUDAPEST HOTEL. If you got it — respect.\n\nToday's is easier. Or is it?\n\nFive emojis, one film that changed its entire genre.\n\n👇 Comment your answer. Reveal tomorrow.\n\n🔁 Share this with someone who'll get it in two seconds." + TAGS_GAME + F),

("take", "He wrote his own breakout film\nbecause nobody would\n*cast* him in one.\n\nThen it won an Oscar. ✍️", "THE STORY", "🎭",
 "🎭 MATT DAMON — the screenplay that built a career.\n\nStruggling to get cast in anything worthwhile, Damon started writing a script as a class assignment at Harvard. He and Ben Affleck kept working on it for years.\n\nThat script became Good Will Hunting. In 1998 the two of them won the Academy Award for Best Original Screenplay — Damon was 27.\n\nWhat followed: the Bourne trilogy redefined the modern action hero, The Martian carried an entire film on one performance, and Ford v Ferrari proved he'd become a genuine character actor. This year he leads Christopher Nolan's The Odyssey.\n\nThe lesson holds up: if the door won't open, build your own.\n\n👇 Comment: what's YOUR favourite Matt Damon performance?\n\n🔁 Share this with someone who needs to hear 'write your own door' today." + TAGS_REVIEW + F),

("take", "I'm a movie where the *hero*\nnever speaks a word\nfor the first 20 minutes —\n\nand a whole planet\nis the villain. 🎬", "MOVIE RIDDLE", "🧠",
 "🧠 MOVIE RIDDLE — medium difficulty.\n\nRead it twice. The clue is in what's missing, not what's there.\n\nMost people guess wrong on the first try. The ones who get it, get it instantly.\n\n👇 Comment your answer. No spoilers for others — just the title.\n\n🔁 Share this with the friend who thinks they're unbeatable at these." + TAGS_GAME + F),

# ============================ DAY 3 (Aug 3) ============================
("take", "Yesterday's answers:\n\nEmoji: *THE DARK KNIGHT* 🃏\nRiddle: *WALL·E* 🤖\n\nToday: name the character —\n\n\"I drink your milkshake.\"", "ANSWER + GUESS WHO", "🎯",
 "🎯 Yesterday: THE DARK KNIGHT and WALL·E. How many did you get?\n\nToday's is a character, not a film. One of the most quoted lines of the century — and one of the great screen monsters.\n\n👇 Comment the character's name (and the film if you know it).\n\n🔁 Share this with someone who quotes movies constantly." + TAGS_GAME + F),

("take", "Nolan's *THE ODYSSEY* has split\neveryone down the middle.\n\nMasterpiece? Or\n*beautiful mess*? 🏛️", "THE DEBATE", "⚔️",
 "⚔️ THE ODYSSEY (2026) — released July 17, and nobody agrees on it.\n\nThe facts: Christopher Nolan directing Homer, roughly $250 million, and a cast most studios couldn't assemble — Matt Damon, Tom Holland, Zendaya, Robert Pattinson, Lupita Nyong'o, Anne Hathaway, Charlize Theron.\n\nThe critics split hard. Variety called it a genuinely grand, gutsy vision. Roger Ebert's site praised its view of human nature. TIME went the other way entirely, calling it underwhelming to look at. Audiences are just as divided — 'masterpiece' and 'violent mess' in the same comment section.\n\nWe're not giving a verdict on a film this fresh. We want yours.\n\n👇 Comment: seen it? Masterpiece or misfire — and why?\n\n🔁 Share this and tag the friend you argued with about it." + TAGS_DEBATE + F),

("take", "*Practical effects* from 1993\nstill look better than\nCGI from last year.\n\nAgree or disagree? 🦖", "THIS OR THAT", "🎥",
 "🦖 Jurassic Park is over thirty years old and the T-rex still looks more real than most of what's released now.\n\nThe argument for practical: it's actually there. Light hits it. Actors react to something physical. It ages like a photograph.\n\nThe argument for CGI: it lets you tell stories you simply couldn't otherwise. Nobody's building a real Middle-earth.\n\nThe honest answer is probably 'the best films use both, invisibly.' But that's a boring comment, so:\n\n👇 Comment: PRACTICAL or CGI — pick a side.\n\n🔁 Share this with someone who has strong opinions about this." + TAGS_DEBATE + F),

# ============================ DAY 4 (Aug 4) ============================
("take", "Yesterday's answer:\n\n*DANIEL PLAINVIEW*\nThere Will Be Blood 🥤\n\nQUIZ TIME —\nswipe your brain into gear 👇", "ANSWER + QUIZ", "🎓",
 "🎓 Yesterday: Daniel Plainview, There Will Be Blood. Day-Lewis at his most terrifying.\n\nTODAY'S QUIZ — 5 questions, answer in the comments:\n\n1. Which film won Best Picture the same year it won Best International Feature?\n2. Who has the most Best Director Oscars ever?\n3. Which actor played both a Marvel and a DC lead?\n4. What's the highest-grossing film that never had a sequel?\n5. Which director has never used a single CGI shot?\n\n👇 Comment your answers 1-5. Score yourself tomorrow.\n\n🔁 Share this with the friend who thinks they'd win a film quiz." + TAGS_GAME + F),

("review", "Mad Max: Fury Road", 2015, 5.0, "RELENTLESS",
 "A two-hour chase that somehow has more character work than films with triple the dialogue. Practical stunts, real dust, real stakes.",
 "ACTION",
 "🎬 MAD MAX: FURY ROAD (2015) — 5/5\n\nA war rig goes one direction, then turns around. That's the plot. It's also perfect.\n\nWhat lands: George Miller shot real vehicles crashing in a real desert, and you can feel it in every frame. Modern action tries to buy that weight with pixels and can't.\n\nThe surprise is the storytelling. Furiosa gets a full arc with maybe forty lines. Max barely speaks. Miller tells you who these people are through what they do under pressure — which is what film is supposed to do.\n\nWeakness: if you need plot complexity, this isn't it. The story is a straight line. The depth is in the execution.\n\nVerdict: the best action film of the last twenty years. It isn't close.\n\n👇 Comment: what's the best action movie ever made — this or something else?\n\n🔁 Share this with someone who still hasn't seen it." + TAGS_REVIEW + F),

("take", "The \"*I know*\" in Empire\nStrikes Back wasn't\nin the script.\n\nHarrison Ford improvised it. ❄️", "MOVIE FACT", "🎥",
 "❄️ The script said 'I love you too.'\n\nHarrison Ford argued it was wrong for Han Solo — the man doesn't say things like that. On the day, he said 'I know' instead. Irvin Kershner kept it.\n\nIt's now one of the most famous lines in film history, and it works precisely because it's not the expected one. Character over sentiment.\n\nThe best improvised lines aren't jokes. They're moments an actor understood better than the page did.\n\n👇 Comment: best improvised movie line you can think of?\n\n🔁 Share this with a Star Wars fan." + TAGS_REVIEW + F),

# ============================ DAY 5 (Aug 5) ============================
("take", "Quiz answers:\n\n1. Parasite  2. John Ford (4)\n3. Ben Affleck  4. Titanic*\n5. Christopher Nolan (mostly)\n\n*New riddle below* 👇", "ANSWER + RIDDLE", "🧠",
 "🎓 How did you score?\n\n(4 is the fun one — Titanic ran for decades without a sequel, which for a film that size is almost unheard of now.)\n\nTODAY'S RIDDLE:\n\nI am a film where the twist is revealed in the first scene — you just don't know you're looking at it. Two men, one city, and a promise that can't be kept.\n\n👇 Comment your answer. Reveal tomorrow.\n\n🔁 Share this with someone who loves a good twist." + TAGS_GAME + F),

("take", "She turned down *three* franchises\nto do smaller films —\n\nand it made her one of\nthe most respected actors alive. 🎭", "THE STORY", "⭐",
 "⭐ LUPITA NYONG'O — the long game.\n\nShe won the Academy Award for Best Supporting Actress for 12 Years a Slave in 2014 — for her first major film role. That almost never happens.\n\nWhat she did next is the interesting part. Instead of cashing it in immediately, she moved between huge films and small ones: motion-capture work in Star Wars, Black Panther, then Jordan Peele's Us — where she played two roles in one film and carried the entire thing.\n\nThis year she appears in Christopher Nolan's The Odyssey.\n\nThe pattern: she picks directors, not paycheques. It's why her filmography holds up.\n\n👇 Comment: Us or Black Panther — which performance hit harder?\n\n🔁 Share this with someone who appreciates real range." + TAGS_REVIEW + F),

("take", "Pick one, forever:\n\nOnly *rewatch* films you love\n\n— or —\n\nOnly watch films\nyou've *never seen* 🎞️", "THE POLL", "🤔",
 "🤔 One or the other. For the rest of your life.\n\nOption A: unlimited rewatches. Your comfort films, forever. But nothing new, ever again.\n\nOption B: everything you watch is new. Constant discovery — but you never see your favourite film again.\n\nMost people say A instantly, then think about it and switch. Some never switch.\n\n👇 Comment A or B — and the one film that made the choice hard.\n\n🔁 Share this and see which one your friends pick." + TAGS_DEBATE + F),

# ============================ DAY 6 (Aug 6) ============================
("take", "Yesterday's answer:\n\n*THE PRESTIGE* 🎩\n\n\"Are you watching closely?\"\n\nToday — finish the line 👇", "ANSWER + FINISH IT", "🎬",
 "🎬 Yesterday: THE PRESTIGE. The whole trick is shown to you in the opening minute.\n\nTODAY — finish these three:\n\n1. \"You either die a hero, or ______\"\n2. \"Why so ______?\"\n3. \"I'm going to make him an offer ______\"\n\nNo Googling. Half the fun is arguing about the exact wording.\n\n👇 Comment your three.\n\n🔁 Share this with someone who quotes films badly." + TAGS_GAME + F),

("take", "In 1999, *six* films came out\nthat each changed cinema.\n\nWe may never get\na year like it again. 📼", "THROWBACK", "🕰️",
 "🕰️ 1999 — the year film broke open.\n\nThe Matrix rewrote action. Fight Club rewired a generation's sense of humour. The Sixth Sense made the twist ending a genre. Being John Malkovich proved weird could be mainstream. Magnolia went for broke. The Blair Witch Project invented modern found footage on almost no money.\n\nOne year. All of them still argued about today.\n\nWhat made it possible: studios were still funding mid-budget films for adults. That's the part we actually lost.\n\n👇 Comment: which 1999 film holds up best?\n\n🔁 Share this with someone who was there for it." + TAGS_REVIEW + F),

("take", "A great film with a *bad* ending\nbeats a mediocre film\nwith a perfect one.\n\nTrue or false? 🎯", "FAN DEBATE", "⚔️",
 "⚔️ Honest question, and people get heated about this one.\n\nThe case for TRUE: you spend two hours in the film and five minutes in the ending. Great characters and craft carry more weight than the landing.\n\nThe case for FALSE: the ending is what you leave with. It rewrites everything before it. A bad one genuinely ruins the rewatch.\n\nThere are famous films on both sides — you're probably already thinking of one.\n\n👇 Comment TRUE or FALSE — and name the film that proves your point.\n\n🔁 Share this and let the comments fight it out." + TAGS_DEBATE + F),

# ============================ DAY 7 (Aug 7) ============================
("take", "Answers:\n\n1. \"...live long enough to see\nyourself become the villain\"\n2. \"...so serious?\"\n3. \"...he can't refuse\" 🎬", "ANSWER REVEAL", "✅",
 "✅ All three: The Dark Knight, The Dark Knight, The Godfather.\n\nIf you got all three without looking — you've earned the film-buff title.\n\nOne more for the weekend: which single movie line do you quote most in real life? Not the most famous one. The one you actually say.\n\n👇 Comment yours.\n\n🔁 Share this with the person you quote movies at constantly." + TAGS_GAME + F),

("list", "5 Films That Are Better the Second Time",
 ["The Prestige", "Parasite", "Arrival", "Fight Club", "Memento"],
 "THE REWATCH LIST",
 "🔁 Some films hide their best work in plain sight.\n\nThese five are built so the second viewing is a different experience — you stop watching the plot and start watching the construction. Every one of them plants the ending in the opening.\n\nSave this for a weekend when you don't want to gamble on something new.\n\n👇 Comment: which film did you understand completely differently the second time?\n\n🔁 Share this with someone who says rewatching is a waste of time." + TAGS_REVIEW + F),

("take", "This week we argued about\nNolan, CGI, and whether\na bad ending ruins a film.\n\n*What should we settle\nnext week?* 🎬", "YOUR CALL", "🗳️",
 "🗳️ End of week one. Thanks to everyone who actually commented — you're the reason this page works.\n\nQuick round-up of where you landed: the practical-vs-CGI thread was the closest fight, and The Odyssey split the room exactly like the critics did.\n\nNow you pick the agenda. What should this page cover next week?\n\n→ A review of a specific film (name it)\n→ A deep dive on one actor or director\n→ More quizzes and riddles\n→ Underrated films nobody talks about\n\n👇 Comment what you want. We'll build next week around the top answers.\n\n🔁 Share this if you want the page to keep going." + TAGS_REVIEW + F),
]

assert len(POSTS) == 21, len(POSTS)
HOURS = [15, 19, 23]  # UTC — US afternoon / EU evening / US prime


def build():
    q = load()
    items = q["items"]
    # Replace the previous generic Aug movie batch
    before = len(items)
    items[:] = [i for i in items
                if not (str(i.get("id", "")).startswith("amv-") and i.get("status") == "pending")]
    print(f"removed {before - len(items)} old pending amv- items")

    have = {i.get("id") for i in items}
    n_img = 0
    for idx, entry in enumerate(POSTS):
        di, pi = divmod(idx, 3)
        iid = f"tmr-w1-d{di+1}-{pi+1}"
        if iid in have:
            continue
        img_path = f"{IMG}/d{di+1}_{pi+1}.png"
        kind = entry[0]
        if kind == "review":
            _, title, year, rating, verdict, line, genre, caption = entry
            render(movie_review, title, year, rating, verdict, line, img_path, genre=genre)
        elif kind == "list":
            _, title, litems, kicker, caption = entry
            render(movie_list, title, litems, img_path, kicker=kicker)
        else:  # take
            _, text, kicker, emoji, caption = entry
            render(movie_take, text, img_path, kicker=kicker, emoji=emoji)
        n_img += 1
        print(f"  rendered {img_path}")
        items.append({"id": iid, "account": "top-movie-reviews", "network": "facebook",
                      "type": "photo", "message": caption, "image_url": img_path,
                      "when": when(di, HOURS[pi]), "status": "pending"})
    save(q)
    print(f"TMR OS WEEK 1: rendered {n_img} images, queue now {len(items)} items")


if __name__ == "__main__":
    build()
