VERDICT: PASS

## Re-check 29 Okt 2026 (after the writer applied the fixes)
- FIX 1 (l13 + captions + pinned + claims + draft timeline): applied correctly. It now reads "tersangka sejak Juli lalu" / "sejak Juli 2026", and the "2 sprindik baru (1 menyebut…)" wording is gone everywhere.
- FIX 2 (l9 "Kata KPK…" + Hukumonline/Antara sources): applied correctly.
- FIX 3 (PMK 68/PMK.04/2018 citation): applied. JDIH lists PMK 68/2018 as **Berlaku**, with no amendments shown. Verified against its text (reproduced at pajakku.com/tax-guide/per-menkeu/68-pmk-04-2018):
  - Pasal 9 ayat (3): "Pengusaha Pabrik atau Importir Hasil Tembakau mengajukan pemesanan pita cukai" to the supervising Bea Cukai office. This supports "Pabrik pesan pitanya ke Bea Cukai" (OK).
  - Pasal 3 ayat (3): pelunasan is done by attaching the correct pita cukai before the goods leave the factory. Pasal 7 ayat (1) huruf a: for Indonesian-made tobacco products, attaching is done inside the factory. This supports "wajib ditempel sebelum rokok keluar pabrik" (OK). No softening needed.
  - Optional: update the claims.json note, which still says these were checked only against PMK 108. They are now verified against PMK 68/2018 Pasal 3(3), 7(1)a and 9(3).

---
Original full check (FIX 3 issues, all resolved above):

MODE=full · sensitivity HIGH · checked 29 Okt 2026

## Bottom line on the sprindik / suspect question
- **July 2026:** on 21 Jul 2026 KPK issued **two** sprindik from the Blueray/Bea Cukai case: one named a suspect (Gatot Heroe Hernanda, Kepala Kantor Bea Cukai Kediri) and one was general. KPK confirmed he was a suspect on 22 Jul. He was detained 26 Aug 2026.
- **October 2026:** KPK issued **one new sprindik umum** ("sprindik baru per Oktober 2026"). This is the basis for the 28 Okt searches at Djarum and KPPBC TMC Kudus. **No one has been named a suspect under it.** Hukumonline quotes Budi Prasetyo: it is a "Sprindik Umum". Antara says KPK "belum menetapkan seorang pun sebagai tersangka dalam pengembangan kasus tersebut", and that this probe is "di luar" the two July developments.
- detik and CNBC write "dua sprindik baru … satu menetapkan Gatot Heroe", which merges the July pair with the October one. CNN counts "3 sprindik aktif: 2 on Gatot, 1 umum", which fits the July+October reading.
- So **l9 is correct**: no suspect yet in the pita-cukai probe, Djarum included. **l13 is wrong**: Gatot Heroe was not named in an October sprindik.

## Claims table
| # | Claim | Verdict | What the source says | Source |
|---|---|---|---|---|
| l1 | Rabu 28 Okt, KPK searched PT Djarum + Bea Cukai Kudus | OK | "Rabu, 28 Oktober 2026"; PT Djarum Kudus + KPPBC TMC Kudus | detik d-8728488; CNN; CNBC |
| l2–l3 | Pita cukai = sign that the cukai has been paid; the factory orders it; it must be attached before the goods leave the factory | FIX (citation) | True in substance, but PMK 108/PMK.04/2008 was **revoked** by PMK 68/PMK.04/2018 tentang Pelunasan Cukai (JDIH lists it "Dicabut"). PMK 68/2018: "Pelunasan Cukai dilaksanakan dengan cara pembayaran, pelekatan pita cukai…" | jdih.kemenkeu.go.id/dok/108-pmk-04-2008 ; jdih.kemenkeu.go.id/api/download/abtrak/2018/68~PMK.04~2018Per.pdf |
| l4 | Jubir KPK Budi Prasetyo: they are looking into an alleged kickback from the pengurusan pita cukai | OK | detik: penyidik mendalami dugaan kickback dari pengurusan pita cukai (Budi Prasetyo) | detik d-8728488 |
| l5 | Including a possible pemberian from PT Djarum to oknum Bea Cukai | OK | CNN: "modus kickback atau pemberian" dari PT Djarum ke oknum Bea Cukai (CNN's own paraphrase of KPK); periskop headline "KPK Dalami Dugaan Pemberian PT Djarum ke Oknum Bea Cukai" | CNN; periskop.id |
| l6 | Documents + electronic evidence seized; "masih tahap awal" | OK | detik: dokumen + BBE; Budi: "masih di tahap awal" | detik d-8728488; Antara Jatim |
| l7 | Grew out of the Bea Cukai import-bribery case uncovered by the OTT in February | OK | Antara: OTT "Februari 2026"; Metro TV: OTT 4 Feb 2026 (Blueray Cargo); CNN/CNBC: "Februari lalu". The visual's "Feb 2026" is OK | kalteng.antaranews.com/berita/848303; metrotvnews NLMC8Gg4 |
| l9 | The pita-cukai probe uses a sprindik umum; no suspect yet, incl. Djarum | OK (add attribution) | Hukumonline: Budi says it is a "Sprindik Umum", no tersangka; Antara: "belum menetapkan seorang pun sebagai tersangka" | hukumonline lt6ae1c962d0007; kalteng.antaranews 848303 |
| l10 | Djarum Group: "Kami menghormati dan menaati hukum." | OK (single source) | Only CNN has it (Budi Darmawan, Corporate Communication Senior Manager Group). CNBC and Hukumonline have no response; Tempo is blocked. The visual already says "via CNN Indonesia". Keep that | CNN |
| l11 | Parent case: 8 people, tersangka + terdakwa | OK | detik: "delapan tersangka dan terdakwa"; Antara: 8 as of 26 Aug | detik; Antara |
| l12 | 3 sentenced, 4 on trial, 1 still with KPK | OK | detik: John Field, Deddy Kurniawan, Andri sentenced; Rizal, Sisprian, Orlando charged + Budiman Bayu Prasojo at the witness stage; Gatot Heroe still being processed at KPK | detik d-8728488 |
| l13 | Gatot Heroe "lewat sprindik baru Oktober ini" | **FIX** | He became a suspect under the **July** 2026 sprindik (KPK confirmed 22 Jul; detained 26 Aug). The October sprindik is general, with no suspect | metrotvnews NLMC8Gg4 (22 Jul 2026); kumparan 283seywEe8e (26 Agt 2026); Antara Jatim 1112623 |
| captions/pinned | "1 (… Gatot Heroe, lewat sprindik baru Oktober)"; "2 sprindik baru (1 menyebut tersangka Gatot Heroe, 1 umum)" | **FIX** | Same error as l13 | as above |

## FIXES (exact replacement wording)

**FIX 1: l13 (wrong sprindik/date for Gatot Heroe)**
- text: `Yang satu itu pejabat Bea Cukai, Gatot Heroe, tersangka sejak Juli lalu.`
- say: `Yang satu itu pejabat Bea Cukai, Gatot Heroe, tersangka sejak Juli lalu.`
- Visual l13 name tag: keep "Gatot Heroe · pejabat Bea Cukai · tersangka (praduga tak bersalah)". Visual l7 timeline: `Feb 2026 · OTT` → `Jul 2026 · Gatot Heroe tersangka` → `Okt 2026 · sprindik umum baru · geledah Kudus`.
- IG / YT / TikTok captions: replace `1 (pejabat Bea Cukai Gatot Heroe, lewat sprindik baru Oktober) masih diproses KPK.` with `1 (pejabat Bea Cukai Gatot Heroe, tersangka sejak Juli 2026) masih diproses KPK.`
- Pinned comment, detik bullet: replace `2 sprindik baru (1 menyebut tersangka Gatot Heroe, 1 umum tanpa tersangka), ` with `` (delete), and add a new bullet:
  `• Sprindik Oktober 2026 bersifat umum, belum ada tersangka; terpisah dari 2 sprindik Juli 2026 (salah satunya menetapkan Gatot Heroe) (Antara, 28 Okt): https://kalteng.antaranews.com/berita/848303/kpk-dalami-kasus-bea-cukai-melalui-penggeledahan-pt-djarum`
- claims.json note and draft.md line 3 ("2 new sprindik: 1 names Gatot Heroe") should be corrected the same way.

**FIX 2: l9 attribution + sources (claim is correct, but sensitivity is high)**
- text: `Kata KPK, penyidikan pita cukai ini pakai sprindik umum. Belum ada tersangka, termasuk Djarum.`
- say: `Kata Ka Pe Ka, penyidikan pita cukai ini pakai sprindik umum. Belum ada tersangka, termasuk Djarum.`
- Add Hukumonline (https://www.hukumonline.com/berita/a/usut-kasus-bea-cukai--kpk-geledah-kantor-pt-djarum-lt6ae1c962d0007/) and Antara to claims.json and the pinned comment as the sources for "sprindik umum, belum ada tersangka". CNN only implies this.

**FIX 3: revoked regulation cited**
- Visual l2–l3 caption tag: `PMK 108/2008` → `PMK 68/2018`.
- End card sources: `PMK 108/2008` → `PMK 68/PMK.04/2018`.
- Pinned comment last source bullet: `• Pita cukai = salah satu cara pelunasan cukai (PMK 68/PMK.04/2018 tentang Pelunasan Cukai, menggantikan PMK 108/PMK.04/2008): https://jdih.kemenkeu.go.id/dok/68-pmk-04-2018`

## Notes (no change required)
- The Djarum quote has one source (CNN). It is a reputable outlet and the visual credits "via CNN Indonesia", so it stays. If the PMK 68/2018 full text cannot be checked for the "pabrik memesan" and "ditempel sebelum keluar pabrik" details, they still rest on long-standing practice and the old PMK. Low risk, but a second source would help.
- Neutrality: "dugaan" is on every allegation, "digeledah ≠ bersalah" is there, Djarum's response is included, and the suspect is shown as a name tag without a face. OK.
