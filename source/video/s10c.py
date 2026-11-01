"""第十季第三批：E68 制冷、E69 抽水马桶与存水弯、E70 避雷针 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s9a import WATER
from s10a import S10A, SER10, VOL10, STEELC

ICE = (200, 230, 245)
COLD = (90, 160, 230)
WARM = (230, 120, 60)
SMELL = (150, 170, 80)
PORC = (225, 225, 220)

def thermo(c, x, y0, y1, T, Tmin, Tmax, col):
    c.rect(x - 14, y0, x + 14, y1, fill=SHEET, outline=MUTED, width=2, r=14)
    f = (T - Tmin) / (Tmax - Tmin)
    yy = y1 - (y1 - y0 - 20) * max(0, min(1, f))
    c.rect(x - 7, min(yy, y1 - 8), x + 7, y1 - 6, fill=col, r=6)
    c.ellipse(x, y1, 26, 26, fill=col)
    for v in range(int(Tmin), int(Tmax) + 1, 5):
        g = y1 - (y1 - y0 - 20) * (v - Tmin) / (Tmax - Tmin)
        c.line([(x + 16, g), (x + 26, g)], MUTED, 2)
        if v % 10 == 0:
            c.text(x + 34, g, f'{v}', 'mono', 18, MUTED, 'lm')

# ---------------------------------------------------------------- E68 制冷
def e68_ice_salt(c, t, i):
    corner_tag(c, '第 68 集 · 冰加盐')
    c.text(60, 96, '冰加一把盐，为什么比冰更冷？', 'serif', 40, INK)
    u = fade(t, 2, 14)
    cups = [('只有冰', 0.0, MUTED), ('冰 + 盐（约 3:1）', -18.0, COLD)]
    for k, (name, Tend, col) in enumerate(cups):
        x = 380 + k * 560
        a = fade(t, 0.5 + k, 1.5 + k)
        c.text(x, 210, name, 'bold', 30, mix(BG, INK, a), 'mm')
        c.rect(x - 160, 300, x + 160, 700, outline=mix(BG, MUTED, a), width=4, r=10)
        rnd = random.Random(k)
        melt = 0.25 * u if k else 0.05 * u
        if melt > 0.02: c.rect(x - 154, 700 - 400 * melt, x + 154, 694, fill=mix(BG, WATER, 0.45 * a))
        for j in range(14):
            cx_ = x - 120 + (j % 4) * 80 + rnd.uniform(-10, 10)
            cy_ = 360 + (j // 4) * 85 + rnd.uniform(-10, 10)
            s_ = 34 * (1 - 0.3 * melt)
            c.rect(cx_ - s_, cy_ - s_, cx_ + s_, cy_ + s_, fill=mix(BG, ICE, 0.8 * a), r=6)
        if k:
            for j in range(40):
                sx, sy = x - 140 + rnd.random() * 280, 320 + rnd.random() * 360
                c.ellipse(sx, sy, 3, 3, fill=mix(BG, (245, 245, 245), a * (1 - u)))
        T = 2 + (Tend - 2) * ease(u)
        thermo(c, x + 230, 260, 700, T, -20, 10, col)
        c.text(x, 760, f'{T:.0f} °C', 'mono', 40, mix(BG, col if k else INK, a), 'mm')
    b = fade(t, 14, 15)
    c.rect(1280, 260, 1860, 700, fill=mix(BG, SHEET, b), r=12)
    for j, (s, kind, cl) in enumerate([('盐溶进冰表面的水里', 'sans', INK), ('盐水要更冷才会结冰', 'sans', INK),
                                       ('冰只好继续化', 'sans', INK), ('化冰要吸热：', 'bold', COLD), ('热从杯子和周围被拿走', 'sans', INK)]):
        c.text(1310, 310 + j * 70, s, kind, 28, mix(BG, cl, b), 'lm')
    caps(c, t, [(0, 6, '两杯冰，一杯撒上盐，各插一支温度计'),
                (6.2, 14, '只有冰的那杯停在 0 度附近；加了盐的那杯一路往下掉，能到零下十几度（以实测为准）'),
                (14.2, 22, '盐让冰在更低的温度下还在化，化冰要吸热：B12 冰鉴里加盐，也是这个道理')], y=1010)

LOOP = [(560, 300), (1360, 300), (1360, 800), (560, 800)]

def e68_heat_pump(c, t, i):
    corner_tag(c, '第 68 集 · 把热搬出去')
    c.text(60, 96, '冰箱不是「造冷」，是把里面的热搬到外面', 'serif', 40, INK)
    # fridge box
    c.rect(150, 250, 630, 860, outline=COLD, width=4, r=12)
    c.text(390, 900, '冰箱里面', 'bold', 26, COLD, 'mm')
    c.text(1560, 900, '冰箱背后（屋里）', 'bold', 26, WARM, 'mm')
    # components
    a = fade(t, 0.5, 1.5)
    labels = [((960, 250), '压缩机：把气压紧，变热', WARM), ((1700, 470), '散热管：热散到屋里', WARM),
              ((960, 860), '细管：一下子放松，变冷', COLD), ((330, 300), '蒸发管：从里面吸热', COLD)]
    for (x, y), s, col in labels:
        c.text(x, y, s, 'bold', 26, mix(BG, col, a), 'mm')
    c.rect(900, 270, 1020, 330, fill=mix(BG, STEELC, a), r=8)
    # zig-zag condenser on the right, evaporator on the left
    zz = [(1360, 330 + k * 47) for k in range(10)]
    seg(c, [(x + (30 if k % 2 else -30), y) for k, (x, y) in enumerate(zz)], mix(BG, WARM, a), 5)
    ez = [(560, 330 + k * 47) for k in range(10)]
    seg(c, [(x + (30 if k % 2 else -30), y) for k, (x, y) in enumerate(ez)], mix(BG, COLD, a), 5)
    c.line([(560, 300), (1360, 300)], mix(BG, MUTED, a), 4)
    c.line([(1360, 800), (560, 800)], mix(BG, MUTED, a), 2)
    # refrigerant particles around the loop (clockwise)
    L = [800, 500, 800, 500]
    tot = sum(L)
    for k in range(26):
        s = (t * 160 + k * tot / 26) % tot
        for j in range(4):
            if s <= L[j]:
                f = s / L[j]
                x0, y0 = LOOP[j]; x1, y1 = LOOP[(j + 1) % 4]
                x, y = x0 + (x1 - x0) * f, y0 + (y1 - y0) * f
                col = [mix(COLD, WARM, f), WARM, mix(WARM, COLD, min(1, f * 4)), COLD][j]
                c.ellipse(x, y, 9, 9, fill=col)
                break
            s -= L[j]
    # heat arrows
    b = fade(t, 6, 7)
    for k in range(3):
        y = 420 + k * 130
        c.arrow(440, y, 520, y, mix(BG, WARM, b), 4, 14)
        c.arrow(1420, y, 1520, y, mix(BG, WARM, b), 4, 14)
    d = fade(t, 15, 16)
    c.text(960, 560, '1834 年 · 珀金斯：第一台压缩式制冷机', 'sans', 26, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '冰箱的管子里流着一种很容易蒸发的液体'),
                (6.2, 14, '在冰箱里蒸发，吸走里面的热；被压缩机压紧，在背后的管子里把热放给屋里'),
                (14.2, 22, '蒸发吸热，压紧放热，一圈一圈地把热从里面搬到外面：所以冰箱背后是热的')], y=1010)

# ---------------------------------------------------------------- E69 抽水马桶
def pipe_u(cx, top, bot, w):
    return cx, top, bot, w

def e69_trap(c, t, i):
    corner_tag(c, '第 69 集 · 存水弯')
    c.text(60, 96, '一段弯管里的水，挡住下水道的臭味', 'serif', 40, INK)
    for k, (name, trap) in enumerate([('直管', False), ('U 形存水弯', True)]):
        x = 520 + k * 860
        a = fade(t, 0.5 + k, 1.5 + k)
        c.text(x, 200, name, 'bold', 32, mix(BG, INK, a), 'mm')
        w = 70
        if not trap:
            c.rect(x - w / 2, 260, x + w / 2, 900, outline=mix(BG, MUTED, a), width=4)
        else:
            # down leg, U bottom, up leg, then down to sewer
            lx, rx = x - 120, x + 120
            c.rect(lx - w / 2, 260, lx + w / 2, 640, outline=mix(BG, MUTED, a), width=4)
            c.rect(rx - w / 2, 480, rx + w / 2, 640, outline=mix(BG, MUTED, a), width=4)
            c.rect(lx - w / 2, 640, rx + w / 2, 720, outline=mix(BG, MUTED, a), width=4)
            c.rect(rx + w / 2, 480, rx + w / 2 + 160, 540, outline=mix(BG, MUTED, a), width=4)
            c.rect(rx + w / 2 + 100, 540, rx + w / 2 + 160, 900, outline=mix(BG, MUTED, a), width=4)
            wl = 560
            c.rect(lx - w / 2 + 4, wl, lx + w / 2 - 4, 716, fill=mix(BG, WATER, 0.8 * a))
            c.rect(lx - w / 2 + 4, 644, rx + w / 2 - 4, 716, fill=mix(BG, WATER, 0.8 * a))
            c.rect(rx - w / 2 + 4, wl, rx + w / 2 - 4, 716, fill=mix(BG, WATER, 0.8 * a))
            c.text(lx - 80, 640, '水封', 'bold', 26, mix(BG, WATER, a), 'rm')
        # smell particles rise from the sewer
        rnd = random.Random(k)
        for j in range(26):
            ph = (t * 0.35 + rnd.random()) % 1
            if not trap:
                y = 900 - 630 * ph
                xx = x + rnd.uniform(-25, 25)
            else:
                y = 900 - 360 * ph
                xx = x + 120 + 35 + 130 + rnd.uniform(-20, 20)
                if y < 560:
                    continue
            c.ellipse(xx, y, 8, 8, fill=mix(BG, SMELL, a))
        if not trap and a > 0:
            c.text(x, 240 - 0, '', 'sans', 20, INK)
    b = fade(t, 9, 10)
    c.text(520, 960 - 0, '臭气一路冒上来', 'bold', 26, mix(BG, NRED, b), 'mm')
    c.text(1380, 960, '臭气被一截水挡在下面', 'bold', 26, mix(BG, GREEN, b), 'mm')
    caps(c, t, [(0, 7, '下水道里的臭气会顺着管子往上冒：直管挡不住'),
                (7.2, 14, '把管子弯成 U 形，冲完水总会留一截水在弯底，气过不去'),
                (14.2, 22, '1775 年卡明斯为 S 形存水弯申请了专利：一截水，比任何盖子都严')], y=1010)

def e69_flush(c, t, i):
    corner_tag(c, '第 69 集 · 一口气抽走')
    c.text(60, 96, '冲水不是靠「冲」，是靠虹吸「抽」', 'serif', 40, INK)
    # bowl (left) + trapway crest (right)
    bx0, bx1, bbot = 300, 760, 820
    crest = 520
    # timeline: 0-3 idle, 3-7 tank dumps -> bowl level rises above crest, 7-12 siphon drains, 12-14 gurgle, 14-20 refill to seal
    if t < 3: lvl = 600
    elif t < 7: lvl = 600 - 140 * ease(fade(t, 3, 6))
    elif t < 12: lvl = 460 + 340 * ease(fade(t, 7, 11.5))
    else: lvl = 800 - 200 * ease(fade(t, 13, 19))
    siphon = 7 <= t < 12.5
    c.poly([(bx0, 300), (bx1, 300), (bx1 - 60, bbot), (bx0 + 80, bbot)], mix(BG, PORC, 0.15))
    seg(c, [(bx0, 300), (bx0 + 80, bbot), (bx1 - 60, bbot), (bx1, 300)], PORC, 5)
    wl = max(lvl, 300)
    if wl < bbot - 4:
        f0 = (wl - 300) / (bbot - 300)
        xl = bx0 + 80 * f0; xr = bx1 - 60 * f0
        c.poly([(xl, wl), (xr, wl), (bx1 - 60, bbot - 3), (bx0 + 80, bbot - 3)], mix(BG, WATER, 0.75))
    # trapway: up from bowl bottom to crest then down
    tx = [(bx1 - 60, bbot - 40), (900, bbot - 40), (900, crest), (1000, crest), (1000, 960)]
    seg(c, tx, PORC, 5)
    seg(c, [(bx1 - 60, bbot), (940, bbot), (940, crest + 40), (960, crest + 40), (960, 960)], PORC, 5)
    if wl < bbot:
        c.rect(bx1 - 58, max(wl, bbot - 38), 938, bbot - 2, fill=mix(BG, WATER, 0.75))
        c.rect(902, max(wl, crest + 42), 938, bbot - 2, fill=mix(BG, WATER, 0.75))
    if siphon:
        c.rect(902, crest + 2, 998, crest + 38, fill=mix(BG, WATER, 0.75))
        c.rect(962, crest + 2, 998, 958, fill=mix(BG, WATER, 0.75))
        for j in range(5):
            d = (t * 1.5 + j / 5) % 1
            c.arrow(980, crest + 60 + 300 * d, 980, crest + 100 + 300 * d, INK, 3, 10)
    c.line([(860, crest), (1100, crest)], mix(BG, NRED, 0.7), 2)
    c.text(1110, crest, '弯管最高点', 'sans', 22, NRED, 'lm')
    # tank
    tank = 1 - fade(t, 3, 6) + fade(t, 13, 19)
    c.rect(1300, 180, 1700, 280, outline=MUTED, width=3, r=6)
    c.rect(1304, 276 - 92 * tank, 1696, 276, fill=mix(BG, WATER, 0.6))
    c.text(1720, 230, '水箱', 'sans', 22, MUTED, 'lm')
    if 3 < t < 6:
        c.arrow(1300, 280, 780, 320, mix(BG, WATER, 0.9), 4, 14)
    # graph of bowl level
    gx0, gx1, gy0, gy1 = 1300, 1820, 620, 900
    c.line([(gx0, gy1), (gx1, gy1)], MUTED, 2); c.line([(gx0, gy0), (gx0, gy1)], MUTED, 2)
    c.text(gx0, gy0 - 24, '马桶里的水位', 'sans', 22, MUTED, 'lm')
    pts = []
    for j in range(int(200 * min(1, t / 22)) + 1):
        tt = j / 200 * 22
        if tt < 3: L_ = 600
        elif tt < 7: L_ = 600 - 140 * ease(fade(tt, 3, 6))
        elif tt < 12: L_ = 460 + 340 * ease(fade(tt, 7, 11.5))
        else: L_ = 800 - 200 * ease(fade(tt, 13, 19))
        pts.append((gx0 + (gx1 - gx0) * j / 200, gy0 + (L_ - 440) / 380 * (gy1 - gy0)))
    if len(pts) > 1: seg(c, pts, WATER, 4)
    status = '水位高过弯顶 → 虹吸开始' if 6 < t < 12.5 else ('进空气「咕噜」一声，虹吸断了' if 12.5 <= t < 14 else ('补水，留下一截水封' if t >= 14 else ''))
    c.text(1300, 420, status, 'bold', 28, INK, 'lm')
    caps(c, t, [(0, 7, '水箱一放，马桶里的水位很快涨过弯管的最高点'),
                (7.2, 13, '弯管一灌满，就像第 26 集的虹吸管：整碗水被一口气抽走'),
                (13.2, 22, '水快抽干时空气钻进来，「咕噜」一声虹吸断了；再补一点水，水封又回来了')], y=1010)

# ---------------------------------------------------------------- E70 避雷针
def e70_point(c, t, i):
    corner_tag(c, '第 70 集 · 尖端')
    c.text(60, 96, '同样带电，尖的地方电场最强', 'serif', 40, INK)
    for k, (name, pointy) in enumerate([('圆球', False), ('尖针', True)]):
        x = 520 + k * 860
        y = 600
        a = fade(t, 0.5 + k, 1.5 + k)
        c.text(x if not pointy else x - 240, 220 if not pointy else 330, name, 'bold', 32, mix(BG, INK, a), 'mm')
        if not pointy:
            c.ellipse(x, y, 110, 110, fill=mix(BG, STEELC, a))
            n = 16
            for j in range(n):
                q = 2 * math.pi * j / n
                c.line([(x + 115 * math.cos(q), y + 115 * math.sin(q)), (x + 300 * math.cos(q), y + 300 * math.sin(q))], mix(BG, SPARK, 0.6 * a), 2)
        else:
            c.poly([(x - 40, y + 260), (x + 40, y + 260), (x + 40, y - 40), (x, y - 160), (x - 40, y - 40)], mix(BG, STEELC, a))
            for j in range(16):
                q = -math.pi / 2 + (j - 7.5) * 0.12
                c.line([(x, y - 165), (x + 210 * math.cos(q), y - 165 + 210 * math.sin(q))], mix(BG, SPARK, 0.8 * a), 2)
            for j in range(-3, 4):
                if j == 0: continue
                c.line([(x + 44 * (1 if j > 0 else -1), y + 30 * abs(j)), (x + 240 * (1 if j > 0 else -1), y + 30 * abs(j))], mix(BG, SPARK, 0.4 * a), 2)
            g = fade(t, 9, 10)
            if g > 0:
                rnd = random.Random(int(t * 12))
                for j in range(30):
                    r = rnd.random() * 90
                    q = rnd.uniform(-math.pi, 0)
                    c.ellipse(x + r * math.cos(q), y - 170 + r * math.sin(q), 3, 3, fill=mix(BG, (170, 150, 255), g))
                c.text(x + 160, y - 260, '尖端附近的空气被「电离」，', 'sans', 24, mix(BG, INK, g), 'lm')
                c.text(x + 160, y - 220, '电荷慢慢漏走', 'sans', 24, mix(BG, INK, g), 'lm')
    b = fade(t, 5, 6)
    c.text(960, 960, '黄线越密，电场越强', 'sans', 24, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 5, '一个圆球和一根尖针，带上同样多的电'),
                (5.2, 12, '圆球表面电场均匀；尖针上，电荷挤到尖端，那里的电场强得多'),
                (12.2, 22, '强到把空气电离，电荷就从尖端悄悄漏走：第 01 集的莱顿瓶，带尖的导线放电也更快')], y=1010)

def e70_ground(c, t, i):
    corner_tag(c, '第 70 集 · 给雷电一条路')
    c.text(60, 96, '避雷针不是把雷吸走，是给电流一条安全的路（只用动画）', 'serif', 36, INK)
    gy = 900
    c.rect(60, gy, 1860, 960, fill=mix(BG, (110, 90, 60), 0.6))
    for k, rod in enumerate([False, True]):
        x = 520 + k * 860
        a = fade(t, 0.5, 1.5)
        # house
        c.rect(x - 200, 620, x + 200, gy, fill=mix(BG, (150, 120, 90), 0.6 * a))
        c.poly([(x - 240, 620), (x + 240, 620), (x, 460)], mix(BG, (120, 70, 50), 0.8 * a))
        c.text(x, 930, '没有避雷针' if not rod else '有避雷针', 'bold', 30, mix(BG, INK, a), 'mm')
        if rod:
            c.line([(x, 460), (x, 330)], STEELC, 8)
            c.line([(x, 460), (x + 250, 560), (x + 250, gy + 40)], STEELC, 6)
            c.line([(x + 210, gy + 40), (x + 290, gy + 40)], STEELC, 6)
            c.text(x + 270, 700, '粗导线', 'sans', 22, MUTED, 'lm')
            c.text(x + 300, gy + 40, '埋进地里', 'sans', 22, MUTED, 'lm')
        strike = 6 <= t < 7.2 or 6 + 0.0 <= t < 6.2
        if t >= 6:
            fl = fade(t, 6, 6.3) * (1 - fade(t, 7, 8))
            top = (x - 40, 300) if not rod else (x - 20, 300)
            tgt = (x - 30, 520) if not rod else (x, 330)
            rnd = random.Random(k + 5)
            pts = [(top[0] + rnd.uniform(-60, 60), 240)]
            for j in range(1, 7):
                f = j / 7
                pts.append((pts[0][0] + (tgt[0] - pts[0][0]) * f + rnd.uniform(-40, 40), 240 + (tgt[1] - 240) * f))
            pts.append(tgt)
            if fl > 0:
                seg(c, pts, mix(BG, (240, 240, 255), fl), 6)
            if rod:
                g = fade(t, 6.3, 7) * (1 - fade(t, 9, 10))
                for j in range(8):
                    d = (t * 2 + j / 8) % 1
                    path = [(x, 330), (x, 460), (x + 250, 560), (x + 250, gy + 40)]
                    L = [130, 270, 380]; tot = sum(L); s = d * tot
                    for m in range(3):
                        if s <= L[m]:
                            f = s / L[m]
                            px = path[m][0] + (path[m + 1][0] - path[m][0]) * f
                            py = path[m][1] + (path[m + 1][1] - path[m][1]) * f
                            c.ellipse(px, py, 8, 8, fill=mix(BG, SPARK, g)); break
                        s -= L[m]
                r = fade(t, 9, 10)
                if r > 0: c.text(x, 820, '电流沿导线入地，房子没事', 'bold', 26, mix(BG, GREEN, r), 'mm')
            else:
                fire = fade(t, 7, 9)
                if fire > 0:
                    rnd2 = random.Random(int(t * 10))
                    for j in range(12):
                        fx = x - 120 + rnd2.random() * 200
                        c.poly([(fx - 20, 580), (fx + 20, 580), (fx, 580 - 60 * fire * (0.6 + rnd2.random()))], SPARK)
                    c.text(x, 820, '电流穿过屋顶和墙：起火', 'bold', 26, mix(BG, NRED, fire), 'mm')
    b = fade(t, 13, 14)
    c.rect(560, 150, 1360, 210, fill=mix(BG, SHEET, b), r=10)
    c.text(960, 180, '1752 年富兰克林提出避雷针（风筝实验极其危险，切勿模仿）', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '雷电要找一条路进地里：没有现成的路，就从屋顶、墙壁、电线里硬闯'),
                (6.2, 12, '避雷针顶上是尖的，下面接一根粗导线，一直埋到地里'),
                (12.2, 22, '雷电走电阻最小的路，顺着导线进了地，房子安然无恙。雷雨天不做任何户外实验')], y=1010)

CLIPS = {
 'E68_冰盐': (e68_ice_salt, 22), 'E68_热泵': (e68_heat_pump, 22),
 'E68_片头': (titles.opening(SER10, VOL10, S10A, 6, '1755 年卡伦 · 1834 年珀金斯'), 7),
 'E68_片尾': (titles.closing(SER10, VOL10, S10A, 6, '下集：马桶为什么不臭？'), 7),
 'E69_水封': (e69_trap, 22), 'E69_虹吸冲水': (e69_flush, 22),
 'E69_片头': (titles.opening(SER10, VOL10, S10A, 7, '1596 年哈林顿 · 1775 年卡明斯'), 7),
 'E69_片尾': (titles.closing(SER10, VOL10, S10A, 7, '下集：一根铁杆，怎么保护整栋楼？'), 7),
 'E70_尖端': (e70_point, 22), 'E70_接地': (e70_ground, 22),
 'E70_片头': (titles.opening(SER10, VOL10, S10A, 8, '1752 年 · 费城 · 富兰克林'), 7),
 'E70_片尾': (titles.closing(SER10, VOL10, S10A, 8, '下集：怎样把乘法变成加法？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
