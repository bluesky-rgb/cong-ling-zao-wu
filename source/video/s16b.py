"""第十六季（古法解密 5.0）第二批：B53 筷子、B54 算盘、B55 九连环 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s16a import SB16, VOL16, WOOD

BEAD = (170, 90, 60)
RING = (190, 190, 200)

# ---------------------------------------------------------------- B53 筷子
def b53_lever(c, t, i):
    corner_tag(c, 'B53 · 筷子是费力杠杆')
    c.text(60, 96, '支点在手里，力在中间，东西在最远的尖上', 'serif', 40, INK)
    x0, y0, x1, y1 = 300, 380, 1500, 620
    ang = math.atan2(y1 - y0, x1 - x0)
    close = 8 * fade(t, 4, 6)
    c.line([(x0, y0), (x1, y1)], WOOD, 14)
    c.line([(x0, y0 + 60), (x1, y1 - close)], mix(WOOD, BG, 0.2), 14)
    c.ellipse(x1 + 20, (y1 + y1 - close) / 2 + 10, 26, 22, fill=(210, 180, 120))
    c.text(x1 + 20, y1 + 70, '花生', 'sans', 24, MUTED, 'mm')
    a = fade(t, 2, 3)
    c.ellipse(x0 + 40, y0 + 30, 22, 22, fill=mix(BG, SPARK, a))
    c.text(x0 + 40, y0 - 30, '支点：虎口和无名指', 'bold', 24, mix(BG, SPARK, a), 'mm')
    b = fade(t, 5, 6)
    fx = x0 + 0.3 * (x1 - x0)
    fy = y0 + 0.3 * (y1 - y0)
    c.arrow(fx, fy - 140, fx, fy - 12, mix(BG, NRED, b), 6, 20)
    c.text(fx, fy - 165, '手指用力（大）', 'bold', 26, mix(BG, NRED, b), 'mm')
    d = fade(t, 9, 10)
    c.arrow(x1 - 30, y1 - 110, x1 - 30, y1 - 20, mix(BG, GREEN, d), 4, 16)
    c.text(x1 - 30, y1 - 135, '尖上的夹力（小）', 'bold', 26, mix(BG, GREEN, d), 'mm')
    e = fade(t, 13, 14)
    c.rect(300, 780, 1620, 900, fill=mix(BG, SHEET, e), r=12)
    c.text(960, 820, '尖上的力 = 手指的力 × 手指到支点 ÷ 筷尖到支点', 'bold', 28, mix(BG, INK, e), 'mm')
    c.text(960, 865, '力小了，可手指动一毫米，筷尖就动好几毫米：换来的是距离和灵巧', 'sans', 24, mix(BG, MUTED, e), 'mm')
    caps(c, t, [(0, 6, '拿筷子时，上面那根以虎口为支点，食指和中指在中间用力'),
                (6.2, 13, '东西在最远的尖上：力臂长的一头，力反而小。这是费力杠杆'),
                (13.2, 22, '费力却不吃亏：手指一点点动作，被放大成筷尖的大动作，还能伸进汤碗里（接 B43 杆秤）')], y=1010)

def b53_grip(c, t, i):
    corner_tag(c, 'B53 · 握高一点还是低一点')
    c.text(60, 96, '握得越高，夹得越远，手指越累', 'serif', 40, INK)
    rows = [('手指在 1/4 处', 0.25, 4.0), ('手指在 1/2 处', 0.5, 2.0), ('手指在 3/4 处', 0.75, 1.33)]
    for k, (nm, pos, f) in enumerate(rows):
        a = fade(t, 1 + k * 3.5, 2 + k * 3.5)
        if a <= 0: continue
        y = 300 + k * 180
        c.line([(200, y), (1000, y)], mix(BG, WOOD, a), 12)
        c.ellipse(200, y, 16, 16, fill=mix(BG, SPARK, a))
        fx = 200 + 800 * pos
        c.arrow(fx, y - 80, fx, y - 8, mix(BG, NRED, a), 5, 16)
        c.text(250, y + 50, nm, 'bold', 26, mix(BG, INK, a), 'lm')
        h = 120 * f / 4 * fade(t, 1.5 + k * 3.5, 3 + k * 3.5)
        c.rect(1200, y + 40 - h, 1300, y + 40, fill=mix(BG, NRED, a), r=6)
        c.text(1330, y, f'手指要用尖上力的 {f:g} 倍', 'sans', 24, mix(BG, INK, a), 'lm')
    d = fade(t, 12, 13)
    c.text(960, 860, '手指离支点越远越省力：所以夹重东西时，手会自然往前挪（以实测为准）', 'bold', 26, mix(BG, GREEN, d), 'mm')
    caps(c, t, [(0, 6, '支点不动，手指往筷尖方向挪：手指到支点的距离变长'),
                (6.2, 13, '同样夹住一颗豆子，手指要用的力就越来越小'),
                (13.2, 22, '可握得太靠前，筷子伸不远、动作也被缩小了：每个人都在力气和灵巧之间找平衡')], y=1010)

# ---------------------------------------------------------------- B54 算盘
def abacus(c, x0, y0, digits, hi=None, a=1.0, w=110):
    n = len(digits)
    W = n * w + 40
    c.rect(x0 - 20, y0 - 20, x0 + W, y0 + 460, outline=mix(BG, WOOD, a), width=10, r=8)
    c.rect(x0 - 20, y0 + 120, x0 + W, y0 + 132, fill=mix(BG, WOOD, a))
    for k, dgt in enumerate(digits):
        x = x0 + 20 + k * w + w / 2
        c.line([(x, y0 - 10), (x, y0 + 450)], mix(BG, MUTED, a), 3)
        five, ones = divmod(dgt, 5)
        col = mix(BG, SPARK if hi == k else BEAD, a)
        yb = y0 + 95 if five else y0 + 25
        c.ellipse(x, yb, 46, 22, fill=col)
        for j in range(4):
            if j < ones:
                yy = y0 + 160 + j * 48
            else:
                yy = y0 + 250 + j * 48
            c.ellipse(x, yy, 46, 22, fill=col)
        c.text(x, y0 + 500, str(dgt), 'mono', 34, mix(BG, INK, a), 'mm')

def b54_place(c, t, i):
    corner_tag(c, 'B54 · 珠子的位置就是数')
    c.text(60, 96, '一档是一位：上面一颗当五，下面四颗各当一', 'serif', 40, INK)
    target = [2, 0, 2, 6]
    k = min(4, int(max(0, t - 2) / 2.5) + (1 if t > 2 else 0))
    digits = [target[j] if j < k else 0 for j in range(4)]
    abacus(c, 600, 220, digits, hi=k - 1 if 0 < k <= 4 else None)
    for j, nm in enumerate(['千', '百', '十', '个']):
        c.text(600 + 20 + j * 110 + 55, 180, nm, 'bold', 26, MUTED, 'mm')
    a = fade(t, 12, 13)
    c.text(1400, 400, '6 = 上面一颗（5）', 'sans', 28, mix(BG, INK, a), 'lm')
    c.text(1400, 450, '　 + 下面一颗（1）', 'sans', 28, mix(BG, INK, a), 'lm')
    c.text(1400, 540, '没有 0 也没关系：', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(1400, 590, '空着的档就是 0', 'bold', 28, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 6, '算盘每一根杆是一位：个、十、百、千，从右往左'),
                (6.2, 13, '靠近横梁的珠子才算数：上面一颗当五，下面每颗当一'),
                (13.2, 22, '一档空着，就是零：这正是第 48 集讲的位值制')], y=1010)

def b54_carry(c, t, i):
    corner_tag(c, 'B54 · 口诀：七去三进一')
    c.text(60, 96, '8 + 7：不用想，照口诀拨珠子', 'serif', 40, INK)
    if t < 5:
        digits, hi, msg = [0, 8], 1, '先拨上 8：上面一颗 + 下面三颗'
    elif t < 10:
        digits, hi, msg = [0, 5], 1, '「七去三」：个位拿掉 3'
    elif t < 15:
        digits, hi, msg = [1, 5], 0, '「进一」：十位拨上 1'
    else:
        digits, hi, msg = [1, 5], None, '答案 15'
    abacus(c, 700, 220, digits, hi=hi)
    c.text(700 + 20 + 55, 180, '十', 'bold', 26, MUTED, 'mm')
    c.text(700 + 20 + 165, 180, '个', 'bold', 26, MUTED, 'mm')
    c.text(1300, 420, msg, 'bold', 34, SPARK, 'lm')
    a = fade(t, 15, 16)
    c.text(1300, 520, '加 7 = 加 10 再减 3', 'sans', 28, mix(BG, INK, a), 'lm')
    c.text(1300, 570, '口诀把「想」变成了「查表」', 'sans', 28, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 5, '个位已经是 8，要再加 7：下面的珠子不够了'),
                (5.2, 10, '口诀「七去三进一」：个位拿掉 3'),
                (10.2, 22, '十位拨上 1，就是 15。熟练的人根本不用算，手指照着口诀走：和第 80 集齿轮的进位一样，只是用手')], y=1010)

# ---------------------------------------------------------------- B55 九连环
def moves(n):
    return (2 ** (n + 1) - 1) // 3 if n % 2 else (2 ** (n + 1) - 2) // 3

def b55_count(c, t, i):
    corner_tag(c, 'B55 · 多一个环，步数翻一倍')
    c.text(60, 96, '解开 n 个环要几步？', 'serif', 40, INK)
    x0, y0 = 200, 860
    for n in range(1, 10):
        a = fade(t, 1 + (n - 1) * 1.3, 2 + (n - 1) * 1.3)
        if a <= 0: continue
        m = moves(n)
        h = 560 * math.log2(m + 1) / math.log2(342)
        x = x0 + (n - 1) * 170
        c.rect(x, y0 - h, x + 110, y0, fill=mix(BG, GREEN if n == 9 else SPARK, a), r=6)
        c.text(x + 55, y0 - h - 30, str(m), 'mono', 28, mix(BG, INK, a), 'mm')
        c.text(x + 55, y0 + 40, f'{n} 环', 'sans', 24, mix(BG, MUTED, a), 'mm')
    c.line([(180, y0), (1760, y0)], LINE, 2)
    c.text(1760, 220, '高度按对数画（拍摄前核对步数算法）', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 6, '1 个环 1 步，2 个环 2 步，3 个环 5 步，4 个环 10 步'),
                (6.2, 13, '每多一个环，步数差不多翻一倍'),
                (13.2, 22, '9 个环，要 341 步（每次只动一个环的算法）。古人说「九连环，解不完」，一点不夸张')], y=1010)

GRAY3 = ['000', '001', '011', '010', '110', '111']

def b55_gray(c, t, i):
    corner_tag(c, 'B55 · 每一步只动一个环')
    c.text(60, 96, '把环在杆上记作 1，不在记作 0：3 个环的解法', 'serif', 40, INK)
    seq = GRAY3[::-1]
    k = min(len(seq) - 1, int(max(0, t - 2) / 2.4))
    for j, st in enumerate(seq):
        a = fade(t, 2 + j * 2.4, 3 + j * 2.4)
        if a <= 0: continue
        y = 220 + j * 110
        hl = j == k
        c.rect(300, y - 40, 900, y + 40, fill=mix(BG, mix(SHEET, SPARK, 0.3) if hl else SHEET, a), r=10)
        c.text(330, y, f'第 {j} 步', 'sans', 24, mix(BG, MUTED, a), 'lm')
        for q, ch in enumerate(st):
            cx = 560 + q * 110
            if ch == '1':
                c.ellipse(cx, y, 34, 34, outline=mix(BG, RING, a), width=8)
            else:
                c.ellipse(cx, y, 34, 34, outline=mix(BG, LINE, a), width=2)
            c.text(cx, y, ch, 'mono', 26, mix(BG, INK, a), 'mm')
    d = fade(t, 15, 16)
    c.rect(1040, 300, 1800, 640, fill=mix(BG, SHEET, d), r=12)
    c.text(1070, 350, '相邻两行只差一位：', 'bold', 28, mix(BG, INK, d), 'lm')
    c.text(1070, 400, '这串数在今天叫「格雷码」', 'bold', 28, mix(BG, GREEN, d), 'lm')
    c.text(1070, 470, '编码器、旋钮、数字电路', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1070, 510, '都用它防止「一下变两位」出错', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1070, 580, '接第 81 集开关、第 48 集数字', 'sans', 22, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 6, '三个环全在杆上是 111，全下来是 000'),
                (6.2, 14, '九连环的规矩：每一步只能动一个环，而且要看前面的环在不在'),
                (14.2, 22, '记下每一步，相邻两行永远只差一位：几百年前的玩具，走的正是今天的格雷码（宋代记载拍摄前核对）')], y=1010)

CLIPS = {
 'B53_杠杆': (b53_lever, 22), 'B53_握位': (b53_grip, 22),
 'B53_片头': (titles.opening(BSER, VOL16, SB16, 3, '商代 · 殷墟铜箸'), 7),
 'B53_片尾': (titles.closing(BSER, VOL16, SB16, 3, '下集：几根杆几颗珠子，怎么算得比人快？'), 7),
 'B54_档位': (b54_place, 22), 'B54_进位': (b54_carry, 22),
 'B54_片头': (titles.opening(BSER, VOL16, SB16, 4, '东汉 ·《数术记遗》「珠算」'), 7),
 'B54_片尾': (titles.closing(BSER, VOL16, SB16, 4, '下集：解开九个环，为什么要走几百步？'), 7),
 'B55_步数': (b55_count, 22), 'B55_格雷码': (b55_gray, 22),
 'B55_片头': (titles.opening(BSER, VOL16, SB16, 5, '宋代 · 九连环'), 7),
 'B55_片尾': (titles.closing(BSER, VOL16, SB16, 5, '下集：一阵风，怎么把米和糠分开？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
