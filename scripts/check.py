"""Dependency-free structural and local-link check; not a browser/accessibility audit."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.tags = []
        self.current = []
        self.language = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if tag == 'html':
            self.language = a.get('lang')
        if 'id' in a:
            self.ids.append(a['id'])
        if a.get('aria-current') == 'page':
            self.current.append(a.get('href'))
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])

pages = {}
for path in ROOT.glob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path] = page
    assert page.language == 'en', f'{path.name}: missing language'
    assert len(page.ids) == len(set(page.ids)), f'{path.name}: duplicate IDs'
    assert all(tag in page.tags for tag in ('title', 'main', 'h1')), path.name
    if path.name != 'admin.html':
        assert page.current == [path.name], f'{path.name}: current navigation'
assert len(pages) == 6, 'Expected six starter pages'
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(ROOT), f'{path.name}: out-of-root link {link}'
        assert target.is_file(), f'{path.name}: missing target {link}'
        if url.fragment and target in pages:
            assert url.fragment in pages[target].ids, f'{path.name}: missing fragment {link}'
print(f'Passed: {len(pages)} pages; local links, assets, IDs, and navigation checked.')
