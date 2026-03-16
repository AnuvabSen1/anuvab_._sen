<h1 id="talks"></h1>
<h2 style="margin: 60px 0px 10px;">Talks & Presentations</h2>

<style>
.talks-timeline { position: relative; padding-left: 24px; margin-top: 20px; }
.talks-timeline::before { content: ''; position: absolute; left: 8px; top: 0; bottom: 0; width: 2px; background: linear-gradient(180deg, #B3A369 0%, #e8e0c8 100%); border-radius: 1px; }

.talk-card { position: relative; background: #fff; border: 1px solid #eee; border-radius: 10px; padding: 20px 24px; margin-bottom: 16px; margin-left: 16px; transition: transform 0.25s ease, box-shadow 0.25s ease; }
.talk-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.07); border-color: #ddd; }
.talk-card::before { content: ''; position: absolute; left: -27px; top: 24px; width: 10px; height: 10px; background: #B3A369; border-radius: 100%; border: 3px solid #fafaf8; z-index: 1; }

.talk-card .talk-type { display: inline-block; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; padding: 3px 10px; border-radius: 4px; margin-bottom: 10px; }
.talk-type.oral { background: linear-gradient(135deg, #b31b1b, #d32f2f); color: #fff; }
.talk-type.invited { background: linear-gradient(135deg, #6a1b9a, #8e24aa); color: #fff; }
.talk-type.poster { background: linear-gradient(135deg, #1565c0, #1e88e5); color: #fff; }
.talk-type.lecture { background: linear-gradient(135deg, #00695c, #00897b); color: #fff; }

.talk-card .talk-title { font-weight: 600; font-size: 16px; color: #13294B; line-height: 1.4; margin-bottom: 8px; }
.talk-card .talk-venues { margin: 0; padding: 0; list-style: none; }
.talk-card .talk-venues li { padding: 6px 0; font-size: 14.5px; color: #555; display: flex; align-items: baseline; gap: 8px; border-bottom: 1px solid #f5f5f5; }
.talk-card .talk-venues li:last-child { border-bottom: none; }
.talk-card .talk-venues .venue-icon { font-size: 16px; flex-shrink: 0; }
.talk-card .talk-venues .venue-name { flex: 1; }
.talk-card .talk-venues .venue-loc { color: #999; font-size: 13px; margin-left: auto; white-space: nowrap; }

/* Dark mode */
body.dark-mode .talk-card { background: #161b22; border-color: #21262d; }
body.dark-mode .talk-card:hover { box-shadow: 0 6px 20px rgba(0,0,0,0.25); border-color: #30363d; }
body.dark-mode .talk-card::before { border-color: #0d1117; }
body.dark-mode .talk-card .talk-title { color: #e6edf3; }
body.dark-mode .talk-card .talk-venues li { color: #c9d1d9; border-bottom-color: #21262d; }
body.dark-mode .talk-card .talk-venues .venue-loc { color: #6e7681; }

@media (max-width: 768px) {
  .talk-card .talk-venues li { flex-wrap: wrap; }
  .talk-card .talk-venues .venue-loc { margin-left: 24px; margin-top: 2px; }
}
</style>

<div class="talks-timeline">

<!-- SSMRadNet WACV 2026 -->
<div class="talk-card">
  <span class="talk-type oral">Oral Presentation</span>
  <div class="talk-title">SSMRadNet: A Sample-wise State-Space Framework for Efficient and Ultra-Light Radar Segmentation and Object Detection</div>
  <ul class="talk-venues">
    <li>
      <span class="venue-icon">🎤</span>
      <span class="venue-name"><strong>IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2026)</strong></span>
      <span class="venue-loc">Tucson, Arizona, USA · Mar 2026</span>
    </li>
  </ul>
</div>

<!-- Benchmarking QAOA -->
<div class="talk-card">
  <span class="talk-type invited">Invited Talk</span>
  <div class="talk-title">Benchmarking Metaheuristic-Integrated QAOA against Quantum Annealing</div>
  <ul class="talk-venues">
    <li>
      <span class="venue-icon">🌏</span>
      <span class="venue-name"><strong>Quantum Information Processing (QIP 2024)</strong></span>
      <span class="venue-loc">Taipei, Taiwan · Jan 2024</span>
    </li>
    <li>
      <span class="venue-icon">🎓</span>
      <span class="venue-name">Guest Lecture for ECE 442, Indian Institute of Engineering Science & Technology</span>
      <span class="venue-loc">Shibpur, India</span>
    </li>
  </ul>
</div>

<!-- Quantum-Enhanced -->
<div class="talk-card">
  <span class="talk-type invited">Invited Talk</span>
  <div class="talk-title">Quantum-Enhanced Hybrid Classical Systems for Complex Data Interpretation</div>
  <ul class="talk-venues">
    <li>
      <span class="venue-icon">🇩🇪</span>
      <span class="venue-name"><strong>Quantum Computing Theory in Practice (QCTiP)</strong></span>
      <span class="venue-loc">Berlin, Germany</span>
    </li>
  </ul>
</div>

</div>
