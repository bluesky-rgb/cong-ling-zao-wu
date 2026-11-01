"""第十二季第二批：E75 变压器与交流电、E76 无线电、E77 太阳能电池 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s12a import S12A, SER12, VOL12, COIL

IRON = (120, 125, 135)
PANEL = (40, 70, 130)

def coil(c, x, y0, y1, n, col, side):
    """draw n windings around a vertical core leg at x"""
    for k in range(n):
        y = y0 + (y1 - y0) * (k + 0.5) / n
        c.ellipse(x, y, 60, 9, outline=col, width=4)

# ---------------------------------------------------------------- E75 变压器
def e75_ratio(c, t, i):
    corner_tag(c, '第 75 集 · 匝数比就是电压比')
    c.text(60, 96, '两组线圈绕在同一个铁芯上', 'serif', 40, INK)
    # core
    cx0, cy0, cx1, cy1 = 520, 220, 1000, 760
    c.rect(cx0, cy0, cx1, cy1, outline=IRON, width=40)
    dc = t >= 15
    amp = 1.0 if not dc else 0.0
    n2 = 20 if t < 8 else (5 if t < 15 else 20)
    coil(c, cx0, 330, 650, 10, COIL, -1)
    coil(c, cx1, 330, 650, n2, GREEN, 1)
    c.text(cx0, 810, '10 圈', 'bold', 26, COIL, 'mm')
    c.text(cx1, 810, f'{n2} 圈', 'bold', 26, GREEN, 'mm')
    # flux arrows in core (alternate)
    ph = math.sin(t * 4)
    if not dc:
        for k in range(6):
            d = ((t * 0.6 + k / 6) % 1)
            x = cx0 + (cx1 - cx0) * d
            c.arrow(x, cy0, x + 40 * (1 if ph > 0 else -1), cy0, mix(BG, SPARK, abs(ph)), 3, 10)
    # input / output waveforms
    gx0, gx1 = 1120, 1840
    def wave(yc, a, col, label):
        c.line([(gx0, yc), (gx1, yc)], MUTED, 1)
        if dc:
            pts = [(gx0, yc - 60), (gx1, yc - 60)] if a > 0 else [(gx0, yc), (gx1, yc)]
            seg(c, pts, col, 4)
        else:
            pts = [(gx0 + (gx1 - gx0) * j / 120, yc - a * 60 * math.sin(j / 120 * 4 * math.pi + t * 4)) for j in range(121)]
            seg(c, pts, col, 4)
        c.text(gx0, yc - 110, label, 'bold', 24, col, 'lm')
    wave(330, 1.0, COIL, '输入（10 圈那边）' + ('：电池直流' if dc else '：交流'))
    wave(620, 0 if dc else n2 / 10, GREEN, f'输出（{n2} 圈那边）' + ('：没有电' if dc else f'：电压 × {n2 / 10:g}'))
    caps(c, t, [(0, 8, '左边线圈通交流电，铁芯里的磁场一会儿向左一会儿向右，右边线圈就感应出电（第 04 集磁生电）'),
                (8.2, 15, '右边圈数是左边的几倍，电压就是几倍：20 圈升压，5 圈降压'),
                (15.2, 22, '换成电池的直流电：磁场不变，右边就没有电。所以变压器只能用在交流电上')], y=1010)

def e75_loss(c, t, i):
    corner_tag(c, '第 75 集 · 为什么要高压输电')
    c.text(60, 96, '送同样多的电，电压高一百倍，线上的损失少一万倍', 'serif', 38, INK)
    rows = [('220 伏直接送', 220, 100, NRED), ('升到 22000 伏再送', 22000, 1, GREEN)]
    for k, (name, V, I, col) in enumerate(rows):
        y = 300 + k * 300
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        c.text(120, y - 70, name, 'bold', 30, mix(BG, INK, a), 'lm')
        c.line([(140, y + 20), (1300, y + 20)], mix(BG, COIL, a), 6 if k == 0 else 3)
        n = 14 if k == 0 else 3
        for j in range(n):
            d = (t * (0.8 if k == 0 else 0.8) + j / n) % 1
            c.ellipse(140 + 1160 * d, y + 20, 8, 8, fill=mix(BG, SPARK, a))
        c.text(1340, y - 20, f'电流 {I} 份', 'mono', 26, mix(BG, INK, a), 'lm')
        loss = I * I
        c.text(1340, y + 30, f'发热损失 {loss} 份', 'mono', 26, mix(BG, col, a), 'lm')
        if k == 0:
            rnd = random.Random(int(t * 8))
            for j in range(10):
                x = 160 + rnd.random() * 1120
                c.line([(x, y + 4), (x + 6, y - 30)], mix(BG, NRED, 0.6 * a), 2)
    b = fade(t, 12, 13)
    c.rect(120, 820, 1800, 920, fill=mix(BG, SHEET, b), r=10)
    c.text(150, 850, '功率 = 电压 × 电流；导线发热 ∝ 电流²', 'bold', 28, mix(BG, INK, b), 'lm')
    c.text(150, 895, '电厂升压 → 高压线送很远 → 变电站一级级降压 → 家里 220 伏', 'sans', 24, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 6, '同样要送一份功率：电压低，电流就大，导线就发热，电在路上浪费掉'),
                (6.2, 12, '电压升高一百倍，电流只要百分之一，发热的损失变成万分之一'),
                (12.2, 22, '所以要用交流电：变压器能升压、能降压。1880 年代的「交流电之争」，交流电赢在这里')], y=1010)

# ---------------------------------------------------------------- E76 无线电
def e76_wave(c, t, i):
    corner_tag(c, '第 76 集 · 变化的电流会「发射」')
    c.text(60, 96, '电流不变，什么也不发生；电流一变，就有波飞出去', 'serif', 38, INK)
    x0, y0 = 420, 560
    c.line([(x0, y0 - 220), (x0, y0 + 220)], COIL, 8)
    c.text(x0, y0 + 270, '导线', 'bold', 24, INK, 'mm')
    steady = t < 6
    if steady:
        for j in range(6):
            d = (t * 0.8 + j / 6) % 1
            c.ellipse(x0, y0 - 220 + 440 * d, 8, 8, fill=SPARK)
        c.text(x0 + 60, y0 - 260, '电流一直不变：没有波', 'bold', 26, MUTED, 'lm')
    else:
        # pulses: each scrape at times
        pulses = [6.5, 8.0, 9.0, 10.8, 12.0, 13.5, 15.0, 16.2, 18.0, 19.5]
        for p in pulses:
            if t > p:
                r = (t - p) * 420
                if r < 1250:
                    a = max(0.0, 1 - r / 1250)
                    c.arc(x0, y0, r, r, -60, 60, mix(BG, SPARK, a), 4)
                    c.arc(x0, y0, r, r, 120, 240, mix(BG, SPARK, a * 0.6), 3)
        flash = any(0 < t - p < 0.15 for p in pulses)
        if flash:
            c.ellipse(x0, y0, 30, 30, fill=SPARK)
        c.text(x0 + 60, y0 - 260, '电流突然变化：一圈波飞出去', 'bold', 26, SPARK, 'lm')
    # radio receiver at right
    rx = 1600
    c.rect(rx - 120, y0 - 80, rx + 120, y0 + 80, fill=SHEET, outline=MUTED, width=3, r=12)
    c.line([(rx + 60, y0 - 80), (rx + 120, y0 - 240)], MUTED, 3)
    c.text(rx, y0 + 120, '收音机', 'bold', 24, INK, 'mm')
    if not steady:
        pulses = [6.5, 8.0, 9.0, 10.8, 12.0, 13.5, 15.0, 16.2, 18.0, 19.5]
        hit = any(0 < t - p - (rx - x0) / 420 < 0.25 for p in pulses)
        if hit:
            c.text(rx, y0 - 140, '咔！', 'serif', 48, NRED, 'mm')
    caps(c, t, [(0, 6, '电池接一根导线，电流一直不变：周围什么都没发生'),
                (6.2, 14, '把电池两极在锉刀上一刮，电流一下有一下没：每变一次，就有一圈电磁波飞出去'),
                (14.2, 22, '旁边的收音机收到这圈波，就「咔」一声。1887 年，赫兹第一次用火花证明了电磁波')], y=1010)

def e76_am(c, t, i):
    corner_tag(c, '第 76 集 · 把声音「骑」在电波上')
    c.text(60, 96, '一直发同一种快速的波，再让它的大小跟着声音变', 'serif', 38, INK)
    gx0, gx1 = 200, 1760
    rows = [(290, '声音（慢）', COPPER), (560, '载波（很快的电磁波）', FIELD), (840, '调幅：载波的大小跟着声音变', SPARK)]
    for k, (y, name, col) in enumerate(rows):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        c.text(gx0, y - 110, name, 'bold', 26, mix(BG, INK, a), 'lm')
        pts = []
        for j in range(601):
            u = j / 600
            s_ = math.sin(u * 3 * 2 * math.pi + t)
            car = math.sin(u * 60 * 2 * math.pi)
            v = s_ if k == 0 else (car if k == 1 else (0.55 + 0.4 * s_) * car)
            pts.append((gx0 + (gx1 - gx0) * u, y - 80 * v))
        seg(c, pts, mix(BG, col, a), 2 if k else 4)
        if k == 2:
            env = [(gx0 + (gx1 - gx0) * j / 200, y - 80 * (0.55 + 0.4 * math.sin(j / 200 * 3 * 2 * math.pi + t))) for j in range(201)]
            seg(c, env, mix(BG, COPPER, a), 3)
    caps(c, t, [(0, 5, '声音变化得慢：每秒几百到几千次'),
                (5.2, 9, '电台一直发一种很快的电磁波：中波每秒约一百万次'),
                (9.2, 22, '让这种快波的大小跟着声音起伏，就是调幅（AM）。收音机把起伏取出来，声音就回来了')], y=1010)

# ---------------------------------------------------------------- E77 太阳能电池
def e77_junction(c, t, i):
    corner_tag(c, '第 77 集 · 光把电子「打」出来')
    c.text(60, 96, '阳光照到硅片上，电子被推到一边：两边就有了电压', 'serif', 38, INK)
    x0, x1 = 300, 1300
    yn0, yn1, yp1 = 380, 520, 760
    c.rect(x0, yn0, x1, yn1, fill=mix(BG, (90, 120, 200), 0.6), r=6)
    c.rect(x0, yn1, x1, yp1, fill=mix(BG, (200, 110, 90), 0.5), r=6)
    c.text(x0 - 20, (yn0 + yn1) / 2, 'N 层', 'bold', 26, INK, 'rm')
    c.text(x0 - 20, (yn1 + yp1) / 2, 'P 层', 'bold', 26, INK, 'rm')
    c.line([(x0, yn1), (x1, yn1)], SPARK, 2)
    c.text(x1 + 20, yn1, '交界处：把电子往上推', 'sans', 22, SPARK, 'lm')
    # sun & photons
    c.ellipse(170, 270, 50, 50, fill=SPARK)
    rnd = random.Random(77)
    for k in range(8):
        ph = (t * 0.9 + k / 8) % 1
        sx, sy = 260 + k * 120, 250
        ex, ey = sx + 200, 600
        x = sx + (ex - sx) * ph; y = sy + (ey - sy) * ph
        if y < yn0 + 140:
            c.line([(x - 18, y - 36), (x, y)], SPARK, 3)
        else:
            # electron freed and pushed up to N side, then into the wire
            q = min(1, (ph - 0.88) / 0.12) if ph > 0.88 else 0
            c.ellipse(x, y - 160 * q, 9, 9, fill=FIELD)
    # external circuit
    c.line([(x1, yn0 + 20), (1600, yn0 + 20), (1600, 520)], COPPER, 5)
    c.line([(x1, yp1 - 20), (1600, yp1 - 20), (1600, 640)], COPPER, 5)
    c.ellipse(1600, 580, 50, 50, outline=INK, width=3)
    spin = t * 6
    c.line([(1600 - 40 * math.cos(spin), 580 - 40 * math.sin(spin)), (1600 + 40 * math.cos(spin), 580 + 40 * math.sin(spin))], INK, 4)
    c.text(1680, 580, '小电机', 'bold', 24, INK, 'lm')
    for k in range(8):
        d = (t * 0.7 + k / 8) % 1
        L = [300, 140, 120, 240, 300]
        path = [(x1, yn0 + 20), (1600, yn0 + 20), (1600, 520), (1600, 640), (1600, yp1 - 20), (x1, yp1 - 20)]
        segs = list(zip(path, path[1:]))
        lens = [math.hypot(b[0] - a_[0], b[1] - a_[1]) for a_, b in segs]
        s_ = d * sum(lens)
        for (a_, b), Ls in zip(segs, lens):
            if s_ <= Ls:
                f = s_ / Ls
                c.ellipse(a_[0] + (b[0] - a_[0]) * f, a_[1] + (b[1] - a_[1]) * f, 7, 7, fill=FIELD)
                break
            s_ -= Ls
    caps(c, t, [(0, 7, '太阳能电池是两层不一样的硅：上面 N 层，下面 P 层，交界处像一道只能往上走的坡'),
                (7.2, 14, '阳光的光子打进硅里，把电子打松；交界处把电子推到上面那层'),
                (14.2, 22, '上下两层就有了电压，接上导线，电子绕一圈回来，电机就转了：没有燃烧，没有转动的零件')], y=1010)

def e77_angle(c, t, i):
    corner_tag(c, '第 77 集 · 正对太阳电最多')
    c.text(60, 96, '板子斜了，接到的阳光就少了', 'serif', 40, INK)
    ang = math.radians(80 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi)))
    cx, cy = 600, 620
    L = 220
    # sun rays from above
    for k in range(9):
        x = 340 + k * 65
        c.line([(x, 180), (x, 560)], mix(BG, SPARK, 0.6), 2)
    px = L * math.cos(ang); py = L * math.sin(ang)
    c.line([(cx - px, cy - py), (cx + px, cy + py)], PANEL, 14)
    c.line([(cx - px, cy + 140), (cx + px, cy + 140)], NRED, 6)
    c.text(cx, cy + 180, '板子「挡住」的阳光宽度 = 长度 × cos(角度)', 'sans', 22, NRED, 'mm')
    c.text(cx, 210, f'倾斜 {math.degrees(ang):.0f}°', 'mono', 30, INK, 'mm')
    # graph
    gx0, gx1, gy0, gy1 = 1100, 1800, 260, 760
    c.line([(gx0, gy1), (gx1, gy1)], MUTED, 2); c.line([(gx0, gy0), (gx0, gy1)], MUTED, 2)
    pts = [(gx0 + (gx1 - gx0) * d / 90, gy1 - (gy1 - gy0) * math.cos(math.radians(d))) for d in range(91)]
    seg(c, pts, SPARK, 4)
    for d in (0, 30, 60, 90):
        c.text(gx0 + (gx1 - gx0) * d / 90, gy1 + 30, f'{d}°', 'mono', 20, MUTED, 'mm')
    c.text(gx0, gy0 - 26, '发电功率（正对太阳 = 100%）', 'sans', 22, MUTED, 'lm')
    dx = gx0 + (gx1 - gx0) * math.degrees(ang) / 90
    dy = gy1 - (gy1 - gy0) * math.cos(ang)
    c.ellipse(dx, dy, 12, 12, fill=GREEN)
    c.text(dx + 20, dy - 20, f'{math.cos(ang) * 100:.0f}%', 'bold', 26, GREEN, 'lm')
    caps(c, t, [(0, 8, '板子正对太阳，接到的阳光最多'),
                (8.2, 15, '斜过去，同样大的板子「挡住」的阳光变窄了：功率按 cos 角度变小'),
                (15.2, 22, '斜 60 度只剩一半；所以太阳能板要朝南、按纬度倾斜（北半球），有的还会跟着太阳转')], y=1010)

CLIPS = {
 'E75_匝数比': (e75_ratio, 22), 'E75_输电': (e75_loss, 22),
 'E75_片头': (titles.opening(SER12, VOL12, S12A, 3, '1880 年代 · 交流电之争（高压只用动画）'), 7),
 'E75_片尾': (titles.closing(SER12, VOL12, S12A, 3, '下集：没有导线，信号怎么飞过去？'), 7),
 'E76_电磁波': (e76_wave, 22), 'E76_调幅': (e76_am, 22),
 'E76_片头': (titles.opening(SER12, VOL12, S12A, 4, '1887 年赫兹 · 1895 年马可尼'), 7),
 'E76_片尾': (titles.closing(SER12, VOL12, S12A, 4, '下集：一块板子，怎么把阳光变成电？'), 7),
 'E77_光子': (e77_junction, 22), 'E77_角度': (e77_angle, 22),
 'E77_片头': (titles.opening(SER12, VOL12, S12A, 5, '1954 年 · 贝尔实验室'), 7),
 'E77_片尾': (titles.closing(SER12, VOL12, S12A, 5, '下集：发动机里，为什么要「点火」？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
