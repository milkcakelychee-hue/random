import { icon } from '../icons.js';

const TOOLS = [
  { href: '#/compare',  icon: 'scale',            name: 'เทียบราคา', desc: 'ของชิ้นไหนคุ้มกว่า' },
  { href: '#/discount', icon: 'percent',          name: 'ส่วนลด',    desc: 'ลดไปเท่าไหร่ จ่ายเท่าไหร่' },
  { href: '#/convert',  icon: 'arrow-left-right', name: 'แปลงหน่วย', desc: 'น้ำหนัก ปริมาตร ความยาว' },
];

export function render(root) {
  root.innerHTML = `
    <div class="home-head">
      <h1 class="title-xl">คำนวณ</h1>
      <p class="home-sub">เลือกเครื่องมือที่ต้องการใช้</p>
    </div>
    <div class="tool-grid">
      ${TOOLS.map(t => `
        <button type="button" class="tool-card surface" data-href="${t.href}">
          <span class="tool-top">
            ${icon(t.icon, 64, 0.9, 'tool-icon')}
            <span class="tool-arrow">${icon('arrow-up-right', 18)}</span>
          </span>
          <span class="tool-text">
            <span class="tool-name">${t.name}</span>
            <span class="tool-desc">${t.desc}</span>
          </span>
        </button>`).join('')}
    </div>`;
}
