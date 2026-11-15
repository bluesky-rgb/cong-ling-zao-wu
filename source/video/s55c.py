"""第五十五季（第二十四层：游乐场）第三批：E288 喷泉、E289 脚踏船、E290 抓娃娃机 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s55a import S55A, SER55, VOL55, KID

WATER = (110, 170, 235)
BOAT = (230, 170, 80)
CLAW = (180, 185, 195)
PLUSH = (220, 150, 170)


# ---------------------------------------------------------------- E288 喷泉
def _fountain(c, tank_h, x0=1300, gy=880, nozzle_x=500, level=1.0):
    top = gy - tank_h
    c.rect(x0 - 100, top - 300, x0 + 100, top, outline=mix(BG, INK, 0.6), width=5, r=10)
    wl = top - 300 * level
    c.rect(x0 - 96, wl, x0 + 96, top - 4, fill=mix(BG, WATER, 0.6), r=8)
    if tank_h > 0:
        c.rect(x0 - 110, top, x0 + 110, gy, fill=mix(BG, (150, 120, 90), 0.8))
    c.line([(x0, top - 4), (x0, gy - 20), (nozzle_x, gy - 20), (nozzle_x, gy - 60)], mix(BG, WATER, 0.9), 12)
    jet = max(0.0, (gy - 60) - wl) * 0.85
    for k in range(14):
        ph = (k / 14)
        y = gy - 60 - jet * math.sin(math.pi * ph / 2)
        c.ellipse(nozzle_x + 10 * math.sin(k), y, 8, 8, fill=mix(BG, WATER, 1.0))
    c.line([(nozzle_x - 200, wl), (x0 + 120, wl)], MUTED, 2)
    c.text(x0 + 140, wl, '水源水面', 'sans', 22, MUTED, 'lm')
    return jet


def e288_head(c, t, i):
    corner_tag(c, '第 288 集 · 水源越高，喷得越高')
    c.text(60, 96, '高处水池的水往下流，在低处的小喷口被挤出来往上喷：水源的水面比喷口高得越多，水压越大，喷得越高', 'serif', 36, INK)
    th = 0 if t < 9 else min(1.0, (t - 9) / 3) * 300
    jet = _fountain(c, th)
    c.text(500, 940, f'喷高约 {jet / 10:.0f} 厘米（示意）', 'bold', 28, INK, 'mm')
    c.line([(200, 880), (1700, 880)], mix(BG, INK, 0.4), 3)
    caps(c, t, [(0, 7, '瓶子和喷口放在一样高：水面比喷口高一点，喷得矮矮的'),
                (7.2, 14, '把瓶子垫高 30 厘米：水位差变大'),
                (14.2, 22, '水压更大，喷得更高；但最高也喷不过瓶里的水面（以实测为准）')], y=1010)


def e288_drop(c, t, i):
    corner_tag(c, '第 288 集 · 水面一降，喷得就矮')
    c.text(60, 96, '瓶里的水一点点流走，水面往下降，水位差变小，喷泉就一点点变矮；老喷泉要一直往高处的水池补水', 'serif', 36, INK)
    level = max(0.05, 1 - t / 22)
    jet = _fountain(c, 300, level=level)
    c.text(500, 940, f'喷高约 {jet / 10:.0f} 厘米（示意）', 'bold', 28, INK, 'mm')
    c.line([(200, 880), (1700, 880)], mix(BG, INK, 0.4), 3)
    caps(c, t, [(0, 7, '瓶身每隔 5 厘米画一道线，看着水面往下降'),
                (7.2, 14, '水面每降一截，喷的高度也跟着矮一截'),
                (14.2, 22, '今天的喷泉多用水泵把水压上去，就不用一直补高处的水池了')], y=1010)


# ---------------------------------------------------------------- E289 脚踏船
def _boat(c, x, y, paddle_ang, rev=False):
    c.poly([(x - 220, y - 40), (x + 180, y - 40), (x + 240, y), (x + 180, y + 50), (x - 220, y + 50)], mix(BG, BOAT, 1.0))
    wx = x - 280
    c.line([(x - 220, y - 10), (wx, y - 10)], INK, 5)
    for k in range(4):
        a = paddle_ang + k * math.pi / 2
        c.line([(wx, y - 10), (wx + 60 * math.cos(a), y - 10 + 60 * math.sin(a))], mix(BG, (120, 120, 130), 1.0), 12)


def e289_push(c, t, i):
    corner_tag(c, '第 289 集 · 往后推水，船往前走')
    c.text(60, 96, '船尾的明轮转起来，桨叶一片片把水往后推；你推水，水也反过来推你，于是船往前走', 'serif', 36, INK)
    wy = 600
    c.rect(100, wy, 1820, 900, fill=mix(BG, WATER, 0.3))
    x = 1100 - 0 + min(500, t * 25)
    _boat(c, x - 300, wy - 20, -t * 3)
    random.seed(4)
    for k in range(10):
        ph = (t * 0.6 + k / 10) % 1
        c.arrow(x - 640 - ph * 200, wy + 10 + (k % 3) * 20, x - 700 - ph * 200, wy + 10 + (k % 3) * 20, mix(BG, WATER, 1.0), 4, 12)
    c.arrow(x - 60, wy - 120, x + 120, wy - 120, GREEN, 6, 18)
    c.text(x + 30, wy - 170, '船往前', 'bold', 28, GREEN, 'mm')
    c.text(x - 760, wy + 120, '水往后', 'bold', 28, WATER, 'mm')
    caps(c, t, [(0, 7, '明轮往后拨水，把水往船后推'),
                (7.2, 14, '水被推的同时，也反过来推桨叶：一推一推，船往前走'),
                (14.2, 22, '往后推的水越多越快，船就越快（示意）')], y=1010)


def e289_reverse(c, t, i):
    corner_tag(c, '第 289 集 · 反着拧，船就倒着走')
    c.text(60, 96, '橡皮筋明轮往一个方向拧，船往前；反着拧，明轮反着转，把水往前推，船就倒着走', 'serif', 36, INK)
    for j, (lab, d) in enumerate([('明轮往后推水：船往前', 1), ('明轮往前推水：船往后', -1)]):
        wy = 380 + j * 320
        c.rect(100, wy, 1820, wy + 120, fill=mix(BG, WATER, 0.3))
        x = 960 + d * min(300, t * 18)
        _boat(c, x, wy - 20, -d * t * 3)
        c.arrow(x - 280 - 0, wy + 60, x - 280 - d * 120, wy + 60, mix(BG, WATER, 1.0), 5, 14)
        c.arrow(x, wy - 90, x + d * 140, wy - 90, GREEN, 5, 16)
        c.text(200, wy - 90, lab, 'bold', 26, INK, 'lm')
    caps(c, t, [(0, 7, '纸盒船尾装一个卡片明轮，用橡皮筋拧 20 圈放进水里'),
                (7.2, 14, '往后推水：船往前走'),
                (14.2, 22, '反着拧 20 圈：明轮把水往前推，船倒着走（浴缸里做要有大人陪）')], y=1010)


# ---------------------------------------------------------------- E290 抓娃娃机
def _claw(c, x, y, close, held):
    c.line([(x, 160), (x, y - 40)], mix(BG, CLAW, 1.0), 4)
    c.rect(x - 30, y - 50, x + 30, y - 20, fill=mix(BG, CLAW, 1.0), r=6)
    for s in (-1, 0, 1):
        a = math.radians(s * (40 - 30 * close) + 90)
        a2 = a + math.radians(-s * 40 * close) if s else a
        x1, y1 = x + s * 20, y - 20
        x2, y2 = x1 + 90 * math.cos(math.radians(90 - s * (40 - 25 * close))), y1 + 90 * math.sin(math.radians(90 - s * (40 - 25 * close)))
        x3, y3 = x2 - s * 40 * close, y2 + 40
        c.line([(x1, y1), (x2, y2), (x3, y3)], mix(BG, CLAW, 1.0), 8)


def e290_grip(c, t, i):
    corner_tag(c, '第 290 集 · 抓力 × 摩擦要撑住重量')
    c.text(60, 96, '爪子收紧压着娃娃，压得越紧摩擦越大；摩擦撑得住娃娃的重量就提得起来，撑不住就从爪子里滑下去', 'serif', 36, INK)
    for j, (lab, grip) in enumerate([('抓力小', 0.4), ('抓力大', 1.0)]):
        cx = 560 + j * 800
        if t < 5:
            yc, close, py = 380 + t * 60, 0.0, 760
        elif t < 7:
            yc, close, py = 680, (t - 5) / 2, 760
        else:
            up = min(1.0, (t - 7) / 4)
            yc, close = 680 - 300 * up, 1.0
            slip = grip < 0.6 and up > 0.4
            py = 760 - 300 * up if not slip else min(760, 760 - 300 * 0.4 + (up - 0.4) * 800)
        _claw(c, cx, yc, close, False)
        c.ellipse(cx, py, 70, 60, fill=mix(BG, PLUSH, 1.0))
        c.text(cx, 900, lab + ('：提到一半滑掉了' if grip < 0.6 and t > 9 else ('：提起来了' if t > 9 else '')), 'bold', 28, NRED if grip < 0.6 else GREEN, 'mm')
    caps(c, t, [(0, 7, '爪子落下、收紧，压住毛绒娃娃'),
                (7.2, 14, '抓力小：压得不紧，摩擦撑不住重量，提到一半滑掉'),
                (14.2, 22, '抓力大：摩擦撑住了重量，提起来了（示意）')], y=1010)


def e290_center(c, t, i):
    corner_tag(c, '第 290 集 · 抓在重心附近')
    c.text(60, 96, '同一个娃娃：抓在一头，提起来娃娃一歪，重量全往一边坠，很快滑掉；抓在中间重心附近，稳稳提起来', 'serif', 36, INK)
    for j, (lab, off) in enumerate([('抓在一头', 90), ('抓在中间', 0)]):
        cx = 560 + j * 800
        up = min(1.0, max(0.0, (t - 4) / 5))
        yc = 600 - 260 * up
        tilt = (0.8 * up if off else 0)
        slip = off and up > 0.6
        _claw(c, cx, yc, 1.0, True)
        px = cx - off * math.cos(tilt)
        py = yc + 120 + off * math.sin(tilt)
        if slip:
            py = min(820, py + (up - 0.6) * 1000)
        c.ellipse(px, py, 130, 50, fill=mix(BG, PLUSH, 1.0))
        c.ellipse(cx - off * math.cos(tilt) * 0, yc + 120, 10, 10, fill=INK)
        c.text(cx, 900, lab + ('：歪了、滑掉' if slip else ('：稳稳提起' if up > 0.9 and not off else '')), 'bold', 28, NRED if off else GREEN, 'mm')
    caps(c, t, [(0, 7, '吸管三爪手：一次抓娃娃的一头，一次抓中间'),
                (7.2, 14, '抓在一头：一提就歪，重量往一边坠，滑掉了'),
                (14.2, 22, '抓在重心附近：稳稳提起；娃娃机的抓力还能被调小，别太较真（以实测为准）')], y=1010)


CLIPS = {
 'E288_水位': (e288_head, 22), 'E288_下降': (e288_drop, 22),
 'E288_片头': (titles.opening(SER55, VOL55, S55A, 6, '古罗马城里就有靠水位差的喷泉'), 7),
 'E288_片尾': (titles.closing(SER55, VOL55, S55A, 6, '下集：往后拨水，船为什么往前？'), 7),
 'E289_推水': (e289_push, 22), 'E289_反转': (e289_reverse, 22),
 'E289_片头': (titles.opening(SER55, VOL55, S55A, 7, '19 世纪已有明轮船'), 7),
 'E289_片尾': (titles.closing(SER55, VOL55, S55A, 7, '下集：娃娃机的爪子为什么抓不牢？'), 7),
 'E290_抓力': (e290_grip, 22), 'E290_重心': (e290_center, 22),
 'E290_片头': (titles.opening(SER55, VOL55, S55A, 8, '20 世纪初出现抓奖品的游戏机'), 7),
 'E290_片尾': (titles.closing(SER55, VOL55, S55A, 8, '下集：哈哈镜怎么把人照变形？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
