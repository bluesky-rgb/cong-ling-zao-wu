"""第五季第二批：E41 齿轮与轴承、B17 指南车、B7 榫卯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s5a import S5A, SB5, SER5, VOL5, WOOD, IRON, BRASS, GREEN

LIGHTWOOD = (196, 156, 104)

def gear(c, cx, cy, teeth, module, ang, col, a=1.0, mark=True):
    r = teeth * module / 2
    pts = []
    for k in range(teeth * 4):
        th = ang + k * 2 * math.pi / (teeth * 4)
        rr = r + module * 0.9 if k % 4 in (1, 2) else r - module * 0.9
        pts.append((cx + rr * math.cos(th), cy + rr * math.sin(th)))
    c.poly(pts, mix(BG, col, a))
    c.ellipse(cx, cy, r * 0.35, r * 0.35, fill=mix(BG, mix(col, BG, 0.4), a))
    c.ellipse(cx, cy, 10, 10, fill=BG)
    if mark:
        mx, my = cx + r * 0.7 * math.cos(ang), cy + r * 0.7 * math.sin(ang)
        c.ellipse(mx, my, 12, 12, fill=mix(BG, NRED, a))

# ---------------------------------------------------------------- E41 齿轮与轴承
def e41_ratio(c, t, i):
    corner_tag(c, '第 41 集 · 齿数比')
    c.text(60, 96, '大齿轮转一圈，小齿轮转几圈？', 'serif', 40, INK)
    m = 14
    z1, z2 = 36, 12
    r1, r2 = z1 * m / 2, z2 * m / 2
    cx1, cy = 640, 560
    cx2 = cx1 + r1 + r2
    w = 0.9
    a1 = -t * w
    a2 = t * w * z1 / z2 + math.pi / z2   # mesh offset
    gear(c, cx1, cy, z1, m, a1, BRASS)
    gear(c, cx2, cy, z2, m, a2, IRON)
    n1 = t * w / (2 * math.pi)
    c.text(cx1, cy + r1 + 70, f'大齿轮 {z1} 齿 · 转了 {n1:.1f} 圈', 'bold', 28, BRASS, 'mm')
    c.text(cx2 + r2 + 40, cy, f'小齿轮 {z2} 齿', 'bold', 28, INK, 'lm')
    c.text(cx2 + r2 + 40, cy + 44, f'转了 {n1 * z1 / z2:.1f} 圈', 'bold', 28, INK, 'lm')
    a = fade(t, 8, 9)
    c.rect(1400, 260, 1880, 560, fill=mix(BG, SHEET, a), r=14)
    c.text(1430, 310, '转速比 = 齿数的反比', 'bold', 30, mix(BG, SPARK, a), 'lm')
    c.text(1430, 370, f'{z1} ÷ {z2} = {z1 // z2}：小的快 {z1 // z2} 倍', 'sans', 28, mix(BG, INK, a), 'lm')
    c.text(1430, 430, '转得快，力气就小', 'sans', 28, mix(BG, INK, a), 'lm')
    c.text(1430, 490, '反过来：小带大，慢而有劲', 'sans', 28, mix(BG, INK, a), 'lm')
    b = fade(t, 15, 16)
    c.text(1430, 640, '两个齿轮咬在一起：', 'sans', 26, mix(BG, MUTED, b), 'lm')
    c.text(1430, 685, '转向相反', 'bold', 28, mix(BG, FIELD, b), 'lm')
    caps(c, t, [(0, 8, '两个齿轮咬在一起，每转过一个齿，对方也转过一个齿'),
                (8.2, 15, '大的 36 齿，小的 12 齿：大的转一圈，小的要转三圈'),
                (15.2, 22, '用齿数比，就能把慢变快、把快变慢；水车接发电机，靠的就是它')], y=1010)

def e41_bearing(c, t, i):
    corner_tag(c, '第 41 集 · 滑动与滚动')
    c.text(60, 96, '同样一块重物，拖着走和滚着走', 'serif', 40, INK)
    for k, (y0, lab, roll) in enumerate([(320, '直接拖：滑动摩擦', False), (680, '下面垫上滚子：滚动摩擦', True)]):
        a = fade(t, 0.5 + k * 6, 1.5 + k * 6)
        if a <= 0: continue
        c.rect(120, y0 + 120, 1500, y0 + 140, fill=mix(BG, LINE, a))
        prog = fade(t, 1 + k * 6, 6 + k * 6 + (0 if roll else 8))
        x = 260 + prog * (700 if not roll else 900)
        if roll:
            for j in range(4):
                rx = x - 90 + j * 60
                c.ellipse(rx, y0 + 100, 20, 20, fill=mix(BG, IRON, a))
                ang = prog * 20 + j
                c.line([(rx, y0 + 100), (rx + 18 * math.cos(ang), y0 + 100 + 18 * math.sin(ang))], mix(BG, BG, a), 3)
            c.rect(x - 130, y0 - 20, x + 130, y0 + 80, fill=mix(BG, WOOD, a), r=8)
        else:
            c.rect(x - 130, y0, x + 130, y0 + 120, fill=mix(BG, WOOD, a), r=8)
            for j in range(10):
                bx = x - 120 + j * 26
                c.line([(bx, y0 + 120), (bx + 8, y0 + 130)], mix(BG, NRED, a * 0.8), 3)
        F = 12 if roll else 60
        c.arrow(x + 140, y0 + 50, x + 140 + F * 4, y0 + 50, mix(BG, COPPER, a), 8, 22)
        c.text(x + 160 + F * 4, y0 + 50, f'拉力约 {F}（示意）', 'bold', 26, mix(BG, COPPER, a), 'lm')
        c.text(140, y0 - 40, lab, 'bold', 30, mix(BG, INK, a), 'lm')
    b = fade(t, 15, 16)
    c.text(960, 960, '轴承：把轴和轴套之间的「滑」，变成钢珠的「滚」', 'serif', 32, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 6, '直接拖：两个表面的凸起互相卡住、刮擦，要很大的力'),
                (6.2, 15, '垫上圆木或钢珠：表面不再互相刮，而是一点一点「滚」过去，省力得多'),
                (15.2, 22, '轴承就是把这个办法装进轮子的轴里')], y=1035)

# ---------------------------------------------------------------- B17 指南车
def cart(c, x, y, heading, W, figure_ang, a=1.0):
    """heading: radians (0 = facing up/north on screen). draws axle with two wheels and figure arrow"""
    hx, hy = math.sin(heading), -math.cos(heading)     # forward
    rx, ry = math.cos(heading), math.sin(heading)      # right
    body = [(x + rx * W * 0.55 + hx * 50, y + ry * W * 0.55 + hy * 50), (x - rx * W * 0.55 + hx * 50, y - ry * W * 0.55 + hy * 50),
            (x - rx * W * 0.55 - hx * 50, y - ry * W * 0.55 - hy * 50), (x + rx * W * 0.55 - hx * 50, y + ry * W * 0.55 - hy * 50)]
    c.poly(body, mix(BG, WOOD, 0.7 * a))
    for s in (-1, 1):
        wx, wy = x + s * rx * W / 2, y + s * ry * W / 2
        c.line([(wx - hx * 34, wy - hy * 34), (wx + hx * 34, wy + hy * 34)], mix(BG, INK, a), 12)
    # figure arm: absolute direction figure_ang (0 = north)
    fx, fy = math.sin(figure_ang), -math.cos(figure_ang)
    c.arrow(x, y, x + fx * 80, y + fy * 80, mix(BG, NRED, a), 6, 18)

def b17_turn(c, t, i):
    corner_tag(c, 'B17 · 转弯时的两个轮子')
    c.text(60, 96, '车一转弯，两个轮子走的路就不一样长', 'serif', 40, INK)
    cx, cy, R = 760, 840, 380
    W = 160
    th = math.pi * 0.5 * fade(t, 2, 12)
    # arcs: inner R - W/2, outer R + W/2 around center (cx, cy), cart starts at angle pi (left), moving up then right (clockwise)
    for rr, col, lab in [(R - W / 2, FIELD, '内侧轮'), (R + W / 2, COPPER, '外侧轮')]:
        pts = [(cx - rr * math.cos(u), cy - rr * math.sin(u)) for u in [k / 60 * th for k in range(61)]]
        if len(pts) > 1 and th > 0.01: c.line(pts, col, 8)
    phi = th
    px, py = cx - R * math.cos(phi), cy - R * math.sin(phi)
    heading = phi
    cart(c, px, py, heading, W, math.pi)
    c.ellipse(cx, cy, 8, 8, fill=MUTED)
    c.text(cx, cy + 30, '转弯的圆心', 'sans', 22, MUTED, 'mm')
    a = fade(t, 12, 13)
    deg = th * 180 / math.pi
    c.rect(1240, 260, 1860, 640, fill=mix(BG, SHEET, a), r=14)
    c.text(1270, 310, f'车头转了 {deg:.0f}°', 'bold', 30, mix(BG, INK, a), 'lm')
    c.text(1270, 370, '外侧轮比内侧轮多走：', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 420, '轮距 × 转过的角度', 'bold', 30, mix(BG, COPPER, a), 'lm')
    c.text(1270, 490, '反过来：知道两轮多走了多少，', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 535, '就知道车转了多少度', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 600, '红箭头：木人的手，一直指南', 'sans', 24, mix(BG, NRED, a), 'lm')
    caps(c, t, [(0, 6, '车往右转弯，左边的外侧轮要绕大圈，右边的内侧轮绕小圈'),
                (6.2, 12, '两个轮子多走、少走的那一段，正好等于轮距乘以转过的角度'),
                (12.2, 22, '只要用齿轮把这段「差」变成木人反方向的转动，木人就一直指着原来的方向')], y=1010)

def b17_two_ways(c, t, i):
    corner_tag(c, 'B17 · 两种复原方案')
    c.text(60, 96, '车里的齿轮怎么排？至今有两种复原方案', 'serif', 40, INK)
    for k, (cx, title, lines, col) in enumerate([
        (520, '离合齿轮（宋代记载）', ['转弯时，车辕带动绳索和重锤', '让一边的小齿轮咬合', '外侧轮的转动传给木人的转盘', '直行时两边都脱开'], COPPER),
        (1400, '差动齿轮（现代复原）', ['两个轮子各接一边的齿轮', '中间的齿轮只「感受」两边的差', '差为零：木人不动', '有差：木人反向转动'], FIELD)]):
        a = fade(t, 0.5 + k * 9, 1.5 + k * 9)
        if a <= 0: continue
        c.rect(cx - 400, 200, cx + 400, 880, fill=mix(BG, SHEET, a), outline=mix(BG, col, a), width=4, r=18)
        c.text(cx, 250, title, 'bold', 32, mix(BG, col, a), 'mm')
        # small mechanism sketch
        rot = t * 1.2
        if k == 0:
            gear(c, cx - 150, 430, 24, 8, rot, mix(BG, BRASS, a), a)
            eng = 0.5 + 0.5 * math.sin(t * 1.5)
            gear(c, cx + 20, 430 - 40 * (1 - eng), 10, 8, -rot * 2.4, mix(BG, IRON, a), a)
            gear(c, cx + 150, 430, 24, 8, -rot * (1 if eng > 0.5 else 0), mix(BG, BRASS, a), a)
            c.text(cx + 20, 330, '升降的小齿轮', 'sans', 22, mix(BG, MUTED, a), 'mm')
        else:
            gear(c, cx - 170, 430, 20, 8, rot, mix(BG, BRASS, a), a)
            gear(c, cx + 170, 430, 20, 8, -rot * 0.6, mix(BG, BRASS, a), a)
            gear(c, cx, 430, 12, 8, rot * 0.2, mix(BG, IRON, a), a)
            c.text(cx, 330, '中间的齿轮只看「差」', 'sans', 22, mix(BG, MUTED, a), 'mm')
        for j, s in enumerate(lines):
            c.text(cx - 340, 600 + j * 56, s, 'sans', 28, mix(BG, INK, a), 'lm')
    b = fade(t, 17, 18)
    c.text(960, 950, '原物都没有留下：讲的是「复原方案」，不是定论', 'serif', 32, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 9, '《宋史》记载了燕肃、吴德仁造的指南车：靠绳索和重锤，转弯时让小齿轮咬合'),
                (9.2, 17, '今天很多复原模型改用差动齿轮：汽车的差速器也是这个原理'),
                (17.2, 22, '哪种更接近古人？原物都没有留下')], y=1035)

# ---------------------------------------------------------------- B7 榫卯
def b7_joint(c, t, i):
    corner_tag(c, 'B7 · 榫和卯')
    c.text(60, 96, '一凸一凹，怎么就咬住了？', 'serif', 40, INK)
    ins = fade(t, 2, 8)
    # mortise piece (vertical post)
    px = 1000
    c.rect(px - 90, 200, px + 90, 900, fill=LIGHTWOOD, r=6)
    c.rect(px - 90, 480, px + 90, 600, fill=mix(LIGHTWOOD, BG, 0.55))
    c.text(px + 130, 540, '卯：凿出的孔', 'bold', 28, INK, 'lm')
    # tenon piece (beam) sliding in from left
    bx = 200 + 610 * ins
    c.rect(bx - 520, 440, bx, 640, fill=WOOD, r=6)
    c.rect(bx, 480, bx + 180 * ins + 2, 600, fill=WOOD)
    c.text(bx - 260, 400, '榫：削出的凸头', 'bold', 28, INK, 'mm')
    a = fade(t, 9, 10)
    if a > 0:
        for y in (500, 580):
            c.arrow(px - 90 + 40, y, px - 90 + 10, y, mix(BG, SPARK, a), 4, 12)
            c.arrow(px + 90 - 40, y, px + 90 - 10, y, mix(BG, SPARK, a), 4, 12)
        c.arrow(px, 380, px, 470, mix(BG, NRED, a), 6, 18)
        c.text(px + 110, 400, '上面压下来的重量', 'sans', 24, mix(BG, NRED, a), 'lm')
        c.text(px - 120, 700, '木头挤紧、摩擦：拉不出来', 'sans', 26, mix(BG, SPARK, a), 'rm')
    b = fade(t, 15, 16)
    c.rect(1240, 700, 1860, 900, fill=mix(BG, SHEET, b), r=14)
    c.text(1270, 750, '河姆渡遗址：约七千年前', 'bold', 28, mix(BG, INK, b), 'lm')
    c.text(1270, 800, '已经有榫卯木构件', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1270, 850, '应县木塔（1056 年）全木结构，不用一枚铁钉', 'sans', 22, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 8, '一根木头削出凸头叫「榫」，另一根凿出孔叫「卯」，把榫插进卯里'),
                (8.2, 15, '上面的重量把它们压紧，木头之间又挤又摩擦：不用钉子也拔不出来'),
                (15.2, 22, '七千年前的河姆渡就有榫卯；九百多年前的应县木塔，全靠它站着')], y=1010)

def frame_pts(sway, x0, ybase, w, h):
    return [(x0, ybase), (x0 + sway, ybase - h), (x0 + w + sway, ybase - h), (x0 + w, ybase)]

def b7_sway(c, t, i):
    corner_tag(c, 'B7 · 晃一晃')
    c.text(60, 96, '地震来了：焊死的框架和榫卯框架', 'serif', 40, INK)
    T = max(0, t - 3)
    for k, (x0, lab, damp, col) in enumerate([(220, '连接处焊死（刚性）', 0.06, IRON), (1100, '榫卯连接（会微微滑动）', 0.35, WOOD)]):
        amp = 70 * math.exp(-damp * T) * math.sin(3.2 * T) if t > 3 else 70 * math.sin(math.pi / 2 * fade(t, 1, 3))
        ground = 18 * math.sin(6 * t) * (1 - fade(t, 2.5, 3))
        pts = frame_pts(amp, x0 + ground, 820, 560, 480)
        c.rect(x0 - 60 + ground, 820, x0 + 620 + ground, 850, fill=LINE)
        c.line([pts[0], pts[1]], col, 26); c.line([pts[3], pts[2]], col, 26); c.line([pts[1], pts[2]], col, 26)
        for p in pts[1:3]:
            c.ellipse(p[0], p[1], 20, 20, fill=NRED if k == 0 else SPARK)
        c.text(x0 + 280, 270, lab, 'bold', 30, INK, 'mm')
        # amplitude trace
        tr = []
        for j in range(0, 101):
            tt = j / 100 * 19
            v = 70 * math.exp(-damp * tt) * math.sin(3.2 * tt)
            if tt > T: break
            tr.append((x0 + j * 5.6, 940 - v * 0.5))
        if len(tr) > 1: c.line(tr, mix(BG, col, 0.9), 3)
    a = fade(t, 12, 13)
    c.text(960, 210, '榫卯接头每晃一下都会微微摩擦，把晃动的能量变成热：晃得更快停下来', 'sans', 26, mix(BG, SPARK, a), 'mm')
    caps(c, t, [(0, 3, '同样大小的两个框架，地面一晃'),
                (3.2, 12, '连接处焊死的，晃起来要很久才停'),
                (12.2, 22, '榫卯连接会微微滑动、摩擦，把晃动的能量一点点「吃掉」（示意）')], y=1010)

CLIPS = {
 'E41_齿数比': (e41_ratio, 22), 'E41_滚动': (e41_bearing, 22),
 'E41_片头': (titles.opening(SER5, VOL5, S5A, 2, '穿越北宋 · 让转速变快变慢'), 7),
 'E41_片尾': (titles.closing(SER5, VOL5, S5A, 2, '下集：车怎么转弯，木人的手都指南？'), 7),
 'B17_转弯': (b17_turn, 22), 'B17_两种方案': (b17_two_ways, 22),
 'B17_片头': (titles.opening(BSER, BVOL, SB5, 1, '北宋 · 1027 年 · 燕肃'), 7),
 'B17_片尾': (titles.closing(BSER, BVOL, SB5, 1, '下集：不用一根钉子的木头'), 7),
 'B7_榫卯': (b7_joint, 22), 'B7_晃动': (b7_sway, 22),
 'B7_片头': (titles.opening(BSER, BVOL, SB5, 2, '约七千年前 · 河姆渡'), 7),
 'B7_片尾': (titles.closing(BSER, BVOL, SB5, 2, '下集：换一副套具，马能多拉几倍？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
