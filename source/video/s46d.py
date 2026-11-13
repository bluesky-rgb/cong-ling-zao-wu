"""第四十六季（古法解密 20.0）收官：B209 龙舟 + 第四十六季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s46a import SB46, VOL46

DRAGON = (200, 60, 50)
OAR = (200, 180, 90)


# ---------------------------------------------------------------- B209 龙舟
def _boat(c, x, y, yaw, n, phases, L=900):
    cy = y
    c.poly([(x - L / 2, cy - 30 + yaw), (x + L / 2, cy - 30 - yaw), (x + L / 2 - 40, cy + 30 - yaw), (x - L / 2 + 40, cy + 30 + yaw)], mix(BG, DRAGON, 1.0))
    c.ellipse(x + L / 2 + 20, cy - 30 - yaw, 30, 22, fill=mix(BG, DRAGON, 1.0))
    for k in range(n):
        px = x - L / 2 + 80 + k * (L - 160) / max(1, n - 1)
        ph = phases[k]
        dx = 50 * math.cos(ph)
        c.line([(px, cy - 20), (px - dx, cy + 70)], mix(BG, OAR, 1.0), 6)


def b209_sync(c, t, i):
    corner_tag(c, 'B209 · 同时发力，力才叠在一起')
    c.text(60, 96, '二十个人同时往后推水，推力全部叠加；各划各的，有人发力、有人收桨，推力抵消一部分，船还会左右扭', 'serif', 36, INK)
    for j, (lab, sync) in enumerate([('听鼓点：同时发力', True), ('各划各的', False)]):
        oy = 380 + j * 330
        c.rect(0, oy - 20, W, oy + 120, fill=mix(BG, WATER, 0.4))
        n = 10
        r = random.Random(3)
        offs = [0.0] * n if sync else [r.uniform(0, 2 * math.pi) for _ in range(n)]
        phases = [t * 4 + o for o in offs]
        yaw = 0 if sync else 18 * math.sin(t * 1.3)
        dist = (t * (90 if sync else 55)) % 900
        _boat(c, 460 + dist, oy + 30, yaw, n, phases, 700)
        thrust = sum(max(0.0, math.sin(p)) for p in phases) / n
        c.text(60, oy - 60, lab, 'bold', 26, GREEN if sync else NRED, 'lm')
    c.text(960, 940, '同步时推力一下一下整齐叠加；不同步时互相抵消一部分（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '龙舟又长又窄，两边坐满桨手，每个人的力都往后推水'),
                (7.2, 14, '同时入水、同时发力，力量叠在一起，船一冲一冲地往前跑'),
                (14.2, 22, '各划各的，推力有先有后、左右不齐，船速慢下来，船头还左右摆（示意）')], y=1010)


def b209_drum(c, t, i):
    corner_tag(c, 'B209 · 鼓点就是全船的节拍器')
    c.text(60, 96, '船头的鼓手一下一下擂鼓，二十个桨手跟着鼓点入水、发力：鼓声快，划得就快；鼓点让一船人变成一个节拍', 'serif', 36, INK)
    bpm = 60 + 40 * (0.5 - 0.5 * math.cos(t * 0.3))
    beat = (t * bpm / 60) % 1
    cx, cy = 360, 520
    c.ellipse(cx, cy, 120, 120, fill=mix(BG, DRAGON, 0.9))
    c.ellipse(cx, cy, 100, 100, fill=mix(BG, (230, 210, 170), 1.0))
    hit = beat < 0.12
    sx = cx + 140 - (60 if hit else 0)
    c.line([(sx, cy - 140), (sx - 40, cy - 40)], mix(BG, WOOD, 1.0), 10)
    if hit:
        for k in range(3):
            c.arc(cx, cy, 140 + k * 30, 140 + k * 30, -40, 40, mix(BG, SPARK, 1.0 - k * 0.3), 4)
    c.text(cx, cy + 180, f'每分钟 {bpm:.0f} 下', 'bold', 28, SPARK, 'mm')
    for k in range(8):
        x = 800 + k * 130
        ph = beat * 2 * math.pi
        dx = 50 * math.cos(ph)
        c.ellipse(x, 440, 20, 20, fill=mix(BG, (230, 180, 140), 1.0))
        c.line([(x, 470), (x - dx, 620)], mix(BG, OAR, 1.0), 6)
    c.text(1250, 720, '所有桨跟着同一个节拍', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '在水盆里用一个塑料盒当龙舟，两个人各拉一根绳子往前拉'),
                (7.2, 14, '打开节拍器，听到拍子同时一拉一放：船走得快，船头一直朝前'),
                (14.2, 22, '不看节拍各拉各的：船走得慢，船头左右扭（以实测为准）')], y=1010)


OLD46 = [('阿拉伯星盘', 'B37'), ('圭表', 'B130'), ('方升', 'B106'), ('漏刻', 'B13'), ('杆秤', 'B43'), ('晒秋', 'B133'),
         ('勾股', 'B62'), ('墨斗', 'B61'), ('搓麻绳', 'B101'), ('竹编', 'B73'), ('谢公屐', 'B127'), ('竹筏', 'B174'),
         ('扁担', 'B100'), ('独轮车', 'B93'), ('桔槔', 'B90'), ('辘轳', 'B81'), ('摇橹', 'B104'), ('鼓', 'B108')]
NEW46 = [('牵星板', 'B200', ['阿拉伯星盘', '圭表']), ('天池测雨', 'B201', ['方升', '漏刻']), ('悬炭测湿', 'B202', ['杆秤', '晒秋']),
         ('规矩', 'B203', ['勾股', '墨斗']), ('草鞋', 'B204', ['搓麻绳', '竹编']), ('秧马', 'B205', ['谢公屐', '竹筏']),
         ('轿子', 'B206', ['扁担', '独轮车']), ('戽斗', 'B207', ['桔槔', '辘轳']), ('竹篙', 'B208', ['摇橹', '竹筏']),
         ('龙舟', 'B209', ['摇橹', '鼓'])]


def s46_graph(c, t, i):
    corner_tag(c, '第四十六季特辑 · 古法解密 20.0')
    c.text(60, 118, '量天与行水：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD46):
        pos[name] = (342, 218 + k * 38)
    for k, (name, num, deps) in enumerate(NEW46):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十六季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW46):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD46:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW46):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第二十季：量天与行水'),
                (8.2, 16, '星盘和圭表长出牵星板，方升长出天池测雨，杆秤长出悬炭测湿，勾股和墨斗长出规矩'),
                (16.2, 24, '搓麻绳长出草鞋，谢公屐和竹筏长出秧马，扁担长出轿子，桔槔和辘轳长出戽斗'),
                (24.2, 30, '摇橹和竹筏长出竹篙；最后，摇橹和鼓一起，长出了听着鼓点划的龙舟')], y=1040)


CLIPS = {
 'B209_同步': (b209_sync, 22), 'B209_鼓点': (b209_drum, 22),
 'B209_片头': (titles.opening(BSER, VOL46, SB46, 9, '战国时已有龙舟竞渡'), 7),
 'B209_片尾': (titles.closing(BSER, VOL46, SB46, 9, '下集：第四十六季特辑 · 古法解密 20.0 回顾'), 7),
 'S46_依赖': (s46_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
