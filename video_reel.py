# -*- coding: utf-8 -*-
"""Top Movie Reviews — 9:16 reel assembly. Pre-rendered brand frames + English
TTS narration + ffmpeg, mirroring the Radio Deshal pipeline but portrait/English.

  frame PNG (1080x1920)  →  edge-tts MP3  →  ffmpeg clip (Ken Burns + fades)
  → concat → single MP4

Narration-only by design: there is no licensed music in this repo, and I won't
ship an unlicensed track. Add a bed from Meta Sound Collection in CapCut before
posting (Meta owns those licences, so Rights Manager can't claim them).

Usage:  python video_reel.py            # builds Reel 1
"""
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

_HERE = Path(__file__).parent
FPS = 30
W, H = 1080, 1920
FADE = 0.28
TAIL_PAD = 0.45          # trailing silence so cuts don't clip the last word
VOICE = "en-US-AndrewNeural"   # natural conversational US male; documentary fit
RATE = "-4%"             # a touch slower than default — narration needs room

# (frame file, narration for that frame)
REEL1 = [
    ("images/reels/r1_01_hook.png",
     "The scariest shark in movie history barely appears on screen."),
    ("images/reels/r1_02_beat.png",
     "In nineteen seventy five, Steven Spielberg had a full size mechanical shark."),
    ("images/reels/r1_03_beat.png",
     "In salt water, it failed almost every single day of the shoot."),
    ("images/reels/r1_04_beat.png",
     "So he did the only thing he could. He stopped showing it."),
    ("images/reels/r1_05_beat.png",
     "You get a fin. You get a barrel. Sometimes nothing at all. "
     "Just the water, and that score."),
    ("images/reels/r1_06_end.png",
     "And your imagination fills in something far worse than any rubber shark "
     "could have been. Fifty years later, horror directors are still copying "
     "a broken prop."),
]


def _tts(text, out_mp3):
    txt = out_mp3.with_suffix(".txt")
    txt.write_text(text, encoding="utf-8")
    subprocess.run(
        # --rate must use the = form: a bare "-4%" is parsed as a flag by argparse
        [sys.executable, "-m", "edge_tts", "--voice", VOICE, f"--rate={RATE}",
         "--file", str(txt), "--write-media", str(out_mp3)],
        check=True, capture_output=True, timeout=180)
    txt.unlink(missing_ok=True)
    if not out_mp3.is_file() or out_mp3.stat().st_size == 0:
        raise RuntimeError(f"TTS produced no audio for: {text[:60]}")


def _duration(media):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(media)], check=True, capture_output=True, text=True)
    return float(out.stdout.strip())


def _clip(png, mp3, out_mp4):
    """One frame + its narration → clip with a slow push and edge fades."""
    dur = _duration(mp3) + TAIL_PAD
    frames = max(int(dur * FPS), 1)
    vf = (
        f"scale={W*2}:{H*2},"
        f"zoompan=z='min(1+0.07*on/{frames},1.07)':d={frames}"
        f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
        f"fade=t=in:st=0:d={FADE},fade=t=out:st={max(dur-FADE,0):.3f}:d={FADE},"
        f"format=yuv420p"
    )
    subprocess.run(
        ["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(mp3),
         "-filter_complex", f"[0:v]{vf}[v];[1:a]apad=pad_dur={TAIL_PAD}[a]",
         "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
         "-t", f"{dur:.3f}", str(out_mp4)],
        check=True, capture_output=True, timeout=900)
    return dur


def build(scenes=REEL1, out_path="images/reels/reel1_jaws.mp4"):
    out = _HERE / out_path
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="reel_"))
    clips, total = [], 0.0
    try:
        for i, (png, line) in enumerate(scenes, 1):
            src = _HERE / png
            if not src.is_file():
                raise FileNotFoundError(src)
            mp3 = work / f"{i:02d}.mp3"
            _tts(line, mp3)
            clip = work / f"{i:02d}.mp4"
            d = _clip(src, mp3, clip)
            total += d
            clips.append(clip)
            print(f"  scene {i}: {d:5.2f}s  {Path(png).name}")

        listing = work / "concat.txt"
        listing.write_text(
            "\n".join(f"file '{c.as_posix()}'" for c in clips), encoding="utf-8")
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
             "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
             "-movflags", "+faststart", str(out)],
            check=True, capture_output=True, timeout=900)
        print(f"\nBUILT {out}  ({total:.1f}s, {out.stat().st_size/1e6:.1f} MB)")
        return str(out)
    finally:
        for f in work.glob("*"):
            f.unlink(missing_ok=True)
        work.rmdir()


if __name__ == "__main__":
    build()
