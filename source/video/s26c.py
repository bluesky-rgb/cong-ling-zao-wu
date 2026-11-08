"""第二十六季（古法解密 10.0：担、桥、风、律）第三批：B106 方升、B107 三分损益、B108 鼓 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import SB26, VOL26, BAMBOO, WOOD, WATER, WATER_L

BRONZE = (190, 140, 80)
GRAIN = (230, 210, 150)
SKIN_D = (225, 200, 160)
STRING = (230, 230, 210)


# ---------------------------------------------------------------- B106 方升
def b106_volume(c, t, i):
    corner_tag(c, 'B106 · 先定尺寸，再算容积')
    c.text(60, 96, '方升的尺寸刻在铜器上：长 × 宽 × 高，就是它能装多少；形状不同，只要算出来一样，装的就一样多', 'serif', 36, INK)
    fill = min(1, max(0, (t % 11) / 7))
    # 长方体（斜二测）
    x0, y0, w, h, d = 260, 760, 320, 300, 140
    def box(level):
        c.poly([(x0, y0), (x0 + w, y0), (x0 + w + d * 0.6, y0 - d * 0.5), (x0 + d * 0.6, y0 - d * 0.5)], mix(BG, BRONZE, 0.25))
        hh = h * level
        if hh > 1:
            c.rect(x0, y0 - hh, x0 + w, y0, fill=mix(BG, GRAIN, 0.8))
            c.poly([(x0, y0 - hh), (x0 + w, y0 - hh), (x0 + w + d * 0.6, y0 - hh - d * 0.5), (x0 + d * 0.6, y0 - hh - d * 0.5)], GRAIN)
        c.line([(x0, y0), (x0, y0 - h), (x0 + w, y0 - h), (x0 + w, y0)], BRONZE, 5)
        c.line([(x0, y0 - h), (x0 + d * 0.6, y0 - h - d * 0.5), (x0 + w + d * 0.6, y0 - h - d * 0.5), (x0 + w, y0 - h)], BRONZE, 5)
        c.line([(x0 + w, y0), (x0 + w + d * 0.6, y0 - d * 0.5), (x0 + w + d * 0.6, y0 - h - d * 0.5)], BRONZE, 5)
    box(fill)
    c.text(x0 + w / 2, y0 + 50, '长方体：8 × 8 × 7.8 厘米', 'sans', 24, INK, 'mm')
    c.text(x0 + w / 2, y0 + 90, '≈ 499 立方厘米', 'mono', 24, SPARK, 'mm')
    cx, cy, R, H = 1060, 760, 150, 300
    hh = H * fill
    c.ellipse(cx, cy, R, R * 0.3, fill=mix(BG, BRONZE, 0.25))
    if hh > 1:
        c.rect(cx - R, cy - hh, cx + R, cy, fill=mix(BG, GRAIN, 0.8))
        c.ellipse(cx, cy, R, R * 0.3, fill=mix(BG, GRAIN, 0.8))
        c.ellipse(cx, cy - hh, R, R * 0.3, fill=GRAIN)
    c.line([(cx - R, cy), (cx - R, cy - H)], BRONZE, 5)
    c.line([(cx + R, cy), (cx + R, cy - H)], BRONZE, 5)
    c.ellipse(cx, cy - H, R, R * 0.3, outline=BRONZE, width=5)
    c.text(cx, cy + 70, '圆柱：直径 8 × 高 10 厘米', 'sans', 24, INK, 'mm')
    c.text(cx, cy + 110, '≈ 503 立方厘米', 'mono', 24, SPARK, 'mm')
    c.rect(1380, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 340, '量杯检查', 'bold', 24, INK, 'mm')
    c.rect(1560, 400, 1680, 600, outline=LINE, width=3)
    c.rect(1564, 596 - 180 * fill, 1676, 596, fill=mix(BG, WATER_L, 0.7))
    c.text(1700, 420, '500 毫升', 'mono', 18, MUTED, 'lm')
    c.line([(1680, 416), (1696, 416)], MUTED, 2)
    caps(c, t, [(0, 7, '量米、量酒，各地的「升」要是不一样大，买卖就没法公平'),
                (7.2, 14, '商鞅方升把尺寸刻在铜器上：长乘宽乘高，就是一升的容积（具体数值拍摄前核对）'),
                (14.2, 22, '形状不重要：长方体、圆柱，只要算出来的体积一样，倒进去的米就一样多（示意）')], y=1010)


def b106_standard(c, t, i):
    corner_tag(c, 'B106 · 照着标准做，误差就小了')
    c.text(60, 96, '凭感觉做的「一升」五花八门；照着刻好尺寸的标准器复制，大家的「一升」就挤在了一起', 'serif', 38, INK)
    rnd = random.Random(9)
    guess = [rnd.gauss(500, 110) for _ in range(40)]
    copy = [rnd.gauss(500, 12) for _ in range(40)]
    k = min(40, int(t / 0.25))
    for row, (data, lab, col) in enumerate(((guess, '凭感觉做', NRED), (copy, '照着标准器做', GREEN))):
        gy = 420 + row * 330
        c.text(140, gy - 140, lab, 'bold', 26, INK, 'lm')
        c.line([(240, gy), (1680, gy)], LINE, 2)
        for v in (200, 300, 400, 500, 600, 700, 800):
            x = 240 + (v - 200) / 600 * 1440
            c.line([(x, gy), (x, gy + 10)], LINE, 2)
            c.text(x, gy + 30, f'{v}', 'mono', 16, MUTED, 'mm')
        x5 = 240 + 300 / 600 * 1440
        seg(c, [(x5, gy - 120), (x5, gy)], mix(BG, SPARK, 0.6), 2)
        stacks = {}
        for v in data[:k]:
            b = int((min(799, max(200, v)) - 200) // 15)
            n = stacks.get(b, 0)
            stacks[b] = n + 1
            x = 240 + (b * 15 + 7.5) / 600 * 1440
            c.ellipse(x, gy - 10 - n * 12, 6, 6, fill=col)
    c.text(1760, 300, '500 毫升', 'mono', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '让 40 个人凭感觉剪一个「装 500 毫升」的盒子，有的大一倍，有的只有一半（数据为示意）'),
                (7.2, 14, '换一种办法：先做一个尺寸精确的标准器，把尺寸刻上去，大家都照着它做'),
                (14.2, 22, '结果全都挤在 500 附近：今天的千克、米，也都靠同一个办法——统一的标准（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B107 三分损益
def b107_string(c, t, i):
    corner_tag(c, 'B107 · 弦长变成三分之二，音高一个五度')
    c.text(60, 96, '弦越短，振得越快，声音越高：去掉三分之一，频率变成 1.5 倍——两个音一起响，特别和谐', 'serif', 38, INK)
    for row, (frac, lab) in enumerate(((1.0, '全长 L：宫'), (2 / 3, '三分之二 L：高一个五度'))):
        gy = 360 + row * 300
        x0 = 220
        Lp = 1200
        x1 = x0 + Lp * frac
        c.rect(x0 - 20, gy - 40, x0, gy + 40, fill=WOOD)
        c.rect(x1, gy - 40, x1 + 20, gy + 40, fill=WOOD)
        if frac < 1:
            seg(c, [(x1 + 20, gy), (x0 + Lp, gy)], mix(BG, STRING, 0.3), 2)
        f = 1.0 / frac
        amp = 40 * math.sin(t * 6 * f)
        pts = [(x0 + (x1 - x0) * j / 60, gy + amp * math.sin(math.pi * j / 60)) for j in range(61)]
        c.line(pts, STRING, 4)
        c.text(x0, gy - 80, lab, 'bold', 24, INK, 'lm')
        c.text(1500, gy, f'频率 × {f:.2f}', 'mono', 28, SPARK if frac < 1 else INK, 'lm')
    gy = 880
    c.text(220, gy - 70, '两个音的波形叠在一起（示意）：每 2 下对 3 下，规整地对齐', 'sans', 22, MUTED, 'lm')
    pts1 = [(220 + j * 3, gy + 30 * math.sin(j * 0.06 + t)) for j in range(480)]
    pts2 = [(220 + j * 3, gy + 30 * math.sin(j * 0.09 + t * 1.5)) for j in range(480)]
    c.line(pts1, mix(BG, INK, 0.6), 2)
    c.line(pts2, SPARK, 2)
    caps(c, t, [(0, 7, '同一根弦，用手指按住三分之二的地方再弹，声音高了一截'),
                (7.2, 14, '弦短了，振得就快：长度变成三分之二，频率正好变成一点五倍'),
                (14.2, 22, '一个振 2 下、另一个振 3 下，又对齐了：这样的两个音一起响，耳朵觉得特别和谐，叫「五度」')], y=1010)


PENT = [(81, '宫'), (54, '徵'), (72, '商'), (48, '羽'), (64, '角')]


def b107_ladder(c, t, i):
    corner_tag(c, 'B107 · 去三分之一，加三分之一')
    c.text(60, 96, '从 81 开始：乘三分之二、再乘三分之四，轮流算下去，就得到宫、徵、商、羽、角五个音', 'serif', 38, INK)
    k = min(5, int(t / 3.2) + 1)
    x0, base = 260, 820
    c.line([(200, base), (1300, base)], LINE, 2)
    for j, (L, nm) in enumerate(PENT[:k]):
        x = x0 + j * 200
        hgt = L * 7
        a = fade(t, j * 3.2, j * 3.2 + 1)
        c.rect(x, base - hgt, x + 120, base, fill=mix(BG, BAMBOO, 0.4 + 0.6 * a), r=6)
        c.text(x + 60, base - hgt - 30, f'{L}', 'mono', 26, INK, 'mm')
        c.text(x + 60, base + 34, nm, 'bold', 30, SPARK, 'mm')
        if j > 0:
            op = '× 2/3' if j % 2 == 1 else '× 4/3'
            c.text(x - 40, base - hgt - 90, op, 'mono', 22, GREEN if j % 2 == 1 else (120, 170, 230), 'mm')
            c.arrow(x - 80, base - PENT[j - 1][0] * 7 - 50, x + 20, base - hgt - 60, MUTED, 2, 10)
    if t > 16:
        a = fade(t, 16, 17)
        c.rect(1380, 260, 1860, 820, fill=mix(BG, SHEET, a), r=14)
        c.text(1620, 300, '按长短排一排', 'bold', 24, mix(BG, INK, a), 'mm')
        srt = sorted(PENT, key=lambda p: -p[0])
        for j, (L, nm) in enumerate(srt):
            y = 370 + j * 86
            c.rect(1420, y - 24, 1420 + L * 4.5, y + 24, fill=mix(BG, BAMBOO, a), r=4)
            c.text(1800, y, nm, 'bold', 28, mix(BG, SPARK, a), 'mm')
        c.text(1620, 800, '宫 商 角 徵 羽：越短越高', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '《管子》里写：把黄钟的长度定为 81，去掉三分之一得 54，再加上三分之一得 72……（原文拍摄前核对）'),
                (7.2, 14, '一减一加，轮流算：81、54、72、48、64，正好都是整数'),
                (14.2, 22, '按长短排好，就是宫、商、角、徵、羽五个音；一直算下去，能得到十二个音，叫十二律（示意）')], y=1010)


# ---------------------------------------------------------------- B108 鼓
def b108_tension(c, t, i):
    corner_tag(c, 'B108 · 绷得越紧，振得越快')
    c.text(60, 96, '鼓皮像一张弹簧床：绷得越紧，被敲下去以后弹回来越快，每秒振的次数越多，声音越高', 'serif', 38, INK)
    for row, (ten, lab) in enumerate(((1.0, '轻绷'), (2.25, '绷紧'))):
        cx = 480 + row * 760
        cy = 560
        R = 240
        f = math.sqrt(ten)
        tt = t % 5.5
        amp = 60 * math.exp(-tt / 1.6) * math.cos(tt * 7 * f)
        c.rect(cx - R - 10, cy, cx + R + 10, cy + 200, fill=mix(BG, WOOD, 0.8), r=12)
        pts = [(cx - R + 2 * R * j / 60, cy + amp * math.cos(math.pi * (j / 60 - 0.5))) for j in range(61)]
        c.line(pts, SKIN_D, 8)
        c.text(cx, cy + 250, lab, 'bold', 28, INK, 'mm')
        gx0 = cx - 260
        gy = 330
        trace = []
        for j in range(201):
            s = tt - 2 + 2 * j / 200
            v = 0 if s < 0 else math.exp(-s / 1.6) * math.cos(s * 7 * f)
            trace.append((gx0 + 520 * j / 200, gy - 60 * v))
        c.line(trace, GREEN, 2)
        c.text(cx, 230, f'频率 × {f:.1f}', 'mono', 26, SPARK if row else INK, 'mm')
        if tt < 0.3:
            c.ellipse(cx, cy - 80, 14, 14, fill=SPARK)
    caps(c, t, [(0, 7, '鼓槌一敲，鼓皮被按下去，又弹回来，来回振动，推着空气发出声音'),
                (7.2, 14, '皮绷得越紧，把它拉回来的力越大，振得越快：张力变成 2.25 倍，频率变成 1.5 倍'),
                (14.2, 22, '鼓越小、皮越薄，声音也越高；鼓身那个空腔，让声音更响、更长（示意，以实测为准）')], y=1010)


def b108_salt(c, t, i):
    corner_tag(c, 'B108 · 撒一把盐，看见振动')
    c.text(60, 96, '鼓面上撒盐：振得厉害的地方把盐粒弹开，盐粒慢慢聚到几乎不动的地方，画出一圈圈「节线」', 'serif', 36, INK)
    cx, cy, R = 700, 580, 340
    c.ellipse(cx, cy, R, R, fill=mix(BG, SKIN_D, 0.25))
    c.ellipse(cx, cy, R, R, outline=WOOD, width=10)
    mode = 0 if t < 11 else 1
    rnd = random.Random(4)
    prog = min(1, ((t % 11)) / 7)
    for k in range(260):
        r0 = R * math.sqrt(rnd.random()) * 0.96
        a0 = rnd.uniform(0, 2 * math.pi)
        if mode == 0:
            tr = R * 0.55
            r = r0 + (tr - r0) * prog
            a = a0
        else:
            tr = R * 0.55
            r = r0 + (tr - r0) * prog * 0.5
            na = round(a0 / math.pi) * math.pi + math.pi / 2
            near = (a0 % math.pi) - math.pi / 2
            a = a0 - near * prog if abs(r0 - tr) > R * 0.25 else a0
            if abs(r0 - tr) <= R * 0.25:
                r = r0 + (tr - r0) * prog
        jit = (1 - prog) * 6 * math.sin(t * 40 + k)
        c.ellipse(cx + r * math.cos(a) + jit, cy + r * math.sin(a) + jit, 4, 4, fill=(245, 245, 245))
    if prog > 0.9:
        c.ellipse(cx, cy, R * 0.55, R * 0.55, outline=mix(BG, SPARK, 0.6), width=2)
        if mode == 1:
            seg(c, [(cx, cy - R), (cx, cy + R)], mix(BG, SPARK, 0.6), 2)
    c.rect(1180, 300, 1840, 760, fill=SHEET, r=14)
    c.text(1510, 340, '这一次的振法（示意）', 'bold', 24, INK, 'mm')
    c.text(1510, 420, '一圈节线' if mode == 0 else '一圈 + 一条直线', 'bold', 30, SPARK, 'mm')
    c.text(1510, 500, '敲的位置、旁边的声音不同，', 'sans', 22, INK, 'mm')
    c.text(1510, 540, '盐粒会画出不同的图案', 'sans', 22, INK, 'mm')
    c.text(1510, 620, '图案以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '在蒙好的气球鼓面上撒一小撮盐，旁边用勺子敲锅盖，或者放一段低音'),
                (7.2, 14, '鼓面振得厉害的地方把盐粒弹起来，盐粒慢慢挪到几乎不动的地方停下'),
                (14.2, 22, '那些不动的线叫「节线」：一面鼓同时有好几种振法，混在一起就是鼓的音色（图案为示意）')], y=1010)


CLIPS = {
 'B106_容积': (b106_volume, 22), 'B106_标准': (b106_standard, 22),
 'B106_片头': (titles.opening(BSER, VOL26, SB26, 6, '战国商鞅方升'), 7),
 'B106_片尾': (titles.closing(BSER, VOL26, SB26, 6, '下集：古人没有频率计，怎么定出一套好听的音阶？'), 7),
 'B107_弦长': (b107_string, 22), 'B107_损益': (b107_ladder, 22),
 'B107_片头': (titles.opening(BSER, VOL26, SB26, 7, '《管子 · 地员》三分损益法'), 7),
 'B107_片尾': (titles.closing(BSER, VOL26, SB26, 7, '下集：同一面鼓，为什么皮绷得越紧声音越高？'), 7),
 'B108_张力': (b108_tension, 22), 'B108_撒盐': (b108_salt, 22),
 'B108_片头': (titles.opening(BSER, VOL26, SB26, 8, '山西陶寺遗址出土鼍鼓'), 7),
 'B108_片尾': (titles.closing(BSER, VOL26, SB26, 8, '下集：几块版印一张彩色画，颜色怎么对得严丝合缝？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
