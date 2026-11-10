# Draft: Bos Nvidia diselidiki dewannya sendiri, 10 Nov 2026

**Pick:** idea #1 (⭐, 10/12), user pick + "OK to post". Storyline: new (`nvidia-huang-probe`). Event E0684.
**Arm:** Pratama · 19:00 · format **standard** · subs **word** · hook **kamu_stakes** · no B (hook_b empty, standing rule from 9 Nov). Storytelling default: chronological scenes, one turn.
**Opening** = hook-critic PICK A: "Punya saham teknologi? Bos Nvidia lagi diselidiki." (same as hooks.md #1). hook_b empty.
**Angle:** what is reported, what the board did, and the turn: the viral US$450 bn one-day loss happened **Thu 5 Nov**, reported as an AI-bubble sell-off, **before** Huang's admission (8 Nov). So the video corrects the "skandal → 450 miliar" shortcut without claiming the scandal had zero effect.
**Sensitivity HIGH, rules applied:** all intelligence claims attributed ("dilaporkan", "diduga", "media AS menyebut"); China's denial included; Huang tetap CEO; board quote included; 18 Nov = request only ("baru permintaan, belum jelas Huang datang"); no "selingkuh"/"mata-mata" on screen as fact, no detail of the private relationship beyond Huang's own admission, no verdict. **Note:** the ideas.md hook "Saham AI kamu goyang gara-gara satu CEO" was dropped: it states a cause no source supports.

## Script (subtitle text)
- `h1` Punya saham teknologi? Bos Nvidia lagi diselidiki.
- `h2` Dan angka 450 miliar dolar yang viral itu, ceritanya lain.
- `rd` Rangkumin dong!
- `l1` Jadi gini. Nvidia bikin chip yang jadi mesin di balik ledakan AI.
- `l2` 29 Oktober, New York Times melaporkan: seorang perempuan, Alice Huang, diduga mendekati CEO-nya, Jensen Huang.
- `l3` Tujuannya, menurut laporan itu: teknologi Nvidia. Dia diduga terkait intelijen China.
- `l4` Kedutaan China membantah tuduhan mata-mata itu.
- `l5` Laporan yang sama: afiliasi Megaspeed, perusahaan tempat Alice pernah bekerja, membeli perangkat AI berisi chip Nvidia, minimal 4,8 miliar dolar.
- `l6` Minggu, 8 November, lewat email ke karyawan, Huang mengakui hubungan di luar nikah.
- `l7` Lalu, dewan Nvidia membentuk komite direktur independen untuk menyelidiki.
- `l8` Kata dewan: belum ada alasan percaya rahasia Nvidia atau keamanan AS bocor. Huang tetap CEO.
- `l9` Tapi ini yang sering ketuker.
- `l10` Kamis, 5 November, Nvidia memang kehilangan sekitar 450 miliar dolar nilai pasar. Dalam. Satu. Hari.
- `l11` Menurut CNBC Indonesia, investor cemas soal gelembung AI. Pengakuan Huang baru keluar tiga hari kemudian.
- `l12` Berikutnya: tiga politisi Republik di DPR AS meminta Huang memberi penjelasan, 18 November.
- `l13` Itu baru permintaan. Belum jelas Huang datang.
- `cta` Menurut kamu, seberapa besar urusan pribadi bos bisa ngaruh ke perusahaannya? Komen!
- `end` Follow Rangkumin Dong, biar nggak ketinggalan!

Spoken words = 216 (numbers spelled out) → **~86 s** at Pratama ~150 wpm (cap 215 met). Turn `l9` starts at ~58% of the words. If it runs over 90 s, cut "Jadi gini." (l1) first.

## Visual plan (Sticker Explainer, paper #F3EFE6)
- **0–3 s, h1:** cover title card (2 lines) **BOS CHIP AI / DISELIDIKI**. Jensen Huang cut-out on the paper ledge (licensed photo below), name tag "Jensen Huang · CEO Nvidia". A magnifier sticker pops over him at ~1.2 s; a phone sticker with a generic red stock list (no prices, label "ilustrasi") slides in at ~2 s.
- **3–6 s, h2:** counter 0 → **US$450 M** with a big "?" stamp; question tag "ceritanya lain" (opens the loop paid in l10–l11).
- **rd:** tagline sticker.
- **l1:** chip sticker with "AI" glow, small arrows to server icons.
- **l2–l3 (chronology header card "29 OKT · New York Times"):** newspaper sticker; a neutral silhouette with name tag "Alice Huang" (no photo: not a public figure with a licensed portrait; we don't show her face). Label bar "DILAPORKAN" on every frame where the intelligence claim is on screen; "diduga" in the subtitle highlight.
- **l4:** stamp "DIBANTAH" + embassy building icon (generic, small label "Kedutaan China di AS").
- **l5:** company card "Megaspeed · Singapura" → "afiliasi (Malaysia)" → crates labelled **≥US$4,8 M perangkat AI berisi chip Nvidia**; source tag "NYT via Al Jazeera, Kyunghyang". Alice's name tag: "mantan karyawan Megaspeed".
- **l6:** date card "MINGGU 8 NOV"; email-envelope icon "ke karyawan". No heart icons, no wife/family imagery (no gossip).
- **l7–l8:** boardroom table icon, label "Komite direktur independen"; quote card with the board's line; badge on Huang cut-out: **TETAP CEO**.
- **l9–l11 (turn, ~58–75%):** timeline bar: **5 NOV** (bar chart drop label "−US$450 M dalam sehari", source tag "Al Jazeera; CNBC Indonesia: >US$440 M") → **8 NOV** (envelope icon "pengakuan"). Gap arrow "3 hari". Label on 5 Nov: "cemas gelembung AI (CNBC Indonesia)". Only these two dates plotted; no price line (daily prices not sourced).
- **l12–l13:** Capitol-style building icon (generic), calendar chip **18 NOV**, stamp **"BARU PERMINTAAN"**.
- **cta:** question card + comment bubble. **"Bukan ajakan jual/beli saham"** small from l10 to the end card.
- **End card:** sources (Al Jazeera, CNBC Indonesia ×3, The Next Web) + "Foto: Anderseidesvik, CC BY-SA 4.0, via Wikimedia Commons".

**People / photos:**
- Jensen Huang: **licensed photo fetched** → `accounts/rangkumindong/assets/people/jensen-huang.jpg` (+ `.json` credit), Commons "File:Jensen huang stanford 2026-04-30 010.jpg", CC BY-SA 4.0, Anderseidesvik. Neutral portrait (looking aside, leather jacket). **Cut-out not made yet:** `engine/cutout.py` failed (`rembg` not installed here); producer to run `cutout.py jensen-huang.jpg jensen-huang.png --kind person`.
- Alice Huang: name tag + neutral silhouette only (no licensed photo; private-ish person accused only in media reports).
- Moolenaar / Mast / Crawford: not named on screen ("tiga politisi Republik"), so no cut-outs needed.

## Sources
- Al Jazeera, 8 Nov 2026: https://www.aljazeera.com/news/2026/11/8/us-chipmaker-nvidia-investigates-ceo-jensen-huang-over-affair
- CNBC Indonesia, 9 Nov 2026 (board, Huang's email): https://www.cnbcindonesia.com/tech/20261109111306-37-783480/kejayaan-nvidia-runtuh-seketika-setelah-ceo-mengaku-selingkuh
- CNBC Indonesia, 9 Nov 2026 (Alice Huang, Megaspeed Singapore): https://www.cnbcindonesia.com/tech/20261109073026-37-783364/siapa-alice-huang-teman-dekat-jensen-huang-diduga-mata-mata-china
- The Next Web (via Semafor), Nov 2026 (18 Nov request, closed-door, not scheduled; NYT 29 Oct; no charges): https://thenextweb.com/news/house-chairs-jensen-huang-briefing-megaspeed
- CNBC Indonesia, 6 Nov 2026 (Thursday drop >9%, >US$440 M, AI-bubble worry): https://www.cnbcindonesia.com/tech/20261106165209-37-783069/bubble-ai-pecah-sampai-amerika-rp18000-triliun-menguap-semalam
- InvestingCube, 6 Nov 2026 (Thu 5 Nov: NVDA −9,26%, >US$440 M): https://www.investingcube.com/shares/nvidia-stock-price-440-billion-wiped-out-in-one-day-can-nvda-hold-180/
- Kyunghyang, 30 Oct 2026 (Malaysian affiliate, ≥US$4,8 M; embassy denial): https://www.khan.co.kr/en/article/202610300934007
- The Star, 30 Oct 2026 (China MFA: 'groundless'): https://www.thestar.com.my/aseanplus/aseanplus-news/2026/10/30/china-dismisses-us-report-of-suspected-spy-targeting-nvidia-ceo-jensen-huang-as-groundless
- Re-check before render: did Huang accept/decline the 18 Nov request (reply was due 11 Nov)? Any board update or Nvidia share move after 9 Nov?

## Captions
**Instagram**
```
Bos chip AI terbesar lagi diselidiki dewannya sendiri. Tapi angka US$450 miliar yang viral itu ceritanya lain 👀

Rangkumin dong 👇
• Dewan Nvidia membentuk komite direktur independen (8/11) untuk menyelidiki CEO Jensen Huang, setelah Huang mengakui hubungan di luar nikah lewat email ke karyawan. Huang tetap CEO; menurut dewan, belum ada alasan untuk percaya rahasia Nvidia atau keamanan AS bocor.
• Dilaporkan New York Times (29/10): Alice Huang diduga mendekati Jensen Huang untuk mencari tahu teknologi Nvidia dan diduga terkait intelijen China; afiliasi Megaspeed (perusahaan tempatnya pernah bekerja) disebut membeli perangkat AI berisi chip Nvidia minimal US$4,8 miliar. Kedutaan China membantah tuduhan mata-mata; belum ada yang didakwa.
• Nilai pasar Nvidia memang hilang sekitar US$450 miliar dalam sehari (Kamis 5/11), saat investor cemas soal gelembung AI (CNBC Indonesia). Pengakuan Huang baru keluar 3 hari kemudian. Tiga politisi Republik di DPR AS meminta Huang memberi penjelasan 18/11; itu baru permintaan.

Menurut kamu, seberapa besar urusan pribadi bos bisa ngaruh ke perusahaannya? Komen 👇

Bukan ajakan jual/beli saham. Sumber di komentar.

#rangkumindong #nvidia #jensenhuang #saham #teknologi #beritateknologi #AI
```
**YouTube title:** Bos Nvidia diselidiki, US$450 miliar hilang sehari: ceritanya lain #Shorts

**YouTube description**
```
Bos chip AI terbesar lagi diselidiki dewannya sendiri. Tapi angka US$450 miliar yang viral itu ceritanya lain 👀

Rangkumin dong 👇
• Dewan Nvidia membentuk komite direktur independen (8/11) untuk menyelidiki CEO Jensen Huang, setelah Huang mengakui hubungan di luar nikah lewat email ke karyawan. Huang tetap CEO; menurut dewan, belum ada alasan untuk percaya rahasia Nvidia atau keamanan AS bocor.
• Dilaporkan New York Times (29/10): Alice Huang diduga mendekati Jensen Huang untuk mencari tahu teknologi Nvidia dan diduga terkait intelijen China; afiliasi Megaspeed (perusahaan tempatnya pernah bekerja) disebut membeli perangkat AI berisi chip Nvidia minimal US$4,8 miliar. Kedutaan China membantah tuduhan mata-mata; belum ada yang didakwa.
• Nilai pasar Nvidia memang hilang sekitar US$450 miliar dalam sehari (Kamis 5/11), saat investor cemas soal gelembung AI (CNBC Indonesia). Pengakuan Huang baru keluar 3 hari kemudian. Tiga politisi Republik di DPR AS meminta Huang memberi penjelasan 18/11; itu baru permintaan.

Menurut kamu, seberapa besar urusan pribadi bos bisa ngaruh ke perusahaannya? Komen 👇

Bukan ajakan jual/beli saham. Sumber:
1) Al Jazeera, 8 Nov 2026: https://www.aljazeera.com/news/2026/11/8/us-chipmaker-nvidia-investigates-ceo-jensen-huang-over-affair
2) CNBC Indonesia, 9 Nov 2026: https://www.cnbcindonesia.com/tech/20261109111306-37-783480/kejayaan-nvidia-runtuh-seketika-setelah-ceo-mengaku-selingkuh
3) CNBC Indonesia, 9 Nov 2026: https://www.cnbcindonesia.com/tech/20261109073026-37-783364/siapa-alice-huang-teman-dekat-jensen-huang-diduga-mata-mata-china
4) The Next Web, Nov 2026: https://thenextweb.com/news/house-chairs-jensen-huang-briefing-megaspeed
5) CNBC Indonesia, 6 Nov 2026: https://www.cnbcindonesia.com/tech/20261106165209-37-783069/bubble-ai-pecah-sampai-amerika-rp18000-triliun-menguap-semalam
6) InvestingCube, 6 Nov 2026: https://www.investingcube.com/shares/nvidia-stock-price-440-billion-wiped-out-in-one-day-can-nvda-hold-180/

#rangkumindong #nvidia #jensenhuang #saham #teknologi #beritateknologi #AI
```
**Tags:** Nvidia, Jensen Huang, dewan Nvidia, investigasi, saham teknologi, saham AS, AI, gelembung AI, Megaspeed, rangkumin dong

**Sources first comment (pin)**
```
Sumber:
1) Al Jazeera, 8 Nov 2026: https://www.aljazeera.com/news/2026/11/8/us-chipmaker-nvidia-investigates-ceo-jensen-huang-over-affair
2) CNBC Indonesia, 9 Nov 2026: https://www.cnbcindonesia.com/tech/20261109111306-37-783480/kejayaan-nvidia-runtuh-seketika-setelah-ceo-mengaku-selingkuh
3) CNBC Indonesia, 9 Nov 2026: https://www.cnbcindonesia.com/tech/20261109073026-37-783364/siapa-alice-huang-teman-dekat-jensen-huang-diduga-mata-mata-china
4) The Next Web, Nov 2026: https://thenextweb.com/news/house-chairs-jensen-huang-briefing-megaspeed
5) CNBC Indonesia, 6 Nov 2026: https://www.cnbcindonesia.com/tech/20261106165209-37-783069/bubble-ai-pecah-sampai-amerika-rp18000-triliun-menguap-semalam
6) InvestingCube, 6 Nov 2026: https://www.investingcube.com/shares/nvidia-stock-price-440-billion-wiped-out-in-one-day-can-nvda-hold-180/
Semua soal Alice Huang/intelijen = laporan media, dibantah Kedutaan China, belum ada dakwaan. Huang tetap CEO. 18 Nov = permintaan, belum jadwal pasti. Foto: Anderseidesvik, CC BY-SA 4.0, via Wikimedia Commons. Bukan ajakan jual/beli saham.
```
**TikTok (≤5 hashtags)**
```
Bos chip AI terbesar lagi diselidiki dewannya sendiri. Tapi angka US$450 miliar yang viral itu ceritanya lain 👀

Rangkumin dong 👇
• Dewan Nvidia membentuk komite direktur independen (8/11) untuk menyelidiki CEO Jensen Huang, setelah Huang mengakui hubungan di luar nikah lewat email ke karyawan. Huang tetap CEO; menurut dewan, belum ada alasan untuk percaya rahasia Nvidia atau keamanan AS bocor.
• Dilaporkan New York Times (29/10): Alice Huang diduga mendekati Jensen Huang untuk mencari tahu teknologi Nvidia dan diduga terkait intelijen China; afiliasi Megaspeed (perusahaan tempatnya pernah bekerja) disebut membeli perangkat AI berisi chip Nvidia minimal US$4,8 miliar. Kedutaan China membantah tuduhan mata-mata; belum ada yang didakwa.
• Nilai pasar Nvidia memang hilang sekitar US$450 miliar dalam sehari (Kamis 5/11), saat investor cemas soal gelembung AI (CNBC Indonesia). Pengakuan Huang baru keluar 3 hari kemudian. Tiga politisi Republik di DPR AS meminta Huang memberi penjelasan 18/11; itu baru permintaan.

Menurut kamu, seberapa besar urusan pribadi bos bisa ngaruh ke perusahaannya? Komen 👇

Bukan ajakan jual/beli saham. Sumber di komentar.

#rangkumindong #nvidia #jensenhuang #saham #AI
```

## Length & B version
- Estimated length ~86 s (standard, 60–90 s).
- Trial Reel B: **no** (standing rule from 9 Nov).

## Fact-check fixes applied (10 Nov)
- FIX 1: Megaspeed's Malaysian affiliate, ≥US$4,8 M of AI equipment containing Nvidia chips, Alice = former employee (l5, captions, visual). l4/l7/l13 trimmed 2 words each to hold length.
- FIX 2: detikInet dropped (doesn't mention Nvidia); InvestingCube 6 Nov is the second source for 5 Nov / US$450 M.

## Unsure / for the fact-checker
- ~~5 Nov inferred~~ confirmed by fact-check (InvestingCube). Earlier note: **5 Nov = the US$450 bn day** was inferred: Al Jazeera says "last week" (~US$450 bn), CNBC Indonesia 6 Nov describes Thursday's trading (>9%, >US$440 bn). Confirm the day; if it can't be pinned, change l10 to "Pekan lalu, …" and l11 to "… Pengakuan Huang baru keluar setelahnya."
- Al Jazeera's "regained 4% on Friday" is ambiguous (4% of losses vs +4%); left out of the script.
- Kedutaan China's denial: Al Jazeera only; find a second source or soften to "Menurut Al Jazeera, …".
- US$4,8 M Megaspeed: Al Jazeera citing NYT only; CNBC Indonesia gives no amount.
- Pronunciation: "En-vidia", "Hwang", "Mega-spid", "Nyu York Taims", "Ce En Be Ce" — listen-check.
