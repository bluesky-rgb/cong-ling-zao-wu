"""第十三季收尾：H4 五铢钱电堆、H5 铅钡琉璃、第十三季特辑（汉代版回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s13a import SH13, SER13, VOL13, BRONZE, HAN

IRON = (120, 120, 128)
BRINE = (150, 190, 215)

# ---------------------------------------------------------------- H4 五铢钱电堆
METALS = [('铜（五铢钱）', True, '有', BRONZE), ('铁', True, '有：汉代已大量冶铁', IRON), ('铅、锡', True, '有：青铜里就有', (140, 140, 160)),
          ('锌', False, '没有：中国炼出金属锌要到明代', NRED), ('铝', False, '没有：19 世纪才提炼出来', NRED)]

def h4_metals(c, t, i):
    corner_tag(c, 'H4 · 汉代有哪些金属能做电堆')
    c.text(60, 96, '第 02 集用铜和锌。可汉代没有锌', 'serif', 40, INK)
    for k, (name, has, note, col) in enumerate(METALS):
        a = fade(t, 0.5 + k * 1.2, 1.3 + k * 1.2)
        if a <= 0: continue
        y = 240 + k * 110
        c.ellipse(200, y, 40, 40, fill=mix(BG, col if has else (90, 90, 90), a), outline=mix(BG, INK, a * 0.5), width=2)
        c.text(270, y, name, 'bold', 30, mix(BG, INK, a), 'lm')
        c.text(620, y, note, 'sans', 26, mix(BG, GREEN if has else NRED, a), 'lm')
    # voltage bars
    b = fade(t, 8, 9)
    c.text(1340, 220, '一节电池的电压（盐水，粗略）', 'bold', 26, mix(BG, INK, b), 'mm')
    bars = [('铜 + 锌（第 02 集）', 0.9, MUTED), ('铜 + 铁（汉代版）', 0.45, HAN)]
    for k, (nm, v, col) in enumerate(bars):
        y = 320 + k * 130
        g = fade(t, 9 + k * 2, 10.5 + k * 2)
        c.text(1100, y - 34, nm, 'sans', 24, mix(BG, INK, b), 'lm')
        c.rect(1100, y - 14, 1100 + 600 * v * g, y + 30, fill=mix(BG, col, b), r=6)
        if g > 0.5:
            c.text(1100 + 600 * v + 16, y + 8, f'约 {v:.1f} 伏', 'mono', 24, mix(BG, INK, b), 'lm')
    d = fade(t, 14, 15)
    c.rect(1080, 620, 1820, 720, fill=mix(BG, SHEET, d), r=10)
    c.text(1450, 670, '数字是常见估计，以本集实测为准', 'sans', 24, mix(BG, MUTED, d), 'mm')
    caps(c, t, [(0, 7, '电池要两种「爱丢电子」程度不同的金属，泡在能导电的液体里'),
                (7.2, 14, '汉代有铜、有铁、有铅和锡，偏偏没有锌：中国炼出金属锌要到明代'),
                (14.2, 22, '用铜钱和铁片配对，一节只有零点几伏：比铜锌电池弱一半左右（以实测为准）')], y=1010)

def h4_stack(c, t, i):
    corner_tag(c, 'H4 · 叠起来，电压就加起来')
    c.text(60, 96, '一节不够，就叠十节', 'serif', 40, INK)
    n = min(10, int(max(0, t - 1) / 1.1) + (1 if t > 1 else 0))
    x0, ybase = 420, 900
    for k in range(n):
        y = ybase - k * 60
        c.rect(x0 - 120, y - 16, x0 + 120, y, fill=IRON, r=3)
        c.rect(x0 - 110, y - 32, x0 + 110, y - 16, fill=mix(BG, BRINE, 0.8))
        c.rect(x0 - 120, y - 52, x0 + 120, y - 32, fill=BRONZE, r=3)
    if n:
        c.text(x0 + 180, ybase - (n - 1) * 60 - 20, f'{n} 节', 'bold', 30, INK, 'lm')
    c.text(x0, 980, '铜钱 / 盐水布 / 铁片', 'sans', 24, MUTED, 'mm')
    v = 0.45 * n
    c.rect(1060, 240, 1760, 420, fill=SHEET, outline=MUTED, width=3, r=16)
    c.text(1410, 300, '万用表（估计）', 'sans', 24, MUTED, 'mm')
    c.text(1410, 370, f'{v:.1f} 伏', 'mono', 60, SPARK, 'mm')
    a = fade(t, 13, 14)
    # compass with coil
    cx, cy = 1410, 700
    c.ellipse(cx, cy, 150, 150, fill=mix(BG, SHEET, a), outline=mix(BG, INK, a), width=3)
    ang = math.radians(-90 + 25 * fade(t, 15, 17))
    c.ellipse(cx, cy, 10, 10, fill=mix(BG, INK, a))
    c.line([(cx - 120 * math.cos(ang), cy - 120 * math.sin(ang)), (cx, cy)], mix(BG, MUTED, a), 8)
    c.line([(cx, cy), (cx + 120 * math.cos(ang), cy + 120 * math.sin(ang))], mix(BG, NRED, a), 8)
    for j in range(5):
        c.ellipse(cx, cy, 24 + j * 5, 175, outline=mix(BG, COPPER, a * 0.9), width=3)
    c.text(cx, cy + 200, '线圈绕在罗盘边：针偏一点点（接第 03 集）', 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '一枚铜钱、一块盐水布、一片铁：这是一节'),
                (6.2, 13, '叠十节，电压加起来，大约四伏多：可电流很小，点不亮灯泡（以实测为准）'),
                (13.2, 22, '把导线绕成圈放在指南针旁边：针动了。汉代人只要想到，就能看见「电生磁」')], y=1040)

# ---------------------------------------------------------------- H5 铅钡琉璃
GLASS = [('罗马 · 钠钙玻璃', [('二氧化硅', 70, (200, 200, 210)), ('氧化钠', 16, (150, 190, 215)), ('氧化钙', 8, (220, 210, 170)), ('其他', 6, LINE)]),
         ('战国—汉 · 铅钡琉璃', [('二氧化硅', 40, (200, 200, 210)), ('氧化铅', 30, (140, 140, 160)), ('氧化钡', 15, (190, 160, 200)), ('其他', 15, LINE)]),
         ('今天 · 铅水晶杯', [('二氧化硅', 58, (200, 200, 210)), ('氧化铅', 24, (140, 140, 160)), ('其他', 18, LINE)])]

def h5_recipe(c, t, i):
    corner_tag(c, 'H5 · 中国古代琉璃，配方不一样')
    c.text(60, 96, '同样叫玻璃，东西方是两套配方', 'serif', 40, INK)
    for k, (name, parts) in enumerate(GLASS):
        y = 280 + k * 200
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        c.text(120, y - 60, name, 'bold', 30, mix(BG, HAN if k == 1 else INK, a), 'lm')
        x = 120
        for nm, pct, col in parts:
            w = 16 * pct * fade(t, 1.5 + k * 4, 3 + k * 4)
            c.rect(x, y - 20, x + w, y + 50, fill=mix(BG, col, a))
            if w > 120:
                c.text(x + w / 2, y + 15, f'{nm} {pct}%', 'bold', 22, BG if sum(col) > 450 else INK, 'mm')
            x += w
    d = fade(t, 13, 14)
    c.text(120, 900, '比例是示意（各件文物差别很大，拍摄前核对）：重点是「铅 + 钡」这两样', 'sans', 24, mix(BG, MUTED, d), 'lm')
    caps(c, t, [(0, 6, '西方玻璃从古罗马起，主要是沙子加苏打、加石灰：钠钙玻璃'),
                (6.2, 13, '战国到汉代的中国琉璃，却含有大量的铅和钡：这种配方别处很少见'),
                (13.2, 22, '今天的水晶杯也加铅：所以它比普通玻璃杯更重、更闪')], y=1010)

def h5_density(c, t, i):
    corner_tag(c, 'H5 · 称一称，照一照')
    c.text(60, 96, '加了铅：更重，也更「闪」', 'serif', 40, INK)
    # density: two blocks equal volume, balance
    a = fade(t, 0.5, 1.5)
    tilt = 8 * fade(t, 2, 4)
    bx, by = 520, 520
    c.line([(bx, by), (bx, 780)], mix(BG, INK, a), 6)
    c.rect(bx - 120, 780, bx + 120, 800, fill=mix(BG, INK, a))
    r = math.radians(tilt)
    lx, ly = bx - 300 * math.cos(r), by + 300 * math.sin(r)
    rx, ry = bx + 300 * math.cos(r), by - 300 * math.sin(r)
    c.line([(lx, ly), (rx, ry)], mix(BG, INK, a), 6)
    c.rect(lx - 60, ly - 100, lx + 60, ly, fill=mix(BG, (140, 140, 160), a), r=8)
    c.rect(rx - 60, ry - 100, rx + 60, ry, fill=mix(BG, (200, 220, 230), a), r=8)
    c.text(lx, ly + 40, '铅玻璃', 'bold', 24, mix(BG, INK, a), 'mm')
    c.text(rx, ry + 40, '普通玻璃', 'bold', 24, mix(BG, INK, a), 'mm')
    b = fade(t, 4, 5)
    c.text(bx, 880, '同样大小：普通约 2.5 克 / 立方厘米，铅水晶约 3 以上（以实测为准）', 'sans', 24, mix(BG, INK, b), 'mm')
    # dispersion prism
    d = fade(t, 9, 10)
    px, py = 1450, 520
    tri = [(px, py - 200), (px - 180, py + 120), (px + 180, py + 120)]
    c.poly(tri, fill=mix(BG, (200, 220, 230), 0.6 * d))
    c.line(tri + [tri[0]], mix(BG, INK, d), 3)
    c.line([(1000, py + 40), (px - 90, py - 20)], mix(BG, (255, 255, 240), d), 6)
    spread = fade(t, 11, 14)
    cols = [(230, 60, 60), (240, 150, 40), (240, 220, 60), (80, 190, 90), (70, 130, 230), (140, 80, 200)]
    for j, col in enumerate(cols):
        ang = math.radians(15 + j * (3 + 4 * spread))
        c.line([(px + 90, py - 20), (px + 90 + 360 * math.cos(ang), py - 20 + 360 * math.sin(ang))], mix(BG, col, d), 5)
    c.text(px, 820, '铅越多，光拐得越厉害，彩虹拉得越开', 'sans', 24, mix(BG, INK, d), 'mm')
    caps(c, t, [(0, 8, '铅原子很重：同样大小的一块，铅玻璃明显更沉，用排水法就能量出来'),
                (8.2, 15, '铅还让光拐弯拐得更厉害，不同颜色分得更开：水晶杯会闪出彩光'),
                (15.2, 22, '汉代琉璃多做成璧、珠、耳珰，很少做杯：铅钡琉璃怕冷热骤变、也不够透（拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- 第十三季特辑：汉代版
SONG = [('01', '摩擦起电'), ('B1', '指南鱼'), ('23', '纸'), ('02', '伏打电堆'), ('21', '玻璃')]
HANN = [('H1', '摩擦起电', '有琥珀毛皮，缺玻璃存电'), ('H2', '司南', '摩擦太大，要磨光或浮起'), ('H3', '纸', '原料与工序都已齐备'),
        ('H4', '五铢钱电堆', '没有锌，铜铁也能发电'), ('H5', '铅钡琉璃', '有玻璃，但配方不同')]

def s13_compare(c, t, i):
    corner_tag(c, '第十三季特辑 · 汉代版')
    c.text(60, 118, '同一个想法，退回一千年', 'serif', 40, INK, 'lm')
    c.text(400, 200, '北宋版（前几季）', 'sans', 24, MUTED, 'mm')
    c.text(1180, 200, '汉代版（第十三季）', 'sans', 24, HAN, 'mm')
    for k, ((sn, sname), (hn, hname, note)) in enumerate(zip(SONG, HANN)):
        y = 290 + k * 140
        c.rect(260, y - 34, 540, y + 34, fill=SHEET, outline=COPPER if sn[0].isdigit() else FIELD, width=2, r=10)
        c.text(280, y, sn, 'mono', 20, MUTED, 'lm')
        c.text(420, y, sname, 'sans', 26, INK, 'mm')
        a = fade(t, 2 + k * 3, 3 + k * 3)
        if a <= 0: continue
        pts = [(540 + (500 - 0) * j / 20, y) for j in range(21)]
        seg(c, [(540, y), (1040, y)], mix(BG, HAN, a * 0.8), 2)
        c.rect(1040, y - 38, 1320, y + 38, fill=mix(BG, mix(SHEET, SPARK, 0.3), a), outline=mix(LINE, HAN, a), width=2, r=10)
        c.text(1060, y, hn, 'mono', 20, mix(BG, MUTED, a), 'lm')
        c.text(1190, y, hname, 'bold', 26, mix(BG, INK, a), 'mm')
        c.text(1360, y, note, 'sans', 24, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 8, '第十三季，把五个北宋版的实验退回到汉代'),
                (8.2, 17, '有的照样能做：琥珀起电、麻纸、铜钱铁片电堆；有的卡在一种材料上：玻璃、锌'),
                (17.2, 24, '真正缺的往往不是道理，而是一种材料，或一道工序'),
                (24.2, 30, '下一次换时代：退回更远，还是往前走到 1800 年？')], y=1040)

CLIPS = {
 'H4_金属': (h4_metals, 22), 'H4_电堆': (h4_stack, 22),
 'H4_片头': (titles.opening(SER13, VOL13, SH13, 3, '汉代 · 五铢钱（公元前 118 年起铸）'), 7),
 'H4_片尾': (titles.closing(SER13, VOL13, SH13, 3, '下集：汉代的玻璃，为什么和西方不一样？'), 7),
 'H5_配方': (h5_recipe, 22), 'H5_称照': (h5_density, 22),
 'H5_片头': (titles.opening(SER13, VOL13, SH13, 4, '战国—汉 · 铅钡琉璃'), 7),
 'H5_片尾': (titles.closing(SER13, VOL13, SH13, 4, '下集：第十三季特辑 · 汉代版回顾'), 7),
 'S13_对照': (s13_compare, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
