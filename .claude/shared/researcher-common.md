# Shared rules for every news researcher (read this first)

You are one of four parallel news researchers for **Rangkumin Dong**, a Bahasa Indonesia short-video account that explains Indonesian business, market, tech and political news. Your only output is one JSON file. The coordinator merges the four files into the events database and builds the day's video ideas from them.

## Inputs
- `accounts/rangkumindong/knowledge/events.csv` — what we already know (last 14 days). Do not re-report an event already there unless there is a **new development** (then report it as a new event with `"update_of": "<id>"`).
- `accounts/rangkumindong/knowledge/storylines/*.md` — active stories. Check each one in your area for new developments.
- Your area brief (the file that told you to read this one).

## How to search
- Window: the last 48 hours before the run date (Asia/Makassar time), plus anything scheduled in the next 14 days (mark `"status": "upcoming"`).
- Search **every item on your checklist separately**, in Bahasa Indonesia first (e.g. "KPK hari ini", "putusan MK terbaru", "IHSG ditutup"), then English if useful. Generic "berita hari ini" searches are not enough — that is how big stories get missed.
- Use WebSearch, then WebFetch the actual article for numbers. Never take numbers from a search snippet alone.
- **Search engines lag 1–3 days on Indonesian news.** For the last 48 h, also WebFetch outlet index pages directly and read the latest headlines, e.g. `https://nasional.kompas.com/`, `https://news.detik.com/berita`, `https://www.cnnindonesia.com/nasional`, `https://www.antaranews.com/politik`, `https://www.cnbcindonesia.com/news`, `https://www.kontan.co.id/`, `https://www.tempo.co/` and the institution's own site (e.g. `https://www.kpk.go.id/id/berita`, `https://www.mkri.id/`, `https://www.kejaksaan.go.id/`). If one blocks you, try another. Known (19 Oct): detik, cnbcindonesia, bisnis, katadata, cnnindonesia work; kompas.com, kpk.go.id, kejaksaan.go.id and idx.co.id often can't be read; kontan.co.id may return a stale cache (check article dates).
- If a checklist item yields nothing from the last 48 h after both methods, list it in `gaps` as "no news found for X since <date>" so the coordinator knows it was checked.
- Prefer primary sources (BI, OJK, BEI/IDX, BPS, ministries, court rulings, company filings) and major outlets (Kompas, Detik, CNN Indonesia, Tempo, Antara, CNBC Indonesia, Kontan, Bisnis, Katadata, Reuters, Bloomberg).
- `status`: `verified` = 2+ independent sources agree, or one primary source; `partial` = one secondary source, or details unclear; `upcoming` = scheduled future event.

## Output — write exactly this file
Path: `accounts/rangkumindong/daily/<RUN_DATE>/sweep-<AREA>.json` (the coordinator gives you RUN_DATE and AREA). JSON, UTF-8:

```json
{
  "area": "<AREA>",
  "run_date": "YYYY-MM-DD",
  "checked": ["every checklist item you searched, e.g. \"MK\", \"KPK\", \"Kompas terpopuler\""],
  "events": [
    {
      "date": "YYYY-MM-DD",
      "category": "MKT|ECO|BIZ|TECH|POL|NEWS|ENV|GLB",
      "event": "One neutral English sentence: who did what. Indonesian names/terms kept as-is.",
      "key_numbers": "All the numbers that matter, with units and dates, separated by ' · '",
      "storyline": "existing storyline slug, a proposed new slug, or empty",
      "update_of": "E00xx or empty",
      "status": "verified|partial|upcoming",
      "sources": [{"label": "Outlet", "url": "https://..."}],
      "why_it_matters": "One line for a general Indonesian audience",
      "signals": {"spreading": 0, "wallet": 0, "surprise": 0, "visual": 0, "fresh": 0, "rivals": 0},
      "spreading_evidence": "where you saw it trending, e.g. \"CNBC terpopuler #2\", or empty",
      "sensitivity": "normal|high"
    }
  ],
  "gaps": ["things you saw mentioned but could not verify"]
}
```
- `signals`, each 0, 1 or 2 (the virality rubric; see playbook → Topic selection):
  - `spreading`: 2 = on an outlet's most-read list or reported trending on X/TikTok today; 1 = widely covered by several outlets; 0 = niche.
  - `wallet`: 2 = changes what many ordinary people pay, earn or can do; 1 = affects a group (investors, sellers, a region); 0 = no direct effect.
  - `surprise`: 2 = a shock number, a reversal, a conflict, or something people believe wrongly; 1 = notable; 0 = expected.
  - `visual`: 2 = one clear number, map or chart that lands in 3 seconds; 1 = needs some setup; 0 = abstract.
  - `fresh`: 2 = happened today/yesterday or has a date in the next 3 days; 1 = this week; 0 = older.
  - `rivals`: 2 = few explainer accounts have covered it; 1 = some; 0 = everyone has. 
  Score the angle that would make the best video, not the dullest reading of the story.
- `sensitivity: high` for allegations, ongoing court cases, elections, SARA, named private individuals.
- Aim for 5–15 events. Quality over quantity: no duplicates, no opinion pieces as events.
- Validate before finishing: `python3 -I engine/day.py check accounts/rangkumindong/daily/<RUN_DATE>/sweep-<AREA>.json`. Fix until it prints OK.

## Final reply to the coordinator
Three lines max: number of events, the single strongest video candidate, and any gap worth a second look. Do not paste the JSON.
