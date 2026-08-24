# -*- coding: utf-8 -*-
"""Top Movie Reviews — 9:16 poster-montage reel pipeline.

Each beat renders a complete frame via image_reel_movie_poster.py (blurred
poster backdrop + sharp TMDB poster + brand text), then ffmpeg applies a slow
Ken-Burns push and muxes Onyx narration. Same lock/resumable-state/retry
pattern as the other video pipelines in this repo.

EDITORIAL USE: posters are fetched through tmdb.py, shown inside our own
review layout with a visible credit line, never reposted standalone.

beats: list of dicts
  {"kind": "hook",   "text", "narration"}
  {"kind": "poster", "title", "year", "text", "narration", "kicker"}
  {"kind": "end",    "text", "narration", "question"}
"""
import json
import os
import subprocess
from pathlib import Path

from image_reel_movie_poster import mvp_hook, mvp_poster, mvp_end
from tmdb import cache_poster
from voicebox_client import ensure_profile, speak

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.3, 0.55

VOICE_PROFILE = "TMR-Narrator-Onyx"
VOICE_ENGINE = "kokoro"
VOICE_ID = "am_onyx"
VOICE_DESC = "deep, cinematic, measured — film-critic authority"


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


def _load_state(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def _save_state(p, s):
    p.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


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


def _clip(png, mp3, out):
    """Slow Ken-Burns push on the composed frame + narration."""
    d = _dur(mp3) + TAIL
    n = max(int(d * FPS), 1)
    vf = (f"scale={W*2}:{H*2},"
          f"zoompan=z='min(1+0.06*on/{n},1.06)':d={n}"
          f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
          f"fade=t=in:st=0:d={FADE},fade=t=out:st={max(d-FADE,0):.3f}:d={FADE},"
          f"format=yuv420p")
    cmd = ["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", str(png), "-i", str(mp3),
           "-filter_complex", f"[0:v]{vf}[v];[1:a]apad=pad_dur={TAIL}[a]",
           "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium",
           "-crf", "20", "-r", str(FPS), "-c:a", "aac", "-b:a", "160k",
           "-ar", "48000", "-ac", "2", "-t", f"{d:.3f}", str(out)]
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
    poster_dir = work / "posters"
    poster_dir.mkdir(exist_ok=True)
    state_path, lock_path = Path(state_path), Path(lock_path)

    _acquire_lock(lock_path)
    try:
        state = _load_state(state_path)
        total = state.get("_total_so_far", 0.0)
        clips_done = state.get("_clips", [])
        profile = ensure_profile(VOICE_PROFILE, VOICE_ENGINE, VOICE_ID, description=VOICE_DESC)

        # Pre-fetch every poster up front: the hook/end cards build their
        # blurred collage + fanned strip out of the whole set, so they need
        # them before their own beat renders.
        all_posters = []
        for b in beats:
            if b["kind"] == "poster":
                p = cache_poster(b["title"], b.get("year"), out_dir=str(poster_dir))
                if p:
                    all_posters.append(p)
        print(f"  pre-fetched {len(all_posters)} poster(s) for collage")

        for i, b in enumerate(beats, 1):
            key = f"b{i:02d}"
            rec = state.setdefault(key, {})
            png = work / f"{key}.png"
            mp3 = work / f"{key}.mp3"
            clip = work / f"{key}.mp4"

            if rec.get("done") and clip.is_file():
                print(f"  {key}: already built, skipping")
                if str(clip) not in clips_done:
                    clips_done.append(str(clip))
                continue

            kind = b["kind"]
            if kind == "poster":
                poster = cache_poster(b["title"], b.get("year"), out_dir=str(poster_dir))
                print(f"    poster[{b['title']}] -> {poster}")
                mvp_poster(b["title"], b.get("year", ""), b["text"], str(png),
                           poster, kicker=b.get("kicker", ""))
            elif kind == "end":
                mvp_end(b["text"], str(png), question=b.get("question", ""),
                        posters=all_posters)
            else:
                mvp_hook(b["text"], str(png), posters=all_posters,
                         eyebrow=b.get("eyebrow", ""))

            _tts(profile, b["narration"], mp3)
            d = _clip(png, mp3, clip)
            total += d
            clips_done.append(str(clip))
            rec["done"] = True
            rec["duration"] = round(d, 2)
            state["_total_so_far"] = total
            state["_clips"] = clips_done
            _save_state(state_path, state)
            print(f"  {key}/{len(beats)}  {d:.1f}s  (total {total:.1f}s)  {b['narration'][:45]}")

        # Derive concat order from the beat list, NOT from clips_done's append
        # order: if only some beats are re-rendered (e.g. after clearing just
        # the hook from state), the rebuilt clips get appended at the end and
        # would otherwise be concatenated out of sequence.
        ordered = [work / f"b{i:02d}.mp4" for i in range(1, len(beats) + 1)]
        missing = [c.name for c in ordered if not c.is_file()]
        if missing:
            raise RuntimeError(f"missing clips before concat: {missing}")
        lst = work / "concat.txt"
        lst.write_text("\n".join(f"file '{c.resolve().as_posix()}'" for c in ordered),
                       encoding="utf-8")
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", str(out_mp4)],
                       check=True, capture_output=True, timeout=1800)
        print(f"\n=> {out_mp4}  total ~{total:.1f}s")
        return out_mp4
    finally:
        _release_lock(lock_path)
