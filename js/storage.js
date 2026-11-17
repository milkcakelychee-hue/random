// อ่าน/เขียน localStorage ทั้งหมดอยู่ที่นี่ หน้าจอเรียกผ่านไฟล์นี้เท่านั้น
const KEY = 'random:prefs';
const DEFAULTS = {
  compareUnitA: 'ml',
  compareUnitB: 'ml',
  convertCategory: 'weight',   // 'weight' | 'volume' | 'length'
  convertFromUnit: 'kg',
};

export function getPrefs() {
  try {
    const raw = localStorage.getItem(KEY);
    return { ...DEFAULTS, ...(raw ? JSON.parse(raw) : {}) };
  } catch { return { ...DEFAULTS }; }
}

export function setPrefs(patch) {
  try { localStorage.setItem(KEY, JSON.stringify({ ...getPrefs(), ...patch })); } catch {}
}
// ไม่มี clearPrefs: แอปไม่มีปุ่มล้างค่า (ตัดออกตามดีไซน์)
