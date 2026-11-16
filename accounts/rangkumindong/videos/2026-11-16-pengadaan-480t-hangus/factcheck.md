VERDICT: FIX (2 issues) · **both APPLIED 16 Nov by writer** (script.json, draft.md, post.json, claims.json)

Checked 16 Nov 2026 against CNN Indonesia, Katadata, Investortrust, Setkab, Databoks (all opened).

| Claim | Verdict | What the source says | Source |
|---|---|---|---|
| HUT ke-15 NasDem, Rabu 11 Nov 2026, Jakarta | OK | "Puncak HUT ke-15 Partai NasDem di NasDem Tower, Jakarta Pusat, Rabu (11/11)" | https://www.cnnindonesia.com/ekonomi/20261111222513-78-1426102/prabowo-sebut-rp480-t-belanja-apbn-hangus-ternyata-banyak-kebocoran |
| Sepertiga APBN = belanja barang/jasa, ~Rp1.200 T | OK | "sepertiga APBN kita adalah belanja barang dan jasa" / "kurang lebih Rp1.200 triliun" (Prabowo) | CNN, Katadata |
| 40% "hangus" (l4) | FIX (attribution) | The 40% is the Kepala LKPP's calculation that Prabowo cited: "Beliau hitung dari situ 40% hangus". l4 says "kata Prabowo" only | https://katadata.co.id/berita/nasional/6af522a6aeb0d/prabowo-sebut-apbn-bocor-rp480-triliun-per-tahun-imbas-belanja-tak-efisien , CNN |
| 40% x Rp1.200 T = Rp480 T, spoken by Prabowo | OK | "Kalau 40 persen dari Rp1.200 triliun itu adalah Rp480 triliun" | CNN |
| 15 harga berbeda for the same goods | OK | "Beli barang yang sama, ada 15 harga berbeda" | https://investortrust.id/macro/122270/prabowo-gagas-satu-badan-belanja-pemerintah-sebut-potensi-penghmatan-capai-rp480-triliun |
| Bus, mobil pemadam, komputer, obat RS | OK | bus, "pemadam kebakaran", komputer, "obat di rumah sakit" | CNN |
| 38 provinsi, 500 kabupaten, satu badan | OK | "Tidak 38 provinsi, tidak 500 kabupaten belanja sendiri-sendiri. Satu badan" | Investortrust, Katadata |
| Agustus: LKPP jadi Badan Pengadaan Pemerintah | OK | "meningkatkan kelembagaan LKPP menjadi Badan Pengadaan Pemerintah" (DPR, Jumat 14/8/2026) | https://setkab.go.id/presiden-prabowo-konsolidasi-pengadaan-pemerintah-berpotensi-hemat-hingga-rp360-triliun/ |
| 14 Agu: ~30% of Rp1.200 T = ~Rp360 T | OK (number) | Efficiency "dapat mencapai sekitar 30 persen dari total belanja pengadaan sebesar Rp1.200 triliun ... sekitar Rp360 triliun", conditional on consolidation; Databoks: a 2027 target | Setkab, https://databoks.katadata.co.id/datapublish/2026/08/14/prabowo-akan-ubah-lkpp-jadi-badan-pengadaan-bidik-efisiensi-30 |
| "Angkanya naik / sudah berubah ... dari belanja yang sama" (h2, l12, l13) | FIX (framing/neutrality) | The two figures measure different things. The Aug 30% / Rp360 T is the savings *target* if procurement is consolidated. The Nov 40% / Rp480 T is the LKPP head's estimate of how much is *hangus* now. Calling it "angkanya naik" suggests the President changed one number, which the sources do not support. The captions already frame the 30% correctly as "potensi hemat", so script and captions disagree | Setkab, Databoks, Katadata |
| Angkanya perkiraan, metode belum dirinci (l11) | OK | Investortrust: the source, base year and method for the 40% were not documented | Investortrust |
| "Tapi ini yang jarang dibahas" | OK (minor) | Editorial line with no source; acceptable as tone. Remove it if a sharper turn is wanted | — |
| Per-year wording avoided | OK | No body text states that Rp1.200 T is an annual figure (only Katadata's headline) | all |
| Photo credit | OK | Commons, public domain | Commons |

Notes: there is no "korupsi" wording, and the CTA is neutral. Not a market topic, so no saham disclaimer is needed. Optional balance: add Prabowo's own framing "ini adalah masalah manajemen" (CNN).

## FIX wording

**1. l4 (attribution)** · APPLIED
- text: `Dari situ, menurut hitungan Kepala LKPP yang dikutip Prabowo, 40 persen hangus.`
- say: `Dari situ, menurut hitungan Kepala El Ka Pe Pe yang dikutip Prabowo, empat puluh persen hangus.`

**2. h2 / l12 / l13 (two different estimates, not one number that rose)** · APPLIED (incl. zone 8 bar labels, h2 tag "angka lain", captions bullet 3)
- h2 text/say: `Hangusnya di mana? Dan ini bukan satu-satunya angka.`
- l12 text: `Agustus, di depan DPR, angkanya beda: kalau belanja disatukan, potensi hematnya sekitar 30 persen, Rp360 triliun.`
- l12 say: `Agustus, di depan, De Pe Er, angkanya beda: kalau belanja disatukan, potensi hematnya sekitar tiga puluh persen, tiga ratus enam puluh triliun.`
- l13 text: `November: yang disebut hangus 40 persen, Rp480 triliun. Dua perkiraan, dari belanja Rp1.200 triliun yang sama.`
- l13 say: `November: yang disebut hangus empat puluh persen, empat ratus delapan puluh triliun. Dua perkiraan, dari belanja seribu dua ratus triliun yang sama.`
- Visual zone 8: relabel the bars "14 Agu · DPR · target hemat 30% → Rp360 T" and "11 Nov · NasDem · disebut hangus 40% → Rp480 T". Change the parked h2 tag "angkanya berubah" to "angka lain".
