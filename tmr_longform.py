# -*- coding: utf-8 -*-
"""Long-form review caption format for Top Movie Reviews.

Answers what / who / when / how / how much, then works through story, acting,
camera, score, direction, strengths, weaknesses, verdict, rating and audience
recommendation — written as prose, not labelled template blocks.

All hard facts verified 2026-07-27 against Wikipedia / Britannica / Variety /
Saturation.io. Nothing here is invented.

Upgrades the queued Day-1 review (tmr-w1-d1-2) in place.
"""
import sys, json
sys.stdout.reconfigure(encoding="utf-8")

PARASITE = """🎬 PARASITE (2019) — the film that finally broke the Oscars' language barrier

Some films win awards because the industry feels it ought to reward them. This one won because there was genuinely nothing else like it that year.

━━━━━━━━━━━━━━━━━━━━

📌 THE BASICS

WHAT: A South Korean dark comedy that quietly becomes a thriller. A poor family talks its way, one member at a time, into working for a rich one.

WHO: Directed by Bong Joon-ho, who co-wrote it with Han Jin-won. Song Kang-ho leads as the father, with Choi Woo-shik and Park So-dam as the son and daughter, Jang Hye-jin as the mother, and Lee Sun-kyun, Cho Yeo-jeong, Park Myung-hoon and Lee Jung-eun on the other side of the story. Shot by Hong Kyung-pyo, cut by Yang Jin-mo, scored by Jung Jae-il.

WHEN: Premiered at Cannes on 21 May 2019, where it became the first Korean film ever to win the Palme d'Or. Runtime is about 2 hours 12 minutes.

HOW MUCH: Made for roughly $11.4 million. Earned about $257.6 million worldwide — more than twenty times its cost.

THE RECORD: Four Academy Awards, including Best Picture, Best Director and Best Original Screenplay. The first film not in the English language to win Best Picture in the Academy's history.

━━━━━━━━━━━━━━━━━━━━

📖 THE STORY (no spoilers)

The Kim family lives in a semi-basement flat where the window looks out at street level. They fold pizza boxes for money and hunt for a neighbour's wifi signal from the bathroom.

Then the son gets a chance: tutoring the daughter of the wealthy Park family, in a house on a hill designed by a famous architect. He takes it. And then he starts finding reasons why his family should work there too.

That's all you should know. The film is built on a turn that arrives roughly halfway through, and knowing it in advance costs you the best hour of cinema in a decade.

What makes the script remarkable is the fairness of it. There's no villain. The rich family isn't cruel — they're pleasant, distracted, and insulated. The poor family isn't noble — they're funny, resourceful and willing to hurt people with less than them. Bong refuses to let you settle into rooting for anyone, and that discomfort is the whole point.

━━━━━━━━━━━━━━━━━━━━

🎭 THE ACTING

Song Kang-ho gives one of the great screen performances of the century, and he does most of it with his face at rest. There's a moment late in the film — a single reaction to a small, thoughtless gesture — that carries more weight than any speech in the script. You watch a man's dignity break in real time.

Park So-dam is the film's secret weapon: completely composed, the smartest person in every room she enters. Cho Yeo-jeong makes the wealthy mother genuinely likeable rather than a caricature, which is much harder and matters much more — the film only works if her kindness feels real.

Lee Jung-eun has the single most demanding stretch in the film. Anyone who has seen it knows exactly which scene, and knows she carries it alone.

━━━━━━━━━━━━━━━━━━━━

🎥 THE CAMERA

Hong Kyung-pyo shoots the two houses as opposing arguments. The Park house is wide, horizontal, full of glass and framed light — the camera has room to breathe. The Kim flat is cramped, vertical, always looking up toward a window at pavement height.

Watch the staircases. The entire film is people moving up and down them, and by the end you'll notice you've been reading the story geographically without anyone explaining it. Nobody in the film ever gives a speech about inequality. The set does it for them — the house was purpose-built for the production so the geometry would land exactly this way.

And it rains. When it rains, the film's whole structure tilts, and the same water means two completely different things depending on which house you're standing in.

━━━━━━━━━━━━━━━━━━━━

🎵 THE MUSIC

Jung Jae-il's score is doing something clever: it's mostly light, mannered, almost baroque. It sounds like polite company. It plays under scenes of people lying to each other with beautiful manners, and the mismatch is deliberately unsettling. Then in the last act it drops the politeness entirely.

If you rewatch, listen to the piano in the first hour. It's telling you what kind of film this is going to become before the film admits it.

━━━━━━━━━━━━━━━━━━━━

🎬 THE DIRECTION

This is Bong's best control of tone, and tone is the hardest thing in filmmaking. Parasite is a comedy for forty minutes. Genuinely funny — the family's schemes play like a heist. Then it turns, and it never turns back, and you can't point to the exact frame where it happened.

Most directors who attempt that leave a visible seam. There is no seam here.

━━━━━━━━━━━━━━━━━━━━

✅ STRENGTHS

• A screenplay with no wasted scene — everything planted pays off
• Song Kang-ho, at the peak of his powers
• Production design that argues the film's thesis without dialogue
• Tonal control that shouldn't be possible
• Rewatch value: the second viewing is a different film

⚠️ WEAKNESSES

• The final act asks a lot of you emotionally, and not everyone wants to be asked
• Some viewers find the turn abrupt — fair, though we'd argue the abruptness is the argument
• If you need a character to root for, this film will refuse you for two hours
• The last ten minutes divide people sharply, and always have

━━━━━━━━━━━━━━━━━━━━

⭐ FINAL VERDICT: 9.5 / 10

The rare film that swept everything AND deserved it. Not a difficult watch, not homework, not medicine — it's tense and funny and moves fast. It just happens to be about something.

👥 WATCH IT IF: you like thrillers with real ideas, you enjoy films that reward a second viewing, or you've been meaning to get past the subtitle barrier and want the best possible reason to.

🚫 MAYBE SKIP IF: you want a comfort watch, or you need a clean, comfortable ending.

━━━━━━━━━━━━━━━━━━━━

👇 COMMENT: Did the ending land for you — or lose you? We've seen this argument split entire friendships, so be honest.

🔁 SHARE this with the person who still says "I don't watch films with subtitles." This is the one that changes their mind.

#MovieReview #Parasite #BongJoonHo #FilmTwitter #Cinephile #MustWatch #KoreanCinema #OscarWinner #MovieNight #FilmLovers #WhatToWatch #Cinema #MovieRecommendation #FilmCritic #BestPicture

🎬 Top Movie Reviews — one honest verdict a day."""


FURY_ROAD = """🎬 MAD MAX: FURY ROAD (2015) — the greatest action film of the century, and it's barely close

A studio spent over $150 million on a two-hour car chase with almost no dialogue, directed by a 70-year-old man who also made Happy Feet. It should have been a disaster. Instead it won six Academy Awards.

━━━━━━━━━━━━━━━━━━━━

📌 THE BASICS

WHAT: A war rig goes one way across the desert, then turns around and comes back. That is genuinely the entire plot — and it's one of the most acclaimed films of the last twenty years.

WHO: Directed and co-written by George Miller, who made the original Mad Max in 1979. Tom Hardy plays Max, Charlize Theron plays Furiosa, Nicholas Hoult plays Nux, and Hugh Keays-Byrne plays Immortan Joe — the same actor who played the villain Toecutter in the 1979 original. Shot by John Seale, who came out of retirement to do it. Cut by Margaret Sixel. Scored by Junkie XL.

WHEN: Released in 2015, roughly thirty years after the previous Mad Max film. Runtime is about 2 hours.

HOW MUCH: Budget reported between $154 million and $185 million. Earned about $380 million worldwide.

THE RECORD: Six Academy Awards — Film Editing, Costume Design, Production Design, Makeup and Hairstyling, Sound Editing and Sound Mixing. It was also nominated for Best Picture, Best Director and Best Cinematography, and lost all three. Ten nominations, six wins, and an argument that's still running about the three it didn't get.

━━━━━━━━━━━━━━━━━━━━

📖 THE STORY (no spoilers)

In a desert wasteland, one man controls the water and therefore controls everyone. Furiosa, his most trusted driver, takes a war rig out on a supply run and quietly goes off-route with something he desperately wants back. Max, captured and being used as a human blood supply, ends up strapped to the front of a pursuing car.

That's the setup. The rest is the chase.

What's remarkable is how much story fits inside it. Furiosa gets a complete character arc with maybe forty lines of dialogue. Nux — a minor henchman — has a more convincing redemption than most protagonists get in three films. And Max barely speaks at all.

Miller told the story visually because he had to: he storyboarded the film before writing a script, and the film reads like something drawn rather than written. You always know exactly where every vehicle is in relation to every other one, which sounds basic until you watch almost any other modern action film and realise you have no idea.

━━━━━━━━━━━━━━━━━━━━

🎭 THE ACTING

Charlize Theron is the lead of this film. Not Tom Hardy — Theron. Furiosa carries the entire emotional weight, and Theron plays her with a kind of exhausted fury that never tips into speechmaking. The moment in the desert, on her knees, is one of the great wordless performances of the decade.

Tom Hardy makes an interesting choice: he plays Max as barely verbal, closer to an animal than a hero, and lets the film be someone else's story. It takes confidence to be the title character and step back.

Nicholas Hoult is the surprise. Nux starts as a disposable fanatic and becomes the most human person on screen, and Hoult does it without a single scene of explanation.

━━━━━━━━━━━━━━━━━━━━

🎥 THE CAMERA

John Seale came out of retirement for this and shot it like nothing else in the genre.

The key decision: the point of interest sits in the centre of the frame, almost always. Sounds trivial. It means that in a film cut this fast, your eye never has to hunt for what matters — so you can cut quickly without confusing anyone. Most modern action is incoherent precisely because it ignores this.

Then there's the crucial fact: the vehicles are real. Real cars, real desert, real stunt performers on poles swinging over moving trucks. There is CGI in the film, but it's mostly removing wires and extending backgrounds. When something crashes, something crashed. That physical weight is why it still looks better than films made a decade later.

Note the colour too — deep orange days and cold blue nights, pushed far past realism, which is why a single frame of this film is instantly recognisable.

━━━━━━━━━━━━━━━━━━━━

🎵 THE MUSIC

Junkie XL's score is essentially a drum and guitar assault, and the film puts the guitar on screen — a blind man on a truck of speakers with a flamethrowing instrument. The score has a character playing it inside the world of the film.

It's relentless by design. There are almost no quiet moments, and the few there are land harder because of the noise around them.

━━━━━━━━━━━━━━━━━━━━

🎬 THE DIRECTION

Miller was 70 when this was released and he out-directed everyone half his age.

The editing deserves its own note. Margaret Sixel — who had never cut an action film — assembled around 480 hours of footage into 120 minutes. Miller's reasoning for hiring her was that if a man cut it, it would look like every other action film. She won the Oscar, and became the first South African-born editor to do so.

━━━━━━━━━━━━━━━━━━━━

✅ STRENGTHS

• Practical stunt work that CGI still hasn't matched
• Charlize Theron's Furiosa — a genuinely new kind of action lead
• Visual storytelling so clear you could follow it with the sound off
• Editing that's fast without ever being confusing
• World-building done entirely through design, never exposition

⚠️ WEAKNESSES

• If you need plot complexity, there isn't any — it's a straight line
• Character backstory is almost entirely withheld; some viewers find that cold
• The relentlessness is exhausting by design, and not everyone wants that
• Max himself is arguably the least interesting person in his own film

━━━━━━━━━━━━━━━━━━━━

⭐ FINAL VERDICT: 9.5 / 10

The best action film since the turn of the century, and the clearest proof that spectacle and craft aren't opposites. Every action director since has been trying to copy it, and almost none have understood that the secret isn't the crashes — it's the clarity.

👥 WATCH IT IF: you like action with actual craft, you're tired of CGI weightlessness, or you want to see what a director does when a studio finally lets him build the thing for real.

🚫 MAYBE SKIP IF: you want a dialogue-driven story, or a quiet night in.

━━━━━━━━━━━━━━━━━━━━

👇 COMMENT: Is this the best action film ever made — or is there something you'd put above it? Name it and defend it.

🔁 SHARE this with the friend who still hasn't seen it. They've had ten years.

#MovieReview #MadMax #FuryRoad #GeorgeMiller #FilmTwitter #Cinephile #MustWatch #ActionMovies #CharlizeTheron #MovieNight #FilmLovers #WhatToWatch #Cinema #MovieRecommendation #FilmCritic

🎬 Top Movie Reviews — one honest verdict a day."""


def apply():
    p = "queue.json"
    q = json.load(open(p, encoding="utf-8"))
    n = 0
    for i in q["items"]:
        if i.get("id") == "tmr-w1-d1-2":
            i["message"] = PARASITE
            n += 1
        elif i.get("id") == "tmr-w1-d4-2":
            i["message"] = FURY_ROAD
            n += 1
    json.dump(q, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"updated {n} item(s); Parasite={len(PARASITE)} chars, "
          f"FuryRoad={len(FURY_ROAD)} chars")


if __name__ == "__main__":
    apply()
