"""Static and (opt-in) live runtime validation of reconstructed native PE images."""
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
    """Validate reconstructed PE images and map crash addresses back to function slots."""
    def __init__(self,store:NativeStore):
        """Initialize the instance with validated constructor state."""
        self.store=store; store.initialize()

    def validate_image(self,image_path:Path, *, actor:str='analyst')->dict[str,Any]:
        """Run static structural checks on a PE image without executing it.

        Verifies that the PE parses, the entry point falls inside a section, sections do not
        overlap, and the headers fit within the file, recording the result as a validation entry.

        Args:
            image_path: Path to the PE image to inspect; resolved before use.
            actor: Actor name attributed to the audit entry.

        Returns:
            The recorded validation dictionary augmented with a ``passed`` flag that is true only
            when every check succeeded.
        """
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
        """Launch a reconstructed image as a subprocess after static validation.

        The image is validated first, then executed only with explicit consent. Timeouts are
        captured as a failed ``completed_before_timeout`` check rather than raising.

        Args:
            image_path: Path to the PE image to launch; resolved before use.
            execute: Must be ``True`` to actually run the image.
            timeout_seconds: Positive per-run timeout in seconds.
            arguments: Optional command-line arguments passed to the image.
            actor: Actor name attributed to the audit entry.

        Returns:
            The recorded validation dictionary augmented with a ``passed`` flag reflecting whether
            the process was created.

        Raises:
            ContractError: If ``execute`` is not ``True``, the host is not Windows, or
                ``timeout_seconds`` is not positive.
        """
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
        """Resolve a crash RVA to the reconstructed function slot that contains it.

        Args:
            rva: Relative virtual address to look up.

        Returns:
            A dictionary with ``mapped`` set to ``False`` when no slot covers ``rva``; otherwise
            ``mapped`` is ``True`` with the containing function's identifier, base RVA, byte
            offset, and classification.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM native_function_slots WHERE rva<=? AND slot_end_rva>? ORDER BY rva DESC LIMIT 1',(rva,rva)).fetchone()
            if row is None: return {'rva':rva,'mapped':False}
            slot=self.store.decode(row,'evidence_json'); return {'rva':rva,'mapped':True,'function_id':slot['function_id'],'function_rva':slot['rva'],'offset':rva-slot['rva'],'classification':slot['classification']}

    def _record(self,path:Path,kind:str,checks:dict[str,Any],details:dict[str,Any],authorized:bool,actor:str)->dict[str,Any]:
        """Persist a validation entry and its audit record.

        Args:
            path: Path of the validated image.
            kind: Validation kind label (e.g. ``static-loader`` or ``native-launch``).
            checks: Mapping of check name to boolean outcome; all-true implies ``passed`` status.
            details: Supplementary detail payload stored as canonical JSON.
            authorized: Whether execution of the image was authorized.
            actor: Actor name attributed to the audit entry.

        Returns:
            A dictionary describing the stored validation, including its id, kind, status, checks,
            details, and authorization flag.
        """
        validation_id=random_id('runtime'); status='passed' if all(checks.values()) else 'failed'; now=utc_now()
        payload={'checks':checks,'details':details}
        with self.store.transaction() as c:
            c.execute('INSERT INTO native_runtime_validations VALUES(?,?,?,?,?,?,?,?)',(validation_id,str(path),sha256_file(path),kind,status,canonical_json(payload),int(authorized),now))
            self.store.audit(actor,'native.runtime.validate',validation_id,{'kind':kind,'status':status},connection=c)
        return {'validation_id':validation_id,'kind':kind,'status':status,'checks':checks,'details':details,'execution_authorized':authorized}
