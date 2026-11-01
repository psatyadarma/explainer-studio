VERDICT: FIX (3 issues)

Checked 1 Nov 2026 (MODE=full). Script, hook B, on-screen plan and captions checked.

| Claim (lines) | Verdict | What the source actually says | Source |
|---|---|---|---|
| "Kamis malam, 29 Oktober" (l1, hb1, hb2, visual header, captions) | FIX | Katadata: "Kamis (29/10)", no time of day. TFTC: outflows 29 Oct, ~20:24–21:04 **UTC**. The Block (US): withdrawal halt "later Thursday night" in **US time**. In WIB that is **Jumat 30 Okt, ~03:24–04:04 dini hari**. "Kamis malam" is only true in US/UTC time, so it is wrong for an Indonesian audience. | katadata.co.id/…/bursa-kripto-binance-dibobol-aset-rp114-3-triliun-lenyap ; tftc.io/binance-suspected-hack-5-billion-outflows-stablecoin-freeze ; theblock.co/news/markets/2026-10-29-binance-investigating-hack-suspicious-outflows-5-billion-432171 |
| US$6,3 M ≈ Rp114 T (h1, l2, hb2) | OK | Katadata: US$6,3 M = Rp114,3 T at Rp18.140. Warta Ekonomi: total impact US$6,3 M. CNBC: TRM US$6,36 M, Chainalysis ~US$6,4 M (Rp104 T at Rp16.500). The caption explains the exchange-rate difference. | Katadata ; wartaekonomi.co.id/read644596 ; CNBC Indonesia |
| 10 blockchain, kebanyakan ~20 menit (l3) | OK | CNBC (TRM): 10 blockchain networks, "sebagian besar … sekitar 20 menit". Katadata: ~20 menit. | CNBC ; Katadata |
| "Awalnya, kata Binance: laptop developer yang diretas" (l4) | OK (3 sources) | Katadata (citing Reuters): Binance's initial investigation points to a compromised developer laptop. Warta Ekonomi: "laptop milik seorang engineer DevOps yang telah dikompromikan". TFTC says the same, and adds that Teng later said it was "not a single one-click action" by one engineer. "Awalnya" covers that later caveat. | Katadata ; Warta Ekonomi ; TFTC |
| TRM Labs & Chainalysis menduga TraderTraitor, Korea Utara (l5) | OK, attributed | CNBC: TRM has "high confidence" in the TraderTraitor link, and Chainalysis' Levin says it was "kemungkinan" TraderTraitor. Warta: TRM. Katadata: US analysis firms "menduga" North Korea (TraderTraitor not named). The line is attributed and not stated as fact. Update: the FBI attributed the attack to North Korea on 31 Oct (TFTC; Investortrust also mentions the FBI). Adding it is optional (see note). | CNBC ; Warta Ekonomi ; TFTC ; Investortrust |
| Binance belum menunjuk pelaku (l6) | OK | Katadata: Teng says the investigation has not yet assigned responsibility to anyone. | Katadata |
| Binance janji tanggung semua kerugian (l7) | OK | Teng on X: "Uang Anda aman dan kami menanggung setiap kerugian" (Katadata). Yi He said the same (The Block). | Katadata ; The Block |
| ~US$3 M dibekukan (l7) | OK | Katadata, CNBC and Warta: ~US$3 M frozen (Binance security update). | Katadata ; CNBC ; Warta |
| Dibekukan ≠ balik; proses hukum, berbulan-bulan sampai tahunan (l8) | OK (single outlet, two named experts) | CNBC: Redbord (TRM) says return happens through legal process. Jardine (Chainalysis) says "berbulan-bulan hingga bertahun-tahun". | CNBC |
| ~US$3,3 M "belum jelas" / "lebih dari separuhnya belum jelas" (h2, l10) | FIX (wording + missing update) | Katadata: US$3,3 M with "belum ada kejelasan lebih lanjut". CNBC: Fundstrat (Sean Farrell) estimates ~US$3,3 M "belum berhasil dibekukan". This is about the **stolen funds** (frozen vs not frozen). **Investortrust 1 Nov** says Binance "berhasil **menutup** 95% dari total aset US$6,3 miliar yang dicuri" and resumed withdrawals in phases on 1 Nov (06:00–09:00 GMT, BTC/ETH/BNB/SOL/XRP/DOGE etc.). "Menutup" means **covering** user losses (Binance making users whole), not recovering money from the hackers. So it does **not** contradict the 3,0/3,3 split of the stolen money. But h2 and l10, as worded ("lebih dari separuhnya belum jelas"), now suggest users' money is uncertain, which is out of date for "Uangmu aman?". The 95% figure is single-source with no primary Binance statement found, so do not use the number. Phased withdrawals are relevant to viewers and should be mentioned. | Katadata ; CNBC ; investortrust.id/market/121172/… |
| Binance stop deposit & withdrawal (hb1 basis) | OK | Katadata, Warta and The Block: deposits and withdrawals were suspended. Timing: Thursday night US time = Friday morning WIB. | Katadata ; Warta ; The Block |
| 22,4 juta akun kripto, OJK, Mei 2026 (l11) | OK | detikFinance 7 Jul: 22,4 juta *akun konsumen* per Mei 2026, Adi Budiarso, OJK. These are accounts, not people, and the script says "akun". | finance.detik.com/fintech/d-8564372/… |
| OJK: tidak ada rush; pakai berizin & diawasi OJK (l12) | OK | Investortrust: Adi Budiarso: "Tidak ada rush"; "Gunakan penyelenggara yang berizin dan diawasi OJK". | Investortrust |
| Disclaimer | OK | "Bukan ajakan jual/beli aset kripto" is on screen in zones 3–4 and in all captions. | — |

## FIX 1: date and time (l1, hook B, header card, captions)
- **l1** text: `Jadi gini. 29 Oktober, Binance dibobol.` · say: `Jadi gini. Dua puluh sembilan Oktober, Binance dibobol.`
  (or, if you want the time of day: `Jumat dini hari, 30 Oktober waktu Indonesia, Binance dibobol.`)
- **Header card:** `29 Okt 2026 · waktu AS` (or `Jumat dini hari · 30 Okt WIB`). Drop "Kamis malam".
- **hb1:** `Jumat pagi, Pak Budi mau tarik kripto. Nggak bisa.`
- **hb2:** `Beberapa jam sebelumnya, Rp114 triliun lenyap dari Binance.` · say: `Beberapa jam sebelumnya, seratus empat belas triliun rupiah lenyap dari Binance.`
- **Captions (IG/YT/TikTok):** `• Kamis malam 29 Okt, Binance dibobol:` → `• 29 Okt (waktu AS), Binance dibobol:`

## FIX 2: say whose money is unclear (h2, l10, visual bar, captions)
- **h2:** `Lebih dari separuh uang curiannya, sampai sekarang belum ketahuan di mana.`
- **l10:** `Dan sisanya, sekitar 3,3 miliar dolar, belum berhasil dibekukan.` · say: `Dan sisanya, sekitar tiga koma tiga miliar dolar, belum berhasil dibekukan.`
- **Visual bar label:** `3,3 · belum dibekukan` (instead of "belum jelas").
- **Captions:** `~US$3,3 M belum jelas.` → `~US$3,3 M uang curian belum berhasil dibekukan.`

## FIX 3: add the 1 Nov withdrawal update (new line after l10, plus captions)
- **l10b** (new) [reassuring]: `Kabar terbarunya: mulai 1 November, Binance buka lagi penarikan, bertahap.` · say: `Kabar terbarunya: mulai satu November, Binance buka lagi penarikan, bertahap.`
- **Captions**, appended to the third bullet: `Per 1 Nov, Binance mulai buka penarikan secara bertahap.`
- Do NOT use "95%" on screen or in the voice-over. It is single-source (Investortrust), its meaning ("menutup") is unclear, and no primary Binance statement was found. Add a source line: `6. Investortrust, 1 Nov 2026: Binance mulai buka penarikan bertahap 1 Nov` (same URL as source 4).

## Notes (no change required)
- l5 is correctly attributed. Optional, stronger and current: `FBI, juga TRM Labs dan Chainalysis, mengaitkannya dengan TraderTraitor, kelompok sokongan Korea Utara.` Use it only if a second outlet for the FBI 31 Oct statement is confirmed (TFTC plus a passing mention in Investortrust so far). l6 stays.
- Caption source 1 lists "10 blockchain", but Katadata does not state that; it comes from CNBC (source 2). The caption already credits CNBC for it, so no change is needed.
