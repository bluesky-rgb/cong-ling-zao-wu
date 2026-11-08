"""第三十季（古法解密 12.0：玩、响、用）收官：B129 印章 + 第三十季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO
from s30a import SB30, VOL30

SEAL = (200, 60, 50)
STONE = (190, 175, 150)
GLYPH = [((0.45, 0.12), (0.45, 0.88)), ((0.45, 0.5), (0.82, 0.5)), ((0.12, 0.88), (0.88, 0.88))]


def _glyph(c, x, y, s, col, mirror=False, w=18, jitter=None):
    for (a, b) in GLYPH:
        ax, bx = (1 - a[0], 1 - b[0]) if mirror else (a[0], b[0])
        pts = [(x + ax * s, y + a[1] * s), (x + bx * s, y + b[1] * s)]
        if jitter is None:
            c.line(pts, col, w)
        else:
            n = 24
            for j in range(n):
                u0, u1 = j / n, (j + 1) / n
                if jitter(j) :
                    c.line([(pts[0][0] + (pts[1][0] - pts[0][0]) * u0, pts[0][1] + (pts[1][1] - pts[0][1]) * u0),
                            (pts[0][0] + (pts[1][0] - pts[0][0]) * u1, pts[0][1] + (pts[1][1] - pts[0][1]) * u1)], col, w)


# ---------------------------------------------------------------- B129 印章
def b129_mirror(c, t, i):
    corner_tag(c, 'B129 · 盖下去，左右就翻过来了')
    c.text(60, 96, '印章面朝下压到纸上，印出来的是印面的镜像：想盖出正的「上」字，印面上就得刻成反的', 'serif', 38, INK)
    for k, (lab, mir) in enumerate((('印面刻成正字', False), ('印面刻成反字', True))):
        x0 = 260 + k * 860
        c.text(x0 + 300, 230, lab, 'bold', 28, INK, 'mm')
        c.rect(x0, 280, x0 + 240, 520, fill=STONE, r=12)
        _glyph(c, x0 + 40, 320, 160, SEAL, mirror=mir, w=22)
        c.text(x0 + 120, 560, '印面（朝上看）', 'sans', 20, MUTED, 'mm')
        a = min(1, max(0, (t - 6 - k * 2) / 3))
        c.arrow(x0 + 270, 400, x0 + 330, 400, MUTED, 3, 12)
        c.text(x0 + 300, 370, '翻过来盖', 'sans', 18, MUTED, 'mm')
        c.rect(x0 + 360, 280, x0 + 600, 520, fill=SHEET, r=6)
        if a > 0:
            _glyph(c, x0 + 400, 320, 160, mix(SHEET, SEAL, a), mirror=not mir, w=22)
        c.text(x0 + 480, 560, '纸上印出来的', 'sans', 20, MUTED, 'mm')
        if a >= 1:
            c.text(x0 + 480, 620, '反了' if not mir else '正了', 'bold', 30, NRED if not mir else GREEN, 'mm')
    c.text(960, 780, '对着镜子看自己写的字，看到的就是印面该刻的样子', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '印章是把印面朝下压到纸上：印面的左边，盖出来到了右边'),
                (7.2, 14, '所以在印面上刻正字，盖出来是反的；刻反字，盖出来才是正的'),
                (14.2, 22, '刻章的人先把字写在纸上，反过来贴到石头上照着刻：活字印刷的字模，也是反着刻的（示意）')], y=1010)


def b129_press(c, t, i):
    corner_tag(c, 'B129 · 轻了缺笔，重了糊边')
    c.text(60, 96, '同一个橡皮章：按得太轻，印泥沾不全，笔画断断续续；按得太重还晃，印泥被挤到边上，笔画发胖、重影', 'serif', 36, INK)
    rnd = random.Random(7)
    holes = [rnd.random() for _ in range(80)]
    a = min(1, t / 5)
    for k, (lab, mode) in enumerate((('轻按', 'light'), ('正常按', 'ok'), ('用力按还晃', 'heavy'))):
        x0 = 220 + k * 540
        c.rect(x0, 300, x0 + 380, 680, fill=SHEET, r=6)
        col = mix(SHEET, SEAL, a)
        if mode == 'light':
            _glyph(c, x0 + 50, 340, 280, col, w=26, jitter=lambda j, k=k: holes[(j * 3 + 1) % 80] > 0.45)
        elif mode == 'ok':
            _glyph(c, x0 + 50, 340, 280, col, w=26)
        else:
            _glyph(c, x0 + 58, 346, 280, mix(SHEET, SEAL, a * 0.5), w=40)
            _glyph(c, x0 + 50, 340, 280, col, w=34)
        c.text(x0 + 190, 730, lab, 'bold', 28, INK, 'mm')
    c.text(960, 820, '用力均匀、垂直按下、不要晃：印子最清楚（示意）', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '印泥只在印面凸起的地方沾上：按得太轻，有的地方没压实，就缺了笔'),
                (7.2, 14, '按得太重，橡皮被压扁，印泥被挤到笔画两边，笔画就变胖了'),
                (14.2, 22, '要是再一晃，就成了重影：力气要匀，压力要平均分到每一笔上（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十季特辑
OLD30 = [('陀螺', 'B50'), ('独轮车', 'B93'), ('搓麻绳', 'B101'), ('九连环', 'B55'), ('七巧板', 'B60'), ('鲁班锁', 'B99'),
         ('鼓', 'B108'), ('空竹', 'B87'), ('陶埙', 'B42'), ('三分损益', 'B107'), ('一钟双音', 'B11'), ('相风乌', 'B105'),
         ('油纸伞', 'B58'), ('剪纸', 'B98'), ('水准', 'B75'), ('高跷', 'B113'), ('榫卯', 'B7'), ('活字印刷', 'B3'),
         ('拓印', 'B77')]
NEW30 = [('滚铁环', 'B120', ['陀螺', '独轮车']), ('翻花绳', 'B121', ['搓麻绳', '九连环']), ('华容道', 'B122', ['七巧板', '鲁班锁']),
         ('拨浪鼓', 'B123', ['鼓', '空竹']), ('笛子', 'B124', ['陶埙', '三分损益']), ('风铃', 'B125', ['一钟双音', '相风乌']),
         ('折扇', 'B126', ['油纸伞', '剪纸']), ('谢公屐', 'B127', ['水准', '高跷']), ('簧片锁', 'B128', ['榫卯', '鲁班锁']),
         ('印章', 'B129', ['活字印刷', '拓印'])]


def s30_graph(c, t, i):
    corner_tag(c, '第三十季特辑 · 古法解密 12.0')
    c.text(60, 118, '玩、响、用：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD30):
        pos[name] = (340, 196 + k * 40)
    for k, (name, num, deps) in enumerate(NEW30):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW30):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD30:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW30):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十二季：玩、响、用'),
                (8.2, 16, '滚铁环越快越稳，翻花绳怎么翻都不打结，华容道有一半推不回去，拨浪鼓靠珠子慢半拍'),
                (16.2, 24, '笛子按孔截短空气柱，风铃长一倍音低两个八度，折扇的褶让纸变硬，谢公屐把坡垫平'),
                (24.2, 30, '簧片锁靠张开的弹片，印章要反着刻：都是讲得清的道理')], y=1040)


CLIPS = {
 'B129_镜像': (b129_mirror, 22), 'B129_力度': (b129_press, 22),
 'B129_片头': (titles.opening(BSER, VOL30, SB30, 9, '先秦已有玺印'), 7),
 'B129_片尾': (titles.closing(BSER, VOL30, SB30, 9, '下集：第三十季特辑 · 古法解密 12.0 回顾'), 7),
 'S30_依赖': (s30_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
