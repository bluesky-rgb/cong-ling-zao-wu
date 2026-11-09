"""第三十六季（古法解密 15.0：力、声、玩、软）第一批：B150 楔子、B151 绳结、B152 溜索 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB36 = [('B150', '楔子'), ('B151', '绳结'), ('B152', '溜索'), ('B153', '车辐'), ('B154', '木鱼'),
        ('B155', '打水漂'), ('B156', '捶丸'), ('B157', '顶碗'), ('B158', '点茶'), ('B159', '毛毡')]
VOL36 = '第三十六季 · 古法解密 15.0'
STONE = (150, 145, 135)
ROPE = (215, 190, 140)
BEAN = (225, 200, 120)
CABLE = (180, 185, 195)


# ---------------------------------------------------------------- B150 楔子
def _wedge(c, cx, tipy, L, ang, col=WOOD):
    hw = L * math.tan(math.radians(ang / 2))
    c.poly([(cx - hw, tipy - L), (cx + hw, tipy - L), (cx, tipy)], mix(BG, col, 0.95))
    return hw


def b150_wedge(c, t, i):
    corner_tag(c, 'B150 · 细长的斜面把力放大')
    c.text(60, 96, '往下敲一下，斜面把这股力变成往两边推的力：楔子越细长，往两边推的力就越大', 'serif', 36, INK)
    for j, (ang, lab) in enumerate([(10, '细长的楔子（约 10°）'), (30, '短粗的楔子（约 30°）')]):
        cx = 520 + j * 880
        d = min(60, t * 6)
        gap = 2 * d * math.tan(math.radians(ang / 2))
        c.rect(cx - 360, 520, cx - gap / 2, 880, fill=mix(BG, STONE, 0.9), r=6)
        c.rect(cx + gap / 2, 520, cx + 360, 880, fill=mix(BG, STONE, 0.9), r=6)
        tip = 520 + d
        L = 300
        _wedge(c, cx, tip, L, ang)
        c.arrow(cx, tip - L - 120, cx, tip - L - 20, SPARK, 6, 18)
        c.text(cx + 30, tip - L - 90, '敲', 'bold', 26, SPARK, 'lm')
        F = 1 / (2 * math.tan(math.radians(ang / 2)))
        c.arrow(cx - 60, 640, cx - 60 - 40 * min(F, 6), 640, NRED, 5, 16)
        c.arrow(cx + 60, 640, cx + 60 + 40 * min(F, 6), 640, NRED, 5, 16)
        c.text(cx, 920, lab, 'bold', 26, INK, 'mm')
        c.text(cx, 960, f'往两边推的力约是敲击的 {F:.1f} 倍（不计摩擦，示意）', 'mono', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '楔子是一个两面都斜的斜面，敲的力是往下的'),
                (7.2, 14, '楔子每往下走一点，两边的石头只被推开一点点：走得远、推得少，力就被放大了'),
                (14.2, 22, '楔子越细长，放大得越多；可也要敲得更深，才能把缝撑开（示意）')], y=1010)


def b150_swell(c, t, i):
    corner_tag(c, 'B150 · 干木头吸了水，自己往外胀')
    c.text(60, 96, '古人把干木楔打进石缝，再一遍遍浇水：木头吸水膨胀，慢慢把石头撑裂；泡水的黄豆也有这股劲', 'serif', 36, INK)
    p = min(1.0, t / 16)
    cx = 520
    c.rect(160, 360, 880, 860, fill=mix(BG, STONE, 0.9), r=8)
    crack = 6 + 30 * p
    c.rect(cx - crack / 2, 360, cx + crack / 2, 700, fill=BG)
    hw = 22 + 14 * p
    c.rect(cx - hw / 2 - crack / 2 + 10, 330, cx + hw / 2 + crack / 2 - 10, 600, fill=mix(BG, mix(WOOD, WATER_L, 0.4 * p), 0.95), r=4)
    for k in range(5):
        y = 250 + ((t * 120 + k * 40) % 120)
        c.ellipse(cx + (k - 2) * 12, y, 4, 7, fill=WATER_L)
    if p > 0.5:
        r = random.Random(1)
        x, y = cx, 700
        pts = [(x, y)]
        for k in range(int(8 * (p - 0.5) * 2)):
            x += r.uniform(-20, 20); y += 20
            pts.append((x, y))
        c.line(pts, BG, 4)
    c.text(520, 900, '浇水 → 木楔胀开 → 石缝越来越宽', 'bold', 24, INK, 'mm')
    bx, by = 1400, 620
    c.rect(bx - 140, by - 220, bx + 140, by + 220, fill=mix(BG, (210, 220, 230), 0.35), outline=MUTED, width=4, r=30)
    c.rect(bx - 60, by - 250, bx + 60, by - 215, fill=MUTED, r=6)
    r = random.Random(5)
    for k in range(70):
        x = bx + r.uniform(-120, 120)
        y = by + r.uniform(-200, 200)
        rad = 12 * (1 + 0.6 * p)
        c.ellipse(x, y, rad, rad * 0.75, fill=mix(BG, BEAN, 0.9))
    if p > 0.8:
        c.text(bx, by - 290, '盖子被顶起来了！', 'bold', 26, NRED, 'mm')
    c.text(bx, 900, '塑料瓶里的黄豆泡一夜', 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '干木头里有无数细小的孔，一碰到水就把水吸进去'),
                (7.2, 14, '木头吸了水要变粗，可石缝不让它变粗，它就使劲往外顶'),
                (14.2, 22, '这股劲又慢又大，能把整块石头沿着一排楔子撑开：黄豆泡水也能把瓶盖顶起来（示意）')], y=1010)


# ---------------------------------------------------------------- B151 绳结
def b151_friction(c, t, i):
    corner_tag(c, 'B151 · 每多绕一圈，摩擦就成倍增加')
    c.text(60, 96, '绳子绕在柱子上：每多绕半圈，能拉住的力就翻一番。好结就是让绳子绕在自己身上，越拉压得越紧', 'serif', 34, INK)
    turns = min(3.0, 0.5 + t / 6)
    cx, cy = 760, 560
    c.ellipse(cx, cy, 90, 90, fill=mix(BG, WOOD, 0.9))
    c.text(cx, cy, '柱子', 'bold', 24, BG, 'mm')
    R = 100
    pts = []
    N = int(turns * 60)
    for k in range(N + 1):
        a = math.pi / 2 + 2 * math.pi * k / 60
        pts.append((cx + R * math.cos(a) + k * 0.4, cy + R * math.sin(a)))
    c.line(pts, ROPE, 10)
    c.line([(cx - 400, cy + R), pts[0]], ROPE, 10)
    c.line([pts[-1], (pts[-1][0] + (300 if math.cos(math.pi / 2 + 2 * math.pi * turns) < 0.5 else 300), pts[-1][1])], ROPE, 10)
    c.rect(cx - 470, cy + R - 10, cx - 400, cy + R + 120, fill=mix(BG, STONE, 0.9), r=6)
    c.text(cx - 435, cy + R + 160, '重物', 'sans', 22, MUTED, 'mm')
    mu = 0.3
    ratio = math.exp(mu * 2 * math.pi * turns)
    c.rect(1300, 300, 1860, 760, fill=SHEET, r=14)
    c.text(1580, 350, f'绕了 {turns:.1f} 圈', 'bold', 30, INK, 'mm')
    c.text(1580, 420, f'手上只要用 1 份力', 'sans', 24, MUTED, 'mm')
    c.text(1580, 480, f'就能拉住 {ratio:.0f} 份重', 'mono', 34, SPARK, 'mm')
    c.text(1580, 560, '（摩擦系数按 0.3 算，示意）', 'sans', 20, MUTED, 'mm')
    c.text(1580, 680, '缆桩、绞盘、绳结都靠它', 'bold', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '绳子在柱子上绕半圈，柱子就分走了一部分拉力'),
                (7.2, 14, '每多绕一点，摩擦就成倍增加：绕三圈，手上一点劲就能拉住很重的东西'),
                (14.2, 22, '绳结也是这样：让绳子自己压住自己，拉得越紧，压得越死（示意）')], y=1010)


def b151_knots(c, t, i):
    corner_tag(c, 'B151 · 三种结，哪个先松？')
    c.text(60, 96, '同一根棉绳打成平结、祖母结、称人结，吊一个小桶一杯杯加水：打错的祖母结最先滑开', 'serif', 36, INK)
    cups = min(10, int(t / 1.6))
    vals = [('平结', 7), ('祖母结', 3), ('称人结', 10)]
    for k, (lab, n) in enumerate(vals):
        x = 380 + k * 560
        top = 260
        ok = cups < n
        c.line([(x, top), (x, top + 140)], ROPE, 8)
        c.ellipse(x, top + 160, 34, 22, outline=ROPE, width=8)
        if ok:
            c.line([(x - 20, top + 180), (x - 60, top + 360), (x + 60, top + 360), (x + 20, top + 180)], ROPE, 6)
            by = top + 360
        else:
            c.line([(x - 20, top + 180), (x - 40, top + 240)], ROPE, 6)
            c.line([(x + 20, top + 180), (x + 40, top + 240)], ROPE, 6)
            by = 760
        c.poly([(x - 90, by), (x + 90, by), (x + 70, by + 160), (x - 70, by + 160)], mix(BG, (120, 170, 210), 0.6))
        fill = min(cups, n) / 10
        if fill > 0.02:
            c.rect(x - 68, by + 158 - 150 * fill, x + 68, by + 158, fill=mix(BG, WATER, 0.8))
        c.text(x, 960 - 20, lab, 'bold', 28, INK, 'mm')
        if not ok:
            c.text(x, 700, f'第 {n} 杯时松开', 'bold', 24, NRED, 'mm')
    c.text(960, 230, f'已加 {cups} 杯水（每杯 200 毫升，示意）', 'mono', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '三个结用的是同一根绳，只是打法不一样'),
                (7.2, 14, '祖母结两次绕的方向一样，绳子没压住自己，一受力就开始滑'),
                (14.2, 22, '平结和称人结让绳子互相压紧，越拉越紧，卸了力又好解（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B152 溜索
def _cable(x0, y0, x1, y1, sag, n=60):
    return [(x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n + sag * 4 * (k / n) * (1 - k / n)) for k in range(n + 1)]


def b152_slope(c, t, i):
    corner_tag(c, 'B152 · 一高一低，靠重力滑过去')
    c.text(60, 96, '溜索两头一高一低：挂在上面的人顺着斜坡滑下去，高差越大，滑得越快', 'serif', 36, INK)
    c.rect(0, 860, 1920, 960, fill=mix(BG, WATER, 0.6))
    c.text(960, 910, '江', 'bold', 30, BG, 'mm')
    c.poly([(0, 300), (260, 300), (300, 860), (0, 860)], mix(BG, STONE, 0.8))
    c.poly([(1660, 620), (1920, 620), (1920, 860), (1620, 860)], mix(BG, STONE, 0.8))
    pts = _cable(240, 320, 1680, 630, 60)
    c.line(pts, CABLE, 5)
    T = 9.0
    f = min(1.0, ((t % 11) / T) ** 1.6)
    k = int(f * (len(pts) - 1))
    x, y = pts[k]
    c.ellipse(x, y, 16, 16, fill=WOOD)
    c.line([(x, y), (x, y + 70)], MUTED, 3)
    c.rect(x - 24, y + 70, x + 24, y + 120, fill=mix(BG, (200, 120, 90), 0.9), r=6)
    c.text(x, y + 150, '玩具小人（示意）', 'sans', 20, MUTED, 'mm')
    c.line([(1720, 320), (1720, 630)], SPARK, 2)
    c.text(1740, 470, '高差', 'bold', 24, SPARK, 'lm')
    c.rect(600, 200, 1300, 280, fill=SHEET, r=12)
    c.text(950, 240, '高差 20 / 40 / 80 厘米：越高越快（以实测为准）', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '没有桥的深谷里，人们在两岸拉一根索，这头高、那头低'),
                (7.2, 14, '人挂在滑轮或溜板上，一松手，重力就把他顺着斜坡拉过去'),
                (14.2, 22, '高差越大越快；回来时要换另一根反方向倾斜的索（示意，人绝不挂上去试）')], y=1010)


def b152_sag(c, t, i):
    corner_tag(c, 'B152 · 绳子越松，中间越垂，滑到半路就停')
    c.text(60, 96, '同样一高一低：拉紧的绳子一路往下；放松的绳子中间垂下去，硬币袋滑到最低点就停住了', 'serif', 36, INK)
    for j, (sag, lab) in enumerate([(30, '拉紧'), (150, '放松 20 厘米')]):
        y0 = 320 + j * 340
        x0, x1 = 180, 1740
        pts = _cable(x0, y0, x1, y0 + 120, sag)
        c.line(pts, CABLE, 5)
        c.rect(x0 - 30, y0 - 10, x0, y0 + 260, fill=mix(BG, WOOD, 0.7))
        c.rect(x1, y0 + 110, x1 + 30, y0 + 260, fill=mix(BG, WOOD, 0.7))
        ys = [p[1] for p in pts]
        kmin = ys.index(max(ys))
        f = min(1.0, t / 10)
        if sag < 100:
            k = int(f * (len(pts) - 1))
        else:
            osc = math.exp(-max(0, t - 6) * 0.4) * math.cos(max(0, t - 6) * 2.2)
            k = int(min(f * kmin * 1.6, kmin + 8 * osc)) if t > 6 else int(f * kmin * 1.6)
            k = max(0, min(len(pts) - 1, k))
        x, y = pts[k]
        c.ellipse(x, y, 12, 12, fill=METAL_C)
        c.rect(x - 22, y + 20, x + 22, y + 60, fill=mix(BG, (230, 210, 120), 0.9), r=6)
        c.text(x0 + 60, y0 - 40, lab, 'bold', 26, INK, 'lm')
        if sag >= 100 and t > 12:
            c.text(x, y - 50, '停在最低点', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '绳子拉得紧，几乎是一条直的斜线，硬币袋一路滑到底'),
                (7.2, 14, '把绳子放松一点，它的中间就垂下来，比低的那头还要低'),
                (14.2, 22, '袋子滑到最低点就停住了：真溜索的最后一段，要靠手攀着拉过去（示意）')], y=1010)


METAL_C = (200, 200, 210)

CLIPS = {
 'B150_斜面': (b150_wedge, 22), 'B150_膨胀': (b150_swell, 22),
 'B150_片头': (titles.opening(BSER, VOL36, SB36, 0, '古人采石用木楔浸水胀裂岩石'), 7),
 'B150_片尾': (titles.closing(BSER, VOL36, SB36, 0, '下集：同一根绳，好结坏结差在哪里？'), 7),
 'B151_摩擦': (b151_friction, 22), 'B151_三种结': (b151_knots, 22),
 'B151_片头': (titles.opening(BSER, VOL36, SB36, 1, '新石器时代已有结网的绳结'), 7),
 'B151_片尾': (titles.closing(BSER, VOL36, SB36, 1, '下集：一根索斜着拉过江，人怎么就滑过去了？'), 7),
 'B152_斜坡': (b152_slope, 22), 'B152_下垂': (b152_sag, 22),
 'B152_片头': (titles.opening(BSER, VOL36, SB36, 2, '怒江一带曾靠溜索渡江'), 7),
 'B152_片尾': (titles.closing(BSER, VOL36, SB36, 2, '下集：车轮挖空了，为什么反而更结实？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
