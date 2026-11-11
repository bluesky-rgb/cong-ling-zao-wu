"""第三十九季（第十六层：运动场）第二批：E205 弧线球、E206 撑竿跳、E207 动力绳 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L
from s39a import S39A, SER39, VOL39, SKIN, RUBBER, FOAM

AIR = (170, 200, 235)
POLE = (230, 200, 90)
ROPE = (120, 170, 230)


# ---------------------------------------------------------------- E205 弧线球
def e205_spin(c, t, i):
    corner_tag(c, '第 205 集 · 旋转的球，两边空气不一样快')
    c.text(60, 96, '球往右飞、同时逆时针转：上边的空气被带着往后走得快，下边被顶着走得慢，压力不同，球被推向一边', 'serif', 34, INK)
    cx, cy = 760, 560
    R = 140
    c.ellipse(cx, cy, R, R, fill=mix(BG, (240, 240, 240), 0.9))
    a = -t * 3
    for k in range(5):
        aa = a + k * 2 * math.pi / 5
        c.line([(cx, cy), (cx + R * 0.9 * math.cos(aa), cy + R * 0.9 * math.sin(aa))], mix(BG, INK, 0.6), 3)
    c.arc(cx, cy, R + 40, R + 40, 200, 340, SPARK, 5)
    c.text(cx, cy - R - 80, '逆时针转', 'sans', 22, SPARK, 'mm')
    for row in range(-4, 5):
        y = cy + row * 70
        if abs(row) <= 1:
            continue
        sp = 1.0 + (0.8 if row < 0 else -0.5) * (1.6 / abs(row))
        for k in range(8):
            x = 1500 - ((t * 160 * sp + k * 180) % 1300)
            c.line([(x, y), (x - 40 * sp, y)], mix(BG, AIR, 0.8), 3)
    c.text(1640, cy - 250, '快 → 压力小', 'bold', 26, GREEN, 'lm')
    c.text(1640, cy + 250, '慢 → 压力大', 'bold', 26, NRED, 'lm')
    c.arrow(cx + 220, cy + 120, cx + 220, cy - 120, SPARK, 8, 22)
    c.text(cx + 260, cy, '球被推向这边', 'bold', 26, SPARK, 'lm')
    c.text(150, cy, '空气相对球 ←', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '球往前飞，相对来说，空气在往后流'),
                (7.2, 14, '球同时在转：一边顺着气流转，把空气带得更快；另一边逆着，空气被拖慢'),
                (14.2, 22, '快的一边压力小，慢的一边压力大：球被推着拐弯，这叫马格努斯效应（示意）')], y=1010)


def e205_curve(c, t, i):
    corner_tag(c, 'E205 · 任意球绕过人墙')
    c.text(60, 96, '从上往下看：不转的球直直撞上人墙；侧旋的球一路被推向一边，绕过人墙拐进球门', 'serif', 36, INK)
    c.rect(140, 220, 1780, 920, fill=mix(BG, (80, 140, 80), 0.45), r=10)
    gx = 1680
    c.rect(gx, 420, gx + 30, 720, fill=mix(BG, (240, 240, 240), 0.9))
    for k in range(4):
        c.ellipse(900, 640 + k * 45, 22, 22, fill=mix(BG, (200, 80, 80), 0.9))
    c.text(900, 600, '人墙', 'sans', 22, INK, 'mm')
    p = min(1.0, (t % 11) / 8)
    sx, sy = 300, 780
    for j, (curv, col, lab) in enumerate([(0, mix(BG, MUTED, 0.9), '不转：撞上人墙'), (1, SPARK, '侧旋：拐进球门')]):
        pts = []
        for k in range(41):
            u = k / 40 * p
            x = sx + (gx - sx) * u
            y = sy - 210 * u if j == 0 else sy - 700 * u + 490 * u * u
            if j == 0 and x > 876:
                break
            pts.append((x, y))
        if len(pts) > 1:
            c.line(pts, col, 4)
            c.ellipse(pts[-1][0], pts[-1][1], 14, 14, fill=col)
        c.text(320 if j == 0 else 1100, 300 if j == 0 else 860, lab, 'bold', 24, col, 'lm')
    c.ellipse(sx, sy, 14, 14, fill=INK)
    caps(c, t, [(0, 7, '踢球时用脚背的一侧搓球，球一边飞一边绕竖直的轴转'),
                (7.2, 14, '一路上，旋转都在把球往一边推，路线弯成一道弧'),
                (14.2, 22, '转得越快、飞得越快，拐得越厉害：乒乓球的弧圈球也是这样（示意）')], y=1010)


# ---------------------------------------------------------------- E206 撑竿跳
def e206_bend(c, t, i):
    corner_tag(c, '第 206 集 · 竿子弯下去，存住速度')
    c.text(60, 96, '助跑的人把竿头插进地上的穴里：竿子被压成一张弓，人的速度慢下来，力气存进了竿子', 'serif', 36, INK)
    gx, gy = 1000, 860
    c.rect(100, gy, 1820, gy + 30, fill=mix(BG, (150, 120, 90), 0.8))
    c.rect(gx - 30, gy - 10, gx + 10, gy + 30, fill=BG)
    T = 11
    ph = (t % T) / T
    L = 560
    if ph < 0.25:
        hx = 300 + ph / 0.25 * 500
        hy = gy - 140
        c.line([(hx + 20, hy - 10), (hx + 300, hy - 60)], POLE, 8)
        bend = 0
    else:
        u = min(1, (ph - 0.25) / 0.45)
        ang = math.radians(160 - 70 * u)
        bend = math.sin(math.pi * min(1, u * 1.1)) * 0.6 if u < 0.95 else 0
        tipx, tipy = gx, gy
        chord = L * (1 - 0.35 * bend)
        hx = tipx + chord * math.cos(ang)
        hy = tipy - chord * math.sin(ang)
        mx, my = (hx + tipx) / 2, (hy + tipy) / 2
        nx, ny = -(tipy - hy), (tipx - hx)
        nl = math.hypot(nx, ny) or 1
        bx, by = mx + nx / nl * 180 * bend, my + ny / nl * 180 * bend
        pts = []
        for k in range(21):
            s = k / 20
            pts.append(((1 - s) ** 2 * hx + 2 * s * (1 - s) * bx + s * s * tipx, (1 - s) ** 2 * hy + 2 * s * (1 - s) * by + s * s * tipy))
        c.line(pts, POLE, 9)
        if ph > 0.7:
            v = (ph - 0.7) / 0.3
            hx, hy = gx + 40 * v, gy - L + 20 - 80 * math.sin(math.pi * min(1, v * 1.3))
    c.ellipse(hx, hy - 30, 22, 22, fill=SKIN)
    c.line([(hx, hy - 10), (hx, hy + 70)], SKIN, 10)
    c.rect(gx - 120, gy - 520, gx - 110, gy, fill=MUTED)
    c.rect(gx + 110, gy - 520, gx + 120, gy, fill=MUTED)
    c.line([(gx - 115, gy - 500), (gx + 115, gy - 500)], NRED, 5)
    c.rect(1380, 230, 1860, 470, fill=SHEET, r=12)
    stage = '助跑：动能' if ph < 0.25 else ('弯竿：存进弹性势能' if ph < 0.7 else '弹直：变成高度')
    c.text(1620, 300, '能量在哪里', 'bold', 26, INK, 'mm')
    c.text(1620, 380, stage, 'bold', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '运动员抱着竿子全速助跑，身上带着很大的动能'),
                (7.2, 14, '竿头插进地上的穴，竿子被压弯，人慢下来，能量存进了竿子'),
                (14.2, 22, '竿子弹直，把能量还给人，变成往上的高度（示意，不在家里模仿）')], y=1010)


def e206_energy(c, t, i):
    corner_tag(c, 'E206 · 按得越深，弹得越高')
    c.text(60, 96, '桌边压住一把尺子，末端按下 2、4、6 厘米再松手：按得越深，存的能量越多，小橡皮弹得越高', 'serif', 36, INK)
    for j, d in enumerate([2, 4, 6]):
        cx = 360 + j * 580
        base = 760
        c.rect(cx - 250, base, cx - 60, base + 120, fill=mix(BG, (150, 120, 90), 0.8))
        T = 6
        ph = (t + j * 0.3) % T
        if ph < 2:
            dd = d * 14 * min(1, ph / 1.2)
            hy = None
        else:
            dd = 0
            u = (ph - 2) / 2.5
            hmax = 14 * d * d
            hy = base - 20 - (hmax * 4 * u * (1 - u) if u < 1 else 0)
        pts = [(cx - 60 + s * 280, base - 6 + dd * (s ** 2)) for s in [k / 10 for k in range(11)]]
        c.line([(cx - 250, base - 6)] + pts, mix(BG, (90, 160, 220), 1.0), 10)
        ex, ey = pts[-1]
        if hy is None:
            c.rect(ex - 20, ey - 28, ex + 10, ey - 6, fill=mix(BG, (240, 150, 160), 1.0), r=4)
        else:
            c.rect(ex - 20, hy - 22, ex + 10, hy, fill=mix(BG, (240, 150, 160), 1.0), r=4)
        for k in range(6):
            yy = base - 20 - k * 100
            c.line([(cx + 260, yy), (cx + 290, yy)], MUTED, 2)
            c.text(cx + 300, yy, f'{k * 10}', 'mono', 16, MUTED, 'lm')
        c.text(cx + 80, base + 170, f'按下 {d} 厘米', 'bold', 26, INK, 'mm')
        c.text(cx + 80, base + 210, '弹得越高（以实测为准）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '尺子被按弯，就像撑竿被压弯，能量存在弯曲里'),
                (7.2, 14, '按下的深度翻一倍，存的能量差不多变成四倍'),
                (14.2, 22, '玻璃纤维竿能弯得很深又不断，所以比竹竿、铝竿跳得高（示意）')], y=1040)


# ---------------------------------------------------------------- E207 动力绳
def e207_catch(c, t, i):
    corner_tag(c, '第 207 集 · 会伸长的绳子慢慢拉停')
    c.text(60, 96, '同样掉下 1 米：几乎不伸长的绳子一下子拉停，拉力尖得吓人；动力绳伸长一段，慢慢拉停', 'serif', 36, INK)
    for j, (lab, k_, col) in enumerate([('静力绳 / 钢丝：几乎不伸长', 1, NRED), ('动力绳：伸长约 30%', 0, GREEN)]):
        cx = 420 + j * 560
        top = 220
        T = 7
        ph = (t % T) / T
        fall = min(1, ph / 0.4)
        L0 = 300
        stretch = 0 if k_ else 120
        if ph < 0.4:
            y = top + L0 * 0.2 + (L0 * 0.8 + 40) * fall ** 2
        else:
            u = min(1, (ph - 0.4) / 0.3)
            y = top + L0 + 40 + stretch * math.sin(min(math.pi / 2, u * math.pi / 2))
        c.line([(cx - 60, top), (cx + 60, top)], INK, 6)
        c.line([(cx, top), (cx, y - 40)], ROPE if not k_ else mix(BG, (200, 200, 210), 1.0), 5 if not k_ else 3)
        c.ellipse(cx, y, 36, 40, fill=mix(BG, (90, 130, 200), 0.9))
        c.text(cx, 930, lab, 'bold', 22, col, 'mm')
    x0, y0, W, H = 1260, 260, 600, 520
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 40, '时间（示意）', 'sans', 20, MUTED, 'mm')
    c.text(x0 + 20, y0 + 30, '拉力', 'sans', 20, MUTED, 'lm')
    tn = min(1.0, t / 10)
    for col, f in [(NRED, lambda s: 10 * math.exp(-((s - 0.2) / 0.03) ** 2)), (GREEN, lambda s: 3 * math.exp(-((s - 0.35) / 0.12) ** 2))]:
        pts = []
        for k in range(101):
            s = k / 100
            if s > tn:
                break
            pts.append((x0 + 20 + s * (W - 40), y0 + H - 20 - f(s) / 11 * (H - 60)))
        if len(pts) > 1:
            c.line(pts, col, 4)
    caps(c, t, [(0, 7, '攀岩的人掉下来，绳子必须把他拉住'),
                (7.2, 14, '不伸长的绳子在一瞬间把人拉停，拉力尖得能伤到人，也能拉坏挂点'),
                (14.2, 22, '尼龙动力绳会伸长，停下的时间变长，最大拉力就小了（示意）')], y=1010)


def e207_snap(c, t, i):
    corner_tag(c, 'E207 · 加一根橡皮筋，线就不断了')
    c.text(60, 96, '同样细的缝衣线，同样掉下来的小水瓶：直接吊的那根「啪」一下断了；中间接了橡皮筋的，伸长、晃几下，没断', 'serif', 33, INK)
    for j, (lab, rub) in enumerate([('只有细线', False), ('细线 + 橡皮筋', True)]):
        cx = 520 + j * 880
        top = 230
        T = 8
        ph = (t % T) / T
        fall = min(1, ph / 0.35)
        L = 260
        if ph < 0.35:
            y = top + 60 + (L - 60) * fall ** 2
            broken = False
        else:
            u = (ph - 0.35) / 0.65
            if rub:
                y = top + L + 80 * math.exp(-u * 3) * abs(math.cos(u * 10)) + 60
                broken = False
            else:
                y = min(820, top + L + 1200 * u * u)
                broken = True
        c.rect(cx - 140, top - 20, cx + 140, top, fill=mix(BG, (150, 120, 90), 0.9))
        if not broken:
            if rub:
                mid = top + (y - 60 - top) * 0.5
                c.line([(cx, top), (cx, mid - 30)], INK, 2)
                c.line([(cx, mid - 30), (cx, mid + 30)], mix(BG, (210, 160, 90), 1.0), 8)
                c.line([(cx, mid + 30), (cx, y - 60)], INK, 2)
            else:
                c.line([(cx, top), (cx, y - 60)], INK, 2)
        else:
            c.line([(cx, top), (cx + 10, top + 120)], INK, 2)
            c.text(cx + 60, top + 140, '断了！', 'bold', 26, NRED, 'lm')
        c.rect(cx - 40, y - 60, cx + 40, y + 60, fill=mix(BG, WATER_L, 0.5), outline=mix(BG, WATER_L, 1.0), width=3, r=12)
        c.rect(cx - 160, 860, cx + 160, 900, fill=mix(BG, (200, 160, 120), 0.6), r=8)
        c.text(cx, 950, lab, 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '两根一样的缝衣线，各吊一个装水的小塑料瓶，从挂点的高度松手'),
                (7.2, 14, '只有细线的那根，瓶子一绷到底，线就断了'),
                (14.2, 22, '接了橡皮筋的那根，伸长了一段，把冲击拉长，线没断（以实测为准）')], y=1010)


CLIPS = {
 'E205_旋转': (e205_spin, 22), 'E205_拐弯': (e205_curve, 22),
 'E205_片头': (titles.opening(SER39, VOL39, S39A, 3, '19 世纪马格努斯研究旋转物体的偏转'), 7),
 'E205_片尾': (titles.closing(SER39, VOL39, S39A, 3, '下集：撑竿弯成一张弓，里面存着什么？'), 7),
 'E206_弯竿': (e206_bend, 22), 'E206_能量': (e206_energy, 22),
 'E206_片头': (titles.opening(SER39, VOL39, S39A, 4, '20 世纪 50 年代起撑竿换成玻璃纤维'), 7),
 'E206_片尾': (titles.closing(SER39, VOL39, S39A, 4, '下集：登山绳为什么要会伸长？'), 7),
 'E207_拉停': (e207_catch, 22), 'E207_断线': (e207_snap, 22),
 'E207_片头': (titles.opening(SER39, VOL39, S39A, 5, '20 世纪 40 年代起尼龙登山绳取代麻绳'), 7),
 'E207_片尾': (titles.closing(SER39, VOL39, S39A, 5, '下集：紧身泳衣真能游得更快吗？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
