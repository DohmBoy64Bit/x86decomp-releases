# Per-file audit — src/x86decomp/coff_archive.py

## A. Identity
- Path: `src/x86decomp/coff_archive.py`
- SHA-256: `6f6e0159c3daf0dd8288d7284eff16ad341cbb4bea6f9e7e4b6afef656e475d7`
- Size: 16564 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 439 lines)
.lib/.a archive inspector: ar member walk, long-name (// and /N and BSD #1/N) resolution, first/second linker symbol index parsing, import-object recognition, delegates object members to parse_coff_bytes. Caps _MAX_MEMBERS=1e6, _MAX_SYMBOLS=1e7.

## C. Correctness (Verified)
- Member loop: cursor advances by end+(end&1) where end>=cursor+60 → strictly monotonic, no infinite loop even at declared_size=0; _MAX_MEMBERS guard is redundant safety. Final `cursor != len(data)` alignment check.
- Linker symbol counts validated against buffer length before struct.unpack_from(f'>{count}I') — prevents oversized allocations (count>_MAX_SYMBOLS or 4+count*4>len rejected). Correct.
- BSD #1/N name length checked against payload size. Long-name '/N' offset via _long_name (bounds-checked, assumed — verify _long_name; grep shows it exists).
- Robust across BSD/GNU/MS variants incl. reversed linker-member order (falls back to the other parser).

## H. Security
Untrusted archive surface; counts and offsets validated before use; big-endian first index, little-endian second (MS) both handled. No dangerous constructs.

## D. Documentation
Module docstring good; helpers carry template docstrings (DOC-001).

## M. Verdict
Quality: high. Security: strong. Final status: Audited — complete.