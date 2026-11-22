VERDICT: FIX (1 issue)

Checked 22 Nov 2026 (Sunday), MODE=full. Weekdays verified: 23 Nov = Senin, 24 = Selasa, 25 = Rabu, 26 = Kamis; 9 Des 2026 minus 14 hari = 25 Nov.

| Claim (lines) | Verdict | What the source actually says | Source |
|---|---|---|---|
| h1 / h2 / YT title: "diputus **minggu ini**", "Minggu Ini: ..." | FIX | The dates are right (UMK by 25 Nov). But the post goes out Sunday 22 Nov at 19:00, and on a Sunday "minggu ini" usually means the week that ends today. The rest of the package says "minggu depan" (folder, format `minggu_depan`, #minggudepan). | (wording / date period) |
| d1: Danantara dijadwalkan rilis LK pertama Senin 23 Nov | OK (tentative) | Katadata 12 Nov: Dony: "Laporan keuangannya 23 November." Journalarta 15 Nov (second source): Dony on 15 Nov: "23 November kalau enggak salah." Hedged, so "dijadwalkan" is the right word. Nothing newer found. Re-check Monday morning. | https://katadata.co.id/finansial/keuangan/6af51dd359706/bos-danantara-jadwalkan-rilis-laporan-keuangan-2025-pada-23-november · https://journalarta.com/news/2026/11/15/laporan-keuangan-danantara-23-november/ |
| d2: COO Dony Oskaria, audit BPK selesai | OK | Katadata: Dony is COO Danantara; BPK has finished its examination. | Katadata (above) |
| d3: sudah mundur dua kali (Juni, lalu Oktober) | OK (one source) | Katadata: first target end of June 2026, then October 2026, both missed. Journalarta mentions only the June deadline. | Katadata (above) |
| l1: Selasa 24 Nov sidang etik Listyo, menurut Bangkapos | OK | Bangkapos: "dijadwalkan menjalani sidang KKEP ... pada Selasa (24/11/2026)", with no source given for the date. Still the only source for the date. Attribution "menurut Bangkapos" and the hook tag DILAPORKAN are correct and must stay. | https://bangka.tribunnews.com/video/1703303/desakan-listyo-sigit-tampil-24-november-kapolri-suyudi-disebut-bakal-pimpin-sidang-etik-video |
| l2: Polri resminya baru bilang "pekan depan"; majelis disiapkan (caption) | OK | Liputan6: Karopenmas Trunoyudo: "akan dilaksanakan pada pekan depan"; Propam is still preparing the panel. | https://www.liputan6.com/news/read/8337394/polri-bicara-susunan-hakim-sidang-etik-listyo |
| l3: dua jenderal lain diputus PTDH | OK | detikNews: Ahrie Sonta (KKEP 10/11) and Eko Hadi Santoso (KKEP 17/11) both received PTDH. | https://news.detik.com/berita/d-8757575/digelar-pekan-depan-siapa-yang-akan-pimpin-sidang-etik-listyo-sigit |
| l3: "Keduanya banding" | OK (one source) | Liputan6 18 Nov: both "telah mengajukan banding". This is not attributed to Polri. detikNews does not mention appeals. Acceptable as worded. | Liputan6 (above) |
| l4: Listyo berstatus tersangka; putusan etik belum ada | OK | detikNews: Listyo is one of four officers Polri named as suspects in the alleged wiretapping case. No ethics ruling yet. | detikNews (above) |
| w2: Kata Ketua MPR, pemilihan wapres mundur ke 9 Des | OK / attribution UNVERIFIED | Viva: the session originally set for 2 Dec "kini digeser menjadi 9 Desember 2026". I could not open the detikNews source (permission timeout), so "Ketua MPR" as the speaker is unconfirmed by me. | https://purwasuka.viva.co.id/nasional/22349-dukungan-dasco-jadi-cawapres-menguat-prabowo-kini-dihadapkan-tenggat-25-november · blocked: https://news.detik.com/berita/d-8755839/sidang-mpr-pemilihan-wapres-mundur-sepekan-ini-pertimbangannya |
| w3/w4: dua nama, 14 hari sebelumnya, tenggat sekitar Rabu 25 Nov, tulis Viva | OK | Viva: two names, "paling lambat 14 hari sebelum sidang paripurna", "batas akhir penyampaian nama jatuh pada 25 November 2026". "sekitar ... tulis Viva" is properly hedged. | Viva (above) |
| k1: Kamis 26 Nov UMSP | OK | detikFinance: UMSP "pada tanggal 26 November"; the governor "wajib" set the UMP and UMSP. | https://finance.detik.com/berita-ekonomi-bisnis/d-8755278/ump-2027-diumumkan-21-november |
| p1/p2: 25 = batas penetapan UMK | OK | detikFinance: UMK "paling lambat 25 November 2026". | detikFinance (above) |
| p5: UMK ikut kebijakan gubernur; UMSK paling lambat 30 Nov | OK | detikFinance: UMK/UMSK "disesuaikan dengan kebijakan gubernur setempat"; UMSK "paling lambat lima hari setelah penetapan UMK atau pada 30 November 2026". | detikFinance (above) |
| p4: UMP Jakarta 2027 Rp6,1 juta (Rp6.136.941), +7,1% | OK | Viva: Rp6.136.941, up Rp407.065 (7,1%) from Rp5.729.876. | https://www.viva.co.id/berita/metro/1945069-resmi-pramono-anung-ketok-ump-jakarta-2027-jadi-rp61-juta-naik-rp407-ribu |
| i1: empat hari, lima agenda | OK | 23 / 24 / 25 (wapres + UMK) / 26 = 5 agendas over 4 days. UMSK on 30 Nov (Senin) falls outside 23-29. | (count) |
| Disclaimer "Bukan ajakan jual/beli saham" | OK | Present in the script metadata, the captions and the pinned comment. | n/a |

Blocked (permission timeout, not retried): liputan6 UMP DKI 8338940 (covered by Viva), detikNews MPR d-8755839, CNBC Menaker 785953 (covered by detikFinance).

## FIX

1. **"minggu ini" means the wrong week on a Sunday post**
   - h1 text/say: `Upah minimum kotamu diputus minggu depan. Tanggal berapa?`
   - Same change in the first line of the IG, YouTube and TikTok captions: `Upah minimum kotamu diputus minggu depan. Tanggal berapa? 🗓️`
   - youtube_title: `Minggu Depan: Danantara, Sidang Listyo, Wapres, UMK #Shorts`
   - (w4 "sekitar Rabu ini" can stay: "Rabu ini" for the coming Wednesday is normal usage. Optional: `Jadi tenggatnya sekitar Rabu, 25 November, tulis Viva.`)

## Fixes applied (writer, 22 Nov)
- [x] FIX 1: h1 text/say → "Upah minimum kotamu diputus minggu depan. Tanggal berapa?"; same first line in IG, YouTube and TikTok captions (post.json + draft.md).
- [x] youtube_title → "Minggu Depan: Danantara, Sidang Listyo, Wapres, UMK #Shorts".
- [x] w2 attribution: speaker unverified, so "Kata Ketua MPR, …" → "Pemilihan wapres di MPR dilaporkan mundur ke 9 Desember." (script, captions bullet, draft visual chip, claims.json). Viva supports the move itself.
- [x] Kept: "menurut Bangkapos" (l1) and the DILAPORKAN tag on the Listyo date. w4 "sekitar Rabu ini" left as is (optional change not taken).
- Length: 214 spoken tokens (cap 215).
