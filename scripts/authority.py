"""Authority edit: compose fewer public sections using the existing page language."""
import json,re

def render(ctx):
    ROOT=ctx['ROOT']; page=ctx['page']; section=ctx['section']; intro=ctx['intro']; a=ctx['a']; old=ctx['old']; services=ctx['services']; contact=ctx['contact']
    content=json.loads((ROOT/'content/authority.json').read_text(encoding='utf-8'))
    records=content['cases']; signature=content['signature']
    def selected():
        return '<div class="cases-grid selected-pair">'+''.join(f'<a class="case" href="/cases/{r["slug"]}"><p class="eyebrow">{r["category"]}</p><h3>{r["title"]}</h3><p>{r["description"]}</p><p class="case-role">{r["role"]}</p><span class="text-link">프로젝트 읽기 ↗</span></a>' for r in records)+'</div>'
    orgs='<div class="selected-organizations"><p class="eyebrow">SELECTED ORGANIZATIONS</p><ul>'+''.join(f'<li>{n}</li>' for n in content['organizations'])+'</ul></div>'
    credentials='<div class="proof-strip authority-proof"><div><b>SINCE 1992</b><p>경영혁신·컨설팅·교육</p></div><div><b>PROFESSOR</b><p>동국대학교 경영대학원</p></div><div><b>INTERNATIONAL<br>STANDARDS</b><p>국가기술표준원 선정 국제표준 전문가</p></div></div>'
    timeline='<ol class="evolution compact-evolution">'+''.join(f'<li>{t}</li>' for t in ['1992<br>Research & Consulting','CRM & Customer Management','B2B & Management Innovation','Smart Industry & Standardization','AI Transformation'])+'</ol>'
    philosophy='<p class="people-copy">기술은 더 빠르게 발전하겠지만 경영의 목적은 결국 사람에게 돌아와야 합니다. AI Transformation도 사람이 더 의미 있는 일을 하고, 기업이 더 나은 가치를 만들도록 돕는 방향이어야 합니다.</p>'
    def signature_preview():
        return f'<div class="signature-copy"><p class="eyebrow">PROFESSOR’S QUESTION</p><h3 class="big-question">{signature["title"]}</h3><p>{signature["summary"]}</p>{a("생각 이어서 읽기","/professors-question")}</div>'
    brief_link='<p class="monthly-link"><a href="/ax-management-brief"><span>Monthly Brief</span> 경영진이 한 달에 한 번 생각해야 할 질문 →</a></p>'
    hero='''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">MANAGEMENT TRANSFORMATION · SINCE 1992</p><h1>경영 패러다임이<br>바뀔 때마다,<br><span>현장에 먼저 답을<br>만들어 왔습니다.</span></h1><p class="lede">30년 이상의 경영혁신 경험으로<br><strong>AI를 ‘도구’에서 ‘경영성과’로 바꿉니다.</strong></p><p class="hero-identity"><b>안영찬</b><br>Management Transformation Advisor</p><p class="hero-authority">동국대학교 경영대학원 교수<br>국가기술표준원 선정 국제표준 전문가</p><div class="cta-row">'''+a('자문·협력 문의','/contact',True)+a('대표 프로젝트','/cases')+'''</div></div><figure class="hero-photo"><img src="/assets/ahn-portrait-20260919.jpg" alt="안영찬 교수 흑백 프로필 사진" width="1462" height="2048" fetchpriority="high"></figure></div></section>'''
    home=hero+section('proof','02 / AUTHORITY','경영의 변화를 현장에서 이어왔습니다.',credentials+orgs)+section('services','03 / WHAT I DO','경영진의 판단에서 조직의 실행까지',services())+section('cases','04 / SELECTED WORK','경력보다 중요한 것은<br>어떤 문제를 풀어왔는가입니다.',selected())+section('thinking','05 / SIGNATURE THINKING','답보다 먼저,<br>좋은 질문을 던집니다.',signature_preview()+a('Insights','/insights')+brief_link)+section('career','06 / ABOUT & PHILOSOPHY','Technology Changes.<br>People Come First.',philosophy+timeline+a('About','/about')+a('People First','/people-first'),'navy-section')+section('contact','07 / CONTACT','지금 조직이 풀어야 할<br>가장 중요한 질문은 무엇입니까?',contact())
    page('/','Management Transformation Advisor',home)
    # Keep each service focused on one decision and avoid repeated catalogues.
    advisory=intro('CEO ADVISORY','경영진의 다음 결정을 함께 설계합니다.','중요한 경영 의제를 함께 검토하고, 판단의 기준과 실행 방향을 구체화합니다.')
    advisory+=section('when','WHEN TO CALL','어떤 상황에서 자문이 필요한가','<div class="editorial-list"><p>AI 도입의 우선순위와 조직의 변화 방향을 결정해야 할 때.</p><p>신사업과 성장 대안을 검토하며, 무엇에 집중할지 판단해야 할 때.</p><p>조직·사람·안전의 과제를 경영진의 의사결정으로 연결해야 할 때.</p></div>')
    advisory+=section('discussion','DISCUSSION AREAS','경영진이 마주한 핵심 의제','<p class="discussion-line">AX · 신사업·성장 · B2B · 조직·사람 · 안전·Governance</p>')
    advisory+=section('process','HOW WE WORK','질문에서 결정으로','<ol class="work-process">'+''.join(f'<li>{x}</li>' for x in ['경영진 미팅','이슈 진단','대안 검토','의사결정 지원','필요시 실행 Follow-up'])+'</ol><p>과제의 범위와 기간에 따라 협의합니다.</p>')
    advisory+=section('experience','SELECTED EXPERIENCE','판단을 뒷받침하는 현장 경험',selected())+section('inquiry','CONTACT','조직의 중요한 결정을 함께 살펴보겠습니다.',a('자문·협력 문의','/contact',True))
    page('/advisory','CEO Advisory',advisory,schema={'@type':'Service','name':'CEO Advisory','provider':{'@id':ctx['BASE']+'/#person'},'description':'경영진의 핵심 의제 검토와 의사결정 지원','url':ctx['BASE']+'/advisory'})
    capabilities=[('AI & WORK','AI Transformation · 업무자동화 · Agentic Workflow'),('GROWTH & MARKET','B2B Marketing · 신사업·신상품 · Customer Experience'),('ORGANIZATION','조직문화 · Change Management · TPS 기반 현장혁신'),('GOVERNANCE & PUBLIC','Safety Management · Standardization · Public Innovation')]
    ax=intro('AX TRANSFORMATION','AI를 넘어, 일하는 방식의 변화로.','AI는 경영의 목적을 실현하는 도구입니다. 고객과 시장, 조직과 운영에 대한 이해를 바탕으로 변화의 우선순위를 설계합니다.')
    ax+=section('expertise','MANAGEMENT CAPABILITIES','경영을 이해하고, 변화를 설계합니다.','<div class="capability-grid">'+''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in capabilities)+'</div>')
    ax+=section('process','FROM STRATEGY TO WORK','업무와 성과를 함께 바꿉니다.','<p>업무진단 → AI 적용영역 선정 → Workflow 재설계 → Agent·자동화 → KPI</p>')+section('inquiry','CONTACT','지금 바꿔야 할 일하는 방식은 무엇입니까?',a('자문·협력 문의','/contact',True))
    page('/ax-transformation','AX Transformation',ax,schema={'@type':'Service','name':'AX Transformation','provider':{'@id':ctx['BASE']+'/#person'},'url':ctx['BASE']+'/ax-transformation'})
    education=intro('EXECUTIVE EDUCATION','교육이 끝난 뒤의 변화를 설계합니다.','조직의 대상, 경영과제, 프로그램 범위에 따라 맞춤 설계합니다.')+section('programs','PROGRAM DESIGN','경영 의제에서 실행 과제까지','<div class="era-grid"><div><h3>CEO·임원 특강</h3><p>경영진의 핵심 의제를 집중적으로 검토합니다.</p><p>대상: CEO·임원<br>산출물: 맞춤 강의안·사례 분석</p></div><div><h3>조직 맞춤형 워크숍</h3><p>현업의 문제를 중심으로 적용 방안을 논의합니다.</p><p>대상: 리더·실무 조직<br>산출물: 실행 체크리스트</p></div><div><h3>실행 프로젝트형 교육</h3><p>배움을 실제 업무의 개선 과제로 연결합니다.</p><p>대상: 과제 수행 조직<br>산출물: 실행 과제·점검 기준</p></div></div>')+section('inquiry','CONTACT','교육 이후, 조직에 어떤 변화가 필요합니까?',a('교육 협력 문의','/contact',True))
    page('/executive-education','Executive Education',education,schema={'@type':'Service','name':'Executive Education','provider':{'@id':ctx['BASE']+'/#person'},'url':ctx['BASE']+'/executive-education'})
    listing=intro('SELECTED WORK','문제와 역할, 그리고 실행','고객경영과 공공혁신 현장에서 수행한 프로젝트입니다.')+section('selected','SELECTED EXPERIENCE','대표 프로젝트',selected())
    page('/cases','대표 프로젝트',listing)
    keys=[('CONTEXT','프로젝트 맥락','context'),('CHALLENGE','핵심 과제','challenge'),('MY ROLE','나의 역할','role'),('WHAT WE DID','수행 내용','execution'),('IMPACT','프로젝트의 의미','impact'),('WHAT IT MEANS TODAY','오늘의 경영에 주는 시사점','meaning'),('EVIDENCE','출처','evidence')]
    for r in records:
        rows=''.join(f'<div class="case-detail-row"><p class="eyebrow">{en}</p><div><h2>{ko}</h2><p>{r[k]}</p>'+ (f'<blockquote class="source-quote">“{r["source_quote"]}”</blockquote>' if k=='evidence' else '')+'</div></div>' for en,ko,k in keys)
        page('/cases/'+r['slug'],r['title'],intro(r['category'],r['title'],r['description'])+'<div class="wrap case-detail">'+rows+'</div>'+section('next','CONTACT','조직의 과제를 함께 논의합니다.',a('자문·협력 문의','/contact',True)))
    for slug in content['draft_slugs']:
        original=ROOT/'cases'/slug/'index.html'; archive=ROOT/'content/drafts'/f'{slug}.html'
        if original.exists() and not archive.exists(): archive.write_bytes(original.read_bytes())
        page('/cases/'+slug,'대표 프로젝트',listing,noindex=True)
    # Retain all original career facts, but remove the unverified proof block.
    about=intro('ABOUT AHN','안영찬','동국대학교 경영대학원 교수<br>국가기술표준원 선정 국제표준 전문가<br>30년+ Management Transformation')+section('selected-experience','SELECTED EXPERIENCE','고객경영에서 공공혁신까지',selected())+old('career')+section('organizations','SELECTED ORGANIZATIONS','함께해 온 기업과 기관',orgs)+section('philosophy','PHILOSOPHY','Technology Changes.<br>People Come First.',philosophy+timeline+a('강의 영상 · YouTube','https://www.youtube.com/@cute_ahn_Professor'),'navy-section')
    page('/about','Profile · 안영찬',about)
    pb=old('probono')
    start=pb.index('<div class="pb-support"'); end=pb.index('</div>',start)+6; pb=pb[:start]+pb[end:]
    pb=re.sub(r'<h2>유료 서비스의 수익과 후원금으로,.*?</h2>','<h2>지식을 나누고, 변화의 기회를 넓힙니다.</h2>',pb,flags=re.S)
    pb=re.sub(r'<p>AI 전환의 격차는.*?</p>','<p>사회적기업, 소상공인, 비영리단체와 학생·청년에게 경영과 AI 활용 지식을 나누는 교육·자문·멘토링을 이어갑니다.</p>',pb,flags=re.S)
    page('/people-first','People First',intro('PHILOSOPHY','Technology Changes.<br>People Come First.','기술보다 먼저, 사람이 더 의미 있는 일을 하고 조직이 더 나은 가치를 만드는가를 묻습니다.')+pb+section('apply','PRO BONO','함께 나눌 수 있는 변화를 이야기해주세요.',a('교육·자문 신청','/contact',True)))
    page('/contact','자문·협력 문의',intro('CONTACT','지금 조직이 풀어야 할<br>가장 중요한 질문은 무엇입니까?','조직의 상황과 고민을 알려주세요.')+section('contact','START A CONVERSATION','조직의 이야기를 들려주세요.',contact()))
    page('/ax-management-brief','AX Management Brief',intro('MONTHLY INSIGHT','한 달에 한 번,<br>경영진이 생각해야 할 질문','AI와 경영환경의 변화 속에서 무엇을 판단해야 하는지 다루는 실행형 Brief.')+old('subscribe'))
    essay='<article class="wrap essay"><p class="essay-byline">안영찬 · Professor’s Question</p><p class="essay-lede">'+signature['summary']+'</p>'+''.join(f'<div><h2>{t}</h2><p>{p}</p></div>' for t,p in signature['paragraphs'])+'</article>'
    page('/professors-question',signature['title'],intro('PROFESSOR’S QUESTION',signature['title'],'AI 시대, 경영자의 판단과 책임에 대하여.')+essay+section('related','INSIGHTS','경영의 질문을 이어갑니다.',a('Insights','/insights')),desc=signature['summary'])
    page('/insights','Thinking & Insights',intro('THINKING & INSIGHTS','답보다 먼저,<br>좋은 질문을 던집니다.','AI와 경영, 조직과 사람에 관한 생각.')+section('signature','SIGNATURE THINKING','AI 시대의 경영 판단',signature_preview())+old('notices')+section('monthly','MONTHLY BRIEF','한 달에 한 번 생각할 질문',brief_link))
