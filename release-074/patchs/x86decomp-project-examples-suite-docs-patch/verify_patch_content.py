#!/usr/bin/env python3
"""Verify the Project Examples Suite payload structure and critical v0.7.4 truth disclosures."""
from __future__ import annotations
import html.parser,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent; PAYLOAD=HERE/'payload'
PAGES=['matching-project','functional-project','hybrid-project','static-analysis-evidence','compiler-laboratory','patch-image-integration','full-relink-convergence','abi-type-recovery','target-release-reproducibility','benchmark-validation-corpus','project-operations-recovery']
class Text(html.parser.HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.text=[]
 def handle_data(self,d):self.text.append(d)
def page_text(p):q=Text();q.feed(p.read_text(encoding='utf-8'));return ' '.join(' '.join(q.text).split())
def main():
 failures=[]; metrics={}
 for name in PAGES:
  p=PAYLOAD/'project-examples'/f'{name}.html'
  if not p.is_file():failures.append(f'missing page: {name}');continue
  raw=p.read_text(encoding='utf-8'); txt=page_text(p); words=len(txt.split())
  metrics[name]={'words':words,'svg_count':raw.count('<svg'),'command_count':len(re.findall(r'\bx86decomp\s+[a-z0-9-]+',txt)),'source_rows':raw.count('<tr>')-1}
  for marker in ('id="source-basis"',):
   if marker not in raw and marker not in txt:failures.append(f'{name}: missing {marker}')
  if not any(x in txt for x in ('Truth boundary','Hard constraints','What a passing functional project means','What this project does not prove','Hybrid truth boundaries')):failures.append(f'{name}: missing bounded-claims section')
  if words<650:failures.append(f'{name}: insufficient detail ({words} words)')
  if '<svg' not in raw:failures.append(f'{name}: missing workflow graph')
  if re.search(r'\b(TODO|TBD|FIXME|COMING SOON)\b',txt,re.I):failures.append(f'{name}: placeholder marker')
 critical={
  'hybrid-project':['not a third mode enum','selected_modes'],
  'patch-image-integration':['candidate file length defines how many bytes are overwritten','does not know function boundaries'],
  'target-release-reproducibility':['legacy per-function modes object','selected_modes'],
  'static-analysis-evidence':['does not parse the referenced report files'],
  'matching-project':['do not automatically promote a function workflow'],
  'functional-project':['supplied concrete harness'],
 }
 for name,phrases in critical.items():
  txt=page_text(PAYLOAD/'project-examples'/f'{name}.html').lower()
  for phrase in phrases:
   if phrase.lower() not in txt:failures.append(f'{name}: missing critical disclosure: {phrase}')
 entries=json.loads((HERE/'SEARCH_ENTRIES.json').read_text())
 hrefs=[e.get('href') for e in entries]
 if len(entries)!=13 or len(set(hrefs))!=13:failures.append('search entries must contain 13 unique hrefs')
 audit=json.loads((HERE/'SOURCE_AUDIT.json').read_text())
 anchors=sum(len(v) for v in audit['pages'].values()); files=len({e['path'] for v in audit['pages'].values() for e in v})
 metrics['source_audit']={'anchors':anchors,'unique_files':files}
 if anchors<90 or files<45:failures.append('source audit coverage below expected floor')
 result={'format':'x86decomp-project-examples-content-verification-v1','target_release':'0.7.4','status':'pass' if not failures else 'fail','example_pages':len(PAGES),'metrics':metrics,'failures':failures}
 print(json.dumps(result,indent=2));return 0 if not failures else 2
if __name__=='__main__':raise SystemExit(main())
