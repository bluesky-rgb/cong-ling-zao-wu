"""第三十六季（古法解密 15.0：力、声、玩、软）收官：B159 毛毡 + 第三十六季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s36a import SB36, VOL36

WOOL = (235, 225, 200)
WOOL2 = (200, 120, 140)
COTTONC = (240, 240, 235)


# ---------------------------------------------------------------- B159 毛毡
def _fiber(c, x0, y, L, col, scales=True, dx=0):
    c.rect(x0 + dx, y - 14, x0 + dx + L, y + 14, fill=mix(BG, col, 0.9), r=14)
    if scales:
        for k in range(int(L / 40)):
            x = x0 + dx + 20 + k * 40
            c.poly([(x, y - 14), (x + 30, y - 14), (x + 34, y - 4)], mix(BG, mix(col, INK, 0.25), 0.95))
            c.poly([(x, y + 14), (x + 30, y + 14), (x + 34, y + 4)], mix(BG, mix(col, INK, 0.25), 0.95))


def b159_scales(c, t, i):
    corner_tag(c, 'B159 · 鳞片只能往一个方向滑')
    c.text(60, 96, '放大一根羊毛：表面一片片鳞片像屋瓦一样朝一个方向排；两根毛一搓，只能往前钻，退不回来', 'serif', 36, INK)
    c.rect(100, 230, 1000, 900, fill=SHEET, r=14)
    c.text(550, 270, '羊毛（显微镜下，示意）', 'sans', 22, MUTED, 'mm')
    _fiber(c, 160, 400, 780, WOOL)
    ph = t % 4
    dx = 60 * (ph / 2) if ph < 2 else 60 * (1 - (ph - 2) / 2) * 0 + 60
    step = int(t / 4) * 60
    _fiber(c, 160, 470, 600, WOOL2, True, min(200, step + (60 * ph / 2 if ph < 2 else 60)) - 60)
    c.arrow(760, 560, 860, 560, GREEN, 4, 12)
    c.text(810, 600, '往这边：顺着鳞片，能滑', 'sans', 20, GREEN, 'mm')
    c.arrow(400, 640, 300, 640, NRED, 4, 12)
    c.text(350, 680, '往回：被鳞片卡住', 'sans', 20, NRED, 'mm')
    c.text(550, 800, '一来一回地搓，毛只能越钻越深', 'bold', 24, SPARK, 'mm')
    c.rect(1080, 230, 1840, 900, fill=SHEET, r=14)
    c.text(1460, 270, '棉花（对照）', 'sans', 22, MUTED, 'mm')
    _fiber(c, 1140, 400, 640, COTTONC, False)
    _fiber(c, 1140, 470, 520, COTTONC, False, 40 * math.sin(t * 1.6))
    c.text(1460, 600, '表面光滑，来回都能滑', 'bold', 24, MUTED, 'mm')
    c.text(1460, 650, '搓不成毡', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '每根羊毛的表面，都覆着一片片小鳞片，像屋顶的瓦朝同一个方向排'),
                (7.2, 14, '两根毛贴在一起来回搓：往前走时顺着鳞片能滑，往回走时就被卡住'),
                (14.2, 22, '于是一来一回，毛只能越钻越深、越缠越紧；棉花没有鳞片，就搓不成毡（示意）')], y=1010)


def b159_shrink(c, t, i):
    corner_tag(c, 'B159 · 加肥皂温水搓，缩成一块毡')
    c.text(60, 96, '温水让鳞片张开，肥皂让毛更好滑动；一搓，千万根毛互相钻进去锁死，整片缩小变厚', 'serif', 36, INK)
    p = min(1.0, t / 16)
    for j, (lab, k_, note) in enumerate([('只加温水', 0.35, '还能撕开'), ('加肥皂温水', 1.0, '撕不开了')]):
        cx = 520 + j * 880
        s = 1 - 0.3 * k_ * p
        W = 520 * s
        c.rect(cx - W / 2, 560 - W / 2, cx + W / 2, 560 + W / 2, fill=mix(BG, WOOL2, 0.35 + 0.45 * k_ * p), r=12)
        r = random.Random(j)
        for q in range(140):
            x = cx + r.uniform(-W / 2 + 10, W / 2 - 10)
            y = 560 + r.uniform(-W / 2 + 10, W / 2 - 10)
            a = r.uniform(0, math.pi)
            L = 40 * (1 - 0.5 * k_ * p)
            c.line([(x - L * math.cos(a), y - L * math.sin(a)), (x + L * math.cos(a), y + L * math.sin(a))], mix(BG, WOOL2, 0.9), 2)
        c.text(cx, 870, lab, 'bold', 28, INK, 'mm')
        c.text(cx, 910, f'边长 {10 * s:.1f} 厘米 · {note if p > 0.9 else "搓着……"}', 'mono', 22, SPARK, 'mm')
    c.text(960, 960, '水温不超过 50 ℃；示意，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '两片同样的羊毛，一片只洒温水，一片洒加了肥皂的温水，都盖上纱网轻轻搓'),
                (7.2, 14, '有肥皂的那片，毛更容易互相滑动、钻进去，很快就粘成一片'),
                (14.2, 22, '越搓越小、越搓越硬，最后缩了两三成，用手撕也撕不开：这就是毡（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十六季特辑
OLD36 = [('榫卯', 'B7'), ('杠杆与滑轮组', '39'), ('搓麻绳', 'B101'), ('缆桩', 'B111'), ('悬索桥', '79'), ('羊皮筏子', 'B82'),
         ('指南车', 'B17'), ('自行车', '66'), ('鼓', 'B108'), ('回音壁', 'B66'), ('机翼', '86'), ('陀螺', 'B50'),
         ('蹴鞠', 'B79'), ('滚铁环', 'B120'), ('不倒翁', 'B51'), ('高跷', 'B113'), ('肥皂', '22'), ('豆腐点卤', 'B14'),
         ('纺锤', 'B70'), ('弹棉花', 'B84')]
NEW36 = [('楔子', 'B150', ['榫卯', '杠杆与滑轮组']), ('绳结', 'B151', ['搓麻绳', '缆桩']), ('溜索', 'B152', ['悬索桥', '羊皮筏子']),
         ('车辐', 'B153', ['指南车', '自行车']), ('木鱼', 'B154', ['鼓', '回音壁']), ('打水漂', 'B155', ['机翼', '陀螺']),
         ('捶丸', 'B156', ['蹴鞠', '滚铁环']), ('顶碗', 'B157', ['不倒翁', '高跷']), ('点茶', 'B158', ['肥皂', '豆腐点卤']),
         ('毛毡', 'B159', ['纺锤', '弹棉花'])]


def s36_graph(c, t, i):
    corner_tag(c, '第三十六季特辑 · 古法解密 15.0')
    c.text(60, 118, '力、声、玩、软：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD36):
        pos[name] = (340, 218 + k * 38)
    for k, (name, num, deps) in enumerate(NEW36):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十六季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW36):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD36:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW36):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十五季：力、声、玩、软，都是手边的小东西'),
                (8.2, 16, '榫卯和杠杆长出楔子，缆桩长出绳结，悬索桥长出溜索，自行车长出车辐，鼓长出木鱼'),
                (16.2, 24, '机翼和陀螺长出打水漂，滚铁环长出捶丸，不倒翁长出顶碗，肥皂长出点茶'),
                (24.2, 30, '最后，纺锤和弹棉花一起，长出了越搓越紧的毛毡')], y=1040)


CLIPS = {
 'B159_鳞片': (b159_scales, 22), 'B159_缩紧': (b159_shrink, 22),
 'B159_片头': (titles.opening(BSER, VOL36, SB36, 9, '游牧民族擀毡已有几千年'), 7),
 'B159_片尾': (titles.closing(BSER, VOL36, SB36, 9, '下集：第三十六季特辑 · 古法解密 15.0 回顾'), 7),
 'S36_依赖': (s36_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
