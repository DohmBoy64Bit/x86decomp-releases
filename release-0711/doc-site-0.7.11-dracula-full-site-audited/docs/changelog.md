---
title: Changelog
description: Changelog summary for x86decomp 0.7.11.
---

# Changelog

# Changelog

## 0.7.11 — Complete docstring coverage and audit evidence

- Added professional docstrings to every audited Python module, class, function, and method across toolkit source, tests, test-suite source, test-suite tests, scripts, and Ghidra helper scripts.
- Added `DOCSTRING_AUDIT_0.7.11.json` and `DOCSTRING_AUDIT_0.7.11.md` with per-file SHA-256 coverage, per-definition docstring records, parser command-registration records, and three verification passes.
- Added `docs/COMMAND_REFERENCE_0.7.11.json` and `docs/COMMAND_REFERENCE_0.7.11.md` to bind command documentation to the live root and canonical command surfaces.
- Added regression coverage in `tests/test_docstring_audit.py` so missing docstrings or command-reference drift fail the test suite.
- Updated synchronized release, contract, skill, and architecture metadata to the 0.7.11 current-release baseline while preserving the adapter-capability surface from the previous baseline.

Earlier release history is retained in source-control tags and published release archives, not in the active 0.7.11 source tree.


## Documentation site update

- Updated the site from the 0.7.10 baseline to the 0.7.11 second-audit fix release.
- Regenerated parser-derived command pages, source coverage, schema references, module pages, function index, test references, release artifacts, search metadata, and sitemap output.
