# Per-file audit — src/x86decomp/coff.py

## A. Identity
- Path: `src/x86decomp/coff.py`
- SHA-256: `4630e57a2d64ffb3d9961e044437d5fe5f0bb4811a2c9748515baf59b167f798`
- Size: 51950 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 1,394 lines)
COFF object parser (classic + BIGOBJ, i386/AMD64), COMDAT resolution, symbol extraction, deterministic synthesis. _parse_header, _read_string_table, _string_at, _decode_symbol/section_name, parse_coff_bytes/parse_coff, extract_symbol, resolve_comdats, write_synthetic_coff(_object). Rich aux-symbol/COMDAT/weak-external modeling.

## C. Correctness (Verified)
- parse_coff_bytes: machine allowlist; section_count in (0,1,000,000]; require() for section table, symbol table, each section's raw data, relocations (incl. NRELOC_OVFL overflow record with count-includes-self semantics correctly handled). String table: size>=4 enforced, _string_at rejects offset<4 or >=len and unterminated.
- extract_symbol: start/end range validated against section.raw_data; ambiguity → ContractError; size<=0 rejected; inferred end via next symbol or section end. Correct boundary logic.
- write_synthetic_coff: deterministic object emission (matching-decomp use); relocations passed as structured records. Round-trip tested (tests/test_coff.py green, R-013).

## D. Documentation
Module docstring strong and honest ('does not pretend a linked PE still contains every original COFF relocation'). BUT the 34 boilerplate docstrings here (highest in tree, R-006) — parse_coff_bytes:709 'Parse coff bytes for the current toolkit workflow', all _read_string_table/_string_at/_decode_* helpers template-only. DOC-001 concentration.

## E. Maintainability
Largest parser; dense but sectioned by concern. Some functions long (resolve_comdats). Acceptable for format complexity.

## H. Security
Untrusted-input surface; all reads bounded; no dangerous constructs. Synthesis path writes files via atomic writers.

## L. Findings
DOC-001 (heaviest concentration: 34 boilerplate/several degenerate). No correctness/security defects found.

## M. Verdict
Quality: high (code); Documentation: poor (boilerplate-heavy despite good module docstring). Final status: Audited — complete.