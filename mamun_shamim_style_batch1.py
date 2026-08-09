# -*- coding: utf-8 -*-
"""Mamun Hossain — refined batch modeled directly on NasirUShamim's (407K)
top-performing format, per full page analysis 2026-08-03 (14 of his posts
reviewed + live page check). Key changes from the previous block-post batch:

  - Color discipline: RED reserved for fear/curiosity + personal-development
    hooks (his two highest-performing categories), BLACK is the default for
    everything else. Charcoal/navy/green dropped — he doesn't use them.
  - First-comment payload on EVERY listicle post (not just prompt posts) —
    the image/caption is only the hook; the actual numbered value goes in
    the page's own first comment, mini-article style (bold label + line).
  - A few no-image text-only hot-take posts mixed in, matching his live
    "Deepseek Code is coming" post (862/84/14, zero image).
  - No zelobiz.com push this batch (user's call 2026-08-03) — pure
    value/growth content, monetization funnel to be decided later.
  - No topic restrictions — user explicitly said not to avoid anything,
    so real tools/companies/AI-news references are fine here (unlike the
    evergreen-only caution applied elsewhere in this project).

Runs 2026-08-08 -> 2026-08-21 (14 days), 2 slots/day (07:00 + 15:00 UTC,
continuing the existing cadence), starting right after the current queue's
Aug 7 tail."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from aug_common import load, save, mkdir, render
from image_block import block_post

IMG = mkdir("images/mamun_shamim1")

# kind: "hook" (image + first_comment payload) | "hot" (text-only, no image)
# hook: (theme, hook_text, [payload lines "**label** — detail"], caption_extra)
# hot:  (text,)
POSTS = [
 ("hook", "black",
  "ChatGPT-এ এই ৭টা সেটিংস বেশিরভাগ মানুষ কখনো ওপেনই করে না!\nঅথচ এগুলো ব্যবহার করলে আপনার প্রতিদিনের কাজ *অর্ধেক সময়ে* শেষ হয়ে যাবে 👇",
  ["**Custom Instructions** — প্রতিবার নিজের প্রফেশন/স্টাইল না বলে একবার সেট করে রাখুন, ChatGPT সব উত্তর সেভাবেই দিবে।",
   "**Memory** — আগের কথোপকথন মনে রাখে, বারবার কনটেক্সট রিপিট করা লাগবে না।",
   "**Projects/Folders** — একই টপিকের চ্যাটগুলো একসাথে রাখুন, ছড়িয়ে-ছিটিয়ে থাকবে না।",
   "**Voice Mode** — টাইপ না করে কথা বলেই ব্রেইনস্টর্ম করুন, অনেক দ্রুত।",
   "**Advanced Data Analysis** — এক্সেল/CSV ফাইল আপলোড করে সরাসরি অ্যানালাইসিস করান।",
   "**Scheduled Tasks** — রোজ একই সময়ে রিপোর্ট/সামারি অটো পাঠাতে সেট করে রাখুন।",
   "**Temporary Chat** — সেনসিটিভ কথোপকথন হিস্টোরিতে সেভ না করে আলাদা রাখুন।"],
  ""),

 ("hook", "crimson",
  "আপনার ফোনের প্রতিটা AI অ্যাপ আসলে আপনার সম্পর্কে যা যা *জানে*,\nসেটা দেখলে আপনি অবাক হবেন! ৫টা জায়গা দেখুন কীভাবে চেক করবেন 👇",
  ["**ChatGPT Data Controls** — Settings → Data Controls থেকে দেখুন কী সেভ হচ্ছে, চাইলে অফ করুন।",
   "**Google Gemini Activity** — myactivity.google.com এ পুরো হিস্টোরি দেখা যায়।",
   "**ফোনের AI Assistant Permissions** — মাইক্রোফোন/লোকেশন এক্সেস কোন অ্যাপে অন আছে চেক করুন।",
   "**ব্রাউজার এক্সটেনশন পারমিশন** — অনেক 'ফ্রি AI টুল' এক্সটেনশন আপনার ব্রাউজিং ডেটা কালেক্ট করে।",
   "**কাস্টম GPT/Agent Memory** — থার্ড-পার্টি GPT ব্যবহার করলে তাদেরও আলাদা মেমোরি থাকতে পারে, চেক করুন।"],
  ""),

 ("hook", "black",
  "মাত্র লঞ্চ হওয়া অথচ ইতিমধ্যে ভাইরাল *৬টি AI টুল*,\nযেগুলো আপনি এখনো ট্রাই করেননি 👇",
  ["**NotebookLM** — নিজের ডকুমেন্ট আপলোড করে সেটা থেকেই প্রশ্ন-উত্তর, এমনকি পডকাস্টও বানানো যায়।",
   "**Perplexity Comet** — রিসার্চের জন্য সোর্স-সহ উত্তর দেয়, Google সার্চের চেয়ে দ্রুত।",
   "**Cursor** — কোড লেখার সময় AI সরাসরি এডিটরের ভেতরেই সাজেশন দেয়।",
   "**ElevenLabs** — যেকোনো টেক্সটকে রিয়েলিস্টিক ভয়েসে কনভার্ট করে, ভিডিওর ভয়েসওভারে দারুণ।",
   "**ChatGPT Agent Mode** — শুধু উত্তর না, নিজে থেকে ব্রাউজ করে টাস্ক শেষ করে দেয়।",
   "**Google Veo** — টেক্সট দিয়ে সিনেমাটিক ভিডিও ক্লিপ বানানো যায়।"],
  ""),

 ("hot",
  "Google এর Gemini 3 আসার পর ChatGPT এর মার্কেট শেয়ার নিয়ে যা হচ্ছে, সেটা কেউ ২ বছর আগে কল্পনাও করেনি।\n\nCompetition এখন সত্যিকারের ইউজারদের লাভ- প্রতি মাসেই নতুন ফিচার, প্রতি মাসেই দাম কমছে।"),

 ("hook", "black",
  "মাসের পর মাস ধরে ফ্রিল্যান্স ক্লায়েন্ট খোঁজার দিন শেষ।\nএখন AI দিয়ে মাত্র *৩টা ধাপে* প্রথম ক্লায়েন্ট পাওয়া সম্ভব 👇",
  ["**ধাপ ১: AI-Assisted Proposal** — Upwork/Fiverr এর জব পোস্ট পেস্ট করে ChatGPT দিয়ে কাস্টম প্রপোজাল লিখুন, জেনেরিক টেমপ্লেট না।",
   "**ধাপ ২: LinkedIn Outreach** — টার্গেট ক্লায়েন্টের প্রোফাইল দিয়ে পার্সোনালাইজড মেসেজ AI দিয়ে ড্রাফট করান।",
   "**ধাপ ৩: Portfolio Optimization** — AI দিয়ে নিজের পোর্টফোলিওর কেস-স্টাডি লেখাগুলো ক্লায়েন্ট-ফোকাসড করে সাজান।"],
  ""),

 ("hook", "crimson",
  "আপনি যদি মনে করেন আপনার আইডিয়া ভালো কিন্তু কেউ পাত্তা দেয় না-\nসমস্যাটা আইডিয়াতে না, আপনার *Presentation*-এ! ৪টা পয়েন্ট দেখুন 👇",
  ["**Clarity** — এক লাইনে বলতে না পারলে, মানুষ ৩০ সেকেন্ডেই আগ্রহ হারায়।",
   "**Proof** — দাবি না, রেজাল্ট দেখান। সংখ্যা, স্ক্রিনশট, আগে-পরের কম্পারিজন।",
   "**নির্দিষ্ট সংখ্যা** — 'ভালো রেজাল্ট' না বলে 'কাজ ৩ ঘণ্টা থেকে ৩০ মিনিটে নেমে এসেছে' বলুন।",
   "**Call to Action** — আইডিয়া শোনানোর পর কী করতে হবে সেটা স্পষ্ট করে বলুন, অনুমানের ওপর ছেড়ে দিবেন না।"],
  ""),

 ("hook", "black",
  "Canva-তে ডিজাইন বানানোর সময় এই *৫টা AI প্রম্পট* সেভ করে রাখুন,\nপ্রফেশনাল ডিজাইনারের মতো রেজাল্ট পাবেন 👇",
  ["**\"Minimal poster design, [topic], bold typography, high contrast\"** — Magic Design এর জন্য।",
   "**\"Remove background, keep shadow natural\"** — প্রোডাক্ট ছবি ক্লিন করতে।",
   "**\"Generate 3 color palette variations from this image\"** — ব্র্যান্ড কালার বের করতে।",
   "**\"Resize this design for Instagram Story and Facebook post, keep text readable\"** — মাল্টি-ফরম্যাট এক ক্লিকে।",
   "**\"Write 3 short headline variations for this design, punchy tone\"** — কপি আইডিয়ার জন্য।"],
  ""),

 ("hook", "black",
  "কনটেন্ট আইডিয়ার অভাব?\nএই *৮টা ওয়েবসাইট* রোজ চেক করুন, কখনো আইডিয়া ফুরাবে না 👇",
  ["**Exploding Topics** — নতুন ট্রেন্ড মেইনস্ট্রিম হওয়ার আগেই ধরতে পারবেন।",
   "**Google Trends** — কোন টপিক এখন সার্চ হচ্ছে বেশি, রিয়েল-টাইমে দেখুন।",
   "**AnswerThePublic** — মানুষ একটা টপিক নিয়ে ঠিক কী প্রশ্ন করছে সেটা দেখায়।",
   "**Reddit (নিজের নিশ সাবরেডিট)** — আসল মানুষের আসল সমস্যা, কনটেন্ট আইডিয়ার সেরা সোর্স।",
   "**AlsoAsked** — একটা প্রশ্নের সাথে রিলেটেড আরও কী প্রশ্ন আসে, ম্যাপ আকারে দেখায়।",
   "**BuzzSumo** — কোন কনটেন্ট সবচেয়ে বেশি শেয়ার হচ্ছে, নিশ অনুযায়ী দেখা যায়।",
   "**Ubersuggest** — কিওয়ার্ড আইডিয়া + কম্পিটিটর অ্যানালাইসিস একসাথে।",
   "**Notion AI (নিজের Brainstorm পেজ)** — সপ্তাহের সব আইডিয়া এক জায়গায় জমিয়ে রাখুন, AI দিয়ে এক্সপ্যান্ড করান।"],
  ""),

 ("hook", "crimson",
  "আপনার প্রতিদিনের রুটিন যদি এই *৩টা কাজ* দিয়ে শুরু হয়,\nবুঝে নিন আপনি নিজের সময় নষ্ট করছেন! দেখুন কোনগুলো 👇",
  ["**ঘুম থেকে উঠেই ফোন চেক** — ব্রেইন এখনো রিল্যাক্সড অবস্থায়, প্রথম ৩০ মিনিট ফোন ছাড়া রাখুন।",
   "**প্ল্যান করার আগে সোশ্যাল মিডিয়া স্ক্রল** — দিনের প্রথম এনার্জি অন্যের কনটেন্টে খরচ হয়ে যায়।",
   "**জরুরি কাজের আগে অজরুরি মেসেজের রিপ্লাই** — সবচেয়ে ফ্রেশ সময়টা ছোট কাজে চলে যায়, বড় কাজ পরে ফেলে রাখা হয়।"],
  ""),

 ("hot",
  "Anthropic এর Claude এখন কোডিং-এ যেভাবে এগিয়ে যাচ্ছে, সামনের ৬ মাসে জুনিয়র ডেভেলপারদের জব মার্কেট পুরাই বদলে যাবে।\n\nযারা এখনো AI কে ignore করছেন, তারাই সবচেয়ে বেশি রিস্কে আছেন।"),

 ("hook", "black",
  "ফ্রি-তে প্রিমিয়াম ফিচার পাওয়ার *৫টা উপায়*\nযা বেশিরভাগ মানুষ জানেই না 👇",
  ["**Student Email Discount** — .edu ইমেইল থাকলে অনেক AI টুলেই ফ্রি প্রিমিয়াম অ্যাক্সেস পাওয়া যায়।",
   "**Free Trial Stacking (বৈধভাবে)** — নতুন ফিচার আসলে আলাদা ফ্রি-ট্রায়াল পিরিয়ড চালু হয়, নোটিফিকেশন অন রাখুন।",
   "**Open-Source Alternative** — পেইড টুলের প্রায় প্রতিটারই একটা শক্তিশালী ওপেন-সোর্স ভার্সন আছে।",
   "**ব্রাউজার এক্সটেনশন** — অনেক প্রিমিয়াম ফিচার আলাদা ফ্রি এক্সটেনশন হিসেবেই পাওয়া যায়।",
   "**কমিউনিটি/নন-প্রফিট অ্যাক্সেস প্রোগ্রাম** — অনেক AI কোম্পানি ছোট বিজনেস/নন-প্রফিটদের জন্য ফ্রি টিয়ার দেয়, সাইট চেক করুন।"],
  ""),

 ("hook", "black",
  "৬ ঘণ্টার এডিটিং কাজ এখন *৬ মিনিটে* শেষ!\nVideo editing-এ AI কীভাবে ব্যবহার করবেন, ৩টা টুল ও পদ্ধতি 👇",
  ["**CapCut AI** — অটো-সাবটাইটেল, অটো-বি-রোল সাজেশন, ব্যাকগ্রাউন্ড নয়েজ রিমুভাল একসাথে।",
   "**Descript** — টেক্সট এডিট করলেই ভিডিও এডিট হয়ে যায়, 'um/ah' অটো রিমুভ করে।",
   "**অটো-ক্যাপশন + অটো-কাট ওয়ার্কফ্লো** — লম্বা র‍কর্ডিং থেকে সবচেয়ে ভালো অংশগুলো AI দিয়ে খুঁজে বের করান, তারপর ম্যানুয়ালি ফাইনাল টাচ দিন।"],
  ""),

 ("hook", "crimson",
  "আপনি প্রতিদিন কাজ করছেন, কিন্তু ইনকাম বাড়ছে না-\nকারণটা হয়তো আপনার Effort না, আপনার *Pricing*! ৩টা পয়েন্ট দেখুন 👇",
  ["**সময় বিক্রি করবেন না, রেজাল্ট বিক্রি করুন** — ঘণ্টা হিসেবে চার্জ করলে আপনি যত দ্রুত কাজ করবেন, তত কম আয় করবেন।",
   "**সবচেয়ে সস্তা হওয়া কোনো স্ট্র্যাটেজি না** — কম দামে যে ক্লায়েন্ট আসে, সে-ই সবচেয়ে বেশি সমস্যা করে।",
   "**বছরে অন্তত ২ বার দাম রিভিউ করুন** — স্কিল বাড়ছে অথচ দাম একই থাকলে, আপনি নিজের গ্রোথকে নিজেই আটকে রাখছেন।"],
  ""),

 ("hook", "black",
  "AI দিয়ে প্যাসিভ ইনকামের *৬টা রিয়েলিস্টিক* আইডিয়া,\nযেগুলো আজকেই শুরু করা যায় 👇",
  ["**Print-on-Demand + AI ডিজাইন** — Midjourney/Canva দিয়ে ডিজাইন বানিয়ে Printify তে আপলোড করুন।",
   "**AI-Narrated কনটেন্ট** — নিজের নিশে ফ্যাক্ট/স্টোরি কনটেন্ট বানিয়ে YouTube/FB তে পোস্ট করুন।",
   "**প্রম্পট বিক্রি** — নিজের বানানো ভালো প্রম্পট PromptBase এর মতো মার্কেটপ্লেসে বিক্রি করুন।",
   "**ছোট বিজনেসের জন্য AI Automation সেটআপ** — লোকাল বিজনেসের জন্য চ্যাটবট/অটো-রিপ্লাই সেটআপ করে দিন, ওয়ানটাইম ফি নিন।",
   "**AI নিউজলেটার কিউরেশন** — একটা নিশে রোজকার আপডেট AI দিয়ে সামারি করে নিউজলেটার পাঠান।",
   "**ডিজিটাল টেমপ্লেট** — Notion/Canva টেমপ্লেট বানিয়ে Gumroad এ বিক্রি করুন।"],
  ""),

 ("hook", "black",
  "প্রতিদিনের ইমেইল লেখার সময় বাঁচাতে\nএই *৫টা প্রম্পট* ChatGPT-তে সেভ করে রাখুন 👇",
  ["**\"Turn these bullet points into a professional email, [tone: friendly/formal]\"**",
   "**\"Shorten this email to 3 sentences without losing the main point\"**",
   "**\"Write a polite follow-up for an email I sent 3 days ago with no reply\"**",
   "**\"Rewrite this email to sound more confident, remove unnecessary apologies\"**",
   "**\"Draft a decline email for this request, keep the relationship positive\"**"],
  ""),

 ("hot",
  "OpenAI, Google, Anthropic- সবাই এখন Agent বানানোর রেসে নেমেছে।\n\n২০২৬ সালটা হবে AI Agent এর বছর- যারা এখন থেকেই শিখে রাখবে, তারাই সামনে এগিয়ে থাকবে।"),

 ("hook", "black",
  "প্রেজেন্টেশন বানানোর জন্য সেরা *৫টি AI টুল*,\nএকদম প্রফেশনাল লুক পাবেন 👇",
  ["**Gamma** — শুধু টপিক লিখলেই পুরো প্রেজেন্টেশন ডিজাইন-সহ বানিয়ে দেয়।",
   "**Canva Magic Design** — এক্সিস্টিং কনটেন্ট থেকে অটো-ডিজাইন সাজেস্ট করে।",
   "**Beautiful.ai** — স্লাইড অ্যাড করার সাথে সাথেই লেআউট অটো-অ্যাডজাস্ট হয়।",
   "**Tome** — স্টোরিটেলিং-ফোকাসড প্রেজেন্টেশনের জন্য দারুণ।",
   "**ChatGPT + Google Slides** — আউটলাইন AI দিয়ে বানিয়ে সরাসরি স্লাইডে পেস্ট করুন।"],
  ""),

 ("hook", "crimson",
  "আপনার CV প্রতিটা কোম্পানির ATS সিস্টেম আসলে যেভাবে *স্ক্যান* করে,\nসেটা জানলে আপনি নিজের CV আজই বদলে ফেলবেন! ৩টা পয়েন্ট 👇",
  ["**কীওয়ার্ড ম্যাচিং** — জব পোস্টের ভাষায় ব্যবহৃত স্কিল-নাম হুবহু আপনার CV তে থাকা লাগবে, প্রতিশব্দ কাজ করে না।",
   "**সিম্পল ফরম্যাট** — টেবিল/গ্রাফিক্স-ভারী CV অনেক ATS ঠিকভাবে পড়তেই পারে না।",
   "**স্ট্যান্ডার্ড সেকশন হেডিং** — 'Experience', 'Education' এর বদলে ক্রিয়েটিভ নাম দিলে সিস্টেম কনফিউজড হয়ে যায়।"],
  ""),

 ("hook", "black",
  "মার্কেট রিসার্চের জন্য সপ্তাহখানেক সময় লাগানোর দিন শেষ।\nAI দিয়ে *২ ঘণ্টায়* সম্পূর্ণ কম্পিটিটর অ্যানালাইসিস করার পদ্ধতি 👇",
  ["**ধাপ ১: Perplexity দিয়ে রিসার্চ** — কম্পিটিটরদের নাম দিয়ে সোর্স-সহ তথ্য জোগাড় করুন।",
   "**ধাপ ২: ChatGPT দিয়ে SWOT** — জোগাড় করা তথ্য পেস্ট করে প্রতিটা কম্পিটিটরের Strength/Weakness বের করান।",
   "**ধাপ ৩: Notion এ কম্পাইল** — সব একটা টেবিলে সাজিয়ে টিমের সাথে শেয়ার করুন।"],
  ""),

 ("hook", "black",
  "স্টুডেন্ট থেকে শুরু করে ফ্রিল্যান্সার- সবার কাজে লাগবে\nএমন *৭টি ফ্রি AI টুল* 👇",
  ["**ChatGPT (Free tier)** — জেনারেল রাইটিং, ব্রেইনস্টর্মিং, রিসার্চের জন্য।",
   "**Canva (Free)** — ডিজাইন, প্রেজেন্টেশন, সোশ্যাল মিডিয়া কনটেন্ট।",
   "**Google Gemini** — Google Docs/Sheets এর সাথে সরাসরি ইন্টিগ্রেটেড।",
   "**Grammarly Free** — ইংরেজি লেখা প্রুফরিড ও ইম্প্রুভ করতে।",
   "**CapCut** — ভিডিও এডিটিং, মোবাইল থেকেই প্রফেশনাল রেজাল্ট।",
   "**NotebookLM** — পড়াশোনা/রিসার্চ পেপার সামারি করতে।",
   "**Perplexity** — সোর্স-সহ রিসার্চের জন্য Google এর বিকল্প।"],
  ""),

 ("hook", "crimson",
  "আপনি যদি রোজ Busy থাকেন কিন্তু কাজ শেষ হয় না-\nসমস্যাটা সময় না, আপনার *Priority* ঠিক নাই! ৩টা পয়েন্ট দেখুন 👇",
  ["**সব কাজ 'জরুরি' না** — দিনে ৩টার বেশি 'must-do' রাখলে, আসলে কোনোটাই ঠিকমতো শেষ হয় না।",
   "**সকালের সবচেয়ে ফ্রেশ সময়টা সবচেয়ে কঠিন কাজে দিন** — ছোট কাজ যেকোনো সময় করা যায়, বড় কাজ না।",
   "**'না' বলতে শিখুন** — প্রতিটা অনুরোধে হ্যাঁ বললে, নিজের আসল প্রায়োরিটির জন্য সময়ই থাকে না।"],
  ""),

 ("hook", "black",
  "ফেসবুক পেজ বড় করার জন্য এই *৬টা ফ্রি টুল* ব্যবহার করুন,\nরেজাল্ট নিজেই দেখবেন 👇",
  ["**Canva** — কনসিস্টেন্ট ব্র্যান্ড লুকের পোস্ট বানাতে।",
   "**Meta Business Suite Insights** — কোন পোস্ট কাজ করছে, কোনটা করছে না, ডেটা দিয়ে বুঝুন।",
   "**ChatGPT** — ক্যাপশন ও হুক লাইন লিখতে সময় বাঁচান।",
   "**CapCut** — রিলস/ভিডিও কনটেন্টের জন্য।",
   "**Google Trends** — কোন টপিক এখন ট্রেন্ডিং সেটা দেখে কনটেন্ট প্ল্যান করুন।",
   "**Meta Business Suite Scheduler** — একসাথে পুরো সপ্তাহের পোস্ট প্ল্যান করে রাখুন।"],
  ""),

 ("hook", "black",
  "বিজনেস আইডিয়া ভ্যালিডেট করার জন্য\nএই *৫টা প্রম্পট* ব্যবহার করুন AI-তে 👇",
  ["**\"Who exactly would pay for [idea], and why would they choose it over what they use now?\"**",
   "**\"What are 3 reasons this idea might fail in the [country/market]?\"**",
   "**\"Write 5 questions I should ask 10 potential customers before building this\"**",
   "**\"What's the cheapest way to test demand for this idea in 1 week?\"**",
   "**\"List 3 existing competitors and what they're missing\"**"],
  ""),

 ("hot",
  "প্রতিদিন হাজারো মানুষ AI নিয়ে ভয় পাচ্ছে চাকরি হারানোর, কিন্তু যারা AI কে টুল হিসেবে ব্যবহার শিখছে তারাই আগামী ৫ বছরে সবচেয়ে বেশি সুবিধা পাবে।\n\nAdapt করাটাই আসল স্কিল।"),

 ("hook", "black",
  "SEO আর কনটেন্ট রাইটিং এর জন্য সেরা *৬টি AI টুল*,\nফ্রি ভার্সনেই কাজ চলবে 👇",
  ["**ChatGPT** — আউটলাইন, ড্রাফট, হেডলাইন ভ্যারিয়েশন।",
   "**Ubersuggest** — কিওয়ার্ড রিসার্চ, ফ্রি টিয়ারেই বেসিক ডেটা পাওয়া যায়।",
   "**Grammarly** — গ্রামার + রিডেবিলিটি চেক।",
   "**AnswerThePublic** — মানুষ ঠিক কোন প্রশ্নের উত্তর খুঁজছে সেটা টার্গেট করে লিখতে।",
   "**Google Search Console** — কোন কিওয়ার্ডে ইতিমধ্যে ট্রাফিক আসছে, সেটা অপ্টিমাইজ করতে।",
   "**Surfer SEO (ফ্রি ট্রায়াল)** — কম্পিটিটরদের কনটেন্ট অ্যানালাইসিস করে গ্যাপ বের করে।"],
  ""),

 ("hook", "crimson",
  "আপনার প্রতিদিনের স্ক্রিন টাইম যদি এই লেভেলে থাকে,\nবুঝে নিন এটা আপনার প্রোডাক্টিভিটি *নিরবে* নষ্ট করছে! ৩টা সাইন দেখুন 👇",
  ["**কাজের ফাঁকে ফাঁকে অকারণে ফোন আনলক করা** — কোনো নোটিফিকেশন ছাড়াই, শুধু অভ্যাসবশত। এটা ফোকাস ভাঙার সবচেয়ে বড় কারণ।",
   "**একটা ভিডিও দেখতে গিয়ে ১ ঘণ্টা স্ক্রল** — অ্যালগরিদম আপনার সময় নেওয়ার জন্যই বানানো, সচেতন না থাকলে টের পাবেন না।",
   "**ঘুমানোর ঠিক আগে স্ক্রিনে চোখ** — ঘুমের মান কমায়, পরদিনের প্রোডাক্টিভিটিতেই সরাসরি প্রভাব পড়ে।"],
  ""),

 ("hook", "black",
  "নিজের পোর্টফোলিও ওয়েবসাইট বানানোর জন্য\nডেভেলপার হায়ার করার দিন শেষ। AI দিয়ে *১ ঘণ্টায়* বানান 👇",
  ["**ধাপ ১: v0/Lovable তে টেক্সটে বর্ণনা দিন** — 'minimal portfolio, dark theme, projects grid' এর মতো প্রম্পট দিন।",
   "**ধাপ ২: নিজের কনটেন্ট বসান** — জেনারেট হওয়া টেমপ্লেটে নিজের প্রজেক্ট/ছবি/বায়ো বসিয়ে দিন।",
   "**ধাপ ৩: এক ক্লিকে ডিপ্লয়** — Vercel/Netlify তে ফ্রি-তে লাইভ করুন, ডোমেইন লাগলে পরে অ্যাড করুন।"],
  ""),

 ("hook", "crimson",
  "ক্যারিয়ারে এগিয়ে থাকতে চাইলে ২০২৬-এ\nএই *৫টা AI স্কিল* এখনই শেখা দরকার 👇",
  ["**Prompt Engineering** — শুধু প্রশ্ন করা না, সঠিকভাবে প্রশ্ন সাজাতে জানা।",
   "**AI Tool Stacking** — একাধিক টুল একসাথে চেইন করে ওয়ার্কফ্লো বানানো।",
   "**Data Literacy** — AI যে ডেটা দিচ্ছে সেটা যাচাই করে বোঝার ক্ষমতা।",
   "**AI Agent Management** — নিজের হয়ে কাজ করা এজেন্ট সেটআপ ও মনিটর করা।",
   "**Human Judgment** — কোন কাজ AI কে দেওয়া উচিত, কোনটা না- এই সিদ্ধান্ত নেওয়ার ক্ষমতা।"],
  ""),
]

assert len(POSTS) == 28

CTA = "\n\n👉 এমন আরও AI টিপস পেতে ফলো করুন Mamun Hossain"

SLOT_HOURS = [7, 15]
START_DATE = "2026-08-08"


def _dates(n):
    import datetime as dt
    d0 = dt.date.fromisoformat(START_DATE)
    return [(d0 + dt.timedelta(days=i)).isoformat() for i in range(n)]


def build():
    q = load()
    items = q["items"]
    have = {i.get("id") for i in items}
    dates = _dates(14)
    n = 0
    for i, post in enumerate(POSTS):
        day_idx, slot_idx = divmod(i, 2)
        iid = f"mamun-shamim1-{day_idx:02d}-{slot_idx}"
        if iid in have:
            continue
        when = f"{dates[day_idx]}T{SLOT_HOURS[slot_idx]:02d}:00:00+00:00"

        if post[0] == "hot":
            it = {"id": iid, "account": "mamun-hossain", "network": "facebook",
                  "type": "text", "message": post[1], "when": when, "status": "pending"}
        else:
            _, theme, hook, payload, extra = post
            img = f"{IMG}/{i:02d}.png"
            render(block_post, hook, out_path=img, theme=theme)
            fc = "\n".join(payload)
            it = {"id": iid, "account": "mamun-hossain", "network": "facebook",
                  "type": "photo", "message": hook.replace("*", "") + CTA + extra,
                  "image_url": img, "when": when, "status": "pending",
                  "first_comment": fc}
        items.append(it)
        n += 1
        print(f"  {iid} -> {when}  ({post[0]})")
    save(q)
    print(f"queued {n} items, total {len(items)}")


if __name__ == "__main__":
    build()
