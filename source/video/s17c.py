"""第十七季（第五层）第三批：E98 互联网、E99 磁悬浮、E100 直升机 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s17a import S17A, SER17, VOL17

PKT = (240, 190, 80)
MAGN = (220, 80, 70)
MAGS = (70, 120, 220)
CU = (200, 120, 70)

NODES = {'A': (220, 520), 'B': (560, 300), 'C': (560, 740), 'D': (960, 220), 'E': (960, 520), 'F': (960, 820), 'G': (1360, 300), 'H': (1360, 740), 'Z': (1700, 520)}
EDGES = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'E'), ('C', 'F'), ('D', 'G'), ('E', 'G'), ('E', 'H'), ('F', 'H'), ('G', 'Z'), ('H', 'Z')]
ROUTES = [['A', 'B', 'D', 'G', 'Z'], ['A', 'C', 'F', 'H', 'Z'], ['A', 'B', 'E', 'H', 'Z'], ['A', 'C', 'E', 'G', 'Z']]

def net(c, a=1.0, broken=None):
    for u, v in EDGES:
        col = NRED if broken and {u, v} == set(broken) else LINE
        c.line([NODES[u], NODES[v]], mix(BG, col, a), 3)
    for k, (x, y) in NODES.items():
        c.ellipse(x, y, 30, 30, fill=mix(BG, SHEET, a), outline=mix(BG, MUTED, a), width=2)
        c.text(x, y, k if k not in 'AZ' else ('你' if k == 'A' else '他'), 'bold', 24, mix(BG, INK, a), 'mm')

def along(route, u):
    pts = [NODES[k] for k in route]
    seglen = len(pts) - 1
    s = min(max(u, 0), 1) * seglen
    i = min(int(s), seglen - 1)
    f = s - i
    return pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f

# ---------------------------------------------------------------- E98 互联网
def e98_packets(c, t, i):
    corner_tag(c, '第 98 集 · 拆成小包，各走各的路')
    c.text(60, 96, '一句话拆成编号小包：走不同的路，到了再按号拼回', 'serif', 40, INK)
    net(c)
    words = ['你', '好', '世', '界', '！', '从', '零', '造']
    arrived = []
    for k, w in enumerate(words):
        t0 = 1 + k * 0.9
        dur = 5 + (k * 37 % 5) * 0.8
        u = (t - t0) / dur
        if u < 0: continue
        if u >= 1:
            arrived.append((t0 + dur, k, w)); continue
        x, y = along(ROUTES[k % 4], u)
        c.rect(x - 34, y - 24, x + 34, y + 24, fill=PKT, r=6)
        c.text(x, y, f'{k + 1}{w}', 'bold', 20, BG, 'mm')
    arrived.sort()
    c.text(1560, 900, '到达顺序：' + ' '.join(f'{k + 1}' for _, k, _ in arrived), 'mono', 24, MUTED, 'rm')
    if len(arrived) == len(words):
        c.text(1560, 960, '按编号拼回：' + ''.join(words), 'bold', 30, GREEN, 'rm')
    caps(c, t, [(0, 7, '一封邮件、一张照片，都会被拆成许多小包，每包写上发给谁、第几号'),
                (7.2, 14, '小包交给路由器，路由器看哪条路空就往哪走：同一封信的小包，可能走完全不同的路'),
                (14.2, 22, '先发的不一定先到；到了以后，按编号重新拼好：这叫分组交换')], y=1040)

def e98_resend(c, t, i):
    corner_tag(c, '第 98 集 · 丢了就补')
    c.text(60, 96, '一条线断了：小包绕路走；丢了一包：要求重发', 'serif', 40, INK)
    broken = ('B', 'D') if t > 4 else None
    net(c, broken=broken)
    if broken:
        x, y = (NODES['B'][0] + NODES['D'][0]) / 2, (NODES['B'][1] + NODES['D'][1]) / 2
        c.text(x, y - 40, '断了', 'bold', 26, NRED, 'mm')
    route = ['A', 'B', 'E', 'G', 'Z'] if broken else ['A', 'B', 'D', 'G', 'Z']
    u = ((t - 1) % 5) / 5
    x, y = along(route, u)
    c.rect(x - 30, y - 22, x + 30, y + 22, fill=PKT, r=6)
    c.text(x, y, '3', 'bold', 22, BG, 'mm')
    a = fade(t, 11, 12)
    c.rect(1180, 860, 1840, 980, fill=mix(BG, SHEET, a), r=12)
    c.text(1210, 895, '他：收到 1、2、4、5……缺 3 号！', 'sans', 24, mix(BG, INK, a), 'lm')
    c.text(1210, 940, '你：好，3 号再发一遍', 'sans', 24, mix(BG, GREEN, a), 'lm')
    caps(c, t, [(0, 4, '原来的路线：经过 B、D、G'),
                (4.2, 11, '中间一根线断了：路由器马上换一条路，小包绕开故障继续走'),
                (11.2, 22, '要是有一包真丢了，对方发现编号缺了，就请你重发。1969 年阿帕网、1974 年 TCP/IP，定下了这套规矩（拍摄前核对）')], y=1040)

# ---------------------------------------------------------------- E99 磁悬浮
def e99_eddy(c, t, i):
    corner_tag(c, '第 99 集 · 铜管里的「刹车」')
    c.text(60, 96, '同一块磁铁：塑料管里一下掉下去，铜管里慢慢飘', 'serif', 40, INK)
    pipes = [('塑料管', MUTED, 1.0), ('铝管', (190, 190, 200), 0.25), ('铜管', CU, 0.1)]
    for k, (nm, col, sp) in enumerate(pipes):
        x = 420 + k * 500
        c.rect(x - 60, 200, x - 40, 900, fill=col)
        c.rect(x + 40, 200, x + 60, 900, fill=col)
        c.text(x, 940, nm, 'bold', 28, INK, 'mm')
        if k == 0:
            y = 220 + min(1, (t % 6) / 0.6) * 660
        else:
            y = 220 + min(1, (t * sp * 0.25) % 1.4) * 660
        y = min(y, 870)
        c.rect(x - 34, y - 20, x + 34, y, fill=MAGN)
        c.rect(x - 34, y, x + 34, y + 20, fill=MAGS)
        if k > 0:
            for dy, sgn in ((-60, 1), (80, -1)):
                c.arc(x, y + dy, 70, 16, 0, 360, mix(BG, SPARK, 0.8), 3)
    a = fade(t, 8, 9)
    c.text(1660, 360, '磁铁往下掉', 'sans', 24, mix(BG, INK, a), 'mm')
    c.text(1660, 400, '管壁里的磁场在变', 'sans', 24, mix(BG, INK, a), 'mm')
    c.text(1660, 440, '→ 感应出一圈圈电流（黄圈）', 'sans', 24, mix(BG, SPARK, a), 'mm')
    c.text(1660, 480, '→ 电流的磁场反过来顶住它', 'bold', 24, mix(BG, GREEN, a), 'mm')
    caps(c, t, [(0, 6, '一块钕磁铁从塑料管里落下：咚，不到半秒'),
                (6.2, 13, '同一块磁铁放进铜管：慢悠悠地往下飘。可铜明明不吸磁铁'),
                (13.2, 22, '磁铁一动，铜管里就感应出一圈圈电流（第 04 集磁生电），这些电流的磁场总是反抗磁铁的运动：这叫楞次定律')], y=1010)

def e99_maglev(c, t, i):
    corner_tag(c, '第 99 集 · 让列车飘起来')
    c.text(60, 96, '用磁力托起车厢：没有轮子和铁轨的摩擦', 'serif', 40, INK)
    lift = 18 * fade(t, 2, 4)
    x = 200 + 700 * fade(t, 6, 14) ** 1.5
    c.rect(100, 760, 1820, 800, fill=MUTED)
    for k in range(18):
        gx = 120 + k * 95
        c.rect(gx, 740, gx + 70, 760, fill=MAGN if k % 2 else MAGS)
    c.poly([(x, 740 - lift), (x + 520, 740 - lift), (x + 600, 680 - lift), (x + 600, 560 - lift), (x + 60, 560 - lift), (x, 620 - lift)], (220, 225, 235))
    for k in range(6):
        c.rect(x + 40 + k * 85, 728 - lift, x + 100 + k * 85, 740 - lift, fill=MAGN)
    a = fade(t, 3, 4)
    c.text(x + 300, 520 - lift, f'悬浮约 1 厘米（示意）', 'sans', 24, mix(BG, INK, a), 'mm')
    b = fade(t, 12, 13)
    c.rect(200, 220, 1720, 420, fill=mix(BG, SHEET, b), r=12)
    c.text(960, 270, '车上和轨道里的电磁铁：一部分负责托起，一部分一前一后地「推拉」车厢前进', 'sans', 26, mix(BG, INK, b), 'mm')
    c.text(960, 320, '就像把第 58 集的电动机「拉直」铺在地上', 'bold', 26, mix(BG, GREEN, b), 'mm')
    c.text(960, 370, '2004 年上海磁浮线开通商业运营，最高时速约 430 千米（拍摄前核对）', 'sans', 24, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 6, '列车跑得越快，车轮和铁轨之间的摩擦、震动就越成问题'),
                (6.2, 13, '磁悬浮列车用电磁铁把车厢托起约一厘米：车和轨道根本不接触'),
                (13.2, 22, '再让轨道里的磁场一节节往前「跑」，拖着车厢走：就是一台被拉直的电动机')], y=1010)

# ---------------------------------------------------------------- E100 直升机
def heli(c, cx, cy, body_ang, rotor_ang, tail_on, a=1.0):
    ca, sa = math.cos(body_ang), math.sin(body_ang)
    def p(dx, dy): return (cx + dx * ca - dy * sa, cy + dx * sa + dy * ca)
    c.poly([p(-60, -40), p(60, -40), p(80, 0), p(60, 40), p(-60, 40), p(-80, 0)], mix(BG, (200, 205, 215), a))
    c.line([p(-70, 0), p(-260, 0)], mix(BG, (200, 205, 215), a), 12)
    if tail_on:
        c.line([p(-260, -40), p(-260, 40)], mix(BG, SPARK, a), 6)
    for k in range(4):
        q = rotor_ang + k * math.pi / 2
        c.line([(cx, cy), (cx + 230 * math.cos(q), cy + 230 * math.sin(q))], mix(BG, MUTED, a), 6)
    c.ellipse(cx, cy, 10, 10, fill=mix(BG, INK, a))

def e100_torque(c, t, i):
    corner_tag(c, '第 100 集 · 旋翼往这边转，机身往那边转')
    c.text(60, 96, '俯视：没有尾桨，机身会跟旋翼反着打转', 'serif', 40, INK)
    heli(c, 520, 560, -t * 0.8, t * 6, False)
    c.text(520, 900, '没有尾桨：机身反着转', 'bold', 28, NRED, 'mm')
    heli(c, 1380, 560, 0.0, t * 6, True)
    c.text(1380, 900, '尾桨往侧面推：机身稳住', 'bold', 28, GREEN, 'mm')
    a = fade(t, 8, 9)
    c.arrow(1380 - 260, 560, 1380 - 260, 560 + 120 * a, mix(BG, SPARK, a), 5, 18)
    caps(c, t, [(0, 7, '发动机让旋翼朝一个方向转，旋翼也同时把机身往反方向扭'),
                (7.2, 14, '没有东西拦着，机身就会跟着反转：这叫反扭矩（坐转椅转风扇就能感觉到）'),
                (14.2, 22, '尾巴上的小旋翼朝侧面吹，正好把这股扭劲顶回去。1939 年西科斯基的 VS-300 就是这样稳住的（拍摄前核对）')], y=1010)

def e100_auto(c, t, i):
    corner_tag(c, '第 100 集 · 纸直升机自己转')
    c.text(60, 96, '往下掉的时候，迎面的风把桨叶吹得转起来', 'serif', 40, INK)
    for k, (L, sp) in enumerate(((60, 1.6), (100, 1.0), (140, 0.7))):
        x = 420 + k * 540
        a = fade(t, 1 + k * 0.5, 2 + k * 0.5)
        y = 260 + min(1, (t * 0.06 * sp) % 1.1) * 440
        ang = t * 10 * sp
        w = L * abs(math.cos(ang))
        c.rect(x - 8, y, x + 8, y + 80, fill=mix(BG, (230, 230, 220), a))
        c.line([(x, y), (x - w, y - 20)], mix(BG, (240, 200, 90), a), 10)
        c.line([(x, y), (x + w, y - 20)], mix(BG, (240, 200, 90), a), 10)
        c.text(x, 920, f'桨叶 {L // 12} 厘米', 'bold', 26, mix(BG, INK, a), 'mm')
        for j in range(3):
            c.arrow(x - 60 + j * 60, y + 200, x - 60 + j * 60, y + 130, mix(BG, (120, 170, 220), a * 0.7), 3, 12)
    b = fade(t, 12, 13)
    c.text(960, 190, '桨叶越长，落得越慢（以实测为准）', 'sans', 24, mix(BG, MUTED, b), 'mm')
    caps(c, t, [(0, 7, '纸直升机往下掉，空气从下往上吹过斜着的桨叶，把它们推得转起来'),
                (7.2, 14, '一转起来，桨叶又像机翼一样产生升力，下落就慢了：这叫自转'),
                (14.2, 22, '真直升机发动机停了，也靠自转慢慢滑降落地：和 B40 竹蜻蜓、第 86 集机翼是同一件事')], y=1010)

CLIPS = {
 'E98_分包': (e98_packets, 22), 'E98_重传': (e98_resend, 22),
 'E98_片头': (titles.opening(SER17, VOL17, S17A, 6, '1969 年阿帕网 · 1974 年 TCP/IP'), 7),
 'E98_片尾': (titles.closing(SER17, VOL17, S17A, 6, '下集：一块磁铁掉进铜管，为什么慢得像羽毛？'), 7),
 'E99_涡流': (e99_eddy, 22), 'E99_悬浮': (e99_maglev, 22),
 'E99_片头': (titles.opening(SER17, VOL17, S17A, 7, '2004 年 · 上海磁浮线'), 7),
 'E99_片尾': (titles.closing(SER17, VOL17, S17A, 7, '下集：直升机尾巴上，为什么还要一个小旋翼？'), 7),
 'E100_反扭矩': (e100_torque, 22), 'E100_自转': (e100_auto, 22),
 'E100_片头': (titles.opening(SER17, VOL17, S17A, 8, '1939 年 · 西科斯基 VS-300'), 7),
 'E100_片尾': (titles.closing(SER17, VOL17, S17A, 8, '下集：卫星为什么不会掉下来？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
