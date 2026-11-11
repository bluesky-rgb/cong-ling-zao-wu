"""第三十九季（第十六层：运动场）第一批：E202 跑鞋缓震、E203 自行车变速、E204 头盔 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L

S39A = [('202', '跑鞋缓震'), ('203', '自行车变速'), ('204', '头盔'), ('205', '弧线球'), ('206', '撑竿跳'),
        ('207', '动力绳'), ('208', '泳衣'), ('209', '电子计时'), ('210', '鹰眼'), ('211', '蹦床')]
SER39, VOL39 = '从零造物', '第三十九季 · 第十六层：运动场'
FOAM = (235, 225, 170)
RUBBER = (70, 70, 80)
SKIN = (220, 170, 130)
SHELL = (230, 90, 70)
CHAIN = (150, 155, 165)


def _curve(c, x0, y0, W, H, f, tmax, col, t_now, fmax, width=5):
    pts = []
    for k in range(121):
        s = k / 120 * tmax
        if s > t_now:
            break
        pts.append((x0 + s / tmax * W, y0 + H - f(s) / fmax * H))
    if len(pts) > 1:
        c.line(pts, col, width)


# ---------------------------------------------------------------- E202 跑鞋缓震
def e202_landing(c, t, i):
    corner_tag(c, '第 202 集 · 落地时间拉长，冲击力变小')
    c.text(60, 96, '同样一次落地：硬地上一眨眼就停住，力又尖又高；软鞋底让停下来的过程变长，力就矮而宽', 'serif', 36, INK)
    x0, y0, W, H = 200, 260, 1100, 560
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 45, '时间（毫秒，示意）', 'sans', 22, MUTED, 'mm')
    c.text(x0 - 20, y0 + 20, '力', 'sans', 24, MUTED, 'rm')
    tn = min(1.0, t / 12) * 60
    hard = lambda s: 9 * math.exp(-((s - 8) / 3) ** 2)
    soft = lambda s: 3.2 * math.exp(-((s - 20) / 9) ** 2)
    _curve(c, x0 + 20, y0 + 20, W - 40, H - 40, hard, 60, NRED, tn, 10)
    _curve(c, x0 + 20, y0 + 20, W - 40, H - 40, soft, 60, GREEN, tn, 10)
    c.text(x0 + 260, y0 + 60, '硬地：又尖又高', 'bold', 24, NRED, 'lm')
    c.text(x0 + 560, y0 + H - 200, '软鞋底：矮而宽', 'bold', 24, GREEN, 'lm')
    a = fade(t, 13, 14)
    c.rect(1400, 300, 1860, 620, fill=SHEET, r=12)
    c.text(1630, 350, '两条曲线下的面积', 'bold', 24, INK, 'mm')
    c.text(1630, 400, '一样大（同一次停下）', 'sans', 22, MUTED, 'mm')
    c.text(1630, 480, '力 × 时间 = 冲量', 'mono', 28, mix(BG, SPARK, a), 'mm')
    c.text(1630, 550, '时间长了，最大的力就小了', 'sans', 22, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 7, '脚落地，要在很短的时间里从往下动变成停住'),
                (7.2, 14, '在硬地上一下就停，力又尖又高；泡沫鞋底被压扁，停下来的过程变长'),
                (14.2, 22, '要停下的「量」一样，时间拉长了，最大的力就小：这叫缓冲（示意）')], y=1010)


def e202_rebound(c, t, i):
    corner_tag(c, 'E202 · 太软也不行')
    c.text(60, 96, '同一颗弹力球落在三种地面上：硬桌面弹得最高；软鞋底压下去一点再弹回；厚海绵把能量吃掉，几乎不弹', 'serif', 34, INK)
    for j, (lab, e, sq, col) in enumerate([('桌面', 0.85, 6, (120, 100, 80)), ('拖鞋底', 0.65, 22, RUBBER), ('厚海绵', 0.2, 60, FOAM)]):
        cx = 380 + j * 580
        base = 740
        c.rect(cx - 200, base, cx + 200, base + 70, fill=mix(BG, col, 0.9), r=8)
        T = 2.2
        tt = t % (T * 3)
        h0 = 420
        h = h0
        tb = tt
        k = 0
        while k < 3:
            dur = 2 * math.sqrt(h / h0) * 0.6
            if tb < dur:
                break
            tb -= dur
            h *= e
            k += 1
        dur = 2 * math.sqrt(max(h, 1) / h0) * 0.6
        if k == 0:
            f = min(1, tb / (dur / 2))
            y = base - 40 - h0 * (1 - f * f) if tb < dur / 2 else base - 40
        else:
            u = tb / dur
            y = base - 40 - h * 4 * u * (1 - u)
        squash = sq if abs(y - (base - 40)) < 8 else 0
        c.ellipse(cx, y + squash * 0.5, 40 + squash * 0.4, 40 - squash * 0.5, fill=SPARK)
        c.text(cx, base + 120, lab, 'bold', 26, INK, 'mm')
        c.text(cx, base + 165, f'弹回约 {e * 100:.0f}% 高度（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '鞋底软，能缓冲；可太软了，落地的能量被压进去就回不来'),
                (7.2, 14, '跑步时每一步都要蹬出去，鞋底最好能把一部分能量弹回来'),
                (14.2, 22, '好跑鞋的泡沫，既要软得能缓冲，又要弹得回来（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E203 自行车变速
def _gear(c, cx, cy, r, ang, col, teeth=None):
    n = teeth or max(10, int(r / 6))
    pts = []
    for k in range(n * 2):
        a = ang + k * math.pi / n
        rr = r + (8 if k % 2 == 0 else -2)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    c.poly(pts, col)
    c.ellipse(cx, cy, r * 0.35, r * 0.35, fill=BG)
    c.line([(cx, cy), (cx + r * 0.8 * math.cos(ang), cy + r * 0.8 * math.sin(ang))], INK, 4)


def e203_ratio(c, t, i):
    corner_tag(c, '第 203 集 · 脚踏一圈，后轮转几圈')
    c.text(60, 96, '前面的大齿盘 44 齿：后面挂 11 齿，脚踏一圈后轮转 4 圈；挂 33 齿，只转 4/3 圈', 'serif', 36, INK)
    for j, (rt, lab) in enumerate([(11, '挂小齿轮：快，但费劲'), (33, '挂大齿轮：慢，但省力')]):
        y = 360 + j * 360
        fx, rx = 420, 1150
        a = t * 1.2
        _gear(c, fx, y, 132, a, mix(BG, CHAIN, 0.9), 22)
        rr = rt * 4.5
        _gear(c, rx, y, rr, a * 44 / rt, mix(BG, SPARK, 0.8), max(8, rt // 2))
        c.line([(fx, y - 140), (rx, y - rr - 8)], CHAIN, 4)
        c.line([(fx, y + 140), (rx, y + rr + 8)], CHAIN, 4)
        c.text(1500, y - 30, lab, 'bold', 26, INK, 'lm')
        turns = 44 / rt * min(1, t / 14)
        c.text(1500, y + 30, f'脚踏 {min(1, t / 14):.2f} 圈 → 后轮 {turns:.2f} 圈', 'mono', 24, SPARK, 'lm')
    caps(c, t, [(0, 7, '链条把前面的大齿盘和后面的小齿轮连在一起，链条走过的齿数一样多'),
                (7.2, 14, '后面齿轮越小，前面转一圈，它就得转越多圈'),
                (14.2, 22, '齿数比 = 前齿数 ÷ 后齿数：数一数你家自行车的齿（示意）')], y=1010)


def e203_climb(c, t, i):
    corner_tag(c, 'E203 · 省力就费距离')
    c.text(60, 96, '上坡要的力大：挂大齿轮，脚上的力小了，可要多蹬好几圈；力和快，不能兼得', 'serif', 36, INK)
    gx, gy = 200, 860
    c.poly([(gx, gy), (1300, gy), (1300, gy - 420)], mix(BG, (120, 140, 100), 0.6))
    p = (t % 11) / 11
    x = gx + 200 + p * 800
    y = gy - (x - gx) / (1100) * 420
    ang = math.atan2(-420, 1100)
    for dx in (-60, 60):
        wx = x + dx * math.cos(ang)
        wy = y + dx * math.sin(ang) - 40
        c.ellipse(wx, wy, 38, 38, fill=None if False else mix(BG, RUBBER, 0.9))
        c.ellipse(wx, wy, 26, 26, fill=BG)
    c.line([(x - 60 * math.cos(ang), y - 60 * math.sin(ang) - 40), (x, y - 100), (x + 60 * math.cos(ang), y + 60 * math.sin(ang) - 40)], SHELL, 6)
    c.ellipse(x - 5, y - 150, 18, 18, fill=SKIN)
    c.rect(1400, 260, 1860, 700, fill=SHEET, r=12)
    c.text(1630, 310, '爬同一段坡', 'bold', 26, INK, 'mm')
    for k, (lab, f, n) in enumerate([('重档（44 / 11）', 4.0, 1.0), ('轻档（44 / 33）', 1.33, 3.0)]):
        y0 = 380 + k * 150
        c.text(1430, y0, lab, 'sans', 22, INK, 'lm')
        c.rect(1430, y0 + 30, 1430 + f * 90, y0 + 60, fill=NRED if k == 0 else GREEN, r=6)
        c.text(1440 + f * 90, y0 + 45, '脚上的力', 'sans', 18, MUTED, 'lm')
        c.text(1430, y0 + 90, f'要蹬 {n:.0f} 份圈数', 'mono', 20, SPARK, 'lm')
    caps(c, t, [(0, 7, '同一段坡，把车推上去要做的功是一样多的'),
                (7.2, 14, '挂轻档，脚上每一下用的力小了，可是得多蹬几圈'),
                (14.2, 22, '这和杠杆一样：省力就费距离。变速只是让你自己挑（示意）')], y=1010)


# ---------------------------------------------------------------- E204 头盔
def e204_shell(c, t, i):
    corner_tag(c, '第 204 集 · 硬壳把力摊开')
    c.text(60, 96, '同样的撞击：打在一个尖点上，压强又大又集中；硬壳把它摊到一大片上，每一处受的力就小了', 'serif', 36, INK)
    for j, (lab, spread) in enumerate([('没有硬壳：力集中在一点', 30), ('有硬壳：力摊在一大片', 300)]):
        cx, cy = 520 + j * 880, 640
        c.ellipse(cx, cy, 260, 220, fill=mix(BG, SKIN, 0.8))
        if j == 1:
            c.arc(cx, cy, 300, 262, 180, 360, SHELL, 26)
        a = min(1, t / 6)
        ry = cy - 520 + 230 * a
        c.poly([(cx - 30, ry - 80), (cx + 30, ry - 80), (cx, ry)], mix(BG, RUBBER, 1.0))
        if a >= 1:
            n = 9
            for k in range(n):
                f = (k - (n - 1) / 2) / ((n - 1) / 2)
                ang = -math.pi / 2 + f * spread / 300 * 1.2
                L = 90 if j == 1 else 160 * (1 - abs(f))
                sx, sy = cx + 230 * math.cos(ang), cy + 200 * math.sin(ang)
                c.arrow(sx, sy, sx - L * 0.6 * math.cos(ang), sy - L * 0.6 * math.sin(ang), NRED, 4, 12)
        c.text(cx, 930, lab, 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '摔倒时，头可能撞到路沿、石头这样的尖角'),
                (7.2, 14, '没有头盔，力全集中在一小块地方，压强很大'),
                (14.2, 22, '硬壳把力摊到一大片，每一处受的力就小了：压强 = 力 ÷ 面积（示意）')], y=1010)


def e204_foam(c, t, i):
    corner_tag(c, 'E204 · 泡沫把时间拉长')
    c.text(60, 96, '硬壳里面那层泡沫被压扁的几毫秒里，头是慢慢停下来的；压扁过一次，它就不能再用了', 'serif', 36, INK)
    cx, cy = 760, 560
    p = min(1.0, max(0, (t - 3) / 8))
    th = 90 * (1 - 0.7 * p)
    c.rect(cx - 400, cy + 240, cx + 400, cy + 300, fill=mix(BG, (110, 110, 115), 0.9))
    c.rect(cx - 300, cy + 240 - 30, cx + 300, cy + 240, fill=SHELL)
    c.rect(cx - 280, cy + 210 - th, cx + 280, cy + 210, fill=mix(BG, FOAM, 0.9))
    r = random.Random(2)
    for k in range(60):
        x = cx - 270 + r.uniform(0, 540)
        y = cy + 210 - r.uniform(5, th - 5)
        c.ellipse(x, y, 6 * (1 - 0.6 * p), 4 * (1 - 0.6 * p), fill=mix(BG, (200, 190, 140), 0.9))
    c.ellipse(cx, cy + 210 - th - 150, 200, 150, fill=mix(BG, SKIN, 0.8))
    c.text(cx + 340, cy + 210 - th / 2, f'泡沫厚 {th / 3:.0f} 毫米', 'mono', 24, SPARK, 'lm')
    c.rect(1380, 280, 1860, 520, fill=SHEET, r=12)
    c.text(1620, 330, '头停下来用的时间', 'bold', 24, INK, 'mm')
    c.text(1620, 400, '没泡沫：约 1 毫秒', 'sans', 22, NRED, 'mm')
    c.text(1620, 450, '有泡沫：约 5–10 毫秒（示意）', 'sans', 22, GREEN, 'mm')
    c.text(1620, 600, '摔过一次的头盔要换新的', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '头盔里面这层泡沫，里面全是小气泡'),
                (7.2, 14, '撞上去时，气泡一个个被压扁，头是在几毫米里慢慢停下来的'),
                (14.2, 22, '压扁了就弹不回去：摔过一次的头盔，看着没坏也要换（示意）')], y=1010)


CLIPS = {
 'E202_落地': (e202_landing, 22), 'E202_弹回': (e202_rebound, 22),
 'E202_片头': (titles.opening(SER39, VOL39, S39A, 0, '20 世纪 70 年代起跑鞋开始用泡沫中底'), 7),
 'E202_片尾': (titles.closing(SER39, VOL39, S39A, 0, '下集：自行车换挡，换的到底是什么？'), 7),
 'E203_齿轮比': (e203_ratio, 22), 'E203_爬坡': (e203_climb, 22),
 'E203_片头': (titles.opening(SER39, VOL39, S39A, 1, '19 世纪末出现自行车变速器'), 7),
 'E203_片尾': (titles.closing(SER39, VOL39, S39A, 1, '下集：头盔的硬壳和泡沫，各自在保护什么？'), 7),
 'E204_硬壳': (e204_shell, 22), 'E204_泡沫': (e204_foam, 22),
 'E204_片头': (titles.opening(SER39, VOL39, S39A, 2, '20 世纪起骑车开始戴硬壳头盔'), 7),
 'E204_片尾': (titles.closing(SER39, VOL39, S39A, 2, '下集：任意球为什么会在空中拐弯？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
