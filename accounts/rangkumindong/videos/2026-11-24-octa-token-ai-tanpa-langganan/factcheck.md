VERDICT: FIX (2 issues)

Checked 2026-11-24. Sources opened: CNBC Indonesia, CNN Indonesia, Telkomsel official OCTA page (telkomsel.com/vas/octa). Bisnis.com could not be loaded (client error).

| Claim | Verdict | What the source actually says | Source |
|---|---|---|---|
| Launched 23 Nov 2026, Telkomsel Smart Office, Jakarta | OK | Press conference Monday 23 Nov 2026, Telkomsel Smart Office, Jakarta | CNBC; CNN ("Senin (23/11)") |
| "69 model AI" (l2, on-screen counter 0 to 69, IG/TikTok caption, YT description, pinned comment) | FIX | CNBC: "69 model AI". CNN gives both: Telkomsel's Aris Sudewo quoted "lebih dari 85 LLM ... atau 85 model", and the article text says "69 model AI". The official OCTA page gives no count ("berbagai model AI (seperti Claude, Gemini, Kimi, dan masih banyak lainnya)"). The company's own spokesperson contradicts 69, so the exact number is disputed | CNBC; CNN; https://www.telkomsel.com/vas/octa |
| Providers OpenAI, Google, Anthropic, DeepSeek | OK | CNBC and CNN both name "OpenAI, Google, Anthropic, (dan) DeepSeek" (CNN adds "dan lainnya"). The official page names Claude, Gemini and Kimi as examples | CNBC; CNN; Telkomsel |
| Packages Rp100.000 / Rp250.000 / Rp500.000 | OK | Same in all three. Official names: Basic / Medium / Pro | CNBC; CNN; Telkomsel |
| Prices include tax (captions only) | OK | CNBC: "sudah termasuk pajak". Official: "(sudah termasuk PPN)". CNN does not mention tax | CNBC; Telkomsel |
| Bonus 500 MB, 30 days (captions only) | OK | CNBC: 500 MB, "masa berlaku 30 hari". Official: 0.5 GB that follows the package's 30-day active period | CNBC; Telkomsel |
| Balance has no expiry (l4 "saldonya nggak ada masa berlaku") | OK | Aris Sudewo (CNBC): "tidak berbatas waktu, jadi tidak ada expired date-nya". Official T&C: "OCTA Token tidak memiliki masa berlaku". The 30 days applies only to the data bonus and package, not to the token. CNN's wording is a little ambiguous, but the two primary sources are clear. The script and captions keep the token and the data bonus apart correctly | CNBC; Telkomsel; CNN |
| Pay in rupiah; pulsa, Halo bill, QRIS, e-wallet, bank | OK | CNBC and CNN list the same payment methods. The official page says pulsa, postpaid bill and other methods in MyTelkomsel | CNBC; CNN; Telkomsel |
| Bought in MyTelkomsel, "khusus Simpati dan Halo" (l5) | OK | CNBC: SIMPATI and Telkomsel Halo customers buy via MyTelkomsel. The official page shows only those two product lines and also requires an active number and age 18+. by.U and Kartu As are not mentioned anywhere | CNBC; Telkomsel |
| Used at octa.telkomsel.com, login with number + SMS OTP | OK | CNN: "nomor Telkomsel dan kode yang dikirim melalui SMS". CNBC: log in with your Telkomsel number | CNN; CNBC |
| No per-prompt price or rate published; cost depends on model and usage (l6, l7) | OK | CNBC: "bergantung pada model AI yang dipilih serta intensitas penggunaannya". CNN: "tergantung jenis model AI yang dipilih dan seberapa banyak layanan yang digunakan". Neither gives a rate, and the official page has none either | CNBC; CNN; Telkomsel |
| #chatgpt hashtag (IG caption) | FIX | No source names ChatGPT. The articles say only "OpenAI", and the official page's examples are Claude, Gemini and Kimi. The hashtag suggests a product the sources do not confirm, purely for reach | CNBC; CNN; Telkomsel |
| Bisnis.com "operator jualan token AI" (pinned comment / end card, context only) | UNVERIFIED | The page failed to load at draft time and again now. No number in the video relies on it | Bisnis.com URL in post.json |
| "Bukan iklan, tidak disponsori" | OK (own statement) | n/a | n/a |
| Market disclaimer | n/a | Not a stock topic | n/a |

## FIX 1: model count (69 vs 85)
The spoken line and all text should not state 69 as a settled number.
- l2 text: `Satu saldo, buat puluhan model AI. Dari OpenAI, Google, Anthropic, sampai DeepSeek.`
- l2 say: `Satu saldo, buat puluhan model e ai. Dari Open e ai, Gugel, Entropik, sampai Dip-sik.`
- Visual l2: drop the 0 to 69 counter. Use the dot grid without a number, or the label "puluhan model".
- IG/TikTok caption bullet: `• Telkomsel rilis OCTA Token (23 Nov): satu saldo buat puluhan model AI (media menyebut 69; Telkomsel juga menyebut lebih dari 85), dari OpenAI, Google, Anthropic sampai DeepSeek`
- YouTube description: `satu saldo untuk puluhan model AI (CNBC/CNN menyebut 69; Telkomsel dikutip menyebut lebih dari 85) dari penyedia seperti OpenAI, Google, Anthropic dan DeepSeek`
- Pinned comment 1: `CNBC Indonesia, OCTA Token: 69 model AI menurut CNBC, paket Rp100/250/500 ribu, ...` (attribute the number). Pinned comment 2: add `(Telkomsel dikutip: "lebih dari 85 model")`.

## FIX 2: #chatgpt hashtag
Remove `#chatgpt` from the IG caption hashtags. Replacement line:
`#rangkumindong #telkomsel #ai #octatoken #teknologi #beritateknologi #tekno`

## Note (no fix required)
Bisnis.com could not be read. Either keep it labelled as context only or drop it from the pinned comment and end card. Every number already has two other sources.
