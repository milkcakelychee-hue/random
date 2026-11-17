// สูตรเทียบราคาและส่วนลด (ไม่แตะ DOM เพื่อทดสอบได้) หน้า compare.js / discount.js เรียกใช้
import { UNITS, toBase } from './units.js';

// ราคาต่อหน่วยที่แสดง: weight ต่อ 100 g, volume ต่อ 100 ml, length ต่อ 1 m (=100 cm)
const DISPLAY_PER = { weight: 100, volume: 100, length: 100 };
const DISPLAY_LABEL = { weight: '100 กรัม', volume: '100 มล.', length: '1 เมตร' };

// a, b = { qty, unit, price } (qty/price จาก parseNum หรือ NaN)
export function compare(a, b) {
  const valid = x => x.qty > 0 && x.price >= 0 && Number.isFinite(x.qty) && Number.isFinite(x.price);
  if (!valid(a) || !valid(b)) return { status: 'empty' };
  const catA = UNITS[a.unit].cat, catB = UNITS[b.unit].cat;
  if (catA !== catB) return { status: 'mismatch' };
  const perBaseA = a.price / toBase(a.qty, a.unit);
  const perBaseB = b.price / toBase(b.qty, b.unit);
  const shownA = perBaseA * DISPLAY_PER[catA];
  const shownB = perBaseB * DISPLAY_PER[catA];
  const hi = Math.max(perBaseA, perBaseB), lo = Math.min(perBaseA, perBaseB);
  const savePct = hi === 0 ? 0 : ((hi - lo) / hi) * 100;
  if (savePct <= 0.005) return { status: 'equal', shownA, shownB, label: DISPLAY_LABEL[catA] };
  return { status: 'ok', winner: perBaseA < perBaseB ? 'A' : 'B', savePct, shownA, shownB, label: DISPLAY_LABEL[catA] };
}

// items = [{ type: 'percent' | 'baht', value: number|NaN }]
export function discount(full, items) {
  if (!(full > 0)) return { status: 'empty' };
  let remaining = full;
  for (const it of items) {
    const v = Number(it.value);
    if (!Number.isFinite(v) || v <= 0) continue;
    const cut = it.type === 'percent'
      ? remaining * (Math.min(v, 100) / 100)
      : v;
    remaining -= Math.min(cut, remaining);
  }
  const totalOff = full - remaining;
  return { status: 'ok', pay: remaining, totalOff, offPct: (totalOff / full) * 100 };
}
