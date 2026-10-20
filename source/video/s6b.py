"""第六季第二批：E46 温度计、E47 用影子测地球、B10 透光镜 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s6a import S6A, SB6, SER6, VOL6, BRONZE, GREEN, seg

GLASS = (150, 175, 190)
REDL = (210, 70, 60)

# ---------------------------------------------------------------- E46 温度计
def tube(c, x, top, bottom, level, col=REDL, a=1.0):
    c.rect(x - 16, top, x + 16, bottom, outline=mix(BG, GLASS, a), width=3, r=14)
    c.ellipse(x, bottom + 34, 46, 46, fill=mix(BG, col, a), outline=mix(BG, GLASS, a), width=3)
    c.rect(x - 8, level, x + 8, bottom + 10, fill=mix(BG, col, a))

def e46_expand(c, t, i):
    corner_tag(c, '第 46 集 · 热胀冷缩')
    c.text(60, 96, '细管里的水，为什么会随温度升降？', 'serif', 40, INK)
    heat = 0.5 + 0.5 * math.sin((t - 2) * 0.55) if t > 2 else 0.0
    # bulb close-up with molecules
    cx, cy, R = 560, 560, 230
    c.ellipse(cx, cy, R, R, outline=GLASS, width=5)
    rnd = random.Random(46)
    for k in range(70):
        u, v, ph = rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(0, 6.3)
        if u * u + v * v > 0.85: continue
        spread = 1 + 0.12 * heat
        jig = 6 + 14 * heat
        x = cx + u * R * 0.85 * spread + jig * math.sin(t * (4 + 6 * heat) + ph)
        y = cy + v * R * 0.85 * spread + jig * math.cos(t * (3.5 + 6 * heat) + ph)
        if (x - cx) ** 2 + (y - cy) ** 2 < (R - 12) ** 2:
            c.ellipse(x, y, 11, 11, fill=mix(FIELD, NRED, heat))
    c.text(cx, cy + R + 50, '热了：分子晃得更厉害，彼此挤得更开', 'sans', 26, INK, 'mm')
    # thermometer at right
    tx = 1400
    level = 760 - 420 * heat
    tube(c, tx, 230, 800, level)
    c.text(tx + 60, level, '液面', 'sans', 24, INK, 'lm')
    c.arrow(tx - 80, 700, tx - 80, 300, mix(BG, NRED, heat), 5, 16)
    c.text(tx - 100, 500, '体积只胀一点点', 'sans', 24, MUTED, 'rm')
    c.text(tx - 100, 545, '细管把它放大成一大段', 'sans', 24, MUTED, 'rm')
    caps(c, t, [(0, 6, '液体受热，分子晃得更厉害，彼此挤开一点点：体积变大'),
                (6.2, 14, '变大的那一点点，被挤进一根很细的管子，就变成很长一段'),
                (14.2, 22, '管子越细，同样的温度变化，液柱升得越高：越灵敏')], y=1010)

def e46_calibrate(c, t, i):
    corner_tag(c, '第 46 集 · 怎样定义「一度」')
    c.text(60, 96, '先找两个永远不变的温度', 'serif', 40, INK)
    tx = 760
    top, bottom = 220, 820
    p0, p100 = 740, 300
    st = 0 if t < 5 else (1 if t < 10 else 2)
    if st == 0: level = p0
    elif st == 1: level = p100
    else: level = p0 + (p100 - p0) * 0.37
    tube(c, tx, top, bottom, level)
    a0, a1, a2 = fade(t, 2, 3), fade(t, 7, 8), fade(t, 11, 13)
    c.line([(tx + 24, p0), (tx + 90, p0)], mix(BG, FIELD, a0), 4)
    c.text(tx + 100, p0, '0：冰水混合物', 'bold', 28, mix(BG, FIELD, a0), 'lm')
    c.line([(tx + 24, p100), (tx + 90, p100)], mix(BG, NRED, a1), 4)
    c.text(tx + 100, p100, '100：水沸腾（一个标准大气压）', 'bold', 28, mix(BG, NRED, a1), 'lm')
    if a2 > 0:
        for k in range(1, 10):
            y = p0 + (p100 - p0) * k / 10
            c.line([(tx + 24, y), (tx + 56, y)], mix(BG, MUTED, a2), 3)
            c.text(tx + 64, y, str(k * 10), 'mono', 20, mix(BG, MUTED, a2), 'lm')
    if st == 0:
        c.text(400, 600, '冰水', 'serif', 40, FIELD, 'mm')
    elif st == 1:
        c.text(400, 300, '沸水', 'serif', 40, NRED, 'mm')
    b = fade(t, 15, 16)
    c.rect(1240, 560, 1860, 860, fill=mix(BG, SHEET, b), r=14)
    c.text(1270, 610, '1714 年 华伦海特：水银温度计', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(1270, 660, '1742 年 摄尔修斯：百分刻度', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(1270, 705, '（他最初把沸点定为 0、冰点定为 100，', 'sans', 22, mix(BG, MUTED, b), 'lm')
    c.text(1270, 745, '　后来才倒过来）', 'sans', 22, mix(BG, MUTED, b), 'lm')
    c.text(1270, 810, '「一度」是人定的，两个定点是自然给的', 'bold', 24, mix(BG, COPPER, b), 'lm')
    caps(c, t, [(0, 5, '放进冰水，液柱停在一个位置：记作 0'),
                (5.2, 10, '放进沸水，停在另一个位置：记作 100'),
                (10.2, 15, '中间平均分成 100 格，每一格就是「一度」'),
                (15.2, 22, '两个定点是自然给的，「一度」多大，是人约定的')], y=1010)

# ---------------------------------------------------------------- E47 用影子测地球
def e47_parallel(c, t, i):
    corner_tag(c, '第 47 集 · 两根杆子')
    c.text(60, 96, '同一时刻，两地的影子为什么不一样长？', 'serif', 40, INK)
    curved = fade(t, 7, 11)
    # sun rays from left top, parallel, vertical-ish (sun overhead city A)
    for k in range(9):
        x = 300 + k * 160
        c.arrow(x, 180, x, 330, mix(BG, SPARK, 0.8), 3, 12)
    c.text(1780, 220, '太阳很远：光线几乎平行', 'sans', 24, SPARK, 'rm')
    cx, cy = 960, 1700
    R = 1100
    # surface: blend flat line y=700 to circle arc
    pts = []
    for k in range(0, 101):
        x = 200 + k * 15.2
        yf = 700
        yc = cy - math.sqrt(max(0, R * R - (x - cx) ** 2))
        pts.append((x, yf + (yc - yf) * curved))
    c.line(pts, MUTED, 6)
    for k, (xs, lab) in enumerate([(700, '城市甲'), (1260, '城市乙')]):
        yf = 700
        yc = cy - math.sqrt(R * R - (xs - cx) ** 2)
        y = yf + (yc - yf) * curved
        ang = math.atan2(xs - cx, cy - yc) * curved          # tilt of local vertical
        H = 160
        tx_, ty_ = xs + H * math.sin(ang), y - H * math.cos(ang)
        c.line([(xs, y), (tx_, ty_)], INK, 6)
        # shadow along ground: sun vertical rays; shadow length = H*sin(ang) roughly toward the right/left
        sh = H * math.tan(abs(ang)) if abs(ang) > 0.001 else 0
        d = 1 if ang > 0 else -1
        if sh > 2:
            gx, gy = math.cos(ang), math.sin(ang)
            c.line([(xs, y), (xs + d * gx * sh, y + d * gy * sh)], FIELD, 10)
            pass
        c.text(xs, y + 60, lab, 'bold', 28, INK, 'mm')
    if curved > 0.9:
        c.text(960, 900, '地面是弯的：两根杆子指向不同的方向，影子（蓝色）就不一样', 'sans', 28, COPPER, 'mm')
    caps(c, t, [(0, 7, '如果大地是平的：阳光平行照下来，两根杆子的影子一样长'),
                (7.2, 14, '可大地是弯的：两根杆子一个竖直、一个是斜的'),
                (14.2, 22, '同一时刻影子不一样长：差多少，就说明地面弯了多少')], y=1010)

def e47_compute(c, t, i):
    corner_tag(c, '第 47 集 · 算出地球')
    c.text(60, 96, '埃拉托色尼的算法', 'serif', 40, INK)
    cx, cy, R = 620, 600, 300
    c.ellipse(cx, cy, R, R, outline=MUTED, width=5)
    ang = math.radians(7.2) * 4    # exaggerated for display
    a = fade(t, 1, 2)
    # city A at top, city B rotated
    ax, ay = cx, cy - R
    bx, by = cx - R * math.sin(ang), cy - R * math.cos(ang)
    c.line([(cx, cy), (ax, ay - 80)], mix(BG, FIELD, a), 3)
    c.line([(cx, cy), (bx - 80 * math.sin(ang), by - 80 * math.cos(ang))], mix(BG, COPPER, a), 3)
    c.ellipse(ax, ay, 12, 12, fill=FIELD); c.ellipse(bx, by, 12, 12, fill=COPPER)
    c.text(ax + 20, ay - 40, '赛伊尼：正午太阳正头顶', 'sans', 24, FIELD, 'lm')
    c.text(bx - 40, by - 20, '亚历山大：影子偏 7.2°', 'sans', 24, COPPER, 'rm')
    c.arc(cx, cy, 80, 80, -90 - math.degrees(ang), -90, SPARK, 4)
    c.text(cx - 20, cy - 110, '7.2°', 'bold', 26, SPARK, 'rm')
    for k in range(6):
        x = 260 + k * 120
        c.arrow(x - 300 * 0, 150, x, 230, mix(BG, SPARK, 0.6), 3, 10)
    b = fade(t, 6, 7)
    rows = [('两地影子的角度差', '7.2° = 圆周的 1/50'), ('两地距离', '约 5000 斯塔德'), ('地球周长', '5000 × 50 = 25 万斯塔德'),
            ('换算成公里', '约 4 万公里上下（斯塔德长度有争议）')]
    for k, (l, r) in enumerate(rows):
        al = fade(t, 6 + k * 3, 7 + k * 3)
        c.text(1100, 300 + k * 120, l, 'sans', 26, mix(BG, MUTED, al), 'lm')
        c.text(1100, 345 + k * 120, r, 'bold', 32, mix(BG, INK if k < 3 else COPPER, al), 'lm')
    c.text(cx, cy + R + 50, '（角度为示意，已放大）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 6, '约公元前 240 年：夏至正午，赛伊尼的井底照得到太阳；北边的亚历山大，影子偏了 7.2 度'),
                (6.2, 15, '7.2 度是整圈的五十分之一，那两地的距离就是地球一圈的五十分之一'),
                (15.2, 22, '唐代僧一行也组织过大规模的实地测量，算出了南北一度有多长')], y=1010)

# ---------------------------------------------------------------- B10 透光镜
def b10_amplify(c, t, i):
    corner_tag(c, 'B10 · 看不见的起伏')
    c.text(60, 96, '肉眼看不出的小起伏，怎么在墙上变成图案？', 'serif', 40, INK)
    mx = 520
    wallx = 1620
    bump = fade(t, 5, 8)
    # mirror surface profile (vertical), bump in the middle
    ys = [260 + k * 6 for k in range(91)]
    def surf(y):
        return mx + bump * 6 * math.exp(-((y - 530) / 40) ** 2)
    c.line([(surf(y), y) for y in ys], (220, 200, 160), 8)
    c.text(mx - 30, 820, '镜面（侧面看）', 'sans', 24, MUTED, 'rm')
    c.rect(wallx, 200, wallx + 30, 860, fill=(90, 90, 96))
    c.text(wallx + 15, 890, '墙', 'sans', 24, MUTED, 'mm')
    # incoming light from left: horizontal rays; reflect: slope affects direction
    hits = []
    for k in range(17):
        y = 300 + k * 30
        # slope dx/dy at y
        h = 0.5
        sl = (surf(y + h) - surf(y - h)) / (2 * h)
        ang = 2 * math.atan(sl) * 0.6      # amplified for visibility
        x0 = surf(y)
        c.line([(120, y), (x0, y)], mix(BG, SPARK, 0.5), 2)
        yw = max(210, min(850, y + (wallx - x0) * math.tan(ang)))
        c.line([(x0, y), (wallx, yw)], mix(BG, SPARK, 0.7), 2)
        hits.append(yw)
    # brightness on wall
    for yw in hits:
        c.ellipse(wallx - 6, yw, 6, 6, fill=SPARK)
    c.text(1180, 200, '光线照到镜面，反射到远处的墙上', 'sans', 24, INK, 'mm')
    if bump > 0.5:
        c.text(1180, 920, '起伏只有头发丝的几十分之一，可墙离得远，偏一点点就挪开很多', 'sans', 26, COPPER, 'mm')
    caps(c, t, [(0, 5, '一面完全平的镜子：反射的光均匀照在墙上'),
                (5.2, 13, '镜面有一处极小的凸起：那里的光被往两边推开，墙上那块就暗一些'),
                (13.2, 22, '墙越远，偏差越大：镜面看不见的起伏，被放大成墙上的明暗图案')], y=1010)

def b10_grind(c, t, i):
    corner_tag(c, 'B10 · 背面的花纹怎么跑到正面')
    c.text(60, 96, '研磨镜面时，薄处和厚处表现不一样', 'serif', 40, INK)
    x0, x1 = 260, 1660
    y_face = 520
    # cross-section: face on top, back with raised pattern (thick parts)
    press = fade(t, 4, 9) * (1 - fade(t, 12, 14))
    relax = fade(t, 12, 15)
    pattern = [(500, 620), (900, 1000), (1300, 1420)]
    def thick(x):
        return any(a <= x <= b for a, b in pattern)
    top_pts, bot_pts = [], []
    for k in range(0, 141):
        x = x0 + k * 10
        th = 150 if thick(x) else 80
        # pressing: thin parts deflect down more; after relax: thin parts bulge up slightly (exaggerated)
        dfl = (0 if thick(x) else 18) * press - (0 if thick(x) else 10) * relax
        top_pts.append((x, y_face + dfl))
        bot_pts.append((x, y_face + dfl + th))
    c.poly(top_pts + bot_pts[::-1], mix(BG, BRONZE, 0.9))
    c.text(x0 - 20, y_face, '镜面', 'sans', 24, MUTED, 'rm')
    c.text(x0 - 20, y_face + 140, '背面花纹', 'sans', 24, MUTED, 'rm')
    if press > 0.05:
        for k in range(8):
            x = x0 + 80 + k * 180
            c.arrow(x, y_face - 140, x, y_face - 30, mix(BG, NRED, press), 5, 16)
        c.text(960, y_face - 170, '研磨、刮削：压力往下', 'sans', 26, mix(BG, NRED, press), 'mm')
    if relax > 0.3:
        c.text(960, y_face - 170, '松开以后：薄的地方回弹多一点，鼓起来', 'sans', 26, mix(BG, GREEN, relax), 'mm')
        for a, b in pattern:
            c.line([((a + b) / 2, y_face - 60), ((a + b) / 2, y_face - 20)], mix(BG, SPARK, relax), 3)
        c.text(960, 820, '镜面留下和背面花纹对应的微小起伏（起伏已放大几千倍示意）', 'sans', 24, mix(BG, SPARK, relax), 'mm')
    b = fade(t, 17, 18)
    c.rect(300, 880, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 920, '沈括猜是「铸时薄处先冷」造成的；今天一般认为关键在研磨时的应力', 'sans', 26, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 4, '铜镜背面有凸起的花纹：花纹处厚，其余地方薄'),
                (4.2, 12, '打磨镜面时一直用力往下压：薄的地方被压弯得多，厚的地方压不动'),
                (12.2, 22, '松开以后，薄处回弹，镜面上就留下了和花纹对应的、看不见的起伏')], y=1035)

CLIPS = {
 'E46_热胀冷缩': (e46_expand, 22), 'E46_定标': (e46_calibrate, 22),
 'E46_片头': (titles.opening(SER6, VOL6, S6A, 1, '穿越北宋 · 从零定义「一度」'), 7),
 'E46_片尾': (titles.closing(SER6, VOL6, S6A, 1, '下集：一根杆子，怎么量出地球多大？'), 7),
 'E47_平行光': (e47_parallel, 22), 'E47_计算': (e47_compute, 22),
 'E47_片头': (titles.opening(SER6, VOL6, S6A, 2, '约公元前 240 年 · 埃拉托色尼 · 唐代一行'), 7),
 'E47_片尾': (titles.closing(SER6, VOL6, S6A, 2, '下集：实心铜镜，怎么把背面花纹「照」到墙上？'), 7),
 'B10_放大': (b10_amplify, 22), 'B10_研磨': (b10_grind, 22),
 'B10_片头': (titles.opening(BSER, BVOL, SB6, 2, '汉代铜镜 · 北宋沈括《梦溪笔谈》'), 7),
 'B10_片尾': (titles.closing(BSER, BVOL, SB6, 2, '下集：为什么换了写法，算账就变快了？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
