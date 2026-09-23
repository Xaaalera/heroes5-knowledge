"""Validate the generated public site, its local links, and language pairs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from datetime import date
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'


def check_articles(docs, factions):
    """Check declared editorial state, not the truth of article content."""
    failures = []
    pages = {}
    counts = dict.fromkeys(('draft', 'verified', 'outdated'), 0)
    types = {'tutorial', 'how-to', 'reference', 'explanation', 'landing', 'meta'}
    for path in docs.rglob('*.md'):
        relative = path.relative_to(docs).as_posix()
        text = path.read_text(encoding='utf-8')
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        try:
            metadata = yaml.safe_load(match.group(1)) if match else None
        except yaml.YAMLError:
            metadata = None
        if not isinstance(metadata, dict):
            failures.append(f'{relative}: missing or invalid YAML metadata')
            continue
        address = relative[:-8] if path.name == 'index.md' else relative[:-3] + '/'
        pages[address] = (relative, metadata)
        language = 'en' if relative.startswith('en/') else 'ru'
        if metadata.get('lang') != language:
            failures.append(f'{relative}: lang must match its language directory')
        if not isinstance(metadata.get('translation'), str):
            failures.append(f'{relative}: translation must be a site-relative URL string')
        kind = metadata.get('content_type')
        status = metadata.get('status')
        if not isinstance(kind, str) or kind not in types:
            failures.append(f'{relative}: invalid content_type')
        if not isinstance(status, str) or status not in counts:
            failures.append(f'{relative}: invalid status')
        else:
            counts[status] += 1
        if not isinstance(metadata.get('faction'), str) or metadata['faction'] not in factions:
            failures.append(f'{relative}: invalid faction')
        if status in ('verified', 'outdated') and kind not in ('landing', 'meta'):
            if not isinstance(metadata.get('scope'), str) or not metadata['scope'].strip():
                failures.append(f'{relative}: verified/outdated article requires scope')
            try:
                date_text = str(metadata.get('verified_on'))
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date_text):
                    raise ValueError('invalid date format')
                verified = date.fromisoformat(date_text)
                if verified > date.today():
                    raise ValueError('future date')
            except ValueError:
                failures.append(f'{relative}: verified_on must be a real non-future date')
            sources = metadata.get('sources')
            if not isinstance(sources, list) or not sources or any(
                not isinstance(source, str) or not source.startswith('https://')
                or not re.match(r'https://[A-Za-z0-9][A-Za-z0-9.-]*(?::[0-9]+)?(?:/|$)', source) for source in sources
            ):
                failures.append(f'{relative}: sources must list public HTTPS evidence URLs')
    for address, (relative, metadata) in pages.items():
        target = metadata.get('translation')
        counterpart = pages.get(target) if isinstance(target, str) else None
        expected = address[3:] if address.startswith('en/') else 'en/' + address
        if target != expected or not counterpart or counterpart[1].get('translation') != address:
            failures.append(f'{relative}: translation must link to its reciprocal RU/EN counterpart')
            continue
        for field in ('content_type', 'status', 'faction'):
            if metadata.get(field) != counterpart[1].get(field):
                failures.append(f'{relative}: translation disagrees on {field}')
    return failures, counts


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if 'id' in attributes:
            self.ids.add(attributes['id'])
        for name in ('href', 'src'):
            if attributes.get(name):
                self.links.append(attributes[name])


def main():
    failures = []
    for path in SITE.rglob('*'):
        if path.is_file() and (path.suffix == '.pyc' or '__pycache__' in path.parts):
            failures.append(f'Python cache must not be published: {path.relative_to(SITE)}')
    files = list(SITE.rglob('*.html'))
    if len(files) < 17:
        failures.append('Expected the bilingual articles and 404 page; run npm run build.')
    parsed = {}
    for path in files:
        text = path.read_text(encoding='utf-8')
        document = Links()
        document.feed(text)
        parsed[path.resolve()] = document
        if re.search(r'heroes5-mod-workshop|[A-Z]:\\|\.local/test-state|gh[oprs]_[A-Za-z0-9]{20,}', text):
            failures.append(f'Unexpected private-workspace or credential reference: {path.relative_to(SITE)}')
    prefix = urlsplit(yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))['site_url']).path
    for path, document in parsed.items():
        for link in document.links:
            address = urlsplit(link)
            if address.scheme or address.netloc:
                continue
            relative = unquote(address.path)
            if relative.startswith(prefix):
                target = SITE / relative[len(prefix):]
            elif relative.startswith('/'):
                failures.append(f'Link escapes deployment prefix in {path.name}: {link}')
                continue
            else:
                target = path.parent / relative if relative else path
            if target.is_dir():
                target /= 'index.html'
            target = target.resolve()
            if not target.is_relative_to(SITE.resolve()) or not target.is_file():
                failures.append(f'Broken local link in {path.relative_to(SITE)}: {link}')
            elif address.fragment and target in parsed and unquote(address.fragment) not in parsed[target].ids:
                failures.append(f'Broken anchor in {path.relative_to(SITE)}: {link}')
    config = yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))
    article_failures, counts = check_articles(ROOT / 'docs', config['extra']['worlds'])
    failures.extend(article_failures)
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print(f'Checked {len(files)} HTML pages: links, anchors, language pairs, and public-content boundary.')
    print(f'Editorial declarations: {counts}. Draft/outdated content is not certified by this check.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
