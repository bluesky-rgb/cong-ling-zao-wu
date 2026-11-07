"""第二十六季（古法解密 10.0：担、桥、风、律）第一批：B100 扁担、B101 搓麻绳、B102 蓑衣 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB26 = [('B100', '扁担'), ('B101', '搓麻绳'), ('B102', '蓑衣'), ('B103', '虹桥'), ('B104', '摇橹'),
        ('B105', '相风乌'), ('B106', '方升'), ('B107', '三分损益'), ('B108', '鼓'), ('B109', '饾版套色')]
VOL26 = '第二十六季 · 古法解密 10.0'
BAMBOO = (200, 180, 100)
WOOD = (175, 125, 75)
WATER = (70, 130, 200)
WATER_L = (110, 170, 230)
FIBER = (210, 190, 150)
FIBER2 = (180, 150, 110)
STRAW = (200, 170, 90)
SKIN = (225, 180, 150)


def _bucket(c, x, y, w=60, h=70):
    c.poly([(x - w / 2, y), (x + w / 2, y), (x + w / 2 - 8, y + h), (x - w / 2 + 8, y + h)], WOOD)
    c.rect(x - w / 2 + 6, y + 4, x + w / 2 - 6, y + 16, fill=WATER_L)


# ---------------------------------------------------------------- B100 扁担
def b100_buffer(c, t, i):
    corner_tag(c, 'B100 · 软一点，冲击就小了')
    c.text(60, 96, '走路时肩膀一上一下地颠：硬木棍把颠簸原样传给水桶，软竹扁担自己弯一弯，把冲击吸掉一大半', 'serif', 36, INK)
    w = 2 * math.pi * 1.8
    A = 14
    yh = A * math.sin(w * t)
    r = 2.0                                     # 颠的节奏是扁担自己颤的节奏的 2 倍（示意）
    yl = -A / (r * r - 1) * math.sin(w * t)    # 稳态响应（无阻尼示意）
    for row, (flex, label) in enumerate(((False, '硬木棍'), (True, '软竹扁担'))):
        cx = 480
        cy = 330 + row * 320
        sy = cy + yh
        c.text(120, cy - 110, label, 'bold', 26, INK, 'lm')
        c.ellipse(cx, sy - 60, 26, 26, fill=SKIN)
        c.rect(cx - 22, sy - 34, cx + 22, sy + 70, fill=mix(BG, SKIN, 0.6), r=10)
        ey = sy if not flex else cy + yl
        pts = []
        for j in range(41):
            u = (j - 20) / 20
            y = sy + (ey - sy) * (abs(u) ** 1.6)
            pts.append((cx + 300 * u, y))
        c.line(pts, BAMBOO if flex else WOOD, 8)
        for s in (-1, 1):
            bx = cx + 300 * s
            c.line([(bx, ey), (bx, ey + 40)], MUTED, 2)
            _bucket(c, bx, ey + 40)
    gx0, gx1 = 1000, 1840
    c.rect(960, 220, 1880, 900, fill=SHEET, r=14)
    c.text(1420, 256, '肩膀受的力（示意）', 'bold', 24, INK, 'mm')
    for row, flex in enumerate((False, True)):
        gy = 440 + row * 300
        c.line([(gx0, gy), (gx1, gy)], LINE, 1)
        c.text(gx0, gy - 130, '硬木棍' if not flex else '软竹扁担', 'sans', 20, MUTED, 'lm')
        pts = []
        for j in range(301):
            s = t - 3 + 3 * j / 300
            if flex:
                f = (A * w * w) / (r * r - 1) * math.sin(w * s) / (A * w * w)
            else:
                f = math.sin(w * s)
            pts.append((gx0 + (gx1 - gx0) * j / 300, gy - 100 * f))
        c.line(pts, NRED if not flex else GREEN, 3)
    c.text(1420, 860, '起伏越小，肩膀越不累', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '人走路时，肩膀每一步都在上下颠；硬木棍跟着颠，两桶水也跟着一下下往下砸'),
                (7.2, 14, '竹扁担会弯：肩膀往上顶时它先弯下去，桶几乎还留在原地，冲击被竹子吸走了'),
                (14.2, 22, '颠的节奏比竹子自己颤得快很多时，肩上受力的起伏只剩下一小部分（比例为示意，以实测为准）')], y=1010)


def b100_rhythm(c, t, i):
    corner_tag(c, 'B100 · 节奏不对，反而越颤越大')
    c.text(60, 96, '每根扁担都有自己颤的快慢：颠的节奏和它差不多时越颤越大；比它快很多，颤动就被「隔开」了', 'serif', 36, INK)
    gx0, gx1, gy0, gy1 = 240, 1400, 860, 260
    c.rect(180, 220, 1460, 920, fill=SHEET, r=14)
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text(820, 900, '颠的节奏 ÷ 扁担自己颤的节奏', 'sans', 20, MUTED, 'mm')
    c.text(gx0 + 10, gy1 - 10, '传到桶上的颤动（倍）', 'sans', 20, MUTED, 'lm')
    z = 0.15
    def T(r):
        return math.sqrt((1 + (2 * z * r) ** 2) / ((1 - r * r) ** 2 + (2 * z * r) ** 2))
    rmax, tmax = 3.0, 4.0
    pts = [(gx0 + (gx1 - gx0) * (k / 300 * rmax) / rmax, gy0 - (gy0 - gy1) * min(T(k / 300 * rmax), tmax) / tmax) for k in range(1, 301)]
    c.line(pts, SPARK, 4)
    y1 = gy0 - (gy0 - gy1) * 1 / tmax
    seg(c, [(gx0, y1), (gx1, y1)], mix(BG, LINE, 0.8), 2)
    c.text(gx1 - 4, y1 - 18, '1 倍：和硬棍一样', 'sans', 18, MUTED, 'rm')
    for rr, lab in ((1, '1'), (2, '2'), (3, '3')):
        x = gx0 + (gx1 - gx0) * rr / rmax
        c.text(x, gy0 + 22, lab, 'mono', 18, MUTED, 'mm')
    r = 0.3 + 2.6 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi))
    tv = min(T(r), tmax)
    mx = gx0 + (gx1 - gx0) * r / rmax
    my = gy0 - (gy0 - gy1) * tv / tmax
    c.ellipse(mx, my, 12, 12, fill=SPARK)
    c.rect(1520, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1690, 340, f'节奏比 {r:.1f}', 'mono', 28, INK, 'mm')
    c.text(1690, 400, f'桶的颤动 ×{T(r):.1f}', 'mono', 26, SPARK, 'mm')
    msg = '差不多：越颤越大' if 0.75 < r < 1.3 else ('快很多：被隔开' if r > 1.6 else '太慢：跟着一起颠')
    c.text(1690, 470, msg, 'bold', 24, NRED if 0.75 < r < 1.3 else (GREEN if r > 1.6 else INK), 'mm')
    amp = 40 * min(T(r), 3) / 3
    c.line([(1580, 560 + amp * math.sin(t * 9)), (1800, 560 - amp * math.sin(t * 9))], BAMBOO, 6)
    caps(c, t, [(0, 7, '把扁担一头挂上水桶，轻轻一碰，它会自己按某个快慢上下颤，就像秋千有自己的节奏'),
                (7.2, 14, '肩膀颠的节奏和它差不多时，每一下都推在点子上，越颤越大，水都会泼出来'),
                (14.2, 22, '比它快很多时，桶几乎不跟着颠：挑担的人会调整步子，避开越颤越大的那个节奏（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B101 搓麻绳
def b101_twist(c, t, i):
    corner_tag(c, 'B101 · 拧紧，纤维就互相抓住了')
    c.text(60, 96, '短纤维一根根挨着：不拧时一拉就滑开；拧紧以后，纤维被挤在一起，摩擦力让它们抓住彼此', 'serif', 36, INK)
    pull = min(1, max(0, (t % 11 - 4) / 4))
    rnd = random.Random(5)
    fibers = [(rnd.uniform(-1, 0.6), rnd.uniform(-1, 1)) for _ in range(28)]
    for row, twisted in enumerate((False, True)):
        cy = 360 + row * 330
        c.text(120, cy - 130, '不拧' if not twisted else '拧紧', 'bold', 26, INK, 'lm')
        x0, x1 = 200, 1400
        for k, (u0, v) in enumerate(fibers):
            L = 0.4
            if twisted:
                sx = 1.0 + 0.04 * pull
            else:
                sx = 1.0 + 0.6 * pull * (1 if u0 > -0.2 else -0.3)
            pts = []
            for j in range(21):
                u = u0 + L * j / 20
                x = 800 + 600 * u * (sx if u > 0 else (1 if twisted else 1 + 0.25 * pull))
                if not twisted:
                    y = cy + 60 * v
                else:
                    y = cy + 40 * math.sin(u * 14 + v * 3 + k)
                pts.append((x, y))
            c.line(pts, FIBER if k % 2 else FIBER2, 3)
        c.rect(150, cy - 70, 200, cy + 70, fill=(90, 90, 100))
        c.arrow(1420, cy, 1420 + 120 * pull + 20, cy, SPARK, 4, 14)
        res = '一拉就散' if not twisted else '拉不动'
        if pull > 0.6:
            c.text(1560, cy, res, 'bold', 26, NRED if not twisted else GREEN, 'lm')
    caps(c, t, [(0, 7, '麻、棉这些纤维都很短，最长的也就几厘米到几十厘米（拍摄前核对），一根根并排放着，轻轻一拉就滑开'),
                (7.2, 14, '朝一个方向拧起来，纤维被绕成螺旋，你一拉，它们反而往里挤得更紧'),
                (14.2, 22, '挤得越紧，纤维之间的摩擦力越大，谁也滑不动：短纤维就成了长长的结实绳子（示意）')], y=1010)


def b101_ply(c, t, i):
    corner_tag(c, 'B101 · 两股反着一合，就松不开')
    c.text(60, 96, '一股拧紧的线一松手就想转回去；把两股拧好的线反方向合在一起，它们互相顶住，绳子就稳住了', 'serif', 36, INK)
    stage = min(2, int(t / 7.3))
    for row in range(2):
        cy = 380 + row * 300
        if row == 0:
            c.text(120, cy - 120, '一股：松手就回转', 'bold', 24, INK, 'lm')
            spin = math.sin(t * 2) * 0.5 if stage >= 1 else 0
            pts = [(300 + j * 6, cy + 30 * math.sin(j * 0.3 + t * (4 if stage >= 1 else 0))) for j in range(200)]
            c.line(pts, FIBER, 6)
            if stage >= 1:
                c.arc(1560, cy, 60, 60, 0, 300, SPARK, 4)
                c.text(1560, cy + 100, '自己往回转', 'sans', 20, SPARK, 'mm')
        else:
            c.text(120, cy - 120, '两股反着合：互相顶住', 'bold', 24, INK, 'lm')
            for k in range(2):
                ph = k * math.pi
                pts = [(300 + j * 6, cy + 34 * math.sin(j * 0.12 + ph)) for j in range(200)]
                c.line(pts, FIBER if k == 0 else FIBER2, 10)
                for j in range(0, 200, 6):
                    x = 300 + j * 6
                    y = cy + 34 * math.sin(j * 0.12 + ph)
                    c.line([(x - 6, y - 6), (x + 6, y + 6)], mix(FIBER, BG, 0.3), 2)
            if stage >= 2:
                c.text(1560, cy, '不再回转', 'bold', 24, GREEN, 'mm')
    caps(c, t, [(0, 7.2, '先把纤维朝一个方向拧成一股：它被拧紧了，就像拧过的橡皮筋，攒着往回转的劲'),
                (7.4, 14.5, '一松手，这一股自己就往回转，还会缠成一团'),
                (14.7, 22, '把两股朝反方向合在一起：每一股想往回转，正好把另一股拧得更紧，两股互相顶住，绳子就稳住了')], y=1010)


# ---------------------------------------------------------------- B102 蓑衣
def _shingles(c, t, reverse):
    x0, y0, x1, y1 = 300, 300, 1300, 800
    dx, dy = (x1 - x0), (y1 - y0)
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = uy, -ux                      # 朝外（上方）的法线
    c.line([(x0, y0), (x1, y1)], mix(BG, (230, 230, 240), 0.5), 8)
    n = 7
    step = L / n
    lift = 34
    order = range(n - 1, -1, -1) if not reverse else range(n)
    for k in order:
        s0 = k * step
        s1 = s0 + step * 1.35
        o0, o1 = (8, lift) if not reverse else (lift, 8)
        pa = (x0 + ux * s0 + nx * o0, y0 + uy * s0 + ny * o0)
        pb = (x0 + ux * s1 + nx * o1, y0 + uy * s1 + ny * o1)
        c.line([pa, pb], STRAW, 14)
    return x0, y0, ux, uy, nx, ny, L, n, step, lift


def _drop(x0, y0, ux, uy, nx, ny, d, off):
    return x0 + ux * d + nx * off, y0 + uy * d + ny * off


def b102_overlap(c, t, i):
    corner_tag(c, 'B102 · 上压下，水只能往下流')
    c.text(60, 96, '蓑衣的草叶从下往上一层压一层：雨水落在上层，顺着叶面流到下层的叶面上，一路滑到底', 'serif', 36, INK)
    x0, y0, ux, uy, nx, ny, L, n, step, lift = _shingles(c, t, False)
    c.text(1340, 840, '下摆', 'sans', 22, MUTED, 'lm')
    c.text(260, 260, '领口', 'sans', 22, MUTED, 'rm')
    c.text(760, 640, '里面（身体）', 'sans', 20, MUTED, 'mm')
    rnd = random.Random(2)
    for k in range(14):
        s = ((t * 0.18 + k / 14) % 1)
        d = s * L
        local = (d % step) / step
        x, y = _drop(x0, y0, ux, uy, nx, ny, d, 8 + (lift - 8) * local + 16)
        c.ellipse(x, y, 7, 9, fill=WATER_L)
    for k in range(10):
        ph = (t * 0.9 + k * 0.37) % 1
        x = 360 + k * 90
        y = 180 + ph * 160
        c.line([(x, y), (x - 6, y + 20)], mix(BG, WATER_L, 0.8), 2)
    c.rect(1460, 300, 1860, 560, fill=SHEET, r=14)
    c.text(1660, 340, '里面那层纸巾', 'bold', 24, INK, 'mm')
    c.text(1660, 420, '几乎是干的', 'bold', 30, GREEN, 'mm')
    c.text(1660, 490, '（实验结果以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '蓑衣是用棕叶或蓑草一层层编起来的，最关键的不是草多，而是怎么搭'),
                (7.2, 14, '下面一层先编，上面一层压在它外面：雨水落在叶面上，只会往低处流'),
                (14.2, 22, '流到叶尖，正好落到下一层的外面，一层传一层滑到下摆：水始终走在外面（示意）')], y=1010)


def b102_reverse(c, t, i):
    corner_tag(c, 'B102 · 搭反了，水就往里灌')
    c.text(60, 96, '把同样的草叶反过来搭（下层压住上层）：水流到每一层的边上，正好钻进缝里，流到里面', 'serif', 36, INK)
    x0, y0, ux, uy, nx, ny, L, n, step, lift = _shingles(c, t, True)
    c.text(1340, 840, '下摆', 'sans', 22, MUTED, 'lm')
    c.text(260, 260, '领口', 'sans', 22, MUTED, 'rm')
    for k in range(14):
        s = ((t * 0.18 + k / 14) % 1)
        d = s * L
        local = (d % step) / step
        inside = local > 0.8 or local < 0.12
        off = (lift - (lift - 8) * local + 16) if not inside else -2 + 0 * local
        if inside:
            off = 2
        x, y = _drop(x0, y0, ux, uy, nx, ny, d, off)
        c.ellipse(x, y, 7, 9, fill=WATER_L if not inside else NRED)
    wet = min(1, t / 18)
    c.line([(x0, y0), (x0 + ux * L * wet, y0 + uy * L * wet)], mix(BG, WATER, 0.8), 8)
    c.rect(1460, 300, 1860, 560, fill=SHEET, r=14)
    c.text(1660, 340, '里面那层纸巾', 'bold', 24, INK, 'mm')
    c.text(1660, 420, '一道道湿了', 'bold', 30, NRED, 'mm')
    c.text(1660, 490, '（实验结果以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '草还是那些草，只是反过来搭：每一层的下边缘被压在了下一层底下'),
                (7.2, 14, '水顺着叶面流到这道边上，前面没有路了，就沿着缝往里钻'),
                (14.2, 22, '一层漏一点，到下摆时里面已经湿了一大片：屋瓦、鱼鳞、鸟的羽毛，也都是上压下（示意）')], y=1010)


CLIPS = {
 'B100_缓冲': (b100_buffer, 22), 'B100_节奏': (b100_rhythm, 22),
 'B100_片头': (titles.opening(BSER, VOL26, SB26, 0, '汉代画像石里的挑担人'), 7),
 'B100_片尾': (titles.closing(BSER, VOL26, SB26, 0, '下集：一根根细纤维，搓成绳子后为什么能吊起重东西？'), 7),
 'B101_捻紧': (b101_twist, 22), 'B101_合股': (b101_ply, 22),
 'B101_片头': (titles.opening(BSER, VOL26, SB26, 1, '新石器时代陶器上的绳纹'), 7),
 'B101_片尾': (titles.closing(BSER, VOL26, SB26, 1, '下集：一件草编的蓑衣，为什么下大雨身上也不湿？'), 7),
 'B102_搭接': (b102_overlap, 22), 'B102_反搭': (b102_reverse, 22),
 'B102_片头': (titles.opening(BSER, VOL26, SB26, 2, '《诗经 · 小雅》「何蓑何笠」'), 7),
 'B102_片尾': (titles.closing(BSER, VOL26, SB26, 2, '下集：汴河上那座没有桥墩的木拱桥，是怎么搭起来的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
