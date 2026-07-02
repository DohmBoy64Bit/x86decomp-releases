#!/usr/bin/env python3
"""Install the source-verified x86decomp 0.7.4 Project Examples Suite into an extracted static docs site."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, html.parser, json, re, shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit
PATCH_ID="x86decomp-project-examples-suite-v2"; ROOT_PAGE="project-examples.html"
class Parser(html.parser.HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        d=dict(attrs); ident=d.get('id')
        if ident:self.ids.add(ident)
        if tag=='a' and d.get('name'):self.ids.add(d['name'])
        for a in ('href','src'):
            if d.get(a):self.links.append((a,d[a]))
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def site_files(root):
    for p in root.rglob('*'):
        if not p.is_file() or any(x.startswith('.project-examples-suite-backup-') or x.startswith('.project-examples-backup-') for x in p.parts):continue
        if p.name in {'SHA256SUMS.txt','MANIFEST.sha256','SITE_MANIFEST.sha256'}:continue
        yield p
def backup(root,paths):
    b=root/f'.project-examples-suite-backup-{dt.datetime.now().strftime("%Y%m%dT%H%M%S")}'
    i=1
    while b.exists():b=root/f'.project-examples-suite-backup-{dt.datetime.now().strftime("%Y%m%dT%H%M%S")}-{i}';i+=1
    b.mkdir(parents=True)
    for p in paths:
        if p.is_file():
            q=b/p.relative_to(root);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
    return b
def patch_nav(text, *, current=False):
    # Remove duplicate Project examples links, then add exactly one after Workflows.
    text=re.sub(r'<a href="(?:\.\./)*project-examples\.html"[^>]*>Project examples</a>','',text)
    pat=re.compile(r'(<a href="(?P<p>(?:\.\./)*)workflows\.html"[^>]*>Workflows</a>)')
    current_attr=' aria-current="page"' if current else ''
    return pat.sub(lambda m:m.group(1)+f'<a href="{m.group("p")}project-examples.html"{current_attr}>Project examples</a>',text,count=1)
def patch_home(text):
    # Remove v1 or v2 project-example cards and add one current suite card after Workflows.
    text=re.sub(r'\s*<a class="card link-card" href="project-examples\.html">.*?</a>','',text,flags=re.S)
    card='\n<a class="card link-card" href="project-examples.html"><div class="card-title">Explore project examples</div><p>Use source-verified matching, functional, hybrid, analysis, compiler, patching, relinking, ABI, release, benchmark, and recovery workflows.</p></a>'
    return re.sub(r'(<a class="card link-card" href="workflows\.html">.*?</a>)',lambda m:m.group(1)+card,text,count=1,flags=re.S)
def patch_workflows(text):
    text=re.sub(r'\s*<section class="callout success"><strong>(?:Complete hybrid project example\.|Source-verified project examples\.)</strong>.*?</section>','',text,flags=re.S)
    block='\n<section class="callout success"><strong>Source-verified project examples.</strong> See <a href="project-examples.html">Project examples</a> for matching, functional, both-mode hybrid, and major supporting workflows grounded in the 0.7.4 source.</section>\n'
    return re.sub(r'(\s*<footer class="page-footer">)',block+r'\1',text,count=1)
def patch_search(path,entries):
    if not path.is_file():return 'search index not present'
    text=read(path); m=re.match(r'(?s)(.*?=\s*)(\[.*\])(\s*;\s*)$',text)
    if not m:return 'search index format not recognized'
    try:data=json.loads(m.group(2))
    except Exception:return 'search index JSON array could not be parsed'
    data=[x for x in data if not str(x.get('href',x.get('url',''))).startswith('project-examples')]
    data.extend(entries)
    write(path,m.group(1)+json.dumps(data,ensure_ascii=False,separators=(',',':'))+m.group(3))
    return f'installed {len(entries)} project-example entries'
def validate(root):
    errors=[]; cache={}
    for page in root.rglob('*.html'):
        if any(x.startswith('.') and 'backup' in x for x in page.parts):continue
        p=Parser();p.feed(read(page))
        for attr,raw in p.links:
            u=urlsplit(raw)
            if u.scheme in {'http','https','mailto','tel','data','javascript'} or raw.startswith('//'):continue
            pp=unquote(u.path);frag=unquote(u.fragment)
            target=page if not pp else ((root/pp.lstrip('/')) if pp.startswith('/') else (page.parent/pp).resolve())
            try:target.relative_to(root.resolve())
            except ValueError:errors.append({'page':str(page.relative_to(root)),'value':raw,'error':'escapes site root'});continue
            if pp and not target.exists():errors.append({'page':str(page.relative_to(root)),'value':raw,'error':'missing target'});continue
            if frag and target.suffix.lower() in {'.html','.htm'} and target.exists():
                if target not in cache:q=Parser();q.feed(read(target));cache[target]=q.ids
                if frag not in cache[target]:errors.append({'page':str(page.relative_to(root)),'value':raw,'error':'missing fragment'})
    return errors
def refresh(root,names):
    payload='\n'.join(f'{sha(p)}  {p.relative_to(root).as_posix()}' for p in sorted(site_files(root),key=lambda x:x.relative_to(root).as_posix()))+'\n'
    for n in names:write(root/n,payload)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('site_root',type=Path);ap.add_argument('--no-backup',action='store_true');a=ap.parse_args()
    here=Path(__file__).resolve().parent;payload=here/'payload';root=a.site_root.expanduser().resolve()
    req=[root/'index.html',root/'assets'/'styles.css'];missing=[str(p) for p in req if not p.exists()]
    if missing:ap.error('not an x86decomp docs site root; missing: '+', '.join(missing))
    installed=[p.relative_to(payload) for p in payload.rglob('*') if p.is_file()]
    touched=[root/r for r in installed]+list(root.rglob('*.html'))+[root/'assets'/'search-index.js',root/'PROJECT_EXAMPLES_VERIFICATION.json',root/'PROJECT_EXAMPLES_VERIFICATION.md']
    b=(backup(root,touched) if not a.no_backup else root/'.project-examples-suite-backup-disabled')
    # Remove old suite directory to guarantee no stale pages, then copy payload.
    if (root/'project-examples').exists():shutil.rmtree(root/'project-examples')
    for p in payload.rglob('*'):
        if p.is_file():q=root/p.relative_to(payload);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
    changed=[r.as_posix() for r in installed]
    for p in [x for x in root.rglob('*.html') if not any('backup' in y and y.startswith('.') for y in x.parts)]:
        t=read(p);u=patch_nav(t,current=(p==root/ROOT_PAGE or (root/'project-examples') in p.parents))
        if p==root/'index.html':u=patch_home(u)
        if p==root/'workflows.html':u=patch_workflows(u)
        if u!=t:write(p,u);changed.append(p.relative_to(root).as_posix())
    msg=patch_search(root/'assets'/'search-index.js',json.loads(read(here/'SEARCH_ENTRIES.json')));changed.append('assets/search-index.js')
    errors=validate(root);names=[n for n in ('SHA256SUMS.txt','MANIFEST.sha256','SITE_MANIFEST.sha256') if (root/n).exists()]
    active_html=[p for p in root.rglob('*.html') if not any('backup' in y and y.startswith('.') for y in p.parts)]
    def sidebar_project_link_count(page):
        match=re.search(r'<aside class="sidebar".*?</aside>',read(page),flags=re.S)
        if not match:return 0
        return len(re.findall(r'<a href="(?:\.\./)*project-examples\.html"[^>]*>Project examples</a>',match.group(0)))
    checks={'landing_present':(root/ROOT_PAGE).is_file(),'detailed_example_pages':len(list((root/'project-examples').glob('*.html')))==12,'source_audit_json_present':(root/'PROJECT_EXAMPLES_SOURCE_AUDIT.json').is_file(),'local_links_and_fragments_valid':not errors,'zero_placeholder_markers':not any(re.search(r'\b(TODO|TBD|FIXME|COMING SOON)\b',read(p),re.I) for p in [root/ROOT_PAGE,*sorted((root/'project-examples').glob('*.html'))]),'single_navigation_entry':all(sidebar_project_link_count(p)==1 for p in active_html)}
    report={'format':'x86decomp-project-examples-docs-patch-v2','patch_id':PATCH_ID,'target_release':'0.7.4','applied_at':dt.datetime.now(dt.timezone.utc).isoformat(),'status':'pass' if all(checks.values()) and not errors else 'fail','backup_directory':b.name,'installed_pages':sorted(str(r) for r in installed if r.suffix=='.html'),'changed_files':sorted(set(changed)),'search_index':msg,'refreshed_hash_manifests':names,'checks':checks,'link_errors':errors,'truth_boundary':'This report verifies installation, navigation, search replacement, placeholder scan, local links, and site checksums. Source semantics are separately recorded in PROJECT_EXAMPLES_SOURCE_AUDIT.json and the patch source-verification report.'}
    write(root/'PROJECT_EXAMPLES_VERIFICATION.json',json.dumps(report,indent=2)+'\n')
    md=['# Project Examples Suite verification','',f'- Patch: `{PATCH_ID}`',f'- Status: **{report["status"].upper()}**',f'- Backup: `{b.name}`',f'- Search index: {msg}','','## Checks','']+[f'- {"PASS" if v else "FAIL"} — `{k}`' for k,v in report['checks'].items()]+['','## Truth boundary','',report['truth_boundary'],'']
    if errors:md+=['## Link errors','','```json',json.dumps(errors,indent=2),'```','']
    write(root/'PROJECT_EXAMPLES_VERIFICATION.md','\n'.join(md))
    refresh(root,names)
    print(f'Applied {PATCH_ID} '+('successfully.' if not errors else f'with {len(errors)} link error(s).'))
    print(f'Landing page: {root/ROOT_PAGE}');print(f'Backup: {b}');print('Verification: PROJECT_EXAMPLES_VERIFICATION.json')
    return 0 if not errors else 2
if __name__=='__main__':raise SystemExit(main())
