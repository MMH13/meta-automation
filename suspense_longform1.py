# -*- coding: utf-8 -*-
"""Suspense Ahead — first 3+ minute long-form horror narration, Lewis voice,
true 9:16. Original story ("The Neighbor Who Wasn't"), no stock footage —
original illustrated scenes (house/hallway/door/window/clock) rotate with
text-forward beats for visual variety across the runtime, per the user's
explicit choice.

This is a genuinely long unattended build: ~32 narration segments, each
requiring its own Voicebox TTS call. Based on pacing observed on this
machine (CPU-bound TTS, several minutes per segment at times), expect this
to take a long time - potentially 1-2+ hours. Single locked process,
resumable state, same pattern as every prior batch on this project.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from image_reel_suspense import (sr_hook, sr_beat, sr_end, sr_scene_house,
                                 sr_scene_hallway, sr_scene_door, sr_scene_window,
                                 sr_scene_clock)
from voicebox_client import ensure_profile, speak

_HERE = Path(__file__).parent
OUT_DIR = _HERE / "images" / "suspense_longform1"
OUT_DIR.mkdir(parents=True, exist_ok=True)
STATE = _HERE / "suspense_longform1_state.json"
LOCK = _HERE / "suspense_longform1.lock"
OUT_MP4 = "images/suspense_longform1.mp4"

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.3, 0.5

TITLE = "The Neighbor Who Wasn't"

# (kind, kwargs-for-render, narration)
# kind: hook | beat | end | house | hallway | door | window | clock
BEATS = [
 ("house", dict(caption="Six months ago,\nI moved into apartment *4B*.", lit_window=True),
  "Six months ago, I moved into apartment four B."),
 ("beat", dict(text="It was quiet.\nAffordable.\n*Perfect.*"),
  "It was quiet. Affordable. Perfect."),
 ("hallway", dict(caption="The only strange thing\nwas *4A*, right across the hall."),
  "The only strange thing was four A, right across the hall."),
 ("door", dict(caption="Every time I left for work,\ntheir door was *open a crack*.", ajar=True),
  "Every time I left for work, their door was open a crack."),
 ("beat", dict(text="Just enough to see someone\nstanding there,\nwatching me *lock up*."),
  "Just enough to see someone standing there, watching me lock up."),
 ("beat", dict(text="I never saw a face.\nJust a shape,\nstill, in the dark gap."),
  "I never saw a face. Just a shape, still, in the dark gap."),
 ("beat", dict(text="At first I thought nothing of it.\nNew city.\n*New nerves.*"),
  "At first I thought nothing of it. New city. New nerves."),
 ("beat", dict(text="Then I started\nnoticing the *timing*."),
  "Then I started noticing the timing."),
 ("clock", dict(caption="Whatever I did,\nthey did it *first*.", hour=8, minute=15),
  "Whatever I did, they did it first."),
 ("beat", dict(text="I'd reach for my keys —\nthe door across the hall\nwould already be open."),
  "I'd reach for my keys. The door across the hall would already be open."),
 ("beat", dict(text="I'd come home late —\nit would already be cracked open,\n*waiting*."),
  "I'd come home late. It would already be cracked open, waiting."),
 ("beat", dict(text="Like they always knew,\n*before I did*."),
  "Like they always knew, before I did."),
 ("beat", dict(text="I tried recording it\non my phone once."),
  "I tried recording it on my phone once."),
 ("beat", dict(text="The video showed an empty hallway.\nNo door.\n*No gap at all.*"),
  "The video showed an empty hallway. No door. No gap at all."),
 ("beat", dict(text="Just my own breathing,\nand one sound\nunderneath it."),
  "Just my own breathing, and one sound underneath it."),
 ("beat", dict(text="Footsteps.\n*Stopping exactly\nwhen mine did.*"),
  "Footsteps. Stopping exactly when mine did."),
 ("beat", dict(text="I asked the building manager\nabout 4A."),
  "I asked the building manager about four A."),
 ("beat", dict(text="He checked his list,\nlooked confused,\nand said—"),
  "He checked his list, looked confused, and said—"),
 ("beat", dict(text="\"4A's been empty\nfor *six years*.\nNo one's rented it.\""),
  "Four A's been empty for six years. No one's rented it."),
 ("beat", dict(text="I told him someone\nwas clearly living there."),
  "I told him someone was clearly living there."),
 ("beat", dict(text="He just shrugged.\nSaid the door\n*sticks funny*. That's all."),
  "He just shrugged. Said the door sticks funny. That's all."),
 ("beat", dict(text="I stopped looking at it after that.\nKept my eyes forward.\n*Walked fast*."),
  "I stopped looking at it after that. Kept my eyes forward. Walked fast."),
 ("beat", dict(text="For two months,\nnothing happened.\nI almost forgot."),
  "For two months, nothing happened. I almost forgot."),
 ("beat", dict(text="But some nights,\nI'd still hear it\nthrough the wall."),
  "But some nights, I'd still hear it through the wall."),
 ("beat", dict(text="Not knocking.\nJust breathing.\n*In time with mine.*"),
  "Not knocking. Just breathing. In time with mine."),
 ("beat", dict(text="By the third night,\nI'd learned to keep\nmy own breathing quiet."),
  "By the third night, I'd learned to keep my own breathing quiet."),
 ("beat", dict(text="It always\nheard me\n*anyway*."),
  "It always heard me anyway."),
 ("clock", dict(caption="Then, last Tuesday,\nat exactly *3 AM* —", hour=3, minute=0),
  "Then, last Tuesday, at exactly three A M—"),
 ("beat", dict(text="Three slow knocks.\nNot on my door.\n*On the wall* between our apartments."),
  "Three slow knocks. Not on my door. On the wall between our apartments."),
 ("beat", dict(text="I lay there\na long time\nbefore I moved."),
  "I lay there a long time before I moved."),
 ("beat", dict(text="Eventually, I got up.\nI opened my door."),
  "Eventually, I got up. I opened my door."),
 ("door", dict(caption="4A's door was open.\n*All the way*, this time.", ajar=True),
  "Four A's door was open. All the way, this time."),
 ("beat", dict(text="I stepped closer.\nThe apartment inside\nwas completely empty."),
  "I stepped closer. The apartment inside was completely empty."),
 ("beat", dict(text="No furniture. No dust.\nLike no one had\never lived there at all."),
  "No furniture. No dust. Like no one had ever lived there at all."),
 ("window", dict(caption="Except one thing.\nTheir *peephole*.", silhouette=False),
  "Except one thing. Their peephole."),
 ("beat", dict(text="It was facing the wrong way.\nPointed *into*\ntheir own empty apartment."),
  "It was facing the wrong way. Pointed into their own empty apartment."),
 ("beat", dict(text="Aimed at a single spot\non the floor.\nRight where someone would stand."),
  "Aimed at a single spot on the floor. Right where someone would stand."),
 ("beat", dict(text="*Waiting for\nsomeone to move in.*"),
  "Waiting for someone to move in."),
 ("beat", dict(text="I backed out of that apartment\nand didn't stop walking\nuntil I was outside."),
  "I backed out of that apartment and didn't stop walking until I was outside."),
 ("beat", dict(text="I didn't sleep\nin 4B\nagain that night."),
  "I didn't sleep in four B again that night."),
 ("beat", dict(text="Last night,\nI caught my reflection\nin the hallway window."),
  "Last night, I caught my reflection in the hallway window."),
 ("end", dict(text="It stood still.\nA half-second\n*after* I did.",
              question="Would you still open the door?"),
  "It stood still. A half second after I did."),
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


def _acquire_lock():
    import os
    if LOCK.is_file():
        try:
            other = int(LOCK.read_text().strip())
            os.kill(other, 0)
            raise SystemExit(f"Already running (pid {other}).")
        except (ValueError, ProcessLookupError, OSError):
            pass
    LOCK.write_text(str(os.getpid()))


def _release_lock():
    LOCK.unlink(missing_ok=True)


def _load_state():
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}


def _save_state(s):
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def _tts(text, out_mp3):
    pid = ensure_profile("SUS-Narrator-Lewis", "kokoro", "bm_lewis",
                         description="deep, ominous, deliberate horror narrator")
    wav = out_mp3.with_suffix(".wav")
    speak(pid, text, str(wav), engine="kokoro")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-b:a", "192k",
                    str(out_mp3)], check=True, capture_output=True, timeout=180)
    wav.unlink(missing_ok=True)


def _dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], check=True, capture_output=True, text=True)
    return float(r.stdout.strip())


def _clip(png, mp3, out):
    d = _dur(mp3) + TAIL
    n = max(int(d * FPS), 1)
    vf = (f"scale={W*2}:{H*2},"
          f"zoompan=z='min(1+0.05*on/{n},1.05)':d={n}"
          f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
          f"fade=t=in:st=0:d={FADE},fade=t=out:st={max(d-FADE,0):.3f}:d={FADE},"
          f"format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(mp3),
                    "-filter_complex", f"[0:v]{vf}[v];[1:a]apad=pad_dur={TAIL}[a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium",
                    "-crf", "20", "-r", str(FPS), "-c:a", "aac", "-b:a", "160k",
                    "-ar", "48000", "-ac", "2", "-t", f"{d:.3f}", str(out)],
                   check=True, capture_output=True, timeout=900)
    return d


_RENDER = {"hook": sr_hook, "beat": sr_beat, "end": sr_end, "house": sr_scene_house,
           "hallway": sr_scene_hallway, "door": sr_scene_door, "window": sr_scene_window,
           "clock": sr_scene_clock}


def build():
    state = _load_state()
    total = state.get("_total_so_far", 0.0)
    clips_done = state.get("_clips", [])

    for i, (kind, kwargs, narration) in enumerate(BEATS, 1):
        key = f"b{i:02d}"
        rec = state.setdefault(key, {})
        png = OUT_DIR / f"{key}.png"
        mp3 = OUT_DIR / f"{key}.mp3"
        clip = OUT_DIR / f"{key}.mp4"

        if rec.get("done") and clip.is_file():
            print(f"  {key}: already built, skipping")
            if str(clip) not in clips_done:
                clips_done.append(str(clip))
            continue

        fn = _RENDER[kind]
        if kind in ("hook", "beat", "end"):
            fn(kwargs.get("text", ""), str(png), **{k: v for k, v in kwargs.items() if k != "text"})
        else:
            fn(str(png), **kwargs)
        _tts(narration, mp3)
        d = _clip(png, mp3, clip)
        total += d
        clips_done.append(str(clip))
        rec["done"] = True
        rec["duration"] = round(d, 2)
        state["_total_so_far"] = total
        state["_clips"] = clips_done
        _save_state(state)
        print(f"  {key}/{len(BEATS)}  {d:.1f}s  (running total {total:.1f}s)  {narration[:45]}")

    lst_path = OUT_DIR / "concat.txt"
    lst_path.write_text("\n".join(f"file '{Path(c).resolve().as_posix()}'" for c in clips_done),
                        encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst_path),
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
                    "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                    "-movflags", "+faststart", OUT_MP4], check=True, capture_output=True, timeout=1800)
    print(f"\n=> {OUT_MP4}  total narration ~{total:.1f}s")
    return OUT_MP4


if __name__ == "__main__":
    _acquire_lock()
    try:
        build()
    finally:
        _release_lock()
