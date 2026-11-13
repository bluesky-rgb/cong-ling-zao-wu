"""第四十七季（第二十层：厨房抽屉）收官：E251 吸管 + 第四十七季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s47a import S47A, SER47, VOL47

WATER = (90, 160, 220)
STRAW = (230, 120, 140)


def _cup(c, cx, base, level, straw_level, leak=False, sealed=False):
    c.rect(cx - 160, base - 360, cx - 150, base, fill=mix(BG, INK, 0.6))
    c.rect(cx + 150, base - 360, cx + 160, base, fill=mix(BG, INK, 0.6))
    c.rect(cx - 160, base, cx + 160, base + 10, fill=mix(BG, INK, 0.6))
    if sealed:
        c.rect(cx - 160, base - 370, cx + 160, base - 360, fill=mix(BG, INK, 0.6))
    c.rect(cx - 150, base - level, cx + 150, base, fill=mix(BG, WATER, 0.7))
    sx = cx + 40
    c.rect(sx - 14, base - 560, sx - 8, base - 20, fill=mix(BG, STRAW, 1.0))
    c.rect(sx + 8, base - 560, sx + 14, base - 20, fill=mix(BG, STRAW, 1.0))
    c.rect(sx - 8, base - straw_level, sx + 8, base - 20, fill=mix(BG, WATER, 0.9))
    if leak:
        c.rect(sx + 8, base - 470, sx + 14, base - 456, fill=BG)
        c.arrow(sx + 60, base - 463, sx + 18, base - 463, FIELD, 4, 12)
        c.text(sx + 70, base - 463, '空气从洞里补进来', 'bold', 22, FIELD, 'lm')
    if not sealed:
        for k in range(5):
            x = cx - 130 + k * 40
            if abs(x - sx) < 30:
                continue
            c.arrow(x, base - level - 120, x, base - level - 14, SPARK, 4, 12)
    return sx


def e251_push(c, t, i):
    corner_tag(c, '第 251 集 · 是大气压把水推上来')
    c.text(60, 96, '嘴只是把吸管里的空气吸走，管里的气压变小；杯里水面上的大气压没变，就把水推进吸管', 'serif', 36, INK)
    ph = min(1.0, (t % 22) / 12)
    base = 860
    sx = _cup(c, 760, base, 220, 220 + (560 - 240) * ph)
    c.ellipse(sx, base - 600, 70, 40, fill=mix(BG, (230, 190, 160), 0.9))
    c.arrow(sx, base - 570, sx, base - 650, mix(BG, INK, 0.7), 4, 12)
    c.text(sx + 90, base - 610, '嘴：吸走管里的空气', 'bold', 24, INK, 'lm')
    c.text(560, base - 380, '大气压往下压水面', 'bold', 24, SPARK, 'mm')
    c.text(1500, 420, '管里气压', 'sans', 26, MUTED, 'mm')
    c.rect(1420, 460, 1580, 500, fill=SHEET, r=6)
    c.rect(1420, 460, 1420 + 160 * (1 - 0.3 * ph), 500, fill=FIELD, r=6)
    c.text(1500, 560, '杯外大气压', 'sans', 26, MUTED, 'mm')
    c.rect(1420, 600, 1580, 640, fill=SPARK, r=6)
    c.text(1500, 700, '外面的大，水就被推上去', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '吸之前，吸管里外的气压一样，水面也一样高'),
                (7.2, 14, '一吸，管里的空气被抽走，气压变小'),
                (14.2, 22, '杯里水面上的大气压比管里大，把水推上吸管（示意；只吸干净的清水）')], y=1010)


def e251_leak(c, t, i):
    corner_tag(c, '第 251 集 · 漏气就吸不上来')
    c.text(60, 96, '吸管上扎个小洞，空气从洞里补进去，管里的气压降不下来；瓶子封死，水面上没有空气推，也吸不动', 'serif', 36, INK)
    base = 860
    ph = min(1.0, (t % 22) / 10)
    _cup(c, 480, base, 220, 220 + 60 * ph, leak=True)
    c.text(480, base + 60, '扎了洞：水只上来一点', 'bold', 26, NRED, 'mm')
    _cup(c, 1440, base, 300, 300 + 40 * ph, sealed=True)
    c.text(1440, base + 60, '瓶子封死：水面上没空气推', 'bold', 26, NRED, 'mm')
    caps(c, t, [(0, 7, '吸管扎一个小洞：一吸，空气从洞里钻进去，管里的气压降不下来'),
                (7.2, 14, '用胶带把洞贴住，又能吸上来了'),
                (14.2, 22, '瓶子封死，里面的水面上没有空气推；松开一点让空气进去，就又能吸（以实测为准）')], y=1010)


OLD47 = [('杠杆与滑轮组', '39'), ('钢', '62'), ('齿轮与轴承', '41'), ('罐藏', '37'), ('泡泡', '235'), ('老虎钳', '226'),
         ('不锈钢', '144'), ('史莱姆', '236'), ('砂纸', '230'), ('螺丝与标准件', '64'), ('虹吸', '26'), ('吸盘', '231')]
NEW47 = [('开瓶器', '242', ['杠杆与滑轮组', '钢']), ('开罐器', '243', ['齿轮与轴承', '罐藏']), ('打蛋器', '244', ['泡泡', '齿轮与轴承']),
         ('压蒜器', '245', ['杠杆与滑轮组', '老虎钳']), ('削皮器', '246', ['钢', '不锈钢']), ('食品夹', '247', ['杠杆与滑轮组', '压蒜器']),
         ('擀面杖', '248', ['齿轮与轴承', '史莱姆']), ('刨丝器', '249', ['砂纸', '削皮器']), ('胡椒磨', '250', ['齿轮与轴承', '螺丝与标准件']),
         ('吸管', '251', ['虹吸', '吸盘'])]


def s47_layer(c, t, i):
    corner_tag(c, '第四十七季特辑 · 第二十层')
    c.text(60, 118, '第二十层：厨房抽屉', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD47):
        pos[name] = (340, 230 + k * 58)
    for k, (name, num, deps) in enumerate(NEW47):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 178, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十七季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW47):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in dict((n, 1) for n, _, _ in NEW47):
                sx, ex = x0 - 110, x1 - 110
                if abs(x0 - x1) < 5:
                    sx = x0 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
                pts[-1] = (ex, y1)
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD47:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW47):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第二十层的十集：厨房抽屉里的小工具'),
                (8.2, 16, '杠杆长出开瓶器和压蒜器，齿轮和罐藏长出开罐器，泡泡长出打蛋器，钢长出削皮器'),
                (16.2, 24, '压蒜器长出食品夹，史莱姆长出擀面杖，砂纸和削皮器长出刨丝器，螺丝长出胡椒磨'),
                (24.2, 30, '最后，虹吸和吸盘一起，长出了吸管')], y=1040)


CLIPS = {
 'E251_气压': (e251_push, 22), 'E251_漏气': (e251_leak, 22),
 'E251_片头': (titles.opening(SER47, VOL47, S47A, 9, '1888 年美国人斯通申请纸吸管专利'), 7),
 'E251_片尾': (titles.closing(SER47, VOL47, S47A, 9, '下集：第四十七季特辑 · 第二十层回顾'), 7),
 'S47_第二十层': (s47_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
