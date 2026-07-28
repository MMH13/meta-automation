# -*- coding: utf-8 -*-
"""Top Movie Reviews — 32 reel scripts for Jul 31 → Aug 15 (2/day).

Deliberate variety, because 32 near-identical reels reads as templated content
to Facebook's unoriginal-content ranking and suppresses the whole set:
  * 6 palette variants rotate
  * 8 distinct formats (fact / misquote / countdown / riddle / year / craft /
    career / debate)
  * lengths run ~20-45s
  * two narrator voices alternate

Every fact here is either long-established film history or checkable; nothing
invented. No studio footage, posters or stills anywhere — original type only.

Schema per reel:
  {"id", "variant", "voice", "caption",
   "frames": [(kind, kwargs, narration), ...]}
kind: hook | beat | title | end
"""

TAGS = ("\n\n#MovieFacts #FilmTwitter #Cinephile #MovieTrivia #FilmLovers "
        "#Cinema #MovieHistory #Filmmaking #WhatToWatch #MovieNight")

V1 = "en-US-AndrewNeural"    # warm conversational
V2 = "en-US-BrianNeural"     # slightly deeper, documentary

REELS = [
# ─────────────────────────── 01 ───────────────────────────
{"id": "r01", "variant": "noir", "voice": V1,
 "caption": "🎬 The most famous line in movie history was improvised on the day.\n\n"
            "The script said \"I love you too.\" Harrison Ford argued Han Solo would never say that. "
            "So he said \"I know\" instead — and it became one of the most quoted moments in film.\n\n"
            "The best improvised lines aren't jokes. They're an actor understanding the character "
            "better than the page did.\n\n"
            "👇 What's the best improvised movie line you can think of?\n\n"
            "🔁 Share this with a Star Wars fan." + TAGS,
 "frames": [
   ("hook", {"text": "THE MOST FAMOUS LINE\nIN MOVIE HISTORY\nWASN'T *IN THE SCRIPT*", "size": 86},
    "The most famous line in movie history was never in the script."),
   ("beat", {"text": "THE PAGE SAID\n\"I LOVE YOU TOO\"", "kicker": "1980", "size": 78},
    "The screenplay said, I love you too."),
   ("beat", {"text": "HARRISON FORD\nSAID *NO*", "size": 88},
    "Harrison Ford refused. He said Han Solo would never talk like that."),
   ("beat", {"text": "SO HE SAID\n*\"I KNOW\"*", "size": 96},
    "So on the day, he said two words instead. I know."),
   ("end", {"text": "IT WORKS BECAUSE\nIT'S THE LINE\nYOU *DON'T EXPECT*",
            "question": "Best *improvised* movie line ever?"},
    "It works because it is the line you don't expect. Character over sentiment. "
    "Forty five years later, we're still quoting it."),
 ]},
# ─────────────────────────── 02 ───────────────────────────
{"id": "r02", "variant": "teal", "voice": V2,
 "caption": "🎥 A studio spent over $150 million on a two-hour car chase with barely any dialogue — "
            "directed by a 70-year-old who also made Happy Feet.\n\n"
            "It should have been a disaster. It won six Academy Awards.\n\n"
            "Mad Max: Fury Road works because the vehicles are real, the desert is real, and the "
            "point of interest sits in the centre of frame so you never lose track of anything.\n\n"
            "👇 Best action film of the century — this or something else?\n\n"
            "🔁 Share this with someone who still hasn't seen it." + TAGS,
 "frames": [
   ("hook", {"text": "A TWO-HOUR CAR CHASE\nWITH ALMOST\n*NO DIALOGUE*", "size": 88},
    "A studio spent over a hundred and fifty million dollars on a two hour car chase with almost no dialogue."),
   ("beat", {"text": "DIRECTED BY A\n*70-YEAR-OLD*", "kicker": "GEORGE MILLER", "size": 84},
    "It was directed by a seventy year old man who also made Happy Feet."),
   ("beat", {"text": "IT WON\n*SIX OSCARS*", "size": 96},
    "It won six Academy Awards."),
   ("beat", {"text": "BECAUSE THE CRASHES\nWERE *REAL*", "size": 86},
    "Because when something crashed, something actually crashed. Real vehicles, real desert, real stunt performers."),
   ("end", {"text": "EVERY ACTION FILM SINCE\nHAS BEEN TRYING\nTO *COPY IT*",
            "question": "Best *action film* of the century?"},
    "Every action director since has been trying to copy it. Almost none have understood that the secret "
    "isn't the crashes. It's the clarity."),
 ]},
# ─────────────────────────── 03 ───────────────────────────
{"id": "r03", "variant": "crimson", "voice": V1,
 "caption": "🎙️ Three of the most quoted lines in history — and none of them were ever said.\n\n"
            "\"Luke, I am your father.\" He never says Luke.\n"
            "\"Play it again, Sam.\" Nobody says it in Casablanca.\n"
            "\"Elementary, my dear Watson.\" Not in a single original Conan Doyle story.\n\n"
            "👇 Which one did YOU believe?\n\n"
            "🔁 Share this and watch someone argue with you." + TAGS,
 "frames": [
   ("hook", {"text": "YOU'VE BEEN QUOTING\nTHESE MOVIES *WRONG*\nYOUR WHOLE LIFE", "size": 86},
    "You have been quoting these movies wrong your whole life."),
   ("beat", {"text": "\"LUKE, I AM\nYOUR FATHER\"\n\nHE NEVER SAYS\n*LUKE*", "kicker": "MISQUOTE 01", "size": 62},
    "Luke, I am your father. He never says Luke. The actual line is, No — I am your father."),
   ("beat", {"text": "\"PLAY IT AGAIN,\nSAM\"\n\n*NOBODY* SAYS THIS", "kicker": "MISQUOTE 02", "size": 64},
    "Play it again, Sam. Nobody says that in Casablanca. Not once."),
   ("beat", {"text": "\"ELEMENTARY,\nMY DEAR WATSON\"\n\n*NOT IN ANY*\nORIGINAL STORY", "kicker": "MISQUOTE 03", "size": 58},
    "Elementary, my dear Watson. Not in a single one of Conan Doyle's original stories."),
   ("end", {"text": "THREE FAMOUS LINES.\n*NONE OF THEM REAL.*",
            "question": "Which one did *you* believe?"},
    "Three of the most quoted lines in history, and none of them were ever actually said."),
 ]},
# ─────────────────────────── 04 ───────────────────────────
{"id": "r04", "variant": "indigo", "voice": V2,
 "caption": "📼 1999 — the year film broke open.\n\nSix films in twelve months, each one permanently "
            "changing what movies could be. We've never had another year like it.\n\n"
            "The reason? Studios were still funding mid-budget films for adults. That's the part we lost.\n\n"
            "👇 Which 1999 film holds up best?\n\n🔁 Share this with someone who was there for it." + TAGS,
 "frames": [
   ("hook", {"text": "SIX FILMS.\n*ONE YEAR.*\nALL SIX CHANGED\nMOVIES FOREVER", "size": 84},
    "Six films came out in one year, and all six changed movies forever."),
   ("title", {"top": "1999", "big": "THE MATRIX", "bottom": "rewrote *action* forever"},
    "The Matrix rewrote what an action film could look like."),
   ("title", {"top": "1999", "big": "FIGHT CLUB", "bottom": "rewired a *generation*"},
    "Fight Club rewired a generation's sense of humour."),
   ("title", {"top": "1999", "big": "THE SIXTH SENSE", "bottom": "made the *twist* a genre"},
    "The Sixth Sense turned the twist ending into its own genre."),
   ("title", {"top": "1999", "big": "THE BLAIR WITCH PROJECT", "bottom": "invented *found footage*"},
    "And The Blair Witch Project invented modern found footage on almost no money."),
   ("end", {"text": "ONE YEAR.\nWE NEVER GOT\n*ANOTHER LIKE IT.*",
            "question": "Which *1999* film holds up best?"},
    "One year. And we never got another like it. Because studios were still funding "
    "mid budget films for adults."),
 ]},
# ─────────────────────────── 05 ───────────────────────────
{"id": "r05", "variant": "violet", "voice": V1,
 "caption": "🏆 Parasite didn't just win Best Picture — it became the first film not in the English "
            "language to ever do it, in 92 years of the Academy Awards.\n\n"
            "Made for about $11 million. Earned around $257 million. Won four Oscars including "
            "Director and Original Screenplay.\n\n"
            "👇 Did the ending land for you — or lose you?\n\n"
            "🔁 Share this with someone who still avoids subtitles." + TAGS,
 "frames": [
   ("hook", {"text": "IT TOOK THE OSCARS\n*92 YEARS*\nTO DO THIS", "size": 92},
    "It took the Academy Awards ninety two years to do this."),
   ("beat", {"text": "A FILM NOT IN\n*ENGLISH*\nWON BEST PICTURE", "kicker": "2020", "size": 78},
    "A film not in the English language finally won Best Picture."),
   ("title", {"top": "BONG JOON-HO", "big": "PARASITE", "bottom": "made for *$11 million*"},
    "Parasite. Made for about eleven million dollars."),
   ("beat", {"text": "IT EARNED\n*$257 MILLION*", "size": 92},
    "It earned around two hundred and fifty seven million worldwide. More than twenty times its cost."),
   ("end", {"text": "FOUR OSCARS.\nINCLUDING *DIRECTOR*\nAND *SCREENPLAY*",
            "question": "Did the ending *land* for you?"},
    "Four Academy Awards, including Best Director and Best Original Screenplay. "
    "The rare film that swept everything and deserved it."),
 ]},
# ─────────────────────────── 06 ───────────────────────────
{"id": "r06", "variant": "noir", "voice": V2,
 "caption": "🧠 Five movie riddles. Most people get two.\n\nNo Googling — that's the whole point.\n\n"
            "👇 Comment how many you got. Answers tomorrow.\n\n"
            "🔁 Share this with the friend who thinks they're unbeatable at these." + TAGS,
 "frames": [
   ("hook", {"text": "FIVE MOVIE RIDDLES.\nMOST PEOPLE\nGET *TWO*.", "size": 90},
    "Five movie riddles. Most people only get two. No Googling."),
   ("beat", {"text": "A HERO WHO NEVER\nSPEAKS FOR *20 MINUTES*\n— AND A PLANET\nAS THE VILLAIN", "kicker": "RIDDLE 01", "size": 56},
    "One. A hero who never speaks for twenty minutes, and a whole planet as the villain."),
   ("beat", {"text": "TWO MAGICIANS\nDESTROY EACH OTHER\nOVER A TRICK YOU'RE\n*SHOWN* IN MINUTE ONE", "kicker": "RIDDLE 02", "size": 54},
    "Two. Two magicians destroy each other over a trick you are shown in the first minute."),
   ("beat", {"text": "ALIENS ARRIVE —\nAND THE WEAPON\nTURNS OUT TO BE\n*GRAMMAR*", "kicker": "RIDDLE 03", "size": 58},
    "Three. Aliens arrive, and the weapon turns out to be grammar."),
   ("beat", {"text": "A GIRL WORKS IN A\nBATHHOUSE *FOR SPIRITS*\nTO WIN BACK\nHER PARENTS", "kicker": "RIDDLE 04", "size": 56},
    "Four. A girl works in a bathhouse for spirits to win back her parents."),
   ("end", {"text": "HOW MANY\nDID YOU *GET*?",
            "question": "Comment your score.\n*Answers tomorrow.*"},
    "How many did you get? Comment your score below, and I'll post the answers tomorrow."),
 ]},
]
