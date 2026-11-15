"""第五十六季（古法解密 25.0：园林与庭院）第三批：B256 石凳、B257 倒影池、B258 门槛 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s56a import SB56, VOL56, WALL, WATER, STONE, LEAF, WOODC

SKIN = (235, 190, 160)
COLDB = (70, 110, 220)


# ---------------------------------------------------------------- B256 石凳
def b256_same(c, t, i):
    corner_tag(c, 'B256 · 放在一起，温度一样')
    c.text(60, 96, '石凳和木凳在同一片树荫下放久了，温度计量出来差不多一样；可手按上去，石头明显更凉', 'serif', 36, INK)
    for j, (lab, col) in enumerate([('石板', STONE), ('木板', WOODC)]):
        cx = 620 + j * 680
        c.rect(cx - 220, 560, cx + 220, 660, fill=mix(BG, col, 1.0), r=8)
        c.text(cx, 720, lab, 'bold', 30, INK, 'mm')
        c.rect(cx - 14, 300, cx + 14, 540, fill=SHEET, outline=MUTED, width=2, r=10)
        h = min(1.0, t / 5) * 150
        c.rect(cx - 8, 530 - h, cx + 8, 532, fill=mix(BG, NRED, 0.9))
        c.ellipse(cx, 540, 18, 18, fill=mix(BG, NRED, 0.9))
        if t > 5:
            c.text(cx + 70, 380, '24 ℃', 'mono', 30, INK, 'lm')
        if t > 9:
            c.text(cx, 820, ['好凉！', '不凉'][j], 'bold', 34, FIELD if j == 0 else MUTED, 'mm')
    c.text(960, 920, '温度是示意，以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '石板和木板在屋里放 1 小时，温度计贴上去量'),
                (7.2, 14, '两个读数差不多：它们其实一样「冷」'),
                (14.2, 22, '可两只手同时按上去，石头明显更凉：为什么？')], y=1010)


def b256_conduct(c, t, i):
    corner_tag(c, 'B256 · 石头把热带走得快')
    c.text(60, 96, '手比凳子暖，热从手流进凳子：石头导热快，热一下子被带走，手就觉得凉；木头导热慢，热留在手上', 'serif', 36, INK)
    for j, (lab, col, sp) in enumerate([('石板', STONE, 1.0), ('木板', WOODC, 0.2)]):
        cx = 620 + j * 680
        c.rect(cx - 240, 560, cx + 240, 760, fill=mix(BG, col, 1.0), r=8)
        c.rect(cx - 160, 470, cx + 160, 560, fill=mix(BG, SKIN, 1.0), r=30)
        c.text(cx, 515, '手', 'bold', 28, BG, 'mm')
        n = 8
        for k in range(n):
            ph = (t * 0.6 + k / n) % 1
            depth = ph * 180 * (1.0 if sp > 0.5 else 0.25)
            x = cx - 140 + (k * 40)
            a = 1 - ph
            c.ellipse(x, 570 + depth, 8, 8, fill=mix(BG, NRED, a))
        c.text(cx, 820, ['热一下子被带走：凉', '热走得慢：不凉'][j], 'bold', 28, FIELD if j == 0 else MUTED, 'mm')
    if t > 14:
        c.text(960, 900, '冰块放在石板上化得更快，也是石头导热快', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '红点表示热：手一按上去，热就往凳子里流'),
                (7.2, 14, '石头导热快，热一下子被带进深处，手上的热少了，觉得凉'),
                (14.2, 22, '冬天坐石凳也一样，热被带走得快，所以特别冰')], y=1010)


# ---------------------------------------------------------------- B257 倒影池
def pavilion(c, cx, base, sc, col, flip=False):
    s = -1 if flip else 1
    c.poly([(cx - 150 * sc, base - s * 180 * sc), (cx, base - s * 260 * sc), (cx + 150 * sc, base - s * 180 * sc)], col)
    c.rect(cx - 100 * sc, min(base - s * 180 * sc, base), cx - 85 * sc, max(base - s * 180 * sc, base), fill=col)
    c.rect(cx + 85 * sc, min(base - s * 180 * sc, base), cx + 100 * sc, max(base - s * 180 * sc, base), fill=col)


def b257_mirror(c, t, i):
    corner_tag(c, 'B257 · 静水像一面镜子')
    c.text(60, 96, '水面平静时，光像照到镜子上一样整齐地反射回来；池底越暗，从水里透出的光越少，倒影越清楚', 'serif', 36, INK)
    for j, (lab, bot, a) in enumerate([('黑池底', (20, 25, 30), 0.85), ('白池底', (220, 220, 215), 0.35)]):
        cx = 520 + j * 880
        pavilion(c, cx, 560, 1.0, mix(BG, (200, 80, 70), 1.0))
        c.rect(cx - 330, 560, cx + 330, 860, fill=mix(BG, bot, 1.0))
        c.rect(cx - 330, 560, cx + 330, 860, fill=mix(mix(BG, bot, 1.0), (60, 90, 120), 0.3))
        pavilion(c, cx, 560, 1.0, mix(mix(BG, bot, 1.0), (200, 80, 70), a * min(1, t / 4)), flip=True)
        c.text(cx, 920, lab + ('：倒影清楚' if j == 0 else '：倒影淡'), 'bold', 28, GREEN if j == 0 else MUTED, 'mm')
    caps(c, t, [(0, 7, '两个托盘装满水：一个垫黑纸，一个垫白纸'),
                (7.2, 14, '黑底的水面像一面镜子，亭子倒影清清楚楚'),
                (14.2, 22, '白底的池子里，池底反上来的光把倒影冲淡了（只用托盘里的水）')], y=1010)


def b257_ripple(c, t, i):
    corner_tag(c, 'B257 · 一起波纹，倒影就碎了')
    c.text(60, 96, '风一吹，水面起了波纹，每一小块水面朝的方向都不一样，反射的光被打乱，倒影就碎成一条条', 'serif', 36, INK)
    cx = 960
    pavilion(c, cx, 540, 1.2, mix(BG, (200, 80, 70), 1.0))
    c.rect(cx - 600, 540, cx + 600, 900, fill=(22, 30, 36))
    amp = 0 if t < 7.2 else min(1.0, (t - 7.2) / 4) * (1 if t < 18 else max(0.2, 1 - (t - 18) / 4))
    col = mix((22, 30, 36), (200, 80, 70), 0.85)
    sc = 1.2
    for row in range(0, int(262 * sc), 6):
        y = 540 + row
        dx = amp * 50 * math.sin(row * 0.15 + t * 4)
        if row < 180 * sc:
            for side in (-1, 1):
                x = cx + side * 92.5 * sc + dx
                c.rect(x - 9, y, x + 9, y + 5, fill=col)
        else:
            w = 150 * sc * (1 - (row - 180 * sc) / (80 * sc))
            if w > 2:
                c.rect(cx - w + dx, y, cx + w + dx, y + 5, fill=col)
    if amp > 0:
        for k in range(5):
            c.arc(cx + 300, 700, 60 + k * 60, 20 + k * 20, 0, 360, mix(BG, WATER, 0.4), 2)
    c.text(cx, 950, '平静：倒影完整' if amp == 0 else '起波纹：倒影碎了', 'bold', 28, GREEN if amp == 0 else NRED, 'mm')
    caps(c, t, [(0, 7, '水面平静：倒影和亭子一模一样，只是上下颠倒'),
                (7.2, 14, '用吸管轻轻一吹：水面起了波纹'),
                (14.2, 22, '每一小块水面朝向不同，倒影碎成一条条；风停了又慢慢合上')], y=1010)


# ---------------------------------------------------------------- B258 门槛
def tank(c, sill, t, t0):
    x0, x1, yb, yt = 260, 1660, 860, 380
    c.rect(x0, yt, x1, yb, fill=mix(BG, WATER, 0.25), outline=MUTED, width=4)
    if sill:
        c.rect(940, yb - 150, 980, yb, fill=mix(BG, WOODC, 1.0))
        c.text(960, yb - 180, '门槛', 'bold', 28, SPARK, 'mm')
    k = max(0.0, t - t0)
    front = min(x1 - x0 - 20, k * 90)
    if sill:
        front_l = min(940 - x0 - 10, front)
        h = 60 + max(0, k * 90 - (940 - x0)) * 0.12
        h = min(h, 140)
        c.rect(x0 + 4, yb - h, x0 + 4 + front_l, yb - 4, fill=mix(BG, COLDB, 0.85))
    else:
        c.rect(x0 + 4, yb - 60, x0 + 4 + front, yb - 4, fill=mix(BG, COLDB, 0.85))
    c.text(x0 + 80, yt - 40, '冷水（蓝）从这头倒进去', 'sans', 24, MUTED, 'lm')


def b258_sink(c, t, i):
    corner_tag(c, 'B258 · 冷的贴着地面走')
    c.text(60, 96, '冷空气比暖空气重，冬天会贴着地面从门缝下面往屋里钻；用水来看：蓝色冰水倒进常温水里，贴着盒底流', 'serif', 36, INK)
    tank(c, False, t, 2)
    c.text(960, 940, '冷水沉在底下，一路贴着盒底流到另一头', 'bold', 28, FIELD, 'mm')
    caps(c, t, [(0, 7, '透明盒子装常温水；冰水滴蓝色素，从一头底部慢慢倒进去'),
                (7.2, 14, '蓝色冷水不往上浮，像一层地毯贴着盒底往前爬'),
                (14.2, 22, '冬天的冷风也这样：贴着地面，从门缝下面钻进屋（色素水不喝）')], y=1010)


def b258_sill(c, t, i):
    corner_tag(c, 'B258 · 门槛把它挡在外面')
    c.text(60, 96, '盒子中间立一道矮矮的「门槛」：贴着底流的冷水撞上门槛就被挡住，越积越厚也翻不过去', 'serif', 36, INK)
    tank(c, True, t, 2)
    c.text(960, 940, '冷水被门槛挡住；下雨天的积水、灰尘也一样', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '同样倒蓝色冷水，这次盒子中间有一道门槛'),
                (7.2, 14, '冷水贴着底流到门槛前，被挡住了，只能在这边越积越厚'),
                (14.2, 22, '老房子的高门槛，就挡住了贴地的冷风和院里的积水（示意）')], y=1010)


CLIPS = {
 'B256_同温': (b256_same, 22), 'B256_导热': (b256_conduct, 22),
 'B256_片头': (titles.opening(BSER, VOL56, SB56, 6, '园林老街里的石桌石凳'), 7),
 'B256_片尾': (titles.closing(BSER, VOL56, SB56, 6, '下集：水面怎么变成镜子？'), 7),
 'B257_镜面': (b257_mirror, 22), 'B257_波纹': (b257_ripple, 22),
 'B257_片头': (titles.opening(BSER, VOL56, SB56, 7, '园林讲究「借景」入池'), 7),
 'B257_片尾': (titles.closing(BSER, VOL56, SB56, 7, '下集：高高的门槛挡住了什么？'), 7),
 'B258_下沉': (b258_sink, 22), 'B258_门槛': (b258_sill, 22),
 'B258_片头': (titles.opening(BSER, VOL56, SB56, 8, '传统房屋门口的高门槛'), 7),
 'B258_片尾': (titles.closing(BSER, VOL56, SB56, 8, '下集：大缸里的水为什么冻不透？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
