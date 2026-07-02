#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parent
ERRORS: list[str] = []


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


manifest = json.loads((ROOT / 'coverage-manifest.json').read_text(encoding='utf-8'))
audit = json.loads((ROOT / 'FULL_DOCSITE_AUDIT.json').read_text(encoding='utf-8'))

required_counts = {
    'root_commands': 140,
    'toolkit_runnable_paths': 280,
    'test_suite_commands': 5,
    'all_command_paths': 285,
    'canonical_routes': 173,
    'features': 137,
    'functions': 983,
    'tests': 215,
    'schemas': 93,
    'adapters': 31,
    'source_manifest_files': 411,
    'ghidra_scripts': 3,
    'toolkit_functions': 843,
    'verification_functions': 140,
    'search_entries': 2183,
}
for key, expected in required_counts.items():
    actual = manifest.get('counts', {}).get(key)
    if actual != expected:
        ERRORS.append(f'coverage count {key}: expected {expected}, got {actual}')

for key in ('root_commands', 'canonical_routes', 'features', 'functions', 'test_suite_commands', 'tests', 'schemas', 'adapters', 'ghidra_scripts', 'source_manifest_files'):
    expected = manifest.get('expected', {}).get(key)
    documented = manifest.get('documented', {}).get(key)
    if expected != documented:
        ERRORS.append(f'coverage list mismatch: {key}')

if audit.get('status') != 'pass' or audit.get('counts', {}).get('failed_checks') != 0:
    ERRORS.append('FULL_DOCSITE_AUDIT.json does not record a clean pass')


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.refs: list[str] = []
        self.nav_links: list[str] = []
        self._inside_sidebar = False
        self._inside_nav = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get('id'):
            self.ids.add(str(data['id']))
        classes = str(data.get('class', '')).split()
        if tag == 'aside' and 'sidebar' in classes:
            self._inside_sidebar = True
        if tag == 'nav' and self._inside_sidebar:
            self._inside_nav = True
        for attr in ('href', 'src'):
            if data.get(attr):
                ref = str(data[attr])
                self.refs.append(ref)
                if tag == 'a' and attr == 'href' and self._inside_nav:
                    self.nav_links.append(ref)

    def handle_endtag(self, tag: str) -> None:
        if tag == 'nav':
            self._inside_nav = False
        if tag == 'aside':
            self._inside_sidebar = False


html_files = sorted(ROOT.rglob('*.html'))
if len(html_files) != 354:
    ERRORS.append(f'HTML page count: expected 354, got {len(html_files)}')

hidden_backups = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_dir() and ('backup' in p.name.lower() or p.name.startswith('.project-examples'))]
if hidden_backups:
    ERRORS.append('embedded backup directories: ' + ', '.join(hidden_backups))

parsed: dict[Path, PageParser] = {}
for path in html_files:
    parser = PageParser()
    parser.feed(path.read_text(encoding='utf-8'))
    parsed[path.resolve()] = parser

for path in html_files:
    parser = parsed[path.resolve()]
    if len(parser.nav_links) != 13:
        ERRORS.append(f'{path.relative_to(ROOT)}: expected 13 sidebar links, got {len(parser.nav_links)}')
    if sum(1 for item in parser.nav_links if item.endswith('source-coverage.html')) != 1:
        ERRORS.append(f'{path.relative_to(ROOT)}: source-coverage navigation entry mismatch')
    for ref in parser.refs:
        if ref.startswith(('mailto:', 'javascript:', 'data:')):
            continue
        if ref.startswith(('http://', 'https://')):
            ERRORS.append(f'{path.relative_to(ROOT)}: external runtime reference {ref}')
            continue
        target, fragment = urldefrag(ref)
        resolved = (path.parent / target).resolve() if target else path.resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            ERRORS.append(f'{path.relative_to(ROOT)}: reference escapes site: {ref}')
            continue
        if not resolved.exists():
            ERRORS.append(f'{path.relative_to(ROOT)}: broken reference: {ref}')
            continue
        if fragment and resolved.suffix.lower() == '.html':
            target_parser = parsed.get(resolved)
            if target_parser is None:
                target_parser = PageParser()
                target_parser.feed(resolved.read_text(encoding='utf-8'))
                parsed[resolved] = target_parser
            if fragment not in target_parser.ids:
                ERRORS.append(f'{path.relative_to(ROOT)}: missing fragment: {ref}')

marker_patterns = (
    re.compile(r'\bTODO\b', re.I),
    re.compile(r'\bTBD\b', re.I),
    re.compile(r'lorem ipsum', re.I),
    re.compile(r'coming soon', re.I),
    re.compile(r'insert (?:text|content) here', re.I),
    re.compile(r'<(?:placeholder|your[-_ ]?[a-z0-9_-]+)>', re.I),
)
for path in ROOT.rglob('*'):
    if not path.is_file() or path.suffix.lower() not in {'.html', '.js', '.css', '.md', '.txt', '.py'}:
        continue
    if path.name in {'FULL_DOCSITE_AUDIT.md', 'verify_site.py'}:
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    for pattern in marker_patterns:
        if pattern.search(text):
            ERRORS.append(f'{path.relative_to(ROOT)}: unfinished-content marker {pattern.pattern}')

search_text = (ROOT / 'assets/search-index.js').read_text(encoding='utf-8')
match = re.search(r'window\.X86DOCS_SEARCH_INDEX\s*=\s*(\[.*\])\s*;?\s*$', search_text, re.S)
if not match:
    ERRORS.append('search-index.js assignment is invalid')
    search_entries = []
else:
    try:
        search_entries = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        ERRORS.append(f'search-index.js JSON is invalid: {exc}')
        search_entries = []
if len(search_entries) != required_counts['search_entries']:
    ERRORS.append(f'search entries: expected {required_counts["search_entries"]}, got {len(search_entries)}')
search_blob = '\n'.join(json.dumps(item, sort_keys=True) for item in search_entries)
for symbol in manifest['expected']['functions']:
    if symbol not in search_blob:
        ERRORS.append(f'search missing function: {symbol}')
for node_id in manifest['expected']['tests']:
    if node_id.split('::', 1)[1] not in search_blob:
        ERRORS.append(f'search missing test: {node_id}')

source_html = (ROOT / 'source-coverage.html').read_text(encoding='utf-8')
for relative in manifest['expected']['source_manifest_files']:
    if relative not in source_html:
        ERRORS.append(f'source coverage missing: {relative}')

checksum_path = ROOT / 'SHA256SUMS.txt'
if not checksum_path.is_file():
    ERRORS.append('SHA256SUMS.txt is missing')
else:
    listed: dict[str, str] = {}
    for line in checksum_path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        digest, relative = line.split('  ', 1)
        listed[relative] = digest
    actual_files = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob('*') if path.is_file() and path.name != 'SHA256SUMS.txt')
    if sorted(listed) != actual_files:
        missing = sorted(set(actual_files) - set(listed))
        stale = sorted(set(listed) - set(actual_files))
        ERRORS.append(f'checksum file inventory mismatch; missing={missing}, stale={stale}')
    for relative, expected in listed.items():
        target = ROOT / relative
        if target.is_file() and sha256(target) != expected:
            ERRORS.append(f'checksum mismatch: {relative}')

if ERRORS:
    print('\n'.join(ERRORS), file=sys.stderr)
    raise SystemExit(1)

print(json.dumps({
    'status': 'pass',
    'html_pages': len(html_files),
    'search_entries': len(search_entries),
    'counts': manifest['counts'],
    'source_audit_checks': audit['counts']['checks'],
    'source_audit_failures': audit['counts']['failed_checks'],
}, indent=2, sort_keys=True))
