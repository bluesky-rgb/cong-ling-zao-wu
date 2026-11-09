"""第三十五季（第十四层：看与听的机器）第一批：E182 扬声器、E183 液晶屏、E184 投影仪 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L

S35A = [('182', '扬声器'), ('183', '液晶屏'), ('184', '投影仪'), ('185', '防窥膜'), ('186', '光盘'),
        ('187', '夜光表盘'), ('188', '骨传导耳机'), ('189', '调音器'), ('190', '自动对焦'), ('191', '视频通话')]
SER35, VOL35 = '从零造物', '第三十五季 · 第十四层：看与听的机器'
COIL = (200, 130, 70)
MAGN = (200, 80, 80)
MAGS = (80, 120, 200)
CUP = (235, 230, 215)
LIGHT = (255, 230, 150)
LC = (150, 200, 170)
SCREEN = (60, 70, 85)


# ---------------------------------------------------------------- E182 扬声器
def e182_vibrate(c, t, i):
    corner_tag(c, '第 182 集 · 电流一变，线圈就被推来推去')
    c.text(60, 96, '音乐信号是一股忽强忽弱、忽正忽反的电流：它让线圈变成一块会翻面的小磁铁，被磁铁推开又吸回', 'serif', 34, INK)
    sig = math.sin(t * 2.2) * 0.7 + 0.3 * math.sin(t * 5.3)
    gx0, gx1, gy = 100, 760, 300
    c.rect(80, 200, 780, 420, fill=SHEET, r=12)
    c.text(430, 230, '手机送出的电流（示意）', 'sans', 22, MUTED, 'mm')
    pts = [(gx0 + (gx1 - gx0) * k / 120, gy + 30 - 70 * (math.sin((t - 3 + k / 40) * 2.2) * 0.7 + 0.3 * math.sin((t - 3 + k / 40) * 5.3))) for k in range(121)]
    c.line(pts, SPARK, 3)
    c.ellipse(gx1, pts[-1][1], 9, 9, fill=SPARK)
    cx, cy = 1250, 640
    dx = sig * 40
    c.rect(cx - 110, cy + 120, cx + 110, cy + 200, fill=MAGN, r=6)
    c.rect(cx - 110, cy + 200, cx + 110, cy + 280, fill=MAGS, r=6)
    c.text(cx, cy + 160, 'N', 'bold', 30, BG, 'mm')
    c.text(cx, cy + 240, 'S', 'bold', 30, BG, 'mm')
    cupy = cy - 60 - dx
    c.poly([(cx - 260, cupy - 210), (cx + 260, cupy - 210), (cx + 120, cupy), (cx - 120, cupy)], mix(BG, CUP, 0.85))
    for k in range(6):
        c.ellipse(cx, cupy + 20 + k * 12, 100, 14, outline=COIL, width=4)
    c.text(cx - 360, cupy + 60, '线圈粘在杯底', 'sans', 22, COIL, 'rm')
    c.text(cx - 360, cy + 200, '磁铁', 'sans', 22, MAGN, 'rm')
    if sig > 0:
        c.arrow(cx + 200, cupy + 40, cx + 200, cupy - 40, GREEN, 4, 12)
        c.text(cx + 230, cupy, '同极相斥：推开', 'bold', 22, GREEN, 'lm')
    else:
        c.arrow(cx + 200, cupy - 40, cx + 200, cupy + 40, NRED, 4, 12)
        c.text(cx + 230, cupy, '异极相吸：拉回', 'bold', 22, NRED, 'lm')
    for k in range(4):
        r = ((t * 200 + k * 60) % 240)
        c.arc(cx, cupy - 225, r + 20, (r + 20) * 0.4, 200, 340, mix(BG, MUTED, 1 - r / 240), 3)
    caps(c, t, [(0, 7, '电流一会儿往这边流、一会儿往那边流，大小也一直在变'),
                (7.2, 14, '通电的线圈就是一块小磁铁，电流一反向，它的南北极就翻过来'),
                (14.2, 22, '磁铁一推一拉，线圈带着纸杯来回振动，推着空气：声音就出来了（示意）')], y=1010)


def e182_magnets(c, t, i):
    corner_tag(c, '第 182 集 · 磁铁越强，纸杯振得越猛')
    c.text(60, 96, '同一个纸杯扬声器、同样的音量：没有磁铁、一块磁铁、两块磁铁，纸杯振动的幅度不一样', 'serif', 36, INK)
    vals = [('没有磁铁', 0.04), ('一块磁铁', 0.5), ('两块磁铁', 0.9)]
    for k, (lab, a) in enumerate(vals):
        x = 360 + k * 600
        y = 560
        d = a * 40 * math.sin(t * 9 + k)
        c.poly([(x - 170, y - 160 - d), (x + 170, y - 160 - d), (x + 80, y + 20 - d), (x - 80, y + 20 - d)], mix(BG, CUP, 0.85))
        for j in range(4):
            c.ellipse(x, y + 34 - d + j * 9, 70, 10, outline=COIL, width=3)
        for j in range(int(k)):
            c.rect(x - 80, y + 90 + j * 50, x + 80, y + 136 + j * 50, fill=MAGN if j % 2 == 0 else MAGS, r=6)
        c.text(x, 850, lab, 'bold', 28, INK, 'mm')
        for j in range(5):
            h = a * 60 * abs(math.sin(t * 9 + j * 0.8))
            c.rect(x - 110 + j * 46, 340 - h, x - 80 + j * 46, 340, fill=mix(BG, SPARK, 0.8), r=4)
        c.text(x, 380, '声音', 'sans', 20, MUTED, 'mm')
    c.text(960, 925, '纸杯的面越大，推动的空气越多；只接手机耳机口，绝不接插座', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '没有磁铁，线圈通了电也没有东西推它，纸杯几乎不动'),
                (7.2, 14, '放上一块磁铁，纸杯里就有了小小的音乐声'),
                (14.2, 22, '两块磁铁更强，推得更猛，声音更大：真扬声器里都有一块强磁铁（示意）')], y=1010)


# ---------------------------------------------------------------- E183 液晶屏
def _wave(c, x0, x1, y, ang, col, ph, amp=40, n=60):
    pts = []
    for k in range(n + 1):
        x = x0 + (x1 - x0) * k / n
        v = amp * math.sin(ph + k * 0.5)
        pts.append((x + v * math.sin(ang) * 0.35, y - v * math.cos(ang)))
    c.line(pts, col, 3)


def e183_polarizer(c, t, i):
    corner_tag(c, '第 183 集 · 两片偏光片转成垂直，光就过不去')
    c.text(60, 96, '屏幕射出的光只在一个方向振动；偏光墨镜只让另一个方向的振动通过，转到垂直，屏幕就黑了', 'serif', 36, INK)
    ang = min(math.pi / 2, t / 16 * math.pi / 2)
    ph = t * 8
    c.rect(100, 380, 260, 740, fill=mix(BG, LIGHT, 0.85), r=10)
    c.text(180, 780, '手机屏', 'bold', 24, INK, 'mm')
    _wave(c, 260, 900, 560, 0, LIGHT, ph)
    c.rect(900, 420, 940, 700, fill=mix(BG, (110, 110, 130), 0.8), r=8)
    for k in range(7):
        y = 440 + k * 38
        cx = 920
        L = 18
        c.line([(cx - L * math.sin(ang), y - L * math.cos(ang) + 18), (cx + L * math.sin(ang), y + L * math.cos(ang) + 18)], INK, 3)
    c.text(920, 740, f'偏光墨镜 转了 {math.degrees(ang):.0f}°', 'bold', 22, INK, 'mm')
    I = math.cos(ang) ** 2
    if I > 0.01:
        _wave(c, 940, 1500, 560, ang, mix(BG, LIGHT, I), ph, 40 * math.sqrt(I))
    c.ellipse(1640, 560, 80, 50, fill=SHEET, outline=INK, width=3)
    c.ellipse(1640, 560, 26, 26, fill=INK)
    c.text(1640, 660, '眼睛看到', 'sans', 22, MUTED, 'mm')
    c.rect(1580, 700, 1700, 760, fill=mix(BG, LIGHT, I), r=6)
    c.text(1640, 800, f'亮度 {I * 100:.0f}%', 'mono', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '手机屏最外面贴着一片偏光片，射出来的光只在一个方向上振动'),
                (7.2, 14, '偏光墨镜也是一片偏光片：方向一致，光全部通过；慢慢转，透过的越来越少'),
                (14.2, 22, '转到 90°，两片垂直，光一点也过不去，屏幕看起来全黑（示意）')], y=1010)


def e183_pixel(c, t, i):
    corner_tag(c, '第 183 集 · 液晶是一扇扇会转的百叶窗')
    c.text(60, 96, '一个像素：两片垂直的偏光片中间夹着液晶。不通电，液晶把光拧转 90° 能过；通电就挡住', 'serif', 34, INK)
    on = (int(t / 5.5) % 2 == 1)
    y = 560
    xs = [180, 520, 860, 1200, 1540]
    c.rect(100, 380, 260, 740, fill=mix(BG, LIGHT, 0.9), r=10)
    c.text(180, 780, '背光', 'bold', 22, INK, 'mm')
    c.rect(500, 400, 540, 720, fill=mix(BG, (110, 110, 130), 0.8), r=8)
    c.text(520, 760, '偏光片 ↕', 'sans', 20, MUTED, 'mm')
    c.rect(1180, 400, 1220, 720, fill=mix(BG, (110, 110, 130), 0.8), r=8)
    c.text(1200, 760, '偏光片 ↔', 'sans', 20, MUTED, 'mm')
    c.rect(620, 420, 1100, 700, fill=mix(BG, LC, 0.25), r=10)
    for k in range(8):
        x = 650 + k * 60
        a = 0 if on else (k / 7) * math.pi / 2
        L = 70
        c.line([(x - 10 * math.sin(a), y - L * math.cos(a) * 0.9 - 10 * math.sin(a)), (x + 10 * math.sin(a), y + L * math.cos(a) * 0.9 + 10 * math.sin(a))], LC, 10)
    c.text(860, 400 - 10, '液晶分子', 'sans', 22, LC, 'mm')
    ph = t * 8
    _wave(c, 260, 500, y, 0, LIGHT, ph, 34)
    _wave(c, 540, 620, y, 0, LIGHT, ph, 34)
    if not on:
        _wave(c, 1100, 1180, y, math.pi / 2, LIGHT, ph, 34)
        _wave(c, 1220, 1500, y, math.pi / 2, LIGHT, ph, 34)
        c.rect(1560, 470, 1760, 650, fill=mix(BG, LIGHT, 0.95), r=10)
        c.text(1660, 700, '不通电：亮', 'bold', 26, GREEN, 'mm')
        c.text(1340, 500, '振动方向转成了横的', 'sans', 20, LIGHT, 'mm')
    else:
        c.rect(1560, 470, 1760, 650, fill=mix(BG, SCREEN, 0.9), outline=MUTED, width=2, r=10)
        c.text(1660, 700, '通电：暗', 'bold', 26, NRED, 'mm')
        c.text(860, 760, '通电后分子全部站直，不再拧转光', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '每个像素背后都有灯，前后各一片偏光片，方向互相垂直'),
                (7.2, 14, '不通电时，液晶分子排成螺旋，把光的振动方向慢慢拧转 90°，正好穿过第二片'),
                (14.2, 22, '一通电，分子全部站直，光不再被拧转，就被挡住：几百万个像素一起开关（示意）')], y=1010)


# ---------------------------------------------------------------- E184 投影仪
def e184_image(c, t, i):
    corner_tag(c, '第 184 集 · 透镜把画面倒过来、放大')
    c.text(60, 96, '屏幕上每一点发出的光，穿过凸透镜后在远处重新聚成一点：画面倒过来，而且放大了', 'serif', 36, INK)
    ax = 540
    lx = 620
    f = 160
    u = 200
    v = u * f / (u - f)
    ox = lx - u
    ix = lx + v
    c.line([(80, ax), (1860, ax)], mix(BG, MUTED, 0.5), 1)
    c.ellipse(lx, ax, 22, 200, fill=mix(BG, (170, 210, 240), 0.5), outline=MUTED, width=3)
    c.text(lx, ax + 240, '放大镜（凸透镜）', 'sans', 22, MUTED, 'mm')
    h = 80
    c.rect(ox - 14, ax - h, ox, ax + 10, fill=mix(BG, LIGHT, 0.9))
    c.arrow(ox - 30, ax, ox - 30, ax - h, SPARK, 4, 14)
    c.text(ox - 40, ax + 40, '手机屏', 'sans', 22, INK, 'mm')
    Hs = h * v / u
    c.rect(ix, ax - 300, ix + 20, ax + 360, fill=mix(BG, CUP, 0.6))
    c.text(ix - 10, ax - 320, '白墙', 'sans', 22, MUTED, 'rm')
    p = min(1.0, t / 10)
    for k, col in enumerate([LIGHT, mix(LIGHT, SPARK, 0.5), mix(LIGHT, MUTED, 0.3)]):
        y0 = ax - h
        tgt = (ix, ax + min(340, Hs))
        if k == 0:
            pts = [(ox, y0), (lx, y0), tgt]
        elif k == 1:
            pts = [(ox, y0), (lx, ax), tgt]
        else:
            pts = [(ox, y0), (lx, ax - h - 60), tgt]
        L = len(pts)
        draw = [pts[0]]
        tot = sum(math.dist(pts[j], pts[j + 1]) for j in range(L - 1))
        d = tot * p
        for j in range(L - 1):
            sl = math.dist(pts[j], pts[j + 1])
            if d >= sl:
                draw.append(pts[j + 1]); d -= sl
            else:
                f_ = d / sl
                draw.append((pts[j][0] + (pts[j + 1][0] - pts[j][0]) * f_, pts[j][1] + (pts[j + 1][1] - pts[j][1]) * f_)); break
        c.line(draw, mix(BG, col, 0.9), 3)
    if p >= 1:
        c.arrow(ix - 30, ax, ix - 30, ax + min(340, Hs), SPARK, 6, 18)
        c.text(ix - 50, ax + 90, '倒过来的大画面', 'bold', 24, SPARK, 'rm')
    c.text(380, 300, '所以手机要倒着放', 'bold', 24, NRED, 'mm')
    caps(c, t, [(0, 7, '手机屏上的每一点都在往四面八方发光'),
                (7.2, 14, '射到放大镜上的那一束，被折弯后在远处的墙上重新聚成一点'),
                (14.2, 22, '上面的点聚到下面，下面的点聚到上面：画面倒过来，还放大了好多倍（示意）')], y=1010)


def e184_distance(c, t, i):
    corner_tag(c, '第 184 集 · 墙越远，手机越要贴近镜片')
    c.text(60, 96, '鞋盒投影仪挪到 1 米、2 米、3 米外：墙越远，画面越大，手机要往镜片那边推一点才清楚', 'serif', 36, INK)
    f = 10.0
    rows = [(100, '1 米'), (200, '2 米'), (300, '3 米')]
    k = min(2, int(t / 6))
    for j, (D, lab) in enumerate(rows):
        y = 300 + j * 190
        u = 1 / (1 / f - 1 / D)
        a = 1.0 if j <= k else 0.25
        c.rect(120, y - 50, 1180, y + 70, fill=SHEET, r=12)
        bx = 200
        c.rect(bx, y - 30, bx + 240, y + 50, fill=mix(BG, (170, 130, 90), 0.6 * a), r=6)
        c.ellipse(bx + 240, y + 10, 8, 40, fill=mix(BG, (170, 210, 240), a))
        px = bx + 240 - u * 18
        c.rect(px - 6, y - 20, px + 6, y + 40, fill=mix(BG, LIGHT, a))
        wx = 520 + D * 2
        c.line([(bx + 248, y + 10), (wx, y - 10 - D * 0.12), (wx, y + 30 + D * 0.12), (bx + 248, y + 10)], mix(BG, LIGHT, 0.5 * a), 2)
        c.rect(wx, y - 14 - D * 0.12, wx + 10, y + 34 + D * 0.12, fill=mix(BG, CUP, a))
        c.text(1220, y, f'墙 {lab}', 'bold', 26, mix(BG, INK, a), 'lm')
        c.text(1380, y, f'手机到镜片 {u:.1f} 厘米', 'mono', 24, mix(BG, SPARK, a), 'lm')
    c.text(960, 900, '按焦距 10 厘米的放大镜算（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '墙离得近，画面小，手机要离镜片远一点'),
                (7.2, 14, '墙挪远，画面变大，手机要往镜片那边推一点'),
                (14.2, 22, '再远，手机就几乎贴在一倍焦距那里：真投影仪也是靠前后挪镜头来对焦（示意）')], y=1010)


CLIPS = {
 'E182_振动': (e182_vibrate, 22), 'E182_磁铁': (e182_magnets, 22),
 'E182_片头': (titles.opening(SER35, VOL35, S35A, 0, '1925 年动圈扬声器问世'), 7),
 'E182_片尾': (titles.closing(SER35, VOL35, S35A, 0, '下集：戴偏光墨镜歪头看手机，屏幕为什么黑了？'), 7),
 'E183_偏振': (e183_polarizer, 22), 'E183_像素': (e183_pixel, 22),
 'E183_片头': (titles.opening(SER35, VOL35, S35A, 1, '1968 年液晶显示首次展示'), 7),
 'E183_片尾': (titles.closing(SER35, VOL35, S35A, 1, '下集：一块小小的手机屏，怎么在墙上放出大画面？'), 7),
 'E184_成像': (e184_image, 22), 'E184_距离': (e184_distance, 22),
 'E184_片头': (titles.opening(SER35, VOL35, S35A, 2, '17 世纪已有幻灯'), 7),
 'E184_片尾': (titles.closing(SER35, VOL35, S35A, 2, '下集：贴了防窥膜，旁边的人为什么只看到一片黑？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
