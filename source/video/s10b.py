"""第十季第二批：E65 印刷机、E66 自行车、E67 化肥 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s9b import gear, WOOD
from s10a import S10A, SER10, VOL10, STEELC

INKC = (30, 30, 35)
PAPERL = (225, 215, 190)
OIL = (200, 160, 60)
LEAF = (90, 170, 90)

# ---------------------------------------------------------------- E65 印刷机
def e65_press(c, t, i):
    corner_tag(c, '第 65 集 · 压得匀')
    c.text(60, 96, '手按和螺旋压力机，差在哪里？', 'serif', 40, INK)
    for k, (name, mode) in enumerate([('用手按', 'hand'), ('螺旋压力机', 'screw')]):
        x0 = 140 + k * 880
        a = fade(t, 0.5 + k * 4, 1.5 + k * 4)
        if a <= 0: continue
        c.text(x0 + 330, 190, name, 'bold', 32, mix(BG, INK, a), 'mm')
        # pressure map over the type block (12 x 6 cells)
        rnd = random.Random(7)
        down = fade(t, 1.5 + k * 4, 3 + k * 4)
        cov = 0
        for r in range(6):
            for q in range(12):
                if mode == 'hand':
                    d = math.hypot(q - 3.5, r - 2.5)
                    p = max(0.0, 1 - d / 5.5) * (0.8 + 0.3 * rnd.random())
                else:
                    p = 0.92 + 0.08 * rnd.random()
                p *= down
                ok = p > 0.55
                cov += ok
                col = mix(PAPERL, INKC, min(1, p)) if ok else mix(PAPERL, INKC, p * 0.35)
                c.rect(x0 + q * 55, 420 + r * 55, x0 + q * 55 + 50, 420 + r * 55 + 50, fill=mix(BG, col, a), r=3)
        if mode == 'hand':
            c.ellipse(x0 + 3.5 * 55 + 25, 330 - 30 * (1 - down), 70, 40, fill=mix(BG, (210, 170, 140), a))
        else:
            # screw, platen and bar
            cx = x0 + 330
            ang = 6 * down
            for j in range(8):
                y = 240 + j * 12 + (ang * 4) % 12
                c.line([(cx - 18, y), (cx + 18, y + 8)], mix(BG, STEELC, a), 3)
            c.rect(cx - 10, 220, cx + 10, 340 + 30 * down, fill=mix(BG, STEELC, 0.6 * a))
            bl = 160 * math.cos(ang)
            c.line([(cx - bl, 250), (cx + bl, 250)], mix(BG, WOOD, a), 8)
            c.rect(x0 - 10, 360 + 30 * down, x0 + 660, 390 + 30 * down, fill=mix(BG, WOOD, a), r=4)
        b = fade(t, 3 + k * 4, 4 + k * 4)
        pct = cov / 72 * 100
        c.text(x0 + 330, 800, f'印清楚的格子：{pct:.0f}%', 'bold', 30, mix(BG, NRED if mode == 'hand' else GREEN, b), 'mm')
    d = fade(t, 12, 13)
    c.rect(140, 860, 1780, 940, fill=mix(BG, SHEET, d), r=10)
    c.text(170, 900, '一根横杠（第 39 集杠杆）转动螺丝（第 64 集）：手上的力被放大，又通过一整块平板均匀地压下去', 'sans', 26, mix(BG, INK, d), 'lm')
    caps(c, t, [(0, 4.5, '用手按，力集中在手掌下面：中间印得黑，边上印不出来'),
                (4.7, 12, '螺旋压力机用一块平板压下去：整版受力一样，每个字都印得清楚'),
                (12.2, 22, '古腾堡借来的是榨葡萄、榨油用的螺旋压力机，再配上金属活字和油性墨（约 1450 年）')], y=1010)

def e65_type_ink(c, t, i):
    corner_tag(c, '第 65 集 · 活字与墨')
    c.text(60, 96, '字要一样高，墨要粘得住金属', 'serif', 40, INK)
    # left: type heights
    a = fade(t, 0.5, 1.5)
    c.text(480, 200, '活字的高度', 'bold', 30, mix(BG, INK, a), 'mm')
    rnd = random.Random(3)
    for row, (lab, uneven) in enumerate([('手刻木字：高低不齐', True), ('铸字模铸出的金属字：一样高', False)]):
        y = 420 + row * 260
        c.text(120, y - 110, lab, 'sans', 24, mix(BG, MUTED, a), 'lm')
        down = fade(t, 2 + row * 2, 3.5 + row * 2)
        platen = y - 90 + 40 * down
        c.rect(120, platen - 16, 840, platen, fill=mix(BG, WOOD, a), r=3)
        for q in range(9):
            hgt = 70 + (rnd.uniform(-14, 6) if uneven else 0)
            x = 140 + q * 78
            col = STEELC if not uneven else WOOD
            top = y - hgt + 30
            c.rect(x, top, x + 60, y + 30, fill=mix(BG, col, 0.8 * a), r=2)
            touch = top <= platen + 2
            if down > 0.95:
                c.rect(x + 8, top - 8, x + 52, top - 2, fill=GREEN if touch else NRED)
        if down > 0.95 and uneven:
            c.text(860, y, '矮的字印不上', 'bold', 24, NRED, 'lm')
    # right: ink on metal
    b = fade(t, 9, 10)
    c.text(1400, 200, '墨和金属', 'bold', 30, mix(BG, INK, b), 'mm')
    for row, (lab, col, contact) in enumerate([('水性墨（写字用）', INKC, 140), ('油性墨（亚麻籽油调炭黑）', OIL, 25)]):
        y = 470 + row * 260
        c.rect(1080, y, 1720, y + 30, fill=mix(BG, STEELC, b), r=3)
        c.text(1080, y - 120, lab, 'sans', 24, mix(BG, MUTED, b), 'lm')
        g = fade(t, 10.5 + row * 2, 12 + row * 2)
        if g > 0:
            if contact > 90:
                for q in range(7):
                    bx = 1120 + q * 88 + (q % 2) * 20
                    rr = 16 + (q * 7) % 12
                    c.ellipse(bx, y - rr * g + 2, rr, rr * g, fill=(60, 70, 120), outline=MUTED, width=2)
            else:
                c.rect(1080, y - 14 * g, 1720, y, fill=(20, 20, 24), outline=MUTED, width=2)
            res = '缩成水珠：粘不住' if contact > 90 else '摊开铺平：粘得牢'
            c.text(1720, y - 70, res, 'bold', 26, mix(BG, NRED if contact > 90 else GREEN, g), 'rm')
    caps(c, t, [(0, 8, '毕昇的泥活字在北宋就有了（B3）。古腾堡用铸字模铸出一模一样高的金属字'),
                (8.2, 15, '可写字用的水性墨在金属上缩成一颗颗水珠，印不匀'),
                (15.2, 22, '换成油调的墨，就能均匀地铺在金属字上：压力机、活字、油墨，三样配齐才印得又快又好')], y=1010)

# ---------------------------------------------------------------- E66 自行车
def e66_chain(c, t, i):
    corner_tag(c, '第 66 集 · 链条与齿数')
    c.text(60, 96, '脚踩一圈，车轮转几圈？', 'serif', 40, INK)
    fx, fy, fr, ft = 640, 560, 150, 44
    rx, ry, rr, rt = 1180, 560, 55, 16
    pedal = t * 1.3 * fade(t, 1, 2)
    gear(c, fx, fy, fr, ft, pedal, COPPER)
    gear(c, rx, ry, rr, rt, pedal * ft / rt, COPPER)
    c.line([(fx, fy - fr), (rx, ry - rr)], MUTED, 4)
    c.line([(fx, fy + fr), (rx, ry + rr)], MUTED, 4)
    # crank & pedal
    px, py = fx + 190 * math.cos(pedal), fy + 190 * math.sin(pedal)
    c.line([(fx, fy), (px, py)], STEELC, 10)
    c.rect(px - 40, py - 10, px + 40, py + 10, fill=INK, r=3)
    # wheel
    wx, wy, wr = 1180, 560, 300
    c.ellipse(wx, wy, wr, wr, outline=MUTED, width=6)
    wa = pedal * ft / rt
    for k in range(6):
        q = wa + k * math.pi / 3
        c.line([(wx, wy), (wx + wr * math.cos(q), wy + wr * math.sin(q))], mix(BG, MUTED, 0.6), 2)
    c.ellipse(wx + wr * math.cos(wa), wy + wr * math.sin(wa), 14, 14, fill=NRED)
    a = fade(t, 4, 5)
    c.text(fx, fy + 260, f'前 {ft} 齿', 'bold', 28, mix(BG, INK, a), 'mm')
    c.text(rx + 90, ry, f'后 {rt} 齿', 'bold', 28, mix(BG, INK, a), 'lm')
    b = fade(t, 7, 8)
    c.rect(1520, 220, 1880, 520, fill=mix(BG, SHEET, b), r=10)
    c.text(1550, 260, f'{ft} ÷ {rt} = {ft / rt:.2f}', 'mono', 30, mix(BG, INK, b), 'lm')
    c.text(1550, 310, '脚踩一圈，车轮转 2.75 圈', 'sans', 22, mix(BG, INK, b), 'lm')
    d = fade(t, 11, 12)
    c.text(1550, 380, '车轮周长约 2.1 米', 'sans', 22, mix(BG, INK, d), 'lm')
    c.text(1550, 430, '一圈走约 5.8 米', 'bold', 28, mix(BG, GREEN, d), 'lm')
    c.text(1550, 480, '（步行一步约 0.7 米）', 'sans', 20, mix(BG, MUTED, d), 'lm')
    n = pedal / (2 * math.pi)
    c.text(60, 900, f'踩了 {n:.1f} 圈 → 走了 {n * 5.8:.0f} 米', 'mono', 30, INK, 'lm')
    caps(c, t, [(0, 7, '第 40 集的曲柄把踩踏变成转动，第 41 集的齿轮和轴承让它转得轻'),
                (7.2, 14, '链条连着前后两个齿盘：齿数之比，就是车轮比脚多转的圈数'),
                (14.2, 22, '前 44 齿、后 16 齿，脚踩一圈车轮转 2.75 圈，大约走 5.8 米（数字以你的车为准）')], y=1010)

def e66_balance(c, t, i):
    corner_tag(c, '第 66 集 · 往哪边倒，就往哪边拐')
    c.text(60, 96, '两个轮子为什么不倒？', 'serif', 40, INK)
    # left: rear view lean angle; right: top view path
    lean0 = 0.35
    tau = 2.5
    def lean(u):
        return lean0 * math.exp(-u / tau) * math.cos(u * 1.4) if u > 0 else lean0
    u = max(0.0, t - 3)
    th = lean(u)
    cx, base = 420, 860
    c.text(420, 200, '从后面看', 'bold', 30, INK, 'mm')
    c.line([(140, base), (700, base)], MUTED, 3)
    hx = cx + 420 * math.sin(th)
    hy = base - 420 * math.cos(th)
    c.line([(cx, base), (hx, hy)], STEELC, 14)
    c.ellipse(hx, hy - 40, 40, 40, fill=COPPER)
    c.text(cx, base + 50, f'倾斜 {math.degrees(th):+.0f}°', 'mono', 26, INK, 'mm')
    # top view
    c.text(1300, 200, '从上面看：车轮的轨迹', 'bold', 30, INK, 'mm')
    pts_w, pts_m = [], []
    steps = int(120 * min(1, t / 20))
    x, y, hd = 900, 820, -math.pi / 2
    for j in range(steps + 1):
        uu = max(0.0, j / 6 - 3)
        th_j = lean(uu)
        steer = 0.9 * th_j
        hd += steer * 0.05
        x += 5 * math.cos(hd); y += 5 * math.sin(hd)
        pts_w.append((x + 800 * 0 + (j * 0), y))
        pts_m.append((x + 60 * math.sin(th_j) * math.cos(hd + math.pi / 2) * 1.5, y + 60 * math.sin(th_j) * math.sin(hd + math.pi / 2) * 1.5))
    # map into right panel
    def P(p):
        return (1300 + (p[0] - 900) * 1.4, 820 + (p[1] - 820) * 1.0)
    if len(pts_w) > 1:
        seg(c, [P(p) for p in pts_w], NRED, 4)
        seg(c, [P(p) for p in pts_m], COPPER, 3)
    c.text(1640, 300, '红：车轮着地点', 'sans', 22, NRED, 'lm')
    c.text(1640, 340, '橙：人和车的重心', 'sans', 22, COPPER, 'lm')
    a = fade(t, 14, 15)
    c.rect(960, 860, 1860, 940, fill=mix(BG, SHEET, a), r=10)
    c.text(990, 900, '往右倒 → 车头往右拐 → 车轮跑回重心下面 → 又立起来', 'bold', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '车往右歪了一点：骑车的人会下意识往右拐，车头的设计也会让它自己往右转'),
                (6.2, 14, '一拐弯，车轮就跑到了重心的正下方，车又立了起来；来回几次，越摆越小'),
                (14.2, 22, '所以骑得越快越稳。陀螺效应只帮了一点小忙（2011 年代尔夫特的实验，拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- E67 化肥
STAVES = [('氮', 0.55, LEAF), ('磷', 0.8, OIL), ('钾', 0.35, (170, 120, 200)), ('水', 0.9, (70, 140, 200)), ('光', 0.85, SPARK)]

def e67_barrel(c, t, i):
    corner_tag(c, '第 67 集 · 最短的那块板')
    c.text(60, 96, '庄稼长多少，看它最缺的那一样', 'serif', 40, INK)
    x0, base, W, H = 560, 900, 800, 600
    add = fade(t, 10, 13)   # add potash (wood ash) -> potassium stave grows
    add2 = fade(t, 15, 18)  # then nitrogen
    hs = []
    for k, (name, h, col) in enumerate(STAVES):
        if name == '钾': h = h + (0.75 - h) * add
        if name == '氮': h = h + (0.85 - h) * add2
        hs.append(h)
    lvl = min(hs)
    wv = fade(t, 1, 3)
    c.rect(x0, base - H * lvl * wv, x0 + W, base, fill=mix(BG, (70, 140, 200), 0.45))
    sw = W / len(STAVES)
    for k, (name, h0, col) in enumerate(STAVES):
        h = hs[k]
        a = fade(t, 0.3 + k * 0.3, 1 + k * 0.3)
        c.rect(x0 + k * sw + 4, base - H * h, x0 + (k + 1) * sw - 4, base, outline=mix(BG, col, a), width=5, r=4)
        c.text(x0 + (k + 0.5) * sw, base - H * h - 30, name, 'bold', 32, mix(BG, col, a), 'mm')
    c.line([(x0 - 40, base - H * lvl * wv), (x0 + W + 40, base - H * lvl * wv)], INK, 2)
    c.text(x0 + W + 60, base - H * lvl * wv, f'收成 ≈ {lvl * 100 * wv:.0f}', 'mono', 28, INK, 'lm')
    b = fade(t, 10, 11)
    c.text(120, 400, '草木灰：主要补钾', 'bold', 28, mix(BG, (170, 120, 200), b), 'lm')
    d = fade(t, 15, 16)
    c.text(120, 460, '豆渣、豆科轮作：补氮', 'bold', 28, mix(BG, LEAF, d), 'lm')
    caps(c, t, [(0, 6, '1840 年前后，李比希说：庄稼的收成由最缺的那种养分决定，像木桶装水看最短的那块板'),
                (6.2, 15, '这块地最缺钾：撒一把草木灰，钾的板子变长，水位跟着涨'),
                (15.2, 22, '再补氮，最短的板子又换了一块。施肥要先知道缺什么（板子高低为示意）')], y=1010)

def e67_nitrogen(c, t, i):
    corner_tag(c, '第 67 集 · 空气里的氮')
    c.text(60, 96, '空气里八成是氮，庄稼为什么还缺氮？', 'serif', 40, INK)
    nodes = [('空气中的氮气（约占 78%）', 960, 230, MUTED),
             ('闪电', 360, 470, SPARK), ('豆科根瘤菌（第 29 集）', 960, 470, LEAF), ('哈伯法合成氨（1909 年）', 1560, 470, NRED),
             ('土里能吸收的氮（铵、硝酸盐）', 960, 690, OIL),
             ('庄稼 → 人和牲畜 → 粪肥、豆渣', 960, 880, LEAF)]
    for k, (name, x, y, col) in enumerate(nodes):
        a = fade(t, 0.5 + k * 1.6, 1.5 + k * 1.6)
        w = 300 if k else 380
        c.rect(x - w, y - 40, x + w, y + 40, fill=mix(BG, SHEET, a), outline=mix(BG, col, a), width=3, r=12)
        c.text(x, y, name, 'bold', 28, mix(BG, INK, a), 'mm')
    def arr(x0, y0, x1, y1, a, col=MUTED):
        if a > 0: c.arrow(x0, y0, x0 + (x1 - x0) * a, y0 + (y1 - y0) * a, col, 4, 14)
    for k, x in enumerate([360, 960, 1560]):
        arr(960 + (x - 960) * 0.5, 272, x, 428, fade(t, 2 + k * 1.6, 3 + k * 1.6))
        arr(x, 512, 960 + (x - 960) * 0.4, 648, fade(t, 7.5, 9))
    arr(960, 732, 960, 838, fade(t, 9.5, 10.5))
    c.arrow(1260, 880, 1440, 880, mix(BG, MUTED, fade(t, 11, 12)), 3, 12)
    c.text(1450, 880, '回到土里', 'sans', 22, mix(BG, MUTED, fade(t, 11, 12)), 'lm')
    b = fade(t, 14, 15)
    c.rect(60, 560, 560, 820, fill=mix(BG, SHEET, b), r=10)
    c.text(90, 600, '氮气的两个原子', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(90, 640, '被三根键牢牢拴住', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(90, 700, '庄稼掰不开，', 'bold', 26, mix(BG, NRED, b), 'lm')
    c.text(90, 745, '只有闪电、根瘤菌和', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(90, 785, '高温高压的工厂能掰开', 'sans', 24, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 7, '空气里八成是氮，可那是两个原子紧紧拴在一起的氮气，庄稼用不了'),
                (7.2, 14, '闪电、豆科的根瘤菌，能把它变成土里能吸收的氮'),
                (14.2, 22, '1909 年哈伯在实验室合成了氨，后来工厂用高温高压大批量造氮肥：今天大约一半人的口粮靠它（量级）')], y=1010)

CLIPS = {
 'E65_压力': (e65_press, 22), 'E65_活字与墨': (e65_type_ink, 22),
 'E65_片头': (titles.opening(SER10, VOL10, S10A, 3, '约 1450 年 · 美因茨 · 古腾堡'), 7),
 'E65_片尾': (titles.closing(SER10, VOL10, S10A, 3, '下集：两个轮子，为什么骑起来不倒？'), 7),
 'E66_链传动': (e66_chain, 22), 'E66_扶正': (e66_balance, 22),
 'E66_片头': (titles.opening(SER10, VOL10, S10A, 4, '1885 年 · 斯塔利的「安全自行车」'), 7),
 'E66_片尾': (titles.closing(SER10, VOL10, S10A, 4, '下集：一把草木灰，为什么能让庄稼长得好？'), 7),
 'E67_最小因子': (e67_barrel, 22), 'E67_氮': (e67_nitrogen, 22),
 'E67_片头': (titles.opening(SER10, VOL10, S10A, 5, '1840 年李比希 · 1909 年哈伯'), 7),
 'E67_片尾': (titles.closing(SER10, VOL10, S10A, 5, '下集：夏天，怎么凭空造出冰？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
