"""第八季第三批：E58 电动机、E59 电镀、E60 电灯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s8a import S8A, SER8, VOL8
from s8b import nail_coil

CU = (200, 110, 60)
CUION = (80, 150, 220)
STEEL = (150, 155, 160)

def magnet(c, x0, y0, x1, y1, north_left=True, a=1.0):
    mid = (x0 + x1) / 2
    c.rect(x0, y0, mid, y1, fill=mix(BG, NRED if north_left else SBLUE, a), r=6)
    c.rect(mid, y0, x1, y1, fill=mix(BG, SBLUE if north_left else NRED, a), r=6)
    c.text((x0 + mid) / 2, (y0 + y1) / 2, 'N' if north_left else 'S', 'bold', 30, mix(BG, INK, a), 'mm')
    c.text((mid + x1) / 2, (y0 + y1) / 2, 'S' if north_left else 'N', 'bold', 30, mix(BG, INK, a), 'mm')

# ---------------------------------------------------------------- E58 电动机
def e58_force(c, t, i):
    corner_tag(c, '第 58 集 · 磁场里的电流')
    c.text(60, 96, '通了电的导线，放进磁铁中间会怎样？', 'serif', 40, INK)
    # poles left/right, field arrows across
    c.rect(200, 300, 380, 780, fill=NRED, r=10); c.text(290, 540, 'N', 'bold', 60, INK, 'mm')
    c.rect(1180, 300, 1360, 780, fill=SBLUE, r=10); c.text(1270, 540, 'S', 'bold', 60, INK, 'mm')
    for y in range(340, 760, 70):
        c.arrow(400, y, 1160, y, mix(BG, FIELD, 0.5), 2, 12)
    on = fade(t, 4, 5)
    off = min(max(t - 5, 0), 2) * 50 * on
    wx = 780
    c.ellipse(wx, 540 - off, 36, 36, fill=mix(BG, CU, 1), outline=INK, width=3)
    if on > 0:
        c.ellipse(wx, 540 - off, 10, 10, fill=INK)   # current out of screen
        c.arrow(wx, 470 - off, wx, 380 - off, mix(BG, SPARK, on), 6, 18)
        c.text(wx + 60, 410 - off, '受力', 'bold', 30, mix(BG, SPARK, on), 'lm')
    c.text(wx, 840, '导线（电流朝屏幕外）', 'sans', 24, MUTED, 'mm')
    a = fade(t, 11, 12)
    c.rect(1420, 260, 1860, 620, fill=mix(BG, SHEET, a), r=14)
    c.text(1450, 310, '磁场 + 电流 → 力', 'bold', 30, mix(BG, SPARK, a), 'lm')
    c.text(1450, 370, '力的方向和两者都垂直', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1450, 420, '电流反向，力也反向', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1450, 490, '把导线弯成线圈：', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1450, 535, '一边往上推，一边往下推', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1450, 580, '线圈就转起来了', 'bold', 26, mix(BG, SPARK, a), 'lm')
    caps(c, t, [(0, 4, '两块磁铁之间是磁场；中间放一根导线'),
                (4.2, 11, '一通电，导线被一股力推了出去：方向和磁场、电流都垂直'),
                (11.2, 22, '把导线弯成一个线圈，一边被往上推、一边被往下推，线圈就转起来：这就是电动机')], y=1010)

def e58_reverse(c, t, i):
    corner_tag(c, '第 58 集 · 倒过来用')
    c.text(60, 96, '电动机和发电机，是不是同一台机器？', 'serif', 40, INK)
    for k, (cx, title, sub, col) in enumerate([(520, '通电 → 转起来', '电动机', SPARK), (1400, '用手转 → 出电', '发电机（第 05 集）', GREEN)]):
        a = fade(t, 0.5 + k * 7, 1.5 + k * 7)
        if a <= 0: continue
        cy = 520
        c.rect(cx - 260, cy - 200, cx + 260, cy + 200, outline=mix(BG, MUTED, a), width=3, r=20)
        magnet(c, cx - 240, cy - 60, cx - 170, cy + 60, True, a)
        magnet(c, cx + 170, cy - 60, cx + 240, cy + 60, False, a)
        ang = t * 3
        for j in range(3):
            q = ang + j * 2 * math.pi / 3
            c.line([(cx, cy), (cx + 130 * math.cos(q), cy + 130 * math.sin(q))], mix(BG, CU, a), 10)
        c.ellipse(cx, cy, 30, 30, fill=mix(BG, STEEL, a))
        c.text(cx, cy - 250, title, 'bold', 32, mix(BG, col, a), 'mm')
        c.text(cx, cy + 250, sub, 'sans', 26, mix(BG, MUTED, a), 'mm')
        if k == 0:
            c.rect(cx - 60, cy + 290, cx + 60, cy + 340, outline=mix(BG, SPARK, a), width=3, r=6)
            c.text(cx, cy + 315, '电池', 'sans', 22, mix(BG, SPARK, a), 'mm')
        else:
            on = 0.5 + 0.5 * math.sin(t * 6)
            c.ellipse(cx, cy + 315, 26, 26, fill=mix(BG, SPARK, a * on))
            c.text(cx + 50, cy + 315, 'LED', 'sans', 22, mix(BG, SPARK, a), 'lm')
    b = fade(t, 15, 16)
    c.rect(300, 900, 1620, 970, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 935, '同一台机器：电进，力出；力进，电出。转起来的电动机也在「发电」，顶着电池（反电动势）', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 7, '给它通电，它就转：电变成了转动'),
                (7.2, 15, '反过来用手拧它，接上的灯就亮：转动又变回了电'),
                (15.2, 22, '电动机和发电机是同一台机器的两个方向。1821 年法拉第第一次让通电导线绕着磁铁转了起来')], y=1035)

# ---------------------------------------------------------------- E59 电镀
def e59_ions(c, t, i):
    corner_tag(c, '第 59 集 · 铜离子搬家')
    c.text(60, 96, '溶液里的铜，怎么「长」到钥匙上？', 'serif', 40, INK)
    c.rect(360, 320, 1400, 880, outline=MUTED, width=5, r=10)
    c.rect(366, 380, 1394, 874, fill=mix(BG, CUION, 0.25), r=8)
    # anode copper plate (left, +), cathode key (right, -)
    c.rect(480, 250, 540, 800, fill=CU, r=4)
    c.text(510, 920, '铜片（接正极）', 'bold', 24, CU, 'mm')
    c.rect(1180, 250, 1240, 800, fill=STEEL, r=4)
    plate = fade(t, 6, 18)
    if plate > 0:
        c.rect(1172, 380, 1180, 800, fill=mix(STEEL, CU, plate)); c.rect(1240, 380, 1248, 800, fill=mix(STEEL, CU, plate))
    c.text(1210, 920, '铁钥匙（接负极）', 'bold', 24, INK, 'mm')
    c.line([(510, 250), (510, 180), (800, 180)], SPARK, 4)
    c.line([(1210, 250), (1210, 180), (960, 180)], SPARK, 4)
    c.rect(800, 155, 960, 205, outline=SPARK, width=3, r=6)
    c.text(880, 180, '电池', 'sans', 22, SPARK, 'mm')
    on = t > 2
    rnd = random.Random(59)
    for k in range(36):
        y = rnd.uniform(420, 840)
        ph = rnd.uniform(0, 1)
        if on:
            f = ((t - 2) * 0.12 + ph) % 1
            x = 560 + (1160 - 560) * f
        else:
            x = 560 + 600 * ph
        c.ellipse(x, y, 14, 14, fill=CUION)
        c.text(x, y, '+', 'bold', 16, INK, 'mm')
    a = fade(t, 9, 10)
    c.rect(1440, 300, 1880, 700, fill=mix(BG, SHEET, a), r=14)
    c.text(1470, 350, '铜离子（蓝点）', 'sans', 24, mix(BG, CUION, a), 'lm')
    c.text(1470, 395, '游向负极的钥匙', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1470, 450, '在钥匙表面得到电子', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1470, 495, '变回铜原子，一层层长上去', 'bold', 26, mix(BG, SPARK, a), 'lm')
    c.text(1470, 560, '正极的铜片同时溶解', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1470, 605, '补充溶液里的铜离子', 'sans', 24, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 2, '硫酸铜溶液里，飘着无数带正电的铜离子'),
                (2.2, 9, '接上电池：铜离子被吸向接负极的钥匙'),
                (9.2, 16, '在钥匙表面接过电子，变回铜原子，一层一层长上去'),
                (16.2, 22, '第 17 集是铁「抢」走溶液里的铜；这一集，是电流把铜一个个「送」上去')], y=1010)

def e59_current(c, t, i):
    corner_tag(c, '第 59 集 · 电流越大越好吗')
    c.text(60, 96, '电流开大一点，镀得更快、更好？', 'serif', 40, INK)
    for k, (cx, lab, rough, col) in enumerate([(520, '小电流 · 慢慢镀', 0.0, (205, 120, 70)), (1400, '大电流 · 急着镀', 1.0, (80, 50, 40))]):
        a = fade(t, 0.5 + k * 6, 1.5 + k * 6)
        if a <= 0: continue
        g = fade(t, 1.5 + k * 6, 6 + k * 6)
        y0 = 560
        c.rect(cx - 300, y0, cx + 300, y0 + 60, fill=mix(BG, STEEL, a), r=4)
        rnd = random.Random(k + 3)
        for j in range(60):
            x = cx - 290 + j * 10
            h = 18 * g * (1 + rough * rnd.uniform(-0.8, 2.2))
            c.rect(x, y0 - h, x + 10, y0, fill=mix(BG, col, a))
        if rough:
            for j in range(18):
                x = cx - 280 + rnd.uniform(0, 560); y = y0 - 30 * g - rnd.uniform(0, 40) * g
                c.ellipse(x, y, 5, 5, fill=mix(BG, col, a * g))
        c.text(cx, 360, lab, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(cx, 720, '均匀、光亮、结实' if not rough else '发黑、粗糙、一擦就掉', 'bold', 28, mix(BG, GREEN if not rough else NRED, a), 'mm')
    b = fade(t, 14, 15)
    c.rect(300, 820, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 860, '镀上的铜有多少，只看通过了多少电量（法拉第，1830 年代）', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 915, '电流太大，铜原子来不及排好就堆上去：「烧焦」了', 'bold', 28, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 6, '小电流慢慢镀：铜原子有时间排好队，一层光亮的铜'),
                (6.2, 14, '电流开太大：铜原子来不及排好就乱堆上去，发黑、发粗，一擦就掉'),
                (14.2, 22, '镀多少只看电量：小电流多镀一会儿，和大电流一样多，还更好看')], y=1010)

# ---------------------------------------------------------------- E60 电灯
def e60_glow(c, t, i):
    corner_tag(c, '第 60 集 · 烧到发白')
    c.text(60, 96, '灯丝为什么会发光？', 'serif', 40, INK)
    T = 20 + 2780 * ease(fade(t, 1, 13))
    def col(T):
        if T < 500: return (60, 60, 60)
        if T < 900: return mix((60, 60, 60), (170, 30, 20), (T - 500) / 400)
        if T < 1400: return mix((170, 30, 20), (240, 120, 30), (T - 900) / 500)
        if T < 2200: return mix((240, 120, 30), (255, 220, 140), (T - 1400) / 800)
        return mix((255, 220, 140), (255, 250, 235), min(1, (T - 2200) / 600))
    cx, cy = 600, 480
    c.ellipse(cx, cy, 230, 260, outline=mix(BG, (200, 210, 220), 0.6), width=4)
    if T > 900:
        c.ellipse(cx, cy, 40 + T / 30, 30 + T / 40, fill=mix(BG, col(T), min(0.18, (T - 900) / 8000)))
    pts = [(cx - 120 + k * 12, cy + (20 if k % 2 else -20)) for k in range(21)]
    c.line(pts, col(T), 6)
    c.line([(cx - 120, cy), (cx - 80, cy + 300)], STEEL, 4)
    c.line([(cx + 120, cy), (cx + 80, cy + 300)], STEEL, 4)
    c.text(cx, cy + 340, f'灯丝温度约 {T:.0f} ℃', 'mono', 32, INK, 'mm')
    marks = [(600, '暗红'), (1000, '橙红'), (1500, '橙黄'), (2500, '黄白（白炽灯）')]
    for k, (Tm, lab) in enumerate(marks):
        y = 280 + k * 110
        a = 1.0 if T >= Tm else 0.25
        c.rect(1100, y - 30, 1160, y + 30, fill=mix(BG, col(Tm), a), r=6)
        c.text(1190, y, f'{Tm} ℃ · {lab}', 'sans', 26, mix(BG, INK, a), 'lm')
    b = fade(t, 14, 15)
    c.rect(300, 860, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 910, '白炽灯是先发热、再发光：电能只有百分之几变成看得见的光，其余都是热', 'bold', 26, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 5, '电流通过很细的灯丝，电阻让它发热'),
                (5.2, 13, '越来越热：先是暗红，再是橙黄，到两千多度就白得刺眼'),
                (13.2, 22, '电灯其实是一个「烧到发白」的电炉：大部分电都变成了热')], y=1010)

def e60_vacuum(c, t, i):
    corner_tag(c, '第 60 集 · 关进真空')
    c.text(60, 96, '同样的灯丝，为什么在空气里一下就断？', 'serif', 40, INK)
    for k, (cx, lab, air) in enumerate([(520, '在空气里', True), (1400, '抽成真空', False)]):
        a = fade(t, 0.5, 1.5)
        cy = 480
        c.ellipse(cx, cy, 230, 260, outline=mix(BG, (200, 210, 220), 0.6 * a), width=4)
        heat = fade(t, 2, 4)
        broke = air and t > 9
        glow = (255, 240, 200)
        if air:
            rnd = random.Random(int(t * 10))
            for j in range(26):
                x = cx + rnd.uniform(-180, 180); y = cy + rnd.uniform(-200, 200)
                c.text(x, y, '氧', 'sans', 18, mix(BG, FIELD, 0.6 * a), 'mm')
        pts = [(cx - 120 + j * 12, cy + (20 if j % 2 else -20)) for j in range(21)]
        if broke:
            c.line(pts[:9], (90, 70, 60), 6); c.line(pts[11:], (90, 70, 60), 6)
            c.text(cx, cy + 90, '烧断了', 'bold', 30, NRED, 'mm')
        else:
            if heat > 0.5:
                c.ellipse(cx, cy, 150, 90, fill=mix(BG, glow, 0.12 * heat))
            c.line(pts, mix((60, 60, 60), glow, heat), 6)
        c.text(cx, cy - 300, lab, 'bold', 32, INK, 'mm')
    b = fade(t, 11, 12)
    c.rect(300, 820, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 860, '空气里的氧会和炽热的灯丝反应，几秒就把它「烧」断', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 915, '1879 年前后，爱迪生和斯旺把碳丝封进真空玻璃泡；后来换成更耐热的钨丝', 'bold', 26, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 4, '同样的灯丝，同样通电烧到发白'),
                (4.2, 11, '在空气里：氧气扑上来，几秒钟灯丝就断了'),
                (11.2, 22, '关进真空玻璃泡，没有氧气，灯丝能亮上千个小时：这就是第 21 集玻璃的又一个用处')], y=1035)

CLIPS = {
 'E58_受力': (e58_force, 22), 'E58_倒过来用': (e58_reverse, 22),
 'E58_片头': (titles.opening(SER8, VOL8, S8A, 6, '穿越北宋 · 让水车「倒着」转'), 7),
 'E58_片尾': (titles.closing(SER8, VOL8, S8A, 6, '下集：一把铁钥匙，怎么镀上一层铜？'), 7),
 'E59_铜离子': (e59_ions, 22), 'E59_电流大小': (e59_current, 22),
 'E59_片头': (titles.opening(SER8, VOL8, S8A, 7, '穿越北宋 · 胆水浸铜的升级版'), 7),
 'E59_片尾': (titles.closing(SER8, VOL8, S8A, 7, '下集：灯丝为什么要关在真空里？'), 7),
 'E60_发热发光': (e60_glow, 22), 'E60_真空': (e60_vacuum, 22),
 'E60_片头': (titles.opening(SER8, VOL8, S8A, 8, '穿越北宋 · 只用动画：一盏不用油的灯'), 7),
 'E60_片尾': (titles.closing(SER8, VOL8, S8A, 8, '下集：电能不能存起来，晚上再用？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
