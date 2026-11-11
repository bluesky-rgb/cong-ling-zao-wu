"""第四十季（古法解密 17.0）收官：B179 拓片 + 第四十季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s40a import SB40, VOL40, AIR

STONE = (120, 120, 125)
PAPER = (235, 230, 215)
INKC = (30, 30, 35)


# ---------------------------------------------------------------- B179 拓片
def b179_relief(c, t, i):
    corner_tag(c, 'B179 · 凸起的沾墨，凹下的留白')
    c.text(60, 96, '从侧面看：薄纸贴在碑面上，墨包轻轻一拍，只碰得到凸起的地方；刻进去的字是凹的，墨够不着', 'serif', 36, INK)
    x0, x1, sy = 200, 1500, 640
    pts = [(x0, sy)]
    grooves = [(420, 520), (700, 760), (900, 1040), (1200, 1280)]
    for a, b in grooves:
        pts += [(a, sy), (a, sy + 60), (b, sy + 60), (b, sy)]
    pts += [(x1, sy), (x1, sy + 260), (x0, sy + 260)]
    c.poly(pts, mix(BG, STONE, 0.95))
    p = min(1.0, t / 6)
    c.line([(x0, sy - 7)] + [pp for pp in pts[1:-2]], mix(BG, PAPER, p), 14)
    T = 1.2
    ph = (t % T) / T
    bx = x0 + min(x1 - x0, max(0, t - 6) * 100)
    by = sy - 140 + 110 * abs(math.sin(ph * math.pi))
    if t > 6:
        c.ellipse(bx, by, 60, 34, fill=(85, 85, 95))
        c.line([(bx, by - 34), (bx, by - 90)], mix(BG, WOOD, 1.0), 10)
        done = min(x1, bx)
        seg_x = x0
        for a, b in grooves + [(x1, x1)]:
            if seg_x < done:
                c.line([(seg_x, sy - 7), (min(a, done), sy - 7)], (40, 40, 48), 16)
            seg_x = b
    c.rect(1560, 300, 1880, 560, fill=SHEET, r=12)
    c.text(1720, 350, '揭下来的纸', 'bold', 24, INK, 'mm')
    c.rect(1600, 400, 1840, 520, fill=INKC)
    for a, b in grooves:
        xx = 1600 + (a - x0) / (x1 - x0) * 240
        ww = (b - a) / (x1 - x0) * 240
        c.rect(xx, 420, xx + ww, 500, fill=PAPER)
    caps(c, t, [(0, 7, '先把湿的薄纸贴在碑上，用刷子把纸轻轻敲进字的凹槽里'),
                (7.2, 14, '纸干一些后，用墨包一下下轻拍，墨只沾在凸起的碑面上'),
                (14.2, 22, '揭下来：碑面是黑的，刻进去的字是白的，这就是黑底白字的拓片（示意）')], y=1010)


def b179_ink(c, t, i):
    corner_tag(c, 'B179 · 轻轻地，一遍遍上墨')
    c.text(60, 96, '铅笔侧面在硬币上轻轻来回涂：涂一遍只有模糊的影子，涂几遍图案越来越清楚；用力太大，纸会破、凹处也会被涂黑', 'serif', 33, INK)
    for j, (lab, n, hard) in enumerate([('轻涂 1 遍', 1, False), ('轻涂 5 遍', 5, False), ('用力猛涂', 5, True)]):
        cx, cy = 360 + j * 600, 520
        c.rect(cx - 220, cy - 220, cx + 220, cy + 220, fill=mix(BG, PAPER, 1.0), r=8)
        p = min(1.0, t / 12)
        dark = min(1.0, n / 5 * p) * (0.7 if not hard else 0.85)
        c.ellipse(cx, cy, 160, 160, fill=mix(PAPER, (80, 80, 85), dark))
        relief = mix(PAPER, (80, 80, 85), dark * (0.15 if not hard else 0.8))
        c.ellipse(cx, cy, 120, 120, fill=relief)
        c.text(cx, cy, '1', 'bold', 140, mix(PAPER, (80, 80, 85), dark), 'mm')
        if hard and p > 0.6:
            c.line([(cx - 100, cy + 140), (cx - 30, cy + 90), (cx + 20, cy + 150)], NRED, 4)
            c.text(cx, cy + 190, '纸破了', 'bold', 22, NRED, 'mm')
        c.text(cx, cy + 270, lab, 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '一遍涂不出来，就再轻轻涂一遍'),
                (7.2, 14, '凸起的地方越来越黑，凹下的地方一直是白的，图案就出来了'),
                (14.2, 22, '用力太猛，铅笔会压进凹处，图案反而糊了，纸也会破（以实测为准）')], y=1040)


# ---------------------------------------------------------------- 第四十季特辑
OLD40 = [('唧筒', 'B27'), ('漏刻', 'B13'), ('筷子', 'B53'), ('夯土版筑', 'B46'), ('船尾舵', 'B44'), ('指南车', 'B17'),
         ('独轮车', 'B93'), ('不倒翁', 'B51'), ('腰舟', 'B139'), ('曹冲称象', 'B74'), ('辘轳', 'B81'), ('绳结', 'B151'),
         ('筛子', 'B114'), ('风箱', 'B160'), ('墨斗', 'B61'), ('楔子', 'B150'), ('印章', 'B129'), ('毛笔', 'B78')]
NEW40 = [('茶壶', 'B170', ['唧筒', '漏刻']), ('筷子提米', 'B171', ['筷子', '夯土版筑']), ('刻舟求剑', 'B172', ['船尾舵', '指南车']),
         ('马镫', 'B173', ['独轮车', '不倒翁']), ('竹筏', 'B174', ['腰舟', '曹冲称象']), ('拉纤', 'B175', ['辘轳', '船尾舵']),
         ('渔网', 'B176', ['绳结', '筛子']), ('鱼篓', 'B177', ['风箱', '筛子']), ('锯子', 'B178', ['墨斗', '楔子']),
         ('拓片', 'B179', ['印章', '毛笔'])]


def s40_graph(c, t, i):
    corner_tag(c, '第四十季特辑 · 古法解密 17.0')
    c.text(60, 118, '水上与手边：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD40):
        pos[name] = (340, 218 + k * 38)
    for k, (name, num, deps) in enumerate(NEW40):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW40):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD40:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW40):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十七季：水上与手边'),
                (8.2, 16, '唧筒和漏刻长出茶壶，筷子长出筷子提米，船尾舵长出刻舟求剑和拉纤，不倒翁长出马镫'),
                (16.2, 24, '腰舟长出竹筏，绳结长出渔网，风箱长出鱼篓，楔子长出锯子'),
                (24.2, 30, '最后，印章和毛笔一起，长出了把石碑搬到纸上的拓片')], y=1040)


CLIPS = {
 'B179_凹凸': (b179_relief, 22), 'B179_拍墨': (b179_ink, 22),
 'B179_片头': (titles.opening(BSER, VOL40, SB40, 9, '唐代已有碑刻拓片传世'), 7),
 'B179_片尾': (titles.closing(BSER, VOL40, SB40, 9, '下集：第四十季特辑 · 古法解密 17.0 回顾'), 7),
 'S40_依赖': (s40_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
