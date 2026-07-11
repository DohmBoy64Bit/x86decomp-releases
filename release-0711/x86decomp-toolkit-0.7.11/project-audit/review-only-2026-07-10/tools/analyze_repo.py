from __future__ import annotations
import ast,csv,hashlib,json,os,re,sys
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path('/mnt/data/x86decomp-audit-work/x86decomp-toolkit-0.7.11')
OUT=Path('/mnt/data/x86decomp-audit-external/repo_analysis.json')

WRITE_CALLS={'write_text','write_bytes','mkdir','unlink','rmdir','rename','replace','touch','chmod','symlink_to','hardlink_to'}
RISK_CALLS={'eval','exec','compile','pickle.loads','pickle.load','yaml.load','subprocess.run','subprocess.Popen','subprocess.call','subprocess.check_call','subprocess.check_output','os.system','os.popen','shutil.rmtree','shutil.unpack_archive','tarfile.extractall','zipfile.extractall','socket.socket','urllib.request.urlopen','requests.get','requests.post','httpx.get','httpx.post','sqlite3.connect','tempfile.mktemp'}
DANGEROUS_C={'gets','strcpy','strcat','sprintf','vsprintf','system','popen','scanf','sscanf'}

def qual(call):
    n=call.func
    parts=[]
    while isinstance(n,ast.Attribute): parts.append(n.attr); n=n.value
    if isinstance(n,ast.Name): parts.append(n.id)
    return '.'.join(reversed(parts))

def classify(rel,suf):
    s=rel.as_posix()
    if s.startswith('project-audit/'): return 'Audit artifact'
    if s.startswith('tests/') or '/tests/' in s or s.startswith('test-suite/'): return 'Test code' if suf in {'.py','.sh','.ps1'} else 'Test fixture/data'
    if s.startswith('src/') and suf=='.py': return 'First-party source code'
    if s.startswith('scripts/') or s.startswith('.github/'): return 'Build or automation'
    if s.startswith('schemas/') or '/schemas/' in s: return 'Configuration/schema'
    if s.startswith('docs/') or suf=='.md': return 'Documentation'
    if s.startswith('examples/'): return 'Example or sample'
    if s.startswith('corpus/') or '/corpus/' in s: return 'Fixture or test data'
    if suf in {'.toml','.cfg','.yml','.yaml','.in'} or rel.name in {'.gitignore','Makefile'}: return 'Configuration/build'
    if suf in {'.json','.csv','.sha256','.txt'}: return 'Generated artifact or data'
    if suf in {'.bin'}: return 'Binary fixture'
    if suf in {'.c','.cpp','.java'}: return 'First-party source code'
    return 'Unknown'

def expr_const(v):
    try:return ast.literal_eval(v)
    except Exception:return None

def norm_func(node):
    # canonicalize function AST excluding name, positions, docstring
    n=ast.fix_missing_locations(ast.parse(ast.unparse(node)).body[0])
    n.name='_'
    if getattr(n,'body',None) and isinstance(n.body[0],ast.Expr) and isinstance(n.body[0].value,ast.Constant) and isinstance(n.body[0].value.value,str): n.body=n.body[1:]
    for x in ast.walk(n):
        for a in ('lineno','col_offset','end_lineno','end_col_offset','type_comment'):
            if hasattr(x,a):
                try: delattr(x,a)
                except Exception: pass
    return hashlib.sha256(ast.dump(n,include_attributes=False).encode()).hexdigest(),len(list(ast.walk(n)))

files=[]; pydefs=[]; imports_by_file={}; calls_by_file={}; duplicate_buckets=defaultdict(list); all_text={}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT); b=p.read_bytes(); sha=hashlib.sha256(b).hexdigest(); rec={'path':rel.as_posix(),'sha256':sha,'size':len(b),'extension':p.suffix.lower(),'classification':classify(rel,p.suffix.lower())}
    try:
        text=b.decode('utf-8'); rec['text_or_binary']='text'; rec['lines']=text.count('\n')+(1 if text and not text.endswith('\n') else 0); all_text[rel.as_posix()]=text
    except UnicodeDecodeError:
        rec['text_or_binary']='binary'; rec['lines']=None; text=None
    if text is not None:
        rec['todo_markers']=[{'line':i,'text':line.strip()[:300]} for i,line in enumerate(text.splitlines(),1) if re.search(r'\b(TODO|FIXME|XXX|HACK)\b',line,re.I)]
        rec['trailing_whitespace_lines']=[i for i,line in enumerate(text.splitlines(),1) if line.rstrip(' \t')!=line]
        rec['long_lines']=[i for i,line in enumerate(text.splitlines(),1) if len(line)>140]
        if p.suffix=='.json':
            try:
                obj=json.loads(text); rec['json_valid']=True; rec['json_top_type']=type(obj).__name__; rec['json_top_keys']=list(obj)[:50] if isinstance(obj,dict) else None
            except Exception as e: rec['json_valid']=False; rec['json_error']=f'{type(e).__name__}: {e}'
        if p.suffix=='.py':
            try:
                tree=ast.parse(text,filename=str(rel)); rec['python_parse']=True
            except SyntaxError as e:
                rec['python_parse']=False; rec['syntax_error']=f'{e.msg} line {e.lineno}'; files.append(rec); continue
            parent={}
            for n in ast.walk(tree):
                for c in ast.iter_child_nodes(n): parent[c]=n
            module_doc=ast.get_docstring(tree,clean=False); rec['module_docstring']=bool(module_doc)
            defs=[]; imports=[]; calls=[]; broad=[]; passes=[]; asserts=[]; globals_=[]
            for n in ast.walk(tree):
                if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
                    # build rough qualname
                    names=[n.name]; q=parent.get(n)
                    while q:
                        if isinstance(q,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): names.append(q.name)
                        q=parent.get(q)
                    qn='.'.join(reversed(names)); doc=ast.get_docstring(n,clean=False)
                    d={'kind':'class' if isinstance(n,ast.ClassDef) else ('async_function' if isinstance(n,ast.AsyncFunctionDef) else 'function'),'name':n.name,'qualname':qn,'line':n.lineno,'end_line':getattr(n,'end_lineno',n.lineno),'docstring':bool(doc),'docstring_first':doc.splitlines()[0] if doc else None}
                    if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
                        d['args']=[a.arg for a in [*n.args.posonlyargs,*n.args.args,*n.args.kwonlyargs]]; d['branch_nodes']=sum(isinstance(x,(ast.If,ast.For,ast.AsyncFor,ast.While,ast.Try,ast.BoolOp,ast.Match,ast.comprehension)) for x in ast.walk(n)); d['node_count']=len(list(ast.walk(n)))
                        h,nc=norm_func(n); d['normalized_hash']=h
                        if nc>=12: duplicate_buckets[h].append((rel.as_posix(),qn,n.lineno,nc))
                    defs.append(d); pydefs.append((rel.as_posix(),d))
                elif isinstance(n,(ast.Import,ast.ImportFrom)):
                    if isinstance(n,ast.Import): imports += [a.name for a in n.names]
                    else: imports += [(('.'*n.level)+(n.module or ''))]
                elif isinstance(n,ast.Call):
                    q=qual(n); item={'name':q,'line':n.lineno}
                    if q in {'subprocess.run','subprocess.Popen','subprocess.call','subprocess.check_call','subprocess.check_output'}:
                        sh=None
                        for kw in n.keywords:
                            if kw.arg=='shell': sh=expr_const(kw.value)
                        item['shell']=sh
                    if q.endswith('.execute') or q.endswith('.executemany'):
                        item['sql_constant']=isinstance(n.args[0],ast.Constant) and isinstance(n.args[0].value,str) if n.args else None
                    if q in RISK_CALLS or any(q.endswith('.'+x) for x in WRITE_CALLS) or q.endswith('.execute') or q.endswith('.executemany'): calls.append(item)
                elif isinstance(n,ast.ExceptHandler):
                    typ=ast.unparse(n.type) if n.type else 'bare'
                    if typ in {'bare','Exception','BaseException'}: broad.append({'line':n.lineno,'type':typ,'body':ast.unparse(ast.Module(body=n.body,type_ignores=[]))[:500]})
                elif isinstance(n,ast.Pass): passes.append(n.lineno)
                elif isinstance(n,ast.Assert): asserts.append(n.lineno)
                elif isinstance(n,(ast.Global,ast.Nonlocal)): globals_.append({'line':n.lineno,'names':n.names,'kind':type(n).__name__})
            rec.update({'definitions':defs,'imports':sorted(set(imports)),'risk_calls':calls,'broad_exceptions':broad,'pass_lines':passes,'assert_lines':asserts,'global_state_decls':globals_})
            imports_by_file[rel.as_posix()]=sorted(set(imports)); calls_by_file[rel.as_posix()]=calls
        elif p.suffix in {'.c','.cpp','.java'}:
            rec['dangerous_api_lines']=[{'line':i,'text':line.strip()[:250]} for i,line in enumerate(text.splitlines(),1) if any(re.search(r'\b'+re.escape(fn)+r'\s*\(',line) for fn in DANGEROUS_C)]
            rec['includes']=[m.group(1) for m in re.finditer(r'^\s*#include\s*[<"]([^>"]+)',text,re.M)]
        elif p.suffix=='.md':
            rec['headings']=[{'line':i,'heading':line.strip()} for i,line in enumerate(text.splitlines(),1) if line.startswith('#')]
            links=[]
            for i,line in enumerate(text.splitlines(),1):
                for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',line): links.append({'line':i,'target':m.group(1)})
            rec['markdown_links']=links
    files.append(rec)

# test references by module stem and symbol names
all_tests='\n'.join(t for p,t in all_text.items() if p.startswith('tests/') or '/tests/' in p or p.startswith('test-suite/'))
for rec in files:
    if rec.get('extension')=='.py' and rec['classification']=='First-party source code':
        stem=Path(rec['path']).stem; rec['test_reference_count']=len(re.findall(r'\b'+re.escape(stem)+r'\b',all_tests))
        syms=[d['name'] for d in rec.get('definitions',[]) if not d['name'].startswith('_')]
        rec['public_symbol_test_refs']={s:len(re.findall(r'\b'+re.escape(s)+r'\b',all_tests)) for s in syms}

# duplicate groups
dups=[]
for h,items in duplicate_buckets.items():
    if len(items)>1:
        # omit same file nested variants only if identical methods? keep
        dups.append({'hash':h,'members':[{'path':a,'symbol':b,'line':c,'nodes':d} for a,b,c,d in items]})

# markdown local link checking
broken=[]
for rec in files:
    if rec.get('extension')!='.md':continue
    base=(ROOT/rec['path']).parent
    for l in rec.get('markdown_links',[]):
        target=l['target'].split('#',1)[0]
        if not target or re.match(r'^[a-z]+://',target,re.I) or target.startswith('mailto:'):continue
        if not (base/target).resolve().exists(): broken.append({'path':rec['path'],'line':l['line'],'target':target})

# dependency import roots
imports=Counter()
for vals in imports_by_file.values():
    for x in vals:
        y=x.lstrip('.').split('.',1)[0]
        if y: imports[y]+=1

out={'root':str(ROOT),'file_count':len(files),'files':files,'duplicate_functions':dups,'broken_markdown_links':broken,'import_roots':imports.most_common(),'full_text_read_count':len(all_text),'binary_count':sum(f['text_or_binary']=='binary' for f in files)}
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'files':len(files),'text':len(all_text),'binary':out['binary_count'],'pydefs':len(pydefs),'dups':len(dups),'broken_links':len(broken)},indent=2))
