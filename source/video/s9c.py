"""第九季第三批：B26 灵渠陡门、B27 唧筒、B28 双动活塞风箱 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s9a import SB9, VOL9, WATER
from s9b import WOOD

STONE = (140, 135, 125)
AIR = (150, 190, 220)

def water(c, x0, x1, top, bed, a=1.0):
    if top < bed - 1:
        c.rect(x0, top, x1, bed, fill=mix(BG, WATER, 0.55 * a))
        c.line([(x0, top), (x1, top)], mix(BG, WATER, a), 3)

def boat(c, x, wl, a=1.0):
    pts = [(x - 90, wl - 26), (x + 90, wl - 26), (x + 66, wl + 14), (x - 66, wl + 14)]
    c.poly(pts, mix(BG, WOOD, 0.8 * a))
    c.line([(x, wl - 26), (x, wl - 120)], mix(BG, WOOD, a), 4)
    c.poly([(x + 4, wl - 116), (x + 4, wl - 40), (x + 62, wl - 46)], mix(BG, SHEET, a))

def gate(c, x, bed, top, lift, col=STONE):
    """lift 0 = closed (from top to bed), 1 = raised out of the water."""
    if lift >= 1: return
    c.rect(x - 12, top, x + 12, bed, fill=mix(BG, col, 1 - lift), r=3)
    if lift > 0:
        c.arrow(x, top - 10, x, top - 70 * lift, mix(BG, MUTED, 1 - lift * 0.5), 3, 10)

# ---------------------------------------------------------------- B26 灵渠陡门
def b26_flash(c, t, i):
    corner_tag(c, 'B26 · 一道陡门')
    c.text(60, 96, '水太浅、坡太陡，船怎么往上走？', 'serif', 40, INK)
    gx = 960
    bedL, bedU = 840, 720
    # ground
    c.poly([(80, bedL), (gx, bedL), (gx, bedU), (1840, bedU), (1840, 900), (80, 900)], mix(BG, STONE, 0.45))
    rise = fade(t, 0.5, 6)
    opn = fade(t, 7, 9)
    # levels
    up_closed = 690 - 150 * rise          # upper water piles up behind the gate
    lo_closed = 790
    eq = fade(t, 8, 15)
    meet = (up_closed + lo_closed) / 2 + 30
    lvlU = up_closed + (meet - 20 - up_closed) * eq * opn
    lvlL = lo_closed + (meet + 20 - lo_closed) * eq * opn
    water(c, 80, gx, lvlL, bedL)
    water(c, gx, 1840, lvlU, bedU)
    if opn > 0 and t < 16:
        for k in range(6):
            d = ((t * 1.4 + k / 6) % 1)
            x = gx + 60 - 260 * d
            y = lvlU + (lvlL - lvlU) * min(1, d * 1.5) + 20
            c.arrow(x + 40, y, x - 10, y + 4, mix(BG, WATER, 0.9), 3, 10)
    gate(c, gx, bedU + 2, 500, opn)
    c.text(gx - 30, 470, '陡门', 'bold', 28, INK, 'rm')
    # boat hauled up
    bx = 520 + 640 * ease(fade(t, 10, 18))
    wl = lvlL if bx < gx else lvlU
    boat(c, bx, wl)
    if 10 < t < 18:
        c.line([(bx + 90, wl - 26), (1500, wl - 60)], MUTED, 2)
        c.text(1520, wl - 70, '拉纤', 'bold', 24, MUTED, 'lm')
    a = fade(t, 1, 2)
    c.text(1180, 230, '关上：上游越积越高', 'sans', 28, mix(BG, INK, a), 'lm')
    b = fade(t, 7, 8)
    c.text(1180, 280, '打开：水面一下子拉平，船趁势通过', 'sans', 28, mix(BG, INK, b), 'lm')
    d = fade(t, 15, 16)
    c.text(1180, 330, '水流很急，逆流要靠人拉', 'sans', 28, mix(BG, NRED, d), 'lm')
    caps(c, t, [(0, 6.5, '灵渠翻越分水岭，水浅坡陡。陡门就是在渠道里横着关上一道门'),
                (6.7, 14, '门一关，上游的水越积越高；门一开，水面拉平，船就过去了'),
                (14.2, 22, '只有一道门，开门时水流很急：上行的船要靠人拉，下行的船要冲下去')], y=1010)

def b26_pound(c, t, i):
    corner_tag(c, 'B26 · 两道闸门')
    c.text(60, 96, '两道门之间关一格水：船坐着电梯上坡', 'serif', 40, INK)
    xa, xb = 700, 1240
    bedL, bedC, bedU = 860, 860, 700
    c.poly([(80, bedL), (xb, bedC), (xb, bedU), (1840, bedU), (1840, 920), (80, 920)], mix(BG, STONE, 0.45))
    lo, up = 680, 470
    fill = ease(fade(t, 6, 13))
    lvlC = lo + (up - lo) * fill
    water(c, 80, xa, lo, bedL)
    water(c, xa, xb, lvlC, bedC)
    water(c, xb, 1840, up, bedU)
    ga = fade(t, 3, 5)                    # gate A closes
    gb = fade(t, 13.5, 15)                # gate B opens
    gate(c, xa, bedC, 400, 1 - ga)
    gate(c, xb, bedU, 400, gb)
    c.text(xa, 360, '下闸门', 'bold', 24, INK, 'mm')
    c.text(xb, 360, '上闸门', 'bold', 24, INK, 'mm')
    if 6 < t < 13:
        for k in range(4):
            d = (t * 0.9 + k / 4) % 1
            c.ellipse(xb - 30 - 80 * d, bedU + 40 + 20 * math.sin(k), 6, 6, fill=WATER)
        c.text(xb + 30, bedU + 80, '小闸孔慢慢放水', 'sans', 22, MUTED, 'lm')
    x = 360 + 610 * ease(fade(t, 0.5, 3)) + 600 * ease(fade(t, 15, 19.5))
    wl = lo if x < xa - 40 else (lvlC if x < xb else up)
    boat(c, x, wl)
    if 6 < t:
        h = 860 - 470
        c.arrow(xa + 60, lo, xa + 60, lvlC, GREEN, 4, 14)
        c.text(xa + 80, (lo + lvlC) / 2, f'水面升高 {fill * 2.1:.1f} 米（示意）', 'sans', 22, GREEN, 'lm')
    a = fade(t, 16, 17)
    c.text(1300, 230, '984 年 · 乔维岳在西河', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(1300, 278, '建两道闸门的船闸（拍摄前核对）', 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 5.5, '船开进两道门之间的闸室，关上下闸门'),
                (5.7, 13.3, '上游的水从小孔慢慢流进来：连通器，水面最后一样高'),
                (13.5, 22, '水面平了才开上闸门，船平平稳稳地开出去：这就是船闸')], y=1010)

# ---------------------------------------------------------------- B27 唧筒
def b27_syringe(c, t, i):
    corner_tag(c, 'B27 · 抽进来，压出去')
    c.text(60, 96, '一根竹筒，怎么把水喷到房顶？', 'serif', 40, INK)
    bx0, bx1, by0, by1 = 760, 1400, 470, 570
    nz = 690
    tub = 1 - fade(t, 7.5, 9)
    if tub > 0:
        c.rect(560, 540, 900, 820, fill=mix(BG, WATER, 0.45 * tub), outline=mix(BG, MUTED, tub), width=3, r=6)
    pull = ease(fade(t, 1, 7))
    push = ease(fade(t, 10, 12.5))
    px = bx0 + 20 + (bx1 - bx0 - 40) * (pull - push * pull)
    c.rect(bx0, by0, bx1, by1, fill=mix(BG, (200, 190, 150), 0.5), outline=WOOD, width=4, r=6)
    if px > bx0 + 22:
        c.rect(bx0 + 4, by0 + 6, px - 8, by1 - 6, fill=mix(BG, WATER, 0.75))
    c.rect(nz, (by0 + by1) / 2 - 12, bx0, (by0 + by1) / 2 + 12, fill=WOOD)
    c.rect(px - 8, by0 + 4, px + 8, by1 - 4, fill=INK, r=3)
    c.rect(px, (by0 + by1) / 2 - 8, 1620, (by0 + by1) / 2 + 8, fill=MUTED)
    c.text(px + 30, by0 - 28, '裹絮的活塞杆', 'sans', 22, MUTED, 'lm')
    if 1 < t < 7:
        c.arrow(640, 700, 700, 560, WATER, 4, 14)
        c.text(400, 860, '拉：筒里压强变小，外面的大气把水压进来', 'sans', 26, INK, 'lm')
    if 10 < t < 14.5:
        rnd = random.Random(int(t * 30))
        for k in range(30):
            s = rnd.random() * min(1, (t - 10) / 1.2)
            x = nz - 900 * s
            y = 520 - 260 * s + 300 * s * s
            if x > 70:
                c.ellipse(x, y, 7, 7, fill=WATER)
    a = fade(t, 12.5, 13.5)
    c.text(400, 860, '推：手的力压在一小块水上，水从小孔高速喷出' if t > 9 else '', 'sans', 26, mix(BG, INK, a), 'lm')
    d = fade(t, 15, 16)
    c.text(1100, 230, '缺点：喷完一筒，', 'sans', 28, mix(BG, NRED, d), 'lm')
    c.text(1100, 278, '得再插回水里重新抽', 'sans', 28, mix(BG, NRED, d), 'lm')
    caps(c, t, [(0, 7.3, '唧筒是一根竹筒，杆头裹着棉絮当活塞。插进水里往外拉，水就被吸进来'),
                (7.5, 14.5, '提出水面再往里推：同样的力挤在小孔上，水就喷得又急又远'),
                (14.7, 22, '可是每喷一筒，都要再插回水里重新抽：下一步，要装单向阀')], y=1010)

def valve(c, x, y, open_, label, vert=False):
    col = GREEN if open_ else NRED
    c.rect(x - 26, y - 26, x + 26, y + 26, fill=mix(BG, col, 0.25), outline=col, width=3, r=6)
    if open_:
        if vert: c.line([(x - 22, y), (x - 6, y - 20)], col, 5)
        else: c.line([(x, y - 22), (x + 18, y - 8)], col, 5)
    else:
        if vert: c.line([(x - 22, y), (x + 22, y)], col, 5)
        else: c.line([(x, y - 22), (x, y + 22)], col, 5)
    if vert: c.text(x + 40, y, label, 'bold', 20, col, 'lm')
    else: c.text(x, y + 46, label, 'bold', 20, col, 'mm')

def b27_valves(c, t, i):
    corner_tag(c, 'B27 · 两个单向阀')
    c.text(60, 96, '装上两个只许单向走的阀门：不用拔出水面', 'serif', 40, INK)
    cx, top, bot = 800, 300, 720
    period = 4.0
    ph = (t % period) / period
    up = ph < 0.5
    k = math.sin(math.pi * (ph * 2 if up else (ph - 0.5) * 2))
    py = (bot - 40) - (bot - top - 120) * ((ph * 2) if up else (1 - (ph - 0.5) * 2))
    # bucket
    c.rect(560, 860, 1040, 990, fill=mix(BG, WATER, 0.45), outline=MUTED, width=3, r=6)
    c.rect(cx - 16, bot, cx + 16, 900, fill=mix(BG, WATER, 0.6), outline=MUTED, width=2)
    # barrel
    c.rect(cx - 100, top, cx + 100, bot, fill=mix(BG, SHEET, 0.6), outline=WOOD, width=4, r=6)
    c.rect(cx - 94, py + 10, cx + 94, bot - 4, fill=mix(BG, WATER, 0.7))
    c.rect(cx - 96, py - 10, cx + 96, py + 10, fill=INK, r=3)
    c.rect(cx - 8, top - 80, cx + 8, py - 10, fill=MUTED)
    # outlet pipe
    c.rect(cx + 100, bot - 60, 1420, bot - 30, fill=mix(BG, WATER, 0.6), outline=MUTED, width=2)
    c.poly([(1420, bot - 66), (1480, bot - 52), (1480, bot - 38), (1420, bot - 24)], MUTED)
    valve(c, cx, bot + 60, up, '进水阀', vert=True)
    valve(c, cx + 170, bot - 45, not up, '出水阀')
    if up:
        for j in range(4):
            d = (t * 2 + j / 4) % 1
            c.ellipse(cx, 880 - 160 * d, 6, 6, fill=WATER)
    else:
        rnd = random.Random(int(t * 30))
        for j in range(24):
            s = rnd.random() * k
            x = 1480 + 380 * s
            y = bot - 45 - 200 * s + 260 * s * s
            c.ellipse(x, y, 6, 6, fill=WATER)
    c.text(cx - 140, (top + bot) / 2, '拉' if up else '推', 'serif', 64, INK, 'mm')
    c.text(1100, 300, ('拉：进水阀开、出水阀关，水从桶里进来' if up else '推：进水阀关、出水阀开，水从管子喷出'), 'sans', 28, INK, 'lm')
    a = fade(t, 13, 14)
    c.text(1100, 380, '一推一拉，水只能往一个方向走', 'bold', 28, mix(BG, GREEN, a), 'lm')
    c.text(1100, 430, '今天的手压水井、打气筒，都是这个结构', 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 6, '阀门像一扇只往一边开的小门：水推它就开，水往回走就关'),
                (6.2, 13, '往上拉，下面的进水阀开；往下推，进水阀关上，水只能从出水阀出去'),
                (13.2, 22, '这样筒子不用拔出水面，就能一下一下连续喷水')], y=1010)

# ---------------------------------------------------------------- B28 双动活塞风箱
def b28_double(c, t, i):
    corner_tag(c, 'B28 · 推也吹，拉也吹')
    c.text(60, 96, '一只木箱、一块活塞、四片小阀门', 'serif', 40, INK)
    x0, x1, y0, y1 = 420, 1320, 300, 640
    period = 5.0
    ph = (t % period) / period
    pushing = ph < 0.5                    # piston moves right
    s = ph * 2 if pushing else 2 - ph * 2
    px = x0 + 80 + (x1 - x0 - 160) * ease(s)
    # air channel under the box
    c.rect(x0, y1, x1, y1 + 90, fill=mix(BG, AIR, 0.25), outline=WOOD, width=4)
    c.rect(x0, y0, x1, y1, fill=mix(BG, SHEET, 0.5), outline=WOOD, width=5)
    c.rect(x1, y1 + 20, 1560, y1 + 70, fill=mix(BG, AIR, 0.25), outline=WOOD, width=3)
    # fire
    fl = 0.75 + 0.15 * math.sin(t * 7)
    c.poly([(1590, 900), (1720, 900), (1655, 900 - 160 * fl)], SPARK)
    c.poly([(1560, y1 + 70), (1600, y1 + 70), (1640, 800), (1610, 810)], WOOD)
    c.text(1655, 940, '炉膛', 'bold', 24, INK, 'mm')
    # piston and rod
    c.rect(px - 12, y0 + 6, px + 12, y1 - 6, fill=INK, r=3)
    c.rect(200, (y0 + y1) / 2 - 8, px, (y0 + y1) / 2 + 8, fill=MUTED)
    c.rect(170, (y0 + y1) / 2 - 50, 200, (y0 + y1) / 2 + 50, fill=WOOD, r=6)
    # valves: intake on end walls (top), outlet on floor near ends
    valve(c, x0 + 20, y0 + 60, pushing, '进', vert=False)
    valve(c, x1 - 20, y0 + 60, not pushing, '进', vert=False)
    valve(c, x0 + 70, y1, not pushing, '出', vert=True)
    valve(c, x1 - 70, y1, pushing, '出', vert=True)
    # air particles
    rnd = random.Random(int(t * 20))
    for j in range(22):
        d = rnd.random()
        if pushing:
            # right chamber squeezed -> out through right floor valve -> channel -> fire
            x = px + (x1 - px) * d
            c.ellipse(x, y0 + 40 + (y1 - y0 - 80) * rnd.random(), 5, 5, fill=AIR)
        else:
            x = x0 + (px - x0) * d
            c.ellipse(x, y0 + 40 + (y1 - y0 - 80) * rnd.random(), 5, 5, fill=AIR)
    for j in range(10):
        d = (t * 1.2 + j / 10) % 1
        c.ellipse(x0 + 60 + (1560 - x0 - 60) * d, y1 + 45, 6, 6, fill=mix(BG, AIR, 0.9))
    c.arrow(1180 if pushing else 560, 220, 1300 if pushing else 440, 220, INK, 4, 16)
    c.text(870, 220, '推（活塞往前）' if pushing else '拉（活塞往后）', 'bold', 30, INK, 'mm')
    a = fade(t, 12, 13)
    c.text(60, 780, '前面的空气被压出去，', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(60, 820, '后面同时吸进新空气：', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(60, 860, '每一下都在送风', 'bold', 28, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 6, '风箱是一只密封的木箱，中间一块活塞，两头各有一片进风阀，底下有两片出风阀'),
                (6.2, 12, '往前推：前面的空气被挤出去，后面的进风阀打开吸进新空气'),
                (12.2, 22, '往回拉：正好反过来。推也送风，拉也送风，风从底下的风道一路吹进炉子')], y=1010)

def b28_flow(c, t, i):
    corner_tag(c, 'B28 · 风断不断')
    c.text(60, 96, '皮囊和双动风箱，送出的风有什么不同？', 'serif', 40, INK)
    gx0, gx1 = 360, 1760
    rows = [(380, '皮囊（单动）', lambda u: max(0.0, math.sin(u)), NRED, '只有压下去时有风：一阵一阵'),
            (720, '双动活塞风箱', lambda u: abs(math.sin(u)), GREEN, '推和拉都有风：几乎不断')]
    show = fade(t, 1, 15)
    for k, (yc, name, f, col, note) in enumerate(rows):
        a = fade(t, 0.5 + k * 3, 1.5 + k * 3)
        if a <= 0: continue
        c.line([(gx0, yc + 120), (gx1, yc + 120)], mix(BG, MUTED, a), 2)
        c.line([(gx0, yc - 130), (gx0, yc + 120)], mix(BG, MUTED, a), 2)
        c.text(gx0 - 20, yc, name, 'bold', 28, mix(BG, INK, a), 'rm')
        c.text(gx1, yc + 150, '时间 →', 'sans', 20, mix(BG, MUTED, a), 'rm')
        n = int(200 * show)
        pts = []
        for j in range(n + 1):
            u = j / 200 * 4 * 2 * math.pi
            pts.append((gx0 + (gx1 - gx0) * j / 200, yc + 120 - 220 * f(u)))
        if len(pts) > 1:
            seg(c, pts, mix(BG, col, a), 4)
        b = fade(t, 15 + k * 1.5, 16 + k * 1.5)
        avg = 0.318 if k == 0 else 0.637
        c.line([(gx0, yc + 120 - 220 * avg), (gx1, yc + 120 - 220 * avg)], mix(BG, col, 0.6 * b), 2)
        c.text(gx1 - 10, yc - 150, f'{note}（平均风量约 {avg:.2f}）', 'sans', 24, mix(BG, INK, b), 'rm')
    caps(c, t, [(0, 7, '皮囊风箱压一下吹一阵，抬起来吸气时，炉子里就没有风'),
                (7.2, 15, '双动活塞风箱推也吹、拉也吹：同样的动作，风几乎不断'),
                (15.2, 22, '同样的节奏，平均风量多一倍，炉温更稳：炼铁、打铁都离不开它（数字为理想化示意）')], y=1010)

CLIPS = {
 'B26_陡门': (b26_flash, 22), 'B26_船闸': (b26_pound, 22),
 'B26_片头': (titles.opening(BSER, VOL9, SB9, 6, '秦 · 灵渠 · 唐代起建陡门'), 7),
 'B26_片尾': (titles.closing(BSER, VOL9, SB9, 6, '下集：宋代的消防队用什么喷水？'), 7),
 'B27_活塞': (b27_syringe, 22), 'B27_单向阀': (b27_valves, 22),
 'B27_片头': (titles.opening(BSER, VOL9, SB9, 7, '北宋 · 1044 年 ·《武经总要》'), 7),
 'B27_片尾': (titles.closing(BSER, VOL9, SB9, 7, '下集：为什么推和拉都在吹风？'), 7),
 'B28_双动': (b28_double, 22), 'B28_连续送风': (b28_flow, 22),
 'B28_片头': (titles.opening(BSER, VOL9, SB9, 8, '明 · 1637 年 ·《天工开物》'), 7),
 'B28_片尾': (titles.closing(BSER, VOL9, SB9, 8, '下集：一张纸币，怎么防伪？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
