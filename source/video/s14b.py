"""第十四季（古法解密 4.0）第二批：B43 杆秤、B44 船尾舵、B45 扎染 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s14a import SB14, VOL14, BAMBOO, AIR

WOOD = (150, 110, 70)
IRON = (120, 120, 128)
WATER = (60, 110, 160)
INDIGO = (40, 60, 150)
LEUCO = (170, 190, 80)
CLOTH = (235, 230, 215)

# ---------------------------------------------------------------- B43 杆秤
def beam(c, x0, y, L, ang, a=1.0):
    dx, dy = math.cos(ang), math.sin(ang)
    c.line([(x0 - 120 * dx, y - 120 * dy), (x0 + L * dx, y + L * dy)], mix(BG, WOOD, a), 14)
    return dx, dy

def b43_moment(c, t, i):
    corner_tag(c, 'B43 · 力 × 力臂')
    c.text(60, 96, '秤砣挪一挪：力臂变长，就能平衡更重的东西', 'serif', 40, INK)
    px, py = 620, 420
    load = 1 + int(min(2, max(0, t - 4) / 5))  # 1,2,3 kg
    xw = 120 * load  # weight position
    ang = 0.0
    dx, dy = beam(c, px, py, 760, ang)
    c.line([(px, py - 120), (px, py)], MUTED, 3)
    c.text(px, py - 140, '提纽（支点）', 'sans', 22, MUTED, 'mm')
    # load on short arm
    hx = px - 100
    c.line([(hx, py), (hx, py + 120)], MUTED, 3)
    c.rect(hx - 50, py + 120, hx + 50, py + 120 + 40 * load, fill=GREEN, r=6)
    c.text(hx, py + 150 + 40 * load, f'{load} 千克', 'bold', 26, INK, 'mm')
    # counterweight
    wx = px + xw * 1.8
    c.line([(wx, py), (wx, py + 80)], MUTED, 3)
    c.ellipse(wx, py + 110, 34, 34, fill=IRON)
    c.text(wx, py + 175, '秤砣', 'sans', 22, INK, 'mm')
    c.text(hx - 60, py - 30, '短臂', 'sans', 22, MUTED, 'mm')
    a = fade(t, 3, 4)
    c.rect(1180, 760, 1840, 900, fill=mix(BG, SHEET, a), r=12)
    c.text(1510, 800, '重物 × 短臂 = 秤砣 × 长臂', 'bold', 30, mix(BG, INK, a), 'mm')
    c.text(1510, 855, f'{load} 千克 → 秤砣挂在第 {load} 格（示意）', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 4, '杆秤是一根杠杆：提纽就是支点'),
                (4.2, 13, '东西越重，秤砣就要挪得越远：力乘力臂，两边相等，杆就平了'),
                (13.2, 22, '一个秤砣，靠改变力臂，就能称出不同的重量')], y=1010)

def b43_scale(c, t, i):
    corner_tag(c, 'B43 · 刻度为什么是等距的')
    c.text(60, 96, '重量每多一斤，秤砣就往外挪同样一段', 'serif', 40, INK)
    x0, y = 260, 420
    c.line([(x0 - 100, y), (x0 + 1400, y)], WOOD, 16)
    c.line([(x0, y - 120), (x0, y)], MUTED, 3)
    c.text(x0, y - 140, '提纽', 'sans', 22, MUTED, 'mm')
    zero = x0 + 160
    a = fade(t, 1, 2)
    c.ellipse(zero, y, 10, 10, fill=mix(BG, SPARK, a))
    c.text(zero, y + 60, '定盘星（零点）', 'bold', 24, mix(BG, SPARK, a), 'mm')
    c.text(zero, y + 95, '空秤时秤砣挂这里，杆刚好平', 'sans', 20, mix(BG, MUTED, a), 'mm')
    step = 200
    for k in range(1, 7):
        b = fade(t, 3 + k * 1.2, 4 + k * 1.2)
        x = zero + k * step
        c.line([(x, y - 22), (x, y + 22)], mix(BG, INK, b), 3)
        c.text(x, y - 46, f'{k}', 'mono', 28, mix(BG, INK, b), 'mm')
        if k > 1:
            c.arrow(x - step + 20, y + 140, x - 20, y + 140, mix(BG, GREEN, b), 3, 12)
    c.text(zero + 3.5 * step, y + 190, '每一格一样长', 'bold', 26, mix(BG, GREEN, fade(t, 9, 10)), 'mm')
    d = fade(t, 13, 14)
    c.rect(260, 760, 1660, 880, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 800, '秤砣位置 = 定盘星 +（重物 × 短臂 ÷ 秤砣）', 'bold', 28, mix(BG, INK, d), 'mm')
    c.text(960, 845, '重物多一份，位置就加同样一段：所以刻度等距', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '秤杆本身也有重量：先找到空秤平衡的那一点，叫定盘星，这是零'),
                (6.2, 13, '从零点往外，重物每多一斤，秤砣就要多挪同样长的一段'),
                (13.2, 22, '因为力矩和距离成正比：秤杆上的刻度，是一格一格等距的')], y=1010)

# ---------------------------------------------------------------- B44 船尾舵
def boat(c, cx, cy, head, rud, a=1.0):
    h = math.radians(head)
    fx, fy = math.cos(h), math.sin(h)
    nx, ny = -fy, fx
    pts = [(cx + 200 * fx, cy + 200 * fy), (cx + 60 * fx + 60 * nx, cy + 60 * fy + 60 * ny), (cx - 180 * fx + 55 * nx, cy - 180 * fy + 55 * ny),
           (cx - 180 * fx - 55 * nx, cy - 180 * fy - 55 * ny), (cx + 60 * fx - 60 * nx, cy + 60 * fy - 60 * ny)]
    c.poly(pts, mix(BG, WOOD, a))
    sx, sy = cx - 180 * fx, cy - 180 * fy
    r = h + math.pi + math.radians(rud)
    ex, ey = sx + 90 * math.cos(r), sy + 90 * math.sin(r)
    c.line([(sx, sy), (ex, ey)], mix(BG, SPARK, a), 10)
    return sx, sy, ex, ey

def b44_force(c, t, i):
    corner_tag(c, 'B44 · 水流冲斜板')
    c.text(60, 96, '舵一偏，水把船尾推向一边，船头就转过去', 'serif', 40, INK)
    for k in range(7):
        off = (t * 160 + k * 210) % 1500
        y = 230 + k * 100
        c.arrow(150 + off, y, 230 + off, y, mix(BG, WATER, 0.6), 3, 12)
    rud = 30 * fade(t, 3, 5)
    sx, sy, ex, ey = boat(c, 800, 560, 180, rud)
    a = fade(t, 6, 7)
    c.arrow(ex, ey, ex, ey - 150, mix(BG, GREEN, a), 6, 22)
    c.text(ex + 20, ey - 170, '水推船尾', 'bold', 26, mix(BG, GREEN, a), 'lm')
    b = fade(t, 10, 11)
    c.arc(800, 560, 330, 330, 150, 210, mix(BG, MUTED, b), 3)
    c.arrow(800 - 330 * math.cos(math.radians(30)), 560 + 330 * math.sin(math.radians(30)) - 10, 800 - 330 * math.cos(math.radians(30)) - 6, 560 + 330 * math.sin(math.radians(30)) + 20, mix(BG, MUTED, b), 3, 14)
    c.text(400, 820, '船头往这边转', 'sans', 24, mix(BG, INK, b), 'mm')
    c.text(1500, 900, '（俯视图，船向左开）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 5, '船往前开，水就从船头流向船尾'),
                (5.2, 12, '舵一偏，水流撞在斜着的舵板上，把船尾推向一边'),
                (12.2, 22, '船绕着重心转：船尾往一边去，船头就往另一边拐。舵不用划，靠的是水流的力')], y=1010)

def b44_angle(c, t, i):
    corner_tag(c, 'B44 · 舵打多少度')
    c.text(60, 96, '舵角太小拐不动，太大只剩刹车', 'serif', 40, INK)
    angs = [0, 15, 30, 60]
    side = [0.0, 0.7, 1.0, 0.45]
    drag = [0.1, 0.25, 0.5, 1.0]
    for k, g in enumerate(angs):
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        if a <= 0: continue
        x = 330 + k * 400
        r = math.radians(90 + g)
        c.line([(x, 260), (x + 110 * math.cos(r), 260 + 110 * math.sin(r))], mix(BG, SPARK, a), 10)
        c.text(x, 420, f'{g}°', 'mono', 34, mix(BG, INK, a), 'mm')
        g1 = fade(t, 2 + k * 2.5, 3.5 + k * 2.5)
        h1, h2 = 300 * side[k] * g1, 300 * drag[k] * g1
        c.rect(x - 80, 860 - h1, x - 5, 860, fill=mix(BG, GREEN, a), r=4)
        c.rect(x + 5, 860 - h2, x + 80, 860, fill=mix(BG, NRED, a), r=4)
    c.line([(200, 860), (1760, 860)], LINE, 2)
    c.rect(1380, 150, 1840, 210, fill=SHEET, r=8)
    c.text(1400, 180, '■', 'sans', 22, GREEN, 'lm'); c.text(1430, 180, '侧推力', 'sans', 22, INK, 'lm')
    c.text(1560, 180, '■', 'sans', 22, NRED, 'lm'); c.text(1590, 180, '阻力（示意）', 'sans', 22, INK, 'lm')
    caps(c, t, [(0, 6, '舵角从零慢慢加大，侧推力跟着变大，船拐得越来越急'),
                (6.2, 14, '可角度太大，水流在舵板背面乱成一团：侧推力反而变小，阻力却一直涨'),
                (14.2, 22, '这和 B40 竹蜻蜓叶片的失速是同一回事：最好的舵角以实测为准')], y=1010)

# ---------------------------------------------------------------- B45 扎染
def b45_capillary(c, t, i):
    corner_tag(c, 'B45 · 染料顺着纤维爬')
    c.text(60, 96, '扎得越紧，染料能钻进去的缝越少', 'serif', 40, INK)
    for k, (nm, gap) in enumerate([('不扎', 1.0), ('扎松', 0.5), ('扎紧', 0.12)]):
        x0 = 160 + k * 580
        a = fade(t, 1 + k * 3, 2 + k * 3)
        if a <= 0: continue
        c.text(x0 + 230, 200, nm, 'bold', 30, mix(BG, INK, a), 'mm')
        c.rect(x0, 240, x0 + 460, 760, fill=mix(BG, CLOTH, a * 0.25), r=8)
        n = 9
        mid = 500
        for j in range(n):
            xx = x0 + 30 + j * 50
            squeeze = (1 - gap) * (xx - (x0 + 230)) * 0.6
            pts = []
            for q in range(21):
                y = 260 + q * 24
                w = math.exp(-((y - mid) / 70) ** 2)
                pts.append((xx - squeeze * w, y))
            c.line(pts, mix(BG, CLOTH, a), 6)
        # dye level creeping from top and bottom
        prog = fade(t, 2 + k * 3, 12)
        reach = 260 * prog
        stop = 230 - 200 * (1 - gap)
        r_ = min(reach, max(stop, 0) if prog > 0.5 else reach)
        dep = min(reach, 260 - 210 * (1 - gap))
        c.rect(x0 + 10, 250, x0 + 450, 250 + dep, fill=mix(BG, INDIGO, 0.55 * a), r=6)
        c.rect(x0 + 10, 750 - dep, x0 + 450, 750, fill=mix(BG, INDIGO, 0.55 * a), r=6)
        if dep >= 250: c.rect(x0 + 10, 250, x0 + 450, 750, fill=mix(BG, INDIGO, 0.55 * a), r=6)
        if gap < 1:
            c.rect(x0 - 10, mid - 12, x0 + 470, mid + 12, fill=mix(BG, NRED, a * (1.2 - gap)), r=4)
        white = max(0, 500 - 2 * dep)
        c.text(x0 + 230, 810, f'留白约 {white / 500 * 100:.0f}%（示意）', 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '棉纤维之间有无数细缝，染料顺着细缝往里爬：这是毛细作用'),
                (6.2, 13, '用绳子扎紧，纤维被挤在一起，细缝几乎被压死'),
                (13.2, 22, '染料爬不进去，那里就留下一圈白花：扎得越紧，留白越清楚（以实测为准）')], y=1010)

def b45_indigo(c, t, i):
    corner_tag(c, 'B45 · 靛蓝：先变黄绿，再变蓝')
    c.text(60, 96, '靛蓝不溶于水：要先「还原」，再靠空气「氧化」', 'serif', 40, INK)
    steps = [('靛蓝（蓝色）', INDIGO, '不溶于水，钻不进纤维'), ('还原后（黄绿色）', LEUCO, '溶于水，钻进纤维'), ('出水晾在空气里', INDIGO, '被氧气氧化，变回蓝色，卡在纤维里')]
    for k, (nm, col, note) in enumerate(steps):
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        x = 330 + k * 630
        c.rect(x - 200, 260, x + 200, 560, fill=mix(BG, col, a), r=16)
        c.text(x, 610, nm, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(x, 660, note, 'sans', 24, mix(BG, MUTED, a), 'mm')
        if k:
            c.arrow(x - 400, 410, x - 230, 410, mix(BG, MUTED, a), 5, 18)
    c.text(645, 360, '还原', 'bold', 26, mix(BG, INK, fade(t, 6, 7)), 'mm')
    c.text(1275, 360, '氧化', 'bold', 26, mix(BG, INK, fade(t, 11, 12)), 'mm')
    d = fade(t, 15, 16)
    c.rect(260, 760, 1660, 880, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 800, '古法：蓝靛加石灰、酒糟或糖发酵，让细菌帮忙还原（拍摄前核对）', 'sans', 26, mix(BG, INK, d), 'mm')
    c.text(960, 845, '本集用成品靛蓝套装：还原剂由成年人按说明操作、通风', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '靛蓝本身不溶于水，直接泡，颜色只浮在布面上，一洗就掉'),
                (6.2, 12, '先把它还原成黄绿色的「隐色靛蓝」：能溶于水，钻进纤维里'),
                (12.2, 22, '布一出水，空气里的氧把它变回蓝色，牢牢卡在纤维里：所以扎染是越晾越蓝')], y=1010)

CLIPS = {
 'B43_力矩': (b43_moment, 22), 'B43_刻度': (b43_scale, 22),
 'B43_片头': (titles.opening(BSER, VOL14, SB14, 3, '战国已有衡器 · 杆秤与定盘星'), 7),
 'B43_片尾': (titles.closing(BSER, VOL14, SB14, 3, '下集：船尾一块板，怎么让大船拐弯？'), 7),
 'B44_侧力': (b44_force, 22), 'B44_舵角': (b44_angle, 22),
 'B44_片头': (titles.opening(BSER, VOL14, SB14, 4, '东汉 · 陶船模型上的舵'), 7),
 'B44_片尾': (titles.closing(BSER, VOL14, SB14, 4, '下集：扎紧的地方，为什么染不上颜色？'), 7),
 'B45_毛细': (b45_capillary, 22), 'B45_靛蓝': (b45_indigo, 22),
 'B45_片头': (titles.opening(BSER, VOL14, SB14, 5, '东晋—唐 · 绞缬'), 7),
 'B45_片尾': (titles.closing(BSER, VOL14, SB14, 5, '下集：一堆土，为什么夯一夯就能筑城墙？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
