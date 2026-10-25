"""第七季第三批：E10 蒸汽发电、E19 煤与焦炭、E21 玻璃 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s7a import S7A, SER7, VOL7

STEAM = (200, 210, 220)
WATER = (70, 140, 200)
HOT = (235, 110, 60)
COAL = (60, 62, 66)
COKE = (120, 122, 126)
CHAR = (40, 36, 34)

def flames(c, x0, x1, y, t, h=60, a=1.0):
    n = max(3, int((x1 - x0) / 34))
    for k in range(n):
        fx = x0 + (x1 - x0) * (k + 0.5) / n
        fh = h * (0.7 + 0.3 * math.sin(t * 9 + k * 1.3))
        c.poly([(fx - 16, y), (fx + 16, y), (fx, y - fh)], mix(BG, SPARK if k % 2 else HOT, a))

# ---------------------------------------------------------------- E10 蒸汽发电
def e10_expand(c, t, i):
    corner_tag(c, '第 10 集 · 一千七百倍')
    c.text(60, 96, '一克水变成蒸汽，体积变大多少？', 'serif', 40, INK)
    # left: one 1 mL cube of water
    a = fade(t, 0.5, 1.5)
    cx, cy = 300, 620
    c.rect(cx - 20, cy - 20, cx + 20, cy + 20, fill=mix(BG, WATER, a), r=3)
    c.text(cx, cy + 60, '1 毫升水', 'bold', 28, mix(BG, INK, a), 'mm')
    c.text(cx, cy + 100, '（约 1 克）', 'sans', 24, mix(BG, MUTED, a), 'mm')
    # right: grows to ~1.7 L cube (side 11.9 cm) shown scaled: 1 mL side 1 cm -> 40 px ; 1.67 L side 11.9 cm -> 475 px
    g = ease(fade(t, 3, 10))
    side = 40 + (475 - 40) * g
    bx, by = 1150, 620
    if g > 0:
        c.rect(bx - side / 2, by + 20 - side, bx + side / 2, by + 20, fill=mix(BG, STEAM, 0.25 * g), outline=mix(BG, STEAM, g), width=3, r=4)
        c.ellipse(bx - side / 2 + 20, by + 20 - side + 20, 4, 4, fill=STEAM)
        rnd = random.Random(3)
        for k in range(int(40 * g)):
            px = bx + rnd.uniform(-side / 2 + 10, side / 2 - 10)
            py = by + 20 - rnd.uniform(10, side - 10)
            c.ellipse(px + 4 * math.sin(t * 7 + k), py + 4 * math.cos(t * 6 + k), 5, 5, fill=STEAM)
        c.text(bx, by + 60, f'约 {1 + 1669 * g:.0f} 毫升蒸汽', 'bold', 28, INK, 'mm')
        c.text(bx, by + 100, '（100 ℃、一个大气压）', 'sans', 24, MUTED, 'mm')
    if 1.5 < t < 10:
        flames(c, cx - 60, cx + 60, cy + 150, t, 50)
    b = fade(t, 12, 13)
    c.rect(300, 790, 1620, 940, fill=mix(BG, SHEET, b), r=14)
    c.text(960, 835, '水变成蒸汽，体积约变成 1700 倍', 'serif', 34, mix(BG, SPARK, b), 'mm')
    c.text(960, 895, '要是不让它变大 —— 关在容器里 —— 压力就会一路升高：这就是蒸汽的力量，也是它的危险', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 3, '一毫升水，大约一克'),
                (3.2, 12, '烧开、变成蒸汽：一个指甲盖大小的水，变成一个一升多的大盒子'),
                (12.2, 22, '蒸汽想变大，就会推动挡在前面的东西；关住它，压力就会危险地升高')], y=1010)

def e10_plant(c, t, i):
    corner_tag(c, '第 10 集 · 火电厂的骨架')
    c.text(60, 96, '从一把火到一盏灯，中间要过几道关？', 'serif', 40, INK)
    # boiler
    bx0, by0, bx1, by1 = 120, 420, 460, 720
    c.rect(bx0, by0, bx1, by1, outline=MUTED, width=5, r=30)
    lvl = by0 + 140
    c.rect(bx0 + 6, lvl, bx1 - 6, by1 - 6, fill=mix(BG, WATER, 0.6), r=24)
    flames(c, bx0 + 20, bx1 - 20, by1 + 70, t, 60)
    c.text((bx0 + bx1) / 2, by1 + 110, '① 锅炉：烧煤把水变成蒸汽', 'sans', 24, INK, 'mm')
    # safety valve
    c.rect(bx0 + 40, by0 - 60, bx0 + 80, by0, fill=NRED, r=4)
    c.text(bx0 + 60, by0 - 80, '安全阀', 'bold', 22, NRED, 'mm')
    # pipe to turbine
    c.line([(bx1 - 60, by0), (bx1 - 60, 300), (760, 300), (760, 420)], STEAM, 14)
    # turbine
    tx, ty = 820, 540
    c.ellipse(tx, ty, 120, 120, outline=MUTED, width=4)
    ang = t * 6
    for k in range(10):
        a_ = ang + k * math.pi / 5
        c.line([(tx + 20 * math.cos(a_), ty + 20 * math.sin(a_)), (tx + 110 * math.cos(a_ + 0.3), ty + 110 * math.sin(a_ + 0.3))], (180, 185, 190), 8)
    c.text(tx, ty + 170, '② 汽轮机：蒸汽冲叶片', 'sans', 24, INK, 'mm')
    # shaft to generator
    c.rect(tx + 120, ty - 10, 1180, ty + 10, fill=MUTED)
    gx = 1260
    c.rect(gx - 80, ty - 90, gx + 80, ty + 90, fill=mix(BG, COPPER, 0.6), outline=COPPER, width=4, r=16)
    c.text(gx, ty, '发电机', 'bold', 26, INK, 'mm')
    c.text(gx, ty + 170, '③ 第 04 集的磁生电', 'sans', 24, INK, 'mm')
    # wire to lamp
    c.line([(gx + 80, ty - 40), (1600, ty - 40), (1600, 380)], COPPER, 5)
    on = 0.6 + 0.4 * math.sin(t * 3) ** 2
    c.ellipse(1600, 340, 50, 50, fill=mix(BG, SPARK, on))
    # condenser back
    c.line([(tx - 120, ty), (600, ty), (600, 680), (bx1, 680)], mix(BG, WATER, 0.9), 10)
    c.rect(530, 570, 670, 630, fill=mix(BG, (90, 150, 220), 0.6), outline=(90, 150, 220), width=3, r=10)
    c.text(600, 600, '④ 冷凝器', 'bold', 22, INK, 'mm')
    # moving steam puffs along pipe
    path = [(bx1 - 60, by0), (bx1 - 60, 300), (760, 300), (760, 420)]
    L = [math.dist(path[k], path[k + 1]) for k in range(3)]
    tot = sum(L)
    for k in range(6):
        d = ((t * 260) + k * tot / 6) % tot
        for j in range(3):
            if d <= L[j]:
                f = d / L[j]
                x = path[j][0] + (path[j + 1][0] - path[j][0]) * f
                y = path[j][1] + (path[j + 1][1] - path[j][1]) * f
                c.ellipse(x, y, 10, 10, fill=INK)
                break
            d -= L[j]
    a = fade(t, 14, 15)
    c.rect(1320, 770, 1860, 960, fill=mix(BG, SHEET, a), r=14)
    c.text(1350, 805, '煤里的热，大约只有', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1350, 855, '三到四成变成电', 'bold', 34, mix(BG, SPARK, a), 'lm')
    c.text(1350, 902, '其余随冷却水和烟气散掉', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1350, 937, '（核电站只是把锅炉换成反应堆）', 'sans', 22, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 5, '锅炉把水烧成高压蒸汽；安全阀守着，压力一超就放气'),
                (5.2, 10, '蒸汽冲向汽轮机的叶片，把它吹得飞转'),
                (10.2, 14, '汽轮机带着发电机转：就是第 04 集的磁生电'),
                (14.2, 22, '用过的蒸汽在冷凝器里变回水，再送回锅炉：今天大多数电，都是这么来的')], y=1010)

# ---------------------------------------------------------------- E19 煤与焦炭
def e19_coking(c, t, i):
    corner_tag(c, '第 19 集 · 炼焦')
    c.text(60, 96, '把煤「闷着烧」，跑掉了什么？', 'serif', 40, INK)
    ox0, oy0, ox1, oy1 = 300, 300, 1000, 760
    c.rect(ox0, oy0, ox1, oy1, outline=(150, 110, 80), width=10, r=8)
    c.text((ox0 + ox1) / 2, oy0 - 40, '隔绝空气加热（炼焦炉）', 'bold', 28, (200, 150, 110), 'mm')
    flames(c, ox0, ox1, oy1 + 70, t, 60)
    prog = fade(t, 3, 14)
    rnd = random.Random(11)
    for k in range(48):
        col_, row = k % 8, k // 8
        x = ox0 + 60 + col_ * 80
        y = oy0 + 90 + row * 70
        col = mix(COAL, COKE, prog)
        r = 30
        c.ellipse(x, y, r, r, fill=col)
        if prog > 0.3:
            for h in range(3):
                hx = x + rnd.uniform(-14, 14); hy = y + rnd.uniform(-14, 14)
                c.ellipse(hx, hy, 4 * prog, 4 * prog, fill=mix(col, BG, 0.6))
    # gases leaving
    if 2 < t < 16:
        for k in range(12):
            d = ((t - 2) * 60 + k * 18) % 210
            x = ox1 + 60 + d * 0.3 + 15 * math.sin(t * 4 + k)
            y = oy0 + 40 - d
            col = [(200, 200, 120), (140, 120, 90), (220, 220, 220)][k % 3]
            c.ellipse(x, y, 10, 10, fill=col)
        c.line([(ox1, oy0 + 40), (ox1 + 60, oy0 + 40)], MUTED, 8)
    a = fade(t, 4, 5)
    c.rect(1150, 230, 1860, 560, fill=mix(BG, SHEET, a), r=14)
    c.text(1180, 280, '跑掉的：', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(1180, 335, '· 煤气（可以燃烧）', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1180, 385, '· 煤焦油（黑色黏稠）', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1180, 435, '· 一部分硫', 'sans', 26, mix(BG, SPARK, a), 'lm')
    c.text(1180, 500, '这就是烧煤冒黄烟、有怪味的东西', 'sans', 22, mix(BG, MUTED, a), 'lm')
    b = fade(t, 12, 13)
    c.rect(1150, 600, 1860, 860, fill=mix(BG, SHEET, b), r=14)
    c.text(1180, 650, '留下的：焦炭', 'bold', 30, mix(BG, INK, b), 'lm')
    c.text(1180, 705, '· 几乎是纯碳，满是小孔', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1180, 755, '· 烧起来火旺、少烟', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1180, 805, '· 比木炭结实，压不碎', 'sans', 26, mix(BG, SPARK, b), 'lm')
    caps(c, t, [(0, 4, '把煤关进炉子里，隔绝空气加热：它烧不起来，只能被「烤」'),
                (4.2, 12, '煤里的煤气、煤焦油和一部分硫，变成烟跑掉了'),
                (12.2, 22, '剩下一块块灰色、多孔、很结实的东西：焦炭。这一步，叫炼焦')], y=1010)

def e19_column(c, t, i):
    corner_tag(c, '第 19 集 · 高炉里的柱子')
    c.text(60, 96, '高炉越造越高，为什么非用焦炭不可？', 'serif', 40, INK)
    for k, (cx, title, col, crush, note) in enumerate([(560, '木炭', CHAR, 0.55, '底下被压碎，堵住风道'), (1360, '焦炭', COKE, 0.05, '撑得住，风能穿过去')]):
        a = fade(t, 0.5 + k * 1, 1.5 + k * 1)
        if a <= 0: continue
        sq = fade(t, 4, 12) * crush
        H = 620
        x0, x1 = cx - 200, cx + 200
        ybot = 900
        c.line([(x0, ybot - H), (x0 - 40, ybot)], mix(BG, MUTED, a), 6)
        c.line([(x1, ybot - H), (x1 + 40, ybot)], mix(BG, MUTED, a), 6)
        c.text(cx, ybot - H - 50, title, 'bold', 34, mix(BG, INK, a), 'mm')
        rows = 10
        y = ybot - 10
        for r in range(rows):
            depth = 1 - r / rows
            rh = 56 * (1 - sq * depth)
            y -= rh
            w = 360 + 40 * (1 - r / rows)
            nx = 5
            for j in range(nx):
                px = cx - w / 2 + (j + 0.5) * w / nx
                c.ellipse(px, y + rh / 2, w / nx / 2 - 4, max(4, rh / 2 - 2), fill=mix(BG, col if r % 2 else (130, 90, 70), a))
        # air arrows at bottom
        flow = 1 - crush * fade(t, 4, 12) * 1.5
        for j in range(3):
            yy = ybot - 60 - ((t * 140 * max(0.15, flow) + j * 150) % (H - 120))
            c.arrow(cx - 60 + j * 60, yy + 40, cx - 60 + j * 60, yy, mix(BG, FIELD, a * max(0.2, flow)), 5, 14)
        b = fade(t, 12, 13)
        c.text(cx, ybot + 50, note, 'bold', 28, mix(BG, NRED if k == 0 else GREEN, b), 'mm')
    caps(c, t, [(0, 4, '高炉里一层矿石、一层燃料，从上往下堆，风从下往上鼓'),
                (4.2, 12, '炉子越高，下面压得越重：木炭被压碎，碎末堵住风道；焦炭硬，撑得住'),
                (12.2, 22, '煤里的硫会让铁「热脆」，一锻就裂；先炼成焦炭，硫少了，柱子也撑住了')], y=1010)

# ---------------------------------------------------------------- E21 玻璃
def e21_melt(c, t, i):
    corner_tag(c, '第 21 集 · 熔点')
    c.text(60, 96, '沙子要多热才化？加一把灰呢？', 'serif', 40, INK)
    x0, x1, y0 = 200, 1720, 800
    def X(T): return x0 + (x1 - x0) * T / 1800
    c.line([(x0, y0), (x1, y0)], MUTED, 3)
    for T in range(0, 1801, 300):
        c.line([(X(T), y0), (X(T), y0 + 12)], MUTED, 3)
        c.text(X(T), y0 + 40, f'{T} ℃', 'mono', 22, MUTED, 'mm')
    # kiln max band
    a = fade(t, 1, 2)
    c.rect(X(1200), 230, X(1300), y0, fill=mix(BG, COPPER, 0.25 * a))
    c.text(X(1250), 210, '宋代窑炉', 'bold', 24, mix(BG, COPPER, a), 'mm')
    c.text(X(1250), 245, '约 1200–1300 ℃', 'sans', 20, mix(BG, COPPER, a), 'mm')
    bars = [('纯石英砂', 1700, 380, NRED, 3), ('砂 + 草木灰 / 纯碱', 1000, 560, GREEN, 9)]
    for name, T, y, col, st in bars:
        b = fade(t, st, st + 3)
        if b <= 0: continue
        c.rect(x0, y - 30, x0 + (X(T) - x0) * ease(b), y + 30, fill=mix(BG, col, 0.7), r=8)
        c.text(x0 + 10, y - 60, name, 'bold', 28, mix(BG, INK, b), 'lm')
        if b > 0.9:
            c.text(X(T) + 16, y, f'约 {T} ℃ 起才熔得动', 'sans', 24, INK, 'lm')
    d = fade(t, 14, 15)
    c.text(960, 900, '助熔剂（草木灰里的碱、纯碱）把石英的熔点拉低几百度 —— 炉子才够得着（数字为量级，拍摄前核对）', 'sans', 24, mix(BG, SPARK, d), 'mm')
    caps(c, t, [(0, 3, '玻璃的主要原料就是沙子，也就是石英'),
                (3.2, 9, '纯石英要一千七百度左右才熔化：古代的炉子够不着'),
                (9.2, 14, '掺进草木灰或纯碱，一千度上下就能熔成玻璃液'),
                (14.2, 22, '这种「帮着熔化」的东西，叫助熔剂')], y=1010)

def lattice(c, cx, cy, ordered, a, t, seed=1):
    rnd = random.Random(seed)
    for r in range(6):
        for k in range(7):
            x = cx - 180 + k * 60
            y = cy - 150 + r * 60
            if not ordered:
                x += rnd.uniform(-22, 22); y += rnd.uniform(-22, 22)
            c.ellipse(x, y, 16, 16, fill=mix(BG, FIELD if (r + k) % 2 else STEAM, a))

def e21_amorphous(c, t, i):
    corner_tag(c, '第 21 集 · 来不及排队')
    c.text(60, 96, '同样是二氧化硅，为什么沙子不透明、玻璃透明？', 'serif', 40, INK)
    a = fade(t, 0.5, 1.5)
    # left: slow cooling -> crystals with many grains (sand)
    lx, rx, cy = 520, 1400, 470
    c.text(lx, 220, '慢慢冷：原子排好队 → 晶体', 'bold', 28, mix(BG, INK, a), 'mm')
    lattice(c, lx, cy, True, a, t)
    b = fade(t, 6, 7)
    c.text(rx, 220, '冷得快：来不及排队 → 玻璃', 'bold', 28, mix(BG, INK, b), 'mm')
    if b > 0:
        lattice(c, rx, cy, False, b, t, 5)
    d = fade(t, 12, 13)
    c.rect(200, 700, 1720, 940, fill=mix(BG, SHEET, d), r=14)
    c.text(960, 745, '一块石英晶体本来是透明的；沙子发白，是因为无数小颗粒的表面把光乱反射', 'sans', 26, mix(BG, INK, d), 'mm')
    c.text(960, 800, '熔成一整块、里面没有颗粒的边界，光就能直直穿过去', 'sans', 26, mix(BG, INK, d), 'mm')
    c.text(960, 870, '玻璃：凝固的液体，原子乱而不散', 'bold', 34, mix(BG, SPARK, d), 'mm')
    caps(c, t, [(0, 6, '熔化的石英慢慢冷却，原子有时间排成整整齐齐的晶体'),
                (6.2, 12, '冷得太快，原子来不及排队就被冻住了：乱糟糟的，这就是玻璃'),
                (12.2, 22, '一整块、没有颗粒的边界，光就能穿过去；磨碎了，又会发白')], y=1010)

CLIPS = {
 'E10_一千七百倍': (e10_expand, 22), 'E10_火电厂': (e10_plant, 22),
 'E10_片头': (titles.opening(SER7, VOL7, S7A, 6, '穿越北宋 · 只用动画：把开水变成电'), 7),
 'E10_片尾': (titles.closing(SER7, VOL7, S7A, 6, '下集：有煤，为什么还要先炼成焦炭？'), 7),
 'E19_炼焦': (e19_coking, 22), 'E19_高炉的柱子': (e19_column, 22),
 'E19_片头': (titles.opening(SER7, VOL7, S7A, 7, '北宋 · 汴京数百万家烧石炭'), 7),
 'E19_片尾': (titles.closing(SER7, VOL7, S7A, 7, '下集：沙子怎么变透明？'), 7),
 'E21_熔点': (e21_melt, 22), 'E21_来不及排队': (e21_amorphous, 22),
 'E21_片头': (titles.opening(SER7, VOL7, S7A, 8, '穿越北宋 · 把沙子烧成透明'), 7),
 'E21_片尾': (titles.closing(SER7, VOL7, S7A, 8, '下集：发霉的面包，怎么变成救命药？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
