# Per-file audit — src/x86decomp/binary_reader.py

## A. Identity
- Path: `src/x86decomp/binary_reader.py`
- SHA-256: `484e3667fb7a5301501d453e8393264f10d8bc9f2d76810405cd16038faa04e4`
- Size: 2867 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 61 lines)
Shared bounded reader (CR-0710-007 fix artifact): require() range check with negative-guard and offset+size>len; unpack via struct.calcsize+unpack_from; u16/u32/u64; c_string (bounded NUL scan, max_length 4096, UTF-8 replace); optional_u16/32/64 for size-gated record fields.

## C. Correctness — strong
- require(): `offset<0 or size<0 or offset+size>len(data)`. Python bigints mean no integer overflow; negative guard present. Solid.
- c_string: end_limit=min(len,offset+max_length); find NUL in [offset,end_limit); raises on unterminated → prevents runaway reads. Correct.
- optional_* gate on `available>=relative+N` — correct partial-record handling for truncated load-config etc.

## H. Security
This is the trust-boundary primitive for all untrusted-binary parsing; its correctness underpins pe/pe32/coff. No issues found. errors="replace" avoids decode crashes on hostile bytes.

## K. Duplication
pdb.py reimplements the same _require/_u16/_u32 locally instead of using BinaryReader (DUP-003); msvc_metadata uses a `view` reader; both bounds-check correctly but the CR-0710-007 consolidation was applied to PE/COFF only, not PDB/metadata.

## M. Verdict
Quality: excellent. Correctness confidence: high. Final status: Audited — complete.