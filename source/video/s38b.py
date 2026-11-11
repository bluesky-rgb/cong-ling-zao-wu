"""第三十八季（古法解密 16.0）第二批：B163 哨子、B164 九宫格、B165 硬帆 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s38a import SB38, VOL38, AIR

SAIL = (220, 200, 160)
BAMBOO = (170, 160, 90)


# ---------------------------------------------------------------- B163 哨子
def b163_edge(c, t, i):
    corner_tag(c, 'B163 · 气流撞上薄边，来回摆动')
    c.text(60, 96, '吹进去的细气流打在一道锋利的边上：一会儿往里拐，一会儿往外拐，带着空腔里的空气一起振', 'serif', 36, INK)
    x0, y0 = 260, 520
    c.rect(x0, y0 - 140, x0 + 1200, y0 + 140, fill=mix(BG, WOOD, 0.25), outline=mix(BG, WOOD, 0.9), width=6, r=20)
    c.rect(x0 - 200, y0 - 26, x0 + 300, y0 + 26, fill=mix(BG, WOOD, 0.6))
    ex = x0 + 420
    c.poly([(ex, y0 - 140), (ex + 140, y0 - 140), (ex + 140, y0 - 20)], BG)
    c.poly([(ex, y0 - 30), (ex + 140, y0 - 140), (ex + 140, y0 - 130), (ex + 10, y0 - 30)], mix(BG, WOOD, 1.0))
    sw = math.sin(t * 2 * math.pi * 1.2)
    for k in range(9):
        f = k / 8
        x = x0 + 300 + f * 140
        y = y0 - 20 - f * 60 * (1 + 0.8 * sw)
        c.ellipse(x, y, 7, 7, fill=AIR)
    if sw > 0:
        c.arrow(ex + 80, y0 - 110, ex + 120, y0 - 200, AIR, 5, 14)
        c.text(ex + 150, y0 - 210, '往外', 'sans', 22, MUTED, 'lm')
    else:
        c.arrow(ex + 60, y0 - 40, ex + 160, y0 + 20, AIR, 5, 14)
        c.text(ex + 180, y0 + 30, '往里', 'sans', 22, MUTED, 'lm')
    for k in range(7):
        r = 40 + k * 60 + 30 * sw
        c.arc(x0 + 900, y0, r, r, -60, 60, mix(BG, SPARK, 0.6 - k * 0.07), 3)
    c.text(x0 - 60, y0 + 80, '吹', 'bold', 28, SPARK, 'mm')
    c.text(ex + 70, y0 - 170, '锋利的边', 'sans', 22, INK, 'mm')
    c.text(x0 + 900, y0 + 200, '空腔里的空气跟着振', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '哨子里没有会振的小片，只有一道削得很薄的边'),
                (7.2, 14, '气流撞上薄边，一会儿拐进空腔、一会儿拐出去，每秒来回上千次'),
                (14.2, 22, '空腔里的空气被推得一胀一缩，发出尖尖的声音：笛子、陶埙也是这样（示意）')], y=1010)


def b163_cavity(c, t, i):
    corner_tag(c, 'B163 · 空腔越小，声音越尖')
    c.text(60, 96, '三个一样的瓶子装不同多的水：留给空气的地方越少，吹出来的音越高', 'serif', 36, INK)
    for j, (fill, lab, hz) in enumerate([(0.0, '空瓶', '约 170 赫兹'), (1 / 3, '1/3 瓶水', '约 220 赫兹'), (2 / 3, '2/3 瓶水', '约 330 赫兹')]):
        cx = 400 + j * 560
        top, bot = 330, 860
        c.rect(cx - 110, top + 120, cx + 110, bot, fill=mix(BG, WATER_L, 0.15), outline=mix(BG, WATER_L, 0.7), width=4, r=30)
        c.rect(cx - 36, top, cx + 36, top + 130, fill=mix(BG, WATER_L, 0.15), outline=mix(BG, WATER_L, 0.7), width=4)
        if fill > 0:
            wy = bot - (bot - top - 120) * fill
            c.rect(cx - 106, wy, cx + 106, bot - 4, fill=mix(BG, WATER, 0.8), r=26)
        else:
            wy = bot
        a = fade(t, 1 + j * 4, 2 + j * 4)
        f = 1 + j * 0.6
        for k in range(4):
            yy = top + 140 + ((t * 120 * f + k * 60) % max(60, wy - top - 160))
            c.line([(cx - 80, yy), (cx + 80, yy)], mix(BG, SPARK, 0.4 * a), 3)
        c.arrow(cx - 160, top - 40, cx - 40, top + 10, AIR, 5, 14)
        c.text(cx, bot + 50, lab, 'bold', 26, INK, 'mm')
        c.text(cx, bot + 95, hz + '（以实测为准）', 'mono', 22, mix(BG, SPARK, a), 'mm')
    caps(c, t, [(0, 7, '对着瓶口斜着吹，瓶里的空气像弹簧一样一胀一缩'),
                (7.2, 14, '水越多，空气越少，这根「空气弹簧」越硬，振得越快'),
                (14.2, 22, '振得快，音就高：剪短吸管哨，声音也会变尖（示意）')], y=1010)


# ---------------------------------------------------------------- B164 九宫格
LO = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]


def _grid(c, x0, y0, s, nums, hl=None, col=None):
    for r in range(3):
        for q in range(3):
            x, y = x0 + q * s, y0 + r * s
            on = hl and (r, q) in hl
            c.rect(x, y, x + s - 8, y + s - 8, fill=mix(SHEET, SPARK, 0.35) if on else SHEET, outline=LINE, width=2, r=10)
            v = nums[r][q]
            if v:
                c.text(x + (s - 8) / 2, y + (s - 8) / 2, str(v), 'bold', int(s * 0.45), col(v) if col else INK, 'mm')


def b164_center(c, t, i):
    corner_tag(c, 'B164 · 每条线等于 15，中间必须是 5')
    c.text(60, 96, '1 到 9 加起来是 45，分成三行，每行就该是 15；正中那格同时在 4 条线上', 'serif', 36, INK)
    st = min(4, int(t / 5))
    nums = [[0] * 3 for _ in range(3)]
    hl = None
    if st >= 1:
        nums[1][1] = 5
    lines = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 1), (2, 1)]]
    if st >= 2:
        hl = lines[int(t * 1.2) % 4]
    _grid(c, 300, 260, 200, nums, hl)
    c.rect(1080, 260, 1840, 860, fill=SHEET, r=14)
    rows = [('1 + 2 + … + 9 = 45', 0), ('45 ÷ 3 行 = 每行 15', 0), ('正中那格在 4 条线上', 1), ('4 条线加起来 = 60', 2),
            ('= 全部 45 + 3 次中间', 3), ('中间 = (60 − 45) ÷ 3 = 5', 3)]
    for k, (s, need) in enumerate(rows):
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        c.text(1120, 320 + k * 90, s, 'mono' if k != 2 else 'sans', 28, mix(BG, SPARK if k == 5 else INK, a), 'lm')
    caps(c, t, [(0, 7, '先不急着试：1 到 9 加起来是 45，每行就必须等于 15'),
                (7.2, 14, '正中那一格最特别，横、竖、两条斜线都经过它'),
                (14.2, 22, '把这 4 条线加起来一算，中间只能是 5：剩下的就好填了')], y=1010)


def b164_fill(c, t, i):
    corner_tag(c, 'B164 · 偶数放四角，一步填完')
    c.text(60, 96, '5 在中间，偶数 2、4、6、8 放四角，奇数 1、3、7、9 放四边：只有一种排法，转一转、翻一翻就是 8 种', 'serif', 34, INK)
    order = [(1, 1), (0, 0), (2, 2), (0, 2), (2, 0), (0, 1), (2, 1), (1, 0), (1, 2)]
    k = min(9, int(t / 1.3) + 1)
    nums = [[0] * 3 for _ in range(3)]
    for (r, q) in order[:k]:
        nums[r][q] = LO[r][q]
    _grid(c, 260, 250, 200, nums, col=lambda v: SPARK if v % 2 == 0 and v != 0 else INK)
    if k >= 9:
        a = fade(t, 13, 14)
        for j in range(8):
            g = [row[:] for row in LO]
            for _ in range(j % 4):
                g = [list(x) for x in zip(*g[::-1])]
            if j >= 4:
                g = [row[::-1] for row in g]
            x0 = 1020 + (j % 4) * 210
            y0 = 300 + (j // 4) * 260
            for r in range(3):
                for q in range(3):
                    c.rect(x0 + q * 60, y0 + r * 60, x0 + q * 60 + 54, y0 + r * 60 + 54, fill=mix(BG, SHEET, a), r=6)
                    c.text(x0 + q * 60 + 27, y0 + r * 60 + 27, str(g[r][q]), 'bold', 24, mix(BG, INK, a), 'mm')
        c.text(1430, 860, '这 8 种其实是同一张：转 4 次 × 翻 2 面', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '5 放正中；偶数放四个角，和对角的那个凑成 10'),
                (7.2, 14, '剩下的奇数填进四条边，8 条线一检查，全都是 15'),
                (14.2, 22, '古人叫它「洛书」或「九宫」：横竖斜都相等的数表叫幻方')], y=1010)


# ---------------------------------------------------------------- B165 硬帆
def _sail_soft(c, x0, y0, w, h, t, gust):
    pts = []
    for k in range(13):
        f = k / 12
        b = 40 * math.sin(math.pi * f) * (1 + 0.6 * gust * math.sin(t * 9 + f * 8))
        pts.append((x0 + b + 20 * gust * math.sin(t * 11 + f * 6), y0 + f * h))
    poly = pts + [(x0 + w, y0 + h), (x0 + w, y0)]
    c.poly(poly, mix(BG, SAIL, 0.9))


def _sail_hard(c, x0, y0, w, h, t, gust, fold=0.0):
    n = 6
    hh = h * (1 - fold * 0.75)
    for k in range(n):
        y = y0 + h - hh + k * hh / n
        b = 6 * gust * math.sin(t * 9 + k)
        c.poly([(x0 + b, y), (x0 + w, y), (x0 + w, y + hh / n), (x0 + b, y + hh / n)], mix(BG, SAIL, 0.9))
        c.line([(x0 - 10, y), (x0 + w + 10, y)], mix(BG, BAMBOO, 1.0), 6)
    c.line([(x0 - 10, y0 + h), (x0 + w + 10, y0 + h)], mix(BG, BAMBOO, 1.0), 6)


def b165_battens(c, t, i):
    corner_tag(c, 'B165 · 竹条把帆撑平')
    c.text(60, 96, '同一阵风：软帆被吹得乱抖、形状一直在变；一根根竹条撑住的帆，始终保持平整', 'serif', 36, INK)
    gust = 0.5 + 0.5 * math.sin(t * 0.8)
    for j, lab in enumerate(['软帆：形状跟着风乱变', '硬帆：竹条把帆撑平']):
        mx = 380 + j * 880
        c.line([(mx + 380, 230), (mx + 380, 880)], mix(BG, WOOD, 1.0), 10)
        if j == 0:
            _sail_soft(c, mx, 260, 380, 560, t, gust)
        else:
            _sail_hard(c, mx, 260, 380, 560, t, gust)
        c.text(mx + 190, 930, lab, 'bold', 26, INK, 'mm')
    for k in range(6):
        x = 80 + ((t * 300 + k * 160) % 260)
        c.arrow(x, 300 + k * 90, x + 70, 300 + k * 90, AIR, 4, 12)
    c.text(140, 250, '风', 'bold', 28, MUTED, 'mm')
    caps(c, t, [(0, 7, '软帆是一整块布，风一大就鼓、就抖，力全挤在几处'),
                (7.2, 14, '中国帆船在帆上横着绑一根根竹条，每根都把帆撑住一段'),
                (14.2, 22, '帆面平整，受力分散；撕了一个口子，也只坏一格（示意）')], y=1010)


def b165_reef(c, t, i):
    corner_tag(c, 'B165 · 像百叶一样一节节收')
    c.text(60, 96, '风突然变大，松开绳子：带竹条的帆一节节落下来叠在一起，帆变小，船就稳了', 'serif', 36, INK)
    fold = max(0.0, min(1.0, (t - 6) / 8))
    mx = 640
    c.line([(mx + 460, 200), (mx + 460, 900)], mix(BG, WOOD, 1.0), 12)
    _sail_hard(c, mx, 240, 460, 600, t, 0.3, fold)
    c.poly([(mx - 120, 900), (mx + 700, 900), (mx + 620, 980), (mx - 60, 980)], mix(BG, WOOD, 0.8))
    c.rect(1380, 280, 1860, 520, fill=SHEET, r=12)
    c.text(1620, 330, '帆的面积', 'bold', 26, INK, 'mm')
    c.text(1620, 400, f'{100 - fold * 75:.0f}%', 'mono', 44, SPARK, 'mm')
    c.text(1620, 470, '风越大，收得越多', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '风平浪静时，帆整张升起来，吃满风'),
                (7.2, 14, '风一大，松开升帆的绳子，竹条带着帆一节节落下'),
                (14.2, 22, '叠在一起的帆整整齐齐，不用爬上桅杆去收：这叫「缩帆」（示意）')], y=1040)


CLIPS = {
 'B163_薄边': (b163_edge, 22), 'B163_空腔': (b163_cavity, 22),
 'B163_片头': (titles.opening(BSER, VOL38, SB38, 3, '河姆渡遗址出土过骨哨'), 7),
 'B163_片尾': (titles.closing(BSER, VOL38, SB38, 3, '下集：1 到 9 怎么填，横竖斜都一样？'), 7),
 'B164_中间': (b164_center, 22), 'B164_填满': (b164_fill, 22),
 'B164_片头': (titles.opening(BSER, VOL38, SB38, 4, '汉代已有「九宫」之数'), 7),
 'B164_片尾': (titles.closing(BSER, VOL38, SB38, 4, '下集：中国古船的帆上，为什么横着一根根竹条？'), 7),
 'B165_竹条': (b165_battens, 22), 'B165_收帆': (b165_reef, 22),
 'B165_片头': (titles.opening(BSER, VOL38, SB38, 5, '宋代中国帆船已用竹条撑帆'), 7),
 'B165_片尾': (titles.closing(BSER, VOL38, SB38, 5, '下集：吊一根线，怎么看墙歪没歪？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
