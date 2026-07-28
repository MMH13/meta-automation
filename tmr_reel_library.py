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
# ─────────────────────────── 07 ───────────────────────────
{"id": "r07", "variant": "teal", "voice": V1,
 "caption": "🦈 The greatest movie monster is the one you never see.\n\nSpielberg's mechanical shark "
            "kept failing in the salt water — so he hid it. A fin. A barrel. Sometimes nothing at all.\n\n"
            "Half of modern horror is still copying a broken prop.\n\n"
            "👇 What's the scariest thing you never actually SAW on screen?\n\n"
            "🔁 Share this with a film nerd." + TAGS,
 "frames": [
   ("hook", {"text": "THE SCARIEST SHARK\nIN MOVIE HISTORY\n*BARELY APPEARS*", "size": 88},
    "The scariest shark in movie history barely appears on screen."),
   ("beat", {"text": "THE MECHANICAL SHARK\n*KEPT BREAKING*", "kicker": "1975", "size": 82},
    "Spielberg had a full size mechanical shark. In salt water, it failed almost every day."),
   ("beat", {"text": "SO HE *STOPPED*\nSHOWING IT", "size": 92},
    "So he stopped showing it."),
   ("beat", {"text": "A FIN.\nA BARREL.\n*NOTHING AT ALL.*", "size": 86},
    "A fin. A barrel. Sometimes nothing at all. Just the water, and that score."),
   ("end", {"text": "YOUR IMAGINATION\nDID THE REST —\nAND DID IT *BETTER*",
            "question": "Scariest thing you *never saw*?"},
    "Your imagination filled in something far worse than any rubber shark could have been. "
    "Fifty years later, horror is still copying a broken prop."),
 ]},
# ─────────────────────────── 08 ───────────────────────────
{"id": "r08", "variant": "amberlow", "voice": V2,
 "caption": "🐈 One of the most famous images in film history was an accident.\n\nMarlon Brando found "
            "a stray cat wandering the set of The Godfather and put it in his lap mid-scene. It wasn't "
            "scripted. It purred so loudly the dialogue was nearly unusable.\n\n"
            "It stayed in — because it made a man ordering violence look like someone's gentle grandfather.\n\n"
            "👇 What's your favourite happy accident in film?\n\n🔁 Share with a Godfather fan." + TAGS,
 "frames": [
   ("hook", {"text": "THE CAT IN\n*THE GODFATHER*\nWASN'T IN THE SCRIPT", "size": 84},
    "The cat in The Godfather was never in the script."),
   ("beat", {"text": "BRANDO FOUND A\n*STRAY* ON SET", "size": 88},
    "Marlon Brando found a stray wandering the studio and simply put it in his lap."),
   ("beat", {"text": "IT PURRED SO LOUD\nTHE DIALOGUE WAS\n*ALMOST UNUSABLE*", "size": 68},
    "It purred so loudly the sound team could barely hear his lines."),
   ("beat", {"text": "THEY *KEPT IT*\nANYWAY", "size": 96},
    "They kept it anyway."),
   ("end", {"text": "A MAN ORDERING MURDER,\nGENTLY STROKING\nA *STRAY CAT*",
            "question": "Favourite *happy accident* in film?"},
    "Because a man calmly ordering violence while stroking a stray cat tells you everything "
    "about him, and nobody had to write a single line of it."),
 ]},
# ─────────────────────────── 09 ───────────────────────────
{"id": "r09", "variant": "indigo", "voice": V1,
 "caption": "🦖 A dinosaur from 1993 still looks more real than most CGI made last year.\n\n"
            "Jurassic Park used full-size animatronics for close-ups and CGI only where it had to. "
            "Real light hit real objects — and actors reacted to something physically there.\n\n"
            "👇 Name a film whose effects STILL hold up.\n\n🔁 Share with someone who says old films look dated." + TAGS,
 "frames": [
   ("hook", {"text": "A 1993 DINOSAUR\nSTILL LOOKS BETTER\nTHAN *LAST YEAR'S CGI*", "size": 78},
    "A dinosaur from nineteen ninety three still looks more real than most computer effects made last year."),
   ("beat", {"text": "BECAUSE IT WAS\n*ACTUALLY THERE*", "size": 92},
    "Because a lot of it was actually there. A full size animatronic, on set, in the rain."),
   ("beat", {"text": "REAL LIGHT HIT\nA REAL *OBJECT*", "size": 88},
    "Real light hit a real object. That is extremely hard to fake, even now."),
   ("beat", {"text": "AND THE ACTORS\nWERE REACTING TO\n*SOMETHING REAL*", "size": 70},
    "And the actors were reacting to something genuinely in front of them, not a tennis ball on a stick."),
   ("end", {"text": "CGI ISN'T THE PROBLEM.\n*REPLACING EVERYTHING*\nWITH IT IS.",
            "question": "Which film's effects *still hold up*?"},
    "CGI isn't the problem. Replacing everything with it is. The best films still use both, invisibly."),
 ]},
# ─────────────────────────── 10 ───────────────────────────
{"id": "r10", "variant": "noir", "voice": V2,
 "caption": "🚿 The most famous murder scene in cinema shows no blade touching skin — and the blood "
            "was chocolate syrup.\n\nHitchcock shot the Psycho shower scene across dozens of setups over "
            "days, for around 45 seconds of screen time. Black and white made the syrup read perfectly.\n\n"
            "👇 Scariest scene that shows almost nothing?\n\n🔁 Share with a horror fan." + TAGS,
 "frames": [
   ("hook", {"text": "CINEMA'S MOST FAMOUS\nMURDER SCENE SHOWS\n*NO KNIFE TOUCHING SKIN*", "size": 68},
    "The most famous murder scene in cinema never shows the knife touching skin."),
   ("beat", {"text": "*45 SECONDS*\nON SCREEN", "kicker": "PSYCHO · 1960", "size": 92},
    "Psycho, nineteen sixty. Around forty five seconds on screen."),
   ("beat", {"text": "SHOT ACROSS\n*DOZENS* OF SETUPS", "size": 84},
    "Hitchcock shot it across dozens of camera setups over several days."),
   ("beat", {"text": "THE BLOOD WAS\n*CHOCOLATE SYRUP*", "size": 84},
    "And the blood was chocolate syrup. In black and white, it read better than the real thing."),
   ("end", {"text": "THE EDIT DOES\nTHE VIOLENCE.\nYOUR MIND *FILLS IT IN.*",
            "question": "Scariest scene that shows *almost nothing*?"},
    "The editing does the violence. Your mind fills in the rest. It's still being copied sixty five years later."),
 ]},
# ─────────────────────────── 11 ───────────────────────────
{"id": "r11", "variant": "crimson", "voice": V1,
 "caption": "🚪 No budget? No problem. These films trap you in one place and never let go.\n\n"
            "12 Angry Men · Rear Window · Buried · The Man From Earth · Locke\n\n"
            "One location forces the writing to carry everything — which is exactly why these hold up.\n\n"
            "👇 Best single-location film you've seen?\n\n🔁 Save this for a night in." + TAGS,
 "frames": [
   ("hook", {"text": "FIVE FILMS SET\nIN *ONE ROOM*\n— AND THEY'RE BETTER\nFOR IT", "size": 76},
    "Five films set almost entirely in one location, and they're better for it."),
   ("title", {"top": "1957", "big": "12 ANGRY MEN", "bottom": "one room. *twelve men.* one verdict"},
    "Twelve Angry Men. One room, twelve men, one verdict."),
   ("title", {"top": "1954", "big": "REAR WINDOW", "bottom": "one *window*. one wheelchair"},
    "Rear Window. One apartment, one window, one wheelchair."),
   ("title", {"top": "2013", "big": "LOCKE", "bottom": "one *car*. one phone. 85 minutes"},
    "Locke. One man, one car, one drive, eighty five minutes."),
   ("end", {"text": "NO SPECTACLE.\nJUST *WRITING*\nAND A CAMERA.",
            "question": "Best *single-location* film?"},
    "No spectacle. Just writing and a camera. When you can't cut away, the script has to be perfect."),
 ]},
# ─────────────────────────── 12 ───────────────────────────
{"id": "r12", "variant": "violet", "voice": V2,
 "caption": "🧠 Round two. Five more movie riddles — these are harder.\n\n👇 Comment how many you got.\n\n"
            "🔁 Share this with someone who got them all last time." + TAGS,
 "frames": [
   ("hook", {"text": "ROUND TWO.\nTHESE ARE *HARDER*.", "size": 96},
    "Round two. Five more movie riddles, and these are harder."),
   ("beat", {"text": "A MAN IMPRISONED\n*15 YEARS* — AND THE\nREASON IS WORSE\nTHAN THE SENTENCE", "kicker": "RIDDLE 01", "size": 54},
    "One. A man is imprisoned for fifteen years, and the reason is worse than the sentence."),
   ("beat", {"text": "A CITY WHERE NO CHILD\nHAS BEEN BORN\nIN *EIGHTEEN YEARS*", "kicker": "RIDDLE 02", "size": 58},
    "Two. A world where no child has been born in eighteen years."),
   ("beat", {"text": "A DANCER'S PERFECTION\nCOSTS HER THE ABILITY\nTO TELL WHAT'S *REAL*", "kicker": "RIDDLE 03", "size": 56},
    "Three. A dancer's pursuit of perfection costs her the ability to tell what is real."),
   ("beat", {"text": "TWO DETECTIVES.\n*SEVEN SINS.*\nONE BOX.", "kicker": "RIDDLE 04", "size": 72},
    "Four. Two detectives, seven sins, and a box nobody should open."),
   ("end", {"text": "SCORE YOURSELF.\n*BE HONEST.*",
            "question": "How many? *Answers tomorrow.*"},
    "Score yourself, and be honest. Comment below. Answers tomorrow."),
 ]},
# ─────────────────────────── 13 ───────────────────────────
{"id": "r13", "variant": "amberlow", "voice": V1,
 "caption": "🎬 Some of the most famous roles in film were turned down first.\n\nThat's not trivia — it's "
            "a reminder that the 'perfect' casting we can't imagine any other way was usually somebody's "
            "second or third choice.\n\n👇 Which recast would have ruined the film?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "THE ROLES YOU CAN'T\nIMAGINE ANYONE ELSE IN\nWERE *TURNED DOWN FIRST*", "size": 68},
    "The roles you can't imagine anyone else playing were usually turned down by somebody first."),
   ("beat", {"text": "CASTING ISN'T\n*DESTINY*", "size": 96},
    "Casting isn't destiny. It's a series of accidents that later look inevitable."),
   ("beat", {"text": "THE 'PERFECT' ACTOR\nWAS OFTEN THE\n*THIRD CHOICE*", "size": 72},
    "The actor who now seems perfect was often the third or fourth choice."),
   ("beat", {"text": "WHICH MEANS THE FILM\nYOU LOVE ALMOST\n*DIDN'T EXIST*", "size": 68},
    "Which means the version of the film you love almost didn't exist at all."),
   ("end", {"text": "SOME PERFORMANCES\nARE SO RIGHT THEY\n*ERASE THE ALTERNATIVES*",
            "question": "Which recast would have *ruined* it?"},
    "Some performances are so right they erase every alternative from your imagination. "
    "Which one would you never recast?"),
 ]},
# ─────────────────────────── 14 ───────────────────────────
{"id": "r14", "variant": "teal", "voice": V2,
 "caption": "⏱️ Not every great film needs three hours.\n\nWhiplash · Run Lola Run · Before Sunset · "
            "12 Angry Men · Toy Story\n\nAll under 100 minutes. All better for it. Constraint is not "
            "the enemy of ambition.\n\n👇 Best film under 100 minutes?\n\n🔁 Save this for a short evening." + TAGS,
 "frames": [
   ("hook", {"text": "GREAT FILMS THAT\nRESPECT YOUR TIME\n— ALL UNDER *100 MINUTES*", "size": 72},
    "Great films that respect your time. All of these run under a hundred minutes."),
   ("title", {"top": "106 MIN", "big": "WHIPLASH", "bottom": "never lets you *breathe*"},
    "Whiplash. It never lets you breathe."),
   ("title", {"top": "80 MIN", "big": "RUN LOLA RUN", "bottom": "*three* versions of one run"},
    "Run Lola Run. Three versions of the same twenty minutes."),
   ("title", {"top": "96 MIN", "big": "12 ANGRY MEN", "bottom": "one room, *zero* wasted lines"},
    "Twelve Angry Men. One room, and not one wasted line."),
   ("end", {"text": "LENGTH ISN'T\nAMBITION.\n*CONTROL IS.*",
            "question": "Best film *under 100 minutes*?"},
    "Length isn't ambition. Control is. A tight film is much harder to make than a long one."),
 ]},
# ─────────────────────────── 15 ───────────────────────────
{"id": "r15", "variant": "noir", "voice": V1,
 "caption": "🎭 A great villain is why you remember the film.\n\nThe weak version wants to 'watch the "
            "world burn.' The great version has a point you almost agree with — and that's what makes "
            "them frightening.\n\n👇 Greatest movie villain of all time?\n\n🔁 Share and start the argument." + TAGS,
 "frames": [
   ("hook", {"text": "HEROES GET THE POSTER.\n*VILLAINS* GET\nREMEMBERED.", "size": 82},
    "Heroes get the poster. Villains get remembered."),
   ("beat", {"text": "A WEAK VILLAIN\nJUST WANTS *CHAOS*", "size": 88},
    "A weak villain just wants chaos. There's nothing to think about."),
   ("beat", {"text": "A GREAT ONE HAS\nA POINT YOU\n*ALMOST AGREE WITH*", "size": 70},
    "A great one has a point you almost agree with. That's the uncomfortable part."),
   ("beat", {"text": "THAT DISCOMFORT\nIS THE *WHOLE JOB*", "size": 80},
    "That discomfort is the entire job. If you never waver, the film isn't working."),
   ("end", {"text": "A WEAK VILLAIN MAKES\nEVEN A GREAT HERO\n*FORGETTABLE*",
            "question": "Greatest movie *villain* ever?"},
    "A weak villain makes even a great hero forgettable. So who's the best ever? Make your case."),
 ]},
# ─────────────────────────── 16 ───────────────────────────
{"id": "r16", "variant": "indigo", "voice": V2,
 "caption": "🔁 Some films are built to be watched twice.\n\nThe Prestige · Parasite · Arrival · "
            "Fight Club · Memento\n\nEvery one of them plants the ending in the opening. The second "
            "viewing is a different film.\n\n👇 Which film did you understand completely differently "
            "the second time?\n\n🔁 Save this." + TAGS,
 "frames": [
   ("hook", {"text": "SOME FILMS HIDE\nTHEIR BEST WORK\n*IN PLAIN SIGHT*", "size": 84},
    "Some films hide their best work in plain sight."),
   ("beat", {"text": "THEY PLANT THE ENDING\nIN THE *OPENING*", "size": 80},
    "They plant the ending in the opening minute, and you don't notice."),
   ("title", {"top": "REWATCH", "big": "THE PRESTIGE", "bottom": "\"are you *watching closely?*\""},
    "The Prestige literally asks you. Are you watching closely?"),
   ("title", {"top": "REWATCH", "big": "ARRIVAL", "bottom": "the first scene is the *last* one"},
    "Arrival. The first scene is also the last one. You just don't know it yet."),
   ("end", {"text": "THE SECOND WATCH\nISN'T A REPEAT.\nIT'S A *DIFFERENT FILM.*",
            "question": "Which one changed on *rewatch*?"},
    "The second viewing isn't a repeat. You stop watching the plot and start watching the construction."),
 ]},
# ─────────────────────────── 17 ───────────────────────────
{"id": "r17", "variant": "crimson", "voice": V1,
 "caption": "💸 Some of the most loved films in history flopped on release.\n\nThe Shawshank Redemption "
            "barely made its budget back in cinemas. Blade Runner was a commercial disappointment. "
            "It's a Wonderful Life lost money.\n\nAll three are now considered classics.\n\n"
            "👇 What's a film you loved that nobody watched?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "SOME OF THE GREATEST\nFILMS EVER MADE\n*FLOPPED*", "size": 84},
    "Some of the greatest films ever made were flops when they came out."),
   ("title", {"top": "1994", "big": "SHAWSHANK", "bottom": "barely made its money back"},
    "The Shawshank Redemption barely made its budget back in cinemas."),
   ("title", {"top": "1982", "big": "BLADE RUNNER", "bottom": "a commercial *disappointment*"},
    "Blade Runner was a commercial disappointment on release."),
   ("title", {"top": "1946", "big": "IT'S A WONDERFUL LIFE", "bottom": "*lost money* on release"},
    "It's a Wonderful Life lost money, and only became a classic decades later on television."),
   ("end", {"text": "BOX OFFICE MEASURES\nA *WEEKEND*.\nNOT A FILM.",
            "question": "A film *you* loved that nobody watched?"},
    "Box office measures a weekend. It doesn't measure a film. Time does."),
 ]},
# ─────────────────────────── 18 ───────────────────────────
{"id": "r18", "variant": "violet", "voice": V2,
 "caption": "🎵 You remember the themes. Star Wars. Jaws. The Godfather. Interstellar.\n\nA great score "
            "doesn't decorate the scene — it tells you how to feel about it before anyone speaks.\n\n"
            "👇 Best movie score ever written?\n\n🔁 Share with someone who still plays film music." + TAGS,
 "frames": [
   ("hook", {"text": "YOU CAN HUM THEM\nWITHOUT REMEMBERING\n*A SINGLE LINE*", "size": 76},
    "You can hum these without remembering a single line of dialogue."),
   ("beat", {"text": "A SCORE DOESN'T\n*DECORATE* A SCENE", "size": 84},
    "A great score doesn't decorate a scene."),
   ("beat", {"text": "IT TELLS YOU HOW\nTO *FEEL* — BEFORE\nANYONE SPEAKS", "size": 70},
    "It tells you how to feel about what you're seeing, before anyone says a word."),
   ("beat", {"text": "TWO NOTES.\nAND YOU KNOW\n*SOMETHING'S COMING.*", "size": 72},
    "Two notes, and you already know something is coming. That's not music. That's storytelling."),
   ("end", {"text": "THE BEST SCORES\nOUTLIVE THE FILMS\nTHEY WERE *WRITTEN FOR*",
            "question": "Best *movie score* ever written?"},
    "The best scores outlive the films they were written for. Which one is the greatest?"),
 ]},
# ─────────────────────────── 19 ───────────────────────────
{"id": "r19", "variant": "teal", "voice": V1,
 "caption": "🎯 An ending can save a film — or ruin one.\n\nA cheap twist hides information from you. "
            "A great twist shows you everything and trusts you to miss it. That's the entire difference.\n\n"
            "👇 Best ending ever written?\n\n🔁 Share this and argue about it." + TAGS,
 "frames": [
   ("hook", {"text": "A CHEAP TWIST\n*HIDES* INFORMATION\nFROM YOU", "size": 82},
    "A cheap twist hides information from you."),
   ("beat", {"text": "A GREAT TWIST\nSHOWS YOU\n*EVERYTHING*", "size": 88},
    "A great twist shows you everything."),
   ("beat", {"text": "AND TRUSTS YOU\nTO *MISS IT*", "size": 92},
    "And then trusts you to miss it."),
   ("beat", {"text": "ONE MAKES YOU FEEL\nCHEATED. THE OTHER\nMAKES YOU *REWATCH*", "size": 66},
    "One makes you feel cheated. The other makes you start the film again immediately."),
   ("end", {"text": "THAT'S THE WHOLE\n*DIFFERENCE*",
            "question": "Best *ending* ever written?"},
    "That's the whole difference. And it's why some endings are still argued about decades later."),
 ]},
# ─────────────────────────── 20 ───────────────────────────
{"id": "r20", "variant": "noir", "voice": V2,
 "caption": "🧠 Round three. Five riddles — these are the hard ones.\n\n👇 Comment your score.\n\n"
            "🔁 Share with someone who claims they're unbeatable." + TAGS,
 "frames": [
   ("hook", {"text": "ROUND THREE.\nTHE *HARD* ONES.", "size": 98},
    "Round three. These are the hard ones."),
   ("beat", {"text": "TWO MEN IN LOVE\nFOR ONE SUMMER —\n*PAINTED*, NOT SPOKEN", "kicker": "RIDDLE 01", "size": 56},
    "One. Two people fall in love over one summer, and it's painted rather than spoken."),
   ("beat", {"text": "A THIEF STEALS *IDEAS*\nAND CAN'T TELL IF\nHE EVER CAME HOME", "kicker": "RIDDLE 02", "size": 56},
    "Two. A thief steals ideas, and can't tell whether he ever came home."),
   ("beat", {"text": "A DRUMMER *BLEEDS*\nFOR A TEACHER WHO MAY\nBE GENIUS OR MONSTER", "kicker": "RIDDLE 03", "size": 54},
    "Three. A drummer bleeds for a teacher who is either a genius or a monster."),
   ("beat", {"text": "A KING'S SON RUNS\nFROM A *LIE*\nHIS UNCLE TOLD HIM", "kicker": "RIDDLE 04", "size": 58},
    "Four. A king's son runs away from a lie his uncle told him."),
   ("end", {"text": "FOUR OUT OF FOUR?\n*PROVE IT.*",
            "question": "Comment your score.\n*Answers tomorrow.*"},
    "Four out of four? Prove it in the comments. Answers tomorrow."),
 ]},
# ─────────────────────────── 21 ───────────────────────────
{"id": "r21", "variant": "amberlow", "voice": V1,
 "caption": "🌍 \"I don't watch films with subtitles\" is the most expensive sentence in film.\n\n"
            "Parasite. Spirited Away. Oldboy. City of God. Amélie. Seven Samurai.\n\nOne inch of text "
            "at the bottom of the screen is all that stands between you and those.\n\n"
            "👇 Best non-English film you've seen?\n\n🔁 Share with someone who needs to hear it." + TAGS,
 "frames": [
   ("hook", {"text": "\"I DON'T DO SUBTITLES\"\nIS THE MOST *EXPENSIVE*\nSENTENCE IN FILM", "size": 68},
    "I don't watch films with subtitles is the most expensive sentence in film."),
   ("beat", {"text": "IT COSTS YOU\n*MOST OF CINEMA*", "size": 92},
    "It costs you most of cinema. Not a corner of it. Most of it."),
   ("title", {"top": "START HERE", "big": "PARASITE", "bottom": "a thriller that *moves fast*"},
    "Start with Parasite. It's a thriller. It moves fast. You'll forget you're reading."),
   ("title", {"top": "THEN", "big": "SPIRITED AWAY", "bottom": "works at *any age*"},
    "Then Spirited Away, which works at any age."),
   ("end", {"text": "TEN MINUTES IN,\nYOU FORGET\nYOU'RE *READING*",
            "question": "Best *non-English* film you've seen?"},
    "Ten minutes in, you stop noticing the subtitles entirely. That's the whole barrier. Ten minutes."),
 ]},
# ─────────────────────────── 22 ───────────────────────────
{"id": "r22", "variant": "indigo", "voice": V2,
 "caption": "🎥 The hardest shot in filmmaking is the one with no cut.\n\nA long take means every actor, "
            "every mark, every light and every camera move has to be perfect at the same time. One "
            "mistake at minute four and you start again.\n\n👇 Best long take you've seen?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "THE HARDEST SHOT\nIN FILMMAKING IS THE\nONE WITH *NO CUT*", "size": 76},
    "The hardest shot in filmmaking is the one with no cut."),
   ("beat", {"text": "EVERY ACTOR.\nEVERY LIGHT.\nEVERY *MARK*.", "size": 84},
    "Every actor, every light, every camera move, every mark on the floor."),
   ("beat", {"text": "ALL PERFECT\n*AT THE SAME TIME*", "size": 88},
    "All of it has to be perfect at the same time."),
   ("beat", {"text": "ONE MISTAKE AT\nMINUTE FOUR —\n*START AGAIN*", "size": 76},
    "One mistake at minute four, and everybody goes back to the beginning."),
   ("end", {"text": "WHEN IT WORKS,\nYOU FEEL LIKE YOU'RE\n*IN THE ROOM*",
            "question": "Best *long take* you've seen?"},
    "And when it works, you stop feeling like you're watching a film and start feeling like "
    "you're in the room."),
 ]},
# ─────────────────────────── 23 ───────────────────────────
{"id": "r23", "variant": "crimson", "voice": V1,
 "caption": "📖 \"The book was better\" — not always.\n\nSome adaptations cut what didn't work, sharpened "
            "what did, and gave the story a shape the novel never had.\n\n👇 Name a film that beat the book.\n\n"
            "🔁 Share this with a reader who'll disagree." + TAGS,
 "frames": [
   ("hook", {"text": "\"THE BOOK WAS BETTER\"\n— *NOT ALWAYS*", "size": 92},
    "The book was better. It's almost a reflex. And it isn't always true."),
   ("beat", {"text": "A NOVEL CAN\n*WANDER*", "size": 96},
    "A novel can wander. It has four hundred pages to fill."),
   ("beat", {"text": "A FILM HAS\n*TWO HOURS*", "size": 96},
    "A film has two hours. Every scene has to earn its place."),
   ("beat", {"text": "SOMETIMES THAT\nPRESSURE MAKES IT\n*SHARPER*", "size": 76},
    "Sometimes that pressure makes the story sharper than the book ever was."),
   ("end", {"text": "CUTTING ISN'T\nLOSING. IT'S\n*CHOOSING.*",
            "question": "Name a film that *beat the book*."},
    "Cutting isn't losing. It's choosing. Name a film that genuinely beat the book."),
 ]},
# ─────────────────────────── 24 ───────────────────────────
{"id": "r24", "variant": "violet", "voice": V2,
 "caption": "🍿 Everyone has one. The film you've seen so many times you don't watch it any more — "
            "you just have it on.\n\nThere's no shame in it. A comfort film is doing a real job.\n\n"
            "👇 What's yours?\n\n🔁 Share and see if your friends have the same one." + TAGS,
 "frames": [
   ("hook", {"text": "THE FILM YOU'VE SEEN\nSO MANY TIMES YOU\n*DON'T WATCH IT ANY MORE*", "size": 66},
    "Everyone has the film they've seen so many times they don't really watch it any more."),
   ("beat", {"text": "YOU JUST\n*HAVE IT ON*", "size": 100},
    "You just have it on."),
   ("beat", {"text": "AND IT MAKES THE\nROOM FEEL *BETTER*", "size": 84},
    "And somehow the room feels better for it."),
   ("beat", {"text": "THAT'S NOT LAZY.\nTHAT'S THE FILM\n*DOING ITS JOB*", "size": 72},
    "That isn't laziness. That's the film doing a real job."),
   ("end", {"text": "REWATCHING SOMETHING\nYOU LOVE ISN'T\n*WASTING* A NIGHT",
            "question": "What's *your* comfort film?"},
    "Rewatching something you love is never wasting a night. So what's yours?"),
 ]},
# ─────────────────────────── 25 ───────────────────────────
{"id": "r25", "variant": "teal", "voice": V1,
 "caption": "🎬 A great opening scene does three jobs in five minutes: tells you the rules, tells you "
            "the tone, and makes you need the next scene.\n\nMost films only manage one.\n\n"
            "👇 Best opening scene in film?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "YOU HAVE *FIVE MINUTES*\nTO HOOK AN AUDIENCE", "size": 84},
    "A film has about five minutes to hook you."),
   ("beat", {"text": "JOB ONE:\nTELL ME THE *RULES*", "size": 88},
    "Job one. Tell me the rules of this world."),
   ("beat", {"text": "JOB TWO:\nTELL ME THE *TONE*", "size": 88},
    "Job two. Tell me the tone, so I know how to feel."),
   ("beat", {"text": "JOB THREE:\nMAKE ME *NEED*\nTHE NEXT SCENE", "size": 78},
    "Job three. Make me need the next scene."),
   ("end", {"text": "MOST FILMS\nMANAGE *ONE*.",
            "question": "Best *opening scene* in film?"},
    "Most films manage one of the three. The great ones do all of it before you've settled in your seat."),
 ]},
# ─────────────────────────── 26 ───────────────────────────
{"id": "r26", "variant": "amberlow", "voice": V2,
 "caption": "🧠 Round four. Final riddle round — and these are brutal.\n\n👇 Comment your score.\n\n"
            "🔁 Share with your most film-obsessed friend." + TAGS,
 "frames": [
   ("hook", {"text": "FINAL ROUND.\nTHESE ARE *BRUTAL*.", "size": 96},
    "Final riddle round, and these are brutal."),
   ("beat", {"text": "A TOY REALISES\nHE'S A *TOY* —\nAND IT BREAKS HIM", "kicker": "RIDDLE 01", "size": 62},
    "One. A toy realises he's a toy, and it breaks him."),
   ("beat", {"text": "A MAN WAKES WITH\nNO MEMORY AND A BODY\nTHAT KNOWS HOW TO *FIGHT*", "kicker": "RIDDLE 02", "size": 54},
    "Two. A man wakes with no memory, and a body that already knows how to fight."),
   ("beat", {"text": "EVERYTHING IS ONE\nLONG CHASE — *ONE WAY*,\nTHEN BACK AGAIN", "kicker": "RIDDLE 03", "size": 56},
    "Three. The entire film is one long chase, one direction, and then back again."),
   ("beat", {"text": "A GOD OF THUNDER\nLOSES HIS HAMMER\nAND FINDS A *HAIRCUT*", "kicker": "RIDDLE 04", "size": 58},
    "Four. A god of thunder loses his hammer, and finds a haircut."),
   ("end", {"text": "IF YOU GOT ALL FOUR\nYOU WATCH *TOO MANY*\nMOVIES. (GOOD.)",
            "question": "Final score? *Comment it.*"},
    "If you got all four, you watch too many movies. Which is exactly the right amount."),
 ]},
# ─────────────────────────── 27 ───────────────────────────
{"id": "r27", "variant": "noir", "voice": V1,
 "caption": "🎬 Great films don't explain themselves.\n\nThey trust you to keep up — and audiences almost "
            "always rise to it. The films that over-explain are the ones that age worst.\n\n"
            "👇 Which film respected your intelligence most?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "GREAT FILMS DON'T\n*EXPLAIN THEMSELVES*", "size": 90},
    "Great films don't explain themselves."),
   ("beat", {"text": "THEY TRUST YOU\nTO *KEEP UP*", "size": 94},
    "They trust you to keep up."),
   ("beat", {"text": "AND AUDIENCES\nALMOST ALWAYS\n*RISE TO IT*", "size": 78},
    "And audiences almost always rise to it."),
   ("beat", {"text": "THE FILMS THAT\nOVER-EXPLAIN AGE\n*WORST*", "size": 76},
    "It's the films that over explain, that spell out every motive, that age the worst."),
   ("end", {"text": "BEING CONFUSED FOR\nTEN MINUTES IS PART\nOF THE *PLEASURE*",
            "question": "Which film *respected* your intelligence?"},
    "Being a little confused for ten minutes is part of the pleasure. Which film trusted you most?"),
 ]},
# ─────────────────────────── 28 ───────────────────────────
{"id": "r28", "variant": "crimson", "voice": V2,
 "caption": "💔 Some films you love. Some films you survive.\n\nThey're not fun. You wouldn't rewatch them "
            "casually. But you're glad you saw them once — and you never quite forget them.\n\n"
            "👇 What's a film you're glad you saw but will never watch again?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "SOME FILMS YOU LOVE.\nSOME FILMS YOU\n*SURVIVE*.", "size": 84},
    "Some films you love. Some films you survive."),
   ("beat", {"text": "THEY'RE NOT *FUN*", "size": 100},
    "They aren't fun."),
   ("beat", {"text": "YOU WOULDN'T PUT\nTHEM ON *CASUALLY*", "size": 82},
    "You'd never put one on casually on a Tuesday evening."),
   ("beat", {"text": "BUT YOU'RE GLAD\nYOU SAW IT *ONCE*", "size": 86},
    "But you're glad you saw it once. And you never quite shake it."),
   ("end", {"text": "THAT'S NOT A FLAW.\nTHAT'S THE FILM\n*WORKING*.",
            "question": "A film you'll *never* watch again?"},
    "That isn't a flaw. That's the film working exactly as intended."),
 ]},
# ─────────────────────────── 29 ───────────────────────────
{"id": "r29", "variant": "indigo", "voice": V1,
 "caption": "🚀 The best science fiction isn't about spaceships.\n\nArrival is about grief. Her is about "
            "loneliness. Children of Men is about hope. The technology is just the way in.\n\n"
            "👇 Best sci-fi that's really about people?\n\n🔁 Save this list." + TAGS,
 "frames": [
   ("hook", {"text": "THE BEST SCI-FI\nISN'T ABOUT\n*SPACESHIPS*", "size": 90},
    "The best science fiction isn't about spaceships."),
   ("title", {"top": "ARRIVAL", "big": "IS ABOUT GRIEF", "bottom": "the aliens are the *way in*"},
    "Arrival is about grief. The aliens are just the way in."),
   ("title", {"top": "HER", "big": "IS ABOUT LONELINESS", "bottom": "the AI is the *mirror*"},
    "Her is about loneliness. The artificial intelligence is the mirror."),
   ("title", {"top": "CHILDREN OF MEN", "big": "IS ABOUT HOPE", "bottom": "the collapse is the *setting*"},
    "Children of Men is about hope. The collapse is only the setting."),
   ("end", {"text": "THE TECHNOLOGY\nIS NEVER\n*THE POINT*",
            "question": "Best sci-fi that's really about *people*?"},
    "The technology is never the point. It's the pressure that shows you who people actually are."),
 ]},
# ─────────────────────────── 30 ───────────────────────────
{"id": "r30", "variant": "amberlow", "voice": V2,
 "caption": "🎞️ A film's last line is the one you carry out of the cinema.\n\nGet it right and it "
            "rewrites everything before it. Get it wrong and two great hours evaporate on the walk home.\n\n"
            "👇 Best final line in film?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "THE LAST LINE IS THE\nONE YOU *CARRY OUT*\nOF THE CINEMA", "size": 76},
    "A film's last line is the one you carry out of the cinema."),
   ("beat", {"text": "GET IT RIGHT AND IT\n*REWRITES* EVERYTHING\nBEFORE IT", "size": 70},
    "Get it right, and it rewrites everything that came before it."),
   ("beat", {"text": "GET IT WRONG AND\nTWO GREAT HOURS\n*EVAPORATE*", "size": 74},
    "Get it wrong, and two great hours evaporate on the walk home."),
   ("beat", {"text": "IT'S THE HARDEST\n*FEW WORDS*\nIN THE SCRIPT", "size": 78},
    "It's the hardest few words in the entire script."),
   ("end", {"text": "SOME FILMS EARN\nSILENCE. SOME EARN\n*APPLAUSE*.",
            "question": "Best *final line* in film?"},
    "Some films earn silence. Some earn applause. Which last line has stayed with you?"),
 ]},
# ─────────────────────────── 31 ───────────────────────────
{"id": "r31", "variant": "violet", "voice": V1,
 "caption": "🎭 The performance that steals the film usually isn't the lead.\n\nA supporting actor has "
            "twenty minutes to make you remember them forever — and the great ones do it in one scene.\n\n"
            "👇 Best scene-stealing supporting performance?\n\n🔁 Share this." + TAGS,
 "frames": [
   ("hook", {"text": "THE PERFORMANCE THAT\nSTEALS THE FILM IS\n*RARELY THE LEAD*", "size": 74},
    "The performance that steals a film is rarely the lead."),
   ("beat", {"text": "A LEAD HAS\n*TWO HOURS*", "size": 96},
    "A lead has two hours to build a person."),
   ("beat", {"text": "A SUPPORTING ACTOR\nHAS *TWENTY MINUTES*", "size": 78},
    "A supporting actor has maybe twenty."),
   ("beat", {"text": "THE GREAT ONES\nDO IT IN *ONE SCENE*", "size": 84},
    "And the great ones do it in a single scene."),
   ("end", {"text": "YOU REMEMBER THEM\nLONGER THAN THE\n*PLOT*",
            "question": "Best *scene-stealing* performance?"},
    "You remember them longer than you remember the plot. Who's the best you've seen?"),
 ]},
# ─────────────────────────── 32 ───────────────────────────
{"id": "r32", "variant": "teal", "voice": V2,
 "caption": "🎬 Two weeks of film talk on this page — and the arguments were the best part.\n\nYou've "
            "picked apart endings, defended villains, and refused to agree on a single thing. Exactly right.\n\n"
            "👇 What should this page cover next? Name it and I'll build around it.\n\n"
            "🔁 Share this if you want more." + TAGS,
 "frames": [
   ("hook", {"text": "TWO WEEKS OF\n*FILM ARGUMENTS*", "size": 96},
    "Two weeks of film arguments on this page."),
   ("beat", {"text": "YOU DEFENDED\n*VILLAINS*", "size": 94},
    "You defended villains."),
   ("beat", {"text": "YOU FOUGHT ABOUT\n*ENDINGS*", "size": 92},
    "You fought about endings."),
   ("beat", {"text": "AND AGREED ON\n*ALMOST NOTHING*", "size": 86},
    "And you agreed on almost nothing, which is exactly how it should be."),
   ("end", {"text": "SO — WHAT SHOULD\nWE ARGUE ABOUT\n*NEXT*?",
            "question": "Name it. I'll build\nthe next weeks *around it*."},
    "So tell me what we should argue about next. Name it in the comments, and I'll build the "
    "next few weeks around whatever you pick."),
 ]},
]
