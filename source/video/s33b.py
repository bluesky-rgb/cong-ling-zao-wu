"""第三十三季（第十三层：跑起来的机器）第二批：E175 差速器、E176 雨刮器、E177 螺旋桨 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L
from s33a import S33A, SER33, VOL33, FLUID, CARC

GEAR = (200, 170, 90)
GLASSC = (150, 190, 220)
AIRC = (150, 200, 240)


# ---------------------------------------------------------------- E175 差速器
def e175_paths(c, t, i):
    corner_tag(c, '第 175 集 · 拐弯时，外轮走的路更长')
    c.text(60, 96, '从上往下看一辆拐弯的车：内侧轮子绕小圈，外侧轮子绕大圈；同样时间里外轮要多走一截，就得转得更快', 'serif', 38, INK)
    cx, cy = 760, 600
    Ri, Ro = 220, 360
    c.arc(cx, cy, Ri, Ri, 180, 360, mix(BG, SPARK, 0.6), 4)
    c.arc(cx, cy, Ro, Ro, 180, 360, mix(BG, GREEN, 0.6), 4)
    c.ellipse(cx, cy, 8, 8, fill=MUTED)
    c.text(cx, cy + 30, '转弯中心', 'sans', 18, MUTED, 'mm')
    a = math.pi + min(math.pi, t / 16 * math.pi)
    xi, yi = cx + Ri * math.cos(a), cy + Ri * math.sin(a)
    xo, yo = cx + Ro * math.cos(a), cy + Ro * math.sin(a)
    c.line([(xi, yi), (xo, yo)], CARC, 40)
    c.ellipse(xi, yi, 20, 20, fill=INK)
    c.ellipse(xo, yo, 20, 20, fill=INK)
    frac = (a - math.pi) / math.pi
    c.rect(1320, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1590, 340, '走过的路（示意）', 'bold', 24, INK, 'mm')
    c.text(1590, 420, f'内轮 {math.pi * 1.0 * frac:.2f} 米', 'mono', 28, SPARK, 'mm')
    c.text(1590, 490, f'外轮 {math.pi * 1.6 * frac:.2f} 米', 'mono', 28, GREEN, 'mm')
    c.text(1590, 570, '外轮要多转约 60%', 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '车拐弯时，两个后轮都绕着同一个中心转，可一个在里圈，一个在外圈'),
                (7.2, 14, '里圈半径 1 米，外圈 1.6 米：转半圈，外轮要多走一大截'),
                (14.2, 22, '要是两个轮子焊在一根轴上转得一样快，总有一个要打滑、磨轮胎（示意）')], y=1010)


def e175_gears(c, t, i):
    corner_tag(c, '第 175 集 · 一组会「让」的齿轮')
    c.text(60, 96, '外壳带着小齿轮推动左右两根半轴：直行时小齿轮不自转，拐弯时它一转，一边快一边慢', 'serif', 36, INK)
    turn = 0 if t < 9 else min(1, (t - 9) / 3)
    base = 1.0
    diff = 0.3 * turn
    wl, wr = base - diff, base + diff
    cy = 560
    cx = 960
    ang_c = t * base * 2
    c.rect(cx - 140, cy - 160, cx + 140, cy + 160, outline=METAL, width=8, r=20)
    c.text(cx, cy - 190, '差速器外壳（发动机带着转）', 'sans', 20, MUTED, 'mm')
    for side, w, x in ((-1, wl, cx - 110), (1, wr, cx + 110)):
        c.ellipse(x, cy, 30, 110, fill=mix(BG, GEAR, 0.8))
        for k in range(6):
            a = t * w * 2 + k * math.pi / 3
            c.line([(x - 26, cy + 100 * math.sin(a)), (x + 26, cy + 100 * math.sin(a))], mix(GEAR, INK, 0.3), 3)
        c.rect(x + side * 30 - (0 if side > 0 else 500), cy - 14, x + side * 30 + (500 if side > 0 else 0), cy + 14, fill=METAL)
    sp = (wr - wl) * 4
    for sy in (cy - 110, cy + 110):
        c.ellipse(cx, sy, 60, 26, fill=SPARK)
        for k in range(5):
            a = t * sp + k * 2 * math.pi / 5
            c.line([(cx + 56 * math.cos(a), sy - 4), (cx + 56 * math.cos(a), sy + 4)], INK, 3)
    c.text(cx, cy + 210, '小齿轮自转' if turn > 0.05 else '小齿轮不自转', 'bold', 24, SPARK if turn > 0.05 else MUTED, 'mm')
    for x, w, lab in ((240, wl, '左轮'), (1680, wr, '右轮')):
        c.ellipse(x, cy, 90, 90, fill=(40, 40, 46))
        a = t * w * 2
        c.line([(x, cy), (x + 80 * math.cos(a), cy + 80 * math.sin(a))], METAL, 6)
        c.text(x, cy + 130, f'{lab} {w:.1f} 倍', 'mono', 24, INK, 'mm')
    c.text(960, 860, '直行' if turn < 0.05 else '向左拐弯', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '直行时，外壳、两个小齿轮、两根半轴像一个整体一起转，两轮一样快'),
                (7.2, 14, '一拐弯，内轮受到的阻力大、慢下来，小齿轮就开始自己转'),
                (14.2, 22, '内轮慢多少，外轮就快多少：两个轮子都有劲，又谁都不打滑（示意）')], y=1010)


# ---------------------------------------------------------------- E176 雨刮器
def fourbar(theta, d=15, a=4, b=14, cc=10):
    Bx, By = a * math.cos(theta), a * math.sin(theta)
    Dx, Dy = d, 0
    dx, dy = Dx - Bx, Dy - By
    L = math.hypot(dx, dy)
    x = (b * b - cc * cc + L * L) / (2 * L)
    h = math.sqrt(max(0, b * b - x * x))
    Cx = Bx + x * dx / L - h * dy / L
    Cy = By + x * dy / L - h * dx / L * -1
    c1 = (Bx + x * dx / L + h * dy / L, By + x * dy / L - h * dx / L)
    c2 = (Bx + x * dx / L - h * dy / L, By + x * dy / L + h * dx / L)
    return (Bx, By), (c1 if c1[1] > c2[1] else c2)


def _rocker_range(a, n=180):
    angs = []
    for k in range(n):
        _, (Cx, Cy) = fourbar(2 * math.pi * k / n, a=a)
        angs.append(math.degrees(math.atan2(Cy - 0, Cx - 15)))
    return min(angs), max(angs)


def e176_linkage(c, t, i, a=4, scale=40, ox=560, oy=700, label=True):
    th = t * 1.6
    (Bx, By), (Cx, Cy) = fourbar(th, a=a)
    P = lambda x, y: (ox + x * scale, oy - y * scale)
    A, B, C, D = P(0, 0), P(Bx, By), P(Cx, Cy), P(15, 0)
    c.line([A, D], MUTED, 8)
    c.line([A, B], SPARK, 12)
    c.line([B, C], METAL, 10)
    c.line([D, C], GREEN, 12)
    ang = math.atan2(C[1] - D[1], C[0] - D[0])
    wiper_end = (D[0] + 13 * scale * math.cos(ang), D[1] + 13 * scale * math.sin(ang))
    c.line([C, wiper_end], mix(INK, BG, 0.3), 6)
    for p in (A, B, C, D):
        c.ellipse(p[0], p[1], 10, 10, fill=INK)
    if label:
        c.text(A[0], A[1] + 40, '电动机（一直转）', 'sans', 20, SPARK, 'mm')
        c.text(D[0], D[1] + 40, '刮杆转轴', 'sans', 20, GREEN, 'mm')
    return A, D


def e176_four(c, t, i):
    corner_tag(c, '第 176 集 · 转一圈，摆一个来回')
    c.text(60, 96, '电动机只带着一根短曲柄转圈，一根连杆把它连到刮杆上：曲柄转一整圈，刮杆就来回摆一次', 'serif', 38, INK)
    c.poly([(560, 240), (1440, 240), (1540, 860), (460, 860)], mix(BG, GLASSC, 0.15))
    e176_linkage(c, t, i, ox=640, oy=740)
    lo, hi = _rocker_range(4)
    c.rect(1500, 300, 1860, 500, fill=SHEET, r=14)
    c.text(1680, 350, '刮杆摆动', 'bold', 24, INK, 'mm')
    c.text(1680, 420, f'约 {hi - lo:.0f}°', 'mono', 34, GREEN, 'mm')
    c.text(1680, 470, '（纸板模型，示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '雨刮器的电动机从头到尾只朝一个方向转'),
                (7.2, 14, '电动机轴上的短曲柄转圈，连杆一推一拉，带着刮杆的转轴来回摆'),
                (14.2, 22, '短杆转整圈，长杆来回摆：这叫曲柄摇杆机构，缝纫机踏板、汽车雨刮都在用（示意）')], y=1010)


def e176_compare(c, t, i):
    corner_tag(c, '第 176 集 · 曲柄长一点，刮得更宽')
    c.text(60, 96, '把短曲柄从 4 厘米换成 6 厘米，其他杆不变：曲柄转一圈，刮杆摆过的角度明显变大', 'serif', 38, INK)
    for k, a in enumerate((4, 6)):
        ox = 200 + k * 860
        e176_linkage(c, t, i, a=a, scale=26, ox=ox, oy=780, label=False)
        lo, hi = _rocker_range(a)
        c.text(ox + 200, 860, f'曲柄 {a} 厘米：摆约 {hi - lo:.0f}°', 'bold', 26, INK, 'mm')
    c.text(960, 930, '杆长：底座 15、连杆 14、摇杆 10 厘米（示意，以纸板实测为准）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '左边曲柄 4 厘米，右边 6 厘米，其他三根杆一样长'),
                (7.2, 14, '曲柄越长，连杆推拉的幅度越大，刮杆摆得越开'),
                (14.2, 22, '汽车设计时，就是靠调几根杆的长短，让雨刮刚好扫满整块玻璃（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E177 螺旋桨
def e177_cart(c, t, i):
    corner_tag(c, '第 177 集 · 把空气往后推，车就往前跑')
    c.text(60, 96, '小风扇绑在玩具车上：风往后吹，车往前走；把风扇转过来往前吹，车就往后退', 'serif', 38, INK)
    rev = t > 11
    tt = t if not rev else t - 11
    v = 50 * min(1, tt / 2)
    x = 760 + (v * tt * 0.9 if not rev else -v * tt * 0.9)
    gy = 780
    c.line([(100, gy), (1820, gy)], LINE, 3)
    c.rect(x - 120, gy - 90, x + 120, gy - 30, fill=CARC, r=10)
    c.ellipse(x - 80, gy - 20, 20, 20, fill=INK)
    c.ellipse(x + 80, gy - 20, 20, 20, fill=INK)
    fx = x - 90 if not rev else x + 90
    c.rect(fx - 20, gy - 230, fx + 20, gy - 90, fill=METAL, r=6)
    c.ellipse(fx, gy - 230, 60, 60, outline=METAL, width=4)
    for k in range(3):
        a = t * 20 + k * 2 * math.pi / 3
        c.line([(fx, gy - 230), (fx + 50 * math.cos(a), gy - 230 + 50 * math.sin(a))], METAL, 6)
    d = -1 if not rev else 1
    for k in range(6):
        u = ((t * 1.2) + k / 6) % 1
        ax = fx + d * (70 + u * 400)
        c.ellipse(ax, gy - 230 + (k - 2.5) * 18, 6, 6, fill=AIRC)
    c.arrow(x, gy - 300, x - d * 200, gy - 300, GREEN, 8, 22)
    c.text(x - d * 100, gy - 340, '车被推着走', 'bold', 24, GREEN, 'mm')
    c.text(fx + d * 300, gy - 330, '空气被推出去', 'bold', 22, AIRC, 'mm')
    caps(c, t, [(0, 7, '手持小风扇绑在玩具车上，风朝后吹，一开机，车慢慢往前跑'),
                (7.2, 14, '风扇把空气往后推，空气就把风扇和车往前推：一推一反推'),
                (14.2, 22, '风扇转过来往前吹，车就往后退：船尾的螺旋桨在水里干的是同一件事（示意）')], y=1010)


def e177_blade(c, t, i):
    corner_tag(c, '第 177 集 · 桨叶是一圈斜着的「小翅膀」')
    c.text(60, 96, '把螺旋桨的一片桨叶切开看：它斜着在水里划过，像一把转圈的斜铲子，把前面的水铲到后面去', 'serif', 38, INK)
    cx, cy = 560, 560
    rot = t * 2.5
    c.text(cx, cy + 290, '从船尾看过去（三片桨叶）', 'sans', 20, MUTED, 'mm')
    for k in range(3):
        a = rot + k * 2 * math.pi / 3
        tx, ty = cx + 230 * math.cos(a), cy + 230 * math.sin(a)
        nx, ny = -math.sin(a), math.cos(a)
        c.poly([(cx + 20 * nx, cy + 20 * ny), (tx + 55 * nx, ty + 55 * ny), (tx - 20 * nx, ty - 20 * ny), (cx - 20 * nx, cy - 20 * ny)], mix(GEAR, METAL, 0.3))
    c.ellipse(cx, cy, 30, 30, fill=INK)
    bx, by = 1300, 560
    for k in range(5):
        off = ((t * 120) + k * 140) % 700 - 350
        y = by + off
        if -260 < off < 260:
            c.line([(bx - 140, y - 100), (bx + 140, y + 100)], GEAR, 14)
    for k in range(8):
        u = ((t * 0.8) + k / 8) % 1
        c.ellipse(bx - 360 + u * 720, by - 260 + (k % 4) * 170, 7, 7, fill=FLUID)
    c.arrow(bx + 380, by, bx + 500, by, FLUID, 5, 16)
    c.text(bx + 440, by - 40, '水被推向后', 'bold', 20, FLUID, 'mm')
    c.text(bx, 900, '把一片桨叶「展平」看：斜着往下扫，把水推到后面（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '螺旋桨有几片扭着的桨叶，装在船尾的传动轴上'),
                (7.2, 14, '桨叶斜着转过水，每一圈都把前面的一团水推到后面去'),
                (14.2, 22, '水被推向后，船就被推向前：桨叶扭的角度叫「螺距」，转一圈理论上前进多远就看它（示意）')], y=1010)


CLIPS = {
 'E175_轨迹': (e175_paths, 22), 'E175_齿轮': (e175_gears, 22),
 'E175_片头': (titles.opening(SER33, VOL33, S33A, 3, '1827 年佩克尔发明现代差速器'), 7),
 'E175_片尾': (titles.closing(SER33, VOL33, S33A, 3, '下集：雨刮器的电动机一直往一边转，刮杆怎么来回摆？'), 7),
 'E176_四杆': (e176_four, 22), 'E176_换曲柄': (e176_compare, 22),
 'E176_片头': (titles.opening(SER33, VOL33, S33A, 4, '1903 年玛丽·安德森发明雨刮器'), 7),
 'E176_片尾': (titles.closing(SER33, VOL33, S33A, 4, '下集：螺旋桨在水里转，船为什么就往前走？'), 7),
 'E177_反推': (e177_cart, 22), 'E177_桨叶': (e177_blade, 22),
 'E177_片头': (titles.opening(SER33, VOL33, S33A, 5, '1830 年代船用螺旋桨出现'), 7),
 'E177_片尾': (titles.closing(SER33, VOL33, S33A, 5, '下集：潜水艇没有翅膀，为什么想沉就沉、想浮就浮？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
