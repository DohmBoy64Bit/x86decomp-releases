#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'coverage-manifest.json').read_text())
errors=[]
for key in ('root_commands','canonical_routes','features','functions','test_suite_commands','tests','schemas','adapters'):
    expected=manifest['expected'][key]
    actual=manifest['documented'][key]
    if expected != actual:
        errors.append(f'{key}: expected/documented mismatch')
counts=manifest['counts']
required={'root_commands':140,'runnable_command_paths':280,'test_suite_commands':5,'all_command_paths':285,'canonical_routes':173,'features':137,'functions':983,'tests':215,'schemas':93,'adapters':31}
for key,value in required.items():
    if counts.get(key)!=value: errors.append(f'{key}: expected {value}, got {counts.get(key)}')
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        data=dict(attrs)
        if 'id' in data: self.ids.add(data['id'])
        if tag=='a' and 'href' in data: self.links.append(data['href'])
html_files=list(ROOT.rglob('*.html'))
parsed={}
for path in html_files:
    parser=Links(); parser.feed(path.read_text(encoding='utf-8')); parsed[path]=parser
for path,parser in parsed.items():
    for href in parser.links:
        if href.startswith(('http:','https:','mailto:','javascript:')): continue
        target,fragment=urldefrag(href)
        resolved=(path.parent/target).resolve() if target else path.resolve()
        try: resolved.relative_to(ROOT.resolve())
        except ValueError: errors.append(f'{path.relative_to(ROOT)}: link escapes site: {href}'); continue
        if not resolved.exists(): errors.append(f'{path.relative_to(ROOT)}: broken link: {href}'); continue
        if fragment and resolved.suffix=='.html':
            target_parser=parsed.get(resolved)
            if target_parser is None:
                target_parser=Links(); target_parser.feed(resolved.read_text(encoding='utf-8')); parsed[resolved]=target_parser
            if fragment not in target_parser.ids: errors.append(f'{path.relative_to(ROOT)}: missing fragment: {href}')
for path in ROOT.rglob('*'):
    if path.name == 'verify_site.py': continue
    if not path.is_file() or path.suffix.lower() not in {'.html','.js','.css','.md','.json','.py','.txt'}: continue
    text=path.read_text(encoding='utf-8',errors='replace')
    for pattern in (r'\bTODO\b',r'\bTBD\b',r'lorem ipsum',r'coming soon',r'insert (?:text|content) here'):
        if re.search(pattern,text,re.I): errors.append(f'{path.relative_to(ROOT)}: unfinished-content marker {pattern}')
search=(ROOT/'assets/search-index.js').read_text(encoding='utf-8')
for symbol in manifest['expected']['functions']:
    if symbol not in search: errors.append(f'search index missing function: {symbol}')
for node in manifest['expected']['tests']:
    name=node.split('::',1)[1]
    if name not in search: errors.append(f'search index missing test: {node}')
if errors:
    print('\n'.join(errors),file=sys.stderr); raise SystemExit(1)
print(json.dumps({'status':'pass','html_files':len(html_files),'counts':counts},indent=2,sort_keys=True))
