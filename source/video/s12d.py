"""第十二季收尾：E81 开关与逻辑门、第十二季特辑（第三层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s12a import S12A, SER12, VOL12

LED_ON = (255, 210, 80)

def switch(c, x, y, on, label):
    c.ellipse(x, y, 8, 8, fill=INK)
    c.ellipse(x + 90, y, 8, 8, fill=INK)
    if on:
        c.line([(x, y), (x + 90, y)], GREEN, 6)
    else:
        c.line([(x, y), (x + 80, y - 40)], NRED, 6)
    c.text(x + 45, y + 40, f'{label} = {1 if on else 0}', 'mono', 24, GREEN if on else NRED, 'mm')

def led(c, x, y, on, label):
    c.ellipse(x, y, 30, 30, fill=LED_ON if on else (60, 60, 60), outline=MUTED, width=2)
    if on:
        c.ellipse(x, y, 46, 46, outline=mix(BG, LED_ON, 0.4), width=4)
    c.text(x, y + 60, label, 'bold', 24, INK, 'mm')

STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]

def e81_and_or(c, t, i):
    corner_tag(c, '第 81 集 · 串联是「与」，并联是「或」')
    c.text(60, 96, '两个开关，两种接法', 'serif', 40, INK)
    k = min(3, int(max(0, t - 2) / 4))
    A, B = STATES[k]
    # AND: series
    y = 330
    c.text(120, y - 110, '串联：A 和 B 都按下，灯才亮（与）', 'bold', 28, INK, 'lm')
    c.line([(120, y), (200, y)], COPPER, 4)
    switch(c, 200, y, A, 'A')
    c.line([(290, y), (420, y)], COPPER, 4)
    switch(c, 420, y, B, 'B')
    c.line([(510, y), (680, y)], COPPER, 4)
    led(c, 720, y, A and B, '灯')
    # OR: parallel
    y2 = 720
    c.text(120, y2 - 170, '并联：A 或 B 任一按下，灯就亮（或）', 'bold', 28, INK, 'lm')
    c.line([(120, y2), (200, y2)], COPPER, 4)
    c.line([(200, y2), (200, y2 - 80), (300, y2 - 80)], COPPER, 4)
    c.line([(200, y2), (200, y2 + 80), (300, y2 + 80)], COPPER, 4)
    switch(c, 300, y2 - 80, A, 'A')
    switch(c, 300, y2 + 80, B, 'B')
    c.line([(390, y2 - 80), (520, y2 - 80), (520, y2 + 80), (390, y2 + 80)], COPPER, 4)
    c.line([(520, y2), (680, y2)], COPPER, 4)
    led(c, 720, y2, A or B, '灯')
    # truth table
    x0 = 1100
    c.text(x0, 240, 'A   B   与   或', 'mono', 32, INK, 'lm')
    for j, (a_, b_) in enumerate(STATES):
        if j > k: break
        yy = 320 + j * 80
        hl = j == k
        if hl:
            c.rect(x0 - 20, yy - 32, x0 + 420, yy + 32, fill=mix(BG, SPARK, 0.2), r=8)
        c.text(x0, yy, f'{a_}   {b_}   {a_ & b_}    {a_ | b_}', 'mono', 32, INK, 'lm')
    a = fade(t, 18, 19)
    c.text(x0, 700, '1 = 开、亮、「是」', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(x0, 750, '0 = 关、灭、「否」', 'sans', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '把开关按下记作 1，松开记作 0；灯亮是 1，灭是 0'),
                (6.2, 14, '串联：两个都按下才亮，这叫「与」；并联：随便按一个就亮，这叫「或」'),
                (14.2, 22, '1937 年，香农在硕士论文里证明：开关电路，就是一套逻辑运算')], y=1010)

def e81_half_adder(c, t, i):
    corner_tag(c, '第 81 集 · 半加器：1 + 1 = 10')
    c.text(60, 96, '用开关做加法：两个 1 位数相加', 'serif', 40, INK)
    k = min(3, int(max(0, t - 2) / 4))
    A, B = STATES[k]
    S, C = A ^ B, A & B
    # inputs
    c.text(260, 240, '输入', 'bold', 28, MUTED, 'mm')
    for j, (nm, v) in enumerate((('A', A), ('B', B))):
        y = 360 + j * 220
        c.rect(180, y - 50, 340, y + 50, fill=mix(BG, GREEN if v else NRED, 0.35), r=10)
        c.text(260, y, f'{nm} = {v}', 'mono', 36, INK, 'mm')
    # gates
    gates = [('异或（XOR）\n一个按下才亮', 360, S, '和'), ('与（AND）\n两个都按下才亮', 640, C, '进位')]
    for nm, y, out, lab in gates:
        c.rect(640, y - 80, 1000, y + 80, fill=SHEET, outline=MUTED, width=3, r=14)
        c.text(820, y, nm, 'bold', 26, INK, 'mm')
        for j in range(2):
            c.line([(340, 360 + j * 220), (640, y - 30 + j * 60)], mix(BG, COPPER, 0.8), 3)
        c.line([(1000, y), (1200, y)], COPPER, 3)
        led(c, 1240, y, out, lab)
    c.text(1560, 360, f'{A} + {B} = {C}{S}' if C else f'{A} + {B} = {S}', 'mono', 60, SPARK, 'mm')
    c.text(1560, 450, '（二进制）', 'sans', 24, MUTED, 'mm')
    a = fade(t, 17, 18)
    c.rect(1320, 560, 1860, 860, fill=mix(BG, SHEET, a), r=12)
    c.text(1350, 610, '楼梯上下各一个开关控制同一盏灯：', 'sans', 22, mix(BG, INK, a), 'lm')
    c.text(1350, 650, '那就是「异或」', 'bold', 26, mix(BG, INK, a), 'lm')
    c.text(1350, 720, '把很多个半加器连起来，', 'sans', 22, mix(BG, INK, a), 'lm')
    c.text(1350, 760, '就能加任意大的数：', 'sans', 22, mix(BG, INK, a), 'lm')
    c.text(1350, 800, '计算机就是这样算的', 'bold', 26, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 6, '二进制里只有 0 和 1：1 + 1 = 10，「和」是 0，向前进 1'),
                (6.2, 14, '「和」这一位：两个输入只有一个是 1 时才亮，叫异或；「进位」：两个都是 1 才亮，就是与'),
                (14.2, 22, '一个异或加一个与，就是半加器。开关换成电磁铁控制的继电器，后来又换成晶体管：这就是计算机')], y=1010)

# ---------------------------------------------------------------- 第十二季特辑：第三层
OLD12 = [('磁生电', '04'), ('电磁铁', '56'), ('电报', '57'), ('鱼洗', 'B9'), ('照相', '55'), ('走马灯', 'B23'), ('电灯', '60'),
         ('影子测地球', '47'), ('蒸汽发电', '10'), ('曲柄连杆', '40'), ('钢', '62'), ('钢筋混凝土', '63'), ('齿轮', '41'), ('计算尺', '71')]
NEW12 = [('电话', '72', ['电磁铁', '电报', '磁生电']), ('留声机', '73', ['电话', '鱼洗']), ('电影', '74', ['照相', '走马灯']),
         ('变压器', '75', ['磁生电', '电灯']), ('无线电', '76', ['电报', '变压器']), ('太阳能电池', '77', ['影子测地球', '电灯']),
         ('内燃机', '78', ['蒸汽发电', '曲柄连杆']), ('悬索桥', '79', ['钢', '钢筋混凝土']), ('机械计算器', '80', ['齿轮', '计算尺']),
         ('逻辑门', '81', ['电磁铁', '机械计算器'])]

def s12_layer(c, t, i):
    corner_tag(c, '第十二季特辑 · 第三层')
    c.text(60, 118, '第三层：组合的组合', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD12):
        pos[name] = (340, 210 + k * 56)
    for k, (name, num, deps) in enumerate(NEW12):
        pos[name] = (1180 + (210 if name in ('留声机', '无线电', '逻辑门') else 0), 225 + k * 76)
    c.text(340, 168, '前十一季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1280, 168, '第十二季新长出', 'sans', 24, MUTED, 'mm')
    oldset = set(n for n, _ in OLD12)
    for k, (name, num, deps) in enumerate(NEW12):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx = x0 + 110
            ex = x1 - 110
            col = mix(BG, FIELD if d in oldset else COPPER, a * 0.8)
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, col, 2)
    for name, num in OLD12:
        x, y = pos[name]
        c.rect(x - 110, y - 22, x + 110, y + 22, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, MUTED, 'lm')
        c.text(x + 14, y, name, 'sans', 21, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW12):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 14, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第三层的十集，长在第二层上：组合的组合'),
                (8.2, 16, '电磁铁和电报长出电话，电话又长出留声机；变压器和电报长出无线电'),
                (16.2, 24, '齿轮和计算尺长出机械计算器，再加上电磁铁，长出了开关里的逻辑'),
                (24.2, 30, '从一块琥珀擦出的静电，走到了能做加法的开关')], y=1040)

CLIPS = {
 'E81_与或': (e81_and_or, 22), 'E81_半加器': (e81_half_adder, 22),
 'E81_片头': (titles.opening(SER12, VOL12, S12A, 9, '1937 年 · 香农：开关电路就是逻辑'), 7),
 'E81_片尾': (titles.closing(SER12, VOL12, S12A, 9, '下集：第十二季特辑 · 第三层'), 7),
 'S12_第三层': (s12_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
