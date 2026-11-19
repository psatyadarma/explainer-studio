VERDICT: FIX (3)

Reviewed: out/video.mp4 (417.4 s), contact sheet every 5 s, full script.json, post.json, per-chapter loudness.
(Editor pass run by the coordinator: no sub-agent tool was available in this session.)

## Checks that passed
- Hook in first 15 s: "Bunga naik, kursi wapres kosong. Lalu apa?" + "Minggu ini" cards (6%, Dasco, Listyo). OK.
- Flow: intro -> 5 chapters -> ch06 "Catat tanggalnya" (with check on last week's promises) -> ch07 outro (12.8 s). OK.
- Every chapter opens with the 2 s title card; colours/typography consistent (sticker kit).
- Audio per chapter: -14.5 to -15.4 LUFS integrated (ch05 lowest, 0.8 LU under the rest; acceptable), peaks <= -0.4 dBFS before the final loudness pass.
- YouTube chapters (build/youtube-chapters.txt and post.json "BAB:"): 00:00 first, 8 chapters, all >= 10 s, match boundaries.
- Repetition: "Misalnya Pak Budi" opens both ch03 and ch05 (script choice, different situations); kept.

## Fixes
1. ch03 ~3:33 (c6 "Kenapa?"): the "+" between "Bunga BI" and the Fed card touches the card edge. Change: move chip to x-560, "+" to x-250.
2. ch05 ~5:15 (e4): "Yang paling bikin kaget" label overlaps the top of the 100-dot grid. Change: move label above the 47% stat (right column).
3. ch06 ~6:08 (g3 -> g4): camera moves to an identical "SENIN 23 NOV" calendar (repeated visual). Change: g4 shows a "Juga 23 Nov" highlight chip instead of a second calendar.

## Re-check (after fixes)
- Re-check: ch03, ch05, ch06 re-rendered; frames at 3:33, 5:15, 6:10 show no overlaps and no repeated calendar. Final video 417.4 s, -14.3 LUFS, -1.3 dBFS peak. VERDICT after fixes: READY.

## Second review (editor-review-2.md) — applied 20 Nov
1. ch01 a9: "Hati-hati" chip moved up and raised above the video card (z-index).
2. ch06 g4: "Bisa diperpanjang" chip un-rotated, spacing added above/below (no contact with either card).
3. ch04 d6 (illicit enrichment, UNVERIFIED) cut: removed from script.json + chapter script, its audio spliced out of voice.wav (11.3 s, no new TTS; backup in chapters/04/build/pre-cut/), timing shifted, remixed, scene + CNN lower third removed. post.json caption/YouTube/TikTok/pinned sources and the tag removed; claims.json d6 marked CUT.
All 8 chapters re-rendered (progress bar ticks depend on total length). Final: 406.2 s, 1920x1080, 30 fps, -14.3 LUFS, -1.3 dBFS. YouTube chapters: 00:00 / 00:29 / 01:41 / 02:48 / 03:53 / 04:37 / 05:27 / 06:33.
Still open (not done here): the Friday 20 Nov rechecks named in editor-review-2 (Kejagung expose / gelar perkara outcome, Listyo detention extension) for b3, b7, g4.
