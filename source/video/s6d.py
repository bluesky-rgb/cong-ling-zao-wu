"""第六季收尾：B18 张衡地动仪、第六季特辑 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER, BVOL
from s6a import S6A, SB6, SER6, VOL6, BRONZE, GREEN, seg

def ground_x(t):
    """earthquake shaking of the ground (left-right), starts at t=3"""
    if t < 3: return 0.0
    tt = t - 3
    return 40 * math.exp(-0.25 * tt) * math.sin(9 * tt)

# ---------------------------------------------------------------- B18 地动仪
def b18_inertia(c, t, i):
    corner_tag(c, 'B18 · 惯性')
    c.text(60, 96, '地面晃了，挂着的重锤为什么几乎不动？', 'serif', 40, INK)
    gx = ground_x(t)
    # ground
    c.rect(0, 840, 1920, 880, fill=mix(BG, MUTED, 0.6))
    c.text(1860, 900, '地面', 'sans', 24, MUTED, 'rm')
    # frame box moves with ground
    bx = 960 + gx
    c.rect(bx - 260, 260, bx + 260, 840, outline=BRONZE, width=8, r=10)
    c.line([(bx - 260, 280), (bx + 260, 280)], BRONZE, 8)
    # pendulum: hangs from frame top, mass lags (inertia) -> stays near 960
    mass_x = 960 + gx * 0.08
    c.line([(bx, 280), (mass_x, 700)], (200, 200, 205), 4)
    c.ellipse(mass_x, 700, 46, 46, fill=COPPER)
    # relative displacement arrow
    rel = mass_x - bx
    if abs(rel) > 4:
        c.arrow(bx, 790, bx + rel * 2.5, 790, NRED, 5, 14)
    c.text(bx, 920, '框架跟着地面动', 'sans', 24, BRONZE, 'mm')
    c.text(mass_x + 70, 700, '重锤：「懒得」动', 'sans', 26, COPPER, 'lm')
    a = fade(t, 10, 11)
    c.rect(1380, 280, 1880, 560, fill=mix(BG, SHEET, a), r=14)
    c.text(1410, 330, '重锤和框架之间', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1410, 380, '出现了相对移动（红箭头）', 'sans', 26, mix(BG, NRED, a), 'lm')
    c.text(1410, 450, '让这一点点移动去推开机关，', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1410, 500, '就能「记录」到地动', 'bold', 28, mix(BG, SPARK, a), 'lm')
    caps(c, t, [(0, 3, '一个框子里挂着一个沉重的锤'),
                (3.2, 10, '地面突然左右晃：框子跟着地面一起动，重锤因为惯性，几乎留在原地'),
                (10.2, 22, '重锤和框子之间的这点相对移动，就是所有地震仪的起点')], y=1010)

DRAGONS = 8

def vessel(c, cx, cy, R, drop=-1, prog=0.0):
    c.ellipse(cx, cy, R, R, fill=mix(BG, BRONZE, 0.75), outline=BRONZE, width=6)
    for k in range(DRAGONS):
        ang = -math.pi / 2 + k * 2 * math.pi / DRAGONS
        dx, dy = cx + (R + 30) * math.cos(ang), cy + (R + 30) * math.sin(ang)
        c.ellipse(dx, dy, 22, 22, fill=GREEN)
        bx, by = cx + (R + 60) * math.cos(ang), cy + (R + 60) * math.sin(ang)
        if k == drop:
            bx, by = cx + (R + 60 + 60 * prog) * math.cos(ang), cy + (R + 60 + 60 * prog) * math.sin(ang)
        c.ellipse(bx, by, 12, 12, fill=SPARK)
        tx, ty = cx + (R + 130) * math.cos(ang), cy + (R + 130) * math.sin(ang)
        c.ellipse(tx, ty, 26, 18, fill=(110, 140, 90))

def b18_models(c, t, i):
    corner_tag(c, 'B18 · 复原方案')
    c.text(60, 96, '「中有都柱」：柱子怎么装？两种思路', 'serif', 40, INK)
    for k, (cx, title, lines) in enumerate([(520, '思路一：直立的柱（倒立摆）', ['柱子立在中间，一晃就倒', '倒向哪边，就推开哪边的机关', '问题：倒的方向未必对着震源']),
                                            (1400, '思路二：悬挂的柱（悬垂摆）', ['柱子从上面吊下来', '地面晃，柱子和外壳相对移动', '推动对应方向的机关，吐出铜丸'])]):
        a = fade(t, 0.5 + k * 8, 1.5 + k * 8)
        if a <= 0: continue
        c.rect(cx - 400, 170, cx + 400, 870, fill=mix(BG, SHEET, a), r=16)
        c.text(cx, 220, title, 'bold', 30, mix(BG, INK, a), 'mm')
        vx, vy = cx, 470
        c.rect(vx - 150, vy - 150, vx + 150, vy + 150, outline=mix(BG, BRONZE, a), width=6, r=40)
        sway = ground_x(t - k * 8)
        if k == 0:
            fall = fade(t, 4, 6)
            ang = -fall * 0.9
            top = (vx + 120 * math.sin(ang), vy + 120 - 240 * math.cos(ang) * 1)
            c.line([(vx, vy + 120), (vx + 190 * math.sin(ang), vy + 120 - 190 * math.cos(ang))], mix(BG, COPPER, a), 16)
        else:
            mx = vx + sway * 0.1
            c.line([(vx + sway, vy - 140), (mx, vy + 90)], mix(BG, (200, 200, 205), a), 5)
            c.ellipse(mx, vy + 90, 34, 34, fill=mix(BG, COPPER, a))
            c.arrow(vx - 230, vy + 170, vx - 230 + sway * 2, vy + 170, mix(BG, NRED, a), 4, 12)
        for j, s_ in enumerate(lines):
            c.text(cx - 340, 690 + j * 50, s_, 'sans', 26, mix(BG, INK if j < 2 else (NRED if k == 0 else GREEN), a), 'lm')
    b = fade(t, 16, 17)
    c.rect(300, 900, 1620, 970, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 935, '原物没有留下，记载只有一两百字：两种都是复原方案，都还有争议', 'bold', 26, mix(BG, SPARK, b), 'mm')
    caps(c, t, [(0, 8, '20 世纪的复原曾用直立的柱子：一震就倒，倒向哪边吐哪颗丸'),
                (8.2, 16, '后来的复原改成悬挂的柱子：外壳跟地动，柱子凭惯性不动，二者的相对移动推开机关'),
                (16.2, 22, '能不能测出远方地震的方向？今天仍有争议')], y=1035)

# ---------------------------------------------------------------- 第六季特辑：量和记
ITEMS6 = [('时间', '摆钟', '45'), ('声音', '一钟双音', 'B11'), ('振动', '鱼洗', 'B9'), ('温度', '温度计', '46'),
          ('距离', '影子测地球', '47'), ('光', '透光镜', 'B10'), ('数', '数字与 0', '48'), ('账', '复式记账', '49'),
          ('消息', '光学电报', '50'), ('地动', '地动仪', 'B18')]

def s6_measure(c, t, i):
    corner_tag(c, '第六季特辑 · 量和记')
    c.text(60, 110, '第六季：量和记', 'serif', 48, INK, 'lm')
    for k, (what, name, num) in enumerate(ITEMS6):
        col, row = k % 5, k // 5
        cx, cy = 260 + col * 350, 360 + row * 320
        a = fade(t, 1 + k * 1.8, 2 + k * 1.8)
        accent = COPPER if num[0].isdigit() else FIELD
        c.rect(cx - 150, cy - 120, cx + 150, cy + 120, fill=mix(BG, SHEET, a), outline=mix(BG, accent, a), width=3, r=16)
        c.text(cx, cy - 40, what, 'serif', 56, mix(BG, accent, a), 'mm')
        c.text(cx, cy + 40, name, 'bold', 28, mix(BG, INK, a), 'mm')
        c.text(cx, cy + 85, num, 'mono', 22, mix(BG, MUTED, a), 'mm')
    c.text(960, 940, '铜色：A 线 · 穿越造物　　蓝色：B 线 · 古法解密', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 10, '第六季的十集，都在回答一件事：怎样把世界「量」出来、「记」下来'),
                (10.2, 19, '时间、声音、温度、地球的大小；数字、账目、消息，还有大地的震动'),
                (19.2, 28, '会量、会记，所有技术才有了地基')], y=1010)

CLIPS = {
 'B18_惯性': (b18_inertia, 22), 'B18_复原方案': (b18_models, 22),
 'B18_片头': (titles.opening(BSER, BVOL, SB6, 3, '东汉 · 公元 132 年 · 张衡'), 7),
 'B18_片尾': (titles.closing(BSER, BVOL, SB6, 3, '下集：第六季特辑'), 7),
 'S6_量和记': (s6_measure, 28),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
