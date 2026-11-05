"""第十八季（古法解密 6.0）第二批：B63 日晷、B64 皮影戏、B65 古琴 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s18a import SB18, VOL18, WOOD

EARTH = (70, 120, 170)
SUN = (250, 200, 80)
STR = (235, 225, 200)

# ---------------------------------------------------------------- B63 日晷
def b63_axis(c, t, i):
    corner_tag(c, 'B63 · 晷针平行于地轴')
    c.text(60, 96, '晷针斜着插：它和地面的夹角，等于你所在的纬度', 'serif', 40, INK)
    cx, cy, R = 640, 600, 300
    c.ellipse(cx, cy, R, R, fill=EARTH)
    seg(c, [(cx - R - 40, cy), (cx + R + 40, cy)], mix(BG, MUTED, 0.8), 2)
    c.text(cx - R - 50, cy, '赤道', 'sans', 22, MUTED, 'rm')
    c.line([(cx, cy + R + 60), (cx, cy - R - 80)], INK, 3)
    c.text(cx + 14, cy - R - 70, '地轴', 'sans', 24, INK, 'lm')
    phi = math.radians(40)
    a = fade(t, 2, 3)
    P = (cx + R * math.cos(phi), cy - R * math.sin(phi))
    if a > 0:
        c.ellipse(P[0], P[1], 10, 10, fill=mix(BG, SPARK, a))
        c.line([(cx, cy), P], mix(BG, MUTED, a), 2)
        c.arc(cx, cy, 80, 80, -math.degrees(phi), 0, mix(BG, SPARK, a), 3)
        c.text(cx + 110, cy - 30, '纬度 φ', 'bold', 24, mix(BG, SPARK, a), 'lm')
        tx, ty = -math.sin(phi), -math.cos(phi)
        c.line([(P[0] - tx * 220, P[1] - ty * 220), (P[0] + tx * 160, P[1] + ty * 160)], mix(BG, GREEN, a), 4)
        c.text(P[0] + 130, P[1] + 130, '地面', 'sans', 22, mix(BG, GREEN, a), 'lm')
    b = fade(t, 7, 8)
    if b > 0:
        L = 170
        Q = (P[0], P[1] - L * b)
        c.line([P, Q], mix(BG, NRED, b), 8)
        c.text(Q[0] + 20, Q[1], '晷针 ∥ 地轴', 'bold', 26, mix(BG, NRED, b), 'lm')
        tx, ty = -math.sin(phi), -math.cos(phi)
        # 夹角标记：晷针（向上）与地面切线（向左上方）之间
        ang_g = -90
        ang_t = math.degrees(math.atan2(ty, tx))
        c.arc(P[0], P[1], 70, 70, min(ang_g, ang_t), max(ang_g, ang_t), mix(BG, NRED, b), 3)
        mid = math.radians((ang_g + ang_t) / 2)
        c.text(P[0] + 105 * math.cos(mid), P[1] + 105 * math.sin(mid), 'φ', 'bold', 30, mix(BG, NRED, b), 'mm')
    d = fade(t, 13, 14)
    if d > 0:
        c.rect(1180, 300, 1840, 700, fill=mix(BG, SHEET, d), r=14)
        c.text(1510, 350, '晷针和地面的夹角 = 纬度', 'bold', 28, mix(BG, INK, d), 'mm')
        for k, (city, v) in enumerate((('北京', '约 40°'), ('上海', '约 31°'), ('广州', '约 23°'))):
            c.text(1300, 430 + k * 60, city, 'sans', 28, mix(BG, INK, d), 'lm')
            c.text(1720, 430 + k * 60, v, 'mono', 28, mix(BG, SPARK, d), 'rm')
        c.text(1510, 640, '（纬度拍摄前核对；用手机地图可查）', 'sans', 22, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 7, '地球绕着地轴转。站在纬度 40 度的地方，地面是斜着贴在球面上的'),
                (7.2, 14, '把晷针插得和地轴平行，它和地面的夹角正好等于当地纬度，针尖指向北天极'),
                (14.2, 22, '这样，太阳绕着晷针转，影子就在晷面上匀速地走')], y=1010)

def b63_hours(c, t, i):
    corner_tag(c, 'B63 · 每小时 15 度')
    c.text(60, 96, '地球 24 小时转一圈：影子每小时转 15 度', 'serif', 40, INK)
    cx, cy, R = 620, 580, 330
    c.ellipse(cx, cy, R, R, fill=SHEET, outline=WOOD, width=6)
    for h in range(6, 19):
        ang = math.radians(90 + (h - 12) * 15)
        x0, y0 = cx + (R - 40) * math.cos(ang), cy + (R - 40) * math.sin(ang)
        x1, y1 = cx + R * math.cos(ang), cy + R * math.sin(ang)
        c.line([(x0, y0), (x1, y1)], INK, 3)
        c.text(cx + (R - 75) * math.cos(ang), cy + (R - 75) * math.sin(ang), str(h), 'mono', 24, INK, 'mm')
    hour = 7 + 10 * min(t / 20, 1)
    ang = math.radians(90 + (hour - 12) * 15)
    c.line([(cx, cy), (cx + (R - 90) * math.cos(ang), cy + (R - 90) * math.sin(ang))], (60, 60, 70), 10)
    c.ellipse(cx, cy, 14, 14, fill=NRED)
    c.text(cx, cy + R + 50, '赤道式日晷的晷面（与赤道平行，晷针穿过圆心）', 'sans', 22, MUTED, 'mm')
    hh = int(hour); mm = int((hour - hh) * 60)
    c.rect(1100, 280, 1840, 470, fill=SHEET, r=14)
    c.text(1470, 330, '日晷读数', 'sans', 26, MUTED, 'mm')
    c.text(1470, 400, f'{hh:02d}:{mm:02d}', 'mono', 56, SPARK, 'mm')
    a = fade(t, 10, 11)
    if a > 0:
        c.rect(1100, 520, 1840, 880, fill=mix(BG, SHEET, a), r=14)
        c.text(1470, 570, '日晷走的是「太阳时」', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(1470, 640, '和北京时间会差几分到几十分钟：', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1470, 690, '① 你不在东经 120°（经度差）', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1470, 740, '② 地球公转有快有慢（均时差）', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1470, 820, '差多少：以实测为准', 'sans', 22, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '晷针平行地轴，太阳一天绕它转一圈：360 度除以 24 小时，每小时 15 度'),
                (7.2, 14, '所以赤道式日晷的刻度是均匀的，一格 15 度就是一个小时'),
                (14.2, 22, '它走的是太阳时：拿手机一对，可能差几分钟，也可能差半个多小时')], y=1010)

# ---------------------------------------------------------------- B64 皮影戏
def b64_size(c, t, i):
    corner_tag(c, 'B64 · 离灯越近，影子越大')
    c.text(60, 96, '影子的大小，看皮影离灯和离幕的距离比', 'serif', 40, INK)
    Lx, Ly = 180, 560
    Sx = 1560
    c.rect(Sx, 180, Sx + 24, 940, fill=(225, 220, 200))
    c.text(Sx + 12, 160, '幕布', 'sans', 24, MUTED, 'mm')
    c.ellipse(Lx, Ly, 18, 18, fill=SUN)
    c.text(Lx, Ly + 50, '小灯', 'sans', 24, MUTED, 'mm')
    u = 0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi * 1.5)
    px = 480 + u * 820
    h = 120
    y1, y2 = Ly - h / 2, Ly + h / 2
    k = (Sx - Lx) / (px - Lx)
    s1, s2 = Ly + (y1 - Ly) * k, Ly + (y2 - Ly) * k
    c.poly([(Lx, Ly), (Sx, s1), (Sx, s2)], mix(BG, SUN, 0.12))
    c.line([(Lx, Ly), (Sx, s1)], mix(BG, SUN, 0.6), 2)
    c.line([(Lx, Ly), (Sx, s2)], mix(BG, SUN, 0.6), 2)
    c.rect(px - 8, y1, px + 8, y2, fill=WOOD)
    c.rect(Sx, s1, Sx + 24, s2, fill=(50, 50, 55))
    c.text(px, y1 - 30, '皮影', 'sans', 22, INK, 'mm')
    d1 = px - Lx; D = Sx - Lx
    c.rect(1640, 400, 1890, 720, fill=SHEET, r=12)
    c.text(1765, 440, '离灯', 'sans', 22, MUTED, 'mm')
    c.text(1765, 480, f'{d1 / D * 100:.0f}%', 'mono', 30, INK, 'mm')
    c.text(1765, 550, '影子放大', 'sans', 22, MUTED, 'mm')
    c.text(1765, 600, f'×{k:.1f}', 'mono', 40, SPARK, 'mm')
    c.text(1765, 680, '= 灯到幕 ÷ 灯到皮影', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '小灯发出的光是直的：皮影挡住一块，幕上就留下一块影子'),
                (7.2, 14, '皮影离灯越近，挡住的光张得越开，影子越大'),
                (14.2, 22, '放大倍数等于灯到幕的距离除以灯到皮影的距离：距离减半，影子大一倍')], y=1010)

def _bright(sy, src_top, src_bot, px, py1, py2, Lx, Sx, n=24):
    vis = 0
    for j in range(n):
        sy0 = src_top + (src_bot - src_top) * (j + 0.5) / n
        yy = sy0 + (sy - sy0) * (px - Lx) / (Sx - Lx)
        if not (py1 <= yy <= py2):
            vis += 1
    return vis / n

def b64_blur(c, t, i):
    corner_tag(c, 'B64 · 灯越小，影子越清楚')
    c.text(60, 96, '大灯照出的影子边缘发虚：本影和半影', 'serif', 40, INK)
    Lx, Ly = 220, 560
    Sx = 1500
    size = 6 + 260 * fade(t, 5, 13)
    st, sb = Ly - size / 2, Ly + size / 2
    c.rect(Lx - 14, st, Lx + 14, sb, fill=SUN, r=6)
    px, py1, py2 = 800, 470, 650
    c.rect(px - 8, py1, px + 8, py2, fill=WOOD)
    for sy0, py in ((st, py1), (sb, py1), (st, py2), (sb, py2)):
        ex = Sx
        ey = sy0 + (py - sy0) * (Sx - Lx) / (px - Lx)
        c.line([(Lx, sy0), (ex, ey)], mix(BG, SUN, 0.45), 2)
    for y in range(160, 960, 4):
        b = _bright(y, st, sb, px, py1, py2, Lx, Sx)
        col = mix((40, 40, 45), (240, 235, 215), b)
        c.rect(Sx, y, Sx + 40, y + 4, fill=col)
    # 亮度曲线
    pts = [(1600 + 200 * _bright(y, st, sb, px, py1, py2, Lx, Sx), y) for y in range(160, 960, 8)]
    c.line([(1600, 160), (1600, 960)], LINE, 2)
    c.line(pts, SPARK, 3)
    c.text(1700, 140, '幕上亮度', 'sans', 22, MUTED, 'mm')
    a = fade(t, 13, 14)
    if a > 0:
        c.text(Sx - 20, 560, '本影', 'bold', 24, mix(BG, INK, a), 'rm')
        c.text(Sx - 20, 300, '半影', 'bold', 24, mix(BG, SPARK, a), 'rm')
    c.text(Lx, sb + 40, f'灯的大小：{"小" if size < 60 else ("中" if size < 160 else "大")}', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 5, '灯很小的时候，影子边缘一刀切：要么全被挡住，要么一点没挡'),
                (5.2, 13, '把灯变大：灯的上半边和下半边各投一个影子，两个影子错开'),
                (13.2, 22, '中间全黑的叫本影，边上半明半暗的叫半影：所以皮影戏要用一盏小灯')], y=1010)

# ---------------------------------------------------------------- B65 古琴
NOTES = [(1.0, '全弦', '宫', '×1'), (3 / 4, '3/4 处', '高四度', '×4/3'), (2 / 3, '2/3 处', '高五度', '×3/2'), (1 / 2, '1/2 处', '高八度', '×2')]

def b65_length(c, t, i):
    corner_tag(c, 'B65 · 弦越短，音越高')
    c.text(60, 96, '按住弦的不同位置：振动的那段越短，音越高', 'serif', 40, INK)
    x0, x1, y = 200, 1700, 520
    c.rect(150, y + 40, 1750, y + 120, fill=WOOD, r=10)
    k = min(int(t / 5.5), 3)
    fr, nm, pitch, ratio = NOTES[k]
    xb = x0 + (x1 - x0) * fr
    c.line([(x0, y), (x0, y + 40)], INK, 6)
    c.line([(x1, y), (x1, y + 40)], INK, 6)
    if fr < 1:
        c.poly([(xb - 16, y + 40), (xb + 16, y + 40), (xb, y - 4)], (200, 200, 210))
        c.line([(xb, y), (x1, y)], STR, 3)
    f = 1 / fr
    amp = 40 * math.cos(t * 12 * f)
    pts = [(x0 + (xb - x0) * u / 60, y + amp * math.sin(math.pi * u / 60)) for u in range(61)]
    c.line(pts, STR, 4)
    c.rect(560, 680, 1360, 900, fill=SHEET, r=14)
    c.text(960, 730, f'振动的长度：{nm}', 'bold', 30, INK, 'mm')
    c.text(960, 800, f'频率 {ratio}  →  {pitch}', 'mono', 34, SPARK, 'mm')
    c.text(960, 860, '长度和频率成反比（以调音 App 实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 5.5, '全弦一弹，是最低的那个音'),
                (5.5, 11, '按在四分之三处，振动的弦短了，频率变成 4/3 倍：高一个四度'),
                (11, 16.5, '按在三分之二处，频率 3/2 倍：高一个五度。三分损益法就是这样一截一截算出来的'),
                (16.5, 22, '按在正中间，频率翻倍：高一个八度')], y=1010)

HUI = [1 / 8, 1 / 6, 1 / 5, 1 / 4, 1 / 3, 2 / 5, 1 / 2, 3 / 5, 2 / 3, 3 / 4, 4 / 5, 5 / 6, 7 / 8]

def b65_hui(c, t, i):
    corner_tag(c, 'B65 · 十三个徽位')
    c.text(60, 96, '徽位都在简单分数上：轻点一下，整根弦分几段一起振', 'serif', 40, INK)
    x0, x1, y = 200, 1700, 540
    c.rect(150, y + 30, 1750, y + 110, fill=WOOD, r=10)
    for k, h in enumerate(HUI):
        xx = x0 + (x1 - x0) * h
        c.ellipse(xx, y + 70, 9, 9, fill=(240, 240, 230))
        c.text(xx, y + 140, str(k + 1), 'mono', 20, MUTED, 'mm')
    seq = [(0, 6, 2), (6, 13, 3), (13, 22, 4)]
    n = 2
    for a0, a1, nn in seq:
        if a0 <= t < a1: n = nn
    touch = x0 + (x1 - x0) / n
    amp = 46 * math.cos(t * 12 * n) / (n ** 0.3)
    pts = [(x0 + (x1 - x0) * u / 120, y + amp * math.sin(math.pi * n * u / 120)) for u in range(121)]
    c.line(pts, STR, 4)
    for j in range(1, n):
        c.ellipse(x0 + (x1 - x0) * j / n, y, 8, 8, fill=NRED)
    c.line([(touch, y - 120), (touch, y - 24)], SPARK, 4)
    c.text(touch, y - 150, '轻点', 'bold', 26, SPARK, 'mm')
    names = {2: ('1/2 处（第 7 徽）', '分 2 段：高八度'), 3: ('1/3 处（第 5 徽）', '分 3 段：高八度再加五度'), 4: ('1/4 处（第 4 徽）', '分 4 段：高两个八度')}
    a, b = names[n]
    c.rect(560, 760, 1360, 920, fill=SHEET, r=14)
    c.text(960, 805, a, 'bold', 30, INK, 'mm')
    c.text(960, 870, b, 'sans', 28, SPARK, 'mm')
    caps(c, t, [(0, 6, '古琴面上嵌着十三个圆点，叫徽。正中间的第七徽，在弦长的 1/2 处'),
                (6.2, 13, '手指只轻轻点在 1/3 处，不按到底：弦被分成一样长的三段一起振，这就是泛音'),
                (13.2, 22, '十三个徽全在 1/2、1/3、1/4、1/5 这样的简单分数上：点哪一个，都能弹出干净的泛音')], y=1010)


CLIPS = {
 'B63_平行地轴': (b63_axis, 22), 'B63_十五度': (b63_hours, 22),
 'B63_片头': (titles.opening(BSER, VOL18, SB18, 3, '汉代日晷 · 故宫赤道式日晷'), 7),
 'B63_片尾': (titles.closing(BSER, VOL18, SB18, 3, '下集：同一个皮影，怎么在幕布上忽大忽小？'), 7),
 'B64_远近': (b64_size, 22), 'B64_半影': (b64_blur, 22),
 'B64_片头': (titles.opening(BSER, VOL18, SB18, 4, '宋 ·《东京梦华录》弄影戏'), 7),
 'B64_片尾': (titles.closing(BSER, VOL18, SB18, 4, '下集：古琴弦上为什么有十三个亮点？'), 7),
 'B65_弦长': (b65_length, 22), 'B65_徽位': (b65_hui, 22),
 'B65_片头': (titles.opening(BSER, VOL18, SB18, 5, '《管子 · 地员》三分损益'), 7),
 'B65_片尾': (titles.closing(BSER, VOL18, SB18, 5, '下集：贴着圆墙小声说话，为什么对面听得见？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
