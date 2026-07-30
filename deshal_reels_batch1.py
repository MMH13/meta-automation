# -*- coding: utf-8 -*-
"""Radio Deshal — first real batch of voiced 9:16 reels, replacing static
meme cards as the primary format per research: this page's own 20 legacy
reels (even reposted stock clips) got the same 0 engagement as its images,
but general 2026 platform data and Bengali-meme-specific patterns both point
to short native-voiced video as the actual high-leverage format here, not a
different image layout. See chat for the full research writeup.

Each reel: same short setup->twist joke writing already approved, spoken in
the validated Bangladeshi-accent voice (Gemini TTS via video_deshal.py),
built at true 1080x1920.

Uploads via the same Reels API used for Health Daily / Top Movie Reviews,
now pointed at radio-deshal. Lock-protected and state-resumable from the
start this time — a prior run on a different page got launched twice by
accident and produced duplicate scheduled posts; see hd_build_week1.py's
_acquire_lock for the postmortem and the fix pattern reused here.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from video_deshal import build_reel_video

_HERE = Path(__file__).parent
OUT_DIR = _HERE / "images" / "deshal_reels_batch1"
OUT_DIR.mkdir(parents=True, exist_ok=True)
STATE = _HERE / "deshal_reels_batch1_state.json"
LOCK = _HERE / "deshal_reels_batch1.lock"

# (id, scenes, caption, schedule ISO)
REELS = [
 ("ardreel-1",
  [{"text": "অফিসে বসের মেসেজ:\n\"একটু ফ্রি আছো?\"", "theme": "berry", "emoji": "😨"},
   {"text": "আমি রিপ্লাই দিলাম,\n\"জি স্যার, বলুন\"", "theme": "grape", "emoji": "😰"},
   {"text": "বস বললেন,\n\"পাসওয়ার্ডটা কী ছিল যেন?\"", "theme": "mango", "emoji": "🙄"},
   {"text": "এই টেনশনটা\n*শুধু আমরাই বুঝি* 😂", "theme": "mint", "emoji": "😂"}],
  "😂 বসের \"একটু ফ্রি আছো\" মেসেজ দেখলেই বুকের ভেতর একটা ধাক্কা লাগে। কে কে এই টেনশনের সাথে পরিচিত? কমেন্টে জানান 👇\n\n🔁 শেয়ার করুন সেই কলিগকে যে সবসময় এই আতঙ্কে থাকে।\n\n📻 রেডিও দেশাল",
  "2026-08-08T15:00:00+00:00"),

 ("ardreel-2",
  [{"text": "পরীক্ষার হলে স্যার বললেন,\n\"সময় শেষ, কলম রাখো\"", "theme": "ocean", "emoji": "⏰"},
   {"text": "সবাই কলম রাখলো,\nএকজন তখনও লিখছে", "theme": "sunset", "emoji": "✍️"},
   {"text": "স্যার আবার বললেন,\n\"কলম রাখো বলছি!\"", "theme": "berry", "emoji": "😠"},
   {"text": "ছেলেটা বললো,\n\"স্যার, *নামটা* লিখছি\" 😂", "theme": "mint", "emoji": "😂"}],
  "😂 এই লেভেলের সময়জ্ঞান থাকলে জীবনে আর কিছু লাগে না। কে কে এমন করেছেন পরীক্ষায়? সত্যি বলুন 👇\n\n🔁 শেয়ার করুন সেই বন্ধুকে যে সবসময় শেষ মুহূর্তে দৌড়ায়।\n\n📻 রেডিও দেশাল",
  "2026-08-09T15:00:00+00:00"),

 ("ardreel-3",
  [{"text": "শাশুড়ি ফোন করে বললেন,\n\"বউমা রান্না কেমন শিখলে?\"", "theme": "grape", "emoji": "😅"},
   {"text": "আমি বললাম,\n\"আম্মা এখনো ডিম ভাজিই ভালো পারি না\"", "theme": "mango", "emoji": "🍳"},
   {"text": "শাশুড়ি বললেন,\n\"কোনো ব্যাপার না মা-\"", "theme": "sunset", "emoji": "🥹"},
   {"text": "\"আমার ছেলে তো\n*শুধু ডিম ভাজিই* খায়!\" 😂", "theme": "mint", "emoji": "😂"}],
  "😂 কিছু শাশুড়ি সত্যিই রত্ন হয়। কার শাশুড়ির সাথে এমন মধুর সম্পর্ক আছে? কমেন্টে জানান 👇\n\n🔁 শেয়ার করুন আপনার শাশুড়ি বা বউমাকে ট্যাগ করে।\n\n📻 রেডিও দেশাল",
  "2026-08-10T15:00:00+00:00"),

 ("ardreel-4",
  [{"text": "গ্রুপ চ্যাটে সবাই\n\"😂😂😂\" রিয়েক্ট দিচ্ছে", "theme": "ocean", "emoji": "📱"},
   {"text": "আমি জিজ্ঞেস করলাম,\n\"কী নিয়ে হাসছেন?\"", "theme": "berry", "emoji": "🤔"},
   {"text": "৫ মিনিট কেউ\nরিপ্লাই দিলো না", "theme": "grape", "emoji": "😶"},
   {"text": "তারপর একজন বললো,\n\"ভাই *স্ক্রল কর উপরে*\" 😂", "theme": "mint", "emoji": "😂"}],
  "😂 গ্রুপ চ্যাটে দেরি করে ঢোকার এই এক লজ্জা সবাই বোঝে। কে কে এই পরিস্থিতিতে পড়েছেন? 👇\n\n🔁 শেয়ার করুন আপনার সবচেয়ে সক্রিয় গ্রুপ চ্যাটে।\n\n📻 রেডিও দেশাল",
  "2026-08-11T15:00:00+00:00"),

 ("ardreel-5",
  [{"text": "খেলা দেখছিলাম,\nবাংলাদেশ ৩ উইকেট হারালো", "theme": "sunset", "emoji": "😰"},
   {"text": "বাবা বললেন,\n\"টিভি বন্ধ কর, অলুক্ষুণে!\"", "theme": "berry", "emoji": "😤"},
   {"text": "টিভি বন্ধ করে\nচুপচাপ বসে রইলাম", "theme": "ocean", "emoji": "😑"},
   {"text": "কিছুক্ষণ পর মোবাইলে দেখি—\n\"বাংলাদেশ *জিতে গেছে*!\" 😄", "theme": "mint", "emoji": "🏏"}],
  "😄 বাঙালি বাবাদের এই কুসংস্কার সবসময় কাজে লাগে কিনা কে জানে, তবে মজা লাগে। কে কে এমন \"টিভি বন্ধ করো\" শুনেছেন? 👇\n\n🔁 শেয়ার করুন সেই ক্রিকেট-পাগল পরিবারের কাউকে।\n\n📻 রেডিও দেশাল",
  "2026-08-12T15:00:00+00:00"),

 ("ardreel-6",
  [{"text": "ফোনে চার্জ মাত্র\n*১%*", "theme": "berry", "emoji": "🔋"},
   {"text": "ঠিক তখনই\nকারেন্ট চলে গেলো", "theme": "grape", "emoji": "😱"},
   {"text": "মোমবাতি খুঁজতে খুঁজতে\nফোনও অফ হয়ে গেলো", "theme": "ocean", "emoji": "🕯️"},
   {"text": "কারেন্ট আসতেই ফোন অন করে দেখি—\n*একটাই নোটিফিকেশন*: চার্জ কম 😂", "theme": "mint", "emoji": "😂"}],
  "😂 এই টাইমিং শুধু বাংলাদেশেই সম্ভব। কে কে এই পরিস্থিতিতে পড়েছেন? 👇\n\n🔁 শেয়ার করুন যাদের এলাকায় এখনো লোডশেডিং হয়।\n\n📻 রেডিও দেশাল",
  "2026-08-13T15:00:00+00:00"),
]


def _acquire_lock():
    import os
    if LOCK.is_file():
        try:
            other = int(LOCK.read_text().strip())
            os.kill(other, 0)
            raise SystemExit(f"Already running (pid {other}). Refusing to start a second instance.")
        except (ValueError, ProcessLookupError, OSError):
            pass
    LOCK.write_text(str(os.getpid()))


def _release_lock():
    LOCK.unlink(missing_ok=True)


def _load_state():
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}


def _save_state(s):
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def build(upload=False):
    state = _load_state()
    for rid, scenes, caption, when_iso in REELS:
        rec = state.setdefault(rid, {})
        mp4 = OUT_DIR / f"{rid}.mp4"

        if not (mp4.is_file() and mp4.stat().st_size > 100_000):
            build_reel_video(scenes, str(mp4))
        rec["mp4"] = str(mp4.relative_to(_HERE)).replace("\\", "/")
        print(f"{rid}: built -> {rec['mp4']}")

        # live re-check right before upload — defense in depth against ever
        # running two instances of this again
        disk = _load_state()
        if disk.get(rid, {}).get("video_id"):
            rec["video_id"] = disk[rid]["video_id"]
            print(f"  already scheduled by another run ({rec['video_id']}) — skipping")
        elif upload and not rec.get("video_id"):
            when = datetime.fromisoformat(when_iso)
            if when <= datetime.now(timezone.utc):
                print("  slot already passed — skipping upload")
            else:
                from publish_reel import publish
                try:
                    r = publish("radio-deshal", rec["mp4"], caption, schedule_ts=when.timestamp())
                    rec.update(r)
                    print(f"  SCHEDULED {r.get('video_id')} for {r.get('publish_at_utc')}")
                except Exception as e:
                    rec["upload_error"] = str(e)[:200]
                    print(f"  UPLOAD FAILED: {str(e)[:160]}")
        _save_state(state)

    done = sum(1 for v in state.values() if v.get("mp4"))
    sched = sum(1 for v in state.values() if v.get("video_id"))
    print(f"\nTOTAL: {done} built, {sched} scheduled")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--upload", action="store_true")
    args = ap.parse_args()
    _acquire_lock()
    try:
        build(upload=args.upload)
    finally:
        _release_lock()
