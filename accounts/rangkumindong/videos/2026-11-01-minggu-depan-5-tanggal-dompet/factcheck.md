VERDICT: FIX (3 issues)

Checked 1 Nov 2026. MODE=full. Highest claim sensitivity: **high** (5 Nov Jokowi witness / Roy Suryo trial; the wording is neutral and schedule-only, so it is OK).

| Claim | Verdict | What the source actually says | Source |
|---|---|---|---|
| d2 / caption: 3 Nov US midterms, "rupiah dipantau" | **FIX** | The date is right (3 Nov 2026). Kontan's rupiah week-ahead piece (30 Okt) does **not** mention the midterms. Its rupiah drivers are US PCE, US Q3 GDP, Fed expectations and student demos. Kontan's IHSG piece (31 Okt) says investors will watch "pelaksanaan pemilu paruh waktu di Amerika Serikat pada 3 November 2026", which is a market link, not a rupiah link. A search found no source that ties the midterms to the rupiah. | https://investasi.kontan.co.id/news/rupiah-diprediksi-bergerak-fluktuatif-pekan-depan-simak-proyeksinya · https://investasi.kontan.co.id/news/ihsg-diprediksi-masih-tertekan-pekan-depan-simak-rekomendasi-excl-medc-dan-tapg |
| Hook B hb1: "Prabowo luncurkan bansos digital" | **FIX** (minor) | Katadata: DEN/Luhut said on 20 Okt that the program "akan diluncurkan langsung oleh Presiden Prabowo" on 10 Nov. The launch is in the future. A bare "luncurkan" reads as if it has already happened. | https://katadata.co.id/berita/nasional/6ad7a6394d4dc/prabowo-bakal-luncurkan-perlinsos-digital-10-november-sasar-50-juta-penerima |
| Caption: BPS October inflation "sekitar" 2 Nov; cited source = Antara September inflation | **FIX** (source) | The Antara link only covers September inflation and does not support the timing. Kontan (30 Okt) says the market is waiting for "pengumuman data inflasi Oktober pada pekan depan", with no day given. BPS usually releases on the first working day, and 2 Nov is a Monday, so the "diperkirakan" wording is fine. The source needs swapping. | https://investasi.kontan.co.id/news/rupiah-diprediksi-bergerak-fluktuatif-pekan-depan-simak-proyeksinya |
| d3b / caption: PDB Q3 "diperkirakan rilis" this week, date not official | OK | Kontan (31 Okt) lists "pertumbuhan ekonomi kuartal III-2026" among next week's data, with no date. BPS has released Q3 on 5 Nov in past years (2025: 5 Nov). The on-screen label "DIPERKIRAKAN · BELUM RESMI" is correct. | https://investasi.kontan.co.id/news/ihsg-diprediksi-masih-tertekan-pekan-depan-simak-rekomendasi-excl-medc-dan-tapg |
| t1–t3 / caption: 9 Nov digital tax, Shopee, Lazada, GoTo, banks/fintech; "baru kata Hashim, DJP belum konfirmasi" | OK (re-check before posting) | Hashim, Ketua Dewan Penasihat Kadin, spoke at the Kadin Rapimnas on 29 Okt: "Ini akan segera dilaksanakan tanggal 9 November … Semua bank pemerintah, bank swasta, dan semua fintech, termasuk Shopee, Lazada, GoTo." detik reports no DJP response and no regulation. A 1 Nov search also found no DJP confirmation. The "katanya" framing is correct. | https://finance.detik.com/berita-ekonomi-bisnis/d-8729936/bocoran-hashim-shopee-goto-pungut-pajak-digital-mulai-9-november-2026/amp |
| d3: 5 Nov Jokowi witness at Roy Suryo trial, PN Jakarta Timur | OK (high sensitivity) | detik (28 Okt): the prosecutor said "Kami akan melakukan pemanggilan terhadap saksi atas nama Ir H Joko Widodo dan Syarif Muhammad Fitriansyah" for Thursday 5 Nov, PN Jakarta Timur. The charges are defamation/slander under KUHP 2023 and the ITE Law. A 1 Nov search found no postponement. The script and visuals say nothing about the diploma and use no verdict language, and the name tags treat both people the same. Re-check on 4 Nov. | https://news.detik.com/berita/d-8728102/jaksa-hadirkan-jokowi-pekan-depan-roy-suryo-ini-yang-ditunggu-tunggu |
| h1 / r1–r2: Perlinsos Digital starts 10 Nov, bansos goes digital | OK | CNBC (29 Okt): "Pemerintah bersiap memulai Program Perlindungan Sosial (Perlinsos) Digital pada 10 November 2026". Katadata confirms 10 Nov. | https://www.cnbcindonesia.com/tech/20261029180207-37-780709/daftar-dan-buka-rekening-bansos-sekarang-cuma-1-menit-ini-caranya |
| r3: target 48 juta keluarga, 15,7 juta registered as of 28 Okt | OK (attribution note) | CNBC: "target sekitar 48 juta KK" and "lebih dari 15,7 juta Kepala Keluarga (KK) telah teregistrasi" as of 28 Okt. CNBC states these in its own narration and does **not** attribute them to Komdigi/Kemensos. Katadata's "50 juta penerima" is a different unit. | same CNBC URL |
| d1: 81 HSC stocks out of the IHSG count from 2 Nov | UNVERIFIED (site fetch failed) | The Bisnis and Tirto pages failed to load. Both headlines match the claim (81, from 2 Nov, removed from the IHSG count). The "82" reported by one outlet is still open. Low risk. | Bisnis / Tirto URLs in claims.json |
| Disclaimer "Bukan ajakan jual/beli saham" | OK | It appears on screen in zone 1, in the caption and in script.json. | — |

## FIX wording

1. **d2** text: `3 November: pemilu sela Amerika, pasar ikut memantau.` · say: `Tiga November: pemilu sela Amerika, pasar ikut memantau.`
   Caption/YT/TikTok: `Sel 3 Nov: pemilu sela Amerika, pasar ikut memantau.`
   Visual zone 2: swap the rupiah coin for a generic market/chart sticker with a "?" (no number). Pinned source 3: replace the Kontan rupiah link with the Kontan IHSG link (31 Okt), which names the 3 Nov midterms.
2. **hb1** text/say: `Prabowo bakal luncurkan bansos digital. Kamu sudah terdaftar?`
3. **Pinned source 2**: replace the Antara September-inflation link with `Kontan, 30 Okt: data inflasi Oktober diumumkan pekan depan https://investasi.kontan.co.id/news/rupiah-diprediksi-bergerak-fluktuatif-pekan-depan-simak-proyeksinya`.

Minor (no verdict change): the zone 5 source line "Komdigi/Kemensos, per 28 Okt" should read `CNBC Indonesia, per 28 Okt`, because CNBC does not attribute the figures to either ministry.

## Fixes applied (writer, 1 Nov)
1. d2 → "3 November: pemilu sela Amerika, pasar ikut memantau." (say: "Tiga November: …"); IG/YT/TikTok captions updated; zone 2 rupiah coin → generic market-chart sticker with "?"; pinned source 3 → Kontan IHSG 31 Okt (+ RM.id); "rupiah" tag and storyline tag removed.
2. hb1 → "Prabowo bakal luncurkan bansos digital. Kamu sudah terdaftar?"
3. Pinned source 2 → Kontan 30 Okt (inflasi Oktober diumumkan pekan depan); Antara link removed.
Minor: zone 5 source line → "CNBC Indonesia, per 28 Okt"; claims.json note updated.
d1 (81 HSC): verified from IDX Channel 26 Okt 20:41 WIB (Dirut BEI Jeffrey Hendrik, press conference: 81 saham, efektif 2 Nov 2026): https://www.idxchannel.com/market-news/81-saham-hsc-dikeluarkan-dari-ihsg-mulai-november-cek-daftarnya/all . Earlier counts 80 (Fortune IDN, 20 Okt) and 82 (Bisnis, 23 Okt) were earlier lists; 81 is the latest. Kept, now cited first in pinned source 1 and claims.json.
Spoken words: 99 (about 47 s).
