// Rangkumin Seminggu helpers (16:9). Load after ../sticker.js and build/timing.js; ../../../build/week.js gives WEEK.
// WEEK = {title, dates, chapters: [{n, title, kicker, start, dur}], total}; CHAPTER = this page's n.
(function () {
  window.FRAME = { w: 1920, h: 1080 };
  window.FRAME_ZOOM = window.FRAME_ZOOM ?? 1; window.FRAME_CY = window.FRAME_CY ?? 540;
  const K = window.K;
  K.W = 1920; K.H = 1080;
  K.cam16 = (world, keys, t) => K.camera(world, keys, t, 1920, 1080);

  // Chrome shared by every chapter: chapter label, whole-video progress with chapter ticks.
  K.weekly = (t) => {
    const W = window.WEEK, n = window.CHAPTER, ch = W && W.chapters.find((c) => c.n === n);
    if (!W || !ch) return;
    let track = document.getElementById('track');
    if (!track) {
      track = document.createElement('div'); track.id = 'track';
      W.chapters.slice(1).forEach((c) => { const i = document.createElement('i'); i.style.left = (c.start / W.total * 100) + '%'; track.appendChild(i); });
      document.getElementById('stage').appendChild(track);
      const lab = document.createElement('div'); lab.id = 'chap';
      lab.innerHTML = n > 0 && ch.title ? `<span class="n">${ch.kicker || 'BAB ' + n}</span><span class="t">${ch.title}</span>` : '';
      document.getElementById('stage').appendChild(lab);
    }
    const p = document.getElementById('progress');
    if (p) p.style.width = ((ch.start + t) / W.total * 100) + '%';
    const lab = document.getElementById('chap');
    lab.style.opacity = K.clamp((t - 2.2) / 0.3);
  };

  // Full-screen title card at the start of a chapter: in at 0, out at `hold` s.
  K.titleCard = (el, t, hold = 2.0) => {
    const s = K.spring(t + 0.05, 260, 20), out = K.easeInOut(K.prog(t, hold, 0.45));
    el.style.opacity = 1 - out;
    el.style.transform = `translateY(${-out * 140}px)`;
    el.querySelectorAll('.title, .kicker, .sub').forEach((e, i) => {
      const k = K.spring(t + 0.3 - 0.06 * i, 260, 18);
      e.style.transform = `scale(${0.7 + 0.3 * k})`; e.style.opacity = K.clamp(k * 1.5);
    });
    el.style.display = out >= 1 ? 'none' : 'flex';
  };

  // Lower third slides in at tIn and out at tOut.
  K.lower = (el, t, tIn, tOut) => {
    const s = K.spring(t - tIn, 240, 20), o = K.easeInOut(K.prog(t, tOut, 0.35));
    el.style.opacity = t < tIn ? 0 : 1 - o;
    el.style.transform = `translateX(${(1 - s) * -80 - o * 80}px) scaleX(${0.8 + 0.2 * s})`;
  };
})();
