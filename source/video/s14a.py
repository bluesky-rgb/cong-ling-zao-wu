"""第十四季（古法解密 4.0：飞、响、量、造、藏）第一批：B40 竹蜻蜓、B41 风筝、B42 陶埙 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB14 = [('B40', '竹蜻蜓'), ('B41', '风筝'), ('B42', '陶埙'), ('B43', '杆秤'), ('B44', '船尾舵'),
        ('B45', '扎染'), ('B46', '夯土'), ('B47', '斗拱'), ('B48', '腌菜'), ('B49', '含嘉仓')]
VOL14 = '第十四季 · 古法解密 4.0'
BAMBOO = (190, 170, 100)
AIR = (120, 170, 220)
CLAY = (170, 110, 70)
KITE = (210, 80, 70)

# ---------------------------------------------------------------- B40 竹蜻蜓
def b40_lift(c, t, i):
    corner_tag(c, 'B40 · 把空气往下推')
    c.text(60, 96, '叶片是斜的：转起来，就把空气往下推', 'serif', 40, INK)
    # side view of top
    cx, cy = 560, 420
    c.line([(cx, cy), (cx, cy + 300)], BAMBOO, 10)
    c.line([(cx - 300, cy - 14), (cx, cy)], BAMBOO, 14)
    c.line([(cx, cy), (cx + 300, cy + 14)], BAMBOO, 14)
    ph = (t * 3) % (2 * math.pi)
    c.arc(cx, cy - 70, 300, 50, 200, 340, mix(BG, MUTED, 0.8), 3)
    c.arrow(cx + 270, cy - 92, cx + 300, cy - 80, mix(BG, MUTED, 0.8), 3, 14)
    c.text(cx - 330, cy - 120, '旋转', 'sans', 22, MUTED, 'mm')
    a = fade(t, 2, 3)
    # air arrows going down
    for k in range(5):
        x = cx - 240 + k * 120
        off = ((t * 120 + k * 37) % 200)
        c.arrow(x, cy + 60 + off * 0.6, x, cy + 120 + off * 0.6, mix(BG, AIR, a), 4, 14)
    b = fade(t, 6, 7)
    c.arrow(cx, cy - 40, cx, cy - 200, mix(BG, GREEN, b), 8, 26)
    c.text(cx + 30, cy - 150, '空气反推：向上', 'bold', 28, mix(BG, GREEN, b), 'lm')
    c.text(cx, cy + 380, '推下去的空气', 'sans', 24, mix(BG, AIR, a), 'mm')
    # blade cross section
    d = fade(t, 10, 11)
    x0, y0 = 1380, 480
    c.text(x0, 220, '叶片的横截面', 'bold', 28, mix(BG, INK, d), 'mm')
    ang = math.radians(20)
    L = 220
    p1 = (x0 - L * math.cos(ang), y0 - L * math.sin(ang))
    p2 = (x0 + L * math.cos(ang), y0 + L * math.sin(ang))
    c.line([p1, p2], mix(BG, BAMBOO, d), 16)
    c.arrow(x0 - 380, y0 - 140, x0 - 260, y0 - 140, mix(BG, MUTED, d), 4, 16)
    c.text(x0 - 320, y0 - 180, '叶片往这边转', 'sans', 22, mix(BG, MUTED, d), 'mm')
    e = fade(t, 13, 14)
    for k in range(3):
        xx = x0 - 60 + k * 70
        c.arrow(xx, y0 + 60, xx + 20, y0 + 200, mix(BG, AIR, e), 4, 14)
    c.text(x0, y0 + 260, '空气被斜面拨向下方', 'sans', 24, mix(BG, INK, e), 'mm')
    caps(c, t, [(0, 6, '双手一搓，竹蜻蜓转起来，自己往上飞'),
                (6.2, 13, '叶片是斜着装的：转的时候，像一把斜铲把空气往下拨'),
                (13.2, 22, '空气被推下去，也同时把叶片推上来：这就是升力，和直升机的旋翼一样')], y=1010)

def b40_angle(c, t, i):
    corner_tag(c, 'B40 · 叶片斜多少度最好')
    c.text(60, 96, '太平推不动空气，太陡只剩阻力', 'serif', 40, INK)
    angs = [0, 15, 30, 45]
    lift = [0.05, 0.85, 1.0, 0.55]  # schematic
    for k, (g, v) in enumerate(zip(angs, lift)):
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        if a <= 0: continue
        x = 300 + k * 380
        ang = math.radians(g)
        c.line([(x - 100 * math.cos(ang), 330 - 100 * math.sin(ang)), (x + 100 * math.cos(ang), 330 + 100 * math.sin(ang))], mix(BG, BAMBOO, a), 14)
        c.text(x, 440, f'{g}°', 'mono', 34, mix(BG, INK, a), 'mm')
        h = 360 * v * fade(t, 2 + k * 2.5, 3.5 + k * 2.5)
        col = GREEN if v == max(lift) else MUTED
        c.rect(x - 70, 880 - h, x + 70, 880, fill=mix(BG, col, a), r=6)
    c.line([(160, 880), (1640, 880)], LINE, 2)
    c.text(160, 500, '飞行高度（示意）', 'sans', 24, MUTED, 'lm')
    d = fade(t, 12, 13)
    c.rect(1240, 150, 1820, 216, fill=mix(BG, SHEET, d), r=10)
    c.text(1390, 183, '高度只是示意：', 'sans', 24, mix(BG, MUTED, d), 'mm')
    c.text(1640, 183, '最好的角度以实测为准', 'bold', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 6, '0 度：叶片是平的，转得再快也推不动空气'),
                (6.2, 13, '斜一点，推下去的空气越来越多，飞得越来越高'),
                (13.2, 22, '太陡了，空气在叶片背面乱成一团，只剩阻力：转不快，也飞不高')], y=1010)

# ---------------------------------------------------------------- B41 风筝
def b41_forces(c, t, i):
    corner_tag(c, 'B41 · 风筝上的四个力')
    c.text(60, 96, '风筝停在天上：四个力刚好抵消', 'serif', 40, INK)
    kx, ky = 900, 460
    tilt = math.radians(30)
    pts = [(0, -160), (90, -20), (0, 140), (-90, -20)]
    rp = [(kx + x * math.cos(tilt) - y * math.sin(tilt) * 0.3, ky + y * math.cos(tilt)) for x, y in pts]
    c.poly(rp, KITE)
    c.line([rp[0], rp[2]], (120, 60, 40), 3)
    # string to ground
    c.line([(kx, ky + 30), (300, 950)], MUTED, 2)
    c.text(300, 980, '拉线', 'sans', 22, MUTED, 'mm')
    # wind
    for k in range(5):
        off = (t * 200 + k * 80) % 400
        c.arrow(120 + off, 300 + k * 70, 220 + off, 300 + k * 70, mix(BG, AIR, 0.7), 3, 12)
    F = [('风把它往上托（升力）', 0, -1, GREEN, 2), ('风把它往后推（阻力）', 1, 0, NRED, 5), ('重力', 0, 1, MUTED, 8), ('线往斜下拉', -0.6, 0.8, COPPER, 11)]
    for nm, dx, dy, col, t0 in F:
        a = fade(t, t0, t0 + 1)
        if a <= 0: continue
        L = 200
        c.arrow(kx, ky, kx + dx * L, ky + dy * L, mix(BG, col, a), 7, 22)
        c.text(kx + dx * L + (20 if dx >= 0 else -20), ky + dy * L + (-24 if dy < 0 else 24), nm, 'bold', 26, mix(BG, col, a), 'lm' if dx >= 0 else 'rm')
    caps(c, t, [(0, 5, '风筝斜着迎风：风撞上纸面，被拨向下方'),
                (5.2, 11, '空气把风筝往上托，这是升力；同时往后推，这是阻力'),
                (11.2, 22, '再加上重力和线的拉力：四个力刚好抵消，风筝就停在天上')], y=1010)

def b41_bridle(c, t, i):
    corner_tag(c, 'B41 · 提线点和尾巴')
    c.text(60, 96, '提线拴在哪，决定风筝斜多少度', 'serif', 40, INK)
    opts = [('提线点太靠头', 75, '几乎竖直迎风：阻力大、飞不高', NRED), ('提线点适中', 35, '斜着迎风：升得最高（以实测为准）', GREEN), ('提线点太靠尾', 8, '几乎平躺：托不起来，容易栽', NRED)]
    for k, (nm, g, note, col) in enumerate(opts):
        a = fade(t, 1 + k * 3, 2 + k * 3)
        if a <= 0: continue
        x, y = 320 + k * 620, 440
        ang = math.radians(g)
        L = 150
        c.line([(x - L * math.cos(ang), y - L * math.sin(ang)), (x + L * math.cos(ang), y + L * math.sin(ang))], mix(BG, KITE, a), 14)
        c.text(x, 220, nm, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(x, 680, note, 'sans', 22, mix(BG, col, a), 'mm')
    d = fade(t, 12, 13)
    c.rect(200, 780, 1720, 900, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 820, '尾巴：后面多一点阻力，像箭的羽毛，把风筝的头一直对准风', 'bold', 26, mix(BG, INK, d), 'mm')
    c.text(960, 865, '没尾巴的菱形风筝容易打转（实验 3 对比）', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '风筝和风的夹角，叫迎角：提线拴的位置决定它'),
                (6.2, 12, '太平，托不起来；太竖，只剩阻力，还会打转'),
                (12.2, 22, '尾巴在后面拖着，让风筝的头始终对着风：这是稳定性')], y=1010)

# ---------------------------------------------------------------- B42 陶埙
def b42_spring(c, t, i):
    corner_tag(c, 'B42 · 腔里的空气是弹簧')
    c.text(60, 96, '吹瓶口为什么会响：口上的空气在上下弹', 'serif', 40, INK)
    cx, cy = 560, 600
    c.ellipse(cx, cy, 240, 260, fill=mix(BG, CLAY, 0.6), outline=CLAY, width=6)
    c.ellipse(cx, cy, 200, 220, fill=BG)
    c.rect(cx - 40, cy - 330, cx + 40, cy - 230, fill=BG)
    c.line([(cx - 40, cy - 330), (cx - 40, cy - 238)], CLAY, 6)
    c.line([(cx + 40, cy - 330), (cx + 40, cy - 238)], CLAY, 6)
    osc = math.sin(t * 9) * fade(t, 2, 3)
    py = cy - 290 + 26 * osc
    c.rect(cx - 36, py - 24, cx + 36, py + 24, fill=AIR, r=6)
    c.text(cx + 80, cy - 290, '口上的一小团空气：小球', 'bold', 24, AIR, 'lm')
    # spring inside
    pts = []
    top, bot = cy - 230 + 26 * osc, cy + 180
    for k in range(41):
        y = top + (bot - top) * k / 40
        pts.append((cx + (40 if k % 2 else -40) * (0 if k in (0, 40) else 1), y))
    c.line(pts, mix(BG, GREEN, fade(t, 4, 5)), 4)
    c.text(cx, cy + 300, '腔里的空气：弹簧', 'bold', 26, mix(BG, GREEN, fade(t, 4, 5)), 'mm')
    d = fade(t, 10, 11)
    x0 = 1100
    c.text(x0, 260, '弹簧越软、小球越重，弹得越慢，音越低：', 'sans', 26, mix(BG, INK, d), 'lm')
    rows = [('腔体越大', '弹簧越软', '音越低'), ('瓶里水越多', '空气越少、弹簧越硬', '音越高'), ('开口越大', '小球推得越容易', '音越高')]
    for k, (a_, b_, c_) in enumerate(rows):
        e = fade(t, 11 + k * 2.5, 12 + k * 2.5)
        y = 360 + k * 110
        c.rect(x0, y - 40, x0 + 720, y + 40, fill=mix(BG, SHEET, e), r=10)
        c.text(x0 + 24, y, f'{a_} → {b_} → {c_}', 'sans', 26, mix(BG, INK, e), 'lm')
    caps(c, t, [(0, 6, '对着瓶口吹，瓶子会呜呜地响：陶埙也是这样发声的'),
                (6.2, 13, '口上那一小团空气像一个小球，腔里的空气像一根弹簧，一推一弹'),
                (13.2, 22, '这叫亥姆霍兹共鸣：腔体越大音越低，开口越大音越高')], y=1010)

def b42_holes(c, t, i):
    corner_tag(c, 'B42 · 孔开在哪，重要吗')
    c.text(60, 96, '笛子看孔的位置，埙看孔的总面积', 'serif', 40, INK)
    # flute
    a = fade(t, 1, 2)
    c.text(120, 230, '笛子：管里的空气柱有长短', 'bold', 28, mix(BG, INK, a), 'lm')
    c.rect(120, 290, 900, 340, fill=mix(BG, BAMBOO, a), r=20)
    for k in range(6):
        c.ellipse(300 + k * 100, 315, 14, 14, fill=BG)
    c.text(120, 390, '按住不同的孔，空气柱长度不同：位置很重要', 'sans', 24, mix(BG, MUTED, a), 'lm')
    # xun
    b = fade(t, 7, 8)
    c.text(1040, 230, '埙：整个腔体一起振动', 'bold', 28, mix(BG, INK, b), 'lm')
    for k, pos in enumerate([(-60, -40), (60, 60)]):
        cx, cy = 1200 + k * 400, 560
        c.ellipse(cx, cy, 130, 150, fill=mix(BG, CLAY, b))
        c.ellipse(cx, cy - 160, 18, 10, fill=BG)
        c.ellipse(cx + pos[0], cy + pos[1], 20, 20, fill=BG)
        c.text(cx, cy + 210, '孔在左上' if k == 0 else '孔在右下', 'sans', 24, mix(BG, INK, b), 'mm')
    d = fade(t, 12, 13)
    c.text(1400, 840, '同样大小的孔：音高几乎一样（实验 3 验证）', 'bold', 26, mix(BG, GREEN, d), 'mm')
    c.text(1400, 890, '要改音高：开更多的孔、或把孔开大', 'sans', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 7, '笛子是一根管子：按住哪个孔，就决定了管里空气柱有多长'),
                (7.2, 14, '埙不一样，它是一个整体的「弹簧腔」：看的是开口总面积'),
                (14.2, 22, '所以埙的孔可以开在手指方便的地方：古人照样能吹出五声音阶（以实测为准）')], y=1010)

CLIPS = {
 'B40_升力': (b40_lift, 22), 'B40_角度': (b40_angle, 22),
 'B40_片头': (titles.opening(BSER, VOL14, SB14, 0, '晋 · 葛洪《抱朴子》「飞车」'), 7),
 'B40_片尾': (titles.closing(BSER, VOL14, SB14, 0, '下集：一张纸，为什么能被风托在天上？'), 7),
 'B41_受力': (b41_forces, 22), 'B41_提线': (b41_bridle, 22),
 'B41_片头': (titles.opening(BSER, VOL14, SB14, 1, '战国 · 墨子作木鸢'), 7),
 'B41_片尾': (titles.closing(BSER, VOL14, SB14, 1, '下集：一个泥蛋，怎么吹出不同的音？'), 7),
 'B42_弹簧': (b42_spring, 22), 'B42_开孔': (b42_holes, 22),
 'B42_片头': (titles.opening(BSER, VOL14, SB14, 2, '新石器时代 · 半坡陶埙'), 7),
 'B42_片尾': (titles.closing(BSER, VOL14, SB14, 2, '下集：一根木杆一个秤砣，怎么称出不同的重量？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
