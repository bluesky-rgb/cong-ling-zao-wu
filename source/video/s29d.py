"""第二十九季（第十一层：家里的机器）收官：E161 扫地机器人 + 第二十九季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import S29A, SER29, VOL29, METAL, WATER_L

ROBOT = (90, 100, 120)
CLEAN = (110, 170, 130)


def _random_path(n=50, N=10, seed=3):
    rnd = random.Random(seed)
    x, y = 0, 0
    path = [(x, y)]
    while len(path) <= n:
        d = rnd.randint(1, 6)
        if d > 4:
            continue
        dx, dy = [(0, -1), (0, 1), (1, 0), (-1, 0)][d - 1]
        if 0 <= x + dx < N and 0 <= y + dy < N:
            x, y = x + dx, y + dy
        path.append((x, y))
    return path


def _snake_path(n=50, N=10):
    path = []
    for row in range(N):
        cols = range(N) if row % 2 == 0 else range(N - 1, -1, -1)
        for col in cols:
            path.append((col, row))
    return path[:n + 1]


RP = _random_path()
SP = _snake_path()


# ---------------------------------------------------------------- E161 扫地机器人
def e161_walk(c, t, i):
    corner_tag(c, '第 161 集 · 乱走和弓字形，同样 50 步')
    c.text(60, 96, '10 × 10 的方格当房间：一个掷骰子乱走，一个一行一行来回扫；走同样 50 步，看谁扫过的格子多', 'serif', 38, INK)
    steps = int(min(50, max(0, (t - 1) * 3)))
    for k, (lab, path) in enumerate((('掷骰子乱走', RP), ('弓字形来回扫', SP))):
        x0, y0, cs = 210 + k * 860, 250, 60
        seen = set(path[:steps + 1])
        for gx in range(10):
            for gy in range(10):
                fill = mix(BG, CLEAN, 0.7) if (gx, gy) in seen else SHEET
                c.rect(x0 + gx * cs, y0 + gy * cs, x0 + gx * cs + cs - 4, y0 + gy * cs + cs - 4, fill=fill, r=4)
        pts = [(x0 + px * cs + cs / 2 - 2, y0 + py * cs + cs / 2 - 2) for (px, py) in path[:steps + 1]]
        if len(pts) > 1:
            c.line(pts, mix(BG, SPARK, 0.6), 3)
        rx, ry = pts[-1]
        c.ellipse(rx, ry, 20, 20, fill=ROBOT, outline=INK, width=2)
        c.text(x0 + 300, y0 - 40, lab, 'bold', 28, INK, 'mm')
        c.text(x0 + 300, y0 + 640, f'走了 {steps} 步，扫过 {len(seen)} 格', 'mono', 24, SPARK if k == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '把房间画成 10 × 10 的方格，扫地机器人从左上角出发，每一步走一格'),
                (7.2, 14, '左边掷骰子决定方向，经常走回扫过的地方；右边一行一行来回扫，每一步都是新格子'),
                (14.2, 22, '同样走 50 步，乱走只扫到十几格，弓字形每一步都是新格子：会规划路线，省下大半力气（以实际掷骰子为准）')], y=1010)


def e161_map(c, t, i):
    corner_tag(c, '第 161 集 · 先撞一撞，再画一张地图')
    c.text(60, 96, '机器人前面有碰撞板、底下有防跌落的探头；有的还会转着圈用激光量距离，一边扫一边把房间画成地图', 'serif', 38, INK)
    x0, y0, x1, y1 = 260, 260, 1100, 880
    reveal = min(1, t / 16)
    c.rect(x0, y0, x1, y1, outline=mix(BG, LINE, 0.3), width=2)
    walls = [((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0)),
             ((620, y0), (620, 520)), ((820, 700), (x1, 700))]
    sofa = (380, 640, 540, 760)
    rx = 420 + 340 * (0.5 - 0.5 * math.cos(t * 0.5))
    ry = 420 + 120 * math.sin(t * 0.35)
    ang = t * 3
    for (a, b) in walls:
        c.line([a, b], mix(BG, INK, 0.15 + 0.85 * reveal), 6)
    c.rect(*sofa, fill=mix(BG, (150, 120, 90), 0.2 + 0.6 * reveal), r=10)
    c.text((sofa[0] + sofa[2]) / 2, (sofa[1] + sofa[3]) / 2, '沙发', 'sans', 20, INK, 'mm')
    lx, ly = rx + 900 * math.cos(ang), ry + 900 * math.sin(ang)
    c.line([(rx, ry), (rx + 120 * math.cos(ang), ry + 120 * math.sin(ang))], NRED, 2)
    c.ellipse(rx, ry, 34, 34, fill=ROBOT, outline=INK, width=2)
    c.arc(rx, ry, 34, 34, -60, 60, SPARK, 6)
    c.ellipse(rx, ry, 8, 8, fill=NRED)
    mx0, my0 = 1260, 300
    c.rect(mx0, my0, 1840, 840, fill=SHEET, r=14)
    c.text(1550, my0 + 36, '机器人画出的地图', 'bold', 24, INK, 'mm')
    sc = 0.6
    for (a, b) in walls:
        pa = (mx0 + 40 + (a[0] - x0) * sc, my0 + 80 + (a[1] - y0) * sc)
        pb = (mx0 + 40 + (b[0] - x0) * sc, my0 + 80 + (b[1] - y0) * sc)
        n = 12
        for j in range(int(n * reveal) + 1):
            u = j / n
            c.ellipse(pa[0] + (pb[0] - pa[0]) * u, pa[1] + (pb[1] - pa[1]) * u, 4, 4, fill=NRED)
    c.ellipse(mx0 + 40 + (rx - x0) * sc, my0 + 80 + (ry - y0) * sc, 10, 10, fill=ROBOT)
    c.text(1550, 800, '红点：激光量到的墙（示意）', 'sans', 18, MUTED, 'mm')
    c.text(680, 930, '黄弧：前面的碰撞板　红线：转动的激光测距', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '最简单的扫地机器人，前面有一块会被撞进去的碰撞板，碰到墙就转个方向'),
                (7.2, 14, '底下还有朝下看的探头，一看到台阶边是空的就停住，免得摔下去'),
                (14.2, 22, '高级一点的会转着圈用激光量四周的距离，一边走一边画出地图，再按地图规划一行一行扫（示意）')], y=1010)


# ---------------------------------------------------------------- 第二十九季特辑
OLD29 = [('螺丝与标准件', '64'), ('齿轮与轴承', '41'), ('曲柄连杆', '40'), ('纺锤', 'B70'), ('电动机', '58'), ('温度计', '46'),
         ('罐藏', '37'), ('电磁铁', '56'), ('磁生电', '04'), ('变压器与交流电', '75'), ('虹吸', '26'), ('LED', '102'),
         ('开关与逻辑门', '81'), ('杆秤', 'B43'), ('晶体管', '92'), ('人工智能', '111')]
NEW29 = [('拉链', '152', ['螺丝与标准件', '齿轮与轴承']), ('缝纫机', '153', ['曲柄连杆', '纺锤']), ('洗衣机甩干', '154', ['电动机', '齿轮与轴承']),
         ('压力锅', '155', ['温度计', '罐藏']), ('电饭煲', '156', ['电磁铁', '温度计']), ('电磁炉', '157', ['磁生电', '变压器与交流电']),
         ('吸尘器', '158', ['电动机', '虹吸']), ('烟雾报警器', '159', ['LED', '开关与逻辑门']), ('电子秤', '160', ['杆秤', '晶体管']),
         ('扫地机器人', '161', ['吸尘器', '人工智能'])]


def s29_layer(c, t, i):
    corner_tag(c, '第二十九季特辑 · 第十一层')
    c.text(60, 118, '第十一层：家里的机器', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD29):
        pos[name] = (340, 200 + k * 46)
    for k, (name, num, deps) in enumerate(NEW29):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第二十九季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW29):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if x0 > 900:
                sx = x0 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD29:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 7 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW29):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 20, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十一层的十集：家里那些天天在用的机器'),
                (8.2, 16, '标准件长出拉链，曲柄和纺锤长出缝纫机，电动机长出洗衣机甩干，温度计长出压力锅和电饭煲'),
                (16.2, 24, '磁生电长出电磁炉，虹吸长出吸尘器，LED 长出烟雾报警器，杆秤和晶体管长出电子秤'),
                (24.2, 30, '最后，吸尘器装上了人工智能，自己满屋子跑：扫地机器人')], y=1040)


CLIPS = {
 'E161_两种走法': (e161_walk, 22), 'E161_地图': (e161_map, 22),
 'E161_片头': (titles.opening(SER29, VOL29, S29A, 9, '2002 年家用扫地机器人上市'), 7),
 'E161_片尾': (titles.closing(SER29, VOL29, S29A, 9, '下集：第二十九季特辑 · 第十一层回顾'), 7),
 'S29_第十一层': (s29_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
