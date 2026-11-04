"""第十五季（第四层：看得见、听得见、飞得起、算得出）第一批：E82 电视、E83 磁带录音、E84 回声测距与雷达 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S15A = [('82', '电视'), ('83', '磁带'), ('84', '雷达'), ('85', '矿石收音机'), ('86', '机翼'),
        ('87', '电梯'), ('88', '火箭'), ('89', '光纤'), ('90', '卫星定位'), ('91', '计算机')]
SER15, VOL15 = '从零造物', '第十五季 · 第四层：看得见、听得见、飞得起、算得出'
COIL = (200, 130, 70)
TAPE = (110, 80, 60)
WAVE = (120, 170, 220)

FACE = ["................",
        ".....######.....",
        "...##......##...",
        "..#..........#..",
        ".#............#.",
        ".#...##..##...#.",
        "#....##..##....#",
        "#..............#",
        "#..............#",
        "#..#........#..#",
        ".#..#......#..#.",
        ".#...######...#.",
        "..#..........#..",
        "...##......##...",
        ".....######.....",
        "................"]

def grid(c, x0, y0, cell, n, upto, src, a=1.0):
    for k in range(n * n):
        r, q = divmod(k, n)
        x, y = x0 + q * cell, y0 + r * cell
        on = src[r * len(src) // n][q * len(src[0]) // n] == '#'
        if k < upto:
            c.rect(x, y, x + cell - 1, y + cell - 1, fill=mix(BG, INK if on else SHEET, a))
        else:
            c.rect(x, y, x + cell - 1, y + cell - 1, outline=mix(BG, LINE, a * 0.6), width=1)

# ---------------------------------------------------------------- E82 电视
def e82_scan(c, t, i):
    corner_tag(c, '第 82 集 · 拆成点，一行行送')
    c.text(60, 96, '一根线一次只能送一个数：把画面拆开，排成一队', 'serif', 40, INK)
    n, cell = 16, 26
    total = n * n
    k = int(total * fade(t, 2, 16))
    c.text(300, 210, '发送端', 'bold', 28, INK, 'mm')
    grid(c, 92, 240, cell, n, total, FACE)
    if k < total:
        r, q = divmod(k, n)
        c.rect(92 + q * cell - 3, 240 + r * cell - 3, 92 + (q + 1) * cell + 2, 240 + (r + 1) * cell + 2, outline=SPARK, width=3)
    c.text(1620, 210, '接收端', 'bold', 28, INK, 'mm')
    grid(c, 1412, 240, cell, n, k, FACE)
    # signal strip
    c.line([(560, 450), (1360, 450)], MUTED, 2)
    for j in range(24):
        idx = k - 24 + j
        if idx < 0: continue
        r, q = divmod(idx, n)
        on = FACE[r][q] == '#'
        x = 560 + j * 33
        c.rect(x, 450 - (50 if on else 8), x + 26, 450, fill=SPARK if on else MUTED, r=3)
    c.text(960, 520, '线上走的：一串「黑、白、白、黑……」', 'sans', 24, MUTED, 'mm')
    c.text(960, 380, f'已送 {k} / {total} 个点', 'mono', 26, INK, 'mm')
    caps(c, t, [(0, 6, '一幅画是二维的，可一根导线、一路电波，一次只能送一个数'),
                (6.2, 13, '办法是：从左上角开始，一行一行地把每个点的明暗依次送出去'),
                (13.2, 22, '接收端按同样的顺序一行行拼回来：这就是扫描。电视每秒要这样扫几十幅画面')], y=1010)

def e82_res(c, t, i):
    corner_tag(c, '第 82 集 · 格子越多越清楚')
    c.text(60, 96, '清楚是有代价的：点越多，要送的数据越多', 'serif', 40, INK)
    for k, (n, cell) in enumerate([(8, 40), (16, 20), (32, 10)]):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        x0 = 200 + k * 560
        grid(c, x0, 220, cell, n, n * n, FACE, a)
        c.text(x0 + 160, 580, f'{n} × {n} = {n * n} 个点', 'bold', 28, mix(BG, INK, a), 'mm')
        h = 200 * (n * n) / 1024
        c.rect(x0 + 110, 860 - h, x0 + 210, 860, fill=mix(BG, SPARK, a), r=6)
    c.line([(150, 860), (1800, 860)], LINE, 2)
    c.text(150, 900, '要送的数据量', 'sans', 22, MUTED, 'lm')
    d = fade(t, 14, 15)
    c.text(1150, 680, '1925 年贝尔德的', 'sans', 24, mix(BG, INK, d), 'mm')
    c.text(1150, 720, '第一台电视只有 30 行', 'bold', 26, mix(BG, INK, d), 'mm')
    c.text(1150, 760, '（拍摄前核对）', 'sans', 22, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '8 乘 8：只看得出是个圆脸'),
                (6.2, 13, '16 乘 16：眼睛嘴巴都出来了；32 乘 32 更细，可点数翻了四倍'),
                (13.2, 22, '格子每多一倍，要送的点就多四倍：清晰度、速度和线路能传多少，要一起权衡')], y=1010)

# ---------------------------------------------------------------- E83 磁带录音
def domains(c, x0, y, n, w, dirs, a=1.0):
    for k in range(n):
        x = x0 + k * w
        d = dirs[k]
        c.rect(x + 2, y - 26, x + w - 2, y + 26, fill=mix(BG, TAPE, a), r=4)
        if d:
            col = NRED if d > 0 else WAVE
            c.arrow(x + w / 2 - 18 * d, y, x + w / 2 + 18 * d, y, mix(BG, col, a), 4, 12)

def e83_write(c, t, i):
    corner_tag(c, '第 83 集 · 把声音写成磁铁的方向')
    c.text(60, 96, '磁头里的电流一正一负，带子上的小磁铁就一左一右', 'serif', 40, INK)
    n, w = 24, 60
    x0 = 240
    pos = fade(t, 2, 16) * n
    sig = [math.sin(k * 0.7) for k in range(n)]
    dirs = [(1 if sig[k] > 0 else -1) if k < pos else 0 for k in range(n)]
    domains(c, x0, 600, n, w, dirs)
    hx = x0 + min(pos, n - 0.01) * w
    c.rect(hx - 40, 450, hx + 40, 570, fill=MUTED, r=8)
    c.text(hx, 430, '磁头', 'bold', 24, INK, 'mm')
    for j in range(4):
        c.line([(hx - 30, 480 + j * 20), (hx + 30, 480 + j * 20)], COIL, 4)
    # waveform
    pts = [(x0 + (k / 4) * w, 300 - 80 * math.sin(k / 4 * 0.7)) for k in range(n * 4)]
    c.line(pts, WAVE, 4)
    c.text(x0, 200, '声音变成的电流', 'sans', 24, WAVE, 'lm')
    c.text(x0, 680, '带子向左走，磁粉被磁化成一排排小磁铁', 'sans', 24, MUTED, 'lm')
    a = fade(t, 15, 16)
    c.rect(240, 760, 1680, 880, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 800, '放音时反过来：带子上的小磁铁经过磁头，在线圈里感应出电流（磁生电）', 'sans', 26, mix(BG, INK, a), 'mm')
    c.text(960, 845, '接第 04 集磁生电、第 56 集电磁铁、第 73 集留声机', 'sans', 22, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '录音时，声音先变成电流，送进磁头里的线圈'),
                (6.2, 14, '电流方向一变，磁头的磁场就跟着变，把带子上的磁粉磁化成不同方向'),
                (14.2, 22, '放音时，带子再从磁头下面经过：磁生电，电流又变回声音')], y=1010)

def e83_erase(c, t, i):
    corner_tag(c, '第 83 集 · 一块强磁铁，全部抹平')
    c.text(60, 96, '留声机的沟纹会磨坏，磁带的「字」会被磁铁抹掉', 'serif', 40, INK)
    n, w = 24, 60
    x0 = 240
    mpos = fade(t, 4, 14) * (n + 2) - 1
    dirs = [(1 if math.sin(k * 0.7) > 0 else -1) if k > mpos else 1 for k in range(n)]
    domains(c, x0, 520, n, w, dirs)
    mx = x0 + mpos * w
    if -1 < mpos < n + 1:
        c.rect(mx - 50, 380, mx + 50, 470, fill=NRED, r=8)
        c.text(mx, 425, 'N S', 'bold', 26, BG, 'mm')
    c.text(x0, 640, '被抹过的地方全朝一个方向：声音没了', 'sans', 24, MUTED, 'lm')
    a = fade(t, 15, 16)
    c.rect(240, 740, 1680, 880, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 785, '所以磁带、银行卡的磁条、老硬盘都怕强磁铁', 'bold', 28, mix(BG, INK, a), 'mm')
    c.text(960, 835, '1898 年波尔森用钢丝录音，1928 年出现涂磁粉的纸带（拍摄前核对）', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '录好的带子上，小磁铁一左一右，排成声音的样子'),
                (6.2, 14, '拿一块强磁铁从上面扫过，所有小磁铁都被拧成同一个方向'),
                (14.2, 22, '记录就被抹平了。好处是：抹掉以后，这段带子还能重新录')], y=1010)

# ---------------------------------------------------------------- E84 回声测距与雷达
def e84_echo(c, t, i):
    corner_tag(c, '第 84 集 · 一来一回')
    c.text(60, 96, '拍一下手：声音跑到墙，再跑回来', 'serif', 40, INK)
    px, wx, y = 260, 1500, 420
    c.ellipse(px, y - 60, 30, 30, fill=INK)
    c.rect(px - 20, y - 30, px + 20, y + 80, fill=INK, r=8)
    c.rect(wx, 220, wx + 60, 620, fill=MUTED)
    c.text(wx + 30, 650, '墙', 'bold', 26, INK, 'mm')
    T0 = 2.0
    trip = 6.0
    u = (t - T0) / trip
    if 0 <= u <= 1:
        x = px + 60 + (wx - px - 60) * (1 - abs(1 - 2 * u))
        for r in range(3):
            c.arc(x, y, 30 + r * 16, 60 + r * 20, -60 if u < 0.5 else 120, 60 if u < 0.5 else 240, WAVE, 4)
    c.line([(px + 60, 560), (wx - 10, 560)], LINE, 2)
    c.text((px + wx) / 2, 590, '距离 d', 'sans', 24, MUTED, 'mm')
    # waveform
    a = fade(t, 9, 10)
    x0, y0 = 300, 820
    pts = []
    for k in range(300):
        tt = k / 300
        v = 0.9 * math.exp(-((tt - 0.15) / 0.01) ** 2) + 0.45 * math.exp(-((tt - 0.65) / 0.012) ** 2)
        pts.append((x0 + k * 4, y0 - 120 * v * math.sin(k * 2.5)))
    c.line(pts, mix(BG, WAVE, a), 2)
    c.line([(x0 + 0.15 * 1200, y0 + 60), (x0 + 0.65 * 1200, y0 + 60)], mix(BG, SPARK, a), 3)
    c.text(x0 + 0.4 * 1200, y0 + 90, '间隔 t', 'bold', 26, mix(BG, SPARK, a), 'mm')
    d = fade(t, 13, 14)
    c.rect(1560, 720, 1880, 900, fill=mix(BG, SHEET, d), r=12)
    c.text(1720, 770, 'd = 340 × t ÷ 2', 'mono', 28, mix(BG, INK, d), 'mm')
    c.text(1720, 820, '声速约 340 米/秒', 'sans', 22, mix(BG, MUTED, d), 'mm')
    c.text(1720, 860, '除以 2：一来一回', 'sans', 22, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 8, '对着远处的墙用力拍一下木板：声音跑过去，撞墙，再跑回来'),
                (8.2, 14, '手机录音里会有两个峰：第一个是拍板，第二个是回声'),
                (14.2, 22, '量出两个峰的间隔，乘声速再除以二：就是墙有多远。蝙蝠和海豚一直这么干')], y=1010)

def e84_radar(c, t, i):
    corner_tag(c, '第 84 集 · 换成电磁波，就是雷达')
    c.text(60, 96, '电磁波比声音快近一百万倍：回声只要几微秒', 'serif', 40, INK)
    cx, cy = 300, 760
    c.poly([(cx - 80, cy), (cx + 80, cy), (cx, cy - 60)], MUTED)
    c.arc(cx, cy - 80, 90, 40, 180, 360, INK, 6)
    px, py = 1450, 330
    c.poly([(px - 90, py), (px + 60, py - 10), (px + 90, py), (px + 60, py + 10)], INK)
    c.poly([(px - 10, py), (px + 20, py - 60), (px + 35, py - 60), (px + 25, py)], INK)
    ph = (t * 0.35) % 1
    for k in range(3):
        u = (ph + k / 3) % 1
        x = cx + (px - cx) * u
        y = cy - 80 + (py - cy + 80) * u
        c.ellipse(x, y, 16, 16, fill=mix(BG, SPARK, 1 - u * 0.5))
    a = fade(t, 6, 7)
    rows = [('声音（空气）', '约 340 米/秒', '1 千米：来回约 6 秒'), ('电磁波（雷达）', '约 30 万千米/秒', '1 千米：来回约 7 微秒')]
    for k, (nm, v, r_) in enumerate(rows):
        y = 620 + k * 90
        c.rect(820, y - 34, 1880, y + 34, fill=mix(BG, SHEET, a), r=10)
        c.text(850, y, nm, 'bold', 26, mix(BG, INK, a), 'lm')
        c.text(1140, y, v, 'mono', 24, mix(BG, INK, a), 'lm')
        c.text(1480, y, r_, 'sans', 24, mix(BG, MUTED, a), 'lm')
    d = fade(t, 13, 14)
    c.text(1350, 850, '1935 年沃森-瓦特用无线电回波探到飞机（拍摄前核对）', 'sans', 24, mix(BG, INK, d), 'mm')
    c.text(1350, 900, '要量这么短的时间，靠的是电子计时：接第 45 集摆钟的「数时间」', 'sans', 22, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '把声音换成无线电波：雷达发出一个短脉冲，等它从飞机上反射回来'),
                (6.2, 13, '道理和拍手一样：距离等于速度乘时间除以二。只是电磁波太快了'),
                (13.2, 22, '一千米外的飞机，回声只要几微秒：雷达比的就是谁能把时间量得更准')], y=1010)

CLIPS = {
 'E82_扫描': (e82_scan, 22), 'E82_分辨率': (e82_res, 22),
 'E82_片头': (titles.opening(SER15, VOL15, S15A, 0, '1884 年 · 尼普科夫扫描盘'), 7),
 'E82_片尾': (titles.closing(SER15, VOL15, S15A, 0, '下集：声音怎么被「存」进一条带子里？'), 7),
 'E83_写入': (e83_write, 22), 'E83_擦除': (e83_erase, 22),
 'E83_片头': (titles.opening(SER15, VOL15, S15A, 1, '1898 年 · 波尔森钢丝录音机'), 7),
 'E83_片尾': (titles.closing(SER15, VOL15, S15A, 1, '下集：发出去一声，怎么知道东西有多远？'), 7),
 'E84_回声': (e84_echo, 22), 'E84_雷达': (e84_radar, 22),
 'E84_片头': (titles.opening(SER15, VOL15, S15A, 2, '1935 年 · 沃森-瓦特'), 7),
 'E84_片尾': (titles.closing(SER15, VOL15, S15A, 2, '下集：一台不用电池的收音机，声音从哪来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
