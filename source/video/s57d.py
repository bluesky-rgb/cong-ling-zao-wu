"""第五十七季（第二十五层：露营）收尾：E301 荧光棒 + 第五十七季特辑依赖图。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s57a import S57A, SER57, VOL57, WARM, COOL

GLOW = (140, 240, 120)


def stick(c, cx, cy, br, label):
    c.rect(cx - 26, cy - 200, cx + 26, cy + 200, fill=mix(BG, GLOW, 0.15 + 0.8 * br), outline=MUTED, width=3, r=26)
    if br > 0.05:
        for k in range(3):
            c.rect(cx - 26 - 14 * (k + 1), cy - 200 - 14 * (k + 1), cx + 26 + 14 * (k + 1), cy + 200 + 14 * (k + 1),
                   outline=mix(BG, GLOW, br * 0.25 / (k + 1)), width=10, r=40)
    c.text(cx, cy + 260, label, 'bold', 28, INK, 'mm')


def e301_mix(c, t, i):
    corner_tag(c, '第 301 集 · 两种液体一混就发光')
    c.text(60, 96, '荧光棒里有一根细细的玻璃小管把两种液体隔开；一折，小管破了，两种液体混在一起起化学反应，能量直接变成光', 'serif', 36, INK)
    cx, cy = 960, 560
    bent = t > 6
    mixk = 0 if t < 6 else min(1.0, (t - 6) / 5)
    c.rect(cx - 60, cy - 320, cx + 60, cy + 320, fill=mix(BG, mix((150, 200, 230), GLOW, mixk), 0.35 + 0.6 * mixk), outline=MUTED, width=4, r=50)
    if not bent:
        c.rect(cx - 22, cy - 260, cx + 22, cy + 260, fill=mix(BG, (230, 200, 120), 0.6), outline=MUTED, width=2, r=20)
        c.text(cx + 120, cy - 200, '外层液体', 'sans', 26, MUTED, 'lm')
        c.text(cx + 120, cy, '玻璃小管里的另一种液体', 'sans', 26, MUTED, 'lm')
    else:
        random.seed(2)
        for k in range(10 if mixk < 0.5 else 0):
            x = cx + random.uniform(-20, 20); y = cy + random.uniform(-240, 240)
            c.poly([(x - 10, y), (x, y - 14), (x + 12, y + 4)], mix(BG, (230, 230, 230), 0.4 * (1 - mixk)))
        if mixk > 0.3:
            for k in range(3):
                c.rect(cx - 60 - 16 * (k + 1), cy - 320 - 16 * (k + 1), cx + 60 + 16 * (k + 1), cy + 320 + 16 * (k + 1),
                       outline=mix(BG, GLOW, mixk * 0.3 / (k + 1)), width=12, r=60)
        c.text(cx + 260, cy - 200, '一折：小管破了', 'bold', 28, SPARK, 'mm')
        if mixk > 0.6:
            c.text(cx + 300, cy + 120, '混合 → 化学反应 → 光', 'bold', 30, GREEN, 'lm')
    caps(c, t, [(0, 7, '荧光棒里：外面一种液体，玻璃小管里装着另一种'),
                (7.2, 14, '一折一摇，小管破了，两种液体混在一起'),
                (14.2, 22, '化学反应把能量直接变成光，不发热也能亮（由大人折，绝不剪开）')], y=1010)


def e301_temp(c, t, i):
    corner_tag(c, '第 301 集 · 越热越亮，越冷越久')
    c.text(60, 96, '温度高，反应跑得快：一下子很亮，但很快就用完；温度低，反应慢：光暗暗的，却能亮更久', 'serif', 36, INK)
    hrs = min(6.0, t / 20 * 6)
    data = [('温水（≤50 ℃）', 1.0, 1.4), ('室温', 0.65, 3.5), ('冰水', 0.3, 9.0)]
    for j, (lab, b0, life) in enumerate(data):
        cx = 480 + j * 480
        br = b0 * max(0.0, 1 - hrs / life)
        stick(c, cx, 500, br, lab)
    c.text(960, 900, f'折亮后过了 {hrs:.1f} 小时（示意，以实测为准）', 'sans', 26, MUTED, 'mm')
    caps(c, t, [(0, 7, '三根一样的荧光棒同时折亮：温水里最亮，冰水里最暗'),
                (7.2, 14, '一两个小时后，温水里那根已经暗下去'),
                (14.2, 22, '冰水里那根还在慢慢地亮：反应慢，用得也慢')], y=1010)


OLD57 = [('复合材料', '150'), ('悬索桥', '79'), ('砂纸', '230'), ('杠杆与滑轮组', '39'), ('保温杯', '147'), ('毛巾', '256'),
         ('铝', '145'), ('红外测温枪', '200'), ('橡胶轮胎', '143'), ('气垫船', '179'), ('千斤顶', '227'), ('老虎钳', '226'),
         ('自动铅笔', '216'), ('动力绳', '207'), ('透镜', '52'), ('投影仪', '184'), ('夜光表盘', '187'), ('速冻', '197')]
NEW57 = [('帐篷', '292', ['复合材料', '悬索桥']), ('地钉', '293', ['砂纸', '杠杆与滑轮组']), ('睡袋', '294', ['保温杯', '毛巾']),
         ('保温毯', '295', ['铝', '红外测温枪']), ('充气垫', '296', ['橡胶轮胎', '气垫船']), ('折叠椅', '297', ['千斤顶', '杠杆与滑轮组']),
         ('登山杖', '298', ['老虎钳', '自动铅笔']), ('吊床', '299', ['悬索桥', '动力绳']), ('头灯', '300', ['透镜', '投影仪']),
         ('荧光棒', '301', ['夜光表盘', '速冻'])]


def s57_layer(c, t, i):
    corner_tag(c, '第五十七季特辑 · 第二十五层')
    c.text(60, 118, '第二十五层：露营', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD57):
        pos[name] = (340, 216 + k * 37)
    for k, (name, num, deps) in enumerate(NEW57):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 178, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十七季新长出', 'sans', 24, MUTED, 'mm')
    newn = dict((n, 1) for n, _, _ in NEW57)
    for k, (name, num, deps) in enumerate(NEW57):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in newn:
                sx, ex = x0 - 110, x1 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
                pts[-1] = (ex, y1)
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD57:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW57):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第二十五层的十集：露营用的东西'),
                (8.2, 16, '复合材料和悬索桥长出帐篷，杠杆长出地钉，保温杯和毛巾长出睡袋，铝长出保温毯，气垫船长出充气垫'),
                (16.2, 24, '千斤顶长出折叠椅，老虎钳长出登山杖，悬索桥和动力绳长出吊床，透镜和投影仪长出头灯'),
                (24.2, 30, '最后，夜光表盘和速冻一起，长出了荧光棒')], y=1040)


CLIPS = {
 'E301_混合': (e301_mix, 22), 'E301_温度': (e301_temp, 22),
 'E301_片头': (titles.opening(SER57, VOL57, S57A, 9, '一折就亮的荧光棒'), 7),
 'E301_片尾': (titles.closing(SER57, VOL57, S57A, 9, '下集：第五十七季特辑 · 第二十五层回顾'), 7),
 'S57_第二十五层': (s57_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
