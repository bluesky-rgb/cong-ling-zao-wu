"""第三十五季（第十四层：看与听的机器）第三批：E188 骨传导耳机、E189 调音器、E190 自动对焦 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s35a import S35A, SER35, VOL35, LIGHT, CUP

SKIN = (225, 190, 160)
BONE = (235, 228, 205)
WAVE = (120, 190, 240)
METALC = (190, 195, 205)


# ---------------------------------------------------------------- E188 骨传导耳机
def _head(c, cx, cy, s=1.0):
    c.ellipse(cx, cy, 260 * s, 300 * s, fill=mix(BG, SKIN, 0.35), outline=mix(BG, SKIN, 0.8), width=4)
    c.ellipse(cx, cy, 230 * s, 270 * s, outline=mix(BG, BONE, 0.7), width=10)
    c.ellipse(cx + 250 * s, cy + 10 * s, 30 * s, 60 * s, fill=mix(BG, SKIN, 0.7))


def e188_bone(c, t, i):
    corner_tag(c, '第 188 集 · 振动顺着骨头直接进内耳')
    c.text(60, 96, '平时声音从耳道进去推动鼓膜；骨传导耳机贴在颧骨上，振动穿过头骨，直接摇动内耳里的液体', 'serif', 36, INK)
    cx, cy = 760, 580
    _head(c, cx, cy)
    ex, ey = cx + 150, cy + 10
    c.line([(cx + 280, cy + 10), (ex + 40, ey)], mix(BG, SKIN, 0.9), 14)
    c.ellipse(ex + 40, ey, 10, 26, fill=mix(BG, (200, 160, 140), 0.9))
    c.text(ex + 40, ey - 60, '鼓膜', 'sans', 20, MUTED, 'mm')
    c.arc(ex - 10, ey, 26, 26, 0, 340, SPARK, 6)
    c.text(ex - 10, ey + 60, '内耳（耳蜗）', 'bold', 22, SPARK, 'mm')
    phase = (t % 11) / 11
    air = t < 11
    if air:
        for k in range(4):
            x = 1500 - ((t * 160 + k * 80) % 320)
            c.arc(x, ey, 40, 60, 140, 220, WAVE, 4)
        c.text(1500, ey - 120, '空气里的声音', 'bold', 24, WAVE, 'mm')
        c.text(1180, 900, '路线 1：耳道 → 鼓膜 → 内耳', 'bold', 26, INK, 'mm')
    else:
        bx, by = cx + 170, cy - 120
        c.rect(bx - 30, by - 20, bx + 30, by + 20, fill=METALC, r=8)
        c.text(bx + 60, by - 40, '骨传导耳机', 'bold', 22, INK, 'lm')
        for k in range(5):
            r = ((t * 120 + k * 40) % 200)
            c.arc(bx, by, r, r, 90, 270, mix(BG, SPARK, 1 - r / 200), 3)
        c.text(1180, 900, '路线 2：头骨 → 内耳（不经过耳道）', 'bold', 26, INK, 'mm')
    caps(c, t, [(0, 7, '平时，空气里的声音钻进耳道，推动鼓膜，再一路传到内耳'),
                (7.2, 14, '骨传导耳机贴在耳朵前面的骨头上，自己不出多少声，而是一直在振动'),
                (14.2, 22, '振动穿过头骨，直接摇动内耳里的液体：耳朵空着，也能听见（示意）')], y=1010)


def e188_spoon(c, t, i):
    corner_tag(c, '第 188 集 · 绳子和手指把振动送进去')
    c.text(60, 96, '勺子绑在绳子中间，绳子两头缠在手指上按住耳屏：敲一下勺子，听到的是一声浑厚的「钟声」', 'serif', 36, INK)
    cx, cy = 960, 470
    _head(c, cx, cy - 20, 0.75)
    hit = (t % 4) < 0.3
    amp = math.exp(-(t % 4) * 1.2) * 10
    sx, sy = cx + 6 * math.sin(t * 40) * amp / 10, 860
    c.line([(cx - 200, cy), (sx, sy - 40)], mix(BG, CUP, 0.9), 3)
    c.line([(cx + 200, cy), (sx, sy - 40)], mix(BG, CUP, 0.9), 3)
    c.ellipse(cx - 200, cy, 22, 22, fill=SKIN)
    c.ellipse(cx + 200, cy, 22, 22, fill=SKIN)
    c.text(cx - 240, cy - 50, '手指按住耳屏', 'sans', 20, MUTED, 'rm')
    c.ellipse(sx, sy, 40, 26, fill=METALC)
    c.line([(sx, sy - 26), (sx, sy - 40)], METALC, 6)
    if hit:
        c.text(sx + 100, sy, '叮！', 'bold', 30, SPARK, 'lm')
    for side in (-1, 1):
        for k in range(3):
            f = ((t * 1.5 + k / 3) % 1)
            x = sx + (cx + side * 200 - sx) * f
            y = sy - 40 + (cy - sy + 40) * f
            c.ellipse(x, y, 7 * (amp / 10 + 0.3), 7 * (amp / 10 + 0.3), fill=mix(BG, SPARK, amp / 10 + 0.2))
    c.rect(1380, 640, 1860, 900, fill=SHEET, r=14)
    c.text(1620, 690, '手指按耳：浑厚的钟声', 'bold', 22, GREEN, 'mm')
    c.text(1620, 740, '手指离开：细细的「叮」', 'bold', 22, NRED, 'mm')
    c.text(1620, 800, '只按耳屏，不塞进耳道', 'sans', 20, NRED, 'mm')
    c.text(1620, 840, '敲得轻一点', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '勺子被敲一下，整个勺子都在振动'),
                (7.2, 14, '振动顺着绷紧的绳子跑到手指，再从耳朵旁边的骨头传进内耳'),
                (14.2, 22, '固体传声比空气好得多：手指一离开耳朵，钟声就变成细细的一声「叮」（示意）')], y=1010)


# ---------------------------------------------------------------- E189 调音器
def e189_frequency(c, t, i):
    corner_tag(c, '第 189 集 · 数一数每秒振动几次')
    c.text(60, 96, '调音器不认识歌，只做一件事：数出声音每秒钟振动多少次（频率），和标准音比高了还是低了', 'serif', 36, INK)
    f_now = 430 + 10 * min(1.0, t / 16)
    gx0, gx1, gy = 120, 1180, 520
    c.rect(100, 300, 1200, 740, fill=SHEET, r=14)
    c.text(650, 330, '放大看 0.02 秒里的声音波形', 'sans', 22, MUTED, 'mm')
    n = f_now * 0.02
    pts = [(gx0 + (gx1 - gx0) * k / 400, gy - 150 * math.sin(2 * math.pi * n * k / 400 + t * 3)) for k in range(401)]
    c.line(pts, WAVE, 3)
    c.text(650, 710, f'0.02 秒里振动了 {n:.1f} 次 → 每秒 {f_now:.0f} 次', 'mono', 24, SPARK, 'mm')
    cx, cy = 1540, 640
    c.arc(cx, cy, 260, 260, 200, 340, MUTED, 6)
    for k, lab in enumerate(['低', '准', '高']):
        a = math.radians(220 + k * 50)
        c.text(cx + 300 * math.cos(a), cy + 300 * math.sin(a), lab, 'bold', 26, [NRED, GREEN, NRED][k], 'mm')
    a = math.radians(270 + (f_now - 440) * 5)
    c.line([(cx, cy), (cx + 240 * math.cos(a), cy + 240 * math.sin(a))], GREEN if abs(f_now - 440) < 1 else SPARK, 6)
    c.ellipse(cx, cy, 14, 14, fill=INK)
    c.text(cx, cy + 80, f'{f_now:.0f} 赫兹', 'mono', 34, INK, 'mm')
    c.text(cx, cy + 130, '标准音 A = 440 赫兹', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 7, '琴弦一振动，空气就跟着一疏一密，手机的麦克风把它变成一条波形'),
                (7.2, 14, '调音器数一数波形每秒钟起伏几次，就是这个音的频率'),
                (14.2, 22, '比 440 少就是低了，往紧里拧；多了就是高了，往松里拧（示意）')], y=1010)


def e189_beats(c, t, i):
    corner_tag(c, '第 189 集 · 两个音差一点，就会「打拍」')
    c.text(60, 96, '440 赫兹和 442 赫兹一起响：有时步调一致变响，有时正好相反抵消，每秒「哇哇」起伏 2 次', 'serif', 36, INK)
    df = 2 if t < 12 else 1
    gx0, gx1 = 120, 1800
    T = 2.0
    for j, (y, f, col, lab) in enumerate([(300, 440, WAVE, '440 赫兹'), (470, 440 + df, SPARK, f'{440 + df} 赫兹')]):
        pts = [(gx0 + (gx1 - gx0) * k / 800, y - 50 * math.sin(2 * math.pi * (12 + (f - 440) * 0.0) * k / 800 + (f - 440) * 2 * math.pi * T * k / 800)) for k in range(801)]
        c.line(pts, col, 2)
        c.text(gx0, y - 80, lab, 'bold', 22, col, 'lm')
    y = 720
    pts = []
    for k in range(801):
        s = k / 800
        a = math.sin(2 * math.pi * 12 * s) + math.sin(2 * math.pi * 12 * s + df * 2 * math.pi * T * s)
        pts.append((gx0 + (gx1 - gx0) * s, y - 45 * a))
    c.line(pts, GREEN, 2)
    env = [(gx0 + (gx1 - gx0) * k / 200, y - 90 * abs(math.cos(math.pi * df * T * k / 200))) for k in range(201)]
    c.line(env, mix(BG, GREEN, 0.5), 2)
    c.text(gx0, y - 130, '两个一起响（合起来）', 'bold', 22, GREEN, 'lm')
    cur = gx0 + (gx1 - gx0) * ((t % T) / T)
    c.line([(cur, 220), (cur, 830)], MUTED, 1)
    c.text(960, 880, f'这 {T:.0f} 秒里起伏了 {df * T:.0f} 次 → 差 {df} 赫兹', 'mono', 26, SPARK, 'mm')
    caps(c, t, [(0, 7, '两个音高几乎一样的声音一起放，听起来会一阵响一阵轻'),
                (7.2, 14, '步调对上就变响，错开半拍就抵消：每秒起伏几次，就差几赫兹'),
                (14.2, 22, '差 1 赫兹，起伏慢一半；拍消失了，两个音就调准了（示意）')], y=1010)


# ---------------------------------------------------------------- E190 自动对焦
def e190_focus(c, t, i):
    corner_tag(c, '第 190 集 · 物体越近，清楚的像离镜片越远')
    c.text(60, 96, '同一个放大镜：远处的楼成像在离镜片很近的地方；植物越近，清楚的像就落得越远，纸要往后挪', 'serif', 36, INK)
    f = 15.0
    ax = 560
    lx = 860
    stages = [(10000, '窗外远景'), (200, '2 米外的植物'), (100, '1 米外的植物'), (50, '50 厘米')]
    k = min(3, int(t / 5.5))
    u, lab = stages[k]
    v = 1 / (1 / f - 1 / u)
    sc = 16
    c.line([(80, ax), (1860, ax)], mix(BG, MUTED, 0.5), 1)
    c.ellipse(lx, ax, 20, 170, fill=mix(BG, (170, 210, 240), 0.5), outline=MUTED, width=3)
    px = lx + v * sc
    c.rect(px, ax - 200, px + 12, ax + 200, fill=mix(BG, CUP, 0.9))
    c.text(px + 20, ax - 220, '白纸', 'sans', 22, MUTED, 'lm')
    ox = max(120, lx - min(u, 60) * 12)
    c.text(ox, ax - 160, lab, 'bold', 24, INK, 'mm')
    c.poly([(ox, ax - 100), (ox - 40, ax), (ox + 40, ax)], mix(BG, GREEN, 0.8))
    for dy in (-100, -60):
        c.line([(ox, ax + dy), (lx, ax - 120 + (dy + 100) * 0.6), (px, ax + (v / u) * 100 * 0.8 + 10)], mix(BG, LIGHT, 0.6), 2)
    c.text(lx, ax + 220, '放大镜', 'sans', 22, MUTED, 'mm')
    c.text((lx + px) / 2, ax + 270, f'纸到镜片 {v:.1f} 厘米', 'mono', 26, SPARK, 'mm')
    c.text(1500, 860, '按焦距 15 厘米算（示意）', 'sans', 20, MUTED, 'mm')
    c.text(1500, 900, '放大镜绝不对着太阳', 'bold', 22, NRED, 'mm')
    caps(c, t, [(0, 7, '对着窗外很远的楼，清楚的像差不多就在一倍焦距那里'),
                (7.2, 14, '换成 2 米、1 米外的植物，清楚的像越落越远，纸得往后挪'),
                (14.2, 22, '手机镜头太小没法挪远，就让镜片自己前后动一点点：这就是对焦（示意）')], y=1010)


def e190_contrast(c, t, i):
    corner_tag(c, '第 190 集 · 最清楚的时候，反差最大')
    c.text(60, 96, '手机怎么知道清楚了？它一边挪镜片，一边看画面里明暗边缘有多「锐」，找到最锐的位置就停', 'serif', 36, INK)
    pos = 0.5 + 0.5 * math.sin(t / 22 * 2 * math.pi * 1.0 - math.pi / 2) if t < 16 else 0.6
    best = 0.6
    blur = abs(pos - best) * 60
    x0, y0 = 160, 260
    c.rect(x0 - 20, y0 - 20, x0 + 620, y0 + 520, fill=SHEET, r=14)
    for k in range(6):
        col = INK if k % 2 == 0 else BG
        x = x0 + k * 100
        c.rect(x, y0, x + 100, y0 + 500, fill=col)
    if blur > 1:
        for k in range(1, 6):
            x = x0 + k * 100
            for j in range(int(blur)):
                f = j / max(1, int(blur))
                c.rect(x - blur / 2 + j, y0, x - blur / 2 + j + 1, y0 + 500, fill=mix(INK, BG, f) if k % 2 == 1 else mix(BG, INK, f))
    c.text(x0 + 300, y0 + 560, '手机看到的画面', 'sans', 22, MUTED, 'mm')
    gx0, gx1, gy0, gy1 = 900, 1800, 760, 300
    c.rect(860, 260, 1860, 820, fill=SHEET, r=14)
    c.line([(gx0, gy1), (gx0, gy0), (gx1, gy0)], MUTED, 3)
    pts = [(gx0 + (gx1 - gx0) * s / 100, gy0 - 400 * math.exp(-((s / 100 - best) / 0.12) ** 2)) for s in range(101)]
    c.line(pts, mix(BG, FIELD, 0.8), 3)
    sx = gx0 + (gx1 - gx0) * pos
    sy = gy0 - 400 * math.exp(-((pos - best) / 0.12) ** 2)
    c.ellipse(sx, sy, 14, 14, fill=SPARK)
    c.text((gx0 + gx1) / 2, gy0 + 34, '镜片位置 →', 'sans', 20, MUTED, 'mm')
    c.text(gx0 + 10, gy1 - 20, '边缘反差', 'sans', 20, MUTED, 'lm')
    if t >= 16:
        c.text(gx0 + (gx1 - gx0) * best, gy1 - 50, '最锐：停！', 'bold', 26, GREEN, 'mm')
    caps(c, t, [(0, 7, '画面模糊时，黑白交界是一片灰；对准了，交界就又黑又白、一刀切开'),
                (7.2, 14, '手机让镜片前后走一遍，每个位置都算一算边缘的反差'),
                (14.2, 22, '反差最大的那一点就是最清楚的位置，镜片停在那里（示意）')], y=1010)


CLIPS = {
 'E188_骨传导': (e188_bone, 22), 'E188_勺子钟': (e188_spoon, 22),
 'E188_片头': (titles.opening(SER35, VOL35, S35A, 6, '20 世纪已有骨传导助听'), 7),
 'E188_片尾': (titles.closing(SER35, VOL35, S35A, 6, '下集：手机贴在琴上，怎么听出这根弦不准？'), 7),
 'E189_频率': (e189_frequency, 22), 'E189_拍': (e189_beats, 22),
 'E189_片头': (titles.opening(SER35, VOL35, S35A, 7, '20 世纪 70 年代出现电子调音器'), 7),
 'E189_片尾': (titles.closing(SER35, VOL35, S35A, 7, '下集：点一下屏幕，模糊的画面怎么就清楚了？'), 7),
 'E190_对焦': (e190_focus, 22), 'E190_反差': (e190_contrast, 22),
 'E190_片头': (titles.opening(SER35, VOL35, S35A, 8, '1977 年第一台自动对焦相机'), 7),
 'E190_片尾': (titles.closing(SER35, VOL35, S35A, 8, '下集：视频通话一秒几十张画面，怎么不卡？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
