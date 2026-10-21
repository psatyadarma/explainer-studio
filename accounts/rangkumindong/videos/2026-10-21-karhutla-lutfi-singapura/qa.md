VERDICT: PASS

QA round 5 of out/video.mp4 (re-rendered 21 Oct 04:44), karhutla / Lutfi / Singapura. Since the round-4 PASS, the only change is in l1 audio. A room-tone pause was inserted before "Be", and "Be En Pe Be" was sped up 1.3x with pitch preserved. Everything after moved earlier. This round checks the edit, the shift, and the length mismatch. The rest of the video was confirmed in rounds 2–4.

## Checks
1. Subtitle sync: PASS.
   - Ran `qa_sync.py --lead 0.02`, which matches `window.SUB_LEAD`. build/stt.json's sha256 matches the current voice.wav (54dc419f…). It is a composite: the cached words were shifted, and only 10.4–13.4 s was re-transcribed. The tool reported "speech-to-text: cached (no credits used)".
   - Result: "PASS: median -39 ms, 95% of 201 matched words in [-200, +100] ms, 1% >150 ms late; worst lines: l1b -133 ms, l1 -107 ms, l5b -91 ms, l12b -88 ms, h1 -74 ms".
2. Shift: PASS.
   - I cross-correlated voice.wav against build/pre-gap/voice.wav. The shift is 0 up to about 11.4 s (corr 0.99–1.00). From 13 s to 88 s it is −0.1173 s at every probe (corr 1.00).
   - timing.json and the absolute sfx.json cues moved by −0.111 s. That is 6 ms less than the audio moved, which is negligible.
   - The voice length dropped from 89.278 s to 89.161 s.
3. Edit artifacts (11.4–12.7 s): PASS. There are no clicks and no processed sound.
   - **Splice in (11.474 s):** this is where "Oktober" ends. There is a fade of about 12 ms (−26 → −33 → −55 dBFS 2 ms peaks), with no step. In the old take, "Oktober" ran straight into "be", so the cut sits on the word boundary.
   - **Pause:** 11.48–11.66 s (about 0.19 s), at −54 to −60 dBFS peaks. The room tone is a looped snippet of about 58 ms taken from the post-BNPB pause. It is about 2–3 dB hotter than the other pauses (mostly below 300 Hz).
   - **Pause in the final mix:** the music bed under the pause is about −31 dB RMS, so the loop and the level step can't be heard.
   - **Splice out (11.664 s):** "be" starts cleanly with its voicing bar.
   - **Second-difference click scan (10.9–13.3 s):** the largest value is 116× the median. All the large values are at 10.98 s, which is unedited speech. The whole-file p99.99 is 258×, so nothing stands out.
   - **Stretch quality:**
     - The spectrogram shows clean harmonics with no smearing or phasiness.
     - Pitch was compared on the time-aligned letters (new vs old): 90.9/90.2, 110/109, 103/103, 177/179, 107/105 Hz, so pitch is preserved.
     - The spectral centroid barely moved (2082 vs 2130 Hz).
   - **Letter separation:** the gaps between letters are now only about 30–40 ms. The fresh speech-to-text still hears four separate letters: B 11.68, N 12.02, P 12.22, B 12.52.
   - **Pause before "catat":** 12.68–12.86 s, about 0.18 s, kept.
4. BNPB highlight: PASS.
   - In timing, BNPB runs 11.675–12.670 s, and the letters are spoken 11.66–12.66 s.
   - In frames, "Oktober," is highlighted at 11.40 s. BNPB is highlighted at 11.65, 11.70, 12.20 and 12.60 s. "catat" is highlighted at 12.75 and 12.80 s; the word is spoken at about 12.86 s, so the highlight is about 0.1 s early, the same as before.
   - "7.118" is highlighted from 13.18 s and "tujuh" starts at about 13.30 s. The counter reads 2.115 at 13.2 s and 7.118 at 14.2 s.
5. Later beats and SFX: PASS.
   - **Frames:**
     - "=10" and "+3" are on the timeline by 30.70 s, with "10." highlighted at 30.85 s.
     - The "BELUM ADA PUTUSAN" stamp lands at 35.10 s, on "Belum".
     - The Lutfi photo with its credit, then the Instagram phone, appear at 36.80 and 38.00 s.
     - The 98 counter starts at 67.35 s, when "98" is spoken (about 67.37 s).
     - The end card is complete at 87.50 s and is the last frame (89.03 s).
   - **SFX onsets measured in mix.wav:**
     - whoosh at 2.18 s (unedited part)
     - thump at 34.93 s, before "Belum" (35.08 s); same spacing as in round 4
     - pop at 67.345 s, on "98"
     - pop cue at 30.73 s, before "se-puluh" (30.84 s)
   - All of these kept their round-4 relation within 6 ms. The new contact sheet (qa-sheet.png) shows nothing overlapping, cut off or empty.
6. Numbers: PASS. The text is unchanged (16 Okt, BNPB, 7.118, 6 provinsi, 7 + 3 = 10, 98) and matches draft.md.
7. Audio: PASS. Integrated −15.2 LUFS, true peak −1.5 dBTP (limit −1.0), LRA 3.7 LU.
8. Format and length: PASS.
   - 1080×1920 at 30 fps. The container is 89.161 s, under the 90 s limit.
   - The video stream is 89.067 s (2672 frames) and the audio stream is 89.161 s. They are 0.094 s apart, which is inside the spec's ±0.1 s.
   - The tail is **not cut**. The audio runs its full length (89.161 s, the same as mix.wav).
   - The last 0.094 s of audio is the end of the ding fading out (−58 to −77 dB RMS), and players keep showing the last frame (the end card) over it.
   - Why the video is short: `render.mjs` muxes with `-shortest` and `-c:v copy`. That dropped the last 3 frames of video.silent.mp4 (2675 frames, 89.167 s). Those 3 frames were identical end-card frames.
   - The cover frame is the same as the silent render's (md5 match).

## Fixes
None.

## Optional (not counted)
- The video vs audio gap of 0.094 s is inside the spec, but it is above the coordinator's ~0.05 s target. To close it, mux without `-shortest`, or with `-t 89.161`, so all 2675 frames are kept (89.167 s video vs 89.161 s audio).
- The room-tone loop in the BNPB pause is 2–3 dB hotter than the natural pauses. It is masked in the mix. If the voice is ever used without the music bed, take one longer room-tone piece without a loop and lower it by about 3 dB.
- With 1.3x, the gaps between the letters are about 30–40 ms. Do not speed this up any further.
