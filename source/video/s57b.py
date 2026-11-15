"""第五十七季（第二十五层：露营）第二批：E295 保温毯、E296 充气垫、E297 折叠椅 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s57a import S57A, SER57, VOL57, WARM, COOL, POLE

FOIL = (200, 205, 215)
MAT = (90, 150, 200)
ROCK = (150, 145, 135)
CLOTH = (200, 90, 70)
WOODL = (190, 150, 100)


# ---------------------------------------------------------------- E295 保温毯
def e295_reflect(c, t, i):
    corner_tag(c, '第 295 集 · 亮面把热反射回去')
    c.text(60, 96, '身体一直在往外放看不见的热辐射；保温毯亮亮的镀铝面像镜子，把这些热反射回身体，大部分跑不出去', 'serif', 36, INK)
    for j in range(2):
        cx = 520 + j * 880
        c.ellipse(cx, 560, 140, 200, fill=mix(BG, WARM, 0.85))
        c.text(cx, 560, '身体', 'bold', 30, BG, 'mm')
        if j == 1:
            c.arc(cx, 560, 260, 320, 0, 360, mix(BG, FOIL, 1.0), 12)
        for k in range(8):
            a = 2 * math.pi * k / 8 + 0.3
            ph = (t * 0.35 + k / 8) % 1
            if j == 0:
                r = 1.0 + ph * 1.1
                x, y = cx + 150 * r * math.cos(a), 560 + 210 * r * math.sin(a)
                c.ellipse(x, y, 10, 10, fill=mix(BG, NRED, 1 - ph * 0.7))
            else:
                r = 1.0 + (ph if ph < 0.5 else 1 - ph) * 1.4
                x, y = cx + 150 * r * math.cos(a), 560 + 210 * r * math.sin(a)
                c.ellipse(x, y, 10, 10, fill=mix(BG, NRED, 0.9))
        c.text(cx, 960, ['不裹：热辐射往四面散掉', '裹保温毯：热被反射回来'][j], 'bold', 28, NRED if j == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '红点是身体放出的热辐射，眼睛看不见，红外测温枪能「看」到'),
                (7.2, 14, '不裹的时候，热辐射一路往外散掉'),
                (14.2, 22, '裹上镀铝的保温毯：亮面像镜子，把热辐射反射回身体')], y=1010)


def e295_wind(c, t, i):
    corner_tag(c, '第 295 集 · 挡住风，热就不被吹走')
    c.text(60, 96, '风一吹，皮肤外面那层被焐热的空气就被刮走，换上冷空气，热跑得飞快；保温毯不透风，那层暖空气就留住了', 'serif', 36, INK)
    for j in range(2):
        cx = 560 + j * 800
        c.rect(cx - 70, 400, cx + 70, 760, fill=mix(BG, WARM, 0.8), r=20)
        if j == 1:
            c.rect(cx - 110, 370, cx + 110, 790, outline=mix(BG, FOIL, 1.0), width=12, r=30)
            c.rect(cx - 98, 382, cx + 98, 778, outline=mix(BG, WARM, 0.35), width=24, r=26)
        for k in range(5):
            y = 430 + k * 70
            x = cx - 380 + ((t * 180 + k * 70) % 260)
            if j == 0 or x < cx - 140:
                c.arrow(x, y, x + 60, y, mix(BG, FIELD, 1.0), 4, 14)
            if j == 0:
                xx = cx + 80 + ((t * 180 + k * 70) % 200)
                c.ellipse(xx, y, 8, 8, fill=mix(BG, NRED, 0.8))
        c.text(cx, 880, ['没遮挡：暖空气被风刮走', '保温毯挡风：暖空气留住'][j], 'bold', 28, NRED if j == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '小风扇对着两瓶温水吹：一瓶裸着，一瓶裹铝箔'),
                (7.2, 14, '裸着的瓶子外面，焐热的空气不停被吹走，换上冷空气'),
                (14.2, 22, '裹上的瓶子，外面那层暖空气留住了，凉得慢（温水不超过 50 ℃）')], y=1010)


# ---------------------------------------------------------------- E296 充气垫
def e296_spread(c, t, i):
    corner_tag(c, '第 296 集 · 空气把重量分散开')
    c.text(60, 96, '人直接躺在石头上，重量全压在几个尖尖的点上，硌得疼；中间垫一层空气，空气把重量匀匀地分到整张垫子上', 'serif', 36, INK)
    gy = 820
    for j in range(2):
        x0 = 220 + j * 820
        c.line([(x0, gy), (x0 + 680, gy)], LINE, 4)
        for k in range(5):
            rx = x0 + 70 + k * 135
            c.poly([(rx - 40, gy), (rx, gy - 60), (rx + 40, gy)], mix(BG, ROCK, 1.0))
        if j == 0:
            c.rect(x0 + 20, gy - 160, x0 + 660, gy - 60, fill=mix(BG, WARM, 0.8), r=30)
            for k in range(5):
                rx = x0 + 70 + k * 135
                c.arrow(rx, gy - 60, rx, gy - 120, NRED, 6, 16)
            c.text(x0 + 340, gy + 60, '直接躺：几个点硌得疼', 'bold', 28, NRED, 'mm')
        else:
            c.rect(x0 + 10, gy - 140, x0 + 670, gy - 50, fill=mix(BG, MAT, 0.7), r=40)
            c.rect(x0 + 20, gy - 250, x0 + 660, gy - 150, fill=mix(BG, WARM, 0.8), r=30)
            if t > 7.2:
                for k in range(12):
                    rx = x0 + 50 + k * 53
                    c.arrow(rx, gy - 100, rx, gy - 140, mix(BG, GREEN, 1.0), 3, 10)
            c.text(x0 + 340, gy + 60, '垫一层空气：处处托一点', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '左边直接躺在石头上，右边中间垫一张吹满气的垫子'),
                (7.2, 14, '垫子里的空气被压时，各处的压强一样大'),
                (14.2, 22, '人的重量被摊到整张垫子上，每个地方只托一点点，石头就硌不到了')], y=1010)


def e296_fill(c, t, i):
    corner_tag(c, '第 296 集 · 气要吹得刚刚好')
    c.text(60, 96, '气太少，人一压垫子就扁到底，石头顶上来；气吹足了，垫子撑得住；吹得太鼓又硬邦邦，像躺在皮球上', 'serif', 36, INK)
    gy = 820
    for j, (lab, th, col) in enumerate([('气太少', 22, NRED), ('刚刚好', 90, GREEN), ('太鼓', 150, SPARK)]):
        x0 = 140 + j * 560
        c.line([(x0, gy), (x0 + 480, gy)], LINE, 4)
        for k in range(4):
            rx = x0 + 60 + k * 120
            c.poly([(rx - 34, gy), (rx, gy - 50), (rx + 34, gy)], mix(BG, ROCK, 1.0))
        k = min(1.0, t / 6)
        top = gy - 50 - th
        c.rect(x0 + 10, gy - 50 - th, x0 + 470, gy - 40 + (0 if th > 30 else 0), fill=mix(BG, MAT, 0.7), r=int(min(40, th / 2 + 10)))
        c.rect(x0 + 40, top - 70, x0 + 440, top, fill=mix(BG, WARM, 0.8), r=24)
        if th < 30:
            for kk in range(4):
                rx = x0 + 60 + kk * 120
                c.arrow(rx, gy - 50, rx, top - 10, NRED, 4, 12)
        c.text(x0 + 240, gy + 60, lab, 'bold', 30, col, 'mm')
    c.text(960, 940, '用长条气球、积木和硬皮书来试；吹破的碎片马上收走', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '同一张垫子，吹三种气量，上面压一样重'),
                (7.2, 14, '气太少：一压就扁到底，石头直接顶到身上'),
                (14.2, 22, '气要刚刚好：撑得住又有点软，睡起来才舒服')], y=1010)


# ---------------------------------------------------------------- E297 折叠椅
def xchair(c, cx, gy, half, h, fabric, sag):
    """X 形椅腿：half 为两脚之间半宽，h 为座面高度。"""
    tl, tr = (cx - half, gy - h), (cx + half, gy - h)
    bl, br = (cx - half, gy), (cx + half, gy)
    c.line([bl, tr], mix(BG, WOODL, 1.0), 14)
    c.line([br, tl], mix(BG, WOODL, 1.0), 14)
    c.ellipse(cx, gy - h / 2, 12, 12, fill=mix(BG, POLE, 1.0))
    if fabric:
        mid = ((tl[0] + tr[0]) / 2, tl[1] + sag)
        seg(c, [tl, mid, tr], mix(BG, CLOTH, 1.0), 12)
    return tl, tr


def e297_open(c, t, i):
    corner_tag(c, '第 297 集 · 一坐，椅腿往外撑')
    c.text(60, 96, 'X 形的两条椅腿在中间转动：人一坐下，重量把上端往下压，下端就往外撑；座面的布把上端拉住，椅子就定住了', 'serif', 36, INK)
    gy = 860
    c.line([(300, gy), (1620, gy)], LINE, 4)
    k = min(1.0, t / 6)
    half = 40 + 110 * k
    h = math.sqrt(max(10, 420 ** 2 - (2 * half) ** 2))
    tl, tr = xchair(c, 960, gy, half, h, k > 0.95, 30)
    if t > 7.2:
        c.rect(860, gy - h - 110, 1060, gy - h - 10, fill=mix(BG, MAT, 0.8), r=20)
        c.text(960, gy - h - 60, '人', 'bold', 30, BG, 'mm')
        c.arrow(960, gy - h - 150, 960, gy - h - 110, NRED, 6, 16)
        c.arrow(960 - half, gy - 30, 960 - half - 90, gy - 30, NRED, 5, 14)
        c.arrow(960 + half, gy - 30, 960 + half + 90, gy - 30, NRED, 5, 14)
        c.text(960, gy - h + 70, '布被拉紧', 'bold', 26, CLOTH, 'mm')
    caps(c, t, [(0, 7, '收起来的折叠椅：两条腿并在一起，像一根长条'),
                (7.2, 14, '一坐下：重量往下压，X 的下端往外撑开'),
                (14.2, 22, '座面的布被拉紧，把两条腿拴住，越坐越稳')], y=1010)


def e297_fabric(c, t, i):
    corner_tag(c, '第 297 集 · 剪掉座面布，一压就塌')
    c.text(60, 96, '座面布不只是用来坐的，它把 X 的两个上端连成一个三角形；剪掉它，两条腿没人拉住，一压就一直撑开，塌下去', 'serif', 36, INK)
    gy = 860
    for j in range(2):
        cx = 560 + j * 800
        c.line([(cx - 380, gy), (cx + 380, gy)], LINE, 4)
        if j == 0:
            half, h = 200, 330
            xchair(c, cx, gy, half, h, True, 20)
            c.poly([(cx - half, gy - h), (cx + half, gy - h), (cx, gy - h / 2)], mix(BG, GREEN, 0.18))
            c.text(cx, gy + 60, '有布：三角形定住', 'bold', 28, GREEN, 'mm')
        else:
            k = 0 if t < 7.2 else min(1.0, (t - 7.2) / 5)
            half = 200 + 180 * k
            h = math.sqrt(max(400, 520 ** 2 - (2 * half) ** 2))
            xchair(c, cx, gy, half, h, False, 0)
            c.text(cx, gy + 60, '没有布：一压就塌', 'bold', 28, NRED, 'mm')
        c.ellipse(cx, gy - 420, 30, 30, fill=mix(BG, SPARK, 1.0)) if False else None
    caps(c, t, [(0, 7, '两把一样的小椅子，一把有座面布，一把剪掉了'),
                (7.2, 14, '同样压一枚硬币：没有布的那把，两条腿一路撑开'),
                (14.2, 22, '布把两个上端连成三角形，形状就定住了（收椅子时小心夹手）')], y=1010)


CLIPS = {
 'E295_反射': (e295_reflect, 22), 'E295_挡风': (e295_wind, 22),
 'E295_片头': (titles.opening(SER57, VOL57, S57A, 3, '急救包里的镀铝保温毯'), 7),
 'E295_片尾': (titles.closing(SER57, VOL57, S57A, 3, '下集：一层空气怎么托住一个人？'), 7),
 'E296_分散': (e296_spread, 22), 'E296_气量': (e296_fill, 22),
 'E296_片头': (titles.opening(SER57, VOL57, S57A, 4, '露营用的充气睡垫'), 7),
 'E296_片尾': (titles.closing(SER57, VOL57, S57A, 4, '下集：折叠椅坐上去为什么不合上？'), 7),
 'E297_撑开': (e297_open, 22), 'E297_布条': (e297_fabric, 22),
 'E297_片头': (titles.opening(SER57, VOL57, S57A, 5, 'X 形椅腿的露营折叠椅'), 7),
 'E297_片尾': (titles.closing(SER57, VOL57, S57A, 5, '下集：登山杖一拧怎么锁得牢？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
