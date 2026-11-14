"""第四十八季收尾：B219 抓子儿 + 第四十八季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s48a import SB48, VOL48

BAG = (200, 90, 90)
SKIN = (220, 180, 150)


def b219_air(c, t, i):
    corner_tag(c, 'B219 · 抛得越高，空中时间越长')
    c.text(60, 96, '沙包抛上去、再落回手里，用的时间只看抛多高：抛得高，空中时间长，才来得及先抓起地上的子', 'serif', 36, INK)
    gy = 860
    c.rect(0, gy, W, gy + 12, fill=mix(BG, (150, 120, 80), 0.6))
    sc = 4.0
    for j, h in enumerate([30, 60, 120]):
        x = 420 + j * 520
        T = 2 * math.sqrt(2 * h / 100 / 9.8)
        per = T + 0.8
        tt = (t % per)
        if tt < T:
            v0 = 9.8 * T / 2
            y = v0 * tt - 0.5 * 9.8 * tt * tt
        else:
            y = 0
        hand = gy - 80
        c.line([(x - 120, hand - h * sc), (x + 120, hand - h * sc)], mix(BG, SPARK, 0.6), 2)
        c.text(x + 130, hand - h * sc, f'{h} 厘米', 'sans', 22, SPARK, 'lm')
        c.ellipse(x, hand - y * 100 * sc, 22, 18, fill=mix(BG, BAG, 1.0))
        c.ellipse(x, hand + 30, 50, 22, fill=mix(BG, SKIN, 1.0))
        c.text(x, gy + 50, f'空中约 {T:.2f} 秒', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '同一个沙包，抛到 30、60、120 厘米'),
                (7.2, 14, '抛得越高，在空中停留越久，手就有时间先去抓地上的子'),
                (14.2, 22, '太高也不行：落下来速度快，不好接（时间为计算值，以实测为准）')], y=1010)


def b219_square(c, t, i):
    corner_tag(c, 'B219 · 高度 4 倍，时间才 2 倍')
    c.text(60, 96, '落下的距离和时间的平方成正比：高度变成 4 倍，空中时间只变成 2 倍；想多一倍时间，要抛高到 4 倍', 'serif', 36, INK)
    x0, y0, x1, y1 = 300, 860, 1500, 260
    c.line([(x0, y0), (x1, y0)], INK, 3)
    c.line([(x0, y0), (x0, y1)], INK, 3)
    c.text((x0 + x1) / 2, y0 + 50, '抛起高度（厘米）', 'sans', 24, MUTED, 'mm')
    c.text(x0 - 30, (y0 + y1) / 2, '空中时间', 'sans', 24, MUTED, 'rm')
    k = min(1.0, t / 12)
    pts = []
    for n in range(int(100 * k) + 1):
        h = 160 * n / 100
        T = 2 * math.sqrt(2 * h / 100 / 9.8)
        pts.append((x0 + h / 160 * (x1 - x0), y0 - T / 1.2 * (y0 - y1)))
    if len(pts) > 1:
        seg(c, pts, SPARK, 5)
    for h, col in [(30, MUTED), (120, GREEN)]:
        if h / 160 <= k:
            T = 2 * math.sqrt(2 * h / 100 / 9.8)
            x = x0 + h / 160 * (x1 - x0); y = y0 - T / 1.2 * (y0 - y1)
            c.ellipse(x, y, 12, 12, fill=col)
            c.text(x + 20, y - 30, f'{h} 厘米 → {T:.2f} 秒', 'bold', 26, col, 'lm')
    if t > 14:
        c.text(1620, 500, '高度 × 4', 'bold', 34, INK, 'mm')
        c.text(1620, 560, '时间 × 2', 'bold', 34, GREEN, 'mm')
    caps(c, t, [(0, 7, '抛得越高，时间越长，但不是一样快地变长'),
                (7.2, 14, '从 30 厘米到 120 厘米，高度是 4 倍'),
                (14.2, 22, '空中时间只是 2 倍：这就是自由落体的规律（计算值，以实测为准）')], y=1040)


OLD48 = [('规矩', 'B203'), ('方升', 'B106'), ('计里画方', 'B95'), ('垂线', 'B166'), ('锚', 'B188'), ('窗纸', 'B119'),
         ('屏风', 'B191'), ('锯子', 'B178'), ('陀螺', 'B50'), ('竹简', 'B182'), ('装裱', 'B148'), ('石磨', 'B76'),
         ('水碓', 'B80'), ('剪纸', 'B98'), ('七巧板', 'B60'), ('扁担', 'B100'), ('轿子', 'B206'), ('毽子', 'B88'), ('投壶', 'B89')]
NEW48 = [('新莽铜卡尺', 'B210', ['规矩', '方升']), ('步弓', 'B211', ['计里画方', '规矩']), ('测深锤', 'B212', ['垂线', '锚']),
         ('竹帘', 'B213', ['窗纸', '屏风']), ('舞钻', 'B214', ['锯子', '陀螺']), ('线装书', 'B215', ['竹简', '装裱']),
         ('杵臼', 'B216', ['石磨', '水碓']), ('粽子', 'B217', ['剪纸', '七巧板']), ('背篓', 'B218', ['扁担', '轿子']),
         ('抓子儿', 'B219', ['毽子', '投壶'])]


def s48_graph(c, t, i):
    corner_tag(c, '第四十八季特辑 · 古法解密 21.0')
    c.text(60, 118, '作坊与街巷：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD48):
        pos[name] = (342, 224 + k * 37)
    for k, (name, num, deps) in enumerate(NEW48):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 182, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十八季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW48):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD48:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW48):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 18, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第二十一季：作坊与街巷'),
                (8.2, 16, '规矩和方升长出卡尺，计里画方长出步弓，垂线和锚长出测深锤，窗纸和屏风长出竹帘'),
                (16.2, 24, '锯子和陀螺长出舞钻，竹简和装裱长出线装书，石磨和水碓长出杵臼，剪纸长出粽子'),
                (24.2, 30, '扁担和轿子长出背篓；最后，毽子和投壶一起，长出了抓子儿')], y=1040)



CLIPS = {
 'B219_空中': (b219_air, 22), 'B219_平方': (b219_square, 22),
 'B219_片头': (titles.opening(BSER, VOL48, SB48, 9, '抓子儿是流传很久的民间游戏'), 7),
 'B219_片尾': (titles.closing(BSER, VOL48, SB48, 9, '下集：第四十八季特辑 · 古法解密 21.0 回顾'), 7),
 'S48_依赖': (s48_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
