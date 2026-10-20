"""第五季收尾：E42 马轭、E43 逆风航行、E44 热气球、第五季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s5a import S5A, SER5, VOL5, WOOD, IRON, BRASS, GREEN, ROPE

HORSE = (150, 112, 80)
SAIL = (226, 214, 190)
WATERC = mix(BG, FIELD, 0.35)

# ---------------------------------------------------------------- E42 马轭
def horse(c, x, y, a=1.0):
    col = mix(BG, HORSE, a)
    c.ellipse(x, y, 190, 80, fill=col)                       # body
    c.poly([(x + 150, y - 40), (x + 230, y - 170), (x + 280, y - 150), (x + 200, y + 10)], col)   # neck
    c.ellipse(x + 285, y - 160, 50, 28, fill=col)            # head
    for dx in (-130, -80, 90, 140):
        c.rect(x + dx - 12, y + 50, x + dx + 12, y + 200, fill=col, r=6)
    c.ellipse(x + 300, y - 168, 6, 6, fill=BG)

def e42_harness(c, t, i):
    corner_tag(c, '第 42 集 · 三种挽具')
    c.text(60, 96, '同一匹马，绳子套在哪里，差别很大', 'serif', 40, INK)
    stage = 0 if t < 7 else (1 if t < 14 else 2)
    names = ['颈带：勒在脖子前面', '胸带：横在胸前', '马轭：卡在肩膀上']
    cols = [NRED, SPARK, GREEN]
    hx, hy = 720, 600
    horse(c, hx, hy)
    pull = 0.5 + 0.5 * math.sin(t * 2)
    if stage == 0:
        # strap across throat rising up the neck
        c.line([(hx + 210, hy - 120 - 20 * pull), (hx + 170, hy - 30)], NRED, 12)
        c.line([(hx + 190, hy - 75), (hx - 300, hy - 60)], ROPE, 6)
        c.arrow(hx + 230, hy - 110, hx + 260, hy - 150, NRED, 5, 16)
        c.text(hx + 300, hy - 60, '一用力，带子往上滑，压住气管和颈部血管', 'sans', 26, NRED, 'lm')
    elif stage == 1:
        c.line([(hx + 200, hy - 10), (hx + 170, hy + 50)], SPARK, 14)
        c.line([(hx + 185, hy + 20), (hx - 300, hy + 10)], ROPE, 6)
        c.text(hx + 260, hy + 30, '力压在胸骨上，不勒脖子', 'sans', 26, SPARK, 'lm')
    else:
        c.ellipse(hx + 175, hy - 60, 40, 90, outline=GREEN, width=16)
        c.line([(hx + 175, hy + 20), (hx - 300, hy + 40)], ROPE, 6)
        c.text(hx + 260, hy - 60, '力压在肩膀两侧的骨头上', 'sans', 26, GREEN, 'lm')
        c.text(hx + 260, hy - 15, '拉点低，更适合犁地和重车', 'sans', 26, GREEN, 'lm')
    c.rect(hx - 420, hy - 100, hx - 300, hy + 60, fill=mix(BG, WOOD, 0.7), r=8)
    for k, n in enumerate(names):
        c.text(200 + k * 560, 240, n, 'bold', 30, cols[k] if k == stage else MUTED, 'lm')
    caps(c, t, [(0, 7, '古希腊罗马的颈带：马一用力，带子就往上滑，勒住脖子（此说有争议）'),
                (7.2, 14, '中国很早就用胸带：力压在胸前，不勒脖子'),
                (14.2, 22, '后来又出现硬质的马轭，卡在肩上：最晚北魏的壁画里已经能看到')], y=1010)

def e42_pressure(c, t, i):
    corner_tag(c, '第 42 集 · 压强')
    c.text(60, 96, '同样的拉力，压在细绳上和宽带上', 'serif', 40, INK)
    for k, (cx, w, lab, col) in enumerate([(560, 16, '细绳：面积小', NRED), (1360, 220, '宽垫：面积大', GREEN)]):
        a = fade(t, 0.5 + k * 4, 1.5 + k * 4)
        if a <= 0: continue
        dent = fade(t, 2 + k * 4, 5 + k * 4)
        depth = (110 if k == 0 else 14) * dent
        # sponge block
        top = 620
        pts = [(cx - 300, top)]
        for j in range(61):
            x = cx - 300 + j * 10
            d = depth * math.exp(-((x - cx) / (w / 2 + 30)) ** 4) if True else 0
            pts.append((x, top + d))
        pts += [(cx + 300, top), (cx + 300, 900), (cx - 300, 900)]
        c.poly(pts, mix(BG, (230, 200, 120), a))
        c.rect(cx - w / 2, top - 40 + depth, cx + w / 2, top + depth, fill=mix(BG, col, a), r=4)
        c.arrow(cx, 330, cx, top - 50 + depth, mix(BG, INK, a), 8, 22)
        c.text(cx, 300, '同样 10 千克', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(cx, 950, lab, 'bold', 30, mix(BG, col, a), 'mm')
    b = fade(t, 13, 14)
    c.text(960, 220, '压强 = 力 ÷ 面积', 'serif', 40, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 8, '细绳压下去，海绵陷得很深：力全集中在一条线上'),
                (8.2, 13, '换成宽垫，同样的力分散开，几乎压不出印子'),
                (13.2, 22, '马轭带衬垫、贴着肩膀，力分散在大块骨头上，马才敢使全力')], y=1030)

# ---------------------------------------------------------------- E43 逆风航行
def boat(c, x, y, heading, sail_ang, a=1.0, keel=True):
    """heading, sail_ang in radians, screen coords, 0 = up"""
    fx, fy = math.sin(heading), -math.cos(heading)
    rx, ry = math.cos(heading), math.sin(heading)
    hull = [(x + fx * 90, y + fy * 90), (x + rx * 34, y + ry * 34), (x - fx * 80 + rx * 26, y - fy * 80 + ry * 26),
            (x - fx * 80 - rx * 26, y - fy * 80 - ry * 26), (x - rx * 34, y - ry * 34)]
    c.poly(hull, mix(BG, WOOD, a))
    if keel:
        c.line([(x - fx * 60, y - fy * 60), (x + fx * 60, y + fy * 60)], mix(BG, IRON, a), 6)
    sa = heading + math.pi + sail_ang
    sx, sy = math.sin(sa), -math.cos(sa)
    c.line([(x, y), (x + sx * 100, y + sy * 100)], mix(BG, SAIL, a), 10)

def e43_lift(c, t, i):
    corner_tag(c, '第 43 集 · 帆的升力')
    c.text(60, 96, '风从侧面吹来，船为什么往前走？', 'serif', 40, INK)
    # wind from top (north) blowing down
    for k in range(7):
        ph = (t * 0.6 + k / 7) % 1
        x = 260 + k * 200
        c.arrow(x, 160 + ph * 200, x, 200 + ph * 200, mix(BG, FIELD, 0.8), 4, 12)
    c.text(1700, 200, '风', 'serif', 40, FIELD, 'mm')
    cx, cy = 900, 640
    heading = math.radians(-50)       # sailing up-left, 50° off the wind
    boat(c, cx, cy, heading, math.radians(25), 1.0, keel=fade(t, 11, 12) > 0.5)
    a = fade(t, 4, 5)
    # sail force: perpendicular to sail, roughly
    Fx, Fy = 200 * math.cos(math.radians(-15)), 200 * math.sin(math.radians(-15)) * -1
    Fx, Fy = -310, 113
    c.arrow(cx, cy, cx + Fx, cy + Fy, mix(BG, COPPER, a), 8, 22)
    c.text(cx + Fx - 20, cy + Fy + 10, '帆上的合力', 'bold', 26, mix(BG, COPPER, a), 'rm')
    b = fade(t, 7, 8)
    hx, hy = math.sin(heading), -math.cos(heading)
    proj = Fx * hx + Fy * hy
    c.arrow(cx, cy, cx + hx * proj, cy + hy * proj, mix(BG, GREEN, b), 6, 18)
    c.text(cx + hx * proj - 20, cy + hy * proj - 30, '往前的分力', 'sans', 24, mix(BG, GREEN, b), 'rm')
    sx_, sy_ = Fx - hx * proj, Fy - hy * proj
    c.arrow(cx, cy, cx + sx_, cy + sy_, mix(BG, NRED, b), 6, 18)
    c.text(cx + sx_ - 10, cy + sy_ + 40, '侧推力', 'sans', 24, mix(BG, NRED, b), 'mm')
    k = fade(t, 12, 13)
    if k > 0:
        c.arrow(cx, cy, cx - sx_, cy - sy_, mix(BG, IRON, k), 6, 18)
        c.text(cx - sx_ + 20, cy - sy_, '龙骨的水阻力抵消侧推', 'sans', 24, mix(BG, INK, k), 'lm')
    c.rect(1300, 620, 1860, 900, fill=SHEET, r=14)
    c.text(1330, 670, '帆像一片竖起来的机翼', 'bold', 28, INK, 'lm')
    c.text(1330, 720, '风绕过弯曲的帆，产生侧向的「升力」', 'sans', 24, INK, 'lm')
    c.text(1330, 770, '一部分往前，一部分往侧面', 'sans', 24, INK, 'lm')
    c.text(1330, 820, '水下的龙骨挡住侧面那部分', 'sans', 24, INK, 'lm')
    caps(c, t, [(0, 4, '风从北边吹来，船却往西北方向走'),
                (4.2, 11, '帆把风「拐」了个弯，得到一个斜向的力：一部分往前推船，一部分往侧面推'),
                (11.2, 22, '船底的龙骨插在水里，侧面推不动它，剩下的就只有往前了')], y=1010)

def e43_tack(c, t, i):
    corner_tag(c, '第 43 集 · 走之字形')
    c.text(60, 96, '正顶着风走不了，那就斜着走', 'serif', 40, INK)
    for k in range(7):
        ph = (t * 0.6 + k / 7) % 1
        x = 220 + k * 230
        c.arrow(x, 150 + ph * 120, x, 190 + ph * 120, mix(BG, FIELD, 0.8), 4, 12)
    sx, sy = 700, 940
    gx, gy = 700, 300
    c.ellipse(gx, gy, 18, 18, fill=SPARK)
    c.text(gx + 30, gy, '目的地（在上风方向）', 'sans', 26, SPARK, 'lm')
    # no-go zone wedge
    a = fade(t, 1, 2)
    for side in (-1, 1):
        ang = math.radians(45) * side
        c.line([(sx, sy), (sx + 300 * math.sin(ang), sy - 300 * math.cos(ang))], mix(BG, NRED, a * 0.8), 3)
    c.text(sx + 240, sy - 230, '迎风 ±45° 以内：走不了', 'sans', 24, mix(BG, NRED, a), 'lm')
    # zigzag path
    legs = []
    xs = [0, -110, 110, -110, 110, -110, 0]
    for k in range(6):
        legs.append(((sx + xs[k], sy - 106 * k), (sx + xs[k + 1], sy - 106 * (k + 1))))
    prog = fade(t, 4, 20) * len(legs)
    drawn = []
    for j, (p0, p1) in enumerate(legs):
        if prog <= j: break
        f = min(1, prog - j)
        q = (p0[0] + (p1[0] - p0[0]) * f, p0[1] + (p1[1] - p0[1]) * f)
        c.line([p0, q], GREEN, 5)
        drawn = (p0, q, p1)
    if drawn:
        p0, q, p1 = drawn
        hd = math.atan2(p1[0] - p0[0], -(p1[1] - p0[1]))
        boat(c, q[0], q[1], hd, math.radians(25 if p1[0] < p0[0] else -25), 1.0)
    b = fade(t, 10, 11)
    c.rect(1180, 420, 1860, 760, fill=mix(BG, SHEET, b), r=14)
    c.text(1210, 470, '每走一段就「掉头」换一边', 'bold', 28, mix(BG, INK, b), 'lm')
    c.text(1210, 530, '多走了路，但一直在往上风方向前进', 'sans', 24, mix(BG, INK, b), 'lm')
    c.text(1210, 600, '宋代徐兢：「风有八面，', 'serif', 26, mix(BG, COPPER, b), 'lm')
    c.text(1210, 645, '唯当头不可行」（原文待核）', 'serif', 26, mix(BG, COPPER, b), 'lm')
    c.text(1210, 700, '正顶风走不了，其余方向都能借', 'sans', 22, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 4, '目的地正好在上风方向：直着开过去，帆就瘪了'),
                (4.2, 12, '那就斜着走：和风向成 45 度左右，走一段，掉头，再斜着走一段'),
                (12.2, 22, '这叫「抢风」或「之字形航行」：多走点路，却能一步步顶着风前进')], y=1010)

# ---------------------------------------------------------------- E44 热气球
RH = random.Random(44)
MOL = [(RH.uniform(0, 1), RH.uniform(0, 1), RH.uniform(0, 6.28), RH.uniform(0.6, 1.4)) for _ in range(60)]

def e44_density(c, t, i):
    corner_tag(c, '第 44 集 · 热空气更轻')
    c.text(60, 96, '空气一受热，为什么就变轻了？', 'serif', 40, INK)
    for k, (cx, lab, T, col) in enumerate([(560, '20 ℃ 的空气', 293, FIELD), (1360, '100 ℃ 的空气', 373, COPPER)]):
        a = fade(t, 0.5 + k * 5, 1.5 + k * 5)
        if a <= 0: continue
        bw, bh = 520, 440
        x0, y0 = cx - bw / 2, 260
        c.rect(x0, y0, x0 + bw, y0 + bh, outline=mix(BG, LINE, a), width=4, r=10)
        n = 48 if k == 0 else int(48 * 293 / 373)
        sp = 1.0 if k == 0 else math.sqrt(373 / 293)
        for j, (u, v, ph, s) in enumerate(MOL[:n]):
            px = x0 + 20 + ((u + 0.07 * sp * s * math.sin(t * 2.5 * sp + ph)) % 1) * (bw - 40)
            py = y0 + 20 + ((v + 0.07 * sp * s * math.cos(t * 2.2 * sp + ph)) % 1) * (bh - 40)
            c.ellipse(px, py, 9, 9, fill=mix(BG, col, a))
        c.text(cx, y0 - 40, lab, 'bold', 30, mix(BG, col, a), 'mm')
        dens = 1.204 * 293 / T
        c.text(cx, y0 + bh + 50, f'同样一立方米：约 {dens:.2f} 千克', 'sans', 28, mix(BG, INK, a), 'mm')
    b = fade(t, 12, 13)
    c.rect(360, 830, 1560, 950, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 865, '分子跑得更快、彼此离得更远：同样体积里的分子少了', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 915, '每立方米轻了约 0.26 千克：这就是热气球能拿到的「浮力」', 'bold', 28, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 5, '一盒 20 度的空气：分子挤得满满的'),
                (5.2, 12, '加热到 100 度：分子跑得更快，把彼此推得更远，同样体积里装的分子少了'),
                (12.2, 22, '热空气比周围的冷空气轻，就像木头在水里一样，会被托起来')], y=1010)

def e44_lift(c, t, i):
    corner_tag(c, '第 44 集 · 要多大的球')
    c.text(60, 96, '想带一个人上天，球要多大？', 'serif', 40, INK)
    per = 1.204 * (1 - 293 / 373)            # kg per m^3
    payload = 70 + 130                       # 人 + 吊篮、球皮、燃料（示意）
    V = payload / per
    r_m = (3 * V / (4 * math.pi)) ** (1 / 3)
    grow = fade(t, 3, 12)
    R = 40 + 200 * grow
    cx, cy = 760, 500
    c.ellipse(cx, cy - 20, R, R * 1.1, fill=mix(BG, COPPER, 0.55), outline=COPPER, width=4)
    c.poly([(cx - R * 0.45, cy + R * 0.95), (cx + R * 0.45, cy + R * 0.95), (cx + 30, cy + R * 1.15 + 20), (cx - 30, cy + R * 1.15 + 20)], mix(BG, COPPER, 0.4))
    c.rect(cx - 40, cy + R * 1.15 + 40, cx + 40, cy + R * 1.15 + 100, fill=WOOD, r=6)
    c.line([(cx - 30, cy + R * 1.15 + 20), (cx - 36, cy + R * 1.15 + 40)], ROPE, 3)
    c.line([(cx + 30, cy + R * 1.15 + 20), (cx + 36, cy + R * 1.15 + 40)], ROPE, 3)
    c.text(cx, cy - 20, f'{V * grow:.0f} 立方米', 'bold', 34, INK, 'mm')
    c.rect(1240, 240, 1860, 720, fill=SHEET, r=14)
    rows = [('100 ℃ 热气 vs 20 ℃ 空气', ''), ('每立方米能托起', f'约 {per:.2f} 千克'),
            ('一个人 + 吊篮、球皮等', f'约 {payload} 千克（示意）'), ('需要的热空气', f'约 {V:.0f} 立方米'),
            ('相当于直径', f'约 {2 * r_m:.0f} 米的球')]
    for k, (a_, b_) in enumerate(rows):
        al = fade(t, 2 + k * 2, 3 + k * 2)
        c.text(1270, 290 + k * 85, a_, 'sans', 26, mix(BG, INK, al), 'lm')
        if b_: c.text(1270, 330 + k * 85, b_, 'bold', 28, mix(BG, COPPER, al), 'lm')
    caps(c, t, [(0, 6, '热空气每立方米只比冷空气轻四分之一千克左右'),
                (6.2, 14, '要托起一个人和吊篮，就得装下七八百立方米的热空气'),
                (14.2, 22, '1783 年，蒙戈尔菲耶兄弟的热气球第一次带人飞上天')], y=1010)

# ---------------------------------------------------------------- 第五季特辑：力的变形记
ITEMS = [('放大', '杠杆滑轮', '39'), ('稳住', '被中香炉', 'B8'), ('转换', '曲柄连杆', '40'),
         ('变速', '齿轮轴承', '41'), ('记方向', '指南车', 'B17'), ('咬合', '榫卯', 'B7'),
         ('拉车', '马轭', '42'), ('借风', '逆风航行', '43'), ('借热', '热气球', '44')]

def s5_forces(c, t, i):
    corner_tag(c, '第五季特辑 · 力的变形记')
    c.text(60, 110, '第五季：力的变形记', 'serif', 48, INK, 'lm')
    for k, (verb, name, num) in enumerate(ITEMS):
        col, row = k % 3, k // 3
        cx, cy = 420 + col * 540, 300 + row * 230
        a = fade(t, 1 + k * 2, 2 + k * 2)
        c.rect(cx - 230, cy - 85, cx + 230, cy + 85, fill=mix(BG, SHEET, a), outline=mix(BG, COPPER if k % 2 == 0 else FIELD, a), width=3, r=16)
        c.text(cx - 200, cy - 20, verb, 'serif', 46, mix(BG, COPPER if k % 2 == 0 else FIELD, a), 'lm')
        c.text(cx + 10, cy - 20, name, 'bold', 30, mix(BG, INK, a), 'lm')
        c.text(cx + 10, cy + 30, num, 'mono', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 10, '第五季的九集，都在给力「变形」：放大它、稳住它、换个方向转'),
                (10.2, 19, '让它变快变慢、记住方向、咬紧不松'),
                (19.2, 28, '最后让马拉得动、船顶风走、人飞上天：省力，从来都要拿距离去换')], y=1010)

CLIPS = {
 'E42_三种挽具': (e42_harness, 22), 'E42_压强': (e42_pressure, 22),
 'E42_片头': (titles.opening(SER5, VOL5, S5A, 3, '北魏壁画里的马轭 · 穿越北宋'), 7),
 'E42_片尾': (titles.closing(SER5, VOL5, S5A, 3, '下集：帆船为什么能逆风前进？'), 7),
 'E43_升力': (e43_lift, 22), 'E43_之字形': (e43_tack, 22),
 'E43_片头': (titles.opening(SER5, VOL5, S5A, 4, '北宋 · 1123 年 · 出使高丽的海船'), 7),
 'E43_片尾': (titles.closing(SER5, VOL5, S5A, 4, '下集：一团热空气，怎么把人带上天？'), 7),
 'E44_热空气': (e44_density, 22), 'E44_多大的球': (e44_lift, 22),
 'E44_片头': (titles.opening(SER5, VOL5, S5A, 5, '1783 年 · 法国 · 蒙戈尔菲耶兄弟'), 7),
 'E44_片尾': (titles.closing(SER5, VOL5, S5A, 5, '下集：第五季特辑'), 7),
 'S5_力的变形记': (s5_forces, 28),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
