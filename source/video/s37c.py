"""第三十七季（第十五层：菜园与厨房）第三批：E198 冻干、E199 恒温器、E200 红外测温枪 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L
from s37a import S37A, SER37, VOL37, HEAT
from s37b import ICE, H2O

BERRY = (220, 90, 100)
ALU = (200, 205, 215)
PAPERC = (235, 225, 200)
IRC = (230, 80, 160)
COLDC = (110, 160, 240)


# ---------------------------------------------------------------- E198 冻干
def e198_sublimation(c, t, i):
    corner_tag(c, '第 198 集 · 冰不化成水，直接变成水汽')
    c.text(60, 96, '把食物先冻住，再把周围的空气抽走：气压很低时，冰来不及化成水，就直接一个个变成水汽飞走', 'serif', 36, INK)
    p = min(1.0, t / 16)
    cx, cy = 620, 580
    c.rect(220, 280, 1020, 880, fill=mix(BG, (60, 70, 85), 0.5), outline=MUTED, width=4, r=20)
    c.text(620, 320, f'抽气：气压越来越低', 'bold', 24, SPARK, 'mm')
    c.ellipse(cx, cy + 40, 200, 150, fill=mix(BG, BERRY, 0.85))
    r = random.Random(7)
    for k in range(60):
        x = cx + r.uniform(-170, 170)
        y = cy + 40 + r.uniform(-120, 120)
        if ((x - cx) / 180) ** 2 + ((y - cy - 40) / 135) ** 2 > 1: continue
        gone = r.random() < p
        if not gone:
            c.rect(x - 8, y - 8, x + 8, y + 8, fill=mix(BG, ICE, 0.95), r=2)
        else:
            c.ellipse(x, y, 6, 6, fill=mix(BG, (60, 40, 40), 0.9))
            ph = (t * 0.6 + k * 0.13) % 1
            c.ellipse(x + (x - cx) * ph * 0.4, max(300, y - ph * 150), 5, 5, fill=mix(BG, H2O, 1 - ph))
    c.text(cx, 760, '冻住的草莓', 'bold', 24, INK, 'mm')
    c.rect(1120, 300, 1860, 760, fill=SHEET, r=14)
    c.text(1490, 350, '平时：冰 → 水 → 水汽', 'bold', 24, INK, 'mm')
    c.text(1490, 410, '气压很低时：冰 → 水汽', 'bold', 24, SPARK, 'mm')
    c.text(1490, 480, '这叫「升华」', 'sans', 22, MUTED, 'mm')
    c.text(1490, 560, '水没有流动，草莓不塌不缩', 'sans', 22, INK, 'mm')
    c.text(1490, 610, '冰的位置留下一个个小空洞', 'sans', 22, INK, 'mm')
    c.text(1490, 690, '冰箱里的冰块也会慢慢「瘦」', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '先把草莓冻得硬硬的，里面的水都变成了一粒粒小冰晶'),
                (7.2, 14, '再把周围的空气抽走，气压低到冰来不及化成水，就直接变成水汽'),
                (14.2, 22, '水汽被抽走，冰晶原来的位置留下小空洞：草莓变得又轻又脆，形状一点不变（示意）')], y=1010)


def e198_rehydrate(c, t, i):
    corner_tag(c, '第 198 集 · 留下小空洞，一泡水就复原')
    c.text(60, 96, '冻干的东西里全是冰留下的细小空洞，水一碰就顺着空洞钻进去：又轻又脆的草莓几分钟就软回来', 'serif', 36, INK)
    p = min(1.0, t / 14)
    cx, cy = 620, 560
    c.rect(220, 280, 1020, 860, fill=mix(BG, WATER_L, 0.3 * p), outline=MUTED, width=4, r=20)
    c.ellipse(cx, cy, 240, 180, fill=mix(BG, BERRY, 0.6 + 0.3 * p))
    r = random.Random(3)
    for k in range(70):
        x = cx + r.uniform(-210, 210)
        y = cy + r.uniform(-150, 150)
        if ((x - cx) / 220) ** 2 + ((y - cy) / 165) ** 2 > 1: continue
        filled = r.random() < p
        c.ellipse(x, y, 9, 9, fill=mix(BG, H2O, 0.9) if filled else mix(BG, (40, 30, 30), 0.95))
    c.text(cx, 900, '空洞（黑）→ 被水填满（蓝）', 'sans', 22, MUTED, 'mm')
    gx0, gx1, gy0, gy1 = 1180, 1820, 820, 360
    c.rect(1120, 300, 1860, 900, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    pts = [(gx0 + (gx1 - gx0) * s / 60, gy0 - 400 * (1 - math.exp(-s / 12))) for s in range(int(60 * p) + 1)]
    if len(pts) > 1:
        c.line(pts, H2O, 4)
    c.text(1500, gy0 + 34, '泡水 → 5 分钟（示意）', 'sans', 20, MUTED, 'mm')
    c.text(gx0 + 10, gy1 - 20, '草莓的重量', 'sans', 20, MUTED, 'lm')
    caps(c, t, [(0, 7, '冻干时，冰一粒粒直接变成水汽走了，留下的位置变成细小的空洞'),
                (7.2, 14, '这些空洞连成一片，水一碰到就顺着钻进去'),
                (14.2, 22, '几分钟就吸饱了水，重量涨回好几倍：宇航员吃的冻干食物，加水就能吃（示意）')], y=1010)


# ---------------------------------------------------------------- E199 恒温器
def _bistrip(c, x0, y0, L, curv, w=18):
    if abs(curv) < 1e-5:
        top = [(x0, y0 - w / 2 + k * 0) for k in range(2)]
        c.rect(x0, y0 - w, x0 + 12, y0, fill=ALU)
        c.rect(x0, y0 - w, x0 + 12, y0, fill=ALU)
    pts_a, pts_b = [], []
    R = 1 / curv if abs(curv) > 1e-5 else None
    for k in range(41):
        s = L * k / 40
        if R is None:
            x, y, nx, ny = x0, y0 - s, 1, 0
        else:
            a = s / R
            x = x0 + R * (1 - math.cos(a))
            y = y0 - R * math.sin(a)
            nx, ny = math.cos(a), math.sin(a)
        pts_a.append((x - nx * w / 2, y - ny * w / 2))
        pts_b.append((x + nx * w / 2, y + ny * w / 2))
    c.line(pts_a, ALU, int(w / 2))
    c.line(pts_b, PAPERC, int(w / 2))
    return pts_a[-1]


def e199_bimetal(c, t, i):
    corner_tag(c, '第 199 集 · 两种材料胀得不一样，片子就弯')
    c.text(60, 96, '口香糖锡纸一面是铝、一面是纸：一吹热风，铝胀得比纸多，长的一面在外，整条就往纸那面弯过去', 'serif', 36, INK)
    heat = 0.5 + 0.5 * math.sin(t * 0.5 - math.pi / 2)
    c.rect(500, 860, 900, 900, fill=mix(BG, (150, 110, 80), 0.8), r=4)
    _bistrip(c, 700, 860, 420, 0.0035 * heat)
    if heat > 0.2:
        for k in range(5):
            ph = (t * 1.5 + k * 0.2) % 1
            c.arrow(150 + ph * 300, 500 + k * 50, 230 + ph * 300, 500 + k * 50, mix(BG, HEAT, heat * (1 - ph)), 3, 10)
        c.text(260, 440, '吹风机暖风（成年人操作）', 'sans', 22, HEAT, 'mm')
    c.rect(1180, 300, 1860, 760, fill=SHEET, r=14)
    c.text(1520, 350, '受热后各自变长多少', 'bold', 24, INK, 'mm')
    c.rect(1240, 420, 1240 + 420 * (1 + 0.15 * heat), 450, fill=ALU, r=4)
    c.text(1240, 400, '铝：胀得多', 'sans', 20, ALU, 'lm')
    c.rect(1240, 520, 1240 + 420 * (1 + 0.04 * heat), 550, fill=PAPERC, r=4)
    c.text(1240, 500, '纸：几乎不胀', 'sans', 20, PAPERC, 'lm')
    c.text(1520, 640, '粘在一起，只能弯', 'bold', 24, SPARK, 'mm')
    c.text(1520, 690, '长的那面在弯的外侧', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '几乎所有东西受热都会变长一点，可不同材料变长的多少不一样'),
                (7.2, 14, '铝和纸粘成一片：热了铝要变长，纸不跟着变，片子只能弯过去'),
                (14.2, 22, '凉下来又弯回来：真正的恒温器用两种金属，叫双金属片（示意）')], y=1010)


def e199_cutoff(c, t, i):
    corner_tag(c, '第 199 集 · 弯到一定程度，把电路断开')
    c.text(60, 96, '把双金属片做成开关的一部分：冷的时候它碰着触点，电路通；热到一定温度它弯开，电就断了', 'serif', 36, INK)
    up = max(0.0, min(1.0, (t - 7) / 5)) - max(0.0, min(1.0, (t - 15) / 5))
    T = 20 + 70 * up
    bend = max(0, (T - 20) / 70)
    on = T < 60
    c.rect(200, 420, 360, 600, fill=mix(BG, (90, 90, 100), 0.9), r=10)
    c.text(280, 510, '1.5 伏电池', 'bold', 20, BG, 'mm')
    c.line([(360, 450), (700, 450), (700, 320)], INK, 4)
    c.line([(360, 570), (1200, 570), (1200, 420)], INK, 4)
    c.ellipse(1200, 380, 50, 50, fill=mix(BG, (255, 220, 120), 0.95 if on else 0.15), outline=MUTED, width=3)
    c.text(1200, 300, '小灯泡', 'sans', 22, MUTED, 'mm')
    a = -0.35 * max(0, (T - 55) / 35)
    for off, col in ((-5, ALU), (5, PAPERC)):
        c.line([(700, 320 + off), (700 + 300 * math.cos(a), 320 + off + 300 * math.sin(a))], col, 8)
    c.ellipse(1000, 320, 14, 14, fill=SPARK)
    c.line([(1000, 320), (1200, 320), (1200, 330)], INK, 4)
    c.text(1000, 270, '触点', 'sans', 20, SPARK, 'mm')
    c.text(960, 760, f'温度 {T:.0f} ℃（示意）', 'mono', 30, HEAT, 'mm')
    c.text(960, 820, '通电：灯亮' if on else '片子弯开：断电，灯灭', 'bold', 28, GREEN if on else NRED, 'mm')
    c.rect(1380, 620, 1860, 880, fill=SHEET, r=14)
    c.text(1620, 670, '电水壶、熨斗、电热毯', 'bold', 22, INK, 'mm')
    c.text(1620, 720, '里面都有类似的小片', 'sans', 22, INK, 'mm')
    c.text(1620, 800, '只用 1.5 伏电池，绝不接插座', 'bold', 20, NRED, 'mm')
    caps(c, t, [(0, 7, '冷的时候，双金属片直直的，正好压着触点，电流通过，灯亮'),
                (7.2, 14, '温度升高，片子慢慢弯起来，弯到离开触点，电路就断了'),
                (14.2, 22, '凉下来它又弯回去接上：一开一关，温度就被管在一个范围里（示意）')], y=1010)


# ---------------------------------------------------------------- E200 红外测温枪
def e200_infrared(c, t, i):
    corner_tag(c, '第 200 集 · 热的东西都在发红外光')
    c.text(60, 96, '一切有温度的东西都在不停发出看不见的红外光：越热发得越多，测温枪就是一只只看红外的「眼睛」', 'serif', 36, INK)
    items = [('冰水', 2, COLDC), ('桌面', 22, (160, 130, 100)), ('手心', 34, (225, 190, 160)), ('温水', 48, WATER_L)]
    for k, (lab, T, col) in enumerate(items):
        x = 280 + k * 380
        y = 560
        c.rect(x - 90, y - 70, x + 90, y + 70, fill=mix(BG, col, 0.85), r=16)
        c.text(x, y, lab, 'bold', 24, BG, 'mm')
        inten = ((T + 273) / 320) ** 4
        n = int(4 + 10 * inten)
        for j in range(n):
            a = 2 * math.pi * j / n + t * 0.3
            ph = (t * 0.8 + j / n) % 1
            r0, r1 = 110, 110 + 130 * ph
            c.line([(x + r0 * math.cos(a), y + r0 * math.sin(a)), (x + r1 * math.cos(a), y + r1 * math.sin(a))], mix(BG, IRC, (1 - ph) * min(1, inten)), 3)
        c.text(x, y + 230, f'{T} ℃', 'mono', 26, SPARK, 'mm')
    c.text(960, 880, '紫色线条：看不见的红外光（示意）——越热越多越强', 'sans', 22, IRC, 'mm')
    caps(c, t, [(0, 7, '我们看不见，但冰水、桌子、你的手，都在一刻不停地发出红外光'),
                (7.2, 14, '温度越高，发出的红外光越多越强'),
                (14.2, 22, '测温枪里有个对红外光敏感的小元件，收到多少就换算成温度（示意）')], y=1010)


def e200_reading(c, t, i):
    corner_tag(c, '第 200 集 · 量的是对准的那块表面')
    c.text(60, 96, '测温枪量的是它对准的那一小块表面发出的红外光：中间隔一块玻璃，玻璃挡住红外，读到的就成了玻璃的温度', 'serif', 34, INK)
    stage = int(t / 7.4)
    cx, cy = 1240, 560
    c.rect(cx - 140, cy - 160, cx + 140, cy + 160, fill=mix(BG, WATER_L, 0.6), outline=MUTED, width=4, r=16)
    c.text(cx, cy + 210, '一杯 48 ℃ 的温水', 'bold', 24, INK, 'mm')
    gx, gy = 300, 560
    c.poly([(gx, gy - 40), (gx + 160, gy - 30), (gx + 160, gy + 30), (gx, gy + 40)], mix(BG, (90, 95, 110), 0.95))
    c.rect(gx + 40, gy + 30, gx + 90, gy + 160, fill=mix(BG, (90, 95, 110), 0.95), r=8)
    c.text(gx + 80, gy - 80, '测温枪', 'bold', 22, INK, 'mm')
    glass = stage == 2
    if glass:
        c.rect(760, 360, 790, 760, fill=mix(BG, (200, 230, 240), 0.5), outline=MUTED, width=2)
        c.text(775, 330, '一块玻璃', 'sans', 22, MUTED, 'mm')
    for k in range(6):
        ph = (t * 0.8 + k / 6) % 1
        x = cx - 140 - ph * (cx - 140 - gx - 160)
        if glass and x < 790:
            continue
        c.line([(x, cy - 60 + k * 24), (x - 40, cy - 60 + k * 24)], IRC, 3)
    if glass:
        for k in range(3):
            ph = (t * 0.8 + k / 3) % 1
            x = 760 - ph * (760 - gx - 160)
            c.line([(x, cy - 30 + k * 30), (x - 30, cy - 30 + k * 30)], mix(BG, IRC, 0.4), 2)
    reading = [48, 48, 24][min(stage, 2)]
    c.rect(gx - 20, 300, gx + 220, 380, fill=SHEET, r=10)
    c.text(gx + 100, 340, f'{reading} ℃', 'mono', 36, SPARK, 'mm')
    c.text(960, 880, ['对准水面', '离远一点也一样', '隔着玻璃：读到的是玻璃'][min(stage, 2)], 'bold', 28, INK if stage < 2 else NRED, 'mm')
    c.text(960, 930, '示意，以实测为准；带激光点的测温枪别对着眼睛', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '对准水面，测温枪收到的是水面发出的红外光，读数和温度计差不多'),
                (7.2, 14, '它量的不是空气，也不是杯子里面，而是对准的那块表面'),
                (14.2, 22, '中间放一块玻璃，玻璃把水的红外光挡住了，测温枪读到的是玻璃自己的温度（示意）')], y=1010)


CLIPS = {
 'E198_升华': (e198_sublimation, 22), 'E198_复原': (e198_rehydrate, 22),
 'E198_片头': (titles.opening(SER37, VOL37, S37A, 6, '二战期间冻干技术用于血浆和青霉素'), 7),
 'E198_片尾': (titles.closing(SER37, VOL37, S37A, 6, '下集：电热水壶烧开了，为什么会自己断电？'), 7),
 'E199_双金属': (e199_bimetal, 22), 'E199_断电': (e199_cutoff, 22),
 'E199_片头': (titles.opening(SER37, VOL37, S37A, 7, '19 世纪 30 年代出现双金属恒温器'), 7),
 'E199_片尾': (titles.closing(SER37, VOL37, S37A, 7, '下集：测温枪没碰到你，怎么量出体温？'), 7),
 'E200_红外': (e200_infrared, 22), 'E200_测温': (e200_reading, 22),
 'E200_片头': (titles.opening(SER37, VOL37, S37A, 8, '20 世纪后期手持红外测温仪普及'), 7),
 'E200_片尾': (titles.closing(SER37, VOL37, S37A, 8, '下集：一块活性炭，怎么把颜色和怪味吸走？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
