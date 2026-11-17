import { toolHead } from './toolhead.js';
import { icon } from '../icons.js';
import { UNITS, CATEGORIES, convert } from '../units.js';
import { parseNum, fmtUnit } from '../format.js';
import { getPrefs, setPrefs } from '../storage.js';

// หน่วยต้นทางเมื่อสลับไปหมวดที่หน่วยที่จำไว้ไม่อยู่ในหมวดนั้น (ตามดีไซน์)
const CAT_DEFAULT = { weight: 'kg', volume: 'l', length: 'm' };
const LONG_CHARS = 9; // ยาวกว่านี้ลดตัวเลขเป็น 26px

export function render(root) {
  const prefs = getPrefs();
  let cat = CATEGORIES[prefs.convertCategory] ? prefs.convertCategory : 'weight';
  let from = CATEGORIES[cat].units.includes(prefs.convertFromUnit) ? prefs.convertFromUnit : CAT_DEFAULT[cat];

  root.innerHTML = `
    ${toolHead('แปลงหน่วย')}
    <div class="tool-body">
      <div class="seg" role="group" aria-label="หมวดหน่วย">
        ${Object.entries(CATEGORIES).map(([k, c]) =>
          `<button type="button" class="seg-btn" data-cat="${k}">${c.label}</button>`).join('')}
      </div>
      <div class="surface conv-input">
        <div class="fld">
          <label class="fld-label" for="conv-val">ค่า</label>
          <div class="field"><input id="conv-val" type="text" inputmode="decimal" placeholder="0" autocomplete="off"></div>
        </div>
        <div class="fld">
          <span class="fld-label" id="conv-from-label">จากหน่วย</span>
          <div class="unit-pick">
            <span class="unit-pick-text"></span>${icon('chevron-down', 18)}
            <select id="conv-from" aria-labelledby="conv-from-label"></select>
          </div>
        </div>
      </div>
      <div class="conv-results" aria-live="polite"></div>
    </div>`;

  const input = root.querySelector('#conv-val');
  const select = root.querySelector('#conv-from');
  const pickText = root.querySelector('.unit-pick-text');
  const results = root.querySelector('.conv-results');

  function syncControls() {
    for (const b of root.querySelectorAll('.seg-btn')) {
      const on = b.dataset.cat === cat;
      b.classList.toggle('is-on', on);
      b.setAttribute('aria-pressed', on);
    }
    select.innerHTML = CATEGORIES[cat].units
      .map(u => `<option value="${u}">${UNITS[u].label}</option>`).join('');
    select.value = from;
    pickText.textContent = UNITS[from].label;
  }

  function renderResults() {
    const v = parseNum(input.value);
    if (!Number.isFinite(v)) {
      results.innerHTML = `
        <div class="surface conv-empty">
          <span class="empty-circle">${icon('arrow-left-right', 22)}</span>
          <span class="empty-text">ใส่ค่าที่ต้องการแปลง</span>
        </div>`;
      return;
    }
    results.innerHTML = CATEGORIES[cat].units.map(u => {
      const txt = fmtUnit(convert(v, from, u));
      const src = u === from;
      return `
        <button type="button" class="conv-row ${src ? 'is-src' : 'surface'}" data-unit="${u}" aria-label="${UNITS[u].label} ${txt}">
          <span class="conv-unit">${UNITS[u].label}</span>
          <span class="conv-num ${txt.length > LONG_CHARS ? 'is-long' : ''}">${txt}</span>
        </button>`;
    }).join('');
  }

  function setFrom(u) {
    from = u;
    setPrefs({ convertCategory: cat, convertFromUnit: from });
    syncControls();
    renderResults();
  }

  root.querySelector('.seg').addEventListener('click', e => {
    const b = e.target.closest('.seg-btn');
    if (!b || b.dataset.cat === cat) return;
    cat = b.dataset.cat;
    setFrom(CATEGORIES[cat].units.includes(from) ? from : CAT_DEFAULT[cat]);
  });
  select.addEventListener('change', () => setFrom(select.value));
  input.addEventListener('input', renderResults);
  results.addEventListener('click', e => {
    const row = e.target.closest('.conv-row');
    if (!row || row.dataset.unit === from) return;
    // ตั้งเป็นหน่วยต้นทางใหม่ โดยใช้ค่าในแถวนั้นเป็นค่าเริ่ม (ผลลัพธ์ทุกแถวจึงคงเดิม)
    const v = parseNum(input.value);
    input.value = String(+convert(v, from, row.dataset.unit).toFixed(10));
    setFrom(row.dataset.unit);
  });

  syncControls();
  renderResults();
}
