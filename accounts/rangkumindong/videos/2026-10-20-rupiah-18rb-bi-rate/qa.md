VERDICT: PASS

This re-check covers out/video.mp4 (render 20 Okt 00:32), made after the l10 hold fix and the two nits. The voice is unchanged: voice.wav's SHA-256 matches build/stt.json. So the check used the cached transcript, and no speech-to-text credits were spent. Every fix from earlier rounds is confirmed.

## Checks
1. **Subtitle sync:** PASS.
   - Command: `qa_sync.py --lead 0.02` (this matches `window.SUB_LEAD`) on the cached transcript.
   - Result line: "PASS: median -78 ms (positive = highlight late), 95% of 130 matched words in [-200, +100] ms, 0% >150 ms late; worst lines: l3b +149 ms, l9 -108 ms, l7 -94 ms, l8 -90 ms, l6 -89 ms".
   - The timing words are unchanged, so the l3b number is the same as last time. It comes from one word ("Covid") and is under the limit.
   - Stills at 26.0, 26.2 and 26.4 s show the page flip now happens on the first word. At 26.2 s, "Covid" is the highlighted word on the new page.
   - l11b and l11c also flip on their first word, at 70.6 s and 73.5 s.
2. **Visuals:** OK. Files: qa-sheet.png and qa-safezone.png (stills at 26–29 s, 59.5–76.5 s and the chart).
   - **l10 (59–66 s):** the 6.3 s hold is gone. The beats now come at:
     - about 59.0 s: the card pops in;
     - 60.1 s: "5,75%" pulses;
     - 62.8 s: the "sebagian ekonom, mis. Danamon" highlight appears and stays through "intervensi";
     - 65.4 s: the shield and the "intervensi" chip appear.
   - **Gaps between beats:** the longest is now about 2.7 s, from 60.1 to 62.8 s.
   - **freezedetect:** at its loose threshold it still reports low motion over 60.2–65.6 s. The stills show the highlight change, but it is too small for the filter to count.
   - **Opsi 2 (66–77 s):** the up-arrow, the Bloomberg highlight and the "saham → obligasi" chip come in on their words. Both sides keep equal weight.
   - **Chart:** the "18.170" label is now clear of the dashed 18.000 line. The stickers, the values to the right of the dots and the earlier beats are all still in place.
   - **Safe zones:** nothing sits in the shaded zones, and no subtitle runs past 3 lines.
3. **Numbers:** OK and unchanged against draft.md and post.json: Rp18.046, 18.049, ≈16.800, 16.575, 18.170, 5,25/5,50/5,75%, 6%, 10 hari, US$146,3 M, 3,28%, and Rabu 21 Okt.
4. **Audio:** OK. Integrated loudness is -14.2 LUFS and true peak is -3.7 dBTP.
5. **Format:** OK. 1080×1920 at 30 fps. Video runs 88.000 s and audio 88.050 s, a gap of 0.05 s. The cover frame is readable.
6. **Must-haves:** OK.
   - The disclaimer appears in the header pill and again on the end card at 32 px.
   - The "Rangkumin dong!" tagline plays at 9.0–10.4 s.
   - The end card shows @rangkumindong and the sources.
   - No PART badge is needed.

## Fixes
None.
