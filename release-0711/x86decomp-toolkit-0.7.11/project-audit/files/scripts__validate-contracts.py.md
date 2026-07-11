# Per-file audit — scripts/validate-contracts.py

## A. Identity
- Path: `scripts/validate-contracts.py`
- SHA-256: `f03c8ca2c28e9925a2e6d08acd41b2d330bf85369acc35f52e1904723810e4d5`
- Size: 6875 bytes | Type: text | Classification: build or packaging
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 156 lines)
Release contract gate: validate every schema against Draft202012 meta-schema, validate examples, Java syntax (javalang), pyflakes static lint (CR-0710-004/009), skill + release-shape checks (reads pyproject via tomllib).

## C. Correctness — Verified by execution
- All 97 schemas pass meta-schema validation (R-017, independent run: 97 valid/0 invalid).
- Full gate PASSES with the compat shim (R-018): 'current contracts, examples, Java syntax, static lint, schemas, skill, and release shape passed', exit 0. Without shim it ModuleNotFoundErrors on tomllib (py3.10 env only). CR-0710-009 javalang diagnostic present.
- Note: this gate validates structure/lint/shape — it does NOT run the test suite and does NOT verify MANIFEST.sha256, which is why it passes while source_hashes verify fails (REPO-001). Illustrates the gate-coverage gap behind TEST-001/REPO-001.

## M. Verdict
High quality. Final status: Audited — complete.