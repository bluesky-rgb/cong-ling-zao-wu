"""第五十二季（古法解密 23.0：驿路与车马）第一批：B230 烽燧、B231 驿马接力、B232 虎符 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB52 = [('B230', '烽燧'), ('B231', '驿马接力'), ('B232', '虎符'), ('B233', '马鞍'), ('B234', '马蹄铁'),
        ('B235', '车脂'), ('B236', '车辖'), ('B237', '铁箍车轮'), ('B238', '车轫'), ('B239', '竹杖')]
VOL52 = '第五十二季 · 古法解密 23.0'
EARTH = (190, 150, 100)
FIRE = (240, 140, 60)
SMOKE = (170, 170, 175)
BRONZE = (190, 150, 80)
ROAD = (150, 130, 100)
HORSE = (150, 100, 70)


def _tower(c, x, y, lit, n=1):
    c.poly([(x - 50, y), (x - 34, y - 160), (x + 34, y - 160), (x + 50, y)], mix(BG, EARTH, 1.0))
    c.rect(x - 40, y - 176, x + 40, y - 160, fill=mix(BG, EARTH, 0.8))
    if lit:
        for k in range(n):
            ox = x + (k - (n - 1) / 2) * 30
            c.ellipse(ox, y - 196, 12, 18, fill=FIRE)
            for s in range(3):
                c.ellipse(ox + 6 * math.sin(s), y - 240 - s * 40, 14 + s * 6, 12 + s * 5, fill=mix(BG, SMOKE, 0.5 - s * 0.12))


# ---------------------------------------------------------------- B230 烽燧
def b230_relay(c, t, i):
    corner_tag(c, 'B230 · 一座接一座传')
    c.text(60, 96, '沿路每隔一段修一座烽燧，看见上一座点起烽烟，就马上点自己的：光和烟一座接一座传，比快马快得多', 'serif', 36, INK)
    xs = [220 + k * 370 for k in range(5)]
    gy = 700
    c.line([(100, gy), (1820, gy)], mix(BG, EARTH, 0.6), 4)
    ph = (t % 11) / 11
    for k, x in enumerate(xs):
        _tower(c, x, gy, ph * 11 > k * 1.2 + 0.5)
    # 快马
    hx = 220 + ph * 11 * 22
    c.ellipse(hx, gy + 120, 34, 20, fill=mix(BG, HORSE, 1.0))
    c.text(hx, gy + 170, '快马', 'bold', 24, NRED, 'mm')
    c.text(1500, gy + 170, '烽烟：几乎同时到达终点（示意）', 'bold', 26, GREEN, 'mm')
    c.text(220, gy + 40, '边关', 'sans', 24, MUTED, 'mm')
    c.text(xs[-1], gy + 40, '都城方向', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '边关看见敌人，点起第一座烽燧'),
                (7.2, 14, '下一座看见就点，一座接一座，烟和火一路传下去'),
                (14.2, 22, '快马还在半路，信号早已传到远方（手电接力实验，不点火）')], y=1010)


def b230_code(c, t, i):
    corner_tag(c, 'B230 · 点几道烟就是暗号')
    c.text(60, 96, '点几道烟、白天放烟夜里举火，都是事先约好的：传过去的不只是「有敌人」，还有「来了多少」', 'serif', 36, INK)
    codes = [(1, '少数敌人'), (2, '敌人较多'), (3, '大批敌人')]
    k = min(2, int(t / 7.3))
    for j, (n, lab) in enumerate(codes):
        x = 400 + j * 560
        on = j == k
        _tower(c, x, 720, True if on else False, n)
        c.text(x, 790, f'{n} 道烟', 'bold', 30, INK if on else MUTED, 'mm')
        c.text(x, 850, lab, 'bold', 28, NRED if on else MUTED, 'mm')
    c.text(960, 220, '约定的具体内容各代不同（示意，拍摄前核对）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '一道烟：来的敌人不多'),
                (7.2, 14, '两道烟：敌人更多了'),
                (14.2, 22, '三道烟：大批敌人，一路传下去，后方早早准备')], y=1010)


# ---------------------------------------------------------------- B231 驿马接力
def b231_tired(c, t, i):
    corner_tag(c, 'B231 · 一匹马跑全程，越跑越慢')
    c.text(60, 96, '一匹马、一个人跑全程，体力越用越少，后面几段越来越慢；平均下来，整段路的速度就低了', 'serif', 36, INK)
    segs = [10, 11.5, 13.5, 16]
    x0, y0 = 300, 820
    for k, v in enumerate(segs):
        x = x0 + k * 340
        a = fade(t, 1 + k * 3, 2 + k * 3)
        h = v * 30 * a
        c.rect(x, y0 - h, x + 200, y0, fill=mix(BG, NRED, 0.4 + 0.15 * k), r=6)
        c.text(x + 100, y0 - h - 30, f'{v:g} 秒' if a > 0.5 else '', 'bold', 28, INK, 'mm')
        c.text(x + 100, y0 + 40, f'第 {k + 1} 段', 'sans', 24, MUTED, 'mm')
    c.line([(260, y0), (1660, y0)], mix(BG, INK, 0.5), 3)
    c.text(960, 230, '一个人连跑 4 段 50 米（数字示意，以实测为准）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '第一段跑得最快'),
                (7.2, 14, '越往后越累，一段比一段慢'),
                (14.2, 22, '一匹马跑一整天也是这样：越跑越慢')], y=1010)


def b231_relay(c, t, i):
    corner_tag(c, 'B231 · 换马换人，每一段都全速')
    c.text(60, 96, '每隔一段设一个驿站，换上歇好的马和人接着跑：每一段都是最快的速度，整条路的平均速度就高', 'serif', 36, INK)
    y = 560
    c.line([(160, y + 40), (1760, y + 40)], mix(BG, ROAD, 1.0), 10)
    st = [160 + k * 400 for k in range(5)]
    for k, x in enumerate(st):
        c.rect(x - 40, y - 60, x + 40, y + 20, fill=mix(BG, EARTH, 0.7), r=6)
        c.text(x, y - 90, '驿站' if 0 < k < 4 else ('出发' if k == 0 else '到达'), 'sans', 22, MUTED, 'mm')
    ph = min(1.0, t / 20)
    pos = 160 + 1600 * ph
    seg_i = min(3, int((pos - 160) / 400))
    cols = [NRED, (90, 150, 220), GREEN, (200, 160, 60)]
    c.ellipse(pos, y + 10, 36, 22, fill=mix(BG, cols[seg_i], 1.0))
    c.text(pos, y - 30, f'第 {seg_i + 1} 匹', 'bold', 22, INK, 'mm')
    for k in range(4):
        x = 300 + k * 340
        a = fade(t, 1 + k * 5, 2 + k * 5)
        h = 10 * 30 * a
        c.rect(x, 900 - h * 0.5, x + 200, 900, fill=mix(BG, cols[k], 0.6), r=6)
        c.text(x + 100, 900 - h * 0.5 - 24, '10 秒' if a > 0.5 else '', 'bold', 24, INK, 'mm')
    c.text(960, 220, '4 人接力，每人 50 米：每一段都差不多一样快（示意）', 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '第一个人全速跑到驿站，把文书交给下一个人'),
                (7.2, 14, '下一个人歇得好好的，也是全速跑'),
                (14.2, 22, '每一段都快，总时间就短：唐代急件一天能传几百里（拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- B232 虎符
def _tiger(c, cx, cy, sx, half, col, jag_seed=7, offset=0, fake=False):
    """画一只侧面的简化老虎，half=-1 左半 / 1 右半 / 0 整只；分界是一条锯齿线。"""
    random.seed(jag_seed)
    jag = [(cx + random.uniform(-14, 14), cy - 90 + k * 18) for k in range(11)]
    if fake:
        random.seed(99)
        jag = [(x + random.uniform(-10, 10), y) for x, y in jag]
    body = [(cx - 260, cy - 40), (cx - 200, cy - 90), (cx + 180, cy - 90), (cx + 260, cy - 130), (cx + 300, cy - 80),
            (cx + 260, cy - 30), (cx + 220, cy + 90), (cx - 240, cy + 90)]
    def clip(side):
        pts = []
        if side < 0:
            pts = [(cx - 260, cy - 40), (cx - 200, cy - 90)] + jag + [(cx - 240, cy + 90)]
        else:
            pts = jag + [(cx + 220, cy + 90), (cx + 260, cy - 30), (cx + 300, cy - 80), (cx + 260, cy - 130), (cx + 180, cy - 90)]
        return [(x + offset, y) for x, y in pts]
    if half == 0:
        c.poly(body, col)
    else:
        c.poly(clip(half), col)
    return jag


def b232_match(c, t, i):
    corner_tag(c, 'B232 · 一分为二，两半对合')
    c.text(60, 96, '虎符从中间分成左右两半：朝廷留一半，将军拿一半；来人带着朝廷那一半，两半一合严丝合缝，才能发兵', 'serif', 36, INK)
    cx, cy = 960, 540
    gap = 300 * max(0.0, 1 - max(0.0, t - 7.2) / 6) if t > 7.2 else 300
    _tiger(c, cx, cy, 1, -1, mix(BG, BRONZE, 1.0), offset=-gap)
    _tiger(c, cx, cy, 1, 1, mix(BG, BRONZE, 0.85), offset=gap)
    c.text(cx - gap - 120, cy, '甲兵之符', 'serif', 30, INK, 'mm')
    c.text(cx + gap + 80, cy, '右在君', 'serif', 30, INK, 'mm')
    c.text(cx - gap - 120, cy + 170, '将军的左半', 'bold', 26, INK, 'mm')
    c.text(cx + gap + 80, cy + 170, '朝廷的右半', 'bold', 26, INK, 'mm')
    if gap < 2:
        c.text(960, 880, '锯齿全对上、字也连起来：命令是真的（铭文示意）', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '一只铜老虎，从中间分成左右两半，上面的字跨过接缝'),
                (7.2, 14, '朝廷派人带着右半边来到边关'),
                (14.2, 22, '两半一合：接缝一点不差，字也连得上，将军才发兵')], y=1010)


def b232_fake(c, t, i):
    corner_tag(c, 'B232 · 仿造的另一半对不上')
    c.text(60, 96, '只看见一半，很难仿出另一半：接缝上每个小齿的形状、跨在缝上的字，差一点就合不拢、对不上', 'serif', 36, INK)
    cx, cy = 960, 520
    _tiger(c, cx, cy, 1, -1, mix(BG, BRONZE, 1.0), offset=0)
    _tiger(c, cx, cy, 1, 1, mix(BG, BRONZE, 0.6), offset=6 if t > 7.2 else 0, fake=t > 7.2)
    c.text(cx - 130, cy, '甲兵之符', 'serif', 30, INK, 'mm')
    c.text(cx + 90, cy + (16 if t > 7.2 else 0), '右在君', 'serif', 30, INK, 'mm')
    if t > 7.2:
        random.seed(7)
        for k in range(10):
            y = cy - 81 + k * 18
            c.ellipse(cx + 8, y, 5, 5, fill=mix(BG, (255, 240, 200), 0.9))
        c.text(960, 820, '缝里漏光，字也错开：是假的', 'bold', 30, NRED, 'mm')
    else:
        c.text(960, 820, '真的那一半：严丝合缝', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 7, '用原来的那一半去合：一点缝都没有'),
                (7.2, 14, '换成照着左半边仿剪的右半边：对着灯一看，缝里漏光'),
                (14.2, 22, '形状越不规则，越难仿；纸板实验由大人剪（以实测为准）')], y=1010)


CLIPS = {
 'B230_接力': (b230_relay, 22), 'B230_暗号': (b230_code, 22),
 'B230_片头': (titles.opening(BSER, VOL52, SB52, 0, '汉代边塞烽燧相连'), 7),
 'B230_片尾': (titles.closing(BSER, VOL52, SB52, 0, '下集：急件为什么要一路换马？'), 7),
 'B231_变慢': (b231_tired, 22), 'B231_换马': (b231_relay, 22),
 'B231_片头': (titles.opening(BSER, VOL52, SB52, 1, '唐代驿站相连'), 7),
 'B231_片尾': (titles.closing(BSER, VOL52, SB52, 1, '下集：将军怎么认出真命令？'), 7),
 'B232_对合': (b232_match, 22), 'B232_仿造': (b232_fake, 22),
 'B232_片头': (titles.opening(BSER, VOL52, SB52, 2, '战国秦汉用铜虎符调兵'), 7),
 'B232_片尾': (titles.closing(BSER, VOL52, SB52, 2, '下集：垫了马鞍，马背为什么不疼？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
