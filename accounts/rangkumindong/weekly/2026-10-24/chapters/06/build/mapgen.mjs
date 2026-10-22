// Map snippets for weekly ch06 (Natural Earth 110m via styles/sticker/data). Writes build/map.js
import { readFileSync, writeFileSync } from 'node:fs';
import { feature } from 'topojson-client';
import { geoMercator, geoPath } from 'd3-geo';
const topo = JSON.parse(readFileSync(new URL('../../../../../../../styles/sticker/data/countries-110m.json', import.meta.url)));
const land = feature(topo, topo.objects.countries);
const box = (lon0, lat0, lon1, lat1) => ({ type: 'Feature', geometry: { type: 'Polygon', coordinates: [[[lon0, lat0], [lon0, lat1], [lon1, lat1], [lon1, lat0], [lon0, lat0]]] } });
function make(W, H, ext, pts) {
  const proj = geoMercator().fitExtent([[0, 0], [W, H]], box(...ext));
  const p = geoPath(proj);
  const indo = land.features.filter((f) => f.properties.name === 'Indonesia').map((f) => p(f)).join(' ');
  const others = land.features.filter((f) => f.properties.name !== 'Indonesia').map((f) => p(f)).filter((d) => d && !/NaN/.test(d)).join(' ');
  const P = {}; for (const k in pts) P[k] = proj(pts[k]).map((v) => Math.round(v));
  return { W, H, indo, others, P };
}
const pts = { kotim: [112.95, -2.53], merak: [106.0, -5.93] };
const M = { kal: make(1300, 760, [104.0, -8.6, 119.5, 2.0], pts), jawa: make(1300, 760, [101.5, -8.2, 111.5, -2.6], pts) };
writeFileSync(new URL('./map.js', import.meta.url), 'window.MAP = ' + JSON.stringify(M) + ';\n');
console.log(M.kal.P, M.jawa.P, M.kal.indo.length, M.jawa.indo.length);
