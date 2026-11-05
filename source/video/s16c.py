"""第十六季（古法解密 5.0）第三批：B56 扇车、B57 蒸笼、B58 油纸伞 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s16a import SB16, VOL16, WOOD

GRAIN = (245, 245, 235)
CHAFF = (205, 120, 60)
AIR = (120, 170, 220)
STEAM = (210, 220, 230)
BAMBOO = (200, 170, 110)
PAPER = (215, 185, 140)
WATERC = (90, 150, 210)

def fall_x(k, wind, tt):
    # horizontal drift ~ wind / (mass/area ratio)
    return wind * tt * tt * 0.5 / k

# ---------------------------------------------------------------- B56 扇车
def b56_sort(c, t, i):
    corner_tag(c, 'B56 · 风里下落')
    c.text(60, 96, '同一阵风：重的米落得近，轻的糠被吹得远', 'serif', 40, INK)
    hx, hy, ground = 360, 300, 860
    c.poly([(hx - 80, hy - 60), (hx + 80, hy - 60), (hx + 20, hy), (hx - 20, hy)], WOOD)
    for k in range(6):
        off = (t * 180 + k * 70) % 300
        c.arrow(100 + off, 300 + k * 80, 170 + off, 300 + k * 80, mix(BG, AIR, 0.6), 3, 12)
    c.text(140, 260, '风', 'bold', 28, AIR, 'mm')
    rnd = random.Random(4)
    for j in range(40):
        t0 = j * 0.35
        tt = t - t0
        if tt <= 0: continue
        heavy = j % 3 != 0
        g = 260
        y = hy + 0.5 * g * tt * tt
        k = 6.0 if heavy else 1.2
        x = hx + fall_x(k, 420, min(tt, math.sqrt(2 * (ground - hy) / g)))
        y = min(y, ground)
        x += rnd.uniform(-30, 30) * (1 if heavy else 3)
        if heavy:
            c.ellipse(x, y, 9, 6, fill=GRAIN)
        else:
            c.ellipse(x, y, 14, 4, fill=CHAFF)
    c.line([(100, ground + 10), (1800, ground + 10)], LINE, 3)
    a = fade(t, 8, 9)
    c.text(560, 920, '米：落在近处', 'bold', 26, mix(BG, GRAIN, a), 'mm')
    c.text(1250, 920, '糠、瘪谷：被吹到远处', 'bold', 26, mix(BG, CHAFF, a), 'mm')
    caps(c, t, [(0, 6, '从高处慢慢倒下米和糠，侧面一直有风吹'),
                (6.2, 13, '米又重又小，风推它的力比起它的重量不值一提，几乎直直落下'),
                (13.2, 22, '糠又轻又薄，迎风面大，被风一路带走：扇车就是一台造风、让东西在风里下落的机器')], y=1010)

def b56_speed(c, t, i):
    corner_tag(c, 'B56 · 风要刚刚好')
    c.text(60, 96, '风太小分不开，风太大连米也吹跑', 'serif', 40, INK)
    cases = [('风太小', 0.25, '米糠混在一起'), ('风刚好', 1.0, '分得最干净'), ('风太大', 2.6, '米也被吹走了')]
    for k, (nm, w, note) in enumerate(cases):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        y0 = 260 + k * 220
        c.text(140, y0, nm, 'bold', 30, mix(BG, INK, a), 'lm')
        c.line([(400, y0 + 60), (1700, y0 + 60)], mix(BG, LINE, a), 2)
        for j, (mu, col, sd) in enumerate(((120 + 180 * w, GRAIN, 50), (300 + 420 * w, CHAFF, 120))):
            mu = min(mu, 1250)
            pts = []
            for q in range(131):
                x = q * 10
                v = math.exp(-((x - mu) / sd) ** 2)
                pts.append((400 + x, y0 + 60 - 80 * v * fade(t, 1.5 + k * 4, 3 + k * 4)))
            c.line(pts, mix(BG, col, a), 4)
        c.text(1720, y0 + 20, note, 'sans', 24, mix(BG, GREEN if k == 1 else NRED, a), 'rm')
    c.text(400, 950, '落点离出口的距离 →（示意）　白：米　橙：糠', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 6, '风太小：米和糠都落在出口附近，混在一起'),
                (6.2, 13, '风刚好：米落近处，糠落远处，中间空出一段'),
                (13.2, 22, '风太大：连米也被吹走了。扇车摇得快慢，就是在找这个刚刚好（接第 40 集曲柄）')], y=1010)

# ---------------------------------------------------------------- B57 蒸笼
def b57_latent(c, t, i):
    corner_tag(c, 'B57 · 蒸汽为什么比开水烫')
    c.text(60, 96, '1 克水蒸气变回水，放出的热比把水烧开还多', 'serif', 40, INK)
    rows = [('1 克水从 0 度烧到 100 度', 418, (90, 150, 210), 1), ('1 克 100 度水蒸气凝结成水', 2260, SPARK, 5)]
    for k, (nm, J, col, t0) in enumerate(rows):
        a = fade(t, t0, t0 + 1)
        if a <= 0: continue
        y = 330 + k * 220
        w = 1300 * J / 2260 * fade(t, t0 + 0.5, t0 + 3)
        c.text(160, y - 60, nm, 'bold', 28, mix(BG, INK, a), 'lm')
        c.rect(160, y - 20, 160 + w, y + 40, fill=mix(BG, col, a), r=8)
        c.text(180 + w, y + 10, f'约 {J} 焦耳', 'mono', 28, mix(BG, INK, a), 'lm')
    d = fade(t, 11, 12)
    c.rect(160, 720, 1760, 860, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 765, '蒸汽碰到冷的包子、冷的竹屉，就在上面凝结：一下放出大量的热', 'bold', 28, mix(BG, INK, d), 'mm')
    c.text(960, 815, '所以被蒸汽烫伤比被开水烫伤更严重：揭蒸笼盖一定要避开脸', 'sans', 24, mix(BG, NRED, d), 'mm')
    caps(c, t, [(0, 6, '把 1 克水从冰点烧到沸点，要大约 418 焦耳'),
                (6.2, 13, '可 1 克水蒸气凝结回水，会一下放出大约 2260 焦耳：五倍多'),
                (13.2, 22, '这叫汽化热（潜热）。蒸笼加热靠的不是热空气，而是蒸汽在冷东西上凝结')], y=1010)

def b57_layers(c, t, i):
    corner_tag(c, 'B57 · 蒸汽一层层往上走')
    c.text(60, 96, '下层先热到 100 度，蒸汽才轮到上层', 'serif', 40, INK)
    x0, y0 = 220, 300
    for k in range(3):
        y = y0 + k * 150
        c.rect(x0, y, x0 + 520, y + 120, outline=BAMBOO, width=8, r=12)
        c.text(x0 + 260, y + 60, ['上层', '中层', '下层'][k], 'bold', 28, INK, 'mm')
    c.rect(x0 - 30, y0 + 450, x0 + 550, y0 + 560, fill=MUTED, r=10)
    c.text(x0 + 260, y0 + 505, '锅里的开水', 'sans', 24, BG, 'mm')
    front = min(3.0, max(0, (t - 2) / 4))
    for j in range(20):
        u = ((t * 0.6 + j * 0.13) % 1)
        lvl = u * 3
        if lvl > front: continue
        yy = y0 + 450 - lvl * 150
        xx = x0 + 40 + (j * 37) % 440
        c.ellipse(xx, yy, 10, 10, fill=mix(BG, STEAM, 0.8))
    # temperature curves
    gx, gy, W, H = 1000, 820, 760, 460
    c.line([(gx, gy), (gx + W, gy)], LINE, 2)
    c.line([(gx, gy), (gx, gy - H)], LINE, 2)
    c.text(gx + W, gy + 40, '时间 →', 'sans', 22, MUTED, 'rm')
    c.text(gx - 10, gy - H, '100°', 'mono', 22, MUTED, 'rm')
    c.line([(gx, gy - H + 20), (gx + W, gy - H + 20)], mix(BG, LINE, 0.6), 1)
    for k, (col, delay) in enumerate(((NRED, 0.0), (SPARK, 1.0), (GREEN, 2.0))):
        pts = []
        for q in range(101):
            u = q / 100 * 4.5
            if u > (t - 1) / 4: break
            temp = 20 + 80 * (1 / (1 + math.exp(-(u - 1 - delay) * 3)))
            pts.append((gx + u / 4.5 * W, gy - (temp - 0) / 100 * (H - 20)))
        if len(pts) > 1:
            c.line(pts, col, 4)
    c.text(gx + 20, gy - H - 30, '红：下层　黄：中层　绿：上层（示意）', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 6, '蒸汽先碰到下层的冷东西，凝结、放热，把下层先烧到接近 100 度'),
                (6.2, 13, '下层热透了，蒸汽不再在那里凝结，就继续往上，轮到中层、再到上层'),
                (13.2, 22, '所以上层只是晚一点，最后都能到 100 度：只要锅里的水一直开着（以实测为准）')], y=1010)

# ---------------------------------------------------------------- B58 油纸伞
def b58_contact(c, t, i):
    corner_tag(c, 'B58 · 水珠趴着还是站着')
    c.text(60, 96, '同一滴水：在白纸上摊开，在油纸上缩成小球', 'serif', 40, INK)
    for k, (nm, ang, col) in enumerate((('白纸', 25, NRED), ('刷了油的纸', 115, GREEN))):
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        cx, base = 520 + k * 880, 620
        c.rect(cx - 340, base, cx + 340, base + 40, fill=mix(BG, PAPER, a))
        th = math.radians(ang)
        R = 160 if ang < 90 else 110
        if ang < 90:
            hgt = R * (1 - math.cos(th))
            half = R * math.sin(th) * 1.6
            pts = [(cx - half + 2 * half * q / 40, base - hgt * math.sin(math.pi * q / 40)) for q in range(41)]
            c.poly(pts + [(cx + half, base), (cx - half, base)], mix(BG, WATERC, a))
            soak = fade(t, 3, 8)
            c.rect(cx - half, base, cx + half, base + 40 * soak, fill=mix(PAPER, WATERC, 0.5 * a))
        else:
            c.ellipse(cx, base - R * 0.75, R, R * 0.9, fill=mix(BG, WATERC, a))
        c.text(cx, 300, nm, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(cx, 760, f'接触角约 {ang}°（示意）', 'mono', 26, mix(BG, col, a), 'mm')
    d = fade(t, 13, 14)
    c.text(960, 860, '水和纸「亲」：摊开、钻进去；水和油「不亲」：缩成球、滚走', 'bold', 26, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 6, '水滴在白纸上，一下就摊开，接着往纸里渗'),
                (6.2, 13, '同一滴水落在刷过油的纸上，缩成一颗圆圆的小球'),
                (13.2, 22, '水珠和纸面的夹角叫接触角：角度大于 90 度，水就站着不趴下，一倾斜就滚走')], y=1010)

def b58_pores(c, t, i):
    corner_tag(c, 'B58 · 把纸里的缝堵上、包上')
    c.text(60, 96, '纸是一团纤维，中间全是缝：油把缝填满，还给纤维穿上雨衣', 'serif', 38, INK)
    rnd = random.Random(8)
    fibers = [(rnd.uniform(0, 1), rnd.uniform(0, 1), rnd.uniform(0, math.pi)) for _ in range(26)]
    for k, (nm, oiled) in enumerate((('白纸：缝是空的', False), ('油纸：缝被油填满', True))):
        a = fade(t, 1 + k * 6, 2 + k * 6)
        if a <= 0: continue
        x0, y0 = 160 + k * 880, 260
        if oiled:
            c.rect(x0, y0, x0 + 720, y0 + 480, fill=mix(BG, (200, 170, 90), 0.5 * a), r=10)
        else:
            c.rect(x0, y0, x0 + 720, y0 + 480, outline=mix(BG, LINE, a), width=2, r=10)
        for fx, fy, q in fibers:
            xa, ya = x0 + 40 + fx * 640, y0 + 40 + fy * 400
            c.line([(xa, ya), (xa + 120 * math.cos(q), ya + 120 * math.sin(q) * 0.5)], mix(BG, PAPER, a), 8)
        c.text(x0 + 360, y0 - 75, nm, 'bold', 28, mix(BG, INK, a), 'mm')
        prog = fade(t, 3 + k * 6, 7 + k * 6)
        if not oiled:
            for j in range(10):
                xx = x0 + 60 + j * 65
                c.line([(xx, y0 - 10), (xx + 10, y0 + 40 + 380 * prog)], mix(BG, WATERC, a), 5)
            c.text(x0 + 360, y0 + 540, '水顺着缝钻进去（毛细作用）', 'sans', 24, mix(BG, NRED, a), 'mm')
        else:
            for j in range(6):
                xx = x0 + 80 + j * 110
                c.ellipse(xx + 60 * prog, y0 - 18, 20, 18, fill=mix(BG, WATERC, a))
            c.text(x0 + 360, y0 + 540, '水进不去，只能在表面滚走', 'sans', 24, mix(BG, GREEN, a), 'mm')
    caps(c, t, [(0, 6, '纸由无数细纤维搭成，纤维之间全是细缝：水顺着细缝钻进去，这就是 B45 讲过的毛细作用'),
                (6.2, 14, '刷上桐油，油渗进缝里、包住纤维；晾干后桐油变硬，像给纸穿了一层透明雨衣'),
                (14.2, 22, '缝堵上了，表面又不亲水：雨点只能滚走。所以油纸伞要刷匀、晾透（桐油由成年人操作）')], y=1010)

CLIPS = {
 'B56_风选': (b56_sort, 22), 'B56_风速': (b56_speed, 22),
 'B56_片头': (titles.opening(BSER, VOL16, SB16, 6, '西汉 · 扇车'), 7),
 'B56_片尾': (titles.closing(BSER, VOL16, SB16, 6, '下集：叠了好几层的蒸笼，为什么最上面也能蒸熟？'), 7),
 'B57_潜热': (b57_latent, 22), 'B57_层层': (b57_layers, 22),
 'B57_片头': (titles.opening(BSER, VOL16, SB16, 7, '新石器时代 · 陶甑'), 7),
 'B57_片尾': (titles.closing(BSER, VOL16, SB16, 7, '下集：一张纸，刷了油怎么就不怕雨？'), 7),
 'B58_接触角': (b58_contact, 22), 'B58_填缝': (b58_pores, 22),
 'B58_片头': (titles.opening(BSER, VOL16, SB16, 8, '桐油纸伞'), 7),
 'B58_片尾': (titles.closing(BSER, VOL16, SB16, 8, '下集：为什么犁辕要做成弯的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
