"""第三十二季（古法解密 13.0：天、凉、数、用）第三批：B136 剪刀、B137 瓦片、B138 纸风车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO
from s32a import SB32, VOL32, SUN, WARM, COOL

STEEL = (190, 195, 205)
TILE = (120, 125, 135)
PAPER2 = (230, 120, 110)
WINDC = (150, 200, 240)


# ---------------------------------------------------------------- B136 剪刀
def b136_lever(c, t, i):
    corner_tag(c, 'B136 · 离支点越近，刀口上的力越大')
    c.text(60, 96, '剪刀是两根交叉的杠杆：手握在离支点 6 厘米处，纸板放得离支点越近，刀口压在纸上的力就越大', 'serif', 38, INK)
    px, py = 960, 520
    open_a = 0.18 + 0.06 * math.sin(t * 1.5)
    for s in (1, -1):
        a = s * open_a
        bx, by = px + 600 * math.cos(a), py - 600 * math.sin(a)
        hx, hy = px - 300 * math.cos(a), py + 300 * math.sin(a)
        c.line([(px, py), (bx, by)], STEEL, 14)
        c.line([(px, py), (hx, hy)], mix(STEEL, INK, 0.2), 14)
        c.ellipse(hx - 20 * math.cos(a), hy + 20 * math.sin(a), 50, 36, outline=(200, 80, 70), width=10)
    c.ellipse(px, py, 14, 14, fill=INK)
    c.text(px, py + 50, '支点', 'sans', 20, MUTED, 'mm')
    k = min(2, int(t / 7.4))
    dists = [(10, '刀尖'), (5, '中间'), (2, '根部')]
    for j, (d, lab) in enumerate(dists):
        x = px + d * 55
        on = j == k
        c.rect(x - 8, py - 60, x + 8, py + 60, fill=mix(BG, WOOD, 0.9 if on else 0.3))
        c.text(x, py + 100, lab, 'bold' if on else 'sans', 22, INK if on else MUTED, 'mm')
    d = dists[k][0]
    F = 20 * 6 / d
    c.rect(1300, 260, 1860, 440, fill=SHEET, r=14)
    c.text(1580, 300, f'手上用 20 牛，纸在离支点 {d} 厘米处', 'sans', 20, INK, 'mm')
    c.text(1580, 370, f'刀口上约 {F:.0f} 牛', 'mono', 36, SPARK, 'mm')
    c.text(1580, 420, '（手柄 6 厘米，示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '剪刀的两片刀用一个铆钉交叉起来，铆钉就是支点'),
                (7.2, 14, '手离支点 6 厘米：纸放在 10 厘米的刀尖，力反而变小了'),
                (14.2, 22, '把纸塞到离支点 2 厘米的根部，手上同样的力，刀口上放大到 3 倍（示意）')], y=1010)


def b136_layers(c, t, i):
    corner_tag(c, 'B136 · 刀尖、中间、根部，各能剪断几层？')
    c.text(60, 96, '同一把儿童圆头剪刀，把 1、2、3 层叠起来的硬纸板条分别放在刀尖、中间、根部去剪', 'serif', 38, INK)
    data = [('刀尖', 1), ('中间', 2), ('根部', 3)]
    grow = min(1, t / 10)
    for k, (lab, n) in enumerate(data):
        x = 460 + k * 500
        for j in range(3):
            y = 760 - j * 70
            ok = j < n and grow > (j + 1) / 3.5
            c.rect(x - 150, y - 25, x + 150, y + 25, fill=mix(BG, WOOD, 0.7), r=4)
            if ok:
                c.line([(x, y - 30), (x, y + 30)], BG, 8)
            elif grow > (j + 1) / 3.5:
                c.text(x + 190, y, '剪不动', 'sans', 18, NRED, 'lm')
        c.text(x, 840, lab, 'bold', 28, INK, 'mm')
        c.text(x, 890, f'剪断 {min(n, int(grow * 3.5))} 层', 'mono', 24, SPARK, 'mm')
    c.text(960, 940, '层数为示意，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '刀尖处：一层还能勉强剪，两层就卡住了'),
                (7.2, 14, '挪到中间：两层能剪断'),
                (14.2, 22, '塞到根部：三层一起剪断。裁缝剪厚布、园丁剪树枝，都往剪刀根部塞（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B137 瓦片
def _roof(c, x0, y0, ang, overlap, n, t, show_rain=True):
    L, W = 160, 110
    dx, dy = L * math.cos(ang), L * math.sin(ang)
    step = 1 - overlap
    pts_leak = []
    for k in range(n):
        sx = x0 + k * dx * step
        sy = y0 + k * dy * step
        c.poly([(sx, sy - 6), (sx + dx, sy + dy - 6), (sx + dx, sy + dy + 6), (sx, sy + 6)], TILE)
        if k > 0:
            pts_leak.append((sx, sy))
    return dx, dy, step


def b137_overlap(c, t, i):
    corner_tag(c, 'B137 · 上面一片，压住下面一片的缝')
    c.text(60, 96, '瓦片一片压一片，从屋脊排到屋檐：雨水落在上面那片，顺着坡流到下面那片的背上，永远碰不到接缝', 'serif', 38, INK)
    ang = math.radians(28)
    x0, y0 = 300, 300
    L = 300
    step = 2 / 3
    for k in (3, 2, 1, 0):
        sx = x0 + k * L * math.cos(ang) * step
        sy = y0 + k * L * math.sin(ang) * step
        ex, ey = sx + L * math.cos(ang), sy + L * math.sin(ang)
        off = k * 18
        c.poly([(sx, sy - 14 + off), (ex, ey - 14 + off), (ex, ey + 14 + off), (sx, sy + 14 + off)], mix(TILE, (200, 200, 210), 0.25 * (k % 2)))
    for j in range(8):
        u = ((t * 0.12) + j / 8) % 1
        d = u * (L * step * 3 + L)
        x = x0 + d * math.cos(ang)
        y = y0 + d * math.sin(ang) - 22 + 18 * min(3, int(d / (L * step)))
        c.ellipse(x, y, 7, 9, fill=WATER)
    for j in range(5):
        rx = 400 + j * 120
        ry = 200 + ((t * 200 + j * 60) % 120)
        c.line([(rx, ry), (rx - 8, ry + 30)], mix(BG, WATER, 0.6), 2)
    c.rect(1300, 300, 1840, 600, fill=SHEET, r=14)
    c.text(1570, 350, '压住 1/3', 'bold', 28, INK, 'mm')
    c.text(1570, 430, '接缝藏在上一片底下', 'sans', 22, MUTED, 'mm')
    c.text(1570, 500, '水只在瓦背上流', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '瓦片之间没有胶，只是一片一片搭着'),
                (7.2, 14, '排的时候从下往上：每一片的下半截压在下一片的上半截上面'),
                (14.2, 22, '雨水只能从一片的背上流到下一片的背上，一路流到屋檐落下去：缝都藏在下面（示意）')], y=1010)


def b137_slope(c, t, i):
    corner_tag(c, 'B137 · 坡太平、压太少，水就倒灌')
    c.text(60, 96, '同样的卡纸瓦：坡度大、压得多，纸巾一滴不湿；坡度太小或者只压一点点，风一吹、水一积，就从缝里渗下去', 'serif', 36, INK)
    cases = [('30° · 压 1/3', 30, 1 / 3, 0), ('10° · 压 1/3', 10, 1 / 3, 2), ('30° · 压 1/10', 30, 0.1, 3), ('10° · 压 1/10', 10, 0.1, 8)]
    for k, (lab, deg, ov, wet) in enumerate(cases):
        x0 = 140 + (k % 2) * 880
        y0 = 260 + (k // 2) * 360
        ang = math.radians(deg)
        L = 150
        step = 1 - ov
        for j in (2, 1, 0):
            sx = x0 + j * L * math.cos(ang) * step
            sy = y0 + j * L * math.sin(ang) * step + j * 10
            c.poly([(sx, sy - 8), (sx + L * math.cos(ang), sy + L * math.sin(ang) - 8), (sx + L * math.cos(ang), sy + L * math.sin(ang) + 8), (sx, sy + 8)], mix(TILE, (200, 200, 210), 0.3 * (j % 2)))
        by = y0 + 250
        c.rect(x0, by, x0 + 640, by + 30, fill=(235, 235, 235), r=4)
        n = int(wet * min(1, t / 14))
        for j in range(n):
            c.ellipse(x0 + 60 + j * 70, by + 15, 16, 10, fill=mix((235, 235, 235), WATER, 0.6))
        c.text(x0 + 700, y0 + 60, lab, 'bold', 22, INK, 'lm')
        c.text(x0 + 700, y0 + 110, f'纸巾湿了 {n} 处', 'mono', 20, GREEN if n == 0 else NRED, 'lm')
    c.text(960, 960, '湿点数为示意，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同样的卡纸瓦，换两种坡度、两种压法，从上面喷水'),
                (7.2, 14, '坡度 30°、压住 1/3：水还没来得及往缝里钻，就顺坡流走了'),
                (14.2, 22, '坡太平、压太少，水在缝边积住、被毛细作用吸进去：所以屋顶要有坡，瓦要压够（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B138 纸风车
def b138_deflect(c, t, i):
    corner_tag(c, 'B138 · 风被叶片拐向一边，叶片被反推着走')
    c.text(60, 96, '从侧面看一片斜着的叶片：迎面来的风撞上去，被拐向一边流走；风往一边去，叶片就被推向另一边——转起来了', 'serif', 36, INK)
    cx, cy = 900, 560
    ang = math.radians(40)
    off = (t * 60) % 400 - 200
    bx = cx + off * 0.0
    L = 260
    p0 = (cx - L / 2 * math.cos(ang), cy + L / 2 * math.sin(ang))
    p1 = (cx + L / 2 * math.cos(ang), cy - L / 2 * math.sin(ang))
    c.line([p0, p1], PAPER2, 16)
    for j in range(7):
        y = 360 + j * 60
        u = ((t * 0.5) + j * 0.13) % 1
        if u < 0.5:
            x = 200 + u / 0.5 * (cx - 200 - 60)
            yy = y
        else:
            v = (u - 0.5) / 0.5
            x = cx - 60 + v * 300
            yy = y - v * 260
        c.ellipse(x, yy, 7, 7, fill=WINDC)
        c.arrow(200, y, 330, y, mix(BG, WINDC, 0.5), 2, 10)
    c.arrow(cx + 40, cy - 40, cx + 220, cy - 280, WINDC, 4, 16)
    c.text(cx + 260, cy - 300, '风被拐向上方', 'bold', 22, WINDC, 'lm')
    c.arrow(cx, cy + 40, cx, cy + 260, SPARK, 6, 20)
    c.text(cx + 30, cy + 240, '叶片被推向下方 → 绕轴转', 'bold', 24, SPARK, 'lm')
    c.text(240, 330, '迎面的风', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '叶片如果正对着风，风只会把它往后推，转不起来'),
                (7.2, 14, '叶片斜着放：风撞上去，被拐到侧面流走'),
                (14.2, 22, '风往一边去，叶片就被反推到另一边：四片叶子都这样，风车就绕着钉子转起来（示意）')], y=1010)


def b138_angle(c, t, i):
    corner_tag(c, 'B138 · 叶片太平太斜都转不快')
    c.text(60, 96, '叶片几乎正对风：只被往后推；叶片几乎顺着风：风滑过去推不动；中间某个斜度转得最快', 'serif', 38, INK)
    x0, y0, x1, y1 = 260, 280, 1300, 860
    c.line([(x0, y1), (x1, y1)], LINE, 2)
    c.line([(x0, y0), (x0, y1)], LINE, 2)
    for a in range(0, 91, 15):
        c.text(x0 + (x1 - x0) * a / 90, y1 + 30, f'{a}°', 'mono', 18, MUTED, 'mm')
    c.text((x0 + x1) / 2, y1 + 70, '叶片和风向的夹角（0° 顺着风，90° 正对风）', 'sans', 20, MUTED, 'mm')
    c.text(x0, y0 - 30, '转速（示意）', 'sans', 20, MUTED, 'lm')
    n = int(min(90, t / 14 * 90))
    pts = []
    for a in range(0, n + 1):
        r = math.sin(math.radians(2 * a)) ** 1.2 if 0 < a < 90 else 0
        pts.append((x0 + (x1 - x0) * a / 90, y1 - (y1 - y0) * r))
    if len(pts) > 1:
        c.line(pts, SPARK, 5)
    cx, cy = 1600, 560
    rot = t * 6
    for k in range(4):
        a = rot + k * math.pi / 2
        p = [(cx, cy), (cx + 180 * math.cos(a), cy + 180 * math.sin(a)), (cx + 120 * math.cos(a + 0.6), cy + 120 * math.sin(a + 0.6))]
        c.poly(p, mix(PAPER2, (230, 200, 90), k / 3))
    c.ellipse(cx, cy, 10, 10, fill=INK)
    c.ellipse(cx + 150 * math.cos(rot), cy + 150 * math.sin(rot), 10, 10, fill=NRED)
    c.text(cx, cy + 240, '红点：慢动作里数圈数', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '做三个叶片斜度不同的风车，用同一档电扇吹，慢动作数红点转了几圈'),
                (7.2, 14, '叶片太平、太陡，都转得慢'),
                (14.2, 22, '理想情况下大约 45° 左右最快，实际纸风车还和叶片形状、风速有关（曲线为示意，以实测为准）')], y=1010)


CLIPS = {
 'B136_杠杆': (b136_lever, 22), 'B136_层数': (b136_layers, 22),
 'B136_片头': (titles.opening(BSER, VOL32, SB32, 6, '汉代已有交股剪'), 7),
 'B136_片尾': (titles.closing(BSER, VOL32, SB32, 6, '下集：瓦片只是搭着，下大雨为什么不漏？'), 7),
 'B137_搭接': (b137_overlap, 22), 'B137_坡度': (b137_slope, 22),
 'B137_片头': (titles.opening(BSER, VOL32, SB32, 7, '西周已有板瓦筒瓦'), 7),
 'B137_片尾': (titles.closing(BSER, VOL32, SB32, 7, '下集：纸风车的叶片，为什么要斜着？'), 7),
 'B138_偏转': (b138_deflect, 22), 'B138_角度': (b138_angle, 22),
 'B138_片头': (titles.opening(BSER, VOL32, SB32, 8, '宋代已有风车玩具'), 7),
 'B138_片尾': (titles.closing(BSER, VOL32, SB32, 8, '下集：拴几个空葫芦过河，为什么就不会沉？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
