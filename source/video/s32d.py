"""第三十二季（古法解密 13.0：天、凉、数、用）收官：B139 腰舟 + 第三十二季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s26a import WOOD, WATER, WATER_L, BAMBOO
from s32a import SB32, VOL32

GOURD = (210, 180, 90)
BAG = (220, 220, 210)


# ---------------------------------------------------------------- B139 腰舟
def b139_float(c, t, i):
    corner_tag(c, 'B139 · 绑上几个空瓶，1 千克的米袋浮起来了')
    c.text(60, 96, '1 千克的米袋放进水里就沉底；每绑一个拧紧的空瓶，就多排开一瓶水，多一份向上的托力，够了就浮起来', 'serif', 38, INK)
    n = min(3, int(t / 5.5))
    wx0, wx1, wy = 360, 1300, 420
    c.rect(wx0, wy, wx1, 900, fill=mix(BG, WATER, 0.35), r=12)
    c.rect(wx0 - 10, 300, wx0, 900, fill=LINE)
    c.rect(wx1, 300, wx1 + 10, 900, fill=LINE)
    bag_vol = 0.75
    buoy = bag_vol + n * 0.5
    floats = buoy > 1.0
    by = 820 if not floats else wy + 40 - 10 * (buoy - 1)
    by = by + 6 * math.sin(t * 2) * floats
    c.rect(780, by - 70, 920, by + 50, fill=BAG, r=16)
    c.text(850, by - 10, '米 1 千克', 'bold', 22, (40, 40, 40), 'mm')
    for k in range(n):
        bx = 700 - k * 80 if k < 2 else 1000
        c.rect(bx - 30, by - 110, bx + 30, by + 20, fill=mix(BG, (200, 230, 250), 0.6), r=12)
        c.rect(bx - 12, by - 130, bx + 12, by - 110, fill=(80, 120, 200))
    c.rect(1400, 300, 1860, 640, fill=SHEET, r=14)
    c.text(1630, 340, f'绑了 {n} 个 500 毫升空瓶', 'bold', 24, INK, 'mm')
    c.text(1630, 420, f'最多排开约 {buoy * 1000:.0f} 毫升水', 'mono', 24, SPARK, 'mm')
    c.text(1630, 480, f'向上托力最多约 {buoy:.2f} 千克', 'mono', 24, SPARK, 'mm')
    c.text(1630, 560, '浮起来了' if floats else '还沉着', 'bold', 34, GREEN if floats else NRED, 'mm')
    c.text(1630, 610, '（米袋体积按约 750 毫升估，示意）', 'sans', 16, MUTED, 'mm')
    caps(c, t, [(0, 7, '一袋 1 千克的米装进密封袋放进水盆：直接沉底'),
                (7.2, 14, '绑上一个空瓶，还是沉；再绑一个，米袋开始往上浮'),
                (14.2, 22, '能排开的水比自己重，就浮得起来：古人过河拴几个空葫芦，就是这个道理（以实测为准）')], y=1010)


def b139_push(c, t, i):
    corner_tag(c, 'B139 · 往下按得越深，托得越用力')
    c.text(60, 96, '把一个空瓶往水里按：按下去越多，排开的水越多，水往上托的力就越大——这股力正好等于排开那些水的重量', 'serif', 36, INK)
    d = 0.5 - 0.5 * math.cos(t / 11 * math.pi) if t < 11 else 1.0 - 0.0
    d = min(1, d)
    cx, wy = 760, 520
    c.rect(400, wy, 1120, 900, fill=mix(BG, WATER, 0.35), r=12)
    rise = 40 * d
    c.rect(400, wy - rise, 1120, wy, fill=mix(BG, WATER, 0.35))
    H = 260
    top = wy - rise - H + H * d
    c.rect(cx - 60, top, cx + 60, top + H, fill=mix(BG, (200, 230, 250), 0.6), r=14)
    c.rect(cx - 20, top - 30, cx + 20, top, fill=(80, 120, 200))
    c.ellipse(cx, top - 70, 40, 30, fill=(225, 180, 150))
    c.arrow(cx + 120, top + H, cx + 120, top + H - 220 * d - 10, SPARK, 6, 20)
    c.text(cx + 150, top + H - 110 * d, f'托力约 {500 * d:.0f} 克力', 'bold', 26, SPARK, 'lm')
    c.text(400, wy - rise - 30, '水面跟着升高（示意）', 'sans', 20, MUTED, 'lm')
    c.rect(1300, 320, 1840, 620, fill=SHEET, r=14)
    c.text(1570, 370, '阿基米德原理', 'bold', 26, INK, 'mm')
    c.text(1570, 450, '浮力 = 排开的水的重量', 'bold', 26, SPARK, 'mm')
    c.text(1570, 530, '500 毫升全按下去 ≈ 托起 500 克', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '拿一个拧紧的空瓶，慢慢往水里按，手越来越吃力'),
                (7.2, 14, '按下去的部分越多，水面升得越高，被挤开的水越多'),
                (14.2, 22, '水往上托的力，就等于被挤开那些水的重量：曹冲称象用的也是排开的水（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十二季特辑
OLD32 = [('日晷', 'B63'), ('用影子测地球', '47'), ('竹编', 'B73'), ('温度计', '46'), ('冰鉴与藏冰', 'B12'), ('腌菜', 'B48'),
         ('蒸发冷却罐', '38'), ('算盘', 'B54'), ('数字与 0', '48'), ('搓麻绳', 'B101'), ('杠杆与滑轮组', '39'), ('筷子', 'B53'),
         ('瓷器', 'B16'), ('屋檐举折', 'B67'), ('相风乌', 'B105'), ('竹蜻蜓', 'B40'), ('羊皮筏子', 'B82'), ('曹冲称象', 'B74')]
NEW32 = [('圭表', 'B130', ['日晷', '用影子测地球']), ('凉席', 'B131', ['竹编', '温度计']), ('竹夫人', 'B132', ['凉席', '冰鉴与藏冰']),
         ('晒秋', 'B133', ['腌菜', '蒸发冷却罐']), ('算筹', 'B134', ['算盘', '数字与 0']), ('结绳记事', 'B135', ['搓麻绳', '算筹']),
         ('剪刀', 'B136', ['杠杆与滑轮组', '筷子']), ('瓦片', 'B137', ['瓷器', '屋檐举折']), ('纸风车', 'B138', ['相风乌', '竹蜻蜓']),
         ('腰舟', 'B139', ['羊皮筏子', '曹冲称象'])]


def s32_graph(c, t, i):
    corner_tag(c, '第三十二季特辑 · 古法解密 13.0')
    c.text(60, 118, '天、凉、数、用：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD32):
        pos[name] = (340, 210 + k * 43)
    for k, (name, num, deps) in enumerate(NEW32):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十二季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW32):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if x0 > 900:
                sx = x0 - 110
                pts = [(sx - 60 * math.sin(math.pi * j / 20), y0 + (y1 - y0) * j / 20) for j in range(21)]
            else:
                sx, ex = x0 + 110, x1 - 110
                pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD32:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=FIELD if num.startswith('B') else COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 6 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW32):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第十三季：天、凉、数、用'),
                (8.2, 16, '日晷长出圭表，竹编长出凉席和竹夫人，腌菜长出晒秋，算盘长出算筹，算筹又长出结绳记事'),
                (16.2, 24, '杠杆和筷子长出剪刀，瓷器和举折长出瓦片，竹蜻蜓长出纸风车'),
                (24.2, 30, '最后，羊皮筏子和曹冲称象一起，长出了拴着空葫芦过河的腰舟')], y=1040)


CLIPS = {
 'B139_浮起': (b139_float, 22), 'B139_按瓶': (b139_push, 22),
 'B139_片头': (titles.opening(BSER, VOL32, SB32, 9, '先秦以葫芦为腰舟'), 7),
 'B139_片尾': (titles.closing(BSER, VOL32, SB32, 9, '下集：第三十二季特辑 · 古法解密 13.0 回顾'), 7),
 'S32_依赖': (s32_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
