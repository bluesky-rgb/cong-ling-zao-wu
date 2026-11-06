"""第十九季（第六层）第二批：E105 语音识别、E106 降噪耳机、E107 电动汽车 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s19a import S19A, SER19, VOL19, ELEC

VOW = {'a': (800, 1200, 2500), 'i': (300, 2300, 3000), 'u': (320, 800, 2300)}
NOISE = (230, 120, 90)
ANTI = (90, 170, 240)

def env(f, F):
    return sum(math.exp(-((f - fk) / 160) ** 2) * w for fk, w in zip(F, (1.0, 0.8, 0.4))) + 0.05

# ---------------------------------------------------------------- E105 语音识别
def e105_spectrum(c, t, i):
    corner_tag(c, '第 105 集 · 每个元音一个花纹')
    c.text(60, 96, '同一个音高，嘴型一变，哪几根「频率柱」高就变了', 'serif', 40, INK)
    keys = ['a', 'i', 'u']
    k = min(int(t / 7), 2)
    v = keys[k]
    F = VOW[v]
    f0 = 150
    # waveform
    x0, y0, W = 120, 400, 760
    pts = []
    for j in range(200):
        tt = j / 200 * 3 / f0
        s = sum(env(f0 * h, F) * math.sin(2 * math.pi * f0 * h * tt + h) for h in range(1, 25))
        pts.append((x0 + W * j / 200, y0 + 14 * s))
    c.line(pts, SPARK, 3)
    c.text(x0, y0 - 130, '声音的波形', 'sans', 24, MUTED, 'lm')
    # spectrum bars
    bx, by, BW, BH = 1000, 640, 820, 380
    c.line([(bx, by), (bx + BW, by)], LINE, 3)
    for h in range(1, 25):
        f = f0 * h
        x = bx + BW * f / 3600
        hh = BH * env(f, F) / 1.05
        c.rect(x - 7, by - hh, x + 7, by, fill=mix(BG, ELEC, 0.9))
    for kk, fk in enumerate(F[:2]):
        x = bx + BW * fk / 3600
        c.line([(x, by - BH - 30), (x, by + 10)], mix(BG, NRED, 0.7), 2)
        c.text(x, by - BH - 50, f'F{kk + 1}', 'mono', 22, NRED, 'mm')
    for f in (0, 1000, 2000, 3000):
        c.text(bx + BW * f / 3600, by + 30, f'{f}', 'mono', 20, MUTED, 'mm')
    c.text(bx + BW / 2, by + 70, '频率（赫兹）', 'sans', 22, MUTED, 'mm')
    c.text(500, 640, f'「{v}」', 'bold', 120, INK, 'mm')
    c.text(500, 780, '共振峰位置（约，拍摄前核对）', 'sans', 22, MUTED, 'mm')
    c.text(500, 820, f'F1 ≈ {F[0]}　F2 ≈ {F[1]}', 'mono', 26, NRED, 'mm')
    caps(c, t, [(0, 7, '说「啊」：声带振出一串等距的频率，嘴和喉咙像一个音箱，把其中几段放大，叫共振峰'),
                (7, 14, '说「衣」：音高没变，嘴型变扁，第一个峰往左挪，第二个峰跑到右边去了'),
                (14, 22, '说「乌」：两个峰都挤在左边。机器认字，先认的就是这些花纹')], y=1010)

TEMPL = {'开灯': 1, '关灯': 2, '播放': 3}

def _sgram(c, x0, y0, w, h, seed, a=1.0, noise=0.0):
    rnd = random.Random(seed)
    cols, rows = 16, 10
    rn = random.Random(99)
    for ci in range(cols):
        for ri in range(rows):
            v = 0.5 + 0.5 * math.sin(ci * 0.6 * seed + ri * 0.9 + seed)
            v = max(0, min(1, v * rnd.uniform(0.6, 1) + noise * rn.uniform(-0.3, 0.3)))
            c.rect(x0 + ci * w / cols, y0 + ri * h / rows, x0 + (ci + 1) * w / cols, y0 + (ri + 1) * h / rows, fill=mix(BG, mix((40, 60, 120), SPARK, v), a))

def e105_match(c, t, i):
    corner_tag(c, '第 105 集 · 拿图去比')
    c.text(60, 96, '把一句话变成一张「声谱图」，再找最像的那一张', 'serif', 40, INK)
    c.text(330, 230, '你说的话', 'bold', 28, INK, 'mm')
    _sgram(c, 130, 270, 400, 260, 2, 1.0, 0.6)
    c.text(330, 570, '横：时间　竖：频率　亮：响', 'sans', 20, MUTED, 'mm')
    scores = {'开灯': 0.41, '关灯': 0.87, '播放': 0.23}
    for k, (nm, sd) in enumerate(TEMPL.items()):
        a = fade(t, 3 + k * 2, 4 + k * 2)
        if a <= 0: continue
        y = 220 + k * 230
        _sgram(c, 900, y, 300, 180, sd, a)
        c.text(1240, y + 60, nm, 'bold', 30, mix(BG, INK, a), 'lm')
        sc = scores[nm] * fade(t, 10, 14)
        c.rect(1400, y + 100, 1400 + 360 * sc, y + 136, fill=mix(BG, GREEN if nm == '关灯' else MUTED, a))
        c.text(1780, y + 118, f'{sc * 100:.0f}%', 'mono', 24, mix(BG, INK, a), 'lm')
        c.arrow(560, 400, 880, y + 90, mix(BG, LINE, a * 0.6), 2, 12)
    b = fade(t, 15, 16)
    if b > 0:
        c.rect(130, 640, 760, 900, fill=mix(BG, SHEET, b), r=14)
        c.text(445, 690, '认出来：「关灯」', 'bold', 34, mix(BG, GREEN, b), 'mm')
        c.text(445, 760, '今天的手机不再一张张比', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(445, 805, '而是用学过海量录音的神经网络', 'sans', 24, mix(BG, INK, b), 'mm')
        c.text(445, 850, '（第 111 集人工智能再讲）', 'sans', 22, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '麦克风把声音变成数字，电脑每隔一小段时间算一次频谱，拼成一张声谱图'),
                (6.2, 14, '最早的语音识别，就是拿这张图去和事先录好的样子一张张比，看哪个最像'),
                (14.2, 22, '同一个词，每个人、每次说都不一样：所以要比的是「像不像」，不是「一不一样」')], y=1010)

# ---------------------------------------------------------------- E106 降噪耳机
def wave(x, t, ph=0):
    return 0.6 * math.sin(x * 0.045 - t * 5 + ph) + 0.4 * math.sin(x * 0.11 - t * 9 + 1.3 + ph)

def e106_cancel(c, t, i):
    corner_tag(c, '第 106 集 · 放一个反着的声音')
    c.text(60, 96, '噪声的波峰遇上反声的波谷，加起来就平了', 'serif', 40, INK)
    x0, W = 520, 1260
    on = fade(t, 7, 10)
    rows = [('噪声', 300, NOISE, 1.0, 0), ('耳机放出的反声', 540, ANTI, on, math.pi), ('耳朵听到的', 800, GREEN, 1.0, None)]
    for nm, y, col, amp, ph in rows:
        c.line([(x0, y), (x0 + W, y)], mix(BG, LINE, 0.6), 1)
        if ph is None:
            pts = [(x0 + j * 6, y - 90 * (wave(j * 6, t) * (1 - on) )) for j in range(W // 6 + 1)]
        else:
            pts = [(x0 + j * 6, y - 90 * amp * wave(j * 6, t, ph)) for j in range(W // 6 + 1)]
        c.line(pts, col, 4)
        c.text(x0 - 30, y, nm, 'bold', 26, col, 'rm')
    c.text(x0 + W / 2, 920, f'抵消掉 {on * 100:.0f}%（理想情况；实际低频消得多、高频消得少）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '耳机外面有个小麦克风，一直在听外面的嗡嗡声'),
                (7.2, 14, '里面的芯片算出一个波峰、波谷正好颠倒的声音，从耳机喇叭里放出来'),
                (14.2, 22, '两个声音一加，波峰填进波谷，耳朵里就安静了。持续的低沉嗡嗡声最好消')], y=1010)

def e106_field(c, t, i):
    corner_tag(c, '第 106 集 · 两只喇叭，一片明暗')
    c.text(60, 96, '两只喇叭放同一个音：有的地方加强，有的地方抵消', 'serif', 40, INK)
    S1, S2 = (760, 240), (1160, 240)
    lam = 260
    cell = 24
    for gx in range(160, 1760, cell):
        for gy in range(280, 960, cell):
            r1 = math.hypot(gx - S1[0], gy - S1[1]); r2 = math.hypot(gx - S2[0], gy - S2[1])
            I = math.cos(math.pi * (r1 - r2) / lam) ** 2
            ph = math.cos(2 * math.pi * (r1 + r2) / (2 * lam) - t * 6)
            v = I * (0.55 + 0.45 * ph)
            c.rect(gx, gy, gx + cell, gy + cell, fill=mix(BG, SPARK, v * 0.85))
    for S in (S1, S2):
        c.rect(S[0] - 30, S[1] - 30, S[0] + 30, S[1] + 30, fill=SHEET, outline=INK, width=3)
    c.text(960, 210, '同一个 400 赫兹的音（示意）', 'sans', 22, MUTED, 'mm')
    px = 300 + 1320 * (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi))
    py = 760
    r1 = math.hypot(px - S1[0], py - S1[1]); r2 = math.hypot(px - S2[0], py - S2[1])
    I = math.cos(math.pi * (r1 - r2) / lam) ** 2
    c.ellipse(px, py, 22, 22, fill=GREEN, outline=INK, width=3)
    c.rect(px - 70, py + 40, px + 70, py + 80, fill=SHEET, r=8)
    c.text(px, py + 60, '响' if I > 0.6 else ('轻' if I < 0.25 else '中'), 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '两只喇叭放同一个音，声波一圈圈散开，在空中交叠'),
                (7.2, 14, '走到这里，两边的波峰一起到：特别响；走几步，一边是波峰一边是波谷：几乎听不见'),
                (14.2, 22, '降噪耳机就是故意造出「波谷对波峰」：只不过它就贴在你耳朵边上')], y=1010)

# ---------------------------------------------------------------- E107 电动汽车
def e107_regen(c, t, i):
    corner_tag(c, '第 107 集 · 刹车也能充电')
    c.text(60, 96, '起步：电池推电机；刹车：车轮带着电机发电', 'serif', 40, INK)
    phase = 'go' if t < 8 else ('cruise' if t < 11 else 'brake')
    if phase == 'go': v = fade(t, 1, 8)
    elif phase == 'cruise': v = 1
    else: v = 1 - fade(t, 11, 19)
    soc = 80 - 6 * fade(t, 1, 8) - 1 * fade(t, 8, 11) + 2.5 * fade(t, 11, 19)
    c.line([(80, 760), (1840, 760)], LINE, 4)
    dist = 0
    for k in range(12):
        x = (k * 180 - (t * 260 * v) % 180)
        c.rect(80 + x, 790, 80 + x + 80, 800, fill=mix(BG, MUTED, 0.5))
    cx = 760
    c.rect(cx - 260, 560, cx + 260, 700, fill=(80, 130, 180), r=24)
    c.rect(cx - 160, 480, cx + 140, 570, fill=(70, 110, 160), r=20)
    for wx in (cx - 160, cx + 160):
        c.ellipse(wx, 710, 50, 50, fill=(40, 40, 45))
        a = t * 8 * v
        c.line([(wx, 710), (wx + 40 * math.cos(a), 710 + 40 * math.sin(a))], (200, 200, 200), 4)
    c.rect(cx - 220, 620, cx - 40, 680, fill=GREEN, r=6)
    c.text(cx - 130, 650, '电池', 'bold', 24, (20, 30, 20), 'mm')
    c.ellipse(cx + 120, 650, 34, 34, fill=COPPER)
    c.text(cx + 120, 650, '电机', 'bold', 18, (30, 20, 10), 'mm')
    if phase == 'go':
        c.arrow(cx - 30, 640, cx + 80, 640, SPARK, 5, 16)
        lab, col = '电池 → 电机：用电', SPARK
    elif phase == 'brake':
        c.arrow(cx + 80, 660, cx - 30, 660, GREEN, 5, 16)
        lab, col = '电机 → 电池：发电（能量回收）', GREEN
    else:
        lab, col = '匀速：用一点点电', MUTED
    c.text(cx, 420, lab, 'bold', 30, col, 'mm')
    c.rect(1300, 300, 1820, 520, fill=SHEET, r=14)
    c.text(1560, 340, '电量', 'sans', 24, MUTED, 'mm')
    c.rect(1340, 380, 1780, 440, outline=INK, width=3, r=6)
    c.rect(1344, 384, 1344 + 432 * soc / 100, 436, fill=GREEN, r=4)
    c.text(1560, 480, f'{soc:.1f}%（示意）', 'mono', 28, INK, 'mm')
    c.text(1560, 880, '回收多少以车型和路况为准', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 8, '起步：电池把电送进电机，电机转起来带着车轮跑'),
                (8.2, 11, '跑起来以后，车带着一大份动能'),
                (11.2, 22, '一松油门：车轮反过来带着电机转，电机变成发电机，把动能变回电送回电池，车也就慢下来了')], y=1010)

def e107_torque(c, t, i):
    corner_tag(c, '第 107 集 · 一起步就有劲')
    c.text(60, 96, '电机从零转速就有最大扭矩；汽油机要先转起来', 'serif', 40, INK)
    ox, oy, W, H = 200, 840, 1100, 560
    c.line([(ox, oy), (ox + W, oy)], LINE, 3)
    c.line([(ox, oy), (ox, oy - H)], LINE, 3)
    c.text(ox + W / 2, oy + 50, '转速', 'sans', 24, MUTED, 'mm')
    c.text(ox - 20, oy - H / 2, '扭矩（推力）', 'sans', 24, MUTED, 'rm')
    p = fade(t, 2, 12)
    N = int(100 * p)
    em = [(ox + W * x / 100, oy - H * (0.9 if x < 40 else 0.9 * 40 / x)) for x in range(0, N + 1)]
    ic = [(ox + W * x / 100, oy - H * 0.65 * math.exp(-((x - 55) / 28) ** 2)) for x in range(10, max(N, 11) + 1)]
    if len(em) > 1:
        c.line(em, GREEN, 5)
    if N > 11:
        c.line(ic, NOISE, 5)
    a = fade(t, 12, 13)
    if a > 0:
        c.text(ox + W * 0.2, oy - H * 0.9 - 30, '电机', 'bold', 28, mix(BG, GREEN, a), 'mm')
        c.text(ox + W * 0.14, oy - H * 0.3, '汽油机', 'bold', 28, mix(BG, NOISE, a), 'mm')
        c.rect(1380, 320, 1840, 640, fill=mix(BG, SHEET, a), r=14)
        c.text(1610, 370, '所以电动车', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(1610, 440, '一踩就窜出去', 'sans', 26, mix(BG, INK, a), 'mm')
        c.text(1610, 500, '大多只要一个挡', 'sans', 26, mix(BG, INK, a), 'mm')
        c.text(1610, 580, '（曲线示意，以资料为准）', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '扭矩就是转动的「劲儿」。汽油机要转到一定转速才有劲，所以要离合器和好几个挡'),
                (6.2, 13, '电机一通电，磁场马上推着转子转：从零转速开始，劲儿就是最大的'),
                (13.2, 22, '这就是第 58 集的电动机：同一个东西，倒过来转，就是第 5 集的发电机')], y=1010)


CLIPS = {
 'E105_频谱': (e105_spectrum, 22), 'E105_比对': (e105_match, 22),
 'E105_片头': (titles.opening(SER19, VOL19, S19A, 3, '1952 年 Audrey · 2011 年手机语音助手'), 7),
 'E105_片尾': (titles.closing(SER19, VOL19, S19A, 3, '下集：降噪耳机为什么能把轰鸣声「消掉」？'), 7),
 'E106_反相': (e106_cancel, 22), 'E106_干涉': (e106_field, 22),
 'E106_片头': (titles.opening(SER19, VOL19, S19A, 4, '1934 年卢格专利 · 1989 年降噪耳机'), 7),
 'E106_片尾': (titles.closing(SER19, VOL19, S19A, 4, '下集：电动车刹车时，为什么还能给电池充电？'), 7),
 'E107_能量回收': (e107_regen, 22), 'E107_扭矩': (e107_torque, 22),
 'E107_片头': (titles.opening(SER19, VOL19, S19A, 5, '1881 年特鲁韦电动三轮车 · 锂电池电动车'), 7),
 'E107_片尾': (titles.closing(SER19, VOL19, S19A, 5, '下集：手机怎么知道自己是横着还是竖着？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
