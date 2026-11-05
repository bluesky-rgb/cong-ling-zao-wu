"""第十六季收尾：B59 曲辕犁、第十六季特辑（古法解密 5.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s16a import SB16, VOL16, WOOD

SOIL = (130, 95, 60)
SOIL2 = (165, 125, 80)

# ---------------------------------------------------------------- B59 曲辕犁
def b59_pull(c, t, i):
    corner_tag(c, 'B59 · 拉力的方向')
    c.text(60, 96, '同样的拉力：斜着往上拉，一部分力在把犁往上提', 'serif', 40, INK)
    for k, (nm, deg, col) in enumerate((('拉线陡（约 35°）', 35, NRED), ('拉线平（约 15°）', 15, GREEN))):
        a = fade(t, 1 + k * 6, 2 + k * 6)
        if a <= 0: continue
        x0, y0 = 260 + k * 860, 720
        c.rect(x0 - 200, y0, x0 + 560, y0 + 120, fill=mix(BG, SOIL, a))
        # plough share
        c.poly([(x0 - 40, y0 + 50), (x0 + 60, y0 + 30), (x0 + 60, y0 + 70)], mix(BG, (150, 150, 160), a))
        th = math.radians(deg)
        L = 300
        ex, ey = x0 + 60 + L * math.cos(th), y0 + 40 - L * math.sin(th)
        c.line([(x0 + 60, y0 + 40), (ex, ey)], mix(BG, WOOD, a), 10)
        c.text(x0 + 180, y0 - 300, nm, 'bold', 28, mix(BG, INK, a), 'mm')
        b = fade(t, 2.5 + k * 6, 4 + k * 6)
        F = 190
        c.arrow(ex, ey, ex + F * math.cos(th) * b, ey - F * math.sin(th) * b, mix(BG, SPARK, a), 6, 20)
        c.arrow(ex, ey, ex + F * math.cos(th) * b, ey, mix(BG, GREEN, a), 4, 16)
        c.arrow(ex + F * math.cos(th) * b, ey, ex + F * math.cos(th) * b, ey - F * math.sin(th) * b, mix(BG, NRED, a), 4, 16)
        c.text(ex + F * math.cos(th) * b + 20, ey - F * math.sin(th) * b / 2, f'往上提 {math.sin(th) * 100:.0f}%', 'sans', 22, mix(BG, NRED, a), 'lm')
        c.text(ex + 40, ey + 34, f'往前拉 {math.cos(th) * 100:.0f}%', 'sans', 22, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 7, '牛拉犁，力是顺着绳子和犁辕的方向斜着往上的'),
                (7.2, 14, '这个力可以拆成两份：往前拉的那份在耕地，往上提的那份在把犁拔出土'),
                (14.2, 22, '拉线越陡，越多的力在「拔犁」。犁辕弯下来、挂钩低一点，拉线就平一些（以实测为准）')], y=1010)

def b59_mould(c, t, i):
    corner_tag(c, 'B59 · 犁壁把土翻过来')
    c.text(60, 96, '犁铧切开一条土，犁壁把它翻个身，草压到下面', 'serif', 40, INK)
    base = 760
    c.rect(0, base - 40, 1920, base + 200, fill=SOIL)
    for k in range(5):
        x = 260 + k * 300
        prog = fade(t, 2 + k * 2.5, 4 + k * 2.5)
        ang = math.pi * prog
        cx, cy = x + 120 * prog, base - 100
        w, h = 240, 120
        pts = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        rp = [(cx + px * math.cos(ang) - py * math.sin(ang), cy + px * math.sin(ang) + py * math.cos(ang)) for px, py in pts]
        c.poly(rp, SOIL2)
        gx, gy = cx + 0 * math.cos(ang) - (-h / 2) * math.sin(ang), cy + 0 * math.sin(ang) + (-h / 2) * math.cos(ang)
        for j in range(5):
            q = ang - math.pi / 2
            c.line([(gx - 60 + j * 30, gy), (gx - 60 + j * 30 + 25 * math.cos(q), gy + 25 * math.sin(q))], GREEN, 4)
    a = fade(t, 14, 15)
    c.rect(200, 220, 1720, 360, fill=mix(BG, SHEET, a), r=12)
    c.text(960, 265, '唐代陆龟蒙《耒耜经》记下了曲辕犁的十一个部件，犁壁就是其中之一（拍摄前核对）', 'sans', 26, mix(BG, INK, a), 'mm')
    c.text(960, 315, '翻过来的土把杂草埋在下面，下层的土翻上来晒太阳：接第 29 集轮作', 'sans', 24, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '犁铧像一把斜铲，把土切开一条'),
                (6.2, 13, '后面弯弯的犁壁接着把这条土托起来、翻个身'),
                (13.2, 22, '草压到了下面，底下的土翻上来晒太阳：一趟走完，地就耕好了')], y=1010)

# ---------------------------------------------------------------- 第十六季特辑
OLD16 = [('齿轮与轴承', '41'), ('公道杯', 'B20'), ('欹器', 'B21'), ('摆钟', '45'), ('杠杆与滑轮组', '39'), ('杆秤', 'B43'),
         ('数字与 0', '48'), ('机械计算器', '80'), ('开关与逻辑门', '81'), ('曲柄连杆', '40'), ('蒸汽发电', '10'), ('蒸发冷却罐', '38'),
         ('松烟墨', 'B32'), ('扎染', 'B45'), ('马轭', '42'), ('轮作固氮', '29')]
NEW16 = [('陀螺', 'B50', ['齿轮与轴承']), ('不倒翁', 'B51', ['欹器', '公道杯']), ('秋千', 'B52', ['摆钟']), ('筷子', 'B53', ['杠杆与滑轮组', '杆秤']),
         ('算盘', 'B54', ['数字与 0', '机械计算器']), ('九连环', 'B55', ['数字与 0', '开关与逻辑门']), ('扇车', 'B56', ['曲柄连杆']),
         ('蒸笼', 'B57', ['蒸汽发电', '蒸发冷却罐']), ('油纸伞', 'B58', ['松烟墨', '扎染']), ('曲辕犁', 'B59', ['马轭', '轮作固氮'])]

def s16_graph(c, t, i):
    corner_tag(c, '第十六季特辑 · 古法解密 5.0')
    c.text(60, 118, '玩、算、吃、用：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD16):
        pos[name] = (340, 205 + k * 50)
    for k, (name, num, deps) in enumerate(NEW16):
        pos[name] = (1180 + (210 if name in ('不倒翁', '筷子', '九连环', '蒸笼', '曲辕犁') else 0), 215 + k * 76)
    c.text(340, 165, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1280, 165, '第十六季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW16):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD16:
        x, y = pos[name]
        c.rect(x - 110, y - 21, x + 110, y + 21, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW16):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第五季：孩子手里的玩具，厨房和田里的老工具'),
                (8.2, 16, '陀螺、不倒翁、秋千讲转动和重心；筷子、算盘、九连环讲杠杆和数'),
                (16.2, 24, '扇车、蒸笼、油纸伞、曲辕犁：风、蒸汽、水和土，各有各的物理'),
                (24.2, 30, '越是天天见的东西，越藏着一条讲得清的道理')], y=1040)

CLIPS = {
 'B59_拉力': (b59_pull, 22), 'B59_犁壁': (b59_mould, 22),
 'B59_片头': (titles.opening(BSER, VOL16, SB16, 9, '唐 · 陆龟蒙《耒耜经》'), 7),
 'B59_片尾': (titles.closing(BSER, VOL16, SB16, 9, '下集：第十六季特辑 · 古法解密 5.0 回顾'), 7),
 'S16_依赖': (s16_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
