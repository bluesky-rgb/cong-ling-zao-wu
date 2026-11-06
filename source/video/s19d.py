"""第十九季（第六层）收尾：E111 人工智能、第十九季特辑（第六层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s19a import S19A, SER19, VOL19, ELEC

BOX = (190, 140, 90)
BEADS = [(230, 90, 80), (90, 170, 240), (240, 200, 80)]

# ---------------------------------------------------------------- E111 人工智能
def _box(c, x, y, counts, a=1.0, label=''):
    c.rect(x - 150, y - 90, x + 150, y + 90, fill=mix(BG, BOX, a), r=10)
    c.rect(x - 130, y - 70, x + 130, y + 70, fill=mix(BG, (110, 80, 50), a), r=8)
    rnd = random.Random(7)
    k = 0
    for ci, n in enumerate(counts):
        for j in range(n):
            bx = x - 110 + (k % 9) * 27
            by = y - 45 + (k // 9) * 28
            c.ellipse(bx, by, 11, 11, fill=mix(BG, BEADS[ci], a))
            k += 1
    if label:
        c.text(x, y + 120, label, 'sans', 22, mix(BG, MUTED, a), 'mm')

def _board(c, x, y, s, move=None, a=1.0):
    for r in range(3):
        for q in range(3):
            c.rect(x + q * s, y + r * s, x + (q + 1) * s - 4, y + (r + 1) * s - 4, fill=mix(BG, SHEET, a))
    for q in range(3):
        c.ellipse(x + q * s + s / 2, y + s / 2, s * 0.3, s * 0.3, fill=mix(BG, INK, a))
    for q in (0, 2):
        c.ellipse(x + q * s + s / 2, y + 2.5 * s, s * 0.3, s * 0.3, fill=mix(BG, NRED, a))
    c.ellipse(x + 1.5 * s, y + 1.5 * s, s * 0.3, s * 0.3, fill=mix(BG, NRED, a))
    for ci, (dx0, dy0, dx1, dy1) in enumerate(((0.5, 2.5, 0.5, 1.5), (0.5, 2.5, 1.5, 1.5), (2.5, 2.5, 2.5, 1.5))):
        if move is None or move == ci:
            c.arrow(x + dx0 * s, y + dy0 * s - s * 0.3, x + dx1 * s, y + dy1 * s + s * 0.3, mix(BG, BEADS[ci], a), 5, 14)

def e111_boxes(c, t, i):
    corner_tag(c, '第 111 集 · 输了就拿走一颗珠子')
    c.text(60, 96, '每个局面一个火柴盒，盒里的彩珠就是能走的步', 'serif', 40, INK)
    _board(c, 140, 230, 110)
    c.text(305, 600, '这个局面能走 3 步：红、蓝、黄', 'sans', 22, MUTED, 'mm')
    games = int(fade(t, 4, 18) * 8)
    counts = [3, 3, 3]
    for g in range(games):
        if counts[0] > 0 and g % 2 == 0: counts[0] -= 1
        elif counts[2] > 0 and g % 3 == 0: counts[2] -= 1
    counts = [max(0, x) for x in counts]
    _box(c, 900, 420, counts, 1.0, f'下了 {games} 盘')
    tot = sum(counts) or 1
    for ci in range(3):
        y = 300 + ci * 90
        p = counts[ci] / tot
        c.rect(1240, y - 22, 1240 + 500 * p, y + 22, fill=BEADS[ci], r=6)
        c.text(1760, y, f'{p * 100:.0f}%', 'mono', 26, INK, 'lm')
    c.text(1490, 240, '下一盘抽到这一步的机会', 'sans', 22, MUTED, 'mm')
    a = fade(t, 12, 13)
    if a > 0:
        c.rect(600, 640, 1840, 900, fill=mix(BG, SHEET, a), r=14)
        c.text(1220, 690, '规则只有两条', 'bold', 30, mix(BG, INK, a), 'mm')
        c.text(1220, 760, '轮到它走：从当前局面的盒子里随便摸一颗珠，照颜色走', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(1220, 820, '它输了：把最后一步摸出的那颗珠子没收', 'sans', 24, mix(BG, NRED, a), 'mm')
        c.text(1220, 870, '（马丁 · 加德纳的六兵棋机器，拍摄前核对）', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 4, '六兵棋：三乘三的格子，各三个兵。机器每遇到一个局面，就去找对应的火柴盒'),
                (4.2, 12, '盒里放着几种颜色的珠子，每种颜色是一步走法。摸到哪颗，就走哪步'),
                (12.2, 22, '输了，就把害它输的那颗珠子拿走：坏步越来越少，好步越来越多。没人教它，它自己变强了')], y=1010)

LAYERS = [3, 4, 2]

def e111_net(c, t, i):
    corner_tag(c, '第 111 集 · 从珠子到权重')
    c.text(60, 96, '神经网络：几十亿根「线」，每根有一个粗细，训练就是调粗细', 'serif', 40, INK)
    xs = [260, 640, 1020]
    pos = []
    for li, n in enumerate(LAYERS):
        pos.append([(xs[li], 560 + (k - (n - 1) / 2) * 150) for k in range(n)])
    prog = fade(t, 3, 18)
    rnd = random.Random(11)
    for li in range(2):
        for a_ in pos[li]:
            for b_ in pos[li + 1]:
                w0 = rnd.uniform(-1, 1)
                w1 = rnd.uniform(-1, 1) * 0.3 + (0.9 if (a_[1] < 560) == (b_[1] < 560) else -0.6)
                w = w0 + (w1 - w0) * prog
                col = SPARK if w > 0 else ELEC
                c.line([a_, b_], mix(BG, col, min(1, 0.3 + abs(w))), max(1, int(1 + 7 * abs(w))))
    for li, layer in enumerate(pos):
        for (x, y) in layer:
            c.ellipse(x, y, 34, 34, fill=SHEET, outline=INK, width=3)
    c.text(260, 300, '输入', 'sans', 24, MUTED, 'mm')
    c.text(1020, 300, '输出', 'sans', 24, MUTED, 'mm')
    ox, oy, W, H = 1260, 820, 560, 420
    c.line([(ox, oy), (ox + W, oy)], LINE, 3)
    c.line([(ox, oy), (ox, oy - H)], LINE, 3)
    n = int(60 * prog)
    pts = [(ox + W * k / 60, oy - H * (0.9 * math.exp(-k / 14) + 0.08 + 0.03 * math.sin(k * 1.7))) for k in range(n + 1)]
    if len(pts) > 1:
        c.line(pts, NRED, 4)
    c.text(ox + W / 2, oy + 40, '训练的轮数', 'sans', 22, MUTED, 'mm')
    c.text(ox + 10, oy - H - 30, '错得有多离谱', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 6, '火柴盒里珠子的多少，就是「这一步有多好」的分数。神经网络把这种分数叫权重'),
                (6.2, 13, '它把输入一层层传下去，每根线乘上一个权重；答错了，就把每根线的粗细往对的方向调一点'),
                (13.2, 22, '调上几百万次，错得越来越少：手机认出你的话、帮你修照片，靠的都是这一大堆调好的数字')], y=1010)

# ---------------------------------------------------------------- 第十九季特辑
OLD19 = [('晶体管', '92'), ('电灯', '60'), ('变压器', '75'), ('电磁铁', '56'), ('印刷机', '65'), ('计算机', '91'),
         ('电话', '72'), ('留声机', '73'), ('回声与雷达', '84'), ('电动机', '58'), ('蓄电池', '61'), ('摆钟', '45'),
         ('触摸屏', '96'), ('陀螺', 'B50'), ('制冷', '68'), ('照相', '55'), ('透镜', '52'), ('开关与逻辑门', '81')]
NEW19 = [('LED', '102', ['晶体管', '电灯']), ('无线充电', '103', ['变压器', '电磁铁']), ('3D 打印', '104', ['印刷机', '计算机']),
         ('语音识别', '105', ['电话', '计算机']), ('降噪耳机', '106', ['留声机', '回声与雷达']), ('电动汽车', '107', ['电动机', '蓄电池']),
         ('陀螺仪', '108', ['摆钟', '触摸屏', '陀螺']), ('空调热泵', '109', ['制冷', '电动机']),
         ('芯片光刻', '110', ['照相', '晶体管', '透镜']), ('人工智能', '111', ['计算机', '开关与逻辑门'])]

def s19_layer(c, t, i):
    corner_tag(c, '第十九季特辑 · 第六层')
    c.text(60, 118, '第六层：聪明的机器', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD19):
        pos[name] = (340, 200 + k * 44)
    for k, (name, num, deps) in enumerate(NEW19):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第十九季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW19):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD19:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW19):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第六层的十集：会发光、会充电、会打印、会听、会消音'),
                (8.2, 16, '晶体管和电灯长出 LED，变压器拿掉铁芯长出无线充电，电话和计算机长出语音识别'),
                (16.2, 24, '摆钟、陀螺和触摸屏缩进一粒芯片；照相加透镜，把晶体管「照」到硅片上'),
                (24.2, 30, '最后，计算机和逻辑门长出一台会自己学的机器')], y=1040)


CLIPS = {
 'E111_火柴盒': (e111_boxes, 22), 'E111_权重': (e111_net, 22),
 'E111_片头': (titles.opening(SER19, VOL19, S19A, 9, '1961 年火柴盒学井字棋 · 2016 年阿尔法围棋'), 7),
 'E111_片尾': (titles.closing(SER19, VOL19, S19A, 9, '下集：第十九季特辑 · 第六层回顾'), 7),
 'S19_第六层': (s19_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
