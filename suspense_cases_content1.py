# -*- coding: utf-8 -*-
"""Suspense Ahead - THE VANCE FILES, pilot season (7 episodes, days 45-51).

Original fiction: Inspector Nora Vance solves a self-contained case each
episode with a fair, visible clue. Every episode has a "YOUR TURN" beat just
before the reveal so viewers can guess in the comments. Stills + Ken Burns
motion pipeline (video_suspense_cases.py), ~60s each. Each case is built on a
different mechanism (swap, tide table, riddle, alibi, cipher, footprints,
auction) so the episodes don't read as one template.
"""
STYLE = "photo"

TAG = "🎭 SUSPENSE AHEAD — a new case every day."


def _narr(text):
    return " ".join(text.replace("*", "").replace("\\\"", "").split())


def H(text, query, narr=None):
    return {"kind": "hook", "text": text, "narration": narr or _narr(text), "query": query}


def B(text, query, kicker="", narr=None):
    d = {"kind": "beat", "text": text, "narration": narr or _narr(text), "query": query}
    if kicker:
        d["kicker"] = kicker
    return d


def E(text, question, query, narr=None):
    return {"kind": "end", "text": text, "question": question,
            "narration": narr or _narr(text), "query": query}


def cap(num, title, teaser, ask):
    return (f"🕵️ THE VANCE FILES · Case #{num}: {title} (original fiction)\n\n"
            f"{teaser}\n\n👇 {ask}\n\n{TAG}")


REELS = [
 ("sa_d45_s1_vance_missing_violin", [
  H("The museum's famous violin\nwas a *fake.*\nNobody knew since when.", "antique violin museum display dark"),
  B("It sat in a sealed glass case.\nThe lock hadn't been touched\nin weeks.", "glass display case museum night"),
  B("Inspector Nora Vance\nwas called in after an expert\nfelt something was off.", "detective woman coat walking museum"),
  B("Three people had been\nnear the case this month:\nthe curator, the conductor, the caterer.", "museum gallery people evening"),
  B("The conductor borrowed\nthe violin once,\nthree weeks ago.", "orchestra conductor baton hands"),
  B("The caterer only served drinks\nin the main hall,\nnever the gallery.", "waiter champagne tray gala"),
  B("The curator held\nthe only key\nand cleaned the case weekly.", "keys museum curator hand"),
  B("A catalog photo, taken\nten days ago, showed\n*dull, old strings.*", "old violin strings closeup", kicker="THE CLUE"),
  B("The violin in the case\nhad\n*bright, brand-new* strings.", "violin strings shiny closeup"),
  B("Strings don't renew themselves.\nSo who swapped it,\nand when?", "magnifying glass detective desk", kicker="YOUR TURN"),
  B("The swap happened after the photo.\nThe conductor had returned it\nweeks before.", "calendar dates desk pen"),
  E("Only one person had the key\nin those ten days.\n*The curator.*", "Did you catch the strings?", "empty museum hallway night"),
 ], cap(1, "The Fake Violin", "A priceless violin turned out to be a copy, and nobody knew since when. Inspector Vance found the answer in its strings.", "Who do you think swapped it: the curator, the conductor, or the caterer?")),

 ("sa_d46_s1_vance_dark_lighthouse", [
  H("A lighthouse went dark\nfor three nights.\nA ship *nearly* wrecked.", "lighthouse night storm dark sea"),
  B("The keeper swore\nhe never left the tower,\nnot once.", "lighthouse keeper old man tower"),
  B("Inspector Vance crossed\nthe causeway\nat low tide.", "causeway sea low tide path"),
  B("The lamp was fine.\nThe oil was full.\nNo fault anywhere.", "lighthouse lamp lens closeup"),
  B("So someone had switched it\noff on purpose.", "light switch dark hand closeup"),
  B("The keeper held\nthe only key\nto the lamp room.", "old key lock door dark"),
  B("A supply boat captain\nsaid he'd seen small boats\nnear the north cove.", "small boat night sea cove"),
  B("The keeper's boots were\ncaked in *fine white sand.*", "muddy boots sand closeup", kicker="THE CLUE"),
  B("The tower stands on bare black rock.\nThe only sand is\nat the north cove.", "black rocks sea waves tower"),
  B("He said he never left.\nSo why was the sand\non his boots?", "detective looking at boots", kicker="YOUR TURN"),
  B("Each dark night matched\nthe lowest tide\nin the tide table.", "tide table chart paper"),
  E("He wasn't guarding the light.\nHe was *clearing the way*\nfor smugglers.", "Would you have checked his boots?", "lighthouse night calm sea"),
 ], cap(2, "The Dark Lighthouse", "A lighthouse went dark three nights running and a ship nearly wrecked. The keeper swore he never left the tower. His boots said otherwise.", "Would you have checked the keeper's boots?")),

 ("sa_d47_s1_vance_torn_map", [
  H("Two siblings. Two halves\nof an old map.\nAnd a treasure *nobody* found.", "old torn treasure map table"),
  B("The map was drawn in 1890\nfor an English village\nwith a bell tower.", "english village church bell tower"),
  B("The siblings had dug up\nthe churchyard for weeks\nand found nothing.", "digging shovel grass churchyard"),
  B("Inspector Vance read\nthe riddle written\nunder the compass.", "old map compass riddle handwriting"),
  B("\"Dig where the bell's shadow\nfalls at noon\non the longest day.\"", "bell tower shadow ground sunlight", kicker="THE CLUE"),
  B("The siblings had dug\nwhere the shadow fell\nin *winter.*", "winter long shadow field"),
  B("In winter the sun sits low\nand shadows stretch\nlong across the ground.", "long shadows low sun grass"),
  B("On the longest day\nthe sun is high,\nand the shadow is *short.*", "short shadow noon summer"),
  B("At noon, which way\ndoes the shadow point,\nand how far from the tower?", "sundial shadow stone", kicker="YOUR TURN"),
  B("On June twenty-first, Vance marked\nthe shadow's tip, just north\nof the tower base.", "person marking ground tower summer"),
  B("Beneath one flagstone,\nher spade struck\nsomething hard.", "spade stone ground digging"),
  E("A small iron chest,\njust steps from where\nthey'd started.", "Would you have dug in summer?", "old iron chest treasure dark"),
 ], cap(3, "The Torn Map", "Two siblings dug for a treasure for weeks and found nothing. Inspector Vance solved the riddle in one afternoon.", "Where would you have dug?")),

 ("sa_d48_s1_vance_wrong_alibi", [
  H("He had a ticket stub,\na witness, and a\n*perfect* alibi.", "cinema ticket stub hand"),
  B("A jeweler's safe was emptied\nat nine o'clock\non Friday night.", "jewelry shop safe night dark"),
  B("The main suspect, Dale,\nsaid he was at the cinema\nall evening.", "man cinema lobby night"),
  B("He showed his ticket stub.\nHe even described\nthe film's ending.", "movie theater seats screen"),
  B("The usher remembered him\nbuying popcorn\nat eight forty.", "popcorn cinema counter"),
  B("Inspector Vance went\nto the cinema to check\nthe schedule.", "detective woman cinema entrance night"),
  B("A notice on the door:\n\"Projector failure.\nFilm stopped halfway.\"", "closed sign door notice dark", kicker="THE CLUE"),
  B("The projector failed at nine fifteen,\nlong before\nthe final scene.", "film projector old dark room"),
  B("Nobody in that cinema\nhad seen\nhow the film ended.", "empty cinema seats dark"),
  B("So how did Dale describe\nan ending he\ncould never have seen?", "detective thinking notebook night", kicker="YOUR TURN"),
  B("He'd read the plot online,\nthen slipped out\nafter the popcorn.", "man leaving cinema side door night"),
  E("He bought a ticket\nto be seen,\nthen left to *do the job.*", "Would you have fallen for the stub?", "cinema marquee night street"),
 ], cap(4, "The Perfect Alibi", "A ticket stub, a witness, and a film he described perfectly. Inspector Vance found the one detail he couldn't have known.", "Did the ending give him away for you?")),

 ("sa_d49_s1_vance_newspaper_cipher", [
  H("A note, nothing but numbers,\nwas left on a\n*locked* desk.", "handwritten numbers note desk closeup"),
  B("Three numbers per line.\n12, 4, 7.\n9, 2, 3.", "numbers handwritten paper pen"),
  B("The banker who found it\nhad no idea\nwhat it meant.", "banker office desk worried"),
  B("Inspector Vance noticed\na folded newspaper\nunder the note.", "folded newspaper desk dark"),
  B("Today's edition,\nwith tiny dots\nmarked beside some words.", "newspaper print closeup dots"),
  B("Page, line, word.\nCould the numbers be\npointing into the paper?", "reading newspaper magnifying glass", kicker="YOUR TURN"),
  B("Page 12, line 4, word 7:\n\"Harbor.\"", "harbor boats evening", kicker="THE CLUE"),
  B("Page 9, line 2, word 3:\n\"Midnight.\"", "clock midnight dark"),
  B("The next lines spelled out:\n\"Pier six. Bring the ledger.\"", "wooden pier night lamp"),
  B("Someone was arranging a meeting\nto sell the bank's\nsecret ledger.", "ledger book old desk"),
  B("Vance waited on pier six\nbefore midnight,\nin the dark.", "pier night fog silhouette"),
  E("The buyer arrived.\nSo did the clerk\n*who wrote the note.*", "Did you crack it before the reveal?", "harbor night fog quiet"),
 ], cap(5, "The Newspaper Cipher", "A note of numbers on a locked desk, and a newspaper left beside it. Inspector Vance worked out what the numbers pointed to.", "Did you crack the code before she did?")),

 ("sa_d50_s1_vance_snow_footprints", [
  H("One set of footprints\nled *into* a cabin.\nNone led out.", "footprints snow cabin"),
  B("A chest of cash vanished\nfrom a mountain cabin\nduring the snowfall.", "mountain cabin snow night"),
  B("The owner, Harlan,\nsaid he'd been\nasleep all night.", "man sleeping cabin bed"),
  B("Fresh snow lay unbroken\naround the whole cabin.", "untouched snow field cabin"),
  B("The only prints went\nfrom the road\nto the front door.", "footprints path snow door"),
  B("So the thief should still\nbe inside the cabin.", "cabin window light snow"),
  B("Vance searched every room.\nNobody was there.\nThe cash was gone too.", "empty cabin room dark detective"),
  B("She knelt by the prints.\nThe *toe* marks were deeper\nthan the heels.", "footprint snow closeup", kicker="THE CLUE"),
  B("People walking forward\nland on their heels first.\nSomeone walking backward doesn't.", "boots walking snow forward"),
  B("What if the prints\nweren't arriving\nat all?", "detective kneeling snow footprints", kicker="YOUR TURN"),
  B("Someone had walked *backward*\nfrom the door to the road,\nin the same footsteps.", "footprints road snow trail"),
  E("The thief left by the front door,\nstepping in his own prints.\n*Harlan's boots matched.*", "Would you have checked the toes?", "cabin snow dawn quiet"),
 ], cap(6, "Footprints in the Snow", "Footprints led into a cabin and none led out, and the cash was gone. Inspector Vance read the story the prints were telling.", "Would you have noticed the toes?")),

 ("sa_d51_s1_vance_midnight_auction", [
  H("One bidder won\nevery best lot.\nNobody ever *saw* him bid.", "auction hall gavel dark"),
  B("The Hargrave Auction House\nsold rare clocks\nevery Thursday night.", "antique clocks auction room"),
  B("Each week an anonymous bidder\nwon the finest pieces\nfor suspiciously low prices.", "antique clock closeup gold"),
  B("He never raised a paddle.\nHe never spoke.\nHe just won.", "auction paddle crowd hands"),
  B("Inspector Vance attended\nthe next auction, quietly,\nin the back row.", "detective woman back row crowd"),
  B("She watched the room.\nThe bids rose.\nThen stopped, abruptly.", "auction crowd watching tense"),
  B("Every sale came just after\nthe auctioneer's pen *clicked.*", "pen click closeup hand", kicker="THE CLUE"),
  B("Click once, and the hammer fell.\nNo one in the room\nhad actually bid.", "gavel falling wooden block"),
  B("So who was the bidder\nthe room could\nnever see?", "empty chair auction dark", kicker="YOUR TURN"),
  B("The \"phone bidder\" was\nalways the same number.\nNobody had ever heard his voice.", "old telephone desk dark"),
  B("Vance asked to hear him.\nThe phone wasn't connected\nto any line at all.", "telephone cord unplugged closeup"),
  E("The bidder never existed.\nThe auctioneer was selling\nthe best clocks *to himself.*", "Did you hear the click?", "auction house night empty"),
 ], cap(7, "The Midnight Auction", "One bidder won every best lot and nobody ever saw him bid. Inspector Vance listened for the one sound that gave it away.", "Did you spot the clue before the reveal?")),
]
