"""第八季（第二层 · 光与电）第一批：E52 透镜、E53 显微镜、E54 望远镜 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S8A = [('52', '透镜'), ('53', '显微镜'), ('54', '望远镜'), ('55', '照相'), ('56', '电磁铁'),
       ('57', '电报'), ('58', '电动机'), ('59', '电镀'), ('60', '电灯'), ('61', '蓄电池')]
SER8, VOL8 = '从零造物', '第八季 · 第二层：光与电'
GLASS = (150, 200, 225)
RAY = SPARK

def lens_shape(c, cx, cy, h, t, col=GLASS, a=1.0):
    """biconvex lens: two circular arcs, half-height h, half-thickness t"""
    R = (h * h + t * t) / (2 * t)
    pts = []
    for k in range(41):
        y = -h + 2 * h * k / 40
        x = math.sqrt(max(R * R - y * y, 0)) - (R - t)
        pts.append((cx + x, cy + y))
    for k in range(41):
        y = h - 2 * h * k / 40
        x = math.sqrt(max(R * R - y * y, 0)) - (R - t)
        pts.append((cx - x, cy + y))
    c.poly(pts, mix(BG, col, 0.35 * a))
    seg(c, pts + [pts[0]], mix(BG, col, a), 3)

# ---------------------------------------------------------------- E52 透镜
def e52_refract(c, t, i):
    corner_tag(c, '第 52 集 · 弯曲的玻璃')
    c.text(60, 96, '平行的光，穿过一块凸起的玻璃会怎样？', 'serif', 40, INK)
    cx, cy, F = 760, 520, 420
    lens_shape(c, cx, cy, 230, 40)
    c.line([(120, cy), (1800, cy)], LINE, 2)
    grow = fade(t, 1, 8)
    for k, y0 in enumerate([-180, -120, -60, 0, 60, 120, 180]):
        x0 = 140
        c.line([(x0, cy + y0), (cx, cy + y0)], mix(BG, RAY, 0.9), 3)
        if grow > 0:
            fx, fy = cx + F, cy
            L = grow
            ex = cx + (fx - cx) * min(1, L * 1.6)
            ey = cy + y0 + (fy - (cy + y0)) * min(1, L * 1.6)
            c.line([(cx, cy + y0), (ex, ey)], mix(BG, RAY, 0.9), 3)
            if L > 0.62:
                k2 = (L - 0.62) / 0.38
                c.line([(fx, fy), (fx + (fx - cx) * 0.6 * k2, fy - y0 * 0.6 * k2)], mix(BG, RAY, 0.5), 2)
    a = fade(t, 7, 8)
    c.ellipse(cx + F, cy, 14, 14, fill=mix(BG, NRED, a))
    c.text(cx + F, cy + 50, '焦点', 'bold', 28, mix(BG, NRED, a), 'mm')
    c.arrow(cx, cy + 290, cx + F, cy + 290, mix(BG, MUTED, a), 3, 12)
    c.arrow(cx + F, cy + 290, cx, cy + 290, mix(BG, MUTED, a), 3, 12)
    c.text(cx + F / 2, cy + 325, '焦距', 'sans', 26, mix(BG, MUTED, a), 'mm')
    b = fade(t, 13, 14)
    c.rect(1280, 180, 1860, 420, fill=mix(BG, SHEET, b), r=14)
    c.text(1310, 230, '光进玻璃会拐弯（折射）', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1310, 285, '边缘斜得多，拐得多', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1310, 340, '于是所有光汇到一点', 'bold', 30, mix(BG, SPARK, b), 'lm')
    c.text(1310, 390, '一滴水、一颗玻璃珠都能做到', 'sans', 24, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 7, '一束平行的光，穿过一块中间厚、边缘薄的玻璃'),
                (7.2, 13, '每一条光都拐了个弯，汇到同一个点：焦点。透镜到焦点的距离，叫焦距'),
                (13.2, 22, '越靠边的地方玻璃越斜，光拐得越多：这就是凸透镜能聚光的秘密')], y=1010)

def e52_magnify(c, t, i):
    corner_tag(c, '第 52 集 · 放大镜')
    c.text(60, 96, '放大镜为什么能把字变大？', 'serif', 40, INK)
    cx, cy, F = 900, 560, 300
    lens_shape(c, cx, cy, 200, 34)
    c.line([(150, cy), (1800, cy)], LINE, 2)
    for s in (-1, 1):
        c.ellipse(cx + s * F, cy, 8, 8, fill=NRED)
    c.text(cx - F, cy - 30, '焦点', 'sans', 22, NRED, 'mm')
    ox, oh = cx - 190, 90   # object inside focal length
    c.line([(ox, cy), (ox, cy - oh)], COPPER, 8)
    c.poly([(ox - 16, cy - oh + 8), (ox + 16, cy - oh + 8), (ox, cy - oh - 20)], COPPER)
    c.text(ox, cy + 90, '字（在焦距以内）', 'sans', 22, COPPER, 'mm')
    a = fade(t, 4, 6)
    if a > 0:
        # ray 1: parallel then through far focus; ray 2: through centre
        c.line([(ox, cy - oh), (cx, cy - oh)], mix(BG, RAY, a), 3)
        c.line([(cx, cy - oh), (cx + F * 1.6, cy - oh + oh / F * F * 1.6)], mix(BG, RAY, a), 3)
        c.line([(ox, cy - oh), (cx + 300, cy - oh + (oh / (cx - ox)) * (cx + 300 - ox))], mix(BG, RAY, a), 3)
    do = cx - ox
    di = do * F / (do - F)   # negative
    M = -di / do
    ix = cx + di
    ih = oh * M
    b = fade(t, 8, 10)
    if b > 0:
        # dashed back-extensions to virtual image
        for k in range(14):
            f0, f1 = k / 14, (k + 0.5) / 14
            x0 = cx + (ix - cx) * f0; x1 = cx + (ix - cx) * f1
            y0 = (cy - oh) + ((cy - ih) - (cy - oh)) * f0; y1 = (cy - oh) + ((cy - ih) - (cy - oh)) * f1
            c.line([(x0, y0), (x1, y1)], mix(BG, MUTED, b), 2)
            x0 = cx + (ix - cx) * f0; x1 = cx + (ix - cx) * f1
            y0 = cy + ((cy - ih) - cy) * f0; y1 = cy + ((cy - ih) - cy) * f1
            c.line([(x0, y0), (x1, y1)], mix(BG, MUTED, b), 2)
        c.line([(ix, cy), (ix, cy - ih)], mix(BG, GREEN, b), 8)
        c.poly([(ix - 22, cy - ih + 10), (ix + 22, cy - ih + 10), (ix, cy - ih - 26)], mix(BG, GREEN, b))
        c.text(ix, cy + 40, f'眼睛看到的「虚像」：约 {M:.1f} 倍', 'bold', 24, mix(BG, GREEN, b), 'mm')
    d = fade(t, 14, 15)
    c.rect(1220, 760, 1860, 940, fill=mix(BG, SHEET, d), r=14)
    c.text(1250, 805, '放大倍数 ≈ 25 厘米 ÷ 焦距', 'serif', 30, mix(BG, SPARK, d), 'lm')
    c.text(1250, 860, '焦距 10 厘米 → 约 2.5 倍', 'mono', 24, mix(BG, INK, d), 'lm')
    c.text(1250, 905, '焦距 1 毫米 → 约 250 倍', 'mono', 24, mix(BG, INK, d), 'lm')
    caps(c, t, [(0, 4, '把字放在焦点以内，透过透镜看'),
                (4.2, 10, '从字出发的光被透镜掰得散得慢一些，眼睛顺着光往回找'),
                (10.2, 14, '就在后面「看见」了一个更大的字：它并不真的在那里，叫虚像'),
                (14.2, 22, '焦距越短，放得越大：这条规律，下一集会带我们看见细菌')], y=1010)

# ---------------------------------------------------------------- E53 显微镜
def e53_bead(c, t, i):
    corner_tag(c, '第 53 集 · 玻璃珠')
    c.text(60, 96, '玻璃珠越小，为什么放得越大？', 'serif', 40, INK)
    beads = [(5.0, '5 毫米'), (2.0, '2 毫米'), (1.0, '1 毫米')]
    for k, (D, lab) in enumerate(beads):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        y = 300 + k * 220
        r = D * 18
        cx = 360
        c.ellipse(cx, y, r, r, fill=mix(BG, GLASS, 0.35 * a), outline=mix(BG, GLASS, a), width=3)
        f = 0.75 * D
        fx = cx + r + f * 60
        for dy in (-0.7, -0.35, 0, 0.35, 0.7):
            c.line([(150, y + dy * r), (cx, y + dy * r)], mix(BG, RAY, a), 2)
            c.line([(cx, y + dy * r), (fx, y)], mix(BG, RAY, a), 2)
        c.ellipse(fx, y, 7, 7, fill=mix(BG, NRED, a))
        M = 250 / f
        c.text(cx, y + r + 34, f'直径 {lab}', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1000, y - 20, f'焦距约 {f:.2f} 毫米', 'mono', 28, mix(BG, INK, a), 'lm')
        c.text(1000, y + 30, f'放大约 {M:.0f} 倍', 'bold', 34, mix(BG, SPARK if k == 2 else INK, a), 'lm')
    b = fade(t, 14, 15)
    c.rect(300, 880, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 920, '玻璃球的焦距约为直径的 3/4：1 毫米的珠子，就是一台三百倍的显微镜', 'sans', 26, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 5, '一颗玻璃球就是一块极端的凸透镜'),
                (5.2, 13, '球越小，弯得越厉害，焦距越短：放大倍数大约是 25 厘米除以焦距'),
                (13.2, 22, '一毫米的玻璃珠，能放大三百倍左右。列文虎克用的就是这样的单颗小透镜')], y=1010)

SCALE = [('头发粗细', 70, MUTED), ('洋葱表皮细胞', 200, GREEN), ('红细胞', 8, NRED), ('乳酸菌', 2, SPARK)]

def e53_scale(c, t, i):
    corner_tag(c, '第 53 集 · 看见细菌')
    c.text(60, 96, '放大三百倍，能看见什么？', 'serif', 40, INK)
    mag = 300
    # 1 µm magnified ×300 = 0.3 mm at 25 cm; draw as px: 1 mm -> 6 px at screen (illustrative)
    c.text(960, 190, '放大 300 倍后，在明视距离上看起来有多大（示意）', 'sans', 26, MUTED, 'mm')
    for k, (name, um, col) in enumerate(SCALE):
        a = fade(t, 1 + k * 3, 2 + k * 3)
        if a <= 0: continue
        y = 330 + k * 140
        apparent_mm = um * mag / 1000
        L = max(4, apparent_mm * 12)
        c.text(380, y, name, 'bold', 30, mix(BG, INK, a), 'rm')
        c.text(380, y + 40, f'约 {um} 微米', 'mono', 22, mix(BG, MUTED, a), 'rm')
        if name == '乳酸菌':
            for j in range(6):
                c.rect(440 + j * 40, y - 6, 440 + j * 40 + L, y + 6, fill=mix(BG, col, a), r=6)
        else:
            c.rect(440, y - 14, 440 + min(L, 1400), y + 14, fill=mix(BG, col, 0.8 * a), r=8)
        c.text(440 + min(L, 1400) + (240 if name == '乳酸菌' else 0) + 20, y, f'看起来约 {apparent_mm:.1f} 毫米', 'sans', 24, mix(BG, INK, a), 'lm')
    b = fade(t, 14, 15)
    c.rect(300, 880, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 920, '1676 年，列文虎克写信给英国皇家学会：水里有无数会动的「小动物」', 'bold', 26, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 6, '头发和细胞，放大三百倍就清清楚楚'),
                (6.2, 13, '细菌只有一两微米：放大三百倍，也才半毫米，像一粒小灰尘'),
                (13.2, 22, '可它们在动。列文虎克就是这样第一次看见细菌的')], y=1010)

# ---------------------------------------------------------------- E54 望远镜
def e54_two(c, t, i):
    corner_tag(c, '第 54 集 · 两片透镜')
    c.text(60, 96, '一片焦距长、一片焦距短，排在一起会怎样？', 'serif', 40, INK)
    y = 520
    c.line([(100, y), (1820, y)], LINE, 2)
    xo, fo, fe = 520, 800, 200
    xe = xo + fo + fe
    lens_shape(c, xo, y, 210, 26)
    lens_shape(c, xe, y, 110, 30)
    c.text(xo, y + 250, '物镜（焦距长）', 'bold', 26, INK, 'mm')
    c.text(xe, y + 160, '目镜（焦距短）', 'bold', 26, INK, 'mm')
    fp = xo + fo
    for k in range(12):
        c.line([(fp, y - 200 + k * 34), (fp, y - 200 + k * 34 + 18)], mix(BG, NRED, 0.8), 2)
    c.text(fp, y + 225, '两片透镜共用的焦平面', 'sans', 22, NRED, 'mm')
    a = fade(t, 1, 6)
    tilt = 0.05
    for dy in (-150, -75, 0, 75, 150):
        y0 = y + dy
        sx = 120
        c.line([(sx, y0 - (xo - sx) * tilt), (xo, y0)], mix(BG, RAY, 0.9), 2)
        if a > 0:
            ty = y + fo * tilt
            c.line([(xo, y0), (xo + (fp - xo) * a, y0 + (ty - y0) * a)], mix(BG, RAY, 0.9), 2)
            if a >= 1:
                b = fade(t, 6, 10)
                ey = ty + (ty - y0) * fe / fo
                c.line([(fp, ty), (fp + (xe - fp) * b, ty + (ey - ty) * b)], mix(BG, RAY, 0.9), 2)
                if b >= 1:
                    c.line([(xe, ey), (1760, ey - (1760 - xe) * tilt * fo / fe)], mix(BG, GREEN, 0.9), 2)
    d = fade(t, 11, 12)
    c.text(1500, 260, '进来的光：斜一点点', 'sans', 24, mix(BG, RAY, d), 'mm')
    c.text(1500, 300, '出去的光：斜得多', 'sans', 24, mix(BG, GREEN, d), 'mm')
    e_ = fade(t, 14, 15)
    c.rect(300, 860, 1620, 960, fill=mix(BG, SHEET, e_), r=12)
    c.text(960, 890, '放大倍数 = 物镜焦距 ÷ 目镜焦距', 'serif', 32, mix(BG, SPARK, e_), 'mm')
    c.text(960, 935, '80 厘米 ÷ 20 厘米 = 4 倍；换 4 厘米的目镜就是 20 倍（伽利略最好的望远镜约 20 倍）', 'sans', 22, mix(BG, INK, e_), 'mm')
    caps(c, t, [(0, 6, '远处来的光几乎是平行的：物镜把它们汇到焦点上，成一个小小的倒像'),
                (6.2, 11, '目镜再像放大镜一样，把这个小像放大'),
                (11.2, 22, '进来时只斜一点的光，出去时斜得多：眼睛看到的角度变大了，东西就变近了')], y=1010)

def e54_jupiter(c, t, i):
    corner_tag(c, '第 54 集 · 木星的四颗月亮')
    c.text(60, 96, '1610 年 1 月，伽利略连着几个晚上看见了什么？', 'serif', 40, INK)
    # four moons with approx periods (days): Io 1.77, Europa 3.55, Ganymede 7.15, Callisto 16.7
    moons = [(1.77, 70, 0.3), (3.55, 110, 1.4), (7.15, 175, 2.2), (16.7, 300, 4.0)]
    nights = 5
    for n in range(nights):
        a = fade(t, 1 + n * 2.6, 2 + n * 2.6)
        if a <= 0: continue
        y = 250 + n * 130
        cx = 980
        c.text(260, y, f'第 {n + 1} 晚', 'bold', 28, mix(BG, INK, a), 'lm')
        c.ellipse(cx, y, 26, 26, fill=mix(BG, (225, 190, 140), a))
        for P, R, ph in moons:
            x = cx + R * math.cos(2 * math.pi * n / P + ph)
            c.ellipse(x, y, 7, 7, fill=mix(BG, INK, a))
    b = fade(t, 14, 15)
    c.rect(300, 900, 1620, 970, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 935, '四颗「星」绕着木星来回走：并不是所有天体都绕着地球转（周期示意，按真实轨道周期计算）', 'sans', 23, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '伽利略把望远镜对准木星，旁边有几颗小星星'),
                (6.2, 14, '一晚一晚地画下来：它们忽左忽右，却始终跟着木星'),
                (14.2, 22, '它们是绕着木星转的月亮。两片透镜，改变了人类对天空的看法')], y=1035)

CLIPS = {
 'E52_折射': (e52_refract, 22), 'E52_放大镜': (e52_magnify, 22),
 'E52_片头': (titles.opening(SER8, VOL8, S8A, 0, '穿越北宋 · 一滴水里的放大镜'), 7),
 'E52_片尾': (titles.closing(SER8, VOL8, S8A, 0, '下集：一颗玻璃珠，怎么看见细菌？'), 7),
 'E53_玻璃珠': (e53_bead, 22), 'E53_看见细菌': (e53_scale, 22),
 'E53_片头': (titles.opening(SER8, VOL8, S8A, 1, '穿越北宋 · 比洗手更早看见敌人'), 7),
 'E53_片尾': (titles.closing(SER8, VOL8, S8A, 1, '下集：两片透镜，怎么把月亮拉近？'), 7),
 'E54_两片透镜': (e54_two, 22), 'E54_木星的月亮': (e54_jupiter, 22),
 'E54_片头': (titles.opening(SER8, VOL8, S8A, 2, '穿越北宋 · 把远处拉到眼前'), 7),
 'E54_片尾': (titles.closing(SER8, VOL8, S8A, 2, '下集：光怎么把一幅画留在纸上？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
