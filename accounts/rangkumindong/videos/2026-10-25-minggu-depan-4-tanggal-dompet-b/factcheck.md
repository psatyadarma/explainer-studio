VERDICT: FIX (3 issues)

Checked 2026-10-25 (MODE=full). Note: the web-fetch safety check was failing for most of this run, so several sources could only be checked from their search-result titles and URLs (marked below). Opened in full: DDTC 1822566, CNBC 28 Sep. pajak.go.id fetch was blocked (permission timeout) and should be opened by hand.

| # | Claim (line) | Verdict | What the sources say | Sensitivity | Source |
|---|---|---|---|---|---|
| 1 | Marketplaces start withholding PPh 22 0,5% on **1 Nov** (r1, r2, captions, calendar "?" reveal) | **FIX** | The draft's sources are the OLDER ones: DDTC 1822566 is dated **18 Sep** (DJP: "Insyaallah 1 November ... sesuai kesiapan platform") and CNBC is dated **28 Sep**. NEWER results say it was brought forward to **1 Oct**: DJP press release **SP-23/2026**, "Pemungutan PPh Pasal 22 melalui marketplace mulai dilaksanakan 1 Oktober 2026" (PDF in pajak.go.id's /2026-10/ folder); DDTC 1822926 "Sah! Pemungutan PPh 22 Marketplace Ternyata Sudah Berlaku Hari Ini" (higher article ID, so later than 1822566); InvestorTrust "DJP Percepatan Proses Pemungutan ... Mulai 1 Oktober 2026"; JawaPos 3 Oct "berlaku mulai 1 Oktober 2026". events.csv E0039 (verified, 19 Oct) agrees. **E0039 is NOT stale. E0289 (1 Nov) is the stale row.** I could not open SP-23 itself; I matched the titles, URLs and dates. | **HIGH** (tax law, sellers' money; it's the reveal) | https://pajak.go.id/id/siaran-pers/pemungutan-pph-pasal-22-melalui-marketplace-mulai-dilaksanakan-1-oktober-2026 ; https://www.pajak.go.id/sites/default/files/2026-10/SP-23_2026%20Pemungutan%20PPh%20Pasal%2022%20melalui%20marketplace%20mulai%20dilaksanakan%201%20Oktober%202026.pdf ; https://news.ddtc.co.id/berita/nasional/1822926/sah-pemungutan-pph-22-marketplace-ternyata-sudah-berlaku-hari-ini ; https://jawapos.com/ekonomi/2610030102/pajak-marketplace-berlaku-mulai-1-oktober-2026 |
| 2 | 0,5% of omzet, Tokopedia/Shopee/Lazada/Blibli | OK | CNBC 28 Sep: 0,5% of gross turnover excl. PPN/PPnBM; the 4 platforms; PMK 37/2025 | high | CNBC 28 Sep |
| 3 | Example Rp10 juta → Rp50 ribu (r3) | OK | 10.000.000 × 0,5% = 50.000; labelled "misalnya" | low | arithmetic |
| 4 | Individuals ≤ Rp500 juta/yr not withheld, with a statement letter (r4) | OK | CNBC: same; turnover counted across all businesses | medium | CNBC 28 Sep |
| 5 | KSPI asks for UMP 2027 announcement on 1 Nov, +7,5–9,5% (t1, t2, hook B) | OK (attribution good) | E0287/E0068: KSPI demand, rallies 15–30 Oct; CNN calls 1 Nov the unions' request. Wording "KSPI minta" / "BURUH MINTA" / "tuntutan, bukan keputusan" is neutral. Not re-fetched this run. | **medium-high** (labour politics) | CNN 22 Okt; Pelita Karawang |
| 6 | Menaker Yassierli has not set a date (t3, hook B) | UNVERIFIED (still current?) | Based on 21 Oct reports (CNN, detik). 4 days old; re-check for a newer Kemnaker statement before posting. | medium (named official) | CNN 21 Okt; detik |
| 7 | Fed decides 28 Oct, FOMC 27–28 Oct (b1) | OK | E0277: Pintu + TradingEconomics. 28 Oct 2026 is a Wednesday. The decision lands early 29 Oct WIB; the visual already says "waktu AS". | low | Pintu News; TradingEconomics |
| 8 | iPhone Duo official sale 30 Oct (Friday), from Rp45,7 juta (b4) | OK | E0290 (verified): sales from 30 Oct; 256 GB Rp45.678.910 → Rp45,7 juta is fine | low | CNBC 23 Okt; CNN 23 Okt |
| 9 | BPS October inflation "sekitar 2 Nov"; Sep 3,28% y/y (b5) | OK (hedged) | Sep 3,28% y/y (Antara; InvestorTrust in E0004). 1 Nov is a Sunday, so Mon 2 Nov is likely but BPS hasn't confirmed it, and "sekitar" covers that. "tertinggi tahun ini" in the caption has one source only. | low | Antara; InvestorTrust |
| 10 | HSC stocks out of IHSG from 2 Nov | n/a (dropped from script) | E0276/E0253: effective 2 Nov 2026 (BEI Peng-00201/BEI.POP/10-2026; CNBC, Tirto, detik). Not in this video, so no stock disclaimer needed. | — | CNBC 23 Okt; Tirto |
| 11 | Photo credit "Foto: Kemendag RI" for Yassierli | UNVERIFIED | Credit names the Trade Ministry for a Manpower Minister photo; check the Commons file page's author field before render. | low | Commons |

## FIX items (exact wording)

**FIX 1 (HIGH): the 1 Nov marketplace reveal is wrong.** Withholding has been running since 1 Oct (SP-23/2026). It doesn't start on 1 Nov. The reveal has to change. Option A (recommended): make 1 Nov the UMP date and keep the tax as a "sudah jalan" line.
- r1: "Yang paling nyentuh dompet? Minggu, 1 November." → keep, but the reveal becomes UMP (t1–t3 move up, with the "permintaan buruh" framing).
- r2: "Ingat juga: sejak 1 Oktober, Tokopedia, Shopee, Lazada, Blibli sudah motong pajak 0,5 persen dari omzet penjual online."
- r3/r4 unchanged.
- t1: "1 November itu tanggal yang ditunggu buruh." (drop "Tapi… juga")
- Hook A/visual: the 1 Nov "?" tile shows "UMP 2027? · BURUH MINTA". Remove the "1 Nov" label from the marketplace receipt sticker.
- Captions: "• Sejak 1 Okt: Tokopedia, Shopee, Lazada, Blibli sudah memungut PPh 22 0,5% dari omzet penjual online (DJP, SP-23/2026). ..." Sources 1–3: replace with the pajak.go.id SP-23/2026 link and DDTC 1822926.
- Option B: if the user can show a DJP statement dated after 1 Oct that pushes it back to 1 Nov, keep the script and cite that statement. I found none.

**FIX 2: knowledge base.** Don't mark E0039 as superseded. Mark **E0289** as superseded by E0039 (its sources are dated 28 Sep, before SP-23).

**FIX 3: currency of t3.** Re-check that Kemnaker still hasn't announced a UMP 2027 date (newer than 21 Oct). If it has, t3 becomes "Menaker Yassierli: [tanggal], menurut Kemnaker."
