"""第三十七季（第十五层：菜园与厨房）第二批：E195 真空包装、E196 干燥剂、E197 速冻 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L
from s37a import S37A, SER37, VOL37, O2, FILM

APPLE = (245, 230, 190)
BROWN = (170, 120, 70)
GEL = (220, 230, 240)
H2O = (110, 170, 240)
ICE = (200, 230, 250)
CELL = (150, 200, 120)


# ---------------------------------------------------------------- E195 真空包装
def e195_oxygen(c, t, i):
    corner_tag(c, '第 195 集 · 没有氧气，坏得就慢')
    c.text(60, 96, '苹果切开后变褐，是切口和空气里的氧气起了反应；把袋子里的空气排掉，氧气少了，变色就慢得多', 'serif', 36, INK)
    p = min(1.0, t / 16)
    for j, (lab, n_o2, rate) in enumerate([('敞口的袋子', 40, 1.0), ('排掉空气的密封袋', 3, 0.12)]):
        cx = 520 + j * 880
        bw = 300 if j == 0 else 220
        c.rect(cx - bw, 300, cx + bw, 820, fill=mix(BG, FILM, 0.15), outline=FILM, width=3, r=30 if j == 0 else 60)
        c.ellipse(cx, 580, 170, 120, fill=mix(APPLE, BROWN, min(1, rate * p)))
        c.ellipse(cx, 580, 30, 18, fill=mix(BG, (90, 60, 40), 0.8))
        r = random.Random(j)
        for k in range(n_o2):
            ang = r.uniform(0, 2 * math.pi)
            rad = r.uniform(190, bw - 20)
            ph = t * r.uniform(0.5, 1.2)
            x = cx + rad * math.cos(ang + ph * 0.3) * (bw / 300)
            y = 560 + rad * 0.9 * math.sin(ang + ph * 0.3) * (bw / 300)
            y = max(320, min(800, y))
            c.ellipse(x, y, 8, 8, fill=O2)
        c.text(cx, 870, lab, 'bold', 26, INK, 'mm')
    c.text(960, 940, f'过了 {p * 2:.1f} 小时（示意，苹果不吃）', 'mono', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '苹果切开，切口里的物质碰到空气中的氧气，就慢慢变成褐色'),
                (7.2, 14, '敞口的袋子里氧气源源不断，切口越来越褐'),
                (14.2, 22, '排掉空气再封口，袋里几乎没剩氧气，变色就慢得多：很多食物变坏都和氧气有关（示意）')], y=1010)


def e195_pressure(c, t, i):
    corner_tag(c, '第 195 集 · 外面的大气压把袋子压紧')
    c.text(60, 96, '袋子里的空气被排走，里面没东西往外顶了，外面的大气从四面八方压过来，把袋子和里面的东西压紧', 'serif', 36, INK)
    p = min(1.0, t / 12)
    cx, cy = 760, 580
    sq = 1 - 0.55 * p
    W, H = 360 * (1 - 0.15 * p), 240 * sq
    c.rect(cx - W, cy - H, cx + W, cy + H, fill=mix(BG, FILM, 0.2), outline=FILM, width=3, r=40)
    c.rect(cx - 220, cy - 140 * sq, cx + 220, cy + 140 * sq, fill=mix(BG, (240, 210, 120), 0.8), r=20)
    c.text(cx, cy, '海绵', 'bold', 26, BG, 'mm')
    for k in range(10):
        a = 2 * math.pi * k / 10
        ex, ey = cx + (W + 40) * math.cos(a), cy + (H + 40) * math.sin(a)
        sx, sy = cx + (W + 140) * math.cos(a), cy + (H + 140) * math.sin(a)
        c.arrow(sx, sy, ex, ey, mix(BG, SPARK, 0.4 + 0.6 * p), 4, 14)
    c.text(cx, 230, '外面的大气压', 'bold', 24, SPARK, 'mm')
    c.rect(1320, 300, 1860, 760, fill=SHEET, r=14)
    c.text(1590, 350, '压水排气法', 'bold', 26, INK, 'mm')
    c.text(1590, 420, '袋子慢慢按进水里', 'sans', 22, INK, 'mm')
    c.text(1590, 470, '袋口留在水面上', 'sans', 22, INK, 'mm')
    c.text(1590, 520, '水把空气挤出去', 'sans', 22, INK, 'mm')
    c.text(1590, 570, '再封口', 'sans', 22, INK, 'mm')
    c.text(1590, 660, '不用嘴吸', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '袋子里有空气时，里外的气压一样大，袋子松松的'),
                (7.2, 14, '把空气排掉，里面没有东西往外顶，外面的大气压就占了上风'),
                (14.2, 22, '四面八方一起压，海绵被压扁一大半：超市里的真空包装硬邦邦，就是这个力（示意）')], y=1010)


# ---------------------------------------------------------------- E196 干燥剂
def e196_pores(c, t, i):
    corner_tag(c, '第 196 集 · 无数细孔把水汽吸住')
    c.text(60, 96, '放大一颗硅胶：里面是迷宫一样的细孔，空气里的水分子钻进去，被粘在孔壁上，出不来', 'serif', 36, INK)
    cx, cy, R = 760, 580, 320
    c.ellipse(cx, cy, R, R, fill=mix(BG, GEL, 0.35), outline=GEL, width=4)
    r = random.Random(2)
    pores = []
    for k in range(14):
        a = 2 * math.pi * k / 14
        pts = [(cx + R * math.cos(a), cy + R * math.sin(a))]
        x, y = pts[0]
        for j in range(6):
            a2 = a + math.pi + r.uniform(-0.6, 0.6)
            x += 40 * math.cos(a2); y += 40 * math.sin(a2)
            pts.append((x, y))
        pores.append(pts)
        c.line(pts, BG, 10)
    for k in range(40):
        pt = pores[k % 14]
        ph = (t * 0.25 + k / 40) % 1.0
        stuck = ph > 0.6
        if not stuck:
            f = ph / 0.6
            idx = min(len(pt) - 1, int(f * (len(pt) - 1)))
            sx, sy = pt[0][0] + (pt[0][0] - cx) * 0.25 * (1 - f * 2) if f < 0.5 else pt[idx][0], pt[0][1] + (pt[0][1] - cy) * 0.25 * (1 - f * 2) if f < 0.5 else pt[idx][1]
            c.ellipse(sx, sy, 8, 8, fill=H2O)
        else:
            x, y = pt[min(5, k % 6)]
            c.ellipse(x + 6, y + 6, 7, 7, fill=mix(BG, H2O, 0.8))
    c.rect(1280, 300, 1860, 740, fill=SHEET, r=14)
    c.text(1570, 350, '1 克硅胶的孔壁', 'bold', 26, INK, 'mm')
    c.text(1570, 410, '摊开有几百平方米', 'mono', 26, SPARK, 'mm')
    c.text(1570, 480, '（约一个篮球场那么大）', 'sans', 22, MUTED, 'mm')
    c.text(1570, 580, '颗粒不能吃', 'bold', 24, NRED, 'mm')
    c.text(1570, 630, '别让幼儿拿到', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '硅胶看着是一颗颗透明的小珠子，里面其实布满了极细的孔'),
                (7.2, 14, '空气里的水分子钻进细孔，被孔壁牢牢吸住，这叫吸附'),
                (14.2, 22, '孔壁加起来面积巨大，能吸住很多水：饼干袋里的空气就一直是干的（示意）')], y=1010)


def e196_saturate(c, t, i):
    corner_tag(c, '第 196 集 · 吸满了就不吸了')
    c.text(60, 96, '一包干燥剂放在敞口的碗里：头几个小时重量涨得快，越往后越慢，最后不再变：孔都被水占满了', 'serif', 36, INK)
    gx0, gx1, gy0, gy1 = 220, 1300, 860, 300
    c.rect(160, 250, 1360, 920, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    p = min(1.0, t / 16)
    pts = [(gx0 + (gx1 - gx0) * s / 100, gy0 - 480 * (1 - math.exp(-s / 22))) for s in range(int(100 * p) + 1)]
    if len(pts) > 1:
        c.line(pts, H2O, 4)
        x, y = pts[-1]
        c.ellipse(x, y, 10, 10, fill=SPARK)
        c.text(x + 16, y - 20, f'+{(gy0 - y) / 480 * 0.3:.2f} 克', 'mono', 22, SPARK, 'lm')
    c.text((gx0 + gx1) / 2, gy0 + 34, '放了多久 → 一天（示意）', 'sans', 22, MUTED, 'mm')
    c.text(gx0 + 16, gy1 - 20, '干燥剂多了多少重', 'sans', 22, MUTED, 'lm')
    c.rect(1420, 330, 1860, 720, fill=SHEET, r=14)
    c.text(1640, 380, '吸满以后', 'bold', 26, INK, 'mm')
    c.text(1640, 450, '再放也不吸了', 'sans', 22, INK, 'mm')
    c.text(1640, 520, '工厂里用低温烘干', 'sans', 22, INK, 'mm')
    c.text(1640, 570, '把水赶出来，还能再用', 'sans', 22, INK, 'mm')
    c.text(1640, 660, '以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '刚拆开的干燥剂，空的细孔很多，吸得很快'),
                (7.2, 14, '孔一个个被水占上，能吸的地方越来越少，涨得越来越慢'),
                (14.2, 22, '最后孔都满了，重量就不再变：所以干燥剂要密封保存，用过的要换（示意）')], y=1010)


# ---------------------------------------------------------------- E197 速冻
def _cells(c, x0, y0, w, h, crystal, broken, seed):
    r = random.Random(seed)
    cols, rows = 5, 4
    cw, ch = w / cols, h / rows
    for a in range(cols):
        for b in range(rows):
            x, y = x0 + a * cw, y0 + b * ch
            c.rect(x + 4, y + 4, x + cw - 4, y + ch - 4, fill=mix(BG, CELL, 0.5), outline=mix(BG, CELL, 0.9), width=3, r=14)
            if broken and r.random() < 0.7:
                c.line([(x + cw * 0.3, y + 4), (x + cw * 0.5, y + ch * 0.4), (x + cw * 0.4, y + ch - 4)], NRED, 3)
    for k in range(int(w * h / (crystal * crystal * 6))):
        x = x0 + r.uniform(0, w)
        y = y0 + r.uniform(0, h)
        s = crystal * r.uniform(0.7, 1.3)
        c.poly([(x, y - s), (x + s * 0.87, y - s / 2), (x + s * 0.87, y + s / 2), (x, y + s), (x - s * 0.87, y + s / 2), (x - s * 0.87, y - s / 2)], mix(BG, ICE, 0.85))


def e197_crystals(c, t, i):
    corner_tag(c, '第 197 集 · 冻得快，冰晶小，细胞不破')
    c.text(60, 96, '放大黄瓜的细胞：慢慢冻，冰晶有时间长大，把细胞壁撑破；飞快冻住，冰晶又小又多，细胞完好', 'serif', 36, INK)
    p = min(1.0, t / 10)
    for j, (lab, cr) in enumerate([('冰箱慢冻', 10 + 34 * p), ('冰盐水速冻', 4 + 6 * p)]):
        x0 = 160 + j * 880
        _cells(c, x0, 300, 640, 480, cr, j == 0 and p > 0.6, j)
        c.text(x0 + 320, 830, lab, 'bold', 28, INK, 'mm')
        if p >= 1:
            c.text(x0 + 320, 880, '细胞被扎破 → 解冻后出水、软塌' if j == 0 else '细胞完好 → 解冻后还挺脆', 'sans', 22, NRED if j == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '水结冰时先出现一个个小冰核，再慢慢长大成冰晶'),
                (7.2, 14, '冻得慢，少数冰晶有时间长得又大又尖，把细胞壁戳破'),
                (14.2, 22, '冻得快，到处同时结冰，冰晶又小又多：解冻后细胞还在，不出水（示意）')], y=1010)


def e197_icesalt(c, t, i):
    corner_tag(c, '第 197 集 · 冰加盐，能冷到零下十几度')
    c.text(60, 96, '一碗冰撒上盐：盐让冰在零度以下也开始化，化冰要从周围吸热，冰水一下子降到零下十几度', 'serif', 36, INK)
    gx0, gx1, gy0, gy1 = 220, 1260, 860, 300
    c.rect(160, 250, 1320, 920, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    zero = gy1 + 120
    c.line([(gx0, zero), (gx1, zero)], mix(BG, MUTED, 0.5), 1)
    c.text(gx0 - 10, zero, '0 ℃', 'mono', 18, MUTED, 'rm')
    p = min(1.0, t / 14)
    for col, low, lab in [(ICE, 0, '只有冰'), (O2, -16, '冰 + 盐')]:
        pts = []
        for k in range(int(80 * p) + 1):
            s = k / 80
            T = 2 + (low - 2) * (1 - math.exp(-s * 5))
            pts.append((gx0 + (gx1 - gx0) * s, zero - T * 20))
        if len(pts) > 1:
            c.line(pts, col, 4)
            c.text(pts[-1][0] + 10, pts[-1][1], f'{lab} {2 + (low - 2) * (1 - math.exp(-p * 5)):.0f} ℃', 'bold', 22, col, 'lm')
    c.text((gx0 + gx1) / 2, gy0 + 34, '撒盐后 → 10 分钟（示意）', 'sans', 22, MUTED, 'mm')
    c.rect(1380, 320, 1860, 700, fill=SHEET, r=14)
    c.text(1620, 370, '冰盐水很冷', 'bold', 26, NRED, 'mm')
    c.text(1620, 430, '戴手套操作', 'sans', 24, INK, 'mm')
    c.text(1620, 480, '别用手长时间握', 'sans', 24, INK, 'mm')
    c.text(1620, 580, '以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '纯冰放在碗里，温度停在 0 度附近'),
                (7.2, 14, '撒上盐，盐水在零度以下也不结冰，冰就开始化，化冰要吸走大量的热'),
                (14.2, 22, '热从冰水本身被抽走，温度一路降到零下十几度：老式手摇冰淇淋机就靠它（示意）')], y=1010)


CLIPS = {
 'E195_氧气': (e195_oxygen, 22), 'E195_压扁': (e195_pressure, 22),
 'E195_片头': (titles.opening(SER37, VOL37, S37A, 3, '20 世纪 60 年代真空包装用于食品'), 7),
 'E195_片尾': (titles.closing(SER37, VOL37, S37A, 3, '下集：饼干袋里那包颗粒，为什么能让饼干一直脆？'), 7),
 'E196_细孔': (e196_pores, 22), 'E196_吸满': (e196_saturate, 22),
 'E196_片头': (titles.opening(SER37, VOL37, S37A, 4, '20 世纪初硅胶干燥剂开始使用'), 7),
 'E196_片尾': (titles.closing(SER37, VOL37, S37A, 4, '下集：速冻的草莓为什么解冻后不出水？'), 7),
 'E197_冰晶': (e197_crystals, 22), 'E197_冰盐': (e197_icesalt, 22),
 'E197_片头': (titles.opening(SER37, VOL37, S37A, 5, '20 世纪 20 年代伯兹艾发明速冻食品'), 7),
 'E197_片尾': (titles.closing(SER37, VOL37, S37A, 5, '下集：冻干水果里的水，是怎么不化就被拿走的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
