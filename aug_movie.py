# -*- coding: utf-8 -*-
"""Top Movie Reviews — Aug 1-7. 3 posts/day (FB). US/EU, English.
Original violet/gold graphics only (no posters we lack rights to, no download funnels).
Rotation: review card / watchlist card / hot-take card. Discussion-driven captions."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, when, mkdir, render
from image_movie import movie_review, movie_list, movie_take

IMG = mkdir("images/aug_movie")

# kinds:
#  ("review", title, year, rating, verdict, line, genre, caption)
#  ("list", title, items, kicker, caption)
#  ("take", text, kicker, emoji, caption)
DAYS = [
[
 ("review", "Inception", 2010, 4.5, "MIND-BENDER",
  "A heist inside dreams that trusts you to keep up. Big ideas, bigger emotion, and an ending built for arguments.",
  "SCI-FI THRILLER",
  "🎬 15 years on, people still argue about that final shot. A film that respects your intelligence and rewards a rewatch.\n\n💬 Did the top keep spinning — or fall? Settle it in the comments 👇"),
 ("list", "5 Mind-Bending Films That Respect Your Intelligence",
  ["Inception", "Shutter Island", "Arrival", "Memento", "Coherence"],
  "THE WATCHLIST",
  "🍿 Save this list for the next night you want a film that makes you THINK, not scroll.\n\n💬 Which have you seen — and which belongs on here that we missed? 👇"),
 ("take", "The best movie you watched this year\nprobably wasn't the one that\n*won all the awards*.", "HOT TAKE", "🏆",
  "🔥 Awards and greatness don't always overlap. Some of the films that stay with us for years never got a trophy.\n\n💬 Name a film you love that got zero recognition 👇"),
],
[
 ("review", "Parasite", 2019, 5.0, "MASTERPIECE",
  "Starts as a comedy, becomes something you won't shake for days. Every frame is doing something. Deserved every bit of praise.",
  "THRILLER · DRAMA",
  "🎬 The film that made the world stop fearing subtitles. Sharp, funny, and quietly devastating.\n\n💬 That basement scene — were you ready for it? 👇"),
 ("list", "5 Films With Endings You'll Argue About for Days",
  ["Parasite", "No Country for Old Men", "The Prestige", "Whiplash", "Prisoners"],
  "ENDINGS THAT HAUNT",
  "🍿 Bookmark this for a night you want a film that doesn't hand you easy answers.\n\n💬 Which ending wrecked you the most? 👇"),
 ("take", "A film with *subtitles* isn't\n\"too much work\" —\n\nit's the rest of the world's\nbest stories, unlocked. 🌍", "HOT TAKE", "💬",
  "🔥 Some of the greatest films ever made were never in English. One inch of subtitles is a small price for that.\n\n💬 What's the best non-English film you've ever seen? 👇"),
],
[
 ("review", "The Dark Knight", 2008, 5.0, "ICONIC",
  "Not a superhero movie — a crime epic that happens to have a cape. Anchored by a villain performance that redefined the genre.",
  "ACTION · CRIME",
  "🎬 Still the bar every comic-book film is measured against. Chaos, morality, and a Joker no one has topped.\n\n💬 Best comic-book movie ever — yes or no? 👇"),
 ("list", "5 Performances That Stole the Entire Movie",
  ["Heath Ledger — The Dark Knight", "Anthony Hopkins — Silence of the Lambs",
   "Joaquin Phoenix — Joker", "Kathy Bates — Misery", "Javier Bardem — No Country for Old Men"],
  "SCENE STEALERS",
  "🍿 The films are great — but these performances are why we remember them.\n\n💬 Whose performance would YOU add to this list? 👇"),
 ("take", "The *villain* is often the reason\na movie sticks with you.\n\nA weak villain makes\neven a great hero forgettable. 🦹", "HOT TAKE", "😈",
  "🔥 Heroes get the poster; villains get remembered. The best antagonists make the whole story matter.\n\n💬 Who's the greatest movie villain of all time? 👇"),
],
[
 ("review", "Interstellar", 2014, 4.5, "EPIC",
  "Ambitious, gorgeous, and unafraid to be emotional. A space film that's really about a parent and a promise.",
  "SCI-FI · DRAMA",
  "🎬 The docking scene, that score, and a story that earns its tears. Watch it on the biggest screen you can.\n\n💬 Did the ending land for you — or lose you? 👇"),
 ("list", "5 Sci-Fi Films That Get the Emotion Right",
  ["Interstellar", "Arrival", "Her", "WALL·E", "Blade Runner 2049"],
  "HEART IN THE STARS",
  "🍿 Sci-fi at its best isn't about spaceships — it's about us. Save this for a thoughtful night in.\n\n💬 Which one made you feel the most? 👇"),
 ("take", "*Practical effects* from 30 years ago\noften age better than\ntoday's CGI. 🎥", "HOT TAKE", "🦖",
  "🔥 There's a weight to real models and sets that pixels still struggle to match. Some old films still look flawless.\n\n💬 Name a movie whose effects STILL hold up 👇"),
],
[
 ("review", "Whiplash", 2014, 4.5, "INTENSE",
  "A two-hour panic attack about the cost of greatness. That final drum solo is one of the best endings ever filmed.",
  "DRAMA · MUSIC",
  "🎬 Under two hours and it never lets you breathe. You'll be exhausted — in the best way.\n\n💬 Was the teacher a monster or a maker of genius? 👇"),
 ("list", "5 Films Under 2 Hours Worth Your Whole Evening",
  ["Whiplash", "Nightcrawler", "Drive", "Gone Girl (edit yourself a snack first)", "Sicario"],
  "SHORT & UNFORGETTABLE",
  "🍿 No time for a 3-hour epic tonight? These punch hard and get out. Save the list.\n\n💬 Best short-but-perfect film in your book? 👇"),
 ("take", "A great movie *doesn't need*\na sequel.\n\nSometimes the bravest ending\nis just... the end. 🎬", "HOT TAKE", "🚪",
  "🔥 Not every story needs a part 2, 3 and a spin-off. Some films are perfect precisely because they stop.\n\n💬 Which movie should NEVER have gotten a sequel? 👇"),
],
[
 ("review", "Se7en", 1995, 4.5, "DARK",
  "A rain-soaked descent with two of the best lead performances of the 90s — and an ending that still hits like a truck.",
  "CRIME · THRILLER",
  "🎬 Bleak, brilliant, and unforgettable. 'What's in the box?' still echoes 30 years later.\n\n💬 Best crime thriller of all time — where does this rank? 👇"),
 ("list", "5 Twist Endings Nobody Saw Coming",
  ["The Sixth Sense", "Se7en", "The Usual Suspects", "Oldboy", "Fight Club"],
  "DIDN'T SEE IT COMING",
  "🍿 The first watch hits once — but the rewatch, knowing the twist, hits differently. Save this.\n\n💬 Which twist fooled you completely? (No spoilers in the first line!) 👇"),
 ("take", "\"The book was better\" —\n\nnot always. Some films\n*improved* on the page. 📖➡️🎬", "HOT TAKE", "📚",
  "🔥 It's almost a reflex to say the book wins. But a few adaptations genuinely sharpened the story.\n\n💬 Name a movie that beat the book 👇"),
],
[
 ("review", "Spirited Away", 2001, 5.0, "MAGICAL",
  "A hand-drawn dream that works at any age. Strange, gentle, and more imaginative than almost anything since.",
  "ANIMATION · FANTASY",
  "🎬 Over two decades old and nothing looks or feels like it. Proof animation is a medium, not a genre.\n\n💬 Favorite animated film of all time — go 👇"),
 ("list", "5 Movies to Watch When You Can't Decide",
  ["Spirited Away", "The Grand Budapest Hotel", "Back to the Future", "Paddington 2", "Ratatouille"],
  "GUARANTEED GOOD NIGHT",
  "🍿 Spent 40 minutes scrolling and picked nothing? Screenshot this list for next time.\n\n💬 What's YOUR go-to comfort movie? 👇"),
 ("take", "Rewatching a film you love\nisn't \"wasting\" a night.\n\nComfort movies exist for\na *reason*. 🍿", "HOT TAKE", "🔁",
  "🔥 There's no rule that says every watch has to be something new. A familiar favorite can be exactly what you need.\n\n💬 Which film have you rewatched the most? 👇"),
],
]

HOURS = [15, 19, 23]  # UTC — US/EU prime


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n_img = 0
    for di, day in enumerate(DAYS):
        for pi, entry in enumerate(day):
            kind = entry[0]
            ts = when(di, HOURS[pi])
            iid = f"amv-d{di+1}-{pi+1}"
            if iid in have:
                continue  # resume: already enqueued
            img_path = f"{IMG}/d{di+1}_{pi+1}.png"
            if kind == "review":
                _, title, year, rating, verdict, line, genre, caption = entry
                render(movie_review, title, year, rating, verdict, line, img_path, genre=genre)
            elif kind == "list":
                _, title, litems, kicker, caption = entry
                render(movie_list, title, litems, img_path, kicker=kicker)
            elif kind == "take":
                _, text, kicker, emoji, caption = entry
                render(movie_take, text, img_path, kicker=kicker, emoji=emoji)
            n_img += 1
            print(f"  rendered {img_path}")
            items.append({"id": iid, "account": "top-movie-reviews", "network": "facebook",
                          "type": "photo", "message": caption, "image_url": img_path,
                          "when": ts, "status": "pending"})
    save(q)
    print(f"TOP MOVIE REVIEWS: rendered {n_img} images, queue now {len(items)} items")


if __name__ == "__main__":
    build()
