# Draft: Rupiah Rp18.046, besok BI putuskan: tahan 5,75% atau naik ke 6%?
**Run 20 Okt 2026** · idea #3 · arm: 🎙 Cahaya (female) · 🕧 12:30 WITA · 🪝 shock number · storyline: new (`rupiah`), links to msci-reclassification · ~86 s (232 spoken words; PART 1 was 190 words = 70,6 s) · fact-check FIXes applied 20 Okt

## Topic + angle
The rupiah is above Rp18.000 the day before BI's 21 Oct decision. Your angle note is built in: **"ini bukan pertama kali"**. On 4 Jun 2026 the rupiah first closed above Rp18.000 (Rp18.049). For scale: the 1998 crisis peak was around Rp16.800 and the Covid low in 2020 was Rp16.575, but in 1998 the rupiah lost more than 80% of its value. In June BI raised rates twice in 10 days (9 Jun to 5,50%, 18 Jun to 5,75%) and has held since July. The video then covers what is different now (MSCI and the Fed; reserves and inflation as cushion) and sets out the two options for tomorrow neutrally, with no prediction.

## Script (subtitle text)
| id | tag | text |
|---|---|---|
| h1 | shocked | Rp18.046 per dolar. |
| h2 | serious, urgent | Besok BI putuskan: bunga ditahan 5,75%, atau naik ke 6%? |
| rd | (tagline, Cahaya) | Rangkumin dong! |
| l1 | curious | Tapi tunggu. Rupiah tembus 18.000 itu… bukan pertama kali. |
| l2 | matter-of-fact | 4 Juni 2026: pertama kali ditutup di atas 18.000, di Rp18.049. |
| l3 | explaining | Buat perbandingan: krisis 1998, puncaknya sekitar Rp16.800. Covid 2020: Rp16.575. |
| l4 | serious | Tapi tahun 1998, rupiah kehilangan lebih dari 80% nilainya. |
| l5 | punchy | Terus, BI ngapain? Naikin bunga. Dua kali. Dalam 10 hari. |
| l6 | quick | 9 Juni ke 5,50%. 18 Juni ke 5,75%. Sejak Juli, ditahan. |
| l7 | serious | Bedanya sekarang? Pemicunya MSCI, plus The Fed yang masih buka peluang naikin bunga. |
| l8 | reassuring | Bantalannya: cadangan devisa US$146,3 miliar. Inflasi 3,28%, masih dalam target. |
| l9 | neutral | Jadi, besok ada dua opsi. |
| l10 | neutral | Opsi 1: tahan di 5,75%. Sebagian ekonom, misalnya Danamon: rupiah dijaga lewat intervensi dulu. |
| l11 | neutral | Opsi 2: naik ke 6%, proyeksi Bloomberg Economics. Kata Citi, kenaikan itu langkah antisipasi, biar arus keluar dari pasar saham nggak merembet ke pasar obligasi. |
| l12 | matter-of-fact | Naik: pinjaman bisa makin mahal. Tahan: tekanan ke rupiah bisa berlanjut. |
| cta | playful | Kalau kamu BI: tahan atau naik? Komen! |
| end | friendly | Follow Rangkumin Dong, biar nggak ketinggalan! |

The spoken `say` versions in script.json spell out every number ("delapan belas ribu empat puluh enam", "be i", "em es si ai").

## Visual plan (zones; plot only the values below)
1. **Hook / cover (h1–h2):** a huge "Rp18.046" counter (accent #FF5A36) above a US$1 bill sticker ⇄ a stack of rupiah notes. Small label "penutupan 19 Okt". Below it, a BI building sticker with two option chips, "5,75%" and "6%?", and a calendar sticker "Rabu 21 Okt". This frame works as the cover.
2. **Tagline (rd).**
3. **"Bukan pertama kali" (l1–l4):** a horizontal bar/marker chart titled **"Rupiah tembus 18.000: dulu vs sekarang"** (Rp per US$). Bars: **1998: ≈16.800 (intraday, Jun 1998)** · **2020: 16.575 (penutupan 23 Mar)** · **2026 low: 18.170 (penutupan 8 Jun)** · **now: 18.046 (penutupan 19 Okt)**. A dashed line at 18.000, with a separate pin on it: **"4 Jun: pertama kali tutup di atas 18.000 (18.049)"**. The 8 Jun bar is shown, not spoken, so the script never calls 19 Okt a record. Then a "−80%+" stamp on the 1998 bar with the note "dari sekitar Rp2.500". Use a "1998 crisis" newspaper sticker and a mask sticker for 2020.
4. **BI's response in June (l5–l6):** a staircase chart of the BI-Rate. 4,75% → 5,25% (20 Mei) → **5,50% (9 Jun)** → **5,75% (18 Jun)** → flat Jul–Sep–Okt. Highlight the 9→18 Jun steps with a "10 hari" bracket. Show a "Juni 2026" timeline strip with a rupiah 18.049 pin on 4 Jun.
5. **Bedanya sekarang (l7–l8):** two trigger stickers, the MSCI logo-free "index" card ("Emerging → Standalone?") and a Fed building "27–28 Okt". Then two cushion tiles: "Cadev US$146,3 miliar (akhir Sep, BI)" and "Inflasi 3,28% (target 2,5±1%)".
6. **Dua opsi (l9–l12):** split screen, Tim A "TAHAN 5,75%" (shield + "intervensi" sticker, small label "sebagian ekonom, mis. Danamon") vs Tim B "NAIK 6%" (up-arrow, small label "proyeksi Bloomberg Economics · Citi: antisipasi"). Trade-off line underneath: "Naik → pinjaman lebih mahal" / "Tahan → rupiah bisa terus ditekan". **No "our pick" mark**; both sides get the same size and colour weight.
7. **CTA + end card:** "Tim A atau Tim B? Komen!", the disclaimer "Bukan ajakan jual/beli saham atau valas", and sources.

Safe area: keep everything in x 60–920, y 240–1480; run `engine/safezone.py`.

## Before render (fast-moving)
- **Refresh the rupiah after the 20 Oct open (09:00 WIB = 10:00 WITA).** No 20 Oct quote existed at draft time (last: 19 Oct close Rp18.046, Antara). If the morning level differs meaningfully, swap h1 to "Rp18.xxx pagi ini" with a spoken update; the slot is 12:30 WITA, so there is time.
- Data vendors differ by tens of rupiah (CNBC/Refinitiv had 16 Oct at Rp18.000, while Antara/Bloomberg implies 18.027). Stick to the Antara/Bisnis quotes in the video.

## Sources
- Antara, 19 Okt 2026 (close Rp18.046, JISDOR 18.050): https://www.antaranews.com/berita/5796589/rupiah-melemah-ke-rp18046-dipengaruhi-potensi-kebijakan-ketat-the-fed
- Bisnis, 4 Jun 2026 (close Rp18.049, terlemah sepanjang masa): https://market.bisnis.com/read/20260604/93/1978431/rupiah-ditutup-terjun-ke-rp18049-per-dolar-as-kamis-46
- Republika, 4 Jun 2026 (tembus 18.000, BI "terus berada di pasar"): https://ekonomi.republika.co.id/berita/tg35xl423/rupiah-tembus-rp-18000-per-dolar-as-terlemah-sepanjang-sejarah
- detikFinance, 4 Jun 2026: https://finance.detik.com/bursa-dan-valas/d-8517059/dolar-as-sudah-tembus-rp-18-000
- Okezone, 6 Jun 2026 ("terendah sejak krismon 1998"): https://economy.okezone.com/read/2026/06/06/320/3222877/7-fakta-rupiah-anjlok-tembus-rp18-000-per-dolar-as
- Bisnis, 10 Des 2025 (1998 ≈16.800, >80%; 2020 16.575): https://market.bisnis.com/read/20251210/93/1935863/4-dekade-jatuh-bangun-nilai-tukar-rupiah-dihajar-krismon-hingga-kebijakan-trump
- IDX Channel, 9 Mar 2026 (1998 16.800 intraday): https://www.idxchannel.com/market-news/rupiah-dibuka-melemah-tembus-rp17000-per-dolar-as-lampaui-krisis-moneter-1998/all
- Bisnis, 2 Jul 2020 (23 Mar 2020 close 16.575): https://market.bisnis.com/read/20200702/93/1260924/4-bulan-corona-di-indonesia-rupiah-sempat-deja-vu-rasa-1998
- Katadata Databoks (23 Mar 2020, 16.575): https://databoks.katadata.co.id/en/economics-macro/statistics/7538ea6c47804ef/coronavirus-cases-rise-rupiah-falls-to-rp-16575us-monday-march-23
- IDN Financials, 20 Mei 2026 (+50 bp to 5,25%): https://www.idnfinancials.com/news/63971/bi-rate-up-50-bps-to-5-25-to-shield-rupiah-from-global-volatility
- Investor Trust, 9 Jun 2026 (5,50%, RDG mingguan): https://investortrust.id/macro/105809/bi-rate-resmi-naik-jadi-5-50-ini-strategi-bank-indonesia-amankan-nilai-tukar-rupiah
- Kontan Insight, 9 Jun 2026: https://insight.kontan.co.id/news/rupiah-jeblok-bank-indonesia-mengerek-bi-rate-ke-angka-550-hari-ini-96
- BI press release, 18 Jun 2026 (5,75%): https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2812626.aspx
- Bisnis, 18 Jun 2026: https://finansial.bisnis.com/read/20260618/11/1981625/bank-indonesia-naikkan-suku-bunga-acuan-bi-rate-25-bps-ke-575
- IDN Financials, 23 Sep 2026 (held Jul/Aug/Sep): https://www.idnfinancials.com/news/69301/bi-holds-rate-at-5-75-for-third-time-to-support-rupiah
- Kontan (cadev Sep US$146,3 miliar): https://nasional.kontan.co.id/news/cadangan-devisa-indonesia-september-2026-turun-jadi-us1463-miliar
- Bank Indonesia (cadev Sep): https://www.bi.go.id/id/iru/highlight-news/Pages/Cadangan-Devisa-September-2026-Tetap-Terjaga.aspx
- Bisnis, 9 Jun 2026 (8 Jun close 18.170): https://market.bisnis.com/read/20260609/93/1979416/nilai-tukar-rupiah-terhadap-dolar-as-hari-ini-selasa-9-juni-2026
- Kontan, 8 Jun 2026 (18.188, rekor terburuk lagi): https://investasi.kontan.co.id/news/rupiah-ditutup-anjlok-ke-rp-18188-per-dolar-as-hari-ini-86-rekor-terburuk-lagi
- Investor Trust (inflasi Sep 3,28%): https://investortrust.id/macro/118018/bps-inflasi-september-2026-tembus-0-30-tahunan-3-28
- Bisnis, 17 Okt 2026 (**hold side**: Irman Faiz/Danamon only; Josua Pardede/Permata sees room for 6% by year-end, so he is not a hold voice; MSCI + Fed; 0,1% growth cost): https://ekonomi.bisnis.com/read/20261017/9/2013276/tekanan-eksternal-bertubi-dari-as-hingga-msci-apa-dampaknya-ke-ekonomi-ri
- CNBC Indonesia, 19 Okt 2026 (**hike side**: Citi via Reuters, a pre-emptive step against outflows spreading from stocks to bonds; Citi gives no level): https://www.cnbcindonesia.com/research/20261018190508-128-777262/ri-di-bibir-jurang-ihsg-rawan-ke-bawah-5000-rupiah-menanti-jurus-bi
- Buletin Finansial, 19 Okt 2026 (**hike side**: Bloomberg Economics → 6%): https://buletinfinansial.com/detail/529078/bi-rate-diproyeksi-naik-25-bps-jadi-6-di-tengah-rupiah-melemah-12

## Captions
**IG caption**
```
Rp18.046 per dolar 😳 Besok (21/10) BI putuskan: bunga ditahan 5,75% atau naik ke 6%?

Rangkumin dong 👇
• Bukan pertama kali di atas Rp18.000: 4 Juni 2026 rupiah ditutup Rp18.049. Sebagai perbandingan, puncak krisis 1998 sekitar Rp16.800 dan Covid 2020 Rp16.575
• Waktu itu BI naikin bunga 2 kali dalam 10 hari: 9 Juni ke 5,50%, 18 Juni ke 5,75%. Sejak Juli ditahan
• Sekarang pemicunya MSCI & The Fed. Opsi besok: tahan 5,75% (sebagian ekonom, misalnya Danamon: rupiah dijaga lewat intervensi) atau naik ke 6% (proyeksi Bloomberg Economics; Citi: langkah antisipasi)

Kalau kamu BI: tahan atau naik? Komen 👇

Bukan ajakan jual/beli saham atau valas. Sumber di komentar.

#rupiah #BIRate #BankIndonesia #sukubunga #dolar #ekonomi #beritaekonomi #rangkumindong
```
**TikTok caption:** the same text with only these hashtags: `#rupiah #BIRate #sukubunga #ekonomi #rangkumindong`

**YouTube title:** Rupiah Rp18.046: Besok BI Tahan 5,75% atau Naik ke 6%? #Shorts

**YouTube description:** the IG caption plus the sources list below.

**Tags:** rupiah, BI Rate, Bank Indonesia, suku bunga, dolar, ekonomi, Indonesia

**Sources first comment (pinned)**
```
Sumber:
1. Antara, 19 Okt 2026: rupiah ditutup Rp18.046, JISDOR Rp18.050
2. Bisnis, 4 Jun 2026: rupiah ditutup Rp18.049, terlemah sepanjang masa saat itu; Republika & detikFinance, 4 Jun 2026: tembus Rp18.000; Bisnis & Kontan, 8 Jun 2026: penutupan Rp18.170–18.188
3. Bisnis, 10 Des 2025 & IDX Channel, 9 Mar 2026: puncak krisis 1998 sekitar Rp16.800, rupiah kehilangan >80% nilainya
4. Bisnis, 2 Jul 2020 & Katadata Databoks: Covid, 23 Mar 2020 ditutup Rp16.575
5. Investor Trust & Kontan, 9 Jun 2026: BI-Rate naik ke 5,50% (RDG mingguan)
6. Siaran pers BI, 18 Jun 2026: BI-Rate naik ke 5,75%
7. IDN Financials, 23 Sep 2026: BI-Rate ditahan 5,75% Juli, Agustus, September
8. Kontan & Bank Indonesia, Okt 2026: cadangan devisa US$146,3 miliar (akhir Sep); Investor Trust: inflasi Sep 3,28% yoy
9. CNBC Indonesia, 19 Okt 2026: Citi (via Reuters) soal kenaikan sebagai langkah antisipasi agar arus keluar dari saham tak meluas ke pasar obligasi
10. Bisnis, 17 Okt 2026: ekonom Danamon soal opsi tahan (buying time lewat intervensi); Buletin Finansial, 19 Okt 2026: Bloomberg Economics proyeksi naik ke 6%
Konten edukasi, bukan rekomendasi investasi.
```

## Length
About 84 s (225 spoken words at PART 1's pace), inside the 60–90 s window. If Cahaya runs slower than Pratama and goes past 90 s, cut l4 ("80%") first, then "proyeksi Bloomberg Economics" from the spoken l11 (keep it on screen).

## Trial Reel B?
Probably not worth it. This topic is time-boxed: the video is stale after the decision at ~14:00 WIB tomorrow, so it has a one-day shelf life. A follow-up "hasil RDG" video on 21 Oct is the better use of the budget.

## Open notes for the fact-checker
- "Pertama kali ditutup di atas 18.000": Bisnis calls the 4 Jun close of 18.049 the "terlemah sepanjang masa", and every earlier record (1998, 2020, Apr 2025 Rp17.217 intraday) is below 18.000, so it was the first close above. Kontan's headline "Rupiah pertama kali tembus Rp18.000" (4 Jun) could not be opened.
- The 2026 low is the 8 Jun close, Rp18.170 (Bisnis) to Rp18.188 (Kontan). The script does not claim 19 Oct is a record. After the open, only call it "rekor baru" if the rupiah is above about 18.188.
- **Second October hold source: none found.** I searched again. Liputan6 (Danamon's Hosianna, Woori Saudara, LPEM) and Bloomberg Technoz (LPEM) are both from **August**. The Kontan October hold articles still won't open, and sultramedia is blocked. The hold side is therefore worded "sebagian ekonom, misalnya Danamon", with equal visual weight and no implied consensus.
- The 19 Oct spot close has one outlet (Antara). JISDOR is BI's own reference rate.
- The split rests on Bisnis 17 Okt (hold: Danamon), CNBC/Citi (pre-emptive hike, no level) and Buletin Finansial/Bloomberg Economics (hike to 6%).
