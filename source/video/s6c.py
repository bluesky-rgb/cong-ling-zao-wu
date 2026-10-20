"""第六季第三批：E48 数字与 0、E49 复式记账、E50 光学电报 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import S6A, SER6, VOL6, GREEN, seg

ROD = (220, 200, 150)

# ---------------------------------------------------------------- E48 数字与 0
def e48_place(c, t, i):
    corner_tag(c, '第 48 集 · 位值制')
    c.text(60, 96, '同一个「3」，放在不同的位置', 'serif', 40, INK)
    cols = ['千', '百', '十', '个']
    x0, w = 560, 200
    for k, n in enumerate(cols):
        x = x0 + k * w
        c.rect(x, 220, x + w - 20, 560, outline=LINE, width=3, r=10)
        c.text(x + (w - 20) / 2, 260, n, 'serif', 34, MUTED, 'mm')
    # stage 1: 3 moves from 个 to 百
    pos = 3 if t < 3 else (2 if t < 5 else 1)
    if t < 8:
        x = x0 + pos * w + (w - 20) / 2
        c.text(x, 420, '3', 'mono', 120, COPPER, 'mm')
        val = {3: '3', 2: '30', 1: '300'}[pos]
        c.text(960, 650, f'= {val}', 'mono', 60, INK, 'mm')
    else:
        # 305 vs 35
        a = fade(t, 8, 9)
        digs = ['', '3', '0', '5'] if t > 12 else ['', '', '3', '5']
        for k, d in enumerate(digs):
            if d:
                col = SPARK if d == '0' else COPPER
                c.text(x0 + k * w + (w - 20) / 2, 420, d, 'mono', 120, mix(BG, col, a), 'mm')
        val = '305' if t > 12 else '35'
        c.text(960, 650, f'= {val}', 'mono', 60, mix(BG, INK, a), 'mm')
        if t > 12:
            c.text(960, 730, '0：这一位「空着」，但必须占住位置', 'bold', 32, SPARK, 'mm')
    b = fade(t, 16, 17)
    c.rect(300, 800, 1620, 940, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 840, '中国的算筹早在战国就是十进位值制：空位留白', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 895, '罗马数字没有位值：XLVII 里每个字母的大小都是固定的', 'sans', 26, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 8, '同一个 3，放在个位是 3，十位是 30，百位是 300：位置本身就是数'),
                (8.2, 16, '305 和 35 只差一个 0：0 占住了「十位是空的」这件事'),
                (16.2, 22, '有了位值和 0，十个符号就能写出任何数')], y=1010)

def e48_column(c, t, i):
    corner_tag(c, '第 48 集 · 竖式')
    c.text(60, 96, '同一道题：47 × 38', 'serif', 40, INK)
    # left: arabic column multiplication
    L = 560
    lines = [('', '47', 0), ('×', '38', 1), (None, None, 2), ('', '376', 3), ('', '141', 4), (None, None, 5), ('', '1786', 6)]
    for k, (op, txt, idx) in enumerate(lines):
        a = fade(t, 1 + idx * 1.4, 2 + idx * 1.4)
        y = 260 + k * 90
        if txt is None:
            c.line([(L - 220, y - 40), (L + 100, y - 40)], mix(BG, INK, a), 4)
            continue
        c.text(L + 100 - (38 if idx == 4 else 0), y, txt, 'mono', 64, mix(BG, INK if idx < 6 else COPPER, a), 'rs')
        if op: c.text(L - 220, y, op, 'mono', 64, mix(BG, INK, a), 'ls')
    c.text(L - 60, 900, '阿拉伯数字 · 竖式', 'bold', 30, INK, 'mm')
    # right: roman
    R = 1360
    rom = ['XLVII', '× XXXVIII', '= ?']
    for k, s_ in enumerate(rom):
        a = fade(t, 1 + k * 1.5, 2 + k * 1.5)
        c.text(R, 300 + k * 110, s_, 'serif', 60, mix(BG, INK, a), 'mm')
    b = fade(t, 9, 10)
    c.text(R, 640, '没有个位、十位可以对齐', 'sans', 28, mix(BG, NRED, b), 'mm')
    c.text(R, 690, '只能拆开、查表，或者拿算板', 'sans', 28, mix(BG, NRED, b), 'mm')
    c.text(R, 780, '= MDCCLXXXVI', 'serif', 48, mix(BG, COPPER, fade(t, 14, 15)), 'mm')
    c.text(R, 900, '罗马数字', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 9, '位值制让每一位都能对齐：一位一位乘，再错一位加起来'),
                (9.2, 16, '罗马数字没有位可以对齐，只好借助算板或查表'),
                (16.2, 22, '1202 年斐波那契把这套写法介绍到欧洲，账房、商人很快就离不开它')], y=1010)

# ---------------------------------------------------------------- E49 复式记账
def balance(c, cx, cy, left, right, a=1.0):
    tilt = max(-0.25, min(0.25, (right - left) / 400))
    c.poly([(cx, cy), (cx - 30, cy + 80), (cx + 30, cy + 80)], mix(BG, MUTED, a))
    lx, ly = cx - 300 * math.cos(tilt), cy - 300 * math.sin(tilt) * -1
    rx, ry = cx + 300 * math.cos(tilt), cy + 300 * math.sin(tilt)
    ly = cy - 300 * math.sin(-tilt)
    c.line([(lx, cy - 300 * math.sin(tilt)), (rx, cy + 300 * math.sin(tilt))], mix(BG, INK, a), 6)
    return (lx, cy - 300 * math.sin(tilt)), (rx, cy + 300 * math.sin(tilt))

ENTRIES = [('买进 10 斤米', '米 +100 文', '现钱 −100 文'), ('卖出 5 斤米', '现钱 +60 文', '米 −50 文、赚 +10 文'),
           ('借邻居 200 文', '现钱 +200 文', '欠款 +200 文')]

def e49_double(c, t, i):
    corner_tag(c, '第 49 集 · 每笔记两边')
    c.text(60, 96, '一笔钱进来，一定有另一处跟着变', 'serif', 40, INK)
    c.text(560, 200, '去向（借）', 'bold', 32, FIELD, 'mm')
    c.text(1360, 200, '来源（贷）', 'bold', 32, COPPER, 'mm')
    c.line([(960, 170), (960, 760)], LINE, 3)
    c.line([(200, 230), (1720, 230)], LINE, 3)
    n = min(3, int(t / 5.5) + 1) if t > 1 else 0
    for k in range(n):
        a = fade(t, 1 + k * 5.5, 2 + k * 5.5)
        name, l, r = ENTRIES[k]
        y = 300 + k * 150
        c.text(960, y - 34, name, 'sans', 24, mix(BG, MUTED, a), 'mm')
        c.text(560, y + 20, l, 'bold', 32, mix(BG, FIELD, a), 'mm')
        c.text(1360, y + 20, r, 'bold', 32, mix(BG, COPPER, a), 'mm')
    b = fade(t, 17, 18)
    c.rect(360, 800, 1560, 940, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 840, '每一笔都同时记两边，金额相等', 'bold', 30, mix(BG, INK, b), 'mm')
    c.text(960, 895, '所以无论记多少笔，左边总数永远等于右边总数', 'sans', 26, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 6, '买米：米多了 100 文，钱就少了 100 文：一笔，记两处'),
                (6.2, 12, '卖米：钱多了，米少了，还多出来的那部分是赚的'),
                (12.2, 17, '借钱：钱多了，可欠别人的也多了'),
                (17.2, 22, '钱从哪来、到哪去，两边总是一样多')], y=1010)

def e49_check(c, t, i):
    corner_tag(c, '第 49 集 · 两边对不上，就有错')
    c.text(60, 96, '一笔记错了，怎么发现？', 'serif', 40, INK)
    err = t > 7
    left = 360
    right = 360 if not err else 330
    if t > 15: right = 360
    tilt = max(-0.2, min(0.2, (left - right) / 150))
    cx, cy = 960, 520
    c.poly([(cx, cy), (cx - 40, cy + 120), (cx + 40, cy + 120)], MUTED)
    lx, ly = cx - 380, cy + 380 * math.sin(tilt)
    rx, ry = cx + 380, cy - 380 * math.sin(tilt)
    c.line([(lx, ly), (rx, ry)], INK, 8)
    for x, y, v, col, lab in [(lx, ly, left, FIELD, '借方合计'), (rx, ry, right, COPPER, '贷方合计')]:
        c.line([(x, y), (x, y + 120)], MUTED, 3)
        c.rect(x - 130, y + 120, x + 130, y + 200, fill=mix(BG, col, 0.5), r=10)
        c.text(x, y + 160, f'{v} 文', 'mono', 40, INK, 'mm')
        c.text(x, y + 240, lab, 'bold', 28, col, 'mm')
    if err and t <= 15:
        c.text(960, 300, '差了 30 文：一定有一笔只记了一边，或记错了数', 'bold', 32, NRED, 'mm')
    if t > 15:
        c.text(960, 300, '找到了：「卖米」那笔漏记了 30 文。改过来，两边又平了', 'bold', 32, GREEN, 'mm')
    b = fade(t, 17, 18)
    c.rect(300, 860, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 910, '宋代的「四柱法」：旧管 + 新收 − 开除 = 实在；明末出现完整复式的「龙门账」', 'sans', 26, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 7, '记完一个月，把左边加起来、右边加起来：应该一样多'),
                (7.2, 15, '不一样？说明中间有一笔只记了一边，或者写错了数'),
                (15.2, 22, '复式记账用「守恒」查错：1494 年帕乔利把它写进了书里')], y=1030)

# ---------------------------------------------------------------- E50 光学电报
def semaphore(c, x, y, a1, a2, reg, col=INK, s=1.0, a=1.0):
    c.rect(x - 6 * s, y, x + 6 * s, y + 180 * s, fill=mix(BG, MUTED, a))
    rl = 110 * s
    rx0, ry0 = x - rl * math.cos(reg), y - rl * math.sin(reg)
    rx1, ry1 = x + rl * math.cos(reg), y + rl * math.sin(reg)
    c.line([(rx0, ry0), (rx1, ry1)], mix(BG, col, a), int(10 * s))
    for (ex, ey), ang in [((rx0, ry0), a1), ((rx1, ry1), a2)]:
        c.line([(ex, ey), (ex + 60 * s * math.cos(ang), ey + 60 * s * math.sin(ang))], mix(BG, COPPER, a), int(8 * s))

def e50_code(c, t, i):
    corner_tag(c, '第 50 集 · 编码')
    c.text(60, 96, '一座塔能表达多少种意思？', 'serif', 40, INK)
    # left: beacon fire: on/off
    a = fade(t, 0.5, 1.5)
    c.rect(320, 420, 440, 700, fill=mix(BG, (120, 110, 100), a), r=6)
    on = (int(t * 1.2) % 2 == 0)
    if on:
        c.ellipse(380, 390, 50, 70, fill=mix(BG, (240, 130, 50), a))
    c.text(380, 760, '烽火：点或不点', 'bold', 30, mix(BG, INK, a), 'mm')
    c.text(380, 810, '2 种', 'mono', 40, mix(BG, NRED, a), 'mm')
    # right: chappe arms cycling
    b = fade(t, 6, 7)
    if b > 0:
        k = int(t * 1.5)
        a1 = (k % 7) * math.pi / 4
        a2 = ((k * 3) % 7) * math.pi / 4
        reg = 0 if (k // 7) % 2 == 0 else math.pi / 2
        semaphore(c, 1100, 330, a1, a2, reg, s=1.4, a=b)
        c.text(1100, 760, '沙普的信号塔：横臂 2 种 × 两只小臂各 7 种', 'bold', 28, mix(BG, INK, b), 'mm')
        c.text(1100, 810, '2 × 7 × 7 = 98 种', 'mono', 40, mix(BG, COPPER, b), 'mm')
    d = fade(t, 13, 14)
    c.rect(300, 860, 1620, 960, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 890, '再配一本密码本：92 页 × 92 条 ≈ 8464 个词句', 'sans', 26, mix(BG, INK, d), 'mm')
    c.text(960, 930, '烽火只能报「来了」，信号塔能传整句话', 'sans', 24, mix(BG, SPARK, d), 'mm')
    caps(c, t, [(0, 6, '烽火台只有两种状态：点着，或者没点。事先约好，点着就是「敌人来了」'),
                (6.2, 13, '1790 年代，沙普兄弟造了能转动的信号臂：一次能摆出 98 种样子'),
                (13.2, 22, '再配上编号的密码本，就能一个词一个词地拼出整句话')], y=1035)

def e50_relay(c, t, i):
    corner_tag(c, '第 50 集 · 中继')
    c.text(60, 96, '230 公里，消息怎么几分钟就到？', 'serif', 40, INK)
    # hills and towers
    n = 8
    xs = [180 + k * 220 for k in range(n)]
    pts = [(0, 760)]
    for k in range(n):
        pts += [(xs[k] - 110, 760), (xs[k], 640), (xs[k] + 110, 760)]
    pts += [(1920, 760), (1920, 1000), (0, 1000)]
    c.poly(pts, mix(BG, GREEN, 0.25))
    prog = fade(t, 2, 14) * (n - 1)
    for k, x in enumerate(xs):
        lit = prog >= k
        k2 = int(t * 2)
        semaphore(c, x, 520, (k2 % 4) * math.pi / 4 if lit else 0, (k2 % 3) * math.pi / 3 if lit else 0, 0, col=INK if lit else MUTED, s=0.7)
        if k < n - 1 and prog > k:
            f = min(1, prog - k)
            c.line([(x + 40, 470), (x + 40 + (xs[k + 1] - x - 80) * f, 470)], mix(BG, SPARK, 0.8), 3)
    c.text(xs[0], 860, '巴黎', 'bold', 28, INK, 'mm')
    c.text(xs[-1], 860, '里尔', 'bold', 28, INK, 'mm')
    c.text(960, 300, '每座塔用望远镜看上一座，照样摆一遍', 'sans', 28, INK, 'mm')
    b = fade(t, 15, 16)
    if b > 0: c.rect(360, 880, 1560, 960, fill=mix(BG, SHEET, b), r=12)
    if b > 0: c.text(960, 920, '巴黎—里尔约 230 公里、15 座塔：一条短消息约 9 分钟；斯特拉斯堡到巴黎 2 小时，骑马要 4 天', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '一座塔看得见的距离有限：十几公里外再立一座'),
                (6.2, 14, '下一座塔用望远镜看清信号，照样摆出来，一站接一站往下传'),
                (14.2, 22, '编码 + 中继：不用电，消息也能比马快几十倍')], y=1035)

CLIPS = {
 'E48_位值': (e48_place, 22), 'E48_竖式': (e48_column, 22),
 'E48_片头': (titles.opening(SER6, VOL6, S6A, 3, '战国算筹 · 印度数字 · 1202 年斐波那契'), 7),
 'E48_片尾': (titles.closing(SER6, VOL6, S6A, 3, '下集：怎样让账永远算不错？'), 7),
 'E49_两边': (e49_double, 22), 'E49_查错': (e49_check, 22),
 'E49_片头': (titles.opening(SER6, VOL6, S6A, 4, '宋代四柱法 · 1494 年帕乔利'), 7),
 'E49_片尾': (titles.closing(SER6, VOL6, S6A, 4, '下集：不用电，怎么把消息传到百里之外？'), 7),
 'E50_编码': (e50_code, 22), 'E50_中继': (e50_relay, 22),
 'E50_片头': (titles.opening(SER6, VOL6, S6A, 5, '1794 年 · 法国 · 沙普信号塔'), 7),
 'E50_片尾': (titles.closing(SER6, VOL6, S6A, 5, '下集：张衡地动仪，真的能测地震吗？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
