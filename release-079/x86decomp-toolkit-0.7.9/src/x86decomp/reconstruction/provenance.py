"""Provide x86decomp.reconstruction.provenance functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, sha256_file, utc_now
from .store import ReconstructionStore

class ProvenanceLedger:
    """Represent provenance ledger state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()
    def record(self,source_path:str,line_start:int,line_end:int,binary_id:str,address_start:str,address_end:str,*,evidence:list[dict[str,Any]],confidence:float,actor:str='analyst')->dict[str,Any]:
        """Implement record.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        source_path=ensure_relative_path(source_path).as_posix()
        if line_start<1 or line_end<line_start: raise ContractError('invalid source line range')
        if not evidence: raise ContractError('provenance requires evidence')
        if not 0<=confidence<=1: raise ContractError('confidence must be between 0 and 1')
        pid=random_id('prov')
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_source_provenance VALUES(?,?,?,?,?,?,?,?,?,?)',(pid,source_path,line_start,line_end,binary_id,address_start,address_end,canonical_json(evidence),confidence,utc_now()))
            self.store.audit(actor,'reconstruction.provenance.record',pid,{'source_path':source_path,'line_start':line_start,'line_end':line_end,'binary_id':binary_id,'address_start':address_start,'address_end':address_end,'confidence':confidence},connection=c)
        return self.get(pid)
    def get(self,provenance_id:str)->dict[str,Any]:
        """Return the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: row=c.execute('SELECT * FROM reconstruction_source_provenance WHERE provenance_id=?',(provenance_id,)).fetchone()
        if not row: raise KeyError(provenance_id)
        return self.store.decode(row,'evidence_json')
    def source(self,path:str,line:int|None=None)->list[dict[str,Any]]:
        """Implement source.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        path=ensure_relative_path(path).as_posix()
        with self.store.connect() as c:
            if line is None: rows=c.execute('SELECT * FROM reconstruction_source_provenance WHERE source_path=? ORDER BY line_start',(path,)).fetchall()
            else: rows=c.execute('SELECT * FROM reconstruction_source_provenance WHERE source_path=? AND line_start<=? AND line_end>=? ORDER BY confidence DESC',(path,line,line)).fetchall()
        return [self.store.decode(r,'evidence_json') for r in rows]
    def binary(self,binary_id:str,address:str|None=None)->list[dict[str,Any]]:
        """Implement binary.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c:
            if address is None: rows=c.execute('SELECT * FROM reconstruction_source_provenance WHERE binary_id=? ORDER BY address_start',(binary_id,)).fetchall()
            else: rows=c.execute('SELECT * FROM reconstruction_source_provenance WHERE binary_id=? AND address_start<=? AND address_end>=? ORDER BY confidence DESC',(binary_id,address,address)).fetchall()
        return [self.store.decode(r,'evidence_json') for r in rows]
    def lock(self,path:str,*,reason:str,actor:str='analyst')->dict[str,Any]:
        """Implement lock.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        path=ensure_relative_path(path).as_posix()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_source_locks VALUES(?,?,?,?) ON CONFLICT(source_path) DO UPDATE SET actor=excluded.actor,reason=excluded.reason,locked_at=excluded.locked_at',(path,actor,reason,utc_now()))
            self.store.audit(actor,'reconstruction.source.lock',path,{'reason':reason},connection=c)
        return {'source_path':path,'locked':True,'actor':actor,'reason':reason}
    def unlock(self,path:str,*,actor:str='analyst')->dict[str,Any]:
        """Implement unlock.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        path=ensure_relative_path(path).as_posix()
        with self.store.transaction() as c:
            c.execute('DELETE FROM reconstruction_source_locks WHERE source_path=?',(path,)); self.store.audit(actor,'reconstruction.source.unlock',path,{},connection=c)
        return {'source_path':path,'locked':False}
    def reconcile(self,path:str,*,before_sha256:str|None=None,semantic:bool|None=None,actor:str='analyst')->dict[str,Any]:
        """Implement reconcile.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        rel=ensure_relative_path(path).as_posix(); actual=self.store.project_root/rel
        if not actual.is_file(): raise FileNotFoundError(actual)
        with self.store.connect() as c:
            if c.execute('SELECT 1 FROM reconstruction_source_locks WHERE source_path=?',(rel,)).fetchone(): raise ContractError('source path is locked')
        after=sha256_file(actual); semantic=bool(semantic if semantic is not None else before_sha256 != after)
        prov=self.source(rel); affected=sorted({f"{p['binary_id']}:{p['address_start']}-{p['address_end']}" for p in prov})
        eid=random_id('edit'); invalid=[]
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_source_edits VALUES(?,?,?,?,?,?,?,?)',(eid,rel,before_sha256,after,1 if semantic else 0,canonical_json(affected),actor,utc_now()))
            if semantic:
                for row in c.execute("SELECT obligation_id FROM governance_proof_obligations WHERE scope_id IN (%s)" % (','.join('?' for _ in affected) or "''"),affected).fetchall() if affected else []:
                    iid=random_id('invalidate'); c.execute('INSERT INTO reconstruction_proof_invalidations VALUES(?,?,?,?,?,?)',(iid,eid,row[0],'source semantic edit','stale',utc_now())); invalid.append(row[0])
            self.store.audit(actor,'reconstruction.source.reconcile',eid,{'source_path':rel,'semantic':semantic,'affected':affected,'invalidated':invalid},connection=c)
        return {'edit_id':eid,'source_path':rel,'before_sha256':before_sha256,'after_sha256':after,'semantic':semantic,'affected':affected,'invalidated_obligations':invalid}
    def impact(self,path:str)->dict[str,Any]:
        """Implement impact.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        rel=ensure_relative_path(path).as_posix(); mappings=self.source(rel)
        return {'source_path':rel,'binary_regions':sorted({f"{p['binary_id']}:{p['address_start']}-{p['address_end']}" for p in mappings}),'mapping_count':len(mappings),'proofs_must_be_revalidated':bool(mappings)}
    def export(self,path:str|Path)->dict[str,Any]:
        """Export the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: rows=c.execute('SELECT * FROM reconstruction_source_provenance ORDER BY source_path,line_start').fetchall()
        payload={'schema':'x86decomp.source-provenance.v1','records':[self.store.decode(r,'evidence_json') for r in rows]}; out=Path(path); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        return {'path':str(out.resolve()),'records':len(rows)}
