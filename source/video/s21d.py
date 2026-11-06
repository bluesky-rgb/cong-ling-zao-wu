"""第二十一季（第七层）收尾：E121 太空望远镜、第二十一季特辑（第七层回顾） —— 动画与片头片尾。"""
import math, random, sys, colorsys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s21a import S21A, SER21, VOL21

STAR = (250, 240, 200)
AIRC = (90, 140, 200)
IRC = (200, 80, 70)
DUST = (120, 95, 80)
GOLD = (220, 180, 80)

# ---------------------------------------------------------------- E121 太空望远镜
def _scope(c, x, y, s=1.0, col=(170, 175, 185)):
    c.rect(x - 22 * s, y - 70 * s, x + 22 * s, y + 10 * s, fill=col, r=6)
    c.line([(x, y + 10 * s), (x - 30 * s, y + 60 * s)], MUTED, 4)
    c.line([(x, y + 10 * s), (x + 30 * s, y + 60 * s)], MUTED, 4)

def e121_twinkle(c, t, i):
    corner_tag(c, '第 121 集 · 星星为什么一闪一闪')
    c.text(60, 96, '星光穿过几十公里乱流的空气，被推来推去：地面看「闪」，太空看不闪', 'serif', 40, INK)
    sx = 640
    c.ellipse(sx, 200, 10, 10, fill=STAR)
    c.text(sx + 24, 200, '一颗星', 'sans', 20, MUTED, 'lm')
    top, bot = 380, 720
    for k in range(9):
        y = top + k * (bot - top) / 8
        pts = [(80 + j * 20, y + 10 * math.sin(j * 0.35 + t * 2.4 + k * 1.3)) for j in range(60)]
        c.line(pts, mix(BG, AIRC, 0.35 + 0.05 * (k % 3)), 3)
    c.text(90, top - 30, '大气：冷热不匀的空气在翻滚', 'sans', 22, AIRC, 'lm')
    x = sx
    pts = [(sx, 210), (sx, top)]
    for k in range(1, 9):
        y = top + k * (bot - top) / 8
        x += 16 * math.sin(t * 3.1 + k * 1.7) * math.sin(t * 1.3 + k)
        pts.append((x, y))
    pts.append((x, 800))
    c.line(pts, STAR, 3)
    _scope(c, sx, 870, 1.0)
    c.rect(1180, 300, 1840, 880, fill=SHEET, r=14)
    c.text(1510, 340, '望远镜里看到的这颗星', 'bold', 26, INK, 'mm')
    for k, (nm, jit) in enumerate((('地面', 1.0), ('太空', 0.0))):
        cx, cy = 1350 + k * 320, 580
        c.ellipse(cx, cy, 120, 120, fill=(10, 14, 22), outline=LINE, width=2)
        dx = jit * 26 * math.sin(t * 3.1) * math.sin(t * 1.9 + 1)
        dy = jit * 22 * math.cos(t * 2.7)
        br = 1.0 - jit * 0.5 * (0.5 + 0.5 * math.sin(t * 5.3))
        r = 8 + jit * 10 * (0.5 + 0.5 * math.sin(t * 4.1))
        c.ellipse(cx + dx, cy + dy, r, r, fill=mix((10, 14, 22), STAR, br))
        c.text(cx, cy + 160, nm, 'bold', 26, INK, 'mm')
        c.text(cx, cy + 200, '晃、忽明忽暗' if jit else '一个稳稳的小点', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '星光走了几千年，最后几十公里要穿过地球的大气'),
                (7.2, 14, '空气冷一块、热一块，还在不停翻滚；光每穿过一块就被推歪一点，星星就一闪一闪'),
                (14.2, 22, '把望远镜送到大气外面，光直直进来：哈勃看到的星，是一个稳稳的小点')], y=1010)

def e121_infrared(c, t, i):
    corner_tag(c, '第 121 集 · 看不见的红外')
    c.text(60, 96, '红外光人眼看不见，却能穿过挡住可见光的尘埃云', 'serif', 40, INK)
    x0, x1, y = 160, 1760, 290
    for k in range(200):
        u = k / 199
        if u < 0.42:
            r, g, b = colorsys.hsv_to_rgb(0.78 * (1 - u / 0.42), 0.75, 0.95)
            col = (int(r * 255), int(g * 255), int(b * 255))
        else:
            col = mix((60, 30, 30), (30, 20, 20), (u - 0.42) / 0.58)
        xx = x0 + (x1 - x0) * u
        c.rect(xx, y - 30, xx + (x1 - x0) / 199 + 1, y + 30, fill=col)
    c.text(x0 + (x1 - x0) * 0.21, y + 60, '可见光（人眼）', 'bold', 22, INK, 'mm')
    c.text(x0 + (x1 - x0) * 0.71, y + 60, '红外（遥控器、韦布望远镜）', 'bold', 22, IRC, 'mm')
    c.text(x0, y - 50, '0.4 微米', 'mono', 18, MUTED, 'lm')
    c.text(x0 + (x1 - x0) * 0.42, y - 50, '0.7 微米', 'mono', 18, MUTED, 'mm')
    c.text(x1, y - 50, '约 28 微米', 'mono', 18, MUTED, 'rm')
    cy = 640
    c.ellipse(260, cy, 50, 50, fill=STAR)
    c.text(260, cy + 80, '尘埃里的新恒星', 'sans', 20, MUTED, 'mm')
    rnd = random.Random(3)
    for k in range(70):
        dx, dy = rnd.uniform(-170, 170), rnd.uniform(-170, 170)
        if dx * dx + dy * dy < 170 * 170:
            c.ellipse(760 + dx, cy + dy, 14, 14, fill=mix(BG, DUST, 0.8))
    c.text(760, cy + 200, '尘埃云', 'sans', 22, MUTED, 'mm')
    for k in range(3):
        yy = cy - 60 + k * 60
        s = (t * 0.35 + k * 0.33) % 1
        xv = 320 + 900 * s
        xe = min(xv, 640)
        c.line([(320, yy - 14), (xe, yy - 14)], (90, 200, 110), 3)
        if xv > 640:
            c.ellipse(640, yy - 14, 8, 8, fill=mix(BG, (90, 200, 110), 0.5))
        c.line([(320, yy + 14), (min(xv, 1480), yy + 14)], IRC, 3)
    c.text(560, cy - 150, '可见光：被挡住', 'sans', 22, (90, 200, 110), 'mm')
    c.text(1150, cy - 150, '红外：穿过去', 'sans', 22, IRC, 'mm')
    for (q, r_) in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]:
        hx = 1600 + 46 * 1.5 * q
        hy = cy + 46 * math.sqrt(3) * (r_ + q / 2)
        c.poly([(hx + 42 * math.cos(b * math.pi / 3), hy + 42 * math.sin(b * math.pi / 3)) for b in range(6)], mix(GOLD, (255, 230, 150), 0.3 * ((q + r_) % 2)))
    c.text(1600, cy + 170, '韦布：18 块镀金六边形镜片拼成（示意）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '彩虹红色的外面，还有人眼看不见的光：红外。电视遥控器就是用它发信号的'),
                (7.2, 14, '新恒星常常藏在尘埃云里，可见光被挡住了，红外却能穿出来'),
                (14.2, 22, '可大气里的水汽会吸收大部分红外，所以韦布望远镜也去了太空，离地球约 150 万公里（拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- 第二十一季特辑
OLD21 = [('无线电', '76'), ('互联网', '98'), ('触摸屏', '96'), ('显微镜', '53'), ('LED', '102'), ('数码相机', '95'),
         ('陀螺仪', '108'), ('电动汽车', '107'), ('摩擦起电', '01'), ('松烟墨', 'B32'), ('照相', '55'), ('透镜', '52'),
         ('计算机', '91'), ('二维码', '97'), ('蒸汽发电', '10'), ('手摇发电机', '05'), ('望远镜', '54'), ('人造卫星', '101')]
NEW21 = [('手机信号', '112', ['无线电', '互联网']), ('指纹识别', '113', ['触摸屏', '显微镜']), ('心率手环', '114', ['LED', '数码相机']),
         ('平衡车', '115', ['陀螺仪', '电动汽车']), ('电子墨水屏', '116', ['触摸屏', '摩擦起电']), ('石墨烯', '117', ['LED', '松烟墨']),
         ('虚拟现实', '118', ['照相', '透镜']), ('加密', '119', ['计算机', '二维码']),
         ('核电站', '120', ['蒸汽发电', '手摇发电机']), ('太空望远镜', '121', ['望远镜', '人造卫星'])]

def s21_layer(c, t, i):
    corner_tag(c, '第二十一季特辑 · 第七层')
    c.text(60, 118, '第七层：身边的未来', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD21):
        pos[name] = (340, 200 + k * 44)
    for k, (name, num, deps) in enumerate(NEW21):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第二十一季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW21):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD21:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW21):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第七层的十集：都是口袋里、手腕上、新闻里的东西'),
                (8.2, 16, '无线电和互联网长出手机信号，触摸屏和显微镜长出指纹识别，LED 和相机长出心率手环'),
                (16.2, 24, '陀螺仪加电机站稳了平衡车；一块铅笔芯剥出石墨烯；照相加透镜，长出虚拟现实'),
                (24.2, 30, '计算机给信息上锁，蒸汽发电接上原子核，望远镜坐上卫星飞出大气')], y=1040)


CLIPS = {
 'E121_闪烁': (e121_twinkle, 22), 'E121_红外': (e121_infrared, 22),
 'E121_片头': (titles.opening(SER21, VOL21, S21A, 9, '1990 年哈勃 · 2021 年韦布'), 7),
 'E121_片尾': (titles.closing(SER21, VOL21, S21A, 9, '下集：第二十一季特辑 · 第七层回顾'), 7),
 'S21_第七层': (s21_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
