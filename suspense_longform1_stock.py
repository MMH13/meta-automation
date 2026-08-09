# -*- coding: utf-8 -*-
"""Suspense Ahead — "The Neighbor Who Wasn't", stock-footage + 1:1 version.
Same story/narration as suspense_longform1.py (the SVG version), rebuilt on
video_suspense_stock.py: real Pexels B-roll instead of illustrated scenes,
1080x1080 square instead of 9:16 (better fit for FB feed/Watch, per the
publishing-format call), captions burned in since most feed viewers watch
muted.

~14 distinct footage categories, reused across matching beats so the pipeline
does ~14 searches/downloads instead of 42 - keeps it fast and avoids
Pexels rate limits, while still giving each story beat visually-matched B-roll.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_suspense_stock import build

_HERE = Path(__file__).parent
OUT_MP4 = _HERE / "images" / "suspense_longform1_square.mp4"
WORK_DIR = _HERE / "images" / "suspense_longform1_square_work"
STATE = _HERE / "suspense_longform1_square_state.json"
LOCK = _HERE / "suspense_longform1_square.lock"

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

# footage_key -> Pexels search query. Reused across multiple beats.
Q = {
    "house_night": "house exterior night window light dark",
    "hallway_normal": "apartment hallway night empty corridor",
    "door_normal": "wooden door closeup dark hallway",
    "dread_dark_room": "dark room night subtle shadow moody",
    "phone_glow": "phone screen glow dark room night",
    "mailboxes": "old mailboxes hallway apartment",
    "manager_office": "office desk lamp night empty",
    "bedroom_night": "dark bedroom night window moody",
    "clock_night": "clock ticking macro night",
    "door_ajar": "door ajar dark room light gap",
    "empty_room": "empty room abandoned dark dust",
    "window_silhouette": "window curtain silhouette night rain",
    "hallway_exit": "walking fast hallway corridor dark",
    "window_reflection": "window reflection night glass dark",
}

BEATS = [
 dict(kind="hook", text="Six months ago,\nI moved into apartment *4B*.",
      narration="Six months ago, I moved into apartment four B.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="It was quiet.\nAffordable.\n*Perfect.*",
      narration="It was quiet. Affordable. Perfect.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The only strange thing\nwas *4A*, right across the hall.",
      narration="The only strange thing was four A, right across the hall.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="Every time I left for work,\ntheir door was *open a crack*.",
      narration="Every time I left for work, their door was open a crack.",
      query=Q["door_normal"], footage_key="door_normal"),
 dict(kind="beat", text="Just enough to see someone\nstanding there,\nwatching me *lock up*.",
      narration="Just enough to see someone standing there, watching me lock up.",
      query=Q["door_normal"], footage_key="door_normal"),
 dict(kind="beat", text="I never saw a face.\nJust a shape,\nstill, in the dark gap.",
      narration="I never saw a face. Just a shape, still, in the dark gap.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="At first I thought nothing of it.\nNew city.\n*New nerves.*",
      narration="At first I thought nothing of it. New city. New nerves.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="Then I started\nnoticing the *timing*.",
      narration="Then I started noticing the timing.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Whatever I did,\nthey did it *first*.", kicker="LATER",
      narration="Whatever I did, they did it first.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="I'd reach for my keys —\nthe door across the hall\nwould already be open.",
      narration="I'd reach for my keys. The door across the hall would already be open.",
      query=Q["door_normal"], footage_key="door_normal"),
 dict(kind="beat", text="I'd come home late —\nit would already be cracked open,\n*waiting*.",
      narration="I'd come home late. It would already be cracked open, waiting.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="Like they always knew,\n*before I did*.",
      narration="Like they always knew, before I did.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I tried recording it\non my phone once.",
      narration="I tried recording it on my phone once.",
      query=Q["phone_glow"], footage_key="phone_glow"),
 dict(kind="beat", text="The video showed an empty hallway.\nNo door.\n*No gap at all.*",
      narration="The video showed an empty hallway. No door. No gap at all.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="Just my own breathing,\nand one sound\nunderneath it.",
      narration="Just my own breathing, and one sound underneath it.",
      query=Q["phone_glow"], footage_key="phone_glow"),
 dict(kind="beat", text="Footsteps.\n*Stopping exactly\nwhen mine did.*",
      narration="Footsteps. Stopping exactly when mine did.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I asked the building manager\nabout 4A.",
      narration="I asked the building manager about four A.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="He checked his list,\nlooked confused,\nand said—",
      narration="He checked his list, looked confused, and said—",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="\"4A's been empty\nfor *six years*.\nNo one's rented it.\"",
      narration="Four A's been empty for six years. No one's rented it.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I told him someone\nwas clearly living there.",
      narration="I told him someone was clearly living there.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="He just shrugged.\nSaid the door\n*sticks funny*. That's all.",
      narration="He just shrugged. Said the door sticks funny. That's all.",
      query=Q["door_normal"], footage_key="door_normal"),
 dict(kind="beat", text="I stopped looking at it after that.\nKept my eyes forward.\n*Walked fast*.",
      narration="I stopped looking at it after that. Kept my eyes forward. Walked fast.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="For two months,\nnothing happened.\nI almost forgot.",
      narration="For two months, nothing happened. I almost forgot.",
      query=Q["bedroom_night"], footage_key="bedroom_night"),
 dict(kind="beat", text="But some nights,\nI'd still hear it\nthrough the wall.",
      narration="But some nights, I'd still hear it through the wall.",
      query=Q["bedroom_night"], footage_key="bedroom_night"),
 dict(kind="beat", text="Not knocking.\nJust breathing.\n*In time with mine.*",
      narration="Not knocking. Just breathing. In time with mine.",
      query=Q["bedroom_night"], footage_key="bedroom_night"),
 dict(kind="beat", text="By the third night,\nI'd learned to keep\nmy own breathing quiet.",
      narration="By the third night, I'd learned to keep my own breathing quiet.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="It always\nheard me\n*anyway*.",
      narration="It always heard me anyway.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Then, last Tuesday,\nat exactly *3 AM* —", kicker="THE NIGHT",
      narration="Then, last Tuesday, at exactly three A M—",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="Three slow knocks.\nNot on my door.\n*On the wall* between our apartments.",
      narration="Three slow knocks. Not on my door. On the wall between our apartments.",
      query=Q["bedroom_night"], footage_key="bedroom_night"),
 dict(kind="beat", text="I lay there\na long time\nbefore I moved.",
      narration="I lay there a long time before I moved.",
      query=Q["bedroom_night"], footage_key="bedroom_night"),
 dict(kind="beat", text="Eventually, I got up.\nI opened my door.",
      narration="Eventually, I got up. I opened my door.",
      query=Q["door_normal"], footage_key="door_normal"),
 dict(kind="beat", text="4A's door was open.\n*All the way*, this time.",
      narration="Four A's door was open. All the way, this time.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="I stepped closer.\nThe apartment inside\nwas completely empty.",
      narration="I stepped closer. The apartment inside was completely empty.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="No furniture. No dust.\nLike no one had\never lived there at all.",
      narration="No furniture. No dust. Like no one had ever lived there at all.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Except one thing.\nTheir *peephole*.",
      narration="Except one thing. Their peephole.",
      query=Q["door_normal"], footage_key="door_normal"),
 dict(kind="beat", text="It was facing the wrong way.\nPointed *into*\ntheir own empty apartment.",
      narration="It was facing the wrong way. Pointed into their own empty apartment.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Aimed at a single spot\non the floor.\nRight where someone would stand.",
      narration="Aimed at a single spot on the floor. Right where someone would stand.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="*Waiting for\nsomeone to move in.*",
      narration="Waiting for someone to move in.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I backed out of that apartment\nand didn't stop walking\nuntil I was outside.",
      narration="I backed out of that apartment and didn't stop walking until I was outside.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I didn't sleep\nin 4B\nagain that night.",
      narration="I didn't sleep in four B again that night.",
      query=Q["bedroom_night"], footage_key="bedroom_night"),
 dict(kind="beat", text="Last night,\nI caught my reflection\nin the hallway window.",
      narration="Last night, I caught my reflection in the hallway window.",
      query=Q["window_reflection"], footage_key="window_reflection"),
 dict(kind="end", text="It stood still.\nA half-second\n*after* I did.",
      question="Would you still open the door?",
      narration="It stood still. A half second after I did.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
]

CAPTION = (
    "😳 \"The Neighbor Who Wasn't\" — a Suspense Ahead original.\n\n"
    "Six months in a new apartment. One door across the hall that's always "
    "open a crack. And a neighbor who seems to know what you're about to do "
    "before you do it.\n\n"
    "👇 Would you have opened that door? Tell us where you'd have stopped.\n\n"
    "🔁 Share this with someone who overthinks every apartment building they've ever lived in.\n\n"
    "🎭 SUSPENSE AHEAD — original horror, every week."
)

if __name__ == "__main__":
    build(BEATS, str(OUT_MP4), str(WORK_DIR), STATE, LOCK,
          VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)
