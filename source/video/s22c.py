"""第二十二季（古法解密 8.0）第三批：B86 冰嬉、B87 空竹、B88 毽子 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import SB22, VOL22, rot

ICE = (190, 220, 240)
ICE_D = (140, 180, 210)
WATERL = (120, 180, 230)
BLADE = (200, 205, 215)
RUBBER = (200, 120, 90)
CUP = (230, 200, 120)
CUP_D = (190, 150, 80)
STICK = (175, 125, 75)
CORD = (220, 220, 230)
AIRW = (120, 170, 220)
FEATHER = (230, 120, 90)
COIN = (200, 190, 150)


# ---------------------------------------------------------------- B86 冰嬉
def b86_layer(c, t, i):
    corner_tag(c, 'B86 · 冰面上那一层')
    c.text(60, 96, '冰的最外面几层分子排不整齐，像水一样能动：东西就在这层上滑（示意）', 'serif', 40, INK)
    x0, y0 = 220, 360
    rnd = random.Random(5)
    rows, cols, d = 7, 22, 54
    for r in range(rows):
        for k in range(cols):
            x = x0 + k * d + (d / 2 if r % 2 else 0)
            y = y0 + r * d * 0.87
            if r < 2:
                jx = 14 * math.sin(t * 3 + k * 1.7 + r * 2.1) + rnd.uniform(-4, 4)
                jy = 10 * math.cos(t * 2.6 + k * 1.3 + r)
                col = WATERL
            else:
                jx = 2 * math.sin(t * 4 + k + r)
                jy = 2 * math.cos(t * 4 + k * 0.7 + r)
                col = ICE
            c.ellipse(x + jx, y + jy, 16, 16, fill=col)
    c.text(x0 + cols * d + 40, y0 + 20, '最外面：像水一样会动', 'bold', 24, WATERL, 'lm')
    c.text(x0 + cols * d + 40, y0 + 300, '里面：整整齐齐的冰', 'bold', 24, ICE_D, 'lm')
    bx = 300 + (t * 60) % 900
    c.rect(bx - 90, y0 - 130, bx + 90, y0 - 40, fill=RUBBER, r=10)
    c.arrow(bx + 100, y0 - 85, bx + 200, y0 - 85, SPARK, 4, 14)
    c.text(bx, y0 - 85, '一块东西', 'sans', 20, INK, 'mm')
    c.text(960, 860, '这一层为什么会有、有多厚，科学家至今还在研究和争论', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '冰里面的水分子排得整整齐齐，像一格格的蜂窝'),
                (7.2, 14, '可是冰的最外面几层分子，排不整齐，能动来动去，有点像水'),
                (14.2, 22, '东西压在这一层上，就很容易滑开。这一层到底怎么来的，科学家还在研究')], y=1010)


def b86_wire(c, t, i):
    corner_tag(c, 'B86 · 铁丝穿冰，冰不断')
    c.text(60, 96, '压力让铁丝下面的冰化一点，铁丝往下走；上面的水没了压力，又冻回去', 'serif', 40, INK)
    cx, top, bot = 900, 360, 760
    c.rect(cx - 280, top, cx + 280, bot, fill=ICE, outline=ICE_D, width=3, r=10)
    c.rect(cx - 330, bot, cx - 280, 900, fill=STICK)
    c.rect(cx + 280, bot, cx + 330, 900, fill=STICK)
    p = min(1.0, t / 20)
    wy = top + 10 + (bot - top - 20) * p
    c.line([(cx - 400, wy), (cx + 400, wy)], BLADE, 5)
    for sgn in (-1, 1):
        x = cx + sgn * 400
        c.line([(x, wy), (x, wy + 180)], BLADE, 3)
        c.rect(x - 34, wy + 180, x + 34, wy + 300, fill=(90, 130, 190), r=10)
    c.rect(cx - 270, wy - 6, cx + 270, wy + 10, fill=WATERL)
    if wy - top > 30:
        c.rect(cx - 270, top + 10, cx + 270, wy - 8, fill=mix(ICE, ICE_D, 0.25))
    c.text(cx - 260, top + 30, '冻回去的冰', 'sans', 20, INK, 'lm')
    c.text(cx + 340, 260, '两瓶水挂在铁丝两头', 'sans', 22, MUTED, 'mm')
    c.rect(1400, 280, 1840, 600, fill=SHEET, r=14)
    c.text(1620, 320, '复冰', 'bold', 28, INK, 'mm')
    c.text(1440, 390, '铁丝下面：受压，化成水', 'sans', 22, INK, 'lm')
    c.text(1440, 450, '水从铁丝边上绕到上面', 'sans', 22, INK, 'lm')
    c.text(1440, 510, '铁丝上面：压力没了，冻回冰', 'sans', 22, INK, 'lm')
    c.text(1620, 570, '（只在 0 °C 附近才明显）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '一根细铁丝跨在冰块上，两头各挂一瓶水'),
                (7.2, 14, '铁丝下面的冰被压得化成一点水，铁丝就往下走；水绕到上面，没了压力，又冻回去'),
                (14.2, 22, '铁丝慢慢穿过了冰块，冰块却还是一整块。冰刀压冰也有这个效果，但滑主要靠那层「像水」的表面')], y=1010)


# ---------------------------------------------------------------- B87 空竹
def _diabolo(c, x, y, ang, s=1.0, spin=0.0):
    pts_l = [(x - 10 * s, y - 14 * s), (x - 90 * s, y - 70 * s), (x - 90 * s, y + 70 * s), (x - 10 * s, y + 14 * s)]
    pts_r = [(x + 10 * s, y - 14 * s), (x + 90 * s, y - 70 * s), (x + 90 * s, y + 70 * s), (x + 10 * s, y + 14 * s)]
    c.poly(rot(pts_l, x, y, ang), CUP)
    c.poly(rot(pts_r, x, y, ang), CUP)
    for k in range(3):
        yy = y + 50 * s * math.sin(spin + k * 2.1)
        for sx in (-1, 1):
            p = rot([(x + sx * 85 * s, yy), (x + sx * 50 * s, yy * 0 + y + 30 * s * math.sin(spin + k * 2.1))], x, y, ang)
            c.line(p, CUP_D, 3)
    c.ellipse(x, y, 12 * s, 12 * s, fill=CUP_D)


def b87_spin(c, t, i):
    corner_tag(c, 'B87 · 转起来就不倒')
    c.text(60, 96, '不转的空竹一碰就歪下绳子；转得飞快的空竹，歪一下又会稳住', 'serif', 40, INK)
    for k, (nm, spinning) in enumerate((('不转', False), ('转得飞快', True))):
        cx = 500 + k * 920
        cy = 560
        c.line([(cx - 300, 340), (cx - 20, cy + 14)], CORD, 3)
        c.line([(cx + 20, cy + 14), (cx + 300, 340)], CORD, 3)
        c.line([(cx - 330, 300), (cx - 300, 340)], STICK, 8)
        c.line([(cx + 330, 300), (cx + 300, 340)], STICK, 8)
        if spinning:
            ang = math.radians(6 * math.sin(t * 1.3))
            _diabolo(c, cx, cy, ang, 1.0, t * 18)
            c.arc(cx, cy, 130, 40, 200, 340, SPARK, 3)
            c.text(cx, cy + 180, '轴的方向稳稳不变', 'sans', 24, GREEN, 'mm')
        else:
            tip = min(70, max(0, (t - 3) * 14))
            ang = math.radians(tip)
            _diabolo(c, cx + tip * 1.2, cy + tip * 1.5, ang, 1.0, 0)
            c.text(cx, cy + 180, '一歪就翻下去' if tip > 30 else '一碰就歪', 'sans', 24, NRED, 'mm')
        c.text(cx, 250, nm, 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '把空竹放在绳子上，不转的时候，轻轻一碰它就歪了，掉下绳子'),
                (7.2, 14, '用绳子把它抖得飞快地转，它就像 B50 的陀螺一样，转轴的方向不肯变'),
                (14.2, 22, '转得越快越稳。抖空竹的人一直拉绳子给它「加速」，它才能一直立在绳上')], y=1010)


def b87_whistle(c, t, i):
    corner_tag(c, 'B87 · 嗡嗡声从哪儿来')
    c.text(60, 96, '空竹肚子里是空的，侧面开一个哨口：转起来，风吹过口子，里面的空气就唱', 'serif', 40, INK)
    cx, cy = 560, 580
    c.ellipse(cx, cy, 260, 260, fill=CUP, outline=CUP_D, width=6)
    c.ellipse(cx, cy, 200, 200, fill=mix(BG, CUP, 0.3))
    a0 = t * 3
    hx, hy = cx + 260 * math.cos(a0), cy + 260 * math.sin(a0)
    c.rect(hx - 20, hy - 12, hx + 20, hy + 12, fill=(40, 40, 50))
    for k in range(10):
        a = a0 - 0.15 - k * 0.12
        r = 290 + 10 * math.sin(t * 10 + k)
        c.ellipse(cx + r * math.cos(a), cy + r * math.sin(a), 6, 6, fill=mix(BG, AIRW, 1 - k / 10))
    sq = 0.5 + 0.5 * math.sin(t * 25)
    c.ellipse(cx, cy, 120 + 30 * sq, 120 + 30 * sq, outline=mix(BG, SPARK, 0.6), width=3)
    c.text(cx, cy, '空腔里的空气\n一胀一缩', 'sans', 22, INK, 'mm')
    c.rect(1120, 260, 1840, 760, fill=SHEET, r=14)
    c.text(1480, 300, '和吹瓶口一样', 'bold', 28, INK, 'mm')
    c.ellipse(1300, 520, 80, 120, fill=mix(SHEET, AIRW, 0.25), outline=AIRW, width=3)
    c.rect(1280, 380, 1320, 410, fill=mix(SHEET, AIRW, 0.25), outline=AIRW, width=3)
    c.arrow(1180, 380, 1290, 390, AIRW, 3, 12)
    c.text(1560, 440, '风吹过口子', 'sans', 24, INK, 'lm')
    c.text(1560, 500, '里面的空气像弹簧', 'sans', 24, INK, 'lm')
    c.text(1560, 560, '一胀一缩发出声音', 'sans', 24, INK, 'lm')
    c.text(1560, 640, '空腔越大，声音越低', 'bold', 24, SPARK, 'lm')
    caps(c, t, [(0, 7, '空竹的两个「轮子」是空心的，侧面开着细长的哨口'),
                (7.2, 14, '它一转，哨口就飞快地划过空气，风从口子上掠过，里面的空气被一推一拉'),
                (14.2, 22, '空腔里的空气像一根弹簧，一胀一缩就嗡嗡地响：和吹瓶口、B42 陶埙是一个道理')], y=1010)


# ---------------------------------------------------------------- B88 毽子
def _shuttle(c, x, y, ang, feathers=1.0):
    c.ellipse(x, y, 26, 26, fill=COIN, outline=(150, 140, 110), width=3)
    if feathers > 0:
        L = 120 * feathers
        for k in range(-3, 4):
            a = ang + math.pi + k * 0.12
            ex, ey = x + L * math.cos(a), y + L * math.sin(a)
            c.line([(x, y), (ex, ey)], FEATHER, 6)


def b88_flip(c, t, i):
    corner_tag(c, 'B88 · 倒着扔，它自己翻过来')
    c.text(60, 96, '重的底座在前、受风大的羽毛在后：空气把它摆成底座朝下', 'serif', 40, INK)
    for k, (nm, fe) in enumerate((('有羽毛', 1.0), ('没有羽毛', 0.0))):
        x = 520 + k * 900
        u = (t % 11) / 11
        y = 330 + 480 * u * u
        if fe > 0:
            target = math.pi / 2
            ang = -math.pi / 2 + (target + math.pi / 2) * (1 - math.exp(-u * 6))
            ang += 0.2 * math.exp(-u * 3) * math.sin(u * 30)
        else:
            ang = -math.pi / 2 + u * 9
        _shuttle(c, x, y, ang, fe)
        if fe == 0:
            c.line([(x - 12, y), (x + 12, y)], (150, 140, 110), 3)
        c.text(x - 300, 330, nm, 'bold', 30, INK, 'mm')
        for j in range(6):
            yy = 300 + j * 100
            c.arrow(x + 260, yy + 40, x + 260, yy - 10, mix(BG, AIRW, 0.6), 2, 10)
        c.text(x, 920, '底座朝下着地' if fe > 0 else '乱翻，哪边着地都有', 'sans', 24, GREEN if fe > 0 else NRED, 'mm')
    c.text(960, 560, '向上的箭头：迎面的风', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '把毽子倒过来，羽毛朝下扔：它在半空里自己翻了个身，底座朝下落地'),
                (7.2, 14, '底座重，羽毛轻却受风大：风总把受风大的一头往后推，重的一头就跑到前面'),
                (14.2, 22, '剪掉羽毛，毽子就没了「尾巴」，在空中乱翻：羽毛就是毽子的方向舵')], y=1010)


def b88_torque(c, t, i):
    corner_tag(c, 'B88 · 重心在前，阻力在后')
    c.text(60, 96, '重心和「风推的中心」不在一点：风推后头，就把它掰正', 'serif', 40, INK)
    cx, cy = 760, 560
    tilt = math.radians(50) * math.exp(-t / 5) * math.cos(t * 1.6)
    ang = math.pi / 2 + tilt
    _shuttle(c, cx, cy, ang, 1.4)
    gx, gy = cx + 12 * math.cos(ang + math.pi), cy + 12 * math.sin(ang + math.pi)
    c.ellipse(gx, gy, 10, 10, fill=NRED)
    c.text(gx + 30, gy + 10, '重心', 'bold', 22, NRED, 'lm')
    px, py = cx + 140 * math.cos(ang + math.pi), cy + 140 * math.sin(ang + math.pi)
    c.ellipse(px, py, 10, 10, fill=AIRW)
    c.text(px - 40, py, '风推的中心', 'bold', 22, AIRW, 'rm')
    c.arrow(px, py + 120, px, py + 20, AIRW, 5, 16)
    c.arrow(gx, gy - 20, gx, gy + 140, NRED, 5, 16)
    c.text(cx, 900, '下落方向 ↓', 'sans', 22, MUTED, 'mm')
    c.rect(1300, 300, 1840, 700, fill=SHEET, r=14)
    c.text(1570, 340, '箭、毽子、羽毛球', 'bold', 26, INK, 'mm')
    c.text(1340, 420, '头重：重心靠前', 'sans', 24, INK, 'lm')
    c.text(1340, 480, '尾巴受风大：风推的中心靠后', 'sans', 24, INK, 'lm')
    c.text(1340, 560, '一歪，风就把尾巴推回来', 'bold', 24, GREEN, 'lm')
    c.text(1340, 630, '下一集投壶，用的就是它', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '毽子歪一下：重心在底座，风推的中心在羽毛那头，两点不在一起'),
                (7.2, 14, '风推羽毛，就像推一根杠杆的长头，把毽子掰回底座朝下'),
                (14.2, 22, '来回晃几下就稳住了。羽毛球、箭尾的羽毛，都是这样让东西「头朝前」飞')], y=1010)


CLIPS = {
 'B86_表面层': (b86_layer, 22), 'B86_复冰': (b86_wire, 22),
 'B86_片头': (titles.opening(BSER, VOL22, SB22, 6, '清代宫廷冰嬉 ·《冰嬉图》'), 7),
 'B86_片尾': (titles.closing(BSER, VOL22, SB22, 6, '下集：空竹为什么转起来就不倒，还会嗡嗡响？'), 7),
 'B87_转稳': (b87_spin, 22), 'B87_哨口': (b87_whistle, 22),
 'B87_片头': (titles.opening(BSER, VOL22, SB22, 7, '明《帝京景物略》记抖空竹'), 7),
 'B87_片尾': (titles.closing(BSER, VOL22, SB22, 7, '下集：毽子为什么总是羽毛朝上落下？'), 7),
 'B88_翻身': (b88_flip, 22), 'B88_力矩': (b88_torque, 22),
 'B88_片头': (titles.opening(BSER, VOL22, SB22, 8, '宋代踢毽流行'), 7),
 'B88_片尾': (titles.closing(BSER, VOL22, SB22, 8, '下集：投壶时，什么样的箭更容易投进去？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
