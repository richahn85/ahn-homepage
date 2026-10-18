"""Validate static routes, migrated external links and Netlify form contracts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
R=Path(__file__).resolve().parents[1]
class Doc(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.ids=set();self.forms=[];self.fields=[];self.feed(s)
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.add(d['id'])
  if tag=='a' and 'href' in d:self.links.append(d['href'])
  if tag=='form':self.forms.append(d)
  if tag in ['input','select','textarea'] and 'name'in d:self.fields.append(d['name'])
def resolve(path):
 p=R/unquote(path.lstrip('/'))
 if p.is_file():return p
 if (p/'index.html').is_file():return p/'index.html'
 if p.with_suffix('.html').is_file():return p.with_suffix('.html')
 return None
routes=re.findall(r'<loc>https://ahnyoungchan.kr(.*?)</loc>',(R/'sitemap.xml').read_text())
errors=[];all_links=set()
for route in routes:
 p=resolve(route);doc=Doc(p.read_text(encoding='utf-8'));all_links.update(doc.links)
 for href in doc.links:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  path=u.path or route
  if path.startswith('/safety-cardnews-part'):continue # checked Netlify redirects
  target=resolve(path)
  if not target:errors.append(f'{route}: missing {href}')
  elif u.fragment and target.suffix=='.html' and u.fragment not in Doc(target.read_text(encoding='utf-8')).ids:errors.append(f'{route}: missing fragment {href}')
 for f in doc.forms:
  if f.get('method','').upper()!='POST' or f.get('action')!='/thank-you' or f.get('data-netlify')!='true' or f.get('netlify-honeypot')!='bot-field':errors.append(f'{route}: form contract')
baseline=json.loads((R/'content/legacy.json').read_text(encoding='utf-8'))
external={x for k,v in baseline.items() for x in Doc(v).links if x.startswith(('https://','mailto:'))}
intentional_removals=set()
errors += ['Lost external link: '+x for x in external-all_links-intentional_removals]
for name,route,fields in [('subscribe','/ax-management-brief',{'form-name','subject','bot-field','name','org','email','phone','plan'}),('contact','/contact',{'form-name','subject','bot-field','name','org','email','type','message'})]:
 doc=Doc(resolve(route).read_text(encoding='utf-8'))
 if not fields.issubset(doc.fields):errors.append(name+': missing fields')
home=resolve('/').read_text(encoding='utf-8')
assert len(re.findall(r'<section\b',home))==7
assert '110-297-224610' not in home and '30,000원' not in home
content=json.loads((R/'content/authority.json').read_text(encoding='utf-8'))
assert len(content['cases'])==2
assert 100<=len(content['signature']['summary'])<=180
for slug in content['draft_slugs']:
 route='/cases/'+slug
 assert route not in routes
 assert 'noindex,follow' in resolve(route).read_text(encoding='utf-8')
 assert (R/'content/drafts'/f'{slug}.html').exists()
 assert route not in {urlsplit(link).path.rstrip('/') for link in all_links}
for route in routes+['/cases/'+s for s in content['draft_slugs']]:
 source=resolve(route).read_text(encoding='utf-8')
 for forbidden in ['근거 확인 중','Evidence 준비 중','프로젝트 자료 확인 후 공개합니다','개별 증빙은 정리 중','국내 최초 7건','칼럼 원문을 정리 중','순차적으로 공개','원본 자료에서 확인되지','110-297-224610','계좌번호 복사','AX-01','AX-06']:
  if forbidden in source:errors.append(f'{route}: forbidden public text {forbidden}')
 if '리포트 구독' in source.split('<footer>')[-1] or '후원 안내' in source.split('<footer>')[-1]:errors.append(route+': commercial footer')
for route in ['/','/advisory','/executive-education']:
 source=resolve(route).read_text(encoding='utf-8')
 assert not re.search(r'\d[\d,]*원',source)
assert '미래융합' not in re.search(r'<section class="hero">.*?</section>',home,re.S).group()
print(json.dumps({'routes':len(routes),'original_external_links':len(external),'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
