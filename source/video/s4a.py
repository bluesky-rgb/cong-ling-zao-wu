"""第四季第一批：E32 洗手、E33 防坏血病、B19 银钗验毒 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL

S4A = [('32', '洗手'), ('33', '坏血病'), ('37', '罐藏'), ('31', '口服补液'), ('35', '种痘'), ('36', '煤气中毒')]
SB4 = [('B19', '银钗验毒')]
SER4, VOL4 = '从零造物', '第四季 · 救命的知识'

SKIN = (214, 170, 140)
GERM = (120, 200, 110)
OIL = (230, 200, 90)
GREEN = (110, 190, 110)
SILVER = (205, 210, 216)
TARN = (60, 56, 60)

# ---------------------------------------------------------------- E32 洗手
ANNUAL = [('1841', 7.8), ('1842', 15.8), ('1843', 9.0), ('1844', 8.2), ('1845', 6.9), ('1846', 11.4)]
MONTH = [('1847.4', 18.3), ('6 月', 2.2), ('7 月', 1.2), ('8 月', 1.9)]

def e32_rates(c, t, i):
    corner_tag(c, '第 32 集 · 维也纳第一产科')
    c.text(60, 96, '医生洗了手，产妇的死亡率发生了什么？', 'serif', 40, INK)
    x0, y1, sc = 200, 820, 26          # 1% = 26 px
    for p in (0, 5, 10, 15, 20):
        y = y1 - p * sc
        c.line([(x0 - 20, y), (1800, y)], LINE, 2)
        c.text(x0 - 30, y, f'{p}%', 'mono', 22, MUTED, 'rm')
    bars = ANNUAL + [None] + MONTH
    for k, b in enumerate(bars):
        if b is None: continue
        lab, v = b
        x = x0 + 40 + k * 145
        a = fade(t, 0.5 + k * 0.6, 1.3 + k * 0.6)
        after = k > len(ANNUAL) + 1
        col = FIELD if after else NRED
        h = v * sc * ease(a)
        if h > 1: c.rect(x, y1 - h, x + 90, y1, fill=mix(BG, col, 0.85), r=6)
        c.text(x + 45, y1 + 34, lab, 'mono', 22, mix(BG, MUTED, a), 'mm')
        if a > 0.6: c.text(x + 45, y1 - h - 24, f'{v}%', 'mono', 22, mix(BG, INK, a), 'mm')
    c.text(x0 + 40 + 2.5 * 145, y1 + 80, '1841–1846 年 · 每年', 'sans', 24, MUTED, 'mm')
    c.text(x0 + 40 + 8.5 * 145, y1 + 80, '1847 年 · 每月', 'sans', 24, MUTED, 'mm')
    a = fade(t, 5.5, 6.5)
    xl = x0 + 40 + 7.85 * 145
    c.line([(xl, 230), (xl, y1)], mix(BG, SPARK, a), 4)
    c.text(xl + 16, 250, '5 月中旬：进产房前', 'bold', 26, mix(BG, SPARK, a), 'lm')
    c.text(xl + 16, 290, '先用漂白粉溶液洗手', 'bold', 26, mix(BG, SPARK, a), 'lm')
    caps(c, t, [(0, 5.5, '维也纳总医院第一产科：每年约有十分之一的产妇死于产褥热'),
                (5.7, 12, '1847 年 5 月，塞麦尔维斯要求医生进产房前先洗手'),
                (12.2, 22, '一个月后，死亡率从 18.3% 掉到 2.2%（数据：维基百科转引塞麦尔维斯的统计）')])

RG = random.Random(32)
SKIN_Y = 700
GERMS = [(260 + k * 175 + RG.uniform(-25, 25), RG.uniform(0, 1)) for k in range(9)]

def e32_soap(c, t, i):
    corner_tag(c, '第 32 集 · 肥皂')
    c.text(60, 96, '光用水冲，为什么冲不掉？', 'serif', 40, INK)
    # skin with grooves
    pts = [(x, SKIN_Y + 18 * math.sin(x / 70)) for x in range(120, 1801, 20)]
    c.poly(pts + [(1800, 1000), (120, 1000)], mix(BG, SKIN, 0.75))
    c.text(150, 950, '皮肤（放大示意）', 'sans', 24, BG, 'lm')
    soap = fade(t, 6, 8)
    lift = fade(t, 12, 17)
    rinse = fade(t, 17, 20)
    # oil film with germs
    for k, (gx, ph) in enumerate(GERMS):
        base = SKIN_Y + 18 * math.sin(gx / 70) - 26
        dy = -lift * (180 + 40 * ph)
        dx = rinse * 900
        cx, cy = gx + dx, base + dy
        if cx > 1900: continue
        c.ellipse(cx, cy, 70, 30, fill=mix(BG, OIL, 0.55))
        c.ellipse(cx, cy, 20, 13, fill=GERM)
        c.ellipse(cx - 8, cy - 3, 4, 4, fill=mix(GERM, BG, 0.5))
        if soap > 0:
            # surfactant molecules around droplet: tail into oil, head outward
            n = 10
            for j in range(n):
                ang = 2 * math.pi * j / n
                ex, ey = cx + 70 * math.cos(ang), cy + 30 * math.sin(ang)
                ox, oy = cx + 104 * math.cos(ang), cy + 54 * math.sin(ang)
                ax, ay = ox + (ex - ox) * soap, oy + (ey - oy) * soap
                c.line([(ax, ay), (ax + 26 * math.cos(ang), ay + 20 * math.sin(ang))], mix(BG, MUTED, soap), 3)
                c.ellipse(ax + 30 * math.cos(ang), ay + 23 * math.sin(ang), 9, 9, fill=mix(BG, FIELD, soap))
    # water
    if t < 6:
        for k in range(8):
            ph = (t * 0.8 + k / 8) % 1
            c.ellipse(200 + k * 210, 300 + ph * 300, 10, 16, fill=mix(BG, FIELD, 0.6))
        c.text(960, 260, '水和油不相溶：水从油膜上滑过去', 'sans', 28, FIELD, 'mm')
    if 8 < t < 17:
        c.text(1500, 230, '肥皂分子', 'bold', 28, INK, 'lm')
        c.ellipse(1530, 290, 11, 11, fill=FIELD); c.line([(1542, 290), (1600, 290)], MUTED, 3)
        c.text(1620, 290, '蓝头抓水，尾巴钻进油里', 'sans', 24, INK, 'lm')
    if t > 17:
        c.text(960, 260, '冲水：油滴连同里面的细菌一起被带走', 'sans', 28, FIELD, 'mm')
    caps(c, t, [(0, 6, '手上的细菌常常裹在一层看不见的油里，光用水冲，水从油上滑过去'),
                (6.2, 12, '肥皂分子一头亲水、一头亲油，把油滴团团围住'),
                (12.2, 17, '搓洗，让油滴从皮肤的纹路里被拽出来：至少搓 20 秒'),
                (17.2, 22, '再用流水一冲，油滴连同细菌一起走了')], y=1050)

# ---------------------------------------------------------------- E33 防坏血病
TREAT = [('苹果酒', '每天一夸脱'), ('稀硫酸「矾酒」', '每天三次，每次 25 滴'), ('醋', '每天三次，每次两勺'),
         ('海水', '每天半品脱'), ('两个橙子、一个柠檬', '每天'), ('大蒜、芥末等糊剂', '每天三次')]

def person(c, x, y, col, s=1.0):
    c.ellipse(x, y - 60 * s, 22 * s, 22 * s, fill=col)
    c.rect(x - 22 * s, y - 34 * s, x + 22 * s, y + 30 * s, fill=col, r=int(10 * s))

def e33_trial(c, t, i):
    corner_tag(c, '第 33 集 · 1747 年的对照实验')
    c.text(60, 96, '12 个病人，分成 6 组：只换一样东西', 'serif', 40, INK)
    for k, (name, dose) in enumerate(TREAT):
        y = 230 + k * 118
        a = fade(t, 0.5 + k * 0.5, 1.2 + k * 0.5)
        good = k == 4
        rec = fade(t, 10, 13) if good else 0
        col = mix(mix(BG, MUTED, 0.7 * a), GREEN, rec)
        person(c, 230, y + 40, col, 0.8); person(c, 310, y + 40, col, 0.8)
        c.text(400, y + 20, name, 'bold', 30, mix(BG, INK, a), 'lm')
        c.text(400, y + 60, dose, 'sans', 22, mix(BG, MUTED, a), 'lm')
        if good and rec > 0:
            c.text(1000, y + 30, '六天后，其中一人已能回去干活', 'bold', 28, mix(BG, GREEN, rec), 'lm')
        elif k != 4 and t > 13:
            c.text(1000, y + 30, '没有明显好转', 'sans', 24, mix(BG, MUTED, fade(t, 13, 14)), 'lm')
    a = fade(t, 5, 6)
    c.rect(1380, 160, 1860, 210, fill=mix(BG, SHEET, a), r=10)
    c.text(1620, 185, '同样的病情 · 同样的伙食', 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 5, '1747 年，索尔兹伯里号上的军医林德挑了 12 个坏血病水手'),
                (5.2, 10, '病情相近、吃同样的饭，每两人一组，只加一种不同的「药」'),
                (10.2, 16, '只有吃橙子和柠檬的那一组，很快好了起来'),
                (16.2, 22, '只改一个条件、其他都一样：这就是对照实验')])

def helix(c, x0, x1, yc, amp, ph, col, w, broken=0.0):
    pts = []
    for k in range(0, 121):
        x = x0 + (x1 - x0) * k / 120
        pts.append((x, yc + amp * math.sin(k / 120 * 6 * math.pi + ph)))
    if broken <= 0:
        c.line(pts, col, w)
    else:
        seg = 12
        for s in range(0, 120, seg):
            if (s // seg) % 3 == 1 and broken > 0.5: continue
            c.line(pts[s:s + seg + 1], col, w)

def e33_vitc(c, t, i):
    corner_tag(c, '第 33 集 · 维生素 C')
    c.text(60, 96, '缺了维生素 C，身体哪里出了问题？', 'serif', 40, INK)
    for row, (lab, ok) in enumerate([('有维生素 C', True), ('缺维生素 C', False)]):
        yc = 330 + row * 260
        a = fade(t, 1 + row * 4, 2 + row * 4)
        cols = [COPPER, FIELD, SPARK]
        for k in range(3):
            helix(c, 300, 1200, yc, 40, k * 2.1, mix(BG, cols[k], a), 6, broken=0 if ok else fade(t, 7, 9))
        if ok:
            for k in range(14):
                x = 330 + k * 62
                c.line([(x, yc - 40), (x, yc + 40)], mix(BG, MUTED, 0.6 * a), 2)
        c.text(300, yc - 90, lab, 'bold', 30, mix(BG, INK if ok else NRED, a), 'lm')
        c.text(1260, yc, '结实的胶原蛋白' if ok else '胶原蛋白松散、易断', 'sans', 28, mix(BG, INK if ok else NRED, a), 'lm')
    a = fade(t, 10, 11)
    for k, s in enumerate(['牙龈出血', '旧伤口重新裂开', '皮下出血、乏力']):
        c.text(300 + k * 420, 780, s, 'bold', 28, mix(BG, NRED, a), 'lm')
    b = fade(t, 14, 15)
    tl = [('1747', '林德的实验'), ('1753', '出版《论坏血病》'), ('1795', '海军每天配发柠檬汁'), ('1928–32', '分离、确认维生素 C')]
    for k, (yr, s) in enumerate(tl):
        x = 260 + k * 400
        c.ellipse(x, 880, 10, 10, fill=mix(BG, COPPER, b))
        c.text(x + 20, 880, yr, 'mono', 24, mix(BG, COPPER, b), 'lm')
        c.text(x + 20, 920, s, 'sans', 22, mix(BG, INK, b), 'lm')
    if b > 0: c.line([(260, 880), (1460, 880)], mix(BG, LINE, b), 2)
    caps(c, t, [(0, 6, '身体里有一种像绳子一样拧成三股的蛋白：胶原蛋白，牙龈、血管、伤疤都靠它'),
                (6.2, 14, '拧绳子时要用维生素 C 帮忙「打结」；缺了它，绳子松散，一扯就断'),
                (14.2, 22, '从林德的实验到海军配发柠檬汁，隔了 48 年')], y=1040)

# ---------------------------------------------------------------- B19 银钗验毒
def spoon(c, x, y, tarn, label):
    col = mix(SILVER, TARN, tarn)
    c.ellipse(x, y, 46, 70, fill=col)
    c.rect(x - 10, y + 60, x + 10, y + 260, fill=col, r=6)
    c.text(x, y + 300, label, 'bold', 26, INK, 'mm')

def b19_tarnish(c, t, i):
    corner_tag(c, 'B19 · 银为什么变黑')
    c.text(60, 96, '银钗变黑，测到的到底是什么？', 'serif', 40, INK)
    g = fade(t, 4, 9)
    cases = [('纯砒霜', 0.0, '三氧化二砷', '不和银反应：不变色'),
             ('古代砒霜', g, '常混有含硫杂质', '变黑'),
             ('煮鸡蛋黄', g, '含硫', '也变黑，可它没毒')]
    for k, (lab, tr, sub, res) in enumerate(cases):
        x = 380 + k * 580
        a = fade(t, 0.5 + k * 1.2, 1.3 + k * 1.2)
        c.rect(x - 200, 220, x + 200, 360, fill=mix(BG, SHEET, a), r=12)
        c.text(x, 265, lab, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(x, 315, sub, 'sans', 24, mix(BG, MUTED, a), 'mm')
        spoon(c, x, 470, tr if a > 0.5 else 0, '')
        r = fade(t, 9.5 + k * 0.6, 10.3 + k * 0.6)
        c.text(x, 790, res, 'bold', 28, mix(BG, (NRED if k == 2 else (SPARK if k == 1 else FIELD)), r), 'mm')
    a = fade(t, 14, 15)
    c.rect(200, 850, 1720, 960, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 880, '银 + 硫 → 硫化银（黑色）', 'serif', 34, mix(BG, COPPER, a), 'mm')
    c.text(960, 930, '变黑说明有硫，不一定有毒；没变黑，也不能说明没毒', 'sans', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 4, '银碰到硫，表面会生成一层黑色的硫化银'),
                (4.2, 9.5, '纯砒霜里没有硫，并不会让银变黑；古代砒霜提纯不好，常混着含硫的杂质'),
                (9.6, 14, '鸡蛋黄这样没毒、却含硫的东西，同样能让银变黑'),
                (14.2, 22, '银钗测到的其实是硫：变黑不一定有毒，不变黑也不一定没毒')], y=1035)

def b19_restore(c, t, i):
    corner_tag(c, 'B19 · 把黑银变回来')
    c.text(60, 96, '黑掉的银，能不能变回来？', 'serif', 40, INK)
    # basin
    c.rect(360, 420, 1560, 860, fill=mix(BG, FIELD, 0.25), r=24)
    c.rect(400, 800, 1520, 840, fill=(170, 175, 182), r=4)
    c.text(960, 890, '铺在盆底的铝箔', 'sans', 24, MUTED, 'mm')
    c.text(400, 450, '热水 + 小苏打', 'sans', 24, FIELD, 'lm')
    back = fade(t, 7, 16)
    sx, sy = 960, 770
    c.rect(sx - 300, sy - 30, sx + 300, sy + 30, fill=mix(TARN, SILVER, back), r=28)
    c.text(sx, sy - 70, '硫化银' if back < 0.5 else '银', 'bold', 28, INK, 'mm')
    if 3 < t < 17:
        for k in range(6):
            ph = (t * 0.9 + k / 6) % 1
            x = 440 + ph * 360 if k % 2 else 1480 - ph * 360
            c.ellipse(x, 820, 8, 8, fill=SPARK)
        c.text(1600, 560, '电子从铝流向硫化银', 'sans', 26, SPARK, 'lm')
        c.text(1600, 600, '（铝要和银接触）', 'sans', 22, MUTED, 'lm')
    a = fade(t, 16, 17)
    c.text(960, 300, '硫跑到铝那边，银留下来', 'serif', 34, mix(BG, COPPER, a), 'mm')
    caps(c, t, [(0, 3, '把变黑的银放在铝箔上，倒进热水和小苏打'),
                (3.2, 10, '铝比银更爱失去电子，电子流到硫化银上，把银「还」回来'),
                (10.2, 16, '黑色一点点褪去。可要是只用皂角水擦，是擦不掉的：原文正是靠「其色不去」下判断'),
                (16.2, 22, '硫被带走，留下的还是银')], y=1010)

CLIPS = {
 'E32_死亡率': (e32_rates, 22), 'E32_肥皂': (e32_soap, 22),
 'E32_片头': (titles.opening(SER4, VOL4, S4A, 0, '1847 年 · 维也纳 · 塞麦尔维斯'), 7),
 'E32_片尾': (titles.closing(SER4, VOL4, S4A, 0, '下集：史上最早的对照实验之一'), 7),
 'E33_对照实验': (e33_trial, 22), 'E33_维生素C': (e33_vitc, 22),
 'E33_片头': (titles.opening(SER4, VOL4, S4A, 1, '1747 年 · 索尔兹伯里号 · 林德'), 7),
 'E33_片尾': (titles.closing(SER4, VOL4, S4A, 1, '下集：银钗变黑，就一定有毒吗？'), 7),
 'B19_银变黑': (b19_tarnish, 22), 'B19_还原': (b19_restore, 22),
 'B19_片头': (titles.opening(BSER, BVOL, SB4, 0, '南宋 · 1247 年 · 宋慈《洗冤集录》'), 7),
 'B19_片尾': (titles.closing(BSER, BVOL, SB4, 0, '下集：比细菌学早几十年的保鲜法'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
