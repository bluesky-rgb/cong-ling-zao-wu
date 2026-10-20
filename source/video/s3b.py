"""第三季第二批：B5 都江堰、E27 陶罐滴灌、E29 轮作固氮 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s3a import S3A, SER3, VOL3, WATER

SAND = (200, 170, 110)
SOIL = (96, 74, 56)
SOILW = (70, 60, 56)
CLAYP = (176, 110, 80)
GREEN = (110, 180, 110)

# ---------------------------------------------------------------- B5 都江堰
RD = random.Random(5)
PARTS = [(RD.random(), RD.random()) for _ in range(140)]

def river_path(u, side):
    """u in [0,1]; returns point along main river (u<0.45) then split into inner (side=-1) / outer (side=+1)."""
    if u < 0.45:
        s = u / 0.45
        return 1000 + 100 * math.sin(s * 1.6), 290 + s * 250
    s = (u - 0.45) / 0.55
    x0, y0 = 1000 + 100 * math.sin(1.6), 540
    if side < 0:
        return x0 - s * 480, y0 + s * 330 + 30 * math.sin(s * 3)
    return x0 + s * 520, y0 + s * 330

def b5_split(c, t, i):
    corner_tag(c, 'B5 · 鱼嘴分水')
    c.text(60, 96, '一个「鱼嘴」，怎么做到旱时多给、涝时少给？', 'serif', 40, INK)
    flood = fade(t, 11, 13)
    inner_share = 0.6 * (1 - flood) + 0.4 * flood
    # banks
    for side, w in ((-1, 70), (1, 110)):
        pts = [river_path(k / 60, side) for k in range(61)]
        for (x, y) in pts:
            c.ellipse(x, y, w * (0.8 + 0.4 * flood), w * (0.8 + 0.4 * flood), fill=mix(BG, FIELD, 0.22))
    # fish mouth
    mx, my = river_path(0.45, 1)
    c.poly([(mx, my - 40), (mx + 70, my + 90), (mx - 60, my + 90)], (150, 140, 120))
    c.text(mx + 120, my - 10, '鱼嘴', 'bold', 30, INK, 'lm')
    # particles
    n = int(60 + 60 * flood)
    for k in range(n):
        u0, r = PARTS[k]
        u = (u0 + t * 0.12) % 1
        side = -1 if r < inner_share else 1
        x, y = river_path(u, side)
        jitter = (r - 0.5) * 60
        c.ellipse(x + jitter, y + jitter * 0.3, 7, 7, fill=mix(BG, FIELD, 0.95))
    x, y = river_path(1, -1); c.text(x - 60, y - 110, '内江 → 成都平原灌溉', 'bold', 28, INK, 'rm')
    x, y = river_path(1, 1); c.text(x + 40, y - 120, '外江 → 泄洪', 'bold', 28, INK, 'lm')
    # panel
    px = 80
    c.rect(px, 200, 560, 520, fill=SHEET, r=16)
    c.text(px + 30, 250, '枯水期' if flood < 0.5 else '丰水期', 'serif', 40, COPPER, 'lm')
    for k, (lab, v, col) in enumerate([('内江', inner_share, FIELD), ('外江', 1 - inner_share, MUTED)]):
        y = 340 + k * 80
        c.text(px + 30, y, lab, 'sans', 28, INK, 'lm')
        c.rect(px + 110, y - 18, px + 440, y + 18, fill=LINE, r=18)
        c.rect(px + 110, y - 18, px + 110 + 330 * v, y + 18, fill=col, r=18)
        c.text(px + 450, y, f'{v * 10:.0f} 成', 'mono', 24, INK, 'lm')
    c.text(px + 30, 480, '内江河床深而窄，外江宽而浅', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 5, '岷江冲出山口，被江心的「鱼嘴」一分为二'),
                (5.2, 11, '枯水期水位低：深而窄的内江分到约六成，保证灌溉'),
                (11.2, 18, '丰水期水位高：宽而浅的外江分走约六成，替成都平原泄洪'),
                (18.2, 24, '不用闸门，靠河床的深浅和宽窄，自动「四六分水」')])

def b5_sand(c, t, i):
    corner_tag(c, 'B5 · 弯道排沙')
    c.text(60, 96, '沙子为什么大多跑进了外江？', 'serif', 40, INK)
    # cross-section of a bend: left = convex (inner bank), right = concave (outer bank)
    x0, x1, ys, yb = 220, 1100, 360, 760
    pts = [(x0, ys)] + [(x0 + (x1 - x0) * k / 40, yb - 200 * (1 - k / 40) ** 2) for k in range(41)] + [(x1, ys)]
    c.poly([(x0, ys)] + pts[1:-1] + [(x1, ys)], mix(BG, FIELD, 0.35))
    c.line(pts[1:-1], SOIL, 8)
    c.text(x0 + 40, 330, '凸岸（弯道内侧）', 'sans', 24, MUTED, 'lm')
    c.text(x1 - 40, 330, '凹岸（弯道外侧）', 'sans', 24, MUTED, 'rm')
    # helical circulation arrows
    a = fade(t, 2, 4)
    if a > 0:
        cx, cy, rx, ry = 660, 540, 300, 120
        for k in range(8):
            ph = (t * 0.5 + k / 8) % 1
            ang = ph * 2 * math.pi
            x, y = cx + rx * math.cos(ang), cy - ry * math.sin(ang)
            x2, y2 = cx + rx * math.cos(ang + 0.25), cy - ry * math.sin(ang + 0.25)
            c.arrow(x, y, x2, y2, mix(BG, INK, a), 4, 12)
        c.text(cx, 400, '表层水冲向凹岸', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(cx - 160, 720, '底层水带着沙流向凸岸', 'sans', 24, mix(BG, SAND, a), 'mm')
    # sand grains moving along bottom toward convex bank
    for k in range(30):
        ph = (t * 0.25 + k / 30) % 1
        s = 0.9 - 0.8 * ph * fade(t, 4, 6)
        bx = x0 + (x1 - x0) * s; by = yb - 200 * (1 - s) ** 2 - 12
        c.ellipse(bx, by, 7, 7, fill=SAND)
    # top view inset
    b = fade(t, 12, 13)
    px = 1180
    if b <= 0:
        caps(c, t, [(0, 4, '河水转弯时，并不是整齐地往前流'), (4.2, 12, '表层的水甩向弯道外侧，底层的水带着沙子流向内侧：弯道环流')])
        return
    c.rect(px, 200, 1860, 860, fill=mix(BG, SHEET, b), r=16)
    c.text(px + 340, 250, '鱼嘴的位置正好卡在弯道上', 'bold', 28, mix(BG, INK, b), 'mm')
    for k, (lab, v, col) in enumerate([('进内江的沙', 0.2, SAND), ('进外江的沙', 0.8, SAND)]):
        y = 360 + k * 100
        c.text(px + 40, y, lab, 'sans', 28, mix(BG, INK, b), 'lm')
        c.rect(px + 230, y - 18, px + 620, y + 18, fill=mix(BG, LINE, b), r=18)
        c.rect(px + 230, y - 18, px + 230 + 390 * v * b, y + 18, fill=col, r=18)
        c.text(px + 600, y + 40, f'约 {int(v * 10)} 成', 'mono', 24, mix(BG, INK, b), 'rm')
    c.text(px + 40, 600, '内江在凹岸一侧：取表层清水', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(px + 40, 650, '外江在凸岸一侧：带走底沙', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(px + 40, 730, '再加上飞沙堰：洪水时', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(px + 40, 775, '把内江多余的水和沙甩回外江', 'sans', 26, mix(BG, COPPER, b), 'lm')
    caps(c, t, [(0, 4, '河水转弯时，并不是整齐地往前流'),
                (4.2, 12, '表层的水甩向弯道外侧，底层的水带着沙子流向内侧：弯道环流'),
                (12.2, 24, '鱼嘴就修在弯道上：清水多进内江，沙子大多去了外江 ——「二八排沙」')])

# ---------------------------------------------------------------- E27 陶罐滴灌
RP = random.Random(27)
DROPS = [(RP.uniform(0, 2 * math.pi), RP.uniform(0, 1)) for _ in range(40)]

def e27_seep(c, t, i):
    corner_tag(c, '第 27 集 · 陶罐渗水')
    c.text(60, 96, '埋一个罐子，为什么能省很多水？', 'serif', 40, INK)
    G = 360
    for side, x0 in ((0, 80), (1, 1000)):
        c.rect(x0, G, x0 + 840, 980, fill=SOIL)
        c.rect(x0, G - 6, x0 + 840, G, fill=(120, 96, 70))
        cx = x0 + 420
        # plant
        c.line([(cx + 260, G), (cx + 260, G - 120)], GREEN, 8)
        for k in range(3):
            c.ellipse(cx + 260 + (-1) ** k * 36, G - 60 - k * 26, 30, 14, fill=GREEN)
        if side == 0:
            c.text(cx - 100, 190, '表面浇水', 'bold', 34, INK, 'mm')
            a = fade(t, 1, 3)
            for k in range(8):
                ph = (t * 0.6 + k / 8) % 1
                c.ellipse(cx - 200 + k * 50, G + 40 + ph * 500, 7, 7, fill=mix(BG, FIELD, a * (1 - ph)))
                c.arrow(cx - 200 + k * 50, G - 20 - ph * 60, cx - 200 + k * 50, G - 50 - ph * 60, mix(BG, (200, 200, 210), a * (1 - ph)), 3, 10)
            c.text(cx, G + 520, '大部分被晒干，或渗到根够不着的深处', 'sans', 26, mix(SOIL, (255, 160, 140), fade(t, 4, 5)), 'mm')
            wet = fade(t, 1, 4) * (1 - 0.6 * fade(t, 10, 18))
            c.ellipse(cx, G + 30, 260, 50 * wet + 1, fill=mix(SOIL, SOILW, wet))
        else:
            c.text(cx - 100, 190, '埋一个素烧陶罐', 'bold', 34, INK, 'mm')
            halo = fade(t, 4, 14)
            c.ellipse(cx, G + 230, 140 + 140 * halo, 160 + 120 * halo, fill=mix(SOIL, SOILW, 0.8))
            # pot
            c.poly([(cx - 70, G), (cx + 70, G), (cx + 110, G + 200), (cx + 60, G + 380), (cx - 60, G + 380), (cx - 110, G + 200)], CLAYP)
            lvl = G + 40 + 200 * fade(t, 2, 22)
            c.poly([(cx - 66 - (lvl - G) * 0.4 if lvl < G + 200 else cx - 100, lvl), (cx + 66 + (lvl - G) * 0.4 if lvl < G + 200 else cx + 100, lvl), (cx + 55, G + 372), (cx - 55, G + 372)], mix(BG, FIELD, 0.8))
            for k, (ang, ph0) in enumerate(DROPS):
                ph = (t * 0.25 + ph0) % 1
                r = 100 + 180 * ph
                x = cx + r * math.cos(ang); y = G + 220 + 0.8 * r * math.sin(ang)
                if y > G + 10:
                    c.ellipse(x, y, 5, 5, fill=mix(BG, FIELD, 0.9 * (1 - ph)))
            # roots growing toward pot
            g = fade(t, 10, 18)
            for k in range(5):
                rx0, ry0 = cx + 260, G
                ex, ey = cx + 260 - 120 * g - k * 10, G + 80 + k * 50 * g
                c.line([(rx0, ry0), ((rx0 + ex) / 2 + 20, (ry0 + ey) / 2), (ex, ey)], (220, 200, 160), 3)
    caps(c, t, [(0, 6, '表面浇水：水一浇下去，大半被太阳晒干，或者渗到根够不着的深处'),
                (6.2, 14, '埋一个没上釉的陶罐，灌满水：水从陶壁的小孔里一点点渗出来'),
                (14.2, 22, '湿润的只有罐子周围，根就往罐子边上长 —— 水都用在了根上')])

def e27_self(c, t, i):
    corner_tag(c, '第 27 集 · 自动调节')
    c.text(60, 96, '土越干，它渗得越快', 'serif', 40, INK)
    states = [('干土', 1.0, 0, 8), ('湿土', 0.25, 8, 16)]
    st = 0 if t < 8 else 1
    name, rate, *_ = states[st]
    cx, cy = 560, 560
    c.rect(160, 260, 960, 900, fill=mix(SOIL, SOILW, 0.2 if st == 0 else 0.85))
    c.poly([(cx - 70, 260), (cx + 70, 260), (cx + 110, 460), (cx + 60, 640), (cx - 60, 640), (cx - 110, 460)], CLAYP)
    for k, (ang, ph0) in enumerate(DROPS[: int(40 * rate)]):
        ph = (t * 0.5 + ph0) % 1
        r = 100 + 200 * ph
        x = cx + r * math.cos(ang); y = 470 + 0.8 * r * math.sin(ang)
        if 270 < y < 890:
            c.ellipse(x, y, 6, 6, fill=mix(BG, FIELD, 0.9 * (1 - ph)))
    c.text(cx, 950, f'现在：{name}', 'serif', 36, COPPER, 'mm')
    # graph
    gx0, gx1, gy0, gy1 = 1100, 1800, 280, 800
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2); c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text(gx1, gy1 + 34, '土壤越干 →', 'sans', 24, MUTED, 'rm')
    c.text(gx0, gy0 - 30, '渗水速度（示意）', 'sans', 24, MUTED, 'lm')
    pts = [(gx0 + k / 40 * (gx1 - gx0), gy1 - (0.1 + 0.85 * (k / 40) ** 1.3) * (gy1 - gy0)) for k in range(41)]
    c.line(pts, FIELD, 6)
    mark = 0.95 if st == 0 else 0.3
    mx_ = gx0 + mark * (gx1 - gx0); my_ = gy1 - (0.1 + 0.85 * mark ** 1.3) * (gy1 - gy0)
    c.ellipse(mx_, my_, 14, 14, fill=COPPER)
    caps(c, t, [(0, 8, '土很干时，土把水「吸」出陶壁的力量大，渗得快'),
                (8.2, 16, '土湿了，吸力变小，渗水就慢下来'),
                (16.2, 20, '不用人看着：植物要多少，罐子就给多少')])

# ---------------------------------------------------------------- E29 轮作固氮
def e29_nodule(c, t, i):
    corner_tag(c, '第 29 集 · 根瘤')
    c.text(60, 96, '豆子的根上，住着一群「造肥料」的细菌', 'serif', 40, INK)
    G = 340
    c.rect(0, G, 900, 1080, fill=SOIL)
    # plant
    c.line([(420, G), (420, G - 180)], GREEN, 10)
    for k in range(4):
        c.ellipse(420 + (-1) ** k * 60, G - 80 - k * 30, 50, 22, fill=GREEN)
    # roots with nodules
    roots = [[(420, G), (380, 500), (300, 680), (260, 860)], [(420, G), (460, 520), (560, 700), (620, 900)], [(420, G), (420, 600), (430, 950)]]
    for r in roots: c.line(r, (220, 200, 160), 6)
    nods = [(352, 560), (300, 690), (470, 560), (560, 700), (422, 720), (430, 860)]
    for (x, y) in nods:
        c.ellipse(x, y, 20, 18, fill=(214, 150, 150))
    z = fade(t, 4, 6)
    if z > 0:
        c.line([(560, 700), (1000, 400)], mix(BG, MUTED, z), 2)
        c.line([(560, 700), (1000, 880)], mix(BG, MUTED, z), 2)
        c.ellipse(1400, 640, 400 * z, 300 * z, fill=mix(BG, (200, 120, 130), 0.5), outline=mix(BG, (214, 150, 150), z), width=4)
        if z > 0.9:
            c.text(1400, 360, '根瘤里面（放大）', 'bold', 28, INK, 'mm')
            for k in range(14):
                x = 1220 + (k % 5) * 90; y = 520 + (k // 5) * 90
                c.rect(x - 22, y - 10, x + 22, y + 10, fill=(240, 220, 160), r=10)
            # N2 → NH3
            f = fade(t, 8, 16)
            for k in range(4):
                ph = (t * 0.4 + k / 4) % 1
                x = 1000 + ph * 220; y = 470 + k * 70
                if ph < 0.8:
                    c.ellipse(x - 8, y, 9, 9, fill=FIELD); c.ellipse(x + 8, y, 9, 9, fill=FIELD)
            c.text(1050, 420, '空气里的氮气 N≡N', 'sans', 22, FIELD, 'lm')
            for k in range(3):
                ph = (t * 0.4 + k / 3) % 1
                x = 1600 + ph * 200; y = 600 + k * 70
                c.ellipse(x, y, 11, 11, fill=SPARK)
                for j in range(3):
                    c.ellipse(x + 16 * math.cos(j * 2.1), y + 16 * math.sin(j * 2.1), 5, 5, fill=INK)
            c.text(1640, 840, '氨 → 植物能吸收的氮', 'sans', 22, SPARK, 'mm')
    caps(c, t, [(0, 4, '挖出一棵豆苗：根上长着一颗颗小疙瘩，叫根瘤'),
                (4.2, 9, '根瘤里住着根瘤菌'),
                (9.2, 16, '它们能把空气里的氮气拆开，变成植物能吸收的氨'),
                (16.2, 24, '豆子给细菌糖，细菌给豆子氮：一笔交换')])

def e29_rotate(c, t, i):
    corner_tag(c, '第 29 集 · 轮作')
    c.text(60, 96, '种过豆子的地，为什么更肥？', 'serif', 40, INK)
    years = ['第一季', '第二季', '第三季']
    rows = [('一直种谷子', ['谷', '谷', '谷'], [0.8, 0.55, 0.35]), ('谷子 → 绿豆（翻压）→ 谷子', ['谷', '豆', '谷'], [0.8, 0.95, 0.85])]
    for r, (lab, crops, nlev) in enumerate(rows):
        y = 300 + r * 300
        c.text(120, y - 70, lab, 'bold', 30, INK, 'lm')
        for k in range(3):
            a = fade(t, 1 + k * 3, 2 + k * 3)
            x = 220 + k * 420
            c.rect(x, y, x + 360, y + 150, fill=mix(BG, SOIL, a), r=10)
            col = GREEN if crops[k] == '豆' else (220, 190, 100)
            for j in range(6):
                c.line([(x + 40 + j * 55, y), (x + 40 + j * 55, y - 50 * a)], mix(BG, col, a), 5)
            c.text(x + 180, y + 40, crops[k], 'serif', 36, mix(BG, BG if False else INK, a), 'mm')
            c.text(x + 180, y + 100, '土里的氮', 'sans', 20, mix(BG, MUTED, a), 'mm')
            c.rect(x + 40, y + 120, x + 320, y + 136, fill=mix(BG, LINE, a), r=8)
            c.rect(x + 40, y + 120, x + 40 + 280 * nlev[k] * a, y + 136, fill=mix(BG, FIELD, a), r=8)
            if r == 0: c.text(x + 180, 200, years[k], 'sans', 24, mix(BG, MUTED, a), 'mm')
    b = fade(t, 11, 12)
    c.rect(220, 900, 1660, 1000, fill=mix(BG, SHEET, b), r=12)
    c.text(940, 935, '《齐民要术》：「凡美田之法，绿豆为上，小豆、胡麻次之」', 'serif', 30, mix(BG, COPPER, b), 'mm')
    c.text(940, 975, '五六月种下，七八月翻进土里，来年种谷「亩收十石」', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 10, '一直种谷子：每收一季，土里的氮就少一截（示意）'),
                (10.2, 20, '中间插一季绿豆，长到一半翻进土里：氮补回来了')], y=1050)

# ---------------------------------------------------------------- 片头片尾
SB3 = [('B5', '都江堰'), ('B12', '冰鉴藏冰'), ('B6', '赵州桥')]
CLIPS = {
 'B5_鱼嘴分水': (b5_split, 24), 'B5_弯道排沙': (b5_sand, 24),
 'B5_片头': (titles.opening(BSER, BVOL, SB3, 0, '战国 · 秦 · 李冰 · 两千多年仍在使用'), 7),
 'B5_片尾': (titles.closing(BSER, BVOL, SB3, 0, '下集：埋一个罐子，为什么能省水？'), 7),
 'E27_陶罐渗水': (e27_seep, 22), 'E27_自动调节': (e27_self, 20),
 'E27_片头': (titles.opening(SER3, VOL3, S3A, 3, '西汉《氾胜之书》· 埋瓮灌瓠'), 7),
 'E27_片尾': (titles.closing(SER3, VOL3, S3A, 3, '下集：种过豆子的地，为什么更肥？'), 7),
 'E29_根瘤': (e29_nodule, 24), 'E29_轮作': (e29_rotate, 20),
 'E29_片头': (titles.opening(SER3, VOL3, S3A, 4, '北魏《齐民要术》· 绿肥与轮作'), 7),
 'E29_片尾': (titles.closing(SER3, VOL3, S3A, 4, '下集：晒一瓶水，为什么能消毒？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
