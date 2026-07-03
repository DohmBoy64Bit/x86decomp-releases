from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

from x86decomp.pe import parse_pe
from x86decomp.util import sha256_file
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import NativeStore


class RuntimeValidation:
    def __init__(self,store:NativeStore): self.store=store; store.initialize()

    def validate_image(self,image_path:Path, *, actor:str='analyst')->dict[str,Any]:
        image_path=image_path.resolve(); image=parse_pe(image_path); sections=sorted(image.sections,key=lambda s:s.virtual_address)
        overlaps=[]
        for left,right in zip(sections,sections[1:]):
            left_end=left.virtual_address+max(left.virtual_size,left.raw_size)
            if left_end>right.virtual_address: overlaps.append({'left':left.name,'right':right.name,'overlap_bytes':left_end-right.virtual_address})
        entry_section=next((s.name for s in sections if s.virtual_address<=image.entry_rva<s.virtual_address+max(s.virtual_size,s.raw_size)),None)
        checks={'pe_parses':True,'entry_point_mapped':entry_section is not None,'section_ranges_non_overlapping':not overlaps,'headers_within_file':image.size_of_headers<=image_path.stat().st_size}
        details={'architecture':image.to_dict()['architecture'],'entry_rva':image.entry_rva,'entry_section':entry_section,'section_overlaps':overlaps,'directories':{d.name:{'rva':d.rva,'size':d.size} for d in image.directories}}
        result=self._record(image_path,'static-loader',checks,details,False,actor)
        return {**result,'passed':all(checks.values())}

    def launch(self,image_path:Path, *, execute:bool=False, timeout_seconds:int=10, arguments:list[str]|None=None, actor:str='analyst')->dict[str,Any]:
        image_path=image_path.resolve(); self.validate_image(image_path,actor=actor)
        if not execute: raise ContractError('native launch requires explicit execute=True consent')
        if os.name!='nt': raise ContractError('native PE launch is supported only on Windows')
        if timeout_seconds<=0: raise ContractError('timeout must be positive')
        command=[str(image_path),*(arguments or [])]
        try:
            completed=subprocess.run(command,capture_output=True,text=True,timeout=timeout_seconds,check=False)
            checks={'process_created':True,'completed_before_timeout':True,'return_code_zero':completed.returncode==0}
            details={'command':command,'return_code':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr}
        except subprocess.TimeoutExpired as exc:
            checks={'process_created':True,'completed_before_timeout':False,'return_code_zero':False}
            details={'command':command,'timeout_seconds':timeout_seconds,'stdout':(exc.stdout or ''),'stderr':(exc.stderr or '')}
        result=self._record(image_path,'native-launch',checks,details,True,actor); return {**result,'passed':checks['process_created']}

    def map_crash(self,rva:int)->dict[str,Any]:
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM native_function_slots WHERE rva<=? AND slot_end_rva>? ORDER BY rva DESC LIMIT 1',(rva,rva)).fetchone()
            if row is None: return {'rva':rva,'mapped':False}
            slot=self.store.decode(row,'evidence_json'); return {'rva':rva,'mapped':True,'function_id':slot['function_id'],'function_rva':slot['rva'],'offset':rva-slot['rva'],'classification':slot['classification']}

    def _record(self,path:Path,kind:str,checks:dict[str,Any],details:dict[str,Any],authorized:bool,actor:str)->dict[str,Any]:
        validation_id=random_id('runtime'); status='passed' if all(checks.values()) else 'failed'; now=utc_now()
        payload={'checks':checks,'details':details}
        with self.store.transaction() as c:
            c.execute('INSERT INTO native_runtime_validations VALUES(?,?,?,?,?,?,?,?)',(validation_id,str(path),sha256_file(path),kind,status,canonical_json(payload),int(authorized),now))
            self.store.audit(actor,'native.runtime.validate',validation_id,{'kind':kind,'status':status},connection=c)
        return {'validation_id':validation_id,'kind':kind,'status':status,'checks':checks,'details':details,'execution_authorized':authorized}
