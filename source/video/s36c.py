"""第三十六季（古法解密 15.0）第三批：B156 捶丸、B157 顶碗、B158 点茶 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s36a import SB36, VOL36, STONE

GRASS = (110, 150, 95)
BALL = (240, 235, 220)
TEA = (150, 190, 110)
FOAM = (235, 240, 225)
BOWL = (210, 205, 195)


# ---------------------------------------------------------------- B156 捶丸
def b156_rolling(c, t, i):
    corner_tag(c, 'B156 · 摩擦让球一路变慢')
    c.text(60, 96, '球推出去以后，地面的摩擦一直在拖它：同样的推力，在硬地上滚得远，在草地（毛巾）上很快停下', 'serif', 36, INK)
    for j, (lab, mu, col) in enumerate([('硬地（地板）', 0.03, mix(BG, WOOD, 0.6)), ('草地（毛巾）', 0.12, mix(BG, GRASS, 0.8))]):
        y = 400 + j * 300
        c.rect(120, y, 1800, y + 80, fill=col, r=8)
        v0 = 2.0
        a = mu * 9.8
        tt = min(t / 3.0, v0 / a)
        d = v0 * tt - 0.5 * a * tt * tt
        dmax = v0 * v0 / (2 * a)
        x = 200 + d * 230
        c.ellipse(x, y - 24, 24, 24, fill=BALL)
        c.ellipse(1600, y + 40, 50, 16, fill=BG, outline=SPARK, width=3)
        c.text(1600, y + 110, '窝', 'sans', 22, SPARK, 'mm')
        c.text(140, y - 50, lab, 'bold', 26, INK, 'lm')
        if tt >= v0 / a - 1e-3:
            c.text(x, y - 80, f'停在 {dmax * 50:.0f} 厘米（示意）', 'mono', 22, SPARK, 'mm')
    c.arrow(160, 330, 260, 330, SPARK, 4, 12)
    c.text(210, 300, '同样的推力', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '球一离开球杖，就再也没人推它了，只剩摩擦在往后拖'),
                (7.2, 14, '硬地上摩擦小，球滚得远；草地软，摩擦大，球很快就停'),
                (14.2, 22, '所以捶丸高手打之前先摸摸地面：同一个距离，草地要多用几分劲（示意）')], y=1010)


def b156_break(c, t, i):
    corner_tag(c, 'B156 · 坡让球拐弯，要往坡上瞄')
    c.text(60, 96, '地面有一点侧坡：直直对着窝打，球被坡带偏滚走；往坡上方瞄偏一点，球拐着弯滚进窝', 'serif', 36, INK)
    x0, y0, x1, y1 = 160, 260, 1760, 900
    c.rect(x0, y0, x1, y1, fill=mix(BG, GRASS, 0.55), r=12)
    for k in range(6):
        y = y0 + 60 + k * 100
        c.arrow(x0 + 40, y, x0 + 40, y + 50, mix(BG, INK, 0.4), 3, 10)
    c.text(x0 + 70, y0 + 30, '坡往下 ↓', 'sans', 22, MUTED, 'lm')
    hx, hy = 1560, 580
    c.ellipse(hx, hy, 34, 34, fill=BG, outline=SPARK, width=3)
    sx, sy = 300, 580
    for j, (aim, col, lab) in enumerate([(0, NRED, '直直对准'), (-0.184, GREEN, '往坡上瞄')]):
        pts = []
        x, y = sx, sy
        vx, vy = 3.0 * math.cos(aim), 3.0 * math.sin(aim)
        for k in range(3000):
            sp = math.hypot(vx, vy)
            if sp < 0.02: break
            vx -= 0.004 * vx / sp
            vy -= 0.004 * vy / sp
            vy += 0.004
            x += vx * 2; y += vy * 2
            if y > y1 - 16 or x > x1 - 16: break
            pts.append((x, y))
            if math.hypot(x - hx, y - hy) < 6 and j == 1: break
        n = int(len(pts) * min(1.0, t / 12))
        if n > 1:
            seg(c, pts[:n], mix(BG, col, 0.9), 3)
            c.ellipse(pts[n - 1][0], pts[n - 1][1], 14, 14, fill=BALL)
        c.text(sx, sy + 60 + j * 40, lab, 'bold', 22, col, 'mm')
    c.ellipse(sx, sy, 14, 14, fill=BALL)
    caps(c, t, [(0, 7, '地面看着平，其实有一点点侧坡，球一边滚一边被坡往低处带'),
                (7.2, 14, '直直对着窝打，球被带偏，从窝的下方滚过去'),
                (14.2, 22, '往坡上方瞄偏一点，让坡把球「送」回来，拐着弯进窝（示意）')], y=1010)


# ---------------------------------------------------------------- B157 顶碗
def b157_balance(c, t, i):
    corner_tag(c, 'B157 · 重心对准支点才稳')
    c.text(60, 96, '一摞碗的重心只要在头顶正上方，就不倒；一歪出去，人就挪一步，把支点重新送到重心底下', 'serif', 36, INK)
    th = 0.18 * math.sin(t * 1.3)
    hx = 760 + 160 * math.sin(t * 1.3 - 0.5)
    base_y = 900
    c.ellipse(hx, base_y - 260, 60, 70, fill=mix(BG, (225, 190, 160), 0.8))
    c.rect(hx - 70, base_y - 190, hx + 70, base_y, fill=mix(BG, (150, 90, 80), 0.8), r=20)
    py = base_y - 330
    L = 300
    cmx = hx + L * 0.6 * math.sin(th)
    cmy = py - L * 0.6 * math.cos(th)
    for k in range(6):
        f = (k + 0.5) / 6
        bx = hx + L * f * math.sin(th)
        by = py - L * f * math.cos(th)
        c.poly([(bx - 70, by - 20), (bx + 70, by - 20), (bx + 45, by + 30), (bx - 45, by + 30)], mix(BG, BOWL, 0.9))
    c.ellipse(cmx, cmy, 14, 14, fill=SPARK)
    c.line([(cmx, cmy), (cmx, py)], SPARK, 2)
    c.text(cmx + 24, cmy, '重心', 'bold', 22, SPARK, 'lm')
    c.ellipse(hx, py, 8, 8, fill=NRED)
    off = cmx - hx
    if abs(off) > 20:
        c.arrow(hx, base_y + 20, hx + (60 if off > 0 else -60), base_y + 20, GREEN, 4, 12)
        c.text(hx + 160, base_y + 20, '挪过去接住', 'bold', 22, GREEN, 'mm')
    c.rect(1320, 320, 1860, 700, fill=SHEET, r=14)
    c.text(1590, 370, '重心在支点正上方：稳', 'bold', 24, GREEN, 'mm')
    c.text(1590, 430, '重心歪出去：开始倒', 'bold', 24, NRED, 'mm')
    c.text(1590, 510, '人往歪的方向挪一步', 'sans', 22, MUTED, 'mm')
    c.text(1590, 555, '支点又回到重心底下', 'sans', 22, MUTED, 'mm')
    c.text(1590, 650, '只用塑料碗', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '一摞碗可以看成一个整体，它的重心在中间偏上的地方'),
                (7.2, 14, '重心一歪出头顶，就开始往那边倒'),
                (14.2, 22, '演员不是让碗不动，而是一直跟着挪，把头顶送到重心底下（示意）')], y=1010)


def b157_tall(c, t, i):
    corner_tag(c, 'B157 · 高的东西倒得慢，来得及接')
    c.text(60, 96, '同样歪一点点：短铅笔一眨眼就倒了，1 米长的尺子慢慢倒，手有足够的时间跟上', 'serif', 36, INK)
    for j, (L, lab, sc) in enumerate([(0.15, '15 厘米铅笔', 1.0), (1.0, '1 米木尺', 0.55)]):
        cx = 420 + j * 760
        by = 860
        g = 9.8
        w = math.sqrt(1.5 * g / L)
        th0 = 0.05
        tt = (t % 7)
        th = min(math.pi / 2, th0 * math.cosh(w * tt))
        Lp = L * 600 * sc / (1.0 if j else 0.15) * (0.15 if not j else 1.0)
        Lp = 90 if j == 0 else 520
        c.line([(cx, by), (cx + Lp * math.sin(th), by - Lp * math.cos(th))], WOOD if j else (240, 200, 90), 14 if j else 10)
        c.ellipse(cx, by + 10, 30, 14, fill=mix(BG, (225, 190, 160), 0.8))
        tf = math.acosh(math.pi / 2 / th0) / w
        c.text(cx, 920, lab, 'bold', 26, INK, 'mm')
        c.text(cx, 960, f'从微歪到倒下约 {tf:.2f} 秒（示意）', 'mono', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '立在手指上的东西都会倒，区别是倒得多快'),
                (7.2, 14, '越高的东西，倒下去要走的路越长，开头那一下歪得越慢'),
                (14.2, 22, '手有时间察觉、跟上去：所以一摞碗高一点，反而比一只碗好顶（示意）')], y=1010)


# ---------------------------------------------------------------- B158 点茶
def _bubbles(c, cx, top, w, h, size, n, seed, alpha=1.0):
    r = random.Random(seed)
    for k in range(n):
        x = cx + r.uniform(-w / 2, w / 2)
        y = top + r.uniform(0, h)
        s = size * r.uniform(0.6, 1.4)
        c.ellipse(x, y, s, s, fill=mix(BG, FOAM, 0.85 * alpha), outline=mix(BG, (200, 210, 190), alpha), width=1)


def b158_foam(c, t, i):
    corner_tag(c, 'B158 · 细小均匀的泡久久不破')
    c.text(60, 96, '茶里有像肥皂一样的成分，能在空气和水之间撑起薄膜；泡越小越匀，薄膜越不容易破', 'serif', 36, INK)
    for j, (lab, size, n, decay) in enumerate([('大泡（乱搅）', 30, 30, 0.25), ('细泡（击拂）', 7, 600, 0.02)]):
        cx = 520 + j * 880
        c.poly([(cx - 300, 420), (cx + 300, 420), (cx + 200, 820), (cx - 200, 820)], mix(BG, BOWL, 0.9))
        c.poly([(cx - 270, 520), (cx + 270, 520), (cx + 195, 800), (cx - 195, 800)], mix(BG, TEA, 0.85))
        h = 110 * math.exp(-decay * t)
        _bubbles(c, cx, 520 - h, 520, h, size, int(n * h / 110) + 1, j)
        c.text(cx, 870, lab, 'bold', 28, INK, 'mm')
        c.text(cx, 910, f'泡沫约 {h / 22:.1f} 厘米', 'mono', 22, SPARK, 'mm')
    c.rect(780, 220, 1140, 320, fill=SHEET, r=12)
    c.text(960, 270, f'过了 {t / 2.2:.0f} 分钟（示意）', 'mono', 24, INK, 'mm')
    caps(c, t, [(0, 7, '茶粉里有一些成分喜欢待在水和空气的交界，能把空气包成小泡'),
                (7.2, 14, '大泡的膜又薄又大，里面的水很快流走，一下就破了'),
                (14.2, 22, '又细又匀的小泡互相撑着，水流得慢，能在碗里停好几分钟（示意）')], y=1010)


def b158_whisk(c, t, i):
    corner_tag(c, 'B158 · 竹筅打出的泡最细最稳')
    c.text(60, 96, '竹筅有几十根细竹丝，一下就把空气切成许多小泡；筷子和勺子只能搅出几个大泡', 'serif', 36, INK)
    vals = [('竹茶筅', 2.2, 0.03), ('筷子', 1.0, 0.12), ('勺子', 0.5, 0.2)]
    p = min(1.0, t / 6)
    for k, (lab, h0, dec) in enumerate(vals):
        x = 360 + k * 580
        c.poly([(x - 200, 380), (x + 200, 380), (x + 130, 640), (x - 130, 640)], mix(BG, BOWL, 0.9))
        c.poly([(x - 180, 440), (x + 180, 440), (x + 128, 625), (x - 128, 625)], mix(BG, TEA, 0.85))
        hh = h0 * p * math.exp(-dec * max(0, t - 6))
        _bubbles(c, x, 440 - hh * 30, 340, hh * 30, [6, 16, 26][k], int(220 * hh / 2.2) + 2, k + 5)
        bh = hh * 100
        c.rect(x - 50, 900 - bh, x + 50, 900, fill=mix(BG, FOAM, 0.8), r=6)
        c.text(x, 880 - bh, f'{hh:.1f} 厘米', 'mono', 22, SPARK, 'mm')
        c.text(x, 940, lab, 'bold', 26, INK, 'mm')
    c.text(1680, 300, '水温不超过 50 ℃', 'bold', 22, NRED, 'mm')
    c.text(1680, 340, '实验的茶不喝', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '同样的茶粉、同样的温水，三种工具各快速搅打 1 分钟'),
                (7.2, 14, '竹筅打出厚厚一层细沫，筷子和勺子只有薄薄一层大泡'),
                (14.2, 22, '放着不动，大泡几分钟就破光了，细沫还留着大半（示意，以实测为准）')], y=1010)


CLIPS = {
 'B156_滚动': (b156_rolling, 22), 'B156_借坡': (b156_break, 22),
 'B156_片头': (titles.opening(BSER, VOL36, SB36, 6, '元代已有记载捶丸的《丸经》'), 7),
 'B156_片尾': (titles.closing(BSER, VOL36, SB36, 6, '下集：杂技演员头上的一摞碗，为什么不掉？'), 7),
 'B157_重心': (b157_balance, 22), 'B157_高的': (b157_tall, 22),
 'B157_片头': (titles.opening(BSER, VOL36, SB36, 7, '汉代百戏里已有顶碗叠案'), 7),
 'B157_片尾': (titles.closing(BSER, VOL36, SB36, 7, '下集：宋人点茶的白沫，为什么久久不散？'), 7),
 'B158_泡沫': (b158_foam, 22), 'B158_工具': (b158_whisk, 22),
 'B158_片头': (titles.opening(BSER, VOL36, SB36, 8, '宋代流行点茶、斗茶'), 7),
 'B158_片尾': (titles.closing(BSER, VOL36, SB36, 8, '下集：一团松散的羊毛，怎么搓成了毡子？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
