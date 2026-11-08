"""第二十六季收尾：B109 饾版套色、第二十六季特辑（古法解密 10.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import SB26, VOL26, WOOD

PAPER = (240, 232, 215)
PETAL = (205, 70, 80)
LEAFC = (80, 150, 90)
INKC = (40, 40, 45)
FOAM = (220, 220, 225)


def _flower(c, x, y, s, layers, off=None):
    off = off or {}
    if 'leaf' in layers:
        dx, dy = off.get('leaf', (0, 0))
        c.ellipse(x - 60 * s + dx, y + 70 * s + dy, 50 * s, 20 * s, fill=LEAFC)
        c.ellipse(x + 60 * s + dx, y + 90 * s + dy, 50 * s, 20 * s, fill=LEAFC)
        c.line([(x + dx, y + dy), (x + dx, y + 160 * s + dy)], LEAFC, max(2, int(6 * s)))
    if 'petal' in layers:
        dx, dy = off.get('petal', (0, 0))
        for k in range(5):
            a = k * 2 * math.pi / 5 - math.pi / 2
            c.ellipse(x + 45 * s * math.cos(a) + dx, y + 45 * s * math.sin(a) + dy, 32 * s, 32 * s, fill=PETAL)
        c.ellipse(x + dx, y + dy, 18 * s, 18 * s, fill=(240, 200, 90))
    if 'line' in layers:
        dx, dy = off.get('line', (0, 0))
        for k in range(5):
            a = k * 2 * math.pi / 5 - math.pi / 2
            c.ellipse(x + 45 * s * math.cos(a) + dx, y + 45 * s * math.sin(a) + dy, 32 * s, 32 * s, outline=INKC, width=max(1, int(3 * s)))


# ---------------------------------------------------------------- B109 饾版套色
def b109_blocks(c, t, i):
    corner_tag(c, 'B109 · 一种颜色一块版')
    c.text(60, 96, '把一幅彩色画按颜色拆成几块小版：叶子一块、花瓣一块、轮廓一块，依次印在同一张纸上', 'serif', 38, INK)
    names = [('leaf', '叶子版', LEAFC), ('petal', '花瓣版', PETAL), ('line', '轮廓版', INKC)]
    for k, (ly, lab, col) in enumerate(names):
        x = 260 + k * 330
        c.rect(x - 130, 240, x + 130, 520, fill=FOAM, r=10)
        _flower(c, x, 360, 0.8, [ly])
        c.text(x, 560, lab, 'bold', 24, INK, 'mm')
    step = min(3, int(t / 5.5))
    px, py = 1480, 560
    c.rect(px - 300, py - 300, px + 300, py + 300, fill=PAPER, r=4)
    c.line([(px - 320, py - 320), (px - 320, py + 320)], WOOD, 12)
    c.line([(px - 320, py - 320), (px + 320, py - 320)], WOOD, 12)
    c.text(px - 340, py - 340, '规矩（定位角）', 'sans', 20, MUTED, 'rm')
    _flower(c, px, py - 40, 1.6, [n for n, _, _ in names[:step]])
    if step < 3:
        ly, lab, col = names[step]
        s = (t % 5.5) / 5.5
        a = math.sin(math.pi * min(1, s * 1.4))
        bx = 260 + step * 330
        x = bx + (px - bx) * a
        y = 380 + (py - 380) * a
        c.rect(x - 130 * (1 + a), y - 140 * (1 + a), x + 130 * (1 + a), y + 140 * (1 + a), outline=mix(BG, col, 0.8), width=4, r=10)
        c.text(px, py + 340, f'第 {step + 1} 块：{lab}', 'bold', 24, SPARK, 'mm')
    else:
        c.text(px, py + 340, '三块版印完：一张彩色画', 'bold', 24, GREEN, 'mm')
    caps(c, t, [(0, 5.5, '一块木版只能刷一种颜色：要印彩色，就把画按颜色拆开，刻成好几块小版'),
                (5.7, 11, '先印浅的叶子，再印花瓣，最后印轮廓：每一块都只管自己那一种颜色'),
                (11.2, 16.5, '明代的笺谱，一幅画要拆成几十块版，叠印几十次（拍摄前核对）'),
                (16.7, 22, '颜色像拼图一样碎，所以叫「饾版」：难的不是刻，是每一次都要对准')], y=1010)


def b109_register(c, t, i):
    corner_tag(c, 'B109 · 卡住同一个角，就不会歪')
    c.text(60, 96, '纸每次都塞进同一个「规矩」角里，版也每次放在同一个位置：印十几次，颜色依然对得严丝合缝', 'serif', 36, INK)
    rnd = random.Random(6)
    k = min(5, int(t / 3.6) + 1)
    for col, (lab, sd) in enumerate((('凭眼睛对', 6.0), ('卡进规矩角', 0.8))):
        for j in range(5):
            x = 260 + j * 170 + col * 0
            y = 340 + col * 330
            if j >= k:
                c.rect(x - 70, y - 90, x + 70, y + 90, outline=mix(BG, LINE, 0.6), width=2, r=4)
                continue
            dx, dy = rnd.gauss(0, sd) * 3, rnd.gauss(0, sd) * 3
            c.rect(x - 70, y - 90, x + 70, y + 90, fill=PAPER, r=4)
            _flower(c, x, y - 20, 0.6, ['leaf', 'petal'], {'petal': (dx, dy)})
        c.text(140, 340 + col * 330 - 120, lab, 'bold', 26, INK, 'lm')
    c.rect(1180, 260, 1860, 820, fill=SHEET, r=14)
    c.text(1520, 300, '平均错位（示意）', 'bold', 24, INK, 'mm')
    for col, (lab, mm, colr) in enumerate((('凭眼睛对', 5.0, NRED), ('卡进规矩角', 0.7, GREEN))):
        y = 440 + col * 200
        w = 400 * mm / 5.0 * min(1, t / 10)
        c.rect(1240, y - 30, 1240 + max(4, w), y + 30, fill=colr, r=6)
        c.text(1240, y - 60, lab, 'sans', 22, INK, 'lm')
        c.text(1260 + max(4, w), y, f'约 {mm:g} 毫米', 'mono', 22, INK, 'lm')
    c.text(1520, 780, '数值以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '凭眼睛把纸放上去，每次都差一点点：花瓣跑到叶子外面，颜色就花了'),
                (7.2, 14, '在桌上固定一个 L 形的「规矩」，每张纸都推进这个角里，每块版也都放在同一个位置'),
                (14.2, 22, '纸和版的相对位置每次都一样，颜色就对上了：今天的彩色印刷机，也靠套准标记对齐（示意）')], y=1010)


# ---------------------------------------------------------------- 第二十六季特辑
OLD26 = [('杠杆与滑轮组', '39'), ('秋千', 'B52'), ('纺锤', 'B70'), ('缫丝', 'B71'), ('竹编', 'B73'), ('油纸伞', 'B58'),
         ('赵州桥', 'B6'), ('榫卯', 'B7'), ('船尾舵', 'B44'), ('逆风航行', '43'), ('风筝', 'B41'), ('指南鱼', 'B1'),
         ('杆秤', 'B43'), ('曹冲称象', 'B74'), ('古琴', 'B65'), ('陶埙', 'B42'), ('一钟双音', 'B11'), ('回音壁', 'B66'),
         ('活字印刷', 'B3'), ('拓印', 'B77')]
NEW26 = [('扁担', 'B100', ['杠杆与滑轮组', '秋千']), ('搓麻绳', 'B101', ['纺锤', '缫丝']), ('蓑衣', 'B102', ['竹编', '油纸伞']),
         ('虹桥', 'B103', ['赵州桥', '榫卯']), ('摇橹', 'B104', ['船尾舵', '逆风航行']), ('相风乌', 'B105', ['风筝', '指南鱼']),
         ('方升', 'B106', ['杆秤', '曹冲称象']), ('三分损益', 'B107', ['古琴', '陶埙']), ('鼓', 'B108', ['一钟双音', '回音壁']),
         ('饾版套色', 'B109', ['活字印刷', '拓印'])]


def s26_graph(c, t, i):
    corner_tag(c, '第二十六季特辑 · 古法解密 10.0')
    c.text(60, 118, '担、桥、风、律：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD26):
        pos[name] = (340, 196 + k * 40)
    for k, (name, num, deps) in enumerate(NEW26):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第二十六季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW26):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD26:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW26):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十季：担、桥、风、律'),
                (8.2, 16, '扁担会颤，麻绳靠捻，蓑衣靠搭；虹桥用短木编拱，摇橹斜着拨水'),
                (16.2, 24, '相风乌靠力矩迎风，方升靠尺寸统一「多少」'),
                (24.2, 30, '三分损益算出音阶，鼓皮越紧越高，饾版靠一个角对齐颜色：都是讲得清的道理')], y=1040)


CLIPS = {
 'B109_分版': (b109_blocks, 22), 'B109_规矩': (b109_register, 22),
 'B109_片头': (titles.opening(BSER, VOL26, SB26, 9, '明代胡正言《十竹斋笺谱》'), 7),
 'B109_片尾': (titles.closing(BSER, VOL26, SB26, 9, '下集：第二十六季特辑 · 古法解密 10.0 回顾'), 7),
 'S26_依赖': (s26_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
