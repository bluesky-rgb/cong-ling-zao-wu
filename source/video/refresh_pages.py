"""Rebuild plan pages (and selected cards / rough cuts) after fact fixes."""
import sys, os, re, shutil, subprocess, importlib
sys.path.insert(0, '/home/claude/video'); os.chdir('/home/claude/video')
import kit
from s4a_eps import fmt
REPO = '/home/claude/cong-ling-zao-wu'; OUT = '/home/claude/video/out'
SCR = '/tmp/claude-0/-home-claude/2bae78cb-602b-5cf3-a87b-834191483ac2/scratchpad'
def folder(ep):
    if ep[0] == 'E': return 'ep' + ep[1:]
    if ep[0] == 'B': return ep.lower()
    if ep[0] == 'S': return 'season' + ep[1:]
def page_html(m, ep):
    shots, end = m.SH[ep]; sp = dict(m.SPEC[ep])
    sp['shots'] = [(s[0], fmt(s[1]), 'done' if s[5] else ('res' if s[2] == 'res' else 'real'), s[3], s[4]) for s in shots]
    sp['shots_lead'] = f'粗剪样片约 {fmt(end)}。已渲染的动画、资料卡、问题卡和片头片尾都已就位；其余镜头是占位画面。旁白里括号中的内容，要按实测结果改写。'
    return kit.page(sp)
def write_page(ep, body):
    open(f'{SCR}/{ep.lower()}-plan.html', 'w', encoding='utf-8').write(body)
    p = f'{REPO}/{folder(ep)}/index.html'
    old = open(p, encoding='utf-8').read()
    head = old[:old.index('<title>')]
    nav = re.search(r'<nav class="repo-nav".*?</nav>', old, re.S).group(0)
    body = body.replace('<div class="wrap">', '<div class="wrap">\n' + nav, 1)
    open(p, 'w', encoding='utf-8').write(head + body + '\n</html>\n')
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).decode())
def ship(src, slug):
    s = f'{OUT}/{src}.mp4'; shutil.copy(s, f'{REPO}/media/video/{slug}.mp4')
    t = 30 if 'rough' in slug else dur(s) * 0.8
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',f'{t:.2f}','-i',s,'-frames:v','1','-vf','scale=960:-2','-q:v','4',f'{REPO}/media/posters/{slug}.jpg'], check=True)
mods = sys.argv[1].split(',')
rerender = sys.argv[2].split(',') if len(sys.argv) > 2 and sys.argv[2] else []
for mn in mods:
    m = importlib.import_module(mn)
    for ep in m.SH:
        if ep in rerender:
            names = [k for k in m.CARDS if k.startswith(ep + '_')]
            kit.render_all({k: m.CARDS[k] for k in names if k.endswith('_资料')})
            m.build(ep)   # roughcut + scratch page
            ship(f'{ep}_资料', f'{ep.lower()}-history'); ship(f'{ep}_粗剪样片', f'{ep.lower()}-rough-cut')
            print('re-rendered', ep)
        write_page(ep, page_html(m, ep))
        print('page', ep)
