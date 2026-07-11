"""Identify and disposition likely library functions."""
from __future__ import annotations

from typing import Any
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import ReconstructionStore

class LibraryRecognition:
    """Identify probable library functions and record analyst dispositions."""
    def __init__(self,store:ReconstructionStore):
        """Initialize LibraryRecognition with `store`."""
        self.store=store; store.initialize()
    def identify(self,subject_id:str,library_name:str,*,version_range:str|None=None,confidence:float,evidence:list[dict[str,Any]],actor:str='analyst')->dict[str,Any]:
        """Identify likely library functions from the supplied evidence."""
        if not 0<=confidence<=1: raise ContractError('confidence must be between 0 and 1')
        if not evidence: raise ContractError('library match requires evidence')
        mid=random_id('libmatch'); now=utc_now()
        with self.store.transaction() as c:
            c.execute('INSERT INTO reconstruction_library_matches VALUES(?,?,?,?,?,?,?,?,?)',(mid,subject_id,library_name,version_range,confidence,canonical_json(evidence),'proposed',now,now)); self.store.audit(actor,'reconstruction.library.identify',mid,{'subject_id':subject_id,'library_name':library_name,'version_range':version_range,'confidence':confidence},connection=c)
        return self.get(mid)
    def get(self,match_id:str)->dict[str,Any]:
        """Return data from library recognition."""
        with self.store.connect() as c: row=c.execute('SELECT * FROM reconstruction_library_matches WHERE match_id=?',(match_id,)).fetchone()
        if not row: raise KeyError(match_id)
        return self.store.decode(row,'evidence_json')
    def candidates(self,subject_id:str)->list[dict[str,Any]]:
        """Return candidate library matches recorded for a function."""
        with self.store.connect() as c: ids=[r[0] for r in c.execute('SELECT match_id FROM reconstruction_library_matches WHERE subject_id=? ORDER BY confidence DESC,library_name',(subject_id,))]
        return [self.get(x) for x in ids]
    def disposition(self,match_id:str,disposition:str,*,actor:str='analyst')->dict[str,Any]:
        """Record the analyst disposition for a library candidate."""
        if disposition not in {'accepted','externalized','reconstruct','rejected'}: raise ContractError('invalid library disposition')
        with self.store.transaction() as c:
            if not c.execute('SELECT 1 FROM reconstruction_library_matches WHERE match_id=?',(match_id,)).fetchone(): raise KeyError(match_id)
            c.execute('UPDATE reconstruction_library_matches SET disposition=?,updated_at=? WHERE match_id=?',(disposition,utc_now(),match_id)); self.store.audit(actor,'reconstruction.library.disposition',match_id,{'disposition':disposition},connection=c)
        return self.get(match_id)
