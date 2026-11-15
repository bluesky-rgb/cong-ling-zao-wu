"""第五十三季（第二十三层：超市与包装）第一批：E272 热敏小票、E273 瓦楞纸箱、E274 易拉罐 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S53A = [('272', '热敏小票'), ('273', '瓦楞纸箱'), ('274', '易拉罐'), ('275', '牛奶盒'), ('276', '薯片袋'),
        ('277', '鸡蛋托'), ('278', '气泡膜'), ('279', '购物车万向轮'), ('280', '卧式冰柜'), ('281', '自动扶梯')]
SER53, VOL53 = '从零造物', '第五十三季 · 第二十三层：超市与包装'
PAPER = (240, 236, 225)
CARD = (200, 160, 110)
ALU = (190, 195, 205)
HOT = (235, 110, 60)
GAS = (150, 200, 240)

GLYPH = ['01110', '10001', '10001', '11111', '10001', '10001', '10001']   # 字母 A 的点阵


# ---------------------------------------------------------------- E272 热敏小票
def e272_head(c, t, i):
    corner_tag(c, '第 272 集 · 一排小加热点')
    c.text(60, 96, '收银机里没有墨水：打印头是一排很小的加热点，纸走过时哪个点一热，纸上那一点就变黑，一行行拼成字', 'serif', 36, INK)
    x0, y0 = 560, 260
    cell = 56
    c.rect(x0 - 40, y0 - 40, x0 + 5 * cell + 40, 900, fill=mix(BG, PAPER, 1.0), r=8)
    rows_done = min(7, int(t / 2.4))
    for r in range(rows_done):
        for k, ch in enumerate(GLYPH[r]):
            if ch == '1':
                c.rect(x0 + k * cell + 6, y0 + r * cell + 6, x0 + (k + 1) * cell - 6, y0 + (r + 1) * cell - 6, fill=mix(BG, (30, 30, 35), 1.0), r=4)
    hy = y0 + rows_done * cell + cell / 2 if rows_done < 7 else y0 + 7 * cell + cell / 2
    c.rect(x0 - 60, hy - 14, x0 + 5 * cell + 60, hy + 14, fill=mix(BG, (90, 90, 100), 1.0), r=6)
    if rows_done < 7:
        for k, ch in enumerate(GLYPH[rows_done]):
            col = HOT if (ch == '1' and (t % 2.4) < 1.2) else mix(BG, (140, 140, 150), 1.0)
            c.ellipse(x0 + k * cell + cell / 2, hy, 12, 12, fill=col)
    c.text(x0 + 5 * cell + 120, hy, '打印头：一排小加热点', 'bold', 26, HOT, 'lm')
    c.arrow(x0 - 120, 700, x0 - 120, 400, MUTED, 4, 14)
    c.text(x0 - 140, 760, '纸往上走', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '小票纸往前走，打印头贴着纸'),
                (7.2, 14, '这一行要黑的点，加热一瞬间；不要黑的点不加热'),
                (14.2, 22, '一行一行加热，黑点就拼成了字（点阵示意）')], y=1010)


def e272_coat(c, t, i):
    corner_tag(c, '第 272 集 · 受热就变黑的涂层')
    c.text(60, 96, '小票纸上涂着一层热敏涂层：平时是白的，温度一高就变黑；指甲快速一划摩擦生热，也能划出一道黑线', 'serif', 36, INK)
    tests = [('指甲快速划', 1.0), ('50 ℃ 温水贴 1 分钟', 0.15), ('热风吹 10 秒（大人）', 1.0)]
    k = min(2, int(t / 7.3))
    for j, (lab, dark) in enumerate(tests):
        x = 360 + j * 600
        c.rect(x - 200, 300, x + 200, 760, fill=mix(BG, PAPER, 1.0), r=8)
        if j < k or (j == k and (t - 7.3 * k) > 2):
            if j == 0:
                c.line([(x - 140, 420), (x + 140, 640)], mix(BG, (30, 30, 35), 1.0), 10)
            elif j == 1:
                c.ellipse(x, 530, 120, 120, fill=mix(mix(BG, PAPER, 1.0), (120, 120, 120), dark))
            else:
                c.ellipse(x, 530, 140, 140, fill=mix(mix(BG, PAPER, 1.0), (30, 30, 35), 0.9))
        c.text(x, 820, lab, 'bold', 26, INK if j <= k else MUTED, 'mm')
        if j <= k and (t - 7.3 * j) > 3:
            c.text(x, 880, ['变黑', '几乎不变（不够热）', '变黑'][j], 'bold', 26, GREEN if j != 1 else NRED, 'mm')
    c.text(960, 230, '显色的温度大约 60–70 ℃（以实测为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '指甲在背面快速一划：摩擦生热，划出一道黑线'),
                (7.2, 14, '贴在 50 ℃ 温水杯上：不够热，几乎不变色'),
                (14.2, 22, '大人用热风吹一下：一大片变黑；摸完小票记得洗手')], y=1010)


# ---------------------------------------------------------------- E273 瓦楞纸箱
def _corr(c, x0, x1, y, h, col, n=14):
    c.rect(x0, y - 4, x1, y, fill=col)
    c.rect(x0, y + h, x1, y + h + 4, fill=col)
    pts = []
    w = (x1 - x0) / n
    for k in range(n * 8 + 1):
        x = x0 + k * w / 8
        pts.append((x, y + h / 2 - (h / 2) * math.cos(2 * math.pi * (x - x0) / w)))
    c.line(pts, col, 4)


def e273_arch(c, t, i):
    corner_tag(c, '第 273 集 · 弯成拱，夹两层')
    c.text(60, 96, '同样一张纸：平放一压就弯；折成一排拱、上下再各贴一层面纸，拱和面纸一起受力，就又硬又能承重', 'serif', 36, INK)
    k = 0 if t < 7.2 else 1
    for j in range(2):
        x0, x1, y = 300 + j * 760, 860 + j * 760, 520
        c.rect(x0 - 40, y, x0, y + 220, fill=mix(BG, (120, 110, 100), 1.0))
        c.rect(x1, y, x1 + 40, y + 220, fill=mix(BG, (120, 110, 100), 1.0))
        n = min(12, int(max(0, t - 2) * 1.2)) if j == 0 else min(30, int(max(0, t - 9) * 3))
        if j == 0:
            sag = min(120, n * 10)
            pts = [(x0 + (x1 - x0) * u / 20, y - 2 + sag * math.sin(math.pi * u / 20)) for u in range(21)]
            c.line(pts, mix(BG, PAPER, 1.0), 6)
            for m in range(n):
                c.ellipse((x0 + x1) / 2 - 20 + (m % 3) * 20, y - 14 - (m // 3) * 10 + sag, 12, 5, fill=mix(BG, (210, 180, 90), 1.0))
            c.text((x0 + x1) / 2, 830, f'平纸：放 {n} 枚就塌（示意）', 'bold', 26, NRED, 'mm')
        elif k:
            _corr(c, x0, x1, y - 40, 40, mix(BG, CARD, 1.0))
            for m in range(n):
                c.ellipse((x0 + x1) / 2 - 40 + (m % 5) * 20, y - 58 - (m // 5) * 10, 12, 5, fill=mix(BG, (210, 180, 90), 1.0))
            c.text((x0 + x1) / 2, 830, f'瓦楞板：放了 {n} 枚还不弯（示意）', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '一张平纸架在两摞书中间，放几枚硬币就弯下去'),
                (7.2, 14, '把一张纸折成一排拱，上下各粘一张面纸'),
                (14.2, 22, '同样多的纸，做成瓦楞板，放了一堆硬币也不弯（以实测为准）')], y=1010)


def e273_upright(c, t, i):
    corner_tag(c, '第 273 集 · 瓦楞竖着最能撑')
    c.text(60, 96, '把瓦楞板卷成纸筒：瓦楞竖着，每一道拱都像一根小柱子；瓦楞横着，一压就顺着折痕塌下去', 'serif', 36, INK)
    books = min(8, int(t / 2.5))
    for j, (lab, up) in enumerate([('瓦楞横着', False), ('瓦楞竖着', True)]):
        cx = 560 + j * 800
        gy = 860
        crush = 0 if up else min(120, max(0, books - 2) * 30)
        h = 300 - crush
        c.rect(cx - 140, gy - h, cx + 140, gy, fill=mix(BG, CARD, 0.9), r=6)
        if up:
            for k in range(9):
                x = cx - 120 + k * 30
                c.line([(x, gy - h + 6), (x, gy - 6)], mix(BG, (150, 110, 70), 1.0), 3)
        else:
            for k in range(int(h / 30)):
                y = gy - h + 15 + k * 30
                c.line([(cx - 130, y), (cx + 130, y)], mix(BG, (150, 110, 70), 1.0), 3)
        nb = books if up else min(books, 3)
        for b in range(nb):
            c.rect(cx - 170, gy - h - (b + 1) * 34, cx + 170, gy - h - b * 34 - 4, fill=mix(BG, [(120, 160, 210), (200, 120, 110), (130, 180, 120)][b % 3], 0.9), r=4)
        c.text(cx, 930, f'{lab}：{"压扁了" if (not up and books > 3) else ("还在撑着" if up else "")}', 'bold', 28, GREEN if up else NRED, 'mm')
    caps(c, t, [(0, 7, '两个一样的纸筒，一个瓦楞横着，一个瓦楞竖着'),
                (7.2, 14, '一本一本往上放书：横着的很快就被压扁'),
                (14.2, 22, '竖着的每道拱像小柱子，撑得住；纸箱的瓦楞也是竖着的')], y=1010)


# ---------------------------------------------------------------- E274 易拉罐
def _can(c, cx, cy, squeeze, pressure, dome=True):
    w = 140 - squeeze
    c.rect(cx - w, cy - 300, cx + w, cy + 290, fill=mix(BG, ALU, 1.0), r=24)
    c.rect(cx - 120, cy - 320, cx + 120, cy - 296, fill=mix(BG, ALU, 0.8), r=8)
    if dome:
        c.arc(cx, cy + 290, 110, 60, 200, 340, mix(BG, (120, 125, 135), 1.0), 8)
        c.poly([(cx - 104, cy + 270), (cx + 104, cy + 270), (cx + 104, cy + 292), (cx - 104, cy + 292)], BG)
    if pressure:
        random.seed(3)
        for k in range(24):
            x = cx + random.uniform(-w + 20, w - 20)
            y = cy + random.uniform(-260, 220)
            c.ellipse(x, y, 7, 7, outline=mix(BG, GAS, 1.0), width=3)
        for a in range(8):
            ang = a * math.pi / 4
            c.arrow(cx + 60 * math.cos(ang), cy + 90 * math.sin(ang), cx + (w - 10) * math.cos(ang), cy + 200 * math.sin(ang) * 0.9, mix(BG, GAS, 1.0), 4, 12)


def e274_press(c, t, i):
    corner_tag(c, '第 274 集 · 里面的气压把薄壁撑硬')
    c.text(60, 96, '易拉罐的壁只有零点一毫米左右；没开的汽水罐里溶着很多二氧化碳，罐里的气压比外面大，从里面把薄壁撑硬', 'serif', 36, INK)
    sq = 8 * abs(math.sin(t * 2)) if t < 14.2 else 50 * abs(math.sin(t * 2))
    _can(c, 560, 560, 6 * abs(math.sin(t * 2)), True)
    _can(c, 1360, 560, 50 * abs(math.sin(t * 2)) if t > 7.2 else 0, False)
    c.text(560, 920, '没开的罐：捏不动', 'bold', 28, GREEN, 'mm')
    c.text(1360, 920, '开了的空罐：一捏就瘪', 'bold', 28, NRED, 'mm')
    for x in (560, 1360):
        if t > 3:
            c.arrow(x - 300, 560, x - 160, 560, MUTED, 5, 14)
            c.arrow(x + 300, 560, x + 160, 560, MUTED, 5, 14)
    caps(c, t, [(0, 7, '没开的汽水罐，里面的气往外顶，罐壁绷得紧紧的'),
                (7.2, 14, '空罐里外气压一样，薄薄的铝一捏就瘪'),
                (14.2, 22, '开罐「呲」的一声，气跑了，罐子也就变软了（饮料不喝）')], y=1010)


def e274_dome(c, t, i):
    corner_tag(c, '第 274 集 · 罐底做成向里凹的拱')
    c.text(60, 96, '罐里的气压往外顶：平底会被顶得鼓出来、站不稳；向里凹的拱形罐底把压力分散到四周，顶得住又站得稳', 'serif', 36, INK)
    p = min(1.0, t / 10)
    for j, (lab, dome) in enumerate([('平底', False), ('向里凹的拱', True)]):
        cx, cy = 560 + j * 800, 560
        c.rect(cx - 160, cy - 260, cx + 160, cy + (150 if dome else 120), fill=mix(BG, ALU, 0.9), r=10)
        if dome:
            c.ellipse(cx, cy + 150, 150, 70, fill=BG)
            c.rect(cx - 170, cy + 150, cx + 170, cy + 230, fill=BG)
            c.arc(cx, cy + 150, 150, 70, 200, 340, mix(BG, (120, 125, 135), 1.0), 12)
            c.line([(cx - 200, cy + 150), (cx + 200, cy + 150)], mix(BG, INK, 0.4), 3)
            for a in range(5):
                x = cx - 100 + a * 50
                c.arrow(x, cy + 30, x + (x - cx) * 0.4, cy + 100, mix(BG, GAS, 1.0), 4, 12)
            c.text(cx, 850, '拱把压力传到四周：顶得住、站得稳', 'bold', 26, GREEN, 'mm')
        else:
            bulge = 70 * p
            c.arc(cx, cy + 120, 160, max(2, bulge), 0, 180, mix(BG, (120, 125, 135), 1.0), 12)
            c.line([(cx - 200, cy + 120 + bulge), (cx + 200, cy + 120 + bulge)], mix(BG, INK, 0.4), 3)
            c.text(cx, 850, '被顶得鼓出来，站不稳（示意）', 'bold', 26, NRED, 'mm')
        c.text(cx, 230, lab, 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '罐里的气压从里面往外推，罐底也被推'),
                (7.2, 14, '平底被推得鼓起来，罐子就站不稳了'),
                (14.2, 22, '把罐底做成向里凹的拱，压力被拱传到四周，罐子稳稳站住')], y=1010)


CLIPS = {
 'E272_打印头': (e272_head, 22), 'E272_涂层': (e272_coat, 22),
 'E272_片头': (titles.opening(SER53, VOL53, S53A, 0, '20 世纪 70 年代热敏纸用于收银'), 7),
 'E272_片尾': (titles.closing(SER53, VOL53, S53A, 0, '下集：一张纸为什么能撑住人？'), 7),
 'E273_拱': (e273_arch, 22), 'E273_竖立': (e273_upright, 22),
 'E273_片头': (titles.opening(SER53, VOL53, S53A, 1, '19 世纪末出现瓦楞纸箱'), 7),
 'E273_片尾': (titles.closing(SER53, VOL53, S53A, 1, '下集：没开的易拉罐为什么捏不动？'), 7),
 'E274_内压': (e274_press, 22), 'E274_拱底': (e274_dome, 22),
 'E274_片头': (titles.opening(SER53, VOL53, S53A, 2, '20 世纪 60 年代出现拉环易拉罐'), 7),
 'E274_片尾': (titles.closing(SER53, VOL53, S53A, 2, '下集：纸盒怎么挡住光和空气？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
