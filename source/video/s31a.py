"""第三十一季（第十二层：城市里的机器）第一批：E162 红绿灯、E163 水塔、E164 电表 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L

S31A = [('162', '红绿灯'), ('163', '水塔'), ('164', '电表'), ('165', '自动门'), ('166', '条形码'),
        ('167', '公交卡'), ('168', '光控路灯'), ('169', '自动售货机'), ('170', '下水道'), ('171', '地图导航')]
SER31, VOL31 = '从零造物', '第三十一季 · 第十二层：城市里的机器'
ROAD = (60, 64, 70)
CAR = (90, 140, 210)
YEL = (240, 200, 60)
RED = (220, 70, 60)
WATER = (90, 150, 220)


def stop_dist(kmh, react=1.0, dec=7.0):
    v = kmh / 3.6
    return v * react, v * v / (2 * dec)


# ---------------------------------------------------------------- E162 红绿灯
def e162_brake(c, t, i):
    corner_tag(c, '第 162 集 · 车速翻倍，刹车距离约变四倍')
    c.text(60, 96, '从看见黄灯到车停下，要经过「反应」和「刹车」两段：反应那段和车速成正比，刹车那段和车速的平方成正比', 'serif', 36, INK)
    x0, scale = 300, 30
    grow = min(1, t / 10)
    for k, kmh in enumerate((30, 50, 70)):
        y = 330 + k * 190
        r, b = stop_dist(kmh)
        c.text(160, y, f'{kmh} 千米/时', 'bold', 26, INK, 'mm')
        c.rect(x0, y - 30, x0 + r * scale * grow, y + 30, fill=mix(BG, YEL, 0.7), r=4)
        c.rect(x0 + r * scale * grow, y - 30, x0 + (r + b) * scale * grow, y + 30, fill=mix(BG, RED, 0.7), r=4)
        c.text(x0 + (r + b) * scale * grow + 20, y, f'约 {(r + b) * grow:.0f} 米', 'mono', 24, SPARK, 'lm')
    c.rect(300, 860, 340, 890, fill=mix(BG, YEL, 0.7))
    c.text(350, 875, '反应 1 秒走过的路', 'sans', 20, MUTED, 'lm')
    c.rect(700, 860, 740, 890, fill=mix(BG, RED, 0.7))
    c.text(750, 875, '踩下刹车后滑行的路', 'sans', 20, MUTED, 'lm')
    c.text(1500, 875, '估算：反应 1 秒、减速度 7 米/秒²', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '司机看见黄灯，要先反应过来，大约 1 秒，这 1 秒车照样往前开'),
                (7.2, 14, '踩下刹车后车还要滑一段：速度翻倍，这段大约变成四倍'),
                (14.2, 22, '50 千米每时的车，从看见黄灯到停下要将近 30 米：黄灯就是给停不下的车留的（估算，以实测为准）')], y=1010)


def e162_zone(c, t, i):
    corner_tag(c, '第 162 集 · 黄灯亮起时，车在哪里？')
    c.text(60, 96, '黄灯一亮：离路口足够远的车，能稳稳停下；已经很近的车，停不住，就要在黄灯时间里开过去', 'serif', 38, INK)
    c.rect(100, 480, 1820, 640, fill=ROAD)
    for k in range(16):
        c.rect(120 + k * 100, 556, 170 + k * 100, 564, fill=(220, 220, 220))
    sx = 1500
    c.rect(sx, 470, sx + 14, 650, fill=(240, 240, 240))
    c.rect(sx + 60, 260, sx + 120, 440, fill=(30, 30, 34), r=10)
    phase = 'g' if t < 5 else ('y' if t < 13 else 'r')
    for k, (col, on) in enumerate(((RED, phase == 'r'), (YEL, phase == 'y'), (GREEN, phase == 'g'))):
        c.ellipse(sx + 90, 290 + k * 55, 20, 20, fill=col if on else mix((30, 30, 34), col, 0.2))
    v = 50 / 3.6
    r, b = stop_dist(50)
    m = 10.0
    stop_line_x = sx
    can_stop_x = stop_line_x - (r + b) * m
    c.rect(can_stop_x - 4, 460, can_stop_x + 4, 660, fill=SPARK)
    c.text(can_stop_x, 690, f'停得住的界线（离路口约 {r + b:.0f} 米）', 'sans', 20, SPARK, 'mm')
    c.text((can_stop_x + stop_line_x) / 2, 440, '这里停不住 → 要开过去', 'bold', 22, NRED, 'mm')
    c.text((150 + can_stop_x) / 2, 440, '这里能停下', 'bold', 22, GREEN, 'mm')
    for k, x_start in enumerate((300, 1150)):
        tt = max(0, t - 5)
        if phase == 'g':
            x = x_start + v * m * t * 0.3
        else:
            x5 = x_start + v * m * 5 * 0.3
            if x5 < can_stop_x:
                d = min((x5 - x5) + (r + b) * m * 0.9, (r + b) * m * 0.9)
                prog = min(1, tt / 4)
                x = x5 + (stop_line_x - 60 - x5) * (1 - (1 - prog) ** 2)
                x = min(x, stop_line_x - 60)
            else:
                x = x5 + v * m * tt * 0.3
        c.rect(x - 50, 520 + k * 50 - 20, x + 50, 520 + k * 50 + 20, fill=CAR, r=8)
    c.text(960, 800, '黄灯的长短，要让「停不住」的车刚好来得及开过路口（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '绿灯时两辆车一前一后开向路口'),
                (7.2, 14, '黄灯一亮：后面那辆离得远，来得及刹住；前面那辆已经太近，硬刹会冲过停车线'),
                (14.2, 22, '所以黄灯的长短，是照着车速和刹车距离算出来的：限速越高的路，黄灯越长（示意）')], y=1010)


# ---------------------------------------------------------------- E163 水塔
def e163_pressure(c, t, i):
    corner_tag(c, '第 163 集 · 水面越高，水压越大')
    c.text(60, 96, '水塔里的水面比全城的水龙头都高：每高 10 米，水龙头那里的压力就多大约一个大气压', 'serif', 38, INK)
    gy = 900
    tx = 400
    level = 330 + 40 * math.sin(t * 0.3)
    c.rect(tx - 20, level + 60, tx + 20, gy, fill=METAL)
    c.rect(tx - 120, level - 60, tx + 120, level + 80, outline=METAL, width=6, r=12)
    c.rect(tx - 114, level - 20, tx + 114, level + 74, fill=WATER)
    c.text(tx, level - 100, '水塔', 'bold', 26, INK, 'mm')
    c.line([(tx + 20, gy - 20), (1700, gy - 20)], WATER, 10)
    floors = [(800, 3), (1150, 2), (1500, 1)]
    for k, (bx, nfl) in enumerate(floors):
        h = 120 * nfl
        c.rect(bx - 90, gy - h, bx + 90, gy, outline=LINE, width=3)
        for f in range(nfl):
            fy = gy - 60 - f * 120
            head = (fy - (level - 20)) / 20
            c.line([(bx, gy - 20), (bx, fy)], WATER, 4)
            c.line([(bx, fy), (bx + 40, fy)], METAL, 6)
            jet = max(0, head) * 3
            pts = []
            for j in range(21):
                dx = jet * j / 20 * 1.6
                yy = fy + dx * dx / (2 * jet + 1)
                if yy > gy - 22:
                    break
                pts.append((bx + 40 + dx, yy))
            if len(pts) > 1:
                c.line(pts, WATER_L, 3)
            c.text(bx - 60, fy, f'{max(0, head):.0f} 米水头', 'mono', 16, SPARK, 'mm')
    c.line([(tx + 140, level - 20), (1760, level - 20)], mix(BG, WATER, 0.6), 1)
    c.text(1740, level - 40, '水面高度', 'sans', 18, MUTED, 'rm')
    c.text(960, 960, '越低的水龙头，离水面越远，水压越大（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '水泵先把水抽到高高的水塔里存着'),
                (7.2, 14, '水塔通过管道连着全城的水龙头：水面比哪个龙头都高'),
                (14.2, 22, '龙头离水面每低 10 米，水压就多大约一个大气压：水自己就「压」出来了（示意）')], y=1010)


def e163_jet(c, t, i):
    corner_tag(c, '第 163 集 · 瓶子举得越高，水射得越远')
    c.text(60, 96, '同一个瓶子接一根软管，放在 30、60、90 厘米高处：软管出口都在地上，瓶越高，水流射得越远、灌杯越快', 'serif', 36, INK)
    gy = 880
    for k, hcm in enumerate((30, 60, 90)):
        x = 330 + k * 520
        top = gy - hcm * 5.5
        c.rect(x - 60, top, x + 60, gy, fill=mix(BG, (130, 100, 70), 0.6))
        c.rect(x - 40, top - 140, x + 40, top, outline=METAL, width=4, r=10)
        c.rect(x - 36, top - 110, x + 36, top - 4, fill=WATER)
        c.line([(x, top - 4), (x + 70, top + 20), (x + 90, gy - 30)], (200, 200, 200), 6)
        v = math.sqrt(2 * 9.8 * hcm / 100)
        rng = 60 + v * 70
        pts = [(x + 90 + u * rng, gy - 30 + 30 * u * u) for u in [j / 12 for j in range(13)]]
        if t > 2:
            c.line(pts, WATER_L, 5)
        c.text(x, gy + 40, f'{hcm} 厘米高', 'bold', 24, INK, 'mm')
        c.text(x + 90 + rng / 2, gy - 80, f'流速约 {v:.1f} 米/秒', 'mono', 18, SPARK, 'mm')
    c.text(960, 960, '理想估算：流速 ≈ √(2 × g × 高度)，有管道阻力实际更小，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '大塑料瓶底部接一根软管，瓶子放在不同高度，出口都放在地上'),
                (7.2, 14, '瓶子越高，出口的水压越大，水流射得越远，灌满一杯越快'),
                (14.2, 22, '高度翻 3 倍，流速大约变成 1.7 倍：水塔建得高，就是为了这个（理想估算，以实测为准）')], y=1010)


# ---------------------------------------------------------------- E164 电表
APPL = [('烧水壶', 1800, 0.25), ('电饭煲', 700, 1.0), ('台灯', 10, 4.0), ('手机充电', 15, 2.0), ('电视待机', 1, 20.0)]


def e164_power(c, t, i):
    corner_tag(c, '第 164 集 · 1000 瓦用 1 小时，就是 1 度电')
    c.text(60, 96, '电表记的不是「电流过了多少」，而是功率乘时间：功率大的用一会儿，功率小的用很久，都可能耗掉差不多的电', 'serif', 36, INK)
    grow = min(1, t / 10)
    x0 = 420
    for k, (name, w, hrs) in enumerate(APPL):
        y = 300 + k * 110
        kwh = w * hrs * 30 / 1000
        c.text(240, y, name, 'bold', 26, INK, 'mm')
        c.text(240, y + 34, f'{w} 瓦 × 每天 {hrs:g} 小时', 'mono', 16, MUTED, 'mm')
        bw = min(1200, kwh * 22) * grow
        c.rect(x0, y - 22, x0 + bw, y + 22, fill=mix(SPARK, GREEN, min(1, kwh / 20)), r=4)
        c.text(x0 + bw + 20, y, f'每月约 {kwh * grow:.1f} 度', 'mono', 22, SPARK, 'lm')
    c.text(960, 880, '功率用插座功率计实测，使用时间按自家情况估（数字为示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '1 度电 = 1 千瓦时：1000 瓦的电器用 1 小时，或者 10 瓦的台灯用 100 小时'),
                (7.2, 14, '烧水壶功率很大，但每天只烧一会儿；电视待机只有 1 瓦左右，可一天插 20 小时'),
                (14.2, 22, '把功率乘上时间，一个月加起来，就是电表上走过的度数（示意，以实测为准）')], y=1010)


def e164_disk(c, t, i):
    corner_tag(c, '第 164 集 · 老电表：功率越大，铝盘转得越快')
    c.text(60, 96, '老式电表里有一块铝盘，电流的磁场在铝盘里感应出涡流推它转：功率越大转得越快，数一数转了多少圈就是用了多少电', 'serif', 34, INK)
    loads = [('台灯 10 瓦', 10), ('电饭煲 700 瓦', 700), ('烧水壶 1800 瓦', 1800)]
    k = min(2, int(t / 7.4))
    name, w = loads[k]
    cx, cy = 620, 560
    c.rect(cx - 300, cy - 300, cx + 300, cy + 300, outline=METAL, width=6, r=20)
    c.ellipse(cx, cy + 60, 220, 50, fill=mix(METAL, BG, 0.2))
    rev = 3000 / 3600 * w / 1000
    ang = sum(3000 / 3600 * loads[j][1] / 1000 * 7.4 for j in range(k)) * 2 * math.pi + (t - 7.4 * k) * rev * 2 * math.pi * 6
    mx = cx + 200 * math.cos(ang)
    c.rect(mx - 10, cy + 40, mx + 10, cy + 80, fill=RED if math.sin(ang) > 0 else mix(RED, BG, 0.5))
    c.rect(cx - 200, cy - 240, cx + 200, cy - 160, fill=(20, 20, 24), r=6)
    kwh = 1234.5 + t * w / 1000 * 0.02
    c.text(cx, cy - 200, f'{kwh:08.1f}', 'mono', 40, (230, 230, 230), 'mm')
    c.text(cx, cy + 180, '铝盘', 'sans', 22, MUTED, 'mm')
    c.rect(1150, 330, 1820, 760, fill=SHEET, r=14)
    c.text(1485, 380, '现在接着', 'bold', 24, INK, 'mm')
    c.text(1485, 460, name, 'bold', 34, SPARK, 'mm')
    c.text(1485, 560, f'铝盘每分钟约 {rev * 60:.1f} 圈', 'mono', 26, INK, 'mm')
    c.text(1485, 640, '（按 3000 转/度估算，转速动画放大）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '老式感应式电表：线圈的磁场在铝盘里感应出涡流，推着铝盘转'),
                (7.2, 14, '功率越大，推得越用力，转得越快；齿轮把圈数记到计数器上'),
                (14.2, 22, '电表上常写着「3000 转/千瓦时」：铝盘转满 3000 圈就是 1 度电。今天的电子电表直接用芯片算（示意）')], y=1010)


CLIPS = {
 'E162_刹车': (e162_brake, 22), 'E162_黄灯': (e162_zone, 22),
 'E162_片头': (titles.opening(SER31, VOL31, S31A, 0, '1868 年伦敦煤气信号灯'), 7),
 'E162_片尾': (titles.closing(SER31, VOL31, S31A, 0, '下集：高处的水塔，为什么能让全城的水龙头出水？'), 7),
 'E163_水压': (e163_pressure, 22), 'E163_射程': (e163_jet, 22),
 'E163_片头': (titles.opening(SER31, VOL31, S31A, 1, '19 世纪城市水塔'), 7),
 'E163_片尾': (titles.closing(SER31, VOL31, S31A, 1, '下集：电表是怎么算出你家用了几度电的？'), 7),
 'E164_功率': (e164_power, 22), 'E164_转盘': (e164_disk, 22),
 'E164_片头': (titles.opening(SER31, VOL31, S31A, 2, '1888 年发明感应式电度表'), 7),
 'E164_片尾': (titles.closing(SER31, VOL31, S31A, 2, '下集：没人按开关，商场的门为什么人一走近就开？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
