# -*- coding: utf-8 -*-
"""Mamun Hossain — 10-day color-block batch (2/day = 20 posts).
Format modeled on top-performing BD AI-creator style: solid color block,
big bold Bengali+English code-switched text, yellow accent on *starred* words.
Original content (my own framing). Prompt posts deliver the prompt as the
page's FIRST COMMENT.
Entry: (block_text, theme, size, caption, first_comment_or_None)
"""

F = "\n\nFollow 👉 Mamun Hossain — প্রতিদিন নতুন AI টিপস, Tool আর Prompt।"

POSTS = [
# ===== DAY 1 =====
("2026 এ AI শুধু\nAnswer দেয় না —\n\nএখন সে *নিজে কাজটা*\n*করেও দেয়* 🤖\n\n(যারা আগে বুঝবে,\nতারা 5 জনের কাজ একা করবে)", "black", 64,
 """🤖 এই বছরের সবচেয়ে বড় পরিবর্তন — AI এখন শুধু চ্যাট করে না, নিজে কাজ করে ফেলে।

আগে: "কীভাবে ইমেইল লিখব?" জিজ্ঞেস করতেন, ও বলে দিত, আপনি লিখতেন।
এখন: AI Agent নিজেই খুঁজে বের করে, লেখে, পাঠিয়েও দেয়।

Gartner বলছে — 2026 সালেই 40% অফিস Software-এ এই Agent ঢুকে যাচ্ছে।

যে কাজ বারবার করেন, সেটা AI-কে একবার শিখিয়ে দিলেই হবে। রুটিন কাজ থেকে মুক্তি।

💬 আপনার কোন কাজটা AI দিয়ে Automate করতে চান? কমেন্টে লিখুন 👇""" + F, None),

("Google এর এই Tool টা\nএখনো 90% মানুষ\n*চেনেই না* 📚\n\nঅথচ পুরো *বই আপলোড*\nকরলেই — পড়া রেডি ✨", "crimson", 66,
 """📚 স্টুডেন্ট আর যারা পড়ে শিখতে চান — এই মুহূর্তের সেরা ফ্রি Tool: Google NotebookLM.

→ PDF, নোট, বই, এমনকি YouTube লিংক আপলোড করুন
→ শুধু সেই ডকুমেন্ট থেকে উত্তর — বাইরের ভুল তথ্য না
→ Summary, টাইমলাইন, Study Guide বানিয়ে দেয়
→ এমনকি আপনার নোট থেকে Podcast বানায় — দুইজন হোস্ট আলোচনা করছে এমন Audio! 🎧

পরীক্ষার আগে 200 পেজের বই? আপলোড → স্টাডি গাইড → রেডি।

notebooklm.google.com — ফ্রি, শুধু Gmail লাগবে।

💬 পরিচিত কোনো Student কে ট্যাগ করুন — যার এটা দরকার 👇""" + F, None),

# ===== DAY 2 =====
("ChatGPT-কে বানিয়ে ফেলুন\nনিজের *Content Planner* 📅\n\nপুরো *30 দিনের* Idea\n2 মিনিটে রেডি\n\n(Prompt টা কমেন্টে 👇)", "navy", 64,
 """📅 কনটেন্ট বানাতে বসে "আজ কী পোস্ট করব?" — এই চিন্তায় আর সময় নষ্ট না।

একটা Prompt দিয়ে দিলাম, যেটা আপনার Niche অনুযায়ী পুরো 30 দিনের কনটেন্ট Idea বানিয়ে দেবে — এক ক্লিকে। Hook, Format, Engagement question — সব সাজিয়ে।

🎁 Prompt টা প্রথম কমেন্টে। কপি করে ChatGPT বা Claude-এ পেস্ট করুন।

💬 আপনি কী নিয়ে কনটেন্ট বানান? কমেন্টে জানান 👇""" + F,
 """🎁 30-Day Content Plan Prompt (কপি করুন):

"You are my content strategist. My niche: [আপনার নিশ]. My audience: [কারা]. Platform: Facebook. Create a 30-day content plan. For each day give: 1) topic, 2) hook (first line in Bengali), 3) format (list/story/tips/prompt), 4) one engagement question, 5) 3 hashtags. Friendly conversational Bengali, not corporate."

[ব্র্যাকেটের] জায়গায় নিজের তথ্য বসান — পুরো মাসের প্ল্যান রেডি! কাজে লাগলে জানাবেন 👇"""),

("গুগলে *30 মিনিট* ❌\n\nPerplexity-তে\n*30 সেকেন্ড* ✅\n\nResearch এর নিয়ম\nবদলে গেছে", "charcoal", 74,
 """🔍 এখনো Research এর জন্য শুধু Google ব্যবহার করেন? তাহলে সময় নষ্ট করছেন।

Google: 10টা লিংক দেয়, একটা একটা খুলে পড়েন, 30 মিনিট শেষ।
Perplexity: সরাসরি উত্তর + কোন Source থেকে নিলো তার লিংকসহ। ভুল তথ্যের ভয় কম।

Student, Content Creator, Freelancer — যাদের প্রতিদিন তথ্য খুঁজতে হয়, তাদের জন্য Game Changer।

ফ্রি, App আর Website দুটোই — perplexity.ai

💬 এখনো Google, নাকি AI-তে Shift করেছেন? 👇""" + F, None),

# ===== DAY 3 =====
("AI, Freelancer দের চাকরি\nখাচ্ছে না।\n\nAI *জানা* Freelancer রা\nAI *না জানা* দের\nReplace করছে 👇", "crimson", 70,
 """💼 পরিষ্কার করে বলি — AI Freelancer দের Replace করছে না। AI-জানা Freelancer রা AI-না-জানাদের Replace করছে।

ভাবুন:
→ যে Designer AI দিয়ে 3 গুণ দ্রুত কাজ দেয়, Client কাকে নেবে?
→ যে Writer AI দিয়ে 1 দিনে Draft দেয়, নাকি যে 4 দিন নেয়?

নতুন Skill পুরনো Skill কে বাতিল করে না — দাম বাড়িয়ে দেয়।
আপনার এখনকার Skill + AI = আপনার নতুন Rate।

💬 আপনি কোন Skill এ Freelancing করেন/করতে চান? কমেন্টে লিখুন 👇""" + F, None),

("Mic ছাড়াই\n*Professional Voiceover* 🎙️\n\nআপনি শুধু *Text* লিখবেন —\nবাকিটা AI করবে", "black", 72,
 """🎙️ ভিডিও বানান কিন্তু নিজের কণ্ঠ রেকর্ড করতে চান না? ElevenLabs আপনার জন্য।

শুধু লেখা টাইপ করুন — একদম মানুষের মতো Voiceover বানিয়ে দেবে। Tone, আবেগ, গতি — সব Control করা যায়।

কাজে লাগান: Faceless YouTube/Reels, Product Promo, Audiobook, Podcast।
ইংরেজি দুর্বল? নিখুঁত উচ্চারণে Voiceover পাবেন।

Free Plan এই মাসে অনেকটা কাজ হয়ে যায়।

💬 নিজের কণ্ঠে বানান, নাকি AI Voice ব্যবহার করবেন? 👇""" + F, None),

# ===== DAY 4 =====
("Client কে কী লিখবেন\nবুঝতে পারেন না? 💬\n\nএই *Prompt* টা আপনার\nজন্য Proposal লিখে দেবে\n\n(কমেন্টে 👇)", "green", 66,
 """💼 Freelancer দের সবচেয়ে বড় সমস্যা — Client কে প্রথম মেসেজে কী লিখব?

প্রথম Proposal-টাই ঠিক করে কাজ পাবেন কি না। Copy-paste জেনেরিক মেসেজে কেউ Reply করে না।

এই Prompt টা আপনার Skill আর Client-এর Job Post অনুযায়ী Custom Proposal লিখে দেবে।

🎁 Prompt প্রথম কমেন্টে।

💬 কোন Marketplace-এ কাজ করেন? Fiverr / Upwork / সরাসরি? 👇""" + F,
 """🎁 Client Proposal Prompt (কপি করুন):

"You are an expert freelance proposal writer. My skills: [আপনার স্কিল]. My experience: [কত বছর]. Client's job post: [পেস্ট করুন]. Write a short personalized proposal (under 150 words) that: 1) shows I understood their specific problem, 2) mentions one relevant example, 3) ends with a question. No generic lines like 'I am hardworking'."

কাজ পেলে জানাবেন 😄👇"""),

("Camera নেই।\nEditing জানেন না।\n\nতবুও শুধু *Text* লিখে\nএখন *Professional Video*\nবানানো যায় 🎬", "charcoal", 68,
 """🎬 ক্যামেরা নেই? Editing জানেন না? সমস্যা নেই — এখন Text থেকেই ভিডিও।

2026-এর নতুন AI Video Tool (Veo, Kling) শুধু একটা লেখা থেকে বাস্তবসম্মত ভিডিও Clip বানিয়ে দেয় — মানুষ, দৃশ্য, Movement সব।

→ Faceless ভিডিও পেজ চালানো এখন সহজ
→ Reels/Shorts-এর জন্য B-roll সেকেন্ডে
→ বিজ্ঞাপন, Intro — বাজেট ছাড়াই

Faceless Content = 2026-এর অন্যতম বড় ইনকামের সুযোগ।

💬 Faceless ভিডিও নিয়ে ফুল গাইড চান? "চাই" লিখুন 👇""" + F, None),

# ===== DAY 5 =====
("এই *5টা Free AI Tool*\nআপনার সপ্তাহে\n20+ ঘণ্টা বাঁচাবে ⏳\n\nলিস্ট *ক্যাপশনে* 👇", "crimson", 72,
 """⏳ কোনো টাকা লাগবে না। আমি প্রতিদিন এই 5টা ব্যবহার করি:

1️⃣ ChatGPT — কনটেন্ট, ক্যাপশন, ইমেইল ড্রাফট
2️⃣ Perplexity — Source সহ Instant Research
3️⃣ Canva — Designer ছাড়াই Design
4️⃣ CapCut — মোবাইলেই Pro Video Editing
5️⃣ Claude — লম্বা লেখা, Document Analysis

এই 5টা শিখলে একা একজন মানুষ একটা ছোট Team-এর কাজ করতে পারে।

💬 এই 5টার মধ্যে কোনটা এখনো ব্যবহার করেননি? 👇""" + F, None),

("Coding না জেনেও\nএখন *App বানানো* যায় 💻\n\nCursor, Claude Code —\n*পুরো Feature* লিখে দেয়", "black", 68,
 """💻 2026-এ Coding সম্পূর্ণ বদলে গেছে।

আগে AI শুধু Autocomplete করত। এখন Cursor, Claude Code পুরো Feature নিজে লিখে দেয় — শুরু থেকে শেষ।

Cursor এখন 2 Billion ডলারের Business — শুধু AI দিয়ে কোড লেখার Tool।

এর মানে: নন-টেকনিক্যাল মানুষও এখন ছোটখাটো App, Automation বানাতে পারে — শুধু ভাষায় বলে দিলেই।

💬 App/Automation বানাতে চান কিন্তু Coding জানেন না? কমেন্টে "হ্যাঁ" লিখুন — এটা নিয়ে বিস্তারিত পোস্ট দেবো 👇""" + F, None),

# ===== DAY 6 =====
("Email এর Reply লিখতে\n15 মিনিট চলে যায়? 📧\n\nএই Prompt টা\n*30 সেকেন্ডে* লিখে দেবে\n\n(কমেন্টে 👇)", "navy", 64,
 """📧 Client বা অফিসের Email-এর Reply লিখতে সময় নষ্ট?

একটা Prompt ব্যবহার করি — যেকোনো Email-এর পারফেক্ট Reply 30 সেকেন্ডে। Tone, ভাষা, Format — সব ঠিক।

🎁 Prompt প্রথম কমেন্টে। কপি করে ব্যবহার করুন।

💬 কাজে লাগলে একটা 👍 দিয়ে জানাবেন — এরকম আরো Prompt শেয়ার করবো 👇""" + F,
 """🎁 Email Reply Prompt (কপি করুন):

"You are my professional email assistant. I'll paste an email I received. Write a reply that is: 1) polite and professional, 2) clear and to the point, 3) in the same language as the original. If any info is missing from my side, mark it [FILL IN]. Here is the email: [পেস্ট করুন]"

যেকোনো Email-এর রেডি Reply! কেমন লাগলো জানাবেন 👇"""),

("Designer ছাড়াই\n*Professional Design* 🎨\n\nCanva-র এই *5টা Free*\nAI Feature 90% মানুষ\nজানেই না", "crimson", 66,
 """🎨 Canva শুধু Template না — ভেতরে 5টা ফ্রি AI Feature লুকিয়ে আছে:

1️⃣ Magic Write — ক্যাপশন, Idea লিখে দেয়
2️⃣ Background Remover — এক ক্লিকে ব্যাকগ্রাউন্ড গায়েব
3️⃣ Magic Eraser — অপ্রয়োজনীয় জিনিস মুছে দিন
4️⃣ Magic Resize — এক ডিজাইন থেকে সব সাইজ
5️⃣ Text to Image — লিখে দিন, ছবি বানিয়ে দেবে

Free Account এই বেশিরভাগ কাজ চলে।

💬 Canva ব্যবহার করেন? কোন Feature টা প্রিয়? 👇""" + F, None),

# ===== DAY 7 =====
("AI *শিখুন* —\n\nনাহলে AI *জানা* মানুষ\nআপনাকে *Replace* করবে ⚡\n\n(কঠিন, কিন্তু সত্যি)", "black", 70,
 """📚 একটা কঠিন সত্য: AI যুগে সবচেয়ে বড় ঝুঁকি চাকরি হারানো না — শেখা বন্ধ করে দেওয়া।

দুনিয়া এখন দুই ভাগ:
→ যারা বলে "এই বয়সে আর এসব শিখব না" — ধীরে ধীরে অপ্রাসঙ্গিক হচ্ছে
→ যারা বলে "দেখি এটা কীভাবে কাজ করে" — অপরিহার্য হচ্ছে

পার্থক্যটা বয়সের না, Mindset-এর।

দিনে 20 মিনিট। একটা Tool, একটা Prompt। 95% মানুষ এটুকুও করে না।

💬 আজ/এই সপ্তাহে নতুন কী শিখলেন? ছোট হোক, কমেন্টে শেয়ার করুন 👇""" + F, None),

("Reels বানান? 🎬\n\nCapCut-এর এই *3টা Feature*\nআপনার ভিডিওকে\n*Pro-level* বানাবে", "charcoal", 68,
 """🎬 Reels/Shorts বানান? CapCut-এর এই 3টা Feature জানলে ভিডিও অন্য Level-এ যাবে:

1️⃣ Auto Captions — এক ক্লিকে কথা Text হয়ে যায়। বাংলাও সাপোর্ট করে! Silent scroller-রাও বুঝবে।
2️⃣ Keyframe Animation — ছবি/টেক্সট জুম-প্যান করে Cinematic ইফেক্ট = বেশি Watch time।
3️⃣ Trending Templates — ভাইরাল Format-এ নিজের ক্লিপ বসান, 30 সেকেন্ডে রেডি।

সব Free Version-এই আছে।

💬 ভিডিও Editing-এ কোন সমস্যায় বেশি পড়েন? 👇""" + F, None),

# ===== DAY 8 =====
("Post এর প্রথম লাইনটাই\nঠিক করে — কেউ পড়বে\nনাকি *Scroll* করবে 📱\n\nHook লেখার Prompt\n(কমেন্টে 👇)", "crimson", 62,
 """✍️ ভাইরাল পোস্ট আর মরা পোস্টের পার্থক্য 80% থাকে প্রথম লাইনে — Hook-এ।

একটা Prompt ব্যবহার করি যেটা যেকোনো Topic-এ 10টা Hook লিখে দেয় — Psychology মেনে: কৌতূহল, ভয়, উপকার, গল্প।

🎁 Prompt প্রথম কমেন্টে। কপি করে নিজের Topic বসান।

💬 আপনি কনটেন্ট বানান? কোন Platform-এ? 👇""" + F,
 """🎁 Hook Generator Prompt (কপি করুন):

"You are a viral content expert for Bengali Facebook audiences. My post topic: [টপিক]. Write 10 different hooks (first lines) in Bengali. Mix these styles: curiosity gap, bold claim, common mistake, personal story, surprising fact, direct question. Each under 15 words. Rank strongest to weakest and explain why #1 works."

সবচেয়ে ভালো Hook টা কমেন্টে শেয়ার করেন 😄👇"""),

("ইংরেজি *ভুল* লিখছেন?\n\nএই Free Tool টা\nযেখানেই লিখবেন —\n*ঠিক করে দেবে* ✍️", "navy", 70,
 """✍️ ইংরেজি লেখার ভুলে Client-এর কাছে খারাপ ইম্প্রেশন? Grammarly আপনার জন্য।

Gmail, Facebook, যেকোনো Website — যেখানেই ইংরেজি লিখবেন, রিয়েল-টাইমে ভুল ধরবে, ঠিক করে দেবে।

Freelancer দের জন্য এটা প্রায় বাধ্যতামূলক — একটা প্রফেশনাল ইমেজ তৈরি করে।

Browser Extension টা Free, একবার Install করলেই সব জায়গায় কাজ করে।

💬 ইংরেজি নিয়ে আপনার সবচেয়ে বড় ভয় কী — বলা, লেখা, নাকি বোঝা? 👇""" + F, None),

# ===== DAY 9 =====
("নতুন AI আগের চেয়ে\n*স্মার্ট* কেন? 🧠\n\nকারণ এখন এরা\nউত্তর দেওয়ার আগে\n*চিন্তা করে*", "black", 68,
 """🧠 লক্ষ্য করেছেন — নতুন AI (GPT-5, Claude Opus, Gemini) আগের চেয়ে অনেক ভালো উত্তর দেয়?

কারণ 2026-এ Reasoning এখন Default। আগে AI সাথে সাথে উত্তর দিত। এখন এরা প্রশ্নটা নিয়ে আগে "চিন্তা" করে, ধাপে ধাপে ভাবে, তারপর উত্তর দেয় — অনেকটা মানুষের মতো।

এর মানে জটিল কাজে (অঙ্ক, Coding, Analysis, Planning) এদের ভুল অনেক কমে গেছে।

💬 আপনি কোন AI বেশি ব্যবহার করেন? ChatGPT / Gemini / Claude? 👇""" + F, None),

("পুরো সপ্তাহ *Plan* করে দেবে\nAI — 2 মিনিটে 📅\n\nআপনার Goal অনুযায়ী\n(Prompt কমেন্টে 👇)", "green", 64,
 """📅 রবিবার রাতে 10 মিনিট Plan = পুরো সপ্তাহ ক্লিয়ার মাথায় কাজ।

কিন্তু Plan করাটাই ঝামেলা লাগে, তাই না?

এই Prompt টা আপনার Goal, সময় আর Energy অনুযায়ী পুরো সপ্তাহের Realistic Plan বানিয়ে দেয় — বিশ্রামের সময়সহ। Robot-এর মতো না, মানুষের মতো।

🎁 Prompt প্রথম কমেন্টে।

💬 আপনি Plan করে চলেন, নাকি যা আসে তাই সামলান? 😄👇""" + F,
 """🎁 Weekly Planner Prompt (কপি করুন):

"You are my productivity coach. My main goals this week: [3টা লক্ষ্য]. My fixed commitments: [জব/ক্লাস/পরিবার]. My peak energy time: [সকাল/দুপুর/রাত]. Create a realistic weekly plan in Bengali: 1) assign goals to specific days and time blocks, 2) keep hard tasks in peak energy hours, 3) add rest/buffer time, 4) one small daily habit. Format as a day-by-day table."

প্ল্যানটা বানিয়ে Screenshot সেভ করে রাখুন 📌👇"""),

# ===== DAY 10 =====
("AI দিয়ে *ইনকাম* —\n\n2026 সালের সবচেয়ে বড়\n*সুযোগ* 🚀\n\n(শুরুটা আজই হোক)", "crimson", 70,
 """🚀 AI দিয়ে ইনকামের রাস্তা এখন অনেক — কিন্তু শুরু করতে হবে একটা দিয়ে:

→ Faceless Content (AI Voice + AI Video)
→ AI দিয়ে দ্রুত Freelancing (Writing, Design, VA)
→ ছোট Business-এর জন্য AI Automation সেটআপ করে দেওয়া
→ Prompt বিক্রি / AI Consulting

সবগুলোর ভিত্তি একটাই — AI-কে ভালোভাবে ব্যবহার করতে শেখা।

দিনে 20 মিনিট শিখুন। 3 মাস পরে নিজের পার্থক্য নিজেই দেখবেন।

💬 কোন রাস্তাটা আপনার জন্য সবচেয়ে বেশি Interesting? 👇""" + F, None),

("এই পেজে যা যা\n*পাবেন* 🎁\n\nFree AI Tool • Prompt\nWorkflow • Income Idea\n— প্রতিদিন", "black", 68,
 """🎁 নতুন যারা এসেছেন — পরিচিত হয়ে যাই।

আমি মামুন। এই পেজে শেয়ার করি:
→ Free AI Tool-এর খোঁজ — যেগুলো আসলেই কাজের
→ Copy-paste রেডি Prompt — প্রথম কমেন্টে পাবেন
→ Skill আর ইনকামের Practical Idea — Hype ছাড়া
→ Productivity System — যা নিজে ব্যবহার করি

লক্ষ্য একটাই: AI-কে ভয় না পেয়ে কাজে লাগানো শিখি, একসাথে।

💬 আপনি কী নিয়ে সবচেয়ে বেশি জানতে চান? কমেন্টে বলুন — কনটেন্ট প্ল্যানে ঢুকিয়ে নেবো 👇

আর ভালো লাগলে পেজটা Follow করে রাখুন 👊""", None),
]

assert len(POSTS) == 20
