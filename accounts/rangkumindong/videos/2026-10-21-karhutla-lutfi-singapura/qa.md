VERDICT: PASS

QA round 6 of out/video.mp4 (re-rendered 21 Oct 06:17), karhutla / Lutfi / Singapura. Three things changed since the round-5 PASS:
- "Be En Pe Be" was redone at 1.45x with a pause of about 200 ms before it. Everything after it moved −0.208 s compared with round 4.
- A 30 ms "HF glitch" at about 20.29 s was low-passed.
- render.mjs now muxes with `-t` set to the audio length.

The cached transcript was used. No credits were spent. I can't actually listen, so the intelligibility judgements below come from envelope, spectrum, voicing and f0 analysis.

## Checks
1. Subtitle sync: PASS.
   - build/stt.json sha256 matches voice.wav (0dd35972…). It is a composite: cached words shifted, plus a fresh speech-to-text pass over 10.4–13.4 s.
   - Ran `qa_sync.py --lead 0.02` (= window.SUB_LEAD): "PASS: median -39 ms, 95% of 201 matched words in [-200, +100] ms, 1% >150 ms late; worst lines: l1b -133 ms, l1 -107 ms, l5b -91 ms, l12b -88 ms, h1 -74 ms". This is the same as round 5.
   - Note: run without `--lead`, the tool does not pick up SUB_LEAD. It falls back to 0.08 and reports a median of −99 ms. It is still PASS that way.
2. Shift: PASS.
   - I cross-correlated voice.wav against build/pre-gap/voice.wav (round 4). The shift is 0 up to 11.4 s. From 13 s to 87 s it is −0.2141 s at every probe (corr 1.00).
   - timing.json line starts and the absolute sfx.json cues moved by −0.208 s. That is 6 ms less than the audio moved, the same leftover as in round 5, and negligible.
   - Voice length went from 89.278 s to 89.064 s.
3. BNPB intelligibility: PASS. The speech-to-text token "B. NP. B" only shows that there is no pause between "en" and "pe". In the acoustics, all 4 letters are separate:
   - **B** (11.665–11.84): a voicing bar before the release, then [e].
   - **Silence** (11.84–11.865): about 25 ms.
   - **E-N** (11.865–12.115):
     - The [ɛ] vowel runs about 115 ms, with strong 0.4–2.5 kHz energy.
     - The **N** follows as about 120 ms of voiced nasal murmur (12.0–12.11). Its centroid is about 170 Hz, the mid band is 15–20 dB below the vowel, it is fully voiced (v 0.6–0.7), and f0 rises from 104 to 185 Hz.
   - **P** (12.115–12.30):
     - Its closure is about 30 ms of silence (−65 to −70 dB, 12.115–12.142).
     - It releases with a sharp broadband burst at 12.145 s (centroid 3.1 kHz) and **no voicing bar**, then the [e] vowel.
   - **B** (12.31–12.56):
     - A short dip, then a voicing bar (12.375–12.405), then the burst at 12.41 and [e].
   - **N vs P:** these are clearly distinguishable (nasal murmur vs silent closure + burst).
   - **P vs B:** these are separated by voicing before the release.
   - **Overall:** the 4 letters take about 0.9 s (about 225 ms each), which is a normal speed for spelling out an acronym. The intonation is natural (f0 90/110/104→185/155→90/130→100 Hz). Do not speed this up any further.
4. Clicks at the edits: PASS.
   - The splice into the pause at 11.47 s fades out "Oktober" smoothly (−24 → −44 → −63 dB over about 15 ms).
   - The pause runs 11.475–11.660 s (about 0.185 s). It is the 60 ms room-tone loop at −63 to −68 dB, covered by the music in the mix.
   - The splice out at 11.66 s runs straight into the voicing bar of "B".
   - A second-difference scan of 11.3–12.95 s gives a maximum of 77× the median in voice.wav and 93× in mix.wav. The whole-file p99.99 is 252× and 184×, so there are no clicks.
5. 20.29 s: no click (PASS). However, the low-passed part was the first half of the /s/ in "Asapnya", not a separate glitch. See Optional 1.
   - **Before the low-pass:** the /s/ ran smoothly from 20.283 to 20.345 s.
     - It was 62 ms long, peaking at 8–12 kHz with a 4 ms onset ramp.
     - The spectrum of 20.29–20.305 matches 20.315–20.335 exactly. There is no separate impulse.
     - It is a hot sibilant (HF rms −14 dB). Only "asap." at 3.62 s (−10.6 dB) is hotter, and that one has passed 5 rounds.
   - **Now:**
     - The HF from 20.272 to 20.310 is cut to −99 dB.
     - The /s/ restarts at 20.311 s and lasts 35 ms. It keeps the same hot level as before, so if the harshness was the complaint, it is still there.
     - In the final mix the music fills the HF hole (about −47 dB). The s onset is a rise of about 30 dB in 2–3 ms, close to the original's 27 dB in 4 ms, so it does not read as a click.
     - "Asapnya" keeps its /s/. The highlight is on "Asapnya" at 20.30 s.
6. Later beats and SFX: PASS.
   - **SFX onsets in mix.wav:**
     - pop at 30.63 s, about 90–110 ms before "se-puluh", as before
     - thump at 34.832 s, about 150 ms before "Belum", as before
     - pop at 67.249 s, about 25 ms before "98", as before
   - **Frames:**
     - BNPB is highlighted at 11.70, 12.00, 12.20 and 12.50 s. "catat" is highlighted at 12.80 s, with the word starting at about 12.79 s.
     - "=10" appears with "10." highlighted at 30.75 s.
     - The "BELUM ADA PUTUSAN" stamp is on "Belum" at 34.95 s.
     - The Kapolri counter is running at 67.30 s.
     - The end card is complete at 89.03 s.
   - The new qa-sheet.png shows nothing overlapping, cut off or empty.
7. Numbers: PASS. The text is unchanged (16 Okt, BNPB, 7.118, 6 provinsi, 7 + 3 = 10, 98).
8. Audio: PASS. Integrated −15.2 LUFS, true peak −1.7 dBTP, LRA 3.8 LU.
9. Format and length: PASS.
   - 1080×1920 at 30 fps.
   - Video is 89.067 s (2672 frames, the same count as video.silent.mp4) and audio is 89.064 s. The gap is **3 ms**, down from 94 ms.
   - mix.wav is 89.064 s, so no audio is lost. The tail rms is −55 dB in both mix.wav and the mp4, so the ding tail is intact.
   - Total length is under 90 s.
10. Must-haves: unchanged since round 4 (credits, end card with sources and handle, disclaimer).

## Fixes
None.

## Optional (not counted)
1. **20.29 s /s/:** the "glitch" fix removed the front 30 ms of a real /s/. It left a shorter, gated /s/ at the same hot level.
   - The cleaner fix is to restore 20.27–20.31 from build/pre-gap/voice-before-declick.wav. Then de-ess the whole /s/ (20.283–20.345) with about a −6 dB high shelf above 5 kHz and 5 ms crossfades.
   - Ideally, do the same to "asap." at 3.62 s.
   - The result is not audible as a click in the mix, so this is optional.
2. **qa_sync.py:** without `--lead`, it does not read `window.SUB_LEAD` from this index.html and falls back to 0.08. Pass `--lead 0.02` explicitly, or fix the parser.
