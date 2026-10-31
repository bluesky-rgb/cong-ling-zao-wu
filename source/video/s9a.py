"""第九季（古法解密 2.0）第一批：B20 公道杯、B21 欹器、B22 长信宫灯 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB9 = [('B20', '公道杯'), ('B21', '欹器'), ('B22', '长信宫灯'), ('B23', '走马灯'), ('B24', '水密隔舱'),
       ('B25', '记里鼓车'), ('B26', '灵渠陡门'), ('B27', '唧筒'), ('B28', '活塞风箱'), ('B29', '交子防伪')]
VOL9 = '第九季 · 古法解密 2.0'
WATER = (70, 140, 200)
PORC = (215, 222, 228)
BRONZE = (176, 141, 87)

# ---------------------------------------------------------------- B20 公道杯
def cup_section(c, cx, top, bot, w, level, flowing, t):
    """cross-section of a cup with a hidden inverted-U siphon around the central pillar"""
    c.rect(cx - w, top, cx + w, bot, outline=PORC, width=6, r=10)
    # water
    if top < level < bot - 10:
        c.rect(cx - w + 6, level, cx + w - 6, bot - 4, fill=mix(BG, WATER, 0.55), r=6)
    # central pillar
    pw = 46
    c.rect(cx - pw, top + 60, cx + pw, bot, fill=mix(BG, PORC, 0.25), outline=PORC, width=3, r=6)
    bend = top + 90
    # siphon: inlet near bottom inside cup (left of pillar), up inside pillar to bend, down through stem
    inner = [(cx - pw - 8, bot - 20), (cx - 16, bot - 20), (cx - 16, bend), (cx + 16, bend), (cx + 16, bot + 140)]
    seg(c, inner, mix(BG, NRED, 0.9), 6)
    if flowing:
        rnd = random.Random(int(t * 8))
        for k in range(10):
            y = bot + 150 + ((t * 300 + k * 24) % 90)
            c.ellipse(cx + 16 + rnd.uniform(-4, 4), y, 6, 9, fill=WATER)
    return bend

def b20_siphon(c, t, i):
    corner_tag(c, 'B20 · 杯里藏着的弯管')
    c.text(60, 96, '只差一点没倒满，为什么一下子全漏光？', 'serif', 40, INK)
    cx, top, bot, w = 640, 220, 720, 260
    # phases: 0-6 fill below bend, 6-9 over bend -> flow, 9-20 drain
    if t < 6:
        level = bot - (bot - (top + 110)) * ease(t / 6)
        flowing = False
    elif t < 8:
        level = top + 110 - 30 * ease((t - 6) / 2)
        flowing = t > 7.5
    else:
        level = (top + 80) + (bot - 10 - (top + 80)) * ease(min(1, (t - 8) / 9))
        flowing = level < bot - 15
    bend = cup_section(c, cx, top, bot, w, level, flowing, t)
    c.line([(cx + w + 30, bend), (cx + w + 120, bend)], SPARK, 2)
    c.text(cx + w + 130, bend, '弯管的最高点', 'sans', 24, SPARK, 'lm')
    a = fade(t, 1, 2)
    c.rect(1240, 300, 1860, 760, fill=mix(BG, SHEET, a), r=14)
    msgs = [(1, '水位低于弯管顶：管里的水上不去，杯子照常装酒'), (6.5, '水位一超过弯管顶：水翻过去，顺着杯柄里的管子往下流'),
            (9, '虹吸一旦开始，就一直吸到进水口露出水面为止：杯里的酒全漏光')]
    for k, (st, s_) in enumerate(msgs):
        b = fade(t, st, st + 1)
        y = 360 + k * 130
        words = [s_[:16], s_[16:]]
        for j, w_ in enumerate(words):
            c.text(1270, y + j * 40, w_, 'bold' if k == 2 else 'sans', 26, mix(BG, SPARK if k == 2 else INK, b), 'lm')
    caps(c, t, [(0, 6, '公道杯中间立着一根柱子，柱子里藏着一根倒 U 形的弯管'),
                (6.2, 9, '只要水位超过弯管的最高点，水就翻过去，从杯底流走'),
                (9.2, 20, '这就是第 26 集的虹吸：一旦开始，就一直流到杯子见底'),
                (20.2, 22, '「满则覆」：倒酒要适可而止')], y=1010)

def b20_threshold(c, t, i):
    corner_tag(c, 'B20 · 七分满')
    c.text(60, 96, '倒到几分满，酒还留得住？', 'serif', 40, INK)
    levels = [(0.5, '五分满', False), (0.7, '七分满', False), (0.85, '超过弯管顶', True)]
    for k, (f, lab, over) in enumerate(levels):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        cx = 360 + k * 600
        top, bot, w = 300, 720, 170
        tt = t - (2 + k * 4)
        if over and tt > 2:
            fl = max(0.0, f - (tt - 2) * 0.12)
            flowing = fl > 0.05
        else:
            fl = f; flowing = False
        level = bot - (bot - top) * fl
        c.rect(cx - w, top, cx + w, bot, outline=mix(BG, PORC, a), width=5, r=10)
        if fl > 0.02:
            c.rect(cx - w + 5, level, cx + w - 5, bot - 4, fill=mix(BG, WATER, 0.55 * a), r=6)
        bend = bot - (bot - top) * 0.78
        c.line([(cx - w - 20, bend), (cx + w + 20, bend)], mix(BG, NRED, a), 2)
        c.text(cx, 780, lab, 'bold', 30, mix(BG, INK, a), 'mm')
        res = '留得住' if not over else ('全部漏光' if fl < 0.1 else '开始漏……')
        c.text(cx, 830, res, 'bold', 28, mix(BG, GREEN if not over else NRED, a), 'mm')
        if flowing:
            for j in range(6):
                y = bot + 8 + ((t * 300 + j * 8) % 40)
                c.ellipse(cx + w - 30, y, 5, 8, fill=WATER)
    c.text(960, 250, '红线：弯管最高点', 'sans', 24, NRED, 'mm')
    caps(c, t, [(0, 5, '同一只杯子，倒到五分满：没事'),
                (5.2, 9, '七分满：还是没事'),
                (9.2, 22, '一旦超过弯管顶：一滴不剩。传说它是在劝人「知足」；原理，是一根看不见的管子')], y=1010)

# ---------------------------------------------------------------- B21 欹器
def qiqi_draw(c, cx, py, fill, ang, a=1.0):
    """vessel hung at pivot (cx, py); fill 0..1; ang tilt (rad, positive = clockwise)"""
    H, Wt, Wb = 300, 150, 70
    # vessel points relative to pivot: pivot sits at y = 100 below rim (rim at -100, bottom at +200)
    rim, base = -110, 190
    pts = [(-Wt, rim), (Wt, rim), (Wb, base), (-Wb, base)]
    def rot(p):
        x, y = p
        return (cx + x * math.cos(ang) - y * math.sin(ang), py + x * math.sin(ang) + y * math.cos(ang))
    if fill > 0:
        lvl = base - (base - rim) * fill
        wl = Wb + (Wt - Wb) * (base - lvl) / (base - rim)
        wpts = [(-wl, lvl), (wl, lvl), (Wb, base), (-Wb, base)]
        c.poly([rot(p) for p in wpts], mix(BG, WATER, 0.6 * a))
    seg(c, [rot(p) for p in pts] + [rot(pts[0])], mix(BG, BRONZE, a), 6)
    c.ellipse(cx, py, 10, 10, fill=mix(BG, SPARK, a))

def b21_states(c, t, i):
    corner_tag(c, 'B21 · 虚则欹，中则正，满则覆')
    c.text(60, 96, '同一只罐子，空着、半满、装满，为什么姿势全不一样？', 'serif', 40, INK)
    states = [(0.0, 0.45, '虚则欹', '空着：歪向一边'), (0.5, 0.0, '中则正', '半满：端端正正'), (1.0, 2.3, '满则覆', '装满：翻倒，把水倒光')]
    for k, (fill, ang, lab, sub) in enumerate(states):
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        cx, py = 360 + k * 600, 470
        c.line([(cx - 220, py), (cx + 220, py)], mix(BG, MUTED, a), 4)
        c.line([(cx - 220, py), (cx - 220, 840)], mix(BG, MUTED, a), 6)
        c.line([(cx + 220, py), (cx + 220, 840)], mix(BG, MUTED, a), 6)
        ang_now = ang * ease(fade(t, 2 + k * 5, 4 + k * 5))
        f = fill if k < 2 else max(0, 1 - fade(t, 13.5, 15.5))
        qiqi_draw(c, cx, py, f, ang_now, a)
        c.text(cx, 220, lab, 'serif', 40, mix(BG, SPARK, a), 'mm')
        c.text(cx, 880, sub, 'sans', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '《荀子》记载：孔子在鲁桓公庙里见到一只「欹器」'),
                (6.2, 11, '空着它是歪的，倒进一半水就正了'),
                (11.2, 22, '再倒满，它一下翻了过去，把水倒光，又回到歪着的样子：「虚则欹，中则正，满则覆」')], y=1010)

def b21_com(c, t, i):
    corner_tag(c, 'B21 · 重心和吊点')
    c.text(60, 96, '罐子会不会翻，只看一件事：重心在吊点上面还是下面', 'serif', 38, INK)
    cases = [('空着', -40, 0.0, '重心在吊点上方：站不稳，歪倒靠在一边'), ('半满', 70, 0.5, '水把重心拉到吊点下方：稳稳挂正'), ('装满', -30, 1.0, '水太多，重心又升到吊点上方：翻过去')]
    for k, (lab, comy, fill, note) in enumerate(cases):
        a = fade(t, 1 + k * 5, 2 + k * 5)
        if a <= 0: continue
        cx, py = 360 + k * 600, 480
        qiqi_draw(c, cx, py, fill, 0.0, a)
        c.ellipse(cx, py + comy, 16, 16, fill=mix(BG, NRED, a))
        c.text(cx + 30, py + comy, '重心', 'bold', 22, mix(BG, NRED, a), 'lm')
        c.text(cx - 30, py, '吊点', 'sans', 22, mix(BG, SPARK, a), 'rm')
        c.text(cx, 770, lab, 'bold', 32, mix(BG, INK, a), 'mm')
        c.text(cx, 830, note[:12], 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(cx, 870, note[12:], 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '罐子从两侧的吊点挂着；空罐的重心，故意做在吊点上方'),
                (6.2, 11, '倒进水，水在底部，把整体重心往下拉，低过吊点：稳了'),
                (11.2, 22, '水越来越多，重心又往上走，越过吊点：翻倒。古人把重心算得这么准，用来提醒人「满招损」')], y=1010)

# ---------------------------------------------------------------- B22 长信宫灯
def lamp(c, cx, cy, a, t, smoke=True):
    # kneeling figure body (hollow), raised right arm as chimney over the lamp tray
    body = [(cx - 120, cy + 260), (cx + 120, cy + 260), (cx + 100, cy - 40), (cx + 50, cy - 160), (cx - 50, cy - 160), (cx - 100, cy - 40)]
    c.poly(body, mix(BG, BRONZE, 0.35 * a))
    seg(c, body + [body[0]], mix(BG, BRONZE, a), 5)
    c.ellipse(cx, cy - 210, 55, 60, fill=mix(BG, BRONZE, 0.35 * a), outline=mix(BG, BRONZE, a), width=4)
    # lamp tray at left
    lx, ly = cx - 320, cy + 120
    c.rect(lx - 110, ly, lx + 110, ly + 24, fill=mix(BG, BRONZE, a), r=4)
    c.rect(lx - 100, ly - 150, lx - 90, ly, fill=mix(BG, BRONZE, a))
    c.rect(lx + 90, ly - 150, lx + 100, ly, fill=mix(BG, BRONZE, a))
    # flame
    fh = 60 + 10 * math.sin(t * 9)
    c.poly([(lx - 16, ly), (lx + 16, ly), (lx, ly - fh)], mix(BG, SPARK, a))
    # sleeve / arm chimney: from above lamp into body shoulder
    arm = [(lx - 90, ly - 150), (lx - 60, ly - 260), (cx - 160, cy - 300), (cx - 60, cy - 120)]
    arm2 = [(lx + 90, ly - 150), (lx + 60, ly - 210), (cx - 140, cy - 230), (cx - 40, cy - 90)]
    seg(c, arm, mix(BG, BRONZE, a), 5); seg(c, arm2, mix(BG, BRONZE, a), 5)
    if smoke:
        rnd = random.Random(22)
        path = [(lx, ly - 70), (lx, ly - 200), (cx - 150, cy - 270), (cx - 50, cy - 100), (cx, cy + 100)]
        L = [math.dist(path[j], path[j + 1]) for j in range(len(path) - 1)]; tot = sum(L)
        for k in range(22):
            d = ((t * 140 + k * tot / 22) % tot)
            for j in range(len(L)):
                if d <= L[j]:
                    f = d / L[j]
                    x = path[j][0] + (path[j + 1][0] - path[j][0]) * f + rnd.uniform(-10, 10)
                    y = path[j][1] + (path[j + 1][1] - path[j][1]) * f
                    c.ellipse(x, y, 9, 9, fill=mix(BG, (150, 150, 150), 0.7 * a)); break
                d -= L[j]
    return lx, ly

def b22_chimney(c, t, i):
    corner_tag(c, 'B22 · 袖子里的烟道')
    c.text(60, 96, '两千年前的油灯，为什么不把屋子熏黑？', 'serif', 40, INK)
    a = fade(t, 0.3, 1.2)
    lamp(c, 900, 560, a, t, smoke=t > 4)
    b = fade(t, 5, 6)
    c.rect(1280, 260, 1860, 720, fill=mix(BG, SHEET, b), r=14)
    c.text(1310, 310, '① 灯火上方罩着宫女的右袖', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1310, 370, '② 热烟往上升，钻进袖管', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1310, 430, '③ 顺着手臂进入中空的身体', 'sans', 26, mix(BG, INK, b), 'lm')
    c.text(1310, 490, '④ 烟灰落在冷的内壁上', 'sans', 26, mix(BG, INK, b), 'lm')
    d = fade(t, 13, 14)
    c.text(1310, 570, '灯身能拆开清洗', 'bold', 28, mix(BG, SPARK, d), 'lm')
    c.text(1310, 625, '1968 年河北满城汉墓出土 · 西汉', 'sans', 22, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 4, '长信宫灯：一位跪坐的宫女，左手托灯，右手举起罩在灯火上方'),
                (4.2, 13, '热烟往上升，钻进宽大的袖管，顺着手臂流进她中空的身体，烟灰就留在里面'),
                (13.2, 22, '和第 36 集的通风、第 44 集的热气球是同一个道理：热空气往上走，给它修一条路')], y=1010)

def b22_shade(c, t, i):
    corner_tag(c, 'B22 · 可以转的灯罩')
    c.text(60, 96, '两块弧形铜板，怎么调亮度和方向？', 'serif', 40, INK)
    cx, cy, R = 700, 560, 200
    open_ = 0.15 + 0.85 * (0.5 + 0.5 * math.sin((t - 3) * 0.6)) if t > 3 else 1.0
    gap = math.pi * 0.9 * open_
    c.ellipse(cx, cy, 30, 30, fill=SPARK)
    for k in range(40):
        ang = -gap / 2 + gap * k / 39
        c.line([(cx, cy), (cx + 600 * math.cos(ang), cy + 600 * math.sin(ang))], mix(BG, SPARK, 0.15), 6)
    # two shades: fixed one on left half, movable one
    c.arc(cx, cy, R, R, 90 + 0, 270, BRONZE, 18)
    c.arc(cx, cy, R, R, int(math.degrees(gap / 2)), 90, BRONZE, 18)
    c.arc(cx, cy, R, R, 270, 360 - int(math.degrees(gap / 2)), BRONZE, 18)
    pct = gap / (math.pi * 0.9) * 100
    c.text(cx, cy + 320, f'开口约 {pct:.0f}%', 'mono', 30, INK, 'mm')
    a = fade(t, 2, 3)
    c.rect(1240, 280, 1860, 640, fill=mix(BG, SHEET, a), r=14)
    c.text(1270, 330, '灯罩是两块弧形铜板', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 390, '一块能左右推开、合上', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1270, 460, '开口大：亮，照得宽', 'bold', 26, mix(BG, SPARK, a), 'lm')
    c.text(1270, 515, '开口小：暗，只照一个方向', 'bold', 26, mix(BG, SPARK, a), 'lm')
    c.text(1270, 585, '像今天能调的台灯', 'sans', 24, mix(BG, MUTED, a), 'lm')
    caps(c, t, [(0, 3, '灯盘四周围着两块弧形的铜灯罩'),
                (3.2, 12, '推开一块，开口变大，光照得又亮又宽；合上一些，只往一个方向照'),
                (12.2, 22, '烟有路走、光能调节、还能拆开洗：两千年前的一盏「环保台灯」')], y=1010)

CLIPS = {
 'B20_弯管': (b20_siphon, 22), 'B20_七分满': (b20_threshold, 22),
 'B20_片头': (titles.opening(BSER, VOL9, SB9, 0, '传说 · 明代景德镇'), 7),
 'B20_片尾': (titles.closing(BSER, VOL9, SB9, 0, '下集：空着歪、半满正、装满翻的罐子'), 7),
 'B21_三种姿势': (b21_states, 22), 'B21_重心': (b21_com, 22),
 'B21_片头': (titles.opening(BSER, VOL9, SB9, 1, '春秋 · 鲁桓公庙 ·《荀子·宥坐》'), 7),
 'B21_片尾': (titles.closing(BSER, VOL9, SB9, 1, '下集：两千年前的油灯，为什么不熏屋子？'), 7),
 'B22_烟道': (b22_chimney, 22), 'B22_灯罩': (b22_shade, 22),
 'B22_片头': (titles.opening(BSER, VOL9, SB9, 2, '西汉 · 河北满城 · 窦绾墓'), 7),
 'B22_片尾': (titles.closing(BSER, VOL9, SB9, 2, '下集：灯一点亮，纸马为什么自己跑？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
