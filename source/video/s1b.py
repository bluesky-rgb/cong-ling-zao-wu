"""第一季续：B14 豆腐点卤、B13 漏刻、E06 水车发电 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles

def caps(c, t, items, y=1010):
    for a0, a1, s_ in items:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0: c.text(960, y, s_, 'bold', 34, mix(BG, INK, al), 'mm')

# ---------------------------------------------------------------- B14 豆腐点卤
RNG = random.Random(14)
PROT = []
for gy in range(2):
    for gx in range(4):
        PROT.append(dict(x=330 + gx * 420 + RNG.uniform(-60, 60), y=380 + gy * 330 + RNG.uniform(-40, 40),
                         th=RNG.uniform(-0.6, 0.6) + (0 if (gx + gy) % 2 else math.pi / 2) * 0.5, ph=RNG.uniform(0, 6)))
WATER = [(RNG.uniform(120, 1800), RNG.uniform(200, 900), RNG.uniform(0, 6)) for _ in range(140)]
NK = 15

def chain_pts(p, u, t, squeeze):
    cx = 960 + (p['x'] - 960) * squeeze
    cy = 545 + (p['y'] - 545) * squeeze
    pts = []
    for k in range(NK):
        a = k / (NK - 1) * 2 * math.pi
        fx, fy = 34 * math.cos(a + p['ph']), 34 * math.sin(a + p['ph'])
        s = (k / (NK - 1) - 0.5) * 300
        w = 16 * math.sin(k * 1.3 + t * 2 + p['ph'])
        ux, uy = math.cos(p['th']), math.sin(p['th'])
        gx, gy = s * ux - w * uy, s * uy + w * ux
        j = 6 * math.sin(t * 1.3 + p['ph'] + k)
        pts.append((cx + fx + (gx - fx) * u + j * (1 - u), cy + fy + (gy - fy) * u + j * (1 - u) * 0.5))
    return pts

def neighbours():
    pairs = []
    for i in range(8):
        if i % 4 < 3: pairs.append((i, i + 1))
        if i < 4: pairs.append((i, i + 4))
    return pairs
PAIRS = neighbours()

def b14_net(c, t, i):
    corner_tag(c, 'B14 · 豆腐点卤')
    c.text(60, 96, '一点卤水，为什么能让豆浆凝固？', 'serif', 40, INK)
    u = fade(t, 6, 10)                       # heat → unfold
    sq = 1 - 0.22 * fade(t, 13, 19)          # network contracts
    # stage label
    st = '生豆浆' if t < 6 else ('煮开' if t < 11 else ('点卤' if t < 18 else '豆腐脑'))
    c.rect(1560, 70, 1860, 130, fill=SHEET, r=10)
    c.text(1710, 100, st, 'serif', 34, COPPER if t >= 11 else INK, 'mm')
    # water molecules
    trapped = fade(t, 18, 20)
    for (x, y, ph) in WATER:
        xx = x + 8 * math.sin(t * 2 + ph) * (1 - trapped * 0.8)
        yy = y + 8 * math.cos(t * 1.7 + ph) * (1 - trapped * 0.8)
        c.ellipse(xx, yy, 5, 5, fill=mix(BG, FIELD, 0.45 + 0.35 * trapped))
    chains = [chain_pts(p, u, t, sq) for p in PROT]
    # bridges
    bridge = []
    for n, (a, b) in enumerate(PAIRS):
        t0 = 11.5 + n * 0.55
        f = fade(t, t0, t0 + 1.2)
        if f <= 0: continue
        pa = min(chains[a], key=lambda q: (q[0] - chains[b][NK // 2][0]) ** 2 + (q[1] - chains[b][NK // 2][1]) ** 2)
        pb = min(chains[b], key=lambda q: (q[0] - pa[0]) ** 2 + (q[1] - pa[1]) ** 2)
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
        sx, sy = -60, my + (n % 3 - 1) * 120
        ix, iy = sx + (mx - sx) * ease(f), sy + (my - sy) * ease(f)
        bridge.append((pa, pb, ix, iy, fade(t, t0 + 1.0, t0 + 1.6)))
    for pa, pb, ix, iy, g in bridge:
        if g > 0:
            c.line([pa, (ix, iy), pb], mix(BG, SPARK, g * 0.9), 4)
    for k, pts in enumerate(chains):
        c.line(pts, COPPER, 7)
        # negative charges on the chain
        for j in (2, 7, 12):
            x, y = pts[j]
            neu = 0.0
            c.ellipse(x, y - 26, 13, 13, fill=SHEET, outline=mix(BG, SBLUE, 0.9), width=2)
            c.text(x, y - 27, '−', 'bold', 22, FIELD, 'mm')
    for pa, pb, ix, iy, g in bridge:
        ion(c, ix, iy, 'Mg', '2+', 24)
    # repulsion arrows in raw soy milk
    rep = fade(t, 1.5, 2.2) * (1 - fade(t, 10, 11))
    if rep > 0:
        for a, b in [(0, 1), (5, 6), (2, 6)]:
            pa, pb = chains[a][NK // 2], chains[b][NK // 2]
            mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
            dx, dy = pb[0] - pa[0], pb[1] - pa[1]; L = math.hypot(dx, dy); dx, dy = dx / L, dy / L
            col = mix(BG, NRED, rep)
            c.arrow(mx - dx * 20, my - dy * 20, mx - dx * 70, my - dy * 70, col, 4, 14)
            c.arrow(mx + dx * 20, my + dy * 20, mx + dx * 70, my + dy * 70, col, 4, 14)
    if trapped > 0:
        c.rect(150, 190, 1770, 920, outline=mix(BG, COPPER, trapped * 0.7), width=3, r=30)
    # legend
    c.ellipse(90, 950, 6, 6, fill=mix(BG, FIELD, 0.7)); c.text(108, 950, '水', 'sans', 24, MUTED, 'lm')
    c.line([(160, 950), (210, 950)], COPPER, 7); c.text(222, 950, '大豆蛋白', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 6, '豆浆里的蛋白质表面带负电，互相排斥，均匀地散在水里'),
                (6.2, 11, '煮开：蛋白质受热展开，露出更多能「抓手」的部位'),
                (11.2, 18, '点卤：镁离子带两份正电，一手拉一条，把蛋白质连起来'),
                (18.2, 24, '连成一张网，把水锁在网眼里 —— 这就是豆腐脑')])

def ion(c, x, y, base, ch, r=22, a=1.0):
    c.ellipse(x, y, r, r, fill=mix(BG, SPARK, a))
    w = c.textw(base, 'bold', r * 0.8)
    c.text(x - 4, y + 2, base, 'bold', int(r * 0.8), BG, 'mm')
    c.text(x - 4 + w / 2 + 1, y - r * 0.35, ch, 'bold', int(r * 0.5), BG, 'lm')

def mini_chain(c, x0, y0, L, wob, t, col=COPPER):
    pts = [(x0 + k / 10 * L, y0 + 10 * math.sin(k * 1.4 + t * 2 + wob)) for k in range(11)]
    c.line(pts, col, 6)
    return pts

def b14_three(c, t, i):
    corner_tag(c, 'B14 · 三种凝固剂')
    c.text(60, 96, '同一锅豆浆，三种「点法」', 'serif', 40, INK)
    P = [(330, '盐卤', '主要成分：氯化镁', ('Mg', '2+'), 0.5), (960, '石膏', '主要成分：硫酸钙', ('Ca', '2+'), 6.5), (1590, '白醋', '主要成分：醋酸', ('H', '+'), 12.5)]
    notes = [['溶得快，凝得快', '要边点边搅，不易点匀', '常用来做「北豆腐」'],
             ['溶得慢，凝得均匀', '豆花细嫩、含水多', '常用来做「南豆腐」'],
             ['把负电中和掉', '豆腐偏散、带酸味', '内酯豆腐也走这条路']]
    for k, (x, name, sub, ion_, t0) in enumerate(P):
        a = fade(t, t0, t0 + 0.6)
        if a <= 0: continue
        c.rect(x - 280, 170, x + 280, 900, fill=mix(BG, SHEET, a), r=18)
        c.text(x, 225, name, 'serif', 48, mix(BG, INK, a), 'mm')
        c.text(x, 280, sub, 'sans', 26, mix(BG, MUTED, a), 'mm')
        g = fade(t, t0 + 1.2, t0 + 3.5)
        gap = 150 - 80 * g
        y1, y2 = 470 - gap / 2, 470 + gap / 2
        p1 = mini_chain(c, x - 200, y1, 400, k, t, mix(BG, COPPER, a))
        p2 = mini_chain(c, x - 200, y2, 400, k + 2, t, mix(BG, COPPER, a))
        for j in (2, 5, 8):
            if k < 2:
                c.text(p1[j][0], p1[j][1] + 24, '−', 'bold', 24, mix(BG, FIELD, a), 'mm')
                c.text(p2[j][0], p2[j][1] - 24, '−', 'bold', 24, mix(BG, FIELD, a), 'mm')
                ix, iy = (p1[j][0] + p2[j][0]) / 2, (p1[j][1] + p2[j][1]) / 2
                fi = fade(t, t0 + 1.0 + j * 0.1, t0 + 2.4)
                if fi > 0:
                    sy = iy - 200 * (1 - fi)
                    ion(c, p1[j][0], sy, ion_[0], ion_[1], 24, fi)
            else:
                fh = fade(t, t0 + 1.0, t0 + 2.4)
                for p, s in ((p1, 1), (p2, -1)):
                    q = p[j]
                    c.text(q[0], q[1] - s * 24, '0' if fh > 0.6 else '−', 'bold', 24,
                           mix(BG, MUTED if fh > 0.6 else FIELD, a), 'mm')
                    if 0 < fh < 0.9:
                        ion(c, q[0] + 30, q[1] - s * (24 + 90 * (1 - fh)), 'H', '+', 17)
        c.text(x, 650, '离子当「桥」连起来' if k < 2 else '不排斥了，自己抱成团', 'bold', 30, mix(BG, COPPER, g), 'mm')
        for j, s_ in enumerate(notes[k]):
            c.text(x, 730 + j * 52, s_, 'sans', 28, mix(BG, INK if j < 2 else MUTED, fade(t, t0 + 2.5 + j * 0.3, t0 + 3.1 + j * 0.3)), 'mm')
    caps(c, t, [(18.3, 22, '豆腐是老是嫩，还要看压掉多少水 —— 我们按实测为准')])

# ---------------------------------------------------------------- B13 漏刻
def vessel(c, x0, y0, x1, y1, level, col=FIELD, wall=MUTED):
    if level < y1 - 6:
        c.rect(x0 + 4, level, x1 - 4, y1 - 4, fill=mix(BG, col, 0.55))
    c.line([(x0, y0), (x0, y1), (x1, y1), (x1, y0)], wall, 6)

def jet(c, x, y, v, col=FIELD, w=7, dirn=1, floor=1000):
    """parabolic stream leaving a side hole with horizontal speed v (px per unit)."""
    if v <= 0.5: return
    pts = []
    for k in range(40):
        s = k / 39 * 1.3
        px, py = x + dirn * v * s, y + 300 * s * s
        if py > floor: break
        pts.append((px, py))
    if len(pts) > 1: c.line(pts, mix(BG, col, 0.85), w)

TD = 18.0
def lev1(t):  # Torricelli: sqrt(h) falls linearly
    s = max(0.0, 1 - min(t, TD) / TD)
    return s * s

def b13_single(c, t, i):
    corner_tag(c, 'B13 · 漏刻')
    c.text(60, 96, '一个壶：水越少，流得越慢', 'serif', 40, INK)
    x0, x1, top, bot = 220, 520, 260, 860
    h = lev1(t)
    lvl = bot - (bot - top - 20) * h
    vessel(c, x0, top, x1, bot, lvl)
    jet(c, x1, bot - 30, 260 * math.sqrt(h) if h > 0.002 else 0, floor=980)
    c.ellipse(x1, bot - 30, 7, 7, fill=INK)
    # marks every 3 s
    for k in range(1, 5):
        tk = k * 3
        if t >= tk:
            y = bot - (bot - top - 20) * lev1(tk)
            c.line([(x0 - 40, y), (x0 - 4, y)], COPPER, 4)
            c.text(x0 - 50, y, f'{tk}秒', 'mono', 20, MUTED, 'rm')
    if t >= 0:
        c.line([(x0 - 40, top + 20), (x0 - 4, top + 20)], COPPER, 4)
        c.text(x0 - 50, top + 20, '0秒', 'mono', 20, MUTED, 'rm')
    c.text((x0 + x1) / 2, top - 40, '水位高 → 压力大 → 流得快', 'sans', 26, MUTED, 'mm')
    # graph
    gx0, gx1, gy0, gy1 = 900, 1780, 220, 760
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2); c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text(gx0 - 14, gy0, '水位', 'sans', 24, MUTED, 'rm'); c.text(gx1, gy1 + 34, '时间', 'sans', 24, MUTED, 'rm')
    pts = [(gx0 + tt / TD * (gx1 - gx0) * 0.92, gy1 - lev1(tt) * (gy1 - gy0 - 20)) for tt in [k * 0.1 for k in range(int(min(t, TD) * 10) + 1)]]
    if len(pts) > 1: c.line(pts, COPPER, 6)
    # straight dashed reference (what a clock would need)
    ra = fade(t, 9, 10)
    if ra > 0:
        for k in range(20):
            if k % 2: continue
            a_, b_ = k / 20, (k + 1) / 20
            c.line([(gx0 + a_ * (gx1 - gx0) * 0.92, gy0 + 20 + a_ * (gy1 - gy0 - 20)), (gx0 + b_ * (gx1 - gx0) * 0.92, gy0 + 20 + b_ * (gy1 - gy0 - 20))], mix(BG, FIELD, ra), 4)
        c.text(gx1 - 10, gy0 + 40, '想要的：一条直线（每段时间流掉一样多）', 'sans', 24, mix(BG, FIELD, ra), 'rm')
    fa = fade(t, 4, 5)
    c.rect(gx0 + 40, 820, gx1, 930, fill=mix(BG, SHEET, fa), r=12)
    c.text(gx0 + 70, 875, '流速 ≈ √(2 × g × 水深)', 'mono', 36, mix(BG, INK, fa), 'lm')
    caps(c, t, [(0, 4, '瓶底开一个小孔，水深的时候喷得远'),
                (4.2, 9, '流速和水深的平方根有关：水越浅，流得越慢'),
                (9.2, 15, '每三秒画一条线：线越来越密'),
                (15.2, 22, '一个壶计时，刻度只能画得不均匀，而且越到后面越不准')])

def b13_multi(c, t, i):
    corner_tag(c, 'B13 · 多级漏壶')
    c.text(60, 96, '让水位不变：溢流', 'serif', 40, INK)
    T = (150, 215, 400, 355)
    ht = 1 - 0.55 * min(t, 24) / 24
    vessel(c, *T, T[3] - (T[3] - T[1] - 20) * ht)
    c.text((T[0] + T[2]) / 2, T[1] - 28, '供水壶', 'sans', 26, MUTED, 'mm')
    jet(c, T[2], T[3] - 16, 70 * math.sqrt(ht), floor=410)
    c.ellipse(T[2], T[3] - 16, 6, 6, fill=INK)
    M = (430, 400, 650, 540)
    lm = M[1] + 26
    vessel(c, *M, lm)
    c.text((M[0] + M[2]) / 2, M[3] + 34, '平水壶', 'serif', 30, COPPER, 'mm')
    # overflow on the left wall → basin
    of = fade(t, 0.5, 1.0)
    c.line([(M[0], lm + 6), (330, lm + 6), (330, 820)], MUTED, 10)
    if of > 0:
        c.line([(M[0] - 4, lm + 6), (334, lm + 6), (334, 820 + 50 * of)], mix(BG, FIELD, 0.8 * of), 5)
    c.line([(270, 830), (270, 900), (390, 900), (390, 830)], MUTED, 5)
    c.rect(274, 896 - 50 * min(1, t / 24), 386, 896, fill=mix(BG, FIELD, 0.5))
    c.text(330, 935, '多余的水流走', 'sans', 22, MUTED, 'mm')
    hl = fade(t, 3, 4) * (1 - fade(t, 9.5, 10))
    if hl > 0:
        c.line([(M[0], lm), (M[2] + 260, lm)], mix(BG, SPARK, hl), 3)
        c.text(M[2] + 270, lm, '水位始终在这里', 'bold', 26, mix(BG, SPARK, hl), 'lm')
    # spout → receiver
    c.line([(M[2], M[3] - 14), (750, M[3] - 14)], MUTED, 6)
    sv = fade(t, 0.5, 1.0)
    R = (680, 620, 820, 930)
    rise = max(0.0, min(1.0, (t - 0.5) / 23.5))
    lr = R[3] - 4 - 240 * rise
    if sv > 0:
        c.line([(750, M[3] - 10), (750, lr)], mix(BG, FIELD, 0.8 * sv), 4)
    vessel(c, *R, lr)
    c.rect(700, lr - 18, 736, lr + 4, fill=SHEET, outline=INK, width=2, r=4)
    c.line([(718, lr - 18), (718, lr - 200)], SPARK, 6)
    for k in range(6):
        y = R[3] - 4 - 18 - 200 - k * 48 + 48 * 5 - 240 + 240
    c.text(732, lr - 196, '箭尺', 'bold', 24, SPARK, 'lm')
    c.text(R[2] + 16, 880, '受水壶', 'sans', 26, MUTED, 'lm')
    # graph
    gx0, gx1, gy0, gy1 = 1080, 1800, 230, 700
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2); c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text(gx1, gy1 + 34, '时间', 'sans', 24, MUTED, 'rm')
    n = int(min(t, 24) * 8)
    if n > 1:
        X = lambda k: gx0 + (k / 8) / 24 * (gx1 - gx0)
        c.line([(X(k), gy1 - 120 - (1 - 0.55 * (k / 8) / 24) * 200) for k in range(n + 1)], MUTED, 4)
        c.line([(X(k), gy1 - 360) for k in range(n + 1)], COPPER, 5)
        c.line([(X(k), gy1 - 420 * max(0, min(1, (k / 8 - 0.5) / 23.5))) for k in range(n + 1)], SPARK, 6)
    lg = [(MUTED, '供水壶水位：在下降'), (COPPER, '平水壶水位：不变'), (SPARK, '箭尺高度：匀速上升')]
    for k, (col, s_) in enumerate(lg):
        c.line([(gx0 + 20, 790 + k * 46), (gx0 + 70, 790 + k * 46)], col, 6)
        c.text(gx0 + 84, 790 + k * 46, s_, 'sans', 26, INK, 'lm')
    caps(c, t, [(0, 4, '最上面的壶水位在降，流出的速度也在变'),
                (4.2, 10, '中间的壶开一个溢流口：多出来的水流走，水位始终不变'),
                (10.2, 17, '水位不变 → 流速不变 → 箭尺匀速上升，刻度可以等距'),
                (17.2, 24, '1030 年，北宋燕肃的「莲花漏」就用了这个办法')])

# ---------------------------------------------------------------- E06 水车发电
def wheel(c, cx, cy, r, a, col=COPPER, n=10):
    c.ellipse(cx, cy, r, r, outline=col, width=6)
    c.ellipse(cx, cy, 16, 16, fill=col)
    for k in range(n):
        b = a + k * 2 * math.pi / n
        x, y = cx + r * math.cos(b), cy + r * math.sin(b)
        c.line([(cx, cy), (x, y)], mix(BG, col, 0.6), 3)
        px, py = math.cos(b), math.sin(b)
        c.poly([(x, y), (x + 40 * px, y + 40 * py), (x + 40 * px - 18 * py, y + 40 * py + 18 * px), (x - 18 * py, y + 18 * px)], col)

def e06_power(c, t, i):
    corner_tag(c, '第 06 集 · 水的功率')
    c.text(60, 96, '流量和落差，哪个更重要？', 'serif', 40, INK)
    phases = [(0, 6, 1, 1, '基准'), (6, 11, 2, 1, '流量 × 2'), (11, 16, 1, 2, '落差 × 2'), (16, 22, 2, 2, '都 × 2')]
    def at(tt):
        for k, (a0, a1, q, h, _) in enumerate(phases):
            if a0 <= tt < a1:
                if k == 0: return q, h
                p = phases[k - 1]; f = fade(tt, a0, a0 + 1.2)
                return p[2] + (q - p[2]) * f, p[3] + (h - p[3]) * f
        return phases[-1][2], phases[-1][3]
    Q, Hh = at(t)
    name = [p[4] for p in phases if p[0] <= t < p[1]] or [phases[-1][4]]
    wx, wy, wr = 560, 770, 130
    spout_y = wy - wr - 80 - 170 * (Hh - 1) - 130
    # channel
    c.rect(150, spout_y - 40, 520, spout_y, fill=mix(BG, FIELD, 0.5))
    c.line([(150, spout_y - 50), (150, spout_y), (520, spout_y)], MUTED, 6)
    # stream
    w = 14 * Q
    for k in range(int(w)):
        x = 515 - k * 1.0
        c.line([(x, spout_y - 2), (x + 30, spout_y + 40), (wx - wr * 0.2 - k * 0.5, wy - wr)], mix(BG, FIELD, 0.75), 2)
    a = t * 1.2 * math.sqrt(Q * Hh)
    wheel(c, wx, wy, wr, a)
    # height dimension
    c.line([(110, spout_y), (110, wy - wr)], SPARK, 3)
    c.arrow(110, (spout_y + wy - wr) / 2, 110, spout_y + 4, SPARK, 3, 12)
    c.arrow(110, (spout_y + wy - wr) / 2, 110, wy - wr - 4, SPARK, 3, 12)
    c.text(126, (spout_y + wy - wr) / 2, '落差', 'bold', 28, SPARK, 'lm')
    c.text(330, spout_y - 64, f'流量', 'bold', 28, FIELD, 'mm')
    # formula + bar
    fx = 960
    c.rect(fx, 220, 1840, 340, fill=SHEET, r=14)
    c.text(fx + 440, 280, '功率 ≈ 流量 × 落差 × 9.8 × 效率', 'serif', 42, INK, 'mm')
    c.text(fx, 410, f'现在：{name[0]}', 'serif', 40, COPPER)
    rows = [('流量', Q / 2, FIELD), ('落差', Hh / 2, SPARK), ('功率', Q * Hh / 4, COPPER)]
    for k, (lab, v, col) in enumerate(rows):
        y = 520 + k * 110
        c.text(fx, y, lab, 'sans', 30, MUTED, 'lm')
        c.rect(fx + 100, y - 18, fx + 840, y + 18, fill=LINE, r=18)
        c.rect(fx + 100, y - 18, fx + 100 + 740 * v, y + 18, fill=col, r=18)
        c.text(fx + 110 + 740 * v, y, f'× {Q * Hh if lab == "功率" else (Q if lab == "流量" else Hh):.1f}'.replace('.0', ''), 'mono', 24, INK, 'lm')
    ex = fade(t, 17, 18)
    c.text(fx, 880, '例：每秒 1 升水，落差 1 米 → 理论上约 9.8 瓦', 'sans', 30, mix(BG, INK, ex))
    c.text(fx, 930, '小水轮加小电机，实际能拿到多少：待实测', 'sans', 30, mix(BG, MUTED, ex))
    caps(c, t, [(0, 6, '水流冲动水轮：水的能量 = 有多少水 × 落下多高'),
                (6.2, 11, '水量翻一倍，功率翻一倍'),
                (11.2, 16, '落差翻一倍，功率也翻一倍 —— 两个一样重要'),
                (16.2, 22, '所以古人修水车，既要引足水，也要筑坝、抬高水位')])

def gear(c, cx, cy, r, teeth, a, col):
    pts = []
    for k in range(teeth * 4):
        b = a + k * 2 * math.pi / (teeth * 4)
        rr = r + (12 if k % 4 in (1, 2) else -6)
        pts.append((cx + rr * math.cos(b), cy + rr * math.sin(b)))
    c.poly(pts, col)
    c.ellipse(cx, cy, r * 0.55, r * 0.55, fill=BG)
    c.ellipse(cx, cy, 14, 14, fill=col)
    c.line([(cx, cy), (cx + r * 0.5 * math.cos(a), cy + r * 0.5 * math.sin(a))], col, 6)

def e06_gear(c, t, i):
    corner_tag(c, '第 06 集 · 齿轮增速')
    c.text(60, 96, '水车力气大，可转得太慢', 'serif', 40, INK)
    geared = fade(t, 7, 8.5)
    w = 0.9  # rad/s of water wheel
    a = t * w
    wheel(c, 360, 560, 200, a, mix(BG, FIELD, 0.9), 12)
    c.text(360, 830, '水轮', 'sans', 28, MUTED, 'mm')
    # big gear on same axle (drawn to the right)
    if geared > 0:
        R1, n1, R2, n2 = 180, 36, 30, 6
        gx, gy = 830, 560
        gear(c, gx, gy, R1 * geared + 1, n1, a, mix(BG, COPPER, geared))
        gear(c, gx + R1 + R2 + 6, gy, R2, n2, -a * 6 + 0.3, mix(BG, SPARK, geared))
        c.line([(360, 560), (gx, gy)], MUTED, 8)
        gen_x = gx + R1 + R2 + 6
        c.text(gx, gy + R1 + 50, '大齿轮 36 齿', 'sans', 26, mix(BG, MUTED, geared), 'mm')
        c.text(gen_x - 20, gy + 130, '小齿轮 6 齿', 'sans', 26, mix(BG, MUTED, geared), 'lm')
    else:
        gen_x = 760
        c.line([(360, 560), (gen_x, 560)], MUTED, 8)
    # generator box
    gb = gen_x + (60 if geared > 0 else 0)
    spd = w * (1 + 5 * geared)
    c.rect(gb + 20, 500, gb + 200, 620, fill=SHEET, outline=COPPER, width=3, r=12)
    c.text(gb + 110, 540, '发电机', 'bold', 28, INK, 'mm')
    ang = t * spd
    c.line([(gb + 110, 585), (gb + 110 + 24 * math.cos(ang), 585 + 24 * math.sin(ang))], COPPER, 5)
    # meters
    mx = 1400
    rpm_w = 9; rpm_g = rpm_w * (1 + 5 * geared)
    c.text(mx, 300, '每分钟转数（示意）', 'sans', 26, MUTED)
    for k, (lab, v, col) in enumerate([('水轮', rpm_w, FIELD), ('发电机', rpm_g, SPARK)]):
        y = 380 + k * 90
        c.text(mx, y, lab, 'sans', 28, INK, 'lm')
        c.rect(mx + 120, y - 16, mx + 460, y + 16, fill=LINE, r=16)
        c.rect(mx + 120, y - 16, mx + 120 + 340 * v / 54, y + 16, fill=col, r=16)
        c.text(mx + 470, y, f'{v:.0f}', 'mono', 26, INK, 'lm')
    c.text(mx, 600, '电压', 'sans', 28, INK, 'lm')
    c.rect(mx + 120, 584, mx + 460, 616, fill=LINE, r=16)
    vv = (1 + 5 * geared) / 6
    c.rect(mx + 120, 584, mx + 120 + 340 * vv, 616, fill=COPPER, r=16)
    c.text(mx, 680, '电压 ∝ 转速', 'mono', 34, COPPER)
    caps(c, t, [(0, 7, '水轮直接连发电机：一分钟才转几圈，电压很低'),
                (7.2, 12.5, '大齿轮带小齿轮：36 齿对 6 齿，转速提高 6 倍'),
                (12.7, 18, '代价是要更大的力 —— 水车正好力气大、转得慢')])

# ---------------------------------------------------------------- 片头片尾
SB = [('B1', '指南鱼'), ('B14', '豆腐点卤'), ('B13', '漏刻'), ('B2', '卓筒井')]
VOL2 = [('06', '水车发电'), ('07', '风车发电'), ('08', '畜力与人力'), ('09', '重力发电'), ('10', '蒸汽发电')]
BSER, BVOL = '从零造物 · 古法解密', '第八卷 · 古人是怎么做到的'

CLIPS = {
 'B14_成网': (b14_net, 24), 'B14_三种凝固剂': (b14_three, 22),
 'B14_片头': (titles.opening(BSER, BVOL, SB, 1, '相传西汉 · 可靠记载始于五代宋初'), 7),
 'B14_片尾': (titles.closing(BSER, BVOL, SB, 1, '下集：没有钟表，古人怎么把一天分得很准？'), 7),
 'B13_单壶': (b13_single, 22), 'B13_多级漏壶': (b13_multi, 24),
 'B13_片头': (titles.opening(BSER, BVOL, SB, 2, '西汉已有漏壶 · 北宋 1030 年 莲花漏'), 7),
 'B13_片尾': (titles.closing(BSER, BVOL, SB, 2, '下集：回到 A 线，让河水替我们发电'), 7),
 'E06_功率': (e06_power, 22), 'E06_齿轮增速': (e06_gear, 18),
 'E06_片头': (titles.opening('从零造物', '第二卷 · 能量从哪来', VOL2, 0, '北宋 · 约公元 1090 年 · 一条河边'), 7),
 'E06_片尾': (titles.closing('从零造物', '第二卷 · 能量从哪来', VOL2, 0, '下集：没有河的地方，让风来摇'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
