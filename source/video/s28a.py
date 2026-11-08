"""第二十八季（古法解密 11.0：桶、绳、戏、窗）第一批：B110 木桶、B111 缆桩、B112 拔河 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO

SB28 = [('B110', '木桶'), ('B111', '缆桩'), ('B112', '拔河'), ('B113', '高跷'), ('B114', '筛子'),
        ('B115', '陶车'), ('B116', '提线木偶'), ('B117', '骰子'), ('B118', '画押'), ('B119', '窗纸')]
VOL28 = '第二十八季 · 古法解密 11.0'
HOOP = (150, 150, 160)
ROPE = (210, 180, 120)
DARKWOOD = (130, 90, 55)
SKIN = (225, 180, 150)


# ---------------------------------------------------------------- B110 木桶
def b110_hoop(c, t, i):
    corner_tag(c, 'B110 · 箍一勒，木条互相挤紧')
    c.text(60, 96, '从上往下看：一圈木条围着，箍一勒紧，每根木条都被往里推，和左右两根挤在一起，缝就小了', 'serif', 38, INK)
    tight = min(1, max(0, (t - 4) / 6))
    cx, cy = 620, 580
    n = 18
    R = 300 - 18 * tight
    gap = 0.07 * (1 - tight) + 0.005
    for k in range(n):
        a0 = 2 * math.pi * k / n + gap / 2
        a1 = 2 * math.pi * (k + 1) / n - gap / 2
        pts = []
        for j in range(7):
            a = a0 + (a1 - a0) * j / 6
            pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
        for j in range(6, -1, -1):
            a = a0 + (a1 - a0) * j / 6
            pts.append((cx + (R - 40) * math.cos(a), cy + (R - 40) * math.sin(a)))
        c.poly(pts, mix(WOOD, DARKWOOD, (k % 3) * 0.2))
        if tight > 0.2:
            am = (a0 + a1) / 2
            c.arrow(cx + (R + 70) * math.cos(am), cy + (R + 70) * math.sin(am), cx + (R + 20) * math.cos(am), cy + (R + 20) * math.sin(am), mix(BG, SPARK, tight), 3, 10)
    c.ellipse(cx, cy, R + 8, R + 8, outline=mix(BG, HOOP, 0.4 + 0.6 * tight), width=int(4 + 8 * tight))
    c.rect(1180, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1520, 340, '箍的拉力 → 往里的推力', 'bold', 24, INK, 'mm')
    c.text(1520, 420, '箍越紧，木条之间', 'sans', 22, INK, 'mm')
    c.text(1520, 460, '压得越紧', 'sans', 22, INK, 'mm')
    c.text(1520, 560, f'缝宽：{"大" if tight < 0.3 else ("小" if tight < 0.9 else "几乎没有")}', 'bold', 28, GREEN if tight > 0.9 else SPARK, 'mm')
    caps(c, t, [(0, 7, '木桶没有一滴胶：几十根木条竖着围成一圈，外面套着两三道竹箍或铁箍'),
                (7.2, 14, '把箍往下敲紧，箍被撑大一点点，就像一根拉紧的皮筋，把每根木条都往桶心推'),
                (14.2, 22, '每根木条被推着挤向左右两根，接缝压得严严实实：圆形让这个力均匀地分到每一根上（示意）')], y=1010)


def b110_swell(c, t, i):
    corner_tag(c, 'B110 · 泡一泡，木头自己把缝挤死')
    c.text(60, 96, '干的木条之间总有细缝，一装水就渗；泡上一会儿，木头吸水胀大，可箍不让它往外跑，只能把缝挤得更死', 'serif', 36, INK)
    soak = min(1, t / 16)
    x0, y0 = 200, 300
    for k in range(9):
        w = 100 + 12 * soak
        x = x0 + k * 112
        col = mix(mix(WOOD, (220, 190, 140), 0.3), mix(WOOD, DARKWOOD, 0.5), soak)
        c.rect(x, y0, x + min(w, 112), y0 + 420, fill=col, r=4)
    c.rect(x0 - 10, y0 + 80, x0 + 9 * 112 + 10, y0 + 100, fill=HOOP)
    c.rect(x0 - 10, y0 + 320, x0 + 9 * 112 + 10, y0 + 340, fill=HOOP)
    rate = 40 * (1 - soak) ** 2 + 1
    rnd = random.Random(1)
    for k in range(8):
        x = x0 + (k + 1) * 112 - 2
        if soak < 0.85:
            for d in range(3):
                ph = (t * rate / 20 + d / 3 + rnd.random()) % 1
                c.ellipse(x, y0 + 420 + ph * 200, 6, 9, fill=WATER_L)
    c.rect(1300, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1580, 340, '泡水时间（示意）', 'bold', 24, INK, 'mm')
    c.text(1580, 410, f'{soak * 10:.0f} 分钟', 'mono', 30, SPARK, 'mm')
    c.text(1580, 480, '每分钟漏', 'sans', 22, INK, 'mm')
    c.text(1580, 540, f'约 {rate:.0f} 滴', 'mono', 30, NRED if rate > 10 else GREEN, 'mm')
    c.text(1580, 600, '（以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '新做的木桶、放干了的木桶，一倒水，缝里就往外渗'),
                (7.2, 14, '先装水泡上一阵：木头的纤维吸了水，一根根胀大'),
                (14.2, 22, '外面有箍箍着，木条没法往外胀，只能互相挤紧：漏水越来越少，最后一滴不漏（示意）')], y=1010)


# ---------------------------------------------------------------- B111 缆桩
def b111_wrap(c, t, i):
    corner_tag(c, 'B111 · 绳子绕着桩，一路被摩擦「吃掉」拉力')
    c.text(60, 96, '船这头拉得很紧；绳子绕着桩走一圈，每一小段都被桩摩擦掉一点，到人手里只剩一小部分', 'serif', 38, INK)
    cx, cy, R = 760, 560, 130
    c.ellipse(cx, cy, R, R, fill=DARKWOOD)
    c.ellipse(cx, cy, R - 20, R - 20, fill=mix(DARKWOOD, WOOD, 0.4))
    turns = 1.25
    mu = 0.3
    prog = min(1, t / 12)
    T0 = 1.0
    nseg = 120
    for j in range(nseg):
        th = 2 * math.pi * turns * j / nseg
        if j / nseg > prog:
            break
        Tn = T0 * math.exp(-mu * th)
        a = -math.pi / 2 - th
        rr = R + 14 + j * 0.15
        x1, y1 = cx + rr * math.cos(a), cy + rr * math.sin(a)
        a2 = -math.pi / 2 - 2 * math.pi * turns * (j + 1) / nseg
        rr2 = R + 14 + (j + 1) * 0.15
        x2, y2 = cx + rr2 * math.cos(a2), cy + rr2 * math.sin(a2)
        c.line([(x1, y1), (x2, y2)], mix(BG, ROPE, 0.3 + 0.7 * Tn), int(4 + 14 * Tn))
    c.line([(cx, cy - R - 14), (cx + 700, cy - R - 14)], ROPE, 18)
    c.text(cx + 720, cy - R - 14, '船：拉力 100%', 'bold', 24, NRED, 'lm')
    if prog >= 1:
        th = 2 * math.pi * turns
        a = -math.pi / 2 - th
        rr = R + 14 + nseg * 0.15
        ex, ey = cx + rr * math.cos(a), cy + rr * math.sin(a)
        Tend = math.exp(-mu * th)
        tx, ty = math.sin(a), -math.cos(a)
        c.line([(ex, ey), (ex + tx * 220, ey + ty * 220)], ROPE, int(4 + 14 * Tend))
        c.text(ex + tx * 220 - 20, ey + ty * 220 + 30, f'人手：约 {Tend * 100:.0f}%', 'bold', 24, GREEN, 'mm')
    c.text(cx + 500, cy + 200, '颜色越淡、绳越细：这一段绳上的拉力越小（摩擦系数取 0.3，示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '缆绳从船上拉过来，绕在码头的木桩上，人只在另一头轻轻拉着'),
                (7.2, 14, '绳子紧紧压在桩上，每走过一小段，桩上的摩擦就帮人「扛」走一点点拉力'),
                (14.2, 22, '一点点累积起来：绕一圈多，人手里只剩一成左右的拉力（具体比例看绳和桩，以实测为准）')], y=1010)


def b111_turns(c, t, i):
    corner_tag(c, 'B111 · 每多绕一圈，力气成倍变小')
    c.text(60, 96, '同一个重物：绕半圈、一圈、两圈、三圈，拉住它要的力不是一点点减少，而是一圈一圈地成倍减少', 'serif', 36, INK)
    mu = 0.3
    W = 10.0
    data = [('不绕', 0), ('半圈', 0.5), ('1 圈', 1), ('2 圈', 2), ('3 圈', 3)]
    gx0, gy0 = 260, 860
    c.line([(gx0, gy0), (1700, gy0)], LINE, 2)
    grow = min(1, t / 10)
    for k, (nm, n) in enumerate(data):
        F = W * math.exp(-mu * 2 * math.pi * n)
        x = gx0 + 80 + k * 280
        h = 540 * F / W * grow
        c.rect(x, gy0 - h, x + 160, gy0, fill=mix(ROPE, GREEN, k / 4), r=8)
        c.text(x + 80, gy0 + 40, nm, 'bold', 24, INK, 'mm')
        c.text(x + 80, gy0 - h - 30, f'{F:.2f} 牛' if F < 1 else f'{F:.1f} 牛', 'mono', 22, INK, 'mm')
    c.text(1300, 260, '挂 1 升水瓶 ≈ 10 牛（示意，摩擦系数取 0.3）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '一根绳绕在擀面杖上，一头挂一瓶水：不绕的时候，要用和水瓶一样大的力才拉得住'),
                (7.2, 14, '绕一圈，只要原来的大约七分之一；再多绕一圈，又变成那一点点的七分之一'),
                (14.2, 22, '这就是为什么码头工人只要在桩上绕几圈，就能拴住被风浪拉扯的大船（倍数以实测为准）')], y=1010)


# ---------------------------------------------------------------- B112 拔河
def b112_friction(c, t, i):
    corner_tag(c, 'B112 · 压得越重、越粗糙，越难拉动')
    c.text(60, 96, '摩擦力大约等于「压在地上的重量 × 一个由接触面决定的系数」：书越多越难拉，橡胶垫比塑料袋难拉得多', 'serif', 36, INK)
    cases = [('塑料袋 · 3 本书', 0.2, 3), ('毛巾 · 3 本书', 0.4, 3), ('橡胶垫 · 3 本书', 0.8, 3), ('橡胶垫 · 6 本书', 0.8, 6)]
    for k, (nm, mu, books) in enumerate(cases):
        y = 300 + k * 160
        c.line([(200, y + 60), (1300, y + 60)], LINE, 3)
        F = mu * books
        pull = 0.5 - 0.5 * math.cos(t * 0.6)
        moving = pull * 5 > F
        dx = ((t * 40) % 300) if moving else 0
        x = 300 + dx
        c.rect(x, y - 40, x + 160, y + 56, fill=(190, 160, 110), r=4)
        for b in range(books):
            c.rect(x + 20, y - 40 - (b + 1) * 12, x + 140, y - 40 - b * 12, fill=mix((120, 160, 220), (220, 120, 120), b / 6))
        c.text(1340, y, nm, 'bold', 22, INK, 'lm')
        bw = 300 * F / 4.8
        c.rect(1340, y + 24, 1340 + bw, y + 44, fill=SPARK, r=4)
        c.text(1350 + bw, y + 34, f'拉动要 ×{F / 0.6:.1f}', 'mono', 18, MUTED, 'lm')
    caps(c, t, [(0, 7, '同一个装书的纸箱，底下垫塑料袋，一拉就走；垫橡胶垫，要用好几倍的力'),
                (7.2, 14, '书从 3 本加到 6 本，箱子压得更重，拉动它的力也差不多翻一倍'),
                (14.2, 22, '拔河时，绳子上的力两边一样大：谁的脚和地面之间的摩擦先撑不住，谁就被拉过去（倍数为示意）')], y=1010)


def _person(c, x, y, lean, col, face=1):
    hx = x + face * lean * 120
    hy = y - 230 * math.cos(math.radians(lean * 40))
    c.line([(x, y), (hx, hy)], col, 14)
    c.ellipse(hx + face * 10, hy - 30, 26, 26, fill=SKIN)
    c.line([(x, y), (x - face * 30, y + 120)], col, 12)
    c.line([(x, y), (x + face * 40, y + 120)], col, 12)
    return hx, hy


def b112_lean(c, t, i):
    corner_tag(c, 'B112 · 身子后仰、脚往前蹬')
    c.text(60, 96, '后仰让身体的重量帮着往后拉，蹬地的脚把力斜着压进地面：同样的人，站法一变，脚下就抓得更牢', 'serif', 36, INK)
    ground = 820
    c.line([(80, ground + 4), (1840, ground + 4)], (110, 160, 90), 8)
    lean_r = min(1, t / 8)
    lx, ly = _person(c, 620, ground - 120, 0.1, (120, 160, 220), face=-1)
    rx, ry = _person(c, 1300, ground - 120, 0.1 + 0.8 * lean_r, (220, 140, 110), face=1)
    ry2 = ly
    c.line([(lx - 20, ly + 60), (rx + 20, ry + 60)], ROPE, 8)
    c.text(620, ground + 60, '站得直直的', 'bold', 24, INK, 'mm')
    c.text(1300, ground + 60, '后仰、压低', 'bold', 24, INK, 'mm')
    c.arrow(1300, ground, 1300 - 120 * lean_r, ground + 0, SPARK, 5, 16)
    c.text(1300 - 140 * lean_r, ground - 30, '脚往前蹬', 'sans', 20, SPARK, 'mm')
    c.rect(1460, 260, 1860, 520, fill=SHEET, r=14)
    c.text(1660, 300, '为什么后仰更稳', 'bold', 24, INK, 'mm')
    c.text(1660, 360, '身体重心在脚的后面', 'sans', 20, INK, 'mm')
    c.text(1660, 400, '自己的重量也在往后拉', 'sans', 20, INK, 'mm')
    c.text(1660, 460, '（示意，以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '站得直直的人，被绳子一拽，身体往前一倾，脚就被拖着走了'),
                (7.2, 14, '身子往后仰、腿往前蹬：重心落在脚的后面，自己的体重也变成往后拉的力'),
                (14.2, 22, '再配上鞋底和地面的好摩擦、大家一起喊号子同时使劲：一千多年前宫里拔河，比的也是这些（史料拍摄前核对）')], y=1010)


CLIPS = {
 'B110_箍紧': (b110_hoop, 22), 'B110_湿胀': (b110_swell, 22),
 'B110_片头': (titles.opening(BSER, VOL28, SB28, 0, '汉代以前已有箍木桶'), 7),
 'B110_片尾': (titles.closing(BSER, VOL28, SB28, 0, '下集：绕在木桩上的缆绳，为什么能拴住一条大船？'), 7),
 'B111_包角': (b111_wrap, 22), 'B111_圈数': (b111_turns, 22),
 'B111_片头': (titles.opening(BSER, VOL28, SB28, 1, '宋代码头系船的木桩'), 7),
 'B111_片尾': (titles.closing(BSER, VOL28, SB28, 1, '下集：拔河比的真的是力气吗？'), 7),
 'B112_摩擦': (b112_friction, 22), 'B112_后仰': (b112_lean, 22),
 'B112_片头': (titles.opening(BSER, VOL28, SB28, 2, '唐代宫廷拔河'), 7),
 'B112_片尾': (titles.closing(BSER, VOL28, SB28, 2, '下集：踩着一人多高的高跷，为什么人不容易倒？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
