"""第四十季（古法解密 17.0）第三批：B176 渔网、B177 鱼篓、B178 锯子 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s40a import SB40, VOL40, AIR

NETC = (200, 200, 180)
FLOAT = (240, 120, 90)
SINK = (150, 150, 160)
FISH = (230, 180, 90)
BAMBOO = (180, 170, 90)
STEEL = (180, 185, 195)


# ---------------------------------------------------------------- B176 渔网
def _net(c, x0, y0, x1, y1, cell, col):
    x = x0
    while x <= x1 + 1:
        c.line([(x, y0), (x, y1)], col, 2)
        x += cell
    y = y0
    while y <= y1 + 1:
        c.line([(x0, y), (x1, y)], col, 2)
        y += cell


def b176_float(c, t, i):
    corner_tag(c, 'B176 · 上浮下坠，把网拉成一道墙')
    c.text(60, 96, '网的上边挂着浮子往上浮，下边挂着坠子往下沉：一上一下把网拉直，在水里竖成一道墙', 'serif', 36, INK)
    cases = [('只有浮子：网漂在水面', True, False), ('浮子 + 坠子：竖起来', True, True), ('只有坠子：沉到底团成一堆', False, True)]
    for j, (lab, fl, sk) in enumerate(cases):
        cx = 330 + j * 630
        wy = 300
        c.rect(cx - 280, wy, cx + 280, 900, fill=mix(BG, WATER, 0.4))
        p = min(1.0, t / 8)
        if fl and sk:
            top, bot = wy + 10, wy + 10 + 480 * p + 40
            _net(c, cx - 200, top, cx + 200, bot, 40, NETC)
            for k in range(5):
                c.ellipse(cx - 200 + k * 100, top, 14, 14, fill=FLOAT)
                c.rect(cx - 210 + k * 100, bot, cx - 190 + k * 100, bot + 20, fill=SINK, r=4)
        elif fl:
            _net(c, cx - 200, wy + 4, cx + 200, wy + 40, 20, NETC)
            for k in range(5):
                c.ellipse(cx - 200 + k * 100, wy + 4, 14, 14, fill=FLOAT)
        else:
            y = wy + 20 + p * 820
            yy = min(860, y)
            _net(c, cx - 120, yy - 30, cx + 120, yy, 15, NETC)
            for k in range(5):
                c.rect(cx - 110 + k * 50, yy, cx - 90 + k * 50, yy + 20, fill=SINK, r=4)
        c.text(cx, 950, lab, 'bold', 22, GREEN if fl and sk else NRED, 'mm')
    caps(c, t, [(0, 7, '浮子是木头、泡沫这类轻东西，坠子是石头、陶块、铅块'),
                (7.2, 14, '浮子把网的上边托在水面，坠子把下边往下拽'),
                (14.2, 22, '两边一拉，网就像一道墙竖在水里，鱼游过来就被拦住（示意）')], y=1010)


def b176_mesh(c, t, i):
    corner_tag(c, 'B176 · 网眼决定留下谁')
    c.text(60, 96, '网眼比鱼大，鱼钻过去；网眼比鱼小，鱼就被拦下：网眼大小，就是一把「筛子」', 'serif', 36, INK)
    for j, (lab, cell) in enumerate([('大网眼：小鱼都游过去了', 50), ('小网眼：大鱼小鱼一网打尽', 16)]):
        cx, cy = 520 + j * 880, 560
        c.rect(cx - 360, 260, cx + 360, 860, fill=mix(BG, WATER, 0.35))
        for k in range(0, 560 // cell + 1):
            y = 280 + k * cell
            c.line([(cx - 10, y), (cx + 10, y)], NETC, 3)
        c.line([(cx - 10, 280), (cx - 10, 840)], NETC, 3)
        c.line([(cx + 10, 280), (cx + 10, 840)], NETC, 3)
        r = random.Random(3)
        for k in range(10):
            size = 14 if k % 2 else 42
            y = 320 + k * 52
            sp = 0.25 + r.uniform(0, 0.15)
            x = cx - 330 + ((t * sp * 200 + k * 60) % 700)
            passes = size < cell * 0.8
            if not passes and x > cx - 12 - size:
                x = cx - 12 - size
            c.ellipse(x, y, size, size * 0.55, fill=FISH)
        c.text(cx, 920, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '同样一群鱼，大的小的都往网游过来'),
                (7.2, 14, '网眼大，小鱼从格子里钻过去，只留下大鱼'),
                (14.2, 22, '古人很早就有「数罟不入洿池」的说法：网眼别太小，给小鱼留条活路（拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- B177 鱼篓
def _trap(c, cx, cy):
    c.rect(cx - 360, cy - 140, cx + 300, cy + 140, fill=mix(BG, BAMBOO, 0.3), outline=mix(BG, BAMBOO, 1.0), width=6, r=60)
    c.line([(cx - 360, cy - 140), (cx - 200, cy - 30)], mix(BG, BAMBOO, 1.0), 6)
    c.line([(cx - 360, cy + 140), (cx - 200, cy + 30)], mix(BG, BAMBOO, 1.0), 6)


def b177_funnel(c, t, i):
    corner_tag(c, 'B177 · 往里收的倒须')
    c.text(60, 96, '篓口装着一圈往里收的竹签，像一个漏斗：从外往里，入口又宽又顺；从里往外，只剩中间一个小口', 'serif', 36, INK)
    cx, cy = 900, 560
    c.rect(100, 260, 1820, 880, fill=mix(BG, WATER, 0.35))
    _trap(c, cx, cy)
    T = 8
    ph = (t % T) / T
    fx = 300 + ph * 700
    fy = cy + 60 * math.sin(ph * 6) * (1 - min(1, ph * 1.5))
    if fx > cx - 200:
        fy = cy + 50 * math.sin(t * 2)
        fx = min(fx, cx + 200)
    c.ellipse(fx, fy, 40, 20, fill=FISH)
    c.poly([(fx - 40, fy), (fx - 64, fy - 16), (fx - 64, fy + 16)], FISH)
    for k in range(3):
        y = cy - 100 + k * 100
    c.text(cx - 200, cy - 200, '外面：宽口，一路往里收', 'sans', 22, GREEN, 'mm')
    c.text(cx + 120, cy + 210, '里面：沿着篓壁转，很难正好对准中间小口', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '鱼顺着水流和漏斗形的倒须往里钻，竹签被挤开，很顺利'),
                (7.2, 14, '进去以后，鱼沿着篓壁游来游去，碰到的都是竹签的尖端或篓壁'),
                (14.2, 22, '只有正好对准中间那个小口才出得去，所以进去容易、出来难（示意）')], y=1010)


def b177_inout(c, t, i):
    corner_tag(c, 'B177 · 晃 30 秒：进去几颗，出来几颗')
    c.text(60, 96, '塑料瓶做的漏斗陷阱：外面撒 10 颗弹珠晃 30 秒，进去不少；里面放 10 颗晃 30 秒，几乎出不来', 'serif', 36, INK)
    p = min(1.0, t / 16)
    for j, (lab, n) in enumerate([('从外往里：进去', int(6 * p)), ('从里往外：出来', int(1 * p))]):
        cx, cy = 520 + j * 880, 520
        c.rect(cx - 360, cy - 220, cx + 360, cy + 220, fill=mix(BG, (200, 190, 170), 0.2), r=12)
        c.rect(cx - 200, cy - 110, cx + 300, cy + 110, fill=mix(BG, (210, 220, 230), 0.2), outline=mix(BG, (210, 220, 230), 0.8), width=4, r=50)
        c.line([(cx - 200, cy - 110), (cx - 80, cy - 20)], mix(BG, (210, 220, 230), 0.9), 4)
        c.line([(cx - 200, cy + 110), (cx - 80, cy + 20)], mix(BG, (210, 220, 230), 0.9), 4)
        r = random.Random(j)
        inside = n if j == 0 else 10 - n
        for k in range(10):
            if k < inside:
                x = cx - 40 + r.uniform(0, 300)
                y = cy - 80 + r.uniform(0, 160)
            else:
                x = cx - 340 + r.uniform(0, 120)
                y = cy - 200 + r.uniform(0, 400)
            c.ellipse(x + 4 * math.sin(t * 5 + k), y, 14, 14, fill=mix(BG, (120, 180, 230), 1.0))
        c.text(cx, cy + 290, lab, 'bold', 26, INK, 'mm')
        c.text(cx, cy + 340, f'{n} 颗（示意，以实测为准）', 'mono', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '同样晃 30 秒，弹珠在托盘里乱滚'),
                (7.2, 14, '从外面滚进漏斗口的，被斜面一路引进瓶里'),
                (14.2, 22, '瓶里的弹珠碰到的大多是瓶壁和漏斗外侧，很少正好滚出小口')], y=1040)


# ---------------------------------------------------------------- B178 锯子
def b178_teeth(c, t, i):
    corner_tag(c, 'B178 · 一排小凿子')
    c.text(60, 96, '每个锯齿都是一把小凿子：往前推一下，每个齿刮掉一点木头，一排齿一起，锯缝一点点变深', 'serif', 36, INK)
    wy = 520
    c.rect(200, wy, 1700, 860, fill=mix(BG, WOOD, 0.85))
    off = 60 * math.sin(t * 3)
    depth = min(200, t * 10)
    c.rect(440, wy, 1500, wy + depth, fill=BG)
    y0 = wy + depth
    pts = []
    for k in range(30):
        x = 520 + k * 30 + off
        pts += [(x, y0 - 4), (x + 15, y0 + 18), (x + 30, y0 - 4)]
    c.rect(520 + off, y0 - 120, 1420 + off, y0 - 4, fill=mix(BG, STEEL, 0.9))
    c.poly([(520 + off, y0 - 4)] + pts + [(1420 + off, y0 - 4)], mix(BG, STEEL, 1.0))
    r = random.Random(2)
    for k in range(20):
        x = 700 + r.uniform(0, 500)
        yy = 470 - ((t * 60 + k * 23) % 120)
        if 440 < x < 1500:
            c.rect(x, yy, x + 6, yy + 4, fill=mix(BG, (220, 190, 140), 1.0))
    c.arrow(1500, 300, 1620, 300, SPARK, 5, 14)
    c.arrow(1500, 340, 1380, 340, SPARK, 5, 14)
    c.text(1500, 260, '来回拉', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '刀刃是一条线，压下去只能挤；锯齿是一排尖，能「啃」'),
                (7.2, 14, '每推一下，每个齿各刮下一小片木屑'),
                (14.2, 22, '几十个齿一起干活，锯缝很快变深（示意）')], y=1010)


def b178_kerf(c, t, i):
    corner_tag(c, 'B178 · 齿尖一左一右，锯缝比锯条宽')
    c.text(60, 96, '从锯条正前方看：齿尖一个往左掰、一个往右掰，锯出的缝比锯条本身宽，锯条在缝里不会被夹住', 'serif', 36, INK)
    for j, (lab, setw) in enumerate([('齿排成一线：缝 = 锯条宽，被夹住', 0), ('齿左右错开：缝比锯条宽，进出顺畅', 22)]):
        cx, cy = 520 + j * 880, 540
        c.rect(cx - 300, cy - 260, cx - 12 - setw, cy + 260, fill=mix(BG, WOOD, 0.85))
        c.rect(cx + 12 + setw, cy - 260, cx + 300, cy + 260, fill=mix(BG, WOOD, 0.85))
        c.rect(cx - 8, cy - 280, cx + 8, cy + 200, fill=mix(BG, STEEL, 1.0))
        if setw:
            c.poly([(cx - 8, cy + 200), (cx - 8 - setw, cy + 250), (cx + 2, cy + 250)], mix(BG, STEEL, 1.0))
            c.poly([(cx + 8, cy + 200), (cx + 8 + setw, cy + 250), (cx - 2, cy + 250)], mix(BG, STEEL, 0.8))
        else:
            c.poly([(cx - 8, cy + 200), (cx + 8, cy + 200), (cx, cy + 250)], mix(BG, STEEL, 1.0))
            for sgn in (-1, 1):
                c.arrow(cx + sgn * 120, cy - 100, cx + sgn * 14, cy - 100, NRED, 5, 14)
        c.text(cx, 870, lab, 'bold', 22, GREEN if setw else NRED, 'mm')
    caps(c, t, [(0, 7, '木头被锯开后会微微往回挤，还有木屑塞在缝里'),
                (7.2, 14, '齿排成一条线，缝和锯条一样宽，越锯越紧，最后拉不动'),
                (14.2, 22, '齿尖左右错开，缝比锯条宽一点，这叫「锯路」：锯条进出顺畅，木屑也能掉出来')], y=1010)


CLIPS = {
 'B176_浮坠': (b176_float, 22), 'B176_网眼': (b176_mesh, 22),
 'B176_片头': (titles.opening(BSER, VOL40, SB40, 6, '新石器时代已有网坠出土'), 7),
 'B176_片尾': (titles.closing(BSER, VOL40, SB40, 6, '下集：鱼为什么钻得进鱼篓，却出不来？'), 7),
 'B177_倒须': (b177_funnel, 22), 'B177_进出': (b177_inout, 22),
 'B177_片头': (titles.opening(BSER, VOL40, SB40, 7, '古代竹编鱼笱口部有向内的倒须'), 7),
 'B177_片尾': (titles.closing(BSER, VOL40, SB40, 7, '下集：锯齿为什么要一左一右地错开？'), 7),
 'B178_锯齿': (b178_teeth, 22), 'B178_锯路': (b178_kerf, 22),
 'B178_片头': (titles.opening(BSER, VOL40, SB40, 8, '春秋时期已有青铜锯'), 7),
 'B178_片尾': (titles.closing(BSER, VOL40, SB40, 8, '下集：石碑上的字，怎么「拍」到纸上？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
