# -*- coding: utf-8 -*-
"""Render several Daily Wisdom content-day modules in one Python process.

Same runner as build_batches.py (TMR), pointed at the wisdom enqueuer/
rebalancer instead — kept as a separate file rather than a generalized one,
matching this project's existing convention of per-page scripts
(tmr_reel_enqueue.py / hd_reel_enqueue.py / sa_reel_enqueue.py) over shared
generic ones. See build_batches.py's docstring for why this shape exists:
in-process looping to avoid Git Bash's fork failure under load, and
disable_watchdog() before every batch and after every restart so an
unattended run doesn't die to voicebox's idle shutdown.

    python wisdom_build_batches.py wisdom_reel_content2 wisdom_reel_content3
"""
import subprocess
import sys
import time

import voicebox_client

EXE = r"C:\Program Files\Voicebox\voicebox-server.exe"
ATTEMPTS = 6


def ready(restart=False, tries=50):
    if restart or not voicebox_client.alive():
        subprocess.run(["taskkill", "/IM", "voicebox-server.exe", "/F"],
                       capture_output=True)
        time.sleep(5)
        subprocess.Popen([EXE], creationflags=subprocess.CREATE_NO_WINDOW)

    for _ in range(tries):
        if voicebox_client.alive():
            ok = voicebox_client.disable_watchdog()
            print(f"    voicebox up; watchdog disabled={ok}", flush=True)
            return ok
        time.sleep(6)
    return False


def main(modules):
    failed = []
    for mod in modules:
        print(f"\n############ {mod} ############", flush=True)
        if not ready():
            print(f"!!! voicebox will not start — skipping {mod}", flush=True)
            failed.append(mod)
            continue
        for attempt in range(1, ATTEMPTS + 1):
            rc = subprocess.run([sys.executable, "wisdom_reel_enqueue.py", mod]).returncode
            if rc == 0:
                break
            print(f"--- {mod} attempt {attempt} failed (rc={rc}); restarting voicebox",
                  flush=True)
            if not ready(restart=True):
                print(f"!!! {mod} abandoned — voicebox would not come back", flush=True)
                failed.append(mod)
                break
        else:
            print(f"!!! {mod} never completed after {ATTEMPTS} attempts", flush=True)
            failed.append(mod)

    subprocess.run([sys.executable, "wisdom_reels_6perday.py"])
    if failed:
        print(f"INCOMPLETE: {', '.join(failed)}", flush=True)
    print("BATCHES_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
