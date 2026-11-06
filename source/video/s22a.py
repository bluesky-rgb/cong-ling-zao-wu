"""第二十二季（古法解密 8.0：转、浮、住、玩）第一批：B80 水碓、B81 辘轳、B82 羊皮筏子 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB22 = [('B80', '水碓'), ('B81', '辘轳'), ('B82', '羊皮筏子'), ('B83', '窑洞'), ('B84', '弹棉花'),
        ('B85', '香篆钟'), ('B86', '冰嬉'), ('B87', '空竹'), ('B88', '毽子'), ('B89', '投壶')]
VOL22 = '第二十二季 · 古法解密 8.0'
WOOD = (175, 125, 75)
DARKWOOD = (130, 90, 55)
STONE = (140, 140, 135)
WATER = (80, 140, 200)
RICE = (235, 230, 210)
ROPE = (210, 190, 140)
SKIN = (200, 160, 110)


def rot(pts, cx, cy, a):
    ca, sa = math.cos(a), math.sin(a)
    return [(cx + (x - cx) * ca - (y - cy) * sa, cy + (x - cx) * sa + (y - cy) * ca) for x, y in pts]


# ---------------------------------------------------------------- B80 水碓
def _pestle(c, px, py, L1, L2, ang, mortar=True):
    """以支点 (px,py) 画碓杆；ang>0 时碓头一端抬起。L1：拨板一侧，L2：碓头一侧。"""
    x1, y1 = px - L1 * math.cos(ang), py + L1 * math.sin(ang)
    x2, y2 = px + L2 * math.cos(ang), py - L2 * math.sin(ang)
    c.line([(x1, y1), (x2, y2)], WOOD, 14)
    c.rect(x2 - 22, y2, x2 + 22, y2 + 90, fill=STONE, r=8)
    c.poly([(px - 26, py + 60), (px + 26, py + 60), (px, py)], DARKWOOD)
    if mortar:
        c.rect(x2 - 60, 760, x2 + 60, 840, fill=(110, 110, 105), r=10)
        c.rect(x2 - 44, 760, x2 + 44, 790, fill=RICE, r=6)
    return (x1, y1), (x2, y2)


def b80_cam(c, t, i):
    corner_tag(c, 'B80 · 一圈压几下')
    c.text(60, 96, '轴上的拨板压下碓杆尾巴，碓头抬起；拨板一滑开，碓头就砸下去', 'serif', 40, INK)
    n = 1 if t < 7.5 else (2 if t < 15 else 3)
    ax, ay, R = 420, 560, 70
    th = t * 1.6
    c.ellipse(ax, ay, R, R, fill=DARKWOOD, outline=WOOD, width=4)
    tip = None
    for k in range(n):
        a = th + k * 2 * math.pi / n
        pts = rot([(ax + R - 6, ay - 14), (ax + R + 70, ay - 10), (ax + R + 70, ay + 10), (ax + R - 6, ay + 14)], ax, ay, a)
        c.poly(pts, WOOD)
        # 拨板端点
        ex, ey = ax + (R + 70) * math.cos(a), ay + (R + 70) * math.sin(a)
        if 0 < math.atan2(ey - ay, ex - ax) < math.pi / 2 and ex > ax:
            tip = max(tip or 0, ey)
    px, py = 900, 560
    # 杆尾在 x≈560 处，被拨板压下时向下偏转
    phase = [((th + k * 2 * math.pi / n) % (2 * math.pi)) for k in range(n)]
    lift = 0.0
    for ph in phase:
        if ph < 1.25:
            lift = max(lift, math.asin(min(1.0, (R + 70) * math.sin(ph) / 340)))
    _pestle(c, px, py, 340, 520, lift)
    c.text(ax, ay + 180, '横轴（被水轮带着转）', 'sans', 22, MUTED, 'mm')
    c.text(px, py + 100, '支点', 'sans', 20, MUTED, 'mm')
    c.rect(1500, 200, 1840, 340, fill=SHEET, r=12)
    c.text(1670, 240, f'拨板：{n} 片', 'bold', 28, INK, 'mm')
    c.text(1670, 296, f'每转一圈砸 {n} 下', 'sans', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '横轴上装一片拨板：每转一圈，拨板压一次碓杆尾巴，碓头抬起来又落下'),
                (7.2, 14, '装两片，一圈就砸两下；拨板一滑开，碓头靠自己的重量砸进臼里'),
                (14.2, 22, '这就是凸轮：把一直转的圈，变成一起一落。碓杆本身是一根杠杆')], y=1010)


def b80_mill(c, t, i):
    corner_tag(c, 'B80 · 一条水，带三把碓')
    c.text(60, 96, '一根长轴上错开装拨板：几把碓轮流起落，水轮受力更均匀', 'serif', 40, INK)
    wx, wy, WR = 260, 600, 170
    for k in range(18):
        s_ = (t * 0.6 + k / 18) % 1
        c.ellipse(60 + 400 * s_, 800 + 10 * math.sin(s_ * 9 + t), 10, 6, fill=WATER)
    c.rect(40, 780, 520, 860, fill=mix(BG, WATER, 0.35))
    th = t * 1.2
    c.ellipse(wx, wy, WR, WR, outline=WOOD, width=8)
    for k in range(10):
        a = th + k * math.pi / 5
        c.line([(wx, wy), (wx + WR * math.cos(a), wy + WR * math.sin(a))], WOOD, 4)
        c.rect(wx + WR * math.cos(a) - 18, wy + WR * math.sin(a) - 18, wx + WR * math.cos(a) + 18, wy + WR * math.sin(a) + 18, fill=DARKWOOD)
    c.ellipse(wx, wy, 26, 26, fill=DARKWOOD)
    seg(c, [(wx + 30, wy), (620, wy)], MUTED, 3)
    for k in range(3):
        ax = 620 + k * 430
        if k:
            seg(c, [(ax - 430 + 30, wy), (ax - 30, wy)], MUTED, 3)
        off = k * 2 * math.pi / 3
        a = th + off
        c.ellipse(ax, wy, 28, 28, fill=DARKWOOD, outline=WOOD, width=3)
        c.line([(ax, wy), (ax + 70 * math.cos(a), wy + 70 * math.sin(a))], WOOD, 12)
        ph = a % (2 * math.pi)
        lift = math.asin(min(1.0, 70 * math.sin(ph) / 100)) if ph < 1.4 else 0.0
        px, py = ax + 170, wy
        tx, ty = px - 100 * math.cos(lift), py + 100 * math.sin(lift)
        hx, hy = px + 170 * math.cos(lift), py - 170 * math.sin(lift)
        c.line([(tx, ty), (hx, hy)], WOOD, 10)
        c.rect(hx - 16, hy, hx + 16, hy + 60, fill=STONE, r=6)
        c.poly([(px - 18, py + 40), (px + 18, py + 40), (px, py)], DARKWOOD)
        c.rect(px + 130, wy + 60, px + 210, wy + 100, fill=(110, 110, 105), r=8)
        c.text(ax + 150, wy + 160, f'第 {k + 1} 把碓', 'sans', 22, MUTED, 'mm')
    c.text(1050, wy - 200, '虚线：同一根横轴（三组拨板各错开 120°）', 'sans', 22, MUTED, 'mm')
    c.text(wx, wy + 270, '水轮', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '水冲着轮子的叶板，水轮带着一根长长的横轴一直转'),
                (7.2, 14, '轴上错开装几组拨板，几把碓轮流起落：这一把刚抬起，那一把正落下'),
                (14.2, 22, '东汉桓谭就记过这种机器，说它的力气比人踩碓大好多倍（拍摄前核对）。和第 4 集水排是一家')], y=1010)


# ---------------------------------------------------------------- B81 辘轳
def b81_wheel(c, t, i):
    corner_tag(c, 'B81 · 摇把越长越省劲')
    c.text(60, 96, '桶的重量乘轴的半径 = 手的力乘摇把的长度', 'serif', 40, INK)
    cx, cy, r = 620, 420, 40
    Rh = 120 + 120 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi * 1.0))
    th = t * 1.3
    c.rect(cx - 260, cy - 20, cx - 220, 900, fill=DARKWOOD)
    c.rect(cx + 220, cy - 20, cx + 260, 900, fill=DARKWOOD)
    c.rect(cx - 220, cy - r, cx + 220, cy + r, fill=WOOD, r=8)
    hx, hy = cx + 260 + 30, cy
    ex, ey = hx + Rh * math.cos(th), hy + Rh * math.sin(th)
    c.line([(cx + 220, cy), (hx, hy)], DARKWOOD, 10)
    c.line([(hx, hy), (ex, ey)], (200, 160, 110), 10)
    c.ellipse(ex, ey, 14, 14, fill=SPARK)
    c.ellipse(hx, hy, Rh, Rh, outline=mix(BG, SPARK, 0.35), width=2)
    c.line([(cx, cy + r), (cx, 760)], ROPE, 4)
    c.rect(cx - 50, 760, cx + 50, 860, fill=(120, 130, 150), r=10)
    c.text(cx, 810, '桶', 'bold', 24, INK, 'mm')
    W = 10.0
    F = W * r / Rh
    c.rect(1280, 260, 1840, 640, fill=SHEET, r=14)
    c.text(1560, 300, '力的账（示意数字）', 'bold', 26, INK, 'mm')
    c.text(1320, 370, f'桶重：{W:.0f} 牛', 'sans', 26, INK, 'lm')
    c.text(1320, 430, f'轴半径：{r / 10:.0f} 厘米', 'sans', 26, INK, 'lm')
    c.text(1320, 490, f'摇把长：{Rh / 10:.0f} 厘米', 'sans', 26, SPARK, 'lm')
    c.text(1320, 570, f'手要用的力 ≈ {F:.1f} 牛', 'bold', 30, GREEN, 'lm')
    c.rect(1320, 600, 1320 + 480 * F / W, 620, fill=GREEN)
    caps(c, t, [(0, 7, '辘轳是一根绕着绳子的横轴，一头装着摇把'),
                (7.2, 14, '轴细、摇把长：桶的重量乘轴的半径，等于手的力乘摇把的长度'),
                (14.2, 22, '摇把是轴半径的 6 倍，手上只要用桶重的六分之一。它不是滑轮，是「轮轴」')], y=1010)


def b81_turns(c, t, i):
    corner_tag(c, 'B81 · 省了力，多走了路')
    c.text(60, 96, '桶升高 1 米，手要转好多圈：力小了，路长了，功没变', 'serif', 40, INK)
    turns = min(4.0, t * 0.3)
    r, Rh = 4, 24
    lift = 2 * math.pi * r * turns / 100
    hand = 2 * math.pi * Rh * turns / 100
    ground = 860
    c.line([(200, ground), (900, ground)], LINE, 4)
    c.rect(300, ground - 0, 340, ground, fill=LINE)
    by = ground - 60 - min(1.0, lift / 1.0) * 500
    c.line([(520, 220), (520, by)], ROPE, 4)
    c.rect(470, by, 570, by + 60, fill=(120, 130, 150), r=8)
    for k in range(5):
        y = ground - 60 - k * 125
        c.line([(600, y), (620, y)], MUTED, 2)
        c.text(630, y, f'{k * 25} 厘米', 'mono', 18, MUTED, 'lm')
    c.ellipse(520, 220, 40, 40, fill=WOOD)
    c.rect(1060, 260, 1840, 720, fill=SHEET, r=14)
    c.text(1450, 300, '同一件事，两种算法', 'bold', 26, INK, 'mm')
    c.text(1100, 380, f'摇了 {turns:.1f} 圈', 'mono', 30, INK, 'lm')
    c.text(1100, 450, f'桶升高 {min(lift, 1.0) * 100:.0f} 厘米', 'sans', 28, INK, 'lm')
    c.text(1100, 520, f'手走了 {min(hand, 6.0):.1f} 米', 'sans', 28, SPARK, 'lm')
    c.text(1100, 620, '力 × 路 ≈ 一样多（不算摩擦）', 'bold', 28, GREEN, 'lm')
    caps(c, t, [(0, 7, '轴的半径 4 厘米，摇把 24 厘米：手上的力只要桶重的六分之一'),
                (7.2, 14, '可是桶升高 1 米，手要转大约 4 圈，走了 6 米'),
                (14.2, 22, '力小了六倍，路长了六倍：省力的机器都不省功，第 39 集滑轮组也是这样')], y=1010)


# ---------------------------------------------------------------- B82 羊皮筏子
def b82_displace(c, t, i):
    corner_tag(c, 'B82 · 空气把水挤开')
    c.text(60, 96, '皮囊压进水里多深，就挤开多少水；挤开的水有多重，托力就有多大', 'serif', 40, INK)
    wl = 560
    c.rect(100, wl, 1100, 900, fill=mix(BG, WATER, 0.45))
    c.line([(100, wl), (1100, wl)], WATER, 3)
    load = min(1.0, max(0.0, (t - 2) / 14))
    depth = 40 + 110 * load
    cx = 600
    c.ellipse(cx, wl - 70 + depth, 230, 110, fill=SKIN, outline=DARKWOOD, width=3)
    c.rect(cx - 260, wl - 190 + depth, cx + 260, wl - 166 + depth, fill=WOOD)
    nb = int(load * 8)
    for k in range(nb):
        c.rect(cx - 200 + k * 50, wl - 230 + depth, cx - 160 + k * 50, wl - 190 + depth, fill=(150, 150, 160), r=4)
    c.arrow(cx, wl - 260 + depth, cx, wl - 260 + depth + 90 + 60 * load, NRED, 5, 18)
    c.text(cx + 30, wl - 250 + depth, '重量', 'bold', 22, NRED, 'lm')
    c.arrow(cx, wl + depth + 60, cx, wl + depth - 30 - 60 * load, GREEN, 5, 18)
    c.text(cx + 30, wl + depth + 50, '水的托力', 'bold', 22, GREEN, 'lm')
    c.rect(1240, 300, 1840, 700, fill=SHEET, r=14)
    c.text(1540, 340, '加货，吃水变深', 'bold', 26, INK, 'mm')
    c.text(1280, 420, f'货物：{nb} 块', 'sans', 26, INK, 'lm')
    c.text(1280, 480, f'吃水：{depth / 10:.0f} 厘米（示意）', 'sans', 26, INK, 'lm')
    c.text(1280, 560, '挤开的水 = 筏 + 货的重量', 'bold', 26, GREEN, 'lm')
    c.text(1280, 620, '皮囊全没进水里，就再也托不住了', 'sans', 22, NRED, 'lm')
    caps(c, t, [(0, 7, '吹满气的羊皮很轻，压进水里一点，就挤开一大块水'),
                (7.2, 14, '往上加货，筏子沉得深一点，挤开更多的水，托力也跟着变大'),
                (14.2, 22, '一直加到皮囊整个没进水里，托力就到头了：这和曹冲称象的船是同一个道理')], y=1010)


def _raft(c, cx, cy, ang, floats, load_dx):
    W = 520
    deck = rot([(cx - W / 2, cy - 12), (cx + W / 2, cy - 12), (cx + W / 2, cy + 12), (cx - W / 2, cy + 12)], cx, cy, ang)
    c.poly(deck, WOOD)
    for fx, rx, ry in floats:
        px, py = rot([(cx + fx, cy + 12 + ry)], cx, cy, ang)[0]
        c.ellipse(px, py, rx, ry, fill=SKIN, outline=DARKWOOD, width=2)
    lx, ly = rot([(cx + load_dx, cy - 52)], cx, cy, ang)[0]
    c.rect(lx - 40, ly - 40, lx + 40, ly + 40, fill=(150, 150, 160), r=6)


def b82_stable(c, t, i):
    corner_tag(c, 'B82 · 一只大囊，还是十几只小囊？')
    c.text(60, 96, '货物偏到一边时，分开放的小气囊能「顶」回来，一只大囊却容易翻', 'serif', 40, INK)
    wl = 620
    c.rect(60, wl, 1860, 940, fill=mix(BG, WATER, 0.45))
    c.line([(60, wl), (1860, wl)], WATER, 3)
    dx = 220 * min(1.0, max(0.0, (t - 3) / 8))
    a_big = -math.radians(4 + 34 * (dx / 220) ** 1.5)
    a_small = -math.radians(9 * dx / 220)
    _raft(c, 520, wl - 40, a_big, [(0, 120, 70)], dx)
    _raft(c, 1400, wl - 40, a_small, [(-210, 50, 40), (-70, 50, 40), (70, 50, 40), (210, 50, 40)], dx)
    c.text(520, 300, '一只大气囊', 'bold', 28, INK, 'mm')
    c.text(1400, 300, '四只小气囊分开绑', 'bold', 28, INK, 'mm')
    c.text(520, 350, f'倾斜 {abs(math.degrees(a_big)):.0f}°（示意）', 'mono', 24, NRED, 'mm')
    c.text(1400, 350, f'倾斜 {abs(math.degrees(a_small)):.0f}°（示意）', 'mono', 24, GREEN, 'mm')
    caps(c, t, [(0, 7, '两只筏子总浮力一样，一只底下是一只大气囊，一只是四只小气囊分开绑'),
                (7.2, 14, '把货推到一边：偏的那一侧小气囊被压深、托力变大，把筏子顶回来'),
                (14.2, 22, '一只大气囊在中间，没东西在边上顶它，就容易翻。黄河上的皮筏，常常绑十几只羊皮（以实测为准）')], y=1010)


CLIPS = {
 'B80_拨板': (b80_cam, 22), 'B80_水轮': (b80_mill, 22),
 'B80_片头': (titles.opening(BSER, VOL22, SB22, 0, '东汉桓谭《新论》· 明《天工开物》'), 7),
 'B80_片尾': (titles.closing(BSER, VOL22, SB22, 0, '下集：为什么摇辘轳打水，比直接拉绳省劲？'), 7),
 'B81_轮轴': (b81_wheel, 22), 'B81_圈数': (b81_turns, 22),
 'B81_片头': (titles.opening(BSER, VOL22, SB22, 1, '春秋辘轳 · 元《王祯农书》'), 7),
 'B81_片尾': (titles.closing(BSER, VOL22, SB22, 1, '下集：几张充了气的羊皮，怎么能载人过黄河？'), 7),
 'B82_排水': (b82_displace, 22), 'B82_稳定': (b82_stable, 22),
 'B82_片头': (titles.opening(BSER, VOL22, SB22, 2, '黄河羊皮筏子 · 《水经注》革囊渡河'), 7),
 'B82_片尾': (titles.closing(BSER, VOL22, SB22, 2, '下集：窑洞为什么冬暖夏凉？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
