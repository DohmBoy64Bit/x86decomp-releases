from __future__ import annotations
import argparse,json,os,re,sys
from pathlib import Path
ROOT=Path('/mnt/data/x86decomp-audit-work/x86decomp-toolkit-0.7.11')
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'test-suite/src')]
from x86decomp.cli import _build_parser
from x86decomp.canonical import canonical_routes,canonical_groups

def action_info(a):
    choices=list(a.choices) if getattr(a,'choices',None) is not None and not isinstance(a,argparse._SubParsersAction) else None
    return {'dest':a.dest,'option_strings':a.option_strings,'required':getattr(a,'required',False),'nargs':a.nargs,'default':None if a.default is argparse.SUPPRESS else a.default,'choices':choices,'help':a.help,'type':getattr(a.type,'__name__',str(a.type)) if a.type else None}

def walk_parser(parser,prefix=[]):
    out=[]
    sub=next((a for a in parser._actions if isinstance(a,argparse._SubParsersAction)),None)
    if not sub:return out
    for name,child in sorted(sub.choices.items()):
        info={'command':' '.join(prefix+[name]),'name':name,'help':None,'description':child.description,'arguments':[action_info(a) for a in child._actions if not isinstance(a,(argparse._HelpAction,argparse._SubParsersAction))]}
        # argparse stores help on pseudoaction
        for ca in sub._choices_actions:
            if ca.dest==name:info['help']=ca.help
        out.append(info); out+=walk_parser(child,prefix+[name])
    return out

p=_build_parser(); commands=walk_parser(p)
doc_text='\n'.join(x.read_text(encoding='utf-8') for x in list((ROOT/'docs').glob('*.md'))+[ROOT/'README.md',ROOT/'VERIFICATION.md',ROOT/'SECURITY.md'])
code_blocks='\n'.join(re.findall(r'```(?:bash|console|sh)?\n(.*?)```',doc_text,re.S))
for c in commands:
    full='x86decomp '+c['command']
    c['mentioned_in_docs']=full in doc_text
    c['example_in_code_block']=full in code_blocks
    c['has_help']=bool(c['help'] and c['help'] is not argparse.SUPPRESS)
    c['has_description']=bool(c['description'])
    c['safety_flags']=[a['dest'] for a in c['arguments'] if a['dest'] in {'apply','allow_host_execution','allow_remote','yes','force','dry_run','expected_original_sha256','expected_function_sha256'}]
root_names=sorted(next(a for a in p._actions if isinstance(a,argparse._SubParsersAction)).choices)
routes=list(canonical_routes())
# docs occurrence for routes in canonical form
for r in routes:
    full=f"x86decomp {r['group']} {r['action']}"
    r['mentioned_in_docs']=full in doc_text; r['example_in_code_block']=full in code_blocks
report={'root_command_count':len(root_names),'parser_nodes':len(commands),'canonical_group_count':len(canonical_groups()),'canonical_route_count':len(routes),'root_commands':root_names,'commands':commands,'canonical_routes':routes,'summary':{'commands_with_help':sum(c['has_help'] for c in commands),'commands_with_description':sum(c['has_description'] for c in commands),'commands_mentioned_docs':sum(c['mentioned_in_docs'] for c in commands),'commands_with_examples':sum(c['example_in_code_block'] for c in commands),'routes_mentioned_docs':sum(r['mentioned_in_docs'] for r in routes),'routes_with_examples':sum(r['example_in_code_block'] for r in routes)}}
Path('/mnt/data/x86decomp-audit-external/command_audit.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(report['summary']|{'root':len(root_names),'nodes':len(commands),'groups':len(canonical_groups()),'routes':len(routes)},indent=2))
print('no help', [c['command'] for c in commands if not c['has_help']][:40])
print('root docs missing', [c['command'] for c in commands if len(c['command'].split())==1 and not c['mentioned_in_docs']][:60])
