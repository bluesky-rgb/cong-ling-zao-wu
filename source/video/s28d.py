"""第二十八季收尾：B119 窗纸、第二十八季特辑（古法解密 11.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s28a import SB28, VOL28, WOOD

FIBERC = (235, 228, 210)
OILC = (230, 200, 120)
LIGHT = (250, 230, 150)


# ---------------------------------------------------------------- B119 窗纸
def _paper(c, x0, y0, w, h, oiled, t, seed):
    rnd = random.Random(seed)
    if oiled:
        c.rect(x0, y0, x0 + w, y0 + h, fill=mix(BG, OILC, 0.45))
    for k in range(45):
        x = x0 + rnd.random() * w
        y = y0 + rnd.random() * h
        a = rnd.uniform(-0.5, 0.5)
        L = rnd.uniform(60, 140)
        c.line([(x - L / 2 * math.cos(a), y - L / 2 * math.sin(a)), (x + L / 2 * math.cos(a), y + L / 2 * math.sin(a))], mix(FIBERC, BG, 0.15), 5)


def b119_scatter(c, t, i):
    corner_tag(c, 'B119 · 纸为什么白而不透：光在缝里乱拐')
    c.text(60, 96, '纸纤维本身透明，中间夹着空气：光过一道边界拐一次弯，拐来拐去大多被弹回；刷上油填满缝，光就直着过去', 'serif', 34, INK)
    for row, (oiled, lab) in enumerate(((False, '白纸：纤维 + 空气'), (True, '油纸：纤维 + 油'))):
        y0 = 250 + row * 360
        x0, w, h = 700, 420, 260
        _paper(c, x0, y0, w, h, oiled, t, 3 + row)
        c.text(x0 + w / 2, y0 - 26, lab, 'bold', 24, INK, 'mm')
        rnd = random.Random(10 + row)
        for k in range(7):
            yy = y0 + 30 + k * 32
            s = (t * 0.35 + k * 0.13) % 1
            if not oiled:
                pts = [(200, yy), (x0, yy)]
                x, y = x0, yy
                ang = 0
                steps = int(s * 14)
                for j in range(steps):
                    ang += rnd.uniform(-1.6, 1.6)
                    x += 30 * math.cos(ang)
                    y += 30 * math.sin(ang)
                    x = max(x0 - 120, min(x0 + w + 80, x))
                    y = max(y0, min(y0 + h, y))
                    pts.append((x, y))
                c.line(pts, mix(BG, LIGHT, 0.8), 3)
            else:
                xe = 200 + (1500 - 200) * s
                c.line([(200, yy), (min(xe, 1500), yy)], mix(BG, LIGHT, 0.9), 3)
        res = '大部分被弹回：看起来白、不透亮' if not oiled else '大部分直着穿过：半透明，屋里亮'
        c.text(x0 + w / 2, y0 + h + 30, res, 'bold', 22, NRED if not oiled else GREEN, 'mm')
    caps(c, t, [(0, 7, '一根纸纤维本身几乎是透明的；纸之所以白，是因为纤维之间塞满了空气'),
                (7.2, 14, '光从纤维进空气、再进纤维，每过一道边界就拐个弯，拐上几十次，大部分又被弹回来'),
                (14.2, 22, '刷上油，空气缝被填满，油和纤维对光「差不多」，光就不拐弯，直着穿过去（示意）')], y=1010)


def b119_trans(c, t, i):
    corner_tag(c, 'B119 · 测一测透过多少光')
    c.text(60, 96, '手机测光 App 贴在纸框后面对着窗户：白纸透过一小部分，油纸透过的多得多，两层白纸更暗，保鲜膜几乎全透', 'serif', 36, INK)
    data = [('白纸', 30, FIBERC), ('两层白纸', 12, mix(FIBERC, BG, 0.2)), ('油纸', 70, OILC), ('保鲜膜', 90, (200, 225, 240))]
    gx0, gy0 = 300, 840
    c.line([(gx0, gy0), (1500, gy0)], LINE, 2)
    grow = min(1, t / 10)
    for k, (nm, v, col) in enumerate(data):
        x = gx0 + 60 + k * 290
        h = 520 * v / 100 * grow
        c.rect(x, gy0 - h, x + 180, gy0, fill=col, r=8)
        c.text(x + 90, gy0 + 40, nm, 'bold', 24, INK, 'mm')
        c.text(x + 90, gy0 - h - 30, f'约 {v * grow:.0f}%', 'mono', 24, INK, 'mm')
    c.rect(1560, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1710, 340, '窗纸的取舍', 'bold', 24, INK, 'mm')
    c.text(1710, 410, '透光：油纸', 'sans', 22, INK, 'mm')
    c.text(1710, 460, '挡风：纸都行', 'sans', 22, INK, 'mm')
    c.text(1710, 510, '不怕潮：油纸', 'sans', 22, INK, 'mm')
    c.text(1710, 600, '（百分比为示意，', 'sans', 18, MUTED, 'mm')
    c.text(1710, 630, '以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '四个纸框：白纸、两层白纸、刷油的纸、保鲜膜，用手机测光 App 贴在后面对着窗户读数'),
                (7.2, 14, '白纸透过的光不多；刷了油的纸亮多了，水滴上去也不会被吸进去'),
                (14.2, 22, '没有玻璃的年代，油纸窗又透光、又挡风、还不怕潮；更讲究的人家用磨薄的贝壳做「明瓦」（史料拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- 第二十八季特辑
OLD28 = [('榫卯', 'B7'), ('竹编', 'B73'), ('搓麻绳', 'B101'), ('辘轳', 'B81'), ('畜力与人力', '08'), ('独轮车', 'B93'),
         ('不倒翁', 'B51'), ('欹器', 'B21'), ('扇车', 'B56'), ('石磨', 'B76'), ('瓷器', 'B16'), ('陀螺', 'B50'),
         ('皮影戏', 'B64'), ('杠杆与滑轮组', '39'), ('算盘', 'B54'), ('投壶', 'B89'), ('拓印', 'B77'), ('交子防伪', 'B29'),
         ('油纸伞', 'B58'), ('纸', '23')]
NEW28 = [('木桶', 'B110', ['榫卯', '竹编']), ('缆桩', 'B111', ['搓麻绳', '辘轳']), ('拔河', 'B112', ['畜力与人力', '独轮车']),
         ('高跷', 'B113', ['不倒翁', '欹器']), ('筛子', 'B114', ['扇车', '石磨']), ('陶车', 'B115', ['瓷器', '陀螺']),
         ('提线木偶', 'B116', ['皮影戏', '杠杆与滑轮组']), ('骰子', 'B117', ['算盘', '投壶']), ('画押', 'B118', ['拓印', '交子防伪']),
         ('窗纸', 'B119', ['油纸伞', '纸'])]


def s28_graph(c, t, i):
    corner_tag(c, '第二十八季特辑 · 古法解密 11.0')
    c.text(60, 118, '桶、绳、戏、窗：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD28):
        pos[name] = (340, 196 + k * 40)
    for k, (name, num, deps) in enumerate(NEW28):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第二十八季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW28):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD28:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW28):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十一季：桶、绳、戏、窗'),
                (8.2, 16, '木桶靠箍和湿胀，缆桩靠绕圈的摩擦，拔河比脚下的摩擦，高跷追着重心走'),
                (16.2, 24, '筛子让小的钻缝，陶车让手转出圆，木偶靠一根根杠杆，骰子掷多了才见规律'),
                (24.2, 30, '画押靠人人不同的指纹，窗纸靠一层油透光：都是讲得清的道理')], y=1040)


CLIPS = {
 'B119_散射': (b119_scatter, 22), 'B119_透光': (b119_trans, 22),
 'B119_片头': (titles.opening(BSER, VOL28, SB28, 9, '宋代油纸窗与明瓦窗'), 7),
 'B119_片尾': (titles.closing(BSER, VOL28, SB28, 9, '下集：第二十八季特辑 · 古法解密 11.0 回顾'), 7),
 'S28_依赖': (s28_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
