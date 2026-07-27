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

WHEN: Premiered at Cannes on 21 May 2019, where it became the first Korean film ever to win the Palme d'Or. Runtime is 132 minutes.

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


def apply():
    p = "queue.json"
    q = json.load(open(p, encoding="utf-8"))
    n = 0
    for i in q["items"]:
        if i.get("id") == "tmr-w1-d1-2":
            i["message"] = PARASITE
            n += 1
    json.dump(q, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"updated {n} item(s); caption length = {len(PARASITE)} chars")


if __name__ == "__main__":
    apply()
