"""第二季 · 火与材料 第一批：E20 制盐、E15 生火、E16 木炭与制陶 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, vessel

FIRE = (236, 120, 48)
WOOD = (150, 104, 66)
CLAY = (176, 120, 86)

# ---------------------------------------------------------------- E20 制盐
SALT = [(0, 35.5), (20, 36), (40, 36.5), (60, 37.5), (80, 38), (100, 39)]
SUGAR = [(0, 179), (20, 204), (40, 241), (60, 288), (80, 363), (100, 487)]

def e20_solubility(c, t, i):
    corner_tag(c, '第 20 集 · 溶解度')
    c.text(60, 96, '糖能靠降温析出，盐为什么不行？', 'serif', 40, INK)
    gx0, gx1, gy0, gy1 = 220, 1100, 200, 860
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2); c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    X = lambda T: gx0 + T / 100 * (gx1 - gx0)
    Y = lambda g: gy1 - g / 500 * (gy1 - gy0)
    for g in (100, 200, 300, 400, 500):
        c.line([(gx0, Y(g)), (gx1, Y(g))], mix(BG, LINE, 0.5), 1)
        c.text(gx0 - 14, Y(g), str(g), 'mono', 22, MUTED, 'rm')
    for T in (0, 20, 40, 60, 80, 100):
        c.text(X(T), gy1 + 30, f'{T}', 'mono', 22, MUTED, 'mm')
    c.text(gx1, gy1 + 64, '水温（℃）', 'sans', 24, MUTED, 'rm')
    c.text(gx0, gy0 - 30, '100 克水最多溶解（克）', 'sans', 24, MUTED, 'lm')
    def curve(data, f, col, lab):
        n = int(f * 100)
        pts = []
        for k in range(n + 1):
            T = k
            for (a, va), (b, vb) in zip(data, data[1:]):
                if a <= T <= b:
                    v = va + (vb - va) * (T - a) / (b - a); break
            pts.append((X(T), Y(v)))
        if len(pts) > 1:
            c.line(pts, col, 6)
            c.text(pts[-1][0] + 14, pts[-1][1], lab, 'bold', 28, col, 'lm')
    curve(SUGAR, fade(t, 0.5, 4), SPARK, '糖')
    curve(SALT, fade(t, 3, 6.5), FIELD, '盐')
    # cooling comparison
    a = fade(t, 8, 9)
    if a > 0:
        f = fade(t, 9, 13)
        x = 1250
        c.rect(x - 20, 200, 1860, 860, fill=mix(BG, SHEET, a), r=16)
        c.text(x + 10, 250, '100 ℃ 的饱和溶液，冷却到 0 ℃', 'bold', 30, mix(BG, INK, a), 'lm')
        for k, (lab, hot, cold, col) in enumerate([('糖', 487, 179, SPARK), ('盐', 39, 35.5, FIELD)]):
            y = 380 + k * 230
            c.text(x + 10, y, lab, 'serif', 40, mix(BG, col, a), 'lm')
            out = (hot - cold) * f
            c.text(x + 80, y, f'析出 {out:.1f} 克', 'mono', 40, mix(BG, INK, a), 'lm')
            c.rect(x + 80, y + 40, x + 80 + 480, y + 70, fill=mix(BG, LINE, a), r=15)
            c.rect(x + 80, y + 40, x + 80 + 480 * out / 308, y + 70, fill=col, r=15)
        c.text(x + 10, 820, '盐几乎不随温度变化 → 只能把水蒸发掉', 'bold', 28, mix(BG, COPPER, fade(t, 13, 14)), 'lm')
    caps(c, t, [(0, 3, '糖：水越热，溶得越多'),
                (3.2, 8, '盐：从 0 ℃ 到 100 ℃，只多溶了 3.5 克'),
                (8.2, 14, '同样从开水冷到冰水：糖析出 300 多克，盐只析出 3.5 克'),
                (14.2, 20, '所以盐不能像糖那样靠降温结晶，只能煮干或晒干')])

RNG = random.Random(20)
IONS = [(RNG.random(), RNG.random()) for _ in range(30)]
def e20_crystal(c, t, i):
    corner_tag(c, '第 20 集 · 结晶与试卤')
    c.text(60, 96, '水走了，盐留下；卤够不够浓，莲子说了算', 'serif', 40, INK)
    if t < 12:
        # evaporation & lattice
        cx, cy = 700, 560
        c.rect(260, 260, 1140, 900, outline=MUTED, width=4, r=10)
        lvl = 340 + 300 * fade(t, 0.5, 10)
        c.rect(264, lvl, 1136, 896, fill=mix(BG, FIELD, 0.25))
        grow = fade(t, 3, 11)
        n = int(1 + grow * 5.5)
        s = 34
        x0, y0 = cx - n * s / 2, 896 - n * s
        for r in range(n):
            for q in range(n):
                na = (r + q) % 2 == 0
                c.ellipse(x0 + q * s + s / 2, y0 + r * s + s / 2, 13 if na else 16, 13 if na else 16,
                          fill=mix(BG, SPARK if na else (120, 200, 140), 0.9))
        for k in range(26):
            ph = (t * 0.35 + k / 26) % 1
            x = 300 + (k * 97) % 800
            y = lvl - 10 - ph * 500
            if y > 120:
                c.ellipse(x, y, 7, 7, fill=mix(BG, FIELD, 0.8 * (1 - ph)))
        # free ions
        for k in range(int(30 * (1 - grow))):
            fx, fy = IONS[k]
            x = 300 + fx * 780 + 6 * math.sin(t * 2 + k); y = lvl + 20 + fy * (850 - lvl)
            if y < 880:
                c.ellipse(x, y, 8, 8, fill=mix(BG, SPARK if k % 2 else (120, 200, 140), 0.7))
        c.ellipse(1300, 300, 13, 13, fill=SPARK); c.text(1330, 300, '钠离子', 'sans', 26, INK, 'lm')
        c.ellipse(1300, 350, 16, 16, fill=(120, 200, 140)); c.text(1330, 350, '氯离子', 'sans', 26, INK, 'lm')
        c.ellipse(1300, 400, 7, 7, fill=FIELD); c.text(1330, 400, '离开的水分子', 'sans', 26, INK, 'lm')
        c.text(1290, 520, '正负离子一个隔一个', 'bold', 30, mix(BG, COPPER, grow), 'lm')
        c.text(1290, 565, '排成立方体的晶格', 'bold', 30, mix(BG, COPPER, grow), 'lm')
        c.text(1290, 610, '所以盐粒是小方块', 'sans', 28, mix(BG, MUTED, grow), 'lm')
    else:
        u = t - 12
        cups = [('淡卤', 0.0), ('中卤', 0.5), ('浓卤', 1.0)]
        for k, (lab, conc) in enumerate(cups):
            x = 420 + k * 540
            c.rect(x - 160, 330, x + 160, 820, outline=MUTED, width=4, r=10)
            c.rect(x - 156, 380, x + 156, 816, fill=mix(BG, SPARK, 0.12 + 0.3 * conc))
            c.text(x, 870, lab, 'bold', 32, INK, 'mm')
            floats = [conc > 0.25, conc > 0.6, conc > 0.85]
            for j in range(3):
                fl = floats[j]
                yy = 380 + 18 if fl else 800 - 18
                yy = 600 + (yy - 600) * fade(u, 0.5 + j * 0.3, 2.5 + j * 0.3)
                c.ellipse(x - 80 + j * 80, yy, 26, 18, fill=(120, 90, 60), outline=(70, 50, 30), width=2)
            c.text(x, 290, ['莲子全沉', '浮起一部分', '大多浮起'][k], 'sans', 26, mix(BG, MUTED, fade(u, 2.5, 3.2)), 'mm')
        caps(c, t, [(12.2, 18, '卤越浓，密度越大；密度超过莲子，莲子就浮起来'),
                    (18.2, 24, '古人用浮起的个数判断卤水能不能下锅 —— 这就是一支密度计')])
    caps(c, t, [(0, 5, '把盐水晒着：水分子一个个离开'),
                (5.2, 12, '剩下的钠离子、氯离子挤在一起，排成整齐的方块：盐结晶了')])

# ---------------------------------------------------------------- E15 生火
def flame(c, x, y, s, t, a=1.0):
    if a <= 0 or s <= 0: return
    w = 26 * s; h = 70 * s * (1 + 0.08 * math.sin(t * 13))
    c.poly([(x - w, y), (x, y - h), (x + w, y)], mix(BG, FIRE, a))
    c.poly([(x - w * 0.5, y), (x, y - h * 0.6), (x + w * 0.5, y)], mix(BG, SPARK, a))

def e15_triangle(c, t, i):
    corner_tag(c, '第 15 集 · 燃烧三要素')
    c.text(60, 96, '火要三样东西，缺一样就灭', 'serif', 40, INK)
    A, B, C = (560, 260), (260, 780), (860, 780)
    phase = 0 if t < 5 else (1 if t < 10 else (2 if t < 15 else 3))
    sides = [(A, B, '可燃物', 1), (B, C, '温度（燃点）', 2), (C, A, '氧气', 3)]
    for (p, q, lab, ph) in sides:
        off = phase == ph
        col = MUTED if off else COPPER
        c.line([p, q], mix(BG, col, 0.4 if off else 1), 10)
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = mx - 560, my - 600
        L = math.hypot(dx, dy)
        c.text(mx + dx / L * 70, my + dy / L * 60, lab, 'bold', 32, mix(BG, INK, 0.4 if off else 1), 'mm')
    # candle scene on the right
    cx, cy = 1380, 760
    c.rect(cx - 30, cy - 180, cx + 30, cy, fill=(220, 214, 196), r=4)
    c.line([(cx, cy - 180), (cx, cy - 200)], INK, 3)
    lit = 1.0
    if phase == 1: lit = 1 - fade(t, 6, 8)
    if phase == 2: lit = 1 - fade(t, 11, 12.5)
    if phase == 3: lit = 1 - fade(t, 16, 19)
    if phase == 3:
        c.rect(cx - 140, cy - 420, cx + 140, cy + 6, outline=mix(BG, FIELD, fade(t, 15, 15.6)), width=4, r=30)
        c.text(cx, cy - 450, '罩上杯子', 'sans', 26, MUTED, 'mm')
        o2 = 21 * (1 - fade(t, 15.6, 19)) + 16 * fade(t, 15.6, 19)
        c.text(cx + 200, cy - 300, f'杯里氧气约 {o2:.0f}%', 'mono', 26, FIELD, 'lm')
    if phase == 2:
        for k in range(6):
            c.line([(cx - 80 + k * 30, cy - 330 + (t * 400 + k * 40) % 120), (cx - 90 + k * 30, cy - 300 + (t * 400 + k * 40) % 120)], FIELD, 3)
        c.text(cx, cy - 450, '喷水降温', 'sans', 26, MUTED, 'mm')
    if phase == 1:
        c.text(cx, cy - 450, '剪掉烛芯', 'sans', 26, MUTED, 'mm')
    flame(c, cx, cy - 196, 1.0 * lit, t, lit)
    caps(c, t, [(0, 5, '可燃物、氧气、足够的温度：三样都在，火才烧得起来'),
                (5.2, 10, '拿走可燃物：火灭'),
                (10.2, 15, '把温度降到燃点以下：火灭'),
                (15.2, 20, '隔绝氧气：火灭 —— 取火，就是凑齐这三样')])

def e15_three(c, t, i):
    corner_tag(c, '第 15 集 · 三种取火')
    c.text(60, 96, '古人的三种取火法，都是在「凑温度」', 'serif', 40, INK)
    P = [(330, '阳燧', '把阳光聚到一点', 0.3), (960, '火镰', '敲下的铁屑在空气里燃烧', 6.3), (1590, '钻木', '摩擦把功变成热', 12.3)]
    for k, (x, name, sub, t0) in enumerate(P):
        a = fade(t, t0, t0 + 0.6)
        if a <= 0: continue
        c.rect(x - 290, 170, x + 290, 900, fill=mix(BG, SHEET, a), r=18)
        c.text(x, 225, name, 'serif', 48, mix(BG, INK, a), 'mm')
        c.text(x, 280, sub, 'sans', 26, mix(BG, MUTED, a), 'mm')
        u = t - t0
        if k == 0:
            c.arc(x, 680, 200, 120, 20, 160, mix(BG, (200, 180, 120), a), 10)
            fy = 560
            for j in range(-3, 4):
                sx = x + j * 50
                sy = 680 + 120 * math.sqrt(max(0, 1 - (j * 50 / 200) ** 2))
                g = fade(u, 0.5 + abs(j) * 0.1, 1.5 + abs(j) * 0.1)
                if j: c.line([(sx, 330), (sx, sy)], mix(BG, SPARK, 0.6 * a), 3)
                if g > 0 and j:
                    c.line([(sx, sy), (sx + (x - sx) * g, sy + (fy - sy) * g)], mix(BG, SPARK, 0.8 * a), 3)
            heat = fade(u, 2, 4.5)
            c.rect(x - 30, fy - 10, x + 30, fy + 10, fill=mix((140, 120, 90), FIRE, heat))
            if heat > 0.95: flame(c, x, fy - 8, 0.6, t)
            c.text(x, 870, '凹面铜镜：《周礼》「以夫遂取明火于日」', 'sans', 22, mix(BG, MUTED, a), 'mm')
        if k == 1:
            hit = (u * 1.5) % 1
            sx = x - 60 + 100 * ease(min(1, hit * 3))
            c.rect(x + 20, 520, x + 150, 640, fill=mix(BG, (120, 130, 140), a), r=20)
            c.text(x + 85, 670, '火石', 'sans', 24, mix(BG, MUTED, a), 'mm')
            c.rect(sx - 160, 600, sx, 630, fill=mix(BG, (90, 90, 96), a), r=6)
            c.text(sx - 80, 590, '钢火镰', 'sans', 24, mix(BG, MUTED, a), 'mm')
            if hit > 0.3:
                for j in range(9):
                    ang = -0.3 - j * 0.15
                    d = (hit - 0.3) * 400
                    px, py = x + 20 + d * math.cos(ang + math.pi), 600 + d * math.sin(ang + math.pi) + 300 * (hit - 0.3) ** 2
                    c.ellipse(px, py, 5, 5, fill=mix(BG, SPARK, (1 - hit) * a * 1.4))
            c.text(x, 780, '火石很硬，从钢上刮下细小的铁屑', 'sans', 24, mix(BG, INK, a), 'mm')
            c.text(x, 820, '铁屑小、发热快，在空气里直接烧起来', 'sans', 24, mix(BG, INK, a), 'mm')
            c.text(x, 860, '落在火绒上，吹一吹就着', 'sans', 24, mix(BG, INK, a), 'mm')
        if k == 2:
            rot = math.sin(u * 9)
            c.rect(x - 200, 640, x + 200, 690, fill=mix(BG, WOOD, a), r=6)
            c.line([(x + rot * 6, 340), (x, 640)], mix(BG, (190, 150, 100), a), 14)
            temp = 20 + 330 * fade(u, 0.5, 4.5)
            c.ellipse(x, 640, 30, 12, fill=mix(BG, mix((60, 40, 30), FIRE, temp / 350), a))
            c.text(x, 740, f'木粉温度 ≈ {temp:.0f} ℃', 'mono', 30, mix(BG, INK, a), 'mm')
            c.text(x, 790, '木头约 300 ℃ 左右开始燃烧（因材而异）', 'sans', 22, mix(BG, MUTED, a), 'mm')
            c.text(x, 830, '热量会散走：要快、要压紧、木粉要聚成堆', 'sans', 22, mix(BG, MUTED, a), 'mm')
            if temp > 330:
                for j in range(4):
                    c.ellipse(x - 20 + j * 14, 610 - (u * 60 + j * 20) % 80, 8, 8, fill=mix(BG, MUTED, 0.6))
    caps(c, t, [(0, 6, '阳燧：凹面铜镜把阳光聚到一点，把火绒加热到燃点'),
                (6.2, 12, '火镰：钢和火石一碰，刮下的铁屑小到能在空气里自燃'),
                (12.2, 18, '钻木：摩擦把力气变成热，木粉越来越烫，冒烟'),
                (18.2, 24, '三种办法，做的是同一件事：把一小撮火绒加热到燃点')])

# ---------------------------------------------------------------- E16 木炭与制陶
def e16_pyro(c, t, i):
    corner_tag(c, '第 16 集 · 干馏木炭')
    c.text(60, 96, '把木头关进铁罐里烤，会剩下什么？', 'serif', 40, INK)
    T = 20 + 480 * fade(t, 0.5, 16)
    cx, cy = 620, 560
    # fire below
    for k in range(5):
        flame(c, cx - 160 + k * 80, 900, 1.2, t + k)
    c.rect(cx - 220, 380, cx + 220, 800, outline=(160, 160, 166), width=8, r=14)
    c.ellipse(cx, 380, 10, 6, fill=BG)
    char = fade(t, 9, 18)
    for k in range(12):
        x = cx - 180 + (k % 6) * 62; y = 600 + (k // 6) * 90
        col = mix(WOOD, (34, 32, 32), char)
        c.rect(x, y, x + 56, y + 70, fill=col, r=6)
    # outputs at the hole
    if 100 <= T < 260:
        for k in range(6):
            ph = (t * 0.6 + k / 6) % 1
            c.ellipse(cx + 20 * math.sin(k + t), 370 - ph * 200, 14 + 20 * ph, 10 + 14 * ph, fill=mix(BG, (200, 210, 220), 0.6 * (1 - ph)))
        c.text(cx + 120, 260, '水蒸气', 'sans', 28, INK, 'lm')
    if T >= 260 and t < 17:
        g = 1 - fade(t, 15, 17)
        flame(c, cx, 372, 1.6 * g, t, g)
        c.text(cx + 120, 260, '木煤气：在小孔外烧起来', 'sans', 28, mix(BG, INK, g), 'lm')
    # temperature & stage panel
    px = 1180
    c.rect(px, 200, 1860, 860, fill=SHEET, r=16)
    c.text(px + 30, 250, f'罐内约 {T:.0f} ℃（示意）', 'mono', 34, COPPER, 'lm')
    stages = [(100, '约 100 ℃', '水分蒸发'), (260, '约 250–400 ℃', '木头分解，放出可燃气体和焦油'), (450, '更高', '剩下的大多是碳：木炭')]
    for k, (thr, a_, b_) in enumerate(stages):
        on = T >= thr
        y = 340 + k * 120
        c.text(px + 30, y, a_, 'bold', 30, INK if on else MUTED, 'lm')
        c.text(px + 30, y + 44, b_, 'sans', 26, INK if on else MUTED, 'lm')
    e = fade(t, 18, 19)
    c.text(px + 30, 720, '燃烧放热：木炭约是干木头的 2 倍', 'bold', 28, mix(BG, SPARK, e), 'lm')
    c.text(px + 30, 770, '烟少、火稳、温度高 —— 炼铜炼铁都靠它', 'sans', 26, mix(BG, INK, e), 'lm')
    caps(c, t, [(0, 5, '木片装进铁罐，只留一个小孔，放在火上烤'),
                (5.2, 10, '先冒白汽：木头里的水分跑出来'),
                (10.2, 16, '再往上，木头分解，可燃气体从小孔喷出，自己烧起来'),
                (16.2, 22, '没有空气，碳烧不掉：剩下的就是木炭')])

RC = random.Random(16)
PLATES = [(RC.uniform(-1, 1), RC.uniform(-1, 1), RC.uniform(-0.5, 0.5)) for _ in range(36)]
def e16_sinter(c, t, i):
    corner_tag(c, '第 16 集 · 泥巴变陶')
    c.text(60, 96, '晒干的泥坯一泡就化，烧过的为什么不会？', 'serif', 40, INK)
    st = 0 if t < 6 else (1 if t < 12 else (2 if t < 18 else 3))
    names = ['湿泥', '晒干', '约 500–600 ℃', '约 900 ℃ 以上']
    for k, n in enumerate(names):
        x = 160 + k * 420
        on = k == st
        c.rect(x, 170, x + 360, 230, fill=mix(BG, COPPER if on else SHEET, 0.9 if on else 1), r=12)
        c.text(x + 180, 200, n, 'bold', 28, BG if on else MUTED, 'mm')
    cx, cy = 700, 580
    sq = [1.0, 0.72, 0.68, 0.6][st]
    water = [1.0, 0.25, 0.0, 0.0][st]
    fuse = fade(t, 18, 21)
    for k, (u, v, r) in enumerate(PLATES):
        gx, gy = (k % 6) - 2.5, (k // 6) - 2.5
        x = cx + (gx * 90 + u * 20) * sq
        y = cy + (gy * 60 + v * 14) * sq
        w, h = 70, 18
        ca, sa = math.cos(r * 0.3), math.sin(r * 0.3)
        pts = [(x + dx * ca - dy * sa, y + dx * sa + dy * ca) for dx, dy in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2))]
        c.poly(pts, mix(CLAY, (200, 90, 60), 0.4 * (st >= 2)))
        if water > 0:
            for j in range(2):
                c.ellipse(x + (j - 0.5) * 40, y + 22, 6, 6, fill=mix(BG, FIELD, water))
        if st == 2:
            ph = (t * 0.8 + k * 0.13) % 1
            c.ellipse(x, y - 30 - ph * 80, 4, 4, fill=mix(BG, MUTED, 1 - ph))
    if fuse > 0:
        for k in range(35):
            if k % 6 == 5: continue
            x = cx + (((k % 6) - 2.5) * 90 + 45) * sq; y = cy + ((k // 6) - 2.5) * 60 * sq
            c.ellipse(x, y, 10 * fuse, 7 * fuse, fill=mix(CLAY, SPARK, 0.7))
    notes = [('颗粒之间夹着水，能随便捏', '加水还能变回泥浆'),
             ('水蒸发了，颗粒靠得更近', '但一泡水，水又钻回去：会化开'),
             ('黏土矿物里结合的水也被赶走', '这一步回不去了'),
             ('颗粒边缘熔化，彼此粘在一起', '这叫烧结：泥巴变成了陶')]
    a_, b_ = notes[st]
    c.rect(1250, 380, 1860, 640, fill=SHEET, r=16)
    c.text(1280, 450, a_, 'bold', 30, INK, 'lm')
    c.text(1280, 520, b_, 'sans', 28, COPPER if st >= 2 else MUTED, 'lm')
    c.ellipse(1290, 700, 8, 8, fill=FIELD); c.text(1310, 700, '水', 'sans', 24, MUTED, 'lm')
    c.rect(1380, 692, 1440, 708, fill=CLAY); c.text(1452, 700, '黏土颗粒', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 6, '湿泥：片状的黏土颗粒之间夹满了水'),
                (6.2, 12, '晒干：只是把水赶走，颗粒并没有连起来'),
                (12.2, 18, '烧到五六百度：连黏土里结合的水也被赶走，回不去了'),
                (18.2, 24, '再往上，颗粒边缘熔化粘连：烧结。所以陶器不怕水')])

# ---------------------------------------------------------------- 片头片尾
S2A = [('20', '制盐'), ('15', '生火'), ('16', '木炭与陶'), ('23', '纸'), ('22', '肥皂'), ('24', '石灰'), ('17', '炼铜'), ('18', '炼铁')]
SER, VOL = '从零造物', '第三卷 · 火与材料'
CLIPS = {
 'E20_溶解度': (e20_solubility, 20), 'E20_结晶与试卤': (e20_crystal, 24),
 'E20_片头': (titles.opening(SER, VOL, S2A, 0, '北宋 · 约公元 1090 年 · 四川盐场'), 7),
 'E20_片尾': (titles.closing(SER, VOL, S2A, 0, '下集：回到一切的起点 —— 火'), 7),
 'E15_燃烧三要素': (e15_triangle, 20), 'E15_三种取火': (e15_three, 24),
 'E15_片头': (titles.opening(SER, VOL, S2A, 1, '从新石器时代到北宋 · 取火的三种办法'), 7),
 'E15_片尾': (titles.closing(SER, VOL, S2A, 1, '下集：要更高的温度 —— 木炭与陶'), 7),
 'E16_干馏': (e16_pyro, 22), 'E16_烧结': (e16_sinter, 24),
 'E16_片头': (titles.opening(SER, VOL, S2A, 2, '新石器时代起 · 木炭与陶器'), 7),
 'E16_片尾': (titles.closing(SER, VOL, S2A, 2, '下集：同样是泥，瓷为什么不吸水？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
