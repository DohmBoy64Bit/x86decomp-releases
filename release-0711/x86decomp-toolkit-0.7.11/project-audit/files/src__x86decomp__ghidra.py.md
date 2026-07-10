# Per-file audit — src/x86decomp/ghidra.py

## A. Identity
- Path: `src/x86decomp/ghidra.py`
- SHA-256: `a4b9ba54d680ccc858a4dbee991eb2462f2e003a49b28224588e2d4eea615474`
- Size: 3754 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 105 lines)
build_export_command (argv array for analyzeHeadless) + run_export (subprocess.run, no shell, timeout enforced, JSON report).

## C/H. Security
- Argument ARRAY, never shell — matches SECURITY.md control. ghidra_project_name validated against '/' and '\\'; binary/scripts existence checked; required scripts checked; all paths .resolve()d. timeout_seconds>0 enforced. function_selector passes through as a distinct argv element (no injection; it's the Ghidra script's input).
- ExternalToolError when analyzeHeadless absent — BLOCKED-not-skipped policy honored.

## M. Verdict
Exemplary subprocess construction. Final status: Audited — complete.