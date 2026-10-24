"""第七季第二批：E12 热电、E13 压电、E14 静电机 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s7a import S7A, SER7, VOL7

IRONC = (150, 160, 170)
HOT = (235, 110, 60)
COLD = (90, 150, 220)

# ---------------------------------------------------------------- E12 热电
def e12_seebeck(c, t, i):
    corner_tag(c, '第 12 集 · 塞贝克效应')
    c.text(60, 96, '一头热、一头冷，电子为什么会「搬家」？', 'serif', 40, INK)
    # one long wire, hot left, cold right
    x0, x1, y = 260, 1660, 380
    heat = fade(t, 1, 3)
    for k in range(60):
        x = x0 + (x1 - x0) * k / 59
        f = 1 - k / 59
        col = mix(mix(INK, COLD, 0.6), mix(INK, HOT, 0.8), f * heat)
        c.rect(x - 12, y - 50, x + 12, y + 50, fill=mix(BG, col, 0.35))
    c.rect(x0 - 10, y - 52, x1 + 10, y + 52, outline=MUTED, width=3, r=6)
    c.text(x0, y + 90, '热端', 'bold', 28, HOT, 'lm')
    c.text(x1, y + 90, '冷端', 'bold', 28, COLD, 'rm')
    if heat > 0:
        for k in range(5):
            fx = x0 + 130 + k * 28
            fh = 60 + 30 * math.sin(t * 9 + k)
            c.poly([(fx - 14, y + 150), (fx + 14, y + 150), (fx, y + 150 - fh * heat)], mix(BG, SPARK, heat))
    rnd = random.Random(7)
    drift = fade(t, 4, 12)
    for k in range(70):
        bx = rnd.uniform(x0 + 20, x1 - 20)
        by = rnd.uniform(y - 38, y + 38)
        f = 1 - (bx - x0) / (x1 - x0)
        amp = 4 + 14 * f * heat
        # net drift toward cold end, piling up there
        tx = x0 + 20 + (x1 - x0 - 40) * ((bx - x0 - 20) / (x1 - x0 - 40)) ** (1 - 0.4 * drift)
        px = tx + amp * math.sin(t * 13 + k * 1.7)
        py = by + amp * math.cos(t * 11 + k * 2.3)
        c.ellipse(px, py, 7, 7, fill=FIELD)
    a = fade(t, 9, 10)
    if a > 0:
        c.text(x0 + 200, y - 90, '缺了电子 → 带正电', 'bold', 28, mix(BG, NRED, a), 'mm')
        c.text(x1 - 200, y - 90, '电子堆积 → 带负电', 'bold', 28, mix(BG, FIELD, a), 'mm')
        c.arrow(x0 + 400, y - 90, x1 - 420, y - 90, mix(BG, MUTED, a), 4, 16)
    b = fade(t, 13, 14)
    c.rect(260, 640, 1660, 900, fill=mix(BG, SHEET, b), r=14)
    c.text(960, 690, '可一根导线自己测不出电压：表笔接上去，表笔的导线也在同样的温差里', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 750, '两种金属「搬家」的程度不同 —— 铜和铁接在一起，差值才露出来', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 830, '电压大致 ∝ 温差：铜—铁每度只有十几微伏（拍摄前核对）', 'bold', 30, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 4, '一根金属丝，一头加热'),
                (4.2, 9, '热端的电子跑得更欢，往冷端扩散得更多'),
                (9.2, 13, '冷端堆了电子带负电，热端缺了电子带正电'),
                (13.2, 22, '不同金属搬家的程度不同：两种金属接成一对，差值就是能测到的电压')], y=1010)

def e12_pile(c, t, i):
    corner_tag(c, '第 12 集 · 热电堆')
    c.text(60, 96, '只有一毫伏，怎么让它有用？', 'serif', 40, INK)
    n = 1 if t < 5 else (4 if t < 10 else 10)
    yh, yc = 330, 690
    c.rect(150, yh - 60, 1770, yh - 20, fill=mix(BG, HOT, 0.5), r=10)
    c.text(960, yh - 95, '热（100 ℃ 的开水）', 'bold', 26, HOT, 'mm')
    c.rect(150, yc + 20, 1770, yc + 60, fill=mix(BG, COLD, 0.5), r=10)
    c.text(960, yc + 95, '冷（0 ℃ 的冰水）', 'bold', 26, COLD, 'mm')
    w = 1500 / 10
    for k in range(n):
        xa = 210 + k * w
        xb = xa + w * 0.5
        xc = xa + w
        c.line([(xa, yc), (xb, yh)], COPPER, 8)
        c.line([(xb, yh), (xc if k < n - 1 else xc, yc)], IRONC, 8)
        c.ellipse(xb, yh, 10, 10, fill=SPARK)
        if k > 0: c.ellipse(xa, yc, 10, 10, fill=COLD)
    end = 210 + n * w
    c.line([(210, yc), (210, 860)], COPPER, 5)
    c.line([(end, yc), (end, 860)], IRONC, 5)
    mv = 1.3 * n
    c.rect(1500, 800, 1860, 920, fill=SHEET, outline=MUTED, width=3, r=12)
    c.text(1680, 860, f'约 {mv:.1f} 毫伏', 'mono', 34, SPARK, 'mm')
    c.line([(210, 860), (1500, 860)], MUTED, 3)
    c.line([(end, 860), (end, 860)], MUTED, 3)
    c.text(120, 860, f'{n} 对', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 5, '一对铜—铁接点，一头开水、一头冰水：只有一毫伏多（数字示意，以实测为准）'),
                (5.2, 10, '把很多对串起来，热的接点都在上面、冷的接点都在下面，电压一对一对加起来'),
                (10.2, 22, '这就是热电堆。今天的热电偶温度计、旅行者号探测器的核电池，用的都是它')], y=1010)

# ---------------------------------------------------------------- E13 压电
def crystal(c, cx, cy, sq, sc=1.0, show_centers=True):
    """hexagon of +/- ions; sq: squeeze 0..1 (vertical)"""
    R = 150 * sc
    pts = []
    for k in range(6):
        ang = math.pi / 6 + k * math.pi / 3
        x = cx + R * math.cos(ang)
        y = cy + R * math.sin(ang) * (1 - 0.35 * sq)
        pts.append((x, y))
    for k in range(6):
        a_, b_ = pts[k], pts[(k + 1) % 6]
        c.line([a_, b_], LINE, 5)
    for k, (x, y) in enumerate(pts):
        pos = k % 2 == 0
        c.ellipse(x, y, 26 * sc, 26 * sc, fill=NRED if pos else SBLUE)
        c.text(x, y, '+' if pos else '−', 'bold', int(30 * sc), INK, 'mm')
    if show_centers:
        py = sum(p[1] for k, p in enumerate(pts) if k % 2 == 0) / 3
        ny = sum(p[1] for k, p in enumerate(pts) if k % 2 == 1) / 3
        px = sum(p[0] for k, p in enumerate(pts) if k % 2 == 0) / 3
        nx = sum(p[0] for k, p in enumerate(pts) if k % 2 == 1) / 3
        c.ellipse(px, py, 8, 8, outline=NRED, width=3)
        c.ellipse(nx, ny, 8, 8, outline=SBLUE, width=3)
        return (px, py), (nx, ny), pts
    return None, None, pts

def e13_crystal(c, t, i):
    corner_tag(c, '第 13 集 · 挤一挤就有电')
    c.text(60, 96, '捏一下晶体，电从哪来？', 'serif', 40, INK)
    sq = 0.0
    if t > 6: sq = ease(min(1, (t - 6) / 2))
    if t > 15: sq = 1 - ease(min(1, (t - 15) / 1.5))
    cx, cy = 700, 540
    pc, nc, pts = crystal(c, cx, cy, sq)
    # pressing plates
    gap = 150 * (1 - 0.35 * sq) + 40
    c.rect(cx - 220, cy - gap - 20, cx + 220, cy - gap, fill=MUTED, r=4)
    c.rect(cx - 220, cy + gap, cx + 220, cy + gap + 20, fill=MUTED, r=4)
    if sq > 0.05:
        c.arrow(cx, cy - gap - 120, cx, cy - gap - 30, mix(BG, INK, sq), 6, 18)
        c.arrow(cx, cy + gap + 120, cx, cy + gap + 30, mix(BG, INK, sq), 6, 18)
    a = fade(t, 2, 3)
    c.text(1150, 300, '不挤：正电荷中心 ○ 和负电荷中心 ○', 'sans', 28, mix(BG, INK, a), 'lm')
    c.text(1150, 345, '重合在一起，对外不显电', 'sans', 28, mix(BG, INK, a), 'lm')
    b = fade(t, 8, 9) * (1 if t < 15 else 1 - fade(t, 15, 16))
    c.text(1150, 450, '挤扁：两个中心被挤得错开', 'bold', 30, mix(BG, SPARK, b), 'lm')
    c.text(1150, 495, '一面多出正电，另一面多出负电', 'bold', 30, mix(BG, SPARK, b), 'lm')
    if b > 0:
        c.text(cx + 260, cy - 60, '+ + +', 'bold', 34, mix(BG, NRED, b), 'lm')
        c.text(cx + 260, cy + 60, '− − −', 'bold', 34, mix(BG, SBLUE, b), 'lm')
    d = fade(t, 16, 17)
    c.rect(1120, 620, 1840, 860, fill=mix(BG, SHEET, d), r=14)
    c.text(1150, 670, '反过来也行：加电压，晶体就变形', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1150, 720, '石英表里的石英片，每秒振动 32768 次', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1150, 790, '压电效应：1880 年居里兄弟发现', 'bold', 28, mix(BG, SPARK, d), 'lm')
    caps(c, t, [(0, 6, '晶体里正负离子排得整整齐齐，正电和负电的中心刚好重合'),
                (6.2, 15, '一挤，形状变了，两个中心错开：一面带正电，另一面带负电，就有了电压'),
                (15.2, 22, '松手又回去。反过来，给它加电压，它会变形 —— 石英表就是靠这个计时')], y=1010)

def e13_igniter(c, t, i):
    corner_tag(c, '第 13 集 · 打火机的点火器')
    c.text(60, 96, '一按「咔哒」一声，火花从哪来？', 'serif', 40, INK)
    # housing
    c.rect(300, 300, 1100, 620, outline=MUTED, width=4, r=20)
    c.text(700, 660, '点火器内部（示意）', 'sans', 24, MUTED, 'mm')
    # crystal block
    c.rect(780, 380, 900, 540, fill=mix(BG, FIELD, 0.5), outline=FIELD, width=3, r=6)
    c.text(840, 440, '压电', 'bold', 24, INK, 'mm'); c.text(840, 480, '陶瓷', 'bold', 24, INK, 'mm')
    # spring & hammer: compress 1-5s, release at 5
    comp = fade(t, 1, 5)
    hit = t >= 5.0
    hx = 420 + 200 * comp if not hit else min(760, 620 + (t - 5) * 3000)
    coils = 10
    pts = []
    for k in range(coils * 4 + 1):
        x = 330 + (hx - 60 - 330) * k / (coils * 4)
        y = 460 + 40 * math.sin(k * math.pi / 2)
        pts.append((x, y))
    seg(c, pts, MUTED, 4)
    c.rect(hx - 60, 410, hx, 510, fill=IRONC, r=6)
    c.text(hx - 30, 380, '小锤', 'sans', 22, MUTED, 'mm')
    # wires to spark gap
    c.line([(900, 420), (1300, 420), (1300, 330)], COPPER, 5)
    c.line([(900, 500), (1300, 500), (1300, 560)], COPPER, 5)
    c.line([(1300, 330), (1300, 420)], COPPER, 5)
    c.ellipse(1300, 420, 8, 8, fill=COPPER)
    c.ellipse(1300, 500, 8, 8, fill=COPPER)
    if hit and t < 5.6:
        rnd = random.Random(int(t * 30))
        zz = [(1300, 425)]
        for k in range(1, 6):
            zz.append((1300 + rnd.uniform(-18, 18), 425 + k * 15))
        zz.append((1300, 495))
        c.line(zz, SPARK, 6)
        c.ellipse(1300, 460, 40, 40, outline=mix(BG, SPARK, 0.5), width=3)
    if t > 5.6:
        c.text(1330, 460, '电火花', 'bold', 28, SPARK, 'lm')
    a = fade(t, 1, 2)
    c.text(320, 250, '① 按下：压缩弹簧', 'sans', 26, mix(BG, INK, a), 'lm')
    b = fade(t, 5, 5.5)
    c.text(740, 250, '② 锁扣松开：小锤猛敲陶瓷', 'sans', 26, mix(BG, INK, b), 'lm')
    d = fade(t, 8, 9)
    c.rect(300, 740, 1620, 940, fill=mix(BG, SHEET, d), r=14)
    c.text(960, 790, '猛敲一下，陶瓷两端瞬间出现几千伏的电压（拍摄前核对），跳过几毫米的空气', 'sans', 26, mix(BG, INK, d), 'mm')
    c.text(960, 850, '电压很高，但电荷极少、能量极小：所以只能点燃气体，不能当电池用', 'bold', 28, mix(BG, SPARK, d), 'mm')
    c.text(960, 900, '火石打火是另一回事：那是敲下来的铁屑在空气里燃烧', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 5, '按下按钮，先把一根弹簧压紧'),
                (5.2, 8, '压到底，锁扣松开，小锤狠狠敲在压电陶瓷上'),
                (8.2, 22, '一下猛挤，几千伏的电压跳过空气，就是那道火花')], y=1010)

# ---------------------------------------------------------------- E14 静电机
def e14_electrophorus(c, t, i):
    corner_tag(c, '第 14 集 · 起电盘')
    c.text(60, 96, '摩擦一次，为什么能取一百次电？', 'serif', 40, INK)
    # phases: 0-4 rubbed plate (-) ; 4-8 put pan on: induction ; 8-12 touch top: - leaves ; 12-16 lift: pan + ; 16-22 spark & repeat
    px, py = 960, 720
    c.rect(px - 400, py, px + 400, py + 50, fill=mix(BG, (70, 70, 80), 1), r=8)
    c.text(px + 430, py + 25, '塑料板（摩擦后带负电）', 'sans', 24, MUTED, 'lm')
    for k in range(10):
        c.text(px - 360 + k * 80, py + 25, '−', 'bold', 30, SBLUE, 'mm')
    ph = t % 22
    lift = 0
    if 12 <= ph < 16: lift = ease((ph - 12) / 2) * 260
    if ph >= 16: lift = 260
    yp = py - 30 - lift
    show = ph >= 4
    if show:
        c.rect(px - 300, yp - 24, px + 300, yp, fill=(180, 185, 190), r=6)
        c.line([(px, yp - 24), (px, yp - 160)], (200, 160, 90), 10)
        c.text(px + 30, yp - 150, '绝缘把手', 'sans', 22, MUTED, 'lm')
        c.text(px - 330, yp - 12, '金属盘', 'sans', 24, MUTED, 'rm')
        if ph < 8:
            a = fade(ph, 4.5, 6)
            for k in range(6):
                c.text(px - 250 + k * 100, yp + 4 + 14, '+', 'bold', 26, mix(BG, NRED, a), 'mm')
                c.text(px - 250 + k * 100, yp - 40, '−', 'bold', 26, mix(BG, SBLUE, a), 'mm')
        elif ph < 12:
            # finger touches, minus leaves
            fx = px + 200
            c.ellipse(fx, yp - 70, 26, 40, fill=(220, 180, 150))
            leave = fade(ph, 8.5, 11)
            for k in range(6):
                c.text(px - 250 + k * 100, yp + 18, '+', 'bold', 26, NRED, 'mm')
                if leave < 1:
                    c.text(px - 250 + k * 100 + (fx - (px - 250 + k * 100)) * leave, yp - 40 - 200 * leave, '−', 'bold', 26, mix(SBLUE, BG, leave), 'mm')
            c.text(fx + 50, yp - 90, '手指一碰：负电从人身上流走', 'sans', 24, INK, 'lm')
        else:
            for k in range(6):
                c.text(px - 250 + k * 100, yp + 18 if lift < 100 else yp - 12, '+', 'bold', 26, NRED, 'mm')
            if ph >= 16:
                kn = (px + 420, yp - 12)
                c.ellipse(kn[0] + 40, kn[1], 18, 18, fill=COPPER)
                if 16.5 < ph < 17.2:
                    c.line([(px + 300, yp - 12), (px + 340, yp - 30), (px + 370, yp + 5), (px + 405, yp - 12)], SPARK, 6)
                c.text(px + 420, yp - 60, '靠近金属：啪！', 'bold', 26, SPARK, 'mm')
    a = fade(t, 18, 19)
    c.rect(160, 860, 1760, 950, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 905, '塑料板上的电没用掉，只是「借」来感应：放下、碰一下、提起来，可以一遍遍取电（1762 年维尔克，1775 年伏打）', 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 4, '先把塑料板摩擦一下，让它带上负电'),
                (4.2, 8, '放上金属盘：负电把盘里的负电推到上面，正电吸到下面'),
                (8.2, 12, '用手指碰一下上面，负电就顺着人流走了'),
                (12.2, 16, '提起金属盘：剩下的正电没处去，盘子带了电'),
                (16.2, 22, '一靠近金属就是一道火花。提起来要用力：这份力气，就是电的来源')], y=1035)

def e14_wimshurst(c, t, i):
    corner_tag(c, '第 14 集 · 感应起电机')
    c.text(60, 96, '把「放下、碰一下、提起来」交给一个转盘', 'serif', 40, INK)
    cx, cy, R = 700, 540, 290
    ang = t * 1.6
    c.ellipse(cx, cy, R, R, fill=mix(BG, (60, 70, 80), 0.6), outline=MUTED, width=4)
    for k in range(16):
        a_ = ang + k * 2 * math.pi / 16
        x0, y0 = cx + 170 * math.cos(a_), cy + 170 * math.sin(a_)
        x1, y1 = cx + 270 * math.cos(a_), cy + 270 * math.sin(a_)
        c.line([(x0, y0), (x1, y1)], (180, 185, 190), 12)
        # charge carried: + on upper half moving right, - on lower half
        sy = math.sin(a_)
        mark = '+' if math.cos(a_) > 0 else '−'
        col = NRED if mark == '+' else SBLUE
        if fade(t, 3, 5) > 0:
            c.text(cx + 220 * math.cos(a_), cy + 220 * math.sin(a_) - 22, mark, 'bold', 24, mix(BG, col, fade(t, 3, 5)), 'mm')
    c.ellipse(cx, cy, 20, 20, fill=MUTED)
    # combs at left and right
    for side, lab, col in [(-1, '集电梳（−）', SBLUE), (1, '集电梳（+）', NRED)]:
        x = cx + side * (R + 30)
        c.line([(x, cy - 50), (x, cy + 50)], COPPER, 6)
        for k in range(5):
            c.line([(x, cy - 40 + k * 20), (x - side * 20, cy - 40 + k * 20)], COPPER, 3)
        c.text(x + side * 30, cy - 90, lab, 'sans', 22, col, 'mm')
        # leyden jar
        jx = x + side * 180
        c.rect(jx - 45, 700, jx + 45, 860, outline=MUTED, width=3, r=8)
        c.rect(jx - 45, 770, jx + 45, 860, fill=mix(BG, (180, 185, 190), 0.5), r=8)
        c.line([(x, cy + 50), (x, 640), (jx, 640), (jx, 700)], COPPER, 4)
    c.text(cx - (R + 210), 890, '莱顿瓶', 'sans', 22, MUTED, 'mm')
    c.text(cx + (R + 210), 890, '莱顿瓶', 'sans', 22, MUTED, 'mm')
    # spark gap above
    lx, rx = cx - 90, cx + 90
    c.line([(cx - (R + 210), 640), (cx - (R + 210), 180), (lx - 20, 180)], COPPER, 4)
    c.line([(cx + (R + 210), 640), (cx + (R + 210), 180), (rx + 20, 180)], COPPER, 4)
    c.ellipse(lx, 180, 20, 20, fill=COPPER)
    c.ellipse(rx, 180, 20, 20, fill=COPPER)
    period = 3.0
    if t > 8 and (t - 8) % period < 0.18:
        rnd = random.Random(int(t * 40))
        zz = [(lx + 20, 180)] + [(lx + 20 + k * 28, 180 + rnd.uniform(-20, 20)) for k in range(1, 5)] + [(rx - 20, 180)]
        c.line(zz, SPARK, 6)
    a = fade(t, 10, 11)
    c.rect(1240, 260, 1860, 640, fill=mix(BG, SHEET, a), r=14)
    c.text(1270, 310, '转盘上的金属片轮流经过：', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 360, '被感应 → 接地放走异号电荷', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 410, '→ 带着电转过去 → 交给集电梳', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 480, '每转一圈，就是很多次「起电盘」', 'bold', 28, mix(BG, SPARK, a), 'lm')
    c.text(1270, 540, '电存进莱顿瓶，攒够了就跳火花', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 600, '1880 年代维姆斯赫斯特起电机', 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 3, '把起电盘的动作交给一个转盘'),
                (3.2, 10, '盘上的金属片一圈圈转：一边被感应、一边把电荷送到集电梳'),
                (10.2, 22, '电荷存进两只莱顿瓶，攒够了就噼啪跳一道火花：手一直摇，静电就源源不断')], y=1010)

CLIPS = {
 'E12_塞贝克效应': (e12_seebeck, 22), 'E12_热电堆': (e12_pile, 22),
 'E12_片头': (titles.opening(SER7, VOL7, S7A, 3, '穿越北宋 · 把热直接变成电'), 7),
 'E12_片尾': (titles.closing(SER7, VOL7, S7A, 3, '下集：按一下打火机，为什么冒火花？'), 7),
 'E13_挤一挤': (e13_crystal, 22), 'E13_点火器': (e13_igniter, 22),
 'E13_片头': (titles.opening(SER7, VOL7, S7A, 4, '穿越北宋 · 挤一挤，就有电'), 7),
 'E13_片尾': (titles.closing(SER7, VOL7, S7A, 4, '下集：怎样让静电源源不断？'), 7),
 'E14_起电盘': (e14_electrophorus, 22), 'E14_感应起电机': (e14_wimshurst, 22),
 'E14_片头': (titles.opening(SER7, VOL7, S7A, 5, '穿越北宋 · 让第 01 集的静电不停下来'), 7),
 'E14_片尾': (titles.closing(SER7, VOL7, S7A, 5, '下集：蒸汽怎么变成电？（只用动画）'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
