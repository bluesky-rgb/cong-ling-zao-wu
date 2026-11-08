"""第三十一季（第十二层：城市里的机器）第三批：E168 光控路灯、E169 自动售货机、E170 下水道 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L
from s31a import S31A, SER31, VOL31, CAR, RED, WATER

LAMP = (250, 220, 130)
SKY_D = (40, 60, 110)
COINC = (210, 185, 90)
SAND = (200, 175, 120)


def lux_at(t, T=22):
    return 2000 * math.exp(-6.5 * t / T)


# ---------------------------------------------------------------- E168 光控路灯
def e168_ldr(c, t, i):
    corner_tag(c, '第 168 集 · 天越暗，光敏电阻越大')
    c.text(60, 96, '路灯头上有一个「看天色」的光敏元件：光越暗，它的电阻越大；暗到设定的程度，电路就把灯打开', 'serif', 38, INK)
    lx = lux_at(t)
    sky = mix((20, 24, 40), (140, 180, 230), min(1, lx / 2000) ** 0.5)
    c.rect(100, 200, 900, 880, fill=sky, r=12)
    on = lx < 30
    px = 500
    c.rect(px - 10, 420, px + 10, 880, fill=METAL)
    c.line([(px, 430), (px + 140, 400)], METAL, 10)
    c.rect(px + 120, 400, px + 200, 430, fill=LAMP if on else (90, 90, 100), r=6)
    if on:
        c.poly([(px + 125, 430), (px + 195, 430), (px + 300, 880), (px + 20, 880)], mix(sky, LAMP, 0.35))
    c.ellipse(px, 410, 12, 12, fill=(240, 240, 240))
    c.text(px - 30, 380, '光敏开关', 'sans', 20, (240, 240, 240), 'rm')
    R = 5 * (1000 / max(lx, 1)) ** 0.7
    c.rect(1050, 260, 1840, 820, fill=SHEET, r=14)
    c.text(1445, 310, '傍晚的读数（示意）', 'bold', 24, INK, 'mm')
    c.text(1445, 400, f'亮度 {lx:,.0f} 勒克斯', 'mono', 30, SPARK, 'mm')
    c.text(1445, 480, f'光敏电阻约 {R:,.0f} 千欧', 'mono', 30, INK, 'mm')
    c.text(1445, 580, '路灯：亮了' if on else '路灯：灭着', 'bold', 36, GREEN if on else MUTED, 'mm')
    c.text(1445, 680, '设定：低于约 30 勒克斯就亮（以产品为准）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '下午外面有好几千勒克斯，光敏电阻只有几千欧'),
                (7.2, 14, '太阳落山，亮度一路往下掉，光敏电阻越来越大'),
                (14.2, 22, '暗到设定的程度，电路翻转，路灯「啪」地亮了：没人按，也不用定时（数值为示意）')], y=1010)


def e168_hyst(c, t, i):
    corner_tag(c, '第 168 集 · 亮和灭，设两条线')
    c.text(60, 96, '亮和灭若用同一条线，天色一晃路灯就忽亮忽灭；所以暗到 A 才亮、亮到 B 才灭，中间留回差', 'serif', 34, INK)
    x0, x1 = 200, 1700
    for k, (lab, hyst) in enumerate((('只有一条线', False), ('留了回差', True))):
        y0 = 260 + k * 340
        h = 220
        c.text(x0 - 20, y0 - 20, lab, 'bold', 26, INK, 'lm')
        c.rect(x0, y0, x1, y0 + h, outline=LINE, width=2, r=6)
        on_th, off_th = (0.40, 0.40) if not hyst else (0.32, 0.52)
        c.line([(x0, y0 + h * (1 - on_th)), (x1, y0 + h * (1 - on_th))], NRED, 2)
        if hyst:
            c.line([(x0, y0 + h * (1 - off_th)), (x1, y0 + h * (1 - off_th))], GREEN, 2)
        state = False
        pts = []
        ons = []
        n = 300
        shown = int(n * min(1, t / 18))
        for j in range(shown):
            u = j / n
            lv = 0.75 - 0.5 * u + 0.06 * math.sin(u * 60) + (0.12 if 0.55 < u < 0.57 else 0)
            x = x0 + (x1 - x0) * u
            pts.append((x, y0 + h * (1 - lv)))
            if not state and lv < on_th:
                state = True
            elif state and lv > off_th:
                state = False
            ons.append((x, state))
        if len(pts) > 1:
            c.line(pts, (150, 190, 240), 3)
        for (x, st) in ons:
            if st:
                c.rect(x, y0 + h + 10, x + 6, y0 + h + 30, fill=LAMP)
        flips = sum(1 for a, b in zip(ons, ons[1:]) if a[1] != b[1])
        c.text(x1 + 30, y0 + h / 2, f'开关 {flips} 次', 'mono', 22, SPARK, 'lm')
    c.text(960, 940, '蓝线：亮度　红线：暗到这里就亮　绿线：亮到这里才灭　黄条：灯亮着（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '傍晚的亮度不是平平地往下降，云飘过、车灯一照，都会晃一晃'),
                (7.2, 14, '只有一条线的话，亮度在线附近一晃，灯就亮了灭、灭了亮'),
                (14.2, 22, '亮和灭各设一条线，中间留出空当：灯只亮一次，稳稳当当（示意）')], y=1010)


# ---------------------------------------------------------------- E169 自动售货机
COINS = [('1 元', 25.0, 6.1), ('5 角', 20.5, 3.8), ('1 角', 19.0, 3.2)]


def e169_slots(c, t, i):
    corner_tag(c, '第 169 集 · 第一关：量直径')
    c.text(60, 96, '硬币沿斜轨滚下，轨道边的缺口从窄到宽：小硬币先从窄口掉下去，大的滚得更远', 'serif', 36, INK)
    x0, y0, x1, y1 = 200, 320, 1600, 620
    c.line([(x0, y0), (x1, y1)], METAL, 10)
    slots = [(0.35, '19–20 毫米口', 19.5), (0.6, '20–22 毫米口', 21.5), (0.85, '24–26 毫米口', 26)]
    for (u, lab, wmm) in slots:
        sx, sy = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
        c.rect(sx - wmm * 2.4, sy + 6, sx + wmm * 2.4, sy + 30, fill=BG)
        c.line([(sx, sy + 30), (sx, 900)], mix(BG, LINE, 0.5), 2)
        c.text(sx, 940, lab, 'sans', 20, MUTED, 'mm')
    order = [2, 1, 0]
    for k, ci in enumerate(order):
        name, d, w = COINS[ci]
        tt = t - k * 5
        if tt < 0:
            continue
        target = slots[k][0]
        u = min(target, tt / 4 * target)
        sx, sy = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
        if u >= target:
            fall = min(1, (tt - 4) / 1.5)
            sy = sy + (860 - sy) * max(0, fall)
        r = d * 1.6
        c.ellipse(sx, sy - r, r, r, fill=COINC, outline=mix(COINC, INK, 0.3), width=2)
        c.text(sx, sy - r, name, 'bold', 18, INK, 'mm')
    c.text(1700, 300, '直径（实测为准）', 'bold', 22, INK, 'mm')
    for k, (name, d, w) in enumerate(COINS):
        c.text(1700, 350 + k * 44, f'{name}  约 {d} 毫米', 'mono', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '投币口进去，硬币先滚上一条斜轨'),
                (7.2, 14, '轨道边上的缺口从窄到宽：1 角最小，第一个口就掉下去'),
                (14.2, 22, '5 角、1 元越滚越远，各进各的口：大小不对的东西，第一关就分出来了（直径以实测为准）')], y=1010)


def e169_checks(c, t, i):
    corner_tag(c, '第 169 集 · 三关：尺寸、重量、材质')
    c.text(60, 96, '一块铁片做得和硬币一样大，第一关能骗过去；可第二关称重、第三关用线圈和磁铁「感觉」金属，就露馅了', 'serif', 38, INK)
    items = [('真 1 元', True, True, True), ('一样大的铁垫片', True, False, False), ('一样大的铝片', True, False, False), ('游戏币', False, None, None)]
    heads = ['尺寸', '重量', '材质']
    x0 = 540
    for j, hd in enumerate(heads):
        c.text(x0 + j * 300, 260, hd, 'bold', 28, INK, 'mm')
    for k, row in enumerate(items):
        y = 360 + k * 130
        c.text(240, y, row[0], 'bold', 26, INK, 'mm')
        for j in range(3):
            a = fade(t, 3 + j * 5 + k * 0.6, 4 + j * 5 + k * 0.6)
            v = row[1 + j]
            if a <= 0 or v is None:
                if v is None and a > 0:
                    c.text(x0 + j * 300, y, '—', 'mono', 30, MUTED, 'mm')
                continue
            c.text(x0 + j * 300, y, '通过' if v else '退回', 'bold', 30, mix(BG, GREEN if v else NRED, a), 'mm')
        if t > 18:
            ok = all(row[1:]) and None not in row[1:]
            c.text(1500, y, '收下' if ok else '从退币口吐出来', 'bold', 26, GREEN if ok else NRED, 'lm')
    c.text(960, 920, '真机器里还会测硬币经过线圈时的电磁「指纹」（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '第一关量大小：游戏币太小，直接退回'),
                (7.2, 14, '第二关称重：铁片、铝片和真币一样大，可重量差一截'),
                (14.2, 22, '第三关测材质：硬币滚过线圈或磁铁，不同金属的反应不一样：三关都过，才算真币（示意）')], y=1010)


# ---------------------------------------------------------------- E170 下水道
def e170_slope(c, t, i):
    corner_tag(c, '第 170 集 · 坡度要刚刚好')
    c.text(60, 96, '下水道的管子一路微微往下斜：太平了水流慢，沙子沉下来堵住管道；陡一点，水够快，就能把沉渣一起冲走', 'serif', 38, INK)
    for k, (lab, s) in enumerate((('坡度 1%', 0.01), ('坡度 3%', 0.03), ('坡度 10%', 0.10))):
        y = 330 + k * 200
        x0, x1 = 300, 1500
        drop = s * 1200 * 1.2
        c.line([(x0, y), (x1, y + drop)], METAL, 30)
        c.line([(x0, y + 8), (x1, y + drop + 8)], mix(BG, WATER, 0.7), 10)
        v = 0.25 + 4.5 * s ** 0.5
        rnd = random.Random(k)
        for j in range(14):
            base = rnd.random()
            if v < 0.8:
                u = min(0.5, base * 0.3 + t * v * 0.01)
            else:
                u = (base + t * v * 0.05) % 1
            c.ellipse(x0 + (x1 - x0) * u, y + drop * u + 10, 8, 6, fill=SAND)
        c.text(160, y, lab, 'bold', 26, INK, 'mm')
        res = '沙子沉在管里' if v < 0.8 else ('冲走了' if s < 0.08 else '冲走了，但水跑得太急')
        c.text(1560, y + drop / 2, res, 'bold', 24, GREEN if v >= 0.8 and s < 0.08 else (NRED if v < 0.8 else SPARK), 'lm')
    c.text(960, 940, '流速是示意；工程上要求流速大约在每秒 0.6 米以上（拍摄前核对）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同一根半截管，垫成不同的坡度，中间放一小勺沙'),
                (7.2, 14, '坡太缓，水慢吞吞，沙子沉在原地；坡度合适，水一冲沙就跟着走了'),
                (14.2, 22, '可也不是越陡越好：太陡水跑得太快，会冲坏管子，还会把粪渣留在后面（示意）')], y=1010)


def e170_network(c, t, i):
    corner_tag(c, '第 170 集 · 一张往低处汇的网')
    c.text(60, 96, '小管汇进支管，支管汇进主干管，一路顺坡往低处流；地势太平的地方，用泵站提高一截', 'serif', 36, INK)
    nodes = {'A': (300, 300), 'B': (520, 330), 'C': (300, 520), 'D': (560, 560), 'E': (850, 450), 'F': (850, 700),
             'G': (1150, 600), 'P': (1400, 600), 'W': (1700, 760)}
    edges = [('A', 'B'), ('B', 'E'), ('C', 'D'), ('D', 'E'), ('E', 'G'), ('F', 'G'), ('G', 'P'), ('P', 'W')]
    for (a, b) in edges:
        (x0, y0), (x1, y1) = nodes[a], nodes[b]
        c.line([(x0, y0), (x1, y1)], METAL, 12 if a in 'GP' else 8)
        for j in range(4):
            u = (t * 0.2 + j * 0.25) % 1
            c.ellipse(x0 + (x1 - x0) * u, y0 + (y1 - y0) * u, 6, 6, fill=WATER)
    for k in 'ABCDF':
        x, y = nodes[k]
        c.rect(x - 30, y - 60, x + 30, y - 10, fill=mix(BG, (200, 160, 120), 0.6), r=4)
    px, py = nodes['P']
    c.rect(px - 50, py - 50, px + 50, py + 50, fill=mix(BG, SPARK, 0.4), r=10)
    c.text(px, py - 80, '泵站：提高一截', 'sans', 20, SPARK, 'mm')
    wx, wy = nodes['W']
    c.rect(wx - 90, wy - 50, wx + 90, wy + 50, fill=mix(BG, GREEN, 0.4), r=10)
    c.text(wx, wy + 80, '污水处理厂', 'sans', 22, GREEN, 'mm')
    c.text(400, 220, '地势高', 'sans', 22, MUTED, 'mm')
    c.text(1700, 650, '地势低', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '每家的下水管接到街道下面的支管，支管再汇进更粗的主干管'),
                (7.2, 14, '整张网从高处往低处倾斜，绝大部分路段不用泵，水靠重力自己流'),
                (14.2, 22, '只有地势太平、管子埋得太深的地方，才用泵站把水提上来，再让它接着往低处流（示意）')], y=1010)


CLIPS = {
 'E168_光敏': (e168_ldr, 22), 'E168_回差': (e168_hyst, 22),
 'E168_片头': (titles.opening(SER31, VOL31, S31A, 6, '20 世纪中叶光控开关普及'), 7),
 'E168_片尾': (titles.closing(SER31, VOL31, S31A, 6, '下集：没人看着，售货机怎么分出真硬币和铁片？'), 7),
 'E169_直径': (e169_slots, 22), 'E169_三关': (e169_checks, 22),
 'E169_片头': (titles.opening(SER31, VOL31, S31A, 7, '1883 年英国投币明信片售卖机'), 7),
 'E169_片尾': (titles.closing(SER31, VOL31, S31A, 7, '下集：没有泵推，下水道的脏水为什么自己流走？'), 7),
 'E170_坡度': (e170_slope, 22), 'E170_管网': (e170_network, 22),
 'E170_片头': (titles.opening(SER31, VOL31, S31A, 8, '1860 年代伦敦现代下水道'), 7),
 'E170_片尾': (titles.closing(SER31, VOL31, S31A, 8, '下集：导航怎么一瞬间从几百万条路里找出最快的一条？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
