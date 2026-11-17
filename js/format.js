// ช่องว่างหรือพิมพ์ไม่ครบต้องเป็น NaN ห้ามเป็น 0 (Number('') === 0 จึงห้ามใช้)
export const parseNum = s => {
  const t = String(s ?? '').replace(/,/g, '').trim();
  return t === '' ? NaN : parseFloat(t);
};

// เงินบาท: ทศนิยม 2 ตำแหน่งเสมอ มีจุลภาคคั่นหลักพัน
export const fmtBaht = n =>
  n.toLocaleString('th-TH', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

// เปอร์เซ็นต์: ทศนิยมสูงสุด 1 ตำแหน่ง ตัด .0 ทิ้ง
export const fmtPct = n => {
  const r = Math.round(n * 10) / 10;
  return r.toLocaleString('th-TH', { minimumFractionDigits: 0, maximumFractionDigits: 1 });
};

// ผลแปลงหน่วย: ทศนิยมสูงสุด 4 ตำแหน่ง ตัดศูนย์ท้าย ถ้า 0 < |ค่า| < 0.0001 แสดง 6 ตำแหน่ง
export const fmtUnit = n => {
  const max = n !== 0 && Math.abs(n) < 0.0001 ? 6 : 4;
  return n.toLocaleString('th-TH', { minimumFractionDigits: 0, maximumFractionDigits: max });
};
