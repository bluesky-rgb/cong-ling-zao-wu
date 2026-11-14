"""第四十九季（第二十一层：浴室）第二批：E255 镜子起雾、E256 毛巾、E257 浴帘 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s49a import S49A, SER49, VOL49, WATER

GLASS = (170, 200, 220)
CLOTH = (200, 120, 120)
CURTAIN = (180, 200, 230)
STEAM = (220, 225, 235)


# ---------------------------------------------------------------- E255 镜子起雾
def e255_drops(c, t, i):
    corner_tag(c, '第 255 集 · 凉镜面上凝成小水珠')
    c.text(60, 96, '热水冒出的水汽碰到凉镜子，冷下来变回一颗颗小水珠；每颗水珠都把光往四面八方散开，镜子就看不清了', 'serif', 36, INK)
    mx0, mx1, my0, my1 = 900, 1700, 220, 900
    c.rect(mx0, my0, mx1, my1, fill=mix(BG, GLASS, 0.5), r=10)
    c.text((mx0 + mx1) / 2, (my0 + my1) / 2, '镜', 'serif', 220, mix(BG, INK, 0.8), 'mm')
    ph = min(1.0, t / 14)
    random.seed(5)
    for k in range(int(600 * ph)):
        x = random.uniform(mx0 + 10, mx1 - 10)
        y = random.uniform(my0 + 10, my1 - 10)
        r = random.uniform(4, 10)
        c.ellipse(x, y, r, r, fill=mix(BG, STEAM, 0.9))
    for k in range(18):
        f = ((t * 0.3) + k / 18) % 1
        x = 200 + f * 680
        y = 800 - 300 * math.sin(f * math.pi) * 0.6 - k * 4
        c.ellipse(x, y, 10, 10, outline=mix(BG, STEAM, 0.8), width=2)
    c.rect(150, 820, 500, 900, fill=mix(BG, WATER, 0.6), r=20)
    c.text(325, 940, '热水（≤50 ℃）', 'bold', 24, INK, 'mm')
    if t > 14:
        x, y = 1300, 560
        for a in range(8):
            ang = a * math.pi / 4
            c.arrow(x, y, x + 80 * math.cos(ang), y + 80 * math.sin(ang), SPARK, 3, 10)
        c.ellipse(x, y, 20, 20, fill=mix(BG, STEAM, 1.0))
    caps(c, t, [(0, 7, '热水不停地冒出看不见的水汽'),
                (7.2, 14, '水汽碰到凉的镜面，冷下来变回水，凝成一颗颗小水珠'),
                (14.2, 22, '每颗小水珠像一个小透镜，把光往四面八方散开：镜子就花了')], y=1010)


def e255_film(c, t, i):
    corner_tag(c, '第 255 集 · 洗洁精让水铺成平膜')
    c.text(60, 96, '抹过洗洁精的镜面，水汽凝下来不再缩成小水珠，而是铺成一层平平的水膜，光能直直穿过，照得清', 'serif', 36, INK)
    random.seed(8)
    for j, (lab, film) in enumerate([('没抹：一颗颗小水珠', False), ('抹了洗洁精：一层平水膜', True)]):
        cx = 480 + j * 960
        c.rect(cx - 360, 260, cx + 360, 760, fill=mix(BG, GLASS, 0.5), r=10)
        c.text(cx, 510, '镜', 'serif', 200, mix(BG, INK, 0.8), 'mm')
        if film:
            c.rect(cx - 360, 260, cx + 360, 760, outline=mix(BG, WATER, 0.9), width=6, r=10)
        else:
            for k in range(500):
                c.ellipse(cx + random.uniform(-350, 350), random.uniform(270, 750), 7, 7, fill=mix(BG, STEAM, 0.9))
        sx, sy = cx - 200, 860
        if film:
            c.rect(sx - 60, sy - 6, sx + 160, sy + 6, fill=mix(BG, WATER, 0.9), r=6)
        else:
            c.ellipse(sx + 50, sy - 30, 50, 40, fill=mix(BG, WATER, 0.9))
        c.line([(sx - 80, sy + 8), (sx + 180, sy + 8)], mix(BG, INK, 0.6), 4)
        c.text(cx + 120, sy - 10, '水滴侧面', 'sans', 22, MUTED, 'lm')
        c.text(cx, 950, lab, 'bold', 26, GREEN if film else NRED, 'mm')
    caps(c, t, [(0, 7, '没抹的镜面：水缩成一颗颗圆圆的小水珠'),
                (7.2, 14, '洗洁精让水在镜面上铺开，小水珠连成一片'),
                (14.2, 22, '平平的水膜不散射光，镜子还照得清；冷镜子起雾也更多（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E256 毛巾
def e256_loops(c, t, i):
    corner_tag(c, '第 256 集 · 成千上万个小线圈')
    c.text(60, 96, '光滑的布表面是平的；毛巾表面立着成千上万个小线圈，线圈和线圈之间、纤维和纤维之间，全是窄窄的缝', 'serif', 36, INK)
    for j, (lab, loops) in enumerate([('光滑棉布：平平的', False), ('毛巾：立着一个个小线圈', True)]):
        cx, by = 480 + j * 960, 700
        c.rect(cx - 380, by, cx + 380, by + 40, fill=mix(BG, CLOTH, 1.0))
        if loops:
            for k in range(19):
                x = cx - 360 + k * 40
                h = 120 + 20 * math.sin(k * 1.7)
                c.arc(x + 15, by - h / 2, 18, h / 2, 180, 360, mix(BG, CLOTH, 1.0), 6)
                c.line([(x - 3, by - h / 2), (x - 3, by)], mix(BG, CLOTH, 1.0), 6)
                c.line([(x + 33, by - h / 2), (x + 33, by)], mix(BG, CLOTH, 1.0), 6)
        else:
            for k in range(30):
                x = cx - 370 + k * 25
                c.line([(x, by - 4), (x + 18, by - 4)], mix(BG, CLOTH, 0.7), 4)
        ph = (t % 7) / 7
        for k in range(10 if loops else 3):
            x = cx - 300 + k * 64
            y = by - 300 + 260 * min(1.0, ph * 1.4)
            if loops or y < by - 20:
                c.ellipse(x, min(y, by - 20), 10, 12, fill=mix(BG, WATER, 1.0))
        c.text(cx, 900, lab, 'bold', 26, GREEN if loops else NRED, 'mm')
    caps(c, t, [(0, 7, '同样大小、同样重的两块布'),
                (7.2, 14, '毛巾的线圈让表面多出很多很多，能碰到水的地方也多得多'),
                (14.2, 22, '线圈之间、纤维之间的窄缝，就是吸水的「小管子」（示意）')], y=1010)


def e256_climb(c, t, i):
    corner_tag(c, '第 256 集 · 水顺着窄缝往上爬')
    c.text(60, 96, '两条布下端插进色素水：水顺着纤维之间的窄缝自己往上爬（毛细作用），毛巾条爬得又快又高', 'serif', 36, INK)
    c.rect(300, 780, 1620, 900, fill=mix(BG, WATER, 0.5), r=10)
    tt = min(t, 20)
    for j, (lab, k) in enumerate([('光滑棉布', 0.55), ('毛巾', 1.0)]):
        x = 640 + j * 640
        top = 260
        c.rect(x - 70, top, x + 70, 840, fill=mix(BG, CLOTH, 0.5))
        h = 480 * k * math.sqrt(tt / 20)
        c.rect(x - 70, 840 - h, x + 70, 840, fill=mix(BG, (90, 120, 200), 0.9))
        c.text(x, 220, lab, 'bold', 28, GREEN if k > 0.8 else INK, 'mm')
        c.text(x + 100, 840 - h, f'{h / 48:.1f} 厘米', 'bold', 24, INK, 'lm')
    c.text(960, 960 - 20, f'{int(tt / 2)} 分钟（示意，以实测为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '纤维之间的窄缝，水会被吸着往上爬，不用人推'),
                (7.2, 14, '毛巾的线圈多、缝多，水爬得更快、更高'),
                (14.2, 22, '拿出来一称，毛巾条吸的水也多得多')], y=1010)


# ---------------------------------------------------------------- E257 浴帘
def e257_flow(c, t, i):
    corner_tag(c, '第 257 集 · 淋浴带起一股气流')
    c.text(60, 96, '淋浴的水往下冲，拖着身边的空气一起往下，在浴帘里面转成一个圈：里面的空气在流动，气压就比外面低一点', 'serif', 36, INK)
    cx = 760
    c.rect(cx - 30, 200, cx + 30, 250, fill=mix(BG, (175, 185, 195), 1.0), r=6)
    random.seed(4)
    for k in range(40):
        f = ((t * 1.2) + k / 40) % 1
        x = cx + random.uniform(-80, 80) + f * random.uniform(-40, 40)
        c.ellipse(x, 260 + f * 620, 4, 8, fill=mix(BG, WATER, 1.0))
    for k in range(16):
        a = t * 1.2 + k * math.pi / 8
        x = cx + 360 + 200 * math.cos(a)
        y = 560 + 300 * math.sin(a)
        c.ellipse(x, y, 6, 6, fill=SPARK)
    c.arrow(cx + 360 + 200, 560, cx + 360 + 200, 500, SPARK, 4, 12)
    c.line([(1360, 220), (1360 + 20 * math.sin(t), 900)], mix(BG, CURTAIN, 1.0), 8)
    c.text(1400, 300, '浴帘', 'bold', 26, INK, 'lm')
    c.text(1150, 940, '帘子里：空气在转（气压低一点）', 'bold', 24, SPARK, 'mm')
    c.text(1700, 600, '外面：\n空气不动', 'bold', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '水流往下冲，把旁边的空气也拖着往下走'),
                (7.2, 14, '空气在帘子里面转成一个圈，一直在流动'),
                (14.2, 22, '流动的空气，气压比静止的空气低一点（示意）')], y=1010)


def e257_push(c, t, i):
    corner_tag(c, '第 257 集 · 外面的空气把帘子推进来')
    c.text(60, 96, '帘子里面气压低，外面气压高：外面的空气推着浴帘往里飘；两张纸中间一吹，纸也会往中间靠', 'serif', 36, INK)
    ph = min(1.0, (t % 11) / 6)
    bend = 160 * ph
    pts = [(700 - bend * math.sin(math.pi * k / 20), 220 + 34 * k) for k in range(21)]
    seg(c, pts, mix(BG, CURTAIN, 1.0), 10)
    for k in range(5):
        y = 320 + k * 120
        c.arrow(940, y, 790 - bend * math.sin(math.pi * (y - 220) / 680) * 0.6, y, NRED, 4, 14)
    c.text(1060, 560, '外面气压高', 'bold', 26, NRED, 'lm')
    c.text(380, 560, '里面\n气压低', 'bold', 26, SPARK, 'mm')
    gap = 120 - 70 * ph
    for s in (-1, 1):
        x = 1560 + s * gap / 2
        c.line([(x, 300), (x - s * 20 * ph, 700)], mix(BG, (240, 240, 230), 1.0), 6)
    c.arrow(1560, 220, 1560, 680, SPARK, 4, 12)
    c.text(1560, 760, '两纸中间吹气：往中间靠', 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '帘子里的空气在流动，气压低；外面的空气静止，气压高'),
                (7.2, 14, '外面的空气就把薄薄的浴帘往里推'),
                (14.2, 22, '冷水淋浴也会这样，热水的上升气流让它更明显（以实测为准）')], y=1010)


CLIPS = {
 'E255_水珠': (e255_drops, 22), 'E255_水膜': (e255_film, 22),
 'E255_片头': (titles.opening(SER49, VOL49, S49A, 3, '20 世纪出现镜面防雾涂层'), 7),
 'E255_片尾': (titles.closing(SER49, VOL49, S49A, 3, '下集：毛巾为什么比光布更吸水？'), 7),
 'E256_线圈': (e256_loops, 22), 'E256_爬水': (e256_climb, 22),
 'E256_片头': (titles.opening(SER49, VOL49, S49A, 4, '19 世纪英国出现机织毛圈毛巾'), 7),
 'E256_片尾': (titles.closing(SER49, VOL49, S49A, 4, '下集：一开淋浴，浴帘为什么往里飘？'), 7),
 'E257_气流': (e257_flow, 22), 'E257_推帘': (e257_push, 22),
 'E257_片头': (titles.opening(SER49, VOL49, S49A, 5, '浴帘往里飘是常见的现象'), 7),
 'E257_片尾': (titles.closing(SER49, VOL49, S49A, 5, '下集：单把手水龙头，冷热水怎么混？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
