"""第四十七季（第二十层：厨房抽屉）第三批：E248 擀面杖、E249 刨丝器、E250 胡椒磨 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s47a import S47A, SER47, VOL47, STEEL

DOUGH = (230, 205, 150)
WOOD = (190, 140, 90)
SOAP = (170, 210, 220)
SALT = (235, 235, 230)


# ---------------------------------------------------------------- E248 擀面杖
def e248_line(c, t, i):
    corner_tag(c, '第 248 集 · 力集中在一条线上')
    c.text(60, 96, '手掌按下去，力摊在一大片面上；擀面杖只碰到一条细线，同样的力集中在这条线上，把面往前推开', 'serif', 36, INK)
    ph = (t % 11) / 11
    for j, (lab, rod) in enumerate([('手掌：力摊在一大片上', False), ('擀面杖：力集中在一条线', True)]):
        cx, base = 480 + j * 960, 760
        if not rod:
            h = 120 - 30 * min(1.0, ph * 2)
            w = 200 + 50 * min(1.0, ph * 2)
            c.rect(cx - w, base - h, cx + w, base, fill=mix(BG, DOUGH, 1.0), r=30)
            c.rect(cx - 150, base - h - 70, cx + 150, base - h, fill=mix(BG, (230, 190, 160), 0.9), r=30)
            for k in range(7):
                x = cx - 120 + k * 40
                c.arrow(x, base - h - 110, x, base - h - 74, SPARK, 3, 10)
        else:
            x = cx - 240 + 480 * ph
            for k in range(60):
                xx = cx - 300 + k * 10
                hh = 40 + 80 * max(0.0, min(1.0, (xx - x) / 70))
                c.rect(xx, base - hh, xx + 10, base, fill=mix(BG, DOUGH, 1.0))
            c.ellipse(x, base - 80, 40, 40, fill=mix(BG, WOOD, 1.0))
            c.arrow(x, base - 220, x, base - 130, SPARK, 6, 16)
            c.text(x, base - 250, '力', 'bold', 24, SPARK, 'mm')
            c.arrow(x + 50, base - 160, x + 130, base - 160, GREEN, 4, 12)
            c.text(x + 140, base - 160, '推开', 'bold', 22, GREEN, 'lm')
        c.text(cx, 900, lab, 'bold', 28, GREEN if rod else NRED, 'mm')
    caps(c, t, [(0, 7, '手掌按一下，力分到整个掌心那么大的面上，面团只是稍微扁一点'),
                (7.2, 14, '擀面杖和面只接触一条细线，压强大得多，面在杖下被压薄、往前挤'),
                (14.2, 22, '杖是滚着走的，几乎没有摩擦，可以来回擀很多次（用橡皮泥代替面团）')], y=1010)


def e248_turn(c, t, i):
    corner_tag(c, '第 248 集 · 转着方向擀才圆')
    c.text(60, 96, '只朝一个方向擀，面会变成长条；每擀一下把面转 90°，四个方向都推开，才越擀越圆', 'serif', 36, INK)
    n = min(20, int(t / 22 * 24))
    for j, (lab, turn) in enumerate([('只朝一个方向：变成长条', False), ('每次转 90°：越擀越圆', True)]):
        cx, cy = 480 + j * 960, 520
        A = 1.0 + 0.05 * n
        if turn:
            rx = ry = 110 * math.sqrt(A)
        else:
            rx, ry = 110 * A, 110 / math.sqrt(A) * 1.0
            ry = max(40, 110 * 1.0 / A * 1.3)
        c.ellipse(cx, cy, rx, ry, fill=mix(BG, DOUGH, 1.0))
        if turn:
            ang = (n % 2) * math.pi / 2
        else:
            ang = 0
        dx, dy = math.cos(ang), math.sin(ang)
        c.line([(cx - 200 * dy, cy + 200 * dx - 0), (cx + 200 * dy, cy - 200 * dx)], mix(BG, WOOD, 1.0), 26)
        c.text(cx, 830, lab, 'bold', 28, GREEN if turn else NRED, 'mm')
    c.text(960, 900, f'擀了 {n} 下（示意，以实测为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '两团一样重的橡皮泥，各擀 20 下'),
                (7.2, 14, '擀面杖只把面往和它垂直的方向推开，一直一个方向就越来越长'),
                (14.2, 22, '每次转 90°，四面都被推开，面就又薄又圆（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E249 刨丝器
def e249_blades(c, t, i):
    corner_tag(c, '第 249 集 · 每个小孔都是一把小刀')
    c.text(60, 96, '刨丝器的每个小孔边上都翘起一道锋利的边：推一下，几十把小刀同时各切下一条细丝', 'serif', 36, INK)
    y0 = 600
    c.rect(200, y0, 1720, y0 + 30, fill=mix(BG, STEEL, 0.9))
    holes = [260 + k * 120 for k in range(13)]
    for x in holes:
        c.rect(x, y0, x + 50, y0 + 30, fill=BG)
        c.poly([(x + 50, y0), (x + 58, y0), (x + 36, y0 - 20), (x + 28, y0 - 20)], mix(BG, STEEL, 1.0))
    ph = (t % 7) / 7
    bx = 300 + 1100 * ph
    c.rect(bx - 120, y0 - 260, bx + 120, y0 - 2, fill=mix(BG, SOAP, 1.0), r=14)
    c.arrow(bx + 140, y0 - 130, bx + 240, y0 - 130, SPARK, 6, 16)
    c.text(bx, y0 - 300, '往前推', 'bold', 26, SPARK, 'mm')
    random.seed(3)
    for x in holes:
        if x < bx + 120 and x + 50 > 300:
            m = max(0.0, min(1.0, (bx + 120 - x) / 400))
            c.rect(x + 18, y0 + 30, x + 30, y0 + 30 + 220 * m, fill=mix(BG, SOAP, 0.95), r=4)
    c.text(960, 940, '一推：好多把小刀一起切（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '仔细看小孔：一边是平的，另一边往上翘起，像一把小刨刀'),
                (7.2, 14, '肥皂推过去，每个翘边各削下一条，从孔里掉下去'),
                (14.2, 22, '一面上有几十个孔，一推就是几十条；孔边很锋利，只由大人操作')], y=1010)


def e249_area(c, t, i):
    corner_tag(c, '第 249 集 · 切得越碎，表面越多')
    c.text(60, 96, '一块切成两半，多出两个切面；切成细丝，碰到水的表面就多出好多倍，所以溶得快', 'serif', 36, INK)
    k = int((t % 21) // 7)
    cx, cy = 600, 540
    S = 300
    n = [1, 2, 8][k]
    gap = 14
    w = (S - gap * (n - 1)) / n
    for a in range(n):
        for b in range(1 if n < 8 else 2):
            x0 = cx - S / 2 + a * (w + gap)
            if n < 8:
                c.rect(x0, cy - S / 2, x0 + w, cy + S / 2, fill=mix(BG, SOAP, 1.0), r=4)
            else:
                h = (S - gap) / 2
                y0 = cy - S / 2 + b * (h + gap)
                c.rect(x0, y0, x0 + w, y0 + h, fill=mix(BG, SOAP, 1.0), r=3)
    area = {1: 6, 2: 8, 8: 6 + 2 * 7 + 2 * 1 * 4}[n]
    labs = ['一整块', '切成两半', '切成细条']
    c.text(cx, cy + 230, labs[k], 'bold', 30, INK, 'mm')
    for j, (nm, v) in enumerate([('一整块', 6), ('切成两半', 8), ('切成细条', 6 + 2 * 7 + 8)]):
        y = 360 + j * 90
        c.rect(1200, y, 1200 + 600 * v / 28, y + 40, fill=GREEN if j == k else LINE, r=6)
        c.text(1180, y + 20, nm, 'sans', 24, MUTED, 'rm')
        c.text(1210 + 600 * v / 28, y + 20, f'{v} 份', 'bold', 24, INK, 'lm')
    c.text(1500, 680, '表面积（每面算 1 份，示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一个小方块有 6 个面'),
                (7.2, 14, '切一刀，多出 2 个新切面'),
                (14.2, 22, '切得越碎，新切面越多，泡在温水里溶得越快（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E250 胡椒磨
def _mill(c, cx, cy, gap, t):
    H = 420
    c.poly([(cx - 200, cy - H / 2), (cx + 200, cy - H / 2), (cx + 140 + gap, cy + H / 2), (cx - 140 - gap, cy + H / 2)], mix(BG, STEEL, 0.55))
    c.poly([(cx - 150, cy - H / 2), (cx + 150, cy - H / 2), (cx + 140, cy + H / 2), (cx - 140, cy + H / 2)], BG)
    c.poly([(cx - 110, cy - H / 2 - 20), (cx + 110, cy - H / 2 - 20), (cx + 130 - 4, cy + H / 2), (cx - 130 + 4, cy + H / 2)], mix(BG, STEEL, 1.0))
    for k in range(9):
        y = cy - H / 2 + k * H / 9 + (t * 40) % (H / 9)
        c.line([(cx - 100, y), (cx + 100, y + 20)], mix(BG, STEEL, 0.7), 3)
    return H


def e250_gap(c, t, i):
    corner_tag(c, '第 250 集 · 上宽下窄的一道缝')
    c.text(60, 96, '胡椒磨里，带斜齿的圆锥套在齿圈里：上面的缝宽，颗粒进得去；越往下越窄，最后被磨碎', 'serif', 36, INK)
    cx, cy = 760, 540
    H = 420
    c.poly([(cx - 260, cy - H / 2), (cx + 260, cy - H / 2), (cx + 170, cy + H / 2), (cx - 170, cy + H / 2)], mix(BG, STEEL, 0.55))
    c.poly([(cx - 200, cy - H / 2), (cx + 200, cy - H / 2), (cx + 150, cy + H / 2), (cx - 150, cy + H / 2)], BG)
    c.poly([(cx - 90, cy - H / 2 - 30), (cx + 90, cy - H / 2 - 30), (cx + 138, cy + H / 2), (cx - 138, cy + H / 2)], mix(BG, STEEL, 1.0))
    random.seed(5)
    for k in range(14):
        ph = ((t * 0.12) + k / 14) % 1.0
        y = cy - H / 2 + H * ph
        half_gap = (200 - 50 * ph) - (90 + 48 * ph)
        size = max(4, min(30, half_gap * 0.6))
        side = 1 if k % 2 else -1
        x = cx + side * ((90 + 48 * ph) + half_gap / 2)
        c.ellipse(x, y, size, size, fill=mix(BG, SALT, 1.0))
    for k in range(10):
        x = cx + random.uniform(-150, 150)
        y = cy + H / 2 + 20 + ((t * 60 + k * 40) % 200)
        c.ellipse(x, y, 4, 4, fill=mix(BG, SALT, 0.9))
    c.text(cx + 300, cy - H / 2 + 20, '上面缝宽：大颗粒进来', 'bold', 24, INK, 'lm')
    c.text(cx + 260, cy + H / 2 - 20, '最下面最窄：决定粗细', 'bold', 24, SPARK, 'lm')
    caps(c, t, [(0, 7, '转动手柄，圆锥在齿圈里转，斜齿把颗粒一点点往下带'),
                (7.2, 14, '越往下缝越窄，颗粒被挤碎、再挤碎'),
                (14.2, 22, '只有比最窄的缝还小的碎粒才能掉出来（用粗盐代替胡椒，不吃）')], y=1010)


def e250_screw(c, t, i):
    corner_tag(c, '第 250 集 · 拧螺母，调最窄的缝')
    c.text(60, 96, '顶上的螺母一拧，圆锥就沿着螺纹上下移动一点：往上，最窄的缝变大，磨得粗；往下，变细', 'serif', 36, INK)
    if t < 7.2:
        u = 0.5
    elif t < 14.2:
        u = 0.5 + 0.5 * min(1.0, (t - 7.2) / 3)
    else:
        u = 1.0 - min(1.0, (t - 14.2) / 3)
    lift = 40 * u
    cx, cy = 760, 700
    H = 320
    c.poly([(cx - 220, cy - H / 2), (cx + 220, cy - H / 2), (cx + 150, cy + H / 2), (cx - 150, cy + H / 2)], mix(BG, STEEL, 0.55))
    c.poly([(cx - 170, cy - H / 2), (cx + 170, cy - H / 2), (cx + 130, cy + H / 2), (cx - 130, cy + H / 2)], BG)
    top = cy - H / 2 - 30 - lift
    bot = cy + H / 2 - lift
    wtop, wbot = 80, 118
    c.poly([(cx - wtop, top), (cx + wtop, top), (cx + wbot, bot), (cx - wbot, bot)], mix(BG, STEEL, 1.0))
    c.line([(cx, top - 160), (cx, top)], mix(BG, STEEL, 0.9), 10)
    for k in range(8):
        y = top - 150 + k * 18
        c.line([(cx - 14, y), (cx + 14, y + 8)], mix(BG, INK, 0.6), 2)
    c.ellipse(cx, top - 160, 50, 22, fill=mix(BG, (210, 170, 90), 1.0))
    c.text(cx + 80, top - 160, '螺母', 'bold', 24, SPARK, 'lm')
    ring_half = 130 + (150 - 130) * 0
    gap = 130 + 40 * (lift / 360) - (wbot - (wbot - wtop) * (lift / (H + 30)))
    gap = max(2, 12 + lift * 0.6)
    c.text(1500, 420, f'最窄的缝：{gap / 10:.1f} 毫米（示意）', 'bold', 32, INK, 'mm')
    c.text(1500, 480, '磨出来：' + ('粗' if u > 0.6 else ('细' if u < 0.4 else '中等')), 'bold', 32, NRED if u > 0.6 else (GREEN if u < 0.4 else INK), 'mm')
    caps(c, t, [(0, 7, '圆锥连在一根带螺纹的轴上，顶上的螺母一拧，圆锥就往上或往下挪'),
                (7.2, 14, '圆锥往上提：它下端和齿圈的缝变宽，磨出粗粒'),
                (14.2, 22, '圆锥往下压：缝变窄，磨出细粉（示意，以实测为准）')], y=1010)


CLIPS = {
 'E248_线压': (e248_line, 22), 'E248_转向': (e248_turn, 22),
 'E248_片头': (titles.opening(SER47, VOL47, S47A, 6, '中国古代已用擀面杖擀饼'), 7),
 'E248_片尾': (titles.closing(SER47, VOL47, S47A, 6, '下集：刨丝器上没有一把正经的刀，怎么刨出丝？'), 7),
 'E249_小刀': (e249_blades, 22), 'E249_表面积': (e249_area, 22),
 'E249_片头': (titles.opening(SER47, VOL47, S47A, 7, '16 世纪欧洲已用金属刨丝器刨奶酪'), 7),
 'E249_片尾': (titles.closing(SER47, VOL47, S47A, 7, '下集：胡椒磨的粗细，是怎么调出来的？'), 7),
 'E250_间隙': (e250_gap, 22), 'E250_螺纹': (e250_screw, 22),
 'E250_片头': (titles.opening(SER47, VOL47, S47A, 8, '19 世纪法国开始生产带螺旋齿的胡椒磨'), 7),
 'E250_片尾': (titles.closing(SER47, VOL47, S47A, 8, '下集：用吸管喝水，水为什么会自己往上走？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
