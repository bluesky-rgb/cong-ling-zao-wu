"""第四十三季（第十八层：工具箱）收官：E231 吸盘 + 第四十三季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s43a import S43A, SER43, VOL43, STEEL

CUP = (90, 170, 220)
TILE = (225, 225, 220)
AIR = (150, 200, 240)


def _cup(c, cx, wy, flat, col=CUP):
    # 吸盘贴在竖直墙面 x=wy 右侧；flat 0..1 越大越扁
    d = 120 - 80 * flat
    c.poly([(wy, cx - 150), (wy + d, cx - 40), (wy + d, cx + 40), (wy, cx + 150)], mix(BG, col, 0.9))
    c.rect(wy + d, cx - 18, wy + d + 160, cx + 18, fill=mix(BG, col, 1.0), r=8)


# ---------------------------------------------------------------- E231 吸盘
def e231_press(c, t, i):
    corner_tag(c, '第 231 集 · 不是吸，是被压住')
    c.text(60, 96, '按下吸盘，里面的空气被挤出去；松手后橡胶想弹回原形，里面的空间变大、空气变稀，外面的大气压就把它紧紧压在墙上', 'serif', 33, INK)
    wx = 520
    c.rect(wx - 80, 220, wx, 900, fill=mix(BG, TILE, 0.9))
    c.text(wx - 40, 250, '瓷砖', 'sans', 20, BG, 'mm')
    cy = 560
    T = 12
    ph = min(1.0, t / 8)
    flat = 1.0 if ph < 0.5 else 1 - 0.6 * (ph - 0.5) / 0.5
    _cup(c, cy, wx, flat)
    inside = 0.15 if ph > 0.3 else 1 - ph / 0.3 * 0.85
    r = random.Random(int(t * 4))
    for k in range(int(30 * inside)):
        c.ellipse(wx + r.uniform(8, 30), cy + r.uniform(-110, 110), 4, 4, fill=AIR)
    for k in range(60):
        x = r.uniform(wx + 200, 1800)
        y = r.uniform(240, 880)
        c.ellipse(x, y, 4, 4, fill=mix(BG, AIR, 0.7))
    if ph > 0.5:
        for y in (cy - 120, cy - 75, cy + 75, cy + 120):
            c.arrow(wx + 330, y, wx + 150 - 60 * (abs(y - cy) - 75) / 45, y, SPARK, 6, 18)
        c.text(wx + 600, cy - 220, '外面的大气压往墙上压', 'bold', 28, SPARK, 'lm')
        c.text(wx + 600, cy - 170, '里面空气稀，往外推得少', 'sans', 24, MUTED, 'lm')
    elif ph < 0.3:
        c.text(wx + 600, cy - 220, '按下：把里面的空气挤出去', 'bold', 28, INK, 'lm')
    caps(c, t, [(0, 7, '把吸盘按在瓷砖上，碗里的空气被挤了出去'),
                (7.2, 14, '一松手，橡胶想弹回去，碗里的空间变大，剩下的空气变得很稀'),
                (14.2, 22, '里外一推一压不平衡：是外面的大气压把吸盘「按」在墙上的（示意）')], y=1010)


def e231_leak(c, t, i):
    corner_tag(c, '第 231 集 · 有缝就漏气')
    c.text(60, 96, '吸盘要贴在光滑、没有缝的表面上：粗糙的墙面坑坑洼洼，空气从小缝里钻进去，里外的压力差一下就没了，吸盘就掉了', 'serif', 33, INK)
    for j, (lab, rough) in enumerate([('光滑瓷砖：边缘贴严，空气进不去', False), ('粗糙墙面：空气从缝里钻进去', True)]):
        ox = 140 + j * 900
        wx = ox + 160
        cy = 520
        if rough:
            pts = [(wx - 80, 220)]
            r = random.Random(2)
            for k in range(40):
                y = 220 + k * 17
                pts.append((wx + r.uniform(-14, 8), y))
            pts.append((wx - 80, 900))
            c.poly(pts, mix(BG, (160, 150, 140), 1.0))
        else:
            c.rect(wx - 80, 220, wx, 900, fill=mix(BG, TILE, 0.9))
        fall = 0
        if rough and t > 12:
            fall = min(1.0, (t - 12) / 3)
        _cup(c, cy + 0, wx + 160 * fall, 0.6 if not fall else 0.0)
        if rough:
            for k in range(int(min(12, t * 1.2))):
                y = cy - 140 + (k * 23) % 280
                c.arrow(wx - 4, y, wx + 30, y, AIR, 3, 10)
        c.text(ox + 400, 820, lab, 'bold', 26, NRED if rough else GREEN, 'mm')
    caps(c, t, [(0, 7, '在瓷砖、玻璃上，吸盘的边紧紧贴住，空气进不去，能挂好久'),
                (7.2, 14, '在粗糙的墙上，边缘下面全是小缝，外面的空气一点点钻进去'),
                (14.2, 22, '里外压力一样了，吸盘就掉下来：边缘抹点水能帮它封住缝（以实测为准）')], y=1010)


OLD43 = [('钢', '62'), ('回形针', '213'), ('电子秤', '160'), ('杠杆与滑轮组', '39'), ('螺丝与标准件', '64'), ('齿轮与轴承', '41'),
         ('自动铅笔', '216'), ('订书机', '212'), ('液压刹车', '172'), ('电磁铁', '56'), ('电生磁', '03'), ('伏打电堆', '02'),
         ('电表', '164'), ('玻璃', '21'), ('复合材料', '150'), ('塑料', '142'), ('真空包装', '195')]
NEW43 = [('卷尺', '222', ['钢', '回形针']), ('弹簧秤', '223', ['钢', '电子秤']), ('扳手', '224', ['杠杆与滑轮组', '螺丝与标准件']),
         ('棘轮', '225', ['齿轮与轴承', '自动铅笔']), ('老虎钳', '226', ['杠杆与滑轮组', '订书机']), ('千斤顶', '227', ['螺丝与标准件', '液压刹车']),
         ('磁性螺丝刀', '228', ['电磁铁', '电生磁']), ('万用表', '229', ['伏打电堆', '电表']), ('砂纸', '230', ['玻璃', '复合材料']),
         ('吸盘', '231', ['塑料', '真空包装'])]


def s43_layer(c, t, i):
    corner_tag(c, '第四十三季特辑 · 第十八层')
    c.text(60, 118, '第十八层：工具箱', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD43):
        pos[name] = (340, 215 + k * 42)
    for k, (name, num, deps) in enumerate(NEW43):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 168, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十三季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW43):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD43:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW43):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十八层的十集：家里工具箱里的东西'),
                (8.2, 16, '钢和回形针长出卷尺，电子秤长出弹簧秤，杠杆和螺丝长出扳手，齿轮和自动铅笔长出棘轮'),
                (16.2, 24, '订书机长出老虎钳，液压刹车长出千斤顶，电磁铁长出磁性螺丝刀，伏打电堆和电表长出万用表'),
                (24.2, 30, '玻璃和复合材料长出砂纸；最后，塑料和真空包装一起，长出了吸盘')], y=1040)


CLIPS = {
 'E231_气压': (e231_press, 22), 'E231_漏气': (e231_leak, 22),
 'E231_片头': (titles.opening(SER43, VOL43, S43A, 9, '19 世纪末出现橡胶吸盘'), 7),
 'E231_片尾': (titles.closing(SER43, VOL43, S43A, 9, '下集：第四十三季特辑 · 第十八层回顾'), 7),
 'S43_第十八层': (s43_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
