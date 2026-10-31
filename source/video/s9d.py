"""第九季收尾：B29 交子防伪、第九季特辑（古法解密 2.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s9a import SB9, VOL9, WATER

PAPERC = (205, 190, 160)
BLACKI = (40, 36, 34)
REDI = (190, 50, 40)

def note(c, x0, y0, w, h, a_black, a_red, dx=0, dy=0, fine=True):
    """A fictional two-colour printed slip (not any real currency)."""
    c.rect(x0, y0, x0 + w, y0 + h, fill=PAPERC, r=6)
    ink = mix(PAPERC, BLACKI, a_black)
    if a_black > 0:
        n = 9 if fine else 4
        for k in range(n):
            o = 14 + k * (5 if fine else 9)
            c.rect(x0 + o, y0 + o, x0 + w - o, y0 + h - o, outline=ink, width=1 if fine else 3, r=4)
        # simple house-and-tree motif
        cx, cy = x0 + w / 2, y0 + h * 0.42
        c.poly([(cx - 70, cy), (cx, cy - 60), (cx + 70, cy)], ink)
        c.rect(cx - 55, cy, cx + 55, cy + 70, outline=ink, width=3)
        c.rect(cx - 15, cy + 25, cx + 15, cy + 70, fill=ink)
        c.ellipse(cx + 110, cy + 10, 28, 34, fill=ink)
        c.rect(cx + 106, cy + 40, cx + 114, cy + 70, fill=ink)
        c.text(cx, y0 + h * 0.72, '示意券 · 非真实票据', 'serif', 22, ink, 'mm')
        # registration cross (black)
        for (px, py) in [(x0 + 36, y0 + h - 36), (x0 + w - 36, y0 + 36)]:
            c.line([(px - 14, py), (px + 14, py)], ink, 2); c.line([(px, py - 14), (px, py + 14)], ink, 2)
    if a_red > 0:
        red = mix(PAPERC, REDI, a_red)
        sx, sy = x0 + w - 110 + dx, y0 + h - 130 + dy
        c.rect(sx, sy, sx + 74, sy + 74, outline=red, width=4, r=4)
        c.text(sx + 37, sy + 37, '押', 'serif', 40, red, 'mm')
        for k in range(3):
            c.rect(x0 + 50 + dx + k * 34, y0 + 60 + dy, x0 + 70 + dx + k * 34, y0 + 120 + dy, fill=red, r=3)
        for (px, py) in [(x0 + 36 + dx, y0 + h - 36 + dy), (x0 + w - 36 + dx, y0 + 36 + dy)]:
            c.line([(px - 10, py - 10), (px + 10, py + 10)], red, 2); c.line([(px - 10, py + 10), (px + 10, py - 10)], red, 2)

def zoom_cross(c, x, y, dx, dy, label, ok):
    c.ellipse(x, y, 90, 90, fill=PAPERC, outline=GREEN if ok else NRED, width=4)
    c.line([(x - 50, y), (x + 50, y)], BLACKI, 5); c.line([(x, y - 50), (x, y + 50)], BLACKI, 5)
    k = 3
    c.line([(x - 36 + dx * k, y - 36 + dy * k), (x + 36 + dx * k, y + 36 + dy * k)], REDI, 5)
    c.line([(x - 36 + dx * k, y + 36 + dy * k), (x + 36 + dx * k, y - 36 + dy * k)], REDI, 5)
    c.text(x, y + 120, label, 'bold', 24, GREEN if ok else NRED, 'mm')

# ---------------------------------------------------------------- B29 交子防伪
def b29_register(c, t, i):
    corner_tag(c, 'B29 · 朱墨间错')
    c.text(60, 96, '两块版、两种颜色：仿的人要同时仿准两块', 'serif', 40, INK)
    W, H = 420, 600
    ab = fade(t, 0.5, 3)
    ar = fade(t, 4, 6.5)
    note(c, 260, 250, W, H, ab, ar)
    c.text(260 + W / 2, 215, '真券：黑版 + 红版，十字对齐', 'bold', 26, INK, 'mm')
    f = fade(t, 8, 10)
    if f > 0:
        note(c, 1240, 250, W, H, ab * f, ar * f, dx=12, dy=-8, fine=False)
        c.text(1240 + W / 2, 215, '仿券：线条粗、红版偏了', 'bold', 26, mix(BG, NRED, f), 'mm')
    z = fade(t, 11, 12.5)
    if z > 0:
        zoom_cross(c, 860, 400, 0, 0, '真券放大：对齐', True)
        zoom_cross(c, 860, 740, 12 / 3 * z, -8 / 3 * z, '仿券放大：错开', False)
    caps(c, t, [(0, 7.5, '交子用两块版套印：先印黑色的花纹和字，再印红色的印记，史书叫「朱墨间错」（拍摄前核对）'),
                (7.7, 14, '仿造的人要同时刻准两块版，还要印得严丝合缝；差一毫米，放大就看出来'),
                (14.2, 22, '花纹越细、颜色越多，仿起来越难：今天的纸币也是这样做的（这里画的是示意券）')], y=1010)

def b29_secret(c, t, i):
    corner_tag(c, 'B29 · 暗记与存根')
    c.text(60, 96, '看得见的花纹之外，还有看不见的记号', 'serif', 40, INK)
    marks = [('铺户押字', '每家各自的花押'), ('隐密题号', '只有发行者知道的编号规则'), ('同一色纸', '专门的纸张')]
    for k, (name, desc) in enumerate(marks):
        a = fade(t, 0.5 + k * 1.5, 1.5 + k * 1.5)
        y = 230 + k * 110
        c.rect(80, y - 40, 820, y + 40, fill=mix(BG, SHEET, a), r=10)
        c.text(110, y, name, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(340, y, desc, 'sans', 24, mix(BG, MUTED, a), 'lm')
    b = fade(t, 6, 7)
    c.text(80, 620, '如果每种记号有 10 种可能，仿造者只能猜：', 'sans', 26, mix(BG, INK, b), 'lm')
    terms = ['1/10', '× 1/10', '× 1/10', '= 1/1000']
    for k, s in enumerate(terms):
        d = fade(t, 7.5 + k * 1.2, 8.3 + k * 1.2)
        c.text(80 + k * 190, 700, s, 'mono', 44, mix(BG, GREEN if k == 3 else INK, d), 'lm')
    e = fade(t, 12.5, 13.5)
    c.text(80, 790, '三个记号全猜对，只有千分之一的机会', 'bold', 28, mix(BG, GREEN, e), 'lm')
    # ledger on the right
    lx = 1060
    g = fade(t, 13, 14)
    c.rect(lx, 190, 1840, 880, fill=mix(BG, SHEET, g), r=12)
    c.text(lx + 30, 230, '交子务的存根（示意）', 'bold', 28, mix(BG, INK, g), 'lm')
    rows = [('0126', True), ('0127', True), ('0131', True), ('0127', False), ('0315', False)]
    for k, (num, ok) in enumerate(rows):
        h = fade(t, 14.5 + k * 1.2, 15.3 + k * 1.2)
        y = 310 + k * 100
        c.text(lx + 40, y, f'来兑换的券：第 {num} 号', 'sans', 26, mix(BG, INK, h), 'lm')
        if ok:
            c.text(lx + 740, y, '存根有，对上', 'bold', 26, mix(BG, GREEN, h), 'rm')
        else:
            why = '重号：已兑过' if num == '0127' else '存根里没有'
            c.text(lx + 740, y, why, 'bold', 26, mix(BG, NRED, h), 'rm')
    caps(c, t, [(0, 6, '记载里，交子印好后各家铺户还要押字、加上只有自己知道的暗号（拍摄前核对）'),
                (6.2, 13, '每多一种暗记，仿造者猜对的机会就再乘一个小数：几样一叠，几乎猜不中'),
                (13.2, 22, '发行时留存根、按号登记：同一个号来两次，或者号码对不上，就是假的')], y=1010)

# ---------------------------------------------------------------- 第九季特辑：古法解密 2.0
GROUPS = [('流体与压强', WATER, [('B20', '公道杯', '虹吸'), ('B24', '水密隔舱', '浮力'), ('B26', '灵渠陡门', '连通器'), ('B27', '唧筒', '大气压'), ('B28', '活塞风箱', '单向阀')]),
          ('力与机械', (176, 141, 87), [('B21', '欹器', '重心'), ('B25', '记里鼓车', '齿轮比')]),
          ('热', SPARK, [('B22', '长信宫灯', '烟气对流'), ('B23', '走马灯', '热气流')]),
          ('信息', GREEN, [('B29', '交子防伪', '概率与暗记')])]

def s9_review(c, t, i):
    corner_tag(c, '第九季特辑 · 古法解密 2.0')
    c.text(60, 110, '十件古物，四类原理', 'serif', 46, INK, 'lm')
    k = 0
    for g, (gname, col, items) in enumerate(GROUPS):
        x = 90 + g * 445
        a = fade(t, 1 + g * 1.5, 2 + g * 1.5)
        c.rect(x, 190, x + 410, 250, fill=mix(BG, col, 0.35 * a), r=10)
        c.text(x + 205, 220, gname, 'bold', 30, mix(BG, INK, a), 'mm')
        for j, (num, name, pr) in enumerate(items):
            b = fade(t, 2 + k * 1.3, 3 + k * 1.3); k += 1
            y = 300 + j * 120
            c.rect(x, y, x + 410, y + 96, fill=mix(BG, SHEET, b), outline=mix(BG, col, b), width=2, r=10)
            c.text(x + 20, y + 30, num, 'mono', 22, mix(BG, MUTED, b), 'lm')
            c.text(x + 90, y + 30, name, 'bold', 28, mix(BG, INK, b), 'lm')
            c.text(x + 20, y + 70, pr, 'sans', 24, mix(BG, col, b), 'lm')
    caps(c, t, [(0, 8, '第九季十集：每一件古物，都能拆成一个今天课本里的原理'),
                (8.2, 16, '一半和水、和空气的压强有关：虹吸、浮力、连通器、大气压、单向阀'),
                (16.2, 24, '另一半是重心、齿轮、热气流，最后一集，是概率和信用'),
                (24.2, 30, '古人不知道这些公式的名字，却把它们做进了杯子、船和纸里')], y=1035)

CLIPS = {
 'B29_朱墨间错': (b29_register, 22), 'B29_暗记': (b29_secret, 22),
 'B29_片头': (titles.opening(BSER, VOL9, SB9, 9, '北宋 · 1024 年 · 益州交子务'), 7),
 'B29_片尾': (titles.closing(BSER, VOL9, SB9, 9, '下集：第九季特辑 · 古法解密 2.0'), 7),
 'S9_回顾': (s9_review, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
