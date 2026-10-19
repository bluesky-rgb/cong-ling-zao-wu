import math
from lib import *

AXIS, CX, R = 430, 960, 150
KS = [round(95 * 1.42 ** i) for i in range(11)]
KFINE = [95 * 1.42 ** (i / 20) for i in range(201)]
SCENE_TOP, SCENE_BOT = 175, 720
THS = [i / 600 * math.pi for i in range(1, 600)]

def crossings(k, d):
    d = abs(d)
    ys, prev = [], None
    for th in THS:
        f = k * math.sin(th) ** 2 * abs(math.cos(th)) - d
        if th > math.pi / 2:
            break
        if prev is not None and (prev[0] < 0) != (f < 0):
            ys.append(k * math.sin(th) ** 3)
        prev = (f, th)
    if d < 1e-6:
        return [0.0, float(k)]
    return ys

def threads(k, d):
    ys = crossings(k, d)
    if len(ys) == 0:
        return False
    if len(ys) == 1:
        return ys[0] < R
    return ys[0] < R < ys[1]

def mag_x(t):
    if t < 2: return 260
    if t < 7: return 260 + (CX - 260) * ease((t - 2) / 5)
    if t < 9: return CX
    if t < 14: return CX + (1660 - CX) * ease((t - 9) / 5)
    return 1660

def count(mx):
    return 2 * sum(threads(k, CX - mx) for k in KS)

T0, T1 = 1.0, 15.0
SAMPLES = [(T0 + (T1 - T0) * i / 280) for i in range(281)]
CURVE = [(t, sum(threads(k, CX - mag_x(t)) for k in KFINE)) for t in SAMPLES]
CMAX = max(v for _, v in CURVE)

def field_line(c, mx, k, sign, col, w):
    seg = []
    for th in THS:
        r = k * math.sin(th) ** 2
        x, y = mx + r * math.cos(th), AXIS - sign * r * math.sin(th)
        if SCENE_TOP < y < SCENE_BOT:
            seg.append((x, y))
        else:
            if len(seg) > 1: c.line(seg, col, w)
            seg = []
    if len(seg) > 1: c.line(seg, col, w)

def draw(c, t, i):
    a = fade(t, 0, 1)
    corner_tag(c, '镜头 10 · 磁通量')
    c.text(60, 96, '把穿过线圈的磁感线，当成「根数」来数', 'serif', 40, mix(BG, INK, a))
    mx = mag_x(t)
    d = CX - mx
    # coil back half
    c.arc(CX, AXIS, 34, R, 90, 270, COPPER, 9)
    for k in KS:
        th_ok = threads(k, d)
        col = COPPER if th_ok else mix(BG, FIELD, 0.55)
        for sgn in (1, -1):
            field_line(c, mx, k, sgn, col, 4.5 if th_ok else 3)
    # magnet
    c.rect(mx - 120, AXIS - 30, mx, AXIS + 30, fill=SBLUE, r=4)
    c.rect(mx, AXIS - 30, mx + 120, AXIS + 30, fill=NRED, r=4)
    c.text(mx - 60, AXIS, 'S', 'bold', 30, (255, 255, 255), 'mm')
    c.text(mx + 60, AXIS, 'N', 'bold', 30, (255, 255, 255), 'mm')
    # coil front half
    c.arc(CX, AXIS, 34, R, 270, 450, COPPER, 9)
    c.rect(CX + 40, AXIS - R - 58, CX + 132, AXIS - R - 14, fill=BG, r=8)
    c.text(CX + 86, AXIS - R - 36, '线圈', 'sans', 28, COPPER, 'mm')
    # counter
    n = count(mx)
    c.rect(1420, 150, 1860, 290, fill=SHEET, r=14)
    c.text(1450, 172, '穿过线圈的磁感线', 'sans', 26, MUTED)
    c.text(1450, 214, f'{n}', 'serif', 64, COPPER)
    c.text(1450 + c.textw(f'{n}', 'serif', 64) + 14, 250, '根', 'sans', 30, INK)
    # callout at center
    ca = fade(t, 7.2, 7.8) * (1 - fade(t, 8.8, 9.2))
    if ca > 0:
        c.rect(CX - 300, SCENE_BOT - 38, CX + 300, SCENE_BOT + 18, fill=BG, r=10)
        c.text(CX, SCENE_BOT - 10, '磁铁在线圈正中：穿过的根数最多', 'bold', 32, mix(BG, SPARK, ca), 'mm')
    # graph
    gx0, gx1, gy0, gy1 = 160, 1760, 790, 1010
    c.line([(gx0, gy1), (gx1, gy1)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    c.text(gx0 - 20, gy0, '磁通量', 'sans', 24, MUTED, 'rm')
    c.text(gx1, gy1 + 30, '时间', 'sans', 24, MUTED, 'rm')
    pts = [(gx0 + (tt - T0) / (T1 - T0) * (gx1 - gx0), gy1 - v / CMAX * (gy1 - gy0 - 10)) for tt, v in CURVE if tt <= t]
    if len(pts) > 1:
        c.line(pts, COPPER, 5)
        c.ellipse(pts[-1][0], pts[-1][1], 9, 9, fill=COPPER)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        c = Canvas(); draw(c, float(sys.argv[1]), 0); c.im.reduce(SS).save('/home/claude/video/prev10.png')
    else:
        render('/home/claude/video/out/镜头10_磁感线计数.mp4', 18, draw)
