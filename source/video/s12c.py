"""第十二季第三批：E78 内燃机、E79 悬索桥、E80 机械计算器 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s9b import gear
from s12a import S12A, SER12, VOL12

STEELG = (150, 160, 175)
GAS = (150, 190, 230)
FIRE = (240, 140, 50)
CABLE = (200, 205, 215)

# ---------------------------------------------------------------- E78 内燃机
STROKES = [('进气', '活塞下行，吸进油气', GAS), ('压缩', '活塞上行，把气压紧', SPARK), ('做功', '火花一点，燃气推活塞', FIRE), ('排气', '活塞上行，推出废气', MUTED)]

def e78_four(c, t, i):
    corner_tag(c, '第 78 集 · 四冲程（燃烧只用动画）')
    c.text(60, 96, '进气、压缩、做功、排气：曲轴转两圈一个循环', 'serif', 38, INK)
    cyc = 8.0
    ph = (t % cyc) / cyc
    k = int(ph * 4)
    u = ph * 4 - k
    ang = ph * 4 * math.pi          # crank angle, 2 turns per cycle
    cx, top, R, L = 700, 300, 100, 200
    py = top + 60 + R * (1 - math.cos(ang)) + 0   # piston top y (0 = TDC)
    # cylinder
    c.rect(cx - 130, top, cx + 130, top + 370, outline=STEELG, width=8)
    # gas fill
    name, desc, col = STROKES[k]
    gc = col if k != 2 else mix(FIRE, MUTED, u)
    c.rect(cx - 122, top + 8, cx + 122, py, fill=mix(BG, gc, 0.55))
    if k == 2 and u < 0.25:
        c.ellipse(cx, top + 40, 60 * (1 - u * 3), 40 * (1 - u * 3), fill=SPARK)
    # valves
    vin = k == 0
    vout = k == 3
    c.line([(cx - 60, top - 60), (cx - 60, top + (20 if vin else 0))], STEELG, 6)
    c.line([(cx + 60, top - 60), (cx + 60, top + (20 if vout else 0))], STEELG, 6)
    c.text(cx - 60, top - 80, '进气门', 'sans', 20, GAS if vin else MUTED, 'mm')
    c.text(cx + 60, top - 80, '排气门', 'sans', 20, MUTED, 'mm')
    c.ellipse(cx, top - 6, 10, 10, fill=SPARK if (k == 2 and u < 0.1) else MUTED)
    # piston, rod, crank
    c.rect(cx - 120, py, cx + 120, py + 70, fill=STEELG, r=6)
    crx, cry = cx, top + 60 + 2 * R + 70 + 150
    pin = (crx + R * math.sin(ang), cry - R * math.cos(ang))
    c.line([(cx, py + 50), pin], STEELG, 12)
    c.ellipse(crx, cry, R + 20, R + 20, outline=MUTED, width=3)
    c.line([(crx, cry), pin], INK, 10)
    # stroke list
    for j, (n_, d_, col_) in enumerate(STROKES):
        y = 300 + j * 130
        on = j == k
        c.rect(1180, y - 50, 1820, y + 50, fill=mix(BG, col_, 0.35 if on else 0.08), r=10)
        c.text(1210, y - 12, f'{j + 1}. {n_}', 'bold', 30, INK if on else MUTED, 'lm')
        c.text(1210, y + 26, d_, 'sans', 22, INK if on else MUTED, 'lm')
    caps(c, t, [(0, 8, '活塞往下吸进燃料和空气，往上把它压紧；火花一点，燃气膨胀猛推活塞，再把废气推出去'),
                (8.2, 16, '连杆和曲轴（第 40 集）把活塞的上下运动变成转动：每两圈只有一次真正在用力'),
                (16.2, 22, '1876 年奥托造出了实用的四冲程发动机（燃烧只用动画，不自制任何燃烧装置）')], y=1010)

def e78_compress(c, t, i):
    corner_tag(c, '第 78 集 · 压得越紧越热')
    c.text(60, 96, '为什么要先压缩，再点火？', 'serif', 40, INK)
    r = 1 + 9 * ease(fade(t, 2, 12))     # compression ratio 1..10
    cx, top, H = 640, 240, 580
    gas_h = H / r
    c.rect(cx - 140, top, cx + 140, top + H + 40, outline=STEELG, width=8)
    py = top + H - gas_h
    T = 300 * r ** 0.4
    col = mix(GAS, FIRE, min(1, (T - 300) / 450))
    c.rect(cx - 132, top + H - gas_h + 8, cx + 132, top + H + 32, fill=mix(BG, col, 0.7))
    c.rect(cx - 132, py - 40, cx + 132, py + 8, fill=STEELG, r=6)
    c.line([(cx, py - 40), (cx, top - 60)], STEELG, 12)
    rnd = random.Random(int(t * 20))
    for j in range(40):
        c.ellipse(cx - 120 + rnd.random() * 240, py + 20 + rnd.random() * max(10, gas_h - 30), 4, 4, fill=INK)
    # readouts
    c.text(1000, 300, f'体积缩小到 1/{r:.1f}', 'mono', 34, INK, 'lm')
    c.text(1000, 380, f'温度约 {T - 273:.0f} °C', 'mono', 34, mix(INK, FIRE, min(1, (T - 300) / 450)), 'lm')
    c.text(1000, 440, '（不跟外面换热时的理想值）', 'sans', 22, MUTED, 'lm')
    a = fade(t, 13, 14)
    c.rect(980, 520, 1820, 800, fill=mix(BG, SHEET, a), r=12)
    c.text(1010, 570, '压紧的油气一点就猛烈燃烧，推力大得多', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1010, 630, '柴油机压得更紧，不用火花：', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1010, 680, '空气热到自己就能点燃燃油', 'bold', 26, mix(BG, FIRE, a), 'lm')
    c.text(1010, 745, '打气筒越打越热，也是这个道理', 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 7, '把一筒空气迅速压缩，分子挤在一起、撞得更凶：温度升高'),
                (7.2, 13, '压到原来的十分之一，理想情况下能从常温升到四五百度'),
                (13.2, 22, '所以发动机先压缩再点火：燃烧更猛、效率更高。家里只用打气筒感受压缩发热')], y=1010)

# ---------------------------------------------------------------- E79 悬索桥
def e79_forces(c, t, i):
    corner_tag(c, '第 79 集 · 谁在受拉，谁在受压')
    c.text(60, 96, '主缆受拉，塔受压，两头的锚把缆拽住', 'serif', 40, INK)
    deck = 760
    t1, t2 = 560, 1360
    tt = 300
    c.rect(100, deck, 1820, deck + 26, fill=STEELG, r=4)
    for x in (t1, t2):
        c.rect(x - 22, tt, x + 22, deck + 120, fill=(170, 160, 150), r=4)
    # main cable: parabola between towers, straight to anchors
    def cy(x):
        mid = (t1 + t2) / 2; half = (t2 - t1) / 2
        return tt + (deck - 60 - tt) * (1 - ((x - mid) / half) ** 2)
    pts = [(160, deck + 20), (t1, tt)] + [(t1 + (t2 - t1) * j / 60, 0) for j in range(1, 60)] + [(t2, tt), (1760, deck + 20)]
    pts = [(x, cy(x) if 0 < j < len(pts) - 1 and t1 < x < t2 else y) for j, (x, y) in enumerate(pts)]
    a = fade(t, 1, 3)
    seg(c, pts, mix(BG, CABLE, a), 6)
    for j in range(1, 16):
        x = t1 + (t2 - t1) * j / 16
        c.line([(x, cy(x)), (x, deck)], mix(BG, CABLE, a * 0.8), 2)
    for x in (t1 + 150, (t1 + t2) / 2, t2 - 150):
        for xs in (t1 + 300, (t1 + t2) / 2, t2 - 300):
            pass
    c.rect(110, deck + 20, 210, deck + 110, fill=(130, 120, 110), r=6)
    c.rect(1710, deck + 20, 1810, deck + 110, fill=(130, 120, 110), r=6)
    c.text(160, deck + 150, '锚', 'bold', 26, INK, 'mm'); c.text(1760, deck + 150, '锚', 'bold', 26, INK, 'mm')
    b = fade(t, 5, 6)
    if b > 0:
        for (x0, y0, x1, y1) in [(t1 + 120, cy(t1 + 120), t1 + 40, cy(t1 + 40) - 40), (t2 - 120, cy(t2 - 120), t2 - 40, cy(t2 - 40) - 40)]:
            c.arrow(x0, y0, x1, y1, mix(BG, NRED, b), 5, 18)
        c.text(960, cy(960) - 50, '主缆：受拉', 'bold', 28, mix(BG, NRED, b), 'mm')
    d = fade(t, 10, 11)
    if d > 0:
        for x in (t1, t2):
            c.arrow(x, tt - 90, x, tt - 10, mix(BG, FIELD, d), 6, 18)
        c.text(t1, tt - 120, '塔：受压', 'bold', 28, mix(BG, FIELD, d), 'mm')
        c.text(t2, tt - 120, '塔：受压', 'bold', 28, mix(BG, FIELD, d), 'mm')
    e = fade(t, 14, 15)
    if e > 0:
        c.arrow(260, deck - 60, 160, deck + 10, mix(BG, NRED, e), 5, 18)
        c.text(300, deck - 100, '锚：拽住缆', 'bold', 26, mix(BG, NRED, e), 'mm')
    caps(c, t, [(0, 5, '桥面挂在一根根吊索上，吊索挂在两根大主缆上'),
                (5.2, 10, '桥面的重量把主缆往下拽：主缆一直在受拉，钢最擅长扛拉力（第 62、63 集）'),
                (10.2, 14, '主缆搭在塔顶，塔被往下压'),
                (14.2, 22, '主缆的两头埋进巨大的锚里。1937 年金门大桥主跨约 1280 米')], y=1010)

def e79_sag(c, t, i):
    corner_tag(c, '第 79 集 · 绳子拉得越平，越要用力')
    c.text(60, 96, '同样挂一个重物：绳子越平，拉力越大', 'serif', 40, INK)
    sag = 260 - 230 * ease(fade(t, 2, 14))
    x0, x1, y0 = 300, 1000, 300
    mx = (x0 + x1) / 2
    c.rect(x0 - 30, y0 - 20, x0, y0 + 300, fill=MUTED); c.rect(x1, y0 - 20, x1 + 30, y0 + 300, fill=MUTED)
    c.line([(x0, y0), (mx, y0 + sag), (x1, y0)], CABLE, 5)
    c.rect(mx - 30, y0 + sag, mx + 30, y0 + sag + 60, fill=(170, 140, 100), r=4)
    W = 1.0
    half = (x1 - x0) / 2
    T = W / 2 * math.hypot(half, sag) / sag
    c.text(mx, y0 + sag + 110, f'垂度 {sag:.0f}', 'mono', 26, MUTED, 'mm')
    c.text(1150, 320, f'绳子拉力 ≈ 重物的 {T:.1f} 倍', 'bold', 34, NRED if T > 3 else INK, 'lm')
    gx0, gx1, gy0, gy1 = 1150, 1800, 420, 860
    c.line([(gx0, gy1), (gx1, gy1)], MUTED, 2); c.line([(gx0, gy0), (gx0, gy1)], MUTED, 2)
    pts = []
    for j in range(1, 101):
        s = 30 + 230 * j / 100
        Tj = W / 2 * math.hypot(half, s) / s
        pts.append((gx1 - (gx1 - gx0) * (s - 30) / 230, gy1 - (gy1 - gy0) * min(Tj, 6.5) / 6.5))
    seg(c, pts, COPPER, 4)
    px = gx1 - (gx1 - gx0) * (sag - 30) / 230
    py = gy1 - (gy1 - gy0) * min(T, 6.5) / 6.5
    c.ellipse(px, py, 12, 12, fill=NRED)
    c.text(gx0, gy1 + 34, '← 垂度大', 'sans', 22, MUTED, 'lm'); c.text(gx1, gy1 + 34, '垂度小 →', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 7, '绳子中间挂一个重物，两头固定：绳子垂得多，拉力不大'),
                (7.2, 14, '把绳子越拉越平，拉力急剧变大：永远拉不成一条直线'),
                (14.2, 22, '所以悬索桥的主缆要垂下一段：垂度和跨度的比，大多在九分之一到十一分之一左右（拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- E80 机械计算器
def digit_wheel(c, x, y, val, label, hot=False):
    c.rect(x - 70, y - 90, x + 70, y + 90, fill=SHEET, outline=SPARK if hot else MUTED, width=4 if hot else 2, r=12)
    v0 = int(math.floor(val)) % 10
    f = val - math.floor(val)
    for d_, off in ((v0, -f), ((v0 + 1) % 10, 1 - f)):
        yy = y + off * 110
        if abs(off) < 0.9:
            c.text(x, yy, str(d_), 'mono', 90, mix(BG, INK, 1 - abs(off)), 'mm')
    c.text(x, y + 130, label, 'sans', 24, MUTED, 'mm')

def e80_carry(c, t, i):
    corner_tag(c, '第 80 集 · 满十进一')
    c.text(60, 96, '37 + 48 = ?   用两个十齿轮算', 'serif', 40, INK)
    # units: start 7, add 8 between t=3..9 ; tens: start 3, +1 carry when units pass 9->0 ; then +4 between t=11..15
    u_add = 8 * ease(fade(t, 3, 9))
    units = 7 + u_add
    tens = 3 + ease(max(0.0, min(1.0, units - 9))) + 4 * ease(fade(t, 11, 15))
    digit_wheel(c, 1100, 520, units % 10, '个位', hot=3 < t < 9)
    digit_wheel(c, 900, 520, tens, '十位', hot=(9.3 <= t < 9.8) or 11 < t < 15)
    # gears below
    gear(c, 1100, 830, 90, 10, -units * 2 * math.pi / 10, COPPER)
    gear(c, 900, 830, 90, 10, -tens * 2 * math.pi / 10, COPPER)
    if 9 <= units < 10.3:
        c.arrow(1040, 780, 960, 780, NRED, 5, 16)
        c.text(1000, 740, '拨一下：进位', 'bold', 26, NRED, 'mm')
    c.text(400, 360, '先加个位：7 + 8', 'sans', 28, INK if t < 10 else MUTED, 'lm')
    c.text(400, 420, '个位转过 9→0 时，拨齿推十位一格', 'sans', 26, INK if 7 < t < 11 else MUTED, 'lm')
    c.text(400, 480, '再加十位：+4', 'sans', 28, INK if t >= 11 else MUTED, 'lm')
    a = fade(t, 16, 17)
    c.text(1400, 520, '= 85', 'mono', 80, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 7, '每一位是一个十个齿的轮子，转一格加一'),
                (7.2, 11, '个位从 7 往上转 8 格，经过 9 到 0 的那一刻，上面的拨齿把十位推一格：这就是进位'),
                (11.2, 22, '再把十位转 4 格：85。1642 年，19 岁的帕斯卡做出了这样的齿轮计算器')], y=1010)

def e80_ripple(c, t, i):
    corner_tag(c, '第 80 集 · 连续进位')
    c.text(60, 96, '999 再加 1：进位一路传过去', 'serif', 40, INK)
    base = 995
    n = base + 6 * ease(fade(t, 1, 12))
    v = n
    for k, label in enumerate(['千位', '百位', '十位', '个位']):
        p = 10 ** (3 - k)
        # each wheel position: smooth for units, carried values for higher wheels
        if k == 3:
            val = v % 10
        else:
            lower = v % p
            whole = v // p
            frac = max(0.0, (lower - (p - 1)) ) if lower > p - 1 else 0.0
            val = (whole % 10) + frac
        digit_wheel(c, 560 + k * 260, 480, val, label, hot=False)
    a = fade(t, 13, 14)
    c.rect(300, 720, 1620, 880, fill=mix(BG, SHEET, a), r=12)
    c.text(330, 770, '帕斯卡的难题：一次要推动好几个轮子，力气会越来越大', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(330, 825, '他用一个先抬起、再落下的小重锤来推进位（细节拍摄前核对）', 'sans', 26, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 7, '汽车里程表、水表，都是一排数字轮'),
                (7.2, 13, '999 加 1 的那一下：个位推十位，十位推百位，百位推千位，一个连一个'),
                (13.2, 22, '进位是机械计算器最难的地方。后来莱布尼茨又让它能做乘法')], y=1010)

CLIPS = {
 'E78_四冲程': (e78_four, 22), 'E78_压缩': (e78_compress, 22),
 'E78_片头': (titles.opening(SER12, VOL12, S12A, 6, '1876 年 · 奥托四冲程（燃烧只用动画）'), 7),
 'E78_片尾': (titles.closing(SER12, VOL12, S12A, 6, '下集：一根根钢缆，怎么吊起整座桥？'), 7),
 'E79_受力': (e79_forces, 22), 'E79_垂度': (e79_sag, 22),
 'E79_片头': (titles.opening(SER12, VOL12, S12A, 7, '1937 年 · 金门大桥'), 7),
 'E79_片尾': (titles.closing(SER12, VOL12, S12A, 7, '下集：齿轮怎么会做加法？'), 7),
 'E80_进位': (e80_carry, 22), 'E80_连续进位': (e80_ripple, 22),
 'E80_片头': (titles.opening(SER12, VOL12, S12A, 8, '1642 年 · 帕斯卡'), 7),
 'E80_片尾': (titles.closing(SER12, VOL12, S12A, 8, '下集：几个开关，怎么会「思考」？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
