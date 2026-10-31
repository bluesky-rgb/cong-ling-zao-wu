"""第八季收尾：E61 蓄电池、第八季特辑（第二层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s8a import S8A, SER8, VOL8

PB = (120, 125, 135)
PBO2 = (110, 70, 50)
SULF = (220, 220, 225)
ACID = (90, 140, 190)

# ---------------------------------------------------------------- E61 蓄电池
def e61_reverse(c, t, i):
    corner_tag(c, '第 61 集 · 能来回的反应')
    c.text(60, 96, '一次性电池和充电电池，差在哪里？', 'serif', 40, INK)
    # phases: 0-9 discharge, 9-11 pause, 11-20 charge
    dis = fade(t, 1, 9)
    chg = fade(t, 11, 19)
    state = dis * (1 - chg)          # 0 = full, 1 = empty
    cx, cy = 640, 560
    c.rect(cx - 330, cy - 220, cx + 330, cy + 260, outline=MUTED, width=5, r=12)
    c.rect(cx - 324, cy - 160, cx + 324, cy + 254, fill=mix(BG, ACID, 0.35 * (1 - 0.6 * state)), r=10)
    # left plate: Pb -> PbSO4 ; right plate: PbO2 -> PbSO4
    c.rect(cx - 220, cy - 260, cx - 160, cy + 200, fill=mix(PB, SULF, state), r=4)
    c.rect(cx + 160, cy - 260, cx + 220, cy + 200, fill=mix(PBO2, SULF, state), r=4)
    c.text(cx - 190, cy + 230, '铅', 'bold', 24, INK, 'mm')
    c.text(cx + 190, cy + 230, '二氧化铅', 'bold', 24, INK, 'mm')
    charging = t > 10.5
    lx = cx
    c.line([(cx - 190, cy - 260), (cx - 190, cy - 340), (cx + 190, cy - 340), (cx + 190, cy - 260)], COPPER, 5)
    if not charging:
        on = 1 - state * 0.8
        c.ellipse(lx, cy - 340, 34, 34, fill=mix(BG, SPARK, on))
        c.text(lx + 50, cy - 340, '灯（放电）', 'bold', 26, SPARK, 'lm')
        sign = 1
    else:
        c.rect(lx - 70, cy - 370, lx + 70, cy - 310, fill=SHEET, outline=GREEN, width=3, r=8)
        c.text(lx, cy - 340, '充电器', 'bold', 24, GREEN, 'mm')
        sign = -1
    if 1 < t < 9 or 11 < t < 19:
        for k in range(8):
            d = ((t * 160 + k * 95) % 760) / 760
            pts = [(cx - 190, cy - 260), (cx - 190, cy - 340), (cx + 190, cy - 340), (cx + 190, cy - 260)]
            if sign < 0: d = 1 - d
            L = [80, 380, 80]; tot = 540; s_ = d * tot
            for j in range(3):
                if s_ <= L[j]:
                    f = s_ / L[j]
                    x = pts[j][0] + (pts[j + 1][0] - pts[j][0]) * f
                    y = pts[j][1] + (pts[j + 1][1] - pts[j][1]) * f
                    c.ellipse(x, y, 7, 7, fill=FIELD); break
                s_ -= L[j]
    pct = (1 - state) * 100
    c.text(cx, cy + 320, f'电量约 {pct:.0f}%', 'mono', 30, INK, 'mm')
    a = fade(t, 2, 3)
    c.rect(1120, 220, 1860, 860, fill=mix(BG, SHEET, a), r=14)
    c.text(1150, 270, '放电：两块极板都慢慢变成', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1150, 315, '白色的硫酸铅，电流流过灯', 'sans', 26, mix(BG, INK, a), 'lm')
    b = fade(t, 11, 12)
    c.text(1150, 400, '充电：外面的电源把电子「推回去」', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1150, 445, '硫酸铅又变回铅和二氧化铅', 'sans', 26, mix(BG, INK, b), 'lm')
    d = fade(t, 17, 18)
    c.text(1150, 540, '能来回进行的反应 = 蓄电池', 'bold', 30, mix(BG, SPARK, d), 'lm')
    c.text(1150, 600, '第 02 集的铁铜电堆：', 'sans', 24, mix(BG, MUTED, d), 'lm')
    c.text(1150, 640, '铁溶解了就回不去，只能用一次', 'sans', 24, mix(BG, MUTED, d), 'lm')
    c.text(1150, 720, '1859 年普兰特：铅酸蓄电池', 'sans', 24, mix(BG, MUTED, d), 'lm')
    c.text(1150, 760, '（铅有毒：只看动画，不自己做）', 'sans', 22, mix(BG, NRED, d), 'lm')
    caps(c, t, [(0, 9, '放电：铅和二氧化铅慢慢变成硫酸铅，电子从一边流过灯泡到另一边'),
                (9.2, 17, '充电：外面的电源把电子推回去，硫酸铅又变回原来的样子'),
                (17.2, 22, '能来回进行的化学反应，就是蓄电池：白天存，晚上用')], y=1010)

DENS = [('举高的重物（第 09 集）', 0.0027, MUTED, '举高 1 米：每千克约 0.003 瓦时'), ('铅酸电池', 35, PB, '约 30–40 瓦时/千克'), ('镍氢电池', 80, FIELD, '约 60–120'), ('锂离子电池', 200, GREEN, '约 150–250'), ('汽油（化学能）', 12000, NRED, '约 12000，但只有一部分能变成功')]

def e61_density(c, t, i):
    corner_tag(c, '第 61 集 · 一千克能存多少电')
    c.text(60, 96, '同样一千克，谁存的能量最多？', 'serif', 40, INK)
    x0, x1 = 560, 1700
    def X(v):  # log scale 0.001 .. 100000
        return x0 + (x1 - x0) * (math.log10(v) + 3) / 8
    for p in range(-3, 6):
        x = X(10 ** p)
        c.line([(x, 220), (x, 800)], LINE, 1)
        c.text(x, 830, f'{10 ** p:g}' if p >= 0 else f'0.{"0" * (-p - 1)}1', 'mono', 18, MUTED, 'mm')
    c.text(1130, 870, '每千克储存的能量（瓦时，对数刻度：每一格多 10 倍）', 'sans', 22, MUTED, 'mm')
    for k, (name, v, col, note) in enumerate(DENS):
        a = fade(t, 1 + k * 2.6, 2 + k * 2.6)
        if a <= 0: continue
        y = 270 + k * 110
        c.text(530, y, name, 'bold', 26, mix(BG, INK, a), 'rm')
        c.rect(x0, y - 22, x0 + (X(v) - x0) * ease(a), y + 22, fill=mix(BG, col, 0.85), r=8)
        c.text(X(v) + 14 if X(v) < 1500 else X(v) - 14, y, note, 'sans', 22, mix(BG, INK, a), 'lm' if X(v) < 1500 else 'rm')
    caps(c, t, [(0, 4, '第 09 集：把 10 千克举高 2 米，只存下约 200 焦耳'),
                (4.2, 12, '一千克的电池，能存几十到几百瓦时：比举高的重物多成千上万倍'),
                (12.2, 22, '一节五号充电电池约 2.4 瓦时，相当于把 10 千克举到约 88 米高（数字为量级）')], y=1010)

# ---------------------------------------------------------------- 第八季特辑：第二层
OLD = [('玻璃', '21'), ('透光镜', 'B10'), ('影子', '47'), ('洗手', '32'), ('青霉素', '51'), ('电生磁', '03'),
       ('光学电报', '50'), ('手摇发电机', '05'), ('伏打电堆', '02'), ('炼铜', '17'), ('水车发电', '06'), ('重力发电', '09')]
NEW = [('透镜', '52', ['玻璃', '透光镜']), ('显微镜', '53', ['透镜', '洗手', '青霉素']), ('望远镜', '54', ['透镜']),
       ('照相', '55', ['透镜', '影子']), ('电磁铁', '56', ['电生磁']), ('电报', '57', ['电磁铁', '光学电报']),
       ('电动机', '58', ['手摇发电机', '电磁铁']), ('电镀', '59', ['伏打电堆', '炼铜']), ('电灯', '60', ['手摇发电机', '水车发电', '玻璃']),
       ('蓄电池', '61', ['伏打电堆', '重力发电'])]

def s8_layer(c, t, i):
    corner_tag(c, '第八季特辑 · 第二层')
    c.text(60, 110, '第二层：每一集，都长在旧的节点上', 'serif', 46, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD):
        pos[name] = (340, 225 + k * 64)
    for k, (name, num, deps) in enumerate(NEW):
        pos[name] = (1150 + (180 if name in ('显微镜', '望远镜', '照相', '电报', '电动机') else 0), 240 + k * 72)
    c.text(340, 172, '前七季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1240, 195, '第八季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx = x0 + 110
            ex = x1 - 100
            col = mix(BG, FIELD if d in dict((n, 1) for n, _ in OLD) else COPPER, a * 0.8)
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, col, 2)
    for name, num in OLD:
        x, y = pos[name]
        c.rect(x - 110, y - 24, x + 110, y + 24, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, MUTED, 'lm')
        c.text(x + 14, y, name, 'sans', 22, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 100, y - 26, x + 100, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 86, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 14, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第八季的十集，没有一集是从零开始的'),
                (8.2, 16, '透镜长在玻璃上，显微镜又长在透镜上，最后看见了第 32 集洗掉的那些细菌'),
                (16.2, 24, '电磁铁、电报、电动机、电镀、电灯、蓄电池：都从第一卷的那一点电长出来'),
                (24.2, 30, '知识会复利：点亮的节点越多，下一个就越容易')], y=1035)

CLIPS = {
 'E61_来回': (e61_reverse, 22), 'E61_能量密度': (e61_density, 22),
 'E61_片头': (titles.opening(SER8, VOL8, S8A, 9, '穿越北宋 · 只用动画：把白天的电留到晚上'), 7),
 'E61_片尾': (titles.closing(SER8, VOL8, S8A, 9, '下集：第八季特辑 · 第二层'), 7),
 'S8_第二层': (s8_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
