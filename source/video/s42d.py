"""第四十二季（古法解密 18.0）收官：B189 号角 + 第四十二季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s42a import SB42, VOL42

HORN = (210, 190, 150)
WAVE = (120, 180, 230)


# ---------------------------------------------------------------- B189 号角
def b189_flare(c, t, i):
    corner_tag(c, 'B189 · 喇叭口把声音「送」出去')
    c.text(60, 96, '直管口小，声音大多被弹回管里；号角的口慢慢张开，把振动一点点交给更多空气：传出去更响，也更朝前', 'serif', 34, INK)
    for j, flare in enumerate([False, True]):
        cy = 380 + j * 340
        x0, x1 = 200, 900
        if flare:
            top = [(x0 + k * 35, cy - 18 - 90 * (k / 20) ** 2.5) for k in range(21)]
        else:
            top = [(x0 + k * 35, cy - 18) for k in range(21)]
        bot = [(x, 2 * cy - y) for x, y in top]
        c.poly(top + bot[::-1], mix(BG, HORN, 0.95))
        c.ellipse(x0 - 20, cy, 22, 22, fill=NRED)
        n = 7 if flare else 3
        amp = 1.0 if flare else 0.45
        for k in range(6):
            rm = 540 if flare else 260
            r = ((t * 90 + k * 90) % rm)
            a = max(0.0, 1 - r / rm) * amp
            if a <= 0.02: continue
            ha = 30 if flare else 70
            c.arc(x1, cy, r + 30, r + 30, -ha, ha, mix(BG, WAVE, a), 4 if flare else 2)
        if not flare:
            for k in range(3):
                xx = x0 + ((t * 300 + k * 230) % 700)
                c.arrow(xx, cy, xx - 60, cy, mix(BG, NRED, 0.7), 3, 10)
        c.text(1650, cy, '张开的号角：响、朝前' if flare else '直管：大部分被弹回', 'bold', 26, GREEN if flare else NRED, 'mm')
    c.text(960, 900, '同样的吹法，用手机分贝 App 在 1 米外读数，以实测为准', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '嘴唇在吹口上振动，振动在管里来回传；管口太小，大部分又被弹回管子里'),
                (7.2, 14, '号角的口一路慢慢张大，像楼梯一样，让振动一级一级地交给更多的空气'),
                (14.2, 22, '交出去的多，传出去就响；口朝哪里，声音就主要往哪里去（示意）')], y=1010)


def b189_lips(c, t, i):
    corner_tag(c, 'B189 · 嘴唇是簧片，管子挑音高')
    c.text(60, 96, '嘴唇像两片簧片一开一合；管里的空气柱只在几个固定频率上共振，所以没有按孔的号角只能吹出几个音', 'serif', 35, INK)
    x0, x1, cy = 300, 1500, 420
    c.rect(x0, cy - 50, x1, cy + 50, fill=mix(BG, HORN, 0.6), r=8)
    n = 1 + int(t / 7) % 3
    pts = []
    for k in range(121):
        u = k / 120
        y = cy + 40 * math.sin(math.pi * n * u / 1) * math.cos(t * 6 * n) * (1 if n else 0)
        pts.append((x0 + u * (x1 - x0), y))
    c.line(pts, WAVE, 5)
    op = 10 + 8 * math.sin(t * 20 * n)
    c.ellipse(x0 - 40, cy - op, 26, 12, fill=NRED)
    c.ellipse(x0 - 40, cy + op, 26, 12, fill=NRED)
    c.text(x0 - 40, cy + 90, '嘴唇', 'sans', 22, MUTED, 'mm')
    for k in range(1, 5):
        x = 400 + (k - 1) * 300
        on = (k == n)
        c.rect(x - 110, 640, x + 110, 760, fill=mix(BG, SPARK if on else SHEET, 0.9 if on else 1.0), outline=LINE, width=2, r=10)
        c.text(x, 680, f'第 {k} 个音', 'bold', 26, INK, 'mm')
        c.text(x, 725, f'约 {k} 倍', 'mono', 22, INK if on else MUTED, 'mm')
    c.text(960, 820, '嘴唇绷得越紧、吹得越急，就跳到更高的那个音（示意）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '嘴唇贴着吹口「噗噗」地振，管子里的空气柱跟着一起来回振动'),
                (7.2, 14, '空气柱只在几个固定的频率上振得最起劲：最低的那个，和它的 2 倍、3 倍……'),
                (14.2, 22, '嘴唇绷紧一点，就跳到更高的一档：所以军号只靠嘴唇就能吹出几个音（示意）')], y=1010)


OLD42 = [('油纸伞', 'B58'), ('走马灯', 'B23'), ('松烟墨', 'B32'), ('毛笔', 'B78'), ('结绳记事', 'B135'), ('绳结', 'B151'),
         ('搓麻绳', 'B101'), ('瓦片', 'B137'), ('冰鉴与藏冰', 'B12'), ('竹夫人', 'B132'), ('古琴', 'B65'), ('三分损益', 'B107'),
         ('斗拱', 'B47'), ('榫卯', 'B7'), ('腰舟', 'B139'), ('边架艇', 'B144'), ('缆桩', 'B111'), ('船尾舵', 'B44'),
         ('陶埙', 'B42'), ('锣', 'B169')]
NEW42 = [('灯笼', 'B180', ['油纸伞', '走马灯']), ('砚台', 'B181', ['松烟墨', '毛笔']), ('竹简', 'B182', ['结绳记事', '绳结']),
         ('搓衣板', 'B183', ['搓麻绳', '瓦片']), ('汤婆子', 'B184', ['冰鉴与藏冰', '竹夫人']), ('二胡', 'B185', ['古琴', '三分损益']),
         ('栈道', 'B186', ['斗拱', '榫卯']), ('浮桥', 'B187', ['腰舟', '边架艇']), ('锚', 'B188', ['缆桩', '船尾舵']),
         ('号角', 'B189', ['陶埙', '锣'])]


def s42_graph(c, t, i):
    corner_tag(c, '第四十二季特辑 · 古法解密 18.0')
    c.text(60, 118, '屋里与河上：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD42):
        pos[name] = (342, 218 + k * 38)
    for k, (name, num, deps) in enumerate(NEW42):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十二季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW42):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD42:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW42):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十八季：屋里与河上'),
                (8.2, 16, '油纸伞和走马灯长出灯笼，松烟墨和毛笔长出砚台，绳结长出竹简，搓麻绳长出搓衣板'),
                (16.2, 24, '冰鉴和竹夫人长出汤婆子，古琴长出二胡，斗拱和榫卯长出栈道，腰舟长出浮桥'),
                (24.2, 30, '缆桩和船尾舵长出锚；最后，陶埙和锣一起，长出了吹得最远的号角')], y=1040)


CLIPS = {
 'B189_喇叭口': (b189_flare, 22), 'B189_嘴唇': (b189_lips, 22),
 'B189_片头': (titles.opening(BSER, VOL42, SB42, 9, '商周已有角，后世军中用号角传令'), 7),
 'B189_片尾': (titles.closing(BSER, VOL42, SB42, 9, '下集：第四十二季特辑 · 古法解密 18.0 回顾'), 7),
 'S42_依赖': (s42_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
