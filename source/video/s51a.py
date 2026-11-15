"""第五十一季（第二十二层：门厅与客厅）第一批：E262 弹子锁、E263 门铃、E264 遥控器 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S51A = [('262', '弹子锁'), ('263', '门铃'), ('264', '遥控器'), ('265', '调光台灯'), ('266', '闭门器'),
        ('267', '百叶窗'), ('268', '暖气片'), ('269', '石英钟'), ('270', '三孔插头'), ('271', '地毯吸音')]
SER51, VOL51 = '从零造物', '第五十一季 · 第二十二层：门厅与客厅'
BRASS = (215, 180, 90)
STEEL = (175, 185, 195)
PINLO = (200, 120, 80)
PINHI = (90, 150, 210)
COPPER = (205, 120, 60)
IR = (200, 70, 70)

LOWS = [60, 110, 80, 130, 90]     # 每根下弹子的长度（像素）


def _lock(c, t, key, cx=960, label=''):
    """画一把剖开的弹子锁：锁壳（上）+ 锁芯（下），key=每个齿的高度列表或 None。"""
    top, shear, bot = 300, 560, 760          # 锁壳顶、分界线、锁芯底
    c.rect(cx - 640, top, cx + 640, shear, fill=mix(BG, STEEL, 0.55), r=12)
    c.rect(cx - 640, shear, cx + 640, bot, fill=mix(BG, BRASS, 0.55), r=12)
    c.line([(cx - 660, shear), (cx + 660, shear)], NRED, 4)
    c.text(cx + 660, shear - 26, '分界线', 'bold', 22, NRED, 'rm')
    c.text(cx - 630, top + 26, '锁壳（不转）', 'sans', 22, INK, 'lm')
    c.text(cx - 630, bot - 26, '锁芯（要转）', 'sans', 22, INK, 'lm')
    keyline = bot - 40                         # 没插钥匙时下弹子底端所在高度
    ok_all = True
    for k, lo in enumerate(LOWS):
        x = cx - 400 + k * 200
        c.rect(x - 34, top + 10, x + 34, bot - 30, fill=mix(BG, (250, 250, 245), 0.9), r=6)
        lift = 0 if key is None else key[k]
        lbot = keyline - lift
        ltop = lbot - lo
        utop, ubot = top + 20, ltop
        hi = 300 - lo - 30
        utop = ubot - hi
        # 弹簧
        sp = [(x + (14 if s % 2 else -14), top + 14 + s * (utop - top - 14) / 8) for s in range(9)]
        c.line(sp, mix(BG, INK, 0.5), 3)
        c.rect(x - 26, utop, x + 26, ubot, fill=mix(BG, PINHI, 1.0), r=8)
        c.rect(x - 26, ltop, x + 26, lbot, fill=mix(BG, PINLO, 1.0), r=8)
        good = abs(ltop - shear) < 4
        ok_all = ok_all and good
        if key is not None:
            c.ellipse(x, shear, 12, 12, fill=GREEN if good else NRED)
    if key is not None:
        pts = [(cx - 560, bot + 60)]
        for k, lift in enumerate(key):
            x = cx - 400 + k * 200
            pts += [(x - 60, keyline + 40 - lift), (x, keyline - lift), (x + 60, keyline + 40 - lift)]
        pts += [(cx + 560, bot + 10), (cx + 560, bot + 60)]
        c.poly(pts + [(cx - 560, bot + 60)], mix(BG, (160, 160, 170), 0.9))
    if label:
        c.text(cx, 930, label, 'bold', 30, GREEN if ok_all else NRED, 'mm')
    return ok_all


# ---------------------------------------------------------------- E262 弹子锁
def e262_pins(c, t, i):
    corner_tag(c, '第 262 集 · 一排上下两截的弹子')
    c.text(60, 96, '锁芯和锁壳之间卡着一排弹子，每根分上下两截；只有对的钥匙能把每个分界都顶到锁芯边上', 'serif', 36, INK)
    good = [(760 - 40) - lo - 560 for lo in LOWS]
    if t < 7:
        _lock(c, t, None, label='没插钥匙：上弹子跨在分界线上，锁芯转不动')
    else:
        f = min(1.0, (t - 7) / 5)
        key = [g * f for g in good]
        ok = _lock(c, t, key, label='对的钥匙：五个分界全对齐' if f >= 1 else '钥匙插进去，把弹子一根根顶起来')
        if ok and t > 15:
            c.arrow(1700, 680, 1700, 820, GREEN, 6, 18)
            c.text(1700, 860, '锁芯能转', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '弹簧把每对弹子往下压，上弹子卡住分界线，锁芯被别住'),
                (7.2, 14, '钥匙插进去，每个齿把一对弹子顶到不同高度'),
                (14.2, 22, '五个分界线同时对齐锁芯边，锁芯才能转（示意）')], y=1010)


def e262_wrong(c, t, i):
    corner_tag(c, '第 262 集 · 错一个齿就转不动')
    c.text(60, 96, '把钥匙的第三个齿剪低一点：其他四个都对，这一根的上弹子还卡在分界线上，锁芯照样转不动', 'serif', 36, INK)
    good = [(760 - 40) - lo - 560 for lo in LOWS]
    bad = list(good)
    bad[2] = good[2] - 40 if t > 7 else good[2]
    lab = '每个齿都对：能转' if t <= 7 else '第三个齿低了：转不动'
    _lock(c, t, bad, label=lab)
    if t > 14.2:
        c.text(960, 210, '5 个齿、每个齿 6 种高度：6 × 6 × 6 × 6 × 6 = 7776 种钥匙（示意）', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '先用对的钥匙：五个绿点，锁芯能转'),
                (7.2, 14, '换一把只有第三个齿低一点的钥匙：那一根变成红点'),
                (14.2, 22, '只要有一根卡着就转不动；齿越多、高度越多，配错的可能越小')], y=1010)


# ---------------------------------------------------------------- E263 门铃
def _coil(c, x0, y0, on):
    c.rect(x0, y0 - 30, x0 + 300, y0 + 30, fill=mix(BG, STEEL, 1.0), r=6)
    for k in range(14):
        x = x0 + 30 + k * 18
        c.ellipse(x, y0, 9, 42, outline=mix(BG, COPPER, 1.0), width=4)
    if on:
        for k in range(3):
            c.arc(x0 + 300, y0, 50 + k * 30, 50 + k * 30, -60, 60, mix(BG, NRED, 0.6), 3)


def e263_magnet(c, t, i):
    corner_tag(c, '第 263 集 · 通电吸，断电放')
    c.text(60, 96, '铁钉绕上线圈接上干电池就成了电磁铁，能吸起回形针；一断开，磁性没了，回形针掉下来', 'serif', 36, INK)
    on = (t < 7 and t > 2) or (t > 14.2 and (t % 2) < 1)
    _coil(c, 500, 480, on)
    c.rect(300, 720, 460, 820, fill=mix(BG, (60, 60, 70), 1.0), r=8)
    c.text(380, 770, '1.5 V', 'bold', 26, (255, 255, 255), 'mm')
    c.line([(460, 750), (560, 750), (560, 510)], mix(BG, COPPER, 1.0), 4)
    c.line([(300, 790), (240, 790), (240, 400), (520, 400), (520, 450)] if on else [(300, 790), (240, 790), (240, 400), (420, 400)], mix(BG, COPPER, 1.0), 4)
    c.text(420, 360, '接通' if on else '断开', 'bold', 26, GREEN if on else NRED, 'mm')
    n = 3
    for k in range(n):
        px = 860 + k * 22
        py = 480 if on else min(900, 480 + 400 * min(1, ((t % 2) if t > 14 else (t - 7 if t > 7 else 1)) * 2))
        if not on and t < 2:
            py = 900
        c.rect(px, py - 40, px + 10, py + 40, outline=mix(BG, STEEL, 1.0), width=4, r=5)
    caps(c, t, [(0, 7, '铁钉绕 50 圈漆包线，接上 1.5 伏干电池：回形针被吸住'),
                (7.2, 14, '断开一头导线：电磁铁没了磁性，回形针掉下来'),
                (14.2, 22, '一接一断，一吸一放，这就是门铃里的「手」（只用干电池）')], y=1010)


def e263_selfbreak(c, t, i):
    corner_tag(c, '第 263 集 · 自己断开又接通')
    c.text(60, 96, '门铃里铁片被吸过去敲一下铃，同时把电路拉断；没电了铁片弹回来，又把电路接上，又吸，又敲', 'serif', 36, INK)
    f = 3.0 if t > 14 else 1.0
    ph = (t * f) % 1
    pulled = ph < 0.5
    _coil(c, 300, 560, pulled)
    ax = 900 if pulled else 980
    c.line([(1000, 820), (1000, 760)], INK, 6)
    c.line([(1000, 760), (ax, 420)], mix(BG, STEEL, 1.0), 10)
    c.ellipse(ax - 20, 420, 26, 26, fill=mix(BG, (90, 90, 100), 1.0))
    c.arc(760, 360, 120, 120, 200, 340, mix(BG, BRASS, 1.0), 14)
    c.text(760, 210, '铃', 'bold', 30, INK, 'mm')
    if pulled:
        c.text(640, 300, '叮！', 'bold', 40, NRED, 'mm')
    cx, cy = 1040, 600
    c.ellipse(cx, cy, 12, 12, fill=INK)
    touching = not pulled
    c.line([(1000, 600), (cx - 10, cy)] if touching else [(960, 600), (980, 600)], mix(BG, COPPER, 1.0), 5)
    c.text(1240, 600, '触点：接上' if touching else '触点：断开', 'bold', 26, GREEN if touching else NRED, 'lm')
    c.text(1240, 680, '通电 → 吸 → 敲 → 断电 → 弹回 → 通电…', 'sans', 26, INK, 'lm')
    caps(c, t, [(0, 7, '按下门铃按钮：电路接通，电磁铁把铁片吸过去，小锤敲一下铃'),
                (7.2, 14, '铁片一动，触点分开，电磁铁没电，铁片被弹回'),
                (14.2, 22, '弹回来又接通，又吸又敲，一秒几十次，铃就一直响（示意）')], y=1010)


# ---------------------------------------------------------------- E264 遥控器
def _remote(c, x, y, lit):
    c.rect(x - 80, y - 260, x + 80, y + 260, fill=mix(BG, (60, 60, 70), 1.0), r=40)
    for r_ in range(4):
        for col in range(3):
            c.ellipse(x - 45 + col * 45, y - 120 + r_ * 70, 16, 16, fill=mix(BG, (150, 150, 160), 1.0))
    c.ellipse(x, y - 230, 14, 14, fill=IR if lit else mix(BG, (40, 40, 40), 1.0))


def e264_ir(c, t, i):
    corner_tag(c, '第 264 集 · 看不见的光')
    c.text(60, 96, '遥控器前端有一颗红外小灯，按键时一闪一闪；眼睛看不见，手机相机却能拍到这个亮点', 'serif', 36, INK)
    lit = (t * 8) % 1 < 0.5
    for j, lab in enumerate(['眼睛直接看：什么也没有', '手机屏幕里：一闪一闪']):
        cx = 520 + j * 880
        _remote(c, cx, 560, lit and j == 1)
        if j == 1:
            c.rect(cx - 260, 220, cx + 260, 900, outline=INK, width=6, r=40)
        c.text(cx, 960, lab, 'bold', 28, NRED if j == 0 else GREEN, 'mm')
    if t > 14.2:
        c.text(960, 180, '红外光比红光的波长更长，人眼看不见（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '按住遥控器的键，用眼睛看前端：什么也看不到'),
                (7.2, 14, '换手机相机对准它：屏幕上一闪一闪的亮点出来了'),
                (14.2, 22, '这是红外光，眼睛看不见，相机的感光芯片能「看」见')], y=1010)


def e264_code(c, t, i):
    corner_tag(c, '第 264 集 · 闪的节奏就是暗号')
    c.text(60, 96, '不同的键闪的节奏不一样，电视上的接收器认出暗号就执行；红外光被手挡住就不灵，却能被白墙反射过去', 'serif', 36, INK)
    codes = [('音量 +', [1, 0, 1, 1, 0, 1, 0, 0]), ('换台 +', [1, 1, 0, 1, 0, 0, 1, 0])]
    k = 0 if t < 7 else 1
    lab, bits = codes[k]
    if t < 14.2:
        for b, v in enumerate(bits):
            x = 300 + b * 160
            h = 160 if v else 30
            c.rect(x, 560 - h, x + 120, 560, fill=IR if v else mix(BG, INK, 0.2), r=6)
        c.text(960, 660, f'按「{lab}」：亮亮灭的节奏（示意）', 'bold', 30, INK, 'mm')
        c.rect(1600, 380, 1820, 560, fill=mix(BG, (40, 40, 50), 1.0), r=10)
        c.text(1710, 470, lab, 'bold', 28, (255, 255, 255), 'mm')
    else:
        _remote(c, 400, 600, (t * 8) % 1 < 0.5)
        c.rect(1500, 380, 1800, 560, fill=mix(BG, (40, 40, 50), 1.0), r=10)
        c.text(1650, 470, '电视', 'bold', 28, (255, 255, 255), 'mm')
        c.rect(900, 240, 960, 900, fill=mix(BG, (230, 230, 220), 1.0))
        c.text(930, 210, '白墙', 'bold', 24, INK, 'mm')
        c.line([(400, 370), (900, 280)], IR, 4)
        c.line([(900, 280), (1500, 470)], IR, 4)
        c.text(960, 960, '对着墙按，红外光反射到电视上，照样换台（以实测为准）', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '按音量键，红外灯按一种节奏亮灭'),
                (7.2, 14, '换台键是另一种节奏；电视的接收器认得每一种暗号'),
                (14.2, 22, '红外光是光：书挡住就不灵，对着白墙按却能反射过去')], y=1010)


CLIPS = {
 'E262_弹子': (e262_pins, 22), 'E262_错齿': (e262_wrong, 22),
 'E262_片头': (titles.opening(SER51, VOL51, S51A, 0, '1861 年小莱纳斯·耶鲁改进了弹子锁'), 7),
 'E262_片尾': (titles.closing(SER51, VOL51, S51A, 0, '下集：门铃怎么一直自己敲？'), 7),
 'E263_电磁铁': (e263_magnet, 22), 'E263_自断': (e263_selfbreak, 22),
 'E263_片头': (titles.opening(SER51, VOL51, S51A, 1, '19 世纪出现了电铃'), 7),
 'E263_片尾': (titles.closing(SER51, VOL51, S51A, 1, '下集：遥控器的信号怎么传过去？'), 7),
 'E264_红外': (e264_ir, 22), 'E264_暗号': (e264_code, 22),
 'E264_片头': (titles.opening(SER51, VOL51, S51A, 2, '20 世纪 80 年代红外遥控器普及'), 7),
 'E264_片尾': (titles.closing(SER51, VOL51, S51A, 2, '下集：台灯旋钮怎么调亮度？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
