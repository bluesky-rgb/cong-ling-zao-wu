"""第三十九季（第十六层：运动场）第三批：E208 泳衣、E209 电子计时、E210 鹰眼 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L
from s39a import S39A, SER39, VOL39, SKIN

WATERC = (60, 120, 190)
LASER = (240, 80, 80)
CAM = (90, 95, 110)
BALLC = (220, 230, 90)


# ---------------------------------------------------------------- E208 泳衣
def e208_drag(c, t, i):
    corner_tag(c, '第 208 集 · 水比空气难推得多')
    c.text(60, 96, '同样往前推：表面毛糙、有褶皱的瓶子，身后拖出一大团乱涡；光滑贴身的，水顺顺地滑过去', 'serif', 36, INK)
    for j, (lab, rough) in enumerate([('套着袜子：拉力大', True), ('光溜溜：拉力小', False)]):
        cy = 380 + j * 340
        c.rect(120, cy - 140, 1800, cy + 140, fill=mix(BG, WATERC, 0.35))
        bx = 900
        c.rect(bx - 160, cy - 50, bx + 160, cy + 50, fill=mix(BG, (200, 220, 235), 0.9), r=45)
        if rough:
            r = random.Random(1)
            for k in range(30):
                x = bx - 150 + r.uniform(0, 300)
                c.ellipse(x, cy - 52 + r.choice([0, 104]), 8, 6, fill=mix(BG, (230, 220, 200), 1.0))
        for k in range(9):
            y = cy - 120 + k * 30
            off = (t * 200 + k * 40) % 300
            for q in range(5):
                x0 = 1700 - off - q * 300
                if bx - 170 < x0 < bx + 170 and abs(y - cy) < 60:
                    continue
                c.line([(x0, y), (x0 - 50, y)], mix(BG, WATER_L, 0.7), 3)
        nwake = 14 if rough else 4
        for k in range(nwake):
            ang = t * 3 + k * 1.3
            rr = 20 + (k * 13) % 50
            wx = bx - 200 - (k * 37) % (220 if rough else 80)
            c.arc(wx, cy + math.sin(k) * 30, rr, rr, math.degrees(ang), math.degrees(ang) + 240, mix(BG, WATER_L, 0.9), 3)
        c.arrow(bx + 180, cy, bx + 380, cy, SPARK, 6, 18)
        c.text(bx + 400, cy, '拉', 'bold', 26, SPARK, 'lm')
        c.text(260, cy - 100, lab, 'bold', 26, NRED if rough else GREEN, 'lm')
    caps(c, t, [(0, 7, '水比空气重八百倍，在水里往前走，每一步都在推开一大片水'),
                (7.2, 14, '表面毛糙、有褶皱，水流被搅乱，身后拖出一串涡，阻力变大'),
                (14.2, 22, '紧身、光滑的泳衣和泳帽，让水顺着身体滑过去（示意）')], y=1010)


def e208_stream(c, t, i):
    corner_tag(c, 'E208 · 形状也要像鱼')
    c.text(60, 96, '同样大小的东西，平的一面朝前，水撞上去绕不过来；尖的、圆滑的一头朝前，水分开又合拢', 'serif', 36, INK)
    shapes = [('平板朝前', 1.0), ('圆头朝前', 0.45), ('流线形（像鱼）', 0.1)]
    for j, (lab, cd) in enumerate(shapes):
        cy = 330 + j * 230
        c.rect(120, cy - 90, 1300, cy + 90, fill=mix(BG, WATERC, 0.3))
        bx = 700
        if j == 0:
            c.rect(bx - 10, cy - 70, bx + 10, cy + 70, fill=INK)
        elif j == 1:
            c.ellipse(bx, cy, 70, 70, fill=INK)
        else:
            c.poly([(bx - 80, cy), (bx - 20, cy - 45), (bx + 120, cy - 10), (bx + 140, cy), (bx + 120, cy + 10), (bx - 20, cy + 45)], INK)
        for k in range(7):
            y = cy - 75 + k * 25
            off = (t * 220 + k * 30) % 200
            for q in range(6):
                x = 1250 - off - q * 200
                if (abs(x - bx) < 90 and abs(y - cy) < 70) or x < 170:
                    continue
                c.line([(x, y), (x - 40, y)], mix(BG, WATER_L, 0.8), 3)
        c.text(1340, cy - 20, lab, 'bold', 24, INK, 'lm')
        c.rect(1340, cy + 15, 1340 + cd * 440, cy + 45, fill=SPARK, r=6)
        c.text(1350 + cd * 440, cy + 30, '阻力（示意）', 'sans', 18, MUTED, 'lm')
    caps(c, t, [(0, 7, '同样大的横截面，形状不同，阻力能差好几倍'),
                (7.2, 14, '平的一面让水撞上去、在后面打转；流线形让水分开又平顺地合拢'),
                (14.2, 22, '游泳时身体伸直、手臂夹紧耳朵，就是把自己变成流线形（示意）')], y=1010)


# ---------------------------------------------------------------- E209 电子计时
def e209_reaction(c, t, i):
    corner_tag(c, '第 209 集 · 人手要零点二秒')
    c.text(60, 96, '眼睛看到 → 大脑判断 → 手指按下：这一路要零点一五到零点三秒，比百米冠军之间的差距大几十倍', 'serif', 36, INK)
    x0 = 200
    steps = [('眼睛看到', 0.03), ('传到大脑', 0.05), ('大脑判断', 0.07), ('传到手', 0.03), ('手指按下', 0.04)]
    tt = (t % 11) / 8
    acc = 0
    total = sum(d for _, d in steps)
    for k, (lab, d) in enumerate(steps):
        w = d / total * 1300
        on = tt * total > acc
        c.rect(x0, 380, x0 + w - 8, 480, fill=mix(BG, SPARK, 0.85) if on else SHEET, r=8)
        c.text(x0 + w / 2, 430, lab, 'bold', 22, INK, 'mm')
        c.text(x0 + w / 2, 510, f'约 {d:.2f} 秒', 'mono', 20, MUTED, 'mm')
        x0 += w
        acc += d
    c.text(200, 600, f'总共约 {total:.2f} 秒（因人而异，示意）', 'bold', 28, NRED, 'lm')
    c.rect(200, 680, 1700, 860, fill=SHEET, r=12)
    c.text(240, 720, '反应尺：', 'bold', 24, INK, 'lm')
    c.text(240, 780, '尺子掉了 d 厘米才被捏住 → 反应时间 ≈ √(2d ÷ 980) 秒', 'mono', 26, SPARK, 'lm')
    c.text(240, 830, '例如掉了 20 厘米 → 约 0.20 秒', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '裁判看到运动员冲线，再按下秒表，中间要过一段时间'),
                (7.2, 14, '这段反应时间大约零点二秒，而且每个人、每一次都不一样'),
                (14.2, 22, '百米决赛常常只差百分之一秒：人手根本按不准')], y=1010)


def e209_gate(c, t, i):
    corner_tag(c, 'E209 · 光线和电路替人按表')
    c.text(60, 96, '发令枪一响，电路同时启动计时器；终点一道光被身体挡住，计时器自己停下，不经过任何人的手', 'serif', 36, INK)
    gy = 760
    c.rect(100, gy, 1820, gy + 20, fill=mix(BG, (180, 90, 70), 0.8))
    sx, ex = 200, 1600
    c.rect(sx - 4, gy - 300, sx + 4, gy, fill=MUTED)
    c.text(sx, gy - 330, '起点：发令枪接计时器', 'sans', 20, MUTED, 'mm')
    c.rect(ex - 10, gy - 360, ex + 10, gy, fill=CAM)
    c.rect(ex + 120, gy - 360, ex + 140, gy, fill=CAM)
    T = 9
    ph = (t % T)
    run = max(0, ph - 1)
    x = sx + min(ex - sx + 60, run * 260)
    blocked = abs(x - ex - 60) < 50
    if not blocked:
        c.line([(ex + 10, gy - 200), (ex + 120, gy - 200)], LASER, 4)
    c.ellipse(x, gy - 260, 26, 26, fill=SKIN)
    c.line([(x, gy - 230), (x, gy - 100)], SKIN, 14)
    leg = math.sin(run * 10) * 40
    c.line([(x, gy - 100), (x + leg, gy)], SKIN, 10)
    c.line([(x, gy - 100), (x - leg, gy)], SKIN, 10)
    if ph > 0.9 and ph < 1.3:
        c.text(sx, gy - 400, '砰！', 'bold', 40, SPARK, 'mm')
    elapsed = min(run, (ex + 60 - sx) / 260)
    c.rect(700, 200, 1220, 320, fill=SHEET, r=12)
    c.text(960, 260, f'{elapsed * 1.43:.2f} 秒', 'mono', 48, GREEN if x >= ex + 60 else SPARK, 'mm')
    c.text(ex + 70, gy - 240, '光线', 'sans', 20, LASER, 'mm')
    caps(c, t, [(0, 7, '发令枪的扳机连着计时器：枪响的同一刻开始计时'),
                (7.2, 14, '终点线两边，一边发出一道光，一边接收；身体一挡住光，电路就停表'),
                (14.2, 22, '今天还会加上每秒拍几千张的终点相机，看清谁的躯干先过线（示意）')], y=1010)


# ---------------------------------------------------------------- E210 鹰眼
def e210_sight(c, t, i):
    corner_tag(c, '第 210 集 · 两条视线交在一起')
    c.text(60, 96, '一台相机只能说「球在这条线上的某处」；再加一台从别的方向看，两条线一交，球的位置就定了', 'serif', 36, INK)
    x0, y0, x1, y1 = 300, 220, 1500, 900
    c.rect(x0, y0, x1, y1, fill=mix(BG, (60, 120, 90), 0.5), r=8)
    c.line([(x0 + 100, y0 + 120), (x1 - 100, y0 + 120)], (240, 240, 240), 4)
    bx, by = 900 + 120 * math.sin(t * 0.4), y0 + 135 + 20 * math.cos(t * 0.6)
    c.ellipse(bx, by, 14, 14, fill=BALLC)
    cams = [(x0 - 120, y0 + 600), (x1 + 120, y0 + 650)]
    for k, (cx, cy) in enumerate(cams):
        a = fade(t, 2 + k * 5, 3 + k * 5)
        c.rect(cx - 40, cy - 30, cx + 40, cy + 30, fill=CAM, r=6)
        if a > 0:
            dx, dy = bx - cx, by - cy
            L = math.hypot(dx, dy)
            c.line([(cx, cy), (cx + dx / L * (L + 300), cy + dy / L * (L + 120))], mix(BG, SPARK, a), 3)
    if t > 13:
        c.arc(bx, by, 32, 32, 0, 360, NRED, 4)
        inside = by > y0 + 120
        c.rect(1560, 300, 1880, 460, fill=SHEET, r=12)
        c.text(1720, 350, '算出来', 'bold', 26, INK, 'mm')
        c.text(1720, 410, '压线：界内' if abs(by - (y0 + 120)) < 22 else ('界内' if inside else '出界'), 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '一台相机拍到球，只知道球在从相机出发的一条线上'),
                (7.2, 14, '换一个方向再放一台，它也画出一条线'),
                (14.2, 22, '两条线的交点就是球：这叫三角测量，卫星定位也靠类似的道理（示意）')], y=1010)


def e210_cams(c, t, i):
    corner_tag(c, 'E210 · 相机越多，算得越准')
    c.text(60, 96, '每台相机都有一点误差，画出来的不是细线而是一条带子；相机越多，带子交出来的那一小块就越小', 'serif', 36, INK)
    cx, cy = 760, 560
    n = 2 + min(6, int(t / 3))
    r = random.Random(3)
    for k in range(n):
        ang = k * math.pi / n + 0.3
        w = 46
        dx, dy = math.cos(ang), math.sin(ang)
        nx, ny = -dy, dx
        L = 300
        c.poly([(cx - dx * L + nx * w, cy - dy * L + ny * w), (cx + dx * L + nx * w, cy + dy * L + ny * w),
                (cx + dx * L - nx * w, cy + dy * L - ny * w), (cx - dx * L - nx * w, cy - dy * L - ny * w)], mix(BG, SPARK, 0.18))
        c.rect(cx - dx * (L + 40) - 22, cy - dy * (L + 40) - 16, cx - dx * (L + 40) + 22, cy - dy * (L + 40) + 16, fill=CAM, r=4)
    err = 46 / math.sqrt(n / 2)
    c.arc(cx, cy, err, err, 0, 360, NRED, 4)
    c.ellipse(cx, cy, 10, 10, fill=BALLC)
    c.rect(1380, 300, 1860, 560, fill=SHEET, r=12)
    c.text(1620, 350, '相机台数', 'bold', 26, INK, 'mm')
    c.text(1620, 420, f'{n} 台', 'mono', 44, SPARK, 'mm')
    c.text(1620, 500, f'误差约 {err / 10:.1f} 毫米（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '在纸上用尺子「瞄」弹珠，每个人瞄得都有一点偏'),
                (7.2, 14, '两个人瞄，交出一个小菱形；三个人、四个人，交出来的地方越来越小'),
                (14.2, 22, '网球场的鹰眼用十来台高速相机，误差只有几毫米（拍摄前核对）')], y=1010)


CLIPS = {
 'E208_阻力': (e208_drag, 22), 'E208_流线': (e208_stream, 22),
 'E208_片头': (titles.opening(SER39, VOL39, S39A, 6, '2008 年前后高科技泳衣引发争议'), 7),
 'E208_片尾': (titles.closing(SER39, VOL39, S39A, 6, '下集：差百分之一秒，比赛怎么分出胜负？'), 7),
 'E209_反应': (e209_reaction, 22), 'E209_光电门': (e209_gate, 22),
 'E209_片头': (titles.opening(SER39, VOL39, S39A, 7, '1912 年奥运会开始用半自动电子计时'), 7),
 'E209_片尾': (titles.closing(SER39, VOL39, S39A, 7, '下集：「鹰眼」怎么算出球压没压线？'), 7),
 'E210_视线': (e210_sight, 22), 'E210_多台': (e210_cams, 22),
 'E210_片头': (titles.opening(SER39, VOL39, S39A, 8, '21 世纪初网球比赛开始用鹰眼'), 7),
 'E210_片尾': (titles.closing(SER39, VOL39, S39A, 8, '下集：蹦床为什么能越跳越高？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
