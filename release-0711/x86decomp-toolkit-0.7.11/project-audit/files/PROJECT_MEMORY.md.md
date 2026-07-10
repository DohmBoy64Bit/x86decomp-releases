# Per-file audit — PROJECT_MEMORY.md

## A. Identity
- Path: `PROJECT_MEMORY.md`
- SHA-256: `c7b05ecb5a481d6d343bfa77201a2c3f8921f9771ab7c5e2398b068b374fbeb3`
- Size: 1828 bytes | Type: text | Classification: documentation
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Durable decisions: unified single-release product, single executables, 59/239 interface, capability packages, byte-form default, separate matching/functional state machines, additive namespaced schemas, BLOCKED-not-skipped adapters, consent for native execution, untrusted LLM output, MkDocs requirement; 0.7.11 adapter-capability note (lm-studio-http can satisfy OpenAI-compatible coverage without marking other providers installed).

## C. Review
Consistent with AGENTS.md/FEATURE_PARITY.md/SKILL.md — the same content is restated in 4+ files nearly verbatim (the '0.7.11 adapter-capability note' paragraph is duplicated word-for-word in PROJECT_MEMORY.md, VERIFICATION.md, FEATURE_PARITY.md, README.md). Synchronization-by-copy: a maintenance hazard flagged as DUP-001 (docs level).
MkDocs claim again without artifact (DOC-002).

## L. Findings
- DUP-001 (Low, Verified): identical multi-sentence blocks duplicated across ≥4 root docs; drift risk demonstrated by the fact that updating them all is already burdensome.

## M. Verdict
Final status: Audited — complete.