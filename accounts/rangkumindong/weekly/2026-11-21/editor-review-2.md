VERDICT: FIX (3)

Independent second review of out/video.mp4 (417.4 s, 1920x1080, -14.3 LUFS, -1.3 dBTP). Contact sheet every 5 s viewed in full, plus full-res frames at problem spots. Script.json read in full and compared with factcheck.md and with on-screen numbers.

## Passed
- Hook, flow (intro, 5 chapters, "Catat tanggalnya", outro 12.8 s), title cards, typography and colours.
- YouTube chapters (post.json "BAB:" and build/youtube-chapters.txt) match the real chapter boundaries from the current per-chapter files (0:00, 0:29, 1:41, 2:48, 3:53, 4:49, 5:38, 6:45). All are 10 s or longer.
- The three fixes from editor-notes.md are confirmed in the final video: "+" at 3:33 is clear of the card, the "Yang paling bikin kaget" label at 5:15 is clear of the dot grid, and 6:05-6:15 no longer repeats the calendar.
- On-screen numbers match script.json and factcheck.md. Checked: 6% / 5,75% / +0,25; 32 ekonom / 11; Rp18.232 / Rp18.254; IHSG -1,07% / -1,02% / 5.194; Rp104,3 T; 7 dari 10; Rp4,89 juta; 47%; 8 names; 2 Des to 9 Des; 14 hari; 25 Nov; 17 Nov; 21 Nov; 23 Nov; 30 Nov; 21 Des; and the weekdays (all consistent with the 2026 calendar). Every factcheck FIX item (b1/b2, b4, b7, d4, g4, g6, a6) is applied on screen.

## Fixes
1. ch01, 1:25-1:32 (a9 "Hati-hati" card): the dark "Hati-hati" chip is half hidden behind the video card (z-order or position), so only its top half shows for about 7 s. Change: move the chip above the card (y -60 px) or raise its z-index so the whole word is visible.
2. ch06, ~6:12-6:20 (g4): the "Bisa diperpanjang" chip is tucked under the bottom edge of the "Akhir masa penahanan Listyo" card and touches the dark "Sidang etik" card below it. Change: shift the chip about 20 px down and add 12 px spacing before the dark card, or make it a sub-line inside the card.
3. ch04, 4:25-4:35 (d6, "Yang tidak ikut masuk: illicit enrichment, menurut CNN Indonesia"): factcheck.md RECHECK #5 is still open and UNVERIFIED (the CNN article bodies could not be opened). Before publishing, either open one CNN article or a second outlet to confirm it, or cut d6 and its scene. Also redo the Friday 20 Nov rechecks (Kejagung expose and gelar perkara outcome; Listyo detention extension). If they change b3, b7 or g4, the affected chapters need a re-render.

## Notes (not blocking)
- "Rp104 T" in the intro versus "Rp104,3 T" in ch05: consistent (rounded). The intro says "hilang" without "ditaksir" (the factcheck accepted this).
- The 5 s sheet shows no visual held for more than 6 s other than the 6:00-6:05 calendar, which changes content (the Danantara card enters).
