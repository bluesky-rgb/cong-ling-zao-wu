"""第四季收尾：E36 煤气中毒与通风、第四季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s4a import S4A, SER4, VOL4, GERM, GREEN

O2C = (111, 176, 222)
COC = (216, 75, 58)
CO2C = (151, 166, 171)
CARB = (60, 60, 64)
BLOOD = (170, 50, 50)

def mol(c, x, y, kind, a=1.0):
    """kind: 'O2' 'CO' 'CO2' 'C'"""
    if kind == 'O2':
        c.ellipse(x - 13, y, 15, 15, fill=mix(BG, O2C, a)); c.ellipse(x + 13, y, 15, 15, fill=mix(BG, O2C, a))
    elif kind == 'CO':
        c.ellipse(x - 13, y, 15, 15, fill=mix(BG, CARB, a), outline=mix(BG, COC, a), width=3)
        c.ellipse(x + 13, y, 15, 15, fill=mix(BG, O2C, a))
    elif kind == 'CO2':
        c.ellipse(x - 26, y, 14, 14, fill=mix(BG, O2C, a)); c.ellipse(x, y, 16, 16, fill=mix(BG, CARB, a), outline=mix(BG, CO2C, a), width=3)
        c.ellipse(x + 26, y, 14, 14, fill=mix(BG, O2C, a))
    else:
        c.ellipse(x, y, 16, 16, fill=mix(BG, CARB, a), outline=mix(BG, MUTED, a), width=2)

def coal(c, cx, cy):
    for k in range(7):
        x = cx - 120 + k * 40
        c.ellipse(x, cy + (k % 2) * 14, 30, 24, fill=(50, 46, 44))
        c.ellipse(x, cy + (k % 2) * 14 - 6, 18, 10, fill=(230, 110, 50))

R36 = random.Random(36)
PTS = [(R36.uniform(-1, 1), R36.uniform(0, 1), R36.uniform(0, 1)) for _ in range(18)]

# ---------------------------------------------------------------- E36
def e36_burn(c, t, i):
    corner_tag(c, '第 36 集 · 不完全燃烧')
    c.text(60, 96, '氧气够不够，烧出来的东西不一样', 'serif', 40, INK)
    for k, (cx, lab, ok) in enumerate([(500, '氧气充足', True), (1420, '门窗紧闭、氧气不足', False)]):
        a = fade(t, 0.5 + k * 6, 1.5 + k * 6)
        c.rect(cx - 380, 200, cx + 380, 820, fill=mix(BG, SHEET, a), r=18)
        c.text(cx, 250, lab, 'bold', 32, mix(BG, INK, a), 'mm')
        if a <= 0: continue
        coal(c, cx, 740)
        for j, (u, v, p) in enumerate(PTS):
            ph = (t * 0.3 + p) % 1
            x = cx + u * 300
            y = 700 - ph * 370
            if ok:
                kind = 'CO2' if j % 3 else 'O2'
            else:
                kind = 'CO' if j % 2 else ('CO2' if j % 4 == 0 else 'C')
            mol(c, x, y, kind, a)
        res = '二氧化碳：燃烧完全' if ok else '一氧化碳：只抢到一个氧'
        c.text(cx, 790, res, 'bold', 28, mix(BG, CO2C if ok else COC, a), 'mm')
    b = fade(t, 13, 14)
    for k, (kind, s) in enumerate([('O2', '氧气'), ('CO2', '二氧化碳'), ('CO', '一氧化碳：无色、无味')]):
        x = 300 + k * 520
        mol(c, x, 880, kind, b)
        c.text(x + 50, 880, s, 'sans', 26, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 6, '炭和煤烧起来，每个碳原子要抢两个氧原子，变成二氧化碳'),
                (6.2, 13, '门窗关紧，氧气不够，碳原子只抢到一个氧：变成一氧化碳'),
                (13.2, 22, '一氧化碳没有颜色、没有气味，屋里的人根本察觉不到')], y=1000)

def hb(c, x, y, seats, a=1.0):
    c.ellipse(x, y, 120, 90, fill=mix(BG, BLOOD, 0.8 * a))
    pos = [(-55, -40), (55, -40), (-55, 40), (55, 40)]
    for k, (dx, dy) in enumerate(pos):
        c.ellipse(x + dx, y + dy, 34, 26, fill=mix(BG, (235, 225, 225), a))
        if seats[k]:
            mol(c, x + dx, y + dy, seats[k], a)

def e36_hb(c, t, i):
    corner_tag(c, '第 36 集 · 抢座位')
    c.text(60, 96, '一氧化碳为什么这么危险？', 'serif', 40, INK)
    c.text(480, 210, '血红蛋白：运氧的「车」，每辆 4 个座位', 'sans', 26, MUTED, 'mm')
    p = fade(t, 6, 14)
    rows = 3
    for r in range(rows):
        for k in range(3):
            x, y = 260 + k * 330, 360 + r * 230
            n_co = int(round(p * 4 * (0.5 + 0.5 * ((r * 3 + k) % 3) / 2)))
            seats = ['CO' if j < n_co else 'O2' for j in range(4)]
            hb(c, x, y, seats)
    c.rect(1180, 240, 1860, 820, fill=SHEET, r=16)
    c.text(1210, 290, '一氧化碳抢座位的本事', 'bold', 28, INK, 'lm')
    c.text(1210, 340, '比氧气强两百多倍', 'bold', 34, COC, 'lm')
    c.text(1210, 410, '坐上去就不太下来', 'sans', 26, INK, 'lm')
    c.text(1210, 470, '「车」还在跑，却运不了氧', 'sans', 26, INK, 'lm')
    a = fade(t, 14, 15)
    c.text(1210, 560, '早期：头痛、头晕、恶心、犯困', 'sans', 26, mix(BG, SPARK, a), 'lm')
    c.text(1210, 610, '睡着的人往往来不及醒', 'sans', 26, mix(BG, NRED, a), 'lm')
    c.text(1210, 690, '开窗通风 · 装一氧化碳报警器', 'bold', 28, mix(BG, GREEN, fade(t, 17, 18)), 'lm')
    c.text(1210, 740, '有人头晕犯困：先开窗、离开、求救', 'sans', 24, mix(BG, INK, fade(t, 17, 18)), 'lm')
    caps(c, t, [(0, 6, '血液里的血红蛋白像一辆辆小车，每辆有 4 个座位，专门运氧'),
                (6.2, 14, '一氧化碳抢座位的本事比氧气强两百多倍，坐上去就不太下来'),
                (14.2, 22, '车还在跑，却运不了氧；人会头痛、犯困，睡着的人往往来不及醒')], y=1000)

# ---------------------------------------------------------------- 第四季特辑：看不见的敌人
GROUPS = [('病菌', '洗手 · 罐藏 · 种痘', '32 · 37 · 35', GERM),
          ('缺的东西', '维生素 C · 盐和水', '33 · 31', SPARK),
          ('毒物', '银钗验毒', 'B19', (205, 210, 216)),
          ('气体', '一氧化碳', '36', COC)]

def s4_enemies(c, t, i):
    corner_tag(c, '第四季特辑 · 看不见的敌人')
    c.text(60, 110, '第四季：看不见的敌人', 'serif', 48, INK, 'lm')
    for k, (name, eps, nums, col) in enumerate(GROUPS):
        cx = 580 + (k % 2) * 760
        cy = 330 + (k // 2) * 320
        a = fade(t, 1 + k * 4, 2 + k * 4)
        c.rect(cx - 330, cy - 120, cx + 330, cy + 150, fill=mix(BG, SHEET, a), outline=mix(BG, col, a), width=4, r=18)
        # icon
        if k == 0:
            for j in range(5): c.ellipse(cx - 230 + (j % 3) * 30, cy - 40 + (j // 3) * 34, 14, 10, fill=mix(BG, col, a))
        elif k == 1:
            c.ellipse(cx - 200, cy - 20, 40, 40, fill=mix(BG, (240, 160, 60), a))
        elif k == 2:
            c.ellipse(cx - 200, cy - 40, 22, 34, fill=mix(BG, col, a)); c.rect(cx - 206, cy - 10, cx - 194, cy + 60, fill=mix(BG, col, a))
        else:
            for j in range(4): c.ellipse(cx - 230 + j * 26, cy - 20 + (j % 2) * 20, 18, 18, fill=mix(BG, col, 0.6 * a))
        c.text(cx - 100, cy - 50, name, 'serif', 44, mix(BG, col, a), 'lm')
        c.text(cx - 100, cy + 20, eps, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(cx - 100, cy + 70, nums, 'mono', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 9, '第四季的七集，对付的都是看不见的东西：病菌，和身体缺的东西'),
                (9.2, 17, '还有毒物，和没有颜色、没有气味的气体'),
                (17.2, 28, '洗手、通风、吃点水果、喝对补液：最便宜的知识，救下的人最多')], y=1010)

CLIPS = {
 'E36_不完全燃烧': (e36_burn, 22), 'E36_抢座位': (e36_hb, 22),
 'E36_片头': (titles.opening(SER4, VOL4, S4A, 5, '北宋 · 汴京 · 家家烧煤'), 7),
 'E36_片尾': (titles.closing(SER4, VOL4, S4A, 5, '下集：第四季特辑'), 7),
 'S4_看不见的敌人': (s4_enemies, 28),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
