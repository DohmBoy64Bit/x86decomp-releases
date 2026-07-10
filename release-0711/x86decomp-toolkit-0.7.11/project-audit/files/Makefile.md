# Per-file audit — Makefile

## A. Identity
- Path: `Makefile`
- SHA-256: `d034035386a8ab7bea1c7e4348d3608367b3ab890c0711a488d2bdbdb48806f7`
- Size: 1232 bytes | Type: text | Classification: configuration
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Developer entry points: verify = compile + contracts + verify-hashes + test; test runs `scripts/run-pytest-partitions.py` with PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 and PYTHONPATH=src:test-suite/src; hashes/verify-hashes call `scripts/source_hashes.py`; package/install/editable/clean.

## C. Correctness
- `verify-hashes` calls `scripts/source_hashes.py verify` — given REPO-001 (68 mismatches vs MANIFEST.sha256), `make verify` should currently FAIL at the verify-hashes step. To be verified by execution in Phase 10 (safe, read-only per script review pending B10). If confirmed, the shipped tree fails its own top-level `make verify` — direct corroboration of REPO-001 user impact.
- `clean` removes `test-suite/.x86decomp-test-tools` but not root `.x86decomp-test-tools` — consistent blind spot (REPO-003).
- Partitioned pytest runner exists specifically because monolithic pytest timed out upstream (RELEASE_VERIFICATION 'Not claimed') — see TEST-001.

## D. Documentation
Targets are conventional; no help target. Minor.

## L. Findings
- Supports REPO-001 impact; TEST-001 context.

## M. Verdict
Quality: good. Priority: medium (verify-hashes currently expected to fail). Final status: Audited — complete.