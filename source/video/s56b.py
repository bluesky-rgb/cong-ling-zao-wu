"""第五十六季（古法解密 25.0：园林与庭院）第二批：B253 花街铺地、B254 竹篱笆、B255 照壁 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s56a import SB56, VOL56, WALL, WATER, STONE, LEAF, WOODC

SOIL = (120, 95, 70)
TILEC = (175, 180, 185)
BAMBOO = (190, 170, 100)


# ---------------------------------------------------------------- B253 花街铺地
def b253_seep(c, t, i):
    corner_tag(c, 'B253 · 雨水从缝里渗走')
    c.text(60, 96, '整块光滑的石板，雨水只能在表面积着；碎瓦卵石竖着拼，留下很多小缝，水从缝里渗到下面的土里', 'serif', 36, INK)
    rain = min(1.0, t / 6)
    seep = max(0.0, min(1.0, (t - 7) / 10))
    for j in range(2):
        x0 = 220 + j * 820
        c.rect(x0, 600, x0 + 640, 880, fill=mix(BG, SOIL, 1.0))
        if j == 0:
            c.rect(x0, 560, x0 + 640, 600, fill=mix(BG, TILEC, 1.0))
            h = 30 * rain
            c.rect(x0, 560 - h, x0 + 640, 560, fill=mix(BG, WATER, 0.7))
            c.text(x0 + 320, 940, '整块石板：水积在上面', 'bold', 28, NRED, 'mm')
        else:
            random.seed(5)
            for k in range(16):
                cx = x0 + 22 + k * 40
                c.ellipse(cx, 580, 16, 22, fill=mix(BG, STONE if k % 3 else TILEC, 1.0))
            h = 30 * rain * (1 - seep)
            if h > 1:
                c.rect(x0, 558 - h, x0 + 640, 558, fill=mix(BG, WATER, 0.7))
            if seep > 0:
                for k in range(15):
                    cx = x0 + 42 + k * 40
                    c.line([(cx, 600), (cx, 600 + 220 * seep)], mix(SOIL, WATER, 0.7), 8)
            c.text(x0 + 320, 940, '卵石拼的路：水从缝里渗下去', 'bold', 28, GREEN, 'mm')
    random.seed(int(t * 10))
    if t < 6:
        for k in range(40):
            x = random.uniform(200, 1700); y = random.uniform(220, 520)
            c.line([(x, y), (x - 6, y + 24)], mix(BG, WATER, 0.9), 2)
    caps(c, t, [(0, 7, '下一场雨：两种路面都淋得湿湿的'),
                (7.2, 14, '整块石板上的水没地方去，积成一层'),
                (14.2, 22, '卵石之间全是小缝：水顺着缝渗进土里，路面很快就干了（示意）')], y=1010)


def b253_grip(c, t, i):
    corner_tag(c, 'B253 · 凸起让鞋底抓得住')
    c.text(60, 96, '湿了的光滑石板，鞋底和石面之间隔着一层水膜，一推就滑；卵石凸起顶开水膜，鞋底卡在缝里，不容易滑', 'serif', 36, INK)
    for j in range(2):
        x0 = 220 + j * 820
        if j == 0:
            c.rect(x0, 620, x0 + 640, 680, fill=mix(BG, TILEC, 1.0))
            c.rect(x0, 610, x0 + 640, 620, fill=mix(BG, WATER, 0.8))
            dx = min(300, max(0, t - 3) * 60)
            c.rect(x0 + 120 + dx, 520, x0 + 320 + dx, 610, fill=mix(BG, NRED, 0.7), r=12)
            c.text(x0 + 320, 760, '光滑湿石板：一推就滑走', 'bold', 28, NRED, 'mm')
        else:
            for k in range(16):
                c.ellipse(x0 + 22 + k * 40, 640, 18, 26, fill=mix(BG, STONE, 1.0))
            dx = min(20, max(0, t - 3) * 6)
            c.rect(x0 + 120 + dx, 520, x0 + 320 + dx, 610, fill=mix(BG, GREEN, 0.7), r=12)
            for k in range(5):
                cx = x0 + 142 + k * 40
                if x0 + 120 + dx < cx < x0 + 320 + dx:
                    c.poly([(cx - 10, 610), (cx + 10, 610), (cx, 622)], mix(BG, GREEN, 0.7))
            c.text(x0 + 320, 760, '卵石路面：鞋底卡住了', 'bold', 28, GREEN, 'mm')
        c.arrow(x0 + 40, 565, x0 + 110, 565, INK, 5, 16)
    c.text(960, 860, '用橡皮包塑料袋当鞋底，用手指同样力推；结果以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '两块路面都喷湿：用同样的力推「鞋底」'),
                (7.2, 14, '光滑石板上隔着一层水，鞋底一推就溜出去'),
                (14.2, 22, '卵石一个个凸起，顶开水膜、卡住鞋底：雨天走着也不滑')], y=1010)


# ---------------------------------------------------------------- B254 竹篱笆
def frame(c, x0, y0, w, h, sh, col, braces):
    """画一个被推歪 sh 像素的方框，braces 为斜撑。"""
    A = (x0, y0 + h); B = (x0 + w, y0 + h); C2 = (x0 + w + sh, y0); D = (x0 + sh, y0)
    for p, q in [(A, B), (B, C2), (C2, D), (D, A)]:
        c.line([p, q], col, 10)
    mid_b = ((A[0] + B[0]) / 2, A[1]); mid_t = ((C2[0] + D[0]) / 2, D[1])
    c.line([mid_b, mid_t], col, 10)
    for p, q in braces:
        c.line([p, q], mix(BG, SPARK, 1.0), 10)
    return A, B, C2, D


def b254_square(c, t, i):
    corner_tag(c, 'B254 · 方格一推就歪')
    c.text(60, 96, '竖杆加横杆绑成方格：四个角都能转，从侧面一推，方格就歪成斜斜的平行四边形', 'serif', 36, INK)
    sh = min(160, max(0, t - 4) * 30)
    A, B, C2, D = frame(c, 660, 340, 600, 500, sh, mix(BG, BAMBOO, 1.0), [])
    c.arrow(D[0] - 160, D[1], D[0] - 20, D[1], NRED, 8, 22)
    for p in (A, B, C2, D):
        c.ellipse(p[0], p[1], 14, 14, fill=mix(BG, NRED, 0.9))
    c.text(960, 920, '四个角像铰链，一推就转', 'bold', 30, NRED, 'mm')
    caps(c, t, [(0, 7, '用筷子和橡皮筋绑一个方格篱笆框'),
                (7.2, 14, '从顶角往旁边推：四个角都跟着转'),
                (14.2, 22, '方格歪成了平行四边形：边长没变，形状却变了')], y=1010)


def b254_triangle(c, t, i):
    corner_tag(c, 'B254 · 三角形推不歪')
    c.text(60, 96, '在方格里斜着加一根竹竿，就分成两个三角形：三条边的长度定了，三角形的形状就变不了', 'serif', 36, INK)
    for j in range(2):
        x0 = 260 + j * 780
        sh = 0 if j else min(16, max(0, t - 4) * 4)
        w, h = 520, 460
        A = (x0, 360 + h); D = (x0 + sh, 360)
        Bp = (x0 + w, 360 + h); Cp = (x0 + w + sh, 360)
        br = [(A, Cp)] if j == 0 else [(A, Cp), (Bp, D)]
        frame(c, x0, 360, w, h, sh, mix(BG, BAMBOO, 1.0), br)
        c.arrow(x0 + sh - 140, 360, x0 + sh - 20, 360, INK, 7, 20)
        c.text(x0 + w / 2, 900, ['加一根斜撑：几乎不歪', '交叉绑两根：更牢'][j], 'bold', 28, GREEN, 'mm')
    if t > 14:
        c.poly([(260, 820), (780, 820), (780, 360)], mix(BG, GREEN, 0.18))
    caps(c, t, [(0, 7, '给方格加一根斜着的竹竿：方格被分成两个三角形'),
                (7.2, 14, '再推：三角形的三条边都不能变长变短，它就歪不了'),
                (14.2, 22, '农家篱笆斜着交叉绑，满墙都是三角形，所以推不歪')], y=1010)


# ---------------------------------------------------------------- B255 照壁
def court(c, wall):
    # 院子俯视：大门在左边
    c.rect(560, 240, 1560, 880, outline=mix(BG, WALL, 0.9), width=14)
    c.rect(553, 500, 567, 620, fill=BG)
    c.text(560, 470, '大门', 'bold', 28, INK, 'mm')
    if wall:
        c.rect(660, 440, 690, 680, fill=mix(BG, WALL, 0.9))
        c.text(675, 410, '照壁', 'bold', 26, SPARK, 'mm')
    c.ellipse(1200, 560, 40, 40, fill=mix(BG, LEAF, 1.0))
    c.text(1200, 630, '院里', 'sans', 24, MUTED, 'mm')


def b255_sight(c, t, i):
    corner_tag(c, 'B255 · 挡住门外的视线')
    c.text(60, 96, '大门一开，门外的人一眼就能看进院子；门里迎面立一堵照壁，视线被挡住，院里的人和东西就看不见了', 'serif', 36, INK)
    wall = t > 7.2
    court(c, wall)
    c.ellipse(260, 560, 30, 30, fill=mix(BG, INK, 0.9))
    c.text(260, 620, '门外的人', 'sans', 24, MUTED, 'mm')
    for dy in (-60, -20, 20, 60):
        ex = 1180 if not wall else 660
        ey = 560 + dy * (ex - 260) / 920
        c.line([(290, 560), (ex, ey)], mix(BG, SPARK if not wall else NRED, 0.8), 3)
    c.text(1060, 960, '一眼看到底' if not wall else '视线被照壁挡住', 'bold', 28, NRED if not wall else GREEN, 'mm')
    caps(c, t, [(0, 7, '没有照壁：大门一开，门外的人一眼看进院子'),
                (7.2, 14, '门里迎面立一堵照壁：视线撞在墙上'),
                (14.2, 22, '进门要往两边绕过去，院子里就有了隐私')], y=1010)


def b255_wind(c, t, i):
    corner_tag(c, 'B255 · 直灌的风绕过两边')
    c.text(60, 96, '没有照壁，风从大门直灌进院；有照壁，风撞上墙分成两股，绕过两边，变缓了再慢慢进院', 'serif', 36, INK)
    wall = t > 7.2
    court(c, wall)
    for k in range(12):
        ph = (t * 0.5 + k / 12) % 1
        if not wall:
            x = 300 + ph * 1100
            c.arrow(x, 545 + (k % 3) * 15, x + 60, 545 + (k % 3) * 15, mix(BG, FIELD, 1.0), 6, 18)
        else:
            sgn = 1 if k % 2 else -1
            if ph < 0.35:
                x = 300 + ph / 0.35 * 340
                c.arrow(x, 560, x + 50, 560, mix(BG, FIELD, 1.0), 6, 18)
            else:
                s = (ph - 0.35) / 0.65
                x = 640 + s * 600
                y = 560 + sgn * (140 * math.sin(min(1, s * 2) * math.pi / 2) - 60 * max(0, s - 0.5))
                c.arrow(x, y, x + 30, y + sgn * (8 if s < 0.5 else -4), mix(BG, FIELD, 0.6), 3, 12)
    sway = (40 if not wall else 12) * math.sin(t * 5)
    c.line([(1350, 420), (1350 + sway, 540)], INK, 6)
    c.text(1350, 380, '纸巾', 'sans', 24, MUTED, 'mm')
    c.text(1060, 960, '纸巾猛飘' if not wall else '纸巾轻轻晃', 'bold', 28, NRED if not wall else GREEN, 'mm')
    caps(c, t, [(0, 7, '风扇对着大门吹：风一路直灌，院里的纸巾猛飘'),
                (7.2, 14, '立起照壁：风撞上墙，分成两股从两边绕过去'),
                (14.2, 22, '绕路的风变缓了，院子还通风，却不再被直吹（示意，以实测为准）')], y=1010)


CLIPS = {
 'B253_渗水': (b253_seep, 22), 'B253_防滑': (b253_grip, 22),
 'B253_片头': (titles.opening(BSER, VOL56, SB56, 3, '江南园林的碎瓦卵石小路'), 7),
 'B253_片尾': (titles.closing(BSER, VOL56, SB56, 3, '下集：交叉绑的篱笆为什么推不歪？'), 7),
 'B254_方框': (b254_square, 22), 'B254_三角': (b254_triangle, 22),
 'B254_片头': (titles.opening(BSER, VOL56, SB56, 4, '农家院子的竹篱笆'), 7),
 'B254_片尾': (titles.closing(BSER, VOL56, SB56, 4, '下集：进门那堵墙挡住了什么？'), 7),
 'B255_视线': (b255_sight, 22), 'B255_绕风': (b255_wind, 22),
 'B255_片头': (titles.opening(BSER, VOL56, SB56, 5, '明清宅院门里的照壁'), 7),
 'B255_片尾': (titles.closing(BSER, VOL56, SB56, 5, '下集：石凳为什么摸着凉？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
