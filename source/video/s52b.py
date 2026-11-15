"""第五十二季（古法解密 23.0：驿路与车马）第二批：B233 马鞍、B234 马蹄铁、B235 车脂 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s52a import SB52, VOL52, EARTH, HORSE, ROAD

LEATHER = (150, 95, 55)
SPONGE = (230, 210, 120)
HOOF = (90, 80, 70)
IRON = (150, 155, 165)
OIL = (230, 190, 60)
WOODC = (170, 125, 80)


def _sponge(c, x0, x1, y, dents):
    """dents: [(xa, xb, depth)]"""
    pts = [(x0, y)]
    for xa, xb, d in dents:
        pts += [(xa - 30, y), (xa, y + d), (xb, y + d), (xb + 30, y)]
    pts += [(x1, y), (x1, y + 200), (x0, y + 200)]
    c.poly(pts, mix(BG, SPONGE, 0.8))


# ---------------------------------------------------------------- B233 马鞍
def b233_area(c, t, i):
    corner_tag(c, 'B233 · 同样的重量，摊开就压得浅')
    c.text(60, 96, '同样一瓶水压在海绵上：顶在一根筷子上陷得最深，放在瓶盖上浅一些，放在一本书上几乎不陷', 'serif', 36, INK)
    items = [('筷子', 12, 120), ('瓶盖', 60, 50), ('一本书', 260, 12)]
    k = min(2, int(t / 7.3))
    y = 640
    for j, (lab, w, d) in enumerate(items):
        cx = 380 + j * 580
        show = j <= k
        dd = d if show else 0
        _sponge(c, cx - 250, cx + 250, y, [(cx - w / 2, cx + w / 2, dd)])
        if show:
            c.rect(cx - w / 2, y + dd - 110, cx + w / 2, y + dd, fill=mix(BG, WOODC, 1.0))
            c.rect(cx - 50, y + dd - 330, cx + 50, y + dd - 110, fill=mix(BG, (120, 170, 230), 0.7), r=14)
            c.text(cx, y + 250, f'{lab}：陷 {"深" if d > 80 else ("一点" if d > 30 else "很浅")}', 'bold', 28, INK, 'mm')
    c.text(960, 940, '压力 = 重量 ÷ 面积：面积越大，每一处受的压力越小（示意）', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '一瓶水顶在一根竖着的筷子上：海绵被压出一个深坑'),
                (7.2, 14, '换成瓶盖：面积大了，坑浅了'),
                (14.2, 22, '换成一本书：重量摊到一大片上，几乎不陷')], y=1010)


def b233_saddle(c, t, i):
    corner_tag(c, 'B233 · 两块宽鞍垫，中间留空')
    c.text(60, 96, '马鞍底下是两块宽宽的鞍垫，搭在马背脊梁两侧，把人的重量摊开；中间拱起留空，不压马的脊梁骨', 'serif', 36, INK)
    cx, cy = 960, 640
    # 马背横截面
    c.ellipse(cx, cy + 120, 380, 260, fill=mix(BG, HORSE, 1.0))
    c.ellipse(cx, cy - 120, 26, 26, fill=mix(BG, (240, 230, 210), 1.0))
    c.text(cx, cy - 60, '脊梁', 'bold', 22, (255, 255, 255), 'mm')
    if t < 7.2:
        c.rect(cx - 30, cy - 260, cx + 30, cy - 146, fill=mix(BG, NRED, 0.8))
        c.arrow(cx, cy - 330, cx, cy - 270, NRED, 6, 16)
        c.text(cx + 220, cy - 290, '光着骑：压在脊梁上', 'bold', 26, NRED, 'lm')
    else:
        for s in (-1, 1):
            c.poly([(cx + s * 60, cy - 150), (cx + s * 260, cy - 80), (cx + s * 250, cy - 40), (cx + s * 50, cy - 110)], mix(BG, LEATHER, 1.0))
            for k in range(5):
                x = cx + s * (80 + k * 40)
                c.arrow(x, cy - 230 + k * 14, x, cy - 150 + k * 14 + 10, GREEN, 4, 12)
        c.arc(cx, cy - 150, 90, 70, 180, 360, mix(BG, LEATHER, 1.0), 14)
        c.text(cx, cy - 300, '中间拱起留空', 'bold', 26, GREEN, 'mm')
        c.text(cx + 330, cy - 120, '鞍垫把重量摊到两侧', 'bold', 26, GREEN, 'lm')
    caps(c, t, [(0, 7, '光着骑，人的重量集中压在马背中间的脊梁上'),
                (7.2, 14, '两块宽鞍垫搭在脊梁两侧，重量摊到一大片肌肉上'),
                (14.2, 22, '中间拱起留空，脊梁不受压：人坐得稳，马也不疼（示意）')], y=1010)


# ---------------------------------------------------------------- B234 马蹄铁
def b234_wear(c, t, i):
    corner_tag(c, 'B234 · 硬路上，蹄子磨得比长得快')
    c.text(60, 96, '马蹄的角质会慢慢长，但天天踩在石头路上，磨掉得比长出来的快；钉上铁掌，磨的就是铁，不是蹄', 'serif', 36, INK)
    gy = 760
    ph = min(1.0, t / 20)
    for j, (lab, shoe) in enumerate([('没有铁掌', False), ('钉了铁掌', True)]):
        cx = 560 + j * 800
        if shoe:
            st = 30 - 10 * ph
            c.rect(cx - 150, gy - st, cx + 150, gy, fill=mix(BG, IRON, 1.0), r=4)
            for k in (-100, -40, 40, 100):
                c.rect(cx + k - 4, gy - st - 14, cx + k + 4, gy - st + 4, fill=mix(BG, (80, 80, 90), 1.0))
            top, bot = gy - st - 260, gy - st
        else:
            wear = 70 * ph
            top, bot = gy - 290 + wear, gy
            if wear > 2:
                c.rect(cx - 150, gy - 290 + 260, cx + 150, gy - 290 + 260 + 0, fill=BG)
        c.poly([(cx - 110, top), (cx + 110, top), (cx + 140, bot), (cx - 140, bot)], mix(BG, HOOF, 1.0))
        c.rect(cx - 60, top - 140, cx + 60, top, fill=mix(BG, HORSE, 1.0))
        c.text(cx, 250, lab, 'bold', 30, NRED if not shoe else GREEN, 'mm')
        c.text(cx, 900, '蹄子越磨越短（示意）' if not shoe else '铁掌磨薄一点，蹄子没磨（示意）', 'bold', 26, INK, 'mm')
    c.rect(200, gy, 1720, gy + 40, fill=mix(BG, ROAD, 1.0))
    random.seed(2)
    for k in range(40):
        c.ellipse(random.uniform(210, 1710), gy + random.uniform(8, 32), 6, 4, fill=mix(BG, (120, 110, 90), 1.0))
    caps(c, t, [(0, 7, '光着蹄子在石头路上走，蹄底的角质一点点磨掉'),
                (7.2, 14, '钉上一圈铁掌：碰到石头的是铁'),
                (14.2, 22, '铁比角质耐磨得多，铁掌磨坏了就换一副（示意）')], y=1010)


def b234_test(c, t, i):
    corner_tag(c, 'B234 · 砂纸上磨 50 下')
    c.text(60, 96, '两块一样的小木块在粗砂纸上各磨 50 下：底下贴了硬币的那块几乎没少，不贴的那块磨掉了一层', 'serif', 36, INK)
    n = min(50, int(t / 20 * 50))
    off = 160 * math.sin(t * 4) if t < 20 else 0
    gy = 700
    c.rect(200, gy, 1720, gy + 30, fill=mix(BG, (180, 150, 110), 1.0))
    for j, (lab, coin) in enumerate([('不贴', False), ('底下贴硬币', True)]):
        cx = 560 + j * 800 + off
        loss = 0 if coin else 40 * n / 50
        c.rect(cx - 110, gy - 200 + loss, cx + 110, gy - (16 if coin else 0), fill=mix(BG, WOODC, 1.0), r=6)
        if coin:
            c.rect(cx - 70, gy - 16, cx + 70, gy, fill=mix(BG, IRON, 1.0), r=4)
        c.text(560 + j * 800, 360, lab, 'bold', 30, GREEN if coin else NRED, 'mm')
        c.text(560 + j * 800, 860, f'磨掉约 {0.0 if coin else 0.08 * n:.1f} 克（示意）', 'bold', 26, INK, 'mm')
    c.text(960, 260, f'第 {n} 下', 'bold', 34, INK, 'mm')
    caps(c, t, [(0, 7, '砂纸固定在桌上，两块木块先称一称'),
                (7.2, 14, '用同样的力各来回磨 50 下'),
                (14.2, 22, '再称：贴硬币的几乎没少，磨的是金属（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B235 车脂
def b235_film(c, t, i):
    corner_tag(c, 'B235 · 油膜把两个面隔开')
    c.text(60, 96, '车轴和车轮的孔放大看都是坑坑洼洼的：干着转，凸起互相卡住；抹上油，一层油膜把两个面隔开', 'serif', 36, INK)
    oil = t > 7.2
    ph = t * (2.0 if oil else 0.6)
    y0, y1 = 520, 640
    random.seed(5)
    top = [(200 + k * 30, y0 - 10 + random.uniform(-14, 14)) for k in range(52)]
    bot = [(200 + k * 30, y1 + (0 if oil else -60) + random.uniform(-14, 14)) for k in range(52)]
    off = (ph * 120) % 30
    c.poly([(x - off, y) for x, y in top] + [(1760, 300), (200, 300)], mix(BG, WOODC, 1.0))
    c.poly([(x, y) for x, y in bot] + [(1760, 840), (200, 840)], mix(BG, (110, 110, 120), 1.0))
    if oil:
        c.rect(200, y0 + 10, 1760, y1 - 20, fill=mix(BG, OIL, 0.55))
        c.text(980, (y0 + y1) / 2, '油膜', 'bold', 30, INK, 'mm')
    else:
        for k in range(6):
            c.ellipse(300 + k * 260, y0 + 30, 16, 16, fill=NRED)
        c.text(980, 900, '凸起互相卡住：难转、发热、磨损', 'bold', 28, NRED, 'mm')
    c.text(980, 270, '车轮孔（转动）', 'sans', 24, (255, 255, 255), 'mm')
    c.text(980, 800, '车轴（固定）', 'sans', 24, (255, 255, 255), 'mm')
    if oil:
        c.text(980, 900, '两个面不直接碰：转得轻快，也不磨轴（示意）', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '放大看：车轴和轮孔表面都有凸起，干着转，凸起互相卡'),
                (7.2, 14, '抹上油脂，一层油膜挤进两个面之间'),
                (14.2, 22, '凸起不再直接碰在一起，摩擦小了，车推着就轻快')], y=1010)


def b235_spins(c, t, i):
    corner_tag(c, 'B235 · 拨一下，数圈数')
    c.text(60, 96, '线轴套在铅笔上，用同样的力拨一下：干的时候很快停下，抹了油转得圈数多得多', 'serif', 36, INK)
    res = [('干的', 3, NRED), ('抹食用油', 9, GREEN), ('抹肥皂水', 6, (90, 150, 220))]
    k = min(2, int(t / 7.3))
    tt = t - k * 7.3
    for j, (lab, n, col) in enumerate(res):
        cx = 380 + j * 580
        on = j == k
        done = j < k
        ang = 0
        if on:
            T = 5.0
            u = min(1, tt / T)
            ang = n * 360 * (1 - (1 - u) ** 2)
        elif done:
            ang = n * 360
        c.line([(cx - 200, 560), (cx + 200, 560)], mix(BG, (230, 200, 90), 1.0), 12)
        c.ellipse(cx, 560, 110, 110, fill=mix(BG, WOODC, 0.9))
        a = math.radians(ang)
        c.ellipse(cx + 85 * math.cos(a), 560 + 85 * math.sin(a), 16, 16, fill=col)
        c.ellipse(cx, 560, 14, 14, fill=mix(BG, (230, 200, 90), 1.0))
        c.text(cx, 740, lab, 'bold', 30, col if (on or done) else MUTED, 'mm')
        c.text(cx, 800, f'约 {ang / 360:.0f} 圈' if (on or done) else '', 'bold', 28, INK, 'mm')
    c.text(960, 900, '圈数是示意，按实测填写', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '干的铅笔：拨一下，转几圈就停'),
                (7.2, 14, '抹一点食用油：同样的力，转的圈数多得多'),
                (14.2, 22, '肥皂水也有点用；油脂最耐用，所以古人给车轴抹的是动物油脂')], y=1010)


CLIPS = {
 'B233_摊开': (b233_area, 22), 'B233_留空': (b233_saddle, 22),
 'B233_片头': (titles.opening(BSER, VOL52, SB52, 3, '汉代已有马鞍'), 7),
 'B233_片尾': (titles.closing(BSER, VOL52, SB52, 3, '下集：为什么要给马钉铁掌？'), 7),
 'B234_磨损': (b234_wear, 22), 'B234_砂纸': (b234_test, 22),
 'B234_片头': (titles.opening(BSER, VOL52, SB52, 4, '马蹄铁在中国唐宋以后逐渐使用'), 7),
 'B234_片尾': (titles.closing(BSER, VOL52, SB52, 4, '下集：车轴抹了油，为什么推得轻快？'), 7),
 'B235_油膜': (b235_film, 22), 'B235_圈数': (b235_spins, 22),
 'B235_片头': (titles.opening(BSER, VOL52, SB52, 5, '《诗经》里有「载脂载舝」'), 7),
 'B235_片尾': (titles.closing(BSER, VOL52, SB52, 5, '下集：车轮为什么不会滑脱？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
