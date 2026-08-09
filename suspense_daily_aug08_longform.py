# -*- coding: utf-8 -*-
"""Suspense Ahead — daily long-form, Aug 8. "The Archive" — original story,
stock-footage 1:1 pipeline."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_suspense_stock import build

_HERE = Path(__file__).parent
OUT_MP4 = _HERE / "images" / "suspense_daily" / "aug08_longform.mp4"
WORK_DIR = _HERE / "images" / "suspense_daily" / "aug08_longform_work"
STATE = _HERE / "suspense_daily_aug08_longform_state.json"
LOCK = _HERE / "suspense_daily_aug08_longform.lock"

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

Q = {
    "library_night": "library archive room dark night books",
    "office_interior": "office desk lamp night empty",
    "dread_dark_room": "dark room night subtle shadow moody",
    "empty_room": "empty room abandoned dark dust",
    "clock_night": "clock ticking macro night",
    "hallway_normal": "hallway night empty corridor",
    "hallway_exit": "walking fast hallway corridor dark",
    "door_ajar": "door ajar dark room light gap",
    "window_reflection": "window reflection night glass dark",
    "stairs_dark": "spiral staircase dark night",
}

BEATS = [
 dict(kind="hook", text="I took a night job\ndigitizing old newspapers at the library.",
      narration="I took a night job digitizing old newspapers at the library.",
      query=Q["library_night"], footage_key="library_night"),
 dict(kind="beat", text="Just me,\na scanner, and boxes of archives.",
      narration="Just me, a scanner, and boxes of archives.",
      query=Q["library_night"], footage_key="library_night"),
 dict(kind="beat", text="The pay was decent.\nThe silence took getting used to.",
      narration="The pay was decent. The silence took getting used to.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="My job was simple.\nScan, catalog, move to the next box.",
      narration="My job was simple. Scan, catalog, move to the next box.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="The archive room\nwas in the basement.",
      narration="The archive room was in the basement.",
      query=Q["stairs_dark"], footage_key="stairs_dark"),
 dict(kind="beat", text="No windows.\nJust rows of shelves and old boxes.",
      narration="No windows. Just rows of shelves and old boxes.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="A few weeks in,\nI started noticing a pattern.",
      narration="A few weeks in, I started noticing a pattern.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Missing person articles.\nOne every few years, going back decades.",
      narration="Missing person articles. One every few years, going back decades.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Different names.\nDifferent decades. *Same details.*",
      narration="Different names. Different decades. Same details.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Always a young person.\nAlways vanished on a Thursday in August.",
      narration="Always a young person. Always vanished on a Thursday in August.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Always last seen\nnear the library.",
      narration="Always last seen near the library.",
      query=Q["library_night"], footage_key="library_night"),
 dict(kind="beat", text="I told myself\nit was coincidence. Small towns repeat patterns.",
      narration="I told myself it was coincidence. Small towns repeat patterns.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I kept scanning.\nBox after box.",
      narration="I kept scanning. Box after box.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Then I found\nan article from thirty years ago.",
      narration="Then I found an article from thirty years ago.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="A young woman.\nStudent, worked nights at the library.",
      narration="A young woman. Student, worked nights at the library.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Her photo\nlooked *exactly like me*.",
      narration="Her photo looked exactly like me.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Not similar.\n*The same face.*",
      narration="Not similar. The same face.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="The name under the photo\nwasn't mine. But everything else was.",
      narration="The name under the photo wasn't mine. But everything else was.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I checked the article date.\nAugust, thirty years ago exactly.",
      narration="I checked the article date. August, thirty years ago exactly.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="*This Thursday.*",
      narration="This Thursday.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="I told myself\nto stop scanning for the night.",
      narration="I told myself to stop scanning for the night.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I couldn't find the stairs\nback up right away.",
      narration="I couldn't find the stairs back up right away.",
      query=Q["stairs_dark"], footage_key="stairs_dark"),
 dict(kind="beat", text="The archive room\nfelt bigger than I remembered.",
      narration="The archive room felt bigger than I remembered.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Shelves I didn't recognize,\nfull of boxes with no labels.",
      narration="Shelves I didn't recognize, full of boxes with no labels.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I opened one.\nMore newspaper clippings. All the same missing-person story.",
      narration="I opened one. More newspaper clippings. All the same missing person story.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Different decades.\nSame face in every photo.",
      narration="Different decades. Same face in every photo.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="*My face.*",
      narration="My face.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I finally found the stairs\nand ran up them.",
      narration="I finally found the stairs and ran up them.",
      query=Q["stairs_dark"], footage_key="stairs_dark"),
 dict(kind="beat", text="The main library\nwas dark. Everyone had gone home.",
      narration="The main library was dark. Everyone had gone home.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="I grabbed my things\nand headed for the exit.",
      narration="I grabbed my things and headed for the exit.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="The front doors\nwere locked from the outside.",
      narration="The front doors were locked from the outside.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="I checked every exit.\nAll locked the same way.",
      narration="I checked every exit. All locked the same way.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I called the front desk number.\nNo one answered.",
      narration="I called the front desk number. No one answered.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I sat by the door\nand waited for morning.",
      narration="I sat by the door and waited for morning.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="At some point,\nI must have fallen asleep.",
      narration="At some point, I must have fallen asleep.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I woke up\nback in the archive room.",
      narration="I woke up back in the archive room.",
      query=Q["library_night"], footage_key="library_night"),
 dict(kind="beat", text="Sitting at the scanner.\nA new box already open in front of me.",
      narration="Sitting at the scanner. A new box already open in front of me.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Inside was\none folder.",
      narration="Inside was one folder.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="*My name*\non the label.",
      narration="My name on the label.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I opened it.\nA newspaper clipping, not yet published.",
      narration="I opened it. A newspaper clipping, not yet published.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="A photo of me, smiling,\nfrom a photo I don't remember taking.",
      narration="A photo of me, smiling, from a photo I don't remember taking.",
      query=Q["window_reflection"], footage_key="window_reflection"),
 dict(kind="beat", text="The headline space\nwas still blank.",
      narration="The headline space was still blank.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Waiting for a date.\n*This Thursday's date.*",
      narration="Waiting for a date. This Thursday's date.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="end", text="I put the folder back in the box.\n*I go back to work tonight.*",
      question="Would you go back to work?",
      narration="I put the folder back in the box. I go back to work tonight.",
      query=Q["window_reflection"], footage_key="window_reflection"),
]

CAPTION = (
    "😳 \"The Archive\" — a Suspense Ahead original.\n\n"
    "A night job digitizing old newspapers. A missing-person story that "
    "repeats every few decades, always the same face. Tonight is Thursday, "
    "and there's already a blank headline waiting.\n\n"
    "👇 Would you go back to work tonight?\n\n"
    "🔁 Share this with someone who's worked a night shift completely alone.\n\n"
    "🎭 SUSPENSE AHEAD — original horror, every day."
)

if __name__ == "__main__":
    build(BEATS, str(OUT_MP4), str(WORK_DIR), STATE, LOCK,
          VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)
