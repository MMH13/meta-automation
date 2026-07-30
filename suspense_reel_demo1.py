# -*- coding: utf-8 -*-
"""Suspense Ahead — first real horror reel, Lewis narrator, true 9:16.
Original 6-beat story, ~30-40s (the reel-length format recommended over
5-10min long-form, per the platform research this accompanies)."""
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from image_reel_suspense import sr_hook, sr_beat, sr_end
from voicebox_client import ensure_profile, speak

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.28, 0.5

BEATS = [
    ("hook", "I live alone\non the third floor.",
     "I live alone on the third floor."),
    ("beat", "Every night at exactly 3 AM,\nI hear *three knocks* on my door.",
     "Every night at exactly three A M, I hear three knocks on my door."),
    ("beat", "Tonight, I finally\nopened it.",
     "Tonight, I finally opened it."),
    ("beat", "No one was there.\nJust a note taped to the frame.",
     "No one was there. Just a note, taped to the frame."),
    ("beat", "It said:\n*\"Wrong door. Sorry.\"*",
     "It said: wrong door. Sorry."),
    ("end", "It was dated\n*tomorrow.*",
     "It was dated tomorrow."),
]
QUESTION = "Would you still sleep tonight?"
OUT = "images/suspense_reel_demo1.mp4"


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
          f"zoompan=z='min(1+0.06*on/{n},1.06)':d={n}"
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


def build():
    work = Path(tempfile.mkdtemp(prefix="susreel_"))
    clips, total = [], 0.0
    try:
        for i, (kind, onscreen, narration) in enumerate(BEATS, 1):
            png = work / f"{i}.png"
            if kind == "hook":
                sr_hook(onscreen, str(png))
            elif kind == "end":
                sr_end(onscreen, str(png), question=QUESTION)
            else:
                sr_beat(onscreen, str(png))
            mp3 = work / f"{i}.mp3"
            _tts(narration, mp3)
            clip = work / f"{i}.mp4"
            d = _clip(png, mp3, clip)
            total += d
            clips.append(clip)
            print(f"  beat {i}/{len(BEATS)}  {d:.1f}s")
        lst = work / "c.txt"
        lst.write_text("\n".join(f"file '{c.as_posix()}'" for c in clips), encoding="utf-8")
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", OUT], check=True, capture_output=True, timeout=900)
    finally:
        for f in work.glob("*"):
            f.unlink(missing_ok=True)
        work.rmdir()
    print(f"\n-> {OUT}  ({total:.1f}s)")


if __name__ == "__main__":
    build()
