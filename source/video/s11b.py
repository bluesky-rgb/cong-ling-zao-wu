"""第十一季第二批：B33 素纱襌衣、B34 水运仪象台的擒纵、B35 罗马混凝土 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s9a import WATER
from s9b import gear, WOOD
from s11a import SB11, VOL11

SILK = (235, 225, 200)
COTTON = (225, 225, 225)
HAIR = (90, 70, 50)
LIME = (230, 230, 220)
ASH = (130, 120, 115)
CALC = (200, 220, 240)

# ---------------------------------------------------------------- B33 素纱襌衣
def b33_fiber(c, t, i):
    corner_tag(c, 'B33 · 一根丝有多细')
    c.text(60, 96, '放大 1000 倍看横截面', 'serif', 40, INK)
    items = [('蚕丝（单根）', 10, SILK), ('棉纤维', 18, COTTON), ('头发', 70, HAIR)]
    for k, (name, d, col) in enumerate(items):
        a = fade(t, 0.5 + k * 2, 1.5 + k * 2)
        x = 360 + k * 560
        r = d * 4.2
        c.ellipse(x, 520, r, r * (0.8 if k == 0 else 1), fill=mix(BG, col, a), outline=mix(BG, MUTED, a), width=2)
        c.text(x, 520 + 320, name, 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(x, 520 + 370, f'约 {d} 微米', 'mono', 26, mix(BG, MUTED, a), 'mm')
    b = fade(t, 8, 9)
    c.rect(200, 180, 1720, 270, fill=mix(BG, SHEET, b), r=10)
    c.text(230, 225, '纤维越细，同样长度越轻：纺织上用「旦」——9000 米长的丝有几克，就是几旦', 'sans', 26, mix(BG, INK, b), 'lm')
    d_ = fade(t, 13, 14)
    c.text(960, 930, '素纱襌衣用的丝约 10 旦出头（9 千米只有 10 克多，待核）', 'bold', 28, mix(BG, GREEN, d_), 'mm')
    caps(c, t, [(0, 8, '一根蚕丝只有十微米左右，比棉纤维细，比头发细得多（数值为量级）'),
                (8.2, 13, '纺织上量丝的粗细用「旦」：九千米长的丝有几克重，就是几旦'),
                (13.2, 22, '马王堆的素纱襌衣用的丝极细：一件衣服的丝拉开有几十千米长，也只有几十克')], y=1010)

def b33_weave(c, t, i):
    corner_tag(c, 'B33 · 纱：织得稀')
    c.text(60, 96, '同样的丝，织得密是绸，织得稀是纱', 'serif', 40, INK)
    for k, (name, gap, frac) in enumerate([('平纹绸：经纬紧挨着', 16, 0.92), ('素纱：方孔占了大半', 44, 0.25)]):
        x0, y0, W = 160 + k * 860, 220, 600
        a = fade(t, 0.5 + k * 3, 1.5 + k * 3)
        c.text(x0 + W / 2, y0 - 30, name, 'bold', 28, mix(BG, INK, a), 'mm')
        c.rect(x0, y0, x0 + W, y0 + W, fill=mix(BG, (60, 70, 80), a), r=6)
        n = int(W / gap)
        th = gap * 0.42 if k == 0 else 7
        prog = fade(t, 1 + k * 3, 4 + k * 3)
        for j in range(int(n * prog)):
            x = x0 + gap / 2 + j * gap
            c.rect(x - th / 2, y0, x + th / 2, y0 + W, fill=mix(BG, SILK, a))
            c.rect(x0, y0 + gap / 2 + j * gap - th / 2, x0 + W, y0 + gap / 2 + j * gap + th / 2, fill=mix(BG, SILK, a))
        b = fade(t, 8, 9)
        c.text(x0 + W / 2, y0 + W + 50, f'丝占面积约 {frac * 100:.0f}%（示意）', 'mono', 26, mix(BG, INK, b), 'mm')
    d = fade(t, 12, 13)
    c.rect(160, 940, 1760, 990, fill=mix(BG, SHEET, d), r=10)
    c.text(960, 965, '直裾素纱襌衣：衣长约 128 厘米，重约 49 克（1972 年马王堆一号汉墓出土；另一件曲裾的约 48 克）', 'sans', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 4, '织得密的绸，经线纬线紧挨在一起'),
                (4.2, 12, '素纱每根丝之间留着方孔，孔比丝还宽：光能透过来，重量也少了一大半'),
                (12.2, 22, '极细的丝，加上稀疏的纱：两样一乘，一件大袍子还不到一两重')], y=1035)

# ---------------------------------------------------------------- B34 水运仪象台
def b34_bucket(c, t, i):
    corner_tag(c, 'B34 · 水斗满了才翻')
    c.text(60, 96, '水一直在流，轮子却一格一格地走', 'serif', 40, INK)
    cx, cy, R = 620, 620, 280
    n = 12
    period = 3.0
    step = int(t / period)
    ph = (t % period) / period
    jump = ease(fade(ph, 0.85, 1.0)) if True else 0
    ang = (step + jump) * 2 * math.pi / n
    c.ellipse(cx, cy, R, R, outline=WOOD, width=6)
    for k in range(n):
        q = ang + k * 2 * math.pi / n - math.pi / 2
        bx, by = cx + R * math.cos(q), cy + R * math.sin(q)
        c.line([(cx, cy), (bx, by)], mix(BG, WOOD, 0.6), 3)
        c.rect(bx - 34, by - 26, bx + 34, by + 26, outline=WOOD, width=3, r=4)
        # the bucket at the top-right (k==0 position after rotation) is filling
        if k == (-step) % n:
            lvl = min(1, ph / 0.85)
            c.rect(bx - 31, by + 23 - 46 * lvl, bx + 31, by + 23, fill=mix(BG, WATER, 0.8))
    # water spout
    sx, sy = cx + R * math.cos(ang - math.pi / 2), cy - R - 120
    c.rect(cx - 20, cy - R - 150, cx + 20, cy - R - 100, fill=mix(BG, WATER, 0.7))
    c.line([(cx, cy - R - 100), (cx, cy - R - 28)], WATER, 6)
    # balance lever (天衡)
    tilt = 0.25 * (1 if ph > 0.85 else -1) * (1 if ph > 0.85 else 0.4)
    lx, ly = cx + 420, cy - R + 20
    c.line([(lx - 200 * math.cos(tilt), ly - 200 * math.sin(tilt)), (lx + 200 * math.cos(tilt), ly + 200 * math.sin(tilt))], (150, 160, 175), 8)
    c.poly([(lx, ly), (lx - 20, ly + 40), (lx + 20, ly + 40)], MUTED)
    c.rect(lx + 180 * math.cos(tilt) - 26, ly + 180 * math.sin(tilt) - 20, lx + 180 * math.cos(tilt) + 26, ly + 180 * math.sin(tilt) + 30, fill=MUTED, r=4)
    c.text(lx, ly + 80, '天衡（杠杆 + 秤锤）', 'bold', 24, INK, 'mm')
    c.text(lx + 220, ly + 180 * math.sin(tilt), '秤锤', 'sans', 22, MUTED, 'lm')
    # step graph
    gx0, gx1, gy0, gy1 = 1240, 1840, 640, 900
    c.line([(gx0, gy1), (gx1, gy1)], MUTED, 2); c.line([(gx0, gy0), (gx0, gy1)], MUTED, 2)
    c.text(gx0, gy0 - 24, '轮子转过的格数', 'sans', 22, MUTED, 'lm')
    pts = []
    for j in range(int(200 * t / 22) + 1):
        tt = j / 200 * 22
        s_ = int(tt / period) + ease(fade((tt % period) / period, 0.85, 1.0))
        pts.append((gx0 + (gx1 - gx0) * tt / 22, gy1 - (gy1 - gy0) * s_ / 8))
    if len(pts) > 1: seg(c, pts, COPPER, 4)
    c.text(gx1, gy1 + 24, '时间 →', 'sans', 20, MUTED, 'rm')
    caps(c, t, [(0, 7, '水从上面一直流进水斗，可轮子被卡住，不动'),
                (7.2, 14, '水斗装满了，重量压过天衡另一头的秤锤，卡子一抬，轮子转过一格又被卡住'),
                (14.2, 22, '连续的水流，变成了一格一格的跳动：这就是擒纵（结构为示意，拍摄前核对）')], y=1010)

def b34_compare(c, t, i):
    corner_tag(c, 'B34 · 为什么要卡住它')
    c.text(60, 96, '不卡住，水大轮子就快，水小就慢', 'serif', 40, INK)
    gx0, gx1 = 260, 1700
    rows = [(380, '没有擒纵：随水流忽快忽慢', NRED, False), (760, '有擒纵：每格都等水斗装满', GREEN, True)]
    for k, (yc, name, col, esc) in enumerate(rows):
        a = fade(t, 0.5 + k * 3, 1.5 + k * 3)
        if a <= 0: continue
        c.text(gx0, yc - 170, name, 'bold', 28, mix(BG, col, a), 'lm')
        c.line([(gx0, yc + 100), (gx1, yc + 100)], mix(BG, MUTED, a), 2)
        c.line([(gx0, yc - 130), (gx0, yc + 100)], mix(BG, MUTED, a), 2)
        prog = fade(t, 1 + k * 3, 12 + k * 3)
        pts = []
        pos = 0.0
        for j in range(int(300 * prog) + 1):
            u = j / 300
            flow = 1 + 0.5 * math.sin(u * 9) + 0.3 * math.sin(u * 23)
            if not esc:
                pos += flow / 300 * 8
                y = pos
            else:
                y = round(u * 8 * 1.0 - 0.5) if u > 0 else 0
            pts.append((gx0 + (gx1 - gx0) * u, yc + 100 - 230 * y / 11))
        if len(pts) > 1: seg(c, pts, mix(BG, col, a), 4)
    b = fade(t, 15, 16)
    c.text(960, 980 - 40, '水斗的容量是固定的：每一格代表差不多一样长的时间。和第 45 集的摆一样，用「一下一下」来数时间', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '水流不可能一直一样快：直接让水推轮子，水大就快，水小就慢'),
                (6.2, 15, '加上擒纵，每一格都要等水斗装满才走：时间被切成一样长的小段'),
                (15.2, 22, '苏颂和韩公廉的水运仪象台（1088–1092 年）用的就是这个思路，比欧洲的机械钟擒纵早两百多年（拍摄前核对）')], y=1035)

# ---------------------------------------------------------------- B35 罗马混凝土
def b35_ash(c, t, i):
    corner_tag(c, 'B35 · 石灰加火山灰')
    c.text(60, 96, '只用石灰泡在水里会软；加上火山灰就在水里变硬', 'serif', 38, INK)
    for k, (name, ash) in enumerate([('石灰 + 沙', False), ('石灰 + 火山灰', True)]):
        x0 = 160 + k * 860
        a = fade(t, 0.5 + k, 1.5 + k)
        c.text(x0 + 300, 200, name, 'bold', 30, mix(BG, INK, a), 'mm')
        c.rect(x0, 250, x0 + 600, 750, fill=mix(BG, WATER, 0.25 * a), outline=mix(BG, MUTED, a), width=3, r=8)
        rnd = random.Random(k + 1)
        g = fade(t, 4, 14)
        for j in range(60):
            px, py = x0 + 40 + rnd.random() * 520, 290 + rnd.random() * 420
            if ash and j % 2:
                c.ellipse(px, py, 14, 14, fill=mix(BG, ASH, a))
            else:
                c.ellipse(px, py, 12, 12, fill=mix(BG, LIME, a))
        if ash and g > 0:
            rnd2 = random.Random(9)
            for j in range(int(140 * g)):
                px, py = x0 + 40 + rnd2.random() * 520, 290 + rnd2.random() * 420
                q = rnd2.random() * math.pi
                c.line([(px, py), (px + 22 * math.cos(q), py + 22 * math.sin(q))], mix(BG, GREEN, 0.9), 3)
        res = '水里泡着，一直是软泥' if not ash else '长出针状、片状的新晶体，越泡越硬'
        c.text(x0 + 300, 800, res, 'bold', 26, mix(BG, NRED if not ash else GREEN, fade(t, 12, 13)), 'mm')
    caps(c, t, [(0, 6, '第 24 集的石灰浆要接触空气里的二氧化碳才慢慢变硬，泡在水里就硬不起来'),
                (6.2, 14, '罗马人加了火山灰：火山灰里的硅和铝跟石灰、水反应，在水里也能结晶变硬'),
                (14.2, 22, '泡在海水里的罗马码头，还会继续长出新的矿物晶体（2017 年的研究，拍摄前核对）')], y=1010)

def b35_heal(c, t, i):
    corner_tag(c, 'B35 · 会自己补裂缝')
    c.text(60, 96, '罗马混凝土里的白色石灰小块，是故意留的？', 'serif', 40, INK)
    x0, x1, y0, y1 = 360, 1560, 260, 800
    c.rect(x0, y0, x1, y1, fill=mix(BG, ASH, 0.7), r=8)
    rnd = random.Random(35)
    for j in range(40):
        c.ellipse(x0 + 30 + rnd.random() * (x1 - x0 - 60), y0 + 30 + rnd.random() * (y1 - y0 - 60), 10 + rnd.random() * 14, 8 + rnd.random() * 10, fill=(150, 140, 130))
    clast = (960, 560, 70)
    c.ellipse(clast[0], clast[1], clast[2], clast[2] * 0.8, fill=LIME)
    c.text(clast[0] + 90, clast[1] + 90, '石灰小块', 'bold', 24, INK, 'lm')
    crack = fade(t, 2, 5)
    if crack > 0:
        pts = [(700, 260), (760, 360), (830, 430), (900, 500), (960, 560)]
        n = int(len(pts) * crack + 0.999)
        seg(c, pts[:max(2, n)], (40, 35, 30), 6)
    wtr = fade(t, 6, 10)
    if wtr > 0:
        pts = [(700, 260), (760, 360), (830, 430), (900, 500), (960, 560)]
        seg(c, pts[:max(2, int(5 * wtr + 0.999))], WATER, 3)
        c.text(640, 240, '雨水渗进裂缝', 'bold', 24, mix(BG, WATER, wtr), 'rm')
    heal = fade(t, 11, 17)
    if heal > 0:
        pts = [(700, 260), (760, 360), (830, 430), (900, 500), (960, 560)]
        seg(c, pts, mix((40, 35, 30), CALC, heal), 8)
        c.ellipse(clast[0], clast[1], clast[2] * (1 - 0.25 * heal), clast[2] * 0.8 * (1 - 0.25 * heal), fill=LIME)
        c.text(1580, 400, '石灰溶进水里，', 'sans', 24, mix(BG, INK, heal), 'lm')
        c.text(1580, 445, '在裂缝里重新结晶', 'sans', 24, mix(BG, INK, heal), 'lm')
        c.text(1580, 490, '（碳酸钙）：缝被填上', 'bold', 24, mix(BG, CALC, heal), 'lm')
    d = fade(t, 17, 18)
    c.text(960, 880, '万神殿穹顶（约公元 125 年）至今仍是世界上最大的无钢筋混凝土穹顶', 'sans', 26, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 6, '罗马混凝土里常见一颗颗白色的石灰小块，过去以为是没拌匀'),
                (6.2, 11, '2023 年的研究认为：裂缝里渗进水，水先溶解这些石灰小块（拍摄前核对）'),
                (11.2, 22, '溶解的石灰在缝里重新结晶，把裂缝自己补上：越用越结实')], y=1010)

CLIPS = {
 'B33_纤维': (b33_fiber, 22), 'B33_纱织': (b33_weave, 22),
 'B33_片头': (titles.opening(BSER, VOL11, SB11, 3, '西汉 · 1972 年长沙马王堆出土'), 7),
 'B33_片尾': (titles.closing(BSER, VOL11, SB11, 3, '下集：一千年前的钟，怎么一格一格地走？'), 7),
 'B34_水斗': (b34_bucket, 22), 'B34_擒纵': (b34_compare, 22),
 'B34_片头': (titles.opening(BSER, VOL11, SB11, 4, '北宋 · 1088–1092 年 · 苏颂、韩公廉'), 7),
 'B34_片尾': (titles.closing(BSER, VOL11, SB11, 4, '下集（世界篇）：海水泡了两千年，为什么反而更结实？'), 7),
 'B35_火山灰': (b35_ash, 22), 'B35_自愈': (b35_heal, 22),
 'B35_片头': (titles.opening(BSER, VOL11, SB11, 5, '世界篇 · 古罗马 · 万神殿'), 7),
 'B35_片尾': (titles.closing(BSER, VOL11, SB11, 5, '下集：拖巨石的人，为什么往沙上浇水？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
