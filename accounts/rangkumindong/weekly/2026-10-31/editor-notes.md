VERDICT: READY  (re-check 3: ch02 re-rendered, week re-assembled)

## Re-check 3
- ch02 at 3–9 s (out/video.mp4 02:03–02:09): the "Sumber" lower third now sits clear above the subtitle block, with no overlap at 4, 6, 8 or 8.8 s. The Brent label ">US$115" fades in with its bar and does not touch the lower third.
- ch02 at 83–87 s (03:23–03:27): `#q` at top:150px clears the BAB 2 badge and the 7,54% card, and it sits on one line.
- Both remaining fixes from re-check 2 are resolved. Nothing is left to fix. The Friday 30/10 IHSG close is still pending, as noted below.

---

## Re-check 2 (superseded): FIX (2)

## Re-check 2: remaining fixes

1. **02:03–02:09 (ch02 at 3–9 s), Siapa yang nombok? The "Sumber" lower third collides with the subtitle.**
   Problem: `#lower1` ("Sumber · Detik, CNBC Indonesia, APBN KiTa, Bisnis"), bottom-left, shown 3.0–9.0 s. Its bottom edge sits on the first subtitle line. At about 8 s "Jumat, 23 Oktober" is drawn over the bottom of the box, which also covers the source text.
   Change: raise `#lower1` by at least 60 px, so that its bottom is at least 16 px above the top of the subtitle block. Alternatively, use ch01's top slot (`.lower { top:120px; bottom:auto; }`), but only if it clears the "> 115" card.
2. **03:23–03:27 (ch02 at 83–87 s). The question card `#q` now overlaps the BAB 2 chapter badge.**
   Problem: the wrap and the overlap with the 7,54% card are fixed. However, at `top:110px` the right end of the card runs under the "BAB 2 · Siapa yang nombok?" badge (top-right, about 30 px of overlap).
   Change: set `#q` to `top:150px`. That clears the badge row and still sits above the 7,54% card, which starts at about 290 px. Alternatively, keep `top:110px` and shift the card left so its right edge stays at or below x=1380.

**Resolved in re-check 2:**
- ch01: the chart labels are no longer cropped and the Fed sticker sits inside the frame.
- ch01 at about 46 s: "5.439" clears the "Penutupan harian" lower third by about 10 px. That is tight, but nothing overlaps.
- ch02: the Brent label now reads ">US$115".
- ch06: "Tertib" clears "Kata polisi".
- post.json: "BAB:" now appears once.
- Chapter durations are unchanged (ch01 85.47, ch02 87.13, ch06 78.03 s; total 611.7 s), so the YouTube timestamps are still valid.

---

## Original review (re-check 1): VERDICT: FIX (5)

Rangkumin Seminggu #2 (24–30 Okt 2026). I reviewed out/video.mp4 (611.7 s, 1920x1080, 30 fps): a contact sheet at one frame every 5 s, zoomed frames at every point the chapter builders flagged, the full script.json, post.json, and factcheck.md against claims.json.

## Fixes

1. **00:41–01:21 (ch01 at 7–47 s), IHSG jatuh lagi. The chart pan crops labels at the left edge.**
   Problem: when the camera pans right to show Rabu and Kamis, the Senin point stays half off screen: "73", "%" and "in" (from 5.373 / −1,22% / Senin) are cut at x=0. This lasts through the Kamis −3,49% beat. The "The Fed tahan suku bunga" sticker also enters touching the right frame edge (about ch01 38 s).
   Change: in chapters/01/index.html, fade out pts[0] and pts[1] (dot, value label, day label) as they pass x < 120 px on screen, or reduce the pan so that Selasa through Kamis sit inside a 96 px safe margin. Move `#fed` (left:3650px) about 100 px left so it stays inside the safe area.

2. **03:23–03:27 (ch02 at 83–87 s), Siapa yang nombok? The final question card overlaps the yield card and wraps badly.**
   Problem: `#q` ("Sampai kapan Pertalite Rp10.000 bisa ditahan?") shrink-wraps to a narrow column of 6 lines. It sits on top of the 7,54% card and hides "Imbal hasil SUN ~10 tahun".
   Change: on `#q` add `white-space:nowrap` (or `width:1100px; text-align:center`) and move it to `top:110px` so it clears the 7,54% card. Alternatively, fade the 7,54% group out at b11 and centre the question alone.

3. **02:00–02:10 (ch02 at 0–10 s), Siapa yang nombok? The Brent bar shows Monday's price under Friday's tag.**
   Problem: the bar label reads "Brent US$115,81" from the first frame, under the sticker "Jum 23 Okt · tertinggi 5 bulan". US$115,81 is Monday's close (claims b3), and b2 only says "di atas 115".
   Change: in chapters/02/index.html, line 31, change the `.cl` text to `Brent<br>&gt;US$115`. The existing `#t26` tag ("Senin: 115,81") already brings in the Monday figure at b3.

4. **08:44–08:46 (ch06 at 67–69 s), Demo 28 Oktober. The "Tertib" stamp covers the "Kata polisi" tag.**
   Problem: after the repositioning, the stamp `#eTr` (top:405px) overlaps the bottom of `#eKp` (top:300px), which cuts off the tag's baseline.
   Change: set `#eTr` to `top:450px`, or `#eKp` to `top:255px`. They need at least 20 px between them.

5. **post.json youtube_description: the chapter header is duplicated.**
   Problem: the description ends with "BAB:\n\nBAB:\n00:00 Minggu ini…", so "BAB:" appears twice.
   Change: delete the first "BAB:\n\n" and keep one "BAB:" before the timestamps.

## Checked and OK
- **Builder flags:**
  - The ch01 disclaimer tag at about 81.4 s is centred and readable, with no overlap (about 4 s on a sparse frame, which is fine).
  - The ch04 card "Tersangka belum tentu bersalah" (83–87 s) is clean and exits cleanly into the BAB 5 title card.
  - The ch00 lower third "Pekan ini · 24–30 Okt" is generic but correct and consistent with the title. It can stay as it is.
- **Hook and flow:** the hook "Seminggu ini rame lagi…" plus a three-item teaser lands in the first 15 s. The order is intro → 6 chapters, each with a title card → "Minggu depan" → outro with a comment CTA and the Follow card.
- **Chapter lengths:** 34 / 85 / 87 / 95 / 87 / 67 / 78 / 67 / 10 s. They are balanced; ch03 is the longest but has the most content.
- **Pacing:** freezedetect found no frozen picture of 4 s or more. There are no black frames and no silences longer than 1.5 s.
- **Consistency:** palette, typography, BAB badges and source tags are consistent across all chapters. The opener "<day> kemarin kami tanya/bahas…" repeats in ch1–5, which is intended because it calls back to the daily videos. "Itu hitungan kami" appears twice (ch01 and ch04), which is fine.
- **Audio:** chapters measure −13.8 to −14.6 LUFS (spread 0.9 LU). The full video is −14.0 LUFS integrated with a −2.8 dBTP true peak, so there are no level jumps.
- **YouTube chapters:** they match the assembled cut. Actual chapter starts are 0 / 34.1 / 119.6 / 206.7 / 302.1 / 389.4 / 456.8 / 534.8 / 601.4 s. The list starts at 00:00, has 9 chapters, and each is at least 10 s (the last is 10.3 s).
- **Numbers against factcheck/claims:**
  - All 9 FIX rewrites are in script.json and on screen (a5 "Kamis dini hari", d5, d8 Hardjuno, c5 "terdampak", c9, p3–p5, p8 KSP Listyo Sigit, g2, g3).
  - The IHSG chain checks out: 5.439 → 5.373 (−1,22%) → 5.266 (−1,99%) → 5.282 (+0,31%) → 5.098 (−3,49%). The week change is −6,27%, so "≈ −6%" is correct.
  - Also verified: BCA −6,35%; Rp376,8 T; SUN Rp31,09 / 20,65 / 30 T and 7,54%; 3.030 / 154 / 1.700, where ≈23 per day matches 1.700 over 73 days; 93 → 79; 462 / 10 / 169 ha; 245 + 20; 35 ribu ha; 8 tersangka/terdakwa; 10–12 ribu (attributed to BEM UI); 53 aksi; 14.00–19.45; 7,5–9,5%; 3,28%.

## Open item (not counted above)
- factcheck.md still has one PENDING item: the Friday 30/10 IHSG close. The video says "sampai Kamis" throughout, but the title covers 24–30 Okt. If Friday's close is to be added (a line after a7, plus the caption, YouTube description, TikTok caption and thumbnail), ch01 needs a re-voice and re-render, and every later timestamp moves.

## Optional
- **ch08 outro chips:** the list ends with "Catat tanggalnya", which is the next-week section, not a story. "Demo mahasiswa" also differs from the chapter title "Demo 28 Oktober". Drop the last chip and consider renaming "Demo mahasiswa" to match the chapter.
