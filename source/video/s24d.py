"""第二十四季收尾：B99 鲁班锁、第二十四季特辑（古法解密 9.0 回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps, BSER
from s6a import GREEN, seg
from s22a import rot
from s24a import SB24, VOL24, WOOD, DARKWOOD

LIGHTW = (210, 170, 110)
KEY = (230, 140, 70)


# ---------------------------------------------------------------- B99 鲁班锁
def _bar(c, x0, y0, x1, y1, col, notch=None):
    c.rect(x0, y0, x1, y1, fill=col, outline=DARKWOOD, width=3, r=4)
    if notch:
        nx0, ny0, nx1, ny1 = notch
        c.rect(nx0, ny0, nx1, ny1, fill=BG)


def b99_lock(c, t, i):
    corner_tag(c, 'B99 · 三根木条互相咬住')
    c.text(60, 96, '每根木条中间开一个缺口，让另一根穿过去；最后一根「钥匙」一插，谁也动不了', 'serif', 40, INK)
    cx, cy = 760, 580
    a1 = fade(t, 1, 4)
    a2 = fade(t, 5, 8)
    a3 = fade(t, 9, 13)
    pull = fade(t, 16, 19) if t < 19.5 else 1.0
    if a1 > 0:
        off = (1 - a1) * -500
        _bar(c, cx - 320 + off, cy - 40, cx + 320 + off, cy + 40, LIGHTW, (cx - 50 + off, cy - 40, cx + 50 + off, cy - 4))
        c.text(cx - 340 + off, cy, '①', 'bold', 28, INK, 'rm')
    if a2 > 0:
        off = (1 - a2) * -400
        _bar(c, cx - 40, cy - 320 + off, cx + 40, cy + 320 + off, WOOD, (cx - 40, cy - 50 + off, cx - 4, cy + 50 + off))
        c.text(cx, cy - 340 + off, '②', 'bold', 28, INK, 'mm')
    if a3 > 0:
        r = 46 * (0.4 + 0.6 * a3)
        dx, dy = pull * 260, pull * 260
        sz = 22 * (1 + 0.6 * pull)
        c.rect(cx - sz + dx, cy - sz + dy, cx + sz + dx, cy + sz + dy, fill=KEY, outline=DARKWOOD, width=3, r=4)
        c.text(cx + 60 + dx, cy - 60 + dy, '③ 钥匙（从正面插进去）' if pull == 0 else '③ 钥匙被抽出来了', 'bold', 24, KEY, 'lm')
    if a3 >= 1 and t < 16:
        for k in range(2):
            c.arrow(cx + 340, cy - 100 + k * 200, cx + 420, cy - 100 + k * 200, NRED, 3, 12)
        c.text(cx + 440, cy, '拉不动', 'bold', 26, NRED, 'lm')
    if t > 16:
        c.text(1500, 860, '先抽出钥匙，另两根才能分开', 'bold', 26, GREEN, 'mm')
    c.rect(1380, 260, 1860, 560, fill=SHEET, r=14)
    c.text(1620, 300, '三根最简单的锁（示意）', 'bold', 24, INK, 'mm')
    c.text(1420, 370, '① 横着放，缺口朝上', 'sans', 22, INK, 'lm')
    c.text(1420, 420, '② 竖着穿过①的缺口', 'sans', 22, INK, 'lm')
    c.text(1420, 470, '③ 前后插进两个缺口剩下的洞', 'sans', 22, INK, 'lm')
    c.text(1420, 520, '三个方向，互相挡死', 'sans', 22, SPARK, 'lm')
    caps(c, t, [(0, 7, '最简单的鲁班锁只有三根木条，分别朝左右、上下、前后三个方向'),
                (7.2, 14, '前两根靠缺口交叉卡在一起，中间留下一个小洞；第三根从正面插进去，正好把洞堵上'),
                (14.2, 22, '三根互相挡住退路，谁也拉不出来；只有先抽出最后插进的那根「钥匙」，才能拆开')], y=1010)


def b99_order(c, t, i):
    corner_tag(c, 'B99 · 只有一根能先动')
    c.text(60, 96, '六根的鲁班锁：箭头表示「被谁挡着」；没有箭头指着的那根，才能先抽出来', 'serif', 40, INK)
    names = ['钥匙', '甲', '乙', '丙', '丁', '戊']
    blocks = {'甲': ['钥匙'], '乙': ['钥匙', '甲'], '丙': ['甲'], '丁': ['乙', '丙'], '戊': ['丁']}
    pos = {}
    cx, cy, R = 720, 580, 300
    for k, n in enumerate(names):
        a = -math.pi / 2 + k * 2 * math.pi / 6
        pos[n] = (cx + R * math.cos(a), cy + R * math.sin(a))
    order = ['钥匙', '甲', '乙', '丙', '丁', '戊']
    removed = set(order[:max(0, min(6, int((t - 4) / 2.6)))]) if t > 4 else set()
    for n, bl in blocks.items():
        for b in bl:
            if n in removed or b in removed:
                continue
            x0, y0 = pos[b]; x1, y1 = pos[n]
            L = math.hypot(x1 - x0, y1 - y0)
            ux, uy = (x1 - x0) / L, (y1 - y0) / L
            c.arrow(x0 + ux * 60, y0 + uy * 60, x1 - ux * 60, y1 - uy * 60, mix(BG, NRED, 0.8), 3, 14)
    for n in names:
        x, y = pos[n]
        free = n not in removed and all(b in removed for b in blocks.get(n, []))
        col = (60, 60, 65) if n in removed else (GREEN if free else (KEY if n == '钥匙' else LIGHTW))
        c.ellipse(x, y, 52, 52, fill=col, outline=DARKWOOD, width=3)
        c.text(x, y, n, 'bold', 26, INK if n not in removed else MUTED, 'mm')
    c.rect(1300, 300, 1860, 700, fill=SHEET, r=14)
    c.text(1580, 340, '拆的顺序', 'bold', 26, INK, 'mm')
    c.text(1580, 420, ' → '.join(order[:len(removed)]) or '（还没开始）', 'sans', 24, SPARK, 'mm')
    c.text(1580, 520, '绿色：现在能抽出来的', 'sans', 22, GREEN, 'mm')
    c.text(1580, 570, '拼回去：倒过来的顺序', 'sans', 22, INK, 'mm')
    c.text(1580, 640, '（关系为示意，各种鲁班锁不同）', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '鲁班锁的每根木条，都被另外几根挡着：一开始，只有「钥匙」那一根没被挡住'),
                (7.2, 14, '抽出钥匙，原来被它挡住的那几根就松了一根；再抽、再松，像解一串连环'),
                (14.2, 22, '拼回去时把顺序倒过来，最后插上钥匙，又锁得死死的：不用钉子胶水，靠的是顺序')], y=1010)


# ---------------------------------------------------------------- 第二十四季特辑
OLD24 = [('杠杆与滑轮组', '39'), ('杆秤', 'B43'), ('水车提水', '28'), ('齿轮与轴承', '41'), ('选种与嫁接', '30'), ('豆腐点卤', 'B14'),
         ('不倒翁', 'B51'), ('自行车', '66'), ('竹编', 'B73'), ('灵渠陡门', 'B26'), ('勾股', 'B62'), ('记里鼓车', 'B25'),
         ('漏刻', 'B13'), ('摆钟', '45'), ('日晷', 'B63'), ('用影子测地球', '47'), ('纸', '23'), ('七巧板', 'B60'),
         ('榫卯', 'B7'), ('九连环', 'B55')]
NEW24 = [('桔槔', 'B90', ['杠杆与滑轮组', '杆秤']), ('龙骨水车', 'B91', ['水车提水', '齿轮与轴承']), ('发豆芽', 'B92', ['选种与嫁接', '豆腐点卤']),
         ('独轮车', 'B93', ['不倒翁', '自行车']), ('鱼笱', 'B94', ['竹编', '灵渠陡门']), ('计里画方', 'B95', ['勾股', '记里鼓车']),
         ('沙漏', 'B96', ['漏刻', '摆钟']), ('浑仪', 'B97', ['日晷', '用影子测地球']), ('剪纸', 'B98', ['纸', '七巧板']),
         ('鲁班锁', 'B99', ['榫卯', '九连环'])]

def s24_graph(c, t, i):
    corner_tag(c, '第二十四季特辑 · 古法解密 9.0')
    c.text(60, 118, '田、路、天、巧：十件老东西接在哪里', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD24):
        pos[name] = (340, 196 + k * 40)
    for k, (name, num, deps) in enumerate(NEW24):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '已点亮的节点', 'sans', 24, MUTED, 'mm')
    c.text(1285, 172, '第二十四季新长出', 'sans', 24, MUTED, 'mm')
    newset = set(n for n, _, _ in NEW24)
    for k, (name, num, deps) in enumerate(NEW24):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            if d in newset:
                pts = [(x0 + 110 if x0 < x1 else x0 - 110, y0), (x1 - 110 if x0 < x1 else x1 + 110, y1)]
                c.line(pts, mix(BG, COPPER, a * 0.9), 3)
                continue
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD24:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=9)
        c.text(x - 96, y, num, 'mono', 17, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW24):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 96, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 24, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '古法解密第九季：田、路、天、巧'),
                (8.2, 16, '桔槔和龙骨水车把水送上田，豆芽在暗处长；独轮车、鱼笱、计里画方走在路上'),
                (16.2, 24, '沙漏数着时间，浑仪量着星星：用的是颗粒、角度和纬度'),
                (24.2, 30, '剪纸折出对称，鲁班锁用顺序锁住木条：手上的巧，都是讲得清的道理')], y=1040)

CLIPS = {
 'B99_互锁': (b99_lock, 22), 'B99_顺序': (b99_order, 22),
 'B99_片头': (titles.opening(BSER, VOL24, SB24, 9, '民间传说鲁班 · 清代孔明锁'), 7),
 'B99_片尾': (titles.closing(BSER, VOL24, SB24, 9, '下集：第二十四季特辑 · 古法解密 9.0 回顾'), 7),
 'S24_依赖': (s24_graph, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
