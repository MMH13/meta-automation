# -*- coding: utf-8 -*-
"""রেডিও দেশাল video assembly — stills + Bengali TTS + ffmpeg.

Deliberately NOT generative video. Reasons:
  * Generative models cannot reliably render Bengali script; the existing HTML/Edge
    card renderer does it perfectly (browser text engine, proper shaping).
  * Cost. Veo/Sora run $0.03–0.50/sec; a 60s daily post is $270–900/month against a
    low-CPM Bengali audience. This pipeline costs ~$0/video.
  * Sora 2's API shuts down 2026-09-24. Nothing here should depend on it.

Pipeline per scene:  deshal_card() PNG  →  edge-tts Bengali MP3  →  ffmpeg clip
Then all scenes are concatenated into one MP4.

Usage:
    python video_deshal.py                    # builds the demo reel
    from video_deshal import build_video
    build_video(SCENES, "images/deshal_test.mp4")

Requires: ffmpeg on PATH, `pip install edge-tts`, Microsoft Edge (for card rendering).
"""

import base64
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

from image_deshal import deshal_card, deshal_reel_scene

_HERE = Path(__file__).parent

FPS = 25
W, H = 1080, 1350          # 4:5, matches the existing card renderer
RW, RH = 1080, 1920        # true 9:16, for build_reel_video() below

TAIL_PAD = 0.55            # seconds of silence after narration, so cuts don't clip
FADE = 0.35                # per-scene fade in/out

# --- Voice -----------------------------------------------------------------
# Achernar on gemini-3.1-flash-tts is the only voice that passed native-speaker
# review (2026-07-19). Seven were tested: the Azure/edge-tts bn-BD pair were
# rejected outright; Aoede/Kore/Sulafat/Vindemiatrix were "better, not enough".
# Do not change VOICE or STEER without re-running that review — the steering
# prompt is doing as much work here as the voice choice.
TTS_MODEL = "gemini-3.1-flash-tts-preview"
VOICE = "Achernar"

STEER = (
    "You are a professional Bangladeshi voice artist from Dhaka narrating a popular "
    "Bengali entertainment page. Speak in natural, colloquial Bangladesh Bengali "
    "(বাংলাদেশি বাংলা) — NOT West Bengal / Kolkata Bengali. "
    "Pronounce every conjunct consonant clearly and do not rush. "
    "Warm, friendly, slightly amused tone, moderate pace:\n\n"
)

# edge-tts fallback: free, no key, but rejected on quality. Kept only so a run can
# still complete if the Gemini key is rate-limited mid-batch.
FALLBACK_VOICE = "bn-BD-PradeepNeural"


def _gemini_key() -> str:
    return json.loads(
        (_HERE / "accounts.json").read_text(encoding="utf-8"))["gemini_api_key"]


def _narration(card_text: str) -> str:
    """Card text → speakable text: drop *highlight* markers and line breaks."""
    t = re.sub(r"\*(.+?)\*", r"\1", card_text)
    return " ".join(ln.strip() for ln in t.strip().split("\n") if ln.strip())


def _tts_gemini(text: str, out_mp3: Path) -> None:
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{TTS_MODEL}:generateContent?key={_gemini_key()}")
    body = {"contents": [{"parts": [{"text": STEER + text}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {
                                     "prebuiltVoiceConfig": {"voiceName": VOICE}}}}}
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    last = None
    for attempt in range(4):
        try:
            resp = json.load(urllib.request.urlopen(req, timeout=180))
            break
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code == 429:          # free-tier quota; back off and retry
                time.sleep(15 * (attempt + 1)); continue
            raise
        except Exception as e:         # transient network/timeout
            last = type(e).__name__
            time.sleep(8)
    else:
        raise RuntimeError(f"Gemini TTS failed after retries ({last})")

    pcm = base64.b64decode(
        resp["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
    raw = out_mp3.with_suffix(".pcm")
    raw.write_bytes(pcm)
    # Gemini returns headerless signed 16-bit PCM @ 24kHz mono. Normalize so the
    # bed-mix downstream has predictable levels.
    subprocess.run(
        ["ffmpeg", "-y", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", str(raw),
         "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "44100", "-ac", "2",
         "-b:a", "192k", str(out_mp3)],
        check=True, capture_output=True, timeout=120)
    raw.unlink(missing_ok=True)


def _tts_edge(text: str, out_mp3: Path) -> None:
    txt_file = out_mp3.with_suffix(".txt")
    txt_file.write_text(text, encoding="utf-8")
    subprocess.run(
        [sys.executable, "-m", "edge_tts", "--voice", FALLBACK_VOICE,
         "--file", str(txt_file), "--write-media", str(out_mp3)],
        check=True, capture_output=True, timeout=120)
    txt_file.unlink(missing_ok=True)


def _tts(text: str, out_mp3: Path, voice: str | None = None) -> None:
    try:
        _tts_gemini(text, out_mp3)
    except Exception as e:
        print(f"    ! Gemini TTS failed ({e}); falling back to edge-tts "
              f"— REVIEW THIS CLIP, quality was rejected")
        _tts_edge(text, out_mp3)
    if not out_mp3.is_file() or out_mp3.stat().st_size == 0:
        raise RuntimeError(f"TTS produced no audio for: {text[:60]}")
    time.sleep(4)   # stay under free-tier rate limits between scenes


def _duration(media: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(media)],
        check=True, capture_output=True, text=True,
    )
    return float(out.stdout.strip())


def _scene_clip(png: Path, mp3: Path, out_mp4: Path) -> float:
    """One still + one narration → an mp4 clip with a slow Ken Burns push."""
    dur = _duration(mp3) + TAIL_PAD
    frames = max(int(dur * FPS), 1)
    # Upscale first so zoompan samples from a larger source (avoids shimmer),
    # then push in ~8% over the scene and fade the edges.
    vf = (
        f"scale={W*2}:{H*2},"
        f"zoompan=z='min(1+0.08*on/{frames},1.08)':d={frames}"
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
        check=True, capture_output=True, timeout=600,
    )
    return dur


def _scene_clip_reel(png: Path, mp3: Path, out_mp4: Path) -> float:
    """9:16 counterpart to _scene_clip — same Ken Burns treatment, RW/RH canvas."""
    dur = _duration(mp3) + TAIL_PAD
    frames = max(int(dur * FPS), 1)
    vf = (
        f"scale={RW*2}:{RH*2},"
        f"zoompan=z='min(1+0.08*on/{frames},1.08)':d={frames}"
        f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={RW}x{RH}:fps={FPS},"
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
        check=True, capture_output=True, timeout=600,
    )
    return dur


def build_reel_video(scenes: list[dict], out_path: str, music: str | None = None,
                     keep_work: bool = False) -> str:
    """True 9:16 counterpart to build_video() — same TTS/voice pipeline, proper
    Reels canvas via deshal_reel_scene() instead of the 4:5 feed card."""
    out = Path(out_path)
    if not out.is_absolute():
        out = _HERE / out
    out.parent.mkdir(parents=True, exist_ok=True)

    work = Path(tempfile.mkdtemp(prefix="deshal_reel_"))
    clips, total = [], 0.0
    try:
        for i, sc in enumerate(scenes, 1):
            png = work / f"s{i}.png"
            mp3 = work / f"s{i}.mp3"
            mp4 = work / f"s{i}.mp4"
            deshal_reel_scene(sc["text"], str(png),
                              theme=sc.get("theme", "sunset"),
                              emoji=sc.get("emoji", ""))
            _tts(sc.get("narration") or _narration(sc["text"]), mp3)
            d = _scene_clip_reel(png, mp3, mp4)
            total += d
            clips.append(mp4)
            print(f"  scene {i}/{len(scenes)}  {d:5.2f}s  {sc['text'].splitlines()[0][:40]}")

        listing = work / "concat.txt"
        listing.write_text(
            "".join(f"file '{c.as_posix()}'\n" for c in clips), encoding="utf-8")

        if music:
            subprocess.run(
                ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
                 "-stream_loop", "-1", "-i", str(music),
                 "-filter_complex",
                 f"[1:a]volume=0.12,afade=t=out:st={max(total-2,0):.2f}:d=2[bed];"
                 f"[0:a][bed]amix=inputs=2:duration=first:dropout_transition=0[a]",
                 "-map", "0:v", "-map", "[a]",
                 "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", str(out)],
                check=True, capture_output=True, timeout=600)
        else:
            subprocess.run(
                ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
                 "-c", "copy", str(out)],
                check=True, capture_output=True, timeout=600)
    finally:
        if not keep_work:
            for p in work.glob("*"):
                p.unlink(missing_ok=True)
            work.rmdir()

    print(f"\n  → {out}  ({total:.1f}s, 9:16)")
    return str(out)


def build_video(scenes: list[dict], out_path: str, music: str | None = None,
                keep_work: bool = False) -> str:
    """scenes: [{"text": str, "theme": str, "emoji": str, "voice": str}, ...]

    music: optional path to a LICENSED background track. None = narration only.
    Never point this at a copyrighted track you do not have rights to — a music
    claim on a 32k page costs more than the video is worth.
    """
    out = Path(out_path)
    if not out.is_absolute():
        out = _HERE / out
    out.parent.mkdir(parents=True, exist_ok=True)

    work = Path(tempfile.mkdtemp(prefix="deshal_vid_"))
    clips, total = [], 0.0
    try:
        for i, sc in enumerate(scenes, 1):
            png = work / f"s{i}.png"
            mp3 = work / f"s{i}.mp3"
            mp4 = work / f"s{i}.mp4"
            deshal_card(sc["text"], str(png),
                        theme=sc.get("theme", "sunset"),
                        emoji=sc.get("emoji", ""))
            _tts(sc.get("narration") or _narration(sc["text"]), mp3)
            d = _scene_clip(png, mp3, mp4)
            total += d
            clips.append(mp4)
            print(f"  scene {i}/{len(scenes)}  {d:5.2f}s  {sc['text'].splitlines()[0][:40]}")

        listing = work / "concat.txt"
        listing.write_text(
            "".join(f"file '{c.as_posix()}'\n" for c in clips), encoding="utf-8")

        if music:
            # Duck the bed well under the voice; loop it to cover the full runtime.
            subprocess.run(
                ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
                 "-stream_loop", "-1", "-i", str(music),
                 "-filter_complex",
                 f"[1:a]volume=0.12,afade=t=out:st={max(total-2,0):.2f}:d=2[bed];"
                 f"[0:a][bed]amix=inputs=2:duration=first:dropout_transition=0[a]",
                 "-map", "0:v", "-map", "[a]",
                 "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", str(out)],
                check=True, capture_output=True, timeout=600)
        else:
            subprocess.run(
                ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
                 "-c", "copy", str(out)],
                check=True, capture_output=True, timeout=600)
    finally:
        if not keep_work:
            for p in work.glob("*"):
                p.unlink(missing_ok=True)
            work.rmdir()

    print(f"\n  → {out}  ({total:.1f}s)")
    return str(out)


# --- demo reel: a relatable Dhaka-life bit, the format the page already runs ---

SCENES = [
    {"text": "ঢাকার ট্রাফিক জ্যাম\nমানে কী জানেন?", "theme": "sunset", "emoji": "🚦"},
    {"text": "*দশ মিনিটের* রাস্তা\nএক ঘণ্টায়", "theme": "mango", "emoji": "⏰"},
    {"text": "বাসে উঠে মনে হয়\n*ধৈর্যের পরীক্ষা* দিচ্ছি", "theme": "ocean", "emoji": "🚌"},
    {"text": "তবুও আমরা হাসি\nকারণ আমরা *ঢাকাবাসী*", "theme": "mint", "emoji": "😄"},
]

if __name__ == "__main__":
    build_video(SCENES, "images/deshal_video_test.mp4")
