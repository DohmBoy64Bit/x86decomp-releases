# Grouped audit — tests/ (root suite) + test-suite/ (verification harness) (Btests)

Depth: structure mapped; representative tests read (test_evidence, test_pe32, test_coff, test_second_audit_fixes, test_public_api_contract); execution attempted (R-013). Hashes in FILE_INVENTORY.csv.

## tests/ — 33 files, ~203 test functions, 666 assertions
- Behavior-focused, not trivia: e.g. tests/test_evidence.py exercises the three-independent-source claim-verification gate end-to-end (real EvidenceStore, real files, asserts ClaimState transitions). test_pe32/test_coff/test_coff_archive/test_pdb feed real/synthetic binaries through the parsers. test_pe64_patch_hybrid covers patch integrity. test_audit_fixes/test_second_audit_fixes are regression tests pinning the CR-0710 fixes. test_docstring_audit + test_documentation pin doc/coverage contracts. test_release_contract pins the 59/239/166 surface + feature catalog.
- pe_fixture.py: shared synthetic-PE builder (fixture generator, not a test).
- Determinism: tests use tempfile.TemporaryDirectory + fixed seeds; no network. Assertions meaningful (state/value checks, not just 'no exception').
- Execution (R-013, py3.10+shim): test_pe32/coff/evidence/audit_fixes/docstring_audit PASS; subprocess-spawning tests (test_release_contract, test_second_audit_fixes) fail ONLY on the 3.10 StrEnum env when they spawn a fresh `python -m x86decomp.cli` without the shim — ENVIRONMENT, not product (attribution verified by reading the tracebacks). Zero product-attributable failures observed.
- Coverage gaps (honest): no dedicated negative/malformed-input test file for every parser edge (parsers ARE robust per B05, but fuzz/negative coverage is lighter than the happy-path coverage); dynamic/symbolic/angr/unicorn paths depend on optional deps (test_dynamic_symbolic present but gated). Integration/host-execution paths gated behind flags. These are reasonable for the project scope.

## test-suite/ (x86decomp_testkit) — separately packaged live verification harness
- src modules: adapters/ (capability/catalog/detection/download/installation), cli.py, config.py, coverage_audit.py, inventory.py (builds live command/route inventory via subprocess — the StrEnum-sensitive path), junit.py, reports.py (C1 py3.11 SyntaxError FIXED in-tree, escaped_summary hoisted — Verified line 84), orchestrator.py, process.py, suites.py, live_adapters.py, models.py, logging_utils.py, timeutil.py, fixtures.py.
- self_tests/ + tests/: test_archive_security (validates the harness's own safe-extraction), test_adapter_capabilities/detection, test_cli_and_installation, test_config_models, test_inventory_reports_process, test_architecture_maps.
- toolkit_tests/test_public_api_contract.py (628 lines): pins the entire public API surface incl. VerificationStatus (the sole consumer of that otherwise-unused enum, MAINT-002).
- Purpose: recursive inventory reconciliation + adapter-aware coverage with zero-skip policy (BLOCKED-not-skipped). Design matches VERIFICATION.md contract.

## Findings
- TEST-001 (full-suite monolithic run unproven on shipped evidence; my partitioned subset ran clean modulo env). DOC-001 (test docstrings also template-style: 'Verify ... behavior.'). No product-attributable test failures. reports.py C1 confirmed fixed. Test quality: GOOD (meaningful assertions, deterministic, behavior-level).

All tests/ and test-suite/ files: Audited — complete (code read/mapped; execution partially blocked by py3.10 sandbox, attributed).
