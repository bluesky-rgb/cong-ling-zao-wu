"""第四十五季（第十九层：玩具箱）第三批：E238 遥控车、E239 磁力片、E240 回力车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s45a import S45A, SER45, VOL45

CAR = (220, 70, 60)
RADIO = (120, 180, 240)
TILE = (120, 200, 160)
MAGN = (210, 70, 70)
MAGS = (70, 110, 210)
SPRINGC = (170, 175, 185)


def _car(c, x, y, col, wheel_rot=0.0, s=1.0):
    c.rect(x - 110 * s, y - 50 * s, x + 110 * s, y + 10 * s, fill=mix(BG, col, 1.0), r=int(14 * s))
    c.rect(x - 50 * s, y - 90 * s, x + 50 * s, y - 50 * s, fill=mix(BG, col, 0.8), r=int(10 * s))
    for wx in (x - 70 * s, x + 70 * s):
        c.ellipse(wx, y + 14 * s, 30 * s, 30 * s, fill=mix(BG, (40, 40, 45), 1.0))
        c.line([(wx, y + 14 * s), (wx + 24 * s * math.cos(wheel_rot), y + 14 * s + 24 * s * math.sin(wheel_rot))], MUTED, 3)


# ---------------------------------------------------------------- E238 遥控车
def e238_code(c, t, i):
    corner_tag(c, '第 238 集 · 按键变成编了码的无线电')
    c.text(60, 96, '按下「前进」，遥控器把它编成一串码，从天线发出无线电波；车上的接收器认出这串码，电动机就往前转', 'serif', 36, INK)
    rx, ry = 340, 700
    c.rect(rx - 90, ry - 160, rx + 90, ry + 160, fill=mix(BG, (60, 62, 70), 1.0), r=20)
    c.line([(rx + 50, ry - 160), (rx + 50, ry - 300)], MUTED, 5)
    key = int(t / 5.5) % 4
    names = ['前进', '后退', '左转', '右转']
    codes = ['1 0 1 1', '1 0 0 1', '1 1 0 1', '1 1 1 0']
    for k, nm in enumerate(names):
        bx, by = rx - 40 + (k % 2) * 80, ry - 60 + (k // 2) * 90
        on = k == key and (t % 5.5) < 1.5
        c.ellipse(bx, by, 32, 32, fill=mix(BG, SPARK if on else (110, 110, 120), 1.0))
        c.text(bx, by + 50, nm, 'sans', 16, MUTED, 'mm')
    for k in range(6):
        r = ((t * 200 + k * 70) % 380)
        c.arc(rx + 50, ry - 300, 30 + r, 30 + r, -25, 25, mix(BG, RADIO, max(0.0, 1 - r / 380)), 4)
    c.text(960, 300, f'「{names[key]}」→ 码 {codes[key]}（示意）', 'bold', 30, SPARK, 'mm')
    cx = 1520 + (60 if key == 0 else -60 if key == 1 else 0) * math.sin(t % 5.5 / 5.5 * math.pi)
    _car(c, cx, 620, CAR, t * (4 if key < 2 else 2))
    c.line([(cx + 80, 530), (cx + 80, 440)], MUTED, 3)
    c.text(1520, 760, '接收器解码 → 电动机转', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '每个按键对应一串不同的码，遥控器把它调制到无线电波上发出去'),
                (7.2, 14, '车上的天线和接收器一直在「听」，认出码就告诉电动机该怎么转'),
                (14.2, 22, '不同的车用不同的频率或配对码，两辆车同时开也不会听错（示意）')], y=1010)


def e238_shield(c, t, i):
    corner_tag(c, '第 238 集 · 纸挡不住，金属盒挡得住')
    c.text(60, 96, '无线电波能穿过塑料袋、纸盒和薄墙；把遥控器关进盖好的金属饼干盒里，电波被金属挡住，车就收不到了', 'serif', 36, INK)
    for k, (lab, ok, col) in enumerate([('塑料袋：车照样跑', True, (220, 220, 230)), ('纸盒：车照样跑', True, (200, 170, 120)), ('金属盒：车不动了', False, (170, 175, 185))]):
        ox = 340 + k * 620
        oy = 460
        c.rect(ox - 110, oy - 90, ox + 110, oy + 90, fill=mix(BG, col, 0.85 if k < 2 else 1.0), r=10)
        c.rect(ox - 40, oy - 60, ox + 40, oy + 60, fill=mix(BG, (60, 62, 70), 0.8), r=8)
        for m in range(4):
            r = ((t * 200 + m * 90) % 360)
            reach = r if ok else min(r, 100)
            a = max(0.0, 1 - r / 360)
            if ok or r < 100:
                c.arc(ox, oy, 60 + reach, 60 + reach, 40, 140, mix(BG, RADIO, a), 4)
        _car(c, ox + (40 * math.sin(t * 2) if ok else 0), 800, CAR, t * 4 if ok else 0, 0.8)
        c.text(ox, 900, lab, 'bold', 24, GREEN if ok else NRED, 'mm')
    caps(c, t, [(0, 7, '站在 3 米外，把遥控器装进塑料袋按前进：车照跑'),
                (7.2, 14, '装进纸盒，还是照跑；装进盖好的金属饼干盒，车一下就不动了'),
                (14.2, 22, '金属把电波挡在外面，这叫屏蔽；电视遥控器用的是红外光，一本书就能挡住（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E239 磁力片
def _rod(c, x, y, ang, L=60):
    dx, dy = L / 2 * math.cos(ang), L / 2 * math.sin(ang)
    c.line([(x - dx, y - dy), (x, y)], MAGS, 16)
    c.line([(x, y), (x + dx, y + dy)], MAGN, 16)


def e239_rotate(c, t, i):
    corner_tag(c, '第 239 集 · 小磁铁会自己转过来')
    c.text(60, 96, '磁力片的边里藏着能在小格子里打滚的圆柱磁铁：两片一靠近，磁铁自己转成红对蓝，所以怎么拼都相吸', 'serif', 36, INK)
    p = min(1.0, t / 8)
    gap = 300 * (1 - p) + 6
    lx = 960 - gap / 2 - 150
    rx = 960 + gap / 2 + 150
    for x, flip in ((lx, False), (rx, True)):
        c.rect(x - 150, 300, x + 150, 760, fill=mix(BG, TILE, 0.55), r=16)
    for k in range(3):
        y = 380 + k * 150
        c.rect(lx + 60, y - 50, lx + 146, y + 50, outline=mix(BG, MUTED, 0.6), width=3, r=8)
        c.rect(rx - 146, y - 50, rx - 60, y + 50, outline=mix(BG, MUTED, 0.6), width=3, r=8)
        a_l = math.radians(0)
        a_r0 = math.radians(0)
        a_r = math.pi * (1 - min(1.0, max(0.0, (p - 0.5) / 0.4)))
        _rod(c, lx + 103, y, 0.0, 70)
        _rod(c, rx - 103, y, a_r, 70)
    if p > 0.95:
        c.text(960, 820, '红（N）对蓝（S）：吸上了', 'bold', 28, GREEN, 'mm')
    else:
        c.text(960, 820, '靠近中：右边的小磁铁在格子里翻身', 'sans', 26, MUTED, 'mm')
    caps(c, t, [(0, 7, '普通磁铁同极相对就推开；磁力片里的圆柱磁铁不是粘死的，能在格子里转'),
                (7.2, 14, '两片一靠近，磁力让小磁铁翻个身，变成异极相对，有时还能听到「咔哒」一声'),
                (14.2, 22, '所以正着拼、翻过来拼都能吸上；千万别拆，里面的小磁铁吞下去很危险（示意）')], y=1010)


def e239_compass(c, t, i):
    corner_tag(c, '第 239 集 · 指南针看见看不见的磁极')
    c.text(60, 96, '磁力片的边慢慢经过指南针：指针先被一头吸过去，到磁铁中间时一下翻转，说明里面藏着有两极的小磁铁', 'serif', 36, INK)
    tx = 260 + (t / 22) * 1400
    c.rect(tx - 200, 260, tx + 200, 420, fill=mix(BG, TILE, 0.55), r=14)
    _rod(c, tx, 400, 0.0, 90)
    cx, cy = 960, 640
    c.ellipse(cx, cy, 130, 130, fill=mix(BG, (235, 235, 225), 0.9))
    c.ellipse(cx, cy, 130, 130, outline=MUTED, width=4)
    dx = tx - cx
    nx, ny = (tx + 45) - cx, 400 - cy
    sx, sy = (tx - 45) - cx, 400 - cy
    dn = math.hypot(nx, ny) ** 3 + 1e-6
    ds = math.hypot(sx, sy) ** 3 + 1e-6
    fx = -nx / dn * 1e6 + sx / ds * 1e6 * 1.0
    fy = -ny / dn * 1e6 + sy / ds * 1e6 * 1.0
    fx += 0.0
    fy -= 0.6
    ang = math.atan2(fy, fx)
    L = 110
    c.line([(cx, cy), (cx + L * math.cos(ang), cy + L * math.sin(ang))], NRED, 12)
    c.line([(cx, cy), (cx - L * math.cos(ang), cy - L * math.sin(ang))], mix(BG, MAGS, 1.0), 12)
    c.ellipse(cx, cy, 12, 12, fill=INK)
    c.text(cx, cy + 190, '指针红头被 S 极吸、被 N 极推（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '磁铁藏在塑料里看不见，指南针能替我们「看」'),
                (7.2, 14, '边慢慢经过，指针先跟着一头转，到中间时一下翻过来'),
                (14.2, 22, '一个小磁铁就有 N、S 两极：磁铁远离手机、银行卡、心脏起搏器（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E240 回力车
def e240_wind(c, t, i):
    corner_tag(c, '第 240 集 · 往后拉，卷紧发条')
    c.text(60, 96, '往后拉时，轮子通过齿轮把车里的发条卷紧，存下弹性势能；一松手，发条松开，经齿轮让轮子飞快地转', 'serif', 36, INK)
    T = 10.0
    ph = (t % T) / T
    if ph < 0.4:
        x = 900 - 300 * (ph / 0.4)
        wind = ph / 0.4
        lab = '往后拉：发条卷紧'
    elif ph < 0.5:
        x = 600
        wind = 1.0
        lab = '松手'
    else:
        u = (ph - 0.5) / 0.5
        x = 600 + 1100 * (1 - (1 - u) ** 2)
        wind = max(0.0, 1 - u * 1.4)
        lab = '冲出去：发条松开'
    gy = 760
    c.rect(100, gy + 50, 1820, gy + 60, fill=mix(BG, MUTED, 0.5))
    _car(c, x, gy, CAR, -x / 30)
    cx, cy = 480, 420
    turns = 2 + 4 * wind
    pts = []
    for k in range(300):
        u = k / 299
        a = u * turns * 2 * math.pi
        r = 20 + 120 * u * (0.6 + 0.4 * (1 - wind))
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    c.line(pts, SPRINGC, 4)
    c.text(cx, cy + 180, '车里的发条（放大）', 'sans', 22, MUTED, 'mm')
    bx = 1600
    c.rect(bx, 230, bx + 60, 560, fill=SHEET, r=8)
    c.rect(bx, 560 - 330 * wind, bx + 60, 560, fill=SPARK, r=8)
    c.text(bx + 30, 600, '存的能量', 'sans', 20, MUTED, 'mm')
    c.text(960, 300, lab, 'bold', 30, SPARK, 'mm')
    caps(c, t, [(0, 7, '回力车没有电池：车肚子里是一圈卷簧和一组小齿轮'),
                (7.2, 14, '往后拉，轮子带着齿轮把卷簧卷紧，能量存在弯紧的钢片里'),
                (14.2, 22, '一松手，卷簧松开，通过齿轮让后轮飞快地转，车就冲了出去（示意）')], y=1010)


def e240_distance(c, t, i):
    corner_tag(c, '第 240 集 · 拉得越多跑得越远，但有上限')
    c.text(60, 96, '拉得越长，发条卷得越紧，存的能量越多，车跑得越远；可发条卷满后再拉就打滑，跑的距离不再增加', 'serif', 36, INK)
    x0, y0, W, H = 300, 260, 1300, 560
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 40, '往后拉的距离（厘米）', 'sans', 22, MUTED, 'mm')
    c.text(x0 + 20, y0 + 30, '跑出去的距离（示意）', 'sans', 22, MUTED, 'lm')
    p = min(1.0, t / 12)
    pts = []
    for m in range(101):
        u = m / 100
        if u > p:
            break
        d = min(1.0, u / 0.6) if u < 0.6 else 1.0
        d = d * (1 - 0.0)
        pts.append((x0 + 60 + u * (W - 120), y0 + H - 50 - d * (H - 140)))
    if len(pts) > 1:
        c.line(pts, GREEN, 5)
    for k, v in enumerate([5, 10, 20, 30]):
        x = x0 + 60 + v / 30 * (W - 120)
        c.text(x, y0 + H - 15, str(v), 'mono', 18, MUTED, 'mm')
    if p > 0.65:
        c.text(x0 + 0.8 * W, y0 + 120, '发条卷满，开始打滑', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '往后拉 5 厘米、10 厘米、20 厘米，各量车跑出去多远'),
                (7.2, 14, '一开始拉得越多跑得越远；拉到一定长度，再往后拉就「咔咔」打滑'),
                (14.2, 22, '在地毯上跑得近：摩擦把能量吃掉了。别拉太猛，会伤齿轮（以实测为准）')], y=1010)


CLIPS = {
 'E238_编码': (e238_code, 22), 'E238_屏蔽': (e238_shield, 22),
 'E238_片头': (titles.opening(SER45, VOL45, S45A, 6, '20 世纪 60 年代出现无线电遥控模型车'), 7),
 'E238_片尾': (titles.closing(SER45, VOL45, S45A, 6, '下集：磁力片怎么拼都能吸上，为什么？'), 7),
 'E239_翻转': (e239_rotate, 22), 'E239_指南针': (e239_compass, 22),
 'E239_片头': (titles.opening(SER45, VOL45, S45A, 7, '21 世纪初出现边缘嵌磁铁的磁力拼搭片'), 7),
 'E239_片尾': (titles.closing(SER45, VOL45, S45A, 7, '下集：回力车没有电池，力气从哪里来？'), 7),
 'E240_卷紧': (e240_wind, 22), 'E240_距离': (e240_distance, 22),
 'E240_片头': (titles.opening(SER45, VOL45, S45A, 8, '20 世纪中后期出现往后拉就能跑的回力车'), 7),
 'E240_片尾': (titles.closing(SER45, VOL45, S45A, 8, '下集：八音盒里没有人，谁在弹琴？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
