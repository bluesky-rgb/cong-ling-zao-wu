"""第二十四季（古法解密 9.0：田、路、天、巧）第一批：B90 桔槔、B91 龙骨水车、B92 发豆芽 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import rot

SB24 = [('B90', '桔槔'), ('B91', '龙骨水车'), ('B92', '发豆芽'), ('B93', '独轮车'), ('B94', '鱼笱'),
        ('B95', '计里画方'), ('B96', '沙漏'), ('B97', '浑仪'), ('B98', '剪纸'), ('B99', '鲁班锁')]
VOL24 = '第二十四季 · 古法解密 9.0'
WOOD = (175, 125, 75)
DARKWOOD = (130, 90, 55)
STONE = (140, 140, 135)
WATER = (70, 130, 200)
WATER_L = (110, 170, 230)
BEAN = (110, 170, 80)
SPROUT = (235, 230, 200)
LEAF = (110, 180, 90)
SOIL = (120, 90, 60)


# ---------------------------------------------------------------- B90 桔槔
def b90_lever(c, t, i):
    corner_tag(c, 'B90 · 把力气存在石头里')
    c.text(60, 96, '长杆一头挂水桶、一头挂石头：压空桶时把石头抬高，提满桶时石头往下帮你', 'serif', 40, INK)
    px, py = 900, 440
    L1, L2 = 460, 300
    phase = (t % 11) / 11
    ang = math.radians(18) * math.sin(phase * 2 * math.pi)
    bx, by = px - L1 * math.cos(ang), py + L1 * math.sin(ang)
    sx, sy = px + L2 * math.cos(ang), py - L2 * math.sin(ang)
    c.rect(px - 14, py, px + 14, 900, fill=DARKWOOD)
    c.line([(bx, by), (sx, sy)], WOOD, 14)
    c.line([(bx, by), (bx, by + 220)], INK, 3)
    full = math.sin(phase * 2 * math.pi) < 0
    c.rect(bx - 40, by + 220, bx + 40, by + 300, fill=(150, 150, 160), r=6)
    if full:
        c.rect(bx - 36, by + 236, bx + 36, by + 296, fill=WATER)
    c.ellipse(sx, sy + 50, 60, 46, fill=STONE)
    c.line([(sx, sy), (sx, sy + 10)], INK, 3)
    c.rect(120, 780, 520, 900, fill=mix(BG, WATER, 0.6))
    c.text(320, 920, '井', 'sans', 22, MUTED, 'mm')
    c.text(sx, sy + 130, '石头（配重）', 'bold', 24, INK, 'mm')
    c.rect(1420, 260, 1860, 620, fill=SHEET, r=14)
    c.text(1640, 300, '手上要用的力（示意）', 'bold', 24, INK, 'mm')
    rows = [('不挂石头：压空桶', 0.05), ('不挂石头：提满桶', 1.0), ('挂石头：压空桶', 0.5), ('挂石头：提满桶', 0.5)]
    for k, (nm, v) in enumerate(rows):
        y = 360 + k * 62
        c.text(1440, y, nm, 'sans', 20, INK, 'lm')
        c.rect(1650, y - 12, 1650 + 180 * v, y + 12, fill=NRED if v > 0.8 else (GREEN if v == 0.5 else MUTED))
    c.text(1640, 600, '配重约半桶水重时，两头都只用一半力', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '井边竖一根柱子，架一根长杆：一头吊水桶，另一头绑一块大石头'),
                (7.2, 14, '把空桶往下压，石头被抬高；桶装满水往上提时，石头往下坠，帮你一起使劲'),
                (14.2, 22, '石头差不多是半桶水那么重：下压和上提都只要一半力。力气被存进了抬高的石头里')], y=1010)


def b90_cycle(c, t, i):
    corner_tag(c, 'B90 · 一来一回，石头当「电池」')
    c.text(60, 96, '下压空桶：手做的功存进石头；上提满桶：石头把功还给你', 'serif', 40, INK)
    phase = (t % 11) / 11
    up = math.sin(phase * 2 * math.pi)
    h = 0.5 + 0.5 * up
    c.rect(260, 260, 760, 860, fill=SHEET, r=14)
    c.text(510, 300, '石头的高度', 'bold', 26, INK, 'mm')
    c.rect(450, 360, 570, 820, outline=LINE, width=2)
    c.rect(452, min(816, 820 - 456 * h), 568, 818, fill=mix(BG, SPARK, 0.8))
    c.ellipse(510, 820 - 456 * h - 20, 40, 30, fill=STONE)
    c.text(510, 840, '高 = 存得多', 'sans', 20, MUTED, 'mm')
    c.rect(960, 260, 1860, 860, fill=SHEET, r=14)
    c.text(1410, 300, '这一刻在做什么', 'bold', 26, INK, 'mm')
    if up > 0:
        c.text(1410, 420, '把空桶压下井', 'bold', 34, SPARK, 'mm')
        c.text(1410, 500, '手往下推 → 石头升高', 'sans', 28, INK, 'mm')
        c.text(1410, 560, '功被「存」起来', 'sans', 26, MUTED, 'mm')
    else:
        c.text(1410, 420, '把满桶提上来', 'bold', 34, GREEN, 'mm')
        c.text(1410, 500, '石头下坠 → 帮手往上拉', 'sans', 28, INK, 'mm')
        c.text(1410, 560, '存的功「还」回来', 'sans', 26, MUTED, 'mm')
    c.text(1410, 700, '不省功，但把一次大力气拆成两次小力气', 'sans', 24, INK, 'mm')
    caps(c, t, [(0, 7, '没有桔槔时：压空桶几乎不用力，提满桶却要一口气使出全部力气'),
                (7.2, 14, '有了石头：压空桶时多用一点力，把石头举高；提满桶时，石头把这份力气还回来'),
                (14.2, 22, '总的功一点没少，可每一次都只用一半力：和第 39 集杠杆、B43 杆秤是同一根杆子')], y=1010)


# ---------------------------------------------------------------- B91 龙骨水车
def b91_chain(c, t, i):
    corner_tag(c, 'B91 · 一圈刮板，一格格推水')
    c.text(60, 96, '斜槽里装一圈连在一起的刮板：上面的轮子一转，刮板把槽里的水一格格推上去', 'serif', 40, INK)
    x0, y0, x1, y1 = 260, 860, 1500, 360
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    c.rect(60, 820, 560, 940, fill=mix(BG, WATER, 0.6))
    c.text(200, 960, '河', 'sans', 22, MUTED, 'mm')
    c.rect(1400, 380, 1860, 460, fill=mix(BG, (100, 150, 80), 0.6))
    c.text(1700, 360, '田', 'sans', 22, MUTED, 'mm')
    trough = [(x0 - nx * 10, y0 - ny * 10), (x1 - nx * 10, y1 - ny * 10), (x1 + nx * 50, y1 + ny * 50), (x0 + nx * 50, y0 + ny * 50)]
    c.poly(trough, mix(BG, WOOD, 0.5))
    c.ellipse(x1, y1 - 40, 70, 70, outline=WOOD, width=8)
    c.ellipse(x0, y0 - 40, 50, 50, outline=WOOD, width=6)
    for k in range(6):
        a = t * 2 + k * math.pi / 3
        c.line([(x1, y1 - 40), (x1 + 70 * math.cos(a), y1 - 40 + 70 * math.sin(a))], WOOD, 4)
    gap = 80
    off = (t * 70) % gap
    n = int(L / gap) + 1
    for k in range(n):
        s = k * gap + off
        if s > L:
            continue
        px, py = x0 + ux * s, y0 + uy * s
        c.line([(px + nx * -8, py + ny * -8), (px + nx * 46, py + ny * 46)], DARKWOOD, 8)
        ws = s - gap * 0.5
        if ws > 0:
            wx, wy = x0 + ux * ws, y0 + uy * ws
            c.poly([(wx - ux * 34 + nx * 2, wy - uy * 34 + ny * 2), (wx + ux * 34 + nx * 2, wy + uy * 34 + ny * 2),
                    (wx + ux * 34 + nx * 38, wy + uy * 34 + ny * 38), (wx - ux * 34 + nx * 38, wy - uy * 34 + ny * 38)], WATER)
        rx, ry = x0 + ux * (L - s) + nx * 90, y0 + uy * (L - s) + ny * 90
        c.line([(rx, ry), (rx + nx * 20, ry + ny * 20)], mix(BG, DARKWOOD, 0.6), 6)
    c.text(x1 + 100, y1 - 120, '人踩或牛拉这个轮', 'sans', 22, INK, 'lm')
    caps(c, t, [(0, 7, '一条长长的木槽斜着架在河岸上，槽里装着一串用木销连起来的刮板，像一条龙的骨头'),
                (7.2, 14, '上面的轮子一转，刮板沿着槽往上走，每两块刮板之间兜住一格水'),
                (14.2, 22, '一格接一格推到槽顶，倒进田里；刮板绕过轮子，再从槽底下回到河里')], y=1010)


def b91_leak(c, t, i):
    corner_tag(c, 'B91 · 槽越陡，漏得越多')
    c.text(60, 96, '刮板和槽之间总有缝；槽越陡，水越容易从缝里往回漏', 'serif', 40, INK)
    for k, deg in enumerate((20, 45)):
        cx, cy = 480 + k * 800, 640
        a = math.radians(deg)
        L = 520
        x0, y0 = cx - L / 2 * math.cos(a), cy + L / 2 * math.sin(a)
        x1, y1 = cx + L / 2 * math.cos(a), cy - L / 2 * math.sin(a)
        c.line([(x0, y0 + 40), (x1, y1 + 40)], WOOD, 8)
        ux, uy = math.cos(a), -math.sin(a)
        for j in range(5):
            s = j * L / 5 + 40
            px, py = x0 + ux * s, y0 + uy * s
            c.line([(px, py + 40), (px - uy * 0 + 0, py + 40 - 60)], DARKWOOD, 6)
            fill = 1.0 - (0.15 if deg == 20 else 0.5)
            ws = s - L / 10
            wx, wy = x0 + ux * ws, y0 + uy * ws
            h = 50 * fill
            c.poly([(wx - ux * 40, wy - uy * 40 + 40), (wx + ux * 40, wy + uy * 40 + 40), (wx + ux * 40, wy + uy * 40 + 40 - h), (wx - ux * 40, wy - uy * 40 + 40 - h)], WATER)
            for m in range(2):
                ss = ((t * 0.8 + m * 0.5 + j * 0.2) % 1)
                if deg == 45 or m == 0:
                    lx, ly = px - ux * 30 * ss, py - uy * 30 * ss + 36
                    c.ellipse(lx, ly, 4, 4, fill=WATER_L)
        c.text(cx, 260, f'槽斜 {deg}°', 'bold', 30, INK, 'mm')
        c.text(cx, 920, '每格大多兜得住' if deg == 20 else '一半漏回下一格', 'sans', 24, GREEN if deg == 20 else NRED, 'mm')
    caps(c, t, [(0, 7, '刮板不可能和槽贴得一丝不漏，总留着一点缝'),
                (7.2, 14, '槽平一些，水安安稳稳待在两块刮板之间；槽一陡，水就顺着缝往下一格漏'),
                (14.2, 22, '所以龙骨水车总是斜得不太陡，田太高就分好几级：和第 28 集水车提水一样，要找最合适的角度（示意）')], y=1010)


# ---------------------------------------------------------------- B92 发豆芽
def _sprout(c, x, base, L, col, leaf=False, bend=0.0):
    pts = []
    for j in range(13):
        u = j / 12
        pts.append((x + bend * u * u * 40, base - L * u))
    c.line(pts, col, 6)
    tx, ty = pts[-1]
    c.ellipse(tx, ty, 14, 10, fill=BEAN if not leaf else LEAF)
    if leaf:
        c.ellipse(tx - 16, ty - 6, 14, 8, fill=LEAF)
        c.ellipse(tx + 16, ty - 6, 14, 8, fill=LEAF)
    c.line([(x, base), (x - 10, base + 40), (x + 6, base + 70)], SPROUT, 3)


def b92_germ(c, t, i):
    corner_tag(c, 'B92 · 喝水、醒来、伸出根')
    c.text(60, 96, '干豆子吸水胀大、种皮裂开，先伸出白白的根，再往上顶出茎', 'serif', 40, INK)
    stages = ['干豆', '泡一夜', '露白', '第 2 天', '第 4 天']
    for k, nm in enumerate(stages):
        x = 260 + k * 340
        base = 760
        c.rect(x - 130, base, x + 130, base + 30, fill=mix(BG, (230, 230, 235), 0.4), r=6)
        a = fade(t, k * 3.5, k * 3.5 + 2)
        if a <= 0:
            continue
        if k == 0:
            c.ellipse(x, base - 20, 22, 16, fill=mix(BG, (80, 120, 60), a))
        elif k == 1:
            c.ellipse(x, base - 26, 32, 24, fill=mix(BG, BEAN, a))
        elif k == 2:
            c.ellipse(x, base - 26, 32, 24, fill=mix(BG, BEAN, a))
            c.line([(x + 20, base - 20), (x + 40, base + 10)], mix(BG, SPROUT, a), 4)
        else:
            L = 120 if k == 3 else 270
            _sprout(c, x, base, L * a, mix(BG, SPROUT, a))
        c.text(x, base + 70, nm, 'bold', 24, INK, 'mm')
    c.rect(1500, 200, 1860, 420, fill=SHEET, r=12)
    c.text(1680, 240, '发芽要三样', 'bold', 24, INK, 'mm')
    c.text(1680, 300, '水 · 温暖 · 空气', 'sans', 26, SPARK, 'mm')
    c.text(1680, 360, '泡在水里不透气会烂', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '干绿豆像睡着了：里面的小芽和养分都封在硬硬的种皮里'),
                (7.2, 14, '泡一夜水，豆子吸饱了水胀大，种皮裂开，先探出一根白白的小根'),
                (14.2, 22, '接着胚轴往上长：这根又白又胖的茎，就是我们说的豆芽（实验豆芽只观察，不食用）')], y=1010)


def b92_dark(c, t, i):
    corner_tag(c, 'B92 · 黑暗里长得又白又长')
    c.text(60, 96, '见不到光，豆芽把力气都用来往上长、找光；一见光就变绿、长叶、不再猛长', 'serif', 40, INK)
    g = min(1.0, t / 18)
    for k, (nm, dark) in enumerate((('窗边有光', False), ('纸箱罩住', True))):
        cx = 520 + k * 880
        base = 860
        c.rect(cx - 320, base, cx + 320, base + 30, fill=mix(BG, (230, 230, 235), 0.4), r=6)
        if dark:
            c.rect(cx - 340, 220, cx + 340, base, outline=(150, 120, 80), width=6)
            c.text(cx, 250, '（纸箱）', 'sans', 20, MUTED, 'mm')
        else:
            c.ellipse(cx - 260, 260, 30, 30, fill=(250, 210, 90))
        for j in range(6):
            x = cx - 240 + j * 96
            L = (520 if dark else 240) * g * (0.85 + 0.15 * math.sin(j * 1.7))
            _sprout(c, x, base, L, SPROUT if dark else mix(SPROUT, LEAF, 0.6), leaf=not dark and g > 0.5, bend=0 if dark else -0.6)
        c.text(cx, base + 100, nm, 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '同样的豆子，一盒放在窗边，一盒用纸箱罩起来'),
                (7.2, 14, '纸箱里的豆芽又白又长：没有光，它就拼命把茎往上长，想快点钻出「土」去找光'),
                (14.2, 22, '窗边的那盒长得矮，早早变绿、张开小叶子，开始自己晒太阳造养分。卖的豆芽都是在暗处发的（示意）')], y=1010)


CLIPS = {
 'B90_配重': (b90_lever, 22), 'B90_存力': (b90_cycle, 22),
 'B90_片头': (titles.opening(BSER, VOL24, SB24, 0, '春秋《庄子 · 天地》记桔槔'), 7),
 'B90_片尾': (titles.closing(BSER, VOL24, SB24, 0, '下集：一串木板，怎么把河里的水「刮」到田里？'), 7),
 'B91_刮板': (b91_chain, 22), 'B91_漏损': (b91_leak, 22),
 'B91_片头': (titles.opening(BSER, VOL24, SB24, 1, '东汉翻车 · 三国马钧改进'), 7),
 'B91_片尾': (titles.closing(BSER, VOL24, SB24, 1, '下集：一把干绿豆，怎么几天就长成一盆豆芽？'), 7),
 'B92_萌发': (b92_germ, 22), 'B92_黄化': (b92_dark, 22),
 'B92_片头': (titles.opening(BSER, VOL24, SB24, 2, '宋代《山家清供》记豆芽'), 7),
 'B92_片尾': (titles.closing(BSER, VOL24, SB24, 2, '下集：一个轮子的车，怎么推得动几百斤东西？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
