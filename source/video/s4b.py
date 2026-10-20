"""第四季第二批：E37 罐藏、E31 口服补液、E35 种痘 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s4a import S4A, SER4, VOL4, GERM, GREEN

BROTH = (200, 160, 90)
GLASS = (150, 175, 190)
SALT = (235, 235, 240)
SUGAR = (242, 189, 69)

def microbe(c, x, y, r=9, col=GERM, a=1.0):
    c.ellipse(x, y, r, r * 0.7, fill=mix(BG, col, a))

# ---------------------------------------------------------------- E37 罐藏
RJ = random.Random(37)
SPOTS = [(RJ.uniform(-110, 110), RJ.uniform(-120, 150)) for _ in range(60)]

def jar(c, cx, top, cloud, lid, label, sub):
    c.rect(cx - 140, top, cx + 140, top + 380, fill=mix(BG, GLASS, 0.25), outline=GLASS, width=4, r=22)
    c.rect(cx - 130, top + 70, cx + 130, top + 370, fill=mix(mix(BG, BROTH, 0.55), (120, 110, 80), cloud), r=16)
    if lid:
        c.rect(cx - 150, top - 30, cx + 150, top + 6, fill=(170, 172, 178), r=6)
    c.text(cx, top + 500, label, 'bold', 30, INK, 'mm')
    c.text(cx, top + 545, sub, 'sans', 24, MUTED, 'mm')

def e37_seal(c, t, i):
    corner_tag(c, '第 37 集 · 加热与密封')
    c.text(60, 96, '同一锅汤，三种做法，几天后会怎样？', 'serif', 40, INK)
    days = fade(t, 8, 18)
    cases = [(380, '煮过 + 趁热密封', '加热杀菌，盖子挡住新来的', 0.0, True, False),
             (960, '煮过 + 敞口', '空气里的微生物又落进去', 1.0, False, True),
             (1540, '没煮 + 密封', '里面的微生物照样繁殖', 1.0, True, False)]
    for k, (cx, lab, sub, grow, lid, fall) in enumerate(cases):
        top = 260
        cl = grow * days * 0.6
        jar(c, cx, top, cl, lid, lab, sub)
        heat = fade(t, 2, 4) * (1 - fade(t, 6, 7)) if k < 2 else 0
        n = int(8 + grow * days * 50) if k else max(0, int(8 * (1 - fade(t, 3, 6))))
        if k == 1 and t < 7: n = max(0, int(8 * (1 - fade(t, 3, 6))))
        for j in range(min(n, len(SPOTS))):
            dx, dy = SPOTS[j]
            microbe(c, cx + dx, top + 210 + dy, 8)
        if heat > 0:
            for j in range(5):
                c.arrow(cx - 100 + j * 50, top + 455, cx - 100 + j * 50, top + 392, mix(BG, NRED, heat), 4, 12)
        if fall and t > 7:
            for j in range(6):
                ph = (t * 0.7 + j / 6) % 1
                microbe(c, cx - 90 + j * 36, top - 120 + ph * 200, 6, GERM, 0.9)
    c.text(960, 900, f'第 {int(days * 5)} 天', 'mono', 30, mix(BG, COPPER, fade(t, 8, 9)), 'mm')
    caps(c, t, [(0, 7, '把汤煮开，热量杀死了里面的大多数微生物'),
                (7.2, 13, '敞着口，空气里的微生物又落进去；没煮过的，里面的微生物一直在'),
                (13.2, 22, '只有「先加热、再密封」的那一罐，能放很久不坏')], y=1000)

def flask(c, cx, base, broke, cloud):
    # body
    c.ellipse(cx, base, 200, 160, fill=mix(BG, GLASS, 0.25), outline=GLASS, width=4)
    c.ellipse(cx, base + 30, 180, 120, fill=mix(mix(BG, BROTH, 0.55), (120, 110, 80), cloud))
    # swan neck path
    pts = [(cx + 60, base - 140), (cx + 120, base - 260), (cx + 230, base - 300), (cx + 320, base - 230),
           (cx + 380, base - 170), (cx + 450, base - 230), (cx + 520, base - 380)]
    if broke:
        pts = pts[:2]
        c.line([(cx + 120, base - 260), (cx + 130, base - 300)], GLASS, 14)
    c.line(pts, GLASS, 18)
    c.line(pts, mix(BG, GLASS, 0.2), 8)
    return pts

RF = random.Random(1859)
DUST = [(RF.uniform(0, 1), RF.uniform(0, 1)) for _ in range(14)]

def e37_swan(c, t, i):
    corner_tag(c, '第 37 集 · 鹅颈瓶')
    c.text(60, 96, '瓶口一直开着，汤为什么不坏？', 'serif', 40, INK)
    broke = t > 12
    cloud = fade(t, 14, 20) * 0.8
    cx, base = 700, 760
    pts = flask(c, cx, base, broke, cloud)
    # dust motes
    for k, (u, v) in enumerate(DUST):
        ph = (t * 0.25 + u) % 1
        if not broke:
            # fall into the open end, slide to the low bend and stop
            ex, ey = cx + 520, base - 380
            bx, by = cx + 380, base - 175
            if ph < 0.5:
                x, y = ex + (v - 0.5) * 80, ey - 200 + ph * 400
            else:
                q = min(1, (ph - 0.5) * 3)
                x, y = ex + (bx - ex) * q, ey + (by - ey) * q
            c.ellipse(x, y, 6, 6, fill=mix(BG, MUTED, 0.9))
        else:
            x = cx + 100 + (v - 0.5) * 120
            y = base - 520 + ph * 560
            c.ellipse(x, y, 6, 6, fill=mix(BG, MUTED, 0.9))
    if broke:
        for j in range(int(40 * cloud)):
            dx, dy = SPOTS[j]
            microbe(c, cx + dx * 1.3, base + 30 + dy * 0.6, 7)
    if not broke:
        c.text(cx + 400, base - 120, '灰尘和微生物卡在弯管最低处', 'sans', 26, SPARK, 'lm')
    else:
        c.text(cx + 220, base - 300, '弯管折断：灰尘直接落进去', 'sans', 26, NRED, 'lm')
    a = fade(t, 17, 18)
    c.rect(1240, 820, 1860, 960, fill=mix(BG, SHEET, a), r=12)
    c.text(1550, 860, '1810 年 阿佩尔：先加热、再密封', 'sans', 26, mix(BG, INK, a), 'mm')
    c.text(1550, 910, '1860 年前后 巴斯德：坏，是因为微生物', 'sans', 26, mix(BG, COPPER, a), 'mm')
    caps(c, t, [(0, 6, '巴斯德把瓶颈拉成弯弯的「鹅颈」，煮过的汤和外面的空气相通'),
                (6.2, 12, '灰尘和微生物落进瓶口，却卡在弯管最低处，进不到汤里，汤一直清亮'),
                (12.2, 22, '把弯管折断，灰尘直接落进去，汤很快就浑了：让食物变坏的，是外面来的微生物')], y=1030)

# ---------------------------------------------------------------- E31 口服补液
RO = random.Random(31)
WM = [(RO.uniform(0, 1), RO.uniform(0, 1), RO.uniform(0, 1)) for _ in range(70)]

def e31_osmosis(c, t, i):
    corner_tag(c, '第 31 集 · 渗透')
    c.text(60, 96, '水往哪边走？', 'serif', 40, INK)
    x0, x1, y0, y1 = 360, 1560, 260, 860
    mid = 960
    shift = fade(t, 4, 14)
    hl = 380 + 90 * shift      # left water surface (y)
    hr = 380 - 90 * shift
    c.rect(x0, hl, mid, y1, fill=mix(BG, FIELD, 0.3))
    c.rect(mid, hr, x1, y1, fill=mix(BG, FIELD, 0.3))
    c.rect(x0 - 10, y0, x0, y1 + 10, fill=GLASS); c.rect(x1, y0, x1 + 10, y1 + 10, fill=GLASS); c.rect(x0 - 10, y1, x1 + 10, y1 + 10, fill=GLASS)
    for yy in range(y0, y1, 24):
        c.line([(mid, yy), (mid, yy + 12)], SPARK, 5)
    c.text(mid, y0 - 40, '只让水通过的膜', 'sans', 24, SPARK, 'mm')
    c.text((x0 + mid) / 2, y1 + 50, '清水', 'bold', 30, INK, 'mm')
    c.text((mid + x1) / 2, y1 + 50, '浓盐水', 'bold', 30, INK, 'mm')
    for k in range(18):
        u, v, _ = WM[k]
        c.ellipse(mid + 40 + u * 540, hr + 40 + v * (y1 - hr - 80), 13, 13, fill=SALT)
    for k, (u, v, p) in enumerate(WM[18:]):
        ph = (t * 0.35 + p) % 1
        if k % 3 == 0 and shift < 0.98:
            x = mid - 120 + ph * 240
            y = 500 + v * 300
        else:
            x = (x0 + 20 + u * 560) if k % 2 else (mid + 20 + u * 560)
            y = (hl if x < mid else hr) + 30 + v * (y1 - (hl if x < mid else hr) - 60)
        c.ellipse(x, y, 7, 7, fill=FIELD)
    if shift > 0.5:
        c.arrow(mid - 80, 640, mid + 80, 640, mix(BG, FIELD, fade(t, 7, 8)), 6, 18)
    caps(c, t, [(0, 4, '中间是一层只让水通过的膜：左边清水，右边浓盐水'),
                (4.2, 14, '水分子会往「溶解的东西更多」的一边跑：这叫渗透'),
                (14.2, 22, '身体吸水也离不开它：盐先进去，水才会跟着进去')], y=1010)

def cell_row(c, y, n=5):
    for k in range(n):
        x = 300 + k * 280
        c.rect(x, y, x + 260, y + 220, fill=mix(BG, (210, 150, 140), 0.45), outline=mix(BG, (210, 150, 140), 0.8), width=3, r=18)
    return [300 + k * 280 for k in range(n)]

def e31_cotransport(c, t, i):
    corner_tag(c, '第 31 集 · 盐和糖一起')
    c.text(60, 96, '为什么光喝白水补不回来？', 'serif', 40, INK)
    c.rect(0, 200, 1920, 420, fill=mix(BG, FIELD, 0.12))
    c.text(80, 240, '肠道里', 'sans', 26, MUTED, 'lm')
    xs = cell_row(c, 430)
    c.text(80, 900, '身体里（血液）', 'sans', 26, MUTED, 'lm')
    chol = fade(t, 0, 1) * (1 - fade(t, 8, 9))
    ors = fade(t, 9, 10)
    # cholera: water & salt pushed out
    if chol > 0:
        for k, x in enumerate(xs):
            for j in range(3):
                ph = (t * 0.6 + j / 3 + k * 0.2) % 1
                y = 640 - ph * 380
                c.ellipse(x + 80 + j * 40, y, 8, 8, fill=mix(BG, FIELD, chol))
        c.text(960, 720, '霍乱毒素：盐和水被大量排进肠道', 'bold', 30, mix(BG, NRED, chol), 'mm')
    if ors > 0:
        for k, x in enumerate(xs):
            tx = x + 130
            c.rect(tx - 22, 422, tx + 22, 450, fill=mix(BG, COPPER, ors), r=6)
            ph = (t * 0.45 + k * 0.17) % 1
            y = 300 + ph * 480
            c.ellipse(tx - 26, y, 11, 11, fill=mix(BG, SALT, ors))
            c.ellipse(tx, y - 4, 13, 13, fill=mix(BG, SUGAR, ors))
            c.ellipse(tx + 26, y, 11, 11, fill=mix(BG, SALT, ors))
            for j in range(3):
                ph2 = (ph - 0.12 - j * 0.06) % 1
                c.ellipse(tx - 60 + j * 20, 300 + ph2 * 480, 7, 7, fill=mix(BG, FIELD, ors))
        c.text(1650, 260, '白点：钠（盐）', 'sans', 24, SALT, 'lm')
        c.text(1650, 300, '黄点：葡萄糖', 'sans', 24, SUGAR, 'lm')
        c.text(1650, 340, '蓝点：水跟着进去', 'sans', 24, FIELD, 'lm')
        c.text(960, 790, '橙色「门」：钠和葡萄糖必须一起进', 'bold', 28, mix(BG, COPPER, ors), 'mm')
    a = fade(t, 16, 17)
    c.rect(300, 840, 1620, 960, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 875, '1971 年难民营：口服补液为主的营地，霍乱病死率约 3%', 'sans', 26, mix(BG, INK, a), 'mm')
    c.text(960, 920, '同期只靠静脉输液的营地约 20%–30%（世卫组织公报）', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 8.6, '霍乱让肠道把盐和水大量排出去，光喝白水，水很难被吸收回来'),
                (9, 16, '可肠壁上有一种「门」：钠和葡萄糖一起进，水就跟着进去，霍乱时它照样工作'),
                (16.2, 22, '配方请用药店的口服补液盐、照说明书；腹泻严重要就医')], y=1035)

# ---------------------------------------------------------------- E35 种痘
def curve(c, x0, y1, pts, col, w=6):
    c.line([(x0 + x, y1 - y) for x, y in pts], col, w)

def e35_memory(c, t, i):
    corner_tag(c, '第 35 集 · 免疫记忆')
    c.text(60, 96, '为什么第二次碰到同一种病菌，身体反应快得多？', 'serif', 40, INK)
    x0, y1, W, H = 220, 820, 1500, 520
    c.line([(x0, y1), (x0 + W, y1)], MUTED, 3); c.line([(x0, y1), (x0, y1 - H)], MUTED, 3)
    c.text(x0 - 20, y1 - H, '抗体（示意）', 'sans', 24, MUTED, 'rm')
    c.text(x0 + W, y1 + 40, '时间', 'sans', 24, MUTED, 'rm')
    p1 = fade(t, 2, 8)
    p2 = fade(t, 10, 15)
    def bump(xc, w, h, prog, x_from):
        pts = []
        for k in range(0, 101):
            x = x_from + k * 6
            if (x - x_from) > prog * 600: break
            y = h * math.exp(-((x - xc) / w) ** 2) * (1 - math.exp(-(x - x_from) / 25)) if x > x_from else 0
            pts.append((x, y))
        return pts
    pts = bump(260, 90, 140, p1, 40)
    if len(pts) > 1: curve(c, x0, y1, pts, FIELD)
    pts = bump(960, 120, 420, p2, 820)
    if len(pts) > 1: curve(c, x0, y1, pts, COPPER)
    for xx, lab, a in [(40, '第一次感染', fade(t, 1, 2)), (820, '第二次碰到', fade(t, 9, 10))]:
        c.arrow(x0 + xx, y1 - H + 40, x0 + xx, y1 - 10, mix(BG, NRED, a), 4, 14)
        c.text(x0 + xx + 10, y1 - H + 30, lab, 'bold', 26, mix(BG, NRED, a), 'lm')
    c.text(x0 + 300, y1 - 180, '慢、少：要一两周', 'sans', 26, mix(BG, FIELD, fade(t, 7, 8)), 'lm')
    c.text(x0 + 1100, y1 - 380, '快、多：记忆细胞认得它', 'sans', 26, mix(BG, COPPER, fade(t, 14, 15)), 'lm')
    caps(c, t, [(0, 8, '第一次碰到某种病原，免疫系统要花一两周才「学会」对付它'),
                (8.2, 15, '它会留下记忆细胞；第二次再来，反应又快又猛，往往还没发病就被清掉了'),
                (15.2, 22, '种痘的思路：先用一次轻的，换来这份记忆')], y=1010)

def virus(c, x, y, r, col, spikes, a=1.0):
    c.ellipse(x, y, r, r, fill=mix(BG, col, 0.6 * a))
    for k in range(10):
        ang = 2 * math.pi * k / 10
        sx, sy = x + r * math.cos(ang), y + r * math.sin(ang)
        ex, ey = x + (r + 22) * math.cos(ang), y + (r + 22) * math.sin(ang)
        c.line([(sx, sy), (ex, ey)], mix(BG, col, a), 4)
        if spikes == 'tri':
            c.poly([(ex, ey), (ex - 8 * math.sin(ang) - 6 * math.cos(ang), ey + 8 * math.cos(ang) - 6 * math.sin(ang)),
                    (ex + 8 * math.sin(ang) - 6 * math.cos(ang), ey - 8 * math.cos(ang) - 6 * math.sin(ang))], mix(BG, col, a))
        else:
            c.ellipse(ex, ey, 7, 7, fill=mix(BG, col, a))

def e35_cowpox(c, t, i):
    corner_tag(c, '第 35 集 · 从人痘到牛痘')
    c.text(60, 96, '一场牛的病，为什么能防住天花？', 'serif', 40, INK)
    a1 = fade(t, 0.5, 1.5); a2 = fade(t, 2.5, 3.5)
    virus(c, 520, 380, 90, GREEN, 'tri', a1)
    c.text(520, 540, '牛痘病毒：症状轻', 'bold', 28, mix(BG, GREEN, a1), 'mm')
    virus(c, 1400, 380, 90, NRED, 'tri', a2)
    c.text(1400, 540, '天花病毒：致命', 'bold', 28, mix(BG, NRED, a2), 'mm')
    a3 = fade(t, 5, 6)
    c.text(960, 380, '表面的「样子」很像', 'sans', 28, mix(BG, SPARK, a3), 'mm')
    c.arrow(760, 420, 640, 420, mix(BG, SPARK, a3), 4, 14); c.arrow(1160, 420, 1280, 420, mix(BG, SPARK, a3), 4, 14)
    b = fade(t, 10, 11)
    tl = [('1567–1572', '人痘（常见说法：明隆庆年间）'), ('1721', '人痘法传入英国'), ('1796', '琴纳接种牛痘'), ('1980', '世卫组织宣布天花根除')]
    for k, (yr, s) in enumerate(tl):
        x = 200 + k * 420
        c.ellipse(x, 720, 10, 10, fill=mix(BG, COPPER, b))
        c.text(x + 20, 720, yr, 'mono', 26, mix(BG, COPPER, b), 'lm')
        c.text(x + 20, 765, s, 'sans', 22, mix(BG, INK, b), 'lm')
    if b > 0: c.line([(200, 720), (1460, 720)], mix(BG, LINE, b), 2)
    a4 = fade(t, 16, 17)
    c.text(960, 880, '人痘用的是真天花，有风险；牛痘轻得多，却同样能让身体记住', 'sans', 28, mix(BG, INK, a4), 'mm')
    caps(c, t, [(0, 5, '牛痘和天花是亲戚，表面的样子很像'),
                (5.2, 10, '免疫系统记住了牛痘，再见到天花，也认得出来'),
                (10.2, 16, '从人痘到牛痘，再到 1980 年天花被宣布根除'),
                (16.2, 22, '人类第一次靠自己的办法，消灭了一种传染病')], y=1010)

CLIPS = {
 'E37_密封': (e37_seal, 22), 'E37_鹅颈瓶': (e37_swan, 22),
 'E37_片头': (titles.opening(SER4, VOL4, S4A, 2, '1810 年 · 巴黎 · 阿佩尔'), 7),
 'E37_片尾': (titles.closing(SER4, VOL4, S4A, 2, '下集：光喝水补不回来，为什么加点盐和糖就行？'), 7),
 'E31_渗透': (e31_osmosis, 22), 'E31_协同转运': (e31_cotransport, 22),
 'E31_片头': (titles.opening(SER4, VOL4, S4A, 3, '1971 年 · 难民营 · 霍乱'), 7),
 'E31_片尾': (titles.closing(SER4, VOL4, S4A, 3, '下集：用一场小病，换来对大病的免疫'), 7),
 'E35_免疫记忆': (e35_memory, 22), 'E35_牛痘': (e35_cowpox, 22),
 'E35_片头': (titles.opening(SER4, VOL4, S4A, 4, '1796 年 · 英国 · 琴纳'), 7),
 'E35_片尾': (titles.closing(SER4, VOL4, S4A, 4, '下集：关紧门窗烧炭，为什么危险？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
