"""第十八季收尾：B69 冰糖、第十八季特辑（古法解密 6.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s18a import SB18, VOL18, WOOD

SUGAR = (235, 235, 245)
SYRUP = (240, 210, 140)

# ---------------------------------------------------------------- B69 冰糖
SOL = [(0, 179), (20, 204), (40, 238), (60, 287), (80, 362), (100, 487)]  # 克 / 100 克水（资料值，拍摄前核对）

def sol(T):
    for (t0, s0), (t1, s1) in zip(SOL, SOL[1:]):
        if T <= t1:
            return s0 + (s1 - s0) * (T - t0) / (t1 - t0)
    return SOL[-1][1]

def b69_super(c, t, i):
    corner_tag(c, 'B69 · 过饱和')
    c.text(60, 96, '热水能溶更多糖；慢慢凉下来，多出来的糖就要「站出来」', 'serif', 40, INK)
    ox, oy, W, H = 220, 880, 1000, 640
    def P(T, s): return (ox + W * T / 100, oy - H * (s - 150) / 350)
    c.line([(ox, oy), (ox + W, oy)], LINE, 3)
    c.line([(ox, oy), (ox, oy - H)], LINE, 3)
    for T in (0, 20, 40, 60, 80, 100):
        c.text(P(T, 150)[0], oy + 30, f'{T}°', 'mono', 22, MUTED, 'mm')
    for s in (200, 300, 400, 500):
        c.text(ox - 16, P(0, s)[1], str(s), 'mono', 20, MUTED, 'rm')
    c.text(ox + W / 2, oy + 72, '水温（摄氏度）', 'sans', 22, MUTED, 'mm')
    c.text(ox, oy - H - 30, '100 克水最多溶多少克糖', 'sans', 22, MUTED, 'lm')
    curve = [P(T, sol(T)) for T in range(0, 101, 2)]
    c.poly(curve + [P(100, 500), P(0, 500)], mix(BG, NRED, 0.12))
    c.line(curve, SPARK, 5)
    c.text(P(12, 470)[0], P(12, 470)[1], '过饱和区', 'bold', 26, mix(BG, NRED, 0.8), 'mm')
    c.text(P(70, 250)[0], P(70, 250)[1], '还能再溶', 'sans', 24, MUTED, 'mm')
    s0 = 400
    T0 = 92
    u = fade(t, 4, 14)
    T = T0 - (T0 - 20) * u
    if t > 15:
        s = s0 - (s0 - sol(20)) * fade(t, 15, 19)
    else:
        s = s0
    c.line([P(T0, s0), P(T, s0)], mix(BG, INK, 0.5), 2)
    x, y = P(T, s)
    c.ellipse(x, y, 14, 14, fill=GREEN)
    a = fade(t, 15, 16)
    if a > 0:
        x1, y1 = P(20, s0); x2, y2 = P(20, sol(20))
        c.arrow(x1 + 30, y1, x2 + 30, y2, mix(BG, GREEN, a), 4, 16)
        c.text(x1 + 50, (y1 + y2) / 2, f'约 {s0 - sol(20):.0f} 克糖结晶出来', 'bold', 24, mix(BG, GREEN, a), 'lm')
    c.rect(1320, 300, 1840, 560, fill=SHEET, r=14)
    c.text(1580, 350, '这杯糖水', 'sans', 24, MUTED, 'mm')
    c.text(1580, 420, f'{T:.0f}°', 'mono', 48, INK, 'mm')
    c.text(1580, 500, f'溶着 {s:.0f} 克 / 100 克水', 'sans', 24, INK, 'mm')
    c.text(1580, 620, '（溶解度为资料值，拍摄前核对）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 4, '这条线是糖的溶解度：水越热，能溶的糖越多'),
                (4.2, 14, '在九十多度溶进 400 克糖，再慢慢凉下来：糖还在水里，可已经超过了它能溶的量，这叫过饱和'),
                (14.2, 22, '多出来的糖分子找到落脚的地方，一层层排上去：这就是结晶')], y=1010)

def _crystals(n, seed):
    rnd = random.Random(seed)
    return [(rnd.uniform(-125, 125), rnd.uniform(30, 430), rnd.uniform(0, 1)) for _ in range(n)]
CR_SLOW = [(0, 60 + k * 105, 0.5 + 0.15 * k) for k in range(4)]
CR_FAST = _crystals(36, 7)

def _cup(c, cx, label, crs, g, a=1.0):
    top, bot = 300, 760
    c.rect(cx - 150, top, cx + 150, bot, fill=mix(BG, SYRUP, 0.35 * a))
    c.line([(cx - 150, top - 20), (cx - 150, bot), (cx + 150, bot), (cx + 150, top - 20)], mix(BG, INK, a * 0.8), 4)
    c.line([(cx - 190, top - 40), (cx + 190, top - 40)], mix(BG, WOOD, a), 10)
    c.line([(cx, top - 40), (cx, bot - 40)], mix(BG, INK, a * 0.7), 2)
    size = 90 / (len(crs) ** (1 / 3))
    for dx, dy, ph in crs:
        s = size * g * (0.7 + 0.3 * ph)
        if s < 1: continue
        x = cx + dx
        y = top + dy
        c.poly([(x, y - s), (x + s * 0.8, y), (x, y + s), (x - s * 0.8, y)], mix(BG, SUGAR, a))
    c.text(cx, bot + 50, label, 'bold', 28, mix(BG, INK, a), 'mm')

def b69_growth(c, t, i):
    corner_tag(c, 'B69 · 慢慢凉，长大块')
    c.text(60, 96, '同样多的糖：落脚的地方越少，每块就长得越大', 'serif', 40, INK)
    g = fade(t, 3, 15)
    _cup(c, 500, '泡沫箱里慢慢凉', CR_SLOW, g)
    _cup(c, 1100, '冰箱里很快凉', CR_FAST, g)
    a = fade(t, 15, 16)
    if a > 0:
        c.rect(1380, 340, 1860, 700, fill=mix(BG, SHEET, a), r=14)
        c.text(1620, 390, '为什么', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(1620, 460, '凉得快：一下冒出很多晶核', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1620, 510, '糖被分成许多小块', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1620, 580, '凉得慢：晶核少，糖慢慢排', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1620, 630, '长成透明的大块（以实测为准）', 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '两杯一样浓的热糖水，各吊一根棉线'),
                (6.2, 14, '冰箱里那杯凉得快，一下子到处冒出小晶核，糖被分成一大堆小颗粒'),
                (14.2, 22, '泡沫箱里那杯凉得慢，晶核只有几个，糖分子一层层整齐地排上去：长成透明的大冰糖')], y=1010)

# ---------------------------------------------------------------- 第十八季特辑
OLD18 = [('数字与 0', '48'), ('算盘', 'B54'), ('榫卯', 'B7'), ('夯土版筑', 'B46'), ('影子测地球', '47'), ('漏刻', 'B13'),
         ('走马灯', 'B23'), ('一钟双音', 'B11'), ('陶埙', 'B42'), ('回声与雷达', '84'), ('斗拱', 'B47'), ('摆钟', '45'),
         ('酿酒与酿醋', 'B15'), ('豆腐点卤', 'B14'), ('制盐', '20')]
NEW18 = [('七巧板', 'B60', ['数字与 0', '算盘']), ('墨斗', 'B61', ['榫卯', '夯土版筑']), ('勾股', 'B62', ['影子测地球', '墨斗']),
         ('日晷', 'B63', ['影子测地球', '漏刻']), ('皮影戏', 'B64', ['走马灯', '影子测地球']), ('古琴', 'B65', ['一钟双音', '陶埙']),
         ('回音壁', 'B66', ['回声与雷达', '一钟双音']), ('屋檐举折', 'B67', ['斗拱', '摆钟']), ('饴糖', 'B68', ['酿酒与酿醋', '豆腐点卤']),
         ('冰糖', 'B69', ['制盐', '饴糖'])]

def s18_graph(c, t, i):
    corner_tag(c, '第十八季特辑 · 古法解密 6.0')
    c.text(60, 118, '量、影、声、糖：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD18):
        pos[name] = (340, 215 + k * 50)
    for k, (name, num, deps) in enumerate(NEW18):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 172, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第十八季新长出', 'sans', 24, MUTED, 'mm')
    newset = set(n for n, _, _ in NEW18)
    for k, (name, num, deps) in enumerate(NEW18):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in newset:
                pts = [(x0 + 110 if x0 < x1 else x0 - 110, y0), (x1 - 110 if x0 < x1 else x1 + 110, y1)]
                c.line(pts, mix(BG, COPPER, a * 0.9), 3)
                continue
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD18:
        x, y = pos[name]
        c.rect(x - 110, y - 20, x + 110, y + 20, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW18):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第六季：量、影、声、糖'),
                (8.2, 16, '七巧板、墨斗、勾股、日晷：不用量角器，也能画准、算准、看准时辰'),
                (16.2, 24, '皮影、古琴、回音壁讲光和声；屋檐、饴糖、冰糖讲水和糖'),
                (24.2, 30, '每一样老手艺背后，都是一条今天还写在课本里的道理')], y=1040)

CLIPS = {
 'B69_过饱和': (b69_super, 22), 'B69_结晶': (b69_growth, 22),
 'B69_片头': (titles.opening(BSER, VOL18, SB18, 9, '元代「糖霜」与冰糖'), 7),
 'B69_片尾': (titles.closing(BSER, VOL18, SB18, 9, '下集：第十八季特辑 · 古法解密 6.0 回顾'), 7),
 'S18_依赖': (s18_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
