"""第五十四季（古法解密 24.0：衣与针线）第一批：B240 顶针、B241 腰机、B242 捣衣杵 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB54 = [('B240', '顶针'), ('B241', '腰机'), ('B242', '捣衣杵'), ('B243', '皂角'), ('B244', '浆衣'),
        ('B245', '火斗'), ('B246', '千层底'), ('B247', '回针'), ('B248', '樟木箱'), ('B249', '发簪')]
VOL54 = '第五十四季 · 古法解密 24.0'
SKIN = (235, 190, 160)
BRASS = (210, 175, 90)
CLOTH = (225, 220, 205)
THREAD = (200, 90, 90)
WEFT = (90, 150, 220)
WATER = (120, 170, 230)
DIRT = (140, 110, 70)
WOODC = (170, 125, 80)


# ---------------------------------------------------------------- B240 顶针
def b240_spread(c, t, i):
    corner_tag(c, 'B240 · 一小点的力摊到整个指腹')
    c.text(60, 96, '推针时针尾只有一小点：同样的力压在一小点上，手指受的压强很大；套上顶针，力被摊到整个指腹', 'serif', 36, INK)
    th = t > 7.2
    cx, cy = 960, 560
    c.ellipse(cx - 300, cy, 260, 150, fill=mix(BG, SKIN, 1.0))
    c.text(cx - 380, cy, '指腹', 'bold', 28, INK, 'mm')
    c.line([(cx + 40, cy), (cx + 700, cy)], mix(BG, (200, 200, 210), 1.0), 8)
    c.poly([(cx + 700, cy - 4), (cx + 740, cy), (cx + 700, cy + 4)], mix(BG, (200, 200, 210), 1.0))
    if th:
        c.arc(cx - 300, cy, 268, 158, -60, 60, mix(BG, BRASS, 1.0), 26)
        random.seed(2)
        for k in range(8):
            a = math.radians(-50 + k * 14)
            c.ellipse(cx - 300 + 268 * math.cos(a), cy + 158 * math.sin(a), 6, 6, fill=mix(BG, (150, 120, 60), 1.0))
        for k in range(7):
            y = cy - 120 + k * 40
            c.arrow(cx - 20, y, cx - 60, y, GREEN, 4, 12)
        c.text(cx - 300, cy + 230, '套上顶针：力摊开，不疼', 'bold', 28, GREEN, 'mm')
    else:
        c.arrow(cx + 60, cy, cx + 30, cy, NRED, 8, 20)
        c.ellipse(cx - 40, cy, 22, 22, fill=mix(BG, NRED, 0.6))
        c.text(cx - 300, cy + 230, '直接顶：力全压在一个小点上，疼', 'bold', 28, NRED, 'mm')
    caps(c, t, [(0, 7, '指腹直接顶着针尾推：针尾那一小点深深压进肉里'),
                (7.2, 14, '套上金属顶针：针尾压在硬硬的顶针上'),
                (14.2, 22, '顶针把力摊到整个指腹，推得动也不疼（竹签泡沫板实验，不用真针）')], y=1010)


def b240_dimple(c, t, i):
    corner_tag(c, 'B240 · 小坑卡住针尾')
    c.text(60, 96, '顶针表面密密麻麻全是小坑：光滑的表面一推，针尾就滑开；有小坑，针尾落进坑里卡住，力才推得出去', 'serif', 36, INK)
    for j, (lab, dimple) in enumerate([('光滑的表面', False), ('带小坑的表面', True)]):
        cx, cy = 560 + j * 800, 560
        c.rect(cx - 280, cy + 40, cx + 280, cy + 120, fill=mix(BG, BRASS, 1.0), r=10)
        if dimple:
            for k in range(9):
                c.ellipse(cx - 240 + k * 60, cy + 44, 16, 10, fill=mix(BG, (150, 120, 60), 1.0))
        slip = 0 if dimple else min(160, max(0, t - 3) * 40) % 200
        ang = math.radians(60)
        tipx, tipy = cx + slip, cy + 40
        c.line([(tipx, tipy), (tipx - 300 * math.cos(ang), tipy - 300 * math.sin(ang))], mix(BG, (200, 200, 210), 1.0), 10)
        c.arrow(tipx - 360 * math.cos(ang), tipy - 360 * math.sin(ang), tipx - 310 * math.cos(ang), tipy - 310 * math.sin(ang), INK, 5, 16)
        c.text(cx, cy + 200, lab + ('：针尾卡住' if dimple else '：针尾滑开'), 'bold', 28, GREEN if dimple else NRED, 'mm')
    caps(c, t, [(0, 7, '斜着推针时，光滑的金属面上针尾一用力就滑开'),
                (7.2, 14, '表面有一个个小坑，针尾落进坑里'),
                (14.2, 22, '卡住了就不打滑，力全用在推针上（放大镜看看真顶针）')], y=1010)


# ---------------------------------------------------------------- B241 腰机
def b241_tension(c, t, i):
    corner_tag(c, 'B241 · 往后一靠，经线绷紧')
    c.text(60, 96, '腰机没有木架子：经线一头拴在树上（门把手上），一头系在腰上；人往后一靠经线就绷紧，往前一倾就松开', 'serif', 36, INK)
    lean = 0.5 + 0.5 * math.sin(t * 0.8)
    x0, y0 = 260, 420
    bx = 1400 + 160 * lean
    sag = 160 * (1 - lean) ** 2
    for k in range(8):
        dy = (k - 3.5) * 10
        pts = [(x0 + (bx - x0) * u / 20, y0 + dy + sag * math.sin(math.pi * u / 20)) for u in range(21)]
        c.line(pts, mix(BG, CLOTH, 1.0), 3)
    c.rect(x0 - 30, y0 - 80, x0, y0 + 80, fill=mix(BG, WOODC, 1.0))
    c.text(x0 - 15, y0 - 110, '树（门把手）', 'sans', 22, MUTED, 'mm')
    # 人
    hx, hy = bx + 60 + 80 * lean, 330
    c.ellipse(hx, hy, 40, 40, fill=mix(BG, SKIN, 1.0))
    c.line([(hx, hy + 40), (bx + 40, 620)], mix(BG, (120, 150, 200), 1.0), 30)
    c.line([(bx + 40, 620), (bx + 260, 640), (bx + 280, 800)], mix(BG, (120, 150, 200), 1.0), 24)
    c.line([(bx, y0 - 40), (bx, y0 + 40)], mix(BG, WOODC, 1.0), 10)
    c.line([(bx, y0), (bx + 40, 600)], mix(BG, THREAD, 1.0), 4)
    tight = lean > 0.6
    c.text(960, 860, '往后靠：经线绷直' if tight else '往前倾：经线松了', 'bold', 30, GREEN if tight else NRED, 'mm')
    caps(c, t, [(0, 7, '经线一头系在门把手上，另一头绑在筷子上，筷子用布带拴在腰上'),
                (7.2, 14, '往后一靠，经线就绷得直直的；往前一倾，就松下来'),
                (14.2, 22, '松紧全靠腰来调：人的身体就是织布机的架子')], y=1010)


def b241_heddle(c, t, i):
    corner_tag(c, 'B241 · 综杆一提，纬线一穿就过')
    c.text(60, 96, '综杆从单数经线下面穿过：一提，一半经线升起让出一条缝，纬线一次穿过整排；再换另一半穿回来', 'serif', 36, INK)
    rows = min(7, int(t / 3.1) + 1)
    x0, x1 = 300, 1500
    xs = [x0 + 60 + k * 120 for k in range(10)]
    def warp(k, col, w):
        c.line([(xs[k], 220), (xs[k], 880)], col, w)
    # 先画全部经线（在下面的）
    for k in range(10):
        warp(k, mix(BG, CLOTH, 0.7), 8)
    for r in range(rows):
        y = 840 - r * 70
        prog = 1.0 if r < rows - 1 else min(1.0, (t % 3.1) / 2.0)
        c.line([(x0, y), (x0 + (x1 - x0) * prog, y)], mix(BG, WEFT, 1.0), 14)
        for k in range(10):
            if (k + r) % 2 == 0 and x0 + (x1 - x0) * prog > xs[k]:
                c.line([(xs[k], y - 12), (xs[k], y + 12)], mix(BG, CLOTH, 1.0), 10)
    phase = (rows - 1) % 2
    c.text(1650, 840 - (rows - 1) * 70, '纬线', 'bold', 26, WEFT, 'lm')
    c.text(960, 190, f'这一行：{"单数" if phase == 0 else "双数"}经线提起，纬线从下面穿过（俯视示意）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '提起综杆，单数经线一起升起，纬线从它们下面一穿就过'),
                (7.2, 14, '压紧以后，换双数经线升起，纬线穿回来'),
                (14.2, 22, '一上一下交替，经线纬线就交织成布（俯视示意）')], y=1010)


# ---------------------------------------------------------------- B242 捣衣杵
def b242_pump(c, t, i):
    corner_tag(c, 'B242 · 一挤一吸，水来回冲')
    c.text(60, 96, '泡湿的布一捶，水被压着从纤维缝里挤出去；木棒一抬，水又吸回来；一挤一吸，水来回冲走缝里的脏东西', 'serif', 36, INK)
    ph = (t * 1.2) % 1
    down = ph < 0.4
    squeeze = math.sin(min(1, ph / 0.4) * math.pi) if down else 0
    y0 = 600
    # 纤维
    for k in range(12):
        x = 360 + k * 100
        c.ellipse(x, y0, 40, 60 - 30 * squeeze, fill=mix(BG, CLOTH, 1.0))
    random.seed(3)
    left = max(0, 30 - int(t * 1.5))
    for k in range(left):
        x = 400 + k * 38 + random.uniform(-8, 8)
        c.ellipse(x, y0 + random.uniform(-20, 20), 8, 8, fill=mix(BG, DIRT, 1.0))
    for k in range(10):
        ox = 410 + k * 100
        if down:
            c.arrow(ox, y0, ox, y0 + 120 + 40 * squeeze, WATER, 4, 12)
        else:
            c.arrow(ox, y0 + 140, ox, y0 + 20, WATER, 4, 12)
    by = 340 + (180 * squeeze if down else 0)
    c.rect(500, by - 60, 1400, by, fill=mix(BG, WOODC, 1.0), r=30)
    c.text(960, 880, f'缝里还剩的泥：{left} 粒（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '木棒捶下去，纤维被压扁，缝里的水连同泥一起被挤出去'),
                (7.2, 14, '木棒抬起，纤维弹回来，又吸进一口清水'),
                (14.2, 22, '一挤一吸几十次，缝里的泥越来越少（示意）')], y=1010)


def b242_compare(c, t, i):
    corner_tag(c, 'B242 · 泡、捶、搓')
    c.text(60, 96, '三块抹了泥的布：只泡在水里，泥几乎还在；捶 100 下、搓 100 下，泥都少多了：要让水动起来才洗得掉', 'serif', 36, INK)
    res = [('只泡 5 分钟', 0.9), ('木棒捶 100 下', 0.25), ('手搓 100 下', 0.3)]
    k = min(2, int(t / 7.3))
    for j, (lab, left) in enumerate(res):
        cx = 400 + j * 560
        c.rect(cx - 180, 320, cx + 180, 680, fill=mix(BG, CLOTH, 1.0), r=8)
        a = left if j <= k else 1.0
        c.ellipse(cx, 500, 110, 90, fill=mix(mix(BG, CLOTH, 1.0), DIRT, a))
        c.text(cx, 740, lab, 'bold', 28, INK if j <= k else MUTED, 'mm')
        if j <= k:
            c.text(cx, 800, ['泥还在', '干净多了', '也干净了'][j], 'bold', 26, NRED if j == 0 else GREEN, 'mm')
    c.text(960, 230, '结果以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '第一块只泡在水里：水不动，泥还卡在纤维缝里'),
                (7.2, 14, '第二块在木板上捶 100 下：水来回冲，泥被带出来'),
                (14.2, 22, '第三块手搓 100 下：也是让水动起来；古人在河边捶，省力又不伤手')], y=1010)


CLIPS = {
 'B240_摊开': (b240_spread, 22), 'B240_小坑': (b240_dimple, 22),
 'B240_片头': (titles.opening(BSER, VOL54, SB54, 0, '汉代墓葬已出土铜顶针'), 7),
 'B240_片尾': (titles.closing(BSER, VOL54, SB54, 0, '下集：靠在腰上怎么织布？'), 7),
 'B241_绷紧': (b241_tension, 22), 'B241_综杆': (b241_heddle, 22),
 'B241_片头': (titles.opening(BSER, VOL54, SB54, 1, '河姆渡出土过腰机部件'), 7),
 'B241_片尾': (titles.closing(BSER, VOL54, SB54, 1, '下集：捶一捶衣服怎么就干净了？'), 7),
 'B242_挤吸': (b242_pump, 22), 'B242_对比': (b242_compare, 22),
 'B242_片头': (titles.opening(BSER, VOL54, SB54, 2, '「长安一片月，万户捣衣声」'), 7),
 'B242_片尾': (titles.closing(BSER, VOL54, SB54, 2, '下集：豆荚泡水怎么能洗油？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
