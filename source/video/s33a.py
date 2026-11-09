"""第三十三季（第十三层：跑起来的机器）第一批：E172 液压刹车、E173 安全带、E174 安全气囊 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L

S33A = [('172', '液压刹车'), ('173', '安全带'), ('174', '安全气囊'), ('175', '差速器'), ('176', '雨刮器'),
        ('177', '螺旋桨'), ('178', '潜水艇'), ('179', '气垫船'), ('180', '降落伞'), ('181', '自动驾驶')]
SER33, VOL33 = '从零造物', '第三十三季 · 第十三层：跑起来的机器'
FLUID = (90, 150, 220)
BELT = (70, 80, 100)
BAGC = (235, 235, 225)
CARC = (90, 140, 210)


# ---------------------------------------------------------------- E172 液压刹车
def e172_pascal(c, t, i):
    corner_tag(c, '第 172 集 · 细活塞推一下，粗活塞力大几倍')
    c.text(60, 96, '两个活塞用一管水连着：细的那头按下去，压强传遍整管水；粗的那头面积大，受到的力就按面积比放大', 'serif', 38, INK)
    p = 0.5 - 0.5 * math.cos(t / 11 * math.pi) if t < 11 else 1
    x1, x2, base = 420, 1260, 800
    r1, r2 = 50, 110
    d1 = 160 * p
    d2 = d1 * (r1 / r2) ** 2
    c.rect(x1 - r1, 360, x1 + r1, base, outline=METAL, width=6)
    c.rect(x2 - r2, 360, x2 + r2, base, outline=METAL, width=6)
    c.rect(x1 - r1 + 4, 460 + d1, x1 + r1 - 4, base - 4, fill=mix(BG, FLUID, 0.7))
    c.rect(x2 - r2 + 4, 460 - d2, x2 + r2 - 4, base - 4, fill=mix(BG, FLUID, 0.7))
    c.rect(x1 + r1, base - 60, x2 - r2, base - 4, fill=mix(BG, FLUID, 0.7))
    c.rect(x1 - r1 + 4, 440 + d1, x1 + r1 - 4, 460 + d1, fill=METAL)
    c.rect(x2 - r2 + 4, 440 - d2, x2 + r2 - 4, 460 - d2, fill=METAL)
    c.arrow(x1, 300 + d1, x1, 430 + d1, SPARK, 6, 18)
    c.text(x1, 270 + d1, '手指 1 份力', 'bold', 24, SPARK, 'mm')
    c.arrow(x2, 430 - d2, x2, 260 - d2, GREEN, 10, 24)
    c.text(x2, 230 - d2, f'约 {(r2 / r1) ** 2:.1f} 份力', 'bold', 28, GREEN, 'mm')
    c.text(x1, base + 40, '细活塞', 'sans', 22, MUTED, 'mm')
    c.text(x2, base + 40, '粗活塞', 'sans', 22, MUTED, 'mm')
    c.rect(1460, 420, 1860, 640, fill=SHEET, r=14)
    c.text(1660, 470, '代价：行程', 'bold', 24, INK, 'mm')
    c.text(1660, 540, f'细的推 {d1 / 10:.0f}，粗的只动 {d2 / 10:.1f}', 'mono', 22, SPARK, 'mm')
    c.text(1660, 600, '（单位：毫米，示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '一细一粗两个活塞，中间连着一管水，水几乎压缩不了'),
                (7.2, 14, '按细活塞，水里每一处的压强都一样增加；粗活塞面积大，受到的力就大好几倍'),
                (14.2, 22, '省了力，费了行程：细的推下去一大截，粗的只往上动一点点（直径比约 2.2，示意）')], y=1010)


def e172_car(c, t, i):
    corner_tag(c, '第 172 集 · 一脚踩下去，四个轮子一起夹紧')
    c.text(60, 96, '刹车踏板推着一个细活塞，刹车油沿着油管分到四个轮子，每个轮子上的粗活塞推着刹车片夹住刹车盘', 'serif', 38, INK)
    press = 0.5 - 0.5 * math.cos(t / 7 * math.pi) if t < 14 else 1
    c.rect(560, 260, 1360, 860, outline=mix(BG, LINE, 0.6), width=3, r=60)
    mx, my = 960, 360
    c.rect(mx - 60, my - 30, mx + 60, my + 30, fill=METAL, r=6)
    c.text(mx, my - 60, '总泵（细活塞）', 'sans', 20, MUTED, 'mm')
    c.line([(mx, my + 30), (mx, my + 80 + 30 * press)], INK, 8)
    c.rect(mx - 40, my + 80 + 30 * press, mx + 40, my + 100 + 30 * press, fill=SPARK, r=4)
    c.text(mx + 70, my + 95 + 30 * press, '脚踩', 'bold', 20, SPARK, 'lm')
    wheels = [(560, 380), (1360, 380), (560, 760), (1360, 760)]
    for (wx, wy) in wheels:
        pts = [(mx, my), (mx, wy if wy < 500 else 560), (wx, wy if wy < 500 else 560), (wx, wy)]
        c.line(pts, mix(BG, FLUID, 0.4 + 0.5 * press), 6)
        c.ellipse(wx, wy, 90, 90, fill=(40, 40, 46))
        c.ellipse(wx, wy, 55, 55, fill=METAL)
        gap = 18 * (1 - press) + 2
        c.rect(wx - 75, wy - 55 - gap - 18, wx - 35, wy - 55 - gap, fill=NRED if press > 0.8 else mix(BG, NRED, 0.5), r=4)
    c.text(960, 940, '刹车片夹紧刹车盘，靠摩擦把车停下（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '脚踩刹车踏板，先经过一根杠杆放大，再推动总泵里的细活塞'),
                (7.2, 14, '刹车油把压强沿着油管同时送到四个轮子，四个轮子上的活塞一起往外推'),
                (14.2, 22, '活塞推着刹车片夹住跟轮子一起转的刹车盘：脚上的力被杠杆和液压放大了几十倍（示意）')], y=1010)


# ---------------------------------------------------------------- E173 安全带
def e173_lock(c, t, i):
    corner_tag(c, 'E173 · 慢拉放行，猛拽卡死'.replace('E173', '第 173 集'))
    c.text(60, 96, '卷收器里有一个棘轮和一个小摆锤：慢慢拉，摆锤不动，棘轮自由转；一猛拽或急刹，摆锤一晃，把棘爪顶进齿里', 'serif', 36, INK)
    jerk = t > 11
    cx, cy = 760, 560
    ang = t * (0.6 if not jerk else 0)
    if jerk and t < 11.6:
        ang = 11 * 0.6 + (t - 11) * 3
    elif jerk:
        ang = 11 * 0.6 + 0.6 * 3
    R = 180
    for k in range(16):
        a = ang + k * 2 * math.pi / 16
        p0 = (cx + R * math.cos(a), cy + R * math.sin(a))
        p1 = (cx + (R + 34) * math.cos(a + 0.12), cy + (R + 34) * math.sin(a + 0.12))
        p2 = (cx + R * math.cos(a + 0.39), cy + R * math.sin(a + 0.39))
        c.poly([p0, p1, p2], METAL)
    c.ellipse(cx, cy, R, R, fill=mix(BG, METAL, 0.5))
    c.ellipse(cx, cy, 40, 40, fill=INK)
    c.line([(cx + R, cy + 40), (cx + R + 500, cy + 40 + 0)], BELT, 30)
    c.text(cx + R + 300, cy + 90, '安全带', 'sans', 22, MUTED, 'mm')
    swing = 0 if not jerk else min(1, (t - 11) / 0.5)
    px, py = cx - 300, cy + 200
    c.line([(px, py - 160), (px + 120 * swing, py)], INK, 6)
    c.ellipse(px + 120 * swing, py, 26, 26, fill=SPARK)
    c.text(px, py + 60, '小摆锤', 'sans', 22, MUTED, 'mm')
    tip = (cx - R - 30 + 20 * swing, cy + 40 - 60 * swing)
    c.line([(px + 40, py - 120), tip], NRED, 10)
    c.text(cx - 360, cy - 120, '棘爪', 'sans', 22, NRED, 'mm')
    c.rect(1300, 260, 1840, 440, fill=SHEET, r=14)
    c.text(1570, 320, '猛拽：卡住了！' if jerk else '慢慢拉：顺畅放出', 'bold', 30, NRED if jerk else GREEN, 'mm')
    c.text(1570, 390, '（示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '安全带卷在一个带齿的卷轴上，旁边有一个棘爪，平时不碰齿'),
                (7.2, 14, '慢慢拉，摆锤垂着不动，卷轴自由地转，安全带一节节放出来'),
                (14.2, 22, '一猛拽或者车子急刹，摆锤因为惯性一晃，把棘爪顶进齿里：卷轴一下就锁死了（示意）')], y=1010)


def e173_marble(c, t, i):
    corner_tag(c, '第 173 集 · 车停了，里面的东西还往前冲')
    c.text(60, 96, '玩具车上放一个盒子，盒里一颗弹珠：车撞到书突然停下，弹珠却照样往前滚，撞上盒子的前壁', 'serif', 38, INK)
    stop_t = 6
    x0 = 300
    v = 140
    xc = x0 + v * min(t, stop_t)
    c.line([(100, 800), (1820, 800)], LINE, 3)
    c.rect(x0 + v * stop_t + 230, 640, x0 + v * stop_t + 290, 800, fill=mix(BG, (160, 120, 90), 0.8), r=6)
    c.text(x0 + v * stop_t + 260, 610, '书', 'sans', 22, MUTED, 'mm')
    c.rect(xc - 30, 700, xc + 230, 770, fill=CARC, r=10)
    c.ellipse(xc + 30, 790, 22, 22, fill=INK)
    c.ellipse(xc + 170, 790, 22, 22, fill=INK)
    c.rect(xc, 560, xc + 200, 700, outline=METAL, width=4)
    if t < stop_t:
        mx = xc + 60
    else:
        mx = min(xc + 178, xc + 60 + v * 1.2 * (t - stop_t))
    c.ellipse(mx, 676, 22, 22, fill=SPARK)
    if t > stop_t + 1:
        c.text(xc + 100, 520, '弹珠撞到前壁', 'bold', 24, NRED, 'mm')
    c.rect(1300, 260, 1840, 440, fill=SHEET, r=14)
    c.text(1570, 320, '没系安全带的人，就像这颗弹珠', 'bold', 22, INK, 'mm')
    c.text(1570, 390, '（示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '小车载着盒子和弹珠，一起往前开'),
                (7.2, 14, '车撞到书，一下子停了；弹珠没被拴住，照样带着原来的速度往前冲'),
                (14.2, 22, '急刹车时车里的人也是这样：安全带的任务，就是在这一刻把人拉住（示意）')], y=1010)


# ---------------------------------------------------------------- E174 安全气囊
def e174_impulse(c, t, i):
    corner_tag(c, '第 174 集 · 同样停下来，时间越长，力越小')
    c.text(60, 96, '同样的速度停下来，要消掉的动量一样多：撞方向盘几毫秒就停，力很大；撞进气囊花几十毫秒，力小得多', 'serif', 34, INK)
    x0, y0, x1, y1 = 260, 260, 1500, 860
    c.line([(x0, y1), (x1, y1)], LINE, 2)
    c.line([(x0, y0), (x0, y1)], LINE, 2)
    c.text((x0 + x1) / 2, y1 + 50, '时间（毫秒，示意）', 'sans', 20, MUTED, 'mm')
    c.text(x0, y0 - 30, '冲击力', 'sans', 20, MUTED, 'lm')
    for ms in (0, 20, 40, 60, 80):
        c.text(x0 + (x1 - x0) * ms / 80, y1 + 22, str(ms), 'mono', 16, MUTED, 'mm')
    grow = min(1, t / 12)
    for lab, T, col in (('撞方向盘', 6, NRED), ('撞进气囊', 50, GREEN)):
        H = 1.0 / T * 6 * (y1 - y0) * 0.95
        pts = []
        for j in range(101):
            ms = 80 * j / 100 * grow
            f = math.sin(math.pi * ms / T) if ms < T else 0
            pts.append((x0 + (x1 - x0) * ms / 80, y1 - H * max(0, f)))
        c.line(pts, col, 5)
        c.text(x0 + (x1 - x0) * T / 160 + 20, y1 - H - 20, lab, 'bold', 24, col, 'lm')
    c.rect(1560, 360, 1880, 620, fill=SHEET, r=14)
    c.text(1720, 410, '两块面积一样大', 'bold', 22, INK, 'mm')
    c.text(1720, 480, '= 要消掉的动量', 'sans', 20, MUTED, 'mm')
    c.text(1720, 560, '时间拉长约 8 倍', 'bold', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '车撞上东西，人要从同样的速度停下来：要消掉的「冲劲」是一样多的'),
                (7.2, 14, '撞在硬方向盘上，几毫秒就停住，力又尖又高'),
                (14.2, 22, '撞进正在放气的气囊，停下的时间拉长了很多倍，同样的冲劲摊开，力就矮了下去（示意）')], y=1010)


def e174_dough(c, t, i):
    corner_tag(c, '第 174 集 · 橡皮泥落在哪，压扁得最少？')
    c.text(60, 96, '同样的橡皮泥球从 50 厘米落下：落在桌面上一下被拍扁；落在吹满气的塑料袋上，袋子一软一托，几乎还是圆的', 'serif', 36, INK)
    cases = [('桌面', 0.35, False), ('一叠毛巾', 0.7, False), ('吹满气的袋子', 0.9, True), ('袋子扎个小孔', 0.85, True)]
    for k, (lab, keep, bag) in enumerate(cases):
        x = 300 + k * 430
        y = 760
        fall = min(1, t / 6)
        land = t > 6
        if bag:
            sq = 0.3 if land else 0
            c.ellipse(x, y - 60 + 30 * sq, 150, 70 * (1 - 0.4 * sq), fill=mix(BG, BAGC, 0.5))
        elif lab == '一叠毛巾':
            c.rect(x - 150, y - 60, x + 150, y, fill=mix(BG, (210, 180, 190), 0.8), r=8)
        else:
            c.rect(x - 150, y - 10, x + 150, y, fill=METAL)
        top = (y - 130 if bag else (y - 60 if lab == '一叠毛巾' else y - 10))
        if not land:
            by = 300 + (top - 40 - 300) * fall ** 2
            c.ellipse(x, by, 40, 40, fill=SPARK)
        else:
            h = 80 * keep
            w = 40 / keep ** 0.5
            c.ellipse(x, top - h / 2, w, h / 2, fill=SPARK)
            c.text(x, top - h - 40, f'剩 {keep * 100:.0f}% 高', 'mono', 22, INK, 'mm')
        c.text(x, 840, lab, 'bold', 24, INK, 'mm')
    c.text(960, 920, '高度比例为示意，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '三个一样的橡皮泥球，从同样 50 厘米高落下'),
                (7.2, 14, '落在桌面上，一瞬间停住，拍成了饼；落在毛巾上好一点'),
                (14.2, 22, '落在鼓鼓的塑料袋上，袋子一边被压一边托，橡皮泥慢慢停下，几乎没变形（以实测为准）')], y=1010)


CLIPS = {
 'E172_帕斯卡': (e172_pascal, 22), 'E172_刹车': (e172_car, 22),
 'E172_片头': (titles.opening(SER33, VOL33, S33A, 0, '1918 年发明汽车液压刹车'), 7),
 'E172_片尾': (titles.closing(SER33, VOL33, S33A, 0, '下集：安全带慢拉能拉出来，猛一拽为什么就卡死？'), 7),
 'E173_棘爪': (e173_lock, 22), 'E173_弹珠': (e173_marble, 22),
 'E173_片头': (titles.opening(SER33, VOL33, S33A, 1, '1959 年三点式安全带问世'), 7),
 'E173_片尾': (titles.closing(SER33, VOL33, S33A, 1, '下集：撞车时一个软软的气袋，为什么能救命？'), 7),
 'E174_冲量': (e174_impulse, 22), 'E174_压扁': (e174_dough, 22),
 'E174_片头': (titles.opening(SER33, VOL33, S33A, 2, '1970 年代汽车安全气囊开始使用'), 7),
 'E174_片尾': (titles.closing(SER33, VOL33, S33A, 2, '下集：汽车拐弯时，外侧轮子为什么要转得更快？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
