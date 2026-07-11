from __future__ import annotations
import argparse, json, os, subprocess, sys, xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ISOLATED={'tests/test_linker_metadata_corpus.py','tests/test_production.py'}

def env(root: Path):
    e=os.environ.copy(); e['PYTHONPATH']=os.pathsep.join([str(root/'src'),str(root/'test-suite/src'),e.get('PYTHONPATH','')]); e['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'; e['PYTHONDONTWRITEBYTECODE']='1'; return e

def collect(root,e):
    p=subprocess.run([sys.executable,'-m','pytest','--collect-only','-q','tests','test-suite/tests','test-suite/src/x86decomp_testkit/toolkit_tests','-p','no:cacheprovider'],cwd=root,env=e,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=300)
    if p.returncode: raise SystemExit(p.stdout)
    ids=[x.strip() for x in p.stdout.splitlines() if '::' in x and not x.startswith('<')]
    g=defaultdict(list)
    for n in ids:g[n.split('::',1)[0]].append(n)
    parts=[]
    for f in sorted(g):
        if f in ISOLATED: parts += [(n,[n]) for n in g[f]]
        else: parts.append((f,[f]))
    return ids,parts

def counts(path):
    r=ET.parse(path).getroot(); suites=[r] if r.tag=='testsuite' else list(r.findall('.//testsuite'))
    return {k:sum(int(s.attrib.get(k,0)) for s in suites) for k in ('tests','failures','errors','skipped')}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--start',type=int,required=True); ap.add_argument('--end',type=int,required=True); ap.add_argument('--timeout',type=int,default=600); a=ap.parse_args()
    root=a.root.resolve(); out=a.out.resolve(); out.mkdir(parents=True,exist_ok=True); e=env(root)
    ids,parts=collect(root,e)
    (out/'collection.json').write_text(json.dumps({'node_ids':ids,'partition_count':len(parts),'partitions':[{'index':i,'name':n,'targets':t} for i,(n,t) in enumerate(parts,1)]},indent=2)+'\n')
    for i in range(a.start,min(a.end,len(parts))+1):
        name,targets=parts[i-1]; j=out/f'{i:03d}.xml'; l=out/f'{i:03d}.log'; rec=out/f'{i:03d}.json'
        if rec.exists():
            old=json.loads(rec.read_text());
            if old.get('returncode')==0 and not any(old.get(k) for k in ('failures','errors','skipped')): print(f'{i}/{len(parts)} already clean {name}',flush=True); continue
        cmd=[sys.executable,'-m','pytest','-q',*targets,'-p','no:cacheprovider',f'--junitxml={j}']
        try:
            p=subprocess.run(cmd,cwd=root,env=e,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=a.timeout)
            l.write_text(p.stdout,encoding='utf-8',errors='replace')
            c=counts(j) if j.exists() else {'tests':0,'failures':0,'errors':1,'skipped':0}
            r={'index':i,'partition':name,'targets':targets,'command':cmd,'returncode':p.returncode,**c,'output_tail':p.stdout[-4000:]}
        except subprocess.TimeoutExpired as ex:
            outtxt=(ex.stdout or '')+(ex.stderr or '') if isinstance(ex.stdout,str) else ''
            l.write_text(outtxt,encoding='utf-8',errors='replace'); r={'index':i,'partition':name,'targets':targets,'command':cmd,'returncode':124,'tests':0,'failures':0,'errors':1,'skipped':0,'timeout':True,'output_tail':outtxt[-4000:]}
        rec.write_text(json.dumps(r,indent=2)+'\n')
        print(f"{i}/{len(parts)} rc={r['returncode']} tests={r['tests']} fail={r['failures']} err={r['errors']} skip={r['skipped']} {name}",flush=True)
        if r['returncode'] or r['failures'] or r['errors'] or r['skipped']: return 2
    return 0
if __name__=='__main__': raise SystemExit(main())
