"""第三十七季（第十五层：菜园与厨房）第一批：E192 温室、E193 无土栽培、E194 保鲜膜 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L

S37A = [('192', '温室'), ('193', '无土栽培'), ('194', '保鲜膜'), ('195', '真空包装'), ('196', '干燥剂'),
        ('197', '速冻'), ('198', '冻干'), ('199', '恒温器'), ('200', '红外测温枪'), ('201', '活性炭')]
SER37, VOL37 = '从零造物', '第三十七季 · 第十五层：菜园与厨房'
SUN = (255, 215, 110)
HEAT = (235, 120, 80)
PLANT = (110, 180, 100)
SOILC = (120, 90, 60)
FILM = (200, 225, 240)
NUTR = (240, 200, 90)
O2 = (150, 210, 250)


# ---------------------------------------------------------------- E192 温室
def e192_trap(c, t, i):
    corner_tag(c, '第 192 集 · 阳光进得来，热出不去')
    c.text(60, 96, '阳光穿过透明的膜照在黑底上，变成热；热空气想往上跑、往外散，被膜挡住关在里面', 'serif', 36, INK)
    for j, (lab, cover) in enumerate([('敞开的盒子', False), ('盖了透明袋的盒子', True)]):
        x0 = 160 + j * 880
        y0, y1 = 520, 860
        c.rect(x0, y0, x0 + 640, y1, fill=mix(BG, (170, 130, 90), 0.5), r=6)
        c.rect(x0 + 16, y1 - 40, x0 + 624, y1 - 16, fill=(30, 30, 30))
        if cover:
            c.line([(x0, y0), (x0 + 640, y0)], mix(BG, FILM, 0.9), 6)
        for k in range(4):
            ph = (t * 0.8 + k * 0.25) % 1
            sx = x0 + 120 + k * 130
            c.line([(sx - 120, 240), (sx - 120 + 200 * min(1, ph * 1.5), 240 + 360 * min(1, ph * 1.5))], mix(BG, SUN, 0.9), 4)
        r = random.Random(j)
        for k in range(14):
            ph = (t * 0.5 + r.random()) % 1
            x = x0 + 60 + r.random() * 520
            y = y1 - 50 - ph * 380
            if cover and y < y0 + 10:
                y = y0 + 10 + (ph * 40) % 30
            if y < 200: continue
            c.ellipse(x, y, 8, 8, fill=mix(BG, HEAT, 0.8))
        T = 20 + (18 if cover else 6) * min(1.0, t / 14)
        c.text(x0 + 320, y0 + 140, f'{T:.0f} ℃', 'mono', 40, HEAT, 'mm')
        c.text(x0 + 320, 920, lab, 'bold', 26, INK, 'mm')
    c.ellipse(1800, 200, 50, 50, fill=SUN)
    c.text(1640, 200, '太阳（绝不直视）', 'sans', 20, NRED, 'rm')
    caps(c, t, [(0, 7, '阳光几乎全部穿过透明的玻璃或塑料，照到黑色的底上，被吸收变成热'),
                (7.2, 14, '敞开的盒子，热空气一边受热一边往上跑走了'),
                (14.2, 22, '盖上一层膜，热空气被关在里面，越积越多：温度高出一大截（示意，以实测为准）')], y=1010)


def e192_store(c, t, i):
    corner_tag(c, '第 192 集 · 水把白天的热存到晚上')
    c.text(60, 96, '太阳下山后，空盒子里的热很快散光；放了一瓶水的盒子，水慢慢把白天存的热放出来', 'serif', 36, INK)
    gx0, gx1, gy0, gy1 = 220, 1700, 860, 280
    c.rect(160, 230, 1780, 920, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    p = min(1.0, t / 16)
    for col, tau, lab in [(HEAT, 0.9, '盒里有一瓶水'), (MUTED, 0.3, '空盒子')]:
        pts = []
        for k in range(int(80 * p) + 1):
            s = k / 80
            T = 14 + 22 * math.exp(-s / tau * 1.0)
            pts.append((gx0 + (gx1 - gx0) * s, gy0 - (T - 10) * 18))
        if len(pts) > 1:
            c.line(pts, col, 4)
            c.text(pts[-1][0] + 10, pts[-1][1] - 20, lab, 'bold', 22, col, 'lm')
    c.text((gx0 + gx1) / 2, gy0 + 36, '太阳下山后 → 1 小时（示意）', 'sans', 22, MUTED, 'mm')
    c.text(gx0 + 20, gy1 - 20, '盒里温度', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '太阳一下山，两个盒子都开始变凉'),
                (7.2, 14, '空气存不住多少热，空盒子很快就跟外面一样冷了'),
                (14.2, 22, '水能存很多热，慢慢放出来：真温室里铺石头、放水桶，夜里就不那么冷（示意）')], y=1010)


# ---------------------------------------------------------------- E193 无土栽培
def e193_roots(c, t, i):
    corner_tag(c, '第 193 集 · 根要的是水、养分和空气')
    c.text(60, 96, '根吸的是溶在水里的养分，土只是扶着它、存着水；把养分直接溶进水里，再给水打点气就行', 'serif', 36, INK)
    cx = 760
    c.rect(cx - 300, 420, cx + 300, 900, fill=mix(BG, WATER_L, 0.35), outline=MUTED, width=4, r=12)
    c.rect(cx - 320, 400, cx + 320, 440, fill=mix(BG, (200, 200, 190), 0.9), r=6)
    c.line([(cx, 400), (cx, 250)], PLANT, 10)
    for s in (-1, 1):
        c.ellipse(cx + s * 70, 260, 70, 30, fill=PLANT)
    r = random.Random(3)
    roots = []
    for k in range(9):
        a = -0.8 + k * 0.2
        pts = [(cx, 440)]
        x, y = cx, 440
        for j in range(12):
            x += 22 * math.sin(a) + r.uniform(-6, 6)
            y += 34
            pts.append((x, y))
        roots.append(pts)
        c.line(pts, (235, 230, 210), 4)
    for k in range(18):
        ph = (t * 0.4 + k / 18) % 1
        rt = roots[k % 9]
        tx, ty = rt[8]
        sx, sy = tx + (60 if k % 2 else -60), ty + 40
        x = sx + (tx - sx) * ph
        y = sy + (ty - sy) * ph
        c.ellipse(x, y, 7, 7, fill=NUTR if k % 3 else O2)
    for k in range(6):
        y = 880 - ((t * 120 + k * 70) % 440)
        c.ellipse(cx + 240, y, 8, 8, outline=O2, width=2)
    c.text(cx + 340, 860, '打气：给根送氧气', 'sans', 22, O2, 'lm')
    c.rect(1240, 340, 1840, 700, fill=SHEET, r=14)
    c.ellipse(1290, 410, 10, 10, fill=NUTR)
    c.text(1320, 410, '溶在水里的养分（氮、磷、钾……）', 'sans', 22, INK, 'lm')
    c.ellipse(1290, 470, 10, 10, fill=O2)
    c.text(1320, 470, '溶在水里的氧气', 'sans', 22, INK, 'lm')
    c.text(1540, 560, '清水里没有养分', 'bold', 22, NRED, 'mm')
    c.text(1540, 610, '死水里氧气不够，根会烂', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '我们以为植物「吃」的是土，其实根只能吸溶在水里的东西'),
                (7.2, 14, '把植物需要的养分按比例溶进水里，根泡在里面就能直接喝到'),
                (14.2, 22, '根还要呼吸：真正的水培会给水打气，或者让水一直流动（示意）')], y=1010)


def e193_growth(c, t, i):
    corner_tag(c, '第 193 集 · 一周后，谁长得最好？')
    c.text(60, 96, '三杯豆苗：种在土里、泡清水、泡营养液。清水里的很快停下来，营养液里的长得和土里一样好甚至更快', 'serif', 34, INK)
    days = min(7.0, t / 2.6)
    vals = [('花盆土', 1.6, SOILC), ('清水', 0.8, WATER_L), ('营养液', 1.9, NUTR)]
    for k, (lab, rate, col) in enumerate(vals):
        x = 380 + k * 580
        c.rect(x - 110, 700, x + 110, 900, fill=mix(BG, col, 0.5), outline=MUTED, width=3, r=8)
        h = 30 + rate * days * 22 * (1 if k != 1 else max(0.4, 1 - days / 10))
        c.line([(x, 700), (x, 700 - h)], PLANT, 8)
        nl = int(1 + rate * days / 2.5)
        for j in range(nl):
            y = 700 - h * (0.4 + 0.6 * j / max(1, nl))
            s = -1 if j % 2 else 1
            c.ellipse(x + s * 34, y, 34, 14, fill=mix(BG, PLANT, 0.9 if k != 1 else 0.6))
        c.text(x, 940, lab, 'bold', 26, INK, 'mm')
        c.text(x, 660 - h, f'{h / 20:.1f} 厘米', 'mono', 22, SPARK, 'mm')
    c.text(1640, 260, f'第 {days:.0f} 天', 'mono', 34, INK, 'mm')
    c.text(1640, 310, '示意，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '头几天，三棵苗差不多：种子里自己带着的养分还没用完'),
                (7.2, 14, '种子的存货用完，清水里的苗停下来、叶子发黄'),
                (14.2, 22, '营养液里的苗一直长，和土里的差不多甚至更快：土不是必需的（示意）')], y=1010)


# ---------------------------------------------------------------- E194 保鲜膜
def e194_cling(c, t, i):
    corner_tag(c, '第 194 集 · 又薄又软，贴紧了就吸住')
    c.text(60, 96, '保鲜膜比头发还薄，又软，一按就贴进碗口每个细小的起伏；撕下来时还带上一点静电，吸得更牢', 'serif', 36, INK)
    p = min(1.0, t / 8)
    x0, x1, y = 200, 1100, 600
    r = random.Random(4)
    rough = [(x0 + k * 15, y + r.uniform(-6, 6)) for k in range(61)]
    c.poly(rough + [(x1, 900), (x0, 900)], mix(BG, (200, 200, 210), 0.85))
    c.text(650, 860, '放大的碗口（看着平，其实坑坑洼洼）', 'sans', 22, BG, 'mm')
    film = [(x, (y - 120) * (1 - p) + (yy - 5) * p) for x, yy in rough]
    c.line(film, FILM, 4)
    c.text(650, y - 160, '保鲜膜', 'bold', 24, FILM, 'mm')
    if p >= 1:
        for k in range(10):
            x = x0 + 40 + k * 90
            c.text(x, y - 30, '+', 'bold', 22, NRED, 'mm')
            c.text(x + 20, y + 40, '−', 'bold', 22, O2, 'mm')
    c.rect(1240, 300, 1840, 760, fill=SHEET, r=14)
    c.text(1540, 350, '粘住靠的是', 'bold', 26, INK, 'mm')
    c.text(1540, 420, '① 贴得极紧，中间几乎没空气', 'sans', 22, INK, 'mm')
    c.text(1540, 470, '② 分子之间的吸引', 'sans', 22, INK, 'mm')
    c.text(1540, 520, '③ 撕下时带上的静电', 'sans', 22, INK, 'mm')
    c.text(1540, 610, '碗口有油：贴不住', 'bold', 22, NRED, 'mm')
    c.text(1540, 660, '没有胶', 'bold', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '保鲜膜没有涂胶，它只是很薄很软'),
                (7.2, 14, '轻轻一按，它就贴进碗口每一个细小的起伏，中间几乎没有空气'),
                (14.2, 22, '从卷上撕下时，膜上还带了静电：贴得越紧，吸得越牢；有油就贴不住了（示意）')], y=1010)


def e194_stretch(c, t, i):
    corner_tag(c, '第 194 集 · 拉一拉，长链分子被理直')
    c.text(60, 96, '保鲜膜里是一根根缠在一起的长链分子：一拉，链子被慢慢理直，膜能拉长好几倍才断', 'serif', 36, INK)
    p = min(1.0, t / 14)
    stretch = 1 + 3 * p
    cx, cy = 960, 560
    W = 300 * stretch
    H = 300 / math.sqrt(stretch)
    c.rect(cx - W / 2, cy - H / 2, cx + W / 2, cy + H / 2, fill=mix(BG, FILM, 0.25), outline=FILM, width=2)
    r = random.Random(8)
    for k in range(10):
        y0 = cy - H / 2 + (k + 0.5) * H / 10
        pts = []
        ph = r.uniform(0, 6)
        for j in range(40):
            f = j / 39
            x = cx - W / 2 + 10 + f * (W - 20)
            amp = (H / 12) * (1 - p * 0.85)
            pts.append((x, y0 + amp * math.sin(f * 18 + ph)))
        c.line(pts, mix(BG, FILM, 0.9), 2)
    c.arrow(cx - W / 2 - 20, cy, cx - W / 2 - 120, cy, SPARK, 5, 16)
    c.arrow(cx + W / 2 + 20, cy, cx + W / 2 + 120, cy, SPARK, 5, 16)
    c.text(cx, cy + H / 2 + 60, f'拉长到原来的 {stretch:.1f} 倍（示意）', 'mono', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '保鲜膜是塑料，塑料是一根根很长很长的分子链缠成的'),
                (7.2, 14, '一拉，缠着的链子被一点点理顺、拉直，膜变长变薄'),
                (14.2, 22, '所以它能裹住形状不规则的碗和水果，紧紧绷着（示意，以实测为准）')], y=1010)


CLIPS = {
 'E192_关热': (e192_trap, 22), 'E192_存热': (e192_store, 22),
 'E192_片头': (titles.opening(SER37, VOL37, S37A, 0, '15 世纪已有加温温室'), 7),
 'E192_片尾': (titles.closing(SER37, VOL37, S37A, 0, '下集：没有一粒土，生菜为什么也能长？'), 7),
 'E193_根': (e193_roots, 22), 'E193_一周': (e193_growth, 22),
 'E193_片头': (titles.opening(SER37, VOL37, S37A, 1, '1929 年前后推广水培'), 7),
 'E193_片尾': (titles.closing(SER37, VOL37, S37A, 1, '下集：保鲜膜没有胶，怎么粘住碗口？'), 7),
 'E194_贴紧': (e194_cling, 22), 'E194_拉长': (e194_stretch, 22),
 'E194_片头': (titles.opening(SER37, VOL37, S37A, 2, '1949 年前后家用保鲜膜上市'), 7),
 'E194_片尾': (titles.closing(SER37, VOL37, S37A, 2, '下集：抽掉空气，食物为什么能放得更久？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
