# Draft: 4 tanggal minggu ini, mana yang nyentuh dompetmu? (Minggu 25 Okt 2026)

**Topic + angle:** Sunday "Minggu Depan" Short. It walks through 4 dates (28 Okt, 30 Okt, sekitar 2 Nov, 1 Nov) and holds back the answer: **1 November**, the date the unions (KSPI) **asked for** the UMP 2027 announcement (labelled "BURUH MINTA"; per 21 Okt the Menaker had not announced a date). The turn: the marketplace PPh 22 0,5% **is already running since 1 Okt** (DJP SP-23/2026).
**Arm:** voice Pratama · 19:00 · hook A question_reveal · hook B person_collage (Yassierli) · subs word · format minggu_depan. Pick: idea #1, default pick at 14:00 (not the user's choice).
**Length:** 147 spoken words ≈ 59 s + tail ≈ **61 s**. Turn at ~70%.
**Storyline:** new (touches ump-2027, ecommerce-seller-rules, consumer-health). No PART badge.
**Fact-check rework (factcheck.md, FIX ×3):** (1) the marketplace tax started 1 Okt, not 1 Nov, so the reveal is now the UMP date and the tax moved to the turn as "sudah jalan duluan"; the "4 tanggal" count still holds (28, 30, 1, 2). (2) E0289 marked superseded by E0039 in events.csv, events.md re-rendered. (3) Menaker phrased as "Per 21 Oktober … belum umumkan". Hook B wording adjusted from the critic's PICK B for FIX 3 (same idea, "buruh minta" kept on screen).

## Script (subtitle text)
| id | line |
|---|---|
| h1 | 4 tanggal minggu ini. Mana yang nyentuh dompetmu? |
| h2 | Jawabannya di akhir. |
| rd | Rangkumin dong! |
| b1 | Rabu, 28 Oktober, The Fed putuskan suku bunga Amerika. |
| b4 | Jumat, 30 Oktober, iPhone Duo resmi dijual. Mulai Rp45,7 juta. |
| b5 | Sekitar 2 November, BPS rilis inflasi. September: 3,28 persen. |
| r1 | Yang paling nyentuh dompet? Minggu, 1 November. |
| u1 | Itu tanggal yang buruh minta buat pengumuman UMP 2027. |
| u2 | KSPI minta naik 7,5 sampai 9,5 persen. |
| u3 | Per 21 Oktober, Menaker Yassierli belum umumkan tanggalnya. |
| t1 | Tapi ada yang sudah jalan duluan. |
| t2 | Sejak 1 Oktober, Tokopedia, Shopee, Lazada, Blibli motong pajak 0,5 persen dari omzet penjual online. |
| r4 | Perorangan beromzet sampai Rp500 juta setahun? Tidak dipotong. |
| cta | Mana yang paling kerasa buat kamu? Komen ceritamu! |
| end | Follow Rangkumin Dong, biar nggak ketinggalan! |

**Hook A (PICK A, hooks.md #1):** h1 + h2 above.
**Hook B (person_collage, from PICK B, replaces h1+h2):** "UMP 2027 naik berapa? Buruh minta diumumkan 1 November." / "Per 21 Oktober, tanggalnya belum diumumkan." (15 words).

## Visual plan
- **Zone 0, hook A (0–5 s):** big 2-line title card **"4 TANGGAL / 1 DOMPET"**, held ~3 s = cover. 4-tile calendar strip (28 · 30 · 1 · 2) pops in tile by tile (~1 s each); the **1 Nov tile is covered by a yellow "?" sticker**. A wallet sticker wobbles. No logo intro.
- **Zone 0, hook B:** collage look (tests/hook-collage): **Yassierli cut-out** on the paper ledge, name tag "Yassierli · Menteri Ketenagakerjaan", label bar "UMP 2027 / NAIK / BERAPA?", calendar sticker "1 NOV? · BURUH MINTA" flying in with a callout arrow, small tag "per 21 Okt: belum diumumkan". A generic protest-sign sticker "UMP NAIK" (no union logo). Photo credit small on screen.
- **Zone 1, 28 Okt (b1):** tile "28". Flat bank-building icon with a US flag pin, label "The Fed · putuskan suku bunga · 27–28 Okt (waktu AS)". No rupiah forecast arrows.
- **Zone 2, 30 Okt (b4):** tile "30". Generic phone sticker (no Apple logo/product render), price tag counting up to **Rp45,7 juta** "termurah, 256 GB".
- **Zone 3, ~2 Nov (b5):** tile "2" with a small "sekitar" tag. Basket icon + counter **3,28%** "inflasi Sep (y/y), BPS".
- **Zone 4, reveal 1 Nov (r1–u3):** the "?" peels off the 1 Nov tile → **"UMP 2027? · BURUH MINTA"**. Range bar 7,5% → 9,5% labelled "tuntutan KSPI, bukan keputusan". **Yassierli cut-out** (same size/style as hook B) with name tag and a tag "per 21 Okt: tanggal belum diumumkan" (not a quote, no quote marks).
- **Zone 5, turn (t1–r4):** camera pulls back to a tile *before* the strip: **"1 OKT · SUDAH JALAN"** with a stamp effect. 4 marketplace names as plain text chips (no logos), "PPh 22 · 0,5% dari omzet". No "1 Nov" anywhere on the tax visuals. Then a green shield badge: "Perorangan ≤ Rp500 juta/tahun: tidak dipotong (asal ada surat pernyataan)".
- **CTA + end card:** all tiles side by side, comment-bubble sticker; end card with sources + photo credit.
- Subs: word mode (y 1290). Safe area x 60–920, y 240–1480; check with engine/safezone.py.
- **Real people:** Yassierli only (File:Yassierli, Menteri Ketenagakerjaan (2024).jpg; public domain; Commons author field: Kementerian Perdagangan Republik Indonesia; 408×607, so keep it ≤ ~600 px tall). The download is still waiting out Commons' rate limit, so assets/people/yassierli.png **does not exist yet**; check it before render. If it never lands, hook B falls back to the next style and the body keeps a name tag. KSPI is named as an organisation only, no face.

## Fact notes
- Marketplace tax: since 1 Okt per DJP SP-23/2026 (factcheck.md; SP-23 itself couldn't be opened, matched by title/URL). E0289 (1 Nov) is superseded.
- UMP: 1 Nov = KSPI's request; Menaker per 21 Okt gave no date. Re-check for a newer Kemnaker statement before posting (web search was down during the rework).
- BPS October release "sekitar 2 November" (1 Nov is a Sunday).
- Dropped for length: Fed odds, the Rp10 juta → Rp50 ribu example, Sumpah Pemuda, the HSC stocks (covered 24 Okt). No stock line left, so no "Bukan ajakan jual/beli saham" needed.

## Captions
**IG caption**
```
4 tanggal minggu ini. Mana yang nyentuh dompetmu? 🗓️

Rangkumin dong 👇
• 28 Okt: The Fed putuskan suku bunga Amerika. 30 Okt: iPhone Duo resmi dijual, mulai Rp45,7 juta. Sekitar 2 Nov: BPS rilis inflasi Oktober (September 3,28% y/y).
• 1 Nov: tanggal yang diminta buruh (KSPI) untuk pengumuman UMP 2027, dengan tuntutan naik 7,5–9,5%. Itu permintaan buruh, bukan jadwal resmi; per 21 Okt, Menaker Yassierli belum mengumumkan tanggalnya.
• Yang sudah jalan: sejak 1 Okt, Tokopedia, Shopee, Lazada, Blibli memungut PPh 22 0,5% dari omzet penjual online (DJP, SP-23/2026). Penjual perorangan beromzet sampai Rp500 juta/tahun tidak dipotong, asal serahkan surat pernyataan.

Mana yang paling kerasa buat kamu? Komen ceritamu 👇

Sumber di komentar.

#minggudepan #UMP2027 #pajakmarketplace #inflasi #jualanonline #beritaekonomi #rangkumindong
```
**YouTube title:** 4 Tanggal Minggu Ini: Mana yang Nyentuh Dompetmu? #Shorts
**YouTube description:** IG caption + sources list below.
**Tags:** minggu depan, UMP 2027, pajak marketplace, PPh 22, inflasi, The Fed, iPhone Duo, jualan online, berita ekonomi
**TikTok caption:** IG caption with `#UMP2027 #pajakmarketplace #jualanonline #beritaekonomi #rangkumindong`

**Sources (pinned first comment)**
```
Sumber:
1. DJP, siaran pers SP-23/2026: pemungutan PPh 22 melalui marketplace mulai 1 Oktober 2026 https://pajak.go.id/id/siaran-pers/pemungutan-pph-pasal-22-melalui-marketplace-mulai-dilaksanakan-1-oktober-2026
2. DDTC News: pemungutan PPh 22 marketplace sudah berlaku https://news.ddtc.co.id/berita/nasional/1822926/sah-pemungutan-pph-22-marketplace-ternyata-sudah-berlaku-hari-ini · JawaPos, 3 Okt 2026 https://jawapos.com/ekonomi/2610030102/pajak-marketplace-berlaku-mulai-1-oktober-2026
3. CNBC Indonesia, 28 Sep 2026 (tarif 0,5%, 4 platform, batas Rp500 juta) https://www.cnbcindonesia.com/news/20260928115107-4-771409/empat-e-commerce-mulai-pungut-pajak-per-1-november
4. CNN Indonesia, 22 Okt 2026: tuntutan buruh UMP 2027 naik hingga 9,5% https://cnnindonesia.com/ekonomi/20261022163811-92-1418495/pengusaha-respons-tuntutan-buruh-ump-2027-naik-hingga-95-persen
5. Pelita Karawang: KSPI jelang 1 November https://www.pelitakarawang.com/2026/10/jelang-penetapan-1-november-2026-kspi.html
6. CNN Indonesia, 21 Okt 2026: Menaker, formula UMP 2027 mengacu UU baru (tanpa tanggal) https://cnnindonesia.com/ekonomi/20261021205702-92-1418188/menaker-formula-ump-2027-mengacu-uu-baru · detikFinance https://finance.detik.com/berita-ekonomi-bisnis/d-8717972/bocoran-penetapan-formula-ump-2027
7. Antara: BPS catat inflasi September 2026 3,28% https://sultra.antaranews.com/berita/542064/bps-catat-inflasi-ri-328-persen-pada-september-2026
8. Pintu News: FOMC 27-28 Oktober https://pintu.co.id/news/295280-fomc-27-28-oktober-2026-peluang-fed-naikkan-bunga-oktober-sempat-tembus-50-kini-sekitar-32
9. CNBC Indonesia, 23 Okt 2026: harga iPhone Duo di RI, dijual 30 Okt https://www.cnbcindonesia.com/tech/20261023124542-37-778889/harga-iphone-duo-di-ri-tembus-rp75-juta-preorder-buka-langsung-ludes · CNN Indonesia https://www.cnnindonesia.com/teknologi/20261023113349-206-1418737/daftar-harga-iphone-duo-di-indonesia-tembus-rp75-juta
Foto Yassierli: Kementerian Perdagangan Republik Indonesia, public domain, via Wikimedia Commons (File:Yassierli, Menteri Ketenagakerjaan (2024).jpg).
```

## Trial Reel B?
Yes, it's the scheduled daily A/B (person_collage vs question_reveal). It depends on yassierli.png landing; only h1/h2 change.

**Build log (producer, 25 Okt ~14:45 WITA):** yassierli.png never landed (background download + one producer retry both hit Commons 429). Fallback per playbook: **B = person_collage without a face → name tag** ("YASSIERLI · Menteri Ketenagakerjaan" label in the collage look, no photo); log the B arm as `person_collage (fallback: name tag, no licensed face)`, not a clean person_collage test. The A body (u3) also shows a name card instead of the cut-out, and no photo credit is shown. index.html switches to the cut-out automatically if assets/people/yassierli.png appears and the videos are re-rendered.
Voice timing note: tts_eleven's word timings came out ~0.8 s late for both A and the B opening (alignment bug); subtitle timings were re-derived from ElevenLabs speech-to-text (build/timing.orig.json kept). qa_sync A: PASS (median −80 ms).
