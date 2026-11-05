"""第十九季（第六层：聪明的机器）第一批：E102 LED、E103 无线充电、E104 3D 打印 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S19A = [('102', 'LED'), ('103', '无线充电'), ('104', '3D 打印'), ('105', '语音识别'), ('106', '降噪耳机'),
        ('107', '电动汽车'), ('108', '陀螺仪'), ('109', '空调热泵'), ('110', '芯片光刻'), ('111', '人工智能')]
SER19, VOL19 = '从零造物', '第十九季 · 第六层：聪明的机器'
ELEC = (90, 160, 240)
HOLE = (230, 120, 90)
RED_L, GRN_L, BLU_L = (240, 70, 60), (90, 210, 110), (80, 130, 250)
PASTE = (235, 235, 240)

def photon(c, x0, y0, x1, y1, col, w=3):
    n = 40
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    pts = [(x0 + dx * k / n - uy * 12 * math.sin(k * 0.9), y0 + dy * k / n + ux * 12 * math.sin(k * 0.9)) for k in range(n + 1)]
    c.line(pts, col, w)
    c.arrow(pts[-2][0], pts[-2][1], x1 + ux * 10, y1 + uy * 10, col, w, 14)

# ---------------------------------------------------------------- E102 LED
def e102_band(c, t, i):
    corner_tag(c, '第 102 集 · 电子落一级台阶')
    c.text(60, 96, '电子从高台阶落到低台阶，多出来的能量变成一粒光', 'serif', 40, INK)
    LEDS = [('红光', 1.8, RED_L), ('绿光', 2.2, GRN_L), ('蓝光', 2.8, BLU_L)]
    for k, (nm, gap, col) in enumerate(LEDS):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        x0 = 160 + k * 560
        yv = 760
        yc = yv - gap * 150
        c.rect(x0, yc - 60, x0 + 420, yc, fill=mix(BG, ELEC, 0.25 * a))
        c.rect(x0, yv, x0 + 420, yv + 60, fill=mix(BG, HOLE, 0.25 * a))
        c.text(x0 + 210, yc - 80, '高台阶（导带）', 'sans', 20, mix(BG, MUTED, a), 'mm')
        c.text(x0 + 210, yv + 90, '低台阶（价带）', 'sans', 20, mix(BG, MUTED, a), 'mm')
        c.arrow(x0 - 30, yv, x0 - 30, yc, mix(BG, INK, a), 2, 12)
        c.arrow(x0 - 30, yc, x0 - 30, yv, mix(BG, INK, a), 2, 12)
        c.text(x0 - 40, (yc + yv) / 2, f'{gap}', 'mono', 22, mix(BG, INK, a), 'rm')
        ph = ((t - 1 - k * 4) * 0.6) % 1
        ex = x0 + 120 + 180 * min(ph * 2, 1)
        ey = yc - 30 if ph < 0.5 else yc - 30 + (yv + 30 - (yc - 30)) * min((ph - 0.5) * 4, 1)
        c.ellipse(ex, ey, 14, 14, fill=mix(BG, ELEC, a))
        for j in range(4):
            c.ellipse(x0 + 60 + j * 100, yv + 30, 12, 12, outline=mix(BG, HOLE, a), width=3)
        if ph > 0.75:
            photon(c, x0 + 330, (yc + yv) / 2, x0 + 450, (yc + yv) / 2 - 160, mix(BG, col, a), 4)
        c.text(x0 + 210, 920, f'{nm}：台阶高约 {gap} 电子伏', 'bold', 26, mix(BG, col, a), 'mm')
    caps(c, t, [(0, 5, 'LED 里是两种半导体贴在一起：一边电子多，一边「空位」多'),
                (5.2, 12, '通上电，电子越过交界落进空位，就像从高台阶跳到低台阶，多出来的能量变成一粒光'),
                (12.2, 22, '台阶越高，光的能量越大：红光台阶最低，蓝光最高，所以蓝光 LED 要的电压也高（数值拍摄前核对）')], y=1010)

def e102_diode(c, t, i):
    corner_tag(c, '第 102 集 · 只许一个方向')
    c.text(60, 96, 'LED 是二极管：反着接，电子过不去', 'serif', 40, INK)
    for k, rev in enumerate((False, True)):
        x0, y0 = 220 + k * 600, 300
        on = not rev
        c.rect(x0, y0, x0 + 420, y0 + 300, outline=COPPER, width=4)
        c.rect(x0 - 30, y0 + 110, x0 + 30, y0 + 190, fill=SHEET)
        c.text(x0, y0 + 130, '+' if not rev else '−', 'bold', 28, INK, 'mm')
        c.text(x0, y0 + 175, '3V', 'mono', 20, MUTED, 'mm')
        lx, ly = x0 + 420, y0 + 150
        c.poly([(lx - 30, ly - 30), (lx - 30, ly + 30), (lx + 22, ly)], RED_L if on else (90, 90, 90))
        c.line([(lx + 24, ly - 30), (lx + 24, ly + 30)], INK, 5)
        if on and math.sin(t * 6) > -2:
            for j in range(3):
                photon(c, lx + 30, ly - 30 + j * 30, lx + 110, ly - 70 + j * 40, RED_L, 3)
            p = (t * 0.5) % 1
            per = 2 * (420 + 300)
            for j in range(6):
                s = ((p + j / 6) % 1) * per
                if s < 420: px, py = x0 + s, y0
                elif s < 720: px, py = x0 + 420, y0 + (s - 420)
                elif s < 1140: px, py = x0 + 420 - (s - 720), y0 + 300
                else: px, py = x0, y0 + 300 - (s - 1140)
                c.ellipse(px, py, 8, 8, fill=ELEC)
        c.text(x0 + 210, y0 + 360, '正着接：亮' if on else '反着接：不亮', 'bold', 28, GREEN if on else NRED, 'mm')
    a = fade(t, 11, 12)
    if a > 0:
        x0, y0 = 1380, 300
        c.text(x0 + 220, y0, '同样的电，变成了什么（示意）', 'sans', 22, mix(BG, MUTED, a), 'mm')
        for k, (nm, light) in enumerate((('灯泡', 0.1), ('LED', 0.4))):
            y = y0 + 80 + k * 150
            c.text(x0, y, nm, 'bold', 26, mix(BG, INK, a), 'lm')
            c.rect(x0 + 100, y - 24, x0 + 100 + 340 * light, y + 24, fill=mix(BG, SPARK, a))
            c.rect(x0 + 100 + 340 * light, y - 24, x0 + 440, y + 24, fill=mix(BG, NRED, a * 0.7))
        c.text(x0 + 100, y0 + 330, '黄：光   红：热', 'sans', 22, mix(BG, MUTED, a), 'lm')
        c.text(x0 + 220, y0 + 380, '比例以资料为准', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '电子只能从电子多的那边，越过交界去空位多的那边'),
                (6.2, 11, '电池反过来接，电子被往回拉，交界处成了一堵墙：不亮'),
                (11.2, 22, '灯泡靠灯丝烧到两千多度发光，大半的电变成了热；LED 不烧，所以摸上去只是温的')], y=1010)

# ---------------------------------------------------------------- E103 无线充电
def coil(c, cx, cy, w, n, col, a=1.0):
    for k in range(n):
        x = cx - w / 2 + w * (k + 0.5) / n
        c.ellipse(x, cy, 10, 26, outline=mix(BG, col, a), width=4)

def e103_induce(c, t, i):
    corner_tag(c, '第 103 集 · 没有铁芯的变压器')
    c.text(60, 96, '下面线圈里电流来回变，磁场跟着变；上面线圈里就感应出电流', 'serif', 40, INK)
    cx = 760
    yb = 760
    gap = 120 + 260 * fade(t, 12, 18)
    yt = yb - gap
    I = math.sin(t * 4)
    coil(c, cx, yb, 520, 12, COPPER)
    coil(c, cx, yt, 520, 12, COPPER)
    c.text(cx - 330, yb, '底座线圈', 'sans', 22, MUTED, 'rm')
    c.text(cx - 330, yt, '手机线圈', 'sans', 22, MUTED, 'rm')
    for k in range(4):
        r = 80 + k * 70
        strength = abs(I) * (1 - k * 0.2)
        col = mix(BG, (120, 200, 255), 0.7 * strength)
        c.ellipse(cx, yb - 20, r * 1.4, r * 0.9 + 20 * k, outline=col, width=2)
    arrow_dir = 1 if I > 0 else -1
    c.arrow(cx - 200, yb + 60, cx - 200 + 160 * arrow_dir * abs(I), yb + 60, NRED, 4, 14)
    c.text(cx, yb + 110, '交流电：方向一秒换很多次', 'sans', 22, NRED, 'mm')
    coupling = 1 / (1 + ((gap - 120) / 90) ** 3)
    ind = I * coupling
    c.arrow(cx + 200, yt - 60, cx + 200 - 160 * (1 if ind > 0 else -1) * abs(ind), yt - 60, GREEN, 4, 14)
    bx, by = cx + 420, yt
    c.ellipse(bx, by, 40, 40, fill=mix((60, 60, 60), SPARK, abs(ind)), outline=MUTED, width=2)
    c.line([(cx + 260, yt), (bx - 40, by)], COPPER, 3)
    c.text(bx + 60, by, f'感应强度 {coupling * 100:.0f}%', 'mono', 24, INK, 'lm')
    a = fade(t, 12, 13)
    if a > 0:
        c.text(1500, 860, '拉开一点，就弱很多', 'bold', 28, mix(BG, NRED, a), 'mm')
    caps(c, t, [(0, 7, '充电板里的线圈通着交流电，电流一秒钟来回变很多次，周围的磁场也跟着一会儿强一会儿弱'),
                (7.2, 12, '手机里也有个线圈：穿过它的磁场一变，里面就感应出电流，这就是第 4 集的磁生电'),
                (12.2, 22, '两个线圈之间没有铁芯，磁场散得很快：拉开一点，感应就弱很多，所以手机要放正、放近')], y=1010)

def e103_audio(c, t, i):
    corner_tag(c, '第 103 集 · 让音乐「跳」过去')
    c.text(60, 96, '手机的音乐信号也是变化的电流：它也能从一个线圈跳到另一个', 'serif', 40, INK)
    c.rect(140, 400, 300, 700, fill=SHEET, r=20)
    c.text(220, 550, '手机', 'bold', 30, INK, 'mm')
    c.line([(300, 550), (420, 550), (420, 760), (470, 760)], COPPER, 3)
    coil(c, 640, 760, 340, 9, COPPER)
    d = 60 + 280 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi))
    yt = 760 - d
    coil(c, 640, yt, 340, 9, COPPER)
    c.line([(810, yt), (1000, yt), (1000, 470)], COPPER, 3)
    c.poly([(1000, 420), (1060, 380), (1060, 560), (1000, 520)], (180, 180, 190))
    coupling = 1 / (1 + ((d - 60) / 70) ** 3)
    for k in range(3):
        r = 40 + k * 40
        c.arc(1080, 470, r, r, -40, 40, mix(BG, GREEN, coupling * (0.9 - 0.25 * k)), 4)
    xs = [1300 + j * 10 for j in range(50)]
    sig = [560 + 80 * math.sin(j * 0.5 + t * 6) * math.sin(j * 0.13 + t) for j in range(50)]
    c.line(list(zip(xs, sig)), mix(BG, SPARK, 0.9), 3)
    sig2 = [800 + 80 * coupling * math.sin(j * 0.5 + t * 6) * math.sin(j * 0.13 + t) for j in range(50)]
    c.line(list(zip(xs, sig2)), GREEN, 3)
    c.text(1300, 470, '手机送出的信号', 'sans', 22, SPARK, 'lm')
    c.text(1300, 710, '喇叭收到的信号', 'sans', 22, GREEN, 'lm')
    c.text(640, 900, f'两个线圈相距 {d / 60:.1f} 厘米（示意）', 'mono', 24, INK, 'mm')
    caps(c, t, [(0, 7, '把手机耳机口接到一个线圈上：音乐就是一串快速变化的电流'),
                (7.2, 14, '另一个线圈接小喇叭，两个线圈不碰在一起，喇叭里也有音乐'),
                (14.2, 22, '慢慢拉开：音乐越来越小。无线充电板送的是电，原理一模一样（距离以实测为准）')], y=1010)

# ---------------------------------------------------------------- E104 3D 打印
def e104_slice(c, t, i):
    corner_tag(c, '第 104 集 · 切成一层层薄片')
    c.text(60, 96, '先把立体切成许多层，再一层一层挤出来叠上去', 'serif', 40, INK)
    base, cx = 860, 640
    layers = 10
    lh = 50
    prog = fade(t, 3, 19) * layers
    nfull = int(prog)
    for k in range(layers):
        w = 520 * (1 - k / layers)
        y = base - (k + 1) * lh
        if k < nfull:
            c.rect(cx - w / 2, y, cx + w / 2, y + lh - 4, fill=PASTE, r=6)
        else:
            c.rect(cx - w / 2, y, cx + w / 2, y + lh - 4, outline=mix(BG, MUTED, 0.6), width=2, r=6)
    if nfull < layers:
        k = nfull
        w = 520 * (1 - k / layers)
        y = base - (k + 1) * lh
        f = prog - nfull
        c.rect(cx - w / 2, y, cx - w / 2 + w * f, y + lh - 4, fill=PASTE, r=6)
        nx = cx - w / 2 + w * f
        c.poly([(nx - 24, y - 70), (nx + 24, y - 70), (nx, y - 6)], (170, 170, 180))
        c.rect(nx - 30, y - 150, nx + 30, y - 70, fill=(120, 120, 130))
    c.line([(cx - 340, base), (cx + 340, base)], LINE, 4)
    k = min(nfull, layers - 1)
    w = 520 * (1 - k / layers)
    c.rect(1220, 260, 1780, 820, fill=SHEET, r=14)
    c.text(1500, 300, f'第 {k + 1} 层的「切片图」', 'bold', 28, INK, 'mm')
    s = w * 0.8
    c.rect(1500 - s / 2, 560 - s / 2, 1500 + s / 2, 560 + s / 2, outline=SPARK, width=4)
    c.text(1500, 780, '每层只是一张平面图', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 6, '电脑先把要打的东西横着切成许多薄片，每一片就是一张平面图'),
                (6.2, 14, '喷头沿着这一层的图来回走，挤出一条条细丝，铺满这一层'),
                (14.2, 22, '升高一层，再照下一张图挤：几百层叠起来，就成了立体的东西')], y=1010)

def e104_layer(c, t, i):
    corner_tag(c, '第 104 集 · 层越薄，越像')
    c.text(60, 96, '同一个圆顶：层厚不同，台阶的粗细不同', 'serif', 40, INK)
    for k, (nm, n) in enumerate((('层厚 4 毫米', 6), ('层厚 2 毫米', 12), ('层厚 1 毫米', 24))):
        a = fade(t, 1 + k * 3, 2 + k * 3)
        if a <= 0: continue
        cx, base, R = 330 + k * 470, 660, 190
        c.arc(cx, base, R, R, 180, 360, mix(BG, SPARK, a), 3)
        for j in range(n):
            y0 = j * R / n
            w = math.sqrt(max(R * R - (y0 + R / n / 2) ** 2, 0))
            c.rect(cx - w, base - (j + 1) * R / n, cx + w, base - j * R / n, fill=mix(BG, PASTE, a * 0.85))
        c.text(cx, base + 60, nm, 'bold', 26, mix(BG, INK, a), 'mm')
        c.text(cx, base + 100, f'{n} 层', 'mono', 22, mix(BG, MUTED, a), 'mm')
    b = fade(t, 12, 13)
    if b > 0:
        c.rect(260, 820, 1660, 960, fill=mix(BG, SHEET, b), r=12)
        c.text(960, 860, '层越薄越精细，可层数越多、打得越慢', 'sans', 26, mix(BG, INK, b), 'mm')
        c.text(960, 915, '悬空的地方没有下一层托着，要先打「支撑」，打完再掰掉', 'sans', 24, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 4, '圆圆的顶，用一层层平的薄片去拼，边上总有一级级小台阶'),
                (4.2, 11, '层越薄，台阶越细，越接近原来的圆：可要打的层数就多了好几倍'),
                (11.2, 22, '还有一个麻烦：悬在半空的部分底下没东西托着，挤出来就垂下去，要先打一层支撑')], y=1010)


CLIPS = {
 'E102_台阶': (e102_band, 22), 'E102_单向': (e102_diode, 22),
 'E102_片头': (titles.opening(SER19, VOL19, S19A, 0, '1962 年红光 LED · 1993 年蓝光 LED'), 7),
 'E102_片尾': (titles.closing(SER19, VOL19, S19A, 0, '下集：手机放在板子上，没插线怎么就充上电了？'), 7),
 'E103_感应': (e103_induce, 22), 'E103_传音乐': (e103_audio, 22),
 'E103_片头': (titles.opening(SER19, VOL19, S19A, 1, '1831 年法拉第 · 2008 年 Qi 标准'), 7),
 'E103_片尾': (titles.closing(SER19, VOL19, S19A, 1, '下集：一台打印机，怎么「打」出一个杯子？'), 7),
 'E104_切片': (e104_slice, 22), 'E104_层厚': (e104_layer, 22),
 'E104_片头': (titles.opening(SER19, VOL19, S19A, 2, '1984 年立体光刻 · 1988 年熔融沉积'), 7),
 'E104_片尾': (titles.closing(SER19, VOL19, S19A, 2, '下集：手机怎么听懂你说的话？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
