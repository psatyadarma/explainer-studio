VERDICT: PASS

QA round 2, 22 Okt 2026 · out/video.mp4 (re-rendered 01:09) · voice build/voice.wav sha e8a4573f… (same take as round 1: 1.15x, l5 cut, h2 pre-gap, mix with --deess)

1. Subtitle sync: PASS: median -75 ms (positive = highlight late), 92% of 153 matched words in [-200, +100] ms, 1% >150 ms late; worst lines: l4b -164 ms, l4 -125 ms, l2b -108 ms, l4c -96 ms, l6b -92 ms. (lead 0.02; speech-to-text cached, no credits used.)
2. Visuals: OK. The "sejak 2026" badge is gone, and the "KUHP baru" title is fully readable at 29–42 s (stills at 25, 27 … 45 s, plus 34 s and 41.8 s full size). A fresh contact sheet (qa-sheet.png) shows the rest of the video unchanged from round 1. Notes carried over, not flagged: whip-pans show the neighbouring zone for about 0.4 s at line changes (house style), and the donut hold at 53–57 s is 4.0 s, which is borderline but not over.
3. Numbers: OK. The "(Pasal 3 ayat 2)" footnote is removed, and the box now reads "kerugian negara tidak disyaratkan". All on-screen numbers are spoken and match draft.md and post.json: 20 Okt, Pasal 2 & 3, 2026, Pasal 603/604, 83%, 2024.
4. Audio: OK. -14.2 LUFS integrated, -3.7 dBTP true peak, LRA 2.3. No clipping.
5. Format: OK. 1080×1920, 30 fps, 88.23 s video against 88.20 s audio (difference 0.03 s). The cover frame is unchanged and readable.
6. Must-haves: OK. No photos are used, and every speaker has the same faceless name tag. The tagline, end card (handle and sources), and "Semua pernyataan sesuai kata masing-masing pihak" are all present. This is not a market topic and it is a new storyline, so the saham disclaimer and PART badge are not needed.

## Questions from production (unchanged from round 1)
(a) Danantara heard as "dan antara": **not an audible problem.** In voice.wav the energy stays above about -16 dB through the whole word (22.14–22.62 s), with no pause between "dan" and "antara". The speech-to-text split is lexical: it doesn't know the proper noun, and "antara" has logprob -1.0. No re-take is needed.
(b) "BELUM JADI ATURAN" stamp (l10b): **acceptable, keep it.** It is a factual summary of what l10 says (not in Prolegnas, no draft RUU announced), contains no number, and was in the approved visual plan. "MASIH WACANA" would be possible, but it is more loaded.
(c) Political neutrality: **OK.** Luhut, Setyo, Trisno and Yusril all get identical plain name tags, and every claim chip is attributed. The two vote chips are equal and each is revealed as it is spoken. The hook eraser only hovers and nothing is erased. The h2 pre-gap works: there is about 180 ms of silence before "Ka Pe Ka", and speech-to-text heard "KPK".

## Round 1 fixes (both applied and verified)
1. The "sejak 2026" badge over the "KUHP baru" title (29–42 s) was removed. Verified.
2. The unspoken "(Pasal 3 ayat 2)" footnote (39–43 s) was removed. Verified.
