# -*- coding: utf-8 -*-
"""Suspense Ahead — daily long-form, Aug 5. "The New Hire" — original story,
stock-footage 1:1 pipeline."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_suspense_stock import build

_HERE = Path(__file__).parent
OUT_MP4 = _HERE / "images" / "suspense_daily" / "aug05_longform.mp4"
WORK_DIR = _HERE / "images" / "suspense_daily" / "aug05_longform_work"
STATE = _HERE / "suspense_daily_aug05_longform_state.json"
LOCK = _HERE / "suspense_daily_aug05_longform.lock"

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

Q = {
    "office_exterior": "office building night lights window",
    "office_interior": "office desk lamp night empty",
    "hallway_normal": "office hallway night empty corridor",
    "dread_dark_room": "dark room night subtle shadow moody",
    "empty_room": "empty room abandoned dark dust",
    "hallway_exit": "walking fast hallway corridor dark",
    "door_ajar": "elevator door open dark hallway",
    "window_reflection": "window reflection night glass dark",
}

BEATS = [
 dict(kind="hook", text="Three months ago,\na new hire joined our team.",
      narration="Three months ago, a new hire joined our team.",
      query=Q["office_exterior"], footage_key="office_exterior"),
 dict(kind="beat", text="Her name was *Elena*.\nQuiet, polite, good at her job.",
      narration="Her name was Elena. Quiet, polite, good at her job.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Nothing strange about her.\nExcept one thing.",
      narration="Nothing strange about her. Except one thing.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="She reminded me of someone.\nI couldn't place who.",
      narration="She reminded me of someone. I couldn't place who.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="By her second week,\nit started coming back to me.",
      narration="By her second week, it started coming back to me.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="Five years ago, we had another coworker.\n*Same first name.*",
      narration="Five years ago, we had another coworker. Same first name.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="She'd left suddenly.\nNo notice. No goodbye.",
      narration="She'd left suddenly. No notice. No goodbye.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="No one really talked about it.\nCompanies move on fast.",
      narration="No one really talked about it. Companies move on fast.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I told myself it was a coincidence.\nElena is a common enough name.",
      narration="I told myself it was a coincidence. Elena is a common enough name.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Then I noticed her coffee order.\n*Exactly* what the old Elena used to get.",
      narration="Then I noticed her coffee order. Exactly what the old Elena used to get.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Same seat in the break room.\nSame parking spot, unassigned.",
      narration="Same seat in the break room. Same parking spot, unassigned.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="I mentioned it to a coworker\nwho'd been here that long.",
      narration="I mentioned it to a coworker who'd been here that long.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="He went quiet.\nThen said he hadn't noticed. *But he looked rattled.*",
      narration="He went quiet. Then said he hadn't noticed. But he looked rattled.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I pulled the old employee directory\nfrom the shared drive.",
      narration="I pulled the old employee directory from the shared drive.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Old Elena's photo.\n*Same face. Not similar. The same.*",
      narration="Old Elena's photo. Same face. Not similar. The same.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I told myself\nold photos can be misleading.",
      narration="I told myself old photos can be misleading.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="That night, I stayed late\nto finish a report.",
      narration="That night, I stayed late to finish a report.",
      query=Q["office_exterior"], footage_key="office_exterior"),
 dict(kind="beat", text="The office was empty.\nJust me, and the hum of the AC.",
      narration="The office was empty. Just me, and the hum of the A C.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="New Elena's desk light\nwas still on.",
      narration="New Elena's desk light was still on.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I walked over.\nHer computer was logged in.",
      narration="I walked over. Her computer was logged in.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="One document was open.\nA resignation letter, half-written.",
      narration="One document was open. A resignation letter, half-written.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Dated *five years ago*.\nThe timestamp on the file was from before she was even hired.",
      narration="Dated five years ago. The timestamp on the file was from before she was even hired.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I backed away from the desk.\nMy hands were shaking.",
      narration="I backed away from the desk. My hands were shaking.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I checked the HR system\nfor the old Elena's exit paperwork.",
      narration="I checked the H R system for the old Elena's exit paperwork.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="There wasn't any.\nNo termination. No resignation on file.",
      narration="There wasn't any. No termination. No resignation on file.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Just one note:\n\"*Status: Pending.*\"",
      narration="Just one note: status, pending.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Pending,\nfor *five years*.",
      narration="Pending, for five years.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I heard the elevator ding\ndown the hall.",
      narration="I heard the elevator ding down the hall.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="No one else should have been\nin the building.",
      narration="No one else should have been in the building.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I grabbed my things\nand headed for the exit.",
      narration="I grabbed my things and headed for the exit.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="New Elena was standing\nby the elevator.",
      narration="New Elena was standing by the elevator.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="She smiled.\n\"*Working late too?*\"",
      narration="She smiled. Working late too?",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Her voice was warm.\nNormal. Completely ordinary.",
      narration="Her voice was warm. Normal. Completely ordinary.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="I said something back.\nI don't remember what.",
      narration="I said something back. I don't remember what.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="In the elevator,\nI watched the floor number.",
      narration="In the elevator, I watched the floor number.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="It was going up.\n*I'd pressed the lobby button.*",
      narration="It was going up. I'd pressed the lobby button.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="The doors opened\non our floor. *Again.*",
      narration="The doors opened on our floor. Again.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="Elena was already there.\nWaiting by her desk.",
      narration="Elena was already there. Waiting by her desk.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I don't remember\nleaving the elevator.",
      narration="I don't remember leaving the elevator.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I checked the window.\nIt was daylight when I arrived.",
      narration="I checked the window. It was daylight when I arrived.",
      query=Q["window_reflection"], footage_key="window_reflection"),
 dict(kind="beat", text="Now it was\n*pitch black*.",
      narration="Now it was pitch black.",
      query=Q["window_reflection"], footage_key="window_reflection"),
 dict(kind="beat", text="I don't know how long\nI was in that building.",
      narration="I don't know how long I was in that building.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="This morning, HR sent an email.\nWelcoming our newest hire.",
      narration="This morning, H R sent an email. Welcoming our newest hire.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="end", text="Her name is *Elena*.\nShe starts *Monday*.",
      question="Whose desk do you think she'll take?",
      narration="Her name is Elena. She starts Monday.",
      query=Q["window_reflection"], footage_key="window_reflection"),
]

CAPTION = (
    "😳 \"The New Hire\" — a Suspense Ahead original.\n\n"
    "A new coworker with the exact same name, same coffee order, same face "
    "as someone who vanished from the company five years ago without a "
    "trace. Tonight, another Elena is starting Monday.\n\n"
    "👇 Whose desk do you think she'll take next? Tell us below.\n\n"
    "🔁 Share this with someone who's had a coworker who felt a little too familiar.\n\n"
    "🎭 SUSPENSE AHEAD — original horror, every day."
)

if __name__ == "__main__":
    build(BEATS, str(OUT_MP4), str(WORK_DIR), STATE, LOCK,
          VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)
