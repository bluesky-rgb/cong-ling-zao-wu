"""第五十四季收尾：B249 发簪 + 第五十四季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s54a import SB54, VOL54, SKIN

YARN = (60, 50, 45)
STICK = (200, 160, 100)


def _bun(c, cx, cy, wraps, pin):
    for k in range(wraps):
        r = 60 + k * 14
        c.arc(cx, cy, r, r * 0.8, k * 40, k * 40 + 300, mix(BG, YARN, 1.0), 12)
    if pin:
        c.line([(cx - 220, cy + 60), (cx + 220, cy - 60)], mix(BG, STICK, 1.0), 14)


def b249_wrap(c, t, i):
    corner_tag(c, 'B249 · 头发绕着簪子越拉越紧')
    c.text(60, 96, '盘好的发髻插进一根簪子：簪子挑住一部分头发横过去，头发一往外散，就绕着簪子被拉紧，压得越紧、摩擦越大', 'serif', 36, INK)
    for j, (lab, pin) in enumerate([('不插簪子', False), ('插上簪子', True)]):
        cx, cy = 560 + j * 800, 460
        c.ellipse(cx, cy + 160, 200, 120, fill=mix(BG, SKIN, 0.9))
        loose = (min(1.0, max(0.0, (t - 4) / 5)) if not pin else 0)
        if loose > 0.3:
            for k in range(10):
                x = cx - 120 + k * 26
                c.line([(x, cy + 40), (x + 20 * math.sin(k + t), cy + 300 * loose)], mix(BG, YARN, 1.0), 6)
        else:
            _bun(c, cx, cy, 5, pin)
        if pin and t > 7.2:
            for k in range(6):
                a = math.radians(-40 + k * 16)
                c.arrow(cx + 200 * math.cos(a), cy + 160 * math.sin(a), cx + 120 * math.cos(a), cy + 96 * math.sin(a), GREEN, 4, 12)
        c.text(cx, 860, lab + ('：一松手就散' if not pin else '：越拉越紧'), 'bold', 28, NRED if not pin else GREEN, 'mm')
    caps(c, t, [(0, 7, '毛线拧几圈盘成发髻，一松手就慢慢散开'),
                (7.2, 14, '用钝头筷子挑起一部分斜插过去：头发被挡住散不开'),
                (14.2, 22, '一往外拉，头发绕着筷子压得更紧，摩擦把发髻锁住（毛线实验）')], y=1010)


def b249_hang(c, t, i):
    corner_tag(c, 'B249 · 插了簪子能挂住多重')
    c.text(60, 96, '把毛线「马尾」挂在门把手上，下面吊一个小水瓶，一点点加水：插了筷子的发髻能挂住的重量多得多', 'serif', 36, INK)
    w = min(400, t * 22)
    for j, (lab, pin, cap) in enumerate([('不插筷子', False, 60), ('插上筷子', True, 400)]):
        cx = 560 + j * 800
        c.rect(cx - 40, 220, cx + 40, 260, fill=mix(BG, (150, 150, 160), 1.0), r=8)
        held = w <= cap
        _bun(c, cx, 360, 4, pin)
        if held:
            c.line([(cx, 420), (cx, 640)], mix(BG, YARN, 1.0), 10)
            hh = 60 + w / 4
            c.rect(cx - 60, 640, cx + 60, 640 + hh, fill=mix(BG, (120, 170, 230), 0.8), r=12)
            c.text(cx, 660 + hh + 30, f'{w:.0f} 克', 'bold', 28, INK, 'mm')
        else:
            c.text(cx, 640, '散了，瓶子掉下来', 'bold', 28, NRED, 'mm')
        c.text(cx, 930, lab, 'bold', 28, GREEN if pin else NRED, 'mm')
    c.text(960, 200, '克数是示意，以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '小瓶挂在毛线末端，一点点往里加水'),
                (7.2, 14, '没插筷子的发髻，加一点水就被拉散了'),
                (14.2, 22, '插了筷子的，挂了几百克还稳稳的；本集只用钝头筷子')], y=1010)


OLD54 = [('马鞍', 'B233'), ('剪刀', 'B136'), ('纺锤', 'B70'), ('提花机', 'B72'), ('杵臼', 'B216'), ('搓衣板', 'B183'),
         ('点茶', 'B158'), ('装裱', 'B148'), ('素纱襌衣', 'B33'), ('汤婆子', 'B184'), ('毛毡', 'B159'), ('草鞋', 'B204'),
         ('绳结', 'B151'), ('绣花绷子', 'B120'), ('木桶', 'B110'), ('香篆钟', 'B85'), ('筷子', 'B53'), ('筷子提米', 'B171')]
NEW54 = [('顶针', 'B240', ['马鞍', '剪刀']), ('腰机', 'B241', ['纺锤', '提花机']), ('捣衣杵', 'B242', ['杵臼', '搓衣板']),
         ('皂角', 'B243', ['搓衣板', '点茶']), ('浆衣', 'B244', ['装裱', '素纱襌衣']), ('火斗', 'B245', ['汤婆子', '毛毡']),
         ('千层底', 'B246', ['草鞋', '装裱']), ('回针', 'B247', ['绳结', '绣花绷子']), ('樟木箱', 'B248', ['木桶', '香篆钟']),
         ('发簪', 'B249', ['筷子', '筷子提米'])]


def s54_graph(c, t, i):
    corner_tag(c, '第五十四季特辑 · 古法解密 24.0')
    c.text(60, 118, '衣与针线：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD54):
        pos[name] = (342, 224 + k * 37)
    for k, (name, num, deps) in enumerate(NEW54):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 182, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十四季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW54):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD54:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW54):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 18, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第二十四季：衣与针线'),
                (8.2, 16, '马鞍和剪刀长出顶针，纺锤和提花机长出腰机，杵臼和搓衣板长出捣衣杵，点茶长出皂角，装裱长出浆衣'),
                (16.2, 24, '汤婆子和毛毡长出火斗，草鞋和装裱长出千层底，绳结长出回针，木桶和香篆钟长出樟木箱'),
                (24.2, 30, '最后，筷子和筷子提米一起，长出了发簪')], y=1040)


CLIPS = {
 'B249_缠绕': (b249_wrap, 22), 'B249_挂重': (b249_hang, 22),
 'B249_片头': (titles.opening(BSER, VOL54, SB54, 9, '商周时已用骨笄绾发'), 7),
 'B249_片尾': (titles.closing(BSER, VOL54, SB54, 9, '下集：第五十四季特辑 · 古法解密 24.0 回顾'), 7),
 'S54_依赖': (s54_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
