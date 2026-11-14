"""第四十九季（第二十一层：浴室）第一批：E252 牙刷、E253 牙膏、E254 花洒 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S49A = [('252', '牙刷'), ('253', '牙膏'), ('254', '花洒'), ('255', '镜子起雾'), ('256', '毛巾'),
        ('257', '浴帘'), ('258', '水龙头'), ('259', '指甲刀'), ('260', '吹风机'), ('261', '电动牙刷')]
SER49, VOL49 = '从零造物', '第四十九季 · 第二十一层：浴室'
TOOTH = (245, 245, 235)
BRISTLE = (90, 160, 220)
PASTE = (230, 240, 250)
WATER = (90, 160, 220)
PLAQUE = (220, 190, 110)
STEEL = (175, 185, 195)


# ---------------------------------------------------------------- E252 牙刷
def _teeth(c, y, gaps):
    for k in range(len(gaps) + 1):
        x0 = 260 + k * 300
        c.rect(x0, y, x0 + 260, y + 300, fill=mix(BG, TOOTH, 1.0), r=40)


def e252_gap(c, t, i):
    corner_tag(c, '第 252 集 · 细毛钻进缝里')
    c.text(60, 96, '毛巾是一整块布，只能擦到牙面；牙刷是成千上万根细毛，每一根都能弯着钻进窄缝，把缝里的东西拨出来', 'serif', 36, INK)
    y = 520
    for k in range(5):
        x0 = 220 + k * 300
        c.rect(x0, y, x0 + 260, y + 320, fill=mix(BG, TOOTH, 1.0), r=40)
    ph = min(1.0, (t % 22) / 14)
    for k in range(4):
        gx = 220 + k * 300 + 260
        left = 1 - ph if t > 7 else 1.0
        c.rect(gx + 6, y + 40, gx + 34, y + 40 + 200 * max(0.0, left), fill=mix(BG, PLAQUE, 1.0), r=6)
    if t < 7:
        c.rect(200, y - 60, 1720, y + 4, fill=mix(BG, (200, 200, 220), 0.9), r=16)
        c.text(960, y - 28, '毛巾：只碰到牙面', 'bold', 26, NRED, 'mm')
    else:
        hx = 220 + ((t * 120) % 1200)
        c.rect(hx - 40, y - 200, hx + 260, y - 150, fill=mix(BG, BRISTLE, 0.6), r=10)
        for b in range(14):
            bx = hx - 20 + b * 20
            gap_near = min(abs(bx - (220 + k * 300 + 280)) for k in range(4))
            tip = y + (90 if gap_near < 24 else 0)
            c.line([(bx, y - 150), (bx + 10, tip)], mix(BG, BRISTLE, 1.0), 4)
        c.text(960, y - 240, '牙刷：毛尖钻进缝里', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '用湿毛巾擦：牙面干净了，缝里的东西还在'),
                (7.2, 14, '换牙刷：刷毛又细又多，碰到缝，毛尖就弯着钻进去'),
                (14.2, 22, '来回几下，缝里的东西被一根根毛尖拨出来（示意）')], y=1010)


def e252_angle(c, t, i):
    corner_tag(c, '第 252 集 · 斜 45°，轻轻抖')
    c.text(60, 96, '用力压着刷，刷毛被压平，毛尖反而进不了缝；斜 45° 对着缝、小幅度抖，毛尖才钻得进去', 'serif', 36, INK)
    for j, (lab, ok) in enumerate([('用力压：刷毛压平', False), ('斜 45° 轻轻抖：毛尖进缝', True)]):
        cx, gy = 480 + j * 960, 640
        c.rect(cx - 340, gy, cx - 20, gy + 280, fill=mix(BG, TOOTH, 1.0), r=30)
        c.rect(cx + 20, gy, cx + 340, gy + 280, fill=mix(BG, TOOTH, 1.0), r=30)
        c.rect(cx - 16, gy + 20, cx + 16, gy + 180, fill=mix(BG, PLAQUE, 1.0) if not (ok and t > 12) else BG, r=6)
        wob = 14 * math.sin(t * 12) if ok else 0
        if ok:
            ang = math.radians(45)
            for b in range(10):
                bx = cx - 120 + b * 26 + wob
                ex, ey = bx + 150 * math.cos(ang), gy - 10 + 150 * math.sin(ang) - 150
                tipx = min(ex, cx + 10) if abs(ex - cx) < 60 else ex
                tipy = gy + 80 if abs(ex - cx) < 60 else gy - 6
                c.line([(bx, gy - 160), (tipx, tipy)], mix(BG, BRISTLE, 1.0), 4)
            c.rect(cx - 150 + wob, gy - 200, cx + 150 + wob, gy - 160, fill=mix(BG, BRISTLE, 0.6), r=8)
        else:
            c.rect(cx - 200, gy - 60, cx + 200, gy - 20, fill=mix(BG, BRISTLE, 0.6), r=8)
            for b in range(16):
                bx = cx - 190 + b * 25
                c.line([(bx, gy - 20), (bx + 40, gy - 4)], mix(BG, BRISTLE, 1.0), 4)
            c.arrow(cx, gy - 160, cx, gy - 70, NRED, 6, 16)
        c.text(cx, 980 - 40, lab, 'bold', 26, GREEN if ok else NRED, 'mm')
    caps(c, t, [(0, 7, '用力往下压，刷毛倒成一片，平平地贴在牙面上'),
                (7.2, 14, '斜着 45° 对准缝，毛尖正好朝着缝口'),
                (14.2, 22, '小幅度抖动，毛尖一次次钻进缝里（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- E253 牙膏
def e253_abrasive(c, t, i):
    corner_tag(c, '第 253 集 · 极细的磨料')
    c.text(60, 96, '牙膏里有很细很细的颗粒，像极细的砂纸：刷的时候把牙面上的污渍一点点磨掉，又细到不会磨伤牙', 'serif', 36, INK)
    gy = 700
    c.rect(200, gy, 1720, gy + 200, fill=mix(BG, TOOTH, 1.0))
    ph = min(1.0, (t % 22) / 16)
    random.seed(9)
    for k in range(60):
        x = 220 + k * 25
        if x > 220 + 1480 * ph:
            c.rect(x, gy - 14, x + 20, gy, fill=mix(BG, PLAQUE, 1.0))
    off = 300 * math.sin(t * 3)
    for k in range(40):
        x = 960 + off + random.uniform(-260, 260)
        y = gy - 26 - random.uniform(0, 30)
        c.ellipse(x, y, 7, 7, fill=mix(BG, (200, 200, 210), 1.0))
    c.rect(700 + off, gy - 180, 1220 + off, gy - 130, fill=mix(BG, BRISTLE, 0.6), r=10)
    for b in range(20):
        bx = 720 + off + b * 25
        c.line([(bx, gy - 130), (bx, gy - 40)], mix(BG, BRISTLE, 1.0), 3)
    c.text(1500, 360, '磨料颗粒：几微米到十几微米', 'bold', 28, INK, 'mm')
    c.text(1500, 420, '（示意，拍摄前核对）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '牙膏抹在黑卡纸上搓开，放大镜能看见一粒粒很细的颗粒'),
                (7.2, 14, '刷的时候，这些颗粒在刷毛下来回滚，把污渍一层层磨掉'),
                (14.2, 22, '颗粒细，只磨掉污渍，不伤牙面；泡沫帮着把碎屑带走')], y=1010)


def e253_fluoride(c, t, i):
    corner_tag(c, '第 253 集 · 氟让表面更耐酸')
    c.text(60, 96, '牙齿和蛋壳表面都怕酸；含氟牙膏能在表面换上一层更耐酸的成分：泡进醋里，涂过的那片冒泡少', 'serif', 36, INK)
    random.seed(3)
    for j, (lab, f) in enumerate([('没涂牙膏：冒泡多', False), ('涂过含氟牙膏：冒泡少', True)]):
        cx, cy = 480 + j * 960, 560
        c.rect(cx - 220, cy - 220, cx + 220, cy + 260, outline=mix(BG, INK, 0.5), width=4, r=20)
        c.rect(cx - 216, cy - 120, cx + 216, cy + 256, fill=mix(BG, (240, 230, 200), 0.35), r=18)
        c.ellipse(cx, cy + 120, 120, 50, fill=mix(BG, TOOTH, 1.0))
        if f:
            c.ellipse(cx, cy + 120, 124, 54, outline=GREEN, width=4)
        n = 6 if f else 30
        for k in range(n):
            ph = ((t * 0.5) + k / n) % 1
            x = cx + random.uniform(-100, 100)
            y = cy + 80 - ph * 220
            c.ellipse(x, y, 6, 6, outline=mix(BG, INK, 0.6), width=2)
        c.text(cx, cy + 320, lab, 'bold', 26, GREEN if f else NRED, 'mm')
    caps(c, t, [(0, 7, '蛋壳和牙齿表面的成分差不多，碰到酸都会慢慢溶掉、冒出小气泡'),
                (7.2, 14, '一片蛋壳先涂满含氟牙膏 10 分钟，冲干净'),
                (14.2, 22, '一起泡进白醋：涂过的那片冒泡少，表面更耐酸（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E254 花洒
def e254_holes(c, t, i):
    corner_tag(c, '第 254 集 · 孔越小越多，水越细越急')
    c.text(60, 96, '同样一瓶水用同样的力挤：瓶盖上 1 个大孔水往下流；20 个小孔，水一股股又细又急地喷出去', 'serif', 36, INK)
    random.seed(1)
    for j, (lab, n, v) in enumerate([('1 个孔', 1, 0.5), ('5 个孔', 5, 0.75), ('20 个孔', 20, 1.0)]):
        cx = 360 + j * 600
        c.rect(cx - 70, 260, cx + 70, 520, fill=mix(BG, WATER, 0.35), r=30)
        c.rect(cx - 80, 520, cx + 80, 560, fill=mix(BG, STEEL, 1.0), r=6)
        for k in range(n):
            a = (k - (n - 1) / 2) * (0.9 / max(1, n - 1)) if n > 1 else 0
            ox = cx + (k - (n - 1) / 2) * (120 / max(1, n))
            L = 340 * v
            w = 18 if n == 1 else (8 if n == 5 else 4)
            for s in range(10):
                f = ((t * 2 + s / 10) % 1)
                px = ox + L * f * math.sin(a)
                py = 560 + L * f * math.cos(a) + (0 if n > 1 else 0)
                c.ellipse(px, py, w * 0.6, w * 0.6, fill=mix(BG, WATER, 1.0))
        c.text(cx, 960, lab, 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '1 个大孔：水粗粗的，往下一流'),
                (7.2, 14, '孔越多越小，每一股越细'),
                (14.2, 22, '用同样的力挤，小孔喷出的水更急、喷得更远（示意，以实测为准）')], y=1010)


def e254_speed(c, t, i):
    corner_tag(c, '第 254 集 · 出口变小，水就加快')
    c.text(60, 96, '一秒钟里流进花洒的水差不多一样多；出口的总面积变小了，同样多的水要挤出去，只能跑得更快', 'serif', 36, INK)
    y0, y1 = 420, 640
    c.rect(200, y0, 1100, y1, fill=mix(BG, WATER, 0.3))
    c.poly([(1100, y0), (1400, 500), (1400, 560), (1100, y1)], mix(BG, WATER, 0.3))
    c.rect(1400, 500, 1750, 560, fill=mix(BG, WATER, 0.3))
    for k in range(8):
        f = ((t * 0.25) + k / 8) % 1
        x = 200 + f * 900
        c.rect(x, 500, x + 30, 560, fill=mix(BG, WATER, 1.0))
    for k in range(8):
        f = ((t * 1.0) + k / 8) % 1
        x = 1400 + f * 350
        c.rect(x, 515, x + 30, 545, fill=NRED)
    c.text(650, 700, '水管粗：走得慢', 'bold', 28, INK, 'mm')
    c.text(1575, 620, '出口细：走得快', 'bold', 28, NRED, 'mm')
    c.text(960, 820, '流量 = 面积 × 速度：面积变成 1/4，速度就变成 4 倍（示意）', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 7, '粗水管里，水慢慢地往前走'),
                (7.2, 14, '到了花洒，出口一下变细，后面的水还在推'),
                (14.2, 22, '同样多的水挤过小出口，只能加快：所以花洒喷得又细又急')], y=1010)


CLIPS = {
 'E252_钻缝': (e252_gap, 22), 'E252_斜抖': (e252_angle, 22),
 'E252_片头': (titles.opening(SER49, VOL49, S49A, 0, '1938 年美国开始出售尼龙刷毛牙刷'), 7),
 'E252_片尾': (titles.closing(SER49, VOL49, S49A, 0, '下集：牙膏里到底有什么？'), 7),
 'E253_磨料': (e253_abrasive, 22), 'E253_护氟': (e253_fluoride, 22),
 'E253_片头': (titles.opening(SER49, VOL49, S49A, 1, '19 世纪末出现软管装牙膏'), 7),
 'E253_片尾': (titles.closing(SER49, VOL49, S49A, 1, '下集：花洒为什么喷得又细又急？'), 7),
 'E254_小孔': (e254_holes, 22), 'E254_变快': (e254_speed, 22),
 'E254_片头': (titles.opening(SER49, VOL49, S49A, 2, '19 世纪欧洲出现莲蓬头淋浴'), 7),
 'E254_片尾': (titles.closing(SER49, VOL49, S49A, 2, '下集：洗完澡，镜子为什么起雾？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
