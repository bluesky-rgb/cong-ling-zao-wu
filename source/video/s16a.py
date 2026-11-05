"""第十六季（古法解密 5.0：玩、算、吃、用）第一批：B50 陀螺、B51 不倒翁、B52 秋千 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB16 = [('B50', '陀螺'), ('B51', '不倒翁'), ('B52', '秋千'), ('B53', '筷子'), ('B54', '算盘'),
        ('B55', '九连环'), ('B56', '扇车'), ('B57', '蒸笼'), ('B58', '油纸伞'), ('B59', '曲辕犁')]
VOL16 = '第十六季 · 古法解密 5.0'
WOOD = (175, 125, 75)
COIN = (220, 180, 80)
ROPE = (190, 170, 130)

# ---------------------------------------------------------------- B50 陀螺
def top_shape(c, x, y, tilt, spin, col, a=1.0):
    ca, sa = math.cos(tilt), math.sin(tilt)
    def p(dx, dy):
        return (x + dx * ca - dy * sa, y + dx * sa + dy * ca)
    body = [p(0, 0), p(-110, -150), p(-120, -170), p(120, -170), p(110, -150)]
    c.poly(body, mix(BG, col, a))
    for k in range(4):
        u = ((spin + k / 4) % 1)
        dx = -110 + 220 * u
        c.line([p(dx, -150), p(dx * 1.05, -168)], mix(BG, mix(col, INK, 0.5), a), 3)
    c.line([p(0, -170), p(0, -240)], mix(BG, WOOD, a), 8)

def b50_spin(c, t, i):
    corner_tag(c, 'B50 · 转起来，就不愿意倒')
    c.text(60, 96, '不转的陀螺一放就倒，转着的陀螺被推也不倒', 'serif', 40, INK)
    # left: not spinning, falls
    fall = min(0.96, max(0, (t - 2) * 0.8))
    top_shape(c, 480, 800, fall, 0, MUTED)
    c.text(480, 900, '不转：一放就倒', 'bold', 28, INK, 'mm')
    # right: spinning, precessing
    prec = math.radians(15) * math.sin(t * 1.2)
    top_shape(c, 1400, 800, prec, t * 3, WOOD)
    c.text(1400, 900, '转着：慢慢绕圈，就是不倒', 'bold', 28, INK, 'mm')
    c.line([(200, 802), (1800, 802)], LINE, 2)
    a = fade(t, 9, 10)
    c.arc(1400, 560, 200, 40, 200, 340, mix(BG, SPARK, a), 3)
    c.text(1400, 480, '进动：轴在慢慢画圈', 'sans', 24, mix(BG, SPARK, a), 'mm')
    caps(c, t, [(0, 6, '同一个陀螺：不转的时候，尖头根本立不住'),
                (6.2, 13, '转起来以后，重力想把它拉倒，它却只是慢慢绕着画圈'),
                (13.2, 22, '转动的东西会「记住」自己的方向：这叫角动量守恒。自行车骑起来不倒，也有它的功劳')], y=1010)

def b50_inertia(c, t, i):
    corner_tag(c, 'B50 · 重量放在哪里')
    c.text(60, 96, '一样重的陀螺，硬币贴在边上转得更久', 'serif', 40, INK)
    for k, (nm, rr, sec) in enumerate([('硬币贴中间', 40, 0.55), ('硬币贴边缘', 190, 1.0)]):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        cx, cy = 520 + k * 880, 420
        c.ellipse(cx, cy, 230, 230, fill=mix(BG, (200, 190, 170), a), outline=mix(BG, WOOD, a), width=4)
        ang = t * (4 + 2 * k)
        for j in range(4):
            q = ang + j * math.pi / 2
            c.ellipse(cx + rr * math.cos(q), cy + rr * math.sin(q), 26, 26, fill=mix(BG, COIN, a))
        c.ellipse(cx, cy, 10, 10, fill=mix(BG, INK, a))
        c.text(cx, cy + 290, nm, 'bold', 28, mix(BG, INK, a), 'mm')
        h = 200 * sec * fade(t, 2 + k * 4, 4 + k * 4)
        c.rect(cx - 70, 960 - h, cx + 70, 960, fill=mix(BG, GREEN if k else MUTED, a), r=6)
    c.text(960, 940, '转的时间（示意，以实测为准）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '同样四枚硬币：一个陀螺贴在中间，一个贴在边缘'),
                (7.2, 14, '贴在边缘的，同样用力拧，转得慢一点，却转得久得多'),
                (14.2, 22, '重量离轴越远，转动惯量越大，越难停下来：飞轮、溜冰的人收臂张臂，都是这个道理')], y=1010)

# ---------------------------------------------------------------- B51 不倒翁
def roly(c, cx, cy, R, tilt, gh, col, a=1.0, show=True):
    # body: circle bottom + head
    ca, sa = math.cos(tilt), math.sin(tilt)
    bx = cx - R * tilt  # rolls on ground
    by = cy
    c.ellipse(bx, by, R, R, fill=mix(BG, col, a))
    hx, hy = bx + 1.4 * R * math.sin(tilt), by - 1.4 * R * math.cos(tilt)
    c.ellipse(hx, hy, R * 0.55, R * 0.55, fill=mix(BG, col, a))
    gx, gy = bx + gh * math.sin(tilt), by - gh * math.cos(tilt)
    if show:
        c.ellipse(bx, by, 8, 8, fill=mix(BG, INK, a))
        c.ellipse(gx, gy, 14, 14, fill=mix(BG, NRED, a))
    return bx, by, gx, gy

def b51_cg(c, t, i):
    corner_tag(c, 'B51 · 重心比圆心低')
    c.text(60, 96, '推歪了，重心被抬高：它只好自己回来', 'serif', 40, INK)
    tilt = 0.5 * math.sin(t * 1.6) * math.exp(-max(0, t - 6) * 0.15)
    R = 170
    bx, by, gx, gy = roly(c, 760, 760, R, tilt, -0.55 * R, (200, 120, 90))
    c.line([(200, by + R), (1400, by + R)], LINE, 3)
    c.line([(gx, gy), (gx, by + R)], mix(BG, NRED, 0.7), 2)
    c.ellipse(bx + R * tilt * 0, by + R, 8, 8, fill=GREEN)
    a = fade(t, 4, 5)
    c.rect(1420, 300, 1860, 600, fill=mix(BG, SHEET, a), r=12)
    c.text(1450, 350, '白点：圆底的圆心', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1450, 400, '红点：重心（底部加了重物）', 'sans', 24, mix(BG, NRED, a), 'lm')
    c.text(1450, 470, '重心在圆心下面：', 'bold', 26, mix(BG, INK, a), 'lm')
    c.text(1450, 515, '往哪边歪，重力都把它拉回', 'bold', 26, mix(BG, INK, a), 'lm')
    c.text(1450, 560, '最低的那个位置', 'bold', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '不倒翁的底是圆的，里面最下面压着一块重物'),
                (6.2, 13, '推歪它，重心反而被抬高了一点；松手，重力把重心拉回最低处'),
                (13.2, 22, '东西总是往重心最低的位置待：这叫稳定平衡。唐代劝酒用的「酒胡子」就是这么做的（拍摄前核对）')], y=1010)

def b51_limit(c, t, i):
    corner_tag(c, 'B51 · 重心太高就倒了')
    c.text(60, 96, '把重物往上挪：过了圆心，它就站不起来', 'serif', 40, INK)
    cases = [('重心很低', -0.6, GREEN, '一推就回来'), ('重心在圆心', 0.0, SPARK, '推到哪停在哪'), ('重心高过圆心', 0.5, NRED, '一推就倒')]
    for k, (nm, g, col, note) in enumerate(cases):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        cx = 360 + k * 600
        prog = fade(t, 2 + k * 4, 4 + k * 4)
        if g < 0:
            tilt = 0.4 * math.sin((t - 2 - k * 4) * 3) * (1 - prog * 0.8) if t > 2 + k * 4 else 0
        elif g == 0:
            tilt = 0.35 * prog
        else:
            tilt = 1.2 * prog
        R = 120
        bx, by, gx, gy = roly(c, cx, 640, R, tilt, g * R, (200, 120, 90), a)
        c.line([(cx - 260, by + R), (cx + 260, by + R)], mix(BG, LINE, a), 2)
        c.text(cx, 260, nm, 'bold', 30, mix(BG, col, a), 'mm')
        c.text(cx, 860, note, 'sans', 26, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 7, '同一个蛋壳，把橡皮泥一点点往上挪'),
                (7.2, 14, '重心正好在圆心：推到哪就停在哪，不回来也不倒'),
                (14.2, 22, '再往上：一推，重心越倒越低，它就躺下了。不倒翁的秘密只有一句：重心要比圆心低')], y=1010)

# ---------------------------------------------------------------- B52 秋千
def pumped(n, t, pump=True):
    # swing with length modulation: shorten at the bottom, lengthen at the turning points
    L0, dL, g = 1.0, 0.05, 9.8
    th, w = 0.2, 0.0
    dt = 0.01
    short = False
    out = []
    for k in range(int(t / dt)):
        L = L0 - (dL if short else 0)
        w += -g / L * math.sin(th) * dt
        prev = th
        th += w * dt
        if pump:
            if not short and prev * th <= 0:
                w *= (L0 / (L0 - dL)) ** 2; short = True
            elif short and abs(w) < 0.05:
                w *= ((L0 - dL) / L0) ** 2; short = False
        out.append((th, short))
    return out

PUMP = pumped(1, 24.0, True)
FREE = pumped(1, 24.0, False)

def b52_pump(c, t, i):
    corner_tag(c, 'B52 · 低处拉短，高处放长')
    c.text(60, 96, '每一趟都送进去一点点能量', 'serif', 40, INK)
    k = min(len(PUMP) - 1, int(t / 0.01 * 0.6))
    for j, (arr, nm, cx, col) in enumerate(((FREE, '不动：摆幅不变', 520, MUTED), (PUMP, '低处拉短、高处放长：越荡越高', 1400, GREEN))):
        th, sh = arr[k]
        L = 420 - (50 if sh else 0)
        px, py = cx, 220
        bx, by = px + L * math.sin(th), py + L * math.cos(th)
        c.ellipse(px, py, 10, 10, fill=INK)
        c.line([(px, py), (bx, by)], ROPE, 4)
        c.ellipse(bx, by, 34, 34, fill=col)
        c.text(cx, 760, nm, 'bold', 28, INK, 'mm')
        amp = max(abs(x[0]) for x in arr[max(0, k - 300):k + 1]) if k > 0 else 0.15
        c.text(cx, 810, f'摆幅约 {math.degrees(amp):.0f}°', 'mono', 26, col, 'mm')
    a = fade(t, 12, 13)
    c.rect(300, 860, 1620, 930, fill=mix(BG, SHEET, a), r=10)
    c.text(960, 895, '在最低处把绳子拉短，人对摆做了功；在最高处放长，几乎不花力气（数值示意）', 'sans', 24, mix(BG, INK, a), 'mm')
    caps(c, t, [(0, 6, '左边的摆什么都不做，右边的摆在最低点把绳子拉短、最高点放长'),
                (6.2, 13, '几趟下来，右边越荡越高：这叫参数共振，按对节拍改变「摆长」，就能送进能量'),
                (13.2, 22, '荡秋千的人在最低处站起、最高处蹲下，做的正是同一件事：重心一高一低，就是摆长一短一长')], y=1040)

def b52_stand(c, t, i):
    corner_tag(c, 'B52 · 时机最重要')
    c.text(60, 96, '同样的站和蹲，时机反了，秋千就会停下来', 'serif', 40, INK)
    rows = [('最低点站起、最高点蹲下', '每趟都加一点能量', GREEN, 1.0), ('乱蹬，时机随便', '有时加有时减，基本不变', SPARK, 0.0), ('最低点蹲下、最高点站起', '每趟都减一点：越荡越低', NRED, -1.0)]
    for k, (nm, note, col, sgn) in enumerate(rows):
        a = fade(t, 1 + k * 4, 2 + k * 4)
        if a <= 0: continue
        y = 300 + k * 200
        c.text(160, y - 40, nm, 'bold', 28, mix(BG, INK, a), 'lm')
        c.text(160, y + 10, note, 'sans', 24, mix(BG, col, a), 'lm')
        pts = []
        for j in range(301):
            x = j / 300
            env = 1 + 0.8 * sgn * x
            pts.append((900 + x * 900, y - 50 * env * math.sin(x * 2 * math.pi * 6) * min(1, fade(t, 1.5 + k * 4, 4 + k * 4) * 3)))
        c.line(pts, mix(BG, col, a), 3)
    caps(c, t, [(0, 6, '站起来，重心升高，相当于把摆长缩短'),
                (6.2, 13, '在最低点站起来最划算：这时绳子拉力最大，你做的功也最多'),
                (13.2, 22, '时机反过来，就是在给秋千「刹车」。秋千在中国至少有两千多年历史（拍摄前核对）')], y=1010)

CLIPS = {
 'B50_角动量': (b50_spin, 22), 'B50_转动惯量': (b50_inertia, 22),
 'B50_片头': (titles.opening(BSER, VOL16, SB16, 0, '新石器时代木陀螺 · 宋代「千千」'), 7),
 'B50_片尾': (titles.closing(BSER, VOL16, SB16, 0, '下集：不倒翁为什么推不倒？'), 7),
 'B51_重心': (b51_cg, 22), 'B51_临界': (b51_limit, 22),
 'B51_片头': (titles.opening(BSER, VOL16, SB16, 1, '唐 · 劝酒的「酒胡子」'), 7),
 'B51_片尾': (titles.closing(BSER, VOL16, SB16, 1, '下集：不用人推，秋千怎么越荡越高？'), 7),
 'B52_参数共振': (b52_pump, 22), 'B52_站蹲': (b52_stand, 22),
 'B52_片头': (titles.opening(BSER, VOL16, SB16, 2, '先秦 · 秋千'), 7),
 'B52_片尾': (titles.closing(BSER, VOL16, SB16, 2, '下集：两根小棍，为什么能夹起一颗花生？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
