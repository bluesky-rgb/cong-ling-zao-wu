"""第二十五季（第九层：看见身体）第一批：E132 听诊器、E133 血压计、E134 近视眼镜 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S25A = [('132', '听诊器'), ('133', '血压计'), ('134', '近视眼镜'), ('135', 'X 光'), ('136', '超声检查'),
        ('137', '人工耳蜗'), ('138', '起搏器'), ('139', '核磁共振'), ('140', 'DNA'), ('141', '微创手术')]
SER25, VOL25 = '从零造物', '第二十五季 · 第九层：看见身体'
SKINC = (225, 185, 160)
HEART = (210, 70, 80)
TUBE = (150, 160, 175)
SOUND = (120, 180, 230)
BLOOD = (200, 50, 60)
CUFF = (90, 120, 170)
EYE = (235, 235, 230)
LENSC = (150, 200, 240)
RAY = (250, 220, 120)


# ---------------------------------------------------------------- E132 听诊器
def e132_spread(c, t, i):
    corner_tag(c, '第 132 集 · 把心跳关进管子里')
    c.text(60, 96, '在空气里，心跳的声音向四面八方散开；在管子里，它只能沿着管子走到耳朵', 'serif', 40, INK)
    for k, tube in enumerate((False, True)):
        hx, hy = 300 + k * 900, 620
        c.ellipse(hx, hy, 50, 44, fill=HEART)
        c.text(hx, hy + 90, '心跳', 'bold', 24, INK, 'mm')
        ex, ey = hx + 560, hy
        c.ellipse(ex, ey, 36, 50, fill=SKINC)
        c.text(ex, ey + 90, '耳朵', 'bold', 24, INK, 'mm')
        beat = (t * 1.2) % 1
        if not tube:
            for j in range(4):
                r = ((beat + j / 4) % 1) * 520
                c.ellipse(hx, hy, r, r, outline=mix(BG, SOUND, 1 - r / 520), width=3)
            c.text(hx + 280, 300, '散到四面八方', 'bold', 28, NRED, 'mm')
            c.rect(hx + 120, 820, hx + 120 + 60, 850, fill=NRED)
            c.text(hx + 200, 835, '到耳朵的声音：很小', 'sans', 22, INK, 'lm')
        else:
            c.rect(hx + 60, hy - 30, ex - 40, hy + 30, outline=TUBE, width=5, r=10)
            for j in range(4):
                x = hx + 60 + ((beat + j / 4) % 1) * (ex - hx - 100)
                c.line([(x, hy - 24), (x, hy + 24)], SOUND, 4)
            c.text(hx + 280, 300, '只能沿着管子走', 'bold', 28, GREEN, 'mm')
            c.rect(hx + 120, 820, hx + 120 + 300, 850, fill=GREEN)
            c.text(hx + 440, 835, '很大（示意）', 'sans', 22, INK, 'lm')
    caps(c, t, [(0, 7, '心跳的声音很轻，从胸口传出来，马上向四面八方散开，到耳朵时只剩一点点'),
                (7.2, 14, '一八一六年，有位医生把一卷纸贴在病人胸口：声音被关在纸筒里，只能沿着它走'),
                (14.2, 22, '听诊器没有把声音放大，只是不让它散掉：管子密封、贴紧皮肤，听得最清楚（年代拍摄前核对）')], y=1010)


def e132_diaphragm(c, t, i):
    corner_tag(c, '第 132 集 · 一张薄膜，推动一管空气')
    c.text(60, 96, '听诊器头上的薄膜被心跳推得一颤一颤，推动管子里的空气，一路推到耳朵', 'serif', 40, INK)
    cx, cy = 400, 600
    c.rect(0, cy + 60, 1920, cy + 200, fill=SKINC)
    c.text(140, cy + 130, '胸口', 'sans', 24, INK, 'mm')
    beat = math.sin(t * 2 * math.pi * 1.2)
    push = max(0.0, beat) ** 3
    c.ellipse(cx, cy + 140, 50, 30, fill=HEART)
    pts = [(cx - 120 + j * 10, cy + 40 - 18 * push * math.sin(math.pi * j / 24)) for j in range(25)]
    c.line(pts, (220, 220, 230), 5)
    c.poly([(cx - 130, cy + 40), (cx + 130, cy + 40), (cx + 60, cy - 40), (cx - 60, cy - 40)], TUBE)
    path = [(cx, cy - 40), (cx, cy - 200), (cx + 300, cy - 300), (cx + 800, cy - 300), (cx + 1100, cy - 200)]
    c.line(path, TUBE, 22)
    c.line(path, BG, 10)
    seglen = []
    tot = 0
    for a, b in zip(path, path[1:]):
        L = math.hypot(b[0] - a[0], b[1] - a[1]); seglen.append(L); tot += L
    for j in range(16):
        s = ((t * 0.5 + j / 16) % 1) * tot
        for (a, b), L in zip(zip(path, path[1:]), seglen):
            if s <= L:
                u = s / L
                x, y = a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u
                dens = 0.5 + 0.5 * math.sin(j * 1.3 - t * 7.5)
                c.ellipse(x, y, 4 + 3 * dens, 4 + 3 * dens, fill=mix(BG, SOUND, 0.4 + 0.6 * dens))
                break
            s -= L
    c.ellipse(cx + 1140, cy - 200, 40, 56, fill=SKINC)
    c.text(cx + 1140, cy - 110, '耳朵', 'bold', 24, INK, 'mm')
    c.rect(1380, 560, 1860, 860, fill=SHEET, r=14)
    c.text(1620, 600, '两种听诊头', 'bold', 26, INK, 'mm')
    c.text(1420, 670, '膜片面：贴紧，听高一点的音', 'sans', 22, INK, 'lm')
    c.text(1420, 720, '钟形面：轻放，听低沉的音', 'sans', 22, INK, 'lm')
    c.text(1420, 790, '（心音、呼吸音各有不同）', 'sans', 20, MUTED, 'lm')
    caps(c, t, [(0, 7, '心脏一跳，胸口跟着轻轻一颤，贴在上面的薄膜也被推得一颤'),
                (7.2, 14, '薄膜推着管子里的空气，一疏一密地往前传，一直传进耳朵'),
                (14.2, 22, '管子要密封、不漏气，听诊头要贴紧：漏一点缝，声音就跑掉一大半')], y=1010)


# ---------------------------------------------------------------- E133 血压计
def e133_cuff(c, t, i):
    corner_tag(c, '第 133 集 · 压住，再慢慢松开')
    c.text(60, 96, '袖带先把血管压扁，再慢慢放气：第一声「咚」是高压，声音消失时是低压', 'serif', 40, INK)
    gx0, gx1, gy0, gy1 = 160, 1400, 820, 260
    def Y(p):
        return gy0 - (p - 40) / (180 - 40) * (gy0 - gy1)
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    for p in (60, 80, 100, 120, 140, 160):
        c.text(gx0 - 12, Y(p), str(p), 'mono', 18, MUTED, 'rm')
        c.line([(gx0, Y(p)), (gx1, Y(p))], mix(BG, LINE, 0.4), 1)
    c.text(gx0 - 12, gy1 - 40, '毫米汞柱', 'sans', 18, MUTED, 'rm')
    T = 22.0
    pts_b, pts_c = [], []
    cuff_now = 170 - 110 * min(1, t / T)
    for j in range(401):
        tt = T * j / 400
        if tt > t:
            break
        x = gx0 + (gx1 - gx0) * tt / T
        ph = (tt * 1.1) % 1
        bp = 80 + 40 * (math.sin(ph * math.pi) ** 2 if ph < 0.5 else math.sin(ph * math.pi) ** 6)
        pts_b.append((x, Y(bp)))
        pts_c.append((x, Y(170 - 110 * tt / T)))
    if len(pts_b) > 1:
        c.line(pts_b, BLOOD, 3)
        c.line(pts_c, CUFF, 5)
    c.line([(gx0, Y(120)), (gx1, Y(120))], mix(BG, NRED, 0.5), 2)
    c.line([(gx0, Y(80)), (gx1, Y(80))], mix(BG, GREEN, 0.5), 2)
    if cuff_now > 120:
        st1, st2, col = '比高压还高：血管压扁', '没有声音', MUTED
    elif cuff_now > 80:
        st1, st2, col = '在高压和低压之间', '血一股股冲过：咚、咚', SPARK
    else:
        st1, st2, col = '比低压还低：血流顺畅', '声音消失', GREEN
    c.rect(1460, 260, 1860, 640, fill=SHEET, r=14)
    c.text(1660, 300, '袖带压力', 'bold', 24, INK, 'mm')
    c.text(1660, 360, f'{cuff_now:.0f}', 'mono', 48, CUFF, 'mm')
    c.text(1660, 450, st1, 'sans', 22, col, 'mm')
    c.text(1660, 490, st2, 'sans', 22, col, 'mm')
    c.text(1660, 580, '红线 120：高压  绿线 80：低压（示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '红线是血管里的压力：心脏一挤，冲到最高；心脏放松，落到最低'),
                (7.2, 14, '蓝线是袖带的压力：先打得比最高还高，把血管压扁，再一点点放气'),
                (14.2, 22, '袖带刚低过最高值，血就一股股冲过去，发出「咚」声；低过最低值，血流顺了，声音就没了（数值为示意）')], y=1010)


def e133_column(c, t, i):
    corner_tag(c, '第 133 集 · 「120」是什么意思')
    c.text(60, 96, '血压 120 毫米汞柱：血管里的压力，能把一根水银柱顶起 12 厘米高', 'serif', 40, INK)
    base = 880
    k = fade(t, 2, 8)
    hm = 120 * 2.0 * k
    c.rect(400, base - 300, 460, base, outline=TUBE, width=4)
    if hm > 3:
        c.rect(404, base - hm, 456, base - 2, fill=(190, 190, 200))
    c.text(430, base + 40, '水银', 'bold', 24, INK, 'mm')
    c.text(480, base - hm, f'{hm / 2:.0f} 毫米', 'mono', 22, INK, 'lm')
    kw = fade(t, 9, 16)
    hw = 640 * kw
    c.rect(900, base - 680, 960, base, outline=TUBE, width=4)
    if hw > 3:
        c.rect(904, base - hw, 956, base - 2, fill=mix(BG, (90, 150, 220), 0.9))
    c.text(930, base + 40, '水', 'bold', 24, INK, 'mm')
    c.text(980, base - hw, f'约 {1.63 * kw:.1f} 米', 'mono', 22, INK, 'lm')
    c.rect(1300, 300, 1860, 660, fill=SHEET, r=14)
    c.text(1580, 340, '同样的压力', 'bold', 26, INK, 'mm')
    c.text(1340, 420, '顶起 12 厘米水银', 'sans', 24, INK, 'lm')
    c.text(1340, 480, '或者 1.6 米多的水（水轻得多）', 'sans', 24, INK, 'lm')
    c.text(1340, 560, '所以老血压计用水银，柱子短', 'sans', 22, MUTED, 'lm')
    c.text(1340, 610, '今天多用电子血压计', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '血压的单位「毫米汞柱」，原来是老式血压计里水银柱的高度'),
                (7.2, 14, '120 毫米汞柱，就是能把水银顶起 12 厘米；换成水，要顶起一米六还多'),
                (14.2, 22, '水银比水重十三倍多，所以用它做柱子，血压计才不用两层楼那么高（数字拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- E134 近视眼镜
def _eye(c, cx, cy, L, lens_x, focus_x, label, extra=None):
    c.ellipse(cx + L / 2 - 60, cy, L / 2, 150, outline=EYE, width=4)
    rx = cx + L - 60
    c.line([(rx, cy - 130), (rx, cy + 130)], NRED, 6)
    c.ellipse(lens_x, cy, 18, 70, fill=LENSC)
    for dy in (-60, 0, 60):
        start = extra[0] if extra else 40
        c.line([(start, cy + dy), (lens_x, cy + dy)], RAY, 2)
        if extra:
            pass
        c.line([(lens_x, cy + dy), (focus_x, cy)], RAY, 2)
        if focus_x < rx:
            ddx = rx - focus_x
            k = ddx / (focus_x - lens_x)
            c.line([(focus_x, cy), (rx, cy - dy * k)], mix(BG, RAY, 0.6), 2)
    c.ellipse(focus_x, cy, 8, 8, fill=SPARK)
    c.text(cx + L / 2, cy - 190, label, 'bold', 26, INK, 'mm')


def e134_myopia(c, t, i):
    corner_tag(c, '第 134 集 · 焦点落在了视网膜前面')
    c.text(60, 96, '近视的眼球偏长：远处来的光聚得太早，到视网膜上已经散开成一团', 'serif', 40, INK)
    rows = [('正常眼：光正好聚在视网膜上', 420, 360), ('近视眼：眼球长了，焦点落在前面', 560, 360)]
    for k, (nm, L, fx) in enumerate(rows):
        cy = 380 + k * 360
        cx = 520
        lens_x = cx + 40
        c.ellipse(cx + L / 2 - 20, cy, L / 2, 140, outline=EYE, width=4)
        rx = cx + L - 20 + 0
        rx = cx + L / 2 - 20 + L / 2
        c.line([(rx, cy - 120), (rx, cy + 120)], NRED, 6)
        c.text(rx + 20, cy - 120, '视网膜', 'sans', 20, NRED, 'lm')
        c.ellipse(lens_x, cy, 16, 70, fill=LENSC)
        focus = lens_x + fx
        for dy in (-60, -20, 20, 60):
            c.line([(100, cy + dy), (lens_x, cy + dy)], RAY, 2)
            c.line([(lens_x, cy + dy), (focus, cy)], RAY, 2)
            if rx > focus + 2:
                kk = (rx - focus) / (focus - lens_x)
                c.line([(focus, cy), (rx, cy - dy * kk)], mix(BG, RAY, 0.6), 2)
        c.ellipse(focus, cy, 7, 7, fill=SPARK)
        blur = abs(rx - focus) * 60 / fx
        c.rect(1400, cy - 80, 1700, cy + 80, fill=SHEET, r=10)
        c.ellipse(1550, cy, 6 + blur, 6 + blur, fill=mix(SHEET, RAY, 0.9 if blur < 3 else 0.5))
        c.text(1550, cy + 110, '视网膜上看到的远处的一点', 'sans', 18, MUTED, 'mm')
        c.text(560, cy - 175, nm, 'bold', 26, INK, 'lm')
    caps(c, t, [(0, 7, '远处的东西发来的光，几乎是平行的；眼睛里的晶状体把它们聚到视网膜上的一点'),
                (7.2, 14, '近视的人，眼球往往长得偏长：光聚得太早，还没到视网膜就交叉了'),
                (14.2, 22, '到了视网膜上，一点已经散成了一团，远处就看模糊了（示意）')], y=1010)


def e134_fix(c, t, i):
    corner_tag(c, '第 134 集 · 先散开一点，再聚到位')
    c.text(60, 96, '凹透镜中间薄、边上厚：把光先散开一点，眼睛再聚，焦点就退回到视网膜上', 'serif', 40, INK)
    cy = 580
    cx = 620
    L = 560
    rx = cx + L
    lens_x = cx + 40
    c.ellipse(cx + L / 2, cy, L / 2, 150, outline=EYE, width=4)
    c.line([(rx, cy - 130), (rx, cy + 130)], NRED, 6)
    c.text(rx + 20, cy - 130, '视网膜', 'sans', 20, NRED, 'lm')
    c.ellipse(lens_x, cy, 16, 70, fill=LENSC)
    on = fade(t, 6, 10)
    gx = 380
    if on > 0:
        c.poly([(gx - 30, cy - 110), (gx + 30, cy - 110), (gx + 8, cy), (gx + 30, cy + 110), (gx - 30, cy + 110), (gx - 8, cy)], mix(BG, LENSC, on))
        c.text(gx, cy + 150, '近视眼镜（凹透镜）', 'bold', 22, mix(BG, INK, on), 'mm')
    f0 = 440
    f = f0 + (L - 40 - f0) * on
    focus = lens_x + f
    for dy in (-50, -15, 15, 50):
        spread = 1 + 0.35 * on
        c.line([(80, cy + dy), (gx, cy + dy)], RAY, 2)
        c.line([(gx, cy + dy), (lens_x, cy + dy * spread)], RAY, 2)
        c.line([(lens_x, cy + dy * spread), (focus, cy)], RAY, 2)
        if rx > focus + 2:
            kk = (rx - focus) / (focus - lens_x)
            c.line([(focus, cy), (rx, cy - dy * spread * kk)], mix(BG, RAY, 0.6), 2)
    c.ellipse(focus, cy, 7, 7, fill=SPARK)
    c.rect(1420, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1640, 340, '两种眼镜', 'bold', 26, INK, 'mm')
    c.text(1460, 420, '近视：凹透镜（中间薄）', 'sans', 22, INK, 'lm')
    c.text(1460, 470, '把光散开，焦点往后挪', 'sans', 22, MUTED, 'lm')
    c.text(1460, 540, '老花、远视：凸透镜（中间厚）', 'sans', 22, INK, 'lm')
    c.text(1460, 590, '帮眼睛多聚一点光', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '近视的眼睛聚光聚得太早：光还没到视网膜，就已经交叉了'),
                (7.2, 14, '在眼睛前面放一片凹透镜，它让平行的光先微微散开'),
                (14.2, 22, '眼睛再去聚它，就要多走一段路：焦点刚好退回到视网膜上，远处就清楚了（示意）')], y=1010)


CLIPS = {
 'E132_管子': (e132_spread, 22), 'E132_膜片': (e132_diaphragm, 22),
 'E132_片头': (titles.opening(SER25, VOL25, S25A, 0, '1816 年纸筒听诊 · 双耳听诊器'), 7),
 'E132_片尾': (titles.closing(SER25, VOL25, S25A, 0, '下集：袖带一放气，怎么就量出了血压？'), 7),
 'E133_袖带': (e133_cuff, 22), 'E133_汞柱': (e133_column, 22),
 'E133_片头': (titles.opening(SER25, VOL25, S25A, 1, '1896 年袖带血压计 · 1905 年柯氏音'), 7),
 'E133_片尾': (titles.closing(SER25, VOL25, S25A, 1, '下集：近视的人戴上眼镜，为什么远处就看清了？'), 7),
 'E134_近视': (e134_myopia, 22), 'E134_矫正': (e134_fix, 22),
 'E134_片头': (titles.opening(SER25, VOL25, S25A, 2, '13 世纪眼镜 · 明代「叆叇」'), 7),
 'E134_片尾': (titles.closing(SER25, VOL25, S25A, 2, '下集：X 光为什么能看穿皮肉，却看不穿骨头？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
