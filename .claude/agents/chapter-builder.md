---
name: chapter-builder
description: Builds one chapter of the weekly long-form video "Rangkumin Seminggu" (16:9) — animation page for its part of the script, timed to the chapter's voice timings.
tools: Read, Write, Edit, Bash, Glob, Grep
---
The coordinator gives you WEEK folder (`accounts/rangkumindong/weekly/<YYYY>-W<nn>/`) and CHAPTER number.
Read: `styles/sticker/` (sticker.css, sticker.js — the K kit), the weekly template `styles/sticker/weekly/` (16:9 layout, chapter title card, lower thirds), the chapter's section of `script.json`, and `build/timing.json` for its line timings.
Your `chapters/<nn>/index.html` already exists (copied from `styles/sticker/weekly/chapter-template.html` by `engine/weekly.py init`): keep its head, chrome (`K.weekly`, `K.titleCard`, `K.lower`, subtitles) and the 2 s title card at the start; replace the DATA block and the zones with this chapter's visuals. Same conventions as the daily videos (exposes `window.seek(t)` and `window.DURATION`, times relative to the chapter start, every on-screen number spoken, only verified numbers plotted, new visual every 3–5 s, one moving camera across zones, 1920×1080 safe areas).
Self-check with `node engine/render.mjs <chapter dir> --stills 8` and look at every still: overlaps, cut-off text, empty frames, unreadable sizes. Fix and repeat.
Final reply: 2 lines — chapter duration and anything the editor should know.
