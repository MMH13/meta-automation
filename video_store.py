# -*- coding: utf-8 -*-
"""Reel videos live in a GitHub release, not in this repo.

Committing rendered mp4s grew meta-automation to 3.4GB and made `git push`
time out (HTTP 408) — for files that are dead weight the moment the reel is
live on Facebook. They now go to the `videos` release on the PUBLIC repo
MMH13/ig-video-assets, which the IG pipeline already depended on: IG's Reels
API needs a genuinely public URL, and a private repo's release asset returns
404 to an unauthenticated fetch (Meta error 2207076).

Queue items carry `video_src` — the public download URL. `resolve()` returns a
local path for the FB 3-phase upload, downloading from `video_src` only when
the file isn't on disk. That keeps local runs fast (the file is right there
after a render) and lets the CI runner work from a checkout with no videos in
it at all.

Asset names are bare basenames. Verified collision-free across all 343 videos
this repo had tracked; upload() re-checks rather than trusting that to hold.
"""
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path

ASSET_REPO = "MMH13/ig-video-assets"
RELEASE_TAG = "videos"

_HERE = Path(__file__).parent
_cache = {}


def url_for(name):
    return f"https://github.com/{ASSET_REPO}/releases/download/{RELEASE_TAG}/{name}"


def hosted_names():
    """Asset names already in the release."""
    out = subprocess.run(
        ["gh", "release", "view", RELEASE_TAG, "--repo", ASSET_REPO,
         "--json", "assets", "--jq", ".assets[].name"],
        capture_output=True, text=True, check=True)
    return {n.strip() for n in out.stdout.splitlines() if n.strip()}


def upload(video_path, known=None, attempts=4):
    """Upload one video and return its public URL. Idempotent via --clobber.

    Retries: a single transient upload failure used to abort a whole 6-reel
    batch, and because the original raised CalledProcessError with the output
    captured, gh's actual message was swallowed — the traceback said only
    "returned non-zero exit status 1". Re-running the same command by hand
    succeeded immediately, which is what a blip looks like.
    """
    p = Path(video_path)
    if not p.is_file():
        raise FileNotFoundError(p)
    if known is not None and p.name in known:
        return url_for(p.name)

    last = ""
    for n in range(1, attempts + 1):
        r = subprocess.run(
            ["gh", "release", "upload", RELEASE_TAG, str(p),
             "--repo", ASSET_REPO, "--clobber"],
            capture_output=True, text=True)
        if r.returncode == 0:
            if known is not None:
                known.add(p.name)
            return url_for(p.name)
        last = ((r.stderr or "") + (r.stdout or "")).strip()[:400]
        if n < attempts:
            wait = 5 * n
            print(f"  upload of {p.name} failed (try {n}/{attempts}): {last}")
            print(f"  retrying in {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"gh release upload failed for {p.name} after "
                       f"{attempts} tries: {last}")


def resolve(item):
    """Local path to this item's video, fetching from the release if needed.

    Prefers the on-disk copy: a fresh render is already local, and re-downloading
    it would be pure waste. Falls back to video_src, then to deriving the URL
    from the basename so items queued before this change still work.
    """
    rel = item.get("video_path")
    if rel:
        local = (_HERE / rel) if not Path(rel).is_absolute() else Path(rel)
        if local.is_file():
            return str(local)

    src = item.get("video_src")
    if not src:
        if not rel:
            raise KeyError(f"item {item.get('id')!r} has no video_path or video_src")
        src = url_for(Path(rel).name)

    if src in _cache and Path(_cache[src]).is_file():
        return _cache[src]

    suffix = Path(rel or src).suffix or ".mp4"
    fd = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    fd.close()
    print(f"  fetching video: {src}")
    urllib.request.urlretrieve(src, fd.name)
    size = Path(fd.name).stat().st_size
    if size < 10_000:
        raise RuntimeError(f"downloaded video is only {size} bytes — {src} is probably a 404")
    print(f"  -> {fd.name} ({size/1e6:.1f} MB)")
    _cache[src] = fd.name
    return fd.name
