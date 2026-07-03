from __future__ import annotations

from typing import Any
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import ReconstructionStore

SEVERITIES={'informational','low','medium','high','critical'}
class SecurityReview:
    def __init__(self,store:ReconstructionStore): self.store=store; store.initialize()
    def finding(self,rule_id:str,severity:str,subject_id:str,summary:str,*,evidence:list[dict[str,Any]],actor:str='analyst')->dict[str,Any]:
        if severity not in SEVERITIES: raise ContractError('invalid severity')
        if not evidence: raise ContractError('security findings require evidence')
        fid=random_id('finding'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_security_findings VALUES(?,?,?,?,?,?,?,?,?)',(fid,rule_id,severity,subject_id,summary,canonical_json(evidence),'open',now,now)); self.store.audit(actor,'reconstruction.security.finding',fid,{'rule_id':rule_id,'severity':severity,'subject_id':subject_id},connection=c)
        return self.get(fid)
    def get(self,finding_id:str)->dict[str,Any]:
        with self.store.connect() as c: row=c.execute('SELECT * FROM reconstruction_security_findings WHERE finding_id=?',(finding_id,)).fetchone()
        if not row: raise KeyError(finding_id)
        return self.store.decode(row,'evidence_json')
    def scan(self,observations:list[dict[str,Any]],*,actor:str='scanner')->dict[str,Any]:
        rules={'VirtualAlloc':'memory-executable-allocation','CreateRemoteThread':'remote-thread','WriteProcessMemory':'cross-process-write','WinExec':'process-execution','URLDownloadToFile':'network-download','strcpy':'unsafe-copy'}
        created=[]
        for obs in observations:
            api=str(obs.get('api',''))
            if api in rules: created.append(self.finding(rules[api],'high' if api in {'CreateRemoteThread','WriteProcessMemory'} else 'medium',str(obs.get('subject_id',api)),f'Observed use of {api}',evidence=[{'kind':'api-observation','record':obs}],actor=actor))
        return {'observations':len(observations),'findings':created,'finding_count':len(created),'behavior_modified':False}
    def policy(self,name:str,policy:dict[str,Any],*,actor:str='analyst')->dict[str,Any]:
        pid=random_id('secpolicy'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_security_policies VALUES(?,?,?,?,?)',(pid,name,canonical_json(policy),now,now)); self.store.audit(actor,'reconstruction.security.policy',pid,{'name':name},connection=c)
        return {'policy_id':pid,'name':name,'policy':policy}
    def report(self)->dict[str,Any]:
        with self.store.connect() as c: rows=c.execute('SELECT * FROM reconstruction_security_findings ORDER BY CASE severity WHEN "critical" THEN 0 WHEN "high" THEN 1 WHEN "medium" THEN 2 WHEN "low" THEN 3 ELSE 4 END,created_at').fetchall()
        findings=[self.store.decode(r,'evidence_json') for r in rows]; counts={s:sum(1 for x in findings if x['severity']==s) for s in sorted(SEVERITIES)}
        return {'findings':findings,'counts':counts,'total':len(findings),'claim':'observational security review; recovered behavior is not automatically sanitized'}
