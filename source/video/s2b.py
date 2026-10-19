"""第二季第二批：B16 瓷器、E23 纸、B3 活字印刷 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s2a import S2A, SER, VOL, CLAY, flame

R = random.Random(16)

# ---------------------------------------------------------------- B16 瓷器
GRAINS = [(R.uniform(-1, 1), R.uniform(-1, 1), R.uniform(14, 24)) for _ in range(46)]

def micro(c, cx, cy, glass, t, label, temp, absorb, drop_t0):
    c.rect(cx - 330, 250, cx + 330, 750, fill=SHEET, r=18)
    c.text(cx, 210, label, 'serif', 44, INK, 'mm')
    c.text(cx, 790, temp, 'mono', 28, MUTED, 'mm')
    # pores (dark) then glass fills
    c.rect(cx - 300, 300, cx + 300, 700, fill=mix((40, 36, 34), (150, 190, 170), glass), r=10)
    for (u, v, r) in GRAINS:
        x, y = cx + u * 270, 500 + v * 170
        c.ellipse(x, y, r + 6 * glass, r * 0.8 + 5 * glass, fill=mix(CLAY, (232, 230, 220), glass))
    # water drop
    f = fade(t, drop_t0, drop_t0 + 3)
    if f > 0:
        if glass < 0.5:
            r = 50 * (1 - f)
            c.ellipse(cx, 300 - r * 0.6, r, r * 0.6, fill=mix(BG, FIELD, 0.85))
            for k in range(6):
                c.line([(cx - 60 + k * 24, 310), (cx - 70 + k * 26, 310 + 160 * f)], mix(BG, FIELD, 0.6 * f), 6)
        else:
            c.ellipse(cx, 274, 50, 26, fill=mix(BG, FIELD, 0.85))
    c.text(cx, 850, absorb, 'bold', 30, COPPER if glass < 0.5 else FIELD, 'mm')

def b16_vitrify(c, t, i):
    corner_tag(c, 'B16 · 玻化')
    c.text(60, 96, '同样是泥，为什么一个吸水、一个不吸水？', 'serif', 40, INK)
    g = fade(t, 8, 13)
    micro(c, 520, 500, 0.0, t, '陶', '约 900 ℃ 烧成', '颗粒之间留着孔：吸水', 4)
    micro(c, 1400, 500, g, t, '瓷', '约 1200–1300 ℃ 烧成', '孔被玻璃填满：几乎不吸水', 14)
    caps(c, t, [(0, 4, '放大看陶片：黏土颗粒烧结在一起，但中间留着许多小孔'),
                (4.2, 8, '水滴上去，顺着小孔钻进去 —— 陶会吸水'),
                (8.2, 14, '瓷烧得更热：一部分原料熔成玻璃，流进孔里，把孔填满'),
                (14.2, 24, '这叫玻化：水进不去，敲起来声音清脆，薄处还能透光')])

def bowl(c, cx, cy, sag, col):
    pts = []
    for k in range(21):
        a = math.pi * k / 20
        x = cx - 150 * math.cos(a)
        x = cx - (150 + 50 * sag) * math.cos(a)
        y = cy + 100 * (1 - 0.65 * sag) * math.sin(a) + 70 * sag
        pts.append((x, y))
    c.line(pts, col, 18)

def b16_recipe(c, t, i):
    corner_tag(c, 'B16 · 瓷土')
    c.text(60, 96, '为什么不是什么泥都能烧成瓷？', 'serif', 40, INK)
    T = 800 + 500 * fade(t, 2, 14)
    # thermometer
    c.rect(1700, 200, 1760, 860, outline=MUTED, width=3, r=30)
    h = (T - 700) / 700 * 620
    c.rect(1706, 856 - h, 1754, 856, fill=mix(SPARK, NRED, (T - 800) / 500), r=24)
    c.text(1680, 856 - h, f'{T:.0f} ℃', 'mono', 30, INK, 'rm')
    # two bowls
    sag1 = fade(T, 1150, 1280)
    bowl(c, 500, 520, sag1, mix(CLAY, (120, 70, 50), sag1))
    c.text(500, 300, '普通黏土', 'bold', 34, INK, 'mm')
    c.text(500, 760, '铁和杂质多：一千一二百度就软塌、起泡' if sag1 > 0.3 else '烧成陶没问题', 'sans', 26, NRED if sag1 > 0.3 else MUTED, 'mm')
    gl = fade(T, 1180, 1300)
    bowl(c, 1150, 520, 0, mix((214, 206, 190), (236, 240, 234), gl))
    c.text(1150, 300, '瓷土', 'bold', 34, INK, 'mm')
    c.text(1150, 760, '耐得住高温不变形' if gl < 0.5 else '形状不变，内部玻化', 'sans', 26, FIELD if gl > 0.5 else MUTED, 'mm')
    # ingredient legend
    a = fade(t, 15, 16)
    items = [('高岭土', '耐高温，撑住形状'), ('长石等', '高温下熔成玻璃，填满孔隙'), ('石英', '骨架')]
    for k, (n, d) in enumerate(items):
        c.text(300 + k * 480, 880, n, 'bold', 30, mix(BG, COPPER, a), 'mm')
        c.text(300 + k * 480, 925, d, 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '同样往窑里送，一碗普通黏土，一碗瓷土'),
                (6.2, 14, '温度过了一千二百度，普通黏土先软塌了；瓷土还稳稳地立着'),
                (14.2, 20, '瓷土的秘密在配方：一部分撑住形状，一部分熔成玻璃')], y=1010)

# ---------------------------------------------------------------- E23 纸
RF = random.Random(23)
FIB = [(RF.uniform(-1, 1), RF.uniform(-1, 1), RF.uniform(0, math.pi), RF.uniform(80, 150), RF.uniform(0, 6)) for _ in range(46)]

def fiber_pts(cx, cy, u, v, a, L, ph, spread, t, wob):
    x0 = cx + u * 520 * spread; y0 = cy + v * 240 * spread
    pts = []
    for k in range(9):
        s = (k / 8 - 0.5) * L
        w = 8 * math.sin(k + ph + t * 1.5 * wob)
        pts.append((x0 + s * math.cos(a) - w * math.sin(a), y0 + s * math.sin(a) + w * math.cos(a)))
    return pts

def seg_inter(p1, p2, p3, p4):
    d = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
    if abs(d) < 1e-9: return None
    ua = ((p4[0] - p3[0]) * (p1[1] - p3[1]) - (p4[1] - p3[1]) * (p1[0] - p3[0])) / d
    ub = ((p2[0] - p1[0]) * (p1[1] - p3[1]) - (p2[1] - p1[1]) * (p1[0] - p3[0])) / d
    if 0 <= ua <= 1 and 0 <= ub <= 1:
        return (p1[0] + ua * (p2[0] - p1[0]), p1[1] + ua * (p2[1] - p1[1]))
    return None

def crossings(fs):
    out = []
    for a in range(len(fs)):
        for b in range(a + 1, len(fs)):
            p = seg_inter(fs[a][0], fs[a][-1], fs[b][0], fs[b][-1])
            if p: out.append(p)
    return out

def e23_web(c, t, i):
    corner_tag(c, '第 23 集 · 纤维成网')
    c.text(60, 96, '一盆浆水，怎么变成一张纸？', 'serif', 40, INK)
    cy = 560
    lift = fade(t, 6, 11)
    dry = fade(t, 12, 17)
    water_top = 260 + 420 * lift
    c.rect(300, water_top, 1620, 860, fill=mix(BG, FIELD, 0.22 * (1 - dry)))
    # screen (帘)
    sy = 880 - 260 * lift
    c.line([(320, sy), (1600, sy)], MUTED, 6)
    for k in range(33):
        c.line([(320 + k * 40, sy - 6), (320 + k * 40, sy + 6)], MUTED, 2)
    c.text(1620, sy + 30, '竹帘', 'sans', 26, MUTED, 'rm')
    spread = 1.0 - 0.15 * lift
    cyy = cy + (sy - 120 - cy) * lift
    fs = []
    for (u, v, a, L, ph) in FIB:
        vv = v * (1 - 0.75 * lift)
        fs.append(fiber_pts(960, cyy, u, vv, a, L, ph, spread, t, 1 - lift))
    for p in fs:
        c.line(p, mix((210, 196, 160), (236, 228, 200), dry), 5)
    if dry > 0:
        for (x, y) in crossings(fs)[:120]:
            c.ellipse(x, y, 6 * dry, 6 * dry, fill=mix(BG, SPARK, dry))
    if t < 6:
        for k in range(30):
            x = 330 + (k * 137) % 1260; y = 300 + (k * 89) % 520
            c.ellipse(x + 10 * math.sin(t + k), y, 4, 4, fill=mix(BG, FIELD, 0.6))
    c.ellipse(1300, 180, 7, 7, fill=SPARK); c.text(1320, 180, '纤维相交处的氢键', 'sans', 26, mix(BG, INK, 0.4 + 0.6 * dry), 'lm')
    caps(c, t, [(0, 6, '打烂的植物纤维散在水里，像一盆细线'),
                (6.2, 12, '竹帘从下面一抄：水漏下去，纤维在帘上交错铺成一层'),
                (12.2, 18, '晾干时，纤维之间的水退出去，相交处的分子直接「手拉手」：氢键'),
                (18.2, 22, '成千上万个氢键，把纤维连成一张网 —— 纸')])

def e23_wet(c, t, i):
    corner_tag(c, '第 23 集 · 纸为什么怕水')
    c.text(60, 96, '干纸很结实，一沾水就一扯就破', 'serif', 40, INK)
    wet = fade(t, 5, 9)
    pull = fade(t, 10, 15)
    fs = []
    for k, (u, v, a, L, ph) in enumerate(FIB[:30]):
        side = -1 if u < 0 else 1
        shift = side * 120 * pull * wet
        p = fiber_pts(960 + shift, 560, u * 0.8, v * 0.9, a, L, ph, 1.0, 0, 0)
        fs.append(p)
    for p in fs:
        c.line(p, (226, 214, 180), 5)
    cr = crossings(fs)
    for (x, y) in cr:
        if wet < 0.5:
            c.ellipse(x, y, 6, 6, fill=SPARK)
        else:
            c.ellipse(x, y, 7, 7, fill=mix(BG, FIELD, 0.9))
    if wet > 0:
        for k in range(40):
            x = 520 + (k * 71) % 880; y = 360 + (k * 53) % 400
            c.ellipse(x, y, 4, 4, fill=mix(BG, FIELD, 0.5 * wet))
    if pull > 0:
        c.arrow(700, 900, 500, 900, NRED, 6, 18); c.arrow(1220, 900, 1420, 900, NRED, 6, 18)
    c.rect(1460, 200, 1860, 330, fill=SHEET, r=12)
    c.ellipse(1490, 240, 7, 7, fill=SPARK); c.text(1510, 240, '纤维之间的氢键', 'sans', 24, INK, 'lm')
    c.ellipse(1490, 290, 7, 7, fill=FIELD); c.text(1510, 290, '水分子挤进去', 'sans', 24, INK, 'lm')
    caps(c, t, [(0, 5, '干纸：每个交叉点都有氢键拉着'),
                (5.2, 10, '一沾水：水分子挤进纤维之间，抢走了氢键'),
                (10.2, 18, '再一拉，纤维轻轻一滑就分开了 —— 湿纸没有力气')])

# ---------------------------------------------------------------- B3 活字印刷
TEXT = '用胶泥刻字薄如钱唇每字为一印火烧令坚'
def b3_plate(c, t, i):
    corner_tag(c, 'B3 · 排版与拆版')
    c.text(60, 96, '一千年前的「可拆卸」排版', 'serif', 40, INK)
    X0, Y0, W, H = 360, 260, 840, 560
    heat1 = fade(t, 6, 8) * (1 - fade(t, 12, 13))
    heat2 = fade(t, 18, 19.5)
    heat = max(heat1, heat2)
    # iron plate + drug layer
    c.rect(X0 - 40, Y0 - 40, X0 + W + 40, Y0 + H + 40, fill=(70, 72, 76), r=10)
    c.rect(X0 - 20, Y0 - 20, X0 + W + 20, Y0 + H + 20, fill=mix((120, 96, 60), (200, 150, 80), heat), r=6)
    c.rect(X0 - 30, Y0 - 30, X0 + W + 30, Y0 + H + 30, outline=(150, 150, 156), width=8, r=8)
    if heat > 0:
        for k in range(5): flame(c, X0 + 80 + k * 170, Y0 + H + 120, 0.9, t + k, heat)
    # types
    n = len(TEXT)
    placed = fade(t, 0.5, 5.5) * n
    press = fade(t, 9, 10.5) * (1 - fade(t, 11.5, 12))
    fall = fade(t, 19.5, 22)
    for k, ch in enumerate(TEXT):
        if k >= placed: break
        col_i, row_i = k // 5, k % 5
        x = X0 + W - 90 - col_i * 200
        y = Y0 + 20 + row_i * 108
        jitter = 0 if t > 10.5 else (k % 3 - 1) * 8 * (1 - fade(t, 9, 10.5))
        dy = -fall * (40 + (k % 4) * 20)
        dx = 0
        fa = 1 - fall
        c.rect(x - 70 + dx, y + jitter + dy, x + 70 + dx, y + 92 + jitter + dy, fill=mix(BG, (178, 132, 96), fa), outline=mix(BG, (120, 86, 60), fa), width=3, r=6)
        c.text(x + dx, y + 46 + jitter + dy, ch, 'serif', 56, mix(BG, (60, 36, 24), fa), 'mm')
    if press > 0:
        yb = Y0 - 140 + 120 * press
        c.rect(X0 - 40, yb - 30, X0 + W + 40, yb, fill=mix(BG, WOODC, 0.95), r=6)
        c.text(X0 + W / 2, yb - 50, '平板一压：字面「平如砥」', 'bold', 28, INK, 'mm')
    # side panel
    px = 1330
    c.rect(px, 260, 1860, 820, fill=SHEET, r=16)
    steps = [(0.5, '① 胶泥刻字，火烧令坚'), (5.5, '② 铁板上铺松脂、蜡、纸灰'), (6.5, '③ 加热，药稍熔'), (9, '④ 平板压平'), (13, '⑤ 冷却固定，上墨印刷'), (18, '⑥ 再加热，「其印自落」')]
    for k, (t0, s_) in enumerate(steps):
        on = t >= t0
        c.text(px + 30, 320 + k * 82, s_, 'bold' if on else 'sans', 28, INK if on else MUTED, 'lm')
    caps(c, t, [(0, 6, '每个字刻成一个小泥块，烧硬：一字一印'),
                (6.2, 12, '铁板上铺一层松脂、蜡和纸灰，加热变软，把字压平'),
                (12.2, 18, '冷了就粘牢，可以上墨印刷'),
                (18.2, 24, '印完再加热，药一熔，字模就掉下来，下一页接着用')])
WOODC = (150, 110, 70)

def b3_cost(c, t, i):
    corner_tag(c, 'B3 · 为什么印得多才划算')
    c.text(60, 96, '「若止印三二本，未为简易」', 'serif', 40, INK)
    gx0, gx1, gy0, gy1 = 220, 1180, 220, 820
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2); c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text(gx1, gy1 + 36, '印多少本 →', 'sans', 26, MUTED, 'rm')
    c.text(gx0, gy0 - 30, '总共花的时间（示意）', 'sans', 26, MUTED, 'lm')
    f = fade(t, 0.5, 8)
    N = 10
    def X(n): return gx0 + n / N * (gx1 - gx0)
    def Y(v): return gy1 - v / 12 * (gy1 - gy0)
    hand = [(X(n), Y(1.1 * n)) for n in range(0, int(f * N) + 1)]
    mov = [(X(n), Y(2.5 + 0.15 * n)) for n in range(0, int(f * N) + 1)]
    if len(hand) > 1: c.line(hand, MUTED, 6); c.text(hand[-1][0] + 10, hand[-1][1], '手抄', 'bold', 28, MUTED, 'lm')
    if len(mov) > 1: c.line(mov, COPPER, 6); c.text(mov[-1][0] + 10, mov[-1][1] - 24, '活字', 'bold', 28, COPPER, 'lm')
    if t > 5:
        a = fade(t, 5, 6)
        xc = X(2.5 / 0.95)
        c.line([(xc, gy0), (xc, gy1)], mix(BG, SPARK, a), 2)
        c.text(xc + 10, gy0 + 20, '少于这里：活字反而慢（排版要时间）', 'sans', 24, mix(BG, SPARK, a), 'lm')
    # two plates pipeline
    a = fade(t, 9, 10)
    if a > 0:
        px, py = 1280, 260
        c.text(px, py - 20, '「常作二铁板」', 'serif', 34, mix(BG, INK, a), 'lm')
        for row, (lab, col0) in enumerate([('甲板', COPPER), ('乙板', FIELD)]):
            y = py + 60 + row * 110
            c.text(px, y + 30, lab, 'bold', 28, mix(BG, INK, a), 'lm')
            for k in range(4):
                x = px + 90 + k * 120
                job = (k + row) % 2
                prog = fade(t, 10 + k * 1.5, 11.4 + k * 1.5)
                c.rect(x, y, x + 110 * prog + 1, y + 60, fill=mix(BG, (col0 if job == 0 else MUTED), a * 0.9), r=6)
                if prog > 0.6:
                    c.text(x + 55, y + 30, '印刷' if job == 0 else '排字', 'sans', 22, BG, 'mm')
        c.text(px, py + 300, '一块在印，另一块同时排下一页', 'sans', 26, mix(BG, INK, a), 'lm')
        c.text(px, py + 345, '「更互用之，瞬息可就」', 'serif', 30, mix(BG, COPPER, a), 'lm')
    caps(c, t, [(0, 5, '活字要先花时间排版；印得越多，排版的时间就越不算什么'),
                (5.2, 9, '只印两三本：不如手抄；印几十几百本：「极为神速」'),
                (9.2, 20, '毕昇还准备两块铁板：一块印的时候，另一块已经在排下一页 —— 流水线')])

# ---------------------------------------------------------------- 片头片尾
SB2 = [('B16', '瓷器'), ('B3', '活字印刷'), ('B15', '酿酒酿醋'), ('B4', '水排')]
CLIPS = {
 'B16_玻化': (b16_vitrify, 24), 'B16_瓷土': (b16_recipe, 20),
 'B16_片头': (titles.opening(BSER, BVOL, SB2, 0, '东汉出现成熟青瓷 · 北宋名窑遍地'), 7),
 'B16_片尾': (titles.closing(BSER, BVOL, SB2, 0, '下集：回到 A 线，在家抄一张纸'), 7),
 'E23_纤维成网': (e23_web, 22), 'E23_湿纸无力': (e23_wet, 18),
 'E23_片头': (titles.opening(SER, VOL, S2A, 3, '西汉已有纸 · 东汉蔡伦改进（公元 105 年）'), 7),
 'E23_片尾': (titles.closing(SER, VOL, S2A, 3, '下集：有了纸，怎么印书？'), 7),
 'B3_排版拆版': (b3_plate, 24), 'B3_双板与成本': (b3_cost, 20),
 'B3_片头': (titles.opening(BSER, BVOL, SB2, 1, '北宋庆历年间 · 毕昇 · 沈括《梦溪笔谈》'), 7),
 'B3_片尾': (titles.closing(BSER, BVOL, SB2, 1, '下集：油加草木灰，为什么能去污？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
