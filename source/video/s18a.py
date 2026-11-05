"""第十八季（古法解密 6.0：量、影、声、糖）第一批：B60 七巧板、B61 墨斗、B62 勾股 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB18 = [('B60', '七巧板'), ('B61', '墨斗'), ('B62', '勾股'), ('B63', '日晷'), ('B64', '皮影戏'),
        ('B65', '古琴'), ('B66', '回音壁'), ('B67', '屋檐举折'), ('B68', '饴糖'), ('B69', '冰糖')]
VOL18 = '第十八季 · 古法解密 6.0'
WOOD = (175, 125, 75)
INKB = (40, 40, 45)
ROPE = (200, 180, 130)

# ---------------------------------------------------------------- B60 七巧板
# 4×4 正方形里的七块（单位：格），面积以「小三角形」计
TANGRAM = [
    ('大三角', [(0, 0), (4, 0), (2, 2)], 4, (220, 90, 80)),
    ('大三角', [(0, 0), (2, 2), (0, 4)], 4, (240, 170, 70)),
    ('中三角', [(4, 2), (4, 4), (2, 4)], 2, (90, 170, 110)),
    ('正方形', [(2, 2), (3, 1), (4, 2), (3, 3)], 2, (80, 150, 210)),
    ('小三角', [(3, 1), (4, 0), (4, 2)], 1, (170, 110, 200)),
    ('小三角', [(2, 2), (3, 3), (1, 3)], 1, (230, 120, 170)),
    ('平行四边形', [(0, 4), (1, 3), (3, 3), (2, 4)], 2, (120, 200, 200)),
]

def cen(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))

def draw_piece(c, pts, ox, oy, s, col, a=1.0, dx=0, dy=0):
    P = [(ox + (x + dx) * s, oy + (y + dy) * s) for x, y in pts]
    c.poly(P, mix(BG, col, a))
    c.line(P + [P[0]], mix(BG, INK, a * 0.8), 3)

def b60_grid(c, t, i):
    corner_tag(c, 'B60 · 七块都是小三角形拼的')
    c.text(60, 96, '把正方形划成 16 个一样的小三角形，七块板正好各占整数个', 'serif', 40, INK)
    ox, oy, s = 180, 260, 150
    e = fade(t, 9, 12)
    for k, (nm, pts, n, col) in enumerate(TANGRAM):
        cx, cy = cen(pts)
        dx, dy = (cx - 2) * 0.35 * e, (cy - 2) * 0.35 * e
        draw_piece(c, pts, ox, oy, s, col, 1.0, dx, dy)
    g = fade(t, 2, 4) * (1 - fade(t, 8, 9))
    if g > 0:
        G = mix(BG, INK, g * 0.7)
        for x0, y0 in ((0, 0), (2, 0), (0, 2), (2, 2)):
            X, Y = ox + x0 * s, oy + y0 * s
            c.line([(X, Y), (X + 2 * s, Y + 2 * s)], G, 2)
            c.line([(X + 2 * s, Y), (X, Y + 2 * s)], G, 2)
            c.line([(X, Y), (X + 2 * s, Y), (X + 2 * s, Y + 2 * s), (X, Y + 2 * s), (X, Y)], G, 2)
    a = fade(t, 12, 13)
    if a > 0:
        for k, (nm, pts, n, col) in enumerate(TANGRAM):
            cx, cy = cen(pts)
            dx, dy = (cx - 2) * 0.35, (cy - 2) * 0.35
            c.text(ox + (cx + dx) * s, oy + (cy + dy) * s, str(n), 'bold', 34, mix(BG, INK, a), 'mm')
    b = fade(t, 14, 15)
    if b > 0:
        x0 = 1150
        c.text(x0, 300, '每块占几个小三角形', 'bold', 30, mix(BG, INK, b), 'lm')
        rows = [('大三角 ×2', '4 + 4'), ('中三角', '2'), ('正方形', '2'), ('平行四边形', '2'), ('小三角 ×2', '1 + 1')]
        for k, (nm, v) in enumerate(rows):
            c.text(x0, 370 + k * 56, nm, 'sans', 28, mix(BG, INK, b), 'lm')
            c.text(x0 + 330, 370 + k * 56, v, 'mono', 28, mix(BG, SPARK, b), 'lm')
        c.line([(x0, 650), (x0 + 520, 650)], mix(BG, LINE, b), 2)
        c.text(x0, 690, '合计', 'bold', 30, mix(BG, INK, b), 'lm')
        c.text(x0 + 330, 690, '16', 'mono', 34, mix(BG, GREEN, b), 'lm')
        c.text(x0, 760, '边长只有两种：短边和它的 √2 倍', 'sans', 24, mix(BG, MUTED, b), 'lm')
        c.text(x0, 800, '所以块块都能对上', 'sans', 24, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 8, '把七巧板的正方形横竖对半、再画两条对角线，正好分成 16 个一样的小三角形'),
                (8.2, 14, '七块板沿着这些线切开：大三角 4 个，中三角、正方形、平行四边形各 2 个，小三角 1 个'),
                (14.2, 22, '边长只有两种，所以怎么转、怎么拼，边都对得上')], y=1010)

SHAPES = [
    [(0, 0)] * 7,
    [(0, 0), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 4), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
]

def b60_reshape(c, t, i):
    corner_tag(c, 'B60 · 换个拼法，面积不变')
    c.text(60, 96, '挪一块，轮廓变了；可还是那 16 个小三角形', 'serif', 40, INK)
    ox, oy, s = 300, 230, 110
    p1 = fade(t, 3, 6)
    p2 = fade(t, 9, 12)
    for k, (nm, pts, n, col) in enumerate(TANGRAM):
        d1, d2 = SHAPES[1][k], SHAPES[2][k]
        dx = d1[0] * p1 + (d2[0] - d1[0]) * p2
        dy = d1[1] * p1 + (d2[1] - d1[1]) * p2
        draw_piece(c, pts, ox, oy, s, col, 1.0, dx, dy)
    labels = ['正方形', '挪了一块', '又挪一块']
    stage = 0 if t < 6 else (1 if t < 12 else 2)
    c.rect(1240, 300, 1800, 640, fill=SHEET, r=14)
    c.text(1520, 350, f'形状：{labels[stage]}', 'bold', 32, INK, 'mm')
    c.text(1520, 430, '面积：16 个小三角形', 'sans', 30, GREEN, 'mm')
    c.text(1520, 500, '周长：变了', 'sans', 28, NRED if stage else MUTED, 'mm')
    c.text(1520, 580, '称一称：七块的重量不变', 'sans', 24, MUTED, 'mm')
    b = fade(t, 15, 16)
    if b > 0:
        c.rect(1240, 690, 1800, 860, fill=mix(BG, SHEET, b), r=14)
        c.text(1520, 740, '面积守恒', 'bold', 30, mix(BG, SPARK, b), 'mm')
        c.text(1520, 800, '切开、挪动、翻面，都不增不减', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '先拼成一个正方形'),
                (6.2, 12, '左边的大三角挪到右边，再把上面的大三角挪到下面：轮廓完全变了'),
                (12.2, 22, '轮廓和周长都变了，可面积还是 16 个小三角形：把七块放上秤，重量一克不差（以实测为准）')], y=1010)

# ---------------------------------------------------------------- B61 墨斗
def b61_snap(c, t, i):
    corner_tag(c, 'B61 · 一弹，印下一条直线')
    c.text(60, 96, '绷紧的线自己就走两点之间最短的路：直线', 'serif', 40, INK)
    xL, xR, y0 = 260, 1660, 470
    c.rect(200, y0 - 30, 1720, y0 + 140, fill=WOOD, r=8)
    for x in (xL, xR):
        c.ellipse(x, y0, 12, 12, fill=(150, 150, 160))
    rel = 4.0
    if t < rel:
        lift = 160 * fade(t, 0.8, 3.2)
        amp = lift
    else:
        tt = t - rel
        amp = 160 * math.cos(9 * tt) * math.exp(-1.6 * tt) if tt < 0.17 else 0
        amp = max(amp, 0)
    if t >= rel + 0.17:
        c.line([(xL, y0 + 2), (xR, y0 + 2)], INKB, 10)
    pts = [(xL + (xR - xL) * u / 40, y0 - amp * math.sin(math.pi * u / 40)) for u in range(41)]
    c.line(pts, (235, 230, 215), 2 if t >= rel + 0.17 else 4)
    if 0.8 < t < rel:
        mx = (xL + xR) / 2
        c.arrow(mx, y0 + 60, mx, y0 - amp + 10, MUTED, 3, 14)
        c.text(mx + 30, y0 - amp - 30, '提起来', 'sans', 24, MUTED, 'lm')
    a = fade(t, 8, 9)
    if a > 0:
        yb = 760
        c.text(200, yb - 60, '徒手画的', 'bold', 26, mix(BG, INK, a), 'lm')
        P = [(xL + (xR - xL) * u / 120, yb + 14 * math.sin(u * 0.21) + 9 * math.sin(u * 0.07 + 1)) for u in range(121)]
        c.line(P, mix(BG, NRED, a), 4)
        c.line([(xL, yb + 120), (xR, yb + 120)], mix(BG, INK, a), 5)
        c.text(200, yb + 80, '弹出来的', 'bold', 26, mix(BG, INK, a), 'lm')
        c.text(xR, yb - 60, '最大偏离：…… 毫米 vs …… 毫米（以实测为准）', 'sans', 22, mix(BG, MUTED, a), 'rm')
    caps(c, t, [(0, 4, '墨斗的线浸过墨，两头钉住、拉紧，中间提起来'),
                (4.2, 9, '一松手，线弹回去，正好拍在木头上，印下一条墨线'),
                (9.2, 22, '绷紧的线自己就是两点之间最短的那条路：比尺子一段段接着画还直')], y=1010)

def b61_plumb(c, t, i):
    corner_tag(c, 'B61 · 线坠：指向地心')
    c.text(60, 96, '一根线吊一块重物，静下来就是「铅垂」', 'serif', 40, INK)
    tilt = math.radians(2.5)
    bx, by, H = 700, 900, 640
    top = (bx + H * math.sin(tilt), by - H * math.cos(tilt))
    c.line([(bx, by), top], WOOD, 26)
    c.line([(bx + 260, by), (top[0] + 260, top[1])], WOOD, 26)
    c.line([(top[0] - 13, top[1]), (top[0] + 273, top[1])], WOOD, 26)
    hx, hy = top[0] + 30, top[1] + 20
    L = 560
    ang = 0.25 * math.cos(2.2 * t) * math.exp(-0.45 * t)
    px, py = hx + L * math.sin(ang), hy + L * math.cos(ang)
    c.line([(hx, hy), (px, py)], INK, 2)
    c.poly([(px - 16, py), (px + 16, py), (px, py + 40)], (160, 160, 170))
    a = fade(t, 7, 8)
    if a > 0:
        c.line([(hx, by - 4), (bx + 30, by - 4)], mix(BG, NRED, a), 4)
        c.text(bx - 30, by + 40, '门框歪了：越往下，离线坠越远（示意）', 'sans', 22, mix(BG, NRED, a), 'lm')
    b = fade(t, 11, 12)
    if b > 0:
        c.arrow(1450, 300, 1450, 760, mix(BG, SPARK, b), 5, 22)
        c.text(1490, 530, '重力：指向地心', 'bold', 30, mix(BG, SPARK, b), 'lm')
        c.rect(1240, 820, 1840, 960, fill=mix(BG, SHEET, b), r=12)
        c.text(1540, 860, '手机水平仪：……°（以实测为准）', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(1540, 910, '线坠和手机，量的是同一个方向', 'sans', 22, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 7, '墨斗另一头常拴一个线坠：线一吊，晃几下就停住'),
                (7.2, 13, '停住的线就是竖直线。拿它贴着门框一比，歪没歪一眼就看出来'),
                (13.2, 22, '因为重物总被地球往地心拉：手机里的水平仪，量的也是这个方向')], y=1010)

# ---------------------------------------------------------------- B62 勾股
def tri(a, b, cc):
    # 底边 c 放平，求顶点
    x = (b * b + cc * cc - a * a) / (2 * cc)
    y = math.sqrt(max(b * b - x * x, 0))
    return [(0, 0), (cc, 0), (x, -y)]

def ang_at(P, Q, R):
    v1 = (Q[0] - P[0], Q[1] - P[1]); v2 = (R[0] - P[0], R[1] - P[1])
    cs = (v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))
    return math.degrees(math.acos(max(-1, min(1, cs))))

def b62_rope(c, t, i):
    corner_tag(c, 'B62 · 13 个结的绳子')
    c.text(60, 96, '12 段一样长的绳子：围成 3、4、5，最大的角就是直角', 'serif', 40, INK)
    sets = [(4, 4, 4), (2, 5, 5), (3, 4, 5)]
    s = 80
    for k, (a, b, cc) in enumerate(sets):
        al = fade(t, 1 + k * 5, 2.5 + k * 5)
        if al <= 0: continue
        ox, oy = 200 + k * 580, 800
        P = tri(a, b, cc)
        Q = [(ox + x * s, oy + y * s) for x, y in P]
        col = GREEN if k == 2 else ROPE
        c.line(Q + [Q[0]], mix(BG, col, al), 6)
        # knots every unit
        for (p0, p1), n in zip(((Q[0], Q[1]), (Q[1], Q[2]), (Q[2], Q[0])), (cc, a, b)):
            for j in range(n):
                u = j / n
                c.ellipse(p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u, 7, 7, fill=mix(BG, INK, al))
        angs = [ang_at(Q[0], Q[1], Q[2]), ang_at(Q[1], Q[2], Q[0]), ang_at(Q[2], Q[0], Q[1])]
        m = max(range(3), key=lambda j: angs[j])
        v = Q[m]
        c.text(ox + cc * s / 2, oy + 60, f'{a} - {b} - {cc}', 'mono', 30, mix(BG, INK, al), 'mm')
        c.text(ox + cc * s / 2, oy + 110, f'最大角 {angs[m]:.0f}°', 'bold', 28, mix(BG, GREEN if k == 2 else MUTED, al), 'mm')
        if k == 2 and al >= 1:
            w = Q[(m + 1) % 3]; u = Q[(m + 2) % 3]
            d1 = ((w[0] - v[0]) / math.hypot(w[0] - v[0], w[1] - v[1]), (w[1] - v[1]) / math.hypot(w[0] - v[0], w[1] - v[1]))
            d2 = ((u[0] - v[0]) / math.hypot(u[0] - v[0], u[1] - v[1]), (u[1] - v[1]) / math.hypot(u[0] - v[0], u[1] - v[1]))
            r = 34
            c.line([(v[0] + d1[0] * r, v[1] + d1[1] * r), (v[0] + (d1[0] + d2[0]) * r, v[1] + (d1[1] + d2[1]) * r), (v[0] + d2[0] * r, v[1] + d2[1] * r)], NRED, 4)
    caps(c, t, [(0, 6, '一根绳子打 13 个等距的结，分成 12 段一样长'),
                (6.2, 13, '围成 4、4、4，角都是 60 度；围成 2、5、5，尖尖的'),
                (13.2, 22, '围成 3、4、5：最大的那个角，正好是直角。古人在地上放大直角，不用角尺')], y=1010)

A3, B4 = 3, 4
T1 = [(0, 0), (4, 0), (0, 3)]
T2 = [(4, 0), (7, 0), (7, 4)]
T3 = [(7, 4), (7, 7), (3, 7)]
T4 = [(3, 7), (0, 7), (0, 3)]
MOVES = [(3, 0), (-4, 3), (0, -4), (0, 0)]
TCOL = [(220, 90, 80), (240, 170, 70), (90, 170, 110), (80, 150, 210)]

def b62_xiantu(c, t, i):
    corner_tag(c, 'B62 · 赵爽弦图')
    c.text(60, 96, '同一个大正方形，四个三角形换个位置', 'serif', 40, INK)
    s = 80
    ox, oy = 240, 230
    W = 7 * s
    c.rect(ox, oy, ox + W, oy + W, fill=SHEET, outline=LINE, width=3)
    p = fade(t, 8, 12)
    if p < 0.5:
        q = 1 - fade(t, 7, 8)
        c.poly([(ox + 4 * s, oy), (ox + 7 * s, oy + 4 * s), (ox + 3 * s, oy + 7 * s), (ox, oy + 3 * s)], mix(SHEET, (60, 90, 130), q))
        c.text(ox + 3.5 * s, oy + 3.5 * s, '弦² = 25', 'bold', 38, mix(SHEET, INK, q), 'mm')
    else:
        q = fade(t, 12, 13)
        c.rect(ox, oy, ox + 3 * s, oy + 3 * s, fill=mix(SHEET, (130, 80, 60), q))
        c.rect(ox + 3 * s, oy + 3 * s, ox + 7 * s, oy + 7 * s, fill=mix(SHEET, (60, 90, 130), q))
        c.text(ox + 1.5 * s, oy + 1.5 * s, '勾² = 9', 'bold', 30, mix(SHEET, INK, q), 'mm')
        c.text(ox + 5 * s, oy + 5 * s, '股² = 16', 'bold', 34, mix(SHEET, INK, q), 'mm')
    for T, (mx, my), col in zip((T1, T2, T3, T4), MOVES, TCOL):
        P = [(ox + (x + mx * p) * s, oy + (y + my * p) * s) for x, y in T]
        c.poly(P, col)
        c.line(P + [P[0]], INK, 3)
    a = fade(t, 14, 15)
    if a > 0:
        c.rect(1060, 300, 1820, 700, fill=mix(BG, SHEET, a), r=14)
        c.text(1440, 360, '大正方形没变，四个三角形没变', 'sans', 28, mix(BG, INK, a), 'mm')
        c.text(1440, 420, '剩下的空白面积也不会变', 'sans', 28, mix(BG, INK, a), 'mm')
        c.text(1440, 520, '勾² + 股² = 弦²', 'bold', 44, mix(BG, SPARK, a), 'mm')
        c.text(1440, 600, '9 + 16 = 25', 'mono', 36, mix(BG, GREEN, a), 'mm')
        c.text(1440, 660, '三国 · 赵爽注《周髀算经》（拍摄前核对）', 'sans', 22, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '边长 3 加 4 的大正方形里放四个直角三角形，中间空出一个斜放的正方形：弦的平方'),
                (7.2, 13, '四个三角形只平移、不转动，换到两两拼成长方形的位置'),
                (13.2, 22, '空白变成两个小正方形：勾的平方加股的平方。空白面积没变，所以两者相等')], y=1010)


CLIPS = {
 'B60_十六格': (b60_grid, 22), 'B60_重拼': (b60_reshape, 22),
 'B60_片头': (titles.opening(BSER, VOL18, SB18, 0, '宋《燕几图》→ 清 · 七巧板'), 7),
 'B60_片尾': (titles.closing(BSER, VOL18, SB18, 0, '下集：木匠弹一下墨线，为什么比尺子画得还直？'), 7),
 'B61_弹线': (b61_snap, 22), 'B61_线坠': (b61_plumb, 22),
 'B61_片头': (titles.opening(BSER, VOL18, SB18, 1, '相传鲁班 · 墨斗'), 7),
 'B61_片尾': (titles.closing(BSER, VOL18, SB18, 1, '下集：一根打了结的绳子，怎么拉出一个直角？'), 7),
 'B62_绳结': (b62_rope, 22), 'B62_弦图': (b62_xiantu, 22),
 'B62_片头': (titles.opening(BSER, VOL18, SB18, 2, '《周髀算经》· 勾三股四弦五'), 7),
 'B62_片尾': (titles.closing(BSER, VOL18, SB18, 2, '下集：一根斜插的针，为什么能当钟用？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
