"""第三十五季（第十四层：看与听的机器）收官：E191 视频通话 + 第三十五季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s35a import S35A, SER35, VOL35, LIGHT

FACE = [
    "..........",
    "...####...",
    "..#....#..",
    ".#.#..#.#.",
    ".#......#.",
    ".#.#..#.#.",
    ".#..##..#.",
    "..#....#..",
    "...####...",
    "..........",
]


def _frame(blink, mouth):
    g = [list(r) for r in FACE]
    if blink:
        g[3][3] = '.'
        g[3][6] = '.'
    if mouth:
        g[6][4] = '.'
        g[6][5] = '.'
        g[7][4] = '#'
        g[7][5] = '#'
    return g


FRAMES = [_frame(False, False), _frame(False, False), _frame(True, False), _frame(False, False), _frame(False, True), _frame(False, True)]


def _grid(c, x0, y0, cs, g, prev=None, hl=True):
    for r in range(10):
        for k in range(10):
            ch = g[r][k]
            changed = prev is not None and prev[r][k] != ch
            c.rect(x0 + k * cs, y0 + r * cs, x0 + (k + 1) * cs - 2, y0 + (r + 1) * cs - 2,
                   fill=INK if ch == '#' else SHEET)
            if changed and hl:
                c.rect(x0 + k * cs - 2, y0 + r * cs - 2, x0 + (k + 1) * cs, y0 + (r + 1) * cs, outline=SPARK, width=3)


def _ndiff(a, b):
    return sum(1 for r in range(10) for k in range(10) if a[r][k] != b[r][k])


# ---------------------------------------------------------------- E191 视频通话
def e191_frames(c, t, i):
    corner_tag(c, '第 191 集 · 一秒几十张画面，大部分没变')
    c.text(60, 96, '视频就是一张接一张的画面；相邻两张几乎一模一样，变的只是眨眼、张嘴那一小块', 'serif', 36, INK)
    n = min(len(FRAMES), 1 + int(t / 3))
    cs = 26
    for j in range(n):
        x0 = 110 + j * 290
        _grid(c, x0, 300, cs, FRAMES[j], FRAMES[j - 1] if j else None)
        c.text(x0 + 130, 300 + 10 * cs + 40, f'第 {j + 1} 张', 'bold', 22, INK, 'mm')
        if j:
            d = _ndiff(FRAMES[j], FRAMES[j - 1])
            c.text(x0 + 130, 300 + 10 * cs + 80, f'变了 {d} 格', 'mono', 22, SPARK if d else GREEN, 'mm')
    c.rect(300, 760, 1620, 880, fill=SHEET, r=14)
    c.text(960, 800, '真实的视频：每张几百万个像素，一秒 30 张', 'bold', 26, INK, 'mm')
    c.text(960, 845, '整张整张地传，网速远远不够', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '摄像头一秒钟拍下几十张画面，连起来就动了'),
                (7.2, 14, '一张一张比一比：背景没动，脸大部分没动，只有眨眼、张嘴那几格变了'),
                (14.2, 22, '要是每张都整张发过去，再快的网也会卡（示意）')], y=1010)


def e191_changes(c, t, i):
    corner_tag(c, '第 191 集 · 只传变了的那一小块')
    c.text(60, 96, '第一张整张发过去；以后每张只说「哪几格变了」，对方在上一张上改一改，要说的话少了好几十倍', 'serif', 36, INK)
    cs = 34
    _grid(c, 120, 260, cs, FRAMES[2], FRAMES[1])
    c.text(120 + 5 * cs, 260 + 10 * cs + 40, '要发的这一张', 'bold', 22, INK, 'mm')
    p = min(1.0, t / 14)
    full = 100
    diff = _ndiff(FRAMES[2], FRAMES[1])
    bx, by = 760, 300
    c.rect(bx - 40, by - 40, 1860, 720, fill=SHEET, r=14)
    for j, (lab, v, col) in enumerate([('整张报', full, NRED), ('只报变了的', diff, GREEN)]):
        y = by + 60 + j * 200
        c.text(bx, y - 40, lab, 'bold', 26, INK, 'lm')
        w = 1000 * v / full * p
        c.rect(bx, y, bx + max(6, w), y + 70, fill=mix(BG, col, 0.85), r=8)
        c.text(bx + max(6, w) + 20, y + 35, f'{v * p:.0f} 句', 'mono', 26, col, 'lm')
    c.text(1290, 660, '「第 4 行第 4 格白」「第 4 行第 7 格白」……', 'sans', 22, MUTED, 'mm')
    c.text(960, 800, '网速不够时：宁可把格子画大一点（画面模糊），也不让画面停住', 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '两人背对背：第一次把 100 个格子一格一格全报给对方'),
                (7.2, 14, '第二张只报变了的那两格，对方在上一张上改一改就行'),
                (14.2, 22, '真正的视频通话也这样：只传变化，再把画面压小，网速一般也不卡（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十五季特辑
OLD35 = [('电动机', '58'), ('留声机', '73'), ('电子墨水屏', '116'), ('电视', '82'), ('透镜', '52'), ('照相', '55'),
         ('触摸屏', '96'), ('激光', '94'), ('LED', '102'), ('电灯', '60'), ('降噪耳机', '106'), ('人工耳蜗', '137'),
         ('语音识别', '105'), ('数码相机', '95'), ('显微镜', '53'), ('互联网', '98')]
NEW35 = [('扬声器', '182', ['电动机', '留声机']), ('液晶屏', '183', ['电子墨水屏', '电视']), ('投影仪', '184', ['透镜', '照相']),
         ('防窥膜', '185', ['触摸屏', '液晶屏']), ('光盘', '186', ['留声机', '激光']), ('夜光表盘', '187', ['LED', '电灯']),
         ('骨传导耳机', '188', ['降噪耳机', '人工耳蜗']), ('调音器', '189', ['留声机', '语音识别']), ('自动对焦', '190', ['数码相机', '显微镜']),
         ('视频通话', '191', ['互联网', '数码相机'])]


def s35_layer(c, t, i):
    corner_tag(c, '第三十五季特辑 · 第十四层')
    c.text(60, 118, '第十四层：看与听的机器', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD35):
        pos[name] = (340, 210 + k * 50)
    for k, (name, num, deps) in enumerate(NEW35):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 165, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十五季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW35):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            if x0 > 1000:
                sx, ex = x0, x1 - 110 if x1 > x0 else x1 + 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD35:
        x, y = pos[name]
        c.rect(x - 110, y - 19, x + 110, y + 19, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW35):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十四层的十集：每天看的屏幕、听的声音背后的机器'),
                (8.2, 16, '电动机长出扬声器，电视长出液晶屏，透镜长出投影仪，液晶屏又长出防窥膜'),
                (16.2, 24, '激光长出光盘，LED 长出夜光表盘，人工耳蜗长出骨传导，显微镜长出自动对焦'),
                (24.2, 30, '最后，互联网和数码相机一起，长出了视频通话')], y=1040)


CLIPS = {
 'E191_帧': (e191_frames, 22), 'E191_只传变化': (e191_changes, 22),
 'E191_片头': (titles.opening(SER35, VOL35, S35A, 9, '2003 年网络视频通话开始普及'), 7),
 'E191_片尾': (titles.closing(SER35, VOL35, S35A, 9, '下集：第三十五季特辑 · 第十四层回顾'), 7),
 'S35_第十四层': (s35_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
