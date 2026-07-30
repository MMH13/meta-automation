# -*- coding: utf-8 -*-
"""Radio Deshal — dialogue setup->twist jokes. New format, structure learned
from a reference page's posts (2026-07-30): highlighted hook line, plain
dialogue body, bolded punchline. Every joke here is an original scenario —
none reproduce the reference page's actual content. One post from that
reference set (the "government job" one) normalized child marriage and was
explicitly excluded as a model for anything."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_deshal import deshal_joke

IMG = mkdir("images/deshal_joke1")
F = "\n\n📻 রেডিও দেশাল"

# (hook, [body lines], punch, punch_emoji, caption)
POSTS = [
 ("সকালে ঘুম থেকে উঠে বারান্দায় দাঁড়িয়েছি-",
  ["পাশের বাসার আন্টি দেখে জিজ্ঞেস করলেন, \"বাবা তুমি এই বাসায় নতুন কাজ শুরু করেছো?\"",
   "আমি বললাম, \"আন্টি আমি তো এই বাসারই ছেলে, তিন বছর ধরে থাকি!\"",
   "আন্টি বললেন, \"তাই নাকি! তোমাকে তো কখনো এত সকালে দেখিনি-\""],
  "তিন বছরে প্রথমবার সকাল দেখাতেই আন্টি চিনতেই পারলেন না", "😅",
  "😂 তিন বছরের প্রতিবেশী, তাও সকাল ৭টায় অচেনা! কে কে এই লেভেলের \"রাত জাগা মানুষ\"? 👇" + F),

 ("সেদিন থেকে একটা জিনিস মাথায় ঘুরছে-",
  ["রুটিকে বাংলায় \"রুটি\" বলি, পরোটাকেও একরকম রুটিই বলা যায়-",
   "তাহলে পিৎজাকে কেন \"রুটি\" না বলে ইংরেজিতেই বলি?"],
  "উত্তর খুঁজতে খুঁজতে খিদাই লেগে গেলো", "😂",
  "😄 এই প্রশ্নের কোনো উত্তর নাই, শুধু ক্ষুধা বাড়ে। কে কে একমত? 👇" + F),

 ("কাজিনের বিয়েতে বন্ধুকে নিয়ে গিয়েছি-",
  ["মামী দেখেই জিজ্ঞেস করলেন, \"এই ছেলেটা কে?\"",
   "আমি কিছু বলার আগেই বন্ধু বলে উঠলো-"],
  "\"আমি ওর কোচিং ব্যাচমেট\"", "😄",
  "😂 বিয়ে বাড়িতে বন্ধু আনার আগে এক্সপ্লানেশন রেডি রাখা লাগে। কে কে এই পরিস্থিতিতে পড়েছেন? 👇" + F),

 ("স্ত্রী রেগে স্বামীকে বললো-",
  ["\"তোমাকে না বলেছি লিস্ট দেখে বাজার করতে, খালি মাথায় বাজার করো কেন?\"",
   "স্বামী বললো, \"আমি তো লিস্ট দেখেই এনেছি!\"",
   "স্ত্রী বললো, \"তাহলে পেঁয়াজ কই?\""],
  "স্বামী লিস্টটাই বাসায় ফেলে বাজারে গিয়েছিল", "😂",
  "😅 লিস্ট নিয়ে বাজারে যাওয়া আর লিস্ট মনে রাখা— দুইটা আলাদা স্কিল। কে কে ভুক্তভোগী? 👇" + F),
]

assert len(POSTS) == 4

SLOTS = [
 "2026-08-08T03:00:00+00:00",
 "2026-08-08T08:00:00+00:00",
 "2026-08-08T12:00:00+00:00",
 "2026-08-08T16:00:00+00:00",
]


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n = 0
    for idx, ((hook, body, punch, emoji, caption), when) in enumerate(zip(POSTS, SLOTS), 1):
        iid = f"ard-joke1-{idx}"
        if iid in have:
            continue
        img = f"{IMG}/{idx}.png"
        render(deshal_joke, hook, body, punch, img, punch_emoji=emoji)
        n += 1
        print(f"  {iid} -> {img}")
        items.append({"id": iid, "account": "radio-deshal", "network": "facebook",
                      "type": "photo", "message": caption, "image_url": img,
                      "when": when, "status": "pending"})
    save(q)
    print(f"queued {n} new jokes, total items {len(items)}")


if __name__ == "__main__":
    build()
