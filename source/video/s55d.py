"""第五十五季（第二十四层：游乐场）收官：E291 哈哈镜 + 第五十五季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s55a import S55A, SER55, VOL55

MIRROR = (200, 210, 225)
FACE = (240, 200, 170)


def _face(c, cx, cy, sx, sy):
    c.ellipse(cx, cy, 90 * sx, 110 * sy, fill=mix(BG, FACE, 1.0))
    for d in (-1, 1):
        c.ellipse(cx + d * 35 * sx, cy - 25 * sy, 10 * sx, 12 * sy, fill=INK)
    c.arc(cx, cy + 30 * sy, 40 * sx, 20 * sy, 20, 160, INK, 5)


def e291_curve(c, t, i):
    corner_tag(c, '第 291 集 · 鼓出来变小，凹进去变大')
    c.text(60, 96, '哈哈镜是弯曲的镜子：向外鼓的地方把光往外散，照出来的样子变小；向里凹的地方把光往里收，照出来的样子变大', 'serif', 36, INK)
    for j, (lab, kind) in enumerate([('平面镜', 0), ('向外鼓', 1), ('向里凹', 2)]):
        cx = 400 + j * 560
        if kind == 0:
            c.line([(cx - 160, 300), (cx + 160, 300)], mix(BG, MIRROR, 1.0), 12)
        else:
            sgn = 1 if kind == 1 else -1
            pts = [(cx - 160 + k * 16, 300 + sgn * 40 * (1 - ((k - 10) / 10) ** 2)) for k in range(21)]
            c.line(pts, mix(BG, MIRROR, 1.0), 12)
        s = [1.0, 0.65, 1.4][kind] if t > 2 + j * 4 else 1.0
        _face(c, cx, 600, s, s)
        c.text(cx, 840, lab + ['：一样大', '：变小', '：变大'][kind], 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '平面镜照出来和自己一样大'),
                (7.2, 14, '镜面向外鼓：光被往外散开，像变小了'),
                (14.2, 22, '镜面向里凹：光被往里收，像变大了（不锈钢汤勺两面也一样）')], y=1010)


def e291_stretch(c, t, i):
    corner_tag(c, '第 291 集 · 只弯一个方向，就被拉长或压扁')
    c.text(60, 96, '哈哈镜往往只在一个方向弯：左右鼓、上下平，人就被压得又高又瘦；上下鼓、左右平，就变得又矮又胖', 'serif', 36, INK)
    ph = 0.5 + 0.5 * math.sin(t * 0.6)
    for j, (lab, sx, sy) in enumerate([('左右向外鼓：变瘦', 0.55, 1.0), ('上下向外鼓：变矮', 1.0, 0.55)]):
        cx = 560 + j * 800
        c.rect(cx - 220, 240, cx + 220, 860, outline=mix(BG, MIRROR, 1.0), width=8, r=20)
        a = 1 - ph * (1 - sx)
        b = 1 - ph * (1 - sy)
        _face(c, cx, 520, a * 1.3, b * 1.3)
        c.rect(cx - 70 * a, 680, cx + 70 * a, 680 + 140 * b, fill=mix(BG, (120, 160, 220), 1.0), r=10)
        c.text(cx, 920, lab, 'bold', 28, INK, 'mm')
    caps(c, t, [(0, 7, '镜面卡纸左右两边往后弯：脸被左右压窄，看起来又高又瘦'),
                (7.2, 14, '卡纸上下两边往后弯：脸被上下压扁，看起来又矮又胖'),
                (14.2, 22, '游乐场的哈哈镜一块镜子上有好几段弯，就照出奇形怪状（只用镜面卡纸）')], y=1010)


OLD55 = [('砂纸', '230'), ('魔术贴', '146'), ('杠杆与滑轮组', '39'), ('电子秤', '160'), ('洗衣机甩干', '154'), ('溜溜球', '232'),
         ('齿轮与轴承', '41'), ('悬索桥', '79'), ('重力发电', '9'), ('回力车', '240'), ('安全气囊', '174'), ('弹力球', '233'),
         ('水塔', '163'), ('花洒', '254'), ('自行车', '66'), ('螺旋桨', '177'), ('老虎钳', '226'), ('电磁铁', '56'), ('透镜', '52'), ('万花筒', '234')]
NEW55 = [('滑梯', '282', ['砂纸', '魔术贴']), ('跷跷板', '283', ['杠杆与滑轮组', '电子秤']), ('旋转转盘', '284', ['洗衣机甩干', '溜溜球']),
         ('摩天轮', '285', ['齿轮与轴承', '悬索桥']), ('过山车', '286', ['重力发电', '回力车']), ('碰碰车', '287', ['安全气囊', '弹力球']),
         ('喷泉', '288', ['水塔', '花洒']), ('脚踏船', '289', ['自行车', '螺旋桨']), ('抓娃娃机', '290', ['老虎钳', '电磁铁']),
         ('哈哈镜', '291', ['透镜', '万花筒'])]


def s55_layer(c, t, i):
    corner_tag(c, '第五十五季特辑 · 第二十四层')
    c.text(60, 118, '第二十四层：游乐场', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD55):
        pos[name] = (340, 216 + k * 37)
    for k, (name, num, deps) in enumerate(NEW55):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 178, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十五季新长出', 'sans', 24, MUTED, 'mm')
    newn = dict((n, 1) for n, _, _ in NEW55)
    for k, (name, num, deps) in enumerate(NEW55):
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
    for name, num in OLD55:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW55):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第二十四层的十集：游乐场里的东西'),
                (8.2, 16, '砂纸长出滑梯，杠杆长出跷跷板，洗衣机甩干长出旋转转盘，悬索桥长出摩天轮，回力车长出过山车'),
                (16.2, 24, '安全气囊长出碰碰车，水塔长出喷泉，螺旋桨长出脚踏船，老虎钳和电磁铁长出抓娃娃机'),
                (24.2, 30, '最后，透镜和万花筒一起，长出了哈哈镜')], y=1040)


CLIPS = {
 'E291_曲面': (e291_curve, 22), 'E291_拉长': (e291_stretch, 22),
 'E291_片头': (titles.opening(SER55, VOL55, S55A, 9, '19 世纪游乐场已有哈哈镜'), 7),
 'E291_片尾': (titles.closing(SER55, VOL55, S55A, 9, '下集：第五十五季特辑 · 第二十四层回顾'), 7),
 'S55_第二十四层': (s55_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
