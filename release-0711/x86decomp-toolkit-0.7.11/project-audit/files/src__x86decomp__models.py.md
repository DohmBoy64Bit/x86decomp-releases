# Per-file audit — src/x86decomp/models.py

## A. Identity
- Path: `src/x86decomp/models.py`
- SHA-256: `368f0a0db647232d1383f15045966d9278cc2428732b9a6bf3978c4984dd0451`
- Size: 3306 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 99 lines)
Stable enums (EvidenceKind, ClaimState, VerificationStatus — all StrEnum, well-documented members) + frozen EvidenceItem and mutable Claim dataclasses with to_dict().

## C. Correctness
- Claim.to_dict: asdict + state.value; evidence enum values serialize via kind.value — deterministic. StrEnum members WOULD serialize as strings anyway; explicit .value harmless.
- Claim default timestamps via field(default_factory=utc_now) — created_at/updated_at both stamped at construction; updated_at maintenance is the caller's job (evidence.py — B04 follow-up).
- VerificationStatus: grep across src/tests/test-suite/schemas finds ZERO runtime consumers; only test_public_api_contract.py pins its members as public API. Refines prior-audit L2: intentional public surface, but no code path produces or consumes it — an API promise without an implementation behind it. MAINT-002 (Low, Verified).

## L. Findings
- MAINT-002 (Low, Verified): VerificationStatus is exported+test-pinned but unused by any runtime path; either wire it into claim verification results or document it as reserved.

## M. Verdict
Final status: Audited — complete.