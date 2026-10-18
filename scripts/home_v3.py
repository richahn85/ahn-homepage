"""One-off V3 content update for the homepage and contact form. Run once: python scripts/home_v3.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def edit(rel, pairs):
    f = ROOT / rel
    s = f.open(encoding='utf-8', newline='').read()
    for old, new in pairs:
        assert s.count(old) == 1, (rel, old[:80])
        s = s.replace(old, new)
    f.write_text(s, encoding='utf-8', newline='')


ARROW = '<span aria-hidden="true">↗</span>'

HERO_OLD = '<p class="eyebrow">MANAGEMENT TRANSFORMATION · SINCE 1992</p><h1>경영 패러다임이<br>바뀔 때마다,<br><span>현장에 먼저 답을<br>만들어 왔습니다.</span></h1><p class="lede">30년 이상의 경영혁신 경험으로<br><strong>AI를 ‘도구’에서 ‘경영성과’로 바꿉니다.</strong></p><p class="hero-identity"><b>안영찬</b><br>Management Transformation Advisor</p><p class="hero-authority">동국대학교 경영대학원 교수<br>국가기술표준원 선정 국제표준 전문가</p><div class="cta-row"><a class="btn btn-seal" href="/contact">자문·협력 문의 <span aria-hidden="true">↗</span></a><a class="btn text-link" href="/cases">대표 프로젝트 <span aria-hidden="true">↗</span></a></div>'
HERO_NEW = ('<p class="eyebrow">동국대학교 경영대학원 교수 · 국가기술표준원 선정 국제표준 전문가</p>'
            '<h1>AI 전환부터 고객경영까지,<br><span>30년 현장에서 검증한<br>강의와 자문</span></h1>'
            '<p class="lede">1992년부터 기업·금융·공공 현장에서 경영혁신을 이끌어 왔습니다.<br><strong>AI를 ‘도구’에서 ‘경영성과’로 바꿉니다.</strong></p>'
            '<p class="hero-identity"><b>안영찬</b><br>Management Transformation Advisor</p>'
            '<ul class="goal-list" aria-label="찾으시는 내용">'
            '<li><a href="/executive-education"><b>강의·특강 섭외</b><span>임원 특강 · AI 실무 교육 · 조직 맞춤 워크숍</span><i aria-hidden="true">→</i></a></li>'
            '<li><a href="/advisory"><b>경영 자문</b><span>AI 전환 전략 · 신사업 · B2B 성장 · 조직문화</span><i aria-hidden="true">→</i></a></li>'
            '<li><a href="/research"><b>공공·연구 용역</b><span>표준화 · 스마트도시·관광 · 정책 연구</span><i aria-hidden="true">→</i></a></li>'
            '</ul>')

PROOF_OLD_START = '<section id="proof" class="v2-section ">'
PROOF_OLD_END = '</ul></div></div></section><section id="services"'
PROOF_NEW = ('<section id="proof" class="v2-section "><div class="wrap"><div class="sec-head"><p class="eyebrow">TRACK RECORD</p><h2>업종을 가리지 않고<br>현장의 문제를 풀어 왔습니다.</h2></div>'
             '<div class="proof-strip v3-proof">'
             '<div><b>1992~</b><p>경영혁신·컨설팅·교육 현장</p></div>'
             '<div><b>100+</b><p>강의·교육을 진행한 기업·기관</p></div>'
             '<div><b>80+</b><p>컨설팅·제안 프로젝트</p></div>'
             '<div><b>30+</b><p>연구보고서·저서</p></div></div>'
             '<p class="proof-note">모든 강의는 영어로도 진행할 수 있습니다.</p>'
             '<div class="org-groups">'
             '<div><h3>제조·IT</h3><ul><li>삼성전자</li><li>LG화학</li><li>현대자동차</li><li>포스코</li><li>SK Telecom</li><li>KT</li></ul></div>'
             '<div><h3>금융</h3><ul><li>국민은행</li><li>우리은행</li><li>하나은행</li><li>신한은행</li><li>삼성화재</li><li>금융결제원</li></ul></div>'
             '<div><h3>공공기관</h3><ul><li>한국관광공사</li><li>한국표준협회</li><li>국민체육진흥공단</li><li>한국도로공사</li><li>한국전력</li><li>강원도</li></ul></div>'
             '<div><h3>유통·서비스</h3><ul><li>현대백화점</li><li>신세계백화점</li><li>에버랜드</li><li>롯데호텔</li><li>강원랜드</li><li>CJ</li></ul></div>'
             '</div></div></section>'
             '<section id="topics" class="v2-section "><div class="wrap"><div class="sec-head"><p class="eyebrow">LECTURES</p><h2>많이 찾는 강의 주제</h2></div>'
             '<div class="topic-grid">'
             '<div class="topic"><span class="who">임원·리더</span><h3>Agentic AI 업무자동화 전략</h3><p>AI 에이전트로 일하는 방식을 바꾸는 순서와 조직 적용법.</p></div>'
             '<div class="topic"><span class="who">전 직원·공무원</span><h3>생성형 AI 실무 활용</h3><p>ChatGPT·Gemini·Claude, Custom GPT·Copilot으로 업무 생산성 높이기.</p></div>'
             '<div class="topic"><span class="who">CEO·임원</span><h3>삼성, 애플을 이길 수 없는 이유</h3><p>글로벌 기업 비교로 읽는 경영전략. 기업·대학 순회 특강.</p></div>'
             '<div class="topic"><span class="who">영업·마케팅 조직</span><h3>B2B 마케팅·영업 전략</h3><p>국내 최초 B2B 마케팅 교육과정을 런칭한 경험을 바탕으로 합니다.</p></div>'
             '<div class="topic"><span class="who">서비스·금융·유통</span><h3>고객만족경영과 CRM</h3><p>MBNQA·KCSI 모델과 현대백화점 CRM 프로젝트 경험.</p></div>'
             '<div class="topic"><span class="who">경영진·현장 리더</span><h3>안전경영과 중대재해 대응</h3><p>4차 산업혁명 기술을 활용한 안전경영 리더십.</p></div>'
             f'</div><a class="btn btn-seal" href="/executive-education#topics">강의 주제 전체 보기 {ARROW}</a></div></section>'
             '<section id="services"')

SERVICES = [
    ('<p class="eyebrow">03 / WHAT I DO</p><h2>경영진의 판단에서 조직의 실행까지</h2>', '<p class="eyebrow">SERVICES</p><h2>경영진의 판단에서 조직의 실행까지</h2>'),
    ('<p class="eyebrow">CEO ADVISORY</p><h3>', '<p class="eyebrow">기업 자문</p><h3>'),
    ('<a class="btn text-link" href="/advisory">CEO ADVISORY 보기', '<a class="btn text-link" href="/advisory">기업 자문 보기'),
    ('<p class="eyebrow">AX TRANSFORMATION</p><h3>', '<p class="eyebrow">AI 전환</p><h3>'),
    ('<a class="btn text-link" href="/ax-transformation">AX TRANSFORMATION 보기', '<a class="btn text-link" href="/ax-transformation">AI 전환 보기'),
    ('<p class="eyebrow">EXECUTIVE EDUCATION</p><h3>', '<p class="eyebrow">강의·특강</p><h3>'),
    ('<a class="btn text-link" href="/executive-education">EXECUTIVE EDUCATION 보기', '<a class="btn text-link" href="/executive-education">강의·특강 보기'),
    ('<p class="eyebrow">04 / SELECTED WORK</p>', '<p class="eyebrow">SELECTED WORK</p>'),
    ('<span class="text-link">프로젝트 읽기 ↗</span></a></div></div></section><section id="thinking"',
     f'<span class="text-link">프로젝트 읽기 ↗</span></a></div><a class="btn text-link" href="/cases">업종별 실적 전체 보기 {ARROW}</a></div></section>'
     '<section id="process" class="v2-section "><div class="wrap"><div class="sec-head"><p class="eyebrow">HOW IT WORKS</p><h2>문의부터 진행까지</h2></div>'
     '<ol class="process-steps">'
     '<li><b>문의</b><p>폼이나 이메일로 주제·대상·희망 일정을 알려주세요.</p></li>'
     '<li><b>사전 미팅</b><p>조직의 상황과 목표를 짧게 확인합니다.</p></li>'
     '<li><b>맞춤 제안</b><p>대상과 과제에 맞춘 강의안·자문 범위를 제안합니다.</p></li>'
     '<li><b>진행</b><p>특강·워크숍·자문을 진행합니다.</p></li>'
     '<li><b>후속 협의</b><p>결과를 함께 돌아보고 다음 과제를 정합니다.</p></li>'
     '</ol></div></section><section id="thinking"'),
    ('<p class="eyebrow">05 / SIGNATURE THINKING</p>', '<p class="eyebrow">SIGNATURE THINKING</p>'),
    ('<a class="btn text-link" href="/insights">Insights <span', '<a class="btn text-link" href="/insights">인사이트 전체 보기 <span'),
    ('<p class="eyebrow">06 / ABOUT & PHILOSOPHY</p>', '<p class="eyebrow">ABOUT & PHILOSOPHY</p>'),
    ('<a class="btn text-link" href="/about">About <span', '<a class="btn text-link" href="/about">소개 <span'),
    ('<p class="eyebrow">07 / CONTACT</p>', '<p class="eyebrow">CONTACT</p>'),
]

FORM_FIELDS_OLD = '<div class="form-fields"><label>이름 *<input name="name" type="text" autocomplete="name" required></label><label>소속 *<input name="org" type="text" autocomplete="organization" required></label><label>이메일 *<input name="email" type="email" autocomplete="email" required></label><label>문의 유형 *<select name="type" required><option value="">선택해주세요</option><option value="경영진 정기 자문">CEO Advisory</option><option value="AX 컨설팅 프로젝트">AX Transformation</option><option value="특강·워크숍">Executive Education</option><option value="Research & Public Project">Research & Public Project</option><option value="Media / Interview">Media / Interview</option><option value="사회공헌 무료 서비스 (사회적기업·소상공인·비영리)">People First / Pro Bono</option></select></label></div><label>현재 가장 해결하고 싶은 경영 과제를 간단히 적어주세요. *<textarea name="message" rows="5" required></textarea></label><button class="form-btn" type="submit">상담 요청 보내기 ↗</button>'
FORM_FIELDS_NEW = ('<div class="form-fields">'
                   '<label>이름 *<input name="name" type="text" autocomplete="name" required></label>'
                   '<label>이메일 *<input name="email" type="email" autocomplete="email" required></label>'
                   '<label>소속 (선택)<input name="org" type="text" autocomplete="organization"></label>'
                   '<label>연락처 (선택)<input name="phone" type="tel" autocomplete="tel"></label>'
                   '<label>문의 유형 *<select name="type" required><option value="">선택해주세요</option>'
                   '<option value="강의·특강 섭외">강의·특강 섭외</option><option value="경영 자문">경영 자문</option>'
                   '<option value="AI 전환 프로젝트">AI 전환 프로젝트</option><option value="공공·연구 용역">공공·연구 용역</option>'
                   '<option value="언론·인터뷰">언론·인터뷰</option><option value="People First (사회적기업·소상공인·비영리)">People First (사회적기업·소상공인·비영리)</option></select></label></div>'
                   '<label>문의 내용 *<textarea name="message" rows="5" required placeholder="예) 임원 30명 대상 AI 활용 특강, 12월 중 2시간 희망"></textarea></label>'
                   '<button class="form-btn" type="submit">문의 보내기 ↗</button>')
CONTACT_INTRO_OLD = '<p>고민의 출발점부터 함께 살펴보겠습니다.<br>조직의 상황과 희망 일정을 알려주세요.</p>'
CONTACT_INTRO_NEW = '<p>주제, 대상, 인원, 희망 일정을 알려주시면<br>확인 후 이메일이나 전화로 회신드립니다.</p>'

edit('index.html', [
    ('<title>Management Transformation Advisor | 안영찬</title>', '<title>안영찬 교수 | AI·경영전략 강의와 기업 자문</title>'),
    ('<meta name="description" content="Management Transformation Advisor — 30년 경영혁신 경험으로 AI 시대의 다음 경영을 설계합니다.">',
     '<meta name="description" content="동국대 경영대학원 안영찬 교수. AI 전환·생성형 AI 특강, 임원 경영전략 강의, B2B 마케팅·고객만족경영 교육, 기업 자문과 공공 연구용역. 1992년부터 100곳 이상의 기업·기관과 함께했습니다.">'),
    (HERO_OLD, HERO_NEW),
    *SERVICES,
    (FORM_FIELDS_OLD, FORM_FIELDS_NEW),
    (CONTACT_INTRO_OLD, CONTACT_INTRO_NEW),
])

# Replace the whole proof section (organizations list included) in one go.
f = ROOT / 'index.html'
s = f.open(encoding='utf-8', newline='').read()
a = s.index(PROOF_OLD_START)
b = s.index(PROOF_OLD_END) + len(PROOF_OLD_END)
s = s[:a] + PROOF_NEW + s[b:]
f.write_text(s, encoding='utf-8', newline='')

edit('contact/index.html', [
    ('<p class="lede">조직의 상황과 고민을 알려주세요.</p>', '<p class="lede">강의 섭외, 경영 자문, 공공·연구 용역 모두 이 폼으로 문의하실 수 있습니다.</p>'),
    ('<p class="eyebrow">START A CONVERSATION</p><h2>조직의 이야기를 들려주세요.</h2>', '<p class="eyebrow">START A CONVERSATION</p><h2>무엇을 도와드릴까요?</h2>'),
    (FORM_FIELDS_OLD, FORM_FIELDS_NEW),
    (CONTACT_INTRO_OLD, CONTACT_INTRO_NEW),
])
print('home and contact updated')
