# Per-file audit — src/x86decomp/pe.py

## A. Identity
- Path: `src/x86decomp/pe.py`
- SHA-256: `c8ef3aff7c297083327f35ddbb6fe6977e2bb709488c5479bfb53e4214a2093d`
- Size: 24516 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 504 lines)
PE32+ (x86-64) parser + architecture dispatcher. Dataclasses TLS64Info/RuntimeFunction/PE64Image; _parse_imports64/_tls64/_delay_imports64/_load_config64/_runtime_functions; parse_pe64; inspect_pe_kind (cheap machine/magic probe); parse_pe (dispatch to pe32/pe64). Reuses pe32's _Reader/_rva_to_offset/_parse_exports/_relocations/_resources/_debug.

## C. Correctness — thorough hardening (Verified by read)
- MZ + PE signature checks; machine==AMD64 enforced; section_count in (0,96]; optional magic==PE32_PLUS and optional_size>=112; every field read via bounded reader.
- Named safety caps MAX_IMPORT_THUNKS=1,000,000 / MAX_TLS_CALLBACKS=65,536 (prior-audit L1 fix — now named constants with docstrings). Import/TLS/delay loops use for/else → raise on missing terminator (no silent truncation). This directly resolves prior L1's 'silent truncation' concern for pe.py.
- Descriptor loops bounded by min(65_536, directory.size//stride+1); thunk offset math bounded by reader.u64 require().
- TLS/delay 'VA below image base' checks reject underflow before subtraction. Correct.
- Section name de-dup loop (`#suffix`) — terminates (finite section_count).
- _parse_runtime_functions rejects size%12!=0. Good.
- inspect_pe_kind: `len(data)<0x40` guard + `pe_offset+26>len(data)` before unpack — bounded even outside the _Reader. Correct.

## D. Documentation
Parser functions have full Args/Returns/Raises (post-fix quality). Dataclasses carry degenerate template docstrings ('Store validated t l s64 info fields...') — DOC-001 instances (cosmetic).

## E/G. Maintainability/Perf
- Section sha256 computed for every section on parse (sha256_bytes(data[raw_offset:raw_offset+raw_size])) — O(file) hashing always; fine for analysis, unnecessary if caller only wants headers. Minor; acceptable given provenance mission.
- pe.py duplicates pe32's import/TLS/delay logic at 64-bit width rather than parameterizing width — deliberate 32/64 split; some duplication (DUP-004, Low).

## H. Security
Primary untrusted-input surface. No eval/exec/pickle (grep-verified). All reads bounded. FormatError raised on every structural violation. Robust against the malformed PE class. The only cross-cutting concern is that FormatError isn't caught by subsystem CLIs (CLI-001) — a CLI-layer issue, not a parser issue.

## I. Testing
tests/test_pe32.py + test_pe64_patch_hybrid.py exercise parse paths (ran green, R-013). Malformed-input behavior runtime-verified clean via root (R-010).

## L. Findings
- DOC-001 (dataclass docstrings). DUP-004 (Low): 32/64 parser logic duplicated rather than width-parameterized.

## M. Verdict
Quality: excellent. Correctness confidence: high. Security: strong. Priority: none (parser); CLI-001 tracked separately. Final status: Audited — complete.