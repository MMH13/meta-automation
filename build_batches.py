# -*- coding: utf-8 -*-
"""Render several TMR reel batches in one Python process.

Two failures this replaces, both of which HUNG rather than errored, so they
looked identical to "still rendering":

1. Git Bash on Windows fails to fork under load ("dofork: child -1 ...
   Resource temporarily unavailable"), which wedged the old shell loop while
   voicebox itself was perfectly healthy. Looping in-process removes the fork.

2. Voicebox shuts its backend down when no client is holding it open, killing
   a long unattended build partway through — exactly what voicebox_client.
   disable_watchdog() exists to prevent. The old loop polled :8000 (the GUI)
   and never disabled the watchdog, so it declared the server healthy right up
   until the render died of connection-refused. We now probe through
   voicebox_client, which discovers the real backend port, and re-disable the
   watchdog before every batch AND after every restart.

    python build_batches.py tmr_reel_content13 tmr_reel_content14
"""
import subprocess
import sys
import time

import voicebox_client

EXE = r"C:\Program Files\Voicebox\voicebox-server.exe"
ATTEMPTS = 6


def ready(restart=False, tries=50):
    """Backend answering AND watchdog disabled — both, or it dies mid-batch.

    Spawns AT MOST ONE server. The backend binds its port immediately but takes
    a few minutes to load models, so an earlier version that re-spawned on every
    poll tick stacked up three competing processes, each holding the port half
    open. Start one, then just wait for it.
    """
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
            rc = subprocess.run([sys.executable, "tmr_reel_enqueue.py", mod]).returncode
            if rc == 0:
                break
            print(f"--- {mod} attempt {attempt} failed (rc={rc}); restarting voicebox",
                  flush=True)
            if not ready(restart=True):
                break
        else:
            print(f"!!! {mod} never completed after {ATTEMPTS} attempts", flush=True)
            failed.append(mod)

    subprocess.run([sys.executable, "tmr_reels_6perday.py"])
    if failed:
        print(f"INCOMPLETE: {', '.join(failed)}", flush=True)
    print("BATCHES_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
