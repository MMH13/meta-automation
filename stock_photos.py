# -*- coding: utf-8 -*-
"""Pexels PHOTO search/download, the still-image sibling of stock_footage.py.
Same key (accounts.json "pexels_api_key"). Free commercial use, no attribution
required (https://www.pexels.com/license/).
"""
import json
import time
from pathlib import Path

import requests

_HERE = Path(__file__).parent
_CONF = json.load(open(_HERE / "accounts.json", encoding="utf-8"))
API_KEY = _CONF.get("pexels_api_key")
SEARCH_URL = "https://api.pexels.com/v1/search"


def _headers():
    if not API_KEY:
        raise RuntimeError("no pexels_api_key in accounts.json")
    return {"Authorization": API_KEY}


def fetch_photo(query, out_path, exclude=None, tries=3):
    """Search + download one photo (large2x). `exclude` is a set of photo ids
    already used in this video so repeats are skipped. Returns (path, photo_id)."""
    out = Path(out_path)
    exclude = exclude if exclude is not None else set()
    out.parent.mkdir(parents=True, exist_ok=True)
    last_err = None
    for attempt in range(tries):
        try:
            r = requests.get(SEARCH_URL, headers=_headers(),
                             params={"query": query, "per_page": 15}, timeout=30)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            r.raise_for_status()
            photos = [p for p in r.json().get("photos", [])
                      if p["id"] not in exclude and min(p["width"], p["height"]) >= 1100]
            if not photos:
                raise RuntimeError(f"no usable Pexels photo for {query!r}")
            pick = photos[0]
            img = requests.get(pick["src"]["large2x"], timeout=120)
            img.raise_for_status()
            tmp = out.with_suffix(".tmp")
            tmp.write_bytes(img.content)
            tmp.replace(out)
            exclude.add(pick["id"])
            return out, pick["id"]
        except Exception as e:
            last_err = e
            time.sleep(3 * (attempt + 1))
    raise last_err
