"""第四十七季（第二十层：厨房抽屉）第一批：E242 开瓶器、E243 开罐器、E244 打蛋器 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S47A = [('242', '开瓶器'), ('243', '开罐器'), ('244', '打蛋器'), ('245', '压蒜器'), ('246', '削皮器'),
        ('247', '食品夹'), ('248', '擀面杖'), ('249', '刨丝器'), ('250', '胡椒磨'), ('251', '吸管')]
SER47, VOL47 = '从零造物', '第四十七季 · 第二十层：厨房抽屉'
STEEL = (175, 185, 195)
CAP = (200, 70, 60)
GLASS = (90, 150, 110)
TIN = (185, 190, 180)
EGG = (245, 235, 200)
FOAM = (250, 250, 245)


def _bar(c, x, y, w, v, col, lab):
    c.rect(x, y, x + w, y + 26, fill=SHEET, r=6)
    c.rect(x, y, x + w * max(0.0, min(1.0, v)), y + 26, fill=col, r=6)
    c.text(x - 16, y + 13, lab, 'sans', 22, MUTED, 'rm')


# ---------------------------------------------------------------- E242 开瓶器
def e242_lever(c, t, i):
    corner_tag(c, '第 242 集 · 手离支点越远越省力')
    c.text(60, 96, '尺子架在橡皮上：水瓶离支点 5 厘米，手离支点越远，抬起它要的力越小', 'serif', 36, INK)
    fx, fy = 760, 640
    k = int((t % 21) // 7)
    arms = [5, 10, 20]
    arm = arms[k]
    ph = (t % 7) / 7
    tilt = 0.08 * min(1.0, ph * 2.5)
    sc = 32
    ca, sa = math.cos(tilt), math.sin(tilt)
    def P(d):
        return (fx + d * sc * ca, fy - 14 + d * sc * sa)
    c.poly([(fx - 40, fy + 60), (fx + 40, fy + 60), (fx, fy - 6)], mix(BG, (230, 200, 120), 1.0))
    c.text(fx, fy + 92, '支点（橡皮）', 'sans', 22, MUTED, 'mm')
    a, b = P(-8), P(22)
    c.line([a, b], mix(BG, STEEL, 1.0), 14)
    lx, ly = P(-5)
    c.rect(lx - 34, ly - 110, lx + 34, ly - 8, fill=mix(BG, FIELD, 0.8), r=10)
    c.text(lx, ly - 60, '水瓶', 'bold', 22, INK, 'mm')
    hx, hy = P(arm)
    F = 5.0 / arm
    c.arrow(hx, hy + 20, hx, hy + 20 + 160 * F, SPARK, 6, 18)
    c.text(hx, hy + 210, f'手在 {arm} 厘米', 'bold', 26, SPARK, 'mm')
    for j, (d, f) in enumerate([(5, 1.0), (10, 0.5), (20, 0.25)]):
        _bar(c, 1420, 300 + j * 70, 360, f, SPARK if d == arm else LINE, f'{d} 厘米')
    c.text(1600, 270, '需要的力（示意）', 'sans', 22, MUTED, 'mm')
    c.text(1600, 540, '力 × 距离 两边相等', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '手也在 5 厘米处：和水瓶一样远，要用和水瓶一样大的力'),
                (7.2, 14, '手挪到 10 厘米：力气只要一半'),
                (14.2, 22, '手挪到 20 厘米：只要四分之一；手动的距离却变长了（以实测为准）')], y=1010)


def e242_cap(c, t, i):
    corner_tag(c, '第 242 集 · 钩子掰弯盖边')
    c.text(60, 96, '开瓶器的头顶住瓶盖中间当支点，钩子卡住盖边；手柄一抬，钩子把盖边一点点掰起来', 'serif', 36, INK)
    ph = min(1.0, (t % 11) / 7)
    bx, by = 760, 520
    c.rect(bx - 90, by + 60, bx + 90, by + 420, fill=mix(BG, GLASS, 0.75), r=24)
    c.rect(bx - 60, by + 10, bx + 60, by + 70, fill=mix(BG, GLASS, 0.75), r=6)
    lift = 26 * ph
    c.poly([(bx - 78, by + 8), (bx + 78, by + 8 - lift), (bx + 78, by - 18 - lift), (bx - 78, by - 18)], mix(BG, CAP, 1.0))
    for k in range(7):
        x = bx - 72 + k * 24
        c.line([(x, by + 8 - lift * (k / 6)), (x + 8, by + 22 - lift * (k / 6))], mix(BG, CAP, 0.8), 4)
    ang = -0.42 * ph
    px, py = bx - 10, by - 22
    L = 420
    ex, ey = px + L * math.cos(ang), py + L * math.sin(ang)
    c.line([(px, py), (ex, ey)], mix(BG, STEEL, 1.0), 22)
    hx, hy = bx + 80, by + 10 - lift
    c.line([(px + 30, py + 4), (hx, hy)], mix(BG, STEEL, 1.0), 10)
    c.ellipse(px, py, 12, 12, fill=GREEN)
    c.text(px - 30, py - 40, '支点：顶住盖子中间', 'bold', 24, GREEN, 'rm')
    c.ellipse(hx, hy, 12, 12, fill=NRED)
    c.text(hx + 20, hy + 46, '钩子：卡住盖边往上掰', 'bold', 24, NRED, 'lm')
    c.arrow(ex, ey + 70, ex, ey - 10, SPARK, 6, 18)
    c.text(ex + 20, ey + 40, '手在远处轻轻一抬', 'bold', 24, SPARK, 'lm')
    if ph >= 1.0:
        c.text(bx, by + 470, '盖边一圈齿被掰弯，瓶盖松开', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '支点在中间，钩子离支点很近，手柄离支点很远'),
                (7.2, 14, '手上一点点力，到钩子那里就放大好几倍，把瓶盖的齿一个个掰弯'),
                (14.2, 22, '玻璃瓶由大人开；孩子用尺子和橡皮做模型（示意）')], y=1010)


# ---------------------------------------------------------------- E243 开罐器
def e243_roll(c, t, i):
    corner_tag(c, '第 243 集 · 滚着切开一圈')
    c.text(60, 96, '圆刀片压在罐子顶边内侧，带齿的小轮在外侧咬住卷边；拧把手，罐子转一圈，刀片就滚着切一圈', 'serif', 36, INK)
    cx, cy, R = 700, 560, 300
    turn = (t / 22) * 2 * math.pi
    c.ellipse(cx, cy, R, R, fill=mix(BG, TIN, 0.6))
    c.ellipse(cx, cy, R - 26, R - 26, fill=mix(BG, TIN, 0.85))
    n = 60
    for k in range(n):
        a0 = -math.pi / 2 + k * 2 * math.pi / n
        if (k / n) * 2 * math.pi <= turn:
            c.line([(cx + (R - 26) * math.cos(a0), cy + (R - 26) * math.sin(a0)),
                    (cx + (R - 26) * math.cos(a0 + 2 * math.pi / n), cy + (R - 26) * math.sin(a0 + 2 * math.pi / n))], NRED, 6)
    tx, ty = cx, cy - R
    c.ellipse(tx, ty + 34, 30, 30, fill=mix(BG, STEEL, 1.0))
    c.text(tx, ty + 34, '刀', 'bold', 22, BG, 'mm')
    c.ellipse(tx, ty - 36, 30, 30, fill=mix(BG, (210, 170, 90), 1.0))
    for k in range(10):
        a = k * math.pi / 5 + t * 3
        c.line([(tx + 30 * math.cos(a), ty - 36 + 30 * math.sin(a)), (tx + 40 * math.cos(a), ty - 36 + 40 * math.sin(a))], mix(BG, (210, 170, 90), 1.0), 5)
    c.text(tx + 70, ty - 36, '齿轮：在外侧咬住卷边，带罐子转', 'bold', 24, SPARK, 'lm')
    c.text(tx + 70, ty + 34, '圆刀片：在内侧压进去，滚着切', 'bold', 24, INK, 'lm')
    c.text(1500, 700, f'已切开 {min(100, int(turn / (2 * math.pi) * 100))}%', 'bold', 40, NRED, 'mm')
    caps(c, t, [(0, 7, '先夹紧：圆刀片压穿罐顶边，齿轮咬住外面的卷边'),
                (7.2, 14, '拧把手，齿轮转，带着整个罐子转；刀片不用来回锯，只在原地滚'),
                (14.2, 22, '转满一圈，罐盖就沿着红线整齐切开；切口锋利，只由大人操作')], y=1010)


def e243_gear(c, t, i):
    corner_tag(c, '第 243 集 · 小轮转很多圈，罐子才转一圈')
    c.text(60, 96, '齿轮的周长比罐子的周长小得多：把手要拧很多圈，罐子才转一圈，所以每一下都很省力', 'serif', 36, INK)
    gx, gy, r = 520, 540, 70
    cx, cy, R = 520 + 70 + 300, 540, 300
    ang_g = t * 2.4
    ang_c = -ang_g * r / R
    c.ellipse(cx, cy, R, R, fill=mix(BG, TIN, 0.6))
    c.line([(cx, cy), (cx + R * math.cos(ang_c - math.pi), cy + R * math.sin(ang_c - math.pi))], NRED, 6)
    c.ellipse(gx, gy, r, r, fill=mix(BG, (210, 170, 90), 1.0))
    c.line([(gx, gy), (gx + r * math.cos(ang_g), gy + r * math.sin(ang_g))], BG, 6)
    for k in range(12):
        a = ang_g + k * math.pi / 6
        c.line([(gx + r * math.cos(a), gy + r * math.sin(a)), (gx + (r + 12) * math.cos(a), gy + (r + 12) * math.sin(a))], mix(BG, (210, 170, 90), 1.0), 6)
    turns_g = ang_g / (2 * math.pi)
    c.text(gx, gy + 140, f'把手 {turns_g:.1f} 圈', 'bold', 30, SPARK, 'mm')
    c.text(cx, cy + R + 50, f'罐子 {turns_g * r / R:.2f} 圈', 'bold', 30, NRED, 'mm')
    c.text(1560, 380, '罐子周长 ÷ 齿轮周长', 'sans', 26, MUTED, 'mm')
    c.text(1560, 440, f'≈ {R / r:.1f} 圈把手 = 1 圈罐子', 'bold', 34, INK, 'mm')
    c.text(1560, 520, '（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '齿轮贴着罐边滚：齿轮转一圈，罐边只走过齿轮一圈那么长'),
                (7.2, 14, '罐子的周长大好几倍，所以要拧好几圈，罐子才转完一圈'),
                (14.2, 22, '拧的圈数多，每一圈用的力就小：这就是齿轮的省力（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E244 打蛋器
def e244_air(c, t, i):
    corner_tag(c, '第 244 集 · 把空气一次次卷进去')
    c.text(60, 96, '筷子只有两根，打蛋器有八九根钢丝：每转一圈，卷进蛋清里的空气多好几倍', 'serif', 36, INK)
    random.seed(7)
    for j, (lab, wires, rate) in enumerate([('一双筷子', 2, 0.35), ('打蛋器', 8, 1.0)]):
        bx, by = 480 + j * 960, 640
        c.arc(bx, by - 120, 300, 260, 0, 180, mix(BG, INK, 0.6), 6)
        lvl = min(1.0, (t / 20) * rate)
        top = by + 120 - 80 - 220 * lvl
        c.rect(bx - 260, top, bx + 260, by + 120, fill=mix(BG, EGG, 0.25 + 0.5 * lvl), r=30)
        nb = int(160 * lvl)
        for k in range(nb):
            x = bx + random.uniform(-240, 240)
            y = random.uniform(top + 10, by + 110)
            rr = random.uniform(4, 10) * (1.2 - 0.5 * lvl)
            c.ellipse(x, y, rr, rr, outline=mix(BG, FOAM, 0.9), width=2)
        a = t * 6
        for w in range(wires):
            off = (w - (wires - 1) / 2) * 22
            x = bx + off * math.cos(a)
            c.line([(x, top - 160), (x, top + 60)], mix(BG, STEEL, 1.0), 4)
        c.text(bx, by + 190, lab, 'bold', 30, INK, 'mm')
        c.text(bx, by + 236, f'泡沫高度（示意）{int(lvl * 100)}%', 'sans', 24, GREEN if rate > 0.5 else MUTED, 'mm')
    caps(c, t, [(0, 7, '两碗一样多的蛋清，同样搅 2 分钟'),
                (7.2, 14, '钢丝越多，每转一圈从表面卷进去的空气越多，打成越来越小的泡'),
                (14.2, 22, '多出来的「体积」全是空气（示意，以实测为准）')], y=1010)


def e244_film(c, t, i):
    corner_tag(c, '第 244 集 · 蛋白质在泡外结膜')
    c.text(60, 96, '蛋清里的蛋白质原本卷成小团；一搅就被拉开，排到每个气泡表面，结成一层膜把泡托住', 'serif', 36, INK)
    ph = min(1.0, (t % 22) / 14)
    for j, (lab, egg) in enumerate([('清水：泡很快破掉', False), ('蛋清：泡外有一层蛋白质膜', True)]):
        cx, cy = 480 + j * 960, 520
        R = 200
        if not egg:
            rr = R * (1 - 0.8 * ph)
            c.ellipse(cx, cy, rr, rr, outline=mix(BG, FIELD, 0.9), width=4)
            if ph > 0.7:
                for k in range(8):
                    a = k * math.pi / 4
                    c.line([(cx + 60 * math.cos(a), cy + 60 * math.sin(a)), (cx + 110 * math.cos(a), cy + 110 * math.sin(a))], MUTED, 3)
        else:
            c.ellipse(cx, cy, R, R, outline=mix(BG, FOAM, 1.0), width=4)
            n = 22
            for k in range(n):
                a = k * 2 * math.pi / n
                fx, fy = cx + 280 * math.cos(a), cy + 280 * math.sin(a)
                tx, ty = cx + R * math.cos(a), cy + R * math.sin(a)
                x, y = fx + (tx - fx) * ph, fy + (ty - fy) * ph
                if ph < 0.5:
                    c.ellipse(x, y, 12, 12, fill=mix(BG, SPARK, 0.9))
                else:
                    c.line([(x - 14 * math.sin(a), y + 14 * math.cos(a)), (x + 14 * math.sin(a), y - 14 * math.cos(a))], SPARK, 7)
            c.text(cx, cy, '空气', 'bold', 30, MUTED, 'mm')
        c.text(cx, 860, lab, 'bold', 26, GREEN if egg else NRED, 'mm')
    caps(c, t, [(0, 7, '清水打出的泡，膜太薄又没东西托着，一下就破'),
                (7.2, 14, '蛋清里卷成团的蛋白质被搅开，排到气泡表面'),
                (14.2, 22, '一圈蛋白质连成膜，泡就立得住；插根筷子也不倒（示意，以实测为准）')], y=1010)


CLIPS = {
 'E242_省力': (e242_lever, 22), 'E242_撬盖': (e242_cap, 22),
 'E242_片头': (titles.opening(SER47, VOL47, S47A, 0, '1892 年美国人潘特发明皇冠瓶盖和开瓶器'), 7),
 'E242_片尾': (titles.closing(SER47, VOL47, S47A, 0, '下集：转一转小把手，怎么就切开了罐头？'), 7),
 'E243_滚切': (e243_roll, 22), 'E243_齿轮': (e243_gear, 22),
 'E243_片头': (titles.opening(SER47, VOL47, S47A, 1, '1858 年美国人华纳申请开罐器专利'), 7),
 'E243_片尾': (titles.closing(SER47, VOL47, S47A, 1, '下集：一碗蛋清，怎么打成一大碗泡沫？'), 7),
 'E244_卷气': (e244_air, 22), 'E244_泡膜': (e244_film, 22),
 'E244_片头': (titles.opening(SER47, VOL47, S47A, 2, '1870 年前后美国出现手摇齿轮打蛋器'), 7),
 'E244_片尾': (titles.closing(SER47, VOL47, S47A, 2, '下集：一瓣蒜，为什么一夹就成了蒜泥？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
