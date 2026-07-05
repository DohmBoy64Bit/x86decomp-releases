"""Provide x86decomp.reconstruction.project_layout functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, utc_now
from .store import ReconstructionStore

class ProjectLayout:
    """Represent project layout state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: ReconstructionStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store=store; store.initialize()

    def create_module(self, name: str, *, kind: str='static-library', source_path: str|None=None, confidence: float=1.0, evidence: list[dict[str,Any]]|None=None, actor: str='analyst') -> dict[str,Any]:
        """Create module.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if kind not in {'executable','static-library','shared-library','resource','support'}: raise ContractError('invalid module kind')
        if not 0 <= confidence <= 1: raise ContractError('confidence must be between 0 and 1')
        if source_path is not None: source_path=ensure_relative_path(source_path).as_posix()
        module_id=random_id('module'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_modules VALUES(?,?,?,?,?,?,?,?,?)',(module_id,name,kind,source_path,confidence,canonical_json(evidence or []),'proposed',now,now))
            self.store.audit(actor,'reconstruction.module.create',module_id,{'name':name,'kind':kind,'source_path':source_path,'confidence':confidence},connection=c)
        return self.show_module(module_id)

    def add_member(self, module_id: str, member_kind: str, member_id: str, *, ordinal: int=0, evidence: list[dict[str,Any]]|None=None, actor: str='analyst') -> dict[str,Any]:
        """Add member.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if member_kind not in {'function','global','resource','object','translation-unit','library'}: raise ContractError('invalid member kind')
        with self.store.transaction() as c:
            if not c.execute('SELECT 1 FROM reconstruction_modules WHERE module_id=?',(module_id,)).fetchone(): raise KeyError(module_id)
            c.execute('INSERT OR REPLACE INTO reconstruction_module_members VALUES(?,?,?,?,?)',(module_id,member_kind,member_id,ordinal,canonical_json(evidence or [])))
            c.execute('UPDATE reconstruction_modules SET updated_at=? WHERE module_id=?',(utc_now(),module_id))
            self.store.audit(actor,'reconstruction.module.member',module_id,{'member_kind':member_kind,'member_id':member_id,'ordinal':ordinal},connection=c)
        return self.show_module(module_id)

    def create_translation_unit(self, source_path: str, *, module_id: str|None=None, language: str='cpp', confidence: float=1.0, evidence: list[dict[str,Any]]|None=None, actor: str='analyst') -> dict[str,Any]:
        """Create translation unit.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        source_path=ensure_relative_path(source_path).as_posix()
        if language not in {'c','cpp','asm','resource'}: raise ContractError('invalid translation-unit language')
        if not 0 <= confidence <= 1: raise ContractError('confidence must be between 0 and 1')
        unit_id=random_id('tu'); now=utc_now()
        with self.store.transaction() as c:
            if module_id and not c.execute('SELECT 1 FROM reconstruction_modules WHERE module_id=?',(module_id,)).fetchone(): raise KeyError(module_id)
            c.execute('INSERT INTO reconstruction_translation_units VALUES(?,?,?,?,?,?,?,?)',(unit_id,module_id,source_path,language,confidence,canonical_json(evidence or []),now,now))
            if module_id: c.execute('INSERT OR IGNORE INTO reconstruction_module_members VALUES(?,?,?,?,?)',(module_id,'translation-unit',unit_id,0,'[]'))
            self.store.audit(actor,'reconstruction.translation_unit.create',unit_id,{'source_path':source_path,'module_id':module_id,'language':language},connection=c)
        return self.show_translation_unit(unit_id)

    def add_translation_unit_member(self, unit_id: str, member_kind: str, member_id: str, *, linkage: str='external', ordinal: int=0, actor: str='analyst') -> dict[str,Any]:
        """Add translation unit member.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if linkage not in {'external','internal','weak','comdat'}: raise ContractError('invalid linkage')
        with self.store.transaction() as c:
            if not c.execute('SELECT 1 FROM reconstruction_translation_units WHERE unit_id=?',(unit_id,)).fetchone(): raise KeyError(unit_id)
            c.execute('INSERT OR REPLACE INTO reconstruction_translation_unit_members VALUES(?,?,?,?,?)',(unit_id,member_kind,member_id,linkage,ordinal))
            c.execute('UPDATE reconstruction_translation_units SET updated_at=? WHERE unit_id=?',(utc_now(),unit_id))
            self.store.audit(actor,'reconstruction.translation_unit.member',unit_id,{'member_kind':member_kind,'member_id':member_id,'linkage':linkage,'ordinal':ordinal},connection=c)
        return self.show_translation_unit(unit_id)

    def synthesize(self, inventory: list[dict[str,Any]], *, actor: str='planner') -> dict[str,Any]:
        """Deterministically group inventory records by explicit object/library/source hints.

        It never invents original filenames: absent hints go to an explicit unknown module.
        """
        groups: dict[str,list[dict[str,Any]]]={}
        for item in inventory:
            if not isinstance(item,dict) or 'id' not in item: raise ContractError('inventory items require id')
            hint=str(item.get('object_file') or item.get('library') or item.get('source_hint') or 'unknown')
            groups.setdefault(hint,[]).append(item)
        created=[]
        for index,(hint,items) in enumerate(sorted(groups.items())):
            safe='unknown' if hint=='unknown' else Path(hint).stem.replace(' ','_') or f'module_{index}'
            name=f'inferred_{safe}'
            module=self.create_module(name,kind='support',source_path=None,confidence=0.25 if hint=='unknown' else 0.75,evidence=[{'kind':'inventory_hint','value':hint}],actor=actor)
            for ordinal,item in enumerate(sorted(items,key=lambda x:str(x['id']))): self.add_member(module['module_id'],str(item.get('kind','function')),str(item['id']),ordinal=ordinal,evidence=[{'kind':'grouping_hint','value':hint}],actor=actor)
            created.append(self.show_module(module['module_id']))
        return {'modules':created,'input_count':len(inventory),'unknown_group_present':'unknown' in groups}

    def show_module(self,module_id:str)->dict[str,Any]:
        """Implement show module.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_modules WHERE module_id=?',(module_id,)).fetchone()
            if not row: raise KeyError(module_id)
            result=self.store.decode(row,'evidence_json')
            result['members']=[self.store.decode(r,'evidence_json') for r in c.execute('SELECT * FROM reconstruction_module_members WHERE module_id=? ORDER BY ordinal,member_kind,member_id',(module_id,))]
        return result

    def show_translation_unit(self,unit_id:str)->dict[str,Any]:
        """Implement show translation unit.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_translation_units WHERE unit_id=?',(unit_id,)).fetchone()
            if not row: raise KeyError(unit_id)
            result=self.store.decode(row,'evidence_json')
            result['members']=[dict(r) for r in c.execute('SELECT * FROM reconstruction_translation_unit_members WHERE unit_id=? ORDER BY ordinal,member_kind,member_id',(unit_id,))]
        return result

    def list_modules(self)->list[dict[str,Any]]:
        """List modules.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as c: ids=[r[0] for r in c.execute('SELECT module_id FROM reconstruction_modules ORDER BY name')]
        return [self.show_module(x) for x in ids]

    def explain_boundaries(self,module_id:str)->dict[str,Any]:
        """Implement explain boundaries.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        module=self.show_module(module_id)
        return {'module_id':module_id,'name':module['name'],'confidence':module['confidence'],'status':module['status'],'evidence':module['evidence'],'members':[{'kind':m['member_kind'],'id':m['member_id'],'ordinal':m['ordinal'],'evidence':m['evidence']} for m in module['members']], 'claim':'inferred module boundary; not original-source attribution'}

    def export(self,path:str|Path)->dict[str,Any]:
        """Export the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        out=Path(path); out.parent.mkdir(parents=True,exist_ok=True)
        payload={'schema':'x86decomp.project-layout.v1','modules':self.list_modules()}
        out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        return {'path':str(out.resolve()),'modules':len(payload['modules'])}
