"""Digest deploy of AYC Working Paper 2026-01 on top of the CURRENT live site.

  python scripts/deploy_wp_2026_01.py preview      # draft deploy, prints a preview URL
  python scripts/deploy_wp_2026_01.py production   # publishes that exact draft

Unlike deploy_v3.py it does not diff against a base commit. It downloads the live
versions of the pages it touches (home, insights, research, sitemap, materials.json),
inserts the Working Paper links only if they are missing, and uploads just those
files plus the new page and the three downloads. Every other live file, function
and edge function is kept. Uses the same Netlify CLI login as deploy_v3.py.
"""
from pathlib import Path
import hashlib, json, sys, time, urllib.parse, urllib.request

ROOT = Path(__file__).resolve().parents[1]
SID = '0743687b-b75b-4236-80dc-be3791849339'
LIVE = 'https://ahnyoungchan.kr'
RECEIPT = ROOT / '.netlify' / 'wp-2026-01-preview.json'
ROUTE = '/insights/wp-2026-01'

cfg = json.loads((Path.home() / 'AppData/Roaming/netlify/Config/config.json').read_text(encoding='utf-8'))
auth = cfg['users'][cfg['userId']]['auth']
TOKEN = auth.get('token', auth.get('access_token')) if isinstance(auth, dict) else auth


def api(path, method='GET', data=None, raw=False):
    body = data if raw else (json.dumps(data).encode() if data is not None else None)
    req = urllib.request.Request('https://api.netlify.com/api/v1/' + path, data=body, method=method, headers={
        'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/octet-stream' if raw else 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r:
        b = r.read()
    return json.loads(b) if b else None


def live(path):
    req = urllib.request.Request(LIVE + path + ('&' if '?' in path else '?') + 'nocache=' + str(time.time()), headers={'User-Agent': 'deploy-script'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf-8')


def sec(id, eb, h, body):
    return f'<section id="{id}" class="v2-section "><div class="wrap"><div class="sec-head"><p class="eyebrow">{eb}</p><h2>{h}</h2></div>{body}</div></section>'


def fn_payload(pub):
    fns = pub.get('available_functions') or []
    conf = {}
    for f in fns:
        c = {'build_data': f['bd'], 'priority': f['p']}
        if f.get('ro'):
            c['routes'] = [{'pattern': r['p'], 'literal': r['l'], 'prefer_static': r['ps']} for r in f['ro']]
        if f.get('tr'):
            c['traffic_rules'] = f['tr']
        conf[f['n']] = c
    return {'functions': {f['n']: f['d'] for f in fns}, 'functions_config': conf, 'function_schedules': pub.get('function_schedules') or []}


def build_files():
    out = {}
    link = '<p class="monthly-link" id="working-paper-2026-01"><a href="/insights/wp-2026-01/"><span>Working Paper</span> 아이 앞에는 사람을, 교사 뒤에는 AI를 · AI 시대 영유아교육 →</a></p>'
    marker = '<p class="monthly-link" id="lecture-downloads">'
    for path, rel in (('/', 'index.html'), ('/insights/', 'insights/index.html')):
        t = live(path)
        if 'working-paper-2026-01' not in t:
            assert t.count(marker) == 1, f'marker not found in live {path}'
            t = t.replace(marker, link + marker, 1)
        out['/' + rel] = t.encode('utf-8')
    t = live('/research/')
    m = '<section id="reports" class="v2-section ">'
    if 'id="working-papers"' not in t:
        assert t.count(m) == 1, 'reports section not found in live /research/'
        t = t.replace(m, sec('working-papers', 'WORKING PAPERS', 'Working Paper', '<dl class="report-list"><dt>2026-01</dt><dd><a href="/insights/wp-2026-01/">아이 앞에는 사람을, 교사 뒤에는 AI를: AI 시대 영유아교육기관의 Human First 전환 모델</a></dd></dl>') + m, 1)
    out['/research/index.html'] = t.encode('utf-8')
    t = live('/sitemap.xml')
    if 'wp-2026-01' not in t:
        t = t.replace('</urlset>', '<url><loc>https://ahnyoungchan.kr/insights/wp-2026-01</loc><lastmod>2026-11-05</lastmod></url></urlset>', 1)
    out['/sitemap.xml'] = t.encode('utf-8')
    mats = json.loads(live('/download/materials.json'))
    title = 'AYC Working Paper 2026-01 · 아이 앞에는 사람을, 교사 뒤에는 AI를'
    for ext, label in (('pdf', 'PDF'), ('hwpx', 'HWPX'), ('docx', 'DOCX')):
        mats[f'/downloads/wp-2026-01/ayc-wp-2026-01.{ext}'] = {'title': f'{title} ({label})', 'filename': f'AYC-WP-2026-01_AI시대_영유아교육_HumanFirst.{ext}'}
        out[f'/downloads/wp-2026-01/ayc-wp-2026-01.{ext}'] = (ROOT / f'downloads/wp-2026-01/ayc-wp-2026-01.{ext}').read_bytes()
    out['/download/materials.json'] = json.dumps(mats, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    # New page: header/footer taken from the live download page so navigation matches the live site.
    repo_page = (ROOT / 'insights/wp-2026-01/index.html').read_text(encoding='utf-8')
    tpl = live('/downloads/samsung-apple/')
    live_head = tpl.split('<main id="main">', 1)[0]
    live_footer = tpl.split('</main>', 1)[1]
    repo_head = repo_page.split('<main id="main">', 1)[0]
    main = '<main id="main">' + repo_page.split('<main id="main">', 1)[1].split('</main>', 1)[0] + '</main>'
    # keep the repo page's <head> (title, meta, JSON-LD) but the live site's <body> header
    body_header = live_head.split('<body', 1)[1]
    out['/insights/wp-2026-01/index.html'] = (repo_head.split('<body', 1)[0] + '<body' + body_header + main + live_footer).encode('utf-8')
    return out


mode = sys.argv[1] if len(sys.argv) > 1 else ''
assert mode in ('preview', 'production'), __doc__
site = api('sites/' + SID)
pub = site['published_deploy']

if mode == 'preview':
    files = build_files()
    current = {f['path']: f['sha'] for f in api('sites/' + SID + '/files')}
    digest, uploads = dict(current), {}
    for path, data in files.items():
        sha = hashlib.sha1(data).hexdigest()
        digest[path] = sha
        uploads[sha] = (path, data)
    print(f'live deploy {pub["id"]}: {len(current)} files kept, {len(files)} changed/new:')
    print('\n'.join('  ' + p for p in files))
    payload = {'draft': True, 'files': digest, **fn_payload(pub)}
    d = api('sites/' + SID + '/deploys?title=' + urllib.parse.quote('WP 2026-01 Working Paper'), 'POST', payload)
    assert not d.get('required_functions') and not d.get('required_edge_functions'), 'function bundles missing, stop'
    for sha in d.get('required', []):
        path, data = uploads[sha]
        api('deploys/' + d['id'] + '/files' + urllib.parse.quote(path), 'PUT', data, True)
    for _ in range(30):
        d = api('deploys/' + d['id'])
        if d['state'] in ('ready', 'error'):
            break
        time.sleep(2)
    assert d['state'] == 'ready', d['state']
    RECEIPT.parent.mkdir(exist_ok=True)
    RECEIPT.write_text(json.dumps({'id': d['id'], 'based_on': pub['id'], 'url': d['deploy_ssl_url']}), encoding='utf-8')
    print('preview ready:', d['deploy_ssl_url'] + ROUTE)
else:
    r = json.loads(RECEIPT.read_text(encoding='utf-8'))
    assert pub['id'] == r['based_on'], f'live site changed since preview ({pub["id"]}), run preview again'
    api('sites/' + SID + '/deploys/' + r['id'] + '/restore', 'POST', {})
    time.sleep(3)
    now = api('sites/' + SID)['published_deploy']
    assert now['id'] == r['id'], now['id']
    print('published:', r['id'], '->', LIVE + ROUTE, '(rollback target:', r['based_on'] + ')')
