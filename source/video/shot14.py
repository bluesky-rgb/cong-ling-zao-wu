import math, random
from lib import *

random.seed(7)
L0, L1, TH = 520, 1400, 84          # wire ends, thickness
EL = [(random.random(), random.uniform(-0.38, 0.38), random.uniform(0, 6.28), random.uniform(0.8, 1.6)) for _ in range(46)]
IONS = [(i / 21, (j - 1) * 0.3) for i in range(1, 21) for j in range(3)]

def wire_y(t):
    # rest at 640, accelerate 4-5, constant speed to 12.5, decelerate to 13.5
    if t < 4: return 640
    v = 36.0  # px / s at full speed
    def dist(tt):
        if tt < 4: return 0
        if tt < 5: return v * (tt - 4) ** 2 / 2
        if tt < 12.5: return v * 0.5 + v * (tt - 5)
        if tt < 13.5:
            u = tt - 12.5
            return v * 0.5 + v * 7.5 + v * (u - u * u / 2)
        return v * 0.5 + v * 7.5 + v * 0.5
    return 640 - dist(t)

def speed(t):
    if t < 4 or t > 13.5: return 0.0
    if t < 5: return t - 4
    if t < 12.5: return 1.0
    return 1 - (t - 12.5)

# separation s(t): first-order response to speed
S = []
s = 0.0
for i in range(int(22 * FPS) + 2):
    tt = i / FPS
    s += (speed(tt) - s) * (1 / FPS) / 0.9
    S.append(s)
def sep(t): return S[min(int(t * FPS), len(S) - 1)]

def draw(c, t, i):
    corner_tag(c, '镜头 14 · 本质层')
    c.text(60, 96, '把镜头放大到导线里面', 'serif', 40, mix(BG, INK, fade(t, 0, 1)))
    # field crosses
    xc = mix(BG, FIELD, 0.45)
    for gx in range(260, 1680, 96):
        for gy in range(210, 860, 96):
            if (gx > 1470 and gy < 350) or (gx < 430 and gy > 720): continue
            c.line([(gx - 9, gy - 9), (gx + 9, gy + 9)], xc, 3)
            c.line([(gx - 9, gy + 9), (gx + 9, gy - 9)], xc, 3)
    # legend
    c.rect(1500, 150, 1860, 330, fill=SHEET, r=14)
    c.line([(1532, 186), (1550, 204)], FIELD, 3); c.line([(1532, 204), (1550, 186)], FIELD, 3)
    c.text(1570, 195, '磁场 B：垂直屏幕向里', 'sans', 24, INK, 'lm')
    c.ellipse(1541, 245, 10, 10, fill=FIELD)
    c.text(1570, 245, '自由电子（带负电）', 'sans', 24, INK, 'lm')
    c.arrow(1530, 295, 1556, 295, COPPER, 4, 12)
    c.text(1570, 295, '洛伦兹力 F', 'sans', 24, INK, 'lm')
    wy = wire_y(t)
    sp, sg = speed(t), sep(t)
    # wire
    c.rect(L0, wy - TH / 2, L1, wy + TH / 2, fill=mix(BG, COPPER, 0.22), outline=COPPER, width=3, r=TH / 2)
    for u, v in IONS:
        x, y = L0 + 30 + u * (L1 - L0 - 60), wy + v * TH
        c.text(x, y, '+', 'bold', 18, mix(BG, MUTED, 0.6), 'mm')
    # electrons
    for k, (u, v, ph, f) in enumerate(EL):
        jx = math.sin(t * 6 * f + ph) * 7
        jy = math.cos(t * 5 * f + ph * 1.3) * 5
        uu = u + sg * (1 - u) * 0.42
        x = L0 + 34 + uu * (L1 - L0 - 68) + jx
        y = wy + v * TH + jy
        c.ellipse(x, y, 9, 9, fill=FIELD)
        if sp > 0.05 and k % 6 == 0:
            c.arrow(x + 12, y, x + 12 + 46 * sp, y, mix(BG, COPPER, sp), 4, 12)
    # end charges
    if sg > 0.08:
        a = min(1, sg)
        c.text(L1 + 50, wy, '−', 'serif', 64, mix(BG, FIELD, a), 'mm')
        c.text(L0 - 50, wy, '+', 'serif', 64, mix(BG, NRED, a), 'mm')
    # velocity
    if sp > 0.02:
        cx = (L0 + L1) / 2
        c.arrow(cx, wy - TH / 2 - 20, cx, wy - TH / 2 - 20 - 110 * sp, mix(BG, INK, sp), 5, 18)
        c.rect(cx + 14, wy - TH / 2 - 104, cx + 214, wy - TH / 2 - 56, fill=BG, r=8)
        c.text(cx + 22, wy - TH / 2 - 80, '导线向上运动 v', 'sans', 26, mix(BG, INK, sp), 'lm')
    # voltage meter
    c.rect(60, 760, 400, 860, fill=SHEET, r=12)
    c.text(84, 790, '两端电压', 'sans', 24, MUTED, 'lm')
    c.rect(84, 822, 376, 838, fill=LINE, r=8)
    c.rect(84, 822, 84 + 292 * min(sg, 1), 838, fill=SPARK, r=8)
    # captions
    caps = [(0, 4, '导线静止：电子在乱动，但没有整体方向'),
            (4.6, 13, '导线在磁场里运动：每个电子都被推向右端'),
            (13.6, 17.4, '停下来：推力消失，电子退回，电压归零'),
            (17.6, 22, '运动的导线 + 磁场 → 电子被推向一端 → 两端出现电压')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.5) * (1 - fade(t, a1 - 0.4, a1))
        if al > 0:
            c.text(960, 1000, s_, 'bold', 38, mix(BG, INK, al), 'mm')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        c = Canvas(); draw(c, float(sys.argv[1]), 0); c.im.reduce(SS).save('/home/claude/video/prev14.png')
    else:
        render('/home/claude/video/out/镜头14_导线里的电子.mp4', 22, draw)
