# Per-file audit — MANIFEST.sha256

## A. Identity
- Path: `MANIFEST.sha256`
- SHA-256: `977b0b4835bea7e1da973f0efbc2b963fa4c80ffd00c73486405c7bafa788ed2`
- Size: 46097 bytes | Type: text | Classification: build or packaging (manifest)
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
449-entry SHA-256 manifest over release source files; consumed by `scripts/source_hashes.py verify` (per Makefile) and by external `sha256sum -c`.

## C. Correctness
- Format valid (sha256sum-compatible). Coverage: 449 of the 694 present files — by design excludes transient dirs, but present-tree extras (dist/, .pytest_cache/, project-audit/ (ours), x86decomp-test.json at root, .x86decomp-test-tools/) are unaccounted; acceptable for a source manifest.
- **68/449 entries FAIL against the actual tree** (RUN_LOG R-004, full list project-audit/manifest_failures.txt). Cause: post-release fix pass (responding to CODE_AUDIT_REPORT.md, itself dated after packaging) edited 68 files without regenerating the manifest. Corroboration: RELEASE_VERIFICATION.json records 449/449 PASS at packaging time; reports.py in-tree already contains the audit's C1 fix (hoisted escaped_summary, verified by direct read); mtimes of src/tests dirs postdate packaging docs. Confidence: mismatch Verified; cause Strongly supported.

## L. Findings
- REPO-001 (High) — this file is the primary evidence.

## M. Verdict
Priority: immediate (regenerate or re-release). Final status: Audited — complete.