"""Reusable opening / closing titles: a volume's tech tree with the current episode highlighted."""
import math
from lib import *

def tree(c, eps, lit, blink, t, y=520):
    n = len(eps)
    x0, x1 = 300, 1620
    xs = [x0 + (x1 - x0) * k / (n - 1) for k in range(n)]
    c.line([(xs[0], y), (xs[-1], y)], LINE, 4)
    for k in range(1, n):
        if lit[k] > 0:
            c.line([(xs[k - 1], y), (xs[k], y)], mix(LINE, COPPER, lit[k]), 6)
    for k, (num, name) in enumerate(eps):
        x = xs[k]
        lv = lit[k]                       # 0..1 lit amount
        q = blink[k]                      # 0..1 pulsing ring
        c.ellipse(x, y, 34, 34, fill=mix(SHEET, COPPER, lv), outline=mix(LINE, COPPER, max(lv, q)), width=3)
        if q > 0:
            r = 44 + 12 * q
            c.ellipse(x, y, r, r, outline=mix(BG, SPARK, q), width=4)
        c.text(x, y, num, 'mono', 24, mix(MUTED, BG if lv > 0.5 else INK, lv), 'mm')
        c.text(x, y + 74, name, 'bold', 28, mix(MUTED, INK, max(lv, q)), 'mm')
    return xs

def opening(series, volume, eps, cur, era):
    def draw(c, t, i):
        a = fade(t, 0, 0.8)
        c.text(960, 190, series, 'serif', 40, mix(BG, MUTED, a), 'mm')
        c.text(960, 270, volume, 'serif', 64, mix(BG, INK, a), 'mm')
        lit = [fade(t, 0.6 + k * 0.35, 1.0 + k * 0.35) if k < cur else 0 for k in range(len(eps))]
        pulse = 0.5 + 0.5 * math.sin((t - 2) * 5) if t > 0.6 + cur * 0.35 else 0
        blink = [pulse * fade(t, 0.6 + cur * 0.35, 1.2 + cur * 0.35) if k == cur else 0 for k in range(len(eps))]
        tree(c, eps, lit, blink, t)
        b = fade(t, 2.6, 3.4)
        num, name = eps[cur]
        c.text(960, 790, f'第 {num} 集  {name}', 'serif', 72, mix(BG, COPPER, b), 'mm')
        c.text(960, 880, era, 'sans', 34, mix(BG, MUTED, fade(t, 3.4, 4.2)), 'mm')
    return draw

def closing(series, volume, eps, cur, teaser):
    def draw(c, t, i):
        c.text(960, 190, series, 'serif', 40, MUTED, 'mm')
        c.text(960, 270, volume, 'serif', 64, INK, 'mm')
        lit = [1.0 if k < cur else (fade(t, 0.6, 1.6) if k == cur else 0) for k in range(len(eps))]
        q = fade(t, 2.2, 2.8)
        blink = [(0.5 + 0.5 * math.sin(t * 5)) * q if k == cur + 1 else 0 for k in range(len(eps))]
        xs = tree(c, eps, lit, blink, t)
        if cur + 1 < len(eps):
            nx = xs[cur + 1]
            c.ellipse(nx, 520, 34, 34, fill=mix(SHEET, BG, 0.0), outline=mix(LINE, SPARK, q), width=3)
            c.text(nx, 520, '?', 'serif', 40, mix(MUTED, SPARK, q), 'mm')
        num, name = eps[cur]
        c.text(960, 790, f'已解锁：{name}', 'serif', 56, mix(BG, COPPER, fade(t, 1.0, 1.6)), 'mm')
        c.text(960, 880, teaser, 'bold', 36, mix(BG, INK, fade(t, 2.8, 3.4)), 'mm')
    return draw

VOL1 = [('01', '摩擦起电'), ('02', '伏打电堆'), ('03', '电生磁'), ('04', '磁生电'), ('05', '手摇发电机')]

if __name__ == '__main__':
    import sys
    op = opening('从零造物', '第一卷 · 电', VOL1, 3, '北宋 · 约公元 1090 年 · 一座没有电的工坊')
    cl = closing('从零造物', '第一卷 · 电', VOL1, 3, '下集：为什么接上灯泡，手柄就变沉了？')
    if len(sys.argv) > 2:
        c = Canvas(); (op if sys.argv[1] == 'o' else cl)(c, float(sys.argv[2]), 0); c.im.reduce(SS).save('/home/claude/video/prevtitle.png')
    else:
        render('/home/claude/video/out/片头_第04集.mp4', 7, op)
        render('/home/claude/video/out/片尾_第04集.mp4', 7, cl)
        print('ok')
