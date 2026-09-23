"""Validate the generated public site, its local links, and language pairs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'


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
    for path in (ROOT / 'docs').rglob('*.md'):
        parts = path.read_text(encoding='utf-8').split('---', 2)
        metadata = yaml.safe_load(parts[1]) if len(parts) == 3 else {}
        if metadata.get('lang') not in ('ru', 'en') or 'translation' not in metadata:
            failures.append(f'Missing language metadata: {path.relative_to(ROOT)}')
            continue
        translated = SITE / metadata['translation'] / 'index.html'
        if not translated.is_file():
            failures.append(f'Missing translated page: {path.relative_to(ROOT)}')
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print(f'Checked {len(files)} HTML pages: links, anchors, language pairs, and public-content boundary.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
