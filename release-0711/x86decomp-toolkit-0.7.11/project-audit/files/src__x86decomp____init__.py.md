# Per-file audit — src/x86decomp/__init__.py

## A. Identity
- Path: `src/x86decomp/__init__.py`
- SHA-256: `08fb24b72cf16b71245c88f08254d76da25b0b9581ec070a23ca043ff2372f99`
- Size: 474 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Public package API (read fully, 13 lines): re-exports PE parsers, project init/verify, workflow enums; __version__ 0.7.11 (matches pyproject — Verified).

## C–K
Minimal and correct. Import of pe/pe32/project/workflow at package import time means `import x86decomp` pulls the parser stack — acceptable, stdlib-only. Public surface is pinned by test-suite test_public_api_contract.py (corroborated by grep). No findings.

## M. Verdict
Quality high. Final status: Audited — complete.