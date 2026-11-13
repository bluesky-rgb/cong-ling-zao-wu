"""第四十三季（第十八层：工具箱）第二批：E225 棘轮、E226 老虎钳、E227 千斤顶 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s43a import S43A, SER43, VOL43, STEEL, BOLT

HANDLE = (200, 60, 60)
BOOK = (120, 150, 200)
PAWL = (230, 180, 70)


def _ratchet(c, cx, cy, R, rot, n=12, col=STEEL):
    pts = []
    for k in range(n):
        a0 = rot + 2 * math.pi * k / n
        a1 = rot + 2 * math.pi * (k + 1) / n
        pts.append((cx + (R - 30) * math.cos(a0), cy + (R - 30) * math.sin(a0)))
        pts.append((cx + R * math.cos(a1 - 0.02), cy + R * math.sin(a1 - 0.02)))
        pts.append((cx + (R - 30) * math.cos(a1), cy + (R - 30) * math.sin(a1)))
    c.poly(pts, mix(BG, col, 1.0))
    c.ellipse(cx, cy, 24, 24, fill=BG)


# ---------------------------------------------------------------- E225 棘轮
def e225_oneway(c, t, i):
    corner_tag(c, '第 225 集 · 斜齿加卡爪')
    c.text(60, 96, '齿一边缓坡、一边陡壁，卡爪被弹簧压在齿上：顺着缓坡转，卡爪滑过「咔哒」；反着转，卡爪顶住陡壁', 'serif', 35, INK)
    for j, (lab, dirn) in enumerate([('顺着缓坡转：卡爪滑过，咔哒咔哒', 1), ('反着转：卡爪顶住陡壁，卡死', -1)]):
        cx, cy = 480 + j * 960, 560
        R = 240
        if dirn == 1:
            rot = t * 0.6
        else:
            rot = 0.04 * math.sin(t * 6)
        _ratchet(c, cx, cy, R, rot)
        step = 2 * math.pi / 12
        ph = ((-math.pi / 2 - rot) % step) / step
        rim = R - 30 + 30 * ph
        px, py = cx, cy - rim + 4
        c.poly([(px - 110, py - 40), (px - 100, py - 60), (px + 4, py - 6), (px - 4, py + 4)], mix(BG, PAWL, 1.0))
        c.ellipse(px - 105, py - 50, 10, 10, fill=INK)
        c.line([(px - 60, py - 40), (px - 60, py - 110)], mix(BG, MUTED, 0.8), 3)
        c.text(px - 50, py - 120, '弹簧', 'sans', 18, MUTED, 'lm')
        if dirn == 1:
            c.arc(cx, cy, R + 60, R + 60, 20, 80, GREEN, 6)
            if ph > 0.85:
                c.text(cx + 220, cy - 260, '咔哒', 'bold', 30, SPARK, 'mm')
        else:
            c.arc(cx, cy, R + 60, R + 60, 100, 160, NRED, 6)
        c.text(cx, cy + R + 90, lab, 'bold', 26, GREEN if dirn == 1 else NRED, 'mm')
    caps(c, t, [(0, 7, '棘轮的每个齿都是歪的：一边缓缓地爬上去，另一边直直地落下来'),
                (7.2, 14, '顺着缓坡转，卡爪被齿顶起来又落下去，每过一个齿就「咔哒」一声'),
                (14.2, 22, '反过来转，卡爪的尖正好抵住陡壁：只能往一个方向走（示意）')], y=1010)


def e225_wrench(c, t, i):
    corner_tag(c, '第 225 集 · 不用松开就能来回拧')
    c.text(60, 96, '普通扳手拧半圈就碰到墙，要拿下来换个角度再套上；棘轮扳手来回摆就行：往前摆带着螺母转，往回摆空转', 'serif', 35, INK)
    cx, cy = 760, 560
    T = 3.0
    ph = (t % T) / T
    swing = math.sin(ph * 2 * math.pi)
    ang = math.radians(-60 + 50 * swing)
    nut_rot = math.radians(50 * 2 * (int(t / T)) + (50 * swing + 50 if swing > 0 else 0))
    c.rect(1250, 260, 1290, 860, fill=mix(BG, (110, 105, 100), 1.0))
    c.text(1300, 300, '墙', 'sans', 22, MUTED, 'lm')
    fwd = math.cos(ph * 2 * math.pi) > 0
    c.poly([(cx + 70 * math.cos(math.radians(60 * k + 30) + nut_rot * 0.3), cy + 70 * math.sin(math.radians(60 * k + 30) + nut_rot * 0.3)) for k in range(6)], mix(BG, BOLT, 1.0))
    ex, ey = cx + 450 * math.cos(ang), cy + 450 * math.sin(ang)
    c.ellipse(cx, cy, 110, 110, outline=STEEL, width=26)
    c.line([(cx + 110 * math.cos(ang), cy + 110 * math.sin(ang)), (ex, ey)], mix(BG, STEEL, 1.0), 40)
    c.text(cx, cy + 220, '往前摆：带着螺母转' if fwd else '往回摆：棘轮空转，咔哒咔哒', 'bold', 28, GREEN if fwd else SPARK, 'mm')
    caps(c, t, [(0, 7, '在墙角、在窄缝里，扳手只能来回摆一点点'),
                (7.2, 14, '棘轮扳手往前摆时卡爪卡住，带着螺母转；往回摆时卡爪滑过，螺母不动'),
                (14.2, 22, '扎带、卷尺的锁、自行车后轮的飞轮，里面都有棘轮（示意）')], y=1010)


# ---------------------------------------------------------------- E226 老虎钳
def e226_lever(c, t, i):
    corner_tag(c, '第 226 集 · 两根杠杆，一个转轴')
    c.text(60, 96, '手握的地方离转轴远，钳口离转轴近：手柄 15 厘米、钳口 3 厘米，手上的力到钳口就放大了大约 5 倍', 'serif', 36, INK)
    px, py = 700, 540
    op = math.radians(6 + 4 * math.sin(t * 1.5))
    for s in (1, -1):
        a = s * op
        hx, hy = px + 900 * math.cos(a), py + 900 * math.sin(a) * 1
        jx, jy = px - 250 * math.cos(a), py - 250 * math.sin(a)
        c.line([(px, py), (hx, hy)], mix(BG, HANDLE, 1.0), 40)
        c.line([(px, py), (jx, jy)], mix(BG, STEEL, 1.0), 44)
    c.ellipse(px, py, 26, 26, fill=INK)
    c.arrow(px + 820, py - 230, px + 820, py - 120, SPARK, 6, 18)
    c.arrow(px + 820, py + 230, px + 820, py + 120, SPARK, 6, 18)
    c.text(px + 860, py - 200, '手：1 份力', 'bold', 26, SPARK, 'lm')
    c.arrow(px - 200, py - 180, px - 200, py - 50, NRED, 10, 26)
    c.arrow(px - 200, py + 180, px - 200, py + 50, NRED, 10, 26)
    c.text(px - 230, py - 210, '钳口：约 5 份力', 'bold', 26, NRED, 'mm')
    c.line([(px, py + 300), (px + 820, py + 300)], MUTED, 2)
    c.text(px + 410, py + 330, '手柄 15 厘米', 'sans', 22, MUTED, 'mm')
    c.line([(px - 200, py + 300), (px, py + 300)], MUTED, 2)
    c.text(px - 100, py + 330, '3 厘米', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '老虎钳是两根杠杆，用一颗铆钉连在一起，铆钉就是支点'),
                (7.2, 14, '手离支点远，钳口离支点近：远处的一点力，在近处变成很大的力'),
                (14.2, 22, '力乘距离两边相等：15 比 3，大约放大 5 倍（以实测为准）')], y=1010)


def e226_cutter(c, t, i):
    corner_tag(c, '第 226 集 · 剪口离转轴最近')
    c.text(60, 96, '同一把钳子，夹在钳口尖上、中间、还是靠近转轴的剪口上，放大的倍数不一样：越靠近转轴，力越大', 'serif', 36, INK)
    pos = [('钳尖：离轴 3 厘米', 3), ('中间：离轴 2 厘米', 2), ('剪口：离轴 1 厘米', 1)]
    p = min(1.0, t / 12)
    for k, (lab, d) in enumerate(pos):
        y = 340 + k * 170
        mult = 15 / d
        w = mult / 15 * 1000 * p
        c.text(420, y, lab, 'bold', 26, INK, 'rm')
        c.rect(460, y - 34, 460 + w, y + 34, fill=mix(BG, NRED if d == 1 else SPARK, 0.85), r=10)
        c.text(480 + w, y, f'约 {mult:.1f} 倍', 'mono', 24, INK, 'lm')
    c.text(960, 860, '手握在离转轴 15 厘米处（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '钳尖离转轴最远，放大得最少，适合夹细小的东西'),
                (7.2, 14, '剪口做在离转轴最近的地方，放大得最多，用来剪铁丝'),
                (14.2, 22, '剪铁丝由大人来：断头会弹，戴眼镜、朝下剪')], y=1010)


# ---------------------------------------------------------------- E227 千斤顶
def e227_screw(c, t, i):
    corner_tag(c, '第 227 集 · 螺纹是绕起来的斜面')
    c.text(60, 96, '把一张直角三角形的纸卷到铅笔上，斜边就绕成了螺纹：螺纹就是一个很长很缓的斜面，绕着轴往上爬', 'serif', 36, INK)
    p = min(1.0, t / 12)
    x0, y0 = 160, 820
    W, H = 900, 180
    c.poly([(x0, y0), (x0 + W, y0), (x0 + W, y0 - H)], mix(BG, (230, 225, 210), 0.8))
    c.text(x0 + W / 2, y0 + 40, '展开：很长很缓的斜面', 'sans', 24, MUTED, 'mm')
    cx = 1450
    top, bot = 300, 840
    c.rect(cx - 70, top, cx + 70, bot, fill=mix(BG, BOLT, 0.7), r=10)
    turns = 6
    n = int(turns * 40 * p)
    for k in range(n):
        u0, u1 = k / (turns * 40), (k + 1) / (turns * 40)
        a0, a1 = u0 * turns * 2 * math.pi, u1 * turns * 2 * math.pi
        y_0 = bot - u0 * (bot - top)
        y_1 = bot - u1 * (bot - top)
        front0, front1 = math.sin(a0) > 0, math.sin(a1) > 0
        col = SPARK if front0 else mix(BG, SPARK, 0.4)
        c.line([(cx + 90 * math.cos(a0), y_0 + 14 * math.sin(a0)), (cx + 90 * math.cos(a1), y_1 + 14 * math.sin(a1))], col, 6)
    c.arrow(1080, 700, 1330, 640, mix(BG, MUTED, 0.8), 4, 14)
    c.text(1200, 600, '卷起来', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '推重物上斜面，坡越缓越省力，但要走更长的路'),
                (7.2, 14, '螺纹就是把一条很长的缓坡绕在一根轴上，占的地方很小'),
                (14.2, 22, '转一圈，只往上爬一个螺距：手走得远，重物升得少（示意）')], y=1010)


def e227_work(c, t, i):
    corner_tag(c, '第 227 集 · 手走得远，重物升得少')
    c.text(60, 96, '手柄转一大圈，手走了大约 60 厘米，箱子只升了 2 毫米：路程差 300 倍，力就能小很多（还要扣掉摩擦）', 'serif', 35, INK)
    T = 8
    ph = (t % T) / T
    turns = ph * 3
    cx, cy = 560, 600
    c.ellipse(cx, cy, 200, 200, outline=mix(BG, MUTED, 0.6), width=3)
    a = turns * 2 * math.pi
    hx, hy = cx + 200 * math.cos(a), cy + 200 * math.sin(a)
    c.line([(cx, cy), (hx, hy)], HANDLE, 16)
    c.ellipse(hx, hy, 24, 24, fill=HANDLE)
    arc_pts = [(cx + 200 * math.cos(u * a / 60), cy + 200 * math.sin(u * a / 60)) for u in range(61)]
    if a > 0.05:
        c.line(arc_pts, SPARK, 6)
    c.text(cx, cy + 270, f'手走了约 {turns * 60:.0f} 厘米', 'bold', 28, SPARK, 'mm')
    bx, by = 1350, 760
    lift = turns * 2 * 8
    c.rect(bx - 60, by - 20 - lift, bx + 60, by + 80, fill=mix(BG, STEEL, 0.8))
    c.rect(bx - 200, by - 200 - lift, bx + 200, by - 20 - lift, fill=mix(BG, BOOK, 1.0), r=8)
    c.text(bx, by - 110 - lift, '一箱书', 'bold', 26, BG, 'mm')
    c.rect(bx - 260, by + 80, bx + 260, by + 100, fill=mix(BG, MUTED, 0.5))
    c.text(bx, by + 140, f'箱子升高约 {turns * 2:.0f} 毫米（画面放大）', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '手柄转一圈，手沿着圆走了一大圈；螺杆只往上顶了一个螺距'),
                (7.2, 14, '手走的路是箱子升高的几百倍：做的功差不多，力就小了很多'),
                (14.2, 22, '千斤顶由大人操作，只顶纸箱；任何时候手脚都不放到顶起的东西下面')], y=1010)


CLIPS = {
 'E225_单向': (e225_oneway, 22), 'E225_来回': (e225_wrench, 22),
 'E225_片头': (titles.opening(SER43, VOL43, S43A, 3, '棘轮机构古已有之，19 世纪用于棘轮扳手'), 7),
 'E225_片尾': (titles.closing(SER43, VOL43, S43A, 3, '下集：老虎钳为什么越靠近转轴越好剪？'), 7),
 'E226_杠杆': (e226_lever, 22), 'E226_剪口': (e226_cutter, 22),
 'E226_片头': (titles.opening(SER43, VOL43, S43A, 4, '古代已有铁钳，19 世纪出现带剪口的钢丝钳'), 7),
 'E226_片尾': (titles.closing(SER43, VOL43, S43A, 4, '下集：摇几下手柄，怎么就顶起了一辆车？'), 7),
 'E227_螺纹': (e227_screw, 22), 'E227_功': (e227_work, 22),
 'E227_片头': (titles.opening(SER43, VOL43, S43A, 5, '19 世纪出现螺旋千斤顶和液压千斤顶'), 7),
 'E227_片尾': (titles.closing(SER43, VOL43, S43A, 5, '下集：一根铁钉，怎么变成一块磁铁？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
