"""第三十九季（第十六层：运动场）收官：E211 蹦床 + 第三十九季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import WATER_L
from s39a import S39A, SER39, VOL39, SKIN

NET = (60, 60, 70)
SPRING = (170, 175, 185)


# ---------------------------------------------------------------- E211 蹦床
def e211_elastic(c, t, i):
    corner_tag(c, '第 211 集 · 网面把能量存起来再还回去')
    c.text(60, 96, '人落下来，把网面和一圈弹簧拉长，速度变成弹性势能；网面弹回去，再把能量还给人', 'serif', 36, INK)
    cx, gy = 760, 700
    W = 520
    T = 3.0
    ph = (t % T) / T
    h = 380 * (2 * abs(ph - 0.5)) ** 2
    dip = 0
    if h < 20:
        dip = 110 * (1 - h / 20)
    y = gy - h + dip
    pts = [(cx - W, gy), (cx, gy + dip), (cx + W, gy)]
    c.line([(cx - W - 60, gy - 10), (cx - W, gy)], SPRING, 6)
    c.line([(cx + W, gy), (cx + W + 60, gy - 10)], SPRING, 6)
    c.line(pts, NET, 8)
    c.line([(cx - W - 60, gy - 10), (cx - W - 60, gy + 220)], MUTED, 8)
    c.line([(cx + W + 60, gy - 10), (cx + W + 60, gy + 220)], MUTED, 8)
    c.ellipse(cx, y - 120, 30, 30, fill=SKIN)
    c.line([(cx, y - 90), (cx, y)], SKIN, 16)
    c.rect(1420, 260, 1860, 640, fill=SHEET, r=12)
    c.text(1640, 300, '能量在哪里', 'bold', 26, INK, 'mm')
    ke = 1 - h / 380 if dip == 0 else (1 - dip / 110)
    pe = h / 380
    ee = dip / 110
    for k, (lab, v, col) in enumerate([('高度', pe, (120, 170, 230)), ('速度', max(0, ke - ee * 0), SPARK), ('网面弹性', ee, GREEN)]):
        yy = 370 + k * 85
        c.text(1450, yy, lab, 'sans', 22, INK, 'lm')
        c.rect(1580, yy - 16, 1580 + 240 * min(1, v), yy + 16, fill=col, r=6)
    caps(c, t, [(0, 7, '人从高处落下，高度变成速度'),
                (7.2, 14, '踩到网面，网面和弹簧被拉长，人慢下来，能量存进了网面'),
                (14.2, 22, '网面弹回去，把人送回空中：能量在高度、速度和弹性之间来回倒（示意）')], y=1010)


def e211_pump(c, t, i):
    corner_tag(c, 'E211 · 在最低点蹬一下，越弹越高')
    c.text(60, 96, '不用力时，每弹一次都损失一点，越弹越低；每次在最低点再蹬一下，补进的能量比损失的多，就越弹越高', 'serif', 34, INK)
    x0, y0, W, H = 200, 260, 1500, 560
    c.rect(x0, y0, x0 + W, y0 + H, fill=SHEET, r=12)
    c.text(x0 + W / 2, y0 + H + 40, '时间（示意）', 'sans', 20, MUTED, 'mm')
    c.text(x0 + 20, y0 + 30, '高度', 'sans', 20, MUTED, 'lm')
    tn = min(1.0, t / 16)
    for col, grow, lab in [(NRED, 0.85, '不用力：越弹越低'), (GREEN, 1.12, '最低点蹬一下：越弹越高')]:
        pts = []
        h = 0.45
        for k in range(8):
            for q in range(21):
                s = (k + q / 20) / 8
                if s > tn:
                    break
                yy = h * 4 * (q / 20) * (1 - q / 20)
                pts.append((x0 + 30 + s * (W - 60), y0 + H - 30 - yy * (H - 80)))
            h = min(0.95, h * grow)
        if len(pts) > 1:
            c.line(pts, col, 4)
    c.text(x0 + 40, y0 + H + 90, '红线：不用力，越弹越低', 'bold', 22, NRED, 'lm')
    c.text(x0 + 700, y0 + H + 90, '绿线：每次最低点蹬一下，越弹越高', 'bold', 22, GREEN, 'lm')
    caps(c, t, [(0, 7, '空气阻力和网面发热，每弹一次都吃掉一点能量'),
                (7.2, 14, '在网面压到最低、正要弹回的那一刻蹬腿，给它补进能量'),
                (14.2, 22, '时机对了，补得比丢得多，就越弹越高：荡秋千也是这个道理（只在有护网的蹦床上玩）')], y=1040)


# ---------------------------------------------------------------- 第三十九季特辑
OLD39 = [('橡胶轮胎', '143'), ('复合材料', '150'), ('自行车', '66'), ('齿轮与轴承', '41'), ('安全带', '173'), ('安全气囊', '174'),
         ('机翼', '86'), ('螺旋桨', '177'), ('杠杆与滑轮组', '39'), ('悬索桥', '79'), ('塑料', '142'), ('潜水艇', '178'),
         ('光控路灯', '168'), ('摆钟', '45'), ('数码相机', '95'), ('卫星定位', '90')]
NEW39 = [('跑鞋缓震', '202', ['橡胶轮胎', '复合材料']), ('自行车变速', '203', ['自行车', '齿轮与轴承']), ('头盔', '204', ['安全带', '安全气囊']),
         ('弧线球', '205', ['机翼', '螺旋桨']), ('撑竿跳', '206', ['复合材料', '杠杆与滑轮组']), ('动力绳', '207', ['悬索桥', '安全气囊']),
         ('泳衣', '208', ['塑料', '潜水艇']), ('电子计时', '209', ['光控路灯', '摆钟']), ('鹰眼', '210', ['数码相机', '卫星定位']),
         ('蹦床', '211', ['橡胶轮胎', '摆钟'])]


def s39_layer(c, t, i):
    corner_tag(c, '第三十九季特辑 · 第十六层')
    c.text(60, 118, '第十六层：运动场', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD39):
        pos[name] = (340, 215 + k * 42)
    for k, (name, num, deps) in enumerate(NEW39):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 168, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第三十九季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW39):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD39:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW39):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十六层的十集：运动场上的机器和装备'),
                (8.2, 16, '橡胶和复合材料长出跑鞋缓震，自行车长出变速，安全气囊长出头盔，机翼长出弧线球'),
                (16.2, 24, '复合材料长出撑竿跳，悬索桥长出动力绳，潜水艇长出泳衣，摆钟长出电子计时，卫星定位长出鹰眼'),
                (24.2, 30, '最后，橡胶和摆钟一起，长出了越跳越高的蹦床')], y=1040)


CLIPS = {
 'E211_弹性': (e211_elastic, 22), 'E211_越弹越高': (e211_pump, 22),
 'E211_片头': (titles.opening(SER39, VOL39, S39A, 9, '20 世纪 30 年代现代蹦床被发明'), 7),
 'E211_片尾': (titles.closing(SER39, VOL39, S39A, 9, '下集：第三十九季特辑 · 第十六层回顾'), 7),
 'S39_第十六层': (s39_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
