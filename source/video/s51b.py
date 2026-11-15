"""第五十一季（第二十二层：门厅与客厅）第二批：E265 调光台灯、E266 闭门器、E267 百叶窗 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s51a import S51A, SER51, VOL51, COPPER, STEEL

LAMP = (250, 220, 120)
GRAPH = (70, 70, 80)
OIL = (210, 170, 60)
WOOD = (170, 130, 90)
SUN = (250, 210, 90)
SLAT = (220, 220, 210)


def _bulb(c, x, y, b):
    for k in range(4, 0, -1):
        c.ellipse(x, y, 40 + k * 26 * b, 40 + k * 26 * b, fill=mix(BG, LAMP, 0.12 * b))
    c.ellipse(x, y, 40, 40, fill=mix(BG, LAMP, 0.25 + 0.75 * b))


# ---------------------------------------------------------------- E265 调光台灯
def e265_resist(c, t, i):
    corner_tag(c, '第 265 集 · 电阻越长，灯越暗')
    c.text(60, 96, '电流先走过一段铅笔芯再到灯：夹子离得越远，要走的铅笔芯越长，电阻越大，电流越小，灯越暗', 'serif', 36, INK)
    x0, x1, y = 400, 1600, 640
    c.rect(x0, y - 18, x1, y + 18, fill=mix(BG, GRAPH, 1.0), r=8)
    c.text(x0 - 20, y, '铅笔芯', 'bold', 24, INK, 'rm')
    d = 0.08 + 0.92 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi * 1.0)) if t > 2 else 0.08
    if t > 14.2:
        d = 0.08 + 0.92 * min(1, (t - 14.2) / 6)
    sx = x0 + 20 + (x1 - x0 - 40) * d
    c.line([(x0 + 20, y - 18), (x0 + 20, 420), (900, 420)], mix(BG, COPPER, 1.0), 5)
    c.rect(sx - 14, y - 40, sx + 14, y + 40, fill=NRED, r=6)
    c.line([(sx, y + 40), (sx, 860), (1100, 860)], mix(BG, COPPER, 1.0), 5)
    c.rect(1100, 820, 1260, 900, fill=mix(BG, (60, 60, 70), 1.0), r=8)
    c.text(1180, 860, '3 V', 'bold', 26, (255, 255, 255), 'mm')
    c.line([(1260, 860), (1750, 860), (1750, 420), (1100, 420)], mix(BG, COPPER, 1.0), 5)
    b = max(0.08, 1 - d)
    _bulb(c, 1000, 420, b)
    L = (sx - x0 - 20) / (x1 - x0 - 40) * 10
    c.text(sx, y - 70, f'{L:.0f} 厘米', 'bold', 26, NRED, 'mm')
    c.text(960, 230, f'亮度（示意）：{"█" * max(1, int(b * 10))}', 'bold', 28, mix(BG, LAMP, 1.0), 'mm')
    caps(c, t, [(0, 7, '夹子离第一个夹子 1 厘米：电流只走一小段铅笔芯，灯很亮'),
                (7.2, 14, '往远处滑，要走的铅笔芯越来越长，灯越来越暗'),
                (14.2, 22, '台灯旋钮背后的电位器也是这样：拧动改变电阻的长度（只用 3 伏干电池）')], y=1010)


def e265_pwm(c, t, i):
    corner_tag(c, '第 265 集 · 飞快地一开一关')
    c.text(60, 96, '很多 LED 台灯调光不靠电阻，而是让灯每秒开关几百次：开的时间占得越多越亮，眼睛看不出在闪', 'serif', 36, INK)
    duty = 0.8 if t < 7 else (0.3 if t < 14.2 else 0.8 - 0.6 * min(1, (t - 14.2) / 6))
    x0, y0, W = 260, 560, 1400
    n = 8
    for k in range(n):
        xa = x0 + k * W / n
        xb = xa + W / n * duty
        c.rect(xa, y0 - 160, xb, y0, fill=mix(BG, LAMP, 1.0))
        c.rect(xb, y0 - 10, xa + W / n, y0, fill=mix(BG, INK, 0.25))
    c.line([(x0, y0 + 4), (x0 + W, y0 + 4)], mix(BG, INK, 0.5), 2)
    c.text(x0, y0 + 50, '时间 →（每一格不到百分之一秒，示意）', 'sans', 24, MUTED, 'lm')
    c.text(960, 330, f'开的时间占 {int(duty * 100)}%', 'bold', 30, INK, 'mm')
    _bulb(c, 960, 780, duty)
    caps(c, t, [(0, 7, '开的时间长、关的时间短：看起来很亮'),
                (7.2, 14, '开的时间缩短：同样一秒里亮的总时间少了，看起来就暗'),
                (14.2, 22, '用手机慢动作录调到最暗的 LED 台灯，有时能看到条纹在闪（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E266 闭门器
def _door(c, ang, label):
    hx, hy = 400, 760
    L = 700
    a = math.radians(ang)
    ex, ey = hx + L * math.cos(a), hy - L * math.sin(a) * 0.55
    c.line([(hx - 100, hy), (hx + 820, hy)], mix(BG, INK, 0.4), 4)
    c.text(hx + 760, hy + 30, '门框', 'sans', 22, MUTED, 'mm')
    c.line([(hx, hy), (ex, ey)], mix(BG, WOOD, 1.0), 26)
    c.ellipse(hx, hy, 16, 16, fill=INK)
    c.text(960, 880, label, 'bold', 28, INK, 'mm')


def e266_spring(c, t, i):
    corner_tag(c, '第 266 集 · 只有弹簧：砰！')
    c.text(60, 96, '只靠弹簧，门越关越快，最后砰地撞上；闭门器里还有一个装油的小缸，油从小孔挤过去，门就慢下来', 'serif', 36, INK)
    if t < 14.2:
        f = min(1, ((t % 7) / 2.0) ** 2)
        ang = 80 * (1 - f)
        _door(c, ang, '只有弹簧：约 2 秒，砰地撞上（示意）')
        if ang < 3:
            c.text(1300, 650, '砰！', 'bold', 60, NRED, 'mm')
    else:
        f = min(1, (t - 14.2) / 7.0)
        ang = 80 * (1 - f) if f < 0.85 else 80 * 0.15 * (1 - (f - 0.85) / 0.15)
        _door(c, ang, '弹簧 + 油缸：慢慢关，最后轻轻贴紧（示意）')
    caps(c, t, [(0, 7, '把阻尼拿掉，只剩弹簧：门被越拉越快'),
                (7.2, 14, '最后砰地一声撞在门框上'),
                (14.2, 22, '加上油缸：油要挤过小孔，门慢慢地、稳稳地关上')], y=1010)


def e266_orifice(c, t, i):
    corner_tag(c, '第 266 集 · 孔越细，回得越慢')
    c.text(60, 96, '针筒装满水，橡皮筋把活塞拉回去：出口套细管，水挤得慢，活塞回得慢；粗管快；不装水更快', 'serif', 36, INK)
    for j, (lab, T) in enumerate([('细吸管：约 12 秒', 12.0), ('粗吸管：约 4 秒', 4.0), ('不装水：约 1 秒', 1.0)]):
        cx = 380 + j * 580
        top, bot = 300, 760
        c.rect(cx - 70, top, cx + 70, bot, outline=mix(BG, INK, 0.6), width=4, r=10)
        f = min(1, (t % 22) / T)
        py = top + 30 + (bot - top - 80) * f
        if j < 2:
            c.rect(cx - 66, py, cx + 66, bot - 4, fill=mix(BG, (90, 160, 220), 0.6), r=8)
        c.rect(cx - 66, py - 16, cx + 66, py, fill=mix(BG, (60, 60, 70), 1.0))
        c.line([(cx, py - 16), (cx, top - 60)], mix(BG, (60, 60, 70), 1.0), 8)
        c.line([(cx, top - 60), (cx + 110, top - 60), (cx + 110, bot)], NRED, 3)
        w = 6 if j == 0 else 18
        c.rect(cx - w / 2, bot, cx + w / 2, bot + 80, fill=mix(BG, (200, 200, 200), 0.8))
        if j < 2 and f < 1:
            for s in range(3):
                c.ellipse(cx, bot + 100 + ((t * 3 + s / 3) % 1) * 60, w / 2 + 2, w / 2 + 2, fill=mix(BG, (90, 160, 220), 1.0))
        c.text(cx, 960, lab, 'bold', 26, INK, 'mm')
    c.text(1500, 170, '红线：橡皮筋（像弹簧）', 'sans', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '橡皮筋就是弹簧，负责把活塞拉回去'),
                (7.2, 14, '水要从出口挤出去：管越细，挤得越慢，活塞回得越慢'),
                (14.2, 22, '闭门器里拧那颗小螺丝，就是在调油孔的大小（时间以实测为准）')], y=1010)


# ---------------------------------------------------------------- E267 百叶窗
def _blind(c, cx, cy, ang, n=7, gap=70, w=200):
    a = math.radians(ang)
    dx, dy = w / 2 * math.cos(a), w / 2 * math.sin(a)
    for k in range(n):
        y = cy + (k - (n - 1) / 2) * gap
        c.line([(cx - dx, y + dy), (cx + dx, y - dy)], mix(BG, SLAT, 1.0), 10)
    return a


def e267_light(c, t, i):
    corner_tag(c, '第 267 集 · 斜照的阳光被叶片挡住')
    c.text(60, 96, '太阳从斜上方照进来：叶片水平时，光直接落到屋里地上；叶片转成屋里那边高，阳光就被挡住或反射到天花板', 'serif', 36, INK)
    ang = 0 if t < 3.5 else (30 if t < 7.2 else (60 if t < 14.2 else 90))
    cx, cy = 960, 560
    _blind(c, cx, cy, ang)
    c.line([(cx + 340, 170), (cx + 340, 930)], mix(BG, INK, 0.2), 2)
    for s in range(7):
        ya = cy - 180 + s * 50
        xa = cx - 70
        thru = ang == 0 or (ang == 30 and s % 2 == 0)
        c.line([(xa - 300, ya - 172), (xa, ya)], mix(BG, SUN, 0.8), 3)
        if thru:
            c.arrow(xa, ya, xa + 420, ya + 240, mix(BG, SUN, 0.8), 3, 12)
        elif ang == 30:
            c.arrow(xa + 40, ya, xa + 200, ya - 200, mix(BG, SUN, 0.5), 3, 12)
    lab = {0: '0°：阳光直接晒进屋里', 30: '30°：一部分被挡住，一部分反射到天花板', 60: '60°：直射的阳光被挡住', 90: '90°：全关，屋里暗'}[ang]
    c.text(960, 960, lab, 'bold', 28, INK, 'mm')
    c.text(380, 930, '窗外', 'sans', 24, MUTED, 'mm')
    c.text(1560, 930, '屋里', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '台灯从斜上方照，叶片转到 0°、30°'),
                (7.2, 14, '转到 60°：直射的光被挡住，白纸上暗了，四周还是亮的'),
                (14.2, 22, '转到 90° 就是全关；角度决定挡住哪个方向的光（示意，以实测为准）')], y=1010)


def e267_view(c, t, i):
    corner_tag(c, '第 267 集 · 从下往上看，被叶片挡住')
    c.text(60, 96, '叶片转成屋里那边低：路上的人从下往上看，视线撞在叶片上看不进来；屋里的人往外上方看，仍看得见', 'serif', 36, INK)
    cx, cy = 960, 500
    _blind(c, cx, cy, -35, n=6, gap=80, w=180)
    c.text(cx, 190, '百叶窗（屋里那边低）', 'bold', 24, INK, 'mm')
    k = math.tan(math.radians(35))
    ex, ey = 1650, 890
    c.ellipse(ex, ey, 30, 30, fill=GREEN)
    c.text(ex, ey + 56, '屋里的人', 'bold', 24, GREEN, 'mm')
    if t < 7.2 or t > 14.2:
        c.arrow(ex - 30, ey - 20, 680, ey - 20 - (ex - 30 - 680) * k, GREEN, 4, 16)
        c.text(1500, 560, '顺着缝往外上方看：看得见', 'bold', 26, GREEN, 'mm')
    px, py = 300, 900
    c.ellipse(px, py, 30, 30, fill=NRED)
    c.text(px, py + 50, '路上的人', 'bold', 24, NRED, 'mm')
    if t > 7:
        tx = cx - 70
        ty = py - (tx - px) * 0.55
        c.arrow(px + 30, py - 20, tx, ty, NRED, 4, 16)
        c.text(tx - 60, ty - 50, '撞在叶片上', 'bold', 26, NRED, 'rm')
    caps(c, t, [(0, 7, '叶片外高内低，屋里的人顺着叶片的缝往外上方看，看得见'),
                (7.2, 14, '路上的人在低处往上看，视线和叶片交叉，撞在叶片上'),
                (14.2, 22, '反过来转，挡住的方向也反过来；角度决定挡住谁的视线（以实测为准）')], y=1010)


CLIPS = {
 'E265_电阻': (e265_resist, 22), 'E265_闪烁': (e265_pwm, 22),
 'E265_片头': (titles.opening(SER51, VOL51, S51A, 3, '20 世纪中期出现可调光的台灯'), 7),
 'E265_片尾': (titles.closing(SER51, VOL51, S51A, 3, '下集：门怎么自己慢慢关上？'), 7),
 'E266_弹簧': (e266_spring, 22), 'E266_油孔': (e266_orifice, 22),
 'E266_片头': (titles.opening(SER51, VOL51, S51A, 4, '19 世纪末出现液压闭门器'), 7),
 'E266_片尾': (titles.closing(SER51, VOL51, S51A, 4, '下集：百叶窗挡住了什么？'), 7),
 'E267_挡光': (e267_light, 22), 'E267_视线': (e267_view, 22),
 'E267_片头': (titles.opening(SER51, VOL51, S51A, 5, '18 世纪欧洲已流行百叶窗'), 7),
 'E267_片尾': (titles.closing(SER51, VOL51, S51A, 5, '下集：一块暖气片怎么暖一屋？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
