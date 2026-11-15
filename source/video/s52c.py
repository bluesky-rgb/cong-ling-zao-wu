"""第五十二季（古法解密 23.0：驿路与车马）第三批：B236 车辖、B237 铁箍车轮、B238 车轫 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s52a import SB52, VOL52, EARTH, ROAD, BRONZE

WOODC = (170, 125, 80)
IRON = (150, 155, 165)
HOT = (235, 110, 60)
AXLE = (200, 170, 110)


def _wheel(c, cx, cy, r, ang, tyre=None, tyre_col=None):
    if tyre:
        c.ellipse(cx, cy, r + tyre, r + tyre, fill=tyre_col)
    c.ellipse(cx, cy, r, r, fill=mix(BG, WOODC, 1.0))
    c.ellipse(cx, cy, r - 24, r - 24, fill=BG)
    for k in range(10):
        a = ang + k * math.pi / 5
        c.line([(cx, cy), (cx + (r - 20) * math.cos(a), cy + (r - 20) * math.sin(a))], mix(BG, WOODC, 1.0), 8)
    c.ellipse(cx, cy, 30, 30, fill=mix(BG, WOODC, 0.8))


# ---------------------------------------------------------------- B236 车辖
def _axle_side(c, cx, cy, slide, pin):
    """侧剖：车轴横放，车轮（竖着的厚片）套在轴头。slide=车轮往外滑的距离。"""
    c.rect(cx - 600, cy - 22, cx + 260, cy + 22, fill=mix(BG, AXLE, 1.0), r=8)
    wx = cx + 60 + slide
    c.rect(wx - 40, cy - 240, wx + 40, cy + 240, fill=mix(BG, WOODC, 1.0), r=12)
    c.rect(wx - 60, cy - 50, wx + 60, cy + 50, fill=mix(BG, WOODC, 0.7), r=10)
    c.text(wx, cy - 270, '车轮', 'bold', 24, INK, 'mm')
    c.text(cx - 400, cy - 50, '车轴', 'bold', 24, INK, 'mm')
    if pin:
        c.rect(cx + 160, cy - 90, cx + 184, cy + 90, fill=mix(BG, BRONZE, 1.0), r=6)
        c.text(cx + 172, cy + 130, '辖', 'bold', 30, GREEN, 'mm')
    else:
        c.ellipse(cx + 172, cy, 10, 10, fill=BG)


def b236_slip(c, t, i):
    corner_tag(c, 'B236 · 颠一颠，车轮往外滑')
    c.text(60, 96, '车轮套在车轴头上，轴孔比车轴略大才能转；路上一颠一拐，车轮就会一点点往外滑，滑到头就脱出去', 'serif', 36, INK)
    s = 0 if t < 3 else min(380, (t - 3) ** 1.6 * 12)
    shake = 10 * math.sin(t * 9)
    _axle_side(c, 860, 560 + shake, s, False)
    if s >= 380:
        c.text(960, 880, '车轮脱了！（示意）', 'bold', 34, NRED, 'mm')
    caps(c, t, [(0, 7, '轴头上什么也没挡：车轮能转，也能左右滑'),
                (7.2, 14, '一路颠簸、拐弯，车轮一点点往外挪'),
                (14.2, 22, '挪到轴头，车轮就掉了（筷子线轴实验）')], y=1010)


def b236_pin(c, t, i):
    corner_tag(c, 'B236 · 插一根辖，能转不能滑')
    c.text(60, 96, '在轴头打一个孔，插进一根销子「辖」：车轮照样能转，往外滑却被它挡住；辖一拔，车轮就能卸下来', 'serif', 36, INK)
    shake = 10 * math.sin(t * 9)
    pulled = t > 14.2
    s = 0 if not pulled else min(380, (t - 15) ** 1.6 * 12) if t > 15 else 0
    if not pulled:
        s = 6 + 6 * math.sin(t * 9)
    _axle_side(c, 860, 560 + shake, s, not pulled)
    if not pulled:
        c.arc(920, 560 + shake, 140, 260, -60, 60, GREEN, 4)
        c.text(1300, 340, '能转', 'bold', 30, GREEN, 'mm')
        c.text(1300, 820, '滑不出去', 'bold', 30, GREEN, 'mm')
    else:
        c.text(1300, 820, '拔掉辖：车轮能卸下', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '轴头插上辖，车轮往外一碰就被挡住'),
                (7.2, 14, '车轮还是能自由地转'),
                (14.2, 22, '要换车轮，把辖拔下来就行：《诗经》说「载脂载舝」，舝就是辖（拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- B237 铁箍车轮
def b237_expand(c, t, i):
    corner_tag(c, 'B237 · 烧热了，铁箍胀大一点')
    c.text(60, 96, '冷的铁箍比木轮小一点，硬套套不上；烧热以后铁箍胀大一点，正好套上去（加热只用动画表示）', 'serif', 36, INK)
    cx, cy = 960, 540
    heat = min(1.0, max(0.0, (t - 3) / 6))
    rr = 240 + 30 * heat
    col = mix(mix(BG, IRON, 1.0), HOT, heat)
    u = 0 if t < 14.2 else min(1, (t - 14.2) / 4)
    wx = cx - 330 + 330 * u
    rx = cx + 330 - 330 * u
    _wheel(c, wx, cy, 230, 0)
    c.ellipse(rx, cy, rr, rr, outline=col, width=20)
    if t < 14.2:
        c.text(cx - 330, 860, '木轮', 'bold', 28, INK, 'mm')
        c.text(cx + 330, 860, '冷：铁箍内圈比木轮小' if heat < 0.3 else '热：胀大，比木轮大一圈', 'bold', 28, NRED if heat < 0.3 else GREEN, 'mm')
    else:
        c.text(cx, 860, '趁热套上去', 'bold', 30, GREEN, 'mm')
    c.text(1600, 300, '胀大多少：示意放大', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '铁箍做得比木轮小一圈'),
                (7.2, 14, '烧热以后，铁箍整个胀大一点'),
                (14.2, 22, '趁热把它套到木轮上（真实操作用火，本集只做动画）')], y=1010)


def b237_shrink(c, t, i):
    corner_tag(c, 'B237 · 凉下来，紧紧箍住')
    c.text(60, 96, '铁箍凉下来缩回去，把木轮紧紧箍住，辐条和轮圈挤得更结实；温水泡瓶盖，金属盖胀一点就好拧开了', 'serif', 36, INK)
    if t < 7.2:
        cx, cy = 600, 560
        cool = min(1.0, t / 6)
        col = mix(HOT, mix(BG, IRON, 1.0), cool)
        _wheel(c, cx, cy, 230, 0)
        c.ellipse(cx, cy, 270 - 20 * cool, 270 - 20 * cool, outline=col, width=20)
        for k in range(8):
            a = k * math.pi / 4
            r1, r2 = 330, 280
            c.arrow(cx + r1 * math.cos(a), cy + r1 * math.sin(a), cx + r2 * math.cos(a), cy + r2 * math.sin(a), GREEN, 4, 12)
        c.text(cx + 520, cy, '凉了收缩：往里箍紧', 'bold', 30, GREEN, 'mm')
    else:
        cx, cy = 960, 560
        c.rect(cx - 160, cy - 100, cx + 160, cy + 260, fill=mix(BG, (200, 220, 230), 0.4), r=30)
        warm = t > 14.2
        c.rect(cx - 120, cy - 150, cx + 120, cy - 100, fill=mix(BG, IRON, 1.0), r=8)
        if warm:
            c.rect(cx - 220, cy - 190, cx + 220, cy - 80, outline=mix(BG, (120, 170, 230), 1.0), width=6, r=12)
            c.text(cx + 380, cy - 135, '50 ℃ 温水泡 1 分钟', 'bold', 26, INK, 'lm')
            c.text(cx, 900, '金属盖胀大一点，好拧开了（以实测为准）', 'bold', 28, GREEN, 'mm')
        else:
            c.text(cx, 900, '拧紧的金属盖：很难拧开', 'bold', 28, NRED, 'mm')
    caps(c, t, [(0, 7, '铁箍冷却收缩，把轮圈和辐条紧紧箍在一起'),
                (7.2, 14, '家里也能看到热胀冷缩：一个拧得很紧的金属瓶盖'),
                (14.2, 22, '瓶盖泡在不超过 50 ℃ 的温水里一会儿，就好拧开了')], y=1010)


# ---------------------------------------------------------------- B238 车轫
def _slope(c, deg):
    a = math.radians(deg)
    x0, y0 = 260, 880
    L = 1400
    x1, y1 = x0 + L * math.cos(a), y0 - L * math.sin(a)
    c.poly([(x0, y0), (x1, y1), (x1, y0)], mix(BG, ROAD, 0.8))
    return (x0, y0), a


def b238_roll(c, t, i):
    corner_tag(c, 'B238 · 坡上的车会溜')
    c.text(60, 96, '马卸下来以后，停在坡上的车没人拉着，车轮一转就顺着坡往下溜', 'serif', 36, INK)
    (x0, y0), a = _slope(c, 14)
    s = 1000 - min(800, (t ** 2) * 4)
    r = 70
    px, py = x0 + s * math.cos(a), y0 - s * math.sin(a)
    cx, cy = px - r * math.sin(a), py - r * math.cos(a)
    _wheel(c, cx, cy, r, -s / r)
    c.rect(cx - 10, cy - 150, cx + 220, cy - 80, fill=mix(BG, WOODC, 0.7), r=6)
    c.text(960, 220, '没有挡块：车往下溜（示意）', 'bold', 30, NRED, 'mm')
    caps(c, t, [(0, 7, '车停在坡上，马卸下来了'),
                (7.2, 14, '重力拉着车往下，车轮一转，车就溜起来'),
                (14.2, 22, '越溜越快，很危险（玩具车实验）')], y=1010)


def b238_chock(c, t, i):
    corner_tag(c, 'B238 · 楔形木块，越压越紧')
    c.text(60, 96, '在车轮下坡的一侧塞一块楔形木头「轫」：车往下压，木头被压得更紧，车就停住；出发时撤掉，叫「发轫」', 'serif', 36, INK)
    (x0, y0), a = _slope(c, 14)
    r = 70
    s = 700
    px, py = x0 + s * math.cos(a), y0 - s * math.sin(a)
    cx, cy = px - r * math.sin(a), py - r * math.cos(a)
    go = t > 14.2
    roll = 0 if not go else min(500, ((t - 15) ** 2) * 6) if t > 15 else 0
    if go:
        s2 = s - roll
        px2, py2 = x0 + s2 * math.cos(a), y0 - s2 * math.sin(a)
        cx, cy = px2 - r * math.sin(a), py2 - r * math.cos(a)
    _wheel(c, cx, cy, r, -roll / r)
    c.rect(cx - 10, cy - 150, cx + 220, cy - 80, fill=mix(BG, WOODC, 0.7), r=6)
    # 楔子：在轮子下坡一侧（左下）
    wx, wy = x0 + (s - 60) * math.cos(a), y0 - (s - 60) * math.sin(a)
    if not go:
        c.poly([(wx - 50, wy + 12), (wx + 22, wy - 6), (wx - 50, wy - 48)], mix(BG, (120, 80, 50), 1.0))
        c.arrow(cx, cy - 10, cx - 50, cy + 30, GREEN, 5, 14)
        c.text(cx - 260, cy - 150, '轫：越压越紧', 'bold', 28, GREEN, 'mm')
    else:
        c.text(960, 220, '撤掉轫，车就能走了：「发轫」（示意）', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '在车轮朝下坡的那一边，塞一块楔形的木头'),
                (7.2, 14, '车往下压，楔子被压进轮子和地面之间，卡得更紧'),
                (14.2, 22, '要出发时把它撤掉，所以开始一件事叫「发轫」')], y=1010)


CLIPS = {
 'B236_滑脱': (b236_slip, 22), 'B236_插辖': (b236_pin, 22),
 'B236_片头': (titles.opening(BSER, VOL52, SB52, 6, '商周车马坑出土过青铜车辖'), 7),
 'B236_片尾': (titles.closing(BSER, VOL52, SB52, 6, '下集：铁箍为什么要烧热了再套？'), 7),
 'B237_胀大': (b237_expand, 22), 'B237_箍紧': (b237_shrink, 22),
 'B237_片头': (titles.opening(BSER, VOL52, SB52, 7, '古代木车轮外圈常包铁箍'), 7),
 'B237_片尾': (titles.closing(BSER, VOL52, SB52, 7, '下集：一块木头怎么挡住一辆车？'), 7),
 'B238_溜坡': (b238_roll, 22), 'B238_楔挡': (b238_chock, 22),
 'B238_片头': (titles.opening(BSER, VOL52, SB52, 8, '停车挡轮的木头叫「轫」'), 7),
 'B238_片尾': (titles.closing(BSER, VOL52, SB52, 8, '下集：拄一根竹杖，为什么走得稳？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
