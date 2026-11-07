"""第二十三季（第八层：大工程）第二批：E125 海水淡化、E126 盾构隧道、E127 抗风阻尼器 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s23a import S23A, SER23, VOL23, WATER, WATER_L, CONC, GROUND

SALT = (240, 240, 245)
FILM = (200, 220, 235)
SUNC = (250, 210, 90)
VAPOR = (180, 200, 230)
SAND = (200, 170, 110)
SAND_D = (165, 135, 85)
STEEL = (160, 165, 175)
RING = (150, 150, 155)
BUILD = (120, 135, 160)
MASS = (200, 170, 90)


# ---------------------------------------------------------------- E125 海水淡化
def e125_still(c, t, i):
    corner_tag(c, '第 125 集 · 太阳把水「搬」出来')
    c.text(60, 96, '太阳晒热盐水，水变成水汽飞走，盐留在原地；水汽碰到凉的膜，又凝成淡水', 'serif', 40, INK)
    cx, base = 760, 860
    c.ellipse(260, 230, 50, 50, fill=SUNC)
    for k in range(8):
        a = k * math.pi / 4
        c.line([(260 + 62 * math.cos(a), 230 + 62 * math.sin(a)), (260 + 82 * math.cos(a), 230 + 82 * math.sin(a))], SUNC, 4)
    c.text(260, 330, '（别直视太阳）', 'sans', 20, MUTED, 'mm')
    c.poly([(cx - 420, base - 220), (cx + 420, base - 220), (cx + 340, base), (cx - 340, base)], (210, 210, 215))
    c.poly([(cx - 400, base - 120), (cx + 400, base - 120), (cx + 340, base - 4), (cx - 340, base - 4)], WATER)
    rnd = random.Random(1)
    for k in range(40):
        c.ellipse(rnd.uniform(cx - 330, cx + 330), rnd.uniform(base - 100, base - 15), 3, 3, fill=SALT)
    c.rect(cx - 70, base - 145, cx + 70, base - 10, fill=(70, 75, 85), outline=(220, 225, 230), width=3, r=6)
    fill = min(1.0, t / 20)
    c.rect(cx - 64, base - 16 - 90 * fill, cx + 64, base - 16, fill=WATER_L)
    sag = 60
    c.line([(cx - 440, base - 230), (cx, base - 230 + sag), (cx + 440, base - 230)], FILM, 4)
    c.ellipse(cx, base - 230 + sag - 10, 18, 10, fill=(200, 190, 140))
    c.text(cx + 460, base - 240, '保鲜膜（凉）', 'sans', 22, FILM, 'lm')
    for k in range(14):
        s = (t * 0.35 + k / 14) % 1
        x = cx - 320 + (k * 47) % 640
        if abs(x - cx) < 90:
            continue
        y = base - 125 - 40 * s
        c.ellipse(x, y, 5, 5, fill=mix(WATER, VAPOR, 1 - s))
    for k in range(6):
        s = (t * 0.25 + k / 6) % 1
        u = (k - 2.5) / 2.5
        x = cx + u * 380 * (1 - s)
        y = base - 230 + sag * (1 - abs(x - cx) / 440) + 8
        c.ellipse(x, y, 6, 8, fill=WATER_L)
    c.text(cx, base + 40, '浓盐水', 'sans', 22, MUTED, 'mm')
    c.text(cx + 90, base - 290, '中间小杯接到的淡水', 'bold', 22, WATER_L, 'lm')
    c.arrow(cx + 85, base - 285, cx + 40, base - 120, WATER_L, 2, 10)
    c.rect(1380, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 340, '谁走了，谁留下', 'bold', 26, INK, 'mm')
    c.text(1420, 420, '水：变成水汽飞走 ✓', 'sans', 24, INK, 'lm')
    c.text(1420, 480, '盐：飞不起来，留在碗里', 'sans', 24, INK, 'lm')
    c.text(1420, 560, '接到的水不喝，只做检验', 'sans', 22, NRED, 'lm')
    caps(c, t, [(0, 7, '太阳晒着一碗浓盐水，水慢慢变成看不见的水汽飞起来'),
                (7.2, 14, '盐溶在水里，却飞不起来，留在碗底；水汽碰到上面凉凉的保鲜膜，又凝成水珠'),
                (14.2, 22, '水珠顺着膜流到最低处，滴进中间的杯子：这就是蒸馏，一杯淡水（我们只检验，不喝）')], y=1010)


def e125_membrane(c, t, i):
    corner_tag(c, '第 125 集 · 用力把水「挤」过去')
    c.text(60, 96, '一层孔极小的膜：水分子挤得过去，盐挤不过去；可得用很大的压力推', 'serif', 40, INK)
    mx = 960
    c.rect(mx - 8, 240, mx + 8, 840, fill=(110, 115, 125))
    for k in range(25):
        y = 260 + k * 23
        c.rect(mx - 8, y, mx + 8, y + 5, fill=BG)
    c.rect(200, 240, mx - 8, 840, fill=mix(BG, WATER, 0.6))
    c.rect(mx + 8, 240, 1720, 840, fill=mix(BG, WATER_L, 0.4))
    push = 0.5 + 0.5 * math.sin(t * 0.8)
    px = 260 + 60 * push
    c.rect(px - 40, 240, px, 840, fill=STEEL)
    c.arrow(px - 160, 540, px - 50, 540, NRED, 8, 22)
    c.text(px - 120, 480, '加压', 'bold', 28, NRED, 'mm')
    rnd = random.Random(7)
    for k in range(60):
        x0 = rnd.uniform(px + 30, mx - 40)
        y0 = rnd.uniform(270, 810)
        is_salt = k % 3 == 0
        if is_salt:
            jx = 6 * math.sin(t * 3 + k)
            c.ellipse(x0 + jx, y0, 11, 11, fill=SALT)
            c.ellipse(x0 + jx, y0, 5, 5, fill=(160, 160, 170))
        else:
            s = ((t * 0.12) + k * 0.037) % 1
            x = x0 + (1700 - x0) * s
            if x > mx - 10 and x < mx + 10:
                pass
            c.ellipse(x, y0, 6, 6, fill=WATER_L)
    c.text(560, 880, '海水：水分子 + 盐', 'sans', 24, INK, 'mm')
    c.text(1340, 880, '淡水：只剩水分子', 'sans', 24, INK, 'mm')
    c.text(mx, 210, '反渗透膜（孔比头发丝细几万倍，示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '现在的大型海水淡化厂，多用一种特殊的膜：孔小到盐挤不过去'),
                (7.2, 14, '可是水不会自己往盐少的那边跑，反而想往盐多的那边钻，所以要用很大的压力推'),
                (14.2, 22, '推得越用力，出水越多，也越费电：淡水里藏着的，是推它过去的电')], y=1010)


# ---------------------------------------------------------------- E126 盾构隧道
def e126_shield(c, t, i):
    corner_tag(c, '第 126 集 · 边挖、边顶、边装')
    c.text(60, 96, '前面刀盘转着削土，钢壳顶住四周不让塌，后面一圈圈装上管片', 'serif', 40, INK)
    top, bot = 260, 900
    c.rect(0, top, 1920, bot, fill=SAND)
    rnd = random.Random(3)
    for k in range(120):
        c.ellipse(rnd.uniform(0, 1920), rnd.uniform(top, bot), 3, 3, fill=SAND_D)
    c.rect(0, top - 40, 1920, top, fill=mix(BG, WATER, 0.7))
    c.text(960, top - 20, '河水', 'sans', 22, INK, 'mm')
    adv = 400 + 50 * t
    cy, R = 600, 170
    c.rect(80, cy - R, adv - 260, cy + R, fill=BG)
    nring = int((adv - 260 - 80) / 60)
    for k in range(nring):
        x = 80 + k * 60
        c.rect(x, cy - R, x + 56, cy - R + 26, fill=RING)
        c.rect(x, cy + R - 26, x + 56, cy + R, fill=RING)
    c.text(max(200, (adv - 260) / 2 + 40), cy, '管片拼成的隧道', 'sans', 22, MUTED, 'mm')
    c.rect(adv - 260, cy - R - 6, adv, cy + R + 6, fill=STEEL, r=6)
    c.rect(adv - 250, cy - R + 20, adv - 10, cy + R - 20, fill=mix(STEEL, BG, 0.5))
    for k in range(3):
        c.arrow(adv - 240, cy - 80 + k * 80, adv - 300, cy - 80 + k * 80, SPARK, 3, 10)
    c.text(adv - 130, cy + R + 40, '盾壳', 'bold', 24, INK, 'mm')
    c.rect(adv, cy - R, adv + 30, cy + R, fill=(120, 120, 125))
    for k in range(6):
        a = t * 2 + k * math.pi / 3
        y = cy + (R - 20) * math.sin(a)
        c.line([(adv + 30, y), (adv + 50, y)], INK, 6)
    c.text(adv + 60, cy - R - 30, '刀盘（一直在转）', 'bold', 22, INK, 'lm')
    for k in range(10):
        s = (t * 0.8 + k / 10) % 1
        c.ellipse(adv - 20 - 400 * s, cy + 100 + 20 * math.sin(k), 6, 6, fill=SAND_D)
    caps(c, t, [(0, 7, '盾构机最前面是一个大圆刀盘，一边转一边把前面的泥沙削下来'),
                (7.2, 14, '后面紧跟着一个钢做的圆筒，叫盾壳，把四周的土顶住，人在里面干活不怕塌'),
                (14.2, 22, '盾壳往前推一点，身后就拼上一圈混凝土管片：一圈接一圈，隧道就长出来了')], y=1010)


def e126_arch(c, t, i):
    corner_tag(c, '第 126 集 · 为什么是圆的')
    c.text(60, 96, '四周的土从各个方向压过来；圆环把压力沿着一圈传开，哪儿都不吃亏', 'serif', 40, INK)
    for k, (nm, shape) in enumerate((('方形', 'sq'), ('圆形', 'ci'))):
        cx, cy = 540 + k * 840, 580
        c.rect(cx - 340, cy - 300, cx + 340, cy + 300, fill=SAND)
        n = 16
        for j in range(n):
            a = j * 2 * math.pi / n
            ox, oy = cx + 300 * math.cos(a), cy + 280 * math.sin(a)
            ix, iy = cx + 210 * math.cos(a), cy + 200 * math.sin(a)
            c.arrow(ox, oy, ix, iy, NRED, 3, 10)
        if shape == 'sq':
            bend = 18 * (0.5 + 0.5 * math.sin(t * 1.5)) * min(1, t / 6)
            pts = [(cx - 150, cy - 150), (cx, cy - 150 + bend), (cx + 150, cy - 150), (cx + 150 - bend, cy), (cx + 150, cy + 150),
                   (cx, cy + 150 - bend), (cx - 150, cy + 150), (cx - 150 + bend, cy)]
            c.poly(pts, BG)
            c.line(pts + [pts[0]], RING, 14)
            c.text(cx, cy, '平的一边被压弯', 'sans', 22, NRED, 'mm')
        else:
            c.ellipse(cx, cy, 160, 160, fill=BG, outline=RING, width=14)
            c.text(cx, cy, '一圈都在受压', 'sans', 22, GREEN, 'mm')
        c.text(cx, cy - 340, nm, 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '地下的隧道，上下左右都被土和水压着'),
                (7.2, 14, '方的隧道，平平的一边最容易被压弯；圆的隧道，压力沿着一圈传开，处处都在被「挤」'),
                (14.2, 22, '混凝土最不怕挤：所以隧道、拱桥都爱做成圆的、拱的（第 63 集钢筋混凝土）')], y=1010)


# ---------------------------------------------------------------- E127 抗风阻尼器
def _tower(c, x, base, H, sway, col=BUILD):
    pts = []
    n = 12
    for j in range(n + 1):
        h = H * j / n
        dx = sway * (h / H) ** 2
        pts.append((x + dx, base - h))
    for j in range(n):
        (x0, y0), (x1, y1) = pts[j], pts[j + 1]
        c.poly([(x0 - 60, y0), (x0 + 60, y0), (x1 + 60, y1), (x1 - 60, y1)], col)
    return pts[-1]


def e127_damper(c, t, i):
    corner_tag(c, '第 127 集 · 和楼反着晃的大球')
    c.text(60, 96, '同一阵风：没有阻尼器的楼晃好久；挂了大摆的楼，摆替它晃，很快就停', 'serif', 40, INK)
    base = 900
    H = 600
    w = 2.0
    a1 = 120 * math.exp(-t / 14) * math.sin(w * t)
    a2 = 120 * math.exp(-t / 3) * math.sin(w * t)
    c.line([(80, base), (1840, base)], GROUND, 6)
    top1 = _tower(c, 520, base, H, a1)
    top2 = _tower(c, 1360, base, H, a2)
    phase = w * t - math.pi / 2
    mamp = 60 * (1 - math.exp(-t / 2)) * math.exp(-t / 10)
    mx = top2[0] + mamp * math.sin(phase)
    py = top2[1] + 60
    c.line([(top2[0], top2[1] + 10), (mx, py + 80)], INK, 3)
    c.ellipse(mx, py + 80, 34, 34, fill=MASS)
    c.text(520, 220, '没有阻尼器', 'bold', 28, INK, 'mm')
    c.text(1360, 220, '楼顶挂一个大摆', 'bold', 28, INK, 'mm')
    c.text(520, 950, f'楼顶晃 {abs(a1) / 10:.1f}（示意）', 'mono', 22, NRED, 'mm')
    c.text(1360, 950, f'楼顶晃 {abs(a2) / 10:.1f}（示意）', 'mono', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '风一推，高楼就像一根插在地上的尺子，左右来回晃'),
                (7.2, 14, '楼顶挂一个很重的摆，摆的快慢和楼一样：楼往右，它偏偏往左'),
                (14.2, 22, '它一直和楼「顶着干」，把楼晃动的力气吸到自己身上，再慢慢消耗掉（台北 101 的大球就是这样，拍摄前核对）')], y=1010)


def e127_tuned(c, t, i):
    corner_tag(c, '第 127 集 · 摆的快慢要「调准」')
    c.text(60, 96, '摆得和楼一样快，减震最好；摆得太快或太慢，就几乎不起作用', 'serif', 40, INK)
    x0, x1, y0, y1 = 220, 1500, 820, 300
    c.line([(x0, y0), (x1, y0)], LINE, 3)
    c.line([(x0, y0), (x0, y1)], LINE, 3)
    c.text((x0 + x1) / 2, y0 + 50, '摆的快慢 ÷ 楼的快慢', 'sans', 24, MUTED, 'mm')
    c.text(x0 - 20, (y0 + y1) / 2, '楼晃\n多少', 'sans', 24, MUTED, 'rm')
    pts = []
    for j in range(201):
        r = 0.4 + 1.2 * j / 200
        d = 1.0 - 0.75 * math.exp(-((r - 1.0) / 0.12) ** 2)
        pts.append((x0 + (x1 - x0) * j / 200, y0 - 440 * d))
    c.line(pts, SPARK, 4)
    c.line([(x0 + (x1 - x0) * 0.5, y0), (x0 + (x1 - x0) * 0.5, y1)], mix(BG, GREEN, 0.6), 2)
    c.text(x0 + (x1 - x0) * 0.5, y1 - 20, '一样快', 'bold', 24, GREEN, 'mm')
    u = 0.5 + 0.45 * math.sin(t * 0.4)
    r = 0.4 + 1.2 * u
    d = 1.0 - 0.75 * math.exp(-((r - 1.0) / 0.12) ** 2)
    c.ellipse(x0 + (x1 - x0) * u, y0 - 440 * d, 14, 14, fill=NRED)
    c.rect(1560, 320, 1860, 620, fill=SHEET, r=12)
    c.text(1710, 360, '调线的长短', 'bold', 24, INK, 'mm')
    c.text(1710, 430, '线长 → 摆得慢', 'sans', 22, INK, 'mm')
    c.text(1710, 480, '线短 → 摆得快', 'sans', 22, INK, 'mm')
    c.text(1710, 560, '第 45 集摆钟', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '挂上去的摆，晃的快慢由线长决定，和第 45 集的摆钟一样'),
                (7.2, 14, '摆的快慢和楼一样时，它和楼「反着晃」得最起劲，楼晃得最少'),
                (14.2, 22, '摆太快或太慢，就跟楼对不上拍子，几乎没用：所以叫「调谐」质量阻尼器（曲线为示意）')], y=1010)


CLIPS = {
 'E125_蒸馏': (e125_still, 22), 'E125_反渗透': (e125_membrane, 22),
 'E125_片头': (titles.opening(SER23, VOL23, S23A, 3, '古代蒸馏取淡水 · 1960 年代反渗透膜'), 7),
 'E125_片尾': (titles.closing(SER23, VOL23, S23A, 3, '下集：在软软的泥沙里挖隧道，为什么不塌？'), 7),
 'E126_盾构': (e126_shield, 22), 'E126_圆环': (e126_arch, 22),
 'E126_片头': (titles.opening(SER23, VOL23, S23A, 4, '1825 年泰晤士河隧道 · 今天的盾构机'), 7),
 'E126_片尾': (titles.closing(SER23, VOL23, S23A, 4, '下集：摩天大楼顶上挂个大球，为什么就晃得少了？'), 7),
 'E127_阻尼': (e127_damper, 22), 'E127_调谐': (e127_tuned, 22),
 'E127_片头': (titles.opening(SER23, VOL23, S23A, 5, '2004 年台北 101 阻尼球'), 7),
 'E127_片尾': (titles.closing(SER23, VOL23, S23A, 5, '下集：高铁为什么能跑三百多公里还很平稳？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
