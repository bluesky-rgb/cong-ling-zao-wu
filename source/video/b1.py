"""B 线第 1 集 · 指南鱼：原文卡、热剩磁动画、两种解释对比、片头片尾。"""
import math, random, sys
from lib import *
import titles

# ---------- 原文卡 ----------
LINES = [
    ('（指南）鱼法：用薄铁叶剪裁，长二寸、阔五分，首尾锐，如鱼形。', '把薄铁片剪成鱼形，约两寸长、半寸宽，头尾都是尖的。', '用薄铁叶剪裁'),
    ('置炭火中烧之。候通赤，以铁钤钤鱼首出火。', '放进炭火里烧，烧到通红，用铁钳夹住鱼头取出。', '以铁钤钤鱼首出火'),
    ('以尾正对子位，蘸水盆中，没尾数分则止。以密器收之。', '鱼尾正对北方，蘸进水盆，尾巴没入几分就停，再收进密闭的盒子。', '以尾正对子位'),
    ('用时置水碗于无风处，平放鱼在水面令浮，其首常南向午也。', '用时在无风处放一碗水，让鱼平浮在水面，鱼头总是指向南方。', '其首常南向午也'),
]

def draw_text(c, t, i):
    corner_tag(c, 'B 线 · 指南鱼 · 原文')
    c.text(960, 120, '北宋《武经总要》前集卷十五 · 约公元 1040–1044 年', 'sans', 28, mix(BG, MUTED, fade(t, 0, 0.8)), 'mm')
    for k, (orig, plain, key) in enumerate(LINES):
        t0 = 0.6 + k * 5.6
        a = fade(t, t0, t0 + 0.8)
        if a <= 0: continue
        y = 250 + k * 190
        active = t0 <= t < t0 + 5.6 or (k == 3 and t >= t0)
        col = INK if active else mix(BG, INK, 0.55)
        # draw original with key phrase highlighted
        pre, post = orig.split(key)
        w_total = c.textw(orig, 'serif', 44)
        x = 960 - w_total / 2
        for seg, hl in ((pre, False), (key, True), (post, False)):
            if not seg: continue
            cc = (mix(BG, COPPER, a) if active else mix(BG, COPPER, 0.5 * a)) if hl else mix(BG, col, a)
            c.text(x, y, seg, 'serif', 44, cc, 'lm')
            x += c.textw(seg, 'serif', 44)
        c.text(960, y + 62, plain, 'sans', 28, mix(BG, MUTED if not active else INK, a * (0.95 if active else 0.6)), 'mm')
    if t > 23.5:
        c.text(960, 1020, '注意：原文里有一步「用铁钳夹住鱼头」——后面会用到它', 'bold', 30, mix(BG, SPARK, fade(t, 23.5, 24.2)), 'mm')

# ---------- 热剩磁动画 ----------
random.seed(3)
FCX, FCY, FL, FW = 860, 520, 560, 150     # fish centre, half-length, half-width
FIELD_A = 0.0                             # field points to +x (tail / north)
def in_fish(x, y):
    u, v = (x - FCX) / FL, (y - FCY) / FW
    return abs(v) < (1 - abs(u)) ** 0.8 * 0.95 and abs(u) < 0.92
DOM = []
for gx in range(FCX - FL, FCX + FL, 62):
    for gy in range(FCY - FW, FCY + FW + 1, 58):
        if in_fish(gx, gy):
            th0 = (len(DOM) * 2.399963) % (2 * math.pi)
            fin = FIELD_A + random.gauss(0, 0.45)
            DOM.append([gx, gy, th0, fin, random.uniform(2, 5) * random.choice((-1, 1)), random.uniform(0, 6.28)])

def temp(t):
    if t < 4: return 20
    if t < 9: return 20 + 880 * ease((t - 4) / 5)
    if t < 10.5: return 900
    if t < 16: return 900 - 880 * ease((t - 10.5) / 5.5)
    return 20
TC = 770
T_FREEZE = 10.5 + 5.5 * 0.5  # approx when temp crosses 770 on the way down (computed below)
for k in range(1000):
    tt = 10.5 + k * 0.0055
    if temp(tt) < TC: T_FREEZE = tt; break
T_HOT = None
for k in range(1000):
    tt = 4 + k * 0.005
    if temp(tt) > TC: T_HOT = tt; break

def dom_angle(d, t):
    gx, gy, th0, fin, w, ph = d
    if t < T_HOT:
        return th0 + 0.06 * math.sin(t * 3 + ph)
    if t < T_FREEZE:
        return th0 + w * (t - T_HOT)
    # settle from spinning angle at freeze to final angle
    a_f = th0 + w * (T_FREEZE - T_HOT)
    # unwrap to nearest equivalent of fin
    target = fin + 2 * math.pi * round((a_f - fin) / (2 * math.pi))
    s = ease((t - T_FREEZE) / 1.2)
    return a_f + (target - a_f) * s + 0.03 * math.sin(t * 3 + ph) * (1 - s)

def draw_domains(c, t, i):
    corner_tag(c, 'B 线 · 指南鱼 · 热剩磁')
    c.text(60, 96, '铁鱼为什么会带上磁性？', 'serif', 40, INK)
    T = temp(t)
    hot = max(0.0, min(1.0, (T - 400) / 500))
    # fish body
    pts = []
    for k in range(121):
        u = -0.95 + 1.9 * k / 120
        pts.append((FCX + u * FL, FCY - (1 - abs(u)) ** 0.8 * FW * 1.15))
    for k in range(121):
        u = 0.95 - 1.9 * k / 120
        pts.append((FCX + u * FL, FCY + (1 - abs(u)) ** 0.8 * FW * 1.15))
    c.poly(pts, mix(mix(BG, MUTED, 0.28), (190, 60, 30), hot))
    c.text(FCX - FL - 20, FCY, '鱼头', 'sans', 26, MUTED, 'rm')
    c.text(FCX + FL + 20, FCY, '鱼尾', 'sans', 26, MUTED, 'lm')
    # field arrow
    fa = 0.35 + 0.65 * fade(t, T_FREEZE - 1.5, T_FREEZE)
    c.arrow(FCX - 260, 300, FCX + 260, 300, mix(BG, FIELD, fa), 5, 20)
    c.text(FCX, 262, '周围的磁场（指向北）', 'sans', 26, mix(BG, FIELD, fa), 'mm')
    # domains
    net = 0.0
    for d in DOM:
        a = dom_angle(d, t)
        net += math.cos(a - FIELD_A)
        L = 22
        col = mix(INK, SPARK, hot)
        c.arrow(d[0] - L * math.cos(a), d[1] - L * math.sin(a), d[0] + L * math.cos(a), d[1] + L * math.sin(a), col, 4, 11)
    net = max(0.0, net / len(DOM))
    # thermometer
    tx, ty0, ty1 = 1640, 200, 760
    c.rect(tx - 18, ty0, tx + 18, ty1, outline=LINE, width=3, r=18)
    h = (T - 0) / 1000 * (ty1 - ty0 - 20)
    c.rect(tx - 10, ty1 - 10 - h, tx + 10, ty1 - 10, fill=mix(FIELD, NRED, T / 900), r=10)
    yc = ty1 - 10 - TC / 1000 * (ty1 - ty0 - 20)
    c.line([(tx - 36, yc), (tx + 36, yc)], SPARK, 3)
    c.text(tx + 50, yc, '约 770°C', 'bold', 26, SPARK, 'lm')
    c.text(tx + 50, yc + 34, '超过就失去磁性', 'sans', 22, MUTED, 'lm')
    c.text(tx, ty1 + 40, f'{int(T)}°C', 'mono', 30, INK, 'mm')
    # net magnetisation meter
    c.rect(60, 820, 560, 900, fill=SHEET, r=12)
    c.text(84, 846, '整条鱼的磁性', 'sans', 24, MUTED, 'lm')
    c.rect(84, 870, 536, 884, fill=LINE, r=7)
    c.rect(84, 870, 84 + 452 * min(1, net / 1.55), 884, fill=COPPER, r=7)
    caps = [(0, 4.2, '常温下：铁里的小磁区各朝各的方向，整体不显磁性'),
            (4.6, 10.4, '烧到通红，超过约 770°C：小磁区彻底乱掉'),
            (10.8, 17.2, '冷却穿过 770°C 的那一刻：小磁区按周围的磁场「排队」'),
            (17.6, 24, '淬火把排好的队形「冻住」：整条鱼成了一块弱磁铁')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0:
            c.text(960, 1010, s_, 'bold', 38, mix(BG, INK, al), 'mm')

# ---------- 两种解释 ----------
def draw_two(c, t, i):
    corner_tag(c, 'B 线 · 指南鱼 · 两种解释')
    c.text(960, 110, '同一个原理，谁的磁场？', 'serif', 48, INK, 'mm')
    c.line([(960, 180), (960, 860)], LINE, 2)
    aL = fade(t, 0.5, 1.2); aR = fade(t, 3.5, 4.2)
    # left: earth field
    c.text(480, 220, '解释一：地磁场', 'bold', 36, mix(BG, FIELD, aL), 'mm')
    c.text(480, 268, '到处都有，但很弱', 'sans', 28, mix(BG, MUTED, aL), 'mm')
    for gy in range(360, 800, 70):
        if 520 < gy < 770: continue
        for gx in range(140, 860, 140):
            ph = (t * 40) % 140
            x = gx + ph - 70
            if 120 < x < 840:
                c.arrow(x - 30, gy - 10, x + 30, gy + 10, mix(BG, FIELD, 0.5 * aL), 3, 10)
    fish_small(c, 480, 600, aL)
    c.text(480, 700, '鱼尾朝北，顺着地磁场冷却', 'sans', 26, mix(BG, INK, aL), 'mm')
    c.text(480, 744, '传统解释', 'sans', 22, mix(BG, MUTED, aL), 'mm')
    # right: tongs
    c.text(1440, 220, '解释二：铁钳', 'bold', 36, mix(BG, COPPER, aR), 'mm')
    c.text(1440, 268, '贴得很近，局部可能更强', 'sans', 28, mix(BG, MUTED, aR), 'mm')
    fish_small(c, 1500, 600, aR)
    # tongs at fish head (left end of fish)
    hx = 1500 - 170
    c.line([(hx - 10, 590), (hx - 260, 470)], mix(BG, MUTED, aR), 12)
    c.line([(hx - 10, 610), (hx - 260, 730)], mix(BG, MUTED, aR), 12)
    for r in (40, 70, 105, 145):
        c.arc(hx, 600, r, r * 0.8, -70, 70, mix(BG, COPPER, aR * (1 - r / 200)), 3)
    c.text(hx - 140, 600, '铁钳', 'sans', 26, mix(BG, INK, aR), 'mm')
    c.text(1440, 744, '黄兴的模拟实验支持这一说', 'sans', 22, mix(BG, MUTED, aR), 'mm')
    b = fade(t, 8, 8.8)
    c.text(960, 940, '两种解释都靠同一个原理：冷却时按周围的磁场排队', 'bold', 34, mix(BG, INK, b), 'mm')
    c.text(960, 1000, '区别只在于：是谁的磁场？我们做实验来分辨。', 'bold', 34, mix(BG, SPARK, fade(t, 12, 12.8)), 'mm')

def fish_small(c, cx, cy, a):
    pts = []
    for k in range(41):
        u = -0.95 + 1.9 * k / 40
        pts.append((cx + u * 180, cy - (1 - abs(u)) ** 0.8 * 50))
    for k in range(41):
        u = 0.95 - 1.9 * k / 40
        pts.append((cx + u * 180, cy + (1 - abs(u)) ** 0.8 * 50))
    c.poly(pts, mix(BG, MUTED, 0.45 * a))

EPS = [('B1', '指南鱼'), ('B2', '卓筒井'), ('B3', '活字印刷'), ('B4', '水排'), ('B5', '都江堰')]
OPEN = titles.opening('从零造物 · 古法解密', '第八卷 · 古人是怎么做到的', EPS, 0, '北宋 · 约公元 1044 年 ·《武经总要》')
CLOSE = titles.closing('从零造物 · 古法解密', '第八卷 · 古人是怎么做到的', EPS, 0, '古人已经会让铁带磁，那磁能变成电吗？见第一卷')

SHOTS = {
    'B1_原文卡': (draw_text, 25),
    'B1_热剩磁': (draw_domains, 24),
    'B1_两种解释': (draw_two, 20),
    'B1_片头': (OPEN, 7),
    'B1_片尾': (CLOSE, 7),
}

if __name__ == '__main__':
    if len(sys.argv) > 2:
        f, _ = SHOTS[sys.argv[1]]
        c = Canvas(); f(c, float(sys.argv[2]), 0); c.im.reduce(SS).save('/home/claude/video/prevb1.png')
    else:
        for n, (f, d) in SHOTS.items():
            render(f'/home/claude/video/out/{n}.mp4', d, f); print(n)
