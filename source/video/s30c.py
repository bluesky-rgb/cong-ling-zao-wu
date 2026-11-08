"""第三十季（古法解密 12.0：玩、响、用）第三批：B126 折扇、B127 谢公屐、B128 簧片锁 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO
from s30a import SB30, VOL30

PAPER = (235, 230, 215)
COIN = (210, 185, 90)
BRASS = (200, 165, 80)


# ---------------------------------------------------------------- B126 折扇
def b126_section(c, t, i):
    corner_tag(c, 'B126 · 褶子把纸「竖」了起来')
    c.text(60, 96, '从侧面切开看：平纸只有一张纸厚；折成褶，纸的一部分竖了起来，整块变「高」，弯它就难多了', 'serif', 38, INK)
    s = min(1, max(0, (t - 3) / 8))
    x0, x1, y = 260, 1660, 420
    amp = 50 * s
    n = 14
    pts = []
    for j in range(n * 2 + 1):
        x = x0 + (x1 - x0) * j / (n * 2)
        pts.append((x, y + (amp if j % 2 else -amp)))
    c.line(pts, PAPER, 4)
    c.text(960, 300, '截面（示意）', 'sans', 22, MUTED, 'mm')
    if s > 0.5:
        c.line([(x1 + 40, y - amp), (x1 + 40, y + amp)], SPARK, 2)
        c.text(x1 + 60, y, '高度', 'sans', 20, SPARK, 'lm')
    by = 760
    c.rect(300, by, 520, by + 120, fill=mix(BG, WOOD, 0.6), r=6)
    c.rect(1400, by, 1620, by + 120, fill=mix(BG, WOOD, 0.6), r=6)
    sag = 120 * (1 - s) + 6
    bpts = [(520 + 880 * j / 30, by - 4 + sag * math.sin(math.pi * j / 30)) for j in range(31)]
    c.line(bpts, PAPER, 6 + 10 * s)
    for k in range(5):
        c.ellipse(960 - 60 + k * 30, by - 14 + sag - k * 0, 14, 6, fill=COIN)
    c.text(960, by + 160, '同样 5 枚硬币：平纸塌下去，褶纸几乎不弯（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一张平纸从侧面看，只有薄薄一层：放几枚硬币，中间就塌了'),
                (7.2, 14, '把它来回折成褶，纸的一部分立了起来，整块的「高度」从零点一毫米变成了一厘米'),
                (14.2, 22, '弯一块东西有多难，跟它高度的三次方有关：高度大了一百倍，就硬了不知多少倍（示意）')], y=1010)


def b126_load(c, t, i):
    corner_tag(c, 'B126 · 一张纸，能放几枚硬币？')
    c.text(60, 96, '同样一张 A4 纸架在两摞书之间：平放、折 1 厘米宽的褶、折 2 厘米宽的褶，一枚一枚往上加硬币', 'serif', 38, INK)
    data = [('平纸', 2), ('1 厘米褶', 18), ('2 厘米褶', 30)]
    grow = min(1, t / 12)
    for k, (lab, n) in enumerate(data):
        x = 420 + k * 460
        m = int(n * grow)
        for j in range(m):
            c.ellipse(x, 840 - j * 14, 60, 12, fill=COIN, outline=mix(COIN, INK, 0.3), width=1)
        c.text(x, 900, lab, 'bold', 26, INK, 'mm')
        c.text(x, 820 - n * 14 * grow - 50, f'{m} 枚', 'mono', 26, SPARK, 'mm')
    c.text(1680, 500, '纸塌下前能放的硬币', 'bold', 22, INK, 'mm')
    c.text(1680, 540, '（数字为示意，以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '两摞书相距 15 厘米，一张 A4 纸平放架在上面：一两枚硬币就塌了'),
                (7.2, 14, '同样的纸折成 1 厘米宽的扇褶，能托住十几枚'),
                (14.2, 22, '褶子折得更宽更高，托得更多：折扇薄薄一张纸，扇起来不软塌，靠的就是这些褶（示意）')], y=1010)


# ---------------------------------------------------------------- B127 谢公屐
def _slope_scene(c, t, mode, title):
    ang = math.radians(15)
    x0, y0 = 300, 860
    L = 1300
    x1, y1 = x0 + L * math.cos(ang), y0 - L * math.sin(ang)
    c.poly([(x0, y0), (x1, y1), (x1, y0)], mix(BG, (110, 140, 90), 0.6))
    u = 0.45
    px, py = x0 + L * u * math.cos(ang), y0 - L * u * math.sin(ang)
    half = 120
    ux_, uy_ = px + half * math.cos(ang), py - half * math.sin(ang)
    dx_, dy_ = px - half * math.cos(ang), py + half * math.sin(ang)
    drop = (dy_ - uy_)
    td = 70
    tu = 70 - drop * min(1, max(0, (t - 6) / 4))
    top_u = (ux_, uy_ - tu)
    top_d = (dx_, dy_ - td)
    c.line([(ux_, uy_), top_u], WOOD, 12)
    c.line([(dx_, dy_), top_d], WOOD, 12)
    c.line([top_d, top_u], mix(WOOD, INK, 0.2), 22)
    tilt = math.degrees(math.atan2(top_d[1] - top_u[1], top_u[0] - top_d[0]))
    c.text(px, min(top_u[1], top_d[1]) - 60, f'鞋底倾角 {abs(tilt):.0f}°', 'mono', 26, GREEN if abs(tilt) < 2 else SPARK, 'mm')
    if mode == 'up':
        lab_u, lab_d = '前齿', '后齿'
        c.arrow(800, 480, 1100, 400, MUTED, 3, 14)
        c.text(950, 380, '上山方向', 'sans', 22, MUTED, 'mm')
    else:
        lab_u, lab_d = '后齿', '前齿'
        c.arrow(1100, 400, 800, 480, MUTED, 3, 14)
        c.text(950, 380, '下山方向', 'sans', 22, MUTED, 'mm')
    c.text(ux_, uy_ + 40, lab_u, 'sans', 20, MUTED, 'mm')
    c.text(dx_, dy_ + 40, lab_d, 'sans', 20, MUTED, 'mm')
    c.text(1700, 300, title, 'bold', 28, INK, 'mm')


def b127_up(c, t, i):
    corner_tag(c, 'B127 · 上山拆前齿')
    c.text(60, 96, '15° 的坡上，前后齿一样长，鞋底就跟着坡往后倒；上山时拆掉前齿，前面低下来，鞋底就平了', 'serif', 38, INK)
    _slope_scene(c, t, 'up', '上山')
    caps(c, t, [(0, 7, '木屐底下有前后两道齿：在平地上，鞋底是平的'),
                (7.2, 14, '一上坡，前后齿一样长，鞋底就跟着坡倾斜，脚后跟往下坠，小腿一直绷着'),
                (14.2, 22, '把前齿拆掉，前面落低了，鞋底又差不多水平：脚踩得稳，走得也省力（示意）')], y=1010)


def b127_down(c, t, i):
    corner_tag(c, 'B127 · 下山拆后齿')
    c.text(60, 96, '下山正好反过来：脚尖朝下坡，鞋底往前栽；拆掉后齿，后面落低，鞋底又平了，身子就不容易往前扑', 'serif', 38, INK)
    _slope_scene(c, t, 'down', '下山')
    caps(c, t, [(0, 7, '下山时脚尖朝着坡下，前后齿一样长的话，鞋底往前栽'),
                (7.2, 14, '人的重心就容易往前冲，一不小心就扑倒'),
                (14.2, 22, '把后齿拆掉，后面落低，鞋底又平了：这就是谢灵运「上山则去前齿，下山去其后齿」的道理（示意）')], y=1010)


# ---------------------------------------------------------------- B128 簧片锁
def _lock(c, t, insert, spread, kx):
    cx0, cx1, cy = 700, 1300, 520
    c.rect(cx0, cy - 90, cx1, cy + 90, outline=BRASS, width=8, r=12)
    c.rect(cx0 - 6, cy - 30, cx0 + 6, cy + 30, fill=BG)
    c.rect(cx1 - 6, cy - 48, cx1 + 6, cy + 48, fill=BG)
    c.text((cx0 + cx1) / 2, cy - 130, '锁壳（左边插锁芯，右边是钥匙孔）', 'sans', 22, MUTED, 'mm')
    tip = cx0 + 60 + 420 * insert
    shaft0 = tip - 600
    c.rect(shaft0, cy - 10, tip, cy + 10, fill=mix(BRASS, INK, 0.2), r=4)
    sp = 60 * spread
    for s_ in (1, -1):
        c.line([(tip, cy), (tip - 140, cy + s_ * (12 + sp))], STEELC, 6)
    if kx is not None:
        c.rect(kx, cy - 40, kx + 360, cy - 16, fill=GREEN, r=4)
        c.rect(kx, cy + 16, kx + 360, cy + 40, fill=GREEN, r=4)
        c.text(kx + 180, cy + 140, '钥匙（空心管）', 'sans', 20, GREEN, 'mm')
    return tip


STEELC = (190, 195, 205)


def b128_barb(c, t, i):
    corner_tag(c, 'B128 · 一插进去，弹片就张开卡住')
    c.text(60, 96, '锁芯头上有几片向外张开的弹簧片：往里插时被小口压拢，一进到锁壳里面就弹开，往回拉就被口卡住', 'serif', 38, INK)
    if t < 8:
        ins = t / 8
        sp = 0.1 if ins < 0.12 else (0.1 + 0.9 * min(1, (ins - 0.12) / 0.1))
    else:
        ins = 1 - 0.12 * min(1, (t - 8) / 3) + 0.02 * math.sin(t * 9) * (t > 11)
        sp = 1
    ins = max(ins, 0.12) if t >= 8 else ins
    _lock(c, t, ins, sp, None)
    if t >= 11:
        c.text(1000, 760, '拉不出来！张开的弹片顶在口上', 'bold', 30, NRED, 'mm')
    caps(c, t, [(0, 7, '老式簧片锁：锁芯头上装着几片弹簧钢片，自然状态是向外张开的'),
                (7.2, 14, '往锁壳里推的时候，小口把弹片压拢；一过小口，弹片「啪」地张开'),
                (14.2, 22, '这时候往回拉，张开的弹片正好顶在小口内侧：再使劲也拔不出来（示意）')], y=1010)


def b128_key(c, t, i):
    corner_tag(c, 'B128 · 钥匙把弹片压拢，就拔出来了')
    c.text(60, 96, '钥匙从另一头的钥匙孔伸进去，它的口子正好套住弹片、把它们挤拢；弹片一收，锁芯就顺顺当当地拉出来了', 'serif', 38, INK)
    k = min(1, t / 6)
    sp = 1 - min(1, max(0, (t - 5) / 4))
    out = min(1, max(0, (t - 10) / 6))
    kx = 1360 + (760 + 420 - 150 - 1360) * k
    _lock(c, t, 1 - out * 1.5, sp, kx)
    lab = '钥匙伸进去' if t < 6 else ('弹片被压拢' if t < 10 else '拔出来了')
    c.text(1000, 760, lab, 'bold', 30, GREEN if t >= 10 else INK, 'mm')
    caps(c, t, [(0, 7, '钥匙是一根空心的管子，口径正好比张开的弹片小一点'),
                (7.2, 14, '它套到弹片上，把每一片都挤拢：张开的倒刺没了'),
                (14.2, 22, '这时候一拉，锁芯就出来了：钥匙的形状要正好压住每一片，随便一根棍子不行（示意）')], y=1010)


CLIPS = {
 'B126_截面': (b126_section, 22), 'B126_承重': (b126_load, 22),
 'B126_片头': (titles.opening(BSER, VOL30, SB30, 6, '北宋时折扇传入'), 7),
 'B126_片尾': (titles.closing(BSER, VOL30, SB30, 6, '下集：上山拆前齿、下山拆后齿，这双木屐为什么走坡更稳？'), 7),
 'B127_上山': (b127_up, 22), 'B127_下山': (b127_down, 22),
 'B127_片头': (titles.opening(BSER, VOL30, SB30, 7, '南朝谢灵运的登山木屐'), 7),
 'B127_片尾': (titles.closing(BSER, VOL30, SB30, 7, '下集：老式铜锁钥匙一插就开，硬拔为什么拔不出来？'), 7),
 'B128_倒刺': (b128_barb, 22), 'B128_钥匙': (b128_key, 22),
 'B128_片头': (titles.opening(BSER, VOL30, SB30, 8, '汉代已有簧片锁'), 7),
 'B128_片尾': (titles.closing(BSER, VOL30, SB30, 8, '下集：印章上的字为什么要刻成反的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
