import calendar, os, sys
ROOT = sys.argv[1]
os.makedirs(os.path.join(ROOT, 'project'), exist_ok=True)

# ---------- icons (Lucide paths) ----------
IC = {
 'calc': '<rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/>',
 'cal': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
 'set': '<path d="M21 4h-7"/><path d="M10 4H3"/><path d="M21 12h-9"/><path d="M8 12H3"/><path d="M21 20h-5"/><path d="M12 20H3"/><path d="M14 2v4"/><path d="M8 10v4"/><path d="M16 18v4"/>',
 'left': '<path d="m15 18-6-6 6-6"/>', 'right': '<path d="m9 18 6-6-6-6"/>',
 'plus': '<path d="M5 12h14"/><path d="M12 5v14"/>', 'x': '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>', 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'repeat': '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
 'cloud': '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
 'chev': '<path d="m9 18 6-6-6-6"/>',
 'briefcase': '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
 'heart': '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
 'house': '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
 'plane': '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
 'activity': '<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>',
 'star': '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>',
 'cake': '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/>',
 'glasses': '<circle cx="6" cy="15" r="4"/><circle cx="18" cy="15" r="4"/><path d="M14 15a2 2 0 0 0-2-1 2 2 0 0 0-2 1"/><path d="M2.5 13 5 7c.7-1.3 1.4-2 3-2"/><path d="M21.5 13 19 7c-.7-1.3-1.5-2-3-2"/>',
}
def svg(name, size=22, color='currentColor', sw=1.5):
    return f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{IC[name]}</svg>'

COLORS = [  # fill, ink
    ('#DCE7FB', '#1F4E9C'), ('#ECE3FB', '#5B3C9E'), ('#FCE4D2', '#94460F'), ('#D8F0DF', '#1E6B3A'),
    ('#D3EDF0', '#1C5F68'), ('#FBE0EA', '#9C2C5A'), ('#F8EFC6', '#6E5200'), ('#E6E6E9', '#47474C'),
]
# user-made categories: key -> (name, color index, icon)
CATS = {
    'work': ('งาน', 0, 'briefcase'), 'home': ('บ้าน', 2, 'house'), 'health': ('สุขภาพ', 3, 'activity'),
    'trip': ('เที่ยว', 4, 'plane'), 'me': ('ส่วนตัว', 1, 'star'),
}
def cfill(k): return COLORS[CATS[k][1]][0]
def cink(k): return COLORS[CATS[k][1]][1]

# entries: start, end, title, cat, time, anniversary-label
ENTRIES = [
    ((1,1),(1,1),'ทำบุญปีใหม่','home',None,None),
    ((3,20),(3,22),'เที่ยวเขาใหญ่','trip',None,None),
    ((4,13),(4,15),'สงกรานต์กลับบ้าน','home',None,None),
    ((5,8),(5,8),'ตรวจสุขภาพประจำปี','health','09:00–11:00',None),
    ((7,18),(7,20),'สัมมนาภูเก็ต','work',None,None),
    ((8,12),(8,12),'วันแม่','home',None,None),
    ((10,10),(10,12),'ทริปเชียงราย','trip',None,None),
    ((11,3),(11,5),'สัมมนาเชียงใหม่','work',None,None),
    ((11,12),(11,12),'ตัดแว่น','health','14:00–15:00','ตัดแว่นครบ 1 ปี'),
    ((11,14),(11,14),'วันเกิดแม่','home',None,None),
    ((11,17),(11,17),'หาหมอฟัน','health','10:30–11:30',None),
    ((11,17),(11,17),'ประชุมทีม','work','14:00–15:30',None),
    ((11,17),(11,17),'จ่ายค่าบัตรเครดิต','me',None,None),
    ((11,17),(11,17),'เริ่มงานที่ใหม่ครบ 1 ปี','work',None,'anniv'),
    ((11,21),(11,23),'กลับบ้านต่างจังหวัด','home',None,None),
    ((11,27),(11,27),'ประชุมไตรมาส','work','13:00–15:00',None),
]
YEAR = 2026; BE = YEAR + 543
TH_MONTHS = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
TH_MON_S = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']
WD = ['จ','อ','พ','พฤ','ศ','ส','อา']
TODAY = (11, 17)
def entries_on(m, d): return [e for e in ENTRIES if e[0] <= (m, d) <= e[1]]

HEAD = '''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bai+Jamjuree:wght@400;500;600&family=Prompt:wght@300;400;500;600&display=swap">
<style>
body{{margin:0}}
button,input,textarea{{font:inherit;color:inherit}}
button{{cursor:pointer;appearance:none;border:0;margin:0;padding:0;background:none}}
input,textarea{{border:0;outline:0;background:transparent;padding:0;margin:0;min-width:0;width:100%;resize:none}}
input::placeholder,textarea::placeholder{{color:#A0A0A6}}
.surface{{background:linear-gradient(180deg,#F5F5F6 0%,#EDEDEE 100%);box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 1px 2px rgba(10,10,10,.04),0 10px 28px rgba(10,10,10,.05)}}
button:focus-visible{{outline:2px solid #0A0A0A;outline-offset:2px}}
</style>
</helmet>
<div style="position: relative; width: 390px; height: 844px; box-sizing: border-box; background: radial-gradient(120% 60% at 50% 0%, #FFFFFF 0%, #FAFAFA 70%); overflow: hidden; font-family: 'Bai Jamjuree', sans-serif; color: #0A0A0A">
'''
FOOT = '''</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":390,"height":844}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
'''
def write(name, title, body):
    with open(os.path.join(ROOT, 'project', name), 'w', encoding='utf-8') as f:
        f.write(HEAD.format(title=title) + body + FOOT)

# ---------- pieces ----------
def tabbar(active='notes'):
    tabs = [('notes','บันทึก','cal'),('calc','คำนวณ','calc'),('settings','ตั้งค่า','set')]
    out = ('<nav aria-label="เมนูหลัก" style="position: absolute; left: 0; right: 0; bottom: 0; height: 84px; box-sizing: border-box; padding: 6px 12px 28px; '
           'background: rgba(255,255,255,.94); border-top: 1px solid #ECECEE; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr))">\n')
    for k, label, ic in tabs:
        on = k == active; c = '#0A0A0A' if on else '#A0A0A6'
        cur = ' aria-current="page"' if on else ''
        out += (f'<button type="button"{cur} style="height: 50px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px">'
                f'{svg(ic, 24, c, 1.7 if on else 1.5)}<span style="font-weight: {600 if on else 500}; font-size: 11px; line-height: 1.2; color: {c}">{label}</span></button>\n')
    return out + '</nav>\n'

IC['pencil'] = '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/>'
IC['chart'] = '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>'
def title_row(mode='month'):
    return ('<div style="position: absolute; left: 24px; right: 20px; top: 72px; display: flex; align-items: center; justify-content: space-between">\n'
            '<h1 style="margin: 0; font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 40px; line-height: 1.25; letter-spacing: -0.5px">บันทึก</h1>\n'
            f'<button type="button" class="surface" style="height: 44px; padding: 0 16px 0 12px; border-radius: 22px; display: flex; align-items: center; gap: 6px; font-weight: 600; font-size: 15px">{svg("chart", 20)}สรุป</button>\n</div>\n')

def seg_row(mode, label='มุมมองปฏิทิน'):
    def seg(lbl, on):
        return (f'<button type="button" aria-pressed="{str(on).lower()}" style="flex: 1; height: 36px; border-radius: 18px; text-align: center; '
                f'background: {"#0A0A0A" if on else "transparent"}; font-weight: {600 if on else 500}; font-size: 15px; color: {"#FFFFFF" if on else "#68686D"}">{lbl}</button>')
    return (f'<div role="group" aria-label="{label}" style="height: 44px; box-sizing: border-box; padding: 4px; border-radius: 22px; background: #FFFFFF; box-shadow: 0 1px 2px rgba(10,10,10,.05); display: flex; gap: 2px; margin: 4px 0 2px">'
            f'{seg("เดือน", mode=="month")}{seg("ปี", mode=="year")}</div>\n')

def nav_btn(ic, label):
    return f'<button type="button" aria-label="{label}" style="width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center">{svg(ic, 20)}</button>'

def tag(k, selected=False, size='m'):
    name, ci, ic = CATS[k]; fill, ink = COLORS[ci]
    bg, fg = (ink, '#FFFFFF') if selected else (fill, ink)
    h, fs, isz = (36, 14, 16) if size == 'm' else (26, 12, 13)
    return (f'<span style="height: {h}px; padding: 0 {12 if size=="m" else 8}px 0 {10 if size=="m" else 7}px; border-radius: 10px; background: {bg}; color: {fg}; '
            f'display: inline-flex; align-items: center; gap: 6px; font-weight: 600; font-size: {fs}px; white-space: nowrap">{svg(ic, isz, fg, 1.8)}{name}</span>')

def month_card(month=11):
    weeks = calendar.Calendar(0).monthdatescalendar(YEAR, month)
    COL = 100 / 7
    out = ('<section class="surface" aria-label="ปฏิทินรายเดือน" style="position: absolute; left: 20px; right: 20px; top: 140px; box-sizing: border-box; border-radius: 28px; padding: 6px 10px 10px">\n'
           + seg_row('month') +
           f'<div style="height: 44px; display: flex; align-items: center; justify-content: space-between">{nav_btn("left","เดือนก่อน")}'
           f'<span style="font-family: \'Prompt\', sans-serif; font-weight: 500; font-size: 18px">{TH_MONTHS[month-1]} {BE}</span>{nav_btn("right","เดือนถัดไป")}</div>\n'
           '<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); height: 22px; align-items: center; text-align: center; font-size: 12px; font-weight: 500; color: #68686D">'
           + ''.join(f'<span>{w}</span>' for w in WD) + '</div>\n')
    for wk in weeks:
        out += '<div style="position: relative; height: 54px">\n'
        owner = {}
        for e in ENTRIES:
            for ci, dt in enumerate(wk):
                if dt.month == month and e[0] <= (dt.month, dt.day) <= e[1]:
                    owner.setdefault(ci, []).append(e)
        runs = []
        for ci in range(7):
            if ci in owner:
                e = owner[ci][0]
                if runs and runs[-1][2] is e and runs[-1][1] == ci - 1: runs[-1][1] = ci
                else: runs.append([ci, ci, e])
        for a, b, e in runs:
            first = (wk[a].month, wk[a].day) == e[0]; last = (wk[b].month, wk[b].day) == e[1]
            rl = 14 if first else 0; rr = 14 if last else 0
            out += (f'<div style="position: absolute; top: 2px; bottom: 2px; left: calc({a*COL}% + {2 if first else 0}px); '
                    f'width: calc({(b-a+1)*COL}% - {(2 if first else 0)+(2 if last else 0)}px); border-radius: {rl}px {rr}px {rr}px {rl}px; background: {cfill(e[3])}"></div>\n')
        # today: frame around the whole cell
        for ci, dt in enumerate(wk):
            if (dt.month, dt.day) == TODAY and dt.month == month:
                out += (f'<div aria-hidden="true" style="position: absolute; top: 2px; bottom: 2px; left: calc({ci*COL}% + 2px); width: calc({COL}% - 4px); '
                        'border-radius: 14px; box-shadow: inset 0 0 0 2px #0A0A0A"></div>\n')
        out += '<div style="position: absolute; inset: 0; display: grid; grid-template-columns: repeat(7, minmax(0, 1fr))">'
        for ci, dt in enumerate(wk):
            inm = dt.month == month
            es = owner.get(ci, [])
            col = '#C2C2C7' if not inm else (cink(es[0][3]) if es else '#0A0A0A')
            bold = 600 if (es or (dt.month, dt.day) == TODAY) else 400
            dots = ''.join(f'<span style="width: 5px; height: 5px; border-radius: 3px; background: {cink(x[3])}"></span>' for x in es[1:3])
            out += (f'<button type="button" aria-label="{dt.day} {TH_MONTHS[dt.month-1]}" style="height: 54px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px">'
                    f'<span style="font-size: 14px; font-weight: {bold}; color: {col}; line-height: 26px">{dt.day}</span>'
                    f'<span style="height: 5px; display: flex; gap: 3px">{dots}</span></button>')
        out += '</div>\n</div>\n'
    return out + '</section>\n'

def scrim(): return '<div style="position: absolute; inset: 0; background: rgba(10,10,10,.42)"></div>\n'
def sheet(title_id, inner, gap=14):
    return (f'<div role="dialog" aria-modal="true" aria-labelledby="{title_id}" style="position: absolute; left: 0; right: 0; bottom: 0; box-sizing: border-box; border-radius: 28px 28px 0 0; '
            f'background: #FAFAFA; padding: 10px 20px 34px; display: flex; flex-direction: column; gap: {gap}px; box-shadow: 0 -10px 40px rgba(10,10,10,.18)">\n'
            '<span style="align-self: center; width: 40px; height: 5px; border-radius: 3px; background: #D4D4D8"></span>\n' + inner + '</div>\n')
def sheet_head(tid, title, sub=None):
    s = f'<span style="font-weight: 500; font-size: 13px; color: #68686D">{sub}</span>' if sub else ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px"><div style="display: flex; flex-direction: column; gap: 2px">{s}'
            f'<h2 id="{tid}" style="margin: 0; font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 22px">{title}</h2></div>'
            f'<button type="button" aria-label="ปิด" class="surface" style="flex: none; width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center">{svg("x", 20)}</button></div>\n')
def label(t): return f'<span style="font-weight: 500; font-size: 13px; color: #68686D">{t}</span>'
def box(inner, h=52, extra=''):
    return f'<div style="height: {h}px; box-sizing: border-box; border-radius: 18px; background: #FFFFFF; padding: 0 16px; display: flex; align-items: center; gap: 8px; {extra}">{inner}</div>'
def fld(t, inner, h=52): return f'<div style="display: flex; flex-direction: column; gap: 6px; min-width: 0">{label(t)}{box(inner, h)}</div>'
def switch(on):
    return (f'<span role="switch" aria-checked="{str(on).lower()}" style="flex: none; width: 51px; height: 31px; border-radius: 16px; background: {"#0A0A0A" if on else "#E2E2E4"}; position: relative">'
            f'<span style="position: absolute; top: 2px; {"right" if on else "left"}: 2px; width: 27px; height: 27px; border-radius: 14px; background: #FFFFFF; box-shadow: 0 2px 4px rgba(10,10,10,.2)"></span></span>')
BLACK_BTN = 'height: 52px; border-radius: 26px; background: #0A0A0A; color: #FFFFFF; font-weight: 600; font-size: 16px; display: flex; align-items: center; justify-content: center; gap: 8px'

# ---------- 1. Month (opens here; nothing below the calendar yet) ----------
write('Notes-Month.dc.html', 'บันทึก — รายเดือน', title_row('month') + month_card() + tabbar())

# ---------- 2. Year ----------
def year_view():
    cal = calendar.Calendar(0)
    out = ('<section class="surface" aria-label="ปฏิทินรายปี" style="position: absolute; left: 20px; right: 20px; top: 140px; box-sizing: border-box; border-radius: 28px; padding: 6px 10px 10px">\n'
           + seg_row('year') +
           f'<div style="height: 44px; display: flex; align-items: center; justify-content: space-between">{nav_btn("left","ปีก่อน")}'
           f'<span style="font-family: \'Prompt\', sans-serif; font-weight: 500; font-size: 20px">พ.ศ. {BE}</span>{nav_btn("right","ปีถัดไป")}</div>\n'
           '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px 6px">\n')
    for m in range(1, 13):
        out += (f'<button type="button" aria-label="{TH_MONTHS[m-1]}" style="border-radius: 14px; padding: 6px 4px 4px; text-align: left; {"background: #FFFFFF;" if m == TODAY[0] else ""}">'
                f'<span style="display: block; padding-left: 4px; margin-bottom: 3px; font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 13px">{TH_MON_S[m-1]}</span>'
                '<span style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); row-gap: 1px">')
        for wk in cal.monthdatescalendar(YEAR, m):
            for dt in wk:
                if dt.month != m: out += '<span style="height: 14px"></span>'; continue
                es = entries_on(m, dt.day)
                st = 'color: #68686D'
                if es: st = f'background: {cfill(es[0][3])}; color: {cink(es[0][3])}; font-weight: 700'
                if (m, dt.day) == TODAY: st += '; box-shadow: inset 0 0 0 1.5px #0A0A0A; color: #0A0A0A; font-weight: 700'
                out += f'<span style="height: 14px; border-radius: 5px; font-size: 8.5px; line-height: 14px; text-align: center; {st}">{dt.day}</span>'
        out += '</span></button>\n'
    return out + '</div>\n</section>\n'
write('Notes-Year.dc.html', 'บันทึก — รายปี', title_row('year') + year_view() + tabbar())

# ---------- 3. Day popup (tap a day) ----------
rows = ''
for e in entries_on(11, 17):
    anniv = e[5] == 'anniv'
    meta = (f'<span style="display: inline-flex; align-items: center; gap: 4px">{svg("repeat", 14, "#68686D")}ครบรอบจาก 17 พ.ย. 2568</span>' if anniv else
            f'<span style="display: inline-flex; align-items: center; gap: 4px">{svg("clock", 14, "#68686D")}{e[4] or "ทั้งวัน"}</span>')
    rows += ('<button type="button" class="surface" style="border-radius: 20px; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; text-align: left">'
             f'<span style="display: flex; align-items: center; justify-content: space-between; gap: 10px; width: 100%"><span style="font-weight: 600; font-size: 16px">{e[2]}</span>{tag(e[3], size="s")}</span>'
             f'<span style="font-size: 13px; color: #68686D">{meta}</span></button>\n')
import datetime
def day_page():
    m, d = TODAY
    out = ('<header style="position: absolute; left: 20px; right: 20px; top: 56px; display: flex; align-items: center; gap: 14px">'
           f'<button type="button" class="surface" aria-label="ย้อนกลับ" style="flex: none; width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center">{svg("left", 22)}</button>'
           '<h1 style="flex: 1; margin: 0; font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 24px; line-height: 44px">พฤศจิกายน 2569</h1>'
           f'<button type="button" aria-label="เพิ่มบันทึก" style="flex: none; width: 44px; height: 44px; border-radius: 22px; background: #0A0A0A; display: flex; align-items: center; justify-content: center">{svg("plus", 22, "#FFFFFF", 2)}</button>'
           '</header>\n')
    t = datetime.date(YEAR, m, d); mon = t - datetime.timedelta(days=t.weekday())
    out += '<div role="group" aria-label="สัปดาห์" style="position: absolute; left: 16px; right: 16px; top: 114px; display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 4px">'
    for i in range(7):
        dt = mon + datetime.timedelta(days=i); on = dt == t
        has = bool(entries_on(dt.month, dt.day))
        dot = f'<span style="width: 5px; height: 5px; border-radius: 3px; background: {"#FFFFFF" if on else "#68686D"}; opacity: {1 if has else 0}"></span>'
        out += (f'<button type="button" aria-pressed="{str(on).lower()}" style="height: 66px; border-radius: 16px; background: {"#0A0A0A" if on else "transparent"}; color: {"#FFFFFF" if on else "#0A0A0A"}; '
                'display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px">'
                f'<span style="font-size: 12px; font-weight: 500; color: {"#FFFFFF" if on else "#68686D"}">{WD[i]}</span>'
                f'<span style="font-family: \'Prompt\', sans-serif; font-size: 18px; font-weight: {600 if on else 400}; line-height: 1.1">{dt.day}</span>{dot}</button>')
    out += '</div>\n'
    ents = entries_on(m, d)
    allday = [e for e in ents if not e[4]]
    timed = [e for e in ents if e[4]]
    out += ('<section aria-label="ทั้งวัน" style="position: absolute; left: 20px; right: 20px; top: 196px; display: flex; flex-direction: column; gap: 8px">'
            '<span style="padding-left: 4px; font-weight: 500; font-size: 13px; color: #68686D">ทั้งวัน · เหตุการณ์</span>')
    for e in allday:
        ann = e[5] == 'anniv'
        out += (f'<button type="button" style="min-height: 48px; border-radius: 16px; background: {cfill(e[3])}; padding: 0 12px 0 14px; display: flex; align-items: center; gap: 10px; text-align: left">'
                + (svg("repeat", 16, cink(e[3]), 1.8) if ann else '') +
                f'<span style="flex: 1; font-weight: 600; font-size: 15px; color: #0A0A0A; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{e[2]}</span>{tag(e[3], size="s")}</button>')
    out += '</section>\n'
    top0 = 196 + 26 + len(allday) * 56 + 26
    H = 60; start = 9
    out += f'<div aria-hidden="true" style="position: absolute; left: 20px; right: 20px; top: {top0 - 14}px; height: 1px; background: #E2E2E4"></div>\n'
    for i, h in enumerate(range(start, start + 9)):
        y = top0 + i * H
        out += (f'<span style="position: absolute; left: 20px; top: {y - 8}px; width: 44px; font-size: 12px; color: #68686D">{h:02d}:00</span>'
                f'<div aria-hidden="true" style="position: absolute; left: 68px; right: 20px; top: {y}px; height: 1px; background: #ECECEE"></div>\n')
    for e in timed:
        s, f = e[4].split('–')
        sh, sm = map(int, s.split(':')); fh, fm = map(int, f.split(':'))
        y = top0 + ((sh - start) * 60 + sm) * H / 60
        hgt = ((fh - sh) * 60 + (fm - sm)) * H / 60 - 4
        out += (f'<button type="button" style="position: absolute; left: 72px; right: 20px; top: {y + 2}px; height: {hgt}px; box-sizing: border-box; border-radius: 16px; background: {cfill(e[3])}; '
                'padding: 8px 12px 8px 14px; display: flex; align-items: flex-start; justify-content: space-between; gap: 8px; text-align: left">'
                f'<span style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="font-weight: 600; font-size: 15px; color: #0A0A0A">{e[2]}</span>'
                f'<span style="font-size: 13px; color: {cink(e[3])}">{s} – {f} น.</span></span>{tag(e[3], size="s")}</button>\n')
    return out
write('Notes-Day.dc.html', 'บันทึก — รายวัน', day_page() + tabbar())

# ---------- 4. Add entry ----------
tags = ''.join(tag(k, selected=(k=='health')) for k in CATS)
tags += (f'<span style="height: 36px; padding: 0 12px 0 10px; border-radius: 10px; box-shadow: inset 0 0 0 1.5px #C7C7CC; color: #68686D; display: inline-flex; align-items: center; gap: 6px; font-weight: 600; font-size: 14px">'
         f'{svg("plus", 16, "#68686D", 2)}หมวดใหม่</span>')
add = sheet('add-title',
    sheet_head('add-title', 'เพิ่มบันทึก', 'วันพุธ 12 พ.ย. 2569') +
    fld('เรื่อง', '<input type="text" value="ตัดแว่น" style="font-size: 18px">') + '\n' +
    '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px">' +
      fld('วันเริ่ม', '<span style="font-size: 16px; font-weight: 500">พ. 12 พ.ย. 2569</span>') +
      fld('วันถึง', '<span style="font-size: 16px; font-weight: 500">พ. 12 พ.ย. 2569</span>') + '</div>\n' +
    '<div style="display: flex; flex-direction: column; gap: 6px">'
      f'<div style="display: flex; align-items: center; justify-content: space-between">{label("กำหนดเวลา (ปิด = ทั้งวัน / เหตุการณ์)")}{switch(True)}</div>'
      '<div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 8px; align-items: center">'
      + box(f'{svg("clock", 18, "#68686D")}<span style="font-size: 16px; font-weight: 500">14:00</span>') +
      '<span style="color: #68686D">–</span>'
      + box(f'{svg("clock", 18, "#68686D")}<span style="font-size: 16px; font-weight: 500">15:00</span>') + '</div></div>\n' +
    f'<div style="display: flex; flex-direction: column; gap: 6px"><div style="display: flex; align-items: center; justify-content: space-between; height: 24px">{label("หมวด")}'
    f'<button type="button" style="height: 44px; margin: -10px 0; padding: 0 2px 0 12px; display: flex; align-items: center; gap: 4px; font-weight: 500; font-size: 13px; color: #0A0A0A">{svg("pencil", 13)}แก้ไขหมวด</button></div>'
    f'<div style="display: flex; flex-wrap: wrap; gap: 8px">{tags}</div></div>\n' +
    '<div style="border-radius: 20px; background: #FFFFFF; padding: 12px 12px 12px 16px; display: flex; flex-direction: column; gap: 10px">'
      f'<div style="display: flex; align-items: center; gap: 10px">{svg("repeat", 20, "#0A0A0A")}<span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 600; font-size: 15px">ครบรอบปีหน้า</span>'
      '<span style="font-size: 13px; color: #68686D">ขึ้นในปฏิทินวันที่ 12 พ.ย. 2570</span></span>' + switch(True) + '</div>'
      '<div style="height: 44px; border-radius: 14px; background: #F0F0F1; padding: 0 14px; display: flex; align-items: center"><input type="text" aria-label="ชื่อที่จะขึ้นวันครบรอบ" value="ตัดแว่นครบ 1 ปี" style="font-size: 16px; font-weight: 500"></div>'
    '</div>\n' +
    f'<button type="button" style="{BLACK_BTN}">บันทึก</button>\n', 12)
write('Notes-Add.dc.html', 'บันทึก — เพิ่มบันทึก', title_row('month') + month_card() + scrim() + add)

# ---------- 5. New category ----------
swatches = ''.join(
    f'<button type="button" aria-label="สี {i+1}" aria-pressed="{str(i==6).lower()}" style="width: 36px; height: 36px; border-radius: 18px; background: {f}; '
    f'box-shadow: inset 0 0 0 2px {k if i==6 else "transparent"}{", 0 0 0 3px #FAFAFA, 0 0 0 5px " + k if i==6 else ""}; display: flex; align-items: center; justify-content: center">'
    f'{svg("check", 16, k, 2.4) if i==6 else ""}</button>' for i, (f, k) in enumerate(COLORS))
icons = ''.join(
    f'<button type="button" aria-label="{n}" aria-pressed="{str(n=="glasses").lower()}" style="height: 48px; border-radius: 14px; '
    f'background: {"#0A0A0A" if n=="glasses" else "#FFFFFF"}; display: flex; align-items: center; justify-content: center">{svg(n, 22, "#FFFFFF" if n=="glasses" else "#0A0A0A")}</button>'
    for n in ['briefcase','house','heart','activity','plane','star','cake','glasses'])
CATS['eyes'] = ('ดวงตา', 6, 'glasses')
cat = sheet('cat-title',
    sheet_head('cat-title', 'หมวดใหม่') +
    f'<div style="display: flex; justify-content: center; padding: 4px 0">{tag("eyes")}</div>\n' +
    fld('ชื่อหมวด', '<input type="text" value="ดวงตา" style="font-size: 18px">') + '\n' +
    f'<div style="display: flex; flex-direction: column; gap: 8px">{label("สี")}<div style="display: flex; justify-content: space-between; padding: 0 4px">{swatches}</div></div>\n' +
    f'<div style="display: flex; flex-direction: column; gap: 8px">{label("ไอคอน")}<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px">{icons}</div></div>\n' +
    f'<button type="button" style="{BLACK_BTN}">สร้างหมวด</button>\n', 14)
write('Notes-Category.dc.html', 'บันทึก — หมวดใหม่', title_row('month') + month_card() + scrim() + cat)
del CATS['eyes']

# ---------- 7. Summary ----------
def summary(mode='month'):
    if mode == 'month':
        es = [e for e in ENTRIES if e[0][0] == 11 or e[1][0] == 11]; period = f'{TH_MONTHS[10]} {BE}'
    else:
        es = list(ENTRIES); period = f'พ.ศ. {BE}'
    counts = {}
    for e in es: counts.setdefault(e[3], []).append(e)
    total = len(es); mx = max(len(v) for v in counts.values())
    def seg(lbl, on):
        return (f'<button type="button" aria-pressed="{str(on).lower()}" style="flex: 1; height: 36px; border-radius: 18px; text-align: center; '
                f'background: {"#0A0A0A" if on else "transparent"}; font-weight: {600 if on else 500}; font-size: 15px; color: {"#FFFFFF" if on else "#68686D"}">{lbl}</button>')
    out = ('<header style="position: absolute; left: 20px; right: 20px; top: 56px; display: flex; align-items: center; gap: 14px">'
           f'<button type="button" class="surface" aria-label="ย้อนกลับ" style="flex: none; width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center">{svg("left", 22)}</button>'
           '<h1 style="margin: 0; font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 30px; line-height: 44px; letter-spacing: -0.3px">สรุป</h1></header>\n'
           '<main style="position: absolute; left: 20px; right: 20px; top: 116px; display: flex; flex-direction: column; gap: 10px">\n'
           '<div role="group" aria-label="ช่วงสรุป" style="height: 44px; box-sizing: border-box; padding: 4px; border-radius: 22px; background: #F0F0F1; box-shadow: inset 0 1px 0 rgba(255,255,255,.9); display: flex; gap: 2px">'
           f'{seg("รายเดือน", mode=="month")}{seg("รายปี", mode=="year")}</div>\n'
           f'<div style="height: 44px; display: flex; align-items: center; justify-content: space-between">{nav_btn("left","ก่อนหน้า")}'
           f'<span style="font-family: \'Prompt\', sans-serif; font-weight: 500; font-size: 18px">{period}</span>{nav_btn("right","ถัดไป")}</div>\n'
           '<section style="height: 104px; box-sizing: border-box; border-radius: 22px; background: #0A0A0A; color: #FFFFFF; padding: 14px 18px; display: flex; flex-direction: column; justify-content: center; gap: 4px">'
           '<div style="display: flex; align-items: baseline; gap: 8px"><span style="font-size: 15px; color: #B4B4B9">ทั้งหมด</span>'
           f'<span style="font-family: \'Prompt\', sans-serif; font-weight: 300; font-size: 48px; line-height: 1.1; letter-spacing: -1px">{total}</span><span style="font-size: 16px; color: #B4B4B9">เรื่อง</span></div>'
           f'<span style="font-size: 14px; color: #B4B4B9">ใน {len(counts)} หมวด</span></section>\n')
    for k, v in sorted(counts.items(), key=lambda x: -len(x[1])):
        titles = ' · '.join(e[2] for e in v[:3]) + (f' และอีก {len(v)-3}' if len(v) > 3 else '')
        out += ('<button type="button" class="surface" style="border-radius: 20px; padding: 12px 16px; display: flex; flex-direction: column; gap: 8px; text-align: left">'
                f'<span style="display: flex; align-items: center; justify-content: space-between; width: 100%">{tag(k, size="s")}'
                f'<span style="display: flex; align-items: baseline; gap: 4px"><span style="font-family: \'Prompt\', sans-serif; font-weight: 500; font-size: 22px">{len(v)}</span><span style="font-size: 13px; color: #68686D">ครั้ง</span></span></span>'
                f'<span style="height: 6px; border-radius: 3px; background: #E2E2E4; width: 100%; display: block"><span style="display: block; height: 6px; border-radius: 3px; width: {len(v)/mx*100:.0f}%; background: {cink(k)}"></span></span>'
                f'<span style="font-size: 13px; color: #68686D; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%">{titles}</span></button>\n')
    return out + '</main>\n'
write('Notes-Summary.dc.html', 'บันทึก — สรุปรายเดือน', summary('month') + tabbar())
write('Notes-Summary-Year.dc.html', 'บันทึก — สรุปรายปี', summary('year') + tabbar())

# ---------- 6. Settings: sync + categories ----------
cat_tags = ''.join(tag(k) for k in CATS) + (f'<span style="height: 36px; padding: 0 12px 0 10px; border-radius: 10px; box-shadow: inset 0 0 0 1.5px #C7C7CC; color: #68686D; '
            f'display: inline-flex; align-items: center; gap: 6px; font-weight: 600; font-size: 14px">{svg("plus", 16, "#68686D", 2)}เพิ่มหมวด</span>')
settings = (
    '<h1 style="position: absolute; left: 24px; top: 72px; margin: 0; font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 40px; line-height: 1.25; letter-spacing: -0.5px">ตั้งค่า</h1>\n'
    '<main style="position: absolute; left: 20px; right: 20px; top: 146px; display: flex; flex-direction: column; gap: 10px">\n'
    '<section class="surface" style="border-radius: 24px; padding: 16px 16px 14px 18px; display: flex; flex-direction: column; gap: 12px">'
      f'<div style="display: flex; align-items: center; gap: 10px">{svg("cloud", 22, "#0A0A0A")}<span style="display: flex; flex-direction: column; gap: 2px">'
      '<span style="font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 18px">ซิงก์ข้อมูล</span>'
      '<span style="font-size: 13px; color: #68686D; line-height: 1.4">เข้าสู่ระบบเพื่อเก็บบันทึกไว้ออนไลน์ ใช้ได้หลายเครื่อง</span></span></div>'
      + box('<input type="email" placeholder="อีเมล" style="font-size: 16px">') +
      f'<button type="button" style="height: 48px; border-radius: 24px; background: #0A0A0A; color: #FFFFFF; font-weight: 600; font-size: 15px">ส่งลิงก์เข้าสู่ระบบ</button>'
    '</section>\n'
    '<section class="surface" style="border-radius: 24px; padding: 12px 12px 12px 18px; display: flex; align-items: center; justify-content: space-between; gap: 12px">'
      '<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500; font-size: 13px; color: #68686D">เกี่ยวกับแอป</span>'
      '<span style="font-family: \'Prompt\', sans-serif; font-weight: 600; font-size: 24px; line-height: 1.2">random</span></div>'
      '<button type="button" style="height: 44px; padding: 0 18px; border-radius: 22px; background: #FFFFFF; box-shadow: 0 1px 3px rgba(10,10,10,.08); font-weight: 500; font-size: 14px">เวอร์ชัน 1.1</button>'
    '</section>\n</main>\n')
write('Settings-Sync.dc.html', 'ตั้งค่า — ซิงก์และหมวด', settings + tabbar('settings'))
print('ok')
