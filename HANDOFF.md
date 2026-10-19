# Handoff: Rangkumin Dong (read this first in a new chat)

Updated: Mon 19 Oct 2026, 17:00 WITA. A new chat takes over from the previous one by reading this file, then the playbook. Keep this file current: whenever something here changes, update it, mirror it to the Video project (`claude/rangkumindong-handoff.md`), commit and push.

## Standing rules from the user
- **Approval:** every video needs the user's OK on its draft (topic, script, style, captions) before rendering. Nothing is published without an explicit "OK post". The overall workflow can be improved without sign-off; flag big changes.
- **Daily ideas:** exactly 5 ranked ideas, considering the last 14 days of events.
- **Try first:** "please try do the actions before asking me to do it if you really cant do it".
- **Early posts:** if a post time is before 10:00 WITA, send the finished video and captions the evening before.
- **TikTok (until it is connected on 24 Oct):** with every finished video, also send the MP4 and a TikTok caption for manual posting.
- **Keys:** never in chat, the repo or the project. Never enter passwords, create accounts or change security settings for the user.

## Keys: how this session reaches ElevenLabs and Upload-Post
- **Sessions the user starts** (claude.ai/code, "Default" environment) get both keys through **network secrets**. Calls work without any key in the session: `engine/tts_eleven.py` and `engine/post.py` send no auth header when no key is found, and the proxy adds it. Verified 200 on both on 19 Oct.
- **Scheduled-task sessions** (fresh sessions created by create_trigger) do **not** get the secrets: tested 4× on 19 Oct, all 401. So the daily chain must run **inside a chat the user started**, via `send_later` into that same chat, not as fresh-session scheduled tasks.
- **First thing in a new chat:** check that the secrets work: `curl -s -o /dev/null -w "%{http_code}" https://api.elevenlabs.io/v1/user/subscription` and `.../api.upload-post.com/api/uploadposts/users`. Both should return 200.

## Setup in a new chat
1. Repo: `git clone https://github.com/psatyadarma/explainer-studio` (if not already present) → `cd explainer-studio && npm install` (playwright-core + @sparticuz/chromium; cdn.playwright.dev is blocked). Check that `ffmpeg` and `python3 -c "import numpy"` work.
2. Read: this file → `accounts/rangkumindong/knowledge/playbook.md` (incl. "Agent pipeline") → `brand.json` → `knowledge/video-log.md` → active `storylines/`.
3. Schedules: create the daily chain with `send_later` into **this chat** at 22:00 UTC (06:00 WITA), with the daily-run message below. Then tell the user so they can switch off the old chat's tasks, or turn them off yourself if you can see them (`list_triggers`: the old chat's tasks are bound to session `session_01MWQK18RcNJoiuB7gvMomkx`).
4. Re-create the one-off reminders listed under "Scheduled" below, in this chat.

## Daily-run message (send_later text)
> DAILY RUN (Rangkumin Dong, 06:00 WITA). Repo explainer-studio (git pull first). Read HANDOFF.md, then follow the "Agent pipeline" section of accounts/rangkumindong/knowledge/playbook.md. You are the coordinator and the user's only contact. (1) Re-arm this message for tomorrow 22:00 UTC with send_later. (2) RUN_DATE = today in Asia/Makassar; `python3 -I engine/day.py init accounts/rangkumindong <RUN_DATE>`; read today's experiment arm in brand.json. On Fridays also start the weekly "Rangkumin Seminggu" draft (posts Sat 08:00 WITA, so the final video goes to the user Friday evening). (3) Run the 4 researcher agents in parallel (news-markets, news-politics, news-business, news-national); check each file with day.py check, rerun thin ones; `day.py merge`. (4) writer (ideas) → fact-checker → apply fixes → send the 5 ideas. (5) After the pick: writer (draft) → fact-checker → apply fixes → send the draft with captions. No render before approval. (6) After approval: re-check fast-moving numbers, voice, render, mix, review stills, send the MP4 (plus a TikTok caption until TikTok is connected). Post only after "OK post" (engine/post.py --when). (7) Update the knowledge files and the video-log; analyst at 24 h/72 h and Sunday review; mirror changed docs to the Video project; commit and push.

## Status
- **Video #1** (IHSG < 5.000 / MSCI, v3, Pratama voice, 69 s) scheduled on Upload-Post for **Mon 19 Oct 19:00 WITA**, IG Reels + YouTube Shorts (job `23adbd953d3347d3ba56e880a497191e`, request_id `Rangkumindong-2026-10-19-ihsg-msci-v3`). The sources go in an automatic first comment. The MP4 and captions were sent for manual TikTok posting.
- **Agent pipeline** built and tested on 19 Oct: 4 researchers → 72 events (66 new merged) → writer → fact-checker caught 9 errors (e.g. the marketplace tax actually started **1 Oct**, not 1 Nov) → revised ideas in `accounts/rangkumindong/daily/2026-10-19/ideas.md`, the test list for Tue 20 Oct (not yet picked by the user).
- **Tue 20 Oct arm:** Cahaya · 12:30 WITA · shock-number hook · tech rotation.
- **Weekly long video** "Rangkumin Seminggu": 6–10 min, 16:9, **Sat 08:00 WITA**, first one Sat 24 Oct. Still to build: a 16:9 version of the sticker style (`styles/sticker/weekly/`), chapter assembly, parallel rendering, and a thumbnail template.

## Scheduled (one-off)
- Mon 19 Oct 19:20 WITA: check that video #1 went live, send the links, update posted.json, the video-log and the storyline.
- Sat 24 Oct 09:00 WITA: the TikTok warm-up is done. Ask the user to connect TikTok to Upload-Post profile "Rangkumindong", verify it, add "tiktok" to `brand.json` posting.platforms, and stop the manual TikTok sends.

## Open items
- Laptop folder `C:\Users\PRAWIRA SATYA DARMA\Documents\ai-projects\auto-video`: needs an access grant from the desktop app; then create `rangkumindong\` and copy the videos.
- The researchers often can't read kompas.com, kpk.go.id, kejaksaan.go.id or idx.co.id; tech coverage was thin (business researcher now has a tech checklist).
- Possible event-database corrections from the 19 Oct sweep: E0023 (BPS trade data timing), E0026 (MSCI weight 1.10% vs 1.16%).
- Optional: YouTube handle @rangkumin.dong; a dashboard for events/metrics; check Upload-Post's analytics and IG cover/Trial Reel fields when first needed.
