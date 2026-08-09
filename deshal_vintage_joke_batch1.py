# -*- coding: utf-8 -*-
"""Radio Deshal — exact-format replica of a reference page's dialogue-joke
posts (2026-08-03, user shared screenshots and asked for the literal visual
style: aged book-page background, green-highlighter setup line, white-
highlighter dialogue block, plain punchline, FB-icon watermark corner).
Every joke here is an ORIGINAL scenario written for this batch — none
reproduce the reference page's actual content, only its visual format."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_deshal import deshal_vintage_joke

IMG = mkdir("images/deshal_vintage1")
F = "\n\n📻 রেডিও দেশাল"

# (setup, [dialogue lines], punch, punch_emoji, caption)
POSTS = [
 ("শাশুড়ি বললেন ছেলের বউকে-",
  ["তুমি তো রোজ রাতে কার সাথে যেন ফোনে কথা বলো-",
   "আমি বললাম, আম্মা সে তো আমার অফিসের বস, কাজের কথা বলি।"],
  "তাহলে আমিও তোমার বসের সাথে একটু কথা বলি-?", "😏",
  "😅 শাশুড়ি বনাম বউ, রাউন্ড ১! এই পরিস্থিতিতে আপনি কার পক্ষে? 👇" + F),

 ("স্বামী স্ত্রীকে মেসেজ দিলো-",
  ["আজকে অফিসে অনেক কাজ, রাতে দেরি হবে ফিরতে-",
   "স্ত্রী রিপ্লাই দিলো, ঠিক আছে, নীলা আপাও তো বলল তার হাজব্যান্ডেরও আজ দেরি হবে।"],
  "স্বামী সাথে সাথে রিপ্লাই দিলো- আচ্ছা থাক, আজ তাড়াতাড়িই ফিরছি।", "😂",
  "😆 এক লাইনেই প্ল্যান ক্যান্সেল! কে কে এই টাইপ রিপ্লাই আগে দেখেছেন? 👇" + F),

 ("একজন স্বামী স্ত্রীকে জিজ্ঞেস করলো-",
  ["তুমি তো বলছিলে শপিং এ যাবে, এত তাড়াতাড়ি ফিরে আসলে যে?",
   "স্ত্রী বলল, তোমার মায়ের সাথে দেখা হয়ে গেলো মার্কেটে, তাই ফিরে আসলাম।"],
  "স্বামী বলল- বাহ, তাহলে তো আম্মাকে রোজ মার্কেটে পাঠাতে হবে।", "😆",
  "😂 এই এক লাইন সমাধান কেউ ভাবতে পারবে না! রিলেট করলে কমেন্টে জানান 👇" + F),

 ("প্রতিবেশী আন্টি আমাকে বললেন-",
  ["তোমার আব্বু-আম্মু তো রোজ সন্ধ্যায় ছাদে হাঁটেন, খুব romantic couple তো!",
   "আমি বললাম, হ্যাঁ আন্টি, ওটা আসলে হাঁটা না, দুজনে ঝগড়া করার জায়গা খুঁজে বের করছেন যেখানে আমরা শুনতে পাই না।"],
  "আন্টি হাসতে হাসতে বললেন- ওহ তাহলে এটাও romantic ব্যাপার!", "😂",
  "😅 প্রতিটা পরিবারেই এই \"ছাদে হাঁটা\" একটা ইনস্টিটিউশন! কে কে চেনেন এই কাপল? 👇" + F),
]

assert len(POSTS) == 4

SLOTS = [
 "2026-08-09T03:00:00+00:00",
 "2026-08-09T08:00:00+00:00",
 "2026-08-09T12:00:00+00:00",
 "2026-08-09T16:00:00+00:00",
]


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n = 0
    for idx, ((setup, lines, punch, emoji, caption), when) in enumerate(zip(POSTS, SLOTS), 1):
        iid = f"deshal-vjoke1-{idx}"
        if iid in have:
            continue
        img = f"{IMG}/{idx}.png"
        render(deshal_vintage_joke, out_path=img, setup=setup,
               dialogue_lines=lines, punch=punch, punch_emoji=emoji)
        it = {"id": iid, "account": "radio-deshal", "network": "facebook",
              "type": "photo", "message": caption, "image_url": img,
              "when": when, "status": "pending"}
        items.append(it)
        n += 1
        print(f"  {iid} -> {when}")
    save(q)
    print(f"queued {n} vintage-joke items, total {len(items)}")


if __name__ == "__main__":
    build()
