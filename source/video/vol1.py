"""第一卷 01、02、03、05 的原理动画。"""
import math, random, sys
from lib import *
import titles

# ======================= E01 摩擦起电 =======================
random.seed(11)
def e01_transfer(c, t, i):
    corner_tag(c, '第 01 集 · 摩擦起电')
    c.text(60, 96, '一擦，电子就被「抢」走了', 'serif', 40, INK)
    # positions: wool slides toward centre and rubs, then separates
    if t < 3: gap = 1 - ease(t / 3) * 0.0
    approach = ease((t - 1) / 2.5) * (1 - ease((t - 10) / 2.5))
    rub = math.sin(t * 9) * 26 if 3.6 < t < 9.6 else 0
    wx = 520 + approach * 330
    ax = 1400 - approach * 330
    wy = 420 + rub
    # blocks
    c.rect(wx - 200, wy - 150, wx + 120, wy + 150, fill=mix(BG, (170, 150, 120), 0.45), r=18)
    c.rect(ax - 120, 270, ax + 200, 570, fill=mix(BG, (210, 150, 50), 0.55), r=18)
    c.text(wx - 40, wy - 190, '毛皮', 'bold', 32, INK, 'mm')
    c.text(ax + 40, 230, '琥珀', 'bold', 32, INK, 'mm')
    # charges: each block has 10 + fixed, 10 electrons; 5 electrons move during rubbing
    moved = min(5, max(0, int((t - 4) / 1.0))) if t > 4 else 0
    for k in range(10):
        gx, gy = k % 5, k // 5
        c.text(wx - 160 + gx * 56, wy - 70 + gy * 120, '+', 'bold', 32, mix(BG, NRED, 0.8), 'mm')
        c.text(ax - 80 + gx * 56, 350 + gy * 120, '+', 'bold', 32, mix(BG, NRED, 0.8), 'mm')
    # electrons
    for k in range(10):
        gx, gy = k % 5, k // 5
        px, py = wx - 160 + gx * 56 + 22, wy - 40 + gy * 120
        if k >= 5 and k - 5 < moved:
            # moved electrons: transition
            tk = 4 + (k - 5) * 1.0
            s = ease((t - tk) / 0.8)
            tx, ty = ax - 80 + (k - 5) * 56 + 22, 440
            px, py = px + (tx - px) * s, py + (ty - py) * s - math.sin(s * math.pi) * 60
        c.ellipse(px, py, 11, 11, fill=FIELD)
    for k in range(10):
        gx, gy = k % 5, k // 5
        c.ellipse(ax - 80 + gx * 56 + 22, 380 + gy * 120, 11, 11, fill=FIELD)
    # net charge labels
    if t > 9.6:
        a = fade(t, 9.6, 10.4)
        c.text(wx - 40, wy + 200, '少了 5 个电子：带正电', 'bold', 30, mix(BG, NRED, a), 'mm')
        c.text(ax + 40, 620, '多了 5 个电子：带负电', 'bold', 30, mix(BG, FIELD, a), 'mm')
    # paper bits attracted
    if t > 13:
        for k in range(7):
            bx = ax - 100 + k * 46
            s = ease((t - 13.5 - k * 0.15) / 1.2)
            by = 900 - s * (900 - 600)
            c.rect(bx - 10, by - 6, bx + 10, by + 6, fill=mix(BG, INK, 0.85), r=2)
        c.text(ax + 40, 960, '纸屑被吸起', 'sans', 26, MUTED, 'mm')
    # legend
    c.rect(60, 760, 520, 880, fill=SHEET, r=12)
    c.ellipse(96, 795, 10, 10, fill=FIELD); c.text(120, 795, '电子（带负电，能移动）', 'sans', 24, INK, 'lm')
    c.text(96, 845, '+', 'bold', 30, NRED, 'mm'); c.text(120, 845, '原子核里的正电（不动）', 'sans', 24, INK, 'lm')
    caps = [(0, 3.6, '一开始：两块材料里的正电和负电一样多，都不带电'),
            (3.8, 9.6, '接触、摩擦：琥珀抓电子的本领更强，抢走了一些电子'),
            (9.8, 13.2, '分开以后：一个带正电，一个带负电'),
            (13.4, 20, '带电的琥珀能隔空吸起纸屑')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(1100, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

def e01_leyden(c, t, i):
    corner_tag(c, '第 01 集 · 莱顿瓶')
    c.text(60, 96, '把电「锁」在瓶子里', 'serif', 40, INK)
    jx, jy0, jy1, jw = 860, 330, 880, 300
    # glass
    c.rect(jx - jw / 2 - 14, jy0, jx + jw / 2 + 14, jy1, outline=mix(BG, FIELD, 0.6), width=6, r=26)
    # outer foil
    c.rect(jx - jw / 2 - 26, jy0 + 160, jx - jw / 2 - 14, jy1 - 10, fill=COPPER)
    c.rect(jx + jw / 2 + 14, jy0 + 160, jx + jw / 2 + 26, jy1 - 10, fill=COPPER)
    # inner foil
    c.rect(jx - jw / 2 + 4, jy0 + 160, jx - jw / 2 + 16, jy1 - 22, fill=COPPER)
    c.rect(jx + jw / 2 - 16, jy0 + 160, jx + jw / 2 - 4, jy1 - 22, fill=COPPER)
    # rod + knob + chain
    c.line([(jx, 210), (jx, jy1 - 40)], MUTED, 6)
    c.ellipse(jx, 200, 30, 30, fill=MUTED)
    c.text(jx + 60, 200, '金属球', 'sans', 24, MUTED, 'lm')
    c.rect(1380, 600, 1840, 800, fill=SHEET, r=12)
    c.rect(1410, 630, 1420, 660, fill=COPPER); c.text(1440, 645, '里层金属箔：存进负电（−）', 'sans', 24, INK, 'lm')
    c.rect(1410, 690, 1420, 720, fill=COPPER); c.text(1440, 705, '外层金属箔：吸来正电（+）', 'sans', 24, INK, 'lm')
    c.rect(1405, 750, 1425, 780, outline=mix(BG, FIELD, 0.6), width=4, r=4); c.text(1440, 765, '中间的玻璃：绝缘，电过不去', 'sans', 24, INK, 'lm')
    # charge level
    if t < 13: q = min(8, int(max(0, t - 1.5) / 1.3))
    elif t < 15.5: q = 8
    else: q = 0
    # charging rod touches knob
    if 1.5 < t < 12:
        ph = ((t - 1.5) % 1.3) / 1.3
        rx = jx + 220 - 170 * math.sin(ph * math.pi)
        c.rect(rx - 10, 120, rx + 140, 150, fill=mix(BG, (210, 150, 50), 0.6), r=8)
        c.text(rx + 65, 100, '带负电的琥珀', 'sans', 22, MUTED, 'mm')
    for k in range(q):
        y = jy0 + 190 + k * 58
        c.text(jx - jw / 2 + 40, y, '−', 'bold', 34, FIELD, 'mm')
        c.text(jx + jw / 2 - 40, y, '−', 'bold', 34, FIELD, 'mm')
        c.text(jx - jw / 2 - 46, y, '+', 'bold', 34, NRED, 'mm')
        c.text(jx + jw / 2 + 46, y, '+', 'bold', 34, NRED, 'mm')
    # discharge
    if 13.2 < t < 15.5:
        a = fade(t, 13.2, 13.6)
        c.line([(jx + 30, 200), (jx + 260, 200), (jx + 260, jy0 + 300), (jx + jw / 2 + 30, jy0 + 300)], mix(BG, MUTED, a), 6)
        if 14 < t < 14.6:
            pts = [(jx + 30, 200)]
            random.seed(int(t * 30))
            for k in range(6):
                pts.append((jx + 30 - 10 * k + random.uniform(-14, 14), 200 - 20 - 10 * k))
            c.line([(jx + 30, 196), (jx + 52, 170), (jx + 44, 150), (jx + 66, 128)], SPARK, 6)
            c.text(jx + 120, 120, '啪！', 'serif', 56, SPARK, 'mm')
    # meter
    c.rect(1400, 400, 1820, 520, fill=SHEET, r=12)
    c.text(1430, 435, '瓶里存的电', 'sans', 26, MUTED, 'lm')
    c.rect(1430, 470, 1790, 490, fill=LINE, r=10)
    c.rect(1430, 470, 1430 + 360 * q / 8, 490, fill=COPPER, r=10)
    caps = [(0, 1.6, '莱顿瓶：玻璃瓶内外各贴一层金属箔'),
            (1.8, 7, '每碰一次金属球，内层就多存一些负电'),
            (7.2, 13, '外层被吸来等量的正电，正负电隔着玻璃互相拉住，跑不掉'),
            (13.2, 16, '用导线把内外连起来：一下子全放掉'),
            (16.2, 22, '电存得住，但只能一次用完')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

# ======================= E02 伏打电堆 =======================
def e02_micro(c, t, i):
    corner_tag(c, '第 02 集 · 电堆里发生了什么')
    c.text(60, 96, '铁把电子「交」给了铜', 'serif', 40, INK)
    fx0, fx1, cx0, cx1, y0, y1 = 360, 460, 1460, 1560, 360, 880
    # brine
    c.rect(fx1, y0 + 40, cx0, y1, fill=mix(BG, FIELD, 0.12), r=0)
    c.text((fx1 + cx0) / 2, y1 + 40, '浸了盐水的布', 'sans', 26, MUTED, 'mm')
    # plates
    c.rect(fx0, y0, fx1, y1, fill=mix(BG, MUTED, 0.55), r=6)
    c.rect(cx0, y0, cx1, y1, fill=COPPER, r=6)
    c.text((fx0 + fx1) / 2, y0 - 30, '铁', 'bold', 34, INK, 'mm')
    c.text((cx0 + cx1) / 2, y0 - 30, '铜', 'bold', 34, INK, 'mm')
    # wire with meter
    c.line([((fx0 + fx1) / 2, y0), ((fx0 + fx1) / 2, 220), ((cx0 + cx1) / 2, 220), ((cx0 + cx1) / 2, y0)], LINE, 5)
    c.ellipse(960, 220, 44, 44, fill=SHEET, outline=INK, width=3)
    c.text(960, 220, 'A', 'bold', 32, INK, 'mm')
    on = t > 3
    # electrons along wire
    if on:
        path = [((fx0 + fx1) / 2, y0), ((fx0 + fx1) / 2, 220), ((cx0 + cx1) / 2, 220), ((cx0 + cx1) / 2, y0)]
        L = [math.dist(path[k], path[k + 1]) for k in range(3)]
        tot = sum(L)
        for k in range(10):
            d = ((t - 3) * 160 + k * tot / 10) % tot
            for j in range(3):
                if d <= L[j]:
                    s = d / L[j]
                    x = path[j][0] + (path[j + 1][0] - path[j][0]) * s
                    y = path[j][1] + (path[j + 1][1] - path[j][1]) * s
                    break
                d -= L[j]
            c.ellipse(x, y, 9, 9, fill=FIELD)
        c.arrow(700, 186, 800, 186, FIELD, 4, 14)
        c.text(750, 160, '电子', 'sans', 24, FIELD, 'mm')
    # Fe ions leaving
    if on:
        for k in range(6):
            ph = ((t - 3) * 0.35 + k / 6) % 1
            x = fx1 + 20 + ph * 380
            y = y0 + 100 + k * 75
            c.ellipse(x, y, 20, 20, fill=mix(BG, (200, 120, 60), 0.8))
            c.text(x, y, 'Fe', 'bold', 15, (255, 255, 255), 'mm')
            c.text(x + 30, y - 16, '2+', 'bold', 15, mix(BG, (200, 120, 60), 1), 'mm')
    # H bubbles at copper
    if t > 5:
        for k in range(9):
            ph = ((t - 5) * 0.5 + k / 9) % 1
            x = cx0 - 22 - (k % 3) * 18
            y = y1 - 40 - ph * (y1 - y0 - 80)
            r = 7 + 6 * ph
            c.ellipse(x, y, r, r, outline=mix(BG, INK, 0.8), width=2)
        c.text(cx0 - 160, y0 + 70, '氢气泡', 'sans', 24, MUTED, 'mm')
    caps = [(0, 3, '一片铁、一片铜，中间夹着盐水布，用导线连起来'),
            (3.2, 9, '铁比铜更容易失去电子：铁原子丢下电子，变成铁离子溶进盐水'),
            (9.2, 15, '电子没法穿过盐水，只能绕道导线，从铁流到铜：这就是电流'),
            (15.2, 20, '在铜片上，电子被盐水里的氢离子接走，冒出氢气泡'),
            (20.2, 24, '气泡越积越多，会挡住反应，电流越来越弱')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

def e02_stack(c, t, i):
    corner_tag(c, '第 02 集 · 串联')
    c.text(60, 96, '一组太弱？叠起来', 'serif', 40, INK)
    n = 1 if t < 3 else (4 if t < 8 else 10)
    if t > 13: n = 10
    bx, base, h = 520, 900, 18
    for k in range(n):
        y = base - (k + 1) * h * 3
        c.rect(bx, y + 2 * h, bx + 260, y + 3 * h, fill=COPPER)
        c.rect(bx + 8, y + h, bx + 252, y + 2 * h, fill=mix(BG, FIELD, 0.35))
        c.rect(bx, y, bx + 260, y + h, fill=mix(BG, MUTED, 0.6))
    c.text(bx + 130, base + 40, '每组从上到下：铁 / 盐水布 / 铜', 'sans', 24, MUTED, 'mm')
    # voltage bars
    gx = 1180
    c.text(gx, 260, '电压', 'sans', 28, MUTED, 'lm')
    for k in range(n):
        c.rect(gx, base - (k + 1) * 50, gx + 120, base - k * 50 - 6, fill=mix(BG, COPPER, 0.25 + 0.75 * fade(t, 0, 0.5)), r=4)
        c.text(gx + 140, base - k * 50 - 28, 'V', 'mono', 22, MUTED, 'lm')
    c.rect(1420, 420, 1840, 600, fill=SHEET, r=12)
    c.text(1450, 460, f'{n} 组', 'serif', 52, INK, 'lm')
    c.text(1450, 530, f'总电压 = {n} × V', 'mono', 32, COPPER, 'lm')
    c.text(1450, 572, 'V = 每组电压（待实测）', 'sans', 22, MUTED, 'lm')
    caps = [(0, 3, '一组铁铜电池，电压只有一点点'),
            (3.2, 8, '把好几组首尾相接叠起来：串联'),
            (8.2, 13, '每多一组，总电压就多加一份'),
            (13.2, 16, '每组到底多少伏？北宋没有锌，用铁片，只能实测')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

# ======================= E03 电生磁 =======================
def e03_ring(c, t, i):
    corner_tag(c, '第 03 集 · 电流周围的磁场')
    c.text(60, 96, '从上往下看：磁针围成了一个圈', 'serif', 40, INK)
    cx, cy, R = 860, 560, 250
    # current state: 0 off (t<4), +1 (4-11), 0 (11-12), -1 (12-18)
    if t < 4: I = 0
    elif t < 11: I = 1
    elif t < 12.5: I = 0
    else: I = -1
    # field circles
    if I != 0:
        for r in (120, 250, 380):
            c.ellipse(cx, cy, r, r, outline=mix(BG, FIELD, 0.35), width=2)
    # wire
    c.ellipse(cx, cy, 34, 34, fill=COPPER)
    if I > 0:
        c.line([(cx - 16, cy - 16), (cx + 16, cy + 16)], BG, 6); c.line([(cx - 16, cy + 16), (cx + 16, cy - 16)], BG, 6)
        c.text(cx, cy + 70, '电流向下（流进屏幕）', 'sans', 24, INK, 'mm')
    elif I < 0:
        c.ellipse(cx, cy, 9, 9, fill=BG)
        c.text(cx, cy + 70, '电流向上（流出屏幕）', 'sans', 24, INK, 'mm')
    else:
        c.text(cx, cy + 70, '断电', 'sans', 24, MUTED, 'mm')
    # needles smooth toward target
    for k in range(8):
        a = k / 8 * 2 * math.pi
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        north = -math.pi / 2
        tang = a + (math.pi / 2 if I > 0 else -math.pi / 2)
        segs = [(0, 0), (4, 1), (11, 0), (12.5, -1)]
        cur = [sg for sg in segs if sg[0] <= t][-1]
        idx = segs.index(cur)
        prevI = segs[idx - 1][1] if idx else 0
        def tgt(I): return north if I == 0 else a + (math.pi / 2 if I > 0 else -math.pi / 2)
        src, dst = tgt(prevI), tgt(cur[1])
        bb = ease((t - cur[0]) / 0.8) if idx else 1
        d = (dst - src + math.pi) % (2 * math.pi) - math.pi
        ang = src + d * bb
        c.ellipse(x, y, 46, 46, outline=LINE, width=2)
        ux, uy = math.cos(ang), math.sin(ang)
        c.poly([(x + ux * 38, y + uy * 38), (x - uy * 9, y + ux * 9), (x + uy * 9, y - ux * 9)], NRED)
        c.poly([(x - ux * 38, y - uy * 38), (x - uy * 9, y + ux * 9), (x + uy * 9, y - ux * 9)], mix(BG, INK, 0.7))
    c.text(1500, 300, '北', 'bold', 30, MUTED, 'mm'); c.arrow(1500, 420, 1500, 330, MUTED, 3, 14)
    caps = [(0, 4, '断电时：所有磁针都指北'),
            (4.2, 11, '通电：磁针转了，沿着导线围成一个圈'),
            (11.2, 12.6, '断电：又都指回北方'),
            (12.8, 18, '电流反向：每根磁针都掉头 —— 磁感线是绕着导线的圆圈')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

random.seed(5)
DOM3 = [(random.uniform(0, 6.28), random.gauss(0, 0.25)) for _ in range(28)]
def e03_magnet(c, t, i):
    corner_tag(c, '第 03 集 · 电磁铁')
    c.text(60, 96, '线圈里放进铁芯，磁性强了很多', 'serif', 40, INK)
    on = 4 < t < 15
    s = ease((t - 4) / 1.2) if t < 15 else 1 - ease((t - 15) / 0.8)
    if t <= 4: s = 0
    # core
    x0, x1, y0, y1 = 520, 1300, 470, 610
    c.rect(x0, y0, x1, y1, fill=mix(BG, MUTED, 0.4), r=10)
    for k, (a0, a1) in enumerate(DOM3):
        gx = x0 + 40 + (k % 14) * 54
        gy = y0 + 40 + (k // 14) * 60
        a = a0 + ((a1 - a0 + math.pi) % (2 * math.pi) - math.pi) * s
        c.arrow(gx - 18 * math.cos(a), gy - 18 * math.sin(a), gx + 18 * math.cos(a), gy + 18 * math.sin(a), INK, 3, 9)
    # coil
    for k in range(14):
        x = x0 + 30 + k * 55
        c.ellipse(x, (y0 + y1) / 2, 14, 110, outline=COPPER, width=5)
    c.text((x0 + x1) / 2, y0 - 150, '线圈', 'sans', 26, COPPER, 'mm')
    c.text((x0 + x1) / 2, y1 + 150, '软铁芯，里面是一个个小磁区', 'sans', 26, MUTED, 'mm')
    # clips
    nclip = int(round(9 * s)) if t < 15 else int(round(9 * s))
    for k in range(9):
        cx = x1 + 80
        if k < nclip:
            y = y0 + 10 + k * 18
            c.rect(cx, y, cx + 60, y + 12, outline=mix(BG, INK, 0.8), width=3, r=6)
        else:
            c.rect(cx + 20 + (k % 3) * 70, 900 - (k // 3) * 22, cx + 80 + (k % 3) * 70, 912 - (k // 3) * 22, outline=mix(BG, INK, 0.6), width=3, r=6)
    c.text(x1 + 200, 380, '回形针', 'sans', 24, MUTED, 'mm')
    caps = [(0, 4, '断电时：铁芯里的小磁区各朝各的方向，互相抵消'),
            (4.2, 10, '通电：线圈的磁场把小磁区排整齐，铁芯变成一块强磁铁'),
            (10.2, 15, '绕的圈数越多、电流越大，磁性越强'),
            (15.2, 20, '一断电，磁性就消失 —— 这是电磁铁比磁石好用的地方')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

# ======================= E05 手摇发电机 =======================
def e05_lenz(c, t, i):
    corner_tag(c, '第 05 集 · 楞次定律')
    c.text(60, 96, '接上灯，手柄为什么变沉？', 'serif', 40, INK)
    states = [(0, 7, '空载', 0.0), (7, 14, '接一盏灯', 0.5), (14, 22, '短路', 1.0)]
    st = [s for s in states if s[0] <= t < s[1]] or [states[-1]]
    name, load = st[0][2], st[0][3]
    a = t * 3.0
    RX, RY = 520, 560
    c.ellipse(RX, RY, 190, 190, outline=LINE, width=2)
    ux, uy = math.cos(a), math.sin(a)
    def bar(s0, s1, col):
        px, py = -uy, ux
        c.poly([(RX + ux * s0 + px * 32, RY + uy * s0 + py * 32), (RX + ux * s1 + px * 32, RY + uy * s1 + py * 32),
                (RX + ux * s1 - px * 32, RY + uy * s1 - py * 32), (RX + ux * s0 - px * 32, RY + uy * s0 - py * 32)], col)
    bar(0, 160, NRED); bar(-160, 0, SBLUE)
    # coil above
    for j in range(7):
        c.ellipse(RX, 260 + j * 20, 72, 11, outline=COPPER, width=5)
    # crank handle
    hx, hy = RX + 230 * math.cos(a + 0.6), RY + 230 * math.sin(a + 0.6)
    c.line([(RX, RY), (hx, hy)], MUTED, 8); c.ellipse(hx, hy, 18, 18, fill=MUTED)
    # bulb
    cur = load * (0.6 + 0.4 * abs(math.sin(a)))
    if load == 0.5:
        c.ellipse(1000, 280, 40, 40, fill=mix(BG, SPARK, 0.2 + 0.8 * abs(math.sin(a))), outline=MUTED, width=2)
        c.text(1000, 350, '灯', 'sans', 24, MUTED, 'mm')
    if load == 1.0:
        c.line([(960, 240), (1040, 320)], NRED, 5); c.text(1000, 350, '两根线直接接通', 'sans', 24, NRED, 'mm')
    # counter-field arrows on coil
    if load > 0:
        k = load
        c.arrow(RX + 120, 300, RX + 120, 300 + 80 * k, mix(BG, FIELD, k), 5, 16)
        c.text(RX + 150, 330, '线圈的反向磁场', 'sans', 24, mix(BG, FIELD, k), 'lm')
    # meters
    mx = 1250
    for k, (lab, val, col) in enumerate([('电流', cur, FIELD), ('手柄阻力', 0.08 + 0.9 * load * (0.7 + 0.3 * abs(math.sin(a))), COPPER)]):
        y = 520 + k * 140
        c.text(mx, y, lab, 'sans', 28, MUTED, 'lm')
        c.rect(mx, y + 30, mx + 540, y + 56, fill=LINE, r=13)
        c.rect(mx, y + 30, mx + 540 * min(1, val), y + 56, fill=col, r=13)
    c.rect(mx, 360, mx + 540, 450, fill=SHEET, r=12)
    c.text(mx + 270, 405, f'现在：{name}', 'serif', 40, INK, 'mm')
    caps = [(0, 7, '空载：线圈里几乎没有电流，手柄很轻'),
            (7.2, 14, '接上灯：电流流动，线圈自己也变成磁铁，反推转动的磁铁'),
            (14.2, 22, '短路：电流最大，反推最强，手柄最沉 —— 电能来自你使的劲')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

def e05_comm(c, t, i):
    corner_tag(c, '第 05 集 · 换向器')
    c.text(60, 96, '每转半圈，接线对调一次', 'serif', 40, INK)
    useC = t >= 9
    th = t * 2.2
    v = math.sin(th)
    out = abs(v) if useC else v
    cx, cy = 480, 560
    # commutator ring: two half rings rotating
    for half, col in ((0, COPPER), (1, mix(BG, COPPER, 0.6))):
        a0 = math.degrees(th) + half * 180
        if useC:
            c.arc(cx, cy, 120, 120, a0 + 8, a0 + 172, col, 26)
        else:
            c.arc(cx, cy, 120 if half == 0 else 170, 120 if half == 0 else 170, 0, 360, col, 20)
    c.ellipse(cx, cy, 40, 40, fill=MUTED)
    # brushes
    c.rect(cx - 30, cy - 220 if useC else cy - 260, cx + 30, cy - 160 if useC else cy - 200, fill=INK, r=4)
    c.rect(cx - 30, cy + 160 if useC else cy + 200, cx + 30, cy + 220 if useC else cy + 260, fill=INK, r=4)
    c.text(cx + 60, cy - 230, '电刷', 'sans', 24, MUTED, 'lm')
    c.text(cx, 860, '换向器：两片半圆铜环' if useC else '没有换向器：两个整圆铜环', 'bold', 30, COPPER if useC else MUTED, 'mm')
    # graph
    gx0, gx1, gm, ga = 860, 1820, 560, 200
    c.line([(gx0, gm), (gx1, gm)], LINE, 2); c.line([(gx0, gm - 260), (gx0, gm + 260)], LINE, 2)
    c.text(gx0 + 12, gm - 260, '输出电压', 'sans', 24, MUTED, 'lm')
    W = 5.0
    t0 = max(0, t - W); prev = None
    for k in range(241):
        tt = t0 + (t - t0) * k / 240
        if t - t0 < 1e-6: break
        vv = math.sin(tt * 2.2); vv = abs(vv) if tt >= 9 else vv
        x = gx1 - (t - tt) / W * (gx1 - gx0); y = gm - vv * ga
        if prev: c.line([prev, (x, y)], COPPER if y <= gm else FIELD, 5)
        prev = (x, y)
    caps = [(0, 9, '线圈在磁场里转，电压一正一负：交流电'),
            (9.2, 14, '装上换向器：每转半圈，接线自动对调一次'),
            (14.2, 18, '输出变成一个方向的脉动电流：直流电，可以用来电解、电镀')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, 1010, s_, 'bold', 34, mix(BG, INK, al), 'mm')

ERA = '北宋 · 约公元 1090 年 · 一座没有电的工坊'
V1 = titles.VOL1
def op(k): return titles.opening('从零造物', '第一卷 · 电', V1, k, ERA)
def cl(k, s): return titles.closing('从零造物', '第一卷 · 电', V1, k, s)

CLIPS = {
 'E01_电子转移': (e01_transfer, 20), 'E01_莱顿瓶': (e01_leyden, 22),
 'E01_片头': (op(0), 7), 'E01_片尾': (cl(0, '下集：静电存不住，怎样得到持续的电？'), 7),
 'E02_电堆微观': (e02_micro, 24), 'E02_串联': (e02_stack, 16),
 'E02_片头': (op(1), 7), 'E02_片尾': (cl(1, '下集：有了持续的电流，指南针为什么会乱转？'), 7),
 'E03_环形磁场': (e03_ring, 18), 'E03_电磁铁': (e03_magnet, 20),
 'E03_片头': (op(2), 7), 'E03_片尾': (cl(2, '下集：电能生磁，那磁能不能生电？'), 7),
 'E05_楞次定律': (e05_lenz, 22), 'E05_换向器': (e05_comm, 18),
 'E05_片头': (op(4), 7), 'E05_片尾': (cl(4, '第一卷完结 · 下一卷：让河水替我们摇'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2:
        kit.preview(CLIPS, sys.argv[1], float(sys.argv[2]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
