"""第四十八季（古法解密 21.0：作坊与街巷）第二批：B213 竹帘、B214 舞钻、B215 线装书 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s48a import SB48, VOL48, ROPE

BAMBOO = (190, 170, 100)
PAPER = (235, 225, 200)
LIGHT = (250, 230, 150)


# ---------------------------------------------------------------- B213 竹帘
def _scene(c, night, label):
    out_l = 0.15 if night else 1.0
    in_l = 0.85 if night else 0.18
    c.rect(80, 260, 900, 880, fill=mix(BG, LIGHT, 0.65 * out_l + 0.05))
    c.rect(1020, 260, 1840, 880, fill=mix(BG, LIGHT, 0.65 * in_l + 0.05))
    c.text(490, 300, '外面' + ('（黑）' if night else '（亮）'), 'bold', 28, INK, 'mm')
    c.text(1430, 300, '屋里' + ('（点灯）' if night else '（暗）'), 'bold', 28, INK, 'mm')
    for k in range(30):
        y = 270 + k * 20
        c.rect(900, y, 1020, y + 14, fill=mix(BG, BAMBOO, 1.0))
    c.ellipse(1430, 640, 60, 60, fill=mix(BG, (200, 120, 100), 0.4 + 0.6 * in_l))
    c.rect(1380, 700, 1480, 840, fill=mix(BG, (120, 140, 200), 0.4 + 0.6 * in_l), r=20)
    c.ellipse(490, 640, 60, 60, fill=mix(BG, (200, 120, 100), 0.4 + 0.6 * out_l))
    c.rect(440, 700, 540, 840, fill=mix(BG, (120, 140, 200), 0.4 + 0.6 * out_l), r=20)
    return out_l, in_l


def b213_light(c, t, i):
    corner_tag(c, 'B213 · 亮的一边看不见暗的一边')
    c.text(60, 96, '竹帘两边一模一样：外面亮、屋里暗时，屋里的人看得见外面，外面的人只看见一片亮亮的帘子', 'serif', 36, INK)
    _scene(c, False, '')
    ph = (t % 4) / 4
    for k in range(4):
        x = 140 + (1500 * ((ph + k / 4) % 1))
        c.arrow(x, 460, x + 60, 460, mix(BG, SPARK, 1.0), 4, 12)
    for k in range(4):
        x = 1800 - (1500 * ((ph + k / 4) % 1))
        if x < 1020:
            c.arrow(x, 520, x - 40, 520, mix(BG, MUTED, 0.25), 2, 8)
        else:
            c.arrow(x, 520, x - 40, 520, mix(BG, MUTED, 0.7), 2, 8)
    c.text(490, 930, '外面的人：只看见亮帘子', 'bold', 26, NRED, 'mm')
    c.text(1430, 930, '屋里的人：看清外面', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '外面的阳光很强，穿过竹帘的缝照进屋，屋里人看得清清楚楚'),
                (7.2, 14, '屋里暗，传出来的光本来就少，又被竹条挡掉一部分'),
                (14.2, 22, '外面的人看到的，主要是竹条反射的亮光，屋里就看不清了')], y=1010)


def b213_flip(c, t, i):
    corner_tag(c, 'B213 · 天黑点灯，就反过来了')
    c.text(60, 96, '竹帘不是单向的：晚上外面黑、屋里点灯，外面的人能看清屋里，屋里的人反而看不清外面', 'serif', 36, INK)
    night = t > 7
    _scene(c, night, '')
    if night:
        c.text(490, 930, '外面的人：看清屋里', 'bold', 26, GREEN, 'mm')
        c.text(1430, 930, '屋里的人：只看见帘子', 'bold', 26, NRED, 'mm')
    else:
        c.text(490, 930, '白天：外面看不进', 'bold', 26, NRED, 'mm')
        c.text(1430, 930, '白天：屋里看得清', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '白天：外亮内暗，屋里看得见外面'),
                (7.2, 14, '晚上：屋里点灯、外面黑，亮暗倒过来'),
                (14.2, 22, '谁那一边亮，谁就看不清对面：竹帘只是挡掉一部分光（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B214 舞钻
def b214_rope(c, t, i):
    corner_tag(c, 'B214 · 绳子把上下变成转动')
    c.text(60, 96, '绳子缠在钻杆上，横杆往下一压，绳子松开，就带着钻杆转起来；上下压动变成了转动', 'serif', 36, INK)
    cx = 760
    per = 3.0
    ph = (t % per) / per
    wind = math.cos(2 * math.pi * ph)
    bar_y = 330 + 180 * (1 - abs(wind))
    ang = 6 * math.pi * wind
    c.line([(cx, 220), (cx, 860)], mix(BG, WOOD, 1.0), 16)
    c.rect(cx - 220, bar_y - 12, cx + 220, bar_y + 12, fill=mix(BG, WOOD, 0.8), r=6)
    turns = abs(wind) * 4
    for k in range(int(turns * 4)):
        y = 230 + k * 8
        c.line([(cx - 10, y), (cx + 10, y + 6)], mix(BG, ROPE, 1.0), 3)
    top_y = 230 + int(turns * 4) * 8
    c.line([(cx - 8, top_y), (cx - 200, bar_y)], mix(BG, ROPE, 1.0), 3)
    c.line([(cx + 8, top_y), (cx + 200, bar_y)], mix(BG, ROPE, 1.0), 3)
    c.ellipse(cx, 720, 140, 30, fill=mix(BG, (120, 110, 100), 1.0))
    for k in range(6):
        a = ang + k * math.pi / 3
        c.line([(cx, 720), (cx + 130 * math.cos(a), 720 + 26 * math.sin(a))], mix(BG, INK, 0.5), 3)
    c.text(cx + 170, 720, '飞轮', 'bold', 24, INK, 'lm')
    d = math.sin(2 * math.pi * ph)
    c.text(1450, 420, '横杆往下压' if bar_y > 420 and d > 0 else ('飞轮把绳子反缠回去' if d < 0 else '横杆被顶起'), 'bold', 32, SPARK, 'mm')
    c.text(1450, 500, '转向：' + ('顺时针' if d > 0 else '逆时针'), 'bold', 30, NRED if d > 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '先转几圈，让绳子缠在钻杆上，横杆被拉到上面'),
                (7.2, 14, '往下一压，绳子松开，钻杆跟着转'),
                (14.2, 22, '压到底时手一松，钻杆还在转，把绳子反着缠上去；再压，就反着转（示意）')], y=1010)


def b214_flywheel(c, t, i):
    corner_tag(c, 'B214 · 没有飞轮就转不回来')
    c.text(60, 96, '飞轮又宽又重：压到底后它靠惯性继续转，把绳子反着缠回去；拿掉飞轮，钻杆转一下就停', 'serif', 36, INK)
    for j, (lab, fly) in enumerate([('有飞轮：来回转很多次', True), ('没飞轮：转一下就停', False)]):
        cx = 480 + j * 960
        decay = 0.12 if fly else 1.2
        amp = math.exp(-decay * t)
        ang = 6 * math.pi * amp * math.cos(2.1 * t)
        c.line([(cx, 260), (cx, 820)], mix(BG, WOOD, 1.0), 14)
        if fly:
            c.ellipse(cx, 700, 150, 32, fill=mix(BG, (120, 110, 100), 1.0))
        for k in range(4):
            a = ang + k * math.pi / 2
            r = 130 if fly else 26
            c.line([(cx, 700), (cx + r * math.cos(a), 700 + (r * 0.2) * math.sin(a))], NRED, 4)
        c.rect(cx - 280, 880, cx - 280 + 560 * amp, 910, fill=GREEN if fly else NRED, r=6)
        c.text(cx, 950, lab, 'bold', 26, GREEN if fly else NRED, 'mm')
    caps(c, t, [(0, 7, '同样压一下横杆，然后都不再用力'),
                (7.2, 14, '有飞轮的，靠惯性来回转了很多次'),
                (14.2, 22, '没有飞轮的，转一下就停了，绳子也缠不回去（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B215 线装书
def b215_fold(c, t, i):
    corner_tag(c, 'B215 · 单面印字，对折朝外')
    c.text(60, 96, '古书一张纸只印一面：印好后字朝外对折，折口在外边，开口一边对齐，空白的背面藏在里面', 'serif', 36, INK)
    ph = min(1.0, (t % 11) / 7)
    cx, cy = 960, 560
    W2 = 360
    c.rect(cx, cy - 240, cx + W2, cy + 240, fill=mix(BG, PAPER, 1.0))
    for k in range(6):
        c.line([(cx + 60 + k * 50, cy - 200), (cx + 60 + k * 50, cy + 200)], mix(BG, INK, 0.5), 3)
    fw = W2 * math.cos(math.pi * ph)
    col = mix(BG, PAPER, 1.0) if fw > 0 else mix(BG, PAPER, 0.75)
    x0 = cx - fw if fw > 0 else cx
    x1 = cx if fw > 0 else cx - fw
    c.rect(min(x0, x1), cy - 240, max(x0, x1), cy + 240, fill=col)
    if fw > 0:
        for k in range(6):
            x = cx - (60 + k * 50) * (fw / W2)
            c.line([(x, cy - 200), (x, cy + 200)], mix(BG, INK, 0.5), 3)
    c.line([(cx, cy - 250), (cx, cy + 250)], SPARK, 3)
    c.text(cx, cy + 290, '折口（书口）', 'bold', 24, SPARK, 'mm')
    if ph >= 1:
        c.text(cx + W2 + 40, cy, '开口一边对齐 → 在这边打孔订线', 'bold', 26, GREEN, 'lm')
    caps(c, t, [(0, 7, '一张纸只在一面印字（古时用纸背透墨，只能印一面）'),
                (7.2, 14, '字朝外对折：前后两面都是字，空白藏在里面'),
                (14.2, 22, '折口朝外成了「书口」，开口的一边对齐，等着订线')], y=1010)


def b215_stitch(c, t, i):
    corner_tag(c, 'B215 · 四眼订：每一针都压住整叠纸')
    c.text(60, 96, '在开口一边打四个孔：线穿过孔、绕过书脊、绕过上下边，拉紧后把整叠纸缠住，不会散，翻开也能摊平', 'serif', 36, INK)
    x0, x1, y0, y1 = 520, 1400, 260, 860
    c.rect(x0, y0, x1, y1, fill=mix(BG, PAPER, 1.0))
    sx = x1 - 70
    holes = [y0 + (y1 - y0) * f for f in (0.15, 0.38, 0.62, 0.85)]
    for y in holes:
        c.ellipse(sx, y, 9, 9, fill=mix(BG, INK, 0.8))
    path = [(sx, holes[1]), (x1 + 30, holes[1]), (sx, holes[1]), (sx, holes[0]), (x1 + 30, holes[0]), (sx, holes[0]), (sx, y0 - 30), (sx, holes[0]),
            (sx, holes[1]), (sx, holes[2]), (x1 + 30, holes[2]), (sx, holes[2]), (sx, holes[3]), (x1 + 30, holes[3]), (sx, holes[3]), (sx, y1 + 30), (sx, holes[3]),
            (sx, holes[2]), (sx, holes[1])]
    n = len(path) - 1
    prog = min(1.0, t / 18) * n
    for k in range(int(prog)):
        c.line([path[k], path[k + 1]], NRED, 5)
    if prog < n:
        k = int(prog); f = prog - k
        a, b = path[k], path[k + 1]
        c.line([a, (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)], NRED, 5)
    c.text(x1 + 60, 560, '书脊', 'bold', 26, INK, 'lm')
    c.text(x0 - 20, 560, '书口（折口）', 'bold', 26, MUTED, 'rm')
    caps(c, t, [(0, 7, '离开口一边 1.5 厘米，平均打四个孔'),
                (7.2, 14, '线从孔里穿过去，再绕过书脊回来，上下两头还要绕过书边'),
                (14.2, 22, '一圈圈拉紧，每一针都压住整叠纸；最后在中间打结藏起来（示意）')], y=1010)


CLIPS = {
 'B213_明暗': (b213_light, 22), 'B213_反转': (b213_flip, 22),
 'B213_片头': (titles.opening(BSER, VOL48, SB48, 3, '古代人家门窗常挂竹帘'), 7),
 'B213_片尾': (titles.closing(BSER, VOL48, SB48, 3, '下集：上下压一根横杆，钻头怎么就转了？'), 7),
 'B214_绳转': (b214_rope, 22), 'B214_飞轮': (b214_flywheel, 22),
 'B214_片头': (titles.opening(BSER, VOL48, SB48, 4, '古代木匠用舞钻（拉钻）钻孔'), 7),
 'B214_片尾': (titles.closing(BSER, VOL48, SB48, 4, '下集：古书为什么对折了再用线订？'), 7),
 'B215_对折': (b215_fold, 22), 'B215_四眼': (b215_stitch, 22),
 'B215_片头': (titles.opening(BSER, VOL48, SB48, 5, '明代以后线装书最常见'), 7),
 'B215_片尾': (titles.closing(BSER, VOL48, SB48, 5, '下集：用杵往下砸，为什么比用手压管用？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
