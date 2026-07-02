#!/usr/bin/env python3
"""Verify that an extracted x86decomp source tree is the exact 0.7.4 source audited for this patch."""
from __future__ import annotations
import argparse,hashlib,json,re
from pathlib import Path

def sha(p:Path)->str:
 h=hashlib.sha256();h.update(p.read_bytes());return h.hexdigest()

def main()->int:
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source_root',type=Path);a=ap.parse_args()
 root=a.source_root.resolve();here=Path(__file__).resolve().parent
 audit=json.loads((here/'SOURCE_AUDIT.json').read_text(encoding='utf-8'))
 entries=[(page,e) for page,items in audit['pages'].items() for e in items]
 expected={e['path']:e['sha256'] for _,e in entries}; failures=[]; cache={}
 for rel,digest in sorted(expected.items()):
  p=root/rel
  if not p.is_file():failures.append({'path':rel,'error':'missing'});continue
  actual=sha(p)
  if actual!=digest:failures.append({'path':rel,'error':'sha256 mismatch','expected':digest,'actual':actual});continue
  cache[rel]=p.read_text(encoding='utf-8',errors='replace').splitlines()
 for page,e in entries:
  lines=cache.get(e['path'])
  if lines is None:continue
  start=e['line_start'];end=e['line_end']
  if start<1 or end<start or end>len(lines):
   failures.append({'path':e['path'],'page':page,'error':'invalid audit line range','line_start':start,'line_end':end,'line_count':len(lines)});continue
  excerpt=lines[start-1:end]
  if not any(e['needle'] in line for line in excerpt):
   failures.append({'path':e['path'],'page':page,'error':'audit anchor absent from declared line range','needle':e['needle'],'line_start':start,'line_end':end})
 version=None
 pyproject=root/'pyproject.toml'
 if pyproject.is_file():
  m=re.search(r'(?m)^version\s*=\s*["\']([^"\']+)["\']',pyproject.read_text(encoding='utf-8',errors='replace'))
  if m:version=m.group(1)
 if version!='0.7.4':failures.append({'path':'pyproject.toml','error':'release version is not 0.7.4','actual':version})
 result={'format':'x86decomp-project-examples-source-verification-v2','target_release':'0.7.4','detected_release':version,'source_root':str(root),'files_checked':len(expected),'anchors_checked':len(entries),'status':'pass' if not failures else 'fail','failures':failures}
 print(json.dumps(result,indent=2));return 0 if not failures else 2
if __name__=='__main__':raise SystemExit(main())
