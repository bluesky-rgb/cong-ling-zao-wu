"""第二十四季（古法解密 9.0）第三批：B96 沙漏、B97 浑仪、B98 剪纸 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import rot
from s24a import SB24, VOL24, WOOD, DARKWOOD, STONE, WATER, WATER_L

SANDC = (220, 190, 120)
GLASS = (170, 190, 210)
BRASS = (200, 165, 80)
EARTH = (70, 130, 200)
STARC = (250, 240, 200)
RED = (210, 50, 50)


# ---------------------------------------------------------------- B96 沙漏
def _vessel(c, x, top, bot, w, level, col):
    c.rect(x - w, top, x + w, bot, outline=GLASS, width=4, r=10)
    y = bot - (bot - top) * level
    if y < bot - 6:
        c.rect(x - w + 4, y, x + w - 4, bot - 4, fill=col)
    c.ellipse(x, bot + 10, 8, 8, fill=GLASS)


def b96_rate(c, t, i):
    corner_tag(c, 'B96 · 沙流得一样快，水越流越慢')
    c.text(60, 96, '水漏：水越少，压力越小，流得越慢；沙漏：沙多沙少，孔口流速几乎一样', 'serif', 40, INK)
    T = 20.0
    u = min(1.0, t / T)
    hw = (1 - u) ** 2
    hs = 1 - u
    _vessel(c, 300, 260, 720, 90, hw, WATER)
    _vessel(c, 640, 260, 720, 90, hs, SANDC)
    if hw > 0.01:
        c.line([(300, 740), (300, 820)], WATER_L, max(1, int(8 * math.sqrt(hw))))
    if hs > 0.01:
        c.line([(640, 740), (640, 820)], SANDC, 6)
    c.text(300, 860, '水', 'bold', 28, INK, 'mm')
    c.text(640, 860, '干沙', 'bold', 28, INK, 'mm')
    gx0, gy0, gx1, gy1 = 960, 780, 1820, 300
    c.rect(920, 240, 1860, 860, fill=SHEET, r=14)
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text((gx0 + gx1) / 2, gy0 + 40, '时间 →', 'sans', 22, MUTED, 'mm')
    c.text(gx0 + 10, gy1 - 20, '剩下多少', 'sans', 22, MUTED, 'lm')
    pw, ps = [], []
    for j in range(101):
        uu = j / 100
        if uu > u:
            break
        x = gx0 + (gx1 - gx0) * uu
        pw.append((x, gy0 - (gy0 - gy1) * (1 - uu) ** 2))
        ps.append((x, gy0 - (gy0 - gy1) * (1 - uu)))
    if len(pw) > 1:
        c.line(pw, WATER, 4)
        c.line(ps, SANDC, 4)
    c.text(gx1 - 10, gy1 + 20, '黄：沙（直线 = 匀速）', 'sans', 22, SANDC, 'rm')
    c.text(gx1 - 10, gy1 + 60, '蓝：水（越来越平 = 越来越慢）', 'sans', 22, WATER, 'rm')
    caps(c, t, [(0, 7, '两个一样的容器，底下开一样的小孔，一个装水、一个装干沙'),
                (7.2, 14, '水满的时候压得重，喷得快；水越少压力越小，流得越来越慢'),
                (14.2, 22, '沙却几乎一直匀速往下流：画出来，沙是一条直线，水是一条越来越平的弯线（示意）')], y=1010)


def b96_arch(c, t, i):
    corner_tag(c, 'B96 · 沙粒互相顶着')
    c.text(60, 96, '沙粒一颗顶一颗，把上面的重量斜着传给瓶壁；孔口附近的沙，只觉得「底下一小拱」压着', 'serif', 40, INK)
    cx, top, bot, W = 700, 260, 880, 300
    c.poly([(cx - W, top), (cx + W, top), (cx + W, bot - 200), (cx + 30, bot), (cx - 30, bot), (cx - W, bot - 200)], mix(BG, SANDC, 0.35))
    c.line([(cx - W, top), (cx - W, bot - 200), (cx - 30, bot)], GLASS, 5)
    c.line([(cx + W, top), (cx + W, bot - 200), (cx + 30, bot)], GLASS, 5)
    r = 18
    rnd = random.Random(4)
    for row in range(16):
        y = top + 30 + row * 2 * r * 0.88
        if y > bot - 10:
            break
        half = W - (max(0, y - (bot - 200)) / 200) * (W - 30)
        n = int((2 * half - 20) / (2 * r))
        for k in range(n):
            x = cx - half + 14 + r + k * 2 * r + (r if row % 2 else 0)
            if x > cx + half - r:
                continue
            c.ellipse(x, y, r - 2, r - 2, fill=SANDC)
    for k in range(3):
        y0 = top + 80 + k * 110
        a = fade(t, 2 + k * 1.5, 4 + k * 1.5)
        if a <= 0:
            continue
        c.arrow(cx, y0, cx - W + 30, y0 + 150, mix(BG, NRED, a), 4, 14)
        c.arrow(cx, y0, cx + W - 30, y0 + 150, mix(BG, NRED, a), 4, 14)
    s = (t * 2) % 1
    for k in range(4):
        c.ellipse(cx + (k - 1.5) * 10, bot + 20 + 120 * ((s + k * 0.25) % 1), 6, 6, fill=SANDC)
    c.rect(1180, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1520, 340, '为什么不随高度变', 'bold', 26, INK, 'mm')
    c.text(1220, 420, '上面的重量，大多被斜着', 'sans', 24, INK, 'lm')
    c.text(1220, 470, '传到了瓶壁上', 'sans', 24, INK, 'lm')
    c.text(1220, 550, '孔口只受到附近一小拱沙的压力', 'sans', 24, INK, 'lm')
    c.text(1220, 630, '所以满瓶和半瓶，流得差不多快', 'bold', 24, GREEN, 'lm')
    caps(c, t, [(0, 7, '水是一整块往下压：越深压得越重，孔口喷得越快'),
                (7.2, 14, '沙是一颗颗的：每一颗都顶着旁边的几颗，把上面的重量斜着传到瓶壁上'),
                (14.2, 22, '孔口那里只受到一小片沙的压力，和上面堆多高关系不大：粮仓底部也是这样（示意）')], y=1010)


# ---------------------------------------------------------------- B97 浑仪
def b97_polaris(c, t, i):
    corner_tag(c, 'B97 · 北极星有多高，你就在北纬多少度')
    c.text(60, 96, '北极星几乎正对着地轴；站在北纬 φ 度的地方，看它离地平线也是 φ 度', 'serif', 40, INK)
    cx, cy, R = 600, 660, 240
    c.ellipse(cx, cy, R, R, fill=EARTH)
    c.line([(cx, cy + R + 40), (cx, cy - R - 160)], MUTED, 3)
    c.ellipse(cx, cy - R - 180, 12, 12, fill=STARC)
    c.text(cx - 24, cy - R - 180, '北极星（很远很远）', 'sans', 22, STARC, 'rm')
    c.line([(cx - R - 40, cy), (cx + R + 40, cy)], mix(BG, MUTED, 0.6), 2)
    c.text(cx + R + 50, cy, '赤道', 'sans', 20, MUTED, 'lm')
    phi = math.radians(20 + 40 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi)))
    ox, oy = cx + R * math.cos(phi), cy - R * math.sin(phi)
    c.line([(cx, cy), (ox, oy)], mix(BG, INK, 0.5), 2)
    c.arc(cx, cy, 70, 70, -math.degrees(phi), 0, SPARK, 3)
    c.text(cx + 90, cy - 30, 'φ', 'bold', 30, SPARK, 'mm')
    tx, ty = -math.sin(phi), -math.cos(phi)
    c.line([(ox - 220 * tx, oy - 220 * ty), (ox + 220 * tx, oy + 220 * ty)], GREEN, 4)
    c.text(ox + 220 * tx - 10, oy + 220 * ty - 20, '地平线', 'sans', 22, GREEN, 'rm')
    c.line([(ox, oy), (ox, oy - 190)], STARC, 3)
    ha = math.degrees(math.atan2(-math.cos(phi), -math.sin(phi)))
    c.arc(ox, oy, 90, 90, ha, -90, SPARK, 3)
    c.text(ox - 60, oy - 110, 'φ', 'bold', 28, SPARK, 'mm')
    c.ellipse(ox, oy, 10, 10, fill=RED)
    c.rect(1240, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1550, 340, '北极星的高度角', 'bold', 26, INK, 'mm')
    c.text(1550, 430, f'= {math.degrees(phi):.0f}°', 'mono', 48, SPARK, 'mm')
    c.text(1550, 520, f'这个人站在北纬 {math.degrees(phi):.0f}°', 'sans', 26, INK, 'mm')
    c.text(1550, 590, '（北京约 40°，广州约 23°，拍摄前核对）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '北极星离我们极远，它的光射到地球各处都是平行的，方向和地轴几乎一样'),
                (7.2, 14, '站在赤道上，北极星贴着地平线；站在北极，它就在头顶正上方'),
                (14.2, 22, '在中间任何地方，北极星离地平线的角度，正好等于你所在的纬度')], y=1010)


def b97_rings(c, t, i):
    corner_tag(c, 'B97 · 几个环套在一起量星星')
    c.text(60, 96, '地平环、子午环、赤道环套在一起，中间一根窥管能转；对准星星，读刻度', 'serif', 40, INK)
    cx, cy, R = 760, 560, 300
    c.ellipse(cx, cy, R, R * 0.28, outline=BRASS, width=8)
    c.text(cx + R + 20, cy, '地平环', 'sans', 22, BRASS, 'lm')
    c.ellipse(cx, cy, R * 0.25, R, outline=BRASS, width=8)
    c.text(cx, cy - R - 30, '子午环', 'sans', 22, BRASS, 'mm')
    tilt = math.radians(50)
    pts = []
    for j in range(73):
        a = j * 2 * math.pi / 72
        x = R * 0.92 * math.cos(a)
        y = R * 0.92 * 0.32 * math.sin(a)
        rx, ry = x * math.cos(tilt) - y * math.sin(tilt), x * math.sin(tilt) + y * math.cos(tilt)
        pts.append((cx + rx, cy + ry))
    c.line(pts, mix(BRASS, SPARK, 0.5), 6)
    c.text(cx - R - 20, cy + 240, '赤道环（和赤道平行）', 'sans', 22, mix(BRASS, SPARK, 0.5), 'rm')
    for k in range(5):
        a = t * 0.15 + k * 1.25
        sx = 1500 + 260 * math.cos(a)
        sy = 360 + 160 * math.sin(a)
        c.ellipse(sx, sy, 7, 7, fill=STARC)
    c.ellipse(1500, 360, 9, 9, fill=SPARK)
    c.text(1500, 560, '星星绕着北天极转（示意）', 'sans', 22, MUTED, 'mm')
    a = t * 0.15 + 1.25
    tx, ty = 1500 + 260 * math.cos(a), 360 + 160 * math.sin(a)
    ang = math.atan2(ty - cy, tx - cx)
    c.line([(cx - 200 * math.cos(ang), cy - 200 * math.sin(ang)), (cx + 200 * math.cos(ang), cy + 200 * math.sin(ang))], (230, 230, 240), 10)
    c.line([(cx + 200 * math.cos(ang), cy + 200 * math.sin(ang)), (tx, ty)], mix(BG, STARC, 0.35), 2)
    c.text(cx, cy + R + 60, '窥管跟着一颗星转', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '浑仪是几个刻着度数的铜环套在一起：一个代表地平，一个代表南北，一个和赤道平行'),
                (7.2, 14, '中间一根空心的窥管能上下左右转动，人从管里对准一颗星'),
                (14.2, 22, '读出环上的刻度，就知道这颗星在天上的位置。元代郭守敬把它拆简，做成了简仪（拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- B98 剪纸
def _cut_pattern(c, cx, cy, S, folds, a):
    c.rect(cx - S, cy - S, cx + S, cy + S, fill=RED)
    pts = [(0.5, 0.2), (0.75, 0.35), (0.5, 0.5)]
    mirrors = [lambda p: p]
    if folds >= 1:
        mirrors = [lambda p: p, lambda p: (-p[0], p[1])]
    if folds >= 2:
        mirrors = mirrors + [lambda p, m=m: (m(p)[0], -m(p)[1]) for m in list(mirrors)]
    if folds >= 3:
        mirrors = mirrors + [lambda p, m=m: (m(p)[1], m(p)[0]) for m in list(mirrors)]
    for m in mirrors:
        q = [m(p) for p in pts]
        c.poly([(cx + S * x * a, cy + S * y * a) for x, y in q], BG)
    if folds >= 1:
        c.line([(cx, cy - S), (cx, cy + S)], mix(RED, INK, 0.3), 1)
    if folds >= 2:
        c.line([(cx - S, cy), (cx + S, cy)], mix(RED, INK, 0.3), 1)
    if folds >= 3:
        c.line([(cx - S, cy - S), (cx + S, cy + S)], mix(RED, INK, 0.3), 1)


def b98_folds(c, t, i):
    corner_tag(c, 'B98 · 折一次，多一条对称轴')
    c.text(60, 96, '同一刀，纸折的层数越多，展开后的缺口越多：折痕就是对称轴', 'serif', 40, INK)
    names = [('不折', 0, 1), ('对折 1 次', 1, 2), ('再对折 1 次', 2, 4), ('再斜折 1 次', 3, 8)]
    for k, (nm, f, n) in enumerate(names):
        cx = 280 + k * 450
        a = fade(t, 2 + k * 4, 4 + k * 4)
        _cut_pattern(c, cx, 560, 170, f, 1.0 if a > 0 else 0.0)
        c.text(cx, 330, nm, 'bold', 28, INK, 'mm')
        if a > 0:
            c.text(cx, 790, f'一刀 → {n} 个口', 'mono', 26, SPARK, 'mm')
            c.text(cx, 840, f'对称轴 {f if f < 3 else 4} 条', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一张红纸不折，剪一个三角缺口，展开就是一个口'),
                (7.2, 14, '对折一次再剪：一刀剪穿两层，展开是两个左右对称的口；再折一次，变成四个'),
                (14.2, 22, '再沿斜线折一次，一刀就是八个口：每一道折痕，都成了一条对称轴')], y=1010)


def b98_rosette(c, t, i):
    corner_tag(c, 'B98 · 一小块花样，转出一朵团花')
    c.text(60, 96, '团花是把一小块花样，绕着中心翻过来、转过去，复制成一整圈', 'serif', 40, INK)
    cx, cy, R = 760, 560, 330
    n = 8
    shown = min(2 * n, int(t / 1.1) + 1)
    c.ellipse(cx, cy, R, R, fill=RED)
    rnd = random.Random(3)
    motif = [(0.25, 0.04, 0.42, 0.12, 0.32, 0.18), (0.55, 0.05, 0.75, 0.1, 0.62, 0.2), (0.82, 0.03, 0.95, 0.15, 0.85, 0.22)]
    for k in range(shown):
        base = (k // 2) * 2 * math.pi / n
        flip = 1 if k % 2 == 0 else -1
        for (r1, a1, r2, a2, r3, a3) in motif:
            pts = []
            for rr, aa in ((r1, a1), (r2, a2), (r3, a3)):
                ang = base + flip * aa * (2 * math.pi / n) / 0.25 * 0.5
                pts.append((cx + R * rr * math.cos(ang), cy + R * rr * math.sin(ang)))
            c.poly(pts, BG)
    c.ellipse(cx, cy, 40, 40, fill=BG)
    for k in range(n):
        a = k * 2 * math.pi / n
        c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], mix(RED, INK, 0.25), 1)
    c.rect(1280, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1570, 340, '八折团花', 'bold', 26, INK, 'mm')
    c.text(1570, 420, f'已经复制 {shown} / {2 * n} 块', 'mono', 26, SPARK, 'mm')
    c.text(1570, 500, '翻一次：镜面对称', 'sans', 24, INK, 'mm')
    c.text(1570, 550, '转一圈：旋转对称', 'sans', 24, INK, 'mm')
    caps(c, t, [(0, 7, '把纸折成八层的扇形，只需要在这一小块上剪花样'),
                (7.2, 14, '展开时，这一小块先被「翻」一次，再绕着中心「转」出一圈'),
                (14.2, 22, '一共十六块一模一样的花样，拼成一朵团花。一千多年前新疆出土的剪纸，就是这样剪的（拍摄前核对）')], y=1010)


CLIPS = {
 'B96_流速': (b96_rate, 22), 'B96_互相顶': (b96_arch, 22),
 'B96_片头': (titles.opening(BSER, VOL24, SB24, 6, '元代五轮沙漏 · 欧洲 14 世纪沙漏'), 7),
 'B96_片尾': (titles.closing(BSER, VOL24, SB24, 6, '下集：古人怎么量出星星在天上的位置？'), 7),
 'B97_北极星': (b97_polaris, 22), 'B97_环': (b97_rings, 22),
 'B97_片头': (titles.opening(BSER, VOL24, SB24, 7, '西汉落下闳浑仪 · 元代郭守敬简仪'), 7),
 'B97_片尾': (titles.closing(BSER, VOL24, SB24, 7, '下集：一张红纸折几下剪几刀，为什么那么对称？'), 7),
 'B98_对称轴': (b98_folds, 22), 'B98_团花': (b98_rosette, 22),
 'B98_片头': (titles.opening(BSER, VOL24, SB24, 8, '吐鲁番出土南北朝团花剪纸'), 7),
 'B98_片尾': (titles.closing(BSER, VOL24, SB24, 8, '下集：几根带缺口的木条，为什么不用钉子也卡得死？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
