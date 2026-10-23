"""Per-day pipeline folder and hand-off checks for the agent setup.

  python3 -I engine/day.py init  <account_dir> <YYYY-MM-DD>      # create daily/<date>/ and status.json
  python3 -I engine/day.py check <sweep.json>                     # validate one researcher file
  python3 -I engine/day.py merge <account_dir> <YYYY-MM-DD>       # add new events from all sweeps to events.csv (dedup), render events.md
  python3 -I engine/day.py status <account_dir> <YYYY-MM-DD> [step=value ...]   # show / set step status
  python3 -I engine/day.py today <account_dir> <YYYY-MM-DD>       # today's brand.json bits only: schedule row,
        # weekday topic, rubric weights, hook-style notes (instead of reading all of brand.json)
  python3 -I engine/day.py candidates <account_dir> <YYYY-MM-DD>  # compact list of today's sweep events for the
        # writer: score, signals, spreading evidence, short title, numbers, storyline, 2 source URLs (~1/3 of the raw JSON)

Day folder: <account_dir>/daily/<date>/
  sweep-markets.json · sweep-politics.json · sweep-business.json · sweep-national.json   (researchers)
  ideas.md · ideas-factcheck.md                                                          (writer, fact-checker)
  status.json                                                                            (coordinator)
"""
import datetime as dt, json, re, subprocess, sys
from pathlib import Path

AREAS = ["markets", "politics", "business", "national"]
CATS = {"MKT", "ECO", "BIZ", "TECH", "POL", "NEWS", "ENV", "GLB"}
STEPS = ["sweep", "merge", "ideas", "ideas_factcheck", "ideas_sent", "picked", "draft", "draft_factcheck",
         "draft_sent", "approved", "render", "video_sent", "ok_post", "posted", "knowledge"]
HERE = Path(__file__).resolve().parent


def day_dir(acct, date):
    return Path(acct) / "daily" / date


def init(acct, date):
    d = day_dir(acct, date)
    d.mkdir(parents=True, exist_ok=True)
    s = d / "status.json"
    if not s.exists():
        s.write_text(json.dumps({"date": date, "steps": {k: "todo" for k in STEPS}, "notes": []}, indent=1))
    print(d)


def check(path):
    errs = []
    try:
        j = json.loads(Path(path).read_text())
    except Exception as e:
        print(f"FAIL: not valid JSON: {e}"); sys.exit(1)
    if j.get("area") not in AREAS:
        errs.append(f"area must be one of {AREAS}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(j.get("run_date", ""))):
        errs.append("run_date must be YYYY-MM-DD")
    if not j.get("checked"):
        errs.append("checked: list every checklist item you searched")
    evs = j.get("events")
    if not isinstance(evs, list) or not evs:
        errs.append("events: must be a non-empty list")
        evs = []
    for i, e in enumerate(evs):
        p = f"events[{i}]"
        try:
            dt.date.fromisoformat(e.get("date", ""))
        except Exception:
            errs.append(f"{p}.date must be YYYY-MM-DD (use the start date for ranges)")
        if e.get("category") not in CATS:
            errs.append(f"{p}.category must be one of {sorted(CATS)}")
        if len(e.get("event", "")) < 15:
            errs.append(f"{p}.event too short")
        if e.get("status") not in ("verified", "partial", "upcoming"):
            errs.append(f"{p}.status must be verified|partial|upcoming")
        src = e.get("sources") or []
        if not src or not all(isinstance(s, dict) and str(s.get("url", "")).startswith("http") and s.get("label") for s in src):
            errs.append(f"{p}.sources must be a list of {{label, url}} with real http(s) URLs")
        sig = e.get("signals")
        keys = ("spreading", "wallet", "surprise", "visual", "fresh", "rivals")
        legacy = sig is None and isinstance(e.get("video_potential"), int) and str(j.get("run_date", "")) < "2026-10-21"
        if not legacy and (not isinstance(sig, dict) or any(sig.get(k) not in (0, 1, 2) for k in keys)):
            errs.append(f"{p}.signals must have {', '.join(keys)}, each 0, 1 or 2")
        if e.get("sensitivity", "normal") not in ("normal", "high"):
            errs.append(f"{p}.sensitivity must be normal|high")
    if errs:
        print("FAIL:\n- " + "\n- ".join(errs)); sys.exit(1)
    print(f"OK: {len(evs)} events")


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def merge(acct, date):
    sys.path.insert(0, str(HERE))
    import events as ev
    k = Path(acct) / "knowledge"
    rows = ev.load(k)
    known_urls = set(re.findall(r"<([^>]+)>", " ".join(r["sources"] for r in rows)))
    known_text = {norm(r["event"])[:80] for r in rows}
    new, skipped = [], 0
    d = day_dir(acct, date)
    for area in AREAS:
        f = d / f"sweep-{area}.json"
        if not f.exists():
            print(f"missing: {f.name}")
            continue
        for e in json.loads(f.read_text())["events"]:
            urls = [s["url"] for s in e["sources"]]
            if norm(e["event"])[:80] in known_text or (urls and all(u in known_urls for u in urls)):
                skipped += 1
                continue
            text = e["event"] + (f" (update of {e['update_of']})" if e.get("update_of") else "")
            new.append({"date": e["date"], "category": e["category"], "event": text,
                        "key_numbers": e.get("key_numbers", ""), "storyline": e.get("storyline", ""),
                        "status": e["status"], "sources": " ; ".join(f"{s['label']} <{s['url']}>" for s in e["sources"])})
            known_text.add(norm(e["event"])[:80]); known_urls.update(urls)
    tmp = d / "merge.json"
    tmp.write_text(json.dumps(new, ensure_ascii=False, indent=1))
    if new:
        ev.add(k, tmp)
    ev.render(k)
    st = d / "status.json"
    if st.exists():
        j = json.loads(st.read_text())
        j["merge_stats"] = {"new": len(new), "duplicates": skipped}
        st.write_text(json.dumps(j, indent=1, ensure_ascii=False))
    print(f"merged {len(new)} new events, skipped {skipped} duplicates")


def status(acct, date, sets):
    s = day_dir(acct, date) / "status.json"
    j = json.loads(s.read_text())
    for kv in sets:
        key, val = kv.split("=", 1)
        if key == "note":
            j["notes"].append(f"{dt.datetime.now(dt.timezone.utc):%H:%MZ} {val}")
        else:
            j["steps"][key] = val
    s.write_text(json.dumps(j, indent=1, ensure_ascii=False))
    print(" · ".join(f"{k}={v}" for k, v in j["steps"].items() if v != "todo") or "nothing done yet")


def candidates(acct, date):
    d = day_dir(acct, date)
    rows = []
    for area in AREAS:
        f = d / f"sweep-{area}.json"
        if not f.exists():
            print(f"# missing sweep-{area}.json"); continue
        j = json.loads(f.read_text())
        for e in j["events"]:
            s = e.get("signals", {})
            rows.append((sum(s.values()), area, e))
        if j.get("gaps"):
            g = j["gaps"] if isinstance(j["gaps"], str) else "; ".join(map(str, j["gaps"]))
            print(f"# gaps {area}: {cut(g, 200)}")
    for tot, area, e in sorted(rows, key=lambda x: -x[0]):
        s = e.get("signals", {})
        sig = " ".join(f"{k[:2]}{v}" for k, v in s.items())
        src = " ".join(x["url"] for x in e.get("sources", [])[:2])
        print(f"[{tot}/12 {sig}] {area} {e['date'][5:10]} {e['category']} {e.get('status', '')[:1]}"
              f"{' sens:' + e['sensitivity'] if e.get('sensitivity') not in (None, '', 'normal') else ''}"
              f"{' ^' + e['update_of'] if e.get('update_of') else ''}{' #' + e['storyline'] if e.get('storyline') else ''}\n"
              f"  {cut(e['event'], 160)}\n  n: {cut(e.get('key_numbers', ''), 180)}\n"
              f"  trend: {cut(e.get('spreading_evidence', ''), 100)}\n  src: {src}")


def today(acct, date):
    b = json.loads((Path(acct) / "brand.json").read_text())
    e = b.get("experiments", {})
    row = next((r for r in e.get("schedule", []) if r.get("date") == date), None)
    wd = dt.date.fromisoformat(date).strftime("%a").lower()
    print("schedule:", json.dumps(row, ensure_ascii=False))
    print("topic_today:", (b.get("topic_rotation") or {}).get(wd, ""))
    print("rubric_weights:", json.dumps(b.get("rubric_weights", {}), ensure_ascii=False))
    hs = e.get("hook_styles")
    if hs and row:
        pick = {k: v for k, v in (hs.items() if isinstance(hs, dict) else []) if k in (row.get("hook"), row.get("hook_b"))}
        print("hook_styles:", json.dumps(pick or hs, ensure_ascii=False))


def cut(s, n):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[:n - 1] + "…"


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "init":
        init(sys.argv[2], sys.argv[3])
    elif c == "check":
        check(sys.argv[2])
    elif c == "merge":
        merge(sys.argv[2], sys.argv[3])
    elif c == "today":
        today(sys.argv[2], sys.argv[3])
    elif c == "candidates":
        candidates(sys.argv[2], sys.argv[3])
    elif c == "status":
        status(sys.argv[2], sys.argv[3], sys.argv[4:])
