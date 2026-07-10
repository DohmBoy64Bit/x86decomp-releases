# Per-file audit — VERIFICATION.md

## A. Identity
- Path: `VERIFICATION.md`
- SHA-256: `607bda4645c43606226fd12e12bbfd52939c382d207c5770c70776df1514f180`
- Size: 1606 bytes | Type: text | Classification: documentation
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Release verification contract: compile/import, recursive schema+example validation, Java syntax validation for Ghidra scripts, exact inventory reconciliation, zero historical references, single entry points, zero-skip tests, body-execution audit, command process audit, coverage floors, build/install checks, deterministic ZIP reproduction, MANIFEST.sha256 verification; BLOCKED-not-skipped policy; adapter-capability note (duplicated text, DUP-001).

## C. Review
The contract's last line — 'Exact root and standalone test-suite MANIFEST.sha256 verification' — is violated by the current tree (REPO-001): by its own contract this tree is not a complete release. Verified consistency check.

## M. Verdict
Final status: Audited — complete.