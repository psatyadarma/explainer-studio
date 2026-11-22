VERDICT: FIX (3 issues)

MODE=light: hook and why-now claims only.

| Claim | Verdict | What the source says | Source |
|---|---|---|---|
| #1 Anthropic nilai pasar ~2x BEI (US$1,1 T ~ Rp20.000 T vs Rp9.047 T) | OK, with caveat | detik: ~US$1,1 T (~Rp20.000 T) at the IPO price, excludes options/RSU, fully diluted ~US$1,5 T; ~84% of 2025 GDP. 20.000/9.047 = 2,2x; against Rp8.725 T it is 2,29x. | https://finance.detik.com/bursa-dan-valas/d-8760676/harga-ipo-anthropic-resmi-us-83-per-saham-nilai-pasarnya-84-pdb-ri |
| #1 IPO US$83, ~US$81,3 M (~Rp1.485 T) | OK | detik: US$83 (range 70-78), US$81,34 M, Rp1.484,6 T | same |
| #1 Why-now: debut Nasdaq ANT, close US$97,17 (+17,1%) | OK | Multiple outlets (TradingView/Invezz, technology.org 20 Nov) report close US$97,17, +17%. 97,17/83 = +17,1%. The ABC/detik pages for it were not opened. | https://www.tradingview.com/news/invezz:f1a2ad0a9094b:0-anthropic-s-ant-closes-at-97-17-up-17-on-its-first-day-of-trading/ |
| #2 IHSG -3,71% (5.344,41 -> 5.146,33), kapitalisasi Rp9.047 T -> Rp8.725 T (-Rp322 T) | OK | detik: same figures; cap -3,56% | https://finance.detik.com/bursa-dan-valas/d-8763001/modal-asing-rp-100-triliun-keluar-dari-pasar-modal-ri |
| #2 Title "asing kabur Rp100 triliun setahun" | FIX | Source says net sell Rp100,235 T "sejak awal 2026" (year to date), not a 12-month period. | same |
| #2 asing net jual Jumat 20 Nov Rp947,41 M | OK | matches | same |
| #3 Cikande: 3 tewas, 36 hilang, 7 kantong jenazah; hook "puluhan pekerja belum ditemukan" | UNVERIFIED | CNN pages blocked (WebFetch permission not granted). Hook "puluhan belum ditemukan" may be stale because 6-7 body bags were evacuated after the 3 tewas / 36 hilang figure. | https://www.cnnindonesia.com/nasional/20261122151116-20-1430085/update-kebakaran-pabrik-permen-cikande-7-kantong-jenazah-dievakuasi |
| #4 Kapolda Bengkulu: sujud 19 Nov, telegram 20 Nov, diumumkan 22 Nov | UNVERIFIED | CNN page blocked; dates from headlines only. Writer already hedges on causation ("usai viral"). | https://www.cnnindonesia.com/nasional/20261122153044-20-1430091/irjen-yudhi-dimutasi-dari-kapolda-bengkulu-usai-viral-aksi-sujud |
| #5 UMP DKI Rp6.136.941, tenggat UMK 25 Nov | not checked (not in a read source this run) | | |

## FIX
1. **Ranking vs rubric (writer.md: "rank mainly by score; topic only breaks near-ties within 1 point").** Scores recompute correctly with weights (wallet 0,5; surprise 1,25; x12/11,5): #1 = 9,39 -> 9, #2 = 10, #3 = 10, #4 = 9,91 -> 10, #5 = 7,57 -> 8. So #1 is within 1 point, but the topic tie-break does not help it, because #2 (IHSG) is also Senin market/economy and scores higher. Under the rule #2 should rank first and carry the star. The only defensible reason to keep #1 is the face rule (person_collage prefers a clear face, Amodei vs none for #2). If kept, say that reason in "Kenapa ⭐" (currently it cites topic fit and a 1-point gap), or reorder with #2 as #1 and star it.
2. #2 title: replace "asing kabur Rp100 triliun setahun" with "asing jual bersih Rp100 triliun sejak awal 2026".
3. #1 "Kenapa sekarang" caveat: add "US$1,1 T = nilai di harga IPO; CNN melaporkan ~US$1,76 T setelah penutupan hari pertama", so the "2x BEI" claim names its basis (IPO price, tanggal BEI).
Also: #3 hook is at risk of being stale ("puluhan belum ditemukan" vs 6-7 jenazah); re-check before use.
