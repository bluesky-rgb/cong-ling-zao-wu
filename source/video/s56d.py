"""第五十六季（古法解密 25.0：园林与庭院）收尾：B259 太平缸 + 第五十六季特辑依赖图。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s56a import SB56, VOL56, WALL, WATER, STONE, LEAF, WOODC

BRONZE = (170, 120, 70)


def temp_big(m):
    return 20 + 30 * math.exp(-m / 70)


def temp_small(m):
    return 20 + 30 * math.exp(-m / 18)


def temp_cover(m):
    return 20 + 30 * math.exp(-m / 130)


def plot(c, t, curves, tmax):
    x0, y0, x1, y1 = 760, 260, 1760, 820
    c.line([(x0, y1), (x1, y1)], MUTED, 3)
    c.line([(x0, y0), (x0, y1)], MUTED, 3)
    c.text(x0 - 20, y0, '50 ℃', 'mono', 22, MUTED, 'rm')
    c.text(x0 - 20, y1, '20 ℃', 'mono', 22, MUTED, 'rm')
    c.text(x1, y1 + 40, '60 分钟', 'mono', 22, MUTED, 'rm')
    c.text(x0, y1 + 40, '0', 'mono', 22, MUTED, 'lm')
    m_now = min(60, t / tmax * 60)
    for f, col, lab in curves:
        pts = []
        for j in range(int(m_now) + 1):
            T = f(j)
            pts.append((x0 + (x1 - x0) * j / 60, y1 - (y1 - y0) * (T - 20) / 30))
        if len(pts) > 1:
            seg(c, pts, col, 5)
            c.text(pts[-1][0] + 14, pts[-1][1], lab, 'bold', 24, col, 'lm')


def b259_store(c, t, i):
    corner_tag(c, 'B259 · 水多，存的热就多')
    c.text(60, 96, '一大瓶水和一小瓶水一样热，一起放进冰箱：小瓶很快凉透，大瓶水多、存的热多，要放很久才凉下来', 'serif', 36, INK)
    c.rect(200, 400, 420, 860, fill=mix(BG, WATER, 0.6), outline=MUTED, width=3, r=20)
    c.rect(480, 700, 560, 860, fill=mix(BG, WATER, 0.6), outline=MUTED, width=3, r=10)
    c.text(310, 900, '1.5 升', 'bold', 26, INK, 'mm')
    c.text(520, 900, '250 毫升', 'bold', 26, INK, 'mm')
    plot(c, t, [(temp_big, mix(BG, FIELD, 1.0), '大瓶'), (temp_small, mix(BG, NRED, 1.0), '小瓶')], 20)
    c.text(1260, 220, '曲线是示意，以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '两瓶一样热的温水（不超过 50 ℃）同时放进冰箱冷藏室'),
                (7.2, 14, '小瓶的温度一下子就掉下来，大瓶慢慢地降'),
                (14.2, 22, '水越多存的热越多：一大缸水要放出很多热才会结冰')], y=1010)


def b259_cover(c, t, i):
    corner_tag(c, 'B259 · 厚缸加盖，散热更慢')
    c.text(60, 96, '热从水面和缸壁往外跑：缸壁厚、外面裹一层、上面加盖，热跑得更慢；故宫的大铜缸冬天还会加棉套（待核）', 'serif', 36, INK)
    cx = 400
    c.rect(cx - 170, 420, cx + 170, 840, fill=mix(BG, BRONZE, 1.0), r=30)
    c.rect(cx - 140, 450, cx + 140, 820, fill=mix(BG, WATER, 0.6), r=20)
    if t > 7.2:
        c.rect(cx - 190, 400, cx + 190, 860, outline=mix(BG, SPARK, 1.0), width=14, r=36)
        c.rect(cx - 190, 380, cx + 190, 420, fill=mix(BG, SPARK, 0.8), r=10)
        c.text(cx, 340, '裹毛巾、加盖', 'bold', 28, SPARK, 'mm')
    for k in range(5):
        ph = (t * 0.4 + k / 5) % 1
        sp = 1 if t <= 7.2 else 0.35
        y = 440 - ph * 160 * sp
        c.arrow(cx - 120 + k * 60, 440, cx - 120 + k * 60, y, mix(BG, NRED, 1 - ph), 4, 12)
    curves = [(temp_big, mix(BG, FIELD, 1.0), '大瓶')]
    if t > 7.2:
        curves.append((temp_cover, mix(BG, SPARK, 1.0), '大瓶 + 毛巾 + 盖'))
    plot(c, t, curves, 20)
    caps(c, t, [(0, 7, '热从水面和缸壁往外跑（红箭头）'),
                (7.2, 14, '给大瓶裹上毛巾、盖好盖子再试一次'),
                (14.2, 22, '降温更慢了：厚缸、加盖，救火的水冬天也不容易冻透（本集不用火）')], y=1010)


OLD56 = [('窗纸', 'B119'), ('风塔', 'B142'), ('竹笕', 'B197'), ('都江堰', 'B5'), ('欹器', 'B21'), ('不倒翁', 'B51'),
         ('瓦片', 'B137'), ('草拌泥', 'B145'), ('竹编', 'B73'), ('竹梯', 'B192'), ('屏风', 'B191'), ('冰鉴与藏冰', 'B12'),
         ('地窖', 'B146'), ('透光镜', 'B10'), ('打水漂', 'B155'), ('门轴', 'B190'), ('窑洞', 'B83'), ('木桶', 'B110')]
NEW56 = [('漏窗', 'B250', ['窗纸', '风塔']), ('曲水流觞', 'B251', ['竹笕', '都江堰']), ('叠石假山', 'B252', ['欹器', '不倒翁']),
         ('花街铺地', 'B253', ['瓦片', '草拌泥']), ('竹篱笆', 'B254', ['竹编', '竹梯']), ('照壁', 'B255', ['屏风', '风塔']),
         ('石凳', 'B256', ['冰鉴与藏冰', '地窖']), ('倒影池', 'B257', ['透光镜', '打水漂']), ('门槛', 'B258', ['门轴', '窑洞']),
         ('太平缸', 'B259', ['木桶', '冰鉴与藏冰'])]


def s56_graph(c, t, i):
    corner_tag(c, '第五十六季特辑 · 古法解密 25.0')
    c.text(60, 118, '园林与庭院：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD56):
        pos[name] = (342, 224 + k * 37)
    for k, (name, num, deps) in enumerate(NEW56):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 182, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十六季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW56):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD56:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW56):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 18, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第二十五季：园林与庭院'),
                (8.2, 16, '窗纸和风塔长出漏窗，竹笕和都江堰长出曲水流觞，欹器和不倒翁长出叠石假山，瓦片长出花街铺地'),
                (16.2, 24, '竹编长出竹篱笆，屏风长出照壁，冰鉴和地窖长出石凳，透光镜长出倒影池，门轴和窑洞长出门槛'),
                (24.2, 30, '最后，木桶和冰鉴与藏冰一起，长出了太平缸')], y=1040)


CLIPS = {
 'B259_存热': (b259_store, 22), 'B259_加盖': (b259_cover, 22),
 'B259_片头': (titles.opening(BSER, VOL56, SB56, 9, '故宫院里储水防火的大缸'), 7),
 'B259_片尾': (titles.closing(BSER, VOL56, SB56, 9, '下集：第五十六季特辑 · 古法解密 25.0 回顾'), 7),
 'S56_依赖': (s56_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
