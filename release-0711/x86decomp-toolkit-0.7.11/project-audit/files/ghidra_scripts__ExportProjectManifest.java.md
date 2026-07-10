# Per-file audit — ghidra_scripts/ExportProjectManifest.java

## A. Identity
- Path: `ghidra_scripts/ExportProjectManifest.java`
- SHA-256: `136d6c725b1dcf122e4cc650f2a008c2dbbaf5322c3e943657074cb3c73d2653`
- Size: 15263 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 307 lines)
Exports program/section/function/symbol/metric manifests + executable sha256/size. Read-only queries; writes JSON under canonicalized output root; MessageDigest sha256 for provenance. No exec/Runtime. javalang-valid.

## M. Verdict
Final status: Audited — complete.