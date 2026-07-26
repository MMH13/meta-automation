# -*- coding: utf-8 -*-
"""Shared enqueue helper for the Aug 1-7 refill drivers.
Each page driver renders its images then calls add()/flush() to append to queue.json.
Sequential run only (no concurrent writers) to avoid clobbering queue.json.
"""
import json, os, datetime

QUEUE = "queue.json"


def load():
    with open(QUEUE, encoding="utf-8") as f:
        return json.load(f)


def save(q):
    with open(QUEUE, "w", encoding="utf-8") as f:
        json.dump(q, f, indent=2, ensure_ascii=False)


def existing_ids(q):
    return {i.get("id") for i in q["items"]}


def when(day_index, hour, minute=0, tz="+00:00", base=(2026, 8, 1)):
    """day_index 0..6 from Aug 1; returns ISO string with tz offset."""
    d = datetime.date(*base) + datetime.timedelta(days=day_index)
    return f"{d.isoformat()}T{hour:02d}:{minute:02d}:00{tz}"


def mkdir(path):
    os.makedirs(path, exist_ok=True)
    return path


def render(fn, *args, **kwargs):
    """Call an image renderer, retrying the occasional headless-Edge hang.
    Edge sometimes stalls past its subprocess timeout; a retry always clears it."""
    import subprocess
    last = None
    for attempt in range(3):
        try:
            return fn(*args, **kwargs)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, RuntimeError) as e:
            last = e
            print(f"    retry {attempt+1}/3 after {type(e).__name__}")
    raise last
