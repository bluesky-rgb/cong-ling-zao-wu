"""第二十八季（古法解密 11.0：桶、绳、戏、窗）第三批：B116 提线木偶、B117 骰子、B118 画押 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s28a import SB28, VOL28, WOOD, DARKWOOD, SKIN, ROPE

PUPPET = (220, 140, 110)
STRINGC = (230, 230, 230)
DIE = (240, 240, 235)
INKRED = (200, 60, 60)
RIDGE = (60, 50, 50)


# ---------------------------------------------------------------- B116 提线木偶
def _puppet(c, cx, top, tilt, scale=1.0):
    """十字控制板绕中心倾斜 tilt（弧度）；返回各线挂点。"""
    bar = 220 * scale
    ca, sa = math.cos(tilt), math.sin(tilt)
    L = (cx - bar * ca, top - bar * sa)
    Rr = (cx + bar * ca, top + bar * sa)
    c.line([L, Rr], WOOD, 12)
    c.line([(cx, top - 30), (cx, top + 30)], WOOD, 12)
    c.ellipse(cx, top, 10, 10, fill=DARKWOOD)
    body_top = top + 380 * scale
    c.line([(cx, top), (cx, body_top - 60 * scale)], STRINGC, 2)
    c.ellipse(cx, body_top - 30 * scale, 32 * scale, 32 * scale, fill=SKIN)
    c.rect(cx - 40 * scale, body_top, cx + 40 * scale, body_top + 160 * scale, fill=PUPPET, r=10)
    arms = []
    for side, P in ((-1, L), (1, Rr)):
        sh = (cx + side * 40 * scale, body_top + 20 * scale)
        string_len = 380 * scale
        hand_y = P[1] + string_len
        dy = max(-200 * scale, min(150 * scale, hand_y - (sh[1] + 140 * scale)))
        hand = (sh[0] + side * 70 * scale, sh[1] + 140 * scale + dy)
        c.line([sh, hand], PUPPET, int(14 * scale))
        c.ellipse(hand[0], hand[1], 12 * scale, 12 * scale, fill=SKIN)
        c.line([P, hand], STRINGC, 2)
        arms.append(hand)
    c.line([(cx - 20 * scale, body_top + 160 * scale), (cx - 30 * scale, body_top + 300 * scale)], PUPPET, int(14 * scale))
    c.line([(cx + 20 * scale, body_top + 160 * scale), (cx + 30 * scale, body_top + 300 * scale)], PUPPET, int(14 * scale))
    return arms


def b116_bar(c, t, i):
    corner_tag(c, 'B116 · 十字板一歪，一边收、一边放')
    c.text(60, 96, '两只手的线拴在横杆两头：横杆绕中间一歪，一头抬高、一头放低，木偶就一只手举起、另一只手落下', 'serif', 38, INK)
    tilt = math.radians(28) * math.sin(t * 0.8)
    _puppet(c, 760, 330, tilt, 0.8)
    c.rect(1300, 260, 1860, 640, fill=SHEET, r=14)
    c.text(1580, 300, '控制板倾斜', 'bold', 24, INK, 'mm')
    c.text(1580, 370, f'{math.degrees(tilt):+.0f}°', 'mono', 36, SPARK, 'mm')
    c.text(1580, 440, '横杆半长 × sin(角度)', 'sans', 20, INK, 'mm')
    c.text(1580, 480, f'＝ 手抬高约 {abs(11 * math.sin(tilt)):.1f} 厘米', 'mono', 22, GREEN, 'mm')
    c.text(1580, 540, '（横杆半长 11 厘米，示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '提线木偶的线不是一根根单独拉的，而是都拴在操偶人手里的一块十字木板上'),
                (7.2, 14, '横杆两头拴着两只手：横杆绕中点一歪，就像跷跷板，一头抬起、一头落下'),
                (14.2, 22, '拴得离中点越远，同样歪一下，手动得越多：一只手腕，就管住了两只胳膊（示意）')], y=1010)


def b116_link(c, t, i):
    corner_tag(c, 'B116 · 一个动作，几根线一起动')
    c.text(60, 96, '控制板前后点一下：头线被拉、腿线跟着变，木偶就点头迈步；拴点的远近，决定每个部位动多少', 'serif', 38, INK)
    for k, (lab, d) in enumerate((('拴在离中点 5 厘米', 5), ('拴在离中点 11 厘米', 11))):
        x0 = 380 + k * 760
        ang = math.radians(25) * math.sin(t * 0.9)
        c.text(x0, 220, lab, 'bold', 24, INK, 'mm')
        Lb = 330
        c.line([(x0 - Lb * math.cos(ang), 380 - Lb * math.sin(ang)), (x0 + Lb * math.cos(ang), 380 + Lb * math.sin(ang))], WOOD, 12)
        c.ellipse(x0, 380, 10, 10, fill=DARKWOOD)
        px = x0 + d * 27 * math.cos(ang)
        py = 380 + d * 27 * math.sin(ang)
        c.ellipse(px, py, 8, 8, fill=SPARK)
        hy = py + 380
        c.line([(px, py), (px, hy)], STRINGC, 2)
        c.ellipse(px, hy, 20, 20, fill=SKIN)
        base = 380 + 380
        seg(c, [(x0 - 120, base), (x0 + 380, base)], LINE, 1)
        c.text(px + 50, hy, f'{(base - hy) / 27:+.1f} 厘米', 'mono', 22, GREEN, 'lm')
    caps(c, t, [(0, 7, '同样把控制板歪 25°：拴在离中点近的线只动一点，拴在远处的线动得多'),
                (7.2, 14, '这就是杠杆：离支点越远，同样转一下走得越远'),
                (14.2, 22, '操偶师把头、手、脚的线拴在不同远近，一个手腕的动作就让木偶的几处一起、按不同幅度动起来（示意）')], y=1010)


# ---------------------------------------------------------------- B117 骰子
def _hist(c, x0, y0, w, h, counts, total, col, label):
    c.rect(x0 - 20, y0 - h - 60, x0 + w + 20, y0 + 70, fill=SHEET, r=12)
    c.text(x0 + w / 2, y0 - h - 30, label, 'bold', 22, INK, 'mm')
    exp = total / 6 if total else 0
    mx = max(max(counts), exp, 1)
    bw = w / 6
    for k in range(6):
        hh = h * counts[k] / mx
        c.rect(x0 + k * bw + 8, y0 - hh, x0 + (k + 1) * bw - 8, y0, fill=col, r=4)
        c.text(x0 + (k + 0.5) * bw, y0 + 24, str(k + 1), 'mono', 20, INK, 'mm')
        c.text(x0 + (k + 0.5) * bw, y0 - hh - 16, str(counts[k]), 'mono', 16, MUTED, 'mm')
    if total:
        ye = y0 - h * exp / mx
        seg(c, [(x0, ye), (x0 + w, ye)], SPARK, 2)


def _rolls(seed, n, weights=None):
    rnd = random.Random(seed)
    out = [0] * 6
    for _ in range(n):
        if weights:
            r = rnd.random() * sum(weights)
            acc = 0
            for k, wv in enumerate(weights):
                acc += wv
                if r < acc:
                    out[k] += 1
                    break
        else:
            out[rnd.randrange(6)] += 1
    return out


def b117_law(c, t, i):
    corner_tag(c, 'B117 · 掷得越多，越接近一样多')
    c.text(60, 96, '掷 12 次，各个点数多的多、少的少；掷 120 次、1200 次，每个点数出现的次数，都越来越接近总数的六分之一', 'serif', 36, INK)
    stage = min(3, int(t / 5.5))
    ns = [12, 120, 1200, 12000]
    for k in range(stage + 1):
        n = ns[k]
        x0 = 140 + k * 440
        counts = _rolls(5, n)
        _hist(c, x0, 760, 360, 360, counts, n, mix((120, 160, 220), GREEN, k / 3), f'掷 {n} 次')
        dev = max(abs(cn - n / 6) for cn in counts) / (n / 6)
        c.text(x0 + 180, 870, f'最大偏差 {dev * 100:.0f}%', 'mono', 20, SPARK, 'mm')
    c.text(960, 940, '黄线：理论上每个点数应出现的次数（总数 ÷ 6），数据为电脑模拟', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '每一次掷骰子，谁也猜不准会出几点：单次全凭运气'),
                (7.2, 14, '可掷得越多，每个点数出现的次数就越接近总数的六分之一，偏差越来越小'),
                (14.2, 22, '这叫大数定律：单次不可预测，很多次却非常有规律。赌场、保险公司都靠它算账')], y=1010)


def b117_loaded(c, t, i):
    corner_tag(c, 'B117 · 做了手脚的骰子，掷多了就露馅')
    c.text(60, 96, '在「1」那面贴两枚硬币，那一面变重、总往下躺，对面的「6」就朝上得多；掷几次看不出，掷几百次就一目了然', 'serif', 36, INK)
    n = int(min(600, 6 + t * 30))
    fair = _rolls(11, n)
    loaded = _rolls(12, n, [0.8, 1, 1, 1, 1, 1.25])
    _hist(c, 220, 760, 600, 420, fair, n, (120, 160, 220), f'普通骰子 · {n} 次')
    _hist(c, 1100, 760, 600, 420, loaded, n, (220, 140, 110), f'偏心骰子 · {n} 次')
    c.text(1400, 870, f'「6」出现 {loaded[5]} 次，理论 {n / 6:.0f} 次', 'mono', 22, SPARK, 'mm')
    c.text(960, 940, '偏心程度为示意，电脑模拟；实际偏多少以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '在骰子的一面贴两枚硬币：这一面重了，落下时更容易躺在底下'),
                (7.2, 14, '它对面的点数就更常朝上；掷十几次，偏差淹没在运气里，看不出来'),
                (14.2, 22, '掷到几百次，那一根柱子明显高出一截：两千多年前就有骰子，公平的骰子每一面都要一样（年代拍摄前核对）')], y=1010)


# ---------------------------------------------------------------- B118 画押
def _ridges(c, cx, cy, kind, R=170, col=RIDGE, seed=0):
    rnd = random.Random(seed)
    for k in range(16):
        r = 14 + k * 10
        pts = []
        for j in range(61):
            u = -1 + 2 * j / 60
            x = cx + u * R
            if kind == 'arch':
                y = cy + 120 - k * 16 - 60 * math.exp(-u * u * 3) * (1 - k / 20)
                pts.append((x, y))
            elif kind == 'loop':
                a = math.pi * j / 60
                if k < 9:
                    xx = cx - 30 + (r * 0.8) * math.cos(a) * 1.1
                    yy = cy + 10 - r * math.sin(a)
                    pts.append((xx, yy))
                else:
                    y = cy + 140 - (k - 9) * 14 - 20 * math.exp(-u * u * 4)
                    pts.append((x, y))
            else:
                a = 2 * math.pi * j / 60
                pts.append((cx + r * math.cos(a) * 1.0, cy + r * math.sin(a) * 1.2))
        if kind == 'loop' and k < 9:
            pts = [(pts[0][0], pts[0][1] + 120)] + pts + [(pts[-1][0], pts[-1][1] + 120)]
        c.line(pts, col, 4)


def b118_types(c, t, i):
    corner_tag(c, 'B118 · 三大类纹型：弓、箕、斗')
    c.text(60, 96, '指尖的纹路大致分三类：像小山的弓形、像簸箕的箕形、一圈圈的斗形；同一类里，每个人的细节又各不相同', 'serif', 36, INK)
    kinds = [('arch', '弓形：像小山'), ('loop', '箕形：一头开口'), ('whorl', '斗形：一圈圈')]
    show = min(3, int(t / 5) + 1)
    for k in range(show):
        kind, lab = kinds[k]
        cx = 360 + k * 600
        c.ellipse(cx, 560, 220, 270, fill=mix(BG, SKIN, 0.85))
        _ridges(c, cx, 560, kind, seed=k)
        c.text(cx, 880, lab, 'bold', 26, INK, 'mm')
    c.text(960, 950, '各类所占比例因人群而异（拍摄前核对）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '用铅笔把指头涂黑，再用透明胶带粘下来，指纹就清清楚楚地印在了纸上'),
                (7.2, 14, '先看大样子：有的像一座小山，有的像簸箕一头开口，有的是一圈圈的旋涡'),
                (14.2, 22, '同一个人十根手指常常不一样，一家人之间也各不相同：放大了看，细节更是千差万别（示意）')], y=1010)


def b118_minutiae(c, t, i):
    corner_tag(c, 'B118 · 放大看：断头、分叉，各不相同')
    c.text(60, 96, '纹线在某处突然断掉、或一分为二：这些小「特征点」的位置和方向，在两个人的手指上几乎不可能完全一样', 'serif', 36, INK)
    for k, (lab, seed) in enumerate((('甲的右手食指', 1), ('乙的右手食指', 2))):
        x0 = 220 + k * 820
        y0 = 260
        c.rect(x0, y0, x0 + 640, y0 + 560, fill=mix(BG, SKIN, 0.85), r=20)
        rnd = random.Random(seed)
        feats = []
        for row in range(12):
            y = y0 + 40 + row * 44
            cut = rnd.random()
            x_cut = x0 + 80 + cut * 480
            pts1 = [(x0 + 30 + j * 10, y + 8 * math.sin(j * 0.15 + row)) for j in range(int((x_cut - x0 - 30) / 10))]
            if rnd.random() < 0.5:
                pts2 = [(x_cut + 30 + j * 10, y + 8 * math.sin((x_cut - x0 + 30) / 10 * 0.15 + j * 0.15 + row)) for j in range(int((x0 + 610 - x_cut - 30) / 10))]
                feats.append(('end', pts1[-1] if pts1 else (x_cut, y)))
            else:
                pts2 = [(x_cut + j * 10, y + 8 * math.sin((x_cut - x0) / 10 * 0.15 + j * 0.15 + row)) for j in range(int((x0 + 610 - x_cut) / 10))]
                br = [(x_cut + j * 10, y + 8 * math.sin(j * 0.15 + row) + j * 1.5) for j in range(12)]
                c.line(br, RIDGE, 3)
                feats.append(('fork', (x_cut, y)))
            if len(pts1) > 1:
                c.line(pts1, RIDGE, 3)
            if len(pts2) > 1:
                c.line(pts2, RIDGE, 3)
        nshow = int(min(len(feats), t * 0.8))
        for kind, (fx, fy) in feats[:nshow]:
            c.ellipse(fx, fy, 14, 14, outline=INKRED if kind == 'end' else (90, 160, 230), width=3)
        c.text(x0 + 320, y0 + 600, lab, 'bold', 24, INK, 'mm')
    c.text(960, 940, '红圈：纹线断头　蓝圈：纹线分叉（示意）', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '两个人的指纹，远看可能都是箕形；凑近看，纹线在哪里断、在哪里分叉，完全不一样'),
                (7.2, 14, '这些特征点从出生就定下来，长大了只是变大，样子基本不变'),
                (14.2, 22, '一千多年前的契约上就按着指印；今天手机解锁、刑侦比对，比的也是这些小点（史料拍摄前核对）')], y=1010)


CLIPS = {
 'B116_十字板': (b116_bar, 22), 'B116_联动': (b116_link, 22),
 'B116_片头': (titles.opening(BSER, VOL28, SB28, 6, '汉代傀儡戏'), 7),
 'B116_片尾': (titles.closing(BSER, VOL28, SB28, 6, '下集：掷骰子全凭运气吗？'), 7),
 'B117_大数定律': (b117_law, 22), 'B117_偏心骰': (b117_loaded, 22),
 'B117_片头': (titles.opening(BSER, VOL28, SB28, 7, '战国墓出土的骰子'), 7),
 'B117_片尾': (titles.closing(BSER, VOL28, SB28, 7, '下集：古人按个红手印，为什么就能证明是自己按的？'), 7),
 'B118_纹型': (b118_types, 22), 'B118_特征点': (b118_minutiae, 22),
 'B118_片头': (titles.opening(BSER, VOL28, SB28, 8, '唐代契约上的指印'), 7),
 'B118_片尾': (titles.closing(BSER, VOL28, SB28, 8, '下集：糊了一层纸的窗户，为什么屋里还能亮堂？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
