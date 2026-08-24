# -*- coding: utf-8 -*-
"""Top Movie Reviews — poster reel batch 1 (days 1-6).

All takes are original one-liners. Titles/years must match TMDB so the poster
lookup resolves; where a remake shares a title, the year disambiguates.
"""
from tmr_reel_common import countdown

TAGS = "#MovieRecommendation #FilmTwitter #WhatToWatch #MovieReview"

REELS = [
 countdown(
  "tmr_d1_never_unsee", "Thriller countdown",
  "5 films\nyou'll never\n*unsee.*",
  "Five thrillers you will never unsee.",
  [("Shutter Island", 2010, "The second watch\nis a *different film.*",
    "The second watch is a different film."),
   ("Gone Girl", 2014, "Nobody in it\nis *telling the truth.*",
    "Nobody in it is telling the truth."),
   ("Prisoners", 2013, "Two hours of dread,\nand *no easy answer.*",
    "Two hours of dread, and no easy answer."),
   ("Oldboy", 2003, "One corridor.\nOne take.\n*Unforgettable.*",
    "One corridor, one take, unforgettable."),
   ("Se7en", 1995, "The last five minutes\n*never leave you.*",
    "The last five minutes never leave you.")],
  hashtags=TAGS),

 countdown(
  "tmr_d2_mind_benders", "Mind-benders",
  "5 films that\n*rewire*\nyour brain.",
  "Five films that rewire your brain.",
  [("Primer", 2004, "Made for $7,000\nand *nobody understands it.*",
    "Made for seven thousand dollars, and nobody understands it."),
   ("Coherence", 2013, "One dinner party.\n*Infinite* versions of it.",
    "One dinner party. Infinite versions of it."),
   ("Arrival", 2016, "The twist isn't a twist.\nIt's *the whole point.*",
    "The twist isn't a twist. It's the whole point."),
   ("Memento", 2000, "Told backwards,\nand it *had to be.*",
    "Told backwards, and it had to be."),
   ("Inception", 2010, "People still argue\nabout *that last shot.*",
    "People still argue about that last shot.")],
  hashtags=TAGS),

 countdown(
  "tmr_d3_gut_punch", "Bring tissues",
  "5 films that\n*wreck* you\nemotionally.",
  "Five films that wreck you emotionally.",
  [("Manchester by the Sea", 2016, "Grief without\nthe *Hollywood ending.*",
    "Grief without the Hollywood ending."),
   ("Grave of the Fireflies", 1988, "The saddest film\never *animated.*",
    "The saddest film ever animated."),
   ("Requiem for a Dream", 2000, "You'll watch it once.\n*That's enough.*",
    "You'll watch it once. That's enough."),
   ("Schindler's List", 1993, "The red coat.\nThat's *all* I'll say.",
    "The red coat. That's all I'll say."),
   ("Hachi: A Dog's Tale", 2009, "Do *not* watch this\nwith a dog nearby.",
    "Do not watch this with a dog nearby.")],
  hashtags=TAGS),

 countdown(
  "tmr_d4_one_location", "One room, one story",
  "5 films set\nin *almost one*\nlocation.",
  "Five films set in almost one location.",
  [("Buried", 2010, "Ninety minutes\ninside *a coffin.*",
    "Ninety minutes inside a coffin."),
   ("12 Angry Men", 1957, "One room.\nTwelve men.\n*Perfect* writing.",
    "One room, twelve men, perfect writing."),
   ("Rear Window", 1954, "He never leaves\nthe chair — and it's\n*unbearable.*",
    "He never leaves the chair, and it's unbearable."),
   ("Locke", 2013, "One man.\nOne car.\n*One long night.*",
    "One man, one car, one long night."),
   ("Rope", 1948, "Built to look like\n*a single take* in 1948.",
    "Built to look like a single take, in 1948.")],
  hashtags=TAGS),

 countdown(
  "tmr_d5_korean", "Korean cinema",
  "5 Korean films\nthat *beat*\nHollywood.",
  "Five Korean films that beat Hollywood at its own game.",
  [("The Wailing", 2016, "You won't know\nwho to *trust.* Ever.",
    "You won't know who to trust. Ever."),
   ("Burning", 2018, "Slow, quiet,\nand *deeply* unsettling.",
    "Slow, quiet, and deeply unsettling."),
   ("Memories of Murder", 2003, "A true case,\nand *no* satisfying answer.",
    "A true case, and no satisfying answer."),
   ("Train to Busan", 2016, "Zombies, yes —\nbut you'll cry *anyway.*",
    "Zombies, yes, but you'll cry anyway."),
   ("Parasite", 2019, "Comedy, then horror.\n*One staircase* apart.",
    "Comedy, then horror, one staircase apart.")],
  hashtags=TAGS),

 countdown(
  "tmr_d6_twists", "Endings that flip",
  "5 twists\nthat *broke*\nthe internet.",
  "Five twists that broke the internet.",
  [("The Prestige", 2006, "The clue is in\nthe *first line.*",
    "The clue is in the first line."),
   ("Fight Club", 1999, "You'll rewatch it\njust to *catch them all.*",
    "You'll rewatch it just to catch them all."),
   ("The Sixth Sense", 1999, "Still the *gold standard.*\nStill holds up.",
    "Still the gold standard, and it still holds up."),
   ("Oldboy", 2003, "The reveal is\n*worse* than you're imagining.",
    "The reveal is worse than you're imagining."),
   ("The Usual Suspects", 1995, "The last thirty seconds\n*rewrite* everything.",
    "The last thirty seconds rewrite everything.")],
  hashtags=TAGS),
]
