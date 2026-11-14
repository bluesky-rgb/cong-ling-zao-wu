"""第四十九季（第二十一层：浴室）收官：E261 电动牙刷 + 第四十九季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s49a import S49A, SER49, VOL49, WATER, STEEL, BRISTLE


def e261_offset(c, t, i):
    corner_tag(c, '第 261 集 · 偏心重块转起来就抖')
    c.text(60, 96, '电动机轴上装一块偏到一边的小重块：转起来时，它一会儿往上甩、一会儿往下甩，整个刷柄就跟着抖', 'serif', 36, INK)
    for j, (lab, off) in enumerate([('重块在正中：转得稳，不抖', False), ('重块偏一边：转起来就抖', True)]):
        cx, cy = 480 + j * 960, 520
        a = t * 8
        shake = 18 * math.sin(a) if off else 0
        c.rect(cx - 300, cy - 60 + shake, cx + 60, cy + 60 + shake, fill=mix(BG, (210, 215, 225), 1.0), r=30)
        c.rect(cx + 60, cy - 12 + shake, cx + 160, cy + 12 + shake, fill=mix(BG, STEEL, 1.0))
        if off:
            mx, my = cx + 200 + 0 * math.cos(a), cy + shake + 50 * math.sin(a)
            c.ellipse(cx + 200, cy + shake, 14, 14, fill=mix(BG, STEEL, 1.0))
            c.line([(cx + 200, cy + shake), (mx, my)], mix(BG, STEEL, 1.0), 8)
            c.ellipse(mx, my, 34, 34, fill=SPARK)
        else:
            c.ellipse(cx + 200, cy, 40, 40, fill=SPARK)
            c.line([(cx + 200 - 30 * math.cos(a), cy - 30 * math.sin(a)), (cx + 200 + 30 * math.cos(a), cy + 30 * math.sin(a))], BG, 4)
        for k in range(5):
            c.line([(cx - 280 + k * 120, 760), (cx - 220 + k * 120, 760 + (abs(shake) if off else 0))], MUTED, 3)
        c.text(cx, 880, lab, 'bold', 26, GREEN if off else MUTED, 'mm')
    caps(c, t, [(0, 7, '电动机轴上什么也不装，或者重块装在正中：转得又快又稳，不抖'),
                (7.2, 14, '重块装到轴的一边：它转到上面，就把整个刷柄往上拉；转到下面，往下拉'),
                (14.2, 22, '每秒转很多圈，刷柄就每秒抖很多次；手机振动也是这样（示意）')], y=1010)


def e261_freq(c, t, i):
    corner_tag(c, '第 261 集 · 每秒抖很多次')
    c.text(60, 96, '电动机转得越快，刷头抖得越快；刷头碰到水面，抖动变成一圈圈波纹：抖得越快，波纹越密', 'serif', 36, INK)
    k = int((t % 21) // 7)
    f = [5, 10, 20][k]
    cx, cy = 760, 600
    for r in range(1, 30):
        rr = ((r * 40) + t * f * 10) % 600
        lam = 400 / f
        rad = (r * lam + t * 60) % 600
        c.ellipse(cx, cy, rad, rad * 0.35, outline=mix(BG, WATER, max(0.1, 1 - rad / 600)), width=3)
    c.rect(cx - 20, cy - 360, cx + 20, cy - 10 + 10 * math.sin(t * f * 6), fill=mix(BG, BRISTLE, 1.0), r=6)
    c.text(1500, 420, f'抖动快慢（示意）：{["慢", "中", "快"][k]}', 'bold', 34, INK, 'mm')
    c.text(1500, 500, '抖得越快，波纹越密', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 7, '刷头轻轻碰到一碗水的水面，一抖就推出一圈波纹'),
                (7.2, 14, '抖得越快，一秒推出的波纹越多，挨得越密'),
                (14.2, 22, '电动牙刷的刷头每秒来回很多次，比手刷快得多（具体次数以说明书为准）')], y=1010)


OLD49 = [('塑料', '142'), ('洗手', '32'), ('肥皂', '22'), ('砂纸', '230'), ('水塔', '163'), ('陶罐滴灌', '27'),
         ('玻璃', '21'), ('蒸发冷却罐', '38'), ('纸', '23'), ('纸尿裤', '149'), ('机翼', '86'), ('煤气中毒与通风', '36'),
         ('螺丝与标准件', '64'), ('橡胶轮胎', '143'), ('杠杆与滑轮组', '39'), ('食品夹', '247'), ('电动机', '58'), ('电灯', '60')]
NEW49 = [('牙刷', '252', ['塑料', '洗手']), ('牙膏', '253', ['肥皂', '砂纸']), ('花洒', '254', ['水塔', '陶罐滴灌']),
         ('镜子起雾', '255', ['玻璃', '蒸发冷却罐']), ('毛巾', '256', ['纸', '纸尿裤']), ('浴帘', '257', ['机翼', '煤气中毒与通风']),
         ('水龙头', '258', ['螺丝与标准件', '橡胶轮胎']), ('指甲刀', '259', ['杠杆与滑轮组', '食品夹']), ('吹风机', '260', ['电动机', '电灯']),
         ('电动牙刷', '261', ['电动机', '牙刷'])]


def s49_layer(c, t, i):
    corner_tag(c, '第四十九季特辑 · 第二十一层')
    c.text(60, 118, '第二十一层：浴室', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD49):
        pos[name] = (340, 214 + k * 38)
    for k, (name, num, deps) in enumerate(NEW49):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 178, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十九季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW49):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in dict((n, 1) for n, _, _ in NEW49):
                sx, ex = x0 - 110, x1 - 110
                if abs(x0 - x1) < 5:
                    sx = x0 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
                pts[-1] = (ex, y1)
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD49:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW49):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第二十一层的十集：浴室里的东西'),
                (8.2, 16, '塑料长出牙刷，肥皂和砂纸长出牙膏，水塔长出花洒，玻璃长出镜子起雾，纸长出毛巾'),
                (16.2, 24, '机翼长出浴帘，螺丝长出水龙头，杠杆长出指甲刀，电动机和电灯长出吹风机'),
                (24.2, 30, '最后，电动机和牙刷一起，长出了电动牙刷')], y=1040)



CLIPS = {
 'E261_偏心': (e261_offset, 22), 'E261_频率': (e261_freq, 22),
 'E261_片头': (titles.opening(SER49, VOL49, S49A, 9, '20 世纪 50 年代瑞士出现电动牙刷'), 7),
 'E261_片尾': (titles.closing(SER49, VOL49, S49A, 9, '下集：第四十九季特辑 · 第二十一层回顾'), 7),
 'S49_第二十一层': (s49_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
