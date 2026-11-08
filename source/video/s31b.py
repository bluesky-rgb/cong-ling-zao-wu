"""第三十一季（第十二层：城市里的机器）第二批：E165 自动门、E166 条形码、E167 公交卡 —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s29a import METAL, WATER_L
from s31a import S31A, SER31, VOL31, CAR, RED

IRC = (230, 90, 90)
GLASS = (150, 190, 220)
CARD = (90, 170, 140)
COIL = (230, 160, 80)

L = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
R_ = [''.join('1' if b == '0' else '0' for b in s) for s in L]
G_ = [s[::-1] for s in R_]
PAR = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']


def ean_bits(code):
    d = [int(ch) for ch in code]
    bits = '101'
    for k in range(6):
        bits += (L if PAR[d[0]][k] == 'L' else G_)[d[1 + k]]
    bits += '01010'
    for k in range(6):
        bits += R_[d[7 + k]]
    bits += '101'
    return bits


def check_digit(code12):
    d = [int(ch) for ch in code12]
    s = sum(d[0::2]) + 3 * sum(d[1::2])
    return (10 - s % 10) % 10, sum(d[0::2]), sum(d[1::2])


# ---------------------------------------------------------------- E165 自动门
def e165_sense(c, t, i):
    corner_tag(c, '第 165 集 · 看不见的光，照到人就反射回来')
    c.text(60, 96, '门顶感应器一直发出看不见的红外线或微波：有人走进来，反射回来的信号一变，门就打开', 'serif', 36, INK)
    gy = 860
    dx = 900
    c.line([(100, gy), (1820, gy)], LINE, 3)
    c.rect(dx - 10, 260, dx + 10, gy, fill=METAL)
    px = 200 + min(1, t / 12) * 480
    near = px > dx - 420
    op = min(1, max(0, (px - (dx - 420)) / 120))
    c.rect(dx - 10, 300, dx + 10 + 0, 300, fill=METAL)
    c.rect(dx + 14 + 200 * op, 330, dx + 200 + 200 * op, gy, fill=mix(BG, GLASS, 0.5), outline=GLASS, width=2)
    c.rect(dx - 70, 260, dx + 70, 320, fill=(40, 40, 46), r=8)
    c.ellipse(dx - 30, 300, 10, 10, fill=IRC)
    for k in range(7):
        a = math.radians(105 + k * 7)
        r = 520
        c.line([(dx - 30, 310), (dx - 30 + r * math.cos(a), 310 + r * math.sin(a))], mix(BG, IRC, 0.25), 2)
    c.ellipse(px, gy - 230, 28, 28, fill=(225, 180, 150))
    c.rect(px - 30, gy - 200, px + 30, gy - 70, fill=CAR, r=10)
    c.line([(px - 15, gy - 70), (px - 25 - 15 * math.sin(t * 6), gy)], INK, 8)
    c.line([(px + 15, gy - 70), (px + 25 + 15 * math.sin(t * 6), gy)], INK, 8)
    if near:
        c.line([(px, gy - 200), (dx - 30, 310)], IRC, 3)
        c.text(px - 120, gy - 300, '反射回来的信号变了', 'bold', 22, IRC, 'mm')
    c.rect(1350, 360, 1840, 640, fill=SHEET, r=14)
    c.text(1595, 410, '感应器收到的信号', 'bold', 24, INK, 'mm')
    c.text(1595, 500, '有变化 → 开门' if near else '没变化 → 关着', 'bold', 32, GREEN if near else MUTED, 'mm')
    c.text(1595, 580, '（示意）', 'sans', 18, MUTED, 'mm')
    caps(c, t, [(0, 7, '自动门门顶装着一个小盒子，朝门前的地面发出人眼看不见的红外线或微波'),
                (7.2, 14, '没人时，地面反射回来的信号一直不变；人一走进这片区域，反射的信号就变了'),
                (14.2, 22, '感应器一发现变化，就让电动机把门拉开：所以有的门你站着不动，它反而会关上（示意）')], y=1010)


def e165_remote(c, t, i):
    corner_tag(c, '第 165 集 · 手机摄像头能看见遥控器的光')
    c.text(60, 96, '遥控器发的是红外光，人眼看不见，手机摄像头看得见；对着白墙按，反射的光照样能开电视', 'serif', 38, INK)
    rx, ry = 420, 600
    c.rect(rx - 60, ry - 180, rx + 60, ry + 180, fill=(50, 50, 56), r=30)
    blink = (int(t * 6) % 2 == 0) and t > 3
    c.ellipse(rx, ry - 190, 14, 10, fill=IRC if blink else (80, 60, 60))
    c.text(rx, ry + 230, '遥控器', 'sans', 22, MUTED, 'mm')
    c.rect(700, 320, 1100, 620, outline=METAL, width=4, r=18)
    c.text(900, 300, '手机屏幕里', 'sans', 20, MUTED, 'mm')
    c.ellipse(900, 470, 60 if blink else 8, 40 if blink else 6, fill=mix((40, 40, 46), (240, 200, 240), 0.9 if blink else 0.1))
    wx = 1400
    c.rect(wx, 250, wx + 30, 900, fill=(220, 220, 220))
    c.text(wx + 15, 220, '白墙', 'sans', 22, MUTED, 'mm')
    tvx, tvy = 1650, 760
    on = t > 12
    c.rect(tvx - 140, tvy - 90, tvx + 140, tvy + 90, fill=mix((20, 20, 24), (90, 150, 220), 0.7 if on else 0), outline=METAL, width=6, r=8)
    c.text(tvx, tvy + 130, '电视' + ('（开了）' if on else ''), 'sans', 22, GREEN if on else MUTED, 'mm')
    if 8 < t:
        c.line([(rx, ry - 190), (wx, 420)], mix(BG, IRC, 0.6), 3)
        c.line([(wx, 420), (tvx - 140, tvy - 40)], mix(BG, IRC, 0.6), 3)
    caps(c, t, [(0, 7, '按下遥控器，眼睛看那颗小灯，什么也没有'),
                (7.2, 14, '用手机摄像头对着它按：屏幕里一闪一闪，那是红外光；背对电视对着白墙按，光被墙反射过去'),
                (14.2, 22, '电视照样开了：自动门的红外感应器，用的就是这种看不见、能反射的光（示意）')], y=1010)


# ---------------------------------------------------------------- E166 条形码
CODE = '6901234567892'


def e166_bars(c, t, i):
    corner_tag(c, '第 166 集 · 黑条是 1，白条是 0')
    c.text(60, 96, '条形码就是一串数字画成的粗细条纹：每个数字占 7 个小格，黑格是 1、白格是 0；扫描器的红光扫过去，读出黑白的节奏', 'serif', 34, INK)
    bits = ean_bits(CODE)
    x0, w, y0, h = 300, 10, 260, 420
    c.rect(x0 - 40, y0 - 30, x0 + 95 * w + 40, y0 + h + 90, fill=(245, 245, 240), r=8)
    for k, b in enumerate(bits):
        if b == '1':
            c.rect(x0 + k * w, y0, x0 + (k + 1) * w, y0 + h, fill=(20, 20, 20))
    c.rect(x0 - 40, y0 - 30, x0 + len(bits) * w + 40, y0 + h + 90, outline=LINE, width=2, r=8)
    c.rect(x0 - 38, y0 - 28, x0 + len(bits) * w + 38, y0 - 1, fill=None) if False else None
    for k, ch in enumerate(CODE):
        if k == 0:
            xx = x0 - 22
        elif k <= 6:
            xx = x0 + (3 + (k - 1) * 7 + 3.5) * w
        else:
            xx = x0 + (3 + 42 + 5 + (k - 7) * 7 + 3.5) * w
        c.text(xx, y0 + h + 45, ch, 'mono', 30, (20, 20, 20), 'mm')
    sx = x0 + (t % 6) / 6 * len(bits) * w
    c.line([(sx, y0 - 20), (sx, y0 + h + 10)], RED, 4)
    k = min(6, int(t / 2.5))
    st = 3 + k * 7
    c.rect(x0 + st * w, y0 - 10, x0 + (st + 7) * w, y0 + h + 10, outline=SPARK, width=3)
    c.rect(1320, 260, 1860, 620, fill=SHEET, r=14)
    c.text(1590, 300, f'第 {k + 2} 位数字「{CODE[k + 1]}」', 'bold', 26, INK, 'mm')
    c.text(1590, 380, ' '.join(bits[st:st + 7]), 'mono', 34, SPARK, 'mm')
    c.text(1590, 460, '7 个小格，黑 1 白 0', 'sans', 20, MUTED, 'mm')
    c.text(1590, 540, '两边和中间的长条是「开始」「中间」「结束」记号', 'sans', 16, MUTED, 'mm')
    caps(c, t, [(0, 7, '条形码下面印着 13 位数字，黑白条纹就是这串数字的另一种写法'),
                (7.2, 14, '每个数字占 7 个小格：黑格算 1，白格算 0，粗的黑条就是几个连在一起的黑格'),
                (14.2, 22, '扫描器的红光扫过去，读出黑白的节奏，就还原出这串数字，再去电脑里查是什么商品（编码规则为 EAN-13）')], y=1010)


def e166_check(c, t, i):
    corner_tag(c, '第 166 集 · 最后一位，是用来查错的')
    c.text(60, 96, '前 12 位里，单数位直接加，双数位加起来乘 3，两者相加；再看还差几才到整十：差的数就是第 13 位', 'serif', 38, INK)
    code12 = CODE[:12]
    cd, so, se = check_digit(code12)
    x0 = 260
    for k, ch in enumerate(CODE):
        x = x0 + k * 110
        odd = k % 2 == 0
        col = SPARK if (k < 12 and odd) else (GREEN if k < 12 else NRED)
        c.rect(x, 280, x + 90, 380, fill=mix(BG, col, 0.25), outline=col, width=3, r=8)
        c.text(x + 45, 330, ch, 'mono', 44, INK, 'mm')
        c.text(x + 45, 410, f'{k + 1}', 'mono', 18, MUTED, 'mm')
    steps = [(2, f'单数位相加：{" + ".join(code12[0::2])} = {so}', SPARK),
             (6, f'双数位相加再乘 3：({" + ".join(code12[1::2])}) × 3 = {se * 3}', GREEN),
             (10, f'合计：{so} + {se * 3} = {so + 3 * se}', INK),
             (14, f'离下一个整十还差 {cd} → 第 13 位应该是 {cd}', NRED)]
    for k, (ts, txt, col) in enumerate(steps):
        a = fade(t, ts, ts + 1)
        if a > 0:
            c.text(300, 500 + k * 80, txt, 'mono', 30, mix(BG, col, a), 'lm')
    if t > 17:
        c.text(1500, 820, '对上了 ✓', 'bold', 36, GREEN, 'mm')
    caps(c, t, [(0, 7, '收银机读出 13 位数字后，不急着查价格，先用前 12 位算一遍'),
                (7.2, 14, '单数位直接加，双数位加起来乘 3，再看还差几才凑成整十'),
                (14.2, 22, '算出来和第 13 位一样，才算读对了；抄错或扫错一位，几乎都会对不上（示例条码为演示用）')], y=1010)


# ---------------------------------------------------------------- E167 公交卡
def e167_coupling(c, t, i):
    corner_tag(c, '第 167 集 · 读卡器的磁场，给卡「送电」')
    c.text(60, 96, '读卡器线圈周围是飞快变化的磁场；卡里绕着一圈天线，靠它感应出电，芯片才醒过来回话', 'serif', 36, INK)
    rx, ry = 640, 640
    c.rect(rx - 260, ry - 30, rx + 260, ry + 60, fill=(50, 50, 56), r=10)
    for k in range(4):
        c.ellipse(rx, ry, 220 - k * 30, 26 - k * 4, outline=COIL, width=3)
    c.text(rx, ry + 100, '读卡器（线圈）', 'sans', 22, MUTED, 'mm')
    cy = 360 + 120 * max(0, 1 - t / 6)
    ph = math.sin(t * 8)
    for k in range(5):
        h = 70 + k * 45
        a = 0.5 + 0.4 * ph
        c.arc(rx, ry, 120 + k * 40, h, 190, 350, mix(BG, (150, 200, 240), a * (1 - k * 0.15)), 2)
    c.rect(rx - 200, cy - 130, rx + 200, cy + 10, fill=mix(BG, CARD, 0.8), r=14)
    for k in range(3):
        c.rect(rx - 180 + k * 12, cy - 112 + k * 12, rx + 180 - k * 12, cy - 8 - k * 12, outline=COIL, width=2, r=10)
    near = cy < 420 and t > 6
    c.rect(rx + 110, cy - 90, rx + 160, cy - 50, fill=GREEN if near else mix(BG, METAL, 0.6), r=4)
    c.text(rx, cy - 160, '公交卡（里面的天线和芯片）', 'sans', 22, MUTED, 'mm')
    c.rect(1250, 300, 1840, 640, fill=SHEET, r=14)
    c.text(1545, 350, '卡里的芯片', 'bold', 26, INK, 'mm')
    c.text(1545, 440, '有电了 → 回话、扣钱' if near else '离得远，没电', 'bold', 30, GREEN if near else MUTED, 'mm')
    if near:
        c.text(1545, 540, '嘀！', 'bold', 40, SPARK, 'mm')
    caps(c, t, [(0, 7, '公交卡里没有电池：卡片中间夹着一圈绕了好几道的天线和一颗小芯片'),
                (7.2, 14, '读卡器的线圈通着每秒变化一千多万次的电流，周围的磁场跟着飞快变化'),
                (14.2, 22, '卡一靠近，天线里就感应出电，芯片醒过来，和读卡器「对话」扣钱：这和第 103 集的无线充电是同一个道理（示意）')], y=1010)


def e167_block(c, t, i):
    corner_tag(c, '第 167 集 · 离远一点、隔层铝箔，就刷不了')
    c.text(60, 96, '读卡器的磁场离开线圈就弱得很快：隔几本书还能刷，离开五六厘米就不行了；包一层铝箔，磁场在铝里被挡住', 'serif', 36, INK)
    cases = [('贴着', 0, False), ('隔 2 厘米书', 2, False), ('隔 5 厘米书', 5, False), ('包一层铝箔', 0, True)]
    k = min(3, int(t / 5.2))
    for j, (lab, d, foil) in enumerate(cases):
        x = 330 + j * 420
        c.rect(x - 150, 700, x + 150, 760, fill=(50, 50, 56), r=8)
        cy = 680 - d * 30
        if d:
            c.rect(x - 140, cy + 10, x + 140, 700, fill=mix(BG, (200, 180, 140), 0.6))
        c.rect(x - 120, cy - 60, x + 120, cy + 10, fill=mix(BG, CARD, 0.8), r=10)
        if foil:
            c.rect(x - 130, cy - 70, x + 130, cy + 20, fill=mix(BG, METAL, 0.85), r=10)
        ok = (d < 4) and not foil
        if j <= k:
            c.text(x, cy - 130, '嘀 ✓' if ok else '没反应', 'bold', 30, GREEN if ok else NRED, 'mm')
        c.text(x, 820, lab, 'bold', 24, INK, 'mm')
    c.text(960, 900, '能刷的距离各家读卡器不同，以实测为准', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '公交卡直接贴着读卡器：嘀一声就读到了'),
                (7.2, 14, '中间隔两厘米的书还行；隔到五厘米，磁场太弱，卡里感应不出足够的电'),
                (14.2, 22, '用铝箔包住，变化的磁场在铝里激起涡流被挡住了：所以卡放进带金属的卡套里会刷不出来（以实测为准）')], y=1010)


CLIPS = {
 'E165_感应': (e165_sense, 22), 'E165_遥控器': (e165_remote, 22),
 'E165_片头': (titles.opening(SER31, VOL31, S31A, 3, '1954 年自动感应门投入使用'), 7),
 'E165_片尾': (titles.closing(SER31, VOL31, S31A, 3, '下集：超市「嘀」一下就认出商品，黑白条里藏着什么？'), 7),
 'E166_条纹': (e166_bars, 22), 'E166_校验': (e166_check, 22),
 'E166_片头': (titles.opening(SER31, VOL31, S31A, 4, '1974 年第一次扫码结账'), 7),
 'E166_片尾': (titles.closing(SER31, VOL31, S31A, 4, '下集：公交卡没有电池，为什么一靠近就能刷？'), 7),
 'E167_感应': (e167_coupling, 22), 'E167_遮挡': (e167_block, 22),
 'E167_片头': (titles.opening(SER31, VOL31, S31A, 5, '1997 年香港八达通卡启用'), 7),
 'E167_片尾': (titles.closing(SER31, VOL31, S31A, 5, '下集：路灯没人按开关，为什么天一黑就自己亮了？'), 7),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
