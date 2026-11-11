"""第四十一季（第十七层）第二批：E215 修正带、E216 自动铅笔、E217 荧光笔 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s41a import S41A, SER41, VOL41, STEEL, PAPERC, GLUE

FILM = (245, 245, 245)
TAPEB = (120, 160, 220)
LEAD = (70, 70, 80)
UV = (150, 90, 230)
FLUO = (220, 255, 60)
YEL = (220, 190, 60)


# ---------------------------------------------------------------- E215 修正带
def e215_transfer(c, t, i):
    corner_tag(c, '第 215 集 · 白膜被「转」到纸上')
    c.text(60, 96, '底带、白膜、胶，三层叠在一起：压在纸上一拉，白膜和纸粘得比和底带牢，就留在了纸上', 'serif', 36, INK)
    y = 600
    c.rect(100, y, 1820, y + 80, fill=mix(BG, PAPERC, 0.9))
    c.text(130, y + 40, '纸', 'sans', 22, INK, 'lm')
    p = min(1.0, t / 14)
    hx = 400 + p * 1000
    c.rect(400, y - 18, hx, y, fill=FILM)
    for k in range(3):
        c.text(500 + k * 300, y - 9, '错', 'bold', 18, mix(FILM, INK, 0.08), 'mm')
    c.poly([(hx - 60, y - 160), (hx + 60, y - 160), (hx + 20, y - 20), (hx - 20, y - 20)], mix(BG, TAPEB, 0.8))
    c.line([(hx - 20, y - 20), (hx - 200, y - 240)], TAPEB, 6)
    c.line([(hx + 20, y - 20), (hx + 200, y - 240)], mix(BG, FILM, 0.9), 10)
    c.rect(1380, 230, 1860, 470, fill=SHEET, r=12)
    c.text(1620, 270, '从上到下', 'bold', 24, INK, 'mm')
    c.rect(1440, 310, 1800, 330, fill=TAPEB)
    c.text(1620, 345, '底带（塑料，表面很滑）', 'sans', 18, MUTED, 'mm')
    c.rect(1440, 365, 1800, 385, fill=FILM)
    c.text(1620, 400, '白膜', 'sans', 18, MUTED, 'mm')
    c.rect(1440, 420, 1800, 432, fill=GLUE)
    c.text(1620, 450, '一层薄胶', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '修正带里卷着一条长长的塑料底带，上面是一层干的白膜，白膜背面有一层胶'),
                (7.2, 14, '带头压在纸上，胶抓住纸；底带表面很滑，白膜和它粘得不牢'),
                (14.2, 22, '一拉，白膜就离开底带、留在纸上，空了的底带被卷回去（示意）')], y=1010)


def e215_pressure(c, t, i):
    corner_tag(c, 'E215 · 换个表面就转不上去')
    c.text(60, 96, '胶要「抓」得住表面：打印纸粗糙多孔，抓得牢；光滑的塑料、保鲜膜抓不住，白膜就跟着带子走了', 'serif', 36, INK)
    for j, (lab, ok, col) in enumerate([('打印纸：转上去了', 1.0, PAPERC), ('塑料文件夹：断断续续', 0.5, (190, 210, 230)), ('保鲜膜：几乎转不上', 0.1, (220, 230, 235))]):
        cx, cy = 330 + j * 630, 520
        c.rect(cx - 260, cy - 60, cx + 260, cy + 60, fill=mix(BG, col, 0.9), r=6)
        p = min(1.0, t / 12)
        r = random.Random(j)
        x = cx - 220
        while x < cx - 220 + 440 * p:
            w = r.uniform(12, 40)
            if r.random() < ok:
                c.rect(x, cy - 14, x + w, cy + 14, fill=FILM)
            x += w
        c.text(cx, cy + 130, lab, 'bold', 24, GREEN if ok > 0.8 else NRED, 'mm')
    c.text(960, 800, '粗糙的表面让胶钻进小坑里，抓得更牢', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '同一卷修正带，在三种表面上各拉一段'),
                (7.2, 14, '纸面有无数纤维和小孔，胶贴上去抓得很牢'),
                (14.2, 22, '光滑的塑料和保鲜膜，胶抓不住，白膜宁可留在底带上（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E216 自动铅笔
def _pencil(c, cx, cy, push, chuck_open, lead_out):
    c.rect(cx - 520, cy - 50, cx + 260, cy + 50, fill=mix(BG, (90, 120, 170), 0.6), r=20)
    c.poly([(cx + 260, cy - 50), (cx + 380, cy - 12), (cx + 380, cy + 12), (cx + 260, cy + 50)], mix(BG, STEEL, 0.9))
    c.rect(cx - 560 - push, cy - 30, cx - 520, cy + 30, fill=mix(BG, (90, 120, 170), 0.9), r=8)
    jx = cx + 60 + push * 0.6
    op = 10 * chuck_open
    c.poly([(jx - 120, cy - 22 - op), (jx, cy - 14 - op), (jx, cy - 4), (jx - 120, cy - 8)], STEEL)
    c.poly([(jx - 120, cy + 22 + op), (jx, cy + 14 + op), (jx, cy + 4), (jx - 120, cy + 8)], STEEL)
    c.poly([(cx + 40, cy - 40), (cx + 120, cy - 40), (cx + 120, cy - 18), (cx + 40, cy - 30)], mix(BG, (160, 120, 80), 1.0))
    c.poly([(cx + 40, cy + 40), (cx + 120, cy + 40), (cx + 120, cy + 18), (cx + 40, cy + 30)], mix(BG, (160, 120, 80), 1.0))
    for k in range(6):
        x = cx - 480 + k * 22
        c.line([(x, cy - 30), (x + 11, cy + 30)], mix(BG, STEEL, 0.6), 3)
    c.rect(cx - 400, cy - 4, cx + 380 + lead_out, cy + 4, fill=LEAD)


def e216_chuck(c, t, i):
    corner_tag(c, '第 216 集 · 能张能合的小夹头')
    c.text(60, 96, '笔里有一个三瓣小夹头，外面套着锥形的套子：往前推，夹头出了套子就张开；弹簧拉回来，被套子一收就夹紧', 'serif', 33, INK)
    T = 4
    ph = (t % T) / T
    push = 60 * math.sin(math.pi * min(1, ph * 2)) if ph < 0.5 else 0
    open_ = 1.0 if push > 30 else 0.0
    _pencil(c, 900, 520, push, open_, 20 + 10 * int(t / T))
    c.text(900 + 60, 650, '夹头（三瓣）', 'sans', 22, MUTED, 'mm')
    c.text(900 + 80, 400, '锥形套', 'sans', 22, MUTED, 'mm')
    c.text(900 - 420, 400, '弹簧', 'sans', 22, MUTED, 'mm')
    c.text(900 - 600, 640, '按钮', 'sans', 22, MUTED, 'mm')
    c.rect(1380, 760, 1860, 900, fill=SHEET, r=12)
    c.text(1620, 830, '按下：夹头张开' if open_ else '松开：夹头夹紧', 'bold', 26, SPARK if open_ else GREEN, 'mm')
    caps(c, t, [(0, 7, '按下按钮，夹头带着铅芯往前走，冲出锥形套后自己张开'),
                (7.2, 14, '松手，弹簧把夹头往回拉，夹头被锥形套挤紧，又夹住了铅芯'),
                (14.2, 22, '前面还有一个小橡胶圈轻轻拦住铅芯，所以夹头张开时它也不会掉下去（示意）')], y=1010)


def e216_step(c, t, i):
    corner_tag(c, 'E216 · 按一下，走一小步')
    c.text(60, 96, '每按一下，铅芯只往前走固定的一小截：按得再重也一样，就像一步步走路', 'serif', 36, INK)
    n = min(10, int(t / 1.8))
    cx, cy = 900, 480
    _pencil(c, cx, cy, 0, 0, n * 9)
    x0, y0 = 300, 680
    c.line([(x0, y0), (x0 + 1300, y0)], MUTED, 2)
    for k in range(11):
        x = x0 + k * 120
        c.line([(x, y0 - 10), (x, y0 + 10)], MUTED, 2)
        c.text(x, y0 + 40, str(k), 'mono', 18, MUTED, 'mm')
    c.rect(x0, y0 - 60, x0 + max(2, n * 120), y0 - 30, fill=mix(BG, LEAD, 0.9))
    c.text(x0 + 650, y0 + 90, '按压次数', 'sans', 22, MUTED, 'mm')
    c.rect(1380, 760, 1860, 900, fill=SHEET, r=12)
    c.text(1620, 800, f'按了 {n} 下', 'bold', 26, INK, 'mm')
    c.text(1620, 855, f'铅芯出来约 {n * 0.5:.1f} 毫米（示意）', 'mono', 22, SPARK, 'mm')
    caps(c, t, [(0, 7, '夹头每次往前走的距离，由它冲出锥形套的那一小段决定'),
                (7.2, 14, '所以每按一下，铅芯都只前进差不多一样长：这叫「步进」'),
                (14.2, 22, '每下到底多长？用尺子量 10 下再除以 10（以实测为准）')], y=1010)


# ---------------------------------------------------------------- E217 荧光笔
def e217_glow(c, t, i):
    corner_tag(c, '第 217 集 · 把看不见的光变成看得见的光')
    c.text(60, 96, '普通颜料只反射一部分照来的光；荧光颜料还会吸收看不见的紫外光、蓝光，再放出黄绿光，所以比周围更亮', 'serif', 33, INK)
    for j, (lab, fl) in enumerate([('普通黄色：只反射', False), ('荧光黄：吸收紫外，放出黄绿', True)]):
        cx, cy = 520 + j * 880, 620
        c.rect(cx - 280, cy, cx + 280, cy + 80, fill=mix(BG, FLUO if fl else YEL, 0.95 if fl else 0.75), r=6)
        for k in range(3):
            x = cx - 200 + k * 200
            col = [UV, (90, 140, 240), (220, 200, 80)][k]
            lab2 = ['紫外（看不见）', '蓝光', '黄光'][k]
            ph = (t * 0.8 + k * 0.3) % 2
            yy = cy - 360 + min(1, ph) * 340
            c.line([(x - 60, cy - 360), (x - 60 + 60 * min(1, ph), yy)], col, 4)
            c.text(x - 60, cy - 390, lab2, 'sans', 18, col, 'mm')
            if ph > 1:
                u = ph - 1
                if k == 2 or fl:
                    oc = (220, 200, 80) if k == 2 else FLUO
                    c.line([(x, cy), (x + 80 * u, cy - 300 * u)], oc, 5 if (fl and k < 2) else 4)
                else:
                    c.ellipse(x, cy + 20, 10, 10, fill=mix(BG, col, 0.5))
        c.text(cx, cy + 150, lab, 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '光照到普通黄色上，只有黄光被反射回来，其他颜色被吃掉'),
                (7.2, 14, '荧光颜料不但反射黄光，还把吃进去的紫外光、蓝光变成黄绿光再放出来'),
                (14.2, 22, '回到眼睛里的黄绿光比照来的还多，看起来就像自己在发光（示意）')], y=1010)


def e217_uv(c, t, i):
    corner_tag(c, 'E217 · 紫外灯一照，亮得刺眼')
    c.text(60, 96, '关灯拉上窗帘，用紫外小手电照：普通黄笔几乎看不见，荧光笔那一道亮得发光；一关灯，马上就灭了', 'serif', 34, INK)
    st = 0 if t < 7 else (1 if t < 15 else 2)
    bg = [mix(BG, (240, 240, 235), 0.9), mix(BG, (40, 20, 60), 1.0), mix(BG, (10, 10, 12), 1.0)][st]
    c.rect(200, 240, 1720, 840, fill=bg, r=12)
    cols = [[(230, 200, 70), (225, 245, 70)], [(70, 60, 40), (240, 255, 90)], [(15, 15, 15), (15, 15, 15)]][st]
    for k, lab in enumerate(['普通黄色彩笔', '黄色荧光笔']):
        y = 420 + k * 220
        c.rect(400, y, 1520, y + 70, fill=cols[k], r=10)
        c.text(400, y - 40, lab, 'bold', 24, INK if st == 0 else MUTED, 'lm')
    if st == 1:
        c.poly([(1700, 260), (1760, 240), (1820, 300), (1760, 330)], (60, 60, 70))
        for k in range(5):
            c.line([(1700, 280), (500 + k * 240, 840)], mix(bg, UV, 0.35), 3)
    c.rect(200, 870, 1720, 930, fill=SHEET, r=8)
    c.text(960, 900, ['白天：两道都是黄色，荧光笔稍亮', '紫外灯下：荧光笔亮得发光', '关灯：都灭了（荧光不是夜光）'][st], 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '白天，两道黄色看起来差不多，荧光那道稍微亮一点'),
                (7.2, 14, '紫外灯下，只有荧光颜料能把紫外光变成可见光，亮得刺眼'),
                (14.2, 22, '关掉紫外灯，荧光马上灭；夜光表盘的磷光才会再亮一会儿（紫外灯不对着眼睛）')], y=1010)


CLIPS = {
 'E215_转印': (e215_transfer, 22), 'E215_表面': (e215_pressure, 22),
 'E215_片头': (titles.opening(SER41, VOL41, S41A, 3, '1980 年代日本推出修正带'), 7),
 'E215_片尾': (titles.closing(SER41, VOL41, S41A, 3, '下集：自动铅笔为什么一截截送出铅芯？'), 7),
 'E216_夹头': (e216_chuck, 22), 'E216_步进': (e216_step, 22),
 'E216_片头': (titles.opening(SER41, VOL41, S41A, 4, '20 世纪初出现按压式自动铅笔'), 7),
 'E216_片尾': (titles.closing(SER41, VOL41, S41A, 4, '下集：荧光笔为什么亮得像在发光？'), 7),
 'E217_荧光': (e217_glow, 22), 'E217_紫外': (e217_uv, 22),
 'E217_片头': (titles.opening(SER41, VOL41, S41A, 5, '20 世纪 60 年代荧光记号笔问世'), 7),
 'E217_片尾': (titles.closing(SER41, VOL41, S41A, 5, '下集：碎纸机的小电动机，为什么能咬碎纸？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
