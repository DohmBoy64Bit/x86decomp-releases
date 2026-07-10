# Per-file audit — src/x86decomp/msvc_metadata.py

## A. Identity
- Path: `src/x86decomp/msvc_metadata.py`
- SHA-256: `997eae04ff2b00d7c5f21b1d6d79bc0423d7dfcf3f409db2d51600ef7f3146bf`
- Size: 42909 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 1,106 lines)
Conservative MSVC C++ metadata recovery: RTTI (TypeDescriptor, CompleteObjectLocator, ClassHierarchyDescriptor, BaseClassArray), x64 unwind/UNWIND_INFO opcode decoding, SafeSEH table, TLS/CRT initializer scanning. Uses a `view` bounded reader; correlates PE + COFF + linker map evidence.

## C. Correctness (Verified by read + spot bounds)
- Every RTTI record returned only after internal pointers/counts/section relationships pass structural checks (module docstring claim matches code: FormatError on truncated UWOP_ALLOC_LARGE/save ops; SafeSEH count cap; section-scan ranges use max(0, raw_size-size+1) to avoid negative ranges).
- Unwind opcode decoder handles ALLOC_LARGE near/far forms and trailing-slot bounds (raise on overrun). Correct per x64 ABI.
- Pointer-scan loops stride by pointer_size within section bounds; slot cap range(512). No unbounded scans.
- Honest scoping: 'not a promise that original class names/layouts are recovered' — consistent with evidence governance.

## D. Documentation
Module + record docstrings good and specific about ABI derivation; some helpers template-style (DOC-001, lighter here).

## E. Maintainability
Largest analysis module (1,106 LOC); complex but well-sectioned by record type. RTTI/unwind are inherently intricate; complexity is essential, not accidental.

## H. Security
Untrusted-input; bounded; no dangerous constructs. re import used for symbol/name heuristics (static patterns, not user-supplied regex → no ReDoS from external input; confirm patterns are literals — they are compiled from constants).

## M. Verdict
Quality: high. Security: strong. Correctness confidence: high for the conservative scope claimed. Final status: Audited — complete.