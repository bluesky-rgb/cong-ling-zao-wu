"""第三十五季（第十四层：看与听的机器）第二批：E185 防窥膜、E186 光盘、E187 夜光表盘 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s35a import S35A, SER35, VOL35, LIGHT, SCREEN, CUP

GLOW = (150, 240, 170)
BLUE_L = (110, 150, 255)
RED_L = (240, 90, 80)


def _spec(f):
    cols = [(150, 80, 220), (70, 110, 240), (60, 200, 220), (90, 210, 90), (240, 220, 60), (245, 150, 50), (230, 60, 50)]
    f = max(0, min(0.999, f)) * (len(cols) - 1)
    k = int(f)
    return mix(cols[k], cols[k + 1], f - k)


# ---------------------------------------------------------------- E185 防窥膜
def e185_louvers(c, t, i):
    corner_tag(c, '第 185 集 · 正着的光穿过，斜着的被挡住')
    c.text(60, 96, '放大防窥膜的剖面：屏幕上方立着一排极细的黑色百叶，光只能从缝里差不多竖直地射出来', 'serif', 36, INK)
    y0, y1 = 760, 640
    c.rect(200, y0, 1720, y0 + 60, fill=mix(BG, LIGHT, 0.85), r=6)
    c.text(960, y0 + 100, '手机屏（每一点都往各个方向发光）', 'sans', 22, MUTED, 'mm')
    gap, H = 80, 120
    for k in range(20):
        x = 240 + k * gap
        c.rect(x - 4, y0 - H, x + 4, y0, fill=(95, 95, 105))
    src = 240 + 9 * gap + gap / 2
    maxang = math.degrees(math.atan(gap / H))
    for k, ang in enumerate([-60, -45, -30, -15, 0, 15, 30, 45, 60]):
        a = math.radians(ang)
        ok = abs(ang) < maxang * 0.5 + 1
        L = 520 if ok else (H / math.cos(a) * (gap / 2) / (H * abs(math.tan(a))) if ang else 0)
        if not ok:
            L = min((gap / 2) / abs(math.sin(a)), 300)
        p = min(1.0, (t - k * 0.4) / 3) if t > k * 0.4 else 0
        ex, ey = src + L * math.sin(a) * p, y0 - L * math.cos(a) * p
        c.line([(src, y0), (ex, ey)], LIGHT if ok else mix(BG, LIGHT, 0.5), 3)
        if not ok and p >= 1:
            c.ellipse(ex, ey, 7, 7, fill=NRED)
    c.ellipse(src, 200 + 40, 70, 40, fill=SHEET, outline=INK, width=3)
    c.ellipse(src, 240, 20, 20, fill=INK)
    c.text(src, 310, '你：正着看', 'bold', 22, GREEN, 'mm')
    c.ellipse(1560, 280, 70, 40, fill=SHEET, outline=MUTED, width=3)
    c.text(1560, 350, '旁边的人：光到不了', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '屏幕上的每一点，都往四面八方发光'),
                (7.2, 14, '防窥膜里有一排极细的黑色百叶：竖着的光从缝里钻出去，斜着的光撞在百叶上'),
                (14.2, 22, '所以正着看清清楚楚，歪着看的人那边，光根本过不去（示意）')], y=1010)


def e185_angle(c, t, i):
    corner_tag(c, '第 185 集 · 百叶越高，能看清的角度越窄')
    c.text(60, 96, '同样的缝宽，百叶从 1 厘米加高到 2 厘米：光能斜着钻出去的角度变小，旁人更难看见', 'serif', 36, INK)
    p = min(1.0, t / 12)
    for j, (H, lab) in enumerate([(60, '百叶 1 厘米'), (120, '百叶 2 厘米')]):
        cx = 520 + j * 880
        y0 = 760
        gap = 50
        for k in range(-4, 5):
            x = cx + k * gap
            c.rect(x - 4, y0 - H, x + 4, y0, fill=(95, 95, 105))
        c.rect(cx - 260, y0, cx + 260, y0 + 30, fill=mix(BG, LIGHT, 0.85))
        ang = math.degrees(math.atan(gap / H))
        sx = cx + gap / 2
        for s in (-1, 1):
            a = math.radians(ang * s * p)
            c.line([(sx - gap / 2 * (s + 1) / 2 * 0 , y0), (sx + 420 * math.sin(a), y0 - 420 * math.cos(a))], mix(BG, LIGHT, 0.6), 2)
        pts = [(sx, y0)] + [(sx + 380 * math.sin(math.radians(a_)), y0 - 380 * math.cos(math.radians(a_))) for a_ in [x * p for x in range(int(-ang), int(ang) + 1, 2)]]
        if len(pts) > 2:
            c.poly(pts, mix(BG, LIGHT, 0.25))
        c.text(cx, 840, lab, 'bold', 28, INK, 'mm')
        c.text(cx, 880, f'约 ±{ang * p:.0f}° 内看得见（示意）', 'mono', 22, SPARK, 'mm')
    c.text(960, 940, '以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '缝宽不变，只把百叶加高一倍'),
                (7.2, 14, '光要斜着穿过更深的「走廊」，能钻出去的角度就小了'),
                (14.2, 22, '能看清的范围更窄，旁边的人更看不见，可自己的屏幕也会暗一点（示意）')], y=1010)


# ---------------------------------------------------------------- E186 光盘
def e186_grating(c, t, i):
    corner_tag(c, '第 186 集 · 很密的细沟把白光按颜色分开')
    c.text(60, 96, '光盘上一圈圈细沟间距只有头发丝的几十分之一：每条沟反射的光叠在一起，不同颜色往不同方向加强', 'serif', 34, INK)
    gy = 820
    for k in range(40):
        x = 160 + k * 18
        c.rect(x, gy, x + 10, gy + 20, fill=mix(BG, (190, 200, 210), 0.9))
    c.text(520, gy + 60, '光盘表面（放大）', 'sans', 22, MUTED, 'mm')
    c.arrow(200, 260, 470, gy - 10, LIGHT, 5, 16)
    c.text(200, 230, '白光', 'bold', 24, LIGHT, 'mm')
    ox, oy = 520, gy - 10
    p = min(1.0, t / 10)
    c.line([(ox, oy), (ox + 360 * p, oy - 560 * p)], mix(BG, LIGHT, 0.9), 4)
    for k in range(30):
        f = k / 29
        ang = math.radians(22 + 24 * f)
        L = 900 * p
        c.line([(ox, oy), (ox + L * math.sin(ang + 0.55), oy - L * math.cos(ang + 0.55))], mix(BG, _spec(f), 0.85), 4)
    c.text(ox + 360 * p + 20, oy - 560 * p, '白点（直接反射）', 'sans', 22, MUTED, 'lm')
    if p >= 1:
        c.text(1560, 420, '红光拐得最多', 'bold', 22, RED_L, 'mm')
        c.text(1260, 240, '紫光拐得最少', 'bold', 22, (150, 80, 220), 'mm')
    caps(c, t, [(0, 7, '光盘上有一圈圈极密的细沟，用来记录 0 和 1'),
                (7.2, 14, '白光照上去，每条沟都反射一点光，这些光在某些方向上步调一致，互相加强'),
                (14.2, 22, '加强的方向和颜色有关：红光拐得多，紫光拐得少，于是铺成一道彩虹（示意）')], y=1010)


def e186_cddvd(c, t, i):
    corner_tag(c, '第 186 集 · 沟越密，颜色分得越开')
    c.text(60, 96, 'CD 的细沟间距约 1.6 微米，DVD 约 0.74 微米：沟更密，彩虹离中心白点更远、拉得更开', 'serif', 36, INK)
    p = min(1.0, t / 12)
    for j, (lab, d) in enumerate([('CD', 1.6), ('DVD', 0.74)]):
        y = 380 + j * 300
        c.rect(120, y - 110, 1800, y + 110, fill=SHEET, r=14)
        c.text(200, y - 70, lab, 'bold', 32, INK, 'mm')
        cx = 300
        c.ellipse(cx, y + 10, 16, 16, fill=LIGHT)
        c.text(cx, y + 60, '中心白点', 'sans', 20, MUTED, 'mm')
        for k in range(120):
            lam = 0.40 + 0.30 * k / 119
            s = lam / d
            if s >= 1: continue
            th = math.degrees(math.asin(s))
            x = cx + 1300 * th / 70 * p
            c.rect(x - 5, y - 20, x + 5, y + 40, fill=_spec(k / 119))
        th_r = math.degrees(math.asin(0.65 / d))
        c.text(1700, y + 70, f'红光约 {th_r:.0f}°', 'mono', 22, SPARK, 'rm')
    c.text(960, 960, '示意，以实测为准；激光笔只由成年人使用，绝不对着眼睛', 'sans', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '手电筒和光盘不动，把 CD 换成 DVD'),
                (7.2, 14, 'DVD 的细沟密了一倍多，每种颜色都拐得更厉害'),
                (14.2, 22, '彩虹离中心白点更远，颜色也分得更开：沟越密，分光越强（示意）')], y=1010)


# ---------------------------------------------------------------- E187 夜光表盘
def e187_store(c, t, i):
    corner_tag(c, '第 187 集 · 吸了光，再慢慢放出来')
    c.text(60, 96, '夜光材料里，电子被光「踢」到高处掉进小坑；关灯后一个个爬出来落回去，每落一次发一点光', 'serif', 34, INK)
    on = t < 7
    c.rect(100, 200, 700, 300, fill=mix(BG, LIGHT, 0.9) if on else mix(BG, SCREEN, 0.6), r=10)
    c.text(400, 250, '灯开着：充光' if on else '关灯：慢慢放光', 'bold', 26, INK if on else GLOW, 'mm')
    lv0, lv1, lv2 = 820, 380, 500
    c.line([(800, lv0), (1700, lv0)], MUTED, 4)
    c.text(780, lv0, '低处', 'sans', 22, MUTED, 'rm')
    c.line([(800, lv1), (1700, lv1)], MUTED, 4)
    c.text(780, lv1, '高处', 'sans', 22, MUTED, 'rm')
    for k in range(6):
        x = 880 + k * 140
        c.rect(x - 40, lv2, x + 40, lv2 + 20, fill=mix(BG, SPARK, 0.4), r=4)
    c.text(780, lv2 + 10, '小坑', 'sans', 22, SPARK, 'rm')
    r = random.Random(3)
    for k in range(6):
        x = 880 + k * 140
        if on:
            ph = (t * 0.9 + k * 0.17) % 1
            y = lv0 - (lv0 - lv1) * min(1, ph * 2) if ph < 0.5 else lv1 + (lv2 - lv1) * (ph - 0.5) * 2
            c.ellipse(x, y, 14, 14, fill=BLUE_L)
            if ph < 0.15:
                c.arrow(x - 70, lv0 - 120, x - 10, lv0 - 30, LIGHT, 3, 10)
        else:
            rel = 7 + k * 2.4 + r.uniform(0, 1)
            if t < rel:
                c.ellipse(x, lv2 - 12, 14, 14, fill=BLUE_L)
            elif t < rel + 1.2:
                f = (t - rel) / 1.2
                c.ellipse(x, lv2 - 12 + (lv0 - lv2) * f, 14, 14, fill=BLUE_L)
                c.ellipse(x + 40, lv0 - 60, 20 * (1 - f) + 6, 20 * (1 - f) + 6, fill=mix(BG, GLOW, 1 - f))
            else:
                c.ellipse(x, lv0 - 12, 14, 14, fill=mix(BG, BLUE_L, 0.5))
    caps(c, t, [(0, 7, '灯开着：光把材料里的电子一个个「踢」到高处，很多掉进旁边的小坑里卡住'),
                (7.2, 14, '关了灯：坑里的电子靠一点点热，过一会儿爬出一个，落回低处，发出一点绿光'),
                (14.2, 22, '一个接一个地爬出来，光就一点点放出来，能亮好几十分钟（示意）')], y=1010)


def e187_colors(c, t, i):
    corner_tag(c, '第 187 集 · 蓝光充得快，红光充不进去')
    c.text(60, 96, '要把电子「踢」上高处，光的每一份能量得够大：蓝光每份能量大，红光每份能量小，踢不上去', 'serif', 36, INK)
    lv0, lv1 = 800, 420
    for j, (lab, col, en) in enumerate([('隔红色糖纸', RED_L, 0.55), ('隔蓝色糖纸', BLUE_L, 1.2)]):
        cx = 520 + j * 880
        c.line([(cx - 260, lv0), (cx + 260, lv0)], MUTED, 4)
        c.line([(cx - 260, lv1), (cx + 260, lv1)], MUTED, 4)
        c.text(cx, 230, lab, 'bold', 30, col, 'mm')
        ph = (t * 0.8) % 1.6
        h = (lv0 - lv1) * min(en, 1.0) * min(1, ph * 1.6) if ph < 1 else 0
        y = lv0 - 12 - (h if en >= 1 else (math.sin(min(1, ph) * math.pi) * (lv0 - lv1) * en))
        c.ellipse(cx, y, 16, 16, fill=col)
        for k in range(3):
            xx = cx - 240 + ((t * 200 + k * 80) % 160)
            c.line([(xx + q * 4, 300 + 14 * math.sin(q * (1.2 if en > 1 else 0.6))) for q in range(30)], col, 3)
        c.text(cx, 880, '踢上去了：能充光' if en >= 1 else '只能跳一半，又落回来', 'bold', 24, GREEN if en >= 1 else NRED, 'mm')
    c.text(960, 940, '所以夜光贴纸在阳光或白光下充得快；闪光灯不对着眼睛，不用紫外灯', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '同样亮的光，隔着红色糖纸和蓝色糖纸照夜光贴纸'),
                (7.2, 14, '红光一份一份的能量太小，电子跳不到高处，又落回来'),
                (14.2, 22, '蓝光每份能量够大，一下就把电子送上去：蓝光充得快，红光几乎充不进（示意）')], y=1010)


CLIPS = {
 'E185_百叶': (e185_louvers, 22), 'E185_视角': (e185_angle, 22),
 'E185_片头': (titles.opening(SER35, VOL35, S35A, 3, '20 世纪 60 年代已有控光膜'), 7),
 'E185_片尾': (titles.closing(SER35, VOL35, S35A, 3, '下集：光盘对着灯一转，为什么有一道道彩虹？'), 7),
 'E186_细沟': (e186_grating, 22), 'E186_两种盘': (e186_cddvd, 22),
 'E186_片头': (titles.opening(SER35, VOL35, S35A, 4, '1982 年 CD 上市'), 7),
 'E186_片尾': (titles.closing(SER35, VOL35, S35A, 4, '下集：夜光贴纸关了灯还亮，光是怎么存起来的？'), 7),
 'E187_存光': (e187_store, 22), 'E187_颜色': (e187_colors, 22),
 'E187_片头': (titles.opening(SER35, VOL35, S35A, 5, '1993 年长余辉夜光粉问世'), 7),
 'E187_片尾': (titles.closing(SER35, VOL35, S35A, 5, '下集：耳机不塞进耳朵，为什么也能听见？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
