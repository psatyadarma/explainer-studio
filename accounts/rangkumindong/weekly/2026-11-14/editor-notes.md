VERDICT: FIX (5)

Reviewed: out/video.mp4 (442.3 s), contact sheet every 5 s, full script.json, post.json, per-chapter loudnorm.
Note: chapter 01 reviewed AS IS; it may be re-voiced after the MPR meeting, so fixes 1, 2 and 3 should be applied to the re-voiced version (re-check timings and the chapter list after the re-voice).

## Checks that passed
- Hook: "Seminggu, dua orang penting mundur. Kamu ketinggalan?" at 0:00, with "DUA MUNDUR" on screen. OK.
- Flow: intro -> 5 chapters -> ch06 "Catat tanggalnya" (next week) -> ch07 outro (11 s) -> OK.
- Audio: integrated loudness per chapter -14.5 to -15.0 LUFS, true peak -1.6 to -1.9 dBTP. No level jumps.
- YouTube chapters: 00:00 first, 8 chapters, all >= 10 s. Timestamps match real boundaries (26.1 / 108.9 / 175.1 / 244.8 / 303.7 / 374.1 / 431.2 s). OK.
- Colours and typography consistent across all chapters.

## Per chapter
- ch00 Intro (0:00-0:26): PASS
- ch01 Wapres Gibran (0:26-1:49, 82.8 s): FIX (1, 2, 3)
- ch02 Penyadapan (1:49-2:55): PASS
- ch03 MSCI (2:55-4:05): FIX (4)
- ch04 Nvidia (4:05-5:04): PASS
- ch05 Kripto/GitHub/bank (5:04-6:14): FIX (4)
- ch06 Catat tanggalnya (6:14-7:11): FIX (2)
- ch07 Outro (7:11-7:22): PASS

## Fixes
1. ch01, ~1:44-1:49 (last line a12, "Siapa dua nama calonnya?"): layout collision. The "Tidak ada Plt wapres" chip overlaps the "Calon 2" box, and the "belum diumumkan resmi" chip is clipped at the right edge (seen in the 1:46 frame). Change: on the a12 scene, remove the "Tidak ada Plt wapres" chip (already shown during a10) and keep only the two Calon boxes plus the "belum diumumkan resmi" chip, fully inside the frame (>= 64 px margin).
2. ch01 a10 vs ch06 g2: repeated sentence. Both say "kata Yusril/Menko Yusril, Presiden ... kalau tidak salah sampai 14 atau 16 November" with the same 14/16 Nov visual. Change: delete line a10 and its card from ch01 (saves ~11 s, ch01 -> ~72 s, closer to the other chapters). Keep it only in ch06 g2. In ch06 g2 add the "tidak ada Plt wapres" point ("selama itu tidak ada pelaksana tugas wapres") so nothing is lost. Alternative if a10 must stay in ch01: in ch06 g2 drop the Yusril attribution and say only "Presiden dijadwalkan kembali pertengahan pekan."
3. ch01 a9 and a12 are time-stale at the Saturday 14 Nov publish: a9 says the MPR joint meeting is "Jumat pukul 14.00" (future tense, "dijadwalkan") and a12 says "sampai naskah ini ditulis, Jumat pagi, belum diumumkan". Both are already past when viewers watch. Change: re-voice after the meeting as planned: a9 -> outcome of the Friday meeting (date set for the paripurna, or not yet), a12 -> current status of the two names. Update the "JUMAT / DIJADWALKAN" card to match. Then rebuild and regenerate build/youtube-chapters.txt and the BAB list in post.json (youtube_description and the Gibran bullet in caption/tiktok_caption).
4. Pacing, visual held > 6 s: (a) ch03, about 3:10-3:25 (IHSG "+2,66% ~5.250" card) stays on the same card for ~12-15 s while only the caption changes (lines c4 -> c5). Change: at the start of c5 (Phintraco analyst) swap in a quote card ("Analis Phintraco, via Suara: redanya ketegangan politik") and shrink the +2,66% to a corner stat. (b) ch05, about 6:00-6:10 ("Bukan cuma sistem besar", e7 -> e8): same scene ~10-15 s. Change: at e8 replace the big title with the two advice chips (beli dompet dari penjual resmi / cek aplikasi bank sebelum tenggat) as the main visual, title moved to a small label.
5. Chapter title cards are inconsistent: ch01 and ch07 open with a title card, ch03 with a faint title, but ch02, ch04, ch05 and ch06 jump straight into content (first frames: "4 tersangka", "KAMIS MALAM WIB", "Binance + Ledger", "MSCI Hasil keluar"). Change: give ch02-ch06 the same 1-1.5 s kicker + title card as ch01 (title text from script.json, no voice delay), or drop it from ch01 and ch07 for consistency. If cards are added, chapter durations grow ~1.5 s each: regenerate build/youtube-chapters.txt after the rebuild.

Minor, no action required: ch00 stat label "IHSG melonjak (persen)" reads awkwardly next to "2,66%"; change to "IHSG, Kamis" if there is time. The 2,66% counts up from 2,60% in the first frames (animation, correct by 0:12).
