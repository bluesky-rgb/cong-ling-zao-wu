"""第四十五季（第十九层：玩具箱）第一批：E232 溜溜球、E233 弹力球、E234 万花筒 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S45A = [('232', '溜溜球'), ('233', '弹力球'), ('234', '万花筒'), ('235', '泡泡'), ('236', '史莱姆'),
        ('237', '积木'), ('238', '遥控车'), ('239', '磁力片'), ('240', '回力车'), ('241', '八音盒')]
SER45, VOL45 = '从零造物', '第四十五季 · 第十九层：玩具箱'
YOYO = (220, 70, 70)
BALL = (240, 120, 160)
PING = (245, 240, 230)
CLAY = (160, 140, 110)
MIRROR = (190, 205, 220)
GEMS = [(230, 80, 80), (80, 170, 90), (70, 120, 220), (240, 200, 60)]


# ---------------------------------------------------------------- E232 溜溜球
def e232_fall(c, t, i):
    corner_tag(c, '第 232 集 · 高度换成转动，转动再卷回去')
    c.text(60, 96, '往下落时绳子放开，它越转越快，高度变成转动；到底后「睡」着空转，手一抖，转动又把绳子卷回去', 'serif', 36, INK)
    T = 10.0
    ph = (t % T) / T
    top, bot = 220, 760
    if ph < 0.4:
        u = (ph / 0.4) ** 2
        y = top + (bot - top) * u
        spin = 40 * u
        lab = '往下落：越转越快'
    elif ph < 0.7:
        y = bot
        spin = 40 * (1 - 0.3 * (ph - 0.4) / 0.3)
        lab = '到底：「睡」着空转'
    else:
        u = (ph - 0.7) / 0.3
        y = bot - (bot - top) * (1 - (1 - u) ** 2)
        spin = 28 * (1 - u)
        lab = '手一抖：卷回手里'
    cx = 700
    c.line([(cx, 210), (cx, y - 70)], mix(BG, INK, 0.8), 3)
    c.ellipse(cx, 200, 26, 18, fill=mix(BG, (230, 190, 160), 1.0))
    c.ellipse(cx, y, 70, 70, fill=mix(BG, YOYO, 1.0))
    a = t * spin * 0.3
    for k in range(3):
        aa = a + k * 2.094
        c.line([(cx, y), (cx + 60 * math.cos(aa), y + 60 * math.sin(aa))], BG, 5)
    c.ellipse(cx, y, 10, 10, fill=INK)
    c.text(cx + 140, y, lab, 'bold', 28, SPARK, 'lm')
    bx = 1500
    h_e = (bot - y) / (bot - top)
    r_e = spin / 40
    for k, (nm, v, col) in enumerate([('高度能', h_e, GREEN), ('转动能', r_e, SPARK)]):
        x = bx + k * 140
        c.rect(x, 300, x + 80, 760, fill=SHEET, r=8)
        c.rect(x, 760 - 460 * max(0.0, min(1.0, v)), x + 80, 760, fill=col, r=8)
        c.text(x + 40, 800, nm, 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '绳子一头松松地套在轴上，溜溜球一落，绳子放开，它就转起来'),
                (7.2, 14, '落到底，绳子松着，轴在绳圈里打滑，溜溜球只转不走：这叫「睡眠」'),
                (14.2, 22, '手一抖，绳子咬住轴，转动把它一圈圈卷回来；摩擦慢慢吃掉能量（示意）')], y=1010)


def e232_rim(c, t, i):
    corner_tag(c, '第 232 集 · 重量放在外圈，转得更久')
    c.text(60, 96, '同样的重量，靠近轴容易转快也容易停；放在外圈，转起来费劲，可一旦转起来也停得慢：这叫转动惯量', 'serif', 36, INK)
    for j, (lab, rim) in enumerate([('硬币靠近轴：转得快，停得也快', False), ('硬币放外圈：转得稳，睡得更久', True)]):
        cx, cy = 480 + j * 960, 520
        R = 220
        decay = math.exp(-t * (0.35 if not rim else 0.12))
        a = (t * 8 * decay) * (1.2 if not rim else 0.8)
        c.ellipse(cx, cy, R, R, fill=mix(BG, YOYO, 0.9))
        c.ellipse(cx, cy, 18, 18, fill=INK)
        rr = 60 if not rim else 190
        for k in range(4):
            aa = a + k * math.pi / 2
            c.ellipse(cx + rr * math.cos(aa), cy + rr * math.sin(aa), 26, 26, fill=mix(BG, (230, 200, 90), 1.0))
        c.rect(cx - 200, 800, cx - 200 + 400 * decay, 830, fill=GREEN if rim else NRED, r=6)
        c.text(cx, 870, lab, 'bold', 24, GREEN if rim else NRED, 'mm')
    c.text(960, 940, '下方横条：还剩多少转动（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '在两个瓶盖做的溜溜球上各粘 4 枚硬币：一个粘在中心旁，一个粘在外圈'),
                (7.2, 14, '外圈的那个落得慢一点，可到底后能在下面「睡」更久'),
                (14.2, 22, '重量离轴越远，转动越难改变：花样溜溜球的重量都集中在外圈（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E233 弹力球
def e233_bounce(c, t, i):
    corner_tag(c, '第 233 集 · 压扁了，还回来多少')
    c.text(60, 96, '球落地被压扁，把能量存成形变：弹性好的几乎全还回来，弹得高；橡皮泥压扁不回弹，能量变成了热', 'serif', 36, INK)
    gy = 820
    c.rect(100, gy, 1820, gy + 20, fill=mix(BG, MUTED, 0.6))
    for k in range(6):
        y = gy - k * 100
        c.line([(120, y), (150, y)], MUTED, 2)
        c.text(160, y, f'{k * 20}', 'mono', 16, MUTED, 'lm')
    H = 500
    for k, (lab, e, col, r) in enumerate([('弹力球', 0.88, BALL, 40), ('乒乓球', 0.75, PING, 36), ('网球', 0.6, (210, 230, 80), 44), ('橡皮泥', 0.0, CLAY, 40)]):
        x = 420 + k * 360
        hh = H
        tt = t % 9
        y = gy - r
        tf = 1.2
        cur = 0.0
        h = hh
        while True:
            seg_t = tf if cur == 0 else 2 * tf * math.sqrt(h / hh)
            if tt < seg_t or h < 4:
                break
            tt -= seg_t
            cur += 1
            h = h * e * e if cur == 1 else h * e * e
        if h < 4 or (e == 0 and cur >= 1):
            y = gy - r
            squash = 1.0 if e > 0 else 0.45
        else:
            if cur == 0:
                u = tt / tf
                y = gy - r - hh * (1 - u * u)
            else:
                half = tf * math.sqrt(h / hh)
                u = (tt - half) / half
                y = gy - r - h * (1 - u * u)
            squash = 1.0
        c.ellipse(x, y + (r * (1 - squash) if squash < 1 else 0), r / squash ** 0.5, r * squash, fill=mix(BG, col, 1.0))
        c.text(x, gy + 60, lab, 'bold', 24, INK, 'mm')
        c.text(x, gy + 100, f'弹回约 {int(e * e * 100)}%', 'mono', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '四个球从同一高度松手，用手机慢动作拍贴在墙上的尺子'),
                (7.2, 14, '弹力球几乎弹回原来的高度，乒乓球、网球低一些，橡皮泥一下就瘫在地上'),
                (14.2, 22, '弹回高度和落下高度的比，说明球把多少能量「还」了回来（数值示意，以实测为准）')], y=1010)


def e233_stack(c, t, i):
    corner_tag(c, '第 233 集 · 叠在一起落，上面的飞得高')
    c.text(60, 96, '小弹力球叠在网球上一起松手：网球先着地弹起，迎面撞上还在下落的小球，把一大份能量传给它，小球就飞得很高', 'serif', 35, INK)
    gy = 860
    c.rect(100, gy, 1820, gy + 20, fill=mix(BG, MUTED, 0.6))
    T = 8.0
    ph = (t % T)
    cx = 960
    h0 = 300
    tf = 1.0
    if ph < tf:
        u = ph / tf
        yb = gy - 50 - h0 * (1 - u * u)
        ys = yb - 50 - 30
        hit = False
    else:
        u = ph - tf
        yb = gy - 50 - min(150, 300 * u - 300 * u * u) if u < 1 else gy - 50
        ys = gy - 130 - (1100 * u - 260 * u * u) if u < 2.2 else gy - 130
        ys = max(250, ys)
        hit = u < 0.15
    c.ellipse(cx, yb, 50, 50, fill=mix(BG, (210, 230, 80), 1.0))
    c.ellipse(cx, ys, 28, 28, fill=mix(BG, BALL, 1.0))
    c.line([(cx - 300, gy - 50 - h0 - 80), (cx - 260, gy - 50 - h0 - 80)], MUTED, 2)
    c.text(cx - 320, gy - 50 - h0 - 80, '松手高度', 'sans', 20, MUTED, 'rm')
    if hit:
        c.text(cx + 120, gy - 140, '撞！', 'bold', 34, SPARK, 'lm')
    c.text(cx + 300, 300, '小球飞得比松手处高很多（示意）', 'bold', 26, GREEN, 'lm')
    caps(c, t, [(0, 7, '网球在下、弹力球在上，从 50 厘米高一起松手'),
                (7.2, 14, '网球先碰地弹起，迎面撞上还在往下掉的弹力球'),
                (14.2, 22, '大球把一大份能量传给小球，小球飞得很高：在室外空地做，别对着人和窗户')], y=1010)


# ---------------------------------------------------------------- E234 万花筒
def _wedge_images(c, cx, cy, deg, gx, gy_, col, R=320):
    n = int(round(360 / deg))
    base_a = math.atan2(gy_ - cy, gx - cx)
    d = math.hypot(gx - cx, gy_ - cy)
    ang0 = math.radians(deg)
    for k in range(n):
        if k % 2 == 0:
            a = base_a + (k // 2) * 2 * ang0
        else:
            a = -base_a + ((k + 1) // 2) * 2 * ang0 - 0
        x, y = cx + d * math.cos(a), cy + d * math.sin(a)
        c.ellipse(x, y, 16, 16, fill=mix(BG, col, 1.0 if k == 0 else 0.7))
    return n


def e234_angle(c, t, i):
    corner_tag(c, '第 234 集 · 360° ÷ 夹角 = 份数')
    c.text(60, 96, '两面镜子立成一个角，里面放一颗珠子：光在镜子间来回反射，一颗被复制成一圈；夹角越小，份数越多', 'serif', 36, INK)
    for k, deg in enumerate([90, 60, 45]):
        cx, cy = 340 + k * 620, 560
        R = 260
        c.ellipse(cx, cy, R, R, outline=mix(BG, MUTED, 0.3), width=2)
        for s in (0, deg):
            a = math.radians(-s)
            c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], mix(BG, MIRROR, 1.0), 10)
        mid = math.radians(-deg * 0.35)
        gx, gy_ = cx + 150 * math.cos(mid), cy + 150 * math.sin(mid)
        p = min(1.0, max(0.0, (t - 2) / 8))
        n = int(round(360 / deg))
        shown = max(1, int(1 + (n - 1) * p))
        base = math.atan2(gy_ - cy, gx - cx)
        for m in range(shown):
            if m % 2 == 0:
                a = base - (m // 2) * 2 * math.radians(deg)
            else:
                a = -base - 2 * math.radians(deg) * ((m + 1) // 2) + 2 * math.radians(deg)
                a = -(base) + 2 * math.radians(-deg) * ((m - 1) // 2) + 2 * math.radians(-deg) * 0
                a = 2 * math.radians(-deg) * ((m + 1) // 2) - base
            x, y = cx + 150 * math.cos(a), cy + 150 * math.sin(a)
            c.ellipse(x, y, 18, 18, fill=mix(BG, GEMS[0], 1.0 if m == 0 else 0.6))
        c.text(cx, cy + R + 50, f'{deg}°：看到 {n} 颗', 'bold', 28, SPARK, 'mm')
    c.text(960, 940, '亮色：真的那颗；淡色：镜子里的像（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '两条镜面卡纸连成一本能开合的「书」，在夹角里放一颗珠子'),
                (7.2, 14, '90° 看到 4 颗，60° 看到 6 颗，45° 看到 8 颗：360 除以夹角'),
                (14.2, 22, '每一次反射都多出一个像，像和像之间左右对称，拼成一圈（以实测为准）')], y=1010)


def e234_pattern(c, t, i):
    corner_tag(c, '第 234 集 · 转一转，花就变')
    c.text(60, 96, '三面镜子围成三棱筒，夹角都是 60°：几粒彩片被复制成六瓣对称的花；一转，彩片换位，整朵花跟着变', 'serif', 36, INK)
    cx, cy, R = 960, 560, 340
    rot = t * 0.25
    r = random.Random(7)
    pieces = [(r.uniform(30, 150), r.uniform(0.1, 0.9), GEMS[k % 4], r.uniform(10, 22)) for k in range(7)]
    c.ellipse(cx, cy, R, R, fill=mix(BG, (25, 25, 35), 1.0))
    for k in range(6):
        base = math.radians(60 * k)
        mirror = k % 2 == 1
        for d, f, col, sz in pieces:
            a_local = (f * math.radians(60) + rot * (1 + 0.3 * f)) % math.radians(60)
            if mirror:
                a_local = math.radians(60) - a_local
            a = base + a_local
            x, y = cx + d * 2 * math.cos(a), cy + d * 2 * math.sin(a)
            c.ellipse(x, y, sz, sz, fill=mix(BG, col, 1.0))
    for k in range(3):
        a = math.radians(90 + 120 * k)
        c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], mix(BG, MIRROR, 0.25), 2)
    c.text(cx + R + 60, cy, '六瓣对称\n（示意）', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 7, '筒底只放了几粒彩纸屑，从小孔里看去，却是一整朵对称的花'),
                (7.2, 14, '三面镜子两两成 60°，每一份都被复制成 6 份，相邻两份左右镜像'),
                (14.2, 22, '一转筒，彩纸屑滚到新位置，6 份一起变：同一朵花几乎不会出现第二次')], y=1010)


CLIPS = {
 'E232_下落': (e232_fall, 22), 'E232_外圈': (e232_rim, 22),
 'E232_片头': (titles.opening(SER45, VOL45, S45A, 0, '20 世纪 20 年代美国开始批量生产溜溜球'), 7),
 'E232_片尾': (titles.closing(SER45, VOL45, S45A, 0, '下集：为什么有的球弹得高，有的一点都不弹？'), 7),
 'E233_回弹': (e233_bounce, 22), 'E233_叠球': (e233_stack, 22),
 'E233_片头': (titles.opening(SER45, VOL45, S45A, 1, '20 世纪 60 年代出现高弹性的「超级球」'), 7),
 'E233_片尾': (titles.closing(SER45, VOL45, S45A, 1, '下集：几粒碎彩片，怎么变成一圈对称的花？'), 7),
 'E234_夹角': (e234_angle, 22), 'E234_图案': (e234_pattern, 22),
 'E234_片头': (titles.opening(SER45, VOL45, S45A, 2, '1816 年英国人布鲁斯特发明万花筒'), 7),
 'E234_片尾': (titles.closing(SER45, VOL45, S45A, 2, '下集：清水吹不出泡泡，加了洗洁精为什么就能？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
