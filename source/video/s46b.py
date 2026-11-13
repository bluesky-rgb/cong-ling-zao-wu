"""第四十六季（古法解密 20.0）第二批：B203 规矩、B204 草鞋、B205 秧马 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s46a import SB46, VOL46, ROD

ROPE = (200, 170, 110)
TILE = (200, 200, 195)
MUD = (110, 85, 60)


# ---------------------------------------------------------------- B203 规矩
def b203_circle(c, t, i):
    corner_tag(c, 'B203 · 规：到中心一样远，就是圆')
    c.text(60, 96, '规就是圆规：一头钉住不动，另一头绕着它转，笔尖到中心的距离处处一样，画出来的就是一个正圆', 'serif', 36, INK)
    cx, cy, R = 700, 560, 280
    p = min(1.0, t / 10)
    a_end = 2 * math.pi * p
    pts = [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in [a_end * k / 120 for k in range(121)]]
    if len(pts) > 1:
        c.line(pts, SPARK, 5)
    px, py = cx + R * math.cos(a_end), cy + R * math.sin(a_end)
    c.line([(cx, cy), (px, py)], mix(BG, ROPE, 1.0), 4)
    c.ellipse(cx, cy, 12, 12, fill=INK)
    c.ellipse(px, py, 12, 12, fill=SPARK)
    if p >= 1:
        for k in range(6):
            a = k * math.pi / 3 + 0.3
            c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], mix(BG, GREEN, 0.6), 2)
        c.text(cx, cy + R + 60, '6 条半径一样长', 'bold', 26, GREEN, 'mm')
    x0 = 1300
    c.text(x0 + 200, 330, '手画的圆', 'sans', 24, MUTED, 'mm')
    r = random.Random(3)
    pts2 = []
    for k in range(61):
        a = 2 * math.pi * k / 60
        rr = 140 + 22 * math.sin(3 * a + 1) + r.uniform(-6, 6)
        pts2.append((x0 + 200 + rr * math.cos(a), 560 + rr * math.sin(a)))
    c.line(pts2, mix(BG, NRED, 0.8), 4)
    caps(c, t, [(0, 7, '一根绳子一头系图钉钉在纸上，一头系铅笔，拉直绕一圈'),
                (7.2, 14, '笔尖始终离图钉一样远：画出来的线就是正圆'),
                (14.2, 22, '用尺子量圆心到圆上 6 个点的距离，都一样长（以实测为准）')], y=1010)


def b203_square(c, t, i):
    corner_tag(c, 'B203 · 矩：3、4、5 拉出直角')
    c.text(60, 96, '矩是两边成直角的曲尺；没有曲尺时，把绳子等分 12 段，按 3、4、5 段围成三角形，最大的角就是直角', 'serif', 36, INK)
    ox, oy = 500, 820
    u = 110
    p = min(1.0, t / 10)
    A = (ox, oy)
    Bp = (ox + 4 * u, oy)
    Cp = (ox, oy - 3 * u)
    pts = [A, Bp, Cp, A]
    segs = [(A, Bp, 4), (Bp, Cp, 5), (Cp, A, 3)]
    tot = 12
    done = 0
    for a, b, n in segs:
        for k in range(n):
            if done >= tot * p:
                break
            f0, f1 = k / n, (k + 1) / n
            x0 = a[0] + (b[0] - a[0]) * f0
            y0 = a[1] + (b[1] - a[1]) * f0
            x1 = a[0] + (b[0] - a[0]) * f1
            y1 = a[1] + (b[1] - a[1]) * f1
            c.line([(x0, y0), (x1, y1)], mix(BG, ROPE, 1.0), 6)
            c.ellipse(x1, y1, 9, 9, fill=INK)
            done += 1
    c.ellipse(A[0], A[1], 9, 9, fill=INK)
    if p >= 1:
        c.rect(ox, oy - 40, ox + 40, oy, outline=GREEN, width=4)
        c.text(ox + 2 * u, oy + 50, '4 段', 'bold', 26, INK, 'mm')
        c.text(ox - 50, oy - 1.5 * u, '3 段', 'bold', 26, INK, 'rm')
        c.text(ox + 2.3 * u, oy - 1.9 * u, '5 段', 'bold', 26, INK, 'lm')
        c.text(ox + 70, oy - 60, '90°', 'bold', 28, GREEN, 'lm')
    x0 = 1250
    c.poly([(x0, 300), (x0 + 60, 300), (x0 + 60, 700), (x0 + 400, 700), (x0 + 400, 760), (x0, 760)], mix(BG, ROD, 1.0))
    c.text(x0 + 200, 820, '曲尺（矩）', 'bold', 26, INK, 'mm')
    c.text(x0 + 230, 400, '3×3 + 4×4 = 5×5\n（勾三股四弦五）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '把一张纸对折再对折，折出来的角就是一个直角，可以当简易的矩'),
                (7.2, 14, '一根绳子等分成 12 段，三个人拉住第 0、3、7 段处，围成 3、4、5 的三角形'),
                (14.2, 22, '三条边一拉直，3 和 4 夹着的那个角就是直角：在野外也能找直角（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B204 草鞋
def b204_grip(c, t, i):
    corner_tag(c, 'B204 · 凹凸嵌住地面')
    c.text(60, 96, '湿石板表面有很多小坑：光滑的塑料底只碰到坑的尖顶，一滑就走；草绳编的鞋底凹凸不平，能嵌进小坑里卡住', 'serif', 36, INK)
    for j, (lab, rope) in enumerate([('光滑鞋底：只碰尖顶，一推就滑', False), ('草绳鞋底：嵌进小坑，卡得住', True)]):
        ox, gy = 480 + j * 960, 640
        r = random.Random(4)
        pts = [(ox - 360, gy + 60)]
        for k in range(37):
            x = ox - 360 + k * 20
            pts.append((x, gy - (14 if k % 2 == 0 else 0) + r.uniform(-3, 3)))
        pts.append((ox + 360, gy + 60))
        c.poly(pts, mix(BG, TILE, 0.85))
        slide = 0 if rope else 40 * (0.5 + 0.5 * math.sin(t * 2))
        bx = ox - 150 + slide
        if rope:
            c.rect(bx, gy - 110, bx + 300, gy - 40, fill=mix(BG, WOOD, 1.0), r=8)
            for k in range(15):
                x = bx + 10 + k * 20
                c.ellipse(x, gy - 22, 11, 14, fill=mix(BG, ROPE, 1.0))
        else:
            c.rect(bx, gy - 100, bx + 300, gy - 30, fill=mix(BG, WOOD, 1.0), r=8)
            c.rect(bx, gy - 30, bx + 300, gy - 14, fill=mix(BG, (220, 220, 230), 1.0))
        c.arrow(bx + 320, gy - 70, bx + 420, gy - 70, SPARK, 5, 16)
        c.text(ox, gy + 140, lab, 'bold', 24, GREEN if rope else NRED, 'mm')
    caps(c, t, [(0, 7, '两块一样的小木块，一块底贴塑料片，一块底缠满麻绳'),
                (7.2, 14, '在湿瓷砖上用行李秤拉：塑料底轻轻一拉就滑，麻绳底要拉得更用力'),
                (14.2, 22, '粗糙的绳子能嵌进石面的小坑，摩擦力大得多（以实测为准）')], y=1010)


def b204_drain(c, t, i):
    corner_tag(c, 'B204 · 把水挤到缝里排走')
    c.text(60, 96, '光滑鞋底和湿地之间夹着一层水膜，像垫了润滑油；草鞋的绳缝把水挤走，鞋底才真正踩到地面', 'serif', 36, INK)
    for j, (lab, rope) in enumerate([('光滑底：被水膜垫起来', False), ('草绳底：水从缝里挤走', True)]):
        ox, gy = 480 + j * 960, 640
        c.rect(ox - 360, gy, ox + 360, gy + 80, fill=mix(BG, TILE, 0.85))
        film = 18 if not rope else 4
        c.rect(ox - 200, gy - film, ox + 200, gy, fill=mix(BG, WATER, 0.9))
        c.rect(ox - 200, gy - film - 80, ox + 200, gy - film, fill=mix(BG, WOOD, 1.0), r=8)
        if rope:
            for k in range(10):
                x = ox - 180 + k * 40
                c.rect(x - 6, gy - film - 18, x + 6, gy - film, fill=mix(BG, WATER, 1.0))
                yy = gy - film - 30 - ((t * 60 + k * 13) % 40)
                c.ellipse(x, yy, 4, 4, fill=WATER_L)
        else:
            for k in range(12):
                x = ox - 190 + k * 34
                c.line([(x, gy - film + 2), (x + 20, gy - film + 2)], WATER_L, 2)
        c.text(ox, gy + 140, lab, 'bold', 24, GREEN if rope else NRED, 'mm')
    caps(c, t, [(0, 7, '雨天的石板路上积着一层薄水，光滑的鞋底踩上去，会被水膜托起来'),
                (7.2, 14, '草鞋底是一道道搓紧的草绳，绳和绳之间有缝，脚一踩，水就被挤进缝里'),
                (14.2, 22, '把湿瓷砖慢慢斜起来：缠绳的木块要斜得更厉害才开始下滑（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B205 秧马
def b205_pressure(c, t, i):
    corner_tag(c, 'B205 · 同样的重量，摊开就不陷')
    c.text(60, 96, '用脚踩，重量全压在一小块泥上，一踩就陷；坐在宽木板上，重量摊到一大片泥上，就浅浅地浮着', 'serif', 36, INK)
    gy = 600
    c.rect(0, gy, W, 960, fill=mix(BG, MUD, 1.0))
    c.rect(0, gy - 30, W, gy, fill=mix(BG, WATER, 0.5))
    p = min(1.0, t / 8)
    for k, (lab, area, x) in enumerate([('瓶子直接立在泥上', 1, 360), ('垫一块小木片', 4, 960), ('放在大木板上', 20, 1560)]):
        depth = 220 / area * p
        w = 40 * math.sqrt(area) if area > 1 else 40
        c.rect(x - w, gy + depth - 20, x + w, gy + depth, fill=mix(BG, WOOD, 1.0)) if area > 1 else None
        bx = x
        c.rect(bx - 34, gy + depth - 20 - 160, bx + 34, gy + depth - 20, fill=mix(BG, (120, 180, 230), 0.9), r=10)
        c.text(x, gy + 280, lab, 'bold', 24, INK, 'mm')
        c.text(x, gy + 320, f'陷下约 {depth / 22:.0f} 份（示意）', 'mono', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '托盘里铺一层湿沙，把同一瓶水直接立上去，压出一个深坑'),
                (7.2, 14, '垫一块小木片，坑浅了；放在大木板上，几乎只压出一道印'),
                (14.2, 22, '重量一样，压的面积越大，每一小块泥受的压力越小：这叫压强（示意）')], y=1010)


def b205_slide(c, t, i):
    corner_tag(c, 'B205 · 前头翘起，像雪橇一样滑')
    c.text(60, 96, '秧马的底板前头往上翘：往前推时压着泥面往上滑，不会扎进泥里；人坐在上面用脚一蹬，就在田里滑行', 'serif', 36, INK)
    gy = 640
    c.rect(0, gy, W, 960, fill=mix(BG, MUD, 1.0))
    for j, (lab, curl) in enumerate([('平头：一推就往泥里铲', False), ('翘头：顺着泥面滑上去', True)]):
        y0 = gy
        x = 300 + ((t * 80) % 500) * (1 if curl else 0.25) + j * 900
        dig = 0 if curl else min(40, (t * 80) % 500 * 0.12)
        pts = [(x, y0 - 10 + dig), (x + 300, y0 - 10 + dig)]
        if curl:
            pts.append((x + 360, y0 - 60))
        else:
            pts.append((x + 320, y0 + 10 + dig))
        c.line(pts, mix(BG, WOOD, 1.0), 16)
        c.rect(x + 80, y0 - 120 + dig, x + 200, y0 - 26 + dig, fill=mix(BG, (200, 160, 110), 1.0), r=10)
        if not curl:
            c.poly([(x + 320, y0 + dig), (x + 380, y0 - 20), (x + 380, y0 + 20 + dig)], mix(BG, MUD, 0.6))
        c.arrow(x - 80, y0 - 70, x - 10, y0 - 70, SPARK, 5, 16)
        c.text(400 + j * 900, gy + 200, lab, 'bold', 24, GREEN if curl else NRED, 'mm')
    caps(c, t, [(0, 7, '北宋的秧马像一只小船，农民骑在上面插秧、拔秧'),
                (7.2, 14, '平头的木板往前推，前沿会铲进泥里，越推越费劲'),
                (14.2, 22, '前头翘起，推的时候压着泥面往上滑：雪橇、滑雪板也是这样（以实测为准）')], y=1010)


CLIPS = {
 'B203_画圆': (b203_circle, 22), 'B203_直角': (b203_square, 22),
 'B203_片头': (titles.opening(BSER, VOL46, SB46, 3, '汉代画像石中伏羲、女娲手持规和矩'), 7),
 'B203_片尾': (titles.closing(BSER, VOL46, SB46, 3, '下集：湿石板路上，为什么穿草鞋不滑？'), 7),
 'B204_嵌合': (b204_grip, 22), 'B204_排水': (b204_drain, 22),
 'B204_片头': (titles.opening(BSER, VOL46, SB46, 4, '先秦已有草编的鞋（草屦）'), 7),
 'B204_片尾': (titles.closing(BSER, VOL46, SB46, 4, '下集：骑着秧马，为什么在烂泥田里不陷？'), 7),
 'B205_压强': (b205_pressure, 22), 'B205_滑行': (b205_slide, 22),
 'B205_片头': (titles.opening(BSER, VOL46, SB46, 5, '北宋苏轼作《秧马歌》'), 7),
 'B205_片尾': (titles.closing(BSER, VOL46, SB46, 5, '下集：抬轿子，前后两个人谁更累？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
