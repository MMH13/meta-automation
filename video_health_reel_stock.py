# -*- coding: utf-8 -*-
"""Health Daily — reusable 9:16 (1080x1920) reel pipeline using real Pexels
B-roll instead of solid-card backgrounds, mirroring video_suspense_stock.py.
Per beat: fetch/cache a scene-matched stock clip -> crop to 1080x1920 ->
loop/trim to narration length -> grade (subtle brand-cohesion tint) ->
overlay the transparent caption PNG (image_reel_health_overlay.py) -> TTS
via Bella -> mux audio -> concat everything. Same PID-lock/resumable-state
safety pattern as every other batch script in this project.

beats: list of dicts {"kind": "hook"|"beat"|"end", "text": "...",
                       "narration": "...", "query": "pexels search terms",
                       "footage_key": "optional reuse key", ...kwargs}
"""
import json
import os
import subprocess
from pathlib import Path

from image_reel_health_overlay import hdo_hook, hdo_beat, hdo_end
from stock_footage import fetch as fetch_footage
from voicebox_client import ensure_profile, speak

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.28, 0.5

_RENDER = {"hook": hdo_hook, "beat": hdo_beat, "end": hdo_end}

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


def _load_state(state_path):
    return json.loads(state_path.read_text(encoding="utf-8")) if state_path.is_file() else {}


def _save_state(state_path, s):
    state_path.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def _tts(profile, text, out_mp3):
    wav = out_mp3.with_suffix(".wav")
    speak(profile, text, str(wav), engine="kokoro")
    last_err = None
    for attempt in range(3):
        try:
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-b:a", "192k",
                            str(out_mp3)], check=True, capture_output=True, timeout=180)
            wav.unlink(missing_ok=True)
            return
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            last_err = e
            print(f"    ffmpeg (tts encode) attempt {attempt+1}/3 failed, retrying...")
    raise last_err


def _dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], check=True, capture_output=True, text=True)
    return float(r.stdout.strip())


def _clip(footage, overlay_png, mp3, out):
    """Crop footage to 1080x1920, loop/trim to narration length, grade, overlay
    the transparent caption PNG, mux the narration audio."""
    d = _dur(mp3) + TAIL
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
          f"crop={W}:{H},"
          f"eq=brightness=-0.02:contrast=1.05:saturation=0.9,"
          f"fade=t=in:st=0:d={FADE},fade=t=out:st={max(d-FADE,0):.3f}:d={FADE},"
          f"format=yuv420p")
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-stream_loop", "-1", "-i", str(footage),
        "-loop", "1", "-i", str(overlay_png),
        "-i", str(mp3),
        "-filter_complex",
        f"[0:v]{vf}[base];[base][1:v]overlay=0:0:shortest=1[v];[2:a]apad=pad_dur={TAIL}[a]",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        "-t", f"{d:.3f}", str(out),
    ]
    # ffmpeg has occasionally crashed with an access violation (exit
    # 3221226091) on an otherwise-valid input mid-batch — transient, not
    # reproducible on retry. Give it up to 2 extra tries before giving up.
    last_err = None
    for attempt in range(3):
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=900)
            return d
        except subprocess.CalledProcessError as e:
            last_err = e
            print(f"    ffmpeg attempt {attempt+1}/3 failed (exit {e.returncode}), retrying...")
    raise last_err


def build(beats, out_mp4, work_dir, state_path, lock_path):
    work = Path(work_dir)
    work.mkdir(parents=True, exist_ok=True)
    footage_dir = work / "footage"
    footage_dir.mkdir(exist_ok=True)
    state_path, lock_path = Path(state_path), Path(lock_path)

    _acquire_lock(lock_path)
    try:
        state = _load_state(state_path)
        total = state.get("_total_so_far", 0.0)
        clips_done = state.get("_clips", [])
        profile = ensure_profile(VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, description=VOICE_DESC)

        for i, b in enumerate(beats, 1):
            key = f"b{i:02d}"
            rec = state.setdefault(key, {})
            png = work / f"{key}_overlay.png"
            mp3 = work / f"{key}.mp3"
            clip = work / f"{key}.mp4"

            if rec.get("done") and clip.is_file():
                print(f"  {key}: already built, skipping")
                if str(clip) not in clips_done:
                    clips_done.append(str(clip))
                continue

            fn = _RENDER[b["kind"]]
            if b["kind"] == "beat":
                fn(b["text"], str(png), kicker=b.get("kicker", ""))
            elif b["kind"] == "end":
                fn(b["text"], str(png), question=b.get("question", ""))
            else:
                fn(b["text"], str(png))

            fkey = b.get("footage_key", key)
            footage_path = footage_dir / f"{fkey}.mp4"
            if not footage_path.is_file():
                path, hit = fetch_footage(b["query"], str(footage_path),
                                          min_width=800, min_duration=4)
                print(f"    footage[{fkey}]: pexels #{hit['id']} ({hit['duration']}s) <- {b['query']!r}")

            _tts(profile, b["narration"], mp3)
            d = _clip(footage_path, png, mp3, clip)
            total += d
            clips_done.append(str(clip))
            rec["done"] = True
            rec["duration"] = round(d, 2)
            state["_total_so_far"] = total
            state["_clips"] = clips_done
            _save_state(state_path, state)
            print(f"  {key}/{len(beats)}  {d:.1f}s  (running total {total:.1f}s)  {b['narration'][:45]}")

        # Derive concat order from the beat list, NOT from clips_done's
        # append order: if only some beats are re-rendered (e.g. after
        # clearing one beat from state to redo it), the rebuilt clips get
        # appended at the end and would be concatenated out of sequence.
        ordered = [work / f"b{i:02d}.mp4" for i in range(1, len(beats) + 1)]
        missing = [c.name for c in ordered if not c.is_file()]
        if missing:
            raise RuntimeError(f"missing clips before concat: {missing}")
        lst_path = work / "concat.txt"
        lst_path.write_text("\n".join(f"file '{c.resolve().as_posix()}'" for c in ordered),
                            encoding="utf-8")
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst_path),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", str(out_mp4)],
                       check=True, capture_output=True, timeout=1800)
        print(f"\n=> {out_mp4}  total narration ~{total:.1f}s")
        return out_mp4
    finally:
        _release_lock(lock_path)
