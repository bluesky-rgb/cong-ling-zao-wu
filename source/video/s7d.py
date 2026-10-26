"""第七季收尾：E51 青霉素、第七季特辑（全系列回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s7a import S7A, SER7, VOL7

AGAR = (205, 180, 120)
BACT = (230, 220, 190)
MOLD = (90, 160, 120)
PEN = (240, 160, 60)

# ---------------------------------------------------------------- E51 青霉素
def e51_zone(c, t, i):
    corner_tag(c, '第 51 集 · 抑菌圈')
    c.text(60, 96, '霉菌旁边，细菌为什么长不起来？', 'serif', 40, INK)
    cx, cy, R = 620, 560, 330
    c.ellipse(cx, cy, R + 12, R + 12, outline=(200, 205, 210), width=5)
    c.ellipse(cx, cy, R, R, fill=mix(BG, AGAR, 0.35))
    mx, my = cx + 60, cy - 40
    lawn = fade(t, 0.5, 4)
    zone = 160 * ease(fade(t, 6, 13))
    rnd = random.Random(51)
    for k in range(900):
        a_ = rnd.uniform(0, 2 * math.pi); r = R * math.sqrt(rnd.random()) * 0.97
        x, y = cx + r * math.cos(a_), cy + r * math.sin(a_)
        d = math.hypot(x - mx, y - my)
        if d < zone: continue
        if rnd.random() > lawn: continue
        c.ellipse(x, y, 4, 4, fill=mix(BG, BACT, 0.8))
    m = fade(t, 4, 7)
    if m > 0:
        rm = 30 + 60 * m
        for k in range(40):
            a_ = k * 2 * math.pi / 40
            rr = rm * (0.7 + 0.3 * math.sin(k * 3.1))
            c.line([(mx, my), (mx + rr * math.cos(a_), my + rr * math.sin(a_))], mix(BG, MOLD, m), 4)
        c.ellipse(mx, my, rm * 0.55, rm * 0.55, fill=mix(BG, MOLD, m))
    if zone > 20:
        c.ellipse(mx, my, zone, zone, outline=mix(BG, SPARK, 0.8), width=3)
        c.arrow(mx + zone + 160, my - 200, mx + zone * 0.75, my - zone * 0.6, SPARK, 4, 14)
        c.text(mx + zone + 170, my - 215, '抑菌圈：细菌长不起来', 'bold', 26, SPARK, 'lm')
    a = fade(t, 1, 2)
    c.text(1080, 540, '· 米黄色的点：细菌（铺满一层）', 'sans', 26, mix(BG, INK, a), 'lm')
    b = fade(t, 4.5, 5.5)
    c.text(1080, 590, '· 绿色：青霉', 'sans', 26, mix(BG, MOLD, b), 'lm')
    d = fade(t, 14, 15)
    c.rect(1080, 660, 1860, 920, fill=mix(BG, SHEET, d), r=14)
    c.text(1110, 710, '1928 年，弗莱明在一只被霉菌污染的', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1110, 760, '培养皿里看到了这个圈', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1110, 830, '霉菌分泌了一种东西，向四周扩散：', 'sans', 26, mix(BG, INK, d), 'lm')
    c.text(1110, 880, '他叫它「青霉素」', 'bold', 30, mix(BG, SPARK, d), 'lm')
    caps(c, t, [(0, 4, '培养皿里铺满了一层细菌'),
                (4.2, 13, '角落里长出一团青霉：它周围一圈，细菌越来越少，最后一片干净'),
                (13.2, 22, '霉菌往外放出了一种能挡住细菌的东西。这一幕，只能在实验室里拍')], y=1010)

def e51_wall(c, t, i):
    corner_tag(c, '第 51 集 · 细胞壁')
    c.text(60, 96, '青霉素杀细菌，为什么不伤人？', 'serif', 40, INK)
    cx, cy = 560, 540
    W, H = 330, 170
    inj = fade(t, 4, 8)          # penicillin arriving
    burst = fade(t, 10, 12)
    # inner membrane (bulging when wall weakens)
    bulge = 1 + 0.25 * burst
    if burst < 1:
        c.ellipse(cx, cy, (W - 30) * bulge, (H - 30) * bulge, fill=mix(BG, (120, 170, 150), 0.6 * (1 - burst)))
    # wall bricks around an ellipse
    n = 36
    for k in range(n):
        a_ = k * 2 * math.pi / n
        x, y = cx + W * math.cos(a_), cy + H * math.sin(a_)
        gap = burst > 0 and k % 3 == 0
        if gap and burst > 0.3: continue
        off = 1 + 0.5 * burst if (k % 3 == 0) else 1
        c.ellipse(cx + W * off * math.cos(a_), cy + H * off * math.sin(a_), 18, 18, fill=mix(BG, (200, 160, 110), 1 - 0.6 * burst))
    if burst > 0.5:
        rnd = random.Random(2)
        for k in range(30):
            a_ = rnd.uniform(0, 2 * math.pi); r = (W + 80 * burst) * rnd.uniform(0.6, 1.1)
            c.ellipse(cx + r * math.cos(a_), cy + r * math.sin(a_) * H / W, 6, 6, fill=mix(BG, (120, 170, 150), 1 - burst * 0.5))
        c.text(cx, cy, '撑破了', 'bold', 34, NRED, 'mm')
    else:
        c.text(cx, cy, '细菌', 'bold', 30, INK, 'mm')
    # penicillin molecules
    if inj > 0:
        for k in range(10):
            a_ = k * 2 * math.pi / 10 + 0.3
            r = W + 220 - 200 * inj
            x, y = cx + r * math.cos(a_), cy + r * H / W * math.sin(a_)
            c.poly([(x, y - 14), (x + 13, y + 9), (x - 13, y + 9)], PEN)
    a = fade(t, 1, 2)
    c.text(cx, cy + H + 90, '细菌外面有一层「细胞壁」：像砌墙，要不停地修补', 'sans', 24, mix(BG, INK, a), 'mm')
    c.text(cx, cy + H + 130, '青霉素（橙色）卡住砌墙的「工人」：墙越来越薄，被里面的压力撑破', 'sans', 24, mix(BG, PEN, inj), 'mm')
    for k, (title, line1, line2, col) in enumerate([('人的细胞', '没有细胞壁', '→ 青霉素「无墙可拆」', GREEN), ('病毒', '没有细胞壁、也不自己造', '→ 青霉素没用！感冒流感不能靠它', NRED)]):
        b = fade(t, 13 + k * 3, 14 + k * 3)
        y0 = 300 + k * 290
        c.rect(1180, y0, 1860, y0 + 230, fill=mix(BG, SHEET, b), r=14)
        c.text(1210, y0 + 50, title, 'bold', 32, mix(BG, col, b), 'lm')
        c.text(1210, y0 + 115, line1, 'sans', 28, mix(BG, INK, b), 'lm')
        c.text(1210, y0 + 170, line2, 'bold', 28, mix(BG, col, b), 'lm')
    caps(c, t, [(0, 4, '细菌外面裹着一层细胞壁，要一边长、一边不停地修补'),
                (4.2, 12, '青霉素卡住了修墙的那一步：墙越来越薄，最后被细菌自己的内压撑破'),
                (12.2, 16, '人的细胞没有这层墙，所以青霉素专挑细菌下手'),
                (16.2, 22, '病毒也没有细胞壁：感冒、流感，抗生素没用。用不用药，一定听医生的')], y=1010)

# ---------------------------------------------------------------- 第七季特辑 · 全系列回顾
TREE = [
 ('一 · 电', ['01 摩擦起电', '02 伏打电堆', '03 电生磁', '04 磁生电', '05 手摇发电机']),
 ('二 · 能量从哪来', ['水车', '风车', '畜力与人力', '重力', '蒸汽', '化学电', '热电', '压电', '静电机']),
 ('三 · 火与材料', ['生火', '木炭与制陶', '炼铜', '炼铁', '煤与焦炭', '制盐', '玻璃', '肥皂', '纸', '石灰与水泥']),
 ('四 · 水与农业', ['螺旋提水', '虹吸', '陶罐滴灌', '水车提水', '轮作固氮', '选种与嫁接']),
 ('五 · 救命的知识', ['口服补液', '洗手', '防坏血病', '净水', '种痘', '煤气中毒', '罐藏', '蒸发冷却罐', '青霉素']),
 ('六 · 机械与交通', ['杠杆与滑轮组', '曲柄连杆', '齿轮与轴承', '马轭', '逆风航行', '热气球']),
 ('七 · 信息与测量', ['摆钟', '温度计', '用影子测地球', '数字与 0', '复式记账', '光学电报']),
 ('八 · 古法解密', ['指南鱼', '卓筒井', '活字印刷', '水排', '都江堰', '赵州桥', '榫卯', '被中香炉', '鱼洗', '透光镜',
                  '一钟双音', '冰鉴', '漏刻', '豆腐点卤', '酿酒与酿醋', '瓷器', '指南车', '地动仪', '银钗验毒']),
]

def s7_tree(c, t, i):
    corner_tag(c, '第七季特辑 · 全系列回顾')
    c.text(60, 110, '从零造物：八卷科技树，全部点亮', 'serif', 46, INK, 'lm')
    x0, x1 = 360, 1860
    y0, dy = 190, 84
    cnt = 0
    rows = []
    for vi, (vol, eps) in enumerate(TREE):
        if len(eps) > 10:
            rows.append((vol, eps[:10], vi, 0)); rows.append(('', eps[10:], vi, 1))
        else:
            rows.append((vol, eps, vi, 0))
    for r, (vol, eps, vi, sub) in enumerate(rows):
        y = y0 + r * dy
        st = 1.5 + min(r, 7) * 2.2 + (1.0 if sub else 0)
        a = fade(t, st - 1, st)
        accent = FIELD if vi == 7 else COPPER
        if vol: c.text(x0 - 30, y + 26, vol, 'bold', 26, mix(BG, accent, a), 'rm')
        n = len(eps)
        w = (x1 - x0) / max(n, 9 if vi == 7 else n)
        fs = int(min(22, w / 5.6))
        for k, name in enumerate(eps):
            lit = fade(t, st + k * 1.6 / n, st + k * 1.6 / n + 0.4)
            bx = x0 + k * w
            c.rect(bx + 3, y, bx + w - 3, y + 52, fill=mix(BG, mix(SHEET, accent, 0.35), lit), outline=mix(LINE, accent, lit), width=2, r=8)
            c.text(bx + w / 2, y + 26, name, 'sans', fs, mix(MUTED, INK, lit), 'mm')
            if lit > 0.5: cnt += 1
    c.text(1860, 110, f'已点亮 {cnt} / 70', 'mono', 30, SPARK, 'rm')
    caps(c, t, [(0, 6, '七季，八卷，七十个选题'),
                (6.2, 14, '从一块琥珀起电，到发电机；从生火、炼铁，到玻璃；从洗手、种痘，到青霉素'),
                (14.2, 22, '古人已经做到的十九件事，我们用今天的原理一件件拆开'),
                (22.2, 30, '每一个节点，都是「为什么」的答案，也是下一个「怎么做」的起点')], y=1035)

CLIPS = {
 'E51_抑菌圈': (e51_zone, 22), 'E51_细胞壁': (e51_wall, 22),
 'E51_片头': (titles.opening(SER7, VOL7, S7A, 9, '1928 年 · 伦敦 · 一只被污染的培养皿'), 7),
 'E51_片尾': (titles.closing(SER7, VOL7, S7A, 9, '下集：第七季特辑 · 全系列回顾'), 7),
 'S7_科技树': (s7_tree, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
