VERDICT: PASS (re-check after fixes; 0 blocking)
1 Sync: PASS - qa_sync --lead -0.04 (= index.html SUB_LEAD): median -40 ms, 93% of 92 words in window, 2% >150 ms late. Note: qa_sync.py does NOT read SUB_LEAD from index.html (defaults 0.08), so always pass --lead explicitly; my first-round FIX was measured at 0.08.
2 Visuals: PASS - counter now "Rp ??? T" blurred, no digits; cover readable, no clipping; only transitional mid-slide stickers (rd, Djarum tag) at frame edges; no hold >4 s; end card with handle, sources, disclaimer present. Minor: 3-line subtitles (l3, l7) sit right at the bottom edge of the 3:4 crop.
3 Numbers: PASS - matches draft.md/post.json (nol tersangka, 6 perusahaan, 28/29 Okt, no money figure).
4 Audio: -14.2 LUFS, TP -4.0 dBTP PASS. Voice sped with atempo 1.14 (pitch kept), ~148 wpm, tagline 1.0x; cannot listen, objective checks only (no clipping, no pitch shift).
5 Format: 1080x1920 30fps, 43.67 s (target 30-45 OK), a/v diff 0.01 s. Gaps 0.15-0.22 s (rd 0.06 s is the tagline join), h1->h2 0.21 s OK.
6 Must-haves: PASS (name tags only, handle + sources end card, tagline; not a market topic).
