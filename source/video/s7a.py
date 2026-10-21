"""第七季第一批：E07 风车发电、E08 畜力与人力、E09 重力发电 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S7A = [('07', '风车'), ('08', '人力'), ('09', '重力'), ('12', '热电'), ('13', '压电'), ('14', '静电机'),
       ('10', '蒸汽'), ('19', '焦炭'), ('21', '玻璃'), ('51', '青霉素')]
SER7, VOL7 = '从零造物', '第七季 · 补全科技树'
AIR = (150, 190, 220)

# ---------------------------------------------------------------- E07 风车发电
def e07_cube(c, t, i):
    corner_tag(c, '第 07 集 · 风速的三次方')
    c.text(60, 96, '风速翻一倍，风能涨几倍？', 'serif', 40, INK)
    for k, (y0, v, lab) in enumerate([(300, 1, '风速 1 倍'), (650, 2, '风速 2 倍')]):
        a = fade(t, 0.5 + k * 6, 1.5 + k * 6)
        if a <= 0: continue
        c.text(120, y0 - 110, lab, 'bold', 30, mix(BG, INK, a), 'lm')
        # rotor disc
        rx = 1100
        c.ellipse(rx, y0, 18, 110, outline=mix(BG, MUTED, a), width=4)
        # air parcels moving: spacing = speed
        n = 6 * v
        for j in range(7):
            x = 160 + ((t * 120 * v + j * 1040 / 7) % 1040)
            if x > 1160 or x < 180: continue
            c.rect(x - 20, y0 - 60, x + 20, y0 + 60, fill=mix(BG, AIR, 0.5 * a), r=8)
        b = fade(t, 2 + k * 6, 3 + k * 6)
        c.text(1250, y0 - 50, f'每秒穿过的空气：×{v}', 'sans', 26, mix(BG, INK, b), 'lm')
        c.text(1250, y0, f'每千克空气的动能：×{v * v}', 'sans', 26, mix(BG, INK, b), 'lm')
        c.text(1250, y0 + 50, f'风的功率：×{v ** 3}', 'bold', 30, mix(BG, COPPER if v > 1 else INK, b), 'lm')
    d = fade(t, 15, 16)
    c.rect(360, 860, 1560, 960, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 910, '风的功率 ∝ 风速³：风速翻一倍，风能约涨 8 倍', 'serif', 32, mix(BG, SPARK, d), 'mm')
    caps(c, t, [(0, 6, '风吹过风车，带来的能量取决于两件事：每秒来多少空气，每千克空气跑多快'),
                (6.2, 15, '风速翻倍：来的空气多一倍，每千克的动能是四倍'),
                (15.2, 22, '两样相乘，就是八倍：风大一点点，电就多很多')], y=1035)

def e07_betz(c, t, i):
    corner_tag(c, '第 07 集 · 拿不走全部')
    c.text(60, 96, '风车能把风能全部变成电吗？', 'serif', 40, INK)
    rx, ry = 960, 520
    # streamtube widening behind rotor
    for j in range(7):
        off = (j - 3) * 50
        pts = []
        for k in range(0, 101):
            x = 200 + k * 15
            widen = 1.0 + 0.6 * (1 / (1 + math.exp(-(x - rx) / 80)))
            pts.append((x, ry + off * widen))
        seg(c, pts, mix(BG, AIR, 0.6), 2)
    for j in range(16):
        p = (t * 160 + j * 100) % 1500
        x = 200 + p if p < 760 else rx + (p - 760) * 0.45
        if x > 1700: continue
        widen = 1.0 + 0.6 * (1 / (1 + math.exp(-(x - rx) / 80)))
        c.ellipse(x, ry + (((j * 37) % 300) - 150) * widen, 7, 7, fill=AIR)
    c.ellipse(rx, ry, 22, 200, outline=COPPER, width=6)
    c.text(400, 260, '前面：风快', 'sans', 26, AIR, 'mm')
    c.text(1560, 260, '后面：风慢下来、散开', 'sans', 26, AIR, 'mm')
    a = fade(t, 8, 9)
    c.rect(300, 800, 1620, 950, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 845, '如果把风完全拦停，后面的空气就走不掉，前面的风也进不来', 'sans', 26, mix(BG, INK, a), 'mm')
    c.text(960, 905, '理论上最多只能拿走约 59%（贝茨极限）；实际风车还要更少', 'bold', 28, mix(BG, SPARK, a), 'mm')
    caps(c, t, [(0, 8, '风穿过风车，被拿走一部分能量，后面的风就变慢、散开'),
                (8.2, 15, '想把风能全拿走，就得把风完全拦停，可那样后面的空气就堵住了'),
                (15.2, 22, '所以风车永远只能拿走一部分：理论上限约 59%')], y=1035)

# ---------------------------------------------------------------- E08 畜力与人力
POWERS = [('LED 灯泡', 5, FIELD), ('人：持续骑车约 1 小时', 100, GREEN), ('白炽灯泡', 60, SPARK), ('一匹马（「马力」的定义）', 746, COPPER), ('电饭煲', 700, NRED)]

def e08_power(c, t, i):
    corner_tag(c, '第 08 集 · 功率')
    c.text(60, 96, '人能「发」多少瓦的电？', 'serif', 40, INK)
    order = [0, 2, 1, 4, 3]
    x0, y0, sc = 520, 230, 1.6
    for k, idx in enumerate(order):
        name, w, col = POWERS[idx]
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        y = y0 + k * 130
        L = w * sc * ease(a)
        c.text(x0 - 20, y + 30, name, 'bold', 26, mix(BG, INK, a), 'rm')
        if L > 1: c.rect(x0, y, x0 + L, y + 60, fill=mix(BG, col, 0.8), r=8)
        if a > 0.5: c.text(x0 + L + 16, y + 30, f'约 {w} 瓦', 'mono', 26, mix(BG, INK, a), 'lm')
    b = fade(t, 15, 16)
    c.rect(300, 880, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 920, '一个普通人拼命蹬，能点亮十几盏 LED，却带不动一个电饭煲（数字为示意，实测为准）', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '功率：每秒做多少功。一盏 LED 灯只要几瓦'),
                (6.2, 15, '一个普通人能持续输出的，大约一百瓦上下；一匹马，大约是人的好几倍'),
                (15.2, 22, '所以古人用牛马拉磨、用水车舂米：人的力气，实在太小了')], y=1010)

def e08_lenz(c, t, i):
    corner_tag(c, '第 08 集 · 越亮越难蹬')
    c.text(60, 96, '接的灯越多，为什么蹬起来越吃力？', 'serif', 40, INK)
    n = 0 if t < 4 else (1 if t < 9 else 3)
    cx, cy = 520, 560
    c.ellipse(cx, cy, 200, 200, outline=MUTED, width=10)
    ang = t * (3.0 - 0.6 * n)
    for k in range(8):
        a_ = ang + k * math.pi / 4
        c.line([(cx, cy), (cx + 190 * math.cos(a_), cy + 190 * math.sin(a_))], MUTED, 3)
    c.text(cx, cy + 260, '脚踏发电机', 'bold', 28, INK, 'mm')
    for k in range(3):
        x = 1100 + k * 220
        on = k < n
        c.ellipse(x, 420, 60, 60, fill=SPARK if on else LINE)
        c.rect(x - 24, 480, x + 24, 530, fill=MUTED, r=4)
    c.text(1320, 600, f'接了 {n} 盏灯', 'bold', 30, INK, 'mm')
    # resistance bar
    c.text(1100, 700, '蹬起来的阻力', 'sans', 26, MUTED, 'lm')
    c.rect(1100, 730, 1700, 770, fill=LINE, r=20)
    c.rect(1100, 730, 1100 + 80 + 170 * n, 770, fill=NRED, r=20)
    if n:
        c.arrow(cx + 230, cy - 120, cx + 230, cy + 60, mix(BG, NRED, 0.9), 6, 18)
        c.text(cx, cy - 250, '线圈里的电流反过来「拖」着轮子', 'sans', 26, NRED, 'mm')
    caps(c, t, [(0, 4, '不接灯，空蹬很轻松'),
                (4.2, 9, '接上一盏灯，马上变沉：电流在发电机里产生一个反向的「拖」'),
                (9.2, 22, '灯越多、越亮，拖得越狠：每一瓦电，都是你腿上的一瓦力气（第 05 集的楞次定律）')], y=1010)

# ---------------------------------------------------------------- E09 重力发电
def e09_energy(c, t, i):
    corner_tag(c, '第 09 集 · 势能')
    c.text(60, 96, '把一袋石头举高，存下了多少能量？', 'serif', 40, INK)
    m, h = 10, 2
    E = m * 9.8 * h
    drop = fade(t, 3, 10)
    x = 600
    top, bot = 250, 250 + 520
    y = top + (bot - top) * drop
    c.line([(x - 200, bot + 60), (x + 200, bot + 60)], MUTED, 4)
    c.line([(x + 140, top - 30), (x + 140, bot + 60)], MUTED, 2)
    c.text(x + 160, (top + bot) / 2, '2 米', 'mono', 28, MUTED, 'lm')
    c.rect(x - 70, y - 60, x + 70, y + 60, fill=(120, 110, 100), r=12)
    c.text(x, y, '10 千克', 'bold', 26, INK, 'mm')
    c.line([(x, 160), (x, y - 60)], (200, 200, 205), 3)
    a = fade(t, 2, 3)
    c.rect(1100, 240, 1860, 560, fill=mix(BG, SHEET, a), r=14)
    c.text(1130, 290, '势能 = 重量 × 高度', 'serif', 32, mix(BG, SPARK, a), 'lm')
    c.text(1130, 350, f'10 千克 × 9.8 × 2 米 ≈ {E:.0f} 焦耳', 'mono', 28, mix(BG, INK, a), 'lm')
    c.text(1130, 410, f'够一盏 1 瓦的 LED 亮约 {E / 60:.1f} 分钟', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1130, 460, '（再打个折：传动和发电都有损耗）', 'sans', 22, mix(BG, MUTED, a), 'lm')
    b = fade(t, 12, 13)
    c.rect(1100, 600, 1860, 880, fill=mix(BG, SHEET, b), r=14)
    c.text(1130, 650, '充满一部手机约 15 瓦时 ≈ 5.5 万焦耳', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1130, 710, '相当于把这袋石头举到', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1130, 780, '约 550 米高', 'bold', 44, mix(BG, NRED, b), 'lm')
    caps(c, t, [(0, 10, '把 10 千克举高 2 米，存下大约 200 焦耳；让它慢慢落下，就能带发电机发电'),
                (10.2, 16, '听起来不少？够一盏 1 瓦的灯亮三分钟左右'),
                (16.2, 22, '要充满一部手机，得把它举到五百多米高：重力储能，能量密度很低')], y=1010)

def e09_gear(c, t, i):
    corner_tag(c, '第 09 集 · 让它慢慢落')
    c.text(60, 96, '同样的能量，落得快和落得慢有什么不同？', 'serif', 40, INK)
    for k, (cx, lab, dur, col) in enumerate([(520, '直接落下：约 0.6 秒', 0.64, NRED), (1400, '齿轮减速：约 3 分钟', 180.0, GREEN)]):
        a = fade(t, 0.5 + k * 5, 1.5 + k * 5)
        if a <= 0: continue
        tt = max(0, t - (1.5 + k * 5))
        f = min(1, tt / dur) if k == 0 else min(1, tt / 60)
        top, bot = 260, 700
        y = top + (bot - top) * f
        c.line([(cx, 200), (cx, y - 50)], mix(BG, (200, 200, 205), a), 3)
        c.rect(cx - 60, y - 50, cx + 60, y + 50, fill=mix(BG, (120, 110, 100), a), r=10)
        c.text(cx, 790, lab, 'bold', 30, mix(BG, col, a), 'mm')
        P = 196 / dur
        c.text(cx, 840, f'功率 ≈ {P:.0f} 瓦' if P >= 1 else f'功率 ≈ {P:.1f} 瓦', 'mono', 30, mix(BG, INK, a), 'mm')
        if k == 1:
            c.ellipse(cx + 150, 230, 50, 50, outline=mix(BG, MUTED, a), width=5)
            c.ellipse(cx + 230, 230, 22, 22, outline=mix(BG, MUTED, a), width=5)
            c.ellipse(cx + 300, 330, 40, 40, fill=mix(BG, SPARK, a * (0.5 + 0.5 * math.sin(t * 8))))
            c.text(cx + 300, 400, '灯一直亮着', 'sans', 24, mix(BG, SPARK, a), 'mm')
    b = fade(t, 13, 14)
    c.text(960, 940, '功率 = 能量 ÷ 时间：落得越慢，功率越小，灯却能亮得越久', 'serif', 30, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 5, '同样 200 焦耳：一松手直接掉下去，零点几秒就没了'),
                (5.2, 13, '用齿轮让它慢慢落，几分钟才落到底：功率很小，但正好点亮一盏小灯'),
                (13.2, 22, '摆钟的重锤、老式的自鸣钟，都是这样「慢慢花」重力势能')], y=1010)

CLIPS = {
 'E07_三次方': (e07_cube, 22), 'E07_贝茨极限': (e07_betz, 22),
 'E07_片头': (titles.opening(SER7, VOL7, S7A, 0, '穿越北宋 · 把风接到发电机上'), 7),
 'E07_片尾': (titles.closing(SER7, VOL7, S7A, 0, '下集：点亮一盏灯，人要蹬多累？'), 7),
 'E08_功率': (e08_power, 22), 'E08_越亮越难蹬': (e08_lenz, 22),
 'E08_片头': (titles.opening(SER7, VOL7, S7A, 1, '穿越北宋 · 人力、牛马和水车'), 7),
 'E08_片尾': (titles.closing(SER7, VOL7, S7A, 1, '下集：一袋石头落下，灯能亮多久？'), 7),
 'E09_势能': (e09_energy, 22), 'E09_慢慢落': (e09_gear, 22),
 'E09_片头': (titles.opening(SER7, VOL7, S7A, 2, '穿越北宋 · 把力气「存」起来'), 7),
 'E09_片尾': (titles.closing(SER7, VOL7, S7A, 2, '下集：金属一头烧热，为什么就有电压？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
