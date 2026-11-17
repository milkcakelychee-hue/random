import { toolHead } from './toolhead.js';
import { icon } from '../icons.js';
import { parseNum, fmtBaht, fmtPct } from '../format.js';
import { discount } from '../calc.js';

const rowHTML = () => `
  <div class="surface disc-row" data-type="percent">
    <div class="disc-head">
      <span class="disc-title"></span>
      <button type="button" class="disc-del">${icon('trash', 16)}ลบ</button>
    </div>
    <div class="disc-grid">
      <div class="field"><input type="text" inputmode="decimal" placeholder="0" autocomplete="off"></div>
      <div class="type-toggle" role="group">
        <button type="button" data-type="percent">%</button>
        <button type="button" data-type="baht">บาท</button>
      </div>
    </div>
  </div>`;

function resultHTML(r) {
  if (r.status === 'empty') {
    return `<div class="res-row res-row-start"><span class="res-circle">${icon('percent', 20)}</span><span class="res-note res-16">ใส่ราคาเต็มเพื่อเริ่มคำนวณ</span></div>`;
  }
  return `<div class="res-col disc-res">
    <div class="pay-line"><span class="res-mute">ต้องจ่าย</span><span class="pay-num">${fmtBaht(r.pay)}</span><span class="res-mute res-16">บาท</span></div>
    <span class="disc-off">ลดไป ${fmtBaht(r.totalOff)} บาท (${fmtPct(r.offPct)}% ของราคาเต็ม)</span>
  </div>`;
}

export function render(root) {
  root.innerHTML = `
    ${toolHead('ส่วนลด')}
    <div class="tool-body disc-body">
      <section class="res-card" aria-live="polite"></section>
      <div class="surface full-card">
        <label class="fld-label" for="disc-full">ราคาเต็ม (บาท)</label>
        <div class="field"><input id="disc-full" type="text" inputmode="decimal" placeholder="0.00" autocomplete="off"></div>
      </div>
      <div class="disc-list">${rowHTML()}</div>
      <button type="button" class="add-btn">${icon('plus', 18, 2)}เพิ่มส่วนลด</button>
      <div class="disc-foot">
        <span class="disc-hint">ส่วนลดคิดต่อกันตามลำดับ</span>
        <button type="button" class="text-btn disc-clear">ล้างทั้งหมด</button>
      </div>
    </div>`;

  const $ = s => root.querySelector(s);
  const res = $('.res-card');
  const list = $('.disc-list');
  const full = $('#disc-full');

  function syncRows() {
    [...list.children].forEach((row, i) => {
      const n = i + 1;
      row.querySelector('.disc-title').textContent = `ส่วนลดที่ ${n}`;
      row.querySelector('.disc-del').setAttribute('aria-label', `ลบส่วนลดที่ ${n}`);
      row.querySelector('input').setAttribute('aria-label', `ส่วนลดที่ ${n}`);
      row.querySelector('.type-toggle').setAttribute('aria-label', `ชนิดส่วนลดที่ ${n}`);
      for (const b of row.querySelectorAll('.type-toggle button')) {
        const on = b.dataset.type === row.dataset.type;
        b.classList.toggle('is-on', on);
        b.setAttribute('aria-pressed', on);
      }
    });
  }

  function update() {
    const items = [...list.children].map(row => ({
      type: row.dataset.type,
      value: parseNum(row.querySelector('input').value),
    }));
    res.innerHTML = resultHTML(discount(parseNum(full.value), items));
  }

  root.querySelector('.disc-body').addEventListener('input', update);

  // ช่อง % รับ 0–100 ถ้าเกินปรับเป็น 100 (ทำตอนออกจากช่อง ไม่ขัดตอนพิมพ์)
  list.addEventListener('focusout', e => {
    const row = e.target.closest('.disc-row');
    if (!row || e.target.tagName !== 'INPUT' || row.dataset.type !== 'percent') return;
    if (parseNum(e.target.value) > 100) { e.target.value = '100'; update(); }
  });

  list.addEventListener('click', e => {
    const row = e.target.closest('.disc-row');
    if (!row) return;
    const t = e.target.closest('.type-toggle button');
    if (t) {
      row.dataset.type = t.dataset.type;
      const inp = row.querySelector('input');
      if (t.dataset.type === 'percent' && parseNum(inp.value) > 100) inp.value = '100';
    } else if (e.target.closest('.disc-del')) {
      row.remove();
    } else return;
    syncRows();
    update();
  });

  $('.add-btn').addEventListener('click', () => {
    list.insertAdjacentHTML('beforeend', rowHTML());
    syncRows();
    update();
  });

  $('.disc-clear').addEventListener('click', () => {
    full.value = '';
    list.innerHTML = rowHTML();
    syncRows();
    update();
  });

  syncRows();
  update();
}
