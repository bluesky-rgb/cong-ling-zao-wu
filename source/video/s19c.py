"""第十九季（第六层）第三批：E108 手机里的陀螺仪、E109 空调与热泵、E110 芯片光刻 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s19a import S19A, SER19, VOL19, ELEC

HOT = (235, 110, 80)
COLD = (90, 170, 240)
SI = (150, 160, 180)

def rot(p, c0, a):
    x, y = p[0] - c0[0], p[1] - c0[1]
    return (c0[0] + x * math.cos(a) - y * math.sin(a), c0[1] + x * math.sin(a) + y * math.cos(a))

# ---------------------------------------------------------------- E108 手机里的陀螺仪
def e108_accel(c, t, i):
    corner_tag(c, '第 108 集 · 芯片上的小弹簧')
    c.text(60, 96, '加速度计：一块挂在弹簧上的小质量块，用电容量它挪了多少', 'serif', 40, INK)
    th = math.radians(80) * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi * 1.5))
    pc = (380, 600)
    body = [(-130, -240), (130, -240), (130, 240), (-130, 240)]
    P = [rot((pc[0] + x, pc[1] + y), pc, th) for x, y in body]
    c.poly(P, SHEET)
    c.line(P + [P[0]], INK, 4)
    c.arrow(120, 300, 120, 400, MUTED, 3, 14)
    c.text(140, 360, '重力', 'sans', 22, MUTED, 'lm')
    # MEMS chip view
    cx, cy = 1050, 560
    c.rect(cx - 330, cy - 230, cx + 330, cy + 230, outline=SI, width=4, r=10)
    disp = 70 * math.sin(th)
    mx = cx + disp
    c.rect(mx - 120, cy - 110, mx + 120, cy + 110, fill=mix(BG, SI, 0.6), r=6)
    for side in (-1, 1):
        x_anchor = cx + side * 330
        x_mass = mx + side * 120
        n = 8
        pts = [(x_anchor + (x_mass - x_anchor) * k / n, cy + (14 if k % 2 else -14) * (0 < k < n)) for k in range(n + 1)]
        c.line(pts, INK, 3)
    for k in range(5):
        y = cy - 80 + k * 40
        c.line([(mx - 60, y), (mx + 60, y)], COPPER, 4)
        c.line([(cx - 60, y + 14), (cx + 60, y + 14)], (220, 200, 120), 4)
    c.text(cx, cy + 270, '芯片里的样子（示意，实际只有零点几毫米）', 'sans', 22, MUTED, 'mm')
    gx, gy = 9.8 * math.sin(th), 9.8 * math.cos(th)
    c.rect(1460, 300, 1860, 560, fill=SHEET, r=14)
    c.text(1660, 340, '传感器 App 读数', 'sans', 22, MUTED, 'mm')
    c.text(1500, 410, f'x：{gx:5.1f}', 'mono', 32, INK, 'lm')
    c.text(1500, 470, f'y：{gy:5.1f}', 'mono', 32, INK, 'lm')
    c.text(1660, 530, '米 / 秒²', 'sans', 20, MUTED, 'mm')
    c.text(1660, 620, f'倾斜 {math.degrees(th):.0f}°', 'bold', 30, SPARK, 'mm')
    caps(c, t, [(0, 7, '手机里有一块比芝麻还小的芯片，上面刻着一块挂在弹簧上的硅质量块'),
                (7.2, 14, '手机一歪，重力把质量块往一边拉，它和旁边梳齿之间的距离变了，电容也跟着变'),
                (14.2, 22, '芯片量出两个方向各被拉了多少，就知道手机是横着还是竖着')], y=1010)

def e108_gyro(c, t, i):
    corner_tag(c, '第 108 集 · 振动的陀螺仪')
    c.text(60, 96, '手机里的陀螺仪不转：一块质量块来回振，一转身它就被往旁边推', 'serif', 40, INK)
    cx, cy = 640, 560
    w = 0 if t < 7 else (1.0 if t < 15 else 2.0)
    c.rect(cx - 300, cy - 300, cx + 300, cy + 300, outline=SI, width=4, r=12)
    trail = []
    for k in range(40):
        tt = t - k * 0.02
        x = 220 * math.sin(tt * 9)
        vx = 220 * 9 * math.cos(tt * 9)
        y = -w * vx * 0.04
        trail.append((cx + x, cy + y))
    seg(c, trail[::-1], mix(BG, ELEC, 0.6), 3)
    x, y = trail[0]
    c.rect(x - 40, y - 40, x + 40, y + 40, fill=SI, r=6)
    c.arrow(cx - 260, cy + 250, cx + 260, cy + 250, MUTED, 2, 12)
    c.arrow(cx + 260, cy + 250, cx - 260, cy + 250, MUTED, 2, 12)
    c.text(cx, cy + 280, '一直左右振动', 'sans', 22, MUTED, 'mm')
    if w > 0:
        c.arc(cx, cy, 360, 360, -60, -10, NRED, 5)
        c.text(cx + 330, cy - 340, f'手机在转：{"慢" if w < 1.5 else "快"}', 'bold', 28, NRED, 'mm')
    c.rect(1240, 320, 1840, 640, fill=SHEET, r=14)
    c.text(1540, 370, '上下被推开多少', 'sans', 24, MUTED, 'mm')
    c.rect(1300, 430, 1300 + 480 * w / 2, 480, fill=GREEN, r=6)
    c.text(1540, 540, '= 手机转得多快', 'bold', 30, INK, 'mm')
    c.text(1540, 600, '（科里奥利力）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '陀螺仪芯片里，一块质量块被电推着一直左右振动'),
                (7.2, 15, '手机一转身，振动的质量块就被往垂直方向推开一点，这个力叫科里奥利力'),
                (15.2, 22, '转得越快，推开得越多：芯片量出这一点点位移，就知道手机转得多快')], y=1010)

# ---------------------------------------------------------------- E109 空调与热泵
LOOP = [(420, 300), (1500, 300), (1500, 820), (420, 820)]

def _loop_pt(s):
    per = 2 * (1080 + 520)
    s = s % per
    if s < 1080: return (420 + s, 300), 0
    s -= 1080
    if s < 520: return (1500, 300 + s), 1
    s -= 520
    if s < 1080: return (1500 - s, 820), 2
    s -= 1080
    return (420, 820 - s), 3

def e109_cycle(c, t, i):
    corner_tag(c, '第 109 集 · 把热搬出去')
    c.text(60, 96, '空调不造冷：它把屋里的热，搬到屋外去', 'serif', 40, INK)
    c.rect(380, 160, 1540, 335, fill=mix(BG, HOT, 0.12), r=14)
    c.text(1700, 300, '屋外', 'bold', 30, HOT, 'mm')
    c.rect(380, 785, 1540, 965, fill=mix(BG, COLD, 0.12), r=14)
    c.text(1700, 820, '屋里', 'bold', 30, COLD, 'mm')
    c.line(LOOP + [LOOP[0]], mix(BG, LINE, 0.8), 14)
    c.rect(1380, 520, 1620, 640, fill=(120, 120, 130), r=12)
    c.text(1500, 580, '压缩机', 'bold', 26, (240, 240, 240), 'mm')
    c.rect(330, 520, 510, 600, fill=(160, 160, 170), r=8)
    c.text(420, 560, '膨胀阀', 'bold', 22, (30, 30, 30), 'mm')
    c.text(960, 260, '冷凝器（屋外机）：热的制冷剂放热', 'sans', 24, HOT, 'mm')
    c.text(960, 870, '蒸发器（屋里机）：冷的制冷剂吸热', 'sans', 24, COLD, 'mm')
    per = 2 * (1080 + 520)
    for k in range(18):
        s = (-t * 160 + k * per / 18)
        (x, y), seg_i = _loop_pt(s)
        if seg_i == 0: col = HOT
        elif seg_i == 1: col = HOT if y < 580 else COLD
        elif seg_i == 2: col = COLD
        else: col = HOT if y < 560 else COLD
        c.ellipse(x, y, 14, 14, fill=col)
    for k in range(4):
        x = 600 + k * 220
        ph = (t * 0.8 + k * 0.25) % 1
        c.arrow(x, 280 - 10, x, 280 - 10 - 80 * ph, mix(BG, HOT, 1 - ph), 4, 12)
        c.arrow(x, 950, x, 950 - 110 * ph, mix(BG, COLD, 1 - ph), 4, 12)
    caps(c, t, [(0, 7, '管子里流着制冷剂。在屋里，它被放得很松、变得很冷，从屋里的空气里吸走热量'),
                (7.2, 14, '压缩机把它使劲一压，它变得很热，比屋外还热'),
                (14.2, 22, '热的制冷剂流到屋外机，把热放给屋外的空气；再经膨胀阀一松，又变冷，回到屋里接着吸热')], y=1010)

def e109_cop(c, t, i):
    corner_tag(c, '第 109 集 · 搬热比造热省电')
    c.text(60, 96, '用 1 份电造热，只得 1 份热；用 1 份电搬热，能搬 3 份以上', 'serif', 40, INK)
    a = fade(t, 1, 3)
    b = fade(t, 6, 9)
    x0, base, u = 300, 820, 150
    c.text(x0 + 140, 300, '电暖器', 'bold', 30, INK, 'mm')
    c.rect(x0, base - u * a, x0 + 120, base, fill=SPARK)
    c.text(x0 + 60, base + 40, '电 1', 'mono', 24, INK, 'mm')
    c.rect(x0 + 160, base - u * a, x0 + 280, base, fill=HOT)
    c.text(x0 + 220, base + 40, '热 1', 'mono', 24, INK, 'mm')
    x1 = 900
    c.text(x1 + 260, 300, '热泵', 'bold', 30, INK, 'mm')
    c.rect(x1, base - u * a, x1 + 120, base, fill=SPARK)
    c.text(x1 + 60, base + 40, '电 1', 'mono', 24, INK, 'mm')
    c.rect(x1 + 160, base - u * 2 * b, x1 + 280, base, fill=COLD)
    c.text(x1 + 220, base + 40, '屋外搬来', 'sans', 20, INK, 'mm')
    c.rect(x1 + 320, base - u * 3 * b - u * a * 0 , x1 + 440, base, fill=HOT)
    c.text(x1 + 380, base + 40, f'热 {1 + 2 * b:.1f}', 'mono', 24, INK, 'mm')
    d = fade(t, 13, 14)
    if d > 0:
        c.rect(1420, 330, 1860, 640, fill=mix(BG, SHEET, d), r=14)
        c.text(1640, 380, '橡皮筋也会「搬热」', 'bold', 28, mix(BG, INK, d), 'mm')
        c.text(1640, 450, '一拉长：贴嘴唇变热', 'sans', 24, mix(BG, HOT, d), 'mm')
        c.text(1640, 510, '一放松：贴嘴唇变凉', 'sans', 24, mix(BG, COLD, d), 'mm')
        c.text(1640, 590, '（倍数以资料为准）', 'sans', 20, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '电暖器把电直接变成热：用一份电，得一份热'),
                (6.2, 13, '热泵不造热，它用电去「搬」：冬天把屋外空气里的热搬进屋，加上电本身，能得到三份以上的热'),
                (13.2, 22, '一根粗橡皮筋就能感觉到：快速拉长，贴到嘴唇上是热的；拉着等它凉了，一松手，又变凉了')], y=1010)

# ---------------------------------------------------------------- E110 芯片光刻
PATTERN = [[(0, 0), (1, 0)], [(1, 0), (1, 1)], [(0.2, 0.5), (0.8, 0.5)], [(0, 1), (0.6, 1)], [(0.3, 0), (0.3, 0.5)]]

def e110_project(c, t, i):
    corner_tag(c, '第 110 集 · 把电路图缩小「照」上去')
    c.text(60, 96, '光穿过掩模上的电路图，透镜把它缩小，照在涂了感光胶的硅片上', 'serif', 40, INK)
    Lx, Mx, Ox, Wx = 160, 520, 1060, 1500
    yc = 560
    c.ellipse(Lx, yc, 30, 30, fill=(200, 160, 250))
    c.text(Lx, yc + 60, '紫外光', 'sans', 22, MUTED, 'mm')
    H1 = 300
    c.rect(Mx - 10, yc - H1 / 2, Mx + 10, yc + H1 / 2, fill=SHEET)
    c.text(Mx, yc - H1 / 2 - 30, '掩模（电路图）', 'sans', 22, INK, 'mm')
    c.ellipse(Ox, yc, 40, 220, outline=COLD, width=5)
    c.text(Ox, yc - 250, '透镜', 'sans', 22, COLD, 'mm')
    H2 = 75
    c.rect(Wx - 10, yc - 200, Wx + 10, yc + 200, fill=SI)
    c.text(Wx, yc - 230, '硅片', 'sans', 22, INK, 'mm')
    p = fade(t, 2, 8)
    for y0 in (-H1 / 2, 0, H1 / 2):
        y1 = -y0 * H2 / H1
        pts = [(Lx, yc), (Mx, yc + y0), (Ox, yc + y0 * 0.45), (Wx, yc + y1)]
        segs = list(zip(pts, pts[1:]))
        tot = sum(math.dist(a, b) for a, b in segs)
        d = p * tot
        out = [pts[0]]
        for a, b in segs:
            L = math.dist(a, b)
            if d <= 0: break
            u = min(1, d / L)
            out.append((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u))
            d -= L
        if len(out) > 1:
            c.line(out, (200, 160, 250), 2)
    # 掩模图案（左下放大）与成像（右下）
    a = fade(t, 9, 10)
    if a > 0:
        bx, by, S = 250, 700, 150
        c.rect(bx - 20, by - 20, bx + S + 20, by + S + 20, fill=mix(BG, SHEET, a), r=8)
        for (p0, p1) in PATTERN:
            c.line([(bx + p0[0] * S, by + p0[1] * S), (bx + p1[0] * S, by + p1[1] * S)], mix(BG, INK, a), 10)
        c.text(bx + S / 2, by + S + 50, '掩模上：大', 'sans', 22, mix(BG, INK, a), 'mm')
        sx, sy, s2 = 1450, 820, 50
        c.rect(sx - 10, sy - 10, sx + s2 + 10, sy + s2 + 10, fill=mix(BG, SI, a), r=4)
        for (p0, p1) in PATTERN:
            c.line([(sx + (1 - p0[0]) * s2, sy + (1 - p0[1]) * s2), (sx + (1 - p1[0]) * s2, sy + (1 - p1[1]) * s2)], mix(BG, GREEN, a), 3)
        c.text(sx + s2 / 2, sy + s2 + 50, '硅片上：缩小 4 倍（示意）', 'sans', 22, mix(BG, GREEN, a), 'mm')
    caps(c, t, [(0, 7, '先在硅片上涂一层感光胶，就像第 55 集照相用的底片'),
                (7.2, 14, '紫外光穿过画着电路的掩模，再经过一组透镜，电路图被缩小、倒过来，照到硅片上'),
                (14.2, 22, '照到的胶变了性，洗掉以后，就在硅片上留下一模一样的小电路：一次照几十亿个晶体管')], y=1010)

def e110_limit(c, t, i):
    corner_tag(c, '第 110 集 · 光的「笔尖」有多粗')
    c.text(60, 96, '两条挨得很近的线，光的波长太长，就糊成一条', 'serif', 40, INK)
    cases = [('紫外汞灯 365 纳米', 365), ('深紫外 193 纳米', 193), ('极紫外 13.5 纳米', 13.5)]
    k = min(int(t / 6.5), 2)
    for j, (nm, lam) in enumerate(cases):
        a = 1.0 if j == k else 0.35
        y0 = 280 + j * 230
        c.text(120, y0 + 90, nm, 'bold', 28, mix(BG, INK, a), 'lm')
        x0, W, H = 640, 1100, 160
        c.line([(x0, y0 + H), (x0 + W, y0 + H)], mix(BG, LINE, a), 2)
        sep = 100
        sig = 18 + lam * 0.32
        pts = []
        for xx in range(0, W + 1, 6):
            xn = xx - W / 2
            v = math.exp(-((xn + sep / 2) / sig) ** 2) + math.exp(-((xn - sep / 2) / sig) ** 2)
            pts.append((x0 + xx, y0 + H - H * min(v, 1.6) / 1.6))
        c.line(pts, mix(BG, SPARK, a), 4)
        for s in (-1, 1):
            c.line([(x0 + W / 2 + s * sep / 2, y0 + H + 10), (x0 + W / 2 + s * sep / 2, y0 + H + 30)], mix(BG, GREEN, a), 4)
        mid = math.exp(-((sep / 2) / sig) ** 2) * 2
        ok = mid < 0.8
        c.text(x0 + W + 30, y0 + H / 2, '分得开' if ok else '糊成一条', 'bold', 26, mix(BG, GREEN if ok else NRED, a), 'lm')
    caps(c, t, [(0, 6.5, '光是波，透镜聚出来的光斑最小也有波长那么宽：两条线靠得太近，就分不开'),
                (6.5, 13, '所以光刻机一代代换更短的光：紫外、深紫外'),
                (13, 22, '今天最先进的用 13.5 纳米的极紫外光，才能画出最细的电路（数值拍摄前核对）')], y=1010)


CLIPS = {
 'E108_加速度计': (e108_accel, 22), 'E108_陀螺仪': (e108_gyro, 22),
 'E108_片头': (titles.opening(SER19, VOL19, S19A, 6, '2007 年起手机内置 MEMS 传感器'), 7),
 'E108_片尾': (titles.closing(SER19, VOL19, S19A, 6, '下集：空调制冷，热量去哪了？'), 7),
 'E109_循环': (e109_cycle, 22), 'E109_搬热': (e109_cop, 22),
 'E109_片头': (titles.opening(SER19, VOL19, S19A, 7, '1902 年开利空调 · 热泵'), 7),
 'E109_片尾': (titles.closing(SER19, VOL19, S19A, 7, '下集：指甲盖大的芯片，怎么塞进几百亿个晶体管？'), 7),
 'E110_缩小投影': (e110_project, 22), 'E110_波长': (e110_limit, 22),
 'E110_片头': (titles.opening(SER19, VOL19, S19A, 8, '1959 年平面工艺 · 极紫外光刻'), 7),
 'E110_片尾': (titles.closing(SER19, VOL19, S19A, 8, '下集：一堆火柴盒，怎么学会下棋？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
