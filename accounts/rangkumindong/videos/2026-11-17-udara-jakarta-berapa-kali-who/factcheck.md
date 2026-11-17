VERDICT: FIX (1 issue)

Checked 17 Nov 2026 (MODE=full). IQAir re-pulled during the check: still showed the 05:00 reading.

| Claim | Verdict | What the source actually says | Source |
|---|---|---|---|
| l1/caption: IQAir, Selasa 17 Nov 2026, 05.00 WIB, US AQI 177, tidak sehat | OK (single source) | Live page: US AQI 177 "Tidak sehat", 05:00 17 Nov local time. The history table logs it as the 04:00–05:00 hour. **No second source found:** no 17 Nov news article (the Antara "Selasa pagi" article 5843011 is from 10 Nov: AQI 127, PM2.5 48), and the official udara.jakarta.go.id (ISPU) page's latest data was 16 Nov 12.30 WIB. Acceptable because IQAir is the primary monitor and the video attributes it ("Data IQAir"). **Re-pull before render.** | https://www.iqair.com/id/indonesia/jakarta/jakarta |
| l2/l3/caption: main pollutant PM2,5, 92 µg/m³ | OK (single source) | "PM2.5 … 92 µg/m³"; IQAir: "18,4 kali nilai panduan tahunan WHO" (92/5 = 18.4, consistent). | https://www.iqair.com/id/indonesia/jakarta/jakarta |
| l4/caption: WHO AQG 2021 PM2,5, 24-hour 15 µg/m³, annual 5 µg/m³ | OK | WHO compendium: PM2.5 annual 5 µg/m³; 24-hour 15 µg/m³ (99th percentile, i.e. 3–4 exceedance days/year). | https://cdn.who.int/media/docs/default-source/who-compendium-on-health-and-environment/who_compendium_chapter2.pdf?sfvrsn=14f84896_8 ; https://www.who.int/publications/i/item/9789240034228 |
| l4: "Kalau seharian begini? Sekitar 6 kali lipat" | OK | 92 ÷ 15 = 6.13. It's stated as a conditional, and the caption says it's not a measured daily average. Fair framing. | as above |
| l6: "itu baru angka satu jam" | OK | IQAir figure is an hourly reading (04:00–05:00). | IQAir |
| Caption: Senin 16 Nov 05.00, AQI 161, PM2,5 69,4 µg/m³ | OK | Koran Jakarta: "poin 161", "69,4 mikrogram per meter kubik", pukul 05.00, 13,9× the WHO annual guideline. | https://koran-jakarta.com/2026-11-16/iqair-senin-pagi-kualitas-udara-jakarta-tak-sehat-warga-disarankan-pakai-masker-di-luar-rumah |
| Caption: PM2,5 = partikel ≤ 2,5 mikrometer | OK | WHO: "PM smaller than or equal to 2.5 microns (µm) in diameter". | https://www.who.int/news-room/questions-and-answers/item/who-global-air-quality-guidelines |
| h2 / cover / titles / captions: "batas aman WHO" | **FIX** | The WHO AQG are recommended guideline levels, not a "safe" threshold. WHO's 24-h level even allows 3–4 exceedance days a year, and WHO notes health effects below the guideline levels. "Batas aman" overstates this and is a health claim. | WHO Q&A above |
| Health statements | OK | The only health claim is IQAir's category "tidak sehat", which is attributed. No cause claimed (smoke, vehicles). | IQAir |
| Pak Budi | OK | Labelled "misalnya" / "Ilustrasi" / "Pak Budi = ilustrasi". | n/a |
| On-screen vs spoken / captions vs script | OK | 177, 92, 15, ×6 are all spoken. Captions match the script. Not a market topic, so no disclaimer is needed. | n/a |

## FIX 1: "batas aman WHO" → "pedoman WHO" (APPLIED 17 Nov by writer: h2, YT title, first caption lines, optional Cara baca line + WHO Q&A source; script/draft/post/claims checked for "aman")
- **h2 text:** `Udara yang dia hirup: berapa kali batas WHO?` (say: `…berapa kali batas, We Ha O?`). Alternative: `berapa kali pedoman udara WHO?`
- **YouTube title:** `Udara Jakarta pagi ini: berapa kali batas pedoman WHO? #Shorts`
- **First line of IG/YouTube/TikTok caption:** `Udara Jakarta pagi ini: berapa kali batas pedoman WHO? 👇`
- Cover card "BERAPA KALI LIPAT?" is fine as is.
- Optional addition to the "Cara baca" bullet: `Pedoman WHO bukan "batas aman": WHO menyebut dampak kesehatan tetap ada di bawah angka itu.`

## Note (not blocking)
- The 17 Nov figure rests on one source (IQAir live). Re-pull IQAir right before render. If a 17 Nov Antara or Koran Jakarta article appears, add it as source 2.
