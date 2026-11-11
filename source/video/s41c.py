"""第四十一季（第十七层）第三批：E218 碎纸机、E219 复印机、E220 扫描仪 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s41a import S41A, SER41, VOL41, STEEL, PAPERC

MOTOR = (120, 130, 150)
TONER = (40, 40, 45)
DRUM = (90, 160, 120)
LIGHT = (250, 240, 170)
PIX = (60, 60, 70)


def _gear(c, cx, cy, r, ang, col, n):
    pts = []
    for k in range(n * 2):
        a = ang + k * math.pi / n
        rr = r + (8 if k % 2 == 0 else -4)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    c.poly(pts, col)
    c.ellipse(cx, cy, 8, 8, fill=BG)
    c.line([(cx, cy), (cx + r * 0.7 * math.cos(ang), cy + r * 0.7 * math.sin(ang))], INK, 3)


# ---------------------------------------------------------------- E218 碎纸机
def e218_gearing(c, t, i):
    corner_tag(c, '第 218 集 · 转得快换成力气大')
    c.text(60, 96, '小电动机每分钟转几千圈，可力气不大；经过几级齿轮，小齿轮带大齿轮，转速一级级变慢，力气一级级变大', 'serif', 33, INK)
    c.rect(150, 440, 330, 640, fill=mix(BG, MOTOR, 0.9), r=16)
    c.text(240, 680, '电动机', 'bold', 22, INK, 'mm')
    w = t * 12
    stages = [(420, 540, 24, 8, mix(BG, STEEL, 0.9)), (560, 540, 96, 32, mix(BG, STEEL, 0.75)),
              (560, 540, 24, 8, mix(BG, SPARK, 0.8)), (760, 420, 96, 32, mix(BG, SPARK, 0.6)),
              (760, 420, 24, 8, mix(BG, GREEN, 0.8)), (960, 540, 96, 32, mix(BG, GREEN, 0.6))]
    angs = [w, -w / 4, -w / 4, w / 16, w / 16, -w / 64]
    order = [1, 0, 3, 2, 5, 4]
    for k in order:
        x, y, r, n, col = stages[k]
        _gear(c, x, y, r, angs[k], col, n)
    c.line([(330, 540), (420, 540)], INK, 6)
    c.rect(1120, 300, 1860, 760, fill=SHEET, r=12)
    c.text(1490, 350, '每一级：小齿轮 8 齿带大齿轮 32 齿', 'bold', 22, INK, 'mm')
    for k, (lab, sp, tq) in enumerate([('电动机', '1', '1'), ('第 1 级后', '1/4', '约 4 倍'), ('第 2 级后', '1/16', '约 16 倍'), ('第 3 级后（刀轴）', '1/64', '约 64 倍')]):
        y = 420 + k * 80
        c.text(1160, y, lab, 'sans', 22, INK, 'lm')
        c.text(1500, y, f'转速 {sp}', 'mono', 22, MUTED, 'lm')
        c.text(1680, y, f'力 {tq}', 'mono', 22, SPARK, 'lm')
    c.text(1490, 730, '（示意，不计损耗）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '电动机转得飞快，但每一下的力气很小'),
                (7.2, 14, '小齿轮带大齿轮：大齿轮转得慢了，推它的力却变大了'),
                (14.2, 22, '几级减速以后，刀轴转得很慢，力气大到能剪开一叠纸（示意）')], y=1010)


def e218_shear(c, t, i):
    corner_tag(c, 'E218 · 两排交错的圆刀')
    c.text(60, 96, '两根刀轴上套着一片片圆刀，像两排交错的剪刀：纸被咬进去，一刀刀剪成细条或碎片', 'serif', 36, INK)
    cx, cy = 800, 560
    for k in range(9):
        y = cy - 280 + k * 70
        c.rect(cx - 160, y, cx - 10, y + 30, fill=mix(BG, STEEL, 0.9), r=6)
        c.rect(cx + 10, y + 35, cx + 160, y + 65, fill=mix(BG, STEEL, 0.7), r=6)
    c.line([(cx - 85, cy - 300), (cx - 85, cy + 360)], INK, 6)
    c.line([(cx + 85, cy - 300), (cx + 85, cy + 360)], INK, 6)
    p = (t % 6) / 6
    c.rect(cx - 400, cy - 260, cx - 160 + 160 * p, cy + 320, fill=mix(BG, PAPERC, 0.9))
    for k in range(int(p * 8)):
        x = cx + 180 + k * 40
        for q in range(9):
            y = cy - 260 + q * 70
            c.rect(x, y + (q % 2) * 10, x + 30, y + 50, fill=mix(BG, PAPERC, 0.9))
    c.text(cx - 280, cy + 380, '整张纸', 'sans', 22, MUTED, 'mm')
    c.text(cx + 340, cy + 380, '碎纸条', 'sans', 22, MUTED, 'mm')
    c.rect(1380, 320, 1860, 560, fill=SHEET, r=12)
    c.text(1620, 370, '千万注意', 'bold', 26, NRED, 'mm')
    c.text(1620, 430, '刀不分纸和手指', 'sans', 22, INK, 'mm')
    c.text(1620, 480, '头发、领带、袖口都会被卷进去', 'sans', 22, INK, 'mm')
    c.text(1620, 530, '只由成年人操作', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '两根刀轴相对转动，把纸往中间卷'),
                (7.2, 14, '一片片圆刀上下交错，每两片之间就是一把剪刀'),
                (14.2, 22, '它分不清纸和手指：碎纸机只由成年人操作，手、头发远离进纸口')], y=1010)


# ---------------------------------------------------------------- E219 复印机
def e219_charge(c, t, i):
    corner_tag(c, '第 219 集 · 光把静电「擦」掉')
    c.text(60, 96, '感光鼓先整个带上静电；原件的白纸部分反射的光照到鼓上，那里的静电就跑掉；字是黑的不反光，那里的静电留着', 'serif', 33, INK)
    cx, cy = 760, 600
    R = 220
    ang = t * 0.6
    c.ellipse(cx, cy, R, R, fill=mix(BG, DRUM, 0.8))
    c.ellipse(cx, cy, 30, 30, fill=BG)
    letters = [0.0, 0.25, 0.55]
    for k in range(48):
        a = ang + k * 2 * math.pi / 48
        x, y = cx + (R - 24) * math.cos(a), cy + (R - 24) * math.sin(a)
        on_letter = any(abs(((a - ang) % (2 * math.pi)) - (l * 2 * math.pi)) < 0.12 for l in letters)
        lit = (math.sin(a) < -0.2)
        charged = on_letter or (math.cos(a) > 0 and not lit)
        if charged:
            c.text(x, y, '+', 'bold', 22, SPARK, 'mm')
    c.rect(cx - 360, cy - R - 160, cx + 360, cy - R - 110, fill=mix(BG, PAPERC, 0.9))
    for k in range(5):
        c.rect(cx - 300 + k * 140, cy - R - 150, cx - 260 + k * 140, cy - R - 120, fill=TONER)
    c.text(cx + 400, cy - R - 135, '原件', 'sans', 22, MUTED, 'lm')
    for k in range(5):
        x = cx - 280 + k * 140 + 70
        c.line([(x, cy - R - 110), (cx + (x - cx) * 0.5, cy - R + 20)], mix(BG, LIGHT, 0.7), 3)
    c.rect(1300, 320, 1860, 600, fill=SHEET, r=12)
    c.text(1580, 370, '鼓上的静电', 'bold', 26, INK, 'mm')
    c.text(1580, 440, '白纸部分：光照到，静电跑掉', 'sans', 22, INK, 'mm')
    c.text(1580, 490, '字的部分：没光，静电留着', 'sans', 22, SPARK, 'mm')
    c.text(1580, 550, '留下一张看不见的「静电字」', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '复印机里的感光鼓表面有一层特别的材料：黑暗里能存住静电，见光就导电'),
                (7.2, 14, '先让整个鼓带上静电，再把原件的影像照到鼓上'),
                (14.2, 22, '亮的地方静电跑光，暗的字留着静电：鼓上就有了一张看不见的「静电字」（示意）')], y=1010)


def e219_toner(c, t, i):
    corner_tag(c, 'E219 · 静电吸住墨粉，加热粘牢')
    c.text(60, 96, '干墨粉撒过去，只被带静电的「字」吸住；再把字压到纸上，用热辊一烫，墨粉熔化粘在纸里', 'serif', 36, INK)
    steps = [('1 吸墨粉', 0), ('2 转到纸上', 1), ('3 加热定影', 2)]
    st = min(2, int(t / 7))
    for k, (lab, _) in enumerate(steps):
        cx = 340 + k * 620
        on = k <= st
        c.rect(cx - 260, 300, cx + 260, 760, fill=SHEET if on else mix(BG, SHEET, 0.4), r=12)
        c.text(cx, 340, lab, 'bold', 26, INK if on else MUTED, 'mm')
        if not on:
            continue
        if k == 0:
            c.rect(cx - 200, 480, cx + 200, 520, fill=mix(BG, DRUM, 0.8))
            r = random.Random(2)
            for q in range(60):
                x = cx - 200 + r.uniform(0, 400)
                inletter = (int((x - cx + 200) / 40) % 2 == 0)
                y = 470 if inletter else 420 - r.uniform(0, 60)
                c.ellipse(x, y, 5, 5, fill=(190, 190, 200))
        elif k == 1:
            c.rect(cx - 200, 520, cx + 200, 560, fill=mix(BG, PAPERC, 0.9))
            for q in range(5):
                c.rect(cx - 200 + q * 80, 510, cx - 160 + q * 80, 520, fill=TONER)
            c.arrow(cx, 460, cx, 500, SPARK, 5, 14)
        else:
            c.rect(cx - 200, 520, cx + 200, 560, fill=mix(BG, PAPERC, 0.9))
            for q in range(5):
                c.rect(cx - 200 + q * 80, 520, cx - 160 + q * 80, 530, fill=TONER)
            c.ellipse(cx, 470, 60, 60, fill=mix(BG, (230, 120, 70), 0.9))
            c.text(cx, 640, '约 180 ℃ 热辊（示意）', 'sans', 20, NRED, 'mm')
    caps(c, t, [(0, 7, '带电的「字」把干干的墨粉吸过来，其他地方不吸'),
                (7.2, 14, '纸从下面经过，纸背后带上更强的静电，把墨粉从鼓上拉到纸上'),
                (14.2, 22, '热辊一压一烫，墨粉熔化粘进纸里，出来的复印件摸着还是热的（示意）')], y=1010)


# ---------------------------------------------------------------- E220 扫描仪
SHAPE = ["0001111000", "0011111100", "0111111110", "0011111100", "0111111110",
         "1111111111", "0001111000", "0000110000", "0000110000", "0000110000"]


def e220_rows(c, t, i):
    corner_tag(c, '第 220 集 · 一次只看一行')
    c.text(60, 96, '扫描仪里有一排很小的感光点，一次只「看」一条细线：记下这一行每一点是亮是暗，然后往下挪一点', 'serif', 36, INK)
    x0, y0, s = 200, 260, 56
    for r in range(10):
        for q in range(10):
            c.rect(x0 + q * s, y0 + r * s, x0 + q * s + s - 4, y0 + r * s + s - 4, fill=PIX if SHAPE[r][q] == '1' else mix(BG, PAPERC, 0.9))
    row = min(9, int(t / 1.6))
    c.line([(x0 - 20, y0 + row * s + s / 2), (x0 + 10 * s + 20, y0 + row * s + s / 2)], mix(BG, LIGHT, 1.0), 8)
    x1 = 1000
    for r in range(row + 1):
        bits = SHAPE[r]
        c.text(x1, y0 + r * s + s / 2, ' '.join('暗' if b == '1' else '亮' for b in bits), 'mono', 22, INK if r < row else SPARK, 'lm')
    c.text(x1, y0 - 30, '记下来的数据', 'bold', 24, MUTED, 'lm')
    caps(c, t, [(0, 7, '一道光照着原稿，一排感光点只看光照着的那一条细线'),
                (7.2, 14, '每个感光点记下自己看到的是亮还是暗，这一行就变成一串数字'),
                (14.2, 22, '灯和感光点一起往下挪一小步，再记一行，直到整页扫完（示意）')], y=1010)


def e220_pixels(c, t, i):
    corner_tag(c, 'E220 · 格子越细，图越清楚')
    c.text(60, 96, '把记下来的每一行拼起来，就是一张由小格子组成的图：格子越小、越多，拼出来的图越像原稿', 'serif', 36, INK)
    for j, (lab, n) in enumerate([('10 × 10 格', 10), ('20 × 20 格', 20), ('40 × 40 格', 40)]):
        cx, cy = 330 + j * 630, 540
        size = 420
        s = size / n
        a = fade(t, 1 + j * 5, 3 + j * 5)
        for r in range(n):
            for q in range(n):
                x = (q + 0.5) / n
                y = (r + 0.5) / n
                inside = ((x - 0.5) ** 2 + (y - 0.42) ** 2 < 0.09) or (0.45 < x < 0.55 and y > 0.6)
                col = PIX if inside else mix(BG, PAPERC, 0.9)
                c.rect(cx - size / 2 + q * s, cy - size / 2 + r * s, cx - size / 2 + (q + 1) * s - 1, cy - size / 2 + (r + 1) * s - 1, fill=mix(BG, col, a))
        c.text(cx, cy + 280, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '每个小格子叫一个像素，只记一个亮暗或颜色'),
                (7.2, 14, '格子少，拼出来是一块块的；格子多，边缘就越来越平滑'),
                (14.2, 22, '扫描仪说的「600 dpi」，就是每英寸要扫 600 个点（以资料为准）')], y=1010)


CLIPS = {
 'E218_减速': (e218_gearing, 22), 'E218_剪切': (e218_shear, 22),
 'E218_片头': (titles.opening(SER41, VOL41, S41A, 6, '20 世纪初出现碎纸机'), 7),
 'E218_片尾': (titles.closing(SER41, VOL41, S41A, 6, '下集：复印机没有墨水，怎么印出字？'), 7),
 'E219_静电': (e219_charge, 22), 'E219_墨粉': (e219_toner, 22),
 'E219_片头': (titles.opening(SER41, VOL41, S41A, 7, '1938 年卡尔森做出第一张静电复印'), 7),
 'E219_片尾': (titles.closing(SER41, VOL41, S41A, 7, '下集：扫描仪一行行扫，怎么变成一张图？'), 7),
 'E220_逐行': (e220_rows, 22), 'E220_像素': (e220_pixels, 22),
 'E220_片头': (titles.opening(SER41, VOL41, S41A, 8, '20 世纪 50 年代出现图像扫描仪'), 7),
 'E220_片尾': (titles.closing(SER41, VOL41, S41A, 8, '下集：电脑怎么知道你按了哪个键？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
