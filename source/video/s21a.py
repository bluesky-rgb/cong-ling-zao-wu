"""第二十一季（第七层：身边的未来）第一批：E112 手机信号、E113 指纹识别、E114 心率手环 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S21A = [('112', '手机信号'), ('113', '指纹识别'), ('114', '心率手环'), ('115', '平衡车'), ('116', '墨水屏'),
        ('117', '石墨烯'), ('118', '虚拟现实'), ('119', '加密'), ('120', '核电站'), ('121', '太空望远镜')]
SER21, VOL21 = '从零造物', '第二十一季 · 第七层：身边的未来'
CELLC = [(90, 150, 220), (230, 160, 70), (110, 190, 120)]
WAVE = (120, 190, 240)
METAL = (170, 175, 185)
SKIN = (220, 170, 140)
BLOOD = (200, 60, 60)

# ---------------------------------------------------------------- E112 手机信号
def _hex(cx, cy, r):
    return [(cx + r * math.cos(math.radians(60 * k + 30)), cy + r * math.sin(math.radians(60 * k + 30))) for k in range(6)]

def e112_cells(c, t, i):
    corner_tag(c, '第 112 集 · 一格一座基站')
    c.text(60, 96, '城市被分成许多小格；相邻格子用不同频率，隔开一格就能重复用', 'serif', 40, INK)
    r = 105
    cells = []
    for q in range(-1, 10):
        for rr in range(0, 5):
            cx = 160 + q * r * math.sqrt(3) + (rr % 2) * r * math.sqrt(3) / 2
            cy = 290 + rr * r * 1.5
            if 60 < cx < 1860 and 250 < cy < 900:
                qa = q - (rr - (rr & 1)) // 2
                col = CELLC[(qa - rr) % 3]
                cells.append((cx, cy, col))
    for cx, cy, col in cells:
        c.poly(_hex(cx, cy, r - 3), mix(BG, col, 0.22))
        c.line(_hex(cx, cy, r - 3) + [_hex(cx, cy, r - 3)[0]], mix(BG, col, 0.7), 2)
        c.line([(cx, cy + 20), (cx, cy - 20)], INK, 3)
        c.poly([(cx - 12, cy + 20), (cx + 12, cy + 20), (cx, cy - 4)], INK)
    px = 200 + 1500 * (t / 22)
    py = 560 + 120 * math.sin(t * 0.5)
    best = min(cells, key=lambda e: (e[0] - px) ** 2 + (e[1] - py) ** 2)
    c.line([(px, py), (best[0], best[1] - 20)], best[2], 4)
    c.rect(px - 18, py - 30, px + 18, py + 30, fill=SHEET, outline=INK, width=3, r=6)
    c.rect(1500, 920, 1860, 980, fill=SHEET, r=10)
    c.text(1680, 950, f'正在连：{["蓝", "橙", "绿"][CELLC.index(best[2])]}色频率', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '手机信号不是从天上来的，来自几百米到几公里外的基站'),
                (7.2, 14, '每座基站管一小块地方，整座城市像一张蜂窝；相邻的格子用不同频率，不打架'),
                (14.2, 22, '你一边走，手机一边换格子，电话不断：这叫切换')], y=1010)

def e112_cage(c, t, i):
    corner_tag(c, '第 112 集 · 金属盒子挡住电磁波')
    c.text(60, 96, '电磁波碰到金属，就在金属里推动电子来回跑，被挡了回去', 'serif', 40, INK)
    for k, (nm, metal) in enumerate((('纸盒', False), ('铁皮盒', True))):
        x0 = 140 + k * 900
        bx0, bx1, by0, by1 = x0 + 420, x0 + 640, 380, 720
        c.rect(bx0, by0, bx1, by1, outline=METAL if metal else (200, 180, 140), width=10 if metal else 4)
        c.rect(bx0 + 80, by0 + 110, bx0 + 140, by0 + 230, fill=SHEET, outline=INK, width=3, r=6)
        for j in range(5):
            ph = (t * 1.5 + j * 0.6) % 3
            xw = x0 + 40 + ph * 200
            if metal and xw > bx0:
                continue
            pts = [(xw + 14 * math.sin(s * 0.3), by0 + 20 + s * 10) for s in range(31)]
            c.line(pts, mix(BG, WAVE, 1 - ph / 3), 3)
        if metal:
            for j in range(6):
                y = by0 + 30 + j * 52
                d = 16 * math.sin(t * 6 + j)
                c.line([(bx0 - 4, y + d), (bx0 - 4, y + d + 20)], SPARK, 4)
            c.text(bx0 - 20, by1 + 50, '金属里的电子来回跑', 'sans', 22, SPARK, 'mm')
            c.text((bx0 + bx1) / 2, by0 + 290, '无服务', 'bold', 26, NRED, 'mm')
        else:
            c.text((bx0 + bx1) / 2, by0 + 290, '有信号', 'bold', 26, GREEN, 'mm')
        c.text((bx0 + bx1) / 2, by0 - 40, nm, 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '电磁波能穿过纸、塑料、木头，所以在屋里也能打电话'),
                (7.2, 14, '碰到金属就不行了：波推动金属里的自由电子来回跑，电子产生的波又把它抵消、挡回去'),
                (14.2, 22, '四面都是金属的盒子，叫法拉第笼。电梯里信号差，也是这个原因（缝留大了会漏，以实测为准）')], y=1010)

# ---------------------------------------------------------------- E113 指纹识别
def ridge(x):
    return 0.5 + 0.5 * math.sin(x * 0.11)

def e113_cap(c, t, i):
    corner_tag(c, '第 113 集 · 用电容「摸」出指纹')
    c.text(60, 96, '凸起的纹（脊）离传感器近，电容大；凹下的谷离得远，电容小', 'serif', 40, INK)
    y0 = 520
    pts = [(x, y0 - 40 - 50 * ridge(x)) for x in range(120, 1160, 6)]
    c.poly(pts + [(1160, 240), (120, 240)], SKIN)
    c.line(pts, mix(SKIN, INK, 0.3), 3)
    c.rect(120, y0 - 10, 1160, y0 + 30, fill=METAL)
    n = 26
    w = 1040 / n
    sc = int(fade(t, 3, 14) * n)
    for k in range(n):
        x = 120 + k * w + w / 2
        v = ridge(x)
        c.rect(120 + k * w + 3, y0 + 40, 120 + (k + 1) * w - 3, y0 + 80, fill=mix(BG, SPARK, v) if k < sc else mix(BG, LINE, 0.4))
        if k == sc and k < n:
            c.line([(x, y0 - 40 - 50 * v), (x, y0 - 10)], GREEN, 3)
    c.text(640, y0 + 120, '传感器上的每一个小格，量出一个电容值', 'sans', 22, MUTED, 'mm')
    a = fade(t, 12, 13)
    if a > 0:
        gx, gy, cs = 1320, 300, 18
        for rr in range(26):
            for qq in range(26):
                x = gx + qq * cs; y = gy + rr * cs
                d = math.hypot(qq - 13, (rr - 15) * 1.2)
                v = 0.5 + 0.5 * math.sin(d * 1.3)
                c.rect(x, y, x + cs - 1, y + cs - 1, fill=mix(BG, mix(BG, SPARK, v), a))
        c.text(gx + 13 * cs, gy + 26 * cs + 40, '拼出来：一张指纹图', 'bold', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '手指按在传感器上：纹路凸起的地方贴得近，凹下的地方隔着一点空气'),
                (6.2, 13, '传感器上有成千上万个小电极，像第 96 集触摸屏那样量电容：近的电容大，远的电容小'),
                (13.2, 22, '把每个小格的读数拼起来，就是一张指纹图')], y=1010)

MIN = [(0.3, 0.4, '分叉'), (0.55, 0.3, '终点'), (0.7, 0.6, '分叉'), (0.4, 0.7, '终点'), (0.6, 0.8, '分叉')]

def _print(c, cx, cy, R, a, mark=None, rot=0.0):
    for k in range(9):
        rr = 30 + k * 26
        c.arc(cx, cy, rr, rr * 1.25, 200 + rot, 520 + rot, mix(BG, SKIN, a), 4)
    if mark:
        for (u, v, kind) in MIN:
            x = cx - R + 2 * R * u; y = cy - R * 1.2 + 2.4 * R * v * 0.9
            col = GREEN if kind == '分叉' else NRED
            c.ellipse(x, y, 14, 14, outline=mix(BG, col, mark), width=4)

def e113_points(c, t, i):
    corner_tag(c, '第 113 集 · 比的是特征点')
    c.text(60, 96, '不比整张图：记下纹路在哪里分叉、在哪里断开', 'serif', 40, INK)
    a = fade(t, 1, 2)
    _print(c, 480, 560, 250, a, fade(t, 4, 6))
    c.text(480, 900, '登记时记下的', 'bold', 26, INK, 'mm')
    b = fade(t, 8, 9)
    if b > 0:
        _print(c, 1180, 560, 250, b, fade(t, 9, 11), rot=8)
        c.text(1180, 900, '这次按下的', 'bold', 26, mix(BG, INK, b), 'mm')
    m = fade(t, 12, 16)
    if m > 0:
        for (u, v, kind) in MIN:
            x1 = 480 - 250 + 500 * u; y1 = 560 - 300 + 600 * v * 0.9
            x2 = 1180 - 250 + 500 * u; y2 = y1
            c.line([(x1, y1), (x1 + (x2 - x1) * m, y2)], mix(BG, SPARK, 0.7), 2)
        c.rect(1480, 360, 1860, 620, fill=mix(BG, SHEET, m), r=14)
        c.text(1670, 410, '对上的特征点', 'sans', 24, mix(BG, MUTED, m), 'mm')
        c.text(1670, 490, f'{int(5 * m)} / 5', 'mono', 48, mix(BG, GREEN, m), 'mm')
        c.text(1670, 570, '够多就解锁', 'bold', 26, mix(BG, INK, m), 'mm')
    caps(c, t, [(0, 7, '每个人的指纹纹路，在哪里分叉、在哪里断开，位置都不一样：这些叫特征点'),
                (7.2, 12, '手机第一次登记时只记下特征点的位置和方向，不存整张照片'),
                (12.2, 22, '下次按上来，哪怕歪一点、只按了一部分，只要对上的特征点够多，就认出是你')], y=1010)

# ---------------------------------------------------------------- E114 心率手环
def pulse(tt, bpm=72):
    ph = (tt * bpm / 60) % 1
    return math.exp(-((ph - 0.15) / 0.06) ** 2) + 0.35 * math.exp(-((ph - 0.45) / 0.08) ** 2)

def e114_ppg(c, t, i):
    corner_tag(c, '第 114 集 · 光照进皮肤')
    c.text(60, 96, '每跳一次，血管里的血多一点，吸走的光就多一点', 'serif', 40, INK)
    c.rect(100, 280, 900, 820, fill=SKIN, r=40)
    p = pulse(t)
    vr = 70 + 26 * p
    c.ellipse(500, 560, 260, vr, fill=mix(BLOOD, SKIN, 0.2))
    c.text(500, 560, '血管', 'bold', 26, (250, 230, 230), 'mm')
    c.rect(330, 830, 430, 880, fill=(90, 220, 120), r=8)
    c.text(380, 920, '绿光 LED', 'sans', 20, MUTED, 'mm')
    c.rect(570, 830, 670, 880, fill=(60, 60, 70), r=8)
    c.text(620, 920, '光传感器', 'sans', 20, MUTED, 'mm')
    for k in range(4):
        x0 = 360 + k * 14
        c.line([(x0, 830), (x0 + 60, 700), (x0 + 200, 700 + k * 6), (600 + k * 10, 830)], mix(BG, (90, 220, 120), 0.8 - 0.4 * p), 2)
    ox, oy, W, H = 1020, 640, 820, 300
    c.line([(ox, oy), (ox + W, oy)], LINE, 2)
    pts = []
    for j in range(120):
        tt = t - (119 - j) * 0.03
        pts.append((ox + W * j / 119, oy - H * 0.8 * (1 - 0.6 * pulse(tt))))
    c.line(pts, (90, 220, 120), 4)
    c.text(ox + W / 2, oy + 40, '传感器收到的光（越低 = 血越多）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '手环背面有绿色的 LED，光照进手腕的皮肤'),
                (7.2, 14, '心脏一跳，血涌进血管，血管变粗，吸走的绿光变多，反射回来的就少'),
                (14.2, 22, '旁边的光传感器一直在量：亮、暗、亮、暗，跟着心跳一起一伏')], y=1010)

def e114_count(c, t, i):
    corner_tag(c, '第 114 集 · 数波峰')
    c.text(60, 96, '数 10 秒里有几个波峰，乘 6，就是一分钟的心跳', 'serif', 40, INK)
    ox, oy, W, H = 140, 600, 1640, 220
    c.line([(ox, oy), (ox + W, oy)], LINE, 2)
    move = fade(t, 12, 13) * (1 - fade(t, 18, 19))
    rnd = random.Random(int(t * 10))
    pts = []
    peaks = 0
    span = 10.0
    prog = min(1, fade(t, 1, 10))
    N = int(400 * prog)
    for j in range(N):
        tt = j / 400 * span
        v = pulse(tt)
        noise = move * 0.35 * math.sin(tt * 9) + move * 0.15 * math.sin(tt * 23)
        pts.append((ox + W * j / 400, oy - H * 0.8 * (v + noise) / 1.2))
    if len(pts) > 1:
        c.line(pts, (90, 220, 120), 4)
    for k in range(12):
        tp = (k + 0.15) * 60 / 72
        if tp < span * prog:
            x = ox + W * tp / span
            c.ellipse(x, oy - H * 0.8 / 1.2 - 20, 10, 10, fill=SPARK)
            peaks += 1
    c.rect(700, 700, 1220, 900, fill=SHEET, r=14)
    c.text(960, 745, f'10 秒里 {peaks} 个波峰', 'mono', 30, INK, 'mm')
    c.text(960, 810, f'× 6 = {peaks * 6} 次 / 分钟', 'mono', 34, SPARK, 'mm')
    if move > 0.1:
        c.text(960, 870, '手一动，波形就乱：要用陀螺仪把晃动减掉', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 10, '把光的起伏画成一条曲线，每个高高的波峰就是一次心跳'),
                (10, 16, '数 10 秒里有几个，乘 6：一分钟 72 次左右'),
                (16, 22, '跑步时手在晃，光也跟着晃：手环再用第 108 集的陀螺仪读出晃动，把它从曲线里减掉')], y=1010)


CLIPS = {
 'E112_蜂窝': (e112_cells, 22), 'E112_屏蔽': (e112_cage, 22),
 'E112_片头': (titles.opening(SER21, VOL21, S21A, 0, '1973 年第一通手机电话 · 蜂窝网络'), 7),
 'E112_片尾': (titles.closing(SER21, VOL21, S21A, 0, '下集：手机为什么一摸就认出是你？'), 7),
 'E113_电容': (e113_cap, 22), 'E113_特征点': (e113_points, 22),
 'E113_片头': (titles.opening(SER21, VOL21, S21A, 1, '1892 年高尔顿《指纹》· 手机指纹解锁'), 7),
 'E113_片尾': (titles.closing(SER21, VOL21, S21A, 1, '下集：手环贴着手腕，怎么知道心跳多快？'), 7),
 'E114_光电': (e114_ppg, 22), 'E114_数心跳': (e114_count, 22),
 'E114_片头': (titles.opening(SER21, VOL21, S21A, 2, '光电容积脉搏波 · 智能手表'), 7),
 'E114_片尾': (titles.closing(SER21, VOL21, S21A, 2, '下集：两个轮子并排的平衡车，为什么不往前倒？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
