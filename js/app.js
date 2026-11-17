import { APP_VERSION } from './version.js';
import { icon } from './icons.js';
import * as home from './pages/home.js';
import * as compare from './pages/compare.js';
import * as discount from './pages/discount.js';
import * as convert from './pages/convert.js';
import * as settings from './pages/settings.js';

// เส้นทาง → หน้า และแท็บที่เลือก
const ROUTES = {
  '/':         { page: home,     tab: 'calc' },
  '/compare':  { page: compare,  tab: 'calc' },
  '/discount': { page: discount, tab: 'calc' },
  '/convert':  { page: convert,  tab: 'calc' },
  '/settings': { page: settings, tab: 'settings' },
};

const app = document.getElementById('app');
app.innerHTML = `
  <main id="view"></main>
  <nav class="tabbar" aria-label="เมนูหลัก">
    <a class="tab" data-tab="calc" href="#/">${icon('calculator', 22)}<span>คำนวณ</span></a>
    <a class="tab" data-tab="settings" href="#/settings">${icon('sliders-horizontal', 22)}<span>ตั้งค่า</span></a>
  </nav>`;
const view = document.getElementById('view');

function route() {
  const path = location.hash.replace(/^#/, '') || '/';
  const r = ROUTES[path] || ROUTES['/'];
  document.body.classList.remove('kb-open');
  view.className = `page page-${path === '/' ? 'home' : path.slice(1)}`;
  r.page.render(view);
  for (const t of document.querySelectorAll('.tab')) {
    const on = t.dataset.tab === r.tab;
    t.classList.toggle('is-active', on);
    if (on) t.setAttribute('aria-current', 'page'); else t.removeAttribute('aria-current');
  }
  window.scrollTo(0, 0);
}
window.addEventListener('hashchange', route);
route();

// ซ่อนเมนูล่างเมื่อช่องกรอกโฟกัส (แป้นพิมพ์เปิด)
const isField = el => el && el.matches && el.matches('input, textarea');
document.addEventListener('focusin', e => { if (isField(e.target)) document.body.classList.add('kb-open'); });
document.addEventListener('focusout', () => {
  setTimeout(() => { if (!isField(document.activeElement)) document.body.classList.remove('kb-open'); }, 0);
});

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register(`./sw.js?v=${APP_VERSION}`).catch(() => {});
  });
}
