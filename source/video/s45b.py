"""第四十五季（第十九层：玩具箱）第二批：E235 泡泡、E236 史莱姆、E237 积木 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s45a import S45A, SER45, VOL45, GEMS

WATERC = (110, 170, 230)
SOAP = (240, 200, 90)
STARCH = (235, 230, 215)
BRICK = (220, 60, 50)
BRICK2 = (60, 120, 210)


# ---------------------------------------------------------------- E235 泡泡
def e235_tension(c, t, i):
    corner_tag(c, '第 235 集 · 表面张力变小，膜才拉得开')
    c.text(60, 96, '水面的分子互相拉得很紧，一拉成薄膜就破；洗洁精挤到水面，把这股拉力变小，水膜就能被吹得又薄又大', 'serif', 36, INK)
    for j, (lab, soap) in enumerate([('清水：拉力太大，一吹就破', False), ('加洗洁精：拉力变小，吹成泡泡', True)]):
        ox, oy = 480 + j * 960, 520
        n = 9
        pull = 1.0 if not soap else 0.45
        for k in range(n):
            x = ox - 320 + k * 80
            col = WATERC
            c.ellipse(x, oy, 22, 22, fill=mix(BG, col, 1.0))
            if soap and k % 2 == 1:
                c.ellipse(x, oy - 34, 12, 12, fill=mix(BG, SOAP, 1.0))
                c.line([(x, oy - 22), (x, oy - 46)], mix(BG, SOAP, 1.0), 4)
            if k < n - 1:
                c.line([(x + 22, oy), (x + 58, oy)], mix(BG, NRED, 0.4 + 0.6 * pull), int(2 + 6 * pull))
        R = 150 * min(1.0, t / 10) if soap else 60 * abs(math.sin(t * 1.4))
        bx, by = ox, oy + 230
        if soap:
            c.ellipse(bx, by, R, R * 0.95, outline=mix(BG, WATERC, 0.8), width=4)
        elif (t * 1.4) % math.pi < 2.6:
            c.ellipse(bx, by, R, R * 0.95, outline=mix(BG, WATERC, 0.8), width=4)
        else:
            r = random.Random(int(t * 10))
            for k in range(10):
                c.ellipse(bx + r.uniform(-60, 60), by + r.uniform(-60, 60), 5, 5, fill=WATERC)
        c.text(ox, oy - 110, lab, 'bold', 26, GREEN if soap else NRED, 'mm')
    caps(c, t, [(0, 7, '水面上的水分子手拉着手，拉得很紧：这就是表面张力'),
                (7.2, 14, '清水吹成膜，拉力太大，膜一薄就被扯破'),
                (14.2, 22, '洗洁精的分子挤到水面，让拉力变小，膜就能拉得又大又薄；加点甘油还能慢点干（示意）')], y=1010)


def e235_colors(c, t, i):
    corner_tag(c, '第 235 集 · 膜有多厚，就是什么颜色')
    c.text(60, 96, '光在泡泡膜的外面和里面各反射一次，两束光叠在一起：膜厚不同，加强的颜色就不同，彩虹色就流了起来', 'serif', 35, INK)
    cx, cy, R = 600, 540, 300
    c.ellipse(cx, cy, R, R, fill=mix(BG, (20, 22, 30), 1.0))
    for k in range(60):
        f = k / 60
        y = cy - R + f * 2 * R
        w = math.sqrt(max(0, R * R - (y - cy) ** 2))
        th = f + 0.15 * math.sin(t * 0.8 + f * 6)
        hue = (th * 3) % 1
        col = (int(128 + 127 * math.sin(2 * math.pi * hue)), int(128 + 127 * math.sin(2 * math.pi * hue + 2.1)), int(128 + 127 * math.sin(2 * math.pi * hue + 4.2)))
        c.line([(cx - w, y), (cx + w, y)], mix(BG, col, 0.55), int(2 * R / 60) + 2)
    c.ellipse(cx, cy, R, R, outline=mix(BG, (220, 230, 240), 0.6), width=3)
    ox, oy = 1300, 560
    c.line([(ox, oy - 160), (ox, oy + 160)], mix(BG, WATERC, 1.0), 6)
    c.line([(ox + 60, oy - 160), (ox + 60, oy + 160)], mix(BG, WATERC, 1.0), 6)
    c.text(ox + 30, oy + 200, '膜（放大）', 'sans', 22, MUTED, 'mm')
    c.arrow(ox - 300, oy - 120, ox - 4, oy - 20, SPARK, 5, 16)
    c.arrow(ox - 4, oy - 20, ox - 300, oy + 60, mix(BG, SPARK, 0.7), 4, 14)
    c.arrow(ox + 56, oy - 10, ox - 300, oy + 110, mix(BG, (120, 200, 255), 0.9), 4, 14)
    c.text(ox - 320, oy + 160, '两束反射光叠加：\n厚度决定哪种颜色变亮', 'sans', 22, INK, 'lm')
    caps(c, t, [(0, 7, '泡泡膜只有头发丝的几百分之一那么薄，上面薄下面厚，还在不停地流'),
                (7.2, 14, '光在膜的外面和里面各反射一次，两束光叠在一起，有的颜色加强，有的抵消'),
                (14.2, 22, '膜越来越薄，颜色一圈圈变；膜薄到一定程度变成黑色，泡泡就快破了（示意）')], y=1010)


# ---------------------------------------------------------------- E236 史莱姆
def e236_shear(c, t, i):
    corner_tag(c, '第 236 集 · 慢是水，快是石')
    c.text(60, 96, '淀粉颗粒悬在水里：慢慢插，水在颗粒之间当润滑，手指滑进去；猛地一砸，水来不及流开，颗粒挤死，像石头一样硬', 'serif', 35, INK)
    for j, (lab, fast) in enumerate([('慢慢插：颗粒让开，像液体', False), ('猛地砸：颗粒卡死，像固体', True)]):
        ox, oy = 480 + j * 960, 600
        r = random.Random(5)
        T = 4.0
        ph = (t % T) / T
        depth = (ph * 220 if not fast else min(25, ph * 400))
        for k in range(110):
            x = ox + r.uniform(-300, 300)
            y = oy + r.uniform(-120, 200)
            dx = 0
            if not fast and abs(x - ox) < 90 and y < oy - 120 + depth + 40:
                dx = 60 * (1 if x > ox else -1) * min(1.0, depth / 200)
            c.ellipse(x + dx, y, 16, 16, fill=mix(BG, STARCH, 0.9))
            if not fast:
                c.ellipse(x + dx, y, 22, 22, outline=mix(BG, (140, 190, 240), 0.5), width=2)
        c.rect(ox - 320, oy - 140, ox + 320, oy + 220, outline=mix(BG, MUTED, 0.5), width=3, r=10)
        if fast:
            c.rect(ox - 50, oy - 250 + depth, ox + 50, oy - 140 + depth, fill=mix(BG, (230, 190, 160), 1.0), r=20)
            if ph > 0.06:
                c.text(ox + 100, oy - 200, '砰！', 'bold', 34, SPARK, 'lm')
        else:
            c.rect(ox - 18, oy - 260 + depth, ox + 18, oy - 140 + depth, fill=mix(BG, (230, 190, 160), 1.0), r=16)
        c.text(ox, oy + 280, lab, 'bold', 26, GREEN if not fast else SPARK, 'mm')
    caps(c, t, [(0, 7, '玉米淀粉和水按大约 2 比 1 调成糊，慢慢用手指插，一下就进去了'),
                (7.2, 14, '用勺背猛地一拍，表面硬得弹手，像拍在石头上'),
                (14.2, 22, '受力越快越硬，叫剪切增稠：它是一种非牛顿流体（示意）')], y=1010)


def e236_compare(c, t, i):
    corner_tag(c, '第 236 集 · 和蜂蜜正好相反')
    c.text(60, 96, '普通液体搅得快慢都差不多稠；番茄酱、油漆越搅越稀；淀粉糊却越搅越稠：搅拌越快，阻力涨得越厉害', 'serif', 36, INK)
    x0, y0, W, H = 300, 260, 1300, 560
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 40, '搅拌速度 →', 'sans', 22, MUTED, 'mm')
    c.text(x0 + 20, y0 + 30, '阻力（示意）', 'sans', 22, MUTED, 'lm')
    p = min(1.0, t / 12)
    curves = [('蜂蜜：差不多不变', lambda u: 0.35, WATERC), ('番茄酱：越搅越稀', lambda u: 0.5 - 0.3 * u ** 0.6, NRED), ('淀粉糊：越搅越稠', lambda u: 0.15 + 0.75 * u ** 2.2, SPARK)]
    for k, (lab, f, col) in enumerate(curves):
        pts = []
        for m in range(101):
            u = m / 100
            if u > p:
                break
            pts.append((x0 + 40 + u * (W - 80), y0 + H - 40 - f(u) * (H - 80)))
        if len(pts) > 1:
            c.line(pts, col, 5)
            c.text(pts[-1][0] - 10, pts[-1][1] - 26, lab, 'bold', 22, col, 'rm')
    caps(c, t, [(0, 7, '用勺子在蜂蜜里慢搅、快搅，阻力差不多'),
                (7.2, 14, '在淀粉糊里慢搅很轻松，一快搅，勺子像被拽住'),
                (14.2, 22, '做完装袋扔进垃圾桶：倒进下水道，它在管子里会变硬堵住（示意）')], y=1010)


# ---------------------------------------------------------------- E237 积木
def _brick(c, x, y, n, col, w=80, h=90):
    c.rect(x, y, x + n * w, y + h, fill=mix(BG, col, 1.0), r=6)
    for k in range(n):
        cx = x + w / 2 + k * w
        c.rect(cx - 24, y - 18, cx + 24, y + 2, fill=mix(BG, col, 0.85), r=4)


def e237_fit(c, t, i):
    corner_tag(c, '第 237 集 · 差一点点，就挤紧了')
    c.text(60, 96, '上面积木底部的管柱和下面的凸点之间，故意做得比「刚好」再紧一丝：按下去塑料微微变形，互相挤住，靠摩擦咬牢', 'serif', 35, INK)
    cx, cy = 700, 560
    p = min(1.0, t / 6)
    ox = cx - 200
    _brick(c, ox, cy, 4, BRICK2)
    top_y = cy - 200 + 200 * p
    c.rect(ox, top_y - 90, ox + 320, top_y, fill=mix(BG, BRICK, 1.0), r=6)
    for k in range(4):
        x = ox + 40 + k * 80
        c.rect(x - 24, top_y - 108, x + 24, top_y - 88, fill=mix(BG, BRICK, 0.85), r=4)
    zx, zy = 1450, 520
    c.ellipse(zx, zy, 230, 230, fill=mix(BG, (25, 27, 34), 1.0))
    c.ellipse(zx, zy, 230, 230, outline=MUTED, width=2)
    s = 1.0 + 0.04 * p
    c.ellipse(zx, zy, 90, 90, fill=mix(BG, BRICK2, 1.0))
    c.ellipse(zx, zy, 92 * s * 0 + 140, 140, outline=mix(BG, BRICK, 1.0), width=int(24 + 6 * p))
    c.text(zx, zy + 280, '放大俯视：管柱壁和凸点\n之间是过盈配合（示意）', 'sans', 22, MUTED, 'mm')
    if p >= 1:
        for k in range(8):
            a = k * math.pi / 4
            c.arrow(zx + 150 * math.cos(a), zy + 150 * math.sin(a), zx + 100 * math.cos(a), zy + 100 * math.sin(a), SPARK, 3, 10)
    caps(c, t, [(0, 7, '积木的凸点和别的积木底下的管柱，尺寸都做得极其精确'),
                (7.2, 14, '比「刚好放进去」再紧一丝：按下去，塑料轻轻变形，四面挤住'),
                (14.2, 22, '太紧按不进，太松一碰就掉：差的这一丝，叫公差（示意）')], y=1010)


def e237_pull(c, t, i):
    corner_tag(c, '第 237 集 · 凸点越多，越难拉开')
    c.text(60, 96, '每个凸点都贡献一份摩擦：扣住的凸点越多，拉开它们要的力越大；尺寸统一，几十年前的积木也能和今天的拼在一起', 'serif', 35, INK)
    p = min(1.0, t / 12)
    for k, (lab, n, f) in enumerate([('只扣 1 个凸点', 1, 1.0), ('2×2：扣 4 个', 4, 3.6), ('2×4：扣 8 个', 8, 7.0)]):
        y = 330 + k * 180
        _brick(c, 200, y, min(n, 4), BRICK2, 60, 60)
        c.rect(200, y - 70, 200 + min(n, 4) * 60, y - 10, fill=mix(BG, BRICK, 1.0), r=4)
        c.text(160, y, lab, 'bold', 24, INK, 'rm')
        w = f / 7 * 900 * p
        c.rect(560, y - 30, 560 + w, y + 30, fill=mix(BG, SPARK, 0.85), r=8)
        c.text(580 + w, y, f'约 {f:.0f} 份力', 'mono', 22, INK, 'lm')
    c.text(960, 900, '拉力为示意，以行李秤实测为准', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '下面一块用胶带固定，上面一块用细绳挂行李秤，竖直慢慢往上拉'),
                (7.2, 14, '扣 1 个凸点一拉就开；扣 8 个，要的力大好几倍'),
                (14.2, 22, '尺寸统一是关键：不同年份、不同品牌只要标准一样，就能拼（以实测为准）')], y=1010)


CLIPS = {
 'E235_张力': (e235_tension, 22), 'E235_彩色': (e235_colors, 22),
 'E235_片头': (titles.opening(SER45, VOL45, S45A, 3, '17 世纪荷兰画作中已有孩子吹肥皂泡'), 7),
 'E235_片尾': (titles.closing(SER45, VOL45, S45A, 3, '下集：一碗淀粉糊，到底是固体还是液体？'), 7),
 'E236_快慢': (e236_shear, 22), 'E236_对比': (e236_compare, 22),
 'E236_片头': (titles.opening(SER45, VOL45, S45A, 4, '20 世纪 70 年代出现玩具史莱姆'), 7),
 'E236_片尾': (titles.closing(SER45, VOL45, S45A, 4, '下集：几十年前的积木，为什么还能和今天的拼上？'), 7),
 'E237_过盈': (e237_fit, 22), 'E237_拉力': (e237_pull, 22),
 'E237_片头': (titles.opening(SER45, VOL45, S45A, 5, '1958 年乐高申请了带凸点和管柱的积木专利'), 7),
 'E237_片尾': (titles.closing(SER45, VOL45, S45A, 5, '下集：遥控车没有线，信号是怎么飞过去的？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
