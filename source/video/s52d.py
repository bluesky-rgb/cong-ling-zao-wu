"""第五十二季收尾：B239 竹杖 + 第五十二季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s52a import SB52, VOL52, ROAD

BAMBOO = (150, 180, 90)
BODY = (120, 150, 200)


def b239_base(c, t, i):
    corner_tag(c, 'B239 · 多一个支点，支撑范围变大')
    c.text(60, 96, '站着时，重心要落在两只脚围成的窄窄范围里；拄上一根杖，地上多一个支点，范围一下变大，不容易歪倒', 'serif', 36, INK)
    stick = t > 7.2
    # 俯视：两只脚 + 杖尖
    cx, cy = 960, 600
    feet = [(cx - 70, cy + 40), (cx + 70, cy + 40)]
    pts = [(cx - 110, cy - 40), (cx + 110, cy - 40), (cx + 110, cy + 120), (cx - 110, cy + 120)]
    if stick:
        tip = (cx + 380, cy - 240)
        c.ellipse(tip[0], tip[1], 22, 22, fill=mix(BG, BAMBOO, 1.0))
        c.text(tip[0], tip[1] - 50, '杖尖', 'bold', 26, GREEN, 'mm')
        poly = [(cx - 110, cy + 120), (cx - 110, cy - 40), tip, (cx + 110, cy + 120)]
        c.poly(poly, mix(BG, GREEN, 0.25))
    else:
        c.poly(pts, mix(BG, NRED, 0.25))
    for fx, fy in feet:
        c.ellipse(fx, fy, 40, 80, fill=mix(BG, BODY, 0.8))
    # 重心投影：左右前后晃
    sway = 150 * math.sin(t * 1.3)
    gx, gy_ = cx + sway * 0.8, cy + 40 - abs(sway) * 0.9
    c.ellipse(gx, gy_, 16, 16, fill=NRED)
    c.text(gx, gy_ + 40, '重心', 'bold', 22, NRED, 'mm')
    c.text(960, 900, '有杖：支撑范围（绿色）大得多' if stick else '没杖：支撑范围（红色）只有脚底这么窄', 'bold', 28, GREEN if stick else NRED, 'mm')
    caps(c, t, [(0, 7, '从上往下看：两只脚围成一小块，重心一晃就跑出去'),
                (7.2, 14, '拄上竹杖，杖尖在地上又多一个支点'),
                (14.2, 22, '三个支点围成一大片，重心在里面晃也不倒（示意）')], y=1010)


def b239_tripod(c, t, i):
    corner_tag(c, 'B239 · 两条腿站不住，三条腿站得住')
    c.text(60, 96, '两根铅笔插成「人」字，一松手就倒；插上第三根就成了三脚架：三个脚围成三角形，重心落在里面就站得稳', 'serif', 36, INK)
    gy = 820
    for j, (n, lab) in enumerate([(2, '两条腿'), (3, '三条腿')]):
        cx = 560 + j * 800
        top = (cx, 360)
        fall = (min(1.0, max(0, (t % 7) - 2) / 2) if n == 2 else 0)
        ang = fall * 1.2
        tx, ty = cx + 460 * math.sin(ang), gy - 460 * math.cos(ang)
        legs = [-160, 160] if n == 2 else [-160, 160, 0]
        for k, dx in enumerate(legs):
            col = mix(BG, (230, 200, 90), 1.0) if k < 2 else mix(BG, (230, 200, 90), 0.7)
            fx = cx + dx * (math.cos(ang) if n == 2 else 1)
            c.line([(tx, ty), (fx if n == 2 else fx + (40 if k == 2 else 0), gy + (0 if k < 2 else -40))], col, 12)
        c.ellipse(tx, ty, 26, 26, fill=mix(BG, (200, 150, 120), 1.0))
        c.line([(140 + j * 800, gy), (980 + j * 800, gy)], mix(BG, INK, 0.4), 3)
        c.text(cx, 900, lab + ('：站不住，一碰就倒' if n == 2 else '：稳稳站住'), 'bold', 28, NRED if n == 2 else GREEN, 'mm')
    caps(c, t, [(0, 7, '两个支点只能连成一条线，往旁边一歪就倒'),
                (7.2, 14, '三个支点围成三角形，重心落在里面就站得住'),
                (14.2, 22, '走山路拄竹杖，就是给自己多加一条「腿」（以实测为准）')], y=1010)


OLD52 = [('号角', 'B189'), ('灯笼', 'B180'), ('记里鼓车', 'B25'), ('沙漏', 'B96'), ('印章', 'B129'), ('鲁班锁', 'B99'),
         ('马镫', 'B173'), ('扁担', 'B100'), ('草鞋', 'B204'), ('谢公屐', 'B127'), ('车辐', 'B153'), ('门轴', 'B190'),
         ('榫卯', 'B7'), ('楔子', 'B150'), ('木桶', 'B110'), ('独轮车', 'B93'), ('高跷', 'B113'), ('竹梯', 'B192')]
NEW52 = [('烽燧', 'B230', ['号角', '灯笼']), ('驿马接力', 'B231', ['记里鼓车', '沙漏']), ('虎符', 'B232', ['印章', '鲁班锁']),
         ('马鞍', 'B233', ['马镫', '扁担']), ('马蹄铁', 'B234', ['草鞋', '谢公屐']), ('车脂', 'B235', ['车辐', '门轴']),
         ('车辖', 'B236', ['榫卯', '楔子']), ('铁箍车轮', 'B237', ['木桶', '车辐']), ('车轫', 'B238', ['楔子', '独轮车']),
         ('竹杖', 'B239', ['高跷', '竹梯'])]


def s52_graph(c, t, i):
    corner_tag(c, '第五十二季特辑 · 古法解密 23.0')
    c.text(60, 118, '驿路与车马：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD52):
        pos[name] = (342, 224 + k * 37)
    for k, (name, num, deps) in enumerate(NEW52):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 182, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十二季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW52):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD52:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW52):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 18, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第二十三季：驿路与车马'),
                (8.2, 16, '号角和灯笼长出烽燧，记里鼓车和沙漏长出驿马接力，印章和鲁班锁长出虎符，马镫和扁担长出马鞍'),
                (16.2, 24, '草鞋长出马蹄铁，车辐和门轴长出车脂，榫卯和楔子长出车辖，木桶长出铁箍车轮，楔子长出车轫'),
                (24.2, 30, '最后，高跷和竹梯一起，长出了竹杖')], y=1040)


CLIPS = {
 'B239_支点': (b239_base, 22), 'B239_三脚': (b239_tripod, 22),
 'B239_片头': (titles.opening(BSER, VOL52, SB52, 9, '苏轼写「竹杖芒鞋轻胜马」'), 7),
 'B239_片尾': (titles.closing(BSER, VOL52, SB52, 9, '下集：第五十二季特辑 · 古法解密 23.0 回顾'), 7),
 'S52_依赖': (s52_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
