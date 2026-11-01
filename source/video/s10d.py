"""第十季收尾：E71 对数与计算尺、第十季特辑（第二层 · 下回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s10a import S10A, SER10, VOL10

RULER = (215, 200, 160)

def log_scale(c, x0, x1, y, up, a=1.0, label=True):
    """draw a 1..10 log scale; up=True puts ticks above the line"""
    L = x1 - x0
    c.line([(x0, y), (x1, y)], mix(BG, INK, a), 2)
    s = -1 if up else 1
    for v in [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10]:
        x = x0 + L * math.log10(v)
        major = v == int(v)
        c.line([(x, y), (x, y + s * (22 if major else 12))], mix(BG, INK, a), 2)
        if major and label:
            c.text(x, y + s * 42, f'{int(v)}', 'mono', 24, mix(BG, INK, a), 'mm')

def e71_log(c, t, i):
    corner_tag(c, '第 71 集 · 把乘法变成加法')
    c.text(60, 96, '2、4、8、16……乘以 2，就是往前走一格', 'serif', 40, INK)
    pw = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    x0, dx = 180, 150
    for k, v in enumerate(pw):
        a = fade(t, 0.3 + k * 0.25, 0.8 + k * 0.25)
        x = x0 + k * dx
        c.rect(x - 60, 230, x + 60, 300, fill=mix(BG, SHEET, a), r=8)
        c.text(x, 265, f'{v}', 'mono', 30, mix(BG, INK, a), 'mm')
        c.text(x, 335, f'第 {k} 格', 'sans', 20, mix(BG, MUTED, a), 'mm')
    # example 8 x 32 = 256 -> 3 + 5 = 8
    b = fade(t, 4, 5)
    if b > 0:
        for k, col in ((3, FIELD), (5, COPPER)):
            x = x0 + k * dx
            c.rect(x - 62, 228, x + 62, 302, outline=mix(BG, col, b), width=4, r=8)
        c.text(960, 420, '8 × 32 = ?', 'mono', 40, mix(BG, INK, b), 'mm')
        d = fade(t, 6, 7)
        c.text(960, 490, '8 在第 3 格，32 在第 5 格：3 + 5 = 8', 'sans', 30, mix(BG, INK, d), 'mm')
        e = fade(t, 8, 9)
        if e > 0:
            x = x0 + 8 * dx
            c.rect(x - 62, 228, x + 62, 302, outline=mix(BG, GREEN, e), width=5, r=8)
            c.text(960, 560, '第 8 格是 256：8 × 32 = 256', 'bold', 32, mix(BG, GREEN, e), 'mm')
    # log rulers: lengths add
    f = fade(t, 11, 12)
    if f > 0:
        X0, X1 = 260, 1660
        L = X1 - X0
        off = L * math.log10(2) * ease(fade(t, 13, 15))
        log_scale(c, X0, X1, 800, False, f)
        c.rect(X0 + off - 4, 700, X1 + off + 4, 760, fill=mix(BG, RULER, 0.25 * f), r=4)
        log_scale(c, X0 + off, X1 + off, 760, True, f)
        c.text(X0 - 30, 730, '上尺', 'sans', 22, mix(BG, MUTED, f), 'rm')
        c.text(X0 - 30, 830, '下尺', 'sans', 22, mix(BG, MUTED, f), 'rm')
        g = fade(t, 15.5, 16.5)
        if g > 0:
            x3 = X0 + off + L * math.log10(3)
            c.line([(x3, 660), (x3, 900)], mix(BG, NRED, g), 3)
            c.text(x3, 930, '上尺的 3 对着下尺的 6：2 × 3 = 6', 'bold', 28, mix(BG, NRED, g), 'mm')
    caps(c, t, [(0, 4, '把 1、2、4、8……排成一排：每乘一次 2，就往前走一格'),
                (4.2, 11, '8 乘 32，不用乘：8 在第 3 格，32 在第 5 格，3 加 5 是第 8 格，就是 256'),
                (11.2, 22, '把这种「格数」画成刻度：两把尺子一滑，长度相加，就是数相乘。这种格数，叫对数')], y=1010)

def e71_rule(c, t, i):
    corner_tag(c, '第 71 集 · 计算尺')
    c.text(60, 96, '3.5 × 4.2 = ?   用两把尺子算', 'serif', 40, INK)
    X0, X1 = 300, 1620
    L = X1 - X0
    a = fade(t, 0.5, 1.5)
    o1 = L * math.log10(3.5)
    o2 = L * (math.log10(3.5) - 1)
    off = o1 * ease(fade(t, 2, 5)) + (o2 - o1) * ease(fade(t, 9, 12))
    c.rect(X0 - 20, 600, X1 + 20, 700, fill=mix(BG, RULER, 0.25 * a), r=6)
    log_scale(c, X0, X1, 600, False, a)
    c.rect(X0 + off - 20, 480, X1 + off + 20, 600, fill=mix(BG, RULER, 0.35 * a), r=6)
    log_scale(c, X0 + off, X1 + off, 600, True, a)
    if t < 9:
        c.text(X0 - 40, 540, '上尺', 'sans', 22, MUTED, 'rm'); c.text(X0 - 40, 650, '下尺', 'sans', 22, MUTED, 'rm')
    if 5 < t < 9:
        b = fade(t, 5, 6)
        x42 = X0 + off + L * math.log10(4.2)
        c.line([(X0 + off, 420), (X0 + off, 740)], mix(BG, FIELD, b), 3)
        c.text(X0 + off, 400, '上尺的 1 对准 3.5', 'bold', 26, mix(BG, FIELD, b), 'mm')
        c.text(min(x42, 1840), 400, '4.2 在这儿：尺子外面了', 'bold', 26, mix(BG, NRED, fade(t, 6.5, 7.5)), 'rm')
    if t >= 12:
        e = fade(t, 12, 13)
        xi = X0 + off + L
        c.line([(xi, 420), (xi, 740)], mix(BG, FIELD, e), 3)
        c.text(xi, 400, '上尺的 10 对准 3.5', 'bold', 26, mix(BG, FIELD, e), 'mm')
        x42 = X0 + off + L * math.log10(4.2)
        g = fade(t, 13.5, 14.5)
        c.line([(x42, 440), (x42, 760)], mix(BG, NRED, g), 3)
        c.text(x42, 790, '上尺的 4.2 对着下尺约 1.47', 'bold', 28, mix(BG, NRED, g), 'mm')
    h = fade(t, 16, 17)
    c.rect(300, 860, 1620, 940, fill=mix(BG, SHEET, h), r=10)
    c.text(330, 900, '读出 1.47，再估小数点：3.5 × 4.2 ≈ 14.7（计算器 14.7）。计算尺能读三位左右', 'sans', 26, mix(BG, INK, h), 'lm')
    caps(c, t, [(0, 8.8, '下尺不动，把上尺的 1 滑到下尺的 3.5：可上尺的 4.2 跑到尺子外面去了'),
                (9, 16, '那就把上尺往回滑，用另一头的 10 对准 3.5：上尺的 4.2 正对下尺的 1.47'),
                (16.2, 22, '小数点自己估：14.7。三位有效数字，造桥、算工程的草稿都够用')], y=1010)

# ---------------------------------------------------------------- 第十季特辑：第二层（下）
OLD10 = [('炼铁', '18'), ('煤与焦炭', '19'), ('石灰与水泥', '24'), ('杠杆', '39'), ('曲柄连杆', '40'), ('齿轮与轴承', '41'),
         ('活字印刷', 'B3'), ('轮作固氮', '29'), ('肥皂', '22'), ('蒸发冷却', '38'), ('冰鉴', 'B12'), ('虹吸', '26'),
         ('通风', '36'), ('摩擦起电', '01'), ('静电机', '14'), ('数字与 0', '48')]
NEW10 = [('钢', '62', ['炼铁', '煤与焦炭']), ('钢筋混凝土', '63', ['石灰与水泥', '钢']), ('螺丝', '64', ['杠杆', '齿轮与轴承']),
         ('印刷机', '65', ['活字印刷', '螺丝']), ('自行车', '66', ['曲柄连杆', '齿轮与轴承']), ('化肥', '67', ['轮作固氮', '肥皂']),
         ('制冷', '68', ['蒸发冷却', '冰鉴']), ('抽水马桶', '69', ['虹吸', '通风']), ('避雷针', '70', ['摩擦起电', '静电机']),
         ('计算尺', '71', ['数字与 0'])]

def s10_layer(c, t, i):
    corner_tag(c, '第十季特辑 · 第二层（下）')
    c.text(60, 118, '第二层（下）：每一集都长在旧的节点上', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD10):
        pos[name] = (340, 205 + k * 50)
    for k, (name, num, deps) in enumerate(NEW10):
        pos[name] = (1180 + (200 if name in ('钢筋混凝土', '印刷机') else 0), 225 + k * 76)
    c.text(340, 168, '前九季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1280, 168, '第十季新长出', 'sans', 24, MUTED, 'mm')
    oldset = set(n for n, _ in OLD10)
    for k, (name, num, deps) in enumerate(NEW10):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx = x0 + 110
            ex = x1 - 110
            col = mix(BG, FIELD if d in oldset else COPPER, a * 0.8)
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, col, 2)
    for name, num in OLD10:
        x, y = pos[name]
        c.rect(x - 110, y - 21, x + 110, y + 21, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, MUTED, 'lm')
        c.text(x + 14, y, name, 'sans', 21, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW10):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 14, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十季的十集，把第二层剩下的三条链长完：材料、机械、日常'),
                (8.2, 16, '炼铁加焦炭长出钢，钢又和水泥长成钢筋混凝土；杠杆和齿轮长出螺丝，螺丝又长出印刷机'),
                (16.2, 24, '虹吸长出抽水马桶，摩擦起电长出避雷针，数字与 0 长出计算尺'),
                (24.2, 30, '第二层的五条链，全部点亮')], y=1040)

CLIPS = {
 'E71_对数': (e71_log, 22), 'E71_计算尺': (e71_rule, 22),
 'E71_片头': (titles.opening(SER10, VOL10, S10A, 9, '1614 年 · 纳皮尔的对数表'), 7),
 'E71_片尾': (titles.closing(SER10, VOL10, S10A, 9, '下集：第十季特辑 · 第二层（下）'), 7),
 'S10_第二层下': (s10_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
