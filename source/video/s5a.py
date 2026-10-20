"""第五季第一批：E39 杠杆与滑轮组、B8 被中香炉、E40 曲柄连杆 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL

S5A = [('39', '杠杆滑轮'), ('40', '曲柄连杆'), ('41', '齿轮轴承'), ('42', '马轭'), ('43', '逆风航行'), ('44', '热气球')]
SB5 = [('B8', '被中香炉'), ('B17', '指南车'), ('B7', '榫卯')]
SER5, VOL5 = '从零造物', '第五季 · 机械与交通'

WOOD = (160, 118, 76)
ROPE = (210, 190, 140)
BRASS = (205, 160, 80)
IRON = (130, 136, 142)

# ---------------------------------------------------------------- E39 杠杆与滑轮组
def e39_lever(c, t, i):
    corner_tag(c, '第 39 集 · 杠杆')
    c.text(60, 96, '支点挪一挪，力气就变了', 'serif', 40, INK)
    L = 1400
    x0 = 260
    # fulcrum ratio: a/(a+b) from 0.5 to 0.25
    r = 0.5 - 0.25 * fade(t, 5, 11)
    fx = x0 + L * r
    W = 60
    a, b = r * L, (1 - r) * L
    F = W * a / b
    lift = fade(t, 14, 19)
    ang = 0.12 * lift       # right end goes down, left up
    cy = 640
    def pt(d):  # point along beam at distance d from fulcrum (negative left)
        return fx + d * math.cos(ang), cy + d * math.sin(ang)
    lx, ly = pt(-a); rx, ry = pt(b)
    c.line([(lx, ly), (rx, ry)], WOOD, 22)
    c.poly([(fx, cy + 10), (fx - 50, cy + 110), (fx + 50, cy + 110)], MUTED)
    # weight
    c.rect(lx - 70, ly - 150, lx + 70, ly - 10, fill=(110, 100, 90), r=10)
    c.text(lx, ly - 80, f'{W} 千克', 'bold', 30, INK, 'mm')
    # force arrow
    c.arrow(rx, ry - 180, rx, ry - 20, COPPER, 8, 24)
    c.text(rx, ry - 210, f'只要约 {F:.0f} 千克的力', 'bold', 30, COPPER, 'mm')
    # arms
    c.text((lx + fx) / 2, cy + 160, f'短臂 {a / L * 4:.1f}', 'mono', 26, MUTED, 'mm')
    c.text((fx + rx) / 2, cy + 160, f'长臂 {b / L * 4:.1f}', 'mono', 26, MUTED, 'mm')
    c.text(960, 230, '重物 × 短臂 = 用力 × 长臂', 'serif', 40, mix(BG, SPARK, fade(t, 3, 4)), 'mm')
    if lift > 0.1:
        c.text(rx - 20, ry + 60, '这头压下去很长一段', 'sans', 26, mix(BG, FIELD, lift), 'rm')
        c.text(lx - 20, ly - 190, '那头只抬起一点', 'sans', 26, mix(BG, FIELD, lift), 'rm')
    caps(c, t, [(0, 5, '一根木杠、一个支点，一头放 60 千克的重物'),
                (5.2, 13, '支点往重物那边挪：重物离支点越近，另一头需要的力越小'),
                (13.2, 22, '可省力就要费距离：这头压下去一大段，那头才抬起一点点')], y=1010)

def pulley(c, x, y, r=46, col=IRON):
    c.ellipse(x, y, r, r, fill=mix(BG, col, 0.5), outline=col, width=5)
    c.ellipse(x, y, 8, 8, fill=col)

def e39_pulleys(c, t, i):
    corner_tag(c, '第 39 集 · 滑轮组')
    c.text(60, 96, '一个人，怎么吊起一头牛？', 'serif', 40, INK)
    beam = 200
    c.rect(120, beam - 20, 1800, beam, fill=WOOD, r=4)
    lift = 120 * fade(t, 8, 16)
    setups = [(380, 1, '一个定滑轮', '1 股绳'), (960, 2, '一个动滑轮', '2 股绳'), (1540, 4, '两定两动', '4 股绳')]
    for k, (cx, n, lab, ns) in enumerate(setups):
        a = fade(t, 0.5 + k * 2, 1.5 + k * 2)
        if a <= 0: continue
        load_y = 760 - lift
        if n == 1:
            pulley(c, cx, beam + 60)
            c.line([(cx - 46, beam + 60), (cx - 46, load_y - 60)], ROPE, 5)
            c.line([(cx + 46, beam + 60), (cx + 46, 640 + lift)], ROPE, 5)
            hx, hy = cx + 46, 640 + lift
        elif n == 2:
            my = load_y - 110
            pulley(c, cx, my)
            c.line([(cx - 46, beam), (cx - 46, my)], ROPE, 5)
            pulley(c, cx + 92, beam + 60, 36)
            c.line([(cx + 46, my), (cx + 56, beam + 60)], ROPE, 5)
            c.line([(cx + 128, beam + 60), (cx + 128, 560 + 2 * lift)], ROPE, 5)
            c.line([(cx, my), (cx, load_y - 60)], IRON, 5)
            hx, hy = cx + 128, 560 + 2 * lift
        else:
            my = load_y - 110
            pulley(c, cx - 40, beam + 60, 36); pulley(c, cx + 40, beam + 60, 36)
            pulley(c, cx - 40, my, 36); pulley(c, cx + 40, my, 36)
            for dx in (-76, -4, 4, 76):
                c.line([(cx + dx, beam + 60), (cx + dx, my)], ROPE, 4)
            c.line([(cx - 40, my), (cx + 40, my)], IRON, 6)
            c.line([(cx, my), (cx, load_y - 60)], IRON, 5)
            c.line([(cx + 76, beam + 60), (cx + 150, beam + 100)], ROPE, 4)
            c.line([(cx + 150, beam + 100), (cx + 150, 500 + 4 * lift * 0.6)], ROPE, 4)
            hx, hy = cx + 150, 500 + 4 * lift * 0.6
        bx = cx - 46 if n == 1 else cx
        c.rect(bx - 80, load_y - 60, bx + 80, load_y + 60, fill=(110, 100, 90), r=10)
        c.text(bx, load_y, '400 千克', 'bold', 26, INK, 'mm')
        c.arrow(hx, hy, hx, hy + 70, COPPER, 6, 18)
        c.text(cx, 900, lab, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(cx, 945, f'{ns} · 拉力约 {400 // n} 千克 · 拉 {n} 米升 1 米', 'sans', 24, mix(BG, COPPER, a), 'mm')
    caps(c, t, [(0, 8, '定滑轮只改方向；每多一股绳分担重量，拉力就少一份'),
                (8.2, 16, '4 股绳一起吊，拉力只要四分之一'),
                (16.2, 22, '代价是：重物升高 1 米，你要拉 4 米绳子。做的功一点没少')], y=1030)

# ---------------------------------------------------------------- B8 被中香炉
def b8_gimbal(c, t, i):
    corner_tag(c, 'B8 · 被中香炉')
    c.text(60, 96, '球滚来滚去，炉子为什么不翻？', 'serif', 40, INK)
    cx, cy, R = 700, 560, 300
    roll = t * 1.3
    th1 = 1.2 * math.sin(t * 1.1)
    th2 = 1.1 * math.sin(t * 0.8 + 1)
    stage = fade(t, 3, 4)
    # outer ball (rolling openwork)
    c.ellipse(cx, cy, R, R, outline=BRASS, width=6)
    for k in range(10):
        ang = roll + k * 2 * math.pi / 10
        c.ellipse(cx + (R - 30) * math.cos(ang), cy + (R - 30) * math.sin(ang), 14, 14, fill=mix(BG, BRASS, 0.5))
    # outer ring: rotates about horizontal axis -> vertical radius scales
    r1 = R - 60
    c.ellipse(cx, cy, r1, r1 * abs(math.cos(th1)) + 6, outline=mix(BG, SPARK, stage), width=6)
    c.ellipse(cx - r1, cy, 10, 10, fill=SPARK); c.ellipse(cx + r1, cy, 10, 10, fill=SPARK)
    # inner ring: rotates about vertical axis -> horizontal radius scales
    r2 = R - 110
    a2 = fade(t, 6, 7)
    c.ellipse(cx, cy, r2 * abs(math.cos(th2)) + 6, r2, outline=mix(BG, FIELD, a2), width=6)
    c.ellipse(cx, cy - r2, 10, 10, fill=FIELD); c.ellipse(cx, cy + r2, 10, 10, fill=FIELD)
    # bowl stays level
    a3 = fade(t, 9, 10)
    c.arc(cx, cy - 10, 110, 90, 0, 180, mix(BG, COPPER, a3), 10)
    c.line([(cx - 110, cy - 10), (cx + 110, cy - 10)], mix(BG, COPPER, a3), 6)
    for k in range(3):
        ph = (t * 0.5 + k / 3) % 1
        c.ellipse(cx - 20 + k * 20 + 10 * math.sin(t * 3 + k), cy - 30 - ph * 120, 8, 8, fill=mix(BG, MUTED, a3 * (1 - ph)))
    c.text(1150, 300, '最外：镂空铜球，随便滚', 'sans', 28, BRASS, 'lm')
    c.text(1150, 380, '外环：绕左右的轴转', 'sans', 28, mix(BG, SPARK, stage), 'lm')
    c.text(1150, 460, '内环：绕前后的轴转', 'sans', 28, mix(BG, FIELD, a2), 'lm')
    c.text(1150, 540, '炉碗：重心在下，始终朝下', 'sans', 28, mix(BG, COPPER, a3), 'lm')
    b = fade(t, 15, 16)
    c.rect(1130, 640, 1860, 860, fill=mix(BG, SHEET, b), r=14)
    c.text(1160, 690, '《西京杂记》：「为机环，转运四周，', 'serif', 26, mix(BG, INK, b), 'lm')
    c.text(1160, 740, '而炉体常平，可置之被褥。」', 'serif', 26, mix(BG, INK, b), 'lm')
    c.text(1160, 810, '今天叫「常平架」：船用罗盘、相机稳定器', 'sans', 24, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 3, '一个镂空的铜球，在被子里随便滚'),
                (3.2, 9, '里面套着两层环：一层绕左右转，一层绕前后转，两根轴互相垂直'),
                (9.2, 15, '中间的炉碗挂在最里面，重心在下：不管球怎么滚，它总是口朝上'),
                (15.2, 22, '西汉长安的工匠丁缓就做过这样的香炉')], y=1010)

def b8_cog(c, t, i):
    corner_tag(c, 'B8 · 重心在哪里')
    c.text(60, 96, '同样一个碗，挂在下面和顶在上面，结果完全不同', 'serif', 40, INK)
    for k, (cx, lab, stable) in enumerate([(560, '重心在支点下方', True), (1360, '重心在支点上方', False)]):
        py = 420
        c.ellipse(cx, py, 14, 14, fill=SPARK)
        c.line([(cx - 160, py), (cx + 160, py)], IRON, 6)
        if stable:
            th = 0.6 * math.exp(-0.25 * max(0, t - 3)) * math.cos(2.4 * max(0, t - 3)) if t > 3 else 0.6 * fade(t, 1, 3)
            L = 200
        else:
            th = math.pi + min(math.pi / 2, 0.05 * math.exp(1.2 * max(0, t - 4)) - 0.05) if t > 4 else math.pi + 0.05 * fade(t, 1, 3)
            L = 200
        bx, by = cx + L * math.sin(th), py + L * math.cos(th)
        c.line([(cx, py), (bx, by)], IRON, 6)
        # bowl perpendicular to rod
        nx, ny = math.cos(th), -math.sin(th)
        c.poly([(bx - 80 * nx, by - 80 * ny), (bx + 80 * nx, by + 80 * ny),
                (bx + 50 * nx + 50 * math.sin(th), by + 50 * ny + 50 * math.cos(th)),
                (bx - 50 * nx + 50 * math.sin(th), by - 50 * ny + 50 * math.cos(th))], COPPER)
        c.ellipse(bx + 25 * math.sin(th), by + 25 * math.cos(th), 10, 10, fill=NRED)
        c.text(cx, 820, lab, 'bold', 32, INK, 'mm')
        c.text(cx, 870, '晃一晃，自己摆回来' if stable else '稍微一歪，就翻过去', 'sans', 28, GREEN if stable else NRED, 'mm')
    c.text(960, 940, '红点：重心', 'sans', 24, NRED, 'mm')
    caps(c, t, [(0, 5, '把炉碗挂在支点下面，和顶在支点上面'),
                (5.2, 12, '挂在下面，一歪，重力就把它拉回来：越晃越稳'),
                (12.2, 22, '顶在上面，一歪，重力就把它推得更歪。被中香炉的秘密，就是把重心放在下面')], y=1010)

GREEN = (110, 190, 110)

# ---------------------------------------------------------------- E40 曲柄连杆
def slider_x(th, r, L):
    return r * math.cos(th) + math.sqrt(L * L - (r * math.sin(th)) ** 2)

def e40_crank(c, t, i):
    corner_tag(c, '第 40 集 · 曲柄连杆')
    c.text(60, 96, '转一圈，来回推一次', 'serif', 40, INK)
    cx, cy, r, L = 360, 560, 130, 380
    th = t * 1.6
    px, py = cx + r * math.cos(th), cy - r * math.sin(th)
    sx = cx + slider_x(th, r, L)
    c.ellipse(cx, cy, r + 40, r + 40, fill=mix(BG, WOOD, 0.5), outline=WOOD, width=6)
    c.ellipse(cx, cy, 12, 12, fill=IRON)
    c.line([(cx, cy), (px, py)], SPARK, 12)
    c.text(cx, cy + r + 80, '曲柄（转）', 'bold', 26, SPARK, 'mm')
    c.line([(px, py), (sx, cy)], FIELD, 12)
    c.ellipse(px, py, 12, 12, fill=INK)
    # guide and slider
    c.rect(cx + L - r - 60, cy - 60, cx + L + r + 160, cy - 50, fill=LINE)
    c.rect(cx + L - r - 60, cy + 50, cx + L + r + 160, cy + 60, fill=LINE)
    c.rect(sx - 10, cy - 48, sx + 110, cy + 48, fill=COPPER, r=6)
    c.text(sx + 50, cy + 100, '滑块（来回）', 'bold', 26, COPPER, 'mm')
    c.text((px + sx) / 2, cy - 90, '连杆', 'bold', 26, FIELD, 'mm')
    # plot
    gx, gy, gw, gh = 1180, 300, 640, 420
    c.rect(gx, gy, gx + gw, gy + gh, fill=SHEET, r=12)
    c.text(gx + 20, gy + 30, '滑块位置 · 曲柄转角', 'sans', 24, MUTED, 'lm')
    pts = []
    for k in range(0, 121):
        a = k / 120 * 4 * math.pi
        if a > th % (4 * math.pi) and k > 0: break
        y = slider_x(a, r, L)
        pts.append((gx + 30 + k / 120 * (gw - 60), gy + gh / 2 + (y - L) / r * 140))
    if len(pts) > 1: c.line(pts, COPPER, 5)
    c.text(gx + gw / 2, gy + gh + 40, '转两圈 · 来回两次', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '轮子上偏离中心的一个销子，叫曲柄；它和滑块之间用一根连杆连着'),
                (7.2, 14, '曲柄转一整圈，滑块就被推出去、拉回来一次'),
                (14.2, 22, '反过来也行：推拉滑块，轮子就转。东汉的水排、后来的蒸汽机，都靠它')], y=1010)

def e40_deadpoint(c, t, i):
    corner_tag(c, '第 40 集 · 死点与飞轮')
    c.text(60, 96, '推的人用力推，轮子为什么卡住不动？', 'serif', 40, INK)
    cx, cy, r, L = 420, 560, 140, 420
    fly = fade(t, 10, 11)
    if t < 10:
        th = 0.0 + 0.04 * math.sin(t * 6)   # stuck near dead point
    else:
        th = (t - 10) * 1.5
    px, py = cx + r * math.cos(th), cy - r * math.sin(th)
    sx = cx + slider_x(th, r, L)
    if fly > 0:
        c.ellipse(cx, cy, 260, 260, outline=mix(BG, IRON, fly), width=26)
        c.text(cx, cy + 320, '加一个沉重的飞轮', 'bold', 28, mix(BG, IRON, fly), 'mm')
    c.ellipse(cx, cy, r + 30, r + 30, fill=mix(BG, WOOD, 0.4), outline=WOOD, width=5)
    c.line([(cx, cy), (px, py)], SPARK, 12)
    c.line([(px, py), (sx, cy)], FIELD, 12)
    c.rect(sx - 10, cy - 45, sx + 110, cy + 45, fill=COPPER, r=6)
    if t < 10:
        c.arrow(sx + 220, cy, sx + 120, cy, NRED, 8, 24)
        c.text(sx + 60, cy - 110, '推力正好对着轮心：转不动', 'bold', 28, NRED, 'mm')
        c.line([(cx - 40, cy), (sx, cy)], mix(BG, NRED, 0.6), 2)
    else:
        c.text(sx + 60, cy - 110, '飞轮的惯性带它冲过死点', 'bold', 28, GREEN, 'mm')
    # torque plot
    gx, gy, gw, gh = 1300, 300, 540, 380
    a = fade(t, 5, 6)
    if a <= 0:
        caps(c, t, [(0, 5, '曲柄和连杆连成一条直线时，推力正对着轮子中心')], y=1010)
        return
    c.rect(gx, gy, gx + gw, gy + gh, fill=mix(BG, SHEET, a), r=12)
    c.text(gx + 20, gy + 30, '同样的推力，能转动轮子的效果', 'sans', 22, mix(BG, MUTED, a), 'lm')
    pts = [(gx + 30 + k / 100 * (gw - 60), gy + gh / 2 - abs(math.sin(k / 100 * 2 * math.pi)) * 140) for k in range(101)]
    c.line(pts, mix(BG, COPPER, a), 5)
    for xx in (0, 0.5, 1):
        c.ellipse(gx + 30 + xx * (gw - 60), gy + gh / 2, 10, 10, fill=mix(BG, NRED, a))
    c.text(gx + gw / 2, gy + gh / 2 + 50, '红点：死点（效果为零）', 'sans', 22, mix(BG, NRED, a), 'mm')
    caps(c, t, [(0, 5, '曲柄和连杆连成一条直线时，推力正对着轮子中心'),
                (5.2, 10, '这时候推得再用力，轮子也不转：这个位置叫「死点」'),
                (10.2, 22, '办法是装一个沉重的飞轮：靠惯性冲过死点。缝纫机、蒸汽机上都有它')], y=1010)

CLIPS = {
 'E39_杠杆': (e39_lever, 22), 'E39_滑轮组': (e39_pulleys, 22),
 'E39_片头': (titles.opening(SER5, VOL5, S5A, 0, '穿越北宋 · 一个人吊起一头牛'), 7),
 'E39_片尾': (titles.closing(SER5, VOL5, S5A, 0, '下集：在被窝里滚来滚去的香炉'), 7),
 'B8_常平架': (b8_gimbal, 22), 'B8_重心': (b8_cog, 22),
 'B8_片头': (titles.opening(BSER, BVOL, SB5, 0, '西汉 · 长安 · 丁缓《西京杂记》'), 7),
 'B8_片尾': (titles.closing(BSER, BVOL, SB5, 0, '下集：来回运动，怎么变成转动？'), 7),
 'E40_曲柄滑块': (e40_crank, 22), 'E40_死点': (e40_deadpoint, 22),
 'E40_片头': (titles.opening(SER5, VOL5, S5A, 1, '西汉风扇车 · 东汉水排 · 北宋'), 7),
 'E40_片尾': (titles.closing(SER5, VOL5, S5A, 1, '下集：怎么让转速变快或变慢？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
