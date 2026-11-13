"""第四十三季（第十八层：工具箱）第一批：E222 卷尺、E223 弹簧秤、E224 扳手 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S43A = [('222', '卷尺'), ('223', '弹簧秤'), ('224', '扳手'), ('225', '棘轮'), ('226', '老虎钳'),
        ('227', '千斤顶'), ('228', '磁性螺丝刀'), ('229', '万用表'), ('230', '砂纸'), ('231', '吸盘')]
SER43, VOL43 = '从零造物', '第四十三季 · 第十八层：工具箱'
STEEL = (185, 190, 200)
TAPE = (240, 200, 60)
CASE = (210, 70, 60)
SPRING = (150, 160, 175)
BOLT = (160, 165, 175)


# ---------------------------------------------------------------- E222 卷尺
def e222_section(c, t, i):
    corner_tag(c, '第 222 集 · 弯成浅槽，就不塌')
    c.text(60, 96, '卷尺的尺带不是平的，横着看是一道浅浅的弧：平片一伸就往下垂，弯成槽形的片子要往下折，得先把弧压平，难得多', 'serif', 33, INK)
    p = min(1.0, t / 12)
    for j, (lab, curved) in enumerate([('平的薄片：伸出一点就垂下', False), ('弯成浅槽：伸出很长才塌', True)]):
        y = 290 + j * 400
        x0 = 200
        c.rect(x0 - 120, y - 20, x0, y + 60, fill=mix(BG, CASE, 1.0), r=10)
        L = 1300 * p
        sag_k = 0.0009 if not curved else 0.00006
        pts = [(x0 + s, y + min(260, sag_k * s * s)) for s in range(0, int(L) + 1, 20)]
        if not curved:
            pts = [q for q in pts if q[1] < y + 259]
        if curved and L > 1100:
            k = int((1100) / 20)
            pts = pts[:k] + [(pts[k - 1][0] + (m + 1) * 14, pts[k - 1][1] + min(170, (m + 1) ** 2 * 3)) for m in range(12)]
        if len(pts) > 1:
            c.line(pts, mix(BG, TAPE, 1.0), 14)
        cx, cy = 1600, y + 10
        if curved:
            c.arc(cx, cy + 60, 120, 60, 200, 340, TAPE, 10)
        else:
            c.line([(cx - 110, cy), (cx + 110, cy)], TAPE, 10)
        c.text(cx, cy + 80, '横截面', 'sans', 20, MUTED, 'mm')
        c.text(x0 - 120, y - 60, lab, 'bold', 26, GREEN if curved else NRED, 'lm')
    caps(c, t, [(0, 7, '同样一条薄钢片，平着伸出去，没多远就弯下来了'),
                (7.2, 14, '弯成浅槽，要往下折就得先把弧压平：形状让它硬了很多倍'),
                (14.2, 22, '伸得太长，槽口终于被压平，尺带就「啪」地折下来（示意）')], y=1010)


def e222_spring(c, t, i):
    corner_tag(c, '第 222 集 · 盒子里的发条')
    c.text(60, 96, '尺盒里有一圈卷紧的薄钢带（发条）连着尺带：拉出时发条卷紧、存住能量；松手时发条把尺子卷回去', 'serif', 35, INK)
    cx, cy = 560, 560
    T = 10
    ph = (t % T) / T
    out = ph / 0.6 if ph < 0.6 else 1 - (ph - 0.6) / 0.4
    c.ellipse(cx, cy, 300, 300, fill=mix(BG, CASE, 0.9))
    turns = 4 + 3 * out
    pts = []
    for k in range(400):
        u = k / 399
        a = u * turns * 2 * math.pi
        r = 40 + 200 * (1 - u) * (0.7 + 0.3 * (1 - out))
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    c.line(pts, mix(BG, SPRING, 1.0), 5)
    L = 640 * out
    c.line([(cx + 290, cy + 260), (cx + 290 + L, cy + 260)], TAPE, 16)
    c.rect(cx + 280 + L, cy + 230, cx + 300 + L, cy + 290, fill=INK)
    bx = 1700
    c.rect(bx, 300, bx + 60, 800, fill=SHEET, r=8)
    h = 480 * out
    c.rect(bx, 800 - h, bx + 60, 800, fill=SPARK, r=8)
    c.text(bx + 30, 840, '发条里存的能量（示意）', 'sans', 22, MUTED, 'mm')
    c.text(cx, cy - 340, '拉出：发条卷紧' if ph < 0.6 else '松手：发条把尺子卷回', 'bold', 28, SPARK if ph < 0.6 else GREEN, 'mm')
    caps(c, t, [(0, 7, '尺盒中间是一根卷成蚊香一样的薄钢带，外头连着尺带'),
                (7.2, 14, '尺子越拉越长，发条被卷得越来越紧，回拉的力也越来越大'),
                (14.2, 22, '一松手，发条松开，把尺子卷回去：回卷时手放在尺盒后面')], y=1010)


# ---------------------------------------------------------------- E223 弹簧秤
def e223_linear(c, t, i):
    corner_tag(c, '第 223 集 · 挂两倍重，伸长两倍')
    c.text(60, 96, '弹簧伸长的长度和拉力成正比：挂 1 袋伸长 2 厘米，挂 2 袋就伸长 4 厘米……所以弹簧秤的刻度是均匀的', 'serif', 35, INK)
    n = min(5, int(t / 3.5))
    top = 230
    sx = 400
    ext = 50 * n
    L = 200 + ext
    coils = 14
    pts = []
    for k in range(coils * 20 + 1):
        u = k / (coils * 20)
        pts.append((sx + 30 * math.sin(u * coils * 2 * math.pi), top + u * L))
    c.line([(sx, top - 30), (sx, top)], INK, 4)
    c.line(pts, SPRING, 5)
    c.line([(sx, top + L), (sx, top + L + 30)], INK, 4)
    for m in range(n):
        c.rect(sx - 50, top + L + 30 + m * 40, sx + 50, top + L + 66 + m * 40, fill=mix(BG, (200, 170, 90), 1.0), r=6)
    c.rect(sx + 80, top + 180, sx + 110, top + 480, fill=SHEET)
    for k in range(6):
        y = top + 200 + k * 50
        c.line([(sx + 80, y), (sx + 110, y)], INK, 2)
        c.text(sx + 120, y, f'{k}', 'mono', 18, MUTED, 'lm')
    x0, y0, W, H = 900, 260, 860, 560
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    for k in range(6):
        c.text(x0 + 60 + k * 150, y0 + H + 30, f'{k} 袋', 'sans', 18, MUTED, 'mm')
    pts = [(x0 + 60 + k * 150, y0 + H - 40 - k * 90) for k in range(n + 1)]
    if len(pts) > 1:
        c.line(pts, GREEN, 5)
    for p in pts:
        c.ellipse(p[0], p[1], 9, 9, fill=GREEN)
    c.text(x0 + 20, y0 + 30, '伸长（厘米，示意）', 'sans', 20, MUTED, 'lm')
    caps(c, t, [(0, 7, '一袋一袋往弹簧下面挂，每挂一袋就量一次下端的位置'),
                (7.2, 14, '每多一袋，弹簧就多伸长差不多一样的一段：画出来是一条直线'),
                (14.2, 22, '伸长和拉力成正比，叫胡克定律：刻度就可以画成均匀的格子（以实测为准）')], y=1010)


def e223_limit(c, t, i):
    corner_tag(c, '第 223 集 · 拉过头就回不去')
    c.text(60, 96, '正比只在一定范围里成立：拉得太狠，弹簧的钢丝被拉变了形，松手后回不到原来的长度，这把秤就不准了', 'serif', 35, INK)
    x0, y0, W, H = 220, 240, 1000, 600
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    p = min(1.0, t / 14)
    pts = []
    for k in range(101):
        f = k / 100
        if f > p:
            break
        e = f if f < 0.6 else 0.6 + (f - 0.6) * 2.6
        pts.append((x0 + 60 + f * (W - 120), y0 + H - 50 - min(1.6, e) * 300))
    if len(pts) > 1:
        c.line(pts, SPARK, 5)
    lx = x0 + 60 + 0.6 * (W - 120)
    c.line([(lx, y0 + 40), (lx, y0 + H - 40)], mix(BG, NRED, 0.6), 2)
    c.text(lx + 10, y0 + 60, '弹性限度', 'bold', 22, NRED, 'lm')
    c.text(x0 + 60, y0 + H + 30, '拉力 →', 'sans', 20, MUTED, 'lm')
    c.text(x0 + 30, y0 + 30, '伸长', 'sans', 20, MUTED, 'lm')
    c.text(x0 + 120, y0 + 200, '直线：成正比，松手能回去', 'sans', 22, GREEN, 'lm')
    c.text(lx + 30, y0 + 140, '拐弯：变形了，回不去', 'sans', 22, NRED, 'lm')
    bx = 1450
    for j, (lab, back) in enumerate([('轻拉后松手', 0), ('拉过头后松手', 1)]):
        y = 300 + j * 280
        coils = 10
        L = 160 + 60 * back
        gap = 1 + 2.2 * back
        pts = [(bx + k * 0 + 24 * math.sin(k / 200 * coils * 2 * math.pi), y + k / 200 * L) for k in range(201)]
        c.line(pts, SPRING, 4)
        c.text(bx + 120, y + 80, lab, 'bold', 22, NRED if back else GREEN, 'lm')
    caps(c, t, [(0, 7, '在弹性限度以内，伸长和拉力是一条直线：松手，弹簧回到原长'),
                (7.2, 14, '超过限度，钢丝本身被拉得变了形，曲线开始拐弯'),
                (14.2, 22, '松手后弹簧比原来长了一截：所以秤上都写着最大量程，不要拉过头（示意）')], y=1010)


# ---------------------------------------------------------------- E224 扳手
def e224_torque(c, t, i):
    corner_tag(c, '第 224 集 · 力 × 力臂')
    c.text(60, 96, '拧螺母要的是「转动的效果」：力乘以手到螺母中心的距离。同样的转动效果，手柄长一倍，力只要一半', 'serif', 35, INK)
    cx, cy = 420, 560
    c.poly([(cx + 70 * math.cos(math.radians(60 * k + 30)), cy + 70 * math.sin(math.radians(60 * k + 30))) for k in range(6)], mix(BG, BOLT, 1.0))
    c.ellipse(cx, cy, 26, 26, fill=BG)
    ph = int(t / 7) % 3
    Ls = [300, 600, 900]
    L = Ls[ph]
    ang = math.radians(-6 * math.sin(t * 1.5))
    ex, ey = cx + (L + 100) * math.cos(ang), cy + (L + 100) * math.sin(ang)
    c.line([(cx + 70, cy), (ex, ey)], mix(BG, STEEL, 1.0), 40)
    hx, hy = cx + L * math.cos(ang), cy + L * math.sin(ang)
    F = 900 / L
    c.arrow(hx, hy - 40 - 60 * F, hx, hy - 30, SPARK, 8, 22)
    c.text(hx, hy - 70 - 60 * F, f'力 {F:.1f} 份', 'bold', 26, SPARK, 'mm')
    c.line([(cx, cy + 90), (hx, cy + 90)], MUTED, 2)
    c.text((cx + hx) / 2, cy + 120, f'力臂 {L // 300} 份', 'sans', 24, MUTED, 'mm')
    c.text(1400, 860, f'力 × 力臂 = {F * L / 300:.0f} 份：转动效果一样', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '手握在离螺母 1 份远的地方，要用 3 份力才拧得动'),
                (7.2, 14, '握到 2 份远，只要 1.5 份力；握到 3 份远，只要 1 份力'),
                (14.2, 22, '力乘力臂，叫力矩：拧不动时，换长扳手或者握在手柄末端（以实测为准）')], y=1010)


def e224_angle(c, t, i):
    corner_tag(c, '第 224 集 · 垂直着推最省力')
    c.text(60, 96, '同样握在手柄末端：垂直于手柄推，整根手柄都算力臂；斜着推，真正起作用的距离变短，就得更用劲', 'serif', 36, INK)
    for j, (lab, deg) in enumerate([('垂直推：有效力臂最长', 90), ('斜着 45° 推：有效力臂变短', 45)]):
        ox = 160 + j * 880
        cx, cy = ox + 120, 520
        c.poly([(cx + 50 * math.cos(math.radians(60 * k + 30)), cy + 50 * math.sin(math.radians(60 * k + 30))) for k in range(6)], mix(BG, BOLT, 1.0))
        L = 560
        c.line([(cx + 50, cy), (cx + L + 60, cy)], STEEL, 30)
        hx = cx + L
        a = math.radians(deg)
        ln = 160
        c.arrow(hx - ln * math.cos(a), cy - ln * math.sin(a) - 20, hx, cy - 20, SPARK, 7, 20)
        d = L * math.sin(a)
        if deg != 90:
            px = hx - L * math.cos(a) * math.cos(a)
            py = cy - L * math.cos(a) * math.sin(a)
            c.line([(hx, cy - 20), (px, py)], mix(BG, MUTED, 0.5), 2)
            c.line([(cx, cy), (px, py)], mix(BG, GREEN, 0.9), 4)
            c.text((cx + px) / 2 - 30, (cy + py) / 2 - 20, '有效力臂', 'sans', 20, GREEN, 'rm')
        else:
            c.line([(cx, cy + 60), (hx, cy + 60)], mix(BG, GREEN, 0.9), 3)
            c.text((cx + hx) / 2, cy + 90, '有效力臂', 'sans', 20, GREEN, 'mm')
        c.text(ox + 380, 800, lab, 'bold', 26, GREEN if deg == 90 else NRED, 'mm')
        c.text(ox + 380, 850, f'需要的力：约 {1 / math.sin(a):.1f} 份（示意）', 'mono', 22, INK, 'mm')
    caps(c, t, [(0, 7, '垂直于手柄推，螺母中心到手的整段距离都算力臂'),
                (7.2, 14, '斜着推，力有一部分顺着手柄白白推了出去，有效力臂只剩一截'),
                (14.2, 22, '斜 45° 推，大约要多用四成的力：拧螺母时尽量垂直着推（以实测为准）')], y=1010)


CLIPS = {
 'E222_截面': (e222_section, 22), 'E222_发条': (e222_spring, 22),
 'E222_片头': (titles.opening(SER43, VOL43, S43A, 0, '19 世纪后半叶出现可自动回卷的钢卷尺'), 7),
 'E222_片尾': (titles.closing(SER43, VOL43, S43A, 0, '下集：弹簧秤的刻度为什么是均匀的？'), 7),
 'E223_正比': (e223_linear, 22), 'E223_限度': (e223_limit, 22),
 'E223_片头': (titles.opening(SER43, VOL43, S43A, 1, '18 世纪英国已制造弹簧秤'), 7),
 'E223_片尾': (titles.closing(SER43, VOL43, S43A, 1, '下集：扳手为什么越长越省力？'), 7),
 'E224_力矩': (e224_torque, 22), 'E224_方向': (e224_angle, 22),
 'E224_片头': (titles.opening(SER43, VOL43, S43A, 2, '19 世纪初出现可调扳手'), 7),
 'E224_片尾': (titles.closing(SER43, VOL43, S43A, 2, '下集：棘轮扳手为什么只往一个方向使劲？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
