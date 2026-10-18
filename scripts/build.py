"""Dependency-free static V2 builder. Run: python scripts/build.py."""
from pathlib import Path
import json, re, html

ROOT=Path(__file__).resolve().parents[1]
legacy=json.loads((ROOT/'content/legacy.json').read_text(encoding='utf-8'))
BASE='https://ahnyoungchan.kr'
NAV=[('ABOUT','/about'),('ADVISORY','/advisory'),('TRANSFORMATION','/ax-transformation'),('CASES','/cases'),('INSIGHTS','/insights'),('PEOPLE FIRST','/people-first')]
pages=[]
def a(label,url,primary=False):
    return f'<a class="btn {"btn-seal" if primary else "text-link"}" href="{url}">{label} <span aria-hidden="true">↗</span></a>'
def section(id,kicker,title,body,cls=''):
    return f'<section id="{id}" class="v2-section {cls}"><div class="wrap"><div class="sec-head"><p class="eyebrow">{kicker}</p><h2>{title}</h2></div>{body}</div></section>'
def old(key):
    s=legacy[key].replace('src="assets/','src="/assets/')
    for key2,url in {'subscribe':'/ax-management-brief#subscribe','services':'/advisory','expertise':'/ax-transformation#expertise','contact':'/contact','support':'/people-first#support','probono':'/people-first'}.items():
        s=s.replace(f'href="#{key2}"',f'href="{url}"')
    s=re.sub(r'<input type="(text|email|tel)" name="([^"]+)" placeholder="([^"]+)"([^>]*)>',lambda m:f'<label>{m[3]}<input type="{m[1]}" name="{m[2]}"{m[4]}></label>',s)
    s=s.replace('<select name="plan" required>','<label>구독 플랜 *<select name="plan" required>').replace('</select>','</select></label>') if key=='subscribe' else s
    s=s.replace('<h4>','<h3>').replace('</h4>','</h3>')
    s=s.replace("onclick=\"navigator.clipboard.writeText('110-297-224610').then(()=>{this.textContent='복사되었습니다';setTimeout(()=>this.textContent='계좌번호 복사',1800)})\"",'data-copy="110-297-224610"')
    s=s.replace("유형을 '사회공헌 무료 서비스'로", "유형을 'People First / Pro Bono'로")
    s=s.replace('아래 문의 폼에서','<a href="/contact">문의 폼</a>에서').replace("아래 '경영진 자문' 서비스와 결합해",'<a href="/advisory">경영진 자문 서비스</a>와 결합해')
    s=s.replace('alt="강의 중 마이크를 들고 설명하는 안영찬 교수" loading="lazy"','alt="강의 중 마이크를 들고 설명하는 안영찬 교수" width="1200" height="1200" loading="lazy"')
    s=s.replace('alt="안영찬 교수 흑백 프로필 사진" loading="lazy"','alt="안영찬 교수 흑백 프로필 사진" width="1462" height="2048" loading="lazy"')
    return s
def page(path,title,body,desc=None,schema=None,noindex=False):
    desc=desc or title+' — 30년 경영혁신 경험으로 AI 시대의 다음 경영을 설계합니다.'
    url=BASE+path
    data=[{'@context':'https://schema.org','@type':'WebSite','@id':BASE+'/#website','name':'AHN YOUNG CHAN','url':BASE},
          {'@context':'https://schema.org','@type':'Person','@id':BASE+'/#person','name':'안영찬','alternateName':'Ahn Young Chan','url':BASE+'/about','image':BASE+'/assets/ahn-portrait-20260919.jpg','jobTitle':'Management Transformation Advisor'}]
    if path!='/': data.append({'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE},{'@type':'ListItem','position':2,'name':title,'item':url}]})
    if schema: data.append({'@context':'https://schema.org',**schema})
    nav=''.join(f'<li><a href="{u}" {"aria-current=\"page\"" if path==u else ""}>{n}</a></li>' for n,u in NAV)
    out=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | 안영찬</title><meta name="description" content="{html.escape(desc,quote=True)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(desc,quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:locale" content="ko_KR"><meta property="og:image" content="{BASE}/assets/ahn-portrait-20260919.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="/assets/legacy.css"><link rel="stylesheet" href="/assets/v2.css?v=20260919-portrait"><script src="/assets/v2.js" defer></script><script type="application/ld+json">{json.dumps(data,ensure_ascii=False)}</script></head>
<body id="top"><a class="skip" href="#main">본문 바로가기</a><header><div class="wrap nav"><a class="brand" href="/">AHN YOUNG CHAN<span>THINKING INTO ACTION</span></a><button class="menu-btn" aria-expanded="false" aria-controls="navigation">메뉴</button><nav id="navigation" aria-label="주 메뉴"><ul class="nav-links">{nav}</ul></nav><a class="nav-cta" href="/contact">자문·협력 문의 <span aria-hidden="true">↗</span></a></div></header>
<main id="main">{body}</main><footer><div class="wrap footer-grid"><div><b>AHN YOUNG CHAN</b><p>Management Transformation · Since 1992</p></div><p>Technology Changes.<br>People Come First.</p><div><a href="/about">About</a> · <a href="/insights">Insights</a> · <a href="/contact">Contact</a><br><a href="mailto:richahn@dongguk.edu">richahn@dongguk.edu</a><br><a href="mailto:richahn85@gmail.com">richahn85@gmail.com</a></div></div><nav class="wrap official-channels" aria-label="공식 채널"><a href="/channels">공식 채널 모아보기</a><a href="https://blog.naver.com/smartwolf85">네이버 블로그 ↗</a><a href="https://www.instagram.com/neverstopwolf/">Instagram ↗</a><a href="https://www.linkedin.com/in/richard-ahn-0359332a/">LinkedIn ↗</a></nav><div class="wrap copyright">© 안영찬. All rights reserved.</div></footer></body></html>'''
    if schema and schema.get('@type')=='Article':
        out=out.replace('property="og:type" content="website"','property="og:type" content="article"')
        out=out.replace('</head>',f'<meta property="article:published_time" content="{schema["datePublished"]}"><meta property="article:modified_time" content="{schema["dateModified"]}"></head>')
    out=out.replace('</head>','<noscript><style>@media(max-width:1000px){.nav{height:auto;flex-wrap:wrap;padding-top:15px;padding-bottom:15px}.nav #navigation{display:block;position:static;width:100%;order:3}.nav-links{display:flex}.menu-btn{display:none}}</style></noscript></head>')
    dest=ROOT/'index.html' if path=='/' else ROOT/path.strip('/')/'index.html'
    if noindex: out=out.replace('</head>','<meta name="robots" content="noindex,follow"></head>')
    dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(out,encoding='utf-8')
    if not noindex: pages.append(path)
def intro(kicker,title,description):
    return f'<section class="page-intro"><div class="wrap"><a class="breadcrumb" href="/">HOME</a><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="lede">{description}</p></div></section>'

SERVICES=[('01','CEO ADVISORY','경영진의 다음 결정을 함께 설계합니다.','CEO·임원이 마주한 AX, 신사업, B2B 성장, 조직문화, 안전경영 의제를 함께 검토하고 의사결정을 지원합니다.','/advisory'),('02','AX TRANSFORMATION','AI를 넘어, 일하는 방식의 변화로.','업무진단 → AI 적용영역 선정 → Workflow 재설계 → Agent·자동화 → KPI까지 연결합니다.','/ax-transformation'),('03','EXECUTIVE EDUCATION','교육이 끝난 뒤의 변화를 설계합니다.','CEO·임원 특강, 조직 맞춤형 AI·경영 워크숍, 실행 프로젝트형 교육을 제공합니다.','/executive-education')]
def services():
    return '<div class="service-list">'+''.join(f'<article><span class="index">{n}</span><div><p class="eyebrow">{en}</p><h3>{t}</h3><p>{d}</p></div>{a(en+" 보기",u)}</article>' for n,en,t,d,u in SERVICES)+'</div>'
CASES=[('k-bpi','K-BPI 브랜드파워 지수','Brand & Customer','한국산업 브랜드 파워 지수(K-BPI) 모델 개발·런칭'),('hyundai-crm','현대백화점 CRM','Customer Management','CRM 개념 적용 현대백화점 프로젝트 PM'),('b2b-marketing','B2B Marketing','B2B Growth','B2B 마케팅 전략 교육과정 프로그램 런칭'),('smart-tourism','Smart Tourism','Public Innovation','스마트관광도시 발전방안 컨설팅(인천), 추진 가이드라인 매뉴얼(한국관광공사)'),('safety-management','Safety Management','Safety & Standardization','중대재해처벌법 대응·안전경영 프로그램 런칭'),('ai-transformation','AI Transformation','Management Transformation','기업·기관 AI 활용과 업무 프로세스 전환')]
def cases():
    return '<div class="cases-grid">'+''.join(f'<a class="case" href="/cases/{slug}"><span class="index">CASE {i+1:02}</span><p>{cat}</p><h3>{t}</h3><span class="case-arrow" aria-hidden="true">↗</span><p>{d}</p></a>' for i,(slug,t,cat,d) in enumerate(CASES))+'</div>'
QUESTIONS=['AI가 인간보다 더 좋은 의사결정을 한다면 CEO의 역할은 무엇인가?','생산성이 높아졌는데 사람이 더 불행해졌다면 그것을 혁신이라 부를 수 있는가?','직원에게 주인의식을 요구하기 전에 회사는 직원을 주인처럼 대하고 있는가?','우리는 왜 생산성을 진보의 가장 중요한 척도로 생각하는가?']
def questions():
    return '<div class="question-list">'+''.join(f'<div><span>Q{i+1:02}</span><h3>{q}</h3></div>' for i,q in enumerate(QUESTIONS))+'</div>'
def contact():
    types=[('경영진 정기 자문','CEO Advisory'),('AX 컨설팅 프로젝트','AX Transformation'),('특강·워크숍','Executive Education'),('Research & Public Project','Research & Public Project'),('Media / Interview','Media / Interview'),('사회공헌 무료 서비스 (사회적기업·소상공인·비영리)','People First / Pro Bono')]
    fields=''.join(f'<label>{label} *<input name="{name}" type="{typ}" autocomplete="{auto}" required></label>' for name,label,typ,auto in [('name','이름','text','name'),('org','소속','text','organization'),('email','이메일','email','email')])
    return f'''<div class="contact-layout"><div><p>고민의 출발점부터 함께 살펴보겠습니다.<br>조직의 상황과 희망 일정을 알려주세요.</p><a href="mailto:richahn@dongguk.edu">richahn@dongguk.edu</a><br><a href="mailto:richahn85@gmail.com">richahn85@gmail.com</a></div><form name="contact" method="POST" action="/thank-you" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="contact"><input type="hidden" name="subject" value="안영찬 홈페이지 문의"><p hidden><label>이 필드는 비워 두세요<input name="bot-field" tabindex="-1" autocomplete="off"></label></p><div class="form-fields">{fields}<label>문의 유형 *<select name="type" required><option value="">선택해주세요</option>{''.join(f'<option value="{v}">{l}</option>' for v,l in types)}</select></label></div><label>현재 가장 해결하고 싶은 경영 과제를 간단히 적어주세요. *<textarea name="message" rows="5" required></textarea></label><button class="form-btn" type="submit">상담 요청 보내기 ↗</button></form></div>'''

from authority import render
render(globals())
article_records=[]
for number,date,title,summary in [
    (5,'2026-07-31','서류 안전을 넘어 ⑤ — 안전 데이터 의무화와 공공기관 First Mover','전자세금계산서처럼 안전 데이터도 의무화해야 하는 이유와 공공기관의 표준화 역할을 10장 카드뉴스로 정리했습니다.'),
    (4,'2026-07-21','서류 안전을 넘어 ④ — 사고율 0건이 안전의 증거일까?','안전보건공시제 시대, 결과 숫자가 아니라 과정 데이터를 공개해야 하는 이유를 10장 카드뉴스로 정리했습니다.'),
    (3,'2026-07-09','서류 안전을 넘어 ③ — 감시카메라가 아니라 유능한 비서가 필요하다','위험성평가 의무화 시대, 안전관리의 디지털 전환을 10장 카드뉴스로 정리했습니다. 공유와 PNG 다운로드가 가능합니다.')]:
    route=f'/insights/safety-part-{number}'
    source=f'/safety-cardnews-part{number}-{date.replace("-","")}/'
    record={'title':title,'datePublished':date,'dateModified':'2026-09-06','author':'안영찬','category':'Card News','topics':['Safety','Standardization'],'summary':[summary,'10장 카드뉴스로 구성된 안전경영 콘텐츠입니다.','원문 보기와 PNG 다운로드를 제공합니다.'],'body':summary,'source':source,'canonical':BASE+route}
    article_records.append(record)
    body=intro('CARD NEWS · SAFETY',title,f'<time datetime="{date}">{date}</time> · 안영찬')+section('summary','AT A GLANCE','세 줄 요약','<ul>'+''.join(f'<li>{line}</li>' for line in record['summary'])+'</ul>')+section('article','ARTICLE','서류 안전을 넘어',f'<p>{summary}</p>'+a('카드뉴스 원문 보기',source,True)+a('PNG 묶음 다운로드',f'https://safety-cardnews-part{number}-{date.replace("-","")}.netlify.app/assets/cardnews_part{number}_png.zip'))+section('related','CONTINUE','관련 콘텐츠와 다음 질문',a('전체 Insights','/insights')+a('조직의 과제 문의','/contact'))
    page(route,title,body,summary,{'@type':'Article','headline':title,'description':summary,'author':{'@type':'Person','name':'안영찬','@id':BASE+'/#person'},'datePublished':date,'dateModified':'2026-09-06','mainEntityOfPage':BASE+route,'image':BASE+'/assets/ahn-portrait-20260919.jpg','articleSection':'Safety'})
(ROOT/'content/articles.json').write_text(json.dumps(article_records,ensure_ascii=False,indent=2),encoding='utf-8')
insights=ROOT/'insights/index.html'
s=insights.read_text(encoding='utf-8')
for r in article_records:s=s.replace(f'href="{r["source"]}">카드뉴스 보기',f'href="{r["canonical"].removeprefix(BASE)}">카드뉴스 보기')
insights.write_text(s,encoding='utf-8')
from downloads import render as render_downloads
render_downloads(globals())
from channels import render as render_channels
render_channels(globals())
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE+p}</loc></url>' for p in pages)+'</urlset>',encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n',encoding='utf-8')
print(f'Built {len(pages)} static pages.')
