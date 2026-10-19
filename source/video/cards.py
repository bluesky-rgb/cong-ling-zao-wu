from lib import *

def statement(tag, lines, sub=None, dur=4.0, accent=COPPER):
    def draw(c, t, i):
        corner_tag(c, tag)
        a = fade(t, 0.2, 0.9)
        y0 = 540 - (len(lines) - 1) * 60 - (30 if sub else 0)
        for k, ln in enumerate(lines):
            ak = fade(t, 0.2 + k * 0.35, 0.9 + k * 0.35)
            col = accent if k == len(lines) - 1 else INK
            c.text(960, y0 + k * 120 + (1 - ak) * 20, ln, 'serif', 84, mix(BG, col, ak), 'mm')
        if sub:
            c.text(960, y0 + len(lines) * 120 + 10, sub, 'sans', 34, mix(BG, MUTED, fade(t, 1.2, 1.8)), 'mm')
    return draw, dur

def question(tag, q, sub, dur=3.5):
    def draw(c, t, i):
        corner_tag(c, tag)
        a = fade(t, 0.15, 0.7)
        c.text(960, 470 + (1 - a) * 20, q, 'serif', 88, mix(BG, INK, a), 'mm')
        c.text(960, 610, sub, 'sans', 36, mix(BG, SPARK, fade(t, 0.9, 1.4)), 'mm')
        # pause indicator: two bars
        b = fade(t, 0.9, 1.4)
        c.rect(940, 700, 952, 740, fill=mix(BG, MUTED, b), r=3)
        c.rect(968, 700, 980, 740, fill=mix(BG, MUTED, b), r=3)
    return draw, dur

def formula(dur=12.0):
    parts = [('ε', '感应电压', 1.5), (' = ', None, None), ('−', '方向总是阻碍变化', 7.5),
             ('N', '线圈匝数', 3.0), (' · ', None, None), ('ΔΦ', '磁通量的变化', 4.5), (' / ', None, None), ('Δt', '用了多少时间', 6.0)]
    def draw(c, t, i):
        corner_tag(c, '镜头 12 · 法拉第电磁感应定律')
        a = fade(t, 0.1, 0.7)
        px = 120
        total = sum(c.textw(p, 'serif', 140) for p, _, _ in parts)
        x = 960 - total / 2
        y = 450
        active = None
        for p, lab, t0 in parts:
            w = c.textw(p, 'serif', 140)
            on = t0 is not None and t0 <= t < t0 + 1.5
            done = t0 is not None and t >= t0 + 1.5
            col = SPARK if on else (COPPER if done and t < 9.5 else INK)
            if t >= 9.5: col = INK
            c.text(x, y, p, 'serif', 140, mix(BG, col, a), 'lm')
            if lab and (on or (done and t < 9.5)):
                la = fade(t, t0, t0 + 0.4)
                c.text(x + w / 2, y + 120, lab, 'sans', 30, mix(BG, SPARK if on else MUTED, la), 'mm')
                c.line([(x + w / 2, y + 72), (x + w / 2, y + 96)], mix(BG, MUTED, la), 2)
            x += w
        fa = fade(t, 9.5, 10.2)
        c.text(960, 800, '电压 = 匝数 × 磁通量变化的快慢', 'bold', 52, mix(BG, COPPER, fa), 'mm')
    return draw, dur

SHOTS = [
    ('镜头03_核心字幕卡', statement('镜头 3', ['磁场不发电', '变化才发电'], '今天只讲这一句话')),
    ('镜头06_问题卡', question('镜头 6', '那反过来，磁能生电吗？', '先停一下，你觉得呢？')),
    ('镜头12_公式卡', formula()),
    ('镜头15_问题卡', question('镜头 15', '一直推拉太累了，怎么办？', '要持续发电，就得让磁通量一直变')),
    ('镜头20_结尾卡', statement('镜头 20', ['自己动手调参数', '链接在简介'], '从零造电 · 第 04 集', 5.0)),
]

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        name, t = sys.argv[1], float(sys.argv[2])
        for n, (d, _) in SHOTS:
            if n.startswith(name):
                c = Canvas(); d(c, t, 0); c.im.reduce(SS).save('/home/claude/video/prevcard.png')
    else:
        for n, (d, dur) in SHOTS:
            render(f'/home/claude/video/out/{n}.mp4', dur, d)
            print(n)
