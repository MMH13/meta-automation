# -*- coding: utf-8 -*-
"""AI-generated scene art via OpenAI's image model (gpt-image-1) — an
alternative to image_ai.py's Gemini pipeline and to Pexels stock footage,
for pages/scenes where a specific custom illustrated look is wanted rather
than a real photo or an SVG illustration.

Key comes from accounts.json ("openai_api_key"), same pattern as
gemini_api_key/pexels_api_key.

Usage:
    from image_dalle import generate_dalle_image
    generate_dalle_image("a moody flat-illustration house at night, one lit "
                         "window, dark horror atmosphere", "images/house.png",
                         size="1024x1536")
"""
import base64
import json
from pathlib import Path

import requests

_HERE = Path(__file__).parent
_CONF = json.loads((_HERE / "accounts.json").read_text(encoding="utf-8"))
API_KEY = _CONF["openai_api_key"]
MODEL = "gpt-image-1"
URL = "https://api.openai.com/v1/images/generations"

# gpt-image-1 supports these exact sizes only.
SIZES = {
    "square": "1024x1024",
    "portrait": "1024x1536",   # closest to 9:16/1:1 reel & square-video use
    "landscape": "1536x1024",
}


def generate_dalle_image(prompt: str, out_path: str, size: str = "portrait",
                         quality: str = "medium") -> str:
    """Generate an image from a text prompt. size: 'square'|'portrait'|
    'landscape' or an exact 'WxH' string. quality: 'low'|'medium'|'high'.
    Returns the local path written."""
    px = SIZES.get(size, size)
    body = {"model": MODEL, "prompt": prompt, "size": px, "quality": quality, "n": 1}
    r = requests.post(URL, headers={"Authorization": f"Bearer {API_KEY}"},
                      json=body, timeout=180)
    if r.status_code >= 400:
        raise RuntimeError(f"OpenAI {r.status_code}: {r.text[:800]}")
    img_b64 = r.json()["data"][0]["b64_json"]
    out = Path(out_path)
    if not out.is_absolute():
        out = _HERE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(img_b64))
    return str(out)


if __name__ == "__main__":
    p = generate_dalle_image(
        "A moody flat-illustration style house at night, one lit window, "
        "dark navy and near-black palette, subtle red glow in the sky, "
        "horror atmosphere, minimalist, no text",
        "images/_dalle_test.png", size="portrait")
    print("wrote", p)
