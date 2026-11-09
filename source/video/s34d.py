"""第三十四季（古法解密 14.0：水、风、土、纸）收官：B149 灯芯 + 第三十四季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, FIBER
from s34a import SB34, VOL34

DYE = (90, 150, 230)
COTTON = (235, 230, 215)


# ---------------------------------------------------------------- B149 灯芯
def b149_capillary(c, t, i):
    corner_tag(c, 'B149 · 细缝把液体往上拉')
    c.text(60, 96, '灯芯里有无数纤维间的细缝：液体贴着缝壁往上爬，缝越细，爬得越高', 'serif', 36, INK)
    c.rect(100, 230, 900, 920, fill=SHEET, r=14)
    c.text(500, 265, '油灯（本集不点火，只用水）', 'sans', 22, MUTED, 'mm')
    c.poly([(240, 700), (760, 700), (680, 860), (320, 860)], mix(BG, (170, 120, 80), 0.9))
    c.rect(300, 740, 700, 760, fill=mix(BG, (200, 170, 90), 0.8))
    c.line([(500, 840), (500, 520)], COTTON, 16)
    up = min(1.0, t / 10)
    c.line([(500, 840), (500, 840 - 320 * up)], mix(COTTON, (200, 170, 90), 0.8), 16)
    c.text(560, 520, '灯芯顶：火苗在这里', 'sans', 22, MUTED, 'lm')
    c.text(560, 560, '（只画示意，不点火）', 'sans', 20, NRED, 'lm')
    c.text(500, 890, '碗底的油', 'sans', 22, MUTED, 'mm')
    gx = [1100, 1390, 1680]
    ws = [10, 22, 44]
    c.rect(1000, 820, 1860, 920, fill=mix(BG, DYE, 0.6))
    for k, (x, w) in enumerate(zip(gx, ws)):
        hmax = 3600 / w
        h = hmax * (1 - math.exp(-t / 4))
        c.rect(x - w / 2 - 22, 300, x - w / 2, 900, fill=mix(BG, FIBER, 0.9), r=4)
        c.rect(x + w / 2, 300, x + w / 2 + 22, 900, fill=mix(BG, FIBER, 0.9), r=4)
        top = 820 - h
        c.rect(x - w / 2, top, x + w / 2, 820, fill=mix(BG, DYE, 0.9))
        c.arc(x, top, w / 2, 8, 0, 180, mix(BG, DYE, 0.9), 2)
        c.text(x, 960 - 0, ['很细的缝', '细一点', '宽缝'][k], 'bold', 22, INK, 'mm')
        c.text(x + w / 2 + 34, top, f'{h / 40:.1f}', 'mono', 20, SPARK, 'lm')
    c.text(1430, 265, '放大看纤维之间的缝（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '油灯的油在碗底，灯芯一头泡在油里，一头伸到碗外'),
                (7.2, 14, '灯芯是一束纤维，纤维之间有无数细缝，液体贴着缝壁一点点往上爬'),
                (14.2, 22, '缝越细，爬得越高：这叫毛细现象，火苗烧掉一点，下面就补上一点（示意）')], y=1010)


def b149_race(c, t, i):
    corner_tag(c, 'B149 · 四种「灯芯」比赛')
    c.text(60, 96, '棉线、纸巾条、毛线、细吸管，一头同时浸进色素水：每分钟量一次颜色爬了多高', 'serif', 36, INK)
    c.line([(160, 280), (1300, 280)], mix(BG, WOOD, 0.9), 14)
    c.text(1330, 280, '横放的筷子', 'sans', 20, MUTED, 'lm')
    c.rect(140, 760, 1320, 900, fill=mix(BG, DYE, 0.55), r=10)
    items = [('纸巾条', 8.0, 60), ('棉线', 6.0, 14), ('毛线', 3.5, 24), ('细吸管', 1.2, 26)]
    mins = min(10.0, t / 22 * 12)
    for k, (lab, hmax, w) in enumerate(items):
        x = 300 + k * 280
        c.rect(x - w / 2, 280, x + w / 2, 880, fill=mix(BG, COTTON, 0.85) if k < 3 else mix(BG, (210, 220, 230), 0.4), r=4)
        h = hmax * math.sqrt(mins / 10)
        y = 760 - h * 55
        c.rect(x - w / 2, y, x + w / 2, 880, fill=mix(BG, DYE, 0.95), r=4)
        c.text(x, 940, lab, 'bold', 24, INK, 'mm')
        c.text(x + w / 2 + 10, y, f'{h:.1f} 厘米', 'mono', 20, SPARK, 'lm')
    c.rect(1450, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1655, 350, f'{mins:.1f} 分钟', 'mono', 40, INK, 'mm')
    c.text(1655, 430, '只用水和色素', 'bold', 22, NRED, 'mm')
    c.text(1655, 470, '不点火、不用油', 'bold', 22, NRED, 'mm')
    c.text(1655, 560, '数值以实测为准', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '四种东西一起挂在筷子上，下端同时浸进加了色素的水'),
                (7.2, 14, '开头爬得快，越往上越慢：要把越来越长的一段水柱托住'),
                (14.2, 22, '纸巾的缝又细又多爬得最高；吸管里只有一条宽缝，几乎不动（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十四季特辑
OLD34 = [('公道杯', 'B20'), ('唧筒', 'B27'), ('龙骨水车', 'B91'), ('桔槔', 'B90'), ('窑洞', 'B83'), ('蒸发冷却罐', '38'),
         ('竹蜻蜓', 'B40'), ('机翼', '86'), ('羊皮筏子', 'B82'), ('不倒翁', 'B51'), ('夯土版筑', 'B46'), ('罗马混凝土', 'B35'),
         ('冰鉴与藏冰', 'B12'), ('曲辕犁', 'B59'), ('筛子', 'B114'), ('拓印', 'B77'), ('窗纸', 'B119'), ('长信宫灯', 'B22'), ('毛笔', 'B78')]
NEW34 = [('渴乌', 'B140', ['公道杯', '唧筒']), ('螺旋泵', 'B141', ['龙骨水车', '桔槔']), ('风塔', 'B142', ['窑洞', '蒸发冷却罐']),
         ('回旋镖', 'B143', ['竹蜻蜓', '机翼']), ('边架艇', 'B144', ['羊皮筏子', '不倒翁']), ('草拌泥', 'B145', ['夯土版筑', '罗马混凝土']),
         ('地窖', 'B146', ['窑洞', '冰鉴与藏冰']), ('耧车', 'B147', ['曲辕犁', '筛子']), ('装裱', 'B148', ['拓印', '窗纸']),
         ('灯芯', 'B149', ['长信宫灯', '毛笔'])]


def s34_graph(c, t, i):
    corner_tag(c, '第三十四季特辑 · 古法解密 14.0')
    c.text(60, 118, '水、风、土、纸：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD34):
        pos[name] = (340, 205 + k * 41)
    for k, (name, num, deps) in enumerate(NEW34):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十四季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW34):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD34:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW34):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十四季：水、风、土、纸，这一季中外各半'),
                (8.2, 16, '公道杯长出渴乌，龙骨水车长出螺旋泵，窑洞长出风塔和地窖，竹蜻蜓和机翼长出回旋镖'),
                (16.2, 24, '羊皮筏子长出边架艇，夯土长出草拌泥，曲辕犁长出耧车，拓印和窗纸长出装裱'),
                (24.2, 30, '最后，长信宫灯和毛笔一起，长出了把油拉上去的灯芯')], y=1040)


CLIPS = {
 'B149_细缝': (b149_capillary, 22), 'B149_比赛': (b149_race, 22),
 'B149_片头': (titles.opening(BSER, VOL34, SB34, 9, '先秦已有油灯，用灯草作芯'), 7),
 'B149_片尾': (titles.closing(BSER, VOL34, SB34, 9, '下集：第三十四季特辑 · 古法解密 14.0 回顾'), 7),
 'S34_依赖': (s34_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
