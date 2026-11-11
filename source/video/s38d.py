"""第三十八季（古法解密 16.0）收官：B169 锣 + 第三十八季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s38a import SB38, VOL38, AIR

BRASS = (205, 165, 80)


# ---------------------------------------------------------------- B169 锣
def b169_vibrate(c, t, i):
    corner_tag(c, 'B169 · 锣面振动发声')
    c.text(60, 96, '槌子一敲，锣面整块前后振动，推着空气一胀一缩，声音就传了出去；手一按，振动马上停', 'serif', 36, INK)
    cx, cy = 640, 560
    hit = t % 7
    amp = 0 if hit < 0.5 else 40 * math.exp(-(hit - 0.5) * 0.5)
    if 5.5 < hit:
        amp *= max(0, 1 - (hit - 5.5) * 3)
    w = amp * math.sin(t * 40)
    c.ellipse(cx + w * 0.3, cy, 60 + abs(w) * 0.2, 300, fill=mix(BG, BRASS, 0.95))
    c.ellipse(cx + w, cy, 26, 150, fill=mix(BG, BRASS, 0.7))
    c.line([(cx, cy - 300), (cx, 180)], INK, 3)
    if hit < 0.5:
        c.line([(cx - 260 + hit * 400, cy), (cx - 400 + hit * 400, cy + 120)], mix(BG, WOOD, 1.0), 14)
        c.ellipse(cx - 260 + hit * 400, cy, 26, 26, fill=mix(BG, (230, 225, 215), 1.0))
    for k in range(6):
        r = 120 + ((t * 300 + k * 110) % 700)
        a = max(0, amp / 40) * (1 - (r - 120) / 700)
        c.arc(cx + 60, cy, r, r * 1.2, -50, 50, mix(BG, SPARK, a), 3)
    if 5.5 < hit:
        c.ellipse(cx - 20, cy + 120, 50, 40, fill=mix(BG, (200, 150, 110), 0.95))
        c.text(cx - 180, cy + 120, '手按住 →', 'sans', 24, INK, 'mm')
    c.rect(1380, 300, 1860, 560, fill=SHEET, r=12)
    c.text(1620, 350, '响度（示意）', 'bold', 26, INK, 'mm')
    c.rect(1440, 420, 1800, 460, fill=mix(BG, LINE, 0.6), r=8)
    c.rect(1440, 420, 1440 + 360 * amp / 40, 460, fill=SPARK, r=8)
    c.text(1620, 510, '耳朵离锣至少 50 厘米', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '锣是一大片薄铜，槌子一敲，整块锣面前后振动'),
                (7.2, 14, '锣面推着空气一胀一缩，声音一圈圈传出去，慢慢变小'),
                (14.2, 22, '手一按住，锣面振不动了，声音马上就没了（示意）')], y=1010)


def b169_glide(c, t, i):
    corner_tag(c, 'B169 · 越敲音越滑')
    c.text(60, 96, '京剧里的锣：敲下去的一瞬间振得最猛，锣面被拉紧，音高；振动变小后，音慢慢滑下来（有的锣反过来往上滑）', 'serif', 32, INK)
    x0, y0, W, H = 260, 300, 1100, 520
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 50, '时间（秒）', 'sans', 22, MUTED, 'mm')
    c.text(x0 - 30, y0 + 20, '音高', 'sans', 22, MUTED, 'rm')
    for j, (lab, col, f) in enumerate([('轻敲', mix(BG, SPARK, 0.5), lambda s: 0.45 - 0.05 * math.exp(-s * 1.5)),
                                       ('重敲', SPARK, lambda s: 0.45 + 0.35 * math.exp(-s * 1.2))]):
        pts = []
        for k in range(60):
            s = k / 59 * 3
            if s > t * 0.25:
                break
            pts.append((x0 + 40 + s / 3 * (W - 80), y0 + H - 40 - f(s) * (H - 80)))
        if len(pts) > 1:
            c.line(pts, col, 5)
        c.text(x0 + W + 30, y0 + 80 + j * 60, lab, 'bold', 24, col, 'lm')
    c.rect(1520, 640, 1880, 860, fill=SHEET, r=12)
    c.text(1700, 690, '敲中间 / 敲边缘', 'bold', 24, INK, 'mm')
    c.text(1700, 750, '音高也不一样', 'sans', 22, MUTED, 'mm')
    c.text(1700, 800, '用调音器 App 读', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '轻轻一敲，音高几乎不变'),
                (7.2, 14, '重重一敲，锣面振得猛、被拉得更紧，刚敲下去音最高，然后慢慢滑下来'),
                (14.2, 22, '锣面中间鼓起的形状决定它往上滑还是往下滑：锅盖实验以实测为准（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十八季特辑
OLD38 = [('唧筒', 'B27'), ('水排', 'B4'), ('蓑衣', 'B102'), ('屋檐举折', 'B67'), ('秋千', 'B52'), ('石磨', 'B76'),
         ('陶埙', 'B42'), ('笛子', 'B124'), ('算筹', 'B134'), ('七巧板', 'B60'), ('逆风航行', '43'), ('船尾舵', 'B44'),
         ('墨斗', 'B61'), ('水准', 'B75'), ('筛子', 'B114'), ('曹冲称象', 'B74'), ('漏刻', 'B13'), ('沙漏', 'B96'),
         ('鼓', 'B108'), ('一钟双音', '11')]
NEW38 = [('风箱', 'B160', ['唧筒', '水排']), ('斗笠', 'B161', ['蓑衣', '屋檐举折']), ('连枷', 'B162', ['秋千', '石磨']),
         ('哨子', 'B163', ['陶埙', '笛子']), ('九宫格', 'B164', ['算筹', '七巧板']), ('硬帆', 'B165', ['逆风航行', '船尾舵']),
         ('垂线', 'B166', ['墨斗', '水准']), ('淘金', 'B167', ['筛子', '曹冲称象']), ('沉碗', 'B168', ['漏刻', '沙漏']),
         ('锣', 'B169', ['鼓', '一钟双音'])]


def s38_graph(c, t, i):
    corner_tag(c, '第三十八季特辑 · 古法解密 16.0')
    c.text(60, 118, '风、雨、田、声与数：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD38):
        pos[name] = (340, 218 + k * 38)
    for k, (name, num, deps) in enumerate(NEW38):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十八季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW38):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD38:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW38):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十六季：风、雨、田、声与数'),
                (8.2, 16, '唧筒和水排长出风箱，蓑衣和屋檐长出斗笠，秋千和石磨长出连枷，陶埙和笛子长出哨子'),
                (16.2, 24, '算筹长出九宫格，船尾舵长出硬帆，墨斗长出垂线，筛子长出淘金，漏刻长出沉碗'),
                (24.2, 30, '最后，鼓和一钟双音一起，长出了越敲音越滑的锣')], y=1040)


CLIPS = {
 'B169_振动': (b169_vibrate, 22), 'B169_滑音': (b169_glide, 22),
 'B169_片头': (titles.opening(BSER, VOL38, SB38, 9, '汉代墓葬已出土铜锣'), 7),
 'B169_片尾': (titles.closing(BSER, VOL38, SB38, 9, '下集：第三十八季特辑 · 古法解密 16.0 回顾'), 7),
 'S38_依赖': (s38_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
