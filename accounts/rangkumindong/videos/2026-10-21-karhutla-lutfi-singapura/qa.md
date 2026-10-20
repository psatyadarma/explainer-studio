VERDICT: PASS

QA round 2 of out/video.mp4 (re-rendered 20 Oct 23:37), karhutla / Lutfi / Singapura. Both round-1 fixes are confirmed. Both optional items are done.

## Round-1 fixes
- Fix 1, true peak: FIXED. Now -1.5 dBTP (limit is -1.0); it was -0.6 dBTP.
- Fix 2, Grace Fu credit gap: FIXED. Frames 25.0–25.9 s at 10 fps: the credit stays on screen through about 25.7 s. The "Kata Singapura" avatar has gone by then and the timeline pan has taken over. There is no frame where the avatar shows without its credit. index.html line 615 now reads `t < at('l4', 0.3)`.
- Optional "=10": DONE. It pops at about 29.9 s, on "Jadi", and stays readable until the l5 pan at about 31.3 s (about 1.4 s, up from 0.8 s). It sits inside the safe area at x ≈ 700–890.
- Optional end-card credit wrap: DONE. It now wraps cleanly into 3 lines: "Foto: Kementerian Perdagangan RI (domain publik);" / "Lukasz Kobus / European Union, CC BY 4.0 (dipotong & diedit)," / "via Wikimedia Commons".

## Checks
1. Subtitle sync: PASS. Ran `qa_sync.py --lead 0.02` on the cached transcript. The lead matches `window.SUB_LEAD = 0.02` in index.html, the voice.wav SHA-256 matches build/stt.json, and no credits were used. Result: "PASS: median -39 ms (positive = highlight late), 94% of 200 matched words in [-200, +100] ms, 2% >150 ms late; worst lines: l1b -103 ms, l5b -91 ms, l12b -88 ms, h1 -74 ms, l1 -72 ms". Round 1 reported -99 ms because it used the default lead of 0.08. The voice track is the same.
2. Visuals: PASS. Checked the contact sheet (`qa-sheet.png`), 34 full-size stills at line starts, and frame strips at 7.8–11.2, 25.0–25.9, 29.7–31.5, 35.4–38.8, 79.8–83.2 and 85.6–88.8 s.
   - Settled frames have no overlapping or cut-off text.
   - The longest near-empty frames are about 0.3–0.4 s (around 9.6, 36.0 and 38.3 s), well under the 2 s limit.
   - No visual is held over 4 s.
   - Safezone (`qa-safezone.png`, the 34 line-start stills): nothing important sits in the shaded zones once a frame settles. Partial elements at the frame edge appear only mid-pan, during zone camera moves.
   - Cover: "10 perusahaan Indonesia" plus "disurati Singapura soal asap" is readable at thumbnail size.
   - Brief cross-dissolve ghosts appear at 16.1–16.5 s (7.118 into the Bromo card) and at about 86.2–86.5 s (CTA into the end card). Both are acceptable.
3. Numbers: PASS. On screen: 10, 7.118, "BNPB · per 16 Okt", 6 provinsi, 4 orang, 16 Okt / 7 perusahaan, 19 Okt / +3, =10, 4 dari 7, 19 Okt, 10 perusahaan, 98. All of them are spoken and match draft.md and post.json. The new labels "Sumatra", "Kalimantan" and "disurati NEA · belum ada putusan" follow the draft's visual spec and contain no numbers.
4. Audio: PASS. Integrated -15.2 LUFS (inside -14 ±1.5), true peak -1.5 dBTP (limit -1.0), LRA 3.5 LU.
5. Format: PASS. 1080×1920, 30 fps, 88.80 s (inside 60–90 s). Video 88.800 s vs audio 88.789 s, a 0.011 s difference.
6. Must-haves: PASS.
   - Licences: accounts/rangkumindong/assets/people/muhammad-lutfi.json is public domain; grace-fu.json is CC BY 4.0.
   - On-screen credits: they show while each photo is visible, during the hook face-off, the Grace Fu avatar (until about 25.7 s) and the Lutfi Instagram scene (about 36.1–38.2 s).
   - End card: it has the handle, the sources, both credits and "Semua pihak yang disebut belum diputus bersalah".
   - Post captions: they carry the credits.
   - Tagline: it appears at the rd beat and on the end card.
   - Not needed: a market disclaimer (not a stock topic) and a PART badge (new storyline).

## Fixes
None.

## Optional (not counted)
- The end-card voice line ("Follow Rangkumin Dong, biar nggak ketinggalan!", 86.4–88.1 s) has no subtitle, because the end card replaces the subtitle area. This is fine if that is the house style; it was the same in round 1.
