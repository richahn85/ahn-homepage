"""Lecture download page and entry links."""
def render(ctx):
    root, page, intro, section = (ctx[k] for k in ('ROOT', 'page', 'intro', 'section'))
    route = '/downloads/samsung-apple'
    title = '삼성전자와 애플, 두 자본주의의 재무제표'
    files = [
        ('강의 보강 자료', 'PPTX · 12장 · 64 KB', 'samsung-apple-lecture-12-slides.pptx', '삼성전자와_애플_두_자본주의의_재무제표_강의보강_12장.pptx'),
        ('신현한 원문 자료', 'PDF · JC 2026-21 · 2.23 MB', 'samsung-apple-jc-2026-21.pdf', 'JC 2026-21 (신현한_ 삼성전자와 애플, 두 자본주의의 재무제표 ) (1).pdf'),
    ]
    cards = '<div class="era-grid">' + ''.join(
        f'<article><p class="eyebrow">{kind}</p><h3>{label}</h3><p>{title}</p>'
        f'<a class="btn btn-seal" href="{route}/{filename}" download="{original}">{kind.split(" · ")[0]} 다운로드 ↓</a></article>'
        for label, kind, filename, original in files
    ) + '</div>'
    page(route, title, intro('LECTURE MATERIALS', title, '강의 보강 자료와 신현한 원문 자료를 다운로드할 수 있습니다.') + section('files', 'DOWNLOADS', '강의 자료 다운로드', cards), desc=title + ' 강의 보강 PPTX 12장 및 신현한 원문 PDF 다운로드.')
    link = f'<p class="monthly-link" id="lecture-downloads"><a href="{route}/"><span>강의 자료 다운로드</span> {title} · PPTX / PDF →</a></p>'
    for name in ('index.html', 'insights/index.html'):
        path = root / name
        text = path.read_text(encoding='utf-8')
        if 'id="lecture-downloads"' not in text:
            if name == 'index.html':
                marker = '<p class="monthly-link">'
                assert marker in text
                text = text.replace(marker, link + marker, 1)
            else:
                text = text.replace('</main>', section('lecture-materials', 'LECTURE MATERIALS', '강의 자료', link) + '</main>', 1)
            path.write_text(text, encoding='utf-8')
