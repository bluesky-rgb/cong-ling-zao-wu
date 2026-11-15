"""第五十四季（古法解密 24.0：衣与针线）第二批：B243 皂角、B244 浆衣、B245 火斗 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s54a import SB54, VOL54, CLOTH, WATER, WOODC

OIL = (230, 190, 60)
FOAM = (235, 240, 245)
STARCH = (240, 235, 210)
STEEL = (180, 185, 195)
HOT = (235, 120, 70)


# ---------------------------------------------------------------- B243 皂角
def _molecule(c, x, y, ang, s=1.0):
    hx, hy = x + 18 * s * math.cos(ang), y + 18 * s * math.sin(ang)
    tx, ty = x - 34 * s * math.cos(ang), y - 34 * s * math.sin(ang)
    c.line([(hx, hy), (tx, ty)], mix(BG, OIL, 0.9), 4)
    c.ellipse(hx, hy, 9 * s, 9 * s, fill=mix(BG, WATER, 1.0))


def b243_micelle(c, t, i):
    corner_tag(c, 'B243 · 一头连水，一头连油')
    c.text(60, 96, '皂苷分子一头喜欢水（蓝头）、一头喜欢油（黄尾）：尾巴钻进油里、头朝着水，把油拆成小油珠带走', 'serif', 36, INK)
    c.rect(200, 220, 1720, 900, fill=mix(BG, WATER, 0.18), r=20)
    split = min(1.0, max(0.0, (t - 7.2) / 6))
    if split < 0.05:
        c.ellipse(960, 560, 260, 160, fill=mix(BG, OIL, 0.9))
        n = int(min(1.0, t / 6) * 30)
        for k in range(n):
            a = 2 * math.pi * k / 30
            x, y = 960 + 300 * math.cos(a), 560 + 200 * math.sin(a)
            _molecule(c, x, y, a)
        c.text(960, 820, '一大滩油，水冲不走', 'bold', 28, NRED, 'mm')
    else:
        for j in range(5):
            ang0 = 2 * math.pi * j / 5
            r = 360 * split
            cx, cy = 960 + r * math.cos(ang0), 560 + 0.6 * r * math.sin(ang0)
            c.ellipse(cx, cy, 70, 70, fill=mix(BG, OIL, 0.9))
            for k in range(12):
                a = 2 * math.pi * k / 12
                _molecule(c, cx + 100 * math.cos(a), cy + 100 * math.sin(a), a, 0.8)
        c.text(960, 950, '拆成被皂苷包住的小油珠，散进水里', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '油和水不相溶，一滩油浮在那里，清水冲不走'),
                (7.2, 14, '皂苷的尾巴钻进油里，头留在水里，把油一圈圈包住'),
                (14.2, 22, '一大滩油被拆成小油珠，跟着水一起冲走（分子示意）')], y=1010)


def b243_jars(c, t, i):
    corner_tag(c, 'B243 · 清水和皂角水')
    c.text(60, 96, '两瓶水各滴 5 滴油摇一摇：清水里的油很快又浮成一层；皂角水里的油散成很多小珠，还冒出一层泡沫', 'serif', 36, INK)
    shake = 20 * math.sin(t * 12) if t < 5 else 0
    settle = min(1.0, max(0.0, (t - 5) / 5))
    for j, (lab, soap) in enumerate([('清水', False), ('皂角水', True)]):
        cx = 560 + j * 800 + shake
        c.rect(cx - 150, 260, cx + 150, 820, outline=mix(BG, INK, 0.6), width=5, r=24)
        c.rect(cx - 144, 430, cx + 144, 814, fill=mix(BG, (200, 160, 90) if soap else WATER, 0.35), r=20)
        random.seed(7 + j)
        if soap:
            for k in range(40):
                c.ellipse(cx + random.uniform(-120, 120), random.uniform(470, 790), 6, 6, fill=mix(BG, OIL, 1.0))
            for k in range(30):
                c.ellipse(cx + random.uniform(-130, 130), 430 - random.uniform(0, 70) * (0.5 + 0.5 * settle), 14, 14, outline=mix(BG, FOAM, 1.0), width=3)
        else:
            if settle < 1:
                for k in range(20):
                    y = random.uniform(470, 790) * (1 - settle) + 440 * settle
                    c.ellipse(cx + random.uniform(-120, 120), y, 10, 10, fill=mix(BG, OIL, 1.0))
            c.rect(cx - 144, 430, cx + 144, 430 + 20 * settle, fill=mix(BG, OIL, 0.9 * settle))
        c.text(cx, 880, lab + ('：油散开，有泡沫' if soap else '：油又浮成一层'), 'bold', 28, GREEN if soap else NRED, 'mm')
    caps(c, t, [(0, 7, '两瓶各滴 5 滴食用油，盖紧摇 20 下'),
                (7.2, 14, '静置一分钟：清水瓶里的油又聚成一层浮在上面'),
                (14.2, 22, '皂角水里的油散成小珠，还有泡沫：和肥皂一个道理（皂角水不喝）')], y=1010)


# ---------------------------------------------------------------- B244 浆衣
def b244_film(c, t, i):
    corner_tag(c, 'B244 · 淀粉结成薄膜，把纤维粘在一起')
    c.text(60, 96, '米汤里有煮出来的淀粉糊：渗进布的纤维缝里，晾干后结成一层薄膜，把一根根纤维粘在一起，布就挺括了', 'serif', 36, INK)
    dry = min(1.0, max(0.0, (t - 7.2) / 7))
    for k in range(9):
        x = 360 + k * 150
        wob = 0 if dry > 0.8 else 20 * math.sin(t * 2 + k)
        c.line([(x, 260), (x + wob, 560), (x, 860)], mix(BG, CLOTH, 1.0), 14)
    if t > 3:
        random.seed(1)
        for k in range(60):
            x = random.uniform(360, 1560)
            y = random.uniform(270, 850)
            c.ellipse(x, y, 10, 10, fill=mix(BG, STARCH, 0.4 + 0.5 * min(1, (t - 3) / 3)))
    if dry > 0:
        for k in range(8):
            x = 360 + k * 150
            c.rect(x + 6, 420, x + 144, 700, fill=mix(BG, STARCH, 0.5 * dry), r=6)
    c.text(960, 220, '湿：纤维软软的、能晃' if dry < 0.5 else '干：淀粉膜把纤维连成一片', 'bold', 28, GREEN if dry >= 0.5 else INK, 'mm')
    caps(c, t, [(0, 7, '布泡进放凉的米汤，淀粉糊渗进纤维之间'),
                (7.2, 14, '晾着晾着，水分跑掉，淀粉结成一层薄膜'),
                (14.2, 22, '纤维被粘在一起不能乱动，布就挺括；下次一洗，淀粉又溶掉')], y=1010)


def b244_droop(c, t, i):
    corner_tag(c, 'B244 · 伸出 15 厘米，垂下多少')
    c.text(60, 96, '两条晾干的布，一头压在桌边伸出 15 厘米：泡清水的软软地垂下去；浆过的挺挺地伸着，几乎不垂', 'serif', 36, INK)
    ph = min(1.0, t / 6)
    for j, (lab, droop) in enumerate([('泡清水', 200), ('浆过米汤', 30)]):
        x0, y0 = 300 + j * 820, 520
        c.rect(x0 - 200, y0, x0, y0 + 300, fill=mix(BG, WOODC, 0.8))
        c.rect(x0 - 160, y0 - 50, x0 - 20, y0, fill=mix(BG, (120, 160, 210), 0.9), r=4)
        d = droop * ph
        pts = [(x0 + 450 * u / 20 * math.cos(math.atan2(d, 450) * u / 20), y0 + d * (u / 20) ** 2) for u in range(21)]
        c.line([(x0 - 160, y0 - 4)] + pts, mix(BG, CLOTH, 1.0), 14)
        c.text(x0 + 220, y0 + 360, f'{lab}：垂下约 {d / 20:.0f} 厘米（示意）', 'bold', 26, NRED if droop > 100 else GREEN, 'mm')
    if t > 14.2:
        c.ellipse(960, 300, 50, 30, fill=mix(BG, (80, 60, 130), 1.0))
        c.text(1060, 300, '米汤 + 碘伏：变蓝紫色，说明里面有淀粉', 'bold', 26, INK, 'lm')
    caps(c, t, [(0, 7, '两条布一头压在桌边，各伸出 15 厘米'),
                (7.2, 14, '泡清水的软软垂下；浆过的挺挺地伸着'),
                (14.2, 22, '米汤滴上碘伏变蓝紫色：里面真有淀粉（米汤不喝，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B245 火斗
def b245_fiber(c, t, i):
    corner_tag(c, 'B245 · 又湿又热，纤维变软')
    c.text(60, 96, '揉皱的布，纤维弯着定了型；遇到水和热，纤维变软，再一压一推就被压直；水分跑掉、凉下来，就在直的样子定型', 'serif', 36, INK)
    st = 0 if t < 4 else (1 if t < 9 else 2)
    flat = min(1.0, max(0.0, (t - 9) / 4))
    for k in range(6):
        y = 380 + k * 80
        amp = 40 * (1 - flat)
        pts = [(300 + u * 66, y + amp * math.sin(u * 0.9 + k)) for u in range(21)]
        col = mix(BG, CLOTH, 1.0) if st == 0 else mix(mix(BG, CLOTH, 1.0), WATER, 0.35)
        c.line(pts, col, 10)
    if st >= 1:
        random.seed(2)
        for k in range(25):
            c.ellipse(random.uniform(300, 1620), random.uniform(360, 820), 6, 6, fill=mix(BG, WATER, 0.9))
    if st == 2:
        ix = 300 + 1320 * min(1.0, (t - 9) / 5)
        c.rect(ix - 120, 300, ix + 120, 360, fill=mix(BG, STEEL, 1.0), r=10)
        c.text(ix, 270, '温水杯（≤50 ℃）', 'bold', 24, HOT, 'mm')
    lab = ['干的：纤维弯着', '喷湿：纤维变软', '一压一推：压直了'][st]
    c.text(960, 900, lab, 'bold', 30, GREEN if st == 2 else INK, 'mm')
    caps(c, t, [(0, 7, '揉皱的布：纤维弯弯曲曲，已经定了型'),
                (7.2, 14, '喷湿，再用装着温水的平底杯一压一推'),
                (14.2, 22, '纤维被压直，干了凉了就在直的样子定型（古人用炭火铜斗，本集只用温水）')], y=1010)


def b245_compare(c, t, i):
    corner_tag(c, 'B245 · 干压、湿压、湿热推')
    c.text(60, 96, '三块一样皱的布：干着压书 10 分钟，皱纹几乎还在；喷湿再压，平了一些；喷湿用温水杯推平再压，最平', 'serif', 36, INK)
    res = [('干着压书', 0.9), ('喷湿压书', 0.5), ('喷湿 + 温水杯推', 0.15)]
    k = min(2, int(t / 7.3))
    for j, (lab, w) in enumerate(res):
        cx = 400 + j * 560
        c.rect(cx - 200, 300, cx + 200, 700, fill=mix(BG, CLOTH, 1.0), r=8)
        ww = w if j <= k else 1.0
        random.seed(10 + j)
        for m in range(int(14 * ww)):
            x = cx + random.uniform(-170, 170)
            y = random.uniform(320, 680)
            a = random.uniform(0, math.pi)
            c.line([(x - 50 * math.cos(a), y - 50 * math.sin(a)), (x + 50 * math.cos(a), y + 50 * math.sin(a))], mix(BG, (150, 140, 120), 1.0), 4)
        c.text(cx, 760, lab, 'bold', 28, INK if j <= k else MUTED, 'mm')
    c.text(960, 840, '皱纹多少以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '干着压书：纤维还是硬的，皱纹几乎都在'),
                (7.2, 14, '喷湿再压：水让纤维变软，平了一些'),
                (14.2, 22, '又湿又热再一推：最平。这就是熨斗的道理')], y=1010)


CLIPS = {
 'B243_油珠': (b243_micelle, 22), 'B243_两瓶': (b243_jars, 22),
 'B243_片头': (titles.opening(BSER, VOL54, SB54, 3, '古人常用皂荚泡水洗衣'), 7),
 'B243_片尾': (titles.closing(BSER, VOL54, SB54, 3, '下集：米汤怎么让布变硬？'), 7),
 'B244_成膜': (b244_film, 22), 'B244_垂度': (b244_droop, 22),
 'B244_片头': (titles.opening(BSER, VOL54, SB54, 4, '古人洗衣后常用米汤上浆'), 7),
 'B244_片尾': (titles.closing(BSER, VOL54, SB54, 4, '下集：热和压怎么把皱纹弄平？'), 7),
 'B245_纤维': (b245_fiber, 22), 'B245_对比': (b245_compare, 22),
 'B245_片头': (titles.opening(BSER, VOL54, SB54, 5, '汉代已有铜熨斗'), 7),
 'B245_片尾': (titles.closing(BSER, VOL54, SB54, 5, '下集：一层层软布怎么变硬？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
