"""第二十三季（第八层：大工程）第一批：E122 船闸、E123 地震仪、E124 天气预报 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S23A = [('122', '船闸'), ('123', '地震仪'), ('124', '天气预报'), ('125', '海水淡化'), ('126', '盾构隧道'),
        ('127', '阻尼器'), ('128', '高铁'), ('129', '潮汐发电'), ('130', '回收火箭'), ('131', '空间站')]
SER23, VOL23 = '从零造物', '第二十三季 · 第八层：大工程'
WATER = (70, 130, 200)
WATER_L = (110, 170, 230)
CONC = (130, 130, 135)
GATE = (170, 120, 70)
HULL = (220, 200, 160)
GROUND = (150, 115, 75)
PAPER = (235, 232, 222)
PEN = (60, 110, 200)
HIGH = (230, 120, 80)
LOW = (90, 150, 230)
CLOUD = (210, 215, 225)


def wave_rect(c, x0, x1, y_top, y_bot, col, t, amp=4):
    pts = [(x0, y_bot)]
    for j in range(31):
        x = x0 + (x1 - x0) * j / 30
        pts.append((x, y_top + amp * math.sin(j * 0.8 + t * 3)))
    pts.append((x1, y_bot))
    c.poly(pts, col)


# ---------------------------------------------------------------- E122 船闸
def e122_vessels(c, t, i):
    corner_tag(c, '第 122 集 · 连着的水，水面一样高')
    c.text(60, 96, '两个盒子底下连通：阀门一开，高的往低的流，直到水面一样高', 'serif', 40, INK)
    open_t = 4.0
    d0 = 300.0
    d = d0 if t < open_t else d0 * math.exp(-(t - open_t) / 3.0)
    ha, hb = 450 + d / 2, 450 - d / 2
    floor = 860
    for k, (x0, x1, h) in enumerate(((220, 720, ha), (1000, 1500, hb))):
        c.rect(x0 - 10, 300, x0, floor + 10, fill=CONC)
        c.rect(x1, 300, x1 + 10, floor + 10, fill=CONC)
        c.rect(x0 - 10, floor, x1 + 10, floor + 10, fill=CONC)
        wave_rect(c, x0, x1, floor - h, floor, WATER, t + k)
        c.text((x0 + x1) / 2, 260, '左盒' if k == 0 else '右盒', 'bold', 26, INK, 'mm')
    c.rect(720, floor - 50, 1000, floor - 10, fill=WATER if t >= open_t else mix(BG, WATER, 0.3))
    c.rect(720, floor - 60, 1000, floor - 50, fill=CONC)
    c.rect(720, floor - 10, 1000, floor, fill=CONC)
    vx = 860
    c.rect(vx - 14, floor - 90, vx + 14, floor - 50 if t >= open_t else floor - 10, fill=GATE)
    c.text(vx, floor - 110, '阀门：开' if t >= open_t else '阀门：关', 'sans', 22, SPARK if t >= open_t else MUTED, 'mm')
    if t >= open_t and d > 8:
        for k in range(6):
            s = ((t * 1.5) + k / 6) % 1
            c.ellipse(720 + 280 * s, floor - 30, 6, 6, fill=WATER_L)
    c.rect(1580, 340, 1860, 600, fill=SHEET, r=12)
    c.text(1720, 380, '水面高差', 'bold', 24, INK, 'mm')
    c.text(1720, 460, f'{d / 10:.0f} 厘米（示意）', 'mono', 30, SPARK, 'mm')
    c.text(1720, 540, '一滴都不用抽', 'sans', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '两个盒子底下用一根管子连着，阀门关着时，一边高一边低'),
                (7.2, 14, '阀门一开，高的那边压得重，水就往低的那边流'),
                (14.2, 22, '流到两边水面一样高就停了：这叫连通器。船闸靠的就是它，水自己流，不用水泵')], y=1010)


def e122_lock(c, t, i):
    corner_tag(c, '第 122 集 · 船怎么「爬」上去')
    c.text(60, 96, '关下闸门、开上阀门：闸室水涨船高，和上游一平，船就开出去', 'serif', 40, INK)
    floor = 880
    lo, hi = 260, 500
    x_lo, x_g1, x_g2, x_hi = 120, 640, 1240, 1800
    # 阶段：0-4 船进闸室；4-6 关下闸门；6-14 上阀门开，水涨；14-16 开上闸门；16-22 船驶出
    if t < 6:
        ch = lo
    elif t < 14:
        ch = lo + (hi - lo) * (0.5 - 0.5 * math.cos((t - 6) / 8 * math.pi))
    else:
        ch = hi
    wave_rect(c, x_lo, x_g1, floor - lo, floor, WATER, t)
    wave_rect(c, x_g1, x_g2, floor - ch, floor, WATER, t + 1)
    wave_rect(c, x_g2, x_hi, floor - hi, floor, WATER, t + 2)
    c.rect(x_g1 - 10, floor - 40, x_g2 + 10, floor + 10, fill=CONC)
    c.rect(x_g2, floor - hi + 0, x_g2 + 10, floor, fill=CONC)
    g1_closed = 4 <= t
    g2_closed = t < 14.5
    if g1_closed:
        c.rect(x_g1 - 14, floor - hi - 60, x_g1 + 14, floor, fill=GATE)
    else:
        c.rect(x_g1 - 14, floor - hi - 60, x_g1 + 14, floor - hi - 30, fill=GATE)
    if g2_closed:
        c.rect(x_g2 - 4, floor - hi - 60, x_g2 + 24, floor - hi + 20, fill=GATE)
        c.rect(x_g2 - 4, floor - hi + 20, x_g2 + 24, floor, fill=CONC)
    c.text(x_g1, floor - hi - 90, '下闸门', 'sans', 22, MUTED, 'mm')
    c.text(x_g2 + 10, floor - hi - 90, '上闸门', 'sans', 22, MUTED, 'mm')
    if 6 <= t < 14:
        for k in range(5):
            s = ((t * 1.2) + k / 5) % 1
            c.ellipse(x_g2 - 20 * s, floor - 30, 6, 6, fill=WATER_L)
        c.text(x_g2 - 120, floor + 40, '上阀门开：上游的水流进闸室', 'sans', 22, SPARK, 'mm')
    if t < 4:
        bx = 300 + (900 - 300) * fade(t, 0, 4)
    elif t < 16:
        bx = 900
    else:
        bx = 900 + (1550 - 900) * fade(t, 16, 21)
    if bx < x_g1:
        wl = floor - lo
    elif bx < x_g2:
        wl = floor - ch
    else:
        wl = floor - hi
    c.poly([(bx - 110, wl - 30), (bx + 110, wl - 30), (bx + 80, wl + 18), (bx - 80, wl + 18)], HULL)
    c.rect(bx - 40, wl - 80, bx + 30, wl - 30, fill=(240, 240, 235), r=4)
    c.text(380, floor - lo - 60, '下游', 'bold', 26, INK, 'mm')
    c.text(1520, floor - hi - 40, '上游', 'bold', 26, INK, 'mm')
    c.text(940, 250, '闸室', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 6, '船从下游开进闸室，身后的下闸门关上'),
                (6.2, 14, '打开上游一侧的小阀门，上游的水自己流进闸室：闸室水面一点点涨，船跟着浮上来'),
                (14.2, 22, '闸室和上游一样高时，打开上闸门，船就开出去了。北宋就有这样两道门的复闸（拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- E123 地震仪
def e123_inertia(c, t, i):
    corner_tag(c, '第 123 集 · 很重的锤「懒得动」')
    c.text(60, 96, '地面带着架子和纸左右晃；吊着的重锤几乎不动，笔就在纸上画出晃动', 'serif', 40, INK)
    amp = 60 if (t % 11) < 6 else 20
    gx = amp * math.sin(t * 5) * (1 if t > 1 else t)
    c.rect(0, 840, 1920, 940, fill=GROUND)
    fx = 520 + gx
    c.rect(fx - 260, 820, fx + 260, 840, fill=CONC)
    c.rect(fx - 260, 260, fx - 240, 820, fill=CONC)
    c.rect(fx - 260, 250, fx + 60, 270, fill=CONC)
    mx = 520 + gx * 0.08
    c.line([(fx + 40, 270), (mx, 600)], INK, 3)
    c.rect(mx - 60, 600, mx + 60, 720, fill=(90, 90, 100), r=10)
    c.line([(mx, 720), (mx, 790)], PEN, 6)
    c.rect(fx - 200, 790, fx + 200, 815, fill=PAPER)
    c.text(mx + 90, 660, '重锤', 'bold', 24, INK, 'lm')
    c.text(fx - 300, 800, '纸', 'sans', 22, MUTED, 'rm')
    c.rect(1060, 260, 1860, 760, fill=SHEET, r=14)
    c.text(1460, 300, '纸带上画出的波形', 'bold', 26, INK, 'mm')
    gy = 520
    c.line([(1100, gy), (1820, gy)], LINE, 2)
    pts = []
    N = 240
    for j in range(N + 1):
        tt = t - (N - j) / N * 6
        if tt < 0:
            continue
        a = 60 if (tt % 11) < 6 else 20
        g = a * math.sin(tt * 5) * (1 if tt > 1 else max(0, tt))
        pts.append((1100 + 720 * j / N, gy - g * 2.4))
    if len(pts) > 1:
        c.line(pts, PEN, 3)
    c.text(1460, 720, '晃得大，线就宽；晃得小，线就窄', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '地面一晃，架子和纸跟着晃；可是吊着的重锤很重，「懒得动」'),
                (7.2, 14, '锤几乎停在原地，笔就相对纸来回移动，把地面的晃动画了下来'),
                (14.2, 22, '这就是惯性。近代地震仪就是这样一台「重摆 + 记录纸」，后来换成了线圈和磁铁')], y=1010)


def e123_waves(c, t, i):
    corner_tag(c, '第 123 集 · 先「嗒」后「晃」')
    c.text(60, 96, '地震同时发出两种波：快的先到、慢的后到；差得越久，震中越远', 'serif', 40, INK)
    ex, ey = 260, 560
    c.ellipse(ex, ey, 18, 18, fill=NRED)
    c.text(ex, ey + 50, '震中', 'bold', 24, NRED, 'mm')
    st = [(820, 420, '甲站'), (1300, 700, '乙站')]
    vp, vs = 140.0, 80.0
    for (sx, sy, nm) in st:
        c.rect(sx - 26, sy - 26, sx + 26, sy + 26, fill=SHEET, outline=LINE, width=2, r=6)
        c.text(sx, sy - 50, nm, 'bold', 24, INK, 'mm')
    rp, rs = vp * t, vs * t
    if rp < 1500:
        c.ellipse(ex, ey, rp, rp, outline=mix(BG, SPARK, 0.7), width=3)
    if rs < 1500:
        c.ellipse(ex, ey, rs, rs, outline=mix(BG, NRED, 0.7), width=3)
    c.text(1560, 260, '黄：纵波（快）', 'sans', 24, SPARK, 'lm')
    c.text(1560, 300, '红：横波（慢）', 'sans', 24, NRED, 'lm')
    for k, (sx, sy, nm) in enumerate(st):
        D = math.hypot(sx - ex, sy - ey)
        tp, ts = D / vp, D / vs
        y0 = 880 + k * 0
        x0 = 120 + k * 900
        c.rect(x0, 800, x0 + 780, 960, fill=SHEET, r=10)
        c.text(x0 + 20, 820, f'{nm}的记录', 'sans', 20, MUTED, 'lm')
        pts = []
        for j in range(201):
            tt = 22 * j / 200
            if tt > t:
                break
            v = 0
            if tt > tp:
                v += 14 * math.sin((tt - tp) * 30) * math.exp(-(tt - tp) * 0.8)
            if tt > ts:
                v += 40 * math.sin((tt - ts) * 14) * math.exp(-(tt - ts) * 0.5)
            pts.append((x0 + 20 + 740 * tt / 22, 890 - v))
        if len(pts) > 1:
            c.line(pts, PEN, 2)
        if t > ts:
            c.text(x0 + 760, 820, f'差 {ts - tp:.1f} 秒（示意）', 'mono', 20, INK, 'rm')
    caps(c, t, [(0, 7, '地震时，地下同时发出两种波：纵波跑得快，横波跑得慢'),
                (7.2, 14, '离得近的甲站，两种波前后脚到；离得远的乙站，要隔好一会儿横波才来'),
                (14.2, 22, '量出两种波差了几秒，就能算出离震中多远；三个站一起算，就找到了震中')], y=760)


# ---------------------------------------------------------------- E124 天气预报
def e124_grid(c, t, i):
    corner_tag(c, '第 124 集 · 把天空切成小格子')
    c.text(60, 96, '每个格子记下温度、气压、风；按物理公式算下一步，一步步往未来推', 'serif', 40, INK)
    nx, ny = 14, 8
    x0, y0, w = 160, 220, 80
    step = int(t / 2.2)
    rnd = random.Random(2)
    base = [[rnd.uniform(0, 1) for _ in range(nx)] for _ in range(ny)]
    field = base
    for s in range(step):
        nf = [[0.0] * nx for _ in range(ny)]
        for y in range(ny):
            for x in range(nx):
                xs = (x - 1) % nx
                nf[y][x] = 0.6 * field[y][xs] + 0.4 * field[y][x]
        field = nf
    for y in range(ny):
        for x in range(nx):
            v = field[y][x]
            c.rect(x0 + x * w, y0 + y * w, x0 + (x + 1) * w - 4, y0 + (y + 1) * w - 4, fill=mix(LOW, HIGH, v))
            if (x + y) % 3 == 0:
                cx, cy = x0 + x * w + w / 2, y0 + y * w + w / 2
                c.arrow(cx - 20, cy, cx + 20, cy, (240, 240, 245), 2, 8)
    c.rect(1340, 240, 1860, 720, fill=SHEET, r=14)
    c.text(1600, 280, '电脑在做的事', 'bold', 26, INK, 'mm')
    c.text(1380, 360, f'已经往前算了 {step} 步', 'mono', 28, SPARK, 'lm')
    c.text(1380, 440, '每一步：每个格子', 'sans', 24, INK, 'lm')
    c.text(1380, 490, '看邻居 → 算风怎么吹', 'sans', 24, INK, 'lm')
    c.text(1380, 540, '→ 算温度、水汽怎么变', 'sans', 24, INK, 'lm')
    c.text(1380, 620, '格子越小、算得越准，也越费电脑', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '把整个地球的天空切成几百万个小格子，每格记下温度、气压、湿度和风'),
                (7.2, 14, '电脑按物理公式算：风把热空气吹到哪一格，水汽在哪一格凝成云'),
                (14.2, 22, '算完一步再算下一步，一直推到明天、后天。这就是第 91 集那台计算机最早的大用处之一')], y=1010)


def e124_pressure(c, t, i):
    corner_tag(c, '第 124 集 · 气压一降，雨要来')
    c.text(60, 96, '空气从气压高的地方流向低的地方；低压中心的空气往上升，冷下来就成云下雨', 'serif', 40, INK)
    hx, lx, cy = 420, 1180, 620
    c.ellipse(hx, cy, 170, 170, fill=mix(BG, HIGH, 0.35))
    c.text(hx, cy, '高', 'bold', 60, HIGH, 'mm')
    c.ellipse(lx, cy, 170, 170, fill=mix(BG, LOW, 0.35))
    c.text(lx, cy, '低', 'bold', 60, LOW, 'mm')
    for k in range(8):
        s = (t * 0.25 + k / 8) % 1
        x = hx + 180 + (lx - hx - 360) * s
        c.arrow(x, cy + 40 * math.sin(k), x + 40, cy + 40 * math.sin(k), (230, 230, 240), 3, 10)
    for k in range(6):
        s = (t * 0.3 + k / 6) % 1
        y = cy - 60 - 280 * s
        c.arrow(lx + (k - 2.5) * 30, y, lx + (k - 2.5) * 30, y - 30, LOW, 3, 10)
    cl = min(1.0, t / 10)
    for k in range(5):
        c.ellipse(lx - 160 + k * 80, 300 - 20 * (k % 2), 70 * cl, 45 * cl, fill=CLOUD)
    if t > 12:
        rnd = random.Random(int(t * 10))
        for k in range(20):
            x = rnd.uniform(lx - 200, lx + 200)
            y = rnd.uniform(360, 460)
            c.line([(x, y), (x - 6, y + 22)], WATER_L, 2)
    c.rect(1480, 260, 1860, 760, fill=SHEET, r=14)
    c.text(1670, 300, '低压这边的气压计', 'bold', 24, INK, 'mm')
    p = 1016 - 12 * min(1.0, t / 18)
    c.text(1670, 400, f'{p:.0f} 百帕', 'mono', 40, SPARK, 'mm')
    c.text(1670, 470, '（示意数字）', 'sans', 20, MUTED, 'mm')
    c.arrow(1670, 520, 1670, 640, SPARK, 5, 16)
    c.text(1670, 690, '一直往下掉：常常要变天', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '气压高的地方空气往下沉，气压低的地方空气往上升'),
                (7.2, 14, '空气从高压流向低压；在低压中心往上升，越升越冷，水汽凝成了云'),
                (14.2, 22, '所以气压计一直往下掉，常常是坏天气要来。气压、温度、湿度，都是预报要算的数')], y=1010)


CLIPS = {
 'E122_连通器': (e122_vessels, 22), 'E122_过闸': (e122_lock, 22),
 'E122_片头': (titles.opening(SER23, VOL23, S23A, 0, '北宋复闸 · 三峡船闸'), 7),
 'E122_片尾': (titles.closing(SER23, VOL23, S23A, 0, '下集：地面在晃，地震仪怎么把晃动画下来？'), 7),
 'E123_惯性': (e123_inertia, 22), 'E123_两种波': (e123_waves, 22),
 'E123_片头': (titles.opening(SER23, VOL23, S23A, 1, '132 年张衡地动仪 · 近代地震仪'), 7),
 'E123_片尾': (titles.closing(SER23, VOL23, S23A, 1, '下集：明天会不会下雨，是怎么算出来的？'), 7),
 'E124_格子': (e124_grid, 22), 'E124_气压': (e124_pressure, 22),
 'E124_片头': (titles.opening(SER23, VOL23, S23A, 2, '1922 年理查森设想 · 1950 年电脑预报'), 7),
 'E124_片尾': (titles.closing(SER23, VOL23, S23A, 2, '下集：海水那么多，怎么变成淡水？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
