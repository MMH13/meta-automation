# -*- coding: utf-8 -*-
"""TMDB lookup for Top Movie Reviews poster cards.

TMDB's API is free and its terms permit using their images; posters are used
here inside our own review layout with a visible credit line (editorial use),
never reposted standalone.

Key lives in accounts.json (gitignored) — never hardcode or commit it.

  poster_url("Parasite", 2019)            -> https://image.tmdb.org/t/p/w780/....jpg
  movie_facts("Parasite", 2019)           -> dict of verified metadata
  cache_poster("Parasite", 2019, "x.jpg") -> local path (downloaded)
"""
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

_HERE = Path(__file__).parent
API = "https://api.themoviedb.org/3"
IMG = "https://image.tmdb.org/t/p"


def _key():
    with open(_HERE / "accounts.json", encoding="utf-8") as f:
        k = json.load(f).get("tmdb_api_key")
    if not k:
        raise RuntimeError("tmdb_api_key missing from accounts.json")
    return k


def _get(path, **params):
    params["api_key"] = _key()
    url = f"{API}/{path}?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=25) as r:
        return json.load(r)


def find(title, year=None):
    """Best matching movie record, or None."""
    p = {"query": title}
    if year:
        p["year"] = year
    res = _get("search/movie", **p).get("results") or []
    if not res:  # retry without the year filter
        res = _get("search/movie", query=title).get("results") or []
    return res[0] if res else None


def poster_url(title, year=None, size="w780"):
    m = find(title, year)
    if not m or not m.get("poster_path"):
        return ""
    return f"{IMG}/{size}{m['poster_path']}"


def cache_poster(title, year=None, out_dir="images/posters", size="w780"):
    """Download the poster once and return a local path (stable for re-renders)."""
    url = poster_url(title, year, size)
    if not url:
        return ""
    out = _HERE / out_dir
    out.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() else "_" for c in f"{title}_{year or ''}").strip("_")
    dest = out / f"{safe}.jpg"
    if not dest.is_file() or dest.stat().st_size < 1000:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=40) as r, open(dest, "wb") as f:
            f.write(r.read())
    return str(dest.relative_to(_HERE)).replace(os.sep, "/")


def movie_facts(title, year=None):
    """Verified metadata for review captions — never guess these by hand."""
    m = find(title, year)
    if not m:
        return {}
    d = _get(f"movie/{m['id']}", append_to_response="credits")
    crew = {c["job"]: c["name"] for c in d.get("credits", {}).get("crew", [])}
    cast = [c["name"] for c in d.get("credits", {}).get("cast", [])[:6]]
    return {
        "title": d.get("title"),
        "year": (d.get("release_date") or "")[:4],
        "release_date": d.get("release_date"),
        "runtime": d.get("runtime"),
        "budget": d.get("budget"),
        "revenue": d.get("revenue"),
        "genres": [g["name"] for g in d.get("genres", [])],
        "tmdb_score": d.get("vote_average"),
        "tmdb_votes": d.get("vote_count"),
        "director": crew.get("Director"),
        "dop": crew.get("Director of Photography"),
        "editor": crew.get("Editor"),
        "composer": crew.get("Original Music Composer"),
        "cast": cast,
        "poster": poster_url(title, year),
    }


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for t, y in [("Parasite", 2019), ("Mad Max: Fury Road", 2015)]:
        print(json.dumps(movie_facts(t, y), indent=1, ensure_ascii=False))
