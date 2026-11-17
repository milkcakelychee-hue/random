import { toolHead } from './toolhead.js';

// ขั้น 3: มีแค่แถวหัวข้อ เนื้อหาหน้าทำในขั้นถัดไป
export function render(root) {
  root.innerHTML = toolHead('ส่วนลด');
}
