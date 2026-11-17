# random · ส่งต่องาน

> อัปเดต 17 พฤศจิกายน 2569 · v1.0 ทำครบ 8 ขั้นตาม BUILD_BRIEF.md แล้ว และเจ้าของทดสอบบน iPhone ผ่านแล้ว
> เว็บ: https://milkcakelychee-hue.github.io/random/ · repo: https://github.com/milkcakelychee-hue/random (branch `main`, Pages ใช้ main / root)

## อ่านตามลำดับนี้
1. **HANDOFF.md** (ไฟล์นี้) · สถานะล่าสุด และสิ่งที่ต่างจากเอกสาร (ชนะเอกสารอื่น)
2. **APP_SPEC.md** · พฤติกรรมและคำบนหน้าจอ (หัวข้อ 6 ต้องตรงทุกตัวอักษร)
3. **BUILD_BRIEF.md** · โครงไฟล์ ค่าดีไซน์ ลำดับงาน เช็กลิสต์ iPhone
4. **design/*.dc.html** · หน้าจอที่อนุมัติแล้ว 19 ภาพ (ต้นฉบับ: https://claude.ai/code/artifact/80c41324-46ea-4285-81d2-3f336ea9fcb9) ถ้าตัวเลขในเอกสารไม่ตรงกับภาพ ให้ยึดภาพ แล้วแจ้งเจ้าของ

## ตั้งค่าเครื่องใหม่ (ทำครั้งเดียว)
```bash
git clone https://github.com/milkcakelychee-hue/random.git
cd random
git config core.hooksPath .githooks
git config user.name "milkcakelychee-hue"
git config user.email "milkcakelychee-hue@users.noreply.github.com"
```
- ต้องตั้ง `core.hooksPath` ทุกเครื่อง: hook `pre-commit` จะเขียนเวลา build ลงใน `const BUILD` ของ `sw.js` ทุกครั้งที่ commit ถ้าไม่ตั้ง แอปที่ติดตั้งไว้จะไม่รู้ว่ามีของใหม่
- ดูผลในเครื่อง: `python -m http.server 5173` แล้วเปิด http://127.0.0.1:5173 ที่ขนาด 390×844
- ทดสอบสูตร: `node tests/calc.test.mjs` ต้องขึ้น "ผ่านทุกข้อ"

## โครงไฟล์จริง (ต่างจาก BUILD_BRIEF เล็กน้อย)
```
index.html · manifest.webmanifest · sw.js · icons/ (ลูกเต๋า 180/192/512)
css/style.css          ตัวแปรดีไซน์ใน :root ด้านบน แล้วแบ่งส่วนตามหน้า
js/app.js              router แบบ hash + เมนูล่าง + ซ่อนเมนูตอนแป้นพิมพ์เปิด + ล็อกซูม + อัปเดตตัวเอง
js/version.js          APP_VERSION + WHATS_NEW (เลขเดียวใช้ทั้งแอปและแคช)
js/storage.js          localStorage ที่เดียว (คีย์ random:prefs)
js/units.js · js/format.js
js/calc.js             สูตร compare() และ discount() (แยกจากหน้าจอเพื่อทดสอบได้ · BUILD_BRIEF วางไว้ใน compare.js/discount.js)
js/icons.js            ไอคอนเส้นแบบ Lucide ที่เขียนฝังเอง
js/pages/              home · toolhead (แถวหัวข้อ+ย้อนกลับ) · compare · discount · convert · settings
tests/calc.test.mjs    ตัวอย่างทดสอบจาก "กติกาเป็นโค้ด" + เพิ่มเติม 33 ข้อ
.githooks/pre-commit   เขียนเวลา build ลง sw.js
design/                หน้าจอจาก Claude Design (อ้างอิง ไม่โหลดในแอป)
```

## สิ่งที่ตัดสินใจแล้ว (ต่างจาก/เพิ่มจากเอกสาร · อย่าย้อนกลับ)
- **ไม่มีกรอบดำตอนโฟกัส** ทั้งช่องกรอกและปุ่มเลือกหน่วยทุกหน้า (เจ้าของสั่ง · BUILD_BRIEF ให้มีกรอบ 2px) ส่วน `:focus-visible` ของปุ่มตอนใช้คีย์บอร์ดยังมีอยู่
- **ปุ่มนำทางเป็น `<button data-href>` ไม่ใช่ `<a>`** เพื่อกันหน้าต่าง peek ตอนกดค้างบน iPhone และมี touchstart listener เปล่าไว้ให้ `:active` ทำงานบน iOS
- **ล็อกซูม:** viewport `maximum-scale=1, user-scalable=no` + CSS `touch-action: pan-y` + กันท่า `gesturestart` ให้เลื่อนได้แค่ขึ้นลง
- **พื้นหลัง:** แสงขาวจากด้านบนเป็นชั้น `body::before` แบบ fixed และตั้ง `overscroll-behavior-y: none` เพื่อไม่ให้เห็นขอบด้านบนตอนดึงลง · theme-color #FFFFFF
- **อัปเดตตัวเอง:** เช็ก `reg.update()` ทุกครั้งที่แอปกลับมาอยู่บนจอ (visibilitychange, focus, online) ถ้ามี service worker ใหม่เข้าคุม (controllerchange) ให้รีโหลดเอง ตอน install โหลดไฟล์ด้วย `cache: 'reload'`
- **ฟอนต์ออฟไลน์:** service worker เก็บไฟล์ CSS และไฟล์ฟอนต์ของ Google Fonts ไว้ตั้งแต่ตอนติดตั้ง
- **ระยะขอบบน:** ใช้ `max(ค่าดีไซน์, env(safe-area-inset-top) + ส่วนเผื่อ)` ดู `--top-title` และ `--top-tool`
- **หัวข้อหน้าแรกและหน้าตั้งค่า** ห่างขอบซ้าย 24px ตามภาพ (เอกสารบอก 20)
- **ไอคอนลบ** ใช้ถังเปล่าตามภาพ (`trash`) ไม่ใช่ `trash-2`
- **แปลงหน่วย:** แตะแถวผลลัพธ์แล้วตั้งเป็นหน่วยต้นทาง และเปลี่ยนช่อง "ค่า" เป็นค่าของแถวนั้น (ผลทุกแถวคงเดิม) · เมื่อสลับหมวด ถ้าหน่วยเดิมไม่อยู่ในหมวดใหม่ ใช้ กก. / ลิตร / ม. ตามดีไซน์ · ตัวเลขยาวเกิน 9 ตัวอักษรลดเป็น 26px
- **ส่วนลด:** ช่อง % ที่เกิน 100 ปรับเป็น 100 ตอนออกจากช่องหรือตอนสลับกลับมาเป็น % · "ล้างทั้งหมด" รีเซ็ตเหลือ 1 รายการว่างแบบ %
- **เทียบราคา:** "ล้างทั้งหมด" ล้างแค่ตัวเลข หน่วยยังอยู่ · หัวข้อ "คุ้มกว่า" อยู่บรรทัดเดียวเสมอ ราคาต่อหน่วยที่ยาวตัดด้วย …
- **Git:** push ขึ้น `main` ได้หลังจบแต่ละงาน (เจ้าของอนุญาต) commit ใช้ชื่อและอีเมล noreply ด้านบน

## กติกาเวลาแก้ต่อ
- เพิ่มไฟล์ใหม่ต้องใส่ชื่อไฟล์ใน `APP_FILES` ของ `sw.js` ด้วย
- ออกฟีเจอร์หลักใหม่ให้แก้ `APP_VERSION` และ `WHATS_NEW` ใน `js/version.js` ส่วนการแก้เล็กน้อยไม่ต้องแก้เลขเวอร์ชัน
- ห้ามเพิ่มฟีเจอร์หรือหน้านอก APP_SPEC.md ถ้าคิดว่าควรมีให้ถามก่อน (ดูหัวข้อ 2 "สิ่งที่ไม่มี" และหัวข้อ 10)
- คำบนหน้าจอใช้ตาม APP_SPEC.md หัวข้อ 6 ทุกตัวอักษร
- หลังแก้: รันเทสต์สูตร แล้วดูในเบราว์เซอร์ที่ 390×844 แล้วสรุปให้เจ้าของพร้อมวิธีทดสอบบน iPhone แล้วรอเจ้าของตรวจ
- ทดสอบในเครื่อง: เบราว์เซอร์อาจใช้ไฟล์เก่าจากแคช HTTP ของ `python http.server` ให้ `fetch(url, {cache:'reload'})` หรือเปลี่ยน origin (localhost ↔ 127.0.0.1) ถ้าเห็นของเก่า

## ไอเดียที่ยังไม่ได้ตกลง (ห้ามทำเองโดยไม่ถาม)
จาก APP_SPEC.md หัวข้อ 10: ช่อง "จำนวนแพ็ก" ในเทียบราคา · หมวดอุณหภูมิ · เทียบมากกว่า 2 ตัวเลือก · หมวด "ชีวิต" · คืนปุ่มล้างค่าที่จำไว้หรือหน้าสอนติดตั้ง

---

## Prompt สำหรับวางในเครื่องใหม่ (Claude Code)

```
ฉันกำลังทำ PWA ชื่อ "random" สำหรับ iPhone (เทียบราคา A/B · ส่วนลด · แปลงหน่วย)
v1.0 เสร็จและขึ้นเว็บแล้วที่ https://milkcakelychee-hue.github.io/random/
repo: https://github.com/milkcakelychee-hue/random

1. ถ้ายังไม่มีโค้ดในเครื่อง ให้ clone repo แล้วทำตามหัวข้อ "ตั้งค่าเครื่องใหม่" ใน HANDOFF.md
   (ต้องตั้ง git config core.hooksPath .githooks)
2. อ่าน HANDOFF.md ให้จบก่อน แล้วอ่าน APP_SPEC.md, BUILD_BRIEF.md และดู design/
   HANDOFF.md ชนะเอกสารอื่นในข้อที่ระบุว่าตัดสินใจแล้ว
3. รัน node tests/calc.test.mjs ให้ผ่าน แล้วสรุปสั้น ๆ ว่าเข้าใจสถานะแอปอย่างไร ยังไม่ต้องแก้อะไร
4. รองานจากฉัน ทุกงานให้ทำทีละขั้น จบแล้วสรุปสิ่งที่ทำและวิธีทดสอบบน iPhone แล้วหยุดรอฉันตรวจ
5. คำบนหน้าจอใช้ตาม APP_SPEC.md หัวข้อ 6 ทุกตัวอักษร ห้ามเพิ่มฟีเจอร์หรือหน้านอกสเปกโดยไม่ถาม
6. push ขึ้น main ได้หลังจบแต่ละงาน
```
