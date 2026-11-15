"""第五十七季（第二十五层：露营）第三批：E298 登山杖、E299 吊床、E300 头灯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s57a import S57A, SER57, VOL57, WARM, COOL, POLE

TUBE = (150, 160, 175)
ROPE = (200, 170, 120)
TREE = (120, 90, 60)
LIGHT = (250, 230, 140)


# ---------------------------------------------------------------- E298 登山杖
def e298_clamp(c, t, i):
    corner_tag(c, '第 298 集 · 锁扣把外管箍紧')
    c.text(60, 96, '登山杖的细管插在粗管里能滑动；扳下锁扣，外管被箍紧，紧紧压在里管上，两根管子之间就有了很大的摩擦力', 'serif', 36, INK)
    cx = 960
    locked = t > 7.2
    slide = 0 if locked else min(180, t * 40)
    # 内管固定在地上，外管被往下压
    c.rect(cx - 48, 420, cx + 48, 900, fill=mix(BG, TUBE, 0.7), r=8)
    c.rect(cx - 70, 240 + slide, cx + 70, 600 + slide, fill=mix(BG, TUBE, 1.0), r=10)
    if slide:
        c.text(cx + 120, 300 + slide, '外管滑下去', 'sans', 24, MUTED, 'lm')
    # 锁扣
    sq = 10 if locked else 0
    c.rect(cx - 90 + sq, 540 + slide, cx - 70 + sq, 600 + slide, fill=mix(BG, SPARK, 1.0), r=4)
    c.rect(cx + 70 - sq, 540 + slide, cx + 90 - sq, 600 + slide, fill=mix(BG, SPARK, 1.0), r=4)
    if locked:
        c.arrow(cx - 180, 570, cx - 95, 570, NRED, 6, 16)
        c.arrow(cx + 180, 570, cx + 95, 570, NRED, 6, 16)
        c.text(cx + 330, 570, '箍紧的压力', 'bold', 28, NRED, 'mm')
        c.arrow(cx, 760, cx, 640, GREEN, 6, 18)
        c.text(cx + 260, 700, '摩擦力往上撑住', 'bold', 28, GREEN, 'mm')
        c.text(cx, 960, '锁住了：压下去也不缩', 'bold', 30, GREEN, 'mm')
    else:
        c.text(cx, 960, '没锁：外管一压就滑下去', 'bold', 30, NRED, 'mm')
    c.arrow(cx, 160 + slide, cx, 230 + slide, INK, 6, 18)
    c.text(cx + 120, 180, '人往下压', 'sans', 26, MUTED, 'lm')
    caps(c, t, [(0, 7, '锁扣松开：里管在外管里一压就滑进去'),
                (7.2, 14, '扳下锁扣：外管被箍紧，紧紧压住里管'),
                (14.2, 22, '压得越紧，两根管子之间的摩擦越大，撑住人往下压的力')], y=1010)


def e298_friction(c, t, i):
    corner_tag(c, '第 298 集 · 箍得越紧，挂得越重')
    c.text(60, 96, '用粗细两根吸管和长尾夹做实验：不夹一碰就滑，小夹子能挂一点水，大夹子箍得更紧，能挂住的水更多', 'serif', 36, INK)
    data = [('不夹', 0.05, NRED), ('小夹子', 0.45, SPARK), ('大夹子', 1.0, GREEN)]
    for j, (lab, v, col) in enumerate(data):
        cx = 420 + j * 540
        c.rect(cx - 26, 220, cx + 26, 520, fill=mix(BG, TUBE, 1.0), r=8)
        c.rect(cx - 16, 460, cx + 16, 700, fill=mix(BG, TUBE, 0.7), r=6)
        if j > 0:
            w = 30 + 20 * j
            c.rect(cx - w, 470, cx + w, 510, fill=mix(BG, POLE, 1.0), r=6)
        c.line([(cx, 700), (cx, 760)], INK, 3)
        k = min(1.0, t / 14)
        h = 140 * v * k
        c.rect(cx - 60, 760, cx + 60, 900, outline=MUTED, width=3, r=10)
        c.rect(cx - 56, 896 - h, cx + 56, 896, fill=mix(BG, COOL, 0.8), r=8)
        c.text(cx, 950, lab, 'bold', 30, col, 'mm')
    c.text(960, 180, '往小瓶里慢慢加水，记下吸管滑下去时加了多少（示意，以实测为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '细吸管插在粗吸管里，下面挂一个小瓶，往瓶里慢慢加水'),
                (7.2, 14, '不夹：几乎一加水就滑下去'),
                (14.2, 22, '夹子箍得越紧，压力越大，摩擦越大，能挂住的水越多')], y=1010)


# ---------------------------------------------------------------- E299 吊床
def hammock(c, x0, x1, ty, sag, w):
    mid = (x0 + x1) / 2
    pts = []
    for j in range(41):
        s = j / 40
        x = x0 + (x1 - x0) * s
        y = ty + sag * (1 - (2 * s - 1) ** 2)
        pts.append((x, y))
    seg(c, pts, ROPE, 6)
    c.rect(mid - 40, ty + sag - 10, mid + 40, ty + sag + 50, fill=mix(BG, COOL, 0.9), r=10)
    return pts


def e299_angle(c, t, i):
    corner_tag(c, '第 299 集 · 绳子越平，拉力越大')
    c.text(60, 96, '人的重量靠两边绳子往上托：绳子越平，往上托的劲越小，只好用更大的拉力去凑', 'serif', 36, INK)
    x0, x1, ty = 360, 1560, 360
    c.rect(x0 - 60, 240, x0 - 20, 900, fill=mix(BG, TREE, 1.0))
    c.rect(x1 + 20, 240, x1 + 60, 900, fill=mix(BG, TREE, 1.0))
    k = (t % 22) / 22
    sag = 30 + 260 * (0.5 + 0.5 * math.cos(k * 2 * math.pi))
    hammock(c, x0, x1, ty, sag, 1)
    half = (x1 - x0) / 2
    ang = math.atan2(2 * sag, half)
    T = 1 / (2 * math.sin(ang))
    c.text(960, 780, f'绳子和水平夹角约 {math.degrees(ang):.0f}°', 'mono', 30, INK, 'mm')
    c.text(960, 840, f'每边绳子的拉力约是体重的 {T:.1f} 倍', 'bold', 32, NRED if T > 1.5 else GREEN, 'mm')
    c.rect(1640, 300, 1700, 300 + min(560, T * 120), fill=mix(BG, NRED if T > 1.5 else GREEN, 0.8), r=6)
    c.text(1670, 270, '拉力', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '绳子下垂得多：两边绳子斜着往上托，拉力不大'),
                (7.2, 14, '把绳子越拉越平：角度变小，拉力一下子涨上去'),
                (14.2, 22, '绳子几乎拉平时，拉力能是体重的好几倍：绳子和树枝都受不了')], y=1010)


def e299_sag(c, t, i):
    corner_tag(c, '第 299 集 · 留一点下垂最安全')
    c.text(60, 96, '用两把椅子、一根细绳、弹簧秤和一瓶水来量：绳子越平读数越大，下垂 10 厘米、20 厘米，读数小了很多', 'serif', 36, INK)
    data = [(2, '下垂 2 厘米'), (10, '下垂 10 厘米'), (20, '下垂 20 厘米')]
    for j, (cm, lab) in enumerate(data):
        y0 = 260 + j * 220
        x0, x1 = 300, 1300
        c.rect(x0 - 30, y0 - 30, x0, y0 + 60, fill=mix(BG, TREE, 1.0))
        c.rect(x1, y0 - 30, x1 + 30, y0 + 60, fill=mix(BG, TREE, 1.0))
        sag = cm * 5
        mid = (x0 + x1) / 2
        seg(c, [(x0, y0), (mid, y0 + sag), (x1, y0)], ROPE, 5)
        c.rect(mid - 20, y0 + sag, mid + 20, y0 + sag + 40, fill=mix(BG, COOL, 0.9), r=6)
        ang = math.atan2(cm, 75)
        T = 3.0 / (2 * math.sin(ang))
        if t > 3 + j * 4:
            c.text(1420, y0 + 10, lab, 'sans', 26, MUTED, 'lm')
            c.text(1420, y0 + 50, f'约 {T:.0f} 牛', 'bold', 30, NRED if T > 6 else GREEN, 'lm')
    c.text(960, 940, '300 毫升水约 3 牛；数值按 1.5 米绳子估算，以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '绳子几乎拉平：弹簧秤读数比水瓶的重量大很多倍'),
                (7.2, 14, '让绳子下垂 10 厘米：读数一下小了很多'),
                (14.2, 22, '真吊床也要留下垂，离地不超过膝盖高度，有大人在旁')], y=1010)


# ---------------------------------------------------------------- E300 头灯
def e300_reflector(c, t, i):
    corner_tag(c, '第 300 集 · 反光碗把光聚成一束')
    c.text(60, 96, '小灯珠的光本来往四面八方散；后面的碗形反光面把往后、往旁边跑的光都反射到正前方，光就聚成了一束', 'serif', 36, INK)
    cy = 560
    for j in range(2):
        cx = 380 + 0 * j
        yy = 330 + j * 420
        has = j == 0
        if has:
            pts = []
            for k in range(41):
                y = -150 + 300 * k / 40
                x = (y * y) / 300
                pts.append((cx - 75 + x, yy + y))
            seg(c, pts, mix(BG, (210, 215, 225), 1.0), 8)
        c.ellipse(cx, yy, 14, 14, fill=mix(BG, LIGHT, 1.0))
        n = 14
        for k in range(n):
            ph = (t * 0.6 + k / n) % 1
            if has:
                y = -130 + 260 * (k / (n - 1))
                x0 = cx - 75 + y * y / 300
                c.line([(cx, yy), (x0, yy + y)], mix(BG, LIGHT, 0.25), 2)
                for d in (0, 0.33, 0.66):
                    q = (ph + d) % 1
                    c.ellipse(x0 + q * 1300, yy + y, 6, 6, fill=mix(BG, LIGHT, 1 - 0.5 * q))
                continue
            else:
                a = 2 * math.pi * k / n
                px, py = cx + ph * 420 * math.cos(a), yy + ph * 170 * math.sin(a)
            c.ellipse(px, py, 7, 7, fill=mix(BG, LIGHT, 1 - 0.5 * ph))
        c.text(1500, yy - 120 if has else yy - 150, ['有反光碗：光成一束，照得远', '没有反光碗：光四散，照不远'][j], 'bold', 28, GREEN if has else NRED, 'mm')
    caps(c, t, [(0, 7, '上面：灯珠后面有一个碗形的反光面；下面：只有灯珠'),
                (7.2, 14, '没有反光碗，一大半的光往后、往旁边跑掉了'),
                (14.2, 22, '反光碗把这些光都转向正前方：一束光照得又远又亮')], y=1010)


def e300_focus(c, t, i):
    corner_tag(c, '第 300 集 · 灯珠要放在焦点上')
    c.text(60, 96, '反光碗有一个特别的点叫焦点：灯珠正好在焦点上，反射出去的光平平地往前走；放偏了，光就散开或交叉', 'serif', 36, INK)
    cx, cy = 380, 560
    pts = []
    for k in range(41):
        y = -220 + 440 * k / 40
        x = (y * y) / 400
        pts.append((cx + x, cy + y))
    seg(c, pts, mix(BG, (210, 215, 225), 1.0), 8)
    f = 100
    off = 0 if 7.2 <= t < 14.2 else (-60 if t < 7.2 else 70)
    lx = cx + f + off
    c.ellipse(lx, cy, 14, 14, fill=mix(BG, LIGHT, 1.0))
    c.line([(cx + f, cy - 20), (cx + f, cy + 20)], MUTED, 2)
    c.text(cx + f, cy + 50, '焦点', 'sans', 22, MUTED, 'mm')
    for k in range(9):
        y = -200 + 400 * k / 8
        if abs(y) < 30:
            continue
        x = y * y / 400
        px, py = cx + x, cy + y
        c.line([(lx, cy), (px, py)], mix(BG, LIGHT, 0.6), 2)
        # 法线方向
        nx, ny = 1, -2 * y / 400
        L = math.hypot(nx, ny); nx, ny = nx / L, ny / L
        dx, dy = px - lx, py - cy
        L = math.hypot(dx, dy); dx, dy = dx / L, dy / L
        dot = dx * nx + dy * ny
        rx, ry = dx - 2 * dot * nx, dy - 2 * dot * ny
        c.line([(px, py), (px + rx * 1200, py + ry * 1200)], mix(BG, LIGHT, 0.8), 3)
    lab = '灯珠太靠里：光往外散' if t < 7.2 else ('灯珠在焦点上：光平行往前' if t < 14.2 else '灯珠太靠外：光交叉后散开')
    c.text(1250, 230, lab, 'bold', 30, GREEN if 7.2 <= t < 14.2 else NRED, 'mm')
    caps(c, t, [(0, 7, '灯珠放得太靠里：反射出去的光往外张开'),
                (7.2, 14, '灯珠正好在焦点上：光平行地往前走，一束照得最远'),
                (14.2, 22, '放得太靠外：光先交叉再散开；用 1.5 伏小手电试，别直照眼睛')], y=1010)


CLIPS = {
 'E298_箍紧': (e298_clamp, 22), 'E298_摩擦': (e298_friction, 22),
 'E298_片头': (titles.opening(SER57, VOL57, S57A, 6, '能伸缩的登山杖'), 7),
 'E298_片尾': (titles.closing(SER57, VOL57, S57A, 6, '下集：吊床绳子拉得太平为什么危险？'), 7),
 'E299_角度': (e299_angle, 22), 'E299_下垂': (e299_sag, 22),
 'E299_片头': (titles.opening(SER57, VOL57, S57A, 7, '挂在两棵树之间的吊床'), 7),
 'E299_片尾': (titles.closing(SER57, VOL57, S57A, 7, '下集：头灯里的反光碗是干什么的？'), 7),
 'E300_反光': (e300_reflector, 22), 'E300_焦点': (e300_focus, 22),
 'E300_片头': (titles.opening(SER57, VOL57, S57A, 8, '头灯和手电筒里的反光碗'), 7),
 'E300_片尾': (titles.closing(SER57, VOL57, S57A, 8, '下集：荧光棒不用电，光从哪来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
