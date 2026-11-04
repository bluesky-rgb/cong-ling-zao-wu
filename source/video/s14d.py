"""第十四季收尾：B49 含嘉仓、第十四季特辑（古法解密 4.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s14a import SB14, VOL14

EARTH = (120, 90, 60)
BURNT = (70, 50, 40)
ASH = (170, 170, 165)
MAT = (190, 160, 100)
GRAIN = (220, 190, 110)
WATERC = (90, 150, 210)

# ---------------------------------------------------------------- B49 含嘉仓
def b49_layers(c, t, i):
    corner_tag(c, 'B49 · 一口粮窖的剖面')
    c.text(60, 96, '口大底小的地窖：一层一层把潮气挡在外面', 'serif', 40, INK)
    c.rect(0, 260, 1920, 980, fill=EARTH)
    c.rect(0, 250, 1920, 262, fill=(90, 130, 70))
    top_w, bot_w, y0, y1 = 520, 360, 262, 900
    cx = 760
    def trap(dw, a_, b_, col):
        c.poly([(cx - top_w + dw, y0 + a_), (cx + top_w - dw, y0 + a_), (cx + bot_w - dw, y1 - b_), (cx - bot_w + dw, y1 - b_)], col)
    layers = [(0, 0, BURNT, '窖壁和窖底用火烤硬（拍摄前核对）', 1),
              (24, 24, ASH, '铺草木灰：吸潮', 4),
              (44, 44, MAT, '再铺木板、草席、糠', 7),
              (64, 64, GRAIN, '粮食', 10)]
    for k, (dw, d, col, note, t0) in enumerate(layers):
        a = fade(t, t0, t0 + 1)
        if a <= 0: continue
        trap(dw, d * 0 + (60 if k == 3 else 0), d, mix(EARTH, col, a))
        c.text(1440, 330 + k * 110, note, 'bold' if k < 3 else 'sans', 26, mix(BG, INK, a), 'lm')
        c.line([(1430, 330 + k * 110), (cx + top_w - dw - 30, 330 + k * 110 + 40)], mix(BG, MUTED, a * 0.6), 2)
    b = fade(t, 13, 14)
    c.rect(cx - top_w - 20, y0 - 20, cx + top_w + 20, y0 + 40, fill=mix(EARTH, (110, 80, 50), b))
    c.text(cx, y0 - 50, '顶上封土密封', 'bold', 26, mix(BG, INK, b), 'mm')
    d = fade(t, 15, 16)
    for k in range(6):
        left = k % 2 == 0
        x = cx - 680 if left else cx + 600
        y = 420 + (k // 2) * 160
        dx = 1 if left else -1
        c.arrow(x, y, x + dx * 70, y, mix(BG, WATERC, d), 4, 14)
        mx = x + dx * 95
        c.line([(mx - 12, y - 12), (mx + 12, y + 12)], mix(BG, NRED, d), 5)
        c.line([(mx - 12, y + 12), (mx + 12, y - 12)], mix(BG, NRED, d), 5)
    caps(c, t, [(0, 6, '隋代洛阳的含嘉仓，是几百口挖在地下的粮窖'),
                (6.2, 13, '窖壁烤硬，铺草木灰、木板和草席，一层层隔开地下的潮气'),
                (13.2, 22, '装满后顶上封土：地下温度稳，潮气和空气都进不来（各层做法拍摄前核对）')], y=1010)

def b49_breath(c, t, i):
    corner_tag(c, 'B49 · 粮食也在「呼吸」')
    c.text(60, 96, '封起来：氧气越用越少，虫和霉就难活', 'serif', 40, INK)
    x0, y0, W, H = 220, 820, 1000, 520
    c.line([(x0, y0), (x0 + W, y0)], LINE, 3)
    c.line([(x0, y0), (x0, y0 - H)], LINE, 3)
    c.text(x0 + W / 2, y0 + 50, '封窖以后的时间 →', 'sans', 24, MUTED, 'mm')
    prog = fade(t, 1, 10)
    o2, co2 = [], []
    for k in range(int(50 * prog) + 1):
        u = k / 50
        o2.append((x0 + u * W, y0 - H * (0.9 - 0.75 * (1 - math.exp(-u * 3)))))
        co2.append((x0 + u * W, y0 - H * (0.05 + 0.7 * (1 - math.exp(-u * 3)))))
    if len(o2) > 1:
        c.line(o2, WATERC, 5)
        c.line(co2, SPARK, 5)
    a = fade(t, 2, 3)
    c.text(x0 + W + 20, y0 - H * 0.9, '氧气', 'bold', 26, mix(BG, WATERC, a), 'lm')
    c.text(x0 + W + 20, y0 - H * 0.75, '二氧化碳', 'bold', 26, mix(BG, SPARK, a), 'lm')
    c.text(x0 + 20, y0 - H - 20, '示意，不是实测数据', 'sans', 22, MUTED, 'lm')
    b = fade(t, 11, 12)
    c.rect(1420, 300, 1860, 760, fill=mix(BG, SHEET, b), r=12)
    rows = ['粮食和虫、霉都要呼吸：', '吸氧气，放出二氧化碳、水和热', '', '封住以后氧气用完：', '虫闷死，霉长不动', '', '地下又凉又稳：', '呼吸更慢，粮食更耐放']
    for k, s_ in enumerate(rows):
        c.text(1450, 340 + k * 50, s_, 'bold' if s_.endswith('：') else 'sans', 24, mix(BG, INK, b), 'lm')
    caps(c, t, [(0, 6, '粮食是活的种子：放着的时候，也在慢慢呼吸'),
                (6.2, 13, '封住的窖里，氧气越用越少，二氧化碳越来越多'),
                (13.2, 22, '虫和霉菌都缺氧、缺水，就长不起来：干、凉、少氧，是藏粮的三个字')], y=1010)

# ---------------------------------------------------------------- 第十四季特辑
OLD14 = [('走马灯', 'B23'), ('一钟双音', 'B11'), ('鱼洗', 'B9'), ('杠杆与滑轮组', '39'), ('欹器', 'B21'), ('水密隔舱', 'B24'),
         ('素纱襌衣', 'B33'), ('石灰与水泥', '24'), ('钢筋混凝土', '63'), ('榫卯', 'B7'), ('赵州桥', 'B6'), ('豆腐点卤', 'B14'), ('冰鉴', 'B12')]
NEW14 = [('竹蜻蜓', 'B40', ['走马灯']), ('风筝', 'B41', ['竹蜻蜓']), ('陶埙', 'B42', ['一钟双音', '鱼洗']), ('杆秤', 'B43', ['杠杆与滑轮组', '欹器']),
         ('船尾舵', 'B44', ['水密隔舱', '竹蜻蜓']), ('扎染', 'B45', ['素纱襌衣']), ('夯土版筑', 'B46', ['石灰与水泥', '钢筋混凝土']),
         ('斗拱', 'B47', ['榫卯', '赵州桥']), ('腌菜', 'B48', ['豆腐点卤']), ('含嘉仓', 'B49', ['冰鉴', '腌菜'])]

def s14_graph(c, t, i):
    corner_tag(c, '第十四季特辑 · 古法解密 4.0')
    c.text(60, 118, '飞、响、量、造、藏：十个老物件接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD14):
        pos[name] = (340, 212 + k * 58)
    for k, (name, num, deps) in enumerate(NEW14):
        pos[name] = (1180 + (210 if name in ('风筝', '船尾舵', '含嘉仓') else 0), 215 + k * 76)
    c.text(340, 165, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1280, 165, '第十四季新长出', 'sans', 24, MUTED, 'mm')
    names_new = set(n for n, _, _ in NEW14)
    for k, (name, num, deps) in enumerate(NEW14):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx = x0 + 110
            ex = x1 - 110
            col = mix(BG, COPPER if d in names_new else FIELD, a * 0.8)
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, col, 2)
    for name, num in OLD14:
        x, y = pos[name]
        c.rect(x - 110, y - 22, x + 110, y + 22, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 20, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW14):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第四季：全是身边摸得到的老物件'),
                (8.2, 16, '竹蜻蜓长出风筝和船尾舵：都是一块斜板在推空气或推水'),
                (16.2, 24, '杆秤接杠杆，斗拱接榫卯，夯土接石灰和混凝土，含嘉仓接冰鉴和腌菜'),
                (24.2, 30, '老物件不老：每一件里都藏着一条物理定律')], y=1040)

CLIPS = {
 'B49_隔潮': (b49_layers, 22), 'B49_呼吸': (b49_breath, 22),
 'B49_片头': (titles.opening(BSER, VOL14, SB14, 9, '隋 · 605 年 · 洛阳含嘉仓'), 7),
 'B49_片尾': (titles.closing(BSER, VOL14, SB14, 9, '下集：第十四季特辑 · 古法解密 4.0 回顾'), 7),
 'S14_依赖': (s14_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
