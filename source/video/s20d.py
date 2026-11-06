"""第二十季收尾：B79 蹴鞠、第二十季特辑（古法解密 7.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s20a import SB20, VOL20, WOOD

LEATHER = (170, 110, 60)
AIR = (150, 200, 240)

# ---------------------------------------------------------------- B79 蹴鞠
CASES = [('打足气', 0.80, LEATHER), ('冷藏 1 小时', 0.70, (140, 160, 190)), ('放掉一半气', 0.55, (150, 120, 90)), ('布团实心球', 0.30, (200, 190, 170))]

def _height(t, e, H):
    # 从 H 落下，g 归一；返回当前高度（0..H）
    g = 2 * H / 1.0 ** 2
    tt = t
    h = H
    v0 = 0.0
    T = math.sqrt(2 * H / g)
    if tt < T:
        return H - 0.5 * g * tt * tt
    tt -= T
    v = g * T * e
    while v > 0.05 * g:
        Tf = 2 * v / g
        if tt < Tf:
            return v * tt - 0.5 * g * tt * tt
        tt -= Tf
        v *= e
    return 0

def b79_bounce(c, t, i):
    corner_tag(c, 'B79 · 同样 1 米，谁弹得高')
    c.text(60, 96, '充了气的球，落地被压扁，压缩的空气把它推回去', 'serif', 40, INK)
    ground, H = 820, 540
    c.line([(80, ground), (1840, ground)], LINE, 4)
    for k in range(5):
        y = ground - H * k / 4
        c.line([(80, y), (100, y)], MUTED, 2)
        c.text(110, y, f'{k * 25} 厘米', 'mono', 18, MUTED, 'lm')
    tt = max(0, t - 1) * 0.8
    for k, (nm, e, col) in enumerate(CASES):
        x = 360 + k * 400
        h = _height(tt, e, 1.0)
        y = ground - 40 - (H - 40) * h
        first = e * e
        c.line([(x - 70, ground - 40 - (H - 40) * first), (x + 70, ground - 40 - (H - 40) * first)], mix(BG, col, 0.8), 2)
        squash = 1.0
        if h < 0.03:
            squash = 0.75
        c.ellipse(x, y + 40 * (1 - squash), 40 / squash ** 0.5, 40 * squash, fill=col, outline=INK, width=2)
        c.text(x, ground + 40, nm, 'bold', 24, INK, 'mm')
        c.text(x, ground + 80, f'第一次弹起约 {first * 100:.0f} 厘米（示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '四个球都从 1 米高落下'),
                (7.2, 14, '打足气的球弹得最高；放掉一半气，落地时压得太扁，劲儿都耗在变形上'),
                (14.2, 22, '冷藏过的球里空气变冷，压不出那么大的劲，也弹得低；实心布团几乎不弹（数值以实测为准）')], y=1010)

MOL = [(random.Random(k).uniform(-1, 1), random.Random(k + 50).uniform(-1, 1), random.Random(k + 90).uniform(0, 6.28)) for k in range(40)]

def b79_gas(c, t, i):
    corner_tag(c, 'B79 · 球里的空气在推')
    c.text(60, 96, '鞠里装的是猪膀胱做的气囊：打进去的空气就是弹簧', 'serif', 40, INK)
    for k, (nm, temp) in enumerate((('室温', 1.0), ('冷藏', 0.75))):
        cx, cy = 520 + k * 760, 560
        sq = 0.82 + 0.18 * abs(math.cos(t * 1.4 + k))
        rx, ry = 230 / sq ** 0.5, 230 * sq
        c.ellipse(cx, cy + 230 - ry, rx + 14, ry + 14, fill=LEATHER)
        c.ellipse(cx, cy + 230 - ry, rx, ry, fill=mix(BG, AIR, 0.25))
        for j, (u, v, ph) in enumerate(MOL):
            sp = temp * 2.2
            x = cx + rx * 0.7 * math.sin(u * 3 + t * sp + ph)
            y = cy + 230 - ry + ry * 0.7 * math.sin(v * 3 + t * sp * 1.3 + ph)
            c.ellipse(x, y, 7, 7, fill=AIR)
            c.line([(x, y), (x - 14 * temp * math.cos(t * sp + ph), y - 14 * temp * math.sin(t * sp + ph))], mix(BG, AIR, 0.5), 2)
        c.line([(cx - 320, cy + 244), (cx + 320, cy + 244)], LINE, 4)
        c.text(cx, 900, f'{nm}：空气分子跑得{"快" if temp > 0.9 else "慢"}，往外推得{"更有劲" if temp > 0.9 else "没那么有劲"}', 'sans', 24, INK, 'mm')
    caps(c, t, [(0, 7, '球里的空气被关在气囊里，一落地球被压扁，里面的空气被挤得更紧'),
                (7.2, 14, '挤紧的空气往四面八方推，把球壳推回圆形，球就弹了起来'),
                (14.2, 22, '空气凉了，分子跑得慢，推的劲小：这和第 46 集温度计里气体受热膨胀是同一个道理')], y=1010)

# ---------------------------------------------------------------- 第二十季特辑
OLD20 = [('素纱襌衣', 'B33'), ('陀螺', 'B50'), ('计算机', '91'), ('油纸伞', 'B58'), ('杆秤', 'B43'), ('螺旋提水', '25'),
         ('墨斗', 'B61'), ('虹吸', '26'), ('扇车', 'B56'), ('豆腐点卤', 'B14'), ('活字印刷', 'B3'), ('松烟墨', 'B32'),
         ('纸', '23'), ('温度计', '46'), ('秋千', 'B52')]
NEW20 = [('纺锤', 'B70', ['素纱襌衣', '陀螺']), ('缫丝', 'B71', ['素纱襌衣', '纺锤']), ('提花机', 'B72', ['计算机', '缫丝']),
         ('竹编', 'B73', ['油纸伞', '提花机']), ('曹冲称象', 'B74', ['杆秤', '螺旋提水']), ('水准', 'B75', ['墨斗', '虹吸']),
         ('石磨', 'B76', ['扇车', '豆腐点卤']), ('拓印', 'B77', ['活字印刷', '松烟墨']), ('毛笔', 'B78', ['松烟墨', '纸']),
         ('蹴鞠', 'B79', ['温度计', '秋千'])]

def s20_graph(c, t, i):
    corner_tag(c, '第二十季特辑 · 古法解密 7.0')
    c.text(60, 118, '织、量、写、玩：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD20):
        pos[name] = (340, 215 + k * 50)
    for k, (name, num, deps) in enumerate(NEW20):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 172, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第二十季新长出', 'sans', 24, MUTED, 'mm')
    newset = set(n for n, _, _ in NEW20)
    for k, (name, num, deps) in enumerate(NEW20):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in newset:
                pts = [(x0 + 110 if x0 < x1 else x0 - 110, y0), (x1 - 110 if x0 < x1 else x1 + 110, y1)]
                c.line(pts, mix(BG, COPPER, a * 0.9), 3)
                continue
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD20:
        x, y = pos[name]
        c.rect(x - 110, y - 20, x + 110, y + 20, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW20):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第七季：织、量、写、玩'),
                (8.2, 16, '纺锤、缫丝、提花机、竹编：从一团棉花，到一台会读程序的织机'),
                (16.2, 24, '曹冲称象和水准靠水来量；石磨、拓印、毛笔，是厨房和书房里的物理'),
                (24.2, 30, '最后一只打了气的鞠：老手艺里，处处是课本上的道理')], y=1040)

CLIPS = {
 'B79_回弹': (b79_bounce, 22), 'B79_气囊': (b79_gas, 22),
 'B79_片头': (titles.opening(BSER, VOL20, SB20, 9, '战国齐国蹴鞠 · 宋代充气鞠'), 7),
 'B79_片尾': (titles.closing(BSER, VOL20, SB20, 9, '下集：第二十季特辑 · 古法解密 7.0 回顾'), 7),
 'S20_依赖': (s20_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
