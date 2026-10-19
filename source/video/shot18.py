import math
from lib import *

DUR = 30
RCX, RCY, RR, RW = 960, 540, 230, 46   # ring centre, mid radius, half width

# switch events: closed between ON and OFF
ON, OFF = 9.0, 17.0
def closed(t): return ON <= t < OFF

def needle(t):
    """induced current in coil B: kick at switch on (+), kick at off (-)"""
    def kick(t0):
        if t < t0: return 0.0
        u = t - t0
        return math.exp(-u / 0.35) * min(1, u / 0.06)
    return kick(ON) - kick(OFF)

def flux(t):
    if t < ON: return 0.0
    if t < OFF: return min(1.0, (t - ON) / 0.25)
    return max(0.0, 1 - (t - OFF) / 0.25)

def coil(c, cx, cy, n, col):
    for j in range(n):
        y = cy - (n - 1) * 11 + j * 22
        c.ellipse(cx, y, RW + 22, 9, outline=col, width=5)

def draw(c, t, i):
    corner_tag(c, '镜头 18 · 历史')
    c.text(60, 96, '1831 年 8 月 29 日，法拉第的铁环', 'serif', 40, mix(BG, INK, fade(t, 0, 1)))
    f = flux(t)
    # ring
    c.ellipse(RCX, RCY, RR + RW, RR + RW, fill=mix(BG, MUTED, 0.35))
    c.ellipse(RCX, RCY, RR - RW, RR - RW, fill=BG)
    if f > 0:
        c.ellipse(RCX, RCY, RR, RR, outline=mix(BG, FIELD, f), width=8)
        for k in range(8):
            a = k / 8 * 2 * math.pi + t * 1.5
            x, y = RCX + RR * math.cos(a), RCY + RR * math.sin(a)
            tx, ty = -math.sin(a), math.cos(a)
            c.arrow(x - tx * 12, y - ty * 12, x + tx * 14, y + ty * 14, mix(BG, FIELD, f), 4, 12)
    # coil A (left) and B (right): drawn vertically on ring sides
    for side, lab in ((-1, '线圈 A'), (1, '线圈 B')):
        cx = RCX + side * RR
        for j in range(7):
            y = RCY - 66 + j * 22
            c.ellipse(cx, y, RW + 20, 9, outline=COPPER, width=5)
        c.text(cx, RCY - 120, lab, 'bold', 28, COPPER, 'mm')
    # circuit A: battery + switch on far left
    ax = RCX - RR - 66
    c.line([(ax, RCY - 66), (380, RCY - 66), (380, 420)], LINE, 3)
    c.line([(ax, RCY + 66), (380, RCY + 66), (380, 660)], LINE, 3)
    # battery
    c.rect(330, 660, 430, 780, fill=SHEET, outline=MUTED, width=2, r=8)
    c.text(380, 720, '电堆', 'sans', 26, INK, 'mm')
    c.line([(380, 420), (380, 380)], LINE, 3)
    # switch
    sw = 1.0 if closed(t) else 0.0
    c.ellipse(380, 380, 7, 7, fill=INK)
    ang = -math.pi / 2 - (1 - sw) * 0.6
    c.line([(380, 380), (380 + 70 * math.cos(ang), 380 + 70 * math.sin(ang))], INK, 5)
    c.ellipse(380, 310, 7, 7, fill=INK)
    c.line([(380, 310), (380, 270), (330, 270), (330, 660)], LINE, 3)
    c.text(300, 345, '开关', 'sans', 24, MUTED, 'rm')
    c.text(380, 830, '接通' if closed(t) else '断开', 'bold', 30, SPARK if closed(t) else MUTED, 'mm')
    # circuit B: galvanometer on right
    bx = RCX + RR + 66
    c.line([(bx, RCY - 66), (1760, RCY - 66), (1760, 600), (1680, 600)], LINE, 3)
    c.line([(bx, RCY + 66), (1500, RCY + 66), (1500, 600)], LINE, 3)
    gx, gy = 1590, 600
    c.arc(gx, gy, 90, 90, 180, 360, INK, 3)
    for k in range(-3, 4):
        a = -math.pi / 2 + k * 0.4
        c.line([(gx + 80 * math.cos(a), gy + 80 * math.sin(a)), (gx + 90 * math.cos(a), gy + 90 * math.sin(a))], MUTED, 2)
    na = -math.pi / 2 + needle(t) * 1.15
    c.line([(gx, gy), (gx + 82 * math.cos(na), gy + 82 * math.sin(na))], SPARK, 6)
    c.ellipse(gx, gy, 8, 8, fill=INK)
    c.text(gx, gy + 40, '检流计', 'sans', 24, MUTED, 'mm')
    # captions
    caps = [(0, 8.6, '铁环两侧各绕一组线圈：A 接电堆，B 接检流计'),
            (9.0, 13.4, '接通的瞬间，指针跳一下，马上回到零'),
            (13.6, 16.8, '电流一直通着，铁环里一直有磁场，指针却不动'),
            (17.0, 22.6, '断开的瞬间，指针往反方向跳'),
            (23.0, 30, '磁场不变时不生电，磁场变化的瞬间才生电')]
    for a0, a1, s_ in caps:
        al = fade(t, a0, a0 + 0.4) * (1 - fade(t, a1 - 0.3, a1))
        if al > 0:
            c.text(960, 1000, s_, 'bold', 38, mix(BG, INK, al), 'mm')
    if f > 0.05:
        c.text(RCX, RCY, '铁环里的磁场', 'sans', 26, mix(BG, FIELD, f), 'mm')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        c = Canvas(); draw(c, float(sys.argv[1]), 0); c.im.reduce(SS).save('/home/claude/video/prev18.png')
    else:
        render('/home/claude/video/out/镜头18_法拉第铁环.mp4', DUR, draw)
