# -*- coding: utf-8 -*-
"""Pre-flight: confirm every film in a TMR reel content module resolves to a
TMDB poster BEFORE starting a long render. Catches typos and wrong years
cheaply instead of failing mid-build.

    python tmr_check_titles.py tmr_reel_content1
"""
import importlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

from tmdb import poster_url


def main(module_name):
    mod = importlib.import_module(module_name)
    seen, bad = set(), []
    for slug, beats, _ in mod.REELS:
        for b in beats:
            if b["kind"] != "poster":
                continue
            key = (b["title"], b.get("year"))
            if key in seen:
                continue
            seen.add(key)
            try:
                url = poster_url(b["title"], b.get("year"))
            except Exception as e:
                url = ""
                print(f"  ERROR {b['title']} ({b.get('year')}): {str(e)[:70]}")
            status = "ok " if url else "MISS"
            if not url:
                bad.append(f"{b['title']} ({b.get('year')}) [{slug}]")
            print(f"  {status} {b['title']} ({b.get('year')})")

    print(f"\nchecked {len(seen)} unique films")
    if bad:
        print(f"{len(bad)} UNRESOLVED:")
        for x in bad:
            print("   -", x)
        sys.exit(1)
    print("all titles resolved")


if __name__ == "__main__":
    main(sys.argv[1])
