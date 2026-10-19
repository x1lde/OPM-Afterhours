"""Validate the static site's local references and production media. No packages needed."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs, self.labels = path, [], [], []
        self.tags = Counter()
        self.errors = []
        self.feed(path.read_text(encoding='utf-8-sig'))

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        self.tags[tag] += 1
        if 'id' in attr:
            self.ids.append(attr['id'])
        for key in ('src', 'href', 'poster'):
            if attr.get(key):
                self.refs.append(attr[key])
        if 'for' in attr:
            self.labels.append(attr['for'])
        if tag == 'script' or any(key.startswith('on') for key in attr):
            self.errors.append('JavaScript is not allowed in the published HTML')
        if tag == 'img' and 'alt' not in attr:
            self.errors.append('Image has no alt attribute')
        if tag == 'a' and attr.get('target') == '_blank':
            if not {'noopener', 'noreferrer'} <= set(attr.get('rel', '').split()):
                self.errors.append('New-tab link needs noopener noreferrer')


def local_ref(base, ref):
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        return None
    return (base.parent / unquote(url.path)).resolve() if url.path else base.resolve()


def validate():
    pages = [Page(ROOT / 'index.html')] + [Page(p) for p in sorted((ROOT / 'artists').glob('*.html'))]
    by_path = {p.path.resolve(): p for p in pages}
    files = set(by_path)
    errors = []
    for page in pages:
        label = page.path.relative_to(ROOT).as_posix()
        errors += [f'{label}: {e}' for e in page.errors]
        if page.tags['h1'] != 1:
            errors.append(f'{label}: expected exactly one h1')
        for item, count in Counter(page.ids).items():
            if count > 1:
                errors.append(f'{label}: duplicate id {item}')
        for target in page.labels:
            if target not in page.ids:
                errors.append(f'{label}: label target {target} missing')
        for ref in page.refs:
            target = local_ref(page.path, ref)
            if target is None:
                continue
            if not target.is_relative_to(ROOT):
                errors.append(f'{label}: reference escapes site: {ref}')
                continue
            if not target.is_file():
                errors.append(f'{label}: missing file: {ref}')
                continue
            # Windows is case-insensitive; web hosts often are not.
            current = ROOT
            for part in target.relative_to(ROOT).parts:
                if part not in {p.name for p in current.iterdir()}:
                    errors.append(f'{label}: filename case mismatch: {ref}')
                    break
                current /= part
            files.add(target)
            fragment = unquote(urlsplit(ref).fragment)
            if fragment and target in by_path and fragment not in by_path[target].ids:
                errors.append(f'{label}: missing fragment: {ref}')
        if page.path.parent.name == 'artists' and page.tags['audio'] != 3:
            errors.append(f'{label}: expected three supplied audio players')

    # Follow CSS assets such as the local icon font.
    for css in list(files):
        if css.suffix == '.css':
            text = css.read_text(encoding='utf-8-sig')
            if text.count('{') != text.count('}'):
                errors.append(f'{css.name}: unbalanced CSS braces')
            for ref in re.findall(r'url\([\"\']?([^\)\"\']+)', text):
                target = local_ref(css, ref)
                if target is not None:
                    files.add(target)
                    if not target.is_file():
                        errors.append(f'{css.name}: missing CSS asset {ref}')
    for path in files:
        if path.is_file() and path.suffix in {'.mp3', '.mp4'}:
            with path.open('rb') as stream:
                if stream.read(128).startswith(b'version https://git-lfs.github.com/spec'):
                    errors.append(f'{path.relative_to(ROOT)}: Git LFS pointer; run git lfs pull')
            if path.stat().st_size == 0:
                errors.append(f'{path.name}: empty media')
    if len(pages) != 11:
        errors.append('Expected homepage and ten artist pages')
    if errors:
        raise SystemExit('\n'.join(errors))
    counts = Counter(path.suffix for path in files)
    print(f'PASS: {len(pages)} pages, {counts[".mp3"]} audio files, {counts[".mp4"]} videos; local files, fragments, labels, and script-free HTML validated.')
    return files


if __name__ == '__main__':
    validate()
