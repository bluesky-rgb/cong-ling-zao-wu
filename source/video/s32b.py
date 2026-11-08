"""第三十二季（古法解密 13.0：天、凉、数、用）第二批：B133 晒秋、B134 算筹、B135 结绳记事 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO
from s32a import SB32, VOL32, SUN, WARM, COOL

ROD = (230, 210, 160)
YARN2 = (210, 120, 90)
PEPPER = (210, 60, 50)


# ---------------------------------------------------------------- B133 晒秋
CONDS = [('阳光 + 风', 0.020, SUN), ('阳光下', 0.012, WARM), ('阴凉 + 电扇', 0.009, COOL), ('阴凉处', 0.004, MUTED)]


def b133_sun_wind(c, t, i):
    corner_tag(c, 'B133 · 热把水赶出来，风把水汽带走')
    c.text(60, 96, '四条一样湿的毛巾条：太阳给热，让水变成水汽；风把贴着表面的湿空气吹走，新的干空气再来接着吸', 'serif', 38, INK)
    x0, y0, x1, y1 = 260, 260, 1400, 860
    c.line([(x0, y1), (x1, y1)], LINE, 2)
    c.line([(x0, y0), (x0, y1)], LINE, 2)
    for m in range(0, 121, 30):
        c.text(x0 + (x1 - x0) * m / 120, y1 + 30, f'{m}', 'mono', 18, MUTED, 'mm')
    c.text((x0 + x1) / 2, y1 + 70, '分钟', 'sans', 20, MUTED, 'mm')
    c.text(x0, y0 - 30, '还剩多少水（示意）', 'sans', 20, MUTED, 'lm')
    tm = min(120, t / 18 * 120)
    for k, (lab, kk, col) in enumerate(CONDS):
        pts = []
        for j in range(int(tm) + 1):
            w = math.exp(-kk * j)
            pts.append((x0 + (x1 - x0) * j / 120, y1 - (y1 - y0) * w))
        if len(pts) > 1:
            c.line(pts, col, 5)
        w = math.exp(-kk * tm)
        c.text(1440, 300 + k * 90, f'{lab}  剩 {w * 100:.0f}%', 'bold', 24, col, 'lm')
    caps(c, t, [(0, 7, '同样湿的毛巾条，分别放在阳光下、阴凉处、阴凉处加电扇、阳光下加风'),
                (7.2, 14, '太阳把水加热，水分子跑得更快；风把表面那层湿空气吹走，蒸发就不会停下'),
                (14.2, 22, '热和风一起上，干得最快：所以晒秋要挑晴天、挑通风的屋顶（示意，以实测为准）')], y=1010)


def b133_thin(c, t, i):
    corner_tag(c, 'B133 · 切薄摊开，水跑出来的路更短')
    c.text(60, 96, '水要从里面走到表面才能蒸发：块越厚路越远；切成薄片摊开不叠，路短、每片都晒得到', 'serif', 36, INK)
    s = min(1, t / 16)
    for k, (lab, th, n) in enumerate((('一整块', 160, 1), ('切成厚片', 60, 3), ('切成薄片摊开', 20, 8))):
        x = 340 + k * 600
        y = 560
        for j in range(n):
            if n == 1:
                bx, w = x - 80, 160
            else:
                w = 160 / n * 2
                bx = x - 260 + j * (520 / n)
            h = th
            wet = max(0, 1 - s * (60 / th) ** 0.9)
            c.rect(bx, y - h / 2, bx + w - 6, y + h / 2, fill=mix((240, 160, 70), PEPPER, 1 - wet * 0.6), r=6)
            core = h / 2 * wet
            if core > 2:
                c.rect(bx + 4, y - core, bx + w - 10, y + core, fill=mix(BG, WATER, 0.5), r=4)
        c.text(x, 760, lab, 'bold', 26, INK, 'mm')
        c.text(x, 810, f'水要走约 {th / 2 / 10:.0f} 毫米', 'mono', 20, SPARK, 'mm')
    c.text(960, 900, '蓝色：还没跑出来的水（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '一整根胡萝卜放在太阳下，表面干了，里面还是湿的'),
                (7.2, 14, '水得从中心一点点走到表面；块越厚，这条路越长，越慢'),
                (14.2, 22, '切成薄片摊开、勤翻面：路短了，每一面都晒得到，几天就干透（示意）')], y=1010)


# ---------------------------------------------------------------- B134 算筹
def rod_digit(c, x, y, d, vertical, size=60, col=ROD, w=8):
    if d == 0:
        return
    gap = size * 0.22
    if vertical:
        n = d if d <= 5 else d - 5
        tot = (n - 1) * gap
        for k in range(n):
            xx = x - tot / 2 + k * gap
            c.line([(xx, y - size / 2), (xx, y + size / 2)], col, w)
        if d > 5:
            c.line([(x - size / 2, y - size / 2 - gap), (x + size / 2, y - size / 2 - gap)], col, w)
    else:
        n = d if d <= 5 else d - 5
        tot = (n - 1) * gap
        for k in range(n):
            yy = y - tot / 2 + k * gap
            c.line([(x - size / 2, yy), (x + size / 2, yy)], col, w)
        if d > 5:
            c.line([(x, y - tot / 2 - gap * 1.5), (x, y - tot / 2 - gap * 1.5 - size * 0.6)], col, w)


def rod_number(c, x_right, y, num, size=60, step=110, col=ROD):
    s = str(num)
    for k, ch in enumerate(reversed(s)):
        rod_digit(c, x_right - k * step, y, int(ch), vertical=(k % 2 == 0), size=size, col=col)


def b134_forms(c, t, i):
    corner_tag(c, 'B134 · 竖着摆、横着摆，一位一换')
    c.text(60, 96, '个位竖着摆，十位横着摆，百位又竖着：纵横相间，一眼就分得清是哪一位；空着的位就是零', 'serif', 38, INK)
    for d in range(1, 10):
        x = 200 + (d - 1) * 180
        rod_digit(c, x, 330, d, True)
        rod_digit(c, x, 520, d, False)
        c.text(x, 620, str(d), 'mono', 26, MUTED, 'mm')
    c.text(80, 330, '纵式', 'bold', 22, INK, 'mm')
    c.text(80, 520, '横式', 'bold', 22, INK, 'mm')
    k = min(2, int(t / 7.4))
    num = [36, 608, 2025][k]
    rod_number(c, 1300, 800, num)
    c.text(1560, 800, f'= {num}', 'mono', 40, SPARK, 'lm')
    if num == 608:
        c.text(1190, 870, '空位', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '1 到 5 是几根就摆几根；6 到 9 上面多一根当 5'),
                (7.2, 14, '个位用竖的，十位用横的，百位又是竖的：相邻两位长得不一样，不会看串'),
                (14.2, 22, '中间空一格就是零：几十根小棍子，就能摆出成千上万的数')], y=1010)


def b134_add(c, t, i):
    corner_tag(c, 'B134 · 47 + 38，满十往左进一根')
    c.text(60, 96, '先摆好 47 和 38，从个位开始合：7 和 8 合在一起是 15，个位留 5，往十位进一根；十位 4 + 3 + 1 = 8', 'serif', 38, INK)
    st = min(3, int(t / 5.5))
    c.text(300, 330, '47', 'mono', 30, MUTED, 'mm')
    c.text(300, 500, '38', 'mono', 30, MUTED, 'mm')
    if st == 0:
        rod_number(c, 1000, 330, 47)
        rod_number(c, 1000, 500, 38)
    elif st == 1:
        rod_digit(c, 890, 330, 4, False)
        rod_digit(c, 890, 500, 3, False)
        rod_digit(c, 1000, 420, 7, True, col=SPARK)
        rod_digit(c, 1100, 420, 8, True, col=SPARK)
        c.text(1300, 420, '7 + 8 = 15', 'mono', 30, SPARK, 'lm')
    elif st == 2:
        rod_digit(c, 890, 330, 4, False)
        rod_digit(c, 890, 500, 3, False)
        rod_digit(c, 890, 640, 1, False, col=GREEN)
        rod_digit(c, 1000, 760, 5, True)
        c.text(1300, 640, '满十，往十位进一根', 'bold', 28, GREEN, 'lm')
    else:
        rod_number(c, 1000, 760, 85)
        c.text(1300, 760, '= 85', 'mono', 40, SPARK, 'lm')
    caps(c, t, [(0, 7, '上面摆 47，下面摆 38，位对齐'),
                (7.2, 14, '先合个位：7 根加 8 根，凑成 15，个位留下 5，多出的十换成十位上的一根'),
                (14.2, 22, '再合十位：4 + 3 + 进来的 1 = 8，答案 85：算盘出现以前，人们就这样算账')], y=1010)


# ---------------------------------------------------------------- B135 结绳记事
AGES = [42, 39, 11, 7]


def _knots(c, x, ytop, tens, ones, a, col=YARN2):
    c.line([(x, ytop), (x, ytop + 480)], col, 5)
    for k in range(tens):
        c.ellipse(x, ytop + 70 + k * 26, 13 * a, 11 * a, fill=mix(BG, col, a))
    for k in range(ones):
        c.ellipse(x, ytop + 300 + k * 22, 11 * a, 9 * a, fill=mix(BG, (240, 200, 120), a))


def b135_tie(c, t, i):
    corner_tag(c, 'B135 · 打结的位置，就是数位')
    c.text(60, 96, '一根主绳挂几根垂绳：靠近主绳的一段打几个结表示几十，下面一段打几个结表示几个', 'serif', 38, INK)
    c.line([(300, 260), (1500, 260)], YARN2, 10)
    c.rect(300, 310, 1500, 490, outline=mix(BG, LINE, 0.6), width=2)
    c.text(1560, 400, '十位段', 'sans', 22, MUTED, 'lm')
    c.rect(300, 540, 1500, 790, outline=mix(BG, LINE, 0.6), width=2)
    c.text(1560, 665, '个位段', 'sans', 22, MUTED, 'lm')
    for k, age in enumerate(AGES):
        x = 450 + k * 300
        a = fade(t, 2 + k * 3.5, 3 + k * 3.5)
        _knots(c, x, 260, age // 10 if a > 0 else 0, age % 10 if a > 0 else 0, max(a, 0.01))
    c.text(960, 880, '每根垂绳记一个家人的年龄（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一根粗主绳横着，上面拴四根垂绳，一根对应一个家人'),
                (7.2, 14, '规定好：上面那段打几个结就是几十，下面那段打几个结就是几'),
                (14.2, 22, '同样是结，位置不同意思就不同：这和算筹「位置决定大小」是一个道理')], y=1010)


def b135_read(c, t, i):
    corner_tag(c, 'B135 · 不看纸条，读出四个数')
    c.text(60, 96, '把打好结的绳子交给另一个人：只要他知道「上段十位、下段个位」的规则，就能一根根读出来', 'serif', 38, INK)
    c.line([(300, 260), (1500, 260)], YARN2, 10)
    k = min(3, int(t / 4.8))
    for j, age in enumerate(AGES):
        x = 450 + j * 300
        _knots(c, x, 260, age // 10, age % 10, 1)
        if j <= k:
            c.rect(x - 80, 790, x + 80, 860, fill=SHEET, r=8)
            c.text(x, 825, f'{age // 10} 个十 + {age % 10}', 'sans', 20, INK, 'mm')
            c.text(x, 900, f'{age}', 'mono', 40, SPARK, 'mm')
    caps(c, t, [(0, 7, '第一根：上段 4 个结，下段 2 个结，读作 42'),
                (7.2, 14, '一根根往下读：39、11、7，最后一根上段一个结都没有，就是不到十'),
                (14.2, 22, '没有文字，也能把数记下来、传给别人：只要大家用同一套规则（示意）')], y=1010)


CLIPS = {
 'B133_热与风': (b133_sun_wind, 22), 'B133_摊薄': (b133_thin, 22),
 'B133_片头': (titles.opening(BSER, VOL32, SB32, 3, '明清以来山村晒秋习俗'), 7),
 'B133_片尾': (titles.closing(BSER, VOL32, SB32, 3, '下集：几根小棍子摆一摆，为什么就能算很大的数？'), 7),
 'B134_纵横': (b134_forms, 22), 'B134_加法': (b134_add, 22),
 'B134_片头': (titles.opening(BSER, VOL32, SB32, 4, '春秋战国已用算筹'), 7),
 'B134_片尾': (titles.closing(BSER, VOL32, SB32, 4, '下集：没有文字的时候，几根绳子怎么记下数目？'), 7),
 'B135_打结': (b135_tie, 22), 'B135_读数': (b135_read, 22),
 'B135_片头': (titles.opening(BSER, VOL32, SB32, 5, '上古结绳记事'), 7),
 'B135_片尾': (titles.closing(BSER, VOL32, SB32, 5, '下集：剪厚纸板，为什么要塞到剪刀根部去剪？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
