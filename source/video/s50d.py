"""第五十季收尾：B229 车同轨 + 第五十季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s50a import SB50, VOL50

SAND = (215, 190, 140)
CART = (170, 120, 70)


def _cart(c, cx, y, gauge, col):
    c.rect(cx - gauge / 2 - 20, y - 70, cx + gauge / 2 + 20, y - 30, fill=col, r=6)
    for s in (-1, 1):
        c.rect(cx + s * gauge / 2 - 12, y - 40, cx + s * gauge / 2 + 12, y + 10, fill=mix(BG, (60, 60, 60), 1.0), r=4)


def b229_ruts(c, t, i):
    corner_tag(c, 'B229 · 车走多了，压出两道车辙')
    c.text(60, 96, '土路上，同样宽的车一辆接一辆走过，轮子总压在同一个地方，慢慢压出两道深深的车辙', 'serif', 36, INK)
    c.rect(200, 300, 1720, 900, fill=mix(BG, SAND, 0.8))
    g = 360
    cx = 960
    depth = min(1.0, t / 14)
    for s in (-1, 1):
        x = cx + s * g / 2
        c.rect(x - 24, 300, x + 24, 900, fill=mix(BG, SAND, 0.8 - 0.4 * depth))
    y = 900 - ((t * 160) % 700)
    _cart(c, cx, y, g, mix(BG, CART, 1.0))
    c.text(1500, 250, f'车辙越来越深（示意）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '每辆车的两个轮子之间的距离（轮距）都一样'),
                (7.2, 14, '轮子总压在同样的两条线上，土被压下去，成了两道车辙'),
                (14.2, 22, '车辙里走起来又稳又省力，车会顺着车辙一路走（示意）')], y=1010)


def b229_gauge(c, t, i):
    corner_tag(c, 'B229 · 轮距不一样：颠簸、卡住')
    c.text(60, 96, '轮距和车辙一样的车，顺着车辙走得又快又稳；轮距不一样，一个轮子在辙里、一个在辙外，车身歪斜，还会卡住', 'serif', 36, INK)
    for j, (lab, gauge) in enumerate([('轮距一样：顺着车辙走', 360), ('轮距宽一点：一边在辙外', 460)]):
        ox = 480 + j * 960
        c.rect(ox - 380, 300, ox + 380, 860, fill=mix(BG, SAND, 0.8))
        for s in (-1, 1):
            x = ox + s * 180
            c.rect(x - 24, 300, x + 24, 860, fill=mix(BG, SAND, 0.4))
        y = 860 - ((t * (160 if gauge == 360 else 60)) % 560)
        tilt = 0 if gauge == 360 else 10 * math.sin(t * 6)
        _cart(c, ox + tilt, y, gauge, mix(BG, (170, 120, 70), 1.0))
        c.text(ox, 920, lab, 'bold', 26, GREEN if gauge == 360 else NRED, 'mm')
    caps(c, t, [(0, 7, '轮距一样：两个轮子都落进车辙，走得又稳又快'),
                (7.2, 14, '轮距宽一点：一个轮子在辙里、一个在高高的路面上，车身一直歪'),
                (14.2, 22, '秦统一后规定轮距一致：全国的车都能顺着车辙走（以实测为准）')], y=1010)


OLD50 = [('都江堰', 'B5'), ('夯土版筑', 'B46'), ('窑洞', 'B83'), ('风塔', 'B142'), ('瓦片', 'B137'), ('筛子', 'B114'),
         ('渔网', 'B176'), ('七巧板', 'B60'), ('竹编', 'B73'), ('锯子', 'B178'), ('剪刀', 'B136'), ('鱼笱', 'B94'),
         ('秋千', 'B52'), ('拔河', 'B112'), ('九宫格', 'B164'), ('算筹', 'B134'), ('车辐', 'B153'), ('独轮车', 'B93')]
NEW50 = [('梯田', 'B220', ['都江堰', '夯土版筑']), ('土楼', 'B221', ['夯土版筑', '窑洞']), ('天井', 'B222', ['风塔', '瓦片']),
         ('蚊帐', 'B223', ['筛子', '渔网']), ('蜂巢', 'B224', ['七巧板', '竹编']), ('镰刀', 'B225', ['锯子', '剪刀']),
         ('鱼钩', 'B226', ['鱼笱', '渔网']), ('跳绳', 'B227', ['秋千', '拔河']), ('围棋', 'B228', ['九宫格', '算筹']),
         ('车同轨', 'B229', ['车辐', '独轮车'])]


def s50_graph(c, t, i):
    corner_tag(c, '第五十季特辑 · 古法解密 22.0')
    c.text(60, 118, '山居与田园：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD50):
        pos[name] = (342, 224 + k * 37)
    for k, (name, num, deps) in enumerate(NEW50):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 182, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW50):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD50:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW50):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 18, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第二十二季：山居与田园'),
                (8.2, 16, '都江堰和夯土长出梯田，夯土和窑洞长出土楼，风塔和瓦片长出天井，筛子和渔网长出蚊帐'),
                (16.2, 24, '七巧板和竹编长出蜂巢，锯子和剪刀长出镰刀，鱼笱长出鱼钩，秋千和拔河长出跳绳'),
                (24.2, 30, '九宫格和算筹长出围棋；最后，车辐和独轮车一起，长出了车同轨')], y=1040)




CLIPS = {
 'B229_车辙': (b229_ruts, 22), 'B229_轮距': (b229_gauge, 22),
 'B229_片头': (titles.opening(BSER, VOL50, SB50, 9, '秦统一后推行「车同轨」'), 7),
 'B229_片尾': (titles.closing(BSER, VOL50, SB50, 9, '下集：第五十季特辑 · 古法解密 22.0 回顾'), 7),
 'S50_依赖': (s50_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
