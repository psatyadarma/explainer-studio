# Handoff: Rangkumin Dong (read this first in every session)

Updated: Mon 19 Oct 2026, 17:15 WITA. Each daily run is a fresh session with no memory of earlier chats. **This file plus the playbook are the memory.** Whenever something here changes, update it, mirror it to the Video project (`claude/rangkumindong-handoff.md`), commit and push.

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
2. Load the keys as above.
3. Read: this file → `accounts/rangkumindong/knowledge/playbook.md` (incl. "Agent pipeline") → `brand.json` → `knowledge/video-log.md` → active `storylines/`.
4. Agents: start them as general-purpose agents told to "Read .claude/agents/<role>.md and follow it exactly" (researchers on model sonnet). Don't rely on the custom agent types being registered.
5. Anything that has to happen later the same day (e.g. checking a 19:00 post at 19:20) → `send_later` into this session.

## Status
- **Video #1** LIVE since Mon 19 Oct 19:00 WITA: IG https://www.instagram.com/reel/DerGr2VijdH/ · YouTube https://www.youtube.com/watch?v=wecMGwOQoBo · TikTok posted manually by the user. Sync-fixed render `videos/2026-10-19-ihsg-msci-v3-sync` (QA sync PASS, −91 ms). Metrics due: 24 h = Tue 20 Oct 19:00, 72 h = Thu 22 Oct 19:00. Upload-Post's status doesn't report the first comment; the user checks and pins it.
- **Agent pipeline** built and tested on 19 Oct: 4 researchers → 72 events (66 new merged) → writer → fact-checker caught 9 errors (e.g. the marketplace tax actually started **1 Oct**, not 1 Nov) → revised ideas in `accounts/rangkumindong/daily/2026-10-19/ideas.md`. That was a test list for Tue 20 Oct; the user hasn't picked one. The 20 Oct run should do a fresh sweep and may reuse these ideas where still current.
- **New from 21 Oct:** virality rubric (6 signals × 0–2 = /12) on every idea + 3 runner-ups; weekly rhythm Mon markets/economy/business · Tue tech · Wed viral · Thu politics · Fri wildcard · Sat weekly video + chapter Short · Sun "Minggu Depan" (see playbook → Topic selection).
- **Weekly long video** "Rangkumin Seminggu": 6–10 min, 16:9, **Sat 08:00 WITA**, first one Sat 24 Oct. The draft goes to the user Friday morning, and the final video Friday evening for "OK post". Still to build before Friday: a 16:9 version of the sticker style (`styles/sticker/weekly/`), chapter assembly, parallel rendering, and a 1280×720 thumbnail template.

## Dashboard: "Rangkumin Dong Studio"
- URL: https://claude.ai/artifact/QidT9TTTnwGZX49Y4gqpW7 (Dashboard artifact; private to the user). Tabs: Today, Pipeline health, Videos & A/B tests, Events.
- Data = 7 JSON files made by `python3 -I engine/dash_export.py accounts/rangkumindong` (→ `accounts/rangkumindong/dashboard/data/`): runs, days, ideas, videos, metrics, events, experiments. The page itself is `accounts/rangkumindong/dashboard/index.html` (stored in the dashboard as `files/index.html`).
- **Refresh** (after the ideas are sent, after posting, and after the analyst runs): run the export, then for each file: upload it with the Artifact tool (`url` = the dashboard, `asset: true`, `file_path` = the JSON file; one call per file) and `ArtifactData update` collection `datasets`, doc `<name>` with `{source: {kind: "file", url: <returned /_blob/… url>, name: "<name>.json", format: "json"}, updated: {at: <ISO time>, by: "Claude (daily run)"}}` (read the doc first for its `version`). Then delete the previous file with Artifact `action: "delete"`, `path` = the old blob id.
- Metrics come from `knowledge/metrics.csv` (date, folder, platform, hours, views, avg_watch_pct, hold_3s_pct, shares, saves, follows), written by the analyst.

## Scheduled
- Daily ~06:00 WITA: "Rangkumin Dong daily" (fresh session).
- Daily 20:07 WITA: "Rangkumin Dong IG insights" (needs the user's computer; read-only Instagram Insights → metrics.csv).
- Mon 19 Oct 19:20 WITA (in the original chat): check that video #1 went live and send the links.
- Sat 24 Oct 09:00 WITA (in the original chat): TikTok warm-up done. The user connects TikTok to Upload-Post profile "Rangkumindong"; then add "tiktok" to `brand.json` posting.platforms and stop the manual TikTok sends.

## Open items
- **Wed 21 Oct ideas: the user asked to include karhutla** (it scored 10/12 on 20 Oct but was left out). Angles: ex-trade minister Lutfi vs Singapore ("your companies are the culprits": attribute it, include the companies' responses, never call a company guilty), 4 firefighters killed at Bromo Tengger Semeru, 7,118 hotspots (BNPB), Jakarta's 367 facilities on standby, Mendagri's statement. Refresh the numbers that morning.
- Laptop folder `C:\Users\PRAWIRA SATYA DARMA\Documents\ai-projects\auto-video`: needs an access grant from the desktop app, then create `rangkumindong\` and copy the videos.
- The researchers often can't read kompas.com, kpk.go.id, kejaksaan.go.id or idx.co.id. Tech coverage was thin, so the business researcher now has a tech checklist.
- Possible event-database corrections from the 19 Oct sweep: E0023 (BPS trade data timing), E0026 (MSCI weight 1.10% vs 1.16%).
- Optional: YouTube handle @rangkumin.dong; a dashboard for events/metrics; check Upload-Post's analytics and IG cover/Trial Reel fields when first needed.
