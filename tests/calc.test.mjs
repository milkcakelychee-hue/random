// รัน: node tests/calc.test.mjs  (ตัวอย่างทดสอบจาก BUILD_BRIEF "กติกาเป็นโค้ด")
import { parseNum, fmtBaht, fmtPct, fmtUnit } from '../js/format.js';
import { convert } from '../js/units.js';
import { compare, discount } from '../js/calc.js';

let fail = 0;
const eq = (name, got, want) => {
  const ok = got === want;
  if (!ok) fail++;
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${name}  →  ${got}${ok ? '' : `  (ต้องเป็น ${want})`}`);
};
const P = parseNum;

// parseNum: ช่องว่างต้องเป็น NaN
eq('parseNum("") เป็น NaN', Number.isNaN(P('')), true);
eq('parseNum("  ") เป็น NaN', Number.isNaN(P('  ')), true);
eq('parseNum(".") เป็น NaN', Number.isNaN(P('.')), true);
eq('parseNum("1,250.5")', P('1,250.5'), 1250.5);
eq('parseNum("0")', P('0'), 0);

// เทียบราคา
let r = compare({ qty: P('500'), unit: 'ml', price: P('25') }, { qty: P('1'), unit: 'l', price: P('45') });
eq('เทียบ: A ต่อ 100 มล.', fmtBaht(r.shownA), '5.00');
eq('เทียบ: B ต่อ 100 มล.', fmtBaht(r.shownB), '4.50');
eq('เทียบ: ผู้ชนะ', r.winner, 'B');
eq('เทียบ: ถูกกว่า %', fmtPct(r.savePct), '10');
eq('เทียบ: ป้ายหน่วย', r.label, '100 มล.');
eq('เทียบ ข้ามหมวด', compare({ qty: 500, unit: 'g', price: 10 }, { qty: 500, unit: 'ml', price: 10 }).status, 'mismatch');
eq('เทียบ เท่ากัน', compare({ qty: 1, unit: 'kg', price: 100 }, { qty: 1000, unit: 'g', price: 100 }).status, 'equal');
eq('เทียบ ราคาว่าง', compare({ qty: P('500'), unit: 'ml', price: P('') }, { qty: 1, unit: 'l', price: 45 }).status, 'empty');

// ส่วนลด
r = discount(1000, [{ type: 'percent', value: 20 }, { type: 'baht', value: 100 }]);
eq('ส่วนลด: ต้องจ่าย', fmtBaht(r.pay), '700.00');
eq('ส่วนลด: ลดไป', fmtBaht(r.totalOff), '300.00');
eq('ส่วนลด: %', fmtPct(r.offPct), '30');
r = discount(100, [{ type: 'baht', value: 150 }]);
eq('ส่วนลดเกิน: ต้องจ่าย', fmtBaht(r.pay), '0.00');
eq('ส่วนลดเกิน: ลดไป', fmtBaht(r.totalOff), '100.00');
eq('ส่วนลดเกิน: %', fmtPct(r.offPct), '100');
r = discount(1000, [{ type: 'percent', value: 20 }, { type: 'baht', value: 100 }, { type: 'percent', value: 10 }]);
eq('ผสม 3: ต้องจ่าย', fmtBaht(r.pay), '630.00');
eq('ผสม 3: ลดไป', fmtBaht(r.totalOff), '370.00');
eq('ผสม 3: %', fmtPct(r.offPct), '37');
eq('ส่วนลด ราคาเต็มว่าง', discount(P(''), []).status, 'empty');
eq('ส่วนลด รายการว่างข้ามไป', fmtBaht(discount(500, [{ type: 'percent', value: P('') }]).pay), '500.00');
eq('ส่วนลด % เกิน 100 ปรับเป็น 100', fmtBaht(discount(500, [{ type: 'percent', value: 150 }]).pay), '0.00');
eq('เงินคั่นหลักพัน', fmtBaht(1234567.891), '1,234,567.89');

// แปลงหน่วย
eq('1 ปอนด์ → กรัม', fmtUnit(convert(1, 'lb', 'g')), '453.5924');
eq('1 กก. → ปอนด์', fmtUnit(convert(1, 'kg', 'lb')), '2.2046');
eq('1 ฟุต → ซม.', fmtUnit(convert(1, 'ft', 'cm')), '30.48');
eq('1 ม. → นิ้ว', fmtUnit(convert(1, 'm', 'in')), '39.3701');
eq('1 ม. → ฟุต', fmtUnit(convert(1, 'm', 'ft')), '3.2808');
eq('ค่าเล็กมากแสดง 6 ตำแหน่ง', fmtUnit(convert(1, 'g', 'kg') / 10), '0.0001');
eq('ค่าเล็กกว่า 0.0001', fmtUnit(0.00005), '0.00005');

console.log(fail ? `\n${fail} ข้อไม่ผ่าน` : '\nผ่านทุกข้อ');
process.exit(fail ? 1 : 0);
