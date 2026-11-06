"""第二十季（古法解密 7.0）第二批：B73 竹编、B74 曹冲称象、B75 水准 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s20a import SB20, VOL20, WOOD

BAMBOO = (200, 175, 110)
WATER = (80, 140, 200)
BOAT = (160, 110, 70)
STONE = (150, 150, 155)

# ---------------------------------------------------------------- B73 竹编
def b73_shear(c, t, i):
    corner_tag(c, 'B73 · 斜着推一推')
    c.text(60, 96, '方孔一推就歪；有三角形的网，推不动', 'serif', 40, INK)
    sh = 0.45 * fade(t, 4, 10)
    # 方孔
    ox, oy, n, s = 200, 320, 5, 100
    c.text(ox + n * s / 2, oy - 40, '方孔网', 'bold', 28, INK, 'mm')
    P = lambda i_, j_: (ox + i_ * s + sh * (n - j_) * s * 0.5, oy + j_ * s)
    for j in range(n + 1):
        c.line([P(0, j), P(n, j)], BAMBOO, 6)
    for i_ in range(n + 1):
        c.line([P(i_, 0), P(i_, n)], BAMBOO, 6)
    c.line([(ox - 20, oy + n * s + 10), (ox + n * s + 20, oy + n * s + 10)], LINE, 4)
    if sh > 0:
        c.arrow(P(0, 0)[0] - 120, oy, P(0, 0)[0] - 20, oy, NRED, 5, 16)
        c.text(ox + n * s / 2, oy + n * s + 60, '歪成菱形', 'bold', 28, mix(BG, NRED, fade(t, 6, 8)), 'mm')
    # 三角网
    ox2, oy2 = 1100, 320
    h = s * math.sqrt(3) / 2
    small = sh * 0.06
    c.text(ox2 + n * s / 2, oy2 - 40, '三向编（处处是三角形）', 'bold', 28, INK, 'mm')
    Q = lambda i_, j_: (ox2 + i_ * s + (j_ % 2) * s / 2 * 0 + (n - j_) * s / 2 * 0 + j_ * s / 2 * 0 + small * (n - j_) * s, oy2 + j_ * h * 500 / (n * h))
    rows = 6
    pts = {}
    for j in range(rows):
        for i_ in range(n + 1):
            x = ox2 + i_ * s - (j % 2) * s / 2 + small * (rows - 1 - j) * s
            y = oy2 + j * h * 1.15
            pts[(i_, j)] = (x, y)
    for j in range(rows):
        c.line([pts[(0, j)], pts[(n, j)]], BAMBOO, 6)
    for j in range(rows - 1):
        for i_ in range(n + 1):
            a = pts[(i_, j)]
            if j % 2 == 0:
                for di in (0, 1):
                    if (i_ + di, j + 1) in pts and 0 <= i_ + di <= n:
                        c.line([a, pts[(i_ + di, j + 1)]], BAMBOO, 4)
            else:
                for di in (-1, 0):
                    if (i_ + di, j + 1) in pts and 0 <= i_ + di <= n:
                        c.line([a, pts[(i_ + di, j + 1)]], BAMBOO, 4)
    if sh > 0:
        c.arrow(ox2 - 140, oy2, ox2 - 40, oy2, NRED, 5, 16)
        c.text(ox2 + n * s / 2, oy2 + 5 * h * 1.15 + 60, '几乎不变形', 'bold', 28, mix(BG, GREEN, fade(t, 6, 8)), 'mm')
    caps(c, t, [(0, 6, '方孔的网，每个格子是四边形：四根边一样长，角度却能随便变'),
                (6.2, 13, '从侧面一推，整张网就歪成一片菱形'),
                (13.2, 22, '三角形三条边定了，角度就定了：编进了三角形的网，推也推不歪')], y=1010)

def b73_weave(c, t, i):
    corner_tag(c, 'B73 · 三个方向的篾')
    c.text(60, 96, '六角眼：三组竹篾，各差 60 度，互相压着', 'serif', 40, INK)
    cx, cy = 760, 590
    d = 70
    L = 900
    for fam, (ang, col) in enumerate(((0, BAMBOO), (60, mix(BAMBOO, (230, 150, 80), 0.4)), (120, mix(BAMBOO, (120, 170, 90), 0.4)))):
        a = fade(t, 1 + fam * 4, 3 + fam * 4)
        if a <= 0: continue
        th = math.radians(ang)
        ux, uy = math.cos(th), math.sin(th)
        nx, ny = -uy, ux
        Rc = 340
        for k in range(-6, 7):
            off = k * d + d / 2 * (fam == 0)
            if abs(off) >= Rc - 10: continue
            hl = math.sqrt(Rc * Rc - off * off)
            ox, oy = cx + nx * off, cy + ny * off
            c.line([(ox - ux * hl, oy - uy * hl), (ox + ux * hl, oy + uy * hl)], mix(BG, col, a), 14)
    b = fade(t, 13, 14)
    if b > 0:
        R = d / math.sqrt(3) * 1.02
        hx = [(cx + R * 2 * math.cos(math.radians(30 + 60 * k)) * 0 + R * math.cos(math.radians(60 * k)) * 1.0, cy + R * math.sin(math.radians(60 * k))) for k in range(6)]
        c.rect(1320, 300, 1860, 640, fill=mix(BG, SHEET, b), r=14)
        c.text(1590, 350, '每一根篾', 'bold', 28, mix(BG, INK, b), 'mm')
        c.text(1590, 420, '被另外两组压着、托着', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(1590, 480, '孔是六角形', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(1590, 540, '孔和孔之间全是小三角形', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 5, '先铺一组横着的竹篾'),
                (5.2, 13, '再铺两组，分别斜 60 度和 120 度，一上一下地穿插'),
                (13.2, 22, '三组篾交出一个个六角形的眼，眼和眼之间是小三角形：又轻、又透气、又推不歪')], y=1010)

# ---------------------------------------------------------------- B74 曹冲称象
def _boat(c, cx, wl, sink, load):
    W, H = 520, 120
    top = wl - H + sink
    c.poly([(cx - W / 2, top), (cx + W / 2, top), (cx + W / 2 - 60, top + H), (cx - W / 2 + 60, top + H)], BOAT)
    return top

def b74_boat(c, t, i):
    corner_tag(c, 'B74 · 让船吃到同一条水线')
    c.text(60, 96, '大象上船，船沉到一条线；换成石头，压到同一条线', 'serif', 40, INK)
    wl = 640
    if t < 5: load, kind = fade(t, 1, 4), 'ele'
    elif t < 8: load, kind = 1 - fade(t, 5, 7.5), 'ele'
    else:
        n = min(8, int(fade(t, 8, 17) * 8 + 1e-6))
        load, kind = n / 8, 'stone'
    sink = 70 * load
    cx = 760
    c.rect(80, wl, 1440, 980, fill=mix(BG, WATER, 0.45))
    top = _boat(c, cx, wl, sink, load)
    mark_y = top + 0  # boat frame
    line_y = wl - (70 * 1.0 - sink)  # where the water line is on the hull when fully loaded
    c.line([(cx - 250, top + 120 - 0 - (120 - 0) + 50), (cx + 250, top + 50)], NRED if t > 4 else mix(BG, NRED, fade(t, 3, 4)), 3)
    c.text(cx + 270, top + 50, '刻下的水线', 'sans', 22, NRED, 'lm')
    if kind == 'ele' and load > 0.02:
        ex, ey = cx, top - 110
        c.ellipse(ex, ey, 150, 100, fill=(150, 150, 160))
        c.ellipse(ex + 150, ey - 40, 60, 55, fill=(150, 150, 160))
        c.line([(ex + 190, ey - 10), (ex + 210, ey + 70)], (150, 150, 160), 18)
        for dx in (-90, -30, 40, 100):
            c.rect(ex + dx - 16, ey + 60, ex + dx + 16, top, fill=(150, 150, 160))
    if kind == 'stone':
        n = int(load * 8 + 1e-6)
        for k in range(n):
            x = cx - 200 + (k % 4) * 120
            y = top - 40 - (k // 4) * 70
            c.ellipse(x, y, 52, 34, fill=STONE, outline=INK, width=2)
        c.rect(1500, 300, 1860, 600, fill=SHEET, r=14)
        c.text(1680, 350, '石头', 'bold', 28, INK, 'mm')
        c.text(1680, 430, f'{n} 筐', 'mono', 40, SPARK, 'mm')
        c.text(1680, 520, '每筐分别过秤', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 5, '把大象赶上船，船往下一沉，在船帮上贴着水面刻一道线'),
                (5.2, 8, '大象下船，船浮了起来'),
                (8.2, 22, '往船上一筐筐搬石头，直到水面又到那道线：石头一筐筐称，加起来就是大象的重量')], y=1010)

def b74_archimedes(c, t, i):
    corner_tag(c, 'B74 · 排开多少水，就托起多重')
    c.text(60, 96, '船沉得越深，排开的水越多，水往上托的力就越大', 'serif', 40, INK)
    load = fade(t, 2, 10)
    cx, wl0 = 560, 560
    c.rect(260, 400, 860, 900, outline=INK, width=4)
    rise = 90 * load
    c.rect(264, wl0 - rise, 856, 896, fill=mix(BG, WATER, 0.5))
    W = 300
    sink = 30 + 110 * load
    top = wl0 - rise - 120 + sink
    c.poly([(cx - W / 2, top), (cx + W / 2, top), (cx + W / 2 - 40, top + 120), (cx - W / 2 + 40, top + 120)], BOAT)
    for k in range(int(load * 5)):
        c.ellipse(cx - 100 + k * 50, top - 25, 22, 16, fill=STONE)
    for k in range(3):
        y = top + 140 + k * 40
        c.arrow(cx - 60 + k * 60, y + 40, cx - 60 + k * 60, y - 10, GREEN, 4, 12)
    c.text(cx + 220, top + 160, '浮力', 'bold', 26, GREEN, 'lm')
    c.arrow(cx, top - 60, cx, top - 10, NRED, 4, 12)
    c.text(cx + 30, top - 70, '重力', 'bold', 26, NRED, 'lm')
    a = fade(t, 11, 12)
    if a > 0:
        c.rect(1060, 320, 1840, 720, fill=mix(BG, SHEET, a), r=14)
        c.text(1450, 380, '阿基米德原理', 'bold', 32, mix(BG, SPARK, a), 'mm')
        c.text(1450, 460, '浮着的船：重量 = 排开的水的重量', 'sans', 26, mix(BG, INK, a), 'mm')
        c.text(1450, 530, '同一条船压到同一条水线', 'sans', 26, mix(BG, INK, a), 'mm')
        c.text(1450, 590, '排开的水一样多 → 船上的东西一样重', 'sans', 26, mix(BG, INK, a), 'mm')
        c.text(1450, 670, '（曹冲的故事比阿基米德晚四百多年，各自想到）', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '往船上加东西，船就往下沉，把更多的水挤开，水面也跟着涨'),
                (6.2, 12, '被挤开的水想回来，就从下往上托着船：挤开得越多，托得越重'),
                (12.2, 22, '所以压到同一条水线，船上的东西就一样重：这就是曹冲称象靠的道理')], y=1010)

# ---------------------------------------------------------------- B75 水准
def b75_tube(c, t, i):
    corner_tag(c, 'B75 · 一管水两头一样高')
    c.text(60, 96, '软管两头怎么举，静下来的水面都在同一高度', 'serif', 40, INK)
    hL = 120 * math.sin(t * 0.6)
    hR = -120 * math.sin(t * 0.6 + 1)
    xL, xR, base = 400, 1500, 880
    level = 520 + 0 * t
    yL_top = 380 + hL
    yR_top = 380 + hR
    for x, ytop in ((xL, yL_top), (xR, yR_top)):
        c.rect(x - 22, ytop, x + 22, base, outline=INK, width=3)
        c.rect(x - 19, level, x + 19, base - 3, fill=mix(BG, WATER, 0.8))
    c.line([(xL, base), (xL, base + 40), (xR, base + 40), (xR, base)], INK, 3)
    c.line([(xL + 20, base + 20), (xR - 20, base + 20)], mix(BG, WATER, 0.8), 30)
    seg(c, [(200, level), (1720, level)], mix(BG, SPARK, 0.9), 3)
    c.text(960, level - 30, '水面永远一样高', 'bold', 28, SPARK, 'mm')
    c.text(xL, yL_top - 30, '举高', 'sans', 22, MUTED, 'mm')
    c.text(xR, yR_top - 30, '放低', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一根透明软管灌满水，两头竖起来'),
                (7.2, 14, '一头举高、一头放低：管子动了，可两边的水面一停下来，又回到同一个高度'),
                (14.2, 22, '这叫连通器。在墙这头和那头各画一个水面记号，连起来就是一条真正水平的线')], y=1010)

def b75_level(c, t, i):
    corner_tag(c, 'B75 · 水平和照板')
    c.text(60, 96, '水槽里的浮子顶面一样高：顺着看过去，读远处标杆上的刻度', 'serif', 40, INK)
    gy = 820
    pts = [(80, gy - 40), (500, gy - 40), (900, gy + 20), (1300, gy - 10), (1840, gy + 50)]
    c.line(pts, mix(BG, (140, 120, 90), 1), 6)
    tx, ty = 300, gy - 250
    c.rect(tx - 160, ty, tx + 160, ty + 40, fill=WOOD)
    c.rect(tx - 150, ty + 4, tx + 150, ty + 30, fill=mix(BG, WATER, 0.7))
    for dx in (-130, 0, 130):
        c.rect(tx + dx - 14, ty - 30, tx + dx + 14, ty + 8, fill=(230, 220, 190))
    c.line([(tx, ty + 40), (tx, gy - 40)], WOOD, 10)
    sight_y = ty - 30
    for k, (sx, gy2) in enumerate(((1000, gy + 15), (1500, gy - 5))):
        a = fade(t, 4 + k * 6, 5 + k * 6)
        if a <= 0: continue
        c.rect(sx - 18, gy2 - 420, sx + 18, gy2, fill=mix(BG, (235, 230, 215), a))
        for m in range(0, 420, 30):
            c.line([(sx - 18, gy2 - m), (sx - 4, gy2 - m)], mix(BG, INK, a), 2)
        seg(c, [(tx + 150, sight_y), (sx, sight_y)], mix(BG, SPARK, a), 2)
        c.ellipse(sx, sight_y, 8, 8, fill=mix(BG, NRED, a))
        reading = (gy2 - sight_y) / 30 * 10
        c.text(sx + 40, sight_y, f'读数 {reading:.0f} 厘米（示意）', 'mono', 22, mix(BG, INK, a), 'lm')
    b = fade(t, 16, 17)
    if b > 0:
        c.text(1250, 300, '两个读数一减，就是两处地面差多高', 'bold', 28, mix(BG, GREEN, b), 'mm')
    caps(c, t, [(0, 6, '《营造法式》里的「水平」：一条长木槽盛水，水里浮着几个小木块，木块顶面就一样高'),
                (6.2, 14, '眼睛贴着浮子顶面看过去，对准远处立着的「照板」，读出这一点在板上的刻度'),
                (14.2, 22, '换个地方再立板、再读：两个读数一减，就知道哪边高、高多少')], y=1010)


CLIPS = {
 'B73_斜推': (b73_shear, 22), 'B73_三向': (b73_weave, 22),
 'B73_片头': (titles.opening(BSER, VOL20, SB20, 3, '新石器编织遗存 · 竹编工艺'), 7),
 'B73_片尾': (titles.closing(BSER, VOL20, SB20, 3, '下集：没有那么大的秤，怎么知道一头大象多重？'), 7),
 'B74_水线': (b74_boat, 22), 'B74_浮力': (b74_archimedes, 22),
 'B74_片头': (titles.opening(BSER, VOL20, SB20, 4, '《三国志》曹冲称象'), 7),
 'B74_片尾': (titles.closing(BSER, VOL20, SB20, 4, '下集：古人盖房子，怎么知道地面平不平？'), 7),
 'B75_连通器': (b75_tube, 22), 'B75_照板': (b75_level, 22),
 'B75_片头': (titles.opening(BSER, VOL20, SB20, 5, '《考工记》「水地以县」· 宋《营造法式》水平'), 7),
 'B75_片尾': (titles.closing(BSER, VOL20, SB20, 5, '下集：两块石头一转，豆子怎么就变成浆？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
