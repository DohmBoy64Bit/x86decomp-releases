"""Stable enums and dataclasses used by evidence and verification contracts."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from typing import Any

from .util import utc_now


class EvidenceKind(StrEnum):
    """Category of evidence backing a claim.

    Members:
        BINARY_BYTES: Raw bytes read directly from the analyzed binary.
        STATIC_ANALYSIS: Facts derived from static analysis without execution.
        DYNAMIC_TRACE: Observations captured while executing or emulating the target.
        COMPILER_OUTPUT: Artifacts produced by compiling reconstructed source.
        DEBUG_SYMBOL: Information recovered from debug symbols (e.g. PDB data).
        EXTERNAL_DOCUMENT: Facts sourced from external documentation or references.
        HUMAN_REVIEW: Assertions contributed by a human reviewer.
    """
    BINARY_BYTES = "binary_bytes"
    STATIC_ANALYSIS = "static_analysis"
    DYNAMIC_TRACE = "dynamic_trace"
    COMPILER_OUTPUT = "compiler_output"
    DEBUG_SYMBOL = "debug_symbol"
    EXTERNAL_DOCUMENT = "external_document"
    HUMAN_REVIEW = "human_review"


class ClaimState(StrEnum):
    """Lifecycle state of a claim as evidence accumulates.

    Members:
        PROPOSED: Claim has been asserted but not yet supported by evidence.
        CORROBORATED: Claim is backed by supporting evidence but not fully verified.
        VERIFIED: Claim has passed its verification criteria.
        REJECTED: Claim has been contradicted or otherwise ruled out.
    """
    PROPOSED = "proposed"
    CORROBORATED = "corroborated"
    VERIFIED = "verified"
    REJECTED = "rejected"


class VerificationStatus(StrEnum):
    """Outcome of running a claim's verification procedure.

    Members:
        NOT_RUN: Verification has not yet been attempted.
        FAILED: Verification ran and did not satisfy the claim.
        PASSED: Verification ran and satisfied the claim.
    """
    NOT_RUN = "not_run"
    FAILED = "failed"
    PASSED = "passed"


@dataclass(frozen=True)
class EvidenceItem:
    """Store validated evidence item fields used by toolkit reports and adapters."""
    id: str
    kind: EvidenceKind
    source: str
    locator: str
    assertion: str
    independent_group: str
    digest_sha256: str | None = None
    observed_at: str = field(default_factory=utc_now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        value = asdict(self)
        value["kind"] = self.kind.value
        return value


@dataclass
class Claim:
    """Store validated claim fields used by toolkit reports and adapters."""
    id: str
    subject: str
    predicate: str
    object: str
    state: ClaimState = ClaimState.PROPOSED
    evidence_ids: list[str] = field(default_factory=list)
    contradiction_ids: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        value = asdict(self)
        value["state"] = self.state.value
        return value
