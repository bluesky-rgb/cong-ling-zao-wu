"""第五十一季（第二十二层：门厅与客厅）第三批：E268 暖气片、E269 石英钟、E270 三孔插头 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s51a import S51A, SER51, VOL51, COPPER, STEEL, BRASS

HOT = (230, 110, 70)
COLD = (90, 150, 230)
QUARTZ = (210, 220, 235)
LIVE = (200, 80, 60)
NEU = (80, 130, 220)
EARTH = (90, 180, 90)


# ---------------------------------------------------------------- E268 暖气片
def e268_conv(c, t, i):
    corner_tag(c, '第 268 集 · 热空气上升，整屋空气转起来')
    c.text(60, 96, '暖气片把旁边的空气烤热，热空气变轻往上走，冷空气从下面补过来又被烤热，一屋子空气就转起来了', 'serif', 36, INK)
    x0, y0, x1, y1 = 200, 180, 1720, 940
    c.rect(x0, y0, x1, y1, outline=mix(BG, INK, 0.5), width=4)
    c.rect(x0 - 10, 360, x0 + 6, 640, fill=mix(BG, (170, 200, 220), 1.0))
    c.text(x0 + 30, 340, '窗', 'sans', 22, MUTED, 'lm')
    c.rect(x0 + 40, 720, x0 + 240, 900, fill=mix(BG, HOT, 0.8), r=8)
    for k in range(6):
        c.line([(x0 + 60 + k * 32, 730), (x0 + 60 + k * 32, 890)], mix(BG, HOT, 1.0), 6)
    c.text(x0 + 140, 690, '暖气片', 'bold', 24, HOT, 'mm')
    # 环流路径：上升 → 顶部向右 → 右侧下降 → 底部向左回来
    cx0, cy0, cx1, cy1 = x0 + 140, 260, x1 - 120, 860
    P = 2 * ((cx1 - cx0) + (cy1 - cy0))
    n = 26
    for k in range(n):
        s = ((t * 0.06) + k / n) % 1 * P
        if s < cy1 - cy0:
            x, y = cx0, cy1 - s
        elif s < (cy1 - cy0) + (cx1 - cx0):
            x, y = cx0 + (s - (cy1 - cy0)), cy0
        elif s < 2 * (cy1 - cy0) + (cx1 - cx0):
            x, y = cx1, cy0 + (s - (cy1 - cy0) - (cx1 - cx0))
        else:
            x, y = cx1 - (s - 2 * (cy1 - cy0) - (cx1 - cx0)), cy1
        warm = 1 - min(1, abs(x - cx0) / (cx1 - cx0) * 0.8 + (0 if s < (cy1 - cy0) * 1.5 else 0.2))
        col = mix(COLD, HOT, max(0, min(1, warm)))
        c.ellipse(x, y, 14, 14, fill=col)
    c.arrow(cx0, 640, cx0, 420, HOT, 6, 18)
    c.arrow(cx1, 420, cx1, 640, COLD, 6, 18)
    if t > 14.2:
        c.text(960, 560, '纸螺旋吊在温水瓶上方：热空气往上推，螺旋慢慢转（以实测为准）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '暖气片旁边的空气被烤热，变轻，往上升'),
                (7.2, 14, '热空气沿天花板走到对面，慢慢变凉、下沉，再从地面流回暖气片'),
                (14.2, 22, '一屋子空气这样转起来；装在窗下，正好先烤热窗边下沉的冷空气')], y=1010)


def e268_fins(c, t, i):
    corner_tag(c, '第 268 集 · 一片片鳍片，散热面积更大')
    c.text(60, 96, '同样多的温水，外面包一圈锡纸折的鳍片的那杯凉得更快：碰到空气的面积大了，热传出去更快', 'serif', 36, INK)
    mins = min(20, t / 22 * 20 * 1.1)
    for j, (lab, rate) in enumerate([('不包', 0.020), ('包锡纸鳍片', 0.034)]):
        cx = 560 + j * 800
        c.rect(cx - 110, 360, cx + 110, 720, outline=mix(BG, INK, 0.6), width=4, r=14)
        temp = 22 + 28 * math.exp(-rate * mins)
        lvl = 400
        c.rect(cx - 106, lvl, cx + 106, 716, fill=mix(COLD, HOT, (temp - 22) / 28), r=10)
        if j == 1:
            for k in range(9):
                fx = cx - 100 + k * 25
                c.line([(fx, 360), (fx, 720)], mix(BG, STEEL, 1.0), 3)
            for side in (-1, 1):
                for k in range(6):
                    fy = 390 + k * 56
                    c.poly([(cx + side * 110, fy), (cx + side * 170, fy + 20), (cx + side * 110, fy + 40)], mix(BG, STEEL, 0.9))
        for k in range(10):
            ph = (t * 0.4 + k / 10) % 1
            c.ellipse(cx - 80 + k * 18, 340 - ph * 120, 5, 5, fill=mix(BG, HOT, 0.6 * (1 - ph)))
        c.text(cx, 790, f'{temp:.0f} ℃', 'bold', 40, INK, 'mm')
        c.text(cx, 860, lab, 'bold', 28, GREEN if j == 1 else INK, 'mm')
    c.text(960, 220, f'过了 {mins:.0f} 分钟（数字示意，以实测为准）', 'bold', 28, MUTED, 'mm')
    caps(c, t, [(0, 7, '两杯 50 ℃ 的温水，一杯外面包一圈锡纸折出的鳍片'),
                (7.2, 14, '每 5 分钟量一次：包了鳍片的那杯降温更快'),
                (14.2, 22, '暖气片做成一片片的，也是为了让更多金属面碰到空气')], y=1010)


# ---------------------------------------------------------------- E269 石英钟
def e269_vib(c, t, i):
    corner_tag(c, '第 269 集 · 找一个稳定的来回')
    c.text(60, 96, '摆钟数钟摆的来回，石英钟数一小块石英晶体的振动：它每秒振动 32768 次，又快又稳', 'serif', 36, INK)
    # 左：钟摆
    px, py = 480, 260
    a = 0.4 * math.sin(t * math.pi)
    L = 420
    bx, by = px + L * math.sin(a), py + L * math.cos(a)
    c.line([(px, py), (bx, by)], mix(BG, INK, 0.7), 5)
    c.ellipse(bx, by, 40, 40, fill=mix(BG, BRASS, 1.0))
    c.ellipse(px, py, 10, 10, fill=INK)
    c.text(480, 820, '钟摆：每秒 1 个来回左右', 'bold', 28, INK, 'mm')
    # 右：音叉形石英晶体
    qx, qy = 1440, 520
    w = 10 * math.sin(t * 60) if t > 7.2 else 0
    c.rect(qx - 90, qy + 80, qx + 90, qy + 160, fill=mix(BG, QUARTZ, 1.0), r=8)
    c.rect(qx - 90 - w, qy - 200, qx - 30 - w, qy + 90, fill=mix(BG, QUARTZ, 1.0), r=8)
    c.rect(qx + 30 + w, qy - 200, qx + 90 + w, qy + 90, fill=mix(BG, QUARTZ, 1.0), r=8)
    c.text(qx, qy - 250, '音叉形的石英晶体（放大示意）', 'sans', 24, MUTED, 'mm')
    c.text(qx, 820, '石英：每秒 32768 次', 'bold', 28, GREEN, 'mm')
    if t > 14.2:
        c.text(960, 920, '钢尺伸出越短，拨一下振得越快：长度、形状定下来，频率就定下来', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '摆钟：钟摆一来一回的时间很稳定，齿轮数着它走'),
                (7.2, 14, '石英钟：通电后，小小的石英晶体以固定的频率振动，快得看不见'),
                (14.2, 22, '都是找一个稳定的「来回」来数，石英的来回又快又稳（示意）')], y=1010)


def e269_count(c, t, i):
    corner_tag(c, '第 269 集 · 数满 32768 次走一秒')
    c.text(60, 96, '32768 是 2 的 15 次方：电路把振动一次次对半分，分 15 次正好剩下每秒 1 次，就推秒针走一格', 'serif', 36, INK)
    n = min(15, int(t / 22 * 17))
    vals = [32768 // (2 ** k) for k in range(16)]
    for k in range(16):
        col, row = k % 8, k // 8
        x = 170 + col * 220
        y = 330 + row * 220
        on = k <= n
        c.rect(x - 95, y - 70, x + 95, y + 70, fill=mix(BG, GREEN if (on and k == 15) else INK, 0.25 if on else 0.07), r=12)
        c.text(x, y, f'{vals[k]}', 'bold', 34 if vals[k] < 10000 else 30, INK if on else MUTED, 'mm')
        if k < 15 and on and k < n:
            if col < 7:
                c.text(x + 110, y, '÷2', 'sans', 20, MUTED, 'mm')
    # 秒针
    cx, cy = 960, 820
    c.ellipse(cx, cy, 120, 120, outline=mix(BG, INK, 0.6), width=4)
    sec = int(t) if n >= 15 else 0
    a = sec / 60 * 2 * math.pi
    c.line([(cx, cy), (cx + 105 * math.sin(a), cy - 105 * math.cos(a))], NRED, 4)
    c.text(cx + 200, cy, '每秒 1 次 → 秒针走一格' if n >= 15 else f'已经分了 {n} 次', 'bold', 28, GREEN if n >= 15 else INK, 'lm')
    caps(c, t, [(0, 7, '在纸上把 32768 一次次除以 2'),
                (7.2, 14, '16384、8192、4096……每除一次少一半'),
                (14.2, 22, '除了 15 次正好是 1：电路就这样数，每秒推秒针一格')], y=1010)


# ---------------------------------------------------------------- E270 三孔插头
def _plug(c, x, y, ins):
    """竖着画一只三孔插头（脚朝上），ins=插入深度 0..1。"""
    c.rect(x - 130, y, x + 130, y + 160, fill=mix(BG, (230, 230, 225), 1.0), r=20)
    c.rect(x - 14, y - 150, x + 14, y, fill=mix(BG, EARTH, 1.0), r=4)
    for dx in (-80, 80):
        c.rect(x + dx - 12, y - 110, x + dx + 12, y, fill=mix(BG, BRASS, 1.0), r=4)


def e270_earth(c, t, i):
    corner_tag(c, '第 270 集 · 外壳带电，电从地线走')
    c.text(60, 96, '第三个脚连着电器的金属外壳：万一里面的电线破了，外壳带了电，电顺着地线流进大地，不从人身上过', 'serif', 36, INK)
    bx, by = 700, 400
    c.rect(bx, by, bx + 420, by + 360, fill=mix(BG, STEEL, 0.8), r=16)
    c.text(bx + 210, by - 30, '电器的金属外壳', 'bold', 26, INK, 'mm')
    leak = t > 7.2
    c.line([(200, 470), (bx + 120, 470), (bx + 120, by + 120)], mix(BG, LIVE, 1.0), 6)
    c.text(200, 440, '火线', 'bold', 24, LIVE, 'lm')
    c.line([(200, 560), (bx + 300, 560)], mix(BG, NEU, 1.0), 6)
    c.text(200, 530, '零线', 'bold', 24, NEU, 'lm')
    c.line([(bx + 420, by + 300), (1400, by + 300), (1400, 880)], mix(BG, EARTH, 1.0), 6)
    c.text(1420, 640, '地线', 'bold', 24, EARTH, 'lm')
    for k in range(4):
        c.line([(1340 + k * 10, 880 + k * 18), (1460 - k * 10, 880 + k * 18)], mix(BG, EARTH, 1.0), 4)
    c.text(1400, 970 - 20, '大地', 'sans', 22, MUTED, 'mm')
    if leak:
        c.text(bx + 120, by + 200, '破皮', 'bold', 26, NRED, 'mm')
        c.ellipse(bx + 120, by + 140, 16, 16, fill=NRED)
        if t > 14.2:
            for k in range(6):
                f = ((t * 0.8) + k / 6) % 1
                pts = [(bx + 120, by + 140), (bx + 420, by + 300), (1400, by + 300), (1400, 880)]
                L = [math.dist(pts[m], pts[m + 1]) for m in range(3)]
                s = f * sum(L)
                for m in range(3):
                    if s <= L[m]:
                        u = s / L[m]
                        x = pts[m][0] + (pts[m + 1][0] - pts[m][0]) * u
                        y = pts[m][1] + (pts[m + 1][1] - pts[m][1]) * u
                        break
                    s -= L[m]
                c.ellipse(x, y, 10, 10, fill=NRED)
            c.text(960, 230, '电走地线这条近路进了大地，摸外壳的人不会触电（示意）', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '插座里有火线、零线，还有一根地线，连着电器的金属外壳'),
                (7.2, 14, '万一里面的电线破了皮、碰到外壳，外壳就带了电'),
                (14.2, 22, '有地线，电顺着地线流进大地；本集只画图，不做任何通电实验')], y=1010)


def e270_long(c, t, i):
    corner_tag(c, '第 270 集 · 地线脚更长：先接后断')
    c.text(60, 96, '量一量：接地的那个脚比另外两个长一点。插的时候它先碰到插座，拔的时候它最后离开（只看拔下的插头）', 'serif', 36, INK)
    ph = (t % 11) / 11
    d = 1 - abs(2 * ph - 1)
    sy = 300
    c.rect(560, 160, 1360, sy, fill=mix(BG, (235, 235, 230), 1.0), r=16)
    c.text(960, 200, '插座（示意）', 'bold', 24, INK, 'mm')
    for dx in (-80, 0, 80):
        c.rect(960 + dx - 16, sy - 30, 960 + dx + 16, sy, fill=mix(BG, (40, 40, 40), 1.0), r=4)
    py = sy + 260 - 220 * d
    _plug(c, 960, py, d)
    e_in = py - 150 <= sy
    p_in = py - 110 <= sy
    c.text(1450, 520, '地线：' + ('接上' if e_in else '没接'), 'bold', 28, GREEN if e_in else MUTED, 'lm')
    c.text(1450, 580, '火线零线：' + ('接上' if p_in else '没接'), 'bold', 28, LIVE if p_in else MUTED, 'lm')
    c.text(960, 900, '插：地线先接上；拔：地线最后断开（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '用尺子量拔下来的三孔插头：接地的那个脚更长（以实测为准）'),
                (7.2, 14, '插进去时，地线先接上，火线零线后接上'),
                (14.2, 22, '拔出来时，火线零线先断，地线最后断：外壳一直有保护（插拔由大人做）')], y=1010)


CLIPS = {
 'E268_对流': (e268_conv, 22), 'E268_鳍片': (e268_fins, 22),
 'E268_片头': (titles.opening(SER51, VOL51, S51A, 6, '19 世纪出现热水和蒸汽暖气片'), 7),
 'E268_片尾': (titles.closing(SER51, VOL51, S51A, 6, '下集：没有钟摆，石英钟靠什么数一秒？'), 7),
 'E269_振动': (e269_vib, 22), 'E269_数数': (e269_count, 22),
 'E269_片头': (titles.opening(SER51, VOL51, S51A, 7, '1927 年出现第一台石英钟'), 7),
 'E269_片尾': (titles.closing(SER51, VOL51, S51A, 7, '下集：插头上的第三个脚有什么用？'), 7),
 'E270_接地': (e270_earth, 22), 'E270_先接': (e270_long, 22),
 'E270_片头': (titles.opening(SER51, VOL51, S51A, 8, '20 世纪中期三孔接地插头普及'), 7),
 'E270_片尾': (titles.closing(SER51, VOL51, S51A, 8, '下集：软软的地毯怎么吃掉声音？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
