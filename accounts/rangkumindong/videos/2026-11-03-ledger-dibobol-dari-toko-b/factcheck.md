VERDICT: FIX (1 issue) → APPLIED (3 Nov): zone 5 no longer shows S$3,5 juta; screen = speech.

Checked 3 Nov 2026 (MODE=full): script.json (A + hook_b), draft.md visual plan, post.json captions/pinned comment, claims.json. All 4 cited sources opened.

| Claim | Verdict | What the source actually says | Source |
|---|---|---|---|
| h1: hardware wallet "offline paling aman" (as "katanya" belief) | OK | CNBC: storing keys offline "dirasa lebih aman dibandingkan dengan online" | https://www.cnbcindonesia.com/tech/20261102065338-37-781330/modus-baru-kuras-rekening-menyusup-di-dompet-warga-ri-sasarannya |
| h2 / hb2: compromised since the shop; "Di Singapura, yang dibeli di beberapa toko ternyata sudah disusupi" | OK | Police: wallets "bought from some retail stores in Singapore" contained malicious components | https://www.malaymail.com/news/singapore/2026/10/28/singapore-crypto-users-lose-s35m-after-ledger-wallets-found-with-malicious-hardware/241011 |
| l1: Polisi Singapura nemu dompet Ledger berisi komponen jahat | OK | Same; components "could capture users' recovery phrases or private keys" | Malay Mail (above), CNBC (above) |
| l2: Kata Ledger, sisipan baca 24 kata pemulihan, kirim lewat sinyal seluler | OK | Ledger Donjon: microcontroller decodes the 24-word recovery phrase, sends it over LTE via provisioned eSIM. Note: Donjon finding is on CryptoBilis-sold devices; Ledger says all confirmed losses involve CryptoBilis devices, so the "Kata Ledger" attribution holds | https://www.bleepingcomputer.com/news/security/ledger-asks-sellers-across-asia-to-halt-sales-after-supply-chain-attack/amp/ |
| l3 / captions: 2 kasus sejak 10 Sep, S$3,5 juta ≈ Rp49,5 miliar | OK | Malay Mail: "at least two cases since September 10", S$3.5 million. CNBC: "dua kasus… sejak 10 September 2026", "SGD 3,5 juta (Rp 49,5 miliar)". Conversion consistent with SGD ≈ Rp14.000 (2026 level) | Malay Mail, CNBC |
| l3 visual: "S$3,5 juta" drawn on screen | FIX (applied) | On-screen number not spoken in l3 (draft's own producer note; default not yet applied to the zone plan) | — |
| l4: cek keaslian bawaan Ledger nggak bisa mendeteksi | OK | Implant doesn't touch Secure Element or OS, "undetectable by Ledger's integrity self-checks" (source says "integrity self-checks", not the "Genuine" feature by name; keep the on-screen panel generic) | BleepingComputer |
| l5 / captions: Ledger minta reseller di 7 wilayah Asia setop jualan, termasuk Indonesia; "pertengahan Oktober" | OK | BleepingComputer (14 Okt): Indonesia, Singapore, Thailand, Philippines, Vietnam, Malaysia, Hong Kong. Malay Mail: Ledger posted on X on 13 Okt. CNBC: 14 Okt. "Pertengahan Oktober" covers both | BleepingComputer, Malay Mail, CNBC |
| l6 / captions: perkiraan analis >US$86 juta (≈Rp1,5 T), belum dikonfirmasi Ledger | OK | Specter (@SpecterAnalyst), 9 Okt: "Total losses $86M+"; Ledger did not confirm; CNBC: analis >US$86 juta (Rp1,5 T), Ledger hasn't disclosed total losses. Later Bitquery figure US$93,2 juta exists; fine since labelled as an estimate | https://blockonomi.com/ledger-investigates-86m-crypto-losses-linked-to-suspected-fake-wallets/, CNBC |
| Captions: Ledger says direct sales channel safe | OK | "infrastructure, systems, services, and direct sales channel are safe to use" | BleepingComputer |
| Captions: police advice (don't share recovery phrase; move assets to new wallet with new phrase) | OK | CNBC: police advise "tidak mengungkapkan kunci pribadi, frasa pemulihan atau frasa benih"; Malay Mail: transfer to new wallet with newly generated recovery phrase | CNBC, Malay Mail |
| Captions: no Indonesian victims implied | OK | Neither source reports Indonesian victims; script/captions only say sales halted in Indonesia | CNBC |
| Disclaimer "Bukan ajakan jual/beli aset kripto" | OK | Present in script.json, end zone and all captions | — |
| Captions vs script consistency | OK | Captions match script figures and attributions | — |

Sensitivity: claims.json has no `sensitivity` field. No allegations against a named party, no court case, no named private individual (analyst is a public pseudonymous handle) → all claims `normal`; highest = normal.

## FIX
1. **[APPLIED 3 Nov, writer: draft.md zone 5 replaced with the exact line below; producer note updated]** Visual zone 5 (l3): remove the small "S$3,5 juta" from screen. Exact replacement for that zone line:
   `5. **l3** — counter: "2 kasus" then "Rp49,5 miliar" counting up.`
   (Alternative only if the S$ figure is wanted on screen: change l3 text to "Polisi catat 2 kasus, rugi 3,5 juta dolar Singapura, sekitar Rp49,5 miliar." and say to match.)
