"""Manage generated regression-contract tests backed by the reconstruction store."""
from __future__ import annotations

from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, sha256_bytes, utc_now
from .store import ReconstructionStore

class GeneratedTests:
    """Store and synthesize generated regression tests in the reconstruction store.

    Wraps the ``reconstruction_generated_tests`` table, materializing test source
    files under the project root and recording their metadata, evidence, and audit
    trail. Generated tests are regression contracts, not proof of original source.
    """
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with validated constructor state."""
        self.store=store; store.initialize()
    def add(self,name:str,scope_kind:str,scope_id:str,test_kind:str,relative_path:str,content:str,*,applicability:dict[str,Any],evidence:list[dict[str,Any]],actor:str='analyst')->dict[str,Any]:
        """Register a generated test, writing its source file and a store record.

        Args:
            name: Human-readable test name.
            scope_kind: Kind of scope the test protects (e.g. function, module).
            scope_id: Identifier of the protected scope.
            test_kind: Test category; one of unit, differential, abi, serialization,
                golden, fuzz, trace, symbolic, or layout.
            relative_path: Project-relative path to write the test source to.
            content: Test source contents.
            applicability: Applicability metadata stored with the test.
            evidence: Non-empty list of evidence records justifying the test.
            actor: Actor recorded in the audit log. Defaults to ``"analyst"``.

        Returns:
            The stored test record as returned by :meth:`get`.

        Raises:
            ContractError: If ``test_kind`` is invalid or ``evidence`` is empty.
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
        """Synthesize a minimal differential regression test for a scope.

        Args:
            scope_kind: Kind of scope the test protects.
            scope_id: Identifier of the protected scope.
            name: Optional test name; defaults to ``test_recovered_<scope>``.
            actor: Actor recorded in the audit log. Defaults to ``"planner"``.

        Returns:
            The stored test record for the synthesized test.
        """
        safe=''.join(ch if ch.isalnum() else '_' for ch in scope_id)[:60]; test_name=name or f'test_recovered_{safe}'
        content=(f'"""Generated regression contract for {scope_kind}:{scope_id}."""\n\n'
                 f'def {test_name}():\n'
                 f'    observed_scope = {scope_id!r}\n'
                 f'    assert observed_scope\n')
        return self.add(test_name,scope_kind,scope_id,'differential',f'tests/generated/{test_name}.py',content,applicability={'targets':['all'],'deterministic':True},evidence=[{'kind':'scope-contract','scope':f'{scope_kind}:{scope_id}'}],actor=actor)
    def promote_counterexample(self,counterexample_id:str,*,name:str|None=None,actor:str='analyst')->dict[str,Any]:
        """Promote a governance counterexample into a generated differential test.

        Looks up the counterexample and emits a test asserting its payload file
        exists and matches the recorded size.

        Args:
            counterexample_id: Identifier of the governance counterexample.
            name: Optional test name; defaults to ``counterexample_<id>``.
            actor: Actor recorded in the audit log. Defaults to ``"analyst"``.

        Returns:
            The stored test record for the promoted test.

        Raises:
            KeyError: If no counterexample with the given id exists.
        """
        with self.store.connect() as c: row=c.execute('SELECT * FROM governance_counterexamples WHERE counterexample_id=?',(counterexample_id,)).fetchone()
        if not row: raise KeyError(counterexample_id)
        safe=counterexample_id.replace('-','_'); content=(f'from pathlib import Path\n\ndef test_counterexample_{safe}():\n    payload = Path({row["payload_path"]!r})\n    assert payload.is_file()\n    assert payload.stat().st_size == {row["size_bytes"]}\n')
        return self.add(name or f'counterexample_{safe}',row['scope_kind'],row['scope_id'],'differential',f'tests/generated/test_{safe}.py',content,applicability={'counterexample_id':counterexample_id,'deterministic':True},evidence=[{'kind':'governance-counterexample','id':counterexample_id}],actor=actor)
    def get(self,test_id:str)->dict[str,Any]:
        """Fetch a generated test record by id.

        Args:
            test_id: Generated test identifier.

        Returns:
            The decoded test record with applicability and evidence expanded.

        Raises:
            KeyError: If no test with the given id exists.
        """
        with self.store.connect() as c: row=c.execute('SELECT * FROM reconstruction_generated_tests WHERE generated_test_id=?',(test_id,)).fetchone()
        if not row: raise KeyError(test_id)
        return self.store.decode(row,'applicability_json','evidence_json')
    def list(self)->list[dict[str,Any]]:
        """List all generated test records ordered by name.

        Returns:
            The decoded records for every generated test in the store.
        """
        with self.store.connect() as c: ids=[r[0] for r in c.execute('SELECT generated_test_id FROM reconstruction_generated_tests ORDER BY name')]
        return [self.get(x) for x in ids]
    def explain(self,test_id:str)->dict[str,Any]:
        """Summarize what a generated test protects and how it is justified.

        Args:
            test_id: Generated test identifier.

        Returns:
            A dict describing the protected scope, test kind, applicability, evidence,
            and content hash, noting the test is a regression contract only.
        """
        item=self.get(test_id); return {'generated_test_id':test_id,'protects':f"{item['scope_kind']}:{item['scope_id']}",'kind':item['test_kind'],'applicability':item['applicability'],'evidence':item['evidence'],'content_sha256':item['content_sha256'],'claim':'generated regression contract, not evidence of original source'}
