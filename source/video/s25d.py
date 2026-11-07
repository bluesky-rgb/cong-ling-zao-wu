"""第二十五季收尾：E141 微创手术、第二十五季特辑（第九层回顾） —— 动画与片头片尾。"""
import math, random, sys
from lib import *
import titles
from s1b import caps
from s6a import GREEN, seg
from s25a import S25A, SER25, VOL25, SKINC, SOUND

BELLY = (225, 175, 150)
TOOL = (190, 195, 205)
BEAN = (210, 180, 90)


# ---------------------------------------------------------------- E141 微创手术
def e141_ports(c, t, i):
    corner_tag(c, '第 141 集 · 三个小孔，一根镜头（动画演示）')
    c.text(60, 96, '不用切开一大道口子：肚子上开几个小孔，一个伸进镜头，另两个伸进细长的器械，医生看着屏幕做', 'serif', 36, INK)
    cx, base = 620, 860
    inflate = min(1, max(0, t / 6))
    h = 230 + 120 * inflate
    pts = [(cx - 420 + 840 * j / 60, base - h * math.sin(math.pi * j / 60)) for j in range(61)]
    c.poly(pts + [(cx + 420, base)], mix(BG, BELLY, 0.35))
    c.line(pts, BELLY, 5)
    c.line([(cx - 440, base), (cx + 440, base)], LINE, 2)
    c.text(cx, base + 34, '腹腔（示意剖面）：先充一点气，把肚皮撑起来留出空间', 'sans', 20, MUTED, 'mm')
    ports = [(-0.62, '器械'), (0.0, '镜头'), (0.62, '器械')]
    target = (cx + 40, base - 60)
    c.ellipse(target[0], target[1], 46, 30, fill=(180, 90, 100))
    for k, (u, nm) in enumerate(ports):
        j = int(30 + u * 30)
        px, py = pts[j]
        wob = 18 * math.sin(t * 1.6 + k * 2) if nm == '器械' else 0
        tx, ty = target[0] + (-60 if u < 0 else 60 if u > 0 else 0) + wob, target[1] - (20 if nm == '器械' else 140)
        out = 1.0 + 0.9
        ox, oy = px + (px - tx) * 0.9, py + (py - ty) * 0.9
        c.line([(ox, oy), (tx, ty)], TOOL if nm == '器械' else (120, 160, 220), 8)
        c.rect(px - 16, py - 8, px + 16, py + 8, fill=(90, 90, 100), r=4)
        c.text(ox, oy - 26, nm, 'bold', 22, INK, 'mm')
        if nm == '镜头':
            c.ellipse(tx, ty, 10, 10, fill=SPARK)
            for a in (-0.5, 0.5):
                c.line([(tx, ty), (tx + 160 * math.sin(a), ty + 160 * math.cos(a))], mix(BG, SPARK, 0.35), 2)
    c.rect(1180, 260, 1860, 760, fill=SHEET, r=14)
    c.text(1520, 296, '屏幕上看到的', 'bold', 24, INK, 'mm')
    c.rect(1220, 330, 1820, 700, fill=(40, 30, 34), r=8)
    c.ellipse(1520 + 10 * math.sin(t * 0.3), 560, 150, 90, fill=(180, 90, 100))
    for k, s in enumerate((-1, 1)):
        wob = 18 * math.sin(t * 1.6 + (0 if s < 0 else 2) * 2)
        x = 1520 + s * 170 + wob * 1.8
        c.line([(1520 + s * 330, 360), (x, 520)], TOOL, 10)
    c.text(1520, 730, '镜头把里面放大了，器械尖在屏幕上很显眼', 'sans', 20, MUTED, 'mm')
    caps(c, t, [(0, 7, '传统手术要切开一道长长的口子，才能伸手进去；微创手术只在肚子上开几个一厘米左右的小孔（拍摄前核对）'),
                (7.2, 14, '先充进一点气体把肚皮撑起来，再从一个孔伸进带灯的小镜头，画面实时显示在屏幕上'),
                (14.2, 22, '另外两个孔伸进细长的器械：医生不看自己的手，而是盯着屏幕做手术，伤口小、恢复快（示意）')], y=1010)


def e141_fulcrum(c, t, i):
    corner_tag(c, '第 141 集 · 手往下，尖往上')
    c.text(60, 96, '长器械穿过小孔，小孔就是支点：手往下压，器械尖往上翘；手动一点，尖动多少，看支点在哪儿', 'serif', 36, INK)
    for row, (ratio, label) in enumerate(((1.0, '支点在中间：手动多少，尖就反着动多少'), (0.4, '支点靠近尖：手动很多，尖只动一点，更精细'))):
        cy = 360 + row * 340
        fx = 900
        c.rect(150, cy - 150, 1750, cy + 130, fill=SHEET, r=14)
        c.text(180, cy - 120, label, 'bold', 24, INK, 'lm')
        c.line([(fx - 300, cy), (fx + 300, cy)], mix(BG, BELLY, 0.8), 10)
        c.text(fx + 320, cy + 34, '肚皮上的小孔＝支点', 'sans', 18, MUTED, 'lm')
        c.ellipse(fx, cy, 12, 12, fill=(90, 90, 100))
        hand = 120 * math.sin(t * 0.9)
        Lh, Lt = 500, 500 * ratio
        ang = math.atan2(hand, Lh)
        hx, hy = fx - Lh * math.cos(ang), cy - 60 - Lh * 0
        hx = fx - Lh
        hy = cy + hand * 0.8
        tx = fx + Lt
        ty = cy - hand * 0.8 * ratio
        c.line([(hx, hy), (tx, ty)], TOOL, 8)
        c.ellipse(hx, hy, 26, 26, fill=SKINC)
        c.text(hx, hy - 44 if hy < cy else hy + 44, '手', 'bold', 22, INK, 'mm')
        c.ellipse(tx, ty, 10, 10, fill=SPARK)
        c.text(tx + 30, ty, '尖', 'bold', 22, SPARK, 'lm')
        c.arrow(hx - 70, cy, hx - 70, cy + (40 if hand > 0 else -40), mix(BG, INK, 0.6), 3, 10)
        c.arrow(tx + 90, cy, tx + 90, cy - (40 if hand > 0 else -40) * ratio, SPARK, 3, 10)
    caps(c, t, [(0, 7, '器械从小孔伸进去，小孔把它卡住了：整根器械只能绕着这个点转，像一根跷跷板'),
                (7.2, 14, '所以手往下压，器械尖往上翘；手往左，尖往右：医生要专门练习这种「反着来」'),
                (14.2, 22, '小孔离尖越近，手动一大下，尖只动一小下，动作就更精细：这就是第 40 集里杠杆的老道理（示意）')], y=1010)


# ---------------------------------------------------------------- 第二十五季特辑
OLD25 = [('留声机', '73'), ('回音壁', 'B66'), ('虹吸', '26'), ('温度计', '46'), ('透镜', '52'), ('照相', '55'),
         ('无线电', '76'), ('回声测距与雷达', '84'), ('压电', '13'), ('电话', '72'), ('降噪耳机', '106'), ('蓄电池', '61'),
         ('摆钟', '45'), ('电磁铁', '56'), ('陀螺仪', '108'), ('显微镜', '53'), ('程序与计算机', '91'), ('光纤', '89'),
         ('曲柄连杆', '40')]
NEW25 = [('听诊器', '132', ['留声机', '回音壁']), ('血压计', '133', ['虹吸', '温度计']), ('近视眼镜', '134', ['透镜', '照相']),
         ('X 光', '135', ['照相', '无线电']), ('超声检查', '136', ['回声测距与雷达', '压电']), ('人工耳蜗', '137', ['电话', '降噪耳机']),
         ('心脏起搏器', '138', ['蓄电池', '摆钟']), ('核磁共振', '139', ['电磁铁', '陀螺仪']), ('DNA', '140', ['显微镜', '程序与计算机']),
         ('微创手术', '141', ['光纤', '曲柄连杆'])]


def s25_layer(c, t, i):
    corner_tag(c, '第二十五季特辑 · 第九层')
    c.text(60, 118, '第九层：看见身体', 'serif', 40, INK, 'lm')
    pos = {}
    for k, (name, num) in enumerate(OLD25):
        pos[name] = (340, 200 + k * 42)
    for k, (name, num, deps) in enumerate(NEW25):
        pos[name] = (1180 + (210 if k % 2 else 0), 215 + k * 76)
    c.text(340, 160, '前几季已点亮', 'sans', 24, MUTED, 'mm')
    c.text(1285, 168, '第二十五季新长出', 'sans', 24, MUTED, 'mm')
    for k, (name, num, deps) in enumerate(NEW25):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        if a <= 0: continue
        x1, y1 = pos[name]
        for d in deps:
            x0, y0 = pos[d]
            sx, ex = x0 + 110, x1 - 110
            pts = [(sx + (ex - sx) * j / 20, y0 + (y1 - y0) * (3 * (j / 20) ** 2 - 2 * (j / 20) ** 3)) for j in range(21)]
            seg(c, pts, mix(BG, FIELD, a * 0.8), 2)
    for name, num in OLD25:
        x, y = pos[name]
        c.rect(x - 110, y - 17, x + 110, y + 17, fill=SHEET, outline=COPPER if num[0].isdigit() else FIELD, width=2, r=8)
        c.text(x - 98, y, num, 'mono', 15, MUTED, 'lm')
        c.text(x + 18, y, name, 'sans', 18, INK, 'mm')
    for k, (name, num, deps) in enumerate(NEW25):
        a = fade(t, 2 + k * 2.2, 3 + k * 2.2)
        x, y = pos[name]
        c.rect(x - 110, y - 26, x + 110, y + 26, fill=mix(BG, mix(SHEET, SPARK, 0.35), a), outline=mix(LINE, SPARK, a), width=2, r=10)
        c.text(x - 98, y, num, 'mono', 18, mix(BG, MUTED, a), 'lm')
        c.text(x + 18, y, name, 'bold', 22, mix(MUTED, INK, a), 'mm')
    caps(c, t, [(0, 8, '第九层的十集：不开刀，也能听见、量出、看见身体里面'),
                (8.2, 16, '留声机和回音壁长出听诊器，虹吸长出血压计，透镜长出眼镜，无线电的亲戚 X 射线照见了骨头'),
                (16.2, 24, '回声和压电长出 B 超，电话长出人工耳蜗，摆钟和电池长出起搏器，陀螺的摆头长出核磁共振'),
                (24.2, 30, '显微镜看见细胞，DNA 写着细胞的程序；光纤和杠杆，让手术只需要几个小孔')], y=1040)


CLIPS = {
 'E141_小孔': (e141_ports, 22), 'E141_支点': (e141_fulcrum, 22),
 'E141_片头': (titles.opening(SER25, VOL25, S25A, 9, '1987 年第一例腹腔镜胆囊切除术'), 7),
 'E141_片尾': (titles.closing(SER25, VOL25, S25A, 9, '下集：第二十五季特辑 · 第九层回顾'), 7),
 'S25_第九层': (s25_layer, 30),
}

if __name__ == '__main__':
    import kit
    if len(sys.argv) > 2 and sys.argv[1] == 'prev':
        kit.preview(CLIPS, sys.argv[2], float(sys.argv[3]))
    else:
        names = sys.argv[1:] or list(CLIPS)
        kit.render_all({n: CLIPS[n] for n in names})
