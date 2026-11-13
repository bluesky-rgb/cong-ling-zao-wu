"""第四十四季（古法解密 19.0：门里与田边）第一批：B190 门轴、B191 屏风、B192 竹梯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB44 = [('B190', '门轴'), ('B191', '屏风'), ('B192', '竹梯'), ('B193', '吊脚楼'), ('B194', '蜡染'),
        ('B195', '纺车'), ('B196', '筒车'), ('B197', '竹笕'), ('B198', '石磬'), ('B199', '笙')]
VOL44 = '第四十四季 · 古法解密 19.0'
DOOR = (170, 110, 60)
STONE = (140, 135, 128)
SCREEN = (225, 205, 160)
BAMBOO = (170, 180, 90)


# ---------------------------------------------------------------- B190 门轴
def b190_arm(c, t, i):
    corner_tag(c, 'B190 · 推在离门轴最远处')
    c.text(60, 96, '门绕着门边的竖轴转：推门的手离门轴越远，力臂越长，同样转动门要的力就越小；推在门轴旁边，怎么推都费劲', 'serif', 35, INK)
    cx, cy = 420, 420
    ang = math.radians(22 * (0.5 - 0.5 * math.cos(t * 0.8)))
    L = 1100
    ex, ey = cx + L * math.cos(ang), cy + L * math.sin(ang)
    c.line([(cx, cy), (ex, ey)], mix(BG, DOOR, 1.0), 46)
    c.ellipse(cx, cy, 30, 30, fill=mix(BG, STONE, 1.0))
    c.ellipse(cx, cy, 12, 12, fill=INK)
    c.text(cx, cy + 70, '门轴', 'bold', 24, INK, 'mm')
    for k, (d, F) in enumerate([(0.12, 8.0), (0.5, 2.0), (0.95, 1.0)]):
        px, py = cx + L * d * math.cos(ang), cy + L * d * math.sin(ang)
        n = math.radians(90) + ang
        ln = 40 + 14 * F
        c.arrow(px - ln * math.cos(n) * 0, py - ln, px, py - 26, [NRED, SPARK, GREEN][k], 6, 18)
        c.text(px, py - ln - 30, f'约 {F:.0f} 份力', 'bold', 22, [NRED, SPARK, GREEN][k], 'mm')
    c.text(cx + L / 2, 900, '俯视示意：同一扇门，三个地方推', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '老式木门没有合页：门边伸出上下两根门轴，整扇门绕着它转'),
                (7.2, 14, '推在门轴旁边，力臂很短，要用很大的力；推在门的另一边，力臂最长'),
                (14.2, 22, '力乘力臂就是转动效果：所以门把手都装在离门轴最远的地方（示意）')], y=1010)


def b190_socket(c, t, i):
    corner_tag(c, 'B190 · 光滑的石臼，小小的接触面')
    c.text(60, 96, '门轴下端插在地上的石臼里：石臼光滑、接触面只有一小圈，摩擦就小；几百斤重的门也能一推就转', 'serif', 36, INK)
    for j, (lab, smooth) in enumerate([('光滑石臼：摩擦小，转得顺', True), ('粗糙的泥坑：摩擦大，推不动', False)]):
        ox = 480 + j * 960
        gy = 720
        c.rect(ox - 300, gy, ox + 300, gy + 160, fill=mix(BG, STONE if smooth else (150, 120, 85), 1.0))
        c.ellipse(ox, gy + 10, 70, 24, fill=mix(BG, (80, 78, 74), 1.0))
        c.rect(ox - 34, 300, ox + 34, gy + 30, fill=mix(BG, DOOR, 0.9), r=8)
        c.rect(ox + 34, 300, ox + 280, gy - 20, fill=mix(BG, DOOR, 1.0))
        rot = t * (2.0 if smooth else 0.3)
        for k in range(3):
            a = rot + k * 2.1
            x = ox + 30 * math.cos(a)
            c.line([(x, 340), (x, gy - 40)], mix(BG, INK, 0.25), 3)
        if not smooth:
            r = random.Random(int(t * 6))
            for k in range(14):
                c.ellipse(ox + r.uniform(-60, 60), gy + r.uniform(-4, 30), 6, 6, fill=mix(BG, (110, 85, 55), 1.0))
        c.arc(ox, gy - 60, 120, 30, 200, 340, GREEN if smooth else NRED, 5)
        c.text(ox, gy + 210, lab, 'bold', 26, GREEN if smooth else NRED, 'mm')
    caps(c, t, [(0, 7, '门的重量全压在下面那根门轴上，门轴在石臼里转'),
                (7.2, 14, '石臼光滑、接触只有一小圈，转起来摩擦很小'),
                (14.2, 22, '要是插在粗糙的泥坑里，泥沙卡着门轴，就很难推动（示意）')], y=1010)


# ---------------------------------------------------------------- B191 屏风
def _foot(c, pts, col):
    c.line(pts, col, 10)


def b191_base(c, t, i):
    corner_tag(c, 'B191 · 底边围成一个宽底面')
    c.text(60, 96, '单片屏风的底只是一条细线，重心稍一偏就出去了；折成「之」字形，几扇的底边围出一大片，重心落在里面，就稳了', 'serif', 35, INK)
    for j, (lab, n) in enumerate([('一片：底面是一条线', 1), ('四扇「之」字：底面很宽', 4)]):
        ox, oy = 480 + j * 960, 640
        wob = 0.12 * math.sin(t * 2)
        if n == 1:
            pts = [(ox - 240, oy), (ox + 240, oy)]
            c.line(pts, mix(BG, SCREEN, 1.0), 16)
            fall = 0 if t < 11 else min(1.0, (t - 11) / 3)
            gx = ox + 60 * math.sin(t * 2) + 120 * fall
            c.ellipse(gx, oy - 6 * 0, 14, 14, fill=NRED)
            c.line([(ox - 260, oy - 40), (ox + 260, oy - 40)], mix(BG, NRED, 0.4), 2)
            c.line([(ox - 260, oy + 40), (ox + 260, oy + 40)], mix(BG, NRED, 0.4), 2)
            c.text(ox, oy + 120, '重心一偏就出线：倒', 'sans', 22, NRED, 'mm')
        else:
            w = 130
            pts = [(ox - 2 * w, oy - 90), (ox - w, oy + 90), (ox, oy - 90), (ox + w, oy + 90), (ox + 2 * w, oy - 90)]
            c.poly(pts + [(ox + 2 * w, oy - 90)], mix(BG, GREEN, 0.15))
            c.line(pts, mix(BG, SCREEN, 1.0), 16)
            hull = [(ox - 2 * w, oy - 90), (ox + 2 * w, oy - 90), (ox + w, oy + 90), (ox - w, oy + 90)]
            c.poly(hull, mix(BG, GREEN, 0.18))
            c.line(pts, mix(BG, SCREEN, 1.0), 16)
            gx, gy = ox + 40 * math.sin(t * 2), oy + 20 * math.cos(t * 2)
            c.ellipse(gx, gy, 14, 14, fill=GREEN)
            c.text(ox, oy + 160, '重心晃来晃去，还在底面里：稳', 'sans', 22, GREEN, 'mm')
        c.text(ox, 300, lab, 'bold', 28, INK, 'mm')
    c.text(960, 900, '俯视示意：粗线是屏风的底边，圆点是重心落在地上的位置', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一张卡纸直直地立着，底只有一条细线，轻轻一扇就倒'),
                (7.2, 14, '折成几扇摆成「之」字，从上往下看，底边围出了一大片'),
                (14.2, 22, '只要重心落在这一片里，屏风就站得住：越宽越稳（示意）')], y=1010)


def b191_angle(c, t, i):
    corner_tag(c, 'B191 · 折角太平又变回一条线')
    c.text(60, 96, '「之」字折得太紧，底面又窄又长；拉得太平，几扇连成一直线，又回到单片的样子：中间的角度底面最宽，最稳', 'serif', 35, INK)
    for k, (deg, lab, ok) in enumerate([(30, '30°：太紧，底面细长', False), (90, '90°：底面最宽', True), (170, '170°：太平，几乎一条线', False)]):
        ox, oy = 340 + k * 620, 560
        w = 100
        half = math.radians(deg / 2)
        dy = w * math.cos(half)
        dx = w * math.sin(half)
        pts = [(ox - 2 * dx, oy - dy / 1), (ox - dx, oy + dy / 1), (ox, oy - dy), (ox + dx, oy + dy), (ox + 2 * dx, oy - dy)]
        hull = [(ox - 2 * dx, oy - dy), (ox + 2 * dx, oy - dy), (ox + dx, oy + dy), (ox - dx, oy + dy)]
        c.poly(hull, mix(BG, GREEN if ok else NRED, 0.18))
        c.line(pts, mix(BG, SCREEN, 1.0), 14)
        c.text(ox, oy + 200, lab, 'bold', 24, GREEN if ok else NRED, 'mm')
    c.text(960, 860, '同样 4 扇、同样宽：浅色区域是底面（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '把 4 扇的卡纸从很紧折到很平，每次都用书扇 5 下'),
                (7.2, 14, '太紧，底面变成细长条；太平，几扇连成一条线：都容易倒'),
                (14.2, 22, '折到差不多直角，底面又宽又方：屏风最稳（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B192 竹梯
def _ladder(c, x0, y0, x1, y1, col):
    for s in (-1, 1):
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        nx, ny = -dy / L * 22 * s, dx / L * 22 * s
        c.line([(x0 + nx, y0 + ny), (x1 + nx, y1 + ny)], col, 10)
    for k in range(1, 9):
        u = k / 9
        x, y = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        nx, ny = -dy / L * 22, dx / L * 22
        c.line([(x - nx, y - ny), (x + nx, y + ny)], col, 6)


def b192_slip(c, t, i):
    corner_tag(c, 'B192 · 梯脚被往外推')
    c.text(60, 96, '梯子斜靠在墙上，墙把梯顶往外推，人的重量又压在梯子上：梯脚就被推着往外滑，全靠地面的摩擦撑住', 'serif', 36, INK)
    wx, gy = 1500, 880
    c.rect(wx, 200, wx + 60, gy, fill=mix(BG, STONE, 0.9))
    c.rect(200, gy, 1700, gy + 30, fill=mix(BG, (150, 130, 100), 1.0))
    H = 600
    slide = 0 if t < 12 else min(260, (t - 12) * 120)
    fx = wx - 520 - slide
    top_y = gy - math.sqrt(max(0, (math.hypot(520, H)) ** 2 - (wx - fx) ** 2))
    _ladder(c, fx, gy - 10, wx - 10, top_y, mix(BG, BAMBOO, 1.0))
    u = min(0.85, 0.2 + t / 14 * 0.65)
    px, py = fx + (wx - 10 - fx) * u, gy - 10 + (top_y - gy + 10) * u
    c.ellipse(px, py - 60, 24, 24, fill=SPARK)
    c.rect(px - 18, py - 36, px + 18, py, fill=SPARK, r=6)
    c.arrow(fx + 40, gy - 40, fx - 140, gy - 40, NRED, 7, 20)
    c.text(fx - 150, gy - 80, '被往外推', 'bold', 24, NRED, 'mm')
    c.arrow(fx - 130, gy + 60, fx + 40, gy + 60, GREEN, 7, 20)
    c.text(fx - 40, gy + 100, '地面摩擦往里拉', 'bold', 24, GREEN, 'mm')
    c.arrow(wx - 20, top_y + 20, wx - 150, top_y + 20, MUTED, 5, 16)
    c.text(wx - 160, top_y - 20, '墙往外推', 'sans', 22, MUTED, 'rm')
    if slide > 0:
        c.text(900, 300, '摩擦撑不住：梯脚滑出去了', 'bold', 30, NRED, 'mm')
    caps(c, t, [(0, 7, '墙是光滑的，只能把梯顶往外推；这个推力一路传到梯脚'),
                (7.2, 14, '人爬得越高，梯脚被往外推得越厉害，地面摩擦要拉得越使劲'),
                (14.2, 22, '地面一滑、摩擦不够，梯脚就滑出去：所以梯脚要防滑、要有人扶（示意）')], y=1010)


def b192_angle(c, t, i):
    corner_tag(c, 'B192 · 太直会翻，太斜会滑')
    c.text(60, 96, '梯子太直，人一往后仰，重心就跑到梯脚外面，整把梯子往后翻；太斜，梯脚被推得更狠，容易滑：不直不斜才安全', 'serif', 35, INK)
    gy = 820
    for k, (deg, lab, col) in enumerate([(85, '太直：容易往后翻', NRED), (75, '合适：稳', GREEN), (50, '太斜：容易滑', NRED)]):
        ox = 200 + k * 600
        wx = ox + 420
        c.rect(wx, 260, wx + 30, gy, fill=mix(BG, STONE, 0.9))
        c.rect(ox - 40, gy, ox + 480, gy + 20, fill=mix(BG, (150, 130, 100), 1.0))
        L = 520
        a = math.radians(deg)
        fx = wx - L * math.cos(a)
        ty = gy - L * math.sin(a)
        _ladder(c, fx, gy - 8, wx - 6, ty, mix(BG, BAMBOO, 1.0))
        c.arc(fx, gy - 8, 80, 80, -deg, 0, MUTED, 3)
        c.text(fx + 100, gy - 30, f'{deg}°', 'mono', 22, MUTED, 'lm')
        c.text(ox + 220, gy + 80, lab, 'bold', 24, col, 'mm')
    c.text(960, 940, '角度为示意，以实测和梯子说明书为准', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '把尺子当梯子靠在书上：梯脚离书越远，梯子越斜'),
                (7.2, 14, '太斜，橡皮擦一往上推，尺子就滑出去；梯脚下垫砂纸，能多撑一会儿'),
                (14.2, 22, '本集只做模型：小孩不爬真梯子，大人用梯子时要有人在下面扶')], y=1010)


CLIPS = {
 'B190_力臂': (b190_arm, 22), 'B190_门臼': (b190_socket, 22),
 'B190_片头': (titles.opening(BSER, VOL44, SB44, 0, '先秦已有门枢与石门臼'), 7),
 'B190_片尾': (titles.closing(BSER, VOL44, SB44, 0, '下集：薄薄的屏风，折一折为什么就站住了？'), 7),
 'B191_底面': (b191_base, 22), 'B191_夹角': (b191_angle, 22),
 'B191_片头': (titles.opening(BSER, VOL44, SB44, 1, '汉代已有屏风，宋代多扇折屏常见'), 7),
 'B191_片尾': (titles.closing(BSER, VOL44, SB44, 1, '下集：一把竹梯，靠多斜才安全？'), 7),
 'B192_滑出': (b192_slip, 22), 'B192_角度': (b192_angle, 22),
 'B192_片头': (titles.opening(BSER, VOL44, SB44, 2, '先秦已有木梯、竹梯'), 7),
 'B192_片尾': (titles.closing(BSER, VOL44, SB44, 2, '下集：一半撑在半空的吊脚楼，为什么不塌？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
