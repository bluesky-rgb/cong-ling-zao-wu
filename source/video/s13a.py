"""第十三季（换时代特别篇 · 汉代版）第一批：H1 摩擦起电、H2 司南、H3 纸 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

SH13 = [('H1', '摩擦起电'), ('H2', '司南'), ('H3', '纸'), ('H4', '五铢钱电堆'), ('H5', '铅钡琉璃')]
SER13, VOL13 = '从零造物 · 换时代特别篇', '第十三季 · 汉代版'
BRONZE = (176, 141, 87)
AMBER = (220, 150, 50)
FIBER = (225, 215, 190)
HAN = (150, 60, 50)

# ---------------------------------------------------------------- H1 摩擦起电
MODERN = [('兔毛', '+'), ('玻璃', '+'), ('羊毛', '+'), ('丝绸', '+/−'), ('纸', '0'), ('琥珀', '−'), ('橡胶', '−'), ('塑料', '−')]
HANLIST = [('毛皮', True), ('玻璃', False), ('羊毛', True), ('丝绸', True), ('麻布、纸', True), ('琥珀', True), ('橡胶', False), ('塑料', False)]

def h1_series(c, t, i):
    corner_tag(c, 'H1 · 汉代能找到哪些材料')
    c.text(60, 96, '同一张起电序列，换成汉代的材料', 'serif', 40, INK)
    c.text(480, 190, '今天常用（越上越爱丢电子）', 'bold', 26, MUTED, 'mm')
    c.text(1400, 190, '东汉能不能找到', 'bold', 26, HAN, 'mm')
    for k, ((name, sign), (_, has)) in enumerate(zip(MODERN, HANLIST)):
        a = fade(t, 0.5 + k * 0.6, 1.2 + k * 0.6)
        y = 270 + k * 80
        c.rect(300, y - 30, 660, y + 30, fill=mix(BG, SHEET, a), r=8)
        c.text(330, y, name, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(630, y, sign, 'mono', 26, mix(BG, MUTED, a), 'rm')
        b = fade(t, 6 + k * 0.6, 6.7 + k * 0.6)
        col = GREEN if has else NRED
        c.rect(1180, y - 30, 1620, y + 30, fill=mix(BG, col, 0.25 * b), outline=mix(BG, col, b), width=2, r=8)
        c.text(1210, y, ('有' if has else '没有 / 极少'), 'bold', 26, mix(BG, col, b), 'lm')
        c.line([(660, y), (1180, y)], mix(BG, LINE, a), 1)
    d = fade(t, 13, 14)
    c.rect(300, 920, 1620, 975, fill=mix(BG, SHEET, d), r=10)
    c.text(960, 947, '王充《论衡》：「顿牟掇芥」——摩擦过的琥珀（或玳瑁）能吸起芥菜籽（原文拍摄前核对）', 'sans', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 6, '第 01 集用的是塑料棒和毛衣。换到东汉：塑料、橡胶都没有'),
                (6.2, 13, '可琥珀、毛皮、丝绸、麻布都有：一个带正电，一个带负电，照样能起电'),
                (13.2, 22, '汉代人其实见过：王充写过「顿牟掇芥」。缺的是玻璃，存不住电（顺序为常见排法，以实测为准）')], y=1035)

def h1_store(c, t, i):
    corner_tag(c, 'H1 · 没有玻璃，拿什么存电')
    c.text(60, 96, '莱顿瓶要一层「不导电」的东西，夹在两层金属中间', 'serif', 38, INK)
    opts = [('玻璃瓶', '汉代极少', 0.95, MUTED), ('陶罐', '有，但吸潮会漏电', 0.25, NRED), ('漆器', '有，漆膜绝缘好', 0.8, GREEN), ('云母片', '有，薄而绝缘（推测）', 0.85, GREEN)]
    for k, (name, note, keep, col) in enumerate(opts):
        y = 270 + k * 170
        a = fade(t, 1 + k * 2.5, 2 + k * 2.5)
        if a <= 0: continue
        # sandwich icon
        c.rect(200, y - 50, 420, y - 34, fill=mix(BG, BRONZE, a))
        c.rect(200, y - 34, 420, y + 34, fill=mix(BG, col if k else (150, 200, 225), 0.5 * a))
        c.rect(200, y + 34, 420, y + 50, fill=mix(BG, BRONZE, a))
        c.text(470, y - 14, name, 'bold', 30, mix(BG, INK, a), 'lm')
        c.text(470, y + 26, note, 'sans', 24, mix(BG, MUTED, a), 'lm')
        # charge kept over time bar
        prog = fade(t, 2 + k * 2.5, 12)
        rem = 1 - (1 - keep) * prog
        c.rect(1000, y - 24, 1000 + 700 * rem, y + 24, fill=mix(BG, col, a), r=6)
        c.text(1000 + 700 * rem + 16, y, f'{rem * 100:.0f}%', 'mono', 24, mix(BG, INK, a), 'lm')
    c.text(1350, 210, '一分钟后还剩多少电（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '要把电存住，中间那一层必须不导电，外面两层贴上金属（汉代有铜箔、锡箔）'),
                (7.2, 14, '陶罐会吸潮，电很快漏光；漆器的漆膜、薄云母片，倒是很好的绝缘层'),
                (14.2, 22, '所以在汉代，「漆杯莱顿瓶」也许能做出来：这一集就来试（效果为推测，以实测为准）')], y=1010)

# ---------------------------------------------------------------- H2 司南
def h2_torque(c, t, i):
    corner_tag(c, 'H2 · 磁力和摩擦力拔河')
    c.text(60, 96, '一把磁勺放在盘子上：转得动吗？', 'serif', 40, INK)
    cases = [('铜盘（汉代可能的做法）', 1.0, BRONZE), ('打磨光滑的盘', 0.3, (180, 180, 190)), ('漂浮在水上（B1 指南鱼）', 0.03, (70, 140, 200))]
    mag = 0.4
    for k, (name, fr, col) in enumerate(cases):
        y = 300 + k * 230
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        c.text(100, y - 70, name, 'bold', 28, mix(BG, INK, a), 'lm')
        c.rect(100, y - 20, 100 + 600 * mag, y + 10, fill=mix(BG, FIELD, a), r=4)
        c.text(110 + 600 * mag, y - 5, '磁力的转动力', 'sans', 20, mix(BG, FIELD, a), 'lm')
        c.rect(100, y + 24, 100 + 600 * fr, y + 54, fill=mix(BG, NRED, a), r=4)
        c.text(110 + 600 * fr, y + 39, '摩擦阻力', 'sans', 20, mix(BG, NRED, a), 'lm')
        # spoon
        sx = 1400
        moves = mag > fr
        target = 0.0
        start = 1.0
        ang = start + (target - start) * (ease(fade(t, 2 + k * 4, 6 + k * 4)) if moves else 0)
        c.ellipse(sx, y + 20, 160, 70, fill=mix(BG, col, 0.4 * a))
        L = 110
        x0, y0 = sx - L * math.cos(ang), y + 20 - L * 0.4 * math.sin(ang)
        x1, y1 = sx + L * math.cos(ang), y + 20 + L * 0.4 * math.sin(ang)
        c.line([(x0, y0), (x1, y1)], mix(BG, INK, a), 8)
        c.ellipse(x0, y0, 26, 16, fill=mix(BG, INK, a))
        c.text(sx + 200, y + 20, '转到南北' if moves else '不动', 'bold', 26, mix(BG, GREEN if moves else NRED, a), 'lm')
    caps(c, t, [(0, 5, '天然磁石做的勺子，磁性不强，转动的力很小'),
                (5.2, 13, '勺底和盘子之间的摩擦，可能比磁力还大：勺子就卡着不动'),
                (13.2, 22, '盘子磨得越光越好；漂在水上几乎没有摩擦：这就是后来指南鱼、指南针要「浮」或「悬」的原因')], y=1010)

def h2_debate(c, t, i):
    corner_tag(c, 'H2 · 司南到底是什么')
    c.text(60, 96, '同一句话，学者们读出了不同的答案', 'serif', 40, INK)
    items = [('约公元 80 年', '王充《论衡·是应》：「司南之杓，投之于地，其柢指南」', INK),
             ('1940 年代', '王振铎按这句话复原出「磁勺 + 铜盘」，后来印上了邮票和课本', GREEN),
             ('近几十年', '有学者质疑：天然磁石做的勺很难转起来；「杓」也可能指北斗或别的东西', NRED),
             ('本集', '我们只做能验证的那部分：磁勺在什么盘面上转得动', SPARK)]
    for k, (when, what, col) in enumerate(items):
        y = 260 + k * 170
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        c.ellipse(220, y, 14, 14, fill=mix(BG, col, a))
        if k:
            c.line([(220, y - 156), (220, y - 14)], mix(BG, LINE, a), 3)
        c.text(270, y - 22, when, 'bold', 28, mix(BG, col, a), 'lm')
        c.text(270, y + 26, what, 'sans', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 8, '「司南」两个字最早出现在战国和汉代的书里，说它能指南'),
                (8.2, 14, '我们熟悉的磁勺，是 1940 年代王振铎的复原：它到底是不是汉代的样子，学界一直有争论（拍摄前核对）'),
                (14.2, 22, '这一集不下结论，只做实验：如果是磁勺，要满足什么条件才能指南')], y=1010)

# ---------------------------------------------------------------- H3 纸
def fiber(c, x0, y0, x1, y1, fibrils, col, rnd):
    c.line([(x0, y0), (x1, y1)], col, 6)
    if fibrils:
        for j in range(10):
            f = rnd.random()
            x = x0 + (x1 - x0) * f; y = y0 + (y1 - y0) * f
            q = rnd.uniform(0, 2 * math.pi)
            c.line([(x, y), (x + 20 * math.cos(q), y + 20 * math.sin(q))], col, 2)

def h3_beat(c, t, i):
    corner_tag(c, 'H3 · 捶打让纤维长出「毛」')
    c.text(60, 96, '不捶的纤维光溜溜，捶过的纤维毛茸茸', 'serif', 40, INK)
    for k, (name, fib) in enumerate([('只泡不捶', False), ('捶打以后', True)]):
        x0 = 140 + k * 880
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        c.text(x0 + 330, 200, name, 'bold', 30, mix(BG, INK, a), 'mm')
        c.rect(x0, 240, x0 + 660, 760, fill=mix(BG, SHEET, a), r=12)
        rnd = random.Random(3 + k)
        for j in range(16):
            xa, ya = x0 + 30 + rnd.random() * 600, 270 + rnd.random() * 460
            q = rnd.uniform(0, math.pi)
            xb, yb = xa + 160 * math.cos(q), ya + 160 * math.sin(q)
            xb = min(max(xb, x0 + 20), x0 + 640); yb = min(max(yb, 260), 740)
            fiber(c, xa, ya, xb, yb, fib, mix(BG, FIBER, a), rnd)
        if fib:
            g = fade(t, 9, 11)
            for j in range(26):
                x, y = x0 + 40 + rnd.random() * 580, 280 + rnd.random() * 440
                c.ellipse(x, y, 6, 6, fill=mix(BG, (70, 140, 200), g))
            c.text(x0 + 330, 800, '纤维之间多了无数个接触点（蓝点）：晾干后粘得牢', 'sans', 22, mix(BG, INK, g), 'mm')
        else:
            c.text(x0 + 330, 800, '纤维之间接触少：一撕就散', 'sans', 22, mix(BG, INK, a), 'mm')
    b = fade(t, 13, 14)
    c.text(960, 890, '纸不靠胶：纤维表面的分子互相「手拉手」（氢键），捶得越细，拉手的地方越多', 'bold', 26, mix(BG, GREEN, b), 'mm')
    caps(c, t, [(0, 6, '麻和树皮的纤维泡软以后，表面还是光溜溜的'),
                (6.2, 13, '用木槌反复捶打，纤维被打松、表面分出许多细丝，像毛刷一样'),
                (13.2, 22, '晾干时，细丝和细丝之间互相粘住：不用胶，纸就成形了')], y=1010)

def h3_process(c, t, i):
    corner_tag(c, 'H3 · 蔡伦改进了什么')
    c.text(60, 96, '原料便宜了，工序定下来了', 'serif', 40, INK)
    a = fade(t, 0.5, 1.5)
    c.text(120, 200, '西汉：已有麻纸（如灞桥纸），粗糙、少见（拍摄前核对）', 'sans', 26, mix(BG, MUTED, a), 'lm')
    b = fade(t, 3, 4)
    c.text(120, 260, '东汉 105 年 · 蔡伦：用树皮、麻头、破布、旧渔网造纸', 'bold', 28, mix(BG, INK, b), 'lm')
    steps = ['泡', '煮（加草木灰）', '捶打', '抄纸', '晒干']
    for k, s in enumerate(steps):
        d = fade(t, 5 + k * 1.6, 6 + k * 1.6)
        x = 220 + k * 360
        c.rect(x - 140, 420, x + 140, 540, fill=mix(BG, SHEET, d), outline=mix(BG, HAN if k == 2 else LINE, d), width=3, r=14)
        c.text(x, 480, s, 'bold', 32, mix(BG, INK, d), 'mm')
        if k:
            c.arrow(x - 220, 480, x - 150, 480, mix(BG, MUTED, d), 4, 14)
    e = fade(t, 14, 15)
    c.rect(120, 640, 1800, 860, fill=mix(BG, SHEET, e), r=12)
    c.text(150, 690, '破布、旧渔网本来是垃圾：原料几乎不要钱', 'sans', 28, mix(BG, INK, e), 'lm')
    c.text(150, 745, '草木灰煮（碱）：把纤维之间的胶质去掉，纤维更容易分开（接第 22 集肥皂）', 'sans', 28, mix(BG, INK, e), 'lm')
    c.text(150, 800, '捶打：最费力、也最关键的一步', 'bold', 28, mix(BG, HAN, e), 'lm')
    caps(c, t, [(0, 5, '蔡伦之前，西汉已经有了麻纸，但粗糙、少见，写字主要还用竹简和绢'),
                (5.2, 13, '蔡伦把便宜的原料和泡、煮、捶、抄、晒的工序定了下来'),
                (13.2, 22, '纸从此便宜起来：这一集就比一比，捶和不捶差多少')], y=1010)

CLIPS = {
 'H1_材料表': (h1_series, 22), 'H1_存电': (h1_store, 22),
 'H1_片头': (titles.opening(SER13, VOL13, SH13, 0, '东汉 · 约公元 80 年 · 王充《论衡》'), 7),
 'H1_片尾': (titles.closing(SER13, VOL13, SH13, 0, '下集：一把勺子，真的能指南吗？'), 7),
 'H2_力矩': (h2_torque, 22), 'H2_争议': (h2_debate, 22),
 'H2_片头': (titles.opening(SER13, VOL13, SH13, 1, '东汉 ·《论衡·是应》'), 7),
 'H2_片尾': (titles.closing(SER13, VOL13, SH13, 1, '下集：蔡伦之前就有纸，他改进了什么？'), 7),
 'H3_捶打': (h3_beat, 22), 'H3_工序': (h3_process, 22),
 'H3_片头': (titles.opening(SER13, VOL13, SH13, 2, '东汉 · 公元 105 年 · 蔡伦'), 7),
 'H3_片尾': (titles.closing(SER13, VOL13, SH13, 2, '下集：汉代人有没有可能做出电池？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
