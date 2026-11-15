"""第五十三季（第二十三层：超市与包装）第二批：E275 牛奶盒、E276 薯片袋、E277 鸡蛋托 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s53a import S53A, SER53, VOL53, PAPER, CARD, ALU, GAS

PLASTIC = (180, 210, 230)
MILK = (245, 245, 240)
LIGHT = (250, 220, 120)
CHIP = (230, 190, 90)
EGG = (240, 225, 200)
PULP = (190, 180, 165)


# ---------------------------------------------------------------- E275 牛奶盒
def e275_layers(c, t, i):
    corner_tag(c, '第 275 集 · 几层贴在一起')
    c.text(60, 96, '常温奶的盒壁不是一层纸：外面一层塑料、中间纸板、再一层塑料、一层极薄的铝箔，最里面还有塑料膜', 'serif', 36, INK)
    layers = [('塑料膜：防水、印刷', PLASTIC, 14), ('纸板：撑起形状', CARD, 70), ('塑料膜：粘合', PLASTIC, 12),
              ('铝箔：挡光、挡氧气', ALU, 10), ('塑料膜：贴着牛奶', PLASTIC, 16)]
    n = min(5, int(t / 3.5) + 1)
    y = 300
    sep = 30 * min(1.0, max(0.0, (t - 3) / 6))
    for k, (lab, col, h) in enumerate(layers):
        if k >= n:
            break
        c.rect(400, y, 1200, y + h, fill=mix(BG, col, 1.0), r=4)
        c.text(1260, y + h / 2, lab, 'bold', 26, INK, 'lm')
        y += h + sep
    c.text(800, 250, '盒外', 'sans', 24, MUTED, 'mm')
    c.text(800, y + 40, '牛奶', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '剪一块盒壁泡在温水里，一层层揭开'),
                (7.2, 14, '纸板撑形状，塑料膜防水封口'),
                (14.2, 22, '亮闪闪的那层是铝箔：薄得像纸，却能挡住光和氧气（层数以实测为准）')], y=1010)


def e275_block(c, t, i):
    corner_tag(c, '第 275 集 · 铝箔挡住光和空气')
    c.text(60, 96, '光和氧气会让牛奶变味，细菌会让它变质；先高温灭菌、无菌灌装，再用带铝箔的盒子关起来，常温也能放好几个月', 'serif', 36, INK)
    for j, (lab, foil) in enumerate([('普通白纸', False), ('带铝箔的那层', True)]):
        cx = 560 + j * 800
        c.ellipse(cx - 280, 560, 40, 40, fill=mix(BG, LIGHT, 1.0))
        c.text(cx - 280, 640, '手电', 'sans', 22, MUTED, 'mm')
        c.rect(cx - 20, 380, cx + 10, 740, fill=mix(BG, ALU if foil else PAPER, 1.0))
        for k in range(5):
            y = 460 + k * 50
            c.line([(cx - 240, 560), (cx - 20, y)], mix(BG, LIGHT, 0.7), 4)
            if not foil:
                c.line([(cx + 10, y), (cx + 220, y + (y - 560) * 0.6)], mix(BG, LIGHT, 0.5), 4)
        if foil:
            for k in range(4):
                ph = (t * 0.3 + k / 4) % 1
                c.ellipse(cx + 160, 420 + ph * 300, 10, 10, outline=mix(BG, (200, 80, 80), 1.0), width=3)
            c.text(cx + 160, 360, '氧气进不去', 'bold', 22, NRED, 'mm')
        c.text(cx, 840, lab + ('：几乎不透光' if foil else '：透出光来'), 'bold', 28, GREEN if foil else NRED, 'mm')
    caps(c, t, [(0, 7, '关灯，手电贴着普通白纸照：对面透出一片光'),
                (7.2, 14, '换成带铝箔的那层：一点光也透不过去'),
                (14.2, 22, '光、氧气、细菌都进不去，灭过菌的牛奶就能常温存放')], y=1010)


# ---------------------------------------------------------------- E276 薯片袋
def _bag(c, cx, cy, puff, chips, broken):
    w, h = 260, 200 + puff
    c.ellipse(cx, cy, w, h / 1.6, fill=mix(BG, PLASTIC, 0.35))
    c.rect(cx - w + 20, cy - h / 1.6 - 10, cx + w - 20, cy - h / 1.6 + 14, fill=mix(BG, PLASTIC, 0.8), r=4)
    random.seed(4)
    for k in range(chips):
        x = cx + random.uniform(-150, 150)
        y = cy + random.uniform(10, 60)
        if k < broken:
            c.ellipse(x - 10, y, 14, 8, fill=mix(BG, CHIP, 1.0))
            c.ellipse(x + 12, y + 4, 12, 7, fill=mix(BG, CHIP, 1.0))
        else:
            c.ellipse(x, y, 34, 16, fill=mix(BG, CHIP, 1.0))


def e276_cushion(c, t, i):
    corner_tag(c, '第 276 集 · 鼓起来像一个气垫')
    c.text(60, 96, '鼓鼓的袋子里一半是气：压一本书上去，先被压扁的是气，饼干不太碎；瘪袋子没有气垫，书直接压在饼干上', 'serif', 36, INK)
    press = min(1.0, max(0.0, (t - 4) / 4))
    for j, (lab, puff) in enumerate([('瘪袋子', False), ('鼓袋子', True)]):
        cx, cy = 560 + j * 800, 600
        p = (130 if puff else 0) * (1 - 0.4 * press)
        broken = int(8 * press) if not puff else int(1 * press)
        _bag(c, cx, cy, p, 10, broken)
        top = cy - (200 + p) / 1.6
        c.rect(cx - 220, top - 70, cx + 220, top - 10, fill=mix(BG, (120, 160, 210), 0.9), r=6)
        c.text(cx, top - 40, '书', 'bold', 26, (255, 255, 255), 'mm')
        c.text(cx, 880, f'{lab}：碎了 {broken} 片（示意）' if press > 0.9 else lab, 'bold', 28, GREEN if puff else NRED, 'mm')
    caps(c, t, [(0, 7, '两袋一样的饼干：一袋吹鼓封口，一袋挤出空气'),
                (7.2, 14, '各压一本书：鼓袋子的气先被压扁，饼干几乎不碎'),
                (14.2, 22, '摔下去也一样，气垫让撞击变轻（饼干不吃，以实测为准）')], y=1010)


def e276_nitrogen(c, t, i):
    corner_tag(c, '第 276 集 · 充的是氮气')
    c.text(60, 96, '空气里有氧气，油碰到氧气会慢慢变味；薯片袋里充的主要是氮气，氮气很「懒」，不和油起反应', 'serif', 36, INK)
    for j, (lab, n2) in enumerate([('充普通空气', False), ('充氮气', True)]):
        cx, cy = 560 + j * 800, 560
        _bag(c, cx, cy, 120, 8, 0)
        random.seed(10 + j)
        for k in range(30):
            x = cx + random.uniform(-200, 200)
            y = cy + random.uniform(-170, -10)
            ox = (not n2) and k % 5 == 0
            c.ellipse(x, y, 9, 9, fill=mix(BG, (220, 90, 80) if ox else GAS, 1.0))
        if not n2 and t > 7.2:
            for k in range(3):
                c.text(cx - 100 + k * 100, cy + 130, '变味', 'bold', 22, NRED, 'mm')
        c.text(cx, 860, lab, 'bold', 28, GREEN if n2 else NRED, 'mm')
    c.text(1500, 230, '蓝：氮气　红：氧气（示意）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '空气里大约五分之一是氧气（红点）'),
                (7.2, 14, '袋里留着氧气，薯片里的油会慢慢被氧化、变味'),
                (14.2, 22, '换成氮气：既当气垫，又不让油变味；读读包装上的「充氮」两个字')], y=1010)


# ---------------------------------------------------------------- E277 鸡蛋托
def e277_arch(c, t, i):
    corner_tag(c, '第 277 集 · 竖着的蛋壳像拱')
    c.text(60, 96, '蛋壳很薄，但它是拱形的：压在蛋的尖头上，力顺着弯弯的壳分散到四周，竖着的鸡蛋能扛住好几本书', 'serif', 36, INK)
    books = min(6, int(t / 3))
    gy = 860
    for k in range(4):
        cx = 420 + k * 360
        c.rect(cx - 90, gy - 90, cx + 90, gy, fill=mix(BG, PULP, 1.0), r=8)
        c.ellipse(cx, gy - 150, 70, 100, fill=mix(BG, EGG, 1.0))
        if t > 7.2:
            for s in (-1, 1):
                pts = [(cx + s * 70 * math.sin(a / 10 * math.pi / 2), gy - 150 - 100 * math.cos(a / 10 * math.pi / 2)) for a in range(11)]
                c.line(pts, GREEN, 4)
    top = gy - 250
    c.rect(300, top - 16, 1620, top, fill=mix(BG, CARD, 1.0))
    for b in range(books):
        c.rect(420 + b * 20, top - 16 - (b + 1) * 40, 1500 - b * 20, top - 16 - b * 40 - 4,
               fill=mix(BG, [(120, 160, 210), (200, 120, 110), (130, 180, 120)][b % 3], 0.9), r=4)
    c.text(1700, 300, f'{books} 本书', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '4 个鸡蛋竖着坐进蛋托四个角的窝里，上面盖一块硬纸板'),
                (7.2, 14, '一本一本放书：力顺着弯弯的蛋壳传下去，分散开'),
                (14.2, 22, '竖着的蛋壳最能扛压（鸡蛋套袋、在托盘上做，实验用不吃）')], y=1010)


def e277_cups(c, t, i):
    corner_tag(c, '第 277 集 · 一个蛋一个窝')
    c.text(60, 96, '鸡蛋放在平盘里，一晃就滚，蛋和蛋撞在一起；蛋托给每个蛋一个小窝，把它们隔开，软软的纸浆还能缓冲', 'serif', 36, INK)
    sh = 60 * math.sin(t * 3)
    # 平盘
    cx, cy = 560, 600
    c.rect(cx - 300 + sh, cy + 60, cx + 300 + sh, cy + 80, fill=mix(BG, (180, 180, 190), 1.0), r=6)
    e1 = cx - 80 + sh * 2.2
    e2 = cx + 80 + sh * 0.3
    if abs(e1 - e2) < 150:
        e1 = e2 - 150
        c.text(cx, cy - 120, '撞！', 'bold', 40, NRED, 'mm')
    for x in (e1, e2):
        c.ellipse(x, cy + 15, 75, 45, fill=mix(BG, EGG, 1.0))
    c.text(cx, 860, '平盘：滚来滚去、互相撞', 'bold', 28, NRED, 'mm')
    # 蛋托
    cx = 1360
    c.rect(cx - 320 + sh, cy + 30, cx + 320 + sh, cy + 90, fill=mix(BG, PULP, 1.0), r=10)
    for k in (-1, 1):
        x = cx + k * 150 + sh
        c.arc(x, cy + 30, 90, 50, 0, 180, mix(BG, PULP, 0.7), 10)
        c.ellipse(x, cy - 40, 55, 80, fill=mix(BG, EGG, 1.0))
    c.text(cx, 860, '蛋托：各待各的窝', 'bold', 28, GREEN, 'mm')
    caps(c, t, [(0, 7, '两个鸡蛋横放在平盘里，轻轻一晃就滚到一起'),
                (7.2, 14, '放回蛋托，每个蛋坐在自己的窝里，晃也碰不到'),
                (14.2, 22, '纸浆软，碰一下能变形，把冲击吸收掉一点')], y=1010)


CLIPS = {
 'E275_分层': (e275_layers, 22), 'E275_挡光': (e275_block, 22),
 'E275_片头': (titles.opening(SER53, VOL53, S53A, 3, '20 世纪 60 年代出现无菌纸盒'), 7),
 'E275_片尾': (titles.closing(SER53, VOL53, S53A, 3, '下集：薯片袋为什么一半是空气？'), 7),
 'E276_气垫': (e276_cushion, 22), 'E276_充氮': (e276_nitrogen, 22),
 'E276_片头': (titles.opening(SER53, VOL53, S53A, 4, '零食开始充氮气包装'), 7),
 'E276_片尾': (titles.closing(SER53, VOL53, S53A, 4, '下集：一托鸡蛋为什么压不碎？'), 7),
 'E277_拱壳': (e277_arch, 22), 'E277_小窝': (e277_cups, 22),
 'E277_片头': (titles.opening(SER53, VOL53, S53A, 5, '1911 年出现纸浆鸡蛋托'), 7),
 'E277_片尾': (titles.closing(SER53, VOL53, S53A, 5, '下集：小泡泡怎么护住东西？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
