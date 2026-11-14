"""第四十九季（第二十一层：浴室）第三批：E258 水龙头、E259 指甲刀、E260 吹风机 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s49a import S49A, SER49, VOL49, WATER, STEEL

RUBBER = (60, 60, 60)
CERAMIC = (235, 235, 225)
COLD = (90, 150, 230)
HOT = (230, 90, 70)
WIRE = (240, 120, 60)


# ---------------------------------------------------------------- E258 水龙头
def e258_washer(c, t, i):
    corner_tag(c, '第 258 集 · 老式水龙头：螺杆压橡胶垫')
    c.text(60, 96, '老式水龙头里是一根螺杆：拧把手，螺杆一圈圈往下走，把一块橡胶垫压在出水口上，水就关住了', 'serif', 36, INK)
    u = 0.5 + 0.5 * math.cos(t * 0.6)
    cx, by = 760, 760
    c.rect(300, by, 1220, by + 90, fill=mix(BG, STEEL, 0.6))
    c.rect(cx - 40, by, cx + 40, by + 90, fill=BG)
    c.rect(cx - 40, by + 40, cx + 40, by + 90, fill=mix(BG, WATER, 0.7) if u > 0.1 else BG)
    gap = 120 * u
    c.rect(cx - 70, by - 30 - gap, cx + 70, by - gap, fill=mix(BG, RUBBER, 1.0), r=6)
    top = by - 30 - gap
    c.rect(cx - 22, top - 420, cx + 22, top, fill=mix(BG, STEEL, 1.0))
    for k in range(14):
        y = top - 400 + k * 28
        c.line([(cx - 22, y), (cx + 22, y + 12)], mix(BG, INK, 0.5), 3)
    c.rect(cx - 160, top - 450, cx + 160, top - 420, fill=mix(BG, STEEL, 0.9), r=8)
    if u > 0.1:
        for k in range(10):
            f = ((t * 1.5) + k / 10) % 1
            c.ellipse(cx + 200 + f * 300, by - 40 + 20 * math.sin(f * 6), 8, 8, fill=mix(BG, WATER, 1.0))
        c.text(1500, 500, '螺杆提上去：水流过', 'bold', 28, GREEN, 'mm')
    else:
        c.text(1500, 500, '橡胶垫压紧：水关住', 'bold', 28, NRED, 'mm')
    c.text(cx + 100, by - 15 - gap, '橡胶垫', 'bold', 22, INK, 'lm')
    caps(c, t, [(0, 7, '拧开：螺杆往上走，橡胶垫离开出水口，水就流过去'),
                (7.2, 14, '拧紧：螺杆往下走，橡胶垫压住出水口'),
                (14.2, 22, '要拧好几圈才全开全关；垫子磨坏了就会滴水（示意，家里水龙头只看不拆）')], y=1010)


def e258_disc(c, t, i):
    corner_tag(c, '第 258 集 · 新式水龙头：两片带孔的瓷片')
    c.text(60, 96, '单把手水龙头里是两片磨得很平的陶瓷片：下片有冷、热两个孔，上片有一个孔；转上片，对上哪个孔多就出哪种水', 'serif', 36, INK)
    cx, cy = 700, 560
    c.ellipse(cx, cy, 300, 300, fill=mix(BG, CERAMIC, 0.75))
    if t < 7:
        rot = -230 + 80 * min(1.0, t / 5)
    elif t < 14:
        rot = -150 + 30 * min(1.0, (t - 7) / 4)
    else:
        rot = -120 + 120 * min(1.0, (t - 14) / 6)
    def cell(a, col):
        a0 = math.radians(a); a1 = math.radians(a + 3)
        c.poly([(cx + 90 * math.cos(a0), cy + 90 * math.sin(a0)), (cx + 260 * math.cos(a0), cy + 260 * math.sin(a0)),
                (cx + 260 * math.cos(a1), cy + 260 * math.sin(a1)), (cx + 90 * math.cos(a1), cy + 90 * math.sin(a1))], col)
    for a in range(-180, 180, 3):
        inwin = 0 <= (a - rot) % 360 < 60
        if -150 <= a < -90:
            cell(a, mix(BG, COLD, 1.0 if inwin else 0.35))
        elif -90 <= a < -30:
            cell(a, mix(BG, HOT, 1.0 if inwin else 0.35))
        elif inwin:
            cell(a, mix(BG, CERAMIC, 0.4))
    for a in (rot, rot + 60):
        r = math.radians(a)
        c.line([(cx + 80 * math.cos(r), cy + 80 * math.sin(r)), (cx + 270 * math.cos(r), cy + 270 * math.sin(r))], INK, 5)
    pts = [(cx + 270 * math.cos(math.radians(a)), cy + 270 * math.sin(math.radians(a))) for a in range(int(rot), int(rot) + 61, 3)]
    seg(c, pts, INK, 5)
    c.text(cx, cy + 340, '亮的颜色：上片的孔和下片的孔对上了', 'sans', 22, MUTED, 'mm')
    def ov(a0, a1):
        lo, hi = max(a0, rot), min(a1, rot + 60)
        return max(0.0, hi - lo) / 60
    cold, hot = ov(-150, -90), ov(-90, -30)
    c.text(1420, 420, f'冷水孔对上：{int(cold * 100)}%', 'bold', 32, COLD, 'mm')
    c.text(1420, 490, f'热水孔对上：{int(hot * 100)}%', 'bold', 32, HOT, 'mm')
    msg = '关' if cold + hot < 0.05 else ('偏凉' if cold > hot * 1.5 else ('偏热' if hot > cold * 1.5 else '温'))
    c.text(1420, 600, f'出水：{msg}', 'bold', 40, INK, 'mm')
    caps(c, t, [(0, 7, '白线框住的是上片的孔，转到哪里，哪里的水就能流过去'),
                (7.2, 14, '只对上冷孔：凉水；两个孔各对上一半：温水'),
                (14.2, 22, '全部错开就关水；瓷片磨得很平，不用橡胶垫也不漏（示意）')], y=1010)


# ---------------------------------------------------------------- E259 指甲刀
def e259_levers(c, t, i):
    corner_tag(c, '第 259 集 · 省力杠杆加费力杠杆')
    c.text(60, 96, '压杆是省力杠杆，把手指的力放大很多倍；刀臂是费力杠杆，刀口比压点离支点稍远，力小一点', 'serif', 36, INK)
    ph = 0.5 - 0.5 * math.cos(min(1.0, (t % 11) / 6) * math.pi)
    x0, y0 = 300, 700
    L = 1200
    c.line([(x0, y0 + 40), (x0 + L, y0 + 40)], mix(BG, STEEL, 1.0), 22)
    a2 = -0.05 * (1 - ph)
    ex, ey = x0 + L * math.cos(a2), y0 + L * math.sin(a2)
    c.line([(x0, y0), (ex, ey)], mix(BG, STEEL, 0.9), 22)
    c.ellipse(x0, y0 + 20, 18, 18, fill=GREEN)
    c.text(x0, y0 + 100, '刀臂的支点（尾端）', 'bold', 22, GREEN, 'mm')
    c.text(ex, y0 + 100, '刀口', 'bold', 24, NRED, 'mm')
    pinx = x0 + 0.88 * L
    piny = y0 + (pinx - x0) * math.sin(a2)
    c.rect(pinx - 8, piny - 70, pinx + 8, y0 + 50, fill=mix(BG, STEEL, 0.6))
    c.ellipse(pinx, piny - 70, 14, 14, fill=SPARK)
    c.text(pinx + 20, piny - 100, '压杆的支点（销钉头）', 'bold', 22, SPARK, 'lm')
    pa = 0.30 * (1 - ph) + 0.02
    hx, hy = pinx - 1000 * math.cos(pa), piny - 70 - 1000 * math.sin(pa)
    c.line([(pinx + 30, piny - 60), (hx, hy)], mix(BG, (200, 205, 215), 1.0), 20)
    c.arrow(hx + 40, hy - 140, hx + 40, hy - 40, SPARK, 6, 16)
    c.text(hx + 40, hy - 170, '手指按这里', 'bold', 24, SPARK, 'mm')
    c.arrow(pinx - 30, piny - 40, pinx - 30, piny - 6, NRED, 4, 10)
    caps(c, t, [(0, 7, '手指按压杆远远的一头，压杆绕着销钉头转，把力放大很多倍'),
                (7.2, 14, '压杆在销钉旁压住刀臂；刀臂绕尾端转，刀口只比压点远一点，力小一点点'),
                (14.2, 22, '合起来，刀口上的力仍是手指的好几倍（示意，以实测为准）')], y=1010)


def e259_ratio(c, t, i):
    corner_tag(c, '第 259 集 · 倍数乘起来')
    c.text(60, 96, '压杆放大约 10 倍，刀臂再乘约 0.9（变小一点）：10 × 0.9 ≈ 9，手指按 1 份力，刀口上大约有 9 份力', 'serif', 36, INK)
    k = min(3, int(t / 5))
    bars = [('手指', 1, SPARK), ('压杆放大后', 10, INK), ('刀臂之后（刀口）', 9, NRED)]
    for j, (lab, v, col) in enumerate(bars):
        if j > k:
            break
        y = 340 + j * 160
        c.text(500, y + 30, lab, 'bold', 28, col, 'rm')
        c.rect(540, y, 540 + 100 * v, y + 60, fill=col, r=8)
        c.text(560 + 100 * v, y + 30, f'{v} 份', 'bold', 30, col, 'lm')
    if t > 15:
        c.text(960, 860, '× 10  × 0.9 ≈ × 9（示意，量自己的指甲刀算倍数）', 'bold', 32, GREEN, 'mm')
    caps(c, t, [(0, 7, '量压杆：手指到销钉头的距离，大约是压点到销钉头的 10 倍（示意）'),
                (7.2, 14, '量刀臂：压点到尾端的距离，比刀口到尾端稍短，力乘约 0.9'),
                (14.2, 22, '两个倍数相乘就是总倍数：靠的主要是那根长长的压杆')], y=1010)


# ---------------------------------------------------------------- E260 吹风机
def e260_heat(c, t, i):
    corner_tag(c, '第 260 集 · 风扇吹风，电热丝加热')
    c.text(60, 96, '吹风机里有两样主要的东西：电动机带着风扇把空气吸进来，前面一圈电热丝通电发热，把空气加热吹出去', 'serif', 36, INK)
    x0, x1, cy = 300, 1500, 540
    c.rect(x0, cy - 150, x1, cy + 150, outline=mix(BG, INK, 0.6), width=5, r=40)
    c.rect(700, cy + 150, 860, cy + 450, outline=mix(BG, INK, 0.6), width=5, r=20)
    fx = 480
    for k in range(4):
        a = t * 10 + k * math.pi / 2
        c.line([(fx, cy), (fx + 30 * math.cos(a), cy + 110 * math.sin(a))], mix(BG, STEEL, 1.0), 14)
    c.ellipse(fx, cy, 20, 20, fill=mix(BG, STEEL, 0.8))
    c.text(fx, cy + 200, '电动机＋风扇', 'bold', 24, INK, 'mm')
    hot = t > 7
    for k in range(10):
        x = 900 + k * 40
        pts = [(x + 20 * math.sin(m * 0.8), cy - 110 + m * 22) for m in range(11)]
        seg(c, pts, WIRE if hot else mix(BG, STEEL, 0.6), 4)
    c.text(1080, cy + 200, '电热丝' + ('（通电发热）' if hot else '（冷风档：不通电）'), 'bold', 24, WIRE if hot else MUTED, 'mm')
    for k in range(10):
        f = ((t * 0.8) + k / 10) % 1
        x = 180 + f * 1600
        col = WIRE if (hot and x > 1300) else mix(BG, (200, 210, 230), 1.0)
        c.ellipse(x, cy - 80 + (k % 4) * 50, 8, 8, fill=col)
    caps(c, t, [(0, 7, '冷风档：只有风扇转，空气从后面吸进来、从前面吹出去'),
                (7.2, 14, '热风档：电热丝通电，像 60 集电灯的灯丝一样发热，把流过的空气加热'),
                (14.2, 22, '吹风机只由大人操作，远离水；出风口别对着脸（示意）')], y=1010)


def e260_away(c, t, i):
    corner_tag(c, '第 260 集 · 热和风各帮一半')
    c.text(60, 96, '热让水分子跑得更快、更容易蒸发；风把湿布旁边那层潮湿的空气吹走、换上干空气，水汽才能不停地跑出来', 'serif', 36, INK)
    tt = min(t, 20)
    rows = [('自然晾干', 0.15, MUTED), ('冷风档', 0.5, SPARK), ('热风档', 0.85, NRED)]
    for j, (lab, rate, col) in enumerate(rows):
        y = 320 + j * 190
        rem = max(0.0, 1 - rate * tt / 20)
        c.text(380, y + 40, lab, 'bold', 30, col, 'rm')
        c.rect(420, y, 420 + 900, y + 80, fill=SHEET, r=10)
        c.rect(420, y, 420 + 900 * rem, y + 80, fill=mix(BG, WATER, 0.8), r=10)
        c.text(1350, y + 40, f'剩下的水 {int(rem * 100)}%', 'bold', 26, INK, 'lm')
    c.text(960, 900, f'{int(tt / 20 * 3 * 10) / 10} 分钟（示意，以实测为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '三块一样湿的布：一块自然晾，一块冷风吹，一块热风吹'),
                (7.2, 14, '只有风，也比自然晾快很多：潮湿的空气被吹走了'),
                (14.2, 22, '又热又有风，干得最快：热和风各帮了一半')], y=1010)


CLIPS = {
 'E258_垫片': (e258_washer, 22), 'E258_瓷片': (e258_disc, 22),
 'E258_片头': (titles.opening(SER49, VOL49, S49A, 6, '20 世纪 60 年代出现陶瓷阀芯水龙头'), 7),
 'E258_片尾': (titles.closing(SER49, VOL49, S49A, 6, '下集：小小指甲刀，怎么剪得动硬指甲？'), 7),
 'E259_两杠杆': (e259_levers, 22), 'E259_倍数': (e259_ratio, 22),
 'E259_片头': (titles.opening(SER49, VOL49, S49A, 7, '20 世纪初美国出现杠杆式指甲刀'), 7),
 'E259_片尾': (titles.closing(SER49, VOL49, S49A, 7, '下集：吹风机为什么吹得那么快？'), 7),
 'E260_加热': (e260_heat, 22), 'E260_吹走': (e260_away, 22),
 'E260_片头': (titles.opening(SER49, VOL49, S49A, 8, '20 世纪 20 年代出现手持电吹风'), 7),
 'E260_片尾': (titles.closing(SER49, VOL49, S49A, 8, '下集：电动牙刷是怎么抖起来的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
