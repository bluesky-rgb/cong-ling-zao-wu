"""第十四季（古法解密 4.0）第三批：B46 夯土版筑、B47 斗拱、B48 腌菜 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s14a import SB14, VOL14

SOIL = (170, 130, 85)
WOODC = (165, 110, 65)
CUKE = (110, 170, 90)
SALT = (235, 235, 240)
WATERC = (90, 150, 210)

# ---------------------------------------------------------------- B46 夯土
def b46_compact(c, t, i):
    corner_tag(c, 'B46 · 把空隙挤掉')
    c.text(60, 96, '同一把土：夯之前全是空隙，夯之后颗粒咬在一起', 'serif', 40, INK)
    rnd = random.Random(7)
    grains = [(rnd.random(), rnd.random(), rnd.uniform(14, 26)) for _ in range(70)]
    for k, (nm, squeeze) in enumerate([('松土', 0.0), ('夯过', 1.0)]):
        x0 = 160 + k * 860
        a = fade(t, 1 + k * 6, 2 + k * 6)
        if a <= 0: continue
        prog = fade(t, 7, 11) if k else 0
        h = 520 - 200 * prog
        c.text(x0 + 330, 200, nm, 'bold', 30, mix(BG, INK, a), 'mm')
        c.rect(x0, 820 - 520, x0 + 660, 820, outline=mix(BG, LINE, a), width=3)
        for gx, gy, r in grains:
            x = x0 + 30 + gx * 600
            y = 820 - 20 - gy * (h - 40)
            c.ellipse(x, y, r, r * (1 - 0.15 * prog), fill=mix(BG, SOIL, a))
        if k:
            ty = 820 - h - 60 - 40 * abs(math.sin(t * 4)) * (1 - prog)
            c.rect(x0 + 230, ty - 40, x0 + 430, ty, fill=WOODC, r=6)
            c.line([(x0 + 330, ty - 40), (x0 + 330, ty - 160)], WOODC, 10)
        c.text(x0 + 330, 870, '空隙多、一压就散' if k == 0 else '空隙少、密度大、更硬', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '一捧松土，颗粒之间全是空隙：一压就散，一泡就塌'),
                (6.2, 13, '用木夯一层层砸下去，颗粒被挤到一起，空隙越来越少'),
                (13.2, 22, '密度变大，颗粒互相咬住：同样的土，夯过就能筑成城墙')], y=1010)

def b46_water(c, t, i):
    corner_tag(c, 'B46 · 水多少最好夯')
    c.text(60, 96, '太干夯不实，太湿也夯不实', 'serif', 40, INK)
    x0, y0, W, H = 260, 840, 1300, 560
    c.line([(x0, y0), (x0 + W, y0)], LINE, 3)
    c.line([(x0, y0), (x0, y0 - H)], LINE, 3)
    c.text(x0 + W / 2, y0 + 50, '含水量 →', 'sans', 26, MUTED, 'mm')
    c.text(x0 - 30, y0 - H / 2, '夯实后的密度', 'sans', 26, MUTED, 'rm')
    prog = fade(t, 1, 9)
    pts = []
    for k in range(int(60 * prog) + 1):
        u = k / 60
        v = math.exp(-((u - 0.45) / 0.22) ** 2)
        pts.append((x0 + 40 + u * (W - 80), y0 - 80 - v * (H - 160)))
    if len(pts) > 1:
        c.line(pts, SPARK, 6)
    a = fade(t, 9, 10)
    px = x0 + 40 + 0.45 * (W - 80)
    c.line([(px, y0), (px, y0 - H + 60)], mix(BG, GREEN, a), 2)
    c.text(px, y0 - H + 30, '最优含水量（以实测为准）', 'bold', 26, mix(BG, GREEN, a), 'mm')
    b = fade(t, 12, 13)
    c.text(x0 + 60, y0 - H + 90, '太干：颗粒之间没有水「润滑」，滑不到一起', 'sans', 22, mix(BG, INK, b), 'lm')
    c.text(x0 + W - 20, y0 - H + 90, '太湿：水占了空隙，挤不出去', 'sans', 22, mix(BG, INK, b), 'rm')
    caps(c, t, [(0, 7, '同一种土，加不同的水，用同样的力气夯'),
                (7.2, 14, '先是越湿越密：一点水让颗粒滑到一起；过了某个点，又越湿越松'),
                (14.2, 22, '太湿的时候，水占住了空隙又挤不出去：古人「手握成团、落地开花」的经验，找的就是这个点（拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- B47 斗拱
def bracket(c, cx, by, a=1.0, shift=0.0):
    col = mix(BG, WOODC, a)
    c.rect(cx - 40, by - 50, cx + 40, by, fill=col, r=4)  # 斗
    for k in range(3):
        w = 120 + k * 80
        y = by - 50 - k * 70
        s = shift * (k + 1)
        c.rect(cx - w + s, y - 26, cx + w + s, y, fill=col, r=4)  # 拱
        c.rect(cx - 30 + s, y - 50, cx + 30 + s, y - 26, fill=mix(col, BG, 0.15), r=4)
        c.rect(cx - w + s - 20, y - 50, cx - w + s + 30, y - 26, fill=mix(col, BG, 0.15), r=4)
        c.rect(cx + w + s - 30, y - 50, cx + w + s + 20, y - 26, fill=mix(col, BG, 0.15), r=4)
    return by - 50 - 3 * 70

def b47_load(c, t, i):
    corner_tag(c, 'B47 · 斗拱在干什么')
    c.text(60, 96, '一层层伸出去：把屋檐的重量，收拢到柱子上', 'serif', 40, INK)
    cx = 760
    c.rect(cx - 50, 640, cx + 50, 960, fill=WOODC, r=4)
    top = bracket(c, cx, 640)
    c.poly([(cx - 560, top + 10), (cx + 560, top + 10), (cx + 640, top + 70), (cx - 640, top + 70)], mix(BG, (110, 80, 60), 0.9))
    a = fade(t, 3, 4)
    for k in range(7):
        x = cx - 480 + k * 160
        c.arrow(x, top - 120, x, top - 10, mix(BG, NRED, a), 4, 14)
    c.text(cx, top - 150, '屋顶和出挑的屋檐压下来', 'bold', 26, mix(BG, NRED, a), 'mm')
    b = fade(t, 8, 9)
    for k in range(3):
        y = 590 - k * 70
        w = 120 + k * 80
        c.arrow(cx - w, y - 20, cx - 40, 600, mix(BG, SPARK, b), 3, 12)
        c.arrow(cx + w, y - 20, cx + 40, 600, mix(BG, SPARK, b), 3, 12)
    c.arrow(cx, 700, cx, 920, mix(BG, SPARK, b), 6, 20)
    c.text(cx + 80, 820, '全部收到柱子上', 'bold', 26, mix(BG, SPARK, b), 'lm')
    d = fade(t, 13, 14)
    c.rect(1440, 300, 1880, 620, fill=mix(BG, SHEET, d), r=12)
    c.text(1465, 350, '斗：方形的木块，像量米的斗', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1465, 410, '拱：弓形的横木，一层比一层长', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1465, 470, '全靠榫卯插接，不用钉子', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1465, 540, '接 B7 榫卯', 'bold', 24, mix(BG, GREEN, d), 'lm')
    caps(c, t, [(0, 6, '屋檐伸得很远，下面没有柱子：重量靠什么撑着？'),
                (6.2, 13, '斗拱一层层往外伸，像倒过来的金字塔，把屋檐的重量一点点收回来'),
                (13.2, 22, '最后全部落在柱子上。斗和拱之间全靠榫卯插接，没有一根钉子')], y=1010)

def b47_shake(c, t, i):
    corner_tag(c, 'B47 · 能滑才抗震')
    c.text(60, 96, '同样的积木塔：一座粘死，一座层间能滑', 'serif', 40, INK)
    shake = 30 * math.sin(t * 7) * fade(t, 2, 3)
    for k, (nm, rigid) in enumerate([('层间粘死', True), ('层间能滑（像斗拱）', False)]):
        x0 = 520 + k * 880
        c.rect(x0 - 300 + shake, 880, x0 + 300 + shake, 910, fill=MUTED, r=4)
        c.text(x0, 960, nm, 'bold', 28, INK, 'mm')
        fall = fade(t, 9, 12) if rigid else 0
        ang = fall * 1.3
        px_, py_ = x0 + 110 + shake, 880
        for j in range(6):
            y = 860 - j * 90
            if rigid:
                off = shake * (1 + j * 0.15) * (1 - fall)
                corners = [(x0 - 110 + off, y - 80), (x0 + 110 + off, y - 80), (x0 + 110 + off, y), (x0 - 110 + off, y)]
                rc = [(px_ + (x - px_) * math.cos(ang) - (y_ - py_) * math.sin(ang), py_ + (x - px_) * math.sin(ang) + (y_ - py_) * math.cos(ang)) for x, y_ in corners]
                c.poly(rc, (150, 120, 90))
                c.line(rc + [rc[0]], BG, 3)
            else:
                ox = x0 + shake * max(0.0, 1 - j * 0.3)
                c.rect(ox - 110, y - 80, ox + 110, y, fill=WOODC, outline=BG, width=3, r=4)
    a = fade(t, 13, 14)
    c.text(960, 220, '能滑的那一座：每一层都在「蹭」掉一点震动的能量（以实测为准）', 'sans', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 7, '地震来了，地面左右晃：粘死的塔整个跟着晃，越往上晃得越厉害'),
                (7.2, 13, '晃过头，就整座倒下'),
                (13.2, 22, '层间能滑的塔，每一层都在摩擦、转动，把震动一点点消耗掉：上面反而晃得小。应县木塔挺过多次地震，斗拱功不可没（拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- B48 腌菜
def b48_osmosis(c, t, i):
    corner_tag(c, 'B48 · 水往咸的地方跑')
    c.text(60, 96, '细胞壁像一张筛子：水能过，盐过得慢', 'serif', 40, INK)
    cx, cy = 760, 560
    shrink = fade(t, 5, 14)
    w = 320 - 90 * shrink
    c.rect(cx - 360, cy - 300, cx + 360, cy + 300, outline=MUTED, width=4, r=24)
    c.rect(cx - w, cy - 220 + 40 * shrink, cx + w, cy + 220 - 40 * shrink, fill=mix(BG, CUKE, 0.5), outline=CUKE, width=4, r=40)
    c.text(cx, cy, '黄瓜细胞', 'bold', 28, INK, 'mm')
    rnd = random.Random(3)
    a = fade(t, 2, 3)
    for k in range(26):
        x = cx - 340 + rnd.random() * 680
        y = cy - 280 + rnd.random() * 560
        if abs(x - cx) < w + 10 and abs(y - cy) < 230: continue
        c.rect(x - 6, y - 6, x + 6, y + 6, fill=mix(BG, SALT, a))
    b = fade(t, 5, 6)
    for k in range(5):
        y = cy - 160 + k * 80
        off = ((t * 60 + k * 23) % 80)
        c.arrow(cx + w - 40 + off, y, cx + w + 20 + off, y, mix(BG, WATERC, b), 4, 14)
        c.arrow(cx - w + 40 - off, y, cx - w - 20 - off, y, mix(BG, WATERC, b), 4, 14)
    d = fade(t, 12, 13)
    c.text(1440, 360, '外面：盐多、水少', 'bold', 28, mix(BG, INK, d), 'mm')
    c.text(1440, 420, '里面：盐少、水多', 'bold', 28, mix(BG, INK, d), 'mm')
    c.text(1440, 500, '水从稀的一边往浓的一边走', 'sans', 26, mix(BG, WATERC, d), 'mm')
    c.text(1440, 560, '这叫渗透', 'bold', 30, mix(BG, WATERC, d), 'mm')
    caps(c, t, [(0, 5, '黄瓜片撒上盐，过一会儿就出了一碗水，菜也软了'),
                (5.2, 12, '细胞壁和细胞膜像筛子：水分子很容易过去，盐过得慢'),
                (12.2, 22, '外面盐浓、水少，里面的水就往外跑：这叫渗透，称一称就知道少了多少（以实测为准）')], y=1010)

def b48_activity(c, t, i):
    corner_tag(c, 'B48 · 让细菌没水可用')
    c.text(60, 96, '盐不是把细菌「毒死」，是把水抢走', 'serif', 40, INK)
    rows = [('不加盐', 1.0, GREEN, '细菌有水，长得飞快'), ('淡盐', 0.6, SPARK, '长得慢一些'), ('浓盐', 0.2, NRED, '细菌自己的水也被吸走：长不起来')]
    for k, (nm, wv, col, note) in enumerate(rows):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        y = 300 + k * 200
        c.text(160, y, nm, 'bold', 30, mix(BG, INK, a), 'lm')
        c.rect(420, y - 30, 420 + 700 * wv * fade(t, 1.5 + k * 4, 3 + k * 4), y + 30, fill=mix(BG, WATERC, a), r=6)
        c.text(420, y + 60, '能被细菌用的水（示意）', 'sans', 20, mix(BG, MUTED, a), 'lm')
        r = 18 + 14 * wv
        for j in range(int(1 + 5 * wv)):
            c.ellipse(1260 + j * 80, y, r, r * 0.7, fill=mix(BG, col, a))
        c.text(1260, y + 60, note, 'sans', 22, mix(BG, INK, a), 'lm')
    d = fade(t, 14, 15)
    c.rect(160, 860, 1760, 930, fill=mix(BG, SHEET, d), r=10)
    c.text(960, 895, '同一个道理：腌肉、蜜饯（糖）、晒干、风干。本集只称重量，不培养细菌，实验用菜不食用', 'sans', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 6, '细菌也是活的细胞：要长、要分裂，都离不开水'),
                (6.2, 13, '盐把水牢牢「拉住」，能被细菌用上的水就少了：这叫水分活度'),
                (13.2, 22, '浓盐里，细菌自己的水也被吸走，长不起来。糖渍、晒干，都是同一个道理')], y=1010)

CLIPS = {
 'B46_压实': (b46_compact, 22), 'B46_含水量': (b46_water, 22),
 'B46_片头': (titles.opening(BSER, VOL14, SB14, 6, '商代 · 郑州商城的夯土城墙'), 7),
 'B46_片尾': (titles.closing(BSER, VOL14, SB14, 6, '下集：不用一根钉子的木塔，为什么九百多年不倒？'), 7),
 'B47_传力': (b47_load, 22), 'B47_晃动': (b47_shake, 22),
 'B47_片头': (titles.opening(BSER, VOL14, SB14, 7, '辽 · 1056 年 · 应县木塔'), 7),
 'B47_片尾': (titles.closing(BSER, VOL14, SB14, 7, '下集：撒一把盐，菜为什么就不容易坏？'), 7),
 'B48_渗透': (b48_osmosis, 22), 'B48_水分活度': (b48_activity, 22),
 'B48_片头': (titles.opening(BSER, VOL14, SB14, 8, '北魏 · 贾思勰《齐民要术》'), 7),
 'B48_片尾': (titles.closing(BSER, VOL14, SB14, 8, '下集：一千多年前的粮仓，怎么让粮食放几十年？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
