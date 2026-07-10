# Per-file audit — src/x86decomp/pdb.py

## A. Identity
- Path: `src/x86decomp/pdb.py`
- SHA-256: `cafd35f8251e24a91b6b01e36d651ef28b698fac11266a47c7daf9b5e9bd6179`
- Size: 26480 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 643 lines)
MSF 7.0 / PDB inventory + PE identity correlation. Local bounded reader (_require/_u16/_u32); MSF superblock (block size in {512,1024,2048,4096}), stream directory, TPI/IPI/DBI metadata; GUID/age extraction; matches PDB to a PE's debug record.

## C. Correctness (Verified)
- _require: `offset>len or size>len-offset` — overflow-safe (subtraction form). Block size allowlist. Caps _MAX_STREAMS/_MAX_BLOCKS/_MAX_MODULES/_MAX_SOURCE_CONTRIBUTIONS all present.
- Discontiguous stream blocks handled (per module docstring); unsupported variants fail explicitly rather than guessing — aligns with the project's evidence discipline.
- parse_pe imported for PE-side GUID correlation; FormatError family used consistently.

## K. Duplication — DUP-003
Reimplements bounded-reader primitives instead of using BinaryReader (CR-0710-007 consolidation didn't reach PDB). Behaviorally equivalent; adds a third copy of require/u16/u32.

## D. Documentation
Module docstring strong and appropriately humble about not doing full CodeView reconstruction. Helper docstrings template-only (DOC-001).

## H. Security
Untrusted-input surface; bounded; no dangerous constructs. math import used for block arithmetic (ceil) — check for div-by-zero: block size from allowlist (never 0), safe.

## M. Verdict
Quality: high. Security: strong. Final status: Audited — complete.