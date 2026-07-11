"""Run closed-loop native reconstruction and verification."""
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from x86decomp.util import sha256_file
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .matching import FunctionMatching
from .store import NativeStore


class ClosedLoop:
    """Run and inspect iterative native reconstruction attempts and their validation evidence."""
    def __init__(self, store:NativeStore):
        """Initialize ClosedLoop with `store`."""
        self.store=store; store.initialize()

    def run(self, function_id:str, source_path:Path, compile_command:list[str], candidate_path:Path, original_path:Path, rva:int, slot_size:int, *, symbol:str|None=None, policy:str='trailing-padding', execute:bool=False, timeout_seconds:int=120, actor:str='analyst')->dict[str,Any]:
        """Run the closed loop workflow."""
        source_path=source_path.resolve(); candidate_path=candidate_path.resolve(); original_path=original_path.resolve()
        if not source_path.is_file(): raise ContractError(f'source does not exist: {source_path}')
        if not execute: raise ContractError('closed-loop compilation requires explicit execute=True consent')
        if not compile_command or timeout_seconds<=0: raise ContractError('compile command and positive timeout are required')
        loop_id=random_id('loop'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO native_loop_runs VALUES(?,?,?,?,?,?,?,?,?,?)',(loop_id,function_id,str(source_path),canonical_json(compile_command),str(candidate_path),policy,'compiling','{}',now,now))
        completed=subprocess.run(compile_command,cwd=source_path.parent,capture_output=True,text=True,timeout=timeout_seconds,check=False)
        compile_result={'return_code':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr,'command':compile_command}
        if completed.returncode!=0 or not candidate_path.is_file():
            result={'loop_id':loop_id,'status':'compile-failed','compile':compile_result,'candidate_exists':candidate_path.is_file()}
        else:
            match=FunctionMatching(self.store).batch(original_path,[{'function_id':function_id,'rva':rva,'slot_size':slot_size,'candidate_path':str(candidate_path),'symbol':symbol}],policy=policy,actor=actor)
            item=match['functions'][0]; result={'loop_id':loop_id,'status':'verified' if item['replacement_safe'] else 'rejected','compile':compile_result,'match_run_id':match['run_id'],'match':item,'source_sha256':sha256_file(source_path),'candidate_sha256':sha256_file(candidate_path)}
        with self.store.transaction() as c:
            c.execute('UPDATE native_loop_runs SET status=?,result_json=?,updated_at=? WHERE loop_id=?',(result['status'],canonical_json(result),utc_now(),loop_id))
            self.store.audit(actor,'native.loop.run',loop_id,{'status':result['status'],'function_id':function_id},connection=c)
        return result

    def show(self,loop_id:str)->dict[str,Any]:
        """Show closed loop."""
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM native_loop_runs WHERE loop_id=?',(loop_id,)).fetchone()
            if row is None: raise KeyError(loop_id)
            return self.store.decode(row,'compile_command_json','result_json')

    def list(self)->list[dict[str,Any]]:
        """List records in closed loop."""
        with self.store.connect() as c: return [self.store.decode(row,'compile_command_json','result_json') for row in c.execute('SELECT * FROM native_loop_runs ORDER BY created_at')]
