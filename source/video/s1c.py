"""第一季收尾：B2 卓筒井、E11 果蔬电池、第一季特辑 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, SB, BSER, BVOL, vessel

SOIL = (92, 74, 58)
ROCK1 = (64, 70, 74)
ROCK2 = (78, 84, 88)

# ---------------------------------------------------------------- B2 卓筒井
def b2_drill(c, t, i):
    corner_tag(c, 'B2 · 卓筒井')
    c.text(60, 96, '没有钢铁钻机，怎么打出深井？', 'serif', 40, INK)
    G = 300                       # ground level
    HX = 1100                     # hole x
    FW0, FW1 = 430, 500           # fresh-water layer
    BR0, BR1 = 860, 930           # brine layer
    layers = [(G, 380, SOIL, '泥土'), (380, FW0, ROCK1, '岩层'), (FW0, FW1, mix(ROCK1, FIELD, 0.45), '含淡水的砂层'),
              (FW1, 690, ROCK2, '岩层'), (690, BR0, ROCK1, '岩层'), (BR0, BR1, mix(ROCK1, SPARK, 0.35), '卤水层'), (BR1, 1000, ROCK2, '')]
    for y0, y1, col, lab in layers:
        c.rect(700, y0, 1860, y1, fill=mix(BG, col, 0.75))
        if lab: c.text(1840, (y0 + y1) / 2, lab, 'sans', 24, INK if '水' in lab else MUTED, 'rm')
    depth = G + (BR0 + 20 - G) * min(1, t / 20) ** 0.9
    c.rect(HX - 26, G, HX + 26, depth, fill=BG)
    # treadle lever (碓板) at the surface
    ph = (t * 1.4) % 1
    lift = math.sin(ph * math.pi) if t < 20 else 0
    pv = (900, G - 40)
    ang = -0.22 * lift + 0.08
    L1, L2 = 220, 200
    a_end = (pv[0] + L1 * math.cos(ang), pv[1] + L1 * math.sin(ang))
    b_end = (pv[0] - L2 * math.cos(ang), pv[1] - L2 * math.sin(ang))
    c.poly([(pv[0] - 18, G), (pv[0] + 18, G), pv], MUTED)
    c.line([b_end, a_end], mix(BG, COPPER, 0.8), 12)
    c.text(b_end[0] - 10, b_end[1] - 40, '人踩碓板', 'sans', 24, MUTED, 'mm')
    # rope from lever tip over pulley to bit
    bit_y = depth - 70 * lift - 6
    c.line([(a_end[0], a_end[1]), (HX, a_end[1] - 40), (HX, bit_y - 60)], INK, 3)
    c.ellipse(HX, a_end[1] - 40, 10, 10, outline=INK, width=3)
    c.rect(HX - 20, bit_y - 60, HX + 20, bit_y - 10, fill=MUTED, r=4)
    c.poly([(HX - 22, bit_y - 10), (HX + 22, bit_y - 10), (HX, bit_y + 8)], INK)
    if lift < 0.1 and t < 20:
        for k in range(5):
            c.ellipse(HX - 30 + k * 15, depth - 8 - (k % 2) * 6, 3, 3, fill=SOIL)
    # fresh water seeping (8–14) and casing (14+)
    cas = fade(t, 13.5, 16)
    if t > 7 and depth > FW1:
        f = fade(t, 7.5, 8.5) * (1 - cas)
        if f > 0:
            for k, s in enumerate((-1, 1)):
                for j in range(2):
                    y = FW0 + 20 + j * 30
                    c.arrow(HX + s * 90, y, HX + s * 32, y, mix(BG, FIELD, f), 4, 12)
            c.rect(HX - 24, FW1, HX + 24, depth, fill=mix(BG, FIELD, 0.35 * f))
    if cas > 0:
        bot = G + (min(depth, BR0) - G) * cas
        for s in (-1, 1):
            c.line([(HX + s * 24, G - 20), (HX + s * 24, bot)], mix(BG, (170, 190, 120), cas), 6)
        for y in range(G + 40, int(bot), 60):
            c.line([(HX - 24, y), (HX + 24, y)], mix(BG, (170, 190, 120), 0.6 * cas), 2)
        c.text(HX + 60, 600, '去节的大竹子', 'bold', 26, mix(BG, (190, 210, 140), cas), 'lm')
        c.text(HX + 60, 636, '首尾相接作井壁', 'sans', 24, mix(BG, INK, cas), 'lm')
        if t > 16:
            for k, s in enumerate((-1, 1)):
                y = FW0 + 35
                c.arrow(HX + s * 90, y, HX + s * 34, y, mix(BG, FIELD, 0.6), 4, 12)
                c.line([(HX + s * 40, y - 14), (HX + s * 52, y + 14)], NRED, 4)
    br = fade(t, 20.5, 22.5)
    if br > 0:
        top = BR0 - (BR0 - 560) * br
        c.rect(HX - 20, top, HX + 20, BR0 + 10, fill=mix(BG, SPARK, 0.5))
        c.text(HX - 50, top, '咸泉自上', 'serif', 32, mix(BG, SPARK, br), 'rm')
    # depth readout
    c.rect(120, 380, 560, 520, fill=SHEET, r=14)
    c.text(150, 410, '井口', 'sans', 26, MUTED, 'lm'); c.text(250, 410, '约一个碗大', 'bold', 28, INK, 'lm')
    c.text(150, 470, '井深', 'sans', 26, MUTED, 'lm'); c.text(250, 470, '深者数十丈', 'bold', 28, INK, 'lm')
    c.text(120, 560, '苏轼《蜀盐说》：', 'sans', 24, MUTED)
    c.text(120, 600, '「用圜刃凿山……', 'serif', 30, INK)
    c.text(120, 644, '深者至数十丈」', 'serif', 30, INK)
    caps(c, t, [(0, 7.5, '踩下碓板，铁钻头被提起；松开，它砸下去：一下一下冲碎岩石'),
                (7.7, 13.5, '打穿含水的砂层，淡水从四周渗进来，卤水就被冲淡了'),
                (13.7, 20.3, '把打通竹节的大竹子一节节接起来插下去：挡住淡水，也撑住井壁'),
                (20.5, 24, '打到卤水层，地下的压力把卤水顶上来')])

def b2_valve(c, t, i):
    corner_tag(c, 'B2 · 汲卤筒')
    c.text(60, 96, '一根竹筒，怎么把卤水提上来？', 'serif', 40, INK)
    WL = 600
    c.rect(200, WL, 1000, 980, fill=mix(BG, SPARK, 0.28))
    c.line([(200, WL), (1000, WL)], mix(BG, SPARK, 0.7), 3)
    c.text(980, WL + 30, '井里的卤水', 'sans', 26, MUTED, 'rm')
    cyc = (t % 9) / 9
    YU, YD = 470, 880
    if cyc < 0.45:
        y = YU + (YD - YU) * ease(cyc / 0.45); going = 'down'
    elif cyc < 0.55:
        y = YD; going = 'hold'
    else:
        y = YD - (YD - YU) * ease((cyc - 0.55) / 0.45); going = 'up'
    x0, x1, L = 520, 640, 280
    top, bot = y - L, y
    if going in ('down', 'hold'):
        lvl = max(WL, top + 16)
        if bot - 6 > lvl: c.rect(x0 + 6, lvl, x1 - 6, bot - 6, fill=mix(BG, SPARK, 0.6))
    else:
        lvl = max(top + 16, bot - (YD - WL))
        c.rect(x0 + 6, lvl, x1 - 6, bot - 6, fill=mix(BG, SPARK, 0.6))
    c.line([(x0, top), (x0, bot)], (170, 190, 120), 8)
    c.line([(x1, top), (x1, bot)], (170, 190, 120), 8)
    c.line([((x0 + x1) / 2, 150), ((x0 + x1) / 2, top)], INK, 3)
    opened = going == 'down' and bot > WL
    if opened:
        c.line([(x0 + 4, bot), (x0 + 30, bot - 50)], COPPER, 8)
        c.line([(x1 - 4, bot), (x1 - 30, bot - 50)], COPPER, 8)
        for k in range(3):
            xx = x0 + 30 + k * 30
            c.arrow(xx, bot + 60, xx, bot + 10, mix(BG, FIELD, 0.9), 4, 12)
        st, col = '往下放：外面的水压把皮阀顶开，卤水涌进筒里', FIELD
    else:
        c.line([(x0 + 4, bot), (x1 - 4, bot)], COPPER, 8)
        if going == 'up':
            for k in range(3):
                xx = x0 + 30 + k * 30
                c.arrow(xx, bot - 70, xx, bot - 16, mix(BG, NRED, 0.9), 4, 12)
        st, col = ('往上提：筒里卤水的重量把皮阀压紧，一滴不漏', NRED) if going == 'up' else ('', INK)
    c.text(x1 + 20, bot - 4, '← 熟皮做的阀', 'sans', 24, COPPER, 'lm')
    if t > 9:
        a = fade(t, 9, 10)
        cx0, cx1 = 1240, 1340
        c.text(1290, 250, '对照：没有阀', 'bold', 30, mix(BG, INK, a), 'mm')
        yb = y; yt = y - L
        if going != 'up' and yb > WL:
            c.rect(cx0 + 4, max(WL, yt), cx1 - 4, yb, fill=mix(BG, SPARK, 0.5 * a))
        c.line([(cx0, yt), (cx0, yb)], mix(BG, MUTED, a), 6)
        c.line([(cx1, yt), (cx1, yb)], mix(BG, MUTED, a), 6)
        if going == 'up':
            c.text(1290, yb + 40, '提起来就漏光', 'sans', 26, mix(BG, NRED, a), 'mm')
    c.rect(1120, 800, 1860, 930, fill=SHEET, r=14)
    c.text(1150, 842, '苏轼记载：筒底「悬熟皮数寸」', 'sans', 28, INK, 'lm')
    c.text(1150, 890, '「气自呼吸而启闭之，一筒致水数斗」', 'serif', 28, COPPER, 'lm')
    if st:
        c.text(960, 1020, st, 'bold', 34, col, 'mm')

# ---------------------------------------------------------------- E11 果蔬电池
def battery_icon(c, x, y, name, colr, metals, a=1.0):
    c.rect(x - 110, y - 70, x + 110, y + 70, fill=mix(BG, colr, 0.55 * a), r=40)
    c.text(x, y + 100, name, 'bold', 28, mix(BG, INK, a), 'mm')
    m1, m2 = metals
    c.rect(x - 60, y - 110, x - 46, y + 30, fill=mix(BG, COPPER, a))
    c.rect(x + 46, y - 110, x + 60, y + 30, fill=mix(BG, (170, 176, 182) if m2 == '锌' else (110, 116, 122), a))
    c.text(x - 53, y - 130, '铜', 'sans', 22, mix(BG, COPPER, a), 'mm')
    c.text(x + 53, y - 130, m2, 'sans', 22, mix(BG, INK, a), 'mm')

def e11_metals(c, t, i):
    corner_tag(c, '第 11 集 · 电压看金属')
    c.text(60, 96, '换水果，还是换金属？', 'serif', 40, INK)
    iron = fade(t, 11, 12.5)
    m2 = '铁' if t >= 11.75 else '锌'
    items = [(400, '土豆（对照）', (176, 150, 96)), (960, '萝卜', (200, 200, 190)), (1520, '橘子', (230, 150, 60))]
    for k, (x, n, col) in enumerate(items):
        a = fade(t, 0.3 + k * 0.6, 0.9 + k * 0.6)
        battery_icon(c, x, 420, n, col, ('铜', m2), a)
        # voltage bar
        v = 0.9 * (1 - iron) + 0.5 * iron
        y = 680
        c.text(x - 200, y, '电压', 'sans', 24, mix(BG, MUTED, a), 'lm')
        c.rect(x - 130, y - 14, x + 200, y + 14, fill=mix(BG, LINE, a), r=14)
        c.rect(x - 130, y - 14, x - 130 + 330 * v * a, y + 14, fill=COPPER, r=14)
        cur = [0.35, 0.25, 0.55][k]
        y2 = 740
        c.text(x - 200, y2, '电流', 'sans', 24, mix(BG, MUTED, a), 'lm')
        c.rect(x - 130, y2 - 14, x + 200, y2 + 14, fill=mix(BG, LINE, a), r=14)
        c.rect(x - 130, y2 - 14, x - 130 + 330 * cur * (1 - 0.3 * iron) * a, y2 + 14, fill=FIELD, r=14)
    lab = '锌 + 铜：每个约 0.9 伏（常见值）' if t < 11.75 else '铁 + 铜：电压明显变低（待实测）'
    c.rect(560, 820, 1360, 890, fill=SHEET, r=12)
    c.text(960, 855, lab, 'bold', 32, COPPER if t < 11.75 else SPARK, 'mm')
    c.text(960, 925, '电流条的长短只是示意，以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 5.5, '同样插一片铜、一片锌：土豆、萝卜、橘子'),
                (5.7, 11, '电压几乎一样 —— 电压由两种金属决定，果蔬只相当于盐水'),
                (11.2, 17, '把锌换成北宋有的铁：三个一起变低'),
                (17.2, 22, '果蔬影响的是电流：汁水多少、离子多少，决定电子走得顺不顺')])

def e11_resist(c, t, i):
    corner_tag(c, '第 11 集 · 内阻与串联')
    c.text(60, 96, '一个不够亮，怎么办？', 'serif', 40, INK)
    boiled = fade(t, 7, 8.5)
    n = 1 if t < 14 else min(3, 1 + int((t - 14) / 1.5))
    # cells in series
    x0 = 220
    for k in range(n):
        x = x0 + k * 300
        a = fade(t, 14 + (k - 1) * 1.5, 14.6 + (k - 1) * 1.5) if k else 1
        c.rect(x, 330, x + 220, 520, outline=mix(BG, INK, a), width=3, r=20)
        c.text(x + 110, 300, '煮过的土豆' if boiled > 0.5 else '生土豆', 'sans', 24, mix(BG, MUTED, a), 'mm')
        # internal resistor zig-zag, size shrinks when boiled
        amp = 30 * (1 - 0.7 * boiled)
        pts = [(x + 40 + j * 14, 425 + (amp if j % 2 else -amp)) for j in range(11)]
        pts = [(x + 30, 425)] + pts + [(x + 190, 425)]
        c.line(pts, mix(BG, NRED, a), 5)
        c.text(x + 110, 490, '内阻', 'sans', 22, mix(BG, NRED, a), 'mm')
        if k < n - 1:
            c.line([(x + 220, 425), (x + 300, 425)], INK, 4)
    xe = x0 + (n - 1) * 300 + 220
    # LED
    lx, ly = 1500, 425
    V = n * 0.9
    I = (0.1 + 0.9 * boiled)
    lit = max(0, min(1, (V - 1.8) / 0.6)) * I
    c.line([(x0, 425), (x0 - 60, 425), (x0 - 60, 700), (lx, 700), (lx, ly + 60)], INK, 4)
    c.line([(xe, 425), (lx - 120, 425), (lx - 120, ly - 60), (lx, ly - 60)], INK, 4)
    if lit > 0:
        c.ellipse(lx, ly, 60 + 30 * lit, 60 + 30 * lit, fill=mix(BG, NRED, 0.3 * lit))
    c.ellipse(lx, ly, 40, 40, fill=mix(SHEET, NRED, 0.2 + 0.8 * lit), outline=INK, width=3)
    c.text(lx + 70, ly, 'LED', 'mono', 24, MUTED, 'lm')
    # electrons along bottom wire
    nd = int(3 + 20 * I) if V >= 1.8 else int(2 + 3 * I)
    for k in range(nd):
        s = ((t * 0.25 * (0.5 + I) + k / nd) % 1)
        xx = x0 - 60 + s * (lx - x0 + 60)
        c.ellipse(xx, 700, 6, 6, fill=FIELD)
    # meters
    mx = 1180
    c.rect(mx - 20, 780, 1860, 960, fill=SHEET, r=14)
    c.text(mx, 820, f'电压 ≈ {n} × 0.9 = {V:.1f} 伏（锌铜常见值）', 'mono', 28, INK, 'lm')
    c.text(mx, 870, '红色 LED 要约 1.8 伏才开始亮', 'sans', 26, MUTED, 'lm')
    c.text(mx, 920, '亮不亮看电压；亮多少看电流', 'bold', 28, COPPER, 'lm')
    caps(c, t, [(0, 7, '一个土豆：电压不到 1 伏，内阻又大，LED 不亮'),
                (7.2, 14, '把土豆煮 8 分钟：内阻变小，功率可以提高到约 10 倍'),
                (14.2, 19, '串起来：电压一个个相加'),
                (19.2, 24, '超过 LED 的门槛，灯就亮了')])

# ---------------------------------------------------------------- 第一季特辑
S1 = [('E04', '磁生电', 'A'), ('B1', '指南鱼', 'B'), ('E01', '摩擦起电', 'A'), ('E02', '伏打电堆', 'A'), ('B14', '豆腐点卤', 'B'),
      ('E03', '电生磁', 'A'), ('E05', '手摇发电机', 'A'), ('B13', '漏刻', 'B'), ('E06', '水车发电', 'A'), ('B2', '卓筒井', 'B'), ('E11', '果蔬电池', 'A')]
LINKS = [('B1', 'E03', '古人会让铁带磁 → 我们让电生磁'), ('B13', 'E06', '平水壶 → 蓄水池稳压'), ('E02', 'E11', '同一种化学电'), ('B14', 'B2', '都和「盐」有关')]

def s1_recap(c, t, i):
    corner_tag(c, '第一季特辑 · 回顾')
    c.text(60, 120, '第一季：11 集，两条线', 'serif', 52, INK, 'lm')
    pos = {}
    a_eps = [e for e in S1 if e[2] == 'A']; b_eps = [e for e in S1 if e[2] == 'B']
    for row, eps, y, lab, col in ((0, a_eps, 400, 'A 线 · 穿越造物', COPPER), (1, b_eps, 720, 'B 线 · 古法解密', FIELD)):
        c.text(60, y, lab.split(' · ')[0], 'bold', 32, col, 'lm')
        c.text(60, y + 42, lab.split(' · ')[1], 'sans', 24, MUTED, 'lm')
        n = len(eps)
        xs = [400 + k * (1400 / max(1, n - 1)) for k in range(n)]
        c.line([(xs[0], y), (xs[-1], y)], LINE, 4)
        for x, e in zip(xs, eps):
            pos[e[0]] = (x, y)
    # lighting in broadcast order
    for k, (eid, name, line) in enumerate(S1):
        x, y = pos[eid]
        a = fade(t, 1 + k * 1.1, 1.6 + k * 1.1)
        col = COPPER if line == 'A' else FIELD
        c.ellipse(x, y, 40, 40, fill=mix(SHEET, col, a), outline=mix(LINE, col, a), width=3)
        c.text(x, y, eid, 'mono', 20, mix(MUTED, BG, a), 'mm')
        c.text(x, y + 70, name, 'bold', 26, mix(MUTED, INK, a), 'mm')
        c.text(x, y - 66, f'{k + 1:02d}', 'mono', 20, mix(BG, MUTED, a), 'mm')
    la = fade(t, 14, 15)
    for k, (p, q, s_) in enumerate(LINKS):
        f = fade(t, 14 + k * 1.2, 15 + k * 1.2)
        if f <= 0: continue
        (x0, y0), (x1, y1) = pos[p], pos[q]
        if y0 == y1:
            ym = y0 + (110 if y0 > 500 else -100)
            pts = [(x0, y0 + (40 if ym > y0 else -40)), (x0, ym), (x1, ym), (x1, y1 + (40 if ym > y0 else -40))]
        else:
            pts = [(x0, y0 - 40), (x1, y1 + 40)] if y0 > y1 else [(x0, y0 + 40), (x1, y1 - 40)]
        for j in range(len(pts) - 1):
            (ax, ay), (bx, by) = pts[j], pts[j + 1]
            L = math.hypot(bx - ax, by - ay); nseg = max(1, int(L / 24))
            for m in range(0, nseg, 2):
                u0, u1 = m / nseg, min(1, (m + 1) / nseg)
                c.line([(ax + (bx - ax) * u0, ay + (by - ay) * u0), (ax + (bx - ax) * u1, ay + (by - ay) * u1)], mix(BG, SPARK, f), 3)
    caps(c, t, [(1, 13.5, '按播出顺序，一集一集点亮'),
                (14, 19.5, 'A 线和 B 线互相接力：古人做到的，正好是我们下一步的起点'),
                (19.7, 26, '下一季：火与材料 —— 生火、制盐、炼铁、烧炭')], y=1000)
    for k, (p, q, s_) in enumerate(LINKS):
        f = fade(t, 14 + k * 1.2, 15 + k * 1.2)
        if f > 0:
            c.text(1880, 160 + k * 30, s_, 'sans', 24, mix(BG, SPARK, f), 'rm')

# ---------------------------------------------------------------- 片头片尾
VOL1X = titles.VOL1 + [('11', '果蔬电池')]
A1 = ('从零造物', '第一卷 · 电 · 番外')
S1T = [('A', '穿越造物'), ('B', '古法解密'), ('★', '特辑')]
CLIPS = {
 'B2_冲击钻': (b2_drill, 24), 'B2_汲卤筒': (b2_valve, 22),
 'B2_片头': (titles.opening(BSER, BVOL, SB, 3, '北宋 · 庆历年间（1041–1048）· 四川'), 7),
 'B2_片尾': (titles.closing(BSER, BVOL, SB, 3, '下集：回到第一卷，用萝卜和橘子发电'), 7),
 'E11_电压看金属': (e11_metals, 22), 'E11_内阻与串联': (e11_resist, 24),
 'E11_片头': (titles.opening(*A1, VOL1X, 5, '北宋 · 约公元 1090 年 · 可是北宋没有土豆'), 7),
 'E11_片尾': (titles.closing(*A1, VOL1X, 5, '下集：第一季特辑'), 7),
 'S1_回顾': (s1_recap, 26),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
