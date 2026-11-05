"""第十八季（古法解密 6.0）第三批：B66 回音壁、B67 屋檐举折、B68 饴糖 —— 动画与片头片尾。"""
import math, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s18a import SB18, VOL18, WOOD

WALL = (200, 170, 140)
SOUND = (120, 190, 240)
TILE = (90, 100, 115)
WATER = (110, 170, 230)

# ---------------------------------------------------------------- B66 回音壁
def b66_wall(c, t, i):
    corner_tag(c, 'B66 · 声音贴着圆墙走')
    c.text(60, 96, '俯视圆形围墙：贴墙说的话，被墙一次次「接力」反射', 'serif', 40, INK)
    cx, cy, R = 700, 590, 380
    c.ellipse(cx, cy, R, R, outline=WALL, width=14)
    c.ellipse(cx, cy, 70, 70, fill=mix(BG, WALL, 0.4))
    c.text(cx, cy, '皇穹宇', 'sans', 22, INK, 'mm')
    th0 = math.radians(160)
    S = (cx + (R - 10) * math.cos(th0), cy + (R - 10) * math.sin(th0))
    c.ellipse(S[0], S[1], 14, 14, fill=SPARK)
    c.text(S[0] - 30, S[1], '说话', 'bold', 24, SPARK, 'rm')
    thL = th0 - math.pi
    Lp = (cx + (R - 10) * math.cos(thL), cy + (R - 10) * math.sin(thL))
    c.ellipse(Lp[0], Lp[1], 14, 14, fill=GREEN)
    c.text(Lp[0] + 30, Lp[1], '听', 'bold', 24, GREEN, 'lm')
    prog = fade(t, 2, 12)
    for k, al in enumerate((8, 12, 18)):
        step = 2 * math.radians(al)
        n = int(math.pi / step) + 1
        pts = [(cx + (R - 10) * math.cos(th0 + j * step), cy + (R - 10) * math.sin(th0 + j * step)) for j in range(n + 1)]
        tot = len(pts) - 1
        m = prog * tot
        full = int(m)
        P = pts[:full + 1]
        if full < tot:
            a, b = pts[full], pts[full + 1]
            f = m - full
            P = P + [(a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)]
        if len(P) > 1:
            c.line(P, mix(BG, SOUND, 0.9 - k * 0.2), 3)
    a = fade(t, 12, 13)
    if a > 0:
        for rr in (100, 170, 240):
            c.arc(S[0], S[1], rr, rr, -50, 50, mix(BG, NRED, a * (1 - rr / 400)), 2)
        c.text(cx, cy + 170, '离开墙：往四面散开', 'sans', 22, mix(BG, NRED, a), 'mm')
    b = fade(t, 14, 15)
    if b > 0:
        c.rect(1200, 330, 1840, 640, fill=mix(BG, SHEET, b), r=14)
        c.text(1520, 380, '为什么贴墙听得清', 'bold', 28, mix(BG, INK, b), 'mm')
        c.text(1520, 450, '墙面光滑、弧度均匀', 'sans', 26, mix(BG, INK, b), 'mm')
        c.text(1520, 500, '声音一直被挡在墙边，不往外散', 'sans', 26, mix(BG, INK, b), 'mm')
        c.text(1520, 580, '围墙半径约 32 米（拍摄前核对）', 'sans', 22, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '贴着墙对墙说话，声音斜斜地撞到墙上'),
                (6.2, 13, '光滑的弧形墙把它反射回来，再撞、再反射，一路贴着墙绕到对面'),
                (13.2, 22, '要是离开墙说，声音往四面散开，走不了多远就弱了')], y=1010)

def _parab_pts(xv, yc, f, sign, H=260, n=40):
    return [(xv + sign * (y * y) / (4 * f), yc + y) for y in [(-H + 2 * H * j / n) for j in range(n + 1)]]

def b66_umbrella(c, t, i):
    corner_tag(c, 'B66 · 两把伞传悄悄话')
    c.text(60, 96, '弧面把声音收拢：一边焦点发出，另一边焦点接住', 'serif', 40, INK)
    yc, f = 560, 150
    xl, xr = 260, 1660
    c.line(_parab_pts(xl, yc, f, 1), WALL, 8)
    c.line(_parab_pts(xr, yc, f, -1), WALL, 8)
    Fl, Fr = (xl + f, yc), (xr - f, yc)
    c.ellipse(Fl[0], Fl[1], 14, 14, fill=SPARK)
    c.text(Fl[0], Fl[1] + 40, '手机滴答声', 'sans', 22, SPARK, 'mm')
    c.ellipse(Fr[0], Fr[1], 14, 14, fill=GREEN)
    c.text(Fr[0], Fr[1] + 40, '耳朵', 'sans', 22, GREEN, 'mm')
    prog = fade(t, 2, 11)
    for y in (-220, -150, -80, 80, 150, 220):
        P1 = (xl + y * y / (4 * f), yc + y)
        P2 = (xr - y * y / (4 * f), yc + y)
        segs = [(Fl, P1), (P1, P2), (P2, Fr)]
        lens = [math.dist(a, b) for a, b in segs]
        tot = sum(lens)
        d = prog * tot
        pts = [Fl]
        for (a, b), L in zip(segs, lens):
            if d <= 0: break
            u = min(1, d / L)
            pts.append((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u))
            d -= L
        if len(pts) > 1:
            c.line(pts, mix(BG, SOUND, 0.85), 3)
    a = fade(t, 12, 13)
    if a > 0:
        c.rect(640, 840, 1280, 960, fill=mix(BG, SHEET, a), r=12)
        c.text(960, 880, '对准焦点：……；挪开 30 厘米：……', 'sans', 24, mix(BG, INK, a), 'mm')
        c.text(960, 925, '（以实测为准）', 'sans', 20, mix(BG, MUTED, a), 'mm')
    caps(c, t, [(0, 6, '两把打开的伞面对面摆着，伞面就是一个弧面'),
                (6.2, 12, '一边焦点上的滴答声撞到伞面，被反射成一束平行的声音，直直飞向对面'),
                (12.2, 22, '对面的伞再把它收拢到自己的焦点：耳朵放在那儿，就像贴在手机旁边')], y=1010)

# ---------------------------------------------------------------- B67 屋檐举折
AX, AY, BX, BY = 300, 230, 1500, 730
def _solve_theta(k):
    lo, hi = 0.1, 2 * math.pi - 0.01
    for _ in range(80):
        m = (lo + hi) / 2
        if (m - math.sin(m)) / (1 - math.cos(m)) < k: lo = m
        else: hi = m
    return (lo + hi) / 2
THB = _solve_theta((BX - AX) / (BY - AY))
RC = (BY - AY) / (1 - math.cos(THB))
GG = 435.0
T_CYC = THB * math.sqrt(RC / GG)
LS = math.hypot(BX - AX, BY - AY)
T_LIN = math.sqrt(2 * LS / (GG * (BY - AY) / LS))

def b67_race(c, t, i):
    corner_tag(c, 'B67 · 先陡后缓，反而更快')
    c.text(60, 96, '同一个起点、同一个终点：直坡和凹坡，谁先到？', 'serif', 40, INK)
    cyc = [(AX + RC * (th - math.sin(th)), AY + RC * (1 - math.cos(th))) for th in [THB * j / 80 for j in range(81)]]
    c.line([(AX, AY), (BX, BY)], MUTED, 6)
    c.line(cyc, SPARK, 6)
    c.ellipse(AX, AY, 10, 10, fill=INK)
    c.ellipse(BX, BY, 10, 10, fill=INK)
    t0 = 3.0
    tt = max(0, t - t0)
    s = min(0.5 * GG * (BY - AY) / LS * tt * tt, LS)
    c.ellipse(AX + (BX - AX) * s / LS, AY + (BY - AY) * s / LS, 22, 22, fill=(200, 200, 210))
    th = min(tt / math.sqrt(RC / GG), THB)
    c.ellipse(AX + RC * (th - math.sin(th)), AY + RC * (1 - math.cos(th)), 22, 22, fill=SPARK)
    c.rect(1180, 220, 1840, 420, fill=SHEET, r=14)
    c.text(1220, 270, '直坡', 'bold', 28, MUTED, 'lm')
    c.text(1220, 340, '凹坡（摆线）', 'bold', 28, SPARK, 'lm')
    c.text(1800, 270, f'{min(tt, T_LIN):.2f} 秒' if tt > 0 else '—', 'mono', 28, INK, 'rm')
    c.text(1800, 340, f'{min(tt, T_CYC):.2f} 秒' if tt > 0 else '—', 'mono', 28, INK, 'rm')
    c.text(1510, 395, '（无摩擦的理想情况；弹珠以实测为准）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 6, '直坡最短，可一路都是缓坡，加速慢'),
                (6.2, 13, '凹下去的坡一开头就很陡，弹珠一下子冲起来，后面靠速度跑完'),
                (13.2, 22, '最快的那条叫最速降线，是一段摆线：和第 45 集摆钟里惠更斯用的是同一条曲线')], y=1010)

def _eave(c, ox, oy, kind, a, t, t0):
    H, W = 220, 360
    if kind == 'line':
        pts = [(ox + W * u / 40, oy + H * u / 40) for u in range(41)]
    else:
        pts = [(ox + W * u / 40, oy + H * (0.85 * (1 - (1 - u / 40) ** 2.2) + 0.15 * u / 40)) for u in range(41)]
    poly = pts + [(pts[-1][0], oy + H + 30), (ox, oy + H + 30)]
    c.line(pts, mix(BG, TILE, a), 14)
    x1, y1 = pts[-1]; x0, y0 = pts[-2]
    ang = math.atan2(y1 - y0, x1 - x0)
    wall = x1 - 40
    c.rect(wall - 30, y1 + 10, wall, 900, fill=mix(BG, WALL, a))
    c.line([(ox - 40, 900), (ox + W + 560, 900)], mix(BG, LINE, a), 3)
    v = math.sqrt(2 * 980 * H)
    vx, vy = v * math.cos(ang), v * math.sin(ang)
    hdrop = 900 - y1
    # 落地时间
    g = 980
    tl = (-vy + math.sqrt(vy * vy + 2 * g * hdrop)) / g
    traj = [(x1 + vx * s, y1 + vy * s + 0.5 * g * s * s) for s in [tl * j / 30 for j in range(31)]]
    p = fade(t, t0, t0 + 2.5)
    if p > 0:
        n = max(2, int(31 * p))
        seg(c, traj[:n], mix(BG, WATER, a), 3)
        c.ellipse(traj[n - 1][0], traj[n - 1][1], 9, 9, fill=mix(BG, WATER, a))
    if p >= 1:
        xl = traj[-1][0]
        c.line([(wall, 930), (xl, 930)], mix(BG, GREEN, a), 4)
        c.text((wall + xl) / 2, 965, '落点离墙', 'sans', 22, mix(BG, GREEN, a), 'mm')
    return math.degrees(ang)

def b67_eave(c, t, i):
    corner_tag(c, 'B67 · 檐口微微翘起')
    c.text(60, 96, '屋面上陡下缓：雨水冲下来，在檐口被平平地甩出去', 'serif', 40, INK)
    a1 = _eave(c, 120, 330, 'line', 1.0, t, 3)
    c.text(300, 285, '直坡屋面', 'bold', 28, INK, 'mm')
    a2 = _eave(c, 920, 330, 'curve', fade(t, 6, 7), t, 8)
    c.text(1100, 285, '凹曲屋面（举折）', 'bold', 28, mix(BG, INK, fade(t, 6, 7)), 'mm')
    b = fade(t, 13, 14)
    if b > 0:
        c.rect(1100, 160, 1880, 225, fill=mix(BG, SHEET, b), r=10)
        c.text(1490, 192, f'出水角度：直坡 {a1:.0f}°，凹坡 {a2:.0f}°：越平甩得越远', 'sans', 24, mix(BG, INK, b), 'mm')
    caps(c, t, [(0, 6, '直坡屋面：雨水一路斜着冲下来，在檐口斜斜地往下落，容易打湿墙根'),
                (6.2, 13, '凹曲屋面：上面陡，水很快冲起来；到下面变平，檐口几乎是水平的'),
                (13.2, 22, '同样高度冲下来，出水越平，落得离墙越远。《营造法式》里叫「举折」（「举折就是最速降线」的说法拍摄前核对）')], y=1010)

# ---------------------------------------------------------------- B68 饴糖
def _glu(c, x, y, col, r=22):
    pts = [(x + r * math.cos(math.radians(60 * k + 30)), y + r * math.sin(math.radians(60 * k + 30))) for k in range(6)]
    c.poly(pts, col)

def b68_enzyme(c, t, i):
    corner_tag(c, 'B68 · 酶把淀粉剪成麦芽糖')
    c.text(60, 96, '淀粉是一长串葡萄糖；麦芽里的淀粉酶两个两个地剪', 'serif', 40, INK)
    N = 24
    x0, y = 230, 470
    step = 56
    cut = int(fade(t, 4, 16) * (N // 2))
    GLC = (240, 220, 150)
    for k in range(N):
        pair = k // 2
        released = pair >= N // 2 - cut
        if released:
            j = pair - (N // 2 - cut)
            px = x0 + k * step + 0
            py = y + 220 + (j % 3) * 40
            _glu(c, px, py, (250, 200, 120))
        else:
            _glu(c, x0 + k * step, y, GLC)
            if k < N - 1 and (k + 1) // 2 < N // 2 - cut or (k % 2 == 0 and not released):
                c.line([(x0 + k * step + 22, y), (x0 + (k + 1) * step - 22, y)], MUTED, 3)
    ex = x0 + (N - 2 * cut) * step - 30
    if cut < N // 2:
        mo = 25 + 20 * abs(math.sin(t * 6))
        c.arc(ex, y - 70, 40, 40, mo, 360 - mo, GREEN, 30)
        c.text(ex, y - 140, '淀粉酶', 'bold', 26, GREEN, 'mm')
    c.text(x0 - 40, y, '淀粉', 'sans', 24, MUTED, 'rm')
    c.text(x0 - 40, y + 260, '麦芽糖', 'sans', 24, MUTED, 'rm')
    left = (N // 2 - cut) / (N // 2)
    col = mix((235, 200, 120), (40, 40, 90), left)
    c.rect(1500, 760, 1800, 940, fill=col, r=14)
    c.text(1650, 730, '滴一滴碘伏', 'sans', 24, MUTED, 'mm')
    c.text(1650, 850, '蓝黑' if left > 0.6 else ('变浅' if left > 0.2 else '不变色'), 'bold', 30, INK if left < 0.5 else (230, 230, 240), 'mm')
    caps(c, t, [(0, 4, '米饭里的淀粉，是几百上千个葡萄糖连成的长链，本身不甜'),
                (4.2, 12, '发了芽的麦子里有淀粉酶，它沿着长链两个两个地剪下来：剪下的叫麦芽糖，是甜的'),
                (12.2, 22, '碘伏碰到长链淀粉会变蓝黑；长链剪得越短，颜色越浅')], y=1010)

def _act(T):
    return math.exp(-((T - 62) / 12) ** 2) if T <= 62 else max(0, 1 - (T - 62) / 16)

def b68_temp(c, t, i):
    corner_tag(c, 'B68 · 六十度上下最好')
    c.text(60, 96, '同样的米汤和麦芽：温度不一样，变甜的快慢差很多', 'serif', 40, INK)
    ox, oy, W, H = 200, 820, 900, 520
    c.line([(ox, oy), (ox + W, oy)], LINE, 3)
    c.line([(ox, oy), (ox, oy - H)], LINE, 3)
    pts = [(ox + W * T / 100, oy - H * 0.9 * _act(T)) for T in range(0, 101)]
    c.line(pts, SPARK, 5)
    for T in (20, 40, 60, 80, 100):
        c.text(ox + W * T / 100, oy + 30, f'{T}°', 'mono', 22, MUTED, 'mm')
    c.text(ox + W / 2, oy + 75, '温度（摄氏度）', 'sans', 22, MUTED, 'mm')
    c.text(ox - 20, oy - H / 2, '剪得多快', 'sans', 22, MUTED, 'rm')
    c.text(ox + W * 0.62, oy - H * 0.95, '约 60° 最快（以实测为准）', 'sans', 22, SPARK, 'mm')
    cups = [('室温', 22), ('保温壶约 60°', 60), ('开水', 100)]
    prog = fade(t, 4, 18)
    for k, (nm, T) in enumerate(cups):
        x = 1300 + k * 200
        c.line([(ox + W * T / 100, oy), (ox + W * T / 100, oy - H * 0.9 * _act(T))], mix(BG, INK, 0.5), 2)
        rem = max(0, 1 - prog * 2.2 * max(_act(T), 0.12)) if T < 95 else 1
        col = mix((235, 200, 120), (40, 40, 90), rem)
        c.rect(x - 70, 480, x + 70, 700, fill=col, r=12)
        c.text(x, 740, nm, 'sans', 22, INK, 'mm')
        c.text(x, 450, f'{T}°', 'mono', 24, MUTED, 'mm')
    c.text(1500, 800, '杯里滴碘伏：蓝黑 = 淀粉还在', 'sans', 22, MUTED, 'mm')
    caps(c, t, [(0, 6, '酶是一种蛋白质，温度高一点，它干活就快一点'),
                (6.2, 13, '可太烫就不行了：开水把酶烫坏，米汤一直是淀粉，碘伏一滴还是蓝黑'),
                (13.2, 22, '所以《齐民要术》里熬饴，要把米饭和麦芽保温放着，等它慢慢变甜（实验用的不食用）')], y=1010)


CLIPS = {
 'B66_贴墙': (b66_wall, 22), 'B66_两把伞': (b66_umbrella, 22),
 'B66_片头': (titles.opening(BSER, VOL18, SB18, 6, '明 · 天坛皇穹宇回音壁'), 7),
 'B66_片尾': (titles.closing(BSER, VOL18, SB18, 6, '下集：中国屋顶为什么是凹下去的弧形？'), 7),
 'B67_最速降线': (b67_race, 22), 'B67_檐口': (b67_eave, 22),
 'B67_片头': (titles.opening(BSER, VOL18, SB18, 7, '宋 · 李诫《营造法式》举折'), 7),
 'B67_片尾': (titles.closing(BSER, VOL18, SB18, 7, '下集：没加一粒糖，麦芽怎么把米变甜？'), 7),
 'B68_剪淀粉': (b68_enzyme, 22), 'B68_温度': (b68_temp, 22),
 'B68_片头': (titles.opening(BSER, VOL18, SB18, 8, '北魏《齐民要术》作饴法'), 7),
 'B68_片尾': (titles.closing(BSER, VOL18, SB18, 8, '下集：一锅糖水，怎么长出透明的大冰糖？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
