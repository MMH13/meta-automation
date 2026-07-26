# -*- coding: utf-8 -*-
"""Mamun Hossain — Aug 1-7. 2 color-block posts/day (FB). Bengali AI/productivity.
Value-formula captions + save-CTA; several carry a copy-paste Prompt in first comment."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, when, mkdir, render
from image_block import block_post

IMG = mkdir("images/aug_mamun")
F = "\n\n📌 কাজে লাগলে সেভ করে রাখুন — পরে দরকার হবে।"

# entry: (block_text, theme, size, caption, first_comment_or_None)
POSTS = [
# ---- DAY 1 ----
("AI দিয়ে ইমেইল লেখা\n*বন্ধ করুন* —\n\nযতক্ষণ না এই\n*৩টা জিনিস* দিচ্ছেন 📧", "crimson", 66,
 """📧 AI-এর লেখা ইমেইল রোবটের মতো শোনায় কেন? কারণ আমরা শুধু বলি "একটা ইমেইল লেখো"।

সমাধান — এই ৩টা জিনিস দিন:
→ টোন: বন্ধুত্বপূর্ণ / প্রফেশনাল / সংক্ষিপ্ত
→ কে পড়বে: বস / ক্লায়েন্ট / সহকর্মী
→ শেষে কী চান: রিপ্লাই / মিটিং / পেমেন্ট

উদাহরণ: "ক্লায়েন্টকে বিনয়ীভাবে পেমেন্ট রিমাইন্ডার, সংক্ষিপ্ত, শেষে পরিশোধের তারিখ চাই।" — ফল রাতদিন তফাত।

🎁 রেডি Prompt প্রথম কমেন্টে।""" + F + "\n💬 আপনি AI দিয়ে কী কী লেখান? 👇",
 """🎁 Email Prompt (কপি করুন):

"You are my email assistant. Write a [tone: friendly/professional] email in Bengali to [recipient]. Context: [আপনার পরিস্থিতি]. Goal of the email: [reply/meeting/payment]. Keep it under 120 words, polite, with a clear call-to-action at the end."

স্ক্রিনশট সেভ করে রাখুন 📌👇"""),

("এই পেজে প্রতিদিন\nযা যা *পাবেন* 🎁\n\nFree AI Tool • Prompt •\nIncome Idea", "black", 66,
 """🎁 নতুন যারা এসেছেন — পরিচিত হয়ে যাই।

আমি মামুন। এই পেজে প্রতিদিন শেয়ার করি:
→ Free AI Tool — যেগুলো আসলেই কাজের
→ Copy-paste রেডি Prompt — প্রথম কমেন্টে
→ Skill আর ইনকামের Practical Idea — Hype ছাড়া
→ Productivity System — যা নিজে ব্যবহার করি

লক্ষ্য একটাই: AI-কে ভয় না পেয়ে কাজে লাগাতে শেখা, একসাথে।""" + F + "\n💬 আপনি কী নিয়ে সবচেয়ে বেশি জানতে চান? কমেন্টে বলুন 👇",
 None),

# ---- DAY 2 ----
("৫টা *Free AI Tool*\nযা আপনার কাজ\n*অর্ধেক* করে দেবে ⚙️\n\n(লিস্ট নিচে 👇)", "navy", 64,
 """⚙️ পেইড টুলের পেছনে টাকা ঢালার আগে — এই ৫টা ফ্রি টুল ট্রাই করুন:

→ লেখা ও আইডিয়া: ChatGPT / Gemini (ফ্রি ভার্সন)
→ ছবি: Bing Image Creator, Leonardo (ফ্রি ক্রেডিট)
→ নোট/সারাংশ: NotebookLM
→ প্রেজেন্টেশন: Gamma
→ ভয়েস/সাবটাইটেল: CapCut

একটা দিয়ে শুরু করুন, মাস্টার করুন, তারপর পরেরটা।

উদাহরণ: শুধু NotebookLM দিয়ে একটা ৩০ পেজের PDF ১০ মিনিটে বুঝে ফেলা যায়।""" + F + "\n💬 কোনটা আগে ট্রাই করবেন? 👇",
 None),

("AI দিয়ে ছবি বানানোর\n*সহজ Prompt ফর্মুলা* 🎨\n\n(এই ৪টা অংশ দিলেই হবে)", "charcoal", 62,
 """🎨 AI ছবি বাজে আসে কেন? কারণ আমরা শুধু লিখি "একটা সুন্দর ছবি"।

ভালো ছবির Prompt ফর্মুলা:
→ Subject: কী/কে (একটা লাল দরজা)
→ Style: বাস্তব / কার্টুন / 3D / oil painting
→ Light & Mood: সকালের নরম আলো, শান্ত
→ Detail: ক্যামেরা অ্যাঙ্গেল, রং, ব্যাকগ্রাউন্ড

এই ৪টা জোড়া লাগালেই ছবি ১০ গুণ ভালো।

🎁 রেডি ফর্মুলা Prompt প্রথম কমেন্টে।""" + F + "\n💬 কোন কাজে AI ছবি বানাতে চান? 👇",
 """🎁 Image Prompt ফর্মুলা (কপি করুন):

"[Subject] , [Style: photorealistic/3D/watercolor] , [Lighting & mood: soft morning light, calm] , [Details: camera angle, colors, background] , high detail, 4k"

উদাহরণ: "A red wooden door on an old brick wall, photorealistic, soft morning light, warm mood, slight vintage tone, high detail, 4k"

সেভ করে রাখুন 📌👇"""),

# ---- DAY 3 ----
("পুরো সপ্তাহ *Plan*\nকরে দেবে AI —\n২ মিনিটে 📅\n\n(Prompt কমেন্টে 👇)", "green", 62,
 """📅 রবিবার রাতে ১০ মিনিট প্ল্যান = পুরো সপ্তাহ ক্লিয়ার মাথায় কাজ।

কিন্তু প্ল্যান করাটাই ঝামেলা লাগে, তাই না?

এই Prompt আপনার Goal, সময় আর Energy অনুযায়ী পুরো সপ্তাহের বাস্তব প্ল্যান বানায় — বিশ্রামসহ। Robot-এর মতো না, মানুষের মতো।

উদাহরণ: "৩টা লক্ষ্য + সকালে এনার্জি বেশি" দিলে ও কঠিন কাজগুলো সকালে বসিয়ে দেয়।

🎁 Prompt প্রথম কমেন্টে।""" + F + "\n💬 আপনি প্ল্যান করে চলেন, নাকি যা আসে তাই সামলান? 😄👇",
 """🎁 Weekly Planner Prompt (কপি করুন):

"You are my productivity coach. My 3 main goals this week: [৩টা লক্ষ্য]. Fixed commitments: [জব/ক্লাস/পরিবার]. My peak energy time: [সকাল/দুপুর/রাত]. Create a realistic weekly plan in Bengali: 1) assign goals to days & time blocks, 2) keep hard tasks in peak energy hours, 3) add rest/buffer, 4) one small daily habit. Format as a day-by-day table."

স্ক্রিনশট সেভ করে রাখুন 📌👇"""),

("নতুন AI আগের চেয়ে\n*স্মার্ট* কেন? 🧠\n\nকারণ এখন এরা উত্তরের\nআগে *চিন্তা করে*", "black", 64,
 """🧠 খেয়াল করেছেন — নতুন AI আগের চেয়ে অনেক ভালো উত্তর দেয়?

কারণ এখন Reasoning ডিফল্ট। আগে AI সাথে সাথে উত্তর দিত। এখন প্রশ্নটা নিয়ে আগে "ভাবে", ধাপে ধাপে চিন্তা করে, তারপর উত্তর দেয় — অনেকটা মানুষের মতো।

মানে জটিল কাজে (অঙ্ক, Coding, Analysis, Planning) ভুল অনেক কমে গেছে।

কাজে লাগান: কঠিন প্রশ্নে বলুন "ধাপে ধাপে ভেবে উত্তর দাও" — ফল ভালো হবে।""" + F + "\n💬 আপনি কোন AI বেশি ব্যবহার করেন? 👇",
 None),

# ---- DAY 4 ----
("ChatGPT কে দিয়ে পড়া\n*মুখস্থ* করান —\n\nএই ৪ ধাপে 📚", "crimson", 64,
 """📚 পড়া মনে থাকে না? কারণ আমরা শুধু পড়ি, নিজেকে যাচাই করি না।

AI দিয়ে স্মার্ট পড়ার ৪ ধাপ:
→ টপিকটা AI-কে সহজ ভাষায় বোঝাতে বলুন
→ ওকে দিয়ে ৫টা প্রশ্ন বানান, নিজে উত্তর দিন
→ যেটা পারলেন না, সেটা আবার বোঝান
→ ২ দিন পর একই প্রশ্নে নিজেকে টেস্ট করুন

এটাই Active Recall — মুখস্থের চেয়ে ১০ গুণ শক্তিশালী।

🎁 রেডি Study Prompt প্রথম কমেন্টে।""" + F + "\n💬 পরীক্ষা সামনে কার? 👇",
 """🎁 Study Prompt (কপি করুন):

"You are my study tutor. Topic: [টপিক]. 1) Explain it in simple Bengali with one everyday example. 2) Then quiz me with 5 questions, one at a time, waiting for my answer. 3) After each answer, tell me if I'm right and explain briefly. 4) At the end, list what I should revise."

সেভ করে রাখুন 📌👇"""),

("AI দিয়ে *ইনকাম* —\n\n2026 সালের সবচেয়ে বড়\n*সুযোগ* 🚀\n\n(শুরুটা আজই হোক)", "navy", 66,
 """🚀 AI দিয়ে ইনকামের রাস্তা এখন অনেক — কিন্তু শুরু করতে হবে একটা দিয়ে:

→ Faceless Content (AI Voice + AI Video)
→ AI দিয়ে দ্রুত Freelancing (Writing, Design, VA)
→ ছোট Business-এর জন্য AI Automation সেটআপ
→ Prompt বিক্রি / AI Consulting

সবগুলোর ভিত্তি একটাই — AI-কে ভালোভাবে ব্যবহার করতে শেখা।

দিনে ২০ মিনিট শিখুন। ৩ মাস পরে নিজের পার্থক্য নিজেই দেখবেন।""" + F + "\n💬 কোন রাস্তাটা আপনার জন্য সবচেয়ে Interesting? 👇",
 None),

# ---- DAY 5 ----
("Freelancing-এ AI দিয়ে\n*দ্রুত কাজ* —\n\n৩টা বাস্তব উপায় 💼", "green", 64,
 """💼 AI ফ্রিল্যান্সারের চাকরি খাচ্ছে না — যে AI ব্যবহার করছে সে এগিয়ে যাচ্ছে।

কীভাবে কাজে লাগাবেন:
→ Writing: প্রথম ড্রাফট AI দিয়ে, তারপর নিজের হাতে ঘষামাজা
→ Design: আইডিয়া ও ভ্যারিয়েশন AI দিয়ে, ফাইনাল টাচ আপনার
→ Client কাজ: রিসার্চ ও আউটলাইন AI দিয়ে, ডেলিভারি দ্বিগুণ দ্রুত

উদাহরণ: ১টা আর্টিকেলে আগে ৩ ঘণ্টা লাগত, এখন ১ ঘণ্টা — কোয়ালিটি ঠিক রেখে।

মনে রাখুন: AI টুল, আপনি ড্রাইভার।""" + F + "\n💬 আপনি কী কাজ করেন / করতে চান? 👇",
 None),

("AI-কে ভালো প্রশ্ন\nকরার *গোপন সূত্র* 🔑\n\nRole + Task + Context +\nFormat", "charcoal", 60,
 """🔑 একই AI, কারও কাছে জাদু, কারও কাছে বাজে — পার্থক্য শুধু প্রশ্নে।

ভালো Prompt-এর ৪টা অংশ:
→ Role: "তুমি একজন অভিজ্ঞ ..." (কার মতো ভাববে)
→ Task: ঠিক কী চাও, স্পষ্ট করে
→ Context: তোমার পরিস্থিতি / দর্শক
→ Format: লিস্ট / টেবিল / ছোট প্যারা

উদাহরণ: "তুমি একজন নিউট্রিশনিস্ট। আমার (context) জন্য ৭ দিনের সহজ বাজেট মিল প্ল্যান দাও, টেবিল আকারে।"

🎁 টেমপ্লেট প্রথম কমেন্টে।""" + F + "\n💬 কোন কাজে Prompt বানাতে চান? বলুন, সাহায্য করি 👇",
 """🎁 Master Prompt টেমপ্লেট (কপি করুন):

"Role: You are a [expert]. Task: [ঠিক কী চান]. Context: [আপনার পরিস্থিতি/দর্শক]. Format: [list/table/short paragraphs]. Language: Bengali. Ask me one question first if anything is unclear."

সেভ করে রাখুন 📌👇"""),

# ---- DAY 6 ----
("দিনে *২০ মিনিট* AI শিখুন —\n\n৩ মাসে নিজেকে\n*চিনতে পারবেন না* 📈", "crimson", 62,
 """📈 বড় কোর্স, বড় প্ল্যান — বেশিরভাগ মানুষ ২ সপ্তাহে ছেড়ে দেয়।

সহজ পথ: দিনে মাত্র ২০ মিনিট।
→ সপ্তাহ ১-২: একটা টুল রোজ ব্যবহার (ChatGPT)
→ সপ্তাহ ৩-৪: ভালো Prompt লেখা শিখুন
→ মাস ২: নিজের কাজে অটোমেশন বসান
→ মাস ৩: একটা ছোট ইনকাম স্কিল দাঁড় করান

উদাহরণ: রোজ একটা রিয়েল কাজ AI দিয়ে করা — এটাই সেরা কোর্স।

Perfect Plan না, চালু রাখাটাই আসল।""" + F + "\n💬 আজ থেকে ২০ মিনিট — কে কে রাজি? 👇",
 None),

("যে ৩টা ভুল\n*বেশিরভাগ মানুষ*\nAI ব্যবহারে করে ❌", "black", 64,
 """❌ AI থেকে ভালো ফল না পাওয়ার আসল কারণ — এই ৩টা ভুল:

→ ভুল ১: এক লাইনের অস্পষ্ট প্রশ্ন। সমাধান: Role + Context দিন।
→ ভুল ২: প্রথম উত্তরেই থেমে যাওয়া। সমাধান: "আরও সংক্ষিপ্ত করো / উদাহরণ দাও" বলে ঘষুন।
→ ভুল ৩: চোখ বন্ধ করে বিশ্বাস। সমাধান: তথ্য যাচাই করুন, বিশেষত সংখ্যা ও রেফারেন্স।

উদাহরণ: একই প্রশ্ন ৩ বার রিফাইন করলে উত্তর প্রায় প্রফেশনাল লেভেলে চলে যায়।""" + F + "\n💬 কোন ভুলটা আপনি করতেন? 👇",
 None),

# ---- DAY 7 ----
("এক ক্লিকে বড় লেখা\n*সারাংশ* করান AI দিয়ে 📄\n\n(পড়ার সময় অর্ধেক)", "navy", 62,
 """📄 লম্বা আর্টিকেল, PDF, রিপোর্ট — সময় নেই পড়ার?

AI দিয়ে স্মার্ট সারাংশ:
→ "৫টা মূল পয়েন্টে সারাংশ করো"
→ "একজন ব্যস্ত মানুষের জন্য ৩ লাইনে বলো"
→ "কী করণীয় (action) সেটা আলাদা লিস্ট করো"
→ "কঠিন শব্দগুলো সহজ ভাষায় বুঝিয়ে দাও"

উদাহরণ: ৩০ পেজের রিপোর্ট → ৫ পয়েন্ট + ৩টা করণীয়, ২ মিনিটে।

🎁 রেডি Summary Prompt প্রথম কমেন্টে।""" + F + "\n💬 কী পড়তে সবচেয়ে বেশি সময় নষ্ট হয় আপনার? 👇",
 """🎁 Summary Prompt (কপি করুন):

"Summarize the text below in Bengali: 1) 5 key points as bullets, 2) a 3-line version for a busy person, 3) a separate list of action items, 4) explain any hard terms simply. Text: [এখানে পেস্ট করুন]"

সেভ করে রাখুন 📌👇"""),

("এই সপ্তাহে যা শিখলাম\n— এক সাথে 🎁\n\n(সেভ করার মতো পোস্ট)", "green", 62,
 """🎁 পুরো সপ্তাহের সারমর্ম, এক জায়গায় — সেভ করে রাখুন:

→ ইমেইল/লেখা: টোন + কে পড়বে + শেষে কী চান — দিন
→ ছবি: Subject + Style + Light + Detail
→ পড়া: বোঝাও → কুইজ → রিভিশন (Active Recall)
→ প্ল্যান: Goal + সময় + Energy দিয়ে AI প্ল্যান
→ Prompt সূত্র: Role + Task + Context + Format
→ অভ্যাস: দিনে ২০ মিনিট, চালু রাখুন

এই ৬টা জানলে আপনি বেশিরভাগ মানুষের চেয়ে এগিয়ে।""" + F + "\n💬 কোনটা এই সপ্তাহে সবচেয়ে কাজে লাগল? 👇",
 None),
]

assert len(POSTS) == 14, len(POSTS)
HOURS = [7, 15]  # 2 posts/day, UTC (=13:00 & 21:00 BD)


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    n_img = 0
    for i, (text, theme, size, caption, fc) in enumerate(POSTS):
        di, pi = divmod(i, 2)
        iid = f"amn-d{di+1}-{pi+1}"
        if iid in have:
            continue  # resume: already enqueued
        img_path = f"{IMG}/d{di+1}_{pi+1}.png"
        render(block_post, text, img_path, theme=theme, size=size)
        n_img += 1
        print(f"  rendered {img_path}")
        item = {"id": iid, "account": "mamun-hossain", "network": "facebook",
                "type": "photo", "message": caption, "image_url": img_path,
                "when": when(di, HOURS[pi]), "status": "pending"}
        if fc:
            item["first_comment"] = fc
        items.append(item)
    save(q)
    print(f"MAMUN HOSSAIN: rendered {n_img} images, queue now {len(items)} items")


if __name__ == "__main__":
    build()
