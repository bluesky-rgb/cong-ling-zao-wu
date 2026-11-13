"""第四十七季（第二十层：厨房抽屉）第二批：E245 压蒜器、E246 削皮器、E247 食品夹 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s47a import S47A, SER47, VOL47, STEEL

CLAY = (200, 170, 120)
CARROT = (235, 130, 50)
SKIN = (180, 90, 40)


# ---------------------------------------------------------------- E245 压蒜器
def e245_lever(c, t, i):
    corner_tag(c, '第 245 集 · 手柄把力放大')
    c.text(60, 96, '压蒜器是两根铰在一起的手柄：手在远处捏，蒜在靠近铰链的地方，力就放大好几倍', 'serif', 36, INK)
    ph = 0.5 - 0.5 * math.cos(min(1.0, (t % 11) / 8) * math.pi)
    hx, hy = 360, 640
    L = 1100
    ang = -0.15 * (1 - ph) - 0.02
    c.line([(hx, hy), (hx + L, hy)], mix(BG, STEEL, 1.0), 26)
    ex, ey = hx + L * math.cos(ang), hy + L * math.sin(ang)
    c.line([(hx, hy - 30), (ex, ey - 30)], mix(BG, STEEL, 1.0), 26)
    c.ellipse(hx, hy - 15, 24, 24, fill=GREEN)
    c.text(hx, hy + 70, '铰链（支点）', 'bold', 24, GREEN, 'mm')
    gx = hx + 260
    top = hy - 30 + 260 * math.tan(ang)
    gh = max(14, (hy - 13) - (top + 13))
    c.rect(gx - 60, hy - 13 - gh, gx + 60, hy - 13, fill=mix(BG, CLAY, 1.0), r=10)
    c.text(gx, hy + 120, '蒜（离支点 4 厘米）', 'bold', 24, CLAY, 'mm')
    c.arrow(ex, ey - 150, ex, ey - 50, SPARK, 6, 18)
    c.text(ex, ey - 180, '手（离支点 16 厘米）', 'bold', 24, SPARK, 'mm')
    c.text(1500, 820, '手上 1 份力 → 蒜上约 4 份力', 'bold', 32, INK, 'mm')
    c.text(1500, 870, '（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '蒜放在离铰链很近的小槽里，手捏在手柄最远的一头'),
                (7.2, 14, '手离支点是蒜的 4 倍远，压在蒜上的力就差不多是手上的 4 倍'),
                (14.2, 22, '代价是手要捏过很长一段距离，蒜那头只走一小段（用橡皮泥代替蒜）')], y=1010)


def e245_holes(c, t, i):
    corner_tag(c, '第 245 集 · 力集中在小孔上')
    c.text(60, 96, '同样的力，用平板压只会把橡皮泥压扁；底下换成带小孔的板，压强集中，它只能从孔里挤出去', 'serif', 36, INK)
    ph = min(1.0, (t % 11) / 8)
    for j, (lab, holes) in enumerate([('平板：只是压扁', False), ('小孔板：一条条挤出来', True)]):
        cx = 480 + j * 960
        py = 300 + 160 * ph
        c.rect(cx - 220, py - 40, cx + 220, py, fill=mix(BG, STEEL, 1.0), r=6)
        c.arrow(cx, 200, cx, py - 50, SPARK, 6, 18)
        base = 620
        if not holes:
            w = 120 + 160 * ph
            c.rect(cx - w, py, cx + w, base, fill=mix(BG, CLAY, 1.0), r=16)
            c.rect(cx - 260, base, cx + 260, base + 30, fill=mix(BG, STEEL, 0.8), r=4)
        else:
            c.rect(cx - 120, py, cx + 120, base, fill=mix(BG, CLAY, 1.0), r=16)
            c.rect(cx - 260, base, cx + 260, base + 30, fill=mix(BG, STEEL, 0.8), r=4)
            for k in range(7):
                x = cx - 105 + k * 35
                c.rect(x - 7, base, x + 7, base + 30, fill=BG)
                ln = 200 * ph
                c.rect(x - 7, base + 30, x + 7, base + 30 + ln, fill=mix(BG, CLAY, 1.0), r=6)
        c.text(cx, 920, lab, 'bold', 28, GREEN if holes else NRED, 'mm')
    caps(c, t, [(0, 7, '压强 = 力 ÷ 面积：同样的力，面积越小，压强越大'),
                (7.2, 14, '平板下面没有出路，橡皮泥只能往两边摊开'),
                (14.2, 22, '小孔板把力集中在一个个小口上，橡皮泥就从孔里挤成细条（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E246 削皮器
def e246_guard(c, t, i):
    corner_tag(c, '第 246 集 · 刀刃只露出一点点')
    c.text(60, 96, '削皮器的刀刃前面有一道挡板，刀刃只比挡板多露出一点点：切进去多深，早就定好了', 'serif', 36, INK)
    for j, (lab, guard) in enumerate([('菜刀：深一刀浅一刀', False), ('削皮器：每一刀一样薄', True)]):
        cx = 480 + j * 960
        sy = 560
        c.rect(cx - 380, sy, cx + 380, sy + 260, fill=mix(BG, CARROT, 0.9), r=10)
        c.rect(cx - 380, sy, cx + 380, sy + 14, fill=mix(BG, SKIN, 1.0))
        prog = (t % 7) / 7
        x = cx - 360 + 720 * prog
        if guard:
            d = 14
            c.rect(cx - 380, sy, x, sy + d, fill=BG)
            c.rect(x - 60, sy - 70, x - 8, sy, fill=mix(BG, STEEL, 0.7), r=4)
            c.line([(x - 4, sy - 70), (x + 30, sy + d)], mix(BG, STEEL, 1.0), 8)
            c.text(x - 34, sy - 96, '挡板', 'sans', 22, MUTED, 'mm')
        else:
            d = 14 + 40 * abs(math.sin((x - cx) / 90))
            for k in range(int(prog * 40)):
                xx = cx - 360 + 18 * k
                dd = 14 + 40 * abs(math.sin((xx - cx) / 90))
                c.rect(xx, sy, xx + 18, sy + dd, fill=BG)
            c.line([(x - 40, sy - 70), (x + 20, sy + d)], mix(BG, STEEL, 1.0), 10)
        c.text(cx, 900, lab, 'bold', 28, GREEN if guard else NRED, 'mm')
    caps(c, t, [(0, 7, '菜刀切多深全靠手感，一不小心就削掉一大块'),
                (7.2, 14, '削皮器的挡板贴着表面滑，刀刃只能切进露出来的那一点点'),
                (14.2, 22, '所以削下的皮又薄又匀；刀片很锋利，只由大人使用（示意）')], y=1010)


def e246_swivel(c, t, i):
    corner_tag(c, '第 246 集 · 刀片会转，贴着弯面走')
    c.text(60, 96, '刀片装在两头的小轴上，可以前后转一点：遇到弯弯的表面，刀片自己转过去贴上', 'serif', 36, INK)
    cx, cy, R = 760, 640, 300
    c.ellipse(cx, cy, R + 14, R + 14, fill=mix(BG, SKIN, 1.0))
    c.ellipse(cx, cy, R, R, fill=mix(BG, CARROT, 0.9))
    a = -math.pi * 0.85 + (t % 11) / 11 * math.pi * 0.7
    for k in range(40):
        aa = -math.pi * 0.85 + k * (math.pi * 0.7) / 40
        if aa < a:
            c.arc(cx, cy, R + 14, R + 14, math.degrees(aa), math.degrees(aa + math.pi * 0.7 / 40) + 0.5, BG, 16)
    px, py = cx + (R + 14) * math.cos(a), cy + (R + 14) * math.sin(a)
    tx, ty = -math.sin(a), math.cos(a)
    c.line([(px - 70 * tx, py - 70 * ty), (px + 70 * tx, py + 70 * ty)], mix(BG, STEEL, 1.0), 10)
    nx, ny = math.cos(a), math.sin(a)
    c.line([(px, py), (px + 160 * nx, py + 160 * ny)], mix(BG, STEEL, 0.6), 6)
    c.text(px + 190 * nx, py + 190 * ny, '刀片转动，始终贴着表面', 'bold', 24, SPARK, 'mm')
    c.text(1560, 500, '转一点：贴着圆面', 'bold', 28, INK, 'mm')
    c.text(1560, 560, '不转：只碰到一个点', 'bold', 28, MUTED, 'mm')
    caps(c, t, [(0, 7, '胡萝卜、土豆都是弯的，固定的刀片只能碰到一小点'),
                (7.2, 14, '刀片能前后转，压上去时自己摆到和表面平行'),
                (14.2, 22, '于是弯面也能削得又薄又匀（示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- E247 食品夹
def e247_force(c, t, i):
    corner_tag(c, '第 247 集 · 手在中间：费力杠杆')
    c.text(60, 96, '食品夹的支点在尾端，手捏在中间，东西夹在最前面：夹子头的力比手上的力还小', 'serif', 36, INK)
    k = int((t % 21) // 7)
    pos = [5, 10, 15][k]
    fx, fy = 260, 520
    sc = 60
    L = 22
    c.line([(fx, fy - 30), (fx + L * sc, fy - 50)], mix(BG, STEEL, 1.0), 16)
    c.line([(fx, fy + 30), (fx + L * sc, fy + 50)], mix(BG, STEEL, 1.0), 16)
    c.ellipse(fx, fy, 30, 30, fill=GREEN)
    c.text(fx, fy + 80, '支点（弹簧）', 'bold', 24, GREEN, 'mm')
    hx = fx + pos * sc
    c.arrow(hx, fy - 200, hx, fy - 60, SPARK, 6, 18)
    c.arrow(hx, fy + 200, hx, fy + 60, SPARK, 6, 18)
    c.text(hx, fy - 230, f'手在 {pos} 厘米', 'bold', 26, SPARK, 'mm')
    tx = fx + L * sc
    c.rect(tx - 40, fy - 40, tx + 40, fy + 40, fill=mix(BG, (210, 200, 120), 1.0), r=10)
    c.text(tx, fy + 90, '海绵（22 厘米处）', 'bold', 24, INK, 'mm')
    f = pos / L
    c.text(960, 820, f'夹子头的力 ≈ 手上的力 × {pos}/22 ≈ {f:.2f} 倍', 'bold', 32, NRED, 'mm')
    c.text(960, 870, '（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '支点在尾端，手离支点比夹子头近，手上的力到了夹子头反而变小'),
                (7.2, 14, '手越往后捏（靠近支点），夹子头越没劲'),
                (14.2, 22, '手往前捏一点，夹得更紧；这种杠杆叫费力杠杆')], y=1010)


def e247_reach(c, t, i):
    corner_tag(c, '第 247 集 · 用力气换距离')
    c.text(60, 96, '手只动一小段，夹子头就张开一大段：费力杠杆换来的是距离，手离热锅也远', 'serif', 36, INK)
    op = 0.5 + 0.5 * math.sin(t * 1.4)
    fx, fy = 360, 560
    L = 1100
    ang = 0.03 + 0.14 * op
    for s in (-1, 1):
        ex, ey = fx + L * math.cos(ang), fy + s * L * math.sin(ang)
        c.line([(fx, fy), (ex, ey)], mix(BG, STEEL, 1.0), 16)
    c.ellipse(fx, fy, 26, 26, fill=GREEN)
    hx = fx + 0.45 * L
    hgap = 2 * 0.45 * L * math.sin(ang)
    tgap = 2 * L * math.sin(ang)
    c.line([(hx, fy - hgap / 2 - 40), (hx, fy + hgap / 2 + 40)], SPARK, 4)
    c.text(hx, fy - hgap / 2 - 70, f'手张开 {hgap / 70:.1f}', 'bold', 26, SPARK, 'mm')
    ex = fx + L * math.cos(ang)
    c.line([(ex + 40, fy - tgap / 2), (ex + 40, fy + tgap / 2)], NRED, 4)
    c.text(ex + 70, fy, f'夹子头张开 {tgap / 70:.1f}', 'bold', 26, NRED, 'lm')
    c.text(960, 900, '夹子头动的距离 ≈ 手的 2 倍多（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '手只要捏一下，夹子头就合拢一大段'),
                (7.2, 14, '力气小了，可动作快、够得远，手不用伸到热锅边'),
                (14.2, 22, '筷子、镊子、扫帚也是这种杠杆；只夹冷的东西做实验')], y=1010)


CLIPS = {
 'E245_杠杆': (e245_lever, 22), 'E245_压强': (e245_holes, 22),
 'E245_片头': (titles.opening(SER47, VOL47, S47A, 3, '20 世纪中叶欧洲家庭开始普及压蒜器'), 7),
 'E245_片尾': (titles.closing(SER47, VOL47, S47A, 3, '下集：削皮器怎么只削下薄薄一层？'), 7),
 'E246_限位': (e246_guard, 22), 'E246_转刀': (e246_swivel, 22),
 'E246_片头': (titles.opening(SER47, VOL47, S47A, 4, '1947 年瑞士出现刀片会转的削皮器'), 7),
 'E246_片尾': (titles.closing(SER47, VOL47, S47A, 4, '下集：用夹子夹东西，为什么比手指还费力？'), 7),
 'E247_费力': (e247_force, 22), 'E247_距离': (e247_reach, 22),
 'E247_片头': (titles.opening(SER47, VOL47, S47A, 5, '弹簧食品夹在 20 世纪的厨房里普及'), 7),
 'E247_片尾': (titles.closing(SER47, VOL47, S47A, 5, '下集：擀面杖一擀，面团为什么又薄又圆？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
