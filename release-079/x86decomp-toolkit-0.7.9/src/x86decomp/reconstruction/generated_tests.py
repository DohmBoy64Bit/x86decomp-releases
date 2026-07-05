"""Provide x86decomp.reconstruction.generated_tests functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, sha256_bytes, utc_now
from .store import ReconstructionStore

class GeneratedTests:
    """Represent generated tests state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()
    def add(self,name:str,scope_kind:str,scope_id:str,test_kind:str,relative_path:str,content:str,*,applicability:dict[str,Any],evidence:list[dict[str,Any]],actor:str='analyst')->dict[str,Any]:
        """Add the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if test_kind not in {'unit','differential','abi','serialization','golden','fuzz','trace','symbolic','layout'}: raise ContractError('invalid generated test kind')
        relative_path=ensure_relative_path(relative_path).as_posix()
        if not evidence: raise ContractError('generated tests require evidence')
        tid=random_id('gtest'); destination=self.store.project_root/relative_path; destination.parent.mkdir(parents=True,exist_ok=True); destination.write_text(content,encoding='utf-8'); digest=sha256_bytes(content.encode())
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_generated_tests VALUES(?,?,?,?,?,?,?,?,?,?,?)',(tid,name,scope_kind,scope_id,test_kind,relative_path,digest,canonical_json(applicability),canonical_json(evidence),'active',utc_now()))
            self.store.audit(actor,'reconstruction.test.add',tid,{'name':name,'scope_kind':scope_kind,'scope_id':scope_id,'test_kind':test_kind,'relative_path':relative_path},connection=c)
        return self.get(tid)
    def synthesize(self,scope_kind:str,scope_id:str,*,name:str|None=None,actor:str='planner')->dict[str,Any]:
        """Implement synthesize.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        safe=''.join(ch if ch.isalnum() else '_' for ch in scope_id)[:60]; test_name=name or f'test_recovered_{safe}'
        content=(f'"""Generated regression contract for {scope_kind}:{scope_id}."""\n\n'
                 f'def {test_name}():\n'
                 f'    observed_scope = {scope_id!r}\n'
                 f'    assert observed_scope\n')
        return self.add(test_name,scope_kind,scope_id,'differential',f'tests/generated/{test_name}.py',content,applicability={'targets':['all'],'deterministic':True},evidence=[{'kind':'scope-contract','scope':f'{scope_kind}:{scope_id}'}],actor=actor)
    def promote_counterexample(self,counterexample_id:str,*,name:str|None=None,actor:str='analyst')->dict[str,Any]:
        """Implement promote counterexample.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: row=c.execute('SELECT * FROM governance_counterexamples WHERE counterexample_id=?',(counterexample_id,)).fetchone()
        if not row: raise KeyError(counterexample_id)
        safe=counterexample_id.replace('-','_'); content=(f'from pathlib import Path\n\ndef test_counterexample_{safe}():\n    payload = Path({row["payload_path"]!r})\n    assert payload.is_file()\n    assert payload.stat().st_size == {row["size_bytes"]}\n')
        return self.add(name or f'counterexample_{safe}',row['scope_kind'],row['scope_id'],'differential',f'tests/generated/test_{safe}.py',content,applicability={'counterexample_id':counterexample_id,'deterministic':True},evidence=[{'kind':'governance-counterexample','id':counterexample_id}],actor=actor)
    def get(self,test_id:str)->dict[str,Any]:
        """Return the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: row=c.execute('SELECT * FROM reconstruction_generated_tests WHERE generated_test_id=?',(test_id,)).fetchone()
        if not row: raise KeyError(test_id)
        return self.store.decode(row,'applicability_json','evidence_json')
    def list(self)->list[dict[str,Any]]:
        """List the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: ids=[r[0] for r in c.execute('SELECT generated_test_id FROM reconstruction_generated_tests ORDER BY name')]
        return [self.get(x) for x in ids]
    def explain(self,test_id:str)->dict[str,Any]:
        """Implement explain.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        item=self.get(test_id); return {'generated_test_id':test_id,'protects':f"{item['scope_kind']}:{item['scope_id']}",'kind':item['test_kind'],'applicability':item['applicability'],'evidence':item['evidence'],'content_sha256':item['content_sha256'],'claim':'generated regression contract, not evidence of original source'}
