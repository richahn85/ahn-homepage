"""Digest deploy of the V3 changes to Netlify, preserving every other live file, functions and edge functions.

  python scripts/deploy_v3.py preview      # draft deploy, prints a preview URL
  python scripts/deploy_v3.py production   # publishes that exact draft deploy

Uses the Netlify CLI login stored in %APPDATA%/netlify/Config/config.json (same as earlier Codex deploys).
"""
from pathlib import Path
import hashlib, json, subprocess, sys, time, urllib.parse, urllib.request

ROOT = Path(__file__).resolve().parents[1]
SID = '0743687b-b75b-4236-80dc-be3791849339'
BASE_COMMIT = '989dee2'  # commit that mirrors the live deploy (6ad5478d, V3)
RECEIPT = ROOT / '.netlify' / 'v3-preview-deploy.json'
REPO_ONLY = ('scripts/', 'content/', '.gitignore', 'README.md', 'INITIAL_CONTENT.md', 'AUTHORITY_EDIT.md', 'V2_AUDIT.md', 'V2_DELIVERY.md')

cfg = json.loads((Path.home() / 'AppData/Roaming/netlify/Config/config.json').read_text(encoding='utf-8'))
auth = cfg['users'][cfg['userId']]['auth']
TOKEN = auth.get('token', auth.get('access_token')) if isinstance(auth, dict) else auth


def api(path, method='GET', data=None, raw=False):
    body = data if raw else (json.dumps(data).encode() if data is not None else None)
    req = urllib.request.Request('https://api.netlify.com/api/v1/' + path, data=body, method=method, headers={
        'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/octet-stream' if raw else 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        b = r.read()
    return json.loads(b) if b else None


def wait_ready(deploy_id):
    for _ in range(30):
        d = api('deploys/' + deploy_id)
        if d['state'] in ('ready', 'error'):
            return d
        time.sleep(2)
    return d


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


mode = sys.argv[1] if len(sys.argv) > 1 else ''
assert mode in ('preview', 'production'), __doc__
site = api('sites/' + SID)
pub = site['published_deploy']

if mode == 'preview':
    changed = subprocess.run(['git', 'diff', '--name-only', BASE_COMMIT, 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    changed = [p for p in changed if not p.startswith(REPO_ONLY) and (ROOT / p).is_file()]
    live = {f['path']: f['sha'] for f in api('sites/' + SID + '/files')}
    digest, uploads = dict(live), {}
    for rel in changed:
        data = (ROOT / rel).read_bytes()
        sha = hashlib.sha1(data).hexdigest()
        digest['/' + rel] = sha
        uploads[sha] = ('/' + rel, data)
    print(f'live deploy {pub["id"]}: {len(live)} files kept, {len(changed)} changed/new:')
    print('\n'.join('  ' + p for p in changed))
    payload = {'draft': True, 'files': digest, **fn_payload(pub)}
    d = api('sites/' + SID + '/deploys?title=' + urllib.parse.quote(sys.argv[2] if len(sys.argv) > 2 else 'V3 update'), 'POST', payload)
    assert not d.get('required_functions') and not d.get('required_edge_functions'), 'function bundles missing, stop'
    for sha in d.get('required', []):
        path, data = uploads[sha]
        api('deploys/' + d['id'] + '/files' + urllib.parse.quote(path), 'PUT', data, True)
    d = wait_ready(d['id'])
    assert d['state'] == 'ready', d['state']
    RECEIPT.parent.mkdir(exist_ok=True)
    RECEIPT.write_text(json.dumps({'id': d['id'], 'based_on': pub['id'], 'url': d['deploy_ssl_url']}), encoding='utf-8')
    print('preview ready:', d['deploy_ssl_url'])
else:
    r = json.loads(RECEIPT.read_text(encoding='utf-8'))
    assert pub['id'] == r['based_on'], f'live site changed since preview ({pub["id"]}), rebuild the preview'
    api('sites/' + SID + '/deploys/' + r['id'] + '/restore', 'POST', {})
    time.sleep(3)
    now = api('sites/' + SID)['published_deploy']
    assert now['id'] == r['id'], now['id']
    print('published:', r['id'], '-> https://ahnyoungchan.kr  (rollback target:', r['based_on'] + ')')
