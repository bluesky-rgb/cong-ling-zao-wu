"""第二十三季（第八层：大工程）第三批：E128 高铁、E129 潮汐发电、E130 可回收火箭 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s23a import S23A, SER23, VOL23, WATER, WATER_L, CONC, GROUND
from s22a import rot

TRAIN = (225, 228, 235)
STRIPE = (60, 110, 200)
AIRL = (140, 180, 220)
WIRE = (200, 200, 210)
MOTOR = (230, 150, 70)
EARTH = (70, 130, 200)
LAND = (110, 160, 90)
MOON = (210, 210, 200)
OCEAN = (60, 120, 200)
ROCKET = (225, 228, 235)
FLAME = (250, 170, 60)
LEG = (90, 90, 100)


# ---------------------------------------------------------------- E128 高铁
def _streams(c, t, y0, nose, x_nose):
    for k in range(9):
        yy = y0 - 160 + k * 40
        pts = []
        for j in range(61):
            x = 100 + j * 20
            dy = 0.0
            dist = x_nose - x
            if nose == 'blunt':
                if -40 < dist < 200 and abs(yy - y0) < 80:
                    dy = (40 if yy >= y0 else -40) * math.exp(-max(0, dist) / 80)
                wig = 10 * math.sin(x * 0.05 + t * 6) if (dist < 0 and abs(yy - y0) < 120) else 0
            else:
                if dist < 300 and abs(yy - y0) < 100:
                    dy = (yy - y0) * 0.25 * min(1, max(0, (300 - dist) / 300))
                wig = 0
            pts.append((x, yy + dy + wig))
        c.line(pts, mix(BG, AIRL, 0.6), 2)


def e128_nose(c, t, i):
    corner_tag(c, '第 128 集 · 车头为什么是尖的')
    c.text(60, 96, '方车头一头撞上空气，后面乱成一团；尖车头把空气顺顺地分开', 'serif', 40, INK)
    rows = [('方车头', 'blunt', 380, 1.0), ('尖车头', 'sharp', 760, 0.45)]
    for nm, nose, y0, drag in rows:
        x_nose = 800
        _streams(c, t, y0, nose, x_nose)
        if nose == 'blunt':
            c.rect(x_nose, y0 - 70, 1500, y0 + 70, fill=TRAIN, r=10)
        else:
            c.poly([(x_nose - 120, y0 + 50), (x_nose + 160, y0 - 70), (1500, y0 - 70), (1500, y0 + 70), (x_nose - 40, y0 + 70)], TRAIN)
        c.rect(x_nose + 40, y0 + 10, 1500, y0 + 26, fill=STRIPE)
        c.text(1540, y0 - 30, nm, 'bold', 28, INK, 'lm')
        c.text(1540, y0 + 20, '空气阻力', 'sans', 22, MUTED, 'lm')
        c.rect(1540, y0 + 50, 1540 + 300 * drag, y0 + 72, fill=NRED if drag > 0.6 else GREEN)
    c.text(960, 940, '（阻力长短为示意；风从左边吹来，相当于车往左开）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '车跑到每小时三百公里，空气就像一堵墙：车速翻一倍，空气阻力大约变成四倍'),
                (7.2, 14, '方方的车头一头撞上去，空气在前面堵住、在后面乱成漩涡，阻力很大'),
                (14.2, 22, '又长又尖的车头把空气顺顺地分开，阻力小得多；进隧道时的「砰」声也小了')], y=1010)


def e128_power(c, t, i):
    corner_tag(c, '第 128 集 · 每节车都有电机')
    c.text(60, 96, '老火车一个车头拉一串；动车组把电机分到很多节车厢，一起推', 'serif', 40, INK)
    for row, (nm, motors, y) in enumerate((('一个车头拉', [0], 360), ('动力分散（动车组）', [0, 1, 3, 4, 6, 7], 720))):
        acc = 0.4 if row == 0 else 1.0
        dx = min(480, 0.5 * acc * 60 * (t ** 2) / 22)
        x0 = 140 + dx
        c.line([(60, y - 170), (1860, y - 170)], WIRE, 3)
        for k in range(8):
            cx = x0 + k * 150
            c.rect(cx, y - 60, cx + 140, y + 30, fill=TRAIN, r=8)
            c.rect(cx, y - 10, cx + 140, y + 2, fill=STRIPE)
            for wx in (cx + 30, cx + 110):
                c.ellipse(wx, y + 40, 14, 14, fill=(80, 80, 90))
            if k in motors:
                c.rect(cx + 50, y + 10, cx + 90, y + 30, fill=MOTOR, r=4)
        px = x0 + 70
        c.line([(px, y - 60), (px + 30, y - 120), (px, y - 170)], INK, 3)
        c.text(80, y - 100, nm, 'bold', 26, INK, 'lm')
        c.text(80, y + 100, f'带电机的车轮：{len(motors) * 2} 对（示意）', 'sans', 22, MOTOR, 'lm')
    c.text(1700, 560, '橙色：电机', 'sans', 22, MOTOR, 'mm')
    caps(c, t, [(0, 7, '高铁车顶的「受电弓」贴着头顶的电线，把电引进车里'),
                (7.2, 14, '电分给很多节车厢底下的电机，好多对轮子一起使劲，起步快、刹车也稳'),
                (14.2, 22, '这叫动力分散。再加上焊成一整条的无缝钢轨，车跑三百多公里，桌上的水都不怎么晃')], y=1010)


# ---------------------------------------------------------------- E129 潮汐发电
def e129_tides(c, t, i):
    corner_tag(c, '第 129 集 · 月亮拉起两个「水包」')
    c.text(60, 96, '月亮把朝着它的海水拉鼓起来，背面也鼓起一个：地球一转，岸边一天涨两次潮', 'serif', 40, INK)
    cx, cy, R = 700, 580, 200
    spin = t / 22 * 2 * math.pi
    mang = 0.0
    mx, my = cx + 620 * math.cos(mang), cy + 620 * math.sin(mang)
    pts = []
    for j in range(121):
        a = j * 2 * math.pi / 120
        r = R + 40 + 45 * math.cos(2 * (a - mang))
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    c.poly(pts, mix(BG, OCEAN, 0.8))
    c.ellipse(cx, cy, R, R, fill=EARTH)
    for k in range(4):
        a = spin + k * math.pi / 2 + 0.4
        c.ellipse(cx + 120 * math.cos(a), cy + 120 * math.sin(a), 50, 36, fill=LAND)
    pa = spin - math.pi / 2
    pr = R + 40 + 45 * math.cos(2 * (pa - mang))
    px, py = cx + pr * math.cos(pa), cy + pr * math.sin(pa)
    c.ellipse(cx + R * math.cos(pa), cy + R * math.sin(pa), 12, 12, fill=NRED)
    c.ellipse(mx, my, 70, 70, fill=MOON)
    c.text(mx, my + 110, '月亮', 'bold', 26, INK, 'mm')
    c.arrow(mx - 90, my, mx - 250, my, mix(BG, MOON, 0.7), 3, 12)
    c.text(cx, cy + R + 130, '红点：一个海边小镇（地球在转）', 'sans', 22, NRED, 'mm')
    c.rect(1460, 220, 1860, 520, fill=SHEET, r=12)
    c.text(1660, 260, '小镇的海面高度', 'bold', 24, INK, 'mm')
    gx0, gx1, gy = 1490, 1830, 400
    hist = []
    for j in range(101):
        tt = t * j / 100
        a = tt / 22 * 2 * math.pi - math.pi / 2
        hist.append((gx0 + (gx1 - gx0) * tt / 22, gy - 70 * math.cos(2 * (a - mang))))
    if len(hist) > 1:
        c.line(hist, OCEAN, 4)
    c.text(1660, 490, '一圈（约一天）涨两次', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '月亮的引力拉着地球上的海水：朝着月亮的一面，海水被拉得鼓起来'),
                (7.2, 14, '背着月亮的一面也鼓起一个水包（地球被拉向月亮，背面的水「落在后面」）'),
                (14.2, 22, '地球一天转一圈，海边小镇就穿过两个水包：一天大约涨两次、落两次潮（比例为示意）')], y=1010)


def e129_barrage(c, t, i):
    corner_tag(c, '第 129 集 · 涨潮落潮都推水轮')
    c.text(60, 96, '一道坝把海湾围起来：涨潮时海水冲进来，落潮时湾里的水冲出去，都要穿过水轮', 'serif', 40, INK)
    floor = 880
    sea = 520 + 140 * math.sin(t / 22 * 2 * math.pi * 1.0)
    bay = 520 + 140 * math.sin(t / 22 * 2 * math.pi - 0.9)
    wave_x0, wave_x1 = 120, 860
    c.rect(wave_x0, floor - (sea - 300), wave_x1, floor, fill=OCEAN)
    c.rect(1060, floor - (bay - 300), 1800, floor, fill=mix(OCEAN, WATER_L, 0.4))
    c.rect(860, 380, 1060, floor, fill=CONC)
    c.rect(900, floor - 140, 1020, floor - 40, fill=BG)
    diff = sea - bay
    spin = t * 4 * (1 if diff > 0 else -1) * min(1, abs(diff) / 60)
    for k in range(4):
        a = spin + k * math.pi / 2
        c.line([(960, floor - 90), (960 + 40 * math.cos(a), floor - 90 + 40 * math.sin(a))], MOTOR, 6)
    if abs(diff) > 15:
        for k in range(5):
            s = (t * 1.2 + k / 5) % 1
            if diff > 0:
                x = 860 + 200 * s
            else:
                x = 1060 - 200 * s
            c.ellipse(x, floor - 90 + 20 * math.sin(k), 6, 6, fill=WATER_L)
    c.text(490, 330, '大海', 'bold', 28, INK, 'mm')
    c.text(1430, 330, '海湾', 'bold', 28, INK, 'mm')
    c.text(960, 350, '坝里的水轮机', 'sans', 22, MUTED, 'mm')
    lit = abs(diff) > 40
    c.ellipse(960, 270, 22, 22, fill=SPARK if lit else (70, 70, 75))
    c.text(1000, 270, '亮' if lit else '水位差太小，不亮', 'sans', 22, SPARK if lit else MUTED, 'lm')
    c.text(490, 950, '涨潮：海比湾高，水往右冲' if diff > 0 else '落潮：湾比海高，水往左冲', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '涨潮时，大海的水面比海湾高，水穿过坝里的水轮机冲进湾里'),
                (7.2, 14, '落潮时反过来，湾里的水比大海高，又穿过水轮机冲出去'),
                (14.2, 22, '一涨一落都能发电；水位差越大，发得越多。和第 6 集水车发电是一个道理')], y=1010)


# ---------------------------------------------------------------- E130 可回收火箭
def _rocket(c, x, y, ang, legs=0.0, flame=0.0, s=1.0):
    body = [(x - 26 * s, y - 300 * s), (x + 26 * s, y - 300 * s), (x + 26 * s, y), (x - 26 * s, y)]
    c.poly(rot(body, x, y - 150 * s, ang), ROCKET)
    tip = [(x - 26 * s, y - 300 * s), (x + 26 * s, y - 300 * s), (x, y - 360 * s)]
    c.poly(rot(tip, x, y - 150 * s, ang), (200, 205, 215))
    for sgn in (-1, 1):
        lp = [(x + sgn * 26 * s, y - 60 * s), (x + sgn * (26 + 90 * legs) * s, y + 30 * s * legs)]
        c.line(rot(lp, x, y - 150 * s, ang), LEG, 6)
    if flame > 0:
        fl = [(x - 18 * s, y), (x + 18 * s, y), (x, y + 140 * s * flame)]
        c.poly(rot(fl, x, y - 150 * s, ang), FLAME)


def e130_land(c, t, i):
    corner_tag(c, '第 130 集 · 倒着点火，竖着落地')
    c.text(60, 96, '火箭第一级掉头往回飞，快到地面时再点火「刹车」，最后伸腿站稳', 'serif', 40, INK)
    ground = 900
    c.rect(0, ground, 1920, 960, fill=GROUND)
    c.rect(780, ground - 10, 1140, ground, fill=CONC)
    T = 18.0
    tt = min(t, T)
    h = 640 * (1 - tt / T) ** 2
    v = 2 * 640 * (1 - tt / T) / T
    burn = 1.0 if 5 < t < T else 0.0
    legs = fade(t, 13, 16)
    sway = math.radians(8) * math.exp(-tt / 4) * math.sin(tt * 2)
    _rocket(c, 960, ground - h, sway, legs, burn * (0.7 + 0.3 * math.sin(t * 20)), 1.0)
    c.rect(1400, 260, 1860, 600, fill=SHEET, r=14)
    c.text(1630, 300, '下降速度（示意）', 'bold', 24, INK, 'mm')
    c.rect(1440, 360, 1440 + 380 * min(1, v / 75), 390, fill=NRED if v > 30 else GREEN)
    c.text(1630, 440, '发动机：' + ('点火刹车' if burn else '关'), 'sans', 24, SPARK if burn else MUTED, 'mm')
    c.text(1630, 500, '着陆腿：' + ('放下' if legs > 0.5 else '收着'), 'sans', 24, INK, 'mm')
    c.text(1630, 560, '陀螺仪一直在纠偏', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '火箭第一级把上面送走以后，掉头往回落，像一根几十米高的铁杆子往下掉'),
                (7.2, 14, '快到地面时，发动机重新点火，往下喷火，把速度一点点刹下来；陀螺仪随时纠正歪斜'),
                (14.2, 22, '最后几秒放下着陆腿，稳稳站在平台上。2015 年第一次在陆地上成功（拍摄前核对）')], y=1010)


def e130_tip(c, t, i):
    corner_tag(c, '第 130 集 · 腿开得大、重心低，才不倒')
    c.text(60, 96, '站在斜坡上：只要重心的竖直线还落在腿撑开的范围里，就倒不了', 'serif', 40, INK)
    tilt = math.radians(28) * min(1.0, t / 14)
    cases = [('腿窄、重心高', 40, 260), ('腿宽、重心低', 120, 130)]
    for k, (nm, half, gh) in enumerate(cases):
        cx = 520 + k * 820
        base_y = 760
        c.line(rot([(cx - 300, base_y), (cx + 300, base_y)], cx, base_y, -tilt), CONC, 8)
        fl = rot([(cx - half, base_y), (cx + half, base_y)], cx, base_y, -tilt)
        g = rot([(cx, base_y - gh)], cx, base_y, -tilt)[0]
        lo = min(fl[0][0], fl[1][0]); hi = max(fl[0][0], fl[1][0])
        falls = not (lo <= g[0] <= hi)
        crit = math.atan(half / gh)
        extra = min(math.radians(70), max(0.0, tilt - crit) * 5)
        ang = -tilt - extra
        piv = fl[0] if (lo == fl[0][0]) else fl[1]
        pvx, pvy = piv
        def R(pts):
            p1 = rot(pts, cx, base_y, -tilt)
            return rot(p1, pvx, pvy, -extra)
        body = R([(cx - 30, base_y - 360), (cx + 30, base_y - 360), (cx + 30, base_y - 40), (cx - 30, base_y - 40)])
        c.poly(body, ROCKET)
        for sgn in (-1, 1):
            c.line(R([(cx + sgn * 30, base_y - 100), (cx + sgn * half, base_y)]), LEG, 8)
        gg = R([(cx, base_y - gh)])[0]
        c.ellipse(gg[0], gg[1], 14, 14, fill=NRED)
        c.line([(gg[0], gg[1]), (gg[0], base_y + 80)], NRED, 2)
        c.rect(lo, base_y + 90, hi, base_y + 100, fill=GREEN)
        c.text(cx, 230, nm, 'bold', 28, INK, 'mm')
        c.text(cx, base_y + 140, '要倒了！' if falls else '还稳', 'bold', 26, NRED if falls else GREEN, 'mm')
    c.text(960, 300, f'斜坡 {math.degrees(tilt):.0f}°', 'mono', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '红点是重心，红线是从重心往下的竖直线，绿条是腿撑开的范围'),
                (7.2, 14, '斜坡越来越陡：腿窄、重心高的那个，竖直线先跑出了绿条，就要翻倒'),
                (14.2, 22, '腿撑得宽、重的东西放在下面，能站稳的坡度大得多：着陆腿就是这样设计的')], y=1010)


CLIPS = {
 'E128_车头': (e128_nose, 22), 'E128_动力分散': (e128_power, 22),
 'E128_片头': (titles.opening(SER23, VOL23, S23A, 6, '1964 年新干线 · 2008 年京津城际'), 7),
 'E128_片尾': (titles.closing(SER23, VOL23, S23A, 6, '下集：海水一天涨落两次，怎么用来发电？'), 7),
 'E129_潮汐': (e129_tides, 22), 'E129_潮汐坝': (e129_barrage, 22),
 'E129_片头': (titles.opening(SER23, VOL23, S23A, 7, '1966 年法国朗斯潮汐电站'), 7),
 'E129_片尾': (titles.closing(SER23, VOL23, S23A, 7, '下集：火箭怎么竖着落回地面，不倒？'), 7),
 'E130_着陆': (e130_land, 22), 'E130_支撑面': (e130_tip, 22),
 'E130_片头': (titles.opening(SER23, VOL23, S23A, 8, '2015 年火箭第一级首次陆地回收'), 7),
 'E130_片尾': (titles.closing(SER23, VOL23, S23A, 8, '下集：空间站里的人为什么飘着？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
