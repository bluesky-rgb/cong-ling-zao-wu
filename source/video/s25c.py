"""第二十五季（第九层：看见身体）第三批：E138 心脏起搏器、E139 核磁共振、E140 DNA —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s25a import S25A, SER25, VOL25, SKINC, SOUND

HEART = (200, 80, 90)
PULSE = (250, 210, 90)
SPIN = (120, 180, 240)
RF = (240, 150, 90)
BASES = {'A': (230, 120, 110), 'T': (120, 190, 140), 'G': (240, 200, 90), 'C': (120, 160, 230)}
PAIR = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def ecg(u):
    """一次心跳的心电示意波形，u 在 0..1。"""
    v = 0.12 * math.exp(-((u - 0.18) / 0.04) ** 2)
    v += -0.15 * math.exp(-((u - 0.30) / 0.012) ** 2)
    v += 1.0 * math.exp(-((u - 0.33) / 0.015) ** 2)
    v += -0.25 * math.exp(-((u - 0.36) / 0.012) ** 2)
    v += 0.28 * math.exp(-((u - 0.58) / 0.06) ** 2)
    return v


# ---------------------------------------------------------------- E138 心脏起搏器
def e138_node(c, t, i):
    corner_tag(c, '第 138 集 · 心脏自己带着一个「节拍器」')
    c.text(60, 96, '心脏右上角有一小团细胞（窦房结），每隔不到一秒自己放一次电，电沿着线路传遍心脏，心就跳一下', 'serif', 36, INK)
    cx, cy = 560, 560
    period = 0.86
    ph = (t % period) / period
    sq = 1 - 0.06 * math.exp(-((ph - 0.4) / 0.12) ** 2)
    c.ellipse(cx, cy, 260 * sq, 300 * sq, fill=mix(BG, HEART, 0.75))
    c.line([(cx - 240, cy - 40), (cx + 240, cy - 40)], mix(BG, INK, 0.25), 3)
    c.text(cx - 140, cy - 130, '心房', 'sans', 24, INK, 'mm')
    c.text(cx, cy + 140, '心室', 'sans', 24, INK, 'mm')
    sa = (cx - 150, cy - 210)
    av = (cx, cy - 40)
    glow = math.exp(-(ph / 0.05) ** 2) + math.exp(-((ph - 1) / 0.05) ** 2)
    c.ellipse(sa[0], sa[1], 18 + 14 * glow, 18 + 14 * glow, fill=mix(BG, PULSE, 0.4 + 0.6 * glow))
    c.text(sa[0] - 30, sa[1] - 50, '窦房结', 'bold', 22, PULSE, 'mm')
    c.ellipse(av[0], av[1], 12, 12, fill=mix(BG, PULSE, 0.6))
    path = [sa, av, (cx, cy + 200), (cx - 120, cy + 120), (cx + 120, cy + 120)]
    c.line([sa, av], mix(BG, PULSE, 0.35), 3)
    c.line([av, (cx, cy + 210)], mix(BG, PULSE, 0.35), 3)
    c.line([(cx, cy + 210), (cx - 150, cy + 100)], mix(BG, PULSE, 0.35), 3)
    c.line([(cx, cy + 210), (cx + 150, cy + 100)], mix(BG, PULSE, 0.35), 3)
    if ph < 0.3:
        u = ph / 0.3
        if u < 0.5:
            p = (sa[0] + (av[0] - sa[0]) * u * 2, sa[1] + (av[1] - sa[1]) * u * 2)
        else:
            p = (av[0], av[1] + 250 * (u - 0.5) * 2)
        c.ellipse(p[0], p[1], 12, 12, fill=PULSE)
    gx0, gx1, gy = 1000, 1840, 600
    c.rect(960, 300, 1880, 860, fill=SHEET, r=14)
    c.text(1420, 340, '心电图（示意）：每一个尖峰，就是一次放电传遍心室', 'bold', 22, INK, 'mm')
    c.line([(gx0, gy), (gx1, gy)], LINE, 1)
    win = 3.0
    pts = []
    for j in range(421):
        s = t - win + win * j / 420
        if s < 0:
            continue
        pts.append((gx0 + (gx1 - gx0) * j / 420, gy - 200 * ecg((s % period) / period)))
    if len(pts) > 1:
        c.line(pts, GREEN, 3)
    c.text(1420, 820, f'约 {60 / period:.0f} 次/分（静息时常见 60–100，拍摄前核对）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '心脏不用大脑每次下命令：右心房上方有一小团特别的细胞，叫窦房结'),
                (7.2, 14, '它自己每隔不到一秒放一次电，电先让心房收缩，再经过一个「中转站」传到心室'),
                (14.2, 22, '心电图上的一个个尖峰，就是这一次次放电：这条线路出了故障，心跳就会变慢、停顿（示意）')], y=1010)


def e138_demand(c, t, i):
    corner_tag(c, '第 138 集 · 起搏器：不跳了才补一下')
    c.text(60, 96, '起搏器一直「听」着心跳：等了太久还没有，就自己放一个小电脉冲；心自己跳了，它就不出声', 'serif', 36, INK)
    gx0, gx1 = 140, 1780
    win = 6.0
    # 自身心跳：不规则，有长停顿
    beats = []
    s = 0.0
    rnd = random.Random(7)
    while s < 40:
        beats.append(s)
        s += rnd.choice([0.8, 0.85, 0.9, 1.9, 2.2, 0.82])
    limit = 1.2
    events = []
    last = -10
    for b in beats:
        while b - last > limit + 1e-9 and last > -5:
            last = last + limit
            events.append((last, 'paced'))
        events.append((b, 'own'))
        last = b
    rows = [(380, '没有起搏器', False), (720, '装了起搏器（等 1.2 秒没跳就补一下，示意）', True)]
    for (gy, label, paced) in rows:
        c.rect(gx0 - 20, gy - 200, gx1 + 20, gy + 70, fill=SHEET, r=12)
        c.text(gx0, gy - 175, label, 'bold', 24, INK, 'lm')
        c.line([(gx0, gy), (gx1, gy)], LINE, 1)
        evs = events if paced else [(b, 'own') for b in beats]
        pts = []
        for j in range(601):
            ss = t - win + win * j / 600
            v = 0.0
            for (e, kind) in evs:
                if e <= ss < e + 0.8:
                    v += ecg((ss - e) / 0.8 * 0.7 + 0.15)
            pts.append((gx0 + (gx1 - gx0) * j / 600, gy - 140 * v))
        c.line(pts, GREEN, 3)
        for (e, kind) in evs:
            if kind == 'paced' and t - win <= e <= t:
                x = gx0 + (gx1 - gx0) * (e - (t - win)) / win
                c.line([(x - 22, gy - 160), (x - 22, gy + 40)], PULSE, 3)
                c.text(x - 22, gy + 52, '补', 'bold', 18, PULSE, 'mm')
    c.rect(1200, 860, 1780, 940, fill=SHEET, r=10)
    c.text(1490, 900, '黄线：起搏器放的电脉冲', 'sans', 22, PULSE, 'mm')
    caps(c, t, [(0, 7, '有的人心脏的「线路」坏了，心跳会突然停顿好一会儿，人就头晕、眼前发黑'),
                (7.2, 14, '起搏器埋在锁骨下面，一根细导线伸进心脏，一直「听」着每一次心跳'),
                (14.2, 22, '等太久还没跳，它就放一个小电脉冲把心「叫」醒；心自己跳了，它就不打扰（等待时间为示意）')], y=1010)


# ---------------------------------------------------------------- E139 核磁共振
def e139_align(c, t, i):
    corner_tag(c, '第 139 集 · 身体里亿万个「小磁针」')
    c.text(60, 96, '水里的氢原子核像一个个小磁针：平时乱指，放进强磁场，就有一点点偏向磁场方向，一边转一边摆', 'serif', 36, INK)
    B = min(1, max(0, (t - 6) / 4))
    rnd = random.Random(3)
    c.rect(120, 220, 1180, 900, fill=mix(BG, SKINC, 0.15), r=16)
    for k in range(48):
        x = 180 + (k % 8) * 128
        y = 280 + (k // 8) * 110
        a0 = rnd.uniform(0, 2 * math.pi)
        tilt = (1 - B) * 1.0 + B * 0.45
        base = a0 * (1 - B) + (-math.pi / 2) * B
        prec = base + B * 0.45 * math.sin(t * 6 + k)
        if B < 1:
            prec = a0 * (1 - B) + (-math.pi / 2 + 0.45 * math.sin(t * 6 + k)) * B
        dx, dy = 40 * math.cos(prec), 40 * math.sin(prec)
        c.arrow(x - dx * 0.5, y - dy * 0.5, x + dx * 0.5, y + dy * 0.5, SPIN, 3, 10)
    c.text(650, 940, '每个箭头：一个氢原子核（示意，真实数量多得多）', 'sans', 20, MUTED, 'mm')
    c.rect(1260, 260, 1860, 840, fill=SHEET, r=14)
    c.text(1560, 300, '外加磁场', 'bold', 26, INK, 'mm')
    for k in range(5):
        x = 1340 + k * 110
        if B > 0:
            c.arrow(x, 760, x, 760 - 380 * B, mix(BG, SPARK, 0.4 + 0.6 * B), 5, 18)
    c.text(1560, 800, '关着' if B == 0 else ('正在打开' if B < 1 else '打开：比地磁场强几万倍'), 'sans', 22, SPARK if B > 0 else MUTED, 'mm')
    caps(c, t, [(0, 7, '人身体里大半是水，水里的每个氢原子核，都像一个极小的磁针'),
                (7.2, 14, '平时它们乱指一气；躺进大圆筒，强磁场一开，就有一点点多的偏向同一个方向'),
                (14.2, 22, '它们不是乖乖站直，而是像陀螺一样一边转一边摆：摆的快慢，由磁场的强弱决定（示意）')], y=1010)


def e139_resonance(c, t, i):
    corner_tag(c, '第 139 集 · 推一下，听它「回声」')
    c.text(60, 96, '用和它摆动一样快的无线电波推一下，小磁针就被推歪；停下后它慢慢回正，同时发出微弱的无线电信号', 'serif', 36, INK)
    T = 11.0
    ph = t % T
    cx, cy = 480, 560
    c.ellipse(cx, cy, 300, 300, outline=LINE, width=2)
    c.arrow(cx, cy + 320, cx, cy - 340, mix(BG, SPARK, 0.5), 3, 14)
    c.text(cx + 30, cy - 330, '磁场方向', 'sans', 20, MUTED, 'lm')
    if ph < 2:
        tilt = 0.25
        pulse = False
    elif ph < 3.5:
        tilt = 0.25 + (math.pi / 2 - 0.25) * (ph - 2) / 1.5
        pulse = True
    else:
        tilt = 0.25 + (math.pi / 2 - 0.25) * math.exp(-(ph - 3.5) / 2.2)
        pulse = False
    az = t * 5
    L = 240
    tipx = cx + L * math.sin(tilt) * math.cos(az)
    tipy = cy - L * math.cos(tilt) + 0.3 * L * math.sin(tilt) * math.sin(az)
    c.arrow(cx, cy, tipx, tipy, SPIN, 6, 20)
    if pulse:
        for k in range(4):
            x = 120 + ((t * 300 + k * 80) % 320)
            c.line([(x, cy - 60 + j * 0) for j in range(1)] + [(x, cy + 60)], RF, 4)
        c.text(200, cy + 120, '无线电脉冲', 'bold', 22, RF, 'mm')
    gx0, gx1, gy = 1000, 1840, 560
    c.rect(960, 260, 1880, 860, fill=SHEET, r=14)
    c.text(1420, 300, '线圈收到的信号（示意）', 'bold', 24, INK, 'mm')
    c.line([(gx0, gy), (gx1, gy)], LINE, 1)
    pts = []
    for j in range(501):
        s = T * j / 500
        if s > ph:
            break
        amp = 0
        if s >= 3.5:
            amp = 220 * math.exp(-(s - 3.5) / 1.4)
        pts.append((gx0 + (gx1 - gx0) * j / 500, gy - amp * math.sin(s * 30)))
    if len(pts) > 1:
        c.line(pts, GREEN, 2)
    c.text(1420, 820, '不同组织「回正」的快慢不同，图上就亮暗不同', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '机器发出一阵无线电波，频率正好和小磁针摆动的快慢一样，就像荡秋千踩准了节拍'),
                (7.2, 14, '小磁针被推歪；无线电一停，它们一边转一边慢慢回正，同时发出微弱的无线电「回声」'),
                (14.2, 22, '脂肪、肌肉、液体回正的快慢不一样，信号也就不一样：再用变化的磁场标出位置，就拼成了一张图（示意）')], y=1010)


# ---------------------------------------------------------------- E140 DNA
SEQ = 'ATGCGTACCTAGGATC'


def e140_helix(c, t, i):
    corner_tag(c, '第 140 集 · 两条链，按规矩配对')
    c.text(60, 96, 'DNA 是两条长链拧成的梯子：梯级是四种「字母」配成的对，A 只和 T 配，G 只和 C 配', 'serif', 38, INK)
    x0, x1, cy = 160, 1760, 500
    n = len(SEQ)
    unzip = min(1, max(0, (t - 12) / 5))
    for k in range(n):
        x = x0 + (x1 - x0) * k / (n - 1)
        ph = k * 0.7 + t * 1.2
        amp = 150 + 120 * unzip
        y1 = cy - amp * math.cos(ph) * (1 - unzip) - amp * unzip
        y2 = cy + amp * math.cos(ph) * (1 - unzip) + amp * unzip
        b1 = SEQ[k]
        b2 = PAIR[b1]
        front = math.sin(ph) > 0 or unzip > 0.5
        if unzip < 0.3:
            c.line([(x, y1), (x, (y1 + y2) / 2)], mix(BG, BASES[b1], 0.9 if front else 0.4), 10)
            c.line([(x, (y1 + y2) / 2), (x, y2)], mix(BG, BASES[b2], 0.9 if front else 0.4), 10)
        c.ellipse(x, y1, 18, 18, fill=mix(BG, (220, 220, 230), 0.8))
        c.ellipse(x, y2, 18, 18, fill=mix(BG, (220, 220, 230), 0.8))
        c.text(x, y1 + (40 if unzip > 0.3 else 0), b1, 'bold', 24, BASES[b1] if unzip > 0.3 else BG, 'mm')
        c.text(x, y2 - (40 if unzip > 0.3 else 0), b2, 'bold', 24, BASES[b2] if unzip > 0.3 else BG, 'mm')
    if unzip > 0.3:
        c.text(960, cy, '拆开：一条链上的字母，决定了另一条链该是什么', 'sans', 24, INK, 'mm')
    c.rect(300, 840, 1620, 930, fill=SHEET, r=12)
    for k, b in enumerate('ATGC'):
        c.rect(360 + k * 320, 865, 400 + k * 320, 905, fill=BASES[b], r=6)
        c.text(420 + k * 320, 885, b + ' 配 ' + PAIR[b], 'bold', 24, INK, 'lm')
    caps(c, t, [(0, 7, '细胞里藏着一本「说明书」，写在一种叫 DNA 的长长的分子上'),
                (7.2, 14, '它是两条链拧成的梯子，每一级梯子是一对「字母」：A 配 T，G 配 C，从不配错'),
                (14.2, 22, '一条链上的字母，决定了另一条；复制时拆开梯子，各自照着配出新的一半（示意）')], y=1010)


def e140_extract(c, t, i):
    corner_tag(c, '第 140 集 · 把 DNA 从草莓里拉出来')
    c.text(60, 96, '捣碎、洗洁精溶开细胞膜、盐让 DNA 聚在一起、过滤，再沿杯壁倒冷酒精：白色絮状物浮了上来', 'serif', 36, INK)
    steps = [('捣碎', '密封袋里压碎草莓'), ('溶膜', '加洗洁精和盐水'), ('过滤', '咖啡滤纸滤出汁'), ('析出', '倒冷酒精（成年人操作）')]
    k = min(3, int(t / 5.5))
    for j, (a, b) in enumerate(steps):
        x = 140 + j * 440
        on = j <= k
        c.rect(x, 200, x + 400, 300, fill=mix(BG, SHEET, 1 if on else 0.4), r=12)
        c.text(x + 200, 235, f'{j + 1}. {a}', 'bold', 26, SPARK if j == k else (INK if on else MUTED), 'mm')
        c.text(x + 200, 275, b, 'sans', 20, INK if on else MUTED, 'mm')
    cx, cy = 960, 640
    s = (t % 5.5) / 5.5
    if k == 0:
        c.rect(cx - 260, cy - 200, cx + 260, cy + 200, fill=mix(BG, (200, 210, 230), 0.25), r=30)
        sq = 1 - 0.5 * s
        for m in range(6):
            c.ellipse(cx - 160 + m * 64, cy + 40, 50, 60 * sq + 10, fill=(210, 60, 70))
        c.text(cx, cy + 250, '把细胞壁、细胞挤破', 'sans', 22, INK, 'mm')
    elif k == 1:
        cells = 5
        for m in range(cells):
            x = cx - 320 + m * 160
            br = min(1, max(0, s * 2 - m * 0.15))
            c.ellipse(x, cy, 60, 60, outline=mix(SHEET, BG, br), width=4)
            for q in range(5):
                a = q * 1.2 + m
                rr = 20 + 50 * br
                c.line([(x + rr * math.cos(a) * 0.4, cy + rr * math.sin(a) * 0.4), (x + rr * math.cos(a + 0.8), cy + rr * math.sin(a + 0.8))], mix(BG, (240, 240, 245), 0.9), 2)
        c.text(cx, cy + 140, '洗洁精溶开油脂做的膜，长长的 DNA 散进汁里；盐让它们更容易聚在一起', 'sans', 22, INK, 'mm')
    elif k == 2:
        c.poly([(cx - 200, cy - 200), (cx + 200, cy - 200), (cx, cy + 20)], mix(BG, (230, 220, 200), 0.6))
        c.rect(cx - 140, cy + 60, cx + 140, cy + 260, outline=LINE, width=3)
        lvl = min(1, s * 1.2)
        c.rect(cx - 136, cy + 256 - 190 * lvl, cx + 136, cy + 256, fill=mix(BG, (220, 90, 110), 0.6))
        for m in range(int(s * 8)):
            c.ellipse(cx, cy + 30 + ((m * 0.37 + s * 3) % 1) * 30, 5, 7, fill=(220, 90, 110))
        c.text(cx, cy + 300, '滤掉果肉，留下带 DNA 的汁', 'sans', 22, INK, 'mm')
    else:
        c.rect(cx - 140, cy - 180, cx + 140, cy + 260, outline=LINE, width=3)
        c.rect(cx - 136, cy + 70, cx + 136, cy + 256, fill=mix(BG, (220, 90, 110), 0.6))
        c.rect(cx - 136, cy + 70 - 150 * min(1, s * 2), cx + 136, cy + 70, fill=mix(BG, (200, 220, 240), 0.25))
        rnd = random.Random(11)
        for m in range(40):
            if rnd.random() < s * 1.3:
                x = cx + rnd.uniform(-110, 110)
                y = cy + 70 - rnd.uniform(0, 120) * min(1, s * 1.5)
                c.line([(x, y), (x + rnd.uniform(-20, 20), y - rnd.uniform(10, 30))], (245, 245, 245), 3)
        c.text(cx, cy + 300, '酒精层里浮起白色絮状物：那就是很多很多 DNA 缠在一起（不能吃）', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 5.5, '先把草莓装进密封袋里压碎，把一个个细胞挤破'),
                (5.7, 11, '洗洁精能溶开细胞外面那层油脂做的膜，盐让散出来的 DNA 更容易聚在一起'),
                (11.2, 16.5, '用咖啡滤纸滤掉果肉，留下带着 DNA 的红色汁液'),
                (16.7, 22, 'DNA 不溶于酒精：沿杯壁倒一层冰过的酒精，白色的絮就浮了上来（酒精由成年人操作，远离明火）')], y=1010)


CLIPS = {
 'E138_窦房结': (e138_node, 22), 'E138_按需起搏': (e138_demand, 22),
 'E138_片头': (titles.opening(SER25, VOL25, S25A, 6, '1958 年第一台植入式心脏起搏器'), 7),
 'E138_片尾': (titles.closing(SER25, VOL25, S25A, 6, '下集：医院里那台大圆筒，怎么用磁铁看见身体里面？'), 7),
 'E139_小磁针': (e139_align, 22), 'E139_共振': (e139_resonance, 22),
 'E139_片头': (titles.opening(SER25, VOL25, S25A, 7, '1970 年代磁共振成像'), 7),
 'E139_片尾': (titles.closing(SER25, VOL25, S25A, 7, '下集：草莓里的「生命说明书」，能用洗洁精和酒精拉出来吗？'), 7),
 'E140_双螺旋': (e140_helix, 22), 'E140_提取': (e140_extract, 22),
 'E140_片头': (titles.opening(SER25, VOL25, S25A, 8, '1953 年发现 DNA 双螺旋结构'), 7),
 'E140_片尾': (titles.closing(SER25, VOL25, S25A, 8, '下集：不开大刀，医生怎么从几个小孔里做手术？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
