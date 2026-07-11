import json,re
from pathlib import Path
root=Path('/mnt/data/x86decomp-audit-work/x86decomp-toolkit-0.7.11')
cmd=json.load(open('/mnt/data/x86decomp-audit-external/command_audit.json'))
files=list((root/'docs').glob('*.md'))+[root/'README.md',root/'VERIFICATION.md',root/'SECURITY.md',root/'PROJECT_MEMORY.md']
texts={p.relative_to(root).as_posix():p.read_text(encoding='utf-8') for p in files}
alltext='\n'.join(texts.values())
blocks=[]
for path,text in texts.items():
 lines=text.splitlines(); inside=False; lang=''; buf=[]; start=0
 for i,line in enumerate(lines,1):
  if line.startswith('```'):
   if not inside: inside=True; lang=line[3:].strip(); buf=[]; start=i+1
   else:
    blocks.append((path,start,lang,'\n'.join(buf))); inside=False
   continue
  if inside:buf.append(line)
code='\n'.join(b[3] for b in blocks if b[2] in {'','bash','sh','console','shell'})
# Match command prefix allowing arguments after it; avoid group prefix counting child command as group example separately (we retain both metrics)
for c in cmd['commands']:
 full='x86decomp '+c['command']
 pat=re.compile(r'(?m)^\s*'+re.escape(full)+r'(?:\s|$)')
 c['documented_files']=[p for p,t in texts.items() if pat.search(t)]
 c['example_files']=[p for p,s,l,t in blocks if l in {'','bash','sh','console','shell'} and pat.search(t)]
for r in cmd['canonical_routes']:
 full=f"x86decomp {r['group']} {r['action']}"; pat=re.compile(r'(?m)^\s*'+re.escape(full)+r'(?:\s|$)')
 r['documented_files']=[p for p,t in texts.items() if pat.search(t)];r['example_files']=[p for p,s,l,t in blocks if l in {'','bash','sh','console','shell'} and pat.search(t)]
rootcmd=[c for c in cmd['commands'] if len(c['command'].split())==1]
summary={'parser_nodes':len(cmd['commands']),'root_commands':len(rootcmd),'root_documented':sum(bool(c['documented_files']) for c in rootcmd),'root_examples':sum(bool(c['example_files']) for c in rootcmd),'all_nodes_documented':sum(bool(c['documented_files']) for c in cmd['commands']),'all_nodes_examples':sum(bool(c['example_files']) for c in cmd['commands']),'canonical_routes':len(cmd['canonical_routes']),'routes_documented':sum(bool(r['documented_files']) for r in cmd['canonical_routes']),'routes_examples':sum(bool(r['example_files']) for r in cmd['canonical_routes']),'code_blocks':len(blocks)}
out={'summary':summary,'commands':cmd['commands'],'canonical_routes':cmd['canonical_routes']}
Path('/mnt/data/x86decomp-audit-external/command_docs_coverage.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps(summary,indent=2))
print('root missing examples', [c['command'] for c in rootcmd if not c['example_files']][:120])
