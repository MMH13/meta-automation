# -*- coding: utf-8 -*-
"""Drives hd_reel_enqueue.main(..., stock=True) across all hd10_batchNN
modules in order, one reel at a time, writing progress to a log file this
script's stdout is redirected to. Safe to re-run: hd_reel_enqueue already
skips any (fb_id, ig_id) pair already present in queue.json, and each video's
own build() call is resumable via its per-beat state file.
"""
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

from hd_reel_enqueue import main as enqueue_main

MODULES = [
    "hd10_batch01", "hd10_batch02", "hd10_batch03",
    "hd10_batch04", "hd10_batch05", "hd10_batch06",
]

t_start = time.time()
for mod in MODULES:
    print(f"\n{'='*60}\n=== MODULE {mod} - starting at +{(time.time()-t_start)/60:.1f}min ===\n{'='*60}")
    try:
        enqueue_main(mod, stock=True)
    except ModuleNotFoundError:
        print(f"  {mod} not written yet, stopping here (re-run driver once it exists).")
        break
    except Exception as e:
        print(f"  !!! {mod} raised {type(e).__name__}: {e} - continuing to next module")

print(f"\nDONE. Total elapsed: {(time.time()-t_start)/60:.1f} min")
