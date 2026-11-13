"""第四十三季（第十八层：工具箱）第三批：E228 磁性螺丝刀、E229 万用表、E230 砂纸 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s43a import S43A, SER43, VOL43, STEEL

MAGN = (210, 70, 70)
MAGS = (70, 110, 210)
METER = (240, 200, 60)
WOODC = (205, 165, 110)
GRIT = (120, 110, 100)


def _arrow_dom(c, x, y, ang, L=34, col=INK):
    dx, dy = L * math.cos(ang), L * math.sin(ang)
    c.arrow(x - dx / 2, y - dy / 2, x + dx / 2, y + dy / 2, col, 4, 12)


# ---------------------------------------------------------------- E228 磁性螺丝刀
def e228_domains(c, t, i):
    corner_tag(c, '第 228 集 · 把小磁畴排整齐')
    c.text(60, 96, '铁里有无数块「小磁铁」（磁畴），平时方向乱、互相抵消；用磁铁朝一个方向蹭，它们就一个个转过来排整齐', 'serif', 35, INK)
    x0, y0 = 260, 380
    cols, rows = 16, 4
    W, H = 1400, 300
    c.rect(x0 - 20, y0 - 20, x0 + W + 20, y0 + H + 20, fill=mix(BG, STEEL, 0.35), r=12)
    r = random.Random(4)
    base = [r.uniform(0, 2 * math.pi) for _ in range(cols * rows)]
    mx = x0 - 200 + (W + 400) * min(1.0, t / 12)
    for k in range(cols * rows):
        cx = x0 + 45 + (k % cols) * (W - 90) / (cols - 1)
        cy = y0 + 40 + (k // cols) * (H - 80) / (rows - 1)
        done = min(1.0, max(0.0, (mx - cx) / 200))
        a0 = base[k]
        tgt = 0.0
        d = ((tgt - a0 + math.pi) % (2 * math.pi)) - math.pi
        a = a0 + d * done
        _arrow_dom(c, cx, cy, a, 40, mix(BG, SPARK if done > 0.95 else INK, 0.9))
    if t < 13:
        c.rect(mx - 60, y0 - 140, mx + 60, y0 - 40, fill=MAGN, r=8)
        c.rect(mx - 60, y0 - 40, mx + 60, y0 - 25, fill=MAGS)
        c.arrow(mx - 160, y0 - 90, mx - 80, y0 - 90, MUTED, 4, 12)
    tip = min(1.0, max(0.0, (t - 13) / 2))
    if tip > 0:
        for k in range(int(5 * tip)):
            c.rect(x0 + W + 40, y0 + 60 + k * 44, x0 + W + 140, y0 + 90 + k * 44, outline=STEEL, width=4, r=14)
        c.text(x0 + W + 90, y0 + 300, '吸起回形针', 'sans', 22, MUTED, 'mm')
    c.text(960, 820, '箭头：每个小磁畴的方向（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '没被磁化的铁钉，小磁畴各指各的方向，合起来几乎没有磁性'),
                (7.2, 14, '磁铁从一头蹭到另一头，经过的地方，小磁畴就跟着转向同一边'),
                (14.2, 22, '排整齐的磁畴一起使劲，铁钉自己变成了一块小磁铁：能吸起回形针（以实测为准）')], y=1010)


def e228_knock(c, t, i):
    corner_tag(c, '第 228 集 · 敲一敲，又乱了')
    c.text(60, 96, '排整齐的磁畴并不牢靠：用锤子敲、在地上摔、放到火上烤，它们又被震乱了，磁性就变弱', 'serif', 36, INK)
    x0, y0 = 260, 400
    cols, rows = 16, 4
    W, H = 1400, 300
    c.rect(x0 - 20, y0 - 20, x0 + W + 20, y0 + H + 20, fill=mix(BG, STEEL, 0.35), r=12)
    r = random.Random(9)
    scat = [r.uniform(-math.pi, math.pi) for _ in range(cols * rows)]
    n_hits = min(10, int(t / 1.6))
    mess = n_hits / 10
    for k in range(cols * rows):
        cx = x0 + 45 + (k % cols) * (W - 90) / (cols - 1)
        cy = y0 + 40 + (k // cols) * (H - 80) / (rows - 1)
        a = scat[k] * mess
        _arrow_dom(c, cx, cy, a, 40, mix(BG, INK, 0.9))
    hit = (t % 1.6) < 0.25 and n_hits < 10
    hx = x0 + W / 2
    hy = y0 - 40 + (30 if hit else 0)
    c.rect(hx - 120, hy - 60, hx + 120, hy, fill=mix(BG, (110, 110, 120), 1.0), r=8)
    c.line([(hx, hy - 60), (hx, hy - 120)], mix(BG, (170, 120, 70), 1.0), 18)
    c.text(960, 800, f'敲了 {n_hits} 下', 'bold', 30, SPARK, 'mm')
    w = 600 * (1 - 0.75 * mess)
    c.rect(660, 860, 660 + w, 900, fill=GREEN, r=8)
    c.text(640, 880, '剩下的磁性', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 7, '把磁化好的铁钉放在水泥地上，由大人用锤子敲'),
                (7.2, 14, '每敲一下，铁钉里一震，一部分小磁畴就转回乱七八糟的方向'),
                (14.2, 22, '敲完再去吸回形针，吸起的少了：磁铁要轻拿轻放，也是这个道理（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E229 万用表
def _meter(c, x, y, txt, lab):
    c.rect(x - 150, y - 220, x + 150, y + 220, fill=mix(BG, METER, 1.0), r=24)
    c.rect(x - 120, y - 190, x + 120, y - 80, fill=mix(BG, (40, 55, 45), 1.0), r=8)
    c.text(x, y - 135, txt, 'mono', 44, (180, 240, 180), 'mm')
    c.ellipse(x, y + 40, 70, 70, fill=mix(BG, (60, 60, 65), 1.0))
    c.text(x, y + 40, lab, 'bold', 22, BG, 'mm')
    c.ellipse(x - 60, y + 170, 16, 16, fill=INK)
    c.ellipse(x + 60, y + 170, 16, 16, fill=NRED)


def e229_voltage(c, t, i):
    corner_tag(c, '第 229 集 · 电压：推电的劲儿')
    c.text(60, 96, '电压是推着电流走的「劲儿」：新电池约 1.5 伏，用旧了劲儿就小；两节头尾串起来，劲儿加在一起', 'serif', 36, INK)
    stage = int(t / 7) % 3
    vals = ['1.58', '1.21', '3.15']
    labs = ['一节新电池', '一节旧电池', '两节串联']
    _meter(c, 360, 560, vals[stage], 'V')
    bx, by = 1100, 560
    n = 2 if stage == 2 else 1
    for k in range(n):
        y = by - 80 + k * 170 - (85 if n == 2 else 0) + (80 if n == 1 else 0)
        c.rect(bx, y - 50, bx + 300, y + 50, fill=mix(BG, (70, 70, 80), 1.0), r=10)
        c.rect(bx + 300, y - 20, bx + 320, y + 20, fill=mix(BG, STEEL, 1.0))
        c.text(bx + 150, y, '1.5 V', 'bold', 26, BG if False else INK, 'mm')
    c.line([(360 - 60, 730), (360 - 60, 820), (bx - 20, 820), (bx - 20, by + (85 if n == 2 else 0))], INK, 4)
    c.line([(360 + 60, 730), (360 + 60, 860), (bx + 340, 860), (bx + 340, by - (85 if n == 2 else 0))], NRED, 4)
    c.text(bx + 160, by + 220, labs[stage], 'bold', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '红笔碰正极、黑笔碰负极，旋钮放在直流电压档，读出一节新电池约 1.5 伏'),
                (7.2, 14, '用旧的电池，推电的劲儿小了，读数也降下来'),
                (14.2, 22, '两节头尾相接，劲儿加起来约 3 伏：只测电池，绝不碰插座（读数以实测为准）')], y=1010)


def e229_resist(c, t, i):
    corner_tag(c, '第 229 集 · 电阻：电流过去难不难')
    c.text(60, 96, '测电阻时，表自己送一点点电流过去，看它过得难不难：铅笔线越长越难走，表笔靠近一半，电阻也差不多少一半', 'serif', 34, INK)
    stage = int(t / 7) % 3
    x0, x1, y = 300, 1500, 520
    c.rect(x0 - 40, y - 140, x1 + 40, y + 140, fill=mix(BG, (245, 243, 236), 0.9), r=10)
    c.line([(x0, y), (x1, y)], mix(BG, (60, 60, 65), 1.0), 26)
    L = [1.0, 0.5, 1.0][stage]
    pa, pb = x0 + 20, x0 + 20 + (x1 - x0 - 40) * L
    for px, col in [(pa, INK), (pb, NRED)]:
        c.line([(px, y - 10), (px - 40, y - 200)], col, 10)
        c.ellipse(px, y - 10, 10, 10, fill=col)
    r = random.Random(int(t * 10))
    for k in range(18):
        u = ((t * 0.3 + k / 18) % 1)
        xx = pa + (pb - pa) * u
        c.ellipse(xx, y + r.uniform(-6, 6), 5, 5, fill=SPARK)
    txt = ['20 kΩ', '10 kΩ', '— —'][stage]
    if stage == 2:
        c.rect(pa + 10, y - 30, pa + 120, y + 30, fill=BG)
        c.text(960, y + 200, '铅笔线中间擦断：电流过不去，读数「开路」', 'bold', 26, NRED, 'mm')
    else:
        c.text(960, y + 200, ['表笔相距 10 厘米', '表笔相距 5 厘米'][stage], 'bold', 26, SPARK, 'mm')
    c.rect(1560, 300, 1820, 420, fill=mix(BG, (40, 55, 45), 1.0), r=8)
    c.text(1690, 360, txt, 'mono', 40, (180, 240, 180), 'mm')
    c.text(1690, 450, '读数（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '2B 铅笔在纸上涂一条粗线，石墨能导电，但不太好导'),
                (7.2, 14, '表笔靠近一半，电流要走的路短一半，电阻也差不多少一半'),
                (14.2, 22, '线一断，电流过不去，表就显示开路：通断档会「嘀」一声告诉你通没通（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E230 砂纸
def e230_grit(c, t, i):
    corner_tag(c, '第 230 集 · 每颗砂粒都是一把小刀')
    c.text(60, 96, '砂纸上粘着无数颗比木头硬得多的小砂粒；在表面上一拖，每颗都刮下一点点材料：颗粒越大，刮得越深，划痕也越深', 'serif', 34, INK)
    for j, (lab, rad, dep) in enumerate([('80 目：颗粒大，刮得深', 26, 40), ('600 目：颗粒小，刮得浅', 8, 10)]):
        ox = 140 + j * 900
        sy = 300
        off = (t * 80) % 200
        c.rect(ox, sy - 40, ox + 800, sy, fill=mix(BG, (200, 180, 140), 0.9))
        r = random.Random(3 + j)
        n = 14 if j == 0 else 40
        for k in range(n):
            gx = ox + 20 + ((k * 800 / n + off) % 780)
            c.poly([(gx - rad, sy), (gx + rad, sy), (gx + r.uniform(-rad / 2, rad / 2), sy + rad * 1.4)], mix(BG, GRIT, 1.0))
        wy = sy + 30 + rad * 1.4
        c.rect(ox, wy, ox + 800, wy + 300, fill=mix(BG, WOODC, 1.0))
        pts = [(ox, wy)]
        r2 = random.Random(10 + j)
        for k in range(80):
            x = ox + k * 10
            pts.append((x, wy + r2.uniform(0, dep)))
        pts.append((ox + 800, wy))
        c.poly(pts, BG)
        for k in range(int(6 * (t % 2))):
            c.ellipse(ox + 400 + r.uniform(-300, 300), wy - 30 - r.uniform(0, 30), 4, 3, fill=mix(BG, WOODC, 0.8))
        c.text(ox + 400, wy + 360, lab, 'bold', 26, NRED if j == 0 else GREEN, 'mm')
    caps(c, t, [(0, 7, '用放大镜看砂纸：一颗颗尖尖的小石粒，紧紧粘在纸上'),
                (7.2, 14, '粗砂纸颗粒大，一下就刮掉很多，但留下的沟也又深又宽'),
                (14.2, 22, '细砂纸颗粒小，刮得慢，留下的沟很浅：摸起来就光滑多了（示意）')], y=1010)


def e230_sequence(c, t, i):
    corner_tag(c, '第 230 集 · 先粗后细')
    c.text(60, 96, '想又快又光：先用粗砂纸磨平大坑，再换中号把粗划痕磨浅，最后用细砂纸磨光；每一号只要磨掉上一号留下的划痕', 'serif', 34, INK)
    x0, x1, y0 = 200, 1700, 600
    stage = min(3, int(t / 5.5))
    deps = [90, 40, 14, 4]
    labs = ['原来：坑坑洼洼', '80 目后：平了，但划痕深', '240 目后：划痕变浅', '600 目后：摸着光滑']
    r = random.Random(5)
    base = [r.uniform(0, 1) for _ in range(150)]
    pts = [(x0, y0 + 300)]
    for k in range(150):
        x = x0 + k * (x1 - x0) / 149
        big = 50 * math.sin(k / 9) if stage == 0 else 0
        pts.append((x, y0 + big * 0.5 + base[k] * deps[stage]))
    pts.append((x1, y0 + 300))
    c.poly(pts, mix(BG, WOODC, 1.0))
    for k, lab in enumerate(labs):
        x = 260 + k * 420
        on = k == stage
        c.rect(x - 180, 260, x + 180, 340, fill=mix(BG, SPARK if on else SHEET, 0.9 if on else 1.0), r=10)
        c.text(x, 300, lab, 'bold', 22, INK if on else MUTED, 'mm')
    c.text(960, 960 - 40, '表面截面，放大示意', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '直接用细砂纸磨大坑，磨半天也磨不平；直接只用粗砂纸，表面又全是深沟'),
                (7.2, 14, '粗的负责「磨平」，细的负责「磨光」：一号接一号，划痕越来越浅'),
                (14.2, 22, '在报纸上磨、戴口罩，磨完洗手：木屑和金属粉都别吸进去')], y=1010)


CLIPS = {
 'E228_磁畴': (e228_domains, 22), 'E228_敲乱': (e228_knock, 22),
 'E228_片头': (titles.opening(SER43, VOL43, S43A, 6, '20 世纪出现带磁性刀头的螺丝刀'), 7),
 'E228_片尾': (titles.closing(SER43, VOL43, S43A, 6, '下集：万用表怎么读出看不见的电？'), 7),
 'E229_电压': (e229_voltage, 22), 'E229_电阻': (e229_resist, 22),
 'E229_片头': (titles.opening(SER43, VOL43, S43A, 7, '1920 年代出现可测电压、电流、电阻的万用表'), 7),
 'E229_片尾': (titles.closing(SER43, VOL43, S43A, 7, '下集：砂纸背面的数字是什么意思？'), 7),
 'E230_砂粒': (e230_grit, 22), 'E230_粗细': (e230_sequence, 22),
 'E230_片头': (titles.opening(SER43, VOL43, S43A, 8, '13 世纪中国已有砂粒粘在纸上的打磨纸'), 7),
 'E230_片尾': (titles.closing(SER43, VOL43, S43A, 8, '下集：吸盘到底是被什么「吸」住的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
