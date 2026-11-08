"""第三十一季（第十二层：城市里的机器）收官：E171 地图导航 + 第三十一季特辑 —— 动画与片头片尾。"""
import math, random, sys, heapq
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s31a import S31A, SER31, VOL31

NODES = {'A': (300, 560), 'B': (560, 330), 'C': (580, 780), 'D': (860, 520), 'E': (1080, 300),
         'F': (1100, 800), 'G': (1360, 540), 'H': (1620, 560)}
EDGES = [('A', 'B', 4), ('A', 'C', 3), ('B', 'D', 3), ('C', 'D', 5), ('B', 'E', 6), ('D', 'E', 2),
         ('D', 'F', 4), ('C', 'F', 7), ('E', 'G', 4), ('F', 'G', 2), ('G', 'H', 3), ('E', 'H', 8)]


def dijkstra_trace():
    adj = {k: [] for k in NODES}
    for a, b, w in EDGES:
        adj[a].append((b, w)); adj[b].append((a, w))
    dist = {k: math.inf for k in NODES}
    prev = {}
    dist['A'] = 0
    done = []
    pq = [(0, 'A')]
    snaps = []
    while pq:
        d, u = heapq.heappop(pq)
        if u in done:
            continue
        done.append(u)
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w; prev[v] = u
                heapq.heappush(pq, (dist[v], v))
        snaps.append((list(done), dict(dist), dict(prev)))
        if u == 'H':
            break
    return snaps


SNAPS = dijkstra_trace()


def _path(prev, end='H'):
    p = [end]
    while p[-1] in prev:
        p.append(prev[p[-1]])
    return p[::-1]


def _graph(c, done, dist, hi=None, weights=None):
    hi = hi or []
    hs = set(zip(hi, hi[1:])) | set(zip(hi[1:], hi))
    for a, b, w in EDGES:
        (x0, y0), (x1, y1) = NODES[a], NODES[b]
        on = (a, b) in hs
        c.line([(x0, y0), (x1, y1)], GREEN if on else mix(BG, LINE, 0.8), 8 if on else 4)
        lab = weights[(a, b)] if weights else w
        c.text((x0 + x1) / 2, (y0 + y1) / 2 - 18, str(lab), 'mono', 22, SPARK, 'mm')
    for k, (x, y) in NODES.items():
        d = dist.get(k, math.inf)
        fill = mix(BG, GREEN, 0.5) if k in done else SHEET
        c.ellipse(x, y, 38, 38, fill=fill, outline=INK, width=2)
        c.text(x, y, k, 'bold', 26, INK, 'mm')
        c.text(x, y + 60, '∞' if d == math.inf else f'{d}', 'mono', 22, INK if d != math.inf else MUTED, 'mm')


# ---------------------------------------------------------------- E171 地图导航
def e171_dijkstra(c, t, i):
    corner_tag(c, '第 171 集 · 从起点一圈圈往外确定')
    c.text(60, 96, '从 A 出发：每次把还没确定、离 A 最近的路口定下来，再用它更新邻居的距离，直到终点 H 被定下', 'serif', 38, INK)
    k = min(len(SNAPS) - 1, int(t / 2.4))
    done, dist, prev = SNAPS[k]
    hi = _path(prev) if 'H' in done else []
    _graph(c, done, dist, hi)
    c.rect(1700, 240, 1880, 420, fill=SHEET, r=12)
    c.text(1790, 280, '已确定', 'bold', 22, INK, 'mm')
    c.text(1790, 340, ' '.join(done), 'mono', 22, GREEN, 'mm')
    if hi:
        c.text(960, 940, f'最短路线：{" → ".join(hi)}，总长 {dist["H"]}', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 7, '8 个路口、12 条路，每条路上写着长度；A 记 0，其他先记「无穷远」'),
                (7.2, 14, '每次挑一个离 A 最近、还没确定的路口定下来，再看经过它能不能让邻居更近'),
                (14.2, 22, '像水波一样一圈圈往外推，终点一被确定，最短路线就出来了：不用把每条路都试一遍')], y=1010)


def e171_fast(c, t, i):
    corner_tag(c, '第 171 集 · 最短的路，不一定最快')
    c.text(60, 96, '把每条路的「长度」换成「要开几分钟」：堵车的路分钟数变大，同样的算法就会绕开它，找出最快的一条', 'serif', 38, INK)
    jam = min(1, max(0, (t - 6) / 4))
    weights = {}
    for a, b, w in EDGES:
        ww = w
        if (a, b) in (('D', 'F'), ('F', 'G')):
            ww = round(w + 6 * jam)
        weights[(a, b)] = ww
    adj = {k: [] for k in NODES}
    for (a, b), w in weights.items():
        adj[a].append((b, w)); adj[b].append((a, w))
    dist = {k: math.inf for k in NODES}
    prev = {}
    dist['A'] = 0
    pq = [(0, 'A')]
    seen = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in seen:
            continue
        seen.add(u)
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w; prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    hi = _path(prev)
    _graph(c, list(NODES), dist, hi, weights)
    if jam > 0:
        for (a, b) in (('D', 'F'), ('F', 'G')):
            (x0, y0), (x1, y1) = NODES[a], NODES[b]
            c.text((x0 + x1) / 2 + 40, (y0 + y1) / 2 + 20, '堵车', 'bold', 22, mix(BG, NRED, jam), 'mm')
    c.text(960, 940, f'现在最快：{" → ".join(hi)}，约 {dist["H"]} 分钟', 'bold', 30, GREEN, 'mm')
    caps(c, t, [(0, 7, '导航真正算的往往是时间：每条路写上「开过去要几分钟」'),
                (7.2, 14, '一条路堵车了，它的分钟数变大；同样的算法再跑一遍'),
                (14.2, 22, '最快的路线就绕开了堵车的那段：手机每隔一会儿用最新路况重算一次（示意）')], y=1010)


# ---------------------------------------------------------------- 第三十一季特辑
OLD31 = [('开关与逻辑门', '81'), ('电灯', '60'), ('水车提水', '28'), ('净水', '34'), ('变压器与交流电', '75'), ('电动机', '58'),
         ('回声测距与雷达', '84'), ('数字与 0', '48'), ('激光', '94'), ('无线充电', '103'), ('磁生电', '04'), ('太阳能电池', '77'),
         ('电子秤', '160'), ('电磁铁', '56'), ('抽水马桶与存水弯', '69'), ('石灰与水泥', '24'), ('卫星定位', '90'), ('程序与计算机', '91')]
NEW31 = [('红绿灯', '162', ['开关与逻辑门', '电灯']), ('水塔', '163', ['水车提水', '净水']), ('电表', '164', ['变压器与交流电', '电动机']),
         ('自动门', '165', ['回声测距与雷达', '电动机']), ('条形码', '166', ['数字与 0', '激光']), ('公交卡', '167', ['无线充电', '磁生电']),
         ('光控路灯', '168', ['太阳能电池', '开关与逻辑门']), ('自动售货机', '169', ['电子秤', '电磁铁']), ('下水道', '170', ['抽水马桶与存水弯', '石灰与水泥']),
         ('地图导航', '171', ['卫星定位', '程序与计算机'])]


def s31_layer(c, t, i):
    corner_tag(c, '第三十一季特辑 · 第十二层')
    c.text(60, 118, '第十二层：城市里的机器', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD31):
        pos[name] = (340, 196 + k * 44)
    for k, (name, num, deps) in enumerate(NEW31):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第三十一季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW31):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD31:
        x, y = pos[name]
        c.rect(x - 110, y - 18, x + 110, y + 18, fill=SHEET, outline=COPPER, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 16, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 19 if len(name) < 7 else 16, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW31):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22 if len(name) < 5 else 20, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第十二层的十集：走出家门，城市里的机器'),
                (8.2, 16, '开关和电灯长出红绿灯，水车和净水长出水塔，交流电长出电表，雷达长出自动门'),
                (16.2, 24, '数字和激光长出条形码，磁生电长出公交卡，电子秤长出售货机，存水弯长出下水道'),
                (24.2, 30, '最后，卫星定位和计算机一起，长出了一瞬间找到最快路线的地图导航')], y=1040)


CLIPS = {
 'E171_最短路': (e171_dijkstra, 22), 'E171_最快': (e171_fast, 22),
 'E171_片头': (titles.opening(SER31, VOL31, S31A, 9, '1959 年提出最短路径算法'), 7),
 'E171_片尾': (titles.closing(SER31, VOL31, S31A, 9, '下集：第三十一季特辑 · 第十二层回顾'), 7),
 'S31_第十二层': (s31_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
