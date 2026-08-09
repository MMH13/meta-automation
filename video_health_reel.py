# -*- coding: utf-8 -*-
"""Health Daily — reusable 9:16 reel pipeline (bright clinical-trust brand,
Bella narration), mirroring video_suspense_reel.py's structure. Same safety
pattern: PID lock file, resumable per-beat state.

beats: list of dicts {"kind": "hook"|"beat"|"end", "text": "...",
                       "narration": "...", ...kwargs}
"""
import json
import os
import subprocess
from pathlib import Path

from image_reel_health import hd_hook, hd_beat, hd_end
from voicebox_client import ensure_profile, speak

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.28, 0.5

_RENDER = {"hook": hd_hook, "beat": hd_beat, "end": hd_end}

VOICE_PROFILE = "HD-Narrator-Bella"
VOICE_ENGINE = "kokoro"
VOICE_ID = "af_bella"
VOICE_DESC = "warm, unhurried, reassuring"


def _acquire_lock(lock_path):
    if lock_path.is_file():
        try:
            other = int(lock_path.read_text().strip())
            os.kill(other, 0)
            raise SystemExit(f"Already running (pid {other}).")
        except (ValueError, ProcessLookupError, OSError):
            pass
    lock_path.write_text(str(os.getpid()))


def _release_lock(lock_path):
    lock_path.unlink(missing_ok=True)


def _tts(text, out_mp3):
    pid = ensure_profile(VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, description=VOICE_DESC)
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


def build(beats, out_mp4, work_dir, state_path, lock_path):
    work = Path(work_dir)
    work.mkdir(parents=True, exist_ok=True)
    state_path, lock_path = Path(state_path), Path(lock_path)

    _acquire_lock(lock_path)
    try:
        state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.is_file() else {}
        total = state.get("_total_so_far", 0.0)
        clips_done = state.get("_clips", [])

        for i, b in enumerate(beats, 1):
            key = f"b{i:02d}"
            rec = state.setdefault(key, {})
            png = work / f"{key}.png"
            mp3 = work / f"{key}.mp3"
            clip = work / f"{key}.mp4"

            if rec.get("done") and clip.is_file():
                if str(clip) not in clips_done:
                    clips_done.append(str(clip))
                continue

            fn = _RENDER[b["kind"]]
            kwargs = {k: v for k, v in b.items() if k not in ("kind", "narration", "text")}
            fn(b.get("text", ""), str(png), **kwargs)

            _tts(b["narration"], mp3)
            d = _clip(png, mp3, clip)
            total += d
            clips_done.append(str(clip))
            rec["done"] = True
            rec["duration"] = round(d, 2)
            state["_total_so_far"] = total
            state["_clips"] = clips_done
            state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  {key}/{len(beats)}  {d:.1f}s  (running total {total:.1f}s)  {b['narration'][:45]}")

        lst_path = work / "concat.txt"
        lst_path.write_text("\n".join(f"file '{Path(c).resolve().as_posix()}'" for c in clips_done),
                            encoding="utf-8")
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst_path),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", str(out_mp4)],
                       check=True, capture_output=True, timeout=900)
        print(f"\n=> {out_mp4}  total narration ~{total:.1f}s")
        return out_mp4
    finally:
        _release_lock(lock_path)
