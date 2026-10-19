"""第二季第三批：E22 肥皂、B15 酿酒与酿醋、E24 石灰 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s2a import S2A, SER, VOL, FIRE, flame
from s2b import SB2

OIL = (226, 186, 70)
GREEN = (120, 200, 140)

# ---------------------------------------------------------------- E22 肥皂
def soap_mol(c, x, y, ang, a=1.0, head=FIELD, L=60):
    hx, hy = x, y
    tx, ty = x + L * math.cos(ang), y + L * math.sin(ang)
    pts = []
    for k in range(7):
        s = k / 6
        w = 5 * math.sin(k * 2.2)
        px = hx + (tx - hx) * s - w * math.sin(ang); py = hy + (ty - hy) * s + w * math.cos(ang)
        pts.append((px, py))
    c.line(pts, mix(BG, (210, 210, 200), a), 4)
    c.ellipse(hx, hy, 10, 10, fill=mix(BG, head, a))

def e22_micelle(c, t, i):
    corner_tag(c, '第 22 集 · 两头的分子')
    c.text(60, 96, '油和水不相溶，肥皂怎么把油带走？', 'serif', 40, INK)
    c.rect(0, 300, 1920, 1080, fill=mix(BG, FIELD, 0.18))
    c.text(1880, 330, '水', 'sans', 26, MUTED, 'rm')
    # cloth fiber at bottom
    c.rect(200, 860, 1720, 900, fill=(190, 180, 160), r=8)
    c.text(1700, 930, '布上的纤维', 'sans', 24, MUTED, 'rm')
    lift = fade(t, 14, 20)
    ox, oy, orr = 960, 860 - 90 - 340 * lift, 90
    c.ellipse(ox, oy, orr * 1.2, orr * (0.75 + 0.25 * lift), fill=OIL)
    c.text(ox, oy, '油', 'bold', 40, BG, 'mm')
    n = 22
    for k in range(n):
        ang = math.pi + k / (n - 1) * math.pi if lift < 0.1 else k / n * 2 * math.pi
        if lift >= 0.1:
            ang = k / n * 2 * math.pi
        # free position
        fx = 260 + (k * 263) % 1400
        fy = 380 + (k * 97) % 320
        f = fade(t, 4 + k * 0.12, 8 + k * 0.12)
        rx = orr * 1.2 + 52
        ry = orr * (0.75 + 0.25 * lift) + 52
        tx = ox + rx * math.cos(ang); ty = oy + ry * math.sin(ang)
        if lift < 0.1 and ty > oy + 10:
            tx, ty = fx, fy
            f = 0
        x = fx + (tx - fx) * ease(f); y = fy + (ty - fy) * ease(f)
        # tail points toward oil when attached, else random
        a_free = k * 1.7 + t * 0.6
        a_att = math.atan2(oy - y, ox - x)
        ang_tail = a_free + (a_att - a_free) * ease(f) if f > 0 else a_free
        soap_mol(c, x, y, ang_tail, 1.0)
    # legend
    c.rect(1400, 140, 1860, 270, fill=SHEET, r=12)
    soap_mol(c, 1440, 205, 0, 1.0)
    c.text(1530, 180, '亲水的「头」', 'sans', 24, FIELD, 'lm')
    c.text(1530, 230, '亲油的「尾巴」', 'sans', 24, INK, 'lm')
    caps(c, t, [(0, 4, '油粘在布上，水冲不走：油和水互相不溶'),
                (4.2, 9, '肥皂分子有两头：一头爱水，一头爱油'),
                (9.2, 14, '爱油的尾巴钻进油里，爱水的头朝外，把油滴团团围住'),
                (14.2, 24, '油滴被「包」起来，脱离布面，随水漂走 —— 这就是去污')])

def fat(c, x, y, a=1.0, split=0.0):
    c.rect(x - 14, y - 90, x + 14, y + 90, fill=mix(BG, GREEN, a), r=8)
    for k in range(3):
        yy = y - 70 + k * 70
        dx = split * (80 + k * 30)
        dy = split * (k - 1) * 60
        pts = [(x + 14 + dx + j * 26, yy + dy + 7 * math.sin(j * 1.8)) for j in range(8)]
        c.line(pts, mix(BG, OIL, a), 6)
        if split > 0.6:
            c.ellipse(x + 14 + dx, yy + dy, 11, 11, fill=mix(BG, FIELD, a * (split - 0.6) / 0.4))

def e22_saponify(c, t, i):
    corner_tag(c, '第 22 集 · 皂化')
    c.text(60, 96, '油加碱，变成了肥皂', 'serif', 40, INK)
    sp = fade(t, 5, 10)
    fat(c, 330, 520, 1.0, sp)
    c.text(330, 300, '油脂', 'bold', 30, INK, 'mm')
    c.text(330, 740, '甘油「骨架」+ 三条脂肪酸', 'sans', 24, MUTED, 'mm')
    a = fade(t, 2, 3)
    for k in range(3):
        x = 140 + k * 60; y = 860 + 20 * math.sin(t * 3 + k)
        c.ellipse(x + 380 * sp, y - 340 * sp * (k == 1), 16, 16, fill=mix(BG, NRED, a * (1 - sp * 0.9)))
        c.text(x + 380 * sp, y - 340 * sp * (k == 1), 'OH', 'mono', 14, mix(BG, BG, 1), 'mm')
    c.text(300, 920, '碱（草木灰水、石灰水……）', 'sans', 24, mix(BG, NRED, a), 'mm')
    if sp > 0.9:
        c.text(420, 330, '→ 甘油', 'sans', 26, GREEN, 'lm')
        c.text(700, 500, '→ 三个肥皂分子', 'bold', 28, FIELD, 'lm')
        c.text(700, 545, '（带电的头 + 亲油的尾）', 'sans', 24, MUTED, 'lm')
    # right: soap pod
    b = fade(t, 12, 13)
    if b > 0:
        x0 = 1180
        c.rect(x0, 200, 1860, 860, fill=mix(BG, SHEET, b), r=16)
        c.text(x0 + 340, 250, '不用碱的「肥皂」：皂荚', 'bold', 32, mix(BG, INK, b), 'mm')
        c.poly([(x0 + 140, 360), (x0 + 560, 330), (x0 + 580, 370), (x0 + 160, 410)], mix(BG, (110, 70, 40), b))
        c.text(x0 + 340, 470, '皂荚里含皂苷：天生就是两头的分子', 'sans', 26, mix(BG, INK, b), 'mm')
        soap_mol(c, x0 + 240, 580, 0, b, head=GREEN, L=120)
        c.text(x0 + 220, 630, '糖链「头」', 'sans', 22, mix(BG, GREEN, b), 'mm')
        c.text(x0 + 330, 630, '亲油的「尾」', 'sans', 22, mix(BG, INK, b), 'mm')
        c.text(x0 + 340, 720, '南宋临安有人沿街卖「肥皂团」', 'sans', 26, mix(BG, COPPER, b), 'mm')
        c.text(x0 + 340, 765, '就是捣碎的皂荚团成的丸子', 'sans', 26, mix(BG, COPPER, b), 'mm')
    caps(c, t, [(0, 5, '油脂分子：一个甘油骨架，挂着三条长长的脂肪酸'),
                (5.2, 12, '遇到碱，三条脂肪酸被剪下来，变成三个肥皂分子：这叫皂化'),
                (12.2, 22, '古人还有现成的：皂荚里的皂苷，天生就是「一头爱水、一头爱油」')])

# ---------------------------------------------------------------- B15 酿酒与酿醋
RB = random.Random(15)
YEAST = [(RB.uniform(560, 1340), RB.uniform(460, 840)) for _ in range(9)]
def jar(c, x0, y0, x1, y1, lvl, col, lid=True, gauze=False):
    c.rect(x0 + 6, lvl, x1 - 6, y1 - 6, fill=col, r=10)
    c.rect(x0, y0, x1, y1, outline=MUTED, width=5, r=20)
    if lid: c.rect(x0 - 10, y0 - 24, x1 + 10, y0 + 4, fill=(110, 80, 50), r=6)
    if gauze:
        for k in range(12):
            c.line([(x0 + k * (x1 - x0) / 11, y0 - 6), (x0 + k * (x1 - x0) / 11 + 12, y0 + 6)], (220, 220, 210), 2)

def b15_wine(c, t, i):
    corner_tag(c, 'B15 · 糖化与酒化')
    c.text(60, 96, '粮食里没有糖，酒是怎么来的？', 'serif', 40, INK)
    jar(c, 480, 300, 1440, 900, 380, mix(BG, (200, 190, 150), 0.35), True)
    c.text(1440, 240, '密封：没有空气', 'sans', 26, MUTED, 'rm')
    cut = fade(t, 4, 11)
    eat = fade(t, 11, 19)
    # starch chain → glucose
    for k in range(14):
        x0 = 600 + k * 52; y0 = 450 + 12 * math.sin(k)
        x = x0 + cut * (((k * 37) % 9) - 4) * 30; y = y0 + cut * ((k * 53) % 7) * 50
        if eat > (k / 14):
            continue
        c.ellipse(x, y, 16, 16, fill=SPARK)
        if k < 13 and cut < 0.2:
            c.line([(x0 + 16, y0), (x0 + 36, y0 + 12 * math.sin(k + 1) - 12 * math.sin(k))], SPARK, 4)
    if 2 < t < 12:
        for k in range(4):
            mx = 620 + k * 200; my = 400 + 30 * math.sin(t * 2 + k)
            c.poly([(mx - 14, my), (mx, my - 14), (mx + 14, my), (mx, my + 14)], GREEN)
        c.text(960, 340, '曲里的霉菌放出酶，把淀粉「剪」成葡萄糖', 'sans', 26, GREEN, 'mm')
    # yeast
    if t > 10:
        a = fade(t, 10, 11)
        for (x, y) in YEAST:
            c.ellipse(x, y, 26, 20, fill=mix(BG, (230, 220, 190), a), outline=mix(BG, MUTED, a), width=2)
        for k in range(int(30 * eat)):
            ph = (t * 0.5 + k * 0.137) % 1
            x = 560 + (k * 79) % 780; y = 860 - ph * 460
            c.ellipse(x, y, 7, 7, outline=mix(BG, INK, 0.6), width=2)
        c.text(960, 940, '酵母：葡萄糖 → 酒精 + 二氧化碳（气泡）', 'bold', 28, mix(BG, INK, a), 'mm')
    c.rect(1480, 320, 1880, 560, fill=SHEET, r=12)
    c.ellipse(1510, 370, 12, 12, fill=SPARK); c.text(1534, 370, '葡萄糖', 'sans', 24, INK, 'lm')
    c.poly([(1496, 420), (1510, 406), (1524, 420), (1510, 434)], GREEN); c.text(1534, 420, '曲的酶', 'sans', 24, INK, 'lm')
    c.ellipse(1510, 470, 16, 12, fill=(230, 220, 190)); c.text(1534, 470, '酵母', 'sans', 24, INK, 'lm')
    c.ellipse(1510, 520, 7, 7, outline=INK, width=2); c.text(1534, 520, '二氧化碳', 'sans', 24, INK, 'lm')
    caps(c, t, [(0, 4, '米饭里是淀粉：一长串连在一起的葡萄糖'),
                (4.2, 11, '酒曲里的霉菌放出酶，把长链剪成一个个葡萄糖'),
                (11.2, 19, '酵母在没有空气的缸里吃糖，放出酒精和二氧化碳'),
                (19.2, 24, '剪糖和吃糖同时进行：这叫「边糖化边发酵」')])

def b15_vinegar(c, t, i):
    corner_tag(c, 'B15 · 醋酸菌')
    c.text(60, 96, '同一缸酒，打开盖子就会变酸', 'serif', 40, INK)
    open_ = fade(t, 2, 4)
    film = fade(t, 6, 12)
    jar(c, 300, 300, 1000, 900, 420, mix(BG, (200, 190, 150), 0.35), lid=open_ < 0.5, gauze=open_ >= 0.5)
    if open_ >= 0.5:
        for k in range(10):
            ph = (t * 0.4 + k / 10) % 1
            x = 340 + k * 64; y = 200 + ph * 220
            c.text(x, y, 'O₂' if False else 'O2', 'mono', 20, mix(BG, FIELD, 1 - ph), 'mm')
        c.text(650, 250, '空气进来了', 'sans', 26, FIELD, 'mm')
    if film > 0:
        c.rect(306, 420, 994, 420 + 30 * film, fill=mix(BG, (230, 220, 200), 0.8 * film))
        c.text(650, 470 + 20 * film, '表面长出一层菌膜：醋酸菌（「醋母」）', 'sans', 24, mix(BG, INK, film), 'mm')
    conv = fade(t, 8, 18)
    bx = 1160
    c.rect(bx, 300, 1860, 880, fill=SHEET, r=16)
    c.text(bx + 30, 350, '醋酸菌：酒精 + 氧气 → 醋酸 + 水', 'bold', 28, INK, 'lm')
    for k, (lab, v, col) in enumerate([('酒精', 1 - conv, SPARK), ('醋酸', conv, NRED)]):
        y = 450 + k * 100
        c.text(bx + 30, y, lab, 'sans', 28, MUTED, 'lm')
        c.rect(bx + 130, y - 18, bx + 650, y + 18, fill=LINE, r=18)
        c.rect(bx + 130, y - 18, bx + 130 + 520 * v, y + 18, fill=col, r=18)
    ph = 4.0 - 1.2 * conv
    c.text(bx + 30, 660, f'pH 约 {ph:.1f}（示意，待实测）', 'mono', 30, COPPER, 'lm')
    c.text(bx + 30, 720, '酵母怕氧、醋酸菌要氧：', 'sans', 26, INK, 'lm')
    c.text(bx + 30, 765, '一个要密封，一个要通风', 'bold', 28, COPPER, 'lm')
    caps(c, t, [(0, 4, '酒酿好了，盖子没盖严……'),
                (4.2, 12, '空气进来，醋酸菌在表面安家，长出一层膜'),
                (12.2, 20, '它们用氧气把酒精变成醋酸：酒「坏」了，醋就成了')])

# ---------------------------------------------------------------- E24 石灰
CYC = [('石灰石', '碳酸钙', (200, 196, 186)), ('生石灰', '氧化钙', (236, 232, 222)), ('熟石灰', '氢氧化钙', (226, 228, 232)), ('变回石头', '碳酸钙', (214, 210, 200))]
POEM = ['千锤万凿出深山', '烈火焚烧若等闲', '粉骨碎身浑不怕', '要留清白在人间']
STEPS = ['开采', '约 900 ℃ 煅烧：放出二氧化碳', '加水：放热、冒汽、碎成粉', '吸收空气里的二氧化碳：慢慢变硬']

def e24_cycle(c, t, i):
    corner_tag(c, '第 24 集 · 石灰的循环')
    c.text(60, 96, '烧过的石头，为什么还能变回石头？', 'serif', 40, INK)
    cx, cy, R = 700, 570, 300
    stage = min(3, int(t / 6))
    for k in range(4):
        ang = -math.pi / 2 + k * math.pi / 2
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        on = k <= stage
        c.ellipse(x, y, 90, 90, fill=mix(SHEET, CYC[k][2], 0.85 if on else 0.15), outline=COPPER if k == stage else LINE, width=4)
        c.text(x, y - 16, CYC[k][0], 'bold', 30, BG if on else MUTED, 'mm')
        c.text(x, y + 22, CYC[k][1], 'sans', 22, mix(BG, (60, 60, 60), 1) if on else MUTED, 'mm')
        # arrow to next
        if k < 3:
            a0 = ang + 0.42; a1 = ang + math.pi / 2 - 0.42
            f = fade(t, (k + 1) * 6 - 1.5, (k + 1) * 6)
            if f > 0:
                pts = [(cx + R * math.cos(a0 + (a1 - a0) * s / 20), cy + R * math.sin(a0 + (a1 - a0) * s / 20)) for s in range(int(20 * f) + 1)]
                if len(pts) > 1: c.line(pts, COPPER, 6)
    if t > 22:
        c.text(cx, cy, '一圈', 'serif', 44, COPPER, 'mm')
    # effects
    if stage == 1:
        for k in range(5): flame(c, cx + R - 80 + k * 40, cy + 130, 0.8, t + k)
        for k in range(6):
            ph = (t * 0.6 + k / 6) % 1
            c.text(cx + R + 120, cy - 40 - ph * 140, 'CO2', 'mono', 22, mix(BG, MUTED, 1 - ph), 'mm')
    if stage == 2:
        for k in range(6):
            ph = (t * 0.7 + k / 6) % 1
            c.ellipse(cx - 60 + k * 24, cy + R + 100 - ph * 120, 10 + 14 * ph, 8 + 10 * ph, fill=mix(BG, (220, 220, 230), 0.6 * (1 - ph)))
        c.text(cx + 140, cy + R + 60, '很烫！', 'bold', 28, NRED, 'lm')
    if stage == 3:
        for k in range(5):
            ph = (t * 0.5 + k / 5) % 1
            c.text(cx - R - 140 + ph * 40, cy - 60 + k * 30, 'CO2', 'mono', 20, mix(BG, FIELD, 1 - ph), 'mm')
    # poem panel
    px = 1180
    c.rect(px, 230, 1860, 900, fill=SHEET, r=16)
    c.text(px + 340, 280, '明 · 于谦《石灰吟》', 'sans', 26, MUTED, 'mm')
    for k in range(4):
        on = k <= stage
        y = 380 + k * 130
        c.text(px + 340, y, POEM[k], 'serif', 44, INK if on else mix(BG, MUTED, 0.5), 'mm')
        c.text(px + 340, y + 50, STEPS[k], 'sans', 24, COPPER if on else mix(BG, MUTED, 0.4), 'mm')
    caps(c, t, [(0, 6, '石灰石的主要成分是碳酸钙'),
                (6.2, 12, '烧到约九百度，二氧化碳跑掉，剩下生石灰'),
                (12.2, 18, '生石灰遇水剧烈放热，变成熟石灰粉'),
                (18.2, 24, '抹上墙，它慢慢吸收空气里的二氧化碳，又变回了碳酸钙')])

RM = random.Random(24)
CRY = [(RM.uniform(-1, 1), RM.uniform(-1, 1), RM.uniform(0, math.pi)) for _ in range(60)]
def e24_rice(c, t, i):
    corner_tag(c, '第 24 集 · 糯米灰浆')
    c.text(60, 96, '城墙的灰浆里，为什么要加糯米汤？', 'serif', 40, INK)
    g = fade(t, 1, 9)
    for side, (cx, lab, rice) in enumerate([(520, '普通石灰浆', False), (1400, '加了糯米汤', True)]):
        c.rect(cx - 360, 220, cx + 360, 780, fill=SHEET, r=16)
        c.text(cx, 190, lab, 'bold', 34, INK, 'mm')
        c.rect(cx - 330, 250, cx + 330, 750, fill=(40, 38, 36), r=8)
        if rice:
            for k in range(14):
                pts = [(cx - 320 + j * 50, 270 + k * 34 + 10 * math.sin(j + k)) for j in range(14)]
                c.line(pts, mix((40, 38, 36), (200, 200, 170), 0.5), 2)
        n = 60 if rice else 22
        for k in range(n):
            u, v, a = CRY[k % 60]
            if rice:
                gx, gy = (k % 10) - 4.5, (k // 10) - 2.5
                x = cx + gx * 64 + u * 8; y = 500 + gy * 80 + v * 8
                s = 24 * g
            else:
                x = cx + u * 260; y = 500 + v * 200
                s = (40 + 30 * abs(math.sin(k))) * g
            ca, sa = math.cos(a), math.sin(a)
            pts = [(x + dx * ca - dy * sa, y + dx * sa + dy * ca) for dx, dy in ((-s, -s * 0.6), (s, -s * 0.6), (s * 1.1, s * 0.6), (-s * 0.9, s * 0.6))]
            c.poly(pts, mix((40, 38, 36), (226, 224, 214), 0.9))
        c.text(cx, 830, '晶体大而乱，缝隙多' if not rice else '晶体小而密，被有机物「粘」住', 'sans', 28, MUTED if not rice else COPPER, 'mm')
    a = fade(t, 12, 13)
    c.text(960, 920, '2010 年的研究：糯米里的支链淀粉控制了碳酸钙晶体的生长', 'sans', 28, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 9, '同样是石灰浆变硬，左边自己长，右边加了糯米汤'),
                (9.2, 20, '糯米的支链淀粉让晶体长得小而致密：更结实、更防水')])

# ---------------------------------------------------------------- 片头片尾
CLIPS = {
 'E22_两头的分子': (e22_micelle, 24), 'E22_皂化与皂荚': (e22_saponify, 22),
 'E22_片头': (titles.opening(SER, VOL, S2A, 4, '周代用草木灰 · 南宋临安卖「肥皂团」'), 7),
 'E22_片尾': (titles.closing(SER, VOL, S2A, 4, '下集：同一缸粮食，怎么先变酒、再变醋？'), 7),
 'B15_糖化与酒化': (b15_wine, 24), 'B15_醋酸菌': (b15_vinegar, 20),
 'B15_片头': (titles.opening(BSER, BVOL, SB2, 2, '北魏《齐民要术》已有制曲、造酒、作醋的专篇'), 7),
 'B15_片尾': (titles.closing(BSER, BVOL, SB2, 2, '下集：烧过的石头，为什么还能变回石头？'), 7),
 'E24_石灰的循环': (e24_cycle, 24), 'E24_糯米灰浆': (e24_rice, 20),
 'E24_片头': (titles.opening(SER, VOL, S2A, 5, '「烈火焚烧若等闲」· 石灰与灰浆'), 7),
 'E24_片尾': (titles.closing(SER, VOL, S2A, 5, '下集：北宋的「胆水浸铜」'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
