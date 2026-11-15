VERDICT: FIX (2 issues)

Checked 15 Nov 2026 (MODE=full).

| Claim | Verdict | What the source says | Source |
|---|---|---|---|
| m1 Gibran resigned 12 Nov, seat vacant | OK (not re-opened: CNN Indonesia / Liputan6 fetch blocked by permission timeout; consistent with IDN Times and Okezone 13 Nov) | - | cnnindonesia.com/nasional/20261112101220-32-1426208 |
| m2 "Kata Ketua MPR Ahmad Muzani, paripurna ... Rabu, 2 Desember" | OK wording / FIX source | IDN Times quotes Muzani directly: "akan dilaksanakan pada hari Rabu tanggal 2 Desember 2026 di Gedung Senayan ini." Kontan does NOT quote Muzani on the date (only says the joint MPR meeting set it; his quote is about sending the letter to the President). Kompas.com blocked. | https://www.idntimes.com/news/indonesia/mpr-tunggu-2-nama-calon-wapres-pengganti-gibran-dari-presiden-pekan-depan-00-xvwcc-dg2mvg |
| m3/m3b 2 names at least 14 days before, so about Wed 18 Nov | OK | Okezone + IDN Times: Pasal 136 Peraturan MPR 1/2024, deadline 18 Nov; Muzani "Insyaallah" next week | news.okezone.com/read/2026/11/13/337/3253892 |
| m4 Prabowo at ASEAN Summit Manila, "lalu ke China" | OK | ANTARA: arrived Manila 14 Nov, KTT ke-49 ASEAN 15-17 Nov. China leg now independently supported: Katadata (11 Nov) says APEC 2026 is in Shenzhen, China, 18-19 Nov and Prabowo will meet Xi there; Okezone sidebar "Usai KTT APEC di Tiongkok". Note: he is in China on 18 Nov itself. | https://www.antaranews.com/berita/5854707/presiden-prabowo-tiba-di-manila-filipina-untuk-hadiri-ktt-ke-49-asean ; https://katadata.co.id/berita/nasional/6af4492c05b53/prabowo-akan-bertemu-xi-jinping-di-ktt-apec-pekan-depan |
| m5 "Kata Kompas, nama dibahas sepulangnya" | UNVERIFIED | Kompas.id robots-blocked; only the headline ("Sepulang dari Filipina dan China, Prabowo segera bahas usulan cawapres...") is seen. Wording is attributed and hedged ("Belum pasti"), so acceptable as is; no second source found. | kompas.id/artikel/sepulang-dari-filipina-dan-china-... |
| b1 BI announces Wed 18 Nov | OK | investor.id: RDG Rabu 18 November 2026; Newsquawk and Vibiznews: BI decision Wednesday of 16-20 Nov week | https://investor.id/market/461908/prediksi-ihsg-dan-rekomendasi-saham-senin-16-november-2026 |
| b2 Now 5.75%, analysts expect +0.25 to 6% | OK | BI: held 5.75% at 20-21 Oct RDG. investor.id: "berpeluang menaikkan BI Rate sebesar 25 bps menjadi 6%"; Vibiznews: "diperkirakan naik 25 bps" | bi.go.id (BI-Rate Held at 5.75 percent); investor.id above |
| b3 Rupiah Fri close Rp18.190 | OK (single source) | Vibiznews: "berakhir melemah 87 poin atau 0,48% ke level Rp18.190 per USD". No second source for 13 Nov close found (Bisnis/Kontan/CNBC searches return up to 11 Nov). Re-check before render. | https://vibiznews.com/index.php/2026/11/14/variatif-ihsg-uptrend-rupiah-rekor-terendah-bi-rate-akan-naik-domestic-market-outlook-16-20-november-2026/ |
| b3b "Sempat tembus Rp18.245. Terlemah sepanjang sejarah." | OK (single source) | Vibiznews: "sempat mencapai level terendah harian sepanjang sejarah di Rp18.245/USD" (intraday) | Vibiznews above |
| b4 KPR "bisa" ikut naik | OK | conditional, flagged as perkiraan | cnbcindonesia.com/news/20261103104715-4-781813 |
| n1 Nvidia reports; first since Huang resigned as CEO | OK | Nvidia IR: call Tue 17 Nov 2026, 2 pm PT / 5 pm ET, quarter ended 25 Oct. SEC 8-K: Huang resigned as President, CEO and director 12 Nov 2026, effective immediately; Colette Kress interim CEO | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/ ; https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm |
| Captions + draft Z4 card: Nvidia call "sekitar 07:00 WITA Rabu" | FIX | 5 pm ET on 17 Nov is EST (UTC-5, DST ended 1 Nov) = 22:00 UTC = **06:00 WITA** Wed 18 Nov, not 07:00. Script line "Rabu pagi" is fine. | Nvidia IR above |
| n2 Fed minutes "Kamis dini hari" WITA | OK | Fed calendar: minutes of 27-28 Oct meeting released 18 Nov, 2:00 pm (ET) = 19:00 UTC = 03:00 WITA Thu 19 Nov | https://www.federalreserve.gov/newsevents/2026-november.htm |
| n3 Market expects Fed hike 9 Dec | OK | Newsquawk: money markets "fully price a 25bps increase" (~10% chance of 50bp); next FOMC 9 Dec; range 3.75-4.00% | newsquawk.com week-in-focus 16-20 Nov |
| Disclaimer "Bukan ajakan jual/beli saham" | OK | in script, captions, on-screen strip b1-n3 | - |

## FIX 1: Nvidia call time (post.json caption, youtube_description, tiktok_caption; draft.md captions x3 and Z4 card)
Replace `(paparan sekitar 07:00 WITA Rabu)` with `(paparan sekitar 06:00 WITA Rabu)`.
Replace card `±07:00 WITA Rabu` with `±06:00 WITA Rabu`.

## FIX 2: Source for Muzani's 2 Des quote (m2) (post.json youtube_description + pinned_comment; draft.md sources lists)
Kontan does not quote Muzani on the date. Replace source 2 with:
`2. Muzani: paripurna wapres baru Rabu 2 Desember (IDN Times, 13 Nov) https://www.idntimes.com/news/indonesia/mpr-tunggu-2-nama-calon-wapres-pengganti-gibran-dari-presiden-pekan-depan-00-xvwcc-dg2mvg`
Suggested addition for the China leg: `Prabowo akan bertemu Xi di KTT APEC Shenzhen (Katadata, 11 Nov) https://katadata.co.id/berita/nasional/6af4492c05b53/prabowo-akan-bertemu-xi-jinping-di-ktt-apec-pekan-depan`

## Open (not FIX)
- "dibahas sepulangnya" rests on the Kompas.id headline only. Keep the "Kata Kompas" attribution and "Belum pasti".
- Rupiah Rp18.190 / Rp18.245 single source (Vibiznews); re-check before render.
