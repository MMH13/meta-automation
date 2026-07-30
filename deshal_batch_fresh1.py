# -*- coding: utf-8 -*-
"""Radio Deshal — short funny memes, back to the established format.
User corrected direction: no long-form story, wants short punchy laugh-and-
interact memes (the standing meme-system mandate). Fresh topics only — none
of these repeat what's already queued/posted in the last ~40 items."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_meme import meme_statement, meme_nobody, meme_split

IMG = mkdir("images/deshal_fresh1")
F = "\n\n📻 রেডিও দেশাল"

# (kind, args-dict, caption)
POSTS = [
 ("stmt", dict(text="যেকোনো বিপদেই\nমায়ের *প্রথম প্রশ্ন* —\n\n\"খাইছো?\" 🍚", theme="yellow", emoji="", size=76),
  "😄 বাড়ি পুড়ে গেলেও মা আগে জিজ্ঞেস করবে ভাত খেয়েছি কিনা। কে কে confirm করবেন? 👇" + F),

 ("split", dict(top_text="রিকশাওয়ালা:\n\"৫০ টাকা\" 🛺", bottom_text="আমি:\n\"৩০ টাকা যাবো\" 😤",
                top_theme="sky", bottom_theme="black", top_emoji="", bottom_emoji=""),
  "😂 শেষে ঠিক ৪০ টাকাতেই মিটমাট। এই নাটক ছাড়া রিকশা ভ্রমণ অসম্পূর্ণ। কে কে এক্সপার্ট? 👇" + F),

 ("stmt", dict(text="ফ্রিজ খুলে কিছু নেই\nদেখেও —\n\n*২ মিনিট পর* আবার খুলি 🧊", theme="black", emoji="", size=78),
  "😅 যদি হঠাৎ নতুন কিছু গজিয়ে যায়! এই অভ্যাস কার কার আছে? 👇" + F),

 ("split", dict(top_text="বাসায়:\n\"দাঁতে অসহ্য ব্যথা\" 😖", bottom_text="ডেন্টিস্টের চেয়ারে:\n\"না না, ব্যথা নাই তো\" 😅",
                top_theme="red", bottom_theme="white", top_emoji="", bottom_emoji=""),
  "😂 দাঁতের ব্যথা ডাক্তার দেখেই ভয়ে পালায়। কে কে এই মিথ্যাবাদী? 👇" + F),

 ("stmt", dict(text="অনলাইনে ছবি দেখে অর্ডার —\n\nহাতে পেয়ে বুঝি,\n*ছবিটাই আসল প্রোডাক্ট* ছিল 📦😭", theme="green", emoji="", size=70),
  "😩 ছবির লাইটিং আর বাস্তবতার মধ্যে একটা মহাসাগর দূরত্ব। কার সাথে এমন হয়েছে? 👇" + F),

 ("nobody", dict(setup="মিটিং বা ক্লাসে\nঘুম পেলে:", punch="চোখ খোলা রেখেই\n*ভেতরে ভেতরে ঘুমাই* 😴", theme="yellow", emoji=""),
  "😄 এই স্কিলটা কোনো সার্টিফিকেট কোর্সে শেখানো হয় না, তাও সবাই এক্সপার্ট। কে কে পারেন? 👇" + F),

 ("stmt", dict(text="নতুন জামা পরে বের হওয়ার\n*১ ঘণ্টার মধ্যেই* —\n\nএকটা দাগ লেগেই যায় 😩", theme="sky", emoji="", size=76),
  "😅 নতুন জামা আর দাগ যেন একসাথেই জন্মায়। কার সাথে আজ বা কালই হয়েছে? 👇" + F),
]

assert len(POSTS) == 7

SLOTS = [
 "2026-07-31T03:00:00+00:00",
 "2026-07-31T06:00:00+00:00",
 "2026-07-31T09:00:00+00:00",
 "2026-07-31T11:00:00+00:00",
 "2026-07-31T13:00:00+00:00",
 "2026-07-31T17:00:00+00:00",
 "2026-07-31T19:00:00+00:00",
]


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n = 0
    for idx, ((kind, args, caption), when) in enumerate(zip(POSTS, SLOTS), 1):
        iid = f"ard-fresh1-{idx}"
        if iid in have:
            continue
        img = f"{IMG}/{idx}.png"
        fn = {"stmt": meme_statement, "nobody": meme_nobody, "split": meme_split}[kind]
        render(fn, out_path=img, **args)
        n += 1
        print(f"  {iid} -> {img}")
        items.append({"id": iid, "account": "radio-deshal", "network": "facebook",
                      "type": "photo", "message": caption, "image_url": img,
                      "when": when, "status": "pending"})
    save(q)
    print(f"queued {n} new memes, total items {len(items)}")


if __name__ == "__main__":
    build()
