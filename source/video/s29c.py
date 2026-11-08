"""第二十九季（第十一层：家里的机器）第三批：E158 吸尘器、E159 烟雾报警器、E160 电子秤 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import S29A, SER29, VOL29, METAL, WATER_L

AIRC = (150, 200, 240)
DUST = (180, 160, 130)
LEDC = (250, 220, 120)
SMOKE = (190, 190, 200)
WIRE = (230, 160, 80)


# ---------------------------------------------------------------- E158 吸尘器
def e158_pressure(c, t, i):
    corner_tag(c, '第 158 集 · 不是「吸」，是外面的空气在推')
    c.text(60, 96, '风扇把机器里的空气往后甩出去，机器里面的气压就比外面低；外面的大气压把空气连同灰尘一起推进吸口', 'serif', 38, INK)
    bx0, by0, bx1, by1 = 700, 360, 1400, 700
    c.rect(bx0, by0, bx1, by1, outline=METAL, width=6, r=30)
    c.rect(300, 600, bx0, 660, fill=mix(BG, METAL, 0.5), r=8)
    c.text(500, 700, '吸口', 'bold', 22, INK, 'mm')
    fx, fy = 1250, 530
    for k in range(5):
        a = t * 8 + k * 2 * math.pi / 5
        c.line([(fx, fy), (fx + 80 * math.cos(a), fy + 80 * math.sin(a))], METAL, 8)
    c.ellipse(fx, fy, 12, 12, fill=INK)
    c.text(fx, by1 + 40, '风扇（电动机带着转）', 'sans', 20, MUTED, 'mm')
    c.rect(bx0 + 40, by0 + 40, bx0 + 260, by1 - 40, outline=mix(BG, DUST, 0.8), width=3, r=10)
    c.text(bx0 + 150, by1 + 40, '集尘袋', 'sans', 20, MUTED, 'mm')
    rnd = random.Random(5)
    for k in range(26):
        s = (t * 0.4 + rnd.random()) % 1
        if s < 0.5:
            x = 120 + s / 0.5 * (bx0 - 120)
            y = 630 + 20 * math.sin(k + t)
        else:
            u = (s - 0.5) / 0.5
            x = bx0 + u * (bx1 - bx0 + 300)
            y = 530 + 60 * math.sin(k)
        c.ellipse(x, y, 5, 5, fill=AIRC)
    for k in range(10):
        s = (t * 0.3 + k * 0.1) % 1
        x = 120 + min(s / 0.6, 1) * (bx0 + 120 - 120)
        c.ellipse(x, 630 + 10 * math.sin(k), 9, 7, fill=DUST)
    c.text(1050, 290, '里面：气压低一点', 'bold', 24, SPARK, 'mm')
    c.text(200, 520, '外面：大气压', 'bold', 24, INK, 'mm')
    for k in range(4):
        c.arrow(140 + k * 40, 560, 220 + k * 40, 610, mix(BG, INK, 0.6), 3, 10)
    c.arrow(bx1, 530, bx1 + 200, 530, AIRC, 4, 14)
    c.text(bx1 + 220, 530, '排气', 'sans', 20, AIRC, 'lm')
    caps(c, t, [(0, 7, '吸尘器里有一个电动机带着的风扇，转得飞快，把机器里的空气往后甩出去'),
                (7.2, 14, '里面的空气少了，气压就比外面低一点；外面的大气压一直压着，就把空气从吸口推进来'),
                (14.2, 22, '空气冲进来的时候顺便带走地上的灰尘，灰尘被集尘袋拦下，干净的空气从后面排出去（示意）')], y=1010)


def e158_distance(c, t, i):
    corner_tag(c, '第 158 集 · 离开几厘米，吸力就弱得很快')
    c.text(60, 96, '空气从四面八方涌向吸口，离得越远风越小，大致和距离的平方成反比，所以要贴近了吸', 'serif', 36, INK)
    cx, cy = 500, 560
    c.rect(cx - 30, cy - 200, cx + 30, cy - 20, fill=mix(BG, METAL, 0.6), r=8)
    for k in range(40):
        a = math.pi * (0.1 + 0.8 * (k % 20) / 19) + (math.pi if k >= 20 else 0) * 0
        r0 = 380
        s = (t * 0.5 + k * 0.05) % 1
        r = r0 * (1 - s) ** 0.5
        x = cx + r * math.cos(a)
        y = cy - 20 + r * math.sin(a) * 0.9
        c.ellipse(x, y, 5, 5, fill=mix(BG, AIRC, 0.4 + 0.6 * (1 - r / r0)))
    for d in (1, 3, 5, 10):
        r = 40 * d
        c.arc(cx, cy - 20, r, r * 0.9, 10, 170, mix(BG, LINE, 0.7), 1)
        c.text(cx + r * 0.7, cy - 20 + r * 0.65, f'{d} 厘米', 'mono', 16, MUTED, 'mm')
    gx0, gy0 = 1060, 840
    c.line([(gx0, gy0), (1820, gy0)], LINE, 2)
    grow = min(1, t / 8)
    for k, d in enumerate((1, 3, 5, 10)):
        v = 1 / d ** 2
        x = gx0 + 40 + k * 190
        h = 460 * v * grow
        c.rect(x, gy0 - h, x + 120, gy0, fill=mix(AIRC, GREEN, 1 - k / 3), r=6)
        c.text(x + 60, gy0 + 34, f'{d} 厘米', 'bold', 22, INK, 'mm')
        c.text(x + 60, gy0 - h - 24, f'{v * 100:.0f}%', 'mono', 20, INK, 'mm')
    c.text(1440, 300, '风速（以 1 厘米处为 100%，示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '吸口周围的空气，是从四面八方一起往里涌的'),
                (7.2, 14, '离吸口越远，同样多的空气分摊到更大的一片，那里的风就越小'),
                (14.2, 22, '离开 3 厘米只剩约十分之一，10 厘米只剩百分之一：所以吸尘器要贴着地面吸（比例为理想估算，以实测为准）')], y=1010)


# ---------------------------------------------------------------- E159 烟雾报警器
def e159_chamber(c, t, i):
    corner_tag(c, '第 159 集 · 暗室里，灯不对着接收器')
    c.text(60, 96, '报警器里有个小暗室：灯朝前照，接收器在旁边不对着灯；烟一进来把光散过去，它就报警', 'serif', 34, INK)
    smoke = min(1, max(0, (t - 8) / 6))
    cx, cy, R = 760, 560, 300
    c.ellipse(cx, cy, R, R, fill=(30, 30, 36))
    for k in range(12):
        a = k * math.pi / 6
        c.line([(cx + (R - 30) * math.cos(a), cy + (R - 30) * math.sin(a)), (cx + R * math.cos(a + 0.2), cy + R * math.sin(a + 0.2))], (60, 60, 70), 6)
    lx, ly = cx - 220, cy
    c.rect(lx - 30, ly - 20, lx + 10, ly + 20, fill=LEDC, r=4)
    c.text(lx - 10, ly + 50, '灯（红外 LED）', 'sans', 18, MUTED, 'mm')
    c.line([(lx + 10, ly), (cx + 220, ly)], mix((30, 30, 36), LEDC, 0.35 + 0.4 * smoke), 6)
    dx, dy = cx, cy - 220
    c.rect(dx - 20, dy - 30, dx + 20, dy + 10, fill=(120, 180, 240), r=4)
    c.text(dx + 40, dy - 10, '接收器', 'sans', 18, MUTED, 'lm')
    rnd = random.Random(int(t * 4))
    hits = 0
    if smoke > 0:
        for k in range(int(40 * smoke)):
            px = cx - 150 + rnd.random() * 300
            py = cy + rnd.uniform(-30, 30)
            c.ellipse(px, py, 6, 6, fill=SMOKE)
            if rnd.random() < 0.3:
                c.line([(px, py), (dx, dy + 10)], mix((30, 30, 36), LEDC, 0.6), 2)
                hits += 1
    alarm = hits > 3
    c.rect(1240, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1550, 340, '接收器收到的光', 'bold', 24, INK, 'mm')
    c.rect(1300, 400, 1300 + 500 * min(1, hits / 12), 450, fill=NRED if alarm else (120, 180, 240), r=6)
    c.text(1550, 520, '嘀——嘀——！' if alarm else '安静', 'bold', 36, NRED if alarm else MUTED, 'mm')
    caps(c, t, [(0, 7, '光电式烟雾报警器里有一个四周带挡板的小暗室，外面的光进不来，烟可以钻进来'),
                (7.2, 14, '一侧的灯一直往前照，接收器装在旁边、不对着灯：没有烟时，它几乎收不到光'),
                (14.2, 22, '烟粒子一飘进来，把光往四面八方散开，一部分就打到了接收器上：光一多，电路就拉响警报（示意）')], y=1010)


def e159_milk(c, t, i):
    corner_tag(c, '第 159 集 · 从侧面看见光的路')
    c.text(60, 96, '手电筒从侧面照进清水，从旁边几乎看不见光路；滴几滴牛奶，水里的小颗粒把光散到旁边，一道光柱就出现了', 'serif', 36, INK)
    drops = int(min(10, t / 2))
    for k, (lab, dd) in enumerate((('清水', 0), (f'滴了 {drops} 滴牛奶', drops))):
        x0 = 300 + k * 720
        c.rect(x0, 320, x0 + 420, 820, outline=LINE, width=4, r=16)
        c.rect(x0 + 4, 380, x0 + 416, 816, fill=mix(BG, (240, 240, 245), 0.03 + 0.012 * dd), r=12)
        c.rect(x0 - 160, 560, x0 - 40, 620, fill=(90, 90, 100), r=8)
        c.ellipse(x0 - 40, 590, 14, 24, fill=LEDC)
        vis = 0.05 + 0.08 * dd
        c.rect(x0 + 4, 570, x0 + 416, 610, fill=mix(BG, LEDC, min(0.9, vis)))
        c.text(x0 + 210, 870, lab, 'bold', 26, INK, 'mm')
    c.text(960, 940, '眼睛在旁边，看到的是被颗粒散射到旁边的光（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '关上灯，用手电筒从侧面照一杯清水：光直直地穿过去，从旁边几乎看不见'),
                (7.2, 14, '滴几滴牛奶搅匀：牛奶里有很多微小的油滴和蛋白颗粒'),
                (14.2, 22, '颗粒把光往四面八方散开，从旁边就能看见一道光柱：烟里的小颗粒，在报警器里干的正是这件事')], y=1010)


# ---------------------------------------------------------------- E160 电子秤
def e160_bend(c, t, i):
    corner_tag(c, '第 160 集 · 放上东西，金属会弯一点点')
    c.text(60, 96, '尺子伸出桌边，挂上硬币就往下弯，挂得越多弯得越多、基本成正比；秤里的金属也这样弯', 'serif', 36, INK)
    n = int(min(20, t * 1.2)) // 5 * 5
    x0, y0 = 260, 400
    c.rect(100, y0, x0 + 40, y0 + 200, fill=(130, 100, 70))
    c.rect(x0 - 160, y0 - 50, x0 + 20, y0, fill=(120, 140, 200), r=4)
    c.text(x0 - 70, y0 - 25, '书压住', 'sans', 18, INK, 'mm')
    L = 760
    k_def = 4.0
    d = n * k_def
    pts = []
    for j in range(41):
        u = j / 40
        pts.append((x0 + L * u, y0 - 4 + d * (3 * u * u - u ** 3) / 2))
    c.line(pts, (220, 220, 230), 10)
    ex, ey = pts[-1]
    c.line([(ex, ey), (ex, ey + 60)], METAL, 2)
    c.rect(ex - 30, ey + 60, ex + 30, ey + 100, fill=mix(BG, (200, 180, 90), 0.8), r=6)
    c.text(ex, ey + 80, f'{n} 枚', 'bold', 18, INK, 'mm')
    seg(c, [(x0 + L - 40, y0 - 4), (x0 + L + 80, y0 - 4)], MUTED, 1)
    c.text(x0 + L + 90, y0 + d / 2, f'下垂 {d / 4:.0f} 毫米（示意）', 'mono', 20, SPARK, 'lm')
    gx0, gy0 = 1240, 900
    c.line([(gx0, gy0), (1820, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, 620)], LINE, 2)
    for m in (0, 5, 10, 15, 20):
        x = gx0 + m * 26
        y = gy0 - m * 12
        if m <= n:
            c.ellipse(x, y, 8, 8, fill=SPARK)
    if n > 0:
        c.line([(gx0, gy0), (gx0 + n * 26, gy0 - n * 12)], mix(BG, SPARK, 0.6), 2)
    c.text(1530, 940, '硬币数 → 下垂', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '30 厘米塑料尺伸出桌边，一头用书压住，尺尖挂一个小袋，5 枚、10 枚……地加硬币'),
                (7.2, 14, '每加 5 枚，尺尖就多往下垂差不多一样多：画成图，是一条直线'),
                (14.2, 22, '电子秤秤盘下面有一块金属，放上东西它也会弯，只是弯得小到肉眼看不出（示意）')], y=1010)


def e160_gauge(c, t, i):
    corner_tag(c, '第 160 集 · 应变片：被拉长一点，电阻就变一点')
    c.text(60, 96, '金属块上贴着折了很多道的细金属丝：金属一弯，细丝被拉长，电阻大一点点，再换算成克', 'serif', 34, INK)
    load = 0.5 - 0.5 * math.cos(t / 11 * 2 * math.pi)
    cx, cy = 700, 560
    bend = 30 * load
    pts_top = [(cx - 420 + 840 * j / 40, cy - 60 + bend * (1 - ((j - 20) / 20) ** 2)) for j in range(41)]
    pts_bot = [(x, y + 120) for (x, y) in pts_top]
    c.poly(pts_top + pts_bot[::-1], mix(METAL, BG, 0.2))
    c.rect(cx - 60, cy - 160 + bend, cx + 60, cy - 80 + bend, fill=(200, 180, 90), r=6)
    c.text(cx, cy - 190 + bend, '放上的东西', 'sans', 20, INK, 'mm')
    gx0, gx1 = cx - 160, cx + 160
    gy = cy + 60 + bend
    stretch = 1 + 0.06 * load
    for k in range(9):
        x = cx + (k - 4) * 34 * stretch
        c.line([(x, gy - 20), (x, gy + 20)], WIRE, 3)
        if k < 8:
            yy = gy + 20 if k % 2 == 0 else gy - 20
            c.line([(x, yy), (x + 34 * stretch, yy)], WIRE, 3)
    c.text(cx, gy + 60, '应变片（贴在底面，被拉长）', 'sans', 20, WIRE, 'mm')
    R0 = 350.0
    R = R0 * (1 + 0.002 * load)
    c.rect(1280, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1570, 340, '应变片电阻', 'bold', 24, INK, 'mm')
    c.text(1570, 410, f'{R:.2f} 欧', 'mono', 32, SPARK, 'mm')
    c.text(1570, 470, '只变了千分之几', 'sans', 20, MUTED, 'mm')
    c.text(1570, 560, f'显示：{load * 500:.0f} 克', 'mono', 32, GREEN, 'mm')
    c.text(1570, 640, '（数值为示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '电子秤秤盘下面是一块特别设计的金属块，上面贴着一片薄薄的应变片'),
                (7.2, 14, '放上东西，金属块弯一点点，贴在上面的细金属丝跟着被拉长、变细，电阻就大了一点点'),
                (14.2, 22, '这点变化只有千分之几，电路把它放大、换算，屏幕上就跳出了克数（数值拍摄前核对）')], y=1010)


CLIPS = {
 'E158_气压差': (e158_pressure, 22), 'E158_距离': (e158_distance, 22),
 'E158_片头': (titles.opening(SER29, VOL29, S29A, 6, '1901 年布斯发明电动吸尘器'), 7),
 'E158_片尾': (titles.closing(SER29, VOL29, S29A, 6, '下集：屋里冒烟时，那个小圆盒怎么「看见」烟？'), 7),
 'E159_暗室': (e159_chamber, 22), 'E159_牛奶水': (e159_milk, 22),
 'E159_片头': (titles.opening(SER29, VOL29, S29A, 7, '1960 年代家用烟雾报警器出现'), 7),
 'E159_片尾': (titles.closing(SER29, VOL29, S29A, 7, '下集：电子秤里没有秤砣，为什么一放东西就知道多重？'), 7),
 'E160_弯曲': (e160_bend, 22), 'E160_应变片': (e160_gauge, 22),
 'E160_片头': (titles.opening(SER29, VOL29, S29A, 8, '1938 年发明电阻应变片'), 7),
 'E160_片尾': (titles.closing(SER29, VOL29, S29A, 8, '下集：扁扁的小圆盘，怎么自己把一屋子扫遍？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
