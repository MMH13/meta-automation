# -*- coding: utf-8 -*-
"""Build + schedule Top Movie Reviews reels from tmr_reel_library.REELS.

Per reel:  render frames -> edge-tts per beat -> ffmpeg clips -> concat MP4
           -> upload to Facebook with video_state=SCHEDULED

Idempotent: a reel whose MP4 already exists is not re-rendered, and anything
already recorded in tmr_reels_state.json is not re-uploaded. Safe to re-run
after a crash.

  python tmr_build_reels.py --build-only          # render MP4s, no upload
  python tmr_build_reels.py --limit 4             # first 4 only
  python tmr_build_reels.py --upload              # build + schedule
"""
import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from aug_common import mkdir, render as _retry
from image_reel import reel_hook, reel_beat, reel_title, reel_end
from tmr_reel_library import REELS

_HERE = Path(__file__).parent
OUT = mkdir("images/reels/auto")
STATE = _HERE / "tmr_reels_state.json"

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.28, 0.45

# 2 reels/day at these UTC hours, starting Jul 31
START = datetime(2026, 7, 31, tzinfo=timezone.utc)
SLOTS = [11, 21]          # US morning / US prime
_FN = {"hook": reel_hook, "beat": reel_beat, "title": reel_title, "end": reel_end}


def _load_state():
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {}


def _save_state(s):
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


_VB_PROFILE = None


def _voicebox_profile():
    """Resolve (and create if needed) this page's narration profile once."""
    global _VB_PROFILE
    if _VB_PROFILE is None:
        from voicebox_client import ensure_profile
        from voice_profiles import voice_for
        v = voice_for("top-movie-reviews")
        _VB_PROFILE = (ensure_profile(v["profile"], v["engine"], v["voice_id"],
                                      description=v["tone"]), v["engine"])
    return _VB_PROFILE


def _tts(text, out_mp3, voice=None):
    """Narrate via Voicebox (local Kokoro/Qwen). `voice` is ignored — kept so
    older library entries carrying an edge-tts voice name still load."""
    from voicebox_client import speak
    pid, engine = _voicebox_profile()
    wav = out_mp3.with_suffix(".wav")
    speak(pid, text, str(wav), engine=engine)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(wav),
                    "-b:a", "192k", str(out_mp3)],
                   check=True, capture_output=True, timeout=180)
    wav.unlink(missing_ok=True)
    if not out_mp3.is_file() or out_mp3.stat().st_size == 0:
        raise RuntimeError(f"no audio for: {text[:50]}")


def _dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], check=True, capture_output=True, text=True)
    return float(r.stdout.strip())


def _clip(png, mp3, out_mp4):
    d = _dur(mp3) + TAIL
    n = max(int(d * FPS), 1)
    vf = (f"scale={W*2}:{H*2},"
          f"zoompan=z='min(1+0.07*on/{n},1.07)':d={n}"
          f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
          f"fade=t=in:st=0:d={FADE},fade=t=out:st={max(d-FADE,0):.3f}:d={FADE},"
          f"format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(mp3),
                    "-filter_complex", f"[0:v]{vf}[v];[1:a]apad=pad_dur={TAIL}[a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium",
                    "-crf", "20", "-r", str(FPS), "-c:a", "aac", "-b:a", "160k",
                    "-ar", "48000", "-ac", "2", "-t", f"{d:.3f}", str(out_mp4)],
                   check=True, capture_output=True, timeout=900)
    return d


def build_reel(spec):
    """Render one reel to MP4. Returns (path, duration)."""
    rid = spec["id"]
    mp4 = _HERE / OUT / f"{rid}.mp4"
    if mp4.is_file() and mp4.stat().st_size > 100_000:
        return str(mp4.relative_to(_HERE)).replace("\\", "/"), _dur(mp4)

    variant, voice = spec.get("variant", "violet"), spec.get("voice", "en-US-AndrewNeural")
    work = Path(tempfile.mkdtemp(prefix=f"{rid}_"))
    clips, total = [], 0.0
    try:
        for i, (kind, kw, narration) in enumerate(spec["frames"], 1):
            png = _HERE / OUT / f"{rid}_{i:02d}.png"
            if not png.is_file():
                fn, kw = _FN[kind], dict(kw)
                kw["variant"] = variant
                if kind == "title":
                    _retry(fn, kw.pop("top"), kw.pop("big"), kw.pop("bottom"), str(png), **kw)
                else:
                    _retry(fn, kw.pop("text"), str(png), **kw)
            mp3 = work / f"{i:02d}.mp3"
            _tts(narration, mp3, voice)
            clip = work / f"{i:02d}.mp4"
            total += _clip(png, mp3, clip)
            clips.append(clip)

        lst = work / "c.txt"
        lst.write_text("\n".join(f"file '{c.as_posix()}'" for c in clips), encoding="utf-8")
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", str(mp4)],
                       check=True, capture_output=True, timeout=900)
        return str(mp4.relative_to(_HERE)).replace("\\", "/"), total
    finally:
        for f in work.glob("*"):
            f.unlink(missing_ok=True)
        work.rmdir()


def slot_for(index):
    """Reel n -> its scheduled UTC datetime (2/day from START)."""
    day, which = divmod(index, len(SLOTS))
    return START + timedelta(days=day, hours=SLOTS[which])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upload", action="store_true")
    ap.add_argument("--build-only", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--start-index", type=int, default=0)
    args = ap.parse_args()

    # Fail fast and loudly rather than burning through the library writing
    # error records, and hold the backend open for the whole batch.
    from voicebox_client import require_alive
    require_alive()

    state = _load_state()
    todo = REELS[args.start_index:]
    if args.limit:
        todo = todo[:args.limit]

    for spec in todo:
        rid = spec["id"]
        idx = next(i for i, r in enumerate(REELS) if r["id"] == rid)
        when = slot_for(idx)
        rec = state.setdefault(rid, {})
        try:
            path, dur = build_reel(spec)
            rec.update({"mp4": path, "duration": round(dur, 1),
                        "scheduled_for": when.isoformat()})
            print(f"{rid}: built {dur:5.1f}s -> {path}  (slot {when:%Y-%m-%d %H:%MZ})")
        except Exception as e:
            print(f"{rid}: BUILD FAILED — {type(e).__name__}: {str(e)[:160]}")
            rec["error"] = str(e)[:200]
            _save_state(state)
            continue

        if args.upload and not rec.get("video_id"):
            if when <= datetime.now(timezone.utc) + timedelta(minutes=15):
                print(f"{rid}: slot is in the past/too soon — skipping upload")
            else:
                try:
                    from publish_reel import publish
                    r = publish("top-movie-reviews", path, spec["caption"],
                                schedule_ts=when.timestamp())
                    rec.update(r)
                    print(f"{rid}: SCHEDULED {r.get('video_id')} for {r.get('publish_at_utc')}")
                except Exception as e:
                    print(f"{rid}: UPLOAD FAILED — {str(e)[:200]}")
                    rec["upload_error"] = str(e)[:200]
        _save_state(state)

    _save_state(state)
    built = sum(1 for v in state.values() if v.get("mp4"))
    sched = sum(1 for v in state.values() if v.get("video_id"))
    print(f"\nSTATE: {built} built, {sched} scheduled, {len(REELS)} in library")


if __name__ == "__main__":
    main()
