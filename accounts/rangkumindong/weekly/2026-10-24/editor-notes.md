VERDICT: READY

Re-check of out/video.mp4 (443.7 s, 1920×1080, 30 fps, −14.2 LUFS) after the fixes below. Contact sheets were made every 2 s for all 9 chapters, plus the chapter boundaries.

## First pass: FIX (6), all applied
1. 02:40 (ch03, 12.7–16.1 s): only the "Kamis · kata Prabowo" tag was on screen for about 3.5 s. Fix: the 19 tally marks now start drawing at "menyebut", so the count runs up to "19".
2. 02:57 (ch03, 29.2–31.5 s): the stage was empty apart from the lower third while the minister was named. Fix: the 32-cell grid now builds from the start of line c6, and "32" still lands on the spoken "32".
3. 04:55 / 05:17 (ch05): the Airlangga and Yassierli lower thirds sat top-left, while every other chapter has them bottom-left. Fix: moved them to `bottom: 205px`.
4. 07:17 (ch08): five chapter chips sat in one row and "Sekilas" was alone on a second row at the left. Fix: two centred rows of 3.
5. 00:21 (ch00): the lower third said "Bab 7 · Minggu depan", but that chapter's kicker is "MINGGU DEPAN" and it is not called Bab 7 anywhere else. Fix: it now reads "Minggu depan · menit 06:38", taken from build/week.js.
6. YouTube description: the outro is only 8.3 s, under YouTube's 10 s minimum per chapter, so the timestamps could be ignored. A leftover "Bab: (daftar bab …)" placeholder was also left in place, because assemble only strips "BAB:". Fixes: `weekly.py index` now folds chapters under 10 s into the previous one, and the placeholder was removed from post.json.

## Checks passed
- Hook: "Kamu ketinggalan yang mana?" at 0 s, with topic stickers by 10 s. The flow is intro → 6 chapters → minggu depan → outro.
- Transitions: every chapter has the same hard cut to a title card.
- Pacing: no static hold over 6 s. Chapter lengths are 61–66 s; Sekilas is 55 s, minggu depan 37 s and the outro 8 s.
- Typography and colours are consistent across chapters.
- Per-chapter loudness ranges from −14.3 to −14.8 LUFS, so there are no level jumps.
- Chapter list: 8 entries, starting at 00:00, each at least 10 s.
- Not changed: the count-up numbers (e.g. 420 penumpang, Rp31,8 T) show in-between values for about 1 s, as in every other video in the series. The final true peak is −0.9 dBTP, a little above the −2 target, because of the AAC encode.
