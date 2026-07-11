# Changelog

## 0.7.11 — Review-only audit remediation

- Made the documented verification path read-only: docstring reports are now deterministic, `--check` never rewrites them, and regeneration is an explicit update action.
- Added Python 3.11.0–3.11.3-compatible validated backup extraction while retaining the hardened `data` tar filter where the runtime supports it.
- Replaced abbreviated license notices with the complete Apache License 2.0 text and added NOTICE files to both distributions.
- Replaced all 364 audit-identified generic docstrings and expanded the audit gate to reject those template families.
- Generated a complete 405-node command reference covering all 166 root commands and 239 canonical routes, including arguments, defaults, output/error contracts, safety notes, examples, and use cases.
- Added normalized-AST synchronization checks for the six source/package self-test pairs.
- Added reproducible Ruff and Pyright dependencies, Makefile gates, and CI enforcement; corrected the type-contract defects exposed by those checks.
- Added `x86decomp --version`, removed all audited trailing whitespace, and added regression tests for every review finding.

## 0.7.11 — Complete docstring coverage and audit evidence

- Added professional docstrings to every audited Python module, class, function, and method across toolkit source, tests, test-suite source, test-suite tests, scripts, and Ghidra helper scripts.
- Added `DOCSTRING_AUDIT_0.7.11.json` and `DOCSTRING_AUDIT_0.7.11.md` with per-file SHA-256 coverage, per-definition docstring records, parser command-registration records, and three verification passes.
- Added `docs/COMMAND_REFERENCE_0.7.11.json` and `docs/COMMAND_REFERENCE_0.7.11.md` to bind command documentation to the live root and canonical command surfaces.
- Added regression coverage in `tests/test_docstring_audit.py` so missing docstrings or command-reference drift fail the test suite.
- Updated synchronized release, contract, skill, and architecture metadata to the 0.7.11 current-release baseline while preserving the adapter-capability surface from the previous baseline.

Earlier release history is retained in source-control tags and published release archives, not in the active 0.7.11 source tree.
