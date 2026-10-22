VERDICT: PASS

QA round 3, 22 Okt 2026 · out/video.mp4 (re-render 10:52, person cut-outs of Luhut, Setyo and Yusril added) · voice and mix unchanged (same take as rounds 1–2)

1. Subtitle sync: PASS: median -75 ms, 92% of 153 matched words in [-200, +100] ms, 1% >150 ms late; worst lines: l4b -164, l4 -125, l2b -108 ms (lead 0.02; speech-to-text cached, no credits used). Identical to round 2. Tool note: running `engine/qa_sync.py` without `--lead` used 0.08 and gave FIX at -135 ms. It does not read `window.SUB_LEAD` from index.html, even though the agent doc says it does. Always pass `--lead 0.02` for this video, or fix the script.
2. Visuals: OK.
   - Cut-outs: there is no leftover background. The silhouettes are clean, and faces keep their aspect ratio (width is auto, height is 0.8 × natural), so nothing is distorted.
   - Size and treatment are equal. Rendered heights are 450, 449 and 463 px, head sizes look the same, all three use the same white sticker border, ledge, rise-from-ledge motion, name tag and credit line, and all are centred in their zone.
   - Safe area: OK on stills at 0, 12, 43.5, 64.5, 75 and 85.5 s (qa-safezone sheet). Photos, tags and credits all sit inside the 3:4 crop and clear of the shaded zones.
   - Cover (t=0) is unchanged and has no photo. The hook is readable.
   - Regressions: none. The "sejak 2026" sticker badge (d2026) is still absent; only the planned small "sejak 2026 · dulu UU Tipikor" book subtitle remains, as accepted in round 2. The rest of the contact sheet matches round 2.
3. Numbers: OK, unchanged. The "(Pasal 3 ayat 2)" footnote is still gone (not in index.html, and the box reads "kerugian negara tidak disyaratkan").
4. Audio: OK. -14.2 LUFS, -3.7 dBTP, LRA 2.3 (same as round 2).
5. Format: OK. 1080×1920, 30 fps, 88.23 s video against 88.20 s audio.
6. Must-haves: OK.
   - Each of the three PNGs has an `assets/people/<slug>.json` with an allowed licence: Luhut public domain, Yusril public domain, Setyo CC BY-SA 4.0.
   - On-screen credit shows while each photo is visible (Luhut 10.0–23.2 s and 64.4–66.1 s, Setyo 43.0–45.7 s, Yusril 72.8–76.8 s). The text matches the json `credit`/`author`; the ministry names are shortened to "Kemenko Marves RI" and "Kemenko Kumham Imipas RI", the same way as the earlier muhammad-lutfi precedent.
   - Setyo carries "CC BY-SA 4.0 (dipotong & diedit)", as the share-alike licence requires.
   - Credits also appear on the end card and in the post.json caption, and post.json `photo_credits` matches all three json files (file, page, author, licence).

Credit flicker during pans: OK, not flagged. I checked every frame of the credit band (y 1200–1340). Credit text overlaps sliding content for at most 3 frames (72.83–72.90 s, where the Yusril credit crosses "pembuktian diperjelas" and "(kata Luhut)" during the whip-pan) and for 1 frame at 43.03 s (Setyo credit against the name tag). That is too short to read as overlapping text, and the credits never stack two lines.

## Optional polish (not blocking)
- Luhut cut-out (`assets/people/luhut-binsar-pandjaitan.png`): small white specks and a slightly chewed hair edge at both temples (about x 120 and x 400, y 120–160 in the PNG). Visible only when zoomed in; invisible on a phone. If re-cut, feather the mask at the hair.
- Setyo cut-out: a faint tan fringe from the original background sits inside the white border around the hair top and right shoulder. It is not visible at playback size, but a 1–2 px mask erode would clean it.
- Setyo is the only candid shot (speaking into a mic, looking off-camera), while Luhut and Yusril are smiling official portraits. Size and framing are equal, and the json notes the official KPK portrait could not be downloaded (Commons 429). Swap in `File:Ketua KPK RI Setyo Budiyanto.jpg` if it becomes downloadable, for fully matched treatment.
