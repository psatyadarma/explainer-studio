"""Export the pipeline's data as JSON row files for the "Rangkumin Dong Studio" dashboard.

  python3 -I engine/dash_export.py <account_dir>      # writes <account_dir>/dashboard/data/*.json

Files (each a JSON array of row objects):
  runs.json         one row per day × research area: events found, verified/partial/upcoming, high-sensitivity,
                    checklist items searched, gaps, whether the file passed validation
  days.json         one row per day: pipeline step reached, events merged/duplicates, ideas, fact-check fixes
  ideas.json        the ideas offered each day (rank, title, recommended, storyline, sensitivity)
  videos.json       every drafted/posted video with experiment arm, QA sync result and links
  metrics.json      per video × platform × checkpoint (24 h / 72 h): views, avg % watched, 3-s hold, shares, saves, follows
  events.json       events database, last 30 days + upcoming
  experiments.json  the A/B schedule (voice, slot, hook) per date
Then upload ONLY the files listed on the "CHANGED:" line (hashes vs the last upload are kept in
dashboard/data/.uploaded.json), and record them after uploading:
  python3 -I engine/dash_export.py <account_dir> --mark runs ideas ...
"""
import csv, datetime as dt, hashlib, json, re, sys, subprocess
from pathlib import Path

AREAS = ["markets", "politics", "business", "national"]
STEP_ORDER = ["sweep", "merge", "ideas", "ideas_factcheck", "ideas_sent", "picked", "draft", "draft_factcheck",
              "draft_sent", "approved", "render", "video_sent", "ok_post", "posted", "knowledge"]
STEP_LABEL = {"sweep": "Research", "merge": "Events merged", "ideas": "Ideas written", "ideas_factcheck": "Ideas fact-checked",
              "ideas_sent": "Ideas sent", "picked": "Topic picked", "draft": "Draft written", "draft_factcheck": "Draft fact-checked",
              "draft_sent": "Draft sent", "approved": "Draft approved", "render": "Rendered", "video_sent": "Video sent",
              "ok_post": "OK post", "posted": "Posted", "knowledge": "Knowledge updated"}
HERE = Path(__file__).resolve().parent


def check_ok(path):
    r = subprocess.run([sys.executable, "-I", str(HERE / "day.py"), "check", str(path)], capture_output=True, text=True)
    return r.stdout.startswith("OK")


def runs_and_days(acct):
    runs, days = [], []
    for d in sorted((acct / "daily").glob("20??-??-??")):
        date = d.name
        for a in AREAS:
            f = d / f"sweep-{a}.json"
            if not f.exists():
                runs.append({"date": date, "area": a, "events": 0, "verified": 0, "partial": 0, "upcoming": 0,
                             "high_sensitivity": 0, "checked": 0, "gaps": 0, "valid": False, "file": "missing"})
                continue
            j = json.loads(f.read_text())
            ev = j.get("events", [])
            runs.append({"date": date, "area": a, "events": len(ev),
                         "verified": sum(e.get("status") == "verified" for e in ev),
                         "partial": sum(e.get("status") == "partial" for e in ev),
                         "upcoming": sum(e.get("status") == "upcoming" for e in ev),
                         "high_sensitivity": sum(e.get("sensitivity") == "high" for e in ev),
                         "checked": len(j.get("checked", [])), "gaps": len(j.get("gaps", [])),
                         "valid": check_ok(f), "file": "ok"})
        st = json.loads((d / "status.json").read_text()) if (d / "status.json").exists() else {"steps": {}}
        steps = st.get("steps", {})
        done = [s for s in STEP_ORDER if steps.get(s) == "done"]
        last = done[-1] if done else None
        fixes = None
        fc = d / "ideas-factcheck.md"
        if fc.exists():
            m = re.search(r"VERDICT:\s*(PASS|FIX)(?:\s*\((\d+))?", fc.read_text())
            if m:
                fixes = 0 if m.group(1) == "PASS" else int(m.group(2) or 1)
        ideas_n = len(re.findall(r"^## \d+\.", (d / "ideas.md").read_text(), re.M)) if (d / "ideas.md").exists() else 0
        ms = st.get("merge_stats", {})
        days.append({"date": date, "steps_done": len(done), "steps_total": len(STEP_ORDER),
                     "last_step": STEP_LABEL.get(last, "Not started"),
                     "next_step": next((STEP_LABEL[s] for s in STEP_ORDER if steps.get(s) != "done"), "Complete"),
                     "events_found": sum(r["events"] for r in runs if r["date"] == date),
                     "events_new": ms.get("new"), "duplicates": ms.get("duplicates"),
                     "ideas": ideas_n, "factcheck_fixes": fixes,
                     "areas_ok": sum(1 for r in runs if r["date"] == date and r["valid"])})
    return runs, days


def ideas(acct):
    out = []
    for d in sorted((acct / "daily").glob("20??-??-??")):
        f = d / "ideas.md"
        if not f.exists():
            continue
        txt = f.read_text()
        for m in re.finditer(r"^## (\d+)\.\s*(.+?)\n(.*?)(?=^## \d+\.|\Z)", txt, re.M | re.S):
            title, body = m.group(2).strip(), m.group(3)
            rec = "⭐" in title
            title = title.replace("⭐", "").strip()
            sl = re.search(r"\*\*Storyline:\*\*\s*([^·\n]+)", body)
            se = re.search(r"\*\*Sensitivity:\*\*\s*([A-Za-z]+)", body)
            slug = re.search(r"(new|continues)\W*\(?([a-z0-9-]+)", sl.group(1)) if sl else None
            story = (("new: " if slug.group(1) == "new" else "") + slug.group(2)) if slug else (sl.group(1).strip()[:40] if sl else "")
            part = re.search(r"PART (\d+)", body)
            out.append({"date": d.name, "rank": int(m.group(1)), "title": title, "recommended": rec,
                        "storyline": story + (f" (part {part.group(1)})" if part else ""),
                        "sensitivity": (se.group(1).lower() if se else "")})
    return out


def videos(acct, k):
    rows = []
    sched = {r["date"]: r for r in json.loads((acct / "brand.json").read_text()).get("experiments", {}).get("schedule", [])}
    cov = list(csv.DictReader(open(k / "covered.csv"))) if (k / "covered.csv").exists() else []
    for r in cov:
        if r["kind"] != "video":
            continue
        folder = acct / r["folder"] if r["folder"] else None
        q = json.loads((folder / "qa-sync.json").read_text()) if folder and (folder / "qa-sync.json").exists() else {}
        p = json.loads((folder / "posted.json").read_text()) if folder and (folder / "posted.json").exists() else {}
        dur = None
        if folder and (folder / "build/timing.json").exists():
            dur = json.loads((folder / "build/timing.json").read_text()).get("duration")
        arm = sched.get(r["date"], {})
        fmt = ""
        if folder and (folder / "script.json").exists():
            fmt = json.loads((folder / "script.json").read_text()).get("format", "")
        fmt = fmt or arm.get("format", "standard")
        links = p.get("links") or {}
        rows.append({"date": r["date"], "title": r["title"], "storyline": r["storyline"], "part": r["part"],
                     "status": r["status"], "voice": arm.get("voice", "").split(":")[-1], "slot": arm.get("slot", ""),
                     "hook": arm.get("hook", "").replace("_", " "), "hook_b": arm.get("hook_b", "").replace("_", " "), "format": fmt.replace("_", " "), "length_s": round(dur, 1) if dur else None,
                     "qa_sync": q.get("verdict"), "sync_median_ms": round(q["median_offset_s"] * 1000) if q else None,
                     "instagram": links.get("instagram", ""), "youtube": links.get("youtube", ""),
                     "folder": r["folder"]})
    return rows


def metrics(k):
    f = k / "metrics.csv"
    if not f.exists():
        return []
    out = []
    for r in csv.DictReader(open(f)):
        for c in ("views", "shares", "saves", "follows"):
            r[c] = int(r[c]) if r.get(c) not in (None, "", "n/a") else None
        for c in ("avg_watch_pct", "hold_3s_pct"):
            r[c] = float(r[c]) if r.get(c) not in (None, "", "n/a") else None
        r["hours"] = int(r["hours"])
        out.append(r)
    return out


def events(k):
    today = dt.date.today()
    out = []
    for r in csv.DictReader(open(k / "events.csv")):
        d = dt.date.fromisoformat(r["date"][:10])
        if d >= today - dt.timedelta(days=30):
            out.append({"id": r["id"], "date": r["date"][:10], "category": r["category"], "event": r["event"],
                        "key_numbers": r["key_numbers"], "storyline": r["storyline"], "status": r["status"],
                        "upcoming": d > today})
    return out


def main():
    acct = Path(sys.argv[1])
    k = acct / "knowledge"
    out = acct / "dashboard" / "data"
    up = out / ".uploaded.json"
    if "--mark" in sys.argv:
        seen = json.loads(up.read_text()) if up.exists() else {}
        for n in sys.argv[sys.argv.index("--mark") + 1:]:
            seen[n] = hashlib.sha256((out / f"{n}.json").read_bytes()).hexdigest()
        up.write_text(json.dumps(seen, indent=1)); print("marked", len(seen)); return
    out.mkdir(parents=True, exist_ok=True)
    runs, days = runs_and_days(acct)
    sched = json.loads((acct / "brand.json").read_text()).get("experiments", {}).get("schedule", [])
    exp = [{"date": r["date"], "voice": r["voice"].split(":")[-1], "slot": r["slot"], "hook": r["hook"].replace("_", " "),
            "format": r.get("format", "standard").replace("_", " "), "cycle": 1} for r in sched]
    # the rotation repeats with voices swapped (playbook → Experiments); show the next cycle too
    if sched:
        names = {"Pratama": "Cahaya", "Cahaya": "Pratama"}
        last = dt.date.fromisoformat(sched[-1]["date"])
        for i, r in enumerate(sched):
            exp.append({"date": (last + dt.timedelta(days=i + 1)).isoformat(),
                        "voice": names.get(r["voice"].split(":")[-1], r["voice"]), "slot": r["slot"],
                        "hook": r["hook"].replace("_", " "), "cycle": 2})
    data = {"runs": runs, "days": days, "ideas": ideas(acct), "videos": videos(acct, k), "metrics": metrics(k),
            "events": events(k), "experiments": exp}
    seen = json.loads(up.read_text()) if up.exists() else {}
    changed = []
    for name, rows in data.items():
        (out / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=0))
        if hashlib.sha256((out / f"{name}.json").read_bytes()).hexdigest() != seen.get(name):
            changed.append(name)
        print(f"{name}.json: {len(rows)} rows")
    print("CHANGED: " + (" ".join(changed) or "none"))


if __name__ == "__main__":
    main()
