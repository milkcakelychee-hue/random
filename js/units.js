// ตัวคูณเป็นหน่วยฐานของหมวด (weight=g, volume=ml, length=cm)
export const UNITS = {
  g:    { cat: 'weight', label: 'กรัม',  factor: 1 },
  kg:   { cat: 'weight', label: 'กก.',   factor: 1000 },
  lb:   { cat: 'weight', label: 'ปอนด์', factor: 453.59237 },
  ml:   { cat: 'volume', label: 'มล.',   factor: 1 },
  l:    { cat: 'volume', label: 'ลิตร',  factor: 1000 },
  floz: { cat: 'volume', label: 'ออนซ์', factor: 29.5735295625 }, // US fluid ounce
  cm:   { cat: 'length', label: 'ซม.',   factor: 1 },
  m:    { cat: 'length', label: 'ม.',    factor: 100 },
  in:   { cat: 'length', label: 'นิ้ว',  factor: 2.54 },
  ft:   { cat: 'length', label: 'ฟุต',   factor: 30.48 },
};

export const CATEGORIES = {
  weight: { label: 'น้ำหนัก',  units: ['g', 'kg', 'lb'] },
  volume: { label: 'ปริมาตร',  units: ['ml', 'l', 'floz'] },
  length: { label: 'ความยาว', units: ['cm', 'm', 'in', 'ft'] },
};

export const toBase = (value, unit) => value * UNITS[unit].factor;
export const convert = (value, from, to) => toBase(value, from) / UNITS[to].factor;
