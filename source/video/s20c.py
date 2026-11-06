"""第二十季（古法解密 7.0）第三批：B76 石磨、B77 拓印、B78 毛笔 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s20a import SB20, VOL20, WOOD

STONE = (140, 140, 145)
BEAN = (230, 200, 120)
INKC = (25, 25, 30)
PAPER = (235, 228, 210)
HAIR = (190, 160, 110)

# ---------------------------------------------------------------- B76 石磨
def _grooves(c, cx, cy, R, rot, col, w=3):
    for k in range(8):
        a0 = rot + k * math.pi / 4
        for j in range(5):
            off = (j - 2) * 18
            # 每个扇区里一组平行于扇区边的斜线
            ux, uy = math.cos(a0 + 0.35), math.sin(a0 + 0.35)
            nx, ny = -uy, ux
            sx, sy = cx + math.cos(a0 + math.pi / 8) * 60 + nx * off, cy + math.sin(a0 + math.pi / 8) * 60 + ny * off
            pts = [(sx + ux * s, sy + uy * s) for s in (0, R * 0.75)]
            p0, p1 = pts
            if math.hypot(p1[0] - cx, p1[1] - cy) > R - 6:
                f = (R - 6) / math.hypot(p1[0] - cx, p1[1] - cy)
                p1 = (cx + (p1[0] - cx) * f, cy + (p1[1] - cy) * f)
            c.line([p0, p1], col, w)

GR = [(random.Random(k).uniform(0, 6.283), random.Random(k + 99).uniform(40, 60)) for k in range(60)]

def b76_grooves(c, t, i):
    corner_tag(c, 'B76 · 斜齿一边剪一边推')
    c.text(60, 96, '磨盘上的齿分成八区，斜着走；上扇一转，碎末顺着齿往外跑', 'serif', 40, INK)
    cx, cy, R = 640, 580, 360
    c.ellipse(cx, cy, R, R, fill=STONE, outline=INK, width=4)
    rot = t * 0.5
    _grooves(c, cx, cy, R, 0, mix(STONE, BG, 0.45), 4)
    _grooves(c, cx, cy, R, -rot, mix(STONE, (230, 230, 235), 0.5), 2)
    c.ellipse(cx, cy, 40, 40, fill=BG)
    c.text(cx, cy, '磨眼', 'sans', 18, MUTED, 'mm')
    for k, (a0, r0) in enumerate(GR):
        tt = (t * 0.9 + k * 0.37) % 6
        r = r0 + (R - r0) * (tt / 6) ** 1.2
        a = a0 + 0.9 * tt
        col = mix(BEAN, (245, 245, 235), tt / 6)
        size = 9 - 6 * tt / 6
        c.ellipse(cx + r * math.cos(a), cy + r * math.sin(a), size, size, fill=col)
    for k in range(10):
        a = k * 0.63 + t * 0.2
        c.ellipse(cx + (R + 30 + 20 * ((t + k) % 2)) * math.cos(a), cy + (R + 30) * math.sin(a), 5, 5, fill=(245, 245, 235))
    c.rect(1200, 320, 1840, 700, fill=SHEET, r=14)
    c.text(1520, 370, '上扇和下扇的齿', 'bold', 28, INK, 'mm')
    c.text(1520, 440, '方向相同，转起来像剪刀交错', 'sans', 24, INK, 'mm')
    c.text(1520, 500, '豆子在中间越剪越碎', 'sans', 24, INK, 'mm')
    c.text(1520, 560, '碎末顺着斜齿被推到边上', 'sans', 24, INK, 'mm')
    c.text(1520, 640, '浅色：上扇的齿　深色：下扇的齿', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '豆子从上扇中间的磨眼漏下去，落进两扇石头之间'),
                (7.2, 14, '两扇石头都刻着分区的斜齿；上扇一转，上下的齿一次次交错，像剪刀一样切'),
                (14.2, 22, '斜齿还像螺旋一样，把切碎的豆末一点点推向边缘：所以豆浆自己从磨边流出来')], y=1010)

def b76_shear(c, t, i):
    corner_tag(c, 'B76 · 剖面：一上一下像剪刀')
    c.text(60, 96, '上扇的齿划过下扇的齿：夹在中间的豆子被一刀刀切小', 'serif', 40, INK)
    y0 = 560
    off = (t * 120) % 120
    c.rect(100, y0 - 220, 1820, y0 - 30, fill=STONE)
    for k in range(-1, 16):
        x = 100 + k * 120 + off
        c.poly([(x, y0 - 30), (x + 60, y0 - 30), (x + 30, y0 + 10)], STONE)
    c.rect(100, y0 + 30, 1820, y0 + 220, fill=mix(STONE, BG, 0.2))
    for k in range(15):
        x = 100 + k * 120
        c.poly([(x, y0 + 30), (x + 60, y0 + 30), (x + 30, y0 - 10)], mix(STONE, BG, 0.2))
    c.arrow(800, y0 - 260, 1100, y0 - 260, SPARK, 5, 16)
    c.text(950, y0 - 290, '上扇转动', 'sans', 24, SPARK, 'mm')
    stage = min(4, int(t / 4))
    sizes = [60, 34, 20, 11, 6]
    s = sizes[stage]
    rnd = random.Random(stage)
    n = 2 ** stage
    for k in range(min(n, 20)):
        x = 300 + rnd.uniform(0, 1300)
        c.ellipse(x, y0, s, s * 0.7, fill=BEAN)
    c.rect(560, 830, 1360, 940, fill=SHEET, r=12)
    c.text(960, 885, f'第 {stage + 1} 次交错：颗粒约 {s / 6:.0f} 份大（示意）', 'mono', 26, INK, 'mm')
    caps(c, t, [(0, 7, '从侧面切开看：上下两扇的齿都是斜面，一转，上齿的刃口划过下齿的刃口'),
                (7.2, 14, '夹在中间的豆子被切开、碾碎，每转一圈都要被切很多次'),
                (14.2, 22, '磨盘越重压得越紧，磨得越细；齿磨平了，就要请石匠重新「锻磨」')], y=1010)

# ---------------------------------------------------------------- B77 拓印
def b77_relief(c, t, i):
    corner_tag(c, 'B77 · 凸处受墨，凹处留白')
    c.text(60, 96, '纸贴紧碑面，墨只拍在凸起的地方：刻进去的字就留白', 'serif', 40, INK)
    y0 = 520
    prof = []
    for x in range(140, 1100, 4):
        dep = 60 if (300 < x < 380 or 520 < x < 580 or 700 < x < 820 or 900 < x < 950) else 0
        prof.append((x, y0 + dep))
    c.poly(prof + [(1100, 800), (140, 800)], STONE)
    press = fade(t, 2, 6)
    paper = [(x, y0 - 30 + (y - y0 + 30) * press - 6 * (1 - press)) for x, y in prof]
    c.line(paper, PAPER, 5)
    dab = fade(t, 7, 14)
    if dab > 0:
        bx = 140 + 960 * dab
        c.ellipse(bx, y0 - 90, 60, 40, fill=(80, 70, 60))
        c.text(bx, y0 - 150, '拓包', 'sans', 22, MUTED, 'mm')
        for (x, y) in prof:
            if x < bx and y == y0:
                c.line([(x, y - 3), (x + 4, y - 3)], (70, 70, 80), 8)
    c.text(620, 860, '剖面：碑上刻进去的笔画是凹的', 'sans', 22, MUTED, 'mm')
    a = fade(t, 14, 15)
    if a > 0:
        c.rect(1240, 300, 1800, 760, fill=mix(BG, (60, 60, 68), a), outline=mix(BG, MUTED, a), width=2, r=8)
        for (x0, x1) in ((300, 380), (520, 580), (700, 820), (900, 950)):
            X0 = 1240 + (x0 - 140) * 560 / 960; X1 = 1240 + (x1 - 140) * 560 / 960
            c.rect(X0, 380, X1, 680, fill=mix(BG, PAPER, a))
        c.text(1520, 800, '揭下来：黑底白字', 'bold', 28, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '湿纸贴在碑上，用刷子轻轻捶打，让纸嵌进刻痕里'),
                (6.2, 14, '纸半干时，用包着棉花的拓包蘸墨，轻轻拍：只有贴在平面上的纸沾到墨'),
                (14.2, 22, '刻进去的笔画里的纸碰不到墨，揭下来就是黑底白字，大小、方向和碑上一模一样')], y=1010)

GLYPH = [((0, 0), (0, 4)), ((0, 2), (2, 2)), ((0, 0), (2, 0)), ((2, 2), (2.6, 3.2))]

def _glyph(c, x, y, s, col, mirror=False, w=10):
    for (a, b) in GLYPH:
        ax = -a[0] if mirror else a[0]; bx = -b[0] if mirror else b[0]
        c.line([(x + ax * s, y + a[1] * s), (x + bx * s, y + b[1] * s)], col, w)

def b77_mirror(c, t, i):
    corner_tag(c, 'B77 · 拓印是正的，印章是反的')
    c.text(60, 96, '拓印：纸蒙在字上，方向不变；印章、活字：刻成反的，印出来才正', 'serif', 40, INK)
    cols = [('碑上的字（凹）', '拓出来', False, False), ('印章上的字（反刻）', '盖出来', True, False)]
    for k, (n1, n2, mir, _) in enumerate(cols):
        a = fade(t, 1 + k * 7, 2 + k * 7)
        if a <= 0: continue
        x0 = 260 + k * 820
        c.text(x0 + 140, 280, n1, 'bold', 26, mix(BG, INK, a), 'mm')
        c.rect(x0, 320, x0 + 280, 600, fill=mix(BG, STONE, a), r=8)
        _glyph(c, x0 + (190 if mir else 80), 380, 45, mix(BG, (90, 90, 95), a), mir)
        c.arrow(x0 + 300, 460, x0 + 400, 460, mix(BG, MUTED, a), 4, 14)
        c.text(x0 + 560, 280, n2, 'bold', 26, mix(BG, INK, a), 'mm')
        if k == 0:
            c.rect(x0 + 420, 320, x0 + 700, 600, fill=mix(BG, INKC, a), r=4)
            _glyph(c, x0 + 500, 380, 45, mix(BG, PAPER, a), False)
        else:
            c.rect(x0 + 420, 320, x0 + 700, 600, fill=mix(BG, PAPER, a), r=4)
            _glyph(c, x0 + 500, 380, 45, mix(BG, NRED, a), False)
    b = fade(t, 15, 16)
    if b > 0:
        c.rect(360, 700, 1560, 900, fill=mix(BG, SHEET, b), r=14)
        c.text(960, 750, '拓印 = 给碑「照相」：一张拓片只拓一次', 'sans', 26, mix(BG, INK, b), 'mm')
        c.text(960, 810, '印刷 = 反刻一块版，可以印成千上万张（B3 活字）', 'sans', 26, mix(BG, INK, b), 'mm')
        c.text(960, 860, '有人认为拓印是雕版印刷的先声（拍摄前核对）', 'sans', 22, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 7, '拓印时纸是蒙在字上面的，纸的正面朝外：拓出来的字方向不变'),
                (7.2, 15, '印章和活字是把纸压在字上面，像照镜子：所以要把字刻反，印出来才是正的'),
                (15.2, 22, '一个是复制已经刻好的碑，一个是为了印很多张而专门反刻：两条路后来走到了一起')], y=1010)

# ---------------------------------------------------------------- B78 毛笔
def b78_tip(c, t, i):
    corner_tag(c, 'B78 · 一蘸水就收成尖')
    c.text(60, 96, '干笔的毛是散的；蘸水一提，水的表面张力把毛拉拢成尖', 'serif', 40, INK)
    cx, top = 760, 300
    wet = fade(t, 6, 11)
    c.rect(cx - 40, top - 80, cx + 40, top + 180, fill=WOOD, r=8)
    c.rect(cx - 46, top + 160, cx + 46, top + 200, fill=(120, 90, 60))
    for k in range(29):
        u = (k - 14) / 14
        spread = 1.0 - 0.85 * wet
        x_end = cx + u * 230 * spread
        y_end = top + 620 - abs(u) * (40 + 120 * wet)
        pts = [(cx + u * 40 + (x_end - cx - u * 40) * s + 25 * (1 - wet) * math.sin(k + s * 3) * s, top + 200 + (y_end - top - 200) * s) for s in [j / 20 for j in range(21)]]
        c.line(pts, mix(HAIR, (60, 50, 40), wet * 0.7), 3)
    if 4 < t < 9:
        c.rect(cx - 200, top + 520, cx + 200, 880, fill=mix(BG, (80, 140, 200), 0.5), r=10)
        c.text(cx + 220, top + 600, '蘸水', 'sans', 24, MUTED, 'lm')
    a = fade(t, 12, 13)
    if a > 0:
        c.rect(1200, 320, 1840, 700, fill=mix(BG, SHEET, a), r=14)
        c.text(1520, 370, '笔的四德', 'bold', 30, mix(BG, INK, a), 'mm')
        for k, (w_, d) in enumerate((('尖', '收得拢、出得尖'), ('齐', '压开后锋毫齐平'), ('圆', '笔肚饱满圆润'), ('健', '有弹性，压下能弹回'))):
            c.text(1280, 440 + k * 60, w_, 'bold', 28, mix(BG, SPARK, a), 'lm')
            c.text(1340, 440 + k * 60, d, 'sans', 24, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '一支没用过的毛笔，毛是蓬开的'),
                (6.2, 12, '蘸了水往上一提：水在毛和毛之间形成一层层薄膜，表面张力把它们往一起拉'),
                (12.2, 22, '毛就收成一个尖。好笔讲究「尖、齐、圆、健」：尖靠的是毛的形状，也靠水')], y=1010)

def b78_capillary(c, t, i):
    corner_tag(c, 'B78 · 毛缝里存墨')
    c.text(60, 96, '毛和毛之间的细缝像细管子：缝越细，墨吸得越高、存得越稳', 'serif', 40, INK)
    base = 820
    for k, (nm, gap) in enumerate((('宽缝', 60), ('中缝', 30), ('细缝', 14))):
        x0 = 220 + k * 330
        h = 3000 / gap * fade(t, 1, 6)
        c.rect(x0 - 140, base, x0 + 140 + 0, base + 60, fill=(70, 85, 140))
        c.rect(x0 - gap / 2, base - h, x0 + gap / 2, base + 30, fill=(70, 85, 140))
        for s in (-1, 1):
            c.rect(x0 + s * gap / 2 - (14 if s < 0 else 0), base - 480, x0 + s * gap / 2 + (0 if s < 0 else 14), base + 30, fill=HAIR)
        c.text(x0, base + 100, nm, 'bold', 26, INK, 'mm')
    c.text(550, 230, '墨在缝里升起的高度（示意，蓝色为墨）', 'sans', 22, MUTED, 'mm')
    a = fade(t, 9, 10)
    if a > 0:
        ink = 1 - 0.85 * fade(t, 10, 20)
        c.rect(1240, 300, 1840, 620, fill=mix(BG, SHEET, a), r=14)
        c.text(1540, 340, '写一笔', 'bold', 28, mix(BG, INK, a), 'mm')
        L = 520 * fade(t, 10, 20)
        pts = [(1280 + s, 460 + 30 * math.sin(s / 60)) for s in range(0, int(L) + 1, 6)]
        if len(pts) > 1:
            for j in range(len(pts) - 1):
                w = max(2, int(16 * (1 - j / max(len(pts), 1) * 0.6)))
                c.line([pts[j], pts[j + 1]], mix(BG, (70, 85, 140), a), w)
            c.line(pts, mix(BG, (200, 200, 200), a * 0.3), 1)
        c.rect(1280, 560, 1280 + 520 * ink, 590, fill=mix(BG, GREEN, a), r=6)
        c.text(1540, 650, '笔里剩下的墨', 'sans', 22, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '一支毛笔有成百上千根毛，毛和毛之间留着很细的缝'),
                (7.2, 14, '墨被这些细缝吸住，缝越细吸得越牢：这叫毛细作用，和第 26 集虹吸、灯芯吸油是一回事'),
                (14.2, 22, '写字时笔尖一压，墨才一点点放出来：所以一笔能写很长，又不会一下子滴成一团')], y=1010)


CLIPS = {
 'B76_斜齿': (b76_grooves, 22), 'B76_剪切': (b76_shear, 22),
 'B76_片头': (titles.opening(BSER, VOL20, SB20, 6, '战国转磨 · 汉代石磨'), 7),
 'B76_片尾': (titles.closing(BSER, VOL20, SB20, 6, '下集：石碑上的字，怎么原样「搬」到纸上？'), 7),
 'B77_凸凹': (b77_relief, 22), 'B77_正反': (b77_mirror, 22),
 'B77_片头': (titles.opening(BSER, VOL20, SB20, 7, '东汉熹平石经 · 唐代拓本'), 7),
 'B77_片尾': (titles.closing(BSER, VOL20, SB20, 7, '下集：一撮软软的毛，怎么写出又尖又韧的笔画？'), 7),
 'B78_收尖': (b78_tip, 22), 'B78_存墨': (b78_capillary, 22),
 'B78_片头': (titles.opening(BSER, VOL20, SB20, 8, '战国楚墓毛笔 · 蒙恬造笔（传）'), 7),
 'B78_片尾': (titles.closing(BSER, VOL20, SB20, 8, '下集：宋代的球，为什么一定要「打气」？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
