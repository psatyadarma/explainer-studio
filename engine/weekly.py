"""Build the weekly long-form video "Rangkumin Seminggu" (16:9) from chapters.

  python3 -I engine/weekly.py init     <week_dir>                     # script.json → chapters/NN/script.json
  python3 -I engine/weekly.py voice    <week_dir> <account> male|female [--piper]   # voice + mix per chapter
  python3 -I engine/weekly.py index    <week_dir>                     # chapter starts → build/week.js (+ YouTube chapters)
  python3 -I engine/weekly.py render   <week_dir> [--jobs 3]          # renders chapters in parallel
  python3 -I engine/weekly.py assemble <week_dir>                     # concat → out/video.mp4, −14 LUFS, chapter list
  python3 -I engine/weekly.py thumb    <week_dir>                     # thumbnail.html → out/thumbnail.jpg (1280×720)

<week_dir>/script.json:
  {"title": "Rangkumin Seminggu", "dates": "19–25 Okt 2026", "direction": "[...]",
   "chapters": [{"n": 0, "kicker": "INTRO", "title": "Minggu ini", "lines": [...]},
                {"n": 1, "kicker": "BAB 1", "title": "IHSG & MSCI", "lines": [...]}, ...]}
Lines use the daily format (id, text, say, tag; the tagline line only in chapter 0).
Each chapter folder gets its own index.html from a chapter-builder agent (template: styles/sticker/weekly/chapter-template.html).
"""
import json, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "styles/sticker/weekly/chapter-template.html"


def place(src, dst):
    """Copy a template, filling {{ROOT}} with the relative path from dst's folder back to the repo root."""
    import os
    rel = os.path.relpath(ROOT, Path(dst).parent.resolve()).replace(os.sep, "/") + "/"
    Path(dst).write_text(Path(src).read_text().replace("{{ROOT}}", rel))


def chapters(week):
    return sorted(p for p in (week / "chapters").glob("[0-9][0-9]") if p.is_dir())


def init(week):
    s = json.loads((week / "script.json").read_text())
    for c in s["chapters"]:
        d = week / "chapters" / f"{c['n']:02d}"
        d.mkdir(parents=True, exist_ok=True)
        (d / "script.json").write_text(json.dumps({"direction": s.get("direction", ""), "lines": c["lines"], "tail": c.get("tail", 0.6)},
                                                  ensure_ascii=False, indent=1))
        if not (d / "index.html").exists():
            place(TEMPLATE, d / "index.html")
        if (week / "sfx.json").exists() and not (d / "sfx.json").exists():
            (d / "sfx.json").write_text("[]")
    print(f"init: {len(s['chapters'])} chapters in {week / 'chapters'}")


def voice(week, account, gender, piper=False):
    for d in chapters(week):
        if piper:
            subprocess.run([sys.executable, "-I", str(ROOT / "engine/tts.py"), str(d)], check=True)
        else:
            subprocess.run([sys.executable, "-I", str(ROOT / "engine/tts_eleven.py"), str(d), account, gender], check=True)
        subprocess.run([sys.executable, "-I", str(ROOT / "engine/mix.py"), str(d)], check=True)
    index(week)


def fmt(t):
    t = int(round(t)); return f"{t // 60:02d}:{t % 60:02d}" if t < 3600 else f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}"


def index(week):
    s = json.loads((week / "script.json").read_text())
    meta = {c["n"]: c for c in s["chapters"]}
    out, t = [], 0.0
    for d in chapters(week):
        dur = json.loads((d / "build/timing.json").read_text())["duration"]
        n = int(d.name); c = meta.get(n, {})
        out.append({"n": n, "title": c.get("title", ""), "kicker": c.get("kicker", f"BAB {n}"), "start": round(t, 3), "dur": dur})
        t += dur
    week_js = {"title": s.get("title", "Rangkumin Seminggu"), "dates": s.get("dates", ""), "chapters": out, "total": round(t, 3)}
    (week / "build").mkdir(exist_ok=True)
    (week / "build/week.js").write_text("window.WEEK = " + json.dumps(week_js, ensure_ascii=False) + ";\n")
    # YouTube needs every chapter ≥ 10 s: a shorter one (e.g. the outro) folds into the chapter before it
    yt = "\n".join(f"{fmt(c['start'])} {c['title'] or c['kicker'].title()}" for i, c in enumerate(out) if i == 0 or c["dur"] >= 10)
    (week / "build/youtube-chapters.txt").write_text(yt + "\n")
    print(f"index: {len(out)} chapters, total {fmt(t)}\n{yt}")


def render(week, jobs=3):
    def one(d):
        r = subprocess.run(["node", str(ROOT / "engine/render.mjs"), str(d)], capture_output=True, text=True)
        return d.name, r.returncode, (r.stdout + r.stderr).strip().splitlines()[-1:]
    with ThreadPoolExecutor(jobs) as ex:
        for name, rc, last in ex.map(one, chapters(week)):
            print(f"chapter {name}: {'ok' if rc == 0 else 'FAILED'} {last}")


def assemble(week):
    vids = [d / "out/video.mp4" for d in chapters(week)]
    missing = [str(v) for v in vids if not v.exists()]
    if missing:
        sys.exit("assemble: missing " + ", ".join(missing))
    (week / "out").mkdir(exist_ok=True)
    lst = week / "out/concat.txt"
    lst.write_text("".join(f"file '{v.resolve()}'\n" for v in vids))
    tmp = week / "out/concat.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(tmp)], check=True)
    # one loudness pass over the whole programme (chapters were mixed separately)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp), "-c:v", "copy",
                    "-af", "loudnorm=I=-14:TP=-2:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    str(week / "out/video.mp4")], check=True)
    tmp.unlink(); lst.unlink()
    pj = week / "post.json"
    if pj.exists() and (week / "build/youtube-chapters.txt").exists():
        p = json.loads(pj.read_text()); yt = (week / "build/youtube-chapters.txt").read_text().strip()
        desc = re.sub(r"\n?BAB:\n.*?(?=\n\n|\Z)", "", p.get("youtube_description", ""), flags=re.S).rstrip()
        p["youtube_description"] = (desc + "\n\nBAB:\n" + yt).strip()
        pj.write_text(json.dumps(p, ensure_ascii=False, indent=1))
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(week / "out/video.mp4")],
                       capture_output=True, text=True).stdout.strip()
    print(f"assemble: {week / 'out/video.mp4'} ({float(d):.1f} s)")


def thumb(week):
    src = week / "thumbnail.html"        # the week's edited copy (keeps {{ROOT}}); made from the template on first run
    if not src.exists():
        shutil.copy(ROOT / "styles/sticker/weekly/thumbnail.html", src)
    tdir = week / "build/thumb"; tdir.mkdir(parents=True, exist_ok=True)
    place(src, tdir / "index.html")
    subprocess.run(["node", str(ROOT / "engine/render.mjs"), str(tdir), "--stills", "1", "--to", "0"], check=True, capture_output=True)
    png = sorted((tdir / "out/stills").glob("*.png"))[0]
    (week / "out").mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(png), "-q:v", "2", str(week / "out/thumbnail.jpg")], check=True)
    print(f"thumb: {week / 'out/thumbnail.jpg'}")


if __name__ == "__main__":
    c, week = sys.argv[1], Path(sys.argv[2]).resolve()
    a = sys.argv[3:]
    if c == "init": init(week)
    elif c == "voice": voice(week, a[0], a[1], "--piper" in a)
    elif c == "index": index(week)
    elif c == "render": render(week, int(a[a.index("--jobs") + 1]) if "--jobs" in a else 3)
    elif c == "assemble": assemble(week)
    elif c == "thumb": thumb(week)
    else: sys.exit(__doc__)
