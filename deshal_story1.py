# -*- coding: utf-8 -*-
"""Radio Deshal — first long-form narrative ('গল্প') post.

Format modeled on the reference post the user linked (a long story-style
post on a Bengali page, ~2.7K reactions / 46 comments / 12 shares): a themed
cover card + a full, complete story as the caption — distinct from this
page's usual short punchy meme one-liners.

The story itself is 100% original — the reference post's actual text was
behind Facebook's login wall and never read, so nothing here is copied or
reconstructed from it. Only the FORMAT and emotional register (quiet
friendship, care read as cleverness) are matched, based on what was visible
in public comments and alt-text.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_deshal import deshal_story

IMG = mkdir("images/deshal_story")

TITLE = "ক্লাসের সবচেয়ে 'কম বুদ্ধির' ছেলেটা"

CARD_STORY = """আমাদের ক্লাসে একটা ছেলে ছিল — রাফি। সারাক্ষণ চুপচাপ, পড়ায় তেমন ভালো না। তাই সবাই ওকে একটু *কম বুদ্ধির* বলে ক্ষ্যাপাতো।

ফাইনাল পরীক্ষার দিন আমার সবচেয়ে কাছের বন্ধুর হঠাৎ হাত কাঁপতে শুরু করল। চোখে পানি, কলম ধরেই রাখতে পারছে না।

কেউ কিছু বোঝার আগেই রাফি উঠে গিয়ে ওর পাশে বসল। কিছু বলল না। শুধু হাতটা ধরে রাখল, যতক্ষণ না কাঁপুনি থামে।

পরীক্ষা শেষে বন্ধু বলেছিল — "ও যদি তখন ওটা না করত, আমি পুরো পরীক্ষাটাই মিস করতাম।"

যাকে আমরা *কম বুদ্ধি* বলতাম, সেদিন বুঝলাম — কিছু বুদ্ধি থাকে বইয়ে না, থাকে *মনে*।"""

CAPTION = """ক্লাসের সবচেয়ে "কম বুদ্ধির" ছেলেটা 💛

আমাদের ক্লাসে একটা ছেলে ছিল, নাম রাফি। সারাক্ষণ চুপচাপ থাকত, পড়াশোনায় তেমন ভালো ছিল না। রেজাল্ট বের হলেই সবাই একটু হাসাহাসি করত — "রাফির মাথায় বুদ্ধি কম, ওকে দিয়ে কিচ্ছু হবে না।"

রাফিও কিছু বলত না। শুনত, মাথা নিচু করত, তারপর আবার নিজের মতো চুপচাপ বসে থাকত।

ফাইনাল পরীক্ষার দিনের কথা। আমার সবচেয়ে কাছের বন্ধু — যে সারা বছর সবচেয়ে ভালো ছাত্রী ছিল — হঠাৎ পরীক্ষার হলে অস্থির হয়ে উঠল। হাত কাঁপছে, চোখে পানি, কলম ধরেই রাখতে পারছে না। প্যানিক অ্যাটাকের মতো কিছু একটা হচ্ছিল ওর সাথে।

শিক্ষক তখনও খেয়াল করেননি। ক্লাসের কেউ কী করবে বুঝে ওঠার আগেই, রাফি — সেই "কম বুদ্ধির" ছেলেটা — চুপচাপ উঠে গিয়ে ওর পাশের বেঞ্চে বসল।

কিছু বলল না। কোনো প্রশ্ন করল না। শুধু ওর হাতটা ধরে রাখল, যতক্ষণ না কাঁপুনি থামল। তারপর নিঃশব্দে নিজের সিটে ফিরে গেল, যেন কিছুই হয়নি।

পরীক্ষা শেষে আমার বন্ধু কেঁদে ফেলেছিল। বলেছিল — "ও যদি তখন ওটা না করত, আমি পুরো পরীক্ষাটাই মিস করতাম। হয়তো পুরো বছরটাই।"

আমরা যাকে বছরের পর বছর "কম বুদ্ধি" বলে ডেকেছি, সেদিন বুঝলাম — কিছু বুদ্ধি বইয়ে থাকে, নম্বরে মাপা যায়। আর কিছু বুদ্ধি থাকে মনে — যেটার কোনো পরীক্ষা হয় না, কিন্তু ঠিক সময়ে ঠিক জায়গায় হাজির হয়।

রাফি হয়তো কোনোদিন ক্লাসে ফার্স্ট হয়নি। কিন্তু সেদিন হলে ও যা করেছিল, সেটা কোনো বইয়ে শেখানো যায় না।

💬 আপনার জীবনেও কি এমন কেউ ছিল, যাকে সবাই ভুল বুঝেছিল, কিন্তু আসল সময়ে সে-ই পাশে দাঁড়িয়েছিল? কমেন্টে লিখুন 👇

🔁 শেয়ার করুন সেই মানুষটার কথা মনে করে, যে চুপচাপ আপনার পাশে দাঁড়িয়েছিল।"""


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    iid = "ard-story-01"
    if iid in have:
        print("already queued, skipping")
        return
    img = f"{IMG}/story01.png"
    render(deshal_story, TITLE, CARD_STORY, img, kicker="আজকের গল্প", emoji="💛")
    print(f"rendered {img}")

    when = "2026-07-31T15:00:00+00:00"  # 21:00 BD, evening prime time, open slot
    items.append({"id": iid, "account": "radio-deshal", "network": "facebook",
                  "type": "photo", "message": CAPTION, "image_url": img,
                  "when": when, "status": "pending"})
    save(q)
    print(f"queued {iid} for {when}")


if __name__ == "__main__":
    build()
