"""第四十五季（第十九层：玩具箱）收官：E241 八音盒 + 第四十五季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s45a import S45A, SER45, VOL45

COMB = (200, 205, 215)
DRUM = (210, 170, 80)


# ---------------------------------------------------------------- E241 八音盒
def e241_comb(c, t, i):
    corner_tag(c, '第 241 集 · 一排钢齿，越短越高')
    c.text(60, 96, '八音盒里有一排长短不同的钢齿，叫音梳：齿越短、越硬，被拨一下振得越快，音越高；一根齿就是一个音', 'serif', 36, INK)
    x0, y0 = 300, 300
    n = 18
    hit = int(t * 3) % n
    for k in range(n):
        L = 420 - k * 16
        x = x0 + k * 64
        vib = 0
        age = (t * 3) % 1
        if k == hit:
            vib = 14 * math.exp(-age * 3) * math.sin(t * 60 * (1 + k * 0.08))
        c.line([(x, y0), (x + vib, y0 + L)], mix(BG, COMB, 1.0), 22)
        if k == hit:
            for m in range(3):
                c.arc(x + vib, y0 + L + 20, 30 + m * 26, 30 + m * 26, 40, 140, mix(BG, SPARK, 1 - age), 3)
    c.rect(x0 - 40, y0 - 40, x0 + n * 64, y0, fill=mix(BG, COMB, 0.8), r=6)
    c.text(x0, y0 + 470, '长：音低', 'bold', 24, INK, 'mm')
    c.text(x0 + (n - 1) * 64, y0 + 470, '短：音高', 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 7, '音梳是一整块钢片，切成一排长短不同的细齿，根部连在一起'),
                (7.2, 14, '齿越长越软，振得慢，音低；齿越短越硬，振得快，音高'),
                (14.2, 22, '有的齿背后还粘着小铅块，让它振得再慢一点，把音调准（示意）')], y=1010)


def e241_drum(c, t, i):
    corner_tag(c, '第 241 集 · 滚筒上的凸针，就是乐谱')
    c.text(60, 96, '滚筒上按乐谱插满凸针：滚筒一转，凸针依次拨响对应的钢齿；凸针排在哪里，就是一段写死的程序', 'serif', 36, INK)
    cx, cy = 700, 600
    W, H = 900, 300
    c.rect(cx - W / 2, cy - H / 2, cx + W / 2, cy + H / 2, fill=mix(BG, DRUM, 1.0), r=40)
    r = random.Random(3)
    pins = [(r.randint(0, 11), r.uniform(0, 1)) for _ in range(40)]
    off = (t * 0.06) % 1
    for col, ph in pins:
        u = (ph + off) % 1
        y = cy - H / 2 + u * H
        if 0.02 < u < 0.98:
            x = cx - W / 2 + 40 + col * 74
            near = abs(u - 0.1) < 0.03
            c.ellipse(x, y, 8, 8, fill=SPARK if near else mix(BG, INK, 0.6))
    for k in range(12):
        x = cx - W / 2 + 40 + k * 74
        c.line([(x, cy - H / 2 - 200), (x, cy - H / 2 + 26)], mix(BG, COMB, 1.0), 14)
    c.text(cx, cy + H / 2 + 50, '滚筒（展开示意）：亮点 = 正在拨响的凸针', 'sans', 22, MUTED, 'mm')
    bx = 1450
    c.text(bx + 150, 300, '同一个思路', 'bold', 26, INK, 'mm')
    for k, nm in enumerate(['八音盒：凸针', '自动钢琴：纸卷上的孔', '早期计算机：打孔卡']):
        c.rect(bx, 350 + k * 120, bx + 320, 440 + k * 120, fill=SHEET, r=10)
        c.text(bx + 160, 395 + k * 120, nm, 'sans', 22, INK, 'mm')
    caps(c, t, [(0, 7, '拧紧发条，发条带着滚筒匀速转，滚筒上插着几百根细细的凸针'),
                (7.2, 14, '凸针转到哪根齿下面，就把它拨响：凸针的位置就是写好的音符和节奏'),
                (14.2, 22, '换一个滚筒就换一首曲子：这和用纸卷、打孔卡控制机器是同一个思路（示意）')], y=1010)


OLD45 = [('齿轮与轴承', '41'), ('摆钟', '45'), ('橡胶轮胎', '143'), ('蹦床', '211'), ('玻璃', '21'), ('透镜', '52'),
         ('肥皂', '22'), ('洗手', '32'), ('塑料', '142'), ('纸尿裤', '149'), ('螺丝与标准件', '64'), ('3D 打印', '104'),
         ('无线电', '76'), ('电动机', '58'), ('电磁铁', '56'), ('磁性螺丝刀', '228'), ('卷尺', '222'), ('留声机', '73'),
         ('程序与计算机', '91')]
NEW45 = [('溜溜球', '232', ['齿轮与轴承', '摆钟']), ('弹力球', '233', ['橡胶轮胎', '蹦床']), ('万花筒', '234', ['玻璃', '透镜']),
         ('泡泡', '235', ['肥皂', '洗手']), ('史莱姆', '236', ['塑料', '纸尿裤']), ('积木', '237', ['螺丝与标准件', '3D 打印']),
         ('遥控车', '238', ['无线电', '电动机']), ('磁力片', '239', ['电磁铁', '磁性螺丝刀']), ('回力车', '240', ['齿轮与轴承', '卷尺']),
         ('八音盒', '241', ['留声机', '程序与计算机'])]


def s45_layer(c, t, i):
    corner_tag(c, '第四十五季特辑 · 第十九层')
    c.text(60, 118, '第十九层：玩具箱', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD45):
        pos[name] = (340, 210 + k * 40)
    for k, (name, num, deps) in enumerate(NEW45):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 168, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第四十五季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW45):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD45:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW45):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十九层的十集：玩具箱里的东西'),
                (8.2, 16, '齿轮和摆钟长出溜溜球，橡胶和蹦床长出弹力球，玻璃和透镜长出万花筒，肥皂长出泡泡'),
                (16.2, 24, '塑料和纸尿裤长出史莱姆，标准件长出积木，无线电长出遥控车，电磁铁长出磁力片'),
                (24.2, 30, '齿轮和卷尺长出回力车；最后，留声机和计算机一起，长出了八音盒')], y=1040)


CLIPS = {
 'E241_音梳': (e241_comb, 22), 'E241_滚筒': (e241_drum, 22),
 'E241_片头': (titles.opening(SER45, VOL45, S45A, 9, '18 世纪末瑞士钟表匠发明八音盒'), 7),
 'E241_片尾': (titles.closing(SER45, VOL45, S45A, 9, '下集：第四十五季特辑 · 第十九层回顾'), 7),
 'S45_第十九层': (s45_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
