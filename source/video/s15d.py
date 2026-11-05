"""第十五季收尾：E91 程序与计算机、第十五季特辑（第四层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s15a import S15A, SER15, VOL15, WAVE

# ---------------------------------------------------------------- E91 程序与计算机
PROG = [('0', '把 1 放进「数」', 'cnt=1'), ('1', '把 0 放进「和」', 'sum=0'), ('2', '「和」加上「数」', 'sum+=cnt'),
        ('3', '「数」加 1', 'cnt+=1'), ('4', '「数」≤ 10 就跳回 2', 'if cnt<=10 goto 2'), ('5', '停', 'halt')]

def trace(n_max=10):
    pc, cnt, s = 0, 0, 0
    steps = []
    while True:
        steps.append((pc, cnt, s))
        if pc == 0: cnt = 1; pc = 1
        elif pc == 1: s = 0; pc = 2
        elif pc == 2: s += cnt; pc = 3
        elif pc == 3: cnt += 1; pc = 4
        elif pc == 4: pc = 2 if cnt <= n_max else 5
        else: break
    return steps

TRACE = trace()

def e91_fetch(c, t, i):
    corner_tag(c, '第 91 集 · 取一条，做一条，再取下一条')
    c.text(60, 96, '一个人照着卡片做：算出 1 + 2 + … + 10', 'serif', 40, INK)
    k = min(len(TRACE) - 1, int(max(0, t - 2) * 2.4))
    pc, cnt, s = TRACE[k]
    c.text(200, 200, '内存：程序', 'bold', 28, MUTED, 'lm')
    for j, (addr, txt, _) in enumerate(PROG):
        y = 260 + j * 90
        on = j == pc
        c.rect(200, y - 34, 900, y + 34, fill=mix(SHEET, SPARK, 0.35) if on else SHEET, outline=SPARK if on else LINE, width=3 if on else 1, r=10)
        c.text(230, y, addr, 'mono', 28, MUTED, 'lm')
        c.text(290, y, txt, 'sans', 28, INK, 'lm')
    yy = 260 + pc * 90
    c.poly([(125, yy - 18), (160, yy), (125, yy + 18)], SPARK)
    c.text(1100, 200, '内存：数据', 'bold', 28, MUTED, 'lm')
    for j, (nm, v) in enumerate((('数', cnt), ('和', s))):
        y = 290 + j * 140
        c.rect(1100, y - 50, 1500, y + 50, fill=SHEET, r=12)
        c.text(1130, y, nm, 'bold', 32, INK, 'lm')
        c.text(1470, y, str(v), 'mono', 48, GREEN, 'rm')
    c.rect(1100, 600, 1500, 680, fill=SHEET, r=12)
    c.text(1130, 640, '指令计数器', 'sans', 26, MUTED, 'lm')
    c.text(1470, 640, str(pc), 'mono', 40, SPARK, 'rm')
    c.text(1300, 760, f'已经走了 {k} 步', 'sans', 26, MUTED, 'mm')
    caps(c, t, [(0, 6, '计算机最核心的循环只有一句话：取一条指令，做完，再取下一条'),
                (6.2, 14, '「跳回 2」让同样几条指令反复做：这叫循环'),
                (14.2, 22, '每一条都只是开关能做的小事：加一、比较、跳转。可几十步下来，答案是 55')], y=1010)

def e91_stored(c, t, i):
    corner_tag(c, '第 91 集 · 程序也是数据')
    c.text(60, 96, '换一个问题，不用重新接线：改一张卡片就行', 'serif', 40, INK)
    a = fade(t, 1, 2)
    c.text(480, 200, 'ENIAC（1946）：换程序 = 重新插线', 'bold', 28, mix(BG, INK, a), 'mm')
    rnd = random.Random(5)
    for k in range(18):
        x1, y1 = 180 + rnd.random() * 600, 260 + rnd.random() * 400
        x2, y2 = 180 + rnd.random() * 600, 260 + rnd.random() * 400
        c.line([(x1, y1), ((x1 + x2) / 2, max(y1, y2) + 40), (x2, y2)], mix(BG, [WAVE, GREEN, SPARK, NRED][k % 4], a * 0.8), 3)
    c.text(480, 720, '要几天时间（拍摄前核对）', 'sans', 24, mix(BG, MUTED, a), 'mm')
    b = fade(t, 7, 8)
    c.text(1440, 200, '存储程序（1945 年起）：程序放进内存', 'bold', 28, mix(BG, INK, b), 'mm')
    for j, (addr, txt, _) in enumerate(PROG):
        y = 280 + j * 70
        changed = j == 4 and t > 12
        col = mix(SHEET, SPARK, 0.4) if changed else SHEET
        c.rect(1100, y - 28, 1780, y + 28, fill=mix(BG, col, b), r=8)
        label = '「数」≤ 20 就跳回 2' if changed else txt
        c.text(1130, y, f'{addr}  {label}', 'sans', 24, mix(BG, INK, b), 'lm')
    d = fade(t, 12, 13)
    c.text(1440, 720, '改一张卡：答案从 55 变成 210', 'bold', 28, mix(BG, GREEN, d), 'mm')
    caps(c, t, [(0, 7, '最早的电子计算机 ENIAC，换一个问题就要拔线、插线，重新连一遍'),
                (7.2, 13, '冯·诺依曼等人的报告提出：把指令也当成数，和数据一起存进内存'),
                (13.2, 22, '改程序就像改一张卡片。开关做逻辑，齿轮做进位，磁带做记忆：合起来，就是会照着程序做的机器')], y=1010)

# ---------------------------------------------------------------- 第十五季特辑：第四层
OLD15 = [('照相', '55'), ('电影', '74'), ('无线电', '76'), ('留声机', '73'), ('电磁铁', '56'), ('摆钟', '45'), ('电话', '72'),
         ('风筝', 'B41'), ('逆风航行', '43'), ('内燃机', '78'), ('滑轮组', '39'), ('电动机', '58'), ('热气球', '44'),
         ('光学电报', '50'), ('玻璃', '21'), ('影子测地球', '47'), ('机械计算器', '80'), ('逻辑门', '81')]
NEW15 = [('电视', '82', ['电影', '无线电', '照相']), ('磁带录音', '83', ['留声机', '电磁铁']), ('雷达', '84', ['无线电', '摆钟']),
         ('矿石收音机', '85', ['无线电', '电话']), ('机翼', '86', ['风筝', '内燃机', '逆风航行']), ('电梯', '87', ['滑轮组', '电动机']),
         ('火箭', '88', ['热气球', '内燃机']), ('光纤', '89', ['光学电报', '玻璃']), ('卫星定位', '90', ['影子测地球', '摆钟', '无线电']),
         ('计算机', '91', ['逻辑门', '机械计算器', '磁带录音'])]

def s15_layer(c, t, i):
    corner_tag(c, '第十五季特辑 · 第四层')
    c.text(60, 118, '第四层：组合的组合的组合', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD15):
        pos[name] = (340, 205 + k * 44)
    for k, (name, num, deps) in enumerate(NEW15):
        pos[name] = (1180 + (210 if name in ('磁带录音', '矿石收音机', '电梯', '光纤', '计算机') else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1280, 160, '第十五季新长出', 'sans', 24, MUTED, 'mm')
    newset = set(n for n, _, _ in NEW15)
    for k, (name, num, deps) in enumerate(NEW15):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx = x0 + 110
            ex = x1 - 110
            col = mix(BG, COPPER if d in newset else FIELD, a * 0.8)
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, col, 2)
    for name, num in OLD15:
        x, y = pos[name]
        c.rect(x - 110, y - 19, x + 110, y + 19, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW15):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第四层的十集：每一集都长在两三个旧节点上'),
                (8.2, 16, '电影加无线电长出电视，风筝加内燃机长出机翼，影子测地球加摆钟长出卫星定位'),
                (16.2, 24, '最后，开关、齿轮计算器和磁带合在一起：一台会照着程序做的计算机'),
                (24.2, 30, '从一块琥珀擦出的静电，走到了一台会照着程序做的机器')], y=1040)

CLIPS = {
 'E91_取指执行': (e91_fetch, 22), 'E91_存储程序': (e91_stored, 22),
 'E91_片头': (titles.opening(SER15, VOL15, S15A, 9, '1945 年 · 存储程序 · 1946 年 ENIAC'), 7),
 'E91_片尾': (titles.closing(SER15, VOL15, S15A, 9, '下集：第十五季特辑 · 第四层'), 7),
 'S15_第四层': (s15_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
