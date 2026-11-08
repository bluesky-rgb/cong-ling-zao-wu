"""第三十季（古法解密 12.0：玩、响、用）第一批：B120 滚铁环、B121 翻花绳、B122 华容道 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO

SB30 = [('B120', '滚铁环'), ('B121', '翻花绳'), ('B122', '华容道'), ('B123', '拨浪鼓'), ('B124', '笛子'),
        ('B125', '风铃'), ('B126', '折扇'), ('B127', '谢公屐'), ('B128', '簧片锁'), ('B129', '印章')]
VOL30 = '第三十季 · 古法解密 12.0'
HOOP = (170, 170, 180)
YARN = (230, 110, 110)
TILE = (220, 190, 130)


# ---------------------------------------------------------------- B120 滚铁环
def b120_speed(c, t, i):
    corner_tag(c, 'B120 · 滚得越快，越久不倒')
    c.text(60, 96, '同一个铁环，轻推、中推、用力推出去：慢的晃两下就倒，快的能一直滚到走廊尽头', 'serif', 38, INK)
    lanes = [('轻推', 0.6, 0.18), ('中推', 1.4, 0.5), ('用力推', 2.6, 0.95)]
    x0, x1 = 200, 1500
    for k, (lab, v, frac) in enumerate(lanes):
        y = 330 + k * 200
        c.line([(x0, y + 60), (x1 + 120, y + 60)], LINE, 2)
        c.text(110, y, lab, 'bold', 26, INK, 'mm')
        xend = x0 + (x1 - x0) * frac
        x = min(xend, x0 + v * 45 * t)
        r = 55
        if x < xend - 1:
            ang = (x - x0) / r
            c.ellipse(x, y, r, r, outline=HOOP, width=6)
            c.ellipse(x + (r - 6) * math.cos(ang), y + (r - 6) * math.sin(ang), 7, 7, fill=SPARK)
        else:
            tf = (t - (xend - x0) / (v * 45))
            f = min(1, tf / 0.8)
            ry = r * max(0.1, 1 - f)
            c.ellipse(xend, y + 60 - ry, r, ry, outline=HOOP, width=6)
            c.text(xend, y - 90, '倒了', 'sans', 20, NRED, 'mm')
        c.text(1700, y, f'约 {frac * 16:.0f} 米', 'mono', 24, SPARK, 'mm')
    c.text(1700, 270, '倒下前滚出（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同一个绣花绷子，在走廊里分别轻推、中推、用力推出去'),
                (7.2, 14, '推得轻的晃了几下就躺下了；推得重的转得飞快，稳稳地往前滚'),
                (14.2, 22, '转得越快的圆环越「倔」，越不容易倒：滚铁环的钩子只是轻轻推一推、拨一拨方向（距离为示意，以实测为准）')], y=1010)


def b120_turn(c, t, i):
    corner_tag(c, 'B120 · 一歪，它就往歪的那边拐')
    c.text(60, 96, '从上往下看：铁环直着滚就走直线；往左歪一点，它不会马上倒，而是往左拐弯，转着转着又把自己立了起来', 'serif', 36, INK)
    for k, (lab, lean) in enumerate((('立直了滚', 0.0), ('往左歪一点', 1.0))):
        cx = 520 + k * 880
        c.text(cx, 230, lab, 'bold', 28, INK, 'mm')
        c.rect(cx - 360, 270, cx + 360, 900, outline=mix(BG, LINE, 0.5), width=2, r=12)
        s = min(1, t / 16)
        pts = []
        R = 520
        for j in range(41):
            u = s * j / 40
            if lean == 0:
                pts.append((cx, 860 - 560 * u))
            else:
                a = 560 * u / R
                pts.append((cx + R * (math.cos(a) - 1) * 0.9, 860 - R * math.sin(a)))
        if len(pts) > 1:
            c.line(pts, mix(BG, SPARK, 0.6), 3)
        hx, hy = pts[-1]
        if len(pts) > 1:
            dx, dy = pts[-1][0] - pts[-2][0], pts[-1][1] - pts[-2][1]
        else:
            dx, dy = 0, -1
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        w = 10 + 18 * lean * (1 - 0.6 * s)
        c.poly([(hx + ux * 50 - uy * w, hy + uy * 50 + ux * w), (hx + ux * 50 + uy * 3, hy + uy * 50 - ux * 3),
                (hx - ux * 50 + uy * 3, hy - uy * 50 - ux * 3), (hx - ux * 50 - uy * w, hy - uy * 50 + ux * w)], HOOP)
        if lean:
            c.text(cx - 200, 600, '往左歪 → 往左拐', 'sans', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '从上往下看：一个立直了的铁环，向前滚就是一条直线'),
                (7.2, 14, '要是它往左歪一点，转动的圆环不会马上倒下，而是往左拐弯'),
                (14.2, 22, '一拐弯，它又被「甩」得立了起来：所以滚铁环拨一拨钩子就能转弯，陀螺歪着也能转好久（示意）')], y=1010)


# ---------------------------------------------------------------- B121 翻花绳
LF = [(560, 360 + k * 95) for k in range(5)]
RF = [(1360, 360 + k * 95) for k in range(5)]
FIGS = [
    ('一个圈', [LF[0], RF[0], RF[4], LF[4]]),
    ('面条', [LF[0], RF[1], LF[2], RF[3], LF[4], RF[4], LF[3], RF[2], LF[1], RF[0]]),
    ('降落伞', [LF[0], RF[0], LF[2], RF[4], LF[4], RF[2], LF[1], RF[1], LF[3], RF[3]]),
    ('牛槽', [LF[0], RF[2], LF[4], RF[4], LF[1], RF[3], LF[3], RF[1], LF[2], RF[0]]),
]


def _crossings(pts):
    n = len(pts)
    segs = [(pts[k], pts[(k + 1) % n]) for k in range(n)]
    cnt = 0
    for a in range(n):
        for b in range(a + 1, n):
            if b == a + 1 or (a == 0 and b == n - 1):
                continue
            (p1, p2), (p3, p4) = segs[a], segs[b]
            d = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
            if abs(d) < 1e-9:
                continue
            u = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / d
            v = ((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) / d
            if 0.001 < u < 0.999 and 0.001 < v < 0.999:
                cnt += 1
    return cnt


def _hands(c):
    for (x, y) in LF + RF:
        c.ellipse(x, y, 16, 16, fill=mix(BG, (225, 180, 150), 0.8))
    c.text(480, 900, '左手五指', 'sans', 20, MUTED, 'mm')
    c.text(1440, 900, '右手五指', 'sans', 20, MUTED, 'mm')


def b121_figures(c, t, i):
    corner_tag(c, 'B121 · 翻一次，交叉点变一次')
    c.text(60, 96, '同一根绳圈挂在十个手指上，钩一钩、挑一挑，交叉点的数目和位置都变了，就成了不同的花样（示意）', 'serif', 36, INK)
    k = min(len(FIGS) - 1, int(t / 5.2))
    name, pts = FIGS[k]
    a = fade(t, k * 5.2, k * 5.2 + 1)
    _hands(c)
    c.line(pts + [pts[0]], mix(BG, YARN, a), 5)
    c.rect(1560, 360, 1860, 620, fill=SHEET, r=14)
    c.text(1710, 410, name, 'bold', 32, INK, 'mm')
    c.text(1710, 500, f'交叉点 {_crossings(pts)} 个', 'mono', 26, SPARK, 'mm')
    c.text(1710, 570, '（示意图）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '一根毛线系成圈，两只手的手指撑开，就是最简单的「一个圈」'),
                (7.2, 14, '另一个人用手指钩住几根线翻过来：线走的路变了，交叉点也变多了'),
                (14.2, 22, '花样越复杂，交叉越多：可绳子本身从头到尾没剪、没解开、没打新结')], y=1010)


def b121_release(c, t, i):
    corner_tag(c, 'B121 · 松开手，一拉就变回一个圈')
    c.text(60, 96, '不管翻出多复杂的花样，只要松开手指一拉，所有交叉都会散开：绳圈从头到尾都没有打结', 'serif', 38, INK)
    pts0 = FIGS[3][1]
    n = len(pts0)
    dense = []
    for k in range(n):
        p, q = pts0[k], pts0[(k + 1) % n]
        for j in range(8):
            u = j / 8
            dense.append((p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u))
    m = len(dense)
    cx, cy = 960, 550
    circ = [(cx + 300 * math.cos(2 * math.pi * k / m - math.pi / 2), cy + 300 * math.sin(2 * math.pi * k / m - math.pi / 2)) for k in range(m)]
    s = min(1, max(0, (t - 4) / 12))
    s = s * s * (3 - 2 * s)
    pts = [(a[0] + (b[0] - a[0]) * s, a[1] + (b[1] - a[1]) * s) for a, b in zip(dense, circ)]
    if s < 0.05:
        _hands(c)
    c.line(pts + [pts[0]], YARN, 5)
    cr = _crossings(pts)
    c.rect(1560, 360, 1860, 560, fill=SHEET, r=14)
    c.text(1710, 410, '看得见的交叉', 'bold', 26, INK, 'mm')
    c.text(1710, 490, f'{cr} 个', 'mono', 36, SPARK if cr else GREEN, 'mm')
    caps(c, t, [(0, 7, '翻到「牛槽」这样复杂的花样，绳子交叉了好多处'),
                (7.2, 14, '两个人一起松开手指，把绳圈往外拉：交叉一个接一个地散开'),
                (14.2, 22, '最后又是一个干干净净的圈：数学上说，它从头到尾都是「没打结的圈」，只是被摆成了不同的样子（示意）')], y=1010)


# ---------------------------------------------------------------- B122 华容道
def _moves(seed, n):
    rnd = random.Random(seed)
    blank = 8
    seq = []
    prev = -1
    for _ in range(n):
        r, c_ = divmod(blank, 3)
        nb = [blank + d for d, ok in ((-3, r > 0), (3, r < 2), (-1, c_ > 0), (1, c_ < 2)) if ok and blank + d != prev]
        nxt = rnd.choice(nb)
        seq.append(nxt)
        prev, blank = blank, nxt
    return seq


def _board(start, seq, steps, frac):
    board = list(start)
    for k in range(steps):
        b = board.index(0)
        board[b], board[seq[k]] = board[seq[k]], 0
    return board


def _inv(board):
    a = [x for x in board if x]
    return sum(1 for p in range(len(a)) for q in range(p + 1, len(a)) if a[p] > a[q])


def _draw_board(c, x0, y0, board, moving=None, frac=0.0, cs=130):
    c.rect(x0 - 12, y0 - 12, x0 + 3 * cs + 8, y0 + 3 * cs + 8, fill=mix(BG, WOOD, 0.4), r=12)
    for p, v in enumerate(board):
        if not v:
            continue
        r, col = divmod(p, 3)
        x, y = x0 + col * cs, y0 + r * cs
        if moving is not None and p == moving[0]:
            r2, c2 = divmod(moving[1], 3)
            x = x + (x0 + c2 * cs - x) * frac
            y = y + (y0 + r2 * cs - y) * frac
        c.rect(x, y, x + cs - 8, y + cs - 8, fill=TILE, r=10)
        c.text(x + cs / 2 - 4, y + cs / 2 - 4, str(v), 'bold', 44, INK, 'mm')


def b122_slide(c, t, i):
    corner_tag(c, 'B122 · 只能把方块推进空格')
    c.text(60, 96, '八块方块、一个空格：每一步只能把挨着空格的一块推进去。先随便推乱 20 步，再原路推回去', 'serif', 38, INK)
    start = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    seq = _moves(4, 20)
    T = 0.45
    total = len(seq)
    st = t / T
    if st < total:
        k = int(st)
        frac = st - k
        board = _board(start, seq, k, 0)
        b = board.index(0)
        _draw_board(c, 760, 300, board, (seq[k], b), frac)
        lab = f'打乱：第 {k + 1} 步'
    else:
        st2 = (t - total * T - 1) / T
        if st2 < 0:
            board = _board(start, seq, total, 0)
            _draw_board(c, 760, 300, board)
            lab = '乱了'
        elif st2 < total:
            k = int(st2)
            frac = st2 - k
            board = _board(start, seq, total - k, 0)
            prevb = ([start.index(0)] + seq)[total - k - 1]
            _draw_board(c, 760, 300, board, (prevb, board.index(0)), frac)
            lab = f'推回：第 {k + 1} 步'
        else:
            _draw_board(c, 760, 300, start)
            lab = '回到原样'
    c.text(960, 760, lab, 'mono', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '3×3 的格子里放 8 块写着数字的方块，留一个空格'),
                (7.2, 14, '每一步只能把挨着空格的一块推进空格：先随便推 20 步，顺序全乱了'),
                (14.2, 22, '再一步一步原路推回去，又回到了 1 到 8：正常推乱的，总能推回来')], y=1010)


def b122_parity(c, t, i):
    corner_tag(c, 'B122 · 对调两块，就永远回不去')
    c.text(60, 96, '把「逆序」数一数：每推一步，逆序数只会变 0 或 2，奇偶永远不变。对调 1 和 2 让它变成了奇数，就再也回不到 0', 'serif', 34, INK)
    starts = [[1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 5, 6, 7, 8, 0]]
    labs = ['正常的一盘', '对调了 1 和 2']
    seq = _moves(9, 40)
    k = int(min(40, t * 2))
    for j in range(2):
        board = _board(starts[j], seq, k, 0)
        x0 = 330 + j * 860
        _draw_board(c, x0, 300, board, cs=110)
        inv = _inv(board)
        c.text(x0 + 160, 250, labs[j], 'bold', 28, INK, 'mm')
        c.text(x0 + 160, 680, f'逆序数 {inv}', 'mono', 28, INK, 'mm')
        c.text(x0 + 160, 730, '偶数' if inv % 2 == 0 else '奇数', 'bold', 32, GREEN if inv % 2 == 0 else NRED, 'mm')
    c.text(960, 820, f'两盘都推了 {k} 步', 'mono', 24, MUTED, 'mm')
    c.text(960, 870, '逆序：一个大数排在一个小数前面，算一对（空格不算）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '从左到右、从上到下读这些数，数一数有几对「大的排在小的前面」，叫逆序数'),
                (7.2, 14, '在 3×3 的格子里，每推一步，逆序数只会变 0 或者变 2：奇偶从来不变'),
                (14.2, 22, '原样是 0，偶数；对调两块变成了 1，奇数：不管再推多少步，都回不到 0（3×3 格子时成立）')], y=1010)


CLIPS = {
 'B120_速度': (b120_speed, 22), 'B120_拐弯': (b120_turn, 22),
 'B120_片头': (titles.opening(BSER, VOL30, SB30, 0, '明清以来民间流行的滚环游戏'), 7),
 'B120_片尾': (titles.closing(BSER, VOL30, SB30, 0, '下集：一根绳圈翻来翻去，为什么拉开永远不打结？'), 7),
 'B121_花样': (b121_figures, 22), 'B121_拉开': (b121_release, 22),
 'B121_片头': (titles.opening(BSER, VOL30, SB30, 1, '民间流传已久的翻绳游戏'), 7),
 'B121_片尾': (titles.closing(BSER, VOL30, SB30, 1, '下集：滑块谜题为什么有的怎么推都推不回去？'), 7),
 'B122_推块': (b122_slide, 22), 'B122_奇偶': (b122_parity, 22),
 'B122_片头': (titles.opening(BSER, VOL30, SB30, 2, '民间流行的滑块谜题'), 7),
 'B122_片尾': (titles.closing(BSER, VOL30, SB30, 2, '下集：手一搓，两边的小珠子为什么就打在鼓面上？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
