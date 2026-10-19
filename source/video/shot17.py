import math
from lib import *

DUR = 17
OMEGA = 2 * math.pi * 0.5   # rad/s at speed 1 (0.5 rev/s)
DT = 1 / FPS / 4

def spd(t):
    if t < 3: return ease(t / 3)
    if t < 11: return 1.0
    if t < 13: return 1 + 0.6 * ease((t - 11) / 2)
    return 1.6

# integrate angle and emf
ANG, EMF = [], []
th = math.pi / 2
n = int((DUR + 1) / DT)
for k in range(n):
    t = k * DT
    w = spd(t) * OMEGA
    th += w * DT
    ANG.append(th)
    EMF.append(w / OMEGA * math.sin(th))   # emf ∝ ω·sinθ ; θ measured from coil axis
def at(arr, t): return arr[min(int(t / DT), len(arr) - 1)]

RX, RY = 420, 600       # rotor centre
CY = 300                # coil centre
GX0, GX1, GM, GA = 820, 1820, 560, 130
WIN = 5.0

def draw(c, t, i):
    corner_tag(c, '镜头 17 · 交流电')
    c.text(60, 96, '磁铁转起来，电流就来回换方向', 'serif', 40, mix(BG, INK, fade(t, 0, 1)))
    # coil with iron core
    c.rect(RX - 26, CY - 90, RX + 26, CY + 120, fill=mix(BG, MUTED, 0.35), r=4)
    for j in range(9):
        y = CY - 70 + j * 21
        c.ellipse(RX, y, 70, 12, outline=COPPER, width=5)
    c.text(RX + 100, CY - 40, '线圈（带铁芯）', 'sans', 26, MUTED, 'lm')
    # wires to meter
    c.line([(RX + 70, CY - 70), (700, CY - 70), (700, 900), (380, 900)], LINE, 3)
    c.line([(RX - 70, CY + 100), (180, CY + 100), (180, 900), (260, 900)], LINE, 3)
    # rotor
    a = at(ANG, t)
    c.ellipse(RX, RY, 170, 170, outline=LINE, width=2)
    ux, uy = math.cos(a), -math.sin(a)
    def bar(s0, s1, col):
        px, py = -uy, ux
        p = [(RX + ux * s0 + px * 30, RY + uy * s0 + py * 30), (RX + ux * s1 + px * 30, RY + uy * s1 + py * 30),
             (RX + ux * s1 - px * 30, RY + uy * s1 - py * 30), (RX + ux * s0 - px * 30, RY + uy * s0 - py * 30)]
        c.poly(p, col)
    bar(0, 150, NRED); bar(-150, 0, SBLUE)
    c.text(RX + ux * 100, RY + uy * 100, 'N', 'bold', 30, (255, 255, 255), 'mm')
    c.text(RX - ux * 100, RY - uy * 100, 'S', 'bold', 30, (255, 255, 255), 'mm')
    c.ellipse(RX, RY, 12, 12, fill=INK)
    # rotation arrow
    c.arc(RX, RY, 200, 200, 200, 250, MUTED, 4)
    c.text(RX, RY + 205, '手摇转动', 'sans', 24, MUTED, 'mm')
    # meter
    e = at(EMF, t)
    c.arc(320, 900, 60, 60, 180, 360, INK, 3)
    na = -math.pi / 2 + max(-1, min(1, e / 1.6)) * 1.2
    c.line([(320, 900), (320 + 54 * math.cos(na), 900 + 54 * math.sin(na))], SPARK, 5)
    c.text(320, 940, '电流表', 'sans', 22, MUTED, 'mm')
    # waveform panel
    c.line([(GX0, GM), (GX1, GM)], LINE, 2)
    c.line([(GX0, GM - 250), (GX0, GM + 250)], LINE, 2)
    c.text(GX0 + 12, GM - 250, '电压', 'sans', 24, MUTED, 'lm')
    c.text(GX1, GM + 280, '时间', 'sans', 24, MUTED, 'rm')
    c.text(GX0 - 16, GM - 120, '正', 'bold', 26, COPPER, 'rm')
    c.text(GX0 - 16, GM + 120, '负', 'bold', 26, FIELD, 'rm')
    t0 = max(0.0, t - WIN)
    steps = 240
    prev = None
    for k in range(steps + 1):
        tt = t0 + (t - t0) * k / steps
        if t - t0 < 1e-6: break
        x = GX1 - (t - tt) / WIN * (GX1 - GX0)
        y = GM - at(EMF, tt) * GA
        if prev:
            col = COPPER if (y + prev[1]) / 2 <= GM else FIELD
            c.line([prev, (x, y)], col, 5)
        prev = (x, y)
    if prev: c.ellipse(prev[0], prev[1], 9, 9, fill=COPPER if prev[1] <= GM else FIELD)
    # speed tag
    c.rect(GX1 - 250, GM - 250, GX1, GM - 196, fill=SHEET, r=10)
    c.text(GX1 - 230, GM - 223, f'转速  ×{spd(t):.1f}', 'mono', 26, INK, 'lm')
    caps = [(0, 5, '磁铁转动时，穿过线圈的磁感线一会儿多、一会儿少'),
            (5.4, 10.6, '电压一会儿正、一会儿负：这就是交流电'),
            (11, 17, '转得越快：变化更快，电压也更高')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.5) * (1 - fade(t, a1 - 0.4, a1))
        if al > 0:
            c.text(1320, 1000, s_, 'bold', 36, mix(BG, INK, al), 'mm')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        c = Canvas(); draw(c, float(sys.argv[1]), 0); c.im.reduce(SS).save('/home/claude/video/prev17.png')
    else:
        render('/home/claude/video/out/镜头17_交流电波形.mp4', DUR, draw)
