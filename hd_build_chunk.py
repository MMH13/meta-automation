# -*- coding: utf-8 -*-
"""Build the next N unbuilt Health Daily hd10 reels, then re-lay the schedule.

    python hd_build_chunk.py 30

hd10_render_driver.py has no voicebox handling and builds everything in one
go; this wraps it so a long refill can be cut into pushable checkpoints:
start/restart voicebox, run the driver capped at the remaining reels, and
repeat while progress is being made. Ends by running hd_reels_10perday.py.
"""
import glob
import importlib
import os
import subprocess
import sys

import sa_build_batches as sb  # reuse ready(): starts voicebox, disables the idle watchdog

MODULES = [f"hd10_batch0{n}" for n in range(1, 7)]
MAX_STALLS = 3


def remaining():
    n = 0
    for mod in MODULES:
        m = importlib.import_module(mod)
        out = mod.replace("hd10_batch", "health_reels_hd10_batch")
        for slug, _, _ in m.REELS:
            if not os.path.isfile(f"images/{out}/{slug}.mp4"):
                n += 1
    return n


def built():
    return len(glob.glob("images/health_reels_hd10_batch0*/*.mp4"))


def main(cap):
    start, stalls = built(), 0
    while built() - start < cap and remaining() > 0:
        if not sb.ready(restart=stalls > 0):
            print("!!! voicebox would not start", flush=True)
            break
        before = built()
        env = dict(os.environ, HD_MAX_BUILD=str(cap - (built() - start)), PYTHONIOENCODING="utf-8")
        subprocess.run([sys.executable, "hd10_render_driver.py"], env=env)
        stalls = 0 if built() > before else stalls + 1
        if stalls >= MAX_STALLS:
            print(f"!!! no progress after {MAX_STALLS} rounds - stopping", flush=True)
            break
    subprocess.run([sys.executable, "hd_reels_10perday.py"])
    print(f"built this chunk: {built() - start} | still unbuilt: {remaining()}", flush=True)
    print("CHUNK_DONE", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30)
