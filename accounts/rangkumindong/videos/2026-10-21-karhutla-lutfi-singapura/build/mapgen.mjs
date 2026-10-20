// Map snippets for this video (Natural Earth 110m via styles/sticker/data). Writes build/map.js
import { readFileSync, writeFileSync } from 'node:fs';
import { feature } from 'topojson-client';
import { geoMercator, geoPath } from 'd3-geo';
const topo = JSON.parse(readFileSync(new URL('../../../../../styles/sticker/data/countries-110m.json', import.meta.url)));
const land = feature(topo, topo.objects.countries);
const box = (lon0, lat0, lon1, lat1) => ({ type: 'Feature', geometry: { type: 'Polygon', coordinates: [[[lon0, lat0], [lon0, lat1], [lon1, lat1], [lon1, lat0], [lon0, lat0]]] } });
function make(W, H, ext, pts) {
  const proj = geoMercator().fitExtent([[0, 0], [W, H]], box(...ext));
  const p = geoPath(proj);
  const get = (n) => land.features.filter((f) => f.properties.name === n).map((f) => p(f)).join(' ');
  const others = land.features.filter((f) => !['Indonesia'].includes(f.properties.name)).map((f) => p(f)).filter(Boolean)
    .filter((d) => !/NaN/.test(d)).join(' ');
  const P = {}; for (const k in pts) P[k] = proj(pts[k]).map((v) => Math.round(v));
  return { W, H, indo: get('Indonesia'), others, P };
}
const pts = { kalteng: [113.4, -1.6], sumsel: [104.4, -3.3], kalsel: [115.4, -2.9], kalbar: [110.6, -0.2], jambi: [102.9, -1.7], riau: [101.7, 0.4], sg: [103.82, 1.35] };
const M = { big: make(960, 600, [95.0, -6.4, 119.6, 6.2], pts), sg: make(900, 760, [99.0, -3.6, 106.6, 3.2], pts) };
writeFileSync(new URL('./map.js', import.meta.url), 'window.MAP = ' + JSON.stringify(M) + ';\n');
console.log(M.big.P, M.sg.P, M.big.indo.length, M.sg.indo.length);
