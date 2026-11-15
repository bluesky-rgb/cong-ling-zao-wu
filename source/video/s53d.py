"""第五十三季（第二十三层：超市与包装）收官：E281 自动扶梯 + 第五十三季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s53a import S53A, SER53, VOL53

STEP = (170, 175, 185)
TRACK1 = (90, 160, 230)
TRACK2 = (230, 140, 80)


def _tracks(s):
    """s：沿扶梯的位置 0..1；返回前轮轨道高度 y1 和后轮轨道高度 y2（像素，向上为负）。"""
    x0, x1 = 260, 1660
    x = x0 + (x1 - x0) * s
    def ramp(u):
        if u < 0.25: return 0.0
        if u > 0.75: return 1.0
        v = (u - 0.25) / 0.5
        return v
    rise = 440
    y = 820 - rise * ramp(s)
    # 中段两条轨道错开 60 像素；两端并拢
    k = 0.0
    if 0.25 < s < 0.75:
        k = min(1.0, (s - 0.25) / 0.06, (0.75 - s) / 0.06)
    return x, y, k


def e281_tracks(c, t, i):
    corner_tag(c, '第 281 集 · 两条轨道')
    c.text(60, 96, '每级台阶下有前后两对轮子，各走一条轨道：中间两条轨道上下错开，台阶就成一级级；两头并拢，台阶就变平', 'serif', 36, INK)
    # 画两条轨道
    pts1, pts2 = [], []
    for k in range(101):
        s = k / 100
        x, y, gap = _tracks(s)
        pts1.append((x, y))
        pts2.append((x, y + 70 * gap))
    c.line(pts1, TRACK1, 6)
    c.line(pts2, TRACK2, 6)
    c.text(300, 860, '蓝：前轮轨道　橙：后轮轨道', 'sans', 24, MUTED, 'lm')
    for n in range(9):
        s = ((t * 0.03) + n / 9) % 1
        x, y, gap = _tracks(s)
        top = y - 6
        c.rect(x - 70, top - 16, x + 70, top, fill=mix(BG, STEP, 1.0), r=3)
        c.rect(x + 54, top, x + 70, top + 70 * gap + 10, fill=mix(BG, STEP, 0.7))
        c.ellipse(x - 50, y, 10, 10, fill=TRACK1)
        c.ellipse(x + 62, y + 70 * gap, 10, 10, fill=TRACK2)
    caps(c, t, [(0, 7, '台阶从地板下面平平地冒出来：两条轨道并在一起'),
                (7.2, 14, '到斜坡上，两条轨道上下错开，台阶的后沿被撑高，变成一级级楼梯'),
                (14.2, 22, '到了顶上两条轨道又并拢，台阶变平，钻进地板绕回去（示意）')], y=1010)


def e281_rail(c, t, i):
    corner_tag(c, '第 281 集 · 扶手和台阶一起走')
    c.text(60, 96, '扶手和台阶由同一套机器带着，速度一样；乘扶梯要站稳、扶好扶手，鞋带系好，不在扶梯上跑跳和玩耍', 'serif', 36, INK)
    x0, y0, x1, y1 = 300, 800, 1600, 360
    c.line([(x0 - 120, y0), (x0, y0), (x1, y1), (x1 + 120, y1)], mix(BG, STEP, 1.0), 12)
    c.line([(x0 - 120, y0 - 160), (x0, y0 - 160), (x1, y1 - 160), (x1 + 120, y1 - 160)], mix(BG, (60, 60, 70), 1.0), 18)
    ph = (t * 0.06) % 1
    for k in range(6):
        u = (ph + k / 6) % 1
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        c.ellipse(x, y - 10, 10, 10, fill=GREEN)
        c.ellipse(x, y - 170, 10, 10, fill=GREEN)
    c.text(960, 230, '绿点：台阶上和扶手上同一时刻的位置，一起前进', 'bold', 26, GREEN, 'mm')
    tips = ['站稳、扶好扶手', '鞋带系好，软胶鞋别贴边', '不坐、不跑跳、不逆行']
    for k, tip in enumerate(tips):
        a = fade(t, 7.2 + k * 2.5, 8.2 + k * 2.5)
        if a > 0:
            c.text(1300, 620 + k * 60, tip, 'bold', 28, mix(BG, NRED, a), 'lm')
    caps(c, t, [(0, 7, '用手机计时：一级台阶从底走到顶要多少秒，扶手也一样'),
                (7.2, 14, '扶手和台阶一起走，扶着就跟着一起上去'),
                (14.2, 22, '只在旁边观察，大人陪同；乘的时候站稳扶好')], y=1010)


OLD53 = [('纸', '23'), ('印刷机', '65'), ('复合材料', '150'), ('铝', '145'), ('开瓶器', '242'), ('罐藏', '37'),
         ('真空包装', '195'), ('塑料', '142'), ('跑鞋缓震', '202'), ('安全气囊', '174'), ('自行车', '66'),
         ('齿轮与轴承', '41'), ('制冷', '68'), ('热气球', '44'), ('电梯与安全钳', '87')]
NEW53 = [('热敏小票', '272', ['纸', '印刷机']), ('瓦楞纸箱', '273', ['纸', '复合材料']), ('易拉罐', '274', ['铝', '开瓶器']),
         ('牛奶盒', '275', ['罐藏', '铝']), ('薯片袋', '276', ['真空包装', '塑料']), ('鸡蛋托', '277', ['跑鞋缓震', '瓦楞纸箱']),
         ('气泡膜', '278', ['跑鞋缓震', '安全气囊']), ('万向轮', '279', ['自行车', '齿轮与轴承']), ('卧式冰柜', '280', ['制冷', '热气球']),
         ('自动扶梯', '281', ['电梯与安全钳', '齿轮与轴承'])]


def s53_layer(c, t, i):
    corner_tag(c, '第五十三季特辑 · 第二十三层')
    c.text(60, 118, '第二十三层：超市与包装', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD53):
        pos[name] = (340, 220 + k * 44)
    for k, (name, num, deps) in enumerate(NEW53):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 178, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十三季新长出', 'sans', 24, MUTED, 'mm')
    newn = dict((n, 1) for n, _, _ in NEW53)
    for k, (name, num, deps) in enumerate(NEW53):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in newn:
                sx, ex = x0 - 110, x1 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
                pts[-1] = (ex, y1)
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD53:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW53):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第二十三层的十集：超市和包装里的东西'),
                (8.2, 16, '纸和印刷机长出热敏小票，纸长出瓦楞纸箱，铝长出易拉罐和牛奶盒，真空包装长出薯片袋'),
                (16.2, 24, '瓦楞纸箱长出鸡蛋托，安全气囊长出气泡膜，自行车长出万向轮，热气球和制冷长出卧式冰柜'),
                (24.2, 30, '最后，电梯和轴承一起，长出了自动扶梯')], y=1040)


CLIPS = {
 'E281_轨道': (e281_tracks, 22), 'E281_扶手': (e281_rail, 22),
 'E281_片头': (titles.opening(SER53, VOL53, S53A, 9, '1900 年前后出现自动扶梯'), 7),
 'E281_片尾': (titles.closing(SER53, VOL53, S53A, 9, '下集：第五十三季特辑 · 第二十三层回顾'), 7),
 'S53_第二十三层': (s53_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
