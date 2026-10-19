# explainer-studio

Faceless 9:16 explainer video pipeline (Sticker Explainer style). Every frame is code: an HTML page
exposes `window.seek(t)`, headless Chromium screenshots each frame, ffmpeg encodes.

## Pipeline
1. `script.json` — lines of narration (`text` = subtitle, optional `say` = pronunciation).
2. `python3 -I engine/tts.py <project> [speed]` — voice + per-line/word timings → `build/voice.wav`, `build/timing.js`.
3. `python3 -I engine/mix.py <project>` — voice + code-synthesized music bed + SFX (`sfx.json`) → `build/mix.wav` at -14 LUFS.
4. `node engine/render.mjs <project>` — renders `out/video.mp4` (1080×1920, 30 fps). `--stills 1.5` for a contact-sheet preview.

## Layout
- `engine/` — render, TTS, mix
- `styles/sticker/` — shared style kit (springs, camera, subtitles, tokens)
- `accounts/<name>/` — brand settings per account
- `tests/style-test/` — 20 s demo of the look (demo data, not news)

## Setup (fresh machine)
- `npm install` (uses @sparticuz/chromium; no system Chrome needed)
- `pip install sherpa-onnx soundfile numpy`
- Voice model: download `vits-piper-id_ID-news_tts-medium` from the sherpa-onnx GitHub releases into `models/`.
