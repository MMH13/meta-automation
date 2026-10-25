# -*- coding: utf-8 -*-
"""Suspense Ahead - case-solving episodes: stock PHOTOS with Ken Burns motion
(zoom in/out, pan left/right) instead of stock video clips. Reuses the lock,
resumable-state, TTS and overlay machinery from video_suspense_stock.py; only
the per-beat clip builder and the visual fetch differ.

Beat dict: same shape as video_suspense_stock, plus optional
  "motion": "zoom_in" | "zoom_out" | "pan_left" | "pan_right"
(default cycles by beat index so consecutive beats never move the same way).
"""
import subprocess
from pathlib import Path

from stock_photos import fetch_photo
from voicebox_client import ensure_profile
from video_suspense_stock import (
    _acquire_lock, _release_lock, _load_state, _save_state, _tts, _dur,
    _RENDER, SW, SH, FPS, FADE, TAIL,
)

_MOTIONS = ["zoom_in", "pan_right", "zoom_out", "pan_left"]
UP = 2160  # upscale before zoompan so sub-pixel steps don't jitter


def _zoompan(motion, frames):
    n = max(frames, 1)
    if motion == "zoom_in":
        z, x, y = f"1+0.13*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif motion == "zoom_out":
        z, x, y = f"1.13-0.13*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif motion == "pan_left":
        z, x, y = "1.12", f"(iw-iw/zoom)*(1-on/{n})", "ih/2-(ih/zoom/2)"
    else:  # pan_right
        z, x, y = "1.12", f"(iw-iw/zoom)*(on/{n})", "ih/2-(ih/zoom/2)"
    return f"zoompan=z='{z}':x='{x}':y='{y}':d={n}:s={SW}x{SH}:fps={FPS}"


def _clip(photo, overlay_png, mp3, out, motion):
    d = _dur(mp3) + TAIL
    frames = int(d * FPS) + 2
    vf = (f"scale={UP}:{UP}:force_original_aspect_ratio=increase,crop={UP}:{UP},"
          f"{_zoompan(motion, frames)},"
          f"eq=brightness=-0.04:contrast=1.08:saturation=0.72,"
          f"fade=t=in:st=0:d={FADE},fade=t=out:st={max(d-FADE,0):.3f}:d={FADE},"
          f"format=yuv420p")
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-i", str(photo),
        "-loop", "1", "-i", str(overlay_png),
        "-i", str(mp3),
        "-filter_complex",
        f"[0:v]{vf}[base];[base][1:v]overlay=0:0:shortest=1[v];[2:a]apad=pad_dur={TAIL}[a]",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        "-t", f"{d:.3f}", str(out),
    ]
    last_err = None
    for attempt in range(3):
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=900)
            return d
        except subprocess.CalledProcessError as e:
            last_err = e
            print(f"    ffmpeg attempt {attempt+1}/3 failed (exit {e.returncode}), retrying...")
    raise last_err


def build(beats, out_mp4, work_dir, state_path, lock_path, voice_profile,
          voice_engine, voice_id, voice_desc):
    work = Path(work_dir)
    work.mkdir(parents=True, exist_ok=True)
    photo_dir = work / "photos"
    photo_dir.mkdir(exist_ok=True)
    state_path, lock_path = Path(state_path), Path(lock_path)

    _acquire_lock(lock_path)
    try:
        state = _load_state(state_path)
        total = state.get("_total_so_far", 0.0)
        used = set(state.get("_photo_ids", []))
        profile = ensure_profile(voice_profile, voice_engine, voice_id, description=voice_desc)

        for i, b in enumerate(beats, 1):
            key = f"b{i:02d}"
            rec = state.setdefault(key, {})
            png = work / f"{key}_overlay.png"
            mp3 = work / f"{key}.mp3"
            clip = work / f"{key}.mp4"

            if rec.get("done") and clip.is_file():
                print(f"  {key}: already built, skipping")
                continue

            fn = _RENDER[b["kind"]]
            if b["kind"] == "beat":
                fn(b["text"], str(png), kicker=b.get("kicker", ""))
            elif b["kind"] == "end":
                fn(b["text"], str(png), question=b.get("question", ""))
            else:
                fn(b["text"], str(png))

            photo_path = photo_dir / f"{key}.jpg"
            if not photo_path.is_file():
                _, pid = fetch_photo(b["query"], str(photo_path), exclude=used)
                state["_photo_ids"] = sorted(used)
                print(f"    photo[{key}]: pexels #{pid} <- {b['query']!r}")

            _tts(profile, b["narration"], mp3)
            motion = b.get("motion") or _MOTIONS[(i + len(str(out_mp4))) % len(_MOTIONS)]
            d = _clip(photo_path, png, mp3, clip, motion)
            total += d
            rec["done"] = True
            rec["duration"] = round(d, 2)
            rec["motion"] = motion
            state["_total_so_far"] = total
            _save_state(state_path, state)
            print(f"  {key}/{len(beats)}  {d:.1f}s  {motion:9s} (running total {total:.1f}s)  {b['narration'][:40]}")

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
