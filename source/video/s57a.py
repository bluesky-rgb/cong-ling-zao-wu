"""第五十七季（第二十五层：露营）第一批：E292 帐篷、E293 地钉、E294 睡袋 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S57A = [('292', '帐篷'), ('293', '地钉'), ('294', '睡袋'), ('295', '保温毯'), ('296', '充气垫'),
        ('297', '折叠椅'), ('298', '登山杖'), ('299', '吊床'), ('300', '头灯'), ('301', '荧光棒')]
SER57, VOL57 = '从零造物', '第五十七季 · 第二十五层：露营'
TENT = (230, 140, 70)
POLE = (90, 90, 100)
SOIL = (130, 100, 70)
WARM = (230, 110, 80)
COOL = (100, 150, 220)
FLUFF = (235, 230, 215)


def arcpts(x0, x1, gy, h, n=40):
    """两端在地面、拱高 h 的弓形撑杆。"""
    out = []
    for j in range(n + 1):
        s = j / n
        out.append((x0 + (x1 - x0) * s, gy - h * math.sin(math.pi * s)))
    return out


# ---------------------------------------------------------------- E292 帐篷
def e292_bow(c, t, i):
    corner_tag(c, '第 292 集 · 撑杆想弹直，把布绷紧')
    c.text(60, 96, '把一根细撑杆弯成弓，两头插在地上：它一直想弹直，往外顶着帐篷布；布又把它拉住，两边较劲就绷紧了', 'serif', 36, INK)
    gy = 860
    c.line([(160, gy), (1760, gy)], LINE, 4)
    k = min(1.0, t / 6)
    # 左：直杆 → 弯曲
    h = 360 * k
    pts = arcpts(360 - 0 * k, 960 - 0 * k, gy, h) if k > 0.02 else [(360, gy), (960, gy)]
    if t > 7.2:
        c.poly(pts + [(960, gy)], mix(BG, TENT, 0.55))
    seg(c, pts, POLE, 9)
    if t > 7.2:
        for s in (0.2, 0.5, 0.8):
            x, y = 360 + 600 * s, gy - h * math.sin(math.pi * s)
            ang = math.atan2(-math.cos(math.pi * s) * math.pi * h / 600, 1) - math.pi / 2
            nx, ny = math.cos(ang), math.sin(ang)
            c.arrow(x, y, x + 70 * nx, y + 70 * ny, NRED, 5, 16)
        c.text(820, gy - h - 40, '杆往外顶', 'bold', 28, NRED, 'mm')
        c.text(660, gy - 60, '布把杆拉住', 'bold', 26, INK, 'mm')
    # 右：一根松布，没有杆
    c.poly([(1180, gy), (1380, gy - 60), (1460, gy - 40), (1600, gy)], mix(BG, TENT, 0.4))
    c.text(1390, gy + 50, '没有撑杆：布塌在地上', 'bold', 26, MUTED, 'mm')
    caps(c, t, [(0, 7, '一根直直的细撑杆，两头往里推，弯成一张弓'),
                (7.2, 14, '弯着的杆一直想弹直，往外顶住帐篷布'),
                (14.2, 22, '布被顶得绷紧，又把杆拉住：两边较劲，帐篷就鼓起来了')], y=1010)


def e292_cross(c, t, i):
    corner_tag(c, '第 292 集 · 两根弓交叉，四面都撑着')
    c.text(60, 96, '只有一根弓，侧面来风一推就歪；两根弓在顶上交叉成十字，四个方向都有杆顶着，风吹也只是轻轻晃', 'serif', 36, INK)
    gy = 820
    for j in range(2):
        cx = 560 + j * 800
        c.line([(cx - 330, gy), (cx + 330, gy)], LINE, 4)
        wind = t > 7.2
        sway = (90 if j == 0 else 14) * (0.5 + 0.5 * math.sin(t * 4)) if wind else 0
        top = (cx + sway, gy - 340)
        # 前后两根杆（简化为两条从地面到顶点的弧线）
        pts1 = [((cx - 280) + (top[0] - (cx - 280)) * s + 60 * math.sin(math.pi * s), gy + (top[1] - gy) * math.sin(math.pi * s / 2)) for s in [q / 20 for q in range(21)]]
        pts2 = [((cx + 280) + (top[0] - (cx + 280)) * s - 60 * math.sin(math.pi * s), gy + (top[1] - gy) * math.sin(math.pi * s / 2)) for s in [q / 20 for q in range(21)]]
        c.poly(pts1 + pts2[::-1], mix(BG, TENT, 0.5))
        seg(c, pts1, POLE, 7)
        seg(c, pts2, POLE, 7)
        if j == 1:
            c.line([(cx - 130, gy - 20), top], mix(POLE, BG, 0.3), 6)
            c.line([(cx + 130, gy - 20), top], mix(POLE, BG, 0.3), 6)
        if wind:
            for k in range(4):
                x = cx - 520 + ((t * 160 + k * 60) % 160)
                c.arrow(x, gy - 300 + k * 60, x + 60, gy - 300 + k * 60, mix(BG, FIELD, 1.0), 4, 14)
        c.text(cx, gy + 60, ['一根弓：风一吹就歪', '两根弓交叉：轻轻晃'][j], 'bold', 28, NRED if j == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '左边只有一根弓，右边两根弓在顶上交叉'),
                (7.2, 14, '风从侧面吹来：一根弓的帐篷被推得歪向一边'),
                (14.2, 22, '交叉的两根弓四个方向都撑着，风吹只轻轻晃（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- E293 地钉
def soil(c, x0, x1, gy, yb):
    c.rect(x0, gy, x1, yb, fill=mix(BG, SOIL, 0.85))
    random.seed(3)
    for k in range(60):
        x = random.uniform(x0 + 10, x1 - 10); y = random.uniform(gy + 10, yb - 10)
        c.ellipse(x, y, 3, 3, fill=mix(BG, SOIL, 1.0))


def peg(c, x, gy, ang_deg, L, col, lift=0):
    a = math.radians(ang_deg)
    x0, y0 = x, gy - 30 - lift
    x1, y1 = x0 + L * math.sin(a), y0 + L * math.cos(a)
    c.line([(x0, y0), (x1, y1)], col, 14)
    c.ellipse(x0, y0, 14, 14, fill=col)
    return x0, y0


def e293_angle(c, t, i):
    corner_tag(c, '第 293 集 · 斜着朝外插，更拉不出')
    c.text(60, 96, '拉绳往斜上方拉：竖着插的钉子顺着拉的方向一撬就出来；斜着、钉头朝外插，钉子和拉绳接近垂直，就拉不动', 'serif', 36, INK)
    gy = 520
    for j in range(2):
        x0 = 160 + j * 820
        soil(c, x0, x0 + 700, gy, 900)
        px = x0 + 380
        if j == 0:
            lift = 0 if t < 9 else min(160, (t - 9) * 40)
            tilt = 0 if t < 9 else min(30, (t - 9) * 8)
            hx, hy = peg(c, px, gy, -tilt, 260, POLE, lift)
            c.text(x0 + 350, 960, '竖着插：被撬出来', 'bold', 28, NRED, 'mm')
        else:
            hx, hy = peg(c, px, gy, -35, 260, POLE)
            c.text(x0 + 350, 960, '斜着朝外插：拉不动', 'bold', 28, GREEN, 'mm')
        tx, ty = hx - 220, hy - 190
        c.line([(hx, hy), (tx, ty)], INK, 4)
        c.text(tx - 10, ty - 30, '帐篷拉绳', 'sans', 24, MUTED, 'mm')
        if t > 4:
            c.arrow(hx, hy, hx - 90, hy - 78, NRED, 6, 18)
    caps(c, t, [(0, 7, '帐篷的拉绳往斜上方拉，两根一样长的钉子一竖一斜'),
                (7.2, 14, '竖着插的钉子，拉力顺着它往外撬，一下就松了'),
                (14.2, 22, '钉头朝外斜着插：拉绳和钉子接近垂直，钉子纹丝不动（只用钝头筷子做实验）')], y=1010)


def e293_wedge(c, t, i):
    corner_tag(c, '第 293 集 · 要拽起一大块土')
    c.text(60, 96, '斜插的钉子要被拉出来，得把压在它前面的一大块土一起拽起来；土越压实、插得越深，这块土越大越重', 'serif', 36, INK)
    gy = 480
    soil(c, 260, 1660, gy, 920)
    px = 980
    hx, hy = peg(c, px, gy, -35, 320, POLE)
    k = min(1.0, max(0, (t - 4) / 5))
    if k > 0:
        a = math.radians(-35)
        ex, ey = hx + 320 * math.sin(a), hy + 320 * math.cos(a)
        c.poly([(hx, gy), (ex, ey), (ex - 260 * k, gy)], mix(SOIL, SPARK, 0.35 * k))
        c.text(ex - 160, gy + 110, '这一大块土', 'bold', 28, mix(INK, SPARK, 0.5), 'mm')
    c.line([(hx, hy), (hx - 320, hy - 260)], INK, 4)
    c.arrow(hx, hy, hx - 100, hy - 84, NRED, 6, 18)
    if t > 14.2:
        c.text(1400, 400, '土松：这块小，容易拉出', 'bold', 26, NRED, 'mm')
        c.text(1400, 360, '土实、插得深：这块大，拉不动', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '斜插的钉子挡在拉绳前面，钉子前上方压着一块土'),
                (7.2, 14, '想把钉子拉出来，就得把这一大块土一起掀起来'),
                (14.2, 22, '土压得越实、钉子插得越深，掀起来越难：所以沙地要用宽大的地钉（待核）')], y=1010)


# ---------------------------------------------------------------- E294 睡袋
def e294_air(c, t, i):
    corner_tag(c, '第 294 集 · 困住不流动的空气')
    c.text(60, 96, '睡袋自己不发热，热是身体发出来的；蓬松的填充物里藏着无数小空气格子，空气不流动，热就很难穿过去', 'serif', 36, INK)
    cx, cy = 960, 560
    c.ellipse(cx, cy, 520, 260, fill=mix(BG, FLUFF, 0.8))
    random.seed(4)
    for k in range(120):
        a = random.uniform(0, 2 * math.pi); r = random.uniform(0.62, 0.97)
        x, y = cx + 520 * r * math.cos(a), cy + 260 * r * math.sin(a)
        c.ellipse(x, y, 14, 10, outline=mix(BG, MUTED, 0.5), width=2)
    c.ellipse(cx, cy, 300, 140, fill=mix(BG, WARM, 0.85))
    c.text(cx, cy, '身体（热）', 'bold', 34, BG, 'mm')
    for k in range(10):
        a = 2 * math.pi * k / 10
        ph = (t * 0.25 + k / 10) % 1
        r0 = 1.02 + ph * 0.25
        x, y = cx + 300 * r0 * math.cos(a), cy + 140 * r0 * math.sin(a)
        c.ellipse(x, y, 9, 9, fill=mix(BG, NRED, 1 - ph))
    c.text(cx + 560, cy - 230, '小空气格子', 'sans', 26, MUTED, 'lm')
    c.line([(cx + 550, cy - 220), (cx + 400, cy - 150)], MUTED, 2)
    caps(c, t, [(0, 7, '身体一直在放热：红点就是想往外跑的热'),
                (7.2, 14, '蓬松的羽绒或棉花里，夹着无数个不流动的小空气格子'),
                (14.2, 22, '静止的空气很难传热，热走到一半就慢下来：睡袋里暖暖的')], y=1010)


def e294_squash(c, t, i):
    corner_tag(c, '第 294 集 · 压扁了反而不暖')
    c.text(60, 96, '三瓶一样热的温水：蓬松棉花包的凉得最慢，同样多的棉花勒紧压扁就差一些，什么都不包的凉得最快', 'serif', 36, INK)
    labels = [('蓬松', 1.0, 90), ('压扁', 0.4, 45), ('不包', 0.0, 18)]
    for j, (lab, fl, tau) in enumerate(labels):
        cx = 420 + j * 540
        if fl > 0:
            c.ellipse(cx, 600, 110 + 90 * fl, 200 + 60 * fl, fill=mix(BG, FLUFF, 0.85))
        c.rect(cx - 60, 430, cx + 60, 770, fill=mix(BG, COOL, 0.5), outline=MUTED, width=3, r=16)
        m = min(60, t / 20 * 60)
        T = 20 + 25 * math.exp(-m / tau)
        hot = (T - 20) / 25
        c.rect(cx - 50, 440, cx + 50, 760, fill=mix(mix(BG, COOL, 0.5), WARM, hot), r=12)
        c.text(cx, 600, f'{T:.0f} ℃', 'mono', 30, INK, 'mm')
        c.text(cx, 900, lab, 'bold', 30, [GREEN, SPARK, NRED][j], 'mm')
    c.text(960, 960, f'过了 {min(60, t / 20 * 60):.0f} 分钟（温度是示意，以实测为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '三瓶温水（不超过 50 ℃）：蓬松包、压扁包、不包'),
                (7.2, 14, '不包的那瓶最先凉下来'),
                (14.2, 22, '同样多的棉花，压扁后空气被挤出去，保暖就差了：睡袋要抖松再用')], y=1010)


CLIPS = {
 'E292_弓杆': (e292_bow, 22), 'E292_交叉': (e292_cross, 22),
 'E292_片头': (titles.opening(SER57, VOL57, S57A, 0, '穹顶帐篷只有两三根细撑杆'), 7),
 'E292_片尾': (titles.closing(SER57, VOL57, S57A, 0, '下集：地钉斜着插为什么更拉不出？'), 7),
 'E293_角度': (e293_angle, 22), 'E293_土块': (e293_wedge, 22),
 'E293_片头': (titles.opening(SER57, VOL57, S57A, 1, '搭帐篷时地钉斜着往外插'), 7),
 'E293_片尾': (titles.closing(SER57, VOL57, S57A, 1, '下集：睡袋不发热，怎么让人暖？'), 7),
 'E294_空气': (e294_air, 22), 'E294_压扁': (e294_squash, 22),
 'E294_片头': (titles.opening(SER57, VOL57, S57A, 2, '睡袋里塞满蓬松的羽绒'), 7),
 'E294_片尾': (titles.closing(SER57, VOL57, S57A, 2, '下集：薄薄一层保温毯凭什么保温？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
