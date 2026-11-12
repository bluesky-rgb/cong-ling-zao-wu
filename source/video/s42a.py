"""第四十二季（古法解密 18.0：屋里与河上）第一批：B180 灯笼、B181 砚台、B182 竹简 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB42 = [('B180', '灯笼'), ('B181', '砚台'), ('B182', '竹简'), ('B183', '搓衣板'), ('B184', '汤婆子'),
        ('B185', '二胡'), ('B186', '栈道'), ('B187', '浮桥'), ('B188', '锚'), ('B189', '号角')]
VOL42 = '第四十二季 · 古法解密 18.0'
LAMP = (255, 220, 120)
LANT = (220, 70, 50)
STONE = (90, 95, 105)
INKP = (40, 40, 48)
SLIP = (200, 180, 110)
CORD = (150, 110, 70)


# ---------------------------------------------------------------- B180 灯笼
def b180_diffuse(c, t, i):
    corner_tag(c, 'B180 · 一个亮点变成一大片')
    c.text(60, 96, '裸灯是一个很小的亮点，影子边缘又黑又硬；罩上纸，纸把光向四面八方散开，整个纸罩都在发亮，影子变得柔和', 'serif', 34, INK)
    for j, (lab, shade) in enumerate([('裸灯：影子又黑又硬', False), ('纸罩：影子柔和', True)]):
        cx = 520 + j * 880
        lx, ly = cx - 220, 560
        wall = cx + 300
        c.rect(wall, 240, wall + 20, 880, fill=mix(BG, (200, 195, 185), 0.6))
        if shade:
            c.rect(lx - 60, ly - 90, lx + 60, ly + 90, fill=mix(BG, LAMP, 0.55), r=20)
            src = [(lx + 60, ly + dy) for dy in range(-80, 81, 20)]
        else:
            c.ellipse(lx, ly, 14, 14, fill=LAMP)
            src = [(lx, ly)]
        px = cx + 40
        c.rect(px - 6, ly - 120, px + 6, ly + 120, fill=mix(BG, (210, 170, 90), 1.0))
        for (sx, sy) in src:
            for dy in (-120, 120):
                y_w = sy + (ly + dy - sy) * (wall - sx) / (px - sx)
                c.line([(sx, sy), (wall, y_w)], mix(BG, LAMP, 0.25 if shade else 0.7), 1)
        if shade:
            c.rect(wall - 4, ly - 160, wall + 24, ly + 160, fill=mix(BG, INKP, 0.5))
            c.rect(wall - 4, ly - 110, wall + 24, ly + 110, fill=mix(BG, INKP, 0.9))
        else:
            c.rect(wall - 4, ly - 200, wall + 24, ly + 200, fill=mix(BG, INKP, 1.0))
        c.text(cx, 930, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '小小的灯芯是一个点，光从一个点射出来，影子边缘清清楚楚、黑得刺眼'),
                (7.2, 14, '薄纸把穿过去的光向各个方向打散，整个纸罩变成一个大大的发光面'),
                (14.2, 22, '光从一大片地方照过来，影子边缘就变得朦朦胧胧，看着不晃眼（示意）')], y=1010)


def b180_fold(c, t, i):
    corner_tag(c, 'B180 · 竹篾一圈圈，能收能放')
    c.text(60, 96, '灯笼的骨架是一圈圈竹篾，中间糊着纸：拉开是一盏圆圆的灯，压扁就收成薄薄一叠，好带又好收', 'serif', 36, INK)
    cx, cy = 760, 560
    p = 0.5 + 0.5 * math.sin(t * 0.7)
    H = 80 + 380 * p
    n = 9
    for k in range(n):
        y = cy - H / 2 + k * H / (n - 1)
        f = 1 - (2 * k / (n - 1) - 1) ** 2
        w = 120 + 160 * math.sqrt(max(0, f))
        if k < n - 1:
            y2 = cy - H / 2 + (k + 1) * H / (n - 1)
            f2 = 1 - (2 * (k + 1) / (n - 1) - 1) ** 2
            w2 = 120 + 160 * math.sqrt(max(0, f2))
            c.poly([(cx - w, y), (cx + w, y), (cx + w2, y2), (cx - w2, y2)], mix(BG, LANT, 0.85))
    for k in range(n):
        y = cy - H / 2 + k * H / (n - 1)
        f = 1 - (2 * k / (n - 1) - 1) ** 2
        w = 120 + 160 * math.sqrt(max(0, f))
        c.line([(cx - w, y), (cx + w, y)], mix(BG, (170, 140, 80), 1.0), 5)
    c.rect(cx - 90, cy - H / 2 - 40, cx + 90, cy - H / 2, fill=mix(BG, (60, 50, 40), 1.0), r=6)
    c.rect(cx - 90, cy + H / 2, cx + 90, cy + H / 2 + 40, fill=mix(BG, (60, 50, 40), 1.0), r=6)
    c.ellipse(cx, cy, 30 * p + 4, 30 * p + 4, fill=mix(BG, LAMP, 0.6 * p))
    c.rect(1380, 320, 1860, 520, fill=SHEET, r=12)
    c.text(1620, 370, '高度', 'bold', 26, INK, 'mm')
    c.text(1620, 440, f'{H / 10:.0f} 厘米（示意）', 'mono', 32, SPARK, 'mm')
    caps(c, t, [(0, 7, '竹篾弯成一圈圈的环，由上到下大小不同，糊上纸，就是灯笼'),
                (7.2, 14, '纸在两圈竹篾之间可以折起来，所以整个灯笼能像手风琴一样压扁'),
                (14.2, 22, '点灯时拉开，收起时压扁：不用了一叠一叠放好（示意）')], y=1010)


# ---------------------------------------------------------------- B181 砚台
def b181_grind(c, t, i):
    corner_tag(c, 'B181 · 砚面的细小锋芒')
    c.text(60, 96, '放大砚台表面：有无数极细的小尖（叫「锋芒」）；墨锭在上面加水来回磨，被一点点刮下极细的颗粒', 'serif', 36, INK)
    y = 700
    pts = [(160, y)]
    r = random.Random(5)
    x = 160
    while x < 1500:
        x += r.uniform(14, 26)
        pts.append((x, y - r.uniform(6, 22)))
        x += r.uniform(10, 20)
        pts.append((x, y))
    pts += [(1500, 860), (160, 860)]
    c.poly(pts, mix(BG, STONE, 0.95))
    c.rect(160, y - 40, 1500, y - 10, fill=mix(BG, WATER_L, 0.25))
    off = 300 * math.sin(t * 1.5)
    bx = 830 + off
    c.rect(bx - 140, y - 330, bx + 140, y - 30, fill=mix(BG, INKP, 1.0), r=10)
    c.text(bx, y - 180, '墨锭', 'bold', 26, (200, 200, 210), 'mm')
    rr = random.Random(int(t * 4))
    for k in range(40):
        px = 180 + rr.uniform(0, 1300)
        py = y - 15 - rr.uniform(0, 25)
        c.ellipse(px, py, 3, 3, fill=(170, 170, 180))
    c.arrow(1580, 400, 1720, 400, SPARK, 5, 14)
    c.arrow(1720, 450, 1580, 450, SPARK, 5, 14)
    c.text(1650, 360, '来回磨', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '好砚台的石头里有细小坚硬的颗粒，在表面形成无数小尖'),
                (7.2, 14, '墨锭压在上面来回磨，小尖一点点刮下极细的墨粒，混进水里'),
                (14.2, 22, '太光滑刮不下来，太粗糙刮下的颗粒又粗：要细而均匀（示意）')], y=1010)


def b181_suspend(c, t, i):
    corner_tag(c, 'B181 · 颗粒越细，越不容易沉')
    c.text(60, 96, '三杯「墨汁」：粗颗粒很快沉到杯底，水变清；极细的颗粒在水里飘很久，写出来的字又黑又匀', 'serif', 36, INK)
    for j, (lab, size, speed) in enumerate([('粗砂纸磨的：几分钟就沉', 9, 1.0), ('细砂纸磨的：沉得慢', 5, 0.3), ('光滑瓷砖：几乎磨不下来', 4, 0.2)]):
        cx = 330 + j * 630
        top, bot = 300, 820
        c.rect(cx - 160, top, cx + 160, bot, fill=mix(BG, WATER_L, 0.2), outline=mix(BG, WATER_L, 0.8), width=4, r=14)
        r = random.Random(j)
        n = [70, 70, 10][j]
        tt = t % 16
        for k in range(n):
            x = cx - 140 + r.uniform(0, 280)
            y0 = top + 30 + r.uniform(0, 400)
            y = min(bot - 10 - (k % 6) * size * 1.2, y0 + speed * 60 * tt)
            c.ellipse(x, y, size, size, fill=(210, 210, 220))
        c.text(cx, bot + 60, lab, 'bold', 22, INK, 'mm')
    c.text(960, 960, '实验用白粉笔代替墨锭（以实测为准）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '颗粒在水里一边往下沉，一边被水分子撞来撞去'),
                (7.2, 14, '颗粒越大，越重，沉得越快；颗粒越细，水的阻力相对越大，沉得越慢'),
                (14.2, 22, '好墨汁里的颗粒极细，能在水里悬着很久，写字时墨色均匀')], y=1010)


# ---------------------------------------------------------------- B182 竹简
def _slips(c, x0, y0, n, gap, h, cords=2, labels=True):
    for k in range(n):
        x = x0 + k * (24 + gap)
        c.rect(x, y0, x + 24, y0 + h, fill=mix(BG, SLIP, 0.95), r=4)
        if labels:
            c.text(x + 12, y0 + h / 2, '从零造物古法解密竹简一卷'[k % 12], 'serif', 18, INKP, 'mm')
    for q in range(cords):
        y = y0 + h * (0.18 if q == 0 else 0.82)
        pts = []
        for k in range(n * 2 + 1):
            x = x0 - 6 + k * (24 + gap) / 2
            pts.append((x, y + (5 if k % 2 else -5)))
        c.line(pts, CORD, 4)


def b182_weave(c, t, i):
    corner_tag(c, 'B182 · 两道绳子编成一排')
    c.text(60, 96, '每根竹片写一行字，用两道绳子在竹片之间一上一下地绕过去：竹片排成一排，谁也跑不了，顺序也不会乱', 'serif', 35, INK)
    n = min(16, 2 + int(t / 1.2))
    _slips(c, 260, 300, n, 20, 480)
    c.rect(1380, 300, 1860, 560, fill=SHEET, r=12)
    c.text(1620, 350, '已经编好', 'bold', 26, INK, 'mm')
    c.text(1620, 430, f'{n} 根', 'mono', 44, SPARK, 'mm')
    c.text(1620, 510, '一卷常有几十到几百根', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '先把竹子剖成一根根窄窄的竹片，削平、烤干，叫「简」'),
                (7.2, 14, '用麻绳或丝绳，在竹片的上下两处来回绕，一根接一根编起来'),
                (14.2, 22, '编好的一排就是一篇文章：成语「韦编三绝」说的就是编竹简的皮绳都翻断了（拍摄前核对）')], y=1010)


def b182_roll(c, t, i):
    corner_tag(c, 'B182 · 留一点空隙才卷得起来')
    c.text(60, 96, '竹片之间留一点空隙，绳子能弯，整排竹简就像帘子一样卷起来；编得太紧，竹片挨死，就卷不动了', 'serif', 36, INK)
    p = 0.5 + 0.5 * math.sin(t * 0.6)
    for j, (lab, gap) in enumerate([('留空隙：卷得起来', 16), ('编太紧：卷不动', 0)]):
        cy = 380 + j * 330
        x0 = 220
        n = 14
        roll = p if gap else min(p, 0.1)
        flat = int(n * (1 - roll))
        for k in range(flat):
            x = x0 + k * (24 + gap)
            c.rect(x, cy - 110, x + 24, cy + 110, fill=mix(BG, SLIP, 0.95), r=4)
        c.line([(x0 - 6, cy - 80), (x0 + flat * (24 + gap), cy - 80)], CORD, 4)
        c.line([(x0 - 6, cy + 80), (x0 + flat * (24 + gap), cy + 80)], CORD, 4)
        rest = n - flat
        if rest > 0:
            rx = x0 + flat * (24 + gap) + 40
            R = 20 + rest * 4
            for k in range(rest):
                a = k / max(1, rest) * 2 * math.pi * (1.5 if gap else 0.2)
                x = rx + R * math.cos(a)
                c.rect(x - 12, cy - 110, x + 12, cy + 110, fill=mix(BG, SLIP, 0.7 + 0.25 * math.cos(a)), r=4)
        if not gap:
            c.text(x0 + flat * 24 + 120, cy, '卡住了', 'bold', 26, NRED, 'lm')
        c.text(1500, cy, lab, 'bold', 24, GREEN if gap else NRED, 'lm')
    caps(c, t, [(0, 7, '竹片本身是硬的，弯不了；能弯的是竹片之间的那一段绳子'),
                (7.2, 14, '竹片之间留一点空隙，每一处都能转一点点角度，加起来就卷成了一卷'),
                (14.2, 22, '编得太紧，竹片互相顶住，一点也转不动：硬的东西靠「关节」变软（示意）')], y=1010)


CLIPS = {
 'B180_漫射': (b180_diffuse, 22), 'B180_折叠': (b180_fold, 22),
 'B180_片头': (titles.opening(BSER, VOL42, SB42, 0, '汉代以后已有纸糊、纱糊的灯笼'), 7),
 'B180_片尾': (titles.closing(BSER, VOL42, SB42, 0, '下集：硬硬的墨锭，怎么磨成墨汁？'), 7),
 'B181_研磨': (b181_grind, 22), 'B181_悬浮': (b181_suspend, 22),
 'B181_片头': (titles.opening(BSER, VOL42, SB42, 1, '汉代已有石砚，唐宋时端砚、歙砚闻名'), 7),
 'B181_片尾': (titles.closing(BSER, VOL42, SB42, 1, '下集：几百根竹片，怎么编成一卷书？'), 7),
 'B182_编连': (b182_weave, 22), 'B182_卷起': (b182_roll, 22),
 'B182_片头': (titles.opening(BSER, VOL42, SB42, 2, '战国到汉代大量使用竹简书写'), 7),
 'B182_片尾': (titles.closing(BSER, VOL42, SB42, 2, '下集：洗衣服为什么要在有棱的板上搓？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
