"""第二十一季（第七层）第二批：E115 平衡车、E116 电子墨水屏、E117 石墨烯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s21a import S21A, SER21, VOL21

STICK = (200, 160, 100)
WHITE_P = (240, 240, 235)
BLACK_P = (40, 40, 45)
GRAPH = (110, 115, 125)

# ---------------------------------------------------------------- E115 平衡车
def _sim(T, ctrl, L=1.0, th0=0.08, dt=0.005):
    g = 9.8
    th, w, x, v = th0, 0.0, 0.0, 0.0
    out = []
    t = 0
    while t <= T:
        a = (40 * th + 9 * w) if ctrl else 0.0
        a = max(-12, min(12, a))
        al = (g * math.sin(th) - a * math.cos(th)) / L
        w += al * dt; th += w * dt
        v += a * dt; x += v * dt
        v *= 0.999
        if abs(th) > 1.45: th = math.copysign(1.45, th); w = 0
        out.append((t, th, x))
        t += dt
    return out

SIM_OFF = _sim(22, False)
SIM_ON = _sim(22, True)

def _at(sim, t):
    k = min(len(sim) - 1, int(t / 0.005))
    return sim[k]

def e115_pendulum(c, t, i):
    corner_tag(c, '第 115 集 · 往哪边倒，就往哪边追')
    c.text(60, 96, '平衡车就是一根倒立的棍子：陀螺仪测到前倾，轮子就往前开', 'serif', 40, INK)
    for k, (nm, sim) in enumerate((('不控制', SIM_OFF), ('陀螺仪 + 电机控制', SIM_ON))):
        ox = 480 + k * 900
        gy = 820
        _, th, x = _at(sim, max(0, t - 1))
        bx = ox + max(-300, min(300, x * 120))
        c.line([(ox - 380, gy + 40), (ox + 380, gy + 40)], LINE, 4)
        c.rect(bx - 70, gy - 20, bx + 70, gy + 10, fill=(90, 90, 100), r=6)
        for wx in (bx - 45, bx + 45):
            c.ellipse(wx, gy + 18, 22, 22, fill=(40, 40, 45))
        L = 420
        tx, ty = bx + L * math.sin(th), gy - 20 - L * math.cos(th)
        c.line([(bx, gy - 20), (tx, ty)], STICK, 12)
        c.ellipse(tx, ty, 26, 26, fill=(220, 170, 140))
        c.text(ox, 260, nm, 'bold', 28, INK, 'mm')
        c.text(ox, 310, f'倾角 {math.degrees(th):5.1f}°', 'mono', 24, NRED if abs(th) > 0.5 else GREEN, 'mm')
    caps(c, t, [(0, 7, '人站在平衡车上，就像一根立在轮子上的棍子：稍微一歪，重力就让它越倒越快'),
                (7.2, 14, '不管它，几秒就倒了'),
                (14.2, 22, '平衡车里的陀螺仪每秒测几百次倾角：一往前倒，电机就让轮子往前追，把底下垫回到重心下面')], y=1010)

def e115_length(c, t, i):
    corner_tag(c, '第 115 集 · 越长，倒得越慢')
    c.text(60, 96, '同样歪一点点：铅笔眨眼就倒，扫帚慢慢才倒，所以扫帚好立', 'serif', 40, INK)
    gy = 860
    for k, (nm, L, px) in enumerate((('铅笔 15 厘米', 0.15, 60), ('尺子 30 厘米', 0.30, 110), ('扫帚 120 厘米', 1.2, 320))):
        ox = 300 + k * 560
        # 无控制下落：θ'' = (3g/2L) sinθ（均匀杆）
        g = 9.8
        th, w = 0.05, 0.0
        tt = 0.0
        dt = 0.002
        T = max(0, t - 2) * 0.065
        fell = None
        while tt < T:
            w += 1.5 * g / L * math.sin(th) * dt
            th += w * dt
            tt += dt
            if th > 1.5:
                th = 1.5
                if fell is None: fell = tt
                break
        Lp = px
        c.line([(ox - 260, gy), (ox + 260, gy)], LINE, 4)
        c.line([(ox, gy), (ox + Lp * math.sin(th), gy - Lp * math.cos(th))], STICK, 10)
        c.text(ox, 320, nm, 'bold', 26, INK, 'mm')
        th2, w2, tf = 0.05, 0.0, 0.0
        while th2 < 1.5:
            w2 += 1.5 * g / L * math.sin(th2) * dt; th2 += w2 * dt; tf += dt
        c.text(ox, 370, f'倒下约需 {tf:.2f} 秒（理想值，慢放约 15 倍）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '三根东西都只歪了一点点，同时松手'),
                (7.2, 14, '铅笔眨眼就倒了；扫帚倒得最慢：越长的东西，倒下去要的时间越久'),
                (14.2, 22, '倒得慢，手就来得及追。所以在手心立扫帚比立铅笔容易：平衡车也是一样，越高越好控制')], y=1010)

# ---------------------------------------------------------------- E116 电子墨水屏
PATTERN = [[0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]]

def e116_capsule(c, t, i):
    corner_tag(c, '第 116 集 · 一颗颗微胶囊')
    c.text(60, 96, '每颗胶囊里有带正电的白粒和带负电的黑粒：底下电极一变，它们就上下换位', 'serif', 40, INK)
    page = 0 if t < 9 else 1
    sw = fade(t, 9, 11) if page == 1 else 0
    pat0, pat1 = PATTERN
    n = 12
    x0, w = 140, 135
    ytop, ybot = 380, 640
    c.text(960, 330, '看的人在上面', 'sans', 22, MUTED, 'mm')
    rnd = random.Random(5)
    for k in range(n):
        cx = x0 + k * w + w / 2
        c.ellipse(cx, (ytop + ybot) / 2, w / 2 - 6, (ybot - ytop) / 2, outline=mix(BG, LINE, 0.9), width=3)
        a = pat0[k] if t < 9 else pat1[k]
        prev = pat0[k]
        cur = pat1[k] if t >= 9 else pat0[k]
        u = sw if prev != cur else 1.0
        black_up = cur == 1
        for j in range(10):
            ox = rnd.uniform(-30, 30)
            oy = rnd.uniform(-20, 20)
            # 黑粒
            yb_up, yb_dn = ytop + 50, ybot - 50
            if prev != cur:
                yb = (yb_dn + (yb_up - yb_dn) * u) if black_up else (yb_up + (yb_dn - yb_up) * u)
            else:
                yb = yb_up if black_up else yb_dn
            yw = ytop + ybot - yb
            c.ellipse(cx + ox, yb + oy, 8, 8, fill=BLACK_P, outline=MUTED, width=1)
            c.ellipse(cx - ox, yw - oy, 8, 8, fill=WHITE_P)
        c.rect(cx - w / 2 + 8, ybot + 20, cx + w / 2 - 8, ybot + 50, fill=SPARK if cur == 1 else ELEC_C, r=4)
        c.text(cx, ybot + 80, '−' if cur == 1 else '+', 'bold', 28, INK, 'mm')
    c.text(960, ybot + 140, '底下的电极：带正电就把黑粒（负）吸下来、白粒推上去；带负电就反过来（示意）', 'sans', 20, MUTED, 'mm')
    off = fade(t, 15, 16)
    if off > 0:
        c.rect(560, 860, 1360, 940, fill=mix(BG, SHEET, off), r=12)
        c.text(960, 900, '断电后颗粒不动，字还在：只有翻页才用电', 'bold', 26, mix(BG, GREEN, off), 'mm')
    caps(c, t, [(0, 8, '屏幕里排着几百万颗比头发丝还细的胶囊，里面是透明液体，泡着白色和黑色两种带电小颗粒'),
                (8.2, 15, '底下的电极换一下正负，黑粒和白粒就上下换位：黑粒在上，这一点就是黑的'),
                (15.2, 22, '它不发光，靠反射外面的光，像纸一样；颗粒停在哪就留在哪，关了电字还在')], y=1010)

ELEC_C = (90, 150, 220)

def e116_static(c, t, i):
    corner_tag(c, '第 116 集 · 带电的东西会被推、被拉')
    c.text(60, 96, '摩擦过的气球带了电，靠近盐和胡椒：轻的胡椒先跳起来', 'serif', 40, INK)
    plate_y = 800
    c.ellipse(960, plate_y + 20, 700, 60, fill=(200, 200, 205))
    rnd = random.Random(2)
    by = 420 + 200 * (1 - fade(t, 3, 9))
    c.ellipse(960, by, 200, 170, fill=(220, 80, 90))
    for k in range(10):
        a = k / 10 * 2 * math.pi
        c.text(960 + 150 * math.cos(a), by + 120 * math.sin(a), '−', 'bold', 26, (250, 230, 230), 'mm')
    near = fade(t, 7, 12)
    for k in range(80):
        x = 360 + rnd.uniform(0, 1200)
        is_pepper = k % 3 == 0
        base = plate_y + rnd.uniform(-10, 10)
        if is_pepper:
            dx = (960 - x) * 0.4
            lift = near * min(1, 1.6 - abs(x - 960) / 600)
            lift = max(0, lift)
            y = base - (base - (by + 170)) * lift
            c.ellipse(x + dx * lift, y, 6, 5, fill=(50, 45, 40))
        else:
            c.rect(x - 4, base - 4, x + 4, base + 4, fill=(245, 245, 245))
    a = fade(t, 13, 14)
    if a > 0:
        c.rect(1440, 300, 1860, 560, fill=mix(BG, SHEET, a), r=14)
        c.text(1650, 350, '同一个道理', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(1650, 420, '带电的颗粒', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1650, 470, '会被电场推着走', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1650, 520, '（第 1 集摩擦起电）', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '气球在头发上一擦，抢走了电子，带上了负电'),
                (6.2, 13, '慢慢靠近盘子：盐和胡椒都被吸，可胡椒又轻又薄，先跳起来粘在气球上'),
                (13.2, 22, '电子墨水屏里的黑白颗粒，也是这样被电场推来推去，只是电场来自屏幕底下的电极')], y=1010)

# ---------------------------------------------------------------- E117 石墨烯
def _sheet(c, x0, y0, W, a, col=GRAPH):
    pts = []
    for k in range(0, int(W), 36):
        c.line([(x0 + k, y0), (x0 + k + 18, y0 - 10), (x0 + k + 36, y0)], mix(BG, col, a), 3)
        c.ellipse(x0 + k, y0, 5, 5, fill=mix(BG, col, a))
        c.ellipse(x0 + k + 18, y0 - 10, 5, 5, fill=mix(BG, col, a))

def e117_layers(c, t, i):
    corner_tag(c, '第 117 集 · 一层一层的碳')
    c.text(60, 96, '石墨是一层层碳原子叠成的；每层都能导电，层和层之间很容易滑开', 'serif', 40, INK)
    peel = fade(t, 7, 17)
    n = 10
    for k in range(n):
        y = 820 - k * 46
        lifted = k >= n - int(peel * (n - 1) + 1e-6) if peel > 0 else False
        if lifted:
            dy = -150
            if k == n - 1:
                c.rect(340, y + dy - 30, 1100, y + dy - 18, fill=mix(BG, (220, 210, 160), 0.7))
            _sheet(c, 360, y + dy, 720, 0.8)
        else:
            _sheet(c, 360, y, 720, 1.0)
    if peel > 0:
        c.text(1180, 300, '透明胶带一粘一撕', 'bold', 26, SPARK, 'lm')
    a = fade(t, 15, 16)
    if a > 0:
        c.rect(1180, 500, 1860, 800, fill=mix(BG, SHEET, a), r=14)
        c.text(1520, 550, '剥到只剩一层：石墨烯', 'bold', 30, mix(BG, GREEN, a), 'mm')
        c.text(1520, 620, '只有一个原子那么厚', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1520, 680, '导电导热极好、又很结实', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1520, 740, '2004 年用胶带剥出，2010 年获诺贝尔奖', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '铅笔芯里不是铅，是石墨：碳原子连成一张张六边形的网，一层层叠起来'),
                (7.2, 15, '层和层之间粘得很松，一写字就蹭下来几层；用透明胶带一粘一撕，也能一次撕下很多层'),
                (15.2, 22, '一直撕到只剩一层，就是石墨烯：薄到只有一个原子，却又导电、又结实')], y=1010)

def e117_circuit(c, t, i):
    corner_tag(c, '第 117 集 · 铅笔线也是导线')
    c.text(60, 96, '铅笔线越短越粗，电阻越小，LED 越亮', 'serif', 40, INK)
    L = 2 + 10 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi))
    c.rect(200, 300, 1500, 820, fill=(235, 232, 225), r=12)
    x0 = 360
    px = 80 * L
    c.rect(x0, 540, x0 + px, 580, fill=GRAPH)
    c.rect(220, 500, 320, 620, fill=(180, 180, 190), r=10)
    c.text(270, 560, '3V', 'bold', 26, INK, 'mm')
    c.line([(320, 560), (x0, 560)], INK, 4)
    lx = x0 + px + 80
    c.line([(x0 + px, 560), (lx - 20, 560)], INK, 4)
    br = min(1, 3.0 / (L + 1))
    c.ellipse(lx, 560, 26, 26, fill=mix((80, 30, 30), (255, 90, 80), br))
    if br > 0.05:
        for k in range(8):
            a = k * math.pi / 4
            c.line([(lx + 36 * math.cos(a), 560 + 36 * math.sin(a)), (lx + (36 + 40 * br) * math.cos(a), 560 + (36 + 40 * br) * math.sin(a))], mix(BG, (255, 120, 100), br), 3)
    c.line([(lx + 20, 560), (lx + 60, 560), (lx + 60, 720), (270, 720), (270, 620)], INK, 4)
    c.rect(1560, 340, 1860, 620, fill=SHEET, r=14)
    c.text(1710, 390, '铅笔线长度', 'sans', 22, MUTED, 'mm')
    c.text(1710, 440, f'{L:.0f} 厘米', 'mono', 34, INK, 'mm')
    c.text(1710, 510, 'LED 亮度', 'sans', 22, MUTED, 'mm')
    c.rect(1600, 550, 1600 + 220 * br, 580, fill=SPARK, r=6)
    c.text(860, 880, '（6B 铅笔涂黑涂粗；亮不亮以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '用 6B 铅笔在纸上涂一条又黑又粗的线，两头接上 3 伏电池和一颗 LED'),
                (7.2, 14, '石墨能导电，电流顺着铅笔线流过去，LED 就亮了'),
                (14.2, 22, '线越长、越细，电阻越大，LED 越暗；线越短越粗，越亮')], y=1010)


CLIPS = {
 'E115_倒立摆': (e115_pendulum, 22), 'E115_长短': (e115_length, 22),
 'E115_片头': (titles.opening(SER21, VOL21, S21A, 3, '2001 年赛格威 · 自平衡车'), 7),
 'E115_片尾': (titles.closing(SER21, VOL21, S21A, 3, '下集：电子书的屏幕为什么像纸，关了电字还在？'), 7),
 'E116_微胶囊': (e116_capsule, 22), 'E116_静电': (e116_static, 22),
 'E116_片头': (titles.opening(SER21, VOL21, S21A, 4, '1997 年电子墨水 · 2007 年电子书'), 7),
 'E116_片尾': (titles.closing(SER21, VOL21, S21A, 4, '下集：铅笔芯里的碳，为什么能导电？'), 7),
 'E117_层状': (e117_layers, 22), 'E117_铅笔线': (e117_circuit, 22),
 'E117_片头': (titles.opening(SER21, VOL21, S21A, 5, '2004 年胶带剥离石墨烯 · 2010 年诺贝尔奖'), 7),
 'E117_片尾': (titles.closing(SER21, VOL21, S21A, 5, '下集：戴上 VR 眼镜，为什么觉得东西就在眼前？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
