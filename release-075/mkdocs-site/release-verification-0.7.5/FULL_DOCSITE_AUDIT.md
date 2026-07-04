# Full documentation-site audit — x86decomp 0.7.5

**Status:** PASS

## Source-derived reference coverage

- **141** toolkit root commands
- **34** canonical capability groups
- **181** canonical routes
- **293** documented command paths
- **142** Python modules across toolkit and verification harness
- **1,019** functions and methods
- **223** distinct collected tests
- **97** JSON Schemas
- **36** adapter declarations
- **6** local-model provider presets
- **163** Project Example command lines parsed by the live CLI

## Built-site coverage

- Markdown source pages: **366**
- Built HTML pages: **367**
- Built files: **418**
- Search-indexed source pages: **366/366**
- Local links, fragments, scripts, styles, and assets checked: **20779**
- Errors: **0**

## Release evidence

- Distinct tests: **223/223 passed**
- Comprehensive harness: **191 PASS, 11 BLOCKED, 0 FAIL, 0 ERROR**
- Function/method body execution: **879/879**
- Statement coverage: **78.89%**
- Branch coverage: **51.73%**
- Root source manifest: **427/427**
- Test-suite source manifest: **60/60**

## Zero-inference policy

Command pages are generated from the live argparse trees. Module/function pages are generated from the source AST and exact docstrings. Tests come from pytest collection and source AST locations. Schemas, adapters, provider presets, manifests, and Project Example evidence ledgers are read directly from current files. Missing docstrings are identified as missing rather than replaced with inferred behavior.

## Truth boundary

This audit proves the enumerated source, parser, AST, schema, adapter, test, manifest, link, search, and build contracts. It does not prove original-source recovery, universal semantic equivalence, or live model quality for an unavailable inference runtime.
