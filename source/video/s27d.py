"""第二十七季收尾：E151 气凝胶、第二十七季特辑（第十层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s27a import S27A, SER27, VOL27, CHAIN, WATER_L

SILICA = (200, 215, 235)
AIRC = (150, 200, 240)
HOT = (235, 110, 80)
ICE = (200, 235, 250)


# ---------------------------------------------------------------- E151 气凝胶
def e151_pores(c, t, i):
    corner_tag(c, '第 151 集 · 把空气关进极小的孔里')
    c.text(60, 96, '气凝胶九成以上是空气：一层极细的骨架围出无数比头发细几千倍的小孔，空气分子关在里面，几乎没法带着热跑', 'serif', 34, INK)
    for col_i, (lab, caged) in enumerate((('敞开的空气', False), ('关在小孔里的空气', True))):
        x0 = 140 + col_i * 880
        y0, y1 = 260, 860
        c.rect(x0, y0, x0 + 760, y1, outline=LINE, width=2, r=12)
        c.text(x0 + 380, y0 - 30, lab, 'bold', 26, INK, 'mm')
        c.rect(x0, y1 - 40, x0 + 760, y1, fill=mix(BG, HOT, 0.8), r=6)
        c.text(x0 + 380, y1 + 30, '下面是热的', 'sans', 20, HOT, 'mm')
        rnd = random.Random(5 + col_i)
        if caged:
            for gx in range(8):
                for gy in range(7):
                    cx = x0 + 50 + gx * 95
                    cy = y0 + 40 + gy * 80
                    c.ellipse(cx, cy, 44, 36, outline=SILICA, width=3)
                    ph = t * 3 + gx * 1.3 + gy * 0.7
                    c.ellipse(cx + 18 * math.cos(ph), cy + 14 * math.sin(ph * 1.3), 6, 6, fill=AIRC)
            c.text(x0 + 380, y1 + 70, '每个分子只在自己的小孔里打转，热传得很慢', 'bold', 22, GREEN, 'mm')
        else:
            for k in range(50):
                s = (t * 0.25 + rnd.random()) % 1
                x = x0 + 40 + rnd.random() * 680 + 30 * math.sin(t * 2 + k)
                y = y1 - 60 - s * (y1 - y0 - 100)
                c.ellipse(x, y, 6, 6, fill=mix(AIRC, HOT, 1 - s))
            c.text(x0 + 380, y1 + 70, '热空气往上冒，把热一路带走（对流）', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '空气本身是很差的导热体，可它一流动，就会把热带走：热空气往上升，冷空气补进来'),
                (7.2, 14, '气凝胶用一层极细的骨架，把空气分成无数个比头发细几千倍的小孔（尺寸拍摄前核对）'),
                (14.2, 22, '空气被关住了，流不动，连互相碰撞都少了：热只能慢慢地挪，所以它特别隔热（示意）')], y=1010)


def e151_ice(c, t, i):
    corner_tag(c, '第 151 集 · 哪块冰化得最慢')
    c.text(60, 96, '同样大的冰块：不包的最先化完；棉布、泡沫、气泡膜都靠「关住空气」挡热，把气泡扎破，效果就差了', 'serif', 36, INK)
    wraps = [('不包', 40, (90, 90, 100)), ('两层棉布', 75, (220, 210, 190)), ('泡沫块', 120, (235, 235, 240)), ('三层气泡膜', 105, AIRC), ('扎破的气泡膜', 70, (160, 180, 200))]
    mins = min(130, t / 20 * 130)
    for k, (nm, life, col) in enumerate(wraps):
        x = 220 + k * 370
        left = max(0, 1 - mins / life)
        s = 120 * math.sqrt(left)
        c.rect(x - 140, 640, x + 140, 660, fill=(150, 150, 160), r=4)
        if k > 0:
            c.rect(x - 110, 640 - 160, x + 110, 640, outline=col, width=8, r=20)
        if s > 2:
            c.rect(x - s / 2, 640 - s, x + s / 2, 640, fill=ICE, r=8)
        c.ellipse(x, 668, 80 * (1 - left) + 4, 8, fill=WATER_L)
        c.text(x, 720, nm, 'bold', 24, INK, 'mm')
        c.text(x, 770, '化完了' if left <= 0 else f'剩 {left * 100:.0f}%', 'mono', 22, NRED if left <= 0 else MUTED, 'mm')
    c.text(960, 230, f'第 {mins:.0f} 分钟（示意，以实测为准）', 'mono', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '四块一样大的冰：一块不包，一块包两层棉布，一块塞进泡沫块，一块包三层气泡膜'),
                (7.2, 14, '不包的最先化完；包着的都慢得多：它们都在冰块周围关住了一层不流动的空气'),
                (14.2, 22, '把气泡膜的泡泡全扎破再包，空气能跑了，冰就化得快了：气凝胶把这一招做到了极致（时间为示意）')], y=1010)


# ---------------------------------------------------------------- 第二十七季特辑
OLD27 = [('肥皂', '22'), ('罐藏', '37'), ('自行车', '66'), ('齿轮与轴承', '41'), ('炼铁', '18'), ('钢', '62'),
         ('电镀', '59'), ('蓄电池', '61'), ('螺丝与标准件', '64'), ('显微镜', '53'), ('制冷', '68'), ('蒸发冷却罐', '38'),
         ('玻璃', '21'), ('纸', '23'), ('净水', '34'), ('钢筋混凝土', '63'), ('石墨烯', '117')]
NEW27 = [('塑料', '142', ['肥皂', '罐藏']), ('橡胶轮胎', '143', ['自行车', '齿轮与轴承']), ('不锈钢', '144', ['炼铁', '钢']),
         ('铝', '145', ['电镀', '蓄电池']), ('魔术贴', '146', ['螺丝与标准件', '显微镜']), ('保温杯', '147', ['制冷', '蒸发冷却罐']),
         ('不粘锅', '148', ['肥皂', '玻璃']), ('纸尿裤', '149', ['纸', '净水']), ('复合材料', '150', ['钢筋混凝土', '纸']),
         ('气凝胶', '151', ['保温杯', '石墨烯'])]


def s27_layer(c, t, i):
    corner_tag(c, '第二十七季特辑 · 第十层')
    c.text(60, 118, '第十层：新材料', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD27):
        pos[name] = (340, 200 + k * 46)
    for k, (name, num, deps) in enumerate(NEW27):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第二十七季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW27):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if x0 > 900:
                sx, ex = x0 - 110, x1 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD27:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW27):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十层的十集：身边那些「新材料」'),
                (8.2, 16, '肥皂和罐藏长出塑料，自行车长出橡胶轮胎，钢长出不锈钢，电长出便宜的铝'),
                (16.2, 24, '显微镜长出魔术贴，制冷长出保温杯，玻璃和肥皂长出不粘锅，纸长出纸尿裤和复合材料'),
                (24.2, 30, '最后，保温杯的真空和石墨烯的薄，一起长出了轻得像烟的气凝胶')], y=1040)


CLIPS = {
 'E151_多孔': (e151_pores, 22), 'E151_冰块': (e151_ice, 22),
 'E151_片头': (titles.opening(SER27, VOL27, S27A, 9, '1931 年基斯特勒制成第一块气凝胶'), 7),
 'E151_片尾': (titles.closing(SER27, VOL27, S27A, 9, '下集：第二十七季特辑 · 第十层回顾'), 7),
 'S27_第十层': (s27_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
