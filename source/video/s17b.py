"""第十七季（第五层）第二批：E95 数码相机、E96 触摸屏、E97 二维码 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s17a import S17A, SER17, VOL17

def scene(x, y):
    # simple scene: sun + hill, x,y in 0..1, returns brightness 0..1
    sky = 0.75 - 0.3 * y
    if (x - 0.72) ** 2 + (y - 0.28) ** 2 < 0.012: return 1.0
    hill = 0.62 + 0.12 * math.sin(x * 5)
    if y > hill: return 0.25 + 0.1 * math.sin(x * 20)
    if 0.15 < x < 0.32 and 0.45 < y < hill: return 0.12
    return sky

# ---------------------------------------------------------------- E95 数码相机
def e95_pixels(c, t, i):
    corner_tag(c, '第 95 集 · 一格一个数')
    c.text(60, 96, '镜头把画面投在芯片上：芯片是一张光电池铺成的格子', 'serif', 40, INK)
    n = [8, 16, 48][min(2, int(t / 7))]
    x0, y0, W = 160, 220, 640
    cell = W / n
    for r in range(n):
        for q in range(n):
            v = scene((q + 0.5) / n, (r + 0.5) / n)
            g = int(30 + 225 * v)
            c.rect(x0 + q * cell, y0 + r * cell, x0 + (q + 1) * cell - (1 if n < 30 else 0), y0 + (r + 1) * cell - (1 if n < 30 else 0), fill=(g, g, g))
    c.text(x0 + W / 2, y0 + W + 40, f'{n} × {n} = {n * n} 个像素', 'bold', 28, INK, 'mm')
    # numbers for a few pixels
    a = fade(t, 1, 2)
    c.text(1000, 240, '每个像素：', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(1000, 290, '一个小光电池（第 77 集）', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1000, 340, '光越亮，产生的电越多 → 记成一个数', 'sans', 26, mix(BG, INK, a), 'lm')
    rows = [[int(scene((q + 0.5) / 8, (r + 0.5) / 8) * 255) for q in range(8)] for r in range(3)]
    for r, row in enumerate(rows):
        c.text(1000, 430 + r * 50, ' '.join(f'{v:3d}' for v in row), 'mono', 24, mix(BG, SPARK, a), 'lm')
    c.text(1000, 590, '……一行一行读出来（第 82 集扫描）', 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 7, '8 乘 8：只看得出亮的天、暗的山'),
                (7.2, 14, '16 乘 16：太阳和树出来了；格子越多，画面越细'),
                (14.2, 22, '手机相机有几千万个这样的小格子：每一格是一个光电池，亮度变成一个数，再一行行读出来')], y=1010)

def e95_bayer(c, t, i):
    corner_tag(c, '第 95 集 · 每个像素只看一种颜色')
    c.text(60, 96, '芯片本身是「色盲」：每格上面盖一片红、绿或蓝的小滤镜', 'serif', 40, INK)
    x0, y0, cell = 200, 240, 70
    cols = {'R': (220, 70, 60), 'G': (80, 190, 90), 'B': (70, 120, 230)}
    for r in range(8):
        for q in range(8):
            ch = ('G' if (r + q) % 2 == 0 else ('R' if r % 2 == 0 else 'B'))
            a = fade(t, 1 + (r * 8 + q) * 0.06, 1.5 + (r * 8 + q) * 0.06)
            c.rect(x0 + q * cell, y0 + r * cell, x0 + (q + 1) * cell - 3, y0 + (r + 1) * cell - 3, fill=mix(BG, cols[ch], a))
            c.text(x0 + q * cell + cell / 2 - 1, y0 + r * cell + cell / 2 - 1, ch, 'bold', 22, mix(BG, BG, a), 'mm')
    b = fade(t, 8, 9)
    c.rect(1000, 260, 1820, 640, fill=mix(BG, SHEET, b), r=12)
    c.text(1030, 310, '绿格子最多：人眼对绿色最敏感', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1030, 370, '每个像素只知道一种颜色的亮度', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1030, 430, '另外两种颜色，看看邻居猜出来', 'bold', 26, mix(BG, GREEN, b), 'lm')
    c.text(1030, 500, '1975 年第一台数码相机：', 'sans', 24, mix(BG, MUTED, b), 'lm')
    c.text(1030, 540, '1 万像素，存一张照片要 23 秒（拍摄前核对）', 'sans', 24, mix(BG, MUTED, b), 'lm')
    caps(c, t, [(0, 7, '光电池只认亮暗，不认颜色：于是给每个格子戴一片彩色小滤镜'),
                (7.2, 14, '红、绿、蓝排成棋盘，绿的最多，因为人眼对绿光最敏感'),
                (14.2, 22, '每格只量了一种颜色，另外两种从旁边的格子「猜」出来：你看到的彩色照片，三分之二是算出来的')], y=1010)

# ---------------------------------------------------------------- E96 触摸屏
def e96_grid(c, t, i):
    corner_tag(c, '第 96 集 · 屏幕下面是一张电极网')
    c.text(60, 96, '手指一靠近，那一格的电容就变了', 'serif', 40, INK)
    x0, y0, W, H, n = 300, 220, 700, 700, 8
    for k in range(n + 1):
        c.line([(x0, y0 + k * H / n), (x0 + W, y0 + k * H / n)], (90, 140, 210), 3)
        c.line([(x0 + k * W / n, y0), (x0 + k * W / n, y0 + H)], (200, 120, 90), 3)
    fx = x0 + W * (0.3 + 0.4 * (0.5 - 0.5 * math.cos(t * 0.6)))
    fy = y0 + H * (0.4 + 0.3 * math.sin(t * 0.45))
    c.ellipse(fx, fy, 60, 70, fill=(230, 190, 160))
    gx, gy = round((fx - x0) / (W / n)), round((fy - y0) / (H / n))
    cx, cy = x0 + gx * W / n, y0 + gy * H / n
    c.ellipse(cx, cy, 20, 20, outline=SPARK, width=5)
    sc = int(t * 4) % (n + 1)
    c.line([(x0, y0 + sc * H / n), (x0 + W, y0 + sc * H / n)], SPARK, 6)
    c.text(x0 + W + 40, y0 + sc * H / n, '正在扫这一行', 'sans', 22, SPARK, 'lm')
    a = fade(t, 6, 7)
    c.rect(1250, 400, 1860, 760, fill=mix(BG, SHEET, a), r=12)
    c.text(1280, 450, '横线和竖线交叉处是一个个小电容', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1280, 510, '手指是导体，又连着人：', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1280, 560, '靠近时「分走」一点电荷', 'bold', 26, mix(BG, INK, a), 'lm')
    c.text(1280, 630, '芯片一秒扫几十上百遍，', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1280, 680, '哪个交叉点变了，手指就在哪', 'bold', 26, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 7, '手机玻璃下面，藏着一横一竖两层透明的电极线'),
                (7.2, 14, '每个交叉点都是一个小电容，就像第 01 集的莱顿瓶：两片导体夹着绝缘层'),
                (14.2, 22, '手指一靠近，把那一点的电场「吸」走一部分：芯片不停地一行行扫，哪个点变了就知道你点在哪')], y=1010)

def e96_what(c, t, i):
    corner_tag(c, '第 96 集 · 什么东西能点动屏幕')
    c.text(60, 96, '要导电，还要连着一个够大的「身体」', 'serif', 40, INK)
    rows = [('手指', True, '导电，又连着整个人'), ('戴手套的手指', False, '布挡住了：电场到不了手指'), ('塑料笔', False, '不导电'),
            ('包锡纸的铅笔，手捏锡纸', True, '锡纸把手的电接到了笔尖'), ('包锡纸的铅笔，手不碰锡纸', False, '锡纸太小，又没连着人'), ('一根香肠（不食用）', True, '里面有盐水，能导电')]
    for k, (nm, ok, why) in enumerate(rows):
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        if a <= 0: continue
        y = 230 + k * 110
        c.rect(160, y - 40, 1760, y + 40, fill=mix(BG, SHEET, a), r=10)
        c.text(200, y, nm, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(980, y, '能点' if ok else '点不动', 'bold', 28, mix(BG, GREEN if ok else NRED, a), 'lm')
        c.text(1160, y, why, 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 7, '电容屏不是靠压力：按得再用力，塑料笔也没用'),
                (7.2, 14, '能点动的东西，要能导电，还要连着一个够大的导体：通常就是你自己'),
                (14.2, 22, '冬天的触屏手套，指尖织进了导电纤维：道理和锡纸一样（实验用的香肠不食用）')], y=1010)

# ---------------------------------------------------------------- E97 二维码
QR = [
"111111100101001111111",
"100000101100001000001",
"101110100011101011101",
"101110101010101011101",
"101110101101001011101",
"100000100110101000001",
"111111101010101111111",
"000000001101100000000",
"101011111010111010110",
"010110010111010101001",
"110101101001101110101",
"001010010110010101010",
"111001101011101100111",
"000000001101011010100",
"111111101010110101011",
"100000100101101010100",
"101110101110010111011",
"101110100001101000101",
"101110101011010110110",
"100000101100101011001",
"111111101011010100111"]

def qr_draw(c, x0, y0, cell, cover=0.0, a=1.0, hl=False):
    n = len(QR)
    c.rect(x0 - cell, y0 - cell, x0 + (n + 1) * cell, y0 + (n + 1) * cell, fill=mix(BG, (245, 245, 240), a))
    for r in range(n):
        for q in range(n):
            if QR[r][q] == '1':
                fp = (r < 7 and q < 7) or (r < 7 and q >= n - 7) or (r >= n - 7 and q < 7)
                col = SPARK if (hl and fp) else (20, 20, 20)
                c.rect(x0 + q * cell, y0 + r * cell, x0 + (q + 1) * cell, y0 + (r + 1) * cell, fill=mix(BG, col, a))
    if cover > 0:
        c.rect(x0 + n * cell * (1 - cover), y0 + n * cell * 0.35, x0 + n * cell + cell, y0 + n * cell + cell, fill=(240, 200, 80))

def e97_binary(c, t, i):
    corner_tag(c, '第 97 集 · 黑白格就是 0 和 1')
    c.text(60, 96, '三个角上的「回」字告诉手机：码在哪、朝哪边', 'serif', 40, INK)
    qr_draw(c, 220, 250, 28, hl=t > 6)
    a = fade(t, 2, 3)
    c.text(1000, 260, '黑 = 1，白 = 0', 'bold', 32, mix(BG, INK, a), 'lm')
    c.text(1000, 330, '一行行读下来，就是一长串二进制数', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1000, 380, QR[8][:21], 'mono', 26, mix(BG, SPARK, a), 'lm')
    b = fade(t, 6, 7)
    c.text(1000, 470, '三个「回」字（定位图形）：', 'bold', 28, mix(BG, SPARK, b), 'lm')
    c.text(1000, 520, '不管怎么斜着、倒着拍，手机都能找到它', 'sans', 26, mix(BG, INK, b), 'lm')
    d = fade(t, 12, 13)
    c.text(1000, 620, '条形码：一维，只能横着读一行', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1000, 670, '二维码：横竖都存，装得下一整个网址', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1000, 740, '（示意图案，不是能扫的真码）', 'sans', 22, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 6, '二维码的每一个小方格，黑的是 1，白的是 0'),
                (6.2, 12, '三个角上的「回」字是定位标记：告诉手机这个码的位置、大小和方向'),
                (12.2, 22, '条形码只能存一行，二维码横竖都存：1994 年日本电装公司发明了 QR 码（拍摄前核对）')], y=1010)

def e97_ecc(c, t, i):
    corner_tag(c, '第 97 集 · 多存一份，挡住也能读')
    c.text(60, 96, '把同一句话多说几遍：听漏一句也不怕', 'serif', 40, INK)
    word = '1011'
    a = fade(t, 1, 2)
    c.text(160, 250, '原来：', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(300, 250, word, 'mono', 40, mix(BG, INK, a), 'lm')
    b = fade(t, 3, 4)
    c.text(160, 340, '每位说三遍：', 'bold', 28, mix(BG, INK, b), 'lm')
    trip = ''.join(ch * 3 for ch in word)
    for k, ch in enumerate(trip):
        bad = k == 4 and t > 6
        c.text(380 + k * 44, 340, ('0' if ch == '1' else '1') if bad else ch, 'mono', 40, mix(BG, NRED if bad else INK, b), 'mm')
    d = fade(t, 7, 8)
    c.text(160, 430, '有一位被弄脏了（红）：三个里取多数，照样读出 1011', 'sans', 26, mix(BG, GREEN, d), 'lm')
    e = fade(t, 11, 12)
    lv = [('L', 7), ('M', 15), ('Q', 25), ('H', 30)]
    c.text(160, 540, 'QR 码的四个纠错等级：最多能丢多少还能读（约）', 'bold', 28, mix(BG, INK, e), 'lm')
    for k, (nm, p) in enumerate(lv):
        y = 610 + k * 70
        c.text(200, y, nm, 'mono', 30, mix(BG, INK, e), 'mm')
        c.rect(250, y - 20, 250 + 30 * p * fade(t, 12 + k * 0.6, 13 + k * 0.6), y + 20, fill=mix(BG, SPARK, e), r=6)
        c.text(270 + 30 * p, y, f'{p}%', 'mono', 26, mix(BG, INK, e), 'lm')
    qr_draw(c, 1300, 560, 14, cover=0.3 * fade(t, 14, 17), a=fade(t, 12, 13))
    caps(c, t, [(0, 6, '最笨的办法：每一位重复说三遍'),
                (6.2, 12, '中间一位被弄脏了，三个里有两个还是对的：少数服从多数，照样读出来'),
                (12.2, 22, '二维码用的是聪明得多的纠错码：选最高一级，挡住约三成还能扫出来（以实测为准）')], y=1010)

CLIPS = {
 'E95_像素': (e95_pixels, 22), 'E95_滤色': (e95_bayer, 22),
 'E95_片头': (titles.opening(SER17, VOL17, S17A, 3, '1969 年 CCD · 1975 年第一台数码相机'), 7),
 'E95_片尾': (titles.closing(SER17, VOL17, S17A, 3, '下集：为什么戴手套点不动手机屏幕？'), 7),
 'E96_电极网': (e96_grid, 22), 'E96_导体': (e96_what, 22),
 'E96_片头': (titles.opening(SER17, VOL17, S17A, 4, '1965 年 · 约翰逊的电容式触摸屏'), 7),
 'E96_片尾': (titles.closing(SER17, VOL17, S17A, 4, '下集：二维码被挡住一块，为什么还能扫出来？'), 7),
 'E97_二进制': (e97_binary, 22), 'E97_纠错': (e97_ecc, 22),
 'E97_片头': (titles.opening(SER17, VOL17, S17A, 5, '1974 年条形码 · 1994 年 QR 码'), 7),
 'E97_片尾': (titles.closing(SER17, VOL17, S17A, 5, '下集：一封邮件，怎么从地球这边跑到那边？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
