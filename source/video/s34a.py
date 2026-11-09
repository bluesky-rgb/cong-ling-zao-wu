"""第三十四季（古法解密 14.0：水、风、土、纸）第一批：B140 渴乌、B141 螺旋泵、B142 风塔 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO, FIBER

SB34 = [('B140', '渴乌'), ('B141', '螺旋泵'), ('B142', '风塔'), ('B143', '回旋镖'), ('B144', '边架艇'),
        ('B145', '草拌泥'), ('B146', '地窖'), ('B147', '耧车'), ('B148', '装裱'), ('B149', '灯芯')]
VOL34 = '第三十四季 · 古法解密 14.0'
TUBE = (200, 210, 220)
WIND = (170, 210, 235)
SAND = (205, 170, 115)
CLAY = (165, 110, 75)


def _basin(c, x0, y0, x1, y1, level):
    c.rect(x0, level, x1, y1, fill=mix(BG, WATER, 0.75))
    c.line([(x0, y0), (x0, y1), (x1, y1), (x1, y0)], MUTED, 5)


def _flow_dots(c, pts, t, speed, col, n=26):
    L = [0]
    for k in range(1, len(pts)):
        L.append(L[-1] + math.dist(pts[k - 1], pts[k]))
    tot = L[-1]
    if speed <= 0:
        return
    for j in range(n):
        d = (j / n * tot + t * speed) % tot
        for k in range(1, len(pts)):
            if L[k] >= d:
                f = (d - L[k - 1]) / max(1e-6, L[k] - L[k - 1])
                x = pts[k - 1][0] + (pts[k][0] - pts[k - 1][0]) * f
                y = pts[k - 1][1] + (pts[k][1] - pts[k - 1][1]) * f
                c.ellipse(x, y, 6, 6, fill=col)
                break


# ---------------------------------------------------------------- B140 渴乌
def b140_siphon(c, t, i):
    corner_tag(c, 'B140 · 出口比水面低，水就自己翻过去')
    c.text(60, 96, '软管灌满水搭过桶沿：出口在水面以下，管里长的一段水往下拽，大气压把水压进管口', 'serif', 36, INK)
    p = min(1.0, t / 22)
    hl = 470 + p * 90
    hr = 860 - p * 90
    _basin(c, 160, 380, 640, 700, hl)
    c.rect(120, 700, 680, 960, fill=mix(BG, WOOD, 0.5), r=6)
    c.text(400, 830, '一摞书垫高', 'sans', 22, MUTED, 'mm')
    _basin(c, 1000, 640, 1520, 960, hr)
    pts = [(470, 640), (470, 330), (560, 260), (900, 260), (1180, 330), (1180, 900)]
    c.line(pts, mix(BG, TUBE, 0.9), 22)
    c.line(pts, mix(BG, WATER_L, 0.9), 12)
    _flow_dots(c, pts, t, 180, INK)
    c.arrow(330, hl - 80, 330, hl - 8, SPARK, 4, 14)
    c.arrow(380, hl - 80, 380, hl - 8, SPARK, 4, 14)
    c.text(355, hl - 105, '大气压往下压', 'sans', 22, SPARK, 'mm')
    c.line([(160, hl), (1560, hl)], mix(BG, SPARK, 0.5), 2)
    c.text(1580, hl, '高盆水面', 'sans', 20, SPARK, 'lm')
    c.arrow(1250, hl + 10, 1250, 890, NRED, 4, 14)
    c.text(1270, (hl + 900) / 2, '出口比水面低多少', 'sans', 22, NRED, 'lm')
    c.text(1270, (hl + 900) / 2 + 34, '就有多大的「拽劲」', 'sans', 22, NRED, 'lm')
    c.text(720, 220, '管子最高点', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '软管整根按进水里灌满，堵住两头，一头放进高盆，一头放进低盆'),
                (7.2, 14, '一松手，水就爬上管子、翻过盆沿，一直流到低盆里'),
                (14.2, 22, '出口那一侧的水柱更长更重，往下一拽，大气压就把高盆的水压进管口（示意）')], y=1010)


def b140_levels(c, t, i):
    corner_tag(c, 'B140 · 两边水面一样高，水就停了')
    c.text(60, 96, '慢慢把低盆抬高：两盆水面的高差越小，水流得越慢；两边一样高，水就不流了', 'serif', 36, INK)
    p = min(1.0, t / 18)
    dh = 1 - p
    ry = 860 - (1 - dh) * 300
    _basin(c, 120, 400, 500, 660, 470)
    c.rect(90, 660, 530, 960, fill=mix(BG, WOOD, 0.5), r=6)
    _basin(c, 700, ry - 260, 1080, ry, 470 + dh * 300)
    c.rect(670, ry, 1110, 960, fill=mix(BG, WOOD, 0.35), r=6)
    pts = [(330, 620), (330, 330), (400, 280), (800, 280), (890, 330), (890, ry - 40)]
    c.line(pts, mix(BG, TUBE, 0.9), 20)
    c.line(pts, mix(BG, WATER_L, 0.9), 10)
    v = math.sqrt(max(0, dh))
    _flow_dots(c, pts, t, 200 * v, INK, 20)
    c.line([(120, 470), (1100, 470)], mix(BG, SPARK, 0.5), 2)
    c.text(1040, 440, f'高差 {dh * 30:.0f} 厘米', 'mono', 26, SPARK, 'mm')
    gx0, gy0, gx1, gy1 = 1250, 820, 1820, 330
    c.rect(1200, 290, 1860, 880, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    c.text((gx0 + gx1) / 2, gy0 + 34, '两盆水面高差 →', 'sans', 20, MUTED, 'mm')
    c.text(gx0 + 10, gy1 - 16, '流速（示意）', 'sans', 20, MUTED, 'lm')
    cur = [(gx0 + (gx1 - gx0) * k / 40, gy0 - (gy0 - gy1 - 40) * math.sqrt(k / 40)) for k in range(41)]
    c.line(cur, mix(BG, FIELD, 0.8), 3)
    k = dh * 40
    c.ellipse(gx0 + (gx1 - gx0) * k / 40, gy0 - (gy0 - gy1 - 40) * math.sqrt(k / 40), 12, 12, fill=SPARK)
    if dh < 0.03:
        c.text(1530, 380, '一样高 → 停', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 6, '高盆不动，把低盆一点点抬高，两盆水面的高差越来越小'),
                (6.2, 13, '高差小了，往下拽的那段水柱短了，水流得越来越慢'),
                (13.2, 22, '两边水面一样高时，左右一样重，水就停在管子里不动了（示意）')], y=1010)


# ---------------------------------------------------------------- B141 螺旋泵
def _screw(c, ax0, ay0, ax1, ay1, R, turns, phi, show_water=True, fill_frac=1.0):
    L = math.dist((ax0, ay0), (ax1, ay1))
    ux, uy = (ax1 - ax0) / L, (ay1 - ay0) / L
    nx, ny = -uy, ux
    if ny < 0:
        nx, ny = -nx, -ny
    c.poly([(ax0 + nx * R, ay0 + ny * R), (ax1 + nx * R, ay1 + ny * R), (ax1 - nx * R, ay1 - ny * R), (ax0 - nx * R, ay0 - ny * R)],
           mix(BG, (90, 100, 110), 0.55))
    N = 240
    back, front = [], []
    for k in range(N + 1):
        s = k / N
        th = 2 * math.pi * turns * s - phi
        x = ax0 + ux * L * s + nx * R * math.cos(th)
        y = ay0 + uy * L * s + ny * R * math.cos(th)
        (front if math.sin(th) > 0 else back).append((k, x, y))
    for grp_, col, w in [(back, mix(BG, TUBE, 0.35), 6), (front, TUBE, 9)]:
        run = []
        for k, x, y in grp_:
            if run and k != run[-1][0] + 1:
                if len(run) > 1: c.line([(a, b) for _, a, b in run], col, w)
                run = []
            run.append((k, x, y))
        if len(run) > 1: c.line([(a, b) for _, a, b in run], col, w)
    if show_water:
        for k in range(-1, int(turns) + 2):
            s = (k + phi / (2 * math.pi)) / turns
            if 0.02 < s < 0.98:
                x = ax0 + ux * L * s + nx * R * 0.85
                y = ay0 + uy * L * s + ny * R * 0.85
                c.ellipse(x, y, 20 * fill_frac + 4, 12 * fill_frac + 3, fill=mix(BG, WATER_L, 0.95))
    return ux, uy, nx, ny, L


def b141_screw(c, t, i):
    corner_tag(c, 'B141 · 水一直往下滑，螺旋却一直往上转')
    c.text(60, 96, '软管绕在斜放的瓶子上：每一圈最低的地方兜着一小团水，转一圈，它就被抬高一圈', 'serif', 36, INK)
    c.rect(100, 760, 700, 960, fill=mix(BG, WATER, 0.7), r=8)
    c.text(180, 920, '下面的水盆', 'sans', 22, INK, 'mm')
    phi = t * 1.6
    ax0, ay0, ax1, ay1 = 360, 860, 1240, 340
    ux, uy, nx, ny, L = _screw(c, ax0, ay0, ax1, ay1, 70, 6, phi)
    c.rect(1240, 500, 1560, 700, fill=mix(BG, WATER, 0.25 + 0.5 * min(1, t / 22)), outline=MUTED, width=4, r=8)
    c.text(1400, 730, '上面接水的盆', 'sans', 22, MUTED, 'mm')
    for j in range(5):
        y = 380 + ((t * 120 + j * 40) % 160)
        c.ellipse(1300 + j * 10, y, 6, 8, fill=WATER_L)
    c.arc(ax0 - 60, ay0 + 40, 50, 50, 200, 340, SPARK, 4)
    c.text(ax0 - 60, ay0 + 120, '手慢慢转', 'sans', 22, SPARK, 'mm')
    k = 3
    s = (k + (phi % (2 * math.pi)) / (2 * math.pi)) / 6
    x = ax0 + ux * L * s + nx * 70 * 0.85
    y = ay0 + uy * L * s + ny * 70 * 0.85
    c.ellipse(x, y, 30, 22, outline=NRED, width=3)
    c.line([(x + 30, y + 10), (1500, 880)], NRED, 2)
    c.text(1510, 880, '盯住这一团水', 'sans', 22, NRED, 'lm')
    caps(c, t, [(0, 7, '每一圈软管的最低处，都兜着一小团水，水只会往低处待'),
                (7.2, 14, '可瓶子一转，「最低处」整个往上挪了一格，水跟着往上走'),
                (14.2, 22, '转 6 圈，最下面的水就被送到最上面，倒进高处的盆里（示意）')], y=1010)


def b141_angle(c, t, i):
    corner_tag(c, 'B141 · 太陡了，管里兜不住水')
    c.text(60, 96, '同样转 20 圈：斜一点送得多；越陡，每一圈兜住的水越少，太陡就一滴也送不上去', 'serif', 36, INK)
    phi = t * 1.6
    vals = [(30, 1.0, 1.0), (45, 0.7, 0.62), (60, 0.25, 0.12)]
    for j, (ang, ff, amt) in enumerate(vals):
        cx = 330 + j * 430
        a = math.radians(ang)
        L = 380
        ax0, ay0 = cx - L / 2 * math.cos(a), 760 + 0
        ax1, ay1 = ax0 + L * math.cos(a), ay0 - L * math.sin(a)
        _screw(c, ax0, ay0, ax1, ay1, 42, 4, phi, True, ff)
        c.text(cx, 840, f'斜 {ang}°', 'bold', 28, INK, 'mm')
    c.rect(1380, 280, 1860, 880, fill=SHEET, r=14)
    c.text(1620, 320, '转 20 圈接到的水（示意）', 'sans', 22, MUTED, 'mm')
    g = min(1.0, t / 16)
    for j, (ang, ff, amt) in enumerate(vals):
        x = 1470 + j * 150
        h = 420 * amt * g
        c.rect(x - 45, 820 - h, x + 45, 820, fill=mix(BG, FIELD, 0.85), r=6)
        c.text(x, 850, f'{ang}°', 'mono', 24, INK, 'mm')
    c.text(1620, 380, '以实测为准', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '把同一个螺旋泵分别斜成 30°、45°、60°，都转 20 圈'),
                (7.2, 14, '越陡，每一圈的「低处」越浅，兜住的那团水越小'),
                (14.2, 22, '陡到一定程度，水从一圈直接滑回下一圈，就送不上去了（示意）')], y=1010)


# ---------------------------------------------------------------- B142 风塔
def _house(c, x0, gy, w, h, tower_open, tower=True):
    c.rect(x0, gy - h, x0 + w, gy, fill=mix(BG, SAND, 0.55), r=4)
    c.rect(x0 + 18, gy - h + 18, x0 + w - 18, gy, fill=mix(BG, SAND, 0.15))
    c.rect(x0 + w - 18, gy - 150, x0 + w, gy - 20, fill=BG)
    if tower:
        tx = x0 + w / 2 - 50
        c.rect(tx, gy - h - 300, tx + 100, gy - h + 18, fill=mix(BG, SAND, 0.55))
        c.rect(tx + 14, gy - h - 300, tx + 86, gy - h + 18, fill=mix(BG, SAND, 0.15))
        c.rect(tx - 4, gy - h - 320, tx + 104, gy - h - 296, fill=mix(BG, SAND, 0.7))
        if tower_open == 'L':
            c.rect(tx, gy - h - 290, tx + 14, gy - h - 200, fill=BG)
        elif tower_open == 'R':
            c.rect(tx + 86, gy - h - 290, tx + 100, gy - h - 200, fill=BG)
        return tx
    return None


def b142_tower(c, t, i):
    corner_tag(c, 'B142 · 迎风的口把风兜进来')
    c.text(60, 96, '风塔顶上的开口朝着风：高处的风被兜进塔里往下灌，穿过屋子，再从门口流出去', 'serif', 36, INK)
    gy = 900
    x0, w, h = 560, 760, 340
    tx = _house(c, x0, gy, w, h, 'L')
    for k in range(6):
        y = 240 + k * 40
        xx = 120 + ((t * 260 + k * 90) % 300)
        c.arrow(xx, y, xx + 120, y, mix(BG, WIND, 0.9), 4, 12)
    c.text(200, 210, '高处的风', 'sans', 22, WIND, 'mm')
    path = [(tx - 120, gy - h - 250), (tx + 50, gy - h - 250), (tx + 50, gy - h + 60), (tx + 50, gy - 100), (x0 + w - 10, gy - 90), (x0 + w + 200, gy - 90)]
    c.line(path, mix(BG, WIND, 0.35), 30)
    _flow_dots(c, path, t, 220, WIND, 30)
    for k in range(4):
        sx = x0 + 120 + k * 90
        ang = math.radians(50 + 8 * math.sin(t * 6 + k))
        c.line([(sx, gy - h + 40), (sx + 70 * math.cos(ang), gy - h + 40 + 70 * math.sin(ang))], (230, 230, 230), 5)
    c.text(x0 + 250, gy - h + 140, '纸巾条被吹向门口', 'sans', 22, MUTED, 'mm')
    c.text(x0 + w + 100, gy - 140, '门', 'sans', 22, MUTED, 'mm')
    c.text(tx + 50, gy - h - 350, '风塔', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '沙漠的屋顶上竖起一座高塔，塔顶迎风的一面开着口'),
                (7.2, 14, '高处的风比地面大、也更干净，一头撞进开口，只能往塔下钻'),
                (14.2, 22, '风灌进屋里，带走热气，再从门口流出去：没有电扇的「空调」（示意）')], y=1010)


def b142_direction(c, t, i):
    corner_tag(c, 'B142 · 开口朝哪边，风就怎么走')
    c.text(60, 96, '同一个鞋盒房子三种做法：开口迎风、开口背风、不要风塔，看屋里的纸巾条怎么飘', 'serif', 36, INK)
    labels = [('开口迎风', 'L', 52, '往下灌进屋'), ('开口背风', 'R', 25, '屋里空气被抽上去'), ('不要风塔', None, 6, '几乎不动')]
    for j, (lab, op, deg, note) in enumerate(labels):
        x0 = 120 + j * 600
        gy = 820
        w, h = 400, 220
        tx = _house(c, x0, gy, w, h, op, op is not None)
        if op is None:
            pass
        for k in range(3):
            sx = x0 + 80 + k * 90
            d = deg + 4 * math.sin(t * 6 + k + j)
            ang = math.radians(90 + d) if op == 'R' else math.radians(90 - d)
            c.line([(sx, gy - h + 30), (sx + 60 * math.cos(ang), gy - h + 30 + 60 * math.sin(ang))], (230, 230, 230), 5)
        if op == 'L':
            c.arrow(tx + 50, gy - h - 220, tx + 50, gy - h - 40, WIND, 4, 12)
        elif op == 'R':
            c.arrow(tx + 50, gy - h - 40, tx + 50, gy - h - 220, WIND, 4, 12)
        c.text(x0 + w / 2, gy + 50, lab, 'bold', 28, INK, 'mm')
        c.text(x0 + w / 2, gy + 92, note, 'sans', 22, MUTED, 'mm')
    for k in range(3):
        y = 260 + k * 40
        xx = 40 + ((t * 200 + k * 70) % 120)
        c.arrow(xx, y, xx + 70, y, WIND, 3, 10)
    c.text(90, 220, '风', 'sans', 22, WIND, 'mm')
    caps(c, t, [(0, 7, '电扇最低档从左边吹，三个鞋盒房子里都挂着纸巾条'),
                (7.2, 14, '开口迎风，风被兜进来往下灌；开口背风，塔口那里气压低，把屋里的空气抽出去'),
                (14.2, 22, '没有风塔，纸巾条几乎不动：古人会按当地的风向来开口（示意）')], y=1010)


CLIPS = {
 'B140_虹吸': (b140_siphon, 22), 'B140_高差': (b140_levels, 22),
 'B140_片头': (titles.opening(BSER, VOL34, SB34, 0, '东汉已有渴乌引水'), 7),
 'B140_片尾': (titles.closing(BSER, VOL34, SB34, 0, '下集：管子绕在斜筒上，转一转，水为什么往上爬？'), 7),
 'B141_螺旋': (b141_screw, 22), 'B141_斜度': (b141_angle, 22),
 'B141_片头': (titles.opening(BSER, VOL34, SB34, 1, '古希腊，传为阿基米德所创'), 7),
 'B141_片尾': (titles.closing(BSER, VOL34, SB34, 1, '下集：沙漠屋顶一座高塔，屋里为什么就有风？'), 7),
 'B142_兜风': (b142_tower, 22), 'B142_方向': (b142_direction, 22),
 'B142_片头': (titles.opening(BSER, VOL34, SB34, 2, '古波斯沙漠城市已有风塔'), 7),
 'B142_片尾': (titles.closing(BSER, VOL34, SB34, 2, '下集：扔出去的回旋镖，为什么会飞回来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
