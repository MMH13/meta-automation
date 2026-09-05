# -*- coding: utf-8 -*-
"""Per-page narration voices, matched to each project's tone.

Built-in Voicebox preset voices only — never the cloned profile.
Voicebox has NO Bengali voices, so Bengali pages are marked unsupported and
must keep their existing pipeline.

  voice_for("top-movie-reviews") -> dict(profile, engine, voice_id, rate)
"""

VOICES = {
    # Cinematic, deep, authoritative — chosen by the user 2026-07-28.
    "top-movie-reviews": {
        "profile": "TMR-Narrator-Onyx",
        "engine": "kokoro",
        "voice_id": "am_onyx",
        "tone": "deep, cinematic, measured — film-critic authority",
    },
    # User-picked after a 3-way audition (Fenrir/Lewis/Michael), 2026-07-31.
    "suspense-ahead": {
        "profile": "SUS-Narrator-Lewis",
        "engine": "kokoro",
        "voice_id": "bm_lewis",
        "tone": "deep, ominous, deliberate horror narrator — distinct from Onyx (movie page)",
    },
    # Warm and calm; health advice has to sound trustworthy, not salesy.
    "health-daily": {
        "profile": "HD-Narrator-Bella",
        "engine": "kokoro",
        "voice_id": "af_bella",
        "tone": "warm, unhurried, reassuring",
    },
    # Reflective and soft — matches the calm-music mandate for that page.
    "psychology-tube": {
        "profile": "PSY-Narrator-Nicole",
        "engine": "kokoro",
        "voice_id": "af_nicole",
        "tone": "soft, reflective, gentle pacing",
    },
    # Calm, grounded, contemplative — verified against a real synthesized
    # sample before adoption (voicebox has no /voices listing endpoint, so
    # ensure_profile() alone doesn't confirm a voice_id is real). Distinct
    # from every voice above: not cinematic (Onyx), not ominous (Lewis), not
    # warm/reassuring (Bella), not soft/gentle (Nicole) — closer to a quiet,
    # measured philosophy-professor register.
    "asmr-life": {
        "profile": "DW-Narrator-Michael",
        "engine": "kokoro",
        "voice_id": "am_michael",
        "tone": "calm, grounded, contemplative — measured philosophy-teacher register",
    },
}

# Voicebox ships no Bengali (bn) voice in any engine — these pages cannot use it.
UNSUPPORTED_BENGALI = {"radio-deshal", "mamun-hossain"}


def voice_for(account):
    if account in UNSUPPORTED_BENGALI:
        raise RuntimeError(
            f"{account} is Bengali; Voicebox has no bn voice. Keep the existing pipeline.")
    if account not in VOICES:
        raise KeyError(f"no voice configured for {account}")
    return VOICES[account]


def ensure_all():
    """Create every configured profile in Voicebox (idempotent)."""
    from voicebox_client import ensure_profile
    out = {}
    for acct, v in VOICES.items():
        out[acct] = ensure_profile(v["profile"], v["engine"], v["voice_id"],
                                   description=v["tone"])
    return out


if __name__ == "__main__":
    import sys, json
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(ensure_all(), indent=1))
