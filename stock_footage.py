# -*- coding: utf-8 -*-
"""Pexels video search/download client for scene-matched B-roll.

Key comes from accounts.json ("pexels_api_key"), same pattern as
image_ai.py's gemini_api_key. Free tier: 200 req/hr, 20k/month - plenty for
per-video builds (one search per beat, cached locally after first fetch).

Usage:
    from stock_footage import find_clip, download_clip
    hit = find_clip("empty apartment hallway night")
    path = download_clip(hit, "images/footage/hallway.mp4")

License: Pexels videos are free for commercial use, no attribution required
(https://www.pexels.com/license/). Still, don't reuse a clip somewhere its
subject/brand would be misleading - fine for atmospheric B-roll like this.
"""
import json
import time
from pathlib import Path

import requests

_HERE = Path(__file__).parent
_CONF = json.load(open(_HERE / "accounts.json", encoding="utf-8"))
API_KEY = _CONF.get("pexels_api_key")
SEARCH_URL = "https://api.pexels.com/videos/search"


def _headers():
    if not API_KEY:
        raise RuntimeError(
            "no pexels_api_key in accounts.json - add the key the user provided")
    return {"Authorization": API_KEY}


def find_clip(query, min_width=800, min_duration=4, orientation="portrait", tries=3):
    """Returns the best-matching video hit dict (raw Pexels API shape) or None.
    Prefers clips >= min_duration seconds and closest to square/portrait so
    less cropping is needed for the 1:1 canvas."""
    for attempt in range(tries):
        r = requests.get(SEARCH_URL, headers=_headers(),
                         params={"query": query, "per_page": 12,
                                 "orientation": orientation}, timeout=30)
        if r.status_code == 429:
            time.sleep(5 * (attempt + 1))
            continue
        r.raise_for_status()
        videos = r.json().get("videos", [])
        candidates = [v for v in videos if v.get("duration", 0) >= min_duration]
        if not candidates:
            candidates = videos
        if not candidates:
            return None

        def _score(v):
            files = [f for f in v["video_files"] if f.get("width", 0) >= min_width]
            if not files:
                return (0, 0)
            best = max(files, key=lambda f: f["width"])
            ratio = best["width"] / max(best["height"], 1)
            return (-abs(ratio - 1.0), v.get("duration", 0))
        return max(candidates, key=_score)
    return None


def best_file(hit, min_width=800):
    """Pick the highest-quality file url from a hit dict."""
    files = [f for f in hit["video_files"] if f.get("width", 0) >= min_width]
    if not files:
        files = hit["video_files"]
    return max(files, key=lambda f: f["width"])["link"]


def download_clip(hit, out_path, min_width=800, tries=3):
    out = Path(out_path)
    if out.is_file() and out.stat().st_size > 0:
        return out  # cached
    out.parent.mkdir(parents=True, exist_ok=True)
    url = best_file(hit, min_width=min_width)
    tmp = out.with_suffix(".tmp")
    last_err = None
    for attempt in range(tries):
        try:
            r = requests.get(url, timeout=120, stream=True)
            r.raise_for_status()
            with open(tmp, "wb") as f:
                for chunk in r.iter_content(1 << 16):
                    f.write(chunk)
            tmp.rename(out)
            return out
        except Exception as e:  # dropped connection mid-download, etc.
            last_err = e
            tmp.unlink(missing_ok=True)
            time.sleep(3 * (attempt + 1))
    raise last_err


def fetch(query, out_path, min_width=800, min_duration=4):
    """One-shot: search + download. Returns the local path, or raises if
    nothing matched (caller should fall back to another query or SVG)."""
    hit = find_clip(query, min_width=min_width, min_duration=min_duration)
    if hit is None:
        raise RuntimeError(f"no Pexels result for query: {query!r}")
    return download_clip(hit, out_path, min_width=min_width), hit
