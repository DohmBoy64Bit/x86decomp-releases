"""Provide x86decomp.native.pe_reconstruction functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import struct
from pathlib import Path
from typing import Any, Iterable

from x86decomp.coff import (
    IMAGE_FILE_MACHINE_AMD64, IMAGE_FILE_MACHINE_I386,
    SyntheticSectionSpec, SyntheticSymbolSpec, write_synthetic_coff_object,
)
from x86decomp.pe import parse_pe
from x86decomp.util import sha256_bytes, sha256_file
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import NativeStore


def _section_header_records(data: bytes) -> list[dict[str, Any]]:
    """Implement section header records.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if len(data) < 0x40 or data[:2] != b"MZ": raise ContractError("not a PE image")
    pe = struct.unpack_from("<I", data, 0x3C)[0]
    if pe + 24 > len(data) or data[pe:pe+4] != b"PE\0\0": raise ContractError("invalid PE signature")
    count = struct.unpack_from("<H", data, pe + 6)[0]
    optional_size = struct.unpack_from("<H", data, pe + 20)[0]
    start = pe + 24 + optional_size
    records = []
    for index in range(count):
        offset = start + index * 40
        if offset + 40 > len(data): raise ContractError("truncated PE section table")
        raw_name = data[offset:offset+8].split(b"\0", 1)[0]
        name = raw_name.decode("ascii", errors="replace")
        virtual_size, virtual_address, raw_size, raw_offset = struct.unpack_from("<IIII", data, offset + 8)
        characteristics = struct.unpack_from("<I", data, offset + 36)[0]
        records.append({"index": index, "header_offset": offset, "name": name, "virtual_size": virtual_size, "virtual_address": virtual_address, "raw_size": raw_size, "raw_offset": raw_offset, "characteristics": characteristics})
    return records


def plan_patch(original: bytes, operations: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Plan patch.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    planned: list[dict[str, Any]] = []
    occupied: list[tuple[int, int]] = []
    for raw in operations:
        offset = int(raw["offset"])
        expected = bytes.fromhex(str(raw["expected_hex"]))
        replacement = bytes.fromhex(str(raw["replacement_hex"]))
        if offset < 0 or offset + len(expected) > len(original): raise ContractError("patch operation lies outside image")
        if len(expected) != len(replacement): raise ContractError("safe patch operations must preserve length")
        if original[offset:offset+len(expected)] != expected: raise ContractError(f"patch precondition mismatch at 0x{offset:x}")
        interval = (offset, offset + len(expected))
        if any(max(interval[0], left) < min(interval[1], right) for left, right in occupied): raise ContractError("overlapping patch operations")
        occupied.append(interval)
        planned.append({"offset": offset, "expected_hex": expected.hex(), "replacement_hex": replacement.hex(), "reason": str(raw.get("reason", "unspecified"))})
    return sorted(planned, key=lambda item: item["offset"])


def apply_operations(original: bytes, operations: Iterable[dict[str, Any]]) -> bytes:
    """Apply operations.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    planned = plan_patch(original, operations)
    result = bytearray(original)
    for operation in planned:
        offset = operation["offset"]
        replacement = bytes.fromhex(operation["replacement_hex"])
        result[offset:offset+len(replacement)] = replacement
    return bytes(result)


class PEReconstruction:
    """Represent p e reconstruction state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: NativeStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()

    def inventory(self, image_path: Path) -> dict[str, Any]:
        """Implement inventory.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        image = parse_pe(image_path)
        return {"path": str(image_path.resolve()), "architecture": image.to_dict()["architecture"], "entry_rva": image.entry_rva, "size_of_image": image.size_of_image, "sections": [section.to_dict() for section in image.sections], "directories": [directory.to_dict() for directory in image.directories]}

    def export_sections(self, image_path: Path, output_root: Path, *, names: Iterable[str] | None=None) -> dict[str, Any]:
        """Export sections.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        image_path=image_path.resolve(); output_root=output_root.resolve(); output_root.mkdir(parents=True,exist_ok=True)
        data=image_path.read_bytes(); selected=set(names or [section.name for section in parse_pe(image_path).sections])
        records=[]
        for section in parse_pe(image_path).sections:
            if section.name not in selected: continue
            payload=data[section.raw_offset:section.raw_offset+section.raw_size]
            safe_name=section.name.lstrip('.') or 'unnamed'
            path=output_root/f"{safe_name}.bin"; path.write_bytes(payload)
            records.append({**section.to_dict(),"path":str(path),"sha256":sha256_bytes(payload)})
        manifest={"schema_version":1,"source":str(image_path),"source_sha256":sha256_file(image_path),"sections":records}
        (output_root/'sections.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        return manifest

    def export_coff(self, image_path: Path, output_root: Path, *, names: Iterable[str] | None=None) -> dict[str, Any]:
        """Export coff.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        image=parse_pe(image_path); output_root=output_root.resolve(); output_root.mkdir(parents=True,exist_ok=True)
        data=Path(image_path).read_bytes(); selected=set(names or [s.name for s in image.sections if s.name != '.text'])
        machine=IMAGE_FILE_MACHINE_I386 if image.to_dict()['architecture']=='x86' else IMAGE_FILE_MACHINE_AMD64
        outputs=[]
        for section in image.sections:
            if section.name not in selected: continue
            payload=data[section.raw_offset:section.raw_offset+section.raw_size]
            path=output_root/f"{section.name.lstrip('.') or 'unnamed'}.o"
            write_synthetic_coff_object(path,sections=[SyntheticSectionSpec(section.name,payload,section.characteristics)],symbols=[SyntheticSymbolSpec(f"__x86decomp_{section.name.lstrip('.') or 'section'}",1)],machine=machine)
            outputs.append({"section":section.name,"path":str(path),"sha256":sha256_file(path)})
        return {"source":str(Path(image_path).resolve()),"objects":outputs}

    def create_plan(self, original_path: Path, output_path: Path, operations: Iterable[dict[str,Any]], *, actor:str='analyst')->dict[str,Any]:
        """Create plan.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        original_path=original_path.resolve(); data=original_path.read_bytes(); planned=plan_patch(data,operations); plan_id=random_id('patch'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO native_patch_plans VALUES(?,?,?,?,?,?,?,?)',(plan_id,str(original_path),sha256_file(original_path),str(output_path.resolve()),canonical_json(planned),'planned',now,now))
            self.store.audit(actor,'native.pe.patch.plan',plan_id,{'operation_count':len(planned)},connection=c)
        return {'plan_id':plan_id,'operations':planned,'original_sha256':sha256_file(original_path),'output_path':str(output_path.resolve())}

    def apply_plan(self, plan_id:str, *, actor:str='analyst')->dict[str,Any]:
        """Apply plan.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.transaction() as c:
            row=c.execute('SELECT * FROM native_patch_plans WHERE plan_id=?',(plan_id,)).fetchone()
            if row is None: raise KeyError(plan_id)
            plan=self.store.decode(row,'operations_json'); original=Path(plan['original_path']); output=Path(plan['output_path'])
            if sha256_file(original)!=plan['original_sha256']: raise ContractError('original image changed after patch plan creation')
            result=apply_operations(original.read_bytes(),plan['operations']); output.parent.mkdir(parents=True,exist_ok=True); output.write_bytes(result)
            c.execute("UPDATE native_patch_plans SET status='applied',updated_at=? WHERE plan_id=?",(utc_now(),plan_id))
            self.store.audit(actor,'native.pe.patch.apply',plan_id,{'output_sha256':sha256_file(output)},connection=c)
        return {'plan_id':plan_id,'output':str(output.resolve()),'output_sha256':sha256_file(output),'size_preserved':output.stat().st_size==original.stat().st_size}

    def text_swap(self, original_path:Path, replacement_path:Path, output_path:Path, *, section_name:str='.text', actor:str='analyst')->dict[str,Any]:
        """Implement text swap.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        original=original_path.resolve().read_bytes(); replacement=replacement_path.resolve().read_bytes(); sections=_section_header_records(original)
        section=next((item for item in sections if item['name']==section_name),None)
        if section is None: raise ContractError(f'PE section not found: {section_name}')
        if len(replacement)>section['raw_size']: raise ContractError('replacement section exceeds original raw allocation')
        expected=original[section['raw_offset']:section['raw_offset']+section['raw_size']]
        replacement_full=replacement+expected[len(replacement):]
        plan=self.create_plan(original_path,output_path,[{'offset':section['raw_offset'],'expected_hex':expected.hex(),'replacement_hex':replacement_full.hex(),'reason':f'RVA-stable {section_name} container-preserving replacement'}],actor=actor)
        applied=self.apply_plan(plan['plan_id'],actor=actor)
        parsed=parse_pe(output_path)
        return {**applied,'section':section_name,'virtual_size_preserved':next(s for s in parsed.sections if s.name==section_name).virtual_size==section['virtual_size'],'raw_size_preserved':next(s for s in parsed.sections if s.name==section_name).raw_size==section['raw_size']}
