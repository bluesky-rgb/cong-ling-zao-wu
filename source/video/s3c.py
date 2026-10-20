"""第三季第三批：E34 净水、B12 冰鉴与藏冰、E38 蒸发冷却罐 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s3a import S3A, SER3, VOL3, WATER
from s3b import SB3, SOIL

ICE = (210, 235, 245)
STRAW = (210, 180, 100)
BRONZE = (150, 120, 80)
HOT = (236, 120, 48)

# ---------------------------------------------------------------- E34 净水
RF = random.Random(34)
PART = [(RF.uniform(-1, 1), RF.random(), RF.choice([0, 0, 1, 1, 2, 3])) for _ in range(90)]
LAYERS = [('石子', 330, 420, (130, 130, 130), 0), ('粗沙', 420, 520, (190, 160, 110), 1), ('细沙', 520, 640, (220, 200, 150), 2), ('木炭', 640, 740, (50, 46, 44), 3), ('纱布', 740, 770, (230, 230, 230), 4)]

def e34_filter(c, t, i):
    corner_tag(c, '第 34 集 · 过滤')
    c.text(60, 96, '一层层沙石，能把水变干净吗？', 'serif', 40, INK)
    cx, w = 620, 220
    c.rect(cx - w - 8, 250, cx + w + 8, 790, outline=MUTED, width=5, r=10)
    for name, y0, y1, col, _ in LAYERS:
        c.rect(cx - w, y0, cx + w, y1, fill=col)
        c.text(cx + w + 30, (y0 + y1) / 2, name, 'sans', 26, INK, 'lm')
    # particles falling: size class decides where they stop
    stops = [400, 500, 620, 720, 1000]
    for k, (u, ph, cls) in enumerate(PART):
        prog = (t * 0.18 + ph) % 1.0
        y = 230 + prog * 700
        stop = stops[cls]
        if y > stop: y = stop - 6 - (k % 4) * 5
        x = cx + u * (w - 20)
        if cls == 3:   # microbes: pass through
            y = 230 + prog * 780
            c.ellipse(x, y, 4, 4, fill=(120, 220, 120))
        else:
            r = [12, 8, 5][cls]
            c.ellipse(x, y, r, r, fill=(150, 110, 70) if cls < 2 else (190, 160, 120))
    c.rect(cx - 160, 810, cx + 160, 940, outline=MUTED, width=4, r=8)
    c.rect(cx - 154, 850, cx + 154, 936, fill=mix(BG, FIELD, 0.5))
    # legend / panel
    px = 1180
    c.rect(px, 230, 1860, 800, fill=SHEET, r=16)
    items = [((150, 110, 70), 12, '泥块、树叶：被石子和粗沙挡住'), ((190, 160, 120), 5, '细泥：被细沙挡住'), ((50, 46, 44), 10, '异味、颜色：被木炭吸附'), ((120, 220, 120), 4, '细菌：大多直接穿过去')]
    for k, (col, r, s_) in enumerate(items):
        y = 300 + k * 90
        a = fade(t, 1 + k * 3, 2 + k * 3)
        c.ellipse(px + 50, y, r + 2, r + 2, fill=mix(BG, col, a))
        c.text(px + 90, y, s_, 'sans', 28, mix(BG, INK if k < 3 else NRED, a), 'lm')
    a = fade(t, 14, 15)
    c.text(px + 40, 700, '变清了 ≠ 能喝了', 'bold', 40, mix(BG, COPPER, a), 'lm')
    caps(c, t, [(0, 7, '浑水从上往下穿过石子、粗沙、细沙、木炭'),
                (7.2, 14, '颗粒越往下越小，被一层层截住；木炭还能吸走一些异味和颜色'),
                (14.2, 22, '可细菌比沙缝小得多，大多直接漏了下去')])

def e34_sodis(c, t, i):
    corner_tag(c, '第 34 集 · 晒水消毒')
    c.text(60, 96, '把一瓶水放在太阳下晒，为什么能消毒？', 'serif', 40, INK)
    # sun
    c.ellipse(220, 230, 70, 70, fill=SPARK)
    # bottle lying
    bx0, by0, bx1, by1 = 300, 560, 1060, 700
    c.rect(bx0, by0, bx1, by1, outline=(200, 210, 220), width=5, r=40)
    c.rect(bx1, by0 + 40, bx1 + 60, by1 - 40, fill=(80, 140, 200), r=6)
    c.rect(bx0 + 8, by0 + 8, bx1 - 8, by1 - 8, fill=mix(BG, FIELD, 0.35), r=34)
    c.text((bx0 + bx1) / 2, by1 + 40, '透明塑料瓶（PET，1–2 升），平放', 'sans', 24, MUTED, 'mm')
    for k in range(6):
        ph = (t * 0.8 + k / 6) % 1
        x = 300 + k * 140; y = 300 + ph * 240
        c.line([(x - 20, y - 40), (x, y)], mix(BG, (180, 140, 255), 1 - ph * 0.5), 4)
    c.text(700, 260, '紫外线（UV-A）', 'sans', 26, (180, 140, 255), 'mm')
    # microbes inside die over time
    kill = fade(t, 4, 16)
    R = random.Random(3)
    for k in range(18):
        x = R.uniform(bx0 + 40, bx1 - 40); y = R.uniform(by0 + 30, by1 - 30)
        alive = (k / 18) > kill
        col = (120, 220, 120) if alive else (90, 90, 90)
        c.ellipse(x, y, 10, 6, fill=col)
        if not alive:
            c.line([(x - 8, y - 6), (x + 8, y + 6)], NRED, 2)
    # thermometer & clock
    T = 25 + 25 * fade(t, 2, 16)
    c.rect(1180, 240, 1860, 820, fill=SHEET, r=16)
    c.text(1210, 290, f'水温约 {T:.0f} ℃（晴天，示意）', 'mono', 28, HOT, 'lm')
    h = 6 * fade(t, 2, 16)
    c.text(1210, 350, f'已经晒了 {h:.1f} 小时', 'mono', 28, INK, 'lm')
    rows = [('晴天或少云', '6 小时'), ('多云', '连晒 2 天'), ('一直下雨', '不能用')]
    for k, (a_, b_) in enumerate(rows):
        y = 450 + k * 60
        c.text(1210, y, a_, 'sans', 26, INK, 'lm'); c.text(1600, y, b_, 'bold', 26, COPPER, 'lm')
    c.text(1210, 660, '紫外线破坏微生物的 DNA', 'sans', 24, INK, 'lm')
    c.text(1210, 700, '超过 50 ℃ 时，热和紫外线一起作用，快得多', 'sans', 24, INK, 'lm')
    c.text(1210, 760, '前提：水要先过滤到比较清', 'bold', 24, NRED, 'lm')
    caps(c, t, [(0, 6, '过滤后的水装进透明塑料瓶，平放在太阳底下'),
                (6.2, 14, '紫外线穿过瓶子，破坏细菌的 DNA；水温升高，又帮了一把'),
                (14.2, 22, '世界卫生组织认可的办法叫 SODIS：晴天晒满 6 小时')])

# ---------------------------------------------------------------- B12 冰鉴与藏冰
def b12_icehouse(c, t, i):
    corner_tag(c, 'B12 · 凌阴')
    c.text(60, 96, '冬天的冰，怎么撑到夏天？', 'serif', 40, INK)
    G = 380
    c.rect(0, G, 1100, 1080, fill=SOIL)
    c.rect(0, 300, 1100, G, fill=mix(BG, HOT, 0.12))
    c.text(60, 330, '夏天地面 35 ℃', 'bold', 28, HOT, 'lm')
    straw = fade(t, 6, 9)
    px0, px1, py0, py1 = 250, 850, 520, 940
    c.rect(px0 - 40 * straw, py0 - 40 * straw, px1 + 40 * straw, py1 + 10, fill=mix(SOIL, STRAW, straw))
    melt = fade(t, 1, 22) * (1 - 0.75 * straw)
    for r in range(4):
        for q in range(6):
            x = px0 + 20 + q * 96; y = py0 + 20 + r * 100
            s = 80 * (1 - 0.6 * melt)
            c.rect(x, y + (80 - s), x + s, y + 80, fill=ICE, r=6)
    if melt > 0.1:
        c.rect(px0, py1 - 30 * melt, px1, py1, fill=mix(BG, FIELD, 0.7))
    # heat arrows
    n_arrows = 6
    for k in range(n_arrows):
        ph = (t * 0.7 + k / n_arrows) % 1
        L = 120 * (1 - 0.7 * straw)
        x = px0 + 40 + k * 100
        c.arrow(x, G + 10, x, G + 10 + L * ph + 20, mix(BG, HOT, 0.9), 4, 12)
    c.text(560, 340, '热量从地面往下钻', 'sans', 26, HOT, 'lm')
    if straw > 0.5:
        c.text(px1 + 70, 600, '稻草层', 'bold', 28, STRAW, 'lm')
        c.text(px1 + 70, 640, '里面全是不流动的空气', 'sans', 24, INK, 'lm')
        c.text(px1 + 70, 675, '热传得很慢', 'sans', 24, INK, 'lm')
    # latent heat panel
    a = fade(t, 13, 14)
    px = 1200
    c.rect(px, 230, 1860, 600, fill=mix(BG, SHEET, a), r=16)
    c.text(px + 30, 280, '冰为什么「耐化」？', 'bold', 30, mix(BG, INK, a), 'lm')
    c.text(px + 30, 350, '化掉 1 千克冰要的热量', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(px + 30, 395, '≈ 把 1 千克水从 0 ℃ 加热到 80 ℃', 'bold', 28, mix(BG, COPPER, a), 'lm')
    c.text(px + 30, 470, '冰越多、越挤在一起，', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(px + 30, 515, '表面积越小，化得越慢', 'sans', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '冬天从河里凿冰，放进地下的冰窖：古人叫「凌阴」'),
                (6.2, 13, '冰的四周、上下塞满稻草：稻草里全是不流动的空气，热量传得很慢'),
                (13.2, 22, '再加上冰本身「耐化」：深埋、厚盖、大块堆放，冰就能撑到夏天')])

def b12_jian(c, t, i):
    corner_tag(c, 'B12 · 冰鉴')
    c.text(60, 96, '两千四百年前的「冰箱」', 'serif', 40, INK)
    cx = 640
    # outer 鉴
    c.rect(cx - 360, 360, cx + 360, 900, fill=BRONZE, r=20)
    c.rect(cx - 330, 390, cx + 330, 880, fill=mix(BG, ICE, 0.35), r=14)
    melt = fade(t, 3, 18)
    for k in range(10):
        x = cx - 310 + (k % 5) * 130 if k < 5 else cx - 310 + (k % 5) * 130
        y = 420 if k < 5 else 820
        if k % 5 in (1, 2, 3) and k < 5: continue
        s = 60 * (1 - 0.5 * melt)
        c.rect(x, y, x + s, y + s * 0.8, fill=ICE, r=6)
    for k, y in enumerate([480, 560, 640, 720]):
        for x in (cx - 310, cx + 250):
            s = 60 * (1 - 0.5 * melt)
            c.rect(x, y, x + s, y + s * 0.8, fill=ICE, r=6)
    # inner 缶 with wine
    c.rect(cx - 200, 300, cx + 200, 800, fill=(120, 96, 70), r=40)
    Tw = 30 - 18 * fade(t, 3, 18)
    c.rect(cx - 170, 380, cx + 170, 780, fill=mix((150, 80, 60), (110, 80, 140), fade(t, 3, 18) * 0.3), r=30)
    c.text(cx, 560, '酒', 'serif', 56, INK, 'mm')
    c.text(cx, 630, f'{Tw:.0f} ℃（示意）', 'mono', 28, INK, 'mm')
    for k in range(4):
        ph = (t * 0.8 + k / 4) % 1
        y = 450 + k * 90
        c.arrow(cx + 170, y, cx + 170 + 120 * ph + 10, y, mix(BG, HOT, 0.9), 4, 12)
        c.arrow(cx - 170, y, cx - 170 - 120 * ph - 10, y, mix(BG, HOT, 0.9), 4, 12)
    c.text(cx, 330, '方缶：装酒', 'sans', 24, INK, 'mm')
    c.text(cx, 940, '方鉴：夹层里放冰', 'sans', 26, INK, 'mm')
    px = 1180
    c.rect(px, 260, 1860, 760, fill=SHEET, r=16)
    c.text(px + 30, 310, '曾侯乙墓铜鉴缶', 'bold', 30, INK, 'lm')
    c.text(px + 30, 360, '1978 年湖北随县出土 · 战国早期', 'sans', 24, MUTED, 'lm')
    c.text(px + 30, 440, '外面一个方鉴，里面套一个方缶', 'sans', 26, INK, 'lm')
    c.text(px + 30, 490, '缶里装酒，夹层放冰', 'sans', 26, INK, 'lm')
    c.text(px + 30, 570, '热量从酒流进冰：', 'sans', 26, INK, 'lm')
    c.text(px + 30, 615, '冰化了，酒凉了', 'bold', 28, COPPER, 'lm')
    c.text(px + 30, 690, '冬天也能反过来放热水温酒', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 7, '外面一个方鉴，里面套一个方缶'),
                (7.2, 14, '夹层里塞满冰：热量从酒里流出，被冰吸走'),
                (14.2, 20, '这不是冷藏柜，而是一只冰镇酒的「冰桶」')])

# ---------------------------------------------------------------- E38 蒸发冷却罐
RM = random.Random(38)
MOL = [(RM.uniform(-1, 1), RM.uniform(0, 1), RM.uniform(0.3, 1.6)) for _ in range(70)]

def e38_evap(c, t, i):
    corner_tag(c, '第 38 集 · 蒸发吸热')
    c.text(60, 96, '水蒸发，为什么会变凉？', 'serif', 40, INK)
    cx, top, bot = 640, 520, 920
    c.rect(cx - 420, top, cx + 420, bot, fill=mix(BG, FIELD, 0.3), r=10)
    c.line([(cx - 420, top), (cx + 420, top)], FIELD, 3)
    escaped = 0
    for k, (u, ph, sp) in enumerate(MOL):
        x0 = cx + u * 390
        fast = sp > 1.25
        if fast and t > 3:
            prog = ((t - 3) * 0.35 * sp + ph) % 1
            y = top - prog * 360
            c.ellipse(x0, y, 9, 9, fill=mix(BG, NRED, 1 - prog * 0.6))
        else:
            y = top + 30 + ph * (bot - top - 60) + 10 * math.sin(t * sp * 2 + k)
            col = mix(FIELD, NRED, (sp - 0.3) / 1.3 * (1 if t < 3 else 0.7))
            c.ellipse(x0 + 12 * math.sin(t * sp + k), y, 9, 9, fill=col)
    c.text(cx + 420, top + 30 + (bot - top), '', 'sans', 26, NRED, 'rm')
    c.text(cx - 420, 190, '红：跑得快的分子　蓝：跑得慢的分子', 'sans', 26, MUTED, 'lm')
    T = 25 - 4 * fade(t, 4, 16)
    px = 1180
    c.rect(px, 240, 1860, 820, fill=SHEET, r=16)
    c.text(px + 30, 290, f'剩下的水：约 {T:.1f} ℃（示意）', 'mono', 30, FIELD, 'lm')
    c.text(px + 30, 370, '温度 = 分子平均跑得多快', 'sans', 26, INK, 'lm')
    c.text(px + 30, 420, '最快的飞走了，留下的平均变慢', 'sans', 26, INK, 'lm')
    c.text(px + 30, 470, '→ 水变凉了', 'bold', 28, COPPER, 'lm')
    c.text(px + 30, 560, '蒸发 1 克水带走约 2400 焦热量', 'sans', 26, INK, 'lm')
    c.text(px + 30, 605, '是融化 1 克冰的 7 倍多', 'bold', 26, COPPER, 'lm')
    c.text(px + 30, 690, '出汗凉快，也是这个道理', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 4, '水里的分子跑得有快有慢'),
                (4.2, 12, '只有跑得最快的，才能挣脱水面，变成水蒸气飞走'),
                (12.2, 22, '快的走了，剩下的平均更慢：温度就降下来了')])

def zeer(c, cx, cy, wet, evap, t, label):
    c.rect(cx - 220, cy - 220, cx + 220, cy + 220, fill=(170, 110, 80), r=40)
    c.rect(cx - 200, cy - 200, cx + 200, cy + 200, fill=mix((200, 180, 140), (120, 100, 80), wet), r=34)
    c.rect(cx - 120, cy - 150, cx + 120, cy + 190, fill=(176, 120, 86), r=24)
    c.rect(cx - 104, cy - 130, cx + 104, cy + 174, fill=(60, 50, 44), r=18)
    c.text(cx, cy + 20, '食物', 'sans', 26, INK, 'mm')
    n = int(10 * evap)
    for k in range(n):
        ph = (t * 0.6 + k / max(1, n)) % 1
        for side in (-1, 1):
            x = cx + side * (230 + ph * 120); y = cy - 160 + (k * 37) % 320
            c.ellipse(x, y, 6, 6, fill=mix(BG, (200, 210, 230), 1 - ph))
    c.text(cx, cy - 270, label, 'bold', 30, INK, 'mm')

def e38_humid(c, t, i):
    corner_tag(c, '第 38 集 · 湿度')
    c.text(60, 96, '同一个罐子，为什么在干燥的地方更凉？', 'serif', 40, INK)
    a = fade(t, 1, 2)
    zeer(c, 480, 560, 0.9, 1.0, t, '干燥（相对湿度 30%）')
    zeer(c, 1440, 560, 0.9, 0.25, t, '潮湿（相对湿度 85%）')
    d1 = 8 * fade(t, 3, 12); d2 = 2 * fade(t, 3, 12)
    for cx, d, col in ((480, d1, FIELD), (1440, d2, MUTED)):
        c.text(cx, 840, f'罐内比外面低约 {d:.0f} ℃（示意）', 'mono', 28, col, 'mm')
    c.text(960, 920, '小罐套大罐，中间填湿沙，上面盖湿布', 'sans', 26, MUTED, 'mm')
    caps(c, t, [(0, 7, '小罐套大罐，中间湿沙里的水从外罐表面蒸发，带走热量'),
                (7.2, 14, '空气越干燥，水蒸发得越快，罐里越凉'),
                (14.2, 20, '空气已经很潮湿，水就蒸发不动了 —— 南方梅雨天它几乎没用')], y=1010)

# ---------------------------------------------------------------- 片头片尾
CLIPS = {
 'E34_过滤': (e34_filter, 22), 'E34_晒水消毒': (e34_sodis, 22),
 'E34_片头': (titles.opening(SER3, VOL3, S3A, 5, '北宋 · 约公元 1090 年 · 人们还不知道细菌'), 7),
 'E34_片尾': (titles.closing(SER3, VOL3, S3A, 5, '下集：冬天的冰，怎么撑到夏天？'), 7),
 'B12_凌阴': (b12_icehouse, 22), 'B12_冰鉴': (b12_jian, 20),
 'B12_片头': (titles.opening(BSER, BVOL, SB3, 1, '先秦凌阴 · 战国曾侯乙铜鉴缶'), 7),
 'B12_片尾': (titles.closing(BSER, BVOL, SB3, 1, '下集：没有冰，也能降温'), 7),
 'E38_蒸发吸热': (e38_evap, 22), 'E38_湿度': (e38_humid, 20),
 'E38_片头': (titles.opening(SER3, VOL3, S3A, 6, '北宋 · 约公元 1090 年 · 一只不用电的「冰箱」'), 7),
 'E38_片尾': (titles.closing(SER3, VOL3, S3A, 6, '下集：不懂基因，怎么改良品种？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
