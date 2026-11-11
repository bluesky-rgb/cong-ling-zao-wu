"""第三十八季（古法解密 16.0）第三批：B166 垂线、B167 淘金、B168 沉碗 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s38a import SB38, VOL38, AIR

BRICK = (170, 95, 70)
SANDC = (205, 180, 130)
GOLD = (235, 190, 60)
STEEL = (190, 195, 205)


# ---------------------------------------------------------------- B166 垂线
def b166_plumb(c, t, i):
    corner_tag(c, 'B166 · 重力替人找到竖直方向')
    c.text(60, 96, '吊一颗重物的细线，不管挂在哪儿，静下来都指向地心：墙和它一比，歪没歪一眼就看出来', 'serif', 36, INK)
    for j, (tilt, lab) in enumerate([(0.0, '墙是直的：上下两处距离一样'), (4.0, '墙歪了：上下两处距离不一样')]):
        bx = 300 + j * 880
        a = math.radians(tilt)
        top, bot = 220, 880
        hgt = bot - top
        for row in range(11):
            y = bot - (row + 1) * hgt / 11
            off = (bot - y) * math.tan(a)
            for q in range(3):
                x = bx + off + (q + (row % 2) * 0.5) * 110
                c.rect(x, y, x + 104, y + hgt / 11 - 6, fill=mix(BG, BRICK, 0.85), r=3)
        hx = bx - 70 + hgt * math.tan(a)
        sw = 10 * math.exp(-t * 0.3) * math.sin(t * 3)
        c.line([(hx, top - 20), (hx + sw, bot - 60)], INK, 3)
        c.ellipse(hx + sw, bot - 40, 18, 22, fill=STEEL)
        c.line([(hx - 30, top - 20), (hx + 60, top - 20)], mix(BG, WOOD, 1.0), 10)
        d_top = bx + (bot - top) * math.tan(a) - hx
        d_bot = bx - hx
        if t > 6:
            for yy, d in [(top + 120, (bx + (bot - top - 120) * math.tan(a)) - hx), (bot - 100, (bx + 100 * math.tan(a)) - hx)]:
                c.line([(hx, yy), (hx + d, yy)], SPARK, 4)
                c.text(hx + d / 2, yy - 24, f'{d / 10:.1f} 厘米', 'mono', 20, SPARK, 'mm')
        c.text(bx + 160, 940, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '古人砌墙，要在墙边吊一根挂着重物的细线，叫「悬」'),
                (7.2, 14, '重物总被地球往地心拉，线一静下来，就是一条现成的竖直线'),
                (14.2, 22, '量一量线到墙上、下两处的距离：一样，墙就是直的（示意）')], y=1010)


def b166_damp(c, t, i):
    corner_tag(c, 'B166 · 泡在水里，很快就停')
    c.text(60, 96, '螺母在空气里晃好久才停；泡进一杯水里，水拖着它，几下就静下来了', 'serif', 36, INK)
    for j, (k, lab) in enumerate([(0.08, '在空气中'), (0.9, '泡在水里')]):
        px, py = 520 + j * 880, 230
        L = 560
        th = 0.35 * math.exp(-k * t) * math.cos(t * 2.2)
        bx, by = px + L * math.sin(th), py + L * math.cos(th)
        if j == 1:
            c.rect(px - 180, py + L - 140, px + 180, py + L + 90, fill=mix(BG, WATER, 0.45), outline=mix(BG, WATER_L, 0.8), width=4, r=14)
        c.line([(px - 80, py), (px + 80, py)], mix(BG, WOOD, 1.0), 10)
        c.line([(px, py), (bx, by)], INK, 3)
        c.poly([(bx + 26 * math.cos(q * math.pi / 3), by + 26 * math.sin(q * math.pi / 3)) for q in range(6)], STEEL)
        c.text(px, py + L + 150, lab, 'bold', 26, INK, 'mm')
        amp = 0.35 * math.exp(-k * t)
        c.text(px, py + L + 195, '还在晃' if amp > 0.02 else '停稳了', 'sans', 22, SPARK if amp > 0.02 else GREEN, 'mm')
    caps(c, t, [(0, 7, '把螺母拉偏松手：在空气里，它来回摆个不停'),
                (7.2, 14, '泡进一杯水，水的阻力每摆一次都吃掉一大截'),
                (14.2, 22, '几下就停稳了：这叫阻尼。秒表计时，以实测为准')], y=1010)


# ---------------------------------------------------------------- B167 淘金
def _pan(c, cx, cy, w, ang):
    ca, sa = math.cos(ang), math.sin(ang)
    def rot(x, y): return (cx + x * ca - y * sa, cy + x * sa + y * ca)
    c.poly([rot(-w, -20), rot(w, -20), rot(w * 0.8, 50), rot(-w * 0.8, 50)], mix(BG, (90, 90, 95), 0.9))
    return rot


def b167_settle(c, t, i):
    corner_tag(c, 'B167 · 重的沉得快')
    c.text(60, 96, '一杯水里同时放下沙粒和金粒：金子比沙子重约 7 倍，一眨眼就沉到底，沙子还在慢慢往下飘', 'serif', 36, INK)
    cx, top, bot = 700, 260, 900
    c.rect(cx - 300, top, cx + 300, bot, fill=mix(BG, WATER, 0.35), outline=mix(BG, WATER_L, 0.7), width=5, r=12)
    r = random.Random(7)
    tt = t % 11
    for k in range(60):
        x = cx - 260 + r.uniform(0, 520)
        gold = k < 8
        v = 140 if gold else 22 + r.uniform(0, 14)
        y = min(bot - 14 - (0 if gold else 8 + (k % 5) * 6), top + 40 + v * tt)
        if gold:
            c.ellipse(x, y, 9, 9, fill=GOLD)
        else:
            c.ellipse(x + 6 * math.sin(tt * 2 + k), y, 7, 7, fill=SANDC)
    c.rect(1180, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1520, 350, '每立方厘米有多重', 'bold', 26, INK, 'mm')
    for k, (lab, g, col) in enumerate([('水', 1.0, WATER_L), ('沙子', 2.65, SANDC), ('金', 19.3, GOLD)]):
        y = 420 + k * 70
        c.text(1220, y, lab, 'sans', 24, INK, 'lm')
        c.rect(1320, y - 16, 1320 + g * 24, y + 16, fill=col, r=6)
        c.text(1330 + g * 24, y, f'{g} 克', 'mono', 22, INK, 'lm')
    c.text(1520, 700, '实验用小钢珠代替金子（约 7.9 克）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '沙粒和金粒一起掉进水里'),
                (7.2, 14, '金子又重又密，水几乎拦不住它，一下就沉到底'),
                (14.2, 22, '沙子轻得多，在水里慢慢飘：淘金就靠这个时间差（示意）')], y=1010)


def b167_pan(c, t, i):
    corner_tag(c, 'B167 · 一圈圈晃，沙被冲走')
    c.text(60, 96, '盘子在水里轻轻转圈晃：轻的沙子被水托起来冲出盘沿，重的钢珠一直留在盘底', 'serif', 36, INK)
    cx, cy = 760, 600
    c.rect(200, 470, 1320, 900, fill=mix(BG, WATER, 0.3), r=20)
    ang = -0.18 + 0.06 * math.sin(t * 3)
    rot = _pan(c, cx, cy, 380, ang)
    p = min(1.0, t / 18)
    r = random.Random(4)
    nsand = int(70 * (1 - p))
    for k in range(70):
        x = r.uniform(-330, 330)
        y = r.uniform(-5, 40)
        if k < nsand:
            px, py = rot(x + 8 * math.sin(t * 3 + k), y)
            c.ellipse(px, py, 7, 7, fill=SANDC)
        else:
            f = ((t * 0.5 + k * 0.13) % 1)
            px, py = rot(-380 - f * 250, -20 + f * 120)
            if py < 900:
                c.ellipse(px, py, 6, 6, fill=mix(BG, SANDC, 0.6))
    for k in range(10):
        px, py = rot(-120 + k * 26, 42)
        c.ellipse(px, py, 9, 9, fill=STEEL)
    c.rect(1420, 360, 1860, 600, fill=SHEET, r=12)
    c.text(1640, 410, '盘里还剩', 'bold', 26, INK, 'mm')
    c.text(1640, 480, f'沙子 {100 * (1 - p):.0f}%', 'mono', 28, SANDC, 'mm')
    c.text(1640, 540, '钢珠 10 颗', 'mono', 28, STEEL, 'mm')
    c.text(1640, 660, '晃太猛，钢珠也会被冲走', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '盘子没进水里，端着轻轻转圈晃'),
                (7.2, 14, '晃动把沙子掀起来，盘子一斜，水就把上层的沙带出盘沿'),
                (14.2, 22, '重的钢珠一直贴着盘底：古人叫「披沙拣金」（示意）')], y=1010)


# ---------------------------------------------------------------- B168 沉碗
def b168_sink(c, t, i):
    corner_tag(c, 'B168 · 小孔慢慢进水，装满就沉')
    c.text(60, 96, '碗底一个小孔，水一点点渗进来；碗越来越重、越吃越深，到某一刻「咕咚」一下沉底', 'serif', 36, INK)
    cx = 760
    surf, bot = 420, 920
    c.rect(240, surf, 1280, bot, fill=mix(BG, WATER, 0.4), r=12)
    T = 16.0
    tt = min(t, T + 6)
    fill = min(1.0, tt / T)
    sink = 0.0 if tt < T else min(1.0, (tt - T) / 1.2)
    dip = 30 + 90 * fill ** 1.3
    by0 = surf - 90 + dip
    by = by0 + sink * (bot - 136 - by0)
    c.poly([(cx - 220, by), (cx + 220, by), (cx + 140, by + 130), (cx - 140, by + 130)], mix(BG, (225, 225, 230), 0.9))
    wl = by + 130 - 120 * fill
    c.poly([(cx - 140 - 80 * (1 - (wl - by) / 130), wl), (cx + 140 + 80 * (1 - (wl - by) / 130), wl), (cx + 140, by + 126), (cx - 140, by + 126)], mix(BG, WATER, 0.8))
    if sink == 0:
        for k in range(3):
            yy = by + 126 - ((t * 60 + k * 15) % 40)
            c.ellipse(cx, yy, 4, 6, fill=WATER_L)
    c.rect(1380, 300, 1860, 560, fill=SHEET, r=12)
    c.text(1620, 350, '秒表', 'bold', 26, INK, 'mm')
    c.text(1620, 430, f'{min(tt, T) * 15:.0f} 秒', 'mono', 44, SPARK, 'mm')
    c.text(1620, 510, '沉了！' if sink > 0 else '还在漂', 'bold', 26, GREEN if sink > 0 else MUTED, 'mm')
    caps(c, t, [(0, 7, '碗底只有一个图钉扎出的小孔，水只能慢慢渗进来'),
                (7.2, 14, '碗里的水越来越多，碗越吃越深，可还漂着'),
                (14.2, 22, '装到一定程度，突然沉底：每次用的时间都差不多（时间以实测为准）')], y=1010)


def b168_holes(c, t, i):
    corner_tag(c, 'B168 · 孔越多越大，沉得越快')
    c.text(60, 96, '同样的碗：1 个孔、3 个孔、1 个大孔，进水快慢不同，沉没的时间也就不同', 'serif', 36, INK)
    base = 300
    for j, (lab, rate) in enumerate([('1 个小孔', 1.0), ('3 个小孔', 3.0), ('1 个大孔', 2.2)]):
        cx = 380 + j * 580
        fill = min(1.0, t * rate / 20)
        c.rect(cx - 220, 380, cx + 220, 700, fill=mix(BG, WATER, 0.35), r=10)
        sunk = fill >= 1
        by = 330 + 60 * fill if not sunk else 600
        c.poly([(cx - 150, by), (cx + 150, by), (cx + 100, by + 80), (cx - 100, by + 80)], mix(BG, (225, 225, 230), 0.9))
        c.rect(cx - 160, 760, cx + 160, 800, fill=mix(BG, LINE, 0.6), r=8)
        c.rect(cx - 160, 760, cx - 160 + 320 * fill, 800, fill=SPARK, r=8)
        c.text(cx, 850, lab, 'bold', 26, INK, 'mm')
        tsec = 20 / rate * 15
        c.text(cx, 895, f'约 {tsec:.0f} 秒沉底（示意）', 'sans', 22, MUTED, 'mm')
        for q in range({'1 个小孔': 1, '3 个小孔': 3, '1 个大孔': 1}[lab]):
            c.ellipse(cx - 30 * (q - 1 if lab == '3 个小孔' else 0), by + 80, 5 if lab != '1 个大孔' else 9, 4, fill=INK)
    caps(c, t, [(0, 7, '孔越多、越大，每秒渗进来的水越多'),
                (7.2, 14, '碗满得快，沉得就早；想量多长的时间，就挑多大的孔'),
                (14.2, 22, '古人一碗沉了就再放一碗，数沉了几碗，就知道过了多久（示意）')], y=1010)


CLIPS = {
 'B166_吊线': (b166_plumb, 22), 'B166_阻尼': (b166_damp, 22),
 'B166_片头': (titles.opening(BSER, VOL38, SB38, 6, '古人筑墙用「县」吊重物定垂直'), 7),
 'B166_片尾': (titles.closing(BSER, VOL38, SB38, 6, '下集：在水里晃一晃，怎么就留下了金粒？'), 7),
 'B167_沉降': (b167_settle, 22), 'B167_晃盘': (b167_pan, 22),
 'B167_片头': (titles.opening(BSER, VOL38, SB38, 7, '古人在河边「披沙拣金」'), 7),
 'B167_片尾': (titles.closing(BSER, VOL38, SB38, 7, '下集：碗底钻个孔，怎么就能计时？'), 7),
 'B168_沉没': (b168_sink, 22), 'B168_孔': (b168_holes, 22),
 'B168_片头': (titles.opening(BSER, VOL38, SB38, 8, '古印度和波斯曾用沉碗计时'), 7),
 'B168_片尾': (titles.closing(BSER, VOL38, SB38, 8, '下集：锣为什么越敲音越滑？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
