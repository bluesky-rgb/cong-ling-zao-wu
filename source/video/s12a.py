"""第十二季（第三层：声音、图像与计算）第一批：E72 电话、E73 留声机、E74 电影 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg

S12A = [('72', '电话'), ('73', '留声机'), ('74', '电影'), ('75', '变压器'), ('76', '无线电'),
        ('77', '太阳能电池'), ('78', '内燃机'), ('79', '悬索桥'), ('80', '机械计算器'), ('81', '逻辑门')]
SER12, VOL12 = '从零造物', '第十二季 · 第三层：声音、图像与计算'
CONE = (200, 190, 170)
MAG = (120, 125, 140)
COIL = (200, 130, 70)
FILM = (60, 55, 50)

def speaker(c, x, y, disp, flip=False, a=1.0):
    """speaker cross-section facing right (or left if flip); disp = cone displacement in px"""
    s = -1 if flip else 1
    # magnet
    c.rect(x - s * 70 - 40, y - 60, x - s * 70 + 40, y + 60, fill=mix(BG, MAG, a), r=6)
    # coil on the cone's neck
    cx = x + s * disp
    c.rect(cx - 18, y - 34, cx + 18, y + 34, fill=mix(BG, COIL, a), r=4)
    # cone
    c.poly([(cx + s * 18, y - 30), (cx + s * 150, y - 130), (cx + s * 150, y + 130), (cx + s * 18, y + 30)], mix(BG, CONE, 0.7 * a))

def wave_pts(x0, x1, y, amp, k, phase, n=120):
    return [(x0 + (x1 - x0) * j / n, y + amp * math.sin(k * j / n * 2 * math.pi + phase)) for j in range(n + 1)]

# ---------------------------------------------------------------- E72 电话
def e72_signal(c, t, i):
    corner_tag(c, '第 72 集 · 振动变电流，电流变振动')
    c.text(60, 96, '对着一个喇叭说话，另一个喇叭里就有声音', 'serif', 40, INK)
    talk = fade(t, 1, 2)
    v = math.sin(t * 9) * 0.6 + math.sin(t * 15.3) * 0.4
    d = 14 * v * talk
    # left: mouth sound waves -> speaker A (as microphone)
    for k in range(4):
        r = 40 + ((t * 120 + k * 60) % 240)
        if talk > 0:
            c.arc(200, 520, r, r * 1.2, -40, 40, mix(BG, MUTED, talk * (1 - r / 300)), 3)
    speaker(c, 520, 520, d, flip=True)
    speaker(c, 1400, 520, d)
    # wires
    c.line([(470, 480), (470, 300), (1450, 300), (1450, 480)], COPPER, 4)
    c.line([(470, 560), (470, 740), (1450, 740), (1450, 560)], COPPER, 4)
    # current waveform travelling along the wire
    if talk > 0:
        pts = [(560 + j * 8, 300 + 30 * talk * math.sin(j * 0.5 - t * 9)) for j in range(100)]
        seg(c, pts, SPARK, 3)
    for k in range(4):
        r = 40 + ((t * 120 + k * 60) % 240)
        if talk > 0:
            c.arc(1720, 520, r, r * 1.2, 140, 220, mix(BG, MUTED, talk * (1 - r / 300)), 3)
    a = fade(t, 4, 5)
    c.text(520, 820, '话筒：振膜带线圈在磁铁旁动\n→ 线圈里感应出电流（磁生电）', 'sans', 24, mix(BG, INK, a), 'mm')
    b = fade(t, 9, 10)
    c.text(1400, 820, '听筒：变化的电流让线圈变成电磁铁\n→ 推着振膜动（电生磁）', 'sans', 24, mix(BG, INK, b), 'mm')
    c.text(960, 220, '随声音变化的电流', 'bold', 26, mix(BG, SPARK, talk), 'mm')
    caps(c, t, [(0, 7, '声音推着喇叭的振膜来回动，振膜上粘着一个小线圈，旁边是磁铁'),
                (7.2, 14, '线圈在磁铁旁边动，就感应出电流：电流跟着声音一起忽大忽小'),
                (14.2, 22, '电流顺着导线跑到另一个喇叭，让那边的线圈和振膜照样动起来：声音就过去了')], y=1010)

def e72_reverse(c, t, i):
    corner_tag(c, '第 72 集 · 同一个零件，正着用反着用')
    c.text(60, 96, '话筒和听筒，是同一个东西', 'serif', 40, INK)
    rows = [('第 04 集 · 磁生电', '动 → 电', '话筒、发电机', FIELD), ('第 56 集 · 电生磁', '电 → 动', '听筒、电动机', COPPER)]
    for k, (name, arrow, use, col) in enumerate(rows):
        y = 330 + k * 300
        a = fade(t, 1 + k * 4, 2 + k * 4)
        c.rect(160, y - 90, 1760, y + 90, fill=mix(BG, SHEET, a), r=14)
        c.text(200, y - 30, name, 'bold', 32, mix(BG, col, a), 'lm')
        c.text(200, y + 30, use, 'sans', 26, mix(BG, MUTED, a), 'lm')
        c.text(960, y, arrow, 'serif', 56, mix(BG, INK, a), 'mm')
        pts = wave_pts(1240, 1720, y, 40, 3, t * 4 + k * 0.4)
        seg(c, pts, mix(BG, col, a), 4)
    b = fade(t, 11, 12)
    c.text(960, 880, '1876 年贝尔的电话：话筒和听筒都是「振膜 + 线圈 + 磁铁」', 'bold', 28, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 5, '第 04 集我们让磁铁在线圈旁动，发出了电'),
                (5.2, 11, '第 56 集让电流过线圈，变成了磁铁：同一套零件，反过来就是另一个用途'),
                (11.2, 22, '电话一头用「动变电」，一头用「电变动」：不用电池，两个小喇叭也能对讲（声音很小）')], y=1010)

# ---------------------------------------------------------------- E73 留声机
def e73_record(c, t, i):
    corner_tag(c, '第 73 集 · 把振动刻下来')
    c.text(60, 96, '对着喇叭口喊，针尖在锡箔上刻出波纹', 'serif', 40, INK)
    # horn + diaphragm + needle
    hx, hy = 520, 460
    c.poly([(hx - 300, hy - 200), (hx, hy - 30), (hx, hy + 30), (hx - 300, hy + 200)], mix(BG, (170, 140, 90), 0.6))
    shout = fade(t, 2, 3) * (1 - fade(t, 13, 14))
    v = (math.sin(t * 23) * 0.7 + math.sin(t * 37) * 0.3) * shout
    c.line([(hx, hy - 40), (hx + 10 * v, hy), (hx, hy + 40)], INK, 4)
    nx = hx + 10 * v
    c.line([(nx, hy), (nx + 120, hy + 160)], (200, 205, 215), 3)
    # foil-covered cylinder moving left (groove drawn)
    gy = hy + 170
    c.rect(200, gy - 40, 1760, gy + 40, fill=(200, 200, 205), r=20)
    speed = 60
    groove = []
    for j in range(260):
        x = nx + 120 - j * 6
        if x < 210: break
        tt = t - j * 6 / speed
        if tt < 0: break
        sh = fade(tt, 2, 3) * (1 - fade(tt, 13, 14))
        vv = (math.sin(tt * 23) * 0.7 + math.sin(tt * 37) * 0.3) * sh
        groove.append((x, gy + 22 * vv))
    if len(groove) > 1: seg(c, groove, (60, 60, 70), 3)
    a = fade(t, 14, 15)
    c.rect(1080, 200, 1820, 420, fill=mix(BG, SHEET, a), r=12)
    c.text(1110, 250, '放的时候反过来：', 'bold', 28, mix(BG, INK, a), 'lm')
    c.text(1110, 305, '针尖顺着波纹抖动 → 振膜抖动', 'sans', 26, mix(BG, INK, a), 'lm')
    c.text(1110, 355, '→ 喇叭口把声音放大', 'sans', 26, mix(BG, INK, a), 'lm')
    caps(c, t, [(0, 6, '1877 年，爱迪生对着喇叭口喊话：声音推动喇叭底部的薄膜'),
                (6.2, 14, '薄膜上的针尖跟着抖，在转动的锡箔上刻出一道起伏的沟'),
                (14.2, 22, '再让针尖从头走一遍沟纹，薄膜跟着抖：声音又回来了。整个过程不用电')], y=1010)

def e73_wave(c, t, i):
    corner_tag(c, '第 73 集 · 沟纹就是声音的形状')
    c.text(60, 96, '响一点、高一点，沟纹会怎么变？', 'serif', 40, INK)
    rows = [('轻声', 18, 3, MUTED), ('大声：起伏更大', 60, 3, COPPER), ('高音：起伏更密', 18, 9, FIELD)]
    for k, (name, amp, f, col) in enumerate(rows):
        y = 300 + k * 230
        a = fade(t, 1 + k * 4, 2 + k * 4)
        c.text(160, y, name, 'bold', 28, mix(BG, INK, a), 'lm')
        c.rect(560, y - 80, 1760, y + 80, fill=mix(BG, (200, 200, 205), 0.25 * a), r=10)
        pts = wave_pts(580, 1740, y, amp, f, t * 2)
        seg(c, pts, mix(BG, col, a), 4)
    caps(c, t, [(0, 5, '声音越轻，针尖抖得越少，沟纹起伏越小'),
                (5.2, 9, '声音越大，起伏越大'),
                (9.2, 22, '音越高，每秒抖得越多，沟纹就越密：唱片上那一圈圈细沟，就是声音的形状')], y=1010)

# ---------------------------------------------------------------- E74 电影
def runner(c, x, y, ph, col, s=1.0):
    """simple stick runner at phase ph (0..1)"""
    q = ph * 2 * math.pi
    c.ellipse(x + 8 * s, y - 150 * s, 22 * s, 22 * s, fill=col)
    c.line([(x + 6 * s, y - 128 * s), (x, y)], col, max(3, int(8 * s)))
    for leg in (0, math.pi):
        th = 0.55 * math.sin(q + leg)
        knee = (x + 62 * s * math.sin(th), y + 62 * s * math.cos(th))
        bend = 0.2 + 0.9 * max(0.0, math.sin(q + leg + math.pi / 2))
        foot = (knee[0] + 60 * s * math.sin(th - bend), knee[1] + 60 * s * math.cos(th - bend))
        c.line([(x, y), knee, foot], col, max(3, int(7 * s)))
        phi = -0.7 * math.sin(q + leg)
        sh = (x + 5 * s, y - 115 * s)
        elbow = (sh[0] + 40 * s * math.sin(phi), sh[1] + 40 * s * math.cos(phi))
        hand = (elbow[0] + 36 * s * math.sin(phi + 1.2), elbow[1] + 36 * s * math.cos(phi + 1.2) * 0.4)
        c.line([sh, elbow, hand], col, max(2, int(6 * s)))

def e74_frames(c, t, i):
    corner_tag(c, '第 74 集 · 每秒几张才连起来')
    c.text(60, 96, '同一组 12 张画，换得越快越像在跑', 'serif', 40, INK)
    # strip of 12 frames on top
    for k in range(12):
        x = 160 + k * 135
        c.rect(x - 55, 180, x + 55, 330, outline=MUTED, width=2, r=4)
        runner(c, x, 280, k / 12, INK, 0.45)
    fps_list = [(0, 6, 2), (6, 12, 6), (12, 17, 12), (17, 22, 24)]
    fps = 2
    for a0, a1, f in fps_list:
        if a0 <= t < a1: fps = f
    k = int(t * fps) % 12
    x = 160 + k * 135
    c.rect(x - 58, 177, x + 58, 333, outline=SPARK, width=4, r=4)
    c.rect(560, 400, 1360, 900, fill=SHEET, r=12)
    runner(c, 960, 760, k / 12, INK, 1.4)
    c.text(1420, 520, f'每秒 {fps} 张', 'mono', 44, SPARK, 'lm')
    verdict = {2: '一顿一顿', 6: '还在跳', 12: '差不多连起来了', 24: '流畅（电影的标准）'}[fps]
    c.text(1420, 590, verdict, 'bold', 30, INK, 'lm')
    caps(c, t, [(0, 6, '每秒两张：一张一张地跳，看得出是图片'),
                (6.2, 12, '每秒六张：开始像动画，但还在跳'),
                (12.2, 17, '每秒十二张左右，眼睛和大脑就把它们连成了动作'),
                (17.2, 22, '有声电影定成每秒 24 格：一秒钟里，其实是 24 张静止的照片')], y=1010)

def e74_shutter(c, t, i):
    corner_tag(c, '第 74 集 · 换片的时候遮住')
    c.text(60, 96, '放映机：胶片走一格、停一下，换片时快门挡住光', 'serif', 38, INK)
    period = 2.0
    ph = (t % period) / period
    moving = ph < 0.35
    shift = ease(min(1, ph / 0.35)) if moving else 1.0
    # film strip vertical
    fx = 520
    for k in range(-2, 4):
        y = 200 + (k + shift) * 200
        if y < 150 or y > 820: continue
        c.rect(fx - 120, y, fx + 120, y + 180, fill=FILM, r=4)
        for h in range(4):
            c.rect(fx - 110, y + 10 + h * 42, fx - 96, y + 30 + h * 42, fill=BG)
            c.rect(fx + 96, y + 10 + h * 42, fx + 110, y + 30 + h * 42, fill=BG)
        frame = (int(t / period) - k) % 12
        runner(c, fx, y + 140, frame / 12, (220, 210, 190), 0.5)
    c.rect(fx - 140, 590, fx + 140, 610, outline=SPARK, width=3)
    # shutter + lamp + screen
    lit = not moving
    c.ellipse(220, 600, 40, 40, fill=SPARK)
    c.text(220, 670, '灯', 'bold', 24, INK, 'mm')
    if lit:
        c.poly([(fx + 120, 560), (fx + 120, 640), (1500, 900), (1500, 300)], mix(BG, SPARK, 0.25))
    sx = 820
    ang = t * math.pi
    c.ellipse(sx, 600, 80, 80, outline=MUTED, width=2)
    c.poly([(sx, 600), (sx + 80 * math.cos(ang), 600 + 80 * math.sin(ang)), (sx + 80 * math.cos(ang + 2.2), 600 + 80 * math.sin(ang + 2.2))], INK if moving else mix(BG, INK, 0.3))
    c.text(sx, 720, '快门', 'bold', 24, INK, 'mm')
    c.rect(1500, 300, 1520, 900, fill=MUTED)
    c.rect(1540, 360, 1840, 840, fill=SHEET if lit else BG, r=6)
    if lit:
        runner(c, 1690, 740, (int(t / period) % 12) / 12, INK, 1.0)
    c.text(1690, 920, '银幕：' + ('看见这一格' if lit else '黑一下（太快，看不出来）'), 'bold', 24, INK, 'mm')
    caps(c, t, [(0, 8, '胶片不是一直在走：抓片爪拉它走一格，停住，再拉一格'),
                (8.2, 15, '走的那一下，快门转过来挡住光；停住的时候，光才打到银幕上'),
                (15.2, 22, '所以银幕其实一亮一黑，太快了眼睛看不出：我们只看见一张张清楚的画（示意已放慢）')], y=1010)

CLIPS = {
 'E72_振动变电流': (e72_signal, 22), 'E72_可逆': (e72_reverse, 22),
 'E72_片头': (titles.opening(SER12, VOL12, S12A, 0, '1876 年 · 贝尔'), 7),
 'E72_片尾': (titles.closing(SER12, VOL12, S12A, 0, '下集：声音怎么被「刻」下来？'), 7),
 'E73_刻槽': (e73_record, 22), 'E73_波形': (e73_wave, 22),
 'E73_片头': (titles.opening(SER12, VOL12, S12A, 1, '1877 年 · 爱迪生的锡箔留声机'), 7),
 'E73_片尾': (titles.closing(SER12, VOL12, S12A, 1, '下集：一张张不动的照片，为什么会动起来？'), 7),
 'E74_帧': (e74_frames, 22), 'E74_快门': (e74_shutter, 22),
 'E74_片头': (titles.opening(SER12, VOL12, S12A, 2, '1895 年 · 巴黎 · 卢米埃尔兄弟'), 7),
 'E74_片尾': (titles.closing(SER12, VOL12, S12A, 2, '下集：为什么电要先升压再输送？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
