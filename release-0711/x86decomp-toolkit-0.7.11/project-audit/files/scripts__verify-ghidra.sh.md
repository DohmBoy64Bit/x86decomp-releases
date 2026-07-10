# Per-file audit — scripts/verify-ghidra.sh

## A. Identity
- Path: `scripts/verify-ghidra.sh`
- SHA-256: `254ae110f3a9b12b33ca77c698d7185792c180139fcef31017e400523440e111`
- Size: 2098 bytes | Type: text | Classification: build or packaging
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully)
Requires GHIDRA_HOME; runs analyzeHeadless with the two export scripts, then a Python inline validator that JSON-parses every exported manifest/jsonl and asserts schema_version==2, body-range invariants (start<end, size==end-start), artifact existence. `rm -rf "$WORK/project" "$WORK/export"` — scoped to the user-provided WORK dir (documented usage); safe given argument contract. `set -eu`.

## H. Security
rm -rf on WORK subdirs is destructive but bounded to the caller-named work dir; acceptable for a dev verify script. argv arrays to analyzeHeadless (no shell interpolation of the binary path beyond standard quoting).

## M. Verdict
Final status: Audited — complete.