"""第三十三季（第十三层：跑起来的机器）第三批：E178 潜水艇、E179 气垫船、E180 降落伞 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L
from s33a import S33A, SER33, VOL33, FLUID, CARC

WATERC = (60, 110, 170)
AIRB = (200, 230, 250)
CHUTE = (230, 120, 90)


# ---------------------------------------------------------------- E178 潜水艇
def e178_diver(c, t, i):
    corner_tag(c, '第 178 集 · 捏一下瓶子，笔帽就沉下去')
    c.text(60, 96, '笔帽里关着一小团空气，让它刚好浮着；一捏瓶子，水压变大，把空气压小、水挤进笔帽，它就变重沉下去', 'serif', 38, INK)
    sq = 0.5 - 0.5 * math.cos(t / 5.5 * math.pi) if t < 16.5 else 0
    sq = max(0, min(1, sq))
    bx = 760
    w = 160 - 30 * sq
    c.rect(bx - w, 260, bx + w, 900, outline=METAL, width=5, r=40)
    c.rect(bx - w + 6, 300, bx + w - 6, 894, fill=mix(BG, WATERC, 0.7), r=36)
    c.rect(bx - 40, 220, bx + 40, 262, fill=(80, 120, 200), r=6)
    if sq > 0.1:
        c.arrow(bx - w - 120, 600, bx - w - 10, 600, SPARK, 6, 18)
        c.arrow(bx + w + 120, 600, bx + w + 10, 600, SPARK, 6, 18)
    air = 1 - 0.35 * sq
    sink = sq > 0.45
    dy = 340 + (380 * min(1, (sq - 0.45) / 0.4) if sink else 0)
    c.rect(bx - 30, dy, bx + 30, dy + 120, outline=INK, width=4, r=6)
    c.rect(bx - 27, dy + 3, bx + 27, dy + 3 + 110 * air, fill=AIRB)
    c.ellipse(bx, dy + 140, 26, 18, fill=(200, 140, 90))
    c.rect(1300, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1580, 350, '笔帽里的空气', 'bold', 24, INK, 'mm')
    c.text(1580, 430, f'{air * 100:.0f}%', 'mono', 40, SPARK, 'mm')
    c.text(1580, 520, '沉下去' if sink else '浮着', 'bold', 34, NRED if sink else GREEN, 'mm')
    c.text(1580, 590, '（示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '笔帽口朝下，挂一小块橡皮泥，里面关着一团空气，刚好能浮在水面'),
                (7.2, 14, '用力捏瓶子：瓶里的水压变大，把笔帽里的空气压小，水挤了进来'),
                (14.2, 22, '空气少了，它排开的水就少了，比自身重量还少，就沉下去；一松手，空气胀回来，又浮上来（示意）')], y=1010)


def e178_tank(c, t, i):
    corner_tag(c, '第 178 集 · 水舱进水就沉，压缩空气把水挤出去就浮')
    c.text(60, 96, '潜水艇两侧有水舱：打开阀门让海水灌进去，艇变重，慢慢下潜；用压缩空气把水吹出去，艇变轻，又浮上来', 'serif', 38, INK)
    ph = (t % 22) / 22
    if ph < 0.45:
        fill = min(1, ph / 0.3)
    else:
        fill = max(0, 1 - (ph - 0.5) / 0.3)
    fill = max(0.0, min(1.0, fill))
    depth = 280 + 380 * fill
    c.rect(100, 260, 1820, 900, fill=mix(BG, WATERC, 0.45))
    c.line([(100, 260), (1820, 260)], (200, 220, 240), 3)
    cx = 960
    c.ellipse(cx, depth, 420, 90, fill=METAL)
    c.rect(cx - 60, depth - 150, cx + 60, depth - 70, fill=METAL, r=10)
    for sx in (-260, 160):
        x0 = cx + sx
        c.rect(x0, depth - 50, x0 + 100, depth + 50, outline=INK, width=3, r=8)
        c.rect(x0 + 3, depth + 47 - 94 * fill, x0 + 97, depth + 47, fill=FLUID)
        c.rect(x0 + 3, depth - 47, x0 + 97, depth + 47 - 94 * fill, fill=AIRB)
    c.text(cx, depth + 130, f'水舱 {fill * 100:.0f}% 是水', 'mono', 24, INK, 'mm')
    state = '下潜' if 0.05 < ph < 0.45 and fill < 1 else ('上浮' if ph > 0.5 and fill > 0 else ('潜在水下' if fill >= 1 else '浮在水面'))
    c.text(1600, 330, state, 'bold', 32, SPARK, 'mm')
    caps(c, t, [(0, 7, '浮在水面时，水舱里装满空气，整条艇比它排开的水轻'),
                (7.2, 14, '打开阀门，海水灌进水舱，艇的平均密度变得比水大，就往下潜'),
                (14.2, 22, '要上浮时，用高压空气把水舱里的水吹出去：和笔帽浮沉子一模一样（示意）')], y=1010)


# ---------------------------------------------------------------- E179 气垫船
def e179_glide(c, t, i):
    corner_tag(c, '第 179 集 · 一层气垫，摩擦几乎没了')
    c.text(60, 96, '光盘平放在桌上，推一下滑不远；套上气球放气，气从光盘底下往外跑，把光盘托起一点点，一推就滑过整张桌子', 'serif', 36, INK)
    for k, (lab, air) in enumerate((('没有气垫', False), ('有气垫', True))):
        y = 440 + k * 300
        c.line([(100, y + 20), (1820, y + 20)], LINE, 3)
        v0 = 260
        dec = 300 if not air else 15
        tt = t % 11
        x = 200 + (v0 * tt - 0.5 * dec * tt * tt if tt < v0 / dec else v0 * v0 / (2 * dec))
        x = min(x, 1700)
        lift = 8 if air else 0
        c.rect(x - 90, y - 4 - lift, x + 90, y + 6 - lift, fill=(200, 200, 215), r=4)
        if air:
            c.ellipse(x, y - 80 - lift, 60, 70, fill=CHUTE)
            c.rect(x - 8, y - 20 - lift, x + 8, y - 4 - lift, fill=METAL)
            for j in range(4):
                u = (t * 2 + j / 4) % 1
                c.ellipse(x - 90 - u * 60, y + 12, 4, 4, fill=AIRB)
                c.ellipse(x + 90 + u * 60, y + 12, 4, 4, fill=AIRB)
        c.text(160, y - 60, lab, 'bold', 26, INK, 'lm')
        c.text(1780, y - 60, f'滑出约 {(x - 200) / 10:.0f} 厘米', 'mono', 22, SPARK, 'rm')
    caps(c, t, [(0, 7, '同样轻轻一推：光盘贴着桌面，摩擦力很快让它停下'),
                (7.2, 14, '气球的气从光盘中间的孔往下吹，在光盘和桌面之间撑出一层很薄的气垫'),
                (14.2, 22, '光盘不再碰到桌面，摩擦几乎没了，就一直滑下去（距离为示意，以实测为准）')], y=1010)


def e179_lift(c, t, i):
    corner_tag(c, '第 179 集 · 压强只高一点点，面积大就托得起')
    c.text(60, 96, '气垫里的气压只比外面高一点点，可它压在船底整整一大片面积上：力 = 压强 × 面积，就托起了整条船', 'serif', 38, INK)
    cx, gy = 760, 820
    infl = min(1, t / 6)
    lift = 60 * infl
    c.rect(100, gy, 1500, gy + 60, fill=mix(BG, WATERC, 0.6))
    c.rect(cx - 400, gy - 160 - lift, cx + 400, gy - 60 - lift, fill=CARC, r=20)
    c.poly([(cx - 420, gy - 60 - lift), (cx + 420, gy - 60 - lift), (cx + 380, gy), (cx - 380, gy)], mix(BG, (60, 60, 70), 0.9))
    c.rect(cx - 360, gy - 55 - lift, cx + 360, gy - 4, fill=mix(BG, AIRB, 0.4 * infl))
    c.ellipse(cx, gy - 200 - lift, 60, 30, fill=METAL)
    for k in range(5):
        a = t * 15 + k * 2 * math.pi / 5
        c.line([(cx, gy - 200 - lift), (cx + 50 * math.cos(a), gy - 200 - lift + 15 * math.sin(a))], INK, 4)
    for k in range(9):
        x = cx - 320 + k * 80
        c.arrow(x, gy - 10, x, gy - 50 - lift, SPARK, 3, 10)
    c.text(cx, gy - 260 - lift, '风机往下吹气', 'sans', 20, MUTED, 'mm')
    c.text(cx + 440, gy - 30, '围裙', 'sans', 20, MUTED, 'lm')
    c.rect(1540, 300, 1880, 640, fill=SHEET, r=14)
    c.text(1710, 350, '气垫比大气压高', 'bold', 22, INK, 'mm')
    c.text(1710, 420, '约 1–2%', 'mono', 34, SPARK, 'mm')
    c.text(1710, 500, '× 100 平方米', 'mono', 26, INK, 'mm')
    c.text(1710, 570, '≈ 托起十几吨（示意）', 'sans', 20, GREEN, 'mm')
    caps(c, t, [(0, 7, '气垫船顶上的风机把空气往下吹，船四周有一圈柔软的「围裙」把气兜住'),
                (7.2, 14, '船底下的气压只比外面高一点点，可是船底面积很大'),
                (14.2, 22, '压强乘面积，就是一个很大的向上的力：船浮了起来，水上、泥地、沙滩都能跑（数值为示意）')], y=1010)


# ---------------------------------------------------------------- E180 降落伞
def e180_drag(c, t, i):
    corner_tag(c, '第 180 集 · 越落越快，阻力追上重力就不再加速')
    c.text(60, 96, '刚放手没有阻力，伞向下加速；越快阻力越大，阻力和重力一样大时，就以固定的速度慢慢落下', 'serif', 36, INK)
    x0, y0, x1, y1 = 900, 280, 1800, 860
    c.line([(x0, y1), (x1, y1)], LINE, 2)
    c.line([(x0, y0), (x0, y1)], LINE, 2)
    c.text((x0 + x1) / 2, y1 + 40, '时间', 'sans', 20, MUTED, 'mm')
    c.text(x0, y0 - 30, '下落速度', 'sans', 20, MUTED, 'lm')
    tm = min(1, t / 16)
    vt = 0.6
    pts = []
    for j in range(int(200 * tm) + 1):
        u = j / 200
        v = vt * math.tanh(u * 6)
        pts.append((x0 + (x1 - x0) * u, y1 - (y1 - y0) * v))
    if len(pts) > 1:
        c.line(pts, SPARK, 5)
    c.line([(x0, y1 - (y1 - y0) * vt), (x1, y1 - (y1 - y0) * vt)], mix(BG, GREEN, 0.6), 2)
    c.text(x1, y1 - (y1 - y0) * vt - 24, '终端速度', 'sans', 20, GREEN, 'rm')
    u = tm
    v = vt * math.tanh(u * 6)
    cx, cy = 420, 280 + 380 * u
    c.arc(cx, cy, 160, 90, 180, 360, CHUTE, 14)
    for s in (-1, -0.4, 0.4, 1):
        c.line([(cx + 160 * s, cy), (cx, cy + 180)], MUTED, 2)
    c.rect(cx - 20, cy + 180, cx + 20, cy + 220, fill=METAL, r=4)
    drag = v / vt
    c.arrow(cx + 230, cy + 200, cx + 230, cy + 200 - 160 * drag - 2, GREEN, 6, 16)
    c.arrow(cx + 290, cy + 40, cx + 290, cy + 200, NRED, 6, 16)
    c.text(cx + 230, cy + 230, '阻力', 'bold', 20, GREEN, 'mm')
    c.text(cx + 290, cy + 20, '重力', 'bold', 20, NRED, 'mm')
    caps(c, t, [(0, 7, '刚松手时，伞还没速度，空气阻力几乎为零，重力让它越落越快'),
                (7.2, 14, '落得越快，迎面撞上的空气越多，阻力越来越大'),
                (14.2, 22, '阻力一追上重力，合力为零，伞就不再加速，以「终端速度」匀速落下（示意）')], y=1010)


def e180_sizes(c, t, i):
    corner_tag(c, '第 180 集 · 伞越大，落得越慢')
    c.text(60, 96, '三把塑料袋伞挂同样的垫片，从同样 2 米高放下：伞面积大，同样的速度撞到的空气多，终端速度就小', 'serif', 38, INK)
    sizes = [(20, '20 厘米'), (30, '30 厘米'), (40, '40 厘米')]
    for k, (s, lab) in enumerate(sizes):
        x = 400 + k * 520
        vt = 3.2 * 20 / s
        T = 2.0 / vt + 0.2
        u = min(1, t / 3 / T) if t < 18 else 1
        y = 260 + 440 * u
        w = s * 4
        c.arc(x, y, w, w * 0.55, 180, 360, CHUTE, 10)
        for sgn in (-1, 1):
            c.line([(x + w * sgn, y), (x, y + 120)], MUTED, 2)
        c.ellipse(x, y + 130, 14, 14, fill=METAL)
        c.text(x, 900, lab, 'bold', 26, INK, 'mm')
        c.text(x, 950, f'约 {T:.1f} 秒', 'mono', 22, SPARK, 'mm')
    c.line([(150, 860), (1770, 860)], LINE, 2)
    c.text(1780, 280, '2 米', 'sans', 20, MUTED, 'rm')
    caps(c, t, [(0, 7, '边长 20、30、40 厘米的三把伞，挂一样的垫片，同时从 2 米高放手'),
                (7.2, 14, '小伞很快就落地了，大伞晃晃悠悠落得最慢'),
                (14.2, 22, '伞面积大，同样速度下阻力就大，不用落很快就能和重力平衡（时间为示意，以实测为准）')], y=1010)


CLIPS = {
 'E178_浮沉子': (e178_diver, 22), 'E178_水舱': (e178_tank, 22),
 'E178_片头': (titles.opening(SER33, VOL33, S33A, 6, '1620 年德雷贝尔造出潜水艇'), 7),
 'E178_片尾': (titles.closing(SER33, VOL33, S33A, 6, '下集：气垫船又能跑水上、又能上沙滩，它怎么浮起来？'), 7),
 'E179_滑行': (e179_glide, 22), 'E179_托力': (e179_lift, 22),
 'E179_片头': (titles.opening(SER33, VOL33, S33A, 7, '1959 年气垫船横渡英吉利海峡'), 7),
 'E179_片尾': (titles.closing(SER33, VOL33, S33A, 7, '下集：一大块布，为什么能让人从天上慢慢落下？'), 7),
 'E180_阻力': (e180_drag, 22), 'E180_大小': (e180_sizes, 22),
 'E180_片头': (titles.opening(SER33, VOL33, S33A, 8, '1797 年加纳林完成跳伞'), 7),
 'E180_片尾': (titles.closing(SER33, VOL33, S33A, 8, '下集：没有司机的汽车，怎么知道该往哪开？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
