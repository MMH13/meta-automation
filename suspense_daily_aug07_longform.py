# -*- coding: utf-8 -*-
"""Suspense Ahead — daily long-form, Aug 7. "The Lighthouse Keeper" — original
story, stock-footage 1:1 pipeline."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_suspense_stock import build

_HERE = Path(__file__).parent
OUT_MP4 = _HERE / "images" / "suspense_daily" / "aug07_longform.mp4"
WORK_DIR = _HERE / "images" / "suspense_daily" / "aug07_longform_work"
STATE = _HERE / "suspense_daily_aug07_longform_state.json"
LOCK = _HERE / "suspense_daily_aug07_longform.lock"

VOICE_PROFILE = "SUS-Narrator-Lewis"
VOICE_ENGINE = "kokoro"
VOICE_ID = "bm_lewis"
VOICE_DESC = "deep, ominous, deliberate horror narrator"

Q = {
    "lighthouse_night": "lighthouse night dark ocean waves",
    "office_interior": "office desk lamp night empty",
    "dread_dark_room": "dark room night subtle shadow moody",
    "empty_room": "empty room abandoned dark dust",
    "window_silhouette": "window curtain silhouette night rain",
    "clock_night": "clock ticking macro night",
    "radio_static": "old radio static dark room",
    "stairs_dark": "spiral staircase dark night",
    "window_reflection": "window reflection night glass dark",
}

BEATS = [
 dict(kind="hook", text="I took a job\nas a lighthouse keeper.",
      narration="I took a job as a lighthouse keeper.",
      query=Q["lighthouse_night"], footage_key="lighthouse_night"),
 dict(kind="beat", text="Six weeks, completely alone.\nJust me and the light.",
      narration="Six weeks, completely alone. Just me and the light.",
      query=Q["lighthouse_night"], footage_key="lighthouse_night"),
 dict(kind="beat", text="The pay was good.\nGood enough not to ask too many questions.",
      narration="The pay was good. Good enough not to ask too many questions.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="The previous keeper\nleft without much notice.",
      narration="The previous keeper left without much notice.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="In the keeper's room,\nI found a shelf of logbooks.",
      narration="In the keeper's room, I found a shelf of logbooks.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Decades of entries.\nOne for every keeper before me.",
      narration="Decades of entries. One for every keeper before me.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="I started reading them\nmy first night.",
      narration="I started reading them my first night.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="Most entries were routine.\nWeather, maintenance, supply notes.",
      narration="Most entries were routine. Weather, maintenance, supply notes.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="But every log\nmentioned the same thing eventually.",
      narration="But every log mentioned the same thing eventually.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="A boat on the horizon.\nAlways at night. Always distant.",
      narration="A boat on the horizon. Always at night. Always distant.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="It never came closer.\nIt never left either.",
      narration="It never came closer. It never left either.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="Every keeper wrote the same line\nabout it, almost word for word.",
      narration="Every keeper wrote the same line about it, almost word for word.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="\"*Still there. Hasn't moved.*\"",
      narration="Still there. Hasn't moved.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I told myself\nit was just a fishing boat, anchored.",
      narration="I told myself it was just a fishing boat, anchored.",
      query=Q["lighthouse_night"], footage_key="lighthouse_night"),
 dict(kind="beat", text="My third night,\nI saw it myself.",
      narration="My third night, I saw it myself.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="Small light on the horizon.\n*Unmoving.*",
      narration="Small light on the horizon. Unmoving.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="I checked the radio\nto see if anyone was broadcasting nearby.",
      narration="I checked the radio to see if anyone was broadcasting nearby.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="Just static.\nThen, faintly, a voice.",
      narration="Just static. Then, faintly, a voice.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="Repeating the same phrase,\nover and over.",
      narration="Repeating the same phrase, over and over.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="\"*The light stays on.\nThe light stays on.*\"",
      narration="The light stays on. The light stays on.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="I turned it off\nand went back to the logs.",
      narration="I turned it off and went back to the logs.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="The last keeper's entries\ngot shorter as the weeks went on.",
      narration="The last keeper's entries got shorter as the weeks went on.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="Then, on day forty,\nthey just stopped.",
      narration="Then, on day forty, they just stopped.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="No explanation.\nNo resignation notice, like the office told me.",
      narration="No explanation. No resignation notice, like the office told me.",
      query=Q["empty_room"], footage_key="empty_room"),
 dict(kind="beat", text="The final entry\nwas one line.",
      narration="The final entry was one line.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="\"*It's closer tonight.*\"",
      narration="It's closer tonight.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I checked the date.\nForty days from his first entry.",
      narration="I checked the date. Forty days from his first entry.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="*I was on day thirty-eight.*",
      narration="I was on day thirty eight.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="That night,\nI climbed the spiral stairs to the light room.",
      narration="That night, I climbed the spiral stairs to the light room.",
      query=Q["stairs_dark"], footage_key="stairs_dark"),
 dict(kind="beat", text="Just to check\neverything was working.",
      narration="Just to check everything was working.",
      query=Q["stairs_dark"], footage_key="stairs_dark"),
 dict(kind="beat", text="From up there,\nthe boat looked closer than before.",
      narration="From up there, the boat looked closer than before.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="Close enough to see\nit had no crew on deck.",
      narration="Close enough to see it had no crew on deck.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="No lights inside it.\nJust the one light I'd been seeing for weeks.",
      narration="No lights inside it. Just the one light I'd been seeing for weeks.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="I went back down\nand locked every door in the keeper's house.",
      narration="I went back down and locked every door in the keeper's house.",
      query=Q["stairs_dark"], footage_key="stairs_dark"),
 dict(kind="beat", text="It didn't help.\nI heard the radio turn itself on.",
      narration="It didn't help. I heard the radio turn itself on.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="The same phrase,\nlouder this time.",
      narration="The same phrase, louder this time.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="\"*The light stays on.*\"",
      narration="The light stays on.",
      query=Q["radio_static"], footage_key="radio_static"),
 dict(kind="beat", text="Day thirty-nine,\nI barely slept.",
      narration="Day thirty nine, I barely slept.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I kept the logbook open on the desk,\nready to write the next entry.",
      narration="I kept the logbook open on the desk, ready to write the next entry.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="beat", text="Tonight\nis day forty.",
      narration="Tonight is day forty.",
      query=Q["clock_night"], footage_key="clock_night"),
 dict(kind="beat", text="The boat hasn't moved all week.\nBut tonight, it looks *closer*.",
      narration="The boat hasn't moved all week. But tonight, it looks closer.",
      query=Q["window_silhouette"], footage_key="window_silhouette"),
 dict(kind="beat", text="I keep thinking about\nthe last keeper's final line.",
      narration="I keep thinking about the last keeper's final line.",
      query=Q["dread_dark_room"], footage_key="dread_dark_room"),
 dict(kind="beat", text="I picked up the pen\nand started writing in the log myself.",
      narration="I picked up the pen and started writing in the log myself.",
      query=Q["office_interior"], footage_key="office_interior"),
 dict(kind="end", text="\"*It's closer tonight.*\"\nThe exact words, in my own handwriting.",
      question="Would you keep the light on?",
      narration="It's closer tonight. The exact words, in my own handwriting.",
      query=Q["window_reflection"], footage_key="window_reflection"),
]

CAPTION = (
    "😳 \"The Lighthouse Keeper\" — a Suspense Ahead original.\n\n"
    "Decades of keepers, all logging the same unmoving boat on the horizon. "
    "Every one of them wrote the exact same line before their entries "
    "stopped. Tonight is day forty.\n\n"
    "👇 Would you keep the light on? Tell us what you'd do.\n\n"
    "🔁 Share this with someone who thinks total isolation sounds peaceful.\n\n"
    "🎭 SUSPENSE AHEAD — original horror, every day."
)

if __name__ == "__main__":
    build(BEATS, str(OUT_MP4), str(WORK_DIR), STATE, LOCK,
          VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, VOICE_DESC)
