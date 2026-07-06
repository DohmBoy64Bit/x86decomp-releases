# x86decomp-toolkit 0.7.10 audit-fix report

## Scope

This release transaction applies fixes for every concrete issue recorded in the prior full code audit report. The sealed prior release artifacts were not rewritten; this is a forward 0.7.10 release built from the audited source baseline.

## Issue resolution matrix

| Audit issue | Finding addressed | Fix applied | Verification |
|---|---|---|---|
| CR-079-001 | Optional `angr` public API test assumed optional packages were installed. | Converted optional-backend tests to explicit `ExternalToolError` assertions when `angr`/`claripy` are missing while preserving full backend assertions when installed. Expanded the same dependency-adaptive pattern for Capstone, Unicorn, and Z3 tests found during validation. | `test_public_api_contract.py`, `tests/test_dynamic_symbolic.py`, `tests/test_abi_disassembly.py`, and production symbolic tests pass in this minimal environment without skips for those optional backends. |
| CR-079-002 | Adapter catalog marked optional toolkit extras as mandatory. | Marked `capstone`, `unicorn`, `z3`, `angr`, `fastapi`, `uvicorn`, and `lief` as optional adapters. | `tests/test_audit_fixes.py::test_optional_toolkit_extras_are_adapter_optional` passed. |
| CR-079-003 | Packaged self-test symlink behavior drifted from source self-tests. | Added the Windows symlink capability guard to the packaged adapter detection self-test. | Test-suite self-tests passed. |
| CR-079-004 | FastAPI read-only UI used `innerHTML` with project JSON. | Replaced `innerHTML` rendering with DOM nodes and `textContent`; added a CSP meta tag. | `tests/test_audit_fixes.py::test_service_index_uses_text_content_not_inner_html` passed. |
| CR-079-005 | Flat aliases duplicated canonical command behavior. | Marked `hybrid-generate` and `project-check` as explicit compatibility aliases; routed `hybrid-generate` through canonical dispatch. Kept `project-check` behavior unchanged because its validation path is not byte-for-byte equivalent to the assembly project check route. | `tests/test_release_contract.py::test_flat_compatibility_aliases_are_explicit` passed. |
| CR-079-006 | Duplicate JSON argument and store-row JSON decode helpers. | Added shared `cli_utils.parse_json_arg`, `cli_utils.emit_json`, and `store_utils.decode_json_fields`; rewired governance/native/reconstruction CLIs and stores to use them while keeping compatibility aliases for existing internal tests. | `tests/test_audit_fixes.py::test_store_decode_json_fields_shared_helper` passed; reconstruction CLI schema tests passed. |
| CR-079-007 | Production unused imports. | Removed the confirmed unused production imports and verified with an AST import-use check over `src` and `test-suite/src`. | Custom import-use check reported `unused_imports 0`. |
| CR-079-008 | `llm_batch_create` suppressed a secondary manifest ID read error. | Preserved the secondary exception in `function_id_error` when manifest ID extraction fails after the primary batch error. | `tests/test_audit_fixes.py::test_batch_create_records_secondary_manifest_id_errors` passed. |
| CR-079-009 | Generated/template-like docstrings remained. | Removed the flagged template phrases from AST docstrings and improved high-value helper docstrings added in the fix pass. | `tests/test_audit_fixes.py::test_no_template_docstring_phrases_remain` and `tests/test_docstring_audit.py` passed. |
| CR-079-010 | Mirrored corpus/example paths had drift risk and only positive integration coverage. | Added the negative integration candidate example and added/updated source-hash and release-contract verification so mirrored example/corpus files remain hash-checked. | Source manifest verification passed for 446 root files and 63 test-suite files; release contract tests passed. |
| CR-079-011 | Z3 dependency constraints disagreed. | Aligned toolkit extra and adapter catalog to `z3-solver>=4.15,<5`. | `tests/test_audit_fixes.py::test_optional_toolkit_extras_are_adapter_optional` passed. |

## Verification summary

- Python compile check: `python3 -m compileall -q src test-suite/src tests scripts` passed.
- Contract/example/schema/skill/Java validation: `scripts/validate-contracts.py` passed after installing declared dev dependency `javalang>=0.13,<1` in the validation environment.
- Source hashes: root manifest `446/446` valid; test-suite manifest `63/63` valid.
- Docstring audit: 208 modules, 160 classes, and 1441 functions/methods have docstrings; 0 missing.
- Command surface: 166 root commands, 59 canonical groups, 239 canonical routes.
- Wheel and source distribution builds passed for toolkit and test-suite.
- Clean wheel install into a fresh venv passed; `pip check` reported no broken requirements.

## Validation note

The monolithic `pytest tests/test_*.py` invocation did not complete reliably in this sandbox even though the same root tests passed in smaller deterministic groups and individual release-contract checks passed. I am not claiming a successful single-process full-suite run from that invocation. The release evidence uses the completed segmented test runs and the targeted audit-fix regression suite.
