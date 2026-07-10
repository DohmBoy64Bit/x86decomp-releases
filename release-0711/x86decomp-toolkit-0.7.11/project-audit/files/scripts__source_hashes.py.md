# Per-file audit — scripts/source_hashes.py

## A. Identity
- Path: `scripts/source_hashes.py`
- SHA-256: `e09d431daa5e3986b435b5f6dd07b8357a47b6fff97c50e3fc1ddeb142013f19`
- Size: 5784 bytes | Type: text | Classification: build or packaging
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 161 lines)
Generate/verify deterministic SHA-256 manifests for root and test-suite. IGNORED_DIRECTORY_NAMES excludes .git/.pytest_cache/.x86decomp-test-tools/__pycache__/build/dist/test-results/tools/venv/egg-info; ignores .pyc/.pyo/.coverage/MANIFEST.sha256/PKG-INFO. verify_manifest reports hash mismatch + unlisted + stale.

## C. Correctness — Verified by execution (R-016)
MANIFEST line parse validates 64-hex digest, rejects dup paths. Coverage set matches what I computed independently. Running `verify` on the shipped tree returns valid=False: 68 hash mismatches (root) + 15 test-suite + CODE_AUDIT_REPORT.md unlisted. This IS the make verify-hashes gate and it FAILS on the shipped release — primary REPO-001 evidence, now from first-party tooling. The script itself is correct; the tree/manifest are out of sync.

## M. Verdict
Script quality: high. Final status: Audited — complete.