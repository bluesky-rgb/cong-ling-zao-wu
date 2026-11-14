"""第五十季（古法解密 22.0：山居与田园）第二批：B223 蚊帐、B224 蜂巢、B225 镰刀 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s50a import SB50, VOL50

NET = (200, 210, 220)
WAX = (240, 190, 70)
STALK = (200, 180, 90)
BLADE = (180, 190, 200)


# ---------------------------------------------------------------- B223 蚊帐
def b223_mesh(c, t, i):
    corner_tag(c, 'B223 · 网眼比蚊子小')
    c.text(60, 96, '蚊帐的网眼只有一毫米左右，比蚊子的身体小，蚊子钻不过去；可网眼比空气分子大得多得多，风照样吹得进来', 'serif', 36, INK)
    x0, y0, x1, y1 = 760, 240, 1160, 900
    g = 28
    for k in range(int((x1 - x0) / g) + 1):
        c.line([(x0 + k * g, y0), (x0 + k * g, y1)], mix(BG, NET, 0.8), 3)
    for k in range(int((y1 - y0) / g) + 1):
        c.line([(x0, y0 + k * g), (x1, y0 + k * g)], mix(BG, NET, 0.8), 3)
    random.seed(4)
    for k in range(5):
        f = ((t * 0.25) + k / 5) % 1
        x = 200 + 540 * min(1.0, f * 1.2)
        y = 320 + k * 120 + 20 * math.sin(t * 6 + k)
        c.ellipse(x, y, 26, 12, fill=mix(BG, (90, 90, 90), 1.0))
        c.line([(x - 10, y), (x - 30, y - 22)], MUTED, 2)
        c.line([(x + 10, y), (x + 30, y - 22)], MUTED, 2)
    for k in range(60):
        f = ((t * 0.6) + k / 60) % 1
        x = 200 + f * 1500
        y = 260 + (k * 37) % 620
        c.ellipse(x, y, 3, 3, fill=mix(BG, (170, 210, 240), 0.9))
    c.text(400, 960, '蚊子：被挡在外面', 'bold', 26, NRED, 'mm')
    c.text(1480, 960, '空气（小点）：照样穿过去', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '用放大镜看蚊帐布：一个个小方格，每格一毫米左右（以实测为准）'),
                (7.2, 14, '蚊子的身体比网眼大，撞上来就过不去'),
                (14.2, 22, '空气、光都比网眼小得多，穿过去一点也不受影响（示意，空气分子极小）')], y=1010)


def b223_air(c, t, i):
    corner_tag(c, 'B223 · 网眼刚刚好')
    c.text(60, 96, '网眼太大，蚊子钻进来；网眼太密（像棉布），蚊子进不来，风也进不来，睡在里面闷热：网眼要刚刚好', 'serif', 36, INK)
    for j, (lab, g, bug, air, col) in enumerate([('纱布：网眼大', 60, True, 1.0, NRED), ('蚊帐布：刚刚好', 26, False, 0.85, GREEN), ('棉布：太密', 8, False, 0.15, NRED)]):
        cx = 330 + j * 630
        x0, y0 = cx - 160, 300
        for k in range(int(320 / g) + 1):
            c.line([(x0 + k * g, y0), (x0 + k * g, y0 + 360)], mix(BG, NET, 0.8), 2)
        for k in range(int(360 / g) + 1):
            c.line([(x0, y0 + k * g), (x0 + 320, y0 + k * g)], mix(BG, NET, 0.8), 2)
        c.ellipse(cx, 220, 22, 10, fill=mix(BG, (90, 90, 90), 1.0))
        if bug:
            y = 220 + ((t * 80) % 500)
            c.ellipse(cx + 30, y, 22, 10, fill=mix(BG, (90, 90, 90), 1.0))
        c.rect(cx - 160, 720, cx - 160 + 320 * air, 750, fill=SPARK, r=6)
        c.text(cx, 790, f'透风（示意）{int(air * 100)}%', 'sans', 22, MUTED, 'mm')
        c.text(cx, 880, lab, 'bold', 26, col, 'mm')
    caps(c, t, [(0, 7, '网眼太大：蚊子一钻就进来'),
                (7.2, 14, '网眼太密：挡住了蚊子，也挡住了风'),
                (14.2, 22, '蚊帐布的网眼刚好比蚊子小一点，风还能吹进来（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B224 蜂巢
def _poly(c, cx, cy, n, R, col, rot=0, outline=None):
    pts = [(cx + R * math.cos(rot + 2 * math.pi * k / n), cy + R * math.sin(rot + 2 * math.pi * k / n)) for k in range(n)]
    c.poly(pts, col)
    if outline:
        pts.append(pts[0]); seg(c, pts, outline, 3)


def b224_area(c, t, i):
    corner_tag(c, 'B224 · 同样的周长，六边形围得最多')
    c.text(60, 96, '三根一样长（24 厘米）的纸条，围成三角形、正方形、六边形：边越多，围住的面积越大', 'serif', 36, INK)
    k = min(3, int(t / 5) + 1)
    items = [(3, 8, '三角形', 27.7), (4, 6, '正方形', 36.0), (6, 4, '六边形', 41.6)]
    for j, (n, side, lab, area) in enumerate(items):
        if j >= k:
            break
        cx = 380 + j * 560
        R = side / (2 * math.sin(math.pi / n)) * 26
        rot = -math.pi / 2 if n == 3 else (math.pi / 4 if n == 4 else 0)
        _poly(c, cx, 520, n, R, mix(BG, WAX, 0.6 + 0.15 * j), rot, INK)
        c.text(cx, 760, lab, 'bold', 30, INK, 'mm')
        c.text(cx, 810, f'约 {area} 平方厘米', 'bold', 26, GREEN if n == 6 else INK, 'mm')
    caps(c, t, [(0, 7, '纸条一样长：周长都是 24 厘米'),
                (7.2, 14, '三角形围得最少，正方形多一些'),
                (14.2, 22, '六边形最多；圆更多，但圆拼不满（面积为计算值）')], y=1010)


def b224_tile(c, t, i):
    corner_tag(c, 'B224 · 能铺满，不留空隙')
    c.text(60, 96, '圆形一个挨一个，中间总留下空隙，浪费蜡；正六边形能一个挨一个铺满，墙还共用：最省材料', 'serif', 36, INK)
    R = 40
    for j in range(2):
        ox = 160 + j * 900
        if j == 0:
            for r in range(6):
                for q in range(9):
                    c.ellipse(ox + q * 2 * R + (R if r % 2 else 0), 280 + r * 1.75 * R, R, R, outline=mix(BG, WAX, 1.0), width=4)
            c.text(ox + 360, 880, '圆形：中间有空隙', 'bold', 26, NRED, 'mm')
        else:
            n = min(54, int(t * 4))
            cnt = 0
            for r in range(6):
                for q in range(9):
                    if cnt >= n:
                        break
                    cx = ox + q * math.sqrt(3) * R + (math.sqrt(3) * R / 2 if r % 2 else 0)
                    cy = 280 + r * 1.5 * R
                    _poly(c, cx, cy, 6, R, mix(BG, WAX, 0.8), math.pi / 6, mix(BG, (160, 110, 30), 1.0))
                    cnt += 1
            c.text(ox + 360, 880, '六边形：铺满，墙共用', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '圆形一个挨一个，中间三角形的空隙浪费了地方'),
                (7.2, 14, '能不留空隙铺满的正多边形只有三种：三角形、正方形、六边形'),
                (14.2, 22, '其中六边形围的面积最大：蜜蜂用最少的蜡盖出最多的格子')], y=1010)


# ---------------------------------------------------------------- B225 镰刀
def b225_chop(c, t, i):
    corner_tag(c, 'B225 · 直直压下去：费劲')
    c.text(60, 96, '刀刃直直地往下压，只靠压力把稻秆压断，要用很大的力；稻秆一弯一躲，还压不断', 'serif', 36, INK)
    cx, cy = 760, 600
    for k in range(7):
        x = cx - 120 + k * 40
        bend = 30 * min(1.0, (t % 7) / 4) * (1 if k % 2 else -1) * 0.5
        c.line([(x, 900), (x + bend, 380)], mix(BG, STALK, 1.0), 10)
    ph = min(1.0, (t % 7) / 4)
    y = 300 + 200 * ph
    c.poly([(cx - 260, y), (cx + 260, y), (cx + 260, y - 60), (cx - 260, y - 40)], mix(BG, BLADE, 1.0))
    c.arrow(cx, y - 180, cx, y - 80, NRED, 6, 16)
    c.text(1450, 500, '只往下压', 'bold', 34, NRED, 'mm')
    c.text(1450, 570, '要用很大的力（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '刀刃平平地压在一束稻秆上，直直往下压'),
                (7.2, 14, '稻秆又韧又会弯，压下去它就往两边躲'),
                (14.2, 22, '要压得很用力才断（实验用塑料刀和纸绳，不用真镰刀）')], y=1010)


def b225_draw(c, t, i):
    corner_tag(c, 'B225 · 勾住往回拉：边压边滑')
    c.text(60, 96, '弯弯的镰刀勾住一把稻秆往回拉：刀刃一边往里压、一边沿着刃口滑过稻秆，像锯一样一点点切开，省力得多', 'serif', 36, INK)
    cx, cy = 900, 600
    ph = (t % 7) / 7
    cut = ph > 0.6
    for k in range(7):
        x = cx - 120 + k * 40
        if cut:
            c.line([(x, 900), (x, 640)], mix(BG, STALK, 1.0), 10)
            c.line([(x + 30, 620), (x + 60, 380)], mix(BG, STALK, 1.0), 10)
        else:
            c.line([(x, 900), (x, 380)], mix(BG, STALK, 1.0), 10)
    bx = cx - 100 + 500 * ph
    pts = [(bx + 260 * math.cos(a), 640 + 160 * math.sin(a)) for a in [math.pi * (0.55 + 0.45 * m / 20) for m in range(21)]]
    seg(c, pts, mix(BG, BLADE, 1.0), 14)
    c.line([(bx + 260 * math.cos(math.pi * 0.55), 640 + 160 * math.sin(math.pi * 0.55)), (bx + 380, 760)], mix(BG, WOOD, 1.0), 22)
    c.arrow(bx + 420, 760, bx + 520, 760, SPARK, 6, 16)
    c.text(1600, 420, '往回拉', 'bold', 34, SPARK, 'mm')
    c.text(1600, 490, '刃口滑过稻秆', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '弯弯的刀刃从侧面勾住一把稻秆'),
                (7.2, 14, '往回一拉：刀刃一边压、一边沿刃口滑，刃上的小齿像锯一样切'),
                (14.2, 22, '比直直压下去省力得多，一拉一大把（示意，以实测为准）')], y=1010)


CLIPS = {
 'B223_网眼': (b223_mesh, 22), 'B223_通风': (b223_air, 22),
 'B223_片头': (titles.opening(BSER, VOL50, SB50, 3, '宋代以后蚊帐普及'), 7),
 'B223_片尾': (titles.closing(BSER, VOL50, SB50, 3, '下集：蜂巢的格子为什么是六边形？'), 7),
 'B224_围面积': (b224_area, 22), 'B224_铺满': (b224_tile, 22),
 'B224_片头': (titles.opening(BSER, VOL50, SB50, 4, '中国古代已有人工养蜂'), 7),
 'B224_片尾': (titles.closing(BSER, VOL50, SB50, 4, '下集：割稻子，为什么拉着割比砍省力？'), 7),
 'B225_直砍': (b225_chop, 22), 'B225_拉切': (b225_draw, 22),
 'B225_片头': (titles.opening(BSER, VOL50, SB50, 5, '商周时已有青铜镰刀'), 7),
 'B225_片尾': (titles.closing(BSER, VOL50, SB50, 5, '下集：鱼钩上为什么要有倒刺？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
