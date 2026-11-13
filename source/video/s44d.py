"""第四十四季（古法解密 19.0）收官：B199 笙 + 第四十四季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L
from s44a import SB44, VOL44, BAMBOO

BRASS = (210, 170, 80)
WAVE = (120, 180, 230)


# ---------------------------------------------------------------- B199 笙
def b199_reed(c, t, i):
    corner_tag(c, 'B199 · 一片铜簧，来回穿过缝')
    c.text(60, 96, '竹管底部有一片薄铜簧嵌在窄缝里：吹气时簧片被推过缝、又弹回来，把气流切成一股一股，就发出声音', 'serif', 35, INK)
    cx, cy = 760, 560
    c.rect(cx - 360, cy - 30, cx + 360, cy + 30, fill=mix(BG, (90, 80, 60), 1.0), r=6)
    c.rect(cx - 300, cy - 8, cx + 300, cy + 8, fill=BG)
    f = 6.0
    disp = 70 * math.sin(t * f * 2 * math.pi / 3)
    pts = []
    for k in range(41):
        u = k / 40
        pts.append((cx - 290 + u * 580, cy + disp * u * u))
    c.line(pts, mix(BG, BRASS, 1.0), 8)
    c.rect(cx - 310, cy - 14, cx - 280, cy + 14, fill=INK)
    open_ = abs(disp) > 25
    for k in range(6):
        y0 = 280 + ((t * 300 + k * 50) % 260)
        c.arrow(cx + 150, y0 - 40, cx + 150, y0, mix(BG, WAVE, 0.8), 4, 12)
    if open_:
        for k in range(4):
            c.ellipse(cx + 150, cy + 80 + k * 40, 8, 8, fill=mix(BG, WAVE, 1.0))
    c.text(cx - 330, cy - 70, '簧片固定端', 'sans', 20, MUTED, 'lm')
    c.text(cx + 330, cy - 70, '自由端', 'sans', 20, MUTED, 'rm')
    bx = 1400
    for k in range(10):
        on = (k * 0.3 + t * 2) % 3 < 1.5
        c.rect(bx + k * 40, 760 - (60 if on else 10), bx + k * 40 + 26, 760, fill=mix(BG, SPARK if on else MUTED, 0.8))
    c.text(bx + 200, 800, '一股一股的气流（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '簧片一头固定，另一头悬在窄缝里，刚好能穿过去'),
                (7.2, 14, '气一吹，簧片被推过缝；弹回来，缝又被挡住：气流被切成一股一股'),
                (14.2, 22, '簧片振得多快，音就多高：音高由簧片自己的长短厚薄决定（示意）')], y=1010)


def b199_hole(c, t, i):
    corner_tag(c, 'B199 · 按住小孔，竹管才算数')
    c.text(60, 96, '竹管上开着小孔：孔开着，管里的空气柱和簧片对不上，不响；按住孔，管长刚好配上簧片，一起共鸣才响', 'serif', 35, INK)
    for j, (lab, closed) in enumerate([('孔开着：管子不配，几乎不响', False), ('按住孔：管子和簧片共鸣', True)]):
        cx = 480 + j * 960
        top, bot = 340, 840
        c.rect(cx - 50, top, cx + 50, bot, fill=mix(BG, BAMBOO, 0.9), r=10)
        hy = top + 140
        c.ellipse(cx + 50, hy, 16, 16, fill=BG)
        if closed:
            c.ellipse(cx + 70, hy, 34, 26, fill=mix(BG, (230, 190, 160), 1.0))
        c.rect(cx - 40, bot - 30, cx + 40, bot - 20, fill=mix(BG, BRASS, 1.0))
        Lt = (bot - top - 40) if closed else (bot - hy - 40)
        y0 = bot - 40
        amp = 36 if closed else 8
        pts = [(cx + amp * math.cos(math.pi * u / 2) * math.sin(t * 12), y0 - u * Lt) for u in [k / 40 for k in range(41)]]
        c.line(pts, mix(BG, WAVE, 1.0), 4)
        for k in range(int(5 * (1 if closed else 0.2))):
            c.arc(cx, top - 20, 30 + k * 22, 30 + k * 22, 220, 320, mix(BG, SPARK, 0.9), 4)
        c.text(cx, 900, lab, 'bold', 26, GREEN if closed else NRED, 'mm')
    caps(c, t, [(0, 7, '笙上十几根竹管插在一个斗子里，吹嘴在斗子上，所有簧片都在吹同一口气'),
                (7.2, 14, '孔开着的那几根，管子短了一截，和簧片对不上，几乎不出声'),
                (14.2, 22, '按住几个孔，就有几根管子同时响：笙能一口气吹出和声（示意）')], y=1010)


OLD44 = [('榫卯', 'B7'), ('石磨', 'B76'), ('折扇', 'B126'), ('窗纸', 'B119'), ('竹编', 'B73'), ('楔子', 'B150'),
         ('斗拱', 'B47'), ('夯土版筑', 'B46'), ('扎染', 'B45'), ('灯芯', 'B149'), ('纺锤', 'B70'), ('车辐', 'B153'),
         ('水排', 'B4'), ('龙骨水车', 'B91'), ('渴乌', 'B140'), ('坎儿井', 'B30'), ('一钟双音', 'B11'), ('三分损益', 'B107'),
         ('陶埙', 'B42'), ('笛子', 'B124')]
NEW44 = [('门轴', 'B190', ['榫卯', '石磨']), ('屏风', 'B191', ['折扇', '窗纸']), ('竹梯', 'B192', ['竹编', '楔子']),
         ('吊脚楼', 'B193', ['斗拱', '夯土版筑']), ('蜡染', 'B194', ['扎染', '灯芯']), ('纺车', 'B195', ['纺锤', '车辐']),
         ('筒车', 'B196', ['水排', '龙骨水车']), ('竹笕', 'B197', ['渴乌', '坎儿井']), ('石磬', 'B198', ['一钟双音', '三分损益']),
         ('笙', 'B199', ['陶埙', '笛子'])]


def s44_graph(c, t, i):
    corner_tag(c, '第四十四季特辑 · 古法解密 19.0')
    c.text(60, 118, '门里与田边：十件老东西接在哪里', 'serif', 42, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD44):
        pos[name] = (342, 218 + k * 38)
    for k, (name, num, deps) in enumerate(NEW44):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(342, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十四季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW44):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD44:
        x, y = pos[name]
        c.rect(x - 110, y - 16, x + 110, y + 16, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18 if len(name) < 5 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW44):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十九季：门里与田边'),
                (8.2, 16, '榫卯和石磨长出门轴，折扇长出屏风，竹编和楔子长出竹梯，斗拱长出吊脚楼'),
                (16.2, 24, '扎染长出蜡染，纺锤和车辐长出纺车，水排长出筒车，渴乌和坎儿井长出竹笕'),
                (24.2, 30, '一钟双音长出石磬；最后，陶埙和笛子一起，长出了笙')], y=1040)


CLIPS = {
 'B199_簧片': (b199_reed, 22), 'B199_按孔': (b199_hole, 22),
 'B199_片头': (titles.opening(BSER, VOL44, SB44, 9, '商代已有笙的前身，《诗经》多次写到笙'), 7),
 'B199_片尾': (titles.closing(BSER, VOL44, SB44, 9, '下集：第四十四季特辑 · 古法解密 19.0 回顾'), 7),
 'S44_依赖': (s44_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
