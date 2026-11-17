// เลขเวอร์ชันแคชมาจาก APP_VERSION ใน js/version.js (app.js register เป็น sw.js?v=<APP_VERSION>)
const VERSION = new URL(self.location).searchParams.get('v') || 'dev';
const APP_CACHE = `random-app-${VERSION}`;
const FONT_CACHE = 'random-fonts';

// ไฟล์แอปทั้งหมด (เพิ่มรายการเมื่อสร้างไฟล์ใหม่ในขั้นถัดไป)
const APP_FILES = [
  './',
  './index.html',
  './manifest.webmanifest',
  './css/style.css',
  './js/app.js',
  './js/version.js',
  './js/storage.js',
  './js/units.js',
  './js/format.js',
  './js/calc.js',
  './js/icons.js',
  './js/pages/home.js',
  './js/pages/toolhead.js',
  './js/pages/compare.js',
  './js/pages/discount.js',
  './js/pages/convert.js',
  './js/pages/settings.js',
  './icons/icon-180.png',
  './icons/icon-192.png',
  './icons/icon-512.png',
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(APP_CACHE).then(c => c.addAll(APP_FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('random-app-') && k !== APP_CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Google Fonts: ใช้ของในแคชก่อน ไม่มีค่อยโหลดแล้วเก็บไว้ (ใช้ออฟไลน์ได้)
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    e.respondWith(
      caches.open(FONT_CACHE).then(async c => {
        const hit = await c.match(req);
        if (hit) return hit;
        const res = await fetch(req);
        if (res.ok || res.type === 'opaque') c.put(req, res.clone());
        return res;
      })
    );
    return;
  }

  if (url.origin !== self.location.origin) return;

  // ไฟล์แอป: แคชก่อน · หน้า HTML ตกกลับไปที่ index.html เมื่อออฟไลน์
  e.respondWith(
    caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req).catch(() =>
      req.mode === 'navigate' ? caches.match('./index.html') : Response.error()
    ))
  );
});
