import { APP_VERSION, WHATS_NEW } from '../version.js';

export function render(root) {
  root.innerHTML = `
    <h1 class="title-xl settings-title">ตั้งค่า</h1>
    <div class="settings-body">
      <div class="surface about-card">
        <div class="about-text">
          <span class="fld-label">เกี่ยวกับแอป</span>
          <span class="about-name">random</span>
        </div>
        <button type="button" class="ver-btn" aria-haspopup="dialog">เวอร์ชัน ${APP_VERSION}</button>
      </div>
    </div>
    <div class="scrim" hidden>
      <div class="pop" role="dialog" aria-modal="true" aria-labelledby="pop-title" tabindex="-1">
        <div class="pop-head">
          <span class="fld-label">มีอะไรใหม่</span>
          <h2 id="pop-title" class="pop-title">เวอร์ชัน ${APP_VERSION}</h2>
        </div>
        <ul class="pop-list">${WHATS_NEW.map(t => `<li>${t}</li>`).join('')}</ul>
        <button type="button" class="pop-close">ปิด</button>
      </div>
    </div>`;

  const scrim = root.querySelector('.scrim');
  const pop = root.querySelector('.pop');
  const verBtn = root.querySelector('.ver-btn');

  const open = () => {
    scrim.hidden = false;
    document.body.classList.add('modal-open');
    pop.focus();
  };
  const close = () => {
    scrim.hidden = true;
    document.body.classList.remove('modal-open');
    verBtn.focus();
  };

  verBtn.addEventListener('click', open);
  root.querySelector('.pop-close').addEventListener('click', close);
  scrim.addEventListener('click', e => { if (e.target === scrim) close(); });
  scrim.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
}
