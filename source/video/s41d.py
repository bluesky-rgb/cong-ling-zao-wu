"""第四十一季（第十七层：书桌与办公室）收官：E221 键盘 + 第四十一季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s41a import S41A, SER41, VOL41, STEEL

FOIL = (200, 205, 215)
KEYC = (70, 75, 90)
LAMP = (250, 220, 90)


# ---------------------------------------------------------------- E221 键盘
def e221_matrix(c, t, i):
    corner_tag(c, '第 221 集 · 横线竖线交叉成格子')
    c.text(60, 96, '键盘里的线排成横竖交叉的格子，每个键在一个交叉点：按下去，就把那一条横线和那一条竖线接通', 'serif', 36, INK)
    x0, y0, s = 300, 340, 140
    rows, cols = 4, 5
    k = int(t / 2.5) % (rows * cols)
    pr, pc = (k * 7) % rows, (k * 3) % cols
    for r in range(rows):
        c.line([(x0 - 60, y0 + r * s), (x0 + (cols - 1) * s + 60, y0 + r * s)], SPARK if r == pr else mix(BG, FOIL, 0.6), 6 if r == pr else 4)
        c.text(x0 - 90, y0 + r * s, f'横 {r + 1}', 'sans', 20, MUTED, 'rm')
    for q in range(cols):
        c.line([(x0 + q * s, y0 - 60), (x0 + q * s, y0 + (rows - 1) * s + 60)], GREEN if q == pc else mix(BG, FOIL, 0.4), 6 if q == pc else 4)
        c.text(x0 + q * s, y0 - 90, f'竖 {chr(65 + q)}', 'sans', 20, MUTED, 'mm')
    for r in range(rows):
        for q in range(cols):
            on = (r, q) == (pr, pc)
            c.rect(x0 + q * s - 40, y0 + r * s - 40, x0 + q * s + 40, y0 + r * s + 40, fill=mix(BG, SPARK, 0.5) if on else mix(BG, KEYC, 0.6), r=10)
    c.rect(1240, 300, 1860, 640, fill=SHEET, r=12)
    c.text(1550, 350, '20 个键', 'bold', 26, INK, 'mm')
    c.text(1550, 410, '每键一根线：要 20 根', 'sans', 22, NRED, 'mm')
    c.text(1550, 460, '排成格子：4 + 5 = 9 根', 'sans', 22, GREEN, 'mm')
    c.text(1550, 540, f'现在按的是：横 {pr + 1} × 竖 {chr(65 + pc)}', 'bold', 24, SPARK, 'mm')
    caps(c, t, [(0, 7, '一个键盘有一百多个键，每个键一根线，线就太多了'),
                (7.2, 14, '把线排成横竖交叉的格子，每个键放在一个交叉点上'),
                (14.2, 22, '按下哪个键，就接通哪一条横线和哪一条竖线：几十根线管一百多个键（示意）')], y=1010)


def e221_scan(c, t, i):
    corner_tag(c, 'E221 · 一行行快速检查')
    c.text(60, 96, '键盘里的小芯片轮流给每一条横线「通电」，同时看哪条竖线有电：每秒检查上千遍，按下立刻就知道', 'serif', 35, INK)
    x0, y0, s = 300, 300, 150
    rows, cols = 4, 5
    pressed = (2, 3)
    cur = int(t * 2) % rows
    for r in range(rows):
        c.line([(x0 - 60, y0 + r * s), (x0 + (cols - 1) * s + 60, y0 + r * s)], LAMP if r == cur else mix(BG, FOIL, 0.5), 6 if r == cur else 4)
    for q in range(cols):
        hot = cur == pressed[0] and q == pressed[1]
        c.line([(x0 + q * s, y0 - 60), (x0 + q * s, y0 + (rows - 1) * s + 60)], GREEN if hot else mix(BG, FOIL, 0.4), 6 if hot else 4)
        c.ellipse(x0 + q * s, y0 + (rows - 1) * s + 100, 16, 16, fill=GREEN if hot else mix(BG, MUTED, 0.5))
    pr, pc = pressed
    c.rect(x0 + pc * s - 40, y0 + pr * s - 40, x0 + pc * s + 40, y0 + pr * s + 40, fill=mix(BG, SPARK, 0.6), r=10)
    c.text(x0 + pc * s, y0 + pr * s, '按下', 'bold', 20, INK, 'mm')
    c.rect(1240, 300, 1860, 640, fill=SHEET, r=12)
    c.text(1550, 350, f'正在检查：横 {cur + 1}', 'bold', 26, LAMP, 'mm')
    found = cur == pressed[0]
    c.text(1550, 430, '竖 D 有电！' if found else '没有竖线有电', 'bold', 24, GREEN if found else MUTED, 'mm')
    c.text(1550, 500, '→ 按下的是 横 3 × 竖 D' if found else '→ 下一行', 'sans', 22, INK, 'mm')
    c.text(1550, 580, '实际每秒扫几百到上千遍（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '芯片先给第 1 条横线通电，看哪条竖线有电；没有，就换第 2 条'),
                (7.2, 14, '轮到第 3 条横线时，竖线 D 有了电：按下的就是第 3 行 D 列那个键'),
                (14.2, 22, '这样一轮轮扫得飞快，你按键的那一下早就被发现了（示意）')], y=1010)


# ---------------------------------------------------------------- 第四十一季特辑
OLD41 = [('杠杆与滑轮组', '39'), ('钢', '62'), ('螺丝与标准件', '64'), ('纸', '23'), ('魔术贴', '146'), ('塑料', '142'),
         ('保鲜膜', '194'), ('摆钟', '45'), ('LED', '102'), ('夜光表盘', '187'), ('电动机', '58'), ('齿轮与轴承', '41'),
         ('摩擦起电', '01'), ('印刷机', '65'), ('数码相机', '95'), ('条形码', '166'), ('开关与逻辑门', '81'), ('程序与计算机', '91')]
NEW41 = [('订书机', '212', ['杠杆与滑轮组', '钢']), ('回形针', '213', ['钢', '螺丝与标准件']), ('便利贴', '214', ['纸', '魔术贴']),
         ('修正带', '215', ['塑料', '保鲜膜']), ('自动铅笔', '216', ['螺丝与标准件', '摆钟']), ('荧光笔', '217', ['LED', '夜光表盘']),
         ('碎纸机', '218', ['电动机', '齿轮与轴承']), ('复印机', '219', ['摩擦起电', '印刷机']), ('扫描仪', '220', ['数码相机', '条形码']),
         ('键盘', '221', ['开关与逻辑门', '程序与计算机'])]


def s41_layer(c, t, i):
    corner_tag(c, '第四十一季特辑 · 第十七层')
    c.text(60, 118, '第十七层：书桌与办公室', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD41):
        pos[name] = (340, 215 + k * 42)
    for k, (name, num, deps) in enumerate(NEW41):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 168, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十一季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW41):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD41:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW41):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十七层的十集：书桌与办公室里的机器和小东西'),
                (8.2, 16, '杠杆和钢长出订书机，钢长出回形针，纸和魔术贴长出便利贴，塑料长出修正带'),
                (16.2, 24, '摆钟长出自动铅笔，LED 长出荧光笔，电动机长出碎纸机，摩擦起电长出复印机，数码相机长出扫描仪'),
                (24.2, 30, '最后，开关与逻辑门和计算机一起，长出了键盘')], y=1040)


CLIPS = {
 'E221_矩阵': (e221_matrix, 22), 'E221_扫描': (e221_scan, 22),
 'E221_片头': (titles.opening(SER41, VOL41, S41A, 9, '19 世纪 70 年代打字机键盘排列定型'), 7),
 'E221_片尾': (titles.closing(SER41, VOL41, S41A, 9, '下集：第四十一季特辑 · 第十七层回顾'), 7),
 'S41_第十七层': (s41_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
