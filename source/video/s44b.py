"""第四十四季（古法解密 19.0）第二批：B193 吊脚楼、B194 蜡染、B195 纺车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s44a import SB44, VOL44, DOOR

HILL = (110, 120, 85)
POST = (160, 110, 65)
INDIGO = (50, 80, 160)
WAX = (240, 235, 210)
YARN = (235, 230, 215)


# ---------------------------------------------------------------- B193 吊脚楼
def _house(c, ox, gy_left, gy_right, mode, push):
    # ox：左柱 x；坡从左高右低；mode 0 只有竖柱，1 加横枋，2 加斜撑
    floor_y = gy_left - 140
    xs = [ox, ox + 220, ox + 440]
    base = [gy_left + (gy_right - gy_left) * (x - ox) / 440 for x in xs]
    shear = push * (60 if mode == 0 else (18 if mode == 1 else 3))
    for x, b in zip(xs, base):
        c.line([(x, b), (x + shear, floor_y)], mix(BG, POST, 1.0), 14)
    if mode >= 1:
        my = (floor_y + base[-1]) / 2 + 20
        c.line([(xs[0] + shear * 0.4, floor_y + 60), (xs[-1] + shear * 0.4, floor_y + 60)], mix(BG, POST, 0.85), 10)
        c.line([(xs[1] + shear * 0.3, my), (xs[-1] + shear * 0.3, my)], mix(BG, POST, 0.85), 10)
    if mode == 2:
        c.line([(xs[1], base[1]), (xs[-1] + shear, floor_y + 4)], mix(BG, GREEN, 0.9), 8)
    c.rect(ox - 20 + shear, floor_y - 18, ox + 460 + shear, floor_y, fill=mix(BG, DOOR, 1.0))
    c.poly([(ox - 30 + shear, floor_y - 18), (ox + 220 + shear, floor_y - 160), (ox + 470 + shear, floor_y - 18)], mix(BG, (90, 80, 70), 1.0))
    return floor_y


def b193_frame(c, t, i):
    corner_tag(c, 'B193 · 横枋把柱子穿成一个框')
    c.text(60, 96, '光有竖柱，一推就像一排筷子一样歪；用横枋把柱子穿起来、再加一根斜撑，就成了一个整体的框，推也推不歪', 'serif', 35, INK)
    push = max(0.0, math.sin(t * 1.6)) if t > 2 else 0.0
    for k, (lab, mode) in enumerate([('只有竖柱：一推就歪', 0), ('加横枋：歪得少', 1), ('加斜撑：几乎不动', 2)]):
        ox = 160 + k * 600
        gl, gr = 640, 860
        c.poly([(ox - 40, gl - 10), (ox + 490, gr), (ox + 490, 920), (ox - 40, 920)], mix(BG, HILL, 0.9))
        fy = _house(c, ox, gl, gr, mode, push)
        if push > 0.2:
            c.arrow(ox - 150, fy - 10, ox - 50, fy - 10, SPARK, 6, 18)
        c.text(ox + 220, 950, lab, 'bold', 24, [NRED, SPARK, GREEN][mode], 'mm')
    caps(c, t, [(0, 7, '吊脚楼一半坐在山上，一半用长柱撑在坡下：竖柱负责把重量传到地上'),
                (7.2, 14, '只靠竖柱，侧面一推，每根柱子都绕着脚歪过去'),
                (14.2, 22, '横枋把柱子穿成一个整体，斜撑再分成三角形：三角形推不变形（示意）')], y=1010)


def b193_slope(c, t, i):
    corner_tag(c, 'B193 · 一半坐在山上，一半撑在空中')
    c.text(60, 96, '陡坡上挖平太费工：吊脚楼靠山一边搭在坡上，坡下一边用长柱撑到同样高，楼板就平了，下面还通风防潮', 'serif', 35, INK)
    p = min(1.0, t / 10)
    c.poly([(100, 380), (1800, 880), (1800, 940), (100, 940)], mix(BG, HILL, 0.9))
    ox = 520
    xs = [ox, ox + 250, ox + 500, ox + 750]
    base = [380 + (x - 100) * 500 / 1700 for x in xs]
    fy = base[0] - 10
    for k, (x, b) in enumerate(zip(xs, base)):
        h = (b - fy) * p
        c.line([(x, b), (x, b - h)], mix(BG, POST, 1.0), 16)
        if p > 0.3:
            c.text(x, b + 36, f'{(b - fy) / 100:.1f} 份', 'mono', 18, MUTED, 'mm')
    if p > 0.95:
        c.rect(ox - 30, fy - 18, ox + 780, fy, fill=mix(BG, DOOR, 1.0))
        c.poly([(ox - 60, fy - 18), (ox + 375, fy - 200), (ox + 810, fy - 18)], mix(BG, (90, 80, 70), 1.0))
        c.text(ox + 375, fy - 60, '平平的楼板', 'bold', 26, BG, 'mm')
        c.text(ox + 640, base[-1] - 120, '下面：通风、防潮', 'sans', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '在陡坡上盖房子，要么挖掉一大片土，要么顺着坡想办法'),
                (7.2, 14, '吊脚楼顺着坡：越往坡下，柱子越长，柱顶都在同一个高度'),
                (14.2, 22, '楼板悬在半空，下面潮气散得快，还能放农具、关牲口（示意）')], y=1010)


# ---------------------------------------------------------------- B194 蜡染
def b194_resist(c, t, i):
    corner_tag(c, 'B194 · 蜡挡住了水做的染料')
    c.text(60, 96, '染料溶在水里，要钻进布的纤维才能上色；蜡是油性的，和水互不相溶，盖住的纤维被封起来，水进不去，那里就留白', 'serif', 34, INK)
    x0, y0, W, H = 260, 260, 1400, 560
    p = min(1.0, max(0.0, (t - 3) / 9))
    c.rect(x0, y0, x0 + W, y0 + H, fill=mix(BG, (245, 243, 236), 1.0))
    for k in range(28):
        x = x0 + 25 + k * 50
        c.line([(x, y0), (x, y0 + H)], mix(BG, (220, 215, 200), 1.0), 2)
    wax = [(x0 + 300, y0 + 280, 120), (x0 + 700, y0 + 200, 90), (x0 + 1050, y0 + 330, 140)]
    dye_w = W * p
    c.rect(x0, y0, x0 + dye_w, y0 + H, fill=mix(BG, INDIGO, 0.85))
    r = random.Random(int(t * 3))
    for k in range(30):
        bx = x0 + dye_w - r.uniform(0, 80)
        by = y0 + r.uniform(0, H)
        if bx > x0:
            c.ellipse(bx, by, 6, 6, fill=mix(BG, INDIGO, 1.0))
    for cx, cy, r in wax:
        c.ellipse(cx, cy, r, r, fill=mix(BG, WAX, 1.0) if cx > x0 + dye_w + r else mix(BG, (250, 248, 240), 1.0))
        c.ellipse(cx, cy, r, r, outline=mix(BG, (200, 190, 150), 1.0), width=3)
    if p > 0.2:
        cx, cy, rr = wax[0]
        if x0 + dye_w > cx:
            for k in range(6):
                a = k * math.pi / 3 + 0.3
                bx, by = cx + (rr + 22) * math.cos(a), cy + (rr + 22) * math.sin(a)
                c.arrow(bx + 20 * math.cos(a), by + 20 * math.sin(a), bx, by, mix(BG, INDIGO, 1.0), 3, 10)
            c.text(cx, cy - rr - 60, '水被蜡挡在外面', 'bold', 22, INK, 'mm')
    c.text(960, 880, '浅色圆：画了蜡的地方；蓝：刷上去的染料（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '先用蜡在白布上画好花，再把整块布浸进蓝色的染缸里'),
                (7.2, 14, '染料跟着水钻进没盖蜡的纤维里；碰到蜡，水被挡在外面'),
                (14.2, 22, '把蜡去掉，蜡下面的布还是白的：白花蓝底就出来了（示意）')], y=1010)


def b194_crack(c, t, i):
    corner_tag(c, 'B194 · 冰纹：蜡上的细缝')
    c.text(60, 96, '蜡冷了会变脆，布一揉，蜡层上就裂出很多细缝；染料顺着缝渗进去，白花里就多了一道道像冰裂一样的细蓝线', 'serif', 35, INK)
    cx, cy, R = 960, 560, 300
    c.rect(400, 220, 1520, 900, fill=mix(BG, INDIGO, 0.85))
    c.ellipse(cx, cy, R, R, fill=mix(BG, (250, 248, 240), 1.0))
    p = min(1.0, t / 12)
    r = random.Random(11)
    n = int(14 * p)
    for k in range(n):
        a0 = r.uniform(0, 2 * math.pi)
        pts = []
        x, y = cx + r.uniform(-R * 0.6, R * 0.6), cy + r.uniform(-R * 0.6, R * 0.6)
        for s in range(6):
            pts.append((x, y))
            a0 += r.uniform(-0.7, 0.7)
            x += 40 * math.cos(a0)
            y += 40 * math.sin(a0)
            if math.hypot(x - cx, y - cy) > R - 6:
                break
        if len(pts) > 1:
            c.line(pts, mix(BG, INDIGO, 1.0), 3)
    c.text(cx, cy + R + 50, '冰纹多少看揉得轻重（示意，以实测为准）', 'sans', 22, BG, 'mm')
    caps(c, t, [(0, 7, '蜡冷下来是脆的，布一折一揉，蜡层就裂开细细的缝'),
                (7.2, 14, '染料的水能钻进缝里，在白花上留下细蓝线'),
                (14.2, 22, '本集不用热蜡：用白色蜡笔画在纸上、揉皱后刷水彩，也能看到冰纹')], y=1010)


# ---------------------------------------------------------------- B195 纺车
def b195_ratio(c, t, i):
    corner_tag(c, 'B195 · 大轮一圈，锭子很多圈')
    c.text(60, 96, '一根绳带绕着大轮和小锭子：绳带走过的长度一样，大轮转一圈走的绳带多，绕到小锭子上，锭子就要转好多圈', 'serif', 35, INK)
    bx, by, BR = 560, 560, 300
    sx, sy, SR = 1500, 560, 40
    a = t * 0.8
    c.ellipse(bx, by, BR, BR, outline=mix(BG, WOOD, 1.0), width=14)
    for k in range(8):
        aa = a + k * math.pi / 4
        c.line([(bx, by), (bx + (BR - 7) * math.cos(aa), by + (BR - 7) * math.sin(aa))], mix(BG, WOOD, 0.8), 6)
    c.ellipse(bx, by, 20, 20, fill=INK)
    c.line([(bx + (BR - 20) * math.cos(a), by + (BR - 20) * math.sin(a)), (bx + (BR + 60) * math.cos(a), by + (BR + 60) * math.sin(a))], mix(BG, DOOR, 1.0), 16)
    c.line([(bx, by - BR), (sx, sy - SR)], mix(BG, MUTED, 0.8), 4)
    c.line([(bx, by + BR), (sx, sy + SR)], mix(BG, MUTED, 0.8), 4)
    sa = a * BR / SR
    c.ellipse(sx, sy, SR, SR, fill=mix(BG, STRAW, 0.9))
    c.line([(sx, sy), (sx + SR * math.cos(sa), sy + SR * math.sin(sa))], NRED, 6)
    c.rect(sx - 10, sy - 200, sx + 10, sy + 200, fill=mix(BG, YARN, 0.6), r=4)
    c.text(bx, by + BR + 70, f'大轮转了 {a / (2 * math.pi):.1f} 圈', 'bold', 26, INK, 'mm')
    c.text(sx, sy + 260, f'锭子转了 {sa / (2 * math.pi):.0f} 圈', 'bold', 26, SPARK, 'mm')
    c.text(1000, 860, f'直径之比约 {BR // SR} 比 1：转速差约 {BR // SR} 倍（示意）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '手摇大轮，绳带跟着大轮的边走，也拉着锭子转'),
                (7.2, 14, '绳带不打滑，大轮边走多少，锭子边就走多少：锭子小，就得转更多圈'),
                (14.2, 22, '直径差几倍，转速就差几倍：手慢慢摇，锭子飞快地转（示意，以实测为准）')], y=1010)


def b195_twist(c, t, i):
    corner_tag(c, 'B195 · 锭子一转，纤维拧成线')
    c.text(60, 96, '松松的棉絮一扯就断；锭子飞快地转，把一缕缕纤维拧在一起，纤维之间互相挤紧、摩擦变大，就成了结实的线', 'serif', 35, INK)
    x0, x1, y = 200, 1500, 560
    tw = t * 3
    p = min(1.0, t / 12)
    xe = x0 + (x1 - x0) * p
    r = random.Random(3)
    for k in range(40):
        yy = y + r.uniform(-60, 60)
        xx = r.uniform(x0 - 120, x0 + 20)
        c.line([(xx, yy), (xx + r.uniform(40, 120), yy + r.uniform(-20, 20))], mix(BG, YARN, 0.7), 3)
    for s in range(3):
        pts = []
        for k in range(120):
            u = k / 119
            x = x0 + (xe - x0) * u
            ph = u * 30 + tw + s * 2 * math.pi / 3
            amp = 34 * (1 - 0.8 * u)
            pts.append((x, y + amp * math.sin(ph)))
        if xe > x0 + 10:
            c.line(pts, mix(BG, YARN, 1.0 - 0.15 * s), 5)
    c.rect(x1 + 20, y - 220, x1 + 50, y + 220, fill=mix(BG, STRAW, 1.0), r=6)
    c.ellipse(x1 + 35, y, 60, 60, fill=mix(BG, YARN, 0.8))
    c.text(x0 - 60, y + 130, '松散的棉絮', 'sans', 22, MUTED, 'mm')
    c.text((x0 + x1) / 2, y + 130, '拧在一起：纤维挤紧，摩擦变大', 'bold', 24, GREEN, 'mm')
    c.text(x1 + 35, y + 270, '锭子', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '棉花、羊毛的纤维都很短，松松地放在一起，一拉就散'),
                (7.2, 14, '锭子转起来，把一缕纤维拧成螺旋，一边拧一边卷到锭子上'),
                (14.2, 22, '拧过的纤维彼此挤紧，摩擦力把它们拴在一起：线就结实了（示意）')], y=1010)


CLIPS = {
 'B193_框架': (b193_frame, 22), 'B193_坡地': (b193_slope, 22),
 'B193_片头': (titles.opening(BSER, VOL44, SB44, 3, '西南山区很早就有干栏式吊脚楼'), 7),
 'B193_片尾': (titles.closing(BSER, VOL44, SB44, 3, '下集：画了蜡的地方，为什么染不上颜色？'), 7),
 'B194_防染': (b194_resist, 22), 'B194_冰纹': (b194_crack, 22),
 'B194_片头': (titles.opening(BSER, VOL44, SB44, 4, '汉代已有蜡缬，西南苗族、布依族传承至今'), 7),
 'B194_片尾': (titles.closing(BSER, VOL44, SB44, 4, '下集：摇一圈纺车，锭子为什么转好多圈？'), 7),
 'B195_转速': (b195_ratio, 22), 'B195_加捻': (b195_twist, 22),
 'B195_片头': (titles.opening(BSER, VOL44, SB44, 5, '汉代画像石上已有手摇纺车'), 7),
 'B195_片尾': (titles.closing(BSER, VOL44, SB44, 5, '下集：没人推的筒车，怎么自己把水提上去？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
