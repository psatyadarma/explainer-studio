"""Re-voice only some lines of a finished take (e.g. a news update after render), splicing them into build/voice.wav.

  python3 -I engine/revoice.py <video_dir> <account_dir> [male|female] --lines l4,l11 [--speed 1.24]

- Edit the lines' "text"/"say" in <video_dir>/script.json first. Consecutive ids are voiced in ONE ElevenLabs
  request (natural flow); each group replaces the old audio from (first.start - 0.05) to (next line.start - 0.05).
- --speed: use the same factor the take was retimed with (build/timing.json "speed", written by retime.py;
  read automatically when present), so the new lines match the rest.
- Later lines shift by the length difference; everything keyed with K.at / K.word in index.html follows.
- Backup of the previous take in build/pre-revoice/ (overwritten each run). Then: mix.py → render.mjs.
"""
import json, shutil, sys
from pathlib import Path
import numpy as np
import soundfile as sf
sys.path.insert(0, str(Path(__file__).resolve().parent))
import tts_eleven as T
from retime import stretch

GAP = 0.22


def opt(name, default):
    return type(default)(sys.argv[sys.argv.index("--" + name) + 1]) if "--" + name in sys.argv else default


def main():
    args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and not sys.argv[i - 1].startswith("--")]
    vdir, adir = Path(args[0]), Path(args[1])
    gender = args[2] if len(args) > 2 else "male"
    ids = [x for x in opt("lines", "").split(",") if x]
    if not ids:
        sys.exit("revoice: pass --lines id1,id2")
    b = vdir / "build"
    script = json.loads((vdir / "script.json").read_text())
    voice = json.loads((adir / "brand.json").read_text())["voices"][gender]
    tim = json.loads((b / "timing.json").read_text())
    speed = opt("speed", float(tim.get("speed", 1.0)))
    if tim.get("voice") and tim["voice"] != voice["name"]:
        sys.exit(f"revoice: take is {tim['voice']}, not {voice['name']}")
    bk = b / "pre-revoice"; bk.mkdir(exist_ok=True)
    for n in ("voice.wav", "timing.json", "timing.js"):
        shutil.copy(b / n, bk / n)
    x, sr = sf.read(b / "voice.wav", dtype="float32")
    if T.SR != sr:
        sys.exit("revoice: sample-rate mismatch")
    order = [l["id"] for l in script["lines"]]
    groups, cur = [], []
    for i in sorted(ids, key=order.index):
        if cur and order.index(i) != order.index(cur[-1]) + 1:
            groups.append(cur); cur = []
        cur.append(i)
    groups.append(cur)
    direction = script.get("direction", "[engaging, conversational news explainer, clear]")[:60]
    L = tim["lines"]
    for g in reversed(groups):   # last first, so earlier positions stay valid
        lines = [next(l for l in script["lines"] if l["id"] == i) for i in g]
        audio, tl = T.segment(lines, voice, direction)
        nz = np.where(np.abs(audio) > 0.01)[0]
        a0 = max(0, nz[0] - int(0.03 * sr)); a1 = min(len(audio), nz[-1] + int(0.06 * sr))
        audio = stretch(audio[a0:a1], sr, speed)
        k0 = next(k for k, l in enumerate(L) if l["id"] == g[0])
        k1 = next(k for k, l in enumerate(L) if l["id"] == g[-1])
        s = L[k0]["start"] - 0.05
        e = (L[k1 + 1]["start"] - 0.05) if k1 + 1 < len(L) else tim["duration"] - script.get("tail", 1.0)
        new = np.concatenate([np.zeros(int(0.05 * sr), np.float32), audio, np.zeros(int(GAP * sr), np.float32)])
        x = np.concatenate([x[: int(s * sr)], new, x[int(e * sr):]])
        off = s + 0.05
        for l in tl:
            l["start"] = round(off + (l["start"] - a0 / sr) / speed, 3); l["end"] = round(off + (l["end"] - a0 / sr) / speed, 3)
            for w in l["words"]:
                w["start"] = round(max(off, off + (w["start"] - a0 / sr) / speed), 3); w["end"] = round(off + (w["end"] - a0 / sr) / speed, 3)
        d = len(new) / sr - (e - s)
        for l in L[k1 + 1:]:
            l["start"] = round(l["start"] + d, 3); l["end"] = round(l["end"] + d, 3)
            for w in l["words"]:
                w["start"] = round(w["start"] + d, 3); w["end"] = round(w["end"] + d, 3)
        L[k0:k1 + 1] = tl
        print(f"revoice {','.join(g)}: {e - s:.2f}s -> {len(new) / sr:.2f}s ({d:+.2f}s)")
    tim["lines"] = L
    tim["duration"] = round(len(x) / sr, 3)
    sf.write(b / "voice.wav", x, sr)
    (b / "timing.json").write_text(json.dumps(tim, ensure_ascii=False, indent=1))
    (b / "timing.js").write_text("window.TIMING = " + json.dumps(tim, ensure_ascii=False) + ";\n")
    print(f"revoice: {tim['duration']}s total; next: mix.py, render.mjs")


if __name__ == "__main__":
    main()
