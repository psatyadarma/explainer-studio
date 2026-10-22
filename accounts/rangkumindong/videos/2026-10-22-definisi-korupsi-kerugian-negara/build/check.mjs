// QA helper: subtitle line counts, safe-area boxes, longest visual hold. node build/check.mjs (from repo root: node <dir>/build/check.mjs <dir>)
import { chromium } from 'playwright-core';
import sparticuz from '@sparticuz/chromium';
import path from 'node:path';
const dir = path.resolve(process.argv[2]);
const browser = await chromium.launch({ executablePath: await sparticuz.executablePath(), args: sparticuz.args });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto('file://' + path.join(dir, 'index.html'));
await page.evaluate(() => document.fonts.ready);
const res = await page.evaluate(() => {
  const out = { subs: [], safe: [], holds: [] };
  const T = window.TIMING, subs = document.getElementById('subs');
  for (const l of T.lines) { window.seek((l.start + l.end) / 2); const lh = parseFloat(getComputedStyle(subs).lineHeight);
    out.subs.push([l.id, Math.round(subs.scrollHeight / lh), Math.round(subs.getBoundingClientRect().bottom)]); }
  const els = [...document.querySelectorAll('#world .abs, #world .ntag')];
  const bad = {};
  let prevSig = '', lastChange = 0;
  const endT = T.lines.find((l) => l.id === 'end').start;
  for (let t = 0; t < T.duration; t += 0.25) {
    window.seek(t - 0.06); const w0 = document.getElementById('world').style.transform.replace(/scale\([^)]*\)/, '');
    window.seek(t); const w1 = document.getElementById('world').style.transform.replace(/scale\([^)]*\)/, '');
    const moving = w0 !== w1;
    const sig = [];
    for (const e of els) {
      const op = parseFloat(getComputedStyle(e).opacity);
      const r = e.getBoundingClientRect();
      if (op < 0.05 || r.bottom < 0 || r.top > 1920 || r.right < 0 || r.left > 1080) continue;
      if (r.width === 0) continue;
      sig.push(e.id + Math.round(r.x / 6) + ',' + Math.round(r.y / 6) + ',' + Math.round(r.width / 6) + (e.textContent || '').length);
      if (!moving && op > 0.9 && (r.left < 60 || r.right > 920 || r.top < 240 || r.bottom > 1480) && e.id !== 'stamp') {
        const k = e.id || e.className; (bad[k] ||= []).push([+t.toFixed(2), [r.left, r.top, r.right, r.bottom].map(Math.round)]);
      }
    }
    const s = sig.join('|');
    if (s !== prevSig) { if (t - lastChange > 3.0 && t < endT) out.holds.push([+lastChange.toFixed(2), +t.toFixed(2)]); lastChange = t; prevSig = s; }
  }
  out.safe = Object.entries(bad).map(([k, v]) => [k, v.length, v[0], v[v.length - 1]]);
  return out;
});
console.log('SUBS (id, lines, bottom px):', JSON.stringify(res.subs));
console.log('SAFE-AREA violations (moving frames included):', JSON.stringify(res.safe, null, 0));
console.log('HOLDS >3 s without a visual change:', JSON.stringify(res.holds));
await browser.close();
