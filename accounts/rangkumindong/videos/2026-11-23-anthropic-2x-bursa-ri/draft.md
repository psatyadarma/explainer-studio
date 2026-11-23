# Draft · Senin 23 Nov 2026 · Anthropic bernilai 2 kali seluruh bursa Indonesia. Segede apa itu?
**Hook-critic PICK A:** "Perusahaan pria ini nilainya dua kali bursa Indonesia." (h1; no hook_b)
**Arm:** Pratama · 19:00 WITA · hook person_collage (no B) · subs block · format **short** · ~110 spoken words + tagline, **~45 s**
**Topic + angle:** Anthropic's Nasdaq IPO (19 Nov), told as a scale story ("segede apa?"): value at the IPO price vs all of BEI, then the held-back payoff (≈84% of Indonesia's GDP in one year).
**Which valuation (fact-check flag):** the video uses **only the IPO-price value, US$1,1 T (~Rp20.000 T)** from detikFinance, against BEI Rp8.725 T on 20 Nov (spoken with its date; fact-check FIX 1) → ~2,3x. detik's own comparison used Rp9.047 T on 13 Nov (2,2x). The first-day close is stated as a price move only (US$97,17, +17%), **verified on readable pages** (AP via NBC Washington; TradingView/Invezz; FourWeekMBA citing the Nasdaq official close). The ~US$1,76 T CNN figure is the fully-diluted basis (US$1,5 T x 97,17/83); on basic shares the close is ~US$1,28 T. Neither post-close value is spoken, so no basis mix-up on screen. Because the close is higher, the "2x" claim only gets truer after day one.

## Script (subtitle text)
| id | line | tag |
|---|---|---|
| h1 | Perusahaan pria ini nilainya dua kali bursa Indonesia. | amazed |
| h2 | Segede apa? Angka terakhirnya paling bikin kaget. | curious, teasing |
| rd | Rangkumin dong! (tagline) | |
| l1 | Ini Dario Amodei, bos Anthropic, pembuat Claude. | matter-of-fact |
| l2 | 19 November, sahamnya debut di Nasdaq. Harga perdananya 83 dolar. | explaining |
| l3 | Di harga itu, nilainya sekitar 1,1 triliun dolar. Kira-kira Rp20.000 triliun. | building up |
| l4 | Seluruh Bursa Efek Indonesia, per 20 November? Rp8.725 triliun. Dua kali lipat lebih. | emphatic |
| l5 | Tapi itu baru harga perdana. Hari pertama, ditutup 97 dolar, naik 17 persen. | surprised (the turn, ~65%) |
| l6 | Angka terakhirnya: nilai perdana itu setara 84 persen ekonomi Indonesia. Setahun. | serious, punchy (payoff) |
| cta | Menurut kamu, nilai segede ini wajar, atau kemahalan? Komen! | playful |

Pronunciation in `say`: Anthropic → "Entropik", Claude → "Klod", Nasdaq → "Nesdek", AI → "e ai". No spelled acronyms besides AI.

## Visual plan
- **Hook (0-3 s, collage look, copy tests/hook-collage):** Dario Amodei cut-out rising on the paper ledge, name tag "Dario Amodei · CEO Anthropic", title card 2 lines **"2X SELURUH / BURSA RI"** (cover frame, on screen ~3 s) with a small chip under it: "di harga IPO". Label-bar headline over torso (black → yellow → white): "1 PERUSAHAAN" / "= 2X" / "BURSA INDONESIA". Objects fly in every ~1 s: Claude logo sticker (press-kit only, else a generic chat-bubble icon), Nasdaq bell icon, rupiah notes. Credit small: "Foto: TechCrunch, CC BY 2.0, via Wikimedia Commons". h2: big "?" stamp + a locked padlock badge "angka terakhir".
- **Tagline** as usual.
- **l1:** cut-out shrinks to a corner sticker; Anthropic name tag + "pembuat AI Claude" chat-bubble icon.
- **l2:** calendar sticker "19 Nov" → Nasdaq board icon "ANT" → price tag "US$83" pops.
- **l3:** counter US$1,1 T → flips to **Rp20.000 T** (chip "di harga IPO"; no exchange-rate number on screen).
- **l4 (the answer visual):** two stacks of Rp100 ribu bricks to scale: BEI Rp8.725 T (label "Semua saham BEI · 20 Nov") vs Anthropic Rp20.000 T; bar heights exactly 20.000 : 8.725. **No numeric ruler** (fact-check FIX 2): a word sticker "DUA KALI LIPAT LEBIH" pops as it is spoken. "Bukan ajakan jual/beli saham" chip appears here and stays to the end.
- **l5 (turn):** mini line from "US$83" to "US$97" with "+17%" arrow (only spoken numbers on screen); small label "tutup hari pertama". Only those two points plotted (no intraday).
- **l6 (payoff):** padlock opens; a big Indonesia-shaped bar "Ekonomi Indonesia setahun" (no rupiah figure on screen) fills to 84% with the Anthropic block. Big number "84%".
- **CTA:** two buttons "WAJAR" / "KEMAHALAN" + comment bubble.
- **End card:** sources (detikFinance, ABC News, AP, TradingView/Invezz) + photo credit.
Safe area per playbook (x 60-920, y 240-1480); subs block mode.

## Real people
- **Dario Amodei: licensed photo found** → `File:Dario Amodei at TechCrunch Disrupt 2023 02.jpg` (portrait 2667x4000, CC BY 2.0, TechCrunch, Commons). Alternative: `File:Dario Amodei in 2023.jpg` (CC BY 2.0, UK Prime Minister). **Downloaded:** `assets/people/dario-amodei.jpg` (960 px thumbnail) + `dario-amodei.json` (CC BY 2.0, TechCrunch, credit "Foto: TechCrunch, CC BY 2.0, via Wikimedia Commons"). **Cut-out not made yet:** `rembg` is not installed here (see HANDOFF); producer runs `engine/cutout.py dario-amodei.jpg dario-amodei.png --kind person`. **No fallback needed:** person_collage stays the hook style.
- No other people are named.

## Sources
- detikFinance, 19 Nov 2026: https://finance.detik.com/bursa-dan-valas/d-8760676/harga-ipo-anthropic-resmi-us-83-per-saham-nilai-pasarnya-84-pdb-ri (US$83, range 70-78, US$81,34 M raised, ~US$1,1 T ≈ Rp20.000 T at IPO price, 2,2x BEI Rp9.047 T on 13/11, 84% PDB 2025 Rp23.821,1 T, fully diluted ~US$1,5 T, JISDOR Rp18.252)
- ABC News: https://abcnews.com/Business/anthropic-announces-price-83-share-ipo/story?id=138245320 (IPO price)
- AP via NBC Washington, 19 Nov: https://www.nbcwashington.com/news/business/anthropic-ipo-begin-trading-nasdaq/4185456/ (close +17% at US$97,17)
- TradingView/Invezz: https://www.tradingview.com/news/invezz:f1a2ad0a9094b:0-anthropic-s-ant-closes-at-97-17-up-17-on-its-first-day-of-trading/ (close US$97,17, open US$111,50)
- FourWeekMBA: https://fourweekmba.com/ai-anthropic-closes-day-one-at-97-17-up-17-from-83-ipo/ (Nasdaq official close, 13,22 bn basic shares → ~US$1,28 T)
- detikFinance (BEI cap context, 21 Nov): https://finance.detik.com/bursa-dan-valas/d-8763001/modal-asing-rp-100-triliun-keluar-dari-pasar-modal-ri (cap fell to Rp8.725 T by 20 Nov; we compare with 13 Nov as detik did; vs Rp8.725 T the ratio is 2,29x, so "dua kali lipat lebih" holds either way)

## Captions
**IG caption**
Perusahaan pria ini nilainya dua kali bursa Indonesia (di harga IPO). 🤯

• Anthropic (pembuat AI Claude, CEO Dario Amodei) debut di Nasdaq 19 Nov, harga perdana US$83 per saham
• Di harga itu nilainya ~US$1,1 triliun (~Rp20.000 T), ~2,3x kapitalisasi BEI Rp8.725 T (20 Nov)
• Hari pertama ditutup US$97,17 (+17%); nilai di harga perdana saja setara ~84% PDB Indonesia 2025

Menurut kamu, nilai segede ini wajar, atau kemahalan? Komen!

Cara hitung: nilai pasar di harga IPO (detikFinance, kurs JISDOR Rp18.252) dibanding kapitalisasi BEI 20 Nov 2026 (detikFinance). Angka fully diluted lebih besar (~US$1,5 T di harga IPO).
Bukan ajakan jual/beli saham.
Catatan: riset & naskah dibantu AI, termasuk Claude buatan Anthropic.
Sumber di komentar.
Foto: TechCrunch, CC BY 2.0, via Wikimedia Commons

#rangkumindong #anthropic #saham #ipo #ai #bursaefekindonesia #ekonomi #beritabisnis

**TikTok caption:** same text, hashtags `#rangkumindong #anthropic #saham #ipo #ai`

**YouTube title:** Di harga IPO, nilainya 2x seluruh bursa Indonesia? #Shorts

**YouTube description:** see post.json (summary, method line, disclaimer, AI disclosure line, 5 source links, photo credit, 5 hashtags).

**Tags:** rangkumindong, anthropic, dario amodei, ipo anthropic, saham ai, bursa efek indonesia, nasdaq, berita bisnis, shorts

**Sources first comment (pin):** detikFinance (IPO price, value, 84% PDB) · detikFinance (BEI Rp8.725 T, 20 Nov) · ABC News (IPO price) · AP via NBC Washington (close US$97,17, +17%) · TradingView/Invezz (close) · photo credit. Full text in post.json → pinned_comment.

## Notes
- Storyline: new (#ai-ipo, events E1033, E0965). Sensitivity low. Covered check: NEW.
- Disclosure: this draft was written by Claude, a product of Anthropic. Every caption (IG, TikTok, YT description) carries "Catatan: riset & naskah dibantu AI, termasuk Claude buatan Anthropic." The script stays factual and the CTA invites both views ("wajar atau kemahalan").
- **Trial Reel B version: not made** (standing rule since 9 Nov). The scale visual would make a decent B test with the question_reveal hook #6 ("Semua saham Indonesia digabung. Masih kalah sama satu perusahaan?") if Trial Reels come back.
- Re-check before render: nothing fast-moving is spoken except the day-one close (historical, fixed). BEI cap is Rp8.725 T dated 20 Nov (spoken and on screen); if a newer weekly figure is out before render, update l4 and the captions.
