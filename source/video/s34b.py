"""第三十四季（古法解密 14.0）第二批：B143 回旋镖、B144 边架艇、B145 草拌泥 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s34a import SB34, VOL34, WIND, CLAY

CARD = (225, 210, 170)
LIFT = (120, 200, 140)


def _blades(c, cx, cy, R, ang, n=3, col=CARD, w=26):
    for k in range(n):
        a = ang + k * 2 * math.pi / n
        c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], col, w)
    c.ellipse(cx, cy, w * 0.6, w * 0.6, fill=col)


# ---------------------------------------------------------------- B143 回旋镖
def b143_lift(c, t, i):
    corner_tag(c, 'B143 · 上面那片转得快，升力大')
    c.text(60, 96, '回旋镖竖着飞：上面的叶片顺着飞行方向转，迎风更快、升力更大；下面的叶片正好相反', 'serif', 36, INK)
    cx, cy = 560, 560
    c.rect(100, 230, 1020, 900, fill=SHEET, r=14)
    c.text(560, 270, '从侧面看（往右飞）', 'sans', 22, MUTED, 'mm')
    _blades(c, cx, cy, 200, -t * 5)
    c.arrow(cx - 60, cy, cx + 120, cy, MUTED, 4, 14)
    c.text(cx + 30, cy + 40, '飞行方向', 'sans', 20, MUTED, 'mm')
    c.arrow(cx - 120, cy - 230, cx + 220, cy - 230, SPARK, 6, 18)
    c.text(cx + 260, cy - 230, '快：飞行 + 转动', 'bold', 22, SPARK, 'lm')
    c.arrow(cx - 40, cy + 230, cx + 60, cy + 230, SPARK, 3, 12)
    c.text(cx + 100, cy + 230, '慢：飞行 − 转动', 'sans', 22, SPARK, 'lm')
    c.arc(cx, cy, 250, 250, 200, 250, MUTED, 3)
    c.text(cx - 260, cy - 170, '转', 'sans', 22, MUTED, 'mm')
    c.rect(1080, 230, 1860, 900, fill=SHEET, r=14)
    c.text(1470, 270, '从背后看：升力一边大一边小', 'sans', 22, MUTED, 'mm')
    bx, by = 1470, 560
    c.line([(bx, by - 220), (bx, by + 220)], CARD, 24)
    for k in range(5):
        y = by - 200 + k * 100
        L = 40 + 140 * (4 - k) / 4
        c.arrow(bx + 10, y, bx + 10 + L, y, LIFT, 4, 12)
    c.text(bx + 210, by - 210, '升力大', 'bold', 22, LIFT, 'lm')
    c.text(bx + 80, by + 210, '升力小', 'sans', 22, LIFT, 'lm')
    a = fade(t, 12, 13)
    if a > 0:
        c.arc(bx, by, 150, 150, 300, 420, mix(BG, NRED, a), 4)
        c.text(bx, by + 290, '上面推得多 → 整个回旋镖慢慢转向，飞的路线拐成圈', 'bold', 22, mix(BG, NRED, a), 'mm')
    caps(c, t, [(0, 7, '叶片的剖面像机翼，一边转一边往前飞，切开空气就有升力'),
                (7.2, 14, '上面那片：转的方向和飞的方向一致，速度叠加，升力大；下面那片正相反'),
                (14.2, 22, '升力上大下小，转着的回旋镖就像陀螺一样被慢慢扭转方向，绕一圈飞回来（示意）')], y=1010)


def _loop(s, kind):
    if kind == 0:
        R = 230
        a = math.pi * 2 * s
        return 960 + R * math.sin(a) * 1.3, 860 - R * (1 - math.cos(a)) * 0.95
    if kind == 1:
        return 960 + 40 * s, 860 - 520 * math.sin(math.pi * s * 0.5) * (1 - 0.0 * s)
    R = 260
    a = math.pi * 1.6 * s
    return 960 - R * math.sin(a) * 1.45, 860 - R * (1 - math.cos(a)) * 1.1


def b143_return(c, t, i):
    corner_tag(c, 'B143 · 哪一个飞得回来？')
    c.text(60, 96, '从上往下看三只卡纸回旋镖：三叶折边的绕一圈回来，不折的直直落在前面，两叶的圈太大', 'serif', 36, INK)
    c.rect(560, 180, 1360, 940, fill=mix(BG, SHEET, 0.7), r=14)
    c.ellipse(960, 860, 16, 16, fill=INK)
    c.text(1000, 890, '起点（你站的地方）', 'sans', 20, MUTED, 'lm')
    c.text(960, 210, '前面的空墙', 'sans', 20, MUTED, 'mm')
    cols = [SPARK, NRED, FIELD]
    names = ['三叶、叶边折', '三叶、不折', '两叶']
    ends = [1.0, 1.0, 1.0]
    p = min(1.0, t / 14)
    for k in range(3):
        pts = [_loop(s * p, k) for s in [j / 60 for j in range(61)]]
        seg(c, pts, mix(BG, cols[k], 0.8), 4)
        x, y = pts[-1]
        _blades(c, x, y, 26, t * 9, 3 if k < 2 else 2, cols[k], 8)
    for k in range(3):
        c.rect(1440, 300 + k * 120, 1860, 390 + k * 120, fill=SHEET, r=10)
        c.line([(1470, 345 + k * 120), (1530, 345 + k * 120)], cols[k], 6)
        c.text(1550, 345 + k * 120, names[k], 'bold', 24, INK, 'lm')
    if t > 14.5:
        c.text(1650, 720, '回到起点附近', 'sans', 22, SPARK, 'mm')
        c.text(1650, 760, '落在前面', 'sans', 22, NRED, 'mm')
        c.text(1650, 800, '绕得太大', 'sans', 22, FIELD, 'mm')
    c.text(260, 500, '对着空墙弹', 'bold', 26, INK, 'mm')
    c.text(260, 545, '不对着人和脸', 'bold', 26, NRED, 'mm')
    caps(c, t, [(0, 7, '同样竖着弹出去，三只卡纸回旋镖从上往下看，飞出三条不同的路线'),
                (7.2, 14, '叶边微微折起，像机翼一样有升力，才能绕圈；不折的几乎没有升力，直接落下'),
                (14.2, 22, '只有两叶的转得不稳、圈也更大：差别要自己弹一弹才知道（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B144 边架艇
def b144_moment(c, t, i):
    corner_tag(c, 'B144 · 浮杆离得远，扶正的力臂长')
    c.text(60, 96, '船往一边歪：浮杆被压进水里，浮力把它往上托；离船越远，这一托扶正船的劲就越大', 'serif', 36, INK)
    wl = 640
    c.rect(0, wl, 1920, 960, fill=mix(BG, WATER, 0.55))
    th = 0.16 * math.sin(t * 0.9)
    cx, cy = 700, wl - 10
    d = 600

    def rot(x, y):
        return cx + (x - cx) * math.cos(th) - (y - cy) * math.sin(th), cy + (x - cx) * math.sin(th) + (y - cy) * math.cos(th)
    hull = [rot(cx + 70 * math.cos(a), cy + 90 * math.sin(a)) for a in [k * math.pi / 20 for k in range(0, 21)]]
    hull += [rot(cx - 70, cy - 40), rot(cx + 70, cy - 40)]
    c.poly([rot(cx + 70 * math.cos(a), cy - 20 + 80 * math.sin(a)) for a in [k * math.pi / 20 for k in range(0, 21)]] + [rot(cx - 70, cy - 60), rot(cx + 70, cy - 60)], mix(BG, WOOD, 0.9))
    b0 = rot(cx + 40, cy - 70)
    b1 = rot(cx + d, cy - 70)
    c.line([b0, b1], mix(BG, WOOD, 0.7), 10)
    fx, fy = rot(cx + d, cy - 20)
    c.line([b1, (fx, fy)], mix(BG, WOOD, 0.7), 8)
    c.ellipse(fx, fy, 70, 26, fill=mix(BG, (220, 220, 210), 0.9))
    sub = (fy + 26 - wl)
    if sub > 22:
        L = min(220, (sub - 20) * 9)
        c.arrow(fx, fy + 40, fx, fy + 40 - L, LIFT, 6, 18)
        c.text(fx + 90, fy - 60, '浮杆被压进水里 → 浮力往上托', 'bold', 22, LIFT, 'lm')
    else:
        c.arrow(fx, fy, fx, fy + 140, NRED, 6, 18)
        c.text(fx + 90, fy + 80, '浮杆被抬出水 → 自身的重往下拉', 'bold', 22, NRED, 'lm')
    c.line([(cx, cy - 200), (cx, cy + 40)], mix(BG, MUTED, 0.6), 2)
    c.line([(cx, cy - 180), (fx, cy - 180)], SPARK, 3)
    c.text((cx + fx) / 2, cy - 210, '力臂', 'bold', 24, SPARK, 'mm')
    c.text(cx, cy + 130, '独木舟（从船头方向看）', 'sans', 22, INK, 'mm')
    c.rect(1380, 200, 1860, 420, fill=SHEET, r=14)
    c.text(1620, 260, '扶正的劲 = 力 × 力臂', 'bold', 28, INK, 'mm')
    c.text(1620, 320, '同样的力，力臂长一倍', 'sans', 22, MUTED, 'mm')
    c.text(1620, 360, '扶正的劲就大一倍', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '又细又长的独木舟跑得快，可一阵浪就能把它掀翻'),
                (7.2, 14, '在旁边远远伸出一根浮杆：船往浮杆那边歪，浮杆被压进水里，浮力往上托'),
                (14.2, 22, '船往另一边歪，浮杆被抬出水面，它的重量往下拉：两头都把船拉回来（示意）')], y=1010)


def b144_distance(c, t, i):
    corner_tag(c, 'B144 · 往一边放硬币，几枚会翻？')
    c.text(60, 96, '保鲜盒当独木舟，往一侧边上一枚枚放硬币：不绑浮杆、浮杆离 10 厘米、离 20 厘米各几枚翻', 'serif', 34, INK)
    vals = [('不绑浮杆', 0, 3), ('浮杆 10 厘米', 120, 9), ('浮杆 20 厘米', 240, 16)]
    p = min(1.0, t / 16)
    for k, (lab, d, n) in enumerate(vals):
        x0 = 140 + k * 420
        y0 = 360
        c.rect(x0, y0, x0 + 110, y0 + 420, fill=mix(BG, WOOD, 0.7), r=40)
        if d:
            c.line([(x0 + 110, y0 + 120), (x0 + 110 + d, y0 + 120)], mix(BG, WOOD, 0.6), 6)
            c.line([(x0 + 110, y0 + 300), (x0 + 110 + d, y0 + 300)], mix(BG, WOOD, 0.6), 6)
            c.rect(x0 + 90 + d, y0 + 90, x0 + 130 + d, y0 + 330, fill=(220, 220, 210), r=18)
        shown = min(n, int(p * 18))
        for j in range(shown):
            c.ellipse(x0 + 20, y0 + 400 - j * 22, 16, 9, fill=SPARK)
        if shown >= n:
            c.text(x0 + 100, y0 + 470, f'第 {n} 枚翻了', 'bold', 24, NRED, 'mm')
        c.text(x0 + 100, y0 - 40, lab, 'bold', 26, INK, 'mm')
    c.rect(1420, 300, 1860, 840, fill=SHEET, r=14)
    c.text(1640, 340, '翻船前放了几枚（示意）', 'sans', 22, MUTED, 'mm')
    for k, (lab, d, n) in enumerate(vals):
        x = 1500 + k * 140
        h = 420 * n / 16 * p
        c.rect(x - 40, 800 - h, x + 40, 800, fill=mix(BG, FIELD, 0.85), r=6)
        c.text(x, 820, ['无', '10', '20'][k], 'mono', 22, INK, 'mm')
    c.text(1640, 380, '以实测为准', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '先不绑浮杆，往保鲜盒的一侧边上一枚一枚放硬币，没几枚就翻了'),
                (7.2, 14, '绑上离船 10 厘米的浮杆，同样的放法，要多放好几枚才翻'),
                (14.2, 22, '浮杆挪到 20 厘米，力臂长了，还要更多枚：远远伸出去，就是为了这个（示意）')], y=1010)


# ---------------------------------------------------------------- B145 草拌泥
RNG = random.Random(145)


def _cracks(seed, n, length, fiber):
    r = random.Random(seed)
    out = []
    for k in range(n):
        a = r.uniform(0, 2 * math.pi)
        x, y = r.uniform(-120, 120), r.uniform(-120, 120)
        pts = [(x, y)]
        L = length * (0.35 if fiber else 1.0) * r.uniform(0.6, 1.2)
        for j in range(10):
            a += r.uniform(-0.6, 0.6)
            x += L / 10 * math.cos(a)
            y += L / 10 * math.sin(a)
            pts.append((x, y))
        out.append(pts)
    return out


CR_PLAIN = _cracks(1, 13, 300, False)
CR_FIB = _cracks(2, 7, 230, True)
FIBERS = [(RNG.uniform(-150, 150), RNG.uniform(-150, 150), RNG.uniform(0, math.pi)) for _ in range(40)]


def b145_shrink(c, t, i):
    corner_tag(c, 'B145 · 泥干了往里缩，就会裂')
    c.text(60, 96, '湿泥饼慢慢干：水跑掉，泥往里缩；不掺东西的裂成一块块，掺了草的只有细细的短缝', 'serif', 36, INK)
    p = min(1.0, t / 18)
    for k, (lab, cr, fib) in enumerate([('不掺东西', CR_PLAIN, False), ('掺剪短的干草', CR_FIB, True)]):
        cx, cy = 520 + k * 880, 560
        R = 230 * (1 - 0.06 * p)
        c.ellipse(cx, cy, R, R, fill=mix(mix(BG, CLAY, 0.95), (200, 170, 140), p * 0.6))
        if fib:
            for fx, fy, fa in FIBERS:
                if fx * fx + fy * fy < 190 * 190:
                    c.line([(cx + fx - 20 * math.cos(fa), cy + fy - 20 * math.sin(fa)), (cx + fx + 20 * math.cos(fa), cy + fy + 20 * math.sin(fa))], mix(BG, STRAW, 0.9), 3)
        g = max(0, (p - 0.3) / 0.7)
        for pts in cr:
            m = max(2, int(len(pts) * g))
            if g > 0:
                pp = [(cx + x * (1 - 0.06 * p), cy + y * (1 - 0.06 * p)) for x, y in pts[:m] if x * x + y * y < 220 * 220]
                if len(pp) > 1:
                    c.line(pp, mix(BG, (40, 30, 25), 0.95), 2 if fib else 5)
        c.text(cx, 840, lab, 'bold', 28, INK, 'mm')
    c.text(960, 300, f'晾了 {p * 3:.1f} 天', 'mono', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '同样的泥、同样厚的两块饼，一块什么都不掺，一块掺了剪短的干草'),
                (7.2, 14, '泥里的水慢慢跑掉，泥粒挨得更紧，整块往里缩'),
                (14.2, 22, '缩不动的地方就被扯开：不掺的裂成大缝，掺草的只有细细的短缝（示意）')], y=1010)


def b145_fiber(c, t, i):
    corner_tag(c, 'B145 · 一根草横在缝上，把两边拉住')
    c.text(60, 96, '放大一条刚开始的裂缝：没有草，缝一扯就开；有一根草横跨两边，它被拉紧，把缝拽住', 'serif', 36, INK)
    p = min(1.0, t / 14)
    for k, (lab, fib) in enumerate([('没有草', False), ('有一根草', True)]):
        x0 = 120 + k * 880
        gap = 8 + p * (90 if not fib else 18)
        mid = x0 + 340
        c.rect(x0, 300, mid - gap / 2, 760, fill=mix(BG, CLAY, 0.9), r=8)
        c.rect(mid + gap / 2, 300, x0 + 680, 760, fill=mix(BG, CLAY, 0.9), r=8)
        r = random.Random(k)
        for j in range(60):
            x = r.uniform(x0 + 10, x0 + 670)
            y = r.uniform(310, 750)
            if abs(x - mid) < gap / 2 + 6:
                continue
            c.ellipse(x + (-p * (gap / 2 - 4) if x < mid else p * (gap / 2 - 4)) * 0, y, 7, 7, fill=mix(BG, (190, 140, 100), 0.8))
        c.arrow(x0 + 120, 830, x0 + 20, 830, MUTED, 4, 12)
        c.arrow(x0 + 560, 830, x0 + 660, 830, MUTED, 4, 12)
        c.text(mid, 830, '干缩往两边扯', 'sans', 22, MUTED, 'mm')
        if fib:
            c.line([(mid - 220, 520), (mid + 220, 540)], mix(BG, STRAW, 1.0), 10)
            c.arrow(mid - 40, 470, mid - 140, 470, LIFT, 4, 12)
            c.arrow(mid + 40, 470, mid + 140, 470, LIFT, 4, 12)
            c.text(mid, 395, '草被拉紧，把两边拽住', 'bold', 22, LIFT, 'mm')
        c.text(mid, 260, lab, 'bold', 28, INK, 'mm')
        c.text(mid, 900, f'缝宽 {gap / 30:.1f} 毫米（示意）', 'mono', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '泥干缩的时候，到处都在往里扯，最弱的地方先裂开一条小缝'),
                (7.2, 14, '没有东西拉着，缝越扯越宽，变成一条大裂缝'),
                (14.2, 22, '一根草横跨在缝上被拉紧，缝就只能停在细细一条；草太多泥粘不住，反而松（示意）')], y=1010)


CLIPS = {
 'B143_升力': (b143_lift, 22), 'B143_飞回': (b143_return, 22),
 'B143_片头': (titles.opening(BSER, VOL34, SB34, 3, '澳大利亚原住民使用已有数千年'), 7),
 'B143_片尾': (titles.closing(BSER, VOL34, SB34, 3, '下集：细长的独木舟绑一根浮杆，为什么就不翻了？'), 7),
 'B144_力臂': (b144_moment, 22), 'B144_浮杆': (b144_distance, 22),
 'B144_片头': (titles.opening(BSER, VOL34, SB34, 4, '南岛语族的边架艇遍布太平洋'), 7),
 'B144_片尾': (titles.closing(BSER, VOL34, SB34, 4, '下集：老泥墙里掺着稻草，为什么干了不容易裂？'), 7),
 'B145_收缩': (b145_shrink, 22), 'B145_纤维': (b145_fiber, 22),
 'B145_片头': (titles.opening(BSER, VOL34, SB34, 5, '新石器以来土坯里就掺草'), 7),
 'B145_片尾': (titles.closing(BSER, VOL34, SB34, 5, '下集：地面冷得结冰，地窖里为什么冻不坏白菜？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
