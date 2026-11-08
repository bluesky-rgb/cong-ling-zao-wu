"""第二十七季（第十层：新材料）第三批：E148 不粘锅、E149 纸尿裤、E150 复合材料 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s27a import S27A, SER27, VOL27, CHAIN, WATER_L

WATER = (90, 150, 220)
PAPER = (235, 225, 205)
GEL = (180, 220, 240)
NA = (240, 200, 90)


def _drop(c, x, base, angle_deg, vol=1.0, col=WATER_L):
    """在 base 线上画一个接触角为 angle 的水珠（圆弧截面）。"""
    th = math.radians(max(5, min(175, angle_deg)))
    area = 9000 * vol
    # 圆弧截面面积 = R^2 (th - sin th cos th)
    R = math.sqrt(area / (th - math.sin(th) * math.cos(th)))
    a = R * math.sin(th)
    cy = base + R * math.cos(th)
    pts = []
    for k in range(61):
        phi = -math.pi / 2 - th + 2 * th * k / 60
        pts.append((x + R * math.cos(phi), cy + R * math.sin(phi)))
    c.poly(pts + [(x + a, base), (x - a, base)], col)
    return a, R, cy


# ---------------------------------------------------------------- E148 不粘锅
def e148_angle(c, t, i):
    corner_tag(c, '第 148 集 · 水珠鼓不鼓，看表面亲不亲水')
    c.text(60, 96, '同样一滴水：在玻璃上摊成一片，在蜡纸上鼓成小包，在不粘锅和荷叶上几乎缩成小球', 'serif', 38, INK)
    surfs = [('玻璃', 25, (200, 220, 230)), ('铝箔', 70, (200, 205, 215)), ('蜡纸', 100, (240, 230, 200)), ('不粘锅', 115, (70, 70, 75)), ('荷叶', 150, (110, 170, 110))]
    grow = min(1, t / 6)
    for k, (nm, ang, col) in enumerate(surfs):
        x = 220 + k * 370
        base = 560
        c.rect(x - 160, base, x + 160, base + 40, fill=col, r=4)
        a_now = 90 + (ang - 90) * grow
        _drop(c, x, base, a_now)
        c.text(x, base + 90, nm, 'bold', 26, INK, 'mm')
        c.text(x, base + 140, f'约 {ang}°', 'mono', 22, MUTED, 'mm')
    c.rect(220, 780, 1700, 900, fill=SHEET, r=12)
    c.text(960, 820, '接触角：水珠边缘和表面的夹角（数值为示意，以实测为准）', 'sans', 22, INK, 'mm')
    c.text(960, 865, '小于 90°：亲水，摊开   ·   大于 90°：疏水，鼓起   ·   大于 150°：几乎是个球', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '水分子之间互相拉着；表面要是也「喜欢」水，水就被拉开摊平，比如干净的玻璃'),
                (7.2, 14, '表面要是「不喜欢」水，水分子宁可自己抱成一团：水珠就鼓起来'),
                (14.2, 22, '不粘锅涂的那层材料，几乎谁都不爱粘：水珠、油和鸡蛋都很难在上面抓牢（示意）')], y=1010)


def e148_roll(c, t, i):
    corner_tag(c, '第 148 集 · 斜一点，谁先滚走')
    c.text(60, 96, '把板子斜过来：亲水的表面把水珠「拖住」，摊着不动；疏水的表面抓不住，水珠一下就滚了下去', 'serif', 38, INK)
    tilt = min(30, t * 4)
    r = math.radians(tilt)
    for row, (nm, ang, col, mobile) in enumerate((('玻璃', 30, (200, 220, 230), False), ('不粘锅', 115, (70, 70, 75), True))):
        ox, oy = 360, 280 + row * 240
        L = 760
        ex, ey = ox + L * math.cos(r), oy + L * math.sin(r)
        c.line([(ox, oy), (ex, ey)], col, 18)
        c.text(ox - 40, oy, nm, 'bold', 26, INK, 'rm')
        s = 120
        if mobile and tilt > 8:
            s = 120 + 0.5 * 600 * ((t - 2) ** 2) * 0.12
            s = min(s, L - 80)
        px, py = ox + s * math.cos(r), oy + s * math.sin(r)
        nx, ny = math.sin(r), -math.cos(r)
        if mobile:
            c.ellipse(px + nx * 34, py + ny * 34, 34, 32, fill=WATER_L)
        else:
            c.ellipse(px + 30 * math.cos(r) + nx * 12, py + 30 * math.sin(r) + ny * 12, 70, 14, fill=WATER_L)
        c.text(ex + 40, ey, '滚走了' if (mobile and s > 600) else ('还摊在原地' if not mobile else ''), 'bold', 24, GREEN if mobile else NRED, 'lm')
    c.text(960, 220, f'倾斜 {tilt:.0f}°', 'mono', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '把同样的水珠滴在玻璃和冷的不粘锅上，再把它们慢慢斜过来'),
                (7.2, 14, '玻璃上的水珠被表面拖着，摊得扁扁的，斜到 30° 还赖着不走'),
                (14.2, 22, '不粘锅上的水珠和表面接触得很少，抓不住，一斜就滚下去：煎蛋也是一样的道理（示意，只用冷锅）')], y=1010)


# ---------------------------------------------------------------- E149 纸尿裤
def _net(c, cx, cy, scale, col, seed=3, n=6):
    rnd = random.Random(seed)
    nodes = []
    for a in range(n):
        for b in range(n):
            nodes.append((cx + (a - (n - 1) / 2) * 60 * scale + rnd.uniform(-8, 8) * scale, cy + (b - (n - 1) / 2) * 60 * scale + rnd.uniform(-8, 8) * scale))
    for a in range(n):
        for b in range(n):
            p = nodes[a * n + b]
            if a + 1 < n:
                q = nodes[(a + 1) * n + b]
                mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 + 10 * scale * math.sin(a + b))
                c.line([p, mid, q], col, 3)
            if b + 1 < n:
                q = nodes[a * n + b + 1]
                mid = ((p[0] + q[0]) / 2 + 10 * scale * math.cos(a * b), (p[1] + q[1]) / 2)
                c.line([p, mid, q], col, 3)
    for p in nodes:
        c.ellipse(p[0], p[1], 5, 5, fill=SPARK)
    return nodes


def e149_swell(c, t, i):
    corner_tag(c, '第 149 集 · 分子网吸水，撑开了就挤不出来')
    c.text(60, 96, '颗粒是一张卷得很紧的分子网：网上带着很多电荷，拼命把水分子拉进来，网被撑大，水就被锁在网眼里', 'serif', 36, INK)
    sw = min(1, max(0, (t - 3) / 12))
    scale = 0.45 + 1.15 * sw
    cx, cy = 760, 560
    nodes = _net(c, cx, cy, scale, CHAIN[0])
    rnd = random.Random(8)
    nin = int(140 * sw)
    span = 150 * scale
    for k in range(nin):
        x = cx + rnd.uniform(-span, span)
        y = cy + rnd.uniform(-span, span)
        c.ellipse(x, y, 6, 6, fill=WATER_L)
    for k in range(30):
        a = k * 0.6 + t
        rr = 420 + 30 * math.sin(t + k)
        x, y = cx + rr * math.cos(a) * (1 - sw * 0.3), cy + rr * math.sin(a) * 0.7
        c.ellipse(x, y, 6, 6, fill=mix(BG, WATER_L, 1 - sw * 0.7))
    c.rect(1360, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1610, 340, '1 克颗粒', 'bold', 24, INK, 'mm')
    c.text(1610, 420, f'吸了约 {int(sw * 200)} 毫升清水', 'mono', 26, SPARK, 'mm')
    c.text(1610, 490, '（数值以实测为准）', 'sans', 18, MUTED, 'mm')
    c.text(1610, 580, '用力挤：几乎不出水', 'bold', 22, GREEN if sw > 0.9 else MUTED, 'mm')
    caps(c, t, [(0, 7, '纸尿裤里那一小撮白色颗粒，叫高吸水树脂：它是一张长链连成的立体网，平时卷得紧紧的'),
                (7.2, 14, '网上挂着很多带电的小基团，水一来，就拼命把水分子拉进网里，网被一点点撑大'),
                (14.2, 22, '撑开的网变成一团凝胶，水被锁在网眼里，用手挤也很难挤出来：一克能吸几百克清水（示意）')], y=1010)


def e149_salt(c, t, i):
    corner_tag(c, '第 149 集 · 盐水，吸得少多了')
    c.text(60, 96, '网把水拉进来，靠的是「里面浓、外面淡」；外面的水里已经有很多盐，里外差得少了，网就撑不开那么大', 'serif', 36, INK)
    sw = min(1, max(0, (t - 3) / 10))
    for col_i, (lab, maxs, ml, salty) in enumerate((('清水', 1.6, 200, False), ('盐水', 0.75, 40, True))):
        cx = 480 + col_i * 840
        c.text(cx, 230, lab, 'bold', 28, INK, 'mm')
        sc = 0.45 + (maxs - 0.45) * sw
        _net(c, cx, 560, sc, CHAIN[0], seed=4 + col_i, n=5)
        if salty:
            rnd = random.Random(2)
            for k in range(40):
                x = cx + rnd.uniform(-330, 330)
                y = 560 + rnd.uniform(-280, 280)
                c.ellipse(x, y, 5, 5, fill=NA)
        c.rect(cx - 200, 880, cx - 200 + 400 * (ml / 200) * sw, 920, fill=WATER, r=6)
        c.text(cx, 950, f'约 {int(ml * sw)} 毫升 / 克（示意）', 'mono', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同样 1 克颗粒，一杯加清水，一杯加盐水，一勺勺加到不再吸为止'),
                (7.2, 14, '清水那杯吸成一大团凝胶；盐水那杯很快就吸不动了，只有小小一团'),
                (14.2, 22, '盐里的小颗粒让网外面也「浓」了，水不那么想往里钻：尿里有盐，所以纸尿裤要多放颗粒（倍数以实测为准）')], y=1010)


# ---------------------------------------------------------------- E150 复合材料
def e150_sandwich(c, t, i):
    corner_tag(c, '第 150 集 · 上面压、下面拉，中间撑开')
    c.text(60, 96, '板子一弯，上表面被挤短、下表面被拉长，中间几乎不受力；把两张薄皮用轻芯撑开，就又轻又硬', 'serif', 38, INK)
    load = 0.5 - 0.5 * math.cos(t / 11 * 2 * math.pi)
    for row, (lab, gap, sag) in enumerate((('一张纸', 0, 1.0), ('夹心板：两张纸 + 瓦楞芯', 60, 0.08))):
        y0 = 360 + row * 330
        x0, x1 = 300, 1400
        c.rect(x0 - 80, y0 + 20, x0, y0 + 160, fill=(120, 110, 100))
        c.rect(x1, y0 + 20, x1 + 80, y0 + 160, fill=(120, 110, 100))
        c.text(x0 - 120, y0 - 60, lab, 'bold', 24, INK, 'lm')
        def ycurve(u, off):
            return y0 + off + 140 * sag * load * math.sin(math.pi * u)
        top = [(x0 + (x1 - x0) * k / 40, ycurve(k / 40, 0)) for k in range(41)]
        bot = [(x0 + (x1 - x0) * k / 40, ycurve(k / 40, gap + 6)) for k in range(41)]
        c.line(top, PAPER, 6)
        if gap:
            c.line(bot, PAPER, 6)
            pts = []
            for k in range(81):
                u = k / 80
                pts.append((x0 + (x1 - x0) * u, ycurve(u, 3 + (gap) * (0.5 + 0.5 * math.sin(k * 1.2)))))
            c.line(pts, mix(PAPER, BG, 0.3), 3)
        mid = (x0 + x1) / 2
        my = ycurve(0.5, 0)
        c.rect(mid - 50, my - 70, mid + 50, my - 6, fill=(150, 150, 160), r=6)
        if load > 0.4:
            c.arrow(mid - 200, my - 20, mid - 120, my - 20, (240, 170, 110), 3, 10)
            c.arrow(mid + 200, my - 20, mid + 120, my - 20, (240, 170, 110), 3, 10)
            c.text(mid + 230, my - 20, '压', 'bold', 20, (240, 170, 110), 'lm')
            yb = ycurve(0.5, gap + 6) + 24
            c.arrow(mid - 120, yb, mid - 200, yb, (120, 180, 240), 3, 10)
            c.arrow(mid + 120, yb, mid + 200, yb, (120, 180, 240), 3, 10)
            c.text(mid + 230, yb, '拉', 'bold', 20, (120, 180, 240), 'lm')
    caps(c, t, [(0, 7, '一张纸架在两摞书之间，放一点东西就弯下去了：它太薄'),
                (7.2, 14, '板子一弯，最吃力的是上下两个表面，一个被压，一个被拉；中间几乎闲着'),
                (14.2, 22, '所以用两张薄皮当表面，中间夹一层轻轻的芯把它们撑开：重量没多多少，硬了很多倍（示意）')], y=1010)


def e150_load(c, t, i):
    corner_tag(c, '第 150 集 · 三张纸，三种结构')
    c.text(60, 96, '一样的三张 A4 纸：平放、卷成纸管、做成瓦楞夹心板，看谁撑得住最多的书', 'serif', 38, INK)
    data = [('平放', 1, (200, 200, 200)), ('6 根纸管', 12, (240, 170, 110)), ('瓦楞夹心', 30, GREEN)]
    gx0, gy0 = 300, 860
    c.line([(gx0, gy0), (1500, gy0)], LINE, 2)
    grow = min(1, t / 12)
    for k, (nm, v, col) in enumerate(data):
        x = gx0 + 120 + k * 380
        h = 560 * v / 30 * grow
        c.rect(x, gy0 - h, x + 200, gy0, fill=col, r=8)
        c.text(x + 100, gy0 + 40, nm, 'bold', 24, INK, 'mm')
        c.text(x + 100, gy0 - h - 30, f'× {v * grow:.0f}', 'mono', 26, INK, 'mm')
    c.rect(1560, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1710, 340, '重量', 'bold', 24, INK, 'mm')
    c.text(1710, 400, '三种都差不多', 'sans', 22, INK, 'mm')
    c.text(1710, 470, '能承重', 'bold', 24, INK, 'mm')
    c.text(1710, 530, '差了几十倍', 'sans', 22, SPARK, 'mm')
    c.text(1710, 620, '（倍数为示意，', 'sans', 18, MUTED, 'mm')
    c.text(1710, 650, '以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '材料一点没多：都是一张 A4 纸，只是摆法不一样'),
                (7.2, 14, '卷成管、做成夹心，就把纸「撑开」了，弯的时候上下表面离得更远，更难弯'),
                (14.2, 22, '飞机、赛车、自行车用的碳纤维复合材料也是这样：很强的细纤维当表面，轻的芯和树脂把它们撑开、粘住')], y=1010)


CLIPS = {
 'E148_接触角': (e148_angle, 22), 'E148_滚走': (e148_roll, 22),
 'E148_片头': (titles.opening(SER27, VOL27, S27A, 6, '1938 年普朗克特意外发现聚四氟乙烯'), 7),
 'E148_片尾': (titles.closing(SER27, VOL27, S27A, 6, '下集：一小撮白色颗粒，为什么能吸进几百倍重的水？'), 7),
 'E149_分子网': (e149_swell, 22), 'E149_盐水': (e149_salt, 22),
 'E149_片头': (titles.opening(SER27, VOL27, S27A, 7, '1980 年代高吸水树脂用于纸尿裤'), 7),
 'E149_片尾': (titles.closing(SER27, VOL27, S27A, 7, '下集：一张纸一压就弯，为什么做成瓦楞纸板就能站人？'), 7),
 'E150_夹心': (e150_sandwich, 22), 'E150_承重': (e150_load, 22),
 'E150_片头': (titles.opening(SER27, VOL27, S27A, 8, '1960 年代碳纤维问世'), 7),
 'E150_片尾': (titles.closing(SER27, VOL27, S27A, 8, '下集：一块轻得像烟的固体，为什么能挡住喷枪的火？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
