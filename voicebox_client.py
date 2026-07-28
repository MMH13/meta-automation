# -*- coding: utf-8 -*-
"""Voicebox local API client (127.0.0.1:17493).

Uses BUILT-IN preset voices only — never the cloned profile, per the user's
instruction (cloned voices of a real person carry consent problems when the
audio is published).

  ensure_profile(name, engine, voice_id)  -> profile_id  (idempotent)
  speak(profile_id, text, out_wav)        -> path to rendered WAV
"""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "http://127.0.0.1:17493"


def _req(method, path, payload=None, timeout=180):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(
        f"{BASE}{path}", data=data, method=method,
        headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        raw = resp.read()
        try:
            return json.loads(raw)
        except Exception:
            return raw


def alive():
    try:
        _req("GET", "/health", timeout=6)
        return True
    except Exception:
        return False


def list_profiles():
    # /profiles returns a bare JSON array, not a wrapped object
    out = _req("GET", "/profiles")
    return out if isinstance(out, list) else out.get("profiles", [])


def ensure_profile(name, engine, voice_id, language="en", description=""):
    """Create a preset-backed profile if one with this name doesn't exist."""
    for p in list_profiles():
        if p.get("name") == name:
            return p["id"]
    out = _req("POST", "/profiles", {
        "name": name,
        "description": description,
        "language": language,
        "voice_type": "preset",
        "preset_engine": engine,
        "preset_voice_id": voice_id,
        "default_engine": engine,
    })
    pid = out.get("id") or out.get("profile_id")
    if not pid:
        raise RuntimeError(f"profile create returned no id: {str(out)[:200]}")
    return pid


def speak(profile_id, text, out_wav, engine=None, language="en", timeout=600):
    """Generate speech and save the WAV. Blocks until the generation is done."""
    body = {"profile_id": profile_id, "text": text, "language": language,
            "personality": False, "normalize": True}
    if engine:
        body["engine"] = engine
    gen = _req("POST", "/generate", body)
    gid = gen.get("generation_id") or gen.get("id")
    if not gid:
        raise RuntimeError(f"no generation id: {str(gen)[:200]}")

    # NOTE: /generate/{id}/status is a text/event-stream, not JSON — polling it
    # blocks and yields bytes. /history/{id} exposes the same state as plain
    # JSON, and is done once audio_path is populated.
    deadline = time.time() + timeout
    while time.time() < deadline:
        h = _req("GET", f"/history/{gid}", timeout=30)
        if isinstance(h, dict):
            if (h.get("error") or "").strip():
                raise RuntimeError(f"generation {gid} failed: {h['error'][:200]}")
            if h.get("audio_path") and (h.get("duration") or 0) > 0:
                break
        time.sleep(2)
    else:
        raise TimeoutError(f"generation {gid} timed out")

    audio = _req("GET", f"/audio/{gid}", timeout=120)
    if not isinstance(audio, (bytes, bytearray)):
        raise RuntimeError(f"unexpected audio payload: {str(audio)[:160]}")
    out = Path(out_wav)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(audio)
    return str(out)
