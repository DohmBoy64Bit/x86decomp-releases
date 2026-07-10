# Per-file audit — src/x86decomp/errors.py

## A. Identity
- Path: `src/x86decomp/errors.py`
- SHA-256: `5bb50a4d169960abdc486866d2e68c894d8c13da401361931d86991ff9f8030d`
- Size: 576 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 21 lines)
Toolkit exception family: X86DecompError base; FormatError (binary/document contract), ContractError (structured-data contract), VerificationError, ExternalToolError.

## C. Correctness — ARC-001
This ContractError (X86DecompError subclass) collides by name with x86decomp.contracts.ContractError (ValueError subclass). Two same-named, semantically overlapping exceptions with DIFFERENT base classes and different catchability: contracts.ContractError is caught by `except ValueError`; errors.ContractError is not. util.py raises errors.ContractError; contracts.py raises its own; cli_utils catches only contracts'. Which one a caller gets depends on which helper module the callee happened to import. Verified by direct reads + import grep (47 importers of contracts.ContractError; util.py imports errors.ContractError).

## L. Findings
- ARC-001 (Medium, Verified): duplicate ContractError types across errors.py/contracts.py with divergent hierarchies; direct contributor to CLI-001's catchability gap and a trap for every `except ContractError` in the codebase (which one is caught depends on the import).

## M. Verdict
Final status: Audited — complete.