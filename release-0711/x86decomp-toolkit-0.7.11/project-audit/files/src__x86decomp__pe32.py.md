# Per-file audit — src/x86decomp/pe32.py

## A. Identity
- Path: `src/x86decomp/pe32.py`
- SHA-256: `531e3625dfd0ee30ab9107d4f3a67dc7c1b2e11cde7f3c778745aae76d285f6b`
- Size: 45538 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 1,144 lines)
Strict dependency-free PE32 (i386) parser. _Reader = BinaryReader alias; _rva_to_offset (header/section mapping with zero-fill-tail + beyond-file rejection); _directory; _parse_imports/_exports/_relocations/_debug_records/_tls/_resources/_delay_imports/_load_config; parse_pe32 with full header validation. Dataclasses for every directory type.

## C. Correctness — hardened (Verified)
- _rva_to_offset: rejects RVA in zero-filled tail (delta>=raw_size), maps-beyond-file, and unmapped RVA — the correct, conservative behavior for adversarial images (many real-world PE exploits abuse RVA→offset). Excellent.
- Export parser: function_count/name_count capped at 1,000,000; ordinal_index>=function_count rejected (prevents OOB into function table); forwarder detection via directory range. Correct.
- Import/delay loops: for/else terminator enforcement; MAX_IMPORT_THUNKS cap. Resource parser: depth cap (>8), cycle detection (visited set), entry_budget=100,000, every offset require()-checked, UTF-16 name length bounded. This is textbook-safe recursive parsing.
- Relocation parser: while consumed<size with per-block 8-byte minimum + block-size validation.
- Minor: line 458 redefines `max_thunks = 1_000_000` locally instead of using module MAX_IMPORT_THUNKS (DRY nit, not a bug).

## D/E. Docs/Maintainability
Parser functions well-documented; dataclasses carry template docstrings (DOC-001). 1,144 lines but cohesive (single format). Nested helper functions (read_name/walk) keep resource logic local and readable.

## H. Security
No dangerous constructs. The strongest-hardened file in the tree. Handles null/empty/truncated/cyclic/oversized inputs explicitly.

## L. Findings
DOC-001 only; local-constant DRY nit (Informational).

## M. Verdict
Quality: excellent. Security: strong. Final status: Audited — complete.