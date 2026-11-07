"""第二十四季（古法解密 9.0）第二批：B93 独轮车、B94 鱼笱、B95 计里画方 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import rot
from s24a import SB24, VOL24, WOOD, DARKWOOD, STONE, WATER, WATER_L

LOAD = (190, 150, 100)
BAMBOO = (190, 170, 110)
FISH = (230, 150, 80)
GRIDC = (90, 100, 115)
ROOM = (200, 190, 170)
BED = (120, 150, 200)
DESK = (180, 130, 90)


# ---------------------------------------------------------------- B93 独轮车
def b93_lever(c, t, i):
    corner_tag(c, 'B93 · 轮子是支点')
    c.text(60, 96, '货离轮子越近，手上越轻：大半重量压在轮子上，人只扶着', 'serif', 40, INK)
    wx, wy, R = 420, 760, 90
    hx, hy = 1400, 620
    c.ellipse(wx, wy, R, R, outline=DARKWOOD, width=10)
    for k in range(8):
        a = k * math.pi / 4
        c.line([(wx, wy), (wx + R * math.cos(a), wy + R * math.sin(a))], DARKWOOD, 3)
    c.line([(wx, wy), (hx, hy)], WOOD, 14)
    c.line([(60, wy + R), (1860, wy + R)], (120, 100, 80), 4)
    u = 0.5 - 0.45 * math.cos(t / 22 * 2 * math.pi)
    L = math.hypot(hx - wx, hy - wy)
    d = 80 + (L - 200) * u
    lx = wx + (hx - wx) * d / L
    ly = wy + (hy - wy) * d / L
    c.rect(lx - 70, ly - 120, lx + 70, ly - 10, fill=LOAD, r=8)
    c.text(lx, ly - 65, '货', 'bold', 30, INK, 'mm')
    c.arrow(lx, ly + 10, lx, ly + 110, NRED, 5, 16)
    F = d / L
    c.arrow(hx, hy + 140 * F + 20, hx, hy + 10, GREEN, 5, 16)
    c.ellipse(hx + 30, hy - 10, 26, 26, fill=(220, 180, 150))
    c.text(hx + 70, hy + 40, '手', 'bold', 26, INK, 'lm')
    c.rect(1460, 230, 1860, 460, fill=SHEET, r=12)
    c.text(1660, 270, '手上要提的力', 'bold', 24, INK, 'mm')
    c.text(1660, 340, f'约货重的 {F * 100:.0f}%（示意）', 'mono', 26, SPARK, 'mm')
    c.rect(1500, 390, 1500 + 320 * F, 420, fill=GREEN)
    c.text(wx, wy + R + 50, '轮轴 = 支点', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '独轮车是一根杠杆：轮子着地的地方是支点，手在长长的车把尾巴上'),
                (7.2, 14, '货放得离轮子越近，手上要提的力就越小，大半重量都压在轮子上'),
                (14.2, 22, '所以推独轮车的人，总把重货堆在轮子正上方：手只管扶稳、往前推')], y=1010)


def b93_balance(c, t, i):
    corner_tag(c, 'B93 · 一个轮子怎么不倒')
    c.text(60, 96, '从后面看：货的重心要压在轮子正上方；一歪，人手一扶就回来', 'serif', 40, INK)
    for k, (nm, off, ok) in enumerate((('货压在轮子正上方', 0, True), ('货偏向一边', 90, False))):
        cx, base = 520 + k * 880, 860
        tilt = 0.08 * math.sin(t * 1.5) if ok else min(math.radians(40), (t / 22) ** 1.3 * math.radians(40))
        c.ellipse(cx, base - 60, 22, 60, fill=DARKWOOD)
        body = rot([(cx - 170, base - 140), (cx + 170, base - 140), (cx + 170, base - 120), (cx - 170, base - 120)], cx, base, tilt)
        c.poly(body, WOOD)
        bx = cx + off
        box = rot([(bx - 90, base - 300), (bx + 90, base - 300), (bx + 90, base - 140), (bx - 90, base - 140)], cx, base, tilt)
        c.poly(box, LOAD)
        g = rot([(bx, base - 220)], cx, base, tilt)[0]
        c.ellipse(g[0], g[1], 12, 12, fill=NRED)
        c.line([(g[0], g[1]), (g[0], base + 20)], NRED, 2)
        c.ellipse(cx, base + 10, 8, 8, fill=GREEN)
        c.text(cx, 260, nm, 'bold', 28, INK, 'mm')
        c.text(cx, base + 70, '小晃一下，手一扶就正' if ok else '重心线跑出轮子，越歪越快', 'sans', 24, GREEN if ok else NRED, 'mm')
    caps(c, t, [(0, 7, '一个轮子只有一个着地点，从后面看，它随时都想往左或往右倒'),
                (7.2, 14, '货的重心压在轮子正上方：歪一点点，推车的人手腕一扭就扶回来，像骑第 66 集的自行车'),
                (14.2, 22, '货偏到一边，重心线跑出了轮子，人就得一直用力往回掰，稍不留神就翻')], y=1010)


# ---------------------------------------------------------------- B94 鱼笱
def _trap(c, cx, cy, W, H, mouth, funnel=True):
    c.rect(cx - W, cy - H, cx + W, cy + H, outline=BAMBOO, width=6, r=30)
    x0 = cx - W
    c.rect(x0 - 3, cy - H, x0 + 3, cy + H, fill=BG)
    if funnel:
        c.line([(x0, cy - H), (x0 + 220, cy - mouth)], BAMBOO, 6)
        c.line([(x0, cy + H), (x0 + 220, cy + mouth)], BAMBOO, 6)


def b94_sim(c, t, i):
    corner_tag(c, 'B94 · 进去容易，出来难')
    c.text(60, 96, '两个笼子里各放 40 条乱游的鱼：出口越小，鱼越难碰上，留下的越多', 'serif', 40, INK)
    for k, funnel in enumerate((True, False)):
        cx, cy, W, H = 560 + k * 860, 560, 280, 200
        x0 = cx - W
        mouth = 30
        _trap(c, cx, cy, W, H, mouth, funnel)
        rate = 0.012 if funnel else 0.13
        N = 40
        left = N - round(N * math.exp(-rate * t))
        rnd = random.Random(20 + k)
        lim = x0 + (230 if funnel else 20)
        for j in range(N):
            fx = rnd.uniform(lim + 20, cx + W - 30)
            fy = rnd.uniform(cy - H + 25, cy + H - 25)
            ph = rnd.uniform(0, 6.28)
            if j < left:
                tl = -math.log(1 - (j + 0.5) / N) / rate if (j + 0.5) / N < 1 else 99
                age = max(0.0, t - tl)
                if age > 5:
                    continue
                x = x0 - 30 - 30 * age
                y = cy + (fy - cy) * 0.5 + 30 * math.sin(ph + age)
            else:
                x = fx + 20 * math.sin(t * 0.9 + ph)
                y = fy + 14 * math.cos(t * 1.1 + ph)
            c.ellipse(x, y, 10, 6, fill=FISH)
        c.text(cx, 250, '有笱口：出口是漏斗尖上的小口' if funnel else '没有笱口：一整面都是出口', 'bold', 26, INK, 'mm')
        c.text(cx, 840, f'还留在笼里：{N - left} / {N}', 'mono', 26, GREEN if funnel else NRED, 'mm')
    c.text(960, 900, '（按出口大小估算的示意，不是真实鱼的游法）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '两个笼子里各放 40 条东游西游的鱼，看过一会儿还剩多少'),
                (7.2, 14, '没有笱口的笼子，一整面都是出口，鱼一会儿就游光了'),
                (14.2, 22, '有笱口的笼子，出口只是漏斗尖上的一个小口，乱游的鱼很难撞上，大多留在里面；笼里放饵，鱼还会主动往里钻')], y=1010)


def b94_geom(c, t, i):
    corner_tag(c, 'B94 · 外面是漏斗，里面是迷宫')
    c.text(60, 96, '从外面看，笱口像漏斗把鱼「引」进小口；从里面看，墙都把鱼引向别处', 'serif', 40, INK)
    cx, cy, W, H = 960, 580, 600, 260
    x0 = cx - W
    mouth = 40
    _trap(c, cx, cy, W, H, mouth, True)
    p = (t % 11) / 11
    if p < 0.5:
        u = p / 0.5
        sx = x0 - 200 + 440 * u
        sy = cy + 180 * (1 - u) * (1 if u < 0.5 else 1)
        sy = cy + 180 * max(0, 1 - u * 1.2)
        c.ellipse(sx, sy, 16, 10, fill=FISH)
        c.text(x0 + 20, 280, '外面：斜墙把鱼往小口引', 'bold', 24, GREEN, 'mm')
    else:
        u = (p - 0.5) / 0.5
        ang = u * 5
        sx = cx + 200 * math.cos(ang)
        sy = cy + 150 * math.sin(ang * 1.3)
        c.ellipse(sx, sy, 16, 10, fill=FISH)
        c.text(cx + 200, 270, '里面：沿着墙游，总被引回笼子深处', 'bold', 24, NRED, 'mm')
    c.arrow(x0 - 60, cy - 220, x0 + 200, cy - 50, mix(BG, GREEN, 0.7), 3, 12)
    c.arrow(x0 - 60, cy + 220, x0 + 200, cy + 50, mix(BG, GREEN, 0.7), 3, 12)
    c.arrow(x0 + 200, cy - 80, x0 + 40, cy - 230, mix(BG, NRED, 0.7), 3, 12)
    c.arrow(x0 + 200, cy + 80, x0 + 40, cy + 230, mix(BG, NRED, 0.7), 3, 12)
    c.text(x0 + 240, cy, '小口', 'sans', 22, INK, 'lm')
    caps(c, t, [(0, 7, '笱口是一圈向里收窄的竹篾，像一个插进笼子里的漏斗'),
                (7.2, 14, '鱼从外面沿着斜墙游，墙把它一路引到小口，一钻就进去了'),
                (14.2, 22, '进了笼子，沿着墙游，墙却把它引向笼子深处；那个小口藏在漏斗尖上，很难撞到')], y=1010)


# ---------------------------------------------------------------- B95 计里画方
def b95_grid(c, t, i):
    corner_tag(c, 'B95 · 先打格子，再填地图')
    c.text(60, 96, '地上一格 50 厘米，纸上一格 1 厘米：量好每样东西占几格，照着填', 'serif', 40, INK)
    gx, gy, cell = 160, 240, 64
    nx, ny = 10, 10
    c.rect(gx, gy, gx + nx * cell, gy + ny * cell, fill=ROOM)
    for k in range(nx + 1):
        c.line([(gx + k * cell, gy), (gx + k * cell, gy + ny * cell)], GRIDC, 1)
    for k in range(ny + 1):
        c.line([(gx, gy + k * cell), (gx + nx * cell, gy + k * cell)], GRIDC, 1)
    c.rect(gx + 6 * cell, gy + 1 * cell, gx + 10 * cell, gy + 5 * cell, fill=BED)
    c.rect(gx + 0 * cell, gy + 7 * cell, gx + 3 * cell, gy + 9 * cell, fill=DESK)
    c.text(gx + 8 * cell, gy + 3 * cell, '床', 'bold', 26, INK, 'mm')
    c.text(gx + 1.5 * cell, gy + 8 * cell, '桌', 'bold', 26, INK, 'mm')
    c.text(gx + nx * cell / 2, gy - 30, '房间（一格 = 50 厘米）', 'bold', 24, INK, 'mm')
    px, py, pc = 1100, 300, 52
    c.rect(px, py, px + nx * pc, py + ny * pc, fill=SHEET)
    for k in range(nx + 1):
        c.line([(px + k * pc, py), (px + k * pc, py + ny * pc)], mix(SHEET, GRIDC, 0.6), 1)
    for k in range(ny + 1):
        c.line([(px, py + k * pc), (px + nx * pc, py + k * pc)], mix(SHEET, GRIDC, 0.6), 1)
    a = fade(t, 6, 10)
    b = fade(t, 11, 15)
    if a > 0:
        c.rect(px + 6 * pc, py + 1 * pc, px + 6 * pc + 4 * pc * a, py + 5 * pc, outline=BED, width=4)
    if b > 0:
        c.rect(px, py + 7 * pc, px + 3 * pc * b, py + 9 * pc, outline=DESK, width=4)
    c.text(px + nx * pc / 2, py - 30, '方格纸（一格 = 1 厘米）', 'bold', 24, INK, 'mm')
    if t > 15:
        c.text(px + nx * pc / 2, py + ny * pc + 50, '床：4 格 × 4 格 → 2 米 × 2 米', 'sans', 24, SPARK, 'mm')
    c.arrow(gx + nx * cell + 30, 560, px - 30, 560, MUTED, 4, 16)
    caps(c, t, [(0, 7, '先在地上按固定的距离打好格子：比如每 50 厘米贴一个记号'),
                (7.2, 14, '量一量：床占了横 4 格、竖 4 格，桌子占了 3 格乘 2 格'),
                (14.2, 22, '再到方格纸上照着格子数填进去：西晋的裴秀和元代的朱思本，就是用「计里画方」画大地图的')], y=1010)


def b95_scale(c, t, i):
    corner_tag(c, 'B95 · 一格等于多少')
    c.text(60, 96, '同样一张纸：一格代表的距离越大，画进去的地方越大，细节越少', 'serif', 40, INK)
    scales = [('一格 = 50 厘米', '一个房间', 1.0), ('一格 = 10 米', '一栋楼和院子', 0.25), ('一格 = 1 里（约 500 米）', '一座城', 0.06)]
    k = min(2, int(t / 7.3))
    nm, what, z = scales[k]
    cx, cy = 760, 600
    S = 640
    c.rect(cx - S / 2, cy - S / 2, cx + S / 2, cy + S / 2, fill=SHEET)
    rnd = random.Random(k)
    if k == 0:
        c.rect(cx + 40, cy - 220, cx + 250, cy - 10, fill=BED)
        c.rect(cx - 280, cy + 80, cx - 120, cy + 200, fill=DESK)
    elif k == 1:
        c.rect(cx - 200, cy - 200, cx + 40, cy + 60, fill=ROOM)
        for j in range(6):
            c.ellipse(rnd.uniform(cx + 80, cx + 280), rnd.uniform(cy - 250, cy + 250), 20, 20, fill=(110, 160, 90))
        c.rect(cx - 160, cy - 160, cx - 140, cy - 140, fill=BED)
    else:
        for j in range(60):
            x, y = rnd.uniform(cx - 300, cx + 280), rnd.uniform(cy - 300, cy + 280)
            c.rect(x, y, x + 18, y + 14, fill=ROOM)
        c.line([(cx - 320, cy + 40), (cx + 320, cy - 20)], WATER, 10)
    for j in range(11):
        c.line([(cx - S / 2 + j * S / 10, cy - S / 2), (cx - S / 2 + j * S / 10, cy + S / 2)], mix(SHEET, GRIDC, 0.5), 1)
        c.line([(cx - S / 2, cy - S / 2 + j * S / 10), (cx + S / 2, cy - S / 2 + j * S / 10)], mix(SHEET, GRIDC, 0.5), 1)
    c.rect(1240, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1550, 350, nm, 'bold', 30, SPARK, 'mm')
    c.text(1550, 420, f'这张纸能画下：{what}', 'sans', 26, INK, 'mm')
    c.text(1550, 500, '格子越「大」，看得越远', 'sans', 24, INK, 'mm')
    c.text(1550, 550, '格子越「小」，看得越细', 'sans', 24, INK, 'mm')
    caps(c, t, [(0, 7, '一格代表 50 厘米：一张纸刚好画下一个房间，连床和桌子都看得清'),
                (7.2, 14, '一格代表 10 米：同一张纸画下一栋楼和院子，床就只剩一个小点'),
                (14.2, 22, '一格代表一里：画下一整座城。古人的「计里画方」，就是先定好一格多少里（示意）')], y=1010)


CLIPS = {
 'B93_杠杆': (b93_lever, 22), 'B93_平衡': (b93_balance, 22),
 'B93_片头': (titles.opening(BSER, VOL24, SB24, 3, '汉代鹿车 · 传说木牛流马'), 7),
 'B93_片尾': (titles.closing(BSER, VOL24, SB24, 3, '下集：竹编的鱼笱，为什么鱼游得进去却游不出来？'), 7),
 'B94_模拟': (b94_sim, 22), 'B94_几何': (b94_geom, 22),
 'B94_片头': (titles.opening(BSER, VOL24, SB24, 4, '《诗经》「毋发我笱」'), 7),
 'B94_片尾': (titles.closing(BSER, VOL24, SB24, 4, '下集：没有卫星照片，古人怎么画出准确的地图？'), 7),
 'B95_方格': (b95_grid, 22), 'B95_比例尺': (b95_scale, 22),
 'B95_片头': (titles.opening(BSER, VOL24, SB24, 5, '西晋裴秀「制图六体」· 元代朱思本'), 7),
 'B95_片尾': (titles.closing(BSER, VOL24, SB24, 5, '下集：沙漏的沙，为什么满的时候和快漏完时流得一样快？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
