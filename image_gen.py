"""Branded post-image generator for the Meta hub.

generate_card() makes a 1080x1080 square card (works for both Facebook and,
later, Instagram): soft vertical gradient, accent bar, big headline, optional
bullet list or subtitle, brand footer.

Brands are defined in BRANDS; add one per page. Usage:
    from image_gen import generate_card
    generate_card(
        title="Walk 10 Minutes After Every Meal",
        subtitle="Your blood sugar will thank you",
        bullets=["Flattens sugar spikes", "Boosts digestion"],
        brand="health-daily",
        out_path="images/walk-after-meals.png",
    )
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

_HERE = Path(__file__).parent
FONT_DIR = Path(r"C:\Windows\Fonts")

BRANDS = {
    "health-daily": {
        "name": "HEALTH DAILY",
        "tagline": "Stay Healthy",
        # deep green -> teal gradient, warm off-white text
        "grad_top": (11, 66, 50),
        "grad_bottom": (16, 108, 87),
        "accent": (110, 231, 183),
        "text": (245, 250, 247),
        "muted": (190, 215, 205),
        "footer": "Follow for daily health tips",
    },
    "mamun-hossain": {
        "name": "MAMUN HOSSAIN",
        "tagline": "Work Smarter with AI",
        # deep navy -> indigo gradient, electric cyan accent
        "grad_top": (13, 20, 48),
        "grad_bottom": (32, 42, 96),
        "accent": (86, 214, 255),
        "text": (245, 248, 255),
        "muted": (170, 185, 220),
        "footer": "Follow @IamMdMamunHossain",
    },
}

SIZE = 1080
MARGIN = 96


def _font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def generate_card(title: str, out_path: str, brand: str = "health-daily",
                  subtitle: str = "", bullets: list[str] | None = None) -> str:
    b = BRANDS[brand]
    img = Image.new("RGB", (SIZE, SIZE))
    d = ImageDraw.Draw(img)

    # vertical gradient
    top, bot = b["grad_top"], b["grad_bottom"]
    for y in range(SIZE):
        t = y / SIZE
        d.line([(0, y), (SIZE, y)],
               fill=tuple(round(top[i] + (bot[i] - top[i]) * t) for i in range(3)))

    # subtle oversized circle, top-right, for depth
    d.ellipse([SIZE - 420, -260, SIZE + 260, 420],
              outline=tuple(min(255, c + 14) for c in top), width=44)

    # brand header
    f_brand = _font("arialbd.ttf", 40)
    d.text((MARGIN, MARGIN), b["name"], font=f_brand, fill=b["accent"])
    w = d.textlength(b["name"], font=f_brand)
    d.text((MARGIN + w + 24, MARGIN + 2), f"|  {b['tagline']}",
           font=_font("segoeui.ttf", 38), fill=b["muted"])

    # accent bar
    bar_y = MARGIN + 92
    d.rectangle([MARGIN, bar_y, MARGIN + 130, bar_y + 12], fill=b["accent"])

    # title (auto-shrink to fit)
    max_w = SIZE - 2 * MARGIN
    size = 96
    while size > 54:
        f_title = _font("arialbd.ttf", size)
        lines = _wrap(d, title, f_title, max_w)
        if len(lines) <= 4:
            break
        size -= 6
    y = bar_y + 60
    for line in lines:
        d.text((MARGIN, y), line, font=f_title, fill=b["text"])
        y += int(size * 1.18)

    # subtitle
    if subtitle:
        y += 20
        f_sub = _font("segoeui.ttf", 46)
        for line in _wrap(d, subtitle, f_sub, max_w):
            d.text((MARGIN, y), line, font=f_sub, fill=b["muted"])
            y += 60

    # bullets with check circles (footer needs the last ~110px)
    if bullets:
        y += 36
        floor = SIZE - 150
        step = 80
        bsize = 44
        if y + step * len(bullets) > floor:  # shrink to fit, floor is hard
            step = max(52, (floor - y) // len(bullets))
            bsize = 34 if step < 64 else 38
        f_b = _font("segoeui.ttf", bsize)
        for item in bullets:
            cy = y + step // 2 - 8
            d.ellipse([MARGIN, cy - 24, MARGIN + 48, cy + 24], fill=b["accent"])
            # checkmark drawn as a polyline (glyph coverage varies by font)
            d.line([(MARGIN + 12, cy + 1), (MARGIN + 21, cy + 11),
                    (MARGIN + 37, cy - 11)], fill=b["grad_top"], width=6,
                   joint="curve")
            d.text((MARGIN + 76, cy), item, font=f_b, fill=b["text"],
                   anchor="lm")
            y += step

    # footer
    f_foot = _font("segoeui.ttf", 34)
    d.text((MARGIN, SIZE - 72), b.get("footer", ""),
           font=f_foot, fill=b["muted"], anchor="ls")

    out = Path(out_path)
    if not out.is_absolute():
        out = _HERE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    return str(out)


if __name__ == "__main__":
    import sys
    p = generate_card(
        title=sys.argv[1] if len(sys.argv) > 1 else "Sample Card Title",
        out_path="images/sample.png",
        subtitle="A subtitle goes here",
        bullets=["First benefit", "Second benefit", "Third benefit"],
    )
    print("wrote", p)
