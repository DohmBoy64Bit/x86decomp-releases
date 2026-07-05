"""Provide x86decomp.native.staging functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any, Iterable

from x86decomp.util import sha256_file
from x86decomp.contracts import ContractError, random_id, utc_now
from .store import NativeStore

_TYPE_MAP = {
    "undefined1": "uint8_t",
    "undefined2": "uint16_t",
    "undefined4": "uint32_t",
    "undefined8": "uint64_t",
    "byte": "uint8_t",
    "word": "uint16_t",
    "dword": "uint32_t",
    "qword": "uint64_t",
}
_SYMBOL_RE = re.compile(r"\b(?P<kind>FUN|DAT|LAB|PTR)_?[0-9A-Fa-f]{6,16}\b")


class StagingBridge:
    """Represent staging bridge state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: NativeStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()

    def scan(self, source_paths: Iterable[Path]) -> dict[str,Any]:
        """Scan the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        symbols: dict[str,str]={}; types:set[str]=set()
        files=[]
        for path in source_paths:
            path=path.resolve()
            if not path.is_file(): raise ContractError(f'staging source does not exist: {path}')
            text=path.read_text(encoding='utf-8',errors='replace'); files.append(str(path))
            for token,replacement in _TYPE_MAP.items():
                if re.search(rf'\b{re.escape(token)}\b',text): types.add(token)
            for match in _SYMBOL_RE.finditer(text): symbols[match.group(0)]=match.group('kind')
        return {'files':files,'types':sorted(types),'symbols':[{'name':name,'kind':kind} for name,kind in sorted(symbols.items())]}

    def generate_context(self, source_paths:Iterable[Path], output:Path, *, actor:str='analyst')->dict[str,Any]:
        """Generate context.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        scan=self.scan(source_paths); lines=['#ifndef X86DECOMP_GENERATED_CONTEXT_H','#define X86DECOMP_GENERATED_CONTEXT_H','','#include <stdint.h>','#include <stddef.h>','']
        for token in scan['types']: lines.append(f'typedef {_TYPE_MAP[token]} {token};')
        if scan['types']: lines.append('')
        for item in scan['symbols']:
            name=item['name']; kind=item['kind']
            declaration=(f'extern void {name}(void);' if kind=='FUN' else f'extern uintptr_t {name};')
            lines.append(declaration)
            now=utc_now()
            with self.store.transaction() as c:
                row=c.execute('SELECT symbol_id FROM native_staging_symbols WHERE symbol_name=?',(name,)).fetchone()
                if row:
                    c.execute('UPDATE native_staging_symbols SET symbol_kind=?,declaration=?,source=?,status=?,updated_at=? WHERE symbol_name=?',(kind,declaration,'generated-context','proposed',now,name))
                else:
                    c.execute('INSERT INTO native_staging_symbols VALUES(?,?,?,?,?,?,?,?,?)',(random_id('symbol'),name,kind,declaration,'generated-context',0.5,'proposed',now,now))
        lines.extend(['','#endif','']); output=output.resolve(); output.parent.mkdir(parents=True,exist_ok=True); output.write_text('\n'.join(lines),encoding='utf-8')
        self.store.audit(actor,'native.staging.context',str(output),{'symbol_count':len(scan['symbols']),'type_count':len(scan['types'])})
        return {'output':str(output),'sha256':sha256_file(output),**scan}

    def resolve(self, mapping:dict[str,str], *, actor:str='analyst')->dict[str,Any]:
        """Resolve the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        updated=[]
        with self.store.transaction() as c:
            for name,declaration in sorted(mapping.items()):
                row=c.execute('SELECT symbol_id FROM native_staging_symbols WHERE symbol_name=?',(name,)).fetchone()
                if row is None: raise KeyError(name)
                c.execute("UPDATE native_staging_symbols SET declaration=?,source='analyst-mapping',confidence=1.0,status='accepted',updated_at=? WHERE symbol_name=?",(utc_now(),declaration,name))
                updated.append(name)
            self.store.audit(actor,'native.staging.resolve','symbols',{'symbols':updated},connection=c)
        return {'updated':updated,'count':len(updated)}

    def unresolved(self)->list[dict[str,Any]]:
        """Implement unresolved.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: return [dict(row) for row in c.execute("SELECT * FROM native_staging_symbols WHERE status!='accepted' ORDER BY symbol_name")]

    def compile_check(self, command:list[str], *, cwd:Path|None=None, timeout_seconds:int=120)->dict[str,Any]:
        """Compile check.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if not command or timeout_seconds<=0: raise ContractError('compile-check requires a command and positive timeout')
        completed=subprocess.run(command,cwd=None if cwd is None else cwd.resolve(),capture_output=True,text=True,timeout=timeout_seconds,check=False)
        return {'command':command,'cwd':None if cwd is None else str(cwd.resolve()),'return_code':completed.returncode,'passed':completed.returncode==0,'stdout':completed.stdout,'stderr':completed.stderr,'timeout_seconds':timeout_seconds}
