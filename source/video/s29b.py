"""第二十九季（第十一层：家里的机器）第二批：E155 压力锅、E156 电饭煲、E157 电磁炉 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import S29A, SER29, VOL29, METAL, WATER_L

HOTC = (235, 110, 80)
COIL = (210, 150, 80)
MAGNET = (200, 70, 70)
IRONC = (150, 155, 165)


def tboil(p_kpa):
    R, L = 8.314, 40660.0
    return 1 / (1 / 373.15 - R * math.log(p_kpa / 101.325) / L) - 273.15


# ---------------------------------------------------------------- E155 压力锅
def e155_curve(c, t, i):
    corner_tag(c, '第 155 集 · 气压越高，水越难沸腾')
    c.text(60, 96, '水要沸腾，蒸气泡得顶开外面的气压：高原上气压低，不到 100 ℃ 就开；压力锅把气压关高，要 110 多度才开', 'serif', 34, INK)
    gx0, gx1, gy0, gy1 = 240, 1300, 860, 240
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    pmin, pmax, tmin, tmax = 40, 220, 70, 130
    def X(p): return gx0 + (gx1 - gx0) * (p - pmin) / (pmax - pmin)
    def Y(T): return gy0 - (gy0 - gy1) * (T - tmin) / (tmax - tmin)
    for p in (50, 100, 150, 200):
        c.text(X(p), gy0 + 26, f'{p}', 'mono', 18, MUTED, 'mm')
    for T in (80, 100, 120):
        c.text(gx0 - 16, Y(T), f'{T}', 'mono', 18, MUTED, 'rm')
        seg(c, [(gx0, Y(T)), (gx1, Y(T))], mix(BG, LINE, 0.5), 1)
    c.text((gx0 + gx1) / 2, gy0 + 60, '气压（千帕）', 'sans', 20, MUTED, 'mm')
    c.text(gx0, gy1 - 30, '沸点 ℃', 'sans', 20, MUTED, 'mm')
    pts = [(X(p), Y(tboil(p))) for p in range(pmin, pmax + 1, 4)]
    c.line(pts, SPARK, 4)
    marks = [(64, '高原（约 4000 米）'), (101, '海边'), (180, '压力锅')]
    show = min(3, int(t / 5) + 1)
    for k, (p, lab) in enumerate(marks[:show]):
        T = tboil(p)
        c.ellipse(X(p), Y(T), 12, 12, fill=[NRED, GREEN, (120, 180, 240)][k])
        c.text(X(p) + 20, Y(T) - 30, f'{lab}：约 {T:.0f} ℃', 'bold', 22, INK, 'lm')
    c.rect(1380, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 340, '为什么炖得烂', 'bold', 24, INK, 'mm')
    c.text(1620, 410, '温度高 10–20 度，', 'sans', 22, INK, 'mm')
    c.text(1620, 450, '肉里的纤维和胶质', 'sans', 22, INK, 'mm')
    c.text(1620, 490, '软化得快得多', 'sans', 22, INK, 'mm')
    c.text(1620, 580, '（数值由公式估算，拍摄前核对）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '水烧开，是水里冒出的蒸气泡能顶开外面的空气：外面压得越重，水就得越热才行'),
                (7.2, 14, '高原上空气稀薄，气压低，水八十多度就开了，面条煮不熟'),
                (14.2, 22, '压力锅把锅盖封死，蒸气出不去，锅里气压升高，水要一百一十多度才开：东西就熟得快（示意）')], y=1010)


def e155_syringe(c, t, i):
    corner_tag(c, '第 155 集 · 反过来：把气压拉低，温水也能沸腾')
    c.text(60, 96, '注射器吸一点 50 ℃ 的温水，堵住口往外拉活塞：气压一下变低，温水竟冒起大泡「沸腾」了', 'serif', 36, INK)
    pull = 0.5 - 0.5 * math.cos(t / 11 * 2 * math.pi)
    x0, y0 = 400, 520
    L = 600 + 300 * pull
    c.rect(x0, y0 - 80, x0 + 900, y0 + 80, outline=LINE, width=4, r=10)
    c.rect(x0 - 60, y0 - 12, x0, y0 + 12, fill=LINE)
    c.ellipse(x0 - 70, y0, 16, 16, fill=SKINC if False else (225, 180, 150))
    c.text(x0 - 70, y0 + 50, '手指堵住', 'sans', 18, MUTED, 'mm')
    px = x0 + L
    c.rect(px, y0 - 76, px + 20, y0 + 76, fill=METAL)
    c.rect(px + 20, y0 - 10, px + 300, y0 + 10, fill=METAL)
    c.rect(x0 + 4, y0 + 10, x0 + 300, y0 + 76, fill=mix(BG, WATER_L, 0.7))
    P = 101 * 300 / (300 + 3000 * pull)
    boil = tboil(P) < 50
    rnd = random.Random(int(t * 8))
    if boil:
        for k in range(18):
            bx = x0 + 20 + rnd.random() * 270
            by = y0 + 20 + rnd.random() * 50
            c.ellipse(bx, by, 4 + rnd.random() * 10, 4 + rnd.random() * 10, outline=(240, 240, 250), width=2)
    c.rect(1380, 280, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 320, '注射器里', 'bold', 24, INK, 'mm')
    c.text(1620, 390, f'气压约 {P:.0f} 千帕', 'mono', 26, SPARK, 'mm')
    c.text(1620, 450, f'沸点约 {tboil(max(P, 8)):.0f} ℃', 'mono', 26, SPARK, 'mm')
    c.text(1620, 520, '水温 50 ℃', 'mono', 24, INK, 'mm')
    c.text(1620, 590, '沸腾了！' if boil else '还没开', 'bold', 28, GREEN if boil else MUTED, 'mm')
    caps(c, t, [(0, 7, '成年人倒一杯约 50 ℃ 的温水，用不带针头的大注射器吸进 10 毫升，再用手指堵住口'),
                (7.2, 14, '慢慢往外拉活塞，里面的空气被拉稀，气压降得很低'),
                (14.2, 22, '低到一定程度，50 ℃ 的水就冒出大泡「沸腾」：压力锅正是反过来，把气压升高（数值为估算，以实测为准）')], y=1010)


# ---------------------------------------------------------------- E156 电饭煲
def e156_plateau(c, t, i):
    corner_tag(c, '第 156 集 · 有水时，锅底被「卡」在 100 ℃')
    c.text(60, 96, '只要还有水，加再多的热也只是把水变成蒸气，锅底卡在 100 ℃ 左右；水一干，温度往上冲，开关就跳了', 'serif', 36, INK)
    gx0, gx1, gy0, gy1 = 220, 1400, 860, 260
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    def Tof(m):
        if m < 8:
            return 20 + 80 * m / 8
        if m < 20:
            return 100 + 0.2 * (m - 8) / 12
        return 100.2 + 15 * (m - 20)
    def X(m): return gx0 + (gx1 - gx0) * m / 24
    def Y(T): return gy0 - (gy0 - gy1) * (T - 20) / 100
    for T in (20, 60, 100):
        c.text(gx0 - 16, Y(T), f'{T}', 'mono', 18, MUTED, 'rm')
    seg(c, [(gx0, Y(103)), (gx1, Y(103))], NRED, 2)
    c.text(gx0 + 700, Y(103) - 90, '红线：磁钢失磁、开关跳起（约 103 ℃，示意）', 'sans', 20, NRED, 'mm')
    now = min(24, t / 20 * 24)
    pts = []
    m = 0.0
    while m <= now:
        T = min(Tof(m), 106)
        pts.append((X(m), Y(T)))
        m += 0.1
    if len(pts) > 1:
        c.line(pts, SPARK, 4)
    c.text(X(4), Y(60) - 40, '加热', 'bold', 22, INK, 'mm')
    c.text(X(14), Y(100) - 40, '水在沸腾：温度不涨', 'bold', 22, INK, 'mm')
    if now > 20:
        c.text(X(21.5), Y(100) + 50, '水干了！', 'bold', 22, NRED, 'mm')
    c.text((gx0 + gx1) / 2, gy0 + 40, '时间（分钟，示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '成年人烧一锅水，每半分钟测一次温度：一开始一路往上涨'),
                (7.2, 14, '到了 100 ℃ 左右，火再大，温度也不涨了：多的热全拿去把水变成蒸气'),
                (14.2, 22, '电饭煲正是利用这一点：饭里的水被吸干、锅底温度一冲过 100 ℃，它就知道饭好了（示意）')], y=1010)


def e156_magnet(c, t, i):
    corner_tag(c, '第 156 集 · 一块到点就失去磁性的磁钢')
    c.text(60, 96, '锅底中间有一块感温磁钢：按下煮饭键它被磁铁吸住；到了约 103 ℃，磁钢失去磁性，弹簧一推，开关弹开', 'serif', 36, INK)
    T = 20 + 90 * min(1, t / 16)
    lost = T >= 103
    cx = 760
    pan_y = 330
    c.rect(cx - 320, pan_y - 40, cx + 320, pan_y, fill=mix(METAL, HOTC, min(1, max(0, (T - 20) / 90))), r=6)
    c.text(cx + 340, pan_y - 20, '内锅锅底', 'sans', 20, MUTED, 'lm')
    gap = 0 if not lost else min(120, (t - 16 * (83 / 90)) * 200)
    c.rect(cx - 60, pan_y + 10, cx + 60, pan_y + 60, fill=mix(IRONC, HOTC, min(1, (T - 20) / 90)), r=6)
    c.text(cx + 80, pan_y + 35, '感温磁钢', 'sans', 20, INK, 'lm')
    my = pan_y + 70 + gap
    c.rect(cx - 50, my, cx + 50, my + 50, fill=MAGNET, r=6)
    c.text(cx + 70, my + 25, '永磁铁', 'sans', 20, INK, 'lm')
    c.line([(cx, my + 50), (cx, my + 160)], METAL, 6)
    for k in range(6):
        y = my + 160 + k * 16
        c.line([(cx - 20, y), (cx + 20, y + 8)], METAL, 3)
    c.line([(cx, my + 260), (cx - 300, my + 300)], METAL, 8)
    c.text(cx - 320, my + 320, '开关：' + ('煮饭' if not lost else '跳到保温'), 'bold', 24, GREEN if lost else SPARK, 'mm')
    if not lost:
        for k in range(3):
            c.line([(cx - 40 + k * 40, pan_y + 62), (cx - 40 + k * 40, my - 2)], mix(BG, SPARK, 0.6), 2)
    c.rect(1380, 300, 1860, 600, fill=SHEET, r=14)
    c.text(1620, 340, '锅底温度', 'bold', 24, INK, 'mm')
    c.text(1620, 420, f'{T:.0f} ℃', 'mono', 44, NRED if lost else INK, 'mm')
    c.text(1620, 500, '吸住' if not lost else '吸不住了', 'bold', 28, SPARK if not lost else GREEN, 'mm')
    c.text(1620, 560, '（温度为示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '按下煮饭键，下面的永磁铁被推上去，吸住锅底中间那块特别的感温磁钢，电路接通'),
                (7.2, 14, '这种磁钢有个「居里温度」：一到这个温度就突然失去磁性。厂家把它定在 100 ℃ 多一点'),
                (14.2, 22, '有水时锅底到不了这个温度；水一干，温度冲上去，磁铁吸不住了，弹簧一推，开关跳到保温（数值拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- E157 电磁炉
def e157_eddy(c, t, i):
    corner_tag(c, '第 157 集 · 线圈的磁场，在锅底里绕出电流')
    c.text(60, 96, '面板下面是一圈线圈，通着每秒变化几万次的电流；它的磁场穿过锅底，在锅底里感应出一圈圈电流，锅自己就热了', 'serif', 36, INK)
    cx, cy = 760, 640
    c.rect(cx - 420, cy - 20, cx + 420, cy + 10, fill=mix(BG, (60, 60, 70), 0.9), r=6)
    c.text(cx + 440, cy - 5, '面板（玻璃陶瓷）', 'sans', 18, MUTED, 'lm')
    for k in range(8):
        r = 60 + k * 36
        c.ellipse(cx, cy + 90, r, r * 0.22, outline=COIL, width=4)
    c.text(cx + 440, cy + 90, '线圈', 'sans', 20, COIL, 'lm')
    ph = math.sin(t * 6)
    for k in range(-4, 5):
        x = cx + k * 80
        c.arrow(x, cy + 70, x, cy - 120 * (0.6 + 0.4 * abs(ph)), mix(BG, (120, 180, 240), 0.7), 2, 10)
    c.rect(cx - 360, cy - 160, cx + 360, cy - 120, fill=mix(IRONC, HOTC, min(1, t / 16)), r=4)
    c.rect(cx - 360, cy - 400, cx - 340, cy - 160, fill=IRONC)
    c.rect(cx + 340, cy - 400, cx + 360, cy - 160, fill=IRONC)
    c.text(cx, cy - 420, '铁锅', 'bold', 24, INK, 'mm')
    for k in range(4):
        r = 60 + k * 70
        a0 = t * 4 * (1 if ph > 0 else -1)
        pts = [(cx + r * math.cos(a0 + j * 0.2), cy - 140 + r * 0.08 * math.sin(a0 + j * 0.2)) for j in range(32)]
        c.line(pts, SPARK, 3)
    c.rect(1320, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1590, 340, '锅底里的涡流', 'bold', 24, SPARK, 'mm')
    c.text(1590, 410, '电流在金属里绕圈，', 'sans', 22, INK, 'mm')
    c.text(1590, 450, '碰到电阻就发热', 'sans', 22, INK, 'mm')
    c.text(1590, 520, '面板自己不发热，', 'sans', 22, INK, 'mm')
    c.text(1590, 560, '只是被锅烫热', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '电磁炉面板下面没有火、没有电热丝，只有一大盘线圈'),
                (7.2, 14, '线圈里的电流每秒变化几万次，磁场跟着忽大忽小、来回翻转（频率拍摄前核对）'),
                (14.2, 22, '变化的磁场穿过锅底，在锅底里感应出一圈圈电流，叫涡流：电流碰到电阻发热，锅就自己热了（示意）')], y=1010)


def e157_tubes(c, t, i):
    corner_tag(c, '第 157 集 · 磁铁穿过铝管，慢得像在油里')
    c.text(60, 96, '同一块小磁铁：塑料管里一下掉到底，铝管、铜管里却慢慢往下飘——管壁里的涡流，用自己的磁场托住了它', 'serif', 34, INK)
    tubes = [('塑料管', 0.45, (180, 180, 190)), ('铝管', 4.0, (200, 205, 215)), ('铜管', 6.0, (210, 150, 90))]
    top, bot = 220, 860
    for k, (nm, T, col) in enumerate(tubes):
        x = 380 + k * 420
        c.rect(x - 40, top, x + 40, bot, outline=col, width=8, r=6)
        tt = t % 8
        frac = min(1, tt / T) if T > 1 else min(1, (tt / T) ** 2)
        y = top + 20 + (bot - top - 60) * frac
        c.rect(x - 24, y, x + 24, y + 40, fill=MAGNET, r=4)
        if nm != '塑料管' and frac < 1:
            for d in (-1, 1):
                c.ellipse(x, y + 20 + d * 50, 46, 10, outline=mix(BG, SPARK, 0.7), width=2)
        c.text(x, bot + 40, nm, 'bold', 24, INK, 'mm')
        c.text(x, bot + 80, f'约 {T:g} 秒落到底（示意）', 'sans', 18, MUTED, 'mm')
    c.rect(1460, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1660, 340, '为什么铜管最慢', 'bold', 24, INK, 'mm')
    c.text(1660, 410, '铜导电更好，', 'sans', 22, INK, 'mm')
    c.text(1660, 450, '涡流更大', 'sans', 22, INK, 'mm')
    c.text(1660, 520, '电磁炉用铁锅，', 'sans', 22, INK, 'mm')
    c.text(1660, 560, '因为铁还会被磁化', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '一块小钕磁铁（远离手机和银行卡），分别从 1 米长的塑料管、铝管、铜管里放下'),
                (7.2, 14, '塑料管里一下就掉到底；铝管和铜管里，它像掉进了蜂蜜，要好几秒才慢慢落下来'),
                (14.2, 22, '磁铁下落时，管壁里感应出涡流，涡流自己的磁场又反过来顶住磁铁：电磁炉里的涡流，就变成了热（时间以实测为准）')], y=1010)


CLIPS = {
 'E155_沸点': (e155_curve, 22), 'E155_注射器': (e155_syringe, 22),
 'E155_片头': (titles.opening(SER29, VOL29, S29A, 3, '1679 年帕潘发明高压蒸煮器'), 7),
 'E155_片尾': (titles.closing(SER29, VOL29, S29A, 3, '下集：电饭煲里没人看着，饭一熟它为什么就自己跳到保温？'), 7),
 'E156_沸点平台': (e156_plateau, 22), 'E156_磁钢': (e156_magnet, 22),
 'E156_片头': (titles.opening(SER29, VOL29, S29A, 4, '1955 年自动电饭煲问世'), 7),
 'E156_片尾': (titles.closing(SER29, VOL29, S29A, 4, '下集：电磁炉面板自己不烫，为什么铁锅放上去就热了？'), 7),
 'E157_涡流': (e157_eddy, 22), 'E157_磁铁下落': (e157_tubes, 22),
 'E157_片头': (titles.opening(SER29, VOL29, S29A, 5, '1970 年代家用电磁炉出现'), 7),
 'E157_片尾': (titles.closing(SER29, VOL29, S29A, 5, '下集：吸尘器的力气从哪来？灰尘是被谁推进去的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
