# Per-file audit — ghidra_scripts/ExportFunctionArtifacts.java

## A. Identity
- Path: `ghidra_scripts/ExportFunctionArtifacts.java`
- SHA-256: `2c1a21482d49c2bdd2fcf86e6df9d3c401fc4e5e4c4a36ea358aa9e2ddf6ca49`
- Size: 24555 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 499 lines)
Ghidra headless post-script: exports per-function artifacts (decompiler C, decompiler-tree/high-pcode/raw-pcode jsonl, instruction/reference jsonl, raw range bytes) WITHOUT flattening discontiguous bodies. Output under canonicalized outputRoot/functions/<id>.

## C/H. Correctness/Security
- Read-only w.r.t. the program; only WRITES analysis artifacts under new File(args[0]).getCanonicalFile(). No Runtime.exec/ProcessBuilder (grep-verified). Function id ':'→'_' for path safety. body-range invariants (start<end, size) match the verify-ghidra.sh asserts and schema_version 2.
- javalang syntax validated by validate-contracts (R-018 PASS).

## M. Verdict
High quality; the RE-evidence exporter. Final status: Audited — complete.