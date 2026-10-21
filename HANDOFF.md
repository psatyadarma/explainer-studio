# Handoff: Rangkumin Dong (read this first in every session)

Updated: Tue 20 Oct 2026, 12:55 WITA. Each daily run is a fresh session with no memory of earlier chats. **This file plus the playbook are the memory.** Whenever something here changes, update it, mirror it to the Video project (`claude/rangkumindong-handoff.md`), commit and push.

## Standing rules from the user
- **Approval:** every video needs the user's OK on its draft (topic, script, style, captions) before rendering. Nothing is published without an explicit "OK post". The overall workflow can be improved without sign-off; flag big changes.
- **Daily ideas:** exactly 5 ranked ideas, considering the last 14 days of events.
- **Try first:** "please try do the actions before asking me to do it if you really cant do it".
- **Early posts:** if a post time is before 10:00 WITA, send the finished video and captions the evening before.
- **TikTok (until it is connected on 24 Oct):** with every finished video, also send the MP4 and a TikTok caption for manual posting, plus a sources comment to pin.
- Never enter passwords, create accounts or change security settings for the user.
- **Computer on:** the user leaves their computer on with Chrome signed in to the social accounts. An evening task ("Rangkumin Dong IG insights", 20:07 WITA, requires that computer) reads Instagram Insights (read-only) into knowledge/metrics.csv. **Morning check:** if a posted video's Instagram 24 h/72 h row is missing from metrics.csv after its evening, warn the user in the morning message that their computer/Chrome may have been off or signed out.

## How the daily run works (from Tue 20 Oct)
- Every day at ~06:00 WITA a **fresh scheduled session** starts by itself (scheduled task "Rangkumin Dong daily"). That session is that day's chat: the user gets a notification and replies in it to pick, approve and say "OK post".
- **Keys:** the user keeps them in their private Video project as the doc `keys` (two lines: `ELEVENLABS_API_KEY=…`, `UPLOAD_POST_API_KEY=…`). Each session reads it with the Projects tool and writes it to `~/.config/explainer-studio/.env` (chmod 600). `engine/tts_eleven.py` and `engine/post.py` read that file. **Never print, echo, commit or send the values.** Verified from a scheduled session on 19 Oct: both APIs returned 200.
- Backup: sessions the user starts by hand in the "Default" environment also get both keys as network secrets, with no file needed. Scheduled sessions do not (tested 4×).
- Rendered MP4s are not committed (`out/` is gitignored). They live in the day's session and on the platforms after posting.

## Session setup (start of every run)
1. `git clone https://github.com/psatyadarma/explainer-studio && cd explainer-studio && npm install` (playwright-core + @sparticuz/chromium; cdn.playwright.dev is blocked). Check that `ffmpeg` and `python3 -c "import numpy"` work, and install anything missing.
2. Load the keys as above. If today's video uses a person cut-out: `pip install --break-system-packages rembg` and download the model once into ~/.u2net (see engine/cutout.py header; GitHub release, ~175 MB).
3. Read: this file → `accounts/rangkumindong/knowledge/playbook.md` (incl. "Agent pipeline") → `brand.json` → `knowledge/video-log.md` → active `storylines/`.
4. Agents: start them as general-purpose agents told to "Read .claude/agents/<role>.md and follow it exactly" (researchers on model sonnet). Don't rely on the custom agent types being registered.
5. Anything that has to happen later the same day (e.g. checking a 19:00 post at 19:20) → `send_later` into this session.

## Status
- **Video #1** LIVE since Mon 19 Oct 19:00 WITA: IG https://www.instagram.com/reel/DerGr2VijdH/ · YouTube https://www.youtube.com/watch?v=wecMGwOQoBo · TikTok posted manually by the user. Sync-fixed render `videos/2026-10-19-ihsg-msci-v3-sync` (QA sync PASS, −91 ms). **24 h (IG): 103 views, reach 93, avg watched ≈8.8 s of 70.6 s (12.4%), 1 comment, 0 shares/saves; YouTube 24 h not reported yet (lag).** 72 h = Thu 22 Oct 19:00. Upload-Post's status doesn't report the first comment; the user checks and pins it.
- **Video #2** LIVE since Tue 20 Oct 12:30 WITA: "Rupiah Rp18.046: besok BI tahan 5,75% atau naik ke 6%?" · IG https://www.instagram.com/reel/Des-m-yj_hs/ · YouTube https://www.youtube.com/watch?v=InOYuXQUm64 · TikTok manual by the user. Folder `videos/2026-10-20-rupiah-18rb-bi-rate`, storyline `storylines/rupiah.md`. Metrics due: 24 h = Wed 21 Oct 12:30, 72 h = Fri 23 Oct 12:30. **Follow-up candidate Wed 21 Oct:** BI RDG result (~14:00 WIB) as rupiah PART 2.
- **20 Oct run (first full pipeline day):** 4 sweeps (13/9/13/15 events, 50 merged) → 5 ideas, fact-check fixed 11 → user picked #3 (rupiah) with own angle "crossed 18k before?" → draft (5 fixes) → approved 07:51 → render → QA FIX ×2 then PASS → OK post 08:35 → live 12:30.
- **Lessons 20 Oct:** (1) **Cahaya reads ~130 wpm**: 232 words came out at 110 s. Writers should aim for **≤190 spoken words for Cahaya**, or use `engine/retime.py <video> --cut <id> --speed 1.15–1.2` (no new TTS credits; tagline kept at 1.0x). (2) `engine/tts_eleven.py` needs `pip install soundfile`. (3) Subtitle lead 0.02 passed sync for Cahaya (default 0.08 was 138 ms early). (4) Long lines (>~20 words) need splitting into subtitle pages in build/timing.json; `K.subtitles` now picks the latest-started line so pages flip on time. (5) QA flags holds >4 s: plan a beat every 2–3 s on long lines.
- **New from 21 Oct:** virality rubric (6 signals × 0–2 = /12) on every idea + 3 runner-ups; weekly rhythm Mon markets/economy/business · Tue tech · Wed viral · Thu politics · Fri wildcard · Sat weekly video + chapter Short · Sun "Minggu Depan" (see playbook → Topic selection).
- **Weekly long video** "Rangkumin Seminggu": 6–10 min, 16:9, **Sat 08:00 WITA**, first one Sat 24 Oct. The draft goes to the user Friday morning, and the final video Friday evening for "OK post". Still to build before Friday: a 16:9 version of the sticker style (`styles/sticker/weekly/`), chapter assembly, parallel rendering, and a 1280×720 thumbnail template.

## Dashboard: "Rangkumin Dong Studio"
- URL: https://claude.ai/artifact/QidT9TTTnwGZX49Y4gqpW7 (Dashboard artifact; private to the user). Tabs: Today, Pipeline health, Videos & A/B tests, Events.
- Data = 7 JSON files made by `python3 -I engine/dash_export.py accounts/rangkumindong` (→ `accounts/rangkumindong/dashboard/data/`): runs, days, ideas, videos, metrics, events, experiments. The page itself is `accounts/rangkumindong/dashboard/index.html` (stored in the dashboard as `files/index.html`).
- **Refresh** (after the ideas are sent, after posting, and after the analyst runs): run the export, then for each file: upload it with the Artifact tool (`url` = the dashboard, `asset: true`, `file_path` = the JSON file; one call per file) and `ArtifactData update` collection `datasets`, doc `<name>` with `{source: {kind: "file", url: <returned /_blob/… url>, name: "<name>.json", format: "json"}, updated: {at: <ISO time>, by: "Claude (daily run)"}}` (read the doc first for its `version`). Then delete the previous file with Artifact `action: "delete"`, `path` = the old blob id.
- Metrics come from `knowledge/metrics.csv` (date, folder, platform, hours, views, avg_watch_pct, hold_3s_pct, shares, saves, follows), written by the analyst.

## Scheduled
- Daily ~06:00 WITA: "Rangkumin Dong daily" (fresh session).
- Mondays 06:52 WITA: "Ajarin Dong weekly" (fresh session: 5 concepts → user picks 3 → drafts → render → posts Mon/Wed/Fri 19:00 via Upload-Post profile "Ajarindong"; see accounts/ajarindong/knowledge/playbook.md).
- Daily 20:07 WITA: "Rangkumin Dong IG insights" (needs the user's computer; read-only Instagram Insights → metrics.csv).
- Tue 20 Oct 20:40 WITA (in the 20 Oct daily chat): analyst for video #1 24 h metrics, dashboard refresh.
- Sat 24 Oct 09:00 WITA (in the original chat): TikTok warm-up done. The user connects TikTok to Upload-Post profile "Rangkumindong"; then add "tiktok" to `brand.json` posting.platforms and stop the manual TikTok sends.

## Open items
- **Back pocket (user decides later):** (1) copying finished videos to the laptop via GitHub release files picked up by the 20:07 task; (2) a public portfolio repo: curated engine + style kit + sanitized agent prompts + README, with clean history, while this repo stays private (the user creates the empty public repo; it must never contain keys, the account email or the knowledge base).
- **Ajarin Dong** (@ajarindong.id on IG/TikTok/YouTube, created 21 Oct; profile picture option C): set up 21 Oct. Upload-Post profile "Ajarindong" has IG + YouTube connected; TikTok is posted manually during warm-up (connect after ~26 Oct). Voices Pratama/Cahaya, tagline "Bingung? Ajarin dong!" (take A, pending the user's pick), 3 videos a week, weekly run on Mondays. The IG insights task should add @ajarindong.id once the user is signed in to it in Chrome.
- **Wed 21 Oct ideas: the user asked to include karhutla** (it scored 10/12 on 20 Oct but was left out). Angles: ex-trade minister Lutfi vs Singapore ("your companies are the culprits": attribute it, include the companies' responses, never call a company guilty), 4 firefighters killed at Bromo Tengger Semeru, 7,118 hotspots (BNPB), Jakarta's 367 facilities on standby, Mendagri's statement. Refresh the numbers that morning.
- Laptop folder `C:\Users\PRAWIRA SATYA DARMA\Documents\ai-projects\auto-video` granted 20 Oct; video #1 copied to `rangkumindong\2026-10-19-ihsg-msci\` (video.mp4 + captions-and-sources.md). How later videos get there is still to decide with the user (daily session can't reach the laptop).
- The researchers often can't read kompas.com, kpk.go.id, kejaksaan.go.id or idx.co.id. Tech coverage was thin, so the business researcher now has a tech checklist.
- Possible event-database corrections from the 19 Oct sweep: E0023 (BPS trade data timing), E0026 (MSCI weight 1.10% vs 1.16%).
- Optional: YouTube handle @rangkumin.dong; a dashboard for events/metrics; check Upload-Post's analytics and IG cover/Trial Reel fields when first needed.
