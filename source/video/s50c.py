"""第五十季（古法解密 22.0：山居与田园）第三批：B226 鱼钩、B227 跳绳、B228 围棋 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s50a import SB50, VOL50

METAL = (180, 190, 200)
SPONGE = (230, 210, 120)
ROPE = (200, 120, 90)
BLACK = (40, 40, 45)
WHITE = (235, 235, 230)


# ---------------------------------------------------------------- B226 鱼钩
def _hook(c, x, y, barb, col):
    pts = [(x, y - 300)] + [(x, y - 300 + 3 * k * 25) for k in range(1, 4)]
    seg(c, [(x, y - 230), (x, y)], col, 10)
    arc = [(x + 60 + 60 * math.cos(math.pi - math.pi * m / 16), y + 60 * math.sin(math.pi * m / 16)) for m in range(17)]
    seg(c, arc, col, 10)
    tip = (x + 120, y - 80)
    seg(c, [arc[-1], tip], col, 10)
    if barb:
        c.poly([(tip[0], tip[1] + 30), (tip[0] - 26, tip[1] + 50), (tip[0], tip[1] + 50)], col)
    return tip


def b226_barb(c, t, i):
    corner_tag(c, 'B226 · 倒刺：顺着进去，逆着卡住')
    c.text(60, 96, '钩尖后面有一个反方向的小倒刺：往里刺时它贴着滑进去；往外拔时倒刺张开、卡在里面，就拔不出来', 'serif', 36, INK)
    for j, (lab, barb) in enumerate([('没有倒刺：一拉就出来', False), ('有倒刺：卡住拔不出', True)]):
        cx = 480 + j * 960
        c.rect(cx - 300, 420, cx + 300, 760, fill=mix(BG, SPONGE, 0.9), r=20)
        ph = (t % 11) / 11
        if ph < 0.4:
            dy = 200 * (1 - ph / 0.4)
        elif barb:
            dy = 12 * min(1.0, (ph - 0.4) / 0.2)
        else:
            dy = 190 * min(1.0, (ph - 0.4) / 0.4)
        _hook(c, cx - 60, 640 - dy, barb, mix(BG, METAL, 1.0))
        if ph > 0.4:
            c.arrow(cx - 60, 260 - dy * 0.0, cx - 60, 200, SPARK, 6, 16)
        c.text(cx, 880, lab, 'bold', 26, GREEN if barb else NRED, 'mm')
    caps(c, t, [(0, 7, '钩子刺进去：倒刺斜着，顺着方向滑进去'),
                (7.2, 14, '往外拉：倒刺的尖顶住里面，张开卡住'),
                (14.2, 22, '没有倒刺的，一拉就滑出来（实验用包好胶带的铁丝和海绵，不用真鱼钩）')], y=1010)


def b226_shape(c, t, i):
    corner_tag(c, 'B226 · 「J」形：越拉钩得越深')
    c.text(60, 96, '鱼钩弯成「J」形：钓线往上拉，钩尖却朝里、朝上转，拉力把钩尖往里带；一根直铁丝，一拉就顺着原路滑出来', 'serif', 36, INK)
    for j, (lab, J) in enumerate([('直铁丝：顺着滑出来', False), ('「J」形：拉力把钩尖往里带', True)]):
        cx = 480 + j * 960
        c.rect(cx - 300, 420, cx + 300, 760, fill=mix(BG, SPONGE, 0.9), r=20)
        ph = min(1.0, (t % 11) / 7)
        if J:
            tip = _hook(c, cx - 60, 640 - 10 * ph, False, mix(BG, METAL, 1.0))
            c.arrow(tip[0] - 40, tip[1] + 60, tip[0] - 10, tip[1] + 10, GREEN, 4, 12)
        else:
            y = 640 - 150 * ph
            seg(c, [(cx - 60, y - 300), (cx - 60, y + 40)], mix(BG, METAL, 1.0), 10)
        c.arrow(cx - 60, 220, cx - 60, 170, SPARK, 6, 16)
        c.text(cx, 880, lab, 'bold', 26, GREEN if J else NRED, 'mm')
    caps(c, t, [(0, 7, '直铁丝：拉力和铁丝在一条线上，它只会顺着进来的路退出去'),
                (7.2, 14, '「J」形：钓线拉在钩柄上，钩尖在另一边，被拉着往里转'),
                (14.2, 22, '越拉，钩尖钩得越深（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B227 跳绳
def b227_arc(c, t, i):
    corner_tag(c, 'B227 · 转起来，往外甩成弧')
    c.text(60, 96, '两头摇着绳子，绳子的每一小段都想沿直线飞出去，被两头拉住才转成圈；转得越快，往外甩得越厉害，弧越鼓', 'serif', 36, INK)
    k = int((t % 21) // 7)
    w = [2.5, 4.0, 6.0][k]
    bulge = [0.6, 0.85, 1.0][k]
    a = t * w
    lx, rx, hy = 300, 1620, 560
    R = 300 * bulge
    pts = []
    for m in range(41):
        s = m / 40
        x = lx + (rx - lx) * s
        amp = R * math.sin(math.pi * s)
        y = hy + amp * math.cos(a) * 1.0
        pts.append((x, y))
    seg(c, pts, mix(BG, ROPE, 1.0), 6)
    c.ellipse(lx, hy, 18, 18, fill=MUTED)
    c.ellipse(rx, hy, 18, 18, fill=MUTED)
    mid = pts[20]
    c.ellipse(mid[0], mid[1], 16, 16, fill=SPARK)
    c.line([(200, hy + 300), (1720, hy + 300)], mix(BG, INK, 0.5), 3)
    c.text(960, 940, ['慢摇：弧比较扁', '中速：弧鼓起来', '快摇：弧最鼓、最稳'][k], 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '慢摇：绳子软软地甩，弧不太鼓，容易打到人'),
                (7.2, 14, '摇快一点：绳子往外甩得更厉害，弧鼓起来'),
                (14.2, 22, '快摇：弧又鼓又稳，绳子最低点贴着地面扫过去（示意，侧面看）')], y=1010)


def b227_timing(c, t, i):
    corner_tag(c, 'B227 · 跳的时机比高度重要')
    c.text(60, 96, '跳的人只要在绳子扫过脚下的那一瞬间离开地面：跳一点点就够；跳得太高，落地太晚，就赶不上下一圈', 'serif', 36, INK)
    per = 1.2
    ph = (t % per) / per
    gy = 820
    cx = 960
    rope_y = gy - 20 + 520 * (0.5 + 0.5 * math.cos(2 * math.pi * ph))
    jump = 60 * max(0.0, math.sin(math.pi * (ph - 0.35) / 0.3)) if 0.35 < ph < 0.65 else 0
    c.line([(400, gy), (1520, gy)], mix(BG, INK, 0.5), 3)
    c.rect(cx - 30, gy - 260 - jump, cx + 30, gy - 40 - jump, fill=mix(BG, (110, 130, 190), 1.0), r=14)
    c.ellipse(cx, gy - 300 - jump, 36, 36, fill=mix(BG, (220, 180, 150), 1.0))
    c.line([(cx - 14, gy - 40 - jump), (cx - 14, gy - jump)], mix(BG, (110, 130, 190), 1.0), 12)
    c.line([(cx + 14, gy - 40 - jump), (cx + 14, gy - jump)], mix(BG, (110, 130, 190), 1.0), 12)
    c.line([(cx - 400, rope_y), (cx + 400, rope_y)], mix(BG, ROPE, 1.0), 6)
    if 0.4 < ph < 0.6:
        c.text(1450, 400, '绳子经过脚下：此刻离地', 'bold', 30, GREEN, 'mm')
    c.text(1450, 470, f'只跳约 {int(60 / 20)} 厘米就够（示意）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '绳子一圈里，只有很短一下扫过脚下'),
                (7.2, 14, '在那一下之前离地、之后落地，就过去了'),
                (14.2, 22, '跳太高反而落地晚，赶不上下一圈：熟练的人跳得又低又快（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B228 围棋
def _board(c, x0, y0, n, g):
    for k in range(n):
        c.line([(x0, y0 + k * g), (x0 + (n - 1) * g, y0 + k * g)], mix(BG, INK, 0.6), 2)
        c.line([(x0 + k * g, y0), (x0 + k * g, y0 + (n - 1) * g)], mix(BG, INK, 0.6), 2)


def b228_libs(c, t, i):
    corner_tag(c, 'B228 · 中间 4 气、边上 3 气、角上 2 气')
    c.text(60, 96, '一颗棋子的「气」，是它上下左右相邻的空点：放在中间有 4 口气，边上只有 3 口，角上只有 2 口', 'serif', 36, INK)
    n, g = 9, 80
    x0, y0 = 260, 220
    c.rect(x0 - 40, y0 - 40, x0 + (n - 1) * g + 40, y0 + (n - 1) * g + 40, fill=mix(BG, (200, 160, 100), 0.55), r=8)
    _board(c, x0, y0, n, g)
    stones = [((4, 4), '中间'), ((0, 4), '边上'), ((0, 0), '角上')]
    k = min(2, int(t / 7))
    (sx, sy), lab = stones[k]
    px, py = x0 + sx * g, y0 + sy * g
    c.ellipse(px, py, 34, 34, fill=BLACK, outline=MUTED, width=2)
    libs = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        qx, qy = sx + dx, sy + dy
        if 0 <= qx < n and 0 <= qy < n:
            libs.append((qx, qy))
    for (qx, qy) in libs:
        c.ellipse(x0 + qx * g, y0 + qy * g, 14, 14, fill=GREEN)
    c.text(1500, 420, f'放在{lab}', 'bold', 40, INK, 'mm')
    c.text(1500, 500, f'{len(libs)} 口气', 'bold', 48, GREEN, 'mm')
    c.text(1500, 580, f'白棋只要 {len(libs)} 颗就能围住', 'bold', 28, NRED, 'mm')
    caps(c, t, [(0, 7, '中间：上下左右都是空点，4 口气，最难被围住'),
                (7.2, 14, '边上：外面是棋盘边，少了 1 口，只剩 3 口气'),
                (14.2, 22, '角上：两边都是边，只剩 2 口气，最容易被吃掉')], y=1010)


def b228_group(c, t, i):
    corner_tag(c, 'B228 · 连成一片，气就多')
    c.text(60, 96, '几颗同色棋子上下左右连在一起，就共用所有的气：连得越长，气越多，越不容易被围住', 'serif', 36, INK)
    n, g = 9, 80
    x0, y0 = 260, 220
    c.rect(x0 - 40, y0 - 40, x0 + (n - 1) * g + 40, y0 + (n - 1) * g + 40, fill=mix(BG, (200, 160, 100), 0.55), r=8)
    _board(c, x0, y0, n, g)
    m = min(3, int(t / 6) + 1)
    group = [(3 + k, 4) for k in range(m)]
    libs = set()
    for (sx, sy) in group:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            q = (sx + dx, sy + dy)
            if q not in group and 0 <= q[0] < n and 0 <= q[1] < n:
                libs.add(q)
    for (sx, sy) in group:
        c.ellipse(x0 + sx * g, y0 + sy * g, 34, 34, fill=BLACK, outline=MUTED, width=2)
    for (qx, qy) in libs:
        c.ellipse(x0 + qx * g, y0 + qy * g, 14, 14, fill=GREEN)
    c.text(1500, 420, f'{m} 颗连在一起', 'bold', 40, INK, 'mm')
    c.text(1500, 500, f'{len(libs)} 口气', 'bold', 48, GREEN, 'mm')
    if t > 18:
        c.text(1500, 620, '9 × 9 = 81 个点，19 × 19 = 361 个点', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '1 颗在中间：4 口气'),
                (7.2, 14, '2 颗连在一起：6 口气；3 颗：8 口气'),
                (14.2, 22, '规则很简单，可 361 个点能下出的局面多到数不清（拍摄前核对）')], y=1010)


CLIPS = {
 'B226_倒刺': (b226_barb, 22), 'B226_J形': (b226_shape, 22),
 'B226_片头': (titles.opening(BSER, VOL50, SB50, 6, '新石器时代已有骨制鱼钩'), 7),
 'B226_片尾': (titles.closing(BSER, VOL50, SB50, 6, '下集：跳绳为什么摇得越快弧越鼓？'), 7),
 'B227_甩弧': (b227_arc, 22), 'B227_时机': (b227_timing, 22),
 'B227_片头': (titles.opening(BSER, VOL50, SB50, 7, '宋代已有「跳索」游戏'), 7),
 'B227_片尾': (titles.closing(BSER, VOL50, SB50, 7, '下集：围棋角上的棋子为什么最危险？'), 7),
 'B228_数气': (b228_libs, 22), 'B228_连子': (b228_group, 22),
 'B228_片头': (titles.opening(BSER, VOL50, SB50, 8, '先秦已有「弈」的记载'), 7),
 'B228_片尾': (titles.closing(BSER, VOL50, SB50, 8, '下集：秦朝为什么要「车同轨」？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
