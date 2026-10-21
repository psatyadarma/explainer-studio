# Playbook — Ajarin Dong

Sibling of Rangkumin Dong. Same engine, sticker style, voices and quality rules (read `accounts/rangkumindong/knowledge/playbook.md` for script & delivery, safe area, real-person cut-outs, fact-checking and approval). What differs is below.

## Brand
- Ajarin Dong! · @ajarindong.id (IG, TikTok, YouTube) · Tagline: "Bingung? Ajarin dong!" (fixed recordings in `assets/voice/`, take A for both voices).
- Accent blue #2F5BEA (instead of Rangkumin's orange), yellow highlight #FFD23F, same paper/ink. Badge "AJARIN DONG" top-left instead of "Rangkumin Dong".
- Audience: people who see a term in the news and don't get it.

## Format (evergreen, 60–90 s)
1. **Question hook** (0–2 s): "Apa sih MSCI itu?" / "Kenapa rupiah bisa melemah?", with the term big on screen.
2. Tagline "Bingung? Ajarin dong!".
3. **One everyday analogy** (warung, arisan, ojol, kos-kosan…). One only, carried through the video.
4. **3 simple steps** that explain how it works, each with one visual.
5. **"Kenapa ini muncul di berita?"**: one line connecting to the current news, pointing to the Rangkumin video ("cek @rangkumindong").
6. CTA: "Mau dijelasin istilah apa lagi? Komen!" + follow both.
- Evergreen: avoid numbers that go stale; when a number is needed, say "per Oktober 2026".
- Accuracy over simplicity: the analogy must not be wrong. The fact-checker checks definitions against an authoritative source (BI, OJK, IDX/BEI, BPS, Kemenkeu, MSCI, textbooks).

## Topics
- Source: `knowledge/concepts.csv`, a backlog of concepts behind Rangkumin's news (events DB + storylines), plus questions from comments on both accounts.
- Score each concept: **in the news now** (0–2), **confusing to normal people** (0–2), **affects daily life** (0–2), **visual/analogy potential** (0–2), **evergreen** (0–2). Total /10.
- Covered log: `knowledge/covered.csv` (same tool: `engine/covered.py`).

## Weekly batch (Mondays)
- Monday ~07:00 WITA: a session offers 5 ranked concepts (+ runner-ups) for the week. The user picks 3 (Mon/Wed/Fri).
- Drafts (script, visual plan, captions) for all 3 go out together for approval. After approval: render → QA → MP4s plus captions → "OK post" → scheduled 19:00 WITA on Mon/Wed/Fri via Upload-Post profile "Ajarindong".
- TikTok: the user posts manually during warm-up, so send a TikTok caption (max 5 hashtags, incl. #ajarindong).

## Captions
- Hook line + 3-bullet summary + question CTA + "Follow @rangkumindong buat berita terbarunya" + 5–7 hashtags incl. #ajarindong #belajarekonomi.
