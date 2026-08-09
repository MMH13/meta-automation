# -*- coding: utf-8 -*-
"""Suspense Ahead — daily long-form, Aug 4. "The Reset" — original story,
same stock-footage 1:1 pipeline as "The Neighbor Who Wasn't"."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_suspense_stock import build

_HERE = Path(__file__).parent
OUT_MP4 = _HERE / "images" / "suspense_daily" / "aug04_longform.mp4"
WORK_DIR = _HERE / "images" / "suspense_daily" / "aug04_longform_work"
STATE = _HERE / "suspense_daily_aug04_longform_state.json"
LOCK = _HERE / "suspense_daily_aug04_longform.lock"

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

Q = {
    "house_night": "house exterior night window light dark",
    "hallway_normal": "apartment hallway night empty corridor",
    "kitchen_dark": "kitchen sink dark night dripping faucet",
    "mailboxes": "old mailboxes hallway apartment",
    "dread_dark_room": "dark room night subtle shadow moody",
    "manager_office": "office desk lamp night empty",
    "empty_room": "empty room abandoned dark dust",
    "clock_night": "clock ticking macro night",
    "door_ajar": "door ajar dark room light gap",
    "window_silhouette": "window curtain silhouette night rain",
    "hallway_exit": "walking fast hallway corridor dark",
    "window_reflection": "window reflection night glass dark",
    "bedroom_dark": "dark bedroom night window moody",
}

BEATS = [
 dict(kind="hook", text="Three weeks ago,\nI moved into apartment *7C*.",
      narration="Three weeks ago, I moved into apartment seven C.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The rent was suspiciously low\nfor the location.",
      narration="The rent was suspiciously low for the location.",
      query=Q["house_night"], footage_key="house_night"),
 dict(kind="beat", text="The landlord said the previous tenant\n*left in a hurry*.",
      narration="The landlord said the previous tenant left in a hurry.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="I didn't think much of it.\nUntil the first week started.",
      narration="I didn't think much of it. Until the first week started.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="Monday, my kitchen faucet started dripping\n*at exactly midnight*.",
      narration="Monday, my kitchen faucet started dripping at exactly midnight.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="I fixed it myself.\nWent back to sleep.",
      narration="I fixed it myself. Went back to sleep.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="Tuesday, a package arrived\naddressed to *someone I'd never heard of*.",
      narration="Tuesday, a package arrived addressed to someone I'd never heard of.",
      query=Q["mailboxes"], footage_key="mailboxes"),
 dict(kind="beat", text="I brought it to the front desk.\nThey said it happens sometimes.",
      narration="I brought it to the front desk. They said it happens sometimes.",
      query=Q["mailboxes"], footage_key="mailboxes"),
 dict(kind="beat", text="Wednesday, I heard arguing through the wall.\nA couple, fighting about money.",
      narration="Wednesday, I heard arguing through the wall. A couple, fighting about money.",
      query=Q["bedroom_dark"], footage_key="bedroom_dark"),
 dict(kind="beat", text="I'd never met my neighbors.\nI didn't even know if anyone lived next door.",
      narration="I'd never met my neighbors. I didn't even know if anyone lived next door.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="By Thursday,\nI started writing it all down. Just in case.",
      narration="By Thursday, I started writing it all down. Just in case.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Friday, the faucet dripped again.\n*Midnight, exactly.*",
      narration="Friday, the faucet dripped again. Midnight, exactly.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="I lay awake,\ncounting the drips.",
      narration="I lay awake, counting the drips.",
      query=Q["bedroom_dark"], footage_key="bedroom_dark"),
 dict(kind="beat", text="The next morning,\nI went to the building office.",
      narration="The next morning, I went to the building office.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="I asked about\nthe previous tenant in 7C.",
      narration="I asked about the previous tenant in seven C.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="The manager checked her computer.\nHer face changed.",
      narration="The manager checked her computer. Her face changed.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="She said: \"That's strange.\nAccording to this, *no one's ever lived in 7C before you*.\"",
      narration="She said: that's strange. According to this, no one's ever lived in seven C before you.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I told her about the faucet,\nthe package, the arguing.",
      narration="I told her about the faucet, the package, the arguing.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="She went very quiet.\nThen asked me to describe it *exactly*.",
      narration="She went very quiet. Then asked me to describe it exactly.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="Faucet at midnight.\nA package for a stranger. An argument about money.",
      narration="Faucet at midnight. A package for a stranger. An argument about money.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="She opened a drawer\nand pulled out a folder.",
      narration="She opened a drawer and pulled out a folder.",
      query=Q["manager_office"], footage_key="manager_office"),
 dict(kind="beat", text="Six tenants.\n*Six identical complaint logs. Word for word.*",
      narration="Six tenants. Six identical complaint logs. Word for word.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Every single one, in their first week,\nwrote down the *same three things*.",
      narration="Every single one, in their first week, wrote down the same three things.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Faucet. Package. Argument.\nIn that order. Every time.",
      narration="Faucet. Package. Argument. In that order. Every time.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="The last tenant's file\nended after day seven.",
      narration="The last tenant's file ended after day seven.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="There was no forwarding address.\nNo move-out notice.",
      narration="There was no forwarding address. No move-out notice.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Just one line, in his own handwriting:\n\"*Someone else's turn now.*\"",
      narration="Just one line, in his own handwriting: someone else's turn now.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="That night, I couldn't sleep.\nI watched the *clock*.",
      narration="That night, I couldn't sleep. I watched the clock.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="11:58.\n*11:59.*",
      narration="Eleven fifty eight. Eleven fifty nine.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="At exactly midnight,\nthe faucet started dripping.",
      narration="At exactly midnight, the faucet started dripping.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="*Right on schedule.*",
      narration="Right on schedule.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="I got up.\nWalked to the kitchen in the dark.",
      narration="I got up. Walked to the kitchen in the dark.",
      query=Q["hallway_normal"], footage_key="hallway_normal"),
 dict(kind="beat", text="The cabinet under the sink was open.\n*I hadn't opened it.*",
      narration="The cabinet under the sink was open. I hadn't opened it.",
      query=Q["door_ajar"], footage_key="door_ajar"),
 dict(kind="beat", text="Inside, taped to the pipe,\nwas an old photograph.",
      narration="Inside, taped to the pipe, was an old photograph.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="A man I didn't recognize,\nstanding in this exact kitchen.",
      narration="A man I didn't recognize, standing in this exact kitchen.",
      query=Q["kitchen_dark"], footage_key="kitchen_dark"),
 dict(kind="beat", text="On the back, in pen:\n\"*Day one. It's already started.*\"",
      narration="On the back, in pen: day one. It's already started.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I looked up.\n*Someone was standing outside my window.*",
      narration="I looked up. Someone was standing outside my window.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="Third floor.\nThere's no ledge. No fire escape.",
      narration="Third floor. There's no ledge. No fire escape.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="By the time I grabbed my phone,\nthe window was empty.",
      narration="By the time I grabbed my phone to record it, the window was empty.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="I didn't sleep\nin 7C again that week.",
      narration="I didn't sleep in seven C again that week.",
      query=Q["hallway_exit"], footage_key="hallway_exit"),
 dict(kind="beat", text="I moved my mattress\nto the living room floor.",
      narration="I moved my mattress to the living room floor.",
      query=Q["bedroom_dark"], footage_key="bedroom_dark"),
 dict(kind="beat", text="It didn't help.\nThe argument through the wall came anyway.",
      narration="It didn't help. The argument through the wall came anyway.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Tonight\nis *day seven*.",
      narration="Tonight is day seven.",
      query=Q["window_reflection"], footage_key="window_reflection"),
 dict(kind="end", text="I keep thinking about that photograph.\n\"*Someone else's turn now.*\"",
      question="Whose turn do you think it is next?",
      narration="I keep thinking about that photograph. Someone else's turn now.",
      query=Q["window_reflection"], footage_key="window_reflection"),
]

CAPTION = (
    "😳 \"The Reset\" — a Suspense Ahead original.\n\n"
    "Every new tenant in apartment 7C writes down the exact same three "
    "complaints in their exact first week. Same order. Every time. Tonight "
    "is day seven for the current one.\n\n"
    "👇 Whose turn do you think it is next? Tell us in the comments.\n\n"
    "🔁 Share this with someone who's ever felt weird about a suspiciously cheap rental.\n\n"
    "🎭 SUSPENSE AHEAD — original horror, every day."
)

if __name__ == "__main__":
    build(BEATS, str(OUT_MP4), str(WORK_DIR), STATE, LOCK,
          VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)
