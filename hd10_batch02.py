# -*- coding: utf-8 -*-
"""Health Daily - 10 reels/day cadence, batch 2 (days 6-10).
Niches: sleep science, exercise/movement fundamentals.
"""

REELS = [
("hd10_d6_1_sleep_cycles_90min", [
 {"kind": "hook", "text": "Sleep happens in\n~90 minute\ncycles, not one block.", "narration": "Sleep isn't one long block, it actually happens in cycles of about ninety minutes each.", "query": "person sleeping peacefully bed"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Each cycle moves\nthrough light, deep,\nand REM sleep.", "narration": "Each cycle moves you through light sleep, deep sleep, and REM sleep in sequence.", "query": "sleep cycle night bedroom"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "Waking mid-cycle\nis why some mornings\nfeel rougher.", "narration": "Waking up in the middle of a cycle is exactly why some mornings feel so much rougher than others.", "query": "person waking up tired"},
 {"kind": "end", "query": "person waking up tired", "text": "Timing your wake-up\nmatters as much as hours.", "question": "Do you wake up groggy some mornings?", "narration": "Timing your wake-up can matter almost as much as total hours slept."},
], "Sleep happens in ~90 minute cycles 🌙\n\nEach cycle moves through light, deep, and REM sleep. Waking mid-cycle is why some mornings feel rougher than others.\n\n💚 Bookmark this sleep-cycle basic.\n\n💬 Do you wake up groggy some mornings?"),

("hd10_d6_2_rem_dreams_memory", [
 {"kind": "hook", "text": "REM sleep is when\nmost of your\ndreaming happens.", "narration": "REM sleep is the stage where most of your vivid dreaming actually takes place.", "query": "person dreaming sleeping night"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your brain activity\nin REM looks almost\nlike being awake.", "narration": "Brain activity during REM sleep looks strikingly similar to being wide awake.", "query": "brain activity illustration sleep"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "REM sleep helps\nfile away memories\nfrom the day.", "narration": "This stage plays a real role in helping your brain file away memories from the day.", "query": "person studying learning memory"},
 {"kind": "end", "query": "person studying learning memory", "text": "Cutting sleep short\ncuts REM the most.", "question": "Do you remember your dreams often?", "narration": "Cutting your sleep short tends to cut into REM time the most."},
], "REM sleep looks like being awake, brain-wise 🧠\n\nThis stage plays a real role in filing away memories from your day. Cutting sleep short cuts REM the most.\n\n💚 Bookmark this REM sleep fact.\n\n💬 Do you remember your dreams often?"),

("hd10_d6_3_circadian_clock_basics", [
 {"kind": "hook", "text": "You have a master\nclock in your brain\nrunning on a 24h loop.", "narration": "Your brain runs a master clock, a small cluster of cells syncing your whole body to roughly a twenty-four hour loop.", "query": "sunrise sunset clock time"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Sunlight is the\nmain signal that\nresets it daily.", "narration": "Morning sunlight is the single strongest signal that resets this internal clock every day.", "query": "morning sunlight window person"},
 {"kind": "beat", "kicker": "WHAT THROWS IT OFF", "text": "Irregular sleep\nand late-night light\nconfuse the signal.", "narration": "Irregular sleep times and bright light late at night quietly confuse that daily signal.", "query": "person phone bed night light"},
 {"kind": "end", "query": "person phone bed night light", "text": "Morning light,\nsteadier rhythm.", "question": "Do you get sunlight soon after waking up?", "narration": "Getting morning light is a simple, free way to keep that rhythm steady."},
], "You have a master clock in your brain ⏰\n\nMorning sunlight is the strongest signal that resets it daily. Irregular sleep and late-night light confuse the signal.\n\n💚 Bookmark this circadian rhythm basic.\n\n💬 Do you get sunlight soon after waking up?"),

("hd10_d6_4_sleep_pressure_adenosine", [
 {"kind": "hook", "text": "The longer you're\nawake, the more\n'sleep pressure' builds.", "narration": "The longer you stay awake, the more a chemical called adenosine builds up, creating what's called sleep pressure.", "query": "person yawning tired evening"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Caffeine works by\nblocking adenosine's\nsignal, not removing it.", "narration": "Caffeine works by blocking adenosine's signal to your brain, it doesn't actually remove the buildup.", "query": "coffee cup desk work"},
 {"kind": "beat", "kicker": "WHAT HAPPENS LATER", "text": "That blocked pressure\ncatches up once\ncaffeine wears off.", "narration": "Once the caffeine wears off, that blocked sleep pressure catches up all at once.", "query": "person tired afternoon crash"},
 {"kind": "end", "query": "person tired afternoon crash", "text": "That's the\nafternoon caffeine crash.", "question": "Do you get a crash after your caffeine wears off?", "narration": "That's exactly what the afternoon caffeine crash actually is."},
], "Caffeine doesn't remove sleep pressure, it just blocks it ☕\n\nAdenosine keeps building up in the background. Once caffeine wears off, that pressure catches up all at once.\n\n💚 Bookmark this caffeine science.\n\n💬 Do you get a crash after your caffeine wears off?"),

("hd10_d6_5_nap_before_3pm_rule", [
 {"kind": "hook", "text": "A nap after 3pm\ncan quietly wreck\nyour night's sleep.", "narration": "A nap taken after three in the afternoon can quietly steal from your sleep pressure that night.", "query": "person napping afternoon couch"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Late naps eat into\nthe sleep pressure\nyou need for bedtime.", "narration": "Late naps eat directly into the sleep pressure your body has been building up all day for bedtime.", "query": "clock afternoon nap time"},
 {"kind": "beat", "kicker": "THE SWEET SPOT", "text": "A short nap before\n3pm rarely causes\nany real problem.", "narration": "A short nap taken before three in the afternoon rarely causes any real disruption to nighttime sleep.", "query": "person resting midday"},
 {"kind": "end", "query": "person resting midday", "text": "Nap early,\nsleep easy later.", "question": "What time do you usually nap?", "narration": "Nap earlier in the day, and your night's sleep stays easy."},
], "That late nap might be wrecking your night's sleep 😴\n\nNaps after 3pm eat into the sleep pressure you need for bedtime. A short nap before 3pm rarely causes issues.\n\n💚 Bookmark this before your next nap.\n\n💬 What time do you usually nap?"),

("hd10_d6_6_cold_bedroom_deep_sleep", [
 {"kind": "hook", "text": "A slightly cold\nroom helps you\nreach deep sleep faster.", "narration": "A slightly cool bedroom actually helps your body reach deep sleep faster.", "query": "bedroom cool night sleep"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your core body\ntemperature naturally\ndrops to fall asleep.", "narration": "Your core body temperature naturally needs to drop a notch for you to fall asleep in the first place.", "query": "person sleeping comfortable bed"},
 {"kind": "beat", "kicker": "THE SWEET SPOT", "text": "Around 18-20°C\n(65-68°F) works\nfor most people.", "narration": "A room temperature around eighteen to twenty degrees Celsius tends to work well for most people.", "query": "thermostat bedroom cozy"},
 {"kind": "end", "query": "thermostat bedroom cozy", "text": "Cooler room,\neasier drift-off.", "question": "Do you sleep with the room warm or cool?", "narration": "A cooler room genuinely makes drifting off that much easier."},
], "A cool bedroom helps you reach deep sleep faster ❄️\n\nYour core temperature naturally needs to drop to fall asleep. 18-20°C works well for most people.\n\n💚 Bookmark this before bedtime tonight.\n\n💬 Do you sleep with the room warm or cool?"),

("hd10_d7_1_consistent_wake_time", [
 {"kind": "hook", "text": "A consistent\nwake-up time matters\nmore than bedtime.", "narration": "A consistent wake-up time actually matters more for your body clock than a fixed bedtime.", "query": "alarm clock morning wake"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your body clock\nanchors itself around\nwhen you wake, not sleep.", "narration": "Your internal body clock tends to anchor itself around when you wake up, not exactly when you fall asleep.", "query": "person waking up stretching"},
 {"kind": "beat", "kicker": "SIMPLE RULE", "text": "Keep wake time\nwithin an hour,\neven on weekends.", "narration": "Keeping your wake time within about an hour, even on weekends, keeps that clock steady.", "query": "weekend morning routine"},
 {"kind": "end", "query": "weekend morning routine", "text": "Same wake time,\nsteadier energy.", "question": "Do you wake up at the same time daily?", "narration": "The same wake time really does mean steadier energy through the week."},
], "Your wake-up time matters more than bedtime ⏰\n\nYour body clock anchors around when you wake, not sleep. Keep it within an hour, even on weekends.\n\n💚 Bookmark this sleep consistency tip.\n\n💬 Do you wake up at the same time daily?"),

("hd10_d7_2_sleep_debt_cant_fully_repay", [
 {"kind": "hook", "text": "You can't fully\n'pay back' a week\nof lost sleep in one night.", "narration": "You genuinely can't pay back a whole week of lost sleep with one long night of rest.", "query": "person sleeping late weekend"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Some functions\nrecover fast, others\ntake several nights.", "narration": "Some brain functions bounce back quickly, but others can take several consistent nights to fully recover.", "query": "person tired recovering rest"},
 {"kind": "beat", "kicker": "BETTER APPROACH", "text": "Small, consistent\nextra sleep beats\none big catch-up.", "narration": "Small, consistent extra sleep over several nights beats trying one big catch-up session.", "query": "person sleeping bedroom peaceful"},
 {"kind": "end", "query": "person sleeping bedroom peaceful", "text": "Consistency beats\na single long sleep-in.", "question": "Do you try to 'catch up' on sleep over weekends?", "narration": "Consistency genuinely beats one dramatic sleep-in."},
], "You can't fully 'pay back' a week of lost sleep 💤\n\nSome brain functions take several nights to recover. Small, consistent extra sleep beats one big catch-up.\n\n💚 Bookmark this sleep debt reality check.\n\n💬 Do you try to 'catch up' on sleep over weekends?"),

("hd10_d7_3_bedroom_darkness_melatonin", [
 {"kind": "hook", "text": "Even small amounts\nof light can\nsuppress melatonin.", "narration": "Even small amounts of light in a room can suppress the melatonin your body is trying to release.", "query": "dark bedroom night sleep"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Melatonin is the\nhormone that signals\n'time to sleep'.", "narration": "Melatonin is the hormone your brain releases specifically to signal that it's time to sleep.", "query": "melatonin hormone sleep illustration"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "Blackout curtains\nor an eye mask\nmake a real difference.", "narration": "Blackout curtains or a simple eye mask can make a genuinely noticeable difference.", "query": "blackout curtains bedroom dark"},
 {"kind": "end", "query": "blackout curtains bedroom dark", "text": "Darker room,\nbetter melatonin flow.", "question": "How dark is your bedroom at night?", "narration": "A darker room genuinely lets your melatonin do its job properly."},
], "Even small light can suppress your melatonin 🌑\n\nMelatonin is the hormone that signals 'time to sleep'. Blackout curtains or an eye mask make a real difference.\n\n💚 Bookmark this before tonight.\n\n💬 How dark is your bedroom at night?"),

("hd10_d7_4_caffeine_half_life_sleep", [
 {"kind": "hook", "text": "Caffeine has a\nhalf-life of about\n5-6 hours in your body.", "narration": "Caffeine sticks around in your body with a half-life of roughly five to six hours.", "query": "coffee cup afternoon"},
 {"kind": "beat", "kicker": "WHAT THAT MEANS", "text": "A 3pm coffee still\nleaves a quarter\nof its caffeine at midnight.", "narration": "That means a coffee at three in the afternoon can still leave a quarter of its caffeine in your system by midnight.", "query": "clock afternoon coffee"},
 {"kind": "beat", "kicker": "SIMPLE RULE", "text": "Cutting caffeine by\nearly-to-mid afternoon\nprotects your sleep.", "narration": "Cutting caffeine off by early-to-mid afternoon genuinely protects the quality of your sleep that night.", "query": "no coffee afternoon cutoff"},
 {"kind": "end", "query": "no coffee afternoon cutoff", "text": "Know your\ncutoff time.", "question": "What time do you usually stop drinking caffeine?", "narration": "Knowing your own cutoff time is worth figuring out."},
], "Your 3pm coffee is still active at midnight ☕\n\nCaffeine's half-life is 5-6 hours. Cutting it off by early-to-mid afternoon protects your sleep that night.\n\n💚 Bookmark this caffeine timing fact.\n\n💬 What time do you usually stop drinking caffeine?"),

("hd10_d7_5_sleep_and_memory_consolidation", [
 {"kind": "hook", "text": "Your brain files\naway what you learned\nmostly while you sleep.", "narration": "Your brain does a huge amount of memory filing and organizing specifically while you sleep.", "query": "person sleeping learning memory"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "This process is\ncalled memory\nconsolidation.", "narration": "This process has a name, memory consolidation, and it happens mostly during deep and REM sleep.", "query": "brain memory illustration sleep"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "Pulling an all-nighter\nto study can actually\nbackfire the next day.", "narration": "That's part of why pulling an all-nighter to study can genuinely backfire on you the next day.", "query": "person studying tired night"},
 {"kind": "end", "query": "person studying tired night", "text": "Sleep is part\nof learning, not a break from it.", "question": "Have you ever pulled an all-nighter to study?", "narration": "Sleep is honestly part of the learning process, not a break from it."},
], "Your brain files away memories mostly while you sleep 🧠\n\nThis is called memory consolidation. Pulling an all-nighter to study can genuinely backfire the next day.\n\n💚 Bookmark this before exam season.\n\n💬 Have you ever pulled an all-nighter to study?"),

("hd10_d7_6_weekend_sleep_shift_effect", [
 {"kind": "hook", "text": "Sleeping in a lot\non weekends creates\na mini jet lag.", "narration": "Sleeping in significantly on weekends can actually create a small version of jet lag by Monday.", "query": "person sleeping late weekend bed"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Doctors call it\n'social jet lag' -\nit's a real pattern.", "narration": "Researchers actually have a name for it, social jet lag, and it's a genuinely well-documented pattern.", "query": "weekend versus weekday clock"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "Keeping wake time\nwithin an hour helps\navoid the Monday slump.", "narration": "Keeping your wake time within about an hour of your weekday schedule helps avoid that rough Monday slump.", "query": "monday morning alarm tired"},
 {"kind": "end", "query": "monday morning alarm tired", "text": "Small shift,\nsmoother Mondays.", "question": "Do you sleep in a lot on weekends?", "narration": "A smaller shift on weekends genuinely means smoother Mondays."},
], "Sleeping in on weekends creates a mini jet lag 🛫\n\nResearchers call it 'social jet lag', a real, documented pattern. Keep wake time within an hour to avoid the Monday slump.\n\n💚 Bookmark this before your next weekend.\n\n💬 Do you sleep in a lot on weekends?"),

("hd10_d8_1_light_therapy_morning", [
 {"kind": "hook", "text": "Bright light\nin the morning can\nlift mood and energy.", "narration": "Bright light exposure in the morning can genuinely lift both mood and energy for the day.", "query": "morning sunlight bright window"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "It works by helping\nanchor your circadian\nrhythm earlier in the day.", "narration": "It works by helping anchor your circadian rhythm firmly earlier in the day, setting the tone for the rest of it.", "query": "sunrise morning person outside"},
 {"kind": "beat", "kicker": "SIMPLE PRACTICE", "text": "Even 10 minutes\noutside soon after\nwaking can help.", "narration": "Even just ten minutes outside soon after waking up can genuinely make a noticeable difference.", "query": "person walking outside morning"},
 {"kind": "end", "query": "person walking outside morning", "text": "Step outside\nbefore your phone.", "question": "Do you get outside soon after waking up?", "narration": "Stepping outside before reaching for your phone is a simple habit worth trying."},
], "Ten minutes of morning light can lift your whole day ☀️\n\nIt helps anchor your circadian rhythm earlier. Even a short walk outside soon after waking makes a difference.\n\n💚 Bookmark this morning habit.\n\n💬 Do you get outside soon after waking up?"),

("hd10_d8_2_sleep_apnea_awareness", [
 {"kind": "hook", "text": "Loud snoring can\nsometimes be a sign\nof something more.", "narration": "Loud, consistent snoring can sometimes be a sign of a condition called sleep apnea, not just a nuisance.", "query": "person sleeping snoring bedroom"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "It means breathing\nbriefly stops and\nstarts many times a night.", "narration": "Sleep apnea means breathing actually briefly stops and restarts, sometimes dozens of times a night.", "query": "person tired despite sleep"},
 {"kind": "beat", "kicker": "COMMON SIGNS", "text": "Waking up tired\ndespite a full\nnight is a key clue.", "narration": "Waking up feeling exhausted despite a full night in bed is one of the clearest clues.", "query": "person exhausted morning"},
 {"kind": "end", "query": "person exhausted morning", "text": "Worth mentioning\nto a doctor.", "question": "Have you ever been told you snore loudly?", "narration": "It's genuinely worth mentioning to a doctor if this sounds familiar."},
], "Loud snoring can be more than just annoying 😴\n\nIt can be a sign of sleep apnea, where breathing briefly stops many times a night. Worth mentioning to a doctor.\n\n💚 Bookmark this and share if it applies to someone you know.\n\n💬 Have you ever been told you snore loudly?"),

("hd10_d8_3_white_noise_sleep_quality", [
 {"kind": "hook", "text": "A steady hum can\nhelp you sleep through\nrandom household noise.", "narration": "A steady background hum, like a fan, can genuinely help mask random noises that would otherwise wake you.", "query": "fan bedroom night quiet"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "It's not silence\nthat matters most,\nit's consistency.", "narration": "It's not total silence that matters most for sleep, it's actually consistency in the background sound.", "query": "quiet bedroom night sleep"},
 {"kind": "beat", "kicker": "SIMPLE OPTION", "text": "A fan, air purifier,\nor white noise app\nall work similarly.", "narration": "A simple fan, an air purifier, or a white noise app all tend to work about the same for this purpose.", "query": "air purifier bedroom device"},
 {"kind": "end", "query": "air purifier bedroom device", "text": "Steady sound,\nfewer wake-ups.", "question": "Do you sleep with any background noise?", "narration": "A steady sound genuinely means fewer random wake-ups through the night."},
], "It's not silence that matters, it's consistency 🌀\n\nA steady hum like a fan masks random noises that would otherwise wake you. Consistency beats total silence.\n\n💚 Bookmark this before tonight.\n\n💬 Do you sleep with any background noise?"),

("hd10_d8_4_sleep_growth_hormone_release", [
 {"kind": "hook", "text": "Most of your growth\nhormone is released\nduring deep sleep.", "narration": "The majority of your body's growth hormone is released specifically during deep sleep at night.", "query": "person sleeping deep bedroom"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "This hormone helps\nrepair tissue and\nbuild muscle overnight.", "narration": "This hormone plays a real role in repairing tissue and helping build muscle while you rest.", "query": "muscle recovery athlete rest"},
 {"kind": "beat", "kicker": "WHY IT MATTERS FOR ACTIVE PEOPLE", "text": "Skimping on sleep\ncan blunt workout\nrecovery noticeably.", "narration": "Skimping on sleep can genuinely blunt how well your body recovers from a hard workout.", "query": "athlete resting recovery sleep"},
 {"kind": "end", "query": "athlete resting recovery sleep", "text": "Sleep is part\nof the training plan.", "question": "Do you prioritize sleep around workout days?", "narration": "Sleep genuinely belongs in the training plan, not as an afterthought."},
], "Growth hormone is released mostly during deep sleep 💪\n\nIt helps repair tissue and build muscle overnight. Skimping on sleep can blunt workout recovery noticeably.\n\n💚 Bookmark this if you train regularly.\n\n💬 Do you prioritize sleep around workout days?"),

("hd10_d8_5_pre_sleep_routine_signal", [
 {"kind": "hook", "text": "A consistent\npre-sleep routine\nsignals your brain to wind down.", "narration": "A consistent pre-sleep routine gives your brain a clear, repeated signal that it's time to start winding down.", "query": "bedtime routine calm evening"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your brain learns\nto associate certain\ncues with sleep over time.", "narration": "Your brain genuinely learns over time to associate certain repeated cues with the approach of sleep.", "query": "person reading book bed"},
 {"kind": "beat", "kicker": "SIMPLE EXAMPLES", "text": "Dimming lights,\nreading, or stretching\nall work as cues.", "narration": "Dimming the lights, reading a few pages, or light stretching can all work well as those cues.", "query": "dim lamp evening bedroom"},
 {"kind": "end", "query": "dim lamp evening bedroom", "text": "Same cues,\neasier wind-down.", "question": "Do you have a wind-down routine before bed?", "narration": "The same cues, repeated nightly, genuinely make winding down easier over time."},
], "Your brain learns to associate cues with sleep 🕯️\n\nDimming lights, reading, or stretching before bed all work as signals. Same cues, easier wind-down over time.\n\n💚 Bookmark this before building a routine.\n\n💬 Do you have a wind-down routine before bed?"),

("hd10_d8_6_exercise_timing_sleep", [
 {"kind": "hook", "text": "Exercise usually\nhelps sleep, but\ntiming can matter.", "narration": "Exercise almost always helps sleep quality overall, but the timing of it can matter for some people.", "query": "person exercising evening gym"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Intense workouts\nlate at night can\nraise alertness for some.", "narration": "Very intense workouts late at night can raise core temperature and alertness enough to delay sleep for some people.", "query": "intense workout night gym"},
 {"kind": "beat", "kicker": "WHAT USUALLY WORKS", "text": "Most people do\nfine with evening\nexercise, just not right before bed.", "narration": "Most people actually do just fine with evening exercise, as long as it's not right up against bedtime.", "query": "person exercising evening outdoor"},
 {"kind": "end", "query": "person exercising evening outdoor", "text": "Give yourself\na buffer before bed.", "question": "Do you work out in the evening?", "narration": "A small buffer between your workout and bedtime is usually all it takes."},
], "Evening workouts usually help sleep, with one catch ⚡\n\nVery intense sessions right before bed can raise alertness for some people. A small buffer usually solves it.\n\n💚 Bookmark this before your next evening workout.\n\n💬 Do you work out in the evening?"),

("hd10_d9_1_sleep_temperature_drop_body", [
 {"kind": "hook", "text": "Warm hands and feet\nat night are actually\na sleep-onset signal.", "narration": "Warm hands and feet at night are actually a sign your body is preparing to fall asleep.", "query": "person feet warm bed night"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your body sends\nblood to your\nextremities to cool your core.", "narration": "Your body sends blood out toward your hands and feet specifically to help cool your core temperature down.", "query": "blood circulation illustration warmth"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "That's why a warm\nshower before bed\ncan help you fall asleep.", "narration": "That's part of why a warm shower before bed can genuinely help you fall asleep faster afterward.", "query": "warm shower evening relax"},
 {"kind": "end", "query": "warm shower evening relax", "text": "Warm up, then\ncool down to sleep.", "question": "Do you take a warm shower before bed?", "narration": "Warm up first, and let your body cool down naturally into sleep."},
], "A warm shower before bed can help you fall asleep faster 🚿\n\nYour body sends blood to hands and feet to cool your core. That drop in core temp is a real sleep-onset signal.\n\n💚 Bookmark this before tonight.\n\n💬 Do you take a warm shower before bed?"),

("hd10_d9_2_insomnia_racing_thoughts", [
 {"kind": "hook", "text": "Racing thoughts\nat bedtime are\na very common pattern.", "narration": "Racing thoughts right at bedtime are an extremely common experience, not a personal failure.", "query": "person lying awake thinking bed"},
 {"kind": "beat", "kicker": "WHY IT HAPPENS", "text": "Lying still finally\ngives your brain\nspace to process the day.", "narration": "Lying still and quiet finally gives your busy brain the space it's been waiting for to process the day.", "query": "person awake ceiling bed"},
 {"kind": "beat", "kicker": "SIMPLE HELP", "text": "Writing down\ntomorrow's worries\ncan quiet the loop.", "narration": "Writing down tomorrow's worries on paper before bed can genuinely quiet that mental loop.", "query": "journaling notebook evening"},
 {"kind": "end", "query": "journaling notebook evening", "text": "Get it on paper,\nnot in your head.", "question": "Do racing thoughts keep you up sometimes?", "narration": "Getting it down on paper, instead of carrying it in your head, really does help."},
], "Racing thoughts at bedtime are incredibly common 💭\n\nLying still finally gives your brain space to process the day. Writing down tomorrow's worries can quiet the loop.\n\n💚 Bookmark this for a restless night.\n\n💬 Do racing thoughts keep you up sometimes?"),

("hd10_d9_3_sleep_quality_vs_quantity", [
 {"kind": "hook", "text": "8 hours of\nbroken sleep isn't\nthe same as 8 solid hours.", "narration": "Eight hours of broken, interrupted sleep is not the same thing as eight solid, uninterrupted hours.", "query": "person sleeping restless bed"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Frequent waking\ndisrupts the deep\nand REM stages most.", "narration": "Frequent waking through the night disrupts your deep and REM sleep stages the most.", "query": "person waking multiple times night"},
 {"kind": "beat", "kicker": "WHAT TO TRACK", "text": "How rested you feel\nmatters more than\njust the hours logged.", "narration": "How genuinely rested you feel matters more than just the raw number of hours logged.", "query": "person feeling rested morning"},
 {"kind": "end", "query": "person feeling rested morning", "text": "Quality counts\nas much as quantity.", "question": "Do you track your sleep quality or just hours?", "narration": "Quality genuinely counts for just as much as the total quantity."},
], "8 broken hours ≠ 8 solid hours of sleep 🌙\n\nFrequent waking disrupts deep and REM sleep the most. How rested you feel matters more than the raw number.\n\n💚 Bookmark this sleep quality reminder.\n\n💬 Do you track your sleep quality or just hours?"),

("hd10_d9_4_sleep_and_immune_repair", [
 {"kind": "hook", "text": "Skimping on sleep\ncan quietly weaken\nyour immune defenses.", "narration": "Skimping on sleep, even for a few nights, can quietly weaken your body's immune defenses.", "query": "person sick tired immune"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Your immune system\nreleases protective\nproteins mostly while you sleep.", "narration": "Your immune system releases certain protective proteins called cytokines mostly during sleep.", "query": "immune system illustration health"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "That's part of why\nyou feel so wiped out\nwhen fighting an illness.", "narration": "That's part of why your body pushes you so hard to sleep more when you're already fighting an illness.", "query": "person resting sick recovering"},
 {"kind": "end", "query": "person resting sick recovering", "text": "Sleep more when\nyour body asks for it.", "question": "Do you sleep more when you're getting sick?", "narration": "Sleeping more when your body asks for it is your immune system doing exactly its job."},
], "Your immune system does its best work while you sleep 🛡️\n\nProtective proteins called cytokines are released mostly during sleep. That's why your body craves rest when you're sick.\n\n💚 Bookmark this before cold season.\n\n💬 Do you sleep more when you're getting sick?"),

("hd10_d9_5_napping_workplace_stigma", [
 {"kind": "hook", "text": "A short nap isn't\nlaziness, it's a\nreal performance tool.", "narration": "A short nap isn't a sign of laziness, it's genuinely a well-studied performance tool.", "query": "person napping desk break"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Some high-performance\nteams and pilots\nuse scheduled naps.", "narration": "Some elite athletic teams and even pilots use scheduled short naps as part of their performance routine.", "query": "person resting break work"},
 {"kind": "beat", "kicker": "THE RIGHT LENGTH", "text": "10-20 minutes\navoids the post-nap\ngroggy feeling.", "narration": "Keeping a nap to ten or twenty minutes helps you avoid that heavy, groggy feeling afterward.", "query": "short nap timer rest"},
 {"kind": "end", "query": "short nap timer rest", "text": "A short nap\nis a smart tool.", "question": "Do you ever nap during the day?", "narration": "A short, well-timed nap is a genuinely smart tool, not something to feel guilty about."},
], "A 15-minute nap isn't laziness, it's strategy 😴\n\nSome elite teams and pilots use scheduled naps for performance. 10-20 minutes avoids the groggy after-effect.\n\n💚 Bookmark this if you feel guilty about napping.\n\n💬 Do you ever nap during the day?"),

("hd10_d9_6_screen_time_before_bed", [
 {"kind": "hook", "text": "It's not just the\nlight from your phone\nkeeping you up.", "narration": "It's not only the blue light from your phone that keeps you up, the content itself plays a role too.", "query": "person phone bed night scrolling"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Scrolling stimulating\ncontent keeps your\nbrain alert and engaged.", "narration": "Scrolling through stimulating or emotional content keeps your brain alert and engaged, delaying sleep onset.", "query": "phone screen scrolling social media"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "A boring book beats\na stimulating feed\nright before bed.", "narration": "A calm, unstimulating book genuinely beats a fast-moving social feed right before bed.", "query": "person reading book calm bed"},
 {"kind": "end", "query": "person reading book calm bed", "text": "It's the content,\nnot just the screen.", "question": "What's the last thing you look at before sleeping?", "narration": "It's really the content, as much as the screen itself, that matters most."},
], "It's not just the blue light keeping you up 📱\n\nScrolling stimulating content keeps your brain alert. A calm book beats a fast-moving feed before bed.\n\n💚 Bookmark this before tonight.\n\n💬 What's the last thing you look at before sleeping?"),

("hd10_d10_1_zone2_cardio_basics", [
 {"kind": "hook", "text": "You don't need to\nsprint to get real\ncardio benefits.", "narration": "You don't need to be sprinting or gasping for air to get real, meaningful cardio benefits.", "query": "person jogging easy pace park"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Easy-paced cardio\nwhere you can still\ntalk builds your aerobic base.", "narration": "Easy-paced cardio, where you can still hold a conversation, builds a genuinely strong aerobic base over time.", "query": "person walking talking exercise"},
 {"kind": "beat", "kicker": "WHY IT WORKS", "text": "It trains your body\nto use fat for fuel\nmore efficiently.", "narration": "This easier pace trains your body to use fat as fuel more efficiently, which pays off later.", "query": "person exercising steady pace"},
 {"kind": "end", "query": "person exercising steady pace", "text": "Easy days\nbuild real fitness.", "question": "Do you always push hard when you exercise?", "narration": "Easy training days genuinely build real, lasting fitness too."},
], "You don't need to sprint for real cardio benefits 🏃\n\nEasy-paced cardio, where you can still talk, builds a strong aerobic base and trains fat-burning efficiency.\n\n💚 Bookmark this before your next cardio session.\n\n💬 Do you always push hard when you exercise?"),

("hd10_d10_2_muscle_soreness_normal", [
 {"kind": "hook", "text": "Sore muscles aren't\na sign of a\n'better' workout.", "narration": "Sore muscles the next day aren't actually a reliable sign that you had a better or more effective workout.", "query": "person stretching sore muscles"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Soreness comes from\nnew or unfamiliar\nmovement, not just intensity.", "narration": "That soreness mostly comes from new or unfamiliar movement patterns, not simply from how hard you pushed.", "query": "person exercising new movement"},
 {"kind": "beat", "kicker": "WHAT ACTUALLY MATTERS", "text": "Consistent, progressive\ntraining builds results,\nsoreness or not.", "narration": "Consistent, gradually progressive training is what actually builds results, whether you're sore or not.", "query": "person training gym consistent"},
 {"kind": "end", "query": "person training gym consistent", "text": "No soreness\ndoesn't mean no progress.", "question": "Do you judge a workout by how sore you get?", "narration": "No soreness the next day absolutely does not mean no progress was made."},
], "Sore muscles don't mean a 'better' workout 💪\n\nSoreness comes from unfamiliar movement, not just intensity. Consistent training builds results, sore or not.\n\n💚 Bookmark this fitness myth-buster.\n\n💬 Do you judge a workout by how sore you get?"),

("hd10_d10_3_walking_pace_health_marker", [
 {"kind": "hook", "text": "Your natural\nwalking pace can\nreflect overall fitness.", "narration": "Your natural, everyday walking pace can actually reflect quite a lot about your overall fitness level.", "query": "person walking street pace"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Researchers use\nwalking speed as\none simple health marker.", "narration": "Researchers genuinely use walking speed as one simple, low-cost marker of general health in studies.", "query": "people walking city street"},
 {"kind": "beat", "kicker": "SIMPLE PRACTICE", "text": "Picking up your pace\non regular walks\ncan build real fitness.", "narration": "Simply picking up the pace on your regular daily walks can build genuinely real fitness over time.", "query": "person brisk walking outdoor"},
 {"kind": "end", "query": "person brisk walking outdoor", "text": "A brisker walk\ncounts as exercise.", "question": "What's your usual walking pace like?", "narration": "A brisker walk genuinely counts as real exercise, not just a stroll."},
], "Your walking pace reflects your overall fitness 🚶\n\nResearchers use walking speed as a simple health marker. Picking up the pace on daily walks builds real fitness.\n\n💚 Bookmark this before your next walk.\n\n💬 What's your usual walking pace like?"),

("hd10_d10_4_strength_training_bone_density", [
 {"kind": "hook", "text": "Lifting weights\ndoes more than\nbuild muscle.", "narration": "Lifting weights does far more for your body than just building visible muscle.", "query": "person lifting weights gym"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "It also stimulates\nyour bones to stay\ndenser and stronger.", "narration": "Resistance training genuinely stimulates your bones to stay denser and stronger over the years.", "query": "bone density illustration health"},
 {"kind": "beat", "kicker": "WHY IT MATTERS LONG-TERM", "text": "This matters more\nas you age, when\nbone loss naturally speeds up.", "narration": "This matters even more as you age, since bone loss naturally speeds up later in life.", "query": "older person exercising strength"},
 {"kind": "end", "query": "older person exercising strength", "text": "Strength training\nis an investment.", "question": "Do you include strength training in your week?", "narration": "Strength training is genuinely a long-term investment in your future self."},
], "Lifting weights protects your bones, not just muscle 🦴\n\nResistance training stimulates bones to stay denser. This matters even more as bone loss naturally speeds up with age.\n\n💚 Bookmark this before your next workout.\n\n💬 Do you include strength training in your week?"),

("hd10_d10_5_exercise_snack_micro_movement", [
 {"kind": "hook", "text": "A few minutes of\nmovement here and\nthere genuinely adds up.", "narration": "A few scattered minutes of movement across the day genuinely add up more than people expect.", "query": "person stretching office break"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Researchers call\nthese short bursts\n'exercise snacks'.", "narration": "Researchers actually have a name for these short bursts of activity, calling them exercise snacks.", "query": "person quick exercise break desk"},
 {"kind": "beat", "kicker": "SIMPLE EXAMPLES", "text": "A minute of squats\nor stairs a few\ntimes a day counts.", "narration": "A minute of bodyweight squats or a quick set of stairs a few times a day genuinely counts.", "query": "person climbing stairs quick"},
 {"kind": "end", "query": "person climbing stairs quick", "text": "No gym required\nto move more.", "question": "Do you sneak in movement during your day?", "narration": "You don't need a gym membership to sneak in real, meaningful movement."},
], "'Exercise snacks' are a real, researched thing 🍎\n\nA minute of squats or a quick set of stairs a few times a day genuinely adds up. No gym required.\n\n💚 Bookmark this for busy days.\n\n💬 Do you sneak in movement during your day?"),

("hd10_d10_6_recovery_active_vs_rest", [
 {"kind": "hook", "text": "'Rest day' doesn't\nhave to mean\nzero movement.", "narration": "A rest day doesn't actually have to mean zero movement at all.", "query": "person light activity rest day"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Light activity like\nwalking can help clear\nsoreness faster than sitting.", "narration": "Light activity like an easy walk can genuinely help clear muscle soreness faster than sitting completely still.", "query": "person walking easy recovery"},
 {"kind": "beat", "kicker": "WHY IT WORKS", "text": "Gentle movement\nincreases blood flow\nto tired muscles.", "narration": "Gentle movement increases blood flow to tired muscles, helping deliver nutrients they need to recover.", "query": "blood flow muscle recovery"},
 {"kind": "end", "query": "blood flow muscle recovery", "text": "Move a little,\nrecover a lot.", "question": "What does your rest day usually look like?", "narration": "Moving a little on rest days can genuinely help you recover a lot faster."},
], "A rest day doesn't have to mean zero movement 🚶\n\nLight activity like an easy walk clears soreness faster than sitting still, by boosting blood flow to tired muscles.\n\n💚 Bookmark this for your next rest day.\n\n💬 What does your rest day usually look like?"),

("hd10_d6_7_exercise_warmup_injury_prevention", [
 {"kind": "hook", "text": "Skipping a warm-up\nis one of the most\ncommon injury triggers.", "narration": "Skipping a proper warm-up is genuinely one of the most common triggers behind exercise injuries.", "query": "person warming up stretching gym"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Cold muscles are\nstiffer and more prone\nto strains.", "narration": "Muscles that haven't warmed up are stiffer and noticeably more prone to strains under sudden load.", "query": "person stretching muscles gym"},
 {"kind": "beat", "kicker": "SIMPLE FIX", "text": "5-10 minutes of\nlight movement\nprepares your body well.", "narration": "Just five to ten minutes of light movement is usually enough to prepare your body properly.", "query": "light cardio warmup gym"},
 {"kind": "end", "query": "light cardio warmup gym", "text": "A few minutes\nnow saves weeks later.", "question": "Do you skip warm-ups sometimes?", "narration": "A few minutes now can genuinely save you weeks of recovery later."},
], "Skipping the warm-up is a top injury trigger 🔥\n\nCold muscles are stiffer and more prone to strains. Just 5-10 minutes of light movement prepares your body well.\n\n💚 Bookmark this before your next workout.\n\n💬 Do you skip warm-ups sometimes?"),

("hd10_d6_8_heart_rate_zones_basics", [
 {"kind": "hook", "text": "Not every workout\nneeds to hit your\nmax heart rate.", "narration": "Not every single workout needs to push you anywhere near your maximum heart rate.", "query": "heart rate monitor exercise"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Different heart rate\nzones train different\nsystems in your body.", "narration": "Different heart rate zones actually train different systems in your body, from fat-burning to peak performance.", "query": "person exercising heart rate watch"},
 {"kind": "beat", "kicker": "SIMPLE TAKEAWAY", "text": "Mixing easy and\nhard days trains\nyour body more completely.", "narration": "Mixing easy and hard training days trains your body far more completely than going hard every time.", "query": "person varied workout intensity"},
 {"kind": "end", "query": "person varied workout intensity", "text": "Variety in\nintensity, not just effort.", "question": "Do you track your heart rate during workouts?", "narration": "Variety in intensity matters just as much as raw effort."},
], "Not every workout needs your max heart rate ❤️\n\nDifferent heart rate zones train different systems. Mixing easy and hard days trains your body more completely.\n\n💚 Bookmark this training basic.\n\n💬 Do you track your heart rate during workouts?"),

("hd10_d6_9_mental_health_movement_link", [
 {"kind": "hook", "text": "Movement is one of\nthe most researched\ntools for mood.", "narration": "Physical movement is genuinely one of the most researched, accessible tools for supporting mood.", "query": "person exercising outdoor happy"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Even a 10-minute\nwalk can measurably\nlift how you feel.", "narration": "Even a short ten-minute walk can measurably lift how you feel, according to a wide body of research.", "query": "person walking outdoor mood"},
 {"kind": "beat", "kicker": "WHY IT WORKS", "text": "Movement changes\nbrain chemistry and\nlowers stress hormones.", "narration": "Movement genuinely changes brain chemistry and helps lower circulating stress hormones.", "query": "person relaxed after exercise"},
 {"kind": "end", "query": "person relaxed after exercise", "text": "A short walk\ncan shift your whole mood.", "question": "Does exercise change your mood noticeably?", "narration": "A short walk really can shift your whole mood, more than people expect."},
], "A 10-minute walk can measurably lift your mood 🚶\n\nMovement changes brain chemistry and lowers stress hormones. One of the most researched tools we have.\n\n💚 Bookmark this for a tough day.\n\n💬 Does exercise change your mood noticeably?"),

("hd10_d6_10_stretching_before_after_debate", [
 {"kind": "hook", "text": "Static stretching\nbefore a workout\nmight not be ideal.", "narration": "Holding long, static stretches right before a workout might not actually be the ideal approach.", "query": "person static stretching before"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Some research links\nit to a brief dip\nin muscle power.", "narration": "Some research links long static stretching right before intense effort to a brief, temporary dip in muscle power.", "query": "person stretching gym floor"},
 {"kind": "beat", "kicker": "BETTER APPROACH", "text": "Save deep static\nstretches for after,\nwarm up dynamically before.", "narration": "Saving deep static stretches for after your workout, and warming up dynamically before, tends to work better.", "query": "dynamic warmup movement gym"},
 {"kind": "end", "query": "dynamic warmup movement gym", "text": "Dynamic before,\nstatic after.", "question": "When do you usually stretch?", "narration": "Dynamic movement before, static stretching after, that's the general rule of thumb."},
], "Static stretching before a workout? Rethink it 🤸\n\nIt's linked to a brief dip in muscle power. Dynamic warm-ups before, static stretches after, works better.\n\n💚 Bookmark this before your next session.\n\n💬 When do you usually stretch?"),

("hd10_d7_7_resting_heart_rate_fitness_marker", [
 {"kind": "hook", "text": "Your resting heart\nrate says a lot\nabout your fitness.", "narration": "Your resting heart rate, taken first thing in the morning, actually says a lot about your fitness level.", "query": "heart rate pulse check morning"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "A lower resting rate\noften means a more\nefficient heart.", "narration": "A lower resting heart rate often means your heart is pumping more blood with every single beat.", "query": "heart health illustration"},
 {"kind": "beat", "kicker": "SIMPLE TRACKING", "text": "Checking it weekly\ncan reveal fitness\ntrends over time.", "narration": "Checking your resting heart rate weekly can reveal genuinely useful fitness trends over months.", "query": "person checking pulse wrist"},
 {"kind": "end", "query": "person checking pulse wrist", "text": "One number,\nworth tracking.", "question": "Do you know your resting heart rate?", "narration": "One simple number that's genuinely worth keeping an eye on."},
], "Your resting heart rate says a lot about your fitness ❤️\n\nA lower resting rate often means a more efficient heart. Checking it weekly reveals real fitness trends over time.\n\n💚 Bookmark this and check yours tomorrow morning.\n\n💬 Do you know your resting heart rate?"),

("hd10_d7_8_exercise_mood_endorphins", [
 {"kind": "hook", "text": "The 'runner's high'\nis a real, measurable\nbrain chemistry shift.", "narration": "The famous runner's high is a real, genuinely measurable shift in brain chemistry, not just a figure of speech.", "query": "runner outdoor happy exercise"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Endorphins and other\ncompounds rise during\nsustained exercise.", "narration": "Endorphins and other feel-good compounds genuinely rise in your bloodstream during sustained exercise.", "query": "person running exercising outdoor"},
 {"kind": "beat", "kicker": "YOU DON'T NEED A MARATHON", "text": "Even moderate\nexercise can trigger\na noticeable lift.", "narration": "Even moderate exercise, not just an intense long run, can trigger a genuinely noticeable mood lift.", "query": "person jogging moderate pace"},
 {"kind": "end", "query": "person jogging moderate pace", "text": "A real chemistry\nshift, not just a mood.", "question": "Have you felt a 'runner's high' before?", "narration": "It's a real chemistry shift in your brain, not just a passing mood."},
], "The 'runner's high' is real brain chemistry 🏃\n\nEndorphins genuinely rise during sustained exercise. You don't need a marathon, moderate exercise triggers it too.\n\n💚 Bookmark this before your next run.\n\n💬 Have you felt a 'runner's high' before?"),

("hd10_d7_9_overtraining_warning_signs", [
 {"kind": "hook", "text": "More exercise\nisn't always\nbetter exercise.", "narration": "More exercise isn't always better exercise, your body genuinely has a limit to how much it can absorb.", "query": "person exhausted after workout"},
 {"kind": "beat", "kicker": "WARNING SIGNS", "text": "Persistent fatigue,\nirritability, and\nworse performance are clues.", "narration": "Persistent fatigue, irritability, and performance that's quietly getting worse are all real warning signs.", "query": "person tired fatigued gym"},
 {"kind": "beat", "kicker": "WHAT HELPS", "text": "A planned lighter\nweek every so often\nprevents burnout.", "narration": "Building in a planned, lighter training week every so often genuinely prevents this kind of burnout.", "query": "person resting recovery week"},
 {"kind": "end", "query": "person resting recovery week", "text": "Listen before\nyou're forced to stop.", "question": "Have you ever pushed through overtraining signs?", "narration": "Listening to these signs early beats being forced to stop later."},
], "More exercise isn't always better exercise ⚠️\n\nPersistent fatigue, irritability, and worse performance are warning signs. A planned lighter week prevents burnout.\n\n💚 Bookmark this if you train hard often.\n\n💬 Have you ever pushed through overtraining signs?"),

("hd10_d7_10_functional_strength_daily_life", [
 {"kind": "hook", "text": "Strength training\npays off in ways\nbeyond the gym.", "narration": "Strength training genuinely pays off in ways that go far beyond how you look or perform in the gym.", "query": "person carrying groceries strong"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Carrying groceries,\nclimbing stairs, getting\nup off the floor all use it.", "narration": "Carrying groceries, climbing stairs, and getting up off the floor all draw directly on functional strength.", "query": "person climbing stairs daily life"},
 {"kind": "beat", "kicker": "WHY IT MATTERS LONG-TERM", "text": "This kind of strength\nbecomes more valuable,\nnot less, as you age.", "narration": "This kind of everyday functional strength becomes more valuable, not less, as the years go on.", "query": "older person active independent"},
 {"kind": "end", "query": "older person active independent", "text": "Train for\nreal life, not just the mirror.", "question": "Do you think about strength training for daily life?", "narration": "Training for real, everyday life is a genuinely worthwhile goal on its own."},
], "Strength training pays off far beyond the gym 🏋️\n\nCarrying groceries, stairs, getting off the floor — all draw on functional strength. More valuable as you age, not less.\n\n💚 Bookmark this long-term reminder.\n\n💬 Do you think about strength training for daily life?"),

("hd10_d8_7_heart_health_walking_minutes", [
 {"kind": "hook", "text": "Just 30 minutes of\nwalking a day supports\nreal heart health.", "narration": "Just thirty minutes of walking most days genuinely supports real, measurable heart health.", "query": "person walking heart health outdoor"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "It can help manage\nblood pressure and\ncholesterol over time.", "narration": "Regular walking can genuinely help manage blood pressure and cholesterol levels over months of consistency.", "query": "person walking park health"},
 {"kind": "beat", "kicker": "THE GOOD NEWS", "text": "It doesn't need to\nbe all at once,\nsplitting it up still counts.", "narration": "The good news is it doesn't need to happen all at once, splitting it into shorter walks still counts.", "query": "person walking short break"},
 {"kind": "end", "query": "person walking short break", "text": "Three 10-minute\nwalks work too.", "question": "Do you hit 30 minutes of walking most days?", "narration": "Three separate ten-minute walks genuinely add up to the same benefit."},
], "30 minutes of walking a day supports real heart health ❤️\n\nIt helps manage blood pressure and cholesterol over time. Splitting it into shorter walks still counts fully.\n\n💚 Bookmark this daily heart-health goal.\n\n💬 Do you hit 30 minutes of walking most days?"),

("hd10_d8_8_exercise_consistency_over_intensity", [
 {"kind": "hook", "text": "A moderate workout\nyou actually finish\nbeats a brutal one you dread.", "narration": "A moderate workout you actually complete consistently beats a brutal one you end up dreading and skipping.", "query": "person consistent workout routine"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Consistency compounds\nover months in a way\nintensity alone can't match.", "narration": "Consistency compounds over months in a way that occasional bursts of intensity simply can't match.", "query": "calendar tracking exercise routine"},
 {"kind": "beat", "kicker": "SIMPLE SHIFT", "text": "Pick a level you\ncan repeat, not\njust one you can survive once.", "narration": "Pick an intensity level you can genuinely repeat often, not just barely survive once.", "query": "person sustainable workout pace"},
 {"kind": "end", "query": "person sustainable workout pace", "text": "Sustainable beats\nheroic, every time.", "question": "Do you go too hard and then burn out?", "narration": "Sustainable really does beat heroic, almost every single time."},
], "A workout you finish beats one you dread 🎯\n\nConsistency compounds over months in a way intensity alone can't match. Pick a level you can repeat, not survive once.\n\n💚 Bookmark this before your next routine.\n\n💬 Do you go too hard and then burn out?"),

("hd10_d8_9_mental_health_exercise_prescription", [
 {"kind": "hook", "text": "Some doctors now\nactually prescribe\nexercise for mental health.", "narration": "Some doctors now genuinely prescribe structured exercise as part of treating mild to moderate mental health concerns.", "query": "doctor prescription exercise health"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Studies show it can\nbe comparably effective\nfor some people.", "narration": "Some studies show structured exercise can be comparably effective to other first-line approaches for certain people.", "query": "person exercising mental health"},
 {"kind": "beat", "kicker": "IMPORTANT NOTE", "text": "It's a support tool,\nnot a replacement for\nprofessional care.", "narration": "It's important to note this is a support tool, not a replacement for professional mental health care.", "query": "person support wellness care"},
 {"kind": "end", "query": "person support wellness care", "text": "Movement as\none tool among many.", "question": "Has exercise ever helped your mental health?", "narration": "Movement genuinely works well as one tool among many, not a cure-all on its own."},
], "Some doctors now prescribe exercise for mental health 🩺\n\nStudies show it can be comparably effective for some people, as a support tool alongside professional care.\n\n💚 Bookmark this and share if it might help someone.\n\n💬 Has exercise ever helped your mental health?"),

("hd10_d8_10_flexibility_aging_maintenance", [
 {"kind": "hook", "text": "Flexibility doesn't\nhave to decline sharply\nwith age.", "narration": "Flexibility genuinely doesn't have to decline sharply just because of getting older.", "query": "older person stretching flexible"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Regular, gentle\nstretching can maintain\nrange of motion for decades.", "narration": "Regular, gentle stretching can genuinely help maintain a wide range of motion well into later decades.", "query": "person stretching consistent routine"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "Good mobility helps\nprevent falls and\nkeeps daily tasks easier.", "narration": "Good mobility genuinely helps prevent falls and keeps everyday tasks like reaching and bending much easier.", "query": "person mobile active daily task"},
 {"kind": "end", "query": "person mobile active daily task", "text": "Use it,\ndon't lose it.", "question": "Do you do any regular stretching?", "narration": "Use it consistently, and you genuinely don't lose it as fast."},
], "Flexibility doesn't have to decline sharply with age 🧘\n\nRegular, gentle stretching maintains range of motion for decades and helps prevent falls later in life.\n\n💚 Bookmark this long-term mobility reminder.\n\n💬 Do you do any regular stretching?"),

("hd10_d9_7_cardio_strength_combo_benefits", [
 {"kind": "hook", "text": "You don't have to\nchoose between cardio\nand strength training.", "narration": "You genuinely don't have to choose one lane between cardio and strength training.", "query": "person gym mixed workout"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Combining both in\na week covers more\nhealth markers than either alone.", "narration": "Combining both across a week covers more health markers, heart, muscle, bone, than either one alone.", "query": "person varied gym equipment"},
 {"kind": "beat", "kicker": "SIMPLE STRUCTURE", "text": "Even 2 strength days\nand 2-3 cardio days\ncovers the bases well.", "narration": "Even a simple split of two strength days and two to three cardio days covers the bases quite well.", "query": "weekly workout schedule plan"},
 {"kind": "end", "query": "weekly workout schedule plan", "text": "A mix wins\nover picking just one.", "question": "Do you mix cardio and strength, or stick to one?", "narration": "A genuine mix wins over locking yourself into just one type."},
], "You don't have to choose cardio OR strength 🔀\n\nCombining both across a week covers more health markers than either alone. Even 2 strength + 2-3 cardio days works.\n\n💚 Bookmark this weekly structure idea.\n\n💬 Do you mix cardio and strength, or stick to one?"),

("hd10_d9_8_exercise_habit_formation", [
 {"kind": "hook", "text": "Motivation fades,\nbut a scheduled habit\nsticks around.", "narration": "Motivation reliably fades over time, but a habit tied to a fixed schedule tends to stick around far longer.", "query": "person scheduled workout routine"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Pairing exercise with\nan existing habit\nmakes it easier to start.", "narration": "Pairing a new exercise habit with something you already do daily makes it noticeably easier to actually start.", "query": "person consistent morning routine"},
 {"kind": "beat", "kicker": "EASY EXAMPLE", "text": "Stretching right\nafter brushing your\nteeth is a simple anchor.", "narration": "Stretching right after brushing your teeth every morning is a simple, low-effort anchor to build from.", "query": "morning routine bathroom stretch"},
 {"kind": "end", "query": "morning routine bathroom stretch", "text": "Anchor it to\nsomething you already do.", "question": "Do you anchor habits to existing routines?", "narration": "Anchoring a new habit to something you already do makes it genuinely easier to keep."},
], "Motivation fades, but a scheduled habit sticks 📅\n\nPairing exercise with something you already do daily makes it far easier to start and keep.\n\n💚 Bookmark this habit-building tip.\n\n💬 Do you anchor habits to existing routines?"),

("hd10_d9_9_heart_rate_recovery_fitness", [
 {"kind": "hook", "text": "How fast your heart\nrate drops after exercise\nis a real fitness signal.", "narration": "How quickly your heart rate drops back down after exercise is a genuinely meaningful fitness signal.", "query": "person resting after exercise"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "A faster drop in\nthe first minute\noften means a fitter heart.", "narration": "A faster drop in heart rate during the first minute after stopping often reflects a fitter, more efficient heart.", "query": "person catching breath recovery"},
 {"kind": "beat", "kicker": "HOW TO IMPROVE IT", "text": "Regular cardio\ntraining over weeks\ncan improve this number.", "narration": "Regular, consistent cardio training over weeks can genuinely improve this recovery number over time.", "query": "person cardio training consistent"},
 {"kind": "end", "query": "person cardio training consistent", "text": "A number worth\nwatching improve.", "question": "Have you ever checked your heart rate recovery?", "narration": "A number that's genuinely worth watching improve over time."},
], "How fast your heart rate recovers matters ❤️\n\nA faster drop in the first minute after exercise often means a fitter heart. Regular cardio improves this over weeks.\n\n💚 Bookmark this fitness marker.\n\n💬 Have you ever checked your heart rate recovery?"),

("hd10_d9_10_posture_exercise_core_strength", [
 {"kind": "hook", "text": "A strong core does\nmore than help\nwith 'abs'.", "narration": "A genuinely strong core does far more for you than just visible abdominal muscles.", "query": "person core exercise plank"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "It stabilizes your\nspine during almost\nevery daily movement.", "narration": "Your core stabilizes your spine during nearly every single daily movement, from bending to twisting.", "query": "person bending lifting daily movement"},
 {"kind": "beat", "kicker": "WHY IT MATTERS", "text": "A stronger core\ncan genuinely support\nbetter posture too.", "narration": "A stronger, more stable core can genuinely support noticeably better posture through the day.", "query": "person good posture standing"},
 {"kind": "end", "query": "person good posture standing", "text": "Core strength\nis a posture tool too.", "question": "Do you train your core regularly?", "narration": "Core strength is genuinely a posture tool, not just an aesthetic one."},
], "Your core does more than help with 'abs' 💪\n\nIt stabilizes your spine during nearly every daily movement and genuinely supports better posture.\n\n💚 Bookmark this before your next core workout.\n\n💬 Do you train your core regularly?"),

("hd10_d10_7_rest_day_mental_benefit", [
 {"kind": "hook", "text": "Rest days aren't\njust for your\nmuscles.", "narration": "Rest days aren't just about giving your muscles a break, they matter for your mind too.", "query": "person relaxing rest day mental"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Stepping back from\na strict routine can\nlower mental fatigue too.", "narration": "Stepping back from a strict daily routine can genuinely lower mental fatigue, not just physical fatigue.", "query": "person relaxed calm break"},
 {"kind": "beat", "kicker": "SIMPLE MINDSET", "text": "A rest day is\nprogress too, not\na day off from progress.", "narration": "A rest day is genuinely part of progress, not a pause from it.", "query": "person peaceful rest day"},
 {"kind": "end", "query": "person peaceful rest day", "text": "Rest is\ntraining too.", "question": "Do you feel guilty on rest days?", "narration": "Rest is genuinely part of training, not a break from it."},
], "Rest days aren't just for your muscles 🧠\n\nStepping back from a strict routine lowers mental fatigue too. A rest day is progress, not a pause from it.\n\n💚 Bookmark this for your next rest day.\n\n💬 Do you feel guilty on rest days?"),

("hd10_d10_8_exercise_outdoors_vs_indoors", [
 {"kind": "hook", "text": "The same workout\noutdoors can feel\ncompletely different.", "narration": "The exact same workout done outdoors can genuinely feel completely different from doing it indoors.", "query": "person exercising outdoor nature"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Outdoor exercise is\nlinked to lower\nperceived effort in some studies.", "narration": "Some studies link outdoor exercise to a lower perceived effort, meaning it can genuinely feel easier.", "query": "person running nature trail"},
 {"kind": "beat", "kicker": "ADDED BONUS", "text": "You also get\nnatural light and\nfresh air alongside it.", "narration": "You get the added bonus of natural light and fresh air layered on top of the workout itself.", "query": "person outdoor sunlight exercise"},
 {"kind": "end", "query": "person outdoor sunlight exercise", "text": "Take it outside\nwhen you can.", "question": "Do you prefer outdoor or indoor workouts?", "narration": "Taking it outside when you can is a simple, free upgrade."},
], "The same workout can feel easier outdoors 🌳\n\nSome studies link outdoor exercise to lower perceived effort, plus natural light and fresh air on top.\n\n💚 Bookmark this before your next workout.\n\n💬 Do you prefer outdoor or indoor workouts?"),

("hd10_d10_9_balance_training_importance", [
 {"kind": "hook", "text": "Balance is a\ntrainable skill,\nnot just a fixed trait.", "narration": "Balance is genuinely a trainable skill, not something you simply either have or don't.", "query": "person balance exercise training"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Simple drills like\nstanding on one leg\ncan build it over weeks.", "narration": "Simple drills like standing on one leg for thirty seconds can build real balance over just a few weeks.", "query": "person standing one leg balance"},
 {"kind": "beat", "kicker": "WHY IT MATTERS LONG-TERM", "text": "Better balance lowers\nfall risk, especially\nas you get older.", "narration": "Better balance genuinely lowers fall risk, which becomes more important as the years go on.", "query": "older person balanced stable"},
 {"kind": "end", "query": "older person balanced stable", "text": "A few minutes\na week, real payoff.", "question": "Have you ever tried a balance drill?", "narration": "Just a few minutes a week for a genuinely real long-term payoff."},
], "Balance is trainable, not just a fixed trait ⚖️\n\nStanding on one leg for 30 seconds a few times a week can build real balance and lower fall risk over time.\n\n💚 Bookmark this simple drill.\n\n💬 Have you ever tried a balance drill?"),

("hd10_d10_10_exercise_motivation_environment_design", [
 {"kind": "hook", "text": "Your environment\noften decides whether\nyou work out, not willpower.", "narration": "Your surrounding environment often decides whether you actually work out, far more than raw willpower does.", "query": "person gym bag ready environment"},
 {"kind": "beat", "kicker": "DID YOU KNOW", "text": "Laying out clothes\nthe night before\nlowers the morning barrier.", "narration": "Simply laying out your workout clothes the night before genuinely lowers the barrier the next morning.", "query": "workout clothes laid out night"},
 {"kind": "beat", "kicker": "SIMPLE DESIGN", "text": "Making the healthy\nchoice the easy\nchoice removes decisions.", "narration": "Designing your environment so the healthy choice is also the easy choice removes a lot of daily decision fatigue.", "query": "person organized ready exercise"},
 {"kind": "end", "query": "person organized ready exercise", "text": "Design the path,\nnot just the willpower.", "question": "Do you prep your workout gear the night before?", "narration": "Designing the path ahead of time beats relying on willpower in the moment."},
], "Your environment decides workouts more than willpower 🎽\n\nLaying out clothes the night before lowers the morning barrier. Make the healthy choice the easy choice.\n\n💚 Bookmark this before tonight.\n\n💬 Do you prep your workout gear the night before?"),
]
