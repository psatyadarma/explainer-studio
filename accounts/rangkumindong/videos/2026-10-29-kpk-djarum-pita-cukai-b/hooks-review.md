# Hooks review (hook-critic) - A = question_reveal, B = kamu_stakes
Scores: one-read / short / plain / stakes / picture / gap / true+neutral

| # | Hook | Style | Scores | Total | Reason |
|---|---|---|---|---|---|
| 1 | Pita kecil di bungkus rokok. Kenapa KPK geledah kantor Djarum? | question_reveal | 2/2/2/1/2/2/2 | 13 | 5-word picture line, plain, question pays off. Stakes only implied. |
| 2 | Kasus Bea Cukai ini sudah berapa tersangka? | question_reveal | 1/2/1/0/0/2/2 | 8 | Needs context, no picture, no stakes. |
| 3 | KPK geledah Djarum. Djarum tersangka atau bukan? | question_reveal | 2/2/2/0/1/2/0 | 9 -> DQ | Puts "tersangka" next to the brand; not neutral. |
| 4 | Pita di rokokmu itu urusan uang negara. Kenapa KPK geledah Djarum? | kamu_stakes | 2/2/2/2/2/2/2 | 14 | Kamu's own pack, plain, "penerimaan negara" is KPK's framing. Resembles top performer (kamu stakes, 29.0%). |
| 5 | Harga rokok kamu ikut kena? | kamu_stakes | 2/2/2/2/1/0/0 | 9 -> DQ | No price facts in claims.json; stakes unsupported. |
| 6 | Tiap bungkus rokokmu ada pitanya. KPK lagi selidiki. | kamu_stakes | 2/2/2/1/2/1/1 | 11 | "Selidiki" is the wrong stage (penyidikan); weaker gap. |
| 7 | Rokok nggak boleh keluar pabrik tanpa pita ini. | free | 1/2/2/1/2/1/2 | 11 | Not in A/B style. |
| 8 | Digeledah KPK, berarti bersalah? Belum tentu. | free | 2/2/2/1/0/1/2 | 10 | Not in A/B style. |

PICK A: Pita kecil di bungkus rokok. Kenapa KPK geledah kantor Djarum?
PICK B: Pita di rokokmu itu urusan uang negara. Kenapa KPK geledah Djarum?
