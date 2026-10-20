"""第六季第一批：E45 摆钟、B11 一钟双音、B9 鱼洗 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL

S6A = [('45', '摆钟'), ('46', '温度计'), ('47', '影子测地球'), ('48', '数字与0'), ('49', '复式记账'), ('50', '光学电报')]
SB6 = [('B11', '一钟双音'), ('B9', '鱼洗'), ('B10', '透光镜'), ('B18', '地动仪')]
SER6, VOL6 = '从零造物', '第六季 · 信息与测量'

BRONZE = (176, 132, 72)
STRING = (200, 200, 205)
GREEN = (110, 190, 110)

def theta_exact(amp_deg, t, L):
    """small-angle-corrected pendulum angle (approx using exact period)"""
    T0 = 2 * math.pi * math.sqrt(L / 9.81)
    a = math.radians(amp_deg)
    # period correction series
    k = math.sin(a / 2)
    T = T0 * (1 + k ** 2 / 4 + 9 * k ** 4 / 64 + 25 * k ** 6 / 256)
    return a * math.cos(2 * math.pi * t / T), T

def pend(c, x, y, Lpx, ang, col, bob=26):
    bx, by = x + Lpx * math.sin(ang), y + Lpx * math.cos(ang)
    c.line([(x, y), (bx, by)], STRING, 3)
    c.ellipse(bx, by, bob, bob, fill=col)
    return bx, by

# ---------------------------------------------------------------- E45 摆钟
def e45_isochron(c, t, i):
    corner_tag(c, '第 45 集 · 摆的等时性')
    c.text(60, 96, '摆得大、摆得小，一个来回的时间一样吗？', 'serif', 40, INK)
    part2 = t >= 11
    top = 200
    if not part2:
        sets = [(560, 1.0, 10, FIELD, '摆幅 10°'), (1360, 1.0, 30, COPPER, '摆幅 30°')]
    else:
        sets = [(420, 0.25, 15, FIELD, '摆长 25 厘米'), (960, 0.5, 15, SPARK, '摆长 50 厘米'), (1500, 1.0, 15, COPPER, '摆长 1 米')]
    tt = t if not part2 else t - 11
    for x, L, amp, col, lab in sets:
        ang, T = theta_exact(amp, tt, L)
        Lpx = 600 * math.sqrt(L) if part2 else 560
        Lpx = 560 * L if part2 else 560
        Lpx = max(Lpx, 140)
        c.rect(x - 60, top - 10, x + 60, top, fill=MUTED)
        pend(c, x, top, Lpx, ang, col)
        c.text(x, 870, lab, 'bold', 30, col, 'mm')
        c.text(x, 920, f'来回一次 {T:.2f} 秒', 'mono', 28, INK, 'mm')
    caps(c, t, [(0, 5, '同样长的两个摆，一个摆得小，一个摆得大'),
                (5.2, 11, '来回一次的时间几乎一样：摆幅大一点，只慢一点点'),
                (11.2, 17, '换摆长：25 厘米、50 厘米、1 米'),
                (17.2, 22, '摆长变成 4 倍，周期变成 2 倍：时间只看摆长')], y=1010)

def e45_escapement(c, t, i):
    corner_tag(c, '第 45 集 · 擒纵')
    c.text(60, 96, '摆怎么管住钟的齿轮？', 'serif', 40, INK)
    px, py = 760, 190
    ang, T = theta_exact(8, t, 1.0)
    def rot(dx, dy):
        return (px + dx * math.cos(ang) + dy * math.sin(ang), py - dx * math.sin(ang) + dy * math.cos(ang))
    # pendulum rod (behind)
    bx, by = rot(0, 640)
    c.line([(px, py), (bx, by)], STRING, 5)
    c.ellipse(bx, by, 36, 36, fill=COPPER)
    c.rect(px - 60, py - 12, px + 60, py, fill=MUTED)
    # escape wheel
    steps = math.floor(2 * t / T)
    wang = steps * (2 * math.pi / 30)
    wx, wy = px, py + 260
    n = 30
    pts = []
    for k in range(n * 2):
        th = wang + k * math.pi / n
        r = 110 if k % 2 == 0 else 88
        pts.append((wx + r * math.cos(th), wy + r * math.sin(th)))
    c.poly(pts, mix(BG, (205, 160, 80), 0.9))
    c.ellipse(wx, wy, 14, 14, fill=BG)
    # anchor
    for s_ in (-1, 1):
        a0 = rot(0, 60); a1 = rot(s_ * 140, 150); a2 = rot(s_ * 110, 230)
        c.line([a0, a1, a2], NRED, 10)
        c.ellipse(a2[0], a2[1], 10, 10, fill=NRED)
    c.text(px - 230, py + 120, '锚', 'bold', 30, NRED, 'mm')
    # drum and weight
    c.line([(wx + 160, wy), (wx + 160, wy + 300 + steps * 3)], STRING, 3)
    c.line([(wx, wy), (wx + 160, wy)], MUTED, 4)
    c.rect(wx + 135, wy + 300 + steps * 3, wx + 185, wy + 380 + steps * 3, fill=MUTED, r=6)
    c.text(wx + 210, wy + 340, '重锤：想让轮子一直转', 'sans', 24, MUTED, 'lm')
    c.text(1300, 300, f'已经放过 {steps} 个齿', 'bold', 30, SPARK, 'lm')
    c.text(1300, 360, '摆每摆一下，锚放过一个齿', 'sans', 26, INK, 'lm')
    c.text(1300, 410, '齿数 = 摆动次数 = 时间', 'sans', 26, INK, 'lm')
    a = fade(t, 14, 15)
    c.rect(1280, 500, 1860, 720, fill=mix(BG, SHEET, a), r=12)
    c.text(1310, 545, '1656 年 惠更斯：第一台摆钟', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1310, 600, '北宋 苏颂水运仪象台：', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1310, 645, '用水斗和「天衡」一格一格放行', 'sans', 24, mix(BG, COPPER, a), 'lm')
    caps(c, t, [(0, 6, '重锤拉着齿轮，想让它一口气转下去'),
                (6.2, 14, '摆上的「锚」左右卡住齿轮：摆每摆一下，只放过一个齿'),
                (14.2, 22, '摆的周期稳定，齿轮就一格一格稳稳地走：这就是钟')], y=1010)

# ---------------------------------------------------------------- B11 一钟双音
def lens(c, cx, cy, w, h, mode, amp, a=1.0, col=BRONZE):
    """合瓦形截面（两段圆弧围成的透镜形）。mode 0：正鼓音；mode 1：侧鼓音（振型转 45°）"""
    R = (w * w + h * h) / (2 * h)
    d = R - h
    base = []
    for k in range(61):
        x = -w + 2 * w * k / 60
        base.append((x, -(math.sqrt(max(0, R * R - x * x)) - d)))
    for k in range(61):
        x = w - 2 * w * k / 60
        base.append((x, math.sqrt(max(0, R * R - x * x)) - d))
    phase = math.pi / 2 if mode == 0 else math.pi / 4
    pts = []
    for x, y in base:
        th = math.atan2(y / h, x / w)
        disp = amp * math.cos(2 * (th - phase))
        r = math.hypot(x, y) or 1
        pts.append((cx + x + x / r * disp, cy + y + y / r * disp))
    c.poly(pts, mix(BG, col, 0.85 * a))
    c.line(pts + [pts[0]], mix(BG, col, a), 4)

def b11_modes(c, t, i):
    corner_tag(c, 'B11 · 两种振动')
    c.text(60, 96, '从上往下看编钟的截面：一个扁扁的「合瓦形」', 'serif', 40, INK)
    for k, (cx, lab, hit) in enumerate([(560, '敲正面中间：正鼓音', (0, 1)), (1360, '敲侧面：侧鼓音', (math.sqrt(0.5), math.sqrt(0.5)))]):
        a = fade(t, 1 + k * 7, 2 + k * 7)
        if a <= 0: continue
        amp = 26 * math.sin(t * (14 if k == 0 else 17)) * a
        lens(c, cx, 520, 300, 150, k, amp, a)
        hx, hy = cx + hit[0] * 300, 520 + hit[1] * 150
        c.arrow(hx + (0 if k == 0 else 90), hy + 90, hx + (0 if k == 0 else 10), hy + 15, mix(BG, NRED, a), 6, 18)
        c.text(cx, 815, lab, 'bold', 30, mix(BG, INK, a), 'mm')
        # node markers
        for j in range(4):
            th = j * math.pi / 2 + math.pi / 4 + (0 if k == 0 else math.pi / 4)
            c.ellipse(cx + 330 * math.cos(th) * 0.75, 520 + 150 * math.sin(th) * 0.75, 9, 9, fill=mix(BG, SPARK, a))
        c.text(cx, 855, '黄点：几乎不动的「节点」', 'sans', 22, mix(BG, SPARK, a), 'mm')
    b = fade(t, 15, 16)
    c.rect(360, 885, 1560, 965, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 925, '一种振动的「节点」，正好是另一种振动最强的地方：敲哪里，就主要激发哪一种', 'sans', 26, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 8, '敲正面中间：钟壁按一种方式振动，发出「正鼓音」'),
                (8.2, 15, '敲侧面：换成另一种振动方式，发出另一个音「侧鼓音」'),
                (15.2, 22, '扁扁的截面让两种振动的频率分开，一口钟就有了两个音')], y=1010)

def b11_decay(c, t, i):
    corner_tag(c, 'B11 · 圆钟和扁钟')
    c.text(60, 96, '为什么编钟不做成圆的？', 'serif', 40, INK)
    for k, (y0, lab, tau, col) in enumerate([(330, '圆钟：余音很长，嗡嗡不停', 6.0, FIELD), (680, '合瓦形：余音很快收住', 1.0, COPPER)]):
        a = fade(t, 0.5 + k * 5, 1.5 + k * 5)
        if a <= 0: continue
        c.text(140, y0 - 120, lab, 'bold', 30, mix(BG, col, a), 'lm')
        c.line([(140, y0), (1780, y0)], mix(BG, LINE, a), 2)
        pts = []
        t0 = 1 + k * 5
        for j in range(0, 1601, 4):
            tt = j / 1600 * 8
            if tt > t - t0: break
            v = 0
            for strike in (0, 2.6, 5.2):
                if tt >= strike:
                    v += 90 * math.exp(-(tt - strike) / tau) * math.sin((tt - strike) * 40)
            pts.append((140 + j, y0 + max(-120, min(120, v))))
        if len(pts) > 1: c.line(pts, mix(BG, col, a), 3)
        for rep in range(3):
            x = 140 + rep * 2.6 / 8 * 1600
            c.text(x, y0 + 130, '敲', 'sans', 22, mix(BG, NRED, a), 'mm')
    b = fade(t, 13, 14)
    c.text(960, 930, '连续敲不同的钟，前一个音很快收住，才不会和后一个混成一片', 'sans', 28, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 5, '圆钟敲一下，声音要很久才消失'),
                (5.2, 13, '合瓦形的钟边缘像两片瓦合在一起，振动很快衰减，余音短'),
                (13.2, 22, '编钟要演奏旋律：一个音收住，下一个音才能清楚')], y=1010)

# ---------------------------------------------------------------- B9 鱼洗
def seg(c, pts, col, w):
    for p, q in zip(pts, pts[1:]):
        c.line([p, q], col, w)

def b9_standing(c, t, i):
    corner_tag(c, 'B9 · 驻波')
    c.text(60, 96, '两列波迎面相遇，会怎样？', 'serif', 40, INK)
    x0, x1, y = 160, 1760, 520
    L = x1 - x0
    k = 4 * math.pi / L * 1.0     # two full wavelengths
    w = 3.0
    show_parts = t < 9
    a1 = fade(t, 0.5, 1.5)
    ptsA, ptsB, ptsS = [], [], []
    for j in range(0, 401):
        x = x0 + j / 400 * L
        yA = 80 * math.sin(k * (x - x0) - w * t)
        yB = 80 * math.sin(k * (x - x0) + w * t)
        ptsA.append((x, y - 220 + yA)); ptsB.append((x, y - 220 + yB)); ptsS.append((x, y + 120 + yA + yB))
    if show_parts or True:
        seg(c, ptsA, mix(BG, FIELD, a1 * 0.9), 3)
        seg(c, ptsB, mix(BG, COPPER, a1 * 0.9), 3)
        c.text(x0, y - 340, '蓝：往右走的波　　橙：往左走的波', 'sans', 24, MUTED, 'lm')
    b = fade(t, 4, 5)
    seg(c, ptsS, mix(BG, INK, b), 5)
    c.text(x0, y + 10, '合起来：驻波', 'bold', 28, mix(BG, INK, b), 'lm')
    for n in range(5):
        x = x0 + n * L / 4
        if t > 9: c.ellipse(x, y + 120, 11, 11, fill=mix(BG, SPARK, fade(t, 9, 10)))
    for n in range(4):
        x = x0 + (n + 0.5) * L / 4
        c.text(x, y + 250, '腹点：晃得最厉害', 'sans', 22, mix(BG, NRED, fade(t, 12, 13)), 'mm')
    c.text(960, y + 380, '黄点：节点，一直不动', 'sans', 24, mix(BG, SPARK, fade(t, 9, 10)), 'mm')
    caps(c, t, [(0, 4, '一列波往右走，一列波往左走'),
                (4.2, 9, '叠在一起，波形不再前进，只在原地上下抖：这叫驻波'),
                (9.2, 22, '有的地方一直不动（节点），有的地方晃得最厉害（腹点）')], y=1010)

def b9_basin(c, t, i):
    corner_tag(c, 'B9 · 鱼洗')
    c.text(60, 96, '搓盆耳，水为什么在四个地方喷起来？', 'serif', 40, INK)
    cx, cy, R = 700, 560, 300
    a = fade(t, 2, 4)
    amp = 22 * a * math.sin(t * 12)
    pts = []
    for k in range(121):
        th = k / 120 * 2 * math.pi
        r = R + amp * math.cos(2 * th)
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    c.poly(pts, mix(BG, BRONZE, 0.9))
    inner = [(cx + (x - cx) * 0.9, cy + (y - cy) * 0.9) for x, y in pts]
    c.poly(inner, mix(BG, FIELD, 0.35))
    # handles at left/right
    for s in (-1, 1):
        c.rect(cx + s * (R + 10) - 20, cy - 50, cx + s * (R + 10) + 20, cy + 50, fill=BRONZE, r=8)
    c.text(cx, cy + R + 60, '湿手搓两只盆耳', 'sans', 26, MUTED, 'mm')
    # antinodes: 0, 90, 180, 270 deg; nodes at 45 deg
    sp = fade(t, 8, 10)
    R2 = random.Random(int(t * 10))
    for j in range(4):
        th = j * math.pi / 2
        ax, ay = cx + R * 0.82 * math.cos(th), cy + R * 0.82 * math.sin(th)
        c.ellipse(ax, ay, 12, 12, fill=mix(BG, NRED, a))
        if sp > 0:
            for d in range(8):
                ox, oy = R2.uniform(-30, 30), R2.uniform(-60, 0) * sp
                c.ellipse(ax + ox, ay + oy - 20 * sp, 6, 6, fill=mix(BG, FIELD, sp))
    for j in range(4):
        th = j * math.pi / 2 + math.pi / 4
        c.ellipse(cx + R * 0.82 * math.cos(th), cy + R * 0.82 * math.sin(th), 10, 10, fill=SPARK)
    c.text(1180, 300, '盆壁变成椭圆、再变回来：', 'sans', 28, INK, 'lm')
    c.text(1180, 350, '每秒上百次', 'bold', 30, INK, 'lm')
    c.text(1180, 430, '红点：腹点，盆壁动得最厉害', 'sans', 26, NRED, 'lm')
    c.text(1180, 480, '黄点：节点，几乎不动', 'sans', 26, SPARK, 'lm')
    b = fade(t, 14, 15)
    c.text(1180, 580, '腹点旁边的水被拍得最狠，', 'sans', 28, mix(BG, FIELD, b), 'lm')
    c.text(1180, 630, '喷起水花', 'bold', 30, mix(BG, FIELD, b), 'lm')
    c.text(1180, 720, '盆底四条鱼的嘴，正对着这四个地方', 'sans', 26, mix(BG, COPPER, b), 'lm')
    caps(c, t, [(0, 6, '湿手搓盆耳，摩擦一停一滑，像拉琴一样让盆壁振动起来'),
                (6.2, 14, '盆壁上形成驻波：四个地方动得最厉害，四个地方几乎不动'),
                (14.2, 22, '动得最厉害的地方把水拍起来：盆底的鱼嘴正对着它们')], y=1010)

CLIPS = {
 'E45_等时性': (e45_isochron, 22), 'E45_擒纵': (e45_escapement, 22),
 'E45_片头': (titles.opening(SER6, VOL6, S6A, 0, '穿越北宋 · 让钟走得准'), 7),
 'E45_片尾': (titles.closing(SER6, VOL6, S6A, 0, '下集：同一口钟，敲两个地方为什么音不同？'), 7),
 'B11_两种振动': (b11_modes, 22), 'B11_余音': (b11_decay, 22),
 'B11_片头': (titles.opening(BSER, BVOL, SB6, 0, '战国 · 公元前 433 年 · 曾侯乙编钟'), 7),
 'B11_片尾': (titles.closing(BSER, BVOL, SB6, 0, '下集：搓一搓盆耳，水为什么会喷起来？'), 7),
 'B9_驻波': (b9_standing, 22), 'B9_鱼洗': (b9_basin, 22),
 'B9_片头': (titles.opening(BSER, BVOL, SB6, 1, '古代 · 铜鱼洗（起源年代待核）'), 7),
 'B9_片尾': (titles.closing(BSER, BVOL, SB6, 1, '下集：温度计上的「一度」是怎么来的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
