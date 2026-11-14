"""第四十八季（古法解密 21.0：作坊与街巷）第三批：B216 杵臼、B217 粽子、B218 背篓 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s48a import SB48, VOL48, ROPE

STONE = (150, 150, 145)
BEAN = (220, 200, 120)
LEAF = (110, 160, 90)
SKIN = (220, 180, 150)
CLOTH = (110, 130, 190)


# ---------------------------------------------------------------- B216 杵臼
def b216_impact(c, t, i):
    corner_tag(c, 'B216 · 一下子停住，冲击力大')
    c.text(60, 96, '手慢慢压，力一直不大；杵从高处落下，碰到豆子时一下子停住，这一瞬间的力比手压大得多', 'serif', 36, INK)
    for j, (lab, drop) in enumerate([('慢慢压', False), ('从高处落下', True)]):
        cx, by = 480 + j * 960, 760
        c.arc(cx, by - 120, 220, 160, 0, 180, mix(BG, STONE, 1.0), 26)
        ph = (t % 3) / 3
        if drop:
            if ph < 0.5:
                y = 300 + (by + 8 - 300) * (ph / 0.5) ** 2
            else:
                y = by + 8 - (by + 8 - 300) * ((ph - 0.5) / 0.5)
            hit = abs(ph - 0.5) < 0.04
        else:
            y = by - 20 + 22 * math.sin(ph * math.pi)
            hit = False
        c.rect(cx - 30, y - 300, cx + 30, y, fill=mix(BG, WOOD, 1.0), r=10)
        for k in range(5):
            bx = cx - 60 + k * 30
            br = 12
            crushed = drop and (t > 3)
            if crushed and abs(bx - cx) < 80:
                c.ellipse(bx, by + 22, br * 1.4, br * 0.5, fill=mix(BG, BEAN, 1.0))
            else:
                c.ellipse(bx, by + 18, br, br, fill=mix(BG, BEAN, 1.0))
        f = 1.0 if hit else (0.15 if not drop else 0.05)
        if not drop:
            f = 0.15
        c.rect(cx - 200, 880, cx - 200 + 400 * f, 910, fill=NRED if hit else LINE, r=6)
        c.text(cx, 950, lab + ('：冲击！' if hit else ''), 'bold', 26, NRED if hit else INK, 'mm')
    caps(c, t, [(0, 7, '手压：力慢慢加，豆子还能滑开、慢慢顶住'),
                (7.2, 14, '杵落下：速度很快，碰到豆子在一瞬间停住'),
                (14.2, 22, '停得越急、杵越重、举得越高，冲击力越大，豆子一下就碎（示意，以实测为准）')], y=1010)


def b216_mortar(c, t, i):
    corner_tag(c, 'B216 · 臼要又重又硬')
    c.text(60, 96, '臼放在软东西上，杵一砸臼就往下陷，力被吸收掉了；又重又硬的臼稳稳不动，力都用在豆子上', 'serif', 36, INK)
    ph = (t % 3) / 3
    for j, (lab, soft) in enumerate([('臼下垫海绵：力被吸走', True), ('又重又硬的臼：力都用上', False)]):
        cx, by = 480 + j * 960, 720
        sink = 0
        if soft and 0.45 < ph < 0.75:
            sink = 40 * math.sin((ph - 0.45) / 0.3 * math.pi)
        if soft:
            c.rect(cx - 260, by + 40 + sink * 0.5, cx + 260, by + 120, fill=mix(BG, (230, 210, 120), 0.8), r=20)
        else:
            c.rect(cx - 260, by + 40, cx + 260, by + 120, fill=mix(BG, STONE, 0.6))
        c.arc(cx, by - 100 + sink, 220, 160, 0, 180, mix(BG, STONE, 1.0), 26)
        if ph < 0.5:
            y = 280 + (by + 40 - 280) * (ph / 0.5) ** 2
        else:
            y = by + 40 - (by + 40 - 280) * ((ph - 0.5) / 0.5)
        c.rect(cx - 30, y - 260 + sink, cx + 30, y + sink, fill=mix(BG, WOOD, 1.0), r=10)
        c.text(cx, 900, lab, 'bold', 26, NRED if soft else GREEN, 'mm')
    caps(c, t, [(0, 7, '同样从 20 厘米落下'),
                (7.2, 14, '垫了海绵：臼往下一沉，一部分力用来压海绵了'),
                (14.2, 22, '又重又硬的臼：不晃、不陷，豆子碎得最多；臼底是圆的，豆子会滑回中间')], y=1010)


# ---------------------------------------------------------------- B217 粽子
def b217_cone(c, t, i):
    corner_tag(c, 'B217 · 先卷成漏斗')
    c.text(60, 96, '一条长叶子，从三分之一处往里一折、一卷，就成了一个尖底的漏斗：先装米，再往下折盖口', 'serif', 36, INK)
    ph = min(1.0, (t % 22) / 10)
    cx, cy = 760, 560
    if ph < 0.5:
        q = ph / 0.5
        L = 900
        c.poly([(cx - L / 2, cy - 40), (cx + L / 2, cy - 40), (cx + L / 2, cy + 40), (cx - L / 2, cy + 40)], mix(BG, LEAF, 1.0))
        fx = cx - L / 2 + L / 3
        c.line([(fx, cy - 50), (fx, cy + 50)], SPARK, 3)
        c.text(fx, cy + 90, '三分之一处', 'bold', 24, SPARK, 'mm')
        a = q * math.pi / 3
        x1 = fx - (L / 3) * math.cos(a)
        y1 = cy - (L / 3) * math.sin(a)
        c.line([(fx, cy), (x1, y1)], mix(BG, LEAF, 0.6), 80)
    else:
        q = (ph - 0.5) / 0.5
        top = cy - 220
        c.poly([(cx - 180, top), (cx + 180, top), (cx, cy + 220)], mix(BG, LEAF, 1.0))
        c.line([(cx - 180, top), (cx + 180, top)], mix(BG, LEAF, 0.6), 6)
        lvl = top + (cy + 200 - top) * (1 - q)
        if q > 0:
            w = 180 * (cy + 220 - lvl) / (cy + 220 - top)
            c.poly([(cx - w, lvl), (cx + w, lvl), (cx, cy + 200)], mix(BG, (120, 170, 90), 0.9))
            random.seed(2)
            for k in range(int(40 * q)):
                yy = random.uniform(lvl + 8, cy + 190)
                ww = 170 * (cy + 220 - yy) / (cy + 220 - top)
                c.ellipse(cx + random.uniform(-ww * 0.8, ww * 0.8), yy, 7, 7, fill=mix(BG, (120, 180, 80), 1.0))
        c.text(cx + 260, cy, '漏斗：装绿豆', 'bold', 28, INK, 'lm')
    caps(c, t, [(0, 7, '长叶子（实验用牛皮纸条）从三分之一处向内折'),
                (7.2, 14, '一卷，成了一个尖底的漏斗，用手捏住'),
                (14.2, 22, '装进几勺绿豆（实验用，不吃），下一步把剩下的叶子折过来盖口')], y=1010)


def b217_tetra(c, t, i):
    corner_tag(c, 'B217 · 四个三角形，合成四面体')
    c.text(60, 96, '剩下的叶子往下一折盖住开口，沿着边再折一次：包好的粽子有四个面、四个角，每个面都是三角形', 'serif', 36, INK)
    a = t * 0.5
    cx, cy, R = 760, 560, 260
    V = [(0, 1, 0), (0.943, -0.333, 0), (-0.471, -0.333, 0.816), (-0.471, -0.333, -0.816)]
    def P(v):
        x, y, z = v
        xr = x * math.cos(a) + z * math.sin(a)
        zr = -x * math.sin(a) + z * math.cos(a)
        yr = y * math.cos(0.35) - zr * math.sin(0.35)
        zz = y * math.sin(0.35) + zr * math.cos(0.35)
        return (cx + R * xr, cy - R * yr, zz)
    pts = [P(v) for v in V]
    faces = [(0, 1, 2), (0, 2, 3), (0, 3, 1), (1, 2, 3)]
    faces.sort(key=lambda f: sum(pts[k][2] for k in f) / 3)
    shades = [0.55, 0.7, 0.85, 1.0]
    for k, f in enumerate(faces):
        c.poly([(pts[j][0], pts[j][1]) for j in f], mix(BG, LEAF, shades[k]))
        for a1, b1 in [(f[0], f[1]), (f[1], f[2]), (f[2], f[0])]:
            c.line([(pts[a1][0], pts[a1][1]), (pts[b1][0], pts[b1][1])], mix(BG, INK, 0.4), 2)
    c.text(1450, 420, '4 个面（三角形）', 'bold', 32, INK, 'mm')
    c.text(1450, 490, '4 个角', 'bold', 32, INK, 'mm')
    c.text(1450, 560, '6 条棱', 'bold', 32, INK, 'mm')
    c.text(1450, 660, '开口全被叶子盖住', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '漏斗本身就是两个面；剩下的叶子往下折，又盖出两个面'),
                (7.2, 14, '最后合成一个四面体：四个三角形面，四个尖角'),
                (14.2, 22, '用绳子缠两圈系紧，倒过来摇也不漏（本集不煮粽子）')], y=1010)


# ---------------------------------------------------------------- B218 背篓
def _person(c, x, gy, lean):
    hx, hy = x + 260 * math.sin(lean), gy - 520 * math.cos(lean)
    c.line([(x, gy), (x + 300 * math.sin(lean), gy - 300 * math.cos(lean))], mix(BG, CLOTH, 1.0), 40)
    c.line([(x + 300 * math.sin(lean), gy - 300 * math.cos(lean)), (hx, hy + 40)], mix(BG, CLOTH, 1.0), 50)
    c.ellipse(hx + 10 * math.sin(lean), hy, 40, 40, fill=mix(BG, SKIN, 1.0))
    return hx, hy


def b218_center(c, t, i):
    corner_tag(c, 'B218 · 贴着后背，压在重心上方')
    c.text(60, 96, '背篓贴着后背，重物几乎压在身体正上方，人稍微往前一倾就站稳；手提时重物离身体远，身体要歪着撑', 'serif', 36, INK)
    gy = 860
    k = int((t % 21) // 7)
    labs = ['贴着后背', '离开后背 15 厘米', '单手提着']
    leans = [0.10, 0.22, -0.20]
    for j in range(3):
        x = 330 + j * 630
        lean = leans[j]
        hx, hy = _person(c, x, gy, lean if j != 2 else 0.14)
        if j == 2:
            c.line([(x + 60, gy - 460), (x - 140, gy - 300)], mix(BG, SKIN, 1.0), 14)
            c.rect(x - 200, gy - 300, x - 80, gy - 170, fill=mix(BG, STRAW, 1.0), r=10)
            c.text(x, gy - 600, '身体往另一边歪', 'bold', 22, NRED, 'mm')
            c.line([(x, gy), (x + 120, gy - 520)], NRED, 3)
        else:
            off = 60 if j == 0 else 160
            bx = x - off - 60 * j
            c.poly([(bx - 70, gy - 560), (bx + 70, gy - 560), (bx + 45, gy - 300), (bx - 45, gy - 300)], mix(BG, STRAW, 1.0))
            c.line([(x, gy), (x, gy - 620)], GREEN if j == 0 else SPARK, 2)
        c.text(x, gy + 60, labs[j], 'bold', 26, GREEN if j == 0 else (SPARK if j == 1 else NRED), 'mm')
        if j == k:
            c.rect(x - 220, 230, x + 220, gy + 90, outline=SPARK, width=3, r=12)
    caps(c, t, [(0, 7, '背篓贴着后背：重物在身体正上方附近，只要稍微前倾'),
                (7.2, 14, '背篓离开后背：重物往后跑，人要更往前弯着腰才不往后倒'),
                (14.2, 22, '单手提：重物在身体一侧，身体往另一边歪着撑，最累（示意，以实测为准）')], y=1010)


def b218_shape(c, t, i):
    corner_tag(c, 'B218 · 上宽下窄，重的在下面')
    c.text(60, 96, '背篓上宽下窄：重东西沉在窄窄的底部，贴着腰；轻的东西在上面的宽口里，整个重心又低又靠近身体', 'serif', 36, INK)
    gy = 860
    for j, (lab, heavy_low) in enumerate([('重的放上面：重心高，晃', False), ('重的放下面：重心低，稳', True)]):
        x = 520 + j * 900
        sway = (0.10 if not heavy_low else 0.03) * math.sin(t * 2)
        hx, hy = _person(c, x, gy, 0.08 + sway)
        bx = x - 90
        top, bot = gy - 600, gy - 300
        c.poly([(bx - 90, top), (bx + 60, top), (bx + 35, bot), (bx - 65, bot)], mix(BG, STRAW, 1.0))
        hb, lb = (bot - 100, top + 20) if heavy_low else (top + 20, bot - 100)
        c.rect(bx - 60, hb, bx + 30, hb + 80, fill=mix(BG, (90, 90, 95), 1.0), r=6)
        c.text(bx - 15, hb + 40, '重', 'bold', 26, BG, 'mm')
        c.rect(bx - 60, lb, bx + 30, lb + 80, fill=mix(BG, (245, 240, 220), 1.0), r=6)
        c.text(bx - 15, lb + 40, '轻', 'bold', 26, INK if False else (60, 60, 60), 'mm')
        gyc = (bot - 130) if heavy_low else (top + 110)
        c.ellipse(bx - 15, gyc, 14, 14, fill=NRED)
        c.text(bx - 50, gyc, '重心', 'bold', 22, NRED, 'rm')
        c.text(x, gy + 60, lab, 'bold', 26, GREEN if heavy_low else NRED, 'mm')
    caps(c, t, [(0, 7, '同样 3 千克的东西，换一下上下的位置'),
                (7.2, 14, '重的在上面：重心高，人一转身就晃'),
                (14.2, 22, '重的在下面：重心低、贴着腰，走山路也稳（米袋小孩不超过 1.5 千克）')], y=1010)


CLIPS = {
 'B216_冲击': (b216_impact, 22), 'B216_硬臼': (b216_mortar, 22),
 'B216_片头': (titles.opening(BSER, VOL48, SB48, 6, '新石器时代已有石臼和木杵'), 7),
 'B216_片尾': (titles.closing(BSER, VOL48, SB48, 6, '下集：一片叶子，怎么包得严严实实？'), 7),
 'B217_漏斗': (b217_cone, 22), 'B217_四面体': (b217_tetra, 22),
 'B217_片头': (titles.opening(BSER, VOL48, SB48, 7, '魏晋时已有用叶子包米的「角黍」'), 7),
 'B217_片尾': (titles.closing(BSER, VOL48, SB48, 7, '下集：山里人背东西，为什么偏偏背在背上？'), 7),
 'B218_重心': (b218_center, 22), 'B218_上宽': (b218_shape, 22),
 'B218_片头': (titles.opening(BSER, VOL48, SB48, 8, '西南山区至今常用竹背篓'), 7),
 'B218_片尾': (titles.closing(BSER, VOL48, SB48, 8, '下集：抓子儿时，子要抛多高才来得及？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
