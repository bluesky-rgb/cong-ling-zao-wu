"""第十一季收尾：B39 大马士革钢、第十一季特辑（古法解密 3.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s11a import SB11, VOL11

STEEL_L = (175, 180, 190)
STEEL_D = (80, 85, 95)
CEM = (235, 235, 240)

# ---------------------------------------------------------------- B39 大马士革钢
def b39_carbide(c, t, i):
    corner_tag(c, 'B39 · 碳化物排成条纹（锻造只用动画）')
    c.text(60, 96, '高碳钢慢慢冷却，析出硬硬的碳化物颗粒', 'serif', 38, INK)
    x0, y0, W, H = 260, 220, 1400, 520
    stretch = fade(t, 6, 13)
    etch = fade(t, 14, 17)
    base = mix(STEEL_L, STEEL_D, 0.7 * etch)
    c.rect(x0, y0 + H * 0.25 * stretch, x0 + W, y0 + H - H * 0.25 * stretch, fill=base, r=8)
    rnd = random.Random(39)
    a = fade(t, 1.5, 4)
    yc = y0 + H / 2
    for k in range(160):
        u, v = rnd.random(), rnd.random() - 0.5
        if k / 160 > a: break
        # before forging: scattered; after forging: squashed toward bands
        band = round(v * 6) / 6
        vv = v + (band - v) * stretch
        x = x0 + 20 + u * (W - 40)
        y = yc + vv * H * (1 - 0.5 * stretch) * 0.85
        rx, ry = 10 + 18 * stretch, 10 - 5 * stretch
        c.ellipse(x, y, rx, ry, fill=mix(CEM, (255, 255, 255), etch))
    if 6 < t < 13:
        hx = x0 + W * ((t - 6) / 7)
        top = y0 + H * 0.25 * stretch
        c.rect(hx - 50, top - 80, hx + 50, top - 10, fill=MUTED, r=6)
        c.line([(hx, top - 80), (hx, top - 150)], (120, 100, 70), 10)
        c.text(x0 + W / 2, y0 + H + 60, '反复锻打：颗粒被压扁、排成一层层', 'bold', 26, INK, 'mm')
    if t >= 14:
        c.text(x0 + W / 2, y0 + H + 60, '酸一腐蚀：钢基体变暗，碳化物还亮 → 水波纹', 'bold', 26, mix(BG, INK, etch), 'mm')
    c.text(x0 + W, y0 - 24, '白点：碳化物（示意）', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 6, '印度一带的乌兹钢含碳很高，慢慢冷却时，碳和铁结成又硬又白的碳化物颗粒'),
                (6.2, 13, '工匠在不太高的温度下反复锻打，颗粒被压扁，排成一层层条带'),
                (13.2, 22, '再用酸一腐蚀：软的钢基体被蚀暗，碳化物不怕酸还亮着，水波纹就出来了（锻造只用动画）')], y=1010)

def b39_fold(c, t, i):
    corner_tag(c, 'B39 · 另一种「大马士革」：折叠层压')
    c.text(60, 96, '两种钢叠在一起，对折、锻合，再对折……', 'serif', 40, INK)
    n = min(10, int(fade(t, 2, 14) * 10 + 0.0001))
    layers = 2 ** (n + 1)
    x0, y0, W, H = 300, 260, 900, 420
    show = min(layers, 128)
    h = H / show
    for k in range(show):
        col = STEEL_L if k % 2 == 0 else STEEL_D
        c.rect(x0, y0 + k * h, x0 + W, y0 + (k + 1) * h + 0.5, fill=col)
    if layers > 128:
        c.text(x0 + W / 2, y0 + H + 40, '（层太细，画不出来了）', 'sans', 22, MUTED, 'mm')
    c.text(x0 + W / 2, y0 - 40, f'对折 {n} 次：{layers} 层', 'mono', 34, INK, 'mm')
    # table
    a = fade(t, 3, 4)
    tx = 1320
    for j, k in enumerate([0, 1, 2, 3, 5, 8, 10]):
        on = n >= k
        c.text(tx, 280 + j * 60, f'{k:>2} 次', 'mono', 26, mix(BG, INK if on else MUTED, a), 'lm')
        c.text(tx + 140, 280 + j * 60, f'{2 ** (k + 1):>5} 层', 'mono', 26, mix(BG, GREEN if on else MUTED, a), 'lm')
    b = fade(t, 15, 16)
    c.rect(300, 800, 1620, 880, fill=mix(BG, SHEET, b), r=10)
    c.text(330, 840, '今天市面上的「大马士革纹」刀多是这种层压钢；真正的乌兹钢工艺 18 世纪前后失传，如何复原仍有争议', 'sans', 24, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 7, '另一种做法：一软一硬两种钢叠在一起锻合，对折，再锻合，再对折'),
                (7.2, 15, '每折一次层数翻一倍：折十次就有两千多层，这是指数增长'),
                (15.2, 22, '腐蚀后两种钢深浅不同，也会露出波纹：这是层压钢，和乌兹钢的原理不一样')], y=1010)

# ---------------------------------------------------------------- 第十一季特辑
ROWS11 = [('水与土', '蒸发、重力、毛细', [('B30', '坎儿井')], [('B36', '古埃及搬巨石')], (70, 140, 200)),
          ('材料', '收缩开裂、碳、纤维、结晶', [('B31', '冰裂纹'), ('B32', '松烟墨'), ('B33', '素纱襌衣')], [('B35', '罗马混凝土'), ('B39', '大马士革钢')], COPPER),
          ('时间与天文', '擒纵、投影、齿数比', [('B34', '水运仪象台')], [('B37', '阿拉伯星盘'), ('B38', '安提基特拉机械')], SPARK)]

def s11_compare(c, t, i):
    corner_tag(c, '第十一季特辑 · 古法解密 3.0')
    c.text(60, 110, '中国与世界：同一个原理，两头各自发现', 'serif', 42, INK, 'lm')
    a = fade(t, 0.5, 1.5)
    c.text(560, 200, '中国', 'bold', 34, mix(BG, NRED, a), 'mm')
    c.text(1360, 200, '世界', 'bold', 34, mix(BG, FIELD, a), 'mm')
    for r, (name, pr, cn, wd, col) in enumerate(ROWS11):
        y = 330 + r * 220
        b = fade(t, 2 + r * 6, 3 + r * 6)
        if b <= 0: continue
        c.rect(820, y - 60, 1100, y + 60, fill=mix(BG, col, 0.35 * b), r=12)
        c.text(960, y - 18, name, 'bold', 30, mix(BG, INK, b), 'mm')
        c.text(960, y + 24, pr, 'sans', 18, mix(BG, INK, b), 'mm')
        for side, items in ((-1, cn), (1, wd)):
            for j, (num, nm) in enumerate(items):
                d = fade(t, 3 + r * 6 + j * 0.8, 4 + r * 6 + j * 0.8)
                x = 960 + side * (330 + j * 0 )
                yy = y + (j - (len(items) - 1) / 2) * 62
                bx = 960 + side * 380
                c.line([(960 + side * 140, y), (bx - side * 150, yy)], mix(BG, col, 0.7 * d), 2)
                c.rect(bx - 150, yy - 26, bx + 150, yy + 26, fill=mix(BG, SHEET, d), outline=mix(BG, col, d), width=2, r=10)
                c.text(bx - 136, yy, num, 'mono', 18, mix(BG, MUTED, d), 'lm')
                c.text(bx + 20, yy, nm, 'bold', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 8, '第十一季十集：五件中国古物，五件世界古物'),
                (8.2, 16, '坎儿井和古埃及的湿沙，都是在和水、和沙子打交道；冰裂纹、墨、罗马混凝土、大马士革钢，都是材料的学问'),
                (16.2, 24, '水运仪象台、星盘、安提基特拉机械，都在用机器「算」时间和天空'),
                (24.2, 30, '不同的地方，相似的原理：古人各自摸到了同一条物理规律')], y=1040)

CLIPS = {
 'B39_碳化物': (b39_carbide, 22), 'B39_折叠': (b39_fold, 22),
 'B39_片头': (titles.opening(BSER, VOL11, SB11, 9, '世界篇 · 中世纪中东 · 乌兹钢'), 7),
 'B39_片尾': (titles.closing(BSER, VOL11, SB11, 9, '下集：第十一季特辑 · 中国与世界'), 7),
 'S11_对照': (s11_compare, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
