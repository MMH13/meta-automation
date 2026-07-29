# -*- coding: utf-8 -*-
"""Health Daily OS Week 1 — render + schedule all 42 items from hd_os_week1.json.

Images: branded health cards -> queue.json (FB photo + IG mirror, per the
        page's standing both-networks rule).
Reels:  9:16 health frames + Bella narration (Voicebox) + ffmpeg -> uploaded to
        Facebook with video_state=SCHEDULED so they publish PC-off.

Idempotent: existing MP4s aren't re-rendered, queue ids aren't duplicated, and
already-scheduled reels aren't re-uploaded (state in hd_reels_state.json).

  python hd_build_week1.py --images       # images only
  python hd_build_week1.py --reels        # build reels (no upload)
  python hd_build_week1.py --reels --upload
"""
import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from aug_common import mkdir, render as _retry
from image_health_light import health_fact, health_myth_fact
from image_reel_health import hd_hook, hd_beat, hd_end

_HERE = Path(__file__).parent
IMG_DIR = mkdir("images/hd_w1")
REEL_DIR = mkdir("images/hd_w1/reels")
STATE = _HERE / "hd_reels_state.json"
PLAN = _HERE / "hd_os_week1.json"
LOCK = _HERE / "hd_build_week1.lock"


def _acquire_lock():
    """Refuse to start if another instance is already running.

    A prior run got launched twice by accident (once via a backgrounded tool
    call that looked dead but wasn't, once manually) and both instances built
    and PUBLISHED the same reels independently -> 8 duplicate scheduled posts
    on the real page, caught and cleaned up by hand afterward. Each process
    only reads state.json once at startup, so two live processes can't see
    each other's progress and will both think a slot is unclaimed."""
    import os
    if LOCK.is_file():
        try:
            other_pid = int(LOCK.read_text().strip())
            os.kill(other_pid, 0)  # raises OSError if that pid is gone
            raise SystemExit(
                f"hd_build_week1 is already running (pid {other_pid}). "
                "Refusing to start a second instance — it would race the "
                "first one and can create duplicate scheduled posts.")
        except (ValueError, ProcessLookupError, OSError):
            pass  # stale lock (process gone or unreadable) — safe to take over
    LOCK.write_text(str(os.getpid()))


def _release_lock():
    LOCK.unlink(missing_ok=True)

FPS, W, H = 30, 1080, 1920
FADE, TAIL = 0.28, 0.45
VOICE_PROFILE = ("HD-Narrator-Bella", "kokoro", "af_bella")


# ── images ──────────────────────────────────────────────────────────────────
def render_image(item, out):
    """Map a plan item to the right branded card."""
    head = item["headline"]
    cat = item["category"]
    if item.get("framework") == "Myth → Truth":
        # headline is "MYTH: <claim>". Take the first 2 sentences of the value
        # paragraph for the FACT panel — one sentence leaves the card near-empty.
        myth = head.split(":", 1)[-1].strip().replace("\n", " ")
        value = item["caption"].split("\n\n")[1].replace("\n", " ").strip()
        parts = [s.strip() for s in value.split(". ") if s.strip()]
        fact = ". ".join(parts[:2]).rstrip(".") + "."
        _retry(health_myth_fact, myth, fact, out)
    else:
        _retry(health_fact, head, out, kicker=cat.upper(), emoji="")
    return out


def build_images(plan):
    q = json.loads((_HERE / "queue.json").read_text(encoding="utf-8"))
    items = q["items"]
    have = {i.get("id") for i in items}
    n = 0
    for it in plan:
        if it["post_type"] != "Image":
            continue
        stamp = it["date"][:10].replace("-", "") + it["date"][11:13]
        iid = f"hdw1-{stamp}"
        if iid + "-fb" in have:
            continue
        out = f"{IMG_DIR}/{stamp}.png"
        if not (_HERE / out).is_file():
            render_image(it, out)
        n += 1
        print(f"  image {iid} -> {out}")
        cap = it["caption"] + "\n\n" + " ".join(it["hashtags"]) + "\n\n" + it["disclaimer"]
        for net, typ, sfx in (("facebook", "photo", "-fb"), ("instagram", "image", "-ig")):
            items.append({"id": iid + sfx, "account": "health-daily", "network": net,
                          "type": typ, "message": cap, "image_url": out,
                          "when": it["date"], "status": "pending"})
    (_HERE / "queue.json").write_text(
        json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"IMAGES: {n} new (x2 networks), queue now {len(items)}")


# ── reels ───────────────────────────────────────────────────────────────────
_VB = None


def _profile():
    global _VB
    if _VB is None:
        from voicebox_client import ensure_profile
        name, eng, vid = VOICE_PROFILE
        _VB = (ensure_profile(name, eng, vid, description="warm, calm, reassuring"), eng)
    return _VB


def _tts(text, out_mp3):
    from voicebox_client import speak
    pid, eng = _profile()
    wav = out_mp3.with_suffix(".wav")
    speak(pid, text, str(wav), engine=eng)
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


def build_reels(plan, upload=False):
    from voicebox_client import require_alive
    require_alive()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}

    reels = [i for i in plan if i["post_type"] == "Reel"]
    for it in reels:
        stamp = it["date"][:10].replace("-", "") + it["date"][11:13]
        rid = f"hdw1-{stamp}"
        rec = state.setdefault(rid, {})
        mp4 = _HERE / REEL_DIR / f"{rid}.mp4"

        if not (mp4.is_file() and mp4.stat().st_size > 100_000):
            # rebuild frames + narration from the plan's script beats
            beats = []
            for line in it["reel_script"].split("\n["):
                if "ON-SCREEN:" not in line:
                    continue
                on = line.split("ON-SCREEN:", 1)[1].split("\n")[0].strip()
                vo = line.split("VO:", 1)[1].strip() if "VO:" in line else ""
                beats.append((on.replace(" / ", "\n"), vo))
            work = Path(tempfile.mkdtemp(prefix=f"{rid}_"))
            clips, total = [], 0.0
            try:
                for i, (on, vo) in enumerate(beats, 1):
                    png = _HERE / REEL_DIR / f"{rid}_{i:02d}.png"
                    if not png.is_file():
                        if i == 1:
                            _retry(hd_hook, on, str(png))
                        elif i == len(beats):
                            _retry(hd_end, on, str(png), question=it["hook"])
                        else:
                            _retry(hd_beat, on, str(png), kicker=it["category"])
                    mp3 = work / f"{i:02d}.mp3"
                    _tts(vo, mp3)
                    c = work / f"{i:02d}.mp4"
                    total += _clip(png, mp3, c)
                    clips.append(c)
                lst = work / "c.txt"
                lst.write_text("\n".join(f"file '{c.as_posix()}'" for c in clips),
                               encoding="utf-8")
                subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                                "-r", str(FPS), "-c:a", "aac", "-b:a", "160k",
                                "-ar", "48000", "-ac", "2", "-movflags", "+faststart",
                                str(mp4)], check=True, capture_output=True, timeout=900)
            finally:
                for f in work.glob("*"):
                    f.unlink(missing_ok=True)
                work.rmdir()
            rec["duration"] = round(total, 1)
        rec["mp4"] = str(mp4.relative_to(_HERE)).replace("\\", "/")
        rec["scheduled_for"] = it["date"]
        print(f"  reel {rid}: {rec.get('duration')}s")

        # Re-read the on-disk state right before upload (not just the in-memory
        # copy loaded at startup) — the defense-in-depth half of the fix. Even
        # if the lock is ever bypassed, this stops a second process from
        # uploading a slot the first one already claimed since this process began.
        disk_state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}
        if disk_state.get(rid, {}).get("video_id"):
            rec["video_id"] = disk_state[rid]["video_id"]
            rec["status"] = disk_state[rid].get("status")
            rec["publish_at_utc"] = disk_state[rid].get("publish_at_utc")
            print(f"    already scheduled by another run ({rec['video_id']}) — skipping")
        elif upload and not rec.get("video_id"):
            when = datetime.fromisoformat(it["date"])
            if when <= datetime.now(timezone.utc):
                print(f"    slot already passed — skipping upload")
            else:
                from publish_reel import publish
                cap = it["caption"] + "\n\n" + " ".join(it["hashtags"]) + "\n\n" + it["disclaimer"]
                try:
                    r = publish("health-daily", rec["mp4"], cap, schedule_ts=when.timestamp())
                    rec.update(r)
                    print(f"    SCHEDULED {r.get('video_id')} for {r.get('publish_at_utc')}")
                except Exception as e:
                    rec["upload_error"] = str(e)[:200]
                    print(f"    UPLOAD FAILED: {str(e)[:160]}")
        STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

    done = sum(1 for v in state.values() if v.get("mp4"))
    sched = sum(1 for v in state.values() if v.get("video_id"))
    print(f"REELS: {done} built, {sched} scheduled")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", action="store_true")
    ap.add_argument("--reels", action="store_true")
    ap.add_argument("--upload", action="store_true")
    a = ap.parse_args()
    _acquire_lock()
    try:
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        if a.images or not (a.images or a.reels):
            build_images(plan)
        if a.reels:
            build_reels(plan, upload=a.upload)
    finally:
        _release_lock()
