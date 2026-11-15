"""第五十三季（第二十三层：超市与包装）第三批：E278 气泡膜、E279 购物车万向轮、E280 卧式冰柜 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s53a import S53A, SER53, VOL53, GAS

BUBBLE = (190, 220, 240)
DOUGH = (230, 150, 150)
METAL = (170, 175, 185)
COLD = (100, 160, 240)
WARM = (235, 130, 80)


# ---------------------------------------------------------------- E278 气泡膜
def _drop(c, cx, gy, t0, t, layers, label):
    h0 = 520
    tt = max(0.0, t - t0)
    fall = min(1.0, (tt / 1.2) ** 2)
    base = gy - layers * 36
    y = (gy - h0) + (base - 40 - (gy - h0)) * fall
    flat = 0
    if fall >= 1:
        flat = {0: 60, 1: 32, 3: 12}[layers]
    for L in range(layers):
        yy = gy - (L + 1) * 36
        sq = (8 if fall >= 1 and L == layers - 1 else 0)
        for k in range(7):
            c.ellipse(cx - 150 + k * 50, yy + 18 + sq / 2, 22, 16 - sq, fill=mix(BG, BUBBLE, 0.8))
    w = 40 + flat
    hgt = 40 - flat * 0.45
    c.ellipse(cx, y + (40 - hgt), w, hgt, fill=mix(BG, DOUGH, 1.0))
    c.text(cx, gy + 70, label, 'bold', 26, INK, 'mm')
    if fall >= 1:
        c.text(cx, gy + 120, f'压扁宽约 {2 * w / 20:.0f} 厘米（示意）', 'bold', 24, GREEN if layers else NRED, 'mm')


def e278_squash(c, t, i):
    corner_tag(c, '第 278 集 · 落在泡泡上，摔得轻')
    c.text(60, 96, '同样的橡皮泥球从 1 米高掉下：落在桌面上摔得最扁；落在气泡膜上，泡泡先被压扁，球就扁得少，层数越多越轻', 'serif', 36, INK)
    gy = 780
    c.line([(160, gy), (1760, gy)], mix(BG, INK, 0.4), 4)
    for j, (layers, lab) in enumerate([(0, '桌面'), (1, '一层气泡膜'), (3, '三层气泡膜')]):
        _drop(c, 400 + j * 560, gy, 1 + j * 6.5, t, layers, lab)
    caps(c, t, [(0, 7, '30 克的橡皮泥球从 1 米高直接落在桌面上：底下摔出一个大平面'),
                (7.2, 14, '落在一层气泡膜上：泡泡先被压扁，球扁得少'),
                (14.2, 22, '三层气泡膜：缓冲更多，球几乎还是圆的（以实测为准）')], y=1010)


def e278_time(c, t, i):
    corner_tag(c, '第 278 集 · 把撞击拉长')
    c.text(60, 96, '要停下一个往下掉的东西，停得越急，冲击力越大；泡泡被压扁要一点时间，把「急停」变成「慢慢停」', 'serif', 36, INK)
    x0, y0, W, H = 300, 820, 1300, 520
    c.line([(x0, y0), (x0 + W, y0)], mix(BG, INK, 0.5), 3)
    c.line([(x0, y0), (x0, y0 - H)], mix(BG, INK, 0.5), 3)
    c.text(x0 + W, y0 + 40, '时间', 'sans', 24, MUTED, 'rm')
    c.text(x0 - 20, y0 - H, '冲击力', 'sans', 24, MUTED, 'rm')
    prog = min(1.0, t / 12)
    pts1 = [(x0 + 100 + k * 3, y0 - 480 * math.exp(-((k - 20) / 7) ** 2)) for k in range(0, int(41 * prog) + 1)]
    if len(pts1) > 1:
        c.line(pts1, NRED, 5)
    if t > 7.2:
        p2 = min(1.0, (t - 7.2) / 6)
        pts2 = [(x0 + 100 + k * 3, y0 - 80 * math.exp(-((k - 80) / 45) ** 2)) for k in range(0, int(200 * p2) + 1)]
        if len(pts2) > 1:
            c.line(pts2, GREEN, 5)
        c.text(x0 + 760, y0 - 150, '落在气泡膜上：时间长，力小', 'bold', 26, GREEN, 'mm')
    c.text(x0 + 330, y0 - 500, '落在桌面上：时间短，力大', 'bold', 26, NRED, 'mm')
    caps(c, t, [(0, 7, '落在硬桌面上：一瞬间就停下，冲击又大又急'),
                (7.2, 14, '落在气泡膜上：泡泡被慢慢压扁，停下来多用了一点时间'),
                (14.2, 22, '两条曲线下面「推」的总量一样，时间拉长了，最大的冲击力就小了（示意）')], y=1010)


# ---------------------------------------------------------------- E279 购物车万向轮
def _caster(c, px, py, heading, swivel, trail):
    """px,py：转轴位置；heading：车的前进方向（弧度，0=向右）；swivel：轮子朝向；trail：偏距。"""
    wx = px - trail * math.cos(swivel)
    wy = py - trail * math.sin(swivel)
    c.line([(px, py), (wx, wy)], mix(BG, METAL, 1.0), 8)
    c.ellipse(px, py, 12, 12, fill=NRED)
    dx, dy = 40 * math.cos(swivel), 40 * math.sin(swivel)
    c.line([(wx - dx, wy - dy), (wx + dx, wy + dy)], mix(BG, (60, 60, 70), 1.0), 18)


def e279_trail(c, t, i):
    corner_tag(c, '第 279 集 · 转轴往前偏一点')
    c.text(60, 96, '万向轮的转轴不在轮子正上方，而是往前偏出一小段；车往哪推，地面就把轮子拖到转轴后面，轮子自己就转过去了', 'serif', 36, INK)
    # 车从左往右走，然后转向下
    turn = min(1.0, max(0.0, (t - 6) / 4))
    heading = turn * math.pi / 2
    sw_target = heading
    lag = math.exp(-max(0.0, t - 6) * 0.8) * (1 if t > 6 else 0)
    swivel = sw_target - 0.9 * lag * (1 if t > 6 else 0)
    cx, cy = 960, 520
    c.rect(cx - 300, cy - 160, cx + 300, cy + 160, outline=mix(BG, METAL, 0.6), width=4, r=20)
    _caster(c, cx + 220, cy, heading, swivel, 70)
    c.arrow(cx + 320, cy + 220, cx + 320 + 160 * math.cos(heading), cy + 220 + 160 * math.sin(heading), GREEN, 6, 18)
    c.text(cx + 330, cy + 300 + 60 * math.sin(heading), '推的方向', 'bold', 24, GREEN, 'lm')
    c.text(cx + 220, cy - 60, '转轴', 'bold', 24, NRED, 'mm')
    c.text(cx - 200, 820, '红点：转轴　灰杆：偏距　黑条：轮子', 'sans', 24, MUTED, 'lm')
    caps(c, t, [(0, 7, '直着推：轮子跟在转轴后面，稳稳地走'),
                (7.2, 14, '一拐弯，地面的摩擦拖着轮子，绕着转轴转到新方向的后面'),
                (14.2, 22, '不用电机，也不用人管，轮子自己就「认路」（示意）')], y=1010)


def e279_compare(c, t, i):
    corner_tag(c, '第 279 集 · 没有偏距，轮子乱摆')
    c.text(60, 96, '转轴正好在轮子正上方，地面拖不动它转向，轮子左右乱摆；往前偏 2 厘米，轮子马上转到后面乖乖跟着', 'serif', 36, INK)
    for j, (lab, trail) in enumerate([('转轴在正上方', 0), ('转轴前偏 2 厘米', 70)]):
        cx, cy = 560 + j * 800, 540
        if trail == 0:
            sw = 0.7 * math.sin(t * 5)
            c.text(cx, 800, lab + '：乱摆', 'bold', 28, NRED, 'mm')
        else:
            sw = 0.6 * math.exp(-t * 0.6) * math.cos(t * 2)
            c.text(cx, 800, lab + '：自己跟着走', 'bold', 28, GREEN, 'mm')
        c.rect(cx - 200, cy - 120, cx + 200, cy + 120, outline=mix(BG, METAL, 0.6), width=4, r=16)
        _caster(c, cx + 100, cy, 0, sw, trail if trail else 1)
        c.arrow(cx - 160, cy + 200, cx + 160, cy + 200, GREEN, 5, 16)
    caps(c, t, [(0, 7, '纸板小车：一个瓶盖轮的转轴在正上方，一个往前偏 2 厘米'),
                (7.2, 14, '拉着走：没偏的那个左右乱摆，偏了的稳稳跟在后面'),
                (14.2, 22, '去超市看看购物车、在家看看办公椅脚，转轴都偏在前面（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E280 卧式冰柜
def e280_sink(c, t, i):
    corner_tag(c, '第 280 集 · 冷空气重，往下沉')
    c.text(60, 96, '冷空气比热空气重：竖着开门的冰箱，门一开冷空气就从下面流出去，热空气从上面补进来', 'serif', 36, INK)
    x0, y0, x1, y1 = 700, 220, 1100, 900
    c.rect(x0, y0, x1, y1, outline=mix(BG, METAL, 1.0), width=10, r=10)
    open_ = t > 3
    if not open_:
        c.rect(x1 - 5, y0, x1 + 5, y1, fill=mix(BG, METAL, 1.0))
    random.seed(1)
    for k in range(40):
        ph = (t * 0.15 + k / 40) % 1
        if open_:
            if k % 2 == 0:  # 冷气从下方流出
                x = x1 - 300 + ph * 700
                y = y1 - 80 + random.uniform(-40, 40) + ph * 40
                c.ellipse(x, y, 9, 9, fill=mix(BG, COLD, 1.0 - ph * 0.6))
            else:  # 热空气从上方进入
                x = x1 + 400 - ph * 600
                y = y0 + 120 + random.uniform(-40, 40)
                c.ellipse(x, y, 9, 9, fill=mix(BG, WARM, 1.0))
        else:
            c.ellipse(x0 + 40 + random.uniform(0, 320), y0 + 40 + random.uniform(0, 600), 9, 9, fill=mix(BG, COLD, 1.0))
    if open_:
        c.arrow(x1 + 20, y1 - 80, x1 + 260, y1 - 50, COLD, 6, 18)
        c.arrow(x1 + 260, y0 + 120, x1 + 20, y0 + 120, WARM, 6, 18)
        c.text(x1 + 300, y1 - 30, '冷气从下面流出', 'bold', 26, COLD, 'lm')
        c.text(x1 + 300, y0 + 120, '热空气从上面补进', 'bold', 26, WARM, 'lm')
    caps(c, t, [(0, 7, '冰箱门上下各贴一条纸巾，请大人打开门'),
                (7.2, 14, '下面那条往外飘：冷空气从门的下半截流了出去'),
                (14.2, 22, '上面那条往里飘：热空气从上半截补进来（开门别太久）')], y=1010)


def e280_chest(c, t, i):
    corner_tag(c, '第 280 集 · 开口朝上，冷气出不来')
    c.text(60, 96, '超市的卧式冰柜开口朝上：冷空气沉在柜子底下，想出来得「往上爬」，所以敞着口也跑得很慢', 'serif', 36, INK)
    for j, (lab, up) in enumerate([('开口朝旁边', False), ('开口朝上', True)]):
        cx, cy = 560 + j * 800, 560
        c.rect(cx - 220, cy - 160, cx + 220, cy + 200, outline=mix(BG, METAL, 1.0), width=10, r=10)
        if up:
            c.rect(cx - 210, cy - 170, cx + 210, cy - 150, fill=BG)
        else:
            c.rect(cx + 210, cy - 150, cx + 230, cy + 190, fill=BG)
        random.seed(5 + j)
        lvl = (cy + 190 - 300) if up else (cy + 190 - 300 + min(240, t * 14))
        for k in range(36):
            x = cx + random.uniform(-195, 195)
            y = random.uniform(max(lvl, cy - 140), cy + 185)
            c.ellipse(x, y, 9, 9, fill=mix(BG, COLD, 1.0))
        if not up:
            for k in range(6):
                ph = (t * 0.3 + k / 6) % 1
                c.ellipse(cx + 240 + ph * 160, cy + 150 + ph * 30, 9, 9, fill=mix(BG, COLD, 1 - ph * 0.7))
        temp = (-2 + 0.3 * t) if not up else (-2 + 0.05 * t)
        c.text(cx, cy + 290, f'{lab}：{temp:.0f} ℃（示意）', 'bold', 28, GREEN if up else NRED, 'mm')
    caps(c, t, [(0, 7, '两个箱子各放一个冰袋：一个开口朝上，一个侧过来开口朝旁边'),
                (7.2, 14, '朝旁边的：冷气从开口下沿流出去，箱子慢慢变暖'),
                (14.2, 22, '朝上的：冷气沉在底下出不来，20 分钟后还是冷的（以实测为准）')], y=1010)


CLIPS = {
 'E278_压扁': (e278_squash, 22), 'E278_拉长': (e278_time, 22),
 'E278_片头': (titles.opening(SER53, VOL53, S53A, 6, '1957 年发明了气泡膜'), 7),
 'E278_片尾': (titles.closing(SER53, VOL53, S53A, 6, '下集：购物车的小轮子怎么自己认路？'), 7),
 'E279_偏距': (e279_trail, 22), 'E279_对比': (e279_compare, 22),
 'E279_片头': (titles.opening(SER53, VOL53, S53A, 7, '20 世纪 30 年代出现购物车'), 7),
 'E279_片尾': (titles.closing(SER53, VOL53, S53A, 7, '下集：敞着口的冰柜，冷气为什么不跑？'), 7),
 'E280_下沉': (e280_sink, 22), 'E280_开口': (e280_chest, 22),
 'E280_片头': (titles.opening(SER53, VOL53, S53A, 8, '超市常用顶部开口的卧式冷柜'), 7),
 'E280_片尾': (titles.closing(SER53, VOL53, S53A, 8, '下集：扶梯台阶怎么一会儿平一会儿高？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
