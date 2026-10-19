"""可复用的单集制作工具：问题卡、资料卡、占位画面、粗剪样片、拍摄本网页。"""
import subprocess, os, json, html
from lib import *

OUT = '/home/claude/video/out'

# ---------- cards ----------
def card(tag, lines, dur=6):
    def draw(c, t, i):
        corner_tag(c, tag)
        for k, ln in enumerate(lines):
            a = fade(t, 0.2 + k * 0.4, 0.8 + k * 0.4)
            c.text(960, 500 + k * 120 - (len(lines) - 1) * 60, ln, 'serif', 76,
                   mix(BG, COPPER if k == len(lines) - 1 else INK, a), 'mm')
    return draw, dur

def history(tag, title, rows, dur=20):
    """资料卡：标题 + 若干行（年份, 文字）。"""
    def draw(c, t, i):
        corner_tag(c, tag)
        c.text(160, 210, title, 'serif', 56, mix(BG, INK, fade(t, 0.1, 0.8)))
        c.line([(160, 300), (1760, 300)], LINE, 2)
        for k, (yr, txt) in enumerate(rows):
            t0 = 0.8 + k * (dur - 3) / max(1, len(rows))
            a = fade(t, t0, t0 + 0.7)
            y = 400 + k * 170
            c.text(160, y, yr, 'mono', 34, mix(BG, COPPER, a), 'lm')
            for j, part in enumerate(txt.split('\n')):
                c.text(470, y + j * 50, part, 'sans', 36, mix(BG, INK, a), 'lm')
    return draw, dur

def placeholder(path, no, start, kind, what, vo, dur, tag):
    c = Canvas()
    col = {'实拍': COPPER, '待结果': SPARK, '录屏': FIELD}.get(kind, MUTED)
    lab = {'实拍': '待实拍', '待结果': '待实拍结果', '录屏': '待录屏'}.get(kind, '待补做')
    c.rect(80, 80, 1840, 1000, outline=mix(BG, col, 0.6), width=3, r=24)
    c.rect(130, 130, 130 + c.textw(lab, 'bold', 34) + 44, 192, fill=mix(BG, col, 0.2), r=10)
    c.text(152, 161, lab, 'bold', 34, col, 'lm')
    c.text(1790, 161, tag, 'sans', 26, MUTED, 'rm')
    c.text(130, 260, f'镜头 {no}', 'serif', 96, INK)
    c.text(130, 400, '画面', 'sans', 28, MUTED)
    wrap_text(c, 130, 450, what, 'bold', 40, INK, 1640, 54)
    c.text(130, 600, '旁白', 'sans', 28, MUTED)
    wrap_text(c, 130, 650, f'「{vo}」', 'serif', 40, INK, 1640, 56, max_lines=4)
    m, s = divmod(start, 60)
    c.text(130, 930, f'{m}:{s:02d} 开始 · 时长约 {dur} 秒', 'mono', 28, MUTED)
    c.im.reduce(SS).save(path)

def wrap_text(c, x, y, s, kind, px, col, width, lh, max_lines=3):
    line, lines = '', []
    for ch in s:
        if c.textw(line + ch, kind, px) > width:
            lines.append(line); line = ch
        else:
            line += ch
    if line: lines.append(line)
    if len(lines) > max_lines:
        lines = lines[:max_lines]; lines[-1] = lines[-1][:-1] + '…'
    for k, ln in enumerate(lines):
        c.text(x, y + k * lh, ln, kind, px, col)

ENC = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', '30']

def roughcut(slug, tag, shots, end, outname):
    """shots: (no, start, kind, picture, voiceover, clip_name or None)"""
    tmp = f'/home/claude/video/tmp_{slug}'
    os.makedirs(tmp, exist_ok=True)
    parts = []
    for k, (no, start, kind, what, vo, clip) in enumerate(shots):
        dur = (shots[k + 1][1] if k + 1 < len(shots) else end) - start
        out = f'{tmp}/seg{no:02d}.mp4'
        if clip:
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{OUT}/{clip}.mp4', '-vf',
                            f'tpad=stop_mode=clone:stop_duration={dur},trim=duration={dur}', *ENC, out], check=True)
        else:
            png = f'{tmp}/ph{no:02d}.png'
            placeholder(png, no, start, kind, what, vo, dur, tag)
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', png, '-t', str(dur), *ENC,
                            '-tune', 'stillimage', out], check=True)
        parts.append(out)
    with open(f'{tmp}/list.txt', 'w') as f:
        for p in parts: f.write(f"file '{p}'\n")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt',
                    '-c', 'copy', '-movflags', '+faststart', f'{OUT}/{outname}.mp4'], check=True)

def render_all(clips):
    for name, (f, dur) in clips.items():
        render(f'{OUT}/{name}.mp4', dur, f)
        print('rendered', name)

def preview(clips, name, t, path='/home/claude/video/prev.png'):
    f, _ = clips[name]
    c = Canvas(); f(c, t, 0); c.im.reduce(SS).save(path)

# ---------- 拍摄本网页 ----------
CSS = open(os.path.join(os.path.dirname(__file__), 'page.css'), encoding='utf-8').read() if os.path.exists(os.path.join(os.path.dirname(__file__), 'page.css')) else ''

def e(s): return html.escape(str(s))

def page(spec):
    """spec keys: key, eyebrow, title, thesis, facts[(k,v)], background[(title, html)], ladder[(myth, fix)],
    layers[3], design, groups{head:[], rows:[[]]}, steps[], log{rows:[], unit, cols:[...]}, verify[], safety[], props[(a,b)],
    shots[(no, tc, kind, pic, vo)], sources[(title,url,note)]"""
    tag = {'real': ('待实拍', 'real'), 'done': ('已渲染', 'done'), 'res': ('待实拍结果', 'res')}
    out = [f'<title>{e(spec["title"])}拍摄本</title>\n<meta name="claude:viewport-fit-sides" content="cover">',
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;900&family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;600&display=swap">',
           f'<style>\n{CSS}\n</style>', '<div class="wrap">', '<header>',
           f'<div class="eyebrow">{e(spec["eyebrow"])}</div>', f'<h1>{e(spec["title"])}</h1>',
           f'<p class="thesis">{e(spec["thesis"])}</p>', '<div class="facts">']
    out += [f'<div><span>{e(k)}</span>{e(v)}</div>' for k, v in spec['facts']]
    out += ['</div>', '</header>']
    if spec.get('background'):
        out += ['<section>', '<h2>背景</h2>']
        for t, body in spec['background']:
            out.append(f'<div class="ol"><p class="o">{e(t)}</p><p class="p">{body}</p></div>')
        out.append('</section>')
    out += ['<section>', '<h2>理解路径</h2>', '<p class="lead">先说出观众最常见的误解，再用实验当场打破它。</p>', '<ol class="ladder">']
    out += [f'<li><span class="k">{i+1}</span><span><s>{e(m)}</s> → {e(f)}</span></li>' for i, (m, f) in enumerate(spec['ladder'])]
    out += ['</ol>', '<h3>三层「为什么」</h3>', '<div class="layers">']
    for lab, txt in zip(['现象层', '规律层', '本质层'], spec['layers']):
        out.append(f'<div class="layer"><span>{lab}</span><p>{e(txt)}</p></div>')
    out.append('</div>')
    if spec.get('design'):
        out.append(f'<p class="lead"><b>原理 → 设计决策：</b>{e(spec["design"])}</p>')
    out.append('</section>')
    # experiment
    g = spec['groups']
    out += ['<section>', '<h2>实验设计</h2>', f'<p class="lead">{e(g.get("lead",""))}</p>', '<div class="tw"><table><thead><tr>']
    out += [f'<th>{e(h)}</th>' for h in g['head']]
    out += ['</tr></thead><tbody>']
    for r in g['rows']:
        out.append('<tr>' + ''.join(f'<td>{e(x)}</td>' for x in r) + '</tr>')
    out += ['</tbody></table></div>', '<h3>操作步骤</h3>', '<ol class="steps">']
    out += [f'<li>{e(s)}</li>' for s in spec['steps']]
    out += ['</ol>']
    lg = spec['log']
    out += ['<h3>实验记录</h3>', '<p class="hint">拍摄时直接填写，只保存在这台设备的浏览器里；拍完截图发给 Claude，旁白会按真实数据改写。</p>',
            '<div class="tw"><table class="log"><thead><tr><th>条件</th>' + ''.join(f'<th>{e(c)}</th>' for c in lg['cols']) + '<th>备注</th></tr></thead><tbody>']
    for ri, r in enumerate(lg['rows']):
        cells = ''.join(f'<td><input type="text" inputmode="decimal" data-k="{spec["key"]}-{ri}-{ci}" aria-label="{e(r)} {e(c)}"></td>' for ci, c in enumerate(lg['cols']))
        out.append(f'<tr><td>{e(r)}</td>{cells}<td><input type="text" data-k="{spec["key"]}-{ri}-n" aria-label="{e(r)} 备注"></td></tr>')
    out += ['</tbody></table></div>', '<div class="row"><button type="button" id="clearlog">清空记录</button></div>']
    out += ['<h3>实践时要验证</h3>', '<ul class="verify">'] + [f'<li>{e(v)}</li>' for v in spec['verify']] + ['</ul>', '</section>']
    # safety & props
    out += ['<section>', '<h2>安全与道具</h2>', '<div class="warn"><b>安全提示</b><ul>'] + [f'<li>{e(s)}</li>' for s in spec['safety']] + ['</ul></div>']
    out += ['<div class="tw"><table><thead><tr><th>道具</th><th>用途</th></tr></thead><tbody>']
    out += [f'<tr><td>{e(a)}</td><td>{e(b)}</td></tr>' for a, b in spec['props']]
    out += ['</tbody></table></div>', '</section>']
    # shots
    out += ['<section>', '<h2>分镜与旁白</h2>',
            f'<p class="lead">{e(spec.get("shots_lead","已渲染的动画、资料卡、问题卡和片头片尾都在粗剪样片里；其余镜头是占位画面。旁白里括号中的内容，要按实测结果改写。"))}</p>',
            '<div class="row"><button type="button" class="primary" id="copyAll">复制全部旁白</button></div>', '<div id="shots" class="shots"></div>', '</section>']
    out += ['<section>', '<h2>来源</h2>', '<ol class="src">']
    out += [f'<li><a href="{e(u)}">{e(t)}</a>{(" <span>" + e(n) + "</span>") if n else ""}</li>' for t, u, n in spec['sources']]
    out += ['</ol>', '</section>', '</div>']
    shots = [[s[0], s[1], s[2], s[3], s[4]] for s in spec['shots']]
    out.append('<script>\n(function(){\nconst SH=' + json.dumps(shots, ensure_ascii=False) + ';\n' + JS + '\n})();\n</script>')
    return '\n'.join(out)

JS = r"""
const TAG={real:['待实拍','real'],done:['已渲染','done'],res:['待实拍结果','res']};
function copy(t,btn){const lab=btn.textContent;const ok=()=>{btn.textContent='已复制';setTimeout(()=>btn.textContent=lab,1500)};
 if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,fb)}else fb();
 function fb(){const ta=document.createElement('textarea');ta.value=t;ta.setAttribute('readonly','');ta.style.position='absolute';ta.style.left='-9999px';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok()}catch(e){btn.textContent='请长按文字复制'}document.body.removeChild(ta);}}
const box=document.getElementById('shots');
SH.forEach(s=>{const a=document.createElement('article');a.className='shot';const g=TAG[s[2]];
 a.innerHTML=`<div class="meta"><span class="no">镜头 ${s[0]}</span><span class="tc">${s[1]}</span><span class="tag ${g[1]}">${g[0]}</span></div><p class="pic"></p>${s[4]?'<p class="vo2"></p><button type="button">复制旁白</button>':''}`;
 a.querySelector('.pic').textContent=s[3];if(s[4]){a.querySelector('.vo2').textContent=s[4];const b=a.querySelector('button');b.onclick=()=>copy(s[4],b);}box.appendChild(a);});
document.getElementById('copyAll').onclick=function(){copy(SH.filter(s=>s[4]).map(s=>s[4]).join('\n\n'),this);};
const inputs=[...document.querySelectorAll('.log input')];
inputs.forEach(i=>{try{i.value=localStorage.getItem('log-'+i.dataset.k)||''}catch(e){}i.addEventListener('input',()=>{try{localStorage.setItem('log-'+i.dataset.k,i.value)}catch(e){}});});
document.getElementById('clearlog').onclick=()=>{inputs.forEach(i=>{i.value='';try{localStorage.removeItem('log-'+i.dataset.k)}catch(e){}});};
"""
