"""第十季（第二层 · 下：材料、机械与日常）第一批：E62 钢、E63 钢筋混凝土、E64 螺丝与标准件 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S10A = [('62', '钢'), ('63', '钢筋混凝土'), ('64', '螺丝'), ('65', '印刷机'), ('66', '自行车'),
        ('67', '化肥'), ('68', '制冷'), ('69', '抽水马桶'), ('70', '避雷针'), ('71', '计算尺')]
SER10, VOL10 = '从零造物', '第十季 · 第二层（下）：材料、机械与日常'
IRON = (130, 135, 145)
HOT = (235, 110, 40)
CONC = (170, 165, 155)
STEELC = (95, 110, 130)
CARB = COPPER

# ---------------------------------------------------------------- E62 钢
ZONES = [(0.0, 0.08, '熟铁', '软：能锻打、能弯', (150, 160, 175)),
         (0.08, 2.1, '钢', '又硬又韧：能淬火', (110, 150, 200)),
         (2.1, 4.5, '生铁', '硬而脆：只能浇铸', (120, 110, 105))]

def e62_carbon(c, t, i):
    corner_tag(c, '第 62 集 · 含碳量')
    c.text(60, 96, '熟铁、钢、生铁，差的只是一点点碳', 'serif', 40, INK)
    x0, x1, y = 200, 1720, 330
    def X(p):  # stretch the first part so the zones are readable
        return x0 + (x1 - x0) * math.sqrt(p / 4.5)
    for k, (a0, a1, name, desc, col) in enumerate(ZONES):
        a = fade(t, 0.5 + k * 1.6, 1.5 + k * 1.6)
        c.rect(X(a0), y - 40, X(a1), y + 40, fill=mix(BG, col, 0.85 * a), r=4)
        mx = (X(a0) + X(a1)) / 2
        c.text(mx, y - 80, name, 'bold', 34, mix(BG, INK, a), 'mm')
        c.text(mx, y + 80, desc, 'sans', 24, mix(BG, MUTED, a), 'mm')
        # lattice with carbon atoms
        rnd = random.Random(k)
        gx0 = mx - 150
        nC = [1, 5, 16][k]
        spots = rnd.sample([(r, q) for r in range(5) for q in range(7)], nC)
        for r in range(5):
            for q in range(7):
                px, py = gx0 + q * 50, 520 + r * 50
                c.ellipse(px, py, 16, 16, fill=mix(BG, IRON, a))
        for (r, q) in spots:
            c.ellipse(gx0 + q * 50 + 25, 520 + r * 50 + 25, 9, 9, fill=mix(BG, CARB, a))
    for p in [0, 0.08, 0.5, 1, 2.1, 3, 4.5]:
        c.line([(X(p), y + 40), (X(p), y + 52)], MUTED, 2)
        c.text(X(p), y + 120, f'{p:g}%', 'mono', 20, MUTED, 'mm')
    c.text(1720, y + 160, '含碳量（质量百分比，刻度已拉伸）', 'sans', 20, MUTED, 'rm')
    b = fade(t, 13, 14)
    c.rect(200, 820, 1720, 900, fill=mix(BG, SHEET, b), r=10)
    c.text(230, 860, '北宋「灌钢」：把熔化的生铁浇进熟铁里，碳从多的一边跑到少的一边 → 钢（《梦溪笔谈》，拍摄前核对）', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(1720, 790, '灰点 = 铁原子，铜色点 = 碳原子（示意）', 'sans', 20, mix(BG, MUTED, fade(t, 5, 6)), 'rm')
    caps(c, t, [(0, 5, '纯铁很软。碳原子挤进铁原子之间，铁就变硬'),
                (5.2, 12.5, '碳很少是熟铁，能锻打；碳多到百分之二以上是生铁，硬却脆；中间那一段，就是钢'),
                (12.7, 22, '北宋的工匠没有化学式，却会把生铁和熟铁合在一起，凑出中间的含碳量')], y=1010)

def bend_pin(c, x, y, ang, col, broken=False, a=1.0):
    L = 220
    c.line([(x, y), (x, y - L * 0.5)], mix(BG, col, a), 8)
    if broken:
        c.line([(x + 30, y - L * 0.5 + 40), (x + 30, y - L)], mix(BG, col, a), 8)
        c.text(x + 60, y - L * 0.5 + 10, '咔', 'serif', 40, mix(BG, NRED, a), 'lm')
    else:
        ex = x + L * 0.5 * math.sin(ang)
        ey = y - L * 0.5 - L * 0.5 * math.cos(ang)
        c.line([(x, y - L * 0.5), (ex, ey)], mix(BG, col, a), 8)

def e62_quench(c, t, i):
    corner_tag(c, '第 62 集 · 淬火与回火')
    c.text(60, 96, '同样烧红，冷却方式不同，脾气就不同', 'serif', 40, INK)
    cols = [('烧红后慢慢冷', '软：弯了就回不来', 'slow'), ('烧红后浸水（淬火）', '硬而脆：一弯就断', 'quench'), ('淬火后再微微加热（回火）', '硬又有弹性：弯了会弹回', 'temper')]
    for k, (title, res, mode) in enumerate(cols):
        x0 = 120 + k * 590
        a = fade(t, 0.5 + k * 0.8, 1.3 + k * 0.8)
        c.text(x0 + 240, 190, title, 'bold', 28, mix(BG, INK, a), 'mm')
        # temperature-time graph
        gx0, gx1, gy0, gy1 = x0, x0 + 480, 230, 520
        c.line([(gx0, gy1), (gx1, gy1)], mix(BG, MUTED, a), 2)
        c.line([(gx0, gy0), (gx0, gy1)], mix(BG, MUTED, a), 2)
        c.text(gx0 - 10, gy0 + 20, '800°C', 'mono', 18, mix(BG, MUTED, a), 'rm')
        prog = fade(t, 2, 10)
        def T(u):
            if u < 0.25: return u / 0.25
            if mode == 'slow': return math.exp(-(u - 0.25) * 4)
            q = math.exp(-(u - 0.25) * 40)
            if mode == 'temper' and u > 0.55:
                q = max(q, 0.38 * math.sin(math.pi * min(1, (u - 0.55) / 0.35)))
            return q
        pts = [(gx0 + (gx1 - gx0) * j / 100, gy1 - (gy1 - gy0 - 20) * T(j / 100)) for j in range(int(100 * prog) + 1)]
        if len(pts) > 1:
            seg(c, pts, mix(BG, HOT, a), 4)
        c.text(gx1, gy1 + 24, '时间 →', 'sans', 18, mix(BG, MUTED, a), 'rm')
        if mode == 'temper':
            c.text(gx0 + 300, gy1 - 150, '约 300°C 回火，表面变蓝', 'sans', 20, mix(BG, MUTED, fade(t, 7, 8)), 'mm')
        # bending test
        b = fade(t, 11, 12)
        if b > 0:
            w = fade(t, 12, 16)
            if mode == 'slow':
                bend_pin(c, x0 + 240, 870, 1.2 * w, STEELC, a=b)
            elif mode == 'quench':
                bend_pin(c, x0 + 240, 870, 0.15 * w, STEELC, broken=w > 0.6, a=b)
            else:
                back = fade(t, 16, 17.5)
                bend_pin(c, x0 + 240, 870, 0.9 * w * (1 - back), STEELC, a=b)
            r = fade(t, 16.5, 17.5)
            c.text(x0 + 240, 920, res, 'bold', 26, mix(BG, [MUTED, NRED, GREEN][k], r), 'mm')
    caps(c, t, [(0, 10, '三根一样的钢发卡，都烧到发红：一根慢慢冷，一根猛地浸进水里，一根浸水后再微微加热'),
                (10.2, 17, '慢冷的软，一弯就弯；淬火的硬，可是一弯就断；回火的又硬又能弹回来'),
                (17.2, 22, '急冷时碳原子来不及跑开，把晶体卡住了：这就是淬火变硬的秘密')], y=1010)

# ---------------------------------------------------------------- E63 钢筋混凝土
def beam_pts(x0, x1, y, h, sag):
    top = [(x0 + (x1 - x0) * j / 40, y + sag * math.sin(math.pi * j / 40)) for j in range(41)]
    bot = [(px, py + h) for px, py in top]
    return top, bot

def e63_bend(c, t, i):
    corner_tag(c, '第 63 集 · 上压下拉')
    c.text(60, 96, '一根梁被压弯时，上面和下面受的力相反', 'serif', 40, INK)
    x0, x1, y, h = 300, 1620, 400, 160
    load = fade(t, 1, 8)
    sag = 40 * ease(load)
    top, bot = beam_pts(x0, x1, y, h, sag)
    c.poly(top + bot[::-1], mix(BG, CONC, 0.8))
    seg(c, top, CONC, 3); seg(c, bot, CONC, 3)
    for sx in (x0 + 40, x1 - 40):
        c.poly([(sx, y + h + 4), (sx - 40, y + h + 70), (sx + 40, y + h + 70)], MUTED)
    mx = (x0 + x1) / 2
    c.arrow(mx, y - 180, mx, y - 10 + sag, INK, 6, 22)
    c.text(mx + 20, y - 170, '重物', 'bold', 28, INK, 'lm')
    a = fade(t, 5, 6)
    if a > 0:
        for k in range(-4, 5):
            px = mx + k * 110
            yy = y + sag * math.sin(math.pi * (px - x0) / (x1 - x0))
            c.arrow(px - 40, yy + 30, px - 8, yy + 30, mix(BG, FIELD, a), 3, 10)
            c.arrow(px + 40, yy + 30, px + 8, yy + 30, mix(BG, FIELD, a), 3, 10)
            c.arrow(px - 8, yy + h - 30, px - 40, yy + h - 30, mix(BG, NRED, a), 3, 10)
            c.arrow(px + 8, yy + h - 30, px + 40, yy + h - 30, mix(BG, NRED, a), 3, 10)
        c.text(x1 + 30, y + 30, '上面：被挤压', 'bold', 26, mix(BG, FIELD, a), 'lm')
        c.text(x1 + 30, y + h + 10, '下面：被拉长', 'bold', 26, mix(BG, NRED, a), 'lm')
    cr = fade(t, 11, 15)
    if cr > 0:
        cy0 = y + h + sag
        pts = [(mx, cy0), (mx - 10, cy0 - 40 * cr), (mx + 8, cy0 - 80 * cr), (mx - 4, cy0 - 120 * cr)]
        seg(c, pts, NRED, 5)
        c.text(mx, cy0 + 50, '裂缝从下面开始', 'bold', 28, NRED, 'mm')
    b = fade(t, 15, 16)
    c.rect(300, 780, 1620, 880, fill=mix(BG, SHEET, b), r=10)
    c.text(330, 830, '混凝土：压，扛得住；拉，大约只扛得住压的十分之一', 'sans', 28, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 6, '梁的中间挂上重物，整根梁往下弯'),
                (6.2, 12, '弯的时候，上面一层被挤短，下面一层被拉长'),
                (12.2, 22, '混凝土很能扛压，却怕拉：所以裂缝总是从梁的下面先开')], y=1010)

BEAMS = [('不加铁丝', None, 2), ('铁丝埋在下面', 'bot', 9), ('铁丝埋在上面', 'top', 3)]

def e63_rebar(c, t, i):
    corner_tag(c, '第 63 集 · 钢筋放在哪儿')
    c.text(60, 96, '同一根铁丝，放对地方才有用', 'serif', 40, INK)
    load = 8 * fade(t, 1.5, 15)
    c.text(1840, 96, f'挂上 {load:.0f} 瓶水', 'mono', 32, INK, 'rm')
    for k, (name, pos, cap) in enumerate(BEAMS):
        y = 250 + k * 240
        x0, x1, h = 520, 1500, 80
        broke = load >= cap
        bt = max(0.0, min(1.0, (load - cap) * 2)) if broke else 0
        sag = 18 * min(load, cap) / 8 + (60 * bt if pos != 'bot' else 0)
        c.text(470, y + 40, name, 'bold', 28, INK, 'rm')
        if broke and pos != 'bot':
            mx = (x0 + x1) / 2
            drop = 110 * bt
            c.poly([(x0, y), (mx - 6, y + drop), (mx - 6, y + h + drop), (x0, y + h)], mix(BG, CONC, 0.8))
            c.poly([(mx + 6, y + drop), (x1, y), (x1, y + h), (mx + 6, y + h + drop)], mix(BG, CONC, 0.8))
            if pos == 'top':
                c.line([(x0 + 20, y + 16), (mx, y + 16 + drop), (x1 - 20, y + 16)], STEELC, 4)
            c.text(1540, y + 40, f'{cap:g} 瓶时断了', 'bold', 26, NRED, 'lm')
        else:
            top, bot = beam_pts(x0, x1, y, h, sag)
            c.poly(top + bot[::-1], mix(BG, CONC, 0.8))
            if pos:
                yy = 16 if pos == 'top' else h - 16
                pts = [(px, py + yy) for px, py in top]
                seg(c, pts, STEELC, 5)
            if pos == 'bot':
                c.text(1540, y + 40, '还扛着' if load < 8 else '8 瓶也没断', 'bold', 26, GREEN, 'lm')
        for sx in (x0 + 20, x1 - 20):
            c.poly([(sx, y + h + 22), (sx - 22, y + h + 60), (sx + 22, y + h + 60)], MUTED)
    caps(c, t, [(0, 5, '三根一样的小梁：一根不加，一根把铁丝埋在下面，一根把铁丝埋在上面'),
                (5.2, 15, '一瓶一瓶往中间挂水：不加的和铁丝在上面的，很快就从下面裂开'),
                (15.2, 22, '铁丝埋在受拉的下面，钢扛拉、混凝土扛压，两样东西各管一半（数字为示意，以实测为准）')], y=1010)

# ---------------------------------------------------------------- E64 螺丝
def e64_helix(c, t, i):
    corner_tag(c, '第 64 集 · 绕起来的斜面')
    c.text(60, 96, '一张三角形的纸，卷起来就是螺纹', 'serif', 40, INK)
    # triangle
    a = fade(t, 0.5, 1.5)
    tx0, ty0, W, Hh = 140, 760, 620, 300
    c.poly([(tx0, ty0), (tx0 + W, ty0), (tx0 + W, ty0 - Hh)], mix(BG, (220, 205, 170), a))
    c.line([(tx0, ty0), (tx0 + W, ty0 - Hh)], mix(BG, NRED, a), 5)
    c.text(tx0 + W / 2, ty0 + 36, '底边 = 绕圆柱 4 圈的长度', 'sans', 22, mix(BG, MUTED, a), 'mm')
    c.text(tx0 + W + 16, ty0 - Hh / 2, '高', 'sans', 22, mix(BG, MUTED, a), 'lm')
    # cylinder
    cx, cy0, cy1, r = 1050, 260, 820, 110
    c.rect(cx - r, cy0, cx + r, cy1, fill=mix(BG, (200, 190, 160), 0.6))
    c.ellipse(cx, cy0, r, 26, fill=mix(BG, (210, 200, 170), 0.8))
    turns = 4
    w = fade(t, 3, 12)
    pts = []
    N = int(400 * w)
    for j in range(N + 1):
        u = j / 400 * turns * 2 * math.pi
        x = cx + r * math.sin(u)
        y = cy1 - (cy1 - cy0 - 40) * j / 400 + 26 * math.cos(u) * 0.0
        if math.cos(u) >= 0:
            pts.append((x, y))
        else:
            if len(pts) > 1: seg(c, pts, NRED, 5)
            pts = []
    if len(pts) > 1: seg(c, pts, NRED, 5)
    p = (cy1 - cy0 - 40) / turns
    b = fade(t, 12, 13)
    c.line([(cx + r + 30, cy1), (cx + r + 30, cy1 - p)], mix(BG, INK, b), 3)
    c.text(cx + r + 46, cy1 - p / 2, '螺距：转一圈前进的距离', 'bold', 24, mix(BG, INK, b), 'lm')
    d = fade(t, 15, 16)
    c.rect(1480, 200, 1860, 500, fill=mix(BG, SHEET, d), r=10)
    c.text(1510, 240, '手柄转一圈走 31 厘米', 'sans', 22, mix(BG, INK, d), 'lm')
    c.text(1510, 280, '螺丝只前进 0.8 毫米', 'sans', 22, mix(BG, INK, d), 'lm')
    c.text(1510, 340, '理想放大约 390 倍', 'bold', 26, mix(BG, GREEN, d), 'lm')
    c.text(1510, 400, '（摩擦会吃掉一大半；', 'sans', 20, mix(BG, MUTED, d), 'lm')
    c.text(1510, 430, '手柄直径 10 厘米、M5 螺丝）', 'sans', 20, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 3, '第 39 集的斜面：坡越缓，推上去越省力'),
                (3.2, 12, '把一条斜边绕在圆柱上，斜面就变成了一圈圈的螺纹'),
                (12.2, 22, '转一大圈只前进一个螺距：走的路长了，力就放大了')], y=1010)

def thread(c, x0, x1, y, pitch, amp, col, w=4, phase=0.0):
    pts = []
    x = x0
    k = 0
    while x <= x1:
        pts.append((x, y + (amp if k % 2 else -amp)))
        x = x0 + phase + (k + 1) * pitch / 2
        k += 1
    seg(c, pts, col, w)

def e64_standard(c, t, i):
    corner_tag(c, '第 64 集 · 统一的螺纹')
    c.text(60, 96, '螺丝和螺母要配得上，螺距和角度都得一样', 'serif', 40, INK)
    a = fade(t, 0.5, 1.5)
    c.text(140, 210, '1841 年以前：每个作坊各做各的', 'bold', 30, mix(BG, INK, a), 'lm')
    shops = [('甲作坊的螺丝', 46, NRED), ('乙作坊的螺母', 58, FIELD)]
    for k, (name, p, col) in enumerate(shops):
        b = fade(t, 1 + k, 2 + k)
        c.text(140, 300 + k * 90, name, 'sans', 24, mix(BG, col, b), 'lm')
    b = fade(t, 1, 3)
    thread(c, 420, 1500, 300, 46, 26, mix(BG, NRED, b))
    thread(c, 420, 1500, 300 + 90 * (1 - fade(t, 4, 7)), 58, 26, mix(BG, FIELD, b))
    m = fade(t, 7, 8)
    c.text(1540, 330, '对不上', 'bold', 30, mix(BG, NRED, m), 'lm')
    d = fade(t, 9, 10)
    c.text(140, 520, '惠特沃斯：统一螺纹角度和每英寸牙数', 'bold', 30, mix(BG, INK, d), 'lm')
    e = fade(t, 10, 11)
    thread(c, 420, 1500, 620, 52, 26, mix(BG, GREEN, e))
    thread(c, 420, 1500, 620 + 90 * (1 - fade(t, 11, 14)), 52, 26, mix(BG, COPPER, e), 3)
    c.text(1540, 650, '拧得进', 'bold', 30, mix(BG, GREEN, fade(t, 14, 15)), 'lm')
    f = fade(t, 15.5, 16.5)
    c.rect(140, 780, 1780, 900, fill=mix(BG, SHEET, f), r=10)
    c.text(170, 820, '今天：M5 = 直径 5 毫米、螺距 0.8 毫米、牙型角 60°，全世界的 M5 螺母都能互换', 'sans', 26, mix(BG, INK, f), 'lm')
    c.text(170, 865, '标准让零件可以分开造、坏了随时换：这是大工厂的前提', 'sans', 24, mix(BG, MUTED, f), 'lm')
    caps(c, t, [(0, 8, '早年的螺丝都是手工配的：这家的螺丝，拧不进那家的螺母'),
                (8.2, 15, '1841 年，惠特沃斯提出统一的螺纹标准，牙型角 55 度，各尺寸规定好牙数（拍摄前核对）'),
                (15.2, 22, '同号的螺丝螺母随便拿一个都能配上：零件可以互换，机器才能大批量地造')], y=1010)

CLIPS = {
 'E62_含碳量': (e62_carbon, 22), 'E62_淬火': (e62_quench, 22),
 'E62_片头': (titles.opening(SER10, VOL10, S10A, 0, '北宋 · 约 1090 年 · 铁匠铺'), 7),
 'E62_片尾': (titles.closing(SER10, VOL10, S10A, 0, '下集：混凝土梁，为什么要在下面埋钢筋？'), 7),
 'E63_上压下拉': (e63_bend, 22), 'E63_钢筋': (e63_rebar, 22),
 'E63_片头': (titles.opening(SER10, VOL10, S10A, 1, '1867 年 · 莫尼耶的花盆'), 7),
 'E63_片尾': (titles.closing(SER10, VOL10, S10A, 1, '下集：为什么同号的螺丝都能拧进螺母？'), 7),
 'E64_斜面': (e64_helix, 22), 'E64_标准': (e64_standard, 22),
 'E64_片头': (titles.opening(SER10, VOL10, S10A, 2, '1841 年 · 惠特沃斯的螺纹标准'), 7),
 'E64_片尾': (titles.closing(SER10, VOL10, S10A, 2, '下集：古腾堡改了什么，让书变便宜？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
