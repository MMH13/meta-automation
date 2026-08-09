# -*- coding: utf-8 -*-
"""Suspense Ahead — daily long-form, Aug 6. "The Inheritance" — original story,
stock-footage 1:1 pipeline."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_suspense_stock import build

_HERE = Path(__file__).parent
OUT_MP4 = _HERE / "images" / "suspense_daily" / "aug06_longform.mp4"
WORK_DIR = _HERE / "images" / "suspense_daily" / "aug06_longform_work"
STATE = _HERE / "suspense_daily_aug06_longform_state.json"
LOCK = _HERE / "suspense_daily_aug06_longform.lock"

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

Q = {
    "house_night": "house exterior night window light dark",
    "office_interior": "office desk lamp night empty",
    "dread_dark_room": "dark room night subtle shadow moody",
    "basement_dark": "basement stairs dark night flashlight",
    "door_ajar": "door ajar dark room light gap",
    "empty_room": "empty room abandoned dark dust",
    "hallway_normal": "hallway night empty corridor",
    "hallway_exit": "walking fast hallway corridor dark",
    "mailboxes": "old mailboxes hallway apartment",
    "window_silhouette": "window curtain silhouette night rain",
    "window_reflection": "window reflection night glass dark",
}

BEATS = [
 dict(kind="hook", text="I inherited a house\nfrom a great-aunt I never met.",
      narration="I inherited a house from a great-aunt I never met.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The lawyer said\nshe left it to me specifically.",
      narration="The lawyer said she left it to me specifically.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Not to my mother.\nNot to anyone else in the family. *Just me.*",
      narration="Not to my mother. Not to anyone else in the family. Just me.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I drove out to see it.\nThree hours from the nearest town.",
      narration="I drove out to see it. Three hours from the nearest town.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The house was old,\nbut well maintained. *Too* well maintained.",
      narration="The house was old, but well maintained. Too well maintained.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The neighbors, what few there were,\nwouldn't quite look at me.",
      narration="The neighbors, what few there were, wouldn't quite look at me.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I stopped at the local store\nfor supplies.",
      narration="I stopped at the local store for supplies.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="The clerk asked which house.\nWhen I told her, she stopped smiling.",
      narration="The clerk asked which house. When I told her, she stopped smiling.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="\"*That's the Whitmore place,*\"\nshe said. Nothing else.",
      narration="That's the Whitmore place, she said. Nothing else.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I moved in that weekend.\nEverything felt fine, at first.",
      narration="I moved in that weekend. Everything felt fine, at first.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The house had a basement.\nThe door was locked. No key on the ring.",
      narration="The house had a basement. The door was locked. No key on the ring.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="I called a locksmith.\nHe canceled the appointment twice.",
      narration="I called a locksmith. He canceled the appointment twice.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="The third time,\nhe just stopped answering.",
      narration="The third time, he just stopped answering.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I decided to break\nthe lock myself.",
      narration="I decided to break the lock myself.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="The door led to stairs.\nOlder than the rest of the house.",
      narration="The door led to stairs. Older than the rest of the house.",
      query=Q["basement_dark"], footage_key="basement_dark"),
 dict(kind="beat", text="I went down\nwith just a flashlight.",
      narration="I went down with just a flashlight.",
      query=Q["basement_dark"], footage_key="basement_dark"),
 dict(kind="beat", text="The basement was one long room.\nShelves along every wall.",
      narration="The basement was one long room. Shelves along every wall.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Boxes. Photographs.\nPersonal items. *Dozens of them.*",
      narration="Boxes. Photographs. Personal items. Dozens of them.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Each box had a name written on it.\nNames I didn't recognize.",
      narration="Each box had a name written on it. Names I didn't recognize.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I opened one.\nA wallet, a watch, a pair of glasses.",
      narration="I opened one. A wallet, a watch, a pair of glasses.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="The ID inside was dated\n*thirty years ago*.",
      narration="The I D inside was dated thirty years ago.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I opened another box.\nSame thing. Different name, different decade.",
      narration="I opened another box. Same thing. Different name, different decade.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="At the very back,\none shelf was empty. *Waiting.*",
      narration="At the very back, one shelf was empty. Waiting.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I went back upstairs\nand called my mother.",
      narration="I went back upstairs and called my mother.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="I asked her what she knew\nabout great-aunt Eleanor.",
      narration="I asked her what she knew about great aunt Eleanor.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="She said the family\nnever talked about that side.",
      narration="She said the family never talked about that side.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Only that every generation,\none person \"took care of the house.\"",
      narration="Only that every generation, one person took care of the house.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I asked what that meant.\nShe said she didn't know. *She hung up.*",
      narration="I asked what that meant. She said she didn't know. She hung up.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="That night, I heard something\nmoving in the basement.",
      narration="That night, I heard something moving in the basement.",
      query=Q["basement_dark"], footage_key="basement_dark"),
 dict(kind="beat", text="The lock I'd broken\nwas fixed. *From the inside.*",
      narration="The lock I'd broken was fixed. From the inside.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="I didn't sleep.\nI sat by the door until morning.",
      narration="I didn't sleep. I sat by the door until morning.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="In daylight,\nI went back down.",
      narration="In daylight, I went back down.",
      query=Q["basement_dark"], footage_key="basement_dark"),
 dict(kind="beat", text="The empty shelf\nwasn't empty anymore.",
      narration="The empty shelf wasn't empty anymore.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="A small box, with a name\nwritten in handwriting *I recognized*.",
      narration="A small box, with a name written in handwriting I recognized.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="*My own.*",
      narration="My own.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I dropped the flashlight.\nIt didn't break, but the batteries went dead instantly.",
      narration="I dropped the flashlight. It didn't break, but the batteries went dead instantly.",
      query=Q["basement_dark"], footage_key="basement_dark"),
 dict(kind="beat", text="I ran upstairs\nand out the front door.",
      narration="I ran upstairs and out the front door.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I didn't stop\nuntil I reached the car.",
      narration="I didn't stop until I reached the car.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I drove straight back to the city.\nI haven't been back since.",
      narration="I drove straight back to the city. I haven't been back since.",
      query=Q["window_reflection"], footage_key="window_reflection"),
 dict(kind="beat", text="Last week, a letter arrived.\nNo return address.",
      narration="Last week, a letter arrived. No return address.",
      query=Q["mailboxes"], footage_key="mailboxes"),
 dict(kind="beat", text="Inside was a single key,\nand a note in *my own handwriting*.",
      narration="Inside was a single key, and a note in my own handwriting.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="\"*Someone has to take care\nof the house.*\"",
      narration="Someone has to take care of the house.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="I haven't opened\nthe box with my name on it.",
      narration="I haven't opened the box with my name on it.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="end", text="But I know\nit's only a matter of time.",
      question="Would you go back?",
      narration="But I know it's only a matter of time.",
      query=Q["window_reflection"], footage_key="window_reflection"),
]

CAPTION = (
    "😳 \"The Inheritance\" — a Suspense Ahead original.\n\n"
    "A house left to one person, in every generation, to \"take care of.\" "
    "A basement full of boxes with strangers' names on them. And one shelf "
    "left waiting — for a box with her own name on it.\n\n"
    "👇 Would you go back? Tell us honestly.\n\n"
    "🔁 Share this with someone who'd immediately sell an inherited house sight unseen.\n\n"
    "🎭 SUSPENSE AHEAD — original horror, every day."
)

if __name__ == "__main__":
    build(BEATS, str(OUT_MP4), str(WORK_DIR), STATE, LOCK,
          VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)
