"""第十七季（第五层：口袋里的科技）第一批：E92 晶体管、E93 微波炉、E94 激光 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S17A = [('92', '晶体管'), ('93', '微波炉'), ('94', '激光'), ('95', '数码相机'), ('96', '触摸屏'),
        ('97', '二维码'), ('98', '互联网'), ('99', '磁悬浮'), ('100', '直升机'), ('101', '人造卫星')]
SER17, VOL17 = '从零造物', '第十七季 · 第五层：口袋里的科技'
NTYPE = (90, 150, 220)
PTYPE = (220, 120, 90)
LASER = (240, 70, 60)
CHOC = (110, 70, 45)

# ---------------------------------------------------------------- E92 晶体管
def e92_amp(c, t, i):
    corner_tag(c, '第 92 集 · 小电流管大电流')
    c.text(60, 96, '手指只漏过一丝电流，LED 却被点亮了', 'serif', 40, INK)
    # schematic
    x0, y0 = 300, 300
    c.rect(x0 - 40, y0 + 160, x0 + 40, y0 + 300, outline=INK, width=4)
    c.text(x0, y0 + 230, '3V', 'mono', 28, INK, 'mm')
    c.line([(x0, y0 + 160), (x0, y0), (900, y0)], COPPER, 4)
    c.ellipse(900, y0 + 70, 34, 34, fill=SPARK if t > 6 else (70, 70, 70), outline=MUTED, width=2)
    c.text(960, y0 + 70, 'LED', 'bold', 24, INK, 'lm')
    c.line([(900, y0), (900, y0 + 36)], COPPER, 4)
    c.line([(900, y0 + 104), (900, y0 + 200)], COPPER, 4)
    # transistor
    tx, ty = 900, y0 + 260
    c.ellipse(tx, ty, 60, 60, outline=INK, width=4)
    c.line([(tx - 20, ty - 40), (tx - 20, ty + 40)], INK, 6)
    c.line([(tx - 20, ty - 15), (tx + 30, ty - 50)], INK, 4)
    c.line([(tx - 20, ty + 15), (tx + 30, ty + 50)], INK, 4)
    c.line([(tx + 30, ty - 50), (900, y0 + 200)], COPPER, 4)
    c.line([(tx + 30, ty + 50), (900, y0 + 420), (x0, y0 + 420), (x0, y0 + 300)], COPPER, 4)
    c.line([(tx - 20, ty), (650, ty)], COPPER, 4)
    c.text(620, ty, '基极', 'sans', 22, MUTED, 'rm')
    # finger
    a = fade(t, 4, 5)
    c.ellipse(560, ty - 80, 50, 28, fill=mix(BG, (230, 190, 160), a))
    c.text(560, ty - 130, '手指碰两根线', 'sans', 22, mix(BG, INK, a), 'mm')
    b = fade(t, 7, 8)
    c.rect(1150, 280, 1840, 640, fill=mix(BG, SHEET, b), r=12)
    c.text(1180, 330, '手指里流过：约 0.01 毫安', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1180, 380, 'LED 里流过：约 1–10 毫安', 'sans', 26, mix(BG, INK, b), 'lm')
    c.rect(1180, 430, 1180 + 6, 470, fill=mix(BG, NRED, b))
    c.rect(1180, 500, 1180 + 600 * fade(t, 8, 11), 540, fill=mix(BG, GREEN, b))
    c.text(1180, 600, '小电流控制大电流：这就是放大（以实测为准）', 'bold', 24, mix(BG, GREEN, b), 'lm')
    caps(c, t, [(0, 6, '电池、LED 和一个三条腿的晶体管：LED 本来不亮'),
                (6.2, 13, '手指同时碰两根导线，一丝极小的电流经过手指流进晶体管的「基极」：LED 亮了'),
                (13.2, 22, '基极的小电流，打开了另外两条腿之间的大电流：像用一根手指拧开消防栓的阀门')], y=1010)

def e92_pn(c, t, i):
    corner_tag(c, '第 92 集 · 三明治一样的半导体')
    c.text(60, 96, 'N、P、N 三层：中间那层薄薄的门，由基极管着', 'serif', 40, INK)
    x0, y0, W, H = 260, 300, 1400, 360
    for k, (nm, col) in enumerate((('N', NTYPE), ('P', PTYPE), ('N', NTYPE))):
        w = [600, 200, 600][k]
        xs = x0 + [0, 600, 800][k]
        c.rect(xs, y0, xs + w, y0 + H, fill=mix(BG, col, 0.35), outline=col, width=3)
        c.text(xs + w / 2, y0 - 30, nm, 'bold', 34, col, 'mm')
    c.text(x0 + 300, y0 + H + 40, '发射极', 'sans', 24, MUTED, 'mm')
    c.text(x0 + 700, y0 + H + 40, '基极', 'sans', 24, MUTED, 'mm')
    c.text(x0 + 1100, y0 + H + 40, '集电极', 'sans', 24, MUTED, 'mm')
    on = t > 8
    rnd = random.Random(2)
    for j in range(30):
        yy = y0 + 30 + rnd.random() * (H - 60)
        sp = rnd.uniform(0.6, 1.2)
        if on:
            u = ((t * 0.25 * sp + rnd.random()) % 1)
            x = x0 + 40 + u * (W - 80)
        else:
            x = x0 + 40 + rnd.random() * 520
        c.ellipse(x, yy, 9, 9, fill=NTYPE)
    msg = '基极没电流：中间的 P 层像一道墙，电子过不去' if not on else '基极有一点电流：墙变薄了，大量电子冲过去'
    c.text(960, 820, msg, 'bold', 28, NRED if not on else GREEN, 'mm')
    caps(c, t, [(0, 8, '晶体管里是三层半导体：两边是 N 型，中间夹着一层很薄的 P 型'),
                (8.2, 15, '基极里送进一点点电流，中间那道「墙」就让开了，大量电子从一边冲到另一边'),
                (15.2, 22, '1947 年贝尔实验室做出了第一个晶体管：它取代了又大又烫的电子管，后来一块芯片上能放几百亿个')], y=1010)

# ---------------------------------------------------------------- E93 微波炉
def e93_standing(c, t, i):
    corner_tag(c, '第 93 集 · 来回反射，站住不动的波')
    c.text(60, 96, '微波在炉腔里来回撞：有的地方一直在猛晃，有的地方几乎不动', 'serif', 38, INK)
    x0, x1, yc = 200, 1720, 460
    c.rect(x0 - 20, yc - 230, x0, yc + 230, fill=MUTED)
    c.rect(x1, yc - 230, x1 + 20, yc + 230, fill=MUTED)
    L = x1 - x0
    lam = L / 3.5
    for k in range(3):
        pts = []
        ph = t * 6 + k * 0.8
        for q in range(301):
            x = x0 + L * q / 300
            v = math.sin(2 * math.pi * (x - x0) / lam * 1.0) * math.cos(ph)
            pts.append((x, yc - 160 * v))
        c.line(pts, mix(BG, (120, 170, 220), 0.4 + 0.3 * k), 3)
    a = fade(t, 6, 7)
    for k in range(7):
        x = x0 + lam / 4 + k * lam / 2
        if x > x1: break
        c.ellipse(x, yc + 300, 30, 30, fill=mix(BG, NRED, a))
    c.text(960, yc + 360, '红点：热点（晃得最厉害的地方），相隔半个波长', 'sans', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '微波从一侧射进炉腔，碰到金属壁反射回来，和后来的微波叠在一起'),
                (6.2, 13, '叠出来的波「站」在原地：有的地方一直猛烈晃动，有的地方几乎不动'),
                (13.2, 22, '晃得厉害的地方热，不动的地方冷：所以要转盘，让食物轮流经过热点')], y=1010)

def e93_speed(c, t, i):
    corner_tag(c, '第 93 集 · 用巧克力量光速')
    c.text(60, 96, '量出熔点的距离，乘 2，再乘频率', 'serif', 40, INK)
    c.rect(200, 280, 1100, 460, fill=CHOC, r=14)
    a = fade(t, 2, 4)
    for k in range(5):
        x = 300 + k * 180
        c.ellipse(x, 370, 40 * a, 30 * a, fill=(170, 120, 80))
    c.line([(300, 500), (480, 500)], SPARK, 4)
    c.text(390, 540, '约 6 厘米（以实测为准）', 'bold', 26, SPARK, 'mm')
    rows = [('相邻熔点距离', '≈ 6.1 厘米', '半个波长'), ('波长', '≈ 12.2 厘米', '× 2'),
            ('频率（铭牌）', '2450 兆赫', '每秒 24.5 亿次'), ('光速 = 波长 × 频率', '≈ 3.0 亿 米/秒', '')]
    for k, (a_, b_, c_) in enumerate(rows):
        d = fade(t, 6 + k * 2.5, 7 + k * 2.5)
        if d <= 0: continue
        y = 640 + k * 70
        c.text(220, y, a_, 'bold', 28, mix(BG, INK, d), 'lm')
        c.text(800, y, b_, 'mono', 28, mix(BG, GREEN if k == 3 else INK, d), 'lm')
        c.text(1300, y, c_, 'sans', 24, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 6, '拿掉转盘，放一板巧克力，只热十几秒：它不会均匀地软，而是化出一排点'),
                (6.2, 13, '相邻两个点隔半个波长：量出来大约 6 厘米，波长就是 12 厘米左右'),
                (13.2, 22, '再乘上铭牌上的频率 2450 兆赫：大约每秒 3 亿米，就是光速。微波炉的磁控管，来自二战时的雷达')], y=1010)

# ---------------------------------------------------------------- E94 激光
def e94_coherent(c, t, i):
    corner_tag(c, '第 94 集 · 一样的颜色，一样的步调')
    c.text(60, 96, '手电的光乱七八糟往外散，激光整整齐齐往前走', 'serif', 40, INK)
    for k, (nm, coh, y0) in enumerate((('手电筒', False, 340), ('激光', True, 700))):
        a = fade(t, 1 + k * 6, 2 + k * 6)
        if a <= 0: continue
        c.rect(160, y0 - 50, 300, y0 + 50, fill=mix(BG, MUTED, a), r=10)
        c.text(230, y0 + 90, nm, 'bold', 28, mix(BG, INK, a), 'mm')
        rnd = random.Random(k + 3)
        for j in range(7):
            if coh:
                col, ph, ang, lam = LASER, t * 8, 0.0, 60
            else:
                col = [(230, 80, 70), (240, 180, 60), (90, 190, 100), (80, 140, 230), (200, 120, 220)][j % 5]
                ph, ang, lam = t * 8 + rnd.uniform(0, 6), rnd.uniform(-0.16, 0.16), rnd.uniform(40, 80)
            pts = []
            for q in range(120):
                d = q * 12
                x = 300 + d * math.cos(ang)
                y = y0 + (j - 3) * (6 if coh else 14) + d * math.sin(ang) + 10 * math.sin(d / lam * 2 * math.pi - ph)
                if x > 1820 or abs(y - y0) > 170: break
                pts.append((x, y))
            c.line(pts, mix(BG, col, a), 2)
    caps(c, t, [(0, 6, '手电的光：各种颜色混在一起，你推我挤，步调不一，出了灯口就散开'),
                (6.2, 13, '激光：只有一种颜色，所有的波峰波谷对得整整齐齐，几乎不散开'),
                (13.2, 22, '1917 年爱因斯坦预言了受激辐射；1960 年梅曼用一根红宝石做出第一台激光器')], y=1010)

def e94_hair(c, t, i):
    corner_tag(c, '第 94 集 · 用激光量头发')
    c.text(60, 96, '一根头发挡在激光前面，墙上出现一排亮点', 'serif', 40, INK)
    c.rect(160, 420, 260, 480, fill=MUTED, r=8)
    c.line([(260, 450), (700, 450)], LASER, 4)
    c.line([(700, 300), (700, 600)], (60, 50, 40), 2)
    c.text(700, 640, '头发', 'sans', 24, MUTED, 'mm')
    a = fade(t, 2, 3)
    for k in range(-4, 5):
        yy = 450 + k * 60
        c.line([(700, 450), (1500, yy)], mix(BG, LASER, a * (0.9 if k == 0 else 0.35)), 2)
        r = 22 if k == 0 else 12
        c.ellipse(1520, yy, r, r * 0.6, fill=mix(BG, LASER, a * (1 if k == 0 else 0.6 / (1 + abs(k) * 0.3))))
    c.rect(1500, 180, 1520, 720, fill=mix(BG, SHEET, 0.7))
    c.text(1560, 480, 'Δx', 'mono', 26, INK, 'lm')
    c.text(1100, 760, 'L：头发到墙的距离', 'sans', 24, MUTED, 'mm')
    b = fade(t, 9, 10)
    c.rect(200, 820, 1720, 920, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 850, '头发粗细 ≈ 波长 × L ÷ Δx', 'bold', 28, mix(BG, INK, b), 'mm')
    c.text(960, 892, '例：650 纳米 × 2 米 ÷ 1.7 厘米 ≈ 76 微米（以实测为准）', 'mono', 24, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '激光碰到一根细头发，从两边绕过去，在墙上叠出一排亮点和暗点'),
                (6.2, 13, '头发越细，亮点之间隔得越开：这就是衍射，只有又纯又整齐的光才看得清'),
                (13.2, 22, '量出亮点间距，就能算出头发有多粗：几十微米的东西，用一把卷尺就量出来了（激光笔由成年人操作）')], y=1010)

CLIPS = {
 'E92_放大': (e92_amp, 22), 'E92_三明治': (e92_pn, 22),
 'E92_片头': (titles.opening(SER17, VOL17, S17A, 0, '1947 年 · 贝尔实验室'), 7),
 'E92_片尾': (titles.closing(SER17, VOL17, S17A, 0, '下集：微波炉为什么转着热？'), 7),
 'E93_驻波': (e93_standing, 22), 'E93_光速': (e93_speed, 22),
 'E93_片头': (titles.opening(SER17, VOL17, S17A, 1, '1945 年 · 斯潘塞与雷达的磁控管'), 7),
 'E93_片尾': (titles.closing(SER17, VOL17, S17A, 1, '下集：激光和手电的光，有什么不一样？'), 7),
 'E94_相干': (e94_coherent, 22), 'E94_衍射': (e94_hair, 22),
 'E94_片头': (titles.opening(SER17, VOL17, S17A, 2, '1960 年 · 梅曼的红宝石激光'), 7),
 'E94_片尾': (titles.closing(SER17, VOL17, S17A, 2, '下集：手机的相机，怎么把光变成一串数字？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
