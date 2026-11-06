"""第二十季（古法解密 7.0：织、量、写、玩）第一批：B70 纺锤、B71 缫丝、B72 提花机 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB20 = [('B70', '纺锤'), ('B71', '缫丝'), ('B72', '提花机'), ('B73', '竹编'), ('B74', '曹冲称象'),
        ('B75', '水准'), ('B76', '石磨'), ('B77', '拓印'), ('B78', '毛笔'), ('B79', '蹴鞠')]
VOL20 = '第二十季 · 古法解密 7.0'
COTTON = (235, 232, 220)
SILK = (245, 235, 200)
SERICIN = (220, 180, 90)
WOOD = (175, 125, 75)
WARP = (90, 150, 210)
WEFT = (230, 170, 80)

# ---------------------------------------------------------------- B70 纺锤
def b70_twist(c, t, i):
    corner_tag(c, 'B70 · 一拧就拉不断')
    c.text(60, 96, '没捻的纤维一拉就滑开；捻过的纤维互相挤紧，摩擦把它们锁住', 'serif', 40, INK)
    pull = fade(t, 8, 14)
    rnd = random.Random(3)
    # 左：未加捻
    x0, x1, y0 = 140, 860, 400
    c.text((x0 + x1) / 2, 300, '没捻：纤维平行躺着', 'bold', 28, INK, 'mm')
    for k in range(14):
        L = rnd.uniform(160, 260)
        s = rnd.uniform(0, x1 - x0 - L)
        y = y0 + rnd.uniform(-40, 40)
        side = -1 if s + L / 2 < (x1 - x0) / 2 else 1
        dx = side * 90 * pull
        c.line([(x0 + s + dx, y), (x0 + s + L + dx, y + rnd.uniform(-6, 6))], COTTON, 3)
    if pull > 0:
        c.arrow(x0 - 10, 600, x0 - 10 - 120 * pull, 600, NRED, 4, 14)
        c.arrow(x1 + 10, 600, x1 + 10 + 120 * pull, 600, NRED, 4, 14)
        c.text((x0 + x1) / 2, 680, '一拉就散', 'bold', 28, mix(BG, NRED, pull), 'mm')
    # 右：加捻
    x0, x1, y0 = 1060, 1780, 400
    c.text((x0 + x1) / 2, 300, '捻过：纤维绕成螺旋', 'bold', 28, INK, 'mm')
    tw = fade(t, 2, 7)
    stretch = 1 + 0.03 * pull
    for k in range(10):
        ph = k * 0.6
        pts = []
        for j in range(80):
            x = x0 + (x1 - x0) * j / 79
            y = y0 + 36 * math.sin(ph + j * 0.35 * tw) * (1 / stretch)
            pts.append((x, y))
        c.line(pts, COTTON, 3)
    if tw > 0.5:
        for xx in (1250, 1420, 1590):
            c.arrow(xx, y0 - 110, xx, y0 - 50, mix(BG, SPARK, tw), 3, 12)
            c.arrow(xx, y0 + 110, xx, y0 + 50, mix(BG, SPARK, tw), 3, 12)
        c.text((x0 + x1) / 2, y0 + 160, '往里挤紧 → 摩擦变大', 'sans', 24, mix(BG, SPARK, tw), 'mm')
    if pull > 0:
        c.arrow(x0 - 10, 600, x0 - 10 - 40 * pull, 600, GREEN, 4, 14)
        c.arrow(x1 + 10, 600, x1 + 10 + 40 * pull, 600, GREEN, 4, 14)
        c.text((x0 + x1) / 2, 680, '拉得动重物', 'bold', 28, mix(BG, GREEN, pull), 'mm')
    caps(c, t, [(0, 7, '棉花里每根纤维只有两三厘米长，平行放着，彼此之间几乎没有摩擦'),
                (7.2, 14, '一拧，纤维绕成螺旋，一拉线，螺旋就往里收紧，纤维越挤越紧'),
                (14.2, 22, '挤得越紧，摩擦越大：短短的纤维就连成了拉不断的长线')], y=1010)

def b70_spindle(c, t, i):
    corner_tag(c, 'B70 · 纺轮就是一个陀螺')
    c.text(60, 96, '纺锤下面加一个纺轮：转得更久，一直替手拧线', 'serif', 40, INK)
    for k, (nm, I, x) in enumerate((('只有一根棍', 1.0, 360), ('加了纺轮', 6.0, 900))):
        w0 = 30
        w = w0 * math.exp(-max(0, t - 1) * 0.9 / I)
        ang = w0 * I / 0.9 * (1 - math.exp(-max(0, t - 1) * 0.9 / I))
        c.line([(x, 260), (x, 820)], WOOD, 10)
        c.line([(x, 260), (x - 40, 180)], COTTON, 3)
        if I > 1:
            c.ellipse(x, 720, 120, 30, fill=(190, 140, 100), outline=INK, width=2)
            for j in range(4):
                a = ang + j * math.pi / 2
                c.line([(x, 720), (x + 110 * math.cos(a), 720 + 26 * math.sin(a))], INK, 2)
        else:
            for j in range(2):
                a = ang + j * math.pi
                c.line([(x - 12 * math.cos(a), 600), (x + 12 * math.cos(a), 600)], INK, 3)
        c.text(x, 880, nm, 'bold', 28, INK, 'mm')
        c.text(x, 930, f'转速 {w:4.1f}', 'mono', 24, SPARK, 'mm')
    ox, oy, W, H = 1250, 820, 580, 480
    c.line([(ox, oy), (ox + W, oy)], LINE, 3)
    c.line([(ox, oy), (ox, oy - H)], LINE, 3)
    for I, col in ((1.0, MUTED), (6.0, GREEN)):
        pts = [(ox + W * s / 22, oy - H * 0.9 * math.exp(-max(0, s - 1) * 0.9 / I)) for s in range(0, int(min(t, 22)) + 1)]
        if len(pts) > 1: c.line(pts, col, 4)
    c.text(ox + W / 2, oy + 40, '时间', 'sans', 22, MUTED, 'mm')
    c.text(ox + 10, oy - H - 30, '转速（示意）', 'sans', 22, MUTED, 'lm')
    caps(c, t, [(0, 7, '手一捻，一根光棍子转几下就停了'),
                (7.2, 14, '下面加一个又重又宽的纺轮，就像第 50 集的陀螺：分量离轴越远，越不容易停'),
                (14.2, 22, '纺锤一边转一边往下坠，纺轮一直替手拧线：新石器时代的人就这样纺线')], y=1010)

# ---------------------------------------------------------------- B71 缫丝
def b71_glue(c, t, i):
    corner_tag(c, 'B71 · 热水泡软丝胶')
    c.text(60, 96, '一根蚕丝：两股丝素，外面裹着一层丝胶', 'serif', 40, INK)
    hot = fade(t, 7, 13)
    cx, cy = 520, 560
    c.ellipse(cx, cy, 300 + 0 * hot, 200, fill=mix(BG, SERICIN, 0.75 * (1 - 0.7 * hot)), outline=mix(BG, SERICIN, 1 - hot * 0.6), width=4)
    for dx in (-110, 110):
        c.poly([(cx + dx - 80, cy + 70), (cx + dx + 80, cy + 70), (cx + dx, cy - 80)], SILK)
    c.text(cx - 110, cy + 120, '丝素', 'bold', 24, INK, 'mm')
    c.text(cx + 110, cy + 120, '丝素', 'bold', 24, INK, 'mm')
    c.text(cx, cy - 240, '丝胶' + ('（变软、溶开）' if hot > 0.5 else '（硬，粘住一圈圈丝）'), 'bold', 26, SERICIN, 'mm')
    c.text(cx, 900, '截面示意', 'sans', 22, MUTED, 'mm')
    # 茧与抽丝
    kx, ky = 1400, 640
    c.rect(1120, 700, 1680, 900, fill=mix(BG, (90, 140, 200), 0.25 + 0.15 * hot), r=12)
    c.text(1400, 870, '热水约 80 度（成年人操作）' if hot > 0.3 else '冷水', 'sans', 22, MUTED, 'mm')
    c.ellipse(kx, ky + 40, 110, 70, fill=SILK, outline=SERICIN, width=3)
    for k in range(5):
        c.arc(kx, ky + 40, 90 - k * 14, 55 - k * 10, 200, 340, mix(BG, SERICIN, 0.8), 2)
    if hot > 0.3:
        u = fade(t, 12, 20)
        pts = [(kx + 40 * math.sin(j * 0.6 + t * 3) * (1 - j / 40), ky - 30 - j * 9 * (0.3 + 0.7 * u)) for j in range(40)]
        c.line([(kx + 60, ky + 10)] + pts, SILK, 2)
        c.text(kx + 120, ky - 300, '一挑就抽出来', 'bold', 24, GREEN, 'lm')
    caps(c, t, [(0, 7, '蚕吐出的丝，是两股丝素被一层丝胶粘在一起；一圈圈绕成茧以后，丝胶把它们粘得死死的'),
                (7.2, 13, '放进热水，丝胶变软、慢慢溶开，一圈圈丝就松开了'),
                (13.2, 22, '用筷子轻轻一搅，挑出丝头往上抽：整个茧，是一根连续的长丝')], y=1010)

def b71_reel(c, t, i):
    corner_tag(c, 'B71 · 一个茧一根丝')
    c.text(60, 96, '绕在纸筒上数圈数：圈数 × 一圈的长度 = 一根丝有多长', 'serif', 40, INK)
    rx, ry, R = 1100, 460, 150
    turns = 1200 * fade(t, 2, 18)
    ang = turns * 2 * math.pi / 60
    c.ellipse(rx, ry, R, R, fill=mix(BG, WOOD, 0.4), outline=WOOD, width=6)
    for j in range(6):
        a = ang + j * math.pi / 3
        c.line([(rx, ry), (rx + R * math.cos(a), ry + R * math.sin(a))], WOOD, 4)
    c.ellipse(rx, ry, R + 8 + turns / 200, R + 8 + turns / 200, outline=SILK, width=2 + int(turns / 300))
    c.ellipse(420, 800, 90, 56, fill=SILK, outline=SERICIN, width=3)
    c.line([(470, 770), (rx - R, ry + 40)], SILK, 2)
    circ = 0.3
    L = turns * circ
    c.rect(1380, 640, 1840, 900, fill=SHEET, r=14)
    c.text(1610, 690, f'圈数 {turns:5.0f}', 'mono', 30, INK, 'mm')
    c.text(1610, 750, f'× 一圈 {circ} 米', 'mono', 26, MUTED, 'mm')
    c.text(1610, 820, f'= {L:4.0f} 米', 'mono', 40, SPARK, 'mm')
    c.text(1610, 870, '（示意，以实测为准）', 'sans', 20, MUTED, 'mm')
    a = fade(t, 14, 15)
    if a > 0:
        c.rect(120, 300, 700, 560, fill=mix(BG, SHEET, a), r=14)
        c.text(410, 350, '一根丝能有多长？', 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(410, 420, '常说几百米到一千多米', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(410, 470, '细到几根才抵一根头发', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(410, 520, '（拍摄前核对）', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 7, '找到丝头，绕到一个纸筒上，一圈一圈地卷'),
                (7.2, 14, '数清卷了多少圈，再乘上纸筒一圈的长度，就知道抽出了多少米'),
                (14.2, 22, '一根丝太细，缫丝时要把好几个茧的丝合在一起抽，才成一根能织布的生丝')], y=1010)

# ---------------------------------------------------------------- B72 提花机
CARD = ['00011000', '00111100', '01111110', '11100111', '11100111', '01111110', '00111100', '00011000']

def b72_weave(c, t, i):
    corner_tag(c, 'B72 · 按卡片提经线')
    c.text(60, 96, '卡片上 1 = 这根经线提起来，纬线从它下面过；一行一行织出图案', 'serif', 40, INK)
    cx0, cy0, cs = 140, 300, 50
    c.text(cx0 + 4 * cs, cy0 - 40, '花本（程序卡）', 'bold', 26, INK, 'mm')
    rows = int(fade(t, 3, 19) * 8 + 0.0001)
    for r, line in enumerate(CARD):
        for q, ch in enumerate(line):
            col = WARP if ch == '1' else mix(BG, LINE, 0.6)
            c.rect(cx0 + q * cs, cy0 + r * cs, cx0 + (q + 1) * cs - 4, cy0 + (r + 1) * cs - 4, fill=col if r < rows or r == rows else mix(BG, col, 0.5))
            c.text(cx0 + q * cs + cs / 2 - 2, cy0 + r * cs + cs / 2 - 2, ch, 'mono', 20, BG if ch == '1' else MUTED, 'mm')
        if r == min(rows, 7):
            c.arrow(cx0 - 60, cy0 + r * cs + cs / 2, cx0 - 10, cy0 + r * cs + cs / 2, GREEN, 4, 12)
    wx0, wy0, ws = 900, 280, 70
    for q in range(8):
        c.rect(wx0 + q * ws + 29, wy0 - 30, wx0 + q * ws + 41, wy0 + 8 * ws + 30, fill=mix(BG, WARP, 0.6))
    for r in range(8):
        if r < rows:
            for q in range(8):
                x = wx0 + q * ws; y = wy0 + r * ws
                if CARD[r][q] == '1':
                    c.rect(x + 4, y + 2, x + 66, y + 68, fill=WARP, r=4)
                    for k in range(3):
                        c.line([(x + 14 + k * 20, y + 6), (x + 14 + k * 20, y + 64)], mix(WARP, BG, 0.3), 2)
                else:
                    c.rect(x + 2, y + 4, x + 68, y + 66, fill=WEFT, r=4)
                    for k in range(3):
                        c.line([(x + 6, y + 16 + k * 20), (x + 64, y + 16 + k * 20)], mix(WEFT, BG, 0.25), 2)
    c.text(wx0 + 4 * ws, wy0 + 8 * ws + 70, f'织到第 {min(rows, 8)} 行：蓝色露出来的地方，就是图案', 'sans', 24, INK, 'mm')
    caps(c, t, [(0, 6, '经线竖着绷在织机上，纬线横着来回穿'),
                (6.2, 14, '每织一行，先照花本上的这一行，把标着 1 的经线提起来，纬线从它们下面穿过去'),
                (14.2, 22, '提起来的经线露在布面上：八行织完，一个菱形就出来了。换一张花本，就换一个图案')], y=1010)

def b72_program(c, t, i):
    corner_tag(c, 'B72 · 花本就是程序')
    c.text(60, 96, '同一行 0 和 1：花本里的线、打孔卡上的孔、计算机里的数', 'serif', 40, INK)
    row = CARD[3]
    cols = [('花本：提不提这根线', 220), ('雅卡尔打孔卡：有没有孔', 760), ('计算机：0 和 1', 1300)]
    for k, (nm, x0) in enumerate(cols):
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        c.text(x0 + 200, 330, nm, 'bold', 26, mix(BG, INK, a), 'mm')
        for q, ch in enumerate(row):
            x = x0 + q * 50 + 25
            if k == 0:
                c.line([(x, 400), (x, 560 if ch == '1' else 620)], mix(BG, WARP, a), 4)
                if ch == '1':
                    c.ellipse(x, 560, 10, 10, fill=mix(BG, SPARK, a))
            elif k == 1:
                c.rect(x0, 420, x0 + 400, 600, fill=mix(BG, (200, 180, 140), a)) if q == 0 else None
                if ch == '1':
                    c.ellipse(x, 510, 14, 22, fill=mix(BG, BG, a))
            else:
                c.text(x, 510, ch, 'mono', 40, mix(BG, GREEN if ch == '1' else MUTED, a), 'mm')
    b = fade(t, 15, 16)
    if b > 0:
        for k, (yr, txt) in enumerate((('汉 · 宋 · 明', '提花机用线编的花本记图案（拍摄前核对）'), ('1804 年', '雅卡尔织机：用打孔卡代替挽花工'), ('1890 年', '霍尔瑞斯用打孔卡统计人口'), ('第 91 集', '计算机照程序一步步走'))):
            c.text(300, 720 + k * 55, yr, 'bold', 24, mix(BG, SPARK, b), 'lm')
            c.text(560, 720 + k * 55, txt, 'sans', 24, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 6, '中国的提花机上，坐在高处的挽花工照着花本，一行行提起经线'),
                (6.2, 15, '一八〇四年，法国的雅卡尔把花本换成一串打了孔的卡片：有孔就提，没孔不提，不用人坐在上面了'),
                (15.2, 22, '后来，打孔卡被拿去统计人口、喂给计算机：一行 0 和 1，就是程序')], y=1010)


CLIPS = {
 'B70_加捻': (b70_twist, 22), 'B70_纺轮': (b70_spindle, 22),
 'B70_片头': (titles.opening(BSER, VOL20, SB20, 0, '新石器陶纺轮 · 宋元纺车'), 7),
 'B70_片尾': (titles.closing(BSER, VOL20, SB20, 0, '下集：一个蚕茧，怎么抽出上千米不断的丝？'), 7),
 'B71_丝胶': (b71_glue, 22), 'B71_一根丝': (b71_reel, 22),
 'B71_片头': (titles.opening(BSER, VOL20, SB20, 1, '传说嫘祖 · 宋《蚕书》'), 7),
 'B71_片尾': (titles.closing(BSER, VOL20, SB20, 1, '下集：一台木头织机，怎么织出复杂的图案？'), 7),
 'B72_经纬': (b72_weave, 22), 'B72_花本': (b72_program, 22),
 'B72_片头': (titles.opening(BSER, VOL20, SB20, 2, '汉代提花机 · 明《天工开物》花楼机'), 7),
 'B72_片尾': (titles.closing(BSER, VOL20, SB20, 2, '下集：竹篮的孔为什么常编成六角形？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
