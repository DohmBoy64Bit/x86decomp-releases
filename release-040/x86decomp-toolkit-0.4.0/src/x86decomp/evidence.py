"""Evidence store and strict three-independent-source claim verification."""

from __future__ import annotations

import re
import uuid
from pathlib import Path
from typing import Iterable

from .errors import ContractError, VerificationError
from .models import Claim, ClaimState, EvidenceItem, EvidenceKind
from .util import copy_file_atomic, load_json, sha256_file, utc_now, write_json

_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._:-]{2,127}$")


def _validate_id(value: str, field: str) -> None:
    if not _ID_RE.fullmatch(value):
        raise ContractError(
            f"{field} must match {_ID_RE.pattern!r}; received {value!r}"
        )


class EvidenceStore:
    """Filesystem-backed evidence and claims with deterministic validation rules."""

    def __init__(self, root: Path):
        self.root = root
        self.items_dir = root / "evidence" / "items"
        self.claims_dir = root / "evidence" / "claims"
        self.files_dir = root / "evidence" / "files"
        self.items_dir.mkdir(parents=True, exist_ok=True)
        self.claims_dir.mkdir(parents=True, exist_ok=True)
        self.files_dir.mkdir(parents=True, exist_ok=True)

    def add_evidence(
        self,
        *,
        kind: EvidenceKind,
        source: str,
        locator: str,
        assertion: str,
        independent_group: str,
        file_path: Path | None = None,
        evidence_id: str | None = None,
        metadata: dict | None = None,
    ) -> EvidenceItem:
        if not all(value.strip() for value in (source, locator, assertion, independent_group)):
            raise ContractError("source, locator, assertion, and independent_group must be non-empty")
        evidence_id = evidence_id or f"ev-{uuid.uuid4().hex[:16]}"
        _validate_id(evidence_id, "evidence_id")
        destination = self.items_dir / f"{evidence_id}.json"
        if destination.exists():
            raise ContractError(f"evidence already exists: {evidence_id}")
        digest = None
        item_metadata = dict(metadata or {})
        if file_path is not None:
            source_file = file_path.resolve()
            if not source_file.is_file():
                raise ContractError(f"evidence file does not exist: {source_file}")
            safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", source_file.name)[:120] or "artifact.bin"
            stored_file = self.files_dir / f"{evidence_id}_{safe_name}"
            copy_file_atomic(source_file, stored_file)
            digest = sha256_file(stored_file)
            item_metadata["file_path"] = str(stored_file.relative_to(self.root)).replace("\\", "/")
            item_metadata["original_file_name"] = source_file.name
            item_metadata["file_size"] = stored_file.stat().st_size
        item = EvidenceItem(
            id=evidence_id,
            kind=kind,
            source=source,
            locator=locator,
            assertion=assertion,
            independent_group=independent_group,
            digest_sha256=digest,
            metadata=item_metadata,
        )
        write_json(destination, item.to_dict())
        return item

    def get_evidence(self, evidence_id: str) -> EvidenceItem:
        _validate_id(evidence_id, "evidence_id")
        path = self.items_dir / f"{evidence_id}.json"
        if not path.exists():
            raise ContractError(f"unknown evidence: {evidence_id}")
        value = load_json(path)
        try:
            return EvidenceItem(
                id=value["id"],
                kind=EvidenceKind(value["kind"]),
                source=value["source"],
                locator=value["locator"],
                assertion=value["assertion"],
                independent_group=value["independent_group"],
                digest_sha256=value.get("digest_sha256"),
                observed_at=value["observed_at"],
                metadata=value.get("metadata", {}),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise ContractError(f"invalid evidence document: {path}") from exc

    def create_claim(
        self,
        *,
        subject: str,
        predicate: str,
        object_value: str,
        evidence_ids: Iterable[str] = (),
        claim_id: str | None = None,
        notes: Iterable[str] = (),
    ) -> Claim:
        if not all(value.strip() for value in (subject, predicate, object_value)):
            raise ContractError("subject, predicate, and object must be non-empty")
        claim_id = claim_id or f"cl-{uuid.uuid4().hex[:16]}"
        _validate_id(claim_id, "claim_id")
        path = self.claims_dir / f"{claim_id}.json"
        if path.exists():
            raise ContractError(f"claim already exists: {claim_id}")
        evidence_list = list(dict.fromkeys(evidence_ids))
        for evidence_id in evidence_list:
            self.get_evidence(evidence_id)
        claim = Claim(
            id=claim_id,
            subject=subject,
            predicate=predicate,
            object=object_value,
            evidence_ids=evidence_list,
            notes=list(notes),
        )
        write_json(path, claim.to_dict())
        return claim

    def get_claim(self, claim_id: str) -> Claim:
        _validate_id(claim_id, "claim_id")
        path = self.claims_dir / f"{claim_id}.json"
        if not path.exists():
            raise ContractError(f"unknown claim: {claim_id}")
        value = load_json(path)
        try:
            return Claim(
                id=value["id"],
                subject=value["subject"],
                predicate=value["predicate"],
                object=value["object"],
                state=ClaimState(value["state"]),
                evidence_ids=list(value.get("evidence_ids", [])),
                contradiction_ids=list(value.get("contradiction_ids", [])),
                notes=list(value.get("notes", [])),
                created_at=value["created_at"],
                updated_at=value["updated_at"],
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise ContractError(f"invalid claim document: {path}") from exc

    def save_claim(self, claim: Claim) -> None:
        claim.updated_at = utc_now()
        write_json(self.claims_dir / f"{claim.id}.json", claim.to_dict())

    def attach_evidence(self, claim_id: str, evidence_id: str) -> Claim:
        claim = self.get_claim(claim_id)
        self.get_evidence(evidence_id)
        if evidence_id not in claim.evidence_ids:
            claim.evidence_ids.append(evidence_id)
            if claim.state is ClaimState.VERIFIED:
                claim.state = ClaimState.PROPOSED
            self.save_claim(claim)
        return claim

    def add_contradiction(self, claim_id: str, evidence_id: str) -> Claim:
        claim = self.get_claim(claim_id)
        self.get_evidence(evidence_id)
        if evidence_id not in claim.contradiction_ids:
            claim.contradiction_ids.append(evidence_id)
            claim.state = ClaimState.PROPOSED
            self.save_claim(claim)
        return claim

    def audit_evidence_integrity(self, item: EvidenceItem) -> list[str]:
        failures: list[str] = []
        file_path_raw = item.metadata.get("file_path")
        if item.digest_sha256 is not None:
            if not isinstance(file_path_raw, str):
                failures.append("digest exists but metadata.file_path is absent")
            else:
                file_path = Path(file_path_raw)
                if not file_path.is_absolute():
                    file_path = self.root / file_path
                file_path = file_path.resolve()
                try:
                    file_path.relative_to(self.root.resolve())
                except ValueError:
                    failures.append(f"evidence file escapes project root: {file_path}")
                    return failures
                if not file_path.is_file():
                    failures.append(f"evidence file is missing: {file_path}")
                elif sha256_file(file_path) != item.digest_sha256:
                    failures.append(f"evidence file hash changed: {file_path}")
        return failures

    def verify_claim(self, claim_id: str) -> dict:
        """Apply the strict verification gate and persist the resulting state.

        VERIFIED requires all of the following:
        - at least three evidence records;
        - at least three independent groups;
        - at least two evidence kinds;
        - no contradiction records;
        - every file-backed evidence hash still matches.

        This is a governance rule, not a mathematical guarantee that a claim is true.
        """
        claim = self.get_claim(claim_id)
        items = [self.get_evidence(evidence_id) for evidence_id in claim.evidence_ids]
        groups = {item.independent_group for item in items}
        kinds = {item.kind for item in items}
        integrity_failures = [
            failure
            for item in items
            for failure in self.audit_evidence_integrity(item)
        ]
        failures: list[str] = []
        if len(items) < 3:
            failures.append("fewer than three evidence records")
        if len(groups) < 3:
            failures.append("fewer than three independent evidence groups")
        if len(kinds) < 2:
            failures.append("fewer than two evidence kinds")
        if claim.contradiction_ids:
            failures.append("unresolved contradiction evidence exists")
        failures.extend(integrity_failures)

        if failures:
            claim.state = ClaimState.CORROBORATED if len(items) >= 2 else ClaimState.PROPOSED
        else:
            claim.state = ClaimState.VERIFIED
        self.save_claim(claim)
        return {
            "claim_id": claim.id,
            "state": claim.state.value,
            "evidence_count": len(items),
            "independent_group_count": len(groups),
            "evidence_kind_count": len(kinds),
            "failures": failures,
        }

    def require_verified(self, claim_id: str) -> Claim:
        result = self.verify_claim(claim_id)
        if result["state"] != ClaimState.VERIFIED.value:
            raise VerificationError(
                f"claim {claim_id} is not verified: {', '.join(result['failures'])}"
            )
        return self.get_claim(claim_id)
