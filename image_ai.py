"""AI photo-style post images via Google Gemini (nano-banana image model).

Generates photorealistic, organic-looking post images — modeled on the style
of top BD creator pages (handwritten note held in hand, warm bokeh, etc.) —
with Bengali or English text rendered inside the scene.

Key comes from accounts.json ("gemini_api_key"). Usage:
    from image_ai import generate_ai_image, STYLES
    generate_ai_image(text="৫টা ফ্রি AI টুল ...", style="torn_paper",
                      out_path="images/foo.png")
"""

import base64
import json
from pathlib import Path

import requests

_HERE = Path(__file__).parent
_CONF = json.loads((_HERE / "accounts.json").read_text(encoding="utf-8"))
API_KEY = _CONF["gemini_api_key"]
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# Scene presets. {text} is replaced with the display text.
STYLES = {
    "torn_paper": (
        "Photorealistic photo: a hand holding a piece of torn white paper with "
        "rough deckled edges, in front of a cozy blurred living-room background "
        "with warm golden bokeh lights. On the paper, neat handwritten text in "
        "dark blue ink reads exactly:\n\n{text}\n\n"
        "The handwriting is casual but very legible, natural pen strokes. "
        "Soft warm indoor lighting, shallow depth of field, shot on a phone "
        "camera, vertical 4:5 composition. Render the text EXACTLY as given, "
        "with correct Bengali script."
    ),
    "whiteboard": (
        "Photorealistic photo: a small white desktop whiteboard on a wooden desk "
        "next to a laptop and a coffee mug, morning window light. Handwritten "
        "marker text in dark blue reads exactly:\n\n{text}\n\n"
        "Legible marker handwriting, slight glare on the board, shallow depth "
        "of field, vertical 4:5 composition. Render the text EXACTLY as given, "
        "with correct Bengali script."
    ),
    "sticky_note": (
        "Photorealistic photo: a large pastel-yellow sticky note stuck on a "
        "laptop screen bezel in a dim cozy workspace, desk lamp glow and blurred "
        "monitor light in the background. Handwritten text in black ink on the "
        "note reads exactly:\n\n{text}\n\n"
        "Neat legible handwriting, shallow depth of field, vertical 4:5 "
        "composition. Render the text EXACTLY as given, with correct Bengali "
        "script."
    ),
    "notebook": (
        "Photorealistic photo: an open spiral notebook on a wooden cafe table "
        "with a pen resting on it and a cup of tea nearby, warm afternoon light. "
        "Handwritten text in dark ink on the page reads exactly:\n\n{text}\n\n"
        "Casual legible handwriting, shallow depth of field, vertical 4:5 "
        "composition. Render the text EXACTLY as given, with correct Bengali "
        "script."
    ),
}


def generate_ai_image(text: str, out_path: str, style: str = "torn_paper",
                      extra: str = "") -> str:
    """Generate a photo-style image with the given text in-scene. Returns path."""
    prompt = STYLES[style].format(text=text)
    if extra:
        prompt += " " + extra
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "4:5"},
        },
    }
    r = requests.post(URL, params={"key": API_KEY}, json=body, timeout=180)
    if r.status_code >= 400:
        raise RuntimeError(f"Gemini {r.status_code}: {r.text[:800]}")
    parts = r.json()["candidates"][0]["content"]["parts"]
    img_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    out = Path(out_path)
    if not out.is_absolute():
        out = _HERE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(img_b64))
    return str(out)


if __name__ == "__main__":
    p = generate_ai_image("পরীক্ষা: বাংলা লেখা\nসঠিকভাবে আসছে কি?",
                          "images/ai_test.png")
    print("wrote", p)
