"""Reconstruction of C/C++ header files: creating headers, recording symbol
declarations and include edges, detecting include cycles, and synthesizing source."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, utc_now
from .store import ReconstructionStore

class HeaderManager:
    """Manage reconstructed header files and their declarations, include graph, and
    synthesized output, persisting all state through a :class:`ReconstructionStore`."""
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with validated constructor state."""
        self.store=store; store.initialize()
    def create(self,path:str,*,visibility:str='private',actor:str='analyst')->dict[str,Any]:
        """Create a new proposed header record.

        Args:
            path: Relative header path; must use a ``.h``, ``.hpp``, or ``.hh`` extension.
            visibility: One of ``"public"``, ``"private"``, or ``"internal"``.
            actor: The actor recorded in the audit log.

        Returns:
            The created header as returned by :meth:`show`.

        Raises:
            ContractError: If the path lacks a header extension or the visibility is invalid.
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
        """Attach a symbol declaration to an existing header.

        Args:
            header_id: The header to declare into.
            symbol_id: The identifier of the declared symbol.
            declaration: The declaration text; must end with ``;`` or ``}``.
            kind: One of ``function``, ``type``, ``variable``, ``enum``, ``macro``, or
                ``forward``.
            confidence: A confidence score recorded with the declaration.
            evidence: Optional supporting evidence records.
            actor: The actor recorded in the audit log.

        Returns:
            The updated header as returned by :meth:`show`.

        Raises:
            ContractError: If the declaration is not properly terminated or the kind is
                invalid.
            KeyError: If ``header_id`` does not exist.
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
        """Record an include edge from one header to another.

        Args:
            source_header_id: The header that includes the target.
            target_header_id: The included header.
            reason: A human-readable justification for the edge.
            actor: The actor recorded in the audit log.

        Returns:
            The source header as returned by :meth:`show`.

        Raises:
            ContractError: If adding the edge would introduce an include cycle.
        """
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_include_edges VALUES(?,?,?)',(source_header_id,target_header_id,reason))
            if self.cycles(connection=c):
                raise ContractError('include edge creates a cycle')
            self.store.audit(actor,'reconstruction.header.include',source_header_id,{'target_header_id':target_header_id,'reason':reason},connection=c)
        return self.show(source_header_id)
    def cycles(self,*,connection=None)->list[list[str]]:
        """Detect cycles in the header include graph.

        Args:
            connection: An open store connection to reuse; if ``None``, a temporary
                connection is opened and closed.

        Returns:
            A list of cycles, each a list of header IDs ending at its start node; empty
            when the include graph is acyclic.
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
            """Depth-first visit that appends any back-edge cycle to ``cycles``."""
            if node in active:
                i=stack.index(node); cycles.append(stack[i:]+[node]); return
            if node in done:return
            active.add(node); stack.append(node)
            for nxt in graph.get(node,[]): visit(nxt)
            stack.pop(); active.remove(node); done.add(node)
        for node in sorted(graph): visit(node)
        return cycles
    def show(self,header_id:str)->dict[str,Any]:
        """Return a header with its declarations and resolved include edges.

        Args:
            header_id: The header to load.

        Returns:
            The header record augmented with ``declarations`` and ``includes`` lists.

        Raises:
            KeyError: If ``header_id`` does not exist.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_headers WHERE header_id=?',(header_id,)).fetchone()
            if not row: raise KeyError(header_id)
            out=dict(row); out['declarations']=[self.store.decode(r,'evidence_json') for r in c.execute('SELECT * FROM reconstruction_header_declarations WHERE header_id=? ORDER BY declaration_kind,symbol_id',(header_id,))]
            out['includes']=[dict(r) for r in c.execute('SELECT e.*,h.path AS target_path FROM reconstruction_include_edges e JOIN reconstruction_headers h ON h.header_id=e.target_header_id WHERE e.source_header_id=? ORDER BY h.path',(header_id,))]
        return out
    def synthesize(self,header_id:str,*,output_root:str|Path|None=None)->dict[str,Any]:
        """Render a header to C source text with an include guard.

        Emits an ``#ifndef``/``#define`` guard derived from the path, the include
        directives, and the recorded declarations, optionally writing the result to disk.

        Args:
            header_id: The header to synthesize.
            output_root: If given, the root under which to write the header file.

        Returns:
            A dict with the header id, path, generated ``content``, declaration count,
            and, when written, the resolved ``written_to`` path.
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
        """Run structural validation checks on a header.

        Args:
            header_id: The header to validate.

        Returns:
            A dict with the header id, a ``checks`` mapping (no include cycles, has
            declarations, unique symbols, relative path), and an overall ``passed`` flag.
        """
        h=self.show(header_id); duplicate_symbols=len({d['symbol_id'] for d in h['declarations']})!=len(h['declarations'])
        checks={'no_include_cycles':not self.cycles(),'has_declarations':bool(h['declarations']),'unique_symbols':not duplicate_symbols,'relative_path':not Path(h['path']).is_absolute()}
        return {'header_id':header_id,'checks':checks,'passed':all(checks.values())}
