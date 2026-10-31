"""第八季第二批：E55 照相、E56 电磁铁、E57 电报 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s8a import S8A, SER8, VOL8, lens_shape, GLASS, RAY

PRUSSIAN = (40, 80, 160)
WIRE = COPPER

# ---------------------------------------------------------------- E55 照相
def e55_pinhole(c, t, i):
    corner_tag(c, '第 55 集 · 小孔成像')
    c.text(60, 96, '墙上的一个小孔，为什么能投出倒过来的风景？', 'serif', 40, INK)
    # tree object at left, wall with hole, screen at right
    tx, ty = 330, 620
    c.rect(tx - 14, ty - 120, tx + 14, ty + 120, fill=(130, 95, 60))
    c.ellipse(tx, ty - 190, 110, 100, fill=GREEN)
    wx = 960
    big = fade(t, 10, 13)
    hole = 6 + 34 * big
    c.rect(wx - 12, 200, wx + 12, 540 - hole, fill=MUTED)
    c.rect(wx - 12, 540 + hole, wx + 12, 900, fill=MUTED)
    sx = 1500
    c.line([(sx, 200), (sx, 900)], (200, 200, 205), 4)
    a = fade(t, 1, 5)
    for (px, py, col) in [(tx, ty - 270, GREEN), (tx, ty + 120, (130, 95, 60))]:
        if a <= 0: break
        for off in ((-hole, hole) if big > 0 else (0,)):
            hy = 540 + off * 0.8
            k = (sx - wx) / (wx - px)
            iy = hy + (hy - py) * k
            c.line([(px, py), (wx, hy)], mix(BG, RAY, a * 0.8), 2)
            c.line([(wx, hy), (wx + (sx - wx) * a, hy + (iy - hy) * a)], mix(BG, RAY, a * 0.8), 2)
    # image on screen: inverted, scaled
    b = fade(t, 5, 7)
    if b > 0:
        k = (sx - wx) / (wx - tx)
        blur = 1 + 3 * big
        top = 540 + (540 - (ty + 120)) * k
        bot = 540 + (540 - (ty - 270)) * k
        crown = 540 + (540 - (ty - 190)) * k
        c.rect(sx + 6, top - 8 * blur, sx + 22, bot - 60 + 8 * blur, fill=mix(BG, (130, 95, 60), b / blur))
        c.ellipse(sx + 14, crown, 26 * k * 0.4 + 10 * blur, 60 * k * 0.4 + 10 * blur, fill=mix(BG, GREEN, b / blur))
    c.text(tx, 940, '窗外的树', 'sans', 24, MUTED, 'mm')
    c.text(wx, 940, '小孔', 'sans', 24, MUTED, 'mm')
    c.text(sx, 940, '对面的墙', 'sans', 24, MUTED, 'mm')
    d = fade(t, 15, 16)
    c.rect(1560, 260, 1880, 560, fill=mix(BG, SHEET, d), r=12)
    c.text(1580, 300, '孔小：清楚，但暗', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1580, 350, '孔大：亮，但糊', 'sans', 24, mix(BG, INK, d), 'lm')
    c.text(1580, 420, '换成透镜：', 'bold', 26, mix(BG, SPARK, d), 'lm')
    c.text(1580, 465, '又亮又清楚', 'bold', 26, mix(BG, SPARK, d), 'lm')
    c.text(1580, 520, '（第 52 集）', 'sans', 22, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 5, '树顶的光穿过小孔往下走，树根的光穿过小孔往上走'),
                (5.2, 10, '在对面的墙上，就拼出一棵倒过来的树。《墨经》里早就写过这件事'),
                (10.2, 15, '孔开大一点，画面亮了，却糊了：每一点的光落成了一片'),
                (15.2, 22, '换成一片透镜，就能又亮又清楚。这就是相机的前半截：先成像')], y=1010)

def e55_cyanotype(c, t, i):
    corner_tag(c, '第 55 集 · 蓝晒')
    c.text(60, 96, '一张纸，怎么把光「记」下来？', 'serif', 40, INK)
    px0, py0, px1, py1 = 260, 220, 1020, 860
    expo = fade(t, 3, 11)
    wash = fade(t, 12, 14)
    paper = mix((210, 205, 150), PRUSSIAN, expo * 0.7)
    if wash > 0: paper = mix(paper, PRUSSIAN, wash)
    c.rect(px0, py0, px1, py1, fill=paper, r=6)
    # leaf mask
    leaf = []
    for k in range(60):
        a_ = k / 59 * 2 * math.pi
        r = 220 * (0.55 + 0.45 * math.sin(a_ / 2) ** 1.0)
        leaf.append((640 + r * 0.55 * math.sin(a_), 540 - r * math.cos(a_)))
    leafcol = (70, 140, 70) if wash < 0.5 else (235, 235, 230)
    c.poly(leaf, mix(leafcol, (235, 235, 230), wash) if wash > 0 else leafcol)
    c.line([(640, 760), (640, 360)], mix(BG, (90, 120, 80), 1 - wash), 3)
    # sun rays
    if 2 < t < 11.5:
        for k in range(9):
            x = px0 + 40 + k * 90
            y = 150 + ((t * 200 + k * 40) % 60)
            c.arrow(x, y - 40, x, y + 20, SPARK, 3, 10)
    a = fade(t, 1, 2)
    c.rect(1120, 220, 1860, 860, fill=mix(BG, SHEET, a), r=14)
    lines = [('① 纸上涂了两种铁盐', INK, 1), ('② 晒到太阳：被照到的地方', INK, 4), ('   铁离子被光「还原」', MUTED, 4),
             ('③ 叶子挡住的地方没变', INK, 8), ('④ 用水一洗：照过的变成普鲁士蓝', FIELD, 12),
             ('   没照到的被洗掉，留下白影', MUTED, 12), ('光的多少，变成了颜色的深浅', SPARK, 15)]
    for k, (s_, col, st) in enumerate(lines):
        b = fade(t, st, st + 1)
        c.text(1150, 280 + k * 80, s_, 'bold' if k in (6,) else 'sans', 28 if k == 6 else 26, mix(BG, col, b), 'lm')
    caps(c, t, [(0, 3, '蓝晒纸上涂着两种铁盐，叶子压在上面'),
                (3.2, 11, '晒太阳：光照到的地方，铁盐起了变化；叶子挡住的地方，没变'),
                (11.2, 16, '放进水里一洗：照过的地方变成深蓝，叶子的影子留成白色'),
                (16.2, 22, '1842 年赫歇尔发明了这种方法：照相的后半截，就是让光改变一种化学物质')], y=1010)

# ---------------------------------------------------------------- E56 电磁铁
def nail_coil(c, cx, cy, turns, on, a=1.0, L=520):
    c.rect(cx - L / 2, cy - 18, cx + L / 2, cy + 18, fill=mix(BG, (150, 155, 160), a), r=6)
    c.poly([(cx + L / 2, cy - 18), (cx + L / 2 + 50, cy), (cx + L / 2, cy + 18)], mix(BG, (150, 155, 160), a))
    c.rect(cx - L / 2 - 26, cy - 34, cx - L / 2, cy + 34, fill=mix(BG, (150, 155, 160), a), r=4)
    n = turns
    span = L * 0.8
    for k in range(n):
        x = cx - span / 2 + span * (k + 0.5) / n
        c.line([(x - 6, cy - 30), (x + 6, cy + 30)], mix(BG, WIRE, a), max(2, int(160 / max(n, 8))))
    if on:
        for k in range(3):
            rx_, ry_ = L * (0.62 + 0.12 * k), 46 + 20 * k
            c.ellipse(cx, cy, rx_, ry_, outline=mix(BG, FIELD, a * (0.7 - k * 0.2)), width=2)

def clips_pile(c, x, y, n, a=1.0):
    for k in range(n):
        cx = x + (k % 6) * 34
        cy = y + (k // 6) * 24
        c.rect(cx, cy, cx + 26, cy + 12, outline=mix(BG, (200, 200, 205), a), width=3, r=6)

def e56_turns(c, t, i):
    corner_tag(c, '第 56 集 · 匝数')
    c.text(60, 96, '线圈绕得越多，磁力越大吗？', 'serif', 40, INK)
    data = [(20, 3), (50, 8), (100, 15)]
    for k, (n, clipsn) in enumerate(data):
        a = fade(t, 1 + k * 4.5, 2 + k * 4.5)
        if a <= 0: continue
        y = 260 + k * 230
        on = t > 2.5 + k * 4.5
        nail_coil(c, 600, y, min(n, 40), on, a, 520)
        c.text(160, y - 60, f'{n} 匝', 'bold', 32, mix(BG, INK, a), 'lm')
        if on:
            clips_pile(c, 900, y + 40, clipsn, a)
            c.text(1180, y + 40, f'吸起约 {clipsn} 个（示意）', 'sans', 26, mix(BG, SPARK, a), 'lm')
    b = fade(t, 15, 16)
    c.rect(300, 880, 1620, 960, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 920, '磁力随「匝数 × 电流」增大；断电，回形针就掉下来（数字以实测为准）', 'bold', 26, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 5, '铁钉上绕二十圈漆包线，接上电池：铁钉变成了磁铁'),
                (5.2, 14, '绕五十圈、一百圈：吸起的回形针越来越多'),
                (14.2, 22, '一断电，回形针全掉下来。这块磁铁，想开就开、想关就关')], y=1010)

def e56_domains(c, t, i):
    corner_tag(c, '第 56 集 · 磁畴')
    c.text(60, 96, '铁钉里面，发生了什么？', 'serif', 40, INK)
    on = fade(t, 6, 10) * (1 - fade(t, 15, 18))
    rnd = random.Random(56)
    x0, y0 = 360, 280
    for r in range(6):
        for k in range(12):
            ang0 = rnd.uniform(-math.pi, math.pi)
            ang = ang0 * (1 - on)
            cx = x0 + k * 100
            cy = y0 + r * 90
            c.rect(cx - 46, cy - 40, cx + 46, cy + 40, outline=LINE, width=2, r=6)
            dx, dy = 32 * math.cos(ang), 32 * math.sin(ang)
            c.arrow(cx - dx, cy - dy, cx + dx, cy + dy, mix(NRED, FIELD, 0.3), 4, 12)
    if on > 0.05:
        c.text(960, 860, '通电：线圈的磁场把一个个小磁区「扳」成同一个方向', 'bold', 28, mix(BG, SPARK, on), 'mm')
    else:
        c.text(960, 860, '平时：铁里有无数小磁区（磁畴），方向乱七八糟，互相抵消', 'sans', 28, INK, 'mm')
    caps(c, t, [(0, 6, '铁里本来就藏着无数个小磁区，可它们方向杂乱，合起来不显磁性'),
                (6.2, 15, '线圈一通电，它的磁场把小磁区一个个扳正：铁钉把磁力放大了几百上千倍'),
                (15.2, 22, '一断电，软铁里的小磁区又乱了：所以电磁铁能开能关')], y=1010)

# ---------------------------------------------------------------- E57 电报
def e57_line(c, t, i):
    corner_tag(c, '第 57 集 · 一根线')
    c.text(60, 96, '按一下键，几十公里外怎么会「咔」一声？', 'serif', 40, INK)
    press = (math.sin(t * 2.2) > 0.2) if t > 4 else False
    # sender
    kx, ky = 320, 560
    c.rect(kx - 120, ky + 40, kx + 120, ky + 70, fill=(120, 90, 60), r=6)
    lever = -14 if not press else 0
    c.line([(kx - 100, ky + lever), (kx + 100, ky)], (190, 190, 195), 12)
    c.ellipse(kx + 100, ky - 8, 18, 18, fill=MUTED)
    c.text(kx, ky + 120, '电键（发报）', 'bold', 26, INK, 'mm')
    # battery
    c.rect(kx - 80, ky - 260, kx + 80, ky - 190, outline=SPARK, width=4, r=8)
    c.text(kx, ky - 225, '电池', 'sans', 24, SPARK, 'mm')
    # receiver sounder
    rx, ry = 1600, 560
    nail_coil(c, rx, ry + 30, 18, press, 1.0, 180)
    arm = -30 if not press else -12
    c.line([(rx - 140, ry + arm), (rx + 140, ry + arm)], (190, 190, 195), 10)
    c.text(rx, ry + 120, '电磁铁响器（收报）', 'bold', 26, INK, 'mm')
    if press:
        c.text(rx + 170, ry - 60, '咔！', 'bold', 40, SPARK, 'mm')
    # long wire
    col = mix(WIRE, SPARK, 0.6) if press else WIRE
    c.line([(kx + 80, ky - 225), (rx, ky - 225), (rx, ry - 10)], col, 5)
    c.line([(kx - 80, ky - 225), (kx - 160, ky - 225), (kx - 160, ky + 55), (kx - 120, ky + 55)], col, 5)
    c.text(960, ky - 260, '几十公里的导线', 'sans', 26, MUTED, 'mm')
    c.line([(rx + 90, ry + 30), (rx + 90, 820), (kx + 100, 820), (kx + 100, ky + 40)], mix(BG, col, 0.6), 3)
    c.text(960, 850, '回路（早期电报用大地当回路，只需一根线）', 'sans', 22, MUTED, 'mm')
    if press:
        for k in range(8):
            d = ((t * 900 + k * 150) % 1300)
            c.ellipse(kx + 80 + d, ky - 225, 7, 7, fill=SPARK)
    caps(c, t, [(0, 4, '这一头：电池、电键；那一头：一个电磁铁和一片铁皮'),
                (4.2, 12, '按下电键，电路接通，远处的电磁铁立刻吸住铁皮：「咔」'),
                (12.2, 22, '松开就弹回去。电流几乎瞬间跑完全程：消息的速度，第一次超过了马和烽火')], y=1010)

MORSE = {'E': '.', 'T': '-', 'A': '.-', 'S': '...', 'O': '---', 'H': '....', 'Q': '--.-', 'Z': '--..'}
def e57_morse(c, t, i):
    corner_tag(c, '第 57 集 · 摩尔斯电码')
    c.text(60, 96, '只有「长」和「短」，怎么拼出整句话？', 'serif', 40, INK)
    rows = [('E', '最常用'), ('T', '常用'), ('A', '常用'), ('S', ''), ('O', ''), ('Q', '不常用'), ('Z', '不常用')]
    for k, (ch, note) in enumerate(rows):
        a = fade(t, 1 + k * 1.2, 2 + k * 1.2)
        if a <= 0: continue
        y = 220 + k * 90
        c.text(300, y, ch, 'mono', 44, mix(BG, INK, a), 'mm')
        x = 400
        for sym in MORSE[ch]:
            if sym == '.':
                c.ellipse(x + 14, y, 14, 14, fill=mix(BG, SPARK, a)); x += 50
            else:
                c.rect(x, y - 14, x + 80, y + 14, fill=mix(BG, SPARK, a), r=14); x += 110
        c.text(900, y, note, 'sans', 24, mix(BG, MUTED, a), 'lm')
    b = fade(t, 11, 12)
    c.rect(1120, 220, 1860, 700, fill=mix(BG, SHEET, b), r=14)
    c.text(1150, 270, '越常用的字母，编码越短', 'bold', 28, mix(BG, SPARK, b), 'lm')
    c.text(1150, 330, 'E 只要一个「点」', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1150, 380, '整句话的总长度就短了', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1150, 450, '第 50 集的信号塔：98 种姿势', 'sans', 24, mix(BG, MUTED, b), 'lm')
    c.text(1150, 495, '电报：只有长和短两种', 'sans', 24, mix(BG, MUTED, b), 'lm')
    c.text(1150, 540, '少了种类，就用长短组合来补', 'sans', 24, mix(BG, MUTED, b), 'lm')
    d = fade(t, 16, 17)
    c.rect(300, 860, 1620, 960, fill=mix(BG, SHEET, d), r=12)
    c.text(960, 910, '1844 年 5 月，华盛顿—巴尔的摩线路发出第一封电报：What hath God wrought', 'bold', 26, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 9, '摩尔斯电码只有两种信号：短的「点」和长的「划」'),
                (9.2, 16, '越常用的字母编码越短：E 只要一个点。整句话发得就快'),
                (16.2, 22, '一根导线、一个电键、一套编码：消息从此按「秒」来算')], y=1010)

CLIPS = {
 'E55_小孔成像': (e55_pinhole, 22), 'E55_蓝晒': (e55_cyanotype, 22),
 'E55_片头': (titles.opening(SER8, VOL8, S8A, 3, '穿越北宋 · 《墨经》里的倒影'), 7),
 'E55_片尾': (titles.closing(SER8, VOL8, S8A, 3, '下集：一根铁钉，怎么变成开关自如的磁铁？'), 7),
 'E56_匝数': (e56_turns, 22), 'E56_磁畴': (e56_domains, 22),
 'E56_片头': (titles.opening(SER8, VOL8, S8A, 4, '穿越北宋 · 指南针之后的下一步'), 7),
 'E56_片尾': (titles.closing(SER8, VOL8, S8A, 4, '下集：一根导线，怎么把一句话传过山？'), 7),
 'E57_一根线': (e57_line, 22), 'E57_摩尔斯电码': (e57_morse, 22),
 'E57_片头': (titles.opening(SER8, VOL8, S8A, 5, '穿越北宋 · 比驿马快一万倍'), 7),
 'E57_片尾': (titles.closing(SER8, VOL8, S8A, 5, '下集：发电机倒过来用，会怎样？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
