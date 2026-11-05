"""第十五季（第四层）第二批：E85 矿石收音机、E86 机翼、E87 电梯与安全钳 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s15a import S15A, SER15, VOL15, COIL, WAVE

AIR = (120, 170, 220)
WINGC = (200, 200, 210)
STEEL = (140, 145, 155)

# ---------------------------------------------------------------- E85 矿石收音机
def e85_tune(c, t, i):
    corner_tag(c, '第 85 集 · 线圈和电容选一个台')
    c.text(60, 96, '空中同时飘着很多台：共振只放一个进来', 'serif', 40, INK)
    x0, y0, W, H = 200, 800, 1500, 480
    c.line([(x0, y0), (x0 + W, y0)], LINE, 3)
    c.text(x0 + W / 2, y0 + 50, '频率 →', 'sans', 24, MUTED, 'mm')
    stations = [0.15, 0.32, 0.5, 0.68, 0.85]
    for k, u in enumerate(stations):
        x = x0 + u * W
        c.rect(x - 8, y0 - 120, x + 8, y0, fill=MUTED, r=3)
        c.text(x, y0 - 140, f'台 {k + 1}', 'sans', 22, MUTED, 'mm')
    f0 = 0.15 + 0.7 * (0.5 - 0.5 * math.cos(min(1, max(0, (t - 2) / 16)) * math.pi))
    pts = []
    for k in range(301):
        u = k / 300
        v = 1 / (1 + ((u - f0) / 0.035) ** 2)
        pts.append((x0 + u * W, y0 - H * 0.9 * v))
    c.line(pts, SPARK, 5)
    near = min(stations, key=lambda s: abs(s - f0))
    if abs(near - f0) < 0.03:
        x = x0 + near * W
        c.rect(x - 10, y0 - 120, x + 10, y0, fill=GREEN, r=3)
        c.text(x, y0 - H - 10, '收到了！', 'bold', 28, GREEN, 'mm')
    c.text(1720, 260, '转动可变电容 →', 'sans', 24, INK, 'rm')
    c.text(1720, 300, '共振峰左右移动', 'sans', 24, INK, 'rm')
    caps(c, t, [(0, 6, '天线收到的是所有电台叠在一起的电波'),
                (6.2, 13, '线圈和电容组成一个「秋千」：只有频率对上它的那一个台，才会被越推越大'),
                (13.2, 22, '转动可变电容，就是换秋千的节拍：峰对上哪个台，耳机里就是哪个台（接第 76 集无线电）')], y=1010)

def e85_detect(c, t, i):
    corner_tag(c, '第 85 集 · 二极管：电流的单行道')
    c.text(60, 96, '电波来回振荡太快，耳机跟不上：先砍掉一半', 'serif', 40, INK)
    rows = [('收到的电波（调幅）', 0, 1), ('二极管只放一个方向', 1, 4), ('耳机膜片跟着「平均」走：就是声音', 2, 8)]
    for k, (nm, mode, t0) in enumerate(rows):
        a = fade(t, t0, t0 + 1)
        if a <= 0: continue
        y = 340 + k * 220
        c.text(120, y - 100, nm, 'bold', 28, mix(BG, INK, a), 'lm')
        c.line([(120, y), (1800, y)], mix(BG, LINE, a), 1)
        pts = []
        for j in range(1201):
            x = j / 1200
            env = 0.55 + 0.4 * math.sin(x * 2 * math.pi * 3)
            carrier = math.sin(x * 2 * math.pi * 90)
            v = env * carrier
            if mode >= 1: v = max(0, v)
            if mode == 2: v = env * 0.64
            pts.append((120 + x * 1680, y - 80 * v))
        c.line(pts, mix(BG, WAVE if mode < 2 else GREEN, a), 2 if mode < 2 else 5)
    d = fade(t, 14, 15)
    c.text(960, 940, '不用电池：推动耳机的能量，全来自电台发来的电波', 'bold', 26, mix(BG, SPARK, d), 'mm')
    caps(c, t, [(0, 6, '电台把声音「骑」在高频电波上：电波的高矮跟着声音变，这叫调幅'),
                (6.2, 13, '高频电波一秒正负来回几十万次，耳机根本跟不上，正负一抵消就没声了'),
                (13.2, 22, '二极管只让电流朝一个方向走：砍掉一半，剩下的平均值，正好是声音的形状')], y=1010)

# ---------------------------------------------------------------- E86 机翼
def wing_shape(c, cx, cy, L, ang, col):
    pts = []
    for k in range(41):
        u = k / 40
        th = 0.12 * L * 4 * u * (1 - u) * (1 - 0.3 * u)
        pts.append((u, th))
    top = [(cx - L / 2 + u * L, cy - 0.35 * th - 0.06 * L * 4 * u * (1 - u)) for u, th in pts]
    bot = [(cx - L / 2 + u * L, cy + 0.35 * th - 0.06 * L * 4 * u * (1 - u)) for u, th in pts][::-1]
    poly = top + bot
    ca, sa = math.cos(ang), math.sin(ang)
    rp = [(cx + (x - cx) * ca - (y - cy) * sa, cy + (x - cx) * sa + (y - cy) * ca) for x, y in poly]
    c.poly(rp, col)

def e86_lift(c, t, i):
    corner_tag(c, '第 86 集 · 机翼把空气往下压')
    c.text(60, 96, '飞机往前冲，机翼把迎面的空气往下拨', 'serif', 40, INK)
    cx, cy = 900, 520
    ang = math.radians(8)
    for k in range(9):
        y = 300 + k * 55
        pts = []
        for j in range(61):
            x = 200 + j * 25
            dx = (x - cx) / 300
            bend = 70 * (1 / (1 + math.exp(-dx * 3))) * math.exp(-abs(y - cy) / 260)
            pts.append((x, y + bend))
        off = (t * 120) % 25
        seg(c, [(x + off, y_) for x, y_ in pts if x + off < 1720], mix(BG, AIR, 0.7), 2)
    wing_shape(c, cx, cy, 520, ang, WINGC)
    a = fade(t, 6, 7)
    for k in range(4):
        x = 1300 + k * 90
        c.arrow(x, 640, x + 20, 760, mix(BG, AIR, a), 4, 14)
    c.text(1450, 800, '空气被压向下方', 'bold', 26, mix(BG, AIR, a), 'mm')
    b = fade(t, 10, 11)
    c.arrow(cx, cy - 20, cx, cy - 240, mix(BG, GREEN, b), 8, 26)
    c.text(cx + 30, cy - 200, '空气把机翼往上推：升力', 'bold', 28, mix(BG, GREEN, b), 'lm')
    caps(c, t, [(0, 6, '机翼略微抬头，还有点弯：迎面的空气流过，被拨向下方'),
                (6.2, 13, '每秒钟有几吨的空气被往下压，空气也就把机翼往上推'),
                (13.2, 22, '和 B40 竹蜻蜓、B41 风筝是同一件事：斜着推空气，空气就推回来')], y=1010)

def e86_speed(c, t, i):
    corner_tag(c, '第 86 集 · 快一倍，升力四倍')
    c.text(60, 96, '为什么飞机要先在跑道上冲那么快', 'serif', 40, INK)
    speeds = [1, 2, 3]
    for k, v in enumerate(speeds):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        x = 400 + k * 520
        h = 45 * v * v * fade(t, 1.5 + k * 4, 3 + k * 4)
        c.rect(x - 80, 860 - h, x + 80, 860, fill=mix(BG, GREEN, a), r=6)
        c.text(x, 900, f'速度 × {v}', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(x, 840 - h, f'升力 × {v * v}', 'mono', 28, mix(BG, GREEN, a), 'mm')
    c.line([(200, 860), (1700, 860)], LINE, 2)
    d = fade(t, 13, 14)
    c.rect(1240, 200, 1840, 360, fill=mix(BG, SHEET, d), r=12)
    c.text(1540, 240, '升力 ∝ 空气密度 × 速度² × 翼面积', 'bold', 26, mix(BG, INK, d), 'mm')
    c.text(1540, 290, '速度不够，升力托不起飞机的重量', 'sans', 24, mix(BG, MUTED, d), 'mm')
    c.text(1540, 330, '所以要跑道加速，或者把机翼做大', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '速度快一倍：每秒撞上机翼的空气多一倍，每一份被拨下去的也快一倍'),
                (6.2, 13, '两样一乘，升力变成四倍；快三倍，就是九倍'),
                (13.2, 22, '飞机在跑道上一直加速，直到升力超过重量才抬头离地：1903 年莱特兄弟的飞机也是先在滑轨上冲')], y=1010)

# ---------------------------------------------------------------- E87 电梯与安全钳
def rail(c, x, y0, y1, side):
    c.rect(x - 14, y0, x + 14, y1, fill=STEEL)
    for y in range(int(y0), int(y1), 40):
        if side < 0:
            c.poly([(x + 14, y), (x + 34, y + 20), (x + 14, y + 40)], STEEL)
        else:
            c.poly([(x - 14, y), (x - 34, y + 20), (x - 14, y + 40)], STEEL)

def e87_brake(c, t, i):
    corner_tag(c, '第 87 集 · 绳子一松，钳子就弹出')
    c.text(60, 96, '靠绳子的拉力把刹车「拉开」：拉力没了，刹车自己合上', 'serif', 40, INK)
    lx, rx = 620, 1300
    rail(c, lx, 200, 980, -1)
    rail(c, rx, 200, 980, 1)
    cut = t > 8
    fall = 0 if not cut else min(60, (t - 8) * 120)
    top = 380 + fall
    cx = (lx + rx) / 2
    if not cut:
        c.line([(cx, 160), (cx, top - 60)], INK, 5)
    else:
        c.line([(cx, 160), (cx, 260)], INK, 5)
        c.text(cx + 30, 280, '绳断', 'bold', 28, NRED, 'lm')
    c.rect(lx + 60, top, rx - 60, top + 300, outline=INK, width=4, r=8)
    c.text(cx, top + 150, '电梯', 'bold', 34, INK, 'mm')
    c.line([(cx, top - 60), (cx, top)], INK, 5)
    out = 0 if not cut else min(1, (t - 8) * 6)
    for side, x in ((-1, lx + 34), (1, rx - 34)):
        px = x - side * 0 + (-side) * 0
        c.rect(x - 14 + side * 0, top + 20, x + 14, top + 60, fill=mix(BG, SPARK, 0.4 + 0.6 * out), r=4)
        dx = -side * (0 if out else 1) * 0
        c.poly([(x, top + 20), (x + side * 26 * out * -1, top + 40), (x, top + 60)], SPARK)
        c.line([(x, top + 60), (cx + side * -120, top - 10)], mix(BG, MUTED, 1 - out), 3)
    c.text(cx, 1000 - 40, '吊着时：绳子的拉力通过连杆把两边的钳子收住', 'sans', 24, MUTED if not cut else BG, 'mm')
    if cut:
        c.text(cx, 960, '绳一断：弹簧把钳子推进齿缝，卡死在导轨上', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 8, '电梯两边有导轨，轿厢上装着安全钳：平时被绳子的拉力收着'),
                (8.2, 14, '绳子一断，拉力没了，弹簧立刻把钳子推出去，卡进导轨'),
                (14.2, 22, '不用人去按，也不用电：1854 年奥的斯当众砍断绳子演示过（拍摄前核对）')], y=1040)

def e87_failsafe(c, t, i):
    corner_tag(c, '第 87 集 · 失效安全')
    c.text(60, 96, '出事的时候，最好什么都不用做', 'serif', 40, INK)
    rows = [('电梯安全钳', '绳子拉着才松开', '绳断 → 自动卡住'),
            ('火车空气刹车', '有气压才松开', '车厢脱开、管子断 → 自动刹车（拍摄前核对）'),
            ('割草机、电锯的握把开关', '一直握着才转', '一松手 → 自动停'),
            ('第 70 集避雷针', '平时什么都不做', '雷来了 → 电流自己走导线')]
    for k, (nm, normal, fail) in enumerate(rows):
        a = fade(t, 1 + k * 3.5, 2 + k * 3.5)
        if a <= 0: continue
        y = 240 + k * 160
        c.rect(120, y - 50, 1800, y + 50, fill=mix(BG, SHEET, a), r=12)
        c.text(160, y, nm, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(720, y, normal, 'sans', 24, mix(BG, MUTED, a), 'lm')
        c.text(1100, y, fail, 'sans', 24, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 6, '奥的斯的办法有一个名字：失效安全'),
                (6.2, 14, '让「正常工作」需要一直出力，一旦出力消失，系统自动落到安全的那一边'),
                (14.2, 22, '火车刹车、电锯开关都是这个思路：出事时，没人来得及去按按钮')], y=1010)

CLIPS = {
 'E85_调谐': (e85_tune, 22), 'E85_检波': (e85_detect, 22),
 'E85_片头': (titles.opening(SER15, VOL15, S15A, 3, '1906 年 · 皮卡德晶体检波器'), 7),
 'E85_片尾': (titles.closing(SER15, VOL15, S15A, 3, '下集：几十吨重的飞机，凭什么飘在空中？'), 7),
 'E86_升力': (e86_lift, 22), 'E86_速度': (e86_speed, 22),
 'E86_片头': (titles.opening(SER15, VOL15, S15A, 4, '1903 年 · 莱特兄弟'), 7),
 'E86_片尾': (titles.closing(SER15, VOL15, S15A, 4, '下集：电梯的绳子断了，为什么不会掉下去？'), 7),
 'E87_安全钳': (e87_brake, 22), 'E87_失效安全': (e87_failsafe, 22),
 'E87_片头': (titles.opening(SER15, VOL15, S15A, 5, '1854 年 · 奥的斯'), 7),
 'E87_片尾': (titles.closing(SER15, VOL15, S15A, 5, '下集：太空里没有空气可以推，火箭怎么往前飞？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
