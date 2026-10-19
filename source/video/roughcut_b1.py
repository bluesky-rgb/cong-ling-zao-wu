import subprocess, os
from lib import *

OUT = '/home/claude/video/out'
TMP = '/home/claude/video/tmp_b1'
os.makedirs(TMP, exist_ok=True)
KCOL = {'实拍': COPPER, '录屏': FIELD, '待补': MUTED, '待结果': SPARK}

# (no, start, kind, what, voiceover, clip)
SHOTS = [
 (1, 0, '实拍', '铁片小鱼浮在水碗里，转了半圈后停下，鱼头指南；旁边放指南针对照', '这条铁鱼从没碰过磁石，可它一停下来，鱼头就指着南方。', None),
 (2, 8, '字幕卡', '', '', 'card_q'),
 (3, 14, '片头', '', '', 'B1_片头'),
 (4, 21, '动画', '', '', 'B1_原文卡'),
 (5, 46, '实拍', '用剪刀把薄铁皮剪成两寸长的小鱼，头尾剪尖', '先照着原文做一条。', None),
 (6, 64, '实拍', '用钳子夹住鱼头放到火上烧红；取出后鱼尾朝北，斜着蘸进水盆', '烧到通红，夹住鱼头，鱼尾朝北，蘸进水里。', None),
 (7, 92, '实拍', '把鱼平放在水面，转动后指南；旁边一条没烧过的鱼不指南', '成了。没烧过的那条，停在哪儿都行。', None),
 (8, 120, '字幕卡', '', '', 'card_q2'),
 (9, 126, '动画', '', '', 'B1_热剩磁'),
 (10, 150, '动画', '', '', 'B1_两种解释'),
 (11, 170, '实拍', '四组对照实验：A 照原文；B 鱼尾朝东；C 换成不吸磁铁的铜夹子；D 不加热', '同样的铁片，每组只改一个条件，每组做三次。', None),
 (12, 240, '待结果', '记录表特写：每组鱼头指向哪里、能不能稳定指南', '结果揭晓（按实拍结果配旁白）', None),
 (13, 270, '待结果', '结论卡：哪种解释被支持', '按结果二选一的结论旁白，见拍摄本', None),
 (14, 300, '实拍', '用磁铁沿一个方向磨钢针，放在水面上指南，和指南鱼对比', '四十多年后，沈括记下了更好的办法：用磁石磨针。', None),
 (15, 325, '片尾', '', '', 'B1_片尾'),
]
END = 332

def card(lines, dur, name):
    def draw(c, t, i):
        corner_tag(c, 'B 线 · 指南鱼')
        for k, ln in enumerate(lines):
            a = fade(t, 0.2 + k * 0.4, 0.8 + k * 0.4)
            c.text(960, 500 + k * 120 - (len(lines) - 1) * 60, ln, 'serif', 76, mix(BG, COPPER if k == len(lines) - 1 else INK, a), 'mm')
    render(f'{OUT}/{name}.mp4', dur, draw)

card(['这条铁鱼没碰过磁石', '为什么会指南？'], 6, 'card_q')
card(['烧红、朝北、蘸水', '哪一步真正起作用？'], 6, 'card_q2')

def placeholder(no, start, kind, what, vo, dur):
    c = Canvas(); col = KCOL[kind]
    c.rect(80, 80, 1840, 1000, outline=mix(BG, col, 0.6), width=3, r=24)
    lab = '待实拍' if kind == '实拍' else ('待实拍结果' if kind == '待结果' else '待补做')
    c.rect(130, 130, 130 + c.textw(lab, 'bold', 34) + 44, 192, fill=mix(BG, col, 0.2), r=10)
    c.text(152, 161, lab, 'bold', 34, col, 'lm')
    c.text(130, 260, f'镜头 {no}', 'serif', 96, INK)
    c.text(130, 400, '画面', 'sans', 28, MUTED)
    c.text(130, 450, what, 'bold', 40, INK)
    c.text(130, 560, '旁白', 'sans', 28, MUTED)
    c.text(130, 610, f'「{vo}」', 'serif', 46, INK)
    m, s = divmod(start, 60)
    c.text(130, 900, f'{m}:{s:02d} 开始 · 时长约 {dur} 秒', 'mono', 28, MUTED)
    p = f'{TMP}/ph{no:02d}.png'; c.im.reduce(SS).save(p); return p

ENC = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', '30']
parts = []
for k, (no, start, kind, what, vo, clip) in enumerate(SHOTS):
    dur = (SHOTS[k + 1][1] if k + 1 < len(SHOTS) else END) - start
    out = f'{TMP}/seg{no:02d}.mp4'
    if clip:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{OUT}/{clip}.mp4', '-vf',
                        f'tpad=stop_mode=clone:stop_duration={dur},trim=duration={dur}', *ENC, out], check=True)
    else:
        png = placeholder(no, start, kind, what, vo, dur)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', png, '-t', str(dur), *ENC, '-tune', 'stillimage', out], check=True)
    parts.append(out)
with open(f'{TMP}/list.txt', 'w') as f:
    for p in parts: f.write(f"file '{p}'\n")
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{TMP}/list.txt', '-c', 'copy',
                '-movflags', '+faststart', f'{OUT}/B1_指南鱼_粗剪样片.mp4'], check=True)
print('ok')
