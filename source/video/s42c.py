"""第四十二季（古法解密 18.0）第三批：B186 栈道、B187 浮桥、B188 锚 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s42a import SB42, VOL42

ROCK = (110, 105, 100)
IRON = (120, 125, 135)
BOAT = (170, 120, 70)
SAND = (150, 130, 95)


# ---------------------------------------------------------------- B186 栈道
def b186_cant(c, t, i):
    corner_tag(c, 'B186 · 梁插进石壁，靠杠杆撑住')
    c.text(60, 96, '人站在梁的外端往下压；梁插在石孔里，孔口的上沿被往上顶、孔底的下沿被往下压：插得越深，两处的力越小，梁越稳', 'serif', 33, INK)
    cx = 520
    c.rect(200, 220, cx, 900, fill=mix(BG, ROCK, 0.95))
    for depth, y, lab in [(80, 420, '插得浅'), (260, 720, '插得深')]:
        c.rect(cx - depth - 10, y - 30, cx, y + 30, fill=mix(BG, (40, 40, 45), 1.0))
        c.rect(cx - depth, y - 22, cx + 800, y + 22, fill=mix(BG, WOOD, 1.0), r=4)
        px = cx + 700
        bob = 6 * math.sin(t * 2)
        c.ellipse(px, y - 70 + bob, 22, 22, fill=SPARK)
        c.rect(px - 18, y - 48 + bob, px + 18, y - 24, fill=SPARK, r=6)
        c.arrow(px, y - 130, px, y - 90, SPARK, 5, 14)
        f = 600 / depth * (0.6 + 0.4 * abs(math.sin(t)))
        L = min(150, 16 * f)
        c.arrow(cx - 4, y + 22 + L, cx - 4, y + 26, GREEN, 6, 16)
        c.arrow(cx - depth + 6, y - 22 - L, cx - depth + 6, y - 26, NRED, 6, 16)
        c.text(cx + 830, y, lab, 'bold', 26, INK, 'lm')
    c.text(1500, 900, '绿：孔口顶梁　红：孔底压梁（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '人一站上去，梁的外端被压下，整根梁想绕着孔口往下转'),
                (7.2, 14, '孔口的石头从下面顶住梁，孔底的石头从上面压住梁尾：两处一起把它别住'),
                (14.2, 22, '插得越深，梁尾的「力臂」越长，需要的力越小，石孔也越不容易崩')], y=1010)


def b186_strut(c, t, i):
    corner_tag(c, 'B186 · 下面加一根斜撑')
    c.text(60, 96, '只靠插进石壁的梁，外端一压就往下弯；在梁下面斜着顶一根木柱，把重量传回石壁，梁就几乎不弯了', 'serif', 36, INK)
    for j, strut in enumerate([False, True]):
        ox = 160 + j * 860
        y = 440
        c.rect(ox, 220, ox + 120, 900, fill=mix(BG, ROCK, 0.95))
        L = 560
        sag = (0 if strut else 70) * (0.5 + 0.5 * math.sin(t * 1.5) ** 2)
        pts = [(ox + 120 + k * L / 20, y + sag * (k / 20) ** 2) for k in range(21)]
        c.line(pts, mix(BG, WOOD, 1.0), 30)
        if strut:
            c.line([(ox + 120, y + 300), (ox + 120 + 360, y + 15)], mix(BG, WOOD, 0.85), 22)
            c.arrow(ox + 380, y + 100, ox + 220, y + 230, GREEN, 5, 14)
        c.ellipse(ox + 120 + L - 30, y + sag * 0.85 - 36, 20, 20, fill=SPARK)
        c.text(ox + 400, 820, '加斜撑：几乎不弯' if strut else '只插梁：外端下垂', 'bold', 28, GREEN if strut else NRED, 'mm')
    caps(c, t, [(0, 7, '用尺子插进一叠书里当栈道，尺子外端放硬币：尺子明显往下弯'),
                (7.2, 14, '在尺子下面斜着顶一根铅笔，另一头抵住书：再放同样的硬币'),
                (14.2, 22, '斜撑把重量顺着斜线传回「石壁」，梁只用管一小段（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B187 浮桥
def b187_buoy(c, t, i):
    corner_tag(c, 'B187 · 压多重，就排开多少水')
    c.text(60, 96, '船浮在水上，是因为它排开的水有多重，水就往上托它多大的力；桥上多一个人，船就往下沉一点，多排开一个人那么重的水', 'serif', 33, INK)
    wy = 600
    c.rect(0, wy, W, 960, fill=mix(BG, WATER, 0.45))
    n = int(t / 4) % 4
    sink = 16 * n
    for k in range(5):
        x = 260 + k * 300
        c.poly([(x - 110, wy - 50 + sink), (x + 110, wy - 50 + sink), (x + 80, wy + 40 + sink), (x - 80, wy + 40 + sink)], mix(BG, BOAT, 1.0))
    c.rect(120, wy - 74 + sink, 1800, wy - 50 + sink, fill=mix(BG, WOOD, 0.9))
    for m in range(n):
        px = 500 + m * 380
        c.ellipse(px, wy - 140 + sink, 22, 22, fill=SPARK)
        c.rect(px - 16, wy - 118 + sink, px + 16, wy - 76 + sink, fill=SPARK, r=6)
    c.line([(80, wy - 50), (1840, wy - 50)], mix(BG, MUTED, 0.6), 2)
    c.text(80, wy - 80, '空桥时船舷的位置', 'sans', 18, MUTED, 'lm')
    c.text(960, 880, f'桥上 {n} 人：船身多沉下 {sink // 4} 厘米（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '每条船都在往下压水，水也在往上托船：托力等于船排开的那部分水的重量'),
                (7.2, 14, '人走上桥，总重量变大，船就沉下一点，多排开一些水，托力跟着变大'),
                (14.2, 22, '只要船舷还露在水面上，托力就追得上：这就是浮桥能过人的原因（示意）')], y=1010)


def b187_share(c, t, i):
    corner_tag(c, 'B187 · 桥面把重量分给好几条船')
    c.text(60, 96, '一块硬桥板搭在几条船上：人站在哪里，重量不只压在脚下那一条船，而是被桥板分给左右好几条船一起扛', 'serif', 35, INK)
    wy = 620
    c.rect(0, wy, W, 960, fill=mix(BG, WATER, 0.45))
    px = 300 + (math.sin(t * 0.5) * 0.5 + 0.5) * 1300
    xs = [260 + k * 280 for k in range(6)]
    for x in xs:
        share = max(0.0, 1 - abs(x - px) / 600)
        s = 40 * share
        c.poly([(x - 100, wy - 50 + s), (x + 100, wy - 50 + s), (x + 70, wy + 40 + s), (x - 70, wy + 40 + s)], mix(BG, BOAT, 1.0))
        c.rect(x - 14, wy + 120, x + 14, wy + 120 + 120 * share, fill=SPARK, r=4)
    def sag(x):
        return 40 * max(0.0, 1 - abs(x - px) / 600)
    pts = [(120 + k * 17.6, wy - 62 + sag(120 + k * 17.6)) for k in range(101)]
    c.line(pts, mix(BG, WOOD, 0.9), 20)
    c.ellipse(px, wy - 150 + sag(px), 22, 22, fill=SPARK)
    c.rect(px - 16, wy - 128 + sag(px), px + 16, wy - 76 + sag(px), fill=SPARK, r=6)
    c.text(120, wy + 290, '每条船分到的重量（黄柱，示意）', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '如果每条船上各放一块短板，人走到哪条船，哪条船就猛地一沉'),
                (7.2, 14, '换成一整块长板搭在所有船上，人一站，附近几条船一起往下沉一点'),
                (14.2, 22, '重量被摊开，每条船只沉一点点，桥面也走得平稳（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B188 锚
def b188_dig(c, t, i):
    corner_tag(c, 'B188 · 越拉，锚爪吃得越深')
    c.text(60, 96, '锚落到水底，船往后一拽，锚杆被拉平，尖尖的锚爪就斜着扎进泥沙里；拉得越用力，爪子吃得越深，抓得越牢', 'serif', 34, INK)
    gy = 640
    c.rect(0, 200, W, gy, fill=mix(BG, WATER, 0.3))
    c.rect(0, gy, W, 960, fill=mix(BG, SAND, 0.9))
    r = random.Random(7)
    for k in range(80):
        c.ellipse(r.uniform(0, W), r.uniform(gy + 10, 950), 3, 3, fill=mix(BG, SAND, 0.6))
    p = min(1.0, t / 14)
    ax = 900 - 120 * p
    depth = 70 * p
    ang = math.radians(-50)
    shank = [(ax, gy - 10 + depth * 0.3), (ax + 300, gy - 10)]
    c.line(shank, IRON, 14)
    fx, fy = ax, gy - 10 + depth * 0.3
    tip = (fx - 110 * math.cos(ang), fy - 110 * math.sin(ang) + depth)
    c.line([(fx, fy), tip], IRON, 14)
    c.ellipse(tip[0], tip[1], 8, 8, fill=IRON)
    c.line([(ax + 300, gy - 10), (1700, 300)], mix(BG, INK, 0.7), 4)
    c.arrow(1500, 380, 1720, 300, SPARK, 6, 18)
    c.text(1600, 440, '船往后拽', 'sans', 24, SPARK, 'mm')
    for k in range(int(6 * p)):
        c.ellipse(tip[0] - 20 - k * 14, tip[1] - 30 + k * 4, 10, 6, fill=mix(BG, SAND, 1.0))
    c.text(ax - 60, gy + 200, '锚爪越扎越深（示意）', 'mono', 22, INK, 'mm')
    caps(c, t, [(0, 7, '锚刚落底时只是躺在沙上，光靠自己的重量抓不住大船'),
                (7.2, 14, '船一往后拽，锚杆被拉得贴着水底，锚爪的尖就斜着往下扎'),
                (14.2, 22, '越往后拉，爪子推开的泥沙越多，泥沙挡着它，力就越大（示意）')], y=1010)


def b188_scope(c, t, i):
    corner_tag(c, 'B188 · 锚链放长一点')
    c.text(60, 96, '锚链太短，船一拉就把锚往上提，爪子被拔出来；锚链放长，拉力几乎是水平的，锚爪才一直扎在底里', 'serif', 36, INK)
    for j, (lab, L, ok) in enumerate([('锚链短：往上提，锚被拔起', 1.2, False), ('锚链长：拉力贴着水底', 5, True)]):
        ox = 120 + j * 900
        sy, gy = 300, 820
        c.rect(ox, sy, ox + 800, gy, fill=mix(BG, WATER, 0.3))
        c.rect(ox, gy, ox + 800, gy + 60, fill=mix(BG, SAND, 0.9))
        bx = ox + 700
        c.poly([(bx - 70, sy - 30), (bx + 70, sy - 30), (bx + 50, sy + 10), (bx - 50, sy + 10)], mix(BG, BOAT, 1.0))
        ax = ox + 120 if ok else bx - 140
        lift = 0 if ok else 30 * abs(math.sin(t * 1.5))
        if ok:
            pts = [(bx - 50, sy + 10)]
            for k in range(1, 21):
                u = k / 20
                x = bx - 50 + (ax - bx + 50) * u
                yy = sy + 10 + (gy - sy - 10) * (1 - (1 - u) ** 3)
                pts.append((x, min(gy - 6, yy)))
            c.line(pts, mix(BG, INK, 0.7), 4)
        else:
            c.line([(bx - 50, sy + 10), (ax, gy - 10 - lift)], mix(BG, INK, 0.7), 4)
        c.line([(ax, gy - 10 - lift), (ax - 60, gy + 20 - lift * 1.5)], IRON, 10)
        c.text(ox + 400, gy + 110, lab, 'bold', 26, GREEN if ok else NRED, 'mm')
    caps(c, t, [(0, 7, '在浴缸里用小钩子当锚，系在玩具船上，链子放短、放长各拉一次'),
                (7.2, 14, '链子短，拉力斜着往上，把锚从沙里提起来；链子长，锚链大半躺在底上'),
                (14.2, 22, '一般建议锚链长度是水深的好几倍：具体倍数以资料和实测为准（示意）')], y=1010)


CLIPS = {
 'B186_杠杆': (b186_cant, 22), 'B186_斜撑': (b186_strut, 22),
 'B186_片头': (titles.opening(BSER, VOL42, SB42, 6, '战国时已在秦岭开凿栈道'), 7),
 'B186_片尾': (titles.closing(BSER, VOL42, SB42, 6, '下集：一排小船，怎么变成一座桥？'), 7),
 'B187_浮力': (b187_buoy, 22), 'B187_分担': (b187_share, 22),
 'B187_片头': (titles.opening(BSER, VOL42, SB42, 7, '周代已有「造舟为梁」的记载'), 7),
 'B187_片尾': (titles.closing(BSER, VOL42, SB42, 7, '下集：一只铁锚，怎么把大船拽住？'), 7),
 'B188_抓底': (b188_dig, 22), 'B188_链长': (b188_scope, 22),
 'B188_片头': (titles.opening(BSER, VOL42, SB42, 8, '古代先用石碇，后有铁锚'), 7),
 'B188_片尾': (titles.closing(BSER, VOL42, SB42, 8, '下集：吹响一只号角，声音为什么传得那么远？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
