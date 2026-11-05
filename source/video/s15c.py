"""第十五季（第四层）第三批：E88 火箭、E89 光纤、E90 卫星定位 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s15a import S15A, SER15, VOL15, WAVE

BALL = (230, 120, 80)
GAS = (240, 180, 90)
LASER = (240, 70, 60)
WATERC = (90, 150, 210)

# ---------------------------------------------------------------- E88 火箭
def e88_recoil(c, t, i):
    corner_tag(c, '第 88 集 · 往后扔，就往前走')
    c.text(60, 96, '站在滑板上往后扔球：人往前滑', 'serif', 40, INK)
    y = 520
    n = min(5, int(max(0, t - 2) / 2.2))
    v = 0.0
    x = 900.0
    for k in range(n):
        tk = 2 + k * 2.2
        x += 40 * (t - tk) if t > tk else 0
    x = min(x, 1500)
    c.rect(x - 60, y + 100, x + 60, y + 116, fill=MUTED, r=6)
    c.ellipse(x - 40, y + 124, 10, 10, fill=INK)
    c.ellipse(x + 40, y + 124, 10, 10, fill=INK)
    c.ellipse(x, y - 60, 26, 26, fill=INK)
    c.rect(x - 18, y - 30, x + 18, y + 100, fill=INK, r=8)
    for k in range(n):
        tk = 2 + k * 2.2
        bx = x - 40 - 160 * (t - tk)
        if bx > 60:
            c.ellipse(bx, y + 10 + k * 6, 18, 18, fill=BALL)
    c.text(x + 60, y - 120, f'扔出 {n} 个球', 'bold', 26, INK, 'lm')
    a = fade(t, 13, 14)
    c.rect(200, 760, 1720, 880, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 800, '球往后的动量 = 人往前的动量（动量守恒）', 'bold', 28, mix(BG, INK, a), 'mm')
    c.text(960, 845, '火箭扔的不是球，是每秒几吨高速喷出的燃气：不需要「推着」任何东西', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '站在滑板上，往后用力扔一个球：人就往前滑一点'),
                (6.2, 13, '扔得越多、越快，人滑得越快：不需要推墙，也不需要推空气'),
                (13.2, 22, '火箭就是一直往后扔燃气的「人」：所以在没有空气的太空里也能加速')], y=1010)

def e88_exhaust(c, t, i):
    corner_tag(c, '第 88 集 · 喷得越快越好')
    c.text(60, 96, '同样多的气，喷得越快，火箭得到的速度越大', 'serif', 40, INK)
    rows = [('粗喷口：喷得慢', 0.45, MUTED), ('细喷口：喷得快（但别太细，气出不来）', 0.8, GREEN)]
    for k, (nm, sp, col) in enumerate(rows):
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        y = 320 + k * 260
        c.line([(160, y), (1760, y)], mix(BG, LINE, a), 2)
        prog = fade(t, 2 + k * 5, 10 + k * 5)
        x = 260 + 1300 * sp * prog
        r = 70 * (1 - 0.6 * prog)
        c.ellipse(x, y, r + 30, r, fill=mix(BG, (210, 80, 80), a))
        w = 16 if k == 0 else 8
        for j in range(6):
            gx = x - r - 40 - j * 40 * (1.6 if k else 1)
            if gx > 160:
                c.ellipse(gx, y + (j % 2) * 8 - 4, w, w * 0.7, fill=mix(BG, GAS, a * (1 - j / 7)))
        c.text(160, y - 80, nm, 'bold', 28, mix(BG, INK, a), 'lm')
    d = fade(t, 13, 14)
    c.rect(200, 800, 1720, 920, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 840, '火箭最终的速度看两样：喷气有多快、燃料占全身重量的比例有多大', 'bold', 26, mix(BG, INK, d), 'mm')
    c.text(960, 885, '1903 年齐奥尔科夫斯基写出了这个关系；1926 年戈达德发射了第一枚液体火箭（拍摄前核对）', 'sans', 22, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '气球火箭：同样一口气，从粗口子慢慢漏，和从细口子快快喷'),
                (6.2, 13, '喷得快的那个飞得更远：每一份气往后带走的动量更多'),
                (13.2, 22, '真火箭也一样：燃料烧得越猛、喷气越快，还要让燃料占的比例尽量大（本集只用气球）')], y=1010)

# ---------------------------------------------------------------- E89 光纤
def e89_tir(c, t, i):
    corner_tag(c, '第 89 集 · 全反射')
    c.text(60, 96, '光从水里往外射：斜到一定程度，一点都出不去', 'serif', 40, INK)
    sx, sy = 560, 820
    c.rect(0, 520, 1920, 980, fill=mix(BG, WATERC, 0.35))
    c.line([(0, 520), (1920, 520)], WATERC, 3)
    c.text(120, 470, '空气', 'bold', 26, MUTED, 'lm')
    c.text(120, 570, '水', 'bold', 26, WATERC, 'lm')
    ang = 10 + 52 * fade(t, 2, 16)
    crit = math.degrees(math.asin(1 / 1.33))
    a = math.radians(ang)
    hx = sx + (sy - 520) * math.tan(a)
    c.line([(sx, sy), (hx, 520)], LASER, 5)
    if ang < crit:
        b = math.asin(min(1, 1.33 * math.sin(a)))
        c.line([(hx, 520), (hx + 400 * math.sin(b), 520 - 400 * math.cos(b))], mix(BG, LASER, 0.9), 5)
        c.line([(hx, 520), (hx + 300 * math.sin(a), 520 + 300 * math.cos(a))], mix(BG, LASER, 0.3), 3)
    else:
        c.line([(hx, 520), (hx + 400 * math.sin(a), 520 + 400 * math.cos(a))], LASER, 5)
        c.text(hx + 60, 480, '全部反射回水里', 'bold', 28, SPARK, 'lm')
    c.ellipse(sx, sy, 12, 12, fill=LASER)
    c.line([(sx, 520 - 200), (sx, sy)], mix(BG, MUTED, 0.6), 1)
    c.text(sx - 20, 300, f'入射角 {ang:.0f}°', 'mono', 28, INK, 'rm')
    c.text(1800, 300, f'临界角约 {crit:.0f}°（水 → 空气）', 'sans', 24, MUTED, 'rm')
    caps(c, t, [(0, 6, '激光从水底斜着往上射：一部分穿出水面，拐个弯；一部分反射回来'),
                (6.2, 13, '越斜，穿出去的越少；到了大约 49 度，一点都出不去了'),
                (13.2, 22, '这叫全反射：光从「密」的材料射向「疏」的材料，够斜就全部被关在里面')], y=1010)

def e89_fiber(c, t, i):
    corner_tag(c, '第 89 集 · 把光关在玻璃丝里')
    c.text(60, 96, '玻璃丝够细、拐弯够缓：光一路全反射，跟着走', 'serif', 40, INK)
    pts_top, pts_bot = [], []
    for k in range(81):
        u = k / 80
        x = 160 + u * 1600
        y = 520 + 180 * math.sin(u * math.pi * 1.2)
        pts_top.append((x, y - 50))
        pts_bot.append((x, y + 50))
    c.poly(pts_top + pts_bot[::-1], mix(BG, (170, 200, 220), 0.35))
    c.line(pts_top, (170, 200, 220), 3)
    c.line(pts_bot, (170, 200, 220), 3)
    prog = fade(t, 2, 14)
    path = []
    n = int(80 * prog)
    for k in range(n + 1):
        u = k / 80
        x = 160 + u * 1600
        y = 520 + 180 * math.sin(u * math.pi * 1.2) + 40 * math.sin(u * 60)
        path.append((x, y))
    if len(path) > 1:
        c.line(path, LASER, 4)
    a = fade(t, 13, 14)
    c.rect(200, 800, 1720, 920, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 840, '真光纤：比头发还细的玻璃芯，外面包一层折射率稍低的玻璃', 'bold', 26, mix(BG, INK, a), 'mm')
    c.text(960, 885, '1842 年科拉东用水流导光；1966 年高锟算出：玻璃够纯，光就能传几十公里（拍摄前核对）', 'sans', 22, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '光射到玻璃丝的内壁，入射角都很大：每一次都被全反射回去'),
                (6.2, 13, '就这样一路反弹、一路拐弯，跟着玻璃丝走到很远的地方'),
                (13.2, 22, '光一闪一灭就是 1 和 0：今天的互联网，海底下铺的就是这样的玻璃丝（接第 50 集光学电报）')], y=1010)

# ---------------------------------------------------------------- E90 卫星定位
SATS = [(640, 460, 300), (1240, 500, 380), (1150, 700, 0)]

def e90_circles(c, t, i):
    corner_tag(c, '第 90 集 · 三个圆交于一点')
    c.text(60, 96, '知道离三个已知点有多远：位置就只剩一个', 'serif', 40, INK)
    # true point
    tx, ty = 0, 0
    # compute point consistent with first two circles (choose one intersection), then define third radius
    (x1, y1, r1), (x2, y2, r2) = SATS[0], SATS[1]
    d = math.hypot(x2 - x1, y2 - y1)
    a_ = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(max(0, r1 * r1 - a_ * a_))
    mx, my = x1 + a_ * (x2 - x1) / d, y1 + a_ * (y2 - y1) / d
    p1 = (mx + h * (y2 - y1) / d, my - h * (x2 - x1) / d)
    p2 = (mx - h * (y2 - y1) / d, my + h * (x2 - x1) / d)
    x3, y3, _ = SATS[2]
    r3 = math.hypot(p2[0] - x3, p2[1] - y3)
    circles = [(x1, y1, r1, 1), (x2, y2, r2, 5), (x3, y3, r3, 10)]
    for k, (x, y, r, t0) in enumerate(circles):
        a = fade(t, t0, t0 + 1.5)
        if a <= 0: continue
        c.ellipse(x, y, r, r, outline=mix(BG, [WAVE, GREEN, SPARK][k], a), width=4)
        c.ellipse(x, y, 14, 14, fill=mix(BG, [WAVE, GREEN, SPARK][k], a))
        c.text(x, y - 34, f'卫星 {k + 1}', 'bold', 24, mix(BG, INK, a), 'mm')
    b = fade(t, 7, 8)
    for p in (p1, p2):
        if t < 12 or p == p2:
            c.ellipse(p[0], p[1], 14, 14, outline=mix(BG, INK, b), width=4)
    if t >= 12:
        c.ellipse(p2[0], p2[1], 18, 18, fill=NRED)
        c.text(p2[0] + 30, p2[1], '你在这里', 'bold', 28, NRED, 'lm')
    caps(c, t, [(0, 5, '离卫星 1 有多远？那你一定在这个圆上'),
                (5.2, 10, '再加卫星 2：两个圆只交在两个点'),
                (10.2, 22, '加上卫星 3：三个圆只交于一点。在真实的三维空间里是球面，道理一样')], y=1010)

def e90_clock(c, t, i):
    corner_tag(c, '第 90 集 · 距离是用时间量的')
    c.text(60, 96, '卫星不停地报时：信号走了多久，乘光速就是距离', 'serif', 40, INK)
    rows = [('信号走了 0.07 秒', '× 30 万千米/秒', '≈ 2 万千米：卫星的高度'),
            ('钟差 1 微秒', '× 30 万千米/秒', '= 300 米的误差'),
            ('钟差 1 毫秒', '× 30 万千米/秒', '= 300 千米：差出一个城市')]
    for k, (a_, b_, c_) in enumerate(rows):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        y = 260 + k * 140
        c.rect(160, y - 50, 1760, y + 50, fill=mix(BG, SHEET, a), r=12)
        c.text(200, y, a_, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(720, y, b_, 'mono', 26, mix(BG, MUTED, a), 'lm')
        c.text(1160, y, c_, 'bold', 28, mix(BG, NRED if k else GREEN, a), 'lm')
    d = fade(t, 13, 14)
    c.rect(160, 720, 1760, 900, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 770, '卫星上装着原子钟，手机里只有便宜的石英钟', 'bold', 28, mix(BG, INK, d), 'mm')
    c.text(960, 820, '办法：再多用一颗卫星，把「手机的钟差多少」也当成一个未知数一起解出来', 'sans', 26, mix(BG, INK, d), 'mm')
    c.text(960, 865, '所以至少要 4 颗卫星（接第 45 集摆钟、第 47 集影子测地球）', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '卫星离地约两万千米，信号走到手机只要零点零几秒'),
                (6.2, 13, '可光太快了：钟差一微秒，位置就差三百米'),
                (13.2, 22, '手机的钟不够准，就多听一颗卫星，把钟差也算出来：四颗卫星，三个坐标加一个时间')], y=1010)

CLIPS = {
 'E88_反冲': (e88_recoil, 22), 'E88_喷速': (e88_exhaust, 22),
 'E88_片头': (titles.opening(SER15, VOL15, S15A, 6, '1926 年 · 戈达德液体火箭'), 7),
 'E88_片尾': (titles.closing(SER15, VOL15, S15A, 6, '下集：一根玻璃丝，怎么把光送到几千公里外？'), 7),
 'E89_全反射': (e89_tir, 22), 'E89_光纤': (e89_fiber, 22),
 'E89_片头': (titles.opening(SER15, VOL15, S15A, 7, '1966 年 · 高锟'), 7),
 'E89_片尾': (titles.closing(SER15, VOL15, S15A, 7, '下集：手机怎么知道你在哪？'), 7),
 'E90_三个圆': (e90_circles, 22), 'E90_时钟': (e90_clock, 22),
 'E90_片头': (titles.opening(SER15, VOL15, S15A, 8, '1978 年 GPS · 2020 年北斗全球组网'), 7),
 'E90_片尾': (titles.closing(SER15, VOL15, S15A, 8, '下集：一堆开关，怎么一步步「照着做」？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
