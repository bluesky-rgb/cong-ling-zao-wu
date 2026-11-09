"""第三十四季（古法解密 14.0）第三批：B146 地窖、B147 耧车、B148 装裱 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s34a import SB34, VOL34, SAND, CLAY

SOIL = (120, 90, 60)
HOT = (230, 110, 80)
COLD = (110, 170, 230)
RICE = (240, 235, 215)
PAPER = (235, 232, 222)


def _tcol(v):
    return mix(COLD, HOT, max(0, min(1, (v + 1) / 2)))


# ---------------------------------------------------------------- B146 地窖
def b146_layers(c, t, i):
    corner_tag(c, 'B146 · 越深，冷热传得越慢越弱')
    c.text(60, 96, '地面一年里忽冷忽热，这个变化往土里传：越往下越弱、越晚到，几米深处几乎一年都一样', 'serif', 36, INK)
    x0, x1, gy = 160, 1180, 300
    ph = t / 22 * 2 * math.pi
    for k in range(30):
        d = k / 29
        amp = math.exp(-d * 3.2)
        v = amp * math.sin(ph - d * 3.2)
        y = gy + k * 20
        c.rect(x0, y, x1, y + 20, fill=mix(BG, _tcol(v), 0.35 + 0.5 * (1 - d * 0.5)))
    c.rect(x0, gy - 12, x1, gy, fill=mix(BG, _tcol(math.sin(ph)), 0.9))
    sky = '夏' if math.sin(ph) > 0.3 else ('冬' if math.sin(ph) < -0.3 else '春秋')
    c.text(x0 + 60, gy - 50, f'地面：{sky}', 'bold', 28, _tcol(math.sin(ph)), 'lm')
    c.rect(820, gy + 330, 940, gy + 420, fill=mix(BG, SOIL, 0.4), outline=INK, width=3, r=6)
    c.text(880, gy + 375, '菜窖', 'bold', 22, INK, 'mm')
    c.line([(880, gy), (880, gy + 330)], MUTED, 3)
    for k, lab in [(0, '0 米'), (10, '1 米'), (20, '2 米'), (29, '3 米')]:
        c.text(x0 - 20, gy + k * 20 + 10, lab, 'mono', 20, MUTED, 'rm')
    gx0, gx1 = 1300, 1840
    c.rect(1260, 260, 1870, 900, fill=SHEET, r=14)
    c.text(1565, 295, '一年里的温度（示意）', 'sans', 22, MUTED, 'mm')
    for j, (d, lab, col) in enumerate([(0, '地面', HOT), (0.33, '1 米深', SPARK), (1.0, '3 米深', GREEN)]):
        amp = math.exp(-d * 3.2)
        pts = [(gx0 + (gx1 - gx0) * s / 60, 580 - 220 * amp * math.sin(2 * math.pi * s / 60 - d * 3.2)) for s in range(61)]
        c.line(pts, col, 3)
        c.text(gx0 + 10, 360 + j * 34, lab, 'bold', 20, col, 'lm')
    cx = gx0 + (gx1 - gx0) * ((t / 22) % 1)
    c.line([(cx, 330), (cx, 840)], MUTED, 1)
    c.text(1565, 870, '一月 → 十二月', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '夏天地面晒得发烫，冬天冻得结冰，冷热一层层往土里传'),
                (7.2, 14, '土传热又慢又差，每往下一层，变化就弱一点、晚一点'),
                (14.2, 22, '到了几米深，冬天不冻、夏天不热：菜窖就挖在这里（示意）')], y=1010)


def b146_daily(c, t, i):
    corner_tag(c, 'B146 · 花盆里的一天')
    c.text(60, 96, '深花盆装湿沙土：外面的空气、2 厘米深、15 厘米深各放一支温度计，从早 8 点读到晚 8 点', 'serif', 36, INK)
    c.poly([(220, 320), (620, 320), (580, 880), (260, 880)], mix(BG, CLAY, 0.8))
    c.rect(235, 330, 605, 360, fill=mix(BG, SAND, 0.8))
    for j, (y, lab, col) in enumerate([(250, '空气', HOT), (380, '2 厘米', SPARK), (640, '15 厘米', GREEN)]):
        c.line([(420 + (j - 1) * 80, y - 70), (420 + (j - 1) * 80, y)], INK, 6)
        c.ellipse(420 + (j - 1) * 80, y, 12, 12, fill=col)
        c.text(660, y, lab, 'bold', 22, col, 'lm')
    gx0, gx1, gy0, gy1 = 900, 1820, 860, 300
    c.rect(860, 260, 1870, 920, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    p = min(1.0, t / 16)
    curves = [(HOT, 12, 0), (SPARK, 7, 0.6), (GREEN, 1.5, 2.2)]
    for col, amp, lag in curves:
        pts = []
        for s in range(int(60 * p) + 1):
            h = 8 + 12 * s / 60
            v = 20 + amp * math.sin((h - 9 - lag) / 24 * 2 * math.pi * 1.6)
            pts.append((gx0 + (gx1 - gx0) * s / 60, gy0 - (v - 5) * 22))
        if len(pts) > 1:
            c.line(pts, col, 4)
    for k, h in enumerate([8, 12, 16, 20]):
        c.text(gx0 + (gx1 - gx0) * (h - 8) / 12, gy0 + 28, f'{h}:00', 'mono', 18, MUTED, 'mm')
    c.text(gx0 + 20, gy1 + 10, '温度（示意）', 'sans', 20, MUTED, 'lm')
    if t > 16:
        c.text(1360, 330, '越深，曲线越平、峰值越晚', 'bold', 26, INK, 'mm')
    c.text(1360, 950, '以实测为准', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '中午太阳一晒，空气那支温度计一路往上蹿，傍晚又落下来'),
                (7.2, 14, '2 厘米深的跟着变，可变得小一点、慢一点'),
                (14.2, 22, '15 厘米深的那条线几乎是平的：薄薄一层土，就挡住了大半冷热（示意）')], y=1010)


# ---------------------------------------------------------------- B147 耧车
RNG = random.Random(147)
HAND = [RNG.gauss(0, 1) for _ in range(400)]


def b147_flow(c, t, i):
    corner_tag(c, 'B147 · 一样大的孔，流得一样快')
    c.text(60, 96, '瓶底三个一样大的小孔：米粒从孔里流出的快慢几乎不变，人走得匀，每一段地落下的就一样多', 'serif', 36, INK)
    gy = 820
    c.rect(100, gy, 1820, gy + 60, fill=mix(BG, PAPER, 0.6))
    for k in range(18):
        x = 100 + k * 95
        c.line([(x, gy), (x, gy + 60)], MUTED, 1)
    bx = 200 + (t / 22) * 1500
    c.rect(bx - 90, 380, bx + 90, 640, fill=mix(BG, (200, 220, 230), 0.35), outline=MUTED, width=3, r=20)
    c.rect(bx - 86, 470, bx + 86, 636, fill=mix(BG, RICE, 0.55), r=16)
    for k in range(3):
        hx = bx - 60 + k * 60
        c.ellipse(hx, 642, 6, 4, fill=BG)
        for j in range(5):
            f = ((t * 3 + j / 5 + k * 0.13) % 1)
            c.ellipse(hx - f * 25, 650 + f * (gy - 650), 4, 6, fill=RICE)
    r = random.Random(1)
    for s in range(int((bx - 200) / 6)):
        for k in range(3):
            x = 200 + s * 6 - 60 + k * 60 + r.uniform(-8, 8) - 25
            if x < 120: continue
            c.ellipse(x, gy + 30 + r.uniform(-20, 20), 3, 2, fill=RICE)
    c.arrow(bx + 120, 500, bx + 220, 500, SPARK, 4, 14)
    c.text(bx + 170, 470, '匀速走', 'sans', 22, SPARK, 'mm')
    c.text(960, 300, '颗粒从小孔流出：快慢只看孔多大，几乎和瓶里装多少米无关（示意）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '成年人在瓶底扎三个一样大的小孔，瓶里装半瓶大米（实验后不吃）'),
                (7.2, 14, '米粒挤在小孔上方，一粒粒稳稳地往下漏，快慢差不多不变'),
                (14.2, 22, '提着瓶子匀速走过纸条，每一格落下的米差不多一样多，排成三条直线（示意）')], y=1010)


def b147_rows(c, t, i):
    corner_tag(c, 'B147 · 手撒成堆，耧车撒成线')
    c.text(60, 96, '同一条两米长的纸，手抓着撒一遍，瓶子漏一遍：数每 10 厘米一格里有几粒米', 'serif', 36, INK)
    p = min(1.0, t / 12)
    for row, (lab, y0) in enumerate([('手撒', 290), ('耧车（漏瓶）', 620)]):
        c.text(110, y0 - 30, lab, 'bold', 26, INK, 'lm')
        c.rect(100, y0, 1820, y0 + 120, fill=mix(BG, PAPER, 0.55))
        for k in range(21):
            c.line([(100 + k * 86, y0), (100 + k * 86, y0 + 120)], MUTED, 1)
        r = random.Random(row + 3)
        counts = [0] * 20
        n = int(400 * p)
        for j in range(n):
            if row == 0:
                g = (j // 40)
                x = 100 + (g * 172 + 129 + HAND[j] * 25) % 1720
            else:
                x = 100 + (j / 400) * 1720
            yy = y0 + 60 + (r.gauss(0, 30) if row == 0 else (j % 3 - 1) * 35 + r.uniform(-4, 4))
            yy = max(y0 + 6, min(y0 + 114, yy))
            c.ellipse(x, yy, 3, 2, fill=RICE)
            idx = int((x - 100) / 86)
            if 0 <= idx < 20: counts[idx] += 1
        if p >= 1:
            for k, v in enumerate(counts):
                h = v * 2.4
                c.rect(110 + k * 86, y0 + 230 - h, 176 + k * 86, y0 + 230, fill=mix(BG, (FIELD if row else NRED), 0.8))
    c.text(960, 940, '下面的小柱子：每一格里有几粒（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '手一把一把地撒，抓得多少不一样、甩得远近也不一样'),
                (7.2, 14, '漏瓶匀速走一遍，米粒一粒一粒落成三条细线'),
                (14.2, 22, '数一数：手撒的格子有的几十粒、有的几粒；漏瓶每格都差不多（示意）')], y=1010)


# ---------------------------------------------------------------- B148 装裱
def _strip(c, x0, y0, L, curv, col, w=14):
    pts = []
    if abs(curv) < 1e-4:
        pts = [(x0 + L * s / 30, y0) for s in range(31)]
    else:
        R = 1 / curv
        for s in range(31):
            a = L * s / 30 / R
            pts.append((x0 + R * math.sin(a), y0 - R * (1 - math.cos(a))))
    c.line(pts, col, w)
    return pts[-1]


def b148_curl(c, t, i):
    corner_tag(c, 'B148 · 一面胀、一面不胀，纸就弯')
    c.text(60, 96, '放大纸的剖面：刷了水的一面纤维吸水胀长，另一面没变，整张纸就往干的那面卷', 'serif', 36, INK)
    p = fade(t, 2, 12)
    x0, y0 = 160, 560
    n = 12
    for k in range(n):
        y = y0 - 140 + k * 24
        wet = k < 6
        L = 900 * (1 + (0.08 * p if wet else 0))
        c.rect(x0, y, x0 + L, y + 16, fill=mix(BG, mix(PAPER, WATER_L, p * 0.6) if wet else PAPER, 0.75), r=8)
    c.text(x0 + 960 + 20, y0 - 80, '刷水的一面：纤维胀长', 'bold', 22, WATER_L, 'lm')
    c.text(x0 + 900 + 20, y0 + 110, '干的一面：不变', 'bold', 22, MUTED, 'lm')
    c.rect(1240, 600, 1860, 930, fill=SHEET, r=14)
    c.text(1550, 630, '整条纸条（侧面看）', 'sans', 22, MUTED, 'mm')
    _strip(c, 1330, 890, 380, 0.0022 * p, mix(PAPER, WATER_L, 0.3 * p), 8)
    if p > 0.6:
        c.text(1550, 670, '往干的一面卷起来', 'bold', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '纸是千千万万根植物纤维压在一起，纤维一吸水就变粗、变长'),
                (7.2, 14, '只刷一面，那一面的纤维胀长了，另一面还是原来的长度'),
                (14.2, 22, '一面长一面短，纸只能弯过去：就像双金属片受热弯曲（示意）')], y=1010)


def b148_backing(c, t, i):
    corner_tag(c, 'B148 · 两面一起胀缩，就不卷')
    c.text(60, 96, '四张纸条：不刷水、只刷一面、背面贴一层纸再刷、两面都刷；量刷完和晾干后翘起多高', 'serif', 36, INK)
    p = fade(t, 2, 10)
    dry = fade(t, 13, 17)
    rows = [('① 不刷水', 0, 0), ('② 只刷一面', 1.0, 0.6), ('③ 背面贴纸再刷', 0.25, 0.1), ('④ 两面都刷', 0.08, 0.15)]
    for k, (lab, wet_c, dry_c) in enumerate(rows):
        y = 300 + k * 160
        c.rect(120, y - 60, 1200, y + 80, fill=SHEET, r=12)
        c.text(150, y - 30, lab, 'bold', 24, INK, 'lm')
        cv = (wet_c * p * (1 - dry) + dry_c * dry) * 0.0016
        end = _strip(c, 560, y + 50, 420, cv, PAPER if k == 0 else mix(PAPER, WATER_L, 0.4 * (1 - dry)), 8)
        if k == 2:
            _strip(c, 560, y + 58, 420, cv, mix(BG, (200, 190, 170), 0.9), 6)
        c.text(1170, y - 30, f'翘起 {(y + 50 - end[1]) / 4:.0f} 毫米', 'mono', 22, SPARK, 'rm')
    c.rect(1280, 300, 1860, 820, fill=SHEET, r=14)
    c.text(1570, 340, '刷完 → 晾干', 'bold', 26, INK, 'mm') if dry < 0.5 else c.text(1570, 340, '晾干以后', 'bold', 26, INK, 'mm')
    for j, s in enumerate(['只刷一面的卷得最厉害', '晾干后也回不平', '背面糊了纸的几乎不卷', '这就是装裱：在画背后', '一层层托上纸']):
        c.text(1320, 410 + j * 70, s, 'sans', 24, INK, 'lm')
    c.text(1570, 790, '翘起高度以实测为准', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '四张一样的纸条，按四种办法处理，平放在桌上'),
                (7.2, 14, '只刷一面的立刻卷成一个弧；背面糊了一层纸的，两层互相拽着，几乎不动'),
                (14.2, 22, '晾干后，只刷一面的留下了波浪；装裱就是在画背后托纸，让两面一起胀缩（示意）')], y=1010)


CLIPS = {
 'B146_深浅': (b146_layers, 22), 'B146_一天': (b146_daily, 22),
 'B146_片头': (titles.opening(BSER, VOL34, SB34, 6, '北方农村冬天用菜窖存菜'), 7),
 'B146_片尾': (titles.closing(BSER, VOL34, SB34, 6, '下集：手撒种子成堆，耧车为什么撒得又匀又直？'), 7),
 'B147_流量': (b147_flow, 22), 'B147_撒种': (b147_rows, 22),
 'B147_片头': (titles.opening(BSER, VOL34, SB34, 7, '西汉赵过推广三脚耧'), 7),
 'B147_片尾': (titles.closing(BSER, VOL34, SB34, 7, '下集：薄纸刷水就卷，背后糊一层为什么就平了？'), 7),
 'B148_卷曲': (b148_curl, 22), 'B148_托纸': (b148_backing, 22),
 'B148_片头': (titles.opening(BSER, VOL34, SB34, 8, '晋唐以来书画就要装裱'), 7),
 'B148_片尾': (titles.closing(BSER, VOL34, SB34, 8, '下集：油在碗底，火在灯芯顶，油怎么爬上去的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
