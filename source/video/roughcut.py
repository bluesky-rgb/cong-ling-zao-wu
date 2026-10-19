import subprocess, os
from lib import *

OUT = '/home/claude/video/out'
TMP = '/home/claude/video/tmp'
os.makedirs(TMP, exist_ok=True)

# (no, start s, kind, what, voiceover, rendered clip or None)
SHOTS = [
 (1, 0, '实拍', '磁铁静止插在线圈中，电流表特写，指针为 0', '这块磁铁就在线圈里，为什么一点电都没有？', None),
 (2, 6, '实拍', '快速抽出磁铁，指针猛跳（慢动作）', '但我一抽——', None),
 (3, 12, '字幕卡', '', '今天只讲这一句话。', '镜头03_核心字幕卡'),
 (4, 20, '录屏', '「从零造电」网页科技树，前 3 步亮起，第 4 步闪烁', '上集我们用电堆做出了电磁铁……', '片头_第04集'),
 (5, 40, '实拍', '电堆 + 导线 + 指南针，接通电流的瞬间', '1820 年，奥斯特发现：电能生磁。', None),
 (6, 70, '字幕卡', '', '先停一下，你觉得呢？', '镜头06_问题卡'),
 (7, 80, '实拍', '线圈接电流表，磁铁放进去不动，等 5 秒（分屏）', '很多人以为放进去就行。等等……', None),
 (8, 120, '实拍', '慢插 vs 快插，左右分屏同时播放', '同一块磁铁，插得越快，指针跳得越高。', None),
 (9, 160, '实拍', '插入和拔出对比，指针分别向左、向右偏', '方向也反了——记住这个，后面要用。', None),
 (10, 190, '动画', '', '把穿过线圈的磁感线当成根数来数。', '镜头10_磁感线计数'),
 (11, 230, '录屏', '网页第 04 章：磁通量曲线和电压曲线对照', '磁通量最大的时候，电压反而是 0。', None),
 (12, 280, '字幕卡', '', '电压 = 匝数 × 磁通量变化的快慢。', '镜头12_公式卡'),
 (13, 320, '实拍', '5 匝和 50 匝线圈，同样速度插入磁铁', '多绕几圈，电压就翻倍。', None),
 (14, 360, '动画', '', '为什么会这样？把镜头放大到导线里面……', '镜头14_导线里的电子'),
 (15, 420, '字幕卡', '', '要持续发电，就得让磁通量一直变。', '镜头15_问题卡'),
 (16, 440, '实拍', '手摇磁铁旋转扫过线圈，小灯泡一闪一闪', '转起来——这就是发电机的雏形。', None),
 (17, 490, '动画', '', '还记得指针会反向吗？这就是交流电。', '镜头17_交流电波形'),
 (18, 530, '待补', '1831 年法拉第铁环实验示意图', '法拉第花了几个月才找到这个答案。', '镜头18_法拉第铁环'),
 (19, 560, '录屏', '网页科技树：第 4 步亮起，第 5 步出现问号', '下集：为什么接上灯泡，手柄就变沉了？', '片尾_第04集'),
 (20, 585, '字幕卡', '', '简介里可以自己动手调参数。', '镜头20_结尾卡'),
]
END = 600
KCOL = {'实拍': COPPER, '录屏': FIELD, '待补': MUTED}

def placeholder(no, start, kind, what, vo, dur):
    c = Canvas()
    col = KCOL[kind]
    c.rect(80, 80, 1840, 1000, outline=mix(BG, col, 0.6), width=3, r=24)
    c.rect(130, 130, 130 + c.textw(f'待{kind}' if kind != '待补' else '待补做', 'bold', 34) + 44, 192, fill=mix(BG, col, 0.2), r=10)
    c.text(152, 161, f'待{kind}' if kind != '待补' else '待补做', 'bold', 34, col, 'lm')
    c.text(130, 260, f'镜头 {no}', 'serif', 96, INK)
    c.text(130, 400, '画面', 'sans', 28, MUTED)
    c.text(130, 450, what, 'bold', 46, INK)
    c.text(130, 560, '旁白', 'sans', 28, MUTED)
    c.text(130, 610, f'「{vo}」', 'serif', 50, mix(BG, INK, 0.9))
    m, s = divmod(start, 60)
    c.text(130, 900, f'{m}:{s:02d} 开始 · 时长约 {dur} 秒', 'mono', 28, MUTED)
    c.text(1790, 900, '拍好后在剪辑软件里替换这一段', 'sans', 28, MUTED, 'rs')
    path = f'{TMP}/ph{no:02d}.png'
    c.im.reduce(SS).save(path)
    return path

ENC = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', '30']
parts = []
for k, (no, start, kind, what, vo, clip) in enumerate(SHOTS):
    dur = (SHOTS[k + 1][1] if k + 1 < len(SHOTS) else END) - start
    out = f'{TMP}/seg{no:02d}.mp4'
    if clip:
        src = f'{OUT}/{clip}.mp4'
        # freeze last frame to fill the slot (narration time)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-vf',
                        f'tpad=stop_mode=clone:stop_duration={dur},trim=duration={dur}', *ENC, out], check=True)
    else:
        png = placeholder(no, start, kind, what, vo, dur)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', png, '-t', str(dur), *ENC,
                        '-tune', 'stillimage', out], check=True)
    parts.append(out)
    print(no, dur)

with open(f'{TMP}/list.txt', 'w') as f:
    for p in parts: f.write(f"file '{p}'\n")
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{TMP}/list.txt',
                '-c', 'copy', '-movflags', '+faststart', f'{OUT}/第04集_磁生电_粗剪样片.mp4'], check=True)
print('ok')
