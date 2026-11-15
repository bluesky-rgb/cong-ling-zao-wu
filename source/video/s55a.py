"""第五十五季（第二十四层：游乐场）第一批：E282 滑梯、E283 跷跷板、E284 旋转转盘 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S55A = [('282', '滑梯'), ('283', '跷跷板'), ('284', '旋转转盘'), ('285', '摩天轮'), ('286', '过山车'),
        ('287', '碰碰车'), ('288', '喷泉'), ('289', '脚踏船'), ('290', '抓娃娃机'), ('291', '哈哈镜')]
SER55, VOL55 = '从零造物', '第五十五季 · 第二十四层：游乐场'
SLIDE = (230, 170, 80)
KID = (120, 160, 220)
BOARD = (190, 140, 90)
COIN = (210, 180, 90)
PLATE = (180, 185, 195)


# ---------------------------------------------------------------- E282 滑梯
def e282_slope(c, t, i):
    corner_tag(c, '第 282 集 · 坡越陡，推力越大')
    c.text(60, 96, '滑下去的推力来自重力顺着坡的那一部分：坡越陡，这部分越大；阻力来自屁股和滑梯面之间的摩擦', 'serif', 36, INK)
    for j, (deg, lab) in enumerate([(20, '20°'), (35, '35°')]):
        x0, y0 = 220 + j * 860, 860
        a = math.radians(deg)
        L = 620
        x1, y1 = x0 + L * math.cos(a), y0 - L * math.sin(a)
        c.poly([(x0, y0), (x1, y1), (x1, y0)], mix(BG, SLIDE, 0.8))
        s = L - min(L - 40, (t % 11) ** 2 * (8 + 10 * j))
        px, py = x0 + s * math.cos(a), y0 - s * math.sin(a)
        c.ellipse(px - 30 * math.sin(a), py - 30 * math.cos(a), 30, 30, fill=mix(BG, KID, 1.0))
        g = 220
        c.arrow(px, py - 40, px, py - 40 + g, MUTED, 4, 14)
        c.arrow(px, py - 40, px - g * math.sin(a) * math.cos(a), py - 40 + g * math.sin(a) * math.sin(a), GREEN, 6, 16)
        c.text((x0 + x1) / 2, y0 + 50, f'坡度 {lab}', 'bold', 28, INK, 'mm')
    c.text(960, 220, '灰：重力　绿：顺着坡往下的那一部分（示意）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '重力一直竖直往下拉'),
                (7.2, 14, '其中顺着坡的那一部分（绿箭头）推着人往下滑'),
                (14.2, 22, '坡越陡，绿箭头越长，滑得越快（示意，以实测为准）')], y=1010)


def e282_surface(c, t, i):
    corner_tag(c, '第 282 集 · 面越光滑，滑得越快')
    c.text(60, 96, '同一个坡：包塑料袋的橡皮哧溜滑下去，包棉布的慢一些，包砂纸的几乎不动；喷了水，塑料袋滑得更快', 'serif', 36, INK)
    res = [('塑料袋', 1.6, (180, 210, 230)), ('棉布', 3.2, (225, 220, 205)), ('砂纸', 99, (170, 140, 100))]
    a = math.radians(22)
    L = 460
    for j, (lab, T, col) in enumerate(res):
        x0, y0 = 160 + j * 600, 820
        c.poly([(x0, y0), (x0 + L * math.cos(a), y0 - L * math.sin(a)), (x0 + L * math.cos(a), y0)], mix(BG, BOARD, 0.8))
        u = min(1.0, ((t % 11) / T) ** 2) if T < 50 else 0.02
        s = (L - 60) * (1 - u) + 30
        px, py = x0 + s * math.cos(a), y0 - s * math.sin(a)
        c.poly([(px - 36 * math.cos(a), py + 36 * math.sin(a)), (px + 36 * math.cos(a), py - 36 * math.sin(a)),
                (px + 36 * math.cos(a) - 36 * math.sin(a), py - 36 * math.sin(a) - 36 * math.cos(a)),
                (px - 36 * math.cos(a) - 36 * math.sin(a), py + 36 * math.sin(a) - 36 * math.cos(a))], mix(BG, col, 1.0))
        c.text(x0 + L / 2, 880, lab + ('：约 ' + str(T) + ' 秒' if T < 50 else '：几乎不动') + '（示意）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '三块一样的橡皮，分别包上塑料袋、棉布、砂纸，从同一高度放手'),
                (7.2, 14, '越光滑摩擦越小：塑料袋最快，砂纸几乎不动'),
                (14.2, 22, '给坡喷点水，水膜让摩擦更小，塑料袋滑得更快（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E283 跷跷板
def _seesaw(c, cx, cy, ang, left, right, L=600):
    a = math.radians(ang)
    c.poly([(cx - 40, cy + 120), (cx + 40, cy + 120), (cx, cy)], mix(BG, (120, 110, 100), 1.0))
    x1, y1 = cx - L * math.cos(a), cy + L * math.sin(a)
    x2, y2 = cx + L * math.cos(a), cy - L * math.sin(a)
    c.line([(x1, y1), (x2, y2)], mix(BG, BOARD, 1.0), 16)
    for d, n, col in left:
        x, y = cx - d * math.cos(a), cy + d * math.sin(a)
        for k in range(n):
            c.ellipse(x, y - 22 - k * 16, 30, 8, fill=mix(BG, col, 1.0))
    for d, n, col in right:
        x, y = cx + d * math.cos(a), cy - d * math.sin(a)
        for k in range(n):
            c.ellipse(x, y - 22 - k * 16, 30, 8, fill=mix(BG, col, 1.0))


def e283_balance(c, t, i):
    corner_tag(c, '第 283 集 · 重量 × 距离')
    c.text(60, 96, '哪边下沉，要看「重量 × 离支点的距离」：左边 2 枚放在 10 厘米，右边 1 枚要放到 20 厘米才平', 'serif', 36, INK)
    d = 200 + min(1.0, t / 10) * 200
    tq = 2 * 200 - 1 * d
    ang = max(-12, min(12, tq / 15))
    _seesaw(c, 960, 560, ang, [(200, 2, COIN)], [(d, 1, COIN)])
    c.text(960 - 200, 760, '2 枚 × 10 厘米 = 20', 'bold', 28, INK, 'mm')
    c.text(960 + 300, 760, f'1 枚 × {d / 20:.0f} 厘米 = {d / 20:.0f}', 'bold', 28, GREEN if abs(tq) < 10 else INK, 'mm')
    if abs(tq) < 10:
        c.text(960, 880, '两边乘积相等：平了！', 'bold', 32, GREEN, 'mm')
    caps(c, t, [(0, 7, '左边离支点 10 厘米放 2 枚硬币，右边 1 枚放在 10 厘米：左边沉'),
                (7.2, 14, '把右边那 1 枚慢慢往外挪'),
                (14.2, 22, '挪到 20 厘米：2 × 10 = 1 × 20，跷跷板平了（示意）')], y=1010)


def e283_people(c, t, i):
    corner_tag(c, '第 283 集 · 大人往中间坐一点')
    c.text(60, 96, '大人比小孩重一倍：小孩坐最外头，大人往中间挪到一半远，两边「重量 × 距离」一样，就玩得起来', 'serif', 36, INK)
    u = min(1.0, max(0.0, (t - 4) / 6))
    db = 560 - 280 * u
    tq = 2 * db - 1 * 560
    ang = max(-12, min(12, tq / 40))
    if u >= 1:
        ang = 8 * math.sin(t * 1.5)
    _seesaw(c, 960, 600, ang, [(db, 0, KID)], [(560, 0, KID)])
    a = math.radians(ang)
    xb, yb = 960 - db * math.cos(a), 600 + db * math.sin(a)
    xk, yk = 960 + 560 * math.cos(a), 600 - 560 * math.sin(a)
    c.ellipse(xb, yb - 90, 60, 80, fill=mix(BG, (200, 120, 110), 1.0))
    c.text(xb, yb - 90, '大人', 'bold', 26, (255, 255, 255), 'mm')
    c.ellipse(xk, yk - 60, 40, 55, fill=mix(BG, KID, 1.0))
    c.text(xk, yk - 60, '小孩', 'bold', 22, (255, 255, 255), 'mm')
    c.text(960, 880, '大人往中间挪：一上一下玩起来了' if u >= 1 else '大人坐在最外头：一边沉到底', 'bold', 30, GREEN if u >= 1 else NRED, 'mm')
    caps(c, t, [(0, 7, '大人和小孩都坐在最外头：大人那边一下沉到底'),
                (7.2, 14, '大人往中间挪，挪到离支点一半远的地方'),
                (14.2, 22, '两边「重量 × 距离」差不多，轻轻一蹬就一上一下（玩时脚别伸到下面）')], y=1010)


# ---------------------------------------------------------------- E284 旋转转盘
def e284_fly(c, t, i):
    corner_tag(c, '第 284 集 · 外圈最先飞出去')
    c.text(60, 96, '硬币想沿直线往前跑，转盘的摩擦拉着它拐弯；越靠外、转得越快，需要的拉力越大，摩擦拉不住就飞出去', 'serif', 36, INK)
    cx, cy = 760, 560
    w = 0.6 + 0.12 * t
    ang = 0.06 * t * t + 0.6 * t
    c.ellipse(cx, cy, 340, 340, fill=mix(BG, PLATE, 0.6))
    c.ellipse(cx, cy, 14, 14, fill=INK)
    radii = [80, 190, 300]
    lim = [5.0, 2.6, 1.7]
    for k, r in enumerate(radii):
        if w < lim[k]:
            x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
            c.ellipse(x, y, 22, 22, fill=mix(BG, COIN, 1.0))
        else:
            tf = (w - lim[k]) * 4
            a0 = ang
            x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
            c.ellipse(x0 + 60 * tf, y0 + 40 * tf, 22, 22, fill=mix(BG, COIN, 0.6))
    c.text(1450, 360, f'转速：{w:.1f}（示意）', 'bold', 30, INK, 'mm')
    gone = sum(1 for L in lim if w >= L)
    c.text(1450, 440, ['三枚都在', '外圈飞出去了', '中圈也飞了', ''][gone], 'bold', 30, NRED if gone else GREEN, 'mm')
    c.text(1450, 520, '外圈 → 中圈 → 内圈', 'sans', 26, MUTED, 'mm')
    caps(c, t, [(0, 7, '离中心 3、8、13 厘米各放一枚硬币，慢慢转起来'),
                (7.2, 14, '越转越快：最外面那枚最先滑出去'),
                (14.2, 22, '再快，中间那枚也飞了；离中心最近的最稳（示意，以实测为准）')], y=1010)


def e284_arms(c, t, i):
    corner_tag(c, '第 284 集 · 收回手臂，转得更快')
    c.text(60, 96, '转椅慢慢转着，伸开的手臂一收回来，人就转得更快；花样滑冰收臂加速也是这个道理（大人扶着、转得很慢）', 'serif', 36, INK)
    cx, cy = 960, 560
    tuck = t > 9
    r_arm = 300 if not tuck else 110
    w = 1.0 if not tuck else 2.6
    ang = (t * w) if not tuck else (9 * 1.0 + (t - 9) * w)
    c.ellipse(cx, cy, 90, 90, fill=mix(BG, KID, 1.0))
    for s in (0, math.pi):
        a = ang + s
        x, y = cx + r_arm * math.cos(a), cy + r_arm * math.sin(a)
        c.line([(cx, cy), (x, y)], mix(BG, KID, 0.8), 22)
        c.rect(x - 30, y - 30, x + 30, y + 30, fill=mix(BG, (200, 120, 110), 1.0), r=6)
    c.arc(cx, cy, 380, 380, 200, 250, MUTED, 4)
    c.text(cx, 940, '手臂伸开：转得慢' if not tuck else '手臂收回：转得快', 'bold', 30, GREEN if tuck else INK, 'mm')
    c.text(1560, 360, '俯视示意，手里各拿一本书', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '大人把转椅慢慢推转起来就松手，坐的人双臂伸开、手拿两本书'),
                (7.2, 14, '把手臂收到胸前：转椅一下子转快了'),
                (14.2, 22, '东西离转轴越近，转得越快；转晕了马上停（示意）')], y=1010)


CLIPS = {
 'E282_坡度': (e282_slope, 22), 'E282_表面': (e282_surface, 22),
 'E282_片头': (titles.opening(SER55, VOL55, S55A, 0, '1922 年英国公园装了早期金属滑梯'), 7),
 'E282_片尾': (titles.closing(SER55, VOL55, S55A, 0, '下集：坐的位置怎么抵消轻重？'), 7),
 'E283_平衡': (e283_balance, 22), 'E283_挪位': (e283_people, 22),
 'E283_片头': (titles.opening(SER55, VOL55, S55A, 1, '游乐场里最常见的设施之一'), 7),
 'E283_片尾': (titles.closing(SER55, VOL55, S55A, 1, '下集：转盘上往外甩的劲从哪来？'), 7),
 'E284_甩出': (e284_fly, 22), 'E284_收臂': (e284_arms, 22),
 'E284_片头': (titles.opening(SER55, VOL55, S55A, 2, '旋转木马已有上百年历史'), 7),
 'E284_片尾': (titles.closing(SER55, VOL55, S55A, 2, '下集：摩天轮的座舱为什么不翻？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
