"""第二十七季（第十层：新材料）第二批：E145 铝、E146 魔术贴、E147 保温杯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s27a import S27A, SER27, VOL27, CHAIN, IRON, WATER_L

ALU = (200, 205, 215)
OXY = (230, 110, 100)
HOOK = (120, 180, 240)
LOOP = (240, 170, 110)
HOT = (235, 110, 80)
STEEL = (170, 175, 185)


# ---------------------------------------------------------------- E145 铝
def e145_electrolysis(c, t, i):
    corner_tag(c, '第 145 集 · 用电把铝和氧拆开')
    c.text(60, 96, '铝和氧抱得太紧，用炭火烧也拆不开；把氧化铝熔在熔盐里通上大电流，铝跑向负极、氧跑向正极，才把它们分开', 'serif', 34, INK)
    x0, y0, x1, y1 = 320, 360, 1300, 880
    c.rect(x0, y0, x1, y1, outline=LINE, width=6, r=10)
    c.rect(x0 + 6, y0 + 80, x1 - 6, y1 - 6, fill=mix(BG, (240, 160, 80), 0.35))
    c.rect(x0 + 6, y1 - 90, x1 - 6, y1 - 6, fill=mix(BG, ALU, 0.6 + 0.3 * min(1, t / 22)))
    c.text((x0 + x1) / 2, y1 + 40, '负极（槽底）：铝液越积越多', 'sans', 22, INK, 'mm')
    for k in range(3):
        ax = x0 + 180 + k * 310
        c.rect(ax - 60, y0 - 100, ax + 60, y0 + 230, fill=(70, 70, 75), r=6)
    c.text((x0 + x1) / 2, y0 - 130, '正极（炭块）：氧在这里变成气体跑掉', 'sans', 22, INK, 'mm')
    rnd = random.Random(2)
    for k in range(40):
        bx = x0 + 60 + rnd.random() * (x1 - x0 - 120)
        by0 = y0 + 200 + rnd.random() * 160
        ph = (t * 0.5 + rnd.random()) % 1
        c.ellipse(bx, by0 + ph * 80, 8, 8, fill=ALU)
        c.ellipse(bx + 18, by0 - ph * 120, 7, 7, fill=OXY)
    c.rect(1400, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1630, 340, '要的电（示意）', 'bold', 24, INK, 'mm')
    c.text(1630, 420, '每炼 1 吨铝', 'sans', 22, INK, 'mm')
    c.text(1630, 490, '约 1.3–1.5 万度电', 'mono', 26, SPARK, 'mm')
    c.text(1630, 560, '（数值拍摄前核对）', 'sans', 18, MUTED, 'mm')
    c.ellipse(1460, 720, 8, 8, fill=ALU)
    c.text(1480, 720, '铝', 'sans', 20, INK, 'lm')
    c.ellipse(1560, 720, 7, 7, fill=OXY)
    c.text(1580, 720, '氧', 'sans', 20, INK, 'lm')
    caps(c, t, [(0, 7, '铝是地壳里最多的金属，可它总和氧抱在一起，躲在矿石里，炭火烧也拆不开'),
                (7.2, 14, '1886 年前后，两个年轻人想到：把氧化铝熔进熔盐里，再通上大电流（拍摄前核对）'),
                (14.2, 22, '铝被拉到负极、沉在槽底，氧在正极跑掉：有了便宜的电，铝才从比金子贵变成能包饭团（示意）')], y=1010)


def e145_boat(c, t, i):
    corner_tag(c, '第 145 集 · 又轻又能浮')
    c.text(60, 96, '同样大小的一块，铝只有铁的三分之一重；铝箔折成船，排开的水比自己重得多，还能多载一堆硬币', 'serif', 36, INK)
    for k, (lab, d, col) in enumerate((('铝', 2.7, ALU), ('铁', 7.9, IRON))):
        x = 300 + k * 320
        c.rect(x - 70, 360, x + 70, 500, fill=col, r=6)
        c.text(x, 330, lab, 'bold', 26, INK, 'mm')
        c.rect(x - 40, 760 - d * 30, x + 40, 760, fill=mix(BG, col, 0.8), r=4)
        c.text(x, 790, f'{d} 克/立方厘米', 'mono', 18, MUTED, 'mm')
    c.line([(200, 760), (720, 760)], LINE, 2)
    n = int(min(20, t * 1.1))
    sink = 10 + n * 4
    wx0, wx1, wl = 900, 1820, 600
    c.rect(wx0, wl, wx1, 900, fill=mix(BG, WATER_L, 0.35))
    bx = (wx0 + wx1) / 2
    top = wl - 60 + sink
    c.poly([(bx - 220, top), (bx + 220, top), (bx + 180, top + 80), (bx - 180, top + 80)], ALU)
    for k in range(n):
        c.ellipse(bx - 150 + (k % 10) * 34, top - 8 - (k // 10) * 14, 15, 6, fill=(220, 180, 80))
    c.line([(wx0, wl), (wx1, wl)], WATER_L, 3)
    c.text(bx, 900 + 30, f'船上 {n} 枚硬币：船排开的水还比船加硬币重，就不沉（示意）', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '同样大小的一块，铝只有铁的三分之一左右重：做飞机、易拉罐、饭盒都省力'),
                (7.2, 14, '一张铝箔揉成团会沉，折成船却能浮：船把水推开，被推开的水有多重，水就往上托多大的力'),
                (14.2, 22, '只要船推开的水比船加货还重，就能浮着：薄薄的铝，比钢更适合做轻的东西')], y=1010)


# ---------------------------------------------------------------- E146 魔术贴
def _hook(c, x, y, s, col, open_=0.0):
    c.line([(x, y), (x, y - 50 * s)], col, max(2, int(4 * s)))
    c.arc(x + 12 * s, y - 50 * s, 12 * s, 12 * s, 180, 360 - 60 * open_, col, max(2, int(4 * s)))


def e146_hooks(c, t, i):
    corner_tag(c, '第 146 集 · 成千上万个小钩钩住小圈')
    c.text(60, 96, '一面长满了带弯钩的硬丝，一面是软软的小线圈；按在一起，钩子钻进线圈挂住，成千上万个一起使劲', 'serif', 36, INK)
    close = min(1, max(0, (t - 3) / 6))
    gap = 400 * (1 - close)
    top_y = 560 - 60 - gap * 0.5
    bot_y = 560 + 60 + gap * 0.5
    c.rect(200, bot_y, 1720, bot_y + 40, fill=mix(BG, HOOK, 0.6), r=6)
    c.rect(200, top_y - 40, 1720, top_y, fill=mix(BG, LOOP, 0.6), r=6)
    for k in range(24):
        x = 240 + k * 62
        _hook(c, x, bot_y, 1.6, HOOK)
        lx = x + 20
        ly = top_y
        c.ellipse(lx, ly + 40, 22, 40, outline=LOOP, width=3)
    c.text(120, bot_y + 20, '钩面', 'bold', 22, HOOK, 'rm')
    c.text(120, top_y - 20, '圈面', 'bold', 22, LOOP, 'rm')
    if close >= 1:
        c.text(960, 940, '每一个钩只挂住一点点力，几千个加起来就很牢', 'bold', 24, GREEN, 'mm')
    caps(c, t, [(0, 7, '1940 年代，一位工程师遛狗回来，发现衣服和狗毛上粘满了苍耳（故事细节拍摄前核对）'),
                (7.2, 14, '他用显微镜一看：苍耳上长满了带弯钩的小刺，正好钩住布上的线圈'),
                (14.2, 22, '照着做：一面做小钩，一面做小圈，一按就挂住，用力一撕又能分开，能用好几千次（示意）')], y=1010)


def e146_peel(c, t, i):
    corner_tag(c, '第 146 集 · 撕开容易，平拉很难')
    c.text(60, 96, '顺着往外撕，每一刻只有边上一排钩在受力，一排一排地松开；平着拉，所有钩一起使劲，难多了', 'serif', 38, INK)
    ph = (t % 11) / 11
    for row, (lab, peel) in enumerate((('撕开（剥离）', True), ('平拉（剪切）', False))):
        y = 360 + row * 300
        c.text(160, y - 120, lab, 'bold', 26, INK, 'lm')
        c.rect(300, y, 1300, y + 30, fill=mix(BG, HOOK, 0.6), r=4)
        if peel:
            k_open = int(ph * 22)
            pts = []
            for j in range(23):
                x = 300 + j * 45
                if j < k_open:
                    yy = y - (k_open - j) * 6
                else:
                    yy = y - 6
                pts.append((x, yy))
            c.line(pts, mix(BG, LOOP, 0.9), 12)
            for j in range(23):
                x = 300 + j * 45
                load = 1.0 if j == k_open else 0
                c.ellipse(x, y - 2, 7, 7, fill=NRED if load else (GREEN if j > k_open else MUTED))
            c.arrow(300, y - k_open * 6 - 20, 300, y - k_open * 6 - 90, SPARK, 5, 16)
        else:
            shift = 30 * math.sin(ph * math.pi) * 0.3
            c.rect(300 + shift, y - 30, 1300 + shift, y - 6, fill=mix(BG, LOOP, 0.9), r=4)
            for j in range(23):
                c.ellipse(300 + j * 45, y - 2, 7, 7, fill=NRED)
            c.arrow(1310, y - 18, 1440, y - 18, SPARK, 5, 16)
    c.rect(1500, 300, 1860, 760, fill=SHEET, r=14)
    c.text(1680, 340, '红点：正在受力的钩', 'sans', 20, NRED, 'mm')
    c.text(1680, 420, '撕开：只有 1 排', 'bold', 24, INK, 'mm')
    c.text(1680, 480, '平拉：全部一起', 'bold', 24, INK, 'mm')
    c.text(1680, 560, '平拉要的力', 'sans', 22, INK, 'mm')
    c.text(1680, 610, '是撕开的好几倍', 'sans', 22, INK, 'mm')
    c.text(1680, 680, '（倍数以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '揭魔术贴时，我们总是从一头往外撕：每一刻只有最边上的一排钩在受力'),
                (7.2, 14, '一排松开，下一排再受力：力不大，嘶啦一声就开了'),
                (14.2, 22, '可平着拉，所有钩一起使劲，难得多：所以鞋子、背包上的魔术贴，平时怎么拽都不会开（示意）')], y=1010)


# ---------------------------------------------------------------- E147 保温杯
def e147_paths(c, t, i):
    corner_tag(c, '第 147 集 · 热有三条路，一条条堵上')
    c.text(60, 96, '热从杯子里跑出去有三条路：顺着杯壁传（传导）、热空气带走（对流）、像阳光一样照出去（辐射）', 'serif', 38, INK)
    stage = min(3, int(t / 5.5))
    cx, cy = 560, 600
    c.rect(cx - 200, cy - 260, cx + 200, cy + 260, outline=STEEL, width=10, r=30)
    c.rect(cx - 160, cy - 220, cx + 160, cy + 220, outline=mix(STEEL, (240, 240, 250), 0.6 if stage >= 3 else 0), width=8 if stage >= 3 else 6, r=24)
    c.rect(cx - 150, cy - 150, cx + 150, cy + 210, fill=mix(BG, HOT, 0.6), r=20)
    if stage >= 1:
        c.text(cx, cy + 300, '两层壁之间：真空', 'sans', 22, MUTED, 'mm')
    if stage >= 2:
        c.rect(cx - 170, cy - 300, cx + 170, cy - 240, fill=(90, 90, 100), r=10)
    paths = [('传导', (cx + 160, cy), (cx + 360, cy)), ('对流', (cx, cy - 230), (cx, cy - 330)), ('辐射', (cx - 160, cy + 80), (cx - 380, cy + 160))]
    blocked = [stage >= 1, stage >= 2, stage >= 3]
    for k, ((nm, a, b), bl) in enumerate(zip(paths, blocked)):
        col = mix(BG, HOT, 0.3) if bl else HOT
        for j in range(3):
            s = ((t * 0.6 + j / 3) % 1)
            x = a[0] + (b[0] - a[0]) * s * (0.25 if bl else 1)
            y = a[1] + (b[1] - a[1]) * s * (0.25 if bl else 1)
            c.ellipse(x, y, 9, 9, fill=col)
        c.text(b[0], b[1] - 30, nm + ('：堵住' if bl else ''), 'bold', 22, GREEN if bl else HOT, 'mm')
    steps = ['热从三条路往外跑', '① 两层壁中间抽真空：传导和杯壁间的对流没了路', '② 盖紧盖子：热空气出不去', '③ 内壁镀亮：把热辐射反射回去']
    c.rect(1100, 300, 1860, 760, fill=SHEET, r=14)
    for k, sline in enumerate(steps):
        c.text(1130, 360 + k * 90, sline, 'bold' if k == stage else 'sans', 22, SPARK if k == stage else (INK if k < stage else MUTED), 'lm')
    caps(c, t, [(0, 5.5, '热水的热会从三条路跑掉：顺着杯壁一个个分子往外传，热空气往上带，还有看不见的热辐射'),
                (5.7, 11, '保温杯是两层钢，中间抽成真空：没有空气，热几乎没法从里层传到外层'),
                (11.2, 16.5, '盖子盖紧，杯口的热空气出不去'),
                (16.7, 22, '里层的外面做得很亮，把热辐射反射回去：三条路都堵上，热水一夜还烫（示意）')], y=1010)


def e147_cooling(c, t, i):
    corner_tag(c, '第 147 集 · 三个杯子的降温曲线')
    c.text(60, 96, '同样一杯 70 ℃ 的热水：玻璃杯掉得最快，陶瓷杯慢一点，保温杯一小时后几乎没怎么变', 'serif', 38, INK)
    gx0, gx1, gy0, gy1 = 220, 1500, 880, 260
    c.line([(gx0, gy0), (gx1, gy0)], LINE, 2)
    c.line([(gx0, gy0), (gx0, gy1)], LINE, 2)
    for v in (20, 30, 40, 50, 60, 70):
        y = gy0 - (gy0 - gy1) * (v - 20) / 50
        c.text(gx0 - 16, y, f'{v}', 'mono', 18, MUTED, 'rm')
    for m in (0, 15, 30, 45, 60):
        c.text(gx0 + (gx1 - gx0) * m / 60, gy0 + 24, f'{m}', 'mono', 18, MUTED, 'mm')
    c.text((gx0 + gx1) / 2, gy0 + 60, '分钟', 'sans', 20, MUTED, 'mm')
    c.text(gx0, gy1 - 30, '℃', 'sans', 20, MUTED, 'mm')
    now = min(60, t / 20 * 60)
    cups = [('玻璃杯', 1 / 25, (120, 180, 240)), ('陶瓷杯', 1 / 35, (240, 170, 110)), ('保温杯', 1 / 900, GREEN)]
    for k, (nm, kk, col) in enumerate(cups):
        pts = []
        for m in range(0, int(now) + 1):
            T = 22 + 48 * math.exp(-kk * m)
            pts.append((gx0 + (gx1 - gx0) * m / 60, gy0 - (gy0 - gy1) * (T - 20) / 50))
        if len(pts) > 1:
            c.line(pts, col, 4)
        T = 22 + 48 * math.exp(-kk * now)
        c.rect(1560, 320 + k * 150, 1860, 430 + k * 150, fill=SHEET, r=12)
        c.text(1710, 350 + k * 150, nm, 'bold', 24, col, 'mm')
        c.text(1710, 400 + k * 150, f'{T:.0f} ℃', 'mono', 30, INK, 'mm')
    caps(c, t, [(0, 7, '三个杯子各倒 200 毫升 70 ℃ 的热水，每 10 分钟用温度计测一次'),
                (7.2, 14, '玻璃杯和陶瓷杯越热掉得越快，慢慢往室温靠；保温杯的线几乎是平的'),
                (14.2, 22, '再把保温杯打开盖子测一次：少了一条路，掉得就快多了（曲线为示意，以实测为准）')], y=1010)


CLIPS = {
 'E145_电解': (e145_electrolysis, 22), 'E145_铝箔船': (e145_boat, 22),
 'E145_片头': (titles.opening(SER27, VOL27, S27A, 3, '1886 年霍尔与埃鲁发明电解炼铝'), 7),
 'E145_片尾': (titles.closing(SER27, VOL27, S27A, 3, '下集：一边是小钩、一边是小圈，为什么一按就粘牢？'), 7),
 'E146_钩环': (e146_hooks, 22), 'E146_撕与拉': (e146_peel, 22),
 'E146_片头': (titles.opening(SER27, VOL27, S27A, 4, '1955 年德·梅斯特拉尔申请魔术贴专利'), 7),
 'E146_片尾': (titles.closing(SER27, VOL27, S27A, 4, '下集：为什么保温杯里的热水，第二天早上还是烫的？'), 7),
 'E147_三条路': (e147_paths, 22), 'E147_降温曲线': (e147_cooling, 22),
 'E147_片头': (titles.opening(SER27, VOL27, S27A, 5, '1892 年杜瓦发明真空瓶'), 7),
 'E147_片尾': (titles.closing(SER27, VOL27, S27A, 5, '下集：为什么煎蛋粘铁锅，在不粘锅上却能滑来滑去？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
