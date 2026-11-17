import { icon } from '../icons.js';

// แถวหัวข้อของหน้าเครื่องมือ: ปุ่มย้อนกลับ + หัวข้อ (ไม่มีคำอธิบาย)
export const toolHead = title => `
  <header class="tool-head">
    <a class="back-btn surface" href="#/" aria-label="ย้อนกลับ">${icon('arrow-left', 22)}</a>
    <h1 class="title-md">${title}</h1>
  </header>`;
