"""Manage reconstruction build systems, targets, variants, and generated build contracts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, utc_now
from .store import ReconstructionStore

class BuildManager:
    """Manage reconstruction build systems, targets, variants, and validations."""
    def __init__(self,store:ReconstructionStore):
        """Initialize the instance with validated constructor state."""
        self.store=store; store.initialize()
    def create(self,name:str,*,mode:str,generator:str='cmake',output_root:str='build',metadata:dict[str,Any]|None=None,actor:str='analyst')->dict[str,Any]:
        """Create a build system record and audit its creation.

        Args:
            name: Human-readable build system name.
            mode: Either ``historical`` or ``portable``.
            generator: Build generator to use; one of ``cmake``, ``make``,
                ``ninja``, ``msvc-project``, or ``response-file``.
            output_root: Project-relative directory for generated build files.
            metadata: Optional metadata mapping stored as canonical JSON.
            actor: Actor recorded in the audit log.

        Returns:
            The build record as produced by :meth:`show`.

        Raises:
            ContractError: If ``mode`` or ``generator`` is not supported.
        """
        if mode not in {'historical','portable'}: raise ContractError('build mode must be historical or portable')
        if generator not in {'cmake','make','ninja','msvc-project','response-file'}: raise ContractError('unsupported build generator')
        output_root=ensure_relative_path(output_root).as_posix(); bid=random_id('build'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_build_systems VALUES(?,?,?,?,?,?,?,?)',(bid,name,mode,generator,output_root,canonical_json(metadata or {}),now,now))
            self.store.audit(actor,'reconstruction.build.create',bid,{'name':name,'mode':mode,'generator':generator},connection=c)
        return self.show(bid)
    def add_target(self,build_id:str,name:str,*,kind:str='executable',output_name:str|None=None,sources:list[str]|None=None,dependencies:list[str]|None=None,actor:str='analyst')->dict[str,Any]:
        """Add a build target to an existing build system.

        Args:
            build_id: Identifier of the owning build system.
            name: Target name.
            kind: Target kind; one of ``executable``, ``static-library``,
                ``shared-library``, or ``resource``.
            output_name: Optional output artifact name; defaults to ``name``.
            sources: Optional project-relative source paths.
            dependencies: Optional list of dependency target names.
            actor: Actor recorded in the audit log.

        Returns:
            The target record as produced by :meth:`show_target`.

        Raises:
            ContractError: If ``kind`` is not a valid target kind.
            KeyError: If ``build_id`` does not exist.
        """
        if kind not in {'executable','static-library','shared-library','resource'}: raise ContractError('invalid target kind')
        clean=[ensure_relative_path(x).as_posix() for x in (sources or [])]; tid=random_id('target')
        with self.store.transaction() as c:
            if not c.execute('SELECT 1 FROM reconstruction_build_systems WHERE build_id=?',(build_id,)).fetchone(): raise KeyError(build_id)
            c.execute('INSERT INTO reconstruction_build_targets VALUES(?,?,?,?,?,?,?)',(tid,build_id,name,kind,output_name or name,canonical_json(clean),canonical_json(dependencies or [])))
            self.store.audit(actor,'reconstruction.build.target',tid,{'build_id':build_id,'name':name,'kind':kind},connection=c)
        return self.show_target(tid)
    def add_variant(self,target_id:str,name:str,*,compiler:str,linker:str,compile_flags:list[str]|None=None,link_flags:list[str]|None=None,environment:dict[str,str]|None=None,actor:str='analyst')->dict[str,Any]:
        """Add a compiler/linker variant to an existing target.

        Args:
            target_id: Identifier of the owning target.
            name: Variant name.
            compiler: Compiler identity for the variant.
            linker: Linker identity for the variant.
            compile_flags: Optional compile flags stored as canonical JSON.
            link_flags: Optional link flags stored as canonical JSON.
            environment: Optional environment variables for the variant.
            actor: Actor recorded in the audit log.

        Returns:
            The variant record as produced by :meth:`show_variant`.

        Raises:
            KeyError: If ``target_id`` does not exist.
        """
        vid=random_id('variant')
        with self.store.transaction() as c:
            if not c.execute('SELECT 1 FROM reconstruction_build_targets WHERE target_id=?',(target_id,)).fetchone(): raise KeyError(target_id)
            c.execute('INSERT INTO reconstruction_build_variants VALUES(?,?,?,?,?,?,?,?)',(vid,target_id,name,compiler,linker,canonical_json(compile_flags or []),canonical_json(link_flags or []),canonical_json(environment or {})))
            self.store.audit(actor,'reconstruction.build.variant',vid,{'target_id':target_id,'name':name,'compiler':compiler,'linker':linker},connection=c)
        return self.show_variant(vid)
    def show(self,build_id:str)->dict[str,Any]:
        """Return a build system record with its nested targets.

        Args:
            build_id: Identifier of the build system.

        Returns:
            The decoded build record with a ``targets`` list ordered by name.

        Raises:
            KeyError: If ``build_id`` does not exist.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_build_systems WHERE build_id=?',(build_id,)).fetchone()
            if not row: raise KeyError(build_id)
            out=self.store.decode(row,'metadata_json'); out['targets']=[self.show_target(r[0]) for r in c.execute('SELECT target_id FROM reconstruction_build_targets WHERE build_id=? ORDER BY name',(build_id,))]
        return out
    def show_target(self,target_id:str)->dict[str,Any]:
        """Return a target record with its nested variants.

        Args:
            target_id: Identifier of the target.

        Returns:
            The decoded target record with a ``variants`` list ordered by name.

        Raises:
            KeyError: If ``target_id`` does not exist.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_build_targets WHERE target_id=?',(target_id,)).fetchone()
            if not row: raise KeyError(target_id)
            out=self.store.decode(row,'sources_json','dependencies_json'); out['variants']=[self.show_variant(r[0]) for r in c.execute('SELECT variant_id FROM reconstruction_build_variants WHERE target_id=? ORDER BY name',(target_id,))]
        return out
    def show_variant(self,variant_id:str)->dict[str,Any]:
        """Return a single build variant record.

        Args:
            variant_id: Identifier of the variant.

        Returns:
            The decoded variant record with flags and environment.

        Raises:
            KeyError: If ``variant_id`` does not exist.
        """
        with self.store.connect() as c:
            row=c.execute('SELECT * FROM reconstruction_build_variants WHERE variant_id=?',(variant_id,)).fetchone()
        if not row: raise KeyError(variant_id)
        return self.store.decode(row,'compile_flags_json','link_flags_json','environment_json')
    def generate(self,build_id:str,*,output_root:str|Path|None=None)->dict[str,Any]:
        """Render a build contract file for a build system.

        Emits ``CMakeLists.txt`` for the cmake generator, a ``Makefile.recovered``
        for make/ninja, or a JSON ``build-contract.json`` otherwise.

        Args:
            build_id: Identifier of the build system to render.
            output_root: Optional output directory; defaults to the store's
                project root.

        Returns:
            A mapping describing the build id, mode, generator, written path,
            target count, and a provenance claim string.
        """
        build=self.show(build_id); root=Path(output_root or self.store.project_root)
        if build['generator']=='cmake':
            lines=['cmake_minimum_required(VERSION 3.20)',f'project({build["name"]} LANGUAGES C CXX)','']
            for t in build['targets']:
                src=' '.join(t['sources'])
                command={'executable':'add_executable','static-library':'add_library','shared-library':'add_library','resource':'add_custom_target'}[t['target_kind']]
                extra=' STATIC' if t['target_kind']=='static-library' else (' SHARED' if t['target_kind']=='shared-library' else '')
                lines.append(f'{command}({t["name"]}{extra} {src})'.rstrip())
                for dep in t['dependencies']: lines.append(f'target_link_libraries({t["name"]} PRIVATE {dep})')
            content='\n'.join(lines)+'\n'; relative='CMakeLists.txt'
        elif build['generator'] in {'make','ninja'}:
            lines=['# Generated by x86decomp-toolkit 0.7.11; review compiler identity before use.','']
            for t in build['targets']: lines.append(f'{t["output_name"]}: {" ".join(t["sources"])}\n\t@echo Build contract for {t["name"]}')
            content='\n'.join(lines)+'\n'; relative='Makefile.recovered'
        else:
            payload={'schema':'x86decomp.build-contract.v1','build':build}; content=json.dumps(payload,indent=2,sort_keys=True)+'\n'; relative='build-contract.json'
        dest=root/relative; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(content,encoding='utf-8')
        return {'build_id':build_id,'mode':build['mode'],'generator':build['generator'],'path':str(dest.resolve()),'target_count':len(build['targets']),'claim':'generated build contract; historical mode requires exact declared toolchain'}
    def validate(self,target_id:str,variant_id:str|None=None,*,actor:str='validator')->dict[str,Any]:
        """Validate a target's sources and variant, recording the result.

        Checks that sources are declared and exist, that a variant is declared,
        and, for historical builds, that the variant names both compiler and
        linker explicitly.

        Args:
            target_id: Identifier of the target to validate.
            variant_id: Optional variant to validate; defaults to the target's
                first variant when present.
            actor: Actor recorded in the audit log.

        Returns:
            A mapping with the validation id, pass/fail status, individual
            checks, and any missing source paths.
        """
        target=self.show_target(target_id); variant=self.show_variant(variant_id) if variant_id else (target['variants'][0] if target['variants'] else None)
        missing=[s for s in target['sources'] if not (self.store.project_root/s).is_file()]
        checks={'sources_declared':bool(target['sources']),'sources_exist':not missing,'variant_declared':variant is not None,'historical_identity_explicit':True}
        if variant and self.show(target['build_id'])['mode']=='historical': checks['historical_identity_explicit']=bool(variant['compiler'] and variant['linker'])
        status='passed' if all(checks.values()) else 'failed'; vid=random_id('buildval')
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_build_validations VALUES(?,?,?,?,?,?)',(vid,target_id,variant_id,status,canonical_json({'checks':checks,'missing_sources':missing}),utc_now()))
            self.store.audit(actor,'reconstruction.build.validate',vid,{'target_id':target_id,'variant_id':variant_id,'status':status},connection=c)
        return {'validation_id':vid,'status':status,'checks':checks,'missing_sources':missing}
    def compare_modes(self,historical_build_id:str,portable_build_id:str)->dict[str,Any]:
        """Compare a historical build against a portable build.

        Args:
            historical_build_id: Identifier of the historical-mode build.
            portable_build_id: Identifier of the portable-mode build.

        Returns:
            A mapping of each build's target names and the set of shared target
            names.

        Raises:
            ContractError: If the builds are not in historical then portable
                mode respectively.
        """
        h,p=self.show(historical_build_id),self.show(portable_build_id)
        if h['mode']!='historical' or p['mode']!='portable': raise ContractError('compare-modes requires historical then portable builds')
        return {'historical':historical_build_id,'portable':portable_build_id,'target_names':{'historical':[t['name'] for t in h['targets']],'portable':[t['name'] for t in p['targets']]},'shared_targets':sorted(set(t['name'] for t in h['targets'])&set(t['name'] for t in p['targets'])),'claims_separated':True}
    def matrix(self)->dict[str,Any]:
        """Return the target-by-mode variant matrix across all builds.

        Returns:
            A mapping with a ``matrix`` of target name to mode to variant names
            (``<none>`` where a target has no variant) and the target count.
        """
        with self.store.connect() as c: rows=c.execute('SELECT b.mode,t.name,v.name FROM reconstruction_build_systems b JOIN reconstruction_build_targets t ON t.build_id=b.build_id LEFT JOIN reconstruction_build_variants v ON v.target_id=t.target_id ORDER BY t.name,b.mode,v.name').fetchall()
        matrix:dict[str,dict[str,list[str]]]={}
        for mode,target,variant in rows: matrix.setdefault(target,{}).setdefault(mode,[]).append(variant or '<none>')
        return {'matrix':matrix,'targets':len(matrix)}
