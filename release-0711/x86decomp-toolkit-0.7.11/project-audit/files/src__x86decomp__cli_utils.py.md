# Per-file audit — src/x86decomp/cli_utils.py

## A. Identity
- Path: `src/x86decomp/cli_utils.py`
- SHA-256: `9ce4927c67b8bbc187f1a0c9bc97dd96bc1f9b0b7df2248ceae4e9860473b32b`
- Size: 3986 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 108 lines)
Shared CLI plumbing: CLI_ERROR_TYPES=(contracts.ContractError, KeyError, OSError, TypeError, ValueError); parse_json_arg (JSON→ContractError); emit_json (dataclass __dict__ unwrap, sorted, default=str); run_cli (parse→dispatch→emit, catch→JSON stderr, exit 2).

## C. Correctness — CLI-001 (verified)
CLI_ERROR_TYPES omits the toolkit's own error family `x86decomp.errors` (X86DecompError, FormatError, VerificationError, ExternalToolError). Direct evidence chain: pe.py:10 imports FormatError and raises it on malformed input (pe.py:192,207,210...); native/matching.py:98, native/pe_reconstruction.py:76+, native/slots.py:131, native/runtime.py:35 call parse_pe with no FormatError handling (grep-verified none in native/); canonical native routes dispatch through run_cli. Result: a malformed/truncated PE fed to any canonical native route raises FormatError → NOT in catch tuple → interpreter traceback, exit 1. The SAME file through root `inspect-pe` is caught (X86DecompError) → friendly error, exit 2. The module's own comment claims the uniform set prevents 'leaking an interpreter traceback' — internally contradicted. Also local_llm raises ExternalToolError through reconstruction llm routes with the same gap; assembly/relocations.py:291 proves FormatError occurs in assembly flows too (it locally catches one site only).
- emit_json's `hasattr(value,'__dict__')` unwrap: fragile for arbitrary objects (functions/classes would serialize their __dict__), but dispatchers return dicts/dataclasses in practice. Informational.

## D. Documentation
Exemplary (post-fix file).

## L. Findings
- CLI-001 (High, Verified statically; runtime demo scheduled Phase 10): canonical/subsystem CLIs crash with tracebacks on the toolkit's own domain errors (malformed binaries — the tool's PRIMARY untrusted input) because CLI_ERROR_TYPES omits X86DecompError family. Fix: add X86DecompError to CLI_ERROR_TYPES (and keep root cli.py aligned), or normalize errors at module boundaries.

## M. Verdict
Priority: immediate-to-near-term. Final status: Audited — complete.