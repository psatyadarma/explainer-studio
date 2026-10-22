// Pak Budi — Rangkumin Dong's everyman character (original design, 22 Oct 2026). Approved by the user.
// K.budi(expr) returns an SVG string (viewBox 450×600). expr: neutral | shocked | happy | worried.
// Use: el.innerHTML = K.budi('shocked'); give the element class "sticker-svg" for the white outline.
// Swap expressions on beats (K.word timings); animate the wrapper (pop, bob, tilt). Never present him as a real person:
// story openings say "misalnya" / "anggap saja", and every number around him is real.
(function () {
window.K.budi = function (expr = "neutral") {
  const skin = '#C98E62', skinD = '#B07A50', hair = '#1E1A17', shirt = '#2F6E8F', sleeve = '#245A75', batik = '#FFD23F', ink = '#1B2430';
  const brow = { neutral: ['M150 168 q25 -8 50 0', 'M250 168 q25 -8 50 0'], shocked: ['M148 150 q27 -18 54 -2', 'M248 148 q27 -16 54 2'],
                 happy: ['M150 165 q25 -12 50 0', 'M250 165 q25 -12 50 0'], worried: ['M150 160 q25 4 50 -10', 'M250 150 q25 14 50 10'] }[expr];
  const mouth = { neutral: '<path d="M200 262 q25 10 50 0" stroke="'+ink+'" stroke-width="9" fill="none" stroke-linecap="round"/>',
                  shocked: '<ellipse cx="225" cy="272" rx="24" ry="30" fill="'+ink+'"/><ellipse cx="225" cy="284" rx="14" ry="10" fill="#E5675B"/>',
                  happy: '<path d="M190 252 q35 44 70 0 z" fill="'+ink+'"/><path d="M200 256 q25 10 50 0" fill="#fff"/>',
                  worried: '<path d="M198 274 q27 -18 54 0" stroke="'+ink+'" stroke-width="9" fill="none" stroke-linecap="round"/>' }[expr];
  const eyes = expr === 'happy' ? '<path d="M158 205 q17 -16 34 0" stroke="'+ink+'" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M258 205 q17 -16 34 0" stroke="'+ink+'" stroke-width="9" fill="none" stroke-linecap="round"/>'
    : `<circle cx="175" cy="203" r="${expr === 'shocked' ? 13 : 10}" fill="${ink}"/><circle cx="275" cy="203" r="${expr === 'shocked' ? 13 : 10}" fill="${ink}"/>`;
  const A = (d) => '<path d="'+d+'" stroke="'+sleeve+'" stroke-width="50" fill="none" stroke-linecap="round"/>';
  const H = (x, y) => '<circle cx="'+x+'" cy="'+y+'" r="27" fill="'+skin+'"/>';
  const arms = { neutral: A('M118 450 q-38 50 -40 118') + H(78, 582) + A('M332 450 q38 50 40 118') + H(372, 582),
    shocked: A('M118 448 q-80 -40 -52 -160') + H(62, 272) + A('M332 448 q80 -40 52 -160') + H(388, 272),
    happy: A('M118 450 q-38 50 -40 118') + H(78, 582) + A('M332 448 q86 -30 76 -160') + H(410, 276) + '<path d="M400 248 l0 -36" stroke="'+skin+'" stroke-width="20" stroke-linecap="round"/>',
    worried: A('M118 450 q-40 70 40 92') + A('M332 450 q40 70 -40 92') + '<rect x="160" y="500" width="130" height="80" rx="14" fill="#fff" stroke="'+ink+'" stroke-width="6"/><text x="225" y="553" font-size="34" font-weight="900" text-anchor="middle" fill="#FF5A36" font-family="Inter">Rp</text>' + H(162, 545) + H(288, 545) }[expr];
  return `<svg viewBox="0 0 450 600">
    <path d="M100 600 q0 -200 125 -200 q125 0 125 200 z" fill="${shirt}"/>
    <g fill="${batik}" opacity=".9"><circle cx="160" cy="500" r="9"/><circle cx="290" cy="500" r="9"/><circle cx="225" cy="560" r="9"/><circle cx="140" cy="570" r="7"/><circle cx="310" cy="570" r="7"/>
      <path d="M190 470 q35 -25 70 0 q-35 25 -70 0" /></g>
    <path d="M190 400 l35 45 l35 -45 z" fill="#fff"/>
    <rect x="198" y="340" width="54" height="70" rx="20" fill="${skinD}"/>
    ${arms}
    <ellipse cx="225" cy="215" rx="125" ry="140" fill="${skin}"/>
    <ellipse cx="102" cy="220" rx="20" ry="30" fill="${skin}"/><ellipse cx="348" cy="220" rx="20" ry="30" fill="${skin}"/>
    <path d="M100 190 q-5 -130 125 -130 q130 0 125 130 q-25 -70 -125 -75 q-100 5 -125 75 z" fill="${hair}"/>
    <path d="M${brow[0].slice(1)}" stroke="${hair}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path d="M${brow[1].slice(1)}" stroke="${hair}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <rect x="140" y="178" width="72" height="54" rx="18" fill="none" stroke="${ink}" stroke-width="7"/>
    <rect x="240" y="178" width="72" height="54" rx="18" fill="none" stroke="${ink}" stroke-width="7"/>
    <path d="M212 200 h28" stroke="${ink}" stroke-width="7"/>
    ${eyes}
    <path d="M225 220 q-8 22 6 26" stroke="${skinD}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M180 240 q45 12 90 0" stroke="${hair}" stroke-width="10" fill="none" stroke-linecap="round" opacity=".85"/>
    ${mouth}
    ${expr === 'worried' ? '<path d="M340 120 q10 20 0 32 q-10 -12 0 -32" fill="#7FC8F8"/>' : ''}
  </svg>`;
}
})();
