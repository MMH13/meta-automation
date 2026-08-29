#!/bin/sh
cd "C:\Users\Mamun\fb-ig-automation"

ensure_voicebox() {
  n=0
  while ! curl -s -m 3 http://127.0.0.1:8000/health > /dev/null 2>&1; do
    n=$((n+1)); [ $n -gt 30 ] && echo "voicebox will not start" && return 1
    powershell -Command "if (-not (Get-Process voicebox-server -ErrorAction SilentlyContinue)) { Start-Process -FilePath 'C:\Program Files\Voicebox\voicebox-server.exe' -WindowStyle Hidden }" 2>/dev/null
    sleep 5
  done
  return 0
}

restart_voicebox() {
  powershell -Command "Get-Process voicebox-server -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue; Start-Sleep -Seconds 4" 2>/dev/null
  ensure_voicebox
}

for mod in tmr_reel_content8 tmr_reel_content9; do
  echo "############ $mod ############"
  ensure_voicebox || exit 1
  for attempt in 1 2 3 4 5 6 7 8; do
    PYTHONIOENCODING=utf-8 python tmr_reel_enqueue.py "$mod" 2>&1 && break
    echo "--- $mod attempt $attempt failed, restarting voicebox ---"
    restart_voicebox
  done
done

PYTHONIOENCODING=utf-8 python tmr_reels_6perday.py 2>&1
echo "BATCHES_89_DONE"
