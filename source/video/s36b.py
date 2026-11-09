"""第三十六季（古法解密 15.0）第二批：B153 车辐、B154 木鱼、B155 打水漂 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s36a import SB36, VOL36, STONE

CARDB = (200, 170, 120)
SOUND = (120, 190, 240)


# ---------------------------------------------------------------- B153 车辐
def _wheel(c, cx, cy, R, spokes, ang=0, solid=False, squash=0.0):
    ry = R * (1 - squash)
    if solid:
        c.ellipse(cx, cy, R, ry, fill=mix(BG, CARDB, 0.9))
        return
    c.ellipse(cx, cy, R, ry, outline=mix(BG, CARDB, 0.95), width=16)
    for k in range(spokes):
        a = ang + 2 * math.pi * k / spokes
        c.line([(cx, cy), (cx + (R - 8) * math.cos(a), cy + (ry - 8) * math.sin(a))], mix(BG, CARDB, 0.9), 5)
    c.ellipse(cx, cy, 30, 30 * (1 - squash), fill=mix(BG, WOOD, 0.95))


def b153_spokes(c, t, i):
    corner_tag(c, 'B153 · 力顺着辐条走')
    c.text(60, 96, '车的重量压在轮毂上，顺着辐条传到轮辋、再传到地面：中间那一大块木头根本不干活，挖掉它', 'serif', 36, INK)
    cx, cy, R = 520, 560, 280
    _wheel(c, cx, cy, R, 0, solid=True)
    c.text(cx, cy, '实心轮', 'bold', 30, BG, 'mm')
    c.text(cx, cy + R + 60, '重：大部分木头只是跟着转', 'sans', 24, MUTED, 'mm')
    cx2 = 1400
    _wheel(c, cx2, cy, R, 12, -t * 0.6)
    c.arrow(cx2, cy - 220, cx2, cy - 40, NRED, 6, 16)
    c.text(cx2 + 20, cy - 200, '车的重量', 'bold', 22, NRED, 'lm')
    p = (t * 0.8) % 1
    for k in range(12):
        a = -t * 0.6 + 2 * math.pi * k / 12
        if math.sin(a) > 0.5:
            x = cx2 + (R - 10) * p * math.cos(a)
            y = cy + (R - 10) * p * math.sin(a)
            c.ellipse(x, y, 8, 8, fill=SPARK)
    c.text(cx2, cy + R + 60, '辐条轮：力只走这几条路', 'sans', 24, MUTED, 'mm')
    c.text(cx2, cy + R + 100, '「三十辐共一毂」', 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '实心木轮又厚又重，可压力只从轮毂往下走到着地的那一点'),
                (7.2, 14, '把用不着的木头挖掉，只留轮辋、轮毂和一根根辐条'),
                (14.2, 22, '转到哪里，哪几根辐条就接过压力：轮子轻了一大半，跑得更快（示意）')], y=1010)


def b153_load(c, t, i):
    corner_tag(c, 'B153 · 往上加书，谁先压扁？')
    c.text(60, 96, '硬纸板做的实心轮和吸管辐条轮：辐条轮轻得多；辐条从 8 根加到 16 根，能顶住的书也多了', 'serif', 36, INK)
    vals = [('实心纸板轮', None, 6, '约 60 克'), ('8 根辐条', 8, 3, '约 25 克'), ('16 根辐条', 16, 6, '约 35 克')]
    books = min(7, int(t / 2.4))
    for k, (lab, sp, nmax, wt) in enumerate(vals):
        cx = 380 + k * 580
        n = min(books, nmax)
        broke = books > nmax
        squash = 0.35 if broke else 0.02 * n
        R = 170
        cy = 800 - R * (1 - squash)
        _wheel(c, cx, cy, R, sp or 0, 0.2, solid=sp is None, squash=squash)
        for b in range(n + (1 if broke else 0)):
            y = cy - R * (1 - squash) - 30 - b * 34
            c.rect(cx - 120, y, cx + 120, y + 30, fill=mix(BG, [(200, 90, 80), (90, 140, 200), (120, 180, 120)][b % 3], 0.85), r=4)
        c.text(cx, 870, lab, 'bold', 26, INK, 'mm')
        c.text(cx, 910, wt + '（示意）', 'mono', 20, MUTED, 'mm')
        if broke:
            c.text(cx, 230, f'第 {nmax + 1} 本压扁了', 'bold', 24, NRED, 'mm')
    c.text(960, 960, '以实测为准；胶枪由成年人使用', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '先称一称：同样大小，辐条轮比实心轮轻得多'),
                (7.2, 14, '一本一本往上放书：8 根辐条的轮子先被压歪'),
                (14.2, 22, '辐条加到 16 根、排得均匀，能顶住的书又多了：轻和结实可以兼得（示意）')], y=1010)


# ---------------------------------------------------------------- B154 木鱼
def b154_cavity(c, t, i):
    corner_tag(c, 'B154 · 空腔里的空气跟着振')
    c.text(60, 96, '木鱼里面是空的，只留一条缝：敲一下，壳在振，缝口那团空气也像弹簧上的小球一样进进出出', 'serif', 36, INK)
    cx, cy = 760, 600
    c.ellipse(cx, cy, 380, 260, fill=mix(BG, WOOD, 0.95))
    c.ellipse(cx, cy + 10, 320, 200, fill=mix(BG, (40, 30, 25), 0.9))
    c.rect(cx - 220, cy + 190, cx + 220, cy + 230, fill=mix(BG, (40, 30, 25), 0.95), r=10)
    c.text(cx, cy + 290, '鱼嘴的缝', 'sans', 22, MUTED, 'mm')
    hit = t % 3
    amp = math.exp(-hit * 1.4)
    for k in range(40):
        r = random.Random(k)
        x = cx + r.uniform(-280, 280)
        y = cy + r.uniform(-160, 160)
        if ((x - cx) / 300) ** 2 + ((y - cy) / 190) ** 2 > 1: continue
        dy = 10 * amp * math.sin(hit * 30 + 0.0)
        c.ellipse(x, y + dy * (y - cy) / 190, 5, 5, fill=SOUND)
    pd = 26 * amp * math.sin(hit * 30)
    c.ellipse(cx, cy + 210 + pd, 50, 16, fill=mix(BG, SOUND, 0.9))
    if hit < 0.25:
        c.text(cx + 300, cy - 280, '笃！', 'bold', 40, SPARK, 'mm')
    for k in range(4):
        r = (hit * 300 + k * 70)
        if r < 600:
            c.arc(cx, cy + 210, r, r * 0.6, 20, 160, mix(BG, SOUND, amp * (1 - r / 600)), 3)
    c.rect(1300, 300, 1860, 760, fill=SHEET, r=14)
    c.text(1580, 350, '空腔里的空气 = 弹簧', 'bold', 26, INK, 'mm')
    c.text(1580, 410, '缝口那团空气 = 弹簧上的小球', 'sans', 22, MUTED, 'mm')
    c.text(1580, 500, '敲的声音里，正好对上', 'sans', 22, MUTED, 'mm')
    c.text(1580, 545, '这个「弹簧」节奏的那一部分', 'sans', 22, MUTED, 'mm')
    c.text(1580, 590, '被放大、拉长', 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '实心木块敲一下，只有木头本身在振，「嗒」一声就没了'),
                (7.2, 14, '木鱼挖空后，里面一大团空气像弹簧，缝口的一小团空气像弹簧上的球'),
                (14.2, 22, '壳一振，空气跟着有节奏地进出缝口，声音就又响又圆，还拖着余音（示意）')], y=1010)


def b154_slot(c, t, i):
    corner_tag(c, 'B154 · 开口大小，有一个最响的')
    c.text(60, 96, '同样的纸盒、同样的敲法：封死的闷，开一条小缝最响，口开得太大，空气跑掉又不响了', 'serif', 36, INK)
    vals = [('实心木块', 0, 62), ('封死的纸盒', 0, 66), ('开 1 厘米缝', 1, 74), ('开 3 厘米缝', 3, 69)]
    p = min(1.0, t / 12)
    for k, (lab, w, db) in enumerate(vals):
        x = 250 + k * 420
        if k == 0:
            c.rect(x - 110, 420, x + 110, 560, fill=mix(BG, WOOD, 0.95), r=6)
        else:
            c.rect(x - 130, 400, x + 130, 580, fill=mix(BG, (200, 170, 130), 0.85), r=6)
            if w:
                c.rect(x - 70, 560 - w * 14, x + 70, 560, fill=BG)
        h = (db - 55) * 12 * p
        c.rect(x - 60, 880 - h, x + 60, 880, fill=mix(BG, SOUND, 0.85), r=6)
        c.text(x, 860 - h, f'{db * p:.0f} 分贝', 'mono', 22, SPARK, 'mm')
        c.text(x, 920, lab, 'bold', 24, INK, 'mm')
    c.text(960, 960, '示意，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同一根筷子、差不多的力，敲四样东西，手机在 30 厘米外读分贝'),
                (7.2, 14, '封死的纸盒有点闷；开一条小缝，声音一下子亮了，还拖着尾巴'),
                (14.2, 22, '把缝剪大，空气进出太自由，「弹簧」就软了：所以木鱼只开一条窄缝（示意）')], y=1010)


# ---------------------------------------------------------------- B155 打水漂
def b155_bounce(c, t, i):
    corner_tag(c, 'B155 · 斜着贴水飞，被水面托起来')
    c.text(60, 96, '扁石头前端稍稍翘起、贴着水面飞：一碰水，就在前面压起一个小水坡，像滑雪板一样被推上去', 'serif', 36, INK)
    wl = 700
    c.rect(0, wl, 1920, 960, fill=mix(BG, WATER, 0.6))
    T = 10.0
    tt = t % 11
    pts = []
    x, y = 120, 420
    vx, vy = 150, 0
    hops = []
    dt = 0.02
    k = 0
    path = []
    while k < 600 and x < 1850:
        vy += 400 * dt
        x += vx * dt * 1.4
        y += vy * dt
        if y >= wl - 8:
            if abs(vy) > 60 and vx > 40:
                vy = -abs(vy) * 0.75
                vx *= 0.82
                hops.append((x, wl))
                y = wl - 8
            else:
                break
        path.append((x, y))
        k += 1
    n = int(len(path) * min(1.0, tt / T))
    if n > 1:
        seg(c, path[:n], mix(BG, MUTED, 0.6), 2)
        x, y = path[n - 1]
        c.poly([(x - 30, y + 4), (x + 30, y - 6), (x + 32, y + 2), (x - 28, y + 10)], mix(BG, STONE, 1.0))
    for hx, hy in hops:
        if hx < (path[n - 1][0] if n > 1 else 0):
            for r in (20, 40, 60):
                c.arc(hx, hy, r, r * 0.25, 0, 360, mix(BG, WATER_L, 0.6), 2)
    c.text(1500, 260, f'蹦了 {sum(1 for hx, _ in hops if n > 1 and hx < path[n - 1][0])} 下', 'bold', 34, SPARK, 'mm')
    bx, by = 520, 880
    c.rect(220, 770, 820, 950, fill=SHEET, r=12)
    c.poly([(bx - 140, by - 50), (bx + 120, by - 90), (bx + 130, by - 78), (bx - 130, by - 38)], mix(BG, STONE, 1.0))
    c.poly([(bx + 60, by - 60), (bx + 180, by - 60), (bx + 120, by - 100)], mix(BG, WATER_L, 0.7))
    c.arrow(bx + 120, by - 40, bx + 90, by - 120, GREEN, 4, 12)
    c.text(520, 935, '放大：前面压起小水坡，水把石头往上推', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '石头一扔进水里就沉，因为它直直地往下扎'),
                (7.2, 14, '扁石头斜着、贴着水面飞，碰水的只是后边一点，前面压起一个小水坡'),
                (14.2, 22, '水坡把石头往上推一下，它就又飞起来；越蹦越慢，最后沉下去（示意）')], y=1010)


def b155_angle(c, t, i):
    corner_tag(c, 'B155 · 约 20° 最容易蹦，转起来更稳')
    c.text(60, 96, '同一个塑料瓶盖贴着水面弹出去：平着、前端翘 20°、翘 60°，再比转与不转', 'serif', 36, INK)
    vals = [('平着', 0, 2), ('翘约 20°', 20, 5), ('翘约 60°', 60, 0), ('20° 不转', 20, 1)]
    p = min(1.0, t / 12)
    for k, (lab, ang, n) in enumerate(vals):
        x = 260 + k * 440
        y = 420
        c.line([(x - 140, y + 60), (x + 140, y + 60)], WATER_L, 4)
        a = math.radians(ang)
        c.line([(x - 60 * math.cos(a), y + 50 + 60 * math.sin(a) * 0), (x + 60 * math.cos(a), y + 50 - 60 * math.sin(a))], mix(BG, (220, 220, 230), 1.0), 10)
        if k < 3:
            c.arc(x, y - 10, 40, 14, 200, 520, SPARK, 3)
            c.text(x + 60, y - 20, '转', 'sans', 20, SPARK, 'lm')
        h = n * 70 * p
        c.rect(x - 60, 880 - h, x + 60, 880, fill=mix(BG, FIELD, 0.85), r=6)
        c.text(x, 860 - h, f'{n * p:.0f} 下', 'mono', 24, SPARK, 'mm')
        c.text(x, 920, lab, 'bold', 24, INK, 'mm')
    c.text(960, 960, '示意，以实测为准；只在浴缸或水盆里做', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '平着碰水，水坡太小托不起来；翘得太高，一头扎进水里'),
                (7.2, 14, '前端稍稍翘起 20° 左右，水坡正好把它推上去，蹦得最多'),
                (14.2, 22, '转起来的瓶盖像陀螺一样稳，角度不会乱：不转的一碰水就翻（示意）')], y=1010)


CLIPS = {
 'B153_辐条': (b153_spokes, 22), 'B153_压书': (b153_load, 22),
 'B153_片头': (titles.opening(BSER, VOL36, SB36, 3, '先秦已有「三十辐共一毂」'), 7),
 'B153_片尾': (titles.closing(BSER, VOL36, SB36, 3, '下集：木鱼为什么敲起来又响又圆？'), 7),
 'B154_空腔': (b154_cavity, 22), 'B154_开口': (b154_slot, 22),
 'B154_片头': (titles.opening(BSER, VOL36, SB36, 4, '唐宋以来寺院就敲木鱼'), 7),
 'B154_片尾': (titles.closing(BSER, VOL36, SB36, 4, '下集：石头为什么能在水面上蹦好几下？'), 7),
 'B155_托起': (b155_bounce, 22), 'B155_角度': (b155_angle, 22),
 'B155_片头': (titles.opening(BSER, VOL36, SB36, 5, '古希腊和中国都有打水漂的游戏'), 7),
 'B155_片尾': (titles.closing(BSER, VOL36, SB36, 5, '下集：捶丸高手为什么先看地面的坡？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
