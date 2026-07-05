"""Provide x86decomp.reconstruction.headers functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, utc_now
from .store import ReconstructionStore

class HeaderManager:
    """Represent header manager state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()
    def create(self,path:str,*,visibility:str='private',actor:str='analyst')->dict[str,Any]:
        """Create the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        path=ensure_relative_path(path).as_posix()
        if not path.endswith(('.h','.hpp','.hh')): raise ContractError('header path must use a header extension')
        if visibility not in {'public','private','internal'}: raise ContractError('invalid visibility')
        hid=random_id('header'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_headers VALUES(?,?,?,?,?,?)',(hid,path,visibility,'proposed',now,now))
            self.store.audit(actor,'reconstruction.header.create',hid,{'path':path,'visibility':visibility},connection=c)
        return self.show(hid)
    def declare(self,header_id:str,symbol_id:str,declaration:str,*,kind:str='function',confidence:float=1.0,evidence:list[dict[str,Any]]|None=None,actor:str='analyst')->dict[str,Any]:
        """Implement declare.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if not declaration.strip().endswith((';','}')): raise ContractError('declaration must end with semicolon or closing brace')
        if kind not in {'function','type','variable','enum','macro','forward'}: raise ContractError('invalid declaration kind')
        did=random_id('decl')
        with self.store.transaction() as c:
            if not c.execute('SELECT 1 FROM reconstruction_headers WHERE header_id=?',(header_id,)).fetchone(): raise KeyError(header_id)
            c.execute('INSERT INTO reconstruction_header_declarations VALUES(?,?,?,?,?,?,?)',(did,header_id,symbol_id,declaration,kind,confidence,canonical_json(evidence or [])))
            c.execute('UPDATE reconstruction_headers SET updated_at=? WHERE header_id=?',(utc_now(),header_id))
            self.store.audit(actor,'reconstruction.header.declaration',did,{'header_id':header_id,'symbol_id':symbol_id,'kind':kind},connection=c)
        return self.show(header_id)
    def include(self,source_header_id:str,target_header_id:str,*,reason:str,actor:str='analyst')->dict[str,Any]:
        """Implement include.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_include_edges VALUES(?,?,?)',(source_header_id,target_header_id,reason))
            if self.cycles(connection=c):
                raise ContractError('include edge creates a cycle')
            self.store.audit(actor,'reconstruction.header.include',source_header_id,{'target_header_id':target_header_id,'reason':reason},connection=c)
        return self.show(source_header_id)
    def cycles(self,*,connection=None)->list[list[str]]:
        """Implement cycles.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        owns=connection is None; c=connection or self.store.connect()
        try:
            edges=[(r[0],r[1]) for r in c.execute('SELECT source_header_id,target_header_id FROM reconstruction_include_edges')]
        finally:
            if owns: c.close()
        graph:dict[str,list[str]]={}
        for a,b in edges: graph.setdefault(a,[]).append(b)
        cycles=[]; stack=[]; active=set(); done=set()
        def visit(node:str):
            """Implement visit.
            
            Parameters and return values follow the signature and runtime validation in the body.
            """
            if node in active:
                i=stack.index(node); cycles.append(stack[i:]+[node]); return
            if node in done:return
            active.add(node); stack.append(node)
            for nxt in graph.get(node,[]): visit(nxt)
            stack.pop(); active.remove(node); done.add(node)
        for node in sorted(graph): visit(node)
        return cycles
    def show(self,header_id:str)->dict[str,Any]:
        """Implement show.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_headers WHERE header_id=?',(header_id,)).fetchone()
            if not row: raise KeyError(header_id)
            out=dict(row); out['declarations']=[self.store.decode(r,'evidence_json') for r in c.execute('SELECT * FROM reconstruction_header_declarations WHERE header_id=? ORDER BY declaration_kind,symbol_id',(header_id,))]
            out['includes']=[dict(r) for r in c.execute('SELECT e.*,h.path AS target_path FROM reconstruction_include_edges e JOIN reconstruction_headers h ON h.header_id=e.target_header_id WHERE e.source_header_id=? ORDER BY h.path',(header_id,))]
        return out
    def synthesize(self,header_id:str,*,output_root:str|Path|None=None)->dict[str,Any]:
        """Implement synthesize.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        header=self.show(header_id); guard='X86DECOMP_'+''.join(ch.upper() if ch.isalnum() else '_' for ch in header['path'])
        lines=[f'#ifndef {guard}',f'#define {guard}','']
        lines.extend(f'#include "{i["target_path"]}"' for i in header['includes'])
        if header['includes']: lines.append('')
        lines.extend(d['declaration'] for d in header['declarations']); lines+=['',f'#endif /* {guard} */','']
        text='\n'.join(lines)
        result={'header_id':header_id,'path':header['path'],'content':text,'declaration_count':len(header['declarations'])}
        if output_root is not None:
            destination=Path(output_root)/ensure_relative_path(header['path']); destination.parent.mkdir(parents=True,exist_ok=True); destination.write_text(text,encoding='utf-8'); result['written_to']=str(destination.resolve())
        return result
    def validate(self,header_id:str)->dict[str,Any]:
        """Validate the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        h=self.show(header_id); duplicate_symbols=len({d['symbol_id'] for d in h['declarations']})!=len(h['declarations'])
        checks={'no_include_cycles':not self.cycles(),'has_declarations':bool(h['declarations']),'unique_symbols':not duplicate_symbols,'relative_path':not Path(h['path']).is_absolute()}
        return {'header_id':header_id,'checks':checks,'passed':all(checks.values())}
