"""生成三张汇总页：拍摄总排期与采购清单（shooting/）、发布素材（publish/）、待核清单（checklist/）。
数据来自各批 *_eps.py 的 SPEC / SH，以及选题详案里的播出顺序。"""
import json, re, html, os, importlib, glob, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
REPO = '/home/claude/cong-ling-zao-wu'
SCR = '/tmp/claude-0/-home-claude/2bae78cb-602b-5cf3-a87b-834191483ac2/scratchpad'
e = lambda s: html.escape(str(s))

# ---------- 数据 ----------
D = {}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*_eps.py'))):
    m = importlib.import_module(os.path.basename(f)[:-3])
    for ep, sp in getattr(m, 'SPEC', {}).items():
        D[ep] = dict(sp=sp, sh=m.SH.get(ep))
epsrc = open(f'{REPO}/episodes/index.html', encoding='utf-8').read()
SEASONS = []
for name, label in [('SEASON', '第一季'), ('SEASON2', '第二季'), ('SEASON3', '第三季'), ('SEASON4', '第四季'), ('SEASON5', '第五季'), ('SEASON6', '第六季'), ('SEASON7', '第七季'), ('SEASON8', '第八季'), ('SEASON9', '第九季'), ('SEASON10', '第十季'), ('SEASON11', '第十一季'), ('SEASON12', '第十二季'), ('SEASON13', '第十三季'), ('SEASON14', '第十四季'), ('SEASON15', '第十五季'), ('SEASON16', '第十六季'), ('SEASON17', '第十七季'), ('SEASON18', '第十八季'), ('SEASON19', '第十九季'), ('SEASON20', '第二十季'), ('SEASON21', '第二十一季'), ('SEASON22', '第二十二季'), ('SEASON23', '第二十三季'), ('SEASON24', '第二十四季'), ('SEASON25', '第二十五季'), ('SEASON26', '第二十六季'), ('SEASON27', '第二十七季'), ('SEASON28', '第二十八季'), ('SEASON29', '第二十九季'), ('SEASON30', '第三十季'), ('SEASON31', '第三十一季'), ('SEASON32', '第三十二季'), ('SEASON33', '第三十三季'), ('SEASON34', '第三十四季')]:
    body = re.search(r'const %s=\[(.*?)\n\];' % name, epsrc, re.S).group(1)
    SEASONS.append((label, re.findall(r"\['([^']+)',", body)))
ROWS = {}
for m in re.finditer(r"^\['([EBH]\d+)',(\d),'([^']*)','([^']*)','([^']*)'", epsrc, re.M):
    ROWS[m.group(1)] = dict(title=m.group(3), era=m.group(4), hook=m.group(5))

def code(x):
    if x.startswith('特辑'): return 'S' + (x[2:] or '1')
    return x
def folder(c):
    if c[0] == 'E': return 'ep' + c[1:]
    if c[0] in 'BH': return c.lower()
    return 'season' + c[1:]
def label(c):
    if c[0] == 'E': return c[1:]
    if c[0] == 'S': return '特辑' + ('' if c == 'S1' else c[1:])
    return c
def title(c):
    if c in D: return D[c]['sp']['title']
    return ROWS.get(c, {}).get('title', c)

# ---------- 公共外壳 ----------
src = open(f'{REPO}/ep51/index.html', encoding='utf-8').read()
HEAD = src[:src.index('<title>')]
i = src.index('<style>', src.index('<title>')); j = src.index('</style>', i)
CSS = src[i + 7:j]
NAV = re.search(r'<nav class="repo-nav".*?</nav>', src, re.S).group(0)
EXTRA = '''
.chk{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px solid var(--line)}
.chk input{margin-top:6px;width:18px;height:18px;flex:none;accent-color:var(--copper)}
.chk .t{min-width:0}.chk .t b{font-weight:500}.chk .t small{display:block;color:var(--muted);font-size:13px}
.pill{display:inline-block;font-family:var(--mono);font-size:11px;letter-spacing:.06em;border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin:2px 4px 2px 0;color:var(--muted);white-space:nowrap}
.pill.hot{border-color:var(--warn);color:var(--warn)}.pill.ok{border-color:var(--good);color:var(--good)}
.card{background:var(--sheet);border:1px solid var(--line);border-radius:8px;padding:14px 16px;display:grid;gap:8px;min-width:0}
.card h3{font-size:19px;font-weight:900}
.card .k{font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted)}
.card pre{white-space:pre-wrap;font-family:var(--body);font-size:14px;margin:0;background:var(--paper);border-radius:6px;padding:10px 12px;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:12px}
.copy{justify-self:start;font-size:13px;padding:4px 10px}
details{background:var(--sheet);border:1px solid var(--line);border-radius:8px;padding:10px 14px}
details summary{cursor:pointer;font-weight:500}
details[open] summary{margin-bottom:8px}
.big{font-family:var(--display);font-size:clamp(22px,4vw,30px);font-weight:900}
'''
JS = '''<script>
(function(){
  var KEY=location.pathname+'#chk';var st={};
  try{st=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){st={}}
  document.querySelectorAll('input[data-k]').forEach(function(b){
    b.checked=!!st[b.dataset.k];
    b.addEventListener('change',function(){st[b.dataset.k]=b.checked;try{localStorage.setItem(KEY,JSON.stringify(st))}catch(e){}});
  });
  document.querySelectorAll('button.copy').forEach(function(btn){
    btn.addEventListener('click',function(){
      var t=document.getElementById(btn.dataset.t).innerText;
      var done=function(){btn.textContent='已复制';setTimeout(function(){btn.textContent='复制'},1500)};
      if(navigator.clipboard){navigator.clipboard.writeText(t).then(done,function(){})}
    });
  });
})();
</script>'''

def shell(ttl, eyebrow, h1, thesis, facts, body):
    out = [f'<title>{e(ttl)}</title>\n<meta name="claude:viewport-fit-sides" content="cover">',
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;900&family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;600&display=swap">',
           f'<style>{CSS}{EXTRA}</style>', '<div class="wrap">', 'NAVPLACEHOLDER',
           f'<header><div class="eyebrow">{e(eyebrow)}</div><h1>{e(h1)}</h1><p class="thesis">{e(thesis)}</p>',
           '<div class="facts">' + ''.join(f'<div><span>{e(k)}</span>{e(v)}</div>' for k, v in facts) + '</div></header>',
           body, '</div>', JS]
    return '\n'.join(out)

def write(folder_, page, scratch_name):
    open(f'{SCR}/{scratch_name}', 'w', encoding='utf-8').write(page.replace('NAVPLACEHOLDER\n', ''))
    os.makedirs(f'{REPO}/{folder_}', exist_ok=True)
    open(f'{REPO}/{folder_}/index.html', 'w', encoding='utf-8').write(HEAD + page.replace('NAVPLACEHOLDER', NAV) + '\n</html>\n')

def table(head, rows):
    return ('<div class="tw"><table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>'
            + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')

def eplink(c, rel='..'):
    if not os.path.isdir(f'{REPO}/{folder(c)}'):
        return f'{e(label(c))} {e(title(c))} <span class="pill">待做</span>'
    return f'<a href="{rel}/{folder(c)}/">{e(label(c))} {e(title(c))}</a>'

# ================================================================ 拍摄总排期
LONG = [  # (code, 提前多久, 做什么)
 ('B46', '约 1 周', '三种含水量的夯土柱脱模后晾干 3–5 天再压'),
 ('B49', '1 周', '三只米罐放进高湿收纳箱，连续 7 天记湿度'),
 ('E24', '约 1 个月', '糯米灰浆试块要养护 7 / 14 / 28 天再测强度'),
 ('E29', '3–4 周', '豆科与非豆科盆栽，挖根看根瘤、再翻土'),
 ('B32', '2 周', '烟灰墨与记号笔的字贴窗晒 14 天'),
 ('B35', '约 2 周', '石灰小块脱模后泡盐水 14 天'),
 ('E67', '约 4 周', '豆苗盆栽四组对照，每周量一次株高'),
 ('E27', '约 2 周', '陶罐滴灌与浇水对照，连续两周记录'),
 ('E30', '约 2 周', '发芽、选种与嫁接成活观察'),
 ('B15', '约 2 周', '米酒敞口放置，测酸度变化（不饮用）'),
 ('E32', '1–2 周', '面包发霉对照（洗手 / 不洗手），全程密封'),
 ('E51', '1–2 周', '面包、橘子在密封袋里长霉，全程不开封'),
 ('E37', '约 1 周', '罐藏与敞口对照，第 1、3、5、7 天拍'),
 ('E16', '3 天+', '泥坯晾干三天再烧、再泡水'),
 ('E33', '3 天', '绿豆发芽（可用第 30 集剩下的绿豆）'),
 ('E34', '2 天', '净水对照盖保鲜膜放两天'),
 ('E31', '1–2 天', '生鸡蛋泡白醋去壳（不食用）'),
 ('B2', '1 天', '石膏或水泥模型凝固一天后脱模'),
 ('E63', '2 天–1 周', '石膏小梁干两天（水泥砂浆养护一周）再加载'),
 ('E20', '1 天', '盐水静置，第二天拍杯底结晶'),
]
VENUES = [  # (地点, [(code, 拍什么)], 提示)
 ('铁匠铺 / 金工工坊', [('E18', '炉火、锻打与淬火'), ('E19', '煤与焦炭的烟色、白瓷片熏'), ('E17', '熔铜或铸造（如工坊能做）'), ('E62', '钢的淬火与回火（如工坊能做）')], '一次预约拍完三集的外景；燃烧只由师傅操作。'),
 ('陶艺工作室 / 窑口', [('E16', '烧陶对照'), ('B16', '瓷与陶的烧成、吸水对比')], '问清窑温与烧成曲线，正好给 E21 的窑温数字做旁证。'),
 ('玻璃工坊（吹制或灯工）', [('E21', '挑料、吹制、退火')], '预约时说明只拍、不参与操作。'),
 ('学校实验室', [('E51', '老师用教学菌株和药敏纸片做抑菌圈，只拍结果')], '提前一周联系，培养需一两天。'),
 ('科技馆 / 学校物理实验室', [('E14', '老师操作感应起电机'), ('E10', '带安全阀的教学蒸汽机模型（可选）')], '戴心脏起搏器的人远离静电机。'),
 ('博物馆', [('B11', '编钟或铜钟实物'), ('B10', '汉代日光镜（如有展出）'), ('E18', '古代铁器')], '只拍允许拍照的展品；可用馆方开放授权图片。'),
 ('户外 / 水边', [('E15', '钻木、打火石生火'), ('E13', '打火石棒火星对比'), ('B4', '水排模型'), ('B5', '都江堰沙盘或实地'), ('E50', '四人接力传信号')], '明火在空地、备水；水边注意安全。'),
]
HELPERS = [('E50', '3–4 位帮手（接力传信号）'), ('E08', '1 位骑车人（骑行台发电）'), ('E48', '1 位家人（计时比赛）'), ('E49', '1 位家人当顾客')]

def build_shooting():
    # 采购：在 ≥3 集里出现的道具
    C = collections.defaultdict(set)
    per = {}
    for c, v in D.items():
        if c[0] == 'S': continue
        items = []
        for p in v['sp'].get('props') or []:
            name = p[0] if isinstance(p, (list, tuple)) else p
            items.append(name)
            for tok in re.split(r'[、，,/＋+]|或', re.sub(r'（[^）]*）|\([^)]*\)', '', name)):
                tok = tok.strip()
                if tok and len(tok) <= 10: C[tok].add(c)
        per[c] = items
    common = [(k, sorted(v, key=lambda x: (x[0], int(x[1:])))) for k, v in C.items() if len(v) >= 3]
    common.sort(key=lambda x: -len(x[1]))
    secs = []
    secs.append('<section><h2>第 0 步：现在就开工的长周期实验</h2><p class="lead">这些实验要等几天到一个月才能拍结果。<b>和其他集并行</b>：先开工，等它们长好时正好拍到那一季。勾选状态只保存在这台设备上。</p>'
                + ''.join(f'<label class="chk"><input type="checkbox" data-k="long-{c}"><span class="t"><b>{eplink(c)}</b> <span class="pill hot">{e(t)}</span><small>{e(w)}</small></span></label>' for c, t, w in LONG) + '</section>')
    # 试播
    secs.append('<section><h2>第 1 步：试播 3 集，先发再定方向</h2><p class="lead">按项目全书的原计划：<b>04 磁生电 → B1 指南鱼 → 01 摩擦起电</b>。三集道具都在家里，两天内能拍完。发布一周后看完播率、评论里问得最多的问题，再决定后面先拍 A 线还是 B 线、先拍哪一季。</p>'
                + table(['顺序', '集', '为什么先拍它', '外拍'], [['1', eplink('E04'), '钩子最强、拍摄本和旁白稿最完整', '无'], ['2', eplink('B1'), 'B 线试播；实验结果未知，本身就是悬念', '无（明火由成年人操作）'], ['3', eplink('E01'), '回到科技树的起点', '无']]) + '</section>')
    # 各季
    rows = []
    for lab, ids in SEASONS:
        cs = [code(x) for x in ids]
        out = sorted({vn for vn, lst, _ in VENUES for cc, _ in lst if cc in cs})
        lg = [c for c, _, _ in LONG if c in cs]
        rows.append([lab, ' '.join((f'<a href="../{folder(c)}/">{e(label(c))}</a>' if os.path.exists(f'{REPO}/{folder(c)}/index.html') else f'<span class="pill">{e(label(c))} 待做</span>') for c in cs), str(len([c for c in cs if c[0] != 'S'])),
                     '、'.join(out) or '—', '、'.join(label(c) for c in lg) or '—'])
    secs.append('<section><h2>第 2 步：按季拍，外景合并预约</h2><p class="lead">每集在家的实拍约 6 段，熟练后<b>半天一集</b>；有外景的再加一天。下表按播出顺序列出每季的外景和长周期实验，外景按地点合并到下一节。</p>'
                + table(['季', '播出顺序', '集数', '要外拍的地点', '长周期实验'], rows) + '</section>')
    vh = []
    for vn, lst, tip in VENUES:
        vh.append(f'<div class="card"><h3>{e(vn)}</h3>' + ''.join(f'<div>{eplink(c)}：{e(w)}</div>' for c, w in lst) + f'<p class="lead">{e(tip)}</p></div>')
    secs.append('<section><h2>外景合并：一个地点一次拍完</h2><div class="grid2">' + ''.join(vh) + '</div>'
                + '<h3>需要帮手的集</h3>' + ''.join(f'<div>{eplink(c)}：{e(w)}</div>' for c, w in HELPERS) + '</section>')
    # 采购
    secs.append('<section><h2>采购清单 · 通用工具箱</h2><p class="lead">在 3 集以上用到的道具，一次买齐（共 '
                + str(len(common)) + ' 项）。勾选表示已备好。</p>'
                + ''.join(f'<label class="chk"><input type="checkbox" data-k="buy-{e(k)}"><span class="t"><b>{e(k)}</b> <span class="pill">{len(v)} 集</span><small>{" ".join(label(c) for c in v)}</small></span></label>' for k, v in common) + '</section>')
    special = [('骑行台 + 自行车发电套件 + USB 功率计', 'E08'), ('压电点火器配件（五金店）、压电蜂鸣片', 'E13'), ('带 K 型热电偶的万用表', 'E12'), ('毫伏表或 200 mV 档万用表', 'E12'), ('台式三档电风扇（带防护罩）、小直流电机', 'E07'),
               ('减速齿轮箱、滑轮、厚泡沫垫', 'E09'), ('煤、焦炭、木炭各一小袋', 'E19'), ('硅胶垫、厨房温度计（测到 200 ℃）', 'E21'), ('纯银勺或银饰', 'B19'), ('第 01 集自制莱顿瓶（塑料杯 + 铝箔）', 'E14'),
               ('1 毫米显微镜玻璃珠', 'E53'), ('老花镜片（+2 度，单片）', 'E54'), ('蓝晒纸（太阳晒图纸）', 'E55'), ('圆形钕磁铁', 'E58'), ('硫酸铜、护目镜、0.01 克精度的秤', 'E59'), ('插座功率计、红外测温枪', 'E60'), ('钢发卡、尖嘴钳、护目镜', 'E62'), ('石膏粉、粗铁丝', 'E63'), ('3 个牌子的 M5 螺丝螺母、游标卡尺', 'E64'), ('C 形夹、两块平整木板', 'E65'), ('花盆四个、沙土、pH 试纸', 'E67'), ('能测到零下 20 度的温度计两支', 'E68'), ('透明软管、线香', 'E69'), ('玻璃瓶验电器材料、铝箔', 'E70'), ('硬纸条、细笔（纸条计算尺）', 'E71'), ('精确到 1 克的厨房秤', 'B30'), ('成品开片杯、玉米淀粉', 'B31'), ('明胶、毛笔、金属勺', 'B32'), ('真丝纱巾、0.1 克精度的秤', 'B33'), ('熟石灰、砖粉或浮石粉', 'B35'), ('细沙一袋、弹簧秤', 'B36'), ('量角器、吸管（象限仪）', 'B37'), ('打印纸齿轮、图钉', 'B38'), ('大马士革纹钢片（不开刃）', 'B39'), ('8 欧小喇叭两个、20 米导线', 'E72'), ('旧黑胶唱片', 'E73'), ('漆包线、大铁钉', 'E75'), ('调幅收音机、9 伏电池、锉刀', 'E76'), ('小太阳能板', 'E77'), ('打气筒、红外测温枪', 'E78'), ('弹簧秤、细绳', 'E79'), ('打印纸齿轮、图钉', 'E80'), ('面包板、按钮、双刀双掷开关、LED', 'E81'), ('琥珀或松香块、芥菜籽、漆杯', 'H1'), ('铁勺、天然磁石（可选）', 'H2'), ('木槌、纱网框', 'H3'), ('仿古铜钱或铜垫片 ×10、铁垫片 ×10', 'H4'), ('标注含铅的水晶挂坠或镇纸', 'H5'), ('冰棍棒、竹签', 'B40'), ('竹签、棉线、薄塑料袋', 'B41'), ('轻黏土、手机调音器 App', 'B42'), ('螺母、木尺', 'B43'), ('泡沫板、图钉', 'B44'), ('靛蓝扎染套装、白棉方巾', 'B45'), ('PVC 管段、过筛园土', 'B46'), ('积木或小木块、托盘', 'B47'), ('黄瓜、土豆（实验用、不食用）', 'B48'), ('电子温湿度计 ×3、玻璃罐 ×3', 'B49'), ('方格纸（16×16、32×32）', 'E82'), ('钢锯条、钕磁铁、小指南针', 'E83'), ('两块木板、手机录音 App', 'E84'), ('锗二极管、高阻耳机或压电耳机、漆包线', 'E85'), ('A4 卡纸、厨房秤（读到 1 克）', 'E86'), ('木条 ×2、小纸盒、冰棍棒、橡皮筋', 'E87'), ('气球、粗细吸管、5 米细绳', 'E88'), ('低功率激光笔（1 级或 2 级）', 'E89'), ('打印地图、圆规、绳子 ×3', 'E90'), ('卡片 ×6、方格纸', 'E91'), ('硬纸板、铅笔、硬币', 'B50'), ('乒乓球（或蛋壳）、橡皮泥', 'B51'), ('细绳、吸管、螺母', 'B52'), ('竹筷、黄豆（不食用）', 'B53'), ('小算盘（上一下四）', 'B54'), ('九连环玩具', 'B55'), ('打孔器纸屑或米糠（米不食用）', 'B56'), ('三层竹蒸笼、探头式温度计 ×3', 'B57'), ('牛皮纸、蜡块、桐油（可选）', 'B58'), ('沙盘、弹簧秤、硬纸板模型犁', 'B59'), ('NPN 晶体管（S8050 等）、LED、电阻', 'E92'), ('整板巧克力（不食用）', 'E93'), ('低功率激光笔（1 级或 2 级）、硬纸框', 'E94'), ('小太阳能板、纸筒、红绿蓝玻璃纸', 'E95'), ('锡纸、手套、香肠（不食用）', 'E96'), ('打印的 L 级与 H 级二维码、便签', 'E97'), ('编号卡片、几位帮手', 'E98'), ('铜管、铝管、塑料管、圆柱钕磁铁', 'E99'), ('A4 纸、回形针、手持小风扇', 'E100'), ('网球、旧袜子、绳子、笔杆、垫圈', 'E101'), ('16 厘米见方的硬纸板、厨房秤', 'B60'), ('棉线、彩色粉笔、大螺母', 'B61'), ('结实的棉绳、量角器', 'B62'), ('卡纸、竹签、指南针', 'B63'), ('LED 手电、描图纸、硬纸板', 'B64'), ('纸盒、钓鱼线、手机调音 App', 'B65'), ('大号长柄伞 ×2、分贝 App', 'B66'), ('硬纸板坡道、弹珠 ×2', 'B67'), ('生麦芽、医用碘伏、保温壶（米汤不食用）', 'B68'), ('白糖、耐热玻璃杯 ×2、棉线、泡沫箱', 'B69'), ('红绿蓝 LED、5 号电池 ×2、电池盒', 'E102'), ('漆包线、耳机转接线、8 欧小喇叭', 'E103'), ('去针头针筒、超轻黏土', 'E104'), ('手机频谱 App', 'E105'), ('两部手机、音调 App、小喇叭、纸盒', 'E106'), ('旧玩具车电机、LED、50 克重物', 'E107'), ('传感器 App、厚袜子、结实的绳子、软垫', 'E108'), ('粗橡皮筋、测温枪、打气筒', 'E109'), ('透明胶片、放大镜、蓝晒纸', 'E110'), ('空火柴盒 ×24、彩色珠子或干豆子、3×3 棋盘', 'E111'), ('脱脂棉、筷子、瓶盖、硬币', 'B70'), ('干蚕茧、温度计、纸筒', 'B71'), ('蓝黄彩色卡纸、打孔器', 'B72'), ('彩色卡纸、吸管、扭扭棒', 'B73'), ('塑料盒 ×2、水盆、硬币、厨房秤', 'B74'), ('2 米透明软管、食用色素、瓶盖', 'B75'), ('大塑料盖 ×2、小米（可选小石磨）', 'B76'), ('薄纸、蜡笔、橡皮、纱布、棉花、墨汁', 'B77'), ('毛笔、牙签、墨汁、厨房秤', 'B78'), ('小皮球、打气筒和气针、卷尺', 'B79'), ('铁皮饼干盒、锡纸、第二部手机', 'E112'), ('软铅笔、透明胶带、放大镜', 'E113'), ('手机心率 App', 'E114'), ('扫帚、30 厘米尺子', 'E115'), ('细盐、胡椒粉、气球', 'E116'), ('6B 铅笔、3 伏纽扣电池、LED、鳄鱼夹导线', 'E117'), ('两个放大镜（立体镜）', 'E118'), ('两把带钥匙的小挂锁、带搭扣的小盒子', 'E119'), ('多米诺骨牌一盒（约 100 块）', 'E120'), ('电视遥控器、格子纸', 'E121'), ('卫生纸筒、冰棍棒、图钉', 'B80'), ('擀面杖、弹簧秤、细绳', 'B81'), ('冰棍棒、空塑料瓶 ×5、水盆', 'B82'), ('温度计 ×2、小玻璃罐、园土', 'B83'), ('粗橡皮筋、脱脂棉', 'B84'), ('线香、细沙、陶瓷碗', 'B85'), ('弹簧秤、细铁丝、平底盘', 'B86'), ('纸杯 ×4、粗吸管、细绳', 'B87'), ('金属垫圈、彩纸条、羽毛球', 'B88'), ('橡皮泥、塑料高筒', 'B89'), ('透明塑料盒 ×3、软管、晾衣夹', 'E122'), ('鞋盒、小药瓶、细沙、长纸条', 'E123'), ('玻璃罐、气球、吸管', 'E124'), ('大碗、保鲜膜、黑卡纸', 'E125'), ('细沙、透明塑料盒', 'E126'), ('50 厘米钢尺、M8 螺母、细线', 'E127'), ('卡纸、弹簧秤、空火柴盒', 'E128'), ('3–6 伏小直流电机、红色 LED、软管', 'E129'), ('冰棍棒、热熔胶、切菜板', 'E130'), ('乒乓球、牙签', 'E131'), ('50 厘米尺子、橡皮泥、厨房秤', 'B90'), ('A4 卡纸、细绳、绿豆', 'B91'), ('绿豆、透明小盒 ×3、小喷壶', 'B92'), ('冰棍棒、塑料瓶盖、牙签', 'B93'), ('1.5 升塑料瓶 ×2、黄豆', 'B94'), ('卷尺、美纹胶带、方格纸', 'B95'), ('500 毫升塑料瓶 ×4、干细沙', 'B96'), ('硬纸盘、量角器、细线', 'B97'), ('红色手工纸、圆头剪刀、小镜子', 'B98'), ('六根木制鲁班锁、编号小贴纸', 'B99'), ('小漏斗 ×2、1 米软管、气球', 'E132'), ('长气球、电子血压计（可选）', 'E133'), ('圆形玻璃花瓶、白卡纸', 'E134'), ('LED 手电筒、铝箔、透明塑料片', 'E135'), ('湿毛巾、纸杯 ×2', 'E136'), ('粗吸管 ×8、橡皮泥', 'E137'), ('手机节拍器 App', 'E138'), ('指南针 ×4、小钕磁铁', 'E139'), ('草莓、咖啡滤纸、75% 医用酒精', 'E140'), ('鞋盒、长筷子 ×2、黄豆', 'E141'), ('30 厘米塑料尺、弹簧秤、小水瓶 ×4', 'B100'), ('长尾夹、1 元硬币若干', 'B101'), ('白色蜡笔、小喷壶', 'B102'), ('长筷子 ×15', 'B103'), ('泡沫板、冰棍棒、图钉', 'B104'), ('小手持风扇、竹签', 'B105'), ('硬卡纸、厨房量杯', 'B106'), ('鞋盒、粗橡皮筋', 'B107'), ('大号气球 ×3、细盐', 'B108'), ('泡沫餐盘 ×3、水彩颜料', 'B109'), ('全脂牛奶、白醋、纱布', 'E142'), ('粗橡皮筋、吹风机', 'E143'), ('普通铁钉 ×5、透明杯 ×6', 'E144'), ('厨房铝箔、1 元硬币', 'E145'), ('魔术贴、弹簧秤', 'E146'), ('保温杯、厨房探针温度计', 'E147'), ('滴管、白色蜡笔', 'E148'), ('新纸尿裤一片、大塑料袋', 'E149'), ('A4 纸、胶棒', 'E150'), ('气泡膜、快递泡沫', 'E151'), ('木质冰棍棒 ×30、橡皮筋', 'B110'), ('擀面杖、棉绳', 'B111'), ('橡胶垫、纸箱', 'B112'), ('卡纸、筷子、木板', 'B113'), ('透明瓶、黄豆、大米', 'B114'), ('懒人转盘、橡皮泥', 'B115'), ('冰棍棒、两脚钉、细线', 'B116'), ('骰子 ×2、1 角硬币', 'B117'), ('2B 铅笔、透明胶带', 'B118'), ('食用油、刷子、白纸', 'B119'), ('拉链、弹簧秤', 'E152'), ('红蓝粗毛线、钝头毛线针', 'E153'), ('沙拉甩干器、厨房秤', 'E154'), ('大号塑料注射器（无针头）', 'E155'), ('厨房温度计、口香糖锡纸', 'E156'), ('小钕磁铁、铝管、铜管', 'E157'), ('普通吸管、直尺', 'E158'), ('全脂牛奶、滴管、手电筒', 'E159'), ('30 厘米塑料尺、一元硬币 20 枚', 'E160'), ('方格纸、骰子、小棋子', 'E161'), ('绣花绷子（约 20 厘米）', 'B120'), ('粗毛线', 'B121'), ('硬卡纸', 'B122'), ('纸杯、木珠或纽扣', 'B123'), ('粗吸管、调音 App', 'B124'), ('不锈钢吸管', 'B125'), ('A4 纸、一元硬币', 'B126'), ('小木块、筷子、橡皮泥', 'B127'), ('粗吸管、卫生纸卷筒', 'B128'), ('大橡皮、印台', 'B129'), ('玩具车、秒表', 'E162'), ('2 升塑料瓶、软管', 'E163'), ('插座功率计', 'E164'), ('电视遥控器', 'E165'), ('计算器', 'E166'), ('铝箔', 'E167'), ('测光 App（免费）', 'E168'), ('小磁铁、铁垫片、铝垫片', 'E169'), ('PVC 管、细沙', 'E170'), ('彩笔、A4 纸', 'E171'), ('1 米木棍、细线、螺母', 'B130'), ('竹杯垫、厨房温度计', 'B131'), ('500 毫升塑料瓶、温度计', 'B132'), ('厨房秤、旧毛巾', 'B133'), ('圆头牙签', 'B134'), ('粗毛线', 'B135'), ('儿童圆头剪刀', 'B136'), ('硬卡纸、喷壶', 'B137'), ('卡纸、图钉', 'B138'), ('拉链密封袋、橡皮筋', 'B139'), ('5 毫升和 20 毫升注射器（无针头）、软管', 'E172'), ('弹珠、小纸盒', 'E173'), ('橡皮泥、大号塑料袋', 'E174'), ('彩色胶带、粉笔', 'E175'), ('开口销（双脚钉）、硬纸板', 'E176'), ('带护罩的手持小风扇', 'E177'), ('透明塑料瓶、笔帽', 'E178'), ('旧光盘、气球、运动水瓶拉嘴盖', 'E179'), ('薄塑料袋、细线、垫片', 'E180'), ('方格纸、玩具小车（或硬币）', 'E181'), ('透明软管 1 米、食用色素', 'B140'), ('1.5 米透明软管、量角器', 'B141'), ('鞋盒、卡纸', 'B142'), ('明信片厚卡纸', 'B143'), ('长条保鲜盒、小空瓶', 'B144'), ('陶土或黏性泥土', 'B145'), ('深花盆、带探头的电子温度计 ×3', 'B146'), ('长纸条、马克笔', 'B147'), ('胶棒、棉签', 'B148'), ('棉线、粗毛线、细吸管', 'B149')]
    secs.append('<section><h2>采购清单 · 单集专用</h2><p class="lead">只有一两集用到、或者较贵的东西，到那一季再买。</p>'
                + ''.join(f'<label class="chk"><input type="checkbox" data-k="sp-{e(k)}"><span class="t"><b>{e(k)}</b><small>{eplink(c)}</small></span></label>' for k, c in special) + '</section>')
    det = ''.join(f'<details><summary>{e(label(c))} {e(title(c))}</summary><div>{"；".join(e(x) for x in per[c])}</div><p><a href="../{folder(c)}/">打开拍摄本 →</a></p></details>'
                  for lab, ids in SEASONS for c in [code(x) for x in ids] if c in per)
    secs.append('<section><h2>逐集道具</h2><p class="lead">按播出顺序，每集拍摄本里的道具表原样汇总（04、B1 见各自拍摄本）。</p>' + det + '</section>')
    secs.append('<section><h2>安全底线（全系列通用）</h2><ul class="verify"><li>明火、高温、刀具、电源由成年人操作；孩子出镜时保持距离。</li><li>不自制任何密封加热的容器；高压蒸汽只用动画。</li><li>不在家培养细菌；发霉食物密封不开封，拍完连袋丢掉。</li><li>实验用的食物一律不吃。</li><li>健康类题材不给剂量和配方；用药遵医嘱。</li><li>煤、炭只在户外或工坊烧，绝不在室内。</li></ul></section>')
    page = shell('拍摄总排期', '从零造物 · 实拍阶段 · 拍摄总排期', '拍摄总排期与采购清单',
                 '77 个拍摄包按「先开工长周期实验 → 试播 3 集 → 按季拍、外景合并」排好；采购清单把 75 本拍摄本里的道具合并成一张表。',
                 [('长周期实验', f'{len(LONG)} 项'), ('外景地点', f'{len(VENUES)} 类'), ('通用道具', f'{len(common)} 项'), ('试播', '04 → B1 → 01')], '\n'.join(secs))
    write('shooting', page, 'shooting.html')
    return len(common)

# ================================================================ 发布素材
def shots_of(c):
    sh = D[c]['sh'][0]
    return sh
def build_publish():
    cards = []
    n = 0
    for lab, ids in SEASONS:
        cards.append(f'<section><h2>{e(lab)}</h2><div class="grid2">')
        for x in ids:
            c = code(x)
            if c in ('E04', 'B1'):
                r = ROWS[c]; ttl = r['title']; q = r['hook']; hook = r['hook']; concl = ''; thesis = ''
                safety = '明火和磁铁由成年人操作。' if c == 'B1' else '实验只用电池或磁铁，安全。'
                anim = ''
            elif c not in D:
                continue
            else:
                sp = D[c]['sp']; sh = shots_of(c); ttl = sp['title']
                q = dict(sp.get('facts') or []).get('暂定标题', '')
                hook = sh[0][4]
                qs = [s for s in sh if str(s[3]).startswith('问题卡')]
                anim = next((s[4] for s in sh if s[5] and not str(s[3]).startswith(('问题卡', '资料卡', '片头', '片尾', '结论卡'))), '')
                concl = next((s[4] for s in sh if str(s[3]).startswith('结论卡')), '')
                thesis = sp.get('thesis', '')
                safety = (sp.get('safety') or [''])[0]
            n += 1
            lineword = 'B 线 · 古法解密' if c[0] == 'B' else ('特辑' if c[0] == 'S' else ('特别篇 · 汉代版' if c[0] == 'H' else 'A 线 · 穿越造物'))
            num = label(c)
            vt = f'【从零造物 {num}】{q or ttl}'
            cover = f'{ttl}\n{(q or "")[:16]}'
            brief = (f'{q}\n\n' if q else '') + (thesis[:120] + ('……' if len(thesis) > 120 else '') if thesis else '') + \
                    (f'\n\n安全提示：{safety}' if safety else '') + f'\n\n#从零造物 #{lineword.split(" · ")[-1]} #科普 #{ttl.replace(" ", "")}'
            if c[0] == 'S':
                slice_ = '特辑不做竖屏切片；从本季各集切片里选播放最好的 3 条做合集。'
            else:
                parts = [f'0–5 秒 · 钩子：{hook}']
                if q: parts.append(f'5–10 秒 · 抛问题：{q}')
                if anim: parts.append(f'10–45 秒 · 原理动画：{anim}')
                if concl: parts.append(f'45–55 秒 · 结论：{concl}')
                parts.append('55–60 秒 · 结尾：完整实验和实测数据，看横屏长视频。')
                slice_ = '\n'.join(parts)
            cid = c.lower()
            cards.append(f'<div class="card"><div class="k">{e(lineword)} · {e(num)}</div><h3><a href="../{folder(c)}/">{e(ttl)}</a></h3>'
                         f'<div class="k">视频标题</div><pre id="t-{cid}">{e(vt)}</pre><button class="copy" data-t="t-{cid}">复制</button>'
                         f'<div class="k">封面文字（两行）</div><pre id="c-{cid}">{e(cover)}</pre>'
                         f'<div class="k">简介</div><pre id="b-{cid}">{e(brief)}</pre><button class="copy" data-t="b-{cid}">复制</button>'
                         f'<details><summary>竖屏切片脚本（约 60 秒）</summary><pre>{e(slice_)}</pre></details></div>')
        cards.append('</div></section>')
    rules = ('<section><h2>发布规则</h2><ul class="verify">'
             '<li><b>先发 3 集试播</b>（04、B1、01），一周后把完播率和评论截图发给 Claude 复盘，再定后面的顺序。</li>'
             '<li>标题用「问题」而不是「答案」：观众点进来是想知道为什么。</li>'
             '<li>封面只放两行字：上行是题目，下行是问题的前半句；画面用实验里最有冲击力的一帧。</li>'
             '<li>简介里的安全提示不能删；健康类（第四季、51 青霉素）保留「遵医嘱」字样。</li>'
             '<li>旁白里括号中的内容要按实测改写后再发；没实测的数字不发。</li>'
             '<li>标「拍摄前核对」的说法，没核对完之前用「据记载」「一般认为」这类措辞。</li></ul></section>')
    page = shell('发布素材', '从零造物 · 实拍阶段 · 发布素材', '发布素材',
                 '每集一张卡：视频标题、封面文字、简介和 60 秒竖屏切片脚本，都从拍摄本里的问题、钩子、动画旁白和结论自动整理，可直接复制再微调。',
                 [('卡片', f'{n} 张'), ('切片', '每集 1 条 · 约 60 秒'), ('顺序', '按各季播出计划'), ('试播', '04 → B1 → 01')], rules + '\n'.join(cards))
    write('publish', page, 'publish.html')
    return n

# ================================================================ 待核清单
FIXED = [
 ('B18', '《后汉书·张衡传》「中有都柱，傍行八道，施关发机」「后数日驿至，果地震陇西」', '已对照维基文库《后汉书》卷五十九，字句一致；资料卡去掉「待核」重新渲染。', '维基文库'),
 ('B19', '《洗冤集录》银钗验毒原文', '与澎湃新闻等转引一致；所在卷次仍以原书为准。', '澎湃新闻'),
 ('E31', '《柳叶刀》1978 年对口服补液的评价', '补上原话：1978 年 8 月 5 日社论，「可能是本世纪最重要的医学进展」。', 'rehydrate.org'),
 ('E32', '洗手至少搓 20 秒', '美国 CDC 的建议，属实。', 'CDC'),
 ('E45', '摆钟让误差从每天约 15 分钟降到约 15 秒', '属实（1656 年惠更斯）。', 'historyofinformation.com'),
 ('B10', '透光镜年代', '改为西汉：「见日之光」日光镜，1979 年广西柳州汉墓出土；资料卡重新渲染。', '中新网 2023'),
 ('E36 / E19', '《鸡肋编》「汴都数百万家，尽仰石炭」', '原书未能取到全文核对，改用可查证的说法：11 世纪起开封人家主要烧煤，12 世纪初新设二十处煤场；资料卡重新渲染。', '维基百科「中国煤炭」'),
 ('E19', '中国炼焦的年代（原写「明末方以智」）', '更正：北宋 11 世纪北方已有用焦炭炼铁的明确记载，最早提到焦炭的文字在 4 世纪初；资料卡和旁白重新渲染。', '华道安《Historical Metallurgy》37:1、郝若贝'),
 ('E07', '波斯风车年代、布拉什风力发电机功率', '至迟 9 世纪、可能早到 7 世纪；布拉什的机器额定约 12 千瓦。中国风车年代说法不一，片中不提。', '维基百科「History of wind power」'),
 ('E08', '桓谭《新论》舂米从人力到畜力、水力', '与李约瑟译文一致；中文原句以辑本为准。', '维基百科「Trip hammer」'),
 ('E09', '重力灯数据', '约 9 千克、约 20 分钟（产品资料）。', '维基百科「GravityLight」'),
 ('E12', '铜—铁中性温度、K 型热电偶灵敏度', '冷端 0 ℃ 时中性温度约 270 ℃、反转约 540 ℃；K 型约 41 μV/℃。', '物理教材'),
 ('E13', '点火器电压', '改为由物理推出：空气约每毫米 3000 伏击穿，火花跳几毫米即至少几千伏。', '—'),
 ('E14', '格里克硫磺球起电机年代', '更正为 1660 年代（原写 1663 年）；资料卡和旁白重新渲染。', '美国国家强磁场实验室'),
 ('E10', '火电厂效率', '煤电平均约 37%–42%（美国约 37%、中国约 39%、日本约 42%），最先进约 48%；片中说「大约四成」。', '《POWER》杂志'),
 ('E21', '石英熔点、宋代窑温', '石英约 1700 ℃；宋代瓷窑实测多在约 1190–1310 ℃，个别达约 1450 ℃。', '皮尔金顿公司、Heritage Science 2019'),
 ('E51', '第一位病人、尿液回收、哈密瓜菌株', '属实：1941 年警察亚历山大，药不够时从尿中回收；1943 年玛丽·亨特找到发霉哈密瓜，产量约 200 倍。删去查不到出处的「多少升培养液治一位病人」，旁白重新渲染。', '美国科学史研究所、MedBound Times'),
]
OPEN = [  # (ep, 内容, 去哪核对, 优先级)
 ('B2', '苏轼《东坡志林》「自庆历、皇祐以来，蜀始创筒井……」原文', '维基文库《东坡志林》，搜索「筒井」（篇名「筒井用水鞴法」）', '高：片中会念出原文'),
 ('E43', '徐兢《宣和奉使高丽图经》「风有八面，唯当头不可行」及卷次', '维基文库该书卷三十四「客舟」条；宋史研究文章转引一致，卷次待确认', '高'),
 ('E17', '《梦溪笔谈》信州铅山苦泉熬胆矾、铁釜化铜', '维基文库《梦溪笔谈》，搜索「苦泉」（一般认为在卷二十五）', '高'),
 ('E20', '宋代用石莲验卤浓淡的出处', '一般引自宋人笔记，需找到具体书名再引用；找不到就说「宋代盐场有这样的做法」', '中'),
 ('E26', '杜佑《通典》竹筒相接、隔山引水的「渴乌」', '维基文库《通典》', '中'),
 ('E27', '《氾胜之书》「区种瓠法」瓦瓮蓄水', '辑本（如石声汉《氾胜之书今释》）', '中'),
 ('E30', '《齐民要术》插梨篇以棠、杜为砧木', '维基文库《齐民要术》卷四「插梨」', '中'),
 ('E39', '《墨经》关于「衡」（杠杆）平衡的原文', '维基文库《墨子》经下、经说下', '中'),
 ('B17', '《宋史》燕肃造指南车的卷次', '维基文库《宋史·舆服志》', '低'),
 ('E41', '汉代出土的青铜 / 铁齿轮具体实物', '博物馆或考古报告（片中可只说「汉代已有金属齿轮出土」）', '低'),
 ('E42', '胸带挽具在中国出现的年代', '李约瑟《中国科学技术史》；维基百科只说马颈圈最早可靠图像在 477–499 年敦煌壁画', '中'),
 ('E47', '一行天文大地测量的测点数和「一度」的里数', '《旧唐书·天文志》《唐会要》卷四十二；现代换算约 131 千米 / 度', '中'),
 ('B9', '铜鱼洗的起源年代', '博物馆藏品说明；片中只说「古代铜鱼洗」', '低'),
 ('B5', '都江堰灌区 1194.5 万亩与「深淘滩，低作堰」出处', '都江堰管理局公开资料', '低'),
]
def build_checklist():
    fixed = table(['集', '说法', '查证结果', '来源'], [[e(a), e(b), e(c), e(d)] for a, b, c, d in FIXED])
    def epl(x):
        return ' / '.join(f'<a href="../{folder(y.strip())}/">{e(y.strip())}</a>' if y.strip() in D or y.strip() in ROWS else e(y) for y in x.split('/'))
    op = ''.join(f'<label class="chk"><input type="checkbox" data-k="v-{i}"><span class="t"><b>{epl(a)} · {e(b)}</b> <span class="pill{" hot" if p.startswith("高") else ""}">{e(p)}</span><small>去哪核对：{e(w)}</small></span></label>' for i, (a, b, w, p) in enumerate(OPEN))
    body = ('<section><h2>这次已查证并改正（' + str(len(FIXED)) + ' 条）</h2><p class="lead">改动都已写回拍摄本；涉及资料卡或旁白的 6 集（E36、B10、B18、E14、E19、E51）重新渲染了资料卡和粗剪样片。</p>' + fixed + '</section>'
            + '<section><h2>还要对照原书的（' + str(len(OPEN)) + ' 条）</h2><p class="lead">多是古籍原文，网上取不到可靠全文。<b>拍到哪集，核对哪集</b>：标「高」的会在片中念出原文，拍之前一定对一遍。勾选状态只保存在这台设备上。</p>' + op + '</section>'
            + '<section><h2>核对的规矩</h2><ul class="verify"><li>古籍以维基文库或权威点校本为准，记下卷次。</li><li>数字至少找到一个可公开查到的来源，写进拍摄本的「资料来源」。</li><li>找不到出处的说法，片中改成「据记载」「一般认为」，或者干脆不说。</li><li>核对完把结果发给 Claude，会改拍摄本、重渲资料卡。</li></ul></section>')
    page = shell('待核清单', '从零造物 · 实拍阶段 · 待核清单', '待核清单',
                 '全系列拍摄本里标「拍摄前核对」的说法汇总在这里：能在网上查证的已经查完并改正，剩下的多是古籍原文，列出去哪核对。',
                 [('已查证', f'{len(FIXED)} 条'), ('待对照原书', f'{len(OPEN)} 条'), ('重渲资料卡', '6 集'), ('更正', 'E19 焦炭 · E14 年代 · B10 年代')], body)
    write('checklist', page, 'checklist.html')

if __name__ == '__main__':
    print('shooting common', build_shooting())
    print('publish cards', build_publish())
    build_checklist(); print('checklist ok')
