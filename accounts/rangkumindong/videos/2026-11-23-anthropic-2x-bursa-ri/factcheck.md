VERDICT: FIX (2 issues)

Checked 23 Nov 2026 (MODE=full). Max sensitivity: **low** (market/business topic, no politics, law or allegations; disclaimer present on screen and in captions).

| # | Claim | Verdict | What the source says | Source |
|---|---|---|---|---|
| h1 | "Perusahaan pria ini nilainya dua kali bursa Indonesia" | OK | ~Rp20.000 T at the IPO price vs BEI Rp9.047 T (13/11) = ~2,2x. Also true at the day-one close (~US$1,28 T basic, per FourWeekMBA). The "di harga IPO" qualifier is on screen and in captions | detikFinance d-8760676 |
| l1 | Dario Amodei, bos Anthropic, pembuat Claude | OK | AP names Amodei as CEO | nbcwashington.com/.../4185456/ |
| l2 | Kamis 19 Nov, debut di Nasdaq, ticker ANT | OK | 19 Nov 2026 is a Thursday. Nasdaq Global Select, ticker ANT | TradingView/Invezz; detikFinance |
| l2 | Harga perdana US$83 (range 70-78) | OK | ABC and detik both say US$83, above the US$70-78 range. Note: the AP/NBC page also says "$82" in one spot, which conflicts with its own figures. Don't rely on AP for the IPO price (the draft doesn't) | abcnews.com/...?id=138245320 |
| l3 | ~US$1,1 T ≈ Rp20.000 T | OK | detik: "sekitar US$1,1 triliun", "sekitar Rp20.000 triliun" at JISDOR Rp18.252 (18 Nov). Check: 13,22 bn shares x 83 = US$1,097 T, and x 18.252 = Rp20.030 T | detikFinance; FourWeekMBA |
| l4 | Semua saham BEI Rp9.047 T; "dua kali lipat lebih" | **FIX** | The figure is right for 13 Nov, but it is stale and **spoken without a date**. BEI cap fell to **Rp8.725 T (20 Nov)**. Today's figure makes the ratio 2,29x, so the claim still holds. The 13 Nov date only appears in a small on-screen label | detikFinance d-8763001 |
| l5 | Hari pertama ditutup naik 17% | OK | Close US$97,17 = +17,1% vs US$83 (AP, Invezz, FourWeekMBA). Historical, fixed | TradingView/Invezz; FourWeekMBA |
| l6 | Nilai perdana ≈ 84% ekonomi Indonesia setahun | OK | detik: ~84% of 2025 PDB Rp23.821,1 T (BPS, current prices). 20.000/23.821 = 84% | detikFinance d-8760676 |
| visual | On-screen numbers that are never spoken: US$97,17 (l5), "2,2x" (l4), "Rp23.821 T" (l6), "Rp18.252" (l3 chip) | **FIX** (minor) | Each figure is correct. The rule says to flag on-screen numbers that aren't spoken. The ones that matter are the big labels US$97,17 and 2,2x | n/a |
| photo | Dario Amodei, TechCrunch Disrupt 2023, CC BY 2.0 | OK | Commons API: Artist TechCrunch, licence CC BY 2.0. Note: `assets/people/dario-amodei.*` was not found in the repo `assets/people/`, so the producer should confirm the download | commons.wikimedia.org File:Dario_Amodei_at_TechCrunch_Disrupt_2023_02.jpg |
| captions | IG/TikTok/YT text vs script | OK | Numbers match the script. "Bukan ajakan jual/beli saham" is present in every caption and on screen from l4 | post.json |

## FIX wording

**1. l4 (BEI cap is stale and has no spoken date).** Preferred option: use the latest figure.
- text: `Semua saham di Bursa Efek Indonesia, per 20 November? Rp8.725 triliun. Dua kali lipat lebih.`
- say: `Semua saham di Bursa Efek Indonesia, per dua puluh November? Delapan ribu tujuh ratus dua puluh lima triliun rupiah. Dua kali lipat lebih.`
- On-screen label: "Semua saham BEI · 20 Nov", bar ratio 20.000 : 8.725, ruler "2,3x". In the captions/YT description, change "2,2x kapitalisasi BEI Rp9.047 T (13 Nov)" to "~2,3x kapitalisasi BEI Rp8.725 T (20 Nov)".
- Minimal option (keeps detik's comparison): text `Semua saham di Bursa Efek Indonesia, pekan lalu? Rp9.047 triliun. Dua kali lipat lebih.`, say `... pekan lalu? Sembilan ribu empat puluh tujuh triliun rupiah. ...`

**2. Unspoken on-screen numbers.**
- l5 text: `Tapi itu baru harga perdana. Hari pertama, sahamnya ditutup 97 dolar, naik 17 persen.`, say `... ditutup sembilan puluh tujuh dolar, naik tujuh belas persen.`
- l4: either say "dua koma tiga kali" in place of "dua kali lipat lebih", or make the ruler read "2x lebih" so screen and voice match.
- The Rp23.821 T and JISDOR chips can stay as small source labels.

## Note (not a factual error, the user's call)
The draft was written by Claude (an Anthropic product) about Anthropic. The script is factual and balanced. The user may want to consider a disclosure. The draft's Notes already raise this.
