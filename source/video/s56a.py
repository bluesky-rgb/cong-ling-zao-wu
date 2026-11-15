"""第五十六季（古法解密 25.0：园林与庭院）第一批：B250 漏窗、B251 曲水流觞、B252 叠石假山 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg

SB56 = [('B250', '漏窗'), ('B251', '曲水流觞'), ('B252', '叠石假山'), ('B253', '花街铺地'), ('B254', '竹篱笆'),
        ('B255', '照壁'), ('B256', '石凳'), ('B257', '倒影池'), ('B258', '门槛'), ('B259', '太平缸')]
VOL56 = '第五十六季 · 古法解密 25.0'
WALL = (232, 228, 218)
TILE = (90, 100, 110)
WATER = (120, 170, 230)
STONE = (165, 160, 150)
LEAF = (110, 170, 110)
WOODC = (170, 125, 80)


def lattice(c, cx, cy, w, col, width=6):
    """画一个简单的花格：外框 + 斜向菱形格。"""
    c.rect(cx - w, cy - w, cx + w, cy + w, outline=col, width=width + 2)
    n = 4
    for k in range(-n, n + 1):
        d = k * w / n * 2
        pts1 = [(cx - w, cy - w + d), (cx + w, cy + w + d)]
        pts2 = [(cx - w, cy + w - d), (cx + w, cy - w - d)]
        for (x0, y0), (x1, y1) in [pts1, pts2]:
            # 裁到方框里
            def clip(x0, y0, x1, y1):
                out = []
                for j in range(41):
                    s = j / 40
                    x, y = x0 + (x1 - x0) * s, y0 + (y1 - y0) * s
                    if cx - w <= x <= cx + w and cy - w <= y <= cy + w:
                        out.append((x, y))
                return out
            p = clip(x0, y0, x1, y1)
            if len(p) > 1:
                c.line([p[0], p[-1]], col, width)


# ---------------------------------------------------------------- B250 漏窗
def b250_light(c, t, i):
    corner_tag(c, 'B250 · 光和风一格格穿过墙')
    c.text(60, 96, '实墙把光和风全挡住；开一扇花格漏窗，光一格格透过来，风变成一股股细流穿过去', 'serif', 36, INK)
    win = t > 7.2
    wx = 860
    c.rect(wx - 30, 220, wx + 30, 900, fill=mix(BG, WALL, 0.9))
    if win:
        c.rect(wx - 30, 420, wx + 30, 700, fill=BG)
        for k in range(7):
            y = 430 + k * 40
            c.rect(wx - 30, y, wx + 30, y + 14, fill=mix(BG, WALL, 0.9))
    # 左边：灯光和风
    c.ellipse(260, 560, 50, 50, fill=mix(BG, SPARK, 1.0))
    c.text(260, 650, '光', 'bold', 28, INK, 'mm')
    for k in range(5):
        y = 470 + k * 45
        ph = (t * 120 + k * 50) % 300
        x = 360 + ph
        if x < wx - 40:
            c.arrow(x, y, x + 60, y, mix(BG, FIELD, 0.9), 4, 12)
    c.text(480, 380, '风', 'bold', 28, FIELD, 'mm')
    # 右边
    if win:
        for k in range(7):
            y = 437 + k * 40 + 20
            c.poly([(wx + 30, y - 6), (wx + 30, y + 6), (wx + 600, y + 40), (wx + 600, y - 40 + 20)], mix(BG, SPARK, 0.25))
        for k in range(4):
            y = 450 + k * 70
            x = wx + 60 + ((t * 120 + k * 60) % 300)
            c.arrow(x, y, x + 50, y, mix(BG, FIELD, 0.9), 3, 10)
        sway = 30 * math.sin(t * 6)
        c.line([(1500, 420), (1500 + sway, 620)], INK, 6)
        c.text(1500, 680, '纸巾飘起来', 'bold', 28, GREEN, 'mm')
    else:
        c.line([(1500, 420), (1500, 620)], INK, 6)
        c.text(1500, 680, '纸巾不动', 'bold', 28, NRED, 'mm')
    c.text(1180, 300, '墙后', 'sans', 26, MUTED, 'mm')
    caps(c, t, [(0, 7, '一堵实墙：手电筒的光、风扇的风，全被挡在前面'),
                (7.2, 14, '墙上刻一扇花格漏窗：光一格格透过来，在后面投出花样'),
                (14.2, 22, '风也从格子里穿过去，墙后的纸巾飘起来了（示意，以实测为准）')], y=1010)


def b250_frame(c, t, i):
    corner_tag(c, 'B250 · 把景色框成一幅画')
    c.text(60, 96, '透过漏窗看墙后的景：离得近，看到一大片；退远几步，只看到框里的一小幅，像墙上挂了一幅画', 'serif', 36, INK)
    far = t > 7.2
    # 墙后景色：树、假山
    def scene(x0, y0, sc):
        c.ellipse(x0, y0 - 60 * sc, 90 * sc, 80 * sc, fill=mix(BG, LEAF, 1.0))
        c.rect(x0 - 10 * sc, y0 - 10 * sc, x0 + 10 * sc, y0 + 80 * sc, fill=mix(BG, WOODC, 1.0))
        c.poly([(x0 + 140 * sc, y0 + 80 * sc), (x0 + 220 * sc, y0 - 40 * sc), (x0 + 300 * sc, y0 + 80 * sc)], mix(BG, STONE, 1.0))
    cx, cy = 960, 560
    w = 230 if not far else 120
    c.rect(cx - 520, cy - 300, cx + 520, cy + 300, fill=mix(BG, WALL, 0.85))
    c.rect(cx - w, cy - w, cx + w, cy + w, fill=mix(BG, (40, 60, 70), 1.0))
    if not far:
        scene(cx - 100, cy + 20, 1.1)
    else:
        scene(cx - 60, cy + 30, 0.6)
    lattice(c, cx, cy, w, mix(BG, WALL, 0.85), 5)
    c.text(cx, cy + 340, '眼睛贴近：看到一大片' if not far else '退远几步：框里只剩一小幅画', 'bold', 30, INK, 'mm')
    caps(c, t, [(0, 7, '眼睛贴近漏窗：墙后的树和假山看到一大片'),
                (7.2, 14, '往后退几步：框里只剩一小幅，像一幅装了花边的画'),
                (14.2, 22, '园林里走几步，每扇漏窗里的「画」都不一样，这叫框景')], y=1010)


# ---------------------------------------------------------------- B251 曲水流觞
def bend_path(s):
    """S 形水渠中线：s 从 0 到 1。"""
    x = 300 + 1320 * s
    y = 560 + 200 * math.sin(s * math.pi * 3)
    return x, y


def b251_bend(c, t, i):
    corner_tag(c, 'B251 · 弯道外侧水快')
    c.text(60, 96, '水在弯道里拐弯：外侧水流得快，内侧水流得慢，漂着的杯子和碎纸被推向弯道外侧', 'serif', 36, INK)
    cx, cy, R0, R1 = 960, 760, 260, 460
    c.arc(cx, cy, R1, R1, 180, 360, mix(BG, WATER, 0.55), R1 - R0)
    c.arc(cx, cy, R0, R0, 180, 360, mix(BG, STONE, 1.0), 8)
    c.arc(cx, cy, R1, R1, 180, 360, mix(BG, STONE, 1.0), 8)
    c.text(cx, cy - R0 + 60, '内侧', 'bold', 28, INK, 'mm')
    c.text(cx, cy - R1 - 40, '外侧', 'bold', 28, INK, 'mm')
    for r, sp in [(R0 + 40, 0.5), (R0 + 100, 0.75), (R1 - 100, 1.0), (R1 - 40, 1.2)]:
        for k in range(4):
            a = 180 + ((t * 18 * sp + k * 45) % 180)
            x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
            a2 = math.radians(a + 8 * sp)
            c.arrow(x, y, cx + r * math.cos(a2), cy + r * math.sin(a2), mix(BG, FIELD, 1.0), 3 + int(sp * 2), 12)
    if t > 7.2:
        k = min(1.0, (t - 7.2) / 8)
        a = math.radians(200 + 140 * k)
        r = R0 + 60 + (R1 - R0 - 120) * k
        c.ellipse(cx + r * math.cos(a), cy + r * math.sin(a), 26, 26, fill=mix(BG, SPARK, 1.0))
        c.text(cx + 560, cy - 80, '瓶盖被推向外侧', 'bold', 28, SPARK, 'mm')
    caps(c, t, [(0, 7, '水渠拐弯：外侧的水走得快，内侧的水走得慢'),
                (7.2, 14, '放一个瓶盖当酒杯：它慢慢往弯道外侧靠'),
                (14.2, 22, '杯子贴着外侧漂，到下一个弯又换一边（示意，本集不用酒）')], y=1010)


def b251_drift(c, t, i):
    corner_tag(c, 'B251 · 弯渠漂得更慢')
    c.text(60, 96, '直渠和弯渠一样长、一样陡：瓶盖在直渠里一下就漂到头，弯渠里一拐一停，漂得慢多了', 'serif', 36, INK)
    # 直渠
    c.line([(300, 330), (1620, 330)], mix(BG, WATER, 0.6), 50)
    c.text(200, 330, '直渠', 'bold', 28, INK, 'mm')
    # 弯渠
    pts = [bend_path(j / 80) for j in range(81)]
    pts = [(x, y + 160) for x, y in pts]
    seg(c, pts, mix(BG, WATER, 0.6), 50)
    c.text(200, 720, '弯渠', 'bold', 28, INK, 'mm')
    s1 = min(1.0, t / 8)
    c.ellipse(300 + 1320 * s1, 330, 22, 22, fill=mix(BG, SPARK, 1.0))
    s2 = min(1.0, t / 20) ** 1.1
    x, y = bend_path(s2)
    c.ellipse(x, y + 160, 22, 22, fill=mix(BG, SPARK, 1.0))
    c.text(1700, 330, f'{min(t, 8):.0f} 秒' if t < 8 else '到了', 'mono', 28, GREEN, 'mm')
    c.text(1700, 720, f'{min(t, 20):.0f} 秒' if t < 20 else '到了', 'mono', 28, GREEN, 'mm')
    c.text(960, 960, '秒数是示意，以实测为准', 'sans', 24, MUTED, 'mm')
    caps(c, t, [(0, 7, '同时放下两个瓶盖：直渠里的那个很快漂到头'),
                (7.2, 14, '弯渠里的瓶盖一路拐弯，常常靠在岸边打转'),
                (14.2, 22, '漂得慢，停的地方也多：古人才有时间作诗')], y=1010)


# ---------------------------------------------------------------- B252 叠石假山
def stone(c, cx, cy, w, h, col):
    c.poly([(cx - w, cy + h), (cx - w * 0.8, cy - h * 0.6), (cx - w * 0.2, cy - h), (cx + w * 0.7, cy - h * 0.8),
            (cx + w, cy + h * 0.2), (cx + w * 0.8, cy + h)], col)


def b252_center(c, t, i):
    corner_tag(c, 'B252 · 重心落在支撑面里')
    c.text(60, 96, '上面的石头比下面大也不一定倒：从重心垂下一根线，落在下面石头的支撑面里就稳，落到外面就倒', 'serif', 36, INK)
    gy = 880
    c.line([(200, gy), (1720, gy)], LINE, 4)
    for j, (off, ok) in enumerate([(40, True), (190, False)]):
        bx = 560 + j * 800
        stone(c, bx, gy - 90, 110, 90, mix(BG, STONE, 1.0))
        c.line([(bx - 110, gy - 180), (bx + 110, gy - 180)], mix(BG, GREEN, 0.8), 6)
        show = t > 3 + j * 7
        tilt = 0
        if not ok and t > 16:
            tilt = min(35, (t - 16) * 18)
        ux, uy = bx + off, gy - 180 - 110
        ang = math.radians(tilt)
        pts = [(-200, 110), (-170, -60), (-60, -110), (150, -90), (200, 20), (170, 110)]
        px, py = bx + 110, gy - 180
        rp = []
        for dx, dy in pts:
            x, y = ux + dx, uy + dy
            x, y = px + (x - px) * math.cos(ang) - (y - py) * math.sin(ang), py + (x - px) * math.sin(ang) + (y - py) * math.cos(ang)
            rp.append((x, y))
        c.poly(rp, mix(BG, (185, 180, 170), 1.0))
        if show:
            gx = ux + (px - ux) * 0 if not tilt else rp[0][0] * 0 + (sum(p[0] for p in rp) / 6)
            gx = sum(p[0] for p in rp) / 6
            gyy = sum(p[1] for p in rp) / 6
            c.ellipse(gx, gyy, 12, 12, fill=mix(BG, SPARK, 1.0))
            c.line([(gx, gyy), (gx, gy - 180)], SPARK, 3)
            inside = bx - 110 <= gx <= bx + 110
            c.text(bx, gy + 60, '重心线落在里面：稳' if inside else '重心线落到外面：倒', 'bold', 28, GREEN if inside else NRED, 'mm')
    caps(c, t, [(0, 7, '下面一块小石头，上面压一块大石头：上大下小'),
                (7.2, 14, '从上面石头的重心垂下一根线：落在下面石头的支撑面里，就稳'),
                (14.2, 22, '把大石头往外挪：重心线一出支撑面，它就翻下来（只在托盘里叠）')], y=1010)


def b252_shim(c, t, i):
    corner_tag(c, 'B252 · 缝里塞小石片')
    c.text(60, 96, '两块石头接触的地方凹凸不平，只碰着一两个点就会晃；缝里塞进小石片，接触点变多，就稳了', 'serif', 36, INK)
    cx, gy = 960, 820
    stone(c, cx, gy - 100, 260, 100, mix(BG, STONE, 1.0))
    shim = t > 8
    rock = 0 if shim else 8 * math.sin(t * 3)
    ang = math.radians(rock)
    px, py = cx, gy - 200
    pts = [(-230, -20), (-200, -200), (-40, -260), (180, -220), (240, -40), (200, 0), (-120, 0)]
    rp = [(px + dx * math.cos(ang) - dy * math.sin(ang), py + dx * math.sin(ang) + dy * math.cos(ang)) for dx, dy in pts]
    c.poly(rp, mix(BG, (185, 180, 170), 1.0))
    c.ellipse(px, py, 10, 10, fill=mix(BG, NRED, 1.0))
    if shim:
        for dx in (-160, 150):
            c.poly([(cx + dx - 40, gy - 196), (cx + dx + 40, gy - 196), (cx + dx + 30, gy - 210), (cx + dx - 30, gy - 210)], mix(BG, SPARK, 1.0))
            c.ellipse(cx + dx, gy - 203, 8, 8, fill=mix(BG, GREEN, 1.0))
        c.text(cx, gy + 80, '三个点撑住：不晃了', 'bold', 30, GREEN, 'mm')
    else:
        c.text(cx, gy + 80, '只碰着一个点：一碰就晃', 'bold', 30, NRED, 'mm')
    caps(c, t, [(0, 7, '两块石头凹凸不平：只碰着中间一个点，像跷跷板一样晃'),
                (7.2, 14, '在两边的缝里塞进小石片：接触的点从一个变成三个'),
                (14.2, 22, '三个点撑住一个面，假山就稳了：工匠叫它「垫石」（待核）')], y=1010)


CLIPS = {
 'B250_透光': (b250_light, 22), 'B250_框景': (b250_frame, 22),
 'B250_片头': (titles.opening(BSER, VOL56, SB56, 0, '苏州园林白墙上的花格漏窗'), 7),
 'B250_片尾': (titles.closing(BSER, VOL56, SB56, 0, '下集：水渠为什么修得弯弯曲曲？'), 7),
 'B251_弯道': (b251_bend, 22), 'B251_漂流': (b251_drift, 22),
 'B251_片头': (titles.opening(BSER, VOL56, SB56, 1, '东晋兰亭雅集「曲水流觞」'), 7),
 'B251_片尾': (titles.closing(BSER, VOL56, SB56, 1, '下集：上大下小的假山怎么不倒？'), 7),
 'B252_重心': (b252_center, 22), 'B252_垫片': (b252_shim, 22),
 'B252_片头': (titles.opening(BSER, VOL56, SB56, 2, '宋代艮岳用太湖石叠山'), 7),
 'B252_片尾': (titles.closing(BSER, VOL56, SB56, 2, '下集：卵石小路为什么不积水？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
