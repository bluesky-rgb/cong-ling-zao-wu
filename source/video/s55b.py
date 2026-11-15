"""第五十五季（第二十四层：游乐场）第二批：E285 摩天轮、E286 过山车、E287 碰碰车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s55a import S55A, SER55, VOL55, KID

STEELC = (170, 175, 185)
CAB = (220, 120, 100)
TRACK = (200, 110, 90)
CAR1 = (90, 150, 220)
CAR2 = (230, 170, 70)
RUBBER = (60, 60, 65)


# ---------------------------------------------------------------- E285 摩天轮
def _wheel(c, cx, cy, R, ang, fixed_idx=None):
    c.ellipse(cx, cy, R, R, outline=mix(BG, STEELC, 1.0), width=8)
    for k in range(8):
        a = ang + k * math.pi / 4
        c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], mix(BG, STEELC, 0.7), 3)
    c.line([(cx, cy), (cx - 160, cy + R + 120)], mix(BG, STEELC, 1.0), 10)
    c.line([(cx, cy), (cx + 160, cy + R + 120)], mix(BG, STEELC, 1.0), 10)
    for k in range(8):
        a = ang + k * math.pi / 4
        px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        c.ellipse(px, py, 7, 7, fill=INK)
        if fixed_idx == k:
            rot = a + math.pi / 2
            pts = [(-30, 10), (30, 10), (30, 70), (-30, 70)]
            P = [(px + x * math.cos(rot) - y * math.sin(rot), py + x * math.sin(rot) + y * math.cos(rot)) for x, y in pts]
            c.poly(P, mix(BG, NRED, 0.9))
        else:
            c.line([(px, py), (px, py + 14)], INK, 3)
            c.rect(px - 30, py + 14, px + 30, py + 70, fill=mix(BG, CAB, 1.0), r=8)


def e285_hang(c, t, i):
    corner_tag(c, '第 285 集 · 吊着的座舱')
    c.text(60, 96, '每个座舱吊在轮边的一根轴上，能自由摆动；重心在吊点下面，不管大轮转到哪里，重力都把座舱拉得竖直向下', 'serif', 36, INK)
    ang = t * 0.25
    _wheel(c, 960, 520, 300, ang)
    c.text(1500, 300, '座舱始终朝下', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '大轮慢慢转，座舱从最低转到最高'),
                (7.2, 14, '每个座舱都吊在一根轴上，重心在吊点下面'),
                (14.2, 22, '重力总把它拉得竖直，里面的人一直坐得正正的（示意）')], y=1010)


def e285_fixed(c, t, i):
    corner_tag(c, '第 285 集 · 焊死了就会翻')
    c.text(60, 96, '把一个座舱焊死在轮上：它会跟着大轮一起转，转到顶上就头朝下；吊着的座舱却一直正着', 'serif', 36, INK)
    ang = t * 0.28
    _wheel(c, 960, 520, 300, ang, fixed_idx=0)
    c.text(1520, 300, '红：焊死的座舱', 'bold', 28, NRED, 'mm')
    c.text(1520, 360, '橙：吊着的座舱', 'bold', 28, mix(BG, CAB, 1.0), 'mm')
    caps(c, t, [(0, 7, '纸板大轮上挂 6 个纸杯，杯里放纽扣；有一个用胶带粘死'),
                (7.2, 14, '慢慢转半圈：挂着的纸杯一直杯口朝上'),
                (14.2, 22, '粘死的那个翻了过来，纽扣掉了出去（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E286 过山车
def _track_pts(h0):
    pts = []
    for k in range(41):
        u = k / 40
        x = 200 + u * 600
        y = 900 - h0 * (1 - u) ** 1.6
        pts.append((x, y))
    cx, cy, R = 1000, 900 - 160, 160
    for k in range(61):
        a = math.pi / 2 + 2 * math.pi * k / 60
        pts.append((cx - R * math.cos(a) * 0 + R * math.sin(-a + math.pi), cy + R * math.cos(-a + math.pi)))
    return pts


def e286_energy(c, t, i):
    corner_tag(c, '第 286 集 · 高度变速度，速度变高度')
    c.text(60, 96, '开头被拉到最高点攒下「高度的能量」，冲下来变成速度，爬坡时又变回高度；路上有摩擦，后面的坡要矮一点', 'serif', 36, INK)
    xs = [200 + k * 20 for k in range(76)]
    def h(x):
        return 640 * math.exp(-((x - 260) / 140) ** 2) + 360 * math.exp(-((x - 1050) / 150) ** 2) + 220 * math.exp(-((x - 1550) / 120) ** 2)
    pts = [(x, 900 - h(x)) for x in xs]
    c.line(pts, mix(BG, TRACK, 1.0), 10)
    K = [(0, 262), (5, 264), (9, 650), (14, 1050), (22, 1660)]
    x = K[-1][1]
    for (t0, x0), (t1, x1) in zip(K, K[1:]):
        if t0 <= t <= t1:
            x = x0 + (x1 - x0) * (t - t0) / (t1 - t0)
            break
    y = 900 - h(x)
    c.ellipse(x, y - 24, 26, 26, fill=mix(BG, CAR1, 1.0))
    H = h(x) / 640
    V = max(0.0, 1 - H)
    c.rect(1700, 900 - 400 * H, 1760, 900, fill=mix(BG, CAR2, 0.9))
    c.rect(1780, 900 - 400 * V, 1840, 900, fill=mix(BG, GREEN, 0.9))
    c.text(1730, 940, '高度', 'sans', 22, INK, 'mm')
    c.text(1810, 940, '速度', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '被拉到最高点：高度最大，速度几乎是零'),
                (7.2, 14, '冲到坡底：高度变成了速度，最快'),
                (14.2, 22, '爬上下一个坡：速度又变回高度，但爬不到起点那么高（示意）')], y=1010)


def e286_loop(c, t, i):
    corner_tag(c, '第 286 集 · 翻回环要从够高的地方出发')
    c.text(60, 96, '弹珠要翻过回环，到顶上时还得有足够的速度；起点太低，到回环顶上就掉下来，起点要比回环顶高出一截', 'serif', 36, INK)
    cx, cy, R = 1200, 640, 170
    c.ellipse(cx, cy, R, R, outline=mix(BG, TRACK, 1.0), width=10)
    c.line([(300, 260), (500, 520), (900, 810), (cx, cy + R)], mix(BG, TRACK, 1.0), 10)
    c.line([(cx, cy + R), (1700, cy + R)], mix(BG, TRACK, 1.0), 10)
    ok = t > 11
    start_y = 260 if ok else 420
    c.ellipse(300 + (start_y - 260) * 0.77, start_y - 20, 18, 18, fill=mix(BG, CAR2, 1.0))
    ph = (t % 11) / 11
    if ph > 0.4:
        a = (ph - 0.4) / 0.6 * 2 * math.pi
        if not ok and a > math.pi * 0.8:
            fall = (a - math.pi * 0.8) * 120
            bx, by = cx + R * math.sin(math.pi * 0.8), cy + R * math.cos(math.pi * 0.8) + fall
        else:
            bx, by = cx + R * math.sin(a), cy + R * math.cos(a)
        c.ellipse(bx, by, 16, 16, fill=mix(BG, CAR1, 1.0))
    c.line([(cx - 260, cy - R), (cx + 260, cy - R)], MUTED, 2)
    c.text(cx + 270, cy - R, '回环顶', 'sans', 22, MUTED, 'lm')
    c.text(960, 940, '起点够高：翻过去了' if ok else '起点太低：到顶上掉下来', 'bold', 30, GREEN if ok else NRED, 'mm')
    caps(c, t, [(0, 7, '泡沫管做的轨道，中间绕一个回环，从不同高度放弹珠'),
                (7.2, 14, '起点只比回环顶高一点：弹珠到顶上速度不够，掉了下来'),
                (14.2, 22, '起点再高一截，弹珠就翻过去了：所以过山车第一个坡最高（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E287 碰碰车
def _car(c, x, y, col, bumper):
    c.rect(x - 90, y - 50, x + 90, y + 50, fill=mix(BG, col, 1.0), r=14)
    if bumper:
        c.rect(x - 104, y - 60, x + 104, y + 60, outline=mix(BG, RUBBER, 1.0), width=14, r=22)
    for dx in (-55, 55):
        c.ellipse(x + dx, y + 52, 18, 18, fill=INK)


def e287_transfer(c, t, i):
    corner_tag(c, '第 287 集 · 冲劲传给被撞的车')
    c.text(60, 96, '一辆车撞上停着的车：撞人的车慢下来甚至停住，被撞的车冲了出去，前一辆的「冲劲」传给了后一辆', 'serif', 36, INK)
    tc = 5.0
    if t < tc:
        x1 = 300 + (900 - 300) * t / tc
        x2 = 1100
    else:
        x1 = 900 + 20 * min(1, (t - tc))
        x2 = 1100 + (t - tc) * 110
    x2 = min(x2, 1760)
    _car(c, x1, 560, CAR1, False)
    _car(c, x2, 560, CAR2, False)
    if abs(t - tc) < 0.5:
        c.text(1000, 440, '砰', 'bold', 40, NRED, 'mm')
    c.text(x1, 680, '撞人的车', 'sans', 24, INK, 'mm')
    c.text(x2, 680, '被撞的车', 'sans', 24, INK, 'mm')
    if t > 14.2:
        c.text(960, 860, '硬币排一排，弹一枚撞过去：最后那枚飞出去，中间的几乎不动', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '一辆车从斜坡滑下，撞向停着的车'),
                (7.2, 14, '撞上以后，撞人的车几乎停了，被撞的车往前冲出去'),
                (14.2, 22, '冲劲从一辆车传到另一辆；尺子槽里的硬币也一样（示意，以实测为准）')], y=1010)


def e287_bumper(c, t, i):
    corner_tag(c, '第 287 集 · 一圈橡胶围边')
    c.text(60, 96, '碰碰车四周围着厚厚的橡胶：撞上时围边先被压扁，把撞击拉长、力变小，再把两辆车弹开，车上的人只觉得被弹了一下', 'serif', 34, INK)
    for j, (lab, bumper) in enumerate([('没有围边：硬碰硬', False), ('橡胶围边：压扁再弹开', True)]):
        y = 400 + j * 300
        ph = (t % 6) / 6
        d = 260 * abs(math.cos(ph * math.pi))
        sq = 0
        if bumper and d < 60:
            sq = (60 - d) * 0.6
        x1 = 960 - 110 - d - (0 if not bumper else 14)
        x2 = 960 + 110 + d + (0 if not bumper else 14)
        _car(c, x1, y, CAR1, bumper)
        _car(c, x2, y, CAR2, bumper)
        if d < 20:
            c.text(960, y - 100, '砰！' if not bumper else '噗', 'bold', 34, NRED if not bumper else GREEN, 'mm')
        c.text(200, y, lab, 'bold', 26, NRED if not bumper else GREEN, 'lm')
    caps(c, t, [(0, 7, '没有围边：两辆硬车一撞，一瞬间就停，冲击又大又急'),
                (7.2, 14, '加上橡胶围边：围边先被压扁，撞击拉长了'),
                (14.2, 22, '冲击变小，围边还把车弹开；坐真碰碰车要系好安全带，别正面撞人')], y=1010)


CLIPS = {
 'E285_吊舱': (e285_hang, 22), 'E285_焊死': (e285_fixed, 22),
 'E285_片头': (titles.opening(SER55, VOL55, S55A, 3, '1893 年芝加哥建成第一座大摩天轮'), 7),
 'E285_片尾': (titles.closing(SER55, VOL55, S55A, 3, '下集：过山车没有发动机，劲从哪来？'), 7),
 'E286_能量': (e286_energy, 22), 'E286_回环': (e286_loop, 22),
 'E286_片头': (titles.opening(SER55, VOL55, S55A, 4, '1884 年科尼岛建成早期过山车'), 7),
 'E286_片尾': (titles.closing(SER55, VOL55, S55A, 4, '下集：碰碰车撞上为什么不疼？'), 7),
 'E287_传递': (e287_transfer, 22), 'E287_围边': (e287_bumper, 22),
 'E287_片头': (titles.opening(SER55, VOL55, S55A, 5, '20 世纪 20 年代出现碰碰车'), 7),
 'E287_片尾': (titles.closing(SER55, VOL55, S55A, 5, '下集：喷泉最高能喷多高？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
