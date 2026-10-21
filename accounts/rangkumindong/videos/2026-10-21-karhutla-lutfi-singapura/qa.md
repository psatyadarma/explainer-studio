VERDICT: PASS

QA round 4 of out/video.mp4 (re-rendered 21 Oct 04:27), karhutla / Lutfi / Singapura. Since the round-3 PASS, the only change is that three silent gaps inside "Be En Pe Be" in l1 were shortened (−0.409 s in total, crossfaded), and everything after them moved back by that amount. This round checks the cuts and the shift. The rest of the video was confirmed in rounds 2 and 3.

## Checks
1. Subtitle sync: PASS.
   - Ran `qa_sync.py --lead 0.02`, which matches `window.SUB_LEAD`. build/stt.json's sha256 matches the current voice.wav (e938929a…). It is the round-3 transcript shifted by −0.409 s after the cuts. "speech-to-text: cached (no credits used)".
   - Result: "PASS: median -39 ms, 95% of 202 matched words in [-200, +100] ms, 1% >150 ms late; worst lines: l1b -133 ms, l1 -99 ms, l5b -91 ms, l12b -88 ms, h1 -74 ms".
   - I checked the shift on the audio itself. Cross-correlating the new voice.wav against build/pre-tighten/voice.wav gives a shift of 0 before 11.7 s (corr 1.00). From 14 s to the end it gives exactly 0.409 s at every probe (14, 20, 40, 70 and 85 s; corr 0.93–0.995). So the shifted transcript is valid.
2. Cuts (~11.7–12.5 s): PASS, with no clicks or artifacts.
   - The cuts sit in the gaps at 11.71–11.78, 12.12–12.19 and 12.45–12.51 s. The old gaps were about 0.20 s each. They are now 0.06–0.07 s.
   - A 2 ms peak trace across each gap shows a smooth fade to the usual noise floor (about −60 to −65 dBFS) and back. There are no spikes.
   - High-pass energy in the gaps is not above the old ones: −33, −37 and −48.5 dB, against −34.8, −35 and −48.4 dB before.
   - In the voice track, the highest HF bursts between 10.9 and 13.4 s are consonants: "Oktober" at 11.35 s, the plosive of the last "be" at 12.57 s, and the "c" of "catat" at 13.0 s. None of them is at a cut.
   - The mix shows the same, plus an SFX transient at 11.40 s that comes before the first cut and is unchanged.
3. BNPB clarity: PASS.
   - There are still four separate letter bursts: be 11.48–11.70, en 11.78–12.10, pe 12.19–12.44 and be 12.50–12.76 s. Each is followed by a real silence (below −55 dBFS), and the pace is now a natural spelled-out rhythm.
   - The 0.2 s pause before "catat" (12.78–12.97 s) was kept.
   - Speech-to-text was not re-run on the new audio, to save credits. The letter syllables are unchanged; only the silence between them is shorter.
4. Subtitle highlight for BNPB: PASS.
   - In timing, BNPB runs 11.498–12.881 s, and the spoken word runs 11.48–12.78 s. The highlight is on the word for its whole length (strip frames at 11.3, 11.8, 12.3 and 12.4 s).
   - The "catat" highlight starts at 12.88 s (frame 12.9 s), and the word is spoken at 12.98 s, about 0.1 s early. That is fine.
   - The "7.118" highlight starts at 13.29 s, and "tujuh" is spoken at about 13.41 s.
5. Visuals and beats after the shift: PASS. I checked a new contact sheet (qa-sheet.png) and frame strips at 10.8–15.4, 29.6–32.1, 34.6–37.1, 36.4–38.4, 66.6–69.1 and 86.6–88.6 s.
   - The "BNPB · per 16 Okt" tag is in place.
   - The 7.118 counter starts at about 13.2 s and reaches 7.118 by about 14.1 s, while "tujuh ribu…" is spoken.
   - The l4 timeline shows +3 on "3." and "=10" by 30.6 s.
   - The "BELUM ADA PUTUSAN" stamp is on "Belum" (35.1 s).
   - The Lutfi photo with its credit, followed by the Instagram phone, runs 36.8–38.4 s.
   - The 98 counter is on "98" (67.6 s).
   - The CTA ends with "Komen!".
   - The end card is fully on screen from about 87.4 s, with the logo, tagline, @rangkumindong, sources, photo credits and "Semua pihak yang disebut belum diputus bersalah".
   - Nothing is overlapping, cut off or empty for long.
6. SFX: PASS. I measured the onsets in build/mix.wav after removing the voice:
   - The pop at 30.83 s lands on "10." (about 30.89 s).
   - The thump at 35.03 s lands on "Belum" (about 35.09 s).
   - The pop at 67.45 s lands on "98" (about 67.56 s).
   - All three absolute cues in sfx.json moved by exactly −0.409 s. The whoosh at 2.182 s comes before the cuts, so it did not move. The relative cues follow the timing lines.
7. Numbers: PASS. The text is unchanged (16 Okt, BNPB, 7.118, 6 provinsi, 7 + 3 = 10, 98) and matches draft.md.
8. Audio: PASS. Integrated −15.2 LUFS (inside −14 ±1.5), true peak −1.7 dBTP (limit −1.0), LRA 3.8 LU.
9. Format: PASS. 1080×1920, 30 fps, video 89.267 s and audio 89.258 s (0.009 s apart). The length is 89.27 s, which now leaves 0.73 s under the 90 s limit. The cover frame is unchanged.

## Fixes
None.

## Optional (not counted)
- The pause between "pe" and the final "be" (about 40–60 ms, 12.45–12.51 s) is now the shortest of the three. It still reads as separate letters. Do not tighten it any further.
- The CTA→end-card dissolve at about 87.0 s is the same as in round 3. It is acceptable.
