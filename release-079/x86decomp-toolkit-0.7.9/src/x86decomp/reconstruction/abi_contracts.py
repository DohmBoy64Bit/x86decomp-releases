"""Provide x86decomp.reconstruction.abi_contracts functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, utc_now
from .store import ReconstructionStore

class ABIContracts:
    """Represent a b i contracts state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()
    def recover(self,subject_kind:str,subject_id:str,architecture:str,contract:dict[str,Any],*,evidence:list[dict[str,Any]],actor:str='analyst')->dict[str,Any]:
        """Recover the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if subject_kind not in {'function','module','library','executable','interface'}: raise ContractError('invalid ABI subject kind')
        if architecture not in {'x86','x86_64'}: raise ContractError('unsupported ABI architecture')
        required={'calling_convention','parameters','return_type'} if subject_kind=='function' else set()
        missing=sorted(required-set(contract));
        if missing: raise ContractError(f'missing ABI fields: {missing}')
        if not evidence: raise ContractError('ABI recovery requires evidence')
        cid=random_id('abi'); now=utc_now()
        with self.store.transaction() as c:
            existing=c.execute('SELECT contract_id FROM reconstruction_abi_contracts WHERE subject_kind=? AND subject_id=? AND architecture=?',(subject_kind,subject_id,architecture)).fetchone()
            if existing:
                cid=existing[0]; c.execute('UPDATE reconstruction_abi_contracts SET contract_json=?,evidence_json=?,status=?,updated_at=? WHERE contract_id=?',(canonical_json(contract),canonical_json(evidence),'proposed',now,cid))
            else: c.execute('INSERT INTO reconstruction_abi_contracts VALUES(?,?,?,?,?,?,?,?,?)',(cid,subject_kind,subject_id,architecture,canonical_json(contract),canonical_json(evidence),'proposed',now,now))
            self.store.audit(actor,'reconstruction.abi.recover',cid,{'subject_kind':subject_kind,'subject_id':subject_id,'architecture':architecture},connection=c)
        return self.get(cid)
    def get(self,contract_id:str)->dict[str,Any]:
        """Return the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: row=c.execute('SELECT * FROM reconstruction_abi_contracts WHERE contract_id=?',(contract_id,)).fetchone()
        if not row: raise KeyError(contract_id)
        return self.store.decode(row,'contract_json','evidence_json')
    def verify(self,contract_id:str)->dict[str,Any]:
        """Verify the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        item=self.get(contract_id); contract=item['contract']; checks={'evidence_present':bool(item['evidence']),'contract_nonempty':bool(contract),'architecture_supported':item['architecture'] in {'x86','x86_64'}}
        if item['subject_kind']=='function': checks.update({'calling_convention_present':bool(contract.get('calling_convention')),'parameters_list':isinstance(contract.get('parameters'),list),'return_type_present':bool(contract.get('return_type'))})
        passed=all(checks.values())
        with self.store.transaction() as c: c.execute('UPDATE reconstruction_abi_contracts SET status=?,updated_at=? WHERE contract_id=?',('verified' if passed else 'rejected',utc_now(),contract_id))
        return {'contract_id':contract_id,'checks':checks,'passed':passed}
    def compare(self,left_id:str,right_id:str)->dict[str,Any]:
        """Compare the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        left,right=self.get(left_id),self.get(right_id); keys=sorted(set(left['contract'])|set(right['contract'])); differences={k:{'left':left['contract'].get(k),'right':right['contract'].get(k)} for k in keys if left['contract'].get(k)!=right['contract'].get(k)}
        return {'left':left_id,'right':right_id,'compatible':not differences,'differences':differences,'architecture_match':left['architecture']==right['architecture']}
    def export(self,contract_id:str,path:str|Path)->dict[str,Any]:
        """Export the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        out=Path(path); out.parent.mkdir(parents=True,exist_ok=True); payload={'schema':'x86decomp.abi-contract.v1',**self.get(contract_id)}; out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8'); return {'path':str(out.resolve()),'contract_id':contract_id}
    def shim(self,contract_id:str,source_path:str,*,shim_kind:str='wrapped',actor:str='analyst')->dict[str,Any]:
        """Implement shim.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if shim_kind not in {'reimplemented','wrapped','translated','assumption-dependent','externally-supplied'}: raise ContractError('invalid shim kind')
        contract=self.get(contract_id); source_path=ensure_relative_path(source_path).as_posix(); sid=random_id('shim')
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_compatibility_shims VALUES(?,?,?,?,?,?,?)',(sid,contract['subject_id'],shim_kind,source_path,canonical_json(contract['contract']),'proposed',utc_now()))
            self.store.audit(actor,'reconstruction.abi.shim',sid,{'contract_id':contract_id,'shim_kind':shim_kind,'source_path':source_path},connection=c)
        return {'shim_id':sid,'contract_id':contract_id,'subject_id':contract['subject_id'],'shim_kind':shim_kind,'source_path':source_path,'status':'proposed'}
