"""第四十季（古法解密 17.0）第二批：B173 马镫、B174 竹筏、B175 拉纤 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s40a import SB40, VOL40, AIR

SKIN = (220, 170, 130)
HORSE = (150, 100, 70)
BAMBOO = (180, 170, 90)
ROPE = (200, 170, 110)


# ---------------------------------------------------------------- B173 马镫
def _rider(c, cx, cy, sway, stirrup):
    c.ellipse(cx, cy + 120, 260, 90, fill=mix(BG, HORSE, 0.9))
    c.rect(cx - 70, cy + 20, cx + 70, cy + 60, fill=mix(BG, (110, 70, 50), 1.0), r=10)
    hx = cx + sway * 160
    c.line([(cx, cy + 30), (hx, cy - 160)], mix(BG, (90, 120, 170), 1.0), 26)
    c.ellipse(hx, cy - 200, 34, 34, fill=SKIN)
    for sgn in (-1, 1):
        kx = cx + sgn * 50
        if stirrup:
            fx, fy = kx + sgn * 10, cy + 200
            c.line([(cx + sgn * 30, cy + 40), (kx, cy + 120), (fx, fy)], mix(BG, (90, 120, 170), 1.0), 18)
            c.line([(cx + sgn * 60, cy + 40), (fx, fy - 10)], mix(BG, (110, 70, 50), 1.0), 3)
            c.rect(fx - 26, fy, fx + 26, fy + 10, fill=mix(BG, (170, 170, 180), 1.0), r=3)
        else:
            c.line([(cx + sgn * 30, cy + 40), (kx + sgn * 30, cy + 140), (kx + sgn * 20 + sway * 60, cy + 240)], mix(BG, (90, 120, 170), 1.0), 18)


def b173_support(c, t, i):
    corner_tag(c, 'B173 · 脚有了支点')
    c.text(60, 96, '没有马镫，人只能靠大腿夹着马背；有了马镫，两只脚踩住，身体多了两个撑住的点', 'serif', 36, INK)
    for j, (lab, st) in enumerate([('没有马镫：一颠就晃', False), ('有马镫：脚踩住，稳', True)]):
        cx, cy = 520 + j * 880, 520
        bump = math.sin(t * 4)
        sway = bump * (0.45 if not st else 0.1)
        _rider(c, cx, cy, sway, st)
        if st:
            for sgn in (-1, 1):
                c.arrow(cx + sgn * 60, cy + 290, cx + sgn * 60, cy + 220, SPARK, 5, 14)
        c.text(cx, 900, lab, 'bold', 26, NRED if not st else GREEN, 'mm')
    caps(c, t, [(0, 7, '马一颠，人的身体就被往一边甩'),
                (7.2, 14, '没有马镫，只能靠大腿和屁股夹住马背，很容易被甩歪'),
                (14.2, 22, '脚踩住马镫，腿能用力撑住，身体晃了也能被拉回来（示意）')], y=1010)


def b173_push(c, t, i):
    corner_tag(c, 'B173 · 同样推一下，晃多少')
    c.text(60, 96, '坐在高凳上脚悬空，肩膀被轻轻一推就歪过去；脚下踩一个小板凳，同样推一下，几乎不动', 'serif', 36, INK)
    for j, (lab, st) in enumerate([('脚悬空', False), ('脚踩小板凳', True)]):
        cx, base = 520 + j * 880, 860
        c.rect(cx - 90, base - 360, cx + 90, base - 330, fill=mix(BG, WOOD, 0.95), r=6)
        for sgn in (-1, 1):
            c.line([(cx + sgn * 80, base - 330), (cx + sgn * 90, base)], mix(BG, WOOD, 1.0), 10)
        T = 5
        ph = (t % T)
        push = max(0, 1 - abs(ph - 1.5) * 1.2) if ph < 2.5 else 0
        amp = 0.5 if not st else 0.08
        sway = amp * push * math.cos(max(0, ph - 1.5) * 6) if ph > 1 else 0
        hx = cx + sway * 180
        c.line([(cx, base - 360), (hx, base - 600)], mix(BG, (90, 120, 170), 1.0), 30)
        c.ellipse(hx, base - 650, 40, 40, fill=SKIN)
        if st:
            c.rect(cx - 110, base - 90, cx + 110, base - 60, fill=mix(BG, WOOD, 0.8), r=6)
            for sgn in (-1, 1):
                c.line([(cx + sgn * 30, base - 345), (cx + sgn * 60, base - 230), (cx + sgn * 50, base - 92)], mix(BG, (90, 120, 170), 1.0), 18)
        else:
            for sgn in (-1, 1):
                c.line([(cx + sgn * 30, base - 345), (cx + sgn * 60, base - 230), (cx + sgn * 50 + sway * 60, base - 140)], mix(BG, (90, 120, 170), 1.0), 18)
        if 0.8 < ph < 1.6:
            c.arrow(hx - 220, base - 560, hx - 50, base - 560, NRED, 6, 18)
        c.text(cx, base + 60, lab, 'bold', 26, INK, 'mm')
    c.rect(0, 860, 1920, 870, fill=mix(BG, (150, 120, 90), 0.6))
    caps(c, t, [(0, 7, '甲坐在高凳上，乙在侧面用手掌轻轻推一下肩膀'),
                (7.2, 14, '脚悬空时，身体只有屁股一个支撑，一推就歪'),
                (14.2, 22, '脚踩住小板凳，腿撑住了，同样一推几乎不动（只轻推一下，旁边有人扶）')], y=1010)


# ---------------------------------------------------------------- B174 竹筏
def b174_hollow(c, t, i):
    corner_tag(c, 'B174 · 空心的竹节装满空气')
    c.text(60, 96, '竹子一节一节被竹节封住，里面全是空气：一根竹子排开的水很多，自己却很轻，浮力远大于重量', 'serif', 36, INK)
    cx, wy = 760, 560
    c.rect(100, wy, 1500, 960, fill=mix(BG, WATER, 0.4))
    c.rect(200, wy - 60, 1320, wy + 60, fill=mix(BG, BAMBOO, 0.9), r=58)
    for k in range(1, 6):
        x = 200 + k * 187
        c.rect(x - 5, wy - 60, x + 5, wy + 60, fill=mix(BG, (130, 120, 60), 1.0))
    c.rect(230, wy - 40, 1290, wy + 40, fill=mix(BG, AIR, 0.25), r=36)
    c.text(760, wy - 100, '竹节把空气一格格封住', 'sans', 22, INK, 'mm')
    for k in range(7):
        x = 260 + k * 170
        c.arrow(x, wy + 160, x, wy + 70, GREEN, 5, 14)
    c.text(760, wy + 200, '浮力：排开多少水，就托起多重', 'bold', 24, GREEN, 'mm')
    c.rect(1540, 300, 1880, 560, fill=SHEET, r=12)
    c.text(1710, 350, '一根粗毛竹', 'bold', 24, INK, 'mm')
    c.text(1710, 410, '自重：约 10 千克', 'sans', 22, INK, 'mm')
    c.text(1710, 460, '能托起：约 30 千克', 'sans', 22, GREEN, 'mm')
    c.text(1710, 510, '（示意，拍摄前核对）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '竹子是空心的，每隔一段有一道竹节把空腔封住'),
                (7.2, 14, '放进水里，它排开的水比自己重得多，浮力把它高高托起'),
                (14.2, 22, '就算一节破了进水，其他节还封着空气，照样浮着（示意）')], y=1010)


def b174_width(c, t, i):
    corner_tag(c, 'B174 · 捆得宽，就不容易翻')
    c.text(60, 96, '同样 6 根竹子：并排捆成宽宽的一层，人站偏一点也只是微微一斜；捆成窄窄的两层，一偏就翻', 'serif', 36, INK)
    for j, (lab, wide) in enumerate([('宽：一层 6 根', True), ('窄：两层，每层 3 根', False)]):
        cx, wy = 520 + j * 880, 600
        c.rect(cx - 380, wy, cx + 380, 900, fill=mix(BG, WATER, 0.4))
        off = 0.5 + 0.5 * math.sin(t * 0.8)
        tilt = (0.06 if wide else 0.5) * off
        ca, sa = math.cos(tilt), math.sin(tilt)
        def R(x, y):
            return (cx + x * ca - y * sa, wy + x * sa + y * ca)
        if wide:
            for k in range(6):
                x = -250 + k * 100
                px, py = R(x, 0)
                c.ellipse(px, py, 48, 48, fill=mix(BG, BAMBOO, 0.9))
            mx, my = R(150 * off, -48)
        else:
            for row in range(2):
                for k in range(3):
                    x = -100 + k * 100
                    px, py = R(x, -row * 96)
                    c.ellipse(px, py, 48, 48, fill=mix(BG, BAMBOO, 0.9))
            mx, my = R(80 * off, -144)
        c.rect(mx - 30, my - 120, mx + 30, my, fill=mix(BG, (90, 120, 170), 1.0), r=10)
        c.ellipse(mx, my - 145, 26, 26, fill=SKIN)
        c.text(cx, 950, lab, 'bold', 26, GREEN if wide else NRED, 'mm')
    caps(c, t, [(0, 7, '人站在筏子上，总会偏到一边'),
                (7.2, 14, '宽筏子一边稍微压下去，那一边排开的水就多了，浮力把它推回来'),
                (14.2, 22, '窄而高的筏子重心高、底面窄，一偏就推不回来，翻了（示意）')], y=1010)


# ---------------------------------------------------------------- B175 拉纤
def b175_parts(c, t, i):
    corner_tag(c, 'B175 · 斜着拉，力分成两份')
    c.text(60, 96, '纤夫在岸上，纤绳斜着拉船：一份力把船往前拉，另一份力把船往岸边拉', 'serif', 36, INK)
    c.rect(0, 220, 1920, 420, fill=mix(BG, (120, 150, 90), 0.45))
    c.rect(0, 420, 1920, 960, fill=mix(BG, WATER, 0.4))
    bx, by = 700, 700
    c.poly([(bx - 220, by - 50), (bx + 180, by - 50), (bx + 260, by), (bx + 180, by + 50), (bx - 220, by + 50)], mix(BG, WOOD, 0.95))
    c.ellipse(bx, by, 14, 14, fill=INK)
    px, py = 1500 + 20 * math.sin(t), 330
    c.line([(bx, by), (px, py)], ROPE, 4)
    c.ellipse(px, py - 30, 22, 22, fill=SKIN)
    c.line([(px, py - 10), (px - 30, py + 60)], SKIN, 12)
    a = fade(t, 4, 6)
    dx, dy = px - bx, py - by
    L = math.hypot(dx, dy)
    F = 380
    fx, fy = dx / L * F, dy / L * F
    c.arrow(bx, by, bx + fx, by + fy, mix(BG, SPARK, a), 6, 18)
    c.arrow(bx, by, bx + fx, by, mix(BG, GREEN, a), 6, 18)
    c.arrow(bx, by, bx, by + fy, mix(BG, NRED, a), 6, 18)
    c.text(bx + fx + 20, by + fy, '纤绳的拉力', 'bold', 24, mix(BG, SPARK, a), 'lm')
    c.text(bx + fx + 20, by + 40, '往前（有用）', 'bold', 24, mix(BG, GREEN, a), 'lm')
    c.text(bx - 30, by + fy - 10, '往岸边', 'bold', 24, mix(BG, NRED, a), 'rm')
    caps(c, t, [(0, 7, '纤夫只能在岸上走，绳子不可能顺着河正前方拉'),
                (7.2, 14, '斜着的拉力可以拆成两份：一份往前，一份往岸边'),
                (14.2, 22, '往前那份推着船逆流而上，往岸边那份会把船拉去撞岸（示意）')], y=1010)


def b175_rudder(c, t, i):
    corner_tag(c, 'B175 · 绳长、桅高、舵一偏')
    c.text(60, 96, '绳子放长，拉的方向更顺着河；系在高高的桅杆上，绳子不拖水；船尾的舵往外一偏，把往岸边那份力抵掉', 'serif', 33, INK)
    c.rect(0, 220, 1920, 360, fill=mix(BG, (120, 150, 90), 0.45))
    c.rect(0, 360, 1920, 960, fill=mix(BG, WATER, 0.4))
    st = min(3, int(t / 6))
    by = 560 if st == 0 else 600
    bx = 500 + (t % 6) * 40
    c.poly([(bx - 220, by - 50), (bx + 180, by - 50), (bx + 260, by), (bx + 180, by + 50), (bx - 220, by + 50)], mix(BG, WOOD, 0.95))
    L = 600 if st == 0 else 1200
    px = min(1880, bx + L * 0.95)
    py = 300
    mx, my = (bx, by - (150 if st >= 2 else 0))
    if st >= 2:
        c.rect(bx - 5, by - 150, bx + 5, by, fill=mix(BG, WOOD, 1.0))
    c.line([(mx, my), (px, py)], ROPE, 4)
    c.ellipse(px, py - 30, 20, 20, fill=SKIN)
    if st >= 3:
        c.line([(bx - 220, by), (bx - 300, by + 40)], mix(BG, WOOD, 1.0), 10)
        c.arrow(bx - 260, by + 20, bx - 260, by - 60, GREEN, 5, 14)
        c.text(bx - 320, by + 90, '舵一偏，船头转向河心', 'sans', 22, GREEN, 'mm')
    labs = ['绳短：拉向岸边的那份很大', '绳放长：方向更顺着河', '系在桅杆上：绳子离开水面', '再加舵：抵掉往岸边的那份']
    c.rect(1180, 700, 1880, 860, fill=SHEET, r=12)
    c.text(1530, 780, labs[st], 'bold', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '绳子短，斜得厉害，往岸边的那份力很大'),
                (7.2, 14, '绳子放长、系在桅杆上，拉的方向更顺，绳子也不拖进水里'),
                (14.2, 22, '船上的人把舵往外偏，水流推着船尾，把往岸边的力抵掉（示意）')], y=1010)


CLIPS = {
 'B173_支点': (b173_support, 22), 'B173_推一下': (b173_push, 22),
 'B173_片头': (titles.opening(BSER, VOL40, SB40, 3, '西晋时期已出现单马镫'), 7),
 'B173_片尾': (titles.closing(BSER, VOL40, SB40, 3, '下集：几根竹子捆一起，怎么载人不翻？'), 7),
 'B174_空心': (b174_hollow, 22), 'B174_宽窄': (b174_width, 22),
 'B174_片头': (titles.opening(BSER, VOL40, SB40, 4, '南方古人用竹子扎筏渡水'), 7),
 'B174_片尾': (titles.closing(BSER, VOL40, SB40, 4, '下集：纤夫在岸上拉船，船为什么不撞岸？'), 7),
 'B175_分力': (b175_parts, 22), 'B175_舵': (b175_rudder, 22),
 'B175_片头': (titles.opening(BSER, VOL40, SB40, 5, '长江三峡的纤夫拉船逆流而上'), 7),
 'B175_片尾': (titles.closing(BSER, VOL40, SB40, 5, '下集：渔网怎么在水里竖起来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
