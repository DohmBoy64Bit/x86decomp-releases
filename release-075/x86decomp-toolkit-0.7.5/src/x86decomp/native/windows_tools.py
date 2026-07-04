from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from x86decomp.contracts import canonical_json, random_id, utc_now
from .store import NativeStore


def discover_ghidra_launcher(ghidra_home:Path|None=None, *, platform_name:str|None=None)->Path|None:
    platform_name=(platform_name or os.name).lower(); homes=[]
    if ghidra_home is not None: homes.append(ghidra_home)
    if os.environ.get('GHIDRA_HOME'): homes.append(Path(os.environ['GHIDRA_HOME']))
    ordered=('analyzeHeadless.bat','analyzeHeadless') if platform_name in {'nt','windows','win32'} else ('analyzeHeadless','analyzeHeadless.bat')
    for home in homes:
        for name in ordered:
            candidate=home/'support'/name
            if candidate.is_file(): return candidate.resolve()
    for name in ordered:
        found=shutil.which(name)
        if found: return Path(found).resolve()
    return None


def write_response_file(path:Path,arguments:list[str])->dict[str,Any]:
    path=path.resolve(); path.parent.mkdir(parents=True,exist_ok=True)
    def quote(value:str)->str:
        if not value or any(ch.isspace() or ch=='"' for ch in value): return '"'+value.replace('\\','\\\\').replace('"','\\"')+'"'
        return value
    path.write_text('\n'.join(quote(item) for item in arguments)+'\n',encoding='utf-8')
    return {'path':str(path),'argument_count':len(arguments),'invocation':f'@{path}'}


class WindowsTools:
    def __init__(self,store:NativeStore): self.store=store; store.initialize()

    def doctor(self, *, ghidra_home:Path|None=None, actor:str='analyst')->dict[str,Any]:
        candidates={
            'ghidra': discover_ghidra_launcher(ghidra_home),
            'gcc': Path(found).resolve() if (found:=shutil.which('gcc')) else None,
            'clang': Path(found).resolve() if (found:=shutil.which('clang')) else None,
            'link': Path(found).resolve() if (found:=shutil.which('link')) else None,
            'lld-link': Path(found).resolve() if (found:=shutil.which('lld-link')) else None,
            'cdb': Path(found).resolve() if (found:=shutil.which('cdb')) else None,
        }
        records=[]
        with self.store.transaction() as c:
            for name,path in candidates.items():
                available=path is not None; version=None; details={}
                if path is not None:
                    try:
                        completed=subprocess.run([str(path),'--version'],capture_output=True,text=True,timeout=5,check=False)
                        text=(completed.stdout+'\n'+completed.stderr).strip(); version=text.splitlines()[0] if text else None
                        details={'return_code':completed.returncode}
                    except (OSError,subprocess.TimeoutExpired) as exc: details={'version_error':str(exc)}
                now=utc_now(); tool_id=random_id('tool')
                c.execute("INSERT INTO native_windows_tools VALUES(?,?,?,?,?,?,?) ON CONFLICT(tool_name) DO UPDATE SET path=excluded.path,available=excluded.available,version=excluded.version,details_json=excluded.details_json,checked_at=excluded.checked_at",(tool_id,name,None if path is None else str(path),int(available),version,canonical_json(details),now))
                records.append({'tool_name':name,'available':available,'path':None if path is None else str(path),'version':version,'details':details})
            self.store.audit(actor,'native.windows.doctor','toolchain',{'available':[r['tool_name'] for r in records if r['available']]},connection=c)
        return {'platform':os.name,'tools':records,'ghidra_launcher_policy':'Windows prefers analyzeHeadless.bat; POSIX prefers analyzeHeadless'}
