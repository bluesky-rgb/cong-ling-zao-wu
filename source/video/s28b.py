"""第二十八季（古法解密 11.0：桶、绳、戏、窗）第二批：B113 高跷、B114 筛子、B115 陶车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s28a import SB28, VOL28, WOOD, DARKWOOD, SKIN, ROPE

BEAN = (220, 190, 110)
RICE = (240, 240, 230)
CLAY = (190, 120, 80)
PAPERC = (235, 225, 205)


# ---------------------------------------------------------------- B113 高跷
def _stilt_fig(c, px, py, ang, base_w, com_h, col):
    """在倾斜木板上画站着的纸人：以底座中心 (px,py) 为原点，板倾角 ang。返回重心垂线是否在底座内。"""
    ca, sa = math.cos(ang), math.sin(ang)
    def T(x, y):
        return (px + x * ca - y * sa, py + x * sa + y * ca)
    c.poly([T(-base_w / 2, 0), T(base_w / 2, 0), T(base_w / 2, -8), T(-base_w / 2, -8)], WOOD)
    c.line([T(-10, -8), T(-10, -200)], DARKWOOD, 6)
    c.line([T(10, -8), T(10, -200)], DARKWOOD, 6)
    c.poly([T(-30, -200), T(30, -200), T(25, -330), T(-25, -330)], col)
    c.ellipse(*T(0, -360), 28, 28, fill=SKIN)
    g = T(0, -com_h)
    c.ellipse(g[0], g[1], 12, 12, fill=SPARK)
    seg(c, [g, (g[0], py + 60)], SPARK, 2)
    left, right = T(-base_w / 2, 0), T(base_w / 2, 0)
    return min(left[0], right[0]) <= g[0] <= max(left[0], right[0])


def b113_base(c, t, i):
    corner_tag(c, 'B113 · 重心垂线落在脚底里，就站得住')
    c.text(60, 96, '从重心往下画一条竖线：只要它落在脚底撑着的范围里，人就倒不了；底座越宽、重心越低，能斜的角度越大', 'serif', 36, INK)
    ang_deg = min(30, t * 1.6)
    ang = math.radians(ang_deg)
    for k, (bw, comh, lab) in enumerate(((40, 260, '窄底 · 重心高'), (120, 260, '宽底 · 重心高'), (120, 120, '宽底 · 重心低'))):
        px = 360 + k * 560
        py = 760
        c.line([(px - 220, py + 220 * math.tan(ang) * 0), (px + 220, py)], LINE, 1)
        L = 220
        c.line([(px - L * math.cos(ang), py - L * math.sin(ang)), (px + L * math.cos(ang), py + L * math.sin(ang))], mix(BG, WOOD, 0.8), 10)
        crit = math.degrees(math.atan((bw / 2) / comh))
        if ang_deg < crit:
            ok = _stilt_fig(c, px, py, ang, bw, comh, (120, 160, 220))
            c.text(px, 900, '站得住', 'bold', 24, GREEN, 'mm')
        else:
            fall = min(1, (ang_deg - crit) / 4)
            _stilt_fig(c, px + 60 * fall, py + 40 * fall, ang + 1.2 * fall, bw, comh, (120, 160, 220))
            c.text(px, 900, '倒了', 'bold', 24, NRED, 'mm')
        c.text(px, 240, lab, 'bold', 24, INK, 'mm')
        c.text(px, 280, f'约 {crit:.0f}° 才倒（示意）', 'mono', 20, MUTED, 'mm')
    c.text(1700, 220, f'板子倾斜 {ang_deg:.0f}°', 'mono', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '纸人里塞一团橡皮泥当「重心」，站在两根筷子做的高跷上，木板一点点斜起来'),
                (7.2, 14, '黄色竖线是重心正下方：它一跑出脚底的范围，纸人就翻倒了'),
                (14.2, 22, '底座窄、重心高的最先倒；底座宽、重心低的能撑到很大的角度（角度为示意，以实测为准）')], y=1010)


def b113_steps(c, t, i):
    corner_tag(c, 'B113 · 站着不动反而难，要不停地挪脚')
    c.text(60, 96, '真人踩高跷，脚底很小，身子总会晃：踩高跷的人一直小步挪动，让脚始终追着重心走，就像手指顶住一根竖着的棍子', 'serif', 34, INK)
    ground = 820
    c.line([(100, ground + 4), (1820, ground + 4)], LINE, 3)
    sway = 70 * math.sin(t * 1.1) + 25 * math.sin(t * 2.7)
    foot = 960 + 0.85 * 70 * math.sin(t * 1.1 - 0.35) + 0.85 * 25 * math.sin(t * 2.7 - 0.6)
    cx = 960 + sway
    c.line([(foot - 20, ground), (cx - 15, ground - 280)], DARKWOOD, 8)
    c.line([(foot + 20, ground), (cx + 15, ground - 280)], DARKWOOD, 8)
    c.poly([(cx - 40, ground - 280), (cx + 40, ground - 280), (cx + 32, ground - 470), (cx - 32, ground - 470)], (220, 140, 110))
    c.ellipse(cx, ground - 510, 32, 32, fill=SKIN)
    g = (cx, ground - 400)
    c.ellipse(g[0], g[1], 12, 12, fill=SPARK)
    seg(c, [g, (g[0], ground)], SPARK, 2)
    c.rect(foot - 40, ground - 4, foot + 40, ground + 8, fill=GREEN)
    c.text(foot, ground + 40, '脚底范围', 'sans', 20, GREEN, 'mm')
    gx0 = 1300
    c.rect(1280, 240, 1860, 560, fill=SHEET, r=14)
    c.text(1570, 280, '手指顶竖棍', 'bold', 24, INK, 'mm')
    rx = 1570 + 30 * math.sin(t * 1.3)
    c.line([(rx, 520), (rx + 50 * math.sin(t * 1.3 + 0.6), 330)], WOOD, 8)
    c.ellipse(rx, 525, 16, 10, fill=SKIN)
    c.text(1570, 545, '棍子往哪歪，手指就往哪追', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '纸人可以一动不动地站着，真人却不行：身体总在微微地晃'),
                (7.2, 14, '踩高跷的人从来不站死，而是不停地小步挪动，让脚底一直待在重心正下方'),
                (14.2, 22, '就像用手指顶住一根竖着的棍子：棍子往哪边歪，手指就往哪边追（示意）。本集只做纸模型，不让孩子踩真高跷')], y=1010)


# ---------------------------------------------------------------- B114 筛子
def b114_rise(c, t, i):
    corner_tag(c, 'B114 · 摇一摇，小的钻缝，大的冒头')
    c.text(60, 96, '每摇一下，大颗粒被抬起一点点，底下就空出一个缝；小颗粒顺势钻进去占住位置，大的就落不回原处了', 'serif', 36, INK)
    x0, y0, x1, y1 = 500, 260, 1100, 880
    c.rect(x0, y0, x1, y1, outline=LINE, width=4, r=16)
    shakes = int(t / 0.6)
    ph = (t % 0.6) / 0.6
    jig = 10 * math.sin(ph * 2 * math.pi)
    rnd = random.Random(3)
    for k in range(260):
        x = x0 + 20 + rnd.random() * (x1 - x0 - 40)
        y = y0 + 60 + rnd.random() * (y1 - y0 - 80)
        c.ellipse(x + jig * 0.3, y, 7, 5, fill=RICE)
    beans = [(x0 + 100 + k * 100, 0.15 + 0.1 * (k % 2)) for k in range(5)]
    for k, (bx, start) in enumerate(beans):
        hgt = min(1, start + shakes * 0.022 * (1 + 0.3 * k % 2))
        by = y1 - 40 - hgt * (y1 - y0 - 120)
        c.ellipse(bx + jig, by, 30, 26, fill=BEAN)
        if ph < 0.4 and hgt < 1:
            for s in range(4):
                c.ellipse(bx - 18 + s * 12, by + 34, 6, 4, fill=mix(RICE, SPARK, 0.6))
    c.rect(1240, 300, 1840, 640, fill=SHEET, r=14)
    c.text(1540, 340, f'摇了 {shakes} 下', 'mono', 30, SPARK, 'mm')
    c.text(1540, 420, '黄豆一点点冒上来', 'sans', 24, INK, 'mm')
    c.text(1540, 480, '（不是因为轻：黄豆比米粒重）', 'sans', 20, MUTED, 'mm')
    c.text(1540, 570, '速度以实测为准', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '瓶底放黄豆，上面压满大米，盖紧，左右轻轻摇'),
                (7.2, 14, '每摇一下，黄豆被晃起一点点，下面空出一个小缝，米粒马上钻进去占住'),
                (14.2, 22, '黄豆落不回原来的位置，只能一次比一次高：这叫「巴西坚果效应」，一罐坚果里大的总在上面（示意）')], y=1010)


def b114_sieve(c, t, i):
    corner_tag(c, 'B114 · 一层层筛子，按大小分开')
    c.text(60, 96, '筛子的孔就是一道门：比孔小的漏下去，比孔大的留在上面；几层孔径不同的筛子叠起来，就能一次分出好几种大小', 'serif', 34, INK)
    layers = [(340, 22, '粗筛：孔大'), (560, 12, '中筛'), (780, 6, '细筛：孔小')]
    rnd = random.Random(7)
    parts = [(rnd.choice([28, 16, 8, 4]), rnd.random(), rnd.random()) for _ in range(120)]
    sh = 12 * math.sin(t * 9)
    for (y, hole, lab) in layers:
        c.line([(400 + sh, y), (1300 + sh, y)], WOOD, 6)
        for k in range(30):
            x = 420 + k * 30 + sh
            c.rect(x, y - 3, x + hole * 0.8, y + 3, fill=BG)
        c.text(1340, y, lab, 'bold', 22, INK, 'lm')
    c.line([(400, 940), (1300, 940)], LINE, 3)
    prog = min(1, t / 14)
    for (d, u, v) in parts:
        x = 430 + u * 840 + sh
        if d >= 22:
            stop = 340
        elif d >= 12:
            stop = 560
        elif d >= 6:
            stop = 780
        else:
            stop = 930
        y = 240 + (stop - 240) * min(1, prog * (1.2 + v)) - d / 2 - 4
        col = {28: BEAN, 16: (200, 150, 90), 8: RICE, 4: (180, 180, 170)}[d]
        c.ellipse(x, y, d / 2, d / 2 * 0.8, fill=col)
    c.rect(1500, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1680, 340, '筛完以后', 'bold', 24, INK, 'mm')
    for k, (nm, col) in enumerate((('最大：粗筛上', BEAN), ('中等：中筛上', (200, 150, 90)), ('小：细筛上', RICE), ('最细：漏到底', (180, 180, 170)))):
        c.ellipse(1540, 410 + k * 70, 12, 10, fill=col)
        c.text(1570, 410 + k * 70, nm, 'sans', 20, INK, 'lm')
    caps(c, t, [(0, 7, '把一堆大小混在一起的颗粒倒在筛子上，前后晃'),
                (7.2, 14, '比孔小的颗粒一碰到孔就漏下去，比孔大的怎么晃也过不去'),
                (14.2, 22, '几层孔径不同的筛子叠起来：粮食、沙子、药材，都是这样一次分出好几种大小（示意）')], y=1010)


# ---------------------------------------------------------------- B115 陶车
def b115_center(c, t, i):
    corner_tag(c, 'B115 · 泥放正中，手一扶就是一个圆')
    c.text(60, 96, '笔尖不动、转盘在转：泥团在正中，笔尖碰到的永远离中心一样远，划出正圆；偏了，就一下碰到一下碰不到', 'serif', 34, INK)
    for col_i, (off, lab) in enumerate(((0, '放在正中'), (80, '偏离中心 2 厘米'))):
        cx, cy = 480 + col_i * 860, 560
        c.ellipse(cx, cy, 300, 300, fill=mix(BG, WOOD, 0.5))
        c.ellipse(cx, cy, 8, 8, fill=INK)
        a = t * 2.2
        ccx, ccy = cx + off * math.cos(a), cy + off * math.sin(a)
        c.ellipse(ccx, ccy, 150, 150, fill=CLAY)
        pen_x = cx + 150 + (60 if off else 0) - 20
        c.line([(pen_x + 160, cy), (pen_x, cy)], (230, 230, 120), 6)
        c.ellipse(pen_x, cy, 6, 6, fill=INK)
        dist = math.hypot(pen_x - ccx, cy - ccy)
        touching = dist <= 152
        c.text(cx, 900, lab, 'bold', 26, INK, 'mm')
        c.text(cx, 950, '笔尖一直贴着泥：一圈正圆' if not off else ('碰到了' if touching else '碰不到……'), 'sans', 22, GREEN if not off else (SPARK if touching else NRED), 'mm')
    caps(c, t, [(0, 7, '懒人转盘中间放一团橡皮泥，铅笔尖轻轻顶住泥团侧面，手不动，只让转盘转'),
                (7.2, 14, '泥团在正中：笔尖碰到的永远是离中心一样远的地方，划出一个正圆'),
                (14.2, 22, '泥团偏了 2 厘米：转到一边笔尖戳进去，转到另一边又够不着，泥团一晃一晃的：陶工第一步就是「定中心」')], y=1010)


def b115_throw(c, t, i):
    corner_tag(c, 'B115 · 手只管高低，转盘负责圆')
    c.text(60, 96, '手指在泥上只做一件事：往里按或往外推、往上提；转盘让这只手的形状绕着中心转一圈，一个对称的罐子就出来了', 'serif', 34, INK)
    prog = min(1, t / 16)
    base = 820
    cx = 760
    H = 120 + 280 * prog
    def r_of(h):
        u = h / H
        return 110 + 80 * prog * math.sin(math.pi * u * 0.85) - 20 * prog * u
    pts_l, pts_r = [], []
    for k in range(41):
        h = H * k / 40
        r = r_of(h)
        pts_r.append((cx + r, base - h))
        pts_l.append((cx - r, base - h))
    c.poly(pts_r + pts_l[::-1], CLAY)
    for k in range(1, 10):
        h = H * k / 10
        r = r_of(h)
        ph = (t * 2 + k * 0.3) % 1
        c.line([(cx - r * math.cos(ph * math.pi), base - h), (cx - r * math.cos(ph * math.pi) + 6, base - h)], mix(CLAY, BG, 0.3), 3)
    c.ellipse(cx, base + 10, 340, 30, fill=mix(BG, WOOD, 0.6))
    hand_h = H * (0.2 + 0.7 * ((t * 0.3) % 1))
    hr = r_of(hand_h)
    c.ellipse(cx + hr + 26, base - hand_h, 26, 18, fill=SKIN)
    c.arc(cx, base + 10, 360, 40, 200, 340, SPARK, 3)
    c.text(cx + 380, base + 10, '转', 'bold', 26, SPARK, 'lm')
    c.rect(1300, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1580, 340, '手的形状 × 转一圈', 'bold', 24, INK, 'mm')
    c.text(1580, 410, '＝ 一个对称的罐子', 'bold', 24, SPARK, 'mm')
    c.text(1580, 490, '车床、旋压做灯罩，', 'sans', 20, INK, 'mm')
    c.text(1580, 530, '也是这个道理', 'sans', 20, INK, 'mm')
    caps(c, t, [(0, 7, '几千年前，陶工发现：让泥转起来，手就不用绕着罐子走一圈了'),
                (7.2, 14, '手指只管往里按、往外推、往上提；转盘让手的每一个动作都均匀地落在一整圈上'),
                (14.2, 22, '手的形状绕中心转一圈，就是罐子的形状：快轮让陶器又薄又圆、做得又快（年代拍摄前核对）')], y=1010)


CLIPS = {
 'B113_支撑面': (b113_base, 22), 'B113_挪脚': (b113_steps, 22),
 'B113_片头': (titles.opening(BSER, VOL28, SB28, 3, '《列子》中兰子踩高跷'), 7),
 'B113_片尾': (titles.closing(BSER, VOL28, SB28, 3, '下集：一筐混着大小颗粒的谷子，为什么摇一摇大的就跑到上面？'), 7),
 'B114_钻缝': (b114_rise, 22), 'B114_筛分': (b114_sieve, 22),
 'B114_片头': (titles.opening(BSER, VOL28, SB28, 4, '《天工开物》里的筛与簸'), 7),
 'B114_片尾': (titles.closing(BSER, VOL28, SB28, 4, '下集：转盘一转，为什么一团泥就长成了圆圆的罐子？'), 7),
 'B115_对中': (b115_center, 22), 'B115_拉坯': (b115_throw, 22),
 'B115_片头': (titles.opening(BSER, VOL28, SB28, 5, '新石器时代快轮制陶'), 7),
 'B115_片尾': (titles.closing(BSER, VOL28, SB28, 5, '下集：木偶身上只有几根线，为什么一歪手它就抬手点头？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
