"""Stable enums and dataclasses used by evidence and verification contracts."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from typing import Any

from .util import utc_now


class EvidenceKind(StrEnum):
    BINARY_BYTES = "binary_bytes"
    STATIC_ANALYSIS = "static_analysis"
    DYNAMIC_TRACE = "dynamic_trace"
    COMPILER_OUTPUT = "compiler_output"
    DEBUG_SYMBOL = "debug_symbol"
    EXTERNAL_DOCUMENT = "external_document"
    HUMAN_REVIEW = "human_review"


class ClaimState(StrEnum):
    PROPOSED = "proposed"
    CORROBORATED = "corroborated"
    VERIFIED = "verified"
    REJECTED = "rejected"


class VerificationStatus(StrEnum):
    NOT_RUN = "not_run"
    FAILED = "failed"
    PASSED = "passed"


@dataclass(frozen=True)
class EvidenceItem:
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
        value = asdict(self)
        value["kind"] = self.kind.value
        return value


@dataclass
class Claim:
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
        value = asdict(self)
        value["state"] = self.state.value
        return value
