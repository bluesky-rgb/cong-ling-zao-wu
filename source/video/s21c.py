"""第二十一季（第七层）第三批：E118 虚拟现实、E119 加密、E120 核电站 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s21a import S21A, SER21, VOL21

EYE = (230, 225, 210)
LOCK_A = (230, 120, 80)
LOCK_B = (90, 160, 230)
NEUT = (120, 200, 250)
URAN = (120, 190, 110)
FRAG = (230, 170, 70)
WATER = (80, 140, 200)
STEAM = (220, 220, 230)

# ---------------------------------------------------------------- E118 虚拟现实
def e118_parallax(c, t, i):
    corner_tag(c, '第 118 集 · 两只眼睛看到的不一样')
    c.text(60, 96, '东西越近，左右眼看到它的位置差得越多：大脑靠这个判断远近', 'serif', 40, INK)
    ex = [(560, 880), (720, 880)]
    for x, y in ex:
        c.ellipse(x, y, 34, 22, fill=EYE)
        c.ellipse(x, y - 4, 12, 12, fill=(60, 60, 70))
    c.text(640, 940, '左眼　右眼（相隔约 6 厘米）', 'sans', 22, MUTED, 'mm')
    d = 0.5 - 0.5 * math.cos(t / 22 * 2 * math.pi)
    oy = 280 + 450 * d
    ox = 640
    c.ellipse(ox, oy, 26, 26, fill=SPARK)
    for x, y in ex:
        c.line([(x, y - 20), (ox, oy)], mix(BG, SPARK, 0.6), 2)
    c.ellipse(ox, 230, 14, 14, fill=MUTED)
    c.text(ox + 30, 230, '远处的山', 'sans', 20, MUTED, 'lm')
    disp = min(120, 6.0 / max(0.3, (880 - oy) / 150) * 30)
    for k, (nm, sgn) in enumerate((('左眼看到', -1), ('右眼看到', 1))):
        bx = 1100 + k * 380
        c.rect(bx, 380, bx + 320, 620, fill=SHEET, outline=LINE, width=2, r=10)
        c.ellipse(bx + 160, 440, 10, 10, fill=MUTED)
        c.ellipse(bx + 160 - sgn * disp, 540, 22, 22, fill=SPARK)
        c.text(bx + 160, 660, nm, 'bold', 24, INK, 'mm')
    c.text(1450, 720, f'两张图里小球差了 {2 * disp:.0f} 像素（示意）', 'mono', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '两只眼睛隔着六厘米左右，看同一个东西，角度不一样'),
                (7.2, 14, '远处的山，两只眼看到的几乎一样；近处的球，在两张图里位置差了一大截'),
                (14.2, 22, '大脑把这点差别算成远近：差得越多，东西越近。闭上一只眼，这个线索就没了')], y=1010)

def e118_headset(c, t, i):
    corner_tag(c, '第 118 集 · 一只眼睛一块屏')
    c.text(60, 96, 'VR 头盔：左右眼各看一张图，透镜把贴脸的屏「推」到远处', 'serif', 40, INK)
    c.rect(300, 300, 1000, 760, outline=MUTED, width=6, r=40)
    c.line([(650, 300), (650, 760)], MUTED, 4)
    for k, x in enumerate((475, 825)):
        c.rect(x - 140, 330, x + 140, 380, fill=(70, 90, 130), r=6)
        c.ellipse(x, 520, 110, 30, outline=(150, 200, 240), width=5)
        c.ellipse(x, 700, 36, 24, fill=EYE)
        c.ellipse(x, 696, 12, 12, fill=(60, 60, 70))
        for dx in (-100, 0, 100):
            c.line([(x + dx, 380), (x + dx * 0.6, 520), (x, 690)], mix(BG, SPARK, 0.5), 2)
    c.text(650, 300 - 30, '两块屏（或一块屏分成两半）', 'sans', 22, MUTED, 'mm')
    c.text(1020, 520, '透镜', 'sans', 22, (150, 200, 240), 'lm')
    yaw = 25 * math.sin(t * 0.5)
    c.rect(1180, 300, 1840, 660, fill=SHEET, r=14)
    c.text(1510, 340, '头一转，画面跟着转', 'bold', 26, INK, 'mm')
    cx = 1510 - yaw * 8
    for k in range(5):
        x = cx + (k - 2) * 160
        if 1200 < x < 1820:
            c.rect(x - 40, 480, x + 40, 600, fill=mix(SHEET, (90, 120, 160), 0.6))
    c.text(1510, 630, f'头转了 {yaw:+.0f}°（陀螺仪，第 108 集）', 'mono', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, 'VR 头盔里，左眼和右眼各对着一块屏，播放的是像两只眼睛那样错开一点拍的两张图'),
                (7.2, 14, '屏离眼睛只有几厘米，中间的透镜把它「推」远，眼睛才能看清'),
                (14.2, 22, '头一转，陀螺仪马上测到，画面跟着转：大脑就信了，自己站在另一个地方')], y=1010)

# ---------------------------------------------------------------- E119 加密
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def e119_caesar(c, t, i):
    corner_tag(c, '第 119 集 · 凯撒密码')
    c.text(60, 96, '每个字母往后挪 3 位：知道「3」的人才能挪回来', 'serif', 40, INK)
    cx, cy = 560, 580
    sh = 3 * fade(t, 2, 6)
    for k, ch in enumerate(ABC):
        a = -math.pi / 2 + k * 2 * math.pi / 26
        c.text(cx + 300 * math.cos(a), cy + 300 * math.sin(a), ch, 'mono', 26, INK, 'mm')
        a2 = a - sh * 2 * math.pi / 26
        c.text(cx + 220 * math.cos(a2), cy + 220 * math.sin(a2), ch, 'mono', 26, SPARK, 'mm')
    c.ellipse(cx, cy, 260, 260, outline=LINE, width=2)
    c.ellipse(cx, cy, 180, 180, outline=LINE, width=2)
    c.text(cx, cy, '外圈：原文\n内圈：密文', 'sans', 22, MUTED, 'mm')
    msg = 'HELLO'
    enc = ''.join(ABC[(ABC.index(ch) + 3) % 26] for ch in msg)
    p = fade(t, 7, 13)
    n = int(p * len(msg) + 1e-6)
    c.text(1300, 380, '原文', 'sans', 24, MUTED, 'mm')
    c.text(1300, 440, msg, 'mono', 56, INK, 'mm')
    c.text(1300, 540, '密文', 'sans', 24, MUTED, 'mm')
    c.text(1300, 600, enc[:n] + '·' * (len(msg) - n), 'mono', 56, SPARK, 'mm')
    b = fade(t, 14, 15)
    if b > 0:
        c.rect(1020, 700, 1580, 900, fill=mix(BG, SHEET, b), r=14)
        c.text(1300, 745, '钥匙就是「挪 3 位」', 'bold', 26, mix(BG, INK, b), 'mm')
        c.text(1300, 800, '可只有 25 种挪法：一个个试就破了', 'sans', 24, mix(BG, NRED, b), 'mm')
        c.text(1300, 850, '今天的钥匙有几百位长的数字', 'sans', 22, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '两千多年前，传说凯撒这样写密信：每个字母都换成字母表里往后数第三个'),
                (6.2, 13, 'HELLO 变成 KHOOR。敌人截到了也看不懂；收信的人往回挪三位，就读出来了'),
                (13.2, 22, '可是钥匙太简单，挨个试 25 次就能破。今天网上用的钥匙，是一个长得试不完的数字')], y=1010)

def _lock(c, x, y, col, a=1.0):
    c.arc(x, y - 18, 16, 18, 180, 360, mix(BG, col, a), 6)
    c.rect(x - 22, y - 18, x + 22, y + 16, fill=mix(BG, col, a), r=4)

def e119_locks(c, t, i):
    corner_tag(c, '第 119 集 · 双锁箱')
    c.text(60, 96, '不用先交换钥匙：两把锁，来回寄三次，秘密就安全送到', 'serif', 40, INK)
    xa, xb, y = 300, 1620, 560
    c.ellipse(xa, y - 160, 50, 50, fill=LOCK_A)
    c.text(xa, y - 80, '甲', 'bold', 30, INK, 'mm')
    c.ellipse(xb, y - 160, 50, 50, fill=LOCK_B)
    c.text(xb, y - 80, '乙', 'bold', 30, INK, 'mm')
    steps = [(0, 4, xa, xa, ['A'], '甲把秘密放进箱子，挂上自己的锁'),
             (4, 7, xa, xb, ['A'], '寄给乙：路上谁也打不开'),
             (7, 9, xb, xb, ['A', 'B'], '乙再挂上自己的锁'),
             (9, 12, xb, xa, ['A', 'B'], '寄回给甲'),
             (12, 14, xa, xa, ['B'], '甲取下自己的锁'),
             (14, 17, xa, xb, ['B'], '再寄给乙'),
             (17, 22, xb, xb, [], '乙取下自己的锁，打开箱子')]
    for (a0, a1, x0, x1, locks, txt) in steps:
        if a0 <= t < a1 or (a1 == 22 and t >= a0):
            u = fade(t, a0, a1)
            x = x0 + (x1 - x0) * u
            c.rect(x - 80, y - 50, x + 80, y + 50, fill=(170, 130, 90), r=8)
            for k, L in enumerate(locks):
                _lock(c, x - 30 + k * 60, y + 80, LOCK_A if L == 'A' else LOCK_B)
            c.text(960, 820, txt, 'bold', 28, INK, 'mm')
            break
    c.line([(xa + 60, y), (xb - 60, y)], mix(BG, LINE, 0.4), 2)
    c.text(960, y - 90, '邮路（谁都能看见箱子）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 9, '甲想把秘密寄给乙，可路上全是偷看的人，两人也没见过面、没法先交钥匙'),
                (9, 17, '办法是两把锁：甲锁一次寄过去，乙再锁一次寄回来，甲解开自己的锁再寄过去'),
                (17, 22, '箱子一路上始终至少挂着一把锁。网上付钱用的公钥加密，靠的也是「锁可以公开、钥匙只在自己手里」')], y=1010)

# ---------------------------------------------------------------- E120 核电站
def e120_chain(c, t, i):
    corner_tag(c, '第 120 集 · 链式反应（动画演示）')
    c.text(60, 96, '一个中子打碎一个铀核，放出两三个中子，再去打别的铀核', 'serif', 40, INK)
    ctrl = t >= 12
    gens = min(5, int(t / 2) + 1) if not ctrl else 5
    rnd = random.Random(4)
    nodes = [(200, 560)]
    gen_counts = [1]
    for g in range(1, gens):
        new = []
        for (x, y) in nodes[-gen_counts[-1]:] if gen_counts else []:
            k = 2 if not ctrl or g < 3 else 2
            for j in range(k):
                ny = y + (j - (k - 1) / 2) * 420 / (2 ** g)
                new.append((x + 320, ny))
        if ctrl and g >= 3:
            new = new[::2]
        nodes += new
        gen_counts.append(len(new))
    idx = 0
    prev = []
    for g, n in enumerate(gen_counts):
        cur = nodes[idx: idx + n]
        for (x, y) in cur:
            c.ellipse(x, y, 22, 22, fill=URAN)
            c.ellipse(x + 30, y - 18, 12, 12, fill=FRAG)
            c.ellipse(x + 30, y + 18, 12, 12, fill=FRAG)
        if prev:
            for (x, y) in cur:
                p = min(prev, key=lambda q: abs(q[1] - y))
                c.arrow(p[0] + 40, p[1], x - 26, y, NEUT, 3, 10)
        prev = cur
        idx += n
    if ctrl:
        for k in range(4):
            x = 1000 + k * 120
            c.rect(x - 12, 230, x + 12, 860, fill=(90, 90, 100))
        c.text(1180, 210, '控制棒：吸走多余的中子', 'bold', 26, SPARK, 'mm')
    c.rect(1560, 300, 1860, 600, fill=SHEET, r=14)
    c.text(1710, 340, '每一代裂变', 'sans', 22, MUTED, 'mm')
    for g, n in enumerate(gen_counts):
        c.rect(1600, 380 + g * 40, 1600 + min(14 * n, 200), 405 + g * 40, fill=GREEN if ctrl and g >= 3 else NRED)
        c.text(1600 + min(14 * n, 200) + 10, 392 + g * 40, str(n), 'mono', 18, INK, 'lm')
    c.text(960, 940, '（只做动画演示，不涉及任何放射性物品）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 6, '铀 235 的原子核被一个中子打中，就裂成两块，放出大量的热，还甩出两三个中子'),
                (6.2, 12, '甩出的中子又去打别的铀核：一变二、二变四，越来越多，这叫链式反应'),
                (12.2, 22, '核电站插进控制棒，吸走多余的中子，让每一代只引发差不多一次：不快不慢，稳稳地放热')], y=1010)

PLANT = [(260, 520), (620, 520), (620, 760), (260, 760)]

def e120_plant(c, t, i):
    corner_tag(c, '第 120 集 · 核电站也是烧开水')
    c.text(60, 96, '反应堆放热 → 烧出蒸汽 → 推汽轮机 → 带发电机：后半截和第 10 集一模一样', 'serif', 40, INK)
    c.rect(180, 420, 520, 860, fill=(70, 80, 95), r=20)
    c.text(350, 400, '反应堆', 'bold', 28, INK, 'mm')
    for k in range(4):
        c.rect(230 + k * 75, 520, 260 + k * 75, 780, fill=(200, 120, 70))
    c.rect(700, 420, 940, 860, fill=(90, 100, 115), r=20)
    c.text(820, 400, '蒸汽发生器', 'bold', 26, INK, 'mm')
    c.rect(1080, 480, 1360, 640, fill=(120, 125, 140), r=14)
    c.text(1220, 460, '汽轮机', 'bold', 26, INK, 'mm')
    for k in range(6):
        a = t * 6 + k * math.pi / 3
        c.line([(1220, 560), (1220 + 60 * math.cos(a), 560 + 60 * math.sin(a))], (230, 230, 240), 4)
    c.rect(1440, 500, 1620, 620, fill=(150, 120, 80), r=12)
    c.text(1530, 480, '发电机', 'bold', 26, INK, 'mm')
    c.line([(1360, 560), (1440, 560)], INK, 6)
    c.line([(1620, 560), (1800, 560)], SPARK, 4)
    c.text(1810, 560, '电', 'bold', 28, SPARK, 'lm')
    for k in range(14):
        s = (t * 0.25 + k / 14) % 1
        x = 520 + (700 - 520) * (s * 2 if s < 0.5 else (1 - s) * 2)
        y = 520 if s < 0.5 else 780
        c.ellipse(x, y, 9, 9, fill=(230, 110, 80) if s < 0.5 else (120, 160, 220))
    for k in range(10):
        s = (t * 0.3 + k / 10) % 1
        if s < 0.5:
            x = 940 + (1080 - 940) * s * 2; y = 520
            col = STEAM
        else:
            x = 1080 - (1080 - 940) * (s - 0.5) * 2; y = 760
            col = WATER
        c.ellipse(x, y, 9, 9, fill=col)
    c.text(610, 900, '第一回路：高压热水（不出反应堆厂房）', 'sans', 20, MUTED, 'mm')
    c.text(1010, 900, '第二回路：蒸汽推汽轮机', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '反应堆里的链式反应放出大量的热，把一回路的水烧得滚烫'),
                (7.2, 14, '热水在蒸汽发生器里，把另一回路的水烧成蒸汽：两路水不混在一起'),
                (14.2, 22, '蒸汽推动汽轮机，带着发电机转：这一半和第 10 集蒸汽发电、第 5 集手摇发电机是一回事')], y=1010)


CLIPS = {
 'E118_视差': (e118_parallax, 22), 'E118_头盔': (e118_headset, 22),
 'E118_片头': (titles.opening(SER21, VOL21, S21A, 6, '1838 年惠斯通立体镜 · VR 头盔'), 7),
 'E118_片尾': (titles.closing(SER21, VOL21, S21A, 6, '下集：网上付钱，为什么别人截获了也看不懂？'), 7),
 'E119_凯撒': (e119_caesar, 22), 'E119_双锁箱': (e119_locks, 22),
 'E119_片头': (titles.opening(SER21, VOL21, S21A, 7, '古罗马凯撒密码 · 1977 年公钥加密'), 7),
 'E119_片尾': (titles.closing(SER21, VOL21, S21A, 7, '下集：一小块铀，为什么能发那么多电？'), 7),
 'E120_链式反应': (e120_chain, 22), 'E120_电站': (e120_plant, 22),
 'E120_片头': (titles.opening(SER21, VOL21, S21A, 8, '1942 年芝加哥一号堆 · 1954 年核电站'), 7),
 'E120_片尾': (titles.closing(SER21, VOL21, S21A, 8, '下集：为什么要把望远镜送上太空？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
