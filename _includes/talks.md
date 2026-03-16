<h1 id="talks"></h1>
<h2 style="margin: 60px 0px 10px;">Talks & Presentations</h2>

<style>
.talks-grid { display: flex; flex-direction: column; gap: 14px; margin-top: 16px; }

.talk-year-label {
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #B3A369;
  margin: 20px 0 6px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.talk-year-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, #B3A369, transparent);
}

.talk-card {
  background: #fff;
  border: 1px solid #eee;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.talk-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 28px rgba(0,0,0,0.08);
  border-color: #ddd;
}

.talk-card-header {
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.talk-card-header.oral { background: linear-gradient(135deg, #fef2f2, #fee2e2); border-bottom: 2px solid #ef4444; }
.talk-card-header.upcoming { background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-bottom: 2px solid #22c55e; }
.talk-card-header.invited { background: linear-gradient(135deg, #faf5ff, #f3e8ff); border-bottom: 2px solid #8b5cf6; }
.talk-card-header.poster { background: linear-gradient(135deg, #eff6ff, #dbeafe); border-bottom: 2px solid #3b82f6; }

.talk-type-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}
.talk-type-badge.oral { background: #ef4444; color: #fff; }
.talk-type-badge.upcoming { background: #22c55e; color: #fff; }
.talk-type-badge.invited { background: #8b5cf6; color: #fff; }
.talk-type-badge.poster { background: #3b82f6; color: #fff; }

.talk-card-header .talk-title-text {
  font-weight: 600;
  font-size: 15.5px;
  color: #13294B;
  line-height: 1.4;
  flex: 1;
}

.talk-card-body { padding: 14px 24px; }

.talk-venue-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid #f5f5f5;
  font-size: 14.5px;
}
.talk-venue-row:last-child { border-bottom: none; }

.talk-venue-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}
.talk-venue-icon.conf { background: #fef3c7; }
.talk-venue-icon.lecture { background: #dbeafe; }
.talk-venue-icon.intl { background: #d1fae5; }

.talk-venue-info { flex: 1; }
.talk-venue-name { font-weight: 600; color: #333; font-size: 14px; }
.talk-venue-detail { color: #888; font-size: 13px; margin-top: 1px; }

.talk-venue-loc {
  color: #999;
  font-size: 12.5px;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
}
.talk-venue-loc svg { width: 12px; height: 12px; fill: #bbb; }

.talk-stats {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.talk-stat {
  background: #fff;
  border: 1px solid #eee;
  border-radius: 10px;
  padding: 14px 20px;
  text-align: center;
  min-width: 100px;
  transition: transform 0.2s;
}
.talk-stat:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
.talk-stat-num { font-size: 26px; font-weight: 700; color: #13294B; line-height: 1; }
.talk-stat-label { font-size: 12px; color: #888; margin-top: 4px; letter-spacing: 0.3px; }

/* Dark mode */
body.dark-mode .talk-card { background: #161b22; border-color: #21262d; }
body.dark-mode .talk-card:hover { box-shadow: 0 8px 28px rgba(0,0,0,0.3); border-color: #30363d; }
body.dark-mode .talk-card-header.oral { background: linear-gradient(135deg, #1c1012, #261416); border-bottom-color: #ef4444; }
body.dark-mode .talk-card-header.upcoming { background: linear-gradient(135deg, #0c1a10, #0f2615); border-bottom-color: #22c55e; }
body.dark-mode .talk-card-header.invited { background: linear-gradient(135deg, #1a1325, #1e1630); border-bottom-color: #8b5cf6; }
body.dark-mode .talk-card-header.poster { background: linear-gradient(135deg, #0c1929, #101d33); border-bottom-color: #3b82f6; }
body.dark-mode .talk-card-header .talk-title-text { color: #e6edf3; }
body.dark-mode .talk-venue-row { border-bottom-color: #21262d; }
body.dark-mode .talk-venue-name { color: #c9d1d9; }
body.dark-mode .talk-venue-detail { color: #6e7681; }
body.dark-mode .talk-venue-loc { color: #6e7681; }
body.dark-mode .talk-venue-loc svg { fill: #484f58; }
body.dark-mode .talk-venue-icon.conf { background: rgba(254,243,199,0.1); }
body.dark-mode .talk-venue-icon.lecture { background: rgba(219,234,254,0.1); }
body.dark-mode .talk-venue-icon.intl { background: rgba(209,250,229,0.1); }
body.dark-mode .talk-stat { background: #161b22; border-color: #21262d; }
body.dark-mode .talk-stat:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
body.dark-mode .talk-stat-num { color: #B3A369; }
body.dark-mode .talk-stat-label { color: #6e7681; }
body.dark-mode .talk-year-label { color: #B3A369; }
body.dark-mode .talk-year-label::after { background: linear-gradient(90deg, rgba(179,163,105,0.4), transparent); }

@media (max-width: 768px) {
  .talk-card-header { flex-direction: column; align-items: flex-start; gap: 8px; padding: 14px 16px; }
  .talk-card-body { padding: 12px 16px; }
  .talk-venue-row { flex-wrap: wrap; }
  .talk-venue-loc { margin-left: 48px; margin-top: 2px; width: 100%; }
  .talk-stats { gap: 10px; }
  .talk-stat { flex: 1; min-width: 80px; padding: 10px 14px; }
}
</style>

<!-- Stats -->
<div class="talk-stats">
  <div class="talk-stat">
    <div class="talk-stat-num">3</div>
    <div class="talk-stat-label">Oral / Invited</div>
  </div>
  <div class="talk-stat">
    <div class="talk-stat-num">5</div>
    <div class="talk-stat-label">Countries</div>
  </div>
  <div class="talk-stat">
    <div class="talk-stat-num">3</div>
    <div class="talk-stat-label">Continents</div>
  </div>
</div>

<div class="talks-grid">

<!-- 2026 -->
<div class="talk-year-label">2026</div>

<!-- SSMRadNet WACV 2026 -->
<div class="talk-card">
  <div class="talk-card-header oral">
    <span class="talk-type-badge oral">🎤 Oral</span>
    <div class="talk-title-text">SSMRadNet: A Sample-wise State-Space Framework for Efficient and Ultra-Light Radar Segmentation and Object Detection</div>
  </div>
  <div class="talk-card-body">
    <div class="talk-venue-row">
      <div class="talk-venue-icon conf">🏛️</div>
      <div class="talk-venue-info">
        <div class="talk-venue-name">IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2026)</div>
        <div class="talk-venue-detail">First Round Acceptance (~6% of submissions)</div>
      </div>
      <div class="talk-venue-loc">
        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        Tucson, Arizona · Mar 2026
      </div>
    </div>
  </div>
</div>

<!-- 2024 -->
<div class="talk-year-label">2024</div>

<!-- Benchmarking QAOA -->
<div class="talk-card">
  <div class="talk-card-header invited">
    <span class="talk-type-badge invited">✨ Invited</span>
    <div class="talk-title-text">Benchmarking Metaheuristic-Integrated QAOA against Quantum Annealing</div>
  </div>
  <div class="talk-card-body">
    <div class="talk-venue-row">
      <div class="talk-venue-icon intl">🌏</div>
      <div class="talk-venue-info">
        <div class="talk-venue-name">Quantum Information Processing (QIP 2024)</div>
        <div class="talk-venue-detail">Premier Quantum Computing Conference</div>
      </div>
      <div class="talk-venue-loc">
        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        Taipei, Taiwan · Jan 2024
      </div>
    </div>
    <div class="talk-venue-row">
      <div class="talk-venue-icon lecture">🎓</div>
      <div class="talk-venue-info">
        <div class="talk-venue-name">Science and Information Conference (SIC 2024)</div>
        <div class="talk-venue-detail">International conference on computing</div>
      </div>
      <div class="talk-venue-loc">
        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        London, UK
      </div>
    </div>
  </div>
</div>

<!-- Quantum-Enhanced -->
<div class="talk-card">
  <div class="talk-card-header invited">
    <span class="talk-type-badge invited">✨ Invited</span>
    <div class="talk-title-text">Quantum-Enhanced Hybrid Classical Systems for Complex Data Interpretation</div>
  </div>
  <div class="talk-card-body">
    <div class="talk-venue-row">
      <div class="talk-venue-icon intl">🇩🇪</div>
      <div class="talk-venue-info">
        <div class="talk-venue-name">Quantum Computing Theory in Practice (QCTiP)</div>
        <div class="talk-venue-detail">International workshop on quantum computing applications</div>
      </div>
      <div class="talk-venue-loc">
        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        Berlin, Germany
      </div>
    </div>
  </div>
</div>

</div>
