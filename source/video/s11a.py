"""第十一季（古法解密 3.0：中国与世界）第一批：B30 坎儿井、B31 冰裂纹、B32 松烟墨 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s9a import WATER

SB11 = [('B30', '坎儿井'), ('B31', '冰裂纹'), ('B32', '松烟墨'), ('B33', '素纱襌衣'), ('B34', '水运仪象台'),
        ('B35', '罗马混凝土'), ('B36', '古埃及巨石'), ('B37', '星盘'), ('B38', '安提基特拉'), ('B39', '大马士革钢')]
VOL11 = '第十一季 · 古法解密 3.0'
SAND = (200, 170, 110)
ROCK = (120, 105, 90)
GLAZE = (170, 200, 190)
BODY = (150, 120, 100)
SOOT = (35, 35, 38)
DYE = (70, 90, 200)

# ---------------------------------------------------------------- B30 坎儿井
def b30_evap(c, t, i):
    corner_tag(c, 'B30 · 露天还是地下')
    c.text(60, 96, '同样一条水渠，露天走和地下走，差在哪？', 'serif', 40, INK)
    # sun and wind
    c.ellipse(1700, 200, 60, 60, fill=SPARK)
    for k in range(4):
        y = 230 + k * 30
        x = 200 + ((t * 300 + k * 230) % 1300)
        c.arrow(x, y, x + 60, y, mix(BG, MUTED, 0.7), 2, 8)
    prog = fade(t, 1, 16)
    for row, (name, under) in enumerate([('露天水渠', False), ('坎儿井（暗渠）', True)]):
        y = 470 + row * 280
        a = fade(t, 0.5 + row, 1.5 + row)
        c.text(100, y - 90, name, 'bold', 30, mix(BG, INK, a), 'lm')
        x0, x1 = 300, 1600
        if under:
            c.rect(x0, y - 60, x1, y + 60, fill=mix(BG, SAND, 0.6 * a))
            for k in range(6):
                sx = x0 + 100 + k * 240
                c.rect(sx - 10, y - 60, sx + 10, y - 20, fill=mix(BG, ROCK, a))
        # water: amount decays along the channel; open channel loses more
        loss = 0.75 if not under else 0.08
        N = 60
        for j in range(N):
            f = j / N
            if f > prog: break
            depth = 34 * (1 - loss * f)
            xx = x0 + (x1 - x0) * f
            c.rect(xx, y + 20 - depth, xx + (x1 - x0) / N + 1, y + 20, fill=mix(BG, WATER, 0.8 * a))
            if not under and j % 6 == 0 and prog > f:
                ph = (t * 0.8 + j * 0.13) % 1
                c.ellipse(xx, y - 10 - 80 * ph, 5, 5, fill=mix(BG, WATER, 0.6 * (1 - ph)))
        if prog > 0.98:
            left = int(100 * (1 - loss))
            c.text(x1 + 30, y, f'剩约 {left}%', 'bold', 28, mix(BG, NRED if not under else GREEN, fade(t, 16, 17)), 'lm')
    caps(c, t, [(0, 6, '吐鲁番夏天又干又热，风沙大：露天的水渠，水还没流到绿洲就被晒干吹干了'),
                (6.2, 15, '坎儿井把水渠挖在地下：太阳晒不到，风吹不着，蒸发少得多'),
                (15.2, 22, '同样一条渠，到了出口，剩下的水差得很远（比例为示意，以实测为准）')], y=1010)

def b30_slope(c, t, i):
    corner_tag(c, 'B30 · 坡度与竖井')
    c.text(60, 96, '不用水泵，水怎么自己流几十里？', 'serif', 40, INK)
    # terrain profile: mountain at left, oasis at right
    ground = [(60, 300), (400, 380), (900, 520), (1400, 620), (1860, 680)]
    c.poly(ground + [(1860, 960), (60, 960)], mix(BG, SAND, 0.45))
    seg(c, ground, SAND, 3)
    a = fade(t, 1, 2)
    # aquifer
    c.poly([(60, 560), (500, 620), (500, 700), (60, 700)], mix(BG, WATER, 0.35 * a))
    c.text(120, 640, '山前地下水', 'bold', 24, mix(BG, WATER, a), 'lm')
    # tunnel: gentle slope from mother well to outlet
    tx0, ty0, tx1, ty1 = 460, 640, 1820, 676
    b = fade(t, 2, 8)
    xe = tx0 + (tx1 - tx0) * b
    ye = ty0 + (ty1 - ty0) * b
    c.line([(tx0, ty0), (xe, ye)], WATER, 10)
    # vertical shafts
    def gy(x):
        for (x0, y0), (x1, y1) in zip(ground, ground[1:]):
            if x0 <= x <= x1:
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
        return ground[-1][1]
    for k in range(9):
        x = tx0 + 40 + k * 140
        if x > xe: break
        yt = ty0 + (ty1 - ty0) * (x - tx0) / (tx1 - tx0)
        c.line([(x, gy(x)), (x, yt)], mix(BG, ROCK, 0.9), 4)
        c.ellipse(x, gy(x) - 6, 14, 6, fill=ROCK)
    c.text(tx0, ty0 + 50, '母井', 'bold', 24, INK, 'mm')
    c.text(1760, 720, '绿洲', 'bold', 28, GREEN, 'mm')
    d = fade(t, 9, 10)
    c.rect(1080, 180, 1840, 420, fill=mix(BG, SHEET, d), r=10)
    c.text(1110, 220, '暗渠比地面坡度更缓：', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1110, 265, '每走 1 千米只降几米（千分之几）', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1110, 320, '竖井：挖的时候出土、通风、定方向', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1110, 375, '吐鲁番现有约一千条（997 条），总长近 3500 公里', 'sans', 22, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 8, '先在山前找到地下水，打一口母井；再从绿洲方向往回挖一条微微倾斜的暗渠'),
                (8.2, 15, '暗渠的坡度比地面缓，水靠重力自己流，到绿洲时正好冒出地面'),
                (15.2, 22, '一排排竖井是挖渠时出土、通风用的：从天上看，像一串串珠子')], y=1010)

# ---------------------------------------------------------------- B31 冰裂纹
def b31_shrink(c, t, i):
    corner_tag(c, 'B31 · 釉比胎缩得多')
    c.text(60, 96, '出窑冷却时，釉和胎各缩各的', 'serif', 40, INK)
    cool = fade(t, 2, 12)
    T = 1200 - 1180 * cool
    c.text(1700, 96, f'{T:.0f} °C', 'mono', 40, mix(INK, (90, 160, 230), cool), 'rm')
    x0, x1, yb = 300, 1620, 640
    L = x1 - x0
    # body shrinks a little, glaze wants to shrink more
    sb = 0.02 * cool
    sg = 0.05 * cool
    bx0, bx1 = x0 + L * sb / 2, x1 - L * sb / 2
    c.rect(bx0, yb, bx1, yb + 160, fill=BODY, r=4)
    c.text((x0 + x1) / 2, yb + 80, '胎', 'bold', 32, INK, 'mm')
    # glaze: stays attached to body length, so it is stretched -> cracks
    want0, want1 = x0 + L * sg / 2, x1 - L * sg / 2
    a = fade(t, 4, 5)
    if a > 0 and cool < 0.85:
        c.rect(want0, yb - 120, want1, yb - 80, outline=mix(BG, GLAZE, a), width=2, r=4)
        c.text((x0 + x1) / 2, yb - 150, '釉「想」缩到这么短', 'sans', 24, mix(BG, MUTED, a), 'mm')
    cracks = cool > 0.85
    if not cracks:
        c.rect(bx0, yb - 40, bx1, yb, fill=GLAZE, r=3)
        tens = fade(t, 5, 9)
        for k in range(6):
            x = bx0 + 80 + k * 220
            c.arrow(x, yb - 20, x - 50 * tens, yb - 20, mix(BG, NRED, tens), 3, 10)
            c.arrow(x + 40, yb - 20, x + 40 + 50 * tens, yb - 20, mix(BG, NRED, tens), 3, 10)
        c.text((x0 + x1) / 2, yb - 60, '被胎拉住：釉里全是拉力', 'bold', 26, mix(BG, NRED, tens), 'mm')
    else:
        rnd = random.Random(31)
        xs = [bx0]
        while xs[-1] < bx1 - 60:
            xs.append(xs[-1] + rnd.uniform(70, 150))
        xs[-1] = bx1
        gap = 4 + 8 * fade(t, 10.5, 12)
        for xa, xb in zip(xs, xs[1:]):
            c.rect(xa + gap / 2, yb - 40, xb - gap / 2, yb, fill=GLAZE, r=2)
            c.line([(xb, yb - 44), (xb, yb)], (60, 50, 40), 3)
        c.text((x0 + x1) / 2, yb - 70, '拉力超过釉的强度：裂开', 'bold', 28, NRED, 'mm')
    b = fade(t, 15, 16)
    c.rect(300, 860, 1620, 940, fill=mix(BG, SHEET, b), r=10)
    c.text(330, 900, '窑工调釉的配方，让釉比胎多缩一点：裂纹就成了故意的花纹（开片）', 'sans', 26, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 6, '瓷器出窑时有一千多度。冷下来，胎和釉都会缩'),
                (6.2, 12, '如果釉比胎缩得多，釉被胎拉住缩不回去，里面全是拉力'),
                (12.2, 22, '拉力一大，釉就裂成一块块：这就是冰裂纹。缩得差不多，就不裂')], y=1010)

_NETS = {}

def _net(w, h, cell, seed, step=5):
    key = (w, h, cell, seed)
    if key in _NETS: return _NETS[key]
    rnd = random.Random(seed)
    n = max(4, int(w * h / (cell * cell)))
    pts = [(rnd.random() * w, rnd.random() * h) for _ in range(n)]
    gw, gh = int(w // step), int(h // step)
    lab = [[0] * gw for _ in range(gh)]
    for r in range(gh):
        y = r * step
        for q in range(gw):
            x = q * step
            best, bi = 1e18, 0
            for k, (px, py) in enumerate(pts):
                d = (px - x) ** 2 + (py - y) ** 2
                if d < best: best, bi = d, k
            lab[r][q] = bi
    out = []
    ox, oy = rnd.random() * w, rnd.random() * h
    for r in range(gh - 1):
        for q in range(gw - 1):
            if lab[r][q] != lab[r][q + 1] or lab[r][q] != lab[r + 1][q]:
                x, y = q * step, r * step
                out.append((math.hypot(x - ox, y - oy), x, y))
    out.sort()
    m = out[-1][0] if out else 1
    _NETS[key] = [(d / m, x, y) for d, x, y in out]
    return _NETS[key]

def crack_net(c, x0, y0, w, h, cell, seed, col, prog=1.0):
    for f, x, y in _net(w, h, cell, seed):
        if f > prog: break
        c.rect(x0 + x, y0 + y, x0 + x + 4, y0 + y + 4, fill=col)

def b31_spacing(c, t, i):
    corner_tag(c, 'B31 · 裂纹的大小')
    c.text(60, 96, '涂层越厚，裂开的块越大', 'serif', 40, INK)
    for k, (name, cell) in enumerate([('薄涂', 45), ('中等', 90), ('厚涂', 160)]):
        x0 = 120 + k * 590
        a = fade(t, 0.5 + k * 0.8, 1.5 + k * 0.8)
        c.text(x0 + 250, 210, name, 'bold', 30, mix(BG, INK, a), 'mm')
        c.rect(x0, 260, x0 + 500, 760, fill=mix(BG, (225, 220, 205), a), r=8)
        p = fade(t, 3 + k, 12 + k)
        if p > 0:
            crack_net(c, x0 + 10, 270, 480, 480, cell, k + 3, mix((225, 220, 205), (60, 50, 40), min(1, p * 1.5)), p)
        b = fade(t, 14, 15)
        c.text(x0 + 250, 800, f'块的大小约 {cell // 45} 份', 'mono', 24, mix(BG, MUTED, b), 'mm')
    d = fade(t, 16, 17)
    c.text(960, 880, '哥窑的「金丝铁线」：大块裂纹和小块裂纹，用墨和茶各染一种颜色（工艺细节待核）', 'sans', 26, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 6, '玉米淀粉糊薄薄地、中等地、厚厚地各涂一盘，晾干'),
                (6.2, 14, '干的时候糊比盘子缩得多，同样会裂：薄的裂成碎碎的小块，厚的裂成大块'),
                (14.2, 22, '窑工控制釉的厚薄和配方，就能控制开片的大小（淀粉糊只是类比，原理相通）')], y=1010)

# ---------------------------------------------------------------- B32 松烟墨
def b32_soot(c, t, i):
    corner_tag(c, 'B32 · 烟灰就是碳')
    c.text(60, 96, '火烧得不充分，就会冒出黑烟：那是碳', 'serif', 40, INK)
    cx, base = 520, 860
    c.rect(cx - 30, base - 200, cx + 30, base, fill=(230, 225, 210), r=6)
    fh = 90 + 12 * math.sin(t * 9)
    c.poly([(cx - 22, base - 200), (cx + 22, base - 200), (cx, base - 200 - fh)], SPARK)
    # spoon above the flame collecting soot
    sy = base - 200 - 120
    cover = fade(t, 3, 12)
    c.ellipse(cx, sy, 120, 26, fill=(190, 195, 205))
    c.ellipse(cx, sy + 4, 110 * cover, 18 * cover, fill=SOOT)
    c.line([(cx + 120, sy), (cx + 360, sy - 60)], (190, 195, 205), 10)
    rnd = random.Random(int(t * 15))
    for k in range(30):
        ph = rnd.random()
        c.ellipse(cx + rnd.uniform(-20, 20), base - 200 - fh - 100 * ph * 0.5, 4, 4, fill=SOOT)
    c.text(cx, 220, '（成年人操作：金属勺，夹子夹着）', 'sans', 24, MUTED, 'mm')
    # zoom: carbon particles + glue
    a = fade(t, 8, 9)
    zx, zy, zr = 1350, 520, 300
    c.ellipse(zx, zy, zr, zr, fill=mix(BG, SHEET, a), outline=mix(BG, MUTED, a), width=3)
    r2 = random.Random(5)
    glue = fade(t, 13, 15)
    for k in range(70):
        q = r2.random() * 2 * math.pi; rr = zr * 0.85 * math.sqrt(r2.random())
        x, y = zx + rr * math.cos(q), zy + rr * math.sin(q)
        if glue > 0:
            c.ellipse(x, y, 18, 18, fill=mix(BG, (200, 170, 100), 0.5 * glue * a))
        c.ellipse(x, y, 11, 11, fill=mix(BG, SOOT, a))
    c.text(zx, zy + zr + 40, '放大：极细的碳颗粒' + ('，外面裹一层胶' if glue > 0.5 else ''), 'bold', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 7, '蜡烛、松木、油烧得不充分，就会冒出黑烟：烟里是极细的碳颗粒'),
                (7.2, 13, '古人烧松木收集「松烟」，沈括还试过用石油的烟做墨（《梦溪笔谈》，拍摄前核对）'),
                (13.2, 22, '再加胶揉成墨锭：胶把碳颗粒粘在一起，写到纸上又把它粘在纤维之间')], y=1010)

def b32_fade(c, t, i):
    corner_tag(c, 'B32 · 为什么不褪色')
    c.text(60, 96, '晒太阳、泡漂白水：碳墨和染料墨谁先褪？', 'serif', 40, INK)
    # left: molecules under light
    a = fade(t, 0.5, 1.5)
    c.text(480, 200, '染料墨：一个个有颜色的分子', 'bold', 28, mix(BG, INK, a), 'mm')
    c.text(1440, 200, '碳墨：一粒粒碳', 'bold', 28, mix(BG, INK, a), 'mm')
    hit = fade(t, 4, 12)
    rnd = random.Random(2)
    for k in range(16):
        x, y = 200 + (k % 4) * 180 + rnd.uniform(-20, 20), 300 + (k // 4) * 110
        broken = k / 16 < hit * 0.85
        if broken:
            c.line([(x - 30, y), (x - 8, y + 12)], mix(BG, MUTED, a), 4)
            c.line([(x + 8, y - 12), (x + 30, y)], mix(BG, MUTED, a), 4)
        else:
            c.line([(x - 30, y), (x + 30, y)], DYE, 6)
            c.ellipse(x, y, 10, 10, fill=DYE)
    for k in range(16):
        x, y = 1160 + (k % 4) * 180, 300 + (k // 4) * 110
        c.ellipse(x, y, 26, 26, fill=SOOT, outline=MUTED, width=2)
    # light rays
    for k in range(8):
        ph = (t * 0.7 + k / 8) % 1
        for x0 in (160, 1120):
            x = x0 + k * 90
            c.line([(x, 240 + 400 * ph), (x + 20, 260 + 400 * ph)], mix(BG, SPARK, 0.8), 3)
    # bars: colour left after N days
    b = fade(t, 13, 14)
    days = 14 * fade(t, 14, 20)
    for k, (name, rate, col) in enumerate([('水性记号笔', 0.06, DYE), ('自制烟灰墨', 0.002, SOOT)]):
        y = 820 + k * 70
        left = max(0.0, 1 - rate * days)
        c.text(500, y, name, 'sans', 26, mix(BG, INK, b), 'rm')
        c.rect(520, y - 20, 520 + 900 * left, y + 20, fill=mix(BG, col if col != SOOT else (90, 90, 95), b), r=4)
    c.text(1460, 855, f'晒了 {days:.0f} 天（示意）', 'mono', 26, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 7, '染料墨的颜色来自一个个分子：阳光和漂白水能把它们打断，颜色就没了'),
                (7.2, 13, '碳很「懒」，几乎不跟光和漂白水反应：黑还是黑'),
                (13.2, 22, '所以两千年前的竹简和帛书，墨迹还是黑的（褪色速度为示意，以实测为准）')], y=1035)

CLIPS = {
 'B30_蒸发': (b30_evap, 22), 'B30_坡度': (b30_slope, 22),
 'B30_片头': (titles.opening(BSER, VOL11, SB11, 0, '吐鲁番 · 沙漠里的地下河'), 7),
 'B30_片尾': (titles.closing(BSER, VOL11, SB11, 0, '下集：瓷器上的裂纹，为什么是故意的？'), 7),
 'B31_热胀冷缩': (b31_shrink, 22), 'B31_裂纹大小': (b31_spacing, 22),
 'B31_片头': (titles.opening(BSER, VOL11, SB11, 1, '南宋 · 哥窑与官窑的开片'), 7),
 'B31_片尾': (titles.closing(BSER, VOL11, SB11, 1, '下集：一块墨，为什么千年不褪色？'), 7),
 'B32_烟灰': (b32_soot, 22), 'B32_褪色': (b32_fade, 22),
 'B32_片头': (titles.opening(BSER, VOL11, SB11, 2, '北宋 · 松烟与沈括的石油烟墨'), 7),
 'B32_片尾': (titles.closing(BSER, VOL11, SB11, 2, '下集：一件衣服，怎么只有 49 克？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
