# -*- coding: utf-8 -*-
"""GitHub Actions runs on ubuntu-latest, but hd_reel_enqueue.py generated
video_path values using Windows path separators (backslash) via a bare
str(Path). That's fine locally but breaks FB reel posting on the Linux
runner, where backslash isn't a path separator. Normalize every existing
video_path in queue.json to forward slashes. One-time fix."""
from aug_common import load, save

BACKSLASH = "\\"


def run():
    q = load()
    fixed = 0
    for item in q["items"]:
        vp = item.get("video_path")
        if vp and BACKSLASH in vp:
            item["video_path"] = vp.replace(BACKSLASH, "/")
            fixed += 1
    save(q)
    print(f"fixed {fixed} video_path values")


if __name__ == "__main__":
    run()
