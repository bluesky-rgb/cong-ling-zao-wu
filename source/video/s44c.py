"""第四十四季（古法解密 19.0）第三批：B196 筒车、B197 竹笕、B198 石磬 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW
from s44a import SB44, VOL44, STONE, BAMBOO

TUBE = (150, 170, 80)
SLATE = (95, 105, 115)


# ---------------------------------------------------------------- B196 筒车
def _wheel(c, cx, cy, R, rot, tilt, wl):
    c.ellipse(cx, cy, R, R, outline=mix(BG, WOOD, 1.0), width=10)
    for k in range(12):
        a = rot + k * math.pi / 6
        c.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], mix(BG, WOOD, 0.7), 4)
        px, py = cx + (R + 30) * math.cos(a), cy + (R + 30) * math.sin(a)
        c.line([(cx + R * math.cos(a), cy + R * math.sin(a)), (px, py)], mix(BG, WOOD, 1.0), 12)
    for k in range(8):
        a = rot + k * math.pi / 4 + 0.2
        bx, by = cx + (R + 10) * math.cos(a), cy + (R + 10) * math.sin(a)
        ta = a + (tilt if tilt else math.pi / 2)
        dx, dy = 40 * math.cos(ta), 40 * math.sin(ta)
        c.line([(bx - dx, by - dy), (bx + dx, by + dy)], mix(BG, TUBE, 1.0), 20)
        rel = ((a - math.pi / 2) % (2 * math.pi))
        full = rel < math.pi * 0.95
        # 竹筒口在 +d 端；若开口朝下就把水倒出来
        mouth_y = by + dy
        if full and by < wl:
            c.ellipse(bx + dx * 0.6, by + dy * 0.6, 8, 8, fill=WATER)


def b196_lift(c, t, i):
    corner_tag(c, 'B196 · 低处舀水，高处倒水')
    c.text(60, 96, '水流推着轮子下面的叶片，整个轮子转起来；轮边斜挂的竹筒转到水里舀满水，转到最高处时筒口朝下，正好倒进水槽', 'serif', 34, INK)
    cx, cy, R = 800, 600, 250
    wl = cy + R - 40
    c.rect(0, wl, W, 960, fill=mix(BG, WATER, 0.5))
    for k in range(8):
        x = ((t * 160 + k * 260) % (W + 200)) - 100
        c.arrow(x, wl + 70, x + 90, wl + 70, mix(BG, WATER_L, 1.0), 4, 12)
    rot = -t * 0.5
    _wheel(c, cx, cy, R, rot, 0.6, wl)
    c.rect(cx - 60, cy - R - 70, cx + 520, cy - R - 40, fill=mix(BG, TUBE, 0.8), r=6)
    c.rect(cx + 520, cy - R - 70, cx + 550, cy - R + 160, fill=mix(BG, TUBE, 0.8), r=6)
    ph = (t * 0.5) % (math.pi / 4)
    if ph < 0.35:
        for k in range(6):
            c.ellipse(cx - 10 + k * 3, cy - R - 30 + k * 6, 6, 6, fill=WATER)
    c.text(cx + 300, cy - R - 100, '水槽：通到高处的田', 'sans', 22, MUTED, 'mm')
    c.arc(cx, cy, R + 90, R + 90, 200, 250, SPARK, 5)
    c.text(cx - R - 140, cy - 80, '转动方向', 'sans', 20, SPARK, 'mm')
    caps(c, t, [(0, 7, '轮子下半截插在河里，水流一刻不停地推着下面的叶片'),
                (7.2, 14, '轮边斜绑着一圈竹筒，转到水里时筒口朝上，舀满了水'),
                (14.2, 22, '转到顶上，筒口歪向下，水正好倒进旁边的水槽，流到高处的田里（示意）')], y=1010)


def b196_tilt(c, t, i):
    corner_tag(c, 'B196 · 竹筒为什么要斜着绑')
    c.text(60, 96, '竹筒如果正着绑（和轮辐垂直），转到一半水就从筒口洒了；斜着绑，舀起的水一路兜着，到最高处才倒出来', 'serif', 36, INK)
    for j, (lab, tilt, ok) in enumerate([('正着绑：半路就洒光', 0.0, False), ('斜着绑：到顶才倒', 0.6, True)]):
        cx, cy, R = 480 + j * 960, 560, 230
        wl = cy + R - 30
        c.rect(cx - 380, wl, cx + 380, 920, fill=mix(BG, WATER, 0.5))
        rot = -t * 0.5
        _wheel(c, cx, cy, R, rot, tilt, wl)
        if not ok:
            r = random.Random(int(t * 4))
            for k in range(10):
                c.ellipse(cx + R + r.uniform(-40, 40), cy - r.uniform(0, 200) + k * 20, 5, 5, fill=WATER)
        c.text(cx, 900, lab, 'bold', 26, GREEN if ok else NRED, 'mm')
    caps(c, t, [(0, 7, '在水池里做两个小筒车：一个药杯正着粘，一个斜着粘'),
                (7.2, 14, '正着粘的，杯口转到侧面就朝外，水半路洒掉'),
                (14.2, 22, '斜着粘的，杯口一路兜着水，到顶才歪下来，正好倒进水槽（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B197 竹笕
def _trough(c, x0, y0, x1, y1, col):
    c.line([(x0, y0), (x1, y1)], col, 22)
    c.line([(x0, y0 - 8), (x1, y1 - 8)], mix(BG, col, 0.6), 6)


def b197_slope(c, t, i):
    corner_tag(c, 'B197 · 一节比一节低一点')
    c.text(60, 96, '水只会往低处流：竹笕一节接一节，每节都比上一节低一点点；只要一路往下斜，泉水就能自己流到很远的水缸里', 'serif', 35, INK)
    segs = []
    x, y = 160, 300
    for k in range(6):
        segs.append((x, y, x + 260, y + 70))
        x += 250
        y += 75
    p = (t * 0.12) % 1
    for k, (a, b, cx, d) in enumerate(segs):
        _trough(c, a, b, cx, d, mix(BG, BAMBOO, 1.0))
        c.rect(cx - 20, d + 10, cx + 4, 930, fill=mix(BG, WOOD, 0.6))
    for k in range(20):
        u = (p + k / 20) % 1
        pos = u * len(segs)
        si = int(pos)
        f = pos - si
        a, b, cx, d = segs[si]
        c.ellipse(a + (cx - a) * f, b + (d - b) * f - 16, 7, 7, fill=WATER)
    c.ellipse(130, 280, 50, 30, fill=mix(BG, WATER, 0.8))
    c.text(130, 230, '山泉', 'sans', 22, MUTED, 'mm')
    c.rect(1640, 760, 1800, 900, fill=mix(BG, (120, 100, 80), 1.0), r=10)
    c.rect(1650, 780, 1790, 890, fill=mix(BG, WATER, 0.7), r=8)
    c.text(1720, 940, '水缸', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '把竹子劈开、打通竹节，就成了一条半圆的槽'),
                (7.2, 14, '一节一节架在木架上，从山泉往家里一路缓缓往下斜'),
                (14.2, 22, '不用水泵，水靠自己的重量往低处流，一直流进水缸（示意）')], y=1010)


def b197_joint(c, t, i):
    corner_tag(c, 'B197 · 上节压下节，中间不能翘')
    c.text(60, 96, '接头要上一节压在下一节上面，水从上往下落进去；中间要是有一节往上翘，水就在那里停住、从旁边溢出来', 'serif', 36, INK)
    for j, (lab, bad) in enumerate([('一路往下：水流到底', False), ('中间翘起：水在低洼处溢出', True)]):
        oy = 300 + j * 330
        pts = [(160, oy), (560, oy + 60), (960, oy + 120), (1360, oy + 180), (1760, oy + 240)]
        if bad:
            pts[2] = (960, oy + 120)
            pts = [(160, oy), (560, oy + 90), (960, oy + 40), (1360, oy + 120), (1760, oy + 180)]
        for k in range(4):
            a, b = pts[k], pts[k + 1]
            _trough(c, a[0] + (6 if k else 0), a[1] - (8 if k else 0), b[0] + 10, b[1], mix(BG, BAMBOO, 1.0))
        r = random.Random(5 + j)
        if not bad:
            for k in range(14):
                u = ((t * 0.15 + k / 14) % 1) * 4
                si = int(u)
                f = u - si
                a, b = pts[si], pts[si + 1]
                c.ellipse(a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f - 14, 6, 6, fill=WATER)
        else:
            lvl = min(1.0, t / 8)
            for k in range(int(12 * lvl)):
                c.ellipse(500 + k * 10, pts[1][1] - 12 - (k % 3) * 4, 6, 6, fill=WATER)
            if lvl >= 1:
                for k in range(6):
                    c.ellipse(560 + r.uniform(-20, 20), pts[1][1] + 20 + ((t * 120 + k * 30) % 160), 5, 5, fill=WATER)
                c.text(560, pts[1][1] + 220, '溢出来', 'bold', 22, NRED, 'mm')
        c.text(1500, oy - 30, lab, 'bold', 26, NRED if bad else GREEN, 'mm')
    caps(c, t, [(0, 7, '吸管槽搭在一排从高到低的书上，最上面慢慢倒水，水一路流到杯子里'),
                (7.2, 14, '把中间一摞书垫高，那一节往上翘：水流到前面的低洼处就停住了'),
                (14.2, 22, '接头也要上节压下节；反过来接，水会从缝里漏掉（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B198 石磬
def _qing(c, cx, cy, s, col, vib=0.0):
    pts = [(-1.0, 0.0), (-0.1, -0.55), (0.25, -0.3), (1.3, 0.45), (1.15, 0.65), (0.1, 0.0), (-0.15, -0.2), (-0.9, 0.3)]
    q = []
    for k, (x, y) in enumerate(pts):
        bend = vib * math.sin(t_global[0] * 40) * (abs(x) ** 1.5)
        q.append((cx + x * s, cy + y * s + bend * 20))
    c.poly(q, mix(BG, col, 1.0))


t_global = [0.0]


def b198_hang(c, t, i):
    t_global[0] = t
    corner_tag(c, 'B198 · 挂起来才响')
    c.text(60, 96, '石板放在桌上一敲，振动被桌子吸走，「咚」一下就闷了；用绳子挂在振动最小的地方，石板能自由地振，声音又清又长', 'serif', 34, INK)
    for j, (lab, hung) in enumerate([('放在桌上：闷，一下就停', False), ('挂起来：清亮，响很久', True)]):
        cx, cy = 480 + j * 960, 520
        hit = (t % 4) < 0.15
        decay = math.exp(-((t % 4) * (0.6 if hung else 6)))
        if hung:
            c.line([(cx - 10, 220), (cx - 10, cy - 70)], mix(BG, MUTED, 1.0), 3)
        else:
            c.rect(cx - 300, cy + 120, cx + 300, cy + 160, fill=mix(BG, WOOD, 1.0))
        _qing(c, cx, cy + (60 if not hung else 0), 220, SLATE, decay * (1 if hung else 0.2))
        for k in range(int(5 * decay)):
            c.arc(cx + 250, cy, 40 + k * 32, 40 + k * 32, -40, 40, mix(BG, SPARK, decay), 4)
        c.text(cx, 880, lab, 'bold', 26, GREEN if hung else NRED, 'mm')
    caps(c, t, [(0, 7, '石磬是一块打磨成「人」字弯的石板，敲它，整块石板都在振'),
                (7.2, 14, '放在桌上，振动一下就被桌子吸走，声音闷'),
                (14.2, 22, '挂在拐角处：那里几乎不振，绳子不拦着它，声音能响很久（示意）')], y=1010)


def b198_pitch(c, t, i):
    t_global[0] = t
    corner_tag(c, 'B198 · 越短越硬，音越高')
    c.text(60, 96, '同样的石料：磬越短、越厚，振得越快，音越高；古人调音时，嫌音低就磨短两端，嫌音高就把中间磨薄一点', 'serif', 35, INK)
    for k, (lab, s, f) in enumerate([('大磬：音低', 260, 1.0), ('中磬', 200, 1.6), ('小磬：音高', 140, 2.6)]):
        cx, cy = 360 + k * 600, 520
        c.line([(cx - 10, 230), (cx - 10, cy - s * 0.3)], mix(BG, MUTED, 1.0), 3)
        _qing(c, cx, cy, s, SLATE, 0.5 * math.exp(-(t % 3)))
        wy = 800
        pts = [(cx - 200 + u * 4, wy + 30 * math.sin(u * 0.12 * f + t * 6) * math.exp(-(t % 3))) for u in range(101)]
        c.line(pts, mix(BG, SPARK, 0.9), 3)
        c.text(cx, wy + 80, lab, 'bold', 24, INK, 'mm')
    c.text(960, 940, '下面的波形：大磬振得慢，小磬振得快（示意，以调音器读数为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '挂起一块大瓷砖和一块小瓷砖，用木勺轻轻敲'),
                (7.2, 14, '小的那块振得快，调音器读出的音更高'),
                (14.2, 22, '一套编磬就是一排大小、厚薄不同的石磬，每块一个音（以实测为准）')], y=1010)


CLIPS = {
 'B196_提水': (b196_lift, 22), 'B196_斜挂': (b196_tilt, 22),
 'B196_片头': (titles.opening(BSER, VOL44, SB44, 6, '唐代已有筒车，宋元时广泛使用'), 7),
 'B196_片尾': (titles.closing(BSER, VOL44, SB44, 6, '下集：不用水泵，山泉怎么一路流到家？'), 7),
 'B197_坡度': (b197_slope, 22), 'B197_接头': (b197_joint, 22),
 'B197_片头': (titles.opening(BSER, VOL44, SB44, 7, '南方山区很早就用竹笕引山泉'), 7),
 'B197_片尾': (titles.closing(BSER, VOL44, SB44, 7, '下集：一块石板挂起来，为什么就成了乐器？'), 7),
 'B198_悬挂': (b198_hang, 22), 'B198_音高': (b198_pitch, 22),
 'B198_片头': (titles.opening(BSER, VOL44, SB44, 8, '商代已有石磬，周代有成套编磬'), 7),
 'B198_片尾': (titles.closing(BSER, VOL44, SB44, 8, '下集：笙为什么要按住小孔才响？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
