VERDICT: PASS

QA round 3 of out/video.mp4 (re-rendered 21 Oct 03:53), karhutla / Lutfi / Singapura. Since the round-2 PASS the only change is a re-voiced l1 (BNPB spelled out letter by letter, 1.15x). It was spliced in at +1.076 s, so everything after it moved by the same amount, SFX included. This round checks the splice and the shift. The rest of the video was confirmed in round 2.

## Checks
1. Subtitle sync: PASS.
   - Ran `qa_sync.py --lead 0.02`, which matches `window.SUB_LEAD`. The voice.wav SHA-256 matches build/stt.json, which is the shifted old transcript plus a fresh transcript of l1. No new credits were used.
   - Result: "PASS: median -39 ms, 95% of 202 matched words in [-200, +100] ms, 1% >150 ms late; worst lines: l1b -133 ms, l1 -99 ms, l5b -91 ms, l12b -88 ms, h1 -74 ms".
   - l1 detail: the only outlier is "7.118" at -359 ms. A waveform/spectral check shows that "tujuh" actually starts at about 13.82 s. The transcript's 14.04 s is late, so the real highlight lead is about 0.14 s early. That is fine.
   - BNPB: the highlight starts at 11.48 s. Speech-to-text puts the word at 11.50–13.16 s.
   - catat: highlight at 13.27 s, speech at about 13.38 s.
   - Every highlight is either on the word or slightly early, which reads as in sync.
2. BNPB clarity: PASS.
   - Speech-to-text on the fresh clip transcribes it as "BNPB".
   - The waveform shows four separate syllables, "be / en / pe / be" (about 11.5, 11.92, 12.46 and 12.92 s), with silences of about 0.2 s between the last three.
   - The subtitle reads "BNPB · per 16 Okt", spelled correctly.
3. Visuals after the shift: PASS. I checked a new contact sheet (qa-sheet.png) and frame strips at 10.6–16.3, 26.0–32.2, 35.3–38.6, 63.5–70.6 and 82.5–89.6 s. Every beat still lands on its word:
   - The "BNPB · per 16 Okt" tag lands on "16".
   - The 7.118 counter runs about 13.6–14.7 s, as "tujuh ribu…" is spoken.
   - The fire icons and the "di 6 provinsi" tag land on l1b.
   - The "Kata Singapura" avatar keeps its credit visible at 26.0 s.
   - The l4 timeline (16 Okt → 7, 19 Okt → +3) lands on its words, and "=10" is on screen by 31.15 s with the spoken "10" at 31.3 s.
   - The "BELUM ADA PUTUSAN" stamp lands on "Belum" (35.5 s).
   - The Lutfi / Instagram scene runs about 37.2–38.6 s.
   - The "?" with "tanggapan belum ditemukan" shows on l12b.
   - The 98 counter lands on "98" (68 s).
   - The CTA options appear in order with "Komen!".
   - Nothing is overlapping, cut off or empty for long.
4. SFX: PASS. The three absolute cues moved by +1.076 s, and the relative cues follow their lines:
   - The pop at 31.25 s lands on "10." (31.30 s).
   - The thump at 35.449 s lands on "Belum" (35.50 s).
   - The pop at 67.866 s lands on "98" (67.97 s).
   - The whoosh at 2.182 s comes before the splice, so it did not move.
5. Numbers: PASS. The l1 text is the same as before: 16 Okt, BNPB, 7.118, 6 provinsi, all matching draft.md. No other text changed.
6. Audio: PASS. Integrated -15.2 LUFS (inside -14 ±1.5), true peak -1.6 dBTP (limit -1.0), LRA 3.6 LU.
7. Format: PASS. 1080×1920, 30 fps, video 89.667 s and audio 89.687 s (0.02 s apart). The length is 89.69 s, which is under 90 s but only 0.31 s inside the limit. The cover frame is unchanged.
8. End card: PASS. It is fully on screen from about 87.6 s to 89.69 s, with the logo, the tagline "Berita ribet? Rangkumin dong.", @rangkumindong, the sources, both photo credits and "Semua pihak yang disebut belum diputus bersalah". The end ding is on the "end" line.

## Fixes
None.

## Optional (not counted)
- The first "be" of BNPB runs straight on from "Oktober" (no gap at about 11.2–11.7 s), while the other three letters have clear pauses. It is still understandable, and speech-to-text heard "BNPB", but its confidence was lower than for other words (logprob -0.63). A short pause after "Oktober," would make it crisper. Re-voicing l1 would cost credits, and any added time must keep the total ≤ 90 s, which leaves only about 0.3 s.
- At about 87.3–87.6 s, the dissolve from the CTA into the end card briefly ghosts the "Follow Rangkumin Dong" subtitle. This is the same dissolve as in round 2, just shifted, and is acceptable.
