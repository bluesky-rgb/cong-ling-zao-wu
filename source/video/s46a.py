"""第四十六季（古法解密 20.0：量天与行水）第一批：B200 牵星板、B201 天池测雨、B202 悬炭测湿 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB46 = [('B200', '牵星板'), ('B201', '天池测雨'), ('B202', '悬炭测湿'), ('B203', '规矩'), ('B204', '草鞋'),
        ('B205', '秧马'), ('B206', '轿子'), ('B207', '戽斗'), ('B208', '竹篙'), ('B209', '龙舟')]
VOL46 = '第四十六季 · 古法解密 20.0'
SEA = (40, 70, 110)
STAR = (250, 230, 140)
CHAR = (60, 58, 56)
ROD = (170, 120, 70)


# ---------------------------------------------------------------- B200 牵星板
def b200_angle(c, t, i):
    corner_tag(c, 'B200 · 绳长固定，板宽就是角度')
    c.text(60, 96, '绳子把板固定在眼前同样远的地方：板的下沿对着海平线、上沿对着北极星，能刚好对上的板越宽，星星就越高', 'serif', 36, INK)
    ex, ey = 320, 700
    c.rect(0, ey, W, 960, fill=mix(BG, SEA, 0.8))
    c.ellipse(ex, ey - 10, 26, 26, fill=mix(BG, (230, 190, 160), 1.0))
    p = (t % 11) / 11
    sx = 1700
    sy = 520 - 300 * min(1.0, t / 14)
    c.ellipse(sx, sy, 14, 14, fill=STAR)
    c.text(sx + 30, sy, '北极星', 'bold', 24, STAR, 'lm')
    L = 380
    ang = math.atan2(ey - 10 - sy, sx - ex)
    bx = ex + L
    h_need = L * math.tan(ang)
    boards = [60, 120, 180, 240]
    best = min(boards, key=lambda b: abs(b - h_need))
    for k, b in enumerate(boards):
        x = bx + k * 26
        on = b == best
        c.rect(x - 8, ey - 10 - b, x + 8, ey - 10, fill=mix(BG, ROD, 1.0 if on else 0.35), r=3)
    c.line([(ex, ey - 10), (bx, ey - 10)], mix(BG, MUTED, 0.9), 2)
    c.text((ex + bx) / 2, ey + 30, '绳长固定', 'sans', 22, MUTED, 'mm')
    c.line([(ex, ey - 10), (sx, sy)], mix(BG, STAR, 0.5), 2)
    c.line([(ex, ey - 10), (sx, ey - 10)], mix(BG, STAR, 0.3), 2)
    c.text(1200, 240, f'星高约 {math.degrees(ang):.0f}°：用第 {boards.index(best) + 1} 块板（示意）', 'bold', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '牵星板是一套大小不同的木板，中间穿一根长度固定的绳子，绳头咬在嘴里'),
                (7.2, 14, '眼睛到板的距离不变，板越宽，从下沿到上沿张开的角度就越大'),
                (14.2, 22, '哪块板刚好盖住海平线到北极星，星星就有那么高（示意，不对着太阳量）')], y=1010)


def b200_latitude(c, t, i):
    corner_tag(c, 'B200 · 越往北，北极星越高')
    c.text(60, 96, '北极星几乎正对地轴：在赤道上它贴着海平线，越往北越高，到北极就在头顶；量出它多高，就知道船在多北', 'serif', 36, INK)
    cx, cy, R = 700, 600, 260
    c.ellipse(cx, cy, R, R, fill=mix(BG, (60, 110, 170), 0.9))
    c.line([(cx, cy - R - 110), (cx, cy + R + 40)], mix(BG, MUTED, 0.6), 2)
    c.text(cx + 14, cy - R - 95, '地轴 → 指向北极星', 'sans', 20, MUTED, 'lm')
    lat = math.radians(10 + 60 * (0.5 - 0.5 * math.cos(t * 0.35)))
    px, py = cx + R * math.cos(lat), cy - R * math.sin(lat)
    c.ellipse(px, py, 16, 16, fill=SPARK)
    hx, hy = -math.sin(lat), -math.cos(lat)
    c.line([(px - 160 * hx, py - 160 * hy), (px + 160 * hx, py + 160 * hy)], mix(BG, SEA, 1.0), 4)
    c.line([(px, py), (px, py - 180)], STAR, 3)
    c.text(px + 40, py - 120, f'北极星高 ≈ {math.degrees(lat):.0f}°', 'bold', 26, STAR, 'lm')
    c.text(1500, 380, '北纬多少度\n≈ 北极星离海平线多高', 'bold', 30, INK, 'mm')
    c.text(1500, 560, '赤道：0°，贴着海平线\n广州：约 23°\n北京：约 40°\n（以资料为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '地球在转，北极星几乎就在地轴的延长线上，整夜不怎么动'),
                (7.2, 14, '站在越北的地方，地平线越「翘」，北极星就显得越高'),
                (14.2, 22, '所以水手量出北极星的高度，就能算出船在南北方向的位置（示意）')], y=1010)


# ---------------------------------------------------------------- B201 天池测雨
def _rain(c, t, x0, x1, top, bot, n=60, seed=0):
    r = random.Random(seed)
    for k in range(n):
        x = r.uniform(x0, x1)
        y = top + ((t * 500 + r.uniform(0, bot - top)) % (bot - top))
        c.line([(x, y), (x - 4, y + 18)], mix(BG, WATER_L, 0.8), 2)


def b201_shapes(c, t, i):
    corner_tag(c, 'B201 · 只有直筒的水深才是雨量')
    c.text(60, 96, '雨量是平地上积水的深度：同一场雨，直筒接到的深度就是雨量；口大底小的盆接得宽、装得窄，水深偏大', 'serif', 36, INK)
    _rain(c, t, 120, 1800, 200, 520, 80, 3)
    p = min(1.0, t / 14)
    gy = 860
    c.rect(100, gy, 1820, gy + 14, fill=mix(BG, MUTED, 0.5))
    rain = 60 * p
    # 直筒
    x = 400
    c.rect(x - 80, 560, x - 74, gy, fill=MUTED)
    c.rect(x + 74, 560, x + 80, gy, fill=MUTED)
    c.rect(x - 74, gy - rain, x + 74, gy, fill=mix(BG, WATER, 0.85))
    c.text(x, gy + 50, f'直筒：{rain / 6:.0f} 毫米', 'bold', 24, GREEN, 'mm')
    # 口大底小
    x = 960
    top_w, bot_w, H = 200, 80, 300
    c.poly([(x - top_w, gy - H), (x - top_w + 6, gy - H), (x - bot_w + 6, gy), (x - bot_w, gy)], MUTED)
    c.poly([(x + top_w, gy - H), (x + top_w - 6, gy - H), (x + bot_w - 6, gy), (x + bot_w, gy)], MUTED)
    vol = rain * (2 * top_w)
    h = 0
    while h < H:
        w = bot_w + (top_w - bot_w) * h / H
        a = (bot_w + w) * h
        if a >= vol:
            break
        h += 1
    w = bot_w + (top_w - bot_w) * h / H
    c.poly([(x - bot_w, gy), (x + bot_w, gy), (x + w, gy - h), (x - w, gy - h)], mix(BG, WATER, 0.85))
    c.text(x, gy + 50, f'口大底小：{h / 6:.0f} 毫米（偏大）', 'bold', 24, NRED, 'mm')
    # 漏斗加细瓶
    x = 1520
    c.poly([(x - 150, 560), (x - 144, 560), (x - 14, 660), (x - 20, 660)], MUTED)
    c.poly([(x + 150, 560), (x + 144, 560), (x + 14, 660), (x + 20, 660)], MUTED)
    c.rect(x - 40, 660, x - 34, gy, fill=MUTED)
    c.rect(x + 34, 660, x + 40, gy, fill=MUTED)
    h2 = min(gy - 670, rain * (300 / 74) * 1.0)
    c.rect(x - 34, gy - h2, x + 34, gy, fill=mix(BG, WATER, 0.85))
    c.text(x, gy + 50, f'漏斗：{h2 / 6:.0f} 毫米（大得多）', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '三个容器并排放着，接同一场「雨」'),
                (7.2, 14, '直筒上下一样粗，接进多深就是多深；口大底小的盆，水挤在窄底里，显得深'),
                (14.2, 22, '漏斗把一大片雨汇进细瓶，水深能大好几倍：直接读都不对（示意）')], y=1010)


def b201_convert(c, t, i):
    corner_tag(c, 'B201 · 用面积换算回来')
    c.text(60, 96, '秦九韶算「天池」：先算盆里积了多少水，再除以盆口面积，才是平地上的雨深；漏斗量雨也这样算', 'serif', 36, INK)
    p = min(1.0, t / 14)
    rows = [('接到的水的体积', '量杯读出：例如 150 毫升', 0.2), ('除以开口面积', '口径 10 厘米 → 面积约 78.5 平方厘米', 0.45), ('= 平地上的雨深', '150 ÷ 78.5 ≈ 1.9 厘米 ≈ 19 毫米（示意）', 0.7)]
    for k, (a, b, th) in enumerate(rows):
        if p < th:
            continue
        y = 330 + k * 180
        c.rect(260, y - 60, 1660, y + 60, fill=SHEET, r=14)
        c.text(320, y, a, 'bold', 32, INK, 'lm')
        c.text(900, y, b, 'sans', 26, MUTED, 'lm')
        if k < 2:
            c.arrow(960, y + 66, 960, y + 110, SPARK, 5, 16)
    caps(c, t, [(0, 7, '把碗和细瓶里的水倒进量杯，读出体积'),
                (7.2, 14, '量出开口直径，算出开口面积：雨是落在整个开口上的'),
                (14.2, 22, '体积除以开口面积，三个容器算出来的雨量就差不多一样了（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B202 悬炭测湿
def b202_pores(c, t, i):
    corner_tag(c, 'B202 · 满身小孔，吸进水汽')
    c.text(60, 96, '木炭是木头烧过留下的骨架，里面全是看不见的小孔，表面积大得惊人：空气潮的时候，水汽钻进孔里粘住，木炭就变重', 'serif', 35, INK)
    cx, cy = 700, 560
    c.rect(cx - 320, cy - 220, cx + 320, cy + 220, fill=mix(BG, CHAR, 1.0), r=20)
    r = random.Random(4)
    pores = [(cx + r.uniform(-290, 290), cy + r.uniform(-190, 190), r.uniform(8, 22)) for _ in range(60)]
    for x, y, s in pores:
        c.ellipse(x, y, s, s, fill=mix(BG, (25, 25, 25), 1.0))
    p = min(1.0, t / 14)
    rr = random.Random(9)
    for k in range(int(70 * p)):
        x, y, s = pores[k % len(pores)]
        c.ellipse(x + rr.uniform(-s / 2, s / 2), y + rr.uniform(-s / 2, s / 2), 4, 4, fill=mix(BG, WATER_L, 1.0))
    r2 = random.Random(int(t * 3))
    for k in range(25):
        x = 1250 + r2.uniform(0, 500)
        y = 260 + r2.uniform(0, 600)
        c.ellipse(x, y, 5, 5, fill=mix(BG, WATER_L, 0.7))
    c.arrow(1220, 560, 1060, 560, mix(BG, WATER_L, 1.0), 5, 16)
    c.text(1500, 900, '潮湿的空气：很多水汽（示意）', 'sans', 22, MUTED, 'mm')
    c.text(cx, cy + 270, f'木炭重量 +{p * 3:.1f}%（示意）', 'bold', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '木炭多孔，一小块里藏着的孔壁摊开来，面积能有好大一片'),
                (7.2, 14, '空气里的水汽碰到孔壁就被粘住，空气越潮，粘住的越多'),
                (14.2, 22, '粘住的水有重量：木炭就悄悄变重了，空气一干又慢慢放出来（示意）')], y=1010)


def b202_balance(c, t, i):
    corner_tag(c, 'B202 · 天平一斜，就知道空气潮了')
    c.text(60, 96, '杆子两头挂木炭和不吸水的砝码，先调平：空气一潮，木炭变重往下沉；空气一干又翘回来，就知道要不要下雨', 'serif', 35, INK)
    cx, cy = 960, 380
    hum = 0.5 - 0.5 * math.cos(t * 0.45)
    tilt = math.radians(9 * hum)
    L = 520
    lx, ly = cx - L * math.cos(tilt), cy + L * math.sin(tilt)
    rx, ry = cx + L * math.cos(tilt), cy - L * math.sin(tilt)
    c.line([(cx, 200), (cx, cy)], MUTED, 3)
    c.line([(lx, ly), (rx, ry)], mix(BG, ROD, 1.0), 12)
    c.ellipse(cx, cy, 10, 10, fill=INK)
    c.line([(lx, ly), (lx, ly + 140)], MUTED, 2)
    c.rect(lx - 70, ly + 140, lx + 70, ly + 240, fill=mix(BG, CHAR, 1.0), r=14)
    c.text(lx, ly + 280, '木炭', 'bold', 24, INK, 'mm')
    c.line([(rx, ry), (rx, ry + 160)], MUTED, 2)
    c.rect(rx - 40, ry + 160, rx + 40, ry + 220, fill=mix(BG, (170, 175, 185), 1.0), r=8)
    c.text(rx, ry + 260, '不吸水的砝码', 'bold', 24, INK, 'mm')
    c.rect(1500, 700, 1800, 740, fill=SHEET, r=8)
    c.rect(1500, 700, 1500 + 300 * hum, 740, fill=mix(BG, WATER_L, 1.0), r=8)
    c.text(1650, 780, '空气湿度（示意）', 'sans', 22, MUTED, 'mm')
    c.text(cx, 880, '炭那头往下沉：空气变潮了' if hum > 0.5 else '杆子回平：空气变干了', 'bold', 28, SPARK if hum > 0.5 else GREEN, 'mm')
    caps(c, t, [(0, 7, '筷子当杆，一头挂一包木炭，一头挂回形针，增减到筷子水平'),
                (7.2, 14, '放进加了温水的箱子里，空气一潮，木炭吸水变重，那头慢慢沉下去'),
                (14.2, 22, '换成硅胶干燥剂，空气变干，木炭放出水汽，筷子又翘回来（以实测为准）')], y=1010)


CLIPS = {
 'B200_角度': (b200_angle, 22), 'B200_纬度': (b200_latitude, 22),
 'B200_片头': (titles.opening(BSER, VOL46, SB46, 0, '明代郑和船队用牵星板量星'), 7),
 'B200_片尾': (titles.closing(BSER, VOL46, SB46, 0, '下集：一场雨到底下了多少？'), 7),
 'B201_直筒': (b201_shapes, 22), 'B201_换算': (b201_convert, 22),
 'B201_片头': (titles.opening(BSER, VOL46, SB46, 1, '南宋秦九韶《数书九章》有「天池测雨」'), 7),
 'B201_片尾': (titles.closing(BSER, VOL46, SB46, 1, '下集：空气潮不潮，怎么用一块木炭称出来？'), 7),
 'B202_吸湿': (b202_pores, 22), 'B202_天平': (b202_balance, 22),
 'B202_片头': (titles.opening(BSER, VOL46, SB46, 2, '西汉《淮南子》记载用炭的轻重判断燥湿'), 7),
 'B202_片尾': (titles.closing(BSER, VOL46, SB46, 2, '下集：「规」和「矩」到底是什么工具？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
