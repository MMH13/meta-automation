# -*- coding: utf-8 -*-
"""Daily Wisdom — turns one compact reel spec into the beats list
video_wisdom_stock.build() expects, plus the Facebook caption.

Each reel is a single self-contained idea (not a countdown), so the shape is
simple and fixed: hook -> insight -> end. `*starred*` in on-screen text
becomes the bronze highlight span (see image_reel_wisdom_overlay._lines_html
usage); keep the highlighted phrase to the ONE word or short phrase that
should land hardest.

    reel(slug, pillar,
         hook_text, hook_vo, hook_query,
         insight_text, insight_vo, insight_query,
         end_text, end_vo, end_query,
         cta="", caption="", hashtags="")
    -> (slug, pillar, beats, caption)
"""

DEFAULT_TAGS = "#Wisdom #Stoicism #LifeLessons #Mindset"


def reel(slug, pillar,
         hook_text, hook_vo, hook_query,
         insight_text, insight_vo, insight_query,
         end_text, end_vo, end_query,
         cta="", caption="", hashtags=DEFAULT_TAGS):
    beats = [
        {"kind": "hook", "text": hook_text, "narration": hook_vo, "query": hook_query},
        {"kind": "beat", "text": insight_text, "narration": insight_vo, "query": insight_query},
        {"kind": "end", "text": end_text, "narration": end_vo, "query": end_query, "cta": cta},
    ]
    full_caption = f"{caption}\n\n{hashtags}".strip() if caption else hashtags
    return slug, pillar, beats, full_caption
