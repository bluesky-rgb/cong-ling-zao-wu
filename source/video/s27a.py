"""第二十七季（第十层：新材料）第一批：E142 塑料、E143 橡胶轮胎、E144 不锈钢 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S27A = [('142', '塑料'), ('143', '橡胶轮胎'), ('144', '不锈钢'), ('145', '铝'), ('146', '魔术贴'),
        ('147', '保温杯'), ('148', '不粘锅'), ('149', '纸尿裤'), ('150', '复合材料'), ('151', '气凝胶')]
SER27, VOL27 = '从零造物', '第二十七季 · 第十层：新材料'
CHAIN = [(120, 180, 240), (240, 150, 90), (130, 200, 140), (220, 120, 170), (230, 200, 90)]
IRON = (150, 155, 165)
RUST = (180, 90, 50)
CHROME = (170, 210, 230)
SULFUR = (240, 220, 80)
WATER_L = (110, 170, 230)


def walk(seed, n, step, x0, y0, box):
    rnd = random.Random(seed)
    pts = [(x0, y0)]
    a = rnd.uniform(0, 2 * math.pi)
    for _ in range(n - 1):
        a += rnd.uniform(-1.2, 1.2)
        x, y = pts[-1][0] + step * math.cos(a), pts[-1][1] + step * math.sin(a)
        if not (box[0] < x < box[2]):
            a = math.pi - a
            x = pts[-1][0] + step * math.cos(a)
        if not (box[1] < y < box[3]):
            a = -a
            y = pts[-1][1] + step * math.sin(a)
        pts.append((x, y))
    return pts


# ---------------------------------------------------------------- E142 塑料
def e142_chain(c, t, i):
    corner_tag(c, '第 142 集 · 小分子手拉手，连成长链')
    c.text(60, 96, '塑料由很多相同的小分子一个接一个连成长链；成千上万条长链缠在一起，就成了一块硬硬的固体', 'serif', 36, INK)
    box = (160, 220, 1760, 900)
    link = min(1, max(0, (t - 3) / 9))
    rnd = random.Random(1)
    for k in range(8):
        pts = walk(10 + k, 40, 26, rnd.uniform(400, 1500), rnd.uniform(350, 780), box)
        col = CHAIN[k % len(CHAIN)]
        nlink = int(39 * link)
        if nlink > 0:
            c.line(pts[:nlink + 1], col, 4)
        for j, (x, y) in enumerate(pts):
            jit = (1 - link) * 10
            c.ellipse(x + jit * math.sin(t * 5 + j + k), y + jit * math.cos(t * 4 + j), 7, 7, fill=col)
    lab = '一颗颗小分子（单体）' if link < 0.2 else ('正在连成长链（聚合）' if link < 1 else '长链缠在一起：塑料')
    c.rect(1380, 160, 1860, 220, fill=SHEET, r=10)
    c.text(1620, 190, lab, 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '一个个小分子到处乱跑，就像一盘散沙，捏不成形'),
                (7.2, 14, '让它们一个接一个手拉手，连成几千、几万个那么长的链，这叫聚合'),
                (14.2, 22, '长链互相缠在一起，谁也拉不开谁：就成了一块能成形的塑料（示意）。牛奶里的酪蛋白也是这样的长链')], y=1010)


def e142_heat(c, t, i):
    corner_tag(c, '第 142 集 · 一种加热会软，一种永远不软')
    c.text(60, 96, '有的塑料长链之间只是缠着，加热就能滑开、变软、重新成形；有的长链之间搭了「桥」，一旦成形再也不软', 'serif', 34, INK)
    heat = 0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi)
    for col_i, (lab, cross) in enumerate((('热塑：缠着', False), ('热固：搭了桥', True))):
        x0 = 140 + col_i * 880
        box = (x0, 260, x0 + 760, 860)
        c.rect(box[0] - 20, box[1] - 40, box[2] + 20, box[3] + 20, fill=mix(BG, (240, 120, 80), 0.25 * heat), r=14)
        c.text(x0 + 380, box[1] - 10, lab, 'bold', 26, INK, 'mm')
        allpts = []
        for k in range(5):
            drift = (heat * 50 if not cross else heat * 3)
            base = _coil(30 + k, x0 + 40, x0 + 720, 340 + k * 110, 0.2, n=30, amp=40)
            pts = [(x + drift * math.sin(t * 2 + k), y + drift * 0.5 * math.cos(t * 1.6 + k + j * 0.3)) for j, (x, y) in enumerate(base)]
            allpts.append(pts)
            c.line(pts, CHAIN[k], 4)
        if cross:
            for k in range(4):
                for j in range(3, 30, 6):
                    a, b = allpts[k][j], allpts[k + 1][j]
                    c.line([a, b], SULFUR, 3)
        st = ('软了，能重新捏' if heat > 0.6 else '硬的') if not cross else '还是硬的'
        c.text(x0 + 380, box[3] + 50, st, 'bold', 24, GREEN if not cross else SPARK, 'mm')
    c.text(960, 170, f'加热程度 {heat * 100:.0f}%（示意）', 'mono', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '矿泉水瓶、塑料袋是一类：长链之间只是缠着，加热后它们能滑开，塑料就软了'),
                (7.2, 14, '电源插座、锅把手是另一类：长链之间搭了很多「桥」，连成一张大网'),
                (14.2, 22, '网一旦织好，加热也滑不开，只会烧焦：所以锅把手不怕热（示意）。一百多年前的第一种合成塑料就是这一类')], y=1010)


# ---------------------------------------------------------------- E143 橡胶轮胎
def _coil(seed, x0, x1, y, stretch, n=40, amp=80):
    rnd = random.Random(seed)
    ph = [rnd.uniform(-1, 1) for _ in range(n)]
    pts = []
    for j in range(n):
        u = j / (n - 1)
        x = x0 + (x1 - x0) * u
        dy = amp * (1 - stretch) * ph[j]
        dx = 40 * (1 - stretch) * math.sin(j * 1.7 + seed)
        pts.append((x + dx, y + dy))
    return pts


def e143_entropy(c, t, i):
    corner_tag(c, '第 143 集 · 拉直了的长链，想缩回乱糟糟')
    c.text(60, 96, '橡胶的长链平时乱糟糟地卷着；拉长时被迫排直，放出热；松手时它们自己缩回乱糟糟的样子，吸走热', 'serif', 36, INK)
    ph = (t % 11) / 11
    st = min(1, ph * 3) if ph < 0.5 else max(0, 1 - (ph - 0.5) * 3)
    x0 = 300
    x1 = 900 + 700 * st
    for k in range(5):
        c.line(_coil(k, x0, x1, 380 + k * 90, st), CHAIN[k], 4)
    c.rect(x0 - 60, 300, x0, 800, fill=(90, 90, 100))
    c.rect(x1, 300, x1 + 60, 800, fill=(90, 90, 100))
    warm = 0
    if ph < 0.35:
        warm = st
    elif ph < 0.5:
        warm = 1 - (ph - 0.35) / 0.15 * 0.6
    else:
        warm = 0.4 - min(1, (ph - 0.5) * 3) * 0.9
    col = mix(BG, (240, 120, 80), max(0, warm)) if warm > 0 else mix(BG, (110, 170, 230), -warm)
    c.rect(1500, 860, 1860, 940, fill=col, r=12)
    c.text(1680, 900, '变热' if warm > 0.15 else ('变凉' if warm < -0.15 else '和室温差不多'), 'bold', 26, INK, 'mm')
    c.text(1460, 900, '贴额头的感觉：', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 7, '橡胶也是长链分子，平时每条链都卷成乱糟糟的一团，这是它们最「舒服」的样子'),
                (7.2, 14, '一拉，长链被迫排直，释放出一点热，橡皮筋就变热了'),
                (14.2, 22, '一松手，长链抖动着缩回乱糟糟的样子，要从周围吸热：所以橡皮筋变凉了（示意）')], y=1010)


def e143_vulcanize(c, t, i):
    corner_tag(c, '第 143 集 · 加硫，把长链连成网')
    c.text(60, 96, '生橡胶一热就黏、一冷就脆，长链会慢慢滑开；加硫加热后，硫原子在长链之间搭桥，橡胶就有了弹性又耐用', 'serif', 34, INK)
    pull = 0.5 - 0.5 * math.cos(t / 11 * 2 * math.pi)
    for col_i, (lab, cross) in enumerate((('生橡胶', False), ('硫化橡胶', True))):
        x0 = 160 + col_i * 860
        y0 = 300
        c.text(x0 + 360, y0 - 50, lab, 'bold', 26, INK, 'mm')
        stretch = pull * 0.8
        allp = []
        for k in range(5):
            slide = (pull * 120 * (k - 2) / 2) if not cross else 0
            pts = _coil(10 + k, x0 + 20 + slide, x0 + 520 + 200 * stretch + slide, y0 + 60 + k * 100, stretch * 0.7, amp=50)
            allp.append(pts)
            c.line(pts, CHAIN[k], 4)
        if cross:
            for k in range(4):
                for j in range(4, 40, 8):
                    c.line([allp[k][j], allp[k + 1][j]], SULFUR, 3)
                    c.ellipse((allp[k][j][0] + allp[k + 1][j][0]) / 2, (allp[k][j][1] + allp[k + 1][j][1]) / 2, 6, 6, fill=SULFUR)
        msg = '长链滑开，回不来' if not cross else '拉长后能弹回原样'
        c.text(x0 + 360, 860, msg, 'bold', 24, NRED if not cross else GREEN, 'mm')
    c.text(1660, 220, '黄色：硫搭的桥', 'sans', 20, SULFUR, 'mm')
    caps(c, t, [(0, 7, '从橡胶树里流出的生橡胶，夏天发黏、冬天变脆，长链拉一拉就互相滑开'),
                (7.2, 14, '有人把橡胶和硫黄一起加热：硫原子在长链之间搭起一座座小桥（这一步工厂里做，家里不做）'),
                (14.2, 22, '长链被连成一张网，拉长以后能弹回原样，也不怕冷热：这就是轮胎用的硫化橡胶（示意）')], y=1010)


# ---------------------------------------------------------------- E144 不锈钢
def e144_rust(c, t, i):
    corner_tag(c, '第 144 集 · 有水、有氧，铁才生锈')
    c.text(60, 96, '铁生锈要同时有水和空气里的氧；盐让水更容易导电，锈得更快；抹一层油把水和氧挡住，就几乎不锈', 'serif', 36, INK)
    day = min(5, t / 4)
    cups = [('清水', 2.0), ('盐水', 4.0), ('空杯', 0.5), ('抹油+清水', 0.4), ('不锈钢+盐水', 0.05)]
    for k, (lab, rate) in enumerate(cups):
        x = 240 + k * 340
        y = 360
        c.rect(x - 110, y - 60, x + 110, y + 260, outline=LINE, width=3, r=10)
        if lab != '空杯':
            c.rect(x - 106, y + 20, x + 106, y + 256, fill=mix(BG, WATER_L, 0.3 + (0.2 if '盐' in lab else 0)))
        r = min(1, rate * day / 20)
        col = mix(IRON, RUST, r) if '不锈钢' not in lab else CHROME
        if '不锈钢' in lab:
            c.ellipse(x, y + 20, 34, 24, fill=col)
            c.line([(x, y + 40), (x, y + 230)], col, 12)
        else:
            c.line([(x, y - 20), (x, y + 220)], col, 12)
            c.rect(x - 22, y - 30, x + 22, y - 16, fill=col)
        c.text(x, y + 300, lab, 'bold', 22, INK, 'mm')
        score = min(5, rate * day / 4)
        c.rect(x - 100, 760, x - 100 + 200 * score / 5, 800, fill=mix(SPARK, RUST, 0.5), r=6)
        c.text(x, 830, f'{score:.1f} 分', 'mono', 20, MUTED, 'mm')
    c.text(1720, 230, f'第 {day:.1f} 天', 'mono', 30, SPARK, 'mm')
    caps(c, t, [(0, 7, '铁原子很想把电子交给氧：只要水和氧同时在，铁就一点点变成红褐色的铁锈'),
                (7.2, 14, '盐水让电子跑得更快，锈得最快；空杯里只有潮气，锈得慢；抹了油的钉子被挡住了'),
                (14.2, 22, '而不锈钢勺子泡在盐水里几天，几乎还是亮的（锈的快慢为示意，以实测为准）')], y=1010)


def e144_film(c, t, i):
    corner_tag(c, '第 144 集 · 铬长出一层看不见的保护膜')
    c.text(60, 96, '不锈钢里加了不少铬：铬和氧一碰，立刻在表面长出一层极薄的膜，把里面的铁和外面的水、氧隔开', 'serif', 36, INK)
    cut = 6 < t < 22
    heal = min(1, max(0, (t - 9) / 6))
    for col_i, (lab, has) in enumerate((('普通钢', False), ('不锈钢', True))):
        x0 = 160 + col_i * 880
        top = 520
        c.text(x0 + 360, 230, lab, 'bold', 28, INK, 'mm')
        c.rect(x0, top, x0 + 720, 860, fill=IRON)
        rnd = random.Random(col_i)
        for k in range(36):
            x = x0 + 20 + (k % 12) * 58
            y = top + 40 + (k // 12) * 100
            c.ellipse(x, y, 10, 10, fill=mix(IRON, (90, 95, 105), 0.6))
            if has and k % 5 == 0:
                c.ellipse(x + 26, y + 30, 9, 9, fill=CHROME)
        for k in range(10):
            x = x0 + 60 + k * 66 + 10 * math.sin(t + k)
            y = 300 + ((t * 40 + k * 37) % 180)
            c.ellipse(x, y, 7, 7, fill=WATER_L)
            c.ellipse(x + 20, y + 14, 5, 5, fill=(230, 120, 110))
        if has:
            gap = (x0 + 330, x0 + 390) if cut else None
            if gap and heal < 1:
                c.rect(x0, top - 10, gap[0], top, fill=CHROME)
                c.rect(gap[1], top - 10, x0 + 720, top, fill=CHROME)
                c.rect(gap[0], top - 10 * heal, gap[1], top, fill=CHROME)
                c.text(x0 + 360, top - 50, '划破了……' if heal < 0.3 else '自己又长好了', 'bold', 22, SPARK, 'mm')
            else:
                c.rect(x0, top - 10, x0 + 720, top, fill=CHROME)
            c.text(x0 + 360, 900, '膜挡住水和氧，几乎不锈', 'bold', 22, GREEN, 'mm')
        else:
            for k in range(8):
                c.ellipse(x0 + 60 + k * 85, top + 4, 24, 12, fill=RUST)
            c.text(x0 + 360, 900, '锈是松的，挡不住，一层层往里烂', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '普通钢表面长出的铁锈又松又脆，水和氧能钻进去，一层层往里烂'),
                (7.2, 14, '不锈钢里加了铬：铬和氧结合，在表面长出一层只有几个纳米厚的致密薄膜（数值拍摄前核对）'),
                (14.2, 22, '就算被划破，铬又马上和氧结合，把膜补好：所以不锈钢勺子用了多年还是亮的（示意）')], y=1010)


CLIPS = {
 'E142_长链': (e142_chain, 22), 'E142_热塑热固': (e142_heat, 22),
 'E142_片头': (titles.opening(SER27, VOL27, S27A, 0, '1907 年贝克兰发明酚醛塑料'), 7),
 'E142_片尾': (titles.closing(SER27, VOL27, S27A, 0, '下集：一根橡皮筋拉长再松开，为什么会变凉？'), 7),
 'E143_熵弹性': (e143_entropy, 22), 'E143_硫化': (e143_vulcanize, 22),
 'E143_片头': (titles.opening(SER27, VOL27, S27A, 1, '1839 年固特异发明硫化橡胶'), 7),
 'E143_片尾': (titles.closing(SER27, VOL27, S27A, 1, '下集：铁钉放几天就锈了，不锈钢勺子为什么不锈？'), 7),
 'E144_生锈': (e144_rust, 22), 'E144_钝化膜': (e144_film, 22),
 'E144_片头': (titles.opening(SER27, VOL27, S27A, 2, '1913 年布里尔利发现不锈钢'), 7),
 'E144_片尾': (titles.closing(SER27, VOL27, S27A, 2, '下集：铝曾经比金子还贵，为什么现在便宜到能包饭团？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
