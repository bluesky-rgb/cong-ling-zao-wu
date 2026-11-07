"""第二十三季收尾：E131 空间站、第二十三季特辑（第八层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s23a import S23A, SER23, VOL23, WATER, WATER_L, CONC, GROUND

CUPC = (235, 230, 215)
EARTH = (70, 130, 200)
LAND = (110, 160, 90)
BALL = (230, 120, 80)


# ---------------------------------------------------------------- E131 空间站
def _cup(c, x, y, level, leak):
    c.poly([(x - 60, y - 150), (x + 60, y - 150), (x + 45, y), (x - 45, y)], CUPC)
    c.poly([(x - 60 + 15 * (1 - level), y - 150 * level), (x + 60 - 15 * (1 - level), y - 150 * level), (x + 45, y - 4), (x - 45, y - 4)], WATER)
    for sgn in (-1, 1):
        hx = x + sgn * 48
        c.ellipse(hx, y - 30, 5, 5, fill=(60, 60, 70))
        if leak > 0:
            pts = []
            for j in range(12):
                u = j / 11
                pts.append((hx + sgn * 90 * u * leak, y - 30 + 160 * u * u * leak))
            c.line(pts, WATER_L, 5)


def e131_drop(c, t, i):
    corner_tag(c, '第 131 集 · 一起往下掉，水就不漏了')
    c.text(60, 96, '拿着杯子，水从孔里喷出来；一松手，杯子和水一起下落，孔里就不流了', 'serif', 40, INK)
    x = 960
    c.rect(700, 900, 1220, 940, fill=mix(BG, WATER, 0.5))
    if t < 8:
        y = 420
        _cup(c, x, y, 0.9 - 0.02 * t, 1.0)
        c.rect(x - 20, y - 220, x + 20, y - 150, fill=(220, 180, 150), r=8)
        c.text(x + 160, y - 120, '手拿着：水往下喷', 'bold', 26, INK, 'lm')
    else:
        tt = min(t - 8, 2.2)
        y = 420 + 0.5 * 220 * tt * tt * (480 / (0.5 * 220 * 2.2 * 2.2))
        _cup(c, x, min(y, 880), 0.74, 0.0 if y < 880 else 1.0)
        c.text(x + 160, min(y, 880) - 120, '下落中：孔里不流水' if y < 880 else '落地', 'bold', 26, GREEN if y < 880 else INK, 'lm')
    c.rect(1380, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 340, '为什么？', 'bold', 26, INK, 'mm')
    c.text(1420, 420, '拿着时：杯子不动，', 'sans', 22, INK, 'lm')
    c.text(1420, 460, '水被重力往下压出去', 'sans', 22, INK, 'lm')
    c.text(1420, 530, '下落时：杯和水掉得一样快，', 'sans', 22, INK, 'lm')
    c.text(1420, 570, '水不再「压」着杯底', 'sans', 22, GREEN, 'lm')
    caps(c, t, [(0, 7, '纸杯侧面扎两个小孔，装满水拿在手里：水从孔里哗哗地喷出来'),
                (7.2, 14, '一松手，杯子和水一起往下掉，掉得一样快：孔里的水忽然不流了'),
                (14.2, 22, '这一瞬间，杯里的水就「失重」了。空间站里的人，就一直处在这一瞬间')], y=1010)


def e131_cannon(c, t, i):
    corner_tag(c, '第 131 集 · 一直在掉，却总也掉不到地上')
    c.text(60, 96, '扔得越快，落得越远；快到地面弯下去的速度跟得上，就绕着地球一直「掉」', 'serif', 40, INK)
    cx, cy, R = 760, 640, 300
    c.ellipse(cx, cy, R, R, fill=EARTH)
    for k in range(5):
        a = k * 1.3 + 0.3
        c.ellipse(cx + 180 * math.cos(a), cy + 180 * math.sin(a), 60, 40, fill=LAND)
    top = (cx, cy - R - 30)
    c.rect(cx - 10, cy - R - 60, cx + 10, cy - R - 20, fill=CONC)
    speeds = [(0.55, (230, 150, 90)), (0.8, SPARK), (1.0, GREEN)]
    n = min(3, int(t / 6) + 1)
    for k in range(n):
        v, col = speeds[k]
        r0 = R + 30
        prog = min(1.0, (t - k * 6) / 5.5) if k < 2 else min(1.0, (t - 12) / 9)
        pts = []
        steps = 300
        x, y = 0.0, r0
        vx, vy = v * math.sqrt(1 / r0) * r0 ** 0.5 * 1.0, 0.0
        GM = r0
        vx = v * math.sqrt(GM / r0)
        dt = 2.0
        for s in range(int(1040 * prog)):
            r = math.hypot(x, y)
            if r < R:
                break
            ax, ay = -GM * x / r ** 3, -GM * y / r ** 3
            vx += ax * dt; vy += ay * dt
            x += vx * dt; y += vy * dt
            pts.append((cx + x, cy - y))
        if len(pts) > 1:
            c.line(pts, col, 4)
            c.ellipse(pts[-1][0], pts[-1][1], 10, 10, fill=col)
    c.rect(1300, 260, 1860, 640, fill=SHEET, r=14)
    c.text(1580, 300, '同一座山顶，越扔越快（示意）', 'bold', 24, INK, 'mm')
    c.text(1340, 380, '慢：落在不远处', 'sans', 24, (230, 150, 90), 'lm')
    c.text(1340, 440, '快：落得更远', 'sans', 24, SPARK, 'lm')
    c.text(1340, 500, '够快：绕地球一圈回来', 'sans', 24, GREEN, 'lm')
    c.text(1340, 580, '空间站：约每秒 7.7 公里（拍摄前核对）', 'sans', 20, MUTED, 'lm')
    caps(c, t, [(0, 7, '在高山顶上水平扔一个球：扔得慢，它很快落地'),
                (7.2, 14, '扔得越快，落得越远；地球是圆的，地面也在往下弯'),
                (14.2, 22, '快到它往下掉的弯，和地面往下弯的弯一样：它就绕着地球一直「掉」，这就是第 101 集的卫星，也是空间站')], y=1010)


# ---------------------------------------------------------------- 第二十三季特辑
OLD23 = [('虹吸', '26'), ('水车提水', '28'), ('摆钟', '45'), ('磁生电', '04'), ('温度计', '46'), ('计算机', '91'),
         ('制盐', '20'), ('净水', '34'), ('齿轮与轴承', '41'), ('钢筋混凝土', '63'), ('悬索桥', '79'), ('电动机', '58'),
         ('机翼', '86'), ('水车发电', '06'), ('人造卫星', '101'), ('火箭', '88'), ('陀螺仪', '108')]
NEW23 = [('船闸', '122', ['虹吸', '水车提水']), ('地震仪', '123', ['摆钟', '磁生电']), ('天气预报', '124', ['温度计', '计算机']),
         ('海水淡化', '125', ['制盐', '净水']), ('盾构隧道', '126', ['齿轮与轴承', '钢筋混凝土']), ('抗风阻尼器', '127', ['摆钟', '悬索桥']),
         ('高铁', '128', ['电动机', '机翼']), ('潮汐发电', '129', ['水车发电', '人造卫星']), ('可回收火箭', '130', ['火箭', '陀螺仪']),
         ('空间站', '131', ['人造卫星', '净水'])]

def s23_layer(c, t, i):
    corner_tag(c, '第二十三季特辑 · 第八层')
    c.text(60, 118, '第八层：大工程', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD23):
        pos[name] = (340, 200 + k * 44)
    for k, (name, num, deps) in enumerate(NEW23):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第二十三季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW23):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD23:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW23):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第八层的十集：都是城市、海岸、天上的大工程'),
                (8.2, 16, '虹吸长出船闸，摆钟长出地震仪和阻尼器，计算机算出了天气预报'),
                (16.2, 24, '制盐和净水长出海水淡化，钢筋混凝土长出盾构隧道，电动机和机翼长出高铁'),
                (24.2, 30, '月亮推动潮汐电站，火箭学会落回地面，卫星长成了能住人的空间站')], y=1040)

CLIPS = {
 'E131_落杯': (e131_drop, 22), 'E131_绕地球': (e131_cannon, 22),
 'E131_片头': (titles.opening(SER23, VOL23, S23A, 9, '1971 年礼炮 1 号 · 2022 年天宫建成'), 7),
 'E131_片尾': (titles.closing(SER23, VOL23, S23A, 9, '下集：第二十三季特辑 · 第八层回顾'), 7),
 'S23_第八层': (s23_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
