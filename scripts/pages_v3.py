"""One-off V3 update: lecture page, new research page, cases track record, sitemap. Run once: python scripts/pages_v3.py"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ARROW = '<span aria-hidden="true">↗</span>'


def read(rel):
    return (ROOT / rel).open(encoding='utf-8', newline='').read()


def write(rel, s):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding='utf-8', newline='')


def swap_main(s, main):
    a, b = s.index('<main id="main">'), s.index('</main>') + len('</main>')
    return s[:a] + main + s[b:]


def intro(eyebrow, h1, lede):
    return f'<section class="page-intro"><div class="wrap"><a class="breadcrumb" href="/">HOME</a><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p></div></section>'


def section(id, eyebrow, h2, body):
    return f'<section id="{id}" class="v2-section "><div class="wrap"><div class="sec-head"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>{body}</div></section>'


def topic(who, title, desc, track):
    return f'<div class="topic"><span class="who">{who}</span><h3>{title}</h3><p>{desc}</p><p class="track">{track}</p></div>'


# ---------- 강의·특강 ----------
TOPICS = [
    ('임원·팀장·실무자', 'Agentic AI 업무자동화 전략', 'AI 에이전트로 일하는 방식을 바꾸는 순서와 조직 적용법. Custom GPT·Copilot 기반 업무자동화.', '농협중앙회 집행임원 · 비콘코리아 반도체 기업 · 세아상역 그룹 AX 전략 특강'),
    ('공무원·공공기관', '공공부문 생성형 AI 활용', 'ChatGPT·Gemini·Claude로 공공 업무 능률을 높이는 실무 교육.', '강원도 고위 공무원 AI 활용 전략 과정 담당교수 · 동국대학교 교직원 AI 특강'),
    ('CEO·임원', '글로벌 기업 비교로 읽는 경영전략', '“삼성, 애플을 이길 수 없는 이유”, GE vs Siemens 등 비교 사례로 전략을 읽습니다.', '순회 특강 · 전경련 국제경영원 CFO·CSO 스쿨 주임교수'),
    ('영업·마케팅 조직', 'B2B 마케팅·영업 전략', '산업별 B2B 시장 분석, 마켓 센싱, 영업전략 수립.', '국내 B2B 마케팅 전략 교육과정 최초 런칭 · 삼성전자 B2B 영업 전문가 과정'),
    ('서비스·금융·유통', '고객만족경영과 CRM', 'MBNQA 기반 고객만족 경영 모델, 고객만족도 조사, CRM 전략.', '현대백화점 CRM 프로젝트 PM · 한국산업 브랜드파워지수(K-BPI) 개발'),
    ('HR·리더', '조직문화와 변화관리(GWP)', '일하기 좋은 기업을 만드는 조직문화와 리더십, 변화관리.', 'GWP Korea 일하기 좋은 100대 기업 심사위원장 · 다수 기업 GWP 특강'),
    ('경영진·현장 리더', '안전경영과 중대재해 대응', '중대재해처벌법 대응 방안과 4차 산업혁명 기술을 활용한 안전경영.', '중대재해 대응 프로그램 국내 최초 런칭 · 한화건설 전 사업장 3년 · 소방학교 5년 특강'),
    ('기획·R&D', '신사업·신상품 개발', 'GE의 NPI와 CECOR 프레임으로 신사업 기회를 찾고 기획합니다.', '삼성전자 신상품·신사업 개발 전문가 과정 · 한화그룹 신사업계획 특강'),
]

edu = read('executive-education/index.html')
edu = edu.replace('<title>Executive Education | 안영찬</title>', '<title>강의·특강 | 안영찬 교수</title>')
edu = edu.replace('<meta name="description" content="Executive Education — 30년 경영혁신 경험으로 AI 시대의 다음 경영을 설계합니다.">',
                  '<meta name="description" content="안영찬 교수 강의·특강 안내. AI 에이전트·생성형 AI 특강, CEO·임원 경영전략 특강, B2B 마케팅·영업 교육, 고객만족경영, 조직문화(GWP), 안전경영·중대재해 대응. 영어 강의 가능.">')
edu = re.sub(r'(<meta property="og:title" content=")Executive Education(")', r'\1강의·특강\2', edu)
edu = swap_main(edu, '<main id="main">'
    + intro('EXECUTIVE EDUCATION', '강의·특강 안내', '삼성전자, LG, 현대자동차, 4대 시중은행, 공공기관에서 진행해 온 강의를 조직의 대상과 과제에 맞춰 다시 설계합니다. 모든 강의는 영어로도 진행할 수 있습니다.')
    + section('topics', 'LECTURE TOPICS', '강의 주제', '<div class="topic-grid">' + ''.join(topic(*t) for t in TOPICS) + '</div>')
    + section('formats', 'FORMATS', '진행 형태',
              '<div class="format-list">'
              '<div><h3>특강</h3><p>CEO·임원, 전 직원 대상 1회 강의. 경영진의 핵심 의제를 사례 중심으로 다룹니다.</p></div>'
              '<div><h3>워크숍</h3><p>리더·실무 조직 대상. 현업의 문제를 놓고 적용 방안과 실행 체크리스트를 만듭니다.</p></div>'
              '<div><h3>과정형 교육</h3><p>사내 MBA, 차세대 리더 과정 등 여러 회차 과정. LS그룹 차세대 임원과정, YESCO 사내 MBA 주임교수 경험.</p></div>'
              '</div>')
    + section('process', 'HOW IT WORKS', '섭외 절차',
              '<ol class="process-steps">'
              '<li><b>문의</b><p>주제·대상·인원·희망 일정을 알려주세요.</p></li>'
              '<li><b>사전 미팅</b><p>교육 목표와 수강자 수준을 확인합니다.</p></li>'
              '<li><b>강의안 제안</b><p>조직 사례를 반영한 맞춤 강의안을 드립니다.</p></li>'
              '<li><b>강의 진행</b><p>특강·워크숍·과정형으로 진행합니다.</p></li>'
              '<li><b>후속 협의</b><p>결과를 함께 돌아보고 후속 과정을 논의합니다.</p></li>'
              '</ol>')
    + section('faq', 'FAQ', '자주 묻는 질문',
              '<div class="faq">'
              '<details><summary>영어로 강의할 수 있나요?</summary><p>네. 모든 강의를 영어로 진행할 수 있습니다. 외국계 기업과 해외 법인 대상 영어 연수(KIS Wire 말레이시아 법인 TPS 과정 등)를 진행했습니다.</p></details>'
              '<details><summary>우리 회사 상황에 맞게 내용을 바꿀 수 있나요?</summary><p>사전 미팅에서 교육 목표, 수강자, 업종 이슈를 확인하고 사례와 실습을 맞춰 구성합니다.</p></details>'
              '<details><summary>강의료는 어떻게 정해지나요?</summary><p>대상, 시간, 준비 범위에 따라 협의합니다. 문의를 남겨 주시면 조건을 확인해 안내드립니다.</p></details>'
              '</div>')
    + section('inquiry', 'CONTACT', '강의 주제와 일정을 알려주세요.', f'<a class="btn btn-seal" href="/contact">강의 섭외 문의 {ARROW}</a>')
    + '</main>')
write('executive-education/index.html', edu)

# ---------- 공공·연구 (new page, built from the lecture page shell) ----------
REPORTS = [
    ('2024', '규제자유특구 매치업기업 컨설턴트 조사결과 최종보고서'),
    ('2023', '스마트농업 표준화 파급효과 최종보고서 · 국가데이터 표준화 현황 보고서 · 데이터 상호운용성 표준·인증 선행연구 및 환경분석 · 빅데이터 플랫폼 운영기관 설문조사 결과 보고서 · 주요산업 기술데이터 활용 보고서 · 경남 물류중심 산업개편 최종보고서'),
    ('2022', 'J TaaS 플랫폼 구축사업 컨설팅부문 보고서 · CCUS 인증체계 보고서'),
    ('2021', '스마트관광도시 중장기 발전전략 수립 최종보고서 · 인천 스마트관광도시 발전방안 최종보고서 · 4차산업혁명 기술연계 표준화수요발굴 최종보고서 · 농업용전자통신 표준화 로드맵 보고서 · 녹색인증기업 매치업 사업 대상 설문조사 최종보고서'),
    ('2020', '해외관광산업 우수사례 벤치마킹 연구 최종보고서 · 스마트공장 표준확산을 위한 제조개선 연구용역 보고서 · 표준화수요발굴 결과보고서'),
    ('2019', '일터혁신 컨설턴트 양성 프로그램 최종보고서 · 경북창조경제혁신센터 최종보고서 · 강원창조경제혁신센터 최종보고서 · 표준화지원 컨설턴트 양성과정 최종보고서'),
    ('2017', 'General Electric 노사관계의 역사적 전개와 리더십 (대한경영학회)'),
    ('2014', '생물안전분야 국가공인 자격제도 도입 방안 연구 (질병관리본부 생물안전평가과, 공동연구)'),
    ('발간', '국내외 임금체계 사례연구 (경제사회발전 노사정위원회, 공동연구) · 세계 은행 산업의 패러다임 변화 · 한국 진출 3대 글로벌 은행 보고서'),
]
PUBLIC_PROJECTS = [
    ('스마트관광·도시', ['한국관광공사 「스마트관광도시 구축 매뉴얼」 제작 컨설팅', '국내 최초 스마트관광도시 추진 가이드라인 매뉴얼 개발', '인천 스마트관광도시 발전방안 컨설팅', '스마트도시협회 AI 도시 구축 자문교수']),
    ('표준화·스마트팩토리', ['한국표준협회 중소중견기업 국제표준화 지원사업(매치업) 5년 수행', '한국표준협회 스마트공장 확산 및 고도화 컨설팅 전략', '한국표준협회 표준화지원 컨설턴트 양성과정', '4차산업혁명 기술연계 표준화 수요발굴']),
    ('지역·산업 혁신', ['강원·경북창조경제혁신센터 조직문화 진단 및 중장기 발전전략', '노사발전재단 중장기 발전전략, 일터혁신 컨설팅 교수법 수립', '새만금개발청 자문교수', '정보통신진흥원(NIPA) 고객만족 경영 컨설팅']),
    ('공공기관 경영혁신', ['국민체육진흥공단 고객만족경영 중장기 전략, 경륜 경정 파크 서비스품질 체계', '한국도로공사 고객중심경영 중장기 전략', '철도청·한국담배인삼공사 고객만족 경영혁신 컨설팅', '국내 공공기관 품질 평가 시스템 개발 및 런칭']),
]

res = read('executive-education/index.html')
res = res.replace('<title>강의·특강 | 안영찬 교수</title>', '<title>공공·연구 | 안영찬 교수</title>')
res = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="안영찬 교수 공공·연구 용역. 국가기술표준원 선정 국제표준 전문가. 표준화·스마트팩토리, 스마트관광도시, 지역혁신, 공공기관 고객만족경영 연구와 컨설팅 보고서 30건 이상.">', res, count=1)
res = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="공공·연구">', res, count=1)
res = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="표준화·스마트관광도시·지역혁신 연구용역과 공공기관 경영혁신 컨설팅.">', res, count=1)
res = res.replace('https://ahnyoungchan.kr/executive-education', 'https://ahnyoungchan.kr/research')
res = res.replace('"name": "Executive Education"', '"name": "공공·연구"')
res = res.replace('<li><a href="/executive-education" aria-current="page">', '<li><a href="/executive-education">')
res = res.replace('<li><a href="/research">', '<li><a href="/research" aria-current="page">')
res = swap_main(res, '<main id="main">'
    + intro('RESEARCH & PUBLIC PROJECTS', '공공·연구 용역', '표준화, 스마트관광도시, 지역혁신, 공공기관 경영혁신 분야에서 연구용역과 컨설팅을 수행해 왔습니다.')
    + section('credentials', 'CREDENTIALS', '공식 자격과 자문 활동',
              '<ul class="credential-list">'
              '<li>국가기술표준원 선정 국제표준 전문가<span>2022 – 현재</span></li>'
              '<li>한국표준협회 스마트팩토리 지원 컨설팅 전문위원<span>현재</span></li>'
              '<li>새만금개발청 자문교수<span>현재</span></li>'
              '<li>스마트도시협회 AI 도시 구축 자문교수<span>현재</span></li>'
              '<li>한국생산관리학회 대외협력위원장<span>현재</span></li>'
              '<li>동국대학교 경영대학원 교수 · 경영학 박사<span>현재</span></li>'
              '</ul>')
    + section('projects', 'PUBLIC PROJECTS', '분야별 수행 과제',
              '<div class="record-groups">' + ''.join(f'<div><h3>{h}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>' for h, items in PUBLIC_PROJECTS) + '</div>')
    + section('reports', 'REPORTS', '주요 연구보고서·저서',
              '<dl class="report-list">' + ''.join(f'<dt>{y}</dt><dd>{t}</dd>' for y, t in REPORTS) + '</dl>')
    + section('inquiry', 'CONTACT', '연구용역·자문 과제를 알려주세요.', f'<a class="btn btn-seal" href="/contact">공공·연구 문의 {ARROW}</a>')
    + '</main>')
write('research/index.html', res)

# ---------- 실적: industry track record below the two featured cases ----------
RECORD = [
    ('금융', ['국민은행 지점 재설계·소형특화점포 입지 및 마케팅 전략', '국민은행 공과금 자동화 시스템 구축 컨설팅', '하나은행 고객만족 경영혁신 프로젝트 주관, PB사업본부 컨설팅', '신한은행 고객만족도 조사·마케팅 전략·변화관리 컨설팅', '동양화재·동부화재 변화관리 및 전략 수립 컨설팅', '일본 Hitachi 국내 금융기관 IT 인프라 조사 프로젝트(2회)']),
    ('제조·에너지', ['LG화학 고객만족 경영혁신, 변화관리·Change Agent 양성, 청주공장 품질혁신·6시그마', 'SK케미칼 BSC+MBO 관리체계 고도화, 영업·마케팅 플랫폼(MPDP) 구축', 'SK Telecom 6시그마 접근법을 통한 발전전략 컨설팅', '동양제과 Transactional Six Sigma & DFSS 컨설팅', '태평양화학 생산구조 고도화 프로젝트', '에너윈코리아 신재생 풍력에너지 터빈 컨설팅']),
    ('유통·서비스', ['현대백화점 CRM 컨설팅 PM (이후 2년간 후속 프로젝트)', '에버랜드 서비스 구축 및 평가 컨설팅 (1995–2013)', '롯데월드 서비스 체계 구축 및 평가 컨설팅', '웅진그룹 아메바경영 도입, 웅진플레이도시 서비스 평가 체계', '컴팩코리아 신규 유통채널·프랜차이즈 마케팅 전략', '한국 OGK 안경 신상품 런칭 및 브랜딩']),
    ('공공기관', ['한국관광공사 스마트관광도시 구축 매뉴얼 제작', '한국표준협회 국제표준화 지원사업(매치업) 5년 수행', '국민체육진흥공단 고객만족경영 중장기 전략', '한국도로공사 고객중심경영 중장기 전략', '강원·경북창조경제혁신센터 조직문화 진단 및 중장기 발전전략', '정보통신진흥원(NIPA) 고객만족 경영 컨설팅']),
]
cases = read('cases/index.html')
cases = cases.replace('<title>대표 프로젝트 | 안영찬</title>', '<title>실적 | 안영찬 교수</title>')
cases = cases.replace('<meta name="description" content="대표 프로젝트 — 30년 경영혁신 경험으로 AI 시대의 다음 경영을 설계합니다.">',
                      '<meta name="description" content="안영찬 교수 컨설팅·교육 실적. 금융, 제조, 유통·서비스, 공공기관에서 수행한 CRM, 고객만족경영, 6시그마·BSC, 변화관리, 스마트관광도시, 표준화 프로젝트.">')
cases = cases.replace('<p class="lede">고객경영과 공공혁신 현장에서 수행한 프로젝트입니다.</p>',
                      '<p class="lede">금융, 제조, 유통·서비스, 공공기관에서 수행한 컨설팅과 교육 실적입니다.</p>')
tail = '</div></div></section></main>'
assert cases.count(tail) == 1
cases = cases.replace(tail, '</div></div></section>'
    + section('record', 'TRACK RECORD', '업종별 주요 컨설팅',
              '<div class="record-groups">' + ''.join(f'<div><h3>{h}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>' for h, items in RECORD) + '</div>')
    + section('education-record', 'EDUCATION', '강의·교육을 진행한 주요 기업·기관',
              '<p class="people-copy" style="max-width:900px">삼성전자, 삼성SDS, 삼성물산, LG전자, SK텔레콤, SK네트웍스, KT, 현대자동차, 기아자동차, 포스코, 현대제철, CJ, 롯데호텔, 신세계백화점, 국민·우리·하나·신한·SC제일은행, 삼성화재, 교보생명, 한화생명, 금융결제원, 농협중앙회, 수협중앙회, 전경련 국제경영원, 한국무역협회, 한국전력, 한국수자원공사, 한국가스안전공사, 국토교통부, 강원도, 소방학교 외 100곳 이상</p>'
              f'<a class="btn text-link" href="/executive-education">강의 주제 보기 {ARROW}</a>')
    + '</main>')
write('cases/index.html', cases)

# ---------- sitemap ----------
sm = read('sitemap.xml')
if '/research' not in sm:
    sm = sm.replace('<url><loc>https://ahnyoungchan.kr/cases</loc>', '<url><loc>https://ahnyoungchan.kr/research</loc></url><url><loc>https://ahnyoungchan.kr/cases</loc>', 1)
write('sitemap.xml', sm)
print('pages updated; research in sitemap:', '/research' in sm)
