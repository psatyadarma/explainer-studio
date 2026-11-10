# Run log — Rangkumin Dong

History moved out of HANDOFF.md (22 Oct) so fresh sessions read less. Append one short dated block per day; lessons that change how we work go into the playbook or the agent files, not here.

## Up to 22 Oct
- **Video #1** LIVE since Mon 19 Oct 19:00 WITA: IG https://www.instagram.com/reel/DerGr2VijdH/ · YouTube https://www.youtube.com/watch?v=wecMGwOQoBo · TikTok posted manually by the user. Sync-fixed render `videos/2026-10-19-ihsg-msci-v3-sync` (QA sync PASS, −91 ms). **24 h (IG): 103 views, reach 93, avg watched ≈8.8 s of 70.6 s (12.4%), 1 comment, 0 shares/saves; YouTube 24 h not reported yet (lag).** 72 h = Thu 22 Oct 19:00. Upload-Post's status doesn't report the first comment; the user checks and pins it.
- **Video #2** LIVE since Tue 20 Oct 12:30 WITA: "Rupiah Rp18.046: besok BI tahan 5,75% atau naik ke 6%?" · IG https://www.instagram.com/reel/Des-m-yj_hs/ · YouTube https://www.youtube.com/watch?v=InOYuXQUm64 · TikTok manual by the user. Folder `videos/2026-10-20-rupiah-18rb-bi-rate`, storyline `storylines/rupiah.md`. **24 h (IG): 87 views, reach 63, avg watched 2.7 s of 88 s (3.1%), 1 share, 1 save; YouTube 5 views, analytics lagging.** 72 h = Fri 23 Oct 12:30. BI RDG result (21 Oct afternoon) was offered as PART 2 for 19:00 but not picked; still a candidate for 22 Oct.
- **20 Oct run (first full pipeline day):** 4 sweeps (13/9/13/15 events, 50 merged) → 5 ideas, fact-check fixed 11 → user picked #3 (rupiah) with own angle "crossed 18k before?" → draft (5 fixes) → approved 07:51 → render → QA FIX ×2 then PASS → OK post 08:35 → live 12:30.
- **Lessons 20 Oct:** (1) **Cahaya reads ~130 wpm**: 232 words came out at 110 s. Writers should aim for **≤190 spoken words for Cahaya**, or use `engine/retime.py <video> --cut <id> --speed 1.15–1.2` (no new TTS credits; tagline kept at 1.0x). (2) `engine/tts_eleven.py` needs `pip install soundfile`. (3) Subtitle lead 0.02 passed sync for Cahaya (default 0.08 was 138 ms early). (4) Long lines (>~20 words) need splitting into subtitle pages in build/timing.json; `K.subtitles` now picks the latest-started line so pages flip on time. (5) QA flags holds >4 s: plan a beat every 2–3 s on long lines.
- **Video #3** LIVE since Wed 21 Oct 19:00 WITA (IG https://www.instagram.com/reel/DewQNdcEvnM/ · YouTube https://www.youtube.com/watch?v=QmaiHm5TzJA · TikTok manual): "10 perusahaan RI disurati Singapura soal asap, Lutfi: pemasok grup yang induknya di Singapura" (karhutla, Pratama, shock number; slot moved 12:30→19:00 because of voice fixes). Folder `videos/2026-10-21-karhutla-lutfi-singapura`, 89.1 s, QA PASS round 6. TikTok manual. Metrics: 24 h = Thu 22 Oct 19:00, 72 h = Sat 24 Oct 19:00.
- **21 Oct run:** 4 sweeps (11/7/9/7, 34 merged) → 5 ideas (light fact-check 6 fixes) → user picked #1 karhutla (said the Chinese rocket debris story was interesting but not attention-grabbing yet) → draft (full fact-check 6 fixes; NEA notices are now 10 firms; Lutfi said the firms are *suppliers* to Singapore-based groups, not owned from there) → approved → render → QA FIX (true peak, credit gap) → PASS → user asked 3× to fix how "BNPB" sounded → OK post 19:00.
- **Lessons 21 Oct:** (1) **Acronyms:** see playbook → Script & delivery → Acronyms ("Be En Pe Be", comma before, quick letters, no full stops). (2) **tts_eleven.py spoke the script's long `direction` text aloud** (+7.5 s twice): fixed 21 Oct, directions over 60 chars are now cut to a short tag (first 3 comma parts); writers should still keep `direction` short. (3) Pratama ran ~150 wpm at 231 words (96.8 s raw) → retime 1.09×; aim ≤215 spoken words for Pratama. (4) `engine/mix.py` true-peak target is now −2.0 dBTP; `engine/render.mjs` muxes with `-t <audio length>` instead of `-shortest` (no dropped end frames). (5) Hot /s/ sibilants can push AAC true peak over the limit: QA suggests a light de-ess above 5 kHz. (6) The fact-checker once put the user's email in a Wikimedia request header — agents must never send personal data in headers (engine/commons.py uses a neutral UA).
- **22 Oct run (Thu, arm Cahaya · 19:00 · question):** all 4 first sweeps came back empty: in the unattended session WebFetch refused section-page URLs typed from the agent files (PROVENANCE_REQUIRED, permission prompt unanswered). URLs returned by a WebSearch (or linked from an already-fetched page) do fetch. Reruns told "search first, then fetch only returned URLs" worked for business (8) and national (11); the markets and politics reruns were blocked by the auto-mode classifier, so those two stayed empty (19 merged). 5 ideas sent ~06:40 WITA (light fact-check 4 fixes): #1 beras fortifikasi 11/12 (rec.), #2 definisi korupsi, #3 benih lobster, #4 Summarecon–Hercules Rp800 jt, #5 anti-scam. BI RDG 21 Oct: BI-Rate held 5,75%, DF up to 5,00%. Waiting for the pick. **Open:** the researcher agent files should be changed (with the user's OK, flag) to start from WebSearch results instead of hard-coded section URLs, or the user grants WebFetch for the news domains; dash_export's ideas.json did not pick up 22 Oct ideas (unchanged hash) — check its parser.
- **New from 21 Oct:** virality rubric (6 signals × 0–2 = /12) on every idea + 3 runner-ups; weekly rhythm Mon markets/economy/business · Tue tech · Wed viral · Thu politics · Fri wildcard · Sat weekly video + chapter Short · Sun "Minggu Depan" (see playbook → Topic selection).
- **Weekly long video** "Rangkumin Seminggu": 6–10 min, 16:9, **Sat 08:00 WITA**, first one Sat 24 Oct. The draft goes to the user Friday morning, and the final video Friday evening for "OK post". Still to build before Friday: a 16:9 version of the sticker style (`styles/sticker/weekly/`), chapter assembly, parallel rendering, and a 1280×720 thumbnail template.
- **22 Oct (cont.):** web fetches allowed in `.claude/settings.json` (WebFetch + WebSearch, user's request; verify on 23 Oct sweeps). User picked #2 definisi korupsi (not the recommended rice). Luhut's overnight clarification reshaped the draft; full fact-check 5 fixes (Pasal 2/3 → KUHP 603/604 since 2 Jan 2026). Approved 07:44 → Cahaya raw 104 s → l5 cut + 1.15x → QA PASS r2. User asked where the people's cut-outs were → added Luhut/Setyo/Yusril (Trisno no licensed photo); Commons rate-limited this server (~10 min/file, originals blocked), so rework ran to 18:54 and the 19:00 slot was missed → QA PASS → OK post → **live 19:30** (IG Dey4SpKEY5J, YT vSNSsBHAMe8).
- **Lessons 22 Oct:** named people get cut-outs by default, photos fetched at draft time (playbook); one message per update, captions in code blocks; Cahaya ~117 wpm at 203 words → aim ≤180 words; `engine/qa_sync.py` needs `--lead 0.02` for Cahaya (doesn't read SUB_LEAD); Upload-Post status = `GET /api/uploadposts/status?request_id=<id>`; `engine/mix.py --deess`; commons.py neutral UA + Retry-After.

## 23 Oct (Fri, #5 survival mode; Pratama, question_reveal)
- User picked #1. Sweeps: 31 events, 30 merged. Fact-check fixes: 2 (light, ideas) + 3 (full, draft). QA FIX then PASS after a SUB_LEAD false alarm.
- Posted ~18:15 WITA at the user's request (slot 19:00): IG De1T7g3AGla, YT 4UDj48AzkDU, TikTok manual. Meta rejected the B Trial Reel (account below follower threshold); B saved, not posted.
- Weekly "Rangkumin Seminggu" 17-23 Okt built (accounts/rangkumindong/weekly/2026-10-24, 7:24); awaiting user OK for Sat 08:00 (no auto-post, high sensitivity).
- Token cuts: events.py window --brief/show, day.py candidates/today.

## 24 Oct (Sat, #6 IHSG chapter cut PART 3; Pratama, kamu_stakes, subs block)
- Weekly MP4 wasn't in this session, so it was re-rendered here (7:22). The weekly had already been scheduled and posted at 08:00 from the 23 Oct chat (IG De2y5UIDySU, YT HrNZE3CJlY4). The morning message wrongly said it was unposted and was corrected later. **Lesson:** `git fetch` and check the Upload-Post schedule again just before telling the user something isn't posted.
- Sweeps: 27 events (8/3/5/11), 26 merged. Light fact-check made 3 fixes. No pick by 14:00, so ⭐ #1 was taken as the default. Full fact-check made 2 fixes (Friday foreign net sell for the full day was Rp1,29 T). QA returned FIX (cover counter, CTA showing under the end card), then PASS on A and B.
- Auto-posted 19:00 (no reply): IG De3-lMjk0Wl, YT TivUTiMxyV0. B not posted (Trial Reels blocked).
- **Engine bug:** subtitle timings from tts_eleven.py and variant.py came out ~0.8–1.2 s late against the voice. The producer re-timed them from the STT transcript with a scratchpad script. Fix this in the engine before the next video.
- Metrics: survival (24 h) IG 492 views, ~28.4% watched; karhutla (72 h) IG 51 views, 30.6%; YT 90.5% on 186 views (treat with caution).

## 25 Oct (Sun, #7 Minggu Depan "4 tanggal dompet"; Pratama, question_reveal, subs word)
- Sweeps: 30 events (7/8/6/9), 26 merged; fixed a leftover merge marker in covered.csv. Light fact-check made 4 fixes. No pick by 14:00, so ⭐ #1 was the default.
- Full fact-check: the marketplace PPh 22 0,5% has applied since **1 Okt** (DJP SP-23/2026), not 1 Nov, so the reveal became UMP 1 Nov ("buruh minta"). E0289 is marked superseded. pajak.go.id was unreadable here, so the date was matched by title/URL. QA: FIX for tiles clipping mid-pan, then PASS on A and B; the 57 s length was waived for minggu_depan (40–60 s).
- Auto-posted 19:00 (no reply): IG De6jT34jOCl, YT i1OvbBvUfDw. B not posted (Trial Reels blocked). Yassierli's photo got Commons 429s, so B fell back to a name tag.
- **Still open:** the subtitle-timing bug (~0.8 s late) in tts_eleven.py; the producer re-timed from STT again. Missing setup this session: soundfile, rembg.
- Weekly review W43 (reviews/2026-W43.md): no variable decided. The analyst proposes replacing the blocked daily A/B with alternating-day hook styles on A only; waiting for the user's decision.

## 26 Oct (Mon, #8 minyak >US$115 vs APBN US$70 "siapa yang nombok", survival PART 2; Pratama, shock_number, subs block, format short)
- Sweeps: 28 events (4/8/6/10); politics failed validation (0 events, detik/antara fetch refused) and was rerun once. 22 merged. Light fact-check: 2 fixes (PC drop = Omdia/IDC; Fed = Sept projections); Brent stated "di atas US$115".
- No pick by 14:00 → ⭐ #1 default. Hook critic switched A to the "ratusan triliun" line. Full fact-check: Rp376,8 T not energy-only (hook says "ratusan triliun"), "listrik nggak naik" dropped (Q4 tariff unannounced), Rp338 T dropped, kompensasi monthly vs subsidi periodic.
- Producer fixed the subtitle-lag bug in `engine/tts_eleven.py segment()` (pin first word to speech onset, corrects lag >0,35 s); today's take wasn't late, SUB_LEAD 0.02. QA: 1 FIX round (stamp clipping, 3-line subs → ≤2 lines), then PASS.
- Auto-posted 19:00 (no reply): IG De9IFgyFfdc, YT fjnB040O9oI. B made, not posted (Trial Reels blocked). Dashboard: 2 old blobs (runs, days) couldn't be deleted (permission denied) — harmless orphans.

## 27 Oct (Tue, #9 definisi korupsi PART 2 "Uang negara hilang. Pasti dihitung korupsi?"; Pratama, question_reveal, subs word, format standard)
- Sweeps: 29 events (10/6/7/6), all valid first try; 26 merged, 3 dupes. Light fact-check: 2 fixes (BYD = Gaikindo wholesale #1, not "listrik #1 pertama kali"; HSC "dikeluarkan dari hitungan IHSG", not "dicoret").
- User picked #5 (definisi korupsi PART 2, 8/12, sens high) over ⭐ #1 BYD (10/12) and asked why #1; answered (score, low sensitivity, wallet/consumer retention). Full fact-check PASS: both ANTARA-only claims got second outlets (CNN, Disway); BUMN line attributed "menurut laporan ANTARA". Cut-outs Prabowo/Yusril/Luhut/Setyo, Romli name tag.
- Producer A 84.7 s / B 81.4 s; QA PASS both first round (qa_sync needs --lead 0.02 with Pratama too). User "OK" ~14:30 → scheduled; posted 19:00: IG De_s4bjCYcA, YT NbyJVwx49cU. B not posted (Trial Reels blocked).
- **New standing rule (user 27 Oct): automatic posting for all kinds of posts**, incl. sensitivity high (QA PASS + fact-check fixes still required). Analyst: minyak-115 24 h IG 196 views/28.7%; IHSG cut 72 h YT 65.7% watched; weekly 72 h IG 604 views, 23 shares. Dashboard: 1 orphan blob (old runs.json 9f4e8de0…) — delete permission denied.

## 28 Oct (Wed, #10 asap karhutla "1.700 penerbangan batal"; Pratama, shock_number, subs block, format short)
- Sweeps: 31 events (11/4/8/8), all valid first try; 30 merged, 1 dupe. Light fact-check: 2 fixes (Singapore FM visit not "mendadak", no gas/MSCI; Tito quote softened). ⭐ moved to karhutla flights after re-score (10/12).
- No user reply all day: default pick #1 at 14:00, default auto-post at 18:40. Hook-critic A 12/14, B kamu_stakes (person_collage fallback, no face). Full fact-check PASS ("1.700 rute" in CNBC body = slip; 23/hari own calc).
- Producer A 43.1 s / B 42.5 s; QA round 1 FIX (subs into bottom zone; sync FIX was a mis-measure at default lead 0.08 — at the real 0.02 it's −80 ms) → round 2 PASS both. Posted 19:00: IG DfCRqk-jygU, YT IsQsbiAmYxE. B not posted (Trial Reels blocked).
- Analyst: definisi korupsi PART 2 24 h IG 1,334–1,347 views, ~50% watched (best ever), followers 21→25. metrics.csv conflict with the 20:07 IG-insights task resolved (its IG rows kept). qa_sync.py default lead 0.08 vs page 0.02 keeps producing false FIX — worth defaulting --lead to the page's SUB_LEAD.

## 29 Oct (Thu, KPK geledah Djarum & Bea Cukai Kudus "pita cukai itu apa?"; Pratama, question_reveal, subs word, format standard)
- Sweeps: 33 events (5/9/9/10), all valid first try; 30 merged, 3 dupes. Markets thin (Fed decision and 28 Oct rupiah close not captured). Light fact-check: 2 fixes on #1 (sprindik/tersangka count), "terancam" on #2.
- No user reply: default pick ⭐ #1 at 14:00. Hook-critic agreed with the writer's A/B. Full fact-check: 3 fixes (Gatot Heroe = suspect since July, not the October general sprindik; "belum ada tersangka" attributed to KPK + Hukumonline/Antara; PMK 108/2008 → PMK 68/PMK.04/2018), then PASS.
- Producer A 75.6 s / B 76.7 s (B hook re-voiced once); QA PASS both first round (qa_sync --lead 0.02). Analyst: karhutla 24 h IG 370 views/29.4%; minyak 72 h IG 200/28.5%.
- **18:40 default post BLOCKED:** the session's auto-mode permission classifier denied `engine/post.py` ("External System Writes") with no live user OK. Video not posted; user told + push. Dashboard old-blob delete also denied again.

## 30 Oct (Fri, Djarum PART 2 "kerugian triliunan"; Cahaya, shock_number / myth, subs block, format short) + weekly #2
- Sweeps 33 events (6/10/7/10), all valid first try; 31 merged. Light fact-check 4 fixes. No pick by 14:00 → default ⭐ #1. Hook-critic picked A/B; full fact-check 1 fix (source attribution). Producer A 51 s → QA FIX (invented counter digits, gap, length) → voice 1.14× atempo, gaps ≤0.21 s → A 43.7 s / B 43.3 s, QA PASS both. qa_sync ignores SUB_LEAD (default 0.08): pass --lead.
- **User said "OK post for today" in the morning** (after asking why 29 Oct didn't post) → A scheduled 19:00 and live (IG DfHbaudCVLy, YT nsRjP_84WAs). B not posted (Trial Reels blocked). The 29 Oct Djarum video stays unposted (superseded).
- Weekly "Rangkumin Seminggu #2" (24–30 Okt, 10:12, Cahaya, 9 chapters): writer → full fact-check 9 fixes → chapter-builders ×9 (Sonnet) → render → editor 5 fixes → re-render ch01/02/06 → PASS. User "Yes" → scheduled Sat 31 Oct 08:00 (request_id Rangkumindong-2026-10-31). post.py can't set the thumbnail.
- Analyst: definisi korupsi P2 72 h IG 1,357 views / 49.4% watched, YT 82 / 49.0%.
- **Permission finding:** the daily task is already permission_mode "auto"; the 29 Oct block was the safety check that requires a live user yes in that day's chat. A morning "OK post hari ini" works.
- 31 Oct 08:00: weekly #2 live (IG DfI0oyajx3t, YT u74sDSDa73M); thumbnail to be set by hand in YouTube Studio.

## 31 Oct (Sat, #13 definisi korupsi PART 3 chapter cut from weekly ch 3; Cahaya, question_reveal / story, subs word, format chapter_cut) + weekly #2 live
- Weekly #2 went live 08:00 (IG DfI0oyajx3t, YT u74sDSDa73M). Sweeps 19 events (7/2/7/3); business first run empty → rerun OK; 13 merged. Light fact-check PASS, 0 fixes.
- User picked #1 and gave "OK to post" ~08:55. Hook-critic added "2024" to A; full fact-check 1 fix ("terpidana" → "terdakwa yang divonis 2024"). Producer A 86.2 s / B 84.9 s (1.2× retime), QA PASS both first round. A scheduled 19:00 and live (IG DfKAISMAIiv, YT 9Ha4Sh0QzL8); B not posted (Trial Reels blocked).
- Analyst: asap 72 h IG 414 / 29.9%, YT 915 / 52.4%; Djarum 24 h IG 37 / 22.0% (weakest of the week).
- Problems: git push rejected once (another session pushed weekly links in parallel; covered.csv duplicate row resolved); deleting the 14:00 send_later was denied by the classifier (harmless no-op wake-up). Dashboard old-blob deletes worked today.

## 1 Nov (Sun, #14 Minggu Depan "5 tanggal 2–10 Nov"; Cahaya, kamu_stakes / person_collage, subs block, format minggu_depan)
- Morning: covered.csv had a leftover "=======" merge-marker line (fixed). Sweeps 6/8/7/9 events, 16 new merged. Ideas: 5 offered + 3 runner-ups.
- No pick by 14:00 → default pick (Minggu Depan). Full fact-check 3 fixes. Producer 47.1 s; first take dropped words, lines after the tagline re-voiced. QA round 1 FIX (zone 5 strip at safe edge, #disc, B collage over header) → round 2 PASS both. User "ok to post" ~15:16 → A live 19:00 (IG DfMk3g-AaNV, YT kWgg0Cbq5A4); B not posted (Trial Reels blocked).
- W44 review written (reviews/2026-W44.md). Recommendation (stop B, rotate 3 hook styles on A only, freeze voice Pratama / block subs / 19:00) awaits user OK.
- Producer notes: render needs CHROME_PATH empty (/usr/bin/google-chrome crashes); pip install soundfile was needed.

## 2 Nov (Mon, #15 Binance dibobol Rp114 T; Cahaya, shock_number / story, subs word, format standard)
- Sweeps 9/2/5/10 events (politics thin, business 5), 19 merged, 7 dupes. Light fact-check 3 fixes (Rp114 T not Rp104 T; frozen split; date). User replied "OK" → read as ⭐ #1 + OK post (first time the recommended idea was taken).
- Draft trimmed 190→165 words (~76 s). Full fact-check 3 fixes: attack 29 Okt US time = Jumat dini hari WIB (morning message's "Kamis malam" corrected to the user). QA: round 1 sync FIX (qa_sync default --lead 0.08 misled; producer set SUB_LEAD 0.0, l12 re-voiced), round 2 visual FIX ×5, round 3 PASS both.
- User "OK to post" 11:08 → A scheduled 19:00, live (IG DfPJo5kFEob, YT LiOd0PidLTc); B not posted. Analyst: Minggu Depan 24 h IG 7 / YT 30; Djarum P2 72 h IG 38 / 21.7%.
- Problems: dashboard old-blob deletes denied 3 of 4 by the classifier (harmless leftovers). qa_sync.py still ignores index.html SUB_LEAD — pass --lead explicitly.

## 3 Nov (Tue, #16 Ledger dibobol dari toko; Cahaya, myth / kamu_stakes (person_collage fallback), subs block, format short)
- Sweeps 9/8/8/10, 33 merged, 2 dupes. Light fact-check 4 fixes (#2 "hingga 20%", #3 "dikabarkan", #4 unverified local figures dropped). User picked ⭐ #1 + "OK to post too" ~05:20 (second recommended pick in a row).
- Draft 94 words; hook-critic A/B 12/14 each; full fact-check 1 fix (unspoken S$3,5 juta off screen). Producer: 48,6 s A / 50,0 s B (over the 45 s short target; QA accepted). QA PASS both, first round.
- A scheduled 08:57 for 19:00, live (IG DfRuXu_iPk-, YT MwVSIfLGxos); B not posted. Analyst: Binance 24 h IG 272 / 23,1%; def. korupsi P3 72 h IG 80 / 12,2%, YT 192 / 76%.
- Problems: delete_trigger for the unneeded 14:00 default-pick wake was denied by the classifier (it fired and did nothing). Shell CHROME_PATH still set to google-chrome → producer must clear it. Cahaya voiced slower than estimated: for short format aim ≤85 words.

## 4 Nov (Wed, #17 Listyo Sigit tersangka penyadapan; Cahaya, kamu_stakes / story, subs word, format standard)
- Sweeps 8/9/6/6, 23 merged, 6 dupes. Light fact-check: 4 fixes on #3 (Bank MNC rumour) and #4 (Listyo). User picked #4 (10/12, sens high) over ⭐ #1 TPPO (11/12) and said "OK to post" early (~09:00).
- Draft 183 words; hook-critic agreed with the writer's A/B (12/14, 13/14). Full fact-check 3 fixes ("file hasil sadapan", detention per Kabareskrim/kumparan, Yusril "berharap"). Producer: A 86,7 s / B 87,4 s (take sped up 1,05×). QA round 1 FIX (disclaimer only from l8; card treatment unequal; B uniformed figure) → round 2 PASS both.
- A scheduled 09:27 for 19:00, live (IG DfUTKP4jxd9, YT oK5ep48c3Wg); B kept, not posted. Analyst: Ledger 24 h IG 45 / 15,4%, YT 7; Minggu Depan 72 h IG 117 / 20,2%, YT 34.
- Problems: delete_trigger for the 14:00 default-pick wake denied again (it will fire and do nothing). CNBC article URL for the detention claim not found (kumparan kept as source).

## 5 Nov (Thu, #18 Listyo PART 2: LIMS + rutan; Cahaya, myth / story, subs block, format short)
- Sweeps 4/1/8/8 (politics thin: detik/cnn/tempo unreachable), 20 merged, 1 dupe. Light fact-check: fixes on #1 BPJS and #2 IHSG. User picked #3 (9/12, sens high) over ⭐ #1 BPJS desil 8 (11/12) and said "OK to post" (~09:30).
- Hook-critic PICK A #2 myth (13/14), B #4 story (12/14). Full fact-check 5 fixes (Istana response/Keppres/Plt Ariyo Windutomo, "diduga milik Presiden", dropped 33-hari beat, 2025–2026, source credit). QA: round 1 length 50 s > 45 s + l8 "Ingat"; round 2 a deletion changed l5's meaning + B hb1 timing; round 3 l7 name; round 4 PASS both (A 44,1 s, B 44,7 s).
- A scheduled ~10:50 for 19:00, live (IG DfW4ARZFLRA, YT LTQJNPv0Fps); B kept, not posted.
- Problems: delete_trigger (14:00 wake) and deleting the old dashboard runs.json blob (e33efdace2d2…) were denied; both harmless. Lesson: when cutting for length, QA must re-check meaning of every line touched.

## 6 Nov (Fri, #19 Listyo PART 3: tersangka ke-4 SU; Pratama, person_collage (Kapolri Suyudi cut-out) / story, subs word, format standard, **storytelling: true**) + weekly #3
- Sweeps 12/8/6/7, 29 merged, 4 dupes. Light fact-check 3 fixes + 1 unverified. User picked #5 (7/12, sens high) over ⭐ #1 Susu Bendera (10/12), "OK to post", and asked for storytelling-style scripts → first narrative script (chronological scenes, open question per beat, cliffhanger; no invented scenes).
- Hook-critic agreed with writer (A 9/14, B 10/14). Full fact-check 6 fixes (4th suspect name only via CNN, "belum ditahan", "sementara"). Producer 1.1× retime, word starts moved to STT timings. QA round 1 flagged Kapolri sticker in body (overruled: speaking figure gets cut-out) → PASS both. A scheduled ~10:05 for 19:00; B kept.
- Weekly #3 (31 Okt–6 Nov, 7:23, Pratama, 8 chapters): writer → full fact-check 5 fixes → builders ×8 → render (parallel run died on container restart; renders must be foreground) → editor 3 fixes (title cards 2 s → 0.3/1.2 s) → PASS; ch01 re-voiced so the 4th suspect is "SU, menurut CNN". Sent to user ~10:15, default post Sat 07:40.
- Problems: container restarted twice (background jobs killed); weekly.py render --jobs 3 reported "FAILED Node.js" for 7 chapters on the first run.
- 19:00 live (IG DfZcwwMknBV, YT MU6pPpz2o0I). Analyst: Listyo P2 24 h IG 172 / 22,1%, YT 1.299; Ledger 72 h IG 56 / 15,1%, YT 7 / 58%. Weekly #3 awaiting "OK weekly" (default post Sat 07:35 wake-up).
- Sat 7 Nov 07:35: weekly #3 default post denied by the safety check (no live yes); user asked for "OK weekly".
- 07:36 user "OK weekly" → scheduled 08:00 (job d1a9c31f…).
- 08:00 weekly #3 live (IG Dfa2COGnI5j, YT mjJIN0HdaXQ); thumbnail to be set by hand in YouTube Studio.

## 7 Nov (Sat, #20 Kripto dibobol dua kali, crypto-hacks PART 2, chapter cut weekly #3 ch 2; Pratama, shock_number / question_reveal, subs block)
- Sweeps 8/12/7/8, 34 merged, 1 dupe. Light fact-check 3 fixes (#1 Binance figures, #4 DHE only a plan). User picked ⭐ #1 + "ok to post" (~06:00).
- Hook-critic A = writer's A (11/14), B new (10/14). Full fact-check 5 fixes (Binance's own US$6,34 M ≈Rp115 T, not ABC's 6,6 M; "hampir separuh" frozen; entry = fake Homebrew). Producer resumed after a container restart (reused matching voice/mix); B opening subtitles recoloured. QA PASS both, first round (A 86,9 s, B 85,4 s).
- A scheduled ~06:40 for 19:00 (job 0c10a65b…); B kept, not posted. Weekly #3: the 07:35 default post was blocked; the user said OK in the 6 Nov chat → live 08:00 (IG Dfa2COGnI5j, YT mjJIN0HdaXQ).
- 19:00 live (IG DfcBjiCklEk, YT anVIFJotWx0). Analyst: Listyo P3 (first storytelling script) 24 h IG 1.524 / 54,6% watched (best IG start yet, ~2,5× the 15–23% band), YT 3.110; Listyo P1 72 h IG 197 / 20,8%, YT 1.430 / 60,7%.
- Problems: the session sat on a detached HEAD, so the morning pushes never landed; rebased onto origin/main (the weekly commits) and merged covered.csv by hand. delete_trigger (14:00 wake) and deleting the old runs.json blob were denied again (harmless).

## 8 Nov (Sun, #21 Minggu Depan 9–15 Nov; Pratama, myth / kamu_stakes, subs word)
- Sweeps 5/9/5/7, 25 merged, 1 dupe. Light fact-check 0 fixes (some sources blocked, unverified items checked in full fc). No pick by 14:00 → default ⭐ #1.
- Hook-critic confirmed writer's A/B. Full fc 2 fixes (BI 6% "beberapa ekonom"; bansos "arahnya tunai"). Producer retimed 1.09x (96→88 s). QA PASS both round 1.
- User ~14:50: "I follow your decisions" → posted A for 19:00 (job 3077ba79) and applied W44/W45 recs: Pratama locked, no B from 9 Nov, hooks rotate on A only. Live IG DfemZPFmbth, YT WZ9FImj_9io.
- Analyst W45 review (reviews/2026-W45.md): storytelling n=2 mixed (P3 54%, kripto 20%); Pratama 30% vs Cahaya 17% → decided; wallet weight 1.0→0.75. Benchmarks blocked again.
- Problems: deleting old dashboard blobs and disabling the 18:00/18:40 wake-ups were denied (harmless; wake-ups no-op'd).
- 2026-11-08 20:10 WITA IG insights: kripto-dibobol 24 h (548 views, 20.1% watched, 3 follows) and listyo-part2 72 h (180, 23.3%, 0 follows) from Upload-Post + IG web insights (instagram.com/insights/media/<media_id>, id = base64-decoded shortcode). Skip rate is not shown in IG web insights (app only) and business.facebook.com is blocked for the Chrome extension → hold_3s n/a. Old dashboard blobs 0660e194…/d1e0037e… not deleted (deletion needs approval).

## 9 Nov (Mon, side story msci-reclassification: 6 investor pegang 98% transaksi, BEI periksa CASA/FUJI/NSSS; Pratama, story, no B)
- Sweeps 10/5/8/1 (national thin: detik/antara blocked), 20 merged, 4 dupes. Light fact-check 1 FIX (PMK 49/2026 removed). Default pick star #1 at 14:00; hook-critic PICK A story 12/14 (person_collage fallback, no licensed face). Full fc PASS 0 fixes; producer 46.4 s, QA PASS round 1.
- User "Ok to go" 15:27 -> scheduled, live 19:00 (IG DfhLK-jnAba, YT M4Wueqxh38g).
- Analyst: Listyo P3 72 h final: IG 1,545 views / 54.3% watched / 5 shares / 3 saves; YT 3,311 / 64.1% / +1 sub. Best of series, flat since 44 h.
- Problems: health.py falsely warned IG 24 h for 7 Nov was missing (row exists but out of order in metrics.csv; health.py should not depend on row order). Deleting old dashboard blob c1bed135... and the 18:00 wake-up were denied (harmless).
- 2026-11-09 20:12 WITA IG insights: minggu-depan 9–15 Nov 24 h (229 views, 17.2% watched, 1 follow) and weekly #3 72 h (actual ~60 h: 1,461 views, 17.7% of 7:23, 28 shares, 10 saves, **33 follows** — biggest follow driver so far). No -b trial folders. Skip rate still app-only → hold_3s n/a. Dashboard days+metrics refreshed; old days blob 5f5503c3… not deleted (deletion denied).

## 10 Nov (Tue, tech: Nvidia board probes CEO Jensen Huang; Pratama, kamu_stakes, subs word, no B)
- Sweeps markets 1 / politics 11 / tech 6 / national 0→7 (rerun once: antara PROVENANCE_REQUIRED). 23 merged, 2 dupes. Light fc 1 FIX (PSI quote) + 2 notes on #1, all applied.
- User picked ⭐ #1 + "OK to post" early morning. Hook-critic PICK A 13/14. Full fc 2 FIX (Megaspeed affiliate wording; detikInet source swapped for InvestingCube). Pre-render news re-check: no change.
- QA round 1 FIX (sync early -146 ms, timeline arrowhead, disclaimer from t=0) → producer set SUB_LEAD -0.04 → PASS. TTS said "Alice Wang" once (accepted). Scheduled ~10:00, live 19:00 (IG Dfjv8ISjuFg, YT trRoEmJt_cQ).
- Problems: health.py false IG-24h WARN again (row order); couldn't delete the 14:00 send_later (denied; it no-op'd). Analyst at 10:00 was too early for 24/72 h reads (logged real hours 15 h / 63 h).
