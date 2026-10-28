# Hooks review (hook-critic) 2026-10-28
Scores: one-read / short / plain / kamu / picture / gap / true&neutral (0-2 each, /14)

| # | Hook | Style | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Total | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.700 penerbangan batal gara-gara asap. (+ Rute kamu termasuk?) | shock_number | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 12 | One number, 6 words, resembles top performer (concrete number + picture); gap = which routes + per-day |
| 2 | 3.030 penerbangan kena asap. Separuh lebih batal. | shock_number | 1 | 2 | 1 | 0 | 1 | 1 | 2 | 8 | Two numbers in effect, no stakes |
| 3 | Rata-rata 23 pesawat batal terbang. Tiap hari. | shock_number | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 10 | Gives the payoff away up front |
| 4 | Mau terbang ke Kalimantan? Jadwalmu bisa digeser. | kamu_stakes | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 12 | Direct stakes for kamu, plain words; gap paid off by routes + night flights |
| 5 | Tiketmu ke Pontianak bisa pindah ke malam. | kamu_stakes | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 12 | Precise but narrows audience to one city (tie-break loses) |
| 6 | Pesawatmu batal karena asap. Uangmu balik nggak? | kamu_stakes | 2 | 2 | 2 | 2 | 1 | 0 | 0 | DQ | No refund facts in claims.json, cannot pay off |
| 7 | Katanya bandara ditutup karena asap. Ternyata nggak. | myth | not in A/B style today |
| 8 | Asap karhutla bikin berapa pesawat batal sehari? | question_reveal | not in A/B style today |

PICK A: 1.700 penerbangan batal gara-gara asap. Rute kamu termasuk?
PICK B: Mau terbang ke Kalimantan? Jadwalmu bisa digeser.
