"""第二十九季（第十一层：家里的机器）第一批：E152 拉链、E153 缝纫机、E154 洗衣机甩干 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S29A = [('152', '拉链'), ('153', '缝纫机'), ('154', '洗衣机甩干'), ('155', '压力锅'), ('156', '电饭煲'),
        ('157', '电磁炉'), ('158', '吸尘器'), ('159', '烟雾报警器'), ('160', '电子秤'), ('161', '扫地机器人')]
SER29, VOL29 = '从零造物', '第二十九季 · 第十一层：家里的机器'
TOOTH = (200, 205, 215)
CLOTH_L = (110, 150, 210)
CLOTH_R = (210, 130, 110)
THREAD_R = (230, 90, 90)
THREAD_B = (90, 140, 230)
METAL = (170, 175, 185)
WATER_L = (110, 170, 230)


# ---------------------------------------------------------------- E152 拉链
def e152_slider(c, t, i):
    corner_tag(c, '第 152 集 · 拉头是一个 Y 形的楔子')
    c.text(60, 96, '拉头里是一条 Y 形通道：往上拉，两排齿被斜着挤到一起互相钩住；往下拉，中间的楔子把它们一个个撬开', 'serif', 36, INK)
    cx = 960
    sy = 300 + 400 * (0.5 - 0.5 * math.cos(t / 11 * 2 * math.pi))
    pitch = 34
    for k in range(-1, 20):
        y = 220 + k * pitch
        if y < sy:
            off = 0
        else:
            off = min(1, (y - sy) / 160) * 120
        for side, col in ((-1, CLOTH_L), (1, CLOTH_R)):
            x = cx + side * (16 + off)
            c.rect(x - 160 * (side > 0) - (0 if side > 0 else 0), y - 12, x + (0 if side < 0 else 160), y + 12, fill=mix(BG, col, 0.5)) if False else None
            c.rect(x + (-200 if side < 0 else 30), y - 14, x + (-30 if side < 0 else 200), y + 14, fill=mix(BG, col, 0.55))
            ty = y + (pitch / 2 if side > 0 else 0)
            c.rect(x - 22, ty - 9, x + 22, ty + 9, fill=TOOTH, r=4)
            c.ellipse(x - side * 18, ty, 7, 7, fill=mix(TOOTH, BG, 0.2))
    c.poly([(cx - 90, sy - 70), (cx + 90, sy - 70), (cx + 60, sy + 70), (cx + 10, sy + 70), (cx, sy + 30), (cx - 10, sy + 70), (cx - 60, sy + 70)], mix(METAL, BG, 0.1))
    c.rect(cx - 12, sy - 150, cx + 12, sy - 70, fill=METAL, r=4)
    c.text(cx + 130, sy - 40, '拉头', 'bold', 24, INK, 'lm')
    c.text(cx + 130, sy + 10, '中间的小楔子把齿撬开', 'sans', 20, MUTED, 'lm')
    c.text(cx - 380, 400, '咬合', 'bold', 24, GREEN, 'mm')
    c.text(cx - 380, 860, '分开', 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '拉链的两排小齿，每个齿上面有个小凸起、下面有个小凹窝'),
                (7.2, 14, '拉头里面是一条 Y 形的通道：往上拉，两排齿被斜着挤到一起，凸起一个个钻进对面的凹窝'),
                (14.2, 22, '往下拉，拉头中间的小楔子从中间顶进去，把齿一个一个撬开（示意）')], y=1010)


def e152_force(c, t, i):
    corner_tag(c, '第 152 集 · 一次撬一个，比一起掰省力得多')
    c.text(60, 96, '直接往外掰，几十个齿要同时脱钩，很费劲；拉头每一刻只撬开一两个齿，楔子还把力放大，轻轻一拉就开', 'serif', 36, INK)
    for row, (lab, n_load, F) in enumerate((('直接往两边掰', 20, 1.0), ('用拉头往下拉', 2, 0.1))):
        y = 360 + row * 300
        c.text(160, y - 110, lab, 'bold', 26, INK, 'lm')
        for k in range(20):
            x = 300 + k * 50
            on = (k < n_load) if row == 0 else (k in (int(t * 2) % 20, (int(t * 2) + 1) % 20))
            c.rect(x - 16, y - 30, x + 16, y - 4, fill=TOOTH, r=3)
            c.rect(x + 9, y + 4, x + 41, y + 30, fill=TOOTH, r=3)
            if on:
                c.ellipse(x + 12, y, 10, 10, fill=NRED)
        bw = 360 * F * min(1, t / 6)
        c.rect(1340, y - 20, 1340 + bw, y + 20, fill=NRED if row == 0 else GREEN, r=6)
        c.text(1350 + bw, y, '要的力（示意）', 'sans', 20, MUTED, 'lm')
    c.text(960, 900, '红点：正在受力、要脱钩的齿', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '用手抓住两边的布直接往外掰：几十个齿同时被拉，每一个都要从凹窝里拔出来'),
                (7.2, 14, '拉头每一刻只撬开最前面的一两个齿，一个接一个'),
                (14.2, 22, '楔子越长越尖，用的力越小：一个小小的拉头，就把「大力气」换成了「多走几步」（倍数以实测为准）')], y=1010)


# ---------------------------------------------------------------- E153 缝纫机
def e153_lock(c, t, i):
    corner_tag(c, '第 153 集 · 针眼在针尖，下面有个梭子')
    c.text(60, 96, '缝纫机的针眼开在针尖：针把上线带到布下面，留出一个线圈，梭子的钩子一勾，把下线穿过线圈，两根线就在布里锁住了', 'serif', 34, INK)
    cloth_y = 520
    c.rect(200, cloth_y - 14, 1500, cloth_y + 14, fill=mix(BG, CLOTH_L, 0.6))
    ph = (t % 4) / 4
    nx = 900
    depth = 160 * math.sin(math.pi * ph) if ph < 1 else 0
    tip = cloth_y + depth - 40
    c.line([(nx, 200), (nx, tip)], METAL, 8)
    c.ellipse(nx, tip - 10, 4, 8, fill=BG)
    c.line([(nx, 200), (nx, tip - 10)], THREAD_R, 3)
    if ph > 0.35 and ph < 0.9:
        loop = 50 * math.sin(math.pi * (ph - 0.35) / 0.55)
        c.ellipse(nx + loop * 0.6, tip + 10, max(4, loop), 30, outline=THREAD_R, width=3)
    hx, hy = nx + 40, cloth_y + 160
    c.ellipse(hx, hy, 70, 70, outline=METAL, width=6)
    ang = ph * 2 * math.pi * 2
    c.line([(hx, hy), (hx + 70 * math.cos(ang), hy + 70 * math.sin(ang))], METAL, 6)
    c.ellipse(hx, hy, 24, 24, fill=mix(BG, THREAD_B, 0.6))
    c.text(hx + 110, hy, '梭子（里面卷着下线）', 'sans', 20, THREAD_B, 'lm')
    n = int(t / 4)
    for k in range(min(n, 12)):
        x = nx - 60 * (k + 1)
        c.line([(x, cloth_y - 14), (x + 60, cloth_y - 14)], THREAD_R, 4)
        c.line([(x, cloth_y + 14), (x + 60, cloth_y + 14)], THREAD_B, 4)
        c.ellipse(x, cloth_y, 6, 10, fill=mix(THREAD_R, THREAD_B, 0.5))
    c.text(nx - 400, cloth_y - 70, '红：上线　蓝：下线　紫点：两线锁在布中间', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '手缝时，针带着线整根穿过布；缝纫机的针只上下戳，针眼开在针尖'),
                (7.2, 14, '针扎下去再往上抬一点，上线在布下面留出一个小线圈；下面转动的梭子钩子正好勾住它'),
                (14.2, 22, '钩子带着线圈绕过梭子，下线就从线圈里穿了过去：一上一下两根线，在布的中间锁住（示意）')], y=1010)


def e153_unravel(c, t, i):
    corner_tag(c, '第 153 集 · 一根线一拉就散，两根线锁住不散')
    c.text(60, 96, '单线的链式线迹像一串钩针：拉住线头，一圈圈全解开；双线锁式线迹每一针都在布里互相套住，拉一头也散不开', 'serif', 36, INK)
    pull = min(1, max(0, (t - 5) / 10))
    for row, (lab, chain) in enumerate((('单线链式', True), ('双线锁式', False))):
        y = 400 + row * 300
        c.rect(200, y - 12, 1500, y + 12, fill=mix(BG, CLOTH_L, 0.6))
        c.text(200, y - 90, lab, 'bold', 26, INK, 'lm')
        nst = 12
        undone = int(pull * nst) if chain else 0
        for k in range(nst):
            x = 260 + k * 100
            if chain:
                if k < undone:
                    c.line([(x, y - 12), (x + 100, y - 12 - 30 * (undone - k) / nst)], mix(THREAD_R, BG, 0.4), 3)
                else:
                    c.ellipse(x + 50, y + 34, 50, 18, outline=THREAD_R, width=3)
                    c.line([(x, y - 12), (x + 100, y - 12)], THREAD_R, 3)
            else:
                c.line([(x, y - 12), (x + 100, y - 12)], THREAD_R, 4)
                c.line([(x, y + 12), (x + 100, y + 12)], THREAD_B, 4)
                c.ellipse(x, y, 6, 10, fill=mix(THREAD_R, THREAD_B, 0.5))
        c.arrow(200, y - 12, 200 - 120 * pull, y - 12, SPARK, 4, 14)
        res = f'散了 {undone} 针' if chain else '一针也没散'
        c.text(1560, y, res, 'bold', 24, NRED if chain else GREEN, 'lm')
    caps(c, t, [(0, 7, '用一根线做链式线迹：每一针都是一个线圈套着下一个线圈'),
                (7.2, 14, '找到线头一拉，线圈一个接一个松开，整条线迹全散了：有的米袋口就是这样一拉就开'),
                (14.2, 22, '两根线的锁式线迹，每一针都在布里互相套住：拉一头，最多拉紧一点，散不开（示意）')], y=1010)


# ---------------------------------------------------------------- E154 洗衣机甩干
def e154_tangent(c, t, i):
    corner_tag(c, '第 154 集 · 桶壁逼它转圈，水想走直线')
    c.text(60, 96, '从上往下看：衣服被桶壁拦着，只能跟着转圈；水滴一到孔边，没人拦了，就沿着那一刻的方向直直地飞出去', 'serif', 36, INK)
    cx, cy, R = 760, 560, 300
    w = 1.6
    c.ellipse(cx, cy, R, R, outline=METAL, width=10)
    holes = 24
    for k in range(holes):
        a = 2 * math.pi * k / holes + t * w
        c.ellipse(cx + R * math.cos(a), cy + R * math.sin(a), 8, 8, fill=BG)
    for k in range(5):
        a = t * w + k * 1.25
        c.ellipse(cx + (R - 50) * math.cos(a), cy + (R - 50) * math.sin(a), 46, 30, fill=mix(BG, (200, 160, 220), 0.7))
    rnd = random.Random(4)
    for k in range(10):
        t0 = k * 1.9 + 0.4
        if t < t0:
            continue
        a0 = t0 * w + rnd.uniform(0, 6.28)
        px, py = cx + R * math.cos(a0), cy + R * math.sin(a0)
        vx, vy = -math.sin(a0), math.cos(a0)
        d = (t - t0) * 320
        if d < 620:
            c.ellipse(px + vx * d, py + vy * d, 8, 8, fill=WATER_L)
            seg(c, [(px, py), (px + vx * d, py + vy * d)], mix(BG, WATER_L, 0.5), 2)
    c.rect(1240, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1550, 340, '水滴飞出去的方向', 'bold', 24, INK, 'mm')
    c.text(1550, 410, '是圆的切线：', 'sans', 22, INK, 'mm')
    c.text(1550, 450, '离开那一刻往哪走，', 'sans', 22, INK, 'mm')
    c.text(1550, 490, '就一直往哪走', 'sans', 22, INK, 'mm')
    c.text(1550, 580, '不是被「甩」向外，而是没被拦住', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '洗衣机甩干时，内桶飞快地转，桶壁上有一圈圈小孔'),
                (7.2, 14, '衣服太大，钻不出小孔，只能被桶壁推着一圈圈转；水滴却很小，一到孔边就钻了出去'),
                (14.2, 22, '钻出去以后没人推它拐弯了，它就沿着那一刻的方向直直地飞向外桶（示意）')], y=1010)


def e154_speed(c, t, i):
    corner_tag(c, '第 154 集 · 转得快一倍，甩水的劲大四倍')
    c.text(60, 96, '要让水跟着转圈，桶壁得一直推它；转得越快需要的推力越大，水越容易从孔里跑掉：速度翻倍，力变四倍', 'serif', 36, INK)
    speeds = [(1, '慢'), (2, '快一倍'), (3, '快两倍')]
    grow = min(1, t / 8)
    gx0, gy0 = 260, 860
    c.line([(gx0, gy0), (1300, gy0)], LINE, 2)
    for k, (s, lab) in enumerate(speeds):
        x = gx0 + 80 + k * 330
        h = 480 * (s * s) / 9 * grow
        c.rect(x, gy0 - h, x + 200, gy0, fill=mix(WATER_L, NRED, k / 2), r=8)
        c.text(x + 100, gy0 + 40, lab, 'bold', 24, INK, 'mm')
        c.text(x + 100, gy0 - h - 30, f'× {s * s}', 'mono', 28, INK, 'mm')
        a = t * 2 * s
        c.ellipse(x + 100, 230, 40, 40, outline=METAL, width=4)
        c.ellipse(x + 100 + 40 * math.cos(a), 230 + 40 * math.sin(a), 8, 8, fill=WATER_L)
    c.rect(1420, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1640, 340, '洗衣机的甩干', 'bold', 24, INK, 'mm')
    c.text(1640, 410, '每分钟上千转', 'sans', 22, INK, 'mm')
    c.text(1640, 460, '（转速以说明书为准）', 'sans', 18, MUTED, 'mm')
    c.text(1640, 540, '转速越高，甩得越干', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '用沙拉甩干器甩一条湿毛巾：慢慢转，水只滴下来一点；转快一倍，甩出来的多得多'),
                (7.2, 14, '让东西转圈需要的力，和转速的平方成正比：快一倍，要四倍的力；快两倍，要九倍'),
                (14.2, 22, '洗衣机甩干时转得飞快，桶壁根本「留不住」水：所以甩完的衣服只是潮潮的（倍数为理论示意）')], y=1010)


CLIPS = {
 'E152_楔形': (e152_slider, 22), 'E152_省力': (e152_force, 22),
 'E152_片头': (titles.opening(SER29, VOL29, S29A, 0, '1913 年桑德贝克改进拉链'), 7),
 'E152_片尾': (titles.closing(SER29, VOL29, S29A, 0, '下集：缝纫机的针为什么不用穿过布，就能一秒缝好几针？'), 7),
 'E153_锁线': (e153_lock, 22), 'E153_散不散': (e153_unravel, 22),
 'E153_片头': (titles.opening(SER29, VOL29, S29A, 1, '1846 年豪威获得锁式缝纫机专利'), 7),
 'E153_片尾': (titles.closing(SER29, VOL29, S29A, 1, '下集：洗衣机一转，湿衣服里的水为什么就被甩出去了？'), 7),
 'E154_切线': (e154_tangent, 22), 'E154_转速': (e154_speed, 22),
 'E154_片头': (titles.opening(SER29, VOL29, S29A, 2, '1908 年前后电动洗衣机出现'), 7),
 'E154_片尾': (titles.closing(SER29, VOL29, S29A, 2, '下集：压力锅为什么能把肉炖得烂烂的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
