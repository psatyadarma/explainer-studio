VERDICT: FIX (3)

Checked: out/video.mp4 (1920x1080, 30 fps, 7:42), contact sheet every 5 s (all 93 frames viewed), full script.json, post.json, thumbnail.jpg, per-chapter loudness, freeze detect.

## Fixes

1. **Whole video, loudest at chapter 2 (BAB 2, about 02:00-02:57).** The final mix peaks at -0.1 dBTP (chapter 2 alone -0.2 dBTP). It can clip after YouTube's AAC re-encode. Loudness is otherwise consistent: chapters -14.5 to -15.2 LUFS, full video -14.1 LUFS, LRA 2.7, so there is no level jump between chapters. Change: re-mix the final audio with `loudnorm=I=-14:TP=-1.5:LRA=7` (or a limiter at -1.5 dBTP) and re-mux. Do not touch the video stream.
2. **04:11 chapter card and "AS ancam tarif 18%" (ch 4 title card, ch 4 header chip, chapter list in the YouTube description, `youtube_title` "Tarif AS 18%").** The headline states 18% as fact. The fact-checked script says USTR proposes an extra tariff of **up to** 18%, and it is still only a proposal. Change: use "AS ancam tarif sampai 18%" in `chapters/04/script.json` (title), the chapter 04 header chip, the `BAB:` line in `post.json` (04:11), and `youtube_title` ("Tarif AS sampai 18%"). Rebuild chapter 04 and re-assemble. If you change the chapter title length, the timestamps do not move, because the audio is unchanged.
3. **Friday 27 Nov rupiah close not yet checked.** factcheck.md requires a recheck before render. The video says Rp18.364 close Thu, "Rp1 juta = sekitar 54 dolar" and the thumbnail ">18.400 (sempat, Kamis siang)". All of these are correct for Thursday. Change: after the Friday close is published, if it is weaker than 18.364, edit the c3/c8 lines and the thumbnail per factcheck.md. If it is the same or stronger, no change. It does not block the on-screen numbers below.

## Numbers on screen vs fact-checked script (all OK)

- Vote **Fri 11 Dec**: calendar "SEMULA 9 DES (struck) -> JUMAT 11 DES, kata MPR" at about 01:45-01:50; ch 6 "Pemilihan, JUMAT 11 DES"; description and caption say 11/12. OK.
- Rupiah: Mon Rp18.203 (+0.37%), Thu "sempat lewat Rp18.400" with a REKOR sticker, Thu close Rp18.364, 5.242 IHSG, Rp1 juta = about 54 dolar. OK.
- USTR: "sampai 18%", Indonesia/Malaysia/Cambodia <=18%, Vietnam <=35%, India <=25%, "MASIH USULAN, belum berlaku, dengar pendapat Januari 2027". OK, apart from the headline in fix 2.
- CPNS counter animates 153.940 -> settles on 154.052 (matches the script). Transient only.
- 732 MPR (580 DPR + 152 DPD), 14 countries, Anthropic US$83/97, Nvidia +31.48%/-5.86%, OCTA Rp100 ribu: all match the script.

## Checklist

- Hook in the first 15 s: OK. "Dua nama masuk, rupiah tembus rekor. Lalu apa?" at 00:00, with a promise of the Monday payoff.
- Flow: intro -> BAB 1-5 -> "Minggu depan / Catat tanggalnya" -> outro (question + follow): OK.
- Chapter lengths: 30 / 85 / 62 / 74 / 70 / 59 / 68 / 14 s. BAB 1 is the longest at 85 s because of its nine beats. This is acceptable, but trim a5 or a6 if you want it tighter.
- Pacing: freezedetect found no frozen stretch of 4 s or more. Nothing is held for more than 6 s.
- Repetition (minor, no fix needed): "Ingat" closes both ch 2 (b9) and ch 3 (c9). Four chapters hinge on "Tapi ...". The intro and outro summaries deliberately mirror each other.
- Typography and colours: consistent across all chapters (paper background, ink/orange/yellow, same header chips).
- YouTube description chapters: 00:00, 00:30, 01:55, 02:57, 04:11, 05:21, 06:20, 07:28 match the cumulative chapter durations (29.8, 114.8, 177.1, 251.0, 320.8, 379.9, 447.9). Eight chapters, all at least 14 s, starting at 00:00. OK.
- Thumbnail: no faces, readable at small size, ">18.400 Rp/US$ sempat, Kamis siang" and "Tarif AS <=18% usulan" are accurate. OK.
