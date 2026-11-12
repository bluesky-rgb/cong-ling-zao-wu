"""第四十二季（古法解密 18.0）第二批：B183 搓衣板、B184 汤婆子、B185 二胡 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s42a import SB42, VOL42

CLOTH = (120, 160, 210)
DIRT = (150, 120, 80)
HOT = (230, 110, 70)
COLD = (90, 140, 220)
BRASS = (200, 160, 80)
STR = (220, 220, 230)


# ---------------------------------------------------------------- B183 搓衣板
def b183_ridges(c, t, i):
    corner_tag(c, 'B183 · 一道道棱，压紧又松开')
    c.text(60, 96, '布在一道道棱上来回搓：压在棱尖上被挤紧，落进棱缝里又松开；纤维反复弯折挤动，夹在里面的污垢就被搓松', 'serif', 34, INK)
    y0 = 700
    pts = [(160, y0 + 120)]
    for k in range(24):
        x = 160 + k * 56
        pts += [(x, y0), (x + 28, y0 - 40), (x + 56, y0)]
    pts += [(160 + 24 * 56, y0 + 120)]
    c.poly(pts, mix(BG, WOOD, 0.95))
    off = 100 * math.sin(t * 2)
    cl = []
    for k in range(60):
        x = 300 + k * 16 + off
        rel = ((x - 160) % 56) / 56
        yy = y0 - 40 * (1 - abs(rel - 0.5) * 2) - 14
        cl.append((x, yy))
    c.line(cl, CLOTH, 14)
    r = random.Random(int(t * 3))
    for k in range(25):
        x = 300 + r.uniform(0, 960) + off
        c.ellipse(x, y0 - 70 - r.uniform(0, 80), 5, 5, fill=DIRT)
    for k in range(6):
        x = 400 + k * 160
        c.line([(x, y0 - 10), (x - 20, y0 + 60)], mix(BG, WATER_L, 0.8), 3)
    c.text(1540, y0 + 40, '水从棱缝里\n带走污垢', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '平板上搓，布只是平平地滑来滑去，纤维挤不动'),
                (7.2, 14, '有棱的板上，布被棱尖顶起来又落进缝里，一下下被弯折、挤压'),
                (14.2, 22, '纤维之间来回挤动，污垢被搓松，水顺着棱缝把它们带走（示意）')], y=1010)


def b183_drag(c, t, i):
    corner_tag(c, 'B183 · 有棱的板摩擦更大')
    c.text(60, 96, '同一块湿布，在平板上一拉就滑过去；在有棱的板上，布被一道道棱卡住，要用更大的力才拉得动', 'serif', 36, INK)
    for j, (lab, ridge, f) in enumerate([('平木板：拉力小', False, 1.0), ('搓衣板：拉力大', True, 2.4)]):
        cy = 400 + j * 300
        x0, x1 = 200, 1300
        if ridge:
            pts = [(x0, cy + 80)]
            for k in range(20):
                x = x0 + k * 55
                pts += [(x, cy), (x + 27, cy - 30), (x + 55, cy)]
            pts += [(x1, cy + 80)]
            c.poly(pts, mix(BG, WOOD, 0.95))
        else:
            c.rect(x0, cy, x1, cy + 80, fill=mix(BG, WOOD, 0.95))
        p = (t % 6) / 6
        bx = x0 + 100 + p * 800
        c.rect(bx - 80, cy - 70, bx + 80, cy - (30 if ridge else 0), fill=CLOTH, r=10)
        c.line([(bx + 80, cy - 40), (bx + 250, cy - 40)], INK, 3)
        c.rect(bx + 250, cy - 70, bx + 300, cy - 10, fill=mix(BG, (90, 90, 100), 1.0), r=8)
        c.rect(1380, cy - 60, 1380 + f * 150, cy - 20, fill=NRED if ridge else GREEN, r=8)
        c.text(1380, cy + 20, lab, 'bold', 24, INK, 'lm')
    c.text(1600, 900, '读数以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '用行李秤钩住一块叠好的湿布，在两块板上慢慢拉'),
                (7.2, 14, '在有棱的板上，布要不停地爬上棱、再滑下去，被卡得更紧'),
                (14.2, 22, '摩擦力大，说明布和板之间「搓」得更狠：这正是洗衣要的（示意）')], y=1010)


# ---------------------------------------------------------------- B184 汤婆子
def b184_heat(c, t, i):
    corner_tag(c, 'B184 · 水能存很多热')
    c.text(60, 96, '同样重、同样升高 1 ℃：水要吸的热，是铜的约 10 倍、石头的约 5 倍；所以一壶热水存的热特别多，能慢慢放很久', 'serif', 33, INK)
    items = [('水', 4.18, COLD), ('石头', 0.84, (150, 150, 155)), ('铜', 0.39, BRASS)]
    p = min(1.0, t / 10)
    for k, (lab, cval, col) in enumerate(items):
        y = 360 + k * 150
        c.text(260, y, lab, 'bold', 30, INK, 'rm')
        w = cval / 4.18 * 1100 * p
        c.rect(300, y - 40, 300 + w, y + 40, fill=mix(BG, col, 0.9), r=10)
        c.text(320 + w, y, f'{cval} 焦/克·℃', 'mono', 24, INK, 'lm')
    c.text(960, 860, '每克升高 1 ℃ 要吸收的热（比热容，以资料为准）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '给东西加热，有的一下就烫，有的要吸很多热才热起来'),
                (7.2, 14, '水就是「要吸很多热」的那种：同样重，它存的热比铜、比石头多得多'),
                (14.2, 22, '反过来，它凉下去时也要放出很多热：一壶热水能慢慢暖一整夜')], y=1010)


def b184_wrap(c, t, i):
    corner_tag(c, 'B184 · 包上布，凉得慢')
    c.text(60, 96, '三个瓶子装 50 ℃ 的温水：裸放的大瓶、包毛巾的大瓶、裸放的小瓶，一小时后谁最暖？', 'serif', 36, INK)
    x0, y0, W, H = 200, 260, 1100, 560
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 40, '时间（分钟）', 'sans', 22, MUTED, 'mm')
    for k in range(7):
        x = x0 + 40 + k * (W - 80) / 6
        c.text(x, y0 + H - 10, str(k * 10), 'mono', 16, MUTED, 'mm')
    tn = min(1.0, t / 14)
    for col, k_, lab in [(COLD, 0.008, '小瓶裸放'), (SPARK, 0.004, '大瓶裸放'), (GREEN, 0.0018, '大瓶包毛巾')]:
        pts = []
        for m in range(61):
            if m / 60 > tn:
                break
            T = 22 + 28 * math.exp(-k_ * m * 2.5)
            pts.append((x0 + 40 + m / 60 * (W - 80), y0 + H - 40 - (T - 20) / 32 * (H - 80)))
        if len(pts) > 1:
            c.line(pts, col, 5)
            c.text(pts[-1][0] + 10, pts[-1][1], lab, 'bold', 20, col, 'lm')
    c.text(x0 + 20, y0 + 30, '温度（℃，示意）', 'sans', 20, MUTED, 'lm')
    caps(c, t, [(0, 7, '热总是从热的地方往冷的地方跑，瓶子的热一点点散进空气里'),
                (7.2, 14, '毛巾里有很多空气，空气传热很慢，把热「捂」住了'),
                (14.2, 22, '大瓶水多、存的热多，比小瓶凉得慢：温水不超过 50 ℃（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B185 二胡
def b185_stickslip(c, t, i):
    corner_tag(c, 'B185 · 一粘一滑，不停地推')
    c.text(60, 96, '弓毛抹了松香，和弦之间时粘时滑：粘住时把弦带着走，带到一定程度弦「啪」地滑开弹回，再被粘住……每秒几百次', 'serif', 33, INK)
    x0, x1, y = 200, 1500, 520
    ph = (t * 1.2) % 1
    if ph < 0.8:
        d = 80 * ph / 0.8
        stick = True
    else:
        d = 80 * (1 - (ph - 0.8) / 0.2)
        stick = False
    mx = (x0 + x1) / 2
    c.line([(x0, y), (mx, y + d), (x1, y)], STR, 4)
    c.ellipse(x0, y, 10, 10, fill=INK)
    c.ellipse(x1, y, 10, 10, fill=INK)
    bx = mx
    c.rect(bx - 300, y + d + 8, bx + 300, y + d + 24, fill=mix(BG, (230, 225, 210), 1.0), r=6)
    c.rect(bx - 320, y + d + 24, bx + 320, y + d + 40, fill=mix(BG, WOOD, 1.0), r=6)
    c.arrow(bx + 380, y + 120, bx + 380, y + 220, SPARK, 6, 18)
    c.text(bx + 420, y + 170, '弓一直往下拉', 'sans', 22, MUTED, 'lm')
    c.text(mx, y - 80, '粘住：弦被带着走' if stick else '滑开：弦弹回去', 'bold', 28, SPARK if stick else GREEN, 'mm')
    x0g, y0g = 300, 820
    pts = []
    for k in range(200):
        s = k / 200 * 4
        p2 = s % 1
        v = p2 / 0.8 if p2 < 0.8 else 1 - (p2 - 0.8) / 0.2
        pts.append((x0g + k * 6, y0g - v * 80))
    c.line(pts, mix(BG, SPARK, 0.8), 3)
    c.text(x0g, y0g + 30, '弦的位置随时间：慢慢被带走，一下子弹回（锯齿形）', 'sans', 20, MUTED, 'lm')
    caps(c, t, [(0, 7, '静止的时候粘得牢，滑动起来摩擦就变小：松香让这个差别特别大'),
                (7.2, 14, '弓一直拉，弦被粘住带走；弦的弹力越来越大，终于挣脱，弹回去，又被粘住'),
                (14.2, 22, '一粘一滑不停地给弦补充能量，所以拉弓的声音能一直响下去（示意）')], y=1010)


def b185_tension(c, t, i):
    corner_tag(c, 'B185 · 拧紧琴轴，音变高')
    c.text(60, 96, '二胡上面两个琴轴一拧，弦就绷得更紧：越紧，弦振得越快，音越高；手指按住弦，振动的那一段变短，音也变高', 'serif', 33, INK)
    for j, (lab, tens) in enumerate([('松：振得慢，音低', 0.5), ('紧：振得快，音高', 1.0)]):
        cy = 380 + j * 320
        x0, x1 = 240, 1400
        f = 2 + 4 * tens
        amp = 40 * (0.6 + 0.4 * abs(math.sin(t * 0.5)))
        pts = [(x0 + k * (x1 - x0) / 80, cy + amp * math.sin(math.pi * k / 80) * math.sin(t * f * 6)) for k in range(81)]
        c.line(pts, STR, 4)
        c.ellipse(x0, cy, 12, 12, fill=INK)
        c.rect(x1, cy - 20, x1 + 40, cy + 20, fill=mix(BG, WOOD, 1.0), r=6)
        c.line([(x1 + 20, cy), (x1 + 20 + 30 * math.cos(t * tens), cy + 30 * math.sin(t * tens))], INK, 6)
        c.text(x1 + 80, cy, lab, 'bold', 24, INK, 'lm')
        c.text(x1 + 80, cy + 40, f'约 {220 * (1 + tens):.0f} 赫兹（示意）', 'mono', 20, SPARK, 'lm')
    caps(c, t, [(0, 7, '弦被拉得越紧，回弹的力越大，来回振动得越快'),
                (7.2, 14, '每秒振动的次数越多，我们听到的音就越高'),
                (14.2, 22, '用调音器 App 读一读：橡皮筋拉紧一点，音高就往上跑（以实测为准）')], y=1010)


CLIPS = {
 'B183_棱': (b183_ridges, 22), 'B183_拉力': (b183_drag, 22),
 'B183_片头': (titles.opening(BSER, VOL42, SB42, 3, '清代至民国家家户户用木搓衣板'), 7),
 'B183_片尾': (titles.closing(BSER, VOL42, SB42, 3, '下集：一壶热水，为什么能暖一整夜？'), 7),
 'B184_存热': (b184_heat, 22), 'B184_包布': (b184_wrap, 22),
 'B184_片头': (titles.opening(BSER, VOL42, SB42, 4, '宋代已有汤婆子用来暖被窝'), 7),
 'B184_片尾': (titles.closing(BSER, VOL42, SB42, 4, '下集：二胡的弓一拉，为什么能一直响？'), 7),
 'B185_粘滑': (b185_stickslip, 22), 'B185_松紧': (b185_tension, 22),
 'B185_片头': (titles.opening(BSER, VOL42, SB42, 5, '唐宋时已有奚琴，后发展为二胡'), 7),
 'B185_片尾': (titles.closing(BSER, VOL42, SB42, 5, '下集：插在峭壁上的木梁，怎么托住人？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
