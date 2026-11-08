"""第三十二季（古法解密 13.0：天、凉、数、用）第一批：B130 圭表、B131 凉席、B132 竹夫人 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO

SB32 = [('B130', '圭表'), ('B131', '凉席'), ('B132', '竹夫人'), ('B133', '晒秋'), ('B134', '算筹'),
        ('B135', '结绳记事'), ('B136', '剪刀'), ('B137', '瓦片'), ('B138', '纸风车'), ('B139', '腰舟')]
VOL32 = '第三十二季 · 古法解密 13.0'
SUN = (250, 200, 80)
SHADOW = (70, 70, 80)
WARM = (230, 120, 80)
COOL = (110, 170, 230)
LAT = 35.0


def noon_alt(doy):
    dec = 23.44 * math.sin(2 * math.pi * (doy - 80) / 365)
    return 90 - LAT + dec


# ---------------------------------------------------------------- B130 圭表
def b130_day(c, t, i):
    corner_tag(c, 'B130 · 一天里，正午的影子最短')
    c.text(60, 96, '杆子竖直立在平地上：上午影子朝西偏北、慢慢变短，正午最短、指向正北，下午又慢慢变长', 'serif', 38, INK)
    h = (t / 22) * 8 + 8
    alt = max(5, 60 * math.sin(math.pi * (h - 6) / 12))
    az = (h - 12) * 15
    cx, cy = 760, 560
    c.ellipse(cx, cy, 400, 330, fill=mix(BG, (150, 130, 100), 0.25))
    L = min(310, 140 / math.tan(math.radians(alt)))
    sx = cx + L * math.sin(math.radians(az))
    sy = cy - L * math.cos(math.radians(az))
    c.line([(cx, cy), (sx, sy)], SHADOW, 12)
    c.ellipse(cx, cy, 14, 14, fill=WOOD)
    c.text(cx + 30, cy + 30, '杆子（从上往下看）', 'sans', 18, MUTED, 'lm')
    for hh in range(8, int(h) + 1):
        a2 = max(5, 60 * math.sin(math.pi * (hh - 6) / 12))
        z2 = (hh - 12) * 15
        L2 = min(310, 140 / math.tan(math.radians(a2)))
        c.ellipse(cx + L2 * math.sin(math.radians(z2)), cy - L2 * math.cos(math.radians(z2)), 6, 6, fill=SPARK)
    c.text(cx, cy - 360, '北', 'bold', 24, MUTED, 'mm')
    c.text(cx - 430, cy, '西', 'bold', 24, MUTED, 'mm')
    c.text(cx + 430, cy, '东', 'bold', 24, MUTED, 'mm')
    c.rect(1380, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 350, f'{int(h)}:{int((h % 1) * 60):02d}', 'mono', 40, INK, 'mm')
    c.text(1620, 440, f'影长 {L / 140:.2f} 米', 'mono', 30, SPARK, 'mm')
    c.text(1620, 520, '（杆高 1 米，示意）', 'sans', 18, MUTED, 'mm')
    c.text(1620, 590, '只看地上的影子，绝不看太阳', 'bold', 20, NRED, 'mm')
    caps(c, t, [(0, 7, '一根 1 米的杆子用铅垂线校直，立在平地上'),
                (7.2, 14, '太阳越高，影子越短：上午影子一点点缩短，橙点记下每个整点的影尖'),
                (14.2, 22, '正午太阳最高，影子最短、正指北方：古人就在这个时刻量影子（示意）')], y=1010)


def b130_year(c, t, i):
    corner_tag(c, 'B130 · 一年里，冬至的正午影子最长')
    c.text(60, 96, '每天正午量同一根杆子的影子：冬天影子长，夏天影子短；最长那天是冬至，两个冬至间就是一年', 'serif', 34, INK)
    x0, x1, y0 = 220, 1700, 860
    c.line([(x0, y0), (x1, y0)], LINE, 2)
    months = ['1 月', '2 月', '3 月', '4 月', '5 月', '6 月', '7 月', '8 月', '9 月', '10 月', '11 月', '12 月']
    for k, m in enumerate(months):
        c.text(x0 + (x1 - x0) * (k + 0.5) / 12, y0 + 30, m, 'sans', 18, MUTED, 'mm')
    n = int(min(365, t / 18 * 365))
    pts = []
    for d in range(0, n + 1, 3):
        L = 1 / math.tan(math.radians(noon_alt(d)))
        pts.append((x0 + (x1 - x0) * d / 365, y0 - L * 300))
    if len(pts) > 1:
        c.line(pts, SPARK, 4)
    for d, lab in ((172, '夏至'), (355, '冬至')):
        if n >= d:
            L = 1 / math.tan(math.radians(noon_alt(d)))
            x = x0 + (x1 - x0) * d / 365
            c.ellipse(x, y0 - L * 300, 10, 10, fill=NRED)
            c.text(x, y0 - L * 300 - 36, f'{lab} {L:.2f} 米', 'bold', 22, NRED, 'mm')
    c.text(1790, 300, '正午影长', 'sans', 20, MUTED, 'mm')
    c.text(960, 940, f'按北纬 {LAT:.0f}°、杆高 1 米估算（示意，以实测为准）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '每天正午，量同一根杆子的影子，画成一条线'),
                (7.2, 14, '夏至那天正午太阳最高，影子只有二十厘米左右；冬至太阳最低，影子长到一米半以上'),
                (14.2, 22, '从一个冬至到下一个冬至，古人数出一年约 365 又 1/4 天（按北纬 35° 估算）')], y=1010)


# ---------------------------------------------------------------- B131 凉席
MATS = [('金属盘', 50, (190, 195, 205)), ('竹席', 3.0, BAMBOO), ('木板', 1.2, WOOD), ('毛巾', 0.4, (220, 200, 210))]


def b131_flow(c, t, i):
    corner_tag(c, 'B131 · 一样的温度，带走热的快慢不一样')
    c.text(60, 96, '房间里这几样东西都是 26 ℃，手是 34 ℃：导热快的，把手上的热一下子带走，摸着就凉', 'serif', 38, INK)
    for k, (name, rel, col) in enumerate(MATS):
        x = 300 + k * 420
        c.rect(x - 150, 620, x + 150, 700, fill=mix(BG, col, 0.8), r=8)
        c.text(x, 740, name, 'bold', 26, INK, 'mm')
        c.text(x, 790, '26 ℃', 'mono', 22, MUTED, 'mm')
        c.ellipse(x, 560, 80, 40, fill=(225, 180, 150))
        n = int(2 + 6 * math.log10(1 + rel * 3))
        for j in range(n):
            u = ((t * (0.3 + 0.2 * math.log10(1 + rel))) + j / n) % 1
            c.ellipse(x - 50 + j * 100 / max(1, n - 1), 590 + u * 80, 6, 6, fill=mix(WARM, COOL, u))
        feel = '很凉' if rel > 10 else ('凉快' if rel > 2 else ('不太凉' if rel > 1 else '暖和'))
        c.text(x, 470, feel, 'bold', 28, COOL if rel > 2 else WARM, 'mm')
    c.text(960, 900, '红点：从手流进去的热（越多越快，越觉得凉，示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '用温度计一测：金属盘、竹席、木板、毛巾放了一小时，温度都一样'),
                (7.2, 14, '可手放上去感觉完全不同：手感觉的不是它的温度，而是热从手上流走得多快'),
                (14.2, 22, '竹子导热比毛巾、木头快，又不像金属凉得扎人：躺上去刚刚好凉快（示意）')], y=1010)


def b131_ice(c, t, i):
    corner_tag(c, 'B131 · 冰块放上去，哪块先化？')
    c.text(60, 96, '反过来试：同样的冰块放在四样东西上，导热快的把房间里的热送给冰块，冰块化得最快', 'serif', 38, INK)
    times = [3.5, 8, 11, 18]
    for k, (name, rel, col) in enumerate(MATS):
        x = 300 + k * 420
        c.rect(x - 150, 640, x + 150, 720, fill=mix(BG, col, 0.8), r=8)
        frac = max(0, 1 - t / times[k])
        s = 70 * frac ** 0.5
        if s > 2:
            c.rect(x - s, 640 - 2 * s, x + s, 640, fill=(200, 230, 250), outline=(160, 200, 230), width=2, r=6)
        c.ellipse(x, 646, 90 * (1 - frac) + 4, 10 * (1 - frac) + 2, fill=mix(BG, COOL, 0.5))
        c.text(x, 760, name, 'bold', 26, INK, 'mm')
        if frac == 0:
            c.text(x, 520, '化完了', 'bold', 26, SPARK, 'mm')
    c.text(960, 880, '先后顺序为示意，以实测为准', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '四块一样大的冰，同时放在金属盘、竹席、木板、毛巾上'),
                (7.2, 14, '金属盘上的冰化得飞快，毛巾上的冰几乎不动'),
                (14.2, 22, '导热越快，热越容易在它和你之间流来流去：凉席凉快，靠的就是这一点（顺序以实测为准）')], y=1010)


# ---------------------------------------------------------------- B132 竹夫人
def b132_cage(c, t, i):
    corner_tag(c, 'B132 · 空心的笼子，风能穿过去')
    c.text(60, 96, '抱着棉枕头，身上的热被棉花困住，越抱越热；竹夫人是空心的竹笼，热空气从缝里散出去，凉风再钻进来', 'serif', 38, INK)
    for k, (lab, cage) in enumerate((('棉枕头', False), ('竹夫人', True))):
        cx = 520 + k * 860
        c.text(cx, 230, lab, 'bold', 30, INK, 'mm')
        if cage:
            for j in range(9):
                x = cx - 220 + j * 55
                c.line([(x, 300), (x, 760)], BAMBOO, 8)
            for y in (300, 530, 760):
                c.ellipse(cx, y, 230, 30, outline=BAMBOO, width=6)
            for j in range(10):
                u = (t * 0.25 + j * 0.1) % 1
                c.ellipse(cx - 300 + u * 600, 380 + (j % 4) * 100, 7, 7, fill=mix(COOL, WARM, 0.2))
        else:
            c.rect(cx - 230, 300, cx + 230, 760, fill=mix(BG, (230, 225, 210), 0.9), r=60)
            for j in range(10):
                c.ellipse(cx - 150 + (j % 5) * 75, 400 + (j // 5) * 200 + 10 * math.sin(t * 2 + j), 8, 8, fill=WARM)
        temp = 34 - (4 * min(1, t / 14) if cage else -1.5 * min(1, t / 14))
        c.text(cx, 840, f'贴着身体那面约 {temp:.1f} ℃', 'mono', 24, COOL if cage else WARM, 'mm')
    c.text(960, 930, '温度为示意', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '夏夜里抱着一个棉枕头：棉花里全是不流动的空气，热散不出去'),
                (7.2, 14, '竹夫人是用竹篾编的空心长笼：竹篾本身导热快，中间又全是通道'),
                (14.2, 22, '热空气从笼缝里跑掉，凉一点的空气钻进来：抱着它，身上的热一直被带走（示意）')], y=1010)


def b132_curve(c, t, i):
    corner_tag(c, 'B132 · 两瓶温水，谁凉得快？')
    c.text(60, 96, '两瓶一样的 50 ℃ 温水：一瓶裹毛巾，一瓶套在纸条编的空心笼里，每 5 分钟测一次水温', 'serif', 38, INK)
    x0, y0, x1, y1 = 260, 260, 1500, 860
    c.line([(x0, y1), (x1, y1)], LINE, 2)
    c.line([(x0, y0), (x0, y1)], LINE, 2)
    for m in range(0, 31, 5):
        c.text(x0 + (x1 - x0) * m / 30, y1 + 30, f'{m}', 'mono', 18, MUTED, 'mm')
    for T in (25, 30, 35, 40, 45, 50):
        c.text(x0 - 30, y1 - (y1 - y0) * (T - 25) / 25, f'{T}', 'mono', 18, MUTED, 'mm')
    c.text((x0 + x1) / 2, y1 + 70, '分钟', 'sans', 20, MUTED, 'mm')
    c.text(x0, y0 - 30, '水温 ℃', 'sans', 20, MUTED, 'mm')
    tm = min(30, t / 18 * 30)
    for lab, k, col in (('裹毛巾', 0.010, WARM), ('空心笼', 0.028, COOL)):
        pts = []
        for j in range(int(tm * 2) + 1):
            m = j / 2
            T = 26 + 24 * math.exp(-k * m)
            pts.append((x0 + (x1 - x0) * m / 30, y1 - (y1 - y0) * (T - 25) / 25))
        if len(pts) > 1:
            c.line(pts, col, 5)
            c.text(pts[-1][0] + 20, pts[-1][1], f'{lab} {26 + 24 * math.exp(-k * tm):.1f} ℃', 'bold', 22, col, 'lm')
    c.text(1500, 230, '冷却快慢为示意，以实测为准', 'sans', 20, MUTED, 'rm')
    caps(c, t, [(0, 7, '两瓶温水一样热，一瓶外面裹两层毛巾，一瓶外面套着纸条编的空心笼'),
                (7.2, 14, '每 5 分钟测一次：裹毛巾的那瓶降得很慢，空心笼里的那瓶降得快得多'),
                (14.2, 22, '毛巾把热捂住，空心笼让热散走：竹夫人就是一个专门「散热」的抱枕（示意）')], y=1010)


CLIPS = {
 'B130_一天': (b130_day, 22), 'B130_一年': (b130_year, 22),
 'B130_片头': (titles.opening(BSER, VOL32, SB32, 0, '西周已用土圭测影'), 7),
 'B130_片尾': (titles.closing(BSER, VOL32, SB32, 0, '下集：温度一样，为什么凉席摸着就是凉？'), 7),
 'B131_导热': (b131_flow, 22), 'B131_冰块': (b131_ice, 22),
 'B131_片头': (titles.opening(BSER, VOL32, SB32, 1, '先秦已有竹席'), 7),
 'B131_片尾': (titles.closing(BSER, VOL32, SB32, 1, '下集：一个空心竹笼，为什么抱着比棉枕头凉快？'), 7),
 'B132_空心': (b132_cage, 22), 'B132_冷却': (b132_curve, 22),
 'B132_片头': (titles.opening(BSER, VOL32, SB32, 2, '宋代已有竹夫人'), 7),
 'B132_片尾': (titles.closing(BSER, VOL32, SB32, 2, '下集：秋天晒辣椒玉米，为什么要晒太阳还要常翻？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
