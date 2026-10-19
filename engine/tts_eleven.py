"""ElevenLabs voice-over with exact timings.

Usage: python3 -I engine/tts_eleven.py <project> <account_dir> [male|female]

- Reads <project>/script.json (same format as tts.py). A line with "tagline": true (or id "rd")
  is replaced by the account's fixed tagline recording, so the signature moment always sounds identical.
- Everything before the tagline and everything after it are each generated in ONE request
  (natural flow between sentences) using /with-timestamps, then mapped back to lines/words.
- Writes build/voice.wav, build/timing.json, build/timing.js (same contract as tts.py).
- Key: ELEVENLABS_API_KEY from env or ~/.config/explainer-studio/.env (never in the repo).
"""
import base64, json, os, re, subprocess, sys, urllib.request
from pathlib import Path
import numpy as np
import soundfile as sf

SR = 44100


def key():
    """Key from env or ~/.config/explainer-studio/.env. If neither exists, return None:
    the cloud environment's network secret (header xi-api-key on api.elevenlabs.io) is attached by the proxy."""
    k = os.environ.get("ELEVENLABS_API_KEY")
    env = Path.home() / ".config/explainer-studio/.env"
    if not k and env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("ELEVENLABS_API_KEY="):
                k = line.split("=", 1)[1].strip()
    return k


def decode(mp3_bytes_or_path):
    src = mp3_bytes_or_path
    args = ["ffmpeg", "-loglevel", "error", "-i", "pipe:0" if isinstance(src, bytes) else str(src),
            "-ac", "1", "-ar", str(SR), "-f", "f32le", "pipe:1"]
    out = subprocess.run(args, input=src if isinstance(src, bytes) else None, capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.float32).copy()


def tts(text, voice_id, model, direction, settings=None):
    body = {"text": (direction + " " if direction else "") + text, "model_id": model,
            "voice_settings": settings or {"stability": 0.5}}
    if model == "eleven_v3":
        body["language_code"] = "id"
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128",
        data=json.dumps(body).encode(), headers={**({"xi-api-key": key()} if key() else {}), "Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=300))
    off = len(direction) + 1 if direction else 0
    al = r.get("normalized_alignment") or r["alignment"]
    return decode(base64.b64decode(r["audio_base64"])), al, off


def compress_pauses(audio, max_gap=0.24, thresh_db=-38):
    """Shorten every silence longer than max_gap to max_gap. Returns new audio and a time-map function."""
    win = int(0.01 * SR)
    n = len(audio) // win
    rms = np.sqrt(np.mean(audio[: n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    silent = 20 * np.log10(rms) < thresh_db
    keep_max = int(max_gap / 0.01)
    cuts = []  # (start_sample, removed_samples)
    i = 0
    while i < n:
        if silent[i]:
            j = i
            while j < n and silent[j]:
                j += 1
            if j - i > keep_max and i > 0 and j < n:  # internal pause only
                a = (i + keep_max // 2) * win
                b = (j - keep_max // 2) * win
                cuts.append((a, b - a))
            i = j
        else:
            i += 1
    if not cuts:
        return audio, (lambda t: t)
    pieces, last = [], 0
    for a, r in cuts:
        pieces.append(audio[last:a]); last = a + r
    pieces.append(audio[last:])
    out = np.concatenate(pieces)
    def tmap(t):
        x = t * SR
        removed = 0
        for a, r in cuts:
            if x >= a + r:
                removed += r
            elif x > a:
                removed += x - a
        return (x - removed) / SR
    return out, tmap


def norm(w):
    return re.sub(r"[^\w]", "", w.lower())


def segment(lines, voice, direction):
    """Generate one request for several lines; return audio and per-line/word timings (relative)."""
    parts, spans, pos = [], [], 0
    for ln in lines:
        s = ln.get("say", ln["text"])
        tag = (ln["tag"] + " ") if ln.get("tag") else ""  # per-line delivery direction, e.g. "[serious]"
        spans.append((pos + len(tag), pos + len(tag) + len(s)))
        parts.append(tag + s)
        pos += len(tag) + len(s) + 1
    text = " ".join(parts)
    audio, al, off = tts(text, voice["voice_id"], voice.get("model", "eleven_v3"), direction, voice.get("settings"))
    chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    # alignment covers the direction tag too; drop it
    chars, st, en = chars[off:], st[off:], en[off:]
    out = []
    for ln, (a, b) in zip(lines, spans):
        idx = [i for i in range(a, min(b, len(chars))) if not chars[i].isspace()]
        if not idx:
            continue
        ls, le = st[idx[0]], en[idx[-1]]
        say = ln.get("say", ln["text"])
        words = ln["text"].split()
        wl = []
        if "say" not in ln:  # exact word timings
            p = a
            for w in words:
                j = say.find(w, p - a)
                if j < 0:
                    break
                ws, we = a + j, a + j + len(w) - 1
                wl.append({"w": w, "start": round(st[ws], 3), "end": round(en[min(we, len(en) - 1)], 3)})
                p = a + j + len(w)
        if len(wl) != len(words):  # proportional fallback for lines with a pronunciation override
            wts = [max(1, len(re.findall(r"[aiueoAIUEO]+", w))) + 0.3 for w in words]
            tot, acc, wl = sum(wts), 0, []
            for w, k in zip(words, wts):
                s0 = ls + (le - ls) * acc / tot; acc += k
                wl.append({"w": w, "start": round(s0, 3), "end": round(ls + (le - ls) * acc / tot, 3)})
        out.append({"id": ln["id"], "text": ln["text"], "start": round(ls, 3), "end": round(le, 3), "words": wl})
    max_gap = voice.get("max_pause", 0.24)
    audio, tm = compress_pauses(audio, max_gap)
    for l in out:
        l["start"], l["end"] = round(tm(l["start"]), 3), round(tm(l["end"]), 3)
        for w in l["words"]:
            w["start"], w["end"] = round(tm(w["start"]), 3), round(tm(w["end"]), 3)
    return audio, out


def main(project, account, gender="male"):
    project, account = Path(project), Path(account)
    script = json.loads((project / "script.json").read_text())
    brand = json.loads((account / "brand.json").read_text())
    voice = brand["voices"][gender]
    direction = script.get("direction", "[engaging, conversational news explainer, clear]")
    lines = script["lines"]
    ti = next((i for i, l in enumerate(lines) if l.get("tagline") or l["id"] == "rd"), None)
    groups = [lines[:ti], lines[ti + 1:]] if ti is not None else [lines]

    lead, gap, tail = 0.3, script.get("tagline_gap", 0.25), script.get("tail", 1.0)
    track = [np.zeros(int(lead * SR), np.float32)]
    t, timing = lead, []
    for gi, g in enumerate(groups):
        if g:
            audio, tl = segment(g, voice, direction)
            for l in tl:
                l["start"] += t; l["end"] += t
                for w in l["words"]:
                    w["start"] = round(w["start"] + t, 3); w["end"] = round(w["end"] + t, 3)
            timing += tl
            track.append(audio); t += len(audio) / SR
        if gi == 0 and ti is not None:
            tag = decode(account / voice["tagline"])
            idx = np.where(np.abs(tag) > 0.01)[0]
            tag = tag[max(0, idx[0] - 400): idx[-1] + 2000]
            track.append(np.zeros(int(gap * SR), np.float32)); t += gap
            ln = lines[ti]
            dur = len(tag) / SR
            words = ln["text"].split()
            timing.append({"id": ln["id"], "text": ln["text"], "start": round(t, 3), "end": round(t + dur, 3),
                           "words": [{"w": w, "start": round(t + dur * i / len(words), 3),
                                      "end": round(t + dur * (i + 1) / len(words), 3)} for i, w in enumerate(words)]})
            track.append(tag); t += dur
            track.append(np.zeros(int(0.3 * SR), np.float32)); t += 0.3
    track.append(np.zeros(int(tail * SR), np.float32))
    voice_audio = np.concatenate(track)
    out = project / "build"; out.mkdir(exist_ok=True)
    sf.write(out / "voice.wav", voice_audio, SR)
    timing = sorted(timing, key=lambda l: l["start"])
    data = {"duration": round(len(voice_audio) / SR, 3), "voice": voice["name"], "lines": timing}
    (out / "timing.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
    (out / "timing.js").write_text("window.TIMING = " + json.dumps(data, ensure_ascii=False) + ";\n")
    print(f"voice {voice['name']}: {data['duration']}s, {len(timing)} lines")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "male")
