# Playbook — Rangkumin Dong

## Brand
- Name: Rangkumin Dong · Tagline: "Berita ribet? Rangkumin dong."
- Handles: IG @rangkumindong · TikTok @rangkumindong · YouTube "Rangkumin Dong!" (@RangkuminDong-d2m)
- Audience: Indonesians who want the gist of business/market/tech/politics news, fast.
- Language: Bahasa Indonesia, casual but accurate.

## Format
- 60–90 s, 1080×1920, 30 fps. Sticker Explainer style (mg-styles-15 #07, MIT): cut-out stickers with white outline, flat icons, exact charts, one moving camera between zones, counters, word-highlight subtitles.
- Colours: paper #F3EFE6 · ink #1B2430 · slate #3E5568 · accent #FF5A36 · highlight #FFD23F.
- Structure: hook (shock number or question, first frame must work as a cover) → fixed tagline "Rangkumin dong!" → 4–8 beats → "what happens next" → vote CTA ("Tim A atau Tim B? Komen!") → end card with sources.
- New visual every 2–4 s. Safe area: keep content above y≈1300 and away from the right 170 px (platform UI).
- Always show "Bukan ajakan jual/beli saham" on market/stock topics.

## Script & delivery ("punchy", approved 19 Oct)
- Conversational, explaining to a friend. Short sentences. Openers like "Jadi gini.", "Pemicunya? X.", "Nah,", "Tapi tenang,".
- Dramatic beat on the key number ("Dalam. Satu. Hari.").
- Every number on screen is spoken; every claim tied to a source.
- Per-line ElevenLabs v3 tags (shocked / serious / skeptical / reassuring / playful). Numbers and acronyms spelled out in `say` ("em es si ai", "sebelas koma lima tujuh").
- Pauses capped at 0.24 s; target ~150–170 spoken wpm.
- Voice A/B: male Pratama vs female Cahaya, 7-day blocks. Taglines are fixed recordings in `assets/voice/`.

## Continuity (videos build on each other)
- Before picking topics, check `storylines/` for active stories with new developments or milestones due.
- Follow-up videos: hook references the last episode ("Minggu lalu IHSG anjlok 11%. Sekarang…"), show a small "PART n" badge, reuse the same chart/visual language, and link the previous video in the pinned comment.
- Each video ends a storyline file update: new facts + sources, link to the video, next milestone.

## Fact-check & sensitive topics
- 2+ independent sources per claim; prefer originals (BPS, BI, OJK, IDX, ministries, company filings, MSCI etc.).
- Re-check fast-moving numbers right before rendering; log any change from the approved draft.
- Politics: neutral, what happened / what each side says / why it matters. No allegations without official sources, no opinions, no party colours.
- Never invent data points for charts; plot only verified values.

## Approval & posting
- User approves topic + script + style before any render. User gives "OK post" before anything is published.
- Posting via Upload-Post (engine/post.py, profile "Rangkumindong"): IG Reels + YouTube Shorts (#Shorts in title). TikTok: user warms the account up manually until 24 Oct 2026, then connect it to Upload-Post (AI-generated label on). Pin a sources comment.
- A/B post-time test: 12:00–13:00 WITA vs 19:00–21:00 WITA, 14-day blocks.
