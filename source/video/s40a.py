"""第四十季（古法解密 17.0：水上与手边）第一批：B170 茶壶、B171 筷子提米、B172 刻舟求剑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, STRAW

SB40 = [('B170', '茶壶'), ('B171', '筷子提米'), ('B172', '刻舟求剑'), ('B173', '马镫'), ('B174', '竹筏'),
        ('B175', '拉纤'), ('B176', '渔网'), ('B177', '鱼篓'), ('B178', '锯子'), ('B179', '拓片')]
VOL40 = '第四十季 · 古法解密 17.0'
AIR = (170, 200, 235)
CLAYPOT = (170, 110, 80)
RICE = (240, 235, 215)
TEA = (190, 140, 70)


# ---------------------------------------------------------------- B170 茶壶
def _pot(c, cx, cy, fill, tilt=0.0):
    c.ellipse(cx, cy, 200, 150, fill=mix(BG, CLAYPOT, 0.95))
    c.rect(cx - 60, cy - 190, cx + 60, cy - 150, fill=mix(BG, CLAYPOT, 1.0), r=12)
    c.poly([(cx + 180, cy - 10), (cx + 330, cy - 120), (cx + 345, cy - 105), (cx + 200, cy + 40)], mix(BG, CLAYPOT, 0.95))
    lv = cy + 120 - 240 * fill
    if fill > 0.02:
        c.rect(cx - 170, lv, cx + 170, cy + 120, fill=mix(BG, TEA, 0.8), r=40)


def b170_vent(c, t, i):
    corner_tag(c, 'B170 · 水出去，空气要进来')
    c.text(60, 96, '壶嘴往外倒一口水，壶里就空出一口的地方：盖上有孔，空气从孔里补进去；孔被堵住，外面的大气就把水「按」在壶里', 'serif', 33, INK)
    for j, (lab, open_) in enumerate([('盖孔堵住：倒一下停一下', False), ('盖孔开着：一直顺顺地流', True)]):
        cx, cy = 480 + j * 900, 560
        T = 6
        ph = (t % T) / T
        fill = 0.8 - 0.5 * ph if open_ else 0.8 - 0.2 * ph
        _pot(c, cx, cy, fill)
        c.ellipse(cx, cy - 195, 10, 6, fill=BG if open_ else NRED)
        if open_:
            for k in range(3):
                y = cy - 260 + ((t * 120 + k * 30) % 90)
                c.arrow(cx, y - 30, cx, y, AIR, 4, 12)
            for k in range(6):
                y = cy - 110 + k * 40 + (t * 200) % 40
                c.ellipse(cx + 345 + (k * 6), y, 8, 10, fill=mix(BG, TEA, 0.9))
        else:
            gl = (t * 2) % 1 < 0.35
            if gl:
                for k in range(3):
                    c.ellipse(cx + 345 + k * 4, cy - 100 + k * 30, 8, 10, fill=mix(BG, TEA, 0.9))
            else:
                c.ellipse(cx + 330, cy - 120, 14, 14, fill=mix(BG, AIR, 0.9))
                c.text(cx + 380, cy - 150, '咕嘟', 'bold', 22, MUTED, 'lm')
        c.text(cx, 900, lab, 'bold', 26, GREEN if open_ else NRED, 'mm')
    caps(c, t, [(0, 7, '水从壶嘴流出去，壶里的空气就被拉得越来越稀'),
                (7.2, 14, '盖孔堵住时，外面的空气只能从壶嘴挤进去，水一顿一顿、咕嘟咕嘟'),
                (14.2, 22, '盖上留个小孔，空气从上面补进去，壶里外气压一样，水就顺了（示意）')], y=1010)


def b170_pour(c, t, i):
    corner_tag(c, 'B170 · 堵住盖孔，侧孔就不漏')
    c.text(60, 96, '瓶身下面扎一个小孔，装满水拧紧盖：堵住盖上的孔，侧孔一滴不漏；手指一松，水马上喷出来', 'serif', 36, INK)
    cx, top, bot = 700, 240, 880
    c.rect(cx - 160, top + 60, cx + 160, bot, fill=mix(BG, WATER_L, 0.25), outline=mix(BG, WATER_L, 0.9), width=4, r=30)
    c.rect(cx - 60, top, cx + 60, top + 70, fill=mix(BG, (90, 140, 200), 0.9), r=8)
    blocked = (t % 10) < 5
    lv = top + 100 + (0 if blocked else ((t % 10) - 5) * 30)
    c.rect(cx - 156, lv, cx + 156, bot - 4, fill=mix(BG, WATER, 0.8), r=26)
    if blocked:
        c.ellipse(cx, top - 10, 40, 26, fill=mix(BG, (220, 170, 130), 1.0))
        c.text(cx + 80, top - 20, '手指堵住', 'sans', 22, MUTED, 'lm')
    else:
        for k in range(3):
            y = top - 60 + ((t * 120 + k * 30) % 70)
            c.arrow(cx, y, cx, y + 30, AIR, 4, 12)
        pts = [(cx + 160 + s * 300, bot - 80 + 300 * (s / 1.0) ** 2) for s in [k / 12 * 0.7 for k in range(13)]]
        c.line(pts, mix(BG, WATER, 1.0), 10)
    c.rect(1240, 300, 1840, 600, fill=SHEET, r=12)
    c.text(1540, 350, '为什么不漏？', 'bold', 26, INK, 'mm')
    c.text(1540, 420, '水想流出去，瓶里就要变「空」', 'sans', 22, INK, 'mm')
    c.text(1540, 470, '外面的大气压比那点水重得多', 'sans', 22, INK, 'mm')
    c.text(1540, 520, '把水按在瓶子里', 'sans', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '堵住盖孔，瓶里的空气没法补进来，侧孔的水就停住了'),
                (7.2, 14, '大气压大约相当于 10 米高的水柱，这一瓶水根本推不动它'),
                (14.2, 22, '一松手指，空气从上面进来，水马上从侧孔喷出（以实测为准）')], y=1010)


# ---------------------------------------------------------------- B171 筷子提米
def b171_pack(c, t, i):
    corner_tag(c, 'B171 · 米粒压紧了，挤成一团')
    c.text(60, 96, '松松的米粒之间全是空隙，一推就滑开；一遍遍压实以后，粒粒都被四周挤住，谁也动不了', 'serif', 36, INK)
    p = min(1.0, t / 14)
    for j, (lab, dense) in enumerate([('松散：空隙多，一推就滑', 0.0), ('压实：挤得紧紧的', 1.0)]):
        cx, cy = 520 + j * 880, 560
        c.poly([(cx - 220, 260), (cx + 220, 260), (cx + 180, 860), (cx - 180, 860)], mix(BG, (210, 220, 230), 0.25))
        r = random.Random(8)
        sp = 34 - 10 * dense * p
        n = 0
        y = 840
        while y > 300 and n < 3000:
            w = 180 + (y - 260) / 600 * -40 + 40
            x = cx - w + r.uniform(0, 12)
            while x < cx + w:
                ang = r.uniform(0, math.pi)
                c.ellipse(x, y, 14, 8, fill=mix(BG, RICE, 1.0))
                x += sp * (1.0 + r.uniform(-0.1, 0.2) * (1 - dense * p))
                n += 1
            y -= sp * 0.62
        c.rect(cx - 10, 160, cx + 10, 820, fill=mix(BG, WOOD, 1.0), r=6)
        if dense > 0:
            for k in range(8):
                yy = 380 + k * 55
                c.arrow(cx - 70, yy, cx - 16, yy, SPARK, 3, 10)
                c.arrow(cx + 70, yy, cx + 16, yy, SPARK, 3, 10)
        c.text(cx, 920, lab, 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '刚倒进去的米，粒和粒之间有很多空隙'),
                (7.2, 14, '用手指一遍遍往下压、再加满，空隙被挤掉，米粒互相卡死'),
                (14.2, 22, '这时插进筷子，四周的米粒都紧紧压在筷子上（示意）')], y=1010)


def b171_lift(c, t, i):
    corner_tag(c, 'B171 · 摩擦力托起整杯米')
    c.text(60, 96, '筷子往上提，每一粒贴着它的米都用摩擦力拽住它；米粒又互相拽着，加起来比整杯米加杯子还重', 'serif', 36, INK)
    cx, base = 760, 860
    lift = max(0, min(1, (t - 6) / 4)) * 80
    cy = base - lift
    c.poly([(cx - 200, cy - 400), (cx + 200, cy - 400), (cx + 160, cy), (cx - 160, cy)], mix(BG, (210, 220, 230), 0.35))
    c.poly([(cx - 192, cy - 370), (cx + 192, cy - 370), (cx + 158, cy - 6), (cx - 158, cy - 6)], mix(BG, RICE, 0.85))
    c.rect(cx - 10, cy - 500, cx + 10, cy - 30, fill=mix(BG, WOOD, 1.0), r=6)
    c.ellipse(cx, cy - 520, 46, 30, fill=mix(BG, (220, 170, 130), 1.0))
    for k in range(8):
        yy = cy - 340 + k * 40
        c.arrow(cx + 40, yy + 10, cx + 16, yy - 10, SPARK, 3, 10)
        c.arrow(cx - 40, yy + 10, cx - 16, yy - 10, SPARK, 3, 10)
    c.arrow(cx + 300, cy - 200, cx + 300, cy - 60, NRED, 6, 18)
    c.text(cx + 330, cy - 130, '米 + 杯子的重量', 'sans', 22, NRED, 'lm')
    c.text(cx + 330, cy - 380, '橙色：米粒对筷子的摩擦（往上）', 'sans', 22, SPARK, 'lm')
    c.rect(0, base, 1920, base + 12, fill=mix(BG, (150, 120, 90), 0.6))
    caps(c, t, [(0, 7, '提筷子时，筷子想往上走，米粒拽着它不让走：这就是摩擦力'),
                (7.2, 14, '压得越紧，米粒压在筷子上的力越大，摩擦力也越大'),
                (14.2, 22, '摩擦力加起来比整杯米还重，杯子就被一起提了起来（米不食用）')], y=1010)


# ---------------------------------------------------------------- B172 刻舟求剑
def _boat(c, x, y):
    c.poly([(x - 220, y), (x + 220, y), (x + 170, y + 70), (x - 170, y + 70)], mix(BG, WOOD, 0.95))
    c.rect(x - 4, y - 160, x + 4, y, fill=mix(BG, WOOD, 1.0))


def b172_mark(c, t, i):
    corner_tag(c, 'B172 · 记号跟着船走了')
    c.text(60, 96, '剑掉下去，留在江底原地；船一直往前划，船边的记号也跟着往前走：等船停下，记号下面早就没有剑了', 'serif', 34, INK)
    wy = 480
    c.rect(0, wy, 1920, 960, fill=mix(BG, WATER, 0.4))
    c.rect(0, 930, 1920, 960, fill=mix(BG, (140, 120, 90), 0.8))
    sx = 500
    p = max(0, min(1, (t - 4) / 12))
    bx = sx + p * 900
    _boat(c, bx, wy - 50)
    c.rect(bx + 120, wy - 40, bx + 136, wy + 10, fill=NRED)
    c.text(bx + 128, wy - 70, '刻痕', 'bold', 22, NRED, 'mm')
    drop = min(1, max(0, (t - 1) / 3))
    swx = sx + 128
    swy = wy - 20 + drop * (900 - wy)
    c.rect(swx - 6, swy - 60, swx + 6, swy, fill=mix(BG, (200, 205, 215), 1.0))
    c.rect(swx - 20, swy - 70, swx + 20, swy - 60, fill=mix(BG, (160, 130, 60), 1.0))
    if p > 0.05:
        c.line([(bx + 128, wy + 10), (bx + 128, 920)], mix(BG, NRED, 0.6), 2)
        c.text(bx + 140, 880, '他在这里找', 'sans', 22, NRED, 'lm')
        c.text(swx + 20, 870, '剑在这里', 'sans', 22, GREEN, 'lm')
    caps(c, t, [(0, 7, '船在江上走，剑「扑通」一声掉进水里，沉到江底'),
                (7.2, 14, '他在剑落下的船边刻了个记号，船继续往前划'),
                (14.2, 22, '船停了，他从记号处下水去找：记号跟着船走了，剑还在原来的地方')], y=1010)


def b172_ref(c, t, i):
    corner_tag(c, 'B172 · 位置要看相对于谁')
    c.text(60, 96, '「剑在哪里」的答案，取决于拿谁当参照物：对船来说，剑在往后退；对岸上的树来说，剑一动不动', 'serif', 36, INK)
    wy = 520
    c.rect(0, 300, 1920, wy - 60, fill=mix(BG, (110, 150, 90), 0.4))
    c.rect(0, wy - 60, 1920, 960, fill=mix(BG, WATER, 0.35))
    tree = 520
    c.ellipse(tree, 280, 70, 90, fill=mix(BG, GREEN, 0.8))
    c.rect(tree - 10, 330, tree + 10, wy - 60, fill=mix(BG, WOOD, 1.0))
    c.text(tree, 170, '岸边的树', 'bold', 24, INK, 'mm')
    p = (t % 12) / 12
    bx = 380 + p * 1200
    _boat(c, bx, wy)
    c.rect(bx + 120, wy + 10, bx + 136, wy + 60, fill=NRED)
    c.line([(tree, 380), (tree, 900)], mix(BG, GREEN, 0.7), 3)
    c.rect(tree - 8, 880, tree + 8, 920, fill=mix(BG, (200, 205, 215), 1.0))
    c.rect(1320, 650, 1880, 920, fill=SHEET, r=12)
    c.text(1600, 700, '用船当参照物：', 'bold', 22, INK, 'mm')
    c.text(1600, 745, f'剑在船后 {p * 12:.1f} 米（一直在变）', 'mono', 22, NRED, 'mm')
    c.text(1600, 815, '用岸上的树当参照物：', 'bold', 22, INK, 'mm')
    c.text(1600, 860, '剑就在树的正前方（不变）', 'mono', 22, GREEN, 'mm')
    caps(c, t, [(0, 7, '同一把剑，站在船上看，它一直在往后退'),
                (7.2, 14, '站在岸边看，它一直待在树的正前方，一动没动'),
                (14.2, 22, '要找回东西，得选一个不跟着你动的参照物：岸边的树、江边的石头')], y=1010)


CLIPS = {
 'B170_气孔': (b170_vent, 22), 'B170_倒水': (b170_pour, 22),
 'B170_片头': (titles.opening(BSER, VOL40, SB40, 0, '宋代起茶壶壶盖普遍留有小气孔'), 7),
 'B170_片尾': (titles.closing(BSER, VOL40, SB40, 0, '下集：一根筷子，怎么提起一整杯米？'), 7),
 'B171_压实': (b171_pack, 22), 'B171_提起': (b171_lift, 22),
 'B171_片头': (titles.opening(BSER, VOL40, SB40, 1, '民间游戏「筷子提米」流传已久'), 7),
 'B171_片尾': (titles.closing(BSER, VOL40, SB40, 1, '下集：照着船上的记号，为什么找不回剑？'), 7),
 'B172_记号': (b172_mark, 22), 'B172_参照物': (b172_ref, 22),
 'B172_片头': (titles.opening(BSER, VOL40, SB40, 2, '《吕氏春秋》记载「刻舟求剑」'), 7),
 'B172_片尾': (titles.closing(BSER, VOL40, SB40, 2, '下集：有了马镫，人为什么就坐稳了？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
