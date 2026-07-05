"""Provide x86decomp.reconstruction.capsules functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, sha256_file, utc_now
from .store import ReconstructionStore

class Capsules:
    """Represent capsules state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()
    def create(self,name:str,output:str|Path,*,include:list[str],external_requirements:list[dict[str,Any]]|None=None,actor:str='analyst')->dict[str,Any]:
        """Create the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        output=Path(output); output.parent.mkdir(parents=True,exist_ok=True)
        members=[]
        for raw in include:
            rel=ensure_relative_path(raw); src=self.store.project_root/rel
            if not src.is_file() or src.is_symlink(): raise ContractError(f'capsule member missing or unsafe: {raw}')
            members.append((rel.as_posix(),src))
        manifest={'schema':'x86decomp.capsule.v1','toolkit_version':'0.7.9','project_root_name':self.store.project_root.name,'members':[{'path':n,'sha256':sha256_file(p),'size':p.stat().st_size} for n,p in sorted(members)],'external_requirements':external_requirements or [],'audit_tip':self.store.verify_audit_chain()['tip_hash']}
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            info=zipfile.ZipInfo('capsule-manifest.json',(1980,1,1,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED; z.writestr(info,json.dumps(manifest,indent=2,sort_keys=True)+'\n')
            for name_,src in sorted(members):
                info=zipfile.ZipInfo('project/'+name_,(1980,1,1,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED; z.writestr(info,src.read_bytes())
        cid=random_id('capsule'); digest=sha256_file(output)
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_capsules VALUES(?,?,?,?,?,?,?)',(cid,name,canonical_json(manifest),str(output.resolve()),digest,'created',utc_now())); self.store.audit(actor,'reconstruction.capsule.create',cid,{'name':name,'archive_sha256':digest,'members':len(members)},connection=c)
        return {'capsule_id':cid,'name':name,'archive_path':str(output.resolve()),'archive_sha256':digest,'manifest':manifest}
    def inspect(self,path:str|Path)->dict[str,Any]:
        """Inspect the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with zipfile.ZipFile(path) as z:
            manifest=json.loads(z.read('capsule-manifest.json')); names=sorted(z.namelist())
        return {'path':str(Path(path).resolve()),'manifest':manifest,'members':names,'archive_sha256':sha256_file(path)}
    def verify(self,path:str|Path)->dict[str,Any]:
        """Verify the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        failures=[]
        try:
            with zipfile.ZipFile(path) as z:
                manifest=json.loads(z.read('capsule-manifest.json'))
                for member in manifest['members']:
                    name='project/'+member['path']
                    try: data=z.read(name)
                    except KeyError: failures.append({'path':member['path'],'error':'missing'}); continue
                    import hashlib
                    actual=hashlib.sha256(data).hexdigest()
                    if actual!=member['sha256'] or len(data)!=member['size']: failures.append({'path':member['path'],'error':'digest-or-size','actual_sha256':actual})
        except (OSError,zipfile.BadZipFile,KeyError,json.JSONDecodeError) as exc: failures.append({'error':type(exc).__name__,'message':str(exc)})
        return {'path':str(Path(path).resolve()),'valid':not failures,'failures':failures}
    def reproduce(self,path:str|Path,destination:str|Path)->dict[str,Any]:
        """Implement reproduce.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        verification=self.verify(path)
        if not verification['valid']: raise ContractError('capsule verification failed')
        destination=Path(destination); destination.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(path) as z:
            for info in z.infolist():
                if not info.filename.startswith('project/'): continue
                rel=ensure_relative_path(info.filename.removeprefix('project/')); target=destination/rel; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(z.read(info))
        return {'destination':str(destination.resolve()),'verified':True,'claim':'files reproduced; external requirements remain caller-supplied'}
