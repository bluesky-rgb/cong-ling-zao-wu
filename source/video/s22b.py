"""第二十二季（古法解密 8.0）第二批：B83 窑洞、B84 弹棉花、B85 香篆钟 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import SB22, VOL22

LOESS = (190, 150, 95)
LOESS_D = (150, 115, 70)
SKY = (70, 110, 160)
HOT = (230, 110, 70)
COLD = (90, 150, 230)
COTTON = (235, 232, 220)
STRING = (230, 210, 150)
ASH = (170, 165, 160)
EMBER = (240, 120, 60)
SMOKE = (150, 150, 160)


def temp_col(v):
    """v 在 0（冷）到 1（热）之间。"""
    return mix(COLD, HOT, max(0.0, min(1.0, v)))


# ---------------------------------------------------------------- B83 窑洞
def b83_layers(c, t, i):
    corner_tag(c, 'B83 · 冷热传不进去')
    c.text(60, 96, '外面一天冷热来回变；往土里越深，变化越小、来得越晚', 'serif', 40, INK)
    day = (t / 22) * 2  # 两天
    outside = 0.5 + 0.45 * math.sin(2 * math.pi * day - math.pi / 2)
    x0, x1 = 160, 1100
    c.rect(x0, 200, x1, 300, fill=mix(BG, temp_col(outside), 0.8))
    c.text(x0 + 20, 250, '地面空气', 'bold', 24, INK, 'lm')
    depths = [0.1, 0.3, 0.6, 1.0, 2.0, 3.0]
    for k, d in enumerate(depths):
        y = 300 + k * 100
        damp = math.exp(-d / 0.45)
        lag = d / 0.45
        v = 0.5 + 0.45 * damp * math.sin(2 * math.pi * day - math.pi / 2 - lag)
        c.rect(x0, y, x1, y + 100, fill=mix(LOESS_D, temp_col(v), 0.65))
        c.text(x0 + 20, y + 50, f'{d:g} 米深', 'sans', 22, INK, 'lm')
        c.line([(x1 - 300 + 0, y + 50), (x1 - 300 + 260 * v, y + 50)], INK, 6)
    c.text(x1 - 170, 960, '← 冷　　热 →', 'sans', 20, MUTED, 'mm')
    c.rect(1240, 240, 1840, 820, fill=SHEET, r=14)
    c.text(1540, 280, '一天里的温度曲线（示意）', 'bold', 24, INK, 'mm')
    gx0, gx1, gy = 1280, 1800, 500
    c.line([(gx0, gy), (gx1, gy)], LINE, 2)
    for d, col in ((0.0, temp_col(0.9)), (0.3, SPARK), (2.0, GREEN)):
        damp = math.exp(-d / 0.45); lag = d / 0.45
        pts = []
        for j in range(101):
            u = j / 100 * 2
            if u > day: break
            pts.append((gx0 + (gx1 - gx0) * u / 2, gy - 170 * damp * math.sin(2 * math.pi * u - math.pi / 2 - lag)))
        if len(pts) > 1:
            c.line(pts, col, 4)
    c.text(1540, 780, '红：地面　黄：0.3 米　绿：2 米', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '白天太阳晒、夜里散热，地面空气的温度一天来回变好多度'),
                (7.2, 14, '热要一层层往土里传，传得很慢：越往下，冷热变化越小，还会晚上好几个小时'),
                (14.2, 22, '到了两三米深，白天黑夜几乎一样（示意，以实测为准）。窑洞就挖在这样厚的土里')], y=1010)


def b83_cave(c, t, i):
    corner_tag(c, 'B83 · 窑洞的一年')
    c.text(60, 96, '外面夏天热、冬天冷；几米厚的黄土把一年的冷热也「抹平」了', 'serif', 40, INK)
    yr = (t / 22)
    outside = 0.5 + 0.45 * math.sin(2 * math.pi * yr - math.pi / 2)
    inside = 0.5 + 0.12 * math.sin(2 * math.pi * yr - math.pi / 2 - 0.9)
    c.rect(0, 160, 1920, 420, fill=mix(BG, temp_col(outside), 0.35))
    c.rect(0, 420, 1920, 940, fill=LOESS)
    for k in range(40):
        rnd = random.Random(k)
        c.line([(rnd.uniform(0, 1920), rnd.uniform(440, 920)), (rnd.uniform(0, 1920), rnd.uniform(440, 920))], mix(LOESS, LOESS_D, 0.5), 1)
    cx, cy = 900, 800
    c.rect(cx - 220, cy - 60, cx + 220, cy + 120, fill=mix(BG, temp_col(inside), 0.6))
    c.ellipse(cx, cy - 60, 220, 100, fill=mix(BG, temp_col(inside), 0.6))
    c.rect(cx - 230, cy + 120, cx + 230, cy + 140, fill=LOESS_D)
    c.text(cx, cy + 20, '窑洞里', 'bold', 30, INK, 'mm')
    c.arrow(cx, 560, cx, 430, INK, 3, 14)
    c.arrow(cx, 560, cx, 650, INK, 3, 14)
    c.text(cx + 30, 545, '顶上几米厚的黄土', 'bold', 24, INK, 'lm')
    mon = ['1 月', '4 月', '7 月', '10 月']
    m = mon[int((yr % 1) * 4)]
    c.rect(1380, 200, 1860, 400, fill=SHEET, r=12)
    c.text(1620, 240, f'{m}（示意）', 'bold', 26, INK, 'mm')
    c.text(1420, 300, '外面', 'sans', 24, INK, 'lm')
    c.rect(1520, 290, 1520 + 300 * outside, 312, fill=temp_col(outside))
    c.text(1420, 360, '窑洞里', 'sans', 24, INK, 'lm')
    c.rect(1520, 350, 1520 + 300 * inside, 372, fill=temp_col(inside))
    caps(c, t, [(0, 7, '黄土高原上，夏天晒、冬天冻，一年里外面的温度差好几十度'),
                (7.2, 14, '窑洞挖进几米厚的黄土里，土把外面的冷热慢慢吸住、慢慢放出来'),
                (14.2, 22, '于是窑洞里冬天不太冷、夏天不太热：土就像一块很大的「温度缓冲垫」')], y=1010)


# ---------------------------------------------------------------- B84 弹棉花
def b84_bow(c, t, i):
    corner_tag(c, 'B84 · 弦一振，纤维就散开')
    c.text(60, 96, '拨一下绷紧的弦，它来回振得飞快，一下下把结块的纤维挑开', 'serif', 40, INK)
    c.line([(200, 300), (1100, 300)], (150, 110, 70), 16)
    c.line([(200, 300), (220, 560)], (150, 110, 70), 12)
    c.line([(1100, 300), (1080, 560)], (150, 110, 70), 12)
    period = 0.9
    ph = (t % period) / period
    amp = 46 * math.exp(-ph * 3.5)
    pts = []
    for j in range(61):
        u = j / 60
        y = 560 + amp * math.sin(math.pi * u) * math.cos(t * 40)
        pts.append((220 + 860 * u, y))
    c.line(pts, STRING, 4)
    rnd = random.Random(7)
    fluff = min(1.0, t / 18)
    for k in range(160):
        x = rnd.uniform(380, 920)
        base = rnd.uniform(620, 760)
        rise = rnd.uniform(0, 160) * fluff
        ang = rnd.uniform(0, math.pi)
        y = base - rise
        L = rnd.uniform(10, 30)
        c.line([(x, y), (x + L * math.cos(ang), y + L * math.sin(ang) * 0.5)], COTTON, 2)
    c.rect(360, 760, 940, 800, fill=mix(BG, COTTON, 0.55 - 0.3 * fluff), r=10)
    c.text(650, 860, '压紧的棉块 → 蓬松的棉', 'sans', 24, MUTED, 'mm')
    c.rect(1260, 260, 1840, 640, fill=SHEET, r=14)
    c.text(1550, 300, '一秒钟振多少下？', 'bold', 26, INK, 'mm')
    c.text(1300, 380, '弦松：振得慢、幅度大', 'sans', 24, INK, 'lm')
    c.text(1300, 440, '弦紧：振得快、声音高', 'sans', 24, INK, 'lm')
    c.text(1300, 520, '每振一次，就挑一下纤维', 'bold', 24, SPARK, 'lm')
    c.text(1300, 580, '「嘣嘣」声就是弦在振', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '弹棉花的人用木槌一敲弓弦，弦就嗡嗡地振起来'),
                (7.2, 14, '弦贴着棉花来回振，每振一下，就把缠在一起的纤维挑起一点、甩开一点'),
                (14.2, 22, '一秒钟振上百下，压得硬邦邦的旧棉絮，就一点点变回蓬松的棉花（以实测为准）')], y=1010)


def b84_tension(c, t, i):
    corner_tag(c, 'B84 · 绷得越紧，振得越快')
    c.text(60, 96, '同一根弦：越紧振得越快，声音越高；越长振得越慢，声音越低', 'serif', 40, INK)
    rows = [('松', 1.0, 1.0), ('紧', 2.0, 1.0), ('紧、短一半', 2.0, 0.5)]
    for k, (nm, T, L) in enumerate(rows):
        y = 320 + k * 200
        f = math.sqrt(T) / L
        x0 = 300
        x1 = x0 + 900 * L
        c.rect(x0 - 16, y - 40, x0, y + 40, fill=(150, 110, 70))
        c.rect(x1, y - 40, x1 + 16, y + 40, fill=(150, 110, 70))
        pts = []
        for j in range(81):
            u = j / 80
            pts.append((x0 + (x1 - x0) * u, y + 36 * math.sin(math.pi * u) * math.cos(t * 6 * f)))
        c.line(pts, STRING, 4)
        c.text(160, y, nm, 'bold', 26, INK, 'mm')
        c.text(1500, y, f'频率 × {f:.1f}', 'mono', 28, SPARK, 'lm')
    caps(c, t, [(0, 7, '同一根橡皮筋，松松地绷着，拨一下：慢慢地晃，声音低'),
                (7.2, 14, '绷紧一些，振得更快，声音也高了：这和 B65 古琴调弦是一回事'),
                (14.2, 22, '弦短一半，又快一倍。弹棉弓的弦绷得很紧，振得快，挑得才细（示意比例）')], y=1010)


# ---------------------------------------------------------------- B85 香篆钟
def b85_burn(c, t, i):
    corner_tag(c, 'B85 · 粗细一样，烧得一样快')
    c.text(60, 96, '一根香只在最前头那一点点阴燃；截面一样，每分钟烧掉的长度就差不多', 'serif', 40, INK)
    L0 = 600
    rate = 22
    for k in range(3):
        x = 380 + k * 300
        burnt = min(L0 - 40, rate * t * (1 + 0.03 * (k - 1)))
        top = 840 - L0 + burnt
        c.rect(x - 70, 840, x + 70, 910, fill=(110, 105, 100), r=10)
        c.line([(x, 840), (x, top)], (160, 110, 70), 8)
        c.ellipse(x, top, 7, 7, fill=EMBER)
        for j in range(6):
            s = (t * 0.7 + j / 6) % 1
            c.ellipse(x + 20 * math.sin(s * 8 + k), top - 30 - s * 200, 6 + 8 * s, 6 + 8 * s, fill=mix(BG, SMOKE, 0.6 * (1 - s)))
        c.text(x, 940, f'第 {k + 1} 根', 'sans', 20, MUTED, 'mm')
    c.rect(1280, 240, 1840, 760, fill=SHEET, r=14)
    c.text(1560, 280, '烧掉的长度（示意）', 'bold', 24, INK, 'mm')
    gx0, gy0, gx1, gy1 = 1330, 700, 1800, 330
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    pts = [(gx0 + (gx1 - gx0) * u / 22, gy0 - (gy0 - gy1) * min(1, rate * u / (L0 - 40))) for u in [j * t / 40 for j in range(41)]]
    c.line(pts, GREEN, 4)
    c.text(1560, 735, '时间 →', 'sans', 20, MUTED, 'mm')
    c.text(1340, 360, '一条直线：烧得匀', 'sans', 22, GREEN, 'lm')
    caps(c, t, [(0, 7, '点着的香不起火苗，只有最前头一小段在慢慢阴燃'),
                (7.2, 14, '同样的香粉、同样粗细，每分钟烧掉的长度几乎一样：画出来是一条直线'),
                (14.2, 22, '只要知道一分钟烧几毫米，香就成了一把能读时间的尺子（以实测为准）')], y=1010)


def b85_seal(c, t, i):
    corner_tag(c, 'B85 · 把一根长香盘成「篆」')
    c.text(60, 96, '把香粉压成盘绕的长线，按刻度一格格烧过去：一盘香，就是一夜的钟', 'serif', 40, INK)
    cx, cy = 640, 600
    pts = []
    n = 400
    for j in range(n + 1):
        u = j / n
        a = u * 2 * math.pi * 4.5
        r = 40 + 280 * u
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    c.ellipse(cx, cy, 340, 340, fill=ASH)
    c.line(pts, (160, 110, 70), 10)
    p = min(1.0, t / 20)
    k = int(p * n)
    if k > 1:
        c.line(pts[:k + 1], (210, 205, 195), 10)
    ex, ey = pts[k]
    c.ellipse(ex, ey, 9, 9, fill=EMBER)
    for m in range(9):
        j = int(n * m / 8)
        mx, my = pts[j]
        c.ellipse(mx, my, 6, 6, fill=SPARK if j <= k else MUTED)
    c.rect(1180, 260, 1840, 760, fill=SHEET, r=14)
    c.text(1510, 300, '刻度：每一格约一个时辰（示意）', 'bold', 24, INK, 'mm')
    hrs = int(p * 8)
    c.text(1510, 420, f'已烧过 {hrs} 格', 'mono', 40, SPARK, 'mm')
    c.text(1510, 520, '盘起来：长香不占地方', 'sans', 24, INK, 'mm')
    c.text(1510, 580, '一路烧过去：不会熄、不会跳', 'sans', 24, INK, 'mm')
    c.text(1510, 660, '宋代人用它在夜里计时（拍摄前核对）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '把香粉用模子压在香灰上，压成一条首尾相连、盘来绕去的长线，像篆字'),
                (7.2, 14, '从一头点着，火点沿着线一路往里烧，路上做好刻度'),
                (14.2, 22, '烧到哪一格，就过了多少时间。和 B13 的漏刻一样，靠的都是「匀速」')], y=1010)


CLIPS = {
 'B83_分层': (b83_layers, 22), 'B83_一年': (b83_cave, 22),
 'B83_片头': (titles.opening(BSER, VOL22, SB22, 3, '黄土高原窑洞'), 7),
 'B83_片尾': (titles.closing(BSER, VOL22, SB22, 3, '下集：弹棉弓一弹，结块的棉花为什么就蓬松了？'), 7),
 'B84_弓弦': (b84_bow, 22), 'B84_松紧': (b84_tension, 22),
 'B84_片头': (titles.opening(BSER, VOL22, SB22, 4, '元代棉纺推广 · 明《天工开物》'), 7),
 'B84_片尾': (titles.closing(BSER, VOL22, SB22, 4, '下集：一盘香，怎么当钟用？'), 7),
 'B85_匀速': (b85_burn, 22), 'B85_香篆': (b85_seal, 22),
 'B85_片头': (titles.opening(BSER, VOL22, SB22, 5, '宋代香篆计时'), 7),
 'B85_片尾': (titles.closing(BSER, VOL22, SB22, 5, '下集：冰为什么那么滑？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
