import { APP_VERSION } from './version.js';

// ขั้น 1: แสดงหัวข้อหน้าแรกชั่วคราว router และหน้าเต็มมาในขั้น 3
document.getElementById('app').innerHTML = `
  <h1 class="page-title">คำนวณ</h1>
  <p class="page-sub">เลือกเครื่องมือที่ต้องการใช้</p>
`;

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register(`./sw.js?v=${APP_VERSION}`).catch(() => {});
  });
}
