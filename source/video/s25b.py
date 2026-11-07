"""第二十五季（第九层：看见身体）第二批：E135 X 光、E136 超声检查、E137 人工耳蜗 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s25a import S25A, SER25, VOL25, SKINC, SOUND

MUSCLE = (200, 110, 100)
BONE = (235, 230, 215)
XRAY = (180, 140, 240)
FILM = (30, 34, 44)
GEL = (140, 200, 230)
ORGAN = (170, 80, 90)
COCH = (230, 180, 150)


# ---------------------------------------------------------------- E135 X 光
def e135_pass(c, t, i):
    corner_tag(c, '第 135 集 · 骨头挡得多，皮肉挡得少（动画演示）')
    c.text(60, 96, 'X 射线穿过手臂：皮肉几乎拦不住它，骨头里的钙拦下了一大半，底片上就留下白白的骨影', 'serif', 40, INK)
    x0, x1 = 160, 1400
    c.rect(x0, 300, x0 + 60, 860, fill=(90, 90, 100), r=8)
    c.text(x0 + 30, 280, 'X 射线管', 'sans', 20, MUTED, 'mm')
    c.rect(1500, 300, 1560, 860, fill=FILM, outline=LINE, width=2)
    c.text(1530, 280, '底片', 'sans', 20, MUTED, 'mm')
    c.ellipse(840, 580, 260, 230, fill=SKINC)
    c.ellipse(840, 580, 220, 190, fill=MUSCLE)
    c.ellipse(840, 580, 70, 70, fill=BONE)
    c.text(840, 860, '手臂横截面：皮、肉、骨', 'sans', 22, INK, 'mm')
    for k in range(13):
        y = 340 + k * 40
        d = abs(y - 580)
        through_bone = d < 70
        s = (t * 0.6 + k * 0.07) % 1
        xe = x0 + 60 + (1500 - x0 - 60) * min(1, s * 1.4)
        col = mix(BG, XRAY, 0.8)
        c.line([(x0 + 60, y), (min(xe, 1500), y)], col, 2 if not through_bone else 2)
        if through_bone and xe > 910:
            c.line([(910, y), (min(xe, 1500), y)], mix(BG, XRAY, 0.25), 2)
        if s * 1.4 >= 1:
            c.rect(1504, y - 18, 1556, y + 18, fill=mix(FILM, (230, 230, 240), 0.85 if through_bone else 0.15))
    c.rect(1600, 380, 1880, 780, fill=SHEET, r=12)
    c.text(1740, 420, '底片上', 'bold', 24, INK, 'mm')
    c.text(1640, 490, '射线打到的地方：变黑', 'sans', 20, INK, 'lm')
    c.text(1640, 540, '被挡住的地方：留白', 'sans', 20, INK, 'lm')
    c.text(1640, 610, '骨头 → 白影', 'bold', 22, SPARK, 'lm')
    c.text(1640, 680, '（只做动画，不接触射线）', 'sans', 18, MUTED, 'lm')
    caps(c, t, [(0, 7, '一八九五年，伦琴发现一种看不见、却能穿过纸和木头的射线，叫它 X 射线（年代拍摄前核对）'),
                (7.2, 14, '它穿过手臂时，皮肉里多是水和碳，几乎拦不住；骨头里有很多钙，拦下了一大半'),
                (14.2, 22, '穿过去的射线让底片变黑，被骨头挡住的地方留白：一张 X 光片，其实是骨头的影子')], y=1010)


def e135_spectrum(c, t, i):
    corner_tag(c, '第 135 集 · 光的一大家子')
    c.text(60, 96, '无线电、微波、红外、可见光、紫外、X 射线：都是电磁波，波越短，能量越大', 'serif', 40, INK)
    bands = [('无线电', (110, 130, 160), 0.02), ('微波', (130, 140, 170), 0.04), ('红外', (200, 90, 70), 0.08),
             ('可见光', None, 0.15), ('紫外', (150, 110, 220), 0.3), ('X 射线', XRAY, 0.6), ('伽马射线', (220, 220, 240), 0.9)]
    x0, w = 120, 240
    y = 380
    for k, (nm, col, en) in enumerate(bands):
        x = x0 + k * w
        if col is None:
            for j in range(40):
                r, g, b = [int(v * 255) for v in __import__('colorsys').hsv_to_rgb(0.78 * (1 - j / 39), 0.75, 0.95)]
                c.rect(x + j * w / 40, y - 50, x + (j + 1) * w / 40 + 1, y + 50, fill=(r, g, b))
        else:
            c.rect(x, y - 50, x + w - 4, y + 50, fill=col)
        c.text(x + w / 2, y + 90, nm, 'bold', 24, INK, 'mm')
        wl = 1.0 / (k + 1) ** 1.2
        pts = [(x + 10 + j * (w - 24) / 100, 620 + 40 * math.sin(j / 100 * 2 * math.pi * (1 + k * 2.2) - t * 3)) for j in range(101)]
        c.line(pts, col if col else (230, 230, 120), 3)
        a = fade(t, 8 + k * 0.6, 9 + k * 0.6)
        h = 260 * en * a
        c.rect(x + 60, 940 - h, x + w - 60, 940, fill=mix(BG, NRED, 0.4 + 0.6 * en))
    c.text(x0, 560, '波长：越来越短 →', 'sans', 22, MUTED, 'lm')
    c.text(x0, 720, '每一份的能量：越来越大 →', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '收音机的无线电、微波炉的微波、遥控器的红外、我们看见的光，和 X 射线是一家人'),
                (7.2, 14, '它们都是电磁波，只是波长不同：X 射线的波，比可见光短上千倍'),
                (14.2, 22, '波越短，每一份能量越大，越能穿透东西，也越能伤到细胞：所以拍 X 光要控制剂量，只在需要时拍')], y=1010)


# ---------------------------------------------------------------- E136 超声检查
def e136_echo(c, t, i):
    corner_tag(c, '第 136 集 · 听回声画图')
    c.text(60, 96, '探头发出一声听不见的「嘀」，碰到每一层边界都弹回一点；回来得越晚，那层就越深', 'serif', 40, INK)
    px, top = 420, 220
    c.rect(px - 60, top, px + 60, top + 50, fill=(170, 175, 190), r=8)
    c.text(px, top - 20, '探头', 'sans', 22, MUTED, 'mm')
    layers = [(300, '皮肤', SKINC), (420, '脂肪', (230, 210, 140)), (560, '器官边界', ORGAN), (760, '另一边', MUSCLE)]
    c.rect(160, top + 50, 700, 900, fill=mix(BG, SKINC, 0.3))
    for (yy, nm, col) in layers:
        c.line([(160, yy), (700, yy)], col, 6)
        c.text(720, yy, nm, 'sans', 22, INK, 'lm')
    T = 5.5
    ph = (t % T) / T
    v = 1300
    yp = top + 50 + v * ph
    if yp < 900:
        c.line([(px - 40, yp), (px + 40, yp)], SOUND, 5)
    for (yy, nm, col) in layers:
        d = yy - (top + 50)
        tret = 2 * d / v
        if ph > d / v and ph < tret:
            ye = yy - (ph - d / v) * v
            c.line([(px - 25, ye), (px + 25, ye)], mix(BG, SPARK, 0.8), 3)
    gx0, gx1, gy = 1000, 1840, 600
    c.rect(960, 260, 1880, 860, fill=SHEET, r=14)
    c.text(1420, 300, '回声到达的时间（A 型显示）', 'bold', 24, INK, 'mm')
    c.line([(gx0, gy), (gx1, gy)], LINE, 2)
    c.text(gx1, gy + 40, '时间 → 深度', 'sans', 20, MUTED, 'rm')
    for (yy, nm, col) in layers:
        d = yy - (top + 50)
        tret = 2 * d / v
        if ph >= tret:
            x = gx0 + (gx1 - gx0) * tret / 1.0
            hgt = 200 * (0.5 if nm != '器官边界' else 1.0)
            c.line([(x, gy), (x, gy - hgt)], col, 6)
            c.text(x, gy - hgt - 24, nm, 'sans', 18, INK, 'mm')
    caps(c, t, [(0, 7, '探头里的压电片一颤，发出一声人听不见的高频「嘀」，钻进身体'),
                (7.2, 14, '每碰到一层边界，就弹回一点回声；越深的边界，回声来得越晚'),
                (14.2, 22, '把回来的时间换成深度，把探头一点点挪开再测：一行行拼起来，就成了一张 B 超图（示意）')], y=1010)


def e136_gel(c, t, i):
    corner_tag(c, '第 136 集 · 一层空气，挡回几乎全部声音')
    c.text(60, 96, '声音从空气进到皮肉，像撞上一堵墙，几乎全被弹回；抹上胶，挤掉空气，声音才进得去', 'serif', 40, INK)
    for k, gel in enumerate((False, True)):
        cy = 360 + k * 330
        c.rect(220, cy - 40, 360, cy + 40, fill=(170, 175, 190), r=8)
        c.text(290, cy - 70, '探头', 'sans', 20, MUTED, 'mm')
        gap_col = GEL if gel else mix(BG, (200, 200, 210), 0.15)
        c.rect(360, cy - 40, 420, cy + 40, fill=gap_col)
        c.text(390, cy + 70, '胶' if gel else '空气', 'bold', 22, INK, 'mm')
        c.rect(420, cy - 120, 1100, cy + 120, fill=mix(BG, SKINC, 0.5))
        c.text(760, cy - 140, '皮肉', 'sans', 20, MUTED, 'mm')
        s = (t * 0.8) % 1
        frac = 0.999 if not gel else 0.1
        if s < 0.3:
            x = 360 + 60 * s / 0.3
            c.line([(x, cy - 30), (x, cy + 30)], SOUND, 6)
        else:
            u = (s - 0.3) / 0.7
            c.line([(420 - 300 * u, cy - 30), (420 - 300 * u, cy + 30)], mix(BG, NRED, 0.3 + 0.7 * frac), 6)
            c.line([(420 + 600 * u, cy - 30), (420 + 600 * u, cy + 30)], mix(BG, SOUND, 1 - frac + 0.05), 6)
        c.rect(1240, cy - 70, 1840, cy + 70, fill=SHEET, r=12)
        c.text(1280, cy - 25, '弹回来：' + ('几乎全部' if not gel else '一小部分'), 'sans', 24, NRED if not gel else INK, 'lm')
        c.text(1280, cy + 25, '进到身体里：' + ('几乎没有' if not gel else '大部分'), 'sans', 24, MUTED if not gel else GREEN, 'lm')
    caps(c, t, [(0, 7, '声音在空气里和在皮肉里，走的「难易」差别非常大'),
                (7.2, 14, '探头和皮肤之间只要隔着薄薄一层空气，绝大部分超声都被弹回去，进不了身体'),
                (14.2, 22, '抹上一层胶，把空气挤得干干净净，超声就顺顺当当钻进去了：所以 B 超前要抹凉凉的胶（比例为示意）')], y=1010)


# ---------------------------------------------------------------- E137 人工耳蜗
def e137_place(c, t, i):
    corner_tag(c, '第 137 集 · 耳蜗按位置分高低音')
    c.text(60, 96, '把耳蜗拉直：入口附近的膜窄而硬，跟着高音振；越往里越宽越软，跟着低音振', 'serif', 40, INK)
    x0, x1, y = 200, 1700, 560
    c.poly([(x0, y - 30), (x1, y - 90), (x1, y + 90), (x0, y + 30)], mix(BG, COCH, 0.5))
    c.text(x0, y + 90, '入口（高音）', 'bold', 24, INK, 'mm')
    c.text(x1, y + 140, '最里面（低音）', 'bold', 24, INK, 'mm')
    f = 20000 * (20 / 20000) ** (0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi))
    pos = math.log(20000 / f) / math.log(1000)
    xp = x0 + (x1 - x0) * pos
    pts = []
    for j in range(301):
        x = x0 + (x1 - x0) * j / 300
        u = j / 300
        env = math.exp(-((u - pos) / 0.06) ** 2) if u <= pos else math.exp(-((u - pos) / 0.02) ** 2)
        pts.append((x, y + 60 * env * math.sin(u * 160 - t * 12)))
    c.line(pts, SPARK, 4)
    c.ellipse(xp, y - 130, 14, 14, fill=SPARK)
    c.line([(xp, y - 116), (xp, y - 60)], SPARK, 2)
    c.rect(700, 240, 1220, 340, fill=SHEET, r=12)
    c.text(960, 290, f'现在听到的音：约 {f:.0f} 赫兹', 'mono', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '耳朵深处的耳蜗像一个蜗牛壳，里面有一条长长的膜，膜上排着几千个毛细胞'),
                (7.2, 14, '尖尖的高音，让入口附近的膜振得最厉害；低沉的声音，振动一直传到最里面才最大'),
                (14.2, 22, '哪里的毛细胞被振得最厉害，大脑就知道是多高的音：耳蜗是按位置分高低的（示意）')], y=1010)


def e137_implant(c, t, i):
    corner_tag(c, '第 137 集 · 把声音拆成几十份，分给几十个电极')
    c.text(60, 96, '话筒收声，处理器把它拆成高低不同的几份，分别送到耳蜗里不同位置的电极', 'serif', 40, INK)
    c.ellipse(200, 520, 40, 40, fill=(170, 175, 190))
    c.text(200, 600, '话筒', 'sans', 22, INK, 'mm')
    pts = [(260 + j * 3, 520 + 40 * math.sin(j * 0.3 + t * 8) * math.sin(j * 0.07)) for j in range(100)]
    c.line(pts, SOUND, 3)
    c.rect(600, 360, 900, 680, fill=SHEET, r=14)
    c.text(750, 340, '处理器', 'bold', 24, INK, 'mm')
    nb = 12
    rnd = random.Random(int(t * 4))
    levels = []
    for k in range(nb):
        lv = max(0.05, 0.5 + 0.45 * math.sin(t * 2.2 + k * 0.9) * math.cos(t * 0.7 + k * 0.4))
        levels.append(lv)
        x = 620 + k * 22
        c.rect(x, 660 - 260 * lv, x + 16, 660, fill=mix(SOUND, SPARK, k / (nb - 1)))
    c.text(750, 700, '高 ← 音 → 低', 'sans', 18, MUTED, 'mm')
    cx, cy = 1400, 540
    for j in range(400):
        a = j / 400 * 2.6 * 2 * math.pi
        r = 260 * (1 - j / 470)
        if j % 3 == 0:
            c.ellipse(cx + r * math.cos(a), cy + r * math.sin(a), 6, 6, fill=mix(BG, COCH, 0.7))
    for k in range(nb):
        j = int(20 + k * 300 / nb)
        a = j / 400 * 2.6 * 2 * math.pi
        r = 260 * (1 - j / 470)
        ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
        c.ellipse(ex, ey, 6 + 12 * levels[k], 6 + 12 * levels[k], fill=mix(BG, mix(SOUND, SPARK, k / (nb - 1)), levels[k]))
    c.line([(900, 520), (cx + 260, cy)], mix(BG, LINE, 0.6), 2)
    c.text(cx, 880, '耳蜗里的电极（入口高音，里面低音）', 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '耳蜗里的毛细胞坏了，声音就传不到神经：人工耳蜗绕过了它们'),
                (7.2, 14, '耳后的处理器把话筒收到的声音，拆成高低不同的十几到二十几份'),
                (14.2, 22, '每一份变成小小的电脉冲，送到耳蜗里对应位置的电极，直接刺激听神经（电极数量拍摄前核对）')], y=1010)


CLIPS = {
 'E135_穿透': (e135_pass, 22), 'E135_电磁波': (e135_spectrum, 22),
 'E135_片头': (titles.opening(SER25, VOL25, S25A, 3, '1895 年伦琴发现 X 射线'), 7),
 'E135_片尾': (titles.closing(SER25, VOL25, S25A, 3, '下集：B 超为什么要在肚子上抹一层凉凉的胶？'), 7),
 'E136_回声': (e136_echo, 22), 'E136_耦合胶': (e136_gel, 22),
 'E136_片头': (titles.opening(SER25, VOL25, S25A, 4, '1950 年代医用超声成像'), 7),
 'E136_片尾': (titles.closing(SER25, VOL25, S25A, 4, '下集：听不见的人，怎么靠小机器重新「听」到声音？'), 7),
 'E137_位置': (e137_place, 22), 'E137_电极': (e137_implant, 22),
 'E137_片头': (titles.opening(SER25, VOL25, S25A, 5, '1970 年代多通道人工耳蜗'), 7),
 'E137_片尾': (titles.closing(SER25, VOL25, S25A, 5, '下集：心跳乱了，小盒子怎么帮它按时跳？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
