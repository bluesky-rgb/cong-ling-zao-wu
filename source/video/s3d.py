"""第三季收尾：E30 选种与嫁接、B6 赵州桥、第三季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s3a import S3A, SER3, VOL3, WATER
from s3b import SB3, GREEN

STONE = (170, 164, 150)
BARK = (120, 86, 60)
CAMB = (120, 210, 120)
XYL = (220, 200, 150)

# ---------------------------------------------------------------- E30 选种与嫁接
RS = random.Random(30)
def e30_select(c, t, i):
    corner_tag(c, '第 30 集 · 选种')
    c.text(60, 96, '每年挑最好的穗留种，会发生什么？', 'serif', 40, INK)
    gen = min(4, int(t / 4.4))
    mu = 1.0 + 0.35 * gen
    R = random.Random(gen)
    vals = sorted([max(0.3, R.gauss(mu, 0.35)) for _ in range(40)])
    thr = vals[-8]
    # plants row
    for k, v in enumerate(vals):
        x = 140 + k * 27
        h = 100 + 70 * v
        c.line([(x, 640), (x, 640 - h)], (180, 170, 90), 4)
        sel = v >= thr and fade(t - gen * 4.4, 2, 2.6) > 0
        c.ellipse(x, 640 - h, 9 + 5 * v, 16 + 8 * v, fill=SPARK if sel else (210, 190, 110))
        if sel:
            c.ellipse(x, 640 - h, 18 + 5 * v, 26 + 8 * v, outline=COPPER, width=3)
    c.text(140, 700, f'第 {gen + 1} 年', 'serif', 40, COPPER, 'lm')
    c.text(400, 700, '橙圈：挑出来留种的穗', 'sans', 26, MUTED, 'lm')
    # histogram of mean over generations
    gx0, gy1 = 1840 - 560, 640
    c.text(gx0, 240, '每年的平均穗大小（示意）', 'sans', 24, MUTED, 'lm')
    for g in range(gen + 1):
        h = 60 + 70 * g
        c.rect(gx0 + g * 110, gy1 - h, gx0 + g * 110 + 80, gy1, fill=mix(BG, COPPER, 0.4 + 0.15 * g), r=6)
        c.text(gx0 + g * 110 + 40, gy1 + 30, f'{g + 1}', 'mono', 22, MUTED, 'mm')
    a = fade(t, 14, 15)
    c.rect(140, 780, 1780, 920, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 825, '《齐民要术》：「常岁岁别收，选好穗纯色者……别种，以拟明年种子」', 'serif', 30, mix(BG, COPPER, a), 'mm')
    c.text(960, 880, '每年单独收、挑好穗、单独种：一代代把好性状攒起来', 'sans', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 7, '同一块地里的穗，有大有小'),
                (7.2, 14, '每年只挑最好的几株留种，第二年的平均水平就往上挪一点'),
                (14.2, 22, '年复一年，好性状一点点攒起来：这就是选种')])

def stem_section(c, cx, cy, r, a=1.0, cut=None):
    c.ellipse(cx, cy, r, r, fill=mix(BG, BARK, a))
    c.ellipse(cx, cy, r * 0.82, r * 0.82, fill=mix(BG, CAMB, a))
    c.ellipse(cx, cy, r * 0.74, r * 0.74, fill=mix(BG, XYL, a))

def e30_graft(c, t, i):
    corner_tag(c, '第 30 集 · 嫁接')
    c.text(60, 96, '把一根枝条「接」到另一棵树上，为什么能活？', 'serif', 40, INK)
    # left: cross section labels
    stem_section(c, 330, 420, 150)
    c.text(330, 620, '树枝横截面', 'bold', 28, INK, 'mm')
    for lab, y, col in [('树皮', 250, BARK), ('形成层：会分裂的一薄层细胞', 300, CAMB), ('木质部：往上运水', 350, XYL)]:
        c.text(520, y, lab, 'sans', 24, col, 'lm')
    # right: side view of graft
    jx = 1220
    join = fade(t, 4, 8)
    heal = fade(t, 9, 15)
    flow = fade(t, 15, 17)
    # rootstock (bottom)
    c.rect(jx - 60, 560, jx + 60, 960, fill=BARK, r=8)
    c.rect(jx - 50, 560, jx - 42, 960, fill=CAMB); c.rect(jx + 42, 560, jx + 50, 960, fill=CAMB)
    c.text(jx + 100, 860, '砧木：提供根', 'sans', 26, INK, 'lm')
    # scion (top) sliding down
    sy = 300 + 220 * join
    c.rect(jx - 60, sy - 260, jx + 60, sy, fill=mix(BARK, (150, 110, 70), 0.4), r=8)
    c.rect(jx - 50, sy - 260, jx - 42, sy, fill=CAMB); c.rect(jx + 42, sy - 260, jx + 50, sy, fill=CAMB)
    c.text(jx + 100, sy - 200, '接穗：好品种的枝条', 'sans', 26, INK, 'lm')
    for k in range(3):
        c.ellipse(jx + (-1) ** k * 70, sy - 230 - k * 20, 40, 18, fill=GREEN)
    if join > 0.95:
        # tape and callus
        c.rect(jx - 70, 540, jx + 70, 580, fill=mix(BG, (200, 200, 210), 0.8), r=6)
        if heal > 0:
            for k in range(int(10 * heal)):
                c.ellipse(jx - 46 + (k % 2) * 92, 548 + (k // 2) * 6, 6, 6, fill=CAMB)
            c.text(jx - 120, 560, '形成层细胞长到一起', 'sans', 24, CAMB, 'rm')
    if flow > 0:
        for k in range(5):
            ph = (t * 0.6 + k / 5) % 1
            c.ellipse(jx - 20, 940 - ph * 640, 7, 7, fill=FIELD)
            c.ellipse(jx + 20, 320 + ph * 640, 7, 7, fill=SPARK)
        c.text(jx - 120, 760, '水往上', 'sans', 24, FIELD, 'rm')
        c.text(jx - 120, 800, '糖往下', 'sans', 24, SPARK, 'rm')
    caps(c, t, [(0, 4, '树枝里有一圈薄薄的「形成层」：会不断分裂长新细胞'),
                (4.2, 9, '嫁接：把好品种的枝条削好，和另一棵树对接，形成层对齐，绑紧'),
                (9.2, 15, '两边的形成层长到一起，连通了输水和输糖的管道'),
                (15.2, 20, '根是砧木的，结的果子是接穗的品种')])

# ---------------------------------------------------------------- B6 赵州桥
def arch_blocks(c, cx, base, span, rise, n, col, a=1.0):
    R = (span ** 2 / 4 + rise ** 2) / (2 * rise)
    yc = base - rise + R
    half = math.asin((span / 2) / R)
    pts = []
    for k in range(n + 1):
        ang = -half + 2 * half * k / n
        pts.append((cx + R * math.sin(ang), yc - R * math.cos(ang)))
    th = 34
    for k in range(n):
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        def off(x, y):
            dx, dy = x - cx, y - yc; L = math.hypot(dx, dy); return x - dx / L * th, y - dy / L * th
        c.poly([(x0, y0), (x1, y1), off(x1, y1), off(x0, y0)], mix(BG, col, a))
        c.line([(x0, y0), off(x0, y0)], mix(BG, BG, 1), 2)
    return pts, R, yc

def b6_arch(c, t, i):
    corner_tag(c, 'B6 · 拱的受力')
    c.text(60, 96, '一块块石头，为什么能架成一座桥？', 'serif', 40, INK)
    flat = fade(t, 11, 13)
    span = 900
    rise = 450 * (1 - flat) + 180 * flat
    cx, base = 760, 820
    pts, R, yc = arch_blocks(c, cx, base, span, rise, 15, STONE)
    c.rect(cx - span / 2 - 120, base, cx - span / 2 + 20, 960, fill=(120, 110, 100), r=6)
    c.rect(cx + span / 2 - 20, base, cx + span / 2 + 120, 960, fill=(120, 110, 100), r=6)
    # load
    for k in range(5):
        x = cx - 300 + k * 150
        c.arrow(x, base - rise - 160, x, base - rise - 60 + (abs(x - cx) / span) * 40, mix(BG, NRED, 0.9), 4, 14)
    c.text(cx, base - rise - 190, '车和人的重量', 'sans', 24, NRED, 'mm')
    a = fade(t, 4, 6)
    if a > 0:
        # thrust arrows along arch
        for k in range(1, 15, 2):
            (x0, y0), (x1, y1) = pts[k], pts[k + 1]
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy)
            sgn = 1 if k > 7 else -1
            c.arrow(mx, my - 40, mx + sgn * dx / L * 50, my - 40 + sgn * dy / L * 50, mix(BG, SPARK, a), 3, 10)
        # outward thrust at feet
        Hs = 1.0 / max(0.2, rise / span)
        for side in (-1, 1):
            x = cx + side * span / 2
            c.arrow(x, base - 20, x + side * (40 + 30 * Hs), base - 20, mix(BG, COPPER, a), 6, 16)
        c.text(cx, base + 60, '拱脚向外推：桥台要顶住', 'sans', 26, mix(BG, COPPER, a), 'mm')
    px = 1360
    c.rect(px, 230, 1860, 760, fill=SHEET, r=16)
    c.text(px + 30, 280, '拱：每块石头只受压', 'bold', 28, INK, 'lm')
    c.text(px + 30, 330, '石头不怕压，最怕拉', 'sans', 26, INK, 'lm')
    c.text(px + 30, 420, '赵州桥的拱很「扁」', 'bold', 28, COPPER, 'lm')
    c.text(px + 30, 470, '跨度约 37 米，拱高只有 7 米多', 'sans', 24, INK, 'lm')
    c.text(px + 30, 515, '桥面平缓，车马好走', 'sans', 24, INK, 'lm')
    c.text(px + 30, 590, '代价：拱脚向外推得更狠', 'sans', 24, NRED, 'lm')
    caps(c, t, [(0, 4, '石头一块挨一块排成弧形，上面压上重量'),
                (4.2, 11, '重量沿着拱一路传下去，每块石头都被「挤」着：只受压，不受拉'),
                (11.2, 22, '把拱压扁，桥面更平，可拱脚向外推得更厉害，两头的桥台要更结实')])

def b6_spandrel(c, t, i):
    corner_tag(c, 'B6 · 敞肩拱')
    c.text(60, 96, '两肩为什么要开四个小拱？', 'serif', 40, INK)
    flood = fade(t, 11, 13)
    for k, (cx, lab, open_) in enumerate([(500, '实肩拱', False), (1420, '敞肩拱（赵州桥）', True)]):
        base, span, rise = 780, 760, 160
        c.rect(cx - 440, 860 - 160 * flood, cx + 440, 980, fill=mix(BG, FIELD, 0.35)) if flood > 0 else None
        pts, R, yc = arch_blocks(c, cx, base, span, rise, 13, STONE)
        deck = base - rise - 60
        # spandrel fill polygons (left and right)
        for side in (-1, 1):
            x_end = cx + side * span / 2
            poly = [(cx + side * 60, deck + 34), (x_end, deck + 34), (x_end, base)]
            arc_pts = [p for p in pts if side * (p[0] - cx) > 60]
            arc_pts = sorted(arc_pts, key=lambda p: -side * p[0])
            poly += arc_pts
            c.poly(poly, mix(BG, STONE, 0.85))
            if open_:
                for j, (ox, w) in enumerate([(0.62, 70), (0.86, 50)]):
                    hx = cx + side * span / 2 * ox
                    c.ellipse(hx, deck + 78, w, w * 0.9, fill=BG if flood < 0.3 else mix(BG, FIELD, 0.35))
        c.rect(cx - span / 2 - 20, deck, cx + span / 2 + 20, deck + 34, fill=STONE, r=4)
        c.text(cx, 220, lab, 'bold', 32, INK, 'mm')
        w = 1.0 if not open_ else 0.8
        c.text(cx, 300, '自重（示意）', 'sans', 24, MUTED, 'mm')
        c.rect(cx - 200, 320, cx + 200, 350, fill=LINE, r=15)
        c.rect(cx - 200, 320, cx - 200 + 400 * w, 350, fill=COPPER if not open_ else FIELD, r=15)
        if flood > 0.5:
            if open_:
                for j in range(6):
                    ph = (t * 1.2 + j / 6) % 1
                    c.arrow(cx - 400 + ph * 800, deck + 78, cx - 380 + ph * 800, deck + 78, mix(BG, FIELD, 0.9), 3, 10)
                c.text(cx, 1000, '洪水从小拱里穿过去', 'sans', 24, FIELD, 'mm')
            else:
                for j in range(4):
                    c.arrow(cx - 440, deck + 40 + j * 30, cx - 380, deck + 40 + j * 30, NRED, 5, 14)
                c.text(cx, 1000, '洪水整个拍在桥身上', 'sans', 24, NRED, 'mm')
    caps(c, t, [(0, 6, '大拱两肩：一种填实，一种开出小拱'),
                (6.2, 11, '开小拱，桥身轻了，压在拱上和地基上的重量也小了'),
                (11.2, 22, '发洪水时，水能从小拱里穿过去，桥被冲的力量小得多')], y=1050)

# ---------------------------------------------------------------- 第三季特辑：一滴水的旅程
STEPS = [('提', '水车 · 螺旋', '28 · 25'), ('引', '虹吸 · 水渠', '26'), ('分', '都江堰', 'B5'), ('省', '陶罐滴灌', '27'),
         ('养', '轮作 · 选种', '29 · 30'), ('净', '过滤 · 晒水', '34'), ('冷', '冰窖 · 蒸发', 'B12 · 38'), ('过', '石拱桥', 'B6')]

def s3_journey(c, t, i):
    corner_tag(c, '第三季特辑 · 一滴水的旅程')
    c.text(60, 110, '第三季：一滴水的旅程', 'serif', 48, INK, 'lm')
    n = len(STEPS)
    pos = []
    for k in range(n):
        row = 0 if k < 4 else 1
        col = k if row == 0 else (7 - k)
        x = 300 + col * 440
        y = 380 if row == 0 else 760
        pos.append((x, y))
    # path
    path = pos[:4] + [(pos[3][0] + 200, 380), (pos[3][0] + 200, 760)] + pos[4:]
    c.line(path, LINE, 6)
    prog = fade(t, 1, 24)
    for k, ((x, y), (ch, lab, ep)) in enumerate(zip(pos, STEPS)):
        a = fade(prog * n, k, k + 0.6)
        c.ellipse(x, y, 80, 80, fill=mix(SHEET, FIELD, 0.85 * a), outline=mix(LINE, FIELD, a), width=4)
        c.text(x, y, ch, 'serif', 56, mix(MUTED, BG, a), 'mm')
        c.text(x, y + 120, lab, 'bold', 28, mix(MUTED, INK, a), 'mm')
        c.text(x, y + 160, ep, 'mono', 22, mix(BG, MUTED, a), 'mm')
    # moving drop
    L = [math.hypot(path[j + 1][0] - path[j][0], path[j + 1][1] - path[j][1]) for j in range(len(path) - 1)]
    d = prog * sum(L)
    for j, l in enumerate(L):
        if d <= l:
            (ax, ay), (bx, by) = path[j], path[j + 1]
            x = ax + (bx - ax) * d / l; y = ay + (by - ay) * d / l
            y -= 110
            c.poly([(x, y - 34), (x - 20, y), (x + 20, y)], mix(BG, FIELD, 1))
            c.ellipse(x, y + 4, 21, 21, fill=FIELD)
            break
        d -= l
    caps(c, t, [(1, 12, '把水从河里提上来，引过堤坝，分进田里'),
                (12.2, 22, '省着用，养活庄稼；喝之前先过滤、晒一晒，热天再让它变凉'),
                (22.2, 28, '下一季：救命的知识 —— 那些能让人多活几十年的常识')], y=1010)

# ---------------------------------------------------------------- 片头片尾
CLIPS = {
 'E30_选种': (e30_select, 22), 'E30_嫁接': (e30_graft, 20),
 'E30_片头': (titles.opening(SER3, VOL3, S3A, 7, '北魏《齐民要术》· 选种、插梨'), 7),
 'E30_片尾': (titles.closing(SER3, VOL3, S3A, 7, '下集：一千四百年的石拱桥'), 7),
 'B6_拱的受力': (b6_arch, 22), 'B6_敞肩拱': (b6_spandrel, 22),
 'B6_片头': (titles.opening(BSER, BVOL, SB3, 2, '隋 · 公元 595–605 年 · 李春'), 7),
 'B6_片尾': (titles.closing(BSER, BVOL, SB3, 2, '下集：第三季特辑'), 7),
 'S3_一滴水的旅程': (s3_journey, 28),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
