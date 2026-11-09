"""第三十三季（第十三层：跑起来的机器）收官：E181 自动驾驶 + 第三十三季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L
from s33a import S33A, SER33, VOL33, CARC

LIDAR = (230, 90, 90)
OBST = (120, 110, 100)

GRID = ["########",
        "#S..#..#",
        "#.#.#.##",
        "#.#...G#",
        "#.####.#",
        "#......#",
        "########"]


def _walk():
    pos = None
    for r, row in enumerate(GRID):
        for c_, ch in enumerate(row):
            if ch == 'S':
                pos = (r, c_)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    path = [(pos, d)]
    for _ in range(60):
        r, c_ = pos
        if GRID[r][c_] == 'G':
            break
        right = (d + 1) % 4
        order = [right, d, (d + 3) % 4, (d + 2) % 4]
        for nd in order:
            dr, dc = dirs[nd]
            if GRID[r + dr][c_ + dc] != '#':
                d = nd
                pos = (r + dr, c_ + dc)
                break
        path.append((pos, d))
    return path


PATH = _walk()


# ---------------------------------------------------------------- E181 自动驾驶
def e181_loop(c, t, i):
    corner_tag(c, '第 181 集 · 看、想、动，一秒几十遍')
    c.text(60, 96, '自动驾驶不停地转一个圈：看周围 → 判断在哪、旁边有什么 → 按地图和规则决定 → 控制方向盘', 'serif', 36, INK)
    cx, cy = 560, 580
    c.rect(100, 300, 1020, 860, fill=mix(BG, (60, 64, 70), 0.6), r=10)
    for k in range(3):
        c.rect(100, 420 + k * 160, 1020, 424 + k * 160, fill=(200, 200, 200))
    carx = 300 + (t * 25) % 500
    c.rect(carx - 60, cy - 30, carx + 60, cy + 30, fill=CARC, r=10)
    for k in range(24):
        a = t * 3 + k * 2 * math.pi / 24
        L = 200
        ox, oy = 760, 450
        ex, ey = carx + L * math.cos(a), cy + L * math.sin(a)
        c.line([(carx, cy), (ex, ey)], mix(BG, LIDAR, 0.35), 1)
    c.rect(720, 420, 820, 480, fill=OBST, r=8)
    c.text(770, 400, '前车', 'sans', 18, MUTED, 'mm')
    steps = ['看：摄像头、雷达、激光', '想：我在哪？旁边有什么？', '定：减速、变道还是停', '动：转向、油门、刹车']
    k = int(t * 1.2) % 4
    for j, s in enumerate(steps):
        x, y = 1440, 330 + j * 140
        c.rect(x - 320, y - 46, x + 320, y + 46, fill=mix(SHEET, SPARK, 0.35) if j == k else SHEET, outline=SPARK if j == k else LINE, width=2, r=12)
        c.text(x, y, s, 'bold', 24, INK, 'mm')
        if j < 3:
            c.arrow(x, y + 50, x, y + 90, MUTED, 3, 10)
    c.arrow(x + 330, 330 + 3 * 140, x + 330, 330, MUTED, 3, 12)
    caps(c, t, [(0, 7, '车顶的激光雷达一圈圈扫，摄像头和雷达一起看：前面有车，旁边有线'),
                (7.2, 14, '电脑把看到的东西和地图对上，算出自己在哪一条车道、前车多远'),
                (14.2, 22, '再按规则决定减速还是变道，控制方向盘和刹车；这个圈一秒钟要转几十遍（示意）')], y=1010)


def e181_rules(c, t, i):
    corner_tag(c, '第 181 集 · 只按规则走，也能找到出口')
    c.text(60, 96, '「车」看不见整张图，只知道前、左、右有没有墙，按一张规则卡一步步走', 'serif', 36, INK)
    cs = 90
    x0, y0 = 300, 290
    for r, row in enumerate(GRID):
        for c_, ch in enumerate(row):
            x, y = x0 + c_ * cs, y0 + r * cs
            if ch == '#':
                c.rect(x, y, x + cs - 4, y + cs - 4, fill=OBST, r=6)
            else:
                c.rect(x, y, x + cs - 4, y + cs - 4, fill=SHEET, r=6)
            if ch == 'G':
                c.text(x + cs / 2, y + cs / 2, '终点', 'bold', 20, GREEN, 'mm')
    n = min(len(PATH) - 1, int(t * 1.6))
    pts = [(x0 + p[1] * cs + cs / 2 - 2, y0 + p[0] * cs + cs / 2 - 2) for p, d in PATH[:n + 1]]
    if len(pts) > 1:
        c.line(pts, mix(BG, SPARK, 0.6), 5)
    (r, c_), d = PATH[n]
    px, py = x0 + c_ * cs + cs / 2 - 2, y0 + r * cs + cs / 2 - 2
    c.ellipse(px, py, 26, 26, fill=CARC)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dx, dy = dirs[d]
    c.arrow(px, py, px + dx * 34, py + dy * 34, INK, 4, 12)
    c.rect(1150, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1505, 350, '规则卡', 'bold', 26, INK, 'mm')
    for j, s in enumerate(['1. 右边空 → 右转', '2. 前面空 → 直走', '3. 左边空 → 左转', '4. 都堵 → 掉头']):
        c.text(1220, 410 + j * 50, s, 'sans', 22, INK, 'lm')
    done = GRID[r][c_] == 'G'
    c.text(1505, 720, f'走了 {n} 步' + ('，到了！' if done else ''), 'mono', 30, GREEN if done else SPARK, 'mm')
    caps(c, t, [(0, 7, '「车」被蒙住眼睛，只靠旁边的人报告：前面、左边、右边有没有墙'),
                (7.2, 14, '它只按一张规则卡走，一步一步，碰到死胡同就掉头'),
                (14.2, 22, '没有看整张地图，也到了终点；真正的自动驾驶，规则和判断要复杂成千上万倍（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十三季特辑
OLD33 = [('杠杆与滑轮组', '39'), ('自行车', '66'), ('电梯与安全钳', '87'), ('摆钟', '45'), ('手机里的陀螺仪', '108'), ('热气球', '44'),
         ('齿轮与轴承', '41'), ('曲柄连杆', '40'), ('电动机', '58'), ('逆风航行', '43'), ('机翼', '86'), ('腰舟', 'B139'),
         ('船闸', '122'), ('直升机', '100'), ('磁悬浮', '99'), ('人工智能', '111'), ('地图导航', '171')]
NEW33 = [('液压刹车', '172', ['杠杆与滑轮组', '自行车']), ('安全带', '173', ['电梯与安全钳', '摆钟']), ('安全气囊', '174', ['手机里的陀螺仪', '热气球']),
         ('差速器', '175', ['齿轮与轴承', '自行车']), ('雨刮器', '176', ['曲柄连杆', '电动机']), ('螺旋桨', '177', ['逆风航行', '机翼']),
         ('潜水艇', '178', ['腰舟', '船闸']), ('气垫船', '179', ['直升机', '磁悬浮']), ('降落伞', '180', ['热气球', '机翼']),
         ('自动驾驶', '181', ['人工智能', '地图导航'])]


def s33_layer(c, t, i):
    corner_tag(c, '第三十三季特辑 · 第十三层')
    c.text(60, 118, '第十三层：跑起来的机器', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD33):
        pos[name] = (340, 210 + k * 46)
    for k, (name, num, deps) in enumerate(NEW33):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 165, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十三季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW33):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD33:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 6 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW33):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十三层的十集：让车、船、伞跑得动、停得住、保得住命的机器'),
                (8.2, 16, '杠杆长出液压刹车，摆钟长出安全带，热气球长出安全气囊，齿轮长出差速器，曲柄连杆长出雨刮器'),
                (16.2, 24, '机翼长出螺旋桨，腰舟长出潜水艇，直升机长出气垫船，热气球又长出降落伞'),
                (24.2, 30, '最后，人工智能和地图导航一起，长出了自己会开的车')], y=1040)


CLIPS = {
 'E181_循环': (e181_loop, 22), 'E181_规则': (e181_rules, 22),
 'E181_片头': (titles.opening(SER33, VOL33, S33A, 9, '2004 年无人车挑战赛'), 7),
 'E181_片尾': (titles.closing(SER33, VOL33, S33A, 9, '下集：第三十三季特辑 · 第十三层回顾'), 7),
 'S33_第十三层': (s33_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
