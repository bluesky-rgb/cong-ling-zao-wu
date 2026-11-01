"""第十一季第三批：B36 古埃及搬巨石、B37 阿拉伯星盘、B38 安提基特拉机械 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s9a import WATER
from s9b import gear, WOOD
from s11a import SB11, VOL11, SAND

STONE = (170, 160, 140)
BRASS = (190, 150, 80)

# ---------------------------------------------------------------- B36 古埃及搬巨石
def b36_sledge(c, t, i):
    corner_tag(c, 'B36 · 干沙和湿沙')
    c.text(60, 96, '同一架雪橇，干沙上和湿沙上', 'serif', 40, INK)
    for k, (name, wet) in enumerate([('干沙', False), ('湿沙（适量的水）', True)]):
        y = 430 + k * 340
        a = fade(t, 0.5 + k, 1.5 + k)
        c.text(80, y - 150, name, 'bold', 30, mix(BG, INK, a), 'lm')
        col = SAND if not wet else mix(SAND, (120, 100, 70), 0.5)
        c.rect(60, y, 1860, y + 90, fill=mix(BG, col, a))
        prog = fade(t, 2, 18)
        speed = 0.35 if not wet else 1.0
        x = 160 + 1300 * prog * speed
        sink = 22 if not wet else 4
        # berm of sand in front of the dry sledge
        if not wet and prog > 0:
            h = 18 + 30 * min(1, prog * 3)
            c.poly([(x + 200, y + 2), (x + 200, y - h), (x + 290, y + 2)], mix(BG, SAND, a))
        c.poly([(x, y + sink - 30), (x + 210, y + sink - 30), (x + 230, y + sink - 10), (x + 210, y + sink), (x, y + sink)], mix(BG, WOOD, a))
        c.rect(x + 30, y + sink - 170, x + 180, y + sink - 30, fill=mix(BG, STONE, a), r=6)
        c.line([(x + 230, y + sink - 20), (x + 420, y - 60)], mix(BG, MUTED, a), 3)
        f = 2.0 if not wet else 1.0
        c.text(x + 430, y - 70, f'拉力 ≈ {f:.0f} 份', 'mono', 26, mix(BG, NRED if not wet else GREEN, a), 'lm')
        if wet:
            for j in range(4):
                d = (t * 1.2 + j / 4) % 1
                c.ellipse(x + 260 + 30 * j, y - 40 + 50 * d, 5, 8, fill=WATER)
    caps(c, t, [(0, 6, '干沙上，雪橇往下陷，前面还会推起一道沙堆，越拉越费劲'),
                (6.2, 14, '在雪橇前面浇上适量的水，沙子变硬，雪橇不再往下陷'),
                (14.2, 22, '2014 年的实验发现，合适的湿度能让拉力减到大约一半（拍摄前核对）')], y=1010)

def b36_bridge(c, t, i):
    corner_tag(c, 'B36 · 水在沙粒之间搭桥')
    c.text(60, 96, '一点点水，把沙粒「粘」在一起', 'serif', 40, INK)
    # zoom of grains
    cx, cy = 560, 560
    rnd = random.Random(36)
    grains = []
    for r in range(5):
        for q in range(6):
            grains.append((cx - 300 + q * 120 + (r % 2) * 60 + rnd.uniform(-8, 8), cy - 240 + r * 115 + rnd.uniform(-8, 8)))
    wet = fade(t, 3, 8)
    for (x, y) in grains:
        c.ellipse(x, y, 54, 54, fill=SAND)
    if wet > 0:
        for (x1, y1) in grains:
            for (x2, y2) in grains:
                d = math.hypot(x2 - x1, y2 - y1)
                if 0 < d < 135 and x1 < x2 + 0.1:
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    c.ellipse(mx, my, 20 * wet, 14 * wet, fill=mix(BG, WATER, 0.8))
    c.text(cx, 900, '放大：每两粒沙之间有一小座「水桥」' if wet > 0.5 else '放大：干沙粒互相滚来滚去', 'bold', 26, INK, 'mm')
    # force vs water content curve
    gx0, gx1, gy0, gy1 = 1120, 1820, 260, 760
    a = fade(t, 9, 10)
    c.line([(gx0, gy1), (gx1, gy1)], mix(BG, MUTED, a), 2); c.line([(gx0, gy0), (gx0, gy1)], mix(BG, MUTED, a), 2)
    c.text(gx0, gy0 - 30, '拉力', 'sans', 22, mix(BG, MUTED, a), 'lm')
    c.text(gx1, gy1 + 34, '含水量 →', 'sans', 22, mix(BG, MUTED, a), 'rm')
    prog = fade(t, 10, 16)
    pts = []
    for j in range(int(100 * prog) + 1):
        u = j / 100
        F = 1 - 0.5 * math.exp(-((u - 0.35) / 0.15) ** 2) + 0.35 * max(0, u - 0.6) ** 1.5 * 4
        pts.append((gx0 + (gx1 - gx0) * u, gy1 - (gy1 - gy0) * 0.65 * F))
    if len(pts) > 1: seg(c, pts, COPPER, 4)
    b = fade(t, 16, 17)
    xm = gx0 + (gx1 - gx0) * 0.35
    c.line([(xm, gy0), (xm, gy1)], mix(BG, GREEN, b), 2)
    c.text(xm, gy1 + 34, '刚刚好', 'bold', 22, mix(BG, GREEN, b), 'mm')
    c.text(gx1 - 10, gy1 - 40, '太湿：成了泥', 'sans', 22, mix(BG, NRED, b), 'rm')
    caps(c, t, [(0, 8, '干沙粒之间没有东西连着，一压就滑开，雪橇就陷下去'),
                (8.2, 16, '加一点水，水在沙粒之间搭起一座座小桥，把沙粒拉在一起：沙变硬了'),
                (16.2, 22, '水太少不够搭桥，太多又成了泥：中间有个刚刚好的湿度（曲线为示意）')], y=1010)

# ---------------------------------------------------------------- B37 阿拉伯星盘
def b37_project(c, t, i):
    corner_tag(c, 'B37 · 把天空压扁')
    c.text(60, 96, '圆圆的天空，怎么画在一块平板上？', 'serif', 40, INK)
    # side view: sphere and projection plane
    cx, cy, R = 520, 560, 260
    a = fade(t, 0.5, 1.5)
    c.ellipse(cx, cy, R, R, outline=mix(BG, MUTED, a), width=3)
    c.line([(cx - 420, cy), (cx + 420, cy)], mix(BG, BRASS, a), 4)
    c.text(cx + 430, cy, '平板（赤道面）', 'sans', 22, mix(BG, BRASS, a), 'lm')
    sp = (cx, cy + R)
    c.ellipse(sp[0], sp[1], 10, 10, fill=mix(BG, NRED, a))
    c.text(sp[0] + 20, sp[1] + 20, '南极：投影点', 'sans', 22, mix(BG, NRED, a), 'lm')
    n = int(7 * fade(t, 2, 10))
    for k in range(n):
        ang = math.radians(-70 + k * 23)
        px, py = cx + R * math.sin(ang), cy - R * math.cos(ang)
        # line from south pole through the point to the plane y=cy
        tt_ = (cy - sp[1]) / (py - sp[1])
        qx = sp[0] + (px - sp[0]) * tt_
        c.line([sp, (px, py)], mix(BG, SPARK, 0.5), 2)
        c.ellipse(px, py, 8, 8, fill=SPARK)
        c.ellipse(qx, cy, 8, 8, fill=COPPER)
    # plate (top view) with rotating rete
    px0, py0, PR = 1420, 560, 300
    b = fade(t, 10, 11)
    c.ellipse(px0, py0, PR, PR, fill=mix(BG, BRASS, 0.25 * b), outline=mix(BG, BRASS, b), width=5)
    for r in (80, 150, 220):
        c.ellipse(px0, py0 + 40 - r * 0.2, r, r, outline=mix(BG, MUTED, b), width=2)
    rot = fade(t, 13, 21) * 2.4
    c.ellipse(px0 + 60 * math.cos(rot), py0 + 60 * math.sin(rot), 170, 170, outline=mix(BG, SPARK, b), width=4)
    for k in range(8):
        q = rot + k * math.pi / 4
        c.line([(px0, py0), (px0 + 260 * math.cos(q), py0 + 260 * math.sin(q))], mix(BG, BRASS, 0.6 * b), 3)
    c.text(px0, py0 + PR + 40, '底盘：本地的地平线和高度圈；网盘：星星和黄道', 'sans', 22, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 10, '从南极往天球上的每一点画直线，直线穿过赤道面的地方，就是那颗星在平板上的位置'),
                (10.2, 16, '这样投下来，天上的圆在板上还是圆：刻出本地的地平线，再叠一块镂空的星图网盘'),
                (16.2, 22, '转动网盘，就像转动天空：哪颗星在哪个高度，一目了然')], y=1010)

def b37_altitude(c, t, i):
    corner_tag(c, 'B37 · 量太阳高度就知道时间')
    c.text(60, 96, '太阳升得越高，离中午越近', 'serif', 40, INK)
    # sun path curve: altitude vs time of day (example: latitude 35N, equinox)
    gx0, gx1, gy0, gy1 = 160, 1100, 240, 820
    c.line([(gx0, gy1), (gx1, gy1)], MUTED, 2); c.line([(gx0, gy0), (gx0, gy1)], MUTED, 2)
    lat = math.radians(35)
    def alt(h):
        H = math.radians((h - 12) * 15)
        return math.degrees(math.asin(max(-1, min(1, math.cos(lat) * math.cos(H)))))
    pts = [(gx0 + (gx1 - gx0) * (h - 6) / 12, gy1 - (gy1 - gy0) * alt(h) / 60) for h in [6 + j * 0.1 for j in range(121)]]
    seg(c, pts, SPARK, 4)
    for h in range(6, 19, 2):
        x = gx0 + (gx1 - gx0) * (h - 6) / 12
        c.text(x, gy1 + 30, f'{h}:00', 'mono', 20, MUTED, 'mm')
    for v in (0, 20, 40, 55):
        y = gy1 - (gy1 - gy0) * v / 60
        c.text(gx0 - 12, y, f'{v}°', 'mono', 20, MUTED, 'rm')
    c.text(gx0 + 10, gy0 - 20, '太阳高度（北纬 35°、春分前后，示意）', 'sans', 22, MUTED, 'lm')
    a = fade(t, 8, 9)
    if a > 0:
        h0 = 9.4
        y = gy1 - (gy1 - gy0) * alt(h0) / 60
        x = gx0 + (gx1 - gx0) * (h0 - 6) / 12
        c.line([(gx0, y), (x, y)], mix(BG, GREEN, a), 2)
        c.line([(x, y), (x, gy1)], mix(BG, GREEN, a), 2)
        c.text(gx0 + 20, y - 24, f'量得 {alt(h0):.0f}°', 'bold', 24, mix(BG, GREEN, a), 'lm')
        c.text(x + 10, gy1 - 30, '→ 约上午 9:24', 'bold', 24, mix(BG, GREEN, a), 'lm')
    # quadrant with straw
    qx, qy = 1500, 760
    b = fade(t, 2, 3)
    c.arc(qx, qy, 260, 260, 180, 270, mix(BG, BRASS, b), 4)
    c.line([(qx, qy), (qx - 260, qy)], mix(BG, BRASS, b), 4)
    c.line([(qx, qy), (qx, qy - 260)], mix(BG, BRASS, b), 4)
    ang = math.radians(alt(9.4))
    c.line([(qx, qy), (qx - 300 * math.cos(ang), qy - 300 * math.sin(ang))], mix(BG, INK, b), 6)
    c.line([(qx - 300 * math.cos(ang), qy - 300 * math.sin(ang)), (qx - 300 * math.cos(ang), qy - 300 * math.sin(ang) + 200)], mix(BG, MUTED, b), 1)
    c.text(qx - 150, qy + 50, '吸管对准太阳：看吸管落在纸上的小圆光斑', 'sans', 22, mix(BG, INK, b), 'mm')
    c.text(qx - 150, qy + 90, '（绝不直视太阳）', 'bold', 22, mix(BG, NRED, b), 'mm')
    caps(c, t, [(0, 8, '同一个地方、同一天，太阳的高度和时刻一一对应：上午升，中午最高，下午降'),
                (8.2, 15, '量出太阳有多高，在曲线上一查，就知道是几点'),
                (15.2, 22, '星盘把这条曲线刻成了能转的盘：转到量得的高度，指针就指着时间。夜里换成量星星')], y=1010)

# ---------------------------------------------------------------- B38 安提基特拉机械
def b38_ratio(c, t, i):
    corner_tag(c, 'B38 · 用齿数比模拟天体')
    c.text(60, 96, '太阳走一圈，月亮走 13 圈多：用齿轮来算', 'serif', 40, INK)
    turn = fade(t, 2, 20) * 2 * math.pi * 1.0
    # year dial and moon dial
    for k, (name, x, ratio, col) in enumerate([('太阳（一年一圈）', 520, 1.0, SPARK), ('月亮（约 13.37 圈）', 1400, 254 / 19, (200, 200, 220))]):
        c.ellipse(x, 520, 260, 260, outline=BRASS, width=5)
        for m in range(12):
            q = m * math.pi / 6
            c.line([(x + 240 * math.cos(q), 520 + 240 * math.sin(q)), (x + 260 * math.cos(q), 520 + 260 * math.sin(q))], BRASS, 3)
        q = turn * ratio - math.pi / 2
        c.line([(x, 520), (x + 220 * math.cos(q), 520 + 220 * math.sin(q))], col, 8)
        c.ellipse(x + 220 * math.cos(q), 520 + 220 * math.sin(q), 18, 18, fill=col)
        c.text(x, 830, name, 'bold', 28, INK, 'mm')
        laps = turn * ratio / (2 * math.pi)
        c.text(x, 880, f'{laps:.2f} 圈', 'mono', 28, MUTED, 'mm')
    a = fade(t, 12, 13)
    c.rect(560, 180, 1360, 260, fill=mix(BG, SHEET, a), r=10)
    c.text(960, 220, '19 年里月亮绕天 254 圈：齿数比 254 : 19 ≈ 13.37', 'bold', 28, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 8, '太阳在天上一年走一圈，月亮一年要走十三圈多'),
                (8.2, 15, '古希腊人知道：19 年里月亮正好绕天 254 圈'),
                (15.2, 22, '把这个比例做成齿数比，摇一下手柄，日月就各走各的：齿轮成了一台「天文计算器」')], y=1010)

def b38_saros(c, t, i):
    corner_tag(c, 'B38 · 预测日食月食')
    c.text(60, 96, '每过 223 个月，日月食会重演一遍', 'serif', 40, INK)
    cx, cy = 700, 570
    turns = 4
    N = 223
    prog = fade(t, 1, 15)
    pts = []
    for j in range(int(N * prog) + 1):
        u = j / N
        q = u * turns * 2 * math.pi - math.pi / 2
        r = 120 + 230 * u
        pts.append((cx + r * math.cos(q), cy + r * math.sin(q)))
    if len(pts) > 1: seg(c, pts, BRASS, 4)
    rnd = random.Random(38)
    marks = sorted(rnd.sample(range(5, 220), 30))
    for m in marks:
        if m / N > prog: break
        u = m / N
        q = u * turns * 2 * math.pi - math.pi / 2
        r = 120 + 230 * u
        x, y = cx + r * math.cos(q), cy + r * math.sin(q)
        sun = m % 2 == 0
        c.ellipse(x, y, 10, 10, fill=SPARK if sun else (150, 150, 200))
    c.text(cx, 950, '螺旋刻度上 223 格，每格一个月；黄点日食、紫点月食（位置为示意）', 'sans', 22, MUTED, 'mm')
    a = fade(t, 9, 10)
    c.rect(1240, 260, 1860, 640, fill=mix(BG, SHEET, a), r=12)
    for j, (s, kind, col) in enumerate([('1901 年从希腊安提基特拉沉船里', 'sans', INK), ('打捞出的青铜碎块', 'sans', INK),
                                        ('残存三十多个齿轮', 'bold', BRASS), ('年代约公元前 2 世纪', 'sans', INK), ('（有争议，拍摄前核对）', 'sans', MUTED)]):
        c.text(1270, 310 + j * 66, s, kind, 28, mix(BG, col, a), 'lm')
    caps(c, t, [(0, 8, '机器背面有一个螺旋刻度，一共 223 格，每格是一个月'),
                (8.2, 15, '古人发现，日月食大约每 223 个月重演一次：在格子上做好记号，就能预告哪个月有食'),
                (15.2, 22, '这样精巧的齿轮，之后一千多年里再没有出现过')], y=1010)

CLIPS = {
 'B36_雪橇': (b36_sledge, 22), 'B36_水桥': (b36_bridge, 22),
 'B36_片头': (titles.opening(BSER, VOL11, SB11, 6, '世界篇 · 古埃及 · 杰胡提霍特普墓壁画'), 7),
 'B36_片尾': (titles.closing(BSER, VOL11, SB11, 6, '下集：一块铜盘，怎么算出时间？'), 7),
 'B37_投影': (b37_project, 22), 'B37_高度': (b37_altitude, 22),
 'B37_片头': (titles.opening(BSER, VOL11, SB11, 7, '世界篇 · 约 10 世纪 · 伊斯兰世界'), 7),
 'B37_片尾': (titles.closing(BSER, VOL11, SB11, 7, '下集：两千年前的齿轮，算的是什么？'), 7),
 'B38_周期比': (b38_ratio, 22), 'B38_日月食': (b38_saros, 22),
 'B38_片头': (titles.opening(BSER, VOL11, SB11, 8, '世界篇 · 古希腊 · 1901 年出水'), 7),
 'B38_片尾': (titles.closing(BSER, VOL11, SB11, 8, '下集：刀身上的水波纹，是怎么来的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
