"""第三十八季（古法解密 16.0：风、雨、田、声与数）第一批：B160 风箱、B161 斗笠、B162 连枷 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB38 = [('B160', '风箱'), ('B161', '斗笠'), ('B162', '连枷'), ('B163', '哨子'), ('B164', '九宫格'),
        ('B165', '硬帆'), ('B166', '垂线'), ('B167', '淘金'), ('B168', '沉碗'), ('B169', '锣')]
VOL38 = '第三十八季 · 古法解密 16.0'
AIR = (170, 200, 235)
CLAY = (200, 150, 110)
GRAIN = (225, 195, 110)


# ---------------------------------------------------------------- B160 风箱
def _flap(c, x, y, h, openv, side):
    """竖直活门：铰链在上端，openv 0..1 打开角度，side=+1 向右开 / -1 向左开。"""
    a = openv * math.radians(55)
    x1 = x + side * h * math.sin(a)
    y1 = y + h * math.cos(a)
    c.line([(x, y), (x1, y1)], SPARK if openv > 0.1 else INK, 7)
    c.ellipse(x, y, 6, 6, fill=INK)


def b160_valves(c, t, i):
    corner_tag(c, 'B160 · 只进不出的小活门')
    c.text(60, 96, '一片轻轻挂着的薄板：气流从这边推，它就打开；从那边吸，它就被压回去关死', 'serif', 36, INK)
    ph = (t % 6) / 6
    push = ph < 0.5
    for j, (lab, flow) in enumerate([('气流往右：活门被推开', 1), ('气流往左：活门被压在门框上', -1)]):
        cx, cy = 520 + j * 880, 560
        c.rect(cx - 320, cy - 160, cx + 320, cy + 160, fill=mix(BG, WOOD, 0.25), r=12)
        c.rect(cx - 320, cy - 60, cx + 320, cy + 60, fill=mix(BG, AIR, 0.18))
        c.rect(cx - 8, cy - 160, cx + 8, cy - 60, fill=mix(BG, WOOD, 0.9))
        c.rect(cx - 8, cy + 60, cx + 8, cy + 160, fill=mix(BG, WOOD, 0.9))
        op = 1.0 if flow > 0 else 0.0
        _flap(c, cx + 10, cy - 60, 118, op, 1)
        if flow > 0:
            for k in range(6):
                x = cx - 300 + ((t * 160 + k * 110) % 600)
                c.arrow(x, cy + (k % 3 - 1) * 30, x + 50, cy + (k % 3 - 1) * 30, AIR, 4, 12)
        else:
            for k in range(3):
                x = cx + 280 - ((t * 120 + k * 90) % 260)
                c.arrow(x, cy + (k - 1) * 30, x - 50, cy + (k - 1) * 30, AIR, 4, 12)
            c.text(cx - 120, cy, '×', 'bold', 60, NRED, 'mm')
        c.text(cx, cy + 230, lab, 'bold', 26, INK, 'mm')
    c.text(960, 880, '活门 = 单向阀：心脏、自行车打气筒、水泵里都有它', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '风箱里藏着几片轻轻挂着的小木板，叫活门'),
                (7.2, 14, '气流从一边推，活门就被推开；从另一边吸，活门被压在框上，关得严严实实'),
                (14.2, 22, '空气只能往一个方向走：这就是单向阀（示意）')], y=1010)


def b160_pushpull(c, t, i):
    corner_tag(c, 'B160 · 推也出风，拉也出风')
    c.text(60, 96, '活塞两边各有一间「气室」：推的时候前面那间往外送，拉的时候后面那间往外送', 'serif', 36, INK)
    x0, x1, y0, y1 = 300, 1300, 380, 700
    s = 0.5 + 0.5 * math.sin(t * 2 * math.pi / 6)
    px = x0 + 120 + s * (x1 - x0 - 240)
    vel = math.cos(t * 2 * math.pi / 6)
    c.rect(x0, y0, x1, y1, fill=mix(BG, WOOD, 0.3), outline=mix(BG, WOOD, 1.0), width=6, r=10)
    c.rect(px - 15, y0 + 8, px + 15, y1 - 8, fill=mix(BG, WOOD, 1.0))
    c.line([(px, (y0 + y1) / 2), (x1 + 260, (y0 + y1) / 2)], mix(BG, WOOD, 1.0), 14)
    c.rect(x1 + 240, (y0 + y1) / 2 - 60, x1 + 280, (y0 + y1) / 2 + 60, fill=mix(BG, WOOD, 1.0), r=8)
    c.text(x1 + 260, (y0 + y1) / 2 + 100, '拉杆', 'sans', 22, MUTED, 'mm')
    # 两端进气活门
    _flap(c, x0 + 6, y0 + 40, 70, 1.0 if vel > 0 else 0.0, 1)
    _flap(c, x1 - 6, y0 + 40, 70, 1.0 if vel < 0 else 0.0, -1)
    c.text(x0 + 40, y0 - 30, '进气活门', 'sans', 20, MUTED, 'mm')
    c.text(x1 - 40, y0 - 30, '进气活门', 'sans', 20, MUTED, 'mm')
    # 风道
    c.rect(x0, y1, x1, y1 + 90, fill=mix(BG, WOOD, 0.2), outline=mix(BG, WOOD, 0.8), width=4)
    c.rect((x0 + x1) / 2 - 40, y1 + 90, (x0 + x1) / 2 + 40, y1 + 200, fill=mix(BG, WOOD, 0.2), outline=mix(BG, WOOD, 0.8), width=4)
    _flap(c, x0 + 60, y1, 60, 1.0 if vel < 0 else 0.0, 1)
    _flap(c, x1 - 60, y1, 60, 1.0 if vel > 0 else 0.0, -1)
    side = '左' if vel < 0 else '右'
    ox = x0 + 60 if vel < 0 else x1 - 60
    for k in range(5):
        f = ((t * 1.2 + k / 5) % 1)
        if f < 0.5:
            x = ox + ((x0 + x1) / 2 - ox) * f * 2
            c.ellipse(x, y1 + 45, 8, 8, fill=AIR)
        else:
            c.ellipse((x0 + x1) / 2, y1 + 90 + (f - 0.5) * 220, 8, 8, fill=AIR)
    c.text((x0 + x1) / 2, y1 + 240, '→ 炉膛（示意，不点火）', 'sans', 22, MUTED, 'mm')
    c.rect(1460, 720, 1880, 920, fill=SHEET, r=12)
    c.text(1670, 765, '拉杆往外拉' if vel > 0 else '拉杆往里推', 'bold', 28, INK, 'mm')
    c.text(1670, 825, f'{side}边气室在送风', 'sans', 24, SPARK, 'mm')
    c.text(1670, 875, '另一边从进气活门吸气', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '活塞把箱子分成左右两间气室，每间都有一个进气活门、一个出气活门'),
                (7.2, 14, '推的时候，前面那间被压缩往外送风，后面那间同时吸进新鲜空气'),
                (14.2, 22, '拉回来正好反过来：一推一拉都在出风，炉火不会一阵一阵（示意）')], y=1010)


# ---------------------------------------------------------------- B161 斗笠
def _cone(c, cx, ty, half, h, col):
    c.poly([(cx, ty), (cx - half, ty + h), (cx + half, ty + h)], col)


def b161_slope(c, t, i):
    corner_tag(c, 'B161 · 斜面让雨水顺坡流走')
    c.text(60, 96, '同样宽的三顶「斗笠」：越陡，雨水在上面停得越短、流得越快', 'serif', 36, INK)
    r = random.Random(3)
    for j, (h, lab) in enumerate([(70, '很平'), (180, '中等'), (330, '很陡')]):
        cx = 360 + j * 600
        base = 700
        half = 230
        _cone(c, cx, base - h, half, h, mix(BG, STRAW, 0.9))
        L = math.hypot(half, h)
        sp = 0.6 + 2.4 * h / L
        for k in range(10):
            f = ((t * sp * 0.35 + k / 10) % 1)
            for sgn in (-1, 1):
                x = cx + sgn * half * f
                y = base - h + h * f - 10
                c.ellipse(x, y, 7, 9, fill=WATER)
        for k in range(14):
            x = cx - 300 + r.uniform(0, 600)
            y = 200 + ((t * 300 + k * 47) % 300)
            if y < base - h - 20 or abs(x - cx) > half:
                c.line([(x, y), (x - 4, y + 18)], mix(BG, WATER_L, 0.8), 3)
        c.text(cx, base + 60, lab, 'bold', 28, INK, 'mm')
        c.text(cx, base + 105, f'水停留约 {1 / sp:.1f} 份时间（示意）', 'sans', 22, MUTED, 'mm')
    c.text(960, 900, '可太陡了，帽子又重又挡风：斗笠的角度是折中出来的', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '雨点落在斗笠上，被斜面引着往下流'),
                (7.2, 14, '坡越陡，水流得越快，渗进竹编缝里的就越少'),
                (14.2, 22, '屋顶、蓑衣也都是同一个办法：让水赶紧走（示意）')], y=1010)


def b161_brim(c, t, i):
    corner_tag(c, 'B161 · 宽檐把水甩到身外')
    c.text(60, 96, '檐窄，水顺着帽沿滴到肩膀上；檐宽过肩膀，水滴落在身体外面', 'serif', 36, INK)
    for j, (half, lab) in enumerate([(150, '檐窄：肩膀湿了'), (300, '檐宽：肩膀干的')]):
        cx = 520 + j * 880
        top = 300
        c.ellipse(cx, 560, 70, 80, fill=mix(BG, CLAY, 0.8))
        c.rect(cx - 170, 650, cx + 170, 900, fill=mix(BG, (90, 110, 150), 0.9), r=40)
        _cone(c, cx, top, half, 190, mix(BG, STRAW, 0.95))
        for sgn in (-1, 1):
            ex = cx + sgn * half
            for k in range(4):
                f = ((t * 0.9 + k / 4) % 1)
                y = top + 190 + f * 420
                land = 650 if abs(ex - cx) < 170 else 960
                if y < land:
                    c.ellipse(ex, y, 7, 10, fill=WATER)
            if abs(ex - cx) < 170:
                c.ellipse(ex, 660, 40, 14, fill=mix(BG, WATER, 0.6))
        c.text(cx, 960, lab, 'bold', 26, NRED if j == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '水流到帽檐的最边上，就一滴滴往下掉：这条线叫滴水线'),
                (7.2, 14, '帽檐窄，滴水线落在肩膀上，衣服很快湿透'),
                (14.2, 22, '帽檐宽过肩膀，水全落在身体外面：屋檐伸出墙外也是这个道理（示意）')], y=1040)


# ---------------------------------------------------------------- B162 连枷
def b162_swing(c, t, i):
    corner_tag(c, 'B162 · 甩起来的短棍末端最快')
    c.text(60, 96, '手只转一小圈，长柄带着短棍甩出去：越到末端，转过的路越长，速度越快', 'serif', 36, INK)
    px, py = 300, 740
    T = 3.0
    ph = (t % T) / T
    e = 0.5 - 0.5 * math.cos(math.pi * min(1, ph * 1.4))
    th = -math.radians(60) + math.radians(68) * e
    L1, L2 = 360, 220
    hx, hy = px + L1 * math.cos(th), py + L1 * math.sin(th)
    th2 = th + math.radians(-30 + 55 * e)
    ex, ey = hx + L2 * math.cos(th2), hy + L2 * math.sin(th2)
    c.line([(px, py), (hx, hy)], mix(BG, WOOD, 1.0), 14)
    c.line([(hx, hy), (ex, ey)], mix(BG, WOOD, 0.85), 18)
    c.ellipse(hx, hy, 12, 12, fill=ROPEC)
    c.ellipse(px, py, 22, 22, fill=mix(BG, CLAY, 0.9))
    c.text(px, py + 50, '手', 'sans', 24, MUTED, 'mm')
    c.rect(1180, 260, 1860, 640, fill=SHEET, r=14)
    c.text(1520, 310, '同一时刻的速度（示意）', 'bold', 26, INK, 'mm')
    for k, (lab, v) in enumerate([('手', 1), ('柄头', 3), ('短棍末端', 5)]):
        y = 380 + k * 80
        c.text(1220, y, lab, 'sans', 24, INK, 'lm')
        c.rect(1380, y - 16, 1380 + v * 80, y + 16, fill=SPARK if k == 2 else mix(BG, SPARK, 0.5), r=6)
        c.text(1400 + v * 80, y, f'× {v}', 'mono', 22, INK, 'lm')
    c.rect(600, 905, 1150, 960, fill=mix(BG, GRAIN, 0.6))
    c.text(875, 932, '谷穗', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '人握着长柄，手腕只转一小圈'),
                (7.2, 14, '长柄带着短棍甩出去：越到末端，同样的时间里走过的路越长'),
                (14.2, 22, '末端的速度比手快好几倍，砸下去，谷粒就从穗上被打下来（示意）')], y=1010)


ROPEC = (215, 190, 140)


def b162_impact(c, t, i):
    corner_tag(c, 'B162 · 越快，砸下去越狠')
    c.text(60, 96, '一样重的木棍，砸下去的速度快一倍，在橡皮泥上砸出的坑就深得多', 'serif', 36, INK)
    p = min(1.0, t / 14)
    for j, (lab, d) in enumerate([('直棍：坑浅', 6), ('连枷：坑深', 18)]):
        cx = 520 + j * 880
        top = 620
        k = min(5, int(t / 2.4))
        depth = d * k / 5 * 3
        c.rect(cx - 260, top, cx + 260, top + 120, fill=mix(BG, CLAY, 0.85), r=10)
        c.ellipse(cx, top + 4, 60, max(2, depth), fill=mix(BG, CLAY, 0.45))
        ph = (t % 2.4) / 2.4
        yy = top - 300 + 300 * min(1, ph * 2) if ph < 0.5 else top - 300 * (ph - 0.5) * 2
        c.rect(cx - 30, yy - 200, cx + 30, yy, fill=mix(BG, WOOD, 0.9), r=8)
        c.text(cx, top + 180, lab, 'bold', 26, INK, 'mm')
        c.text(cx, top + 225, f'已砸 {k} 下，坑深约 {depth / 10:.1f} 厘米（示意）', 'sans', 22, MUTED, 'mm')
    c.text(960, 960, '只砸橡皮泥，不朝人甩', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '同样的手腕动作，直棍和连枷各在橡皮泥饼上砸 5 下'),
                (7.2, 14, '连枷的短棍到达泥饼时快得多，坑也深得多'),
                (14.2, 22, '速度越快，一下撞击里交给谷穗的冲击就越大；短棍太重又甩不起来（示意）')], y=1020)


CLIPS = {
 'B160_活门': (b160_valves, 22), 'B160_推拉': (b160_pushpull, 22),
 'B160_片头': (titles.opening(BSER, VOL38, SB38, 0, '宋元时期已有推拉式双动木风箱'), 7),
 'B160_片尾': (titles.closing(BSER, VOL38, SB38, 0, '下集：竹编的尖帽子，为什么雨淋不湿肩膀？'), 7),
 'B161_斜面': (b161_slope, 22), 'B161_宽檐': (b161_brim, 22),
 'B161_片头': (titles.opening(BSER, VOL38, SB38, 1, '先秦已有「笠」遮雨挡日'), 7),
 'B161_片尾': (titles.closing(BSER, VOL38, SB38, 1, '下集：打谷子为什么要一节会转的短棍？'), 7),
 'B162_甩': (b162_swing, 22), 'B162_冲击': (b162_impact, 22),
 'B162_片头': (titles.opening(BSER, VOL38, SB38, 2, '春秋时已有连枷打谷'), 7),
 'B162_片尾': (titles.closing(BSER, VOL38, SB38, 2, '下集：一吹就响的哨子，声音从哪里来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
