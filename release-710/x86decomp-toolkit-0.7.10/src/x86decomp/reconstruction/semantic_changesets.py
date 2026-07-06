"""Provide the current runtime implementation for the `x86decomp.reconstruction.semantic_changesets` module."""
from __future__ import annotations

import json
from typing import Any
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import ReconstructionStore

class SemanticChangeSets:
    """Coordinate semantic change sets behavior for the current toolkit workflow."""
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with validated constructor state."""
        self.store=store; store.initialize()
    def create(self,name:str,*,base_audit_hash:str|None=None,actor:str='analyst')->dict[str,Any]:
        """Create create for the current toolkit workflow."""
        cid=random_id('schangeset'); now=utc_now(); base_audit_hash=base_audit_hash or self.store.verify_audit_chain()['tip_hash']
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_semantic_changesets VALUES(?,?,?,?,?,?,?)',(cid,name,base_audit_hash,'[]','draft',now,now)); self.store.audit(actor,'reconstruction.changeset.create',cid,{'name':name,'base_audit_hash':base_audit_hash},connection=c)
        return self.get(cid)
    def get(self,changeset_id:str)->dict[str,Any]:
        """Execute the get operation for the current toolkit workflow."""
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_semantic_changesets WHERE changeset_id=?',(changeset_id,)).fetchone()
            if not row: raise KeyError(changeset_id)
            out=self.store.decode(row,'operations_json'); out['conflicts']=[self.store.decode(r,'details_json','resolution_json') for r in c.execute('SELECT * FROM reconstruction_merge_conflicts WHERE changeset_id=? ORDER BY created_at',(changeset_id,))]
        return out
    def add_operation(self,changeset_id:str,operation:dict[str,Any],*,actor:str='analyst')->dict[str,Any]:
        """Execute the add operation operation for the current toolkit workflow."""
        if operation.get('kind') not in {'source-edit','type-decision','hypothesis-decision','test-add','proof-invalidation','candidate-promotion','review-decision','build-change'}: raise ContractError('invalid semantic operation kind')
        if 'subject_id' not in operation: raise ContractError('semantic operation requires subject_id')
        with self.store.transaction() as c:
            row=c.execute('SELECT operations_json,status FROM reconstruction_semantic_changesets WHERE changeset_id=?',(changeset_id,)).fetchone()
            if not row: raise KeyError(changeset_id)
            if row['status']!='draft': raise ContractError('only draft changesets can be edited')
            operations=json.loads(row['operations_json']); operations.append(operation); c.execute('UPDATE reconstruction_semantic_changesets SET operations_json=?,updated_at=? WHERE changeset_id=?',(canonical_json(operations),utc_now(),changeset_id)); self.store.audit(actor,'reconstruction.changeset.operation',changeset_id,operation,connection=c)
        return self.get(changeset_id)
    def merge(self,left_id:str,right_id:str,name:str,*,actor:str='analyst')->dict[str,Any]:
        """Execute the merge operation for the current toolkit workflow."""
        left,right=self.get(left_id),self.get(right_id); merged=self.create(name,base_audit_hash=left['base_audit_hash'],actor=actor); seen={}; conflicts=[]
        for op in left['operations']+right['operations']:
            key=(op['kind'],op['subject_id'])
            if key in seen and seen[key]!=op:
                conflicts.append({'kind':'semantic','subject_id':op['subject_id'],'left':seen[key],'right':op})
            elif key not in seen: seen[key]=op
        with self.store.transaction() as c:
            c.execute('UPDATE reconstruction_semantic_changesets SET operations_json=?,status=?,updated_at=? WHERE changeset_id=?',(canonical_json(list(seen.values())),'conflicted' if conflicts else 'merged',utc_now(),merged['changeset_id']))
            for conflict in conflicts:
                fid=random_id('conflict'); c.execute('INSERT INTO reconstruction_merge_conflicts VALUES(?,?,?,?,?,?,?,?,?)',(fid,merged['changeset_id'],conflict['kind'],conflict['subject_id'],canonical_json(conflict),'open',None,utc_now(),utc_now()))
            self.store.audit(actor,'reconstruction.changeset.merge',merged['changeset_id'],{'left':left_id,'right':right_id,'conflicts':len(conflicts)},connection=c)
        return self.get(merged['changeset_id'])
    def conflicts(self,changeset_id:str)->list[dict[str,Any]]:
        """Execute the conflicts operation for the current toolkit workflow."""
        return self.get(changeset_id)['conflicts']
    def verify(self,changeset_id:str)->dict[str,Any]:
        """Verify verify for the current toolkit workflow."""
        item=self.get(changeset_id); open_conflicts=[x for x in item['conflicts'] if x['status']=='open']; checks={'operations_present':bool(item['operations']),'no_open_conflicts':not open_conflicts,'base_hash_shape':item['base_audit_hash'] is None or len(item['base_audit_hash'])==64}
        return {'changeset_id':changeset_id,'checks':checks,'passed':all(checks.values())}
    def rebase(self,changeset_id:str,new_base_hash:str,*,actor:str='analyst')->dict[str,Any]:
        """Execute the rebase operation for the current toolkit workflow."""
        if len(new_base_hash)!=64: raise ContractError('new base hash must be sha256')
        with self.store.transaction() as c: c.execute('UPDATE reconstruction_semantic_changesets SET base_audit_hash=?,updated_at=? WHERE changeset_id=?',(new_base_hash,utc_now(),changeset_id)); self.store.audit(actor,'reconstruction.changeset.rebase',changeset_id,{'new_base_hash':new_base_hash},connection=c)
        return self.get(changeset_id)
