"""第四十六季（古法解密 20.0）第三批：B206 轿子、B207 戽斗、B208 竹篙 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s46a import SB46, VOL46, ROD

SEDAN = (180, 60, 50)
PERSON = (230, 180, 140)
BUCKET = (150, 120, 80)
BOATC = (170, 120, 70)


def _porter(c, x, y, col=PERSON):
    c.ellipse(x, y - 150, 24, 24, fill=mix(BG, col, 1.0))
    c.rect(x - 18, y - 126, x + 18, y - 40, fill=mix(BG, (90, 110, 150), 1.0), r=8)
    c.line([(x - 8, y - 40), (x - 14, y)], INK, 6)
    c.line([(x + 8, y - 40), (x + 14, y)], INK, 6)


# ---------------------------------------------------------------- B206 轿子
def b206_share(c, t, i):
    corner_tag(c, 'B206 · 离谁近，谁担得多')
    c.text(60, 96, '轿杆就是一根杠杆：坐轿的人在正中间，前后两人各担一半；往前挪一点，离前面的轿夫近了，前面的人就担得更多', 'serif', 36, INK)
    gy = 760
    x0, x1 = 360, 1560
    pos = 0.5 + 0.25 * math.sin(t * 0.5)
    _porter(c, x0, gy)
    _porter(c, x1, gy)
    c.line([(x0, gy - 120), (x1, gy - 120)], mix(BG, ROD, 1.0), 12)
    cx = x0 + (x1 - x0) * pos
    c.rect(cx - 110, gy - 330, cx + 110, gy - 126, fill=mix(BG, SEDAN, 1.0), r=14)
    c.ellipse(cx, gy - 250, 22, 22, fill=mix(BG, PERSON, 1.0))
    front = pos
    back = 1 - pos
    for x, f, lab in [(x0, back, '后'), (x1, front, '前')]:
        h = 260 * f
        c.rect(x - 30, 260, x + 30, 260 + h, fill=SPARK, r=6)
        c.text(x, 230, f'{lab}：{f * 100:.0f}%', 'bold', 26, SPARK, 'mm')
    c.text(960, 880, '黄条：各自扛的那一份重量（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '扫帚杆两头各挂一个行李秤，两个人提着；米袋挂在正中间，两个秤读数差不多'),
                (7.2, 14, '米袋往前挪，前面的秤读数变大、后面的变小'),
                (14.2, 22, '重物离谁近，谁就担得多：和杆秤、扁担是同一个道理（以实测为准）')], y=1010)


def b206_slope(c, t, i):
    corner_tag(c, 'B206 · 上坡时，后面的人更累')
    c.text(60, 96, '上坡时轿子斜了，坐轿人的重心往下坡一侧偏，离后面（低处）的轿夫更近：后面的人就担得更多', 'serif', 36, INK)
    ang = math.radians(14 * min(1.0, t / 8))
    gx0, gy0 = 200, 860
    gx1, gy1 = 1720, 860 - 1520 * math.tan(ang)
    c.poly([(gx0, gy0), (gx1, gy1), (gx1, 960), (gx0, 960)], mix(BG, (110, 120, 85), 0.8))
    L = 1000
    bx = 460
    by = gy0 - (bx - gx0) * math.tan(ang)
    fx = bx + L * math.cos(ang)
    fy = by - L * math.sin(ang)
    _porter(c, bx, by)
    _porter(c, fx, fy)
    hb, hf = (bx, by - 120), (fx, fy - 120)
    c.line([hb, hf], mix(BG, ROD, 1.0), 12)
    mx, my = (hb[0] + hf[0]) / 2, (hb[1] + hf[1]) / 2
    c.rect(mx - 100, my - 210, mx + 100, my - 6, fill=mix(BG, SEDAN, 1.0), r=14)
    gxc = mx - 160 * math.sin(ang) * 1.6
    c.line([(gxc, my - 120), (gxc, my + 140)], mix(BG, NRED, 0.8), 3)
    c.ellipse(gxc, my - 120, 10, 10, fill=NRED)
    c.text(gxc - 20, my + 170, '重心往低处偏', 'sans', 22, NRED, 'rm')
    share_b = 0.5 + 0.8 * math.sin(ang)
    c.text(bx, 300, f'后：{share_b * 100:.0f}%', 'bold', 28, SPARK, 'mm')
    c.text(fx, 300, f'前：{(1 - share_b) * 100:.0f}%', 'bold', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '平地上，坐在中间的人前后各担一半'),
                (7.2, 14, '一上坡，轿子倾斜，坐轿的人比轿杆高，重心就往低处偏'),
                (14.2, 22, '让后面的人把秤放低 20 厘米，读数就往后面那个秤上跑（数值示意，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B207 戽斗
def b207_swing(c, t, i):
    corner_tag(c, 'B207 · 两根绳，一个摆')
    c.text(60, 96, '两人各拉一根绳子把小桶吊在中间：一放，桶落进低处的水里舀满；一起往上荡，桶口一歪，水泼进高处的田', 'serif', 35, INK)
    lx, rx, hy = 300, 1620, 360
    low_y, high_y = 860, 620
    c.rect(400, low_y, 1000, 960, fill=mix(BG, WATER, 0.7))
    c.text(700, low_y + 50, '低处的水渠', 'sans', 22, BG, 'mm')
    c.rect(1100, high_y, 1600, 960, fill=mix(BG, (110, 140, 80), 1.0))
    c.text(1350, high_y + 50, '高处的田', 'sans', 22, BG, 'mm')
    _porter(c, lx - 60, high_y + 160)
    _porter(c, rx + 60, high_y + 160)
    T = 4.0
    ph = (t % T) / T
    a = math.cos(2 * math.pi * ph)
    bx = 800 + 300 * (-a)
    by = 780 - 240 * max(0.0, -a) - 40 * (1 - abs(a))
    if a > 0.6:
        by = low_y - 10
        bx = 700
    c.line([(lx, hy + 80), (bx - 30, by - 30)], mix(BG, MUTED, 1.0), 3)
    c.line([(rx, hy + 80), (bx + 30, by - 30)], mix(BG, MUTED, 1.0), 3)
    tilt = 0.6 if bx > 1050 else 0.0
    c.poly([(bx - 40, by - 30), (bx + 40, by - 30 - 40 * tilt), (bx + 30, by + 30), (bx - 30, by + 30)], mix(BG, BUCKET, 1.0))
    if tilt > 0:
        for k in range(6):
            c.ellipse(bx + 50 + k * 14, by - 20 + k * 12, 6, 6, fill=WATER_L)
    lab = '一放：舀水' if a > 0.3 else ('一起拉：荡上去' if ph < 0.75 else '一歪：倒进田里')
    c.text(960, 300, lab, 'bold', 30, SPARK, 'mm')
    caps(c, t, [(0, 7, '戽斗是一只小桶，两边各系两根绳子，两个人面对面站在水渠两岸'),
                (7.2, 14, '一起放松，桶落进水里；一起往上拉，桶像秋千一样荡起来'),
                (14.2, 22, '荡到田埂上方，一边稍松，桶口一歪，水就泼进田里（示意）')], y=1010)


def b207_sync(c, t, i):
    corner_tag(c, 'B207 · 合拍才送得上去')
    c.text(60, 96, '两个人的拉和放要对上：同时放、同时拉，桶才能顺着摆动荡起来；一个拉一个放，桶就在中间乱晃，水全洒在路上', 'serif', 36, INK)
    for j, (lab, sync) in enumerate([('合拍：一起放、一起拉', True), ('不合拍：你拉我放', False)]):
        oy = 330 + j * 320
        x0 = 260
        for k in range(16):
            x = x0 + k * 80
            ph1 = (t * 2 + k * 0.6) % (2 * math.pi)
            ph2 = ph1 if sync else ph1 + math.pi * 0.9
            c.rect(x - 12, oy - 40 * math.sin(ph1) - 10, x + 12, oy - 40 * math.sin(ph1) + 10, fill=mix(BG, SPARK, 0.8), r=4)
            c.rect(x - 12, oy + 70 - 40 * math.sin(ph2) - 10, x + 12, oy + 70 - 40 * math.sin(ph2) + 10, fill=mix(BG, (120, 180, 240), 0.8), r=4)
        c.text(x0 - 30, oy, '甲', 'bold', 22, SPARK, 'rm')
        c.text(x0 - 30, oy + 70, '乙', 'bold', 22, (120, 180, 240), 'rm')
        vol = 1.0 if sync else 0.25
        c.rect(1620, oy - 20, 1620 + 220 * vol, oy + 90, fill=mix(BG, WATER, 0.85), r=8)
        c.text(1730, oy + 130, lab, 'bold', 22, GREEN if sync else NRED, 'mm')
    c.text(960, 900, '右边蓝块：1 分钟送上去的水（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '两个人喊着「一放、二拉」，1 分钟能送上去一大盘水'),
                (7.2, 14, '不喊口令各拉各的，桶东摇西摆，舀不满也倒不准'),
                (14.2, 22, '一个人双手各拉一根也能做，但很快就累：戽斗本来就是两个人的活（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B208 竹篙
def b208_push(c, t, i):
    corner_tag(c, 'B208 · 推河底，走的是船')
    c.text(60, 96, '篙尖戳住河底，人用力把篙往后推：河底推不动，就把篙往前推回来，这股力经过人的手脚传给船，船就往前走', 'serif', 36, INK)
    wy, by = 520, 880
    c.rect(0, wy, W, by, fill=mix(BG, WATER, 0.45))
    c.rect(0, by, W, 960, fill=mix(BG, (120, 100, 70), 1.0))
    T = 6.0
    ph = (t % T) / T
    base = 300 + 260 * int(t / T)
    move = 260 * (min(1.0, ph / 0.6))
    bx = (base + move) % 1500 + 100
    c.poly([(bx - 220, wy - 30), (bx + 260, wy - 30), (bx + 220, wy + 30), (bx - 180, wy + 30)], mix(BG, BOATC, 1.0))
    px = bx - 60
    _porter(c, px, wy - 30)
    tipx = bx - 60 - 300 - move * 0.6 + 200
    tipx = min(tipx, bx - 200)
    c.line([(px + 10, wy - 140), (tipx, by)], mix(BG, (200, 180, 90), 1.0), 8)
    if ph < 0.6:
        c.arrow(tipx + 20, by - 30, tipx - 90, by - 30, NRED, 5, 16)
        c.text(tipx - 100, by - 70, '人把篙往后推', 'sans', 22, NRED, 'rm')
        c.arrow(px + 40, wy - 200, px + 160, wy - 200, GREEN, 6, 18)
        c.text(px + 170, wy - 200, '河底把船推向前', 'bold', 24, GREEN, 'lm')
    caps(c, t, [(0, 7, '撑船的人把竹篙斜着戳到河底，双手往后一推'),
                (7.2, 14, '你推河底，河底也一样大地推你：这一对力大小相等、方向相反'),
                (14.2, 22, '河底不动，被推走的就是人和船：所以水深了，篙够不到底就撑不动（示意）')], y=1010)


def b208_angle(c, t, i):
    corner_tag(c, 'B208 · 斜着撑，才往前走')
    c.text(60, 96, '篙越竖直，力大多往下压在河底，往前的分力很小；太斜了，篙尖又容易在河底打滑：斜着一个合适的角度，船走得最远', 'serif', 35, INK)
    for k, (deg, lab, ok) in enumerate([(85, '太直：力往下压', False), (60, '合适：往前推得多', True), (25, '太斜：篙尖打滑', False)]):
        ox, oy = 360 + k * 600, 760
        c.rect(ox - 240, oy, ox + 240, oy + 20, fill=mix(BG, (120, 100, 70), 1.0))
        a = math.radians(deg)
        L = 320
        ox = ox - 120 * math.cos(a)
        tx, ty = ox, oy
        hx, hy = ox + L * math.cos(a), oy - L * math.sin(a)
        c.line([(tx, ty), (hx, hy)], mix(BG, (200, 180, 90), 1.0), 8)
        F = 150
        fx, fy = F * math.cos(a), F * math.sin(a)
        c.arrow(hx, hy, hx + fx, hy - fy, mix(BG, MUTED, 0.9), 4, 14)
        c.arrow(hx, hy, hx + fx, hy, GREEN if ok else NRED, 6, 18)
        c.text(hx + fx / 2, hy + 40, f'往前 {math.cos(a) * 100:.0f}%', 'mono', 20, GREEN if ok else NRED, 'mm')
        if deg < 30:
            c.text(ox - 60, oy - 40, '滑！', 'bold', 26, NRED, 'mm')
        c.text(ox, oy + 80, lab, 'bold', 24, GREEN if ok else NRED, 'mm')
    c.text(960, 900, '百分比只看方向，不计打滑（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '水盆里放一个塑料盒当船，用一根长筷子抵住盆底往后推'),
                (7.2, 14, '筷子竖直推，船几乎不动；只在水里划一下不碰底，船走得很近'),
                (14.2, 22, '斜着一个合适的角度抵住盆底推，船走得最远（以实测为准）')], y=1010)


CLIPS = {
 'B206_分担': (b206_share, 22), 'B206_上坡': (b206_slope, 22),
 'B206_片头': (titles.opening(BSER, VOL46, SB46, 6, '宋代以后轿子在城市中普及'), 7),
 'B206_片尾': (titles.closing(BSER, VOL46, SB46, 6, '下集：两根绳子悠一只桶，怎么把水甩上田？'), 7),
 'B207_摆动': (b207_swing, 22), 'B207_合拍': (b207_sync, 22),
 'B207_片头': (titles.opening(BSER, VOL46, SB46, 7, '汉代已有戽斗'), 7),
 'B207_片尾': (titles.closing(BSER, VOL46, SB46, 7, '下集：撑船的人推的是河底，为什么走的是船？'), 7),
 'B208_推底': (b208_push, 22), 'B208_角度': (b208_angle, 22),
 'B208_片头': (titles.opening(BSER, VOL46, SB46, 8, '先秦已用竹篙撑船'), 7),
 'B208_片尾': (titles.closing(BSER, VOL46, SB46, 8, '下集：划龙舟为什么一定要听鼓点？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
