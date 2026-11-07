"""第二十二季收尾：B89 投壶、第二十二季特辑（古法解密 8.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import SB22, VOL22, rot, WOOD

VASE = (90, 130, 120)
VASE_D = (60, 95, 85)
CHOP = (200, 160, 100)
CLAY = (200, 90, 80)
AIRW = (120, 170, 220)


# ---------------------------------------------------------------- B89 投壶
def _vase(c, x, ground, mouth=40):
    c.ellipse(x, ground - 110, 90, 110, fill=VASE)
    c.rect(x - mouth, ground - 300, x + mouth, ground - 200, fill=VASE)
    c.rect(x - mouth - 10, ground - 310, x + mouth + 10, ground - 296, fill=VASE_D, r=4)
    return ground - 303


def _stick(c, x, y, ang, L=110, head=0):
    hx, hy = x + L / 2 * math.cos(ang), y + L / 2 * math.sin(ang)
    tx, ty = x - L / 2 * math.cos(ang), y - L / 2 * math.sin(ang)
    c.line([(tx, ty), (hx, hy)], CHOP, 6)
    if head > 0:
        c.ellipse(hx, hy, 11, 11, fill=CLAY)
    elif head < 0:
        c.ellipse(tx, ty, 11, 11, fill=CLAY)


def b89_arc(c, t, i):
    corner_tag(c, 'B89 · 一条刚好落进壶口的弧线')
    c.text(60, 96, '出手的角度和快慢要配好：平着扔容易擦过壶口，高高抛起才能「掉」进去', 'serif', 40, INK)
    ground = 900
    x0, y0 = 220, 700
    vx_target = 1100
    mouth_y = _vase(c, vx_target, ground)
    c.line([(80, ground), (1840, ground)], LINE, 3)
    c.text(x0, ground + 30, '出手点', 'sans', 20, MUTED, 'mm')
    c.line([(x0, ground), (x0, y0)], mix(BG, MUTED, 0.5), 2)
    D = vx_target - x0
    h = y0 - mouth_y
    g = 900.0
    cases = [(15, (230, 150, 90), '15° 平着扔'), (40, SPARK, '40°'), (60, GREEN, '60° 高抛')]
    for k, (deg, col, nm) in enumerate(cases):
        th = math.radians(deg)
        v2 = g * D * D / (2 * math.cos(th) ** 2 * (D * math.tan(th) - h))
        v = math.sqrt(v2)
        T = D / (v * math.cos(th))
        a = fade(t, 1 + k * 5, 1 + k * 5 + 3.5)
        if a <= 0: continue
        n = 60
        pts = []
        for j in range(int(n * a) + 1):
            tt = T * j / n
            pts.append((x0 + v * math.cos(th) * tt, y0 - v * math.sin(th) * tt + 0.5 * g * tt * tt))
        if len(pts) > 1:
            c.line(pts, col, 4)
            ex, ey = pts[-1]
            if len(pts) > 2:
                px, py = pts[-2]
                _stick(c, ex, ey, math.atan2(ey - py, ex - px), 90, 1)
        vy_end = -v * math.sin(th) + g * T
        ang_in = math.degrees(math.atan2(vy_end, v * math.cos(th)))
        c.text(1400, 300 + k * 60, f'{nm}：入壶角 {ang_in:.0f}°', 'sans', 24, col, 'lm')
    c.text(vx_target, mouth_y - 40, '壶口', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '同样投进一个壶口，可以平平地扔，也可以高高地抛：每个角度都要配一个刚好的快慢'),
                (7.2, 14, '平着扔，箭斜斜地擦过来，壶口在它眼里只剩窄窄一条缝'),
                (14.2, 22, '高高抛起，箭陡陡地往下掉，壶口在它眼里宽得多：所以投壶常常往高处抛（示意，以实测为准）')], y=1010)


def b89_heavy(c, t, i):
    corner_tag(c, 'B89 · 头重的箭飞得稳')
    c.text(60, 96, '头上缠一点橡皮泥：重心靠前，飞起来自己把头摆向前方，不乱翻', 'serif', 40, INK)
    rows = [('光筷子', 0), ('头重（前端缠橡皮泥）', 1), ('尾重（后端缠橡皮泥）', -1)]
    for k, (nm, head) in enumerate(rows):
        y0 = 420 + k * 230
        c.text(80, y0 + 40, nm, 'bold', 24, INK, 'lm')
        for j in range(7):
            u = j / 6
            x = 460 + 1150 * u
            y = y0 - 120 * math.sin(math.pi * u)
            vel = math.atan2(-120 * math.pi * math.cos(math.pi * u) / 1150, 1)
            if head > 0:
                ang = vel + 0.5 * math.exp(-u * 5) * math.cos(u * 14)
            elif head == 0:
                ang = vel + 0.6 * math.sin(u * 5) * u
            else:
                ang = vel + u * 9
            if u <= (t % 11) / 11 + 1e-6:
                _stick(c, x, y, ang, 100, head)
        c.text(1700, y0 - 60, ['有点晃', '头朝前，稳', '翻跟头'][[0, 1, -1].index(head)], 'bold', 24, [MUTED, GREEN, NRED][[0, 1, -1].index(head)], 'lm')
    caps(c, t, [(0, 7, '光筷子飞出去，前后一样重，在空中会慢慢晃、转'),
                (7.2, 14, '头上缠一小团橡皮泥：重心靠前，空气推着轻的尾巴往后，箭头始终朝前'),
                (14.2, 22, '橡皮泥缠在尾巴上，就翻起跟头来。和上一集毽子一样：重的一头在前，才飞得稳')], y=1010)


# ---------------------------------------------------------------- 第二十二季特辑
OLD22 = [('水排', 'B4'), ('杠杆与滑轮组', '39'), ('齿轮与轴承', '41'), ('曹冲称象', 'B74'), ('水密隔舱', 'B24'), ('夯土版筑', 'B46'),
         ('温度计', '46'), ('古琴', 'B65'), ('纺锤', 'B70'), ('漏刻', 'B13'), ('生火', '15'), ('冰鉴与藏冰', 'B12'),
         ('陀螺', 'B50'), ('陶埙', 'B42'), ('风筝', 'B41'), ('欹器', 'B21'), ('火箭', '88')]
NEW22 = [('水碓', 'B80', ['水排', '杠杆与滑轮组']), ('辘轳', 'B81', ['杠杆与滑轮组', '齿轮与轴承']), ('羊皮筏子', 'B82', ['曹冲称象', '水密隔舱']),
         ('窑洞', 'B83', ['夯土版筑', '温度计']), ('弹棉花', 'B84', ['古琴', '纺锤']), ('香篆钟', 'B85', ['漏刻', '生火']),
         ('冰嬉', 'B86', ['冰鉴与藏冰', '温度计']), ('空竹', 'B87', ['陀螺', '陶埙']), ('毽子', 'B88', ['风筝', '欹器']),
         ('投壶', 'B89', ['毽子', '火箭'])]

def s22_graph(c, t, i):
    corner_tag(c, '第二十二季特辑 · 古法解密 8.0')
    c.text(60, 118, '转、浮、住、玩：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD22):
        pos[name] = (340, 205 + k * 46)
    for k, (name, num, deps) in enumerate(NEW22):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 172, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第二十二季新长出', 'sans', 24, MUTED, 'mm')
    newset = set(n for n, _, _ in NEW22)
    for k, (name, num, deps) in enumerate(NEW22):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in newset:
                pts = [(x0 + 110 if x0 < x1 else x0 - 110, y0), (x1 - 110 if x0 < x1 else x1 + 110, y1)]
                c.line(pts, mix(BG, COPPER, a * 0.9), 3)
                continue
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD22:
        x, y = pos[name]
        c.rect(x - 110, y - 20, x + 110, y + 20, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW22):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第八季：转、浮、住、玩'),
                (8.2, 16, '水碓和辘轳让水和摇把替人出力；羊皮筏子靠空气浮在黄河上'),
                (16.2, 24, '窑洞、弹棉花、香篆钟：住的、用的，都是热、振动和匀速'),
                (24.2, 30, '冰嬉、空竹、毽子、投壶：玩具里藏着摩擦、陀螺和飞行稳定')], y=1040)

CLIPS = {
 'B89_抛物线': (b89_arc, 22), 'B89_头重': (b89_heavy, 22),
 'B89_片头': (titles.opening(BSER, VOL22, SB22, 9, '春秋战国投壶礼 ·《礼记 · 投壶》'), 7),
 'B89_片尾': (titles.closing(BSER, VOL22, SB22, 9, '下集：第二十二季特辑 · 古法解密 8.0 回顾'), 7),
 'S22_依赖': (s22_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
