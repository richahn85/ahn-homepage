"""Official cross-channel directory using the site's existing page template."""
CHANNELS = [
    ('공식 홈페이지', '소개 · 경영자문 · AI 전환 · 교육 · 프로젝트', 'https://ahnyoungchan.kr'),
    ('네이버 블로그', '경영·AI·People First 인사이트와 좋은잠 연구소 원문', 'https://blog.naver.com/smartwolf85'),
    ('Instagram', '현장 이야기와 넘겨보는 좋은잠 연구소 카드뉴스', 'https://www.instagram.com/neverstopwolf/'),
    ('LinkedIn', '전문 인사이트 · 경력 · 협업 네트워크', 'https://www.linkedin.com/in/richard-ahn-0359332a/'),
]

def render(ns):
    cards = ''.join(f'<article class="channel-card"><h2>{name}</h2><p>{desc}</p><a class="text-link" href="{url}">{name} 바로가기 ↗</a></article>' for name, desc, url in CHANNELS)
    body = '<section class="v2-section"><div class="wrap"><p class="eyebrow">OFFICIAL CHANNELS · THINKING INTO ACTION</p><h1>안영찬 교수의 공식 채널</h1><p class="channel-lead">경영혁신·AI 전환·교육·People First.<br>생각을 실행으로 연결하는 이야기들을 한곳에서 만나보세요.</p><div class="channel-grid">'+cards+'</div><p class="channel-lead">Technology Changes. People Come First.</p></div></section>'
    ns['page']('/channels', '공식 채널 모아보기', body, '안영찬 교수의 홈페이지, 네이버 블로그, Instagram, LinkedIn을 한곳에서 만나보세요.')
