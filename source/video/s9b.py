"""第九季第二批：B23 走马灯、B24 水密隔舱、B25 记里鼓车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s9a import SB9, VOL9, WATER, BRONZE

WOOD = (150, 110, 70)
PAPER = (225, 215, 190)
HOTAIR = (235, 130, 70)

# ---------------------------------------------------------------- B23 走马灯
def b23_flow(c, t, i):
    corner_tag(c, 'B23 · 热气推叶轮')
    c.text(60, 96, '没有风，纸马为什么会自己跑？', 'serif', 40, INK)
    cx, base = 640, 860
    # candle
    c.rect(cx - 30, base - 120, cx + 30, base, fill=(230, 225, 210), r=6)
    fh = 60 + 10 * math.sin(t * 9)
    c.poly([(cx - 16, base - 120), (cx + 16, base - 120), (cx, base - 120 - fh)], SPARK)
    # rising hot air parcels
    rnd = random.Random(23)
    for k in range(26):
        ph = rnd.random()
        y = base - 200 - ((t * 120 + ph * 500) % 500)
        x = cx + rnd.uniform(-60, 60) * (1 + (base - 200 - y) / 400)
        c.ellipse(x, y, 10, 10, fill=mix(BG, HOTAIR, 0.5))
    # impeller seen in perspective at top
    iy = 260
    c.line([(cx, iy), (cx, base - 220)], MUTED, 3)
    ang = t * 2.2
    for k in range(8):
        a_ = ang + k * math.pi / 4
        x0 = cx + 40 * math.cos(a_); x1 = cx + 230 * math.cos(a_)
        y0 = iy + 14 * math.sin(a_); y1 = iy + 80 * math.sin(a_)
        c.poly([(x0, y0 - 8), (x1, y1 - 18), (x1, y1 + 18), (x0, y0 + 8)], mix(BG, PAPER, 0.6 + 0.4 * math.cos(a_)))
    c.ellipse(cx, iy, 14, 14, fill=SPARK)
    # paper horses on a ring below impeller
    for k in range(6):
        a_ = ang + k * math.pi / 3
        x = cx + 300 * math.cos(a_); y = 470 + 40 * math.sin(a_)
        if math.sin(a_) > -0.2:
            c.text(x, y, '马', 'serif', 40, mix(BG, INK, 0.5 + 0.5 * math.sin(a_)), 'mm')
    a = fade(t, 6, 7)
    c.rect(1180, 260, 1860, 700, fill=mix(BG, SHEET, a), r=14)
    c.text(1210, 310, '① 蜡烛把空气烧热', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 365, '② 热空气轻，往上升', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 420, '③ 撞上斜着装的叶片', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 475, '④ 叶片被推向一侧：转了', 'sans', 26, mix(BG, INK, a), 'lm')
    b = fade(t, 13, 14)
    c.text(1210, 560, '热气流 → 转动', 'bold', 30, mix(BG, SPARK, b), 'lm')
    c.text(1210, 615, '和今天燃气涡轮的道理相通', 'sans', 24, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 6, '灯里的蜡烛一点，上面的纸叶轮就转了起来，带着一圈纸马跑'),
                (6.2, 13, '热空气比冷空气轻，往上升；叶片是斜着装的，上升的气流推在斜面上，就推出一个侧向的力'),
                (13.2, 22, '和第 44 集热气球、第 07 集风车一起看：热气流也是风，叶片把它变成了转动')], y=1010)

def b23_angle(c, t, i):
    corner_tag(c, 'B23 · 叶片角度')
    c.text(60, 96, '叶片斜多少，转得最快？', 'serif', 40, INK)
    angles = [(0, 0.0), (20, 0.6), (45, 1.0), (70, 0.55), (90, 0.0)]
    for k, (deg, sp) in enumerate(angles):
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        if a <= 0: continue
        cx = 260 + k * 350
        cy = 420
        r = math.radians(deg)
        # blade cross-section: line tilted by deg from horizontal
        dx, dy = 90 * math.cos(r), -90 * math.sin(r)
        c.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], mix(BG, PAPER, a), 10)
        for j in range(3):
            c.arrow(cx - 40 + j * 40, cy + 170, cx - 40 + j * 40, cy + 70, mix(BG, HOTAIR, a), 4, 14)
        c.text(cx, cy - 150, f'{deg}°', 'mono', 36, mix(BG, INK, a), 'mm')
        h = 220 * sp
        c.rect(cx - 50, 860 - h, cx + 50, 860, fill=mix(BG, GREEN if sp > 0.9 else FIELD, a), r=6)
        c.text(cx, 890, '不转' if sp == 0 else ('最快' if sp == 1 else '较慢'), 'bold', 26, mix(BG, INK, a), 'mm')
    c.line([(100, 860), (1820, 860)], LINE, 2)
    c.text(100, 620, '转速（示意）', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 4, '叶片平放：气流直直顶上来，只往上推，不转'),
                (4.2, 12, '叶片竖起：气流擦着过去，也几乎推不动'),
                (12.2, 22, '斜着四五十度左右，侧向的力最大，转得最快：实验里我们一档一档地量（以实测为准）')], y=1010)

# ---------------------------------------------------------------- B24 水密隔舱
def b24_compartments(c, t, i):
    corner_tag(c, 'B24 · 船破了一格')
    c.text(60, 96, '船底撞开一个洞，为什么不沉？', 'serif', 40, INK)
    for k, (y0, lab, bh) in enumerate([(200, '没有隔板', False), (620, '12 道隔板、13 个舱', True)]):
        a = fade(t, 0.5 + k * 1, 1.5 + k * 1)
        if a <= 0: continue
        off = y0 - 220
        wl = 420 + off
        c.rect(120, wl, 1800, wl + 150, fill=mix(BG, WATER, 0.25))
        hole = t > 4
        if bh:
            sink = 18 * fade(t, 5, 9)
        else:
            sink = 90 * fade(t, 5, 15)
        # draw hull with local water line
        x0, x1, deck, keel = 300, 1500, 330 + off, 470 + off
        pts = [(x0, deck + sink), (x1, deck + sink), (x1 - 60, keel + sink), (x0 + 60, keel + sink)]
        c.poly(pts, mix(BG, WOOD, 0.5 * a)); seg(c, pts + [pts[0]], mix(BG, WOOD, a), 4)
        n = 13; w = (x1 - x0) / n
        if bh:
            for j in range(1, n):
                x = x0 + j * w
                c.line([(x, deck + sink), (x, keel + sink)], mix(BG, WOOD, a), 3)
        if hole:
            if bh:
                fx0 = x0 + 6 * w
                c.rect(fx0 + 3, wl, fx0 + w - 3, keel + sink - 3, fill=mix(BG, WATER, 0.85))
            else:
                lvl = max(deck + sink + 4, keel + sink - (keel - deck) * fade(t, 5, 15))
                if lvl < keel + sink - 8:
                    c.rect(x0 + 62, lvl, x1 - 62, keel + sink - 3, fill=mix(BG, WATER, 0.85))
            c.text(x0 + 6.5 * w, keel + sink + 30, '破洞', 'bold', 24, NRED, 'mm')
        c.text(140, y0 + 10, lab, 'bold', 28, mix(BG, INK, a), 'lm')
        res = '水灌满整个船舱：沉' if not bh else '水只进了一格：吃水只深了一点'
        b = fade(t, 9 + k * 2, 10 + k * 2)
        c.text(1780, y0 + 10, res, 'bold', 26, mix(BG, NRED if not bh else GREEN, b), 'rm')
    caps(c, t, [(0, 4, '两条一样的船，一条船舱是一整个大空间，一条用隔板分成十三个舱'),
                (4.2, 12, '船底都撞开一个洞：没有隔板的那条，水灌进整个船舱'),
                (12.2, 22, '有隔板的那条，水只进了一格。1974 年泉州湾出土的南宋海船，就是 12 道隔板、13 个舱')], y=1010)

def b24_buoyancy(c, t, i):
    corner_tag(c, 'B24 · 浮力账')
    c.text(60, 96, '少了一格的浮力，还剩多少？', 'serif', 40, INK)
    n = 13
    x0, y0, w, h = 260, 360, 100, 300
    lost = t > 6
    for k in range(n):
        a = fade(t, 0.5 + k * 0.25, 1 + k * 0.25)
        x = x0 + k * (w + 8)
        col = WATER if (lost and k == 6) else GREEN
        c.rect(x, y0, x + w, y0 + h, fill=mix(BG, col, 0.7 * a), r=6)
        c.text(x + w / 2, y0 + h + 30, str(k + 1), 'mono', 22, mix(BG, MUTED, a), 'mm')
    c.text(960, 300, '每一格都在「托」着船（浮力）', 'sans', 26, INK, 'mm')
    b = fade(t, 7, 8)
    c.rect(360, 760, 1560, 950, fill=mix(BG, SHEET, b), r=14)
    c.text(960, 805, '进水一格：浮力只少了约 1/13 ≈ 8%', 'serif', 32, mix(BG, SPARK, b), 'mm')
    c.text(960, 860, '船只要多吃一点水，用剩下 12 格多排开一点水，就又浮住了', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 910, '浮力 = 排开的水的重量（阿基米德）', 'sans', 24, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '十三个舱，每一格都在排开水、托着船'),
                (6.2, 14, '破了一格，那一格不再出力：少了大约十三分之一的浮力'),
                (14.2, 22, '船身稍稍下沉，用其余的舱多排开一点水，就重新浮住了。隔板还让船身更结实')], y=1010)

# ---------------------------------------------------------------- B25 记里鼓车
def gear(c, cx, cy, r, teeth, ang, col, a=1.0):
    pts = []
    for k in range(teeth * 2):
        rr = r if k % 2 == 0 else r * 0.86
        q = ang + k * math.pi / teeth
        pts.append((cx + rr * math.cos(q), cy + rr * math.sin(q)))
    c.poly(pts, mix(BG, col, 0.5 * a))
    seg(c, pts + [pts[0]], mix(BG, col, a), 2)
    c.ellipse(cx, cy, 8, 8, fill=mix(BG, INK, a))

def b25_gears(c, t, i):
    corner_tag(c, 'B25 · 齿轮减速')
    c.text(60, 96, '轮子转 100 圈，鼓才响一声：怎么做到？', 'serif', 40, INK)
    wheel_turns = t * 6
    # road wheel
    wx, wy, wr = 300, 640, 180
    c.ellipse(wx, wy, wr, wr, outline=WOOD, width=10)
    for k in range(8):
        q = wheel_turns * 2 * math.pi + k * math.pi / 4
        c.line([(wx, wy), (wx + wr * math.cos(q), wy + wr * math.sin(q))], WOOD, 5)
    # gear chain: 1:10 then 1:10 (illustrative)
    g1 = wheel_turns * 2 * math.pi
    gear(c, 640, 640, 50, 10, g1, BRONZE)
    gear(c, 640 + 50 + 150 + 6, 640, 150, 30, -g1 / 3 + 0.1, BRONZE)       # 10:30 -> 1/3 (shown)
    gear(c, 1100, 400, 40, 8, -g1 / 3, BRONZE)
    gear(c, 1100 + 40 + 160 + 6, 400, 160, 32, g1 / 12 + 0.1, BRONZE)
    c.text(640, 760, '小齿轮', 'sans', 22, MUTED, 'mm')
    c.text(846, 820, '大齿轮', 'sans', 22, MUTED, 'mm')
    c.text(1306, 600, '更大的齿轮', 'sans', 22, MUTED, 'mm')
    c.line([(wx, wy), (640, 640)], MUTED, 4)
    count = int(wheel_turns)
    li = count // 100
    c.text(300, 300, f'车轮已转 {count} 圈', 'mono', 32, INK, 'mm')
    c.text(300, 350, f'鼓响 {li} 声', 'mono', 32, SPARK, 'mm')
    hit = (wheel_turns % 100) < 3 and wheel_turns > 50
    c.ellipse(1600, 760, 70, 50, fill=mix(BG, NRED, 0.7), outline=NRED, width=3)
    if hit:
        c.text(1600, 660, '咚！', 'bold', 44, SPARK, 'mm')
    c.text(1600, 850, '鼓', 'sans', 24, MUTED, 'mm')
    a = fade(t, 12, 13)
    c.rect(1300, 160, 1860, 300, fill=mix(BG, SHEET, a), r=12)
    c.text(1330, 200, '每一级：小齿轮带大齿轮，转得更慢', 'sans', 22, mix(BG, INK, a), 'lm')
    c.text(1330, 250, '几级串起来，100 圈只剩 1 圈（示意）', 'bold', 24, mix(BG, SPARK, a), 'lm')
    caps(c, t, [(0, 6, '车轮一边走，一边带着齿轮转'),
                (6.2, 12, '小齿轮带大齿轮，转速一级一级降下来'),
                (12.2, 22, '降到车轮转一百圈、最后那个齿轮才转一圈：拨一下木人的手，鼓就「咚」一声')], y=1010)

def b25_math(c, t, i):
    corner_tag(c, 'B25 · 一里有多长')
    c.text(60, 96, '为什么偏偏是 100 圈？', 'serif', 40, INK)
    a = fade(t, 0.5, 1.5)
    cx, cy, r = 420, 520, 150
    c.ellipse(cx, cy, r, r, outline=mix(BG, WOOD, a), width=8)
    c.line([(cx - r, cy + r + 40), (cx + r, cy + r + 40)], mix(BG, MUTED, a), 2)
    c.text(cx, cy + r + 75, '直径 6 尺', 'sans', 26, mix(BG, INK, a), 'mm')
    rolled = fade(t, 2, 6)
    c.line([(cx - r * 2.4, cy + r), (cx - r * 2.4 + 2 * math.pi * r * 0.8 * rolled, cy + r)], mix(BG, SPARK, a), 6)
    c.text(cx, cy - r - 40, '滚一圈 ≈ 18 尺（周长）', 'bold', 28, mix(BG, SPARK, rolled), 'mm')
    b = fade(t, 7, 8)
    c.rect(900, 260, 1860, 640, fill=mix(BG, SHEET, b), r=14)
    lines = [('一圈：18 尺', INK), ('100 圈：1800 尺', INK), ('= 300 步（1 步 = 6 尺）', INK), ('= 1 里', SPARK)]
    for k, (s_, col) in enumerate(lines):
        d = fade(t, 8 + k * 2, 9 + k * 2)
        c.text(940, 320 + k * 80, s_, 'bold' if k == 3 else 'sans', 36 if k == 3 else 30, mix(BG, col, d), 'lm')
    e_ = fade(t, 16, 17)
    c.rect(300, 820, 1620, 950, fill=mix(BG, SHEET, e_), r=12)
    c.text(960, 860, '《宋史·舆服志》记下了 1027 年卢道隆记里鼓车的轮径和齿数（拍摄前核对原文）', 'sans', 24, mix(BG, INK, e_), 'mm')
    c.text(960, 910, '误差来自：轮子打滑、路面起伏、车轮磨损', 'sans', 24, mix(BG, MUTED, e_), 'mm')
    caps(c, t, [(0, 7, '车轮直径六尺，滚一圈大约十八尺'),
                (7.2, 16, '一百圈就是一千八百尺，三百步，正好一里：所以齿轮要把一百圈减成一圈'),
                (16.2, 22, '先定好轮子的大小，再算齿数。一辆车，就成了一把会走路的尺子')], y=1010)

CLIPS = {
 'B23_热气流': (b23_flow, 22), 'B23_叶片角度': (b23_angle, 22),
 'B23_片头': (titles.opening(BSER, VOL9, SB9, 3, '南宋 · 临安元宵灯市'), 7),
 'B23_片尾': (titles.closing(BSER, VOL9, SB9, 3, '下集：船破了一格，为什么不沉？'), 7),
 'B24_分舱': (b24_compartments, 22), 'B24_浮力账': (b24_buoyancy, 22),
 'B24_片头': (titles.opening(BSER, VOL9, SB9, 4, '南宋 · 1974 年泉州湾出土海船'), 7),
 'B24_片尾': (titles.closing(BSER, VOL9, SB9, 4, '下集：车子自己怎么知道走了几里？'), 7),
 'B25_齿轮减速': (b25_gears, 22), 'B25_一里': (b25_math, 22),
 'B25_片头': (titles.opening(BSER, VOL9, SB9, 5, '北宋 · 1027 年 · 卢道隆'), 7),
 'B25_片尾': (titles.closing(BSER, VOL9, SB9, 5, '下集：船怎么翻过一道坡？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
