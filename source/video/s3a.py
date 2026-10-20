"""第三季第一批：E28 水车提水、E25 螺旋提水、E26 虹吸 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, wheel

WATER = mix(BG, FIELD, 0.75)
WOODC = (160, 118, 76)
BAMBOO = (170, 190, 120)

# ---------------------------------------------------------------- E28 水车提水
def e28_chain(c, t, i):
    corner_tag(c, '第 28 集 · 翻车')
    c.text(60, 96, '一节节木板，把水「刮」上田埂', 'serif', 40, INK)
    # river (low) and field (high)
    c.rect(0, 820, 760, 1080, fill=mix(BG, FIELD, 0.35))
    c.text(80, 860, '河', 'sans', 28, MUTED, 'lm')
    c.rect(1380, 430, 1920, 470, fill=(110, 90, 60))
    c.rect(1400, 400, 1920, 432, fill=mix(BG, FIELD, 0.35 + 0.3 * fade(t, 4, 18)))
    c.text(1880, 370, '田埂上的水渠', 'sans', 26, MUTED, 'rm')
    # inclined trough from (420, 900) to (1400, 430)
    x0, y0, x1, y1 = 420, 920, 1400, 440
    L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L; nx, ny = -uy, ux
    W = 70
    c.poly([(x0 + nx * W, y0 + ny * W), (x1 + nx * W, y1 + ny * W), (x1, y1), (x0, y0)], mix(BG, WOODC, 0.5))
    c.line([(x0 + nx * W, y0 + ny * W), (x1 + nx * W, y1 + ny * W)], WOODC, 6)
    # paddles moving up in the trough; return chain above
    sp = 90
    off = (t * 120) % sp
    n = int(L / sp) + 1
    for k in range(n):
        s = k * sp + off
        if s > L: continue
        px, py = x0 + ux * s, y0 + uy * s
        # water slug ahead of paddle (in trough)
        if s > 40 and s < L - 10:
            c.poly([(px + nx * W * 0.9, py + ny * W * 0.9), (px + ux * 60 + nx * W * 0.9, py + uy * 60 + ny * W * 0.9),
                    (px + ux * 60 + nx * W * 0.35, py + uy * 60 + ny * W * 0.35), (px + nx * W * 0.35, py + ny * W * 0.35)], WATER)
        c.line([(px - nx * 30, py - ny * 30), (px + nx * W, py + ny * W)], WOODC, 8)
        # return run (above)
        rs = L - s
        rx, ry = x0 + ux * rs - nx * 60, y0 + uy * rs - ny * 60
        c.line([(rx - nx * 10, ry - ny * 10), (rx + nx * 40, ry + ny * 40)], mix(BG, WOODC, 0.7), 6)
    c.line([(x0 - nx * 30, y0 - ny * 30), (x1 - nx * 30, y1 - ny * 30)], (90, 70, 50), 4)
    c.line([(x0 - nx * 60, y0 - ny * 60), (x1 - nx * 60, y1 - ny * 60)], (90, 70, 50), 4)
    # top sprocket with treadles
    a = t * 2.4
    cx, cy = x1 - nx * 30, y1 - ny * 30
    c.ellipse(cx, cy, 50, 50, outline=WOODC, width=8)
    for k in range(4):
        b = a + k * math.pi / 2
        c.line([(cx + 50 * math.cos(b), cy + 50 * math.sin(b)), (cx + 110 * math.cos(b), cy + 110 * math.sin(b))], WOODC, 10)
    c.text(cx + 40, cy - 150, '人踩踏板转动上轮', 'sans', 26, INK, 'mm')
    # pour
    for k in range(4):
        ph = (t * 1.5 + k / 4) % 1
        c.ellipse(x1 + 20 + ph * 30, y1 - 10 + ph * 20, 8, 8, fill=WATER)
    caps(c, t, [(0, 6, '一条斜放的木槽，一串用链子连起来的木板'),
                (6.2, 13, '踩动上面的轮子，木板在槽里往上走，每块板推着前面一小段水'),
                (13.2, 22, '水被一节节「刮」上来，倒进田埂上的渠里 —— 翻车，也叫龙骨水车')])

def e28_tube(c, t, i):
    corner_tag(c, '第 28 集 · 筒车')
    c.text(60, 96, '不用人踩：让河水自己把自己送上去', 'serif', 40, INK)
    cx, cy, R = 760, 560, 340
    c.rect(0, 760, 1920, 1080, fill=mix(BG, FIELD, 0.35))
    for k in range(6):
        ph = (t * 0.8 + k / 6) % 1
        c.arrow(200 + ph * 1400, 900 + (k % 3) * 40, 260 + ph * 1400, 900 + (k % 3) * 40, mix(BG, FIELD, 0.9), 3, 10)
    c.text(1880, 800, '河水流向 →', 'sans', 26, MUTED, 'rm')
    a = t * 0.35
    wheel(c, cx, cy, R, a, WOODC, 16)
    # tubes on rim
    for k in range(16):
        b = a + k * 2 * math.pi / 16
        x, y = cx + (R + 40) * math.cos(b), cy + (R + 40) * math.sin(b)
        tilt = b + 0.6
        ex, ey = x + 50 * math.cos(tilt), y + 50 * math.sin(tilt)
        c.line([(x, y), (ex, ey)], BAMBOO, 14)
        ang = math.atan2(math.sin(b), math.cos(b))
        full = (y > 700) or (-math.pi / 2 < ang < 0.3 and math.sin(b) < 0.95 and math.cos(b) > -0.2 and y < 760 and ang > -1.4)
        # full when on rising side (right side moving up) after dipping
        rising = math.cos(b) > 0
        if rising and y > cy - R * 0.9:
            c.line([(x, y), (x + 25 * math.cos(tilt), y + 25 * math.sin(tilt))], WATER, 10)
        # pouring near top
        if abs(b % (2 * math.pi) - 3 * math.pi / 2) < 0.25:
            for j in range(4):
                c.ellipse(x - 10 - j * 6, y + 20 + j * 22, 7, 7, fill=WATER)
    # trough at top-left
    c.rect(cx - 300, cy - R - 10, cx + 20, cy - R + 20, fill=WOODC, r=4)
    c.text(cx - 140, cy - R - 40, '水槽 → 田里', 'sans', 26, INK, 'mm')
    # energy panel
    px = 1280
    c.rect(px, 200, 1860, 620, fill=SHEET, r=16)
    c.text(px + 30, 250, '能量的账', 'bold', 30, INK, 'lm')
    c.text(px + 30, 320, '大量河水推动轮子（失去一点速度）', 'sans', 26, INK, 'lm')
    c.text(px + 30, 380, '→ 把少量的水抬高几米', 'sans', 26, COPPER, 'lm')
    c.text(px + 30, 460, '水不能自己往高处走，', 'sans', 26, MUTED, 'lm')
    c.text(px + 30, 505, '是更多的水「推」它上去的', 'bold', 26, FIELD, 'lm')
    c.text(px + 30, 570, '唐代已有筒车（又称天车）', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 7, '轮子一半泡在河里，河水推着它转'),
                (7.2, 14, '轮边绑着斜放的竹筒：在水里灌满，转到顶上再倒出来'),
                (14.2, 22, '它和第 06 集的水车是同一个轮子：一个用来发电，一个用来提水')])

# ---------------------------------------------------------------- E25 螺旋提水
def screw_scene(c, ox, oy, L, theta, phase, t, A=46, P=120, label=True, scale=1.0):
    """Draw an inclined screw (2D projection). Water sits in the local minima of height along the helix."""
    ux, uy = math.cos(theta), -math.sin(theta)
    nx, ny = -uy, ux
    # tube outline
    R = 60 * scale
    c.line([(ox + nx * R, oy + ny * R), (ox + ux * L + nx * R, oy + uy * L + ny * R)], MUTED, 4)
    c.line([(ox - nx * R, oy - ny * R), (ox + ux * L - nx * R, oy + uy * L - ny * R)], MUTED, 4)
    # helix: height above ground h(s) = s*sin(theta) - A*cos(2*pi*s/P + phase)*cos(theta)
    pts = []
    hs = []
    N = 260
    for k in range(N + 1):
        s = k / N * L
        w = math.cos(2 * math.pi * s / P + phase)
        px = ox + ux * s + nx * R * w * 0.95
        py = oy + uy * s + ny * R * w * 0.95
        pts.append((px, py))
        hs.append(-py)
    c.line(pts, COPPER, 5)
    # local minima → water pockets (only where a basin exists)
    pockets = 0
    for k in range(1, N):
        if hs[k] < hs[k - 1] and hs[k] <= hs[k + 1]:
            # basin depth: compare with next local max ahead
            j = k
            while j < N and hs[j + 1] >= hs[j]: j += 1
            depth = hs[j] - hs[k]
            if depth > 6:
                px, py = pts[k]
                d = min(depth, 30)
                c.ellipse(px, py - d * 0.3, 18 * scale, d * 0.45 + 6, fill=WATER)
                pockets += 1
    return pockets

def e25_pockets(c, t, i):
    corner_tag(c, '第 25 集 · 螺旋提水')
    c.text(60, 96, '一根螺旋，怎么把水送上高处？', 'serif', 40, INK)
    c.rect(0, 880, 520, 1080, fill=mix(BG, FIELD, 0.35))
    c.text(60, 920, '低处的水', 'sans', 26, MUTED, 'lm')
    c.rect(1400, 330, 1920, 380, fill=mix(BG, FIELD, 0.35 + 0.3 * fade(t, 6, 20)))
    c.text(1860, 300, '高处', 'sans', 26, MUTED, 'rm')
    theta = math.radians(28)
    phase = -t * 2.2
    screw_scene(c, 360, 900, 1200, theta, phase, t, P=300)
    for k in range(4):
        ph = (t * 1.2 + k / 4) % 1
        c.ellipse(1420 + ph * 20, 360 + ph * 10, 8, 8, fill=WATER)
    a = fade(t, 12, 13)
    c.rect(1180, 620, 1860, 860, fill=mix(BG, SHEET, a), r=14)
    c.text(1210, 670, '每一圈螺旋的底部，都是一个小「水洼」', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 720, '水始终待在局部的最低处', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1210, 770, '螺旋一转，水洼整体往上挪', 'bold', 28, mix(BG, COPPER, a), 'lm')
    c.text(1210, 815, '水其实一直在「往下流」', 'sans', 26, mix(BG, FIELD, a), 'lm')
    caps(c, t, [(0, 6, '一根斜放的管子，里面是一圈圈螺旋'),
                (6.2, 12, '转动它：下端舀起一点水，水就一格一格往上走'),
                (12.2, 24, '这是公元前 3 世纪传说中阿基米德的发明；北宋的中国还没有它')])

def e25_angle(c, t, i):
    corner_tag(c, '第 25 集 · 倾角')
    c.text(60, 96, '放得越陡越好吗？', 'serif', 40, INK)
    phase = -t * 2.2
    angles = [20, 35, 55]
    for k, deg in enumerate(angles):
        a = fade(t, 0.5 + k * 3, 1.5 + k * 3)
        if a <= 0: continue
        ox = 140 + k * 600
        th = math.radians(deg)
        L = 480
        n = screw_scene(c, ox, 860, L, th, phase, t, A=46, P=280, scale=0.8)
        c.text(ox + 220, 930, f'倾角 {deg}°', 'bold', 32, INK, 'mm')
        ok = n > 0
        c.text(ox + 220, 980, '能提水' if ok else '没有「水洼」：水全部倒流', 'sans', 26, FIELD if ok else NRED, 'mm')
    caps(c, t, [(0, 9, '同一根螺旋，换三种倾角'),
                (9.2, 15, '越陡，每一格的「水洼」越浅，能装的水越少'),
                (15.2, 20, '陡到一定程度，水洼消失，水一滴也提不上去')], y=1040)

# ---------------------------------------------------------------- E26 虹吸
def bucket(c, x0, y0, x1, y1, lvl):
    if lvl < y1 - 6: c.rect(x0 + 6, lvl, x1 - 6, y1 - 6, fill=WATER, r=6)
    c.line([(x0, y0), (x0 + 10, y1), (x1 - 10, y1), (x1, y0)], MUTED, 6)

def e26_siphon(c, t, i):
    corner_tag(c, '第 26 集 · 虹吸')
    c.text(60, 96, '水为什么能先往上爬，再翻过去？', 'serif', 40, INK)
    # wall
    c.rect(880, 380, 1040, 980, fill=(110, 96, 80), r=4)
    c.text(960, 1000, '堤坝', 'sans', 24, MUTED, 'mm')
    filled = fade(t, 4, 6)
    flow = t > 6 and t < 17
    raise_out = fade(t, 17, 19)
    lvlA = 560 + 80 * fade(t, 6, 17)
    bucket(c, 340, 500, 780, 960, lvlA)
    outy = 900 - 420 * raise_out
    lvlB = 940 - 80 * fade(t, 6, 17)
    bucket(c, 1240, 700, 1680, 980, lvlB)
    # tube path
    path = [(560, 900), (560, 330), (960, 300), (1360, 330), (1360, outy)]
    c.line(path, (200, 200, 200), 18)
    if filled > 0:
        c.line(path, mix((200, 200, 200), FIELD, filled), 10)
    if flow and raise_out < 0.5:
        for k in range(10):
            s = (t * 0.6 + k / 10) % 1
            # parametric along path
            seg = [(path[j], path[j + 1]) for j in range(len(path) - 1)]
            lens = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in seg]
            d = s * sum(lens)
            for (a, b), l in zip(seg, lens):
                if d <= l:
                    c.ellipse(a[0] + (b[0] - a[0]) * d / l, a[1] + (b[1] - a[1]) * d / l, 6, 6, fill=INK); break
                d -= l
        for j in range(4):
            c.ellipse(1360, outy + 20 + j * 18, 7, 7, fill=WATER)
    # height difference marker
    if t > 7:
        a = fade(t, 7, 8)
        c.line([(1720, lvlA), (1720, outy)], mix(BG, SPARK, a), 3)
        c.line([(780, lvlA), (1740, lvlA)], mix(BG, SPARK, 0.5 * a), 2)
        c.text(1740, (lvlA + outy) / 2, '高差', 'bold', 26, mix(BG, SPARK, a), 'lm')
    if 1 < t < 4:
        c.text(560, 260, '空管子：不流', 'bold', 28, NRED, 'mm')
    # pressure arrows on source surface
    if t > 9 and t < 17:
        for k in range(4):
            c.arrow(400 + k * 100, lvlA - 80, 400 + k * 100, lvlA - 10, mix(BG, FIELD, 0.9), 4, 12)
        c.text(560, lvlA - 110, '大气压往下压水面', 'sans', 24, FIELD, 'mm')
    caps(c, t, [(0, 4, '一根空管子搭过堤坝：水不会自己爬上去'),
                (4.2, 9, '先把管子灌满水，再放开：水就源源不断翻过去了'),
                (9.2, 17, '出口比水面低：低的那一侧水更重，把水往下拉；大气压把水面往管里推'),
                (17.2, 22, '把出口抬到水面以上：立刻断流 —— 高差决定一切')])

def e26_limit(c, t, i):
    corner_tag(c, '第 26 集 · 十米极限')
    c.text(60, 96, '管子能翻多高的山？', 'serif', 40, INK)
    gy = 960; scale = 62  # px per metre
    H = 2 + 10 * fade(t, 1, 14)
    c.rect(200, gy - 60, 700, gy, fill=WATER)
    for m in range(0, 13, 2):
        y = gy - m * scale
        c.line([(150, y), (180, y)], MUTED, 2); c.text(140, y, f'{m} 米', 'mono', 22, MUTED, 'rm')
    top = gy - H * scale
    c.line([(400, gy - 40), (400, top), (800, top), (800, gy + 40)], (200, 200, 200), 16)
    broken = H > 10.3
    col_top = top if not broken else gy - 10.3 * scale
    c.line([(400, gy - 40), (400, col_top)], FIELD, 8)
    c.line([(800, col_top + 0), (800, gy + 40)], FIELD, 8)
    if not broken:
        c.line([(400, top), (800, top)], FIELD, 8)
    else:
        c.line([(400, top), (800, top)], mix(BG, SPARK, 0.6), 8)
        c.text(600, top - 40, '顶上被「拉」出一段真空：断流', 'bold', 28, NRED, 'mm')
    c.line([(160, gy - 10.3 * scale), (1000, gy - 10.3 * scale)], mix(BG, SPARK, 0.8), 2)
    c.text(1010, gy - 10.3 * scale, '约 10.3 米', 'mono', 26, SPARK, 'lm')
    c.text(900, top, f'翻越高度 {H:.1f} 米', 'mono', 28, INK, 'lm')
    px = 1240
    c.rect(px, 260, 1860, 640, fill=SHEET, r=16)
    c.text(px + 30, 310, '一个大气压', 'bold', 30, INK, 'lm')
    c.text(px + 30, 365, '≈ 10 米高的水柱的重量', 'sans', 28, COPPER, 'lm')
    c.text(px + 30, 440, '大气压最多把水推上约 10 米', 'sans', 26, INK, 'lm')
    c.text(px + 30, 490, '再高，管顶的水就「断」了', 'sans', 26, INK, 'lm')
    c.text(px + 30, 570, '现实中还有摩擦、气泡，会更低', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 8, '把管子顶部一点点抬高……'),
                (8.2, 14, '过了大约十米，管顶的水撑不住了'),
                (14.2, 18, '虹吸能翻过堤坝，翻不过高山')])

# ---------------------------------------------------------------- 片头片尾
S3A = [('28', '水车提水'), ('25', '螺旋提水'), ('26', '虹吸'), ('27', '陶罐滴灌'), ('29', '轮作固氮'), ('34', '净水'), ('38', '冷却罐'), ('30', '选种嫁接')]
SER3, VOL3 = '从零造物', '第三季 · 水与农业'
CLIPS = {
 'E28_翻车': (e28_chain, 22), 'E28_筒车': (e28_tube, 22),
 'E28_片头': (titles.opening(SER3, VOL3, S3A, 0, '东汉翻车 · 唐代筒车 · 北宋田间'), 7),
 'E28_片尾': (titles.closing(SER3, VOL3, S3A, 0, '下集：北宋还没有的机械 —— 螺旋'), 7),
 'E25_一格一格': (e25_pockets, 24), 'E25_倾角': (e25_angle, 20),
 'E25_片头': (titles.opening(SER3, VOL3, S3A, 1, '北宋 · 约公元 1090 年 · 一样「穿越」来的机械'), 7),
 'E25_片尾': (titles.closing(SER3, VOL3, S3A, 1, '下集：不用机器，水也能翻过堤坝'), 7),
 'E26_虹吸原理': (e26_siphon, 22), 'E26_十米极限': (e26_limit, 18),
 'E26_片头': (titles.opening(SER3, VOL3, S3A, 2, '东汉「渴乌」· 一根管子翻过堤坝'), 7),
 'E26_片尾': (titles.closing(SER3, VOL3, S3A, 2, '下集：两千年还在用的都江堰'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
