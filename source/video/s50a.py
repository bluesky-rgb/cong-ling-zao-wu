"""第五十季（古法解密 22.0：山居与田园）第一批：B220 梯田、B221 土楼、B222 天井 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB50 = [('B220', '梯田'), ('B221', '土楼'), ('B222', '天井'), ('B223', '蚊帐'), ('B224', '蜂巢'),
        ('B225', '镰刀'), ('B226', '鱼钩'), ('B227', '跳绳'), ('B228', '围棋'), ('B229', '车同轨')]
VOL50 = '第五十季 · 古法解密 22.0'
SOIL = (170, 130, 80)
RICE = (120, 170, 80)
EARTH = (190, 150, 100)
ROOF = (110, 110, 120)
RAIN = (120, 170, 230)


# ---------------------------------------------------------------- B220 梯田
def b220_wash(c, t, i):
    corner_tag(c, 'B220 · 一整面斜坡：水越流越快')
    c.text(60, 96, '雨落在一整面斜坡上，水顺着坡一路往下，越流越快，把表面的泥土一层层带走', 'serif', 36, INK)
    x0, y0, x1, y1 = 200, 320, 1700, 880
    c.poly([(x0, y0), (x1, y1), (x0, y1)], mix(BG, SOIL, 1.0))
    random.seed(2)
    for k in range(30):
        f = ((t * 0.35) + k / 30) % 1
        x = x0 + 40 + f * (x1 - x0 - 80)
        y = y0 + (x - x0) * (y1 - y0) / (x1 - x0) - 10
        sp = 4 + 10 * f
        c.line([(x - sp * 2, y - sp * 2 * (y1 - y0) / (x1 - x0)), (x, y)], mix(BG, WATER, 1.0), 5)
        if f > 0.4:
            c.ellipse(x + 10, y + 6, 5, 5, fill=mix(BG, SOIL, 0.7))
    c.rect(1640, 880, 1880, 960, fill=mix(BG, (150, 120, 80), 0.9), r=10)
    c.text(1760, 920, '浑水', 'bold', 26, BG, 'mm')
    caps(c, t, [(0, 7, '整面斜坡上，雨水没有地方停，一落下就往下跑'),
                (7.2, 14, '越往下水越多、越快，把表面的泥土带走'),
                (14.2, 22, '坡底接到的是一杯浑水：土被冲走了（示意，以实测为准）')], y=1010)


def b220_steps(c, t, i):
    corner_tag(c, 'B220 · 一层层平台：水停一停再走')
    c.text(60, 96, '修成一层层平台：雨水先在这一层停住、慢慢渗下去，多的水才从田埂缺口流到下一层，水慢了就冲不走泥土', 'serif', 36, INK)
    n = 5
    for k in range(n):
        x0 = 200 + k * 300
        y = 360 + k * 110
        c.rect(x0, y, 1720, y + 110, fill=mix(BG, SOIL, 1.0 - 0.06 * k))
        lvl = min(1.0, max(0.0, (t - k * 2.5) / 3))
        c.rect(x0, y - 18 * lvl, x0 + 280, y, fill=mix(BG, WATER, 0.9))
        c.rect(x0 + 270, y - 22, x0 + 300, y, fill=mix(BG, SOIL, 0.7))
        for r in range(5):
            c.line([(x0 + 40 + r * 50, y - 18 * lvl), (x0 + 40 + r * 50, y - 50)], mix(BG, RICE, 1.0), 3)
        if lvl >= 1 and k < n - 1:
            c.line([(x0 + 300, y - 10), (x0 + 310, y + 100)], mix(BG, WATER, 1.0), 4)
    c.rect(1640, 900, 1880, 960, fill=mix(BG, WATER, 0.7), r=10)
    c.text(1760, 930, '清水', 'bold', 26, BG, 'mm')
    caps(c, t, [(0, 7, '每一层都修得平平的，四边有田埂'),
                (7.2, 14, '雨水在这一层停住、泡着稻田，慢慢渗下去'),
                (14.2, 22, '满了才从缺口流到下一层，水一直走得慢，土就留住了（示意）')], y=1010)


# ---------------------------------------------------------------- B221 土楼
def b221_wall(c, t, i):
    corner_tag(c, 'B221 · 一米多厚的夯土墙')
    c.text(60, 96, '土楼的外墙用夯土一层层筑起来，底层一米多厚：墙厚，热要很久才能穿过去，屋里的温度就变得慢', 'serif', 36, INK)
    cx, cy = 760, 560
    c.ellipse(cx, cy, 400, 280, fill=mix(BG, EARTH, 1.0))
    c.ellipse(cx, cy, 290, 200, fill=mix(BG, (90, 90, 80), 0.6))
    c.ellipse(cx, cy, 190, 130, fill=mix(BG, (200, 200, 180), 0.5))
    for k in range(6):
        y = cy - 280 + k * 90
    sun = t < 11
    if sun:
        c.ellipse(1600, 260, 70, 70, fill=(250, 200, 80))
        for k in range(6):
            f = ((t * 0.5) + k / 6) % 1
            x = 1500 - f * 330
            c.ellipse(x, 300 + k * 60, 10, 10, fill=SPARK)
    else:
        c.ellipse(1600, 260, 60, 60, fill=mix(BG, (220, 220, 240), 0.9))
        c.ellipse(1630, 245, 55, 55, fill=BG)
    c.text(cx, cy + 320, '外墙：夯土，底层一米多厚', 'bold', 26, INK, 'mm')
    c.text(1500, 720, '白天：墙还没热透，太阳就落山' if sun else '夜里：墙里存的热慢慢放回屋里', 'bold', 28, SPARK if sun else GREEN, 'mm')
    caps(c, t, [(0, 7, '圆形土楼一圈住几十户人家，外墙全用夯土筑成'),
                (7.2, 14, '白天太阳晒，热要穿过厚厚的土墙，走得很慢'),
                (14.2, 22, '夜里外面冷了，墙里存的热又慢慢放出来：冬暖夏凉（示意）')], y=1010)


def b221_delay(c, t, i):
    corner_tag(c, 'B221 · 厚墙让温度变得慢')
    c.text(60, 96, '两杯一样的 50 ℃ 温水：一杯直接放着，一杯四周包上 3 厘米厚的湿沙；30 分钟里，包沙的那杯凉得慢', 'serif', 36, INK)
    x0, y0, x1, y1 = 300, 820, 1500, 300
    c.line([(x0, y0), (x1, y0)], INK, 3)
    c.line([(x0, y0), (x0, y1)], INK, 3)
    c.text((x0 + x1) / 2, y0 + 50, '时间（分钟）', 'sans', 24, MUTED, 'mm')
    c.text(x0 - 20, y1, '50 ℃', 'mono', 20, MUTED, 'rm')
    c.text(x0 - 20, y0, '20 ℃', 'mono', 20, MUTED, 'rm')
    k = min(1.0, t / 16)
    for lab, tau, col in [('直接放着', 18, NRED), ('包着湿沙（厚墙）', 60, GREEN)]:
        pts = []
        for n in range(int(60 * k) + 1):
            m = 30 * n / 60
            T = 20 + 30 * math.exp(-m / tau)
            pts.append((x0 + m / 30 * (x1 - x0), y0 - (T - 20) / 30 * (y0 - y1)))
        if len(pts) > 1:
            seg(c, pts, col, 5)
            c.text(pts[-1][0] + 20, pts[-1][1], lab, 'bold', 24, col, 'lm')
    c.text(1620, 900, '（示意曲线，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '直接放着的那杯，热很快散到空气里'),
                (7.2, 14, '包了湿沙的那杯，热要先穿过厚厚的沙层，凉得慢得多'),
                (14.2, 22, '反过来装冰水，包沙的也热得慢：厚墙挡住了外面的冷热变化')], y=1010)


# ---------------------------------------------------------------- B222 天井
def _roof(c, x0, x1, ytop, ybot, inward_left):
    if inward_left:
        c.poly([(x0, ytop), (x1, ybot), (x1, ybot + 20), (x0, ytop + 20)], mix(BG, ROOF, 1.0))
    else:
        c.poly([(x0, ybot), (x1, ytop), (x1, ytop + 20), (x0, ybot + 20)], mix(BG, ROOF, 1.0))


def b222_collect(c, t, i):
    corner_tag(c, 'B222 · 四水归堂')
    c.text(60, 96, '天井四面的屋顶都朝中间斜：雨水顺着瓦片流下来，从四面汇进天井中间的水池，不会淋湿外面的墙脚', 'serif', 36, INK)
    cx = 960
    gy = 820
    c.rect(300, 520, 360, gy, fill=mix(BG, EARTH, 0.8))
    c.rect(1560, 520, 1620, gy, fill=mix(BG, EARTH, 0.8))
    c.poly([(240, 420), (820, 560), (820, 580), (240, 440)], mix(BG, ROOF, 1.0))
    c.poly([(1680, 420), (1100, 560), (1100, 580), (1680, 440)], mix(BG, ROOF, 1.0))
    c.rect(820, gy - 40, 1100, gy, fill=mix(BG, (90, 90, 90), 0.6))
    lvl = min(36, t * 2.2)
    c.rect(824, gy - 4 - lvl, 1096, gy - 4, fill=mix(BG, WATER, 0.9))
    random.seed(1)
    for k in range(50):
        f = ((t * 0.9) + k / 50) % 1
        x = random.uniform(240, 1680)
        y = 200 + f * 220
        c.line([(x, y), (x - 4, y + 18)], mix(BG, RAIN, 0.8), 2)
    for k in range(8):
        f = ((t * 0.7) + k / 8) % 1
        c.ellipse(240 + f * 580, 430 + f * 140 - 8, 6, 6, fill=mix(BG, WATER, 1.0))
        c.ellipse(1680 - f * 580, 430 + f * 140 - 8, 6, 6, fill=mix(BG, WATER, 1.0))
    c.text(cx, gy + 50, '天井水池', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '四面屋顶朝里斜，像一个漏斗的四个面'),
                (7.2, 14, '雨水顺着瓦片流向中间，从屋檐滴进天井'),
                (14.2, 22, '一大片屋顶的雨水全汇到一个小池子里：叫「四水归堂」（示意）')], y=1010)


def b222_compare(c, t, i):
    corner_tag(c, 'B222 · 朝里斜和朝外斜')
    c.text(60, 96, '同样喷 30 秒雨：屋顶朝里斜，水都流进中间的碗；屋顶朝外斜，水流到外面，碗里只接到正上方落下的一点点', 'serif', 36, INK)
    for j, (lab, inward) in enumerate([('朝里斜：碗里接满', True), ('朝外斜：碗里很少', False)]):
        cx = 480 + j * 960
        gy = 760
        L = 300
        if inward:
            c.poly([(cx - 360, 440), (cx - 70, 560), (cx - 70, 580), (cx - 360, 460)], mix(BG, ROOF, 1.0))
            c.poly([(cx + 360, 440), (cx + 70, 560), (cx + 70, 580), (cx + 360, 460)], mix(BG, ROOF, 1.0))
        else:
            c.poly([(cx - 360, 560), (cx - 70, 440), (cx - 70, 460), (cx - 360, 580)], mix(BG, ROOF, 1.0))
            c.poly([(cx + 360, 560), (cx + 70, 440), (cx + 70, 460), (cx + 360, 580)], mix(BG, ROOF, 1.0))
        c.rect(cx - 80, gy - 70, cx + 80, gy, outline=mix(BG, INK, 0.6), width=4, r=10)
        lvl = min(60, t * (3.0 if inward else 0.6))
        c.rect(cx - 76, gy - 4 - lvl, cx + 76, gy - 4, fill=mix(BG, WATER, 0.9))
        if not inward:
            for s in (-1, 1):
                c.rect(cx + s * 380 - 30, gy - 10, cx + s * 380 + 30, gy, fill=mix(BG, WATER, 0.9))
        c.text(cx, 880, lab, 'bold', 26, GREEN if inward else NRED, 'mm')
    caps(c, t, [(0, 7, '四块硬纸板当屋顶，中间放一个小碗当天井'),
                (7.2, 14, '朝里斜：落在屋顶上的雨全流进碗里'),
                (14.2, 22, '朝外斜：雨水流到托盘边上，碗里只接到一点点（以实测为准）')], y=1010)


CLIPS = {
 'B220_冲刷': (b220_wash, 22), 'B220_台阶': (b220_steps, 22),
 'B220_片头': (titles.opening(BSER, VOL50, SB50, 0, '哈尼梯田已有上千年历史'), 7),
 'B220_片尾': (titles.closing(BSER, VOL50, SB50, 0, '下集：厚厚的土墙，为什么冬暖夏凉？'), 7),
 'B221_厚墙': (b221_wall, 22), 'B221_延迟': (b221_delay, 22),
 'B221_片头': (titles.opening(BSER, VOL50, SB50, 1, '福建土楼多建于明清'), 7),
 'B221_片尾': (titles.closing(BSER, VOL50, SB50, 1, '下集：四面屋顶为什么都朝里斜？'), 7),
 'B222_汇水': (b222_collect, 22), 'B222_对比': (b222_compare, 22),
 'B222_片头': (titles.opening(BSER, VOL50, SB50, 2, '徽州民居讲究「四水归堂」'), 7),
 'B222_片尾': (titles.closing(BSER, VOL50, SB50, 2, '下集：风进得来，蚊子为什么进不来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
