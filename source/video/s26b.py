"""第二十六季（古法解密 10.0：担、桥、风、律）第二批：B103 虹桥、B104 摇橹、B105 相风乌 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import SB26, VOL26, BAMBOO, WOOD, WATER, WATER_L

DARKWOOD = (130, 90, 55)
RIVER = (50, 90, 140)
COPPERC = (200, 130, 80)
WINDC = (150, 200, 230)


# ---------------------------------------------------------------- B103 虹桥
def _arch_nodes(n, x0, x1, base, rise):
    pts = []
    for k in range(n + 1):
        u = k / n
        x = x0 + (x1 - x0) * u
        y = base - rise * math.sin(math.pi * u)
        pts.append((x, y))
    return pts


def b103_weave(c, t, i):
    corner_tag(c, 'B103 · 短木头互相压住，编成一道拱')
    c.text(60, 96, '每根木头都不够长：两套木头交替搭接，一根压在横木上、又被下一根压住，拼出一道跨过整条河的拱', 'serif', 36, INK)
    base = 760
    c.rect(0, base + 20, 1920, 1000, fill=mix(BG, RIVER, 0.5))
    c.rect(80, base - 40, 300, base + 120, fill=mix(BG, (150, 140, 120), 0.8))
    c.rect(1620, base - 40, 1840, base + 120, fill=mix(BG, (150, 140, 120), 0.8))
    A = _arch_nodes(4, 300, 1620, base - 40, 380)
    B = _arch_nodes(5, 300, 1620, base - 40, 380)
    order = []
    for k in range(4):
        order.append(('A', k))
    for k in range(5):
        order.append(('B', k))
    order = [order[j] for j in (0, 4, 1, 5, 2, 6, 3, 7, 8)]
    shown = int(min(len(order), t / 1.6 + 1))
    for j, (sys_, k) in enumerate(order[:shown]):
        P = A if sys_ == 'A' else B
        p, q = P[k], P[k + 1]
        a = fade(t, j * 1.6, j * 1.6 + 0.8)
        off = -14 if sys_ == 'A' else 14
        c.line([(p[0], p[1] + off), (q[0], q[1] + off)], mix(BG, WOOD if sys_ == 'A' else DARKWOOD, a), 18)
    for P, col in ((A, WOOD), (B, DARKWOOD)):
        for (x, y) in P[1:-1]:
            c.ellipse(x, y, 16, 16, fill=mix(BG, (90, 70, 50), 0.9))
    c.rect(1460, 230, 1880, 400, fill=SHEET, r=12)
    c.line([(1490, 280), (1560, 280)], WOOD, 14)
    c.text(1580, 280, '第一套：4 节', 'sans', 22, INK, 'lm')
    c.line([(1490, 340), (1560, 340)], DARKWOOD, 14)
    c.text(1580, 340, '第二套：5 节', 'sans', 22, INK, 'lm')
    caps(c, t, [(0, 7, '北宋汴河水急、船多，不能在河中间立桥墩；可一根木头，又跨不过整条河'),
                (7.2, 14, '工匠用两套短木头：第一套搭成几段折线，第二套错开搭在它的节点上，节点处压一根横木'),
                (14.2, 22, '每一根都压着别的、又被别的压着：不用钉子，短木头就编成了一道长长的拱（结构为示意）')], y=1010)


def b103_load(c, t, i):
    corner_tag(c, 'B103 · 压得越重，咬得越紧')
    c.text(60, 96, '桥上的人和车越重，木头在交叉处互相压得越紧，压力越大摩擦越大，谁也滑不开', 'serif', 38, INK)
    load = 0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi)
    cx, cy = 760, 560
    c.line([(cx - 420, cy + 120), (cx + 60, cy - 60)], WOOD, 26)
    c.line([(cx - 60, cy - 60), (cx + 420, cy + 120)], DARKWOOD, 26)
    c.ellipse(cx, cy - 58, 26, 26, fill=(90, 70, 50))
    c.text(cx - 70, cy - 100, '横木', 'sans', 20, MUTED, 'rm')
    w = 60 + 120 * load
    c.rect(cx - 60, cy - 120 - 30 - w * 0.5, cx + 60, cy - 120 - 30, fill=mix(BG, (170, 170, 180), 0.9), r=8)
    c.text(cx, cy - 150 - w * 0.25, '桥上的重', 'bold', 20, INK, 'mm')
    c.arrow(cx, cy - 145, cx, cy - 90, NRED, 4 + 6 * load, 18)
    for s in (-1, 1):
        L = 60 + 140 * load
        ang = math.atan2(60 + 120, 420 - 60) * (1 if s < 0 else -1)
        x0, y0 = cx + s * 120, cy - 20
        c.arrow(x0, y0, x0 + s * L * math.cos(ang) * 0 + s * L * 0.9, y0 + L * 0.4, SPARK, 4, 14)
    c.rect(1260, 260, 1860, 820, fill=SHEET, r=14)
    c.text(1560, 300, '交叉处（示意）', 'bold', 24, INK, 'mm')
    gx0, gy0 = 1320, 760
    c.line([(gx0, gy0), (1820, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, 360)], LINE, 2)
    c.text(1570, 790, '桥上的重 →', 'sans', 20, MUTED, 'mm')
    c.line([(gx0, gy0), (1800, 400)], mix(BG, SPARK, 0.7), 3)
    c.line([(gx0, gy0), (1800, 480)], mix(BG, GREEN, 0.7), 3)
    mx = gx0 + 480 * load
    c.ellipse(mx, gy0 - (gy0 - 400) * load, 10, 10, fill=SPARK)
    c.ellipse(mx, gy0 - (gy0 - 480) * load, 10, 10, fill=GREEN)
    c.text(1340, 380, '压力', 'sans', 20, SPARK, 'lm')
    c.text(1340, 420, '能抵住的摩擦力', 'sans', 20, GREEN, 'lm')
    caps(c, t, [(0, 7, '桥上的重量压在横木上，横木又把两套木头往下、往外推'),
                (7.2, 14, '交叉的地方，木头和木头压得越来越紧：压得越紧，摩擦力越大'),
                (14.2, 22, '所以重量越大，木头咬得越死；真正怕的是两头的桥台被推开（比例为示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B104 摇橹
def b104_scull(c, t, i):
    corner_tag(c, 'B104 · 斜着拨水，力有一部分朝前')
    c.text(60, 96, '从上往下看：橹板斜着在水里左右摆，像鱼尾一样；往左、往右每一下，都把水往后推', 'serif', 38, INK)
    c.rect(0, 160, 1920, 960, fill=mix(BG, RIVER, 0.35))
    by = 560
    bx = 1200 - (t * 18) % 400 * 0
    c.poly([(bx + 360, by), (bx + 200, by - 90), (bx - 300, by - 90), (bx - 300, by + 90), (bx + 200, by + 90)], mix(BG, WOOD, 0.9))
    c.text(bx + 30, by, '船', 'bold', 30, INK, 'mm')
    c.arrow(bx + 380, by, bx + 520, by, GREEN, 6, 20)
    c.text(bx + 450, by - 40, '前进', 'bold', 22, GREEN, 'mm')
    px, py = bx - 300, by
    sw = math.sin(t * 2.2)
    yt = py + 180 * sw
    xt = px - 420
    c.line([(px, py), (xt, yt)], DARKWOOD, 10)
    vy = math.cos(t * 2.2)
    tilt = 0.5 * (1 if vy > 0 else -1)
    L = 70
    bx0, by0 = xt + L * math.sin(tilt), yt - L * math.cos(tilt) * 0.0 - 30 * math.cos(tilt)
    pa = (xt - 50 * math.cos(tilt), yt - 50 * math.sin(tilt) * (-1))
    pa = (xt - 55, yt + 40 * (1 if vy > 0 else -1))
    pb = (xt + 55, yt - 40 * (1 if vy > 0 else -1))
    c.line([pa, pb], BAMBOO, 16)
    c.text(xt - 110, yt, '橹板', 'sans', 20, INK, 'rm')
    d = 1 if vy > 0 else -1
    c.arrow(xt, yt, xt, yt + 90 * d, mix(BG, INK, 0.7), 3, 12)
    c.text(xt + 20, yt + 110 * d, '摆的方向', 'sans', 18, MUTED, 'lm')
    c.arrow(xt + 20, yt, xt + 150, yt, SPARK, 5, 16)
    c.text(xt + 160, yt - 30, '水给橹的力：有一部分朝前', 'sans', 18, SPARK, 'lm')
    for k in range(10):
        s = (t * 0.7 + k * 0.1) % 1
        x = xt - 60 - s * 400
        y = py + 180 * math.sin((t - s * 1.5) * 2.2)
        c.ellipse(x, y, 6 + 8 * s, 6 + 8 * s, outline=mix(BG, WATER_L, 1 - s), width=2)
    c.text(xt - 260, py + 300, '水被推向后方', 'sans', 20, WATER_L, 'mm')
    caps(c, t, [(0, 7, '桨是一下一下往后划，划完还要抬出水面拿回来；橹却一直泡在水里，左右来回摆'),
                (7.2, 14, '秘诀是橹板始终斜着：往左摆时它朝一边斜，往右摆时翻过来朝另一边斜'),
                (14.2, 22, '斜着的板拨水，水给它的力就有一部分朝前：左一下、右一下都在推船，像鱼甩尾巴（示意）')], y=1010)


def b104_angle(c, t, i):
    corner_tag(c, 'B104 · 斜多少最好？')
    c.text(60, 96, '橹板不斜，左右摆只把水往两边推，船不走；斜得太多，又拨不动水：中间有一个最合适的角度', 'serif', 36, INK)
    th = 75 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi))
    r = math.radians(th)
    thrust = math.sin(2 * r)
    c.rect(140, 240, 900, 860, fill=SHEET, r=14)
    c.text(520, 280, '从上往下看橹板', 'bold', 24, INK, 'mm')
    cx, cy = 520, 560
    c.line([(cx - 300, cy), (cx + 300, cy)], mix(BG, LINE, 0.6), 1)
    c.text(cx + 300, cy - 20, '船前进方向 →', 'sans', 18, MUTED, 'rm')
    dx, dy = 150 * math.cos(r), 150 * math.sin(r)
    c.line([(cx - dx, cy + dy), (cx + dx, cy - dy)], BAMBOO, 16)
    if th > 1:
        c.arc(cx, cy, 90, 90, -th, 0, SPARK, 3)
    c.text(cx + 120, cy - 150, f'斜 {th:.0f}°', 'mono', 30, SPARK, 'lm')
    c.arrow(cx, cy + 220, cx, cy + 160, mix(BG, INK, 0.7), 3, 12)
    c.text(cx + 20, cy + 230, '往这边摆', 'sans', 18, MUTED, 'lm')
    gx0, gx1, gy0, gy1 = 1060, 1800, 820, 320
    c.rect(1000, 240, 1860, 860, fill=SHEET, r=14)
    c.text(1430, 280, '往前推的力（示意）', 'bold', 24, INK, 'mm')
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    pts = [(gx0 + (gx1 - gx0) * a / 90, gy0 - (gy0 - gy1) * math.sin(math.radians(2 * a))) for a in range(0, 91)]
    c.line(pts, SPARK, 3)
    for a in (0, 30, 45, 60, 90):
        c.text(gx0 + (gx1 - gx0) * a / 90, gy0 + 22, f'{a}°', 'mono', 16, MUTED, 'mm')
    c.ellipse(gx0 + (gx1 - gx0) * th / 90, gy0 - (gy0 - gy1) * thrust, 12, 12, fill=SPARK)
    caps(c, t, [(0, 7, '橹板竖得笔直、和船身平行时，左右摆只是把水推向两边，船原地晃'),
                (7.2, 14, '斜一点，水的反推力就有了朝前的一份；越斜，这一份越多'),
                (14.2, 22, '可斜得太多，板几乎是横着划过水面，拨不动多少水：中间某个角度推力最大（曲线为示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B105 相风乌
def _vane_sim(t, k, phis, seed):
    th, w = 2.5, 0.0
    rnd = random.Random(seed)
    dt = 1 / 30
    n = int(t / dt)
    for s in range(n):
        tt = s * dt
        phi = phis[min(len(phis) - 1, int(tt / 7.3))]
        acc = -k * math.sin(th - phi) - 1.6 * w + (rnd.uniform(-1, 1) * 1.5 if abs(k) < 0.5 else 0)
        w += acc * dt
        th += w * dt
    return th, phis[min(len(phis) - 1, int(t / 7.3))]


def _bird(c, x, y, th, head, tail, col):
    ux, uy = math.cos(th), math.sin(th)
    nx, ny = -uy, ux
    hx, hy = x + ux * 90, y + uy * 90
    c.line([(x - ux * 90, y - uy * 90), (hx, hy)], col, 8)
    c.ellipse(hx, hy, 12 * head, 12 * head, fill=col)
    tx, ty = x - ux * 90, y - uy * 90
    c.poly([(tx, ty), (tx - ux * 40 * tail + nx * 30 * tail, ty - uy * 40 * tail + ny * 30 * tail), (tx - ux * 40 * tail - nx * 30 * tail, ty - uy * 40 * tail - ny * 30 * tail)], col)
    c.ellipse(x, y, 7, 7, fill=INK)


def b105_torque(c, t, i):
    corner_tag(c, 'B105 · 尾巴大，头就迎着风')
    c.text(60, 96, '风推鸟身：尾巴面积大、离转轴远，被推的力矩大，尾巴就被推到下风，头自然转向来风', 'serif', 38, INK)
    phis = [math.pi, math.pi * 0.5, math.pi * 1.25]
    th, phi = _vane_sim(t, 6.0, phis, 1)
    cx, cy = 760, 560
    c.ellipse(cx, cy, 260, 260, outline=LINE, width=2)
    for k, nm in enumerate(('东', '南', '西', '北')):
        a = k * math.pi / 2
        c.text(cx + 300 * math.cos(a), cy + 300 * math.sin(a), nm, 'sans', 22, MUTED, 'mm')
    wx, wy = math.cos(phi), math.sin(phi)
    for k in range(-2, 3):
        nx, ny = -wy, wx
        s = (t * 0.8 + k * 0.2) % 1
        sx = cx + wx * (420 - 300 * s) + nx * k * 60
        sy = cy + wy * (420 - 300 * s) + ny * k * 60
        c.arrow(sx, sy, sx - wx * 70, sy - wy * 70, mix(BG, WINDC, 1 - s * 0.6), 3, 12)
    c.text(cx + wx * 460, cy + wy * 460 * 0.8, '风从这边来', 'bold', 20, WINDC, 'mm')
    _bird(c, cx, cy, th, 1.0, 1.8, COPPERC)
    err = abs((th - phi + math.pi) % (2 * math.pi) - math.pi)
    c.rect(1300, 300, 1860, 560, fill=SHEET, r=14)
    c.text(1580, 350, '鸟头和来风的夹角', 'bold', 24, INK, 'mm')
    c.text(1580, 440, f'{math.degrees(err):.0f}°', 'mono', 56, GREEN if err < 0.2 else SPARK, 'mm')
    c.text(1580, 520, '风一变，它就转过去', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '相风乌是一只装在竖杆上、能自由转动的鸟：转轴偏向鸟头一边，尾巴做得又大又宽'),
                (7.2, 14, '风吹过来，推尾巴的力比推头的大，离转轴也更远：尾巴被推到下风'),
                (14.2, 22, '一直推到头尾和风一条线、头迎着来风才停：风向一变，它马上转过去（示意）')], y=1010)


def b105_three(c, t, i):
    corner_tag(c, 'B105 · 三只鸟，谁指得准？')
    c.text(60, 96, '同样的风：尾巴比头大的鸟头迎着风；头尾一样大的乱转；头比尾巴大的，反而把屁股对着风', 'serif', 38, INK)
    phis = [math.pi, math.pi * 0.5, math.pi * 1.25]
    birds = [(6.0, 1.0, 1.8, 'A：尾巴大'), (0.0, 1.0, 1.0, 'B：一样大'), (-6.0, 1.8, 0.6, 'C：头大')]
    for k, (kk, hd, tl, lab) in enumerate(birds):
        cx = 360 + k * 600
        cy = 560
        th, phi = _vane_sim(t, kk, phis, 3 + k)
        c.ellipse(cx, cy, 200, 200, outline=LINE, width=2)
        wx, wy = math.cos(phi), math.sin(phi)
        c.arrow(cx + wx * 260, cy + wy * 260, cx + wx * 200, cy + wy * 200, WINDC, 4, 14)
        _bird(c, cx, cy, th, hd, tl, COPPERC)
        c.text(cx, cy + 320, lab, 'bold', 26, INK, 'mm')
        err = abs((th - phi + math.pi) % (2 * math.pi) - math.pi)
        res = '迎着风' if err < 0.35 else ('背着风' if err > 2.8 else '乱转')
        c.text(cx, cy + 365, res, 'sans', 24, GREEN if res == '迎着风' else NRED, 'mm')
    c.text(960, 220, '蓝箭头：风从这边来', 'sans', 20, WINDC, 'mm')
    caps(c, t, [(0, 7, '用卡纸剪三只鸟，插在吸管上套住竹签：A 尾巴比头大，B 头尾一样大，C 头比尾巴大'),
                (7.2, 14, 'A 每次都把头转向来风；B 两边受的力差不多，晃来晃去停不准'),
                (14.2, 22, 'C 被推到反方向，屁股对着风：要指得准，尾巴一定要大（示意，以实测为准）')], y=1010)


CLIPS = {
 'B103_编木': (b103_weave, 22), 'B103_压紧': (b103_load, 22),
 'B103_片头': (titles.opening(BSER, VOL26, SB26, 3, '北宋《清明上河图》汴河虹桥'), 7),
 'B103_片尾': (titles.closing(BSER, VOL26, SB26, 3, '下集：船尾一支橹左右摇，船为什么一直往前走？'), 7),
 'B104_侧摆': (b104_scull, 22), 'B104_角度': (b104_angle, 22),
 'B104_片头': (titles.opening(BSER, VOL26, SB26, 4, '汉代出现船橹'), 7),
 'B104_片尾': (titles.closing(BSER, VOL26, SB26, 4, '下集：屋顶上的铜鸟，为什么总把头转向来风？'), 7),
 'B105_力矩': (b105_torque, 22), 'B105_三只鸟': (b105_three, 22),
 'B105_片头': (titles.opening(BSER, VOL26, SB26, 5, '东汉张衡相风铜乌'), 7),
 'B105_片尾': (titles.closing(BSER, VOL26, SB26, 5, '下集：两千多年前，各地的一「升」为什么差不多一样多？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
