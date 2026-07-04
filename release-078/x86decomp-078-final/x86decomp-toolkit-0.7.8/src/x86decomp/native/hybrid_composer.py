from __future__ import annotations

from pathlib import Path
from typing import Any

from x86decomp.pe import parse_pe
from x86decomp.util import sha256_file
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .matching import FunctionMatching, compare_function_bytes, extract_candidate, rva_to_file_offset
from .store import NativeStore


class HybridComposer:
    def __init__(self, store: NativeStore): self.store=store; store.initialize()

    def compose(self, run_id:str, output_path:Path, *, actor:str='analyst')->dict[str,Any]:
        report=FunctionMatching(self.store).report(run_id)
        original_path=Path(report['original_path'])
        if sha256_file(original_path) != report['original_sha256']:
            raise ContractError('original image changed after match verification')
        image=parse_pe(original_path); original=original_path.read_bytes(); result=bytearray(original)
        promoted=[]; fallbacks=[]
        for match in report['functions']:
            if not match['replacement_safe']:
                fallbacks.append({'function_id':match['function_id'],'reason':match['classification']}); continue
            candidate_path=Path(match['candidate_path'])
            if sha256_file(candidate_path) != match['candidate_sha256']:
                raise ContractError(f"candidate changed after verification: {match['function_id']}")
            candidate=extract_candidate(candidate_path,symbol=match['details'].get('symbol'))
            slot_size=int(match['slot_size'])
            if len(candidate)>slot_size:
                raise ContractError(f"candidate grew after verification: {match['function_id']}")
            offset=rva_to_file_offset(image,int(match['rva']))
            original_slot=original[offset:offset+slot_size]
            verification=compare_function_bytes(
                original_slot,
                candidate,
                policy=report['comparison_policy'],
                pad_bytes=report['pad_bytes'],
                protected_offsets=match['details'].get('protected_offsets',[]),
            )
            if not verification['replacement_safe']:
                raise ContractError(f"candidate no longer matches verified slot: {match['function_id']}")
            result[offset:offset+len(candidate)]=candidate
            promoted.append({'function_id':match['function_id'],'rva':match['rva'],'bytes_replaced':len(candidate),'classification':match['classification']})
        output_path=output_path.resolve(); output_path.parent.mkdir(parents=True,exist_ok=True); output_path.write_bytes(bytes(result)); parse_pe(output_path)
        composition_id=random_id('compose'); now=utc_now(); preserved=[s.name for s in image.sections if s.name!='.text']
        summary={'composition_id':composition_id,'run_id':run_id,'original':str(original_path),'output':str(output_path),'output_sha256':sha256_file(output_path),'promoted_count':len(promoted),'fallback_count':len(fallbacks),'promoted':promoted,'fallbacks':fallbacks,'preserved_sections':preserved,'container_size_preserved':len(result)==len(original)}
        with self.store.transaction() as c:
            c.execute('INSERT INTO native_hybrid_compositions VALUES(?,?,?,?,?,?,?,?,?,?)',(composition_id,run_id,str(original_path),str(output_path),summary['output_sha256'],len(promoted),len(fallbacks),canonical_json(preserved),canonical_json(summary),now))
            self.store.audit(actor,'native.hybrid.compose',composition_id,{'promoted':len(promoted),'fallbacks':len(fallbacks)},connection=c)
        return summary

    def verify(self, composition_id:str)->dict[str,Any]:
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM native_hybrid_compositions WHERE composition_id=?',(composition_id,)).fetchone()
            if row is None: raise KeyError(composition_id)
            item=self.store.decode(row,'preserved_sections_json','report_json'); output=Path(item['output_path'])
            checks={'exists':output.is_file(),'sha256_matches':output.is_file() and sha256_file(output)==item['output_sha256'],'pe_parses':False}
            if output.is_file():
                try: parse_pe(output); checks['pe_parses']=True
                except Exception: checks['pe_parses']=False
            return {**item,'checks':checks,'passed':all(checks.values())}
