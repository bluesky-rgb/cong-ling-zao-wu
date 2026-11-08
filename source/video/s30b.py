"""第三十季（古法解密 12.0：玩、响、用）第二批：B123 拨浪鼓、B124 笛子、B125 风铃 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO
from s30a import SB30, VOL30

DRUM = (200, 70, 60)
SKINC = (235, 215, 180)
STEEL = (190, 195, 205)
AIRC = (150, 200, 240)


# ---------------------------------------------------------------- B123 拨浪鼓
def b123_lag(c, t, i):
    corner_tag(c, 'B123 · 鼓身先转，珠子落在后面')
    c.text(60, 96, '从上往下看：手一搓，鼓身往左转；珠子因为惯性还留在原地，绳子一绷，把它拉过来甩到鼓面上', 'serif', 38, INK)
    cx, cy, R = 760, 560, 120
    w = 2 * math.pi * 1.2
    th = 0.9 * math.sin(w * t)
    # 珠子：简单的受迫摆，相位落后
    phase = math.pi * 0.75
    rel = 1.6 * math.sin(w * t - phase) - 0.9 * math.sin(w * t)
    c.ellipse(cx, cy, R, R * 0.35 + 0, fill=DRUM)
    c.rect(cx - R, cy - 18, cx + R, cy + 18, fill=mix(DRUM, BG, 0.2))
    for s in (1, -1):
        ax = cx + s * R * math.cos(th)
        ay = cy + s * R * 0.35 * math.sin(th) * 0.5
        a = th + (0 if s > 0 else math.pi) + rel * s * 0.6
        L = 150
        bx = ax + L * math.cos(a) * (1 if s > 0 else 1)
        by = ay + L * 0.45 * math.sin(a)
        c.line([(ax, ay), (bx, by)], INK, 2)
        c.ellipse(bx, by, 16, 16, fill=WOOD)
        hit = abs(bx - cx) < R + 20 and abs(by - cy) < 40
    c.line([(cx, cy + 30), (cx, cy + 300)], WOOD, 12)
    c.text(cx, cy + 340, '手柄（双手搓）', 'sans', 20, MUTED, 'mm')
    gx0, gy = 1250, 560
    c.rect(1230, 300, 1860, 820, fill=SHEET, r=14)
    c.text(1545, 336, '转角随时间（示意）', 'bold', 22, INK, 'mm')
    pts1, pts2 = [], []
    for k in range(121):
        tt = t - 3 + k / 40
        x = gx0 + k * 4.8
        pts1.append((x, gy - 120 * math.sin(w * tt)))
        pts2.append((x, gy + 140 - 120 * math.sin(w * tt - phase) * 0.6))
    c.line(pts1, DRUM, 3)
    c.line(pts2, WOOD, 3)
    c.text(1300, 378, '— 鼓身', 'sans', 20, DRUM, 'lm')
    c.text(1560, 378, '— 珠子：慢半拍', 'sans', 20, WOOD, 'lm')
    caps(c, t, [(0, 7, '拨浪鼓的鼓身插在手柄上，两边各用一根短绳拴着一颗小珠子'),
                (7.2, 14, '双手一搓，鼓身往一边转；珠子有惯性，没跟上，落在了后面'),
                (14.2, 22, '鼓身往回转时，绳子把珠子猛地拉过来，正好甩到鼓面上：一来一回，咚咚两声（示意）')], y=1010)


def b123_length(c, t, i):
    corner_tag(c, 'B123 · 绳子长短，决定打不打得到')
    c.text(60, 96, '绳太短，珠子够不着鼓面；绳太长，珠子来不及甩回来。只有长短合适，才能一搓一响', 'serif', 38, INK)
    data = [(4, 14), (6, 22), (9, 9)]
    grow = min(1, t / 9)
    for k, (L, n) in enumerate(data):
        x = 380 + k * 420
        c.rect(x - 70, 300, x + 70, 360, fill=DRUM, r=20)
        sw = 0.8 * math.sin(2 * math.pi * 1.3 * t + k)
        ex = x + 70 + L * 14 * math.cos(sw)
        ey = 330 + L * 14 * math.sin(sw) * 0.6 + L * 6
        c.line([(x + 70, 330), (ex, ey)], INK, 2)
        c.ellipse(ex, ey, 12, 12, fill=WOOD)
        c.text(x, 520, f'绳长 {L} 厘米', 'bold', 24, INK, 'mm')
        h = 300 * n / 22 * grow
        c.rect(x - 60, 900 - h, x + 60, 900, fill=mix(SPARK, GREEN, 0.5 if n == 22 else 0), r=6)
        c.text(x, 880 - h, f'{n * grow:.0f} 声', 'mono', 22, INK, 'mm')
    c.line([(260, 900), (1320, 900)], LINE, 2)
    c.text(1600, 600, '搓 10 秒响几声', 'bold', 26, INK, 'mm')
    c.text(1600, 650, '（数字为示意，以实测为准）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同样的鼓身，绳子分别留 4 厘米、6 厘米、9 厘米'),
                (7.2, 14, '4 厘米的珠子常常够不到鼓面；9 厘米的甩得太远，回来得太慢'),
                (14.2, 22, '中间那根正合适，搓得越快响得越密：小小的拨浪鼓，长短是调出来的（示意）')], y=1010)


# ---------------------------------------------------------------- B124 笛子
def b124_column(c, t, i):
    corner_tag(c, 'B124 · 管子越短，声音越高')
    c.text(60, 96, '对着吸管口吹气，管里的空气柱跟着振动：一头封住的管子，空气柱长度约等于声波的四分之一，管越短音越高', 'serif', 36, INK)
    lens = [6, 8, 10, 12, 15, 20]
    for k, L in enumerate(lens):
        x = 260 + k * 250
        top = 300
        h = L * 26
        c.rect(x - 24, top, x + 24, top + h, outline=STEEL, width=3, r=6)
        c.rect(x - 26, top + h - 6, x + 26, top + h + 6, fill=MUTED)
        f = 343 / (4 * L / 100)
        amp = 18
        pts = []
        for j in range(41):
            u = j / 40
            y = top + h * u
            a = amp * math.cos(math.pi / 2 * u) * math.sin(2 * math.pi * min(f, 1500) / 600 * t)
            pts.append((x + a * 0.8, y))
        c.line(pts, AIRC, 3)
        c.text(x, top - 30, f'{L} 厘米', 'bold', 22, INK, 'mm')
        c.text(x, top + h + 40, f'约 {f:.0f} 赫兹', 'mono', 20, SPARK, 'mm')
    c.text(960, 940, '理想估算：频率 ≈ 声速 ÷（4 × 管长），实际会低一点，以调音 App 读数为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '六根吸管剪成不同长度，下面封住，嘴唇对着上口侧面吹'),
                (7.2, 14, '管口那里空气来回动得最厉害，封住的底部空气动不了：空气柱就在两者之间振动'),
                (14.2, 22, '管长减半，频率差不多翻倍：音高一下子高了八度（数值为理想估算）')], y=1010)


def b124_holes(c, t, i):
    corner_tag(c, 'B124 · 开一个孔，空气柱就「变短」了')
    c.text(60, 96, '笛子上的孔全按住，整根管子的空气柱一起振，音最低；从下往上一个个放开，振动的那段到开着的孔就停了', 'serif', 36, INK)
    x0, x1, y = 300, 1600, 520
    c.rect(x0, y - 40, x1, y + 40, fill=mix(BG, BAMBOO, 0.8), r=40)
    c.ellipse(x0 + 80, y - 40, 14, 8, fill=INK)
    c.text(x0 + 80, y - 90, '吹孔', 'sans', 20, MUTED, 'mm')
    holes = [x1 - 140 - k * 120 for k in range(6)]
    nopen = min(6, int(t / 3))
    for k, hx in enumerate(holes):
        is_open = k < nopen
        c.ellipse(hx, y - 40, 16, 10, fill=BG if is_open else (225, 180, 150))
        if not is_open:
            c.ellipse(hx, y - 70, 24, 30, fill=mix(BG, (225, 180, 150), 0.6))
    end = holes[nopen - 1] if nopen else x1
    pts = []
    for j in range(81):
        u = j / 80
        x = x0 + 80 + (end - x0 - 80) * u
        a = 26 * math.sin(math.pi * u) * math.sin(2 * math.pi * 1.5 * t)
        pts.append((x, y + a))
    c.line(pts, AIRC, 4)
    c.line([(x0 + 80, y + 100), (end, y + 100)], SPARK, 3)
    c.text((x0 + 80 + end) / 2, y + 140, f'振动的空气柱：{(end - x0 - 80) / 10:.0f} 单位长', 'mono', 22, SPARK, 'mm')
    notes = ['最低音', '高一点', '再高', '再高', '更高', '更高', '最高']
    c.text(960, 800, f'开了 {nopen} 个孔 → {notes[nopen]}', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '笛子两头是通的，六个孔全部按住，整根管子里的空气柱一起振动，吹出最低的音'),
                (7.2, 14, '从最下面一个孔开始抬起手指：开着的孔通到外面，空气柱振到这里就「断」了'),
                (14.2, 22, '孔开得越靠上，振动的那段越短，音就越高：手指按孔，其实是在剪短空气柱（示意）')], y=1010)


# ---------------------------------------------------------------- B125 风铃
def b125_lengths(c, t, i):
    corner_tag(c, 'B125 · 长一倍，音高降到约四分之一')
    c.text(60, 96, '风铃的金属管不是靠里面的空气响，而是管子自己弯来弯去地振：频率大约和长度的平方成反比', 'serif', 38, INK)
    lens = [10, 14, 20, 28]
    for k, L in enumerate(lens):
        x = 330 + k * 260
        top = 260
        h = L * 20
        hit = (t * 0.8 + k * 0.25) % 1 < 0.6
        a = 6 * math.sin(2 * math.pi * 3 * t * (10 / L) ** 2) if hit else 0
        c.line([(x, 220), (x, top + h * 0.2)], MUTED, 1)
        pts = [(x + a * math.sin(math.pi * j / 20), top + h * j / 20) for j in range(21)]
        c.line(pts, STEEL, 14)
        c.text(x, top + h + 40, f'{L} 厘米', 'bold', 22, INK, 'mm')
        rel = (10 / L) ** 2
        c.text(x, top + h + 80, f'× {rel:.2f}', 'mono', 22, SPARK, 'mm')
    c.rect(1380, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1620, 340, '以 10 厘米为 1', 'bold', 22, INK, 'mm')
    gx0, gy0 = 1420, 600
    for k, L in enumerate(lens):
        rel = (10 / L) ** 2
        x = gx0 + k * 110
        c.rect(x, gy0 - 220 * rel, x + 70, gy0, fill=mix(STEEL, SPARK, rel), r=4)
    c.text(1620, 680, '理想细管估算，以调音 App 读数为准', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '四根一样粗的不锈钢管，长 10、14、20、28 厘米，一根根敲'),
                (7.2, 14, '管长 14 厘米，频率只剩大约一半；长一倍的 20 厘米，只剩大约四分之一'),
                (14.2, 22, '这和笛子不一样：笛子长一倍音高减半，风铃管长一倍音高掉到四分之一（理想估算，以实测为准）')], y=1010)


def b125_nodes(c, t, i):
    corner_tag(c, 'B125 · 吊在不动的地方，响得最久')
    c.text(60, 96, '管子振动时两头和中间在摆，离两端约五分之一处几乎不动；把线拴在这里，振动不被拽住，叮——的余音最长', 'serif', 36, INK)
    x0, x1, yc = 360, 1560, 520
    L = x1 - x0
    bl = 4.730
    def shape(u):
        x = bl * u
        s = (math.cosh(x) + math.cos(x)) - ((math.cosh(bl) - math.cos(bl)) / (math.sinh(bl) - math.sin(bl))) * (math.sinh(x) + math.sin(x))
        return s
    amp = 70 * math.sin(2 * math.pi * 1.2 * t)
    pts = [(x0 + L * j / 60, yc + amp * shape(j / 60) / 2) for j in range(61)]
    c.line(pts, STEEL, 16)
    for u in (0.224, 0.776):
        x = x0 + L * u
        c.line([(x, yc - 200), (x, yc)], MUTED, 2)
        c.ellipse(x, yc, 10, 10, fill=SPARK)
        c.text(x, yc - 230, '几乎不动的点', 'sans', 20, SPARK, 'mm')
    c.text(x0 + L * 0.224, yc + 150, '约 22%', 'mono', 22, INK, 'mm')
    c.text(x0 + L * 0.776, yc + 150, '约 78%', 'mono', 22, INK, 'mm')
    c.text(960, 820, '吊在端点：余音短；吊在约 1/5 处：余音长（以实测为准）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '风铃管被敲一下，像一根两头自由的梁那样上下弯着振动'),
                (7.2, 14, '两头和中间摆得最厉害，离两端大约 22% 的地方几乎不动'),
                (14.2, 22, '线拴在这两个点上，就不会拽住振动：叮——的余音能拖好久（示意）')], y=1010)


CLIPS = {
 'B123_落后': (b123_lag, 22), 'B123_绳长': (b123_length, 22),
 'B123_片头': (titles.opening(BSER, VOL30, SB30, 3, '战国已有「鼗」'), 7),
 'B123_片尾': (titles.closing(BSER, VOL30, SB30, 3, '下集：手指按住不同的孔，笛子为什么就换了音？'), 7),
 'B124_空气柱': (b124_column, 22), 'B124_按孔': (b124_holes, 22),
 'B124_片头': (titles.opening(BSER, VOL30, SB30, 4, '贾湖骨笛约 9000 年前'), 7),
 'B124_片尾': (titles.closing(BSER, VOL30, SB30, 4, '下集：风铃为什么长的那根声音低？'), 7),
 'B125_长度': (b125_lengths, 22), 'B125_吊点': (b125_nodes, 22),
 'B125_片头': (titles.opening(BSER, VOL30, SB30, 5, '唐宋屋檐下的「铁马」'), 7),
 'B125_片尾': (titles.closing(BSER, VOL30, SB30, 5, '下集：薄薄一张纸，折成褶为什么就硬挺了？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
