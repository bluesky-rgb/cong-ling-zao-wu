"""第五十四季（古法解密 24.0：衣与针线）第三批：B246 千层底、B247 回针、B248 樟木箱 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s54a import SB54, VOL54, CLOTH, THREAD, WOODC, SKIN

PASTE = (240, 235, 210)
STONE = (140, 140, 150)
FELT = (120, 150, 190)
CAMPHOR = (190, 140, 90)
SCENT = (150, 210, 160)


# ---------------------------------------------------------------- B246 千层底
def b246_layers(c, t, i):
    corner_tag(c, 'B246 · 一层层粘成一块')
    c.text(60, 96, '旧布刷上浆糊一层层贴起来（叫袼褙），晾干后粘成一整块，层数越多越厚越硬；再用线密密纳紧，各层就不会分开', 'serif', 36, INK)
    n = min(8, int(t / 1.6) + 1)
    x0, x1, yb = 460, 1460, 760
    for k in range(n):
        y = yb - k * 34
        c.rect(x0, y - 22, x1, y, fill=mix(BG, CLOTH, 1.0 - 0.05 * (k % 2)), r=4)
        if k < n - 1:
            c.rect(x0, y - 34, x1, y - 22, fill=mix(BG, PASTE, 0.7))
    if t > 14.2:
        for k in range(9):
            x = x0 + 60 + k * 110
            c.line([(x, yb + 6), (x, yb - n * 34 - 6)], mix(BG, THREAD, 1.0), 5)
        c.text(960, 320, '线一针针纳紧：各层钉成一体', 'bold', 28, GREEN, 'mm')
    c.text(1520, yb - n * 17, f'{n} 层', 'bold', 30, INK, 'lm')
    caps(c, t, [(0, 7, '面粉加冷水调成浆糊，刷一层，贴一层布'),
                (7.2, 14, '一层层叠到 8 层，压在书下晾一晚，粘成一块硬片'),
                (14.2, 22, '真的千层底还要用麻线一针针纳紧，各层就不会分开（示意）')], y=1010)


def b246_stone(c, t, i):
    corner_tag(c, 'B246 · 垫得越厚，石子越不硌')
    c.text(60, 96, '脚踩在一颗小石子上：隔着单层布，石子一个尖顶住脚心；隔着 8 层的硬片，压力被摊到一大片上，几乎不硌', 'serif', 36, INK)
    for j, (lab, n) in enumerate([('单层布', 1), ('2 层', 2), ('8 层', 8)]):
        cx, gy = 400 + j * 560, 760
        c.ellipse(cx, gy - 18, 26, 18, fill=mix(BG, STONE, 1.0))
        thick = n * 10
        bend = 26 * (1 if n == 1 else (0.6 if n == 2 else 0.1))
        pts = [(cx - 200 + u * 20, gy - 36 - thick / 2 - (bend * math.exp(-((u - 10) / 3) ** 2))) for u in range(21)]
        for L in range(n):
            c.line([(x, y - L * 9) for x, y in pts], mix(BG, CLOTH, 1.0), 8)
        top = gy - 36 - thick - 20
        c.poly([(cx - 180, top), (cx + 180, top), (cx + 160, top - 120), (cx - 160, top - 120)], mix(BG, SKIN, 1.0))
        if n == 1:
            c.ellipse(cx, top + 4, 18, 18, fill=mix(BG, NRED, 0.7))
        c.text(cx, 860, lab + ('：硌脚' if n == 1 else ('：好一点' if n == 2 else '：几乎不硌')), 'bold', 28, NRED if n == 1 else (INK if n == 2 else GREEN), 'mm')
    caps(c, t, [(0, 7, '单层布：石子的尖顶起一个小包，正好顶在脚心'),
                (7.2, 14, '2 层：好一点，还是能感到'),
                (14.2, 22, '8 层硬片：石子顶不弯它，压力被摊开（穿袜子轻轻踩，以实测为准）')], y=1010)


# ---------------------------------------------------------------- B247 回针
def b247_stitch(c, t, i):
    corner_tag(c, 'B247 · 平针和回针')
    c.text(60, 96, '平针一上一下往前走，线是一段一段的；回针往前一针、退回半针，背面的线一段搭一段连成一条', 'serif', 36, INK)
    for j, (lab, back) in enumerate([('平针', False), ('回针', True)]):
        y = 420 + j * 300
        c.rect(260, y - 50, 1660, y + 50, fill=mix(BG, FELT, 0.5), r=8)
        n = min(12, int(t * 0.9) + 1)
        for k in range(n):
            x = 300 + k * 110
            if back:
                c.line([(x, y - 10), (x + 110, y - 10)], mix(BG, THREAD, 1.0), 8)
                c.line([(x + 55, y + 14), (x + 165, y + 14)], mix(BG, THREAD, 0.55), 6)
            else:
                if k % 2 == 0:
                    c.line([(x, y - 10), (x + 110, y - 10)], mix(BG, THREAD, 1.0), 8)
                else:
                    c.line([(x, y + 14), (x + 110, y + 14)], mix(BG, THREAD, 0.55), 6)
        c.text(200, y, lab, 'bold', 30, INK, 'rm')
    c.text(960, 880, '深色：正面的线　浅色：背面的线', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '平针：一上一下往前，每一针单独穿过布'),
                (7.2, 14, '回针：往前一针，退回半针，再往前一针'),
                (14.2, 22, '回针背面的线一段搭着一段，连成一条（俯视示意）')], y=1010)


def b247_pull(c, t, i):
    corner_tag(c, 'B247 · 一拉，谁先松开')
    c.text(60, 96, '往两边拉：平针的线在针眼里顺着滑，缝口一扯就张开；回针针针相搭，力分到很多针上，拉开难得多', 'serif', 36, INK)
    pull = min(1.0, t / 14)
    for j, (lab, back, maxf) in enumerate([('平针', False, 1.5), ('回针', True, 4.0)]):
        cx = 560 + j * 800
        gap = (120 * max(0.0, pull - 0.5) * 2) if not back else 12 * pull
        c.rect(cx - 250, 300, cx + 250, 560 - gap / 2, fill=mix(BG, FELT, 0.8), r=8)
        c.rect(cx - 250, 560 + gap / 2, cx + 250, 820, fill=mix(BG, FELT, 0.6), r=8)
        for k in range(8):
            x = cx - 210 + k * 60
            c.line([(x, 540 - gap / 2), (x + (0 if back else 10), 580 + gap / 2)], mix(BG, THREAD, 1.0), 4)
        f = maxf * min(1.0, pull * (2 if not back else 1)) if not back or pull < 1 else maxf
        if not back and pull > 0.5:
            f = maxf
        c.text(cx, 240, f'行李秤：{f:.1f} 千克（示意）', 'bold', 28, INK, 'mm')
        c.text(cx, 880, lab + ('：先被拉开' if not back else '：撑得更久'), 'bold', 28, NRED if not back else GREEN, 'mm')
    caps(c, t, [(0, 7, '两组缝口一样长、针脚一样大，下面压住，上面挂行李秤慢慢拉'),
                (7.2, 14, '平针的线在针眼里滑，缝口很快张开'),
                (14.2, 22, '回针的线互相卡住，力分散到很多针上，读数大得多（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B248 樟木箱
def b248_evap(c, t, i):
    corner_tag(c, 'B248 · 气味从木头里慢慢跑出来')
    c.text(60, 96, '樟木里含有樟脑等油性的气味物质，它们一点点从木头表面挥发出来：盖严的箱子里，气味越攒越浓，虫子就不来', 'serif', 36, INK)
    for j, (lab, closed) in enumerate([('盖严', True), ('敞开', False)]):
        cx, cy = 560 + j * 800, 600
        c.rect(cx - 260, cy - 200, cx + 260, cy + 200, outline=mix(BG, CAMPHOR, 1.0), width=24, r=10)
        if closed:
            c.rect(cx - 280, cy - 230, cx + 280, cy - 190, fill=mix(BG, CAMPHOR, 1.0), r=8)
        else:
            c.rect(cx - 280, cy - 340, cx - 120, cy - 300, fill=mix(BG, CAMPHOR, 1.0), r=8)
        random.seed(3 + j)
        n = int(min(1.0, t / 14) * (60 if closed else 14))
        for k in range(n):
            x = cx + random.uniform(-230, 230)
            y = cy + random.uniform(-170, 170)
            c.ellipse(x, y, 8, 8, fill=mix(BG, SCENT, 0.9))
        if not closed:
            for k in range(8):
                ph = (t * 0.25 + k / 8) % 1
                c.ellipse(cx + random.uniform(-150, 150), cy - 200 - ph * 160, 8, 8, fill=mix(BG, SCENT, 1 - ph))
        c.text(cx, cy + 270, lab + ('：气味攒起来' if closed else '：气味跑掉了'), 'bold', 28, GREEN if closed else NRED, 'mm')
    caps(c, t, [(0, 7, '樟木箱的木板里有油性的气味物质，绿点是挥发出来的气味分子'),
                (7.2, 14, '盖严了，气味跑不掉，越攒越浓'),
                (14.2, 22, '敞着口，气味一出来就跑了；很多蛀虫不喜欢这股味道，就不来产卵（示意）')], y=1010)


def b248_surface(c, t, i):
    corner_tag(c, 'B248 · 磨出新面，气味又浓了')
    c.text(60, 96, '用了几十年的樟木箱，表面的油挥发得差不多了，气味变淡；刨一刨、磨一磨，露出新木头，气味又浓起来', 'serif', 36, INK)
    fresh = t > 7.2
    cx, cy = 960, 560
    c.rect(cx - 400, cy - 140, cx + 400, cy + 140, fill=mix(BG, CAMPHOR, 0.7), r=10)
    for k in range(7):
        y = cy - 120 + k * 40
        c.line([(cx - 390, y), (cx + 390, y + 10 * math.sin(k))], mix(BG, (150, 100, 60), 1.0), 3)
    c.rect(cx - 400, cy - 140, cx + 400, cy - 110, fill=mix(BG, (120, 100, 80), 1.0 if not fresh else 0.0))
    if fresh:
        c.rect(cx - 140, cy - 150, cx + 140, cy - 110, fill=mix(BG, (225, 190, 140), 1.0), r=4)
        c.text(cx, cy + 190, '大人用细砂纸磨出的新面', 'bold', 24, INK, 'mm')
    random.seed(8)
    n = 4 if not fresh else 30
    for k in range(n):
        ph = (t * 0.3 + k / max(1, n)) % 1
        x = cx + random.uniform(-120 if fresh else -380, 120 if fresh else 380)
        c.ellipse(x, cy - 160 - ph * 200, 8, 8, fill=mix(BG, SCENT, 1 - ph * 0.7))
    c.text(cx, 840, '旧表面：气味淡' if not fresh else '新表面：气味浓', 'bold', 30, GREEN if fresh else NRED, 'mm')
    caps(c, t, [(0, 7, '先闻一闻樟木块的旧表面：气味淡淡的'),
                (7.2, 14, '请大人用细砂纸磨出一小块新表面'),
                (14.2, 22, '再闻：气味浓多了。只用樟木块，不用樟脑丸')], y=1010)


CLIPS = {
 'B246_层压': (b246_layers, 22), 'B246_石子': (b246_stone, 22),
 'B246_片头': (titles.opening(BSER, VOL54, SB54, 6, '北方布鞋的「千层底」'), 7),
 'B246_片尾': (titles.closing(BSER, VOL54, SB54, 6, '下集：回针为什么更结实？'), 7),
 'B247_针法': (b247_stitch, 22), 'B247_拉开': (b247_pull, 22),
 'B247_片头': (titles.opening(BSER, VOL54, SB54, 7, '古代缝补讲究「回针」'), 7),
 'B247_片尾': (titles.closing(BSER, VOL54, SB54, 7, '下集：木头箱子怎么防虫？'), 7),
 'B248_挥发': (b248_evap, 22), 'B248_新面': (b248_surface, 22),
 'B248_片头': (titles.opening(BSER, VOL54, SB54, 8, '江南人家常用樟木箱存衣'), 7),
 'B248_片尾': (titles.closing(BSER, VOL54, SB54, 8, '下集：一根小棍怎么固定发髻？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
