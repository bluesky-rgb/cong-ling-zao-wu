"""第四十一季（第十七层：书桌与办公室）第一批：E212 订书机、E213 回形针、E214 便利贴 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S41A = [('212', '订书机'), ('213', '回形针'), ('214', '便利贴'), ('215', '修正带'), ('216', '自动铅笔'),
        ('217', '荧光笔'), ('218', '碎纸机'), ('219', '复印机'), ('220', '扫描仪'), ('221', '键盘')]
SER41, VOL41 = '从零造物', '第四十一季 · 第十七层：书桌与办公室'
STEEL = (185, 190, 200)
PAPERC = (235, 232, 222)
NOTE = (250, 220, 90)
GLUE = (240, 180, 120)
BODY = (200, 70, 70)


# ---------------------------------------------------------------- E212 订书机
def e212_lever(c, t, i):
    corner_tag(c, '第 212 集 · 长柄把力放大')
    c.text(60, 96, '手按在长柄末端，转轴在后面，钉头离转轴近：手上一点力，到钉头上变成好几倍', 'serif', 36, INK)
    px, py = 300, 620
    T = 4
    ph = (t % T) / T
    ang = math.radians(14) * (0.5 + 0.5 * math.cos(ph * 2 * math.pi))
    L = 1100
    ex, ey = px + L * math.cos(ang), py - L * math.sin(ang)
    c.rect(px - 40, py + 40, px + L + 40, py + 90, fill=mix(BG, (90, 90, 100), 0.9), r=10)
    c.line([(px, py), (ex, ey)], BODY, 46)
    c.ellipse(px, py, 22, 22, fill=INK)
    c.text(px, py + 130, '转轴', 'sans', 22, MUTED, 'mm')
    sx = px + 300
    sy = py - 300 * math.sin(ang)
    c.rect(sx - 30, sy + 20, sx + 30, py + 30, fill=mix(BG, STEEL, 0.6))
    c.text(sx, py + 130, '钉头', 'sans', 22, MUTED, 'mm')
    c.arrow(ex - 40, ey - 160, ex - 40, ey - 30, SPARK, 6, 18)
    c.text(ex - 40, ey - 190, '手：1 份力', 'bold', 24, SPARK, 'mm')
    c.arrow(sx, sy - 160, sx, sy - 30, NRED, 12, 26)
    c.text(sx + 40, sy - 160, '钉头：约 3–4 份力（示意）', 'bold', 24, NRED, 'lm')
    caps(c, t, [(0, 7, '订书机就是一根杠杆：转轴在一头，手按在另一头'),
                (7.2, 14, '钉头离转轴近，手离转轴远：手动得多，钉头动得少'),
                (14.2, 22, '省了力，就能把钉子压穿厚厚一叠纸：按的位置越靠末端越省力（示意）')], y=1010)


def e212_clinch(c, t, i):
    corner_tag(c, 'E212 · 底座凹槽把钉脚引弯')
    c.text(60, 96, '钉脚穿过纸，撞到底座上一对弧形凹槽：凹槽像滑梯一样把钉脚引着往里弯，两只脚相对合拢', 'serif', 36, INK)
    for j, (lab, inward) in enumerate([('正常底座：钉脚往里弯，夹紧纸', True), ('旋转底座：钉脚往外弯，方便拆', False)]):
        cx, base = 520 + j * 880, 640
        c.rect(cx - 300, base, cx + 300, base + 60, fill=mix(BG, (90, 90, 100), 0.9), r=8)
        for sgn in (-1, 1):
            gx = cx + sgn * 110
            c.arc(gx + (-sgn * 30 if inward else sgn * 30), base, 40, 30, 180, 360, mix(BG, (60, 60, 65), 1.0), 6)
        c.rect(cx - 220, base - 80, cx + 220, base, fill=mix(BG, PAPERC, 0.9))
        p = min(1.0, (t % 8) / 5)
        top = base - 180 + 100 * min(1, p * 1.6)
        c.line([(cx - 110, top), (cx + 110, top)], STEEL, 8)
        bend = max(0, (p - 0.6) / 0.4)
        for sgn in (-1, 1):
            x0 = cx + sgn * 110
            yb = min(base + 10, top + 90)
            c.line([(x0, top), (x0, yb)], STEEL, 8)
            if bend > 0:
                dirx = -sgn if inward else sgn
                c.line([(x0, yb), (x0 + dirx * 70 * bend, yb + 14 * bend)], STEEL, 8)
        c.text(cx, base + 140, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '订书钉是一根弯成 U 形的细钢丝，两只脚向下'),
                (7.2, 14, '钉脚穿透纸以后，撞上底座的弧形凹槽，顺着弧面往里拐'),
                (14.2, 22, '两只脚贴着纸背合拢，纸就被夹住了；底座转个方向，钉脚往外弯，好拆')], y=1010)


# ---------------------------------------------------------------- E213 回形针
def _clip_shape(cx, cy, s, open_):
    pts = []
    for k in range(60):
        a = math.pi / 2 + k / 59 * math.pi
        pts.append((cx - 160 * s + 60 * s * math.cos(a), cy + 60 * s * math.sin(a)))
    pts.append((cx + 160 * s, cy + 60 * s))
    for k in range(60):
        a = math.pi / 2 - k / 59 * math.pi
        pts.append((cx + 160 * s + 60 * s * math.cos(a), cy + 60 * s * math.sin(a) - open_ * 0))
    pts.append((cx - 100 * s, cy - 60 * s))
    for k in range(40):
        a = -math.pi / 2 - k / 39 * math.pi
        pts.append((cx - 100 * s + 40 * s * math.cos(a), cy - 20 * s + 40 * s * math.sin(a) + open_ * 40 * (k / 39)))
    pts.append((cx + 110 * s, cy + 20 * s + open_ * 40))
    return pts


def e213_spring(c, t, i):
    corner_tag(c, '第 213 集 · 撑开一点，自己弹回来')
    c.text(60, 96, '夹几张纸，钢丝只被撑开一点点，松开就弹回原样；夹得太厚，撑过了头，就回不去了', 'serif', 36, INK)
    for j, (lab, op, back) in enumerate([('夹 2 张：弹回原样', 0.3, 1.0), ('夹 10 张：还能弹回', 0.8, 1.0), ('夹 30 张：撑开回不去', 1.8, 0.4)]):
        cx, cy = 330 + j * 630, 520
        T = 6
        ph = (t % T) / T
        load = math.sin(math.pi * min(1, ph * 2)) if ph < 0.5 else 0
        o = op * load if ph < 0.5 else op * (1 - back)
        c.line(_clip_shape(cx, cy, 1.0, o), STEEL, 7)
        if ph < 0.5:
            c.rect(cx - 40, cy + 10, cx + 220, cy + 20 + 30 * o, fill=mix(BG, PAPERC, 0.8))
        c.text(cx, cy + 200, lab, 'bold', 24, NRED if back < 1 else GREEN, 'mm')
    caps(c, t, [(0, 7, '钢丝被撑开一点点，就像弹簧，松手就弹回去：这叫弹性'),
                (7.2, 14, '撑开太多，钢丝里面的结构被永久挪动了，松手回不去：这叫塑性'),
                (14.2, 22, '回形针设计成只夹薄薄一叠，一直待在弹性范围里，能用很多次（示意）')], y=1010)


def e213_fatigue(c, t, i):
    corner_tag(c, 'E213 · 来回弯，伤痕越来越大')
    c.text(60, 96, '同一个地方来回弯：每弯一次，弯处的金属里就多一点细小的裂纹；裂纹连成一片，钢丝就断了', 'serif', 36, INK)
    cx, cy = 700, 560
    n = min(12, int(t / 1.5))
    ang = math.radians(60) * math.sin(t * 2.1) if n < 12 else math.radians(80)
    c.line([(cx - 500, cy), (cx, cy)], STEEL, 12)
    ex, ey = cx + 400 * math.cos(ang), cy - 400 * math.sin(ang)
    if n < 12:
        c.line([(cx, cy), (ex, ey)], STEEL, 12)
    else:
        c.line([(cx + 30, cy + 40), (cx + 380, cy + 160)], STEEL, 12)
        c.text(cx + 40, cy + 60, '断了！', 'bold', 30, NRED, 'lm')
    r = random.Random(1)
    for k in range(n * 3):
        a = r.uniform(0, 2 * math.pi)
        rr = r.uniform(4, 22)
        c.line([(cx + rr * math.cos(a), cy + rr * math.sin(a)), (cx + (rr + 10) * math.cos(a + 0.3), cy + (rr + 10) * math.sin(a + 0.3))], NRED, 2)
    c.rect(1320, 300, 1860, 560, fill=SHEET, r=12)
    c.text(1590, 350, '已经弯了', 'bold', 26, INK, 'mm')
    c.text(1590, 430, f'{n} 次', 'mono', 48, SPARK, 'mm')
    c.text(1590, 510, '断的次数以实测为准', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '把回形针掰直，在同一个位置来回弯'),
                (7.2, 14, '每弯一次，弯处都超出了弹性范围，留下细小的伤痕'),
                (14.2, 22, '伤痕一次次累积、连起来，钢丝就断了：这叫金属疲劳，飞机、桥梁都要防它')], y=1010)


# ---------------------------------------------------------------- E214 便利贴
def e214_spheres(c, t, i):
    corner_tag(c, '第 214 集 · 一颗颗小胶粒')
    c.text(60, 96, '放大便利贴背面：胶不是一整层，而是一颗颗很小的弹性胶粒，只有一部分碰到纸面', 'serif', 36, INK)
    for j, (lab, mode) in enumerate([('普通胶带：一整层胶，全贴住', 0), ('便利贴：一颗颗胶粒，只碰一部分', 1)]):
        cx, cy = 520 + j * 880, 560
        c.rect(cx - 340, cy - 140, cx + 340, cy - 100, fill=mix(BG, NOTE if mode else (220, 220, 230), 0.95))
        if mode == 0:
            c.rect(cx - 340, cy - 100, cx + 340, cy - 70, fill=mix(BG, GLUE, 0.9))
        else:
            for k in range(14):
                x = cx - 320 + k * 48
                rr = 18 + (k * 7) % 9
                c.ellipse(x, cy - 100 + rr * 0.7, rr, rr * 0.8, fill=mix(BG, GLUE, 0.95))
        c.rect(cx - 360, cy - 60, cx + 360, cy + 40, fill=mix(BG, PAPERC, 0.9))
        r = random.Random(j)
        for k in range(40):
            x = cx - 350 + r.uniform(0, 700)
            y = cy - 60 + r.uniform(0, 90)
            c.line([(x, y), (x + r.uniform(-30, 30), y + r.uniform(-6, 6))], mix(BG, (200, 190, 170), 1.0), 2)
        p = max(0, min(1, (t - 8) / 6))
        if p > 0:
            if mode == 0:
                for k in range(12):
                    x = cx - 300 + k * 52
                    c.line([(x, cy - 70 - 60 * p), (x + 10, cy - 50)], mix(BG, (200, 190, 170), 1.0), 3)
                c.text(cx, cy + 120, '撕的时候带走纸纤维', 'sans', 22, NRED, 'mm')
            else:
                c.text(cx, cy + 120, '轻轻撕下，纸面完好', 'sans', 22, GREEN, 'mm')
        c.text(cx, cy + 200, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '普通胶带的胶是平平的一整层，整片贴住纸'),
                (7.2, 14, '便利贴的胶是一颗颗有弹性的小胶粒，只有一部分顶端碰到纸'),
                (14.2, 22, '接触面积小，粘力刚好够贴住，撕的时候也不会把纸纤维扯下来（示意）')], y=1010)


def e214_reuse(c, t, i):
    corner_tag(c, 'E214 · 能反复贴好多次')
    c.text(60, 96, '每贴一次、撕一次，胶粒都被压一压又弹回去；慢慢沾上灰，粘力才一点点变弱', 'serif', 36, INK)
    x0, y0, W, H = 200, 260, 1100, 520
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 40, '贴撕次数', 'sans', 22, MUTED, 'mm')
    c.text(x0 + 20, y0 + 30, '粘力（示意）', 'sans', 20, MUTED, 'lm')
    tn = min(1.0, t / 14)
    for col, f, lab in [(GREEN, lambda n: 1.0 - 0.025 * n, '便利贴'), (NRED, lambda n: 1.0 if n < 1 else max(0.05, 0.25 - 0.05 * n), '普通胶带')]:
        pts = []
        for k in range(21):
            if k / 20 > tn:
                break
            pts.append((x0 + 40 + k / 20 * (W - 80), y0 + H - 40 - f(k) * (H - 100)))
        if len(pts) > 1:
            c.line(pts, col, 5)
    c.text(x0 + W + 20, y0 + 120, '便利贴：慢慢变弱', 'bold', 22, GREEN, 'lm')
    c.text(x0 + W + 20, y0 + H - 80, '胶带：撕一次就沾满纤维', 'bold', 22, NRED, 'lm')
    caps(c, t, [(0, 7, '小胶粒有弹性，贴上去被压扁一点，撕下来又鼓回去'),
                (7.2, 14, '胶粒很少被纸纤维带走，所以能一次次重复贴'),
                (14.2, 22, '真正让它不粘的是灰尘：贴撕几十次后挂不住夹子了（以实测为准）')], y=1010)


CLIPS = {
 'E212_杠杆': (e212_lever, 22), 'E212_弯脚': (e212_clinch, 22),
 'E212_片头': (titles.opening(SER41, VOL41, S41A, 0, '19 世纪末出现可装订书钉的订书机'), 7),
 'E212_片尾': (titles.closing(SER41, VOL41, S41A, 0, '下集：回形针为什么能夹纸，掰几次就断？'), 7),
 'E213_弹回': (e213_spring, 22), 'E213_疲劳': (e213_fatigue, 22),
 'E213_片头': (titles.opening(SER41, VOL41, S41A, 1, '19 世纪末出现双圈回形针'), 7),
 'E213_片尾': (titles.closing(SER41, VOL41, S41A, 1, '下集：便利贴为什么粘得住又撕得下？'), 7),
 'E214_胶粒': (e214_spheres, 22), 'E214_反复贴': (e214_reuse, 22),
 'E214_片头': (titles.opening(SER41, VOL41, S41A, 2, '1970 年代便利贴的低粘胶被推广'), 7),
 'E214_片尾': (titles.closing(SER41, VOL41, S41A, 2, '下集：修正带的白膜为什么乖乖留在纸上？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
