import { toolHead } from './toolhead.js';
import { icon } from '../icons.js';
import { UNITS, CATEGORIES } from '../units.js';
import { parseNum, fmtBaht, fmtPct } from '../format.js';
import { compare } from '../calc.js';
import { getPrefs, setPrefs } from '../storage.js';

// ตัวเลือกหน่วยแบบเนทีฟ แบ่งกลุ่ม น้ำหนัก / ปริมาตร / ความยาว
const unitOptions = () => Object.values(CATEGORIES).map(c =>
  `<optgroup label="${c.label}">${c.units.map(u => `<option value="${u}">${UNITS[u].label}</option>`).join('')}</optgroup>`
).join('');

const optionCard = k => `
  <div class="surface opt-card" data-opt="${k}">
    <div class="opt-head">
      <span class="opt-title">ตัวเลือก ${k}</span>
      <span class="win-badge">${icon('check', 14, 2.2)}คุ้มกว่า</span>
    </div>
    <div class="opt-grid">
      <div class="fld">
        <label class="fld-label" for="q${k}">ปริมาณ</label>
        <div class="field field-unit">
          <input id="q${k}" type="text" inputmode="decimal" placeholder="0" autocomplete="off">
          <span class="unit-btn">
            <span class="unit-btn-text"></span>${icon('chevron-down', 16)}
            <select id="u${k}" aria-label="หน่วยของตัวเลือก ${k}">${unitOptions()}</select>
          </span>
        </div>
      </div>
      <div class="fld">
        <label class="fld-label" for="p${k}">ราคา (บาท)</label>
        <div class="field"><input id="p${k}" type="text" inputmode="decimal" placeholder="0.00" autocomplete="off"></div>
      </div>
    </div>
  </div>`;

const circle = name => `<span class="res-circle">${icon(name, 20)}</span>`;

function resultHTML(r) {
  if (r.status === 'empty') {
    return `<div class="res-row">${circle('scale')}<span class="res-note">กรอกปริมาณกับราคาทั้งสองตัวเลือกเพื่อดูผล</span></div>`;
  }
  if (r.status === 'mismatch') {
    return `<div class="res-col">
      <div class="res-line">${circle('ban')}<span class="res-big res-28">เทียบไม่ได้</span></div>
      <span class="res-small">ตัวเลือกคนละประเภทกัน (เช่น น้ำหนักกับปริมาตร)</span>
    </div>`;
  }
  const lineA = `A: ${fmtBaht(r.shownA)} บาท / ${r.label}`;
  const lineB = `B: ${fmtBaht(r.shownB)} บาท / ${r.label}`;
  if (r.status === 'equal') {
    return `<div class="res-col">
      <div class="res-line">${circle('equal')}<span class="res-big res-26">ราคาต่อหน่วยเท่ากัน</span></div>
      <div class="res-pair"><span class="res-tiny">${lineA}</span><span class="res-tiny">${lineB}</span></div>
    </div>`;
  }
  const w = r.winner;
  return `<div class="res-win">
    <div class="res-win-main">
      <div class="res-line"><span class="win-letter">${w}</span><span class="res-big res-30">คุ้มกว่า</span></div>
      <div class="res-save"><span class="res-mute">ถูกกว่า</span><span class="res-pct">${fmtPct(r.savePct)}%</span><span class="res-mute">ต่อหน่วย</span></div>
    </div>
    <div class="res-per">
      <span class="${w === 'A' ? 'is-win' : ''}">${lineA}</span>
      <span class="${w === 'B' ? 'is-win' : ''}">${lineB}</span>
    </div>
  </div>`;
}

export function render(root) {
  const prefs = getPrefs();
  root.innerHTML = `
    ${toolHead('เทียบราคา')}
    <div class="tool-body cmp-body">
      <section class="res-card" aria-live="polite"></section>
      ${optionCard('A')}
      ${optionCard('B')}
      <button type="button" class="text-btn clear-btn">ล้างทั้งหมด</button>
    </div>`;

  const $ = s => root.querySelector(s);
  const res = $('.res-card');
  const unitPref = { A: 'compareUnitA', B: 'compareUnitB' };

  for (const k of ['A', 'B']) {
    const sel = $(`#u${k}`);
    sel.value = UNITS[prefs[unitPref[k]]] ? prefs[unitPref[k]] : 'ml';
    $(`[data-opt="${k}"] .unit-btn-text`).textContent = UNITS[sel.value].label;
    sel.addEventListener('change', () => {
      $(`[data-opt="${k}"] .unit-btn-text`).textContent = UNITS[sel.value].label;
      setPrefs({ [unitPref[k]]: sel.value });
      update();
    });
  }

  const read = k => ({ qty: parseNum($(`#q${k}`).value), unit: $(`#u${k}`).value, price: parseNum($(`#p${k}`).value) });

  function update() {
    const r = compare(read('A'), read('B'));
    res.innerHTML = resultHTML(r);
    for (const k of ['A', 'B']) {
      root.querySelector(`[data-opt="${k}"]`).classList.toggle('is-win', r.status === 'ok' && r.winner === k);
    }
  }

  root.querySelector('.cmp-body').addEventListener('input', update);
  $('.clear-btn').addEventListener('click', () => {
    for (const el of root.querySelectorAll('.opt-card input')) el.value = '';
    update();
  });

  update();
}
