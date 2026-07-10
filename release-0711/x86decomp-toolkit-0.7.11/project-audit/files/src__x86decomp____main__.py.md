# Per-file audit — src/x86decomp/__main__.py

## A. Identity
- Path: `src/x86decomp/__main__.py`
- SHA-256: `cd307c2c0d8d783cc42355eb7a64ec5a09987b0c0d63e873ae7adc0c67af2b04`
- Size: 134 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
`python -m x86decomp` shim (read fully, 4 lines): imports cli.main, raises SystemExit(main()) at module level.

## C. Correctness
No `if __name__ == "__main__"` guard — any tooling that imports x86decomp.__main__ (rather than executing it) would run the CLI. Convention varies on this; runpy only executes it as __main__, so practical risk is limited to unusual imports (e.g., pydoc x86decomp.__main__). Informational.

## M. Verdict
Final status: Audited — complete.