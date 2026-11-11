"""第三十七季（第十五层：菜园与厨房）收官：E201 活性炭 + 第三十七季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L
from s37a import S37A, SER37, VOL37

CARBON = (70, 70, 75)
DYEC = (80, 120, 230)
SMELL = (200, 170, 90)


# ---------------------------------------------------------------- E201 活性炭
def e201_adsorption(c, t, i):
    corner_tag(c, '第 201 集 · 极细的孔把分子粘在孔壁上')
    c.text(60, 96, '放大一粒活性炭：里面是层层叠叠的细孔，色素和气味分子游进去，就被粘在孔壁上出不来了', 'serif', 36, INK)
    cx, cy = 700, 580
    c.rect(cx - 380, cy - 300, cx + 380, cy + 300, fill=mix(BG, WATER_L, 0.25), r=20)
    c.poly([(cx - 260, cy - 200), (cx + 240, cy - 230), (cx + 280, cy + 180), (cx - 220, cy + 240)], mix(BG, CARBON, 0.95))
    r = random.Random(5)
    walls = []
    for k in range(12):
        x = cx - 200 + k * 38
        y0 = cy - 180 + r.uniform(-20, 20)
        y1 = cy + 180 + r.uniform(-20, 20)
        c.line([(x, y0), (x + r.uniform(-20, 20), (y0 + y1) / 2), (x, y1)], mix(BG, (30, 30, 34), 1.0), 6)
        walls.append(x)
    p = min(1.0, t / 16)
    for k in range(50):
        stuck = k < 50 * p
        if stuck:
            w = walls[k % 12]
            y = cy - 160 + (k * 37) % 320
            c.ellipse(w + 6, y, 7, 7, fill=DYEC if k % 3 else SMELL)
        else:
            a = r.uniform(0, 2 * math.pi)
            rad = r.uniform(300, 360)
            x = cx + rad * math.cos(a + t * 0.2)
            y = cy + rad * 0.75 * math.sin(a + t * 0.2)
            c.ellipse(x, y, 7, 7, fill=DYEC if k % 3 else SMELL)
    c.rect(1180, 300, 1860, 780, fill=SHEET, r=14)
    c.text(1520, 350, '1 克活性炭的孔壁', 'bold', 26, INK, 'mm')
    c.text(1520, 410, '摊开有 500–1500 平方米', 'mono', 24, SPARK, 'mm')
    c.ellipse(1260, 510, 9, 9, fill=DYEC)
    c.text(1290, 510, '色素分子', 'sans', 22, INK, 'lm')
    c.ellipse(1260, 560, 9, 9, fill=SMELL)
    c.text(1290, 560, '气味分子', 'sans', 22, INK, 'lm')
    c.text(1520, 660, '实验的水都不喝', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '活性炭是木头、椰壳烧成炭以后，再用高温水蒸气「打」出无数细孔'),
                (7.2, 14, '色素、气味这些分子在水里、空气里乱跑，一撞进细孔，就被孔壁吸住'),
                (14.2, 22, '孔壁面积巨大，能吸住大量分子：冰箱除味、净水器滤芯都靠它（示意）')], y=1010)


def e201_dye(c, t, i):
    corner_tag(c, '第 201 集 · 活性炭那杯越来越淡')
    c.text(60, 96, '两杯同样的蓝色水：放活性炭的那杯一小时里越来越淡；放普通木炭的那杯几乎没变', 'serif', 36, INK)
    p = min(1.0, t / 16)
    for j, (lab, k_) in enumerate([('鱼缸用活性炭', 0.85), ('普通木炭碎', 0.15)]):
        cx = 520 + j * 880
        c.poly([(cx - 180, 320), (cx + 180, 320), (cx + 150, 820), (cx - 150, 820)], mix(BG, (200, 210, 220), 0.25))
        c.poly([(cx - 172, 380), (cx + 172, 380), (cx + 151, 812), (cx - 151, 812)], mix(mix(BG, WATER_L, 0.45), DYEC, 0.9 * (1 - k_ * p)))
        r = random.Random(j)
        for q in range(14):
            x = cx + r.uniform(-120, 120)
            y = 790 - r.uniform(0, 30)
            c.poly([(x - 14, y), (x, y - 16), (x + 16, y - 4), (x + 8, y + 10)], mix(BG, (60, 60, 65), 1.0))
        c.text(cx, 870, lab, 'bold', 26, INK, 'mm')
    c.rect(780, 220, 1140, 300, fill=SHEET, r=12)
    c.text(960, 260, f'过了 {p * 60:.0f} 分钟（示意）', 'mono', 24, INK, 'mm')
    c.text(960, 940, '以实测为准；敲木炭由成年人操作', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '两杯滴了蓝色色素的水，一杯放鱼缸用活性炭，一杯放普通烧烤木炭'),
                (7.2, 14, '每 10 分钟搅一搅：活性炭那杯越来越淡'),
                (14.2, 22, '普通木炭也有孔，可又少又粗，几乎吸不了：关键不在黑，在孔有多少、多细（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十七季特辑
OLD37 = [('玻璃', '21'), ('空调与热泵', '109'), ('化肥', '67'), ('选种与嫁接', '30'), ('塑料', '142'), ('摩擦起电', '01'),
         ('罐藏', '37'), ('压力锅', '155'), ('海水淡化', '125'), ('制冷', '68'), ('蒸发冷却罐', '38'), ('青霉素', '51'),
         ('温度计', '46'), ('开关与逻辑门', '81'), ('热电', '12'), ('数码相机', '95'), ('木炭与制陶', '16'), ('净水', '34')]
NEW37 = [('温室', '192', ['玻璃', '空调与热泵']), ('无土栽培', '193', ['化肥', '选种与嫁接']), ('保鲜膜', '194', ['塑料', '摩擦起电']),
         ('真空包装', '195', ['罐藏', '压力锅']), ('干燥剂', '196', ['海水淡化', '罐藏']), ('速冻', '197', ['制冷', '蒸发冷却罐']),
         ('冻干', '198', ['制冷', '青霉素']), ('恒温器', '199', ['温度计', '开关与逻辑门']), ('红外测温枪', '200', ['热电', '数码相机']),
         ('活性炭', '201', ['木炭与制陶', '净水'])]


def s37_layer(c, t, i):
    corner_tag(c, '第三十七季特辑 · 第十五层')
    c.text(60, 118, '第十五层：菜园与厨房', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD37):
        pos[name] = (340, 215 + k * 42)
    for k, (name, num, deps) in enumerate(NEW37):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 168, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十七季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW37):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD37:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW37):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十五层的十集：让菜种得出来、存得下去的机器'),
                (8.2, 16, '玻璃长出温室，化肥长出无土栽培，塑料长出保鲜膜，罐藏长出真空包装和干燥剂'),
                (16.2, 24, '制冷长出速冻和冻干，温度计长出恒温器，热电长出红外测温枪'),
                (24.2, 30, '最后，木炭和净水一起，长出了吸走颜色和怪味的活性炭')], y=1040)


CLIPS = {
 'E201_吸附': (e201_adsorption, 22), 'E201_颜色': (e201_dye, 22),
 'E201_片头': (titles.opening(SER37, VOL37, S37A, 9, '一战期间活性炭用于防毒面具'), 7),
 'E201_片尾': (titles.closing(SER37, VOL37, S37A, 9, '下集：第三十七季特辑 · 第十五层回顾'), 7),
 'S37_第十五层': (s37_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
