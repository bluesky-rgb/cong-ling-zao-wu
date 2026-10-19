"""第二季收尾：E17 炼铜、B4 水排、E18 炼铁、第二季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL, wheel
from s2a import S2A, SER, VOL, FIRE, flame
from s2b import SB2

CU = (214, 110, 70)
CUBLUE = (70, 140, 220)
FEGREEN = (170, 210, 170)
IRON = (130, 134, 140)
CHAR = (50, 46, 44)

# ---------------------------------------------------------------- E17 炼铜
RC = random.Random(17)
IONS = [(RC.uniform(-1, 1), RC.uniform(-1, 1), RC.uniform(0, 6)) for _ in range(60)]

def e17_displace(c, t, i):
    corner_tag(c, '第 17 集 · 胆水浸铜')
    c.text(60, 96, '一根铁钉放进蓝色的水，为什么会长出铜？', 'serif', 40, INK)
    prog = fade(t, 5, 18)
    x0, y0, x1, y1 = 300, 240, 1100, 900
    c.rect(x0 + 6, y0 + 60, x1 - 6, y1 - 6, fill=mix(mix(BG, CUBLUE, 0.45), mix(BG, FEGREEN, 0.35), prog), r=10)
    c.rect(x0, y0, x1, y1, outline=MUTED, width=5, r=20)
    nx = 700
    c.rect(nx - 26, 180, nx + 26, 840, fill=IRON, r=8)
    c.rect(nx - 60, 170, nx + 60, 196, fill=IRON, r=6)
    # copper coating grows
    if prog > 0:
        th = 4 + 18 * prog
        top = 300
        c.rect(nx - 26 - th, top, nx - 26, 840, fill=CU)
        c.rect(nx + 26, top, nx + 26 + th, 840, fill=CU)
        c.rect(nx - 26 - th, 840, nx + 26 + th, 840 + th, fill=CU)
    # ions
    for k, (u, v, ph) in enumerate(IONS):
        x = (x0 + x1) / 2 + u * 360 + 10 * math.sin(t + ph)
        y = 600 + v * 260 + 8 * math.cos(t * 1.3 + ph)
        if abs(x - nx) < 70: x += 120 * (1 if x >= nx else -1)
        is_cu = (k / len(IONS)) > prog
        if is_cu:
            c.ellipse(x, y, 13, 13, fill=CUBLUE)
            c.text(x, y, 'Cu', 'bold', 12, BG, 'mm')
        else:
            c.ellipse(x, y, 13, 13, fill=FEGREEN)
            c.text(x, y, 'Fe', 'bold', 12, BG, 'mm')
    # electron arrows near surface
    if 6 < t < 18:
        for k in range(4):
            yy = 380 + k * 110
            ph = (t * 1.2 + k * 0.3) % 1
            c.arrow(nx + 30, yy, nx + 30 + 80 * ph + 10, yy, SPARK, 3, 10)
        c.text(nx + 160, 340, '电子：铁 → 铜离子', 'sans', 24, SPARK, 'lm')
    px = 1200
    c.rect(px, 240, 1860, 900, fill=SHEET, r=16)
    c.text(px + 30, 300, '铁 + 硫酸铜 → 硫酸亚铁 + 铜', 'bold', 30, INK, 'lm')
    c.text(px + 30, 380, '铁比铜更容易失去电子', 'sans', 28, INK, 'lm')
    c.text(px + 30, 425, '（和第 02 集的电堆是同一个道理）', 'sans', 24, MUTED, 'lm')
    c.text(px + 30, 520, '沈括《梦溪笔谈》：', 'sans', 26, MUTED, 'lm')
    c.text(px + 30, 575, '「熬胆矾铁釜，', 'serif', 36, COPPER, 'lm')
    c.text(px + 30, 630, '久之亦化为铜」', 'serif', 36, COPPER, 'lm')
    c.text(px + 30, 720, '不用火、不用高温', 'bold', 28, FIELD, 'lm')
    c.text(px + 30, 765, '北宋已经大规模用它产铜', 'sans', 26, INK, 'lm')
    caps(c, t, [(0, 5, '胆水：溶着硫酸铜的蓝色泉水'),
                (5.2, 12, '铁把电子交给铜离子：铜变成金属，贴在铁上；铁变成离子溶进水里'),
                (12.2, 18, '蓝色慢慢褪去，铁钉裹上一层红铜'),
                (18.2, 22, '这叫「胆水浸铜」：世界上最早的湿法冶金之一')])

def e17_smelt(c, t, i):
    corner_tag(c, '第 17 集 · 火法炼铜')
    c.text(60, 96, '绿色的石头，怎么烧出红色的铜？', 'serif', 40, INK)
    T = 300 + 900 * fade(t, 1, 14)
    fx0, fx1, fy0, fy1 = 480, 1000, 260, 900
    c.poly([(fx0, fy0), (fx1, fy0), (fx1 + 60, fy1), (fx0 - 60, fy1)], (90, 70, 60))
    c.poly([(fx0 + 40, fy0 + 10), (fx1 - 40, fy0 + 10), (fx1 + 10, fy1 - 30), (fx0 - 10, fy1 - 30)], mix((40, 30, 28), FIRE, min(1, (T - 300) / 900) * 0.55))
    R = random.Random(3)
    for k in range(70):
        x = R.uniform(fx0 + 20, fx1 - 20); y = R.uniform(fy0 + 40, fy1 - 140)
        mal = k % 3 == 0
        col = (60, 160, 110) if mal else CHAR
        if mal and T > 800: col = mix((60, 160, 110), (60, 40, 30), fade(T, 800, 1000))
        c.rect(x - 16, y - 12, x + 16, y + 12, fill=col, r=6)
    if T > 1084:
        pool = fade(T, 1084, 1200)
        c.rect(fx0 - 10, fy1 - 30 - 60 * pool, fx1 + 10, fy1 - 30, fill=mix(CU, SPARK, 0.4), r=6)
        c.text((fx0 + fx1) / 2, fy1 - 30 - 30 * pool, '铜水', 'bold', 28, BG, 'mm')
    # air in
    for k in range(3):
        ph = (t * 1.5 + k / 3) % 1
        c.arrow(fx0 - 220 + ph * 160, 820, fx0 - 200 + ph * 160 + 40, 820, FIELD, 4, 12)
    c.text(fx0 - 160, 780, '鼓风', 'sans', 26, FIELD, 'mm')
    for k in range(5):
        ph = (t * 0.6 + k / 5) % 1
        c.text(fx0 + 60 + k * 90, fy0 - 20 - ph * 100, 'CO2', 'mono', 20, mix(BG, MUTED, 1 - ph), 'mm')
    px = 1180
    c.rect(px, 240, 1860, 900, fill=SHEET, r=16)
    c.text(px + 30, 290, f'炉温约 {T:.0f} ℃（示意）', 'mono', 32, COPPER, 'lm')
    lines = [('孔雀石：铜和氧、碳酸根结合在一起', 300), ('木炭燃烧生成一氧化碳', 600), ('一氧化碳抢走铜身上的氧 → 铜', 800), ('约 1084 ℃：铜熔成铜水，流到炉底', 1084)]
    for k, (s_, thr) in enumerate(lines):
        on = T >= thr
        c.text(px + 30, 380 + k * 80, s_, 'bold' if on else 'sans', 26, INK if on else MUTED, 'lm')
    c.text(px + 30, 760, '要的不只是高温，', 'sans', 26, INK, 'lm')
    c.text(px + 30, 805, '还要碳把氧夺走（还原）', 'bold', 26, COPPER, 'lm')
    caps(c, t, [(0, 5, '孔雀石里没有现成的铜块：铜和氧紧紧结合在一起'),
                (5.2, 11, '木炭在鼓风下燃烧，生成一氧化碳，把氧从铜身上抢走'),
                (11.2, 20, '温度过了一千零八十度，铜熔化，流到炉底')])

# ---------------------------------------------------------------- B4 水排
def b4_crank(c, t, i):
    corner_tag(c, 'B4 · 曲柄连杆')
    c.text(60, 96, '水轮只会转圈，风箱要来回推拉，怎么办？', 'serif', 40, INK)
    a = t * 1.6
    # water wheel (side view)
    wx, wy = 330, 640
    for k in range(5):
        c.line([(60, 920 - k * 6), (600, 920 - k * 6)], mix(BG, FIELD, 0.3 + 0.1 * k), 3)
    wheel(c, wx, wy, 190, a, mix(BG, FIELD, 0.9), 10)
    c.text(wx, 900, '水轮', 'sans', 26, MUTED, 'mm')
    # crank disk
    cx, cy, r = 780, 520, 90
    c.line([(wx, wy), (cx, cy)], MUTED, 8)
    c.ellipse(cx, cy, r, r, outline=COPPER, width=6)
    px_, py_ = cx + r * math.cos(a), cy + r * math.sin(a)
    c.ellipse(px_, py_, 14, 14, fill=SPARK)
    c.text(cx, cy - r - 30, '曲柄（偏心的销子）', 'sans', 24, COPPER, 'mm')
    # connecting rod to slider
    L = 330
    sx = px_ + math.sqrt(max(0, L * L - (py_ - cy) ** 2))
    c.line([(px_, py_), (sx, cy)], INK, 8)
    c.text((px_ + sx) / 2, cy - 40, '连杆', 'sans', 24, INK, 'mm')
    c.rect(sx - 20, cy - 40, sx + 20, cy + 40, fill=IRON, r=4)
    # bellows: box whose length depends on sx
    bx0 = sx + 20; bx1 = 1640
    c.rect(bx0, cy - 110, bx1, cy + 110, outline=(160, 120, 80), width=6, r=10)
    c.text((bx0 + bx1) / 2, cy, '风箱', 'bold', 30, INK, 'mm')
    vel = -math.sin(a)
    if vel > 0.2:
        for k in range(3):
            c.arrow(bx1 + 10, cy - 30 + k * 30, bx1 + 10 + 80 * vel, cy - 30 + k * 30, FIELD, 4, 12)
        c.text(bx1 + 60, cy + 90, '鼓风', 'sans', 24, FIELD, 'mm')
    for k in range(3): flame(c, 1790, 760 - k * 0, 1.0 + 0.6 * max(0, vel), t + k)
    c.text(1790, 800, '炉', 'sans', 26, MUTED, 'mm')
    # trace
    gx0, gx1, gy = 820, 1640, 860
    c.line([(gx0, gy - 60), (gx0, gy + 60)], LINE, 2)
    pts = []
    for k in range(120):
        tt = t - (119 - k) / 30
        if tt < 0: continue
        aa = tt * 1.6
        ppx = cx + r * math.cos(aa); ppy = cy + r * math.sin(aa)
        ss = ppx + math.sqrt(max(0, L * L - (ppy - cy) ** 2))
        pts.append((gx0 + k / 119 * (gx1 - gx0), gy - (ss - (cx + L)) / r * 50))
    if len(pts) > 1: c.line(pts, COPPER, 4)
    c.text(gx0 - 14, gy, '推拉', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 7, '水轮一直朝一个方向转'),
                (7.2, 14, '轮轴上装一个偏心的销子，再接一根连杆'),
                (14.2, 22, '销子转一圈，连杆就把风箱推一次、拉一次：转动变成了推拉')])

def b4_blast(c, t, i):
    corner_tag(c, 'B4 · 鼓风的作用')
    c.text(60, 96, '风吹得越猛，炉子越热', 'serif', 40, INK)
    rows = [('自然通风', 0.45, MUTED), ('人力皮囊', 0.7, FIELD), ('水排', 0.95, COPPER)]
    for k, (lab, v, col) in enumerate(rows):
        f = fade(t, 1 + k * 2.5, 3 + k * 2.5)
        y = 330 + k * 150
        c.text(200, y, lab, 'bold', 32, INK, 'lm')
        c.rect(420, y - 24, 1500, y + 24, fill=LINE, r=24)
        c.rect(420, y - 24, 420 + 1080 * v * f, y + 24, fill=col, r=24)
    X = lambda T: 420 + (T - 600) / 800 * 1080 / 0.95 * 0.95
    for T, lab in [(1084, '铜熔化 1084 ℃'), (1147, '生铁熔化 约 1150 ℃')]:
        a = fade(t, 9, 10)
        if a <= 0: continue
        x = 420 + (T - 400) / (1300 - 400) * 1080
        c.line([(x, 250), (x, 720)], mix(BG, SPARK, a), 3)
        c.text(x, 230 if T < 1100 else 760, lab, 'sans', 24, mix(BG, SPARK, a), 'mm')
    c.text(1500, 780, '炉温（示意）→', 'sans', 24, MUTED, 'rm')
    a = fade(t, 12, 13)
    c.text(200, 860, '氧气送得越多，木炭烧得越快，放热越集中', 'sans', 30, mix(BG, INK, a), 'lm')
    c.text(200, 910, '水排不知疲倦：一座炉子日夜鼓风，「用力少，见功多」', 'sans', 30, mix(BG, COPPER, a), 'lm')
    caps(c, t, [(0, 8, '同样的木炭，鼓风越猛，炉温越高'),
                (8.2, 14, '炼铜、炼铁都要过一千度：靠人拉风箱，又累又不稳'),
                (14.2, 20, '东汉杜诗用水排鼓风：河水替人干活，炉火日夜不停')])

# ---------------------------------------------------------------- E18 炼铁
def e18_reduce(c, t, i):
    corner_tag(c, '第 18 集 · 高炉里发生了什么')
    c.text(60, 96, '铁矿石其实就是「铁锈」', 'serif', 40, INK)
    fx0, fx1, fy0, fy1 = 520, 980, 200, 940
    c.poly([(fx0 - 20, fy0), (fx1 + 20, fy0), (fx1 + 100, fy1), (fx0 - 100, fy1)], (90, 70, 60))
    c.poly([(fx0 + 20, fy0 + 10), (fx1 - 20, fy0 + 10), (fx1 + 60, fy1 - 20), (fx0 - 60, fy1 - 20)], (46, 34, 30))
    sh = (t * 30) % 60
    R = random.Random(18)
    for k in range(80):
        y = R.uniform(fy0 + 30, fy1 - 160) + sh
        if y > fy1 - 160: y -= 560
        w = (y - fy0) / (fy1 - fy0)
        x = R.uniform(fx0 + 10 - 60 * w, fx1 - 10 + 60 * w)
        kind = k % 3
        if kind == 0:
            col = mix((150, 60, 40), IRON, fade(y, 400, 750))
        elif kind == 1:
            col = CHAR
        else:
            col = (210, 206, 196)
        c.rect(x - 14, y - 10, x + 14, y + 10, fill=col, r=5)
    melt = fade(t, 6, 10)
    c.rect(fx0 - 80, fy1 - 140, fx1 + 80, fy1 - 90, fill=mix(BG, (200, 190, 150), 0.9 * melt))
    c.rect(fx0 - 90, fy1 - 90, fx1 + 90, fy1 - 22, fill=mix(BG, mix(FIRE, SPARK, 0.5), melt))
    if melt > 0.5:
        c.text(fx1 + 130, fy1 - 115, '炉渣', 'sans', 24, INK, 'lm')
        c.text(fx1 + 130, fy1 - 56, '铁水', 'bold', 26, SPARK, 'lm')
    for k in range(3):
        ph = (t * 1.5 + k / 3) % 1
        c.arrow(fx0 - 300 + ph * 160, fy1 - 200, fx0 - 280 + ph * 160 + 40, fy1 - 200, FIELD, 4, 12)
    c.text(fx0 - 200, fy1 - 240, '鼓风（水排）', 'sans', 24, FIELD, 'mm')
    for k in range(5):
        ph = (t * 0.5 + k / 5) % 1
        c.text(fx0 + 60 + k * 90, fy0 - 10 - ph * 80, 'CO2', 'mono', 20, mix(BG, MUTED, 1 - ph), 'mm')
    leg = [((150, 60, 40), '铁矿石（氧化铁）'), (CHAR, '木炭'), ((210, 206, 196), '石灰石（帮杂质变成炉渣）')]
    for k, (col, s_) in enumerate(leg):
        c.rect(1200, 260 + k * 50, 1230, 284 + k * 50, fill=col, r=4)
        c.text(1250, 272 + k * 50, s_, 'sans', 26, INK, 'lm')
    a = fade(t, 10, 11)
    c.rect(1180, 470, 1860, 900, fill=mix(BG, SHEET, a), r=16)
    c.text(1210, 520, '一氧化碳从下往上走', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(1210, 570, '把氧从氧化铁身上抢走：', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 630, '氧化铁 + 一氧化碳 → 铁 + 二氧化碳', 'mono', 26, mix(BG, COPPER, a), 'lm')
    c.text(1210, 710, '铁一边往下走，一边吸进碳', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 760, '含碳多了，熔点降到约 1150 ℃', 'bold', 26, mix(BG, SPARK, a), 'lm')
    c.text(1210, 810, '于是能熔成铁水，浇进模子里', 'sans', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '矿石、木炭、石灰石一层层从炉顶加进去，鼓风从下面吹进来'),
                (6.2, 12, '木炭烧成一氧化碳，一路往上，把氧化铁变回铁'),
                (12.2, 24, '吸了碳的铁在约 1150 ℃ 熔化：中国很早就能浇铸生铁')])

def e18_carbon(c, t, i):
    corner_tag(c, '第 18 集 · 碳决定软硬')
    c.text(60, 96, '同样是铁，为什么有的软、有的硬、有的脆？', 'serif', 40, INK)
    gx0, gx1, gy0, gy1 = 200, 1100, 220, 820
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2); c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    X = lambda C: gx0 + C / 4.5 * (gx1 - gx0)
    Y = lambda T: gy1 - (T - 1000) / 600 * (gy1 - gy0)
    for C in (0, 1, 2, 3, 4):
        c.text(X(C), gy1 + 30, f'{C}%', 'mono', 22, MUTED, 'mm')
    c.text(gx1, gy1 + 66, '含碳量', 'sans', 24, MUTED, 'rm')
    for T in (1100, 1300, 1500):
        c.text(gx0 - 14, Y(T), f'{T}', 'mono', 22, MUTED, 'rm')
    c.text(gx0, gy0 - 30, '开始熔化的温度（℃，简化示意）', 'sans', 24, MUTED, 'lm')
    f = fade(t, 1, 6)
    pts = []
    for k in range(int(f * 100) + 1):
        C = 4.3 * k / 100
        T = 1538 - (1538 - 1147) * (C / 4.3) ** 0.85
        pts.append((X(C), Y(T)))
    if len(pts) > 1: c.line(pts, COPPER, 6)
    if t > 5:
        c.text(X(0) + 10, Y(1538) - 20, '纯铁 1538 ℃：古代炉子烧不化', 'sans', 24, INK, 'lm')
        c.text(X(4.3) - 10, Y(1147) - 30, '约 4.3%：约 1147 ℃', 'sans', 24, SPARK, 'rm')
    zones = [(0, 0.1, '熟铁', '软，能锻打', MUTED), (0.2, 2.0, '钢', '又硬又韧', FIELD), (2.0, 4.3, '生铁', '硬而脆，能浇铸', COPPER)]
    a = fade(t, 7, 8)
    for k, (c0, c1, n, d, col) in enumerate(zones):
        c.rect(X(c0), gy1 - 40, X(c1), gy1 - 4, fill=mix(BG, col, 0.7 * a))
        c.text((X(c0) + X(c1)) / 2 + (40 if k == 0 else 0), gy1 - 70, n, 'bold', 26, mix(BG, col, a), 'mm')
    # lattice panel
    b = fade(t, 11, 12)
    px = 1250
    c.rect(px, 220, 1860, 820, fill=mix(BG, SHEET, b), r=16)
    for r_ in range(6):
        for q in range(6):
            c.ellipse(px + 90 + q * 85, 300 + r_ * 85, 26, 26, fill=mix(BG, IRON, b))
    nC = int(fade(t, 13, 18) * 10)
    R = random.Random(5)
    for k in range(nC):
        q = R.randint(0, 4); r_ = R.randint(0, 4)
        c.ellipse(px + 132 + q * 85, 342 + r_ * 85, 11, 11, fill=mix(BG, CHAR if False else (30, 30, 30), b), outline=mix(BG, SPARK, b), width=2)
    c.text(px + 305, 780, '碳原子塞进铁原子的空隙，铁层就不好滑动了', 'sans', 22, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 7, '碳越多，铁越容易熔化：纯铁要 1538 ℃，含碳约 4.3% 只要约 1147 ℃'),
                (7.2, 13, '可碳也决定了软硬：熟铁软，钢又硬又韧，生铁硬而脆'),
                (13.2, 22, '碳原子塞进铁的晶格里，挡住铁原子层的滑动 —— 炼钢，就是把碳调到刚好')])

# ---------------------------------------------------------------- 第二季特辑：温度阶梯
LADDER = [(30, '酿酒、酿醋', 'B15', FIELD), (25, '抄纸', '23', FIELD), (100, '煮盐', '20', FIELD),
          (300, '木头开始炭化', '16', MUTED), (900, '烧陶、煅烧石灰', '16 · 24', COPPER),
          (1084, '铜熔化', '17', CU), (1147, '生铁熔化', '18', SPARK), (1250, '烧瓷', 'B16', (230, 230, 220)),
          (1538, '纯铁熔化（古代做不到）', '—', NRED)]

def s2_ladder(c, t, i):
    corner_tag(c, '第二季特辑 · 温度阶梯')
    c.text(60, 110, '第二季：一部往上爬温度的历史', 'serif', 48, INK, 'lm')
    gx, gy0, gy1 = 420, 200, 960
    Y = lambda T: gy1 - T / 1600 * (gy1 - gy0)
    c.rect(gx - 16, gy0, gx + 16, gy1, fill=LINE, r=16)
    lvl = 1600 * fade(t, 1, 20)
    if lvl > 10: c.rect(gx - 12, Y(lvl), gx + 12, gy1 - 4, fill=mix(SPARK, NRED, lvl / 1600), r=12)
    for T in (0, 500, 1000, 1500):
        c.text(gx - 40, Y(T), f'{T} ℃', 'mono', 22, MUTED, 'rm')
    used = []
    for k, (T, lab, ep, col) in enumerate(sorted(LADDER)):
        a = fade(lvl, T - 20, T + 40)
        if a <= 0: continue
        y = Y(T)
        # avoid overlap
        yy = y
        for u in used:
            if abs(yy - u) < 46: yy = u - 46
        used.append(yy)
        c.line([(gx + 16, y), (gx + 70, yy)], mix(BG, col, a), 3)
        c.text(gx + 80, yy, f'{T} ℃', 'mono', 24, mix(BG, col, a), 'lm')
        c.text(gx + 220, yy, lab, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(gx + 220 + c.textw(lab, 'bold', 28) + 20, yy, ep, 'mono', 22, mix(BG, MUTED, a), 'lm')
    b = fade(t, 20, 21)
    c.rect(1240, 300, 1860, 780, fill=mix(BG, SHEET, b), r=16)
    c.text(1270, 360, '每往上爬一级，都要：', 'bold', 30, mix(BG, INK, b), 'lm')
    for k, s_ in enumerate(['更好的燃料：木头 → 木炭', '更强的鼓风：人力 → 水排', '更好的炉窑：露天 → 窑 → 高炉', '能扛住高温的材料：泥 → 瓷土']):
        c.text(1270, 440 + k * 70, s_, 'sans', 28, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 10, '把第二季的每一项技艺，按需要的温度排一排'),
                (10.2, 20, '从三十度的酒缸，到一千一百多度的铁水'),
                (20.2, 28, '火与材料，说到底是一场和温度的较量')], y=1020)

# ---------------------------------------------------------------- 片头片尾
CLIPS = {
 'E17_胆水浸铜': (e17_displace, 22), 'E17_火法炼铜': (e17_smelt, 20),
 'E17_片头': (titles.opening(SER, VOL, S2A, 6, '北宋 · 胆水浸铜 · 沈括《梦溪笔谈》'), 7),
 'E17_片尾': (titles.closing(SER, VOL, S2A, 6, '下集：炼铁之前，先解决鼓风'), 7),
 'B4_曲柄连杆': (b4_crank, 22), 'B4_鼓风的作用': (b4_blast, 20),
 'B4_片头': (titles.opening(BSER, BVOL, SB2, 3, '东汉 · 公元 31 年 · 杜诗'), 7),
 'B4_片尾': (titles.closing(BSER, BVOL, SB2, 3, '下集：第二季高潮 —— 炼铁'), 7),
 'E18_高炉': (e18_reduce, 24), 'E18_碳决定软硬': (e18_carbon, 22),
 'E18_片头': (titles.opening(SER, VOL, S2A, 7, '春秋晚期已有生铁 · 北宋铁产量大增'), 7),
 'E18_片尾': (titles.closing(SER, VOL, S2A, 7, '下集：第二季特辑'), 7),
 'S2_温度阶梯': (s2_ladder, 28),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
