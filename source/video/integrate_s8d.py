"""把第八季收尾（E61 / 特辑8）的拍摄包并入仓库。
导航改为「在现有导航里插入新链接」，不再整体重写，免得冲掉排期、发布素材等后加的链接。"""
import os, re, shutil, subprocess, glob
REPO = '/home/claude/cong-ling-zao-wu'
OUT = '/home/claude/video/out'
SCR = '/tmp/claude-0/-home-claude/2bae78cb-602b-5cf3-a87b-834191483ac2/scratchpad'
STD = [('粗剪样片', 'rough-cut'), ('片头', 'title-open'), ('问题1', 'question-1'), ('资料', 'history')]
EPS = {
 'E61': ('ep61', [('来回', 'reversible-reaction'), ('能量密度', 'energy-density')]),
}
SPECIAL = {'S8': ('season8', [('S8_粗剪样片', 's8-rough-cut'), ('S8_第二层', 's8-second-layer'), ('S8_问题', 's8-question'), ('S8_评分', 's8-scoring'), ('S8_结论', 's8-conclusion')])}
AFTER = '<a href="../ep60/">60</a>'
NEW = '<a href="../ep61/">61</a><a href="../season8/">特辑8</a>'

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).decode())

ref = open(f'{REPO}/ep51/index.html', encoding='utf-8').read()
HEAD = ref[:ref.index('<title>')]
NAV = re.search(r'<nav class="repo-nav".*?</nav>', ref, re.S).group(0)
if NEW not in NAV:
    NAV = NAV.replace(AFTER, AFTER + NEW, 1)

for ep, (folder, anim) in EPS.items():
    clips = [(f'{ep}_{n}', f'{ep.lower()}-{s}') for n, s in STD + [anim[0], ('问题2', 'question-2'), anim[1], ('结论', 'conclusion'), ('片尾', 'title-close')]]
    for src, slug in clips:
        s = f'{OUT}/{src}.mp4'
        shutil.copy(s, f'{REPO}/media/video/{slug}.mp4')
        L = dur(s); t = 30 if 'rough' in slug else L * 0.8
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.2f}', '-i', s, '-frames:v', '1', '-vf', 'scale=960:-2', '-q:v', '4',
                        f'{REPO}/media/posters/{slug}.jpg'], check=True)
        print(slug, f'{L:.1f}s')
    body = open(f'{SCR}/{ep.lower()}-plan.html', encoding='utf-8').read()
    body = body.replace('<div class="wrap">', '<div class="wrap">\n' + NAV, 1)
    os.makedirs(f'{REPO}/{folder}', exist_ok=True)
    open(f'{REPO}/{folder}/index.html', 'w', encoding='utf-8').write(HEAD + body + '\n</html>\n')

for ep, (folder, clips) in SPECIAL.items():
    for src, slug in clips:
        s_ = f'{OUT}/{src}.mp4'
        shutil.copy(s_, f'{REPO}/media/video/{slug}.mp4')
        L = dur(s_); t = 30 if 'rough' in slug else L * 0.8
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.2f}', '-i', s_, '-frames:v', '1', '-vf', 'scale=960:-2', '-q:v', '4',
                        f'{REPO}/media/posters/{slug}.jpg'], check=True)
        print(slug, f'{L:.1f}s')
    body = open(f'{SCR}/{ep.lower()}-plan.html', encoding='utf-8').read()
    body = body.replace('<div class="wrap">', '<div class="wrap">\n' + NAV, 1)
    os.makedirs(f'{REPO}/{folder}', exist_ok=True)
    open(f'{REPO}/{folder}/index.html', 'w', encoding='utf-8').write(HEAD + body + '\n</html>\n')

n = 0
for f in glob.glob(f'{REPO}/*/index.html') + glob.glob(f'{REPO}/*/voice.html'):
    s = open(f, encoding='utf-8').read()
    head, sep, rest = s.partition('</nav>')
    if AFTER in head and NEW not in head:
        open(f, 'w', encoding='utf-8').write(head.replace(AFTER, AFTER + NEW, 1) + sep + rest); n += 1
print('nav updated', n)
for f in ['s8d.py', 's8d_eps.py', 'integrate_s8d.py']:
    shutil.copy(f'/home/claude/video/{f}', f'{REPO}/source/video/{f}')
print('videos', len(glob.glob(f'{REPO}/media/video/*.mp4')))
