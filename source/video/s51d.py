"""第五十一季（第二十二层：门厅与客厅）收官：E271 地毯吸音 + 第五十一季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s51a import S51A, SER51, VOL51

SOUND = (120, 180, 230)
RUG = (190, 110, 90)
WALL = (200, 200, 195)


def e271_echo(c, t, i):
    corner_tag(c, '第 271 集 · 硬墙把声音弹回来')
    c.text(60, 96, '空房间的硬墙、硬地板几乎把声音全弹回来，来回弹好几次才消失；铺上地毯、挂上被子，弹回来的少了', 'serif', 36, INK)
    soft = t > 7.2
    x0, y0, x1, y1 = 300, 220, 1620, 860
    c.rect(x0, y0, x1, y1, outline=mix(BG, WALL, 1.0), width=10)
    if soft:
        c.rect(x0 + 6, y1 - 50, x1 - 6, y1 - 6, fill=mix(BG, RUG, 1.0))
        c.rect(x1 - 60, y0 + 6, x1 - 6, y1 - 6, fill=mix(BG, (150, 140, 200), 1.0))
        c.text(960, y1 - 28, '地毯', 'bold', 24, (255, 255, 255), 'mm')
        c.text(x1 - 33, 540, '被', 'bold', 24, (255, 255, 255), 'mm')
    cx, cy = 700, 560
    ph = (t % 7) / 7
    for k in range(4):
        r = ph * 1400 - k * 260
        if r <= 0:
            continue
        a = (0.25 if soft else 0.85) ** (k + (0 if k == 0 else 1))
        c.ellipse(cx, cy, r * 0.5, r * 0.35, outline=mix(BG, SOUND, a), width=5)
    c.ellipse(cx, cy, 22, 22, fill=NRED)
    c.text(cx, cy + 50, '拍手', 'bold', 24, NRED, 'mm')
    # 录音波形
    wx, wy = 300, 960
    n = 120
    pts = []
    for k in range(n):
        tt = k / n
        decay = math.exp(-tt * (14 if soft else 4))
        pts.append((wx + 1320 * tt, wy - 0 + 0))
    for k in range(n):
        tt = k / n
        decay = math.exp(-tt * (14 if soft else 4))
        h = 50 * decay * abs(math.sin(k * 1.7))
        c.line([(wx + 11 * k, wy - h), (wx + 11 * k, wy + h)], mix(BG, SOUND, 1.0), 4)
    c.text(wx - 20, wy, '录音', 'sans', 22, MUTED, 'rm')
    caps(c, t, [(0, 7, '空房间里拍一下手：声音在硬墙之间来回弹，录音里拖着长长的尾巴'),
                (7.2, 14, '铺上毯子、挂上被子，同样力度再拍一次'),
                (14.2, 22, '弹回来的声音少了，尾巴短了，屋里听着就安静（以实测为准）')], y=1030)


def e271_pores(c, t, i):
    corner_tag(c, '第 271 集 · 钻进纤维缝里，变成一点点热')
    c.text(60, 96, '声音是空气来回地挤；钻进地毯和毛巾的纤维缝里，空气和纤维来回摩擦，一部分声音变成了一点点热', 'serif', 36, INK)
    for j, (lab, soft) in enumerate([('硬墙：几乎全弹回来', False), ('多孔的软材料：弹回来的少', True)]):
        cx = 500 + j * 920
        wx = cx + 160
        if soft:
            random.seed(4)
            c.rect(wx, 260, wx + 160, 820, fill=mix(BG, RUG, 0.5))
            for k in range(70):
                x = wx + random.uniform(5, 155)
                y = random.uniform(270, 810)
                c.line([(x, y), (x + random.uniform(-20, 20), y + random.uniform(-20, 20))], mix(BG, RUG, 1.0), 3)
        else:
            c.rect(wx, 260, wx + 160, 820, fill=mix(BG, WALL, 1.0))
        ph = (t * 0.4) % 1
        for k in range(8):
            x = cx - 380 + ((ph * 540 + k * 68) % 540)
            amp = 1.0
            c.line([(x, 420), (x, 660)], mix(BG, SOUND, 0.8), 4)
        c.arrow(cx - 380, 540, wx - 10, 540, SOUND, 6, 18)
        back = 1.0 if not soft else 0.3
        c.arrow(wx - 10, 600, cx - 380, 600, mix(BG, SOUND, back), int(2 + 6 * back), 18)
        if soft and t > 7.2:
            for k in range(5):
                c.text(wx + 80, 330 + k * 110, '热', 'bold', 22, mix(BG, NRED, 0.4 + 0.3 * math.sin(t * 3 + k)), 'mm')
        c.text(cx, 900, lab, 'bold', 28, GREEN if soft else INK, 'mm')
    if t > 14.2:
        c.text(960, 210, '纸箱里放手机播放：空箱子外 30 厘米量一次，塞满毛巾再量一次（以实测为准）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '硬墙又平又密，声音碰上去几乎原样弹回来'),
                (7.2, 14, '地毯、毛巾里全是小缝，声音钻进去，空气和纤维来回摩擦，一部分变成热'),
                (14.2, 22, '所以软的、多孔的东西吸音好；又硬又重的东西反而把声音弹回来')], y=1010)


OLD51 = [('螺丝与标准件', '64'), ('弹簧秤', '223'), ('电磁铁', '56'), ('电报', '57'), ('LED', '102'), ('红外测温枪', '200'),
         ('电灯', '60'), ('液压刹车', '172'), ('防窥膜', '185'), ('玻璃', '21'), ('空调与热泵', '109'), ('温度计', '46'),
         ('摆钟', '45'), ('压电', '13'), ('变压器与交流电', '75'), ('避雷针', '70'), ('回声测距与雷达', '84'), ('降噪耳机', '106')]
NEW51 = [('弹子锁', '262', ['螺丝与标准件', '弹簧秤']), ('门铃', '263', ['电磁铁', '电报']), ('遥控器', '264', ['LED', '红外测温枪']),
         ('调光台灯', '265', ['电灯', 'LED']), ('闭门器', '266', ['液压刹车', '弹簧秤']), ('百叶窗', '267', ['防窥膜', '玻璃']),
         ('暖气片', '268', ['空调与热泵', '温度计']), ('石英钟', '269', ['摆钟', '压电']), ('三孔插头', '270', ['变压器与交流电', '避雷针']),
         ('地毯吸音', '271', ['回声测距与雷达', '降噪耳机'])]


def s51_layer(c, t, i):
    corner_tag(c, '第五十一季特辑 · 第二十二层')
    c.text(60, 118, '第二十二层：门厅与客厅', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD51):
        pos[name] = (340, 214 + k * 38)
    for k, (name, num, deps) in enumerate(NEW51):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 178, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第五十一季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW51):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD51:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 5 else 17, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW51):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 19, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第二十二层的十集：门厅和客厅里的东西'),
                (8.2, 16, '标准件和弹簧长出弹子锁，电磁铁长出门铃，LED 长出遥控器和调光台灯，液压刹车长出闭门器'),
                (16.2, 24, '防窥膜长出百叶窗，空调长出暖气片，摆钟和压电长出石英钟，交流电和避雷针长出三孔插头'),
                (24.2, 30, '最后，回声测距和降噪耳机一起，长出了地毯吸音')], y=1040)


CLIPS = {
 'E271_回声': (e271_echo, 22), 'E271_纤维': (e271_pores, 22),
 'E271_片头': (titles.opening(SER51, VOL51, S51A, 9, '录音棚的墙上贴满吸音棉'), 7),
 'E271_片尾': (titles.closing(SER51, VOL51, S51A, 9, '下集：第五十一季特辑 · 第二十二层回顾'), 7),
 'S51_第二十二层': (s51_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
