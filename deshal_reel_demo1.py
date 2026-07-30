# -*- coding: utf-8 -*-
"""Radio Deshal — research-driven format demo: short native Bengali-voiced
reel instead of a static meme card. See rationale in the chat response this
accompanies. Original joke, office-life category (already in the standing
content mix), same short/punchy writing style as the approved dialogue jokes
— just delivered as a 15-20s voiced video instead of a still image."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from video_deshal import build_reel_video

SCENES = [
    {"text": "অফিসে বসের মেসেজ:\n\"একটু ফ্রি আছো?\"", "theme": "berry", "emoji": "😨"},
    {"text": "আমি রিপ্লাই দিলাম,\n\"জি স্যার, বলুন\"", "theme": "grape", "emoji": "😰"},
    {"text": "বস বললেন,\n\"পাসওয়ার্ডটা কী ছিল যেন?\"", "theme": "mango", "emoji": "🙄"},
    {"text": "এই টেনশনটা\n*শুধু আমরাই বুঝি* 😂", "theme": "mint", "emoji": "😂"},
]

if __name__ == "__main__":
    build_reel_video(SCENES, "images/deshal_reel_demo1_916.mp4")
