"""第四十八季（古法解密 21.0：作坊与街巷）第一批：B210 新莽铜卡尺、B211 步弓、B212 测深锤 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB48 = [('B210', '新莽铜卡尺'), ('B211', '步弓'), ('B212', '测深锤'), ('B213', '竹帘'), ('B214', '舞钻'),
        ('B215', '线装书'), ('B216', '杵臼'), ('B217', '粽子'), ('B218', '背篓'), ('B219', '抓子儿')]
VOL48 = '第四十八季 · 古法解密 21.0'
BRONZE = (180, 130, 70)
SAND = (215, 190, 140)
PEB = (140, 140, 135)
ROPE = (200, 170, 110)


def _ruler(c, x0, y, x1, mm=4.0):
    c.rect(x0, y, x1, y + 50, fill=mix(BG, BRONZE, 0.9), r=4)
    n = int((x1 - x0 - 20) / mm)
    for k in range(n + 1):
        x = x0 + 20 + k * mm
        h = 22 if k % 10 == 0 else (14 if k % 5 == 0 else 8)
        c.line([(x, y), (x, y + h)], mix(BG, INK, 0.8), 2)
        if k % 10 == 0:
            c.text(x, y + 36, str(k // 10), 'mono', 16, INK, 'mm')


# ---------------------------------------------------------------- B210 新莽铜卡尺
def b210_jaws(c, t, i):
    corner_tag(c, 'B210 · 两只爪夹住，距离就是粗细')
    c.text(60, 96, '固定尺一头有一只爪，活动尺套在上面带着另一只爪滑动：两爪夹住东西，两爪之间的距离就是它的粗细', 'serif', 36, INK)
    mm = 12.0
    x0, y = 300, 380
    _ruler(c, x0, y, 1650, mm)
    D = 23.0
    ph = min(1.0, (t % 11) / 6)
    gap = 60 * (1 - ph) + D * ph if ph < 1 else D
    gap = 60 - (60 - D) * ph
    fx = x0 + 20
    c.rect(fx - 30, y + 50, fx, y + 260, fill=mix(BG, BRONZE, 1.0))
    mx = fx + gap * mm
    c.rect(mx - 60, y - 20, mx + 120, y + 70, fill=mix(BG, BRONZE, 0.7), r=6)
    c.rect(mx, y + 50, mx + 30, y + 260, fill=mix(BG, BRONZE, 1.0))
    c.line([(mx, y - 20), (mx, y + 50)], NRED, 3)
    cx = fx + D * mm / 2
    c.ellipse(cx, y + 180, D * mm / 2, D * mm / 2, fill=mix(BG, (200, 170, 90), 0.9), outline=mix(BG, INK, 0.6), width=3)
    c.text(cx, y + 180, '铜钱', 'bold', 28, INK, 'mm')
    c.text(mx + 30, y - 60, f'{gap:.1f} 毫米', 'bold', 34, NRED, 'lm')
    if ph >= 1:
        c.text(960, 840, '两爪刚好贴住：读数 23 毫米（示意）', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 7, '直尺量圆东西：尺子的刻度和圆的边对不齐，总差一点'),
                (7.2, 14, '卡尺：固定爪顶住一边，推动活动爪，直到两爪都贴住'),
                (14.2, 22, '活动尺上的指针线，直接指着两爪之间的距离（示意，以实测为准）')], y=1010)


def b210_diam(c, t, i):
    corner_tag(c, 'B210 · 转一转，找最大的读数')
    c.text(60, 96, '圆的东西，卡在边上量出来偏小；转一转、挪一挪，找到最大的读数，那就是直径', 'serif', 36, INK)
    cx, cy, R = 760, 560, 220
    c.ellipse(cx, cy, R, R, fill=mix(BG, (200, 170, 90), 0.8), outline=mix(BG, INK, 0.6), width=3)
    off = R * 0.9 * math.cos(t * 0.5) * (1 - min(1.0, max(0.0, (t - 14) / 4)))
    half = math.sqrt(max(0.0, R * R - off * off))
    y = cy + off
    c.line([(cx - half, y), (cx + half, y)], NRED, 5)
    c.rect(cx - half - 30, y - 60, cx - half, y + 60, fill=mix(BG, BRONZE, 1.0))
    c.rect(cx + half, y - 60, cx + half + 30, y + 60, fill=mix(BG, BRONZE, 1.0))
    val = 2 * half / (2 * R) * 23
    c.text(1500, 480, f'读数：{val:.1f} 毫米', 'bold', 40, NRED, 'mm')
    c.text(1500, 560, '最大值 = 直径', 'bold', 30, GREEN, 'mm')
    c.text(1500, 620, '（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '两爪如果卡在铜钱靠边的地方，量出来的只是一条短弦'),
                (7.2, 14, '慢慢挪动，读数变大又变小'),
                (14.2, 22, '最大的那个读数，两爪正好卡在最宽处：就是直径')], y=1010)


# ---------------------------------------------------------------- B211 步弓
def b211_flip(c, t, i):
    corner_tag(c, 'B211 · 两脚距离固定，翻一次一步')
    c.text(60, 96, '步弓像一把大圆规，两脚之间的距离是固定的：一只脚踩住，另一只脚翻过去，每翻一次就是同样长的一步', 'serif', 36, INK)
    gy = 760
    c.rect(0, gy, W, gy + 20, fill=mix(BG, (150, 120, 80), 0.7))
    step = 260
    n = int(t / 2.2) % 5
    ph = (t / 2.2) % 1
    base = 200 + (n + 1) * step
    for k in range(int((base - 200) / step) + 1):
        x = 200 + k * step
        c.line([(x, gy - 10), (x, gy + 30)], SPARK, 4)
        c.text(x, gy + 56, str(k), 'mono', 22, SPARK, 'mm')
    fx2 = base - step * math.cos(math.pi * ph)
    fy2 = gy - 40 * math.sin(math.pi * ph)
    ax, ay = (base + fx2) / 2, gy - 380
    c.line([(base, gy), (ax, ay)], mix(BG, WOOD, 1.0), 14)
    c.line([(fx2, fy2), (ax, ay)], mix(BG, WOOD, 1.0), 14)
    c.line([(base, gy), (fx2, fy2)], mix(BG, ROPE, 1.0), 3)
    c.ellipse(base, gy, 12, 12, fill=GREEN)
    c.text(base, gy - 30, '踩住', 'bold', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '两脚之间拉一根绳子，张开的宽度就固定了'),
                (7.2, 14, '一只脚踩住不动，另一只脚翻过去落地'),
                (14.2, 22, '再换脚翻……数一数翻了几次，乘以一步的长度，就是总长')], y=1010)


def b211_error(c, t, i):
    corner_tag(c, 'B211 · 人走一步长短不一')
    c.text(60, 96, '人走路，一步大一步小，三个人量同一段路，数出来的步数都不一样；步弓的每一步都一样长', 'serif', 36, INK)
    random.seed(11)
    rows = [('步弓', [50] * 18, GREEN)]
    for nm in ['甲', '乙', '丙']:
        base = random.choice([55, 62, 70])
        rows.append((nm, [base + random.uniform(-9, 9) for _ in range(20)], NRED))
    total = 900
    sc = 1500 / total
    k = min(1.0, t / 14)
    for j, (nm, steps, col) in enumerate(rows):
        y = 300 + j * 140
        c.text(170, y, nm, 'bold', 28, col, 'rm')
        c.line([(200, y + 30), (200 + total * sc, y + 30)], LINE, 3)
        x = 0
        cnt = 0
        for s in steps:
            if x + s > total * k + 0.01:
                break
            c.line([(200 + (x + s) * sc, y + 10), (200 + (x + s) * sc, y + 50)], col, 4)
            x += s
            cnt += 1
        c.text(1760, y + 30, f'{cnt} 步', 'bold', 26, col, 'lm')
    caps(c, t, [(0, 7, '同一段 9 米的路'),
                (7.2, 14, '三个人走，步子有大有小，数出来的步数都不一样'),
                (14.2, 22, '步弓每一步都是一样的 50 厘米：谁来量都一样（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B212 测深锤
def b212_knots(c, t, i):
    corner_tag(c, 'B212 · 重锤拉直绳子，数结读深度')
    c.text(60, 96, '绳子每隔一段打一个结：重锤沉到底、绳子一松就停，数一数水面以下有几个结，就知道水有多深', 'serif', 36, INK)
    surf = 360
    bottom = 860
    c.rect(0, surf, W, bottom, fill=mix(BG, (110, 120, 90), 0.5))
    c.rect(0, bottom, W, 960, fill=mix(BG, SAND, 0.9))
    c.rect(400, surf - 80, 1200, surf - 10, fill=mix(BG, WOOD, 0.9), r=12)
    ph = min(1.0, (t % 22) / 10)
    sx = 900
    wy = surf - 10 + (bottom - 30 - (surf - 10)) * ph
    c.line([(sx, 200), (sx, wy)], mix(BG, ROPE, 1.0), 4)
    gap = 50
    k = 0
    y = 220
    under = 0
    while y < wy:
        c.ellipse(sx, y, 8, 8, fill=mix(BG, ROPE, 1.0))
        if y > surf:
            under += 1
        y += gap
    c.rect(sx - 28, wy, sx + 28, wy + 40, fill=mix(BG, PEB, 1.0), r=6)
    c.text(1300, 300, f'水面以下 {under} 个结', 'bold', 34, NRED, 'lm')
    c.text(1300, 360, f'≈ {under * 5} 厘米（每结 5 厘米，示意）', 'sans', 26, INK, 'lm')
    if ph >= 1:
        c.text(sx + 60, bottom - 60, '触底：绳子一松', 'bold', 26, GREEN, 'lm')
    caps(c, t, [(0, 7, '重锤把绳子拉得笔直，往下沉'),
                (7.2, 14, '一碰到底，手上的绳子一下子松了'),
                (14.2, 22, '数水面以下有几个结，乘以结的间距，就是水深（以实测为准）')], y=1010)


def b212_tallow(c, t, i):
    corner_tag(c, 'B212 · 锤底抹油，粘起水底')
    c.text(60, 96, '锤底挖一个小坑抹上油脂：沉到底一压，水底的沙子、泥或碎石就粘在上面，提上来一看就知道底下是什么', 'serif', 36, INK)
    random.seed(4)
    for j, (lab, col, rr) in enumerate([('沙底：粘起细沙', SAND, 5), ('石底：粘起碎石', PEB, 14)]):
        cx = 480 + j * 960
        bottom = 720
        c.rect(cx - 400, bottom, cx + 400, bottom + 160, fill=mix(BG, col, 0.7))
        for k in range(40):
            c.ellipse(cx + random.uniform(-390, 390), bottom + random.uniform(10, 150), rr, rr * 0.8, fill=mix(BG, col, 1.0))
        ph = (t % 11) / 11
        if ph < 0.4:
            wy = 300 + (bottom - 60 - 300) * (ph / 0.4)
        elif ph < 0.55:
            wy = bottom - 60
        else:
            wy = bottom - 60 - (bottom - 360) * ((ph - 0.55) / 0.45)
        c.line([(cx, 200), (cx, wy)], mix(BG, ROPE, 1.0), 4)
        c.rect(cx - 50, wy, cx + 50, wy + 60, fill=mix(BG, (110, 110, 115), 1.0), r=8)
        c.rect(cx - 36, wy + 50, cx + 36, wy + 60, fill=mix(BG, (240, 230, 180), 1.0))
        if ph >= 0.55:
            random.seed(20 + j)
            for k in range(8 if rr > 8 else 22):
                c.ellipse(cx + random.uniform(-32, 32), wy + 64 + random.uniform(0, 8), rr * 0.7, rr * 0.6, fill=mix(BG, col, 1.0))
        c.text(cx, 940, lab, 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '锤底抹一层油脂（实验用凡士林）'),
                (7.2, 14, '沉到底轻轻一压，底下的东西粘了上来'),
                (14.2, 22, '船工看粘起的是沙、是泥还是碎石，判断在哪一段河、能不能下锚')], y=1010)


CLIPS = {
 'B210_夹爪': (b210_jaws, 22), 'B210_直径': (b210_diam, 22),
 'B210_片头': (titles.opening(BSER, VOL48, SB48, 0, '新莽时期已有铜卡尺'), 7),
 'B210_片尾': (titles.closing(BSER, VOL48, SB48, 0, '下集：翻着走的木架子，能把地量准吗？'), 7),
 'B211_翻步': (b211_flip, 22), 'B211_误差': (b211_error, 22),
 'B211_片头': (titles.opening(BSER, VOL48, SB48, 1, '明清丈量田地常用步弓'), 7),
 'B211_片尾': (titles.closing(BSER, VOL48, SB48, 1, '下集：看不见底的浑水，怎么量有多深？'), 7),
 'B212_读结': (b212_knots, 22), 'B212_粘底': (b212_tallow, 22),
 'B212_片头': (titles.opening(BSER, VOL48, SB48, 2, '古代船上用系绳的铅锤测水深'), 7),
 'B212_片尾': (titles.closing(BSER, VOL48, SB48, 2, '下集：挂一挂竹帘，为什么外面看不进屋？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
