"""第十七季（第五层）收尾：E101 人造卫星、第十七季特辑（第五层回顾） —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s17a import S17A, SER17, VOL17

BALL = (210, 220, 80)
EARTH = (70, 120, 170)
LAND = (90, 150, 90)

# ---------------------------------------------------------------- E101 人造卫星
def e101_tangent(c, t, i):
    corner_tag(c, '第 101 集 · 一松手，沿切线飞走')
    c.text(60, 96, '绳子一直把球往圆心拽，球才拐弯', 'serif', 40, INK)
    cx, cy, R = 700, 600, 260
    w = 1.6
    rel = 9.0
    c.ellipse(cx, cy, R, R, outline=mix(BG, LINE, 0.9), width=2)
    c.ellipse(cx, cy, 16, 16, fill=COPPER)
    if t < rel:
        ang = w * t
        bx, by = cx + R * math.cos(ang), cy + R * math.sin(ang)
        c.line([(cx, cy), (bx, by)], INK, 3)
        # pull toward center
        ux, uy = (cx - bx) / R, (cy - by) / R
        c.arrow(bx, by, bx + ux * 110, by + uy * 110, NRED, 5, 18)
        c.text(bx + ux * 140, by + uy * 140, '拉力', 'bold', 24, NRED, 'mm')
        # velocity
        vx, vy = -math.sin(ang), math.cos(ang)
        c.arrow(bx, by, bx + vx * 130, by + vy * 130, GREEN, 4, 16)
        c.ellipse(bx, by, 26, 26, fill=BALL)
    else:
        ang = w * rel
        bx0, by0 = cx + R * math.cos(ang), cy + R * math.sin(ang)
        vx, vy = -math.sin(ang), math.cos(ang)
        d = min((t - rel) * w * R, 520)
        bx, by = bx0 + vx * d, by0 + vy * d
        seg(c, [(bx0 + vx * s, by0 + vy * s) for s in range(0, int(d) + 1, 8)], mix(BG, GREEN, 0.6), 3)
        c.ellipse(bx0, by0, 8, 8, fill=NRED)
        c.text(bx0 + 30, by0 + 34, '松手', 'sans', 22, NRED, 'lm')
        c.ellipse(bx, by, 26, 26, fill=BALL)
    a = fade(t, 13, 14)
    if a > 0:
        c.rect(1180, 300, 1840, 760, fill=mix(BG, SHEET, a), r=14)
        c.text(1510, 350, '拉力要多大？', 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(1510, 420, 'F = m v² ÷ r', 'mono', 34, mix(BG, SPARK, a), 'mm')
        for k, (sp, f) in enumerate((('转速 ×1', 1), ('转速 ×2', 4))):
            y = 500 + k * 110
            c.text(1230, y, sp, 'sans', 26, mix(BG, INK, a), 'lm')
            c.rect(1400, y - 18, 1400 + 90 * f, y + 18, fill=mix(BG, NRED, a), r=6)
            c.text(1420 + 90 * f, y, f'拉力 ×{f}', 'sans', 24, mix(BG, NRED, a), 'lm')
        c.text(1510, 720, '转快一倍，拉力变 4 倍（以实测为准）', 'sans', 22, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 8, '甩着的球每时每刻都想直着飞，是绳子一直把它往圆心拽，它才拐成一个圈'),
                (8.2, 14, '一松手，拉力没了：球不往外甩，也不往里掉，而是顺着切线直直飞走'),
                (14.2, 22, '转得越快，需要的拉力越大：快一倍，拉力要四倍')], y=1010)


# Newton's cannon: integrate in screen units
EC, ER, R0 = (960, 640), 300, 340
GM = 330.0 ** 2 * R0           # circular speed at R0 is 330 px/s

def _traj(v):
    x, y, vx, vy = EC[0], EC[1] - R0, v, 0.0
    pts = [(x, y)]
    dt = 0.01
    T = 2 * math.pi * R0 / 330 * 1.02
    tt = 0
    while tt < T:
        dx, dy = x - EC[0], y - EC[1]
        r = math.hypot(dx, dy)
        if r < ER:
            break
        ax, ay = -GM * dx / r ** 3, -GM * dy / r ** 3
        vx += ax * dt; vy += ay * dt
        x += vx * dt; y += vy * dt
        tt += dt
        pts.append((x, y))
    return pts

SHOTS = [(0.6, '慢'), (0.8, '快'), (0.93, '更快'), (1.0, '每秒约 7.9 千米')]
TRAJ = [_traj(330 * f) for f, _ in SHOTS]

def e101_cannon(c, t, i):
    corner_tag(c, '第 101 集 · 牛顿的山顶大炮')
    c.text(60, 96, '扔得越快落得越远；快到一定程度，就再也落不了地', 'serif', 40, INK)
    c.ellipse(EC[0], EC[1], ER, ER, fill=EARTH)
    c.ellipse(EC[0] - 90, EC[1] - 60, 110, 70, fill=LAND)
    c.ellipse(EC[0] + 120, EC[1] + 90, 90, 60, fill=LAND)
    top = EC[1] - ER
    c.poly([(EC[0] - 70, top + 12), (EC[0], EC[1] - R0 + 4), (EC[0] + 70, top + 12)], (140, 120, 100))
    cols = [MUTED, COPPER, SPARK, GREEN]
    for k, ((f, lab), pts) in enumerate(zip(SHOTS, TRAJ)):
        t0 = 1 + k * 4
        span = 3 if k < 3 else 6
        p = fade(t, t0, t0 + span)
        if p <= 0: continue
        n = max(2, int(len(pts) * p))
        seg(c, pts[:n], cols[k], 4)
        x, y = pts[n - 1]
        c.ellipse(x, y, 10, 10, fill=cols[k])
        if k < 3:
            ex, ey = pts[-1]
            if p >= 1:
                dx, dy = ex - EC[0], ey - EC[1]; rr = math.hypot(dx, dy)
                c.text(ex + dx / rr * 70, ey + dy / rr * 70, lab, 'bold', 24, cols[k], 'mm')
    a = fade(t, 18, 19)
    if a > 0:
        c.text(EC[0] + R0 + 40, EC[1] + 110, '每秒约 7.9 千米', 'bold', 28, mix(BG, GREEN, a), 'lm')
        c.text(EC[0] + R0 + 40, EC[1] + 154, '一直在掉，', 'sans', 24, mix(BG, INK, a), 'lm')
        c.text(EC[0] + R0 + 40, EC[1] + 190, '地面也一直弯下去', 'sans', 24, mix(BG, INK, a), 'lm')
    b = fade(t, 12, 13)
    if b > 0:
        c.rect(60, 760, 560, 960, fill=mix(BG, SHEET, b), r=12)
        c.text(310, 800, '每往前飞约 8 千米', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(310, 845, '地面弯下去约 5 米', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(310, 890, '1 秒里也正好落下约 5 米', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(310, 935, '（数值拍摄前核对）', 'sans', 20, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '牛顿想象在高山顶上架一门大炮，水平往前打'),
                (6.2, 13, '打得越快，炮弹落得越远，因为地面是弯的，落点也跟着往后退'),
                (13.2, 22, '快到每秒约 7.9 千米，它往下掉的弯和地球的弯一样：一直在掉，却永远落不了地')], y=1010)


# ---------------------------------------------------------------- 第十七季特辑
OLD17 = [('矿石收音机', '85'), ('开关与逻辑门', '81'), ('雷达', '84'), ('无线电', '76'), ('光纤', '89'), ('透镜', '52'),
         ('电视', '82'), ('太阳能电池', '77'), ('照相', '55'), ('莱顿瓶', '01'), ('计算机', '91'), ('九连环', 'B55'),
         ('电报', '57'), ('磁生电', '04'), ('电磁铁', '56'), ('电动机', '58'), ('机翼', '86'), ('竹蜻蜓', 'B40'),
         ('内燃机', '78'), ('火箭', '88'), ('卫星定位', '90'), ('影子测地球', '47')]
NEW17 = [('晶体管', '92', ['矿石收音机', '开关与逻辑门']), ('微波炉', '93', ['雷达', '无线电']), ('激光', '94', ['光纤', '透镜']),
         ('数码相机', '95', ['电视', '太阳能电池', '照相']), ('触摸屏', '96', ['莱顿瓶', '计算机']), ('二维码', '97', ['电视', '计算机', '九连环']),
         ('互联网', '98', ['电报', '光纤', '计算机']), ('磁悬浮', '99', ['磁生电', '电磁铁', '电动机']),
         ('直升机', '100', ['机翼', '竹蜻蜓', '内燃机']), ('人造卫星', '101', ['火箭', '卫星定位', '影子测地球'])]

def s17_layer(c, t, i):
    corner_tag(c, '第十七季特辑 · 第五层')
    c.text(60, 118, '第五层：口袋里的科技', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD17):
        pos[name] = (340, 200 + k * 36)
    for k, (name, num, deps) in enumerate(NEW17):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 168, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第十七季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW17):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD17:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW17):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第五层的十集：每一样都揣在口袋里、摆在厨房里、挂在天上'),
                (8.2, 16, '收音机和逻辑门长出晶体管，雷达长出微波炉，光纤和透镜长出激光'),
                (16.2, 24, '电视、计算机和九连环长出二维码；电报、光纤和计算机连成互联网'),
                (24.2, 30, '最后，火箭加上用影子量出的地球：一颗一直在掉、却永远落不了地的卫星')], y=1040)


CLIPS = {
 'E101_切线': (e101_tangent, 22), 'E101_牛顿大炮': (e101_cannon, 22),
 'E101_片头': (titles.opening(SER17, VOL17, S17A, 9, '1957 年斯普特尼克 1 号 · 1970 年东方红一号'), 7),
 'E101_片尾': (titles.closing(SER17, VOL17, S17A, 9, '下集：第十七季特辑 · 第五层回顾'), 7),
 'S17_第五层': (s17_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
